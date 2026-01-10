---
title: Comment configurer l'authentification GatsbyJS avec Auth0
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-11T21:40:07.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-gatsbyjs-authentication-with-auth0-d07abdd5a4f4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*vaizCYVmspYXc7W-Yavprw.png
tags:
- name: Auth0
  slug: auth0
- name: authentication
  slug: authentication
- name: GatsbyJS
  slug: gatsbyjs
- name: JavaScript
  slug: javascript
- name: MongoDB
  slug: mongodb
seo_title: Comment configurer l'authentification GatsbyJS avec Auth0
seo_desc: 'By Michael Ozoemena

  TL;DR

  GatsbyJS is a framework that uses GraphQL and ReactJS to enable you to create feature-rich,
  super fast and dynamic web apps. It gives you the ability to consume data from virtually
  anywhere and use them in your app. In this ...'
---

Par Michael Ozoemena

#### TL;DR

GatsbyJS est un framework qui utilise GraphQL et ReactJS pour vous permettre de créer des applications web riches en fonctionnalités, super rapides et dynamiques. Il vous donne la possibilité de consommer des données de pratiquement n'importe où et de les utiliser dans votre application. Dans ce tutoriel, je vais vous montrer comment utiliser Auth0, une plateforme d'authentification et d'autorisation, pour ajouter l'authentification à votre application GatsbyJS et à votre fonction serverless sur Netlify.

Je vais supposer que vous avez au moins une compréhension de base de React, Node et GraphQL.

