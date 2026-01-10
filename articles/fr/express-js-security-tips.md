---
title: 'Conseils de sécurité Express.js : Comment sauvegarder et sécuriser votre application'
subtitle: ''
author: Oleh Romanyuk
co_authors: []
series: null
date: '2019-10-10T13:03:00.000Z'
originalURL: https://freecodecamp.org/news/express-js-security-tips
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/PWA-min.png
tags:
- name: Express
  slug: express
- name: Express.js
  slug: expressjs
seo_title: 'Conseils de sécurité Express.js : Comment sauvegarder et sécuriser votre
  application'
seo_desc: 'Take 7 steps to make sure that your app is invincible

  Is your phone locked? Do you have a pin-code, password, fingerprint, or FaceID?
  I am 99 percent sure that you do. And it is clear why – you care about your safety.
  Nowadays, keeping your phone pro...'
---

# 7 étapes pour vous assurer que votre application est invincible

Votre téléphone est-il verrouillé ? Avez-vous un code PIN, un mot de passe, une empreinte digitale ou FaceID ? Je suis sûr à 99 % que oui. Et il est clair pourquoi – vous tenez à votre sécurité. De nos jours, garder votre téléphone protégé est aussi important que de vous brosser les dents le matin.

Pour les développeurs de logiciels diligents et attentifs, garder leur application sécurisée est tout aussi important que de protéger leur téléphone. Si vous êtes un développeur et que vous choisissez de le négliger – s'il vous plaît, reconsidérez votre approche. Si vous êtes propriétaire d'un projet et que votre équipe de développement dit que la sécurité des données peut attendre, s'il vous plaît, reconsidérez votre équipe.

