---
title: Comment authentifier les utilisateurs et implémenter CORS dans les applications
  Node.js
subtitle: ''
author: Idris Olubisi
co_authors: []
series: null
date: '2021-07-06T16:02:13.000Z'
originalURL: https://freecodecamp.org/news/how-to-authenticate-users-and-implement-cors-in-nodejs-applications
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/Screenshot-2021-06-27-at-00.10.45.png
tags:
- name: authentication
  slug: authentication
- name: authorization
  slug: authorization
- name: CORS
  slug: cors
- name: node
  slug: node
seo_title: Comment authentifier les utilisateurs et implémenter CORS dans les applications
  Node.js
seo_desc: 'In this tutorial, you will learn how to authenticate users and secure endpoints
  in Node.js. You''ll also see how to implement Cross-Origin Resource Sharing (CORS)
  in Node. So let''s get started.

  Prerequisites

  You''ll need the following to follow along w...'
---

Dans ce tutoriel, vous apprendrez comment authentifier les utilisateurs et sécuriser les endpoints dans Node.js. Vous verrez également comment implémenter le partage de ressources cross-origin (CORS) dans Node. Alors, commençons.

### Prérequis

Vous aurez besoin des éléments suivants pour suivre ce tutoriel : 
- Une compréhension fonctionnelle de JavaScript.
- Une bonne compréhension de Node.js.
- Une connaissance pratique de MongoDB ou d'une autre base de données de votre choix.
- [Postman](https://www.postman.com/) et une compréhension basique de son fonctionnement.

Avant de plonger dans la partie principale de l'article, définissons quelques termes pour que nous soyons tous sur la même longueur d'onde.

## Qu'est-ce que l'authentification ?

L'authentification et l'autorisation peuvent sembler être la même chose. Mais il y a une grande différence entre entrer dans une maison (authentification) et ce que vous pouvez faire une fois que vous y êtes (autorisation).

L'authentification est le processus de confirmation de l'identité d'un utilisateur en obtenant des identifiants et en utilisant ces identifiants pour valider leur identité. Si les certificats sont valides, la procédure d'autorisation commence.

Vous êtes probablement déjà familier avec le processus d'authentification, car nous y sommes tous confrontés quotidiennement – que ce soit au travail (connexion à votre ordinateur) ou à la maison (mots de passe ou connexion à un site web). En fait, la plupart des "choses" connectées à Internet nécessitent que vous fournissiez des identifiants pour prouver votre identité.

## Qu'est-ce que l'autorisation ?

L'autorisation est le processus d'octroi aux utilisateurs authentifiés de l'accès aux ressources en vérifiant s'ils ont ou non des permissions d'accès au système. Elle permet également de restreindre les privilèges d'accès en accordant ou en refusant des licences spécifiques aux utilisateurs authentifiés.

Après que le système ait authentifié votre identité, l'autorisation se produit, vous donnant un accès complet aux ressources telles que les informations, les fichiers, les bases de données, les finances, les emplacements, et tout autre élément. 

Cette approbation impacte votre capacité à accéder au système et l'étendue à laquelle vous pouvez le faire.

## Qu'est-ce que le partage de ressources cross-origin (CORS) ?

>[CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) est un système basé sur les en-têtes HTTP qui permet à un serveur de spécifier toute autre origine (domaine, schéma ou port) à partir de laquelle un navigateur doit permettre le chargement de ressources autres que les siennes.

CORS utilise également un système dans lequel les navigateurs envoient une requête "preflight" au serveur hébergeant l'aide cross-origin pour s'assurer qu'il permettra la requête réelle.

Nous utiliserons la norme des jetons web JSON pour représenter les revendications entre deux parties.

## Qu'est-ce que les jetons web JSON (JWT) ?

> Les jetons web JSON (JWT) sont une norme industrielle ouverte définie par la RFC 7519 utilisée pour représenter des revendications entre deux parties. [jwt.io](https://jwt.io/introduction) 

Vous pouvez utiliser [jwt.io](https://jwt.io) pour décoder, vérifier et créer des JWT, par exemple.

JWT définit une manière concise et autonome d'échanger des informations entre deux parties sous forme d'objet JSON. Vous pouvez examiner et faire confiance à ces informations car elles sont signées. 

Les JWT peuvent être signés avec un secret (en utilisant l'algorithme HMAC) ou une paire de clés publique/privée de RSA ou ECDSA. Nous verrons quelques exemples de leur utilisation un peu plus tard.

Commençons.

## Comment utiliser un jeton pour l'authentification dans le développement Node.js 

Pour commencer, nous devons d'abord configurer notre projet.

Naviguez vers un répertoire de votre choix sur votre machine et ouvrez-le dans le terminal pour lancer Visual Studio Code.

Ensuite, exécutez :

```bash
code .
```

> **Note** : Si vous n'avez pas Visual Studio Code installé sur votre ordinateur, `code .` ne fonctionnera pas. Assurez-vous simplement de l'avoir installé avant d'essayer cette commande.


### Comment créer un répertoire et le configurer avec `npm`

Créez un répertoire et initialisez `npm` en tapant la commande suivante :

- Dans Windows PowerShell :

```bash
mkdir cors-auth-project

cd cors-auth-project

npm init -y
```

- Dans Linux :

```bash
mkdir cors-auth-project

cd cors-auth-project

npm init -y
```

### Comment créer des fichiers et des répertoires

Dans l'étape précédente, nous avons initialisé npm avec la commande `npm init -y`, qui a automatiquement créé un fichier package.json.

Nous allons créer les répertoires `model`, `middleware` et `config` ainsi que leurs fichiers, par exemple, `user.js`, `auth.js`, `database.js` en utilisant les commandes ci-dessous.

```bash
mkdir model middleware config

touch config/database.js middleware/auth.js model/user.js
```

Nous pouvons maintenant créer les fichiers `index.js` et `app.js` dans le répertoire racine de notre projet avec cette commande :

```bash
touch app.js index.js
```

Cela nous donnera une structure de dossier comme celle que vous voyez ci-dessous :

![structure de dossier](https://www.freecodecamp.org/news/content/images/2021/06/Screenshot-2021-06-26-at-19.43.15.png)


### Comment installer les dépendances

Nous installerons plusieurs dépendances comme `mongoose`, `jsonwebtoken`, `express`, `dotenv`, `bcryptjs`, `cors` et des dépendances de développement comme `nodemon` pour redémarrer le serveur automatiquement lorsque nous apportons des modifications.

Puisque j'utiliserai MongoDB dans ce projet, nous installerons Mongoose, et les identifiants de l'utilisateur seront vérifiés par rapport à ce que nous avons dans notre base de données. Par conséquent, l'ensemble du processus d'authentification n'est pas limité à la base de données que nous utiliserons dans ce tutoriel.

```bash
npm install cors mongoose express jsonwebtoken dotenv bcryptjs 

npm install nodemon -D
```

### Comment créer un serveur Node.js et connecter votre base de données

Maintenant, ajoutez les extraits suivants à vos fichiers `app.js`, `index.js`, `database.js` et `.env` dans cet ordre pour établir notre serveur Node.js et connecter notre base de données.

Dans notre `database.js` :

`config/database.js` :
```javascript
const mongoose = require("mongoose");

const { MONGO_URI } = process.env;

exports.connect = () => {
  // Connexion à la base de données
  mongoose
    .connect(MONGO_URI, {
      useNewUrlParser: true,
      useUnifiedTopology: true,
      useCreateIndex: true,
      useFindAndModify: false,
    })
    .then(() => {
      console.log("Connecté avec succès à la base de données");
    })
    .catch((error) => {
      console.log("La connexion à la base de données a échoué. Sortie maintenant...");
      console.error(error);
      process.exit(1);
    });
};
```

Dans notre `app.js` :

`auth-cors-project/app.js`
```javascript
require("dotenv").config();
require("./config/database").connect();
const express = require("express");

const app = express();

app.use(express.json());

// La logique va ici

module.exports = app;
```

Dans notre `index.js` :

`auth-cors-project/index.js`
```javascript
const http = require("http");
const app = require("./app");
const server = http.createServer(app);

const { API_PORT } = process.env;
const port = process.env.PORT || API_PORT;

// serveur en écoute 
server.listen(port, () => {
  console.log(`Serveur en cours d'exécution sur le port ${port}`);
});
```

Notre fichier, comme vous pouvez le voir, nécessite diverses variables d'environnement. Si vous ne l'avez pas déjà fait, créez un nouveau fichier `.env` et ajoutez vos variables avant d'exécuter l'application.

Dans notre `.env` :

```javascript
API_PORT=4001

MONGO_URI= // Votre URI de base de données
```

Modifiez l'objet scripts dans notre `package.json` pour qu'il ressemble à celui ci-dessous afin de démarrer notre serveur.

```javascript
"scripts": {
    "start": "node index.js",
    "dev": "nodemon index.js",
    "test": "echo \"Erreur : aucun test spécifié\" && exit 1"
  }
```

Nous avons réussi à insérer l'extrait ci-dessus dans les fichiers `app.js`, `index.js` et `database.js`. Nous avons donc commencé par créer notre serveur Node.js dans `index.js`, puis nous avons importé le fichier `app.js`, qui avait déjà des routes configurées.

Ensuite, dans database.js, nous avons utilisé Mongoose pour établir une connexion à la base de données.

`npm run dev` est la commande pour démarrer notre application.

Tant qu'ils n'ont pas planté, le serveur et la base de données devraient être en cours d'exécution.

### Comment créer un modèle d'utilisateur et une route

Après l'inscription pour la première fois, nous établirons notre schéma pour les détails de l'utilisateur. Ensuite, lors de la connexion, nous les vérifierons par rapport aux identifiants mémorisés.

Dans le dossier model, ajoutez l'extrait suivant à `user.js` :

`model/user.js`

```javascript
const mongoose = require("mongoose");

const userSchema = new mongoose.Schema({
  first_name: { type: String, default: null },
  last_name: { type: String, default: null },
  email: { type: String, unique: true },
  password: { type: String },
  token: { type: String },
});

module.exports = mongoose.model("user", userSchema);
```

Maintenant, créons les routes pour `register` et `login`, respectivement.

Dans `app.js` dans le répertoire racine, ajoutez l'extrait suivant pour l'inscription et la connexion.

`app.js`
```javascript
// importation du contexte utilisateur
const User = require("./model/user");

// Inscription
app.post("/register", (req, res) => {
// notre logique d'inscription va ici...
});

// Connexion
app.post("/login", (req, res) => {
// notre logique de connexion va ici
});
```

### Comment implémenter les fonctionnalités d'inscription et de connexion

Nous allons implémenter ces deux routes dans notre application. Avant de stocker les identifiants dans notre base de données, nous utiliserons JWT pour les signer et `bycrypt` pour les chiffrer.

Nous allons : 
- Obtenir les entrées de l'utilisateur à partir de la route `/register`.
- Vérifier les entrées de l'utilisateur.
- Vérifier si l'utilisateur a déjà été créé.
- Protéger le mot de passe de l'utilisateur en le chiffrant.
- Créer un compte utilisateur dans notre base de données.
- Enfin, construire un jeton JWT signé.

Modifiez la structure de la route `/register` que nous avons créée précédemment pour qu'elle ressemble à ce qui est montré ci-dessous :

`app.js`
```javascript
// ...

app.post("/register", async (req, res) => {

  // Notre logique d'inscription commence ici
   try {
    // Obtenir les entrées de l'utilisateur
    const { firstName, lastName, email, password } = req.body;

    // Valider les entrées de l'utilisateur
    if (!(email && password && firstName && lastName)) {
      res.status(400).send("Toutes les entrées sont requises");
    }

    // vérifier si l'utilisateur existe déjà
    // Valider si l'utilisateur existe dans notre base de données
    const oldUser = await User.findOne({ email });

    if (oldUser) {
      return res.status(409).send("L'utilisateur existe déjà. Veuillez vous connecter");
    }

    // Chiffrer le mot de passe de l'utilisateur
    encryptedUserPassword = await bcrypt.hash(password, 10);

    // Créer l'utilisateur dans notre base de données
    const user = await User.create({
      first_name: firstName,
      last_name: lastName,
      email: email.toLowerCase(), // sanitize
      password: encryptedUserPassword,
    });

    // Créer un jeton
    const token = jwt.sign(
      { user_id: user._id, email },
      process.env.TOKEN_KEY,
      {
        expiresIn: "5h",
      }
    );
    // sauvegarder le jeton de l'utilisateur
    user.token = token;

    // retourner le nouvel utilisateur
    res.status(201).json(user);
  } catch (err) {
    console.log(err);
  }
  // Notre logique d'inscription se termine ici
});

// ...
```

> **Note** : Mettez à jour votre fichier `.env` avec une `TOKEN_KEY`, qui peut être une chaîne aléatoire.

En utilisant Postman pour tester l'endpoint, nous obtiendrons la réponse montrée ci-dessous après une inscription réussie.

![inscription de l'utilisateur](https://www.freecodecamp.org/news/content/images/2021/06/Screenshot-2021-06-26-at-22.57.16.png)

Nous allons : 
- Obtenir les entrées de l'utilisateur pour la route `/login`.
- Vérifier les entrées de l'utilisateur.
- Vérifier si l'utilisateur est authentique.
- Comparer le mot de passe de l'utilisateur à celui que nous avons sauvegardé précédemment dans notre base de données.
- Enfin, construire un jeton JWT signé.

Faites en sorte que la structure de la route `/login` que nous avons définie précédemment ressemble à ceci :

```javascript
// ...

app.post("/login", async (req, res) => {

  // Notre logique de connexion commence ici
   try {
    // Obtenir les entrées de l'utilisateur
    const { email, password } = req.body;

    // Valider les entrées de l'utilisateur
    if (!(email && password)) {
      res.status(400).send("Toutes les entrées sont requises");
    }
    // Valider si l'utilisateur existe dans notre base de données
    const user = await User.findOne({ email });

    if (user && (await bcrypt.compare(password, user.password))) {
      // Créer un jeton
      const token = jwt.sign(
        { user_id: user._id, email },
        process.env.TOKEN_KEY,
        {
          expiresIn: "5h",
        }
      );

      // sauvegarder le jeton de l'utilisateur
      user.token = token;

      // utilisateur
      return res.status(200).json(user);
    }
    return res.status(400).send("Identifiants invalides");
    
  // Notre logique de connexion se termine ici
});

// ...
```

En utilisant Postman pour tester, nous obtiendrons la réponse montrée ci-dessous après une connexion réussie.

![connexion de l'utilisateur](https://www.freecodecamp.org/news/content/images/2021/06/Screenshot-2021-06-26-at-23.00.45.png)

### Comment créer un middleware pour l'authentification

Nous pouvons maintenant créer et connecter un utilisateur avec succès. Maintenant, nous allons établir une route qui nécessite un jeton utilisateur dans l'en-tête, qui sera le jeton JWT que nous avons créé précédemment.

Ajoutez l'extrait suivant à l'intérieur de `auth.js` :

`middleware/auth.js`
```javascript
const jwt = require("jsonwebtoken");

const config = process.env;

const verifyToken = (req, res, next) => {
  const token =
    req.body.token || req.query.token || req.headers["x-access-token"];

  if (!token) {
    return res.status(403).send("Un jeton est requis pour l'authentification");
  }
  try {
    const decoded = jwt.verify(token, config.TOKEN_KEY);
    req.user = decoded;
  } catch (err) {
    return res.status(401).send("Jeton invalide");
  }
  return next();
};

module.exports = verifyToken;
```

Pour tester le middleware, créez la route `/welcome` et modifiez app.js avec le code suivant :

`app.js`
```javascript
const auth = require("./middleware/auth");

app.post("/welcome", auth, (req, res) => {
  res.status(200).send("Bienvenue chez FreeCodeCamp 👌");
});
```

Lorsque nous essayons d'accéder à la route /welcome que nous venons de créer sans envoyer de jeton dans l'en-tête avec la clé x-access-token, nous obtenons la réponse suivante :

![réponse échouée](https://www.freecodecamp.org/news/content/images/2021/06/Screenshot-2021-06-26-at-23.09.13.png)

Nous pouvons maintenant re-tester en ajoutant un jeton dans l'en-tête avec la clé x-access-token.

Voici la réponse que vous obtiendrez :

![réponse réussie](https://www.freecodecamp.org/news/content/images/2021/06/success-response.png)

## Comment implémenter le partage de ressources cross-origin (CORS)

[CORS](https://www.npmjs.com/package/cors) est un package Node.js qui fournit un middleware Connect/Express que vous pouvez utiliser pour activer CORS avec une variété de paramètres.

1. Il est facile à utiliser (Activer toutes les requêtes CORS)

L'ajout de l'extrait suivant à `app.js` nous permet d'ajouter CORS à notre application et d'activer toutes les requêtes CORS.

```
// ...

const cors = require("cors") // Nouvellement ajouté
const app = express();

app.use(cors()) // Nouvellement ajouté


app.use(express.json({ limit: "50mb" }));

// ...
```

2. Vous pouvez activer CORS pour une seule route

En utilisant la route `/welcome` comme exemple, vous pouvez activer CORS pour une seule route dans votre application en ajoutant l'extrait suivant dans `app.js` :

```
app.get('/welcome', cors(), auth, (req, res) => {
  res.status(200).send("Bienvenue chez FreeCodeCamp 👌 ");
});
```

3. Comment configurer CORS

Nous pouvons définir des options dans le package CORS en ajoutant des paramètres pour le configurer, comme montré ci-dessous :

```
// ...

const corsOptions = {
  origin: 'http://example.com',
  optionsSuccessStatus: 200 // pour certains navigateurs hérités
}

app.get('/welcome', cors(corsOptions), auth, (req, res) => {
  res.status(200).send("Bienvenue chez FreeCodeCamp 👌 ");
});

// ...
```

Vous pouvez consulter [NPM CORS PACKAGE](https://www.npmjs.com/package/cors) pour en savoir plus sur le partage de ressources cross-origin.

Vous pouvez [cliquer ici](https://github.com/Olanetsoft/auth-cors-demo) pour consulter le code complet sur GitHub.

## Conclusion

Dans cet article, nous avons appris ce qu'est JWT, l'authentification, l'autorisation et CORS. Nous avons également appris comment créer une API dans Node.js qui utilise un jeton JWT pour l'authentification.

Merci d'avoir lu !