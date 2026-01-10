---
title: Comment sécuriser votre application MERN Stack avec l'authentification et l'autorisation
  des utilisateurs basée sur JWT
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-05-15T17:15:14.000Z'
originalURL: https://freecodecamp.org/news/how-to-secure-your-mern-stack-application
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/trlyJUK.jpg
tags:
- name: authentication
  slug: authentication
- name: authorization
  slug: authorization
- name: Express JS
  slug: express-js
- name: MongoDB
  slug: mongodb
- name: node js
  slug: node-js
- name: React
  slug: reactjs
seo_title: Comment sécuriser votre application MERN Stack avec l'authentification
  et l'autorisation des utilisateurs basée sur JWT
seo_desc: 'By FADAHUNSI SEYI SAMUEL

  MongoDB, Express, React, and Node.js are the components of the MERN stack, one of
  the most widely used web development stacks out there today.

  The MERN stack enables programmers to create dependable web applications with stro...'
---

Par FADAHUNSI SEYI SAMUEL

[MongoDB](https://www.mongodb.com/docs/), [Express](https://expressjs.com/en/starter/installing.html), [React](https://react.dev/learn), et [Node.js](https://nodejs.org/en/docs) sont les composants de la stack MERN, l'une des stacks de développement web les plus utilisées aujourd'hui.

La stack MERN permet aux programmeurs de créer des applications web fiables avec des capacités solides. Pourtant, la sécurité devrait être une préoccupation clé avec toute application web.

L'authentification et les permissions des utilisateurs sont certaines des fonctionnalités de sécurité les plus importantes de tout service web. Afin de protéger les informations sensibles et d'empêcher l'accès non autorisé aux fonctions importantes, celles-ci garantissent que seuls les utilisateurs autorisés peuvent accéder à certaines zones de l'application.

À la fin de cet article, vous aurez une solide compréhension de la manière d'intégrer l'authentification et l'autorisation des utilisateurs basée sur [JWT](https://jwt.io/introduction) (Json Web Token) dans votre application web de la stack MERN.

### Voici ce que nous allons couvrir :

* [Qu'est-ce que l'authentification et l'autorisation des utilisateurs ?](#heading-questce-que-lauthentification-et-lautorisation-des-utilisateurs)
* [Qu'est-ce que la stack MERN ?](#heading-questce-que-la-stack-mern)
* [Pourquoi utiliser la stack MERN ?](#heading-pourquoi-utiliser-la-stack-mern)
* [Comment configurer l'environnement du projet](#heading-comment-configurer-environnement-du-projet)
* [Comment créer une nouvelle application React](#heading-comment-creer-une-nouvelle-application-react)
* [Installation et configuration de Node.js et Express.js](#heading-installation-et-configuration-de-nodejs-et-expressjs)
* [Comment configurer MongoDB](#heading-comment-configurer-mongodb)
* [Comment implémenter le backend](#heading-comment-implementer-le-backend)
* [Comment gérer la route SIGNUP](#heading-comment-gerer-la-route-signup)
* [Comment gérer la route LOGIN](#heading-comment-gerer-la-route-login)
* [Comment gérer la route HOME](#heading-comment-gerer-la-route-home)
* [Comment implémenter le frontend](https://www.freecodecamp.org/news/p/43c39ded-b2ce-4029-8fbe-66015525449f/howtoimplementthefrontend)
* [Comment gérer la logique de Signup](#heading-comment-gerer-la-logique-de-signup)
* [Comment gérer la logique de Login](#heading-comment-gerer-la-logique-de-login)
* [Comment gérer la logique de la page Home](#heading-comment-gerer-la-logique-de-la-page-home)
* [Conclusion](#heading-conclusion)

## Qu'est-ce que l'authentification et l'autorisation des utilisateurs ?

En matière de sécurité des applications, l'authentification et l'autorisation sont deux concepts cruciaux qui fonctionnent ensemble pour garantir l'accès aux ressources d'une application.

Beaucoup de gens confondent souvent ces termes – mais après avoir lu ce guide, nous ne le ferons plus, N'EST-CE PAS !

### Authentification
La vérification de l'identité d'un utilisateur ou d'une entité est le processus appelé **Authentification**. Cela implique de valider les informations d'identification de l'utilisateur, telles qu'un nom d'utilisateur et un mot de passe, pour s'assurer que l'utilisateur est bien celui qu'il prétend être.

### Autorisation

Le processus d'autorisation ou de refus d'accès à des ressources ou fonctions particulières au sein d'une application est appelé **Autorisation**. Une fois qu'un utilisateur a été vérifié comme authentique, le programme vérifie son niveau d'autorisation pour décider à quelles zones de l'application il peut accéder.

**L'authentification** est comparable à lorsqu'un candidat à l'université est admis dans un programme sur la base des résultats d'un examen écrit. L'étudiant est autorisé sur le campus de l'école, mais n'est pas autorisé dans un département ou une classe qui n'est pas le sien (qui ne lui a pas été donné lors de l'admission). Cette action est appelée **Autorisation**.

## Qu'est-ce que la stack MERN ?

Parlons des différents éléments de la stack MERN avant de commencer à créer le mécanisme d'authentification.

1. **MongoDB** est une base de données NoSQL qui utilise des schémas dynamiques et des documents ressemblant à JSON pour stocker des données. MongoDB est une option populaire pour créer des applications web scalables car elle est efficace pour gérer de grandes quantités de données.
2. **Express.js** est un framework d'application web Node.js qui offre une sélection de fonctionnalités pour créer des applications en ligne. Express.js est une option populaire pour développer des applications en ligne car il est compact, rapide et simple à utiliser.
3. **React.js** est une bibliothèque JavaScript utilisée pour créer des interfaces utilisateur. En décomposant des interfaces utilisateur complexes en composants plus petits et réutilisables, React.js offre une méthode déclarative pour le faire.
4. **Node.js** est basé sur le moteur JavaScript V8 dans Chrome, et est un environnement d'exécution JavaScript. La capacité à exécuter JavaScript côté serveur fait de Node.js la plateforme parfaite pour créer des applications web.

## Pourquoi utiliser la stack MERN ?

La stack MERN est une excellente option pour développer des applications web car elle inclut toutes les technologies nécessaires pour créer une application en ligne moderne et scalable.

Après avoir discuté des différents éléments de la stack MERN, nous allons utiliser des extraits de code pour développer un système complet d'authentification utilisateur à partir de zéro.


## Comment configurer l'environnement du projet

Pour commencer à construire le système d'authentification, nous devons d'abord configurer le projet. Nous allons créer une nouvelle application React en utilisant `create-react-app` et installer les dépendances requises. Nous allons également configurer `MongoDB` et configurer notre serveur `Node.js`.

NB : Dans cet article, nous allons utiliser l'éditeur [Visual Studio Code](https://code.visualstudio.com/download), que je recommande vivement.

Avant de plonger dans cela, vous allez créer un dossier qui contiendra d'autres sous-dossiers au fur et à mesure que vous avancez dans cet article.

Après avoir créé votre dossier, il devrait ressembler à l'image ci-dessous :

![Structure du dossier](https://i.imgur.com/JrxZbI3.png)

Le dossier que vous venez de créer contiendra deux sous-dossiers appelés `client` et `server`. Exécutez les commandes ci-dessous dans votre terminal pour créer les sous-dossiers :

```
mkdir client
```

Cela créera le sous-dossier `client`.

```
mkdir server
```

Cela créera le sous-dossier `server`. Votre dossier d'application devrait ressembler à ceci :

![Dossier de l'application](https://i.imgur.com/jwPj09J.png)

### Comment créer une nouvelle application React

Vous pouvez créer une nouvelle application React en utilisant `create-react-app`. Ouvrez votre terminal et exécutez la commande ci-dessous pour créer une nouvelle application React.

Mais d'abord, vous devrez vous rendre dans le dossier `client` en utilisant `cd client`, puis exécuter la commande suivante :

```shell
npx create-react-app
```

Après que la commande ci-dessus a créé avec succès l'application, tapez `npm start` dans votre terminal. Assurez-vous d'être dans votre répertoire `client`. Votre sortie devrait ressembler à l'image ci-dessous :

![](https://i.imgur.com/Y8N9gbL.png)

Avant de passer au répertoire du serveur, vous devrez supprimer certains éléments de base dans votre application React. Votre `client` devrait ressembler à l'image ci-dessous ;

![](https://i.imgur.com/27WytE6.png)

Une fois que vous avez terminé ce qui précède, redémarrez votre application React en exécutant `npm start` dans votre terminal. Votre application devrait ressembler à ceci :

![](https://i.imgur.com/ws2F4wH.png)

Maintenant, vous avez réussi à configurer le côté client de votre application 😊 yeah !

### Installation et configuration de Node.js et Express.js

Pour configurer votre application backend, exécutez `mkdir server` dans votre terminal pour accéder au sous-dossier `server`. Après être entré dans le sous-dossier `server`, exécutez la commande suivante pour initialiser l'application backend :

```shell
npm init --yes

```

La commande `npm init --yes` dans Node.js crée un nouveau fichier `package.json` pour un projet avec des paramètres par défaut, sans poser de questions à l'utilisateur.

Le flag `--yes` ou `-y` indique à npm d'utiliser des valeurs par défaut pour toutes les invites qui apparaîtraient normalement pendant le processus d'initialisation.

Le dossier serveur devrait maintenant contenir un fichier `package.json` comme suit :

```javascript
{
  "name": "server",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC"
}


```

Pour installer Express.js et d'autres dépendances, exécutez les commandes suivantes dans votre terminal :

```shell
 npm install express cors bcrypt cookie-parser nodemon jsonwebtoken mongoose dotenv


```

Les commandes ci-dessus installent les dépendances suivantes :

* `Express.js`, qui est notre framework d'application web Node.js.
* `bcrypt`, qui nous aide à hacher le mot de passe de l'utilisateur.
* `cookie-parser` est le middleware cookie-parser qui gère les sessions basées sur les cookies. Il extrait les informations des cookies qui peuvent être requises pour l'authentification ou d'autres fins.
* `nodemon` est un outil utilisé pour redémarrer automatiquement une application Node.js chaque fois que des modifications sont apportées au code.
* `CORS` est un middleware utilisé pour activer le partage des ressources entre origines (CORS) pour une application Express.js.
* `jsonwebtoken` nous aide à créer et vérifier les JSON Web Tokens.
* `dotenv` vous permet de stocker les données de configuration dans un fichier `.env`, qui n'est généralement pas validé dans le contrôle de version, pour séparer les informations sensibles de votre base de code. Ce fichier contient des paires clé-valeur qui représentent les variables d'environnement.

Après avoir installé les dépendances requises, créez un nouveau fichier appelé `index.js` dans le répertoire racine de votre sous-dossier `server` de votre application. Le fichier `index.js` contiendra notre serveur Node.js.

Dans le fichier `index.js` de votre `server`, ajoutez le code suivant :

```javascript
const express = require("express");

const app = express();
const PORT = 4000;

app.listen(PORT, () => {
  console.log(`Server is listening on port ${PORT}`);
});

```

Avant de démarrer le serveur, mettez à jour votre fichier `package.json` dans le serveur en ajoutant le code ci-dessous :

```javascript
  "scripts":{
  start: "nodemon index.js",
  test: 'echo "Error: no test specified" && exit 1',
};


```

Cela garantira que votre application redémarre à chaque mise à jour. Maintenant, vous pouvez démarrer votre `server` en exécutant `npm start` dans votre terminal.

Si tout cela est exécuté avec succès, votre terminal devrait ressembler à ceci :

![Image](https://i.imgur.com/EsjRkqi.png)

### Comment configurer MongoDB

Vous avez presque terminé la configuration de votre application. Si vous n'avez pas installé `mongodb` sur votre ordinateur, suivez ces [étapes](https://www.mongodb.com/docs/manual/installation/).

Maintenant, je suppose que vous avez installé `mongodb` avec succès sur votre ordinateur. Pour lier votre base de données à votre backend, suivez les procédures ci-dessous.

ÉTAPE 1 : Allez dans vos clusters cloud MongoDB, qui devraient ressembler à l'image ci-dessous :

![](https://i.imgur.com/MZbppS2.png)

ÉTAPE 2 : Cliquez sur Database Access, qui se trouve à gauche de la barre latérale. Cliquez sur `ADD NEW DATABASE USER` qui fera apparaître une modale, comme l'image ci-dessous :

![](https://i.imgur.com/Hyiky7V.png)

ÉTAPE 3 : Remplissez le champ `Password Authentication` avec votre nom d'utilisateur et mot de passe souhaités pour la base de données de ce projet particulier.

ÉTAPE 4 : Avant de sauvegarder cela, cliquez sur le menu déroulant `Built-in Role`, et sélectionnez `Read and write to any database`. Maintenant, allez-y et cliquez sur `Add user`.

ÉTAPE 5 : Cliquez sur `Database`, et sur le côté gauche de la barre latérale, cliquez sur le bouton `connect`, qui se trouve à côté de `View Monitoring`. Une fenêtre modale s'affichera, puis cliquez sur `connect your application` et copiez l'extrait de code que vous trouvez là.

![](https://i.imgur.com/Hqmbxro.png)

Vous remplacerez `<username>` et `<password>` par le nom d'utilisateur et le mot de passe que vous avez créés dans `ÉTAPE 3` dans votre fichier `index.js` dans le dossier serveur.

Avant d'aller dans votre fichier `index.js`, vous allez créer un fichier `.env` dans votre répertoire `server`, qui contiendra votre `MONGODB_URL`, `PORT`, `database_name`, et `database_password` comme le code ci-dessous :

```javascript
MONGO_URL =
  "mongodb+srv://database_name:database_password@cluster0.fbx6x.mongodb.net/?retryWrites=true&w=majority";
PORT = 4000;
```

Une fois que vous avez terminé cela, allez dans votre `index.js` dans votre répertoire `server`, et mettez-le à jour avec le code ci-dessous :

```javascript
const express = require("express");
const mongoose = require("mongoose");
const cors = require("cors");
const app = express();
require("dotenv").config();
const { MONGO_URL, PORT } = process.env;

mongoose
  .connect(MONGO_URL, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  })
  .then(() => console.log("MongoDB is  connected successfully"))
  .catch((err) => console.error(err));

app.listen(PORT, () => {
  console.log(`Server is listening on port ${PORT}`);
});

app.use(
  cors({
    origin: ["http://localhost:4000"],
    methods: ["GET", "POST", "PUT", "DELETE"],
    credentials: true,
  })
);

app.use(express.json());
```

Dans le code ci-dessus, nous configurons notre application pour qu'elle puisse avoir accès au fichier `.env`. Vous pouvez obtenir les informations dans votre fichier `.env` en faisant `process.env`.

Ainsi, vous déstructurez les valeurs du fichier `.env` en faisant `process.env` afin de ne pas vous répéter (DRY), ce qui est une bonne pratique d'ingénierie.

* CORS (Cross origin resource sharing) : Vous pouvez autoriser les requêtes d'autres domaines à accéder aux ressources de votre serveur en utilisant la fonction middleware `cors()` express. Les en-têtes CORS que votre serveur doit inclure dans la réponse peuvent être spécifiés en utilisant le paramètre de configuration objet optionnel de la fonction, qui est pris comme paramètre par la fonction qui est l'`origin`, les `methods` et les `credentials`.
* express.json() : Le `express.json()` ajoutera une propriété `body` à l'objet `request` ou `req`. Cela inclut les données JSON analysées du corps de la requête. `req.body` dans votre fonction de gestionnaire de route vous permettra d'accéder à ces données.
* useNewUrlParser : Cette propriété spécifie que Mongoose doit utiliser le nouvel analyseur d'URL pour analyser les chaînes de connexion MongoDB. Cela est défini sur true par défaut.
* useUnifiedTopology : Cette propriété spécifie que Mongoose doit utiliser le nouveau moteur de découverte et de surveillance de serveur. Cela est défini sur false par défaut.

Après avoir suivi les étapes ci-dessus, vous redémarrerez votre application en faisant `npm start` dans votre répertoire `server`. Votre terminal devrait ressembler à l'image ci-dessous ;

![](https://i.imgur.com/Ly8zIk5.png)


## Comment implémenter le Backend

Créez les dossiers suivants dans le répertoire `server` de votre application après vous être assuré d'être dans ce répertoire. `Controllers`, `Middlewares`, `Routes`, `Models`, et `util` sont les noms de ces dossiers.

### Comment gérer la route SIGNUP

Créez un fichier appelé `UserModel.js` dans le répertoire `Models` et mettez le code suivant dedans pour commencer :

```javascript
const mongoose = require("mongoose");
const bcrypt = require("bcryptjs");

const userSchema = new mongoose.Schema({
  email: {
    type: String,
    required: [true, "Your email address is required"],
    unique: true,
  },
  username: {
    type: String,
    required: [true, "Your username is required"],
  },
  password: {
    type: String,
    required: [true, "Your password is required"],
  },
  createdAt: {
    type: Date,
    default: new Date(),
  },
});

userSchema.pre("save", async function () {
  this.password = await bcrypt.hash(this.password, 12);
});

module.exports = mongoose.model("User", userSchema);
```

Le schéma utilisateur et le mot de passe de l'utilisateur seront créés dans le code ci-dessus en utilisant `mongoose` et `bcryptjs`, respectivement, à des fins de sécurité.

Le `password` est haché pour des raisons de sécurité avant de sauvegarder l'utilisateur.

Ensuite, vous allez configurer une fonction pour gérer la génération d'un token, qui sera appelée `SecretToken.js` dans le dossier `util`. Copiez et collez le code ci-dessous dans le fichier nouvellement créé (`SecretToken.js`) :

```javascript
require("dotenv").config();
const jwt = require("jsonwebtoken");

module.exports.createSecretToken = (id) => {
  return jwt.sign({ id }, process.env.TOKEN_KEY, {
    expiresIn: 3 * 24 * 60 * 60,
  });
};
```

Une fois cela fait, créez un fichier appelé `AuthController.js` dans le répertoire `Controllers` et collez le code suivant :

```javascript
const User = require("../Models/UserModel");
const { createSecretToken } = require("../util/SecretToken");
const bcrypt = require("bcryptjs");

module.exports.Signup = async (req, res, next) => {
  try {
    const { email, password, username, createdAt } = req.body;
    const existingUser = await User.findOne({ email });
    if (existingUser) {
      return res.json({ message: "User already exists" });
    }
    const user = await User.create({ email, password, username, createdAt });
    const token = createSecretToken(user._id);
    res.cookie("token", token, {
      withCredentials: true,
      httpOnly: false,
    });
    res
      .status(201)
      .json({ message: "User signed in successfully", success: true, user });
    next();
  } catch (error) {
    console.error(error);
  }
};
```

Les entrées de l'utilisateur sont obtenues à partir de `req.body` dans le code ci-dessus, et vous vérifiez ensuite l'`email` pour vous assurer qu'aucune inscription précédente n'a été faite. Nous utiliserons les valeurs obtenues à partir de `req.body` pour créer le nouvel `user` après que cela se soit produit.

Vous n'avez pas besoin de vous soucier de la manière dont l'`_id` unique a été obtenu car MongoDB attribue toujours un nouvel utilisateur avec un `_id` unique.

L'`_id` du nouvel `user` formé est ensuite fourni comme paramètre à la fonction `createSecretToken()`, qui gère la génération de token.

Le `cookie` sera envoyé au client avec la clé `"token"`, et la valeur `token`.

Ensuite, créez un fichier appelé `AuthRoute.js` dans le répertoire `Routes`. Collez le code ci-dessous dans le fichier nouvellement créé :

```javascript
const { Signup } = require("../Controllers/AuthController");
const router = require("express").Router();

router.post("/signup", Signup);

module.exports = router;
```

Dans le code ci-dessus, la route `/signup` a une méthode `post` attachée, lorsqu'elle est appelée, le contrôleur `Signup` sera exécuté.

Ensuite, mettez à jour votre fichier `index.js` afin qu'il puisse être conscient des routes. Votre fichier `index.js` devrait ressembler au code ci-dessous :

```javascript
const express = require("express");
const mongoose = require("mongoose");
const cors = require("cors");
const app = express();
require("dotenv").config();
const cookieParser = require("cookie-parser");
const authRoute = require("./Routes/AuthRoute");
const { MONGO_URL, PORT } = process.env;

mongoose
  .connect(MONGO_URL, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  })
  .then(() => console.log("MongoDB is  connected successfully"))
  .catch((err) => console.error(err));

app.listen(PORT, () => {
  console.log(`Server is listening on port ${PORT}`);
});

app.use(
  cors({
    origin: ["http://localhost:3000"],
    methods: ["GET", "POST", "PUT", "DELETE"],
    credentials: true,
  })
);
app.use(cookieParser());

app.use(express.json());

app.use("/", authRoute);
```

Le `cookie-parser` gère les sessions basées sur les cookies ou extrait les données des cookies. Il est ajouté au code ci-dessus avec le `authRoute` que l'application utilisera.

Maintenant, allons-y pour tester la route `/signup` avec un outil appelé [Postman](https://www.postman.com/downloads/). Assurez-vous d'être dans le répertoire `server` dans le terminal, puis exécutez `npm start` pour démarrer votre application.

![](https://i.imgur.com/zzN1QyQ.png)

L'image ci-dessus montre la réponse obtenue lorsqu'une requête est envoyée.

![](https://i.imgur.com/8jrGe0T.png)

L'image ci-dessus montre le cookie généré à partir de la réponse.

![](https://i.imgur.com/KJ8haPB.png)

L'image ci-dessus illustre ce qui se passe lorsque vous essayez d'utiliser un email déjà enregistré.

À ce stade, l'utilisateur sera créé dans la base de données comme le montre l'image ci-dessous :

![](https://i.imgur.com/XQsjWRt.png)


### Comment gérer la route LOGIN

Ouvrez le fichier `AuthController.js` dans le répertoire `Controllers`, et mettez-le à jour avec le code ci-dessous :

```javascript
module.exports.Login = async (req, res, next) => {
  try {
    const { email, password } = req.body;
    if(!email || !password ){
      return res.json({message:'All fields are required'})
    }
    const user = await User.findOne({ email });
    if(!user){
      return res.json({message:'Incorrect password or email' }) 
    }
    const auth = await bcrypt.compare(password,user.password)
    if (!auth) {
      return res.json({message:'Incorrect password or email' }) 
    }
     const token = createSecretToken(user._id);
     res.cookie("token", token, {
       withCredentials: true,
       httpOnly: false,
     });
     res.status(201).json({ message: "User logged in successfully", success: true });
     next()
  } catch (error) {
    console.error(error);
  }
}
```

Vous déterminez dans le code ci-dessus si l'`email` et le `password` correspondent à un `user` précédemment stocké dans la base de données.

Ensuite, ajoutez le code suivant au fichier `AuthRoute.js` dans le répertoire `Routes` :

```javascript
const { Signup, Login } = require('../Controllers/AuthController')
const router = require('express').Router()

router.post('/signup', Signup)
router.post('/login', Login)

module.exports = router
```

Maintenant, allons-y pour tester l'application :

![](https://i.imgur.com/gwRjAGk.png)

Si vous essayez d'utiliser un `email` ou un `password` non enregistré, vous recevrez le message ci-dessous :

![](https://i.imgur.com/fLj20iU.png)


### Comment gérer la route HOME

Maintenant, vous allez créer un fichier `AuthMiddleware.js`, dans le répertoire `Middlewares`, et coller le code ci-dessous :

```javascript
const User = require("../Models/UserModel");
require("dotenv").config();
const jwt = require("jsonwebtoken");

module.exports.userVerification = (req, res) => {
  const token = req.cookies.token
  if (!token) {
    return res.json({ status: false })
  }
  jwt.verify(token, process.env.TOKEN_KEY, async (err, data) => {
    if (err) {
     return res.json({ status: false })
    } else {
      const user = await User.findById(data.id)
      if (user) return res.json({ status: true, user: user.username })
      else return res.json({ status: false })
    }
  })
}
```

Le code ci-dessus vérifie si l'utilisateur a accès à la route en vérifiant si les `token`s correspondent.

Ensuite, mettez à jour le fichier `AuthRoute.js` dans le répertoire `Routes` avec le code ci-dessous :

```javascript
router.post('/',userVerification)
```

Maintenant, vous pouvez aller de l'avant pour tester votre route. Cela devrait ressembler à l'image ci-dessous :

![](https://i.imgur.com/xk1J1Zs.png)



## Comment implémenter le Frontend

Pour commencer, allez dans le répertoire `client` et installez ce qui suit dans votre terminal :

```shell
npm install react-cookie react-router-dom react-toastify axios
```

Maintenant, mettez à jour le fichier `index.js` dans le répertoire `client` avec l'extrait de code ci-dessous :

![](https://i.imgur.com/LcoXMWB.png)

Dans le code ci-dessus, envelopper votre composant `App` avec `BrowserRouter` est nécessaire pour activer le routage côté client et tirer parti de ses avantages dans votre application.

NB : Supprimez le `React.StrictMode` plus tard lorsque vous testez l'application et que vos données sont récupérées deux fois.

De plus, importez `react-toastify` pour qu'il soit disponible dans votre application.

Maintenant, allez-y pour créer le répertoire `pages` dans votre répertoire `client`, qui contiendra le fichier `Home.jsx`, le fichier `Login.jsx`, le fichier `Signup.jsx` et `index.js` pour exporter les composants. Votre dossier devrait ressembler à l'image ci-dessous :

![](https://i.imgur.com/G4rQ48P.png)

Maintenant, remplissez respectivement `Login.jsx`, `Signup.jsx`, et `Home.jsx`, avec le code ci-dessous. Ces extraits ci-dessous sont des composants fonctionnels qui seront modifiés plus tard dans ce guide.

NB : Cela peut être généré automatiquement en tapant le raccourci `rafce` + `enter` dans le fichier où vous souhaitez ajouter l'extrait dans votre éditeur Visual Studio Code. Assurez-vous que cette [extension](https://marketplace.visualstudio.com/items?itemName=dsznajder.es7-react-js-snippets) est installée dans votre Visual Studio Code pour que cela fonctionne.

`Login.jsx` :

```javascript
import React from "react";

const Login = () => {
  return <h1>Login Page</h1>;
};

export default Login
```

`Signup.jsx` :

```javascript
import React from "react";

const Signup = () => {
  return <h1>Signup Page</h1>;
};

export default Signup
```

`Home.jsx` :

```javascript
import React from "react";

const Home = () => {
  return <h1>Home PAGE</h1>;
};

export default Home
```

Après cela, vous irez dans le fichier `index.js` dans le répertoire `pages` pour exporter les composants nouvellement créés. Cela devrait ressembler à l'image ci-dessous :

![](https://i.imgur.com/XKroJyH.png)

La méthode montrée ci-dessus facilite l'importation des composants en ne nécessitant qu'une seule ligne d'importation.

Maintenant, mettez à jour le fichier `App.js` dans le répertoire `src` avec le code ci-dessous.

```javascript
import { Route, Routes } from "react-router-dom";
import { Login, Signup } from "./pages";
import Home from "./pages/Home";

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<Signup />} />
      </Routes>
    </div>
  );
}

export default App;
```

Les routes seront mises à disposition dans votre application en utilisant le code ci-dessus. L'exemple ci-dessous aidera à clarifier :

![](https://i.imgur.com/w78YqgX.gif)


### Comment gérer la logique de Signup

Dans le fichier `Signup.jsx` dans le répertoire `pages`, collez l'extrait de code suivant :

```javascript
import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import axios from "axios";
import { ToastContainer, toast } from "react-toastify";

const Signup = () => {
  const navigate = useNavigate();
  const [inputValue, setInputValue] = useState({
    email: "",
    password: "",
    username: "",
  });
  const { email, password, username } = inputValue;
  const handleOnChange = (e) => {
    const { name, value } = e.target;
    setInputValue({
      ...inputValue,
      [name]: value,
    });
  };

  const handleError = (err) =>
    toast.error(err, {
      position: "bottom-left",
    });
  const handleSuccess = (msg) =>
    toast.success(msg, {
      position: "bottom-right",
    });

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const { data } = await axios.post(
        "http://localhost:4000/signup",
        {
          ...inputValue,
        },
        { withCredentials: true }
      );
      const { success, message } = data;
      if (success) {
        handleSuccess(message);
        setTimeout(() => {
          navigate("/");
        }, 1000);
      } else {
        handleError(message);
      }
    } catch (error) {
      console.log(error);
    }
    setInputValue({
      ...inputValue,
      email: "",
      password: "",
      username: "",
    });
  };

  return (
    <div className="form_container">
      <h2>Signup Account</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="email">Email</label>
          <input
            type="email"
            name="email"
            value={email}
            placeholder="Enter your email"
            onChange={handleOnChange}
          />
        </div>
        <div>
          <label htmlFor="email">Username</label>
          <input
            type="text"
            name="username"
            value={username}
            placeholder="Enter your username"
            onChange={handleOnChange}
          />
        </div>
        <div>
          <label htmlFor="password">Password</label>
          <input
            type="password"
            name="password"
            value={password}
            placeholder="Enter your password"
            onChange={handleOnChange}
          />
        </div>
        <button type="submit">Submit</button>
        <span>
          Already have an account? <Link to={"/login"}>Login</Link>
        </span>
      </form>
      <ToastContainer />
    </div>
  );
};

export default Signup;
```



### Comment gérer la logique de Login

Ajoutez l'extrait de code suivant au fichier `Login.jsx` dans le répertoire `pages` :

```javascript
import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import axios from "axios";
import { ToastContainer, toast } from "react-toastify";

const Login = () => {
  const navigate = useNavigate();
  const [inputValue, setInputValue] = useState({
    email: "",
    password: "",
  });
  const { email, password } = inputValue;
  const handleOnChange = (e) => {
    const { name, value } = e.target;
    setInputValue({
      ...inputValue,
      [name]: value,
    });
  };

  const handleError = (err) =>
    toast.error(err, {
      position: "bottom-left",
    });
  const handleSuccess = (msg) =>
    toast.success(msg, {
      position: "bottom-left",
    });

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const { data } = await axios.post(
        "http://localhost:4000/login",
        {
          ...inputValue,
        },
        { withCredentials: true }
      );
      console.log(data);
      const { success, message } = data;
      if (success) {
        handleSuccess(message);
        setTimeout(() => {
          navigate("/");
        }, 1000);
      } else {
        handleError(message);
      }
    } catch (error) {
      console.log(error);
    }
    setInputValue({
      ...inputValue,
      email: "",
      password: "",
    });
  };

  return (
    <div className="form_container">
      <h2>Login Account</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="email">Email</label>
          <input
            type="email"
            name="email"
            value={email}
            placeholder="Enter your email"
            onChange={handleOnChange}
          />
        </div>
        <div>
          <label htmlFor="password">Password</label>
          <input
            type="password"
            name="password"
            value={password}
            placeholder="Enter your password"
            onChange={handleOnChange}
          />
        </div>
        <button type="submit">Submit</button>
        <span>
          Already have an account? <Link to={"/signup"}>Signup</Link>
        </span>
      </form>
      <ToastContainer />
    </div>
  );
};

export default Login;

```

### Comment gérer la logique de la page Home

Copiez et collez l'extrait de code suivant dans le fichier `Home.jsx` situé dans le répertoire `pages` :

```javascript
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { useCookies } from "react-cookie";
import axios from "axios";
import { ToastContainer, toast } from "react-toastify";

const Home = () => {
  const navigate = useNavigate();
  const [cookies, removeCookie] = useCookies([]);
  const [username, setUsername] = useState("");
  useEffect(() => {
    const verifyCookie = async () => {
      if (!cookies.token) {
        navigate("/login");
      }
      const { data } = await axios.post(
        "http://localhost:4000",
        {},
        { withCredentials: true }
      );
      const { status, user } = data;
      setUsername(user);
      return status
        ? toast(`Hello ${user}`, {
            position: "top-right",
          })
        : (removeCookie("token"), navigate("/login"));
    };
    verifyCookie();
  }, [cookies, navigate, removeCookie]);
  const Logout = () => {
    removeCookie("token");
    navigate("/signup");
  };
  return (
    <>
      <div className="home_page">
        <h4>
          {" "}
          Welcome <span>{username}</span>
        </h4>
        <button onClick={Logout}>LOGOUT</button>
      </div>
      <ToastContainer />
    </>
  );
};

export default Home;
```

Assurez-vous que les styles ci-dessous sont copiés dans votre fichier `index.css` :

```css
*,
::before,
::after {
  box-sizing: border-box;
  padding: 0;
  margin: 0;
}

label {
  font-size: 1.2rem;
  color: #656262;
}

html,
body {
  height: 100%;
  width: 100%;
}

body {
  display: flex;
  justify-content: center;
  align-items: center;
  background: linear-gradient(
    90deg,
    rgba(2, 0, 36, 1) 0%,
    rgba(143, 187, 204, 1) 35%,
    rgba(0, 212, 255, 1) 100%
  );
  font-family: Verdana, Geneva, Tahoma, sans-serif;
}

.form_container {
  background-color: #fff;
  padding: 2rem 3rem;
  border-radius: 0.5rem;
  width: 100%;
  max-width: 400px;
  box-shadow: 8px 8px 24px 0px rgba(66, 68, 90, 1);
}

.form_container > h2 {
  margin-block: 1rem;
  padding-block: 0.6rem;
  color: rgba(0, 212, 255, 1);
}

.form_container > form {
  display: flex;
  flex-direction: column;
  gap: 1.4rem;
}

.form_container div {
  display: flex;
  flex-direction: column;
  gap: 0.3rem;
}

.form_container input {
  border: none;
  padding: 0.5rem;
  border-bottom: 1px solid gray;
  font-size: 1.1rem;
  outline: none;
}

.form_container input::placeholder {
  font-size: 0.9rem;
  font-style: italic;
}

.form_container button {
  background-color: rgba(0, 212, 255, 1);
  color: #fff;
  border: none;
  padding: 0.6rem;
  font-size: 1rem;
  cursor: pointer;
  border-radius: 0.3rem;
}

span a {
  text-decoration: none;
  color: rgba(0, 212, 255, 1);
}

.home_page {
  height: 100vh;
  width: 100vw;
  background: #000;
  color: white;
  display: flex;
  justify-content: center;
  align-items: center;
  text-transform: uppercase;
  font-size: 3rem;
  flex-direction: column;
  gap: 1rem;
}

.home_page span {
  color: rgba(0, 212, 255, 1);
}

.home_page button {
  background-color: rgb(27, 73, 83);
  color: #fff;
  cursor: pointer;
  padding: 1rem 3rem;
  font-size: 2rem;
  border-radius: 2rem;
  transition: ease-in 0.3s;
  border: none;
}

.home_page button:hover {
  background-color: rgba(0, 212, 255, 1);
}


@media only screen and (max-width: 1200px){
  .home_page{
    font-size: 1.5rem;
  }
  .home_page button {
    padding: 0.6rem 1rem;
    font-size: 1.5rem;
  }
}
```

Je vais maintenant démontrer rapidement tout ce que vous avez appris dans cet article.

![](https://i.imgur.com/1mQJVm7.gif)


## Conclusion

Dans cet article, vous avez appris comment utiliser JWT pour l'authentification et l'autorisation, vous aidant à construire des applications Node.js sécurisées.

Ce guide peut vous aider à vous protéger contre les menaces de sécurité et à prévenir l'accès non autorisé en mettant en œuvre des procédures d'authentification et d'autorisation solides.