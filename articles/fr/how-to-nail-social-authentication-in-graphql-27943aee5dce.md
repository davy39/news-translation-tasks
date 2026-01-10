---
title: Comment réussir l'authentification sociale dans GraphQL
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-31T20:12:57.000Z'
originalURL: https://freecodecamp.org/news/how-to-nail-social-authentication-in-graphql-27943aee5dce
coverImage: https://cdn-media-1.freecodecamp.org/images/1*t-7yWb1aLXCvv8nunA1hzQ.png
tags:
- name: authentication
  slug: authentication
- name: GraphQL
  slug: graphql
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: technology
  slug: technology
seo_title: Comment réussir l'authentification sociale dans GraphQL
seo_desc: 'By Oladipupo Bello

  In this article you will learn how to perform social authentication in GraphQL server
  with Passport.JS.

  Perhaps you have an authentication system in place, using directives or resolver
  wrappers to protect your schema from unauthori...'
---

Par Oladipupo Bello

Dans cet article, vous apprendrez comment effectuer l'**authentification sociale** sur un serveur **GraphQL** avec **Passport.JS**.

Peut-être avez-vous déjà un système d'authentification en place, utilisant des directives ou des wrappers de résolveurs pour protéger votre schéma contre les accès non autorisés, et vous vous demandez comment ajouter l'authentification via Google, Facebook ou tout autre fournisseur OAuth à votre API.

Eh bien, accrochez-vous, car en quelques lignes de code, vous aurez exactement cela.

Je n'entrerai pas dans les détails sur le fonctionnement des JWT ou sur la manière d'obtenir un _jeton d'accès_ auprès d'un fournisseur. Ce tutoriel se concentrera sur l'utilisation d'un _jeton d'accès_ obtenu côté client pour récupérer les données utilisateur auprès d'un fournisseur pour l'inscription et la connexion.

Je n'aborderai pas non plus la mise en place de l'autorisation pour votre schéma, car de nombreux tutoriels [tutoriels](https://www.apollographql.com/docs/apollo-server/features/authentication.html) ont déjà été réalisés sur le sujet.

### **Un court voyage dans le passé — Avant GraphQL 🏃‍♂️**

L'authentification en REST est simple : placez votre middleware sur un endpoint et c'est terminé. Dans GraphQL, cependant, il n'y a qu'un seul endpoint, donc nous avons besoin d'une approche différente.

### L'essentiel

Une fois que vous comprenez comment procéder pour implémenter la connexion sociale, le choix du framework, du langage ou de la base de données que vous souhaitez utiliser en fin de compte sera illimité. Alors, c'est parti :

**Étape 1** : Sur le front-end, faites apparaître la fenêtre contextuelle de connexion du fournisseur d'authentification tiers.

**Étape 2** : (Toujours sur le front-end) Récupérez le jeton d'accès que le fournisseur retourne après avoir accepté la connexion.

**Étape 3** : (Oui, toujours sur le front-end) Envoyez ce jeton au back-end en tant que partie de l'argument d'entrée de votre mutation.

**Étape 4** : Sur le back-end, vérifiez le jeton.

**Étape 5** : Si le jeton est authentique, vous recevrez l'utilisateur dans le cadre de la réponse de vérification (du moins, c'est le cas avec Passport.js, que nous allons utiliser).

**Étape 6** : Enregistrez les données de l'utilisateur dans votre base de données.

**Étape 7** : Retournez un JWT au front-end. Ce que vous faites avec ce jeton est hors du cadre de ce tutoriel, mais il devrait probablement être utilisé pour authentifier chaque action de l'utilisateur connecté.

Vous y voilà, le squelette pour créer une connexion sociale avec GraphQL.

