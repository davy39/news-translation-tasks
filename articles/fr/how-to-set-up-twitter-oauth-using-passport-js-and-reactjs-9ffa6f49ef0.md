---
title: Comment configurer Twitter OAuth en utilisant Passport.js et ReactJS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-03T16:23:29.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-twitter-oauth-using-passport-js-and-reactjs-9ffa6f49ef0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*hYMUC_9w-Szc075Uztq2bw.jpeg
tags:
- name: authentication
  slug: authentication
- name: JavaScript
  slug: javascript
- name: passportjs
  slug: passportjs
- name: React
  slug: reactjs
- name: technology
  slug: technology
seo_title: Comment configurer Twitter OAuth en utilisant Passport.js et ReactJS
seo_desc: 'By Leanne Zhang

  Getting started

  This is a simple authentication tutorial for building a Twitter Authentication web
  application using Passport API. It’s a side project that I worked on for education
  purposes.

  I broke down this tutorial into two parts....'
---

Par Leanne Zhang

### **Mise en route**

Ce didacticiel est un guide simple pour créer une application web d'authentification Twitter en utilisant [Passport API](http://www.passportjs.org/packages/passport-twitter/). C'est un projet secondaire sur lequel j'ai travaillé à des fins éducatives.

J'ai divisé ce didacticiel en deux parties. La première partie se concentre sur la création de routes d'authentification dans le backend. La deuxième partie se concentre sur la création de composants UI dans le front-end en utilisant React.

#### **Stack Technique**

