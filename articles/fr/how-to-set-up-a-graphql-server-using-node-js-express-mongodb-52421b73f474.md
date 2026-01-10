---
title: Comment configurer un serveur GraphQL en utilisant Node.js, Express et MongoDB
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-05T21:02:09.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-a-graphql-server-using-node-js-express-mongodb-52421b73f474
coverImage: https://cdn-media-1.freecodecamp.org/images/1*rhpr5EnxrphBwqyTus0jmg.png
tags:
- name: GraphQL
  slug: graphql
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: software
  slug: software
- name: technology
  slug: technology
seo_title: Comment configurer un serveur GraphQL en utilisant Node.js, Express et
  MongoDB
seo_desc: 'By Leonardo Maldonado

  The most straightforward way to start with GraphQL & MongoDB.


  So you are planning to start with GraphQL and MongoDB. Then you realize how can
  I set up those two technologies together? Well, this article is made precisely for
  yo...'
---

Par Leonardo Maldonado

#### La manière la plus simple de commencer avec GraphQL et MongoDB.

![Image](https://cdn-media-1.freecodecamp.org/images/1*rhpr5EnxrphBwqyTus0jmg.png)

Vous prévoyez donc de commencer avec GraphQL et MongoDB. Ensuite, vous vous demandez comment configurer ces deux technologies ensemble ? Eh bien, cet article est fait précisément pour vous. Je vais vous montrer comment configurer un serveur GraphQL en utilisant MongoDB. Je vais vous montrer comment vous pouvez modulariser votre schéma GraphQL et tout cela en utilisant MLab comme base de données.

[**Tout le code de cet article est disponible ici.**](https://github.com/leonardomso/graphql-mongodb-server)

Alors maintenant, commençons.

### Pourquoi GraphQL ?

GraphQL est un langage de requête pour vos API. Il a été publié par Facebook en 2015 et a connu une adoption très élevée. C'est le remplacement de _REST_.

Avec GraphQL, le client peut demander les données exactes dont il a besoin et obtenir exactement ce qu'il a demandé. GraphQL utilise également une syntaxe de requête similaire à JSON pour effectuer ces requêtes. Toutes les requêtes vont au même endpoint.

Si vous lisez cet article, je suppose que vous connaissez un peu GraphQL. Si vous ne connaissez pas, vous pouvez en apprendre davantage sur GraphQL [ici.](https://graphql.org/)

### Commencer

Tout d'abord, créez un dossier, puis démarrez notre projet.

```
npm init -y 
```

Ensuite, installez quelques dépendances pour notre projet.

```
npm install @babel/cli @babel/core @babel/preset-env body-parser concurrently cors express express-graphql graphql graphql-tools merge-graphql-schemas mongoose nodemon
```

Et ensuite _@babel/node_ comme dépendance de développement :

```
npm install --save-dev @babel/node 
```

#### Babel

Maintenant, nous allons configurer Babel pour notre projet. Créez un fichier appelé _.babelrc_ dans votre dossier de projet. Ensuite, mettez _@babel/env_ là, comme ceci :

Ensuite, allez dans votre package.json et ajoutez quelques scripts :

Nous n'aurons qu'un seul script que nous allons utiliser dans notre projet.

"server" — Il exécutera principalement notre serveur.

#### Serveur

Maintenant, dans notre dossier racine, créez le fichier _index.js_. Ce sera là où nous allons créer notre serveur.

Tout d'abord, nous allons importer tous les modules que nous allons utiliser.

Ensuite, nous allons créer notre connexion avec MongoDB en utilisant Mongoose :

Qu'en est-il de cette constante _db_ ? C'est là que vous allez mettre l'URL de votre base de données pour vous connecter à MongoDB. Ensuite, vous allez me dire : "Mais, je n'ai pas encore de base de données", oui, je vous comprends. Pour cela, nous utilisons MLab.

MLab est une base de données en tant que service pour MongoDB, tout ce que vous avez à faire est d'aller sur leur site ([cliquez ici](https://mlab.com/)) et de vous inscrire.

Après vous être inscrit, allez et créez une nouvelle base de données. Pour l'utiliser gratuitement, choisissez cette option :

![Image](https://cdn-media-1.freecodecamp.org/images/1*JDDQnoWbkwJM4R_MFVCB4A.png)
_Option gratuite de MLab à utiliser dans notre serveur MongoDB._

Choisissez US East (Virginie) comme option, puis donnez un nom à notre base de données. Après cela, notre base de données s'affichera sur la page d'accueil.

![Image](https://cdn-media-1.freecodecamp.org/images/1*q25QbcqFOFHIVtxtedxfFw.png)
_Notre base de données créée avec MLab._

Cliquez sur notre base de données, puis allez dans _User_ et créez un nouvel utilisateur. Dans cet exemple, je vais créer un utilisateur appelé _leo_ et le mot de passe _leoleo1_.

Après la création de notre utilisateur, en haut de notre page, nous trouvons deux _URLs. L'_une pour se connecter en utilisant _Mongo Shell._ L'autre pour se connecter en utilisant une _URL MongoDB._ Nous copions la seconde.

Après cela, tout ce que vous avez à faire est de coller cette URL dans notre constante _db_ dans le fichier _index.js._ Notre constante _db_ ressemblerait à ceci :

#### Express

Maintenant, nous allons enfin démarrer notre serveur. Pour cela, nous avons ajouté quelques lignes supplémentaires dans notre fichier _index.js_ et nous avons terminé.

Maintenant, exécutez la commande _npm run server_ et allez sur _localhost:4000/graphql_ et vous trouverez une page comme celle-ci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*BIhNVFafvKf1kEgDbQ4j9g.png)
_Le terrain de jeu GraphiQL._

### MongoDB et Schéma

Maintenant, dans notre dossier racine, créez un dossier nommé _models_ et créez un fichier à l'intérieur appelé User.js (oui, avec un U majuscule).

À l'intérieur de User.js, nous allons créer notre premier schéma dans MongoDB en utilisant Mongoose.

Maintenant que nous avons créé notre schéma User, nous allons commencer avec GraphQL.

### GraphQL

Dans notre dossier racine, nous allons créer un dossier appelé _graphql._ À l'intérieur de ce dossier, nous allons créer un fichier appelé _index.js_ et deux autres dossiers : _resolvers_ et _types_.

#### Requêtes

Les requêtes dans GraphQL sont la manière dont nous demandons des données à notre serveur. Nous demandons les données dont nous avons besoin, et il retourne exactement ces données.

Toutes nos requêtes seront à l'intérieur de notre dossier _types_. À l'intérieur de ce dossier, créez un fichier _index.js_ et un dossier User.

À l'intérieur du dossier User, nous allons créer un fichier _index.js_ et écrire nos requêtes.

Dans notre dossier types, dans notre fichier _index.js_, nous allons importer tous les types que nous avons. Pour l'instant, nous avons les types User.

Au cas où vous auriez plus d'un type, vous l'importez dans votre fichier et l'incluez dans le tableau _typeDefs_.

#### Mutations

Les mutations dans GraphQL sont la manière dont nous modifions les données sur le serveur.

Toutes nos mutations seront à l'intérieur de notre dossier _resolvers_. À l'intérieur de ce dossier, créez un fichier _index.js_ et un dossier User.

À l'intérieur du dossier User, nous allons créer un fichier _index.js_ et écrire nos mutations.

Maintenant que toutes nos résolutions et mutations sont prêtes, nous allons modulariser notre schéma.

#### Modularisation de notre schéma

À l'intérieur de notre dossier appelé graphql, allez dans notre index.js et créez notre schéma, comme ceci :

Maintenant que notre schéma est terminé, allez dans notre dossier racine et à l'intérieur de notre _index.js_ importer notre schéma.

Après tout cela, notre schéma se terminera comme ceci :

### Jouer avec nos requêtes et mutations

Pour tester nos requêtes et mutations, nous allons démarrer notre serveur avec la commande _npm run server_, et aller sur _localhost:4000/graphql._

#### Créer un utilisateur

Tout d'abord, nous allons créer notre premier utilisateur avec une mutation :

```
mutation {  addUser(id: "1", name: "Dan Abramov", email: "dan@dan.com") {    id    name    email  }}
```

Après cela, si le terrain de jeu GraphiQL vous retourne l'objet de données que nous avons créé, cela signifie que notre serveur fonctionne correctement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*U2vN26hF2kLC_8JXtUMvyA.png)
_L'objet de données que GraphiQL Playground nous a retourné._

Pour être sûr, allez sur MLab, et à l'intérieur de notre collection _users_, vérifiez si nos données que nous venons de créer s'y trouvent.

![Image](https://cdn-media-1.freecodecamp.org/images/1*kY0ftzycpo0QwjRgc0eFUA.png)
_Dans notre première mutation, nous avons créé un utilisateur._

Après cela, créez un autre utilisateur appelé "Max Stoiber". Nous ajoutons cet utilisateur pour nous assurer que notre mutation fonctionne correctement et que nous avons plus d'un utilisateur dans la base de données.

#### Supprimer un utilisateur

Pour supprimer un utilisateur, notre mutation sera comme ceci :

```
mutation {  deleteUser(id: "1", name: "Dan Abramov", email: "dan@dan.com") {    id    name    email  }}
```

Comme l'autre, si le terrain de jeu GraphiQL vous retourne l'objet de données que nous avons créé, cela signifie que notre serveur fonctionne correctement.

#### Obtenir tous les utilisateurs

Pour obtenir tous les utilisateurs, nous allons exécuter notre première requête comme ceci :

```
query {  users {    id    name    email  }}
```

Puisque nous n'avons qu'un seul utilisateur, il devrait retourner cet utilisateur exact.

![Image](https://cdn-media-1.freecodecamp.org/images/1*r_o7jCMP0fQdiFDsozGoWg.png)
_Tous nos utilisateurs seront retournés._

#### Obtenir un utilisateur spécifique

Pour obtenir un utilisateur spécifique, voici la requête :

```
query {  user(id: "2"){    id    name    email  }}
```

Cela devrait retourner l'utilisateur exact.

![Image](https://cdn-media-1.freecodecamp.org/images/1*A6UZ-KVEhOthrgFO4qZxcg.png)
_L'utilisateur exact que nous avons demandé._

### Et nous avons terminé !

Notre serveur est en cours d'exécution, nos requêtes et mutations fonctionnent correctement, nous sommes prêts à commencer notre client. Vous pouvez commencer avec _create-react-app._ Dans votre dossier racine, donnez simplement la commande _create-react-app client_ et ensuite, si vous exécutez la commande **_npm run dev_**, notre _serveur_ et _client_ s'exécuteront simultanément !

[**Tout le code de cet article est disponible ici.**](https://github.com/leonardomso/graphql-mongodb-server)

? S[**uivez-moi sur Twitter !**](https://twitter.com/leonardomso)   
**✨** S[**uivez-moi sur GitHub !**](https://github.com/leonardomso)

_Je cherche une opportunité à distance, donc si vous en avez, j'adorerais en entendre parler, alors s'il vous plaît contactez-moi !_