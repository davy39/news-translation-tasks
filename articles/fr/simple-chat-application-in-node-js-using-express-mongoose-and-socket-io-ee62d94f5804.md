---
title: Comment créer une application de chat en temps réel en Node.js en utilisant
  Express, Mongoose et Socket.io
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-30T12:51:38.000Z'
originalURL: https://freecodecamp.org/news/simple-chat-application-in-node-js-using-express-mongoose-and-socket-io-ee62d94f5804
coverImage: https://cdn-media-1.freecodecamp.org/images/1*c4mV8Ppc8oe42XVQHfsjQw.png
tags:
- name: Express.js
  slug: expressjs
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Tutorial
  slug: tutorial
seo_title: Comment créer une application de chat en temps réel en Node.js en utilisant
  Express, Mongoose et Socket.io
seo_desc: 'By Arun Mathew Kurian

  In this tutorial, we will use the Node.js platform to build a real time chat application
  that sends and shows messages to a recipient instantly without any page refresh.
  We will use the JavaScript framework Express.js and the li...'
---

Par Arun Mathew Kurian

Dans ce tutoriel, nous allons utiliser la plateforme Node.js pour construire une **application de chat en temps réel** qui envoie et affiche les messages à un destinataire instantanément sans aucun rafraîchissement de page. Nous allons utiliser le framework JavaScript Express.js et les bibliothèques Mongoose et Socket.io pour y parvenir.

Avant de commencer, jetons un rapide coup d'œil aux bases de Node.js

### **Node.js**

