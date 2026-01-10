---
title: Construire une API Node.js en moins de 30 minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-01-10T16:40:30.000Z'
originalURL: https://freecodecamp.org/news/building-a-simple-node-js-api-in-under-30-minutes-a07ea9e390d2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*s5LVdcugM62xzSvGUpTLWA.png
tags:
- name: api
  slug: api
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: Construire une API Node.js en moins de 30 minutes
seo_desc: 'By Scott Domes

  Node.js can be intimidating to beginners. But its flexible structure and lack of
  strict guidelines makes it seem more complicated than it is.

  This tutorial is a quick and simple guide to Node.js, the Express framework, and
  MongoDB, foc...'
---

Par Scott Domes

Node.js peut être intimidant pour les débutants. Mais sa structure flexible et son manque de directives strictes le rendent plus compliqué qu'il ne l'est en réalité.

Ce tutoriel est un guide rapide et simple pour Node.js, le framework Express et MongoDB, en se concentrant sur les routes REST fondamentales et les interactions de base avec la base de données. Vous allez construire un modèle d'API simple qui pourra ensuite être utilisé comme fondation pour n'importe quelle application.

**À qui s'adresse ce tutoriel** : Vous devriez avoir une compréhension de base des API REST et des opérations CRUD, ainsi que des connaissances de base en JavaScript. J'utilise ES6 (principalement des fonctions fléchées), mais rien de trop complexe.

Pour ce tutoriel, vous allez créer le squelette d'un back-end pour une application de prise de notes — pensez à [Google Keep](http://keep.google.com). Vous voulez pouvoir effectuer les quatre actions CRUD sur vos notes : créer, lire, mettre à jour et supprimer.

### Installation

Si vous n'avez pas Node installé, [voir ici](https://howtonode.org/how-to-install-nodejs).

Dans un nouveau répertoire, exécutez npm init, et suivez les invites, en donnant à votre application le nom de 'notable' (ou autre chose que vous préférez).

```bash
npm init
```

Une fois cela fait, vous devriez avoir un fichier *package.json* prêt à l'emploi dans votre répertoire. Cela signifie que vous pouvez commencer à installer les dépendances nécessaires pour votre projet.

Vous allez utiliser Express comme framework, MongoDB comme base de données, et un package appelé body-parser pour aider à gérer les requêtes JSON.

```bash
npm install --save express mongodb@2.2.16 body-parser
```

Je recommande également vivement d'installer Nodemon comme dépendance de développement. C'est un petit package simple qui redémarre automatiquement votre serveur lorsque les fichiers changent.

Si vous exécutez :

```bash
npm install --save-dev nodemon
```

Vous pouvez ensuite ajouter le script suivant à *package.json* :

```json
// package.json
  "scripts": {
    "dev": "nodemon server.js"
  },
```

Votre fichier *package.json* complet devrait ressembler à ceci :

```json
// package.json
{
  "name": "notable",
  "version": "1.0.0",
  "description": "",
  "main": "server.js",
  "scripts": {
    "dev": "nodemon server.js"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "body-parser": "^1.15.2",
    "express": "^4.14.0",
    "mongodb": "^2.2.16"
  },
  "devDependencies": {
    "nodemon": "^1.11.0"
  }
}
```

Maintenant, vous pouvez créer votre fichier *server.js* et commencer à construire votre API.

### Notre Serveur

Commençons par inclure toutes vos dépendances dans *server.js*.

```javascript
// server.js
const express = require('express');
const MongoClient = require('mongodb').MongoClient;
const bodyParser = require('body-parser');

const app = express();
```

Vous allez utiliser le MongoClient pour interagir avec votre base de données. Notez que vous initialisez également votre application comme une instance d'Express, votre framework.

La dernière chose que vous devez faire pour démarrer votre serveur est de dire à votre application de commencer à *écouter* les requêtes HTTP.

Vous pouvez spécifier un port et démarrer l'écoute comme suit :

