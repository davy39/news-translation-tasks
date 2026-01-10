---
title: Comment créer votre propre application de chat en temps réel
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-11-16T06:37:31.000Z'
originalURL: https://freecodecamp.org/news/building-a-chat-application-with-mean-stack-637254d1136d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*q9WivDkg8ALSxw1jG1y1Jw.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: Comment créer votre propre application de chat en temps réel
seo_desc: 'By Sudheesh Shetty

  Messaging apps are surging in popularity. The past few years have brought apps like
  WhatsApp, Telegram, Signal, and Line.

  People seem to prefer chat-based applications because they allow for real-time interaction.
  They also add a p...'
---

Par Sudheesh Shetty

Les applications de messagerie sont de plus en plus populaires. Les dernières années ont vu l'émergence d'applications comme WhatsApp, Telegram, Signal et Line.

Les gens semblent préférer les applications basées sur le chat car elles permettent une interaction en temps réel. Elles ajoutent également une touche personnelle à l'expérience.

J'ai récemment assisté à un atelier organisé par le Free Software Movement Karnataka à Bangalore où j'ai encadré un groupe d'étudiants.

Lors des interactions, j'ai observé certaines choses :

1. Malgré l'encouragement des étudiants à interagir avec le mentor, la communication était toujours à sens unique.
2. Les étudiants étaient souvent trop timides pour poser des questions pendant les sessions.
3. Ils étaient plus à l'aise pour poser des questions et obtenir des retours dans des conversations en tête-à-tête.

Nous avons donc dû trouver une solution pour briser la glace entre les mentors et les étudiants. Une application de chat locale s'est avérée utile dans cette situation. Les gens aiment être anonymes, ce qui leur donne plus de pouvoir pour s'exprimer et poser des questions à tout moment et n'importe où. C'est la même philosophie utilisée par la plupart des forums populaires sur Internet, comme Reddit et 4chan. Ce ne sont que quelques exemples géants d'applications semi-anonymes.

J'ai donc commencé à réfléchir à cette idée. J'ai établi certaines des exigences et fonctionnalités de base.

1. Les utilisateurs s'inscrivent en donnant un pseudonyme, qui est unique pour chaque utilisateur (un nom fictif). Seul le pseudonyme sera révélé aux autres utilisateurs. Ainsi, les gens sont libres de choisir n'importe quel pseudonyme et restent donc anonymes.
2. Un membre peut voir les autres membres qui sont en ligne. Ils ont une option pour passer en public, ce qui diffuse le message à tous les membres en ligne dans le chat.
3. Pour les messages privés, l'expéditeur doit d'abord envoyer une demande à l'autre membre. Les autres membres, en acceptant la demande, peuvent avoir une conversation privée avec eux.

### **Technologie, Outils utilisés**

1. Pile MEAN (Mongo, Express, Angular, Node).
2. Sockets pour permettre la communication en tête-à-tête en temps réel
3. AJAX pour l'inscription et la connexion

### **Comment créer une simple application de chat ?**

Dans ce tutoriel, je vais vous aider à créer votre propre application de chat. Vous pourrez ensuite l'intégrer en tant que widget dans n'importe quel projet ! Ce tutoriel ne se concentrera pas sur le développement complet d'une application de chat. Mais il vous aidera à en construire une.

**Prérequis :** Vous devez connaître quelques bases de la pile MEAN, car nous l'utilisons pour en construire une.

Tout d'abord, créez une structure de répertoires comme ceci.

