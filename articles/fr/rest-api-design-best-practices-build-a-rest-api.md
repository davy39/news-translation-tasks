---
title: Guide des meilleures pratiques de conception d'API REST – Comment construire
  une API REST avec JavaScript, Node.js et Express.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-05-04T15:10:32.000Z'
originalURL: https://freecodecamp.org/news/rest-api-design-best-practices-build-a-rest-api
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/rest-api-design-course-header.png
tags:
- name: best practices
  slug: best-practices
- name: Express JS
  slug: express-js
- name: JavaScript
  slug: javascript
- name: node js
  slug: node-js
- name: REST API
  slug: rest-api
seo_title: Guide des meilleures pratiques de conception d'API REST – Comment construire
  une API REST avec JavaScript, Node.js et Express.js
seo_desc: 'By Jean-Marc Möckel

  I''ve created and consumed many API''s over the past few years. During that time,
  I''ve come across good and bad practices and have experienced nasty situations when
  consuming and building API''s. But there also have been great moment...'
---

Par Jean-Marc M6ckel

J'ai cr99 et consomm9 de nombreuses API au cours des derni8res ann9es. Pendant cette p9riode, j'ai rencontr9 de bonnes et de mauvaises pratiques et j'ai v9cu des situations d9sagr9ables lors de la consommation et de la cr9ation d'API. Mais il y a aussi eu de grands moments.

Il existe des articles utiles en ligne qui pr9sentent de nombreuses bonnes pratiques, mais beaucoup d'entre eux manquent, 0 mon avis, de pragmatisme. Connaetre la th9orie avec quelques exemples est bien, mais je me suis toujours demand9 comment l'impl9mentation se pr9senterait dans un exemple plus r9aliste.

Fournir des exemples simples aide 0 comprendre le concept lui-mame sans trop de complexit9, mais en pratique, les choses ne sont pas toujours si simples. Je suis sbr que vous savez de quoi je parle 0991

C'est pourquoi j'ai d9cid9 d'9crire ce tutoriel. J'ai fusionn9 toutes ces apprentissages (bons et mauvais) en un seul article digestible tout en fournissant un exemple pratique qui peut atre suivi. 0 la fin, nous construirons une API compl8te tout en impl9mentant une bonne pratique apr8s l'autre.

Quelques points 0 retenir avant de commencer :

Les bonnes pratiques sont, comme vous l'avez peut-atre devin9, pas des lois ou des r8gles sp9cifiques 0 suivre. Ce sont des conventions ou des conseils qui ont 9volu9 au fil du temps et se sont av9r9s efficaces. Certaines sont devenues des standards de nos jours. Mais cela ne signifie pas que vous devez les adapter 0 l'identique.

Elles devraient vous donner une direction pour am9liorer vos API en termes d'exp9rience utilisateur (pour le consommateur et le constructeur), de s9curit9 et de performance. 

Gardez simplement 0 l'esprit que les projets sont diff9rents et n9cessitent des approches diff9rentes. Il peut y avoir des situations o9 vous ne pouvez pas ou ne devez pas suivre une certaine convention. Chaque ing9nieur doit donc d9cider cela pour lui-mame ou avec son 9quipe.

Maintenant que nous avons 9clairci ces points, sans plus attendre, mettons-nous au travail !

## Table des mati8res