```javascript
// server.js
const port = 8000;

app.listen(port, () => {
  console.log('Nous sommes en ligne sur ' + port);
});
```

Maintenant, si vous exécutez *npm run dev* (ou *node server.js* si vous n'avez pas installé Nodemon), vous devriez voir 'Nous sommes en ligne sur le port 8000' dans le terminal.

Votre serveur est en ligne. Mais il ne fait pas grand-chose. Ou quoi que ce soit, vraiment.

Corrigeons cela.

### Routes CRUD

Pour cet exemple, vous voulez construire 4 routes ; pour CRÉER une note, pour LIRE vos notes, pour METTRE À JOUR une note, et pour SUPPRIMER une note.

Cela vous donnera une bonne idée de la façon de structurer presque n'importe quelle route de base avec Node.

Pour tester votre API, cependant, vous devez imiter un client faisant des requêtes. Pour ce faire, vous allez utiliser une excellente application appelée [Postman](https://www.getpostman.com/). Elle vous permet de faire des requêtes HTTP simples avec des corps et des paramètres personnalisés.

Installez Postman, et commençons à configurer vos routes.

### Super Organisé

La plupart des tutoriels Node.js (et de nombreuses applications réelles) mettent toutes leurs routes dans un gros fichier *routes.js*. Cela me met un peu mal à l'aise. En revanche, diviser vos fichiers en dossiers séparés conduit à une bonne lisibilité et rend les grandes applications plus gérables.

Vous n'avez pas une grosse application, mais faisons cela correctement. Créez les répertoires suivants : un dossier *app* avec un dossier routes à l'intérieur, avec un fichier *index.js* et un fichier *note_routes.js* à l'intérieur.

En d'autres termes : racine > app > routes > index.js et note_routes.js.

```bash
mkdir app
cd app
mkdir routes
cd routes
touch index.js
touch note_routes.js
```

Ces répertoires peuvent sembler excessifs pour votre petite application simple, mais il est toujours bon de commencer avec les meilleures pratiques.

### Votre Première Route

Commençons par le C dans CRUD - créer. Comment créer une note ?

Eh bien, avant de faire cela, vous devez construire un peu plus d'infrastructure. Dans Express, les routes sont enveloppées dans une fonction, qui prend l'instance Express et une base de données comme arguments.

Comme ceci :

```javascript
// routes/note_routes.js
module.exports = function (app, db) {

};
```

Vous pouvez ensuite exporter cette fonction via votre *index.js* :

```javascript
// routes/index.js
const noteRoutes = require('./note_routes');

module.exports = function (app, db) {
  noteRoutes(app, db);
  // D'autres groupes de routes pourraient aller ici, à l'avenir
};
```

Puis l'importer pour l'utiliser dans *server.js* :

```javascript
// server.js
const express = require('express');
const MongoClient = require('mongodb').MongoClient;
const bodyParser = require('body-parser');

const app = express();

const port = 8000;

require('./app/routes')(app, {});

app.listen(port, () => {
  console.log('Nous sommes en ligne sur ' + port);
});
```

Notez que puisque vous n'avez pas encore configuré de base de données, vous passez simplement un objet vide.

D'accord, *maintenant* vous pouvez créer votre route CREATE.

La syntaxe est simple :

```javascript
// note_routes.js
module.exports = function (app, db) {
  app.post('/notes', (req, res) => {
    // Vous allez créer votre note ici.
    res.send('Bonjour');
  });
};
```

Lorsque l'application reçoit une requête *post* vers le chemin '/notes', elle exécutera le code à l'intérieur du callback - en passant un objet de requête (qui contient les paramètres ou le JSON de la requête) et un objet de réponse (utilisé pour répondre).

Vous pouvez tester cela en utilisant Postman pour envoyer une requête POST à localhost:8000/notes.

![Image](https://cdn-media-1.freecodecamp.org/images/GZ5bBXdyag5FkmGYwwsj-8x8bC1ee4qYMc1E align="left")

*Vous devriez obtenir le 'Bonjour' en retour.*

Bien ! Vous avez créé votre première vraie route.

L'étape suivante consiste à ajouter des paramètres à votre requête et à les traiter dans votre API et, enfin, à ajouter votre base de données.

### Paramètres de Requête

Dans Postman, allez dans l'onglet Body et ajoutez quelques paires clé-valeur, après avoir sélectionné le bouton radio *x-www-form-urlencoded*.

Cela ajoutera des données de formulaire encodées à votre requête, que vous pourrez traiter avec votre API.

![Image](https://cdn-media-1.freecodecamp.org/images/HRtYe15CJSXkMaL80tD43VS1QSbV6IIaf35C align="left")

*Vous pouvez essayer d'être plus créatif que moi.*

Maintenant, dans votre *note_routes.js*, enregistrons simplement le corps.

```javascript
// note_routes.js
module.exports = function (app, db) {
  app.post('/notes', (req, res) => {
    console.log(req.body);
    res.send('Bonjour');
  });
};
```

Essayez d'envoyer la requête Postman et vous verrez... undefined.

Malheureusement, Express ne peut pas traiter les formulaires URL encodés par lui-même. Mais vous avez installé ce package body-parser...

```javascript
// server.js
const express = require('express');
const MongoClient = require('mongodb').MongoClient;
const bodyParser = require('body-parser');

const app = express();

const port = 8000;

app.use(bodyParser.urlencoded({ extended: true }));

require('./app/routes')(app, {});

app.listen(port, () => {
  console.log('Nous sommes en ligne sur ' + port);
});
```

Maintenant, vous devriez voir le corps comme un objet dans le terminal.

```bash
{ title: 'Mon Titre de Note', body: 'Quelle note géniale.' }
```

Dernière étape de votre route préliminaire : configurer la base de données, puis ajouter vos données.

La manière la plus simple de configurer une base de données Mongo est via [mLab](https://mlab.com/) : c'est gratuit pour la plus petite taille, et assez rapide à configurer.

Une fois que vous avez créé un compte et un déploiement MongoDB, ajoutez un utilisateur à la base de données avec un nom d'utilisateur et un mot de passe :

![Image](https://cdn-media-1.freecodecamp.org/images/5s8PyFy4o8vd6syfkOaH62kni8pg6DhJutul align="left")

puis récupérez l'URL ici (la deuxième) :

![Image](https://cdn-media-1.freecodecamp.org/images/04Rg5oco8HKxKUc0YFMXfrpWM4Xop0sxAKui align="left")

Et dans un répertoire config à la racine de votre projet, créez un fichier db.js.

```bash
mkdir config 
cd config
touch db.js
```

À l'intérieur, ajoutez l'URL :

```javascript
module.exports = {
  url: '...', // Votre URL ici
};
```

N'oubliez pas d'ajouter votre nom d'utilisateur et votre mot de passe (ceux de l'utilisateur de la base de données, pas de votre compte mLab) dans l'URL. (Si vous commitez ce projet sur Github, assurez-vous d'inclure un fichier .gitignore [comme ceci](https://github.com/scottdomes/notable-node-api-tutorial/blob/master/.gitignore), pour ne pas partager votre mot de passe avec tout le monde.)

Maintenant, dans votre *server.js*, vous pouvez utiliser le MongoClient pour vous connecter à votre base de données, et utiliser cela pour envelopper la configuration de votre application :

```javascript
// server.js
const express = require('express');
const MongoClient = require('mongodb').MongoClient;
const bodyParser = require('body-parser');
const db = require('./config/db');

const app = express();

const port = 8000;

app.use(bodyParser.urlencoded({ extended: true }));

MongoClient.connect(db.url, (err, database) => {
  if (err) return console.log(err);
  require('./app/routes')(app, database);
  app.listen(port, () => {
    console.log('Nous sommes en ligne sur ' + port);
  });
});
```

Si vous utilisez la dernière version de MongoDB (3.0+), modifiez-le comme suit :

```javascript
// server.js
const express = require('express');
const MongoClient = require('mongodb').MongoClient;
const bodyParser = require('body-parser');
const db = require('./config/db');

const app = express();

const port = 8000;

app.use(bodyParser.urlencoded({ extended: true }));

MongoClient.connect(db.url, (err, database) => {
  if (err) return console.log(err);

  // Assurez-vous d'ajouter le nom de la base de données et non le nom de la collection
  const database = database.db('note-api');
  require('./app/routes')(app, database);
  app.listen(port, () => {
    console.log('Nous sommes en ligne sur ' + port);
  });
});
```

*(Merci à [Alex Stroulger](https://github.com/astr0-4) pour la correction pour la version 3.0)*

C'est la dernière partie de votre configuration d'infrastructure ! Il ne reste plus que la construction des routes.

### Ajout à votre Base de Données

MongoDB stocke les données dans des *collections* — qui sont exactement comme elles sonnent. Dans votre cas, vous voulez stocker vos notes dans une collection appelée — vous l'avez deviné — notes.

Puisque vous passez votre base de données comme argument *db* dans vos routes, vous pouvez y accéder comme suit :

```javascript
db.collection('notes');
```

Créer une note est aussi simple que d'appeler *insert* sur votre collection :

```javascript
const note = { text: req.body.body, title: req.body.title };

db.collection('notes').insert(note, (err, results) => {});
```

Une fois l'insertion terminée (ou a échoué pour une raison quelconque), vous voulez soit envoyer une erreur, soit envoyer l'objet de note nouvellement créé. Voici le code complet de *note_routes.js* :

```javascript
// note_routes.js
module.exports = function (app, db) {
  const collection = app.post('/notes', (req, res) => {
    const note = { text: req.body.body, title: req.body.title };
    db.collection('notes').insert(note, (err, result) => {
      if (err) {
        res.send({ error: 'Une erreur est survenue' });
      } else {
        res.send(result.ops[0]);
      }
    });
  });
};
```

Essayez-le ! Envoyez une requête POST x-www-form-urlencoded avec Postman, avec un *title* et un *body* définis sous l'onglet Body.

La réponse devrait ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/YLnBtktzcamhwIEDPE90AAywxgQ2Q1hNTDlZ align="left")

Si vous vous connectez à mLab, vous devriez également voir la note créée dans la base de données.

### Votre Route READ

Maintenant, vous pouvez accélérer un peu le rythme.

Disons que vous voulez récupérer la note que vous venez de créer, en naviguant vers localhost:8000/notes/{l'id}. Dans ce cas, ce serait localhost:8000/notes/585182bd42ac5b07a9755ea3.

(Si vous n'avez pas l'ID pour l'une de vos notes, vous pouvez vérifier sur mLab ou simplement en créer une nouvelle).

Voici à quoi cela ressemblerait dans *note_routes.js* :

```javascript
// note_routes.js
module.exports = function (app, db) {
  app.get('/notes/:id', (req, res) => {});
  app.post('/notes', (req, res) => {
    const note = { text: req.body.body, title: req.body.title };
    db.collection('notes').insert(note, (err, result) => {
      if (err) {
        res.send({ error: 'Une erreur est survenue' });
      } else {
        res.send(result.ops[0]);
      }
    });
  });
};
```

Tout comme avant, vous allez appeler une méthode sur votre collection de base de données de notes. Ici, c'est le bien nommé findOne.

```javascript
// note_routes.js
module.exports = function (app, db) {
  app.get('/notes/:id', (req, res) => {
    const details = { _id: '...' }; // ID va ici
    db.collection('notes').findOne(details, (err, item) => {
      if (err) {
        res.send({ error: 'Une erreur est survenue' });
      } else {
        res.send(item);
      }
    });
  });

  app.post('/notes', (req, res) => {
    const note = { text: req.body.body, title: req.body.title };
    db.collection('notes').insert(note, (err, result) => {
      if (err) {
        res.send({ error: 'Une erreur est survenue' });
      } else {
        res.send(result.ops[0]);
      }
    });
  });
};
```

Vous pouvez récupérer l'id à partir des paramètres d'URL via *req.params.id*. Cependant, si vous essayez de simplement placer la chaîne dans les chevrons ci-dessus, cela ne fonctionnera pas.

MongoDB nécessite non seulement un ID sous forme de *chaîne*, mais aussi un ID sous forme d'*objet*, ou, comme ils l'appellent, un ObjectID.

Ne vous inquiétez pas, c'est une correction facile. Voici le code complet :

```javascript
// note_routes.js
var ObjectID = require('mongodb').ObjectID;
module.exports = function (app, db) {
  app.get('/notes/:id', (req, res) => {
    const id = req.params.id;
    const details = { _id: new ObjectID(id) };
    db.collection('notes').findOne(details, (err, item) => {
      if (err) {
        res.send({ error: 'Une erreur est survenue' });
      } else {
        res.send(item);
      }
    });
  });

  app.post('/notes', (req, res) => {
    const note = { text: req.body.body, title: req.body.title };
    db.collection('notes').insert(note, (err, result) => {
      if (err) {
        res.send({ error: 'Une erreur est survenue' });
      } else {
        res.send(result.ops[0]);
      }
    });
  });
};
```

Essayez-le avec l'un de vos identifiants de note, et cela devrait ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/bjUsCmHLB9qpy9uWnWQiOq-hIKNyYpVfTPji align="left")

### Votre Route DELETE

Supprimer un objet est en fait presque la même chose que trouver un objet. Vous utilisez simplement la fonction *remove* au lieu de *findOne*. Voici le code complet. J'ai mis en évidence ce qui est différent de votre GET :

```javascript
// note_routes.js
// ...
app.delete('/notes/:id', (req, res) => {
  const id = req.params.id;
  const details = { _id: new ObjectID(id) };
  db.collection('notes').remove(details, (err, item) => {
    if (err) {
      res.send({ error: 'Une erreur est survenue' });
    } else {
      res.send('Note ' + id + ' supprimée !');
    }
  });
});
// ...
```

### **Votre Route UPDATE**

Dernière étape ! Le PUT est essentiellement un hybride entre READ et CREATE. Vous trouvez l'objet, puis vous le mettez à jour en conséquence. Si vous avez supprimé votre seule note, il est temps d'en créer une autre !

Le code :

```javascript
// note_routes.js
// ...
app.put('/notes/:id', (req, res) => {
  const id = req.params.id;
  const details = { _id: new ObjectID(id) };
  const note = { text: req.body.body, title: req.body.title };
  db.collection('notes').update(details, note, (err, result) => {
    if (err) {
      res.send({ error: 'Une erreur est survenue' });
    } else {
      res.send(note);
    }
  });
});
// ...
```

Maintenant, vous pouvez mettre à jour n'importe laquelle de vos notes, comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/4NC6Hb8T1I0ObXupcIUIYqjSet57RCpuOYg7 align="left")

Notez l'imperfection avec ce code - si vous ne fournissez pas de corps ou de titre, la requête PUT va annuler ces champs sur la note dans la base de données.

Vous pourriez facilement ajouter une logique conditionnelle pour mettre à jour les champs uniquement s'ils sont présents dans la requête - je l'ai laissé de côté juste pour garder cela simple.

### API Complète

C'est tout ! Vous avez une API Node fonctionnelle avec chacune des quatre opérations CRUD majeures.

Le but de ce tutoriel était de vous donner un degré de familiarité avec Express, Node et MongoDB — vous pouvez utiliser votre application simple comme tremplin pour des projets plus complexes.

À l'avenir, j'écrirai des tutoriels pour créer d'autres API simples dans différents langages et frameworks. Appuyez sur le bouton de suivi si vous êtes intéressé !

Si ce tutoriel vous a été d'une quelconque aide, veuillez appuyer sur le cœur vert ci-dessous — cela signifie beaucoup. N'hésitez pas à me laisser également un commentaire avec vos retours ou questions.

Merci d'avoir lu !