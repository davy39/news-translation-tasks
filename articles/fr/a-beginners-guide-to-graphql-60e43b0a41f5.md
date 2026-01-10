---
title: Un guide sur GraphQL en français simple
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-17T00:13:12.000Z'
originalURL: https://freecodecamp.org/news/a-beginners-guide-to-graphql-60e43b0a41f5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*PpKiiMujrwHszBHWoZDqPQ.jpeg
tags:
- name: api
  slug: api
- name: GraphQL
  slug: graphql
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: technology
  slug: technology
seo_title: Un guide sur GraphQL en français simple
seo_desc: 'By Luis Aguilar

  All you need to know about the latest buzzword that’s taking the API development
  scene by storm.


  TL;DR

  GraphQL is a query language and runtime that we can use to build and expose APIs
  as a strongly-typed schema instead of hundreds of...'
---

Par Luis Aguilar

#### Tout ce que vous devez savoir sur le dernier mot à la mode qui fait fureur dans le monde du développement d'API.

![Image](https://cdn-media-1.freecodecamp.org/images/1*PpKiiMujrwHszBHWoZDqPQ.jpeg)

### TL;DR

_GraphQL_ est un langage de requête _et_ un runtime que nous pouvons utiliser pour construire et exposer des API sous forme de schéma fortement typé au lieu de centaines de points de terminaison REST. Vos clients voient le schéma. Ils écrivent une requête pour ce qu'ils veulent. Ils l'envoient et reçoivent exactement les données qu'ils ont demandées et rien de plus.

Un schéma ressemble à ceci :

<script src="https://gist.github.com/ldiego08/8492502e3d95a9beaa3415fe53b959c8.js"></script>

Ainsi, si un client veut un utilisateur avec un ID de 2, au lieu de faire un `GET /api/v1/users/2`, il enverrait plutôt une requête comme ceci :

<script src="https://gist.github.com/ldiego08/4220bbfff7ce646c906f4c818a742bbf.js"></script>


... et obtenir une réponse comme ceci :

<script src="https://gist.github.com/ldiego08/cc5294ae03f7876fea2f5b0685ccb613.js"></script>

Pourquoi REST devrait-il surveiller ses arrières, et pourquoi devriez-vous vous en soucier ?

1. **Le schéma est fortement typé.** Le schéma dicte que le paramètre `id` doit être un entier. Si un client envoie `user(id: "2")` à la place, le moteur GraphQL rejettera toute la requête.
2. **Les clients choisissent ce dont ils ont besoin.** Vous voyez ces accolades après les paramètres de la requête ? C'est ainsi que nos clients indiquent quels champs ils veulent. Moins de champs = réponses plus légères et plus rapides.
3. **C'est rapide.** Les champs non sélectionnés ne seront pas traités, ce qui signifie moins de stress sur le serveur.
4. **Et surtout, c'est flexible.** Si un client a besoin de moins de champs depuis un point de terminaison, nous ne créons pas un nouveau point de terminaison ou ne versionnons pas toute notre API exclusivement pour ce besoin. Ils peuvent choisir les champs dont ils ont besoin, et c'est gratuit pour nous.

Et c'est tout, vraiment. Pas de magie. Juste une manière plus pratique, flexible et naturelle de construire votre API.

Mais qu'est-ce que la vie sans ces concepts fondamentaux juteux et ces exemples de code sucrés ?

### Les Cinq Grands

Avant de passer au vrai plaisir, il y a quelques concepts que nous devons avoir en tête, sinon rien d'autre n'aura de sens.

Ne vous inquiétez pas, je vais faire court.

#### **Requête**

Un membre du schéma qui lit les données.

<script src="https://gist.github.com/ldiego08/41e5d69e45c31198fb86e210581192e2.js"></script>

#### **Mutation**

Un membre du schéma qui modifie les données (c'est-à-dire créer, éditer ou supprimer.)

<script src="https://gist.github.com/ldiego08/955d4ab670a88441aa3e9b588b2a32fc.js"></script>

#### **Schéma**

Un arbre à racine unique avec deux nœuds principaux : un pour les requêtes, et un autre pour les mutations.

<script src="https://gist.github.com/ldiego08/50e1b0913d75d5e5a8264a1154c74fe5.js"></script>

#### Type

La forme de tout ce qui compose le schéma. Les données retournées par une requête, les champs de ces données, les paramètres pris par une mutation, les requêtes et les mutations elles-mêmes—tout a un type.

<script src="https://gist.github.com/ldiego08/44d713c8c41d9314b9bbeb16c444f65d.js"></script>

Les types sont composés de champs qui ont également un type.

Les nœuds initiaux `query` et `mutation` sont de type `Query` et `Mutation` respectivement. Ceux-ci ont plus de champs, `users` et `user`, et leur type peut également avoir plus de champs ! C'est ainsi que vous structurez vos données d'API en un arbre interrogeable.

<script src="https://gist.github.com/ldiego08/d54644fc52f0e7b4cdb903baebe4f6c8.js"></script>

#### Résolveur

La pièce réelle qui connecte votre code à votre schéma. Les résolveurs sont des fonctions réelles qui _résolvent_ la valeur d'un seul champ dans un type. Ce qui suit est un exemple très, **très** basique de pseudo-code de son fonctionnement—ne vous en souciez pas trop.

<script src="https://gist.github.com/ldiego08/4d48f724f8cca7bdff607acb7d0da927.js"></script>

Facile, non ? Eh bien, c'est tout pour la théorie, il est temps pour un peu de code !

### Un exemple de code totalement original et pas du tout surutilisé

Fatigué de l'exemple classique de code de modèle d'utilisateur ? Moi non plus ! D'accord, cela peut être ennuyeux et sans intérêt, mais cela sert bien à illustrer les concepts précédents, alors restons-y. À la fin, nous aurons une API que les clients pourront interroger pour les utilisateurs, les rôles et créer de nouveaux utilisateurs.

#### 1. Créer un serveur

Comme déjà mentionné, GraphQL est un langage, _et_ un runtime—nous devons encore le mettre quelque part. Pour cet exemple, il vivra dans un serveur Express.

Alors, commençons :

* Créez un nouveau dossier.
* Ouvrez un terminal et `cd` vers votre dossier.
* Exécutez `npm init && touch server.js`
* Exécutez `npm i express --save` pour, eh bien, installer ExpressJS.
* Mettez ceci dans `server.js` :

<script src="https://gist.github.com/ldiego08/4d48f724f8cca7bdff607acb7d0da927.js"></script>

* Exécutez le serveur avec `node server.js`

Et ainsi nous avons un foyer pour notre API GraphQL.

#### 2. Ajouter une pincée de GraphQL

Aussi simple que :

* Exécutez `npm i graphql graphql-express --save`
* Modifiez `server.js` comme ceci :

<script src="https://gist.github.com/ldiego08/f5d94ce7b4b6db44f6cbb7e578172337.js"></script>

Et c'est pourquoi il était essentiel de passer en revue les concepts avant de passer au code. Cette simple application Hello World a déjà **beaucoup** de choses en cours, mais nous pouvons au moins avoir une idée.

Ne vous inquiétez pas, voici la version annotée :

<script src="https://gist.github.com/ldiego08/bb627e0f0dd0e4fbc46e3c950564681d.js"></script>

> _Attendez, codons-nous notre schéma en utilisant une énorme chaîne magique ? Ne paniquez pas—nous y viendrons plus tard._

D'accord, il est temps de lancer Postman et d'envoyer quelques requêtes à notre API GraphQL !

Heh, je plaisante...

À la ligne `46`, nous avons activé GraphiQL (prononcé _"graphical"_), un IDE intégré et complet pour écrire des requêtes. Maintenant, fermez Postman et allez sur `localhost:4000/graphql` dans votre navigateur préféré.

![Image](https://cdn-media-1.freecodecamp.org/images/1*kilXLXH_EGVuMulfFfiYPg.png)
_GraphiQL : la meilleure chose depuis la [taxe IE7](https://www.wired.com/2012/06/retailer-taxes-customers-still-using-internet-explorer-7/" rel="noopener" target="_blank" title=")._

Que pouvez-vous faire avec cela ? Eh bien, voici quelques choses que vous pouvez essayer :

* **Voir le schéma.** À droite, sélectionnez le type racine `Query` pour voir ses champs, types de retour, documentation, etc.
* **Écrire des requêtes.** À gauche, tapez la requête suivante, et remarquez comment l'éditeur montre l'autocomplétion et la documentation au fur et à mesure :

<script src="https://gist.github.com/ldiego08/50bb8897229d3de0121f3a8a8c58cdee.js"></script>

* **Tester des requêtes.** Si votre requête est valide, appuyez sur ce bouton de lecture en haut et voyez les résultats dans le panneau central.

![Image](https://cdn-media-1.freecodecamp.org/images/1*DnfYdpMnUbIGAwshyLL5yw.gif)
_GraphiQL : Le Nouveau Meilleur Ami de Tout le Monde_

Mais qu'en est-il des clients ? Ils peuvent utiliser Graph_i_QL (ou un outil similaire—il y en a des tonnes) pour construire et tester leurs requêtes. Ensuite, les envoyer en utilisant un client GraphQL comme Apollo Boost—aussi facile que copier et coller !

#### 3. Ajouter une requête pour lister les utilisateurs

D'accord, Hello World est bien et tout, mais nous voulons faire plus que saluer les gens. Ajoutons un nouveau type `User`, et remplaçons `hello` par `users` qui retournera tous les utilisateurs d'un dépôt factice.

* Modifiez `server.js` comme ceci :

<script src="https://gist.github.com/ldiego08/768a065d0a65973fa708fe82b86d5cdd.js"></script>

* Récupérez le fichier `user-repository.js` depuis [ici](https://github.com/ldiego08/workshops-graphql/blob/2-with-repository/user-repository.js) et mettez-le dans votre répertoire local.
* Redémarrez votre serveur et actualisez l'éditeur Graph_i_QL.
* Dans votre requête, remplacez `hello` par `users { id, login }` et appuyez sur play.
* **Profit.**

![Image](https://cdn-media-1.freecodecamp.org/images/1*i6jTWR6tXLF_7ypl9hoK_g.gif)
_Construire une Requête : Aussi Facile que 1–2–3._

Annoté :

<script src="https://gist.github.com/ldiego08/a9705fa26ee350d7d94c2981acf95782.js"></script>

#### 4. Ajouter une requête pour obtenir un seul utilisateur par ID

À ce stade, vous pourriez vous demander : si les requêtes sont également des champs d'un type, pourquoi ne pas les appeler des champs ? Qu'est-ce qui les rend différentes ?

**Les requêtes peuvent prendre des paramètres et utiliser un résolveur.**

La manière la plus simple de le voir est de le comparer aux classes OOP. Alors que les classes ont des champs et des fonctions, les types GraphQL ont des champs et des requêtes.

* Modifiez `server.js` avec :

<script src="https://gist.github.com/ldiego08/434191e901d3b79a77a2c9d990718d72.js"></script>

Encore une fois, pas de magie.

Nous disons que la requête `user` prend un paramètre `id`, et c'est ce que sa fonction de résolveur prendra. Oh, remarquez également le signe `!` signifiant que le paramètre est requis—GraphQL s'assurera qu'il est fourni.

#### 5. Remplacer le constructeur de schéma par des définitions manuelles

Vous vous souvenez comment nous avons appelé cette énorme chaîne magique que nous avons utilisée pour définir notre schéma ? Eh bien, il est temps de corriger cela.

D'accord, dans une application réelle, vous mettriez votre schéma dans des fichiers `*.graphql` séparés. Ensuite, vous pouvez ajouter des plugins de surlignage de syntaxe et de complétion de code à votre éditeur de code. Cependant, les définitions manuelles offrent une meilleure intégration avec le reste de notre code. Consultez [cet article](https://blog.apollographql.com/three-ways-to-represent-your-graphql-schema-a41f4175100d) pour plus d'informations.

Pour cette étape, nous utiliserons les classes et helpers spécialisés fournis par GraphQL :

<script src="https://gist.github.com/ldiego08/6d856472fde11ee9b7b6f26a02fe7111.js"></script>

Terminé ? D'accord, maintenant annoté :

<script src="https://gist.github.com/ldiego08/fe5e44292438018e8b336950390dabd9.js"></script>

De cette manière, nous pouvons mettre nos définitions de types dans des fichiers séparés pour mieux organiser notre code serveur !

Comme indiqué dans l'exemple, dans cette notation, la fonction de résolveur prend les paramètres suivants :

* `**root**`—l'objet parent résolu, dans ce cas l'utilisateur.
* `**args**`—arguments passés par la requête.
* `**context**`, `info`—hors du cadre de ce guide.

#### 6. Ajouter une sous-requête pour récupérer les rôles de l'utilisateur

Jusqu'à présent, nous avons appris à définir des requêtes de base. Il est temps de passer à la vitesse supérieure ! Ajoutons un nouveau champ au type `User` pour ses rôles assignés. Dans une architecture traditionnelle, nous serions tentés de créer une nouvelle requête comme `userRoles(userId: Int!): Role` et en rester là. Mais ce n'est pas comme ça que les choses fonctionnent dans GraphQL !

**Nous devons penser en _graphes_.**

Dans le langage des graphes, pour obtenir les rôles d'un utilisateur, nous enverrions une requête comme ceci :

<script src="https://gist.github.com/ldiego08/4d4437d1c2f9b94befe1b17010b685c6.js"></script>


... et obtenir un résultat JSON comme ceci :

<script src="https://gist.github.com/ldiego08/54c1e39b10e094bd3e428f989122003f.js"></script>

Cela a du sens, non ? Allons-y et modifions le schéma.

* Modifiez `server.js` avec :

<script src="https://gist.github.com/ldiego08/ba3260d390ffe8bf0a2f63105a1dd5a4.js"></script>

Voilà—nous pouvons maintenant récupérer les rôles des utilisateurs. Remarquez comment nous avons utilisé l'instance `User` passée en tant que premier paramètre au résolveur pour obtenir l'ID de l'utilisateur parent résolu.

![Image](https://cdn-media-1.freecodecamp.org/images/1*o6VJ8MEkuRgfgPHZEx4hAg.gif)
_Documentation du Schéma : Il a votre dos._

L'avantage des sous-requêtes ? GraphQL ne résoudra pas le champ `roles` à moins qu'il ne soit sélectionné dans la requête.

**Avez-vous repéré le piège avec le dernier morceau de code ?**

Si nous interrogeons 100 utilisateurs et leurs rôles, la fonction de résolveur `roles` s'exécutera cent fois. Ensuite, disons que chaque utilisateur a 10 rôles et que chaque rôle a un champ de sous-requête. Cette requête s'exécutera 100 * 10 fois.

Cela s'appelle [Le Problème N + 1](https://secure.phabricator.com/book/phabcontrib/article/n_plus_one/).

Découvrir comment corriger cela est votre devoir ! Mais il est dangereux d'y aller seul, alors prenez ceci :

[**Éviter les requêtes n+1 dans GraphQL, y compris dans les abonnements**](https://medium.com/slite/avoiding-n-1-requests-in-graphql-including-within-subscriptions-f9d7867a257d)  
[_Note : cet article n'aura pas beaucoup de sens à moins que vous ne connaissiez les bases de GraphQL, une technologie géniale que nous utilisons chez
..._medium.com](https://medium.com/slite/avoiding-n-1-requests-in-graphql-including-within-subscriptions-f9d7867a257d)

#### 7. Ajouter une mutation pour créer un nouvel utilisateur

Comme mentionné précédemment, les _mutations_ sont la manière dont nous modifions les données dans notre schéma. Si nous voulons créer, éditer ou supprimer un compte utilisateur, nous aurons besoin d'une mutation pour cela.

Les mutations sont définies presque exactement de la même manière qu'une requête, et retournent souvent les données affectées. Donc la seule différence entre elles est purement logique ?

Exactement.

Comme mentionné précédemment, les requêtes peuvent également prendre des paramètres. Elles ne retournent que des données.

* Modifiez `server.js` avec :

<script src="https://gist.github.com/ldiego08/ccd363aac96df4440c2ab098102abf9f.js"></script>

* Envoyez la requête suivante depuis Graph_i_QL :

<script src="https://gist.github.com/ldiego08/f286b4f91e03dabff287ec06536b1903.js"></script>

* **Profit.**

![Image](https://cdn-media-1.freecodecamp.org/images/1*qq5k85ub7aQ3xB-siyUKUw.gif)
_Fautes de frappe : Gâchant les enregistrements GIF depuis 1927_

### Conclusion

Espérons que les bases de GraphQL sont claires : configurer un serveur, créer un schéma (en notation simple et complexe) avec des types, des requêtes et des mutations. J'ai utilisé un exemple assez basique. Espérons qu'il a bien servi à illustrer chaque concept sans être intrusif.

À partir de ce point, c'est à vous de développer l'exemple avec plus de choses. Ou vous pouvez créer une toute nouvelle base de code pour un autre cas d'utilisation.

Pour vous lancer, voici quelques choses que vous pouvez essayer :

* Résoudre le problème N+1 en implémentant des chargeurs de données.
* Créer des mutations pour valider les identifiants des utilisateurs, gérer les rôles des utilisateurs, et plus.
* Ajouter une base de données réelle pour alimenter vos résolveurs (MySQL, SQLite, etc.)
* Utiliser un backend d'authentification comme OAuth pour valider les utilisateurs.
* Créer une application client simple qui utilise le client Apollo Boost pour se connecter à votre serveur.
* Reconstruire l'exemple avec TypeScript.

Les possibilités sont infinies !

### Obtenez le code source

L'exemple entier est hébergé sur GitHub. Parcourez les [tags](https://github.com/ldiego08/workshops-graphql/tags) pour voir une progression graduelle du code.

[**ldiego08/workshops-graphql**](https://github.com/ldiego08/workshops-graphql)  
[_GitHub est l'endroit où les gens construisent des logiciels. Plus de 28 millions de personnes utilisent GitHub pour découvrir, fork et contribuer à plus de
..._github.com](https://github.com/ldiego08/workshops-graphql)

> Vous avez des questions, des commentaires ou quelque chose que vous aimeriez partager ? Retrouvez-moi sur Twitter en tant que [@ldiego08](https://twitter.com/ldiego08). De plus, n'oubliez pas de ?, partager et suivre si cet article a été utile !

[**Luis Aguilar (@ldiego08) | Twitter**](https://twitter.com/ldiego08)  
[_San José, Costa Rica — Écrivain de science-fiction, développeur de logiciels @skillshare._ twitter.com](https://twitter.com/ldiego08)