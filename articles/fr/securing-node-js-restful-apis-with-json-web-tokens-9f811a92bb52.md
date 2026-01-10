---
title: Sécuriser les API RESTful Node.js avec les JSON Web Tokens
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-09-04T19:52:59.000Z'
originalURL: https://freecodecamp.org/news/securing-node-js-restful-apis-with-json-web-tokens-9f811a92bb52
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0ABaK4SrXGUnXgmXqMkZtA.png
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: Web Development
  slug: web-development
seo_title: Sécuriser les API RESTful Node.js avec les JSON Web Tokens
seo_desc: 'By Adnan Rahić

  Have you ever wondered how authentication works? What’s behind all the complexity
  and abstractions. Actually, nothing special. It’s a way of encrypting a value, in
  turn creating a unique token that users use as an identifier. This toke...'
---

Par Adnan Rahić

Vous êtes-vous déjà demandé comment fonctionne l'authentification ? Qu'y a-t-il derrière toute cette complexité et ces abstractions ? En réalité, rien de spécial. C'est une manière de chiffrer une valeur, créant ainsi un jeton unique que les utilisateurs utilisent comme identifiant. Ce jeton vérifie votre identité. Il peut authentifier qui vous êtes et autoriser l'accès à diverses ressources. Si par hasard vous ne connaissez pas ces termes, soyez patient, je vais tout expliquer ci-dessous.

Ce sera un tutoriel étape par étape sur la manière d'ajouter une authentification basée sur des jetons à une API REST existante. La stratégie d'authentification en question est JWT (JSON Web Token). Si cela ne vous dit rien, ce n'est pas grave. C'était tout aussi étrange pour moi lorsque j'ai entendu ce terme pour la première fois.

Que signifie réellement JWT d'un point de vue terre-à-terre ? Décomposons ce que dit la définition officielle :

> JSON Web Token (JWT) est un moyen compact et sécurisé pour les URL de représenter des revendications à transférer entre deux parties. Les revendications dans un JWT sont encodées sous forme d'objet JSON qui est utilisé comme charge utile d'une structure JSON Web Signature (JWS) ou comme texte en clair d'une structure JSON Web Encryption (JWE), permettant aux revendications d'être signées numériquement ou protégées en intégrité avec un Message Authentication Code (MAC) et/ou chiffrées.  
> - [**Internet Engineering Task Force (IETF)**](https://tools.ietf.org/html/rfc7519)

C'était un peu long. Traduisons cela en français. Un JWT est une chaîne de caractères encodée qui est sûre à envoyer entre deux ordinateurs s'ils utilisent tous deux HTTPS. Le jeton représente une valeur accessible uniquement par l'ordinateur qui a accès à la clé secrète avec laquelle il a été chiffré. Assez simple, n'est-ce pas ?

À quoi cela ressemble-t-il dans la vie réelle ? Supposons qu'un utilisateur souhaite se connecter à son compte. Il envoie une requête avec les informations d'identification requises, telles que l'email et le mot de passe, au serveur. Le serveur vérifie si les informations d'identification sont valides. Si c'est le cas, le serveur crée un jeton en utilisant la charge utile souhaitée et une clé secrète. Cette chaîne de caractères résultant du chiffrement est appelée un jeton. Ensuite, le serveur le renvoie au client. Le client, à son tour, enregistre le jeton pour l'utiliser dans chaque autre requête que l'utilisateur enverra. La pratique consistant à ajouter un jeton aux en-têtes de requête est une manière d'autoriser l'utilisateur à accéder aux ressources. Voici un exemple pratique de fonctionnement de JWT.

D'accord, assez parlé ! Le reste de ce tutoriel sera consacré au codage, et j'aimerais que vous suiviez et codiez avec moi au fur et à mesure. Chaque extrait de code sera suivi d'une explication. Je pense que la meilleure façon de bien comprendre est de le coder vous-même en cours de route.

Avant de commencer, il y a quelques choses que vous devez savoir sur Node.js et certaines normes EcmaScript que j'utiliserai. Je n'utiliserai pas ES6, car il n'est pas aussi convivial pour les débutants que JavaScript traditionnel. Mais je m'attendrai à ce que vous sachiez déjà comment construire une API RESTful avec Node.js. Si ce n'est pas le cas, vous pouvez faire un détour et [consulter ceci](https://hackernoon.com/restful-api-design-with-node-js-26ccf66eab09) avant de continuer.

De plus, [toute la démonstration est sur GitHub](https://github.com/adnanrahic/securing-restful-apis-with-jwt) si vous souhaitez la voir dans son intégralité.

### Commençons à écrire du code, d'accord ?

Eh bien, pas encore en fait. Nous devons d'abord configurer l'environnement. Le code devra attendre au moins quelques minutes de plus. Cette partie est ennuyeuse, alors pour démarrer rapidement, nous allons cloner le dépôt du tutoriel ci-dessus. Ouvrez une fenêtre de terminal ou une invite de commande et exécutez cette commande :

```bash
git clone https://github.com/adnanrahic/nodejs-restful-api.git
```

Vous verrez un dossier apparaître, ouvrez-le. Jetons un coup d'œil à la structure du dossier.

```bash
> user
  - User.js
  - UserController.js
- db.js
- server.js
- app.js
- package.json
```

Nous avons un dossier utilisateur avec un modèle et un contrôleur, et un CRUD de base déjà implémenté. Notre fichier **app.js** contient la configuration de base. Le fichier **db.js** garantit que l'application se connecte à la base de données. Le fichier **server.js** garantit que notre serveur démarre.

Allez-y et installez tous les modules Node requis. Revenez à votre fenêtre de terminal. Assurez-vous d'être dans le dossier nommé '_nodejs-restful-api_' et exécutez `npm install`. Attendez une seconde ou deux pour que les modules s'installent. Maintenant, vous devez ajouter une chaîne de connexion à la base de données dans **db.js**.

Rendez-vous sur [mLab](https://mlab.com/), créez un compte si vous n'en avez pas déjà un, et ouvrez votre tableau de bord de base de données. Créez une nouvelle base de données, nommez-la comme vous le souhaitez et accédez à sa page de configuration. Ajoutez un utilisateur de base de données à votre base de données et copiez la chaîne de connexion du tableau de bord dans votre code.

![Image](https://cdn-media-1.freecodecamp.org/images/Z5HFF8CQYR9cwiRY8f08tlWbz8PQARSVDHGL)

Tout ce que vous avez à faire maintenant est de changer les valeurs de remplissage pour `<dbuser>` et `<dbpassword>`. Remplacez-les par le nom d'utilisateur et le mot de passe de l'utilisateur que vous avez créé pour la base de données. Une explication détaillée étape par étape de ce processus peut être trouvée dans [le tutoriel lié ci-dessus](https://hackernoon.com/restful-api-design-with-node-js-26ccf66eab09).

Supposons que l'utilisateur que j'ai créé pour la base de données s'appelle `wally` avec un mot de passe `theflashisawesome`. En gardant cela à l'esprit, le fichier **db.js** devrait maintenant ressembler à ceci :

```js
var mongoose = require('mongoose');
mongoose.connect('mongodb://wally:theflashisawesome@ds147072.mlab.com:47072/securing-rest-apis-with-jwt', { useMongoClient: true });
```

Allez-y et démarrez le serveur, dans votre fenêtre de terminal, tapez `node server.js`. Vous devriez voir `Express server listening on port 3000` enregistré dans le terminal.

### Enfin, du code.

Commençons par réfléchir à ce que nous voulons construire. Tout d'abord, nous voulons ajouter une authentification utilisateur. Cela signifie mettre en place un système pour enregistrer et connecter les utilisateurs.

Deuxièmement, nous voulons ajouter une autorisation. L'acte d'accorder aux utilisateurs la permission d'accéder à certaines ressources sur notre API REST.

Commencez par ajouter un nouveau fichier dans le répertoire racine du projet. Donnez-lui le nom **config.js**. Ici, vous mettrez les paramètres de configuration pour l'application. Tout ce dont nous avons besoin pour l'instant est de définir une clé secrète pour notre JSON Web Token.

**Avertissement** : Gardez à l'esprit que, en aucune circonstance, vous ne devez jamais, (JAMAIS !) avoir votre clé secrète visible publiquement comme ceci. Placez toujours toutes vos clés dans des variables d'environnement ! Je l'écris comme ça uniquement à des fins de démonstration.

```js
// config.js
module.exports = {
  'secret': 'supersecret'
};
```

Avec ceci ajouté, vous êtes prêt à commencer à ajouter la logique d'authentification. Créez un dossier nommé **auth** et commencez par ajouter un fichier nommé **AuthController.js**. Ce contrôleur sera le foyer de notre logique d'authentification.

Ajoutez ce morceau de code en haut du fichier **AuthController.js**.

```js
// AuthController.js

var express = require('express');
var router = express.Router();
var bodyParser = require('body-parser');
router.use(bodyParser.urlencoded({ extended: false }));
router.use(bodyParser.json());
var User = require('../user/User');
```

Maintenant, vous êtes prêt à ajouter les modules pour utiliser [JSON Web Tokens](https://github.com/auth0/node-jsonwebtoken) et [chiffrer les mots de passe](https://github.com/dcodeIO/bcrypt.js). Collez ce code dans le **AuthController.js** :

```js
var jwt = require('jsonwebtoken');
var bcrypt = require('bcryptjs');
var config = require('../config');
```

Ouvrez une fenêtre de terminal dans votre dossier de projet et installez les modules suivants :

```bash
npm install jsonwebtoken --save
npm install bcryptjs --save
```

Ce sont tous les modules dont nous avons besoin pour implémenter notre authentification souhaitée. Maintenant, vous êtes prêt à créer un point de terminaison `/register`. Ajoutez ce morceau de code à votre **AuthController.js** :

```js
router.post('/register', function(req, res) {
  
  var hashedPassword = bcrypt.hashSync(req.body.password, 8);
  
  User.create({
    name : req.body.name,
    email : req.body.email,
    password : hashedPassword
  },
  function (err, user) {
    if (err) return res.status(500).send("Il y a eu un problème lors de l'enregistrement de l'utilisateur.")
    // créer un jeton
    var token = jwt.sign({ id: user._id }, config.secret, {
      expiresIn: 86400 // expire dans 24 heures
    });
    res.status(200).send({ auth: true, token: token });
  }); 
});
```

Ici, nous attendons que l'utilisateur nous envoie trois valeurs : un nom, un email et un mot de passe. Nous allons immédiatement prendre le mot de passe et le chiffrer avec la méthode de hachage de Bcrypt. Ensuite, nous prenons le mot de passe haché, incluons le nom et l'email et créons un nouvel utilisateur. Après que l'utilisateur a été créé avec succès, nous pouvons créer un jeton pour cet utilisateur.

La méthode `jwt.sign()` prend une charge utile et la clé secrète définie dans **config.js** comme paramètres. Elle crée une chaîne de caractères unique représentant la charge utile. Dans notre cas, la charge utile est un objet contenant uniquement l'id de l'utilisateur. Écrivons un morceau de code pour obtenir l'id de l'utilisateur en fonction du jeton que nous avons reçu du point de terminaison d'enregistrement.

```js
router.get('/me', function(req, res) {
  var token = req.headers['x-access-token'];
  if (!token) return res.status(401).send({ auth: false, message: 'Aucun jeton fourni.' });
  
  jwt.verify(token, config.secret, function(err, decoded) {
    if (err) return res.status(500).send({ auth: false, message: 'Échec de l\'authentification du jeton.' });
    
    res.status(200).send(decoded);
  });
});
```

Ici, nous attendons que le jeton soit envoyé avec la requête dans les en-têtes. Le nom par défaut pour un jeton dans les en-têtes d'une requête HTTP est `x-access-token`. Si aucun jeton n'est fourni avec la requête, le serveur renvoie une erreur. Plus précisément, un statut `401 non autorisé` avec un message de réponse '_Aucun jeton fourni_'. Si le jeton existe, la méthode `jwt.verify()` sera appelée. Cette méthode décode le jeton, ce qui permet de voir la charge utile originale. Nous gérerons les erreurs s'il y en a et, s'il n'y en a pas, nous renverrons la valeur décodée comme réponse.

Enfin, nous devons ajouter la route au **AuthController.js** dans notre fichier principal **app.js**. Tout d'abord, exportez le routeur depuis **AuthController.js** :

```js
// ajoutez ceci au bas de AuthController.js
module.exports = router;
```

Ensuite, ajoutez une référence au contrôleur dans l'application principale, juste au-dessus de l'endroit où vous avez exporté l'application.

```js
// app.js
var AuthController = require('./auth/AuthController');
app.use('/api/auth', AuthController);
module.exports = app;
```

### Testons cela. Pourquoi pas ?

Ouvrez votre outil de test d'API REST préféré, j'utilise [Postman](https://www.getpostman.com/postman) ou [Insomnia](https://insomnia.rest/), mais n'importe lequel fera l'affaire.

Retournez à votre terminal et exécutez `node server.js`. Si le serveur est en cours d'exécution, arrêtez-le, enregistrez toutes les modifications apportées à vos fichiers et exécutez à nouveau `node server.js`.

Ouvrez Postman et accédez au point de terminaison d'enregistrement (`/api/auth/register`). Assurez-vous de choisir la méthode POST et `x-www-form-url-encoded`. Maintenant, ajoutez quelques valeurs. Le nom de mon utilisateur est Mike et son mot de passe est 'thisisasecretpassword'. Ce n'est pas le meilleur mot de passe que j'aie jamais vu, pour être honnête, mais cela fera l'affaire. Envoyez !

![Image](https://cdn-media-1.freecodecamp.org/images/vshJBCITdZGicsO1sw5prUHlSGR9bNugRtjv)
_/register_

Vous voyez la réponse ? Le jeton est une longue chaîne de caractères mélangés. Pour essayer le point de terminaison `/api/auth/me`, copiez d'abord le jeton. Changez l'URL en `/me` au lieu de `/register`, et la méthode en GET. Maintenant, vous pouvez ajouter le jeton à l'en-tête de la requête.

![Image](https://cdn-media-1.freecodecamp.org/images/Lh6dOAOqy3A5tpOPy8xUQLKONDUsVmT-uVup)
_/me_

Voilà ! Le jeton a été décodé en un objet avec un champ id. Vous voulez vous assurer que l'id appartient vraiment à Mike, l'utilisateur que nous venons de créer ? Bien sûr que oui. Retournez dans votre éditeur de code.

```js
// dans AuthController.js, changez cette ligne
res.status(200).send(decoded);

// par
User.findById(decoded.id, function (err, user) {
  if (err) return res.status(500).send("Il y a eu un problème lors de la recherche de l'utilisateur.");
  if (!user) return res.status(404).send("Aucun utilisateur trouvé.");
  
  res.status(200).send(user);
});
```

Maintenant, lorsque vous envoyez une requête au point de terminaison `/me`, vous verrez :

![Image](https://cdn-media-1.freecodecamp.org/images/JfGjoyqG9zttRCEPsXTkUiNQ12NbKbRiqzyy)

La réponse contient maintenant l'objet utilisateur complet ! Cool ! Mais pas bien. Le mot de passe ne devrait jamais être renvoyé avec les autres données de l'utilisateur. Corrigons cela. Nous pouvons ajouter une projection à la requête et omettre le mot de passe. Comme ceci :

```js
User.findById(decoded.id, 
  { password: 0 }, // projection
  function (err, user) {
    if (err) return res.status(500).send("Il y a eu un problème lors de la recherche de l'utilisateur.");
    if (!user) return res.status(404).send("Aucun utilisateur trouvé.");
    
    res.status(200).send(user);
});
```

![Image](https://cdn-media-1.freecodecamp.org/images/GSTNoNziXzH43m9kEYX499bgB012YenWiHAF)

C'est mieux, maintenant nous pouvons voir toutes les valeurs sauf le mot de passe. Mike a l'air bien.

### Quelqu'un a dit connexion ?

Après avoir implémenté l'enregistrement, nous devons créer un moyen pour les utilisateurs existants de se connecter. Réfléchissons-y une seconde. Le point de terminaison d'enregistrement nous a demandé de créer un utilisateur, de hacher un mot de passe et d'émettre un jeton. Que devra implémenter le point de terminaison de connexion ? Il devrait vérifier si un utilisateur avec l'email donné existe. Mais aussi vérifier si le mot de passe fourni correspond au mot de passe haché dans la base de données. Ce n'est qu'alors que nous voudrons émettre un jeton. Ajoutez ceci à votre **AuthController.js**.

```js
router.post('/login', function(req, res) {

  User.findOne({ email: req.body.email }, function (err, user) {
    if (err) return res.status(500).send('Erreur sur le serveur.');
    if (!user) return res.status(404).send('Aucun utilisateur trouvé.');
    
    var passwordIsValid = bcrypt.compareSync(req.body.password, user.password);
    if (!passwordIsValid) return res.status(401).send({ auth: false, token: null });
    
    var token = jwt.sign({ id: user._id }, config.secret, {
      expiresIn: 86400 // expire dans 24 heures
    });
    
    res.status(200).send({ auth: true, token: token });
  });
  
});
```

Tout d'abord, nous vérifions si l'utilisateur existe. Ensuite, en utilisant la méthode `.compareSync()` de Bcrypt, nous comparons le mot de passe envoyé avec la requête au mot de passe dans la base de données. S'ils correspondent, nous signons un jeton. C'est à peu près tout. Essayons cela.

![Image](https://cdn-media-1.freecodecamp.org/images/sSJkpDDrhTNNLeYSG-b0MD5gfQBFqNMK6uUx)

Cool, ça marche ! Que se passe-t-il si nous nous trompons de mot de passe ?

![Image](https://cdn-media-1.freecodecamp.org/images/QkXrnEyXUKhakmAGysGEIGVd39S3uLmhncLE)

Super, lorsque le mot de passe est incorrect, le serveur envoie un statut de réponse `401 non autorisé`. Exactement ce que nous voulions !

Pour terminer cette partie du tutoriel, ajoutons un point de terminaison de déconnexion simple pour annuler le jeton.

```js
// AuthController.js
router.get('/logout', function(req, res) {
  res.status(200).send({ auth: false, token: null });
});
```

**Avertissement** : Le point de terminaison de déconnexion n'est pas nécessaire. L'acte de déconnexion peut être effectué uniquement côté client. Un jeton est généralement conservé dans un cookie ou le localStorage du navigateur. La déconnexion est aussi simple que de détruire le jeton sur le client. Ce point de terminaison `/logout` est créé pour décrire logiquement ce qui se passe lorsque vous vous déconnectez. Le jeton est défini sur `null`.

Avec cela, nous avons terminé la partie **authentification** du tutoriel. Vous voulez passer à l'autorisation ? Je parie que oui.

### Avez-vous la permission d'être ici ?

Pour comprendre la logique derrière une stratégie d'autorisation, nous devons nous familiariser avec quelque chose appelé **middleware**. Son nom est en partie explicite, n'est-ce pas ? Le middleware est un morceau de code, une fonction dans Node.js, qui agit comme un pont entre certaines parties de votre code.

Lorsque une requête atteint un point de terminaison, le routeur a la possibilité de transmettre la requête à la fonction middleware suivante dans la chaîne. Insistons sur le mot **suivant** ! Parce que c'est exactement le nom de la fonction ! Voyons un exemple. Commentez la ligne où vous renvoyez l'utilisateur comme réponse. Ajoutez un `next(user)` juste en dessous.

```js
router.get('/me', function(req, res, next) {
    
  var token = req.headers['x-access-token'];
  if (!token) return res.status(401).send({ auth: false, message: 'Aucun jeton fourni.' });
  
  jwt.verify(token, config.secret, function(err, decoded) {
    if (err) return res.status(500).send({ auth: false, message: 'Échec de l\'authentification du jeton.' });
    
    User.findById(decoded.id, 
    { password: 0 }, // projection
    function (err, user) {
      if (err) return res.status(500).send("Il y a eu un problème lors de la recherche de l'utilisateur.");
      if (!user) return res.status(404).send("Aucun utilisateur trouvé.");
        
      // res.status(200).send(user); Commentez ceci !
      next(user); // ajoutez cette ligne
    });
  });
});

// ajoutez la fonction middleware
router.use(function (user, req, res, next) {
  res.status(200).send(user);
});
```

> Les fonctions **Middleware** sont des fonctions qui ont accès à l'objet [request](https://expressjs.com/en/4x/api.html#req) (`req`), à l'objet [response](https://expressjs.com/en/4x/api.html#res) (`res`), et à la fonction `next` dans le cycle de requête-réponse de l'application. La fonction `next` est une fonction dans le routeur Express qui, lorsqu'elle est appelée, exécute le middleware suivant le middleware actuel.  
> - [Utilisation du middleware](https://expressjs.com/en/guide/using-middleware.html), expressjs.com

Retournez à Postman et voyez ce qui se passe lorsque vous accédez au point de terminaison `/api/auth/me`. Êtes-vous surpris que le résultat soit exactement le même ? Cela devrait être le cas !

**Avertissement** : Allez-y et supprimez cet exemple avant de continuer car il est uniquement utilisé pour démontrer la logique de l'utilisation de `next()`.

Prenons cette même logique et appliquons-la pour créer une fonction middleware afin de vérifier la validité des jetons. Créez un nouveau fichier dans le dossier **auth** et nommez-le **VerifyToken.js**. Collez ce snippet de code à l'intérieur.

```js
var jwt = require('jsonwebtoken');
var config = require('../config');

function verifyToken(req, res, next) {
  var token = req.headers['x-access-token'];
  if (!token)
    return res.status(403).send({ auth: false, message: 'Aucun jeton fourni.' });
    
  jwt.verify(token, config.secret, function(err, decoded) {
    if (err)
    return res.status(500).send({ auth: false, message: 'Échec de l\'authentification du jeton.' });
      
    // si tout est bon, sauvegardez dans la requête pour une utilisation dans d'autres routes
    req.userId = decoded.id;
    next();
  });
}

module.exports = verifyToken;
```

Décomposons cela. Nous allons utiliser cette fonction comme un middleware personnalisé pour vérifier si un jeton existe et s'il est valide. Après l'avoir validé, nous ajoutons la valeur `decoded.id` à la variable de requête (`req`). Nous avons maintenant accès à celle-ci dans la fonction suivante de la chaîne dans le cycle de requête-réponse. L'appel de `next()` garantira que le flux se poursuivra vers la fonction suivante en attente dans la chaîne. Enfin, nous exportons la fonction.

Maintenant, ouvrez à nouveau le **AuthController.js**. Ajoutez une référence à **VerifyToken.js** en haut du fichier et modifiez le point de terminaison `/me`. Il devrait maintenant ressembler à ceci :

```js
// AuthController.js

var VerifyToken = require('./VerifyToken');

// ...

router.get('/me', VerifyToken, function(req, res, next) {

  User.findById(req.userId, { password: 0 }, function (err, user) {
    if (err) return res.status(500).send("Il y a eu un problème lors de la recherche de l'utilisateur.");
    if (!user) return res.status(404).send("Aucun utilisateur trouvé.");
    
    res.status(200).send(user);
  });
  
});

// ...
```

Vous voyez comment nous avons ajouté `VerifyToken` dans la chaîne de fonctions ? Nous gérons maintenant toute l'autorisation dans le middleware. Cela libère tout l'espace dans le callback pour ne gérer que la logique dont nous avons besoin. C'est un exemple génial de la façon d'écrire du code DRY. Maintenant, chaque fois que vous devez autoriser un utilisateur, vous pouvez ajouter cette fonction middleware à la chaîne. Testons à nouveau dans Postman, pour nous assurer que cela fonctionne comme prévu.

![Image](https://cdn-media-1.freecodecamp.org/images/19EpKwBFR9RiWF4P-lDTJYRIiCYsCynW9bU7)

N'hésitez pas à manipuler le jeton et à essayer à nouveau le point de terminaison. Avec un jeton invalide, vous verrez le message d'erreur souhaité, et soyez sûr que le code que vous avez écrit fonctionne comme vous le souhaitez.

Pourquoi est-ce si puissant ? Vous pouvez maintenant ajouter le middleware `VerifyToken` à n'importe quelle chaîne de fonctions et être sûr que les points de terminaison sont sécurisés. Seuls les utilisateurs avec des jetons vérifiés peuvent accéder aux ressources !

### Comprendre tout cela.

Ne vous sentez pas mal si vous n'avez pas tout saisi d'un coup. Certains de ces concepts sont difficiles à comprendre. Il est normal de faire un pas en arrière et de reposer votre cerveau avant d'essayer à nouveau. C'est pourquoi je vous recommande de parcourir le code par vous-même et d'essayer de le faire fonctionner.

Encore une fois, [voici le dépôt GitHub](https://github.com/adnanrahic/securing-restful-apis-with-jwt). Vous pouvez rattraper les choses que vous avez peut-être manquées, ou simplement mieux regarder le code si vous êtes bloqué.

Rappelez-vous, l'**authentification** est l'acte de connecter un utilisateur. L'**autorisation** est l'acte de vérifier les droits d'accès d'un utilisateur à interagir avec une ressource.

Les fonctions **Middleware** sont utilisées comme des ponts entre certaines parties du code. Lorsqu'elles sont utilisées dans la chaîne de fonctions d'un point de terminaison, elles peuvent être incroyablement utiles pour l'autorisation et la gestion des erreurs.

J'espère que vous, les gars et les filles, avez apprécié la lecture de ceci autant que j'ai apprécié l'écrire. Jusqu'à la prochaine fois, soyez curieux et amusez-vous.

_Pensez-vous que ce tutoriel sera utile à quelqu'un ? N'hésitez pas à le partager. Si vous l'avez aimé, applaudissez pour moi._