---
title: Comment construire une application de télémédecine en utilisant Stream Video
  et Chat SDK dans React
subtitle: ''
author: Okoro Emmanuel Nzube
co_authors: []
series: null
date: '2025-07-18T22:53:24.426Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-telehealth-app-using-stream-video-and-chat-sdk-in-react
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1752879185676/ab0574c8-d16b-41d0-8883-7df0f4bd0eb5.png
tags:
- name: streams SDK
  slug: streams-sdk
- name: Streams
  slug: streams
- name: React
  slug: reactjs
- name: Tailwind CSS
  slug: tailwind-css
- name: MERN Stack
  slug: mern
- name: Mern Stack Development
  slug: mern-stack-development
seo_title: Comment construire une application de télémédecine en utilisant Stream
  Video et Chat SDK dans React
seo_desc: "Remember when the COVID-19 pandemic moved everything online – doctor’s\
  \ visits included – and staying home became the safest option? \nThat moment kicked\
  \ off a massive shift in how healthcare gets delivered. \nTelehealth became more\
  \ than a workaround. I..."
---

Vous souvenez-vous lorsque la pandémie de COVID-19 a tout déplacé en ligne, y compris les visites chez le médecin, et que rester à la maison est devenu l'option la plus sûre ?

Ce moment a marqué un changement massif dans la manière dont les soins de santé sont dispensés.