Voici [le dépôt Github](https://github.com/THEozmic/micro-blog) si vous souhaitez jeter un coup d'œil au code source.

#### Entrez GatsbyJS.

Créé en 2015, [Gatsby](https://www.gatsbyjs.com) est un moyen simple de construire un site web avec React. Aujourd'hui, Gatsby est connu pour être utilisé pour construire des sites web comme des blogs, des pages de portfolio, et même des applications e-commerce. Les sites Gatsby sont connus pour être extrêmement rapides, et cela est dû au fait que lorsque vous construisez un site web en utilisant Gatsby, il vient avec des tonnes d'optimisations de performance prêtes à l'emploi, contrairement à certains autres frameworks frontend qui vous laissent vous débrouiller pour rendre votre site web plus performant. Le secret de la rapidité de Gatsby réside dans le fait qu'il suit le modèle architectural PRPL, qui signifie :

* **Push** les ressources critiques pour l'URL initiale en utilisant `<link preload>` et http/2.
* **Render** la route initiale.
* **Pre-cache** les routes restantes.
* **Lazy-load** et créer les routes restantes à la demande.

C'est un modèle développé par Google pour structurer et servir des applications web progressives (PWA), avec un accent sur la performance de la livraison et du lancement des applications. Vous pouvez [en lire plus sur ce modèle ici](https://developers.google.com/web/fundamentals/performance/prpl-pattern/).

#### Qu'est-ce qu'Auth0 ?

[Auth0](https://auth0.com), prononcé « Auth Zero », est une plateforme robuste d'authentification et d'autorisation. Elle rend super facile l'ajout de fonctionnalités comme l'inscription des utilisateurs, la récupération de mot de passe, la connexion, la connexion sociale, l'authentification multifacteur, la connexion entreprise, le single sign-on, et plus encore, dans votre application de production.

Auth0 prête une attention particulière à l'expérience des développeurs avec leurs excellents articles de blog et leur documentation robuste et facile à comprendre. Avec Auth0, vous pouvez utiliser diverses normes d'identité :

* **OAuth 1**
* **OAuth 2**
* **Open ID Connect**
* **JSON Web Tokens (JWT)**
* **Security Assertion Markup Language (SAML)**
* **WS-Federation**

Dans ce tutoriel, nous nous concentrerons sur l'utilisation d'une combinaison de **JSON Web Tokens** et de connexions sociales avec **OAuth 2**.

#### Fonctions Serverless et Netlify.

Netlify est une plateforme qui vous permet de déployer votre projet sans vous soucier de certaines charges comme le déploiement continu, les certificats HTTP, et [plus encore](https://www.netlify.com/features/), créée comme un moyen de déployer et de gérer des sites web statiques qui n'ont pas de backend.

Maintenant, parce que tout le monde ne veut pas déployer un site web statique et qu'il y a besoin de support pour un backend, Netlify a ajouté une fonctionnalité appelée « Serverless functions » qui sont des backends où vous n'avez pas à vous soucier de l'infrastructure serveur.

Derrière les scènes, les fonctions Netlify se situent entre vous et quelque chose appelé Amazon Web Services (AWS) Lambda où le vrai « serverless » se produit, et il vit sur la plateforme cloud AWS d'Amazon. Les fonctions Netlify aident à simplifier les choses pour vous, afin que vous n'ayez pas à traiter directement avec AWS et que vous puissiez continuer à utiliser toutes les autres fonctionnalités cool de Netlify comme le déploiement continu.

Le mot « serverless » n'implique pas sans serveur ; cela signifie que vous, en tant que développeur, n'avez pas à vous soucier de l'infrastructure serveur (physique et autre).

Vous pouvez en lire plus sur [Netlify](https://www.netlify.com/) et leurs [Fonctions Serverless](https://www.netlify.com/features/functions/).

#### Notre App : Micro Blog.

![Image](https://cdn-media-1.freecodecamp.org/images/1*RgCKVGa1FIaFvPnUI-9CCA.png)

Notre application s'appelle « Micro Blog ». C'est une plateforme qui permet aux utilisateurs de créer des posts courts et fréquents. Chaque post contient du texte, un nom d'utilisateur et une image de profil de la personne qui fait le post.

N'importe qui peut ouvrir l'application web et voir les posts de tout le monde, mais pour faire un post eux-mêmes, ils doivent se connecter. L'application supporte les connexions sociales et une connexion par email.

Si vous êtes déjà familier avec la plupart de ces choses et que vous voulez voir le code, vous pouvez vous rendre sur [le code source sur Github](https://github.com/THEozmic/micro-blog).

#### Construction du Front-End.

Notre front-end est une application GatsbyJS, et cela signifie que la première chose que nous devons faire est d'installer le package node Gatsby CLI depuis npm.

**Note :** Utilisez la version de node « >= 6.9.0 <7.0.0 || >= 8.9.0 » sinon vous obtenez une erreur lorsque vous essayez de créer un nouveau site Gatsby, cela est dû à la dépendance « css-loader@1.0.1 ».

```
# installer le CLI Gatsby globalement
npm install -g gatsby-cli
```

```
# créer un nouveau site Gatsby en utilisant le démarreur par défaut
gatsby new micro-blog
```

Après que les commandes aient fini de s'exécuter, vous devriez pouvoir entrer dans le répertoire appelé « micro-blog », relatif à l'endroit où vous avez exécuté les commandes ci-dessus.

```
cd micro-blog
```

Lorsque vous regardez le contenu de ce répertoire, vous trouverez un tas de contenu généré. À ce stade, vous pouvez lancer votre site Gatsby et le voir fonctionner. Pour cela, dans votre terminal, exécutez ceci :

```
gatsby develop
```

Cela démarrera votre site Gatsby sur `[http://localhost:8000/](http://localhost:8000/)`.

L'étape suivante consiste à ajouter et modifier le contenu spécifique à notre application.

Nous commencerons par `gatsby-config.js`. Remplacez le contenu du fichier par :

Vous pourriez vouloir mettre à jour la valeur du placeholder de l'auteur « <YOUR NAME> ».

Ce fichier contient les paramètres de votre application Gatsby, des choses comme les métadonnées de votre site et les plugins. C'est un fichier assez important que Gatsby recherche lorsque vous démarrez votre application. Au sein de l'application, nous pouvons utiliser GraphQL pour interroger le contenu de ce fichier.

Ensuite, `src/components/header.js` :

Ce fichier est notre composant d'en-tête partagé. Maintenant, quelques choses se passent ici :

* Nous importons certaines choses de la bibliothèque `gatsby` : `Link` et `navigate`. `Link` est un composant React utilisé pour lier à d'autres pages qui sont dans votre application comme « /app/home », tandis que `navigate` est une fonction qui accepte une URL et navigue de manière programmatique l'utilisateur vers l'URL spécifiée.
* `isLoggedIn`, `logout`, et `getUserNickname` sont des méthodes qui vérifient si l'utilisateur est connecté, déconnectent l'utilisateur, et obtiennent le surnom d'un utilisateur connecté pour des fins d'affichage, respectivement.
* `Button` est un composant qui affiche un élément bouton pour l'utilisateur. Il accepte plusieurs props qui nous aident à donner facilement au bouton des apparences variées.

Voici à quoi ressemble `Button` :

Comme vous le verrez, nous allons utiliser beaucoup [Styled Components](https://emotion.sh/) et spécifiquement `emotion`, qui est l'un des nombreux packages CSS-in-JS supportés pour GatsbyJS.

Plus tard, nous jetterons un coup d'œil à `src/services/auth.js`.

Le fichier suivant à regarder est `/src/components/layout.js` :

Ce fichier est le fichier wrapper pour notre application. Il inclut l'en-tête, un pied de page, et rend les enfants qui lui sont passés. Nous voyons également le package `graphql` importé de `gatsby` ainsi que le composant `StaticQuery`. `StaticQuery` accepte une prop `query` qui est une requête GraphQL. Toute valeur résolue à partir de la `query` est rendue disponible dans la prop render du composant `StaticQuery`.

En regardant de plus près la requête, nous pouvons voir qu'elle obtient des données à partir du fichier `gatsby-config.js`.

Notre CSS accompagnateur `/src/components/layouts.css` reste presque le même que celui généré avec la seule différence étant à la ligne 8 :

```
body {
```

```
   margin: 0;
```

```
   background-color: #f2f9ff;
```

```
}
```

Laissons le répertoire `/src/components` pour l'instant et jetons un coup d'œil à `/src/pages/index.js` :

Tous les fichiers dans `/src/pages/` deviennent des pages dans votre application Gatsby. Par exemple, `index.js` devient la page d'accueil et `/src/pages/app/home.js` devient `[http://yourdomain.com/app/home](http://yourdomain.com/app/home)`.

Sur notre page d'accueil, nous voulons que nos utilisateurs voient les posts récents et leur demander de se connecter ou de s'inscrire s'ils veulent créer un post.

Pour obtenir nos posts récents, nous avons besoin d'`axios`, qui est une bibliothèque basée sur les promesses pour faire des requêtes réseau en JavaScript. Installez `axios` en exécutant ceci dans votre terminal :

```
npm install axios
```

Lorsque notre composant est monté, nous vérifions si l'utilisateur est connecté et nous le redirigeons vers `/app/home` car nous ne voulons pas qu'ils soient sur cette page s'ils sont connectés. Admettons que c'est une approche assez naïve, et nous pourrions utiliser des « Protected Routes » à la place. Utiliser des « Protected Routes » signifie que ce composant n'aura même pas la chance d'être monté du tout. En raison de la petite taille de ce projet, j'ai décidé de ne pas utiliser les Protected Routes.

Au cas où vous voudriez implémenter des Protected Routes dans votre application Gatsby, veuillez vous référer à [ce guide](https://www.gatsbyjs.org/docs/authentication-tutorial/#creating-client-only-routes) sur le site officiel de Gatsby.

Nous créons une requête pour obtenir les posts lorsque notre composant est monté, puis nous mettons à jour l'état avec les données retournées. La mise à jour de l'état provoque le re-rendu de notre composant enfant `RecentPosts` puisque celui-ci utilise ledit état.

Remarquez que l'URI dans la requête réseau pour récupérer les données des posts est une variable d'environnement `process.env.API_URI`. Ces variables d'environnement ne sont pas les variables d'environnement typiques que vous trouvez dans une application Node. Pour créer ces variables d'environnement, vous avez besoin de deux fichiers dans le répertoire racine de votre application Gatsby : `env.production` et `env.development`. Ces fichiers seront automatiquement chargés par Gatsby dans l'environnement approprié lorsque vous démarrez votre application.

Comme je l'ai mentionné précédemment, ces variables d'environnement ne sont pas les mêmes que vos variables d'environnement Node et ce qui les rend différentes est qu'elles ne sont pas des fichiers privés que vous excluez typiquement dans votre fichier `.gitignore`. Vous devez pousser ces fichiers lorsque vous voulez déployer votre application car GatsbyJS aura besoin de lire ces fichiers au démarrage.

Le mien ressemble à ceci :

```
AUTH0_DOMAIN=micro-blog.auth0.com
```

```
AUTH0_CLIENTID=cIovhIQvYOr6fk3yhDtKjB5EiIvLevxf
```

```
REDIRECT_URI='http://localhost:8000/callback'
```

```
API_URI='http://localhost:9000/.netlify/functions/'
```

En production, c'est un peu différent :

```
AUTH0_DOMAIN=micro-blog.auth0.com
```

```
AUTH0_CLIENTID=cIovhIQvYOr6fk3yhDtKjB5EiIvLevxf
```

```
REDIRECT_URI='https://angry-shaw-7a81ce.netlify.com/callback'
```

```
API_URI='https://angry-shaw-7a81ce.netlify.com/.netlify/functions/'
```

Afin d'obtenir ces valeurs pour votre propre application, vous devez [créer un compte Auth0](https://auth0.com/signup) si vous n'en avez pas déjà un.

Notez que vous pouvez utiliser Auth0 gratuitement avec des fonctionnalités limitées.

Après avoir créé un compte, connectez-vous à votre [tableau de bord de gestion Auth0](https://manage.auth0.com/) et créez une nouvelle application Auth0. Vous pouvez le faire en cliquant sur l'élément de menu Applications puis sur le bouton **Créer une application**. Vous pouvez mettre à jour le nom de l'application de « My App » à ce que vous voulez utiliser. Vous pouvez changer cela plus tard si vous le souhaitez. Dans mon cas, j'utilise « Micro Blog ».

Ensuite, vous sélectionnez « Single Page Web App » et cliquez sur **Créer**. Cela créera immédiatement votre application.

![Image](https://cdn-media-1.freecodecamp.org/images/1*i_bqW8WOT-LaCOYYUNMoFA.png)

Une fois que vous avez terminé la création de votre application, vous devriez naviguer vers « Settings », là vous trouverez vos valeurs `**AUTH0_CLIENTID**` et `**AUTH0_DOMAIN**`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*-l_4flPcJdcwMW9Boj2jiA.png)

**Note :** Pour votre `.env.production`, vous n'avez pas les `**REDIRECT_URI**` et `**API_URI**` à ce stade. Plus tard, après avoir créé notre application Netlify, nous obtiendrons l'URL de l'application que nous pourrons ensuite y mettre de manière appropriée.

Maintenant, jetons un coup d'œil à `src/components/recentPosts.js` :

Ici encore, nous utilisons Styled Components. Nous utilisons également une méthode de cycle de vie React `shouldComponentUpdate` pour éviter les re-rendus inutiles lorsque le composant `RecentPosts` est utilisé dans un autre composant.

Lorsque l'utilisateur clique sur le bouton de connexion, nous le redirigeons vers une page de connexion Auth0. Après qu'il ait été authentifié, nous le redirigeons vers une URL dans notre application appelée `/callback` où nous vérifions que l'utilisateur a bien été connecté et enregistrons ses détails dans `localStorage`. Voici à quoi ressemble la page `/callback` :

Nous appelons la méthode `handleAuthentication` qui obtiendra les données de l'URL, les analysera, enregistrera les données extraites dans `localStorage` et appellera ensuite la méthode `() => navigate('/app/home')` pour rediriger l'utilisateur vers l'application principale.

Maintenant, nous regardons la page `/pages/app/home.js`, où seuls les utilisateurs connectés peuvent accéder :

Il n'y a pas grand-chose de nouveau ici. Les seules choses que je mentionnerais sont :

* Nous créons de nouveaux posts dans la méthode `handlePostSubmit` et là, nous faisons un appel `axios` régulier mais avec une option `headers` contenant le jeton JWT « id_token ». Nous faisons cela car, dans notre fonction Serverless, nous aurons besoin de cette valeur dans les en-têtes pour authentifier une requête, en nous assurant qu'un seul utilisateur connecté peut créer un nouveau post et que le jeton enregistré côté client est effectivement valide et non falsifié. Cela améliore grandement la sécurité et la fiabilité de notre application.
* Nous redirigeons l'utilisateur vers `/` lorsqu'ils ne sont pas correctement connectés et qu'ils parviennent à atterrir sur cette page. Nous faisons cela dans la méthode de cycle de vie `componentDidMount`. Encore une fois, les [Protected Routes](https://www.gatsbyjs.org/docs/authentication-tutorial/#creating-client-only-routes) sont une meilleure option dans vos applications de production.

Enfin, nous arrivons à `/src/services/auth.js`. Nous avons utilisé des fonctions de ce fichier tout au long de l'application, il est temps de le regarder :

Dans ce fichier, nous utilisons `auth0-js`, une bibliothèque JavaScript d'Auth0 pour gérer les parties d'authentification de notre application. Ajoutez-la à votre application en exécutant ceci dans votre terminal :

```
npm install auth0-js
```

La prochaine chose que vous voyez dans ce fichier est la création de `isBrowser` qui indique si notre fichier est actuellement exécuté dans le contexte d'un navigateur. Cela est important car pendant le processus de construction, vous pourriez rencontrer des erreurs en essayant d'appeler des choses comme `window.localStorage`.

Regardons quelques-unes des méthodes de ce fichier :

La méthode `getUser` obtient les détails de l'utilisateur à partir du jeton d'accès précédemment stocké dans le `localStorage`, après que notre utilisateur ait été connecté. Elle utilise la méthode `getAccessToken` pour récupérer le jeton d'accès stocké.

La méthode `handleLogin` est appelée lorsque l'utilisateur essaie de se connecter. Elle le redirige vers la page de connexion Auth0 qui, à son tour, redirige l'utilisateur vers `/callback` une fois qu'il a été connecté.

La méthode `isLoggedIn` vérifie que la date d'expiration du jeton JWT « id_token » enregistrée dans `localStorage` sous `expiresAt` n'a pas été dépassée, invalidant ainsi la session de l'utilisateur.

La méthode `handleAuthentication` est celle que vous voyez utilisée dans la page `/callback`. Cette méthode analyse le hash de l'URL et obtient des valeurs importantes que nous enregistrons ensuite dans `localStorage` dans la méthode `setSession`.

Enfin, la méthode `logout` déconnecte l'utilisateur en supprimant les identifiants enregistrés. Cela fonctionne bien, mais vous pourriez aller plus loin en [appelant un endpoint sur Auth0](https://auth0.com/docs/api/authentication#logout) qui invalidera complètement la session. Je me suis arrêté ici pour le bien de ce tutoriel.

Enfin, nous mettons à jour la ligne 6 sur `/src/components/seo.js` :

```
const SEO = ({ description = null, lang = "eng", meta = [], keywords = [], title }) => {
```

En utilisant une fonction fléchée ES6 et des valeurs par défaut.

#### Construction du Back-End.

Ensuite, nous allons construire une API pour servir une liste de posts et pour collecter de nouveaux posts. Ce sont des fonctions serverless hébergées sur Netlify. Notre API doit faire quelques choses :

* Avoir un endpoint pour servir la liste des posts : `/.netlify/functions/postsRead`.
* Avoir un endpoint pour collecter de nouveaux posts : `/.netlify/functions/postsCreate`.
* Authentifier les requêtes pour créer de nouveaux posts en utilisant Auth0.

Pour commencer, nous devons installer quelques packages npm :

```
npm install netlify-lambda mongoose jwks-rsa jsonwebtoken dotenv
```

L'étape suivante consiste à créer un répertoire appelé `utils` dans le répertoire racine de notre application Gatsby. Dans ce répertoire se trouveront nos fichiers qui ne sont pas tout à fait l'API. L'un de ces fichiers est notre fichier `/utils/db.js` :

Dans ce fichier, nous établissons une connexion à notre base de données MongoDB.

Il manque quelque chose ici, notre fichier `.env` (oui, un troisième !). Le mien ressemble à ceci :

```
DATABASE_PROD='mongodb://<username>:<password>@<db_url>'
DATABASE_DEV='mongodb://localhost:27017/micro-blog'
```

J'utilise [mLab](https://mlab.com) pour héberger ma base de données en ligne et j'ai [MongoDB](https://www.mongodb.com/) installé sur ma machine de développement. Vous pouvez suivre ce [guide pour installer MongoDB](https://docs.mongodb.com/v3.2/administration/install-community/) sur votre machine de développement également.

Le fichier suivant sur lequel se concentrer est `/utils/index.js`, ce fichier contient d'autres méthodes que nous utiliserons dans nos fonctions Netlify.

La première méthode `respondWith` abstrait la logique de réponse aux requêtes qui atteignent nos fonctions Netlify. Et la deuxième méthode `verifyToken` vérifie que les jetons envoyés dans les en-têtes des requêtes sont valides.

Enfin, les fonctions Netlify. Créez un nouveau répertoire dans la racine de votre application appelé `functions` (ou autre chose que vous trouvez attrayant) et dans ce répertoire, créez trois fichiers :

* `postsCreate.js`
* `postsRead.js`
* `postsModel.js`

Les deux premiers fichiers contiendront notre implémentation pour la création et la lecture des posts tandis que le dernier fichier décrira notre schéma de base de données des posts.

Voici à quoi ressemble le fichier `postsModel.js` :

Et `postsCreate.js` :

Enfin, `postsRead.js` :

Maintenant, pour exécuter nos fonctions localement, nous créons d'abord un nouveau script dans notre fichier `package.json` :

```
"scripts": {
  // autres scripts
```

```
  "start:lambda": "NODE_ENV=development netlify-lambda serve functions"
```

```
}
```

J'utilise « serve functions » car le répertoire « functions » est l'endroit où je mets mes fonctions Netlify, le vôtre pourrait être différent.

Après avoir créé ce script, nous l'exécutons dans notre terminal :

```
npm run start:lambda
```

#### **Déploiement de l'application.**

La dernière chose que nous ferons est de déployer notre application sur Netlify et pour cela, nous devons d'abord créer un fichier à la racine de notre application appelé `netlify.toml`. Ce fichier est un fichier de configuration que Netlify lira lors de la construction et du déploiement de l'application. Voici à quoi ressemble ce fichier :

```
[build]
  functions = "lambda"
  Command = "npm run prod"
```

La ligne `functions = lambda` indique à Netlify de mettre les fonctions construites dans un dossier appelé « lambda ». Et la ligne `Command = "npm run prod"` spécifie un script à exécuter afin de construire l'ensemble de l'application. Cela est assez important car nous devons construire à la fois notre application Gatsby et nos fonctions Netlify. Voici à quoi ressemble ce script dans notre `package.json` :

```
"scripts": {
```

```
  // scripts précédents
```

```
  "build:lambda": "netlify-lambda build functions",
```

```
  "prod": "NODE_ENV=production npm run build; npm run build:lambda"
```

Ici, nous exécutons d'abord `npm run build` qui construit notre application Gatsby, puis nous exécutons `npm run build:lambda` qui construit nos fonctions Netlify. Encore une fois, ici j'utilise « functions » car c'est le nom du dossier où je mets mes fonctions Netlify.

Après avoir fait tout cela, nous créons un nouveau dépôt Github et poussons notre code là-bas. [Créez un nouveau compte Netlify](https://app.netlify.com/signup) si vous n'en avez pas déjà un. Je préfère utiliser l'option d'inscription Github dans ce cas. Lorsque vous êtes connecté, vous cliquez sur le bouton **Nouveau site depuis Git** qui vous guidera ensuite à travers le processus de création d'une nouvelle application Netlify.

![Image](https://cdn-media-1.freecodecamp.org/images/1*2qwvW3hrPYdewA7WPRPedg.png)

Si, lors du processus de création d'une nouvelle application Netlify, vous ne trouvez pas votre dépôt dans la liste affichée, assurez-vous d'avoir donné à Netlify l'accès à tous vos dépôts ou au moins à ce dépôt en particulier.

![Image](https://cdn-media-1.freecodecamp.org/images/1*JUqE4yBnsBu-I5gOH4yNVA.png)

Avant de déployer, cliquez sur le bouton **Afficher les options avancées** et créez une nouvelle variable appelée `DATABASE_PROD`, en définissant la valeur sur ce qui se trouve dans votre fichier `.env`. N'oubliez pas que ce fichier est exclu de votre application dans votre `.gitignore`, donc il n'y a aucun moyen pour votre application de lire cette valeur à moins que vous ne le fassiez.

De plus, ajoutez `public/` comme répertoire de publication puisque c'est le répertoire où Gatsby construit et dépose les fichiers.

![Image](https://cdn-media-1.freecodecamp.org/images/1*n0H9KJFp5bQoIZoaX8VqEg.png)

Netlify gérera automatiquement le déploiement des fonctions. Après que l'application ait été déployée, vous devriez voir l'URL de votre application sur votre tableau de bord.

![Image](https://cdn-media-1.freecodecamp.org/images/1*eivTZZNT6DcTMvAg8JczoA.png)

Et maintenant que vous avez l'URL de l'application, vous pouvez mettre à jour votre fichier `.env.production` en conséquence.

Merci d'avoir lu !