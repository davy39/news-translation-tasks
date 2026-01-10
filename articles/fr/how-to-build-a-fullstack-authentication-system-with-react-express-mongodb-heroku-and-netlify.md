---
title: Comment créer une application d'authentification Full-Stack avec React, Express,
  MongoDB, Heroku et Netlify
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-07-05T13:50:44.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-fullstack-authentication-system-with-react-express-mongodb-heroku-and-netlify
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/pexels-sora-shimazaki-5935794--1-.jpg
tags:
- name: authentication
  slug: authentication
- name: full stack
  slug: full-stack
- name: React
  slug: react
seo_title: Comment créer une application d'authentification Full-Stack avec React,
  Express, MongoDB, Heroku et Netlify
seo_desc: 'By Njoku Samson Ebere

  It''s almost impossible to build an application without registration and login functionalities.
  But this can be a bit tricky for beginners.

  In this article, I will guide you through creating a full-stack authentication applicatio...'
---

Par Njoku Samson Ebere

Il est presque impossible de créer une application sans fonctionnalités d'inscription et de connexion. Mais cela peut être un peu délicat pour les débutants.

Dans cet article, je vais vous guider à travers la création d'une application d'authentification full-stack. Vous commencerez par le backend qui sera construit avec Express et hébergé sur [Heroku](https://www.heroku.com/). Ensuite, vous terminerez avec le frontend qui sera créé avec React et hébergé sur [Netlify](https://www.netlify.com/).

À la fin de ce tutoriel, vous aurez appris à utiliser des outils tels que Nodejs, Express, React, MongoDB, Heroku, Netlify, bcrypt, jsonwebtoken et React-Bootstrap.

## Table des matières

1. [Section 1 : Comment construire le Backend](#heading-section-1-comment-construire-le-backend)

* [Comment configurer la base de données](#heading-comment-configurer-la-base-de-donnees)
* [Comment connecter Node.js à MongoDB](#heading-comment-connecter-nodejs-a-mongodb)
* [Comment créer le modèle Utilisateurs](#heading-comment-creer-le-modele-utilisateurs)
* [Comment créer le point de terminaison d'inscription](#heading-comment-creer-le-point-de-terminaison-dinscription)
* [Comment créer le point de terminaison de connexion](#heading-comment-creer-le-point-de-terminaison-de-connexion)
* [Comment protéger les points de terminaison](#heading-comment-proteger-les-points-de-terminaison)
* [Comment héberger le Backend](#heading-comment-heberger-le-backend)
* [Faisons un bilan](#heading-faisons-un-bilan)

2. [Section 2 : Comment construire le Frontend](#heading-section-2-comment-construire-le-frontend)

* [Comment construire l'interface utilisateur](#heading-comment-construire-linterface-utilisateur)
* [Comment inscrire un utilisateur](#heading-comment-inscrire-un-utilisateur)
* [Comment connecter un utilisateur](#heading-comment-connecter-un-utilisateur)
* [Comment protéger les routes](#heading-comment-proteger-les-routes)
* [Comment faire des appels API en utilisant le hook useEffect](#heading-comment-faire-des-appels-api-en-utilisant-le-hook-useeffect)
* [Comment construire la fonction de déconnexion](#heading-comment-construire-la-fonction-de-deconnexion)
* [Comment héberger le Frontend](#heading-comment-heberger-le-frontend)
* [Faisons un bilan](#heading-faisons-un-bilan)

3. [Toutes les ressources et aperçus](#heading-toutes-les-ressources-et-aperçus)

4. [Conclusion](#heading-conclusion)

## Prérequis

Ce tutoriel suppose que vous connaissez déjà les bases de :

* Nodejs et Express. Consultez ce [tutoriel](https://www.freecodecamp.org/news/build-a-secure-server-with-node-and-express/) sinon.
* [Github](https://github.com/).
* [React](https://reactjs.org/).

## Code de départ

* Veuillez cloner le code de départ [ici](https://github.com/EBEREGIT/auth-backend/tree/starter-code).
* Dans le répertoire du projet, exécutez `npm install` pour installer les dépendances
* Exécutez `nodemon index` pour servir le projet sur le port 3000.
* Vérifiez `http://localhost:3000/` sur votre navigateur pour confirmer

```cmd

$ git clone -b starter-code https://github.com/EBEREGIT/auth-backend


```

# Section 1 : Comment construire le Backend

Le backend représente toutes les fonctionnalités que les utilisateurs ne voient pas. Cela inclut la conception de la base de données et les points de terminaison de l'API.

Cette section vous guidera étape par étape sur la façon de construire le backend d'un système d'authentification.

Nous commencerons par configurer une base de données en utilisant MongoDB, puis nous créerons des points de terminaison (**login** et **register**), et nous terminerons en hébergeant les points de terminaison sur Heroku.

Commençons !

## Comment configurer la base de données

Cette partie couvrira la configuration de la base de données en utilisant [mongoDB atlas](https://www.mongodb.com/cloud/atlas).

Vous pouvez créer un compte gratuit [ici](https://account.mongodb.com/account/register).

### Comment créer un nouvel utilisateur de base de données

Sur votre tableau de bord, cliquez sur le lien `Database Access` à gauche (cela vous invitera à ajouter un nouvel utilisateur de base de données).

![Photo d'accès à la base de données](https://dev-to-uploads.s3.amazonaws.com/i/j3jakvaahhes3hwifuyw.JPG)
_tableau de bord de l'utilisateur_

Cliquez sur le bouton "Add New Database User" et une boîte de dialogue `Add New Database User` s'ouvrira.

![Boîte de dialogue Add New Database User](https://dev-to-uploads.s3.amazonaws.com/i/3y63tqp3ama824jyjagg.JPG)
_boîte de dialogue `Add New Database User`_

Sélectionnez `Password` comme méthode d'authentification, et tapez un nom d'utilisateur de votre choix.

Ensuite, tapez un mot de passe ou générez un mot de passe sécurisé automatiquement. Je recommande de générer automatiquement un mot de passe et de le stocker quelque part. Vous en aurez besoin bientôt.

Cliquez sur `Add User` pour terminer le processus.

![Utilisateur créé](https://dev-to-uploads.s3.amazonaws.com/i/iv92tdfrqegxgnj1lwyz.JPG)

### Comment créer un cluster

Dans le menu latéral, cliquez sur `clusters`. Cela vous amène à la page du cluster avec un bouton : `Build a Cluster`.

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/i/s2mtfzhyrzkz79omckha.JPG)

Cliquez sur le bouton, et une autre page apparaîtra.

Choisissez le `free cluster`. La page des paramètres s'ouvrira. Vous n'apporterez aucune modification à cette page.

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/i/zmitdioyw4io3vuuv7u2.JPG)

Cliquez sur `Create Cluster`. Attendez un moment que le cluster soit créé complètement. Une fois terminé, votre écran devrait ressembler à ceci :

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/i/whgefzv95dnmy2qo91xn.JPG)

### Comment connecter un utilisateur au cluster

Cliquez sur le bouton `connect` :

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/i/n92cm0ztfc55i66vwx8t.JPG)

Dans la modale `Connect to Cluster0` qui apparaît, sélectionnez `Connect from Anywhere` et mettez à jour les paramètres.

Cliquez sur le bouton `Choose a connection method` :

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/i/y42t9m2kzmkp3oon0bb7.JPG)

Cliquez sur `Connect Your Application`. Dans la page qui s'ouvre, assurez-vous que le `DRIVER` est `nodejs` et que la `VERSION` est `3.6 ou ultérieure`.

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/i/9yrg7nknor2xhogwldoe.JPG)

Copiez la chaîne de connexion et stockez-la quelque part. Vous en aurez besoin bientôt.

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/i/jj816egjtx7jjsiixs1a.JPG)

Elle devrait être similaire à :

```javascript

mongodb+srv://plenty:<password>@cluster0.z3yuu.mongodb.net/<dbname>?retryWrites=true&w=majority


```

Fermez la boîte de dialogue.

### Comment créer une collection (Tables)

De retour sur la page Cluster, cliquez sur `COLLECTIONS`.

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/i/gtk0xqwbcf7xgdef6d9p.JPG)

Vous devriez être sur la page ci-dessous. Cliquez sur le bouton `Add My Own Data` :

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/i/b3itcf0383pvcuk7f8g7.JPG)

Dans la boîte de dialogue qui apparaît, entrez un `nom de base de données` et un `nom de collection`. Mon nom de base de données est `authDB` et mon nom de collection est `users`.

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/i/2bb2p5fm1kz3muma35ow.JPG)

Cliquez sur le bouton `Create`.

Félicitations pour la création de cette base de données et de cette collection (table) !

## Comment connecter Node.js à MongoDB

Revenons au code de départ.

Vous vous souvenez toujours du nom de la base de données, de la chaîne de connexion et du mot de passe que vous avez générés ? Vous allez les utiliser dans un instant.

Remplacez `<password>` et `<dbname>` par le mot de passe que vous avez généré et le nom de la base de données que vous avez créée comme suit :

```javascript

mongodb+srv://plenty:RvUsNHBHpETniC3l@cluster0.z3yuu.mongodb.net/authDB?retryWrites=true&w=majority


```

Créez un fichier dans le dossier racine et nommez-le `.env`.

Créez une variable `DB_URL` et attribuez-lui la chaîne de connexion :

```javascript

DB_URL=mongodb+srv://plenty:RvUsNHBHpETniC3l@cluster0.z3yuu.mongodb.net/authDB?retryWrites=true&w=majority


```

Créez un dossier et nommez-le `db`.

Créez un nouveau fichier et nommez-le `dbConnect.js`.

Ensuite, nous devons installer [mongoose](https://www.npmjs.com/package/mongoose) :

```javascript

npm i mongoose -s


```

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/i/lsyp8s6sk30ke7g8x0ym.JPG)

Dans le fichier `dbConnect`, requérez `mongoose` et `env` avec le code suivant :

```javascript

// imports externes
const mongoose = require("mongoose");
require('dotenv').config()


```

Créez et exportez une fonction pour héberger la connexion :

```javascript

async function dbConnect() {

}

module.exports = dbConnect;


```

Dans la fonction, la connexion à la base de données a été créée en utilisant la chaîne de connexion du fichier `.evn` :

```javascript

// utiliser mongoose pour connecter cette application à notre base de données sur mongoDB en utilisant le DB_URL (chaîne de connexion)
  mongoose
    .connect(
        process.env.DB_URL,
      {
        //   ces sont des options pour s'assurer que la connexion est faite correctement
        useNewUrlParser: true,
        useUnifiedTopology: true,
        useCreateIndex: true,
      }
    )


```

Utilisez un bloc `then...catch...` pour montrer si la connexion a réussi ou non :

```javascript

.then(() => {
      console.log("Connexion réussie à MongoDB Atlas !");
    })
    .catch((error) => {
      console.log("Impossible de se connecter à MongoDB Atlas !");
      console.error(error);
    });


```

Le fichier `dbConnect` devrait ressembler à ceci :

```javascript

// imports externes
const mongoose = require("mongoose");
require('dotenv').config()

async function dbConnect() {
  // utiliser mongoose pour connecter cette application à notre base de données sur mongoDB en utilisant le DB_URL (chaîne de connexion)
  mongoose
    .connect(
        process.env.DB_URL,
      {
        //   ces sont des options pour s'assurer que la connexion est faite correctement
        useNewUrlParser: true,
        useUnifiedTopology: true,
        useCreateIndex: true,
      }
    )
    .then(() => {
      console.log("Connexion réussie à MongoDB Atlas !");
    })
    .catch((error) => {
      console.log("Impossible de se connecter à MongoDB Atlas !");
      console.error(error);
    });
}

module.exports = dbConnect;


```

Dans le fichier `app.js`, requérez la fonction `dbConnect` et exécutez-la :

```javascript

// requérir la connexion à la base de données 
const dbConnect = require("./db/dbConnect");

// exécuter la connexion à la base de données 
dbConnect();


```

Vérifiez votre terminal. Si vous n'avez pas manqué d'étapes, vous devriez avoir `"Connexion réussie à MongoDB Atlas!"` imprimé :

![Terminal montrant "Connexion réussie à MongoDB Atlas!"](https://dev-to-uploads.s3.amazonaws.com/i/u36z3xyjtr6mpgyq6gty.JPG)

## Comment créer le modèle Utilisateurs

Le modèle utilisateur indique à la base de données comment stocker les données qu'un utilisateur transmet. Les étapes suivantes vous montreront comment créer un modèle pour les utilisateurs :

Créez un fichier dans le dossier `db` et nommez-le `userModel`.

Requérez `mongoose` dans le fichier `userModel` :

```javascript

const mongoose = require("mongoose");


```

Créez une constante (`UserSchema`) et attribuez-lui le schéma mongoose :

```javascript

const UserSchema = new mongoose.Schema({})


```

Dans le schéma, entrez les 2 champs nécessaires (`email` et `password`) et attribuez-leur un objet vide :

```javascript
const UserSchema = new mongoose.Schema({
  email: {},

  password: {},
})


```

Spécifiez comment les champs doivent fonctionner en ajoutant quelques [options mongoose](https://mongoosejs.com/docs/guide.html) :

```javascript

email: {
    type: String,
    required: [true, "Veuillez fournir un email !"],
    unique: [true, "Email Existant"],
  },

  password: {
    type: String,
    required: [true, "Veuillez fournir un mot de passe !"],
    unique: false,
  },


```

Enfin, exportez `UserSchema` avec le code suivant :

```javascript

module.exports = mongoose.model.Users || mongoose.model("Users", UserSchema);


```

Le code ci-dessus dit : _"créez une table ou une collection d'utilisateurs s'il n'y a pas déjà de table avec ce nom"._

Vous avez terminé le modèle pour l'utilisateur. La collection `user` est maintenant prête à recevoir les données qui doivent lui être transmises.

## Comment créer le point de terminaison d'inscription

Dans cette section, vous allez créer un point de terminaison que vous utiliserez pour ajouter un utilisateur à la base de données. Suivez ces étapes :

Installez [bcrypt](https://www.npmjs.com/package/bcrypt). Nous l'utiliserons pour hacher le mot de passe reçu des utilisateurs.

```javascript

npm install --save bcrypt


```

Requérez `bcrypt` en haut du fichier `app.js` :

```javascript

const bcrypt = require("bcrypt");


```

Requérez le `userModel` juste en dessous de la ligne où vous avez requis la base de données :

```javascript

const User = require("./db/userModel");


```

Créez un point de terminaison `register` juste avant la ligne `module.exports = app;` :

```javascript

app.post("/register", (request, response) => {

});


```

Hachez le mot de passe avant de sauvegarder l'`email` et le `password` dans la base de données avec le code suivant :

```javascript

bcrypt.hash(request.body.password, 10)
  .then()
  .catch()


```

Le code ci-dessus demande à `bcrypt` de hacher le `password` reçu du `request body` 10 fois ou 10 tours de sel.

Si le hachage est réussi, continuez dans le bloc `then` et sauvegardez l'`email` et le `hashed password` dans la base de données, sinon retournez une erreur dans le bloc `catch`.

Dans le bloc `catch`, retournez une erreur :

```javascript

   .catch((e) => {
      response.status(500).send({
        message: "Le mot de passe n'a pas été haché avec succès",
        e,
      });
    });


```

Dans le bloc `then`, sauvegardez les données que vous avez maintenant. Créez une nouvelle instance du `userModel` et collectez les données mises à jour :

```javascript

.then((hashedPassword) => {
      const user = new User({
        email: request.body.email,
        password: hashedPassword,
      });
});


```

Sauvegardez les données avec :

```javascript

user.save()


```

Et c'est tout. Si vous vous arrêtez à ce stade, tout est bon. Cela sauvegarde mais vous n'obtenez aucun retour.

Pour obtenir un retour, utilisez un bloc `then...catch...` :

```javascript

     user.save().then((result) => {
        response.status(201).send({
          message: "Utilisateur créé avec succès",
          result,
        });
      })
      .catch((error) => {
        response.status(500).send({
          message: "Erreur lors de la création de l'utilisateur",
          error,
        });
      });


```

Enfin, le point de terminaison `register` ressemble à ceci :

```javascript

// point de terminaison d'inscription
app.post("/register", (request, response) => {
  // hacher le mot de passe
  bcrypt
    .hash(request.body.password, 10)
    .then((hashedPassword) => {
      // créer une nouvelle instance d'utilisateur et collecter les données
      const user = new User({
        email: request.body.email,
        password: hashedPassword,
      });

      // sauvegarder le nouvel utilisateur
      user
        .save()
        // retourner un succès si le nouvel utilisateur est ajouté à la base de données avec succès
        .then((result) => {
          response.status(201).send({
            message: "Utilisateur créé avec succès",
            result,
          });
        })
        // capturer l'erreur si le nouvel utilisateur n'a pas été ajouté avec succès à la base de données
        .catch((error) => {
          response.status(500).send({
            message: "Erreur lors de la création de l'utilisateur",
            error,
          });
        });
    })
    // capturer l'erreur si le hachage du mot de passe n'est pas réussi
    .catch((e) => {
      response.status(500).send({
        message: "Le mot de passe n'a pas été haché avec succès",
        e,
      });
    });
});


```

### Comment tester le point de terminaison d'inscription

Démarrez le serveur dans le terminal si vous ne l'avez pas encore fait :

![Démarrez votre terminal](https://dev-to-uploads.s3.amazonaws.com/i/oo9g5y5j9tiv1t8cn91y.JPG)

Allez sur Postman et testez :

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/i/oe3ay8c5gz2c24cpw1cr.JPG)

Allez sur votre MongoDB Atlas.

Cliquez sur `Collections` et vous devriez voir les données que vous venez d'ajouter :

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/i/4znw7bw783l1hx1i3rms.JPG)



## Comment créer le point de terminaison de connexion

Cette partie couvrira la connexion avec [`jasonwebtoken (JWT)`](https://www.npmjs.com/package/jsonwebtoken). À la fin, vous aurez appris à vérifier les utilisateurs et à faire correspondre le `mot de passe haché` au `mot de passe en texte brut`.

Voici les étapes :

Tout d'abord, vous devez installer JWT :

```javascript

npm i jsonwebtoken -s


```

Importez `JWT` juste en dessous de la ligne `const bcrypt = require("bcrypt");` en haut du fichier `app.js` :

```javascript

const jwt = require("jsonwebtoken");


```

Juste en dessous du point de terminaison `register`, entrez la fonction suivante :

```javascript

app.post("/login", (request, response) => {
  
})


```

Vérifiez si l'email que l'utilisateur entre lors de la connexion existe :

```javascript

  User.findOne({ email: request.body.email })


```

Utilisez un bloc `then...catch...` pour vérifier si la recherche d'email ci-dessus a réussi ou non. Si elle n'aboutit pas, capturez cela dans le bloc `catch` :

```javascript

User.findOne({ email: request.body.email })
    .then()
    .catch((e) => {
      response.status(404).send({
        message: "Email non trouvé",
        e,
      });
    });


```

Si la recherche réussit, comparez le mot de passe entré avec le mot de passe haché dans la base de données. Faites cela dans le bloc `then...` :

```javascript

   .then((user)=>{
      bcrypt.compare(request.body.password, user.password)
   })


```

Utilisez à nouveau un bloc `then...catch...` pour vérifier si la comparaison est réussie ou non. Si la comparaison n'aboutit pas, retournez un message d'erreur dans le bloc `catch` :

```javascript

    .then((user)=>{
      bcrypt.compare(request.body.password, user.password)
      .then()
      .catch((error) => {
        response.status(400).send({
          message: "Les mots de passe ne correspondent pas",
          error,
        });
      })
    })


```

Vérifiez si le mot de passe est correct dans le bloc `then` :

```javascript

      .then((passwordCheck) => {

          // vérifier si les mots de passe correspondent
          if(!passwordCheck) {
            return response.status(400).send({
              message: "Les mots de passe ne correspondent pas",
              error,
            });
          }
        })


```

Si le mot de passe correspond, créez un jeton aléatoire avec la fonction `jwt.sign()`. Elle prend 3 paramètres : `jwt.sign(payload, secretOrPrivateKey, [options, callback])`. Vous pouvez en lire plus [ici](https://www.npmjs.com/package/jsonwebtoken#usage).

```javascript

bcrypt.compare(request.body.password, user.password)
      .then((passwordCheck) => {

          // vérifier si les mots de passe correspondent
          if(!passwordCheck) {
            return response.status(400).send({
              message: "Les mots de passe ne correspondent pas",
              error,
            });
          }

        //   créer un jeton JWT
        const token = jwt.sign(
          {
            userId: user._id,
            userEmail: user.email,
          },
          "RANDOM-TOKEN",
          { expiresIn: "24h" }
        );
      })


```

Enfin, retournez un message de succès avec le jeton créé :

```javascript

.then((user)=>{
      bcrypt.compare(request.body.password, user.password)
      .then((passwordCheck) => {

          // vérifier si les mots de passe correspondent
          if(!passwordCheck) {
            return response.status(400).send({
              message: "Les mots de passe ne correspondent pas",
              error,
            });
          }

        //   créer un jeton JWT
        const token = jwt.sign(
          {
            userId: user._id,
            userEmail: user.email,
          },
          "RANDOM-TOKEN",
          { expiresIn: "24h" }
        );

         //   retourner une réponse de succès
         response.status(200).send({
          message: "Connexion réussie",
          email: user.email,
          token,
        });
      })


```

Le point de terminaison de connexion ressemble maintenant à ceci :

```javascript

// point de terminaison de connexion
app.post("/login", (request, response) => {
  // vérifier si l'email existe
  User.findOne({ email: request.body.email })

    // si l'email existe
    .then((user) => {
      // comparer le mot de passe entré et le mot de passe haché trouvé
      bcrypt
        .compare(request.body.password, user.password)

        // si les mots de passe correspondent
        .then((passwordCheck) => {

          // vérifier si les mots de passe correspondent
          if(!passwordCheck) {
            return response.status(400).send({
              message: "Les mots de passe ne correspondent pas",
              error,
            });
          }

          //   créer un jeton JWT
          const token = jwt.sign(
            {
              userId: user._id,
              userEmail: user.email,
            },
            "RANDOM-TOKEN",
            { expiresIn: "24h" }
          );

          //   retourner une réponse de succès
          response.status(200).send({
            message: "Connexion réussie",
            email: user.email,
            token,
          });
        })
        // capturer l'erreur si les mots de passe ne correspondent pas
        .catch((error) => {
          response.status(400).send({
            message: "Les mots de passe ne correspondent pas",
            error,
          });
        });
    })
    // capturer l'erreur si l'email n'existe pas
    .catch((e) => {
      response.status(404).send({
        message: "Email non trouvé",
        e,
      });
    });
});



```

### Comment tester le point de terminaison de connexion

Essayons de nous connecter avec les identifiants qui ont été enregistrés dans la dernière partie. Voyez le jeton aléatoire généré lors d'une connexion réussie :

![Image de succès de connexion](https://dev-to-uploads.s3.amazonaws.com/i/krz1ikslqsilk1d8lvpr.JPG)

Si l'`email` est incorrect ou n'existe pas, voici ce que vous obtenez :

![Email incorrect ou n'existe pas](https://dev-to-uploads.s3.amazonaws.com/i/xy9ka8we8n2nvdaeain4.JPG)

Si le `mot de passe` est incorrect, voici ce que vous voyez :

![Mot de passe incorrect](https://dev-to-uploads.s3.amazonaws.com/i/tvq3cvsoh3ff24zl9e5k.JPG)

## Comment protéger les points de terminaison

Cette partie vous apprendra à protéger certains points de terminaison des utilisateurs non authentifiés.

### Créer deux points de terminaison

Vous avez besoin de deux points de terminaison pour pouvoir voir comment cela fonctionne. Copiez les points de terminaison suivants et collez-les dans le fichier `app.js` juste avant la dernière ligne.

```javascript
// point de terminaison libre
app.get("/free-endpoint", (request, response) => {
  response.json({ message: "Vous êtes libre d'accéder à moi à tout moment" });
});

// point de terminaison d'authentification
app.get("/auth-endpoint", (request, response) => {
  response.json({ message: "Vous êtes autorisé à accéder à moi" });
});

```

### Créer la fonction d'authentification

Ensuite, vous devrez créer une fonction pour vous permettre de protéger un point de terminaison particulier des utilisateurs non authentifiés.

Créez un fichier dans le répertoire racine et nommez-le `auth.js`.

Importez `jasonwebtoken` en haut du fichier :

```javascript

const jwt = require("jsonwebtoken");


```

Créez et exportez une fonction asynchrone dans laquelle le code d'autorisation résidera :

```javascript

module.exports = async (request, response, next) => {
    
}


```

Dans la fonction, utilisez un bloc `try...catch...` pour vérifier si un utilisateur est connecté :

```javascript

    try {
        
    } catch (error) {
        response.status(401).json({
            error: new Error("Requête invalide !"),
          });
    }


```

Dans le bloc `try{}` , obtenez le jeton d'authentification de l'`authorization header` :

```javascript

//   obtenir le jeton de l'en-tête d'autorisation
    const token = await request.headers.authorization.split(" ")[1];


```

Vérifiez si le jeton qui a été généré correspond à la chaîne de jeton (**RANDOM-TOKEN**) entrée initialement :

```javascript

//vérifier si le jeton correspond à l'origine supposée
    const decodedToken = await jwt.verify(
      token,
      "RANDOM-TOKEN"
    );


```

Passez les détails du `decodedToken` à la constante `user` :

```javascript

// récupérer les détails de l'utilisateur connecté
    const user = await decodedToken;


```

Passez l'`user` au point de terminaison :

```javascript

// transmettre l'utilisateur aux points de terminaison ici
    request.user = user;


```

Enfin, ouvrez la voie vers le point de terminaison :

```javascript

// transmettre la fonctionnalité au point de terminaison
    next();


```

Le fichier `auth.js` ressemble maintenant à ceci :

```javascript

const jwt = require("jsonwebtoken");

module.exports = async (request, response, next) => {
  try {
    //   obtenir le jeton de l'en-tête d'autorisation
    const token = await request.headers.authorization.split(" ")[1];

    //vérifier si le jeton correspond à l'origine supposée
    const decodedToken = await jwt.verify(token, "RANDOM-TOKEN");

    // récupérer les détails de l'utilisateur connecté
    const user = await decodedToken;

    // transmettre l'utilisateur aux points de terminaison ici
    request.user = user;

    // transmettre la fonctionnalité au point de terminaison
    next();
    
  } catch (error) {
    response.status(401).json({
      error: new Error("Requête invalide !"),
    });
  }
};


```

### Comment protéger le point de terminaison

C'est l'étape finale et la plus simple. Commencez par importer la fonction d'authentification dans le fichier `app.js` comme suit :

```javascript

const auth = require("./auth");


```

Ajoutez `auth` comme deuxième argument dans le point de terminaison d'authentification dans le fichier `app.js` :

```javascript

// point de terminaison d'authentification
app.get("/auth-endpoint", auth, (request, response) => {
  response.json({ message: "Vous êtes autorisé à accéder à moi" });
});


```

Et c'est tout. C'est tout ce dont vous avez besoin pour protéger cette route. Testons-la.

### Comment tester la protection du point de terminaison

Si l'utilisateur n'est pas connecté :

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/i/k9tlcam9ef4hjh93qeha.JPG)

Si l'utilisateur est connecté :

* Connectez-vous comme suit :

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/i/has8qii5z8srvlu5nbp9.JPG)

Copiez le jeton, puis ouvrez un nouvel onglet sur `postman`.

Sélectionnez `bearer token` dans le type d'authentification.

Collez le jeton dans le champ `token` et envoyez la requête.

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/i/s7evrpmfjy3mmfi5vtlb.JPG)

### Comment gérer les erreurs CORS

Une dernière chose ! Vous devez gérer les erreurs CORS. Cela permettra à l'utilisateur dans le frontend de consommer les API que vous avez créées sans aucun problème.

Pour ce faire, naviguez vers le fichier `app.js`.

Ajoutez le code suivant juste en dessous de la ligne `dbConnect()` :

```javascript

// Curb Cores Error en ajoutant un en-tête ici
app.use((req, res, next) => {
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader(
    "Access-Control-Allow-Headers",
    "Origin, X-Requested-With, Content, Accept, Content-Type, Authorization"
  );
  res.setHeader(
    "Access-Control-Allow-Methods",
    "GET, POST, PUT, DELETE, PATCH, OPTIONS"
  );
  next();
});


```

Et avec cela, vous êtes un champion de l'authentification Backend !!

## Comment héberger le Backend

Cette partie vous apprend à héberger l'application backend sur Heroku. À la fin, elle sera disponible pour tout le monde sur Internet. Suivez les étapes ci-dessous :

Créez un compte sur [Heroku](https://heroku.com/).

Si vous avez créé un compte, vous avez peut-être été invité à créer une application (c'est-à-dire un dossier où votre application sera hébergée). Créez-la. La mienne s'appelle `nodejs-mongodb-auth-app`.

Allez sur le tableau de bord de votre application :

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/i/msnum8scqj031dw53j27.JPG)

Sélectionnez la méthode de déploiement `GitHub` :

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/i/5edwt90cpy75b3uyqgvy.JPG)

Recherchez et sélectionnez un dépôt.

Cliquez sur `connect` :

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/i/6rpr4heuqqa9gn4qy1rt.JPG)

Sélectionnez la branche que vous souhaitez déployer (dans mon cas, c'est la branche `master`) :

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/i/4ka9c6781vft1gio7p0k.JPG)

Activez le déploiement automatique en cliquant sur le bouton `Enable automatic deployment` comme dans l'image ci-dessus.

Cliquez sur le bouton `Deploy` dans le déploiement manuel :

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/i/7ksrclnfyjzzvn2nr4gc.JPG)

Vous n'aurez pas à faire tout cela pour les déploiements ultérieurs.

Maintenant, vous avez un bouton vous disant de "view site" après la fin de la construction. Cliquez dessus. Cela ouvrira votre application dans un nouvel onglet.

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/i/pa4ohxetzg4o6a9ek53n.jpg)

**OHHH NON !!! UN BUG ? ERREUR D'APPLICATION ?**

Eh bien, ce n'est qu'un petit problème. Quelque chose que vous ne devez jamais oublier de faire lors des déploiements. La plupart des services d'hébergement l'exigeront.

### Comment corriger l'erreur de l'application Heroku

Dans le répertoire racine de votre projet, créez un fichier et nommez-le `Procfile`. Il n'a pas d'extension.

Dans le fichier, entrez ce qui suit :

```javascript
web: node index.js

```

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/i/k655prvq8m34jsbs3p37.JPG)

Cela dirige Heroku vers le fichier serveur (`index.js`) qui est le point d'entrée de l'application. Si votre serveur est dans un fichier différent, allez-y et modifiez-le comme requis.

Enregistrez le fichier et poussez les nouvelles modifications vers GitHub.

Attendez 2 à 5 minutes pour que Heroku détecte automatiquement les modifications dans votre dépôt GitHub et reflète les modifications sur l'application.

Vous pouvez maintenant actualiser cette page d'erreur et voir votre travail acharné porter ses fruits :

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/i/cfdmvfquj0jsoxf4npeg.JPG)

### Comment ajouter MongoDB

Vous avez peut-être remarqué que les autres routes ne sont pas fonctionnelles. C'est parce que vous n'avez pas inclus la base de données.

Rappelez-vous que l'URL de la base de données est dans le fichier `.env`. Mais le fichier `.env` n'est pas inclus dans le projet sur GitHub après l'avoir poussé. Vous devez donc ajouter directement l'URL MongoDB dans l'application Heroku.

Faisons cela...

Naviguez vers les paramètres de votre application : `https://dashboard.heroku.com/apps/<your_app_name>/settings`

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/i/ojmvtebcl4dg6hhbsme5.JPG)

Faites défiler vers le bas jusqu'à la section `Config Vars`.

Ajoutez la clé et la valeur de votre base de données :

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/i/jo0nlhdf81aeu5cw26n3.JPG)

C'est tout ! Votre application devrait fonctionner correctement maintenant.

### Comment tester les points de terminaison après l'hébergement

Le moyen le plus simple de tester si cela fonctionne est d'essayer le point de terminaison de connexion.

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/i/op98eomewsw8n96hibbe.JPG)

Cela a fonctionné !

## Faisons un bilan

Le but de cette section était de créer une application d'authentification backend. Au fur et à mesure que vous avez développé l'application, vous avez appris à connaître `bycrypt`, `jsonwebtoken`, `heroku`, `CORS`, `database`, `MongoDB`, `Clusters`, `collections`, et `models`.

Vous avez commencé par configurer une base de données sur MongoDB Atlas. Ensuite, vous avez procédé à la création de deux points de terminaison - register et login - pour nous permettre d'entrer un utilisateur dans la base de données et de vérifier si l'utilisateur existe. Ensuite, vous avez vu comment vous pouvez protéger les points de terminaison et comment gérer les erreurs CORS. Enfin, vous avez appris à héberger l'application que vous avez construite.

Le code de cette section peut être trouvé [ici](https://github.com/EBEREGIT/auth-backend). Il est en direct sur Heroku [ici](https://nodejs-mongodb-auth-app.herokuapp.com/).

La section suivante nous aidera à rendre cette application utile pour les utilisateurs finaux en construisant un frontend pour combler le fossé entre les utilisateurs et le backend.

# Section 2 : Comment construire le Frontend

Le frontend représente ce que l'utilisateur peut voir et avec quoi il peut interagir. Vous allez construire une interface utilisateur pour permettre à l'utilisateur de communiquer avec le backend en cliquant sur des boutons.

Vous allez commencer par construire l'UI en utilisant React-Bootstrap. Ensuite, vous allez connecter l'UI aux points de terminaison en utilisant `axios`. Vous allez ensuite protéger certaines routes contre les utilisateurs non autorisés. Enfin, vous allez héberger le frontend sur Netlify.

Mettons-nous au travail !

## Comment construire l'interface utilisateur

Cette partie vous présentera React-Bootstrap et vous guidera dans la construction des formulaires d'inscription et de connexion.

[Bootstrap](https://getbootstrap.com/) a volé le cœur de nombreux développeurs au fil des ans. Cela est compréhensible car il vous aide à écrire un code plus court et plus propre, il fait gagner du temps et il est suffisamment sophistiqué pour gérer de nombreuses préoccupations des développeurs, surtout si vous n'aimez pas écrire du CSS.

Il y a aussi [React](https://reactjs.org/) qui est devenu l'un des frameworks/bibliothèques JavaScript frontend les plus populaires. Il a également une grande communauté construite autour.

Pour garantir un développement encore plus facile et rapide avec React, Bootstrap a développé une nouvelle base de code appelée [React-Bootstrap](https://react-bootstrap.netlify.app/).

React-Bootstrap est toujours Bootstrap mais il a été conçu pour s'intégrer correctement à React. Cela garantit qu'il y a peu ou pas de bugs lors de la construction de votre application.

### Pourquoi utiliser React-Bootstrap au lieu de Bootstrap ?

React-Bootstrap a été construit et adapté spécifiquement pour les applications React. Cela signifie qu'il est plus compatible.

Le code React-Bootstrap est généralement plus court que le code Bootstrap. Par exemple, si vous souhaitez créer une colonne de grille de trois dans une rangée, vous pouvez le faire de la manière suivante :

En utilisant Bootstrap :

```javascript

<div class="container">
  <div class="row">
    <div class="col-sm">
      Une des trois colonnes
    </div>
    <div class="col-sm">
      deux des trois colonnes
    </div>
    <div class="col-sm">
      trois des trois colonnes
    </div>
  </div>
</div>


```

En utilisant React-Bootstrap :

```javascript

<Container>
  <Row>
    <Col>Une des trois colonnes</Col>
    <Col>deux des trois colonnes</Col>
    <Col>trois des trois colonnes</Col>
  </Row>
</Container>


```

### Comment utiliser React-Bootstrap

Les étapes suivantes vous montreront comment créer une interface utilisateur simple avec React-Bootstrap :

#### Comment configurer le projet

Créez un projet React et nommez-le `react-auth`.

```javascript

npx create-react-app react-auth


```

Ouvrez le projet dans un terminal et naviguez dans le dossier du projet. J'utiliserai VS Code.

```javascript

cd react-auth


```

Installez React-Bootstrap :

```javascript

npm install react-bootstrap bootstrap


```

Importez le fichier CSS Bootstrap dans le fichier `index.js` :

```javascript

import 'bootstrap/dist/css/bootstrap.min.css';


```

### Comment créer les composants

Cette partie vous montrera comment utiliser les composants déjà créés pour créer une interface utilisateur. Vous allez créer les formulaires d'inscription et de connexion ici.

Créez un nouveau fichier dans le dossier `src`. Nommez-le : `Register.js`.

Dans le fichier, commencez avec le code suivant :

```javascript

import React from 'react'

export default function Register() {
    return (
        <>
            
        </>
    )
}


```

Entrez le code suivant dans l'instruction `return` :

```javascript

      <h2>Inscription</h2>
      <Form>
        {/* email */}
        <Form.Group controlId="formBasicEmail">
          <Form.Label>Adresse email</Form.Label>
          <Form.Control type="email" placeholder="Entrez l'email" />
        </Form.Group>

        {/* mot de passe */}
        <Form.Group controlId="formBasicPassword">
          <Form.Label>Mot de passe</Form.Label>
          <Form.Control type="password" placeholder="Mot de passe" />
        </Form.Group>

        {/* bouton de soumission */}
        <Button variant="primary" type="submit">
          Soumettre
        </Button>
      </Form>


```

Maintenant, vous devez informer Bootstrap que vous souhaitez utiliser les composants `Form` et `Button`. Donc, importez-les en haut :

```javascript

import { Form, Button } from "react-bootstrap";


```

Vous pouvez également choisir de le faire individuellement comme suit :

```javascript

import Form from 'react-bootstrap/Form'
import Button from 'react-bootstrap/Button'


```

Affichez le composant Register sur la page. Tout d'abord, remplacez le code dans le fichier `App.js` par le code suivant :

```javascript

import { Container, Col, Row } from "react-bootstrap";
import "./App.css";

function App() {
  return (
    <Container>
      <Row>

      </Row>
    </Container>
  );
}

export default App;


```

Dans le composant `Row`, entrez ce qui suit :

```javascript

    <Col xs={12} sm={12} md={6} lg={6}></Col>
    <Col xs={12} sm={12} md={6} lg={6}></Col>


```

Cela garantira qu'il y a deux colonnes sur les appareils de grande et moyenne taille, tandis qu'il y aura une colonne sur chaque ligne sur les appareils de petite et très petite taille.

Dans la première colonne, ajoutez le composant `Register` que vous avez créé et importez-le en haut du fichier. Le fichier `App.js` ressemblera à ceci :

```javascript

import { Container, Col, Row } from "react-bootstrap";
import Register from "./Register";

function App() {
  return (
    <Container>
      <Row>
        <Col xs={12} sm={12} md={6} lg={6}>
          <Register />
        </Col>

        <Col xs={12} sm={12} md={6} lg={6}></Col>
      </Row>
    </Container>
  );
}

export default App;



```

Exécutez `npm start` dans le terminal et voyez le résultat sur le navigateur.

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/i/lml6u4qdyq936ld3w72j.JPG)

Vous remarquerez qu'une seule colonne est prise. Maintenant, votre travail est de créer un composant LOGIN avec le même code que dans le composant REGISTER. Ensuite, ajoutez-le dans la deuxième colonne. Consultez ma sortie ci-dessous :

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/i/pic57grbm1tjcz6fcrre.JPG)

Walah ! Vous pouvez maintenant créer des applications React plus rapidement en tirant parti de React-Bootstrap.

Maintenant, vous allez commencer à connecter ces formulaires au backend.

## Comment inscrire un utilisateur

Cette partie vous guide à travers la connexion du formulaire d'inscription au point de terminaison `register` : `https://nodejs-mongodb-auth-app.herokuapp.com/register`.

Naviguez dans le fichier `Register.js`.

Définissez les états initiaux pour `email`, `password` et `register`.

```javascript

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [register, setRegister] = useState(false);


```

Définissez un attribut `name` et `value` pour les champs de saisie `email` et `password` :

```javascript

{/* email */}
        <Form.Group controlId="formBasicEmail">
          <Form.Label>Adresse email</Form.Label>
          <Form.Control
            type="email"
            name="email"
            value={email}
            placeholder="Entrez l'email"
          />
        </Form.Group>

        {/* mot de passe */}
        <Form.Group controlId="formBasicPassword">
          <Form.Label>Mot de passe</Form.Label>
          <Form.Control
            type="password"
            name="password"
            value={password}
            placeholder="Mot de passe"
          />
        </Form.Group>


```

À ce stade, vous remarquerez que vous ne pouvez plus taper dans les champs du formulaire d'inscription. Cela est dû au fait que vous n'avez pas défini le champ pour qu'il se mette à jour de l'état précédent à l'état actuel.

Faisons cela...

Ajoutez `onChange={(e) => setEmail(e.target.value)}`
et `onChange={(e) => setPassword(e.target.value)}` aux champs de saisie `email` et `password` respectivement :

```javascript

       {/* email */}
        <Form.Group controlId="formBasicEmail">
          <Form.Label>Adresse email</Form.Label>
          <Form.Control
            type="email"
            name="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="Entrez l'email"
          />
        </Form.Group>

        {/* mot de passe */}
        <Form.Group controlId="formBasicPassword">
          <Form.Label>Mot de passe</Form.Label>
          <Form.Control
            type="password"
            name="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="Mot de passe"
          />
        </Form.Group>


```

Maintenant, vous pouvez taper dans les champs du formulaire car il met à jour l'état en fonction du contenu que vous tapez.

Ajoutez `onSubmit={(e)=>handleSubmit(e)}` et `onClick={(e)=>handleSubmit(e)}` aux éléments `form` et `button`, respectivement.

`onSubmit` permet la soumission du formulaire en utilisant la touche `Entrée`, tandis que `onClick` permet la soumission du formulaire en cliquant sur le bouton. Maintenant, le formulaire ressemble à ceci :

```javascript

      <Form onSubmit={(e)=>handleSubmit(e)}>
        {/* email */}
        <Form.Group controlId="formBasicEmail">
          <Form.Label>Adresse email</Form.Label>
          <Form.Control
            type="email"
            name="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="Entrez l'email"
          />
        </Form.Group>

        {/* mot de passe */}
        <Form.Group controlId="formBasicPassword">
          <Form.Label>Mot de passe</Form.Label>
          <Form.Control
            type="password"
            name="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="Mot de passe"
          />
        </Form.Group>

        {/* bouton de soumission */}
        <Button
          variant="primary"
          type="submit"
          onClick={(e) => handleSubmit(e)}
        >
          Inscription
        </Button>
      </Form>


```

Pour tester si cela fonctionne, créez la fonction suivante juste avant la ligne `return` :

```javascript

const handleSubmit = (e) => {
    // empêcher le formulaire de rafraîchir toute la page
    e.preventDefault();
    // faire une alerte popup montrant le texte "soumis"
    alert("Soumis");
  }


```

Si vous cliquez sur le bouton ou appuyez sur la touche Entrée, voici ce que vous devriez obtenir :

![Test de la fonction handleSubmit](https://dev-to-uploads.s3.amazonaws.com/i/zryimfq0tsf20umz70oj.JPG)

### Comment construire la fonction `handleSubmit`

Maintenant, retirez l'instruction `alert` de la fonction `handleSubmit`.

Installez `axios`. Vous l'utiliserez pour appeler le point de terminaison ou connecter le frontend au backend, selon le cas.

```javascript

npm i axios


```

Importez `axios` en haut du fichier :

```javascript

import axios from "axios";


```

Dans la fonction handleSubmit, construisez la configuration nécessaire pour que `axios` connecte avec succès le frontend au backend.

```javascript

// définir les configurations
    const configuration = {
      method: "post",
      url: "https://nodejs-mongodb-auth-app.herokuapp.com/register",
      data: {
        email,
        password,
      },
    };


```

La `méthode` indique comment les données seront traitées, `url` est le point de terminaison appelé, et `data` contient toutes les entrées ou le `corps de la requête` que le backend attend.

Ayant configuré les configurations, faites l'appel. L'appel API est simplement une instruction d'une ligne :

```javascript

axios(configuration)


```

Avec cela, l'appel API a été complété. Cependant, vous devez être sûr qu'il a réussi. Et peut-être montrer le résultat aux utilisateurs.

Pour corriger cela, vous utiliserez un bloc then...catch....

Maintenant, vous avez ceci :

```javascript

    // faire l'appel API
    axios(configuration)
    .then((result) => {console.log(result);})
    .catch((error) => {console.log(error);})


```

Inscrire un nouvel utilisateur et vérifier la console pour le résultat. Le résultat que vous obtenez devrait ressembler à ceci :

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/i/p18oqn02fsqe0hx2qnlc.JPG)

Bien sûr, vous ne dirigerez pas vos utilisateurs vers la console pour vérifier le résultat de leur inscription. Vous avez besoin d'un moyen de communiquer avec l'utilisateur.

Remplacez ce code par le code suivant :

```javascript

    // faire l'appel API
    axios(configuration)
      .then((result) => {
        setRegister(true);
      })
      .catch((error) => {
        error = new Error();
      });


```

En définissant `register` sur `true`, vous pouvez maintenant savoir quand le processus d'inscription est terminé. Informez l'utilisateur en utilisant le code suivant dans l'élément `Form` :

```javascript

      {/* afficher le message de succès */}
        {register ? (
          <p className="text-success">Vous êtes inscrit avec succès</p>
        ) : (
          <p className="text-danger">Vous n'êtes pas inscrit</p>
        )}


```

Le code est une instruction conditionnelle pour afficher un message de succès lorsque `register` est `true`. Maintenant, essayez-le !

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/i/mbavmdxdhuleb9259rf1.gif)

Si vous obtenez le même résultat que ci-dessus, alors vous l'avez fait !

Vous êtes génial.

## Comment connecter un utilisateur

Maintenant, il est temps de vous concentrer sur le fichier `Login.js`.

Définissez les états initiaux pour `email`, `password` et `login` comme suit :

```javascript

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [login, setLogin] = useState(false);


```

Définissez un attribut `name` et `value` pour les champs de saisie `email` et `password` :

```javascript

{/* email */}
        <Form.Group controlId="formBasicEmail">
          <Form.Label>Adresse email</Form.Label>
          <Form.Control
            type="email"
            name="email"
            value={email}
            placeholder="Entrez l'email"
          />
        </Form.Group>

        {/* mot de passe */}
        <Form.Group controlId="formBasicPassword">
          <Form.Label>Mot de passe</Form.Label>
          <Form.Control
            type="password"
            name="password"
            value={password}
            placeholder="Mot de passe"
          />
        </Form.Group>


```

Ajoutez `onChange={(e) => setEmail(e.target.value)}`
et `onChange={(e) => setPassword(e.target.value)}` aux champs de saisie `email` et `password`, respectivement. Voici le mien :

```javascript

       {/* email */}
        <Form.Group controlId="formBasicEmail">
          <Form.Label>Adresse email</Form.Label>
          <Form.Control
            type="email"
            name="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="Entrez l'email"
          />
        </Form.Group>

        {/* mot de passe */}
        <Form.Group controlId="formBasicPassword">
          <Form.Label>Mot de passe</Form.Label>
          <Form.Control
            type="password"
            name="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="Mot de passe"
          />
        </Form.Group>


```

Vous pouvez maintenant taper dans le formulaire.

Ajoutez `onSubmit={(e)=>handleSubmit(e)}` et `onClick={(e)=>handleSubmit(e)}` aux éléments `form` et `button`, respectivement.

Le `onSubmit` permet la soumission du formulaire en utilisant la touche `Entrée` tandis que le `onClick` permet la soumission du formulaire en cliquant sur le bouton.

Maintenant, le formulaire ressemble à ceci :

```javascript

      <Form onSubmit={(e)=>handleSubmit(e)}>
        {/* email */}
        <Form.Group controlId="formBasicEmail">
          <Form.Label>Adresse email</Form.Label>
          <Form.Control
            type="email"
            name="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="Entrez l'email"
          />
        </Form.Group>

        {/* mot de passe */}
        <Form.Group controlId="formBasicPassword">
          <Form.Label>Mot de passe</Form.Label>
          <Form.Control
            type="password"
            name="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="Mot de passe"
          />
        </Form.Group>

        {/* bouton de soumission */}
        <Button
          variant="primary"
          type="submit"
          onClick={(e) => handleSubmit(e)}
        >
          Connexion
        </Button>
      </Form>


```

Pour tester si cela fonctionne, créez la fonction suivante juste avant la ligne `return` :

```javascript

const handleSubmit = (e) => {
    // empêcher le formulaire de rafraîchir toute la page
    e.preventDefault();
    // faire une alerte popup montrant le texte "soumis"
    alert("Soumis");
  }


```

Si vous cliquez sur le bouton ou appuyez sur la touche `Entrée`, voici ce que vous devriez obtenir :

![Test de la fonction handleSubmit](https://dev-to-uploads.s3.amazonaws.com/i/zryimfq0tsf20umz70oj.JPG)

### Comment construire la fonction `handleSubmit`

Maintenant, vous devez retirer l'instruction `alert` de la fonction `handleSubmit`.

Importez `axios` en haut du fichier :

```javascript

import axios from "axios";


```

Dans la fonction `handleSubmit`, construisez la configuration nécessaire pour que `axios` connecte avec succès le frontend au backend.

```javascript

// définir les configurations
    const configuration = {
      method: "post",
      url: "https://nodejs-mongodb-auth-app.herokuapp.com/login",
      data: {
        email,
        password,
      },
    };


```

La `méthode` indique comment les données seront traitées, `url` est le point de terminaison par lequel la fonction API est accessible, et `data` contient toutes les entrées ou le `corps de la requête` que le backend attend.

Ayant configuré les configurations, faites l'appel.

```javascript

    // faire l'appel API
    axios(configuration)
    .then((result) => {console.log(result);})
    .catch((error) => {console.log(error);})


```

Essayez de connecter un utilisateur et vérifiez la console pour le résultat

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/i/82z97iv2ym4z9sbng7ib.JPG)

Remplacez ce code par le code suivant :

```javascript

    // faire l'appel API
    axios(configuration)
      .then((result) => {
        setLogin(true);
      })
      .catch((error) => {
        error = new Error();
      });


```

En définissant `login` sur `true`, vous pouvez maintenant savoir quand le processus de connexion est terminé. Faites cela avec le code suivant dans l'élément `Form` :

```javascript

      {/* afficher le message de succès */}
        {login ? (
          <p className="text-success">Vous êtes connecté avec succès</p>
        ) : (
          <p className="text-danger">Vous n'êtes pas connecté</p>
        )}


```

Le code est une instruction conditionnelle pour afficher un message de succès lorsque `login` est `true`. Essayez-le.

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/i/ujiildu7dqscevjhai3z.gif)

Si vous obtenez le même résultat que ci-dessus, alors vous l'avez fait !

Vous êtes une rockstar !

## Comment protéger les routes

L'authentification sera inutile si n'importe quel utilisateur peut toujours accéder à l'application d'une manière ou d'une autre. Peut-être en tapant l'URL souhaitée dans la barre d'adresse. Dans cette partie, vous serez en mesure de protéger chaque route qui nécessite une authentification pour être accessible.

Tout d'abord, vous allez créer deux composants supplémentaires. Ensuite, vous allez configurer des routes pour ces composants. Enfin, vous allez créer un composant pour protéger les routes et appliquer le composant aux routes souhaitées.

### Tout d'abord, créez deux composants

Créez un nouveau fichier dans le répertoire `src` et nommez-le `FreeComponent.js`

Le fichier doit avoir le contenu suivant :

```javascript

import React from "react";

export default function FreeComponent() {
  return (
    <div>
      <h1 className="text-center">Composant gratuit</h1>
    </div>
  );
}


```

Créez un fichier et nommez-le `AuthComponent.js`. Le fichier doit avoir le contenu suivant :

```javascript

import React from "react";

export default function AuthComponent() {
  return (
    <div>
      <h1 className="text-center">Composant d'authentification</h1>
    </div>
  );
}


```

### Comment configurer la route

Installez `react-router-dom` :

```javascript

npm install --save react-router-dom


```

Naviguez vers le fichier `index.js`.

Importez `BrowserRouter` :

```javascript

import { BrowserRouter } from "react-router-dom";


```

Enveloppez le composant `<App>` avec le composant `</BrowserRouter>`. Ainsi, le fichier `index.js` ressemble maintenant à ceci :

```javascript

import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import App from "./App";
import reportWebVitals from "./reportWebVitals";
import "bootstrap/dist/css/bootstrap.min.css";
import { BrowserRouter } from "react-router-dom";

ReactDOM.render(
  <React.StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </React.StrictMode>,
  document.getElementById("root")
);

// Si vous voulez commencer à mesurer les performances dans votre application, passez une fonction
// pour enregistrer les résultats (par exemple : reportWebVitals(console.log))
// ou envoyez à un point de terminaison d'analyse. En savoir plus : https://bit.ly/CRA-vitals
reportWebVitals();


```

Maintenant, naviguez vers le fichier `App.js`.

Importez `Switch` et `Route` en haut du fichier :

```javascript

import { Switch, Route } from "react-router-dom";


```

Remplacez le composant `Account` par le code suivant :

```javascript

     <Switch>
        <Route exact path="/" component={Account} />
        <Route exact path="/free" component={FreeComponent} />
        <Route exact path="/auth" component={AuthComponent} />
      </Switch>


```

Vous remarquerez que rien n'a changé. Cela est dû au fait que le composant Account est toujours le composant par défaut lors du routage. Mais vous avez maintenant accès à plusieurs routes.

Ajoutez des liens à des fins de navigation sous l'en-tête `React Authentication Tutorial` :

```javascript

     <Row>
        <Col className="text-center">
          <h1>Tutoriel d'authentification React</h1>

          <section id="navigation">
            <a href="/">Accueil</a>
            <a href="/free">Composant gratuit</a>
            <a href="/auth">Composant d'authentification</a>
          </section>
        </Col>
      </Row>


```

Naviguez vers `index.css` pour ajouter le style suivant à des fins esthétiques :

```css

#navigation{
  margin-top: 5%;
  margin-bottom: 5%;
}

#navigation a{
  margin-right: 10%;
}

#navigation a:last-child{
  margin-right: 0;
}


```

### Le composant de route protégée

Ayant configuré avec succès les routes, vous souhaitez maintenant protéger l'une d'entre elles (c'est-à-dire le `AuthComponent`). Pour ce faire, vous devez créer un nouveau composant qui vous aidera à vérifier si une certaine condition a été remplie avant d'autoriser un utilisateur à accéder à cette route.

La condition que vous utiliserez dans ce cas est le jeton généré lors de la `connexion`. Donc, avant de créer ce composant `ProtectedRoute`, allons chercher le jeton dans le composant `Login` et le rendre disponible dans toutes les parties de l'application.

#### Comment obtenir le jeton

Installez `universal-cookie`. Il s'agit d'un package de cookies qui nous aide à partager une valeur ou une variable dans toute l'application :

```javascript

npm i universal-cookie -s


```

Naviguez vers le fichier `Login.js`.

Importez `universal-cookie` en haut et initialisez-le :

```javascript

import Cookies from "universal-cookie";
const cookies = new Cookies();


```

Ensuite, ajoutez le code suivant dans le bloc `then` de l'appel `axios` :

```javascript

       // définir le cookie
        cookies.set("TOKEN", result.data.token, {
          path: "/",
        });


```

Le code ci-dessus définit le cookie avec `cookie.set()`. Il prend trois arguments : `Nom` du cookie (ici c'est `"TOKEN"`, mais cela peut être n'importe quoi que vous choisissez), `Valeur` du cookie (`result.data.token`), et sur quelle page ou route vous voulez qu'il soit disponible (définir le `path` sur `"/"` rend le cookie disponible sur toutes les pages). Espérons que cela a du sens.

En dessous de `cookie.set()`, ajoutez la ligne de code suivante pour rediriger l'utilisateur vers le `authComponent` après une connexion réussie

```javascript

        // rediriger l'utilisateur vers la page d'authentification
        window.location.href = "/auth";


```

#### Comment créer le composant de route protégée

Puisque le jeton est maintenant disponible dans toute l'application, vous avez maintenant accès à celui-ci sur tous les composants ou pages déjà créés ou à créer. Continuons...

Créez un fichier avec ce nom : `ProtectedRoutes.js`.

Entrez le code suivant dans le fichier :

```javascript

import React from "react";
import { Route, Redirect } from "react-router-dom";
import Cookies from "universal-cookie";
const cookies = new Cookies();

// reçoit le composant et tout autre prop représenté par ...rest
export default function ProtectedRoutes({ component: Component, ...rest }) {
  return (

    // cette route prend d'autres routes qui lui sont assignées depuis App.js et retourne la même route si la condition est remplie
    <Route
      {...rest}
      render={(props) => {
        // obtenir le cookie du navigateur si connecté
        const token = cookies.get("TOKEN");

        // retourne la route s'il y a un jeton valide défini dans le cookie
        if (token) {
          return <Component {...props} />;
        } else {
          // retourne l'utilisateur à la page d'accueil s'il n'y a pas de jeton valide défini
          return (
            <Redirect
              to={{
                pathname: "/",
                state: {
                  // définit l'emplacement qu'un utilisateur était sur le point d'accéder avant d'être redirigé vers la connexion
                  from: props.location,
                },
              }}
            />
          );
        }
      }}
    />
  );
}


```

Attendez ! Attendez !! Que se passe-t-il dans le composant `ProtectedRoutes` ?

C'est comme un modèle. Ce qui change, c'est la condition sur laquelle le composant `ProtectedRoutes` est basé. Dans ce cas, il est basé sur le `jeton` reçu du cookie lors de la connexion. Donc dans une autre application, la condition peut être différente.

Voici ce qui se passe ici : Le composant `ProtectedRoutes` reçoit un `composant` puis décide si le composant doit être retourné à l'utilisateur ou non.

Pour prendre cette décision, il vérifie s'il y a un `jeton` valide (le jeton est défini lors d'une connexion réussie) provenant du cookie. Si le jeton est `indéfini`, alors il redirige vers le `chemin` par défaut (la page d'accueil dans ce cas).

Les commentaires dans le code vous aideront également à comprendre ce qui se passe dans le composant. Suivez patiemment...

### Comment utiliser le composant `ProtectedRoutes`

Il est temps d'utiliser le composant `ProtectedRoutes` pour protéger le AuthComponent puisqu'il ne doit être accessible qu'aux utilisateurs authentifiés.

Naviguez vers le fichier `App.js`.

Importez le composant `ProtectedRoutes` :

```javascript

import ProtectedRoutes from "./ProtectedRoutes";


```

Remplacez `<Route exact path="/auth" component={AuthComponent} />` par `<ProtectedRoutes path="/auth" component={AuthComponent} />`.

Le fichier `App.js` à ce stade ressemble à ceci :

```javascript

import { Switch, Route } from "react-router-dom";
import { Container, Col, Row } from "react-bootstrap";
import Account from "./Account";
import FreeComponent from "./FreeComponent";
import AuthComponent from "./AuthComponent";
import ProtectedRoutes from "./ProtectedRoutes";

function App() {
  return (
    <Container>
      <Row>
        <Col className="text-center">
          <h1>Tutoriel d'authentification React</h1>

          <section id="navigation">
            <a href="/">Accueil</a>
            <a href="/free">Composant gratuit</a>
            <a href="/auth">Composant d'authentification</a>
          </section>
        </Col>
      </Row>

      {/* créer des routes ici */}
      <Switch>
        <Route exact path="/" component={Account} />
        <Route exact path="/free" component={FreeComponent} />
        <ProtectedRoutes path="/auth" component={AuthComponent} />
      </Switch>
    </Container>
  );
}

export default App;


```

Essayez d'accéder à `http://localhost:3000/auth` sans vous connecter et remarquez comment il vous redirige vers la page d'accueil.

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/i/7wmf5t65c946kqsndg8f.gif)
_C'est incroyable. N'est-ce pas ?_

## Comment faire des appels API en utilisant le hook `useEffect`

> [React Hooks](https://reactjs.org/docs/hooks-overview.html#:~:text=Hooks%20are%20functions%20that%20let,if%20you'd%20like.)) sont des fonctions qui vous permettent de "vous accrocher" aux fonctionnalités d'état et de cycle de vie de React à partir de composants de fonction. Les hooks ne fonctionnent pas à l'intérieur des classes - ils vous permettent d'utiliser React sans classes.

Les exemples de hooks incluent `useState`, `useEffect` et `useRef`.

Cette partie vous montrera comment faire des appels API en utilisant le hook `useEffect`. Le hook `useEffect` fait pour les composants `fonctionnels` React ce que `componentDidMount()` fait pour les composants `de classe` React.

Les points de terminaison suivants que vous allez appeler sont :

* **Point de terminaison gratuit** : `https://nodejs-mongodb-auth-app.herokuapp.com/free-endpoint`
* **Point de terminaison protégé** : `https://nodejs-mongodb-auth-app.herokuapp.com/auth-endpoint`

### Comment appeler le point de terminaison gratuit

Suivez les étapes ci-dessous pour appeler `https://nodejs-mongodb-auth-app.herokuapp.com/free-endpoint`.

Naviguez vers le fichier `FreeComponent.js`.

Importez `useEffect` et `useState` en ajustant votre ligne d'importation `react` avec ce qui suit :

```javascript

import React, { useEffect, useState,  } from "react";


```

Importez `axios` :

```javascript

import axios from "axios";


```

Définissez un état initial pour `message` :

```javascript

const [message, setMessage] = useState("");


```

Juste au-dessus de l'instruction `return`, déclarez la fonction `useEffect` :

```javascript

  useEffect(() => {

  }, [])


```

Le tableau vide (c'est-à-dire `[]`) est important pour éviter une exécution continue après qu'un appel API a été complété.

Dans la fonction, définissez les configurations suivantes :

```javascript

  useEffect(() => {
    // définir les configurations pour l'appel API ici
    const configuration = {
      method: "get",
      url: "https://nodejs-mongodb-auth-app.herokuapp.com/free-endpoint",
    };
  }, [])


```

Ensuite, faites l'appel API en utilisant `axios` :

```javascript

  // useEffect s'exécute automatiquement une fois que la page est complètement chargée
  useEffect(() => {
    // définir les configurations pour l'appel API ici
    const configuration = {
      method: "get",
      url: "https://nodejs-mongodb-auth-app.herokuapp.com/free-endpoint",
    };

    // faire l'appel API
    axios(configuration)
      .then((result) => {
        // attribuer le message dans notre résultat au message que nous avons initialisé ci-dessus
        setMessage(result.data.message);
      })
      .catch((error) => {
        error = new Error();
      });
  }, [])


```

`setMessage(result.data.message);` attribue le message dans le résultat (c'est-à-dire result.data.message) au message initialisé ci-dessus. Maintenant, vous pouvez afficher le `message` dans votre composant.

Pour afficher le `message` que vous avez obtenu sur la page `FreeComponent`, entrez le code suivant en dessous de la ligne `<h1 className="text-center">Free Component</h1>` :

```javascript

<h3 className="text-center text-danger">{message}</h3>


```

React lira le `message` comme une variable à cause des accolades. Si le `message` est sans les accolades, React le lit comme une chaîne de caractères.

Voici le fichier `FreeComponent.js` à ce stade :

```javascript

import React, { useEffect, useState } from "react";
import axios from "axios";

export default function FreeComponent() {
  // définir un état initial pour le message que nous recevrons après l'appel API
  const [message, setMessage] = useState("");

  // useEffect s'exécute automatiquement une fois que la page est complètement chargée
  useEffect(() => {
    // définir les configurations pour l'appel API ici
    const configuration = {
      method: "get",
      url: "https://nodejs-mongodb-auth-app.herokuapp.com/free-endpoint",
    };

    // faire l'appel API
    axios(configuration)
      .then((result) => {
        // attribuer le message dans notre résultat au message que nous avons initialisé ci-dessus
        setMessage(result.data.message);
      })
      .catch((error) => {
        error = new Error();
      });
  }, []);

  return (
    <div>
      <h1 className="text-center">Composant gratuit</h1>

      {/* afficher notre message de notre appel API */}
      <h3 className="text-center text-danger">{message}</h3>
    </div>
  );
}


```

Voici la page `FreeComponent` à l'heure actuelle :

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/i/7ap2bd2okfjwsrzl9a67.JPG)

### Comment appeler le point de terminaison protégé

Il est temps d'appeler `https://nodejs-mongodb-auth-app.herokuapp.com/auth-endpoint`.

Naviguez vers le fichier `AuthComponent.js`.

Importez `useEffect` et `useState` en ajustant votre ligne d'importation `react` avec ce qui suit :

```javascript

import React, { useEffect, useState,  } from "react";


```

Importez `axios` :

```javascript

import axios from "axios";


```

Importez et initialisez universal-cookie :

```javascript

import Cookies from "universal-cookie";
const cookies = new Cookies();


```

Obtenez le jeton généré lors de la connexion :

```javascript

const token = cookies.get("TOKEN");


```

Définissez un état initial pour `message` :

```javascript

const [message, setMessage] = useState("");


```

Juste au-dessus de l'instruction `return`, déclarez la fonction `useEffect` :

```javascript

  useEffect(() => {

  }, [])


```

Dans la fonction, définissez les configurations suivantes :

```javascript

  useEffect(() => {
    // définir les configurations pour l'appel API ici
    const configuration = {
      method: "get",
      url: "https://nodejs-mongodb-auth-app.herokuapp.com/auth-endpoint",
      headers: {
        Authorization: `Bearer ${token}`,
      },
    };
  }, [])


```

Remarquez que cette configuration contient un `header`. C'est la principale différence avec la configuration `free-endpoint`.

C'est le cas parce que le `auth-endpoint` est un point de terminaison protégé qui n'est accessible qu'en utilisant un `jeton d'autorisation`. C'est donc dans l'en-tête que vous spécifiez le `jeton d'autorisation`. Sans cet en-tête, l'appel API retournera une erreur `403:Forbidden`.

Faites l'appel API :

```javascript

// useEffect s'exécute automatiquement une fois que la page est complètement chargée
  useEffect(() => {
    // définir les configurations pour l'appel API ici
    const configuration = {
      method: "get",
      url: "https://nodejs-mongodb-auth-app.herokuapp.com/auth-endpoint",
      headers: {
        Authorization: `Bearer ${token}`,
      },
    };

    // faire l'appel API
    axios(configuration)
      .then((result) => {
        // attribuer le message dans notre résultat au message que nous avons initialisé ci-dessus
        setMessage(result.data.message);
      })
      .catch((error) => {
        error = new Error();
      });
  }, []);


```

Pour afficher le `message` que vous avez obtenu sur la page `AuthComponent`, entrez le code suivant en dessous de la ligne `<h1 className="text-center">Auth Component</h1>` :

```javascript

<h3 className="text-center text-danger">{message}</h3>


```

Voici la page `AuthComponent` à l'heure actuelle :

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/i/qqud8uirnrepmfxd0mff.JPG)

## Comment construire la fonction de déconnexion

Si pour une raison quelconque vous partagez un appareil avec quelqu'un d'autre, il est toujours possible pour eux d'avoir accès à la page `authComponent` après que vous soyez connecté.

Pour vous assurer que cela ne se produise pas, vous devez détruire votre jeton d'autorisation chaque fois que vous avez terminé.

Pour ce faire, ajoutez un bouton sur la page `authComponent`.

Importez le composant `Button` :

```javascript

import { Button } from "react-bootstrap";


```

Ajoutez le code suivant en dessous du texte :

```javascript

<Button type="submit" variant="danger">Déconnexion</Button>


```

La fonction de déconnexion doit être déclenchée lorsque le bouton est cliqué. Ajoutez donc `onClick={() => logout()}` aux options du bouton. Le bouton ressemblera maintenant à ceci :

```javascript

{/* déconnexion */}
<Button type="submit" variant="danger" onClick={() => logout()}>
   Déconnexion
</Button>


```

Créez la fonction. Entrez le code suivant juste au-dessus du return :

```javascript

  // déconnexion
  const logout = () => {
    
  }


```

Ajoutez le code suivant à la fonction de déconnexion pour supprimer ou détruire le jeton généré lors de la connexion :

```javascript

// déconnexion
  const logout = () => {
    // détruire le cookie
    cookies.remove("TOKEN", { path: "/" });
  }


```

Redirigez l'utilisateur vers la page d'accueil avec le code suivant :

```javascript

// déconnexion
  const logout = () => {
    // détruire le cookie
    cookies.remove("TOKEN", { path: "/" });
    // rediriger l'utilisateur vers la page d'accueil
    window.location.href = "/";
  }


```

Ajoutez `className="text-center"` au parent `div` de `AuthComponent`, juste pour centrer toute la page. Vous pouvez maintenant le supprimer des autres endroits. Le fichier `AuthComponent.js` contient maintenant le contenu suivant :

```javascript

import React, { useEffect, useState } from "react";
import { Button } from "react-bootstrap";
import axios from "axios";
import Cookies from "universal-cookie";
const cookies = new Cookies();

// obtenir le jeton généré lors de la connexion
const token = cookies.get("TOKEN");

export default function AuthComponent() {
  // définir un état initial pour le message que nous recevrons après l'appel API
  const [message, setMessage] = useState("");

  // useEffect s'exécute automatiquement une fois que la page est complètement chargée
  useEffect(() => {
    // définir les configurations pour l'appel API ici
    const configuration = {
      method: "get",
      url: "https://nodejs-mongodb-auth-app.herokuapp.com/auth-endpoint",
      headers: {
        Authorization: `Bearer ${token}`,
      },
    };

    // faire l'appel API
    axios(configuration)
      .then((result) => {
        // attribuer le message dans notre résultat au message que nous avons initialisé ci-dessus
        setMessage(result.data.message);
      })
      .catch((error) => {
        error = new Error();
      });
  }, []);

  // déconnexion
  const logout = () => {
    // détruire le cookie
    cookies.remove("TOKEN", { path: "/" });
    // rediriger l'utilisateur vers la page d'accueil
    window.location.href = "/";
  }

  return (
    <div className="text-center">
      <h1>Composant d'authentification</h1>

      {/* afficher notre message de notre appel API */}
      <h3 className="text-danger">{message}</h3>

      {/* déconnexion */}
      <Button type="submit" variant="danger" onClick={() => logout()}>
        Déconnexion
      </Button>
    </div>
  );
}


```

Vous pouvez voir l'application fonctionnelle ci-dessous :

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/i/8b4g8m53ckqc7ns0tdo8.gif)

Et c'est tout pour l'authentification React !

Félicitations ! Vous êtes maintenant un pro de l'authentification React :)

## Comment héberger le Frontend

L'application React sera hébergée sur Netlify. Cela ne vous prendra que quelques étapes à configurer, alors suivez le guide :

Naviguez vers [https://app.netlify.com/signup](https://app.netlify.com/signup) et inscrivez-vous.

Suivez le processus jusqu'à ce que vous arriviez à votre tableau de bord.

Faites défiler un peu et vous arriverez à cet écran :

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/xehd8jio7ht4lsjqvb7p.JPG)

Vous pouvez glisser votre dossier de projet dans la boîte et votre hébergement sera fait ! Ou vous pouvez le connecter à votre dépôt distant.

L'avantage de se connecter à un dépôt distant est pour le déploiement continu. Vous n'aurez pas à refaire ces étapes si vous avez une raison de modifier votre application à l'avenir.

Donc, cliquez sur le bouton `New Site from Git`.

Choisissez la plateforme Git que vous souhaitez et accordez l'autorisation de la synchroniser avec votre application Netlify.

Choisissez le dépôt que vous souhaitez synchroniser.

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/5rxhv6iy5z5qo3ywgix4.JPG)

Cliquez sur le bouton `Deploy Site` sur la page vers laquelle vous êtes redirigé.

Attendez que votre site soit publié. Cela devrait prendre moins de 2 minutes. Après cela, vous pouvez maintenant cliquer sur le lien que vous voyez pour accéder à votre site.

Remarquez l'URL de votre site en haut de la page. Il s'agit d'une URL aléatoire qui vous est donnée par Netlify.

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/doakehth09usrxg6vv2f.JPG)

Vous pouvez la changer en cliquant sur le bouton `Site Settings`.

Dans la section `Site details`, cliquez sur le bouton `change site name`.

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/449x0ag7kwwmzwpcisu3.JPG)

Changez le nom et cliquez sur `Save`.


![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/4w4yaioa0wl9mw5hrei2.JPG)

Remarquez que le nom du site a été changé. Voici le mien ci-dessous :

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/kkojgyc0waxjn2ybq588.JPG)

Vous risquez de rencontrer le problème de redirection vers une autre page après l'hébergement. L'erreur peut ressembler à l'image ci-dessous :

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/12hi8shcwxyenvy1igar.JPG)

### Comment corriger l'erreur "Page Not Found"

Allez dans le dossier public de votre projet React.

Créez un fichier et nommez-le `_redirects`, et entrez le contenu suivant :

```

    /*  /index.html 200


```

Enregistrez et poussez vers la plateforme Git où votre application est hébergée.

Attendez un moment que l'application soit automatiquement publiée et tout devrait être bon.

![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/zuewuniqjhpa9u8mys3d.JPG)
_L'erreur a disparu_

Félicitations ! Vous êtes maintenant un ingénieur full-stack... :)

## Faisons un bilan

Cette section vous a aidé à connecter les utilisateurs au backend en construisant une interface utilisateur. Vous avez pu apprendre à connaître `React-Bootstrap`, `axios`, `React Hooks` et `react-router-dom`.

Vous avez commencé par une brève introduction à `React-Bootstrap` et dans cette partie, vous avez construit le formulaire d'inscription et de connexion.

Ensuite, vous avez connecté les formulaires à leurs points de terminaison respectifs et protégé certaines routes contre les utilisateurs non autorisés. Enfin, vous avez utilisé Netlify pour héberger l'application.

Tout le code de cette section peut être trouvé [ici](https://github.com/EBEREGIT/react-auth). Il est en direct sur Netlify [ici](https://react-auth-app.netlify.app/)

## Toutes les ressources et aperçus

#### Backend

* [Le code Node.js est ici](https://github.com/EBEREGIT/auth-backend)
* [Le backend est en direct ici](https://nodejs-mongodb-auth-app.herokuapp.com/)

#### Frontend

* [Le code React.js est ici](https://github.com/EBEREGIT/react-auth)
* [Le frontend est en direct ici](https://react-auth-app.netlify.app/)

## Conclusion

C'était un long tutoriel, mais j'espère qu'il était rempli de gemmes utiles à chaque étape. Et j'espère que vous avez apprécié le parcourir autant que j'ai apprécié le préparer. C'est mon désir sincère de réduire la barrière pour quiconque entre dans le domaine de la technologie.

Le but principal de ce tutoriel est d'enseigner à quiconque comment créer une authentification à la fois sur le backend et le frontend. Mais au-delà de cela, ce tutoriel est destiné à aider les débutants et les développeurs avancés qui cherchent à devenir des développeurs full-stack.

Les parties d'hébergement ajoutées à chaque section enseignent aux débutants comment rendre leurs projets publics. Lorsque vos projets sont publics et disponibles pour un aperçu, les recruteurs peuvent facilement accéder à ce que vous pouvez faire. Cela vous donne une meilleure chance de lutte lors du recrutement.

À ce stade, vous êtes sûr de continuer à gagner si vous continuez à construire. Rien ne peut plus vous arrêter.