[Node.js](https://en.wikipedia.org/wiki/Node.js) est un environnement d'exécution JavaScript open-source et multiplateforme qui exécute du code JavaScript en dehors du navigateur. Le principal avantage de l'utilisation de Node est que nous pouvons utiliser JavaScript à la fois comme langage front-end et back-end.

Comme nous le savons, JavaScript était principalement utilisé pour le scripting côté client, dans lequel les scripts étaient intégrés dans le HTML d'une page web et exécutés côté client par un moteur JavaScript dans le navigateur web de l'utilisateur.

Node.js permet aux développeurs d'utiliser JavaScript pour écrire des outils en ligne de commande et pour le scripting côté serveur — exécuter des scripts côté serveur pour produire du contenu de page web dynamique avant que la page ne soit envoyée au navigateur web de l'utilisateur.

Pour installer Node :

[https://nodejs.org/en/download](https://nodejs.org/en/download/)/

Même si Node est monothread, il est encore plus rapide d'utiliser des fonctions asynchrones. Par exemple, Node peut traiter d'autres choses pendant qu'un fichier est lu depuis le disque, ou en attendant qu'une requête HTTP se termine. Le comportement asynchrone peut être implémenté en utilisant des callbacks. De plus, JavaScript fonctionne bien avec JSON et les bases de données No-SQL.

#### **Modules NPM**

Node.js permet d'inclure les modules de bibliothèques dans l'application. Ces modules peuvent être définis par l'utilisateur ou des modules tiers.

Les modules tiers peuvent être installés en utilisant la commande suivante :

```bash
npm install module_name
```

et les modules installés peuvent être utilisés en utilisant la fonction **require()** :

```js
var module = require('module_name')
```

Dans les applications Node, nous utiliserons un fichier package.json pour maintenir les versions des modules. Ce fichier peut être créé par cette commande :

```bash
npm init
```

et les packages doivent être installés comme suit :

```bash
npm install -s module_name
```

Il existe de nombreux frameworks qui peuvent être ajoutés en tant que modules à notre application Node. Ceux-ci seront expliqués plus loin selon les besoins.

### **Application de chat simple**

L'application doit permettre à plusieurs utilisateurs de discuter ensemble. Les messages doivent être mis à jour sans rafraîchir la page. Pour simplifier, nous éviterons la partie authentification.

Nous pouvons commencer par créer un nouveau répertoire de projet et nous y déplacer. Ensuite, nous pouvons initier notre projet avec la commande suivante :

```bash
npm init
```

Cela nous invitera à entrer les détails de notre projet.

Après cela, un fichier **package.json** sera créé :

```json
{
 "name": "test",
 "version": "1.0.0",
 "description": "",
 "main": "index.js",
 "scripts": {
 "test": "echo \"Error: no test specified\" && exit 1"
 },
 "author": "",
 "license": "ISC"
}
```

Notre répertoire d'application est maintenant configuré.

La première chose dont nous avons besoin est de créer un serveur. Pour cela, nous allons utiliser un framework nommé **Express.**

#### **Express.js**

Express.js, ou simplement Express, est un framework d'application web pour Node.js. Express [fournit un ensemble robuste de fonctionnalités pour les applications web et mobiles](https://expressjs.com/). Express fournit une couche mince de fonctionnalités fondamentales d'application web, sans obscurcir les fonctionnalités de Node.js.

Nous allons installer Express.js en utilisant la commande suivante :

```bash
npm install -s express
```

À l'intérieur du fichier package.json, une nouvelle ligne sera ajoutée :

```json
dependencies": {
 "express": "^4.16.3"
 }
```

Ensuite, nous allons créer un fichier **server.js**.

Dans ce fichier, nous devons inclure Express et créer une référence à une variable à partir d'une instance d'Express. Les contenus statiques comme HTML, CSS ou JavaScript peuvent être servis en utilisant express.js :

```
var express = require('express');

var app = express();
```

et nous pouvons commencer à écouter un port en utilisant le code :

```js
var server = app.listen(3000, () => {
 console.log('server is running on port', server.address().port);
});
```

Maintenant, nous devons créer un fichier HTML index.html qui affiche notre interface utilisateur. J'ai ajouté les CDN de Bootstrap et JQuery.

```html
//index.html

<!DOCTYPE html>
<html>
<head>
 <! — include bootstrap and jquery cdn →
</head>
<body>
<div class="container">
 <br>
 <div class="jumbotron">
 <h1 class="display-4">Envoyer un message</h1>
 <br>
 <input id = "name" class="form-control" placeholder="Nom">
 <br>
 <textarea id = "message" class="form-control" placeholder="Votre message ici">
</textarea>
 <br>
 <button id="send" class="btn btn-success">Envoyer</button>
 </div>
 <div id="messages">
 
</div>
</div>
<script>

</script>
</body>
</html>
```

Veuillez noter que la balise _<script> </script>_ vide sera l'endroit où nous écrirons le code JavaScript côté client.

Pour indiquer à Express que nous allons utiliser un fichier statique, nous ajouterons une nouvelle ligne dans **server.js** :

```js
app.use(express.static(__dirname));
```

Nous pouvons exécuter le fichier server.js en utilisant la commande

```bash
node ./server.js
```

ou un package appelé **nodemon**, afin que les modifications apportées au code soient automatiquement détectées. Nous téléchargerons nodemon en utilisant la commande

```bash
npm install -g nodemon
```

-g — global, afin qu'il soit accessible dans tous les projets.

Nous exécuterons le code en utilisant la commande

```bash
nodemon ./server.js
```

Si vous allez sur localhost:3000, nous pouvons voir le fichier index :

![Image](https://cdn-media-1.freecodecamp.org/images/caxmtV7tYzJ1EUU69TeX4YQVsC69EhgzcSL5)
_index.html_

Maintenant que notre serveur est opérationnel, nous devons créer notre base de données. Pour cette application, nous aurons une base de données No-SQL et nous utiliserons **Mongodb**. Je configure mon mongodb sur [**mlab.com**](https://mlab.com/). Notre base de données contiendra une seule collection appelée **messages** avec les champs **name** et **message.**

![Image](https://cdn-media-1.freecodecamp.org/images/UWJYcDmpxrFhUoKRCrgkhtaTcBD4z4NivreC)

Pour connecter cette base de données à l'application, nous utiliserons un autre package appelé **Mongoose.**

#### **Mongoose**

Mongoose est un outil de modélisation d'objets MongoDB conçu pour fonctionner dans un environnement asynchrone. Mongoose peut être installé en utilisant la commande

```bash
npm install -s mongoose
```

À l'intérieur de **server.js**, nous allons inclure mongoose :

```js
var mongoose = require('mongoose');
```

Et nous allons assigner une variable, l'URL de notre base de données mlab :

```js
var dbUrl = 'mongodb://username:pass@ds257981.mlab.com:57981/simple-chat'
```

Mongoose se connectera à la base de données mlab avec la méthode connect :

```js
mongoose.connect(dbUrl , (err) => { 
   console.log('mongodb connected',err);
})
```

Et nous allons définir notre modèle de message comme

```js
var Message = mongoose.model('Message',{ name : String, message : String})
```

Nous pouvons implémenter la logique de chat maintenant. Mais avant cela, il y a un autre package qui doit être ajouté.

#### **Body-Parser**

Body-Parser extrait la totalité de la partie corps d'un flux de requête entrant et l'expose sur req.body. Le middleware faisait partie d'Express.js auparavant, mais maintenant vous devez l'installer séparément.

Installez-le en utilisant la commande suivante :

```bash
npm install -s body-parser
```

Ajoutez les codes suivants à **server.js** :

```js
var bodyParser = require('body-parser')
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: false}))
```

#### **Routing**

Le routage fait référence à la manière dont les endpoints d'une application (URIs) répondent aux requêtes des clients. Vous définissez le routage en utilisant des méthodes de l'objet d'application Express qui correspondent aux méthodes HTTP : app.get() pour gérer les requêtes GET et app.post() pour gérer les requêtes POST.

Ces méthodes de routage [spécifient une fonction de rappel](https://expressjs.com/en/guide/routing.html) (parfois appelée « fonctions de gestion ») appelée lorsque l'application reçoit une requête vers la route (endpoint) et la méthode HTTP spécifiées. En d'autres termes, l'application « écoute » les requêtes qui correspondent aux routes et méthodes spécifiées, et lorsqu'elle détecte une correspondance, elle appelle la fonction de rappel spécifiée.

Maintenant, nous devons créer deux routes pour les messages afin que notre chat fonctionne.

À l'intérieur de **server.js** :

**get :** récupérera tous les messages de la base de données

```js
app.get('/messages', (req, res) => {
  Message.find({},(err, messages)=> {
    res.send(messages);
  })
})
```

**post :** publiera de nouveaux messages créés par l'utilisateur dans la base de données

```js
app.post('/messages', (req, res) => {
  var message = new Message(req.body);
  message.save((err) =>{
    if(err)
      sendStatus(500);
    res.sendStatus(200);
  })
})
```

Afin de connecter ces routes au front-end, nous devons ajouter le code suivant dans la balise de script côté client dans le fichier **index.html** :

```js
$(() => {
    $("#send").click(()=>{
       sendMessage({
          name: $("#name").val(), 
          message:$("#message").val()});
        })
      getMessages()
    })
    
function addMessages(message){
   $(#messages).append(`
      <h4> ${message.name} </h4>
      <p>  ${message.message} </p>`)
   }
   
function getMessages(){
  $.get('http://localhost:3000/messages', (data) => {
   data.forEach(addMessages);
   })
 }
 
function sendMessage(message){
   $.post('http://localhost:3000/messages', message)
 }
```

Ici, **sendMessage** est utilisé pour invoquer la route post des messages et sauvegarder un message envoyé par l'utilisateur. Le message est créé lorsqu'un utilisateur clique sur le bouton d'envoi.

De même, **getMessage** est utilisé pour invoquer la route get des messages. Cela récupérera tous les messages sauvegardés dans la base de données et les ajoutera à la div des messages.

![Image](https://cdn-media-1.freecodecamp.org/images/m1tJ6aV53XnmvkU8PjY7u16wkI1gKrplYWHo)

Le seul problème maintenant est qu'il n'y a aucun moyen pour le client de savoir si le serveur est mis à jour. Donc, chaque fois que nous publions un message, nous devons rafraîchir la page pour voir les nouveaux messages.

Pour résoudre ce problème, nous pouvons ajouter un système de notification push qui enverra des messages du serveur au client. Dans Node.js, nous utilisons **socket.io.**

#### **Socket.io**

Socket.IO est une bibliothèque JavaScript pour les applications web en temps réel. [Elle permet une communication en temps réel et bidirectionnelle entre les clients web et le serveur](https://www.tutorialspoint.com/socket.io/socket.io_overview.htm). Elle se compose de deux parties : une bibliothèque côté client qui s'exécute dans le navigateur, et une bibliothèque côté serveur pour Node.js. Socket.io permet une communication bidirectionnelle en temps réel basée sur des événements.

Pour installer socket.io :

```bash
npm install -s socket.io
```

nous avons également besoin d'un package HTTP pour que Socket.io fonctionne :

```bash
npm install -s http
```

Ajoutez le code suivant à **server.js** :

```js
var http = require('http').Server(app);
var io = require('socket.io')(http);
```

Et nous pouvons créer une connexion :

```js
io.on('connection', () =>{
 console.log('un utilisateur est connecté')
})
```

Dans le fichier **index.html**, ajoutez la balise suivante :

```html
<script src="/socket.io/socket.io.js"></script>
```

Maintenant, nous devons créer une action d'émission lorsqu'un message est créé dans **server.js**. Donc, la route post devient celle-ci :

```js
app.post('/messages', (req, res) => {
  var message = new Message(req.body);
  message.save((err) =>{
    if(err)
      sendStatus(500);
    io.emit('message', req.body);
    res.sendStatus(200);
  })
})
```

Et dans la balise de script côté client dans **index.html**, ajoutez le code suivant :

```html
var socket = io();

socket.on('message', addMessages)
```

Ainsi, chaque fois qu'un message est publié, le serveur mettra à jour les messages dans la div des messages.

![Image](https://cdn-media-1.freecodecamp.org/images/6KUYtaL4L3ShtPNaHRKWXvP6v3mMuUAdq6R0)

Super !!

Ceci est une application très basique que nous pouvons créer en Node.js. Il y a beaucoup de place pour l'amélioration. Le code final peut être trouvé sur [https://github.com/amkurian/simple-chat](https://github.com/amkurian/simple-chat)

**server.js**

```js
var express = require('express');
var bodyParser = require('body-parser')
var app = express();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var mongoose = require('mongoose');

app.use(express.static(__dirname));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: false}))

var Message = mongoose.model('Message',{
  name : String,
  message : String
})

var dbUrl = 'mongodb://username:password@ds257981.mlab.com:57981/simple-chat'

app.get('/messages', (req, res) => {
  Message.find({},(err, messages)=> {
    res.send(messages);
  })
})

app.get('/messages', (req, res) => {
  Message.find({},(err, messages)=> {
    res.send(messages);
  })
})

app.post('/messages', (req, res) => {
  var message = new Message(req.body);
  message.save((err) =>{
    if(err)
      sendStatus(500);
    io.emit('message', req.body);
    res.sendStatus(200);
  })
})

io.on('connection', () =>{
  console.log('un utilisateur est connecté')
})

mongoose.connect(dbUrl ,{useMongoClient : true} ,(err) => {
  console.log('mongodb connected',err);
})

var server = http.listen(3001, () => {
  console.log('server is running on port', server.address().port);
});
```

J'espère que cela a été utile pour comprendre quelques concepts de base.

Quelques liens utiles

[**Socket.IO**](https://socket.io/)  
[_SOCKET.IO 2.0 IS HERE FEATURING THE FASTEST AND MOST RELIABLE REAL-TIME ENGINE ~/Projects/tweets/index.js var io =…_socket.io](https://socket.io/)[**Express - Node.js web application framework**](https://expressjs.com/)  
[_Express is a minimal and flexible Node.js web application framework that provides a robust set of features for web and…_expressjs.com](https://expressjs.com/)

[http://mongoosejs.com/](http://mongoosejs.com/)