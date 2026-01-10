---
title: Un hack d'efficacité majeur en 5 lignes pour vos résolveurs de types d'API
  GraphQL
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-08T14:16:56.000Z'
originalURL: https://freecodecamp.org/news/a-5-line-major-efficiency-hack-for-your-graphql-api-type-resolvers-b58438b62864
coverImage: https://cdn-media-1.freecodecamp.org/images/1*_5uB_PojUyPvVW0UkpMDUw.jpeg
tags:
- name: Apollo GraphQL
  slug: apollo
- name: efficiency
  slug: efficiency
- name: GraphQL
  slug: graphql
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Un hack d'efficacité majeur en 5 lignes pour vos résolveurs de types d'API
  GraphQL
seo_desc: 'By Vampiire

  Using Apollo Server and Postgres — Sequelize, we’ll create a proof of concept exploiting
  the info parameter of the resolver function for a 94% reduction in database load
  on Type queries*.

  If you are already familiar with the Apollo Server...'
---

Par Vampiire

En utilisant Apollo Server et Postgres — Sequelize, nous allons créer une preuve de concept exploitant le paramètre info de la fonction de résolution pour une réduction de 94 % de la charge de la base de données sur les requêtes de Type*.

Si vous êtes déjà familiarisé avec la signature du résolveur Apollo Server et son paramètre `info` et que vous souhaitez [**passer directement au hack, cliquez ici**](https://medium.com/@vampiire/a-5-line-major-efficiency-hack-for-your-graphql-api-type-resolvers-b58438b62864#a693). Merci à mon ami inquisiteur [Sloan Brantley Gwaltney](https://www.freecodecamp.org/news/a-5-line-major-efficiency-hack-for-your-graphql-api-type-resolvers-b58438b62864/undefined) pour m'avoir mis sur la piste du potentiel du paramètre `info`.

### Contexte — La signature de la fonction de résolution

Apollo Server fournit la signature de fonction de résolution suivante [d'après leur documentation](https://www.apollographql.com/docs/graphql-tools/resolvers#Resolver-function-signature) :

```
fieldName(obj, args, context, info) { result }
```

En avril, j'ai écrit quelques notes sur la signature pour enseigner à des coéquipiers qui étaient nouveaux dans GraphQL / Apollo Server. Voici ma version (légèrement) modifiée de la signature :

```
(instance, arguments, context, info) { ...returning data... }
```

#### `**instance**`

> _obj / root / instance_  
> _— Type GraphQL associé au résolveur_  
> _— uniquement utilisé dans les résolveurs de champs personnalisés de Type (pour d'autres Types / champs renommés)_  
> _— existe en tant qu'**instance** du **Modèle de base de données** correspondant au Type_

> `ex:`  
> `Type: User`  
> `Model: User, instance est 'user'`  
> `Résolveur de champ personnalisé de Type:`   
> `user => user.property/.relationshipGette`r()

#### `**arguments**`

> _arguments / Input object_  
> _— arguments pour la Query ou la Mutation_  
> _— typiquement sous la forme d'un objet de Type Input [définis dans le Schéma]_  
> _— Les Inputs sont des objets réutilisables qui peuvent contenir de nombreux champs, dont un sous-ensemble est approprié pour chaque résolveur_  
> _— inputs flexibles qui peuvent être utilisés pour les résolveurs de Query et de Mutation_  
> _— la déstructuration dans le résolveur permet la sélectivité des champs de l'objet Input_

> `ex:`  
> `UserInput: { id, username, avatar, githubID }`   
> `resolver: (root, { id }) => User.findById(id);`  
> `// déstructure 1 des 4 champs UserInput`

#### `**context**`

> _context / ctx_  
> _— l'objet context est injecté à l'exécution dans la déclaration du middleware Apollo de app.js_  
> _— c'est le plus polyvalent des paramètres du résolveur_  
> _— permet de passer des choses comme des fonctions utilitaires, des modèles de base de données, un utilisateur authentifié, et ainsi de suite_  
> _— en passant ces éléments dans le contexte, vous n'avez plus besoin de déclarations 'require' pour les modèles et les helpers. Ils sont accessibles directement depuis le résolveur._  
> _— typiquement défini comme un objet de nesting avec chaque sous-contexte ayant son propre objet_

#### `**info**`

> _aucune idée ?_

...C'était jusqu'à une conversation serendipiteuse avec Sloan qui a conduit à discuter de ce paramètre **inutile**. Sloan a mentionné qu'il contenait des informations sur la Query entrante. Cela a fait tourner mes engrenages pour améliorer l'efficacité du résolveur.

### Le paramètre info

L'objet `info` contient des détails sur l'ensemble de votre Schéma d'API et d'autres éléments que j'imagine Apollo Server utilise pour le traitement. En particulier, il contient des informations sur la Query elle-même — spécifiquement l'ensemble des champs de Type demandés.

#### Sequelize et le conte de la grosse inefficacité

Il s'avère que lorsque Sequelize (et je crois tous les autres OR/DM*) résout des lignes ou des documents, il le fait dans leur intégralité. À l'avant / à l'extrémité de réception, les données sont effectivement réduites selon les spécifications. Mais à l'arrière, le processus semble être :

`Requête DB pour la ligne/doc **entière**` → `map / résolveur personnalisé des champs demandés` → `filtrer les données et résoudre les champs demandés`

Cela a été prouvé avec un echo Postgres que j'ai exécuté depuis Sequelize sur une requête User :

```
SELECT "id", "role", "email", ...wtf Sequelize..., "timezone", "country_id", "city_id", "created_at", "updated_at" FROM "users" AS "User" WHERE "User"."github_username" = 'the-vampiire' LIMIT 1;
```

La requête Postgres **sélectionne** **tous les 17 champs** tandis que la requête API elle-même n'en demande qu'un :

`user(username:"the-vampiire") { id }`

#### Creuser dans l'objet info

Avec un peu de creusement dans l'objet `info`, j'ai pu atteindre ma cible : les champs demandés. Ma théorie était que si je connaissais les champs, je pourrais les passer en tant que propriété `attributes` de l'objet de requête Sequelize pour réduire la charge sur le serveur Postgres.

`info.fieldNodes[].selectionSet.selections[].name.value`

#### notes

* `fieldNodes` est un tableau avec l'élément `0th` étant la première requête. Mon hypothèse est que c'est un tableau pour supporter les requêtes par lots.
* `selections` est un tableau avec des objets pour chaque champ demandé du Type
* le nom du champ lui-même est enterré sous `selections.name.value`

### Le Hack

Alors, que signifie tout cela ? Eh bien, avec quelques lignes de code, un Modèle (du contexte bien sûr !), et l'argument `info`, j'ai écrit l'utilitaire et la preuve de concept suivants. Il utilise la propriété `attributes` de Sequelize de l'objet de requête pour obtenir des données uniquement à partir des colonnes demandées.

L'utilisation de cet utilitaire a entraîné une **réduction de 94 % de la taille de la requête**. Cela, bien sûr, s'adapte au nombre de champs demandés.

L'un des principaux avantages connus de l'utilisation d'une API GraphQL est qu'elle permet à l'avant de demander une charge utile de la forme et de la taille exactes nécessaires.

L'utilisation de mon utilitaire permet à l'arrière de refléter les mêmes avantages en réduisant de manière similaire la charge sur le serveur de base de données.

Les première et dernière lignes de la fonction `mapAttributes` garantissent que seuls les champs du Modèle directement mappés sont passés en tant qu'`attributes` à l'objet de requête.

Cela prévient les erreurs qui surviennent lors de la demande de champs qui n'existent pas en tant que colonnes sur le Modèle.

Celles-ci surviennent à partir de champs qui nécessitent des résolveurs de champs de Type personnalisés (comme les relations de Type ou les noms de champs de Type personnalisés).

#### Preuve de concept

`Requête de Type User : user(username:"the-vampiire") { id }`

`avant` → tous les 17 champs de la table User sont interrogés

```
SELECT "id", "role", "email", ...wtf Sequelize..., "timezone", "country_id", "city_id", "created_at", "updated_at" FROM "users" AS "User" WHERE "User"."github_username" = 'the-vampiire' LIMIT 1;
```

`après` → seul le champ unique demandé est interrogé

```
Executing (default): SELECT "status", "id" FROM "users" AS "User" WHERE "User"."github_username" = 'the-vampiire' LIMIT 1;
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*uY5yPukkf28oxZUtcQVXFw.jpeg)
_Ce hack est officiellement approuvé par The Dude_

### Mises en garde*

* Je n'ai pas testé cela avec Mongoose ou d'autres OR/DM populaires, mais en principe, l'effet devrait être le même. La fonction `mapAttributes` et l'objet de requête auraient simplement besoin de quelques personnalisations.
* Je n'ai pas testé cela avec des requêtes par lots avec différents champs demandés (cela peut affecter la propriété `fieldNodes` de `info`).
* Ne fonctionne pas avec les résolveurs de champs de Type personnalisés pour les champs renommés
* Les avantages s'adapteront au ratio des champs de Type demandés par rapport au nombre total de champs sur le Modèle correspondant.

— Vamp