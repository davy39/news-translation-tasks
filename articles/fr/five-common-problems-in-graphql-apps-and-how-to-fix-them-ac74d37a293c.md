---
title: Cinq problèmes courants dans les applications GraphQL (et comment les résoudre)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-09T08:05:49.000Z'
originalURL: https://freecodecamp.org/news/five-common-problems-in-graphql-apps-and-how-to-fix-them-ac74d37a293c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*a5ZZXSCeFVJZ27VXNN8ELQ.png
tags:
- name: GraphQL
  slug: graphql
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Cinq problèmes courants dans les applications GraphQL (et comment les résoudre)
seo_desc: 'By Sacha Greif

  Learn to unlock the power of GraphQL without suffering its drawbacks

  GraphQL is all the rage these days, and for good reason: it’s an elegant approach
  that solves many of the problems associated with traditional REST APIs.

  Yet I’d be l...'
---

Par Sacha Greif

#### Apprenez à exploiter la puissance de GraphQL sans en subir les inconvénients

[GraphQL](http://graphql.org) est sur toutes les lèvres ces jours-ci, et pour de bonnes raisons : c'est une approche élégante qui résout de nombreux problèmes associés aux API REST traditionnelles.

Pourtant, je mentirais si je vous disais que GraphQL ne vient pas avec son propre ensemble de problèmes. Et si vous n'êtes pas prudent, ces problèmes peuvent non seulement conduire à une base de code gonflée, mais même à une application considérablement ralentie.

Je parle de problèmes tels que :

* **Duplication de schéma**
* **Inadéquation des données serveur/client**
* **Appels de base de données superflus**
* **Mauvaises performances**
* **Surcharge de code standardisé**

Je suis prêt à parier que votre application souffre d'au moins l'un d'entre eux. La bonne nouvelle, c'est qu'aucun d'entre eux n'est incurable !

Pour chaque problème, je vais décrire le problème, puis expliquer comment je le traite dans [Vulcan](http://vulcanjs.org), un framework React/GraphQL open-source sur lequel je travaille depuis un an (vous devriez le vérifier !). Mais espérons que vous pourrez appliquer les mêmes stratégies à votre propre base de code, que vous utilisiez Vulcan ou non.

![Image](https://cdn-media-1.freecodecamp.org/images/WzpNm95jVV1teXE08i6UcUQ3UmjxuQrX7d8E)

### Problème : Duplication de schéma

L'une des premières choses que vous réalisez lorsque vous codez un back-end GraphQL à partir de zéro est qu'il implique beaucoup de code similaire mais pas tout à fait identique, surtout en ce qui concerne les schémas.

À savoir, vous avez besoin d'un schéma pour votre base de données, et d'un autre pour votre endpoint GraphQL. Non seulement il est frustrant de devoir écrire plus ou moins la même chose deux fois, mais vous avez maintenant deux sources de vérité indépendantes que vous devez constamment garder synchronisées.

#### Solution : Génération de schéma GraphQL

Un certain nombre de solutions à ce problème ont émergé dans l'écosystème GraphQL. Par exemple, [PostGraphile](https://www.graphile.org/postgraphile/) génère un schéma GraphQL à partir de votre base de données PostgreSQL, et [Prisma](https://www.prismagraphql.com/) vous aidera également à générer des types pour vos requêtes et mutations.

Je me souviens également avoir entendu [Laney Zamore & Adam Kramer de l'équipe GraphQL](https://www.youtube.com/watch?v=XfHOrfTyJJw) décrire comment ils généraient directement leur schéma GraphQL à partir de leurs définitions de types PHP.

Pour Vulcan, je suis tombé indépendamment sur une solution très similaire. J'utilisais [SimpleSchema](https://github.com/aldeed/simple-schema-js) pour décrire mes schémas en tant qu'objets JavaScript, et j'ai commencé simplement en convertissant le type `String` de JavaScript en une `String` GraphQL, `Number` en `Int` ou `Float`, et ainsi de suite.

Donc ce champ JavaScript :

```
title: {  type: String}
```

Deviendrait ce champ GraphQL :

```
title: String
```

Mais bien sûr, un schéma GraphQL peut également avoir des types personnalisés : `User`, `Comment`, `Event`, et ainsi de suite.

Je ne voulais pas ajouter trop de magie à l'étape de génération de schéma, alors j'ai créé des [résolveurs de champ](http://docs.vulcanjs.org/field-resolvers.html), une manière simple de vous laisser spécifier ces types personnalisés. Donc ce champ JavaScript :

```
userId{  type: String,  resolveAs: {    fieldName: 'user',    type: 'User',    resolver: document => {      return Users.findOne(document.userId)    }  }}
```

Deviendrait :

```
user: User
```

Comme vous pouvez le voir, nous définissons également la fonction de [résolveur](http://graphql.org/learn/execution/) réelle sur le champ, puisque celle-ci est également directement liée au champ GraphQL.

Que vous utilisiez quelque chose comme PostGraphile ou que vous écriviez votre propre code de génération de schéma, je vous encourage à éviter la duplication de schéma dans votre propre application.

Ou bien, vous pouvez également utiliser un service hébergé tel que [Graphcool](https://www.graph.cool/) pour gérer votre schéma en utilisant leur tableau de bord et contourner entièrement ce problème.

![Image](https://cdn-media-1.freecodecamp.org/images/czkjIXuQcTg3x1rNV41WWK8U7BWTiF-UV5xm)

### Problème : Inadéquation des données serveur/client

Comme nous venons de le voir, votre base de données et votre API GraphQL auront des schémas différents, ce qui se traduit par des formes de document différentes.

Ainsi, alors qu'un `post` frais sorti de la base de données aura une propriété `userId`, le même `post` récupéré via votre API aura plutôt une propriété `user`.

Cela signifie que l'obtention du nom de l'auteur d'un post sur le client ressemblera à ceci :

```
const getPostNameClient = post => {  return post.user.name}
```

Mais sur le serveur, ce sera une histoire complètement différente :

```
const getPostNameServer = post => {  const postAuthor = Users.findOne(post.userId)  return postAuthor.name}
```

Cela peut poser un problème chaque fois que vous essayez de partager du code entre le client et le serveur pour simplifier votre base de code. Et même au-delà de cela, cela signifie que vous passez à côté de la grande approche de GraphQL pour l'interrogation des données sur le serveur.

J'ai récemment ressenti cette douleur en essayant de construire un système pour générer des newsletters hebdomadaires : chaque newsletter était composée de plusieurs posts et commentaires, ainsi que d'informations sur leurs auteurs ; en d'autres termes, un cas d'utilisation parfait pour GraphQL. Mais cette génération de newsletter se faisait sur le _serveur_, ce qui signifie que je n'avais pas de moyen d'interroger mon endpoint GraphQL...

#### Solution : Requêtes GraphQL de serveur à serveur

Ou peut-être que si ? Il s'avère que vous pouvez exécuter des requêtes GraphQL de serveur à serveur sans problème ! Il suffit de [passer votre schéma exécutable GraphQL à la fonction `graphql`](http://graphql.org/graphql-js/graphql/#graphql), ainsi que votre requête GraphQL :

```
const result = await graphql(executableSchema, query, {}, context, variables);
```

Dans Vulcan, [j'ai généralisé ce modèle dans un helper `runQuery`](http://docs.vulcanjs.org/server-queries.html), et j'ai également ajouté des fonctions `queryOne` à chaque collection. Celles-ci agissent exactement comme les fonctions `findOne` de MongoDB, sauf qu'elles retournent le document tel que récupéré via l'API GraphQL :

```
const user = await Users.queryOne(userId, {  fragmentText: `    fragment UserFragment on User {      _id      username      createdAt      posts{        _id        title      }    }  `});
```

Les requêtes GraphQL de serveur à serveur m'ont aidé à simplifier considérablement mon code. Cela m'a permis de refactoriser mon appel de génération de newsletter d'un fouillis d'appels de base de données successifs et de boucles à une seule requête GraphQL :

```
query NewsletterQuery($terms: JSON){  SiteData{    title  }  PostsList(terms: $terms){    _id    title    url    pageUrl    linkUrl    domain    htmlBody    thumbnailUrl    commentsCount    postedAtFormatted    user{      pageUrl      displayName    }    comments(limit: 3){      user{        displayName        avatarUrl        pageUrl      }      htmlBody      postedAt    }  }}
```

Le message à retenir ici : ne voyez pas GraphQL comme un simple protocole client-serveur. GraphQL peut être utilisé pour interroger des données dans n'importe quelle situation, y compris client à client avec [Apollo Link State](https://github.com/apollographql/apollo-link-state) ou même pendant un processus de construction statique avec [Gatsby](https://www.gatsbyjs.org/).

![Image](https://cdn-media-1.freecodecamp.org/images/FuGWs40558hc3tICTQLvg0tjEZC1B3CsngvM)

### Problème : Appels de base de données superflus

Imaginez une liste de posts, chacun ayant un utilisateur attaché. Vous souhaitez maintenant afficher 10 de ces posts, ainsi que le nom de leur auteur.

Avec une implémentation typique, cela signifierait **deux** appels de base de données. Un pour obtenir les 10 posts, et un pour obtenir les 10 utilisateurs correspondant à ces posts.

Mais qu'en est-il de GraphQL ? En supposant que nos posts ont un champ `user` avec son propre résolveur, nous avons toujours un appel initial à la base de données pour obtenir la liste des posts. Mais nous avons maintenant un appel supplémentaire pour récupérer chaque utilisateur _par résolveur_, pour un total de **11** appels de base de données !

Maintenant, imaginez que chaque post ait également 5 commentaires, chacun ayant un auteur. Notre nombre d'appels a maintenant gonflé à :

* 1 pour la liste des posts
* 10 pour les auteurs des posts
* 10 pour chaque sous-liste de 5 commentaires
* 50 pour les auteurs des commentaires

Pour un total de **71** appels de base de données pour afficher _une seule vue_ !

Personne ne veut avoir à expliquer à son patron pourquoi la page d'accueil prend 25 secondes à charger. Heureusement, il existe une solution : [Dataloader](https://github.com/facebook/dataloader).

#### Solution : Dataloader

Dataloader vous permettra de regrouper et de mettre en cache les appels de base de données.

* **Regroupement** signifie que si Dataloader découvre que vous accédez à la même table de base de données plusieurs fois, il regroupera tous les appels ensemble. Dans notre exemple, les appels des 10 auteurs de posts et des 50 auteurs de commentaires seraient tous regroupés en un seul appel.
* **Mise en cache** signifie que si Dataloader détecte que deux posts (ou un post et un commentaire) ont le même auteur, il réutilisera l'objet utilisateur qu'il a déjà en mémoire au lieu de faire un nouvel appel à la base de données.

En pratique, vous n'atteignez pas toujours une mise en cache et un regroupement parfaits, mais Dataloader est toujours d'une grande aide.

Et Vulcan rend l'utilisation de Dataloader extra facile. Dès la sortie de la boîte, [chaque modèle Vulcan inclut des fonctions Dataloader](http://docs.vulcanjs.org/performance.html#Caching-amp-Batching) comme alternatives aux fonctions de requête MongoDB "normales".

Ainsi, en plus de `collection.findOne` et `collection.find`, vous pouvez utiliser `collection.loader.load` et `collection.loader.loadMany`.

La seule limitation est que Dataloader ne fonctionne que lorsque vous interrogez en utilisant des IDs de document. Vous pouvez donc l'utiliser pour interroger un document dont l'ID est déjà connu, mais vous devrez toujours accéder à votre base de données si vous souhaitez demander, par exemple, le post créé le plus récemment.

![Image](https://cdn-media-1.freecodecamp.org/images/GxlQow63LtMbXmI1doulB29kJ9Bvpfmg3DbZ)

### Problème : Mauvaises performances

Même avec Dataloader activé, des vues complexes peuvent encore déclencher plusieurs appels de base de données, ce qui peut à son tour entraîner des temps de chargement lents.

Cela peut être frustrant : d'une part, vous voulez tirer pleinement parti des fonctionnalités de traversée de graphe de GraphQL ("montrez-moi les auteurs des commentaires de l'auteur du post de..." etc.). Mais d'autre part, vous ne voulez pas que votre application devienne lente et sans réponse.

#### Solution : Mise en cache des requêtes

Il existe cependant une solution, qui consiste à mettre en cache la réponse _entière_ de la requête GraphQL. Contrairement à Dataloader, dont la portée est limitée à la requête actuelle (ce qui signifie qu'il ne mettra en cache les documents que _dans_ la même requête), je parle ici de la mise en cache de la requête entière pendant une période de temps.

[Apollo Engine](https://www.apollographql.com/engine/) est un excellent moyen de faire exactement cela. C'est un service hébergé qui fournit des analyses sur vos requêtes GraphQL, mais il dispose également d'une fonctionnalité de [mise en cache](https://www.apollographql.com/docs/engine/caching.html) très utile.

Vulcan est livré avec une intégration Engine intégrée, vous devez simplement ajouter votre clé API à votre fichier de paramètres. Vous pouvez ensuite ajouter l'argument `enableCache: true` à vos requêtes GraphQL pour les mettre en cache en utilisant Engine.

Ou, en utilisant les [composants d'ordre supérieur de chargement de données](http://docs.vulcanjs.org/resolvers.html#Higher-Order-Components) intégrés de Vulcan :

```
withList({  collection: Posts,   enableCache: true})(PostsList)
```

La beauté de cette approche est que vous pouvez facilement contrôler quelles requêtes sont mises en cache et lesquelles ne le sont pas, même pour le même résolveur. Par exemple, vous pouvez vouloir mettre en cache la liste des posts récents présentés sur votre page d'accueil fréquemment consultée, mais pas la liste complète des posts disponibles sur votre page d'archives.

Une dernière remarque : la mise en cache n'est pas toujours possible. Par exemple, elle n'est pas conseillée pour les données qui changent fréquemment, ou pour les données qui dépendent de l'utilisateur actuellement connecté.

![Image](https://cdn-media-1.freecodecamp.org/images/biuavoAHWIt5n3bDypomKTulQZywt2NZyN0L)

### Problème : Surcharge de code standardisé

Ce n'est en aucun cas un problème exclusif aux applications GraphQL, mais il est vrai qu'elles vous obligent généralement à écrire beaucoup de code standardisé similaire.

Typiquement, l'ajout d'un nouveau modèle (par exemple, `Comments`) à votre application impliquera les étapes suivantes :

* Écrire un résolveur pour obtenir une liste de commentaires.
* Écrire un composant d'ordre supérieur (alias conteneur) pour charger cette liste de commentaires.
* Optionnellement, écrire un résolveur pour obtenir un seul commentaire par ID ou slug, ainsi que le composant d'ordre supérieur correspondant.
* Écrire des mutations pour insérer un nouveau commentaire, modifier un commentaire et supprimer un commentaire.
* Ajouter les formulaires correspondants et le code de gestion des formulaires.

C'est beaucoup de CRUD !

#### Solution : Résolveurs, mutations et composants d'ordre supérieur génériques

L'approche de Vulcan est de vous offrir des options génériques intelligentes et faciles à utiliser pour chacune de ces étapes. Vous obtiendrez :

* [Résolveurs par défaut](http://docs.vulcanjs.org/resolvers.html#Default-Resolvers) pour afficher des listes de documents et des documents uniques.
* [Composants d'ordre supérieur pré-faits](http://docs.vulcanjs.org/resolvers.html#Higher-Order-Components) pour charger une liste de documents ou un document unique.
* [Résolveurs de mutation par défaut](http://docs.vulcanjs.org/mutations.html#Default-Mutations) pour insérer, modifier et supprimer des documents.
* [Formulaires générés](http://docs.vulcanjs.org/forms.html) basés sur votre schéma qui fonctionnent avec tout ce qui précède.

Tous ces éléments sont écrits de manière suffisamment générique pour qu'ils fonctionnent avec n'importe quel nouveau modèle dès la sortie de la boîte.

Pour être sûr, cette approche "taille unique" n'est pas sans ses inconvénients. Par exemple, parce que les requêtes sont générées dynamiquement par les composants d'ordre supérieur génériques, il est un peu plus difficile d'utiliser des [requêtes statiques](https://dev-blog.apollodata.com/5-benefits-of-static-graphql-queries-b7fa90b0b69a).

Mais cette stratégie reste un excellent moyen de commencer, au moins jusqu'à ce que vous ayez le temps de refactoriser chaque partie de votre application pour une solution plus sur mesure.

GraphQL est encore relativement nouveau, ce qui signifie que tandis que tout le monde est occupé à vanter ses mérites, il est facile de négliger les défis très réels liés à la construction d'applications GraphQL.

Heureusement, tous ces défis ont des solutions, et plus nous en discuterons (le [Slack de Vulcan](http://slack.vulcanjs.org) est un excellent endroit pour cela, soit dit en passant !), meilleures ces solutions deviendront !