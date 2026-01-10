---
title: Comment créer un système d'authentification sécurisé avec JWT et Refresh Tokens
subtitle: ''
author: Joan Ayebola
co_authors: []
series: null
date: '2025-11-25T18:32:53.009Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-secure-authentication-system-with-jwt-and-refresh-tokens
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1764095460886/51b9c653-fa95-42f0-8c51-37f6d6805da4.png
tags:
- name: authentication
  slug: authentication
- name: JWT
  slug: jwt
- name: Security
  slug: security
seo_title: Comment créer un système d'authentification sécurisé avec JWT et Refresh
  Tokens
seo_desc: 'Every app that handles user accounts needs a way to confirm who’s who.
  That’s what authentication is for, making sure the person using an app is the person
  they claim to be. But doing this securely is harder than it sounds.

  Traditional methods often ...'
---


Chaque application qui gère des comptes utilisateurs a besoin d'un moyen de confirmer l'identité de chacun. C'est à cela que sert l'authentification : s'assurer que la personne qui utilise une application est bien celle qu'elle prétend être. Mais réaliser cela de manière sécurisée est plus difficile qu'il n'y paraît.

Les méthodes traditionnelles reposent souvent sur des sessions serveur et des cookies. Elles fonctionnent, mais ne passent pas toujours bien à l'échelle, surtout lorsque vous construisez des API ou des applications mobiles qui communiquent avec plusieurs services. C'est pourquoi les JWT, ou JSON Web Tokens, sont utiles. Ce sont de petits jetons autonomes qui peuvent transporter des données utilisateur en toute sécurité entre un client et un serveur.

Les JWT permettent de vérifier facilement les utilisateurs sans interroger constamment une base de données – mais ils expirent également rapidement pour réduire les risques. Pour maintenir les utilisateurs connectés sans les forcer à se reconnecter toutes les quelques minutes, nous utilisons ce qu'on appelle un refresh token. Il s'agit d'un jeton séparé, à longue durée de vie, qui peut demander de nouveaux access tokens lorsque les anciens expirent.

Dans ce guide, nous allons parcourir la création d'un système d'authentification sécurisé utilisant des JWT et des refresh tokens. Vous apprendrez à générer des tokens, à les valider, à gérer l'expiration et à protéger l'ensemble contre les menaces de sécurité courantes.

## Table des matières