- [Notre projet d'exemple](#heading-notre-projet-exemple)
    - [Pr9requis](#heading-prerequis)
    - [Architecture](#heading-architecture)
    - [Installation de base](#heading-installation-de-base)
- [Meilleures pratiques pour les API REST](#heading-meilleures-pratiques-api-rest)
    - [Versionnement](#heading-versionnement)
    - [Nommer les ressources au pluriel](#heading-nommer-ressources-pluriel)
    - [Accepter et r9pondre avec des donn9es au format JSON](#heading-accepter-repondre-donnees-json)
    - [R9pondre avec des codes d'erreur HTTP standard](#heading-repondre-codes-erreur-http)
    - [Eviter les verbes dans les noms des endpoints](#heading-eviter-verbes-endpoints)
    - [Grouper les ressources associ9es ensemble](#heading-grouper-ressources-associees)
    - [Int9grer le filtrage, le tri et la pagination](#heading-integrer-filtrage-tri-pagination)
    - [Utiliser la mise en cache des donn9es pour am9liorer les performances](#heading-utiliser-cache-ameliorer-performances)
    - [Bonnes pratiques de s9curit9](#heading-bonnes-pratiques-securite)
    - [Documenter correctement votre API](#heading-documenter-api)
- [Conclusion](#heading-conclusion)

## Notre projet d'exemple

![Image](https://www.freecodecamp.org/news/content/images/2022/04/alvaro-reyes-qWwpHwip31M-unsplash--1-.jpg)
_Photo par [Unsplash](https://unsplash.com/@alvarordesign?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Alvaro Reyes</a> sur <a href="https://unsplash.com/s/photos/project?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText)_

Avant de commencer 0 impl9menter les meilleures pratiques dans notre projet d'exemple, je voudrais vous donner une br8ve introduction de ce que nous allons construire.

Nous allons construire une API REST pour une application d'entraenement CrossFit. Si vous n'ates pas familier avec le CrossFit, c'est une m9thode de fitness et un sport comp9titif qui combine des entraenements de haute intensit9 avec des 9l9ments de plusieurs sports (halt9rophilie olympique, gymnastique, et autres).

Dans notre application, nous aimerions cr9er, lire, mettre 0 jour et supprimer des **WOD** (**W**orkouts **o**f the **D**ay). Cela aidera nos utilisateurs (qui seront des propri9taires de salles de sport) 0 9laborer des plans d'entraenement et 0 maintenir leurs propres entraenements dans une seule application. En plus de cela, ils peuvent 9galement ajouter des conseils d'entraenement importants pour chaque s9ance.

Notre travail consistera 0 concevoir et impl9menter une API pour cette application.

### Pr9requis

Pour suivre ce tutoriel, vous devez avoir une certaine exp9rience en JavaScript, Node.js, Express.js et en architecture backend. Des termes comme REST et API ne devraient pas atre nouveaux pour vous et vous devriez avoir une compr9hension du [mod8le Client-Serveur](https://en.wikipedia.org/wiki/Client%E2%80%93server_model).

Bien sbr que vous n'ayez pas besoin d'atre un expert dans ces domaines, une certaine familiarit9 et id9alement une certaine exp9rience devraient suffire.

Mame si tous les pr9requis ne s'appliquent pas 0 vous, ce n'est bien sbr pas une raison de sauter ce tutoriel. Il y a encore beaucoup 0 apprendre ici pour vous. Mais avoir ces comp9tences rendra les choses plus faciles pour vous.

Mame si cette API est 9crite en JavaScript et Express, les bonnes pratiques ne sont pas limit9es 0 ces outils. Elles peuvent atre appliqu9es 0 d'autres langages de programmation ou frameworks.

### Architecture

Comme discut9 pr9c9demment, nous utiliserons Express.js pour notre API. Je ne veux pas compliquer les choses avec une architecture complexe, donc je souhaite rester avec l'**architecture en 3 couches** :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Bildschirmfoto-2022-04-25-um-14.33.24-1.png)

Dans le **Contr4leur**, nous g9rerons tout ce qui est li9 au HTTP. Cela signifie que nous traitons les requates et les r9ponses pour nos endpoints. Au-dessus de cette couche se trouve 9galement un petit **Routeur** d'Express qui transmet les requates au contr4leur correspondant.

Toute la logique m9tier sera dans la **Couche de Service** qui exporte certains services (m9thodes) utilis9s par le contr4leur.

La troisi8me couche est la **Couche d'Acc8s aux Donn9es** o9 nous travaillerons avec notre base de donn9es. Nous exporterons certaines m9thodes pour des op9rations de base de donn9es sp9cifiques comme la cr9ation d'un WOD qui peuvent atre utilis9es par notre Couche de Service.

Dans notre exemple, nous n'utilisons pas de base de donn9es _r9elle_ comme MongoDB ou PostgreSQL car je souhaite me concentrer davantage sur les bonnes pratiques elles-mames. Par cons9quent, nous utilisons un fichier JSON local qui imite notre base de donn9es. Mais cette logique peut atre transf9r9e 0 d'autres bases de donn9es bien sbr.

### Installation de base

Maintenant, nous devrions atre prats 0 cr9er une installation de base pour notre API. Nous ne compliquerons pas trop les choses et nous construirons une structure de projet simple mais organis9e.

Tout d'abord, cr9ons la structure globale des dossiers avec tous les fichiers et d9pendances n9cessaires. Apr8s cela, nous ferons un test rapide pour v9rifier si tout fonctionne correctement :

```bash
# Cr9er un dossier de projet et naviguer dedans
mkdir crossfit-wod-api && cd crossfit-wod-api
```

```bash
# Cr9er un dossier src et naviguer dedans
mkdir src && cd src
```

```bash
# Cr9er des sous-dossiers
mkdir controllers && mkdir services && mkdir database && mkdir routes
```

```bash
# Cr9er un fichier index (point d'entr9e de notre API)
touch index.js
```

```bash
# Nous sommes actuellement dans le dossier src, donc nous devons remonter d'un niveau
cd .. 

# Cr9er un fichier package.json 
npm init -y
```

Installer les d9pendances pour l'installation de base :

```bash
# D9pendances de d9veloppement 
npm i -D nodemon 

# D9pendances 
npm i express
```

Ouvrez le projet dans votre 9diteur de texte pr9f9r9 et configurez Express :

```javascript
// Dans src/index.js 
const express = require("express"); 

const app = express(); 
const PORT = process.env.PORT || 3000; 

// Pour des fins de test 
app.get("/", (req, res) => { 
    res.send("<h2>Cela fonctionne !</h2>"); 
}); 

app.listen(PORT, () => { 
    console.log(`L'API 9coute sur le port ${PORT}`); 
});
```

Int9grez un nouveau script appel9 **"dev"** dans package.json :

```json
{
  "name": "crossfit-wod-api",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "dev": "nodemon src/index.js"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "nodemon": "^2.0.15"
  },
  "dependencies": {
    "express": "^4.17.3"
  }
}

```

Le script garantit que le serveur de d9veloppement red9marre automatiquement lorsque nous apportons des modifications (gr2ce 0 nodemon).

Lancez le serveur de d9veloppement :

```bash
npm run dev
```

Regardez votre terminal, et vous devriez voir un message indiquant que **"L'API 9coute sur le port 3000"**.

Visitez **localhost:3000** dans votre navigateur. Si tout est configur9 correctement, vous devriez voir ce qui suit :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Bildschirmfoto-2022-04-30-um-11.09.44.png)

G9nial ! Nous sommes maintenant prats 0 impl9menter les meilleures pratiques.

## Meilleures pratiques pour les API REST

![Image](https://www.freecodecamp.org/news/content/images/2022/04/constantin-wenning-idDvA4jPBO8-unsplash--1-.jpg)
_Photo par [Unsplash](https://unsplash.com/@conniwenningsimages?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Constantin Wenning</a> sur <a href="https://unsplash.com/s/photos/handshake?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText)_

Oui ! Maintenant que nous avons une configuration Express vraiment basique, nous pouvons 9tendre notre API avec les meilleures pratiques suivantes.

Commen7ons simplement avec nos endpoints CRUD fondamentaux. Apr8s cela, nous 9tendrons l'API avec chaque bonne pratique.

### Versionnement

Attendez une seconde. Avant d'9crire du code sp9cifique 0 l'API, nous devons atre conscients du versionnement. Comme dans d'autres applications, il y aura des am9liorations, de nouvelles fonctionnalit9s, et des choses comme 7a. Il est donc important de versionner notre API 9galement.

Le grand avantage est que nous pouvons travailler sur de nouvelles fonctionnalit9s ou am9liorations sur une nouvelle version tandis que les clients utilisent toujours la version actuelle et ne sont pas affect9s par les changements cassants.

Nous ne for7ons pas non plus les clients 0 utiliser la nouvelle version tout de suite. Ils peuvent utiliser la version actuelle et migrer par eux-mames lorsque la nouvelle version est stable.

Les versions actuelle et nouvelle fonctionnent essentiellement en parall8le et ne s'affectent pas mutuellement.

Mais comment pouvons-nous diff9rencier les versions ? Une bonne pratique consiste 0 ajouter un segment de chemin comme **v1** ou **v2** dans l'URL.

```javascript
// Version 1 
"/api/v1/workouts" 

// Version 2 
"/api/v2/workouts" 

// ...
```

C'est ce que nous exposons au monde ext9rieur et ce qui peut atre consomm9 par d'autres d9veloppeurs. Mais nous devons 9galement structurer notre projet afin de diff9rencier chaque version.

Il existe de nombreuses approches diff9rentes pour g9rer le versionnement dans une API Express. Dans notre cas, j'aimerais cr9er un sous-dossier pour chaque version dans notre r9pertoire **src** appel9 **v1**.

```bash
mkdir src/v1
```

Maintenant, d9placons notre dossier routes dans ce nouveau r9pertoire v1.

```bash
# Obtenez le chemin de votre r9pertoire actuel (copiez-le) 
pwd 

# D9placez "routes" dans "v1" (ins9rez le chemin ci-dessus dans {pwd}) 
mv {pwd}/src/routes {pwd}/src/v1
```

Le nouveau r9pertoire **/src/v1/routes** stockera toutes nos routes pour la version 1. Nous ajouterons du "vrai" contenu plus tard. Mais pour l'instant, ajoutons un simple fichier **index.js** pour tester les choses.

```bash
# Dans /src/v1/routes 
touch index.js
```

0 l'int9rieur, nous d9marrons un simple routeur.

```javascript
// Dans src/v1/routes/index.js
const express = require("express");
const router = express.Router();

router.route("/").get((req, res) => {
  res.send(`<h2>Bonjour de ${req.baseUrl}</h2>`);
});

module.exports = router;

```

Maintenant, nous devons connecter notre routeur pour v1 dans notre point d'entr9e racine dans src/index.js.

```javascript
// Dans src/index.js
const express = require("express");
// *** AJOUTER ***
const v1Router = require("./v1/routes");

const app = express();
const PORT = process.env.PORT || 3000;

// *** SUPPRIMER ***
app.get("/", (req, res) => {
  res.send("<h2>Cela fonctionne !</h2>");
});

// *** AJOUTER ***
app.use("/api/v1", v1Router);

app.listen(PORT, () => {
  console.log(`L'API 9coute sur le port ${PORT}`);
});

```

Cela s'est bien pass9, n'est-ce pas ? Maintenant, nous capturons toutes les requates qui vont vers **/api/v1/workouts** avec notre v1WorkoutRouter.

0 l'int9rieur de notre routeur, nous appellerons une m9thode diff9rente g9r9e par notre contr4leur pour chaque endpoint diff9rent.

Cr9ons une m9thode pour chaque endpoint. Envoyer un message en retour devrait suffire pour l'instant.

```javascript
// Dans src/controllers/workoutController.js
const getAllWorkouts = (req, res) => {
  res.send("Obtenir tous les entraenements");
};

const getOneWorkout = (req, res) => {
  res.send("Obtenir un entraenement existant");
};

const createNewWorkout = (req, res) => {
  res.send("Cr9er un nouvel entraenement");
};

const updateOneWorkout = (req, res) => {
  res.send("Mettre 0 jour un entraenement existant");
};

const deleteOneWorkout = (req, res) => {
  res.send("Supprimer un entraenement existant");
};

module.exports = {
  getAllWorkouts,
  getOneWorkout,
  createNewWorkout,
  updateOneWorkout,
  deleteOneWorkout,
};

```

Maintenant, il est temps de refactoriser un peu notre routeur d'entraenement et d'utiliser les m9thodes du contr4leur.

```javascript
// Dans src/v1/routes/workoutRoutes.js
const express = require("express");
const workoutController = require("../../controllers/workoutController");

const router = express.Router();

router.get("/", workoutController.getAllWorkouts);

router.get("/:workoutId", workoutController.getOneWorkout);

router.post("/", workoutController.createNewWorkout);

router.patch("/:workoutId", workoutController.updateOneWorkout);

router.delete("/:workoutId", workoutController.deleteOneWorkout);

module.exports = router;

```

Maintenant, nous pouvons tester notre endpoint **GET /api/v1/workouts/:workoutId** en tapant **localhost:3000/api/v1/workouts/2342** dans le navigateur. Vous devriez voir quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Bildschirmfoto-2022-04-30-um-11.29.19.png)

Nous avons r9ussi ! La premi8re couche de notre architecture est termin9e. Cr9ons notre couche de service en impl9mentant la prochaine bonne pratique.

### Accepter et r9pondre avec des donn9es au format JSON

Lorsque vous interagissez avec une API, vous envoyez toujours des donn9es sp9cifiques avec votre requate ou vous recevez des donn9es avec la r9ponse. Il existe de nombreux formats de donn9es diff9rents, mais JSON (JavaScript Object Notation) est un format standardis9.

Bien qu'il y ait le terme **JavaScript** dans JSON, il n'est pas sp9cifiquement li9 0 celui-ci. Vous pouvez 9galement 9crire votre API avec Java ou Python qui peuvent g9rer JSON 9galement.

En raison de sa standardisation, les API devraient accepter et r9pondre avec des donn9es au format JSON.

Examinons notre impl9mentation actuelle et voyons comment nous pouvons int9grer cette bonne pratique.

Tout d'abord, nous cr9ons notre couche de service.

```javascript
// Dans src/services/workoutService.js
const getAllWorkouts = () => {
  return;
};

const getOneWorkout = () => {
  return;
};

const createNewWorkout = () => {
  return;
};

const updateOneWorkout = () => {
  return;
};

const deleteOneWorkout = () => {
  return;
};

module.exports = {
  getAllWorkouts,
  getOneWorkout,
  createNewWorkout,
  updateOneWorkout,
  deleteOneWorkout,
};

```

Il est 9galement bon de nommer les m9thodes de service de la mame mani8re que les m9thodes du contr4leur afin d'avoir une connexion entre celles-ci. Commen7ons par ne rien retourner.

Dans notre contr4leur d'entraenement, nous pouvons utiliser ces m9thodes.

```javascript
// Dans src/controllers/workoutController.js
// *** AJOUTER ***
const workoutService = require("../services/workoutService");

const getAllWorkouts = (req, res) => {
  // *** AJOUTER ***
  const allWorkouts = workoutService.getAllWorkouts();
  res.send("Obtenir tous les entraenements");
};

const getOneWorkout = (req, res) => {
  // *** AJOUTER ***
  const workout = workoutService.getOneWorkout();
  res.send("Obtenir un entraenement existant");
};

const createNewWorkout = (req, res) => {
  // *** AJOUTER ***
  const createdWorkout = workoutService.createNewWorkout();
  res.send("Cr9er un nouvel entraenement");
};

const updateOneWorkout = (req, res) => {
  // *** AJOUTER ***
  const updatedWorkout = workoutService.updateOneWorkout();
  res.send("Mettre 0 jour un entraenement existant");
};

const deleteOneWorkout = (req, res) => {
  // *** AJOUTER ***
  workoutService.deleteOneWorkout();
  res.send("Supprimer un entraenement existant");
};

module.exports = {
  getAllWorkouts,
  getOneWorkout,
  createNewWorkout,
  updateOneWorkout,
  deleteOneWorkout,
};

```

Pour l'instant, rien ne devrait avoir chang9 dans nos r9ponses. Mais sous le capot, notre couche de contr4leur communique maintenant avec notre couche de service.

Dans nos m9thodes de service, nous g9rerons notre logique m9tier comme la transformation des structures de donn9es et la communication avec notre couche de base de donn9es.

Pour cela, nous avons besoin d'une base de donn9es et d'une collection de m9thodes qui g8rent effectivement l'interaction avec la base de donn9es. Notre base de donn9es sera un simple fichier JSON pr9-rempli avec quelques entraenements d9j0.

```bash
# Cr9er un nouveau fichier appel9 db.json dans src/database 
touch src/database/db.json 

# Cr9er un fichier Workout qui stocke toutes les m9thodes sp9cifiques aux entraenements dans /src/database 
touch src/database/Workout.js
```

Copiez ce qui suit dans db.json :

```json
{
  "workouts": [
    {
      "id": "61dbae02-c147-4e28-863c-db7bd402b2d6",
      "name": "Tommy V",
      "mode": "For Time",
      "equipment": [
        "barbell",
        "rope"
      ],
      "exercises": [
        "21 thrusters",
        "12 rope climbs, 15 ft",
        "15 thrusters",
        "9 rope climbs, 15 ft",
        "9 thrusters",
        "6 rope climbs, 15 ft"
      ],
      "createdAt": "4/20/2022, 2:21:56 PM",
      "updatedAt": "4/20/2022, 2:21:56 PM",
      "trainerTips": [
        "Split the 21 thrusters as needed",
        "Try to do the 9 and 6 thrusters unbroken",
        "RX Weights: 115lb/75lb"
      ]
    },
    {
      "id": "4a3d9aaa-608c-49a7-a004-66305ad4ab50",
      "name": "Dead Push-Ups",
      "mode": "AMRAP 10",
      "equipment": [
        "barbell"
      ],
      "exercises": [
        "15 deadlifts",
        "15 hand-release push-ups"
      ],
      "createdAt": "1/25/2022, 1:15:44 PM",
      "updatedAt": "3/10/2022, 8:21:56 AM",
      "trainerTips": [
        "Deadlifts are meant to be light and fast",
        "Try to aim for unbroken sets",
        "RX Weights: 135lb/95lb"
      ]
    },
    {
      "id": "d8be2362-7b68-4ea4-a1f6-03f8bc4eede7",
      "name": "Heavy DT",
      "mode": "5 Rounds For Time",
      "equipment": [
        "barbell",
        "rope"
      ],
      "exercises": [
        "12 deadlifts",
        "9 hang power cleans",
        "6 push jerks"
      ],
      "createdAt": "11/20/2021, 5:39:07 PM",
      "updatedAt": "11/20/2021, 5:39:07 PM",
      "trainerTips": [
        "Aim for unbroken push jerks",
        "The first three rounds might feel terrible, but stick to it",
        "RX Weights: 205lb/145lb"
      ]
    }
  ]
}
```

Comme vous pouvez le voir, trois entraenements sont ins9r9s. Un entraenement se compose d'un id, d'un nom, d'un mode, d'9quipements, d'exercices, de createdAt, de updatedAt et de trainerTips.

Commen7ons par le plus simple et retournons tous les entraenements stock9s et commen7ons par impl9menter la m9thode correspondante dans notre couche d'acc8s aux donn9es (src/database/Workout.js).

Encore une fois, j'ai choisi de nommer la m9thode ici de la mame mani8re que celle du service et du contr4leur. Mais cela est totalement facultatif.

```javascript
// Dans src/database/Workout.js
const DB = require("./db.json");

const getAllWorkouts = () => {
  return DB.workouts;
};

module.exports = { getAllWorkouts };

```

Sautez directement dans notre service d'entraenement et impl9mentez la logique pour **getAllWorkouts.**

```javascript
// Dans src/database/workoutService.js
// *** AJOUTER ***
const Workout = require("../database/Workout");
const getAllWorkouts = () => {
  // *** AJOUTER ***
  const allWorkouts = Workout.getAllWorkouts();
  // *** AJOUTER ***
  return allWorkouts;
};

const getOneWorkout = () => {
  return;
};

const createNewWorkout = () => {
  return;
};

const updateOneWorkout = () => {
  return;
};

const deleteOneWorkout = () => {
  return;
};

module.exports = {
  getAllWorkouts,
  getOneWorkout,
  createNewWorkout,
  updateOneWorkout,
  deleteOneWorkout,
};

```

Retourner tous les entraenements est assez simple et nous n'avons pas besoin de faire de transformations car c'est d9j0 un fichier JSON. Nous n'avons pas non plus besoin de prendre d'arguments pour l'instant. Donc cette impl9mentation est assez simple. Mais nous reviendrons sur cela plus tard.

Dans notre contr4leur d'entraenement, nous recevons la valeur de retour de `workoutService.getAllWorkouts()` et l'envoyons simplement comme r9ponse au client. Nous avons fait passer la r9ponse de la base de donn9es par notre service vers le contr4leur.

```javascript
// Dans src/controllers/workoutControllers.js
const workoutService = require("../services/workoutService");

const getAllWorkouts = (req, res) => {
  const allWorkouts = workoutService.getAllWorkouts();
  // *** AJOUTER ***
  res.send({ status: "OK", data: allWorkouts });
};

const getOneWorkout = (req, res) => {
  const workout = workoutService.getOneWorkout();
  res.send("Obtenir un entraenement existant");
};

const createNewWorkout = (req, res) => {
  const createdWorkout = workoutService.createNewWorkout();
  res.send("Cr9er un nouvel entraenement");
};

const updateOneWorkout = (req, res) => {
  const updatedWorkout = workoutService.updateOneWorkout();
  res.send("Mettre 0 jour un entraenement existant");
};

const deleteOneWorkout = (req, res) => {
  workoutService.deleteOneWorkout();
  res.send("Supprimer un entraenement existant");
};

module.exports = {
  getAllWorkouts,
  getOneWorkout,
  createNewWorkout,
  updateOneWorkout,
  deleteOneWorkout,
};

```

Allez sur **localhost:3000/api/v1/workouts** dans votre navigateur et vous devriez voir la r9ponse JSON.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Bildschirmfoto-2022-04-30-um-11.38.14.png)

Cela s'est bien pass9 ! Nous envoyons des donn9es au format JSON. Mais qu'en est-il de leur acceptation ? Pensons 0 un endpoint o9 nous devons recevoir des donn9es JSON du client. L'endpoint pour cr9er ou mettre 0 jour un entraenement a besoin de donn9es du client.

Dans notre contr4leur d'entraenement, nous extrayons le corps de la requate pour cr9er un nouvel entraenement et nous le transmettons au service d'entraenement. Dans le service d'entraenement, nous l'ins9rerons dans notre DB.json et enverrons le nouvel entraenement cr99 au client.

Pour pouvoir analyser le JSON envoy9 dans le corps de la requate, nous devons d'abord installer **body-parser** et le configurer.

```bash
npm i body-parser
```

```javascript
// Dans src/index.js 
const express = require("express");
// *** AJOUTER ***
const bodyParser = require("body-parser");
const v1WorkoutRouter = require("./v1/routes/workoutRoutes");

const app = express();
const PORT = process.env.PORT || 3000;

// *** AJOUTER ***
app.use(bodyParser.json());
app.use("/api/v1/workouts", v1WorkoutRouter);

app.listen(PORT, () => {
  console.log(`L'API 9coute sur le port ${PORT}`);
});

```

Maintenant, nous sommes en mesure de recevoir les donn9es JSON dans nos contr4leurs sous **req.body.**

Pour le tester correctement, ouvrez simplement votre client HTTP pr9f9r9 (j'utilise Postman), cr9ez une requate POST vers localhost:3000/api/v1/workouts et un corps de requate au format JSON comme ceci :

```javascript
{
  "name": "Core Buster",
  "mode": "AMRAP 20",
  "equipment": [
    "rack",
    "barbell",
    "abmat"
  ],
  "exercises": [
    "15 toes to bars",
    "10 thrusters",
    "30 abmat sit-ups"
  ],
  "trainerTips": [
    "Split your toes to bars into two sets maximum",
    "Go unbroken on the thrusters",
    "Take the abmat sit-ups as a chance to normalize your breath"
  ]
}
```

Comme vous l'avez peut-atre remarqu9, certaines propri9t9s sont manquantes comme "id", "createdAt" et "updatedAt". C'est le travail de notre API d'ajouter ces propri9t9s avant de les ins9rer. Nous nous en occuperons dans notre service d'entraenement plus tard.

Dans la m9thode **createNewWorkout** de notre contr4leur d'entraenement, nous pouvons extraire le corps de l'objet de requate, faire une validation et le transmettre comme argument 0 notre service d'entraenement.

```javascript
// Dans src/controllers/workoutController.js
...

const createNewWorkout = (req, res) => {
  const { body } = req;
  // *** AJOUTER ***
  if (
    !body.name ||
    !body.mode ||
    !body.equipment ||
    !body.exercises ||
    !body.trainerTips
  ) {
    return;
  }
  // *** AJOUTER ***
  const newWorkout = {
    name: body.name,
    mode: body.mode,
    equipment: body.equipment,
    exercises: body.exercises,
    trainerTips: body.trainerTips,
  };
  // *** AJOUTER ***
  const createdWorkout = workoutService.createNewWorkout(newWorkout);
  // *** AJOUTER ***
  res.status(201).send({ status: "OK", data: createdWorkout });
};

...
```

Pour am9liorer la validation des requates, vous devriez normalement utiliser un package tiers comme [express-validator](https://express-validator.github.io/docs/).

Allons dans notre service d'entraenement et recevons les donn9es dans notre m9thode createNewWorkout.

Apr8s cela, nous ajoutons les propri9t9s manquantes 0 l'objet et les transmettons 0 une nouvelle m9thode dans notre couche d'acc8s aux donn9es pour les stocker dans notre DB.

Tout d'abord, nous cr9ons une simple fonction utilitaire pour 9craser notre fichier JSON afin de persister les donn9es.

```bash
# Cr9er un fichier utils dans notre r9pertoire de base de donn9es 
touch src/database/utils.js
```

```javascript
// Dans src/database/utils.js
const fs = require("fs");

const saveToDatabase = (DB) => {
  fs.writeFileSync("./src/database/db.json", JSON.stringify(DB, null, 2), {
    encoding: "utf-8",
  });
};

module.exports = { saveToDatabase };

```

Ensuite, nous pouvons utiliser cette fonction dans notre fichier Workout.js.

```javascript
// Dans src/database/Workout.js
const DB = require("./db.json");
// *** AJOUTER ***
const { saveToDatabase } = require("./utils");


const getAllWorkouts = () => {
  return DB.workouts;
};

// *** AJOUTER ***
const createNewWorkout = (newWorkout) => {
  const isAlreadyAdded =
    DB.workouts.findIndex((workout) => workout.name === newWorkout.name) > -1;
  if (isAlreadyAdded) {
    return;
  }
  DB.workouts.push(newWorkout);
  saveToDatabase(DB);
  return newWorkout;
};

module.exports = {
  getAllWorkouts,
  // *** AJOUTER ***
  createNewWorkout,
};

```

Cela s'est bien pass9 ! L'9tape suivante est d'utiliser les m9thodes de la base de donn9es dans notre service d'entraenement.

```bash
# Installer le package uuid 
npm i uuid
```

```javascript
// Dans src/services/workoutService.js
// *** AJOUTER ***
const { v4: uuid } = require("uuid");
// *** AJOUTER ***
const Workout = require("../database/Workout");

const getAllWorkouts = () => {
    const allWorkouts = Workout.getAllWorkouts();
    return allWorkouts;
};

const getOneWorkout = () => {
  return;
};

const createNewWorkout = (newWorkout) => {
  // *** AJOUTER ***
  const workoutToInsert = {
    ...newWorkout,
    id: uuid(),
    createdAt: new Date().toLocaleString("en-US", { timeZone: "UTC" }),
    updatedAt: new Date().toLocaleString("en-US", { timeZone: "UTC" }),
  };
  // *** AJOUTER ***
  const createdWorkout = Workout.createNewWorkout(workoutToInsert);
  return createdWorkout;
};

const updateOneWorkout = () => {
  return;
};

const deleteOneWorkout = () => {
  return;
};

module.exports = {
  getAllWorkouts,
  getOneWorkout,
  createNewWorkout,
  updateOneWorkout,
  deleteOneWorkout,
};

```

Waouh ! C'9tait amusant, n'est-ce pas ? Maintenant, vous pouvez aller dans votre client HTTP, envoyer la requate POST 0 nouveau, et vous devriez recevoir le nouvel entraenement cr99 en JSON.

Si vous essayez d'ajouter le mame entraenement une deuxi8me fois, vous recevez toujours un code de statut 201, mais sans le nouvel entraenement ins9r9. 

Cela signifie que notre m9thode de base de donn9es annule l'insertion pour l'instant et ne retourne simplement rien. C'est parce que notre instruction if pour v9rifier s'il y a d9j0 un entraenement ins9r9 avec le mame nom entre en jeu. C'est bien pour l'instant, nous g9rerons ce cas dans la prochaine bonne pratique !

Maintenant, envoyez une requate GET 0 **localhost:3000/api/v1/workouts** pour lire tous les entraenements. Je choisis le navigateur pour cela. Vous devriez voir que notre entraenement a 9t9 ins9r9 et persist9 avec succ8s :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Bildschirmfoto-2022-04-30-um-11.57.23.png)

Vous pouvez impl9menter les autres m9thodes par vous-mame ou simplement copier mes impl9mentations.

Tout d'abord, le contr4leur d'entraenement (vous pouvez simplement copier tout le contenu) :

```javascript
// Dans src/controllers/workoutController.js
const workoutService = require("../services/workoutService");

const getAllWorkouts = (req, res) => {
  const allWorkouts = workoutService.getAllWorkouts();
  res.send({ status: "OK", data: allWorkouts });
};

const getOneWorkout = (req, res) => {
  const {
    params: { workoutId },
  } = req;
  if (!workoutId) {
    return;
  }
  const workout = workoutService.getOneWorkout(workoutId);
  res.send({ status: "OK", data: workout });
};

const createNewWorkout = (req, res) => {
  const { body } = req;
  if (
    !body.name ||
    !body.mode ||
    !body.equipment ||
    !body.exercises ||
    !body.trainerTips
  ) {
    return;
  }
  const newWorkout = {
    name: body.name,
    mode: body.mode,
    equipment: body.equipment,
    exercises: body.exercises,
    trainerTips: body.trainerTips,
  };
  const createdWorkout = workoutService.createNewWorkout(newWorkout);
  res.status(201).send({ status: "OK", data: createdWorkout });
};

const updateOneWorkout = (req, res) => {
  const {
    body,
    params: { workoutId },
  } = req;
  if (!workoutId) {
    return;
  }
  const updatedWorkout = workoutService.updateOneWorkout(workoutId, body);
  res.send({ status: "OK", data: updatedWorkout });
};

const deleteOneWorkout = (req, res) => {
  const {
    params: { workoutId },
  } = req;
  if (!workoutId) {
    return;
  }
  workoutService.deleteOneWorkout(workoutId);
  res.status(204).send({ status: "OK" });
};

module.exports = {
  getAllWorkouts,
  getOneWorkout,
  createNewWorkout,
  updateOneWorkout,
  deleteOneWorkout,
};

```

Ensuite, le service d'entraenement (vous pouvez simplement copier tout le contenu) :

```javascript
// Dans src/services/workoutServices.js
const { v4: uuid } = require("uuid");
const Workout = require("../database/Workout");

const getAllWorkouts = () => {
  const allWorkouts = Workout.getAllWorkouts();
  return allWorkouts;
};

const getOneWorkout = (workoutId) => {
  const workout = Workout.getOneWorkout(workoutId);
  return workout;
};

const createNewWorkout = (newWorkout) => {
  const workoutToInsert = {
    ...newWorkout,
    id: uuid(),
    createdAt: new Date().toLocaleString("en-US", { timeZone: "UTC" }),
    updatedAt: new Date().toLocaleString("en-US", { timeZone: "UTC" }),
  };
  const createdWorkout = Workout.createNewWorkout(workoutToInsert);
  return createdWorkout;
};

const updateOneWorkout = (workoutId, changes) => {
  const updatedWorkout = Workout.updateOneWorkout(workoutId, changes);
  return updatedWorkout;
};

const deleteOneWorkout = (workoutId) => {
  Workout.deleteOneWorkout(workoutId);
};

module.exports = {
  getAllWorkouts,
  getOneWorkout,
  createNewWorkout,
  updateOneWorkout,
  deleteOneWorkout,
};

```

Et enfin, nos m9thodes de base de donn9es dans la couche d'acc8s aux donn9es (vous pouvez simplement copier tout le contenu) :

```javascript
// Dans src/database/Workout.js
const DB = require("./db.json");
const { saveToDatabase } = require("./utils");

const getAllWorkouts = () => {
  return DB.workouts;
};

const getOneWorkout = (workoutId) => {
  const workout = DB.workouts.find((workout) => workout.id === workoutId);
  if (!workout) {
    return;
  }
  return workout;
};

const createNewWorkout = (newWorkout) => {
  const isAlreadyAdded =
    DB.workouts.findIndex((workout) => workout.name === newWorkout.name) > -1;
  if (isAlreadyAdded) {
    return;
  }
  DB.workouts.push(newWorkout);
  saveToDatabase(DB);
  return newWorkout;
};

const updateOneWorkout = (workoutId, changes) => {
  const indexForUpdate = DB.workouts.findIndex(
    (workout) => workout.id === workoutId
  );
  if (indexForUpdate === -1) {
    return;
  }
  const updatedWorkout = {
    ...DB.workouts[indexForUpdate],
    ...changes,
    updatedAt: new Date().toLocaleString("en-US", { timeZone: "UTC" }),
  };
  DB.workouts[indexForUpdate] = updatedWorkout;
  saveToDatabase(DB);
  return updatedWorkout;
};

const deleteOneWorkout = (workoutId) => {
  const indexForDeletion = DB.workouts.findIndex(
    (workout) => workout.id === workoutId
  );
  if (indexForDeletion === -1) {
    return;
  }
  DB.workouts.splice(indexForDeletion, 1);
  saveToDatabase(DB);
};

module.exports = {
  getAllWorkouts,
  createNewWorkout,
  getOneWorkout,
  updateOneWorkout,
  deleteOneWorkout,
};

```

G9nial ! Passons 0 la prochaine bonne pratique et voyons comment nous pouvons g9rer les erreurs correctement.

### R9pondre avec des codes d'erreur HTTP standard

Nous avons d9j0 parcouru un long chemin, mais nous n'avons pas encore fini. Notre API a maintenant la capacit9 de g9rer les op9rations CRUD de base avec le stockage des donn9es. C'est g9nial, mais pas vraiment id9al.

Pourquoi ? Laissez-moi expliquer.

Dans un monde parfait, tout fonctionne sans heurts sans aucune erreur. Mais comme vous le savez peut-atre, dans le monde r9el, de nombreuses erreurs peuvent se produire, que ce soit d'un point de vue humain ou technique.

Vous connaissez probablement ce sentiment 9trange lorsque les choses fonctionnent correctement d8s le d9part sans aucune erreur. C'est g9nial et agr9able, mais en tant que d9veloppeurs, nous sommes plus habitu9s aux choses qui ne fonctionnent pas correctement. 0991

Il en va de mame pour notre API. Nous devons g9rer certains cas qui peuvent mal se passer ou g9n9rer une erreur. Cela renforcera 9galement notre API.

Lorsque quelque chose ne va pas (soit de la requate, soit 0 l'int9rieur de notre API), nous envoyons des codes d'erreur HTTP. J'ai vu et utilis9 des API qui renvoyaient tout le temps un code d'erreur 400 lorsqu'une requate 9tait bogu9e, sans aucun message sp9cifique sur POURQUOI cette erreur s'est produite ou quelle 9tait l'erreur. Le d9bogage est alors devenu un cauchemar.

C'est la raison pour laquelle il est toujours bon de renvoyer des codes d'erreur HTTP appropri9s pour diff9rents cas. Cela aide le consommateur ou l'ing9nieur qui a construit l'API 0 identifier le probl8me plus facilement.

Pour am9liorer l'exp9rience, nous pouvons 9galement envoyer un message d'erreur rapide avec la r9ponse d'erreur. Mais comme je l'ai 9crit dans l'introduction, cela n'est pas toujours tr8s judicieux et doit atre consid9r9 par l'ing9nieur lui-mame.

Par exemple, renvoyer quelque chose comme **"Le nom d'utilisateur est d9j0 inscrit"** doit atre bien r9fl9chi car vous fournissez des informations sur vos utilisateurs que vous devriez vraiment cacher.

Dans notre API Crossfit, nous allons examiner l'endpoint de cr9ation et voir quelles erreurs peuvent survenir et comment nous pouvons les g9rer. 0 la fin de ce conseil, vous trouverez 9galement l'impl9mentation compl8te des autres endpoints.

Commen7ons par examiner notre m9thode createNewWorkout dans notre contr4leur d'entraenement :

```javascript
// Dans src/controllers/workoutController.js
...

const createNewWorkout = (req, res) => {
  const { body } = req;
  if (
    !body.name ||
    !body.mode ||
    !body.equipment ||
    !body.exercises ||
    !body.trainerTips
  ) {
    return;
  }
  const newWorkout = {
    name: body.name,
    mode: body.mode,
    equipment: body.equipment,
    exercises: body.exercises,
    trainerTips: body.trainerTips,
  };
  const createdWorkout = workoutService.createNewWorkout(newWorkout);
  res.status(201).send({ status: "OK", data: createdWorkout });
};

...
```

Nous avons d9j0 intercept9 le cas o9 le corps de la requate n'est pas correctement construit et manque de cl9s que nous attendons.

Ce serait un bon exemple pour envoyer une erreur HTTP 400 avec un message d'erreur correspondant.

```javascript
// Dans src/controllers/workoutController.js
...

const createNewWorkout = (req, res) => {
  const { body } = req;
  if (
    !body.name ||
    !body.mode ||
    !body.equipment ||
    !body.exercises ||
    !body.trainerTips
  ) {
    res
      .status(400)
      .send({
        status: "FAILED",
        data: {
          error:
            "One of the following keys is missing or is empty in request body: 'name', 'mode', 'equipment', 'exercises', 'trainerTips'",
        },
      });
    return;
  }
  const newWorkout = {
    name: body.name,
    mode: body.mode,
    equipment: body.equipment,
    exercises: body.exercises,
    trainerTips: body.trainerTips,
  };
  const createdWorkout = workoutService.createNewWorkout(newWorkout);
  res.status(201).send({ status: "OK", data: createdWorkout });
};

...
```

Si nous essayons d'ajouter un nouvel entraenement mais oublions de fournir la propri9t9 "mode" dans le corps de notre requate, nous devrions voir le message d'erreur accompagn9 du code d'erreur HTTP 400.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Bildschirmfoto-2022-04-30-um-15.17.21.png)

Un d9veloppeur qui consomme l'API est maintenant mieux inform9 sur ce qu'il doit rechercher. Il sait imm9diatement qu'il doit aller dans le corps de la requate et v9rifier s'il a oubli9 de fournir l'une des propri9t9s requises.

Laisser ce message d'erreur plus g9n9rique pour toutes les propri9t9s sera acceptable pour l'instant. Typiquement, vous utiliseriez un validateur de sch9ma pour g9rer cela.

Allons un niveau plus profond dans notre service d'entraenement et voyons quelles erreurs potentielles peuvent survenir.

```javascript
// Dans src/services/workoutService.js
...

const createNewWorkout = (newWorkout) => {
  const workoutToInsert = {
    ...newWorkout,
    id: uuid(),
    createdAt: new Date().toLocaleString("en-US", { timeZone: "UTC" }),
    updatedAt: new Date().toLocaleString("en-US", { timeZone: "UTC" }),
  };
  const createdWorkout = Workout.createNewWorkout(workoutToInsert);
  return createdWorkout;
};

...
```

Une chose qui peut mal se passer est l'insertion dans la base de donn9es **Workout.createNewWorkout()**. J'aime envelopper cela dans un bloc try/catch pour attraper l'erreur lorsqu'elle se produit.

```javascript
// Dans src/services/workoutService.js
...

const createNewWorkout = (newWorkout) => {
  const workoutToInsert = {
    ...newWorkout,
    id: uuid(),
    createdAt: new Date().toLocaleString("en-US", { timeZone: "UTC" }),
    updatedAt: new Date().toLocaleString("en-US", { timeZone: "UTC" }),
  };
  try {
    const createdWorkout = Workout.createNewWorkout(workoutToInsert);
    return createdWorkout;
  } catch (error) {
    throw error;
  }
};

...
```

Toute erreur qui est lev9e dans notre m9thode Workout.createNewWorkout() sera captur9e dans notre bloc catch. Nous la relan7ons simplement, afin de pouvoir ajuster nos r9ponses plus tard dans notre contr4leur.

D9finissons nos erreurs dans Workout.js :

```javascript
// Dans src/database/Workout.js
...

const createNewWorkout = (newWorkout) => {
  const isAlreadyAdded =
    DB.workouts.findIndex((workout) => workout.name === newWorkout.name) > -1;
  if (isAlreadyAdded) {
    throw {
      status: 400,
      message: `Workout with the name '${newWorkout.name}' already exists`,
    };
  }
  try {
    DB.workouts.push(newWorkout);
    saveToDatabase(DB);
    return newWorkout;
  } catch (error) {
    throw { status: 500, message: error?.message || error };
  }
};

...
```

Comme vous pouvez le voir, une erreur se compose de deux choses, un statut et un message. J'utilise simplement le mot-cl9 **throw** ici pour envoyer une structure de donn9es diff9rente d'une chaene, ce qui est requis dans **throw new Error()**. 

Un petit inconv9nient de simplement lancer est que nous n'obtenons pas de trace de pile. Mais normalement, ce lancement d'erreur serait g9r9 par une biblioth8que tierce de notre choix (par exemple Mongoose si vous utilisez une base de donn9es MongoDB). Mais pour les besoins de ce tutoriel, cela devrait suffire.

Maintenant, nous sommes en mesure de lancer et de capturer des erreurs dans le service et la couche d'acc8s aux donn9es. Nous pouvons passer dans notre contr4leur d'entraenement maintenant, capturer les erreurs l0-bas 9galement, et r9pondre en cons9quence.

```javascript
// Dans src/controllers/workoutController.js
...

const createNewWorkout = (req, res) => {
  const { body } = req;
  if (
    !body.name ||
    !body.mode ||
    !body.equipment ||
    !body.exercises ||
    !body.trainerTips
  ) {
    res
      .status(400)
      .send({
        status: "FAILED",
        data: {
          error:
            "One of the following keys is missing or is empty in request body: 'name', 'mode', 'equipment', 'exercises', 'trainerTips'",
        },
      });
    return;
  }
  const newWorkout = {
    name: body.name,
    mode: body.mode,
    equipment: body.equipment,
    exercises: body.exercises,
    trainerTips: body.trainerTips,
  };
  // *** AJOUTER ***
  try {
    const createdWorkout = workoutService.createNewWorkout(newWorkout);
    res.status(201).send({ status: "OK", data: createdWorkout });
  } catch (error) {
    res
      .status(error?.status || 500)
      .send({ status: "FAILED", data: { error: error?.message || error } });
  }
};

...
```

Vous pouvez tester les choses en ajoutant un entraenement avec le mame nom deux fois ou en ne fournissant pas une propri9t9 requise dans le corps de votre requate. Vous devriez recevoir les codes d'erreur HTTP correspondants avec le message d'erreur.

Pour conclure et passer au conseil suivant, vous pouvez copier les autres m9thodes impl9ment9es dans les fichiers suivants ou vous pouvez essayer par vous-mame :

```javascript
// Dans src/controllers/workoutController.js
const workoutService = require("../services/workoutService");

const getAllWorkouts = (req, res) => {
  try {
    const allWorkouts = workoutService.getAllWorkouts();
    res.send({ status: "OK", data: allWorkouts });
  } catch (error) {
    res
      .status(error?.status || 500)
      .send({ status: "FAILED", data: { error: error?.message || error } });
  }
};

const getOneWorkout = (req, res) => {
  const {
    params: { workoutId },
  } = req;
  if (!workoutId) {
    res
      .status(400)
      .send({
        status: "FAILED",
        data: { error: "Parameter ':workoutId' can not be empty" },
      });
  }
  try {
    const workout = workoutService.getOneWorkout(workoutId);
    res.send({ status: "OK", data: workout });
  } catch (error) {
    res
      .status(error?.status || 500)
      .send({ status: "FAILED", data: { error: error?.message || error } });
  }
};

const createNewWorkout = (req, res) => {
  const { body } = req;
  if (
    !body.name ||
    !body.mode ||
    !body.equipment ||
    !body.exercises ||
    !body.trainerTips
  ) {
    res
      .status(400)
      .send({
        status: "FAILED",
        data: {
          error:
            "One of the following keys is missing or is empty in request body: 'name', 'mode', 'equipment', 'exercises', 'trainerTips'",
        },
      });
    return;
  }
  const newWorkout = {
    name: body.name,
    mode: body.mode,
    equipment: body.equipment,
    exercises: body.exercises,
    trainerTips: body.trainerTips,
  };
  try {
    const createdWorkout = workoutService.createNewWorkout(newWorkout);
    res.status(201).send({ status: "OK", data: createdWorkout });
  } catch (error) {
    res
      .status(error?.status || 500)
      .send({ status: "FAILED", data: { error: error?.message || error } });
  }
};

const updateOneWorkout = (req, res) => {
  const {
    body,
    params: { workoutId },
  } = req;
  if (!workoutId) {
    res
      .status(400)
      .send({
        status: "FAILED",
        data: { error: "Parameter ':workoutId' can not be empty" },
      });
  }
  try {
    const updatedWorkout = workoutService.updateOneWorkout(workoutId, body);
    res.send({ status: "OK", data: updatedWorkout });
  } catch (error) {
    res
      .status(error?.status || 500)
      .send({ status: "FAILED", data: { error: error?.message || error } });
  }
};

const deleteOneWorkout = (req, res) => {
  const {
    params: { workoutId },
  } = req;
  if (!workoutId) {
    res
      .status(400)
      .send({
        status: "FAILED",
        data: { error: "Parameter ':workoutId' can not be empty" },
      });
  }
  try {
    workoutService.deleteOneWorkout(workoutId);
    res.status(204).send({ status: "OK" });
  } catch (error) {
    res
      .status(error?.status || 500)
      .send({ status: "FAILED", data: { error: error?.message || error } });
  }
};

module.exports = {
  getAllWorkouts,
  getOneWorkout,
  createNewWorkout,
  updateOneWorkout,
  deleteOneWorkout,
  getRecordsForWorkout,
};

```

```javascript
// Dans src/services/workoutService.js
const { v4: uuid } = require("uuid");
const Workout = require("../database/Workout");

const getAllWorkouts = () => {
  try {
    const allWorkouts = Workout.getAllWorkouts();
    return allWorkouts;
  } catch (error) {
    throw error;
  }
};

const getOneWorkout = (workoutId) => {
  try {
    const workout = Workout.getOneWorkout(workoutId);
    return workout;
  } catch (error) {
    throw error;
  }
};

const createNewWorkout = (newWorkout) => {
  const workoutToInsert = {
    ...newWorkout,
    id: uuid(),
    createdAt: new Date().toLocaleString("en-US", { timeZone: "UTC" }),
    updatedAt: new Date().toLocaleString("en-US", { timeZone: "UTC" }),
  };
  try {
    const createdWorkout = Workout.createNewWorkout(workoutToInsert);
    return createdWorkout;
  } catch (error) {
    throw error;
  }
};

const updateOneWorkout = (workoutId, changes) => {
  try {
    const updatedWorkout = Workout.updateOneWorkout(workoutId, changes);
    return updatedWorkout;
  } catch (error) {
    throw error;
  }
};

const deleteOneWorkout = (workoutId) => {
  try {
    Workout.deleteOneWorkout(workoutId);
  } catch (error) {
    throw error;
  }
};

module.exports = {
  getAllWorkouts,
  getOneWorkout,
  createNewWorkout,
  updateOneWorkout,
  deleteOneWorkout,
};

```

```javascript
// Dans src/database/Workout.js
const DB = require("./db.json");
const { saveToDatabase } = require("./utils");

const getAllWorkouts = () => {
  try {
    return DB.workouts;
  } catch (error) {
    throw { status: 500, message: error };
  }
};

const getOneWorkout = (workoutId) => {
  try {
    const workout = DB.workouts.find((workout) => workout.id === workoutId);
    if (!workout) {
      throw {
        status: 400,
        message: `Can't find workout with the id '${workoutId}'`,
      };
    }
    return workout;
  } catch (error) {
    throw { status: error?.status || 500, message: error?.message || error };
  }
};

const createNewWorkout = (newWorkout) => {
  try {
    const isAlreadyAdded =
      DB.workouts.findIndex((workout) => workout.name === newWorkout.name) > -1;
    if (isAlreadyAdded) {
      throw {
        status: 400,
        message: `Workout with the name '${newWorkout.name}' already exists`,
      };
    }
    DB.workouts.push(newWorkout);
    saveToDatabase(DB);
    return newWorkout;
  } catch (error) {
    throw { status: error?.status || 500, message: error?.message || error };
  }
};

const updateOneWorkout = (workoutId, changes) => {
  try {
    const isAlreadyAdded =
      DB.workouts.findIndex((workout) => workout.name === changes.name) > -1;
    if (isAlreadyAdded) {
      throw {
        status: 400,
        message: `Workout with the name '${changes.name}' already exists`,
      };
    }
    const indexForUpdate = DB.workouts.findIndex(
      (workout) => workout.id === workoutId
    );
    if (indexForUpdate === -1) {
      throw {
        status: 400,
        message: `Can't find workout with the id '${workoutId}'`,
      };
    }
    const updatedWorkout = {
      ...DB.workouts[indexForUpdate],
      ...changes,
      updatedAt: new Date().toLocaleString("en-US", { timeZone: "UTC" }),
    };
    DB.workouts[indexForUpdate] = updatedWorkout;
    saveToDatabase(DB);
    return updatedWorkout;
  } catch (error) {
    throw { status: error?.status || 500, message: error?.message || error };
  }
};

const deleteOneWorkout = (workoutId) => {
  try {
    const indexForDeletion = DB.workouts.findIndex(
      (workout) => workout.id === workoutId
    );
    if (indexForDeletion === -1) {
      throw {
        status: 400,
        message: `Can't find workout with the id '${workoutId}'`,
      };
    }
    DB.workouts.splice(indexForDeletion, 1);
    saveToDatabase(DB);
  } catch (error) {
    throw { status: error?.status || 500, message: error?.message || error };
  }
};

module.exports = {
  getAllWorkouts,
  createNewWorkout,
  getOneWorkout,
  updateOneWorkout,
  deleteOneWorkout,
};

```

### 9viter les verbes dans les noms des endpoints

Il n'est pas tr8s logique d'utiliser des verbes dans vos endpoints et c'est en fait assez inutile. G9n9ralement, chaque URL devrait pointer vers une ressource (rappelons l'exemple de la boete pr9c9demment mentionn9e). Rien de plus, rien de moins.

Utiliser un verbe dans une URL montre un certain comportement qu'une ressource elle-mame ne peut pas avoir.

Nous avons d9j0 impl9ment9 les endpoints correctement sans utiliser de verbes dans l'URL, mais examinons comment nos URL auraient l'air si nous avions utilis9 des verbes.

```javascript
// Impl9mentations actuelles (sans verbes)
GET "/api/v1/workouts" 
GET "/api/v1/workouts/:workoutId" 
POST "/api/v1/workouts" 
PATCH "/api/v1/workouts/:workoutId" 
DELETE "/api/v1/workouts/:workoutId"  

// Impl9mentation utilisant des verbes 
GET "/api/v1/getAllWorkouts" 
GET "/api/v1/getWorkoutById/:workoutId" 
CREATE "/api/v1/createWorkout" 
PATCH "/api/v1/updateWorkout/:workoutId" 
DELETE "/api/v1/deleteWorkout/:workoutId"
```

Voyez-vous la diff9rence ? Avoir une URL compl8tement diff9rente pour chaque comportement peut devenir confus et inutilement complexe tr8s rapidement.

Imaginez que nous avons 300 endpoints diff9rents. Utiliser une URL s9par9e pour chacun pourrait atre un cauchemar (et de documentation).

Une autre raison que je voudrais souligner pour ne pas utiliser de verbes dans votre URL est que le verbe HTTP lui-mame indique d9j0 l'action.

Des choses comme **"GET /api/v1/getAllWorkouts"** ou **"DELETE api/v1/deleteWorkout/workoutId"** sont inutiles.

Lorsque vous regardez notre impl9mentation actuelle, cela devient beaucoup plus propre car nous n'utilisons que deux URL diff9rentes et le comportement r9el est g9r9 via le verbe HTTP et la charge utile de la requate correspondante.

J'imagine toujours que le verbe HTTP d9crit l'action (ce que nous aimerions faire) et l'URL elle-mame (qui pointe vers une ressource) la cible. **"GET /api/v1/workouts"** est 9galement plus fluide en langage humain.

### Grouper les ressources associ9es ensemble (imbrication logique)

Lorsque vous concevez votre API, il peut y avoir des cas o9 vous avez des ressources associ9es 0 d'autres. Il est bon de les regrouper dans un seul endpoint et de les imbriquer correctement.

Supposons que dans notre API, nous avons 9galement une liste de membres inscrits dans notre CrossFit box ("box" est le nom pour une salle de sport CrossFit). Afin de motiver nos membres, nous suivons les records globaux de la box pour chaque entraenement.

Par exemple, il y a un entraenement o9 vous devez faire un certain ordre d'exercices le plus rapidement possible. Nous enregistrons les temps pour tous les membres afin d'avoir une liste des temps pour chaque membre qui a compl9t9 cet entraenement.

Maintenant, le frontend a besoin d'un endpoint qui r9ponde avec tous les records pour un entraenement sp9cifique afin de l'afficher dans l'interface utilisateur.

Les entraenements, les membres et les records sont stock9s dans diff9rents endroits de la base de donn9es. Donc, ce dont nous avons besoin ici, c'est une box (records) dans une autre box (entraenements), n'est-ce pas ?

L'URI pour cet endpoint sera **/api/v1/workouts/:workoutId/records**. C'est une bonne pratique de permettre l'imbrication logique des URL. L'URL elle-mame ne doit pas n9cessairement refl9ter la structure de la base de donn9es.

Commen7ons 0 impl9menter cet endpoint.

Tout d'abord, ajoutez un nouveau tableau dans votre db.json appel9 "members". Placez-le sous "workouts".

```json
{
  "workouts": [ ...
  ],
  "members": [
    {
      "id": "12a410bc-849f-4e7e-bfc8-4ef283ee4b19",
      "name": "Jason Miller",
      "gender": "male",
      "dateOfBirth": "23/04/1990",
      "email": "jason@mail.com",
      "password": "666349420ec497c1dc890c45179d44fb13220239325172af02d1fb6635922956"
    },
    {
      "id": "2b9130d4-47a7-4085-800e-0144f6a46059",
      "name": "Tiffany Brookston",
      "gender": "female",
      "dateOfBirth": "09/06/1996",
      "email": "tiffy@mail.com",
      "password": "8a1ea5669b749354110dcba3fac5546c16e6d0f73a37f35a84f6b0d7b3c22fcc"
    },
    {
      "id": "11817fb1-03a1-4b4a-8d27-854ac893cf41",
      "name": "Catrin Stevenson",
      "gender": "female",
      "dateOfBirth": "17/08/2001",
      "email": "catrin@mail.com",
      "password": "18eb2d6c5373c94c6d5d707650d02c3c06f33fac557c9cfb8cb1ee625a649ff3"
    },
    {
      "id": "6a89217b-7c28-4219-bd7f-af119c314159",
      "name": "Greg Bronson",
      "gender": "male",
      "dateOfBirth": "08/04/1993",
      "email": "greg@mail.com",
      "password": "a6dcde7eceb689142f21a1e30b5fdb868ec4cd25d5537d67ac7e8c7816b0e862"
    }
  ]
}
```

Avant que vous ne commen7iez 0 demander, oui, les mots de passe sont hach9s. 0999

Apr8s cela, ajoutez quelques "records" sous "members".

```json
{
  "workouts": [ ...
  ],
  "members": [ ...
  ],
  "records": [
    {
      "id": "ad75d475-ac57-44f4-a02a-8f6def58ff56",
      "workout": "4a3d9aaa-608c-49a7-a004-66305ad4ab50",
      "record": "160 reps"
    },
    {
      "id": "0bff586f-2017-4526-9e52-fe3ea46d55ab",
      "workout": "d8be2362-7b68-4ea4-a1f6-03f8bc4eede7",
      "record": "7:23 minutes"
    },
    {
      "id": "365cc0bb-ba8f-41d3-bf82-83d041d38b82",
      "workout": "a24d2618-01d1-4682-9288-8de1343e53c7",
      "record": "358 reps"
    },
    {
      "id": "62251cfe-fdb6-4fa6-9a2d-c21be93ac78d",
      "workout": "4a3d9aaa-608c-49a7-a004-66305ad4ab50",
      "record": "145 reps"
    }
  ],
}
```

Pour vous assurer que vous avez les mames entraenements que moi avec les mames identifiants, copiez 9galement les entraenements :

```json
{
  "workouts": [
    {
      "id": "61dbae02-c147-4e28-863c-db7bd402b2d6",
      "name": "Tommy V",
      "mode": "For Time",
      "equipment": [
        "barbell",
        "rope"
      ],
      "exercises": [
        "21 thrusters",
        "12 rope climbs, 15 ft",
        "15 thrusters",
        "9 rope climbs, 15 ft",
        "9 thrusters",
        "6 rope climbs, 15 ft"
      ],
      "createdAt": "4/20/2022, 2:21:56 PM",
      "updatedAt": "4/20/2022, 2:21:56 PM",
      "trainerTips": [
        "Split the 21 thrusters as needed",
        "Try to do the 9 and 6 thrusters unbroken",
        "RX Weights: 115lb/75lb"
      ]
    },
    {
      "id": "4a3d9aaa-608c-49a7-a004-66305ad4ab50",
      "name": "Dead Push-Ups",
      "mode": "AMRAP 10",
      "equipment": [
        "barbell"
      ],
      "exercises": [
        "15 deadlifts",
        "15 hand-release push-ups"
      ],
      "createdAt": "1/25/2022, 1:15:44 PM",
      "updatedAt": "3/10/2022, 8:21:56 AM",
      "trainerTips": [
        "Deadlifts are meant to be light and fast",
        "Try to aim for unbroken sets",
        "RX Weights: 135lb/95lb"
      ]
    },
    {
      "id": "d8be2362-7b68-4ea4-a1f6-03f8bc4eede7",
      "name": "Heavy DT",
      "mode": "5 Rounds For Time",
      "equipment": [
        "barbell",
        "rope"
      ],
      "exercises": [
        "12 deadlifts",
        "9 hang power cleans",
        "6 push jerks"
      ],
      "createdAt": "11/20/2021, 5:39:07 PM",
      "updatedAt": "4/22/2022, 5:49:18 PM",
      "trainerTips": [
        "Aim for unbroken push jerks",
        "The first three rounds might feel terrible, but stick to it",
        "RX Weights: 205lb/145lb"
      ]
    },
    {
      "name": "Core Buster",
      "mode": "AMRAP 20",
      "equipment": [
        "rack",
        "barbell",
        "abmat"
      ],
      "exercises": [
        "15 toes to bars",
        "10 thrusters",
        "30 abmat sit-ups"
      ],
      "trainerTips": [
        "Split your toes to bars in two sets maximum",
        "Go unbroken on the thrusters",
        "Take the abmat sit-ups as a chance to normalize your breath"
      ],
      "id": "a24d2618-01d1-4682-9288-8de1343e53c7",
      "createdAt": "4/22/2022, 5:50:17 PM",
      "updatedAt": "4/22/2022, 5:50:17 PM"
    }
  ],
  "members": [ ...
  ],
  "records": [ ...
  ]
}
```

D'accord, prenons quelques minutes pour r9fl9chir 0 notre impl9mentation. 

Nous avons une ressource appel9e "workouts" d'un c4t9 et une autre appel9e "records" de l'autre c4t9. 

Pour avancer dans notre architecture, il serait conseill9 de cr9er un autre contr4leur, un autre service et une autre collection de m9thodes de base de donn9es responsables des records. 

Il est probable que nous devions impl9menter des endpoints CRUD pour les records 9galement, car les records doivent atre ajout9s, mis 0 jour ou supprim9s 0 l'avenir. Mais ce ne sera pas la t2che principale pour l'instant.

Nous aurons 9galement besoin d'un routeur de records pour capturer les requates sp9cifiques aux records, mais nous n'en avons pas besoin pour l'instant. Cela pourrait atre une excellente opportunit9 pour vous d'impl9menter les op9rations CRUD pour les records avec leurs propres routes et de vous entraener un peu.

```bash
# Cr9er un contr4leur de records 
touch src/controllers/recordController.js 

# Cr9er un service de records 
touch src/services/recordService.js 

# Cr9er des m9thodes de base de donn9es pour les records 
touch src/database/Record.js
```

C'9tait facile. Continuons et commen7ons par l'impl9mentation de nos m9thodes de base de donn9es.

```javascript
// Dans src/database/Record.js
const DB = require("./db.json");

const getRecordForWorkout = (workoutId) => {
  try {
    const record = DB.records.filter((record) => record.workout === workoutId);
    if (!record) {
      throw {
        status: 400,
        message: `Can't find workout with the id '${workoutId}'`,
      };
    }
    return record;
  } catch (error) {
    throw { status: error?.status || 500, message: error?.message || error };
  }
};
module.exports = { getRecordForWorkout };

```

Assez simple, n'est-ce pas ? Nous filtrons tous les records qui sont li9s 0 l'identifiant de l'entraenement dans le param8tre de la requate.

Le suivant est notre service de records :

```javascript
// Dans src/services/recordService.js
const Record = require("../database/Record");

const getRecordForWorkout = (workoutId) => {
  try {
    const record = Record.getRecordForWorkout(workoutId);
    return record;
  } catch (error) {
    throw error;
  }
};
module.exports = { getRecordForWorkout };

```

Encore une fois, rien de nouveau ici.

Maintenant, nous sommes en mesure de cr9er une nouvelle route dans notre routeur d'entraenement et de diriger la requate vers notre service de records.

```javascript
// Dans src/v1/routes/workoutRoutes.js
const express = require("express");
const workoutController = require("../../controllers/workoutController");
// *** AJOUTER ***
const recordController = require("../../controllers/recordController");

const router = express.Router();

router.get("/", workoutController.getAllWorkouts);

router.get("/:workoutId", workoutController.getOneWorkout);

// *** AJOUTER ***
router.get("/:workoutId/records", recordController.getRecordForWorkout);

router.post("/", workoutController.createNewWorkout);

router.patch("/:workoutId", workoutController.updateOneWorkout);

router.delete("/:workoutId", workoutController.deleteOneWorkout);

module.exports = router;

```

G9nial ! Testons les choses dans notre navigateur.

Tout d'abord, nous r9cup9rons tous les entraenements pour obtenir un identifiant d'entraenement.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Bildschirmfoto-2022-04-30-um-15.36.48.png)

Voyons si nous pouvons r9cup9rer tous les records pour cela :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Bildschirmfoto-2022-04-30-um-15.36.32.png)

Comme vous pouvez le voir, l'imbrication logique a du sens lorsque vous avez des ressources qui peuvent atre li9es ensemble. Th9oriquement, vous pouvez l'imbriquer aussi profond9ment que vous le souhaitez, mais la r8gle empirique ici est d'aller jusqu'0 trois niveaux de profondeur maximum.

Si vous souhaitez imbriquer plus profond9ment que cela, vous pourriez faire un petit ajustement dans vos enregistrements de base de donn9es. Je vais vous montrer un petit exemple.

Imaginez que le frontend a 9galement besoin d'un endpoint pour obtenir des informations sur quel membre d9tient exactement le record actuel et souhaite recevoir des m9tadonn9es 0 leur sujet.

Bien sbr, nous pourrions impl9menter l'URI suivante :

```javascript
GET /api/v1/workouts/:workoutId/records/members/:memberId
```

L'endpoint devient maintenant moins g9rable plus nous ajoutons d'imbrications. Par cons9quent, il est bon de stocker l'URI pour recevoir des informations sur un membre directement dans le record.

Consid9rez ce qui suit dans la base de donn9es :

```json
{
  "workouts": [ ...
  ],
  "members": [ ...
  ],
  "records": [ ... {
      "id": "ad75d475-ac57-44f4-a02a-8f6def58ff56",
      "workout": "4a3d9aaa-608c-49a7-a004-66305ad4ab50",
      "record": "160 reps",
      "memberId": "11817fb1-03a1-4b4a-8d27-854ac893cf41",
      "member": "/members/:memberId"
    },
  ]
}
```

Comme vous pouvez le voir, nous avons ajout9 les deux propri9t9s "memberId" et "member" 0 nos records dans la base de donn9es. Cela pr9sente l'9norme avantage que nous n'avons pas besoin d'imbriquer plus profond9ment notre endpoint existant.

Le frontend doit simplement appeler **GET /api/v1/workouts/:workoutId/records** et re7oit automatiquement tous les records qui sont connect9s avec cet entraenement. 

En plus de cela, il obtient l'identifiant du membre et l'endpoint pour r9cup9rer des informations sur ce membre. Ainsi, nous avons 9vit9 l'imbrication plus profonde de notre endpoint.

Bien sbr, cela ne fonctionne que si nous pouvons g9rer les requates vers "/members/:memberId" 0991 Cela semble atre une excellente opportunit9 de formation pour vous d'impl9menter cette situation !

### Int9grer le filtrage, le tri et la pagination

Actuellement, nous sommes en mesure d'effectuer plusieurs op9rations avec notre API. C'est un grand progr8s, mais il y a plus.

Au cours des derni8res sections, nous nous sommes concentr9s sur l'am9lioration de l'exp9rience d9veloppeur et sur la mani8re dont notre API peut atre interagie. Mais la performance globale de notre API est un autre facteur cl9 que nous devons travailler.

C'est pourquoi l'int9gration du filtrage, du tri et de la pagination est 9galement un facteur essentiel sur ma liste.

Imaginez que nous avons 2 000 entraenements, 450 records et 500 membres stock9s dans notre DB. Lorsque nous appelons notre endpoint pour obtenir tous les entraenements, nous ne voulons pas envoyer les 2 000 entraenements en une seule fois. Cela sera bien sbr une r9ponse tr8s lente, ou cela fera planter nos syst8mes (peut-atre avec 200 000 0991).

C'est la raison pour laquelle le filtrage et la pagination sont importants. Le filtrage, comme le nom l'indique d9j0, est utile car il nous permet d'obtenir des donn9es sp9cifiques 0 partir de notre collection compl8te. Par exemple, tous les entraenements qui ont le mode "For Time".

La pagination est un autre m9canisme pour diviser notre collection compl8te d'entraenements en plusieurs "pages" o9 chaque page ne se compose que de vingt entraenements, par exemple. Cette technique nous aide 0 nous assurer que nous n'envoyons pas plus de vingt entraenements en mame temps avec notre r9ponse au client.

Le tri peut atre une t2che complexe. Il est donc plus efficace de le faire dans notre API et d'envoyer les donn9es tri9es au client.

Commen7ons par int9grer un m9canisme de filtrage dans notre API. Nous allons am9liorer notre endpoint qui envoie tous les entraenements en acceptant des param8tres de filtre. Normalement, dans une requate GET, nous ajoutons les crit8res de filtre en tant que param8tre de requate.

Notre nouvelle URI ressemblera 0 ceci, lorsque nous souhaitons obtenir uniquement les entraenements qui sont en mode "AMRAP" (**A**s **M**any **R**ounds **A**s **P**ossible) : **/api/v1/workouts?mode=amrap.**

Pour rendre cela plus amusant, nous devons ajouter quelques entraenements suppl9mentaires. Collez ces entraenements dans votre collection "workouts" dans db.json :

```json
{
  "name": "Jumping (Not) Made Easy",
  "mode": "AMRAP 12",
  "equipment": [
    "jump rope"
  ],
  "exercises": [
    "10 burpees",
    "25 double-unders"
  ],
  "trainerTips": [
    "Scale to do 50 single-unders, if double-unders are too difficult"
  ],
  "id": "8f8318f8-b869-4e9d-bb78-88010193563a",
  "createdAt": "4/25/2022, 2:45:28 PM",
  "updatedAt": "4/25/2022, 2:45:28 PM"
},
{
  "name": "Burpee Meters",
  "mode": "3 Rounds For Time",
  "equipment": [
    "Row Erg"
  ],
  "exercises": [
    "Row 500 meters",
    "21 burpees",
    "Run 400 meters",
    "Rest 3 minutes"
  ],
  "trainerTips": [
    "Go hard",
    "Note your time after the first run",
    "Try to hold your pace"
  ],
  "id": "0a5948af-5185-4266-8c4b-818889657e9d",
  "createdAt": "4/25/2022, 2:48:53 PM",
  "updatedAt": "4/25/2022, 2:48:53 PM"
},
{
  "name": "Dumbbell Rower",
  "mode": "AMRAP 15",
  "equipment": [
    "Dumbbell"
  ],
  "exercises": [
    "15 dumbbell rows, left arm",
    "15 dumbbell rows, right arm",
    "50-ft handstand walk"
  ],
  "trainerTips": [
    "RX weights for women: 35-lb",
    "RX weights for men: 50-lb"
  ],
  "id": "3dc53bc8-27b8-4773-b85d-89f0a354d437",
  "createdAt": "4/25/2022, 2:56:03 PM",
  "updatedAt": "4/25/2022, 2:56:03 PM"
}
```

Apr8s cela, nous devons accepter et g9rer les param8tres de requate. Notre contr4leur d'entraenement sera le bon endroit pour commencer :

```javascript
// Dans src/controllers/workoutController.js
...

const getAllWorkouts = (req, res) => {
  // *** AJOUTER ***
  const { mode } = req.query;
  try {
    // *** AJOUTER ***
    const allWorkouts = workoutService.getAllWorkouts({ mode });
    res.send({ status: "OK", data: allWorkouts });
  } catch (error) {
    res
      .status(error?.status || 500)
      .send({ status: "FAILED", data: { error: error?.message || error } });
  }
};

...
```

Nous extrayons "mode" de l'objet req.query et d9finissons un param8tre de workoutService.getAllWorkouts. Ce sera un objet qui se compose de nos param8tres de filtre. 

J'utilise la syntaxe abr9g9e ici pour cr9er une nouvelle cl9 appel9e "mode" dans l'objet avec la valeur de ce qui se trouve dans "req.query.mode". Cela peut atre soit une valeur v9ridique, soit ind9finie s'il n'y a pas de param8tre de requate appel9 "mode". Nous pouvons 9tendre cet objet avec plus de param8tres de filtre que nous souhaitons accepter.

Dans notre service d'entraenement, transmettez-le 0 votre m9thode de base de donn9es :

```javascript
// Dans src/services/workoutService.js
...

const getAllWorkouts = (filterParams) => {
  try {
    // *** AJOUTER ***
    const allWorkouts = Workout.getAllWorkouts(filterParams);
    return allWorkouts;
  } catch (error) {
    throw error;
  }
};

...
```

Maintenant, nous pouvons l'utiliser dans notre m9thode de base de donn9es et appliquer le filtrage :

```javascript
// Dans src/database/Workout.js
...

const getAllWorkouts = (filterParams) => {
  try {
    let workouts = DB.workouts;
    if (filterParams.mode) {
      return DB.workouts.filter((workout) =>
        workout.mode.toLowerCase().includes(filterParams.mode)
      );
    }
    // D'autres instructions if iront ici pour diff9rents param8tres
    return workouts;
  } catch (error) {
    throw { status: 500, message: error };
  }
};

...
```

Assez simple, n'est-ce pas ? Tout ce que nous faisons ici est de v9rifier si nous avons effectivement une valeur v9ridique pour la cl9 "mode" dans notre "filterParams". Si c'est vrai, nous filtrons tous les entraenements qui ont le mame "mode". Si ce n'est pas vrai, alors il n'y a pas de param8tre de requate appel9 "mode" et nous retournons tous les entraenements car nous n'avons pas besoin de filtrer.

Nous avons d9fini "workouts" ici comme une variable "let" car lorsque nous ajoutons plus d'instructions if pour diff9rents filtres, nous pouvons 9craser "workouts" et enchaener les filtres.

Dans votre navigateur, vous pouvez visiter localhost:3000/api/v1/workouts?mode=amrap et vous recevrez tous les entraenements "AMRAP" stock9s :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Bildschirmfoto-2022-04-30-um-15.48.57.png)

Si vous laissez le param8tre de requate vide, vous devriez obtenir tous les entraenements comme avant. Vous pouvez essayer davantage en ajoutant "for%20time" comme valeur pour le param8tre "mode" (rappel : "%20" signifie "espace") et vous devriez recevoir tous les entraenements qui ont le mode "For Time" s'il y en a stock9s. 

Lorsque vous tapez une valeur qui n'est pas stock9e, vous devriez recevoir un tableau vide.

Les param8tres pour le tri et la pagination suivent la mame philosophie. Examinons quelques fonctionnalit9s que nous pourrions 9ventuellement impl9menter :

* Recevoir tous les entraenements qui n9cessitent une barre : **/api/v1/workouts?equipment=barbell**
* Obtenir seulement 5 entraenements : **/api/v1/workouts?length=5**
* Lorsque vous utilisez la pagination, recevoir la deuxi8me page : **/api/v1/workouts?page=2**
* Trier les entraenements dans la r9ponse par ordre d9croissant selon leur date de cr9ation : **/api/v1/workouts?sort=-createdAt**
* Vous pouvez 9galement combiner les param8tres, pour obtenir les 10 derniers entraenements mis 0 jour par exemple : **/api/v1/workouts?sort=-updatedAt&length=10**

### Utiliser la mise en cache des donn9es pour am9liorer les performances

L'utilisation d'un cache de donn9es est 9galement une excellente pratique pour am9liorer l'exp9rience globale et les performances de notre API.

Il est tr8s logique d'utiliser un cache pour servir des donn9es, lorsque les donn9es sont une ressource fr9quemment demand9e et/ou lorsque l'interrogation de ces donn9es dans la base de donn9es est une t2che lourde et peut prendre plusieurs secondes.

Vous pouvez stocker ce type de donn9es dans votre cache et les servir 0 partir de l0 au lieu d'aller dans la base de donn9es chaque fois pour interroger les donn9es.

Une chose importante 0 garder 0 l'esprit lors de la fourniture de donn9es 0 partir d'un cache est que ces donn9es peuvent devenir obsol8tes. Vous devez donc vous assurer que les donn9es dans le cache sont toujours 0 jour.

Il existe de nombreuses solutions diff9rentes. Un exemple appropri9 est d'utiliser [redis](https://www.npmjs.com/package/redis) ou le middleware express [apicache](https://www.npmjs.com/package/apicache).

J'aimerais utiliser apicache, mais si vous souhaitez utiliser Redis, je peux fortement recommander de consulter leur excellente [documentation](https://docs.redis.com/latest/rs/references/client_references/client_nodejs/).

Prenons un instant pour r9fl9chir 0 un sc9nario dans notre API o9 un cache serait judicieux. Je pense que la requate pour recevoir tous les entraenements serait efficacement servie 0 partir de notre cache.

Tout d'abord, installons notre middleware :

```bash
npm i apicache
```

Maintenant, nous devons l'importer dans notre routeur d'entraenement et le configurer.

```javascript
// Dans src/v1/routes/workoutRoutes.js
const express = require("express");
// *** AJOUTER ***
const apicache = require("apicache");
const workoutController = require("../../controllers/workoutController");
const recordController = require("../../controllers/recordController");

const router = express.Router();
// *** AJOUTER ***
const cache = apicache.middleware;

// *** AJOUTER ***
router.get("/", cache("2 minutes"), workoutController.getAllWorkouts);

router.get("/:workoutId", workoutController.getOneWorkout);

router.get("/:workoutId/records", recordController.getRecordForWorkout);

router.post("/", workoutController.createNewWorkout);

router.patch("/:workoutId", workoutController.updateOneWorkout);

router.delete("/:workoutId", workoutController.deleteOneWorkout);

module.exports = router;

```

Commencer est assez simple, n'est-ce pas ? Nous pouvons d9finir un nouveau cache en appelant **apicache.middleware** et l'utiliser comme un middleware dans notre route get. Vous devez simplement le mettre en tant que param8tre entre le chemin r9el et notre contr4leur d'entraenement.

L0-dedans, vous pouvez d9finir combien de temps vos donn9es doivent atre mises en cache. Pour les besoins de ce tutoriel, j'ai choisi deux minutes. Le temps d9pend de la rapidit9 ou de la fr9quence de changement de vos donn9es dans votre cache.

Testons les choses !

Dans Postman ou un autre client HTTP de votre choix, d9finissez une nouvelle requate qui obtient tous les entraenements. Je l'ai fait dans le navigateur jusqu'0 pr9sent, mais je souhaite mieux visualiser les temps de r9ponse pour vous. C'est la raison pour laquelle je demande la ressource via Postman pour l'instant.

Appelons notre requate pour la premi8re fois :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Bildschirmfoto-2022-04-26-um-15.36.46-1.png)

Comme vous pouvez le voir, notre API a mis 22,93 ms pour r9pondre. Une fois que notre cache est vide 0 nouveau (apr8s deux minutes), il doit atre rempli 0 nouveau. Cela se produit avec notre premi8re requate.

Donc, dans le cas ci-dessus, les donn9es n'ont PAS 9t9 servies depuis notre cache. Elles ont pris le chemin "r9gulier" depuis la base de donn9es et rempli notre cache.

Maintenant, avec notre deuxi8me requate, nous recevons un temps de r9ponse plus court, car elle a 9t9 servie directement depuis le cache :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Bildschirmfoto-2022-04-26-um-15.36.59-1.png)

Nous avons 9t9 en mesure de servir trois fois plus vite que dans notre requate pr9c9dente ! Tout cela gr2ce 0 notre cache.

Dans notre exemple, nous avons mis en cache une seule route, mais vous pouvez 9galement mettre en cache toutes les routes en l'impl9mentant comme ceci :

```javascript
// Dans src/index.js
const express = require("express");
const bodyParser = require("body-parser");
// *** AJOUTER ***
const apicache = require("apicache");
const v1WorkoutRouter = require("./v1/routes/workoutRoutes");

const app = express();
// *** AJOUTER ***
const cache = apicache.middleware;
const PORT = process.env.PORT || 3000;

app.use(bodyParser.json());
// *** AJOUTER ***
app.use(cache("2 minutes"));
app.use("/api/v1/workouts", v1WorkoutRouter);

app.listen(PORT, () => {
  console.log(`L'API 9coute sur le port ${PORT}`);
});

```

Il y a une chose **importante** que je voudrais noter ici en ce qui concerne la mise en cache. Bien qu'elle semble r9soudre de nombreux probl8mes pour vous, elle peut 9galement apporter certains probl8mes dans votre application.

Quelques points 0 garder 0 l'esprit lors de l'utilisation d'un cache :

* vous devez toujours vous assurer que les donn9es dans le cache sont 0 jour car vous ne voulez pas servir des donn9es obsol8tes 
* pendant que la premi8re requate est en cours de traitement et que le cache est sur le point d'atre rempli et que d'autres requates arrivent, vous devez d9cider si vous retardez ces autres requates et servez les donn9es depuis le cache ou si elles re7oivent 9galement des donn9es directement depuis la base de donn9es comme la premi8re requate
* c'est un autre composant dans votre infrastructure si vous choisissez un cache distribu9 comme Redis (donc vous devez vous demander si cela vaut vraiment la peine de l'utiliser)

Voici comment proc9der habituellement :

J'aime commencer aussi simplement et proprement que possible avec tout ce que je construis. Il en va de mame pour les API. 

Lorsque je commence 0 construire une API et qu'il n'y a pas de raisons particuli8res d'utiliser un cache tout de suite, je le laisse de c4t9 et je vois ce qui se passe avec le temps. Lorsque des raisons d'utiliser un cache se pr9sentent, je peux l'impl9menter 0 ce moment-l0.

### Bonnes pratiques de s9curit9

Waouh ! Cela a 9t9 un voyage assez formidable jusqu'0 pr9sent. Nous avons abord9 de nombreux points importants et 9tendu notre API en cons9quence.

Nous avons parl9 des meilleures pratiques pour augmenter l'utilisabilit9 et la performance de notre API. La s9curit9 est 9galement un facteur cl9 pour les API. Vous pouvez construire la meilleure API, mais si elle est un logiciel vuln9rable en cours d'ex9cution sur un serveur, elle devient inutile et dangereuse.

La premi8re chose et un must absolu est d'utiliser SSL/TLS car c'est un standard de nos jours pour les communications sur Internet. C'est encore plus important pour les API o9 des donn9es priv9es sont envoy9es entre le client et notre API.

Si vous avez des ressources qui ne devraient atre disponibles que pour les utilisateurs authentifi9s, vous devriez les prot9ger avec une v9rification d'authentification. 

Dans Express, par exemple, vous pouvez l'impl9menter en tant que middleware comme nous l'avons fait avec notre cache pour des routes sp9cifiques et v9rifier d'abord si la requate est authentifi9e avant qu'elle n'acc8de 0 une ressource.

Il peut 9galement y avoir des ressources ou des interactions avec notre API que nous ne voulons pas permettre 0 tous les utilisateurs de demander. Vous devriez alors mettre en place un syst8me de r4les pour vos utilisateurs. Vous devez donc ajouter une autre logique de v9rification 0 cette route et valider si l'utilisateur a le privil8ge d'acc9der 0 cette ressource.

Les r4les d'utilisateur auraient 9galement du sens dans notre cas d'utilisation lorsque nous voulons que seuls des utilisateurs sp9cifiques (comme les entraeneurs) cr9ent, mettent 0 jour et suppriment nos entraenements et records. La lecture peut atre pour tout le monde (y compris les membres "r9guliers").

Cela peut atre g9r9 dans un autre middleware que nous utilisons pour les routes que nous souhaitons prot9ger. Par exemple, notre requate POST vers /api/v1/workouts pour cr9er un nouvel entraenement. 

Dans le premier middleware, nous v9rifierons si l'utilisateur est authentifi9. Si c'est vrai, nous passerons au middleware suivant, qui serait celui pour v9rifier le r4le de l'utilisateur. Si l'utilisateur a le r4le appropri9 pour acc9der 0 cette ressource, la requate est transmise au contr4leur correspondant.

Dans le gestionnaire de route, cela ressemblerait 0 ceci :

```javascript
// Dans src/v1/routes/workoutRoutes.js
...

// Middlewares personnalis9s
const authenticate = require("../../middlewares/authenticate");
const authorize = require("../../middlewares/authorize");

router.post("/", authenticate, authorize, workoutController.createNewWorkout);

...
```

Pour lire davantage et obtenir d'autres bonnes pratiques sur ce sujet, je peux sugg9rer de lire [cet article](https://restfulapi.net/security-essentials/).

### Documenter correctement votre API

Je sais que la documentation n'est d9finitivement pas une t2che pr9f9r9e des d9veloppeurs, mais c'est une chose n9cessaire 0 faire. Surtout lorsqu'il s'agit d'une API.

Certaines personnes disent :

> "Une API est aussi bonne que sa documentation"

Je pense qu'il y a beaucoup de v9rit9 dans cette d9claration car si une API n'est pas bien document9e, elle ne peut pas atre utilis9e correctement et devient donc inutile. La documentation aide 9galement 0 rendre la vie des d9veloppeurs beaucoup plus facile.

N'oubliez jamais que la documentation est g9n9ralement la premi8re interaction que les consommateurs ont avec votre API. Plus les utilisateurs peuvent comprendre rapidement la documentation, plus ils peuvent utiliser rapidement l'API.

C'est donc notre travail d'impl9menter une bonne et pr9cise documentation. Il existe de nombreux outils qui facilitent notre vie.

Comme dans d'autres domaines de l'informatique, il existe 9galement une sorte de standard pour documenter les API appel9 [Sp9cification OpenAPI](https://swagger.io/specification/).

Voyons comment nous pouvons cr9er une documentation qui justifie cette sp9cification. Nous utiliserons les packages [swagger-ui-express](https://www.npmjs.com/package/swagger-ui-express) et [swagger-jsdoc](https://www.npmjs.com/package/swagger-jsdoc) pour y parvenir. Vous serez 9merveill9 de voir 0 quel point c'est g9nial dans un instant !

Tout d'abord, nous configurons notre structure de base pour notre documentation. Comme nous avons pr9vu d'avoir diff9rentes versions de notre API, les docs seront 9galement un peu diff9rentes. C'est la raison pour laquelle j'aimerais d9finir notre fichier swagger pour lancer notre documentation dans le dossier de version correspondant.

```bash
# Installer les packages npm requis 
npm i swagger-jsdoc swagger-ui-express 

# Cr9er un nouveau fichier pour configurer les docs swagger 
touch src/v1/swagger.js
```

```javascript
// Dans src/v1/swagger.js
const swaggerJSDoc = require("swagger-jsdoc");
const swaggerUi = require("swagger-ui-express");

// Informations m9ta de base sur notre API
const options = {
  definition: {
    openapi: "3.0.0",
    info: { title: "Crossfit WOD API", version: "1.0.0" },
  },
  apis: ["./src/v1/routes/workoutRoutes.js", "./src/database/Workout.js"],
};

// Docs au format JSON
const swaggerSpec = swaggerJSDoc(options);

// Fonction pour configurer nos docs
const swaggerDocs = (app, port) => {
  // Gestionnaire de route pour visiter nos docs
  app.use("/api/v1/docs", swaggerUi.serve, swaggerUi.setup(swaggerSpec));
  // Rendre nos docs disponibles au format JSON
  app.get("/api/v1/docs.json", (req, res) => {
    res.setHeader("Content-Type", "application/json");
    res.send(swaggerSpec);
  });
  console.log(
    `Version 1 Docs are available on http://localhost:${port}/api/v1/docs`
  );
};

module.exports = { swaggerDocs };

```

La configuration est donc assez simple. Nous avons d9fini quelques m9tadonn9es de base de notre API, cr99 les docs au format JSON et cr99 une fonction qui rend nos docs disponibles. 

Pour v9rifier si tout est en ordre, nous enregistrons un simple message dans la console o9 nous pouvons trouver nos docs.

Ce sera la fonction que nous utiliserons dans notre fichier racine, o9 nous avons cr99 le serveur Express pour nous assurer que les docs sont 9galement lanc9es.

```javascript
// Dans src/index.js
const express = require("express");
const bodyParser = require("body-parser");
const v1WorkoutRouter = require("./v1/routes/workoutRoutes");
// *** AJOUTER ***
const { swaggerDocs: V1SwaggerDocs } = require("./v1/swagger");

const app = express();
const PORT = process.env.PORT || 3000;

app.use(bodyParser.json());
app.use("/api/v1/workouts", v1WorkoutRouter);

app.listen(PORT, () => {
  console.log(`L'API 9coute sur le port ${PORT}`);
  /// *** AJOUTER ***
  V1SwaggerDocs(app, PORT);
});

```

Maintenant, vous devriez voir dans votre terminal o9 votre serveur de d9veloppement est en cours d'ex9cution :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Bildschirmfoto-2022-04-28-um-20.23.51-1.png)

Et lorsque vous visitez localhost:3000/api/v1/docs, vous devriez d9j0 voir notre page de docs :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Bildschirmfoto-2022-04-28-um-20.25.00-1.png)

Je suis 9merveill9 chaque fois de voir 0 quel point cela fonctionne bien. Maintenant, la structure de base est configur9e et nous pouvons commencer 0 impl9menter les docs pour nos endpoints. C'est parti !

Lorsque vous regardez **options.apis** dans notre fichier swagger.js, vous verrez que nous avons inclus le chemin vers nos routes d'entraenement et vers le fichier d'entraenement dans notre dossier de base de donn9es. C'est la chose la plus importante dans la configuration qui rendra toute la magie possible.

Avoir ces fichiers d9finis dans nos options swagger nous permettra d'utiliser des commentaires qui r9f9rencent OpenAPI et ont une syntaxe comme dans les fichiers yaml, qui sont n9cessaires pour configurer nos docs.

Maintenant, nous sommes prats 0 cr9er des docs pour notre premier endpoint ! Sautons directement dedans.

```javascript
// Dans src/v1/routes/workoutRoutes.js
...

/**
 * @openapi
 * /api/v1/workouts:
 *   get:
 *     tags:
 *       - Workouts
 *     responses:
 *       200:
 *         description: OK
 *         content:
 *           application/json:
 *             schema:
 *               type: object
 *               properties:
 *                 status:
 *                   type: string
 *                   example: OK
 *                 data:
 *                   type: array 
 *                   items: 
 *                     type: object
 */
router.get("/", cache("2 minutes"), workoutController.getAllWorkouts);

...
```

C'est essentiellement toute la magie pour ajouter un endpoint 0 nos docs swagger. Vous pouvez consulter toutes les sp9cifications pour d9crire un endpoint dans leur [excellente documentation](https://swagger.io/docs/specification/about/).

Lorsque vous rechargez votre page de docs, vous devriez voir ce qui suit :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Bildschirmfoto-2022-04-29-um-07.21.51-1.png)

Cela devrait vous sembler tr8s familier si vous avez d9j0 travaill9 avec des API qui ont une documentation OpenAPI. C'est la vue o9 tous nos endpoints seront list9s et vous pouvez 9tendre chacun pour obtenir plus d'informations 0 son sujet.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Bildschirmfoto-2022-04-29-um-07.41.46-1.png)

Lorsque vous regardez de pr8s notre r9ponse, vous verrez que nous n'avons pas d9fini la valeur de retour correcte car nous disons simplement que notre propri9t9 "data" sera un tableau d'objets vides.

C'est l0 que les sch9mas entrent en jeu.

```javascript
// Dans src/databse/Workout.js
...

/**
 * @openapi
 * components:
 *   schemas:
 *     Workout:
 *       type: object
 *       properties:
 *         id: 
 *           type: string
 *           example: 61dbae02-c147-4e28-863c-db7bd402b2d6
 *         name: 
 *           type: string
 *           example: Tommy V  
 *         mode:
 *           type: string
 *           example: For Time
 *         equipment:
 *           type: array
 *           items:
 *             type: string
 *           example: ["barbell", "rope"]
 *         exercises:
 *           type: array
 *           items:
 *             type: string
 *           example: ["21 thrusters", "12 rope climbs, 15 ft", "15 thrusters", "9 rope climbs, 15 ft", "9 thrusters", "6 rope climbs, 15 ft"]
 *         createdAt:
 *           type: string
 *           example: 4/20/2022, 2:21:56 PM
 *         updatedAt: 
 *           type: string
 *           example: 4/20/2022, 2:21:56 PM
 *         trainerTips:
 *           type: array
 *           items:
 *             type: string
 *           example: ["Split the 21 thrusters as needed", "Try to do the 9 and 6 thrusters unbroken", "RX Weights: 115lb/75lb"]
 */

...
```

Dans l'exemple ci-dessus, nous avons cr99 notre premier sch9ma. Typiquement, cette d9finition sera dans votre fichier de sch9ma ou de mod8le o9 vous avez d9fini vos mod8les de base de donn9es.

Comme vous pouvez le voir, c'est 9galement assez simple. Nous avons d9fini toutes les propri9t9s qui composent un entraenement, y compris le type et un exemple.

Vous pouvez visiter notre page de docs 0 nouveau et nous recevrons une autre section contenant nos sch9mas.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Bildschirmfoto-2022-04-29-um-07.29.49-1.png)

Ce sch9ma peut maintenant atre r9f9renc9 dans notre r9ponse de notre endpoint.

```javascript
// Dans src/v1/routes/workoutRoutes.js
...

/**
 * @openapi
 * /api/v1/workouts:
 *   get:
 *     tags:
 *       - Workouts
 *     responses:
 *       200:
 *         description: OK
 *         content:
 *           application/json:
 *             schema:
 *               type: object
 *               properties:
 *                 status:
 *                   type: string
 *                   example: OK
 *                 data:
 *                   type: array 
 *                   items: 
 *                     $ref: "#/components/schemas/Workout"
 */
router.get("/", cache("2 minutes"), workoutController.getAllWorkouts);

...
```

Regardez de pr8s le bas de notre commentaire sous "items". Nous utilisons "$ref" pour cr9er une r9f9rence et r9f9rencer le chemin vers notre sch9ma que nous avons d9fini dans notre fichier d'entraenement.

Maintenant, nous sommes en mesure de montrer un Workout complet dans notre r9ponse.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Bildschirmfoto-2022-04-29-um-07.44.12-1.png)

Assez cool, n'est-ce pas ? Vous pourriez penser "taper ces commentaires 0 la main peut atre une t2che fastidieuse". 

Cela pourrait atre vrai, mais pensez-y de cette mani8re. Ces commentaires qui sont dans votre base de code sont 9galement une excellente documentation pour vous-mame en tant que d9veloppeur d'API. Vous n'avez pas besoin de visiter les docs tout le temps lorsque vous voulez connaetre la documentation d'un endpoint sp9cifique. Vous pouvez simplement le consulter en un seul endroit dans votre code source. 

Documenter les endpoints aide 9galement 0 mieux les comprendre et vous "force" 0 penser 0 tout ce que vous auriez pu oublier d'impl9menter.

Comme vous pouvez le voir, j'ai effectivement oubli9 quelque chose. Les r9ponses d'erreur possibles et les param8tres de requate sont encore manquants !

Corrigeons cela :

```javascript
// Dans src/v1/routes/workoutRoutes.js
...

/**
 * @openapi
 * /api/v1/workouts:
 *   get:
 *     tags:
 *       - Workouts
 *     parameters:
 *       - in: query
 *         name: mode
 *         schema:
 *           type: string
 *         description: The mode of a workout
 *     responses:
 *       200:
 *         description: OK
 *         content:
 *           application/json:
 *             schema:
 *               type: object
 *               properties:
 *                 status:
 *                   type: string
 *                   example: OK
 *                 data:
 *                   type: array 
 *                   items: 
 *                     $ref: "#/components/schemas/Workout"
 *       5XX:
 *         description: FAILED
 *         content:
 *           application/json:
 *             schema:
 *               type: object
 *               properties:
 *                 status: 
 *                   type: string
 *                   example: FAILED
 *                 data:
 *                   type: object
 *                   properties:
 *                     error:
 *                       type: string 
 *                       example: "Some error message"
 */
router.get("/", cache("2 minutes"),  workoutController.getAllWorkouts);

...
```

Lorsque vous regardez le haut de notre commentaire sous "tags", vous pouvez voir que j'ai ajout9 une autre cl9 appel9e "parameters", o9 j'ai d9fini notre param8tre de requate pour le filtrage.

Nos docs affichent maintenant cela correctement :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Bildschirmfoto-2022-04-29-um-08.03.00-1.png)

Et pour documenter un cas d'erreur possible, nous ne renvoyons qu'une erreur 5XX 0 ce stade. Donc sous "responses", vous pouvez voir que j'ai 9galement d9fini une autre documentation pour cela.

Sur notre page de docs, cela ressemble 0 ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Bildschirmfoto-2022-04-29-um-08.04.44-2.png)

G9nial ! Nous venons de cr9er la documentation compl8te pour un endpoint. Je vous recommande vivement d'impl9menter le reste des endpoints par vous-mame pour vous familiariser avec cela. Vous apprendrez beaucoup dans le processus !

Comme vous l'avez peut-atre vu, documenter votre API ne doit pas toujours atre un casse-tate. Je pense que les outils que je vous ai pr9sent9s r9duisent votre effort global, et la configuration est assez simple.

Nous pouvons donc nous concentrer sur l'essentiel, la documentation elle-mame. 0 mon avis, la documentation de swagger/OpenAPI est tr8s bonne et il existe de nombreux excellents exemples sur Internet.

Ne pas avoir de documentation en raison de trop de travail "suppl9mentaire" ne devrait plus atre une raison.

## Conclusion

Pfiou, c'9tait un voyage assez amusant. J'ai vraiment appr9ci9 9crire cet article pour vous et j'ai 9galement beaucoup appr9s.

Il peut y avoir des bonnes pratiques qui sont importantes tandis que d'autres peuvent ne pas sembler s'appliquer 0 votre situation actuelle. C'est bien, car comme je l'ai dit pr9c9demment, c'est la responsabilit9 de chaque ing9nieur de choisir les bonnes pratiques qui peuvent atre appliqu9es 0 leur situation actuelle.

J'ai fait de mon mieux pour fusionner toutes ces bonnes pratiques que j'ai r9alis9es jusqu'0 pr9sent tout en construisant notre propre API en cours de route. Cela a rendu cela tr8s amusant pour moi !

J'adorerais recevoir des retours de toute sorte. Si vous avez quelque chose 0 me dire (bon ou mauvais), n'h9sitez pas 0 me contacter :

Voici [mon Instagram](https://www.instagram.com/jean_marc.dev/) (vous pouvez 9galement suivre mon parcours en tant que d9veloppeur logiciel)

0 la prochaine !