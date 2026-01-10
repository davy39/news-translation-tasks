---
title: Comment créer un serveur sécurisé avec Node.js et Express et téléverser des
  images avec Cloudinary
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-12-14T16:51:14.000Z'
originalURL: https://freecodecamp.org/news/build-a-secure-server-with-node-and-express
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/pexels-aleksandar-pasaric-325185.jpg
tags:
- name: Express
  slug: express
- name: node js
  slug: node-js
- name: servers
  slug: servers
- name: Web Security
  slug: web-security
seo_title: Comment créer un serveur sécurisé avec Node.js et Express et téléverser
  des images avec Cloudinary
seo_desc: 'By Njoku Samson Ebere

  In this tutorial, we will learn how to create a server. We will begin without express
  and then strengthen the server using express. After that, we will see how to upload
  images to Cloudinary from the app we have created.

  I assum...'
---

Par Njoku Samson Ebere

Dans ce tutoriel, nous allons apprendre à créer un serveur. Nous commencerons sans `express` puis nous renforcerons le serveur en utilisant `express`. Après cela, nous verrons comment téléverser des images vers Cloudinary depuis l'application que nous avons créée.

Je suppose que vous comprenez déjà les bases de `Node.js`, `express` et `nodemon`, donc nous allons directement aux parties pratiques.

## Installer Node.js et NPM

Si vous ne l'avez pas encore fait, vous devrez installer Node et npm sur votre machine.

1. Allez sur le [site web de Node.js](https://nodejs.org/en/)
2. Cliquez sur le bouton de téléchargement recommandé

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screenshot-2021-12-13-at-18.52.57.png)
_Page d'accueil de Node.js_

Lorsque le téléchargement est terminé, installez Node en utilisant le fichier `.exe` téléchargé (il suit le processus d'installation normal).

### Vérifier si l'installation a réussi

1. Allez dans votre terminal/invite de commande _(exécutez en tant qu'administrateur si possible)_
2. Tapez chacune des commandes suivantes et appuyez sur Entrée

```javascript
node -v 
npm -v
```

Votre sortie devrait être similaire à l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/termial-1.jpeg)
_Terminal montrant les versions de node et npm_

La version peut être différente mais ce n'est pas grave.

## Comment créer un serveur Node sans Express

Pour le reste de ce tutoriel, j'utiliserai VS code comme éditeur. Vous pouvez utiliser l'éditeur de votre choix.

Commençons par créer un répertoire de projet. Ouvrez un terminal et tapez ce qui suit pour créer un répertoire et l'ouvrir :

```javascript

mkdir server-tutorial cd server-tutorial

```

J'ai nommé mon répertoire de projet `server-tutorial`, mais vous pouvez nommer le vôtre comme vous le souhaitez.

Dans le terminal, tapez `npm init`. Appuyez sur le bouton `Entrée` pour toutes les invites. Une fois terminé, vous devriez avoir un fichier `package.json` dans votre répertoire de projet.

Le fichier `package.json` est simplement un fichier avec tous les détails de votre projet. Vous n'avez pas besoin de l'ouvrir.

Créez un fichier appelé `index.js`.

Dans le fichier, requérez le module `HTTP` comme suit :

```javascript
  const http = require('http');

```

Appelez la méthode `createServer()` et attribuez-la à une constante comme ceci :

```javascript
  const server = http.createServer();

```

Appelez la méthode `listen()` sur la constante du serveur comme ceci :

```javascript
  server.listen();

```

Donnez-lui un port à écouter. Cela pourrait être n'importe quel port libre, mais nous utiliserons le port `3000` qui est le port conventionnel. Donc nous avons ceci :

```javascript
  const http = require('http');

  const server = http.createServer();

  server.listen(3000);

```

En gros, c'est tout ce que vous devez faire pour créer un serveur.

### Comment tester le serveur

Dans votre terminal (devrait être dans le répertoire du projet), tapez `node index.js` et appuyez sur le bouton `Entrée`.

Ouvrez un nouvel onglet dans [`postman`](https://www.getpostman.com/) ou n'importe quel navigateur web et dans la barre d'adresse, tapez `http://localhost:3000/`, et appuyez sur le bouton `Entrée`. (J'utiliserai postman en raison de ses fonctionnalités étendues hors de la boîte.)

Vous remarquerez que votre navigateur ou postman continue de charger indéfiniment comme ceci :

![Postman Loading Indefinitely](https://dev-to-uploads.s3.amazonaws.com/i/fp7k6pcfctn0548n0rmx.JPG)

Youpi ! C'est bien. Notre serveur est opérationnel.

Mais c'est déjà ennuyeux. Nous devons faire parler le serveur.

Commençons immédiatement.

### Comment renvoyer une réponse du serveur

De retour dans le code, ajoutez ce qui suit à `const server = http.createServer();` :

```javascript
 (request, response) => {
    response.end('Hey! This is your server response!');
 }

```

Nous avons maintenant :

```javascript
  const http = require('http');

  const server = http.createServer((request, response) => {
    response.end('Hey! This is your server response!');
  });

server.listen(3000);

```

En termes simples, l'objet `request` indique au `server` que nous voulons quelque chose, l'objet `response` nous indique ce que le `server` a à dire sur notre `request`, et la méthode `end()` termine la communication avec le `server` `response`.

Espérons que cela ait du sens !

Maintenant, testez à nouveau le serveur en suivant les étapes que nous avons décrites ci-dessus et votre serveur devrait vous parler. Voici ma sortie :

![Postman returning a response](https://dev-to-uploads.s3.amazonaws.com/i/b0189qzrdkppbvr57uo8.JPG)

N'hésitez pas à changer la chaîne comme vous le souhaitez.

Utilisez `Control/Command + C` pour terminer le serveur et exécutez `node index` pour redémarrer le serveur.

Ça a l'air bien ! N'est-ce pas ? Tout va bien...

## Comment créer un serveur Node avec Express

Dans cette section, nous voulons faciliter notre vie en utilisant `Express` et `Nodemon` (node-mon ou no-demon, prononcez-le comme vous le souhaitez).

Dans le terminal, installez ce qui suit :

```
npm install express --save 
npm install nodemon --save-dev
```

Créez un nouveau fichier nommé `app.js` ou tout autre nom qui vous convient.

Dans le fichier,

1. Requérez express comme suit :

`const express = require('express');`

2.   Attribuez la méthode express à une constante comme ceci :

`const app = express();`

3.   Exportez la constante app pour la rendre disponible pour une utilisation dans d'autres fichiers du répertoire comme suit :

`module.exports = app;`

Nous avons donc :

```javascript
const express = require('express');

const app = express();



module.exports = app;

```

Dans le fichier `index.js`, requérez l'`app` que nous avons exportée il y a un moment :

`const app = require('./app');`

Ensuite, définissez le port en utilisant l'application comme suit :

`app.set('port', 3000);`

Et remplacez le code dans la méthode `http.createServer()` par simplement `app` comme ceci :

`const server = http.createServer(app);`

Cela dirige toute la gestion de l'API vers le fichier `app.js`, aidant à la séparation des préoccupations.

Notre fichier `index.js` ressemble maintenant à ceci :

```javascript
const http = require('http');
const app = require('./app');

app.set('port', 3000);
const server = http.createServer(app);

server.listen(3000);

```

De retour dans notre fichier `app.js`, puisque nous avons dirigé toute la gestion de l'API vers celui-ci, créons un endpoint pour nous parler comme avant.

Donc, avant la ligne `module.exports = app`, ajoutez le code suivant :

```javascript
app.use((request, response) => {
   response.json({ message: 'Hey! This is your server response!' }); 
});

```

Nous avons maintenant :

```javascript
const express = require('express');

const app = express();

app.use((request, response) => {
   response.json({ message: 'Hey! This is your server response!' }); 
});

module.exports = app;

```

Ahaaa... Il est temps de tester notre application.

Pour tester notre application, nous tapons maintenant `nodemon index` dans notre terminal et appuyons sur le bouton `Entrée`. Voici mon terminal :

![Terminal running nodemon](https://dev-to-uploads.s3.amazonaws.com/i/1gy6psmeylb6onbbt18i.JPG)

Remarquez-vous que nodemon nous donne des détails d'exécution dans le terminal contrairement à Node ? C'est la beauté de nodemon.

Vous pouvez maintenant aller dans `postman` ou n'importe quel `navigateur` et dans la barre d'adresse, tapez `http://localhost:3000/` et appuyez sur `Entrée`. Voici ma sortie :

![Postman returning response from express app](https://dev-to-uploads.s3.amazonaws.com/i/m4yrqaf3d235xo7hjqae.JPG)

**Walah ! Ça marche.**

Maintenant, plus de raisons d'utiliser nodemon. Allez dans le fichier `app.js` et changez la chaîne `message` en n'importe quelle chaîne de votre choix, enregistrez, et regardez le `terminal`.

![nodemon restarting after changes](https://dev-to-uploads.s3.amazonaws.com/i/qcslu7vqa746nq5hvjwk.JPG)

Wow... Il redémarre automatiquement le serveur. Cela était impossible avec Node. Nous devions redémarrer le serveur nous-mêmes.

## Comment sécuriser le serveur et le rendre prêt pour l'avenir

Dans le fichier `index.js`, remplacez tout le code par ce qui suit :

```javascript
const http = require('http');
const app = require('./app');

const normalizePort = val => {
  const port = parseInt(val, 10);

  if (isNaN(port)) {
    return val;
  }
  if (port >= 0) {
    return port;
  }
  return false;
};
const port = normalizePort(process.env.PORT || '3000');
app.set('port', port);

const errorHandler = error => {
  if (error.syscall !== 'listen') {
    throw error;
  }
  const address = server.address();
  const bind = typeof address === 'string' ? 'pipe ' + address : 'port: ' + port;
  switch (error.code) {
    case 'EACCES':
      console.error(bind + ' requires elevated privileges.');
      process.exit(1);
      break;
    case 'EADDRINUSE':
      console.error(bind + ' is already in use.');
      process.exit(1);
      break;
    default:
      throw error;
  }
};

const server = http.createServer(app);

server.on('error', errorHandler);
server.on('listening', () => {
  const address = server.address();
  const bind = typeof address === 'string' ? 'pipe ' + address : 'port ' + port;
  console.log('Listening on ' + bind);
});

server.listen(port);

```

`process.env.PORT` rend l'application dynamique afin qu'elle puisse exécuter n'importe quel port qui lui est attribué à l'avenir lorsqu'elle est hébergée sur un serveur en direct.

La fonction `normalizePort` retourne un port valide, qu'il soit fourni sous forme de nombre ou de chaîne.

La fonction `errorHandler` vérifie diverses erreurs et les gère de manière appropriée — elle est ensuite enregistrée sur le serveur.

Un écouteur d'événement `listening` est également enregistré, enregistrant le port ou le pipe nommé sur lequel le serveur est en cours d'exécution dans la console.

YooH ! Notre serveur est plus sécurisé et robuste maintenant. Remarquez que nodemon affiche également le port que nous écoutons.

Vous l'avez, un serveur Node.js simple, sécurisé et robuste.

## Comment téléverser des images vers Cloudinary

Maintenant que nous avons un serveur cool en cours d'exécution, apprenons comment nous pouvons sauvegarder nos images sur Cloudinary. Ce ne sera qu'une introduction de base, donc ce devrait être amusant 😊.

[Cloudinary](https://cloudinary.com/) aide les développeurs du monde entier à gérer des images avec un effort minimal.

### Comment créer un compte Cloudinary

Pour créer un compte, allez sur le [site web de Cloudinary](https://cloudinary.com/).

1. Cliquez sur le bouton `s'inscrire` en haut à droite.
2. Remplissez le formulaire qui apparaît en conséquence.
3. Soumettez le formulaire en utilisant le bouton `Créer un compte`.
4. Vérifiez votre email pour terminer en validant votre email

Vous devriez pouvoir accéder à votre tableau de bord qui ressemble au mien ci-dessous :

![Cloudinary Dashboard](https://dev-to-uploads.s3.amazonaws.com/i/qfiw7cobdp7pv3c0fb65.JPG)

Remarquez les `détails du compte`. Vous **ne devriez pas révéler ces informations à qui que ce soit**. Je vous les montre ici parce que c'est un compte temporaire que j'utilise uniquement pour les besoins de ce tutoriel.

Consultez également l'onglet `Bibliothèque de médias`. C'est là que les images téléversées apparaîtront.

Si vous avez tout cela, alors commençons...

### Comment installer Cloudinary dans notre projet

Ouvrez votre terminal et naviguez dans le répertoire du projet.

Exécutez la commande suivante pour installer `Cloudinary` :

```javascript
  npm install cloudinary --save

```

### Comment configurer Cloudinary dans notre projet

Dans le fichier app.js, requérez `cloudinary` sous le `const app = express();` comme suit :

```javascript
  const cloudinary = require('cloudinary').v2

```

Ensuite, ajoutez les détails de configuration à partir des détails du compte sur votre tableau de bord comme ceci :

```javascript
    cloud_name: 'placez votre cloud_name ici',
    api_key: 'placez votre api_key ici',
    api_secret: 'placez votre api_secret ici',

```

Voici ce que j'ai :

```javascript
  // configuration cloudinary
  cloudinary.config({
    cloud_name: "dunksyqjj",
    api_key: "173989938887513",
    api_secret: "ZPLqvCzRu55MaM1rt-wxJCmkxqU"
  });

```

### Comment créer un EndPoint pour téléverser une image

Pour éviter les bugs dans notre code, remplacez d'abord l'API existante par le code suivant :

```javascript
  app.get("/", (request, response) => {
    response.json({ message: "Hey! This is your server response!" });
  });

```

C'est essentiellement la même chose, mais cette fois, nous utilisons le verbe `get` à la place du verbe `use` et nous avons ajouté un endpoint racine (`/`).

Ensuite, juste avant la ligne `module.exports = app;`, nous allons créer notre API `image-upload`.

Commençons par placer ce code là :

```javascript
// API de téléversement d'image
app.post("/upload-image", (request, response) => {});

```

En gros, voici comment nous configurons une API. L'API fait une `requête POST` au `serveur`, indiquant au `serveur` que la `requête` doit être traitée avec un certain niveau de sécurité. Elle utilise deux paramètres pour faire cette requête : un `endpoint` (/upload-image) et une `fonction de rappel` ((request, response) => {}).

Donnons vie à l'API en construisant la `fonction de rappel`.

### Comment construire la fonction de rappel

#### Installer [body-parser](https://www.npmjs.com/package/body-parser)

Ce package npm nous permet de gérer les requêtes entrantes en utilisant `req.body` ou `request.body` selon le cas. Nous allons installer `body-parser` en utilisant le code suivant :

```javascript
  npm install --save body-parser

```

#### Configurer body-parser pour notre projet

Requérez body-parser dans app.js comme suit :

```javascript
const bodyParser = require('body-parser');

```

Ensuite, ajoutez le code suivant pour définir sa fonction `json` comme middleware global pour notre application comme suit :

```javascript
  app.use(bodyParser.json());
  app.use(bodyParser.urlencoded({ extended: true }));

```

Nous pouvons maintenant gérer le corps de notre requête de manière appropriée.

### Retour à la construction de notre fonction

Dans la fonction, ajoutez le code suivant pour collecter les données (images) entrées par un utilisateur :

```javascript
    // image collectée d'un utilisateur
    const data = {
        image: request.body.image,
    };

```

Ensuite, téléversez l'image vers `cloudinary` en utilisant le code suivant :

```javascript
cloudinary.uploader.upload(data.image);

```

En gros, c'est tout ce dont nous avons besoin pour téléverser notre image. Donc notre `app.js` ressemble à ceci :

```javascript
const express = require("express");
const app = express();
const cloudinary = require("cloudinary").v2;
const bodyParser = require('body-parser');

// configuration du body parser
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// configuration cloudinary
cloudinary.config({
  cloud_name: "dunksyqjj",
  api_key: "173989938887513",
  api_secret: "ZPLqvCzRu55MaM1rt-wxJCmkxqU"
});

app.get("/", (request, response) => {
  response.json({ message: "Hey! This is your server response!" });
});

// API de téléversement d'image
app.post("/image-upload", (request, response) => {
    // image collectée d'un utilisateur
    const data = {
      image: request.body.image,
    }

    // téléverser l'image ici
    cloudinary.uploader.upload(data.image);
    
});

module.exports = app;

```

Maintenant, cela a l'air bien et cela fonctionne parfaitement. Vous pouvez le tester en utilisant `postman`. Mais ce serait génial si notre application pouvait nous donner un retour lorsque le traitement de nos requêtes est terminé, n'est-ce pas ?

Pour que cela se produise, nous allons ajouter le bloc `then...catch...` suivant au téléversement cloudinary comme ceci :

```javascript
    // téléverser l'image ici
    cloudinary.uploader.upload(data.image)
    .then((result) => {
      response.status(200).send({
        message: "success",
        result,
      });
    }).catch((error) => {
      response.status(500).send({
        message: "failure",
        error,
      });
    });

```

Donc notre code final sera :

```javascript
const express = require("express");
const app = express();
const cloudinary = require("cloudinary").v2;
const bodyParser = require('body-parser');

// configuration du body parser
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// configuration cloudinary
cloudinary.config({
  cloud_name: "dunksyqjj",
  api_key: "173989938887513",
  api_secret: "ZPLqvCzRu55MaM1rt-wxJCmkxqU"
});

app.get("/", (request, response) => {
  response.json({ message: "Hey! This is your server response!" });
});

// API de téléversement d'image
app.post("/image-upload", (request, response) => {
    // image collectée d'un utilisateur
    const data = {
      image: request.body.image,
    }

    // téléverser l'image ici
    cloudinary.uploader.upload(data.image)
    .then((result) => {
      response.status(200).send({
        message: "success",
        result,
      });
    }).catch((error) => {
      response.status(500).send({
        message: "failure",
        error,
      });
    });
    
});

module.exports = app;

```

### Comment tester notre API

Créez un dossier/répertoire dans le répertoire racine et nommez-le `images` comme suit :

```javascript
  mkdir images

```

Copiez une image de votre choix dans ce dossier. (Maintenant, le chemin vers votre image par rapport au fichier app.js devrait ressembler à ceci : `"images/<votre-image.jpg">`.)

Maintenant, procédons à `postman`.

1. Dans la barre d'adresse, entrez ceci : `http://localhost:3000/image-upload`
2. Définissez la clé `Header` sur `Content-Type` et la valeur sur `application/json`
3. Définissez le `body` sur les données `json` que nous avons déclarées dans notre code comme suit :

```javascript
       {
	   "image": "images/oskar-yildiz-gy08FXeM2L4-unsplash.jpg"
       }

```

Appuyez sur le bouton `Send` et attendez que le téléversement soit terminé et obtenez votre réponse :

![Postman setup to upload image](https://dev-to-uploads.s3.amazonaws.com/i/ate77jhmka2agj3nxip2.JPG)

Maintenant, voici le résultat. L'image a maintenant un `public_id` unique qui est généré aléatoirement par Cloudinary et une `secure_url` qui est accessible globalement (vous pouvez la charger dans votre navigateur pour la voir).

![Postman showing result of upload](https://dev-to-uploads.s3.amazonaws.com/i/wys21hgc58nl4rfmq63i.JPG)

Enfin, en vérifiant l'onglet `Bibliothèque de médias` sur votre tableau de bord Cloudinary, vous devriez avoir une nouvelle image avec un badge `new` dessus. Cela aura un identifiant unique qui correspond au `public_id` que nous avons vu dans le résultat de postman ci-dessus, comme dans l'image ci-dessous :

![Cloudinary Media Files](https://dev-to-uploads.s3.amazonaws.com/i/vkvevngtumyfdd105suu.JPG)

Walah ! Nous persistons les images sans stress... Cela fait du bien.

Eh bien, une dernière chose — SÉCURITÉ !

Nos détails de configuration Cloudinary sont exposés dans notre fichier app.js. Si nous poussons notre projet vers GitHub, il devient accessible au public pour quiconque souhaite le consulter. Et cela devient un problème s'il tombe entre de mauvaises mains.

Mais ne vous inquiétez pas, il existe une solution pour presque tout dans cet espace. Nous allons utiliser le package npm `dotenv` pour masquer nos configurations au public.

## Comment sécuriser nos configurations avec `dotenv`

Tout d'abord, vous devrez installer [dotenv](https://www.npmjs.com/package/dotenv) si ce n'est pas déjà fait :

```javascript
npm install dotenv --save

```

Ensuite, requérez `dotenv` dans `app.js` comme suit :

```javascript
  require('dotenv').config()

```

Créez un nouveau fichier dans le répertoire racine et nommez-le `.env`.

Dans le fichier, entrez vos détails de configuration Cloudinary comme suit :

```javascript
  CLOUD_NAME=dunksyqjj
  API_KEY=173989938887513
  API_SECRET=ZPLqvCzRu55MaM1rt-wxJCmkxqU

```

Dans le fichier app.js, nous accéderons aux configurations dans le fichier `.env` via la propriété `process.env` comme suit :

```javascript
// configuration cloudinary
cloudinary.config({
  cloud_name: process.env.CLOUD_NAME,
  api_key: process.env.API_KEY,
  api_secret: process.env.API_SECRET
});

```

Voici mon code `app.js` pour le moment :

```javascript
const express = require("express");
const app = express();
const cloudinary = require("cloudinary").v2;
const bodyParser = require('body-parser');
require('dotenv').config()

// configuration du body parser
app.use(bodyParser.json());
  app.use(bodyParser.urlencoded({ extended: true }));

// configuration cloudinary
cloudinary.config({
  cloud_name: process.env.CLOUD_NAME,
  api_key: process.env.API_KEY,
  api_secret: process.env.API_SECRET
});

app.get("/", (request, response, next) => {
  response.json({ message: "Hey! This is your server response!" });
  next();
});

// API de téléversement d'image
app.post("/image-upload", (request, response) => {
    // image collectée d'un utilisateur
    const data = {
      image: request.body.image,
    }

    // téléverser l'image ici
    cloudinary.uploader.upload(data.image)
    .then((result) => {
      response.status(200).send({
        message: "success",
        result,
      });
    }).catch((error) => {
      response.status(500).send({
        message: "failure",
        error,
      });
    });
});

module.exports = app;

```

Testons à nouveau notre application pour nous assurer que rien n'est cassé. Voici mon résultat :

![Cloudinary media library](https://dev-to-uploads.s3.amazonaws.com/i/d3a2b47shxlmext6o40j.JPG)

J'ai maintenant deux images identiques mais avec des `public_id` différents.

Et c'est tout !

Yeeeh ! Notre application est plus sécurisée qu'au début.

## Conclusion

Dans ce tutoriel, nous avons passé en revue les étapes impliquées dans la création d'un serveur en utilisant uniquement Node.js. Et après cela, nous avons amélioré notre serveur en utilisant Express et nodemon.

Enfin, nous avons vu comment téléverser une image vers Cloudinary via notre application Express et comment nos détails de configuration sont sécurisés en utilisant le package `dotenv`.

Ce n'est qu'une introduction. Vous pouvez faire beaucoup plus si vous jouez avec cette application.

Vous pouvez trouver le code de création du serveur [ici](https://github.com/EBEREGIT/server-tutorial/tree/create-server).

Et les codes de téléversement d'images sont disponibles [ici](https://github.com/EBEREGIT/server-tutorial/tree/cloudinary-upload).

Merci pour votre temps. 😊