1. [Comprendre les JWT (JSON Web Tokens)](#comprendre-les-jwt-json-web-tokens)
    
2. [Configuration du projet](#configuration-du-projet)
    
3. [Comment implémenter l'authentification JWT](#comment-implementer-lauthentification-jwt)
    
4. [Comment vérifier les JWT et protéger les routes](#comment-verifier-les-jwt-et-proteger-les-routes)
    
5. [Refresh Tokens et Rotation](#refresh-tokens-et-rotation)
    
6. [Conclusion](#conclusion)
    

## Comprendre les JWT (JSON Web Tokens)

Un JWT, abréviation de JSON Web Token, est un moyen compact de partager des informations entre un client et un serveur. Il est souvent utilisé pour prouver qu'un utilisateur est bien celui qu'il prétend être. Le token est créé sur le serveur après la connexion d'un utilisateur, puis renvoyé au client. Le client inclut ensuite ce token dans chaque requête, afin que le serveur sache qui effectue l'appel.

Un JWT se compose de trois parties : un header, un payload et une signature.

* Le **header** indique généralement au système quel algorithme a été utilisé pour signer le token.
    
* Le **payload** contient les données, telles que l'ID ou le rôle de l'utilisateur.
    
* La **signature** est la partie qui sécurise l'ensemble. Elle est créée en hachant le header et le payload avec une clé secrète.
    

Une fois créé, un JWT ressemble à une longue chaîne de caractères aléatoires séparés par des points. Lorsque le client le renvoie au serveur, le serveur vérifie la signature en utilisant la même clé secrète. Si elle correspond, la requête est considérée comme fiable.

L'un des principaux avantages des JWT est qu'ils sont sans état (stateless). Le serveur n'a pas besoin de stocker les données de session. Tout ce qui est nécessaire pour vérifier l'utilisateur se trouve déjà à l'intérieur du token. Cela les rend rapides et faciles à utiliser dans les API modernes et les microservices.

Les JWT ont cependant un inconvénient : ils ne peuvent pas être révoqués facilement une fois émis. Si un token est volé, l'attaquant peut l'utiliser jusqu'à ce qu'il expire. C'est pourquoi les durées de vie courtes des tokens sont importantes. C'est aussi la raison d'être des refresh tokens.

Dans la section suivante, nous terminerons la configuration de base du JWT. Après cela, nous ajouterons des refresh tokens dans la section **« Refresh Tokens et Rotation »**. Cette partie montre comment gérer l'expiration sans obliger les utilisateurs à se reconnecter.

## Configuration du projet

Avant d'écrire du code, configurons un backend simple où nous pourrons construire et tester notre système d'authentification. Pour ce guide, nous utiliserons Node.js avec Express, car il est léger et facile à suivre. Vous pourrez utiliser n'importe quelle Stack plus tard une fois que vous aurez compris le flux.

### Prérequis

Assurez-vous d'avoir :

* Node.js et npm installés
    
* Un éditeur de texte (VS Code fonctionne très bien)
    
* Des connaissances de base en JavaScript et en API
    

### 1\. Initialiser le projet

Créez un nouveau dossier et ouvrez-le dans votre terminal.

```bash
mkdir jwt-auth-demo
cd jwt-auth-demo
npm init -y
```

Cela crée un fichier `package.json` qui suivra vos dépendances.

### 2\. Installer les dépendances

Vous aurez besoin de quelques packages pour commencer :

* `express` : le Framework web
    
* `jsonwebtoken` : pour créer et vérifier les tokens
    
* `bcryptjs` : pour hacher les mots de passe
    
* `dotenv` : pour gérer les variables d'environnement
    

Installez-les tous en une seule fois comme ceci :

```bash
npm install express jsonwebtoken bcryptjs dotenv
```

Si vous voulez un rechargement automatique pendant le développement, installez nodemon en tant que dépendance de développement :

```bash
npm install --save-dev nodemon
```

### 3\. Structure du projet

Voici une structure propre pour garder les choses organisées :

```plaintext
jwt-auth-demo/
│
├── server.js
├── .env
├── package.json
│
├── config/
│   └── db.js
│
├── middleware/
│   └── auth.js
│
├── routes/
│   └── auth.js
│
└── models/
    └── user.js
```

### 4\. Configuration de base d'Express

Dans `server.js`, commencez par un serveur Express minimal.

```js
require('dotenv').config();
const express = require('express');
const app = express();

app.use(express.json());

app.get('/', (req, res) => {
  res.send('JWT Auth API running');
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```

Vous pouvez maintenant le lancer en utilisant :

```bash
node server.js
```

ou, si vous utilisez nodemon :

```bash
npx nodemon server.js
```

Si tout est configuré correctement, en visitant `http://localhost:5000`, vous devriez voir s'afficher **« JWT Auth API running »** :

![Capture d'écran d'un terminal exécutant nodemon server.js à côté d'une fenêtre de navigateur affichant le texte « JWT Auth API running » à l'adresse http://localhost:5000, confirmant que le serveur a démarré correctement.](https://cdn.hashnode.com/res/hashnode/image/upload/v1760559643076/8fb7dcbf-50ca-44bc-b2a3-32273d82957f.png align="center")

## **Comment implémenter l'authentification JWT**

Maintenant que votre serveur est opérationnel, ajoutons une véritable authentification. Nous allons commencer par l'inscription des utilisateurs, le hachage des mots de passe et la connexion. Chaque utilisateur recevra un token après s'être connecté, qu'il pourra utiliser pour accéder aux routes protégées.

### 1\. Configurer le modèle utilisateur

Nous stockerons les utilisateurs dans une base de données simple. Pour cette démo, utilisons MongoDB avec Mongoose, car c'est rapide à configurer et facile à faire évoluer plus tard.

Installez les packages requis :

```bash
npm install mongoose
```

Ensuite, créez `models/user.js` :

```js
const mongoose = require('mongoose');

const userSchema = new mongoose.Schema({
  username: { type: String, required: true, unique: true },
  email: { type: String, required: true, unique: true },
  password: { type: String, required: true }
});

module.exports = mongoose.model('User', userSchema);
```

Nous stockons les utilisateurs avec un email unique et un mot de passe haché. La base de données ne voit jamais le mot de passe en clair. Le hachage rend les données volées plus difficiles à utiliser.

### 2\. Se connecter à MongoDB

À l'intérieur de `config/db.js` :

```js
const mongoose = require('mongoose');

const connectDB = async () => {
  try {
    await mongoose.connect(process.env.MONGO_URI);
    console.log('MongoDB connected');
  } catch (err) {
    console.error(err.message);
    process.exit(1);
  }
};

module.exports = connectDB;
```

`mongoose.connect` lit la chaîne de connexion depuis `.env`. Si la connexion échoue, nous quittons le processus pour ne pas continuer dans un état défectueux.

Mettez à jour votre `server.js` pour inclure la connexion :

```js
const connectDB = require('./config/db');
connectDB();
```

Et n'oubliez pas d'ajouter votre URI MongoDB dans le fichier `.env` :

```plaintext
MONGO_URI=mongodb+srv://votreutilisateur:votremotdepasse@cluster.mongodb.net/auth
JWT_SECRET=votre_cle_secrete_jwt
```

### 3\. Créer les routes d'inscription et de connexion

Dans `routes/auth.js` :

```js
const express = require('express');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const User = require('../models/user');

const router = express.Router();

// Inscrire un nouvel utilisateur
router.post('/register', async (req, res) => {
  try {
    const { username, email, password } = req.body;

    const existingUser = await User.findOne({ email });
    if (existingUser) return res.status(400).json({ message: 'User already exists' });

    const hashedPassword = await bcrypt.hash(password, 10);

    const newUser = new User({ username, email, password: hashedPassword });
    await newUser.save();

    res.status(201).json({ message: 'User created successfully' });
  } catch (err) {
    res.status(500).json({ message: 'Server error' });
  }
});

// Connexion et émission de JWT
router.post('/login', async (req, res) => {
  try {
    const { email, password } = req.body;

    const user = await User.findOne({ email });
    if (!user) return res.status(400).json({ message: 'Invalid credentials' });

    const isMatch = await bcrypt.compare(password, user.password);
    if (!isMatch) return res.status(400).json({ message: 'Invalid credentials' });

    const payload = { id: user._id, email: user.email };

    const token = jwt.sign(payload, process.env.JWT_SECRET, { expiresIn: '15m' });

    res.json({ token });
  } catch (err) {
    res.status(500).json({ message: 'Server error' });
  }
});

module.exports = router;
```

Ajoutez-le à votre serveur dans `server.js` :

```js
const authRoutes = require('./routes/auth');
app.use('/api/auth', authRoutes);
```

### 4\. Tester le fonctionnement

Vous pouvez maintenant tester ces routes en utilisant Postman ou Insomnia.

Envoyez une requête `POST` à `/api/auth/register` avec un corps JSON :

```json
{
  "username": "demoUser",
  "email": "demo@email.com",
  "password": "mypassword"
}
```

![Capture d'écran d'une requête Postman envoyant un appel POST à http://localhost:3000/api/auth/register avec un corps JSON contenant un nom d'utilisateur, un email et un mot de passe. La zone de réponse affiche un statut 201 Created et le message « User created successfully. »](https://cdn.hashnode.com/res/hashnode/image/upload/v1760713863394/c13ddbd5-ebb1-47d1-9b6d-06bc0f33eb7d.png align="center")

La route d'inscription vérifie si un utilisateur existe déjà par email. Elle hache le mot de passe avec un facteur de coût de 10, puis renvoie un 201 en cas de succès. Nous n'enregistrons pas le mot de passe et ne l'incluons pas dans la réponse.

Ensuite, connectez-vous à `/api/auth/login` pour recevoir un JWT.

![Capture d'écran d'une requête Postman envoyant un appel POST à http://localhost:3000/api/auth/login avec un corps JSON contenant un nom d'utilisateur, un email et un mot de passe. Le panneau de réponse affiche un statut 200 OK et un objet JSON avec un token JWT généré.](https://cdn.hashnode.com/res/hashnode/image/upload/v1760713960135/58eeaa4e-d652-4509-ad6e-756baf19ff8c.png align="center")

La route de connexion trouve l'utilisateur par email et compare le mot de passe avec `bcrypt.compare`. Si cela correspond, nous signons un token avec un petit payload : l'ID de l'utilisateur et l'email. Le `JWT_SECRET` signe le token afin que le serveur puisse le vérifier plus tard. Le paramètre `expiresIn: '15m'` maintient le token à courte durée de vie pour limiter les risques. La réponse n'inclut que le token. Les données utilisateur peuvent être récupérées à partir d'une route protégée.

Une fois que vous avez obtenu le token, copiez-le, vous l'utiliserez pour accéder aux routes protégées plus tard.

## Comment vérifier les JWT et protéger les routes

Maintenant que la connexion renvoie un token, nous devrions le vérifier à chaque requête nécessitant une authentification. Nous allons écrire un petit Middleware qui vérifie le header `Authorization`, valide le token et ajoute les informations de l'utilisateur à la requête.

### 1\. Créer le Middleware d'authentification

Créez `middleware/auth.js` :

```js
const jwt = require('jsonwebtoken');

function auth(req, res, next) {
  const authHeader = req.headers.authorization || '';
  const [scheme, token] = authHeader.split(' ');

  if (scheme !== 'Bearer' || !token) {
    return res.status(401).json({ message: 'Missing or invalid Authorization header' });
  }

  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    req.user = { id: decoded.id, email: decoded.email };
    next();
  } catch (err) {
    if (err.name === 'TokenExpiredError') {
      return res.status(401).json({ message: 'Access token expired' });
    }
    return res.status(401).json({ message: 'Invalid token' });
  }
}

module.exports = auth;
```

Ce qu'il fait :

* Lit le header `Authorization`.
    
* Vérifie le format `Bearer <token>`.
    
* Vérifie le token avec le secret.
    
* Attache un objet `user` simple à `req` pour une utilisation ultérieure.
    

### 2\. Créer la route protégée

Créez une petite route de profil qui renvoie l'utilisateur actuel. Ajoutez `routes/profile.js` :

```js
const express = require('express');
const auth = require('../middleware/auth');
const User = require('../models/user');

const router = express.Router();

router.get('/me', auth, async (req, res) => {
  try {
    const user = await User.findById(req.user.id).select('-password');
    if (!user) {
      return res.status(404).json({ message: 'User not found' });
    }
    res.json({ user });
  } catch (err) {
    res.status(500).json({ message: 'Server error' });
  }
});

module.exports = router;
```

Connectez-la dans `server.js` :

```js
const profileRoutes = require('./routes/profile');
app.use('/api/profile', profileRoutes);
```

Désormais, un appel `GET /api/profile/me` ne fonctionnera qu'avec un token valide.

### 3\. Gérer clairement l'expiration du token

Les access tokens courts réduisent les dommages en cas de fuite. Nous avons défini `expiresIn: '15m'` lors de la connexion. Lorsqu'un token expire, le Middleware renvoie un 401 avec `Access token expired`.

Nous ne rafraîchirons pas le token ici car le rafraîchissement nécessite son propre endpoint, son stockage et ses règles de rotation. Vous ajouterez cela dans la section **« Refresh Tokens et Rotation »**. Pour l'instant, le 401 prouve que l'expiration est appliquée.

### 4\. Tester le flux

Dans cette section, nous allons tester que le serveur bloque les requêtes sans token valide et autorise les requêtes avec un token valide.

Connectez-vous à `/api/auth/login` et copiez le token. Appelez ensuite `/api/profile/me` avec :

```typescript
Authorization: Bearer <coller_le_token_ici>
```

Vous devriez voir l'utilisateur actuel sans le champ mot de passe.

![Capture d'écran d'une requête GET Postman vers http://localhost:3000/api/profile/me utilisant un JWT valide. La réponse affiche un statut 200 OK et renvoie l'_id, le nom d'utilisateur et l'email de l'utilisateur, confirmant que la route protégée fonctionne lorsqu'un token approprié est inclus.](https://cdn.hashnode.com/res/hashnode/image/upload/v1760715340324/13779fe0-304c-460b-87ac-c86133eea2a4.png align="left")

Ensuite, supprimez le header ou modifiez le token et appelez à nouveau. Vous devriez obtenir un 401.

Ensuite, attendez que le token expire ou changez `expiresIn` pour une valeur très courte pour un test rapide. Appelez à nouveau et confirmez que vous obtenez `Access token expired`.

#### Conseils pour le débogage

* Un 401 avec « Missing or invalid Authorization header » signifie que le format du header est incorrect. Utilisez `Authorization: Bearer <token>`.
    
* Un 401 avec « Invalid token » signifie que la chaîne du token est erronée, signée avec le mauvais secret ou corrompue.
    
* Un 401 avec « Access token expired » signifie que la vérification de l'expiration fonctionne. Vous corrigerez l'expérience client avec l'endpoint de rafraîchissement plus tard.
    
* Si tous les appels échouent, confirmez que votre `JWT_SECRET` est défini dans `.env` et que le serveur a été redémarré après les modifications.
    

### 5\. Support optionnel des cookies

Vous pouvez stocker les tokens dans des cookies HTTP-only. Le navigateur les envoie automatiquement. Les scripts ne peuvent pas lire les cookies HTTP-only, ce qui réduit le risque d'attaques XSS.

Installez et activez les cookies :

```plaintext
npm install cookie-parser
```

```javascript
// server.js
const cookieParser = require('cookie-parser');
app.use(cookieParser());
```

Lisez l'access token à partir d'un cookie en guise de solution de repli :

```javascript
// middleware/auth.js
const jwt = require('jsonwebtoken');

function auth(req, res, next) {
  const header = req.headers.authorization || '';
  const [scheme, tokenFromHeader] = header.split(' ');
  const tokenFromCookie = req.cookies?.access_token;

  const token = scheme === 'Bearer' && tokenFromHeader ? tokenFromHeader : tokenFromCookie;

  if (!token) return res.status(401).json({ message: 'No token provided' });

  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    req.user = { id: decoded.id, email: decoded.email };
    next();
  } catch (err) {
    const msg = err.name === 'TokenExpiredError' ? 'Access token expired' : 'Invalid token';
    return res.status(401).json({ message: msg });
  }
}

module.exports = auth;
```

Comment cela fonctionne :

* L'access token peut résider dans un cookie nommé `access_token`.
    
* Marquez le cookie comme `httpOnly` et `secure` en production.
    
* Définissez `sameSite: 'strict'` pour réduire le risque de CSRF.
    
* Pour les API utilisées par les navigateurs, les cookies simplifient l'envoi des tokens. Pour les SPA qui appellent de nombreux domaines, un header `Authorization` peut être plus simple.
    

Dans la section suivante, nous utiliserons la même approche de cookie pour le refresh token. Cette section explique pourquoi le rafraîchissement doit se faire via un cookie et comment la rotation bloque le rejeu.

## Refresh Tokens et Rotation

Les access tokens ont une durée de vie courte et sont utilisés à chaque requête. Ils prouvent rapidement l'identité de l'utilisateur. Les refresh tokens vivent plus longtemps et ne sont utilisés que pour obtenir de nouveaux access tokens lorsque les anciens expirent. Cette séparation permet de garder les requêtes quotidiennes rapides et limite les dommages en cas de fuite de token.

Nous stockerons le refresh token dans un cookie HTTP-only. Cela réduit l'exposition aux scripts et maintient un flux fluide.

### 1\. Installation et configuration

Nous avons déjà `cookie-parser`. Nous n'ajouterons rien de nouveau pour l'instant, mais nous utiliserons le [module `crypto` intégré de Node](https://nodejs.org/api/crypto.html) pour hacher le refresh token avant de le stocker. Pour rappel, le hachage signifie que le token brut n'est jamais enregistré. Si la base de données fuit, les attaquants ne peuvent pas utiliser les hachages pour se connecter.

Créez `models/refreshToken.js` :

```js
const mongoose = require('mongoose');

const refreshTokenSchema = new mongoose.Schema({
  user: { type: mongoose.Schema.Types.ObjectId, ref: 'User', index: true },
  tokenHash: { type: String, required: true, unique: true },
  jti: { type: String, required: true, index: true },
  expiresAt: { type: Date, required: true, index: true },
  revokedAt: { type: Date, default: null },
  replacedBy: { type: String, default: null }, // nouveau jti lors de la rotation
  createdAt: { type: Date, default: Date.now },
  ip: String,
  userAgent: String
});

module.exports = mongoose.model('RefreshToken', refreshTokenSchema);
```

### 2\. Helpers de Token

Créez `utils/tokens.js` pour une logique propre et réutilisable.

```js
const jwt = require('jsonwebtoken');
const crypto = require('crypto');
const RefreshToken = require('../models/refreshToken');

const ACCESS_TTL = '15m';
const REFRESH_TTL_SEC = 60 * 60 * 24 * 7; // 7 jours

function hashToken(token) {
  return crypto.createHash('sha256').update(token).digest('hex');
}

function createJti() {
  return crypto.randomBytes(16).toString('hex');
}

function signAccessToken(user) {
  const payload = { id: user._id.toString(), email: user.email };
  return jwt.sign(payload, process.env.JWT_SECRET, { expiresIn: ACCESS_TTL });
}

function signRefreshToken(user, jti) {
  const payload = { id: user._id.toString(), jti };
  const token = jwt.sign(payload, process.env.REFRESH_TOKEN_SECRET, { expiresIn: REFRESH_TTL_SEC });
  return token;
}

async function persistRefreshToken({ user, refreshToken, jti, ip, userAgent }) {
  const tokenHash = hashToken(refreshToken);
  const expiresAt = new Date(Date.now() + REFRESH_TTL_SEC * 1000);
  await RefreshToken.create({ user: user._id, tokenHash, jti, expiresAt, ip, userAgent });
}

function setRefreshCookie(res, refreshToken) {
  const isProd = process.env.NODE_ENV === 'production';
  res.cookie('refresh_token', refreshToken, {
    httpOnly: true,
    secure: isProd,
    sameSite: 'strict',
    path: '/api/auth/refresh',
    maxAge: REFRESH_TTL_SEC * 1000
  });
}

async function rotateRefreshToken(oldDoc, user, req, res) {
  // révoquer l'ancien
  oldDoc.revokedAt = new Date();
  const newJti = createJti();
  oldDoc.replacedBy = newJti;
  await oldDoc.save();

  // émettre les nouveaux
  const newAccess = signAccessToken(user);
  const newRefresh = signRefreshToken(user, newJti);
  await persistRefreshToken({
    user,
    refreshToken: newRefresh,
    jti: newJti,
    ip: req.ip,
    userAgent: req.headers['user-agent'] || ''
  });
  setRefreshCookie(res, newRefresh);
  return { accessToken: newAccess };
}

module.exports = {
  hashToken,
  createJti,
  signAccessToken,
  signRefreshToken,
  persistRefreshToken,
  setRefreshCookie,
  rotateRefreshToken
};
```

Dans ce code,

* `signAccessToken` crée un token court avec l'ID utilisateur et l'email.
    
* `signRefreshToken` crée un token à longue durée de vie avec une valeur `jti`. Le `jti` nous permet de faire pivoter et de suivre les tokens.
    
* `persistRefreshToken` hache le refresh token et stocke les métadonnées comme l'expiration et les informations sur l'appareil.
    
* `setRefreshCookie` écrit le cookie HTTP-only afin que le navigateur l'envoie automatiquement à l'endpoint de rafraîchissement.
    
* `rotateRefreshToken` révoque l'ancien token, émet une nouvelle paire et enregistre le nouvel enregistrement. La rotation bloque le rejeu si un ancien refresh token est volé.
    

### 3\. Émettre un Refresh Token lors de la connexion

Mettez à jour votre gestionnaire de connexion dans `routes/auth.js` pour créer et stocker un refresh token, puis définir le cookie.

```js
const express = require('express');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const User = require('../models/user');
const RefreshToken = require('../models/refreshToken');
const {
  createJti,
  signAccessToken,
  signRefreshToken,
  persistRefreshToken,
  setRefreshCookie
} = require('../utils/tokens');

const router = express.Router();

router.post('/login', async (req, res) => {
  try {
    const { email, password } = req.body;

    const user = await User.findOne({ email });
    if (!user) return res.status(400).json({ message: 'Invalid credentials' });

    const isMatch = await bcrypt.compare(password, user.password);
    if (!isMatch) return res.status(400).json({ message: 'Invalid credentials' });

    const accessToken = signAccessToken(user);

    const jti = createJti();
    const refreshToken = signRefreshToken(user, jti);

    await persistRefreshToken({
      user,
      refreshToken,
      jti,
      ip: req.ip,
      userAgent: req.headers['user-agent'] || ''
    });

    setRefreshCookie(res, refreshToken);

    res.json({ accessToken });
  } catch (err) {
    res.status(500).json({ message: 'Server error' });
  }
});

module.exports = router;
```

Lors de la connexion, nous émettons les deux tokens. L'access token va dans la réponse JSON. Le refresh token va dans un cookie HTTP-only limité au chemin `/api/auth/refresh`. Cela maintient le refresh token à l'écart du code frontend tout en permettant au navigateur de l'envoyer à l'endpoint de rafraîchissement.

### 4\. L'endpoint de rafraîchissement

Créez un endpoint qui lit le cookie de rafraîchissement, le vérifie, contrôle l'entrée en base de données et le fait pivoter. Si toutes les vérifications passent, il renvoie un nouvel access token et définit un nouveau cookie de rafraîchissement.

Ajoutez à `routes/auth.js` :

```js
const { hashToken, rotateRefreshToken } = require('../utils/tokens');

router.post('/refresh', async (req, res) => {
  try {
    const token = req.cookies?.refresh_token;
    if (!token) return res.status(401).json({ message: 'No refresh token' });

    let decoded;
    try {
      decoded = jwt.verify(token, process.env.REFRESH_TOKEN_SECRET);
    } catch (err) {
      return res.status(401).json({ message: 'Invalid or expired refresh token' });
    }

    const tokenHash = hashToken(token);
    const doc = await RefreshToken.findOne({ tokenHash, jti: decoded.jti }).populate('user');

    if (!doc) {
      return res.status(401).json({ message: 'Refresh token not recognized' });
    }
    if (doc.revokedAt) {
      return res.status(401).json({ message: 'Refresh token revoked' });
    }
    if (doc.expiresAt < new Date()) {
      return res.status(401).json({ message: 'Refresh token expired' });
    }

    const result = await rotateRefreshToken(doc, doc.user, req, res);
    return res.json({ accessToken: result.accessToken });
  } catch (err) {
    res.status(500).json({ message: 'Server error' });
  }
});
```

L'endpoint de rafraîchissement vérifie le cookie, contrôle l'enregistrement en base de données, confirme qu'il n'est ni expiré ni révoqué, puis le fait pivoter. La rotation définit `revokedAt` sur l'ancien enregistrement et en crée un nouveau avec un `jti` frais. La réponse renvoie un nouvel access token et définit un nouveau cookie de rafraîchissement.

### 5\. Déconnexion et révocation

Lors de la déconnexion, révoquez le refresh token actuel et effacez le cookie.

```js
router.post('/logout', async (req, res) => {
  try {
    const token = req.cookies?.refresh_token;
    if (token) {
      const tokenHash = hashToken(token);
      const doc = await RefreshToken.findOne({ tokenHash });
      if (doc && !doc.revokedAt) {
        doc.revokedAt = new Date();
        await doc.save();
      }
    }
    res.clearCookie('refresh_token', { path: '/api/auth/refresh' });
    res.json({ message: 'Logged out' });
  } catch (err) {
    res.status(500).json({ message: 'Server error' });
  }
});
```

La déconnexion révoque le refresh token correspondant s'il est présent et efface le cookie. Cela met fin à la session proprement côté serveur et côté client.

### 6\. Flux client

Voici comment l'application de navigation doit se comporter :

* Gardez l'access token en mémoire. Ne le mettez pas dans le `localStorage`.
    
* Appelez les API protégées avec le header `Authorization` ou laissez les cookies s'en charger si vous avez choisi l'approche par cookie pour l'accès.
    
* Si un appel échoue avec `Access token expired`, appelez `/api/auth/refresh`. Le navigateur envoie automatiquement le cookie de rafraîchissement.
    
* Remplacez l'access token en mémoire par le nouveau.
    
* Réessayez la requête d'origine.
    
* Lors de la déconnexion, appelez `/api/auth/logout` et effacez tout état local.
    

### 7\. Notes sur la sécurité

Voici quelques étapes clés que vous pouvez suivre pour vous assurer que tout est sécurisé :

#### Secrets séparés

Utilisez un secret différent pour les access tokens et les refresh tokens. Si le secret d'accès fuit, les refresh tokens utilisent toujours une clé différente. Définissez `JWT_SECRET` et `REFRESH_TOKEN_SECRET` dans `.env`.

#### HTTPS uniquement

Servez le trafic de production via HTTPS. Les cookies marqués `secure: true` ne circulent que via HTTPS. Cela protège les tokens en transit.

#### Rotation à chaque rafraîchissement

Émettez un nouveau refresh token et révoquez l'ancien à chaque rafraîchissement. La rotation rend un ancien token volé inutile après le rafraîchissement suivant.

#### Hacher les refresh tokens en base de données

Stockez un hachage SHA-256, pas le token brut. De cette façon, une fuite de base de données ne donne pas aux attaquants la chaîne de token réelle.

#### Portée et drapeaux pour les cookies

Utilisez `httpOnly: true`, `secure: true` en production, `sameSite: 'strict'`, et un chemin étroit tel que `/api/auth/refresh`. Ces drapeaux réduisent les risques XSS et CSRF et limitent l'endroit où le cookie est envoyé.

#### TTL d'accès court et TTL de rafraîchissement modéré

Gardez les access tokens courts, par exemple 15 minutes. Utilisez une durée de vie de rafraîchissement comme 7 jours. Cela maintient le risque bas sans agacer les utilisateurs.

#### Sensibilité à l'appareil

Stockez l' `ip` et l' `userAgent`. Si les schémas changent de manière suspecte, vous pouvez révoquer ou contester la session.

#### Audit et limites

Enregistrez les événements de rafraîchissement et envisagez des limites de débit (rate limits) sur l'endpoint de rafraîchissement. Cela aide à détecter les abus.

Ajoutez à `.env` :

```plaintext
REFRESH_TOKEN_SECRET=votre_cle_secrete_de_rafraichissement
```

## Conclusion

Vous disposez maintenant d'un système d'authentification fonctionnel qui utilise des JWT et des refresh tokens pour maintenir les utilisateurs connectés en toute sécurité. L'access token gère la vérification rapide. Le refresh token renouvelle discrètement l'accès lorsqu'il expire. Ensemble, ils trouvent un équilibre entre sécurité et commodité.

Vous avez construit l'inscription des utilisateurs, la connexion, les routes protégées et un flux de rafraîchissement complet. Vous avez également appris à faire pivoter les refresh tokens, à les stocker en toute sécurité et à gérer proprement la déconnexion. Chaque étape ajoute une couche de sécurité supplémentaire qui protège votre application et vos utilisateurs.

À partir de là, vous pouvez étendre cette configuration pour qu'elle corresponde à votre projet réel. Vous pouvez ajouter des autorisations basées sur les rôles, suivre les sessions utilisateur par appareil ou déplacer la logique dans un service d'authentification dédié. Ce qui importe le plus, c'est de comprendre le flux et de garder les tokens à courte durée de vie et bien gardés.