---
title: Construire une application Node.js sur Android, Partie 2
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-03-26T19:52:47.000Z'
originalURL: https://freecodecamp.org/news/building-a-node-js-application-on-android-part-2-express-and-nedb-ced04caea7bb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*gpCGhSHig8ZaHUOxjDJO8g.jpeg
tags:
- name: api
  slug: api
- name: JavaScript
  slug: javascript
- name: learning to code
  slug: learning-to-code
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
seo_title: Construire une application Node.js sur Android, Partie 2
seo_desc: 'By Aurélien Giraud

  Part 2: Express and NeDB


  In Part 1 we saw how to use Termux, a Terminal emulator and Linux environment for
  Android. We also edited files with Vim and saw how to run Node. We are now going
  to build a small node application with the...'
---

Par Aurélien Giraud

#### Partie 2 : Express et NeDB

![Image](https://cdn-media-1.freecodecamp.org/images/1*gpCGhSHig8ZaHUOxjDJO8g.jpeg)

Dans la [Partie 1](https://medium.freecodecamp.com/building-a-node-js-application-on-android-part-1-termux-vim-and-node-js-dfa90c28958f#.6oc2qvfwl), nous avons vu comment utiliser Termux, un émulateur de terminal et un environnement Linux pour Android. Nous avons également édité des fichiers avec Vim et vu comment exécuter Node. Nous allons maintenant construire une petite application Node avec le framework Express et utiliser NeDB pour la base de données.

### L'histoire et qui pourrait en bénéficier

Quand j'ai découvert que je pouvais construire une application Node.js complète avec une base de données de type Mongo sur ma tablette Android, j'ai été vraiment excité. J'ai donc décidé d'essayer et de partager mon expérience.

Il s'avère que, une fois Termux en cours d'exécution sur Android et Node installé, le fait que nous soyons sur Android au lieu de Linux ne fait pas une grande différence. En fait, toute la configuration spécifique à Termux a été faite dans la Partie 1 et vous êtes les bienvenus pour coder sur votre appareil/ordinateur/IDE cloud préféré...

Cela signifie également que, à part le fait que nous substituons Mongo par NeDB, cet article est comme l'introduction habituelle à la construction d'une API RESTful et est principalement destiné aux personnes qui sont plutôt nouvelles dans Node, Express et Mongo/NeDB.

### Ce que nous allons faire

![Image](https://cdn-media-1.freecodecamp.org/images/1*9CqFS4MJHVuFSPiFTMasDA.png)
_Un suivi de base des objectifs récurrents_

Afin de démontrer comment commencer avec le framework web Express et une base de données NeDB, examinons un suivi de base des objectifs que j'ai construit pour moi-même. À l'étape actuelle, il ressemble à ce qui est montré dans l'image ci-dessus.

Les utilisateurs peuvent :

* soumettre un nouvel objectif
* supprimer un objectif
* enregistrer un succès pour un objectif
* enregistrer un échec pour un objectif

Eh bien, en fait, nous allons seulement implémenter les deux premières fonctionnalités dans cet article, et au cas où vous seriez curieux au sujet des deux restantes, je fournirai à la fin un lien vers le code de l'implémentation complète.

Ainsi, sans le besoin d'enregistrer les succès et les échecs, notre code sera un peu plus simple :

![Image](https://cdn-media-1.freecodecamp.org/images/1*RkYG-8TICUIdjaKhR1OD5g.png)

Voici les étapes que nous allons suivre :

1. Configurer le serveur avec **Express**.
2. Décrire quelques **histoires utilisateur**.
3. Configurer **NeDB**.
4. Construire une **API RESTful**.

### Prérequis

Nous allons commencer là où nous nous sommes arrêtés dans la Partie 1. Ainsi, la seule exigence est que Node soit installé.

### 1. Configuration du serveur avec Express

[Express](http://expressjs.com/) est un framework web pour Node qui aide à construire des applications Node. Si vous avez du mal à comprendre ce qu'Express apporte à Node, je vous recommande de consulter l'article d'Evan Hahn [Comprendre Express](http://evanhahn.com/understanding-express/).

Commençons un nouveau projet :

```bash
$ mkdir goals-tracker && cd goals-tracker
$ npm init
$ touch server.js
```

et installons Express :

```bash
npm install express --save
```

Nous allons utiliser Express pour définir les routes, c'est-à-dire définir les points de terminaison de l'application (URIs) et configurer comment l'application répond aux requêtes des clients.

Ouvrez server.js et copiez-collez/écrivez :

```js
// server.js

// DÉPENDANCES ET CONFIGURATION
// ===============================================

var express = require('express'),
  app = express(),
  port = Number(process.env.PORT || 8080);

// ROUTES
// ===============================================

// Définir la route de la page d'accueil.
app.get('/', function(req, res) {
  res.send('Notre première route fonctionne. :)');
});

// DÉMARRER LE SERVEUR
// ===============================================

app.listen(port, function() {
  console.log('Écoute sur le port ' + port);
});
```

Avec cela en place, vous pouvez démarrer l'application :

```bash
$ node server.js
```

Cela devrait imprimer dans la console le numéro du port sur lequel le serveur écoute. Si vous visitez [**http://localhost:8080**](http://localhost:8080) dans le navigateur (en supposant que 8080 est le numéro qui a été imprimé dans la console), vous devriez voir sur la page : Notre première route fonctionne. :)

#### Quelques explications

Le **'/'** dans **app.get( ... )** définit la route où nous voulons attacher un comportement du serveur. Utiliser '/' fait référence à l'URI de base, dans notre cas : [http://localhost:8080](http://localhost:8080/goals). Notez que nous obtiendrions le même résultat dans la fenêtre du navigateur si nous utilisions **app.get('/goals', ...)** à la place et visitions [http://localhost:8080/goals](http://localhost:8080/goals).

Le deuxième argument dans **app.get( ... )** est une fonction de rappel qui nous permet de définir ce que le serveur doit faire lorsque la route donnée comme premier argument est visitée. Dans cette fonction :

* **req** signifie **requête** : ce sont les informations que le serveur reçoit d'un client (par exemple, cela peut provenir de quelqu'un utilisant la partie front-end du site web/application).
* **res** signifie **réponse** : ce sont les informations que le serveur renvoie à l'utilisateur. Cela peut être une page web ou d'autres données comme une image, du JSON ou du XML.

#### Nodemon

Dans les prochaines parties de ce tutoriel, nous allons apporter plusieurs modifications au fichier server.js. Afin d'éviter de redémarrer le serveur manuellement à chaque fois pour voir le résultat, nous pouvons installer [**nodemon**](http://nodemon.io/).

Nodemon est un utilitaire qui surveillera les changements dans votre code et redémarrera automatiquement le serveur. Nous allons l'installer comme une dépendance uniquement pour le développement en utilisant le tag save-dev :

```bash
npm install nodemon --save-dev
```

Maintenant, vous pouvez redémarrer le serveur avec la commande nodemon au lieu de node :

```bash
nodemon server.js
```

### 2. Les histoires utilisateur

Avant de passer à la partie sur NeDB, faisons une pause pour réfléchir à la logique métier. Afin de voir ce que nous devons implémenter, nous commençons par définir quelques histoires utilisateur.

Une [histoire utilisateur](https://fr.wikipedia.org/wiki/Histoire_utilisateur) est une définition de très haut niveau d'une exigence. Les histoires utilisateur sont utiles pour discuter du produit en termes non techniques avec un client, pour estimer combien de temps et d'efforts l'implémentation d'une fonctionnalité prendra, pour guider le développement global d'une application, et pour faire du [Développement Piloté par les Tests](https://fr.wikipedia.org/wiki/Test_driven_development).

Voici les 4 histoires utilisateur que nous allons utiliser :

1. En tant qu'utilisateur, je peux sauvegarder un nouvel objectif avec sa date de création.
2. En tant qu'utilisateur, je peux accéder à tous les objectifs qui ont été sauvegardés.
3. En tant qu'utilisateur, je peux accéder à toutes les informations sur un objectif.
4. En tant qu'utilisateur, je peux supprimer un objectif.

Dans notre cas, les histoires correspondent une à une aux 4 opérations CRUD dont nous allons parler dans la Partie 4.

### 3. Utilisation de NeDB

Le fait que [NeDB](https://github.com/louischatriot/nedb#inserting-documents) soit facile à installer, bien documenté et utilise l'API de MongoDB le rend parfait pour commencer à développer des applications Node.js sur Android. Il existe même [un outil](https://github.com/louischatriot/nedb-to-mongodb) pour vous aider à passer à MongoDB plus tard si nécessaire (je ne l'ai pas encore essayé, cependant).

Ajoutons donc NeDB au projet :

```bash
$ npm install nedb --save
```

et ajoutons à server.js quelques lignes pour configurer la base de données et nous assurer que nous pouvons y sauvegarder :

```js
// server.js

// DÉPENDANCES ET CONFIGURATION
// ===============================================

var express = require('express'),
  app = express(),
  port = Number(process.env.PORT || 8080);

// BASE DE DONNÉES
// ===============================================

// Configurer la base de données.
var Datastore = require('nedb');
var db = new Datastore({
  filename: 'goals.db', // fournir un chemin vers le fichier de la base de données 
  autoload: true, // charger automatiquement la base de données
  timestampData: true // ajouter et gérer automatiquement les champs createdAt et updatedAt
});

// Vérifions que nous pouvons sauvegarder dans la base de données.
// Définir un objectif.
var goal = {
  description: 'Faire 10 minutes de méditation chaque jour',
};

// Sauvegarder cet objectif dans la base de données.
db.insert(goal, function(err, newGoal) {
  if (err) console.log(err);
  console.log(newGoal);
});

// ROUTES
// ===============================================

// Définir la route de la page d'accueil.
app.get('/', function(req, res) {
  res.send('Notre première route fonctionne. :)');
});

// DÉMARRER LE SERVEUR
// ===============================================

app.listen(port, function() {
  console.log('Écoute sur le port ' + port);
});
```

Un **Datastore** fait référence à ce qui serait appelé une collection dans Mongo. Nous pourrions créer plusieurs datastores si nous avions besoin de plusieurs collections. Comme démontré dans la documentation de NeDB, chaque collection serait sauvegardée dans un fichier séparé. Ici, nous avons choisi de stocker la collection des objectifs dans un fichier nommé goals.db.

#### Vérification si cela a fonctionné

Si le serveur a été démarré plus tôt avec nodemon, il devrait avoir été mis à jour après que les changements dans server.js aient été sauvegardés. Cela signifie que db.insert(...) devrait avoir été exécuté et l'objectif devrait avoir été enregistré dans la console :

```
$ nodemon server.js
[nodemon] 1.9.1
[nodemon] pour redémarrer à tout moment, entrez `rs`
[nodemon] surveillance : *.*
[nodemon] démarrage de `node server.js`
Écoute sur le port 8080
[nodemon] redémarrage dû aux changements...
[nodemon] démarrage de `node server.js`
Écoute sur le port 8080
{ description: 'Faire 10 minutes de méditation chaque jour',
 successes: [],
 failures: [],
 _id: 'ScfixKjsOqz9xBo5',
 createdAt: Fri Mar 18 2016 22:10:58 GMT+0000 (UTC),
 updatedAt: Fri Mar 18 2016 22:10:58 GMT+0000 (UTC) }
```

Un nouveau fichier appelé goals.db devrait également avoir été créé.

```
$ ls 
goals.db  node_modules/  package.json  server.js
```

Et il devrait contenir l'objectif qui vient d'être sauvegardé.

```
$ less goals.db
{"description":"Faire 10 minutes de méditation chaque jour","_id":"ScfixKjsOqz9xBo5","createdAt":{"$$date":1458339058282},"updatedAt":{"$$date":1458339058282}}
```

Notez que les champs **__id**, **_createdAt_** et **_updatedAt_** ont été remplis automatiquement par NeDB parce que nous avons configuré le Datastore avec l'option **_timestampData_** définie sur _true_.

### 4. Construction d'une API RESTful

Ensuite, construisons une API RESTful pour l'application. En un mot, cela signifie que nous voulons utiliser des **verbes HTTP** et des URIs afin de permettre au client d'effectuer des opérations [**CRUD**](http://fr.wikipedia.org/wiki/Create,_read,_update_and_delete) (Create, Read, Update et Delete). Ces opérations vont également généralement renvoyer des données au client.

En termes de CRUD, nous pouvons :

* **Créer** des données avec **POST**,
* **Lire** des données avec **GET**,
* **Mettre à jour** des données avec [**PUT** ou **PATCH**](http://williamdurand.fr/2014/02/14/please-do-not-patch-like-an-idiot/),
* **Supprimer** des données avec **DELETE**.

Les verbes HTTP que nous allons utiliser dans cet article sont POST, GET et DELETE.

#### Notre API

Voici un tableau montrant les routes que nous allons configurer, comment elles seront accessibles (c'est-à-dire avec quel verbe HTTP) et ce que chacune permet :

![Image](https://cdn-media-1.freecodecamp.org/images/1*8KehmekfVxgjtJerJhVbIg.png)

Si vous souhaitez en savoir plus sur les API RESTful, vous pourriez consulter [_Concevoir une API Web RESTful_](https://scotch.io/bar-talk/designing-a-restful-web-api) par Mathias Hansen ou [_Utiliser les méthodes HTTP pour les services RESTful_](http://www.restapitutorial.com/lessons/httpmethods.html).

#### Test de l'API

Nous allons tester l'API manuellement dans le terminal en utilisant [curl](https://github.com/curl/curl). Si vous n'êtes pas sur Android et que vous préféreriez utiliser une interface graphique pour tester l'API, vous pourriez utiliser [POSTMAN](https://www.getpostman.com/).

Voyons un premier exemple de l'utilisation de curl. Assurez-vous que le serveur est en cours d'exécution, ouvrez un autre terminal (dans Termux, balayez vers la droite depuis la bordure gauche et cliquez sur _nouvelle session_) et tapez :

```bash
$ curl -X GET "http://localhost:8080"
```

Cela devrait imprimer dans la console ce que nous avons obtenu dans la fenêtre du navigateur plus tôt, c'est-à-dire : Notre première route fonctionne. :)

Nous allons maintenant ajouter du code à server.js petit à petit. Au cas où vous préféreriez voir le tableau d'ensemble en premier, vous pouvez vous rendre sur [le fichier server.js final](https://gist.github.com/aurerua/6679d82cc9939247ffa7).

#### Body-parser

Pour gérer les requêtes que le serveur reçoit, nous allons installer [body-parser](https://github.com/expressjs/body-parser). Il traite les requêtes entrantes et facilite l'accès aux parties pertinentes.

```bash
npm install body-parser --save
```

Ajoutez le code de configuration de body-parser en haut de server.js (par exemple, juste après la configuration du numéro de port) :

```js
var  bodyParser = require('body-parser'), // Middleware pour lire les données POST

// Configurer body-parser.
// Pour analyser JSON :
app.use(bodyParser.json());
// Pour analyser les données de formulaire :
app.use(bodyParser.urlencoded({
  extended: true
}));
```

#### Obtenir tous les objectifs

```js
// GET tous les objectifs.
// (Accessible à GET http://localhost:8080/goals)
app.get('/goals', function(req, res) {
  db.find({}).sort({
    updatedAt: -1
  }).exec(function(err, goals) {
    if (err) res.send(err);
    res.json(goals);
  });
});
```

Si le serveur reçoit une requête **GET** à **_/goals_**, le rappel sera exécuté et la base de données sera interrogée avec **_db.find({})_**. Ici, l'objet passé à _find()_ est vide. Cela signifie qu'aucune contrainte n'est définie sur ce que nous recherchons et tous les objets de la base de données doivent être retournés.

Remarquez également qu'aucun rappel n'a été spécifié à _find()_. Ainsi, un objet Curseur est retourné, qui peut d'abord être modifié avec **sort**, **skip** ou **limit** avant que nous utilisions **_exec(callback)_** pour terminer la requête. Ici, nous utilisons **sort** pour retourner les objectifs avec les plus récemment mis à jour en haut (c'est-à-dire ceux avec la date de dernière mise à jour la plus 'grande').

Si tout s'est bien passé, le résultat de la requête (dans notre cas, un tableau d'objectifs) est renvoyé au client formaté en JSON. En cas de problème et si une erreur est produite, le message d'erreur est renvoyé au client à la place.

Testons si cela fonctionne :

```bash
$ curl -X GET "http://localhost:8080/goals/"
```

Cela devrait imprimer dans la console un tableau contenant l'objectif que nous avons sauvegardé dans la base de données plus tôt.

#### Créer un objectif

```js
// POST un nouvel objectif.
// (Accessible à POST http://localhost:8080/goals)
app.post('/goals', function(req, res) {
  var goal = {
    description: req.body.description,
  };
  db.insert(goal, function(err, goal) {
    if (err) res.send(err);
    res.json(goal);
  });
});
```

**_req.body_** contient des paires clé-valeur de données qui ont été soumises dans le corps de la requête. Par défaut, il est indéfini et il est peuplé par le middleware [_body-parser_](https://www.npmjs.org/package/body-parser). Dans notre cas, la requête doit contenir une paire clé-valeur dont la clé est nommée 'description' et dont la valeur est ainsi récupérée en utilisant **_req.body.description_**.

Ainsi, l'objectif que nous voulons insérer dans la base de données est construit à partir de la requête en utilisant _req.body.description_. Ensuite, il peut être inséré dans la base de données et si aucune erreur n'est survenue, la réponse est renvoyée au serveur en JSON.

Essayons maintenant de POSTer un nouvel objectif en utilisant curl :

```bash
$ curl -X POST -H "Content-Type: application/x-www-form-urlencoded" -d "description=Lire sur la programmation fonctionnelle chaque jour" "http://localhost:8080/goals/"
```

Cela devrait imprimer la représentation JSON de l'objectif qui a été renvoyé au client.

Nous postons les données en tant que _x-www-form-urlencoded_. Cela envoie les données sous forme de chaînes de requête qui sont analysées par le _body-parser_.

#### Obtenir un objectif en utilisant son id

```js
// GET un objectif.
// (Accessible à GET http://localhost:8080/goals/goal_id)
app.get('/goals/:id', function(req, res) {
  var goal_id = req.params.id;
  db.findOne({
    _id: goal_id
  }, {}, function(err, goal) {
    if (err) res.send(err);
    res.json(goal);
  });
});
```

**_req.params_** est un objet contenant des propriétés mappées aux paramètres de la route. Ici, il nous permet d'accéder à la valeur de l'id de l'objectif, qui est censé venir après _/goals/_ dans l'URL de la requête. Pour que cela fonctionne, nous devons utiliser un deux-points dans l'URI devant la propriété à laquelle nous voulons accéder avec _req.params_.

À part le fait que nous utilisons _findOne(...)_ au lieu de _find(...)_, rien de nouveau ici. Alors testons-le. Pour cela, vous pourriez vérifier ce qui a été imprimé dans la console après avoir sauvegardé un nouvel objectif en utilisant POST et utiliser sa valeur "_id". Voici ma commande avec l'id que j'ai obtenu :

```bash
$ curl -X GET "http://localhost:8080/goals/JJtcFVQnoAxW7KXc"
```

Cela devrait imprimer dans la console l'objectif avec l'id donné.

#### Supprimer un objectif en utilisant son id

```js
// DELETE un objectif.
// (Accessible à DELETE http://localhost:8080/goals/goal_id)
app.delete('/goals/:id', function(req, res) {
  var goal_id = req.params.id;
  db.remove({
    _id: goal_id
  }, {}, function(err, goal) {
    if (err) res.send(err);
    res.sendStatus(200);
  });
});
```

Nous utilisons _remove(...)_ pour supprimer un objectif de la base de données. Si la suppression est réussie, la réponse est envoyée avec le code d'état HTTP 200 ([200 signifie que la suppression a réussi](http://www.restapitutorial.com/lessons/httpmethods.html)).

### Conclusion

Nous avons configuré un serveur avec Express et NeDB, et construit une API REST. Ce qui nous manque encore, c'est un front-end et un peu de câblage.

Cette prochaine étape pourrait nous mener sur de nombreuses routes différentes : opterions-nous pour un moteur de template et si oui, lequel ? Bootstrap ou un framework similaire ? Angular, React, Aurelia ? La liste est sans fin.

Au cas où vous aimeriez jeter un coup d'œil à une implémentation minimale d'un front-end — et peut-être jouer avec dans votre navigateur — vous pouvez voir le code d'une solution possible que j'ai implémentée en utilisant [Handlebars](http://handlebarsjs.com/), [Material Design Lite](https://www.getmdl.io/) et l'API [fetch](https://developers.google.com/web/updates/2015/03/introduction-to-fetch) en visitant [son dépôt sur GitHub](https://github.com/aurerua/goals-tracker.git) ou en le clonant :

```bash
$ git clone --branch rest-and-view https://github.com/aurerua/goals-tracker.git --depth 1
```

#### Aller plus loin

Le back-end que nous avons construit soulève encore la question : comment le code doit-il être divisé en différents fichiers et dossiers pour une meilleure modularité et maintenabilité ?

Au cas où vous seriez curieux, j'ai également écrit [une autre version de l'application](https://github.com/aurerua/goals-tracker-mvc.git) qui utilise une structure de dossiers Modèle-Vue-Contrôleur. N'hésitez pas à y jeter un coup d'œil :

```bash
$ git clone https://github.com/aurerua/goals-tracker-mvc.git
```

Et si vous avez des questions ou des commentaires, n'hésitez pas à me contacter !