Dans cet article, je veux parler de la manière de vous assurer que votre projet [<ins>Express.js</ins>](https://keenethics.com/tech-back-end-express) est sûr et invincible face aux attaques malveillantes.

Il existe 7 mesures simples et moins simples à prendre pour assurer la sécurité des données :

1. **Utilisez des versions fiables d'Express.js**
2. **Sécurisez la connexion et les données**
3. **Protégez vos cookies**
4. **Sécurisez vos dépendances**
5. **Validez l'entrée de vos utilisateurs**
6. **Protégez votre système contre les attaques par force brute**
7. **Contrôlez l'accès des utilisateurs**

Examinons chacun de plus près.

## **1. Utilisez des versions fiables d'Express.js**

Les versions obsolètes ou dépassées d'Express.js sont à éviter. Les 2e et 3e versions d'Express ne sont plus supportées. Dans ces versions, les problèmes de sécurité ou de performance ne sont plus corrigés.

En tant que développeur, vous devez absolument [migrer vers Express 4](https://expressjs.com/en/guide/migrating-4.html). Cette version est une révolution ! Elle est assez différente en termes de système de routage, de middleware et d'autres aspects mineurs.

## **2. Sécurisez la connexion et les données**

Pour sécuriser les en-têtes HTTP, vous pouvez utiliser [<ins>Helmet.js</ins>](https://helmetjs.github.io/) – un module Node.js utile. Il s'agit d'une collection de 13 fonctions middleware pour définir les en-têtes de réponse HTTP. En particulier, il existe des fonctions pour définir la politique de sécurité du contenu, gérer la transparence des certificats, prévenir le clickjacking, désactiver la mise en cache côté client ou ajouter des protections XSS.

```js
npm install helmet --save
```

Même si vous ne souhaitez pas utiliser toutes les fonctions de Helmet, le minimum absolu que vous devez faire est de désactiver l'en-tête X-Powered-By :

```js
app.disable('x-powered-by')
```

Cet en-tête peut être utilisé pour détecter que l'application est alimentée par Express, ce qui permet aux pirates de mener une attaque précise. Bien sûr, l'en-tête X-Powered-By n'est pas le seul moyen d'identifier une application exécutée par Express, mais c'est probablement le plus courant et le plus simple.

Pour protéger votre système contre les attaques de pollution des paramètres HTTP, vous pouvez utiliser [<ins>HPP</ins>](https://www.npmjs.com/package/hpp). Ce middleware met de côté des paramètres tels que req.query et req.body et sélectionne la dernière valeur de paramètre à la place. La commande d'installation est la suivante :

```js
npm install hpp --save
```

Pour chiffrer les données envoyées du client au serveur, utilisez Transport Layer Security (TLS). TLS est un protocole cryptographique pour sécuriser le réseau informatique, le descendant du chiffrement Secure Socket Layer (SSL). TLS peut être géré avec [<ins>Nginx</ins>](https://www.nginx.com/) – un serveur HTTP gratuit mais efficace – et [<ins>Let's Encrypt</ins>](https://letsencrypt.org/about/) – un certificat TLS gratuit.

## **3. Protégez vos cookies**

Dans Express.js 4, il existe deux modules de session de cookies :

* express-session (dans Express.js 3, c'était express.session)
* cookie-session (dans Express.js 3, c'était express.cookieSession)

Le module express-session stocke l'ID de session dans le cookie et les données de session sur le serveur. Le cookie-session stocke toutes les données de session dans le cookie.

En général, cookie-session est plus efficace. Cependant, si les données de session que vous devez stocker sont complexes et susceptibles de dépasser 4096 octets par cookie, utilisez express-session. Une autre raison d'utiliser express-session est lorsque vous devez garder les données du cookie invisibles pour le client.

De plus, vous devez définir les options de sécurité des cookies, à savoir :

* secure
* httpOnly
* domain
* path
* expires

Si « secure » est défini sur « true », le navigateur enverra les cookies uniquement via HTTPS. Si « httpOnly » est défini sur « true », le cookie sera envoyé non pas via le JS client, mais via HTTP(S). La valeur de « domain » indique le domaine du cookie. Si le domaine du cookie correspond au domaine du serveur, « path » est utilisé pour indiquer le chemin du cookie. Si le chemin du cookie correspond au chemin de la requête, le cookie sera envoyé dans la requête. Enfin, comme son nom l'indique, la valeur de « expires » représente le moment où les cookies expireront.

Une autre recommandation importante est de ne pas utiliser le nom de cookie de session par défaut. Cela pourrait permettre aux pirates de détecter le serveur et de lancer une attaque ciblée. Utilisez plutôt des noms de cookies génériques.

## **4. Sécurisez vos dépendances**

Sans aucun doute, npm est un outil puissant de développement web. Cependant, pour garantir le plus haut niveau de sécurité, envisagez d'utiliser uniquement la 6e version – [<ins>npm@6</ins>](https://www.npmjs.com/package/npm/v/6.0.1). Les versions plus anciennes peuvent contenir des vulnérabilités de sécurité sérieuses, ce qui mettra en danger toute votre application. De plus, pour analyser l'arborescence des dépendances, utilisez la commande suivante :

```js
npm audit
```

npm audit peut aider à corriger des problèmes réels dans votre projet. Il vérifie toutes vos dépendances dans dependencies, devDependencies, bundledDependencies et optionalDependencies, mais pas vos peerDependencies. [<ins>Ici</ins>](https://www.npmjs.com/advisories) vous pouvez lire sur toutes les vulnérabilités actuelles dans les packages npm.

![Sécuriser les dépendances](https://images.ctfassets.net/6xhdtf1foerq/2LwpppvohhSerxOi2K7yNp/5a7869f23e9474fe9fe6b6e61a956322/Screenshot_2019-10-07_at_5.07.57_PM.png?fm=png&q=85&w=1000)

Un autre outil pour garantir la sécurité des dépendances est [<ins>Snyk</ins>](https://snyk.io/). Snyk exécute la vérification de l'application pour identifier si elle contient une vulnérabilité répertoriée dans la base de données open-source de Snyk. Pour effectuer la vérification, exécutez trois étapes simples.

### Étape 1. Installer Snyk

```js
npm install -g snyk
cd votre-app
```

### Étape 2. Exécuter un test

```js
snyk test
```

### Étape 3. Apprendre à corriger le problème

```js
snyk wizard
```

Wizard est une méthode Snyk qui explique la nature de la vulnérabilité de la dépendance et propose des moyens de la corriger.

## **5. Validez l'entrée de vos utilisateurs**

Contrôler l'entrée des utilisateurs est une partie extrêmement importante pour le développement côté serveur. Ce n'est pas un problème moins important que les requêtes non autorisées, qui seront décrites dans la septième partie de cet article.

Tout d'abord, une mauvaise entrée utilisateur peut casser votre serveur lorsque certaines valeurs sont indéfinies et que vous n'avez pas de gestion des erreurs pour un endpoint spécifique. Cependant, différents systèmes ORM peuvent avoir un comportement imprévisible lorsque vous essayez de définir des valeurs indéfinies, nulles ou d'autres types de données dans la base de données.

Par exemple, la méthode destroyAll dans Loopback.js ORM (framework Node.js) peut détruire toutes les données dans une table de la base de données : lorsqu'elle ne correspond à aucun enregistrement, elle supprime tout comme décrit [ici](https://www.npmjs.com/package/npm/v/6.0.1). Imaginez que vous pouvez perdre toutes les données dans une table de production simplement parce que vous avez ignoré la validation de l'entrée.

### Utilisez la validation du corps/objet pour les inspections intermédiaires

Pour commencer, vous pouvez utiliser la validation du corps/objet pour les inspections intermédiaires. Par exemple, nous utilisons le validateur ajv qui est le validateur de schéma JSON le plus rapide pour Node.js.

```js
const Ajv = require('ajv'); 
const ajv = new Ajv({allErrors: true}); 
const speaker = { 
  'type': 'object', 
  'required': [
    'id', 
    'name'
  ],
  'properties': { 
    'id': {
      'type': 'integer', 
    }, 
    'name': { 
      'type': 'string',
    }, 
  }, 
};
const conversation = { 
  type: 'object', 
  required: [
    'duration', 
    'monologues'
  ], 
  properties: { 
    duration: { 
      type: 'integer',
    }, 
    monologues: { 
      type: 'array', 
      items: monolog, 
    }, 
  }, 
};
const body = { 
  type: 'object', 
  required: [
    'speakers', 
    'conversations'
  ], 
  properties: { 
    speakers: { 
      type: 'array', 
      items: speaker, 
    }, 
    conversations: { 
      type: 'array', 
      items: conversation, 
    }, 
  }, 
}; 
const validate = ajv.compile(body); 
const isValidTranscriptBody = transcriptBody => { 
  const isValid = validate(transcriptBody);
  if (!isValid) { 
    console.error(validate.errors); 
  } 
  return isValid; 
};
```

### Gérer les erreurs

Maintenant, imaginez que vous avez oublié de vérifier un certain objet et que vous effectuez des opérations avec la propriété indéfinie. Ou vous utilisez une certaine bibliothèque et vous obtenez une erreur. Cela peut casser votre instance, et le serveur va planter. Ensuite, l'attaquant peut pinguer un endpoint spécifique où se trouve cette vulnérabilité et peut arrêter votre serveur pendant une longue période.

Le moyen le plus simple de gérer les erreurs est d'utiliser la construction try-catch :

```js
try { 
  const data = body;
  if (data.length === 0) throw new Error('Client Error'); 
  const beacons = await  this.beaconLogService.filterBeacon(data); 
  if (beacons.length > 0) { 
    const max = beacons.reduce((prev, current) => (prev.rssi > current.rssi) ? prev : current); 
    await this.beaconLogService.save({ 
      ...max,
      userId: headers['x-uuid'] 
    }); 
    return { 
      data: { 
        status: 'Saved', 
        position: max 
      }, 
    }; 
  } 
  return { 
    data: { 
      status: 'Not valid object', 
    }, 
  }; 
} 
catch(err) { 
  this.logger.error(err.message, err.stack); 
  throw new HttpException('Server Error',     HttpStatus.INTERNAL_SERVER_ERROR); 
}
```

N'hésitez pas à utiliser un nouveau constructeur Error('message') pour la gestion des erreurs ou même à étendre cette classe pour vos propres besoins !

### Utilisez JOI

La leçon principale ici est que vous devez toujours valider l'entrée de l'utilisateur pour ne pas devenir victime d'attaques de type man-in-the-middle. Une autre façon de le faire est avec l'aide de [<ins>@hapi/joi</ins>](https://www.npmjs.com/package/@hapi/joi) – une partie de l'écosystème hapi et une puissante bibliothèque de validation de données JS.

Faites attention ici que le module [<ins>joi</ins>](https://www.npmjs.com/package/joi) a été obsolète. Pour cette raison, la commande suivante est à éviter :

```js
npm install joi
```

Utilisez plutôt celle-ci :

```js
npm install @hapi/joi
```

### Utilisez express-validator

Une autre façon de valider l'entrée de l'utilisateur est d'utiliser express-validator – un ensemble de middlewares express.js, qui comprend validator.js et un fonction de nettoyage. Pour l'installer, exécutez la commande suivante :

```js
npm install --save express-validator
```

### Nettoyer l'entrée de l'utilisateur

De plus, une mesure importante à prendre est de nettoyer l'entrée de l'utilisateur pour protéger le système contre une injection d'opérateurs MongoDB. Pour cela, vous devez installer et utiliser express-mongo-sanitize :

```js
npm install express-mongo-sanitize
```

### Protégez votre application contre CSRF

De plus, vous devez protéger votre application contre la falsification de requête inter-sites (CSRF). CSRF est lorsque des commandes non autorisées sont envoyées depuis un utilisateur de confiance. Vous pouvez le faire avec l'aide de [<ins>csurf</ins>](https://www.npmjs.com/package/csurf). Avant cela, vous devez vous assurer que le middleware de session pour les cookies est configuré comme décrit précédemment dans cet article. Pour installer ce module Node.js, exécutez la commande :

```js
npm install csurf
```

## **6. Protégez votre système contre les attaques par force brute**

Une attaque par force brute est le moyen le plus simple et le plus courant d'obtenir un accès à un site web ou à un serveur. Le pirate (dans la plupart des cas automatiquement, rarement manuellement) essaie divers noms d'utilisateur et mots de passe à plusieurs reprises pour pénétrer dans le système.

Ces attaques peuvent être prévenues avec l'aide du package [<ins>rate-limiter-flexible</ins>](https://github.com/animir/node-rate-limiter-flexible). Ce package est rapide, flexible et adapté à tout framework Node.

Pour installer, exécutez la commande suivante :

```js
npm i --save rate-limiter-flexible
yarn add rate-limiter-flexible
```

Cette méthode a une alternative plus simple mais plus primitive : [<ins>express-rate-limit</ins>](https://www.npmjs.com/package/express-rate-limit). La seule chose qu'elle fait est de limiter les requêtes répétées aux API publiques ou à la réinitialisation du mot de passe.

```js
npm install --save express-rate-limit
```

## **7. Contrôlez l'accès des utilisateurs**

Parmi les méthodes d'authentification, il y a les tokens, Auth0 et JTW. Concentrons-nous sur le troisième ! JTW (JSON Web Tokens) sont utilisés pour transférer les données d'authentification dans les applications client-serveur. Les tokens sont créés par le serveur, signés avec une clé secrète et transférés à un client. Ensuite, le client utilise ces tokens pour confirmer son identité.

[<ins>Express-jwt-permissions</ins>](https://www.npmjs.com/package/express-jwt-permissions) est un outil utilisé avec [<ins>express-jwt</ins>](https://github.com/auth0/express-jwt) pour vérifier les permissions d'un certain token. Ces permissions sont un tableau de chaînes à l'intérieur du token :

```js
"permissions": [
  "status",
  "user:read",
  "user:write"
]
```

Pour installer l'outil, exécutez la commande suivante :

```js
npm install express-jwt-permissions --save
```

## **Pour conclure**

Ici, j'ai listé les meilleures pratiques essentielles de sécurité pour Express.js et quelques outils qui peuvent être utilisés en cours de route.

### **Pour réviser :**

![Sécuriser les dépendances](https://images.ctfassets.net/6xhdtf1foerq/2LwpppvohhSerxOi2K7yNp/5a7869f23e9474fe9fe6b6e61a956322/Screenshot_2019-10-07_at_5.07.57_PM.png?fm=png&q=85&w=1000)

Je vous recommande vivement de vous assurer que votre application est résistante aux attaques malveillantes. Sinon, votre entreprise et vos utilisateurs pourraient subir des pertes importantes.

## Avez-vous une idée pour un projet Express.js ?

Mon entreprise KeenEthics est expérimentée dans le [développement express js](https://keenethics.com/tech-back-end-express). Si vous avez besoin d'une estimation gratuite d'un projet similaire, n'hésitez pas à [nous contacter](https://keenethics.com/contacts).

Si vous avez apprécié l'article, vous devriez définitivement continuer avec un article sur la sécurité des données dans l'externalisation en Ukraine : [L'équipe KeenEthics en garde : vos données sont en sécurité en Ukraine](https://keenethics.com/blog/1543388400000-your-data-is-safe-in-ukraine?utm_source=freecodecamp&utm_medium=freecodecamp&utm_campaign=freecodecamp). L'article original publié sur le blog de KeenEthics peut être trouvé ici : [conseils de sécurité express js](https://keenethics.com/blog/express-js-security-tips).

## P.S.

Un énorme merci à [Volodia Andrushchak](https://www.linkedin.com/in/andrushchak-volodia-167430125/), Développeur Logiciel Full-Stack @KeenEthics pour m'avoir aidé avec l'article.

L'article original publié sur le blog de KeenEthics peut être trouvé ici : [Conseils de sécurité Express.js : Sauvez votre application !](https://keenethics.com/blog/express-js-security-tips)

#