Je vais omettre les étapes 1, 2 et 3 car elles ont déjà été couvertes [ici](https://medium.com/@alexanderleon/implement-social-authentication-with-react-restful-api-9b44f4714fa). En pratique, peu importe les frameworks/bibliothèques que vous utilisez sur le front-end. Tout ce qui compte, c'est de récupérer un code d'accès et d'exécuter une mutation avec celui-ci.

**Assez de bavardages. Commençons.**

Tout d'abord, vous devrez récupérer les identifiants et secrets d'authentification auprès des différents fournisseurs.

### Facebook

**Étape 1** : Allez sur [https://developers.facebook.com/apps/](https://developers.facebook.com/apps/) et sélectionnez « Ajouter une nouvelle application ».

**Étape 2** : Donnez un nom à votre application et complétez la question de sécurité.

**Étape 3** : Sélectionnez « Intégrer la connexion Facebook » et cliquez sur confirmer.

**Étape 4** : Copiez les valeurs _App Id_ et _App Secret_ qui se cachent quelque part sur la même page.

### Google

**Étape 1** : Allez sur la console développeur : [https://console.developers.google.com/](https://console.developers.google.com/) et créez un projet.

**Étape 2** : Recherchez « oauth credentials » dans la barre de recherche et cliquez sur l'unique option qui apparaît.

**Étape 3** : Essayez de trouver le bouton « Create credentials ». Si vous le trouvez, cliquez dessus. Choisissez « Oauth Client Id ».

Pour le type d'application, sélectionnez « _application web_ ».

Pour les origines autorisées, ajoutez http://localhost:3000. En production, vous voudrez probablement être un peu plus spécifique.

![Image](https://cdn-media-1.freecodecamp.org/images/1*TrFJT0yyVejORPd8QvKyTw.png)

**Étape 4** : Cliquez sur créer et copiez les valeurs _Client Id_ et _Client Secret_ qui se cachent quelque part sur la même page.

### **Le serveur API**

Créez un dossier pour votre serveur :

```
mkdir graphql-social-auth && cd graphql-social-auth
```

Initialisez l'application [avec](https://docs.npmjs.com/creating-a-package-json-file)

```
npm init
```

ou si vous utilisez [yarn](https://yarnpkg.com/lang/en/docs/cli/init/)

```
yarn init
```

Mettons en place un serveur API. J'utiliserai apollo-server ici.

```
npm install --save apollo-server graphql
```

ou si vous utilisez yarn

```
yarn add apollo-server graphql
```

Apollo Server configurera un serveur Express pour vous tant que vous lui fournissez `typeDefs` et `resolvers`.

typeDefs signifie Type Definitions qui définissent la « forme » de vos données. Les résolveurs, quant à eux, sont responsables de la récupération des données pour ces types.

Créez un fichier src/app.js et ajoutez le code suivant :

À ce stade, nous pouvons démarrer le serveur en exécutant

```
node src/app.js
```

Après avoir démarré le serveur, il devrait afficher un message dans la console indiquant qu'il est prêt.

```
? Server ready at http://localhost:4000/ 
```

Vous vous demandez comment changer le port ou connecter le serveur à une application node.js existante ? Consultez la [documentation](https://www.apollographql.com/docs/apollo-server) d'apollo-server pour plus d'informations.

Pour explorer la nouvelle API GraphQL, ouvrez un navigateur à l'adresse indiquée dans la console, `http://localhost:4000/`. Apollo Server configure GraphQL Playground pour vous afin que vous puissiez commencer à exécuter des requêtes et explorer le schéma rapidement.

Pour exécuter une requête, copiez la requête suivante puis appuyez sur le bouton « ▶️ » :

```
query {  hello}
```

Et le serveur devrait retourner une réponse simple :

```
{  "data": {    "hello": "world"  }}
```

Hourra ! Le serveur fonctionne. Maintenant, voici la partie amusante.

1. Nous devons configurer notre schéma et nos résolveurs GraphQL.
2. Nous devons configurer Passport et le connecter à nos résolveurs pour valider nos jetons provenant du front-end.
3. Nous devrons également configurer Mongo pour gérer le stockage de nos utilisateurs.

J'utiliserai MongoDB car il est plus facile à configurer, mais le remplacer par MySQL ne devrait pas poser de problème.

Tout d'abord, installons les dépendances nécessaires :

```
npm install --save passport passport-facebook-token passport-google-token mongoose jsonwebtoken
```

ou si vous utilisez yarn

```
yarn add passport passport-facebook-token passport-google-token mongoose jsonwebtoken
```

Ensuite, ouvrez le dossier src et créez les fichiers suivants :

```
mongoose.jspassport.jstypeDefs.jsresolvers.js
```

Ajoutez ce qui suit à src/mongoose.js :

Cela connectera l'application à la base de données et configurera le schéma utilisateur.

Il créera également des méthodes pour générer des JWT et trouver des utilisateurs à partir de Facebook et Google dans notre base de données.

Ajoutez ce qui suit à src/passport.js :

N'oubliez pas de remplacer les identifiants et secrets factices par ceux de Facebook et Google.

Cela dit, tout ce qui reste à faire maintenant est de mettre à jour les types et résolveurs GraphQL.

Déplaçons les typeDefs et les résolveurs vers des fichiers séparés pour garder notre app.js propre et ordonné. Ajoutez ce qui suit à src/typeDefs.js :

Ensuite, src/resolver.js :

Ensuite, nous refactorisons notre src/app.js pour importer le schéma depuis les fichiers séparés.

Enfin, nous ajoutons les objets request et response d'express à notre _contexte_ GraphQL. Cela les rendra disponibles dans nos résolveurs de mutation pour une utilisation avec **Passport.JS**.

Et nous avons terminé.

### **Essayons cela**

Exécutez la commande suivante dans une fenêtre séparée pour lancer le démon Mongo :

```
mongod
```

Maintenant, redémarrez le serveur API :

```
node src/app.js
```

Pour vous assurer que tout fonctionne correctement, récupérons quelques _jetons d'accès_ et effectuons quelques tests.

### **Facebook**

**Étape 1** : Ouvrez les paramètres de votre application sur [https://developers.facebook.com/apps/](https://developers.facebook.com/apps/) et sélectionnez Rôles -> Utilisateurs de test dans la barre latérale de gauche.

**Étape 2** : Cliquez sur modifier et sélectionnez « Modifier les autorisations que cet utilisateur de test a accordées à l'application »

![Image](https://cdn-media-1.freecodecamp.org/images/1*tmYa2WfM-9vT8aS7sqKXAw.png)

**Étape 3** : Ajoutez l'email aux autorisations et cliquez sur mettre à jour.

![Image](https://cdn-media-1.freecodecamp.org/images/1*rnPPkAOquvteaBW96SUeqg.png)

**Étape 4** : Cliquez sur modifier et sélectionnez « Obtenir un jeton d'accès pour cet utilisateur de test »

**Étape 5** : Copiez le _jeton d'accès_ et exécutez la mutation authFacebook avec celui-ci dans le GraphQL Playground.

![Image](https://cdn-media-1.freecodecamp.org/images/1*qzNV2a2nM1AMFkDCY3TUwA.png)
_mutation et réponse du graphql playground_

### **Google**

Pour autant que je sache, Google n'a pas d'équivalent d'utilisateur de test pour leurs API. Mais nous pouvons utiliser le Oauth Playground pour obtenir un _jeton d'accès_ valide.

**Étape 1** : Allez sur [https://developers.google.com/oauthplayground](https://developers.google.com/oauthplayground/), sélectionnez les portées « Google OAuth2 API v2 » et cliquez sur « Autoriser les API » :

![Image](https://cdn-media-1.freecodecamp.org/images/1*l4jSrY3UnfA9WBjzA78Mlw.png)
_Portées d'authentification pour Google OAuth2 API v2_

Vous serez redirigé vers l'écran de consentement Google.

**Étape 2** : Après avoir donné votre consentement, trouvez le bouton « exchange authorization code for tokens » sur la page et cliquez dessus. Cela générera un _refresh_ et un _jeton d'accès_ valides pour l'utilisateur connecté.

**Étape 3** : Copiez le _jeton d'accès_ généré et exécutez la mutation authGoogle avec celui-ci dans le GraphQL Playground.

![Image](https://cdn-media-1.freecodecamp.org/images/1*IWW78ntUV-9kV3vp5JXB5A.png)
_mutation et réponse du graphql playground_

### C'est tout !

Vous avez réussi jusqu'à la fin ! Si vous êtes bloqué en cours de route, n'hésitez pas à consulter le code dans ce [dépôt](https://github.com/DavyBello/graphql-social-auth-tutorial). Si vous avez des questions ou des commentaires, faites-le moi savoir dans les commentaires ci-dessous.

Santé !

[Ladi Bello](https://ladi-bello.netlify.com)