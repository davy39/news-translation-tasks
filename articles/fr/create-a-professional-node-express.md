---
title: Comment créer une solution d'API de chat professionnelle avec des Sockets dans
  NodeJS [Niveau débutant]
date: '2020-06-16T23:47:21.000Z'
author: freeCodeCamp
authorURL: https://www.freecodecamp.org/news/author/adeel/
originalURL: https://freecodecamp.org/news/create-a-professional-node-express
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a39740569d1a4ca2455.jpg
tags:
- name: backend
  slug: backend
- name: Express.js
  slug: expressjs
- name: node js
  slug: node-js
- name: Node.js
  slug: nodejs
- name: REST API
  slug: rest-api
- name: SocketIO
  slug: socketio
- name: websocket
  slug: websocket
seo_desc: 'By Adeel Imran

  Have you ever wondered how chat applications work behind the scenes? Well, today
  I am going to walk you through how to make a REST + Sockets-based application built
  on top of NodeJS/ExpressJS using MongoDB.

  I have been working on the c...'
---


Vous êtes-vous déjà demandé comment fonctionnent les applications de chat en coulisses ? Eh bien, aujourd'hui, je vais vous expliquer comment créer une application basée sur REST + Sockets, construite sur [NodeJS][1]/[ExpressJS][2] en utilisant [MongoDB][3].

<!-- more -->

Je travaille sur le contenu de cet article depuis plus d'une semaine maintenant – j'espère vraiment qu'il aidera quelqu'un.

## Prérequis

-   Configurez MongoDB sur votre machine \[[Guide d'installation écrit ici][4]\]
-   Pour les utilisateurs Windows, vous trouverez le guide d'installation \[[ici][5]\]
-   Pour les utilisateurs macOS, vous trouverez le guide d'installation \[[ici][6]\]\[[L'installation directe que j'ai écrite][7]\]
-   Pour les utilisateurs Linux, vous trouverez le guide d'installation \[[ici][8]\]
-   Installez Node/NPM sur votre machine \[[Lien d'installation ici][9]\] (J'utilise la version Node v12.18.0)

## Sujets abordés

### Général

-   Créer un serveur Express
-   Comment effectuer les validations d'API
-   Créer le squelette de base pour l'ensemble de l'application
-   Configuration de MongoDB (installation, configuration dans Express)
-   Création de l'API utilisateurs + Base de données (Créer un utilisateur, Obtenir un utilisateur par ID, Obtenir tous les utilisateurs, Supprimer un utilisateur par ID)
-   Comprendre ce qu'est un middleware
-   Authentification JWT (JSON Web Tokens) (décodage/encodage) - Middleware de connexion
-   Classe Web Socket qui gère les événements lorsqu'un utilisateur se déconnecte, ajoute son identité, rejoint une salle de chat, souhaite mettre une salle de chat en sourdine
-   Discussion sur le modèle de base de données des salles de chat et des messages

### Pour l'API

-   Initier un chat entre utilisateurs
-   Créer un message dans une salle de chat
-   Voir la conversation d'une salle de chat par son ID
-   Marquer une conversation entière comme lue (similaire à WhatsApp)
-   Obtenir les conversations récentes de tous les chats (similaire à Facebook Messenger)

### Bonus - API

-   Supprimer une salle de chat par ID ainsi que tous ses messages associés
-   Supprimer un message par ID

Avant de commencer, je voulais aborder quelques notions de base dans les vidéos suivantes.

### Comprendre les bases d'ExpressJS

Que sont les routes ? Les contrôleurs ? Comment autorisons-nous le CORS (partage de ressources entre origines multiples) ? Comment permettons-nous à l'utilisateur final d'envoyer des données au format JSON dans une requête API ?

Je parle de tout cela et plus encore (y compris les conventions REST) dans cette vidéo :

<iframe width="480" height="270" src="https://www.youtube.com/embed/t7-yuYFVG1Y?feature=oembed" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" name="fitvid0"></iframe>

De plus, voici un [lien GitHub vers l'intégralité du code source de cette vidéo][10] \[Chapitre 0\]

Jetez un œil au fichier README.md pour le code source du "Chapitre 0". Il contient tous les liens d'apprentissage pertinents que je mentionne dans la vidéo ainsi qu'un excellent tutoriel d'une demi-heure sur Postman.

### Ajouter la validation d'API à votre point de terminaison d'API

Dans la vidéo ci-dessous, vous apprendrez à écrire votre propre validation personnalisée à l'aide d'une bibliothèque appelée "make-validation" :

<iframe width="480" height="270" src="https://www.youtube.com/embed/t-KGXLM0YlE?feature=oembed" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" name="fitvid1"></iframe>

Voici le [lien GitHub vers l'intégralité du code source de cette vidéo][11] \[Chapitre 0\].

Et voici le lien de la bibliothèque **make-validation** \[G[itHub][12]\]\[[npm][13]\]\[[exemple][14]\].

L'intégralité du code source de ce tutoriel peut être consultée **[ici][15]**. Si vous avez des commentaires, n'hésitez pas à me contacter sur [http://twitter.com/adeelibr][16]. Si vous aimez ce tutoriel, merci de laisser une étoile sur le [**répertoire GitHub**][17]**.**

Commençons maintenant que vous connaissez les bases d'ExpressJS et comment valider une réponse utilisateur.

## Mise en route

Créez un dossier appelé `chat-app` :

```
mkdir chat-app;
cd chat-app;
```

Ensuite, initialisez un nouveau projet npm dans le dossier racine de votre projet en tapant ce qui suit :

```
npm init -y
```

et installez les paquets suivants :

```
npm i cors @withvoid/make-validation express jsonwebtoken mongoose morgan socket.io uuid --save;
npm i nodemon --save-dev;
```

Et dans la section `scripts` de votre `package.json`, ajoutez les 2 scripts suivants :

```
"scripts": {
	"start": "nodemon server/index.js",
	"start:server": "node server/index.js"
},
```

Votre `package.json` devrait maintenant ressembler à ceci :

```
{
  "name": "chapter-1-chat",
  "version": "0.0.0",
  "private": true,
  "type": "module",
  "scripts": {
    "start": "nodemon server/index.js",
    "start:server": "node server/index.js"
  },
  "dependencies": {
    "@withvoid/make-validation": "1.0.5",
    "cors": "2.8.5",
    "express": "4.16.1",
    "jsonwebtoken": "8.5.1",
    "mongoose": "5.9.18",
    "morgan": "1.9.1",
    "socket.io": "2.3.0",
    "uuid": "8.1.0"
  },
  "devDependencies": {
    "nodemon": "2.0.4"
  }
}
```

Génial !

Maintenant, dans le dossier racine de votre projet, créez un nouveau dossier appelé `server` :

```
cd chat-app;
mkdir server;
cd server;
```

À l'intérieur de votre dossier `server`, créez un fichier appelé `index.js` et ajoutez-y le contenu suivant :

```
import http from "http";
import express from "express";
import logger from "morgan";
import cors from "cors";
// routes
import indexRouter from "./routes/index.js";
import userRouter from "./routes/user.js";
import chatRoomRouter from "./routes/chatRoom.js";
import deleteRouter from "./routes/delete.js";
// middlewares
import { decode } from './middlewares/jwt.js'

const app = express();

/** Get port from environment and store in Express. */
const port = process.env.PORT || "3000";
app.set("port", port);

app.use(logger("dev"));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));

app.use("/", indexRouter);
app.use("/users", userRouter);
app.use("/room", decode, chatRoomRouter);
app.use("/delete", deleteRouter);

/** catch 404 and forward to error handler */
app.use('*', (req, res) => {
  return res.status(404).json({
    success: false,
    message: 'API endpoint doesnt exist'
  })
});

/** Create HTTP server. */
const server = http.createServer(app);
/** Listen on provided port, on all network interfaces. */
server.listen(port);
/** Event listener for HTTP server "listening" event. */
server.on("listening", () => {
  console.log(`Listening on port:: http://localhost:${port}/`)
});
```

Ajoutons les routes pour `indexRouter`, `userRouter`, `chatRoomRouter` & `deleteRouter`.

Dans le dossier racine de votre projet, créez un dossier appelé `routes`. À l'intérieur du dossier `routes`, ajoutez les fichiers suivants :

-   `index.js`
-   `user.js`
-   `chatRoom.js`
-   `delete.js`

Ajoutons d'abord le contenu pour `routes/index.js` :

```
import express from 'express';
// controllers
import users from '../controllers/user.js';
// middlewares
import { encode } from '../middlewares/jwt.js';

const router = express.Router();

router
  .post('/login/:userId', encode, (req, res, next) => { });

export default router;
```

Ajoutons ensuite le contenu pour `routes/user.js` :

```
import express from 'express';
// controllers
import user from '../controllers/user.js';

const router = express.Router();

router
  .get('/', user.onGetAllUsers)
  .post('/', user.onCreateUser)
  .get('/:id', user.onGetUserById)
  .delete('/:id', user.onDeleteUserById)

export default router;
```

Et maintenant, ajoutons le contenu pour `routes/chatRoom.js` :

```
import express from 'express';
// controllers
import chatRoom from '../controllers/chatRoom.js';

const router = express.Router();

router
  .get('/', chatRoom.getRecentConversation)
  .get('/:roomId', chatRoom.getConversationByRoomId)
  .post('/initiate', chatRoom.initiate)
  .post('/:roomId/message', chatRoom.postMessage)
  .put('/:roomId/mark-read', chatRoom.markConversationReadByRoomId)

export default router;
```

Enfin, ajoutons le contenu pour `routes/delete.js` :

```
import express from 'express';
// controllers
import deleteController from '../controllers/delete.js';

const router = express.Router();

router
  .delete('/room/:roomId', deleteController.deleteRoomById)
  .delete('/message/:messageId', deleteController.deleteMessageById)

export default router;
```

Génial, maintenant que nos routes sont en place, ajoutons les contrôleurs pour chaque route.

Créez un nouveau dossier appelé `controllers`. À l'intérieur de ce dossier, créez les fichiers suivants :

-   `user.js`
-   `chatRoom.js`
-   `delete.js`

Commençons par `controllers/user.js` :

```
export default {
  onGetAllUsers: async (req, res) => { },
  onGetUserById: async (req, res) => { },
  onCreateUser: async (req, res) => { },
  onDeleteUserById: async (req, res) => { },
}
```

Ensuite, ajoutons le contenu dans `controllers/chatRoom.js` :

```
export default {
  initiate: async (req, res) => { },
  postMessage: async (req, res) => { },
  getRecentConversation: async (req, res) => { },
  getConversationByRoomId: async (req, res) => { },
  markConversationReadByRoomId: async (req, res) => { },
}
```

Et enfin, ajoutons le contenu pour `controllers/delete.js` :

```
export default {
  deleteRoomById: async (req, res) => {},
  deleteMessageById: async (req, res) => {},
}
```

Jusqu'à présent, nous avons ajouté des contrôleurs vides pour chaque route, ils ne font donc pas encore grand-chose. Nous ajouterons les fonctionnalités dans un instant.

Encore une chose – ajoutons un nouveau dossier appelé `middlewares` et à l'intérieur de ce dossier, créons un fichier appelé `jwt.js`. Ajoutez ensuite le contenu suivant :

```
import jwt from 'jsonwebtoken';

export const decode = (req, res, next) => {}

export const encode = async (req, res, next) => {}
```

Je parlerai de ce que fait ce fichier dans un instant, alors pour l'instant, ignorons-le.

![0f2621f3fad63457842f817f81df58ec](https://www.freecodecamp.org/news/content/images/2020/06/0f2621f3fad63457842f817f81df58ec.gif)

Nous en avons terminé avec notre structure de base du code.

Nous avons fini par faire ce qui suit :

-   Créé un serveur Express qui écoute sur le port 3000
-   Ajouté le partage de ressources entre origines multiples (CORS) à notre `server.js`
-   Ajouté un logger à notre `server.js`
-   Et également ajouté des gestionnaires de routes avec des contrôleurs vides.

Rien de bien sorcier que je n'aie pas déjà couvert dans les vidéos ci-dessus.

## Configuration de MongoDB dans notre application

Avant d'ajouter MongoDB à notre code, assurez-vous qu'il est installé sur votre machine en suivant l'un des guides suivants :

-   Pour les utilisateurs Windows \[[ici][18]\]
-   Pour les utilisateurs macOS \[[ici][19]\]\[[L'installation directe que j'ai écrite][20]\]
-   Pour les utilisateurs Linux \[[ici][21]\]

Si vous rencontrez des problèmes pour installer MongoDB, faites-le-moi savoir sur [https://twitter.com/adeelibr][22] et j'écrirai un guide personnalisé pour vous ou je ferai une vidéo d'installation. :)

J'utilise [Robo3T][23] comme interface graphique pour MongoDB.

Maintenant, vous devriez avoir votre instance MongoDB en cours d'exécution et [Robo3T][24] installé. (Vous pouvez utiliser n'importe quel client graphique que vous aimez. J'aime beaucoup [Robo3T][25], donc je l'utilise. De plus, c'est open source.)

Voici une petite vidéo que j'ai trouvée sur YouTube qui donne une introduction de 6 minutes à [Robo3T][26] :

<iframe width="480" height="270" src="https://www.youtube.com/embed/DKZr1Urs7sA?feature=oembed" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" name="fitvid2"></iframe>

Une fois que votre instance MongoDB est opérationnelle, commençons à intégrer MongoDB dans notre code également.

Dans votre dossier racine, créez un nouveau dossier appelé `config`. À l'intérieur de ce dossier, créez un fichier appelé `index.js` et ajoutez le contenu suivant :

```
const config = {
  db: {
    url: 'localhost:27017',
    name: 'chatdb'
  }
}

export default config
```

Habituellement, le port par défaut sur lequel les instances `MongoDB` s'exécutent est `27017`.

Ici, nous définissons les informations sur l'URL de notre base de données (qui se trouve dans `db`) et le nom de la base de données qui est `chatdb` (vous pouvez l'appeler comme vous voulez).

Ensuite, créez un nouveau fichier appelé `config/mongo.js` et ajoutez le contenu suivant :

```
import mongoose from 'mongoose'
import config from './index.js'

const CONNECTION_URL = `mongodb://${config.db.url}/${config.db.name}`

mongoose.connect(CONNECTION_URL, {
  useNewUrlParser: true,
  useUnifiedTopology: true
})

mongoose.connection.on('connected', () => {
  console.log('Mongo has connected succesfully')
})
mongoose.connection.on('reconnected', () => {
  console.log('Mongo has reconnected')
})
mongoose.connection.on('error', error => {
  console.log('Mongo connection has an error', error)
  mongoose.disconnect()
})
mongoose.connection.on('disconnected', () => {
  console.log('Mongo connection is disconnected')
})
```

Ensuite, importez `config/mongo.js` dans votre fichier `server/index.js` comme ceci :

```
.
.
// mongo connection
import "./config/mongo.js";
// routes
import indexRouter from "./routes/index.js";
```

Si vous vous perdez à un moment donné, l'intégralité du code source de ce tutoriel est disponible juste [**ici**][27]**.**

Voyons ce que nous faisons ici étape par étape :

Nous importons d'abord notre fichier `config.js` dans `config/mongo.js`. Ensuite, nous passons la valeur à notre `CONNECTION_URL` comme ceci :

```
const CONNECTION_URL = `mongodb://${config.db.url}/${config.db.name}`
```

Ensuite, en utilisant la `CONNECTION_URL`, nous formons une connexion Mongo, en faisant ceci :

```
mongoose.connect(CONNECTION_URL, {
  useNewUrlParser: true,
  useUnifiedTopology: true
})
```

Cela indique à `mongoose` d'établir une connexion avec la base de données avec notre application Node/Express.

Les options que nous donnons à Mongo ici sont :

-   `useNewUrlParser`: Le pilote MongoDB a déprécié son analyseur de [chaîne de connexion][28] actuel. `useNewUrlParser: true` indique à mongoose d'utiliser le nouvel analyseur de Mongo. (S'il est défini sur true, nous devons fournir un port de base de données dans la `CONNECTION_URL`.)
-   `useUnifiedTopology`: False par défaut. Défini sur `true` pour opter pour l'utilisation du [nouveau moteur de gestion de connexion du pilote MongoDB][29]. Vous devriez définir cette option sur `true`, sauf dans le cas peu probable où elle vous empêcherait de maintenir une connexion stable.

Ensuite, nous ajoutons simplement des gestionnaires d'événements `mongoose` comme ceci :

```
mongoose.connection.on('connected', () => {
  console.log('Mongo has connected succesfully')
})
mongoose.connection.on('reconnected', () => {
  console.log('Mongo has reconnected')
})
mongoose.connection.on('error', error => {
  console.log('Mongo connection has an error', error)
  mongoose.disconnect()
})
mongoose.connection.on('disconnected', () => {
  console.log('Mongo connection is disconnected')
})
```

-   `connected` sera appelé une fois la connexion à la base de données établie
-   `disconnected` sera appelé lorsque votre connexion Mongo est désactivée
-   `error` est appelé s'il y a une erreur de connexion à votre base de données Mongo
-   L'événement `reconnected` est appelé lorsque la base de données perd la connexion puis tente de se reconnecter avec succès.

Une fois cela en place, allez simplement dans votre fichier `server/index.js` et importez `config/mongo.js`. Et c'est tout. Maintenant, lorsque vous démarrez votre serveur en tapant ceci :

```
npm start;
```

Vous devriez voir quelque chose comme ceci :

![Screenshot-2020-06-15-at-19.42.53](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-15-at-19.42.53.png)

Logs au démarrage de votre serveur

Si vous voyez cela, vous avez ajouté avec succès Mongo à votre application.

Félicitations !

Si vous êtes resté bloqué ici pour une raison quelconque, faites-le-moi savoir sur [twitter.com/adeelibr][30] et j'essaierai de régler cela pour vous. :)

## Configuration de notre première section d'API pour users/

La configuration de notre API pour `users/` n'aura pas de token d'authentification pour ce tutoriel, car mon objectif principal est de vous enseigner l'application de chat ici.

### Schéma du modèle utilisateur

Créons notre premier modèle (schéma de base de données) pour la collection `user`.

Créez un nouveau dossier appelé `models`. À l'intérieur de ce dossier, créez un fichier appelé `User.js` et ajoutez le contenu suivant :

```
import mongoose from "mongoose";
import { v4 as uuidv4 } from "uuid";

export const USER_TYPES = {
  CONSUMER: "consumer",
  SUPPORT: "support",
};

const userSchema = new mongoose.Schema(
  {
    _id: {
      type: String,
      default: () => uuidv4().replace(/\-/g, ""),
    },
    firstName: String,
    lastName: String,
    type: String,
  },
  {
    timestamps: true,
    collection: "users",
  }
);

export default mongoose.model("User", userSchema);
```

Décomposons cela en morceaux :

```
export const USER_TYPES = {
  CONSUMER: "consumer",
  SUPPORT: "support",
};
```

Nous allons essentiellement avoir 2 types d'utilisateurs, `consumer` (consommateur) et `support`. Je l'ai écrit de cette façon parce que je veux assurer par programmation la validation de l'API et de la base de données, dont je parlerai plus tard.

Ensuite, nous créons un schéma sur la façon dont un seul `document` (objet/élément/entrée/ligne) se présentera à l'intérieur de notre collection `user` (une collection est l'équivalent d'une table MySQL). Nous le définissons comme ceci :

```
const userSchema = new mongoose.Schema(
  {
    _id: {
      type: String,
      default: () => uuidv4().replace(/\-/g, ""),
    },
    firstName: String,
    lastName: String,
    type: String,
  },
  {
    timestamps: true,
    collection: "users",
  }
);
```

Ici, nous indiquons à `mongoose` que pour un seul document dans notre collection `users`, nous voulons que la structure soit la suivante :

```
{
	id: String // obtiendra une chaîne aléatoire par défaut grâce à uuidv4
    	firstName: String,
    	lastName: String,
    	type: String // cela peut être de 2 types consumer/support
}
```

Dans la deuxième partie du schéma, nous avons quelque chose comme ceci :

```
{
    timestamps: true,
    collection: "users",
}
```

Définir `timestamps` sur `true` ajoutera 2 choses à mon schéma : une valeur de date `createdAt` et `updatedAt`. Chaque fois que nous créons une nouvelle entrée, `createdAt` sera mis à jour automatiquement et `updatedAt` sera mis à jour une fois que nous mettrons à jour une entrée dans la base de données à l'aide de mongoose. Ces deux opérations sont effectuées automatiquement par `mongoose`.

La deuxième partie est `collection`. Cela montre quel sera le nom de ma collection dans ma base de données. Je lui assigne le nom `users`.

Et enfin, nous exporterons l'objet comme ceci :

```
export default mongoose.model("User", userSchema);
```

Ainsi, `mongoose.model` prend 2 paramètres ici.

-   Le nom du modèle, qui est `User` ici
-   Le schéma associé à ce modèle, qui est `userSchema` dans ce cas

Note : Basé sur le nom du modèle, qui est `User` dans ce cas, nous n'ajoutons pas de clé `collection` dans la section schéma. Il prendra ce nom `User` et lui ajoutera un `s` pour créer une collection par son nom, qui devient `users`.

Génial, nous avons maintenant notre premier modèle.

Si vous êtes bloqué n'importe où, jetez un œil au [code source][31].

### Créer une API de nouvel utilisateur [Requête POST]

Ensuite, écrivons notre premier contrôleur pour cette route : `.post('/', user.onCreateUser)`.

Allez dans `controllers/user.js` et importez 2 choses en haut :

```
// utils
import makeValidation from '@withvoid/make-validation';
// models
import UserModel, { USER_TYPES } from '../models/User.js';
```

Ici, nous importons la bibliothèque de validation dont j'ai parlé dans la vidéo tout en haut. Nous importons également notre modèle utilisateur ainsi que les `USER_TYPES` du même fichier.

Voici ce que représente `USER_TYPES` :

```
export const USER_TYPES = {
  CONSUMER: "consumer",
  SUPPORT: "support",
};
```

Ensuite, trouvez le contrôleur `onCreateUser` et ajoutez-y le contenu suivant :

```
onCreateUser: async (req, res) => {
    try {
      const validation = makeValidation(types => ({
        payload: req.body,
        checks: {
          firstName: { type: types.string },
          lastName: { type: types.string },
          type: { type: types.enum, options: { enum: USER_TYPES } },
        }
      }));
      if (!validation.success) return res.status(400).json(validation);

      const { firstName, lastName, type } = req.body;
      const user = await UserModel.createUser(firstName, lastName, type);
      return res.status(200).json({ success: true, user });
    } catch (error) {
      return res.status(500).json({ success: false, error: error })
    }
  },
```

Divisons cela en 2 sections.

D'abord, nous validons la réponse de l'utilisateur en faisant ceci :

```
const validation = makeValidation(types => ({
  payload: req.body,
  checks: {
    firstName: { type: types.string },
    lastName: { type: types.string },
    type: { type: types.enum, options: { enum: USER_TYPES } },
  }
}));
if (!validation.success) return res.status(400).json({ ...validation });
```

Veuillez vous assurer d'avoir vu la vidéo (ci-dessus) sur `valider une requête API dans Node en utilisant une validation personnalisée ou en utilisant la bibliothèque make-validation`.

Ici, nous utilisons la bibliothèque `[make-validation][32]` (que j'ai fini par créer en écrivant ce tutoriel). Je parle de son utilisation dans la vidéo au début de ce tutoriel.

Tout ce que nous faisons ici est de passer `req.body` au `payload`. Ensuite, dans les vérifications, nous ajoutons un objet où, pour chaque `key`, nous indiquons quelles sont les exigences pour chaque type, par exemple :

```
firstName: { type: types.string },
```

Ici, nous lui indiquons que `firstName` est de type string. Si l'utilisateur oublie d'ajouter cette valeur lors de l'appel de l'API, ou si le type n'est pas string, une erreur sera générée.

La variable `validation` retournera un objet avec 3 choses : `{success: boolean, message: string, errors: object}`.

Si `validation.success` est false, nous retournons simplement tout ce qui provient de la validation et le donnons à l'utilisateur avec un code d'état `400`.

Une fois notre validation en place et que nous savons que les données que nous recevons sont valides, nous faisons ce qui suit :

```
const { firstName, lastName, type } = req.body;
const user = await UserModel.createUser(firstName, lastName, type);
return res.status(200).json({ success: true, user });
```

Ensuite, nous déstructurons `firstName, lastName, type` de `req.body` et passons ces valeurs à notre `UserModel.createUser`. Si tout se passe bien, il retourne simplement `success: true` avec le nouvel `user` créé ainsi qu'un statut `200`.

Si n'importe où dans ce processus quelque chose ne va pas, une erreur est générée et passe au bloc catch :

```
catch (error) {
  return res.status(500).json({ success: false, error: error })
}
```

Là, nous retournons simplement un message d'erreur avec le statut HTTP `500`.

La seule chose qui nous manque ici est la méthode `UserModel.createUser()`.

Retournons donc dans notre fichier `models/User.js` et ajoutons-la :

```
userSchema.statics.createUser = async function (
	firstName, 
    	lastName, 
    	type
) {
  try {
    const user = await this.create({ firstName, lastName, type });
    return user;
  } catch (error) {
    throw error;
  }
}


export default mongoose.model("User", userSchema);
```

Tout ce que nous faisons ici est d'ajouter une méthode statique à notre `userSchema` appelée `createUser` qui prend 3 paramètres : `firstName, lastName, type`.

Ensuite, nous utilisons ceci :

```
const user = await this.create({ firstName, lastName, type });
```

Ici, la partie `this` est très importante, car nous écrivons une méthode statique sur `userSchema`. L'écriture de `this` garantira que nous effectuons des opérations sur l'objet `userSchema`.

Une chose à noter ici est que `userSchema.statics.createUser = async (firstName, lastName, type) => {}` ne fonctionnera pas. Si vous utilisez une fonction fléchée `=>`, le contexte `this` sera perdu et cela ne fonctionnera pas.

Si vous souhaitez en savoir plus sur les méthodes `static` dans mongoose, consultez cet exemple de documentation très court mais utile [ici][33].

Maintenant que tout est configuré, démarrons notre terminal en exécutant la commande suivante dans le dossier racine du projet :

```
npm start;
```

Allez dans Postman, configurez une requête `POST` sur cette API `http://localhost:3000/users`, et ajoutez le corps suivant à l'API :

```
{
	"firstName": "John",
    	"lastName": "Doe",
    	"type": "consumer"
}
```

Comme ceci :

![Screenshot-2020-06-15-at-21.37.15](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-15-at-21.37.15.png)

Vous pouvez également obtenir la **collection API Postman complète** [**ici**][34] afin de ne pas avoir à réécrire les API encore et encore.

Génial – nous venons de créer notre première API. Créons quelques API utilisateur supplémentaires avant de passer à la partie chat, car il n'y a pas de chat sans utilisateurs (à moins d'avoir des robots, mais les robots sont aussi des utilisateurs, n'est-ce pas ?).

### Obtenir un utilisateur par son ID [Requête GET]

Ensuite, nous devons écrire une API qui nous permet d'obtenir un utilisateur par son ID. Donc pour notre route `.get('/:id', user.onGetUserById)`, écrivons son contrôleur.

Allez dans `controllers/user.js` et pour la méthode `onGetUserById`, écrivez ceci :

```
onGetUserById: async (req, res) => {
  try {
    const user = await UserModel.getUserById(req.params.id);
    return res.status(200).json({ success: true, user });
  } catch (error) {
    return res.status(500).json({ success: false, error: error })
  }
},
```

Cool, cela semble simple. Ajoutons `UserModel.getUserById()` dans notre fichier `models/User.js`.

Ajoutez cette méthode sous la dernière méthode `static` que vous avez écrite :

```
userSchema.statics.getUserById = async function (id) {
  try {
    const user = await this.findOne({ _id: id });
    if (!user) throw ({ error: 'No user with this id found' });
    return user;
  } catch (error) {
    throw error;
  }
}
```

Nous passons un paramètre `id` et nous enveloppons notre fonction dans un `try/catch`. C'est très important lorsque vous utilisez `async/await`. Les lignes sur lesquelles se concentrer ici sont ces 2 :

```
const user = await this.findOne({ _id: id });
if (!user) throw ({ error: 'No user with this id found' });
```

Nous utilisons la méthode `findOne` de `mongoose` pour trouver une entrée par `id`. Nous savons qu'un seul élément existe dans la collection avec cet `id` car l'ID est unique. Si aucun utilisateur n'est trouvé, nous lançons simplement une erreur avec le message `No user with this id found`.

Et c'est tout ! Démarrons notre serveur :

```
npm start;
```

Ouvrez Postman et créez une requête `GET` `http://localhost:3000/users/:id`.

Note : J'utilise l'ID du dernier utilisateur que nous venons de créer.

![Screenshot-2020-06-15-at-22.01.16](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-15-at-22.01.16.png)

Bien joué ! Bon travail.

Encore deux API à faire pour notre section utilisateur.

### Obtenir tous les utilisateurs [Requête GET]

Pour notre routeur dans `.get('/', user.onGetAllUsers)`, ajoutons les informations à son contrôleur.

Allez dans `controllers/user.js` et ajoutez le code dans la méthode `onGetAllUsers()` :

```
onGetAllUsers: async (req, res) => {
  try {
    const users = await UserModel.getUsers();
    return res.status(200).json({ success: true, users });
  } catch (error) {
    return res.status(500).json({ success: false, error: error })
  }
},
```

Ensuite, créons la méthode statique pour `getUsers()` dans le fichier `models/User.js`. Sous la dernière méthode statique que vous avez écrite dans ce fichier, tapez :

```
userSchema.statics.getUsers = async function () {
  try {
    const users = await this.find();
    return users;
  } catch (error) {
    throw error;
  }
}
```

Nous utilisons la méthode `mongoose` appelée `await this.find();` pour obtenir tous les enregistrements de notre collection `users` et les retourner.

Note : Je ne gère pas la pagination dans notre API utilisateurs car ce n'est pas l'objectif principal ici. Je parlerai de la pagination une fois que nous passerons à nos API de chat.

Démarrons notre serveur :

```
npm start;
```

Ouvrez Postman et créez une requête `GET` pour cette route `http://localhost:3000/users` :

![Screenshot-2020-06-15-at-22.12.13](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-15-at-22.12.13.png)

Je suis allé de l'avant et j'ai fini par créer quelques utilisateurs de plus. ?

### Supprimer un utilisateur par ID [Requête DELETE] (Section bonus)

Créons notre dernière route pour supprimer un utilisateur par son ID. Pour la route `.delete('/:id', user.onDeleteUserById)`, allez dans son contrôleur dans `controllers/user.js` et écrivez ce code dans la méthode `onDeleteUserById()` :

```
onDeleteUserById: async (req, res) => {
  try {
    const user = await UserModel.deleteByUserById(req.params.id);
    return res.status(200).json({ 
      success: true, 
      message: `Deleted a count of ${user.deletedCount} user.` 
    });
  } catch (error) {
    return res.status(500).json({ success: false, error: error })
  }
},
```

Ajoutons la méthode statique `deleteByUserById` dans `models/User.js` :

```
userSchema.statics.deleteByUserById = async function (id) {
  try {
    const result = await this.remove({ _id: id });
    return result;
  } catch (error) {
    throw error;
  }
}
```

Nous passons l'`id` ici en paramètre, puis nous utilisons la méthode `mongoose` appelée `this.remove` pour supprimer un enregistrement d'une collection spécifique. Dans ce cas, c'est la collection `users`.

Démarrons notre serveur :

```
npm start;
```

Allez sur Postman et créez une nouvelle route `DELETE` :

![Screenshot-2020-06-15-at-22.24.51](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-15-at-22.24.51.png)

Avec cela, nous conclurons notre section API UTILISATEURS.

Ensuite, nous verrons comment authentifier les routes avec un token d'authentification. C'est la dernière chose que je veux aborder avant de passer à la section chat – car toutes les API de chat seront authentifiées.

### Que sont les middlewares dans ExpressJS ?

Comment pouvons-nous les écrire ? En ajoutant un middleware JWT dans votre application :

<iframe width="480" height="270" src="https://www.youtube.com/embed/G8Z6yeV0ytc?feature=oembed" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" name="fitvid3"></iframe>

Et voici le [lien GitHub vers l'intégralité du code source de cette vidéo][35] \[Chapitre 0\].

Et encore une fois, toutes les informations pertinentes se trouvent dans le README.

Revenons à notre code, créons un middleware JWT pour authentifier nos routes. Allez dans `middlewares/jwt.js` et ajoutez ce qui suit :

```
import jwt from 'jsonwebtoken';
// models
import UserModel from '../models/User.js';

const SECRET_KEY = 'some-secret-key';

export const encode = async (req, res, next) => {
  try {
    const { userId } = req.params;
    const user = await UserModel.getUserById(userId);
    const payload = {
      userId: user._id,
      userType: user.type,
    };
    const authToken = jwt.sign(payload, SECRET_KEY);
    console.log('Auth', authToken);
    req.authToken = authToken;
    next();
  } catch (error) {
    return res.status(400).json({ success: false, message: error.error });
  }
}

export const decode = (req, res, next) => {
  if (!req.headers['authorization']) {
    return res.status(400).json({ success: false, message: 'No access token provided' });
  }
  const accessToken = req.headers.authorization.split(' ')[1];
  try {
    const decoded = jwt.verify(accessToken, SECRET_KEY);
    req.userId = decoded.userId;
    req.userType = decoded.type;
    return next();
  } catch (error) {

    return res.status(401).json({ success: false, message: error.message });
  }
}
```

Discutons d'abord de la méthode `encode` :

```
export const encode = async (req, res, next) => {
  try {
    const { userId } = req.params;
    const user = await UserModel.getUserById(userId);
    const payload = {
      userId: user._id,
      userType: user.type,
    };
    const authToken = jwt.sign(payload, SECRET_KEY);
    console.log('Auth', authToken);
    req.authToken = authToken;
    next();
  } catch (error) {
    return res.status(400).json({ 
    	success: false, message: error.error 
    });
  }
}
```

Passons-la en revue étape par étape.

Nous récupérons l'`userId` de nos `req.params`. Si vous vous souvenez de la vidéo précédente, `req.params` est l'identifiant `/:<identifier>` défini dans notre section routes.

Ensuite, nous utilisons la méthode `const user = await UserModel.getUserById(userId);` que nous venons de créer pour obtenir les informations de l'utilisateur. Si l'utilisateur existe – sinon cette ligne lancera une erreur et ira directement au bloc `catch` où nous retournerons une réponse `400` avec un message d'erreur.

Mais si nous recevons une réponse de la méthode `getUserById`, nous créons alors un payload :

```
const payload = {
      userId: user._id,
      userType: user.type,
};
```

Ensuite, nous signons ce payload en JWT en utilisant ce qui suit :

```
const authToken = jwt.sign(payload, SECRET_KEY);
```

Une fois que nous avons le JWT signé, nous faisons ceci :

```
req.authToken = authToken;
next();
```

Nous l'assignons à notre `req.authToken` puis nous transmettons cette information avec `next()`.

Ensuite, parlons de la méthode `decode` :

```
export const decode = (req, res, next) => {
  if (!req.headers['authorization']) {
    return res.status(400).json({ success: false, message: 'No access token provided' });
  }
  const accessToken = req.headers.authorization.split(' ')[1];
  try {
    const decoded = jwt.verify(accessToken, SECRET_KEY);
    req.userId = decoded.userId;
    req.userType = decoded.type;
    return next();
  } catch (error) {

    return res.status(401).json({ success: false, message: error.message });
  }
}
```

Décomposons cela :

```
if (!req.headers['authorization']) {
  return res.status(400).json({ 
  	success: false, 
    	message: 'No access token provided' 
  });
}
```

D'abord, nous vérifions si l'en-tête `authorization` est présent ou non. Sinon, nous retournons simplement un message d'erreur à l'utilisateur.

Ensuite, nous faisons ceci :

```
const accessToken = req.headers.authorization.split(' ')[1];
```

Il est divisé par `split(' ')` par espace, puis nous récupérons le deuxième index du tableau en accédant à son index `[1]` car la convention est `authorization: Bearer <auth-token>`. Vous voulez en savoir plus à ce sujet ? Consultez ce fil de discussion intéressant [sur Quora][36].

Ensuite, nous essayons de décoder notre token :

```
try {
  const decoded = jwt.verify(accessToken, SECRET_KEY);
  req.userId = decoded.userId;
  req.userType = decoded.type;
  return next();
} catch (error) {
  return res.status(401).json({ 
  	success: false, message: error.message 
  });
}
```

Si cela ne réussit pas, `jwt.verify(accessToken, SECRET_KEY)` lancera simplement une erreur et notre code ira immédiatement dans le bloc `catch`. Si cela réussit, nous pouvons alors le décoder. Nous récupérons l'`userId` et le `type` du token et les enregistrons dans `req.userId, req.userType` et appelons simplement `next()`.

Désormais, chaque route qui passe par ce middleware `decode` aura l'`id` et le `type` de l'utilisateur actuel.

C'était tout pour la section middleware. Créons une route `login` afin de pouvoir demander à un utilisateur ses informations et lui donner un token en retour (car à l'avenir, il aura besoin d'un token pour accéder au reste des API de chat).

### Création d'une route de connexion [Requête POST]

Allez dans votre fichier `routes/index.js` et collez le contenu suivant :

```
import express from 'express';
// middlewares
import { encode } from '../middlewares/jwt.js';

const router = express.Router();

router
  .post('/login/:userId', encode, (req, res, next) => {
    return res
      .status(200)
      .json({
        success: true,
        authorization: req.authToken,
      });
  });

export default router;
```

Tout ce que nous faisons est d'ajouter le middleware `encode` à notre route `http://localhost:3000/login/:<user-id>` \[POST\]. Si tout se passe bien, l'utilisateur recevra un token d'autorisation.

Note : Je n'ajoute pas de flux de connexion/inscription complet, mais je voulais quand même aborder JWT/middleware dans ce tutoriel.

Habituellement, l'authentification se fait de manière similaire. La seule différence ici est que l'utilisateur ne fournit pas son ID. Il fournit son nom d'utilisateur, son mot de passe (que nous vérifions dans la base de données), et si tout concorde, nous lui donnons un token d'autorisation.

Si vous êtes resté bloqué n'importe où jusqu'à présent, écrivez-moi sur [twitter.com/adeelibr][37], de cette façon je pourrai améliorer le contenu. Vous pouvez également m'écrire si vous souhaitez apprendre autre chose.

Pour rappel, l'intégralité du code source est disponible [ici][38]. Vous n'êtes pas obligé de coder en même temps que ce tutoriel, mais si vous le faites, les concepts s'ancreront mieux.

Vérifions maintenant notre route `/login`.

Démarrez votre serveur :

```
npm start;
```

Lançons Postman. Créez une nouvelle requête POST `http://localhost:3000/login/<user-id>` :

![Screenshot-2020-06-15-at-23.03.15](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-15-at-23.03.15.png)

Quand l'ID utilisateur est correct

![Screenshot-2020-06-15-at-23.03.32](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-15-at-23.03.32.png)

Quand l'ID utilisateur est invalide

Avec cela, nous en avons terminé avec notre flux de connexion également.

C'était beaucoup. Mais maintenant, nous pouvons nous concentrer uniquement sur nos routes de chat.

## Créer une classe web socket

Cette classe web socket gérera les événements lorsqu'un utilisateur se déconnecte, rejoint une salle de chat ou souhaite mettre une salle de chat en sourdine.

Créons donc une classe web-socket qui gérera les sockets pour nous. Créez un nouveau dossier appelé `utils`. À l'intérieur de ce dossier, créez un fichier appelé `WebSockets.js` et ajoutez le contenu suivant :

```
class WebSockets {
  users = [];
  connection(client) {
    // event fired when the chat room is disconnected
    client.on("disconnect", () => {
      this.users = this.users.filter((user) => user.socketId !== client.id);
    });
    // add identity of user mapped to the socket id
    client.on("identity", (userId) => {
      this.users.push({
        socketId: client.id,
        userId: userId,
      });
    });
    // subscribe person to chat & other user as well
    client.on("subscribe", (room, otherUserId = "") => {
      this.subscribeOtherUser(room, otherUserId);
      client.join(room);
    });
    // mute a chat room
    client.on("unsubscribe", (room) => {
      client.leave(room);
    });
  }

  subscribeOtherUser(room, otherUserId) {
    const userSockets = this.users.filter(
      (user) => user.userId === otherUserId
    );
    userSockets.map((userInfo) => {
      const socketConn = global.io.sockets.connected(userInfo.socketId);
      if (socketConn) {
        socketConn.join(room);
      }
    });
  }
}

export default new WebSockets();
```

La classe WebSockets contient trois éléments majeurs ici :

-   le tableau `users`
-   la méthode `connection`
-   l'abonnement des membres d'une salle de chat à celle-ci : `subscribeOtherUser`

Décomposons cela.

Nous avons une classe :

```
class WebSockets {

}

export default new WebSockets();
```

Nous créons une classe et exportons une instance de cette classe.

À l'intérieur de la classe, nous avons un tableau `users` vide. Ce tableau contiendra une liste de tous les utilisateurs actifs qui sont en ligne en utilisant notre application.

Ensuite, nous avons une méthode `connection`, le cœur de cette classe :

```
connection(client) {
  // event fired when the chat room is disconnected
  client.on("disconnect", () => {
    this.users = this.users.filter((user) => user.socketId !== client.id);
  });
  // add identity of user mapped to the socket id
  client.on("identity", (userId) => {
    this.users.push({
      socketId: client.id,
      userId: userId,
    });
  });
  // subscribe person to chat & other user as well
  client.on("subscribe", (room, otherUserId = "") => {
    this.subscribeOtherUser(room, otherUserId);
    client.join(room);
  });
  // mute a chat room
  client.on("unsubscribe", (room) => {
    client.leave(room);
  });
}
```

La méthode `connection` prend un paramètre appelé `client` (le client ici sera notre instance de serveur, j'en parlerai plus en détail dans un instant).

Nous prenons le paramètre `client` et lui ajoutons des événements :

-   `client.on('disconnect')` // lorsque la connexion d'un utilisateur est perdue, cette méthode sera appelée
-   `client.on('identity')` // lorsque l'utilisateur se connecte depuis le front-end, il établit une connexion avec notre serveur en donnant son identité
-   `client.on('subscribe')` // lorsqu'un utilisateur rejoint une salle de chat, cette méthode est appelée
-   `client.on('unsubscribe')` // lorsqu'un utilisateur quitte ou souhaite mettre une salle de chat en sourdine

Parlons de `disconnect` :

```
client.on("disconnect", () => {
  this.users = this.users.filter((user) => user.socketId !== client.id);
});
```

Dès que la connexion est déconnectée, nous exécutons un filtre sur le tableau `users`. Lorsque nous trouvons `user.id === client.id`, nous le supprimons de notre tableau de sockets. (`client` ici provient du paramètre de la fonction.)

Parlons d' `identity` :

```
client.on("identity", (userId) => {
  this.users.push({
    socketId: client.id,
    userId: userId,
  });
});
```

Lorsqu'un utilisateur se connecte via l'application front-end web/android/ios, il établit une connexion socket avec notre application back-end et appelle cette méthode d'identité. Il enverra également son propre ID utilisateur.

Nous prendrons cet ID utilisateur et l'ID client (l'ID de socket unique de l'utilisateur que socket.io crée lorsqu'il établit une connexion avec notre BE).

Ensuite, nous avons `unsubscribe` :

```
client.on("unsubscribe", (room) => {
  client.leave(room);
});
```

L'utilisateur transmet l'ID de la salle (`room`) et nous indiquons simplement à `client.leave()` de supprimer l'utilisateur actuel appelant cette méthode d'une salle de chat particulière.

Ensuite, nous avons `subscribe` :

```
client.on("subscribe", (room, otherUserId = "") => {
  this.subscribeOtherUser(room, otherUserId);
  client.join(room);
});
```

Lorsqu'un utilisateur rejoint une salle de chat, il nous indique la salle qu'il souhaite rejoindre ainsi que l'autre personne qui fait partie de cette salle de chat.

Note : Nous verrons plus tard que lorsque nous initions une salle de chat, nous obtenons tous les utilisateurs associés à cette salle dans la réponse de l'API.

**À mon avis** : Une autre chose que nous aurions pu faire ici, c'est lorsque l'utilisateur envoie le numéro de la salle, nous pouvons faire une requête en base de données pour voir tous les membres de la salle de chat et les faire rejoindre s'ils sont en ligne à ce moment-là (c'est-à-dire dans notre liste d'utilisateurs).

La méthode `subscribeOtherUser` est définie comme ceci :

```
subscribeOtherUser(room, otherUserId) {
  const userSockets = this.users.filter(
    (user) => user.userId === otherUserId
  );
  userSockets.map((userInfo) => {
    const socketConn = global.io.sockets.connected(userInfo.socketId);
    if (socketConn) {
      socketConn.join(room);
    }
  });
}
```

Nous passons `room` et `otherUserId` en paramètres à cette fonction.

En utilisant l'`otherUserId`, nous filtrons sur notre tableau `this.users` et tous les résultats correspondants sont stockés dans le tableau `userSockets`.

Vous vous demandez peut-être – comment un utilisateur peut-il avoir plusieurs présences dans le tableau des utilisateurs ? Eh bien, pensez à un scénario où le même utilisateur est connecté à la fois depuis son application web et son téléphone mobile. Cela créera plusieurs connexions socket pour le même utilisateur.

Ensuite, nous mappons sur `userSockets`. Pour chaque élément de ce tableau, nous le passons dans cette méthode : `const socketConn = global.io.sockets.connected(userInfo.socketId)`

Je parlerai plus en détail de ce `global.io.sockets.connected` dans un instant. Mais ce que cela fait initialement, c'est qu'il prend `userInfo.socketId` et s'il existe dans notre connexion socket, il retournera la connexion, sinon `null`.

Ensuite, nous vérifions simplement si `socketConn` est disponible. Si c'est le cas, nous prenons ce `socketConn` et faisons rejoindre cette connexion à la salle `room` passée dans la fonction :

```
if (socketConn) {
	socketConn.join(room);
}
```

Et c'est tout pour notre classe WebSockets.

Importons ce fichier dans notre fichier `server/index.js` :

```
import socketio from "socket.io";
// mongo connection
import "./config/mongo.js";
// socket configuration
import WebSockets from "./utils/WebSockets.js";
```

Importez donc `socket.io` et importez `WebSockets` quelque part en haut.

Ensuite, là où nous créons notre serveur, ajoutez le contenu en dessous :

```
/** Create HTTP server. */
const server = http.createServer(app);
/** Create socket connection */
global.io = socketio.listen(server);
global.io.on('connection', WebSockets.connection)
```

Le serveur a été créé et nous faisons deux choses :

-   assigner `global.io` à `socketio.listen(server)` (Dès qu'un port commence à écouter sur le serveur, les sockets commencent également à écouter les événements se produisant sur ce port.)
-   ensuite, nous assignons la méthode `global.io.on('connection', WebSockets.connection)`. Chaque fois que quelqu'un depuis le front-end établit une connexion socket, la méthode `connection` sera appelée, ce qui invoquera notre classe `WebSockets` et, à l'intérieur de cette classe, la méthode `connection`.

`global.io` est l'équivalent de l'objet `window` dans le navigateur. Mais comme nous n'avons pas `window` dans NodeJS, nous utilisons `global.io`. Tout ce que nous mettons dans `global.io` est disponible dans toute l'application.

C'est le même `global.io` que nous avons utilisé dans la classe `WebSockets` à l'intérieur de la méthode `subscribeOtherUser`.

Si vous vous êtes perdu, voici l'[intégralité du code source de cette application de chat][39]. N'hésitez pas non plus à m'envoyer un message avec vos commentaires et j'essaierai d'améliorer le contenu de ce tutoriel.

## Discussion sur le modèle de base de données des salles de chat et des messages

Avant de commencer avec le Chat, je pense qu'il est vraiment important de discuter du modèle de base de données sur lequel nous allons créer notre application de chat. Regardez la vidéo ci-dessous :

<iframe width="480" height="270" src="https://www.youtube.com/embed/GAt-XjGvMxM?feature=oembed" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" name="fitvid4"></iframe>

Maintenant que vous avez une idée claire de ce que sera notre structure de chat, commençons par créer notre modèle de salle de chat.

Allez dans votre dossier `models` et créez le fichier `ChatRoom.js` suivant. Ajoutez-y le contenu suivant :

```
import mongoose from "mongoose";
import { v4 as uuidv4 } from "uuid";

export const CHAT_ROOM_TYPES = {
  CONSUMER_TO_CONSUMER: "consumer-to-consumer",
  CONSUMER_TO_SUPPORT: "consumer-to-support",
};

const chatRoomSchema = new mongoose.Schema(
  {
    _id: {
      type: String,
      default: () => uuidv4().replace(/\-/g, ""),
    },
    userIds: Array,
    type: String,
    chatInitiator: String,
  },
  {
    timestamps: true,
    collection: "chatrooms",
  }
);

chatRoomSchema.statics.initiateChat = async function (
	userIds, type, chatInitiator
) {
  try {
    const availableRoom = await this.findOne({
      userIds: {
        $size: userIds.length,
        $all: [...userIds],
      },
      type,
    });
    if (availableRoom) {
      return {
        isNew: false,
        message: 'retrieving an old chat room',
        chatRoomId: availableRoom._doc._id,
        type: availableRoom._doc.type,
      };
    }

    const newRoom = await this.create({ userIds, type, chatInitiator });
    return {
      isNew: true,
      message: 'creating a new chatroom',
      chatRoomId: newRoom._doc._id,
      type: newRoom._doc.type,
    };
  } catch (error) {
    console.log('error on start chat method', error);
    throw error;
  }
}

export default mongoose.model("ChatRoom", chatRoomSchema);
```

Nous avons trois choses qui se passent ici :

-   Nous avons une constante pour `CHAT_ROOM_TYPES` qui n'a que deux types.
-   Nous définissons notre schéma ChatRoom.
-   Nous ajoutons une méthode statique pour initier le chat.

## API liées au chat

### Initier un chat entre utilisateurs (/room/initiate [Requête POST])

Discutons de notre méthode statique définie dans `models/ChatRoom.js` appelée `initiateChat` :

```
chatRoomSchema.statics.initiateChat = async function (userIds, type, chatInitiator) {
  try {
    const availableRoom = await this.findOne({
      userIds: {
        $size: userIds.length,
        $all: [...userIds],
      },
      type,
    });
    if (availableRoom) {
      return {
        isNew: false,
        message: 'retrieving an old chat room',
        chatRoomId: availableRoom._doc._id,
        type: availableRoom._doc.type,
      };
    }

    const newRoom = await this.create({ userIds, type, chatInitiator });
    return {
      isNew: true,
      message: 'creating a new chatroom',
      chatRoomId: newRoom._doc._id,
      type: newRoom._doc.type,
    };
  } catch (error) {
    console.log('error on start chat method', error);
    throw error;
  }
}
```

Cette fonction prend trois paramètres :

-   userIds (tableau d'utilisateurs)
-   type (type de salle de chat)
-   chatInitiator (l'utilisateur qui a créé la salle de chat)

Ensuite, nous faisons deux choses ici : soit retourner un document de salle de chat existant, soit en créer un nouveau.

Décomposons cela :

```
const availableRoom = await this.findOne({
  userIds: {
    $size: userIds.length,
    $all: [...userIds],
  },
  type,
});
if (availableRoom) {
  return {
    isNew: false,
    message: 'retrieving an old chat room',
    chatRoomId: availableRoom._doc._id,
    type: availableRoom._doc.type,
  };
}
```

D'abord, en utilisant l'API `this.findOne()` de mongoose, nous trouvons toutes les salles de chat où les critères suivants sont remplis :

```
userIds: { $size: userIds.length, $all: [...userIds] },
type: type,
```

Vous pouvez en savoir plus sur l'opérateur `$size` [ici][40], et plus sur l'opérateur `$all` [ici][41].

Nous vérifions pour trouver un document de salle de chat où un élément existe dans notre collection `chatrooms` où :

1.  les `userIds` sont les mêmes que ceux que nous passons à cette fonction (quel que soit l'ordre des IDs utilisateur), et
2.  la longueur de `userIds` est la même que celle de mon `userIds.length` que nous passons via la fonction.

De plus, nous vérifions que le type de salle de chat doit être le même.

Si quelque chose comme cela est trouvé, nous retournons simplement la salle de chat existante.

Sinon, nous créons une nouvelle salle de chat et la retournons en faisant ceci :

```
const newRoom = await this.create({ userIds, type, chatInitiator });
return {
  isNew: true,
  message: 'creating a new chatroom',
  chatRoomId: newRoom._doc._id,
  type: newRoom._doc.type,
};
```

Créer une nouvelle salle et retourner la réponse.

Nous avons également une clé `isNew` où, s'il s'agit de récupérer une ancienne salle de chat, nous la définissons sur `false`, sinon sur `true`.

Ensuite, pour votre route créée dans `routes/chatRoom.js` appelée `post('/initiate', chatRoom.initiate)`, allez dans son contrôleur approprié dans `controllers/chatRoom.js` et ajoutez ce qui suit dans la méthode `initiate` :

```
initiate: async (req, res) => {
  try {
    const validation = makeValidation(types => ({
      payload: req.body,
      checks: {
        userIds: { 
          type: types.array, 
          options: { unique: true, empty: false, stringOnly: true } 
        },
        type: { type: types.enum, options: { enum: CHAT_ROOM_TYPES } },
      }
    }));
    if (!validation.success) return res.status(400).json({ ...validation });

    const { userIds, type } = req.body;
    const { userId: chatInitiator } = req;
    const allUserIds = [...userIds, chatInitiator];
    const chatRoom = await ChatRoomModel.initiateChat(allUserIds, type, chatInitiator);
    return res.status(200).json({ success: true, chatRoom });
  } catch (error) {
    return res.status(500).json({ success: false, error: error })
  }
},
```

Nous utilisons la bibliothèque `[make-validation][42]` ici pour valider la requête de l'utilisateur. Pour l'API d'initiation, nous attendons de l'utilisateur qu'il envoie un tableau d' `users` et qu'il définisse également le type de la `chat-room` en cours de création.

Une fois la validation réussie, alors :

```
const { userIds, type } = req.body;
const { userId: chatInitiator } = req;
const allUserIds = [...userIds, chatInitiator];
const chatRoom = await ChatRoomModel.initiateChat(allUserIds, type, chatInitiator);
return res.status(200).json({ success: true, chatRoom });
```

Une chose à remarquer ici est que `userIds, type` proviennent de `req.body` tandis que `userId` qui est aliasé en `chatInitiatorId` provient de `req` grâce à notre middleware `decode`.

Si vous vous souvenez, nous avons attaché `app.use("/room", decode, chatRoomRouter);` dans notre fichier `server/index.js`. Cela signifie que cette route `/room/initiate` est authentifiée. Ainsi, `const { userId: chatInitiator } = req;` est l'ID de l'utilisateur actuellement connecté.

Nous appelons simplement notre méthode `initiateChat` de `ChatRoomModel` et lui passons `allUserIds, type, chatInitiator`. Quel que soit le résultat, nous le transmettons simplement à l'utilisateur.

Exécutons cela et voyons si cela fonctionne (voici une vidéo de moi le faisant) :

<iframe width="459" height="344" src="https://www.youtube.com/embed/vWzmTrNoNJs?feature=oembed" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" name="fitvid5"></iframe>

### Créer un message dans une salle de chat (/:roomId/message) [Requête POST]

Créons un message pour la salle de chat que nous venons de créer avec `pikachu`.

Mais avant de créer un message, nous devons créer un modèle pour nos `chatmessages`. Faisons cela d'abord. Dans votre dossier `models`, créez un nouveau fichier appelé `ChatMessage.js` et ajoutez-y le contenu suivant :

```
import mongoose from "mongoose";
import { v4 as uuidv4 } from "uuid";

const MESSAGE_TYPES = {
  TYPE_TEXT: "text",
};

const readByRecipientSchema = new mongoose.Schema(
  {
    _id: false,
    readByUserId: String,
    readAt: {
      type: Date,
      default: Date.now(),
    },
  },
  {
    timestamps: false,
  }
);

const chatMessageSchema = new mongoose.Schema(
  {
    _id: {
      type: String,
      default: () => uuidv4().replace(/\-/g, ""),
    },
    chatRoomId: String,
    message: mongoose.Schema.Types.Mixed,
    type: {
      type: String,
      default: () => MESSAGE_TYPES.TYPE_TEXT,
    },
    postedByUser: String,
    readByRecipients: [readByRecipientSchema],
  },
  {
    timestamps: true,
    collection: "chatmessages",
  }
);

chatMessageSchema.statics.createPostInChatRoom = async function (chatRoomId, message, postedByUser) {
  try {
    const post = await this.create({
      chatRoomId,
      message,
      postedByUser,
      readByRecipients: { readByUserId: postedByUser }
    });
    const aggregate = await this.aggregate([
      // get post where _id = post._id
      { $match: { _id: post._id } },
      // do a join on another table called users, and 
      // get me a user whose _id = postedByUser
      {
        $lookup: {
          from: 'users',
          localField: 'postedByUser',
          foreignField: '_id',
          as: 'postedByUser',
        }
      },
      { $unwind: '$postedByUser' },
      // do a join on another table called chatrooms, and 
      // get me a chatroom whose _id = chatRoomId
      {
        $lookup: {
          from: 'chatrooms',
          localField: 'chatRoomId',
          foreignField: '_id',
          as: 'chatRoomInfo',
        }
      },
      { $unwind: '$chatRoomInfo' },
      { $unwind: '$chatRoomInfo.userIds' },
      // do a join on another table called users, and 
      // get me a user whose _id = userIds
      {
        $lookup: {
          from: 'users',
          localField: 'chatRoomInfo.userIds',
          foreignField: '_id',
          as: 'chatRoomInfo.userProfile',
        }
      },
      { $unwind: '$chatRoomInfo.userProfile' },
      // group data
      {
        $group: {
          _id: '$chatRoomInfo._id',
          postId: { $last: '$_id' },
          chatRoomId: { $last: '$chatRoomInfo._id' },
          message: { $last: '$message' },
          type: { $last: '$type' },
          postedByUser: { $last: '$postedByUser' },
          readByRecipients: { $last: '$readByRecipients' },
          chatRoomInfo: { $addToSet: '$chatRoomInfo.userProfile' },
          createdAt: { $last: '$createdAt' },
          updatedAt: { $last: '$updatedAt' },
        }
      }
    ]);
    return aggregate[0];
  } catch (error) {
    throw error;
  }
}

export default mongoose.model("ChatMessage", chatMessageSchema);
```

Il y a plusieurs choses qui se passent ici :

-   Nous avons un objet `MESSAGE_TYPES` qui n'a qu'un seul type appelé `text`.
-   Nous définissons notre schéma pour `chatmessage` et `readByRecipient`.
-   Ensuite, nous écrivons notre méthode statique pour `createPostInChatRoom`.

Je sais que c'est beaucoup de contenu, mais restez avec moi. Écrivons simplement le contrôleur pour la route qui crée ce message.

Pour la route définie dans notre API `routes/chatRoom.js` appelée `.post('/:roomId/message', chatRoom.postMessage)`, allons dans son contrôleur dans `controllers/chatRoom.js` et définissons-le :

```
postMessage: async (req, res) => {
  try {
    const { roomId } = req.params;
    const validation = makeValidation(types => ({
      payload: req.body,
      checks: {
        messageText: { type: types.string },
      }
    }));
    if (!validation.success) return res.status(400).json({ ...validation });

    const messagePayload = {
      messageText: req.body.messageText,
    };
    const currentLoggedUser = req.userId;
    const post = await ChatMessageModel.createPostInChatRoom(roomId, messagePayload, currentLoggedUser);
    global.io.sockets.in(roomId).emit('new message', { message: post });
    return res.status(200).json({ success: true, post });
  } catch (error) {
    return res.status(500).json({ success: false, error: error })
  }
},
```

Cool, discutons de ce que nous faisons ici :

<iframe width="459" height="344" src="https://www.youtube.com/embed/z1C0Sl2wmJU?feature=oembed" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" name="fitvid6"></iframe>

Les opérateurs abordés dans cette vidéo sont :

-   [$match][43]
-   [$last][44]
-   [$addToSet][45]
-   [$lookup][46]
-   [$unwind][47]
-   [$group][48]

### Voir la conversation d'une salle de chat par son ID [Requête GET]

Maintenant que nous avons :

-   Créé une salle de chat
-   Sont capables d'ajouter des messages dans cette salle de chat

Voyons l'intégralité de la conversation pour ce chat (avec pagination).

Pour votre route `.get('/:roomId', chatRoom.getConversationByRoomId)` dans `routes/chatRoom.js`, ouvrez son contrôleur dans le fichier `controllers/chatRoom.js` et ajoutez le contenu suivant à la salle de chat :

```
getConversationByRoomId: async (req, res) => {
  try {
    const { roomId } = req.params;
    const room = await ChatRoomModel.getChatRoomByRoomId(roomId)
    if (!room) {
      return res.status(400).json({
        success: false,
        message: 'No room exists for this id',
      })
    }
    const users = await UserModel.getUserByIds(room.userIds);
    const options = {
      page: parseInt(req.query.page) || 0,
      limit: parseInt(req.query.limit) || 10,
    };
    const conversation = await ChatMessageModel.getConversationByRoomId(roomId, options);
    return res.status(200).json({
      success: true,
      conversation,
      users,
    });
  } catch (error) {
    return res.status(500).json({ success: false, error });
  }
},
```

Ensuite, créons une nouvelle méthode statique dans notre fichier `ChatRoomModel` appelée `getChatRoomByRoomId` dans `models/ChatRoom.js` :

```
chatRoomSchema.statics.getChatRoomByRoomId = async function (roomId) {
  try {
    const room = await this.findOne({ _id: roomId });
    return room;
  } catch (error) {
    throw error;
  }
}
```

Très simple – nous récupérons la salle par `roomId` ici.

Ensuite, dans notre `UserModel`, créez une méthode statique appelée `getUserByIds` dans le fichier `models/User.js` :

```
userSchema.statics.getUserByIds = async function (ids) {
  try {
    const users = await this.find({ _id: { $in: ids } });
    return users;
  } catch (error) {
    throw error;
  }
}
```

L'opérateur utilisé ici est [$in][49] – j'en parlerai dans un instant.

Et enfin, allez dans votre modèle `ChatMessage` dans `models/ChatMessage.js` et écrivez une nouvelle méthode statique appelée `getConversationByRoomId` :

```
chatMessageSchema.statics.getConversationByRoomId = async function (chatRoomId, options = {}) {
  try {
    return this.aggregate([
      { $match: { chatRoomId } },
      { $sort: { createdAt: -1 } },
      // do a join on another table called users, and 
      // get me a user whose _id = postedByUser
      {
        $lookup: {
          from: 'users',
          localField: 'postedByUser',
          foreignField: '_id',
          as: 'postedByUser',
        }
      },
      { $unwind: "$postedByUser" },
      // apply pagination
      { $skip: options.page * options.limit },
      { $limit: options.limit },
      { $sort: { createdAt: 1 } },
    ]);
  } catch (error) {
    throw error;
  }
}
```

Discutons de tout ce que nous avons fait jusqu'à présent :

<iframe width="459" height="344" src="https://www.youtube.com/embed/cnwOMrVMv0c?feature=oembed" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" name="fitvid7"></iframe>

**[Tout le code source est disponible ici][50].**

### Marquer une conversation entière comme lue (fonctionnalité similaire à WhatsApp)

Une fois que l'autre personne est connectée et qu'elle consulte une conversation pour un ID de salle, nous devons marquer cette conversation comme lue de son côté.

Pour ce faire, dans votre `routes/chatRoom.js` pour la route :

```
put('/:roomId/mark-read', chatRoom.markConversationReadByRoomId)
```

allez dans son contrôleur approprié dans `controllers/chatRoom.js` et ajoutez le contenu suivant dans le contrôleur `markConversationReadByRoomId`.

```
markConversationReadByRoomId: async (req, res) => {
  try {
    const { roomId } = req.params;
    const room = await ChatRoomModel.getChatRoomByRoomId(roomId)
    if (!room) {
      return res.status(400).json({
        success: false,
        message: 'No room exists for this id',
      })
    }

    const currentLoggedUser = req.userId;
    const result = await ChatMessageModel.markMessageRead(roomId, currentLoggedUser);
    return res.status(200).json({ success: true, data: result });
  } catch (error) {
    console.log(error);
    return res.status(500).json({ success: false, error });
  }
},
```

Tout ce que nous faisons ici est d'abord de vérifier si la salle existe ou non. Si c'est le cas, nous continuons. Nous prenons `req.userId` comme `currentLoggedUser` et le passons à la fonction suivante :

```
ChatMessageModel.markMessageRead(roomId, currentLoggedUser);
```

Qui, dans notre modèle `ChatMessage`, est définie comme ceci :

```
chatMessageSchema.statics.markMessageRead = async function (chatRoomId, currentUserOnlineId) {
  try {
    return this.updateMany(
      {
        chatRoomId,
        'readByRecipients.readByUserId': { $ne: currentUserOnlineId }
      },
      {
        $addToSet: {
          readByRecipients: { readByUserId: currentUserOnlineId }
        }
      },
      {
        multi: true
      }
    );
  } catch (error) {
    throw error;
  }
}
```

Un cas d'utilisation possible est que l'utilisateur n'ait pas lu les 15 derniers messages lorsqu'il ouvre la conversation d'une salle spécifique. Ils devraient tous être marqués comme lus. Nous utilisons donc la fonction `this.updateMany` de mongoose.

La requête elle-même est définie en 2 étapes :

-   Trouver
-   Mettre à jour

Et plusieurs instructions peuvent être mises à jour.

Pour la section de recherche, faites ceci :

```
{
  chatRoomId,
  'readByRecipients.readByUserId': { $ne: currentUserOnlineId }
},
```

Cela signifie que je veux trouver tous les messages dans la collection `chatmessages` où le `chatRoomId` correspond et où le tableau `readByRecipients` ne contient pas l'`userId` que je passe à cette fonction (`currentUserOnlineId`).

Une fois qu'il a tous les documents où les critères correspondent, il est alors temps de les mettre à jour :

```
{
  $addToSet: {
    readByRecipients: { readByUserId: currentUserOnlineId }
  }
},
```

`$addToSet` ajoutera simplement une nouvelle entrée au tableau `readByRecipients`. C'est comme `Array.push` mais pour Mongo.

Ensuite, nous voulons indiquer à `mongoose` de ne pas seulement mettre à jour le premier enregistrement qu'il trouve, mais de mettre à jour tous les enregistrements où la condition correspond. En faisant ceci :

```
{
  multi: true
}
```

Et c'est tout – nous retournons les données telles quelles.

Exécutons cette API.

Démarrez le serveur :

```
npm start;
```

Ouvrez votre Postman et créez une nouvelle requête `PUT` pour tester cette route `localhost:3000/room/<room-id-here>/mark-read` :

![Screenshot-2020-06-16-at-23.20.53](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-16-at-23.20.53.png)

### Section Bonus

-   Comment supprimer une salle de chat et tous ses messages associés
-   Comment supprimer un message par son ID de message

<iframe width="459" height="344" src="https://www.youtube.com/embed/GHhOIg5ZDa4?feature=oembed" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" name="fitvid8"></iframe>

Et nous avons terminé ! Waouh, c'était beaucoup d'apprentissage aujourd'hui.

Vous pouvez trouver le code source de ce tutoriel [ici][51].

Contactez-moi sur Twitter avec vos commentaires – j'aimerais savoir si vous avez des suggestions d'amélioration : [twitter.com/adeelibr][52]

Si vous avez aimé cet article, n'hésitez pas à donner une étoile au [répertoire GitHub][53] et à vous abonner à ma [chaîne YouTube][54].

[1]: https://nodejs.org/
[2]: http://expressjs.com/
[3]: https://www.mongodb.com/
[4]: https://github.com/adeelibr/node-playground/blob/master/chapter-1-chat/guidelines/installing-mongo.md
[5]: https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/#procedure
[6]: https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/#install-homebrew
[7]: https://github.com/adeelibr/node-playground/blob/master/chapter-1-chat/guidelines/installing-mongo.md
[8]: https://docs.mongodb.com/manual/administration/install-on-linux/
[9]: https://nodejs.org/en/download/
[10]: https://github.com/adeelibr/node-playground/tree/master/chapter-0-basic
[11]: https://github.com/adeelibr/node-playground/tree/master/chapter-0-basic
[12]: https://github.com/withvoid/make-validation
[13]: https://www.npmjs.com/package/@withvoid/make-validation
[14]: https://github.com/withvoid/make-validation/tree/master/example
[15]: https://github.com/adeelibr/node-playground/tree/master/chapter-1-chat
[16]: http://twitter.com/adeelibr
[17]: https://github.com/adeelibr/node-playground
[18]: https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/#procedure
[19]: https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/#install-homebrew
[20]: https://github.com/adeelibr/node-playground/blob/master/chapter-1-chat/guidelines/installing-mongo.md
[21]: https://docs.mongodb.com/manual/administration/install-on-linux/
[22]: https://twitter.com/adeelibr
[23]: https://robomongo.org/
[24]: https://robomongo.org/
[25]: https://robomongo.org/
[26]: https://robomongo.org/
[27]: https://github.com/adeelibr/node-playground/tree/master/chapter-1-chat
[28]: https://docs.mongodb.com/manual/reference/connection-string/
[29]: https://mongoosejs.com/docs/deprecations.html#useunifiedtopology
[30]: https://twitter.com/adeelibr
[31]: https://github.com/adeelibr/node-playground/tree/master/chapter-1-chat
[32]: https://www.npmjs.com/package/@withvoid/make-validation
[33]: https://mongoosejs.com/docs/2.7.x/docs/methods-statics.html
[34]: https://www.getpostman.com/collections/c28b12148c3d980fc39d
[35]: https://github.com/adeelibr/node-playground/tree/master/chapter-0-basic
[36]: https://www.quora.com/Why-is-Bearer-required-before-the-token-in-Authorization-header-in-a-HTTP-request
[37]: https://twitter.com/adeelibr
[38]: https://github.com/adeelibr/node-playground/tree/master/chapter-1-chat
[39]: https://github.com/adeelibr/node-playground/tree/master/chapter-1-chat
[40]: https://docs.mongodb.com/manual/reference/operator/query/size/
[41]: https://docs.mongodb.com/manual/reference/operator/query/all/
[42]: https://www.npmjs.com/package/@withvoid/make-validation
[43]: https://docs.mongodb.com/manual/reference/operator/aggregation/match/
[44]: https://docs.mongodb.com/manual/reference/operator/aggregation/last/
[45]: https://docs.mongodb.com/manual/reference/operator/update/addToSet/
[46]: https://docs.mongodb.com/manual/reference/operator/aggregation/lookup/
[47]: https://docs.mongodb.com/manual/reference/operator/aggregation/unwind/
[48]: https://docs.mongodb.com/manual/reference/operator/aggregation/group/
[49]: https://docs.mongodb.com/manual/reference/operator/query/in/
[50]: https://github.com/adeelibr/node-playground/tree/master/chapter-1-chat
[51]: https://github.com/adeelibr/node-playground/tree/master/chapter-1-chat
[52]: https://twitter.com/adeelibr
[53]: https://github.com/adeelibr/node-playground/tree/master/chapter-1-chat
[54]: https://www.youtube.com/channel/UCGHFI8lm4QzUzFH5nnzqkjA