La [télémédecine](https://getstream.io/chat/solutions/healthcare/) est devenue plus qu'une solution de contournement. Elle fait désormais partie intégrante des soins modernes. Alors que la demande augmente, les développeurs se mobilisent pour construire des plateformes sécurisées et en temps réel qui connectent les patients et les prestataires de soins de n'importe où.

Dans cet article, vous apprendrez à construire une application de télémédecine avec les SDK [React Video](https://getstream.io/video/sdk/react/) et [Chat](https://getstream.io/chat/sdk/react/) de Stream. Vous mettrez en place l'authentification, créerez des appels vidéo, activerez la messagerie et concevrez une interface utilisateur fonctionnelle qui imite les flux de travail réels de la télémédecine.

Commençons.

## Plan

* [Introduction](#heading-introduction)
    
* [Prérequis](#heading-prerequisites)
    
* [Structure de l'application](#heading-app-structure)
    
* [Configuration du projet](#heading-installation)
    
* [Configuration du backend](#heading-backend-setup)
    
* [Configuration du frontend](#heading-frontend-setup)
    
* [Intégration de Stream Chat et Video](#heading-stream-chat-and-video-integration)
    
* [Fonction de chat et vidéo (Frontend)](#heading-chat-and-video-function-\(frontend\))
    
* [Démonstration du projet](#heading-project-demo)
    
* [Conclusion](#heading-conclusion)
    

## Prérequis

Avant de commencer ce tutoriel, assurez-vous d'avoir :

* Une compréhension de base de React.
    
* Node.js et npm/yarn installés sur votre ordinateur
    
* Un [compte gratuit avec Stream](https://getstream.io/try-for-free/)
    
* Une familiarité avec les SDK de Stream
    
* Une compréhension de base de Tailwind CSS pour le style
    
* Une expérience avec VS Code et Postman (pour tester les API)
    

## **Structure de l'application**

Avant de plonger dans le code, il est utile de comprendre comment l'application est structurée.

```markdown
# Structure du flux de l'application

- Page d'accueil  
  - Navigation  
    - Accueil  
    - À propos  
    - Inscription  
      - Vérifier le compte  
        - Se connecter  
          - Tableau de bord  
            - Stream Chat  
            - Stream Video  
            - Se déconnecter
```

## **Configuration du projet**

Avant de commencer, créez deux dossiers : « Frontend » pour gérer le code côté client et « Backend » pour la logique côté serveur. Cette séparation vous permet de gérer efficacement les deux parties de votre application.

### **Configurer React pour le Frontend**

Une fois les dossiers créés, vous pouvez configurer l'application React dans le dossier Frontend.

Tout d'abord, naviguez vers le répertoire Frontend en utilisant la commande `cd Frontend`.

Vous pouvez maintenant initialiser votre projet React. Vous utiliserez Vite, un outil de construction rapide pour les applications React.

Pour créer votre projet React, exécutez la commande suivante :

`npm create vite@latest [nom du projet] -- --template react`

Ensuite, naviguez vers votre nouveau dossier de projet, en utilisant la commande :

`cd [nom du projet]`

Une fois là-bas, installez les dépendances requises en exécutant :

`npm install`

Cette commande installe à la fois le dossier `node_modules` (qui contient tous les packages de votre projet) et le fichier `package-lock.json` (qui enregistre les versions exactes des packages installés).

Ensuite, vous devrez installer Tailwind CSS pour le style. Suivez la [documentation de Tailwind](https://v3.tailwindcss.com/docs/guides/vite) pour des instructions étape par étape.

Ensuite, il est temps de configurer le site Web. En utilisant React, vous créerez les pages de connexion/d'inscription à la maison. Les deux seront imbriquées ensemble en utilisant `React-router-dom`.

Voici à quoi ressemble la [page d'accueil](https://github.com/Derekvibe/Telehealth_Frontend/tree/main/src/pages/Home) :

![Page d'accueil de la télémédecine](https://cdn.hashnode.com/res/hashnode/image/upload/v1752705718347/ed5dd289-2998-41f7-8d10-352aa35fe614.gif align="center")

Maintenant, l'utilisateur a un endroit où atterrir chaque fois qu'il visite le site Web.

Configurons le backend.

## **Configuration du Backend**

### **Installation des packages requis**

Avant de configurer le backend de votre projet, il est important de définir ce que votre projet doit offrir. Cela vous aidera à installer tous les packages nécessaires en une seule fois.

Commencez par vous déplacer dans le dossier backend en utilisant la commande : `cd Backend`

À l'intérieur du répertoire Backend, initialisez votre projet Node.js en utilisant `npm install`

Cela créera un fichier `package.json`, qui stocke les métadonnées et les dépendances de votre projet.

Ensuite, installez toutes les dépendances nécessaires pour construire votre backend. Exécutez la commande suivante :

`npm i bcryptjs cookie-parser cors dotenv express jsonwebtoken mongoose nodemailer validator nodemon`

Voici un bref aperçu de ce que fait chaque package :

* bcryptjs : Chiffre les mots de passe des utilisateurs pour un stockage sécurisé.
    
* Cookie-parser : Gère les cookies dans votre application.
    
* CORS : Middleware qui permet les requêtes cross-origin - essentiel pour la communication frontend-backend.
    
* dotenv : Charge les variables d'environnement à partir d'un fichier `.env` dans process.env.
    
* Express : Le framework principal pour construire votre serveur et les routes API.
    
* jsonwebtoken : Génère et vérifie les jetons JWT pour l'authentification.
    
* Mongoose : Connecte votre application à une base de données MongoDB.
    
* nodemailer : Gère l'envoi d'e-mails depuis votre application.
    
* Validator : Valide les entrées utilisateur comme l'e-mail, les chaînes, etc.
    
* nodemon : Redémarre automatiquement votre serveur lorsque des modifications sont apportées aux fichiers.
    

Une fois vos packages installés, créez deux fichiers clés dans le répertoire backend : `App.js`, qui contient la logique de votre application, le middleware et les gestionnaires de routes, et `server.js`, responsable de l'initialisation et de la configuration de votre serveur.

Ensuite, vous devez mettre à jour le script de démarrage de votre `package.json`. Rendez-vous dans le fichier `package.json` de votre répertoire backend et remplacez le script par défaut :

```json
"scripts": {
	"test": "echo\Erreur : aucun test spécifié\" && exit 1
  }
```

par ceci :

```json
"scripts": {
    "start": "nodemon server.js"
}
```

Cette configuration vous permet d'exécuter votre serveur en utilisant `nodemon`, le rechargeant automatiquement lorsque des modifications sont apportées. Cela aide à augmenter la productivité pendant le développement.

Pour vérifier si votre configuration backend est correcte, ouvrez le fichier `server.js` et ajoutez un log de test : `console.log("N'importe quel message de log")`. Ensuite, rendez-vous dans votre terminal dans le répertoire backend, et exécutez npm start. Vous devriez voir le message de log dans le terminal, confirmant que votre backend est en cours d'exécution.

![Test du serveur backend](https://cdn.hashnode.com/res/hashnode/image/upload/v1752703046663/dc06ce5a-3b6c-4846-bd33-53c423a57235.png align="center")

### Configuration de `App.js`

Dans le fichier `App.js`, commencez par importer les packages que vous avez initialement installés.

```javascript
const express = require("express");

const cors = require("cors");

const cookieParser = require("cookie-parser");

const app = express();


app.use(

 cors({

origin: [

 "http://localhost:5173",

],

credentials: true,

})

);

app.use(express.json({ limit: "10kb" }));

app.use(cookieParser());

module.exports = app;
```

Voici ce que fait le code ci-dessus :

Les instructions require importent `express`, `cors`, et `cookie-parser`, qui sont essentiels pour créer votre serveur backend, gérer les requêtes cross-origin et analyser les cookies.

La commande `const app = express();` configure une nouvelle instance d'une application Express.

`app.use(cors({ origin: ["`[`http://localhost:5173`](http://localhost:5173)`"], credentials: true }));` accorde la permission ou permet les requêtes de votre frontend et active le partage de cookies entre le frontend et le backend de votre application. Cela est important pour l'authentification.

La commande `app.use(express.json({ limit: "10kb" }));` est une fonction middleware qui garantit que le serveur peut traiter les charges utiles JSON entrantes et protège contre les requêtes trop volumineuses, qui pourraient être utilisées dans des attaques DoS.

La commande `app.use(cookieParser());` rend les cookies disponibles via `req.cookies`.

Enfin, la commande `module.exports = app;` permet à l'application d'être importée dans d'autres fichiers, en particulier dans `server.js`, où l'application sera démarrée.

### Configuration de `Server.js`

Une fois que `App.js` est configuré, l'étape suivante consiste à créer et configurer votre serveur dans un nouveau fichier appelé `server.js`.

Avant de faire cela, assurez-vous d'avoir une **base de données MongoDB** configurée. Si vous n'en avez pas encore, vous pouvez [suivre ce tutoriel vidéo](https://youtu.be/pO6m0nmo1k0?si=Rqi_50fnsfQrM-ww) pour configurer une base de données MongoDB.

Après avoir configuré MongoDB, vous recevrez un `nom d'utilisateur` et un `mot de passe`. Copiez le mot de passe, rendez-vous dans votre répertoire backend, et créez un fichier `.env` pour le stocker.

Après avoir stocké le mot de passe, retournez pour compléter la configuration de votre base de données.

Ensuite, cliquez sur le bouton "Créer un utilisateur de base de données", puis cliquez sur l'option `choisir la méthode de connexion`. Puisque nous utilisons Node.js pour ce projet, choisissez l'option "Pilotes". Cela vous donne la chaîne de connexion de la base de données (vous devriez la voir au n° 3).

![Authentification de la chaîne de la base de données](https://cdn.hashnode.com/res/hashnode/image/upload/v1752706253668/ad0cdbb4-453c-4291-ab4c-395d14ce297c.gif align="center")

Ensuite, rendez-vous dans votre `.env` et collez-la là, et ajoutez `auth` immédiatement après avoir "net/ ".

Voici à quoi cela ressemble :

`mongodb+srv://<username>:<password>@cluster0.qrrtmhs.mongodb.net/auth?retryWrites=true&w=majority&appName=Cluster0`

![Fichier config.env du backend](https://cdn.hashnode.com/res/hashnode/image/upload/v1752767020758/aee4f54c-e562-4916-a8f5-b97590a671d1.png align="center")

Enfin, mettez votre adresse IP sur liste blanche. Cela garantit que votre backend peut se connecter à MongoDB depuis votre machine locale ou tout environnement pendant le développement.

Pour permettre à votre application de se connecter à la base de données :

* Allez dans la section "Accès réseau" dans la barre latérale de sécurité de votre tableau de bord MongoDB.
    
* Cliquez sur "AJOUTER UNE ADRESSE IP".
    
* Choisissez "Autoriser l'accès depuis n'importe où", puis cliquez sur Confirmer.
    

À ce stade, vous pouvez configurer votre `server.js`

```javascript
//server.js
require("dotenv").config();
const mongoose = require("mongoose");
const dotenv = require("dotenv"); //pour gérer notre variable d'environnement
 
dotenv.config({ path: "./config.env" });
// console.log(process.env.NODE_ENV);
 
const app = require("./app");
 
const db = process.env.DB;
//connecter l'application à la base de données en utilisant MongoDB
 
mongoose
  .connect(db)
  .then(() => {
	console.log("Connexion à la base de données réussie");
  })
  .catch((err) => {
	console.log(err);
  });
 
const port = process.env.PORT || 3000;
// console.log(process.env.PORT)
 
app.listen(port, () => {
  console.log(`Application en cours d'exécution sur le port ${port}`);
});
```

Le fichier `server.js` est responsable de la gestion de toutes les fonctions et logiques liées au serveur. À partir du code ci-dessus, le fichier `server.js` charge les variables d'environnement en utilisant `dotenv`, connecte votre backend à MongoDB en utilisant `mongoose`, et démarre le serveur Express. Il obtient l'URL de la base de données et le port à partir du fichier `config.env`, se connecte à la base de données, puis exécute votre application sur le port spécifié (`8000`).

Si le port spécifié n'est pas trouvé, il revient au port `3000` et un message de confirmation est imprimé sur la console indiquant que le serveur est en cours d'exécution sur le port spécifié.

![server-js Telehealth App](https://cdn.hashnode.com/res/hashnode/image/upload/v1752703203108/a94c724c-ad9c-4653-9081-894ac6e44dd6.png align="center")

### Connecter la base de données à MongoDB Compass

Tout d'abord, téléchargez l'application MongoDB Compass. (Allez ici pour télécharger et installer : [https://www.mongodb.com/try/download/compass](https://www.mongodb.com/try/download/compass)). L'application MongoDB Compass nous permet de gérer facilement nos données.

Une fois l'installation terminée, ouvrez l'application et cliquez sur `Cliquez pour ajouter une nouvelle connexion`. Allez dans votre fichier `.env`, copiez la chaîne de connexion que vous avez initialement obtenue lors de la configuration de MongoDB, collez-la dans la section URL, puis cliquez sur "connecter". Cette configuration vous aide à gérer vos données lorsque vous créez et supprimez des utilisateurs.

![Mongo-DB-Compass](https://cdn.hashnode.com/res/hashnode/image/upload/v1752703344533/8dff0ff6-66e9-4359-a2c0-fe7a4bd5e4ba.png align="center")

### **Mettre en place une méthode avancée de gestion des erreurs**

Vous allez maintenant créer un mécanisme avancé de gestion des erreurs. Pour ce faire, créez un dossier utils dans votre backend, un fichier `catchAsync.js` dans le dossier utils, et ajoutez ce code :

```javascript
//catchAsync.js
module.exports = (fn) => {
  return (req, res, next) => {
	fn(req, res, next).catch(next);
  };
};
```

Ensuite, créez un fichier `appError.js` toujours dans votre dossier utils. Dans le fichier `appError.js`, ajoutez la commande suivante :

```javascript
class AppError extends Error {
  constructor(message, statusCode) {
	super(message);
 
	this.statusCode = statusCode;
	this.status = `${statusCode}`.startsWith("4") ? "fail" : "error";
	this.isOperational = true;
 
	Error.captureStackTrace(this, this.constructor);
  }
}
 
module.exports = AppError;
```

Le code ci-dessus est utile pour suivre et tracer les erreurs. Il vous fournit également l'URL et l'emplacement du fichier où votre erreur pourrait se produire, ce qui aide à une gestion des erreurs et un débogage plus propres.

Ensuite, créons un gestionnaire d'erreurs global. Commencez par créer un nouveau dossier dans le répertoire backend, et nommez-le "controller". Dans le dossier controller, créez votre fichier de gestion des erreurs globales. Vous pouvez le nommer comme vous le souhaitez. Dans cet exemple, il s'appelle `globalErrorHandler.js`.

Votre fichier `globalErrorHandler` définira plusieurs fonctions qui gèrent des types d'erreurs spécifiques, telles que les problèmes de base de données, les échecs de validation, ou même les problèmes de JWT, et renvoie une réponse d'erreur bien formatée pour les utilisateurs. Pour que le `globalErrorHandler` fonctionne correctement, vous devez créer une fonction de contrôleur.

Donc, ensuite, créez un fichier `errorController.js` (toujours à l'intérieur du dossier controller). Le fichier `errorController.js` répond à l'utilisateur chaque fois qu'une erreur est capturée, en envoyant l'erreur au format JSON.

`globalErrorHandler.js` :

```javascript
// globalErrorHandler.js
const AppError = require("../utils/appError");
 
const handleCastErrorDB = (err) => {
  const message = `Invalid ${err.path}: ${err.value}.`;
  return new AppError(message, 400);
};
 
const handleDuplicateFieldsDB = (err) => {
  const value = err.keyValue ? JSON.stringify(err.keyValue) : "duplicate field";
  const message = `Duplicate field value: ${value}. Please use another value!`;
  return new AppError(message, 400);
};
 
const handleValidationErrorDB = (err) => {
  const errors = Object.values(err.errors).map((el) => el.message);
  const message = `Invalid input: ${errors.join(". ")}`;
  return new AppError(message, 400);
};
 
const handleJWTError = () =>
  new AppError("Invalid token. Please log in again!", 401);
const handleJWTExpiredError = () =>
  new AppError("Your token has expired! Please log in again.", 401);
 
module.exports = {
  handleCastErrorDB,
  handleDuplicateFieldsDB,
  handleValidationErrorDB,
  handleJWTError,
  handleJWTExpiredError,
};
```

Voici ce que fait le code ci-dessus :

La section `const handleCastErrorDB = (err) =>..` gère les erreurs CastError de MongoDB qui se produisent généralement lorsqu'un ID invalide est passé, et renvoie une réponse d'erreur `400 Bad Request` en utilisant votre classe `AppError`.

La section `const handleDuplicateFieldsDB = (err) =>...` vérifie et gère les erreurs de clé dupliquée de MongoDB, telles que tenter de s'inscrire avec un email ou un nom d'utilisateur déjà pris, et renvoie une erreur `400 Bad Request`.

La section `const handleValidationErrorDB = (err) =>...` gère les erreurs de validation de Mongoose (comme les champs requis manquants ou les mauvais types de données). Elle rassemble tous les messages d'erreur de validation individuels et les combine en un seul.

Les sections `const handleJWTError = () =>` et `const handleJWTExpiredError = () =>` gèrent les erreurs qui peuvent survenir en raison de jetons JWT invalides, falsifiés ou expirés, et renvoient une réponse d'erreur `401 Unauthorized`.

La section `module.exports = {};` exporte tous les gestionnaires d'erreurs individuels afin qu'ils puissent être utilisés dans le fichier `errorController.js`.

`errorController.js` :

```javascript
//errorController.js
const errorHandlers = require("./globalErrorHandler");

const {
  handleCastErrorDB,
  handleDuplicateFieldsDB,
  handleValidationErrorDB,
  handleJWTError,
  handleJWTExpiredError,
} = errorHandlers;

module.exports = (err, req, res, next) => {
  err.statusCode = err.statusCode || 500;
  err.status = err.status || "error";

  let error = { ...err, message: err.message };

  if (err.name === "CastError") error = handleCastErrorDB(err);
  if (err.code === 11000) error = handleDuplicateFieldsDB(err);
  if (err.name === "ValidationError") error = handleValidationErrorDB(err);
  if (err.name === "JsonWebTokenError") error = handleJWTError();
  if (err.name === "TokenExpiredError") error = handleJWTExpiredError();

  res.status(error.statusCode).json({
    status: error.status,
    message: error.message,
    ...(process.env.NODE_ENV === "production" && { error, stack: err.stack }),
  });
};
```

Pour vous assurer que votre fonction de gestion des erreurs fonctionne correctement, rendez-vous dans votre `App.js` et ajoutez la commande :

```javascript
//import command
const globalErrorHandler = require("./controller/errorController");
const AppError = require("./utils/appError");
 
//Catch unknown routes
app.all("/{*any}", (req, res, next) => {
  next(new AppError(`Can't find ${req.originalUrl} on this server!`, 404)); });
 
app.use(globalErrorHandler);
```

Cela garantit que toutes les erreurs sont correctement gérées et envoie la réponse d'erreur à l'utilisateur.

### **Créer un modèle d'utilisateur**

Pour construire un modèle d'utilisateur, créez un nouveau dossier dans le répertoire backend et nommez-le "model". À l'intérieur du dossier model, créez un nouveau fichier nommé `userModel.js`.

Le fichier `userModel.js` est construit essentiellement pour l'authentification et la sécurité des utilisateurs. Il fournit un schéma riche en validation pour gérer les utilisateurs en utilisant Mongoose, qui mappe comment les données des utilisateurs sont structurées dans la base de données MongoDB. Il inclut des validations, le hachage des mots de passe et des méthodes pour comparer les mots de passe des utilisateurs de manière sécurisée.

```javascript
//userModel.js
const mongoose = require("mongoose");
const validator = require("validator");
const bcrypt = require("bcryptjs");
 
const userSchema = new mongoose.Schema(
  {
	username: {type: String, required: [true, "Please provide username"], trim: true, minlength: 3, maxlength: 30, index: true,},
	email: {type: String, required: [true, "Please Provide an email"], unique: true, lowercase: true, validate: [validator.isEmail, "Please provide a valid email"],},
	password: {type: String, required: [true, "Please provide a Password"], minlength: 8, select: false,},
	passwordConfirm: {type: String, required: [true, "Please confirm your Password"],
 	validate: {validator: function (el) {return el === this.password;},
    	message: "Passwords do not match",
  	},
	},
	isVerified: {type: Boolean, default: false,}, otp: String,
	otpExpires: Date,
 	resetPasswordOTP: String,
  	resetPasswordOTPExpires: Date,
	createdAt: {type: Date, default: Date.now,},}, { timestamps: true });
 
// Hash password before saving
userSchema.pre("save", async function (next) {
  if (!this.isModified("password")) return next();
 
  this.password = await bcrypt.hash(this.password, 12);
  this.passwordConfirm = undefined; // Remove passwordConfirm before saving
  next();
});
 
const User = mongoose.model("User", userSchema);
module.exports = User;
```

### **Contrôleur d'authentification**

Maintenant, vous pouvez créer une logique qui régule le processus d'authentification de votre utilisateur. Cette logique d'authentification se compose de l'inscription, de la connexion (login), de l'OTP, etc.

Pour ce faire, rendez-vous d'abord dans votre dossier controller et créez un nouveau fichier. Appelez-le `authController.js` car il gère le flux d'authentification de votre projet.

Après avoir créé le fichier, vous créerez votre fonction d'inscription.

```javascript
//import
const User = require("../model/userModel");
const AppError = require("../utils/appError");
const catchAsync = require("../utils/catchAsync");
const generateOtp = require("../utils/generateOtp");
const jwt = require("jsonwebtoken");
const sendEmail = require("../utils/email")
 
exports.signup = catchAsync(async (req, res, next) => {
  const { email, password, passwordConfirm, username } = req.body;

  const existingUser = await User.findOne({ email });
 
  if (existingUser) return next(new AppError("Email already registered", 400));
 
  const otp = generateOtp();
 
  const otpExpires = Date.now() + 24 60 60 * 1000; //when thhe otp will expire (1 day)
 
  const newUser = await User.create({
	username,
	email,
	password,
	passwordConfirm,
	otp,
	otpExpires,
  });
 
  //configure email sending functionality
  try {
	await sendEmail({
  	email: newUser.email,
  	subject: "OTP for email Verification",
  	html: `<h1>Your OTP is : ${otp}</h1>`,
	});
 
	createSendToken(newUser, 200, res, "Registration successful");
  } catch (error) {
	console.error("Email send error:", error);
	await User.findByIdAndDelete(newUser.id);
	return next(
  	new AppError("There is an error sending the email. Try again", 500)
	);
  }
});
```

`const { email, password, passwordConfirm, username } = req.body;` extrait les détails d'inscription nécessaires de la requête entrante : email, mot de passe, confirmation du mot de passe et nom d'utilisateur lors de l'inscription de l'utilisateur.

`const existingUser = await User.findOne({ email });` vérifie la base de données pour voir si un utilisateur existe déjà avec l'email donné. Si oui, il envoie une réponse d'erreur en utilisant votre utilitaire `AppError`.

`const otp = generateOtp();` génère l'OTP, et `const otpExpires =` [`Date.now`](http://date.now)`()..` est utilisé pour définir l'expiration de l'OTP à une heure ou un jour spécifié.

Avec `const newUser = await User.create({});`, le nouvel utilisateur est enregistré dans MongoDB avec ses identifiants et les informations OTP, le mot de passe étant automatiquement haché.

`await sendEmail({});` envoie un email à l'utilisateur. Cet email contient leur OTP de connexion. Si l'email est envoyé avec succès, `createSendToken(newUser, 200, res, "Registration successful");` (qui est une fonction utilitaire) génère un jeton JWT et l'envoie dans la réponse avec un message de succès.

Si l'envoi de l'email échoue ou si quelque chose ne va pas, `await User.findByIdAndDelete(`[`newUser.id`](http://newuser.id)`);` supprime l'utilisateur de la base de données pour garder les choses propres, et un message d'erreur de `There is an error sending the email. Try again", 500` est retourné.

### **Générer un OTP**

Pour vous assurer que l'OTP de vos utilisateurs leur est envoyé avec succès, dans le dossier utils, créez un nouveau fichier et nommez-le `generateOtp.js`. Ensuite, ajoutez le code :

```javascript
module.exports = () => {
  return Math.floor(1000 + Math.random() * 9000).toString();
};
```

Le code ci-dessus est une fonction qui génère un OTP aléatoire de 4 chiffres pour l'utilisateur et le retourne sous forme de chaîne.

Après avoir complété le code ci-dessus, allez dans votre authController.js et assurez-vous d'importer le `generateOtp.js` dans la section d'importation.

### **Créer un jeton utilisateur**

Ensuite, le jeton de connexion de l'utilisateur sera créé et il sera attribué à l'utilisateur lors de la connexion.

```javascript
const signToken = (userId) => {
  return jwt.sign({ id: userId }, process.env.JWT_SECRET, {
	expiresIn: process.env.JWT_EXPIRES_IN || "90d",
  });
};
 
//function to create the token
const createSendToken = (user, statusCode, res, message) => {
  const token = signToken(user._id);
 
  //function to generate the cookie
  const cookieOptions = {
	expires: new Date(
  	Date.now() + process.env.JWT_COOKIE_EXPIRES_IN 24 60 60 1000
	),
 
	httponly: true,
	secure: process.env.NODE_ENV === "production", //only secure in production
	sameSite: process.env.NODE_ENV === "production" ? "none" : "Lax",
  };
 
  res.cookie("token", token, cookieOptions);
 
  user.password = undefined;
  user.passwordConfirm = undefined;
  user.otp = undefined;
```

Avant que le code ci-dessus ne puisse fonctionner parfaitement, créez un JWT dans votre fichier `.env`.

```javascript
//.env
JWT_SECRET = kaklsdolrnnhjfsnlsoijfbwhjsioennbandksd;
JWT_EXPIRES_IN = 90d
JWT_COOKIE_EXPIRES_IN = 90
```

Voici à quoi doit ressembler le fichier `.env`. Votre `JWT_SECRET` peut être n'importe quoi, comme vous pouvez le voir dans le code.

Note : La logique de création du jeton utilisateur doit s'exécuter avant la logique de connexion. Donc dans ce cas, la logique `signToken` et `createSendToken` doit être placée en haut avant la logique `signup`.

### **Envoyer un email**

Ensuite, vous devez configurer la fonctionnalité d'envoi d'email afin de pouvoir envoyer automatiquement l'OTP de l'utilisateur à son email chaque fois qu'il se connecte. Pour configurer l'email, rendez-vous dans le dossier utils, créez un nouveau fichier et donnez-lui un nom. Dans cet exemple, le nom est `email.js`.

Dans `email.js`, nous allons envoyer des emails en utilisant le package `nodemailer` et Gmail comme fournisseur.

```javascript
//email.js
const nodemailer = require('nodemailer');
 
const sendEmail = async (options) => {
  const transporter = nodemailer.createTransport({
	service: 'Gmail',
	auth: {
  	user: process.env.HOST_EMAIL,
  	pass: process.env.EMAIL_PASS
	}
  })
 
  //defining email option and structure
 
  const mailOptions = {
	from: `"{HOST Name}" <{HOST Email} >`,
	to: options.email,
	subject: options.subject,
	html: options.html,
  };
  await transporter.sendMail(mailOptions);
};
 
module.exports = sendEmail;
```

À partir du code ci-dessus, la commande `const nodemailer = require('nodemailer');` importe le package `nodemailer`. Il s'agit d'une bibliothèque Node.js populaire pour l'envoi d'e-mails.

La commande `const transporter = nodemailer.createTransport({..})` est un transporteur d'e-mails. Puisque nous allons utiliser le fournisseur de services Gmail, `service` sera attribué à `Gmail` et `auth` récupère votre adresse Gmail et votre mot de passe à partir du fichier `.env` où ils sont stockés.

Note : Le mot de passe n'est pas votre mot de passe Gmail réel, mais plutôt votre mot de passe d'application Gmail. Vous pouvez voir comment obtenir votre [mot de passe Gmail ici](https://youtu.be/MkLX85XU5rU?si=yBIj4MJDLY7-k-c4).

Une fois que vous avez obtenu avec succès votre mot de passe d'application Gmail, stockez-le dans votre fichier `.env`.

### **Création de routes**

À ce stade, vous avez terminé la configuration de la fonction d'inscription de votre projet. Ensuite, vous devez tester si votre inscription fonctionne correctement en utilisant Postman. Mais avant cela, définissons et définissons une route où la fonction d'inscription sera exécutée.

Pour configurer votre route, créez un nouveau dossier dans votre répertoire backend nommé "routes" et un fichier nommé `userRouter.js`.

```javascript
const express = require("express");
const {signup} = require(../controller/authController);
 
const router = express.Router();
router.post("/signup", signup);
 
module.exports = router;
```

Ensuite, allez dans votre fichier `App.js` et ajoutez le routeur.

```javascript
const userRouter = require("./routes/userRouters"); //Route import statement
app.use("/api/v1/users", userRouter) //common route for all auth, i.e sign up, log in, forget password, etc.
```

Après avoir configuré vos routes, vous pouvez tester votre inscription pour voir si elle fonctionne. Il s'agit d'une requête post, et l'URL de la route sera [`http://localhost:8000/api/v1/users/signup`](http://localhost:8000/api/v1/users/signup%60).

![Test d'inscription d'un nouvel utilisateur](https://cdn.hashnode.com/res/hashnode/image/upload/v1752704061383/380d8480-9997-4678-8ca7-0ed86ea24481.png align="center")

L'image ci-dessus montre que la fonction d'inscription fonctionne parfaitement avec un `statusCode` de `200` et un code OTP envoyé à l'email de l'utilisateur.

Félicitations pour être arrivé à ce stade ! Vous pouvez vérifier votre base de données MongoDB pour voir si l'utilisateur est affiché.

![Affichage de l'utilisateur dans Mongo-DB-Compass](https://cdn.hashnode.com/res/hashnode/image/upload/v1752703565468/0f23f8ab-d17e-4555-8347-475bb6483b8a.png align="center")

À partir de l'image ci-dessus, vous pouvez voir que les détails de l'utilisateur sont obtenus et que le mot de passe est sous une forme cryptée, ce qui garantit que les informations d'identification de l'utilisateur sont sécurisées.

### **Créer une fonction de contrôleur de vérification de compte**

Dans cette section, vous allez créer une fonction de contrôleur de vérification de compte. Cette fonction vérifie le compte d'un utilisateur à l'aide du code OTP envoyé à son adresse e-mail.

Tout d'abord, allez dans votre fichier `authController.js` et ajoutez :

```javascript
exports.verifyAccount = catchAsync(async (req, res, next) => {
  const { email, otp } = req.body;
 
  if (!email || !otp) {
	return next(new AppError("Email and OTP are required", 400));
  }
 
  const user = await User.findOne({ email });
 
  if (!user) {
	return next(new AppError("No user found with this email", 404));
  }
 
  if (user.otp !== otp) {
	return next(new AppError("Invalid OTP", 400));
  }
 
  if (Date.now() > user.otpExpires) {
	return next(
  	new AppError("OTP has expired. Please request a new OTP.", 400)
	);
  }
 
  user.isVerified = true;
  user.otp = undefined;
  user.otpExpires = undefined;
 
  await user.save({ validateBeforeSave: false });
 
  //  Optionally return a response without logging in
  res.status(200).json({
	status: "success",
	message: "Email has been verified",
  });
});
```

Ensuite, créez une fonction middleware pour authentifier l'utilisateur actuellement connecté.

Dans votre répertoire backend, créez un nouveau dossier appelé `middlewares`. À l'intérieur du dossier `middlewares`, créez un fichier nommé `isAuthenticated.js`.

Ajoutez le code suivant :

```javascript
//isAuthenticated.js
const jwt = require("jsonwebtoken");
const catchAsync = require("../utils/catchAsync");
const AppError = require("../utils/appError");
const User = require("../model/userModel");
 
const isAuthenticated = catchAsync(async (req, res, next) => {
  let token;
 
  // 1. Retrieve token from cookies or Authorization header
  if (req.cookies?.token) {
	token = req.cookies.token;
  } else if (req.headers.authorization?.startsWith("Bearer")) {
	token = req.headers.authorization.split(" ")[1];
  }
 
  if (!token) {
	return next(
  	new AppError(
    	"You are not logged in. Please log in to access this resource.",
    	401
  	)
	);
  }
 
  // 2. Verify token
  let decoded;
  try {
	decoded = jwt.verify(token, process.env.JWT_SECRET);
  } catch (err) {
	return next(
  	new AppError("Invalid or expired token. Please log in again.", 401)
	);
  }
 
// 3. Confirm user still exists in database
  const currentUser = await User.findById(decoded._id);
  if (!currentUser) {
	return next(
  	new AppError("User linked to this token no longer exists.", 401)
	);
  }
 
  // 4. Attach user info to request
  req.user = currentUser;
  req.user = {
	id: currentUser.id,
	name: currentUser.name,
  };
 
  next();
});
 
module.exports = isAuthenticated;
```
Maintenant, allez dans votre fichier `userRouter.js` et ajoutez la route pour la fonction de vérification de compte :
```
const { verifyAccount} = require("../controller/authController");
const isAuthenticated = require("../middlewares/isAuthenticated");
router.post("/verify", isAuthenticated, verifyAccount);
```

Voici ce que font ces deux ensembles de code :

Lorsque l'utilisateur envoie une requête à la route `/verify`, le middleware `isAuthenticated` s'exécute en premier. Il vérifie si un jeton valide existe dans le cookie ou l'en-tête d'autorisation. Si aucun jeton n'est trouvé, il lance une erreur : `Vous n'êtes pas connecté. Veuillez vous connecter pour accéder à cette ressource.`

Si un jeton est trouvé, il vérifie le jeton et vérifie si l'utilisateur associé existe toujours. Si ce n'est pas le cas, une autre erreur est lancée : `"L'utilisateur lié à ce jeton n'existe plus."`

Si l'utilisateur existe et que le jeton est valide, ses détails sont attachés à la requête (`req.user`). La requête passe ensuite au contrôleur `verifyAccount`, qui gère la vérification de l'OTP.

Vous pouvez tester ce point de terminaison en utilisant Postman avec une requête POST à : [`http://localhost:8000/api/v1/users/verify`](http://localhost:8000/api/v1/users/verify%60)

![Vérifier le compte](https://cdn.hashnode.com/res/hashnode/image/upload/v1752703870392/a534d04f-7cb9-4f84-92e1-e9844cfa6921.png align="center")

L'image ci-dessus montre que la fonction de vérification du jeton fonctionne bien, et un code de statut de `200` est affiché.

### **Fonction de connexion**

Si vous êtes arrivé à ce stade, vous avez réussi à vous inscrire et à vérifier le compte d'un utilisateur.

Il est maintenant temps de créer la fonction de connexion, qui permet à un utilisateur vérifié d'accéder à son compte. Voici comment vous pouvez le faire :

Rendez-vous dans votre fichier `authController.js` et créez votre fonction de connexion en ajoutant ce qui suit :

```javascript
exports.login = catchAsync(async (req, res, next) => {
  const { email, password } = req.body;
 
  // 1. Validate email & password presence
  if (!email || !password) {
	return next(new AppError("Please provide email and password", 400));
  }
 
  // 2. Check if user exists and include password
  const user = await User.findOne({ email }).select("+password");
  if (!user || !(await user.correctPassword(password, user.password))) {
	return next(new AppError("Incorrect email or password", 401));
  }
 
  // 3. Create JWT token
  const token = signToken(user._id);
 
  // 4. Configure cookie options
  const cookieOptions = {
	expires: new Date(
  	Date.now() +
    	(parseInt(process.env.JWT_COOKIE_EXPIRES_IN, 10) || 90) 24 60 60 1000
	),
	httpOnly: true,
	// secure: process.env.NODE_ENV === "production",
	// sameSite: process.env.NODE_ENV === "production" ?
	//  "None" : "Lax",
 
	//set to false during or for local HTTP and cross-origin
	secure: false,
	sameSite: "Lax",
  };
 
  // 5. Send cookie
  res.cookie("token", token, cookieOptions);
 
});
```

`if (!email || !password) {}` vérifie si l'utilisateur a effectivement fourni à la fois un email et un mot de passe. Si ce n'est pas le cas, il retourne l'erreur : `Veuillez fournir un email et un mot de passe", 400`.

`const user = await User.findOne({ email }).select("+password");` recherche dans la base de données un utilisateur avec l'email fourni et inclut explicitement le champ du mot de passe, puisque celui-ci est normalement masqué par défaut dans le schéma.

`if (!user || !(await user.correctPassword())) {}` vérifie si l'utilisateur existe et si le mot de passe saisi correspond à celui stocké dans la base de données (après comparaison de hachage). Si l'un des deux est incorrect, il lance : `Email ou mot de passe incorrect`.

La ligne `signToken(user._id)` génère un JWT en utilisant l'ID unique de l'utilisateur. L'objet `cookieOptions` configure le comportement du cookie - il définit le cookie pour qu'il expire après un nombre spécifique de jours défini dans le fichier `.env`, le marque comme `httpOnly` pour empêcher l'accès JavaScript pour des raisons de sécurité, définit `secure` sur `false` puisque l'application est actuellement en développement, et utilise `sameSite: "Lax"` pour permettre les requêtes cross-origin pendant les tests locaux.

Enfin, `res.cookie(...)` envoie le jeton en tant que cookie attaché à la réponse HTTP, permettant au client de stocker le jeton à des fins d'authentification.

À partir du code ci-dessus, vous avez peut-être remarqué que le mot de passe stocké dans la base de données est haché pour des raisons de sécurité. Cela signifie qu'il semble complètement différent du mot de passe de l'utilisateur lors de la connexion. Ainsi, même si un utilisateur tape le bon mot de passe, il ne correspondra pas au hachage stocké directement par une simple comparaison.

Pour résoudre ce problème, vous devez comparer le mot de passe saisi avec celui haché en utilisant le package `bcryptjs`.

Rendez-vous dans votre fichier `userModel.js` et créez une méthode qui gère la comparaison des mots de passe. Cette méthode prendra le mot de passe en texte brut fourni par l'utilisateur et le comparera au mot de passe haché stocké dans la base de données.

```javascript
//userModel.js
//create a method responsible for comparing the password stored in the database
 
userSchema.methods.correctPassword = async function (password, userPassword) {
  return await bcrypt.compare(password, userPassword);
};
```

Cette méthode `correctPassword` utilise `bcrypt.compare()`, qui hache internement le mot de passe en clair et vérifie s'il correspond à la version hachée stockée. Cela garantit que la validation de la connexion fonctionne correctement et de manière sécurisée, même si le mot de passe réel n'est pas stocké en texte clair.

Ensuite, ajoutez la fonctionnalité de connexion au fichier `userRouter.js`.

```javascript
const {login} = require("../controller/authController");
const isAuthenticated = require("../middlewares/isAuthenticated");
 
router.post("/login", login);
```

Vous pouvez tester ce point de terminaison en utilisant Postman avec une requête `POST` à : [`http://localhost:8000/api/v1/users/login`](http://localhost:8000/api/v1/users/login%60)

### **Fonction de déconnexion**

À ce stade, vous pouvez implémenter la fonction de déconnexion pour mettre fin à la session d'un utilisateur de manière sécurisée. Pour ce faire, naviguez jusqu'à votre fichier `authController.js` et ajoutez la fonction suivante :

```javascript
//creating a log out function
exports.logout = catchAsync(async (req, res, next) => {
  res.cookie("token", "loggedout", {
	expires: new Date(0),
	httpOnly: true,
	secure: process.env.NODE_ENV === "production",
  });
 
  res.status(200).json({
	status: "success",
	message: "Logged out successfully",
  });
});
```

Cette fonction fonctionne en écrasant le cookie d'authentification nommé `token` avec la valeur `"loggedout"` et en définissant son heure d'expiration dans le passé en utilisant `new Date(0)`. Cela invalide efficacement le cookie et le supprime du navigateur.

Le drapeau `httpOnly: true` garantit que le cookie ne peut pas être accessible via JavaScript, ce qui le protège des attaques XSS, tandis que le drapeau `secure` garantit que le cookie n'est envoyé que via HTTPS dans un environnement de production. Une fois le cookie effacé, une réponse de succès est retournée avec le message "Déconnexion réussie" pour confirmer l'action.

Ensuite, ajoutez la fonctionnalité de `déconnexion` à votre route :

```javascript
const {logout} = require("../controller/authController");
const isAuthenticated = require("../middlewares/isAuthenticated");
 
router.post("/logout", logout);
```

Ensuite, rendez-vous sur Postman pour tester votre fonction de déconnexion et voir si elle fonctionne.

## **Configuration du Frontend**

Maintenant que votre backend est opérationnel, vous pouvez l'intégrer dans votre application frontend.

Tout d'abord, naviguez vers le répertoire frontend en utilisant la commande `cd Frontend`.

Créez un nouveau dossier dans le dossier `src` où vos fichiers liés à l'authentification résideront. Selon votre préférence ou la structure de votre application, vous pouvez le nommer quelque chose comme `auth` ou `pages`. Ensuite, créez un nouveau fichier appelé `NewUser.js`. Ce fichier gérera la fonctionnalité d'inscription des utilisateurs.

```javascript
import axios from 'axios';
import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { Loader } from 'lucide-react';
import { useDispatch } from 'react-redux';
import { setAuthUser, setPendingEmail } from '../../../../store/authSlice';
 
const API_URL = import.meta.env.VITE_API_URL;
 
function NewUser() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
 
  const [loading, setLoading] = useState(false);
 
  const [formData, setFormData] = useState({
	username: '',
	email: '',
	password: '',
	passwordConfirm: '',
  });
 
  const handleChange = (e) => {
	const { name, value } = e.target;
	setFormData((prev) => ({ ...prev, [name]: value }));
  };
 
  const submitHandler = async (e) => {
	e.preventDefault();
	setLoading(true);
	try {
  	const response = await axios.post(`${API_URL}/users/signup`, formData, {
    	withCredentials: true,
  	});
  	const user = response.data.data.user;
  	dispatch(setAuthUser(user));
  	dispatch(setPendingEmail(formData.email)); // Save email for OTP
  	navigate('/verifyAcct'); // Navigate to OTP verification page
	} catch (error) {
  	alert(error.response?.data?.message || 'Signup failed');
	} finally {
  	setLoading(false);
	}
  };
 
  return (
<div>
// visit the frontend Github repository to see the remaining code for the OTP Verification
 
https://github.com/Derekvibe/Telehealth_Frontend/blob/main/src/pages/Auth/Join/NewUser.jsx
	</div>
  );
}
 
export default NewUser;
```

Le code ci-dessus rend un formulaire d'inscription avec des champs pour `username`, `email`, `password` et `passwordConfirm`. Lorsque l'utilisateur soumet le formulaire, le frontend envoie une requête `POST` au point de terminaison `/users/signup` du backend en utilisant `Axios`. L'option `withCredentials: true` garantit que les cookies comme le `jeton d'authentification` sont correctement définis par le backend.

Si l'inscription est réussie, les données de l'utilisateur sont dispatchées dans Redux en utilisant `setAuthUser()`, et leur email est sauvegardé avec `setPendingEmail()` afin qu'il puisse être utilisé lors de la `vérification OTP`. Ensuite, l'utilisateur est redirigé vers la route `/verifyAcct`, où il peut entrer son `OTP`.

![Frontend-Sign-Up](https://cdn.hashnode.com/res/hashnode/image/upload/v1752704266192/0d1d5891-000a-48dc-a1d8-306a0103824a.png align="center")

### **Page de vérification OTP**

La page de vérification OTP est l'étape suivante du processus d'authentification de l'utilisateur. Une fois qu'un utilisateur s'est inscrit, il est redirigé pour entrer le code OTP à 4 chiffres envoyé à son email. Cela vérifie son compte avant de permettre l'accès à la connexion.

```javascript
import React, { useState, useRef, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useNavigate, Link } from 'react-router-dom';
import axios from 'axios';
import { clearPendingEmail } from '../../../../store/authSlice';
 
const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000/api'; // adjust as needed
  
function VerifyAcct() {
  const [code, setCode] = useState(['', '', '', '']);
  const [loading, setLoading] = useState(false);
  const [resendLoading, setResendLoading] = useState(false);
  const [timer, setTimer] = useState(60);
 
  const inputsRef = useRef([]);
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const email = useSelector((state) => state.auth.pendingEmail);
 
  useEffect(() => {
	let interval;
	if (timer > 0) {
  	interval = setInterval(() => setTimer((prev) => prev - 1), 1000);
	}
	return () => clearInterval(interval);
  }, [timer]);
 
  const handleChange = (value, index) => {
	if (!/^\d*$/.test(value)) return;
	const newCode = [...code];
// visit the frontend Github repository to see the remaining code for the OTP Verification
https://github.com/Derekvibe/Telehealth_Frontend/blob/main/src/pages/Auth/login/VerifyAcct.jsx
}
export default VerifyAcct;
```

Voici ce que fait le code :

L'OTP est stocké sous forme de tableau de 4 caractères (`[ ,  ,  ,  ]`). Chaque case n'accepte que des chiffres, et le focus se déplace automatiquement vers l'entrée suivante à mesure que l'utilisateur tape le chiffre. Le focus revient à la case d'entrée précédente si l'utilisateur appuie sur la touche de retour arrière sur une case vide.

Lorsque l'OTP a été ajouté et que le formulaire est soumis, le code à 4 chiffres est joint en une chaîne et une requête `HTTP POST` est faite au point de terminaison backend `/user/verify/` avec l'email stocké et l'OTP. Si la vérification est réussie, l'utilisateur est alerté et redirigé vers la page de connexion, et si ce n'est pas le cas, une erreur est affichée.

![Frontend-OTP](https://cdn.hashnode.com/res/hashnode/image/upload/v1752704448954/8ea46e32-c6d9-42e1-a016-f04b259eb0e7.png align="center")

### **Connexion**

Vous pouvez maintenant créer l'interface de connexion pour votre application. Tout d'abord, créez un fichier `Login.jsx` et entrez le code :

```javascript
//Login.Jsx
 
import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import axios from 'axios';
 
const API_URL = import.meta.env.VITE_API_URL || 'https://telehealth-backend-2m1f.onrender.com/api/v1';
 
function Join() {
  const [formData, setFormData] = useState({ email: '', password: '' });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const navigate = useNavigate();
 
  const handleChange = (e) => {
	setFormData({ ...formData, [e.target.name]: e.target.value });
  };
 
  const handleLogin = async (e) => {
	e.preventDefault();
	setLoading(true);
	setError('');
 
	try {
  	const res = await axios.post(`${API_URL}/users/login`, formData, {
    	withCredentials: true,
  	});
 
  	if (res.data.status === 'success') {
    	const { token, user, streamToken } = res.data;
 
    	// Save to localStorage
    	localStorage.setItem('authToken', token);
    	localStorage.setItem('user', JSON.stringify(user));
    	localStorage.setItem('streamToken', streamToken);
 
    	navigate('/dashboard');
  	}
	} catch (err) {
  	console.error(err);
  	setError(
    	err.response?.data?.message || 'Something went wrong. Please try again.'
  	);
	} finally {
  	setLoading(false);
	}
  };
 
  return (
<div>
{// visit the frontend Github repository to see the remaining code for the OTP Verification
https://github.com/Derekvibe/Telehealth_Frontend/blob/main/src/pages/Auth/login/Login.jsx
 </div>
);
}
```

Le composant `Export default Join;` permet à un utilisateur enregistré et vérifié de se connecter à votre application en utilisant son email et son mot de passe. Il gère la soumission du formulaire, communique avec le backend et stocke les données utilisateur de manière sécurisée si la connexion est réussie.

`handleChange()` met à jour le champ email ou mot de passe à mesure que l'utilisateur tape.

`handleLogin()` est déclenché lorsque le formulaire de connexion est soumis. Lorsque le bouton de connexion est déclenché, il envoie une requête `Post` à `/users/login` avec les données du formulaire, qui inclut `{withCredentials: true}` pour activer la gestion des cookies.

Si la connexion est réussie, il extrait le jeton JWT, les données utilisateur et le jeton Stream Chat de la réponse et les stocke dans le `localStorage` afin que l'utilisateur reste connecté entre les sessions. Ensuite, il redirige l'utilisateur vers la page du tableau de bord en utilisant `navigate(/dashboard)`.

![Frontend-Login](https://cdn.hashnode.com/res/hashnode/image/upload/v1752704515845/55c6e74a-a8bc-462a-b988-67b0e8df40ac.png align="center")

### **Configurer la route Frontend**

Tout comme vous avez configuré la route backend, vous devez faire de même pour le frontend.

Rendez-vous dans `App.jsx`. Avant d'ajouter la route, assurez-vous d'avoir installé le package `react-router-dom`. Si ce n'est pas le cas, exécutez cette commande dans le terminal frontend :

`npm install react-router-dom`

Ensuite, ajoutez la commande à votre fichier `App.jsx` :

```javascript
import React from 'react';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import HomeIndex from './pages/Home/HomeIndex';
import Hero from './pages/Home/Hero';
 
//Section d'authentification
import NewUser from './pages/Auth/Join/NewUser';
import Login from './pages/Auth/login/Login'
import VerifyAcct from './pages/Auth/login/VerifyAcct';
 
// Tableau de bord
import Dashboard from './pages/Dashboard/Dashboard';
import VideoStream from './components/VideoStream';
 
const router = createBrowserRouter([
  {
	path: '/',
	element: <HomeIndex />,
	children: [
  	{ index: true, element: <Hero /> }
	],
  },
 
  {
	path: 'signup',
	element: <NewUser />,
	children: [
  	{ index: true, element: <NewUser /> }
	],
  },
 
  {
	path: 'login',
	element: <Login />,
	children: [
  	{index:true, element:<Login />}
	]
  },
 
]);
{// visit the frontend Github repository to see the remaining code for the OTP Verification
https://github.com/Derekvibe/Telehealth_Frontend/blob/main/src/App.jsx}
 
function App() {
  return (
	<div className='border border-red-700 w-full min-w-[100vw] min-h-[100vh]'>
  	<RouterProvider router={router} />
	</div>
  );
}
 
export default App;
```

## **Intégration de Stream Chat et Video**

Avant de passer au tableau de bord, intégrons la fonctionnalité Stream [Chat](https://getstream.io/chat/) et [Video](https://getstream.io/video/) dans le projet.

Tout d'abord, [créez un compte Stream gratuit](https://getstream.io/try-for-free/), commencez un nouveau projet dans votre tableau de bord et obtenez votre `CLÉ API` et `SECRET API`.

```javascript
STREAM_API_KEY=your_app_key
STREAM_API_SECRET=your_api_secret
```

Regardez le guide de démarrage rapide de Stream [Chat React](https://youtu.be/kGKq4giL4ok?si=M_nkWAiq4IzGNYD_) pour voir comment vous pouvez le configurer.

Ensuite, stockez votre `CLÉ API` et `SECRET API` Stream dans votre `.env`.

### **Installer les packages Stream (Frontend)**

Maintenant, installez les packages Stream Chat et Video dans votre terminal.

```javascript
npm install stream-chat stream-chat-react
npm install @stream-io/video-react-sdk
npm install @stream-io/stream-chat-css
```

### **Gestionnaire de jetons Stream**

Tout d'abord, créez un nouveau fichier dans votre répertoire Src frontend et nommez-le. Dans cet exemple, il s'agit de `StreamContext.jsx`. Ce fichier configure un contexte pour récupérer et gérer le jeton Stream Chat lors de la connexion et inclut la fonctionnalité de déconnexion.

```javascript
import React, { createContext, useContext, useEffect, useState } from "react";
import axios from "axios";
 
const API_URL = import.meta.env.VITE_API_URL || 'https://telehealth-backend-2m1f.onrender.com/api/v1';
 
// 1. Create the context
const StreamContext = createContext();
 
// 2. Provider component
export const StreamProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [token, setToken] = useState(null);
 
  useEffect(() => {
	const fetchToken = async () => {
  	try {
    	const res = await axios.get(`${API_URL}/stream/get-token`, {
      	withCredentials: true,
    	});
 
    	if (res.data?.user && res.data?.token) {
      	setUser(res.data.user);
      	setToken(res.data.token);
      	console.log("Stream user/token:", res.data);
    	} else {
      	console.error("Token or user missing in response:", res.data);
    	}
  	} catch (error) {
    	console.error("Error fetching Stream token:", error);
  	}
	};
 
	fetchToken();
  }, []);
 
  //Log out Functionality
  const logout = async () => {
	try {
  	await axios.post(`${API_URL}/users/logout`, {},
    	{
      	withCredentials: true
    	});
     
  	// Clear localStorage
  	localStorage.removeItem('authToken');
  	localStorage.removeItem('user');
  	localStorage.removeItem('streamToken');
     
  	// Clear context
  	setUser(null);
  	setToken(null);
	} catch (error) {
  	console.error("Logout failed", error);
	}
  };
 
  // Expose Logout with capital L
  return (
	<StreamContext.Provider value={{ user, token, Logout:logout }}>
  	{children}
	</StreamContext.Provider>
  );
};
 
// 3. Custom hook for easy access
export const useStream = () => useContext(StreamContext);
```

Le code ci-dessus crée un StreamContext en utilisant l'API de contexte de React. Dans la section `useEffect`, il effectue une requête `GET` vers `/stream/get-token` pour récupérer l'utilisateur authentifié et son jeton Stream. Ensuite, il les stocke dans les états `user` et `token`. Il fournit également l'utilisateur/jeton via le contexte afin que tout composant qui en a besoin puisse l'utiliser.

Enfin, il ajoute une méthode `Logout` qui frappe le point de terminaison de déconnexion et efface toutes les données d'authentification stockées dans le `localStorage`.

Ensuite, ouvrez votre `main.jsx` et enveloppez toute votre application avec le `StreamProvider` afin que tous les composants enfants puissent accéder au contexte Stream.

```javascript
// main.jsx
import { createRoot } from 'react-dom/client';
import { StrictMode } from 'react';
import App from './App';
import { StreamProvider } from './components/StreamContext';
 
createRoot(document.getElementById('root')).render(
  <StrictMode>
	<StreamProvider>
  	<App />
	</StreamProvider>
  </StrictMode>
);
```

### **Configurer l'API Stream**

Après avoir créé avec succès le streamContent, l'étape suivante consiste à configurer l'API Stream. Ce sera le point de terminaison à partir duquel l'ID utilisateur et le jeton utilisateur Stream peuvent être générés et récupérés lors de la connexion.

Pour le configurer, naviguez vers votre répertoire backend en exécutant `cd Backend` dans votre terminal. Ensuite, installez le package Stream en utilisant la commande :

```javascript
npm install getstream
npm install stream-chat stream-chat-react
```

Ouvrez votre fichier `.env` et ajoutez votre `CLÉ API` et `SECRET API` Stream :

```javascript
STREAM_API_KEY=your_app_key
STREAM_API_SECRET=your_api_secret
```

Ensuite, ouvrez votre `authController.js` et créez votre logique Stream Chat :

```javascript
//Initialize the Stream Client
const {StreamChat} = require("stream-chat");
const streamClient = StreamChat.getInstance(
  process.env.STREAM_API_KEY,
  process.env.STREAM_API_SECRET
);
 
// Modifies the `createSendToken to include `streamToken`
const createSendToken = (user, statusCode, res, message) => {

const streamToken = streamClient.createToken(user._id.toString());
 
  //structure of the cookie response when sent to the user
  res.status(statusCode).json({
	status: "success",
	message,
	token,
	streamToken,
	data: {
  	user: {
    	id: user._id.toString(),
    	name: user.username,
  	},
	},
  });
};
 
//login functionality
exports.login = catchAsync(async (req, res, next) => {
 {..}
 
// Generate Stream token
  await streamClient.upsertUser({
	id: user._id.toString(),
	name: user.username,
  });
  const streamToken = streamClient.createToken(user._id.toString());
 
user.password = undefined;
 
  res.status(200).json({
	status: "success",
	message: "Login successful",
	token,
	user: {
  	id: user._id.toString(),
  	name: user.username,
	},
	streamToken,
  });
```

### `streamRoutes` **Endpoint**

Ensuite, créez un point de terminaison à partir duquel le jeton Stream peut être appelé. Pour ce faire, allez dans votre dossier routes et créez un nouveau fichier appelé `streamRoutes.js`. Dans `streamRoutes.js`, ajoutez la commande :

```javascript
const express = require("express");
const { StreamChat } = require("stream-chat");

const protect = require("../middlewares/protect");

const router = express.Router();

const apiKey = process.env.STREAM_API_KEY;
const apiSecret = process.env.STREAM_API_SECRET;

if (!apiKey || !apiSecret) {
  throw new Error(
    "Missing Stream credentials. Check your environment variables."
  );
}

const streamClient = StreamChat.getInstance(apiKey, apiSecret);

router.get("/get-token", protect, async (req, res) => {
  try {
    const { id, username } = req.user || {};
    console.log(req.user.id, "User");
    // TRY LOGGING THE ID AND NAME FROM YOUR REQUEST FIRST

    if (!id || !username) {
      return res.status(400).json({ error: "Invalid user data" });
    }

    // const userId = _id.toString();
    const user = { id, username };

    // Ensure user exists in Stream backend
    await streamClient.upsertUser(user);

    // Add user to my_general_chat channel
    const channel = streamClient.channel("messaging", "my_general_chat");
    await channel.addMembers([id]);


    // Generate token
    const token = streamClient.createToken(id);
    res.status(200).json({ token, user });
  } catch (error) {
    console.error("Stream token generation error:", error);
    res.status(500).json({ error: "Failed to generate Stream token" });
  }
});

/**
 * @route   POST /api/stream/token
 * @desc    Generate a Stream token for any userId from request body (no auth)
 * @access  Public
 */
router.post("/token", async (req, res) => {
  try {
    const { userId, name } = req.body;

    if (!userId) {
      return res.status(400).json({ error: "userId is required" });
    }

    const userName = name || "Anonymous";
    const user = { id: userId, name: userName };

    await streamClient.upsertUser(user);

    // Add user to my_general_chat channel
    const channel = streamClient.channel("messaging", "my_general_chat");
    await channel.addMembers([userId]);

    
    const token = streamClient.createToken(userId);

    res.status(200).json({
      token,
      user: {
        id: userId,
        name: name,
        role: "admin",
        image: `https://getstream.io/random_png/?name=${name}`,
      },
    });
  } catch (error) {
    console.error("Public token generation error:", error);
    res.status(500).json({ error: "Failed to generate token" });
  }
});

module.exports = router;
```

## **Point de terminaison de déconnexion de l'utilisateur**

Rendez-vous dans votre `authController.js` et créez une fonctionnalité qui gère la déconnexion de l'utilisateur :

```javascript
exports.logout = catchAsync(async (req, res, next) => {
  res.cookie("token", "loggedout", {
	expires: new Date(0),
	httpOnly: true,
	secure: process.env.NODE_ENV === "production",
  });
 
  res.status(200).json({
	status: "success",
	message: "Logged out successfully",
  });
});
```

Ensuite, enregistrez votre route de déconnexion dans votre `userRouters.js` :

```javascript
const express = require("express");
const {logout}= require("../controller/authController");
const isAuthenticated = require("../middlewares/isAuthenticated");
 
 
router.post("/logout", isAuthenticated, logout);
 
module.exports = router;
```

## Fonction de chat et vidéo (Frontend)

Après avoir configuré votre API Stream backend, la dernière tâche consiste à configurer le chat et la vidéo dans votre application frontend.

### `Dashboard.jsx`

Créez un nouveau fichier `Dashboard.jsx` dans votre répertoire frontend. C'est ici que vous configurerez votre fonction Stream et vidéo.

```javascript
import React, { useState, useEffect } from "react";
import axios from "axios";
import {
  Chat,
  Channel,
  ChannelHeader,
  MessageInput,
  MessageList,
  Thread,
  Window,
  useCreateChatClient,
} from "stream-chat-react";
import "stream-chat-react/dist/css/v2/index.css";
import { useStream } from "../../components/StreamContext";
import VideoStream from "../../components/VideoStream";
import { useNavigate } from "react-router-dom";
 
 
 
const apiKey = import.meta.env.VITE_STREAM_API_KEY;
 
const API_URL = import.meta.env.VITE_API_URL || 'https://telehealth-backend-2m1f.onrender.com/api/v1';
 
function App() {
  const [channel, setChannel] = useState(null);
  const [clientReady, setClientReady] = useState(false);
  const navigate = useNavigate();
 
  // const ChatComponent = () => {
	const { user, token, Logout } = useStream();
 
	// Always call the hook
	const chatClient = useCreateChatClient({
  	apiKey,
  	tokenOrProvider: token,
  	userData: user?.id ? { id: user.id } : undefined,
	});
 
  // Debug: See when user/token is ready
  useEffect(() => {
	console.log("Stream user:", user);
	console.log("Stream token:", token);
  }, [user, token]);
 
	// Connect user to Stream
	useEffect(() => {
  	const connectUser = async () => {
    	if (!chatClient || !user || !token || !user?.id) {
          console.warn("Missing chat setup data:", { chatClient, token, user });
      	return;
    	}
     
 
    	try {
      	await chatClient.connectUser(
        	{
          	id: user.id,
          	name: user.name || "Anonymous",
          	image:
            	user.image ||
            	`https://getstream.io/random_png/?name=${user.name || "user"}`,
        	},
        	token
      	);
 
      	const newChannel = chatClient.channel("messaging", "my_general_chat", {
        	name: "General Chat",
        	members: [user.id],
      	});
 
      	await newChannel.watch();
      	setChannel(newChannel);
      	setClientReady(true);
    	} catch (err) {
      	console.error("Error connecting user:", err);
    	}
  	};
 
  	connectUser();
	}, [chatClient, user, token]);
 
	const handleVideoCallClick = () => {
  	navigate("/videoCall");
  };
 
  const handleLogout = async () => {
	await Logout();
	navigate("/login");
  }
 
  if (!user || !token) {
	return <div className="text-red-600">User or token not ready.</div>;
  }
 
  if (!clientReady || !channel) return <div>Loading chat...</div>;
 
 
  return (
{ checkout the github repo}
        	<ChannelHeader />
        	<MessageList />
        	<MessageInput />
      	</Window>
      	<Thread />
    	</Channel>
  	</Chat>
     
    
  	</div>
     
	);
  }
 
export default App;
```

### **Configuration de la vidéo**

Vous allez maintenant configurer la fonction vidéo pour votre frontend. Pour ce faire, créez un nouveau fichier `VideoStream.jsx` et ajoutez la commande :

```javascript
import React, { useEffect, useState } from "react";
import { StreamVideoClient } from "@stream-io/video-client";
import { StreamVideo, StreamCall } from "@stream-io/video-react-sdk";
import { useNavigate } from "react-router-dom";
 
 
import { useStream } from "./StreamContext";
import { MyUILayout } from "./MyUILayout";
 
 
const apiKey = import.meta.env.VITE_STREAM_API_KEY;
 
function VideoStream() {
 
  const [client, setClient] = useState(null);
	const [call, setCall] = useState(null);
  const { user, token } = useStream();
  const navigate = useNavigate();
 
  useEffect(() => {
     
	let clientInstance;
	let callInstance;
 
 
	const setup = async () => {
  	if (!apiKey || !user || !token) return;
 
  	clientInstance = new StreamVideoClient({ apiKey, user, token });
       
  	callInstance = clientInstance.call("default", user.id); // Use user.id as callId
 
 
  	await callInstance.join({ create: true });
 
      setClient(clientInstance);
  	setCall(callInstance);
	};
 
	setup();
   
	return () => {
  	if (callInstance) callInstance.leave();
  	if (clientInstance) clientInstance.disconnectUser();
 
	};
  }, [user, token]);
 
  const handleLeaveCall = async () => {
	if (call) await call.leave();
	if (client) await client.disconnectUser();
 
	setCall(null);
	setClient(null);
 
	navigate("/dashboard"); // or any other route
  };
 
  if (!apiKey) return <div>Missing Stream API Key</div>;
 
  if (!client || !call)
	return (
  <div className="flex items-center justify-center h-screen text-xl font-semibold">
	Connecting to the video call...
  </div>
	);
 
  return (
	<div className="relative h-screen w-full p-2 sm:p-4 bg-gray-50">
  	<StreamVideo client={client}>
    	<StreamCall call={call}>
      	<MyUILayout />
    	</StreamCall>
  	</StreamVideo>
 
  	<button
    	onClick={handleLeaveCall}
    	className="absolute top-2 right-2 sm:top-4 sm:right-4 bg-red-600 text-white text-sm sm:text-base px-3 sm:px-4 py-1.5 sm:py-2 rounded-lg shadow hover:bg-red-700 transition"
  	>
    	Leave Call
  	</button>
	</div>
	);
  }
 
export default VideoStream;
 
```

```javascript
//MYUILayout.jsx
import React from 'react';
import {
  useCall,
  useCallStateHooks,
  CallingState,
} from '@stream-io/video-react-sdk';
 
export function MyUILayout() {
  const call = useCall();
  const { useCallCallingState, useParticipantCount } = useCallStateHooks();
  const callingState = useCallCallingState();
  const participantCount = useParticipantCount();
 
  if (callingState !== CallingState.JOINED) {
	return <div>Joining call...</div>;
  }
 
  return (
	<div style={{ padding: '1rem', fontSize: '1.2rem' }}>
  	 Call "<strong>{call?.id}</strong>" has <strong>{participantCount}</strong> participants.
	</div>
  );
}
```

## Démonstration du projet

![Démonstration finale du projet de télémédecine](https://cdn.hashnode.com/res/hashnode/image/upload/v1752705861841/85b6d6b3-0f5e-402f-b8b5-8ab51d820403.gif align="center")

Félicitations ! Vous avez réussi à intégrer les fonctions de chat et de vidéo de Stream dans votre application.

## **Conclusion**

Et voilà !

Vous avez [construit une application de télémédecine](https://getstream.io/blog/telemedicine-app-development/) avec une vidéo sécurisée, un chat en temps réel et une authentification des utilisateurs - le tout alimenté par les SDK Chat et Video de Stream.

Cette base vous donne la flexibilité de vous développer davantage avec des fonctionnalités comme la planification des rendez-vous, l'historique des patients ou le partage de fichiers conforme à la HIPPA.

Vous pouvez trouver les applications [frontend](https://github.com/Derekvibe/Telehealth_Backend) et [backend](https://github.com/Derekvibe/Telehealth_Frontend) sur GitHub. L'application frontend est hébergée en utilisant le service d'hébergement Vercel, et le backend est hébergé sur Render.

Consultez le [dépôt de l'application](https://telehealth-frontend.vercel.app/).

Bon codage ! 