* Côté Serveur : [Node.js](https://nodejs.org/en/), [Express.js](https://expressjs.com/), [Passport Twitter API](http://www.passportjs.org/packages/passport-twitter/), [MongoDB](https://www.mongodb.com/),
* Client : [ReactJS](https://reactjs.org/)

#### **Que allons-nous construire ?**

* L'utilisateur clique sur le bouton de connexion qui le redirige vers la page d'authentification Twitter OAuth.
* Une fois l'OAuth authentifié avec succès auprès de Twitter, l'utilisateur sera redirigé vers la page d'accueil de l'application web.

![Image](https://cdn-media-1.freecodecamp.org/images/DT6OHJBlHLyZ1cMi9iU5S7-WXsToLAP5o1mn)
_Authentification via passport-twitter_

[_Passport.js._](http://www.passportjs.org/) _offre des API d'authentification à d'autres fournisseurs de services OAuth tels que Google et Facebook. Par exemple, j'ai choisi d'utiliser Twitter comme fournisseur de services OAuth._

#### **Qu'est-ce que OAuth ?**

Open Authorization est un standard pour accorder à votre application web l'accès à un service de connexion tiers comme Twitter, Facebook ou Google, qui retourne un jeton OAuth. Un jeton OAuth est une information d'identification qui peut être utilisée par une application pour accéder à une API de service externe.

Dans ce projet, j'utilise le middleware `passport-twitter` pour gérer l'authentification Twitter en utilisant l'API OAuth 1.0, car cela permet de gagner du temps et de gérer tout le processus d'authentification complexe en arrière-plan.

#### Quels sont les points de terminaison du serveur ?

**/auth/twitter** — authentification via passport twitter

**/auth/login/success** — retourne une réponse de succès de connexion avec les informations de l'utilisateur

**/auth/login/failed** — retourne un message d'échec de connexion

**/auth/logout** — déconnexion et redirection vers la page d'accueil du client

**/auth/twitter/redirect** — redirection vers la page d'accueil si la connexion a réussi ou redirection vers _/auth/login/failed_ en cas d'échec

#### Diagramme d'Architecture

Voici un aperçu du diagramme d'architecture que nous allons examiner plus en détail.

![Image](https://cdn-media-1.freecodecamp.org/images/2ZnSn0-X1F2Unvll-wTomYQJl-jPG3cT8jSx)
_Diagramme d'Architecture_

#### Structure du Projet

J'ai séparé la logique du serveur et du client dans différents dossiers pour plus de clarté et de propreté. Mon **serveur** fonctionne sur _localhost:4000_, tandis que le **client** fonctionne sur _localhost:3000_. (N'hésitez pas à définir votre propre port.)

```
|-- twitter-auth-project|   |-- server|   |   |-- index.js|   |   |-- package.json|   |-- client|   |   |-- src|   |   |   |-- index.jsx|   |   |   |-- package.json
```

### Mise en œuvre

#### **Partie 1 : Enregistrer votre application en tant que fournisseur OAuth sur le site des applications Twitter**

Tout d'abord, enregistrez votre application sur [Twitter Application Management](https://apps.twitter.com/). Vous recevrez une clé de consommateur (clé API) et un secret de consommateur (secret API) que vous pourrez utiliser dans la stratégie passport plus tard.

Vous devrez également configurer une URL de rappel. Il s'agit de l'URL de rappel après que l'OAuth a été authentifié avec succès.

À des fins de développement local, j'ai personnalisé mes URL de rappel pour qu'elles soient l'URL du client, qui est **localhost:3000**.

![Image](https://cdn-media-1.freecodecamp.org/images/wgnQM7zKUznjvIjAK976b1Mqbm3t2Ipct1RP)
_[https://developer.twitter.com/en/apps/create](https://developer.twitter.com/en/apps/create" rel="noopener" target="_blank" title=")_

#### **Partie 2 : Configurer le serveur Express pour l'authentification Twitter**

J'ai choisi [Express.js](https://expressjs.com/) pour configurer le serveur en backend. **Express.js** est un framework d'application web pour Node.js conçu pour construire des API.

```
|-- server|   |-- config|   |   |-- keys.js|   |   |-- passport-setup.js|-- |-- models|   |   |-- user-model.js|   |-- routes|   |   |-- auth-routes.js|   |-- index.js|   |-- package.json
```

`npm install express` pour installer un serveur [express](https://expressjs.com/en/starter/hello-world.html). Le serveur fonctionne sur _http://localhost:4000_.

`index.js` est le point d'entrée pour tous les points de terminaison du serveur.

`/routes/auth-routes.js` contient tous les points de terminaison d'authentification.

`/config/keys.js` contient toutes les clés de consommateur de l'API Twitter et les configurations de la base de données. _Vous pouvez les copier et mettre vos propres clés._

#### **Partie 3 : Configurer les routes d'authentification**

Précédemment dans la section « Quels sont les points de terminaison du serveur ? », nous avons identifié les points de terminaison d'authentification pour l'API Twitter.

> **/auth/twitter** — authentification via passport twitter

> **/auth/login/success** — retourne une réponse de succès de connexion avec les informations de l'utilisateur

> **/auth/login/failed** — retourne un message d'échec de connexion

> **/auth/logout** — déconnexion et redirection vers la page d'accueil du client

> **/auth/twitter/redirect** — redirection vers la page d'accueil si la connexion a réussi ou vers _/auth/login/failed_ en cas d'échec

Mettons-les en pratique.

`/routes/auth-routes.js`

Dans `index.js`, importer `routes/auth-routes`,

`npm install cors` — support du navigateur cross-origin

#### **Partie 4 : Configurer la stratégie Twitter en utilisant l'API Passport**

[**API Passport**](http://www.passportjs.org/docs/) est un middleware que nous utilisons pour nous authentifier via Twitter OAuth. L'API Passport gère l'authentification de connexion en arrière-plan, vous n'avez donc pas besoin de gérer la logique complexe. Elle dispose également de différentes stratégies d'authentification (par exemple, GoogleStrategy, FacebookStrategy). Dans mon exemple, j'ai choisi d'utiliser [TwitterStrategy](http://www.passportjs.org/docs/twitter/) pour me connecter via un compte Twitter.

#### **Partie 5 : Configurer et connecter une base de données**

Lorsque le système authentifie avec succès l'utilisateur via PassportAPI, il devra stocker l'utilisateur dans une base de données afin de pouvoir récupérer ces informations utilisateur pour le client.

![Image](https://cdn-media-1.freecodecamp.org/images/olggPPJCKJy8Y39CLOIoZcJv5EcPiAa2qLPN)
_diagramme d'architecture_

J'utilise MongoDB pour stocker les informations de connexion de l'utilisateur.

Partie 5.1 — Inscrivez-vous sur mlab et suivez les instructions ici : [**https://mlab.com/**](https://mlab.com/)

Partie 5.2 — Ajoutez les identifiants MongoDB dans `keys.js`

Partie 5.3 — Établissez une connexion MongoDB en utilisant mongoose

`npm install mongoose` pour se connecter à MongoDB.

> _"Mongoose fournit une solution simple et basée sur un schéma pour modéliser les données de votre application. Il inclut le typage intégré, la validation et la construction de requêtes."_ ([https://mongoosejs.com/](https://mongoosejs.com/))

Partie 5.4 — Créez un modèle d'objet utilisateur qui représente le profil utilisateur dans l'enregistrement de la base de données

`/models/user-model.js`

#### **Partie 6 : Enregistrer et récupérer l'utilisateur d'une base de données**

Une fois que l'API Passport a authentifié avec succès via Twitter OAuth, notre serveur enregistre les informations de l'utilisateur dans MongoDB. Si cet utilisateur existe déjà, le système trouve simplement l'utilisateur actuel dans la base de données et retourne l'utilisateur au client. Tout cela est fait en utilisant les API mongoose.

`/config/passport-setup.js`

#### **Partie 7 : Utiliser la session client pour stocker la session de cookie**

Chaque fois que l'utilisateur se connecte à un site web, le navigateur se souvient de ces informations utilisateur afin que l'utilisateur n'ait pas besoin de se reconnecter. La manière dont cet utilisateur est mémorisé est par le biais d'un cookie HTTP. Un cookie HTTP contient des données cryptées sur l'utilisateur et la durée de la session.

Si vous vous connectez à une page web et ouvrez les DevTools, vous pouvez voir que les cookies ont été définis dans le navigateur.

![Image](https://cdn-media-1.freecodecamp.org/images/u1oOba61pi1OvWgDmeQMWUOobbNl7JsG4w2r)
_Après une connexion réussie, les cookies sont définis dans le navigateur. Ouvrez DevTools, allez dans Application | Cookies._

La sérialisation et la désérialisation sont des concepts importants à connaître. La **sérialisation** est le processus par lequel l'utilisateur est crypté à partir de la base de données et envoyé au navigateur sous forme de cookie. La **désérialisation** est le processus par lequel le cookie utilisateur est décrypté du navigateur vers la base de données.

Afin de supporter les sessions de connexion, Passport va sérialiser et désérialiser l'instance utilisateur vers et depuis la session.

`/config/passport-setup.js`

Voici le fichier `index.js` final utilisant cookie-session.

J'ai choisi d'utiliser `cookie-session` comme middleware pour stocker les données de session sur le client.

```
$ npm install cookie-session
```

Utilisez également cookieSession dans `index.js`

```
app.use(cookieSession({  name: 'session',  keys: [/* secret keys */],  maxAge: 24 * 60 * 60 * 1000 // session expirera après 24 heures}))
```

`passport.session()` agit comme un middleware pour modifier l'objet req et changer la valeur utilisateur cryptée qui est actuellement la signature de session (à partir du cookie client) en un objet utilisateur.

_Étape optionnelle :_

J'ai personnalisé l'URL racine localhost:4000/ pour afficher un message de succès si la connexion est correcte, sinon affiche un message d'échec.

### **Étape suivante : Client — Configurer la page de connexion et la page de déconnexion en utilisant React**

J'ai construit les composants front-end en utilisant [React](https://reactjs.org/), et [React Router](https://github.com/ReactTraining/react-router) pour configurer les liens.

![Image](https://cdn-media-1.freecodecamp.org/images/yrUyRcfvEDo8aYJSDidulrhgCzUV1p90EVyH)
_Page de connexion et page de déconnexion_

#### **Fonctionnalité**

La page contient un en-tête avec un bouton d'accueil et de connexion/déconnexion. Initialement, la page affichera le message de "bienvenue" et le bouton "connexion". Une fois que l'utilisateur s'est authentifié via l'authentification Twitter, il affichera le nom d'utilisateur et le bouton "déconnexion".

#### Configuration du client

```
client|-- src|   |-- components|   |   |-- Header.jsx|   |   |-- Homepage.jsx|   |-- App.js|   |-- AppRouter.js|   |-- index.js|   |-- index.css|   |-- serviceWorker.js|-- package.json
```

#### Identifier les composants UI

![Image](https://cdn-media-1.freecodecamp.org/images/UHGcoXjPC61QZx7nWr7aPR13FHhDDGLNr7Lv)
_Composants UI_

* HomePage : un conteneur qui affiche les messages de bienvenue et les informations utilisateur. Appelle le point de terminaison _/auth/login/success_. Si le point de terminaison réussit, les informations utilisateur seront stockées dans l'objet _user_ et l'état de _authenticated_ sera défini sur _true_. La page affiche un message indiquant que "Vous êtes connecté avec succès". Si le point de terminaison échoue, l'utilisateur n'est pas authentifié et la page affiche "Bienvenue".
* Header : Il gère la navigation. Lorsque l'utilisateur est authentifié, "connexion" sera changé en "déconnexion". L'état _authenticated_ est passé de HomePage en tant que prop.

#### Mise en œuvre

HomePage.jsx : un conteneur qui affiche les messages de bienvenue et les informations utilisateur

Header.jsx — composant de navigation

Enfin, configurez la route qui navigue vers HomePage dans AppRouter.jsx et App.jsx

Merci beaucoup d'avoir lu cet article de blog. J'espère que vous l'avez trouvé utile.

L'ensemble du projet est disponible sur mon Github : [https://github.com/leannezhang/twitter-authentication](https://github.com/leannezhang/twitter-authentication)

Si vous avez des commentaires ou des retours, n'hésitez pas à commenter ci-dessous ou à me contacter.

Twitter : @ liyangz

#### Matériel de lecture

* [Exemple Passport Twitter](https://github.com/passport/express-4.x-twitter-example)
* [Passport Twitter](https://github.com/jaredhanson/passport-twitter)
* [Didacticiel de l'API Passport Google](https://youtu.be/sakQbeRjgwg)