![Image](https://cdn-media-1.freecodecamp.org/images/aholQChXQkfdRI26smzgqaGHiw0Ak82Yg7Gx)
_**Structure des répertoires du projet**_

Installez [Node.js](https://nodejs.org/en/download/package-manager/) et [MongoDB](https://docs.mongodb.com/manual/administration/install-community/).

Nous utiliserons AngularJS 1 pour ce tutoriel. Téléchargez la bibliothèque AngularJS depuis [ici](https://angularjs.org/) et copiez-la dans le dossier lib du répertoire Client.

Si vous souhaitez embellir l'application, vous pouvez télécharger n'importe quelle bibliothèque CSS et les copier également dans lib.

### **Construction du Serveur**

**Étape 1** — Démarrer le projet :

Allez dans le répertoire Server et exécutez cette commande :

```
npm init
```

Cela démarrera un nouveau projet. Fournissez tous les détails requis. Le fichier _package.json_ sera créé et ressemblera à quelque chose comme ceci.

```json
{
  "name": "chat",
  "version": "1.0.0",
  "description": "Application de chat",
  "main": "server.js",
  "scripts": {
    "test": "echo \"Erreur : aucun test spécifié\" && exit 1"
  },
  "author": "Votre nom",
  "license": "ISC"
}
```

**Étape 2** — Installer les dépendances.

* **socket.io** — est une bibliothèque _javascript_ pour les applications web en temps réel. Elle permet une communication en temps réel et bidirectionnelle entre les clients web et les serveurs.
* **express** — est un framework d'application web _Node.js_. Il fournit un ensemble de fonctionnalités pour développer des applications web et mobiles. On peut répondre à une requête HTTP en utilisant différents middlewares et également rendre des pages HTML.

```
npm install --save socket.io
npm install --save express
```

Cela installera les dépendances requises et les ajoutera à _package.json_. Un champ supplémentaire sera ajouté à _package.json_ qui ressemblera à ceci :

```json
"dependencies": {
    "express": "^4.14.0",
    "socket.io": "^1.4.8"
  }
```

**Étape 3 —** Création du Serveur

Créez un serveur qui écoute sur le port 3000 et qui enverra le html lorsqu'il sera appelé.

Initialisez une nouvelle connexion socket en passant l'objet HTTP.

L'événement _connection_ écoutera les sockets entrants.

Chaque socket émet un événement _disconnect_ qui sera appelé chaque fois qu'un client se déconnecte.

* **socket.on** attend l'événement. Chaque fois que cet événement est déclenché, la fonction de rappel est appelée.
* **io.emit** est utilisé pour émettre le message à tous les sockets qui y sont connectés.

La syntaxe est :

```js
socket.on('event', function(msg){})
io.emit('event', 'message')
```

Créez un serveur avec le nom _server.js_. Il doit :

* afficher un message sur la console lorsqu'un utilisateur se connecte
* écouter les événements _chat message_ et diffuser le message reçu à tous les sockets connectés.
* Chaque fois qu'un utilisateur se déconnecte, il doit afficher le message sur la console.

Le serveur ressemblera à quelque chose comme ceci :

```js
var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);

app.get('/', function(req, res){
  res.sendfile('index.html');
});

io.on('connection', function(socket){
  console.log('utilisateur connecté');
  socket.on('chat message', function(msg){
    io.emit('chat message', msg);
  });
  socket.on('disconnect', function(){
    console.log('utilisateur déconnecté');
  });
});

http.listen(3000, function(){
  console.log('écoute sur *:3000');
});
```

### **Construction du Client**

Créez le fichier index.html dans le répertoire client, style.css dans le répertoire css et app.js dans le répertoire js du client.

**_index.html:_**

Écrivons un simple HTML qui peut prendre notre message et également l'afficher.

Incluez _socket.io-client_ et _angular.js_ dans votre script HTML.

```html
<script src="/path/to/angular.js"></script>
<script src="/socket.io/socket.io.js"></script>
```

**socket.io** sert le client pour nous. Il se connecte par défaut à l'hôte qui sert la page. Le HTML final ressemble à quelque chose comme ceci :

```html
<!doctype html>
<html ng-app="myApp">
  <head>
    <title>Socket.IO chat</title>
    <link rel="stylesheet" href="/css/style.css">
    <script src="/lib/angular/angular.js"></script>
    <script src="/socket.io/socket.io.js"></script>
    <script src="http://code.jquery.com/jquery-1.11.1.js">
    </script>
    <script src="/js/app.js"></script>
  </head>
  <body ng-controller="mainController">
    <ul id="messages"></ul>
    <div>
      <input id="m" ng-model="message" autocomplete="off" />
      <button ng-click="send()">Envoyer</button>
    </div>
  </body>
</html>
```

**_css/style.css:_**

Donnez-lui un peu de style pour qu'il ressemble à une boîte de chat. Vous pouvez utiliser n'importe quelle bibliothèque.

```css
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font: 13px Helvetica, Arial; }
div { background: #000; padding: 3px; position: fixed; bottom: 0; width: 100%; }
div input { border: 0; padding: 10px; width: 90%; margin-right: .5%; }
div button { width: 9%; background: rgb(130, 224, 255); border: none; padding: 10px; }
#messages { list-style-type: none; margin: 0; padding: 0; }
#messages li { padding: 5px 10px; }
#messages li:nth-child(odd) { background: #eee; }
```

**_js/app.js:_**

Créez une application angular.js et initialisez une connexion socket.

* **socket.on** écoute un événement particulier. Il appelle une fonction de rappel chaque fois que cet événement est appelé.
* **socket.emit** est utilisé pour émettre le message à l'événement particulier.

La syntaxe de base des deux est :

```js
socket.on('nom de l'événement', function(msg){});
socket.emit('nom de l'événement', message);
```

Ainsi, chaque fois que le message est tapé et que le bouton est cliqué, appelez la fonction pour envoyer le message.

Chaque fois que le socket reçoit un message, affichez-le.

Le JavaScript ressemblera à quelque chose comme ceci :

```js
var app=angular.module('myApp',[]);

app.controller('mainController',['$scope',function($scope){
 var socket = io.connect();
 $scope.send = function(){
  socket.emit('chat message', $scope.message);
  $scope.message="";
 }
 socket.on('chat message', function(msg){
  var li=document.createElement("li");
  li.appendChild(document.createTextNode(msg));
  document.getElementById("messages").appendChild(li);
 });
}]);
```

### **Exécution de l'application**

Allez dans le répertoire serveur où se trouve notre serveur. Exécutez le serveur en utilisant la commande suivante :

```
node server.js
```

Le serveur commence à s'exécuter sur le port 3000. Allez dans le navigateur et tapez l'URL suivante :

```
http://localhost:3000
```

### **Comment améliorer la même application**

Vous pouvez concevoir une base de données pour sauvegarder les détails des utilisateurs et les messages. Il serait bon que la conception soit évolutive afin que vous puissiez ajouter plus de fonctionnalités plus tard.

Vous devez installer Mongoose ou un module MongoDB pour utiliser une base de données Mongo :

```
npm install --save mongoose
```

ou :

```
npm install --save mongodb
```

Voici la documentation pour utiliser [mongoose](http://mongoosejs.com/docs/index.html) et le module [mongodb](https://docs.mongodb.com/getting-started/node/client/).

Voici à quoi ressemble ma conception de schéma :

```json
{
 "_id" : ObjectId("5809171b71e640556be904ef"),
 "name" : "Sudheesh Shetty",
 "handle" : "sudheesh",
 "password" : "556624370",
 "phone" : "8888888888",
 "email" : "sudheeshshetty@gmail.com",
 "friends" : [
    {
      "name" : "abc",
      "status" : "Ami"
    },
    {
      "name" : "xyz",
      "status" : "Ami"
    }
 ],
 "__v" : 0
}
```

Ici, le statut de chaque membre peut être :

* Ami : Indique que le membre est un ami.
* En attente : Si le membre n'a pas encore accepté.
* Bloqué : Si le membre a bloqué l'autre membre.

Supposons que le membre a rejeté une demande de chat. L'expéditeur peut alors envoyer une nouvelle demande de chat. Un utilisateur peut également sauvegarder les messages en créant une collection supplémentaire. Chaque document contiendra le message, l'expéditeur, le destinataire et l'heure.

Concevez donc votre base de données en fonction de vos besoins spécifiques et de la manière dont vous souhaitez gérer les messages.

2. Créez des API REST pour servir le client. Par exemple, un endpoint qui envoie une page d'accueil, à partir de laquelle les utilisateurs peuvent faire d'autres demandes.

Quelques-uns de mes endpoints API sont :

```js
app.post('register',function(req,res){})

app.post('login',function(req,res){})

app.post('friend_request',function(req,res){})

app.post('friend_request/confirmed',function(req,res){})
```

3. Pensez à quelques fonctionnalités supplémentaires sympas et implémentez-les.

J'ai créé ma propre application de chat :

[**sudheeshshetty/Chat**](https://github.com/sudheeshshetty/Chat)  
[Contribuez au développement de Chat en créant un compte sur GitHub.github.com](https://github.com/sudheeshshetty/Chat)

Voici un aperçu rapide de mon application de chat :

![Image](https://cdn-media-1.freecodecamp.org/images/1-PmXr40QmsMiaRVejb1iS--qs3BqE2zINJE)
_Ecran de connexion_

![Image](https://cdn-media-1.freecodecamp.org/images/qQFOHwAEgl7k4DqVqRKVMlR1yd9c8T9I-388)
_À quoi cela ressemble après la connexion._

N'hésitez pas à la consulter et à lui donner une étoile en haut à droite si vous l'aimez. Il y a de nombreuses façons dont je pourrais améliorer cette application. Si vous avez des suggestions, envoyez-les-moi à sudheeshshetty@gmail.com.

Vous pouvez me suivre ici en cliquant sur le cœur vert si vous avez trouvé cela utile afin que plus de gens voient cela. Vous pouvez également [me suivre sur GitHub](https://github.com/sudheeshshetty) et [twitter](https://twitter.com/sudheeshshetty).