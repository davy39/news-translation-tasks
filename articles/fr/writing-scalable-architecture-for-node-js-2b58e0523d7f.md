---
title: Écrire une architecture évolutive pour Node.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-04T01:36:32.000Z'
originalURL: https://freecodecamp.org/news/writing-scalable-architecture-for-node-js-2b58e0523d7f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*VR3E6lnDj4LuHhdM1sWFQw.jpeg
tags:
- name: Express.js
  slug: expressjs
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Écrire une architecture évolutive pour Node.js
seo_desc: 'By Zafar Saleem

  Writing backend logic for any project these days is pretty easy, thanks to full
  stack JavaScript. This is especially so with the introduction of dozens of frameworks
  for both client side and server side implementation.

  One of the most...'
---

Par Zafar Saleem

Écrire la logique backend pour n'importe quel projet de nos jours est assez facile, grâce à JavaScript full stack. Cela est particulièrement vrai avec l'introduction de dizaines de frameworks pour l'implémentation côté client et côté serveur.

L'un des frameworks Node.js les plus populaires est [Express.js](https://expressjs.com/). Il offre une approche facile pour construire des applications à différentes échelles. Cependant, à mesure qu'un projet grandit, il devient difficile de le faire évoluer à un certain point.

De nombreux développeurs ont tendance à continuer à ajouter de nouveaux fichiers de routes et de modèles pour de nouveaux services et points de terminaison API. Cette approche fonctionne, mais elle rend vraiment difficile pour les futurs ingénieurs de faire évoluer et d'ajouter de nouveaux services.

Dans ce blog, je vais construire un système de connexion et d'inscription qui utilise l'authentification JWT avec une architecture évolutive. Pour ceux qui préfèrent se lancer directement dans le code, allez-y et [clonez ce dépôt](https://github.com/zafar-saleem/NodeScalableArchitecture).

Il y aura quatre parties dans ce blog.

1. Configuration de l'architecture de base
2. Inscription
3. Connexion
4. Tableau de bord

Ce blog suppose que vous avez [déjà installé Node.js](https://nodejs.org/en/download/) sur votre système. Passons à la première étape — la configuration de l'architecture de base.

#### Configuration de l'architecture de base

Tout d'abord, créez un nouveau répertoire sur votre système de fichiers et appelez-le `auth` (ou ce que vous voulez).

```
mkdir auth
```

Maintenant, `cd` dans ce répertoire et créez un fichier package.json. Ajoutez les lignes ci-dessous dedans.

```
{    "name": "auth",    "version": "0.0.0",    "private": true,    "main": "index.js",    "scripts": {      "start": "node index.js"    },    "dependencies": {      "bcrypt": "latest",      "body-parser": "^1.18.2",      "cookie-parser": "~1.4.3",      "express": "~4.15.5",      "jsonwebtoken": "^8.1.1",      "mongoose": "^5.0.3",      "lodash": "^4.17.11",      "morgan": "^1.9.0",      "passport": "^0.4.0",      "passport-jwt": "^3.0.1",      "serve-favicon": "~2.4.5"    }  }
```

La partie la plus importante du fichier ci-dessus est la propriété `dependencies`. Ce sont les dépendances requises pour le projet. Elles seront utilisées comme middleware plus tard dans ce blog.

Maintenant, allez-y et exécutez la commande ci-dessous pour installer toutes ces dépendances. Vous devrez peut-être attendre quelques secondes.

```
npm install
```

Une fois qu'il a installé toutes les dépendances ci-dessus, allez-y et créez un fichier `index.js` dans votre dossier racine, comme ci-dessous :

```
touch index.js
```

Ce fichier particulier est uniquement responsable du démarrage du serveur. Pour ce faire, ajoutez le code ci-dessous dedans :

```
'use strict';
```

```
const server = require('./server')();const config = require('./configs');const db = require('./configs/db');
```

```
server.create(config, db);server.start();
```

Comme vous pouvez le voir, ce fichier nécessite trois fichiers :

1. server
2. config
3. db

Nous allons créer ceux-ci ensuite.

Le code ci-dessus appelle ensuite la méthode `create` sur le module serveur. Enfin, il appelle la méthode `start`, qui démarre le serveur.

#### 1. Créer le dossier `server`

```
mkdir server
```

Une fois terminé, `cd` dans ce dossier et créez un autre fichier `index.js`.

```
touch index.js
```

Maintenant, ajoutez le code ci-dessous dans ce fichier :

```
'use strict';
```

```
const express = require('express');const bodyParser = require('body-parser');const logger = require('morgan');const mongoose = require('mongoose');const passport = require('passport');const cookieParser = require('cookie-parser');
```

```
module.exports = function() {  let server = express(),      create,      start;
```

```
   create = function(config, db) {      let routes = require('./routes');
```

```
       // Paramètres du serveur       server.set('env', config.env);       server.set('port', config.port);       server.set('hostname', config.hostname);
```

```
       // Retourne le middleware qui analyse le json       server.use(bodyParser.json());       server.use(bodyParser.urlencoded({ extended: false }));       server.use(cookieParser());       server.use(logger('dev'));       server.use(passport.initialize());       mongoose.connect(db.database);       require('../configs/passport')(passport);
```

```
       // Configurer les routes       routes.init(server);   };
```

```
   start = function() {       let hostname = server.get('hostname'),       port = server.get('port');
```

```
       server.listen(port, function () {          console.log('Serveur Express à l'écoute sur - http://' + hostname + ':' + port);        });    };
```

```
    return {       create: create,       start: start    };};
```

Dans ce fichier, nous commençons par exiger toutes les dépendances nécessaires pour ce projet. Notez que d'autres dépendances peuvent être ajoutées à ce fichier chaque fois que nécessaire.

Ensuite, nous exportons une fonction anonyme de ce module en utilisant `module.exports`. À l'intérieur de cette fonction, créez trois variables : `server`, `create` et `start`.

La variable `server` est pour le serveur Express.js. Appelez donc la fonction `express()` et attribuez-la à `server`. Nous attribuerons des fonctions anonymes aux variables `create` et `start`.

Maintenant, il est temps d'écrire une fonction `create` avec deux paramètres : `config` et `db`.

Ensuite, définissez quelques paramètres de serveur en utilisant la fonction server.use() c'est-à-dire env, port et hostname. Ensuite, utilisez les middlewares `cookieParser, bodyParser, logger et passport`. Ensuite, connectez-vous à la base de données `mongoose` et enfin, exigez le fichier de configuration de passport et appelez-le avec le passport requis.

Le middleware Passport est utilisé pour l'authentification, que nous utiliserons plus tard dans ce blog. Pour en savoir plus à ce sujet, cliquez [ici](http://www.passportjs.org/).

Maintenant, il est temps pour les points de terminaison de l'API, c'est-à-dire les routes. Appelez simplement la fonction `init` sur les routes et passez `server` dedans.

Ensuite, écrivez la fonction `start`. Définissez `hostname` et `port` et démarrez le serveur avec la commande `listen` à l'intérieur de cette fonction.

Ensuite, retournez les fonctions `create` et `start` pour les rendre disponibles pour que d'autres modules les utilisent.

#### 2. Créer le dossier config

Au niveau racine, créez un dossier `configs` :

```
mkdir configs
```

`cd` dans ce dossier et créez un fichier index.js :

```
touch index.js
```

Ajoutez le code ci-dessous au fichier index.js :

```
'use strict';
```

```
const _ = require('lodash');const env = process.env.NODE_ENV || 'local';const envConfig = require('./' + env);
```

```
let defaultConfig = {  env: env};
```

```
module.exports = _.merge(defaultConfig, envConfig);
```

Maintenant, créez un fichier local.js :

```
touch local.js
```

Ouvrez-le et ajoutez le code ci-dessous :

```
'use strict';
```

```
let localConfig = {  hostname: 'localhost',  port: 3000};
```

```
module.exports = localConfig;
```

Celui-ci est simple aussi. Nous créons un objet `localConfig` et ajoutons quelques propriétés telles que `hostname` et `port`. Ensuite, nous l'exportons pour l'utiliser comme nous le faisons dans le fichier `./index.js`.

#### 3. Maintenant, créez une base de données

```
touch db.js
```

Ouvrez db.js dans votre éditeur préféré et collez le code ci-dessous dedans.

```
module.exports = {   'secret': 'putsomethingsecretehere',  'database': 'mongodb://127.0.0.1:27017/formediumblog'};
```

Nous exportons un objet JavaScript avec les propriétés `secret` et `database`. Ceux-ci sont utilisés pour se connecter à une base de données MongoDB en utilisant un middleware appelé mongoose.

### Construction de l'application

Maintenant que nous avons terminé la configuration de base de notre projet, il est temps pour les choses amusantes !

`cd` dans le dossier `server` et créez les dossiers suivants :

```
mkdir controllers models routes services
```

Tout d'abord, nous allons couvrir le dossier `routes`. Ce dossier est utilisé pour ajouter tous les points de terminaison qui sont disponibles pour une utilisation côté client. Tout d'abord, allez-y et créez le fichier `index.js` d'abord à l'intérieur du dossier `routes`.

```
touch index.js
```

Et mettez le code ci-dessous dans ce fichier :

```
'use strict';
```

```
const apiRoute = require('./apis');
```

```
function init(server) {  server.get('*', function (req, res, next) {    console.log('La requête a été faite à : ' + req.originalUrl);    return next();  });
```

```
  server.use('/api', apiRoute);}
```

```
module.exports = {  init: init};
```

Tout d'abord, exigez le dossier `apiRoute` que nous allons créer ensuite. Ce dossier contiendra un autre dossier avec le numéro de version de l'API, c'est-à-dire `v1`.

Deuxièmement, créez une fonction `init`. Nous appelons cette fonction depuis le fichier `server/index.js` à l'intérieur de la fonction `create` en bas et passons `server` comme paramètre. Il obtient simplement toutes les routes et retourne la fonction de rappel suivante.

Ensuite, utilisez le `apiRoute` que nous exigeons ci-dessus. Enfin, exportez la fonction init pour rendre cette fonction disponible dans le reste du projet.

Maintenant, allez-y et créez un dossier `apis`. À l'intérieur de ce dossier, créez un fichier `index.js`.

```
mkdir apistouch index.js
```

Collez le code ci-dessous dans le fichier `index.js`.

```
'use strict';
```

```
const express = require('express');const v1ApiController = require('./v1');
```

```
let router = express.Router();
```

```
router.use('/v1', v1ApiController);
```

```
module.exports = router;
```

Ce fichier exige `express` et le dossier de version de l'API, c'est-à-dire `v1`. Ensuite, créez le routeur et faites le point de terminaison `/v1` en utilisant la méthode `router.use()`. Enfin, exportez le routeur.

Il est temps de créer le fichier `apis/v1.js`. Collez le code ci-dessous dans le fichier `v1.js` :

```
'use strict';
```

```
const registerController = require('../../controllers/apis/register');const express = require('express');
```

```
let router = express.Router();
```

```
router.use('/register', registerController);
```

```
module.exports = router;
```

Nous devons enregistrer le contrôleur et express.js et créer un routeur. Ensuite, nous devons exposer les points de terminaison de l'API `register` pour une utilisation côté client. Enfin, nous devons exporter le routeur de ce module.

C'est le fichier que nous allons continuer à modifier. Nous aurons besoin de plus de contrôleurs ici lorsque nous les créerons.

Maintenant que nous avons terminé avec le dossier des routes, il est temps pour le dossier des contrôleurs. Allez-y et CD dans ce dossier et créez un dossier `apis`.

```
mkdir apis
```

Maintenant que nous avons le dossier apis à l'intérieur de `controllers`, nous allons créer les trois contrôleurs suivants et leurs services respectifs.

1. Configuration de l'architecture de base
2. **Inscription**
3. Connexion
4. Tableau de bord

Le premier est le `registerController`. Allez-y et créez le fichier ci-dessous.

```
touch register.js
```

Ouvrez ce fichier dans votre éditeur préféré et collez le code ci-dessous dedans :

```
'use strict';
```

```
const express = require('express');const registerService = require('../../services/authentication/register');
```

```
let router = express.Router();
```

```
router.post('/', registerService.registerUser);
```

```
module.exports = router;
```

Tout d'abord, il exige `express.js` et le service `register` (que nous allons écrire plus tard). Ensuite, créez un routeur en utilisant la méthode `express.Router()` et faites une requête post au chemin `'/'`. Ensuite, appelez la méthode registerUser sur registerService (que nous allons écrire plus tard). Enfin, exportez le routeur de ce module.

Maintenant, nous devons exiger ce contrôleur à l'intérieur du fichier `routes/apis/v1.js` que nous avons déjà fait.

Maintenant, l'enregistrement du contrôleur est terminé. Il est temps de passer au dossier `services`. CD dans ce dossier et créez un dossier `authentication`. Tout d'abord, cd dans `authentication` et créez un fichier `register.js`.

```
touch register.js
```

Ensuite, ouvrez le fichier `register.js` et collez le code ci-dessous dedans :

```
'use strict';
```

```
const express = require('express');const User = require('../../models/User');
```

```
const httpMessages = {  onValidationError: {    success: false,    message: 'Veuillez entrer un email et un mot de passe.'  },  onUserSaveError: {    success: false,    message: 'Cette adresse email existe déjà.'  },  onUserSaveSuccess: {    success: true,    message: 'Utilisateur créé avec succès.'  }}
```

```
// Inscrire de nouveaux utilisateursfunction registerUser(request, response) {  let { email, password } = request.body;
```

```
  if (!email || !password) {    response.json(httpMessages.onValidationError);  } else {    let newUser = new User({      email: email,      password: password    });
```

```
    // Tentative de sauvegarde de l'utilisateur    newUser.save(error => {      if (error) {        return response.json(httpMessages.onUserSaveError);      }      response.json(httpMessages.onUserSaveSuccess);    });  }}
```

```
module.exports = {  registerUser: registerUser};
```

Dans le service `register`, nous exigeons d'abord `expressjs` et le modèle `User`. Ensuite, nous créons un objet JavaScript, c'est-à-dire `httpMessages`, qui est essentiellement une liste de tous les messages que nous allons envoyer aux clients via l'API lorsque le client envoie la requête.

Ensuite, la fonction `registerUser` qui effectue réellement le processus d'inscription. Avant de sauvegarder l'utilisateur, il y a une vérification si l'utilisateur a fourni son email et son mot de passe. S'il l'a fait, créez un nouvel utilisateur en utilisant le mot-clé `new` avec l'email et le mot de passe fournis.

Ensuite, appelez simplement la fonction `save` sur `newUser` pour sauvegarder cet utilisateur dans la base de données et envoyez la réponse appropriée en utilisant `response.json`.

Enfin, exportez cette fonction en utilisant `module.exports` pour l'utiliser dans le reste du projet. Nous utilisons cela à l'intérieur du fichier `controllers/register.js`.

Avant de tester cela pour voir si cela fonctionne, nous devons d'abord créer un modèle `User`. Allez-y et créez un fichier `User.js` à l'intérieur du dossier `models`.

```
touch User.js
```

Et collez ce code dans le fichier ci-dessus :

```
const mongoose = require('mongoose');const bcrypt = require('bcrypt');
```

```
const UserSchema = new mongoose.Schema({  email: {    type: String,    lowercase: true,    unique: true,    required: true  },  password: {    type: String,    required: true  },  role: {    type: String,    enum: ['Client', 'Manager', 'Admin'],    default: 'Client'  }});
```

```
UserSchema.pre('save', function(next) {  let user = this;
```

```
   if (this.isModified('password') || this.isNew) {      bcrypt.genSalt(10, (err, salt) => {        if (err) {          console.log(err);          return next(err);        }
```

```
        bcrypt.hash(user.password, salt, (err, hash) => {          if (err) {            console.log(err);            return next(err);          }
```

```
          user.password = hash;          next();        });      });  } else {    return next();  }});
```

```
// Créer une méthode pour comparer le mot de passe saisi avec le mot de passe sauvegardé dans la base de donnéesUserSchema.methods.comparePassword = function(pw, cb) {  bcrypt.compare(pw, this.password, function(err, isMatch) {    if (err) {      return cb(err);    }
```

```
    cb(null, isMatch);  });};
```

```
module.exports = mongoose.model('User', UserSchema);
```

Tout d'abord, exigez les modules `mongoose` et `bcrypt`. Mongoose est utilisé pour créer un schéma mongodb tandis que bcrypt est utilisé pour crypter les mots de passe avant de les stocker dans la base de données.

Créez `UserSchema` avec les propriétés `email, password et role`. Ensuite, avant de sauvegarder l'utilisateur, effectuez quelques vérifications avant de hacher le mot de passe.

La fonction finale est de comparer les mots de passe. Elle compare le mot de passe de l'utilisateur avec le mot de passe haché dans la base de données.

Maintenant, afin de tester ce code, ouvrez postman (si vous n'avez pas installé postman, allez-y et installez-le depuis [ici](https://www.getpostman.com/)). Ouvrez postman et entrez l'URL ci-dessous :

```
http://localhost:3000/api/v1/register
```

Sélectionnez POST comme requête, choisissez l'onglet body et `form-urlencoded` et entrez l'email et le mot de passe. Appuyez sur le bouton envoyer et vous devriez voir le message de succès ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/v24ai9wIGdPv0m2RrvssyzNtBa1c3MK1yA3k)

Maintenant, la partie inscription est terminée.

1. Configuration de l'architecture de base
2. Inscription
3. **Connexion**
4. Tableau de bord

Il est temps de se concentrer sur la connexion. Créez un fichier `login.js` à l'intérieur du dossier `controllers`.

```
touch login.js
```

Maintenant, ouvrez-le et collez le code ci-dessous :

```
'use strict';
```

```
const express = require('express');const loginService = require('../../services/authentication/login');
```

```
let router = express.Router();
```

```
router.post('/', loginService.loginUser);
```

```
module.exports = router;
```

Encore une fois, c'est simple et identique au module d'inscription : après avoir importé `express.js` et `loginService`, nous créons le routeur et faisons une requête post au chemin racine `'/'` avec la fonction de rappel `loginUser` sur `loginService`. Enfin, exportez le routeur.

Il est temps d'exiger `loginController` dans le fichier `routes/apis/v1.js`. Votre fichier `v1.js` devrait maintenant ressembler à ceci.

```
'use strict';
```

```
const registerController = require('../../controllers/apis/register');const loginController = require('../../controllers/apis/login');
```

```
const express = require('express');
```

```
let router = express.Router();
```

```
router.use('/register', registerController);router.use('/login', loginController);
```

```
module.exports = router;
```

Maintenant, pour le service de connexion, créez un fichier `login.js` à l'intérieur de `services/authentication/` :

```
touch login.js
```

Et collez le code ci-dessous dans ce fichier :

```
'use strict';
```

```
const express = require('express');const apiRoutes = express.Router();
```

```
const jwt = require('jsonwebtoken');const passport = require('passport');const db = require('../../../configs/db');
```

```
const User = require('../../models/User');
```

```
const httpResponse = {  onUserNotFound: {    success: false,    message: 'Utilisateur non trouvé.'  },  onAuthenticationFail: {    success: false,    message: 'Les mots de passe ne correspondent pas.'  }}
```

```
function loginUser(request, response) {   let { email, password } = request.body;
```

```
User.findOne({    email: email  }, function(error, user) {    if (error) throw error;
```

```
    if (!user) {      return response.send(httpResponse.onUserNotFound);    }
```

```
    // Vérifier si le mot de passe correspond    user.comparePassword(password, function(error, isMatch) {      if (isMatch && !error) {        var token = jwt.sign(user.toJSON(), db.secret, {           expiresIn: 10080        });
```

```
        return response.json({           success: true, token: 'JWT ' + token        });      }
```

```
      response.send(httpResponse.onAuthenticationFail);    });  });};
```

```
module.exports = {  loginUser: loginUser};
```

Tout d'abord, exigez certains modules nécessaires tels que : `express.js, jsonwebtoken, passport, db et User model`. Créez un objet JavaScript qui contient une liste de messages à envoyer au côté client lorsque la requête http est faite à ce service.

Créez une fonction loginUser, et à l'intérieur de celle-ci, créez quelques variables, c'est-à-dire email et password, et attribuez l'email et le mot de passe envoyés par l'utilisateur à ces variables qui se trouvent dans `request.body`.

Ensuite, utilisez la méthode `findOne()` sur le modèle `User` pour trouver un utilisateur basé sur l'email envoyé par le client par l'utilisateur. La fonction de rappel de `findOne()` accepte 2 paramètres, `error et user`. Vérifiez d'abord si la méthode `findOne()` ci-dessus lance une erreur — si c'est le cas, lancez une erreur.

Ensuite, effectuez une vérification : si aucun utilisateur n'est trouvé, envoyez la réponse appropriée avec un message de la liste des messages que nous avons déclarés ci-dessus dans ce module.

Ensuite, comparez le mot de passe que l'utilisateur a envoyé avec celui dans la base de données en utilisant la fonction `compare` que nous avons écrite dans le modèle `User` plus tôt dans ce blog.

Si le mot de passe correspond et qu'il ne retourne pas d'erreur, alors nous créons un token en utilisant le module `jsonwebtoken` et retournons ce token en utilisant `json.response()` au client. Sinon, nous envoyons un message `authenticationFail`.

Enfin, exportez la fonction `loginUser` avec `exports.module` afin que nous puissions l'utiliser dans nos contrôleurs et ailleurs.

Il est temps de tester la fonctionnalité de connexion. Retournez à postman et cette fois remplacez `register` par `login` comme point de terminaison de l'API dans l'URL. Entrez l'email et le mot de passe et appuyez sur le bouton envoyer. Vous devriez pouvoir recevoir un token. Allez-y et copiez-le dans le presse-papiers car vous l'utiliserez plus tard pour accéder au tableau de bord.

![Image](https://cdn-media-1.freecodecamp.org/images/NgY6nezWpJkKbuOU7555pCd4abpZBNzzPvBd)

1. Configuration de l'architecture de base
2. Inscription
3. Connexion
4. **Tableau de bord**

Maintenant, il est temps pour le fichier `dashboard.js`. Créez le fichier `dashboard.js` à l'intérieur du dossier `controllers`.

```
touch dashboard.js
```

Et ouvrez-le et collez le code ci-dessous :

```
'use strict';
```

```
const passport = require('passport');const express = require('express');const dashboardService = require('../../services/dashboard/dashboard');
```

```
let router = express.Router();
```

```
router.get('/', passport.authenticate('jwt', { session: false }), dashboardService.getDashboard);
```

```
module.exports = router;
```

Ce contrôleur est différent dans le sens où il nécessite un accès authentifié. C'est-à-dire qu'un seul utilisateur connecté peut accéder au service de tableau de bord et faire différentes requêtes http.

Pour cette raison, nous importons également passport, et pour la requête get, nous utilisons la fonction `passport.authenticate()` pour accéder au service `getDashboard`.

Encore une fois, nous devons exiger `dashboardController` dans le fichier `routes/apis/v1.js`. Votre fichier `v1.js` devrait ressembler à ceci :

```
'use strict';
```

```
const registerController = require('../../controllers/apis/register');const loginController = require('../../controllers/apis/login');const dashboardController = require('../../controllers/apis/dashboard');
```

```
const express = require('express');
```

```
let router = express.Router();
```

```
router.use('/register', registerController);router.use('/login', loginController);router.use('/dashboard', dashboardController);
```

```
module.exports = router;
```

Maintenant que `dashboardController` est disponible pour être utilisé pour les requêtes côté client, il est temps de créer son service respectif. Allez dans le dossier des services et créez un dossier `dashboard` à l'intérieur. Créez un fichier `dashboard.js` et mettez le code ci-dessous dans ce fichier.

```
'use strict';
```

```
function getDashboard(request, response) {  response.json('Ceci vient du tableau de bord');}
```

```
module.exports = {  getDashboard: getDashboard}
```

Pas de choses fantaisistes. À des fins de démonstration, je réponds simplement avec un message texte `Ceci vient du tableau de bord`. Ensuite, exportez cette méthode pour qu'elle soit utilisée dans son contrôleur respectif, ce que nous avons déjà accompli.

Maintenant, il est temps de tester. Ouvrez postman et changez le point de terminaison de l'URL pour le tableau de bord. Cliquez sur l'onglet headers et ajoutez `Authorization` et collez le JTW copié à l'étape précédente lorsque vous vous êtes connecté.

![Image](https://cdn-media-1.freecodecamp.org/images/cQtptcZskXGs8nrmEPsRlDuRxsJjxv5a9gE1)

Vous devriez voir le message `Ceci vient du tableau de bord` comme réponse.

Comme vous pouvez le voir, lorsque nous créons un nouveau service, nous avons besoin d'un contrôleur pour celui-ci et nous pouvons continuer à ajouter de nouveaux services à l'architecture. Si vous souhaitez changer la version de l'API et également conserver la version actuelle, ajoutez simplement un nouveau fichier `v2.js` et redirigez toutes les requêtes vers ce point de terminaison. C'est un exemple simple.

J'espère que vous avez aimé ce blog et je vous vois la prochaine fois.

MISE À JOUR : Si vous souhaitez implémenter son côté client, veuillez [cliquer ici](https://medium.com/@zafarsaleem/login-using-react-redux-redux-saga-86b26c8180e) où j'ai utilisé react.js pour m'authentifier avec ce serveur.