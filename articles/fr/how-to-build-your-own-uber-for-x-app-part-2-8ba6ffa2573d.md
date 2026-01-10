---
title: Comment construire votre propre application Uber-for-X (PARTIE 2)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-01-29T01:20:05.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-your-own-uber-for-x-app-part-2-8ba6ffa2573d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*WcHHixgDq7o5lN3biKIu9Q.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment construire votre propre application Uber-for-X (PARTIE 2)
seo_desc: 'By Ashwin Hariharan

  Featured in Mybridge’s Top Ten NodeJS articles from Jan-Feb 2017 and Top 50 NodeJS
  articles of the year (v.2018)



  Update: Read the updated version of this article on my tech blog.



  Welcome to part 2 of this series Building your ...'
---

Par Ashwin Hariharan

Présenté dans [Mybridge](https://medium.mybridge.co/) parmi les [Top Ten des articles NodeJS de janvier-février 2017](https://medium.mybridge.co/node-js-top-10-articles-for-the-past-month-v-feb-2017-9a9240c0db8c#.nq45mjr1cr) et les [Top 50 des articles NodeJS de l'année (v.2018)](https://medium.com/@Mybridge/learn-node-js-we-created-a-directory-of-top-articles-from-2017-783e809452dd)

*****
> **Mise à jour :** Lisez la version mise à jour de cet article sur mon [blog technique](https://www.ashwinhariharan.tech/blog/how-to-build-your-own-uber-for-x-app-part-2/).
*****

Bienvenue dans la partie 2 de cette série **_Construire votre propre application Uber-for-X_**. Dans la partie 1, vous avez utilisé un exemple d'application citoyen-policier et appris à récupérer les policiers situés près d'une paire donnée de coordonnées de latitude et de longitude. Dans cette partie, vous continuerez à construire la même application et apprendrez à implémenter ces fonctionnalités :

* Échanger des données entre policiers et citoyens en temps réel en utilisant des web sockets
* Utiliser des cartes pour montrer les détails de localisation du citoyen et du policier
* Visualiser les données de criminalité

Assurez-vous de [lire la partie 1](https://www.freecodecamp.org/news/how-to-build-your-own-uber-for-x-app-33237955e253/) attentivement et d'essayer les exemples avant de continuer avec le reste de ce tutoriel.

### Configuration du projet et organisation des dossiers

![Image](https://cdn-media-1.freecodecamp.org/images/1*9PB6fJhap7bJTGit3QHB2w.png)

Analysons les fichiers du projet que nous avons actuellement, de la partie précédente :

* _app.js_ contient la configuration de votre serveur et de votre base de données. Chaque fois que vous devez démarrer le serveur, vous utiliserez ce fichier en tapant _node app.js_ dans votre terminal.
* _routes.js_ — vous utiliserez ce fichier pour écrire des points de terminaison et des gestionnaires
* _db-operations_ — où vous écrirez les opérations de base de données
* _views_ contiendra vos pages HTML
* _public_ contiendra des sous-dossiers pour stocker les JavaScripts, les feuilles de style et les images

Si vous avez déjà utilisé Uber, vous savez qu'il y a l'application pour les conducteurs et l'application pour les passagers. Essayons d'implémenter la même chose — _citizen.html_ montrera le côté citoyen de l'application et _cop.html_ montrera l'application pour les policiers. Vous enregistrerez ces fichiers à l'intérieur du dossier _views_. Ouvrez _citizen.html_ dans votre éditeur de texte et ajoutez ceci :

```html
<!DOCTYPE html>
<html lang = "en">
<head>
    <meta charset="utf-8"/>
    <title>Citoyen <%= userId %> </title>
</head>
<body data-userId="<%= userId %>">
    <h1>Bonjour Citoyen <%= userId %></h1>
    <h4 id="notification"> 
        <!-- Certaines informations seront affichées ici-->
    </h4>
    <div id="map"> 
        <!-- Nous chargerons une carte ici plus tard-->
    </div>
    <!--Charger les JavaScripts -->
</body>
</html>
```

Répétez cette étape pour _cop.html_ également, mais remplacez le mot _Citizen_ par _Cop_.

L'attribut _data-userId_ est un attribut qui commence par le préfixe _data-_, que vous pouvez utiliser pour stocker certaines informations sous forme de chaînes, qui n'ont pas nécessairement besoin d'avoir une représentation visuelle. `<%= userId %>` peut sembler être une syntaxe étrange, mais ne vous inquiétez pas — votre moteur de template comprend que tout ce qui se trouve entre `_<%=_` et `%>` est une variable, et il substituera la variable _userId_ par la valeur réelle côté serveur avant que la page ne soit servie. Vous comprendrez mieux cela au fur et à mesure que vous avancerez.

Si vous vous souvenez de la partie précédente, vous aviez ces lignes dans _app.js :_

```js
app.set('views', 'views'); 
app.use(express.static('./public'));
app.set('view engine','html');
app.engine('html',consolidate.underscore);
```

La première ligne indique à votre application de rechercher des fichiers HTML à l'intérieur du dossier _views_ chaque fois qu'elle reçoit une demande pour une page particulière. La deuxième ligne définit le dossier à partir duquel les actifs statiques comme les feuilles de style et les JavaScripts seront servis lorsque la page se charge dans le navigateur. Les deux lignes suivantes indiquent à notre application d'utiliser le moteur de template _underscore_ pour analyser nos fichiers html.

Maintenant que la structure du répertoire est configurée et que les vues sont prêtes, il est temps de commencer à implémenter les fonctionnalités ! Avant de continuer, il sera utile de garder à l'esprit les points suivants :

* Écrivez le code JS à l'intérieur de la balise _script_ dans le document HTML. Vous pouvez choisir de l'écrire à l'intérieur d'un fichier _.js_, auquel cas vous devez enregistrer le(s) fichier(s) JS à l'intérieur du dossier _/public/js_ et le charger dans votre page. Assurez-vous de charger les bibliothèques et autres dépendances en premier !
* Il sera utile de garder la console de développement ouverte dans votre navigateur pour vérifier les messages d'erreur au cas où quelque chose ne semble pas fonctionner. Surveillez également la sortie du terminal.
* Les mots _événement_ et _signal_ seront utilisés de manière interchangeable dans ce tutoriel — les deux signifient la même chose.

Commençons à coder !

### Servir les pages Citoyen et Policier

Rendons la page citoyen en allant sur [_http://localhost:8000/citizen.html,_](http://localhost:8000/police.html,) et la page policier en allant sur [_http://localhost:8000/cop.html_](http://localhost:8000/police.html,). Pour ce faire, ouvrez _app.js_ et ajoutez ces lignes à l'intérieur de la fonction de rappel de _mongoClient.connect_ :

```js
app.get('/citizen.html', function(req, res){
    res.render('citizen.html',{
        userId: req.query.userId
    });
});

app.get('/cop.html', function(req, res){
    res.render('cop.html', {
        userId: req.query.userId
    });
});
```

Enregistrez vos fichiers, redémarrez votre serveur et chargez les pages citoyen et policier. Vous devriez voir **Bonjour Citoyen** sur la page. Si vous passez _userId_ en tant que paramètres de requête dans l'URL, par exemple — [_http://localhost:8000/citizen.html?userId=YOURNAME_](http://localhost:8000/citizen.html?userId=YOURNAME) alors vous verrez **Bonjour Citoyen YOURNAME**. C'est parce que votre moteur de template a substitué la variable _userId_ par la valeur que vous avez passée depuis les paramètres de requête, et a renvoyé la page.

### Pourquoi avez-vous besoin de web sockets, et comment fonctionnent-ils ?

La communication basée sur des événements ou des signaux a toujours été une manière intuitive de transmettre des messages depuis les temps historiques. Les premières techniques étaient assez rudimentaires — comme l'utilisation de signaux de feu à diverses fins, principalement pour avertir les gens d'un danger.

![Image](https://cdn-media-1.freecodecamp.org/images/1*7KB_Iw02iJiCPPWDlVl0kA.gif)

Au fil des siècles, de nouvelles et meilleures formes de communication ont émergé. L'avènement des ordinateurs et d'Internet a déclenché quelque chose de vraiment innovant — et avec le développement du modèle OSI, de la programmation de sockets et de la révolution des smartphones, la communication en tête-à-tête est devenue assez sophistiquée. Les principes de base restent les mêmes, mais maintenant beaucoup plus intéressants que de mettre le feu à quelque chose et de le jeter.

En utilisant les Sockets, vous pouvez envoyer et recevoir des informations via des _événements_, ou en d'autres termes des _signaux_. Il peut y avoir différents types de tels signaux, et si les parties impliquées savent quel type de signal « écouter », alors il peut y avoir un échange d'informations.

#### Mais pourquoi ne pas simplement utiliser des requêtes HTTP ?

J'ai lu un très bon article sur la [différence entre les requêtes HTTP et les web-sockets](https://www.pubnub.com/blog/2015-01-05-websockets-vs-rest-api-understanding-the-difference/). C'est un article court, donc vous pouvez le lire pour mieux comprendre le concept des web-sockets.

Mais en résumé, les requêtes HTTP traditionnelles comme GET et POST initient une nouvelle demande de connexion et ferment ensuite la connexion après que le serveur a renvoyé la réponse. Si vous deviez tenter de construire une application en temps réel en utilisant HTTP, le client devrait initier des requêtes à intervalles réguliers pour vérifier les nouvelles informations (qui peuvent ou non être disponibles). Cela est dû au fait que le serveur lui-même est incapable de « pousser » des informations de sa propre initiative.

Et cela est hautement inefficace — le client gaspillerait des ressources en interrompant constamment le serveur et en disant « Salut, je suis XYZ — serrons-nous la main. Avez-vous quelque chose de nouveau pour moi ? », et le serveur serait comme — « Salut (serrant la main). Non, je n'ai rien. Au revoir ! » encore et encore, ce qui signifie que même le serveur gaspille des ressources !

Les web-sockets, cependant, créent une connexion persistante entre un client et le serveur. Ainsi, le client n'a pas besoin de continuer à demander au serveur, le serveur peut « pousser » des informations lorsqu'il en a besoin. Cette méthode est beaucoup plus efficace pour construire des applications en temps réel.

Les [web-sockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) sont pris en charge dans tous les principaux navigateurs, mais pour les quelques navigateurs qui ne les prennent pas en charge, il existe d'autres options/techniques de repli sur lesquelles s'appuyer, comme le Long Polling. Ces techniques de repli et les API Web Sockets sont regroupées au sein de Socket.IO, donc vous n'auriez pas à vous soucier de la compatibilité des navigateurs. Voici une [excellente réponse](http://stackoverflow.com/a/12855533/3989925) sur Stack Overflow qui compare beaucoup de ces options.

### Intégration de Socket.IO

Commençons par intégrer Socket.io avec le serveur express et chargeons également la bibliothèque côté client de socket.io dans les pages html. Vous utiliserez également jQuery — ce n'est pas nécessaire pour que socket.io fonctionne, mais votre application en aura besoin pour faire des requêtes AJAX et plein d'autres choses. Alors, allez-y, écrivez ceci dans les deux pages :

```html
<!-- Charger la bibliothèque cliente socket.io -->
<script src="/socket.io/socket.io.js"></script>

<!-- Charger JQuery depuis un CDN -->
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>

<!-- charger les bibliothèques avant votre code JS
Écrivez le reste de votre code JS ici -->

<script type="text/javascript">
    var socket = io();
    
    //Récupérer userId depuis l'attribut data du body tag
    var userId = document.body.getAttribute("data-userId");
    
    /*Déclencher un événement 'join' et envoyer votre userId au serveur, pour rejoindre une salle - le nom de la salle sera le userId lui-même!
*/ 
    socket.emit('join', {userId: userId});
    
//Déclarer des variables, cela sera utilisé plus tard
    var requestDetails = {};
    var copDetails = {};
    var map, marker;
    
</script>
```

La première balise _script_ charge la bibliothèque cliente de Socket.IO (une fois que nous servons la page en utilisant le serveur socket.io), qui expose un objet global _io_. Votre application utilisera cet objet pour émettre des événements/signaux vers le serveur et écouter les événements en provenance du serveur.

Maintenant, vous devez modifier _app.js_ pour utiliser socket.io :

```js
var http = require("http");
var express = require("express");
var consolidate = require("consolidate"); //1
var _ = require("underscore");
var bodyParser = require('body-parser');

var routes = require('./routes'); //Fichier qui contient nos endpoints
var mongoClient = require("mongodb").MongoClient;

var app = express();
app.use(bodyParser.urlencoded({
    extended: true,
}));

app.use(bodyParser.json({
    limit: '5mb'
}));

app.set('views', 'views'); //Définir le nom du dossier à partir duquel vous servez la page html. 
app.use(express.static('./public')); //définir le nom du dossier (public) où tous les fichiers statiques comme css, js, images etc sont mis à disposition

app.set('view engine', 'html');
app.engine('html', consolidate.underscore); //Utiliser underscore pour analyser les templates lorsque nous faisons res.render

var server = http.Server(app);
var portNumber = 8000; //pour locahost:8000

var io = require('socket.io')(server); //Créer une nouvelle instance socket.io en passant l'objet serveur HTTP

server.listen(portNumber, function() { //Exécute le serveur sur le port 8000
    console.log('Serveur à l'écoute sur le port ' + portNumber);

    var url = 'mongodb://localhost:27017/myUberApp'; //Nom de la base de données
    mongoClient.connect(url, function(err, db) { //une connexion avec mongodb est établie ici.
        console.log("Connecté à la base de données");

        app.get('/citizen.html', function(req, res) { //une requête à /citizen.html rendra notre page citizen.html
            //Substituer la variable userId dans citizen.html avec la valeur userId extraite des paramètres de requête de la demande.
            res.render('citizen.html', {
                userId: req.query.userId
            });
        });

        app.get('/cop.html', function(req, res) {
            res.render('cop.html', {
                userId: req.query.userId
            });
        });

        io.on('connection', function(socket) { //Écouter l'événement 'connection' pour les sockets entrants
            console.log('Un utilisateur vient de se connecter');

            socket.on('join', function(data) { //Écouter tout événement de connexion des utilisateurs connectés
                socket.join(data.userId); //L'utilisateur rejoint une salle/chaîne unique nommée d'après l'userId 
                console.log("L'utilisateur a rejoint la salle : " + data.userId);
            });

            routes.initialize(app, db, socket, io); //Passer les objets socket et io que nous pourrions utiliser à différentes parties de notre application
        });
    });
});

/* 1. Tous les moteurs de template ne fonctionnent pas uniformément avec express, donc cette bibliothèque en js, (consolidate), est utilisée pour faire fonctionner les moteurs de template uniformément. Bien qu'elle n'ait aucun 
module propre et que tout moteur de template à utiliser doive être installé séparément!*/
```

Assurez-vous de modifier la fonction **_initialize_** dans _routes.js_ pour accepter **quatre** paramètres au lieu de deux, comme ceci — _function initialize(app, db, **socket**, **io**)_.

Si vous redémarrez le serveur et actualisez vos pages, vous verrez le message _Un utilisateur vient de se connecter_ dans votre terminal. Le serveur créera également une nouvelle salle une fois qu'il recevra un événement _join_ des clients connectés, donc vous verrez un autre message imprimé — _L'utilisateur a rejoint la salle._ Essayez avec [http://localhost:8000/cop.html?userId=02](http://localhost:8000/citizen.html?userId=tyrion), vous devriez obtenir une sortie similaire.

Parfait — maintenant que vous avez intégré socket.io, vous pouvez commencer à construire le reste de votre application.

### Communication citoyen-policier :

L'ensemble du processus peut être divisé en deux ensembles de fonctionnalités :

1. Demander de l'aide et notifier les policiers à proximité
2. Accepter la demande et notifier le citoyen

Essayons de comprendre comment implémenter chacune de ces fonctionnalités en détail.

#### Demander de l'aide et notifier les policiers à proximité :

![Image](https://cdn-media-1.freecodecamp.org/images/1*gjLDPhI-t_Qr4LDwIW7FwA.png)

* Tout d'abord, créez un point de terminaison _/cops/info_ à l'intérieur de _routes.js_, qui appellera une fonction pour récupérer les informations de profil d'un policier, et retournera les résultats sous forme de JSON au client —

```js
// Requête GET à '/cops/info?userId=02'
app.get('/cops/info', function(req, res){
    var userId = req.query.userId //extraire userId des paramètres de requête
    dbOperations.fetchCopDetails(db, userId, function(results){
        res.json({
            copDetails: results //retourner les résultats au client
        });
    });
});
```

* Ensuite, vous écrirez la fonction _fetchCopDetails_ dans _db-operations.js_, qui accepte une instance de _db_, l'_userId_ du policier et une fonction de rappel. Cette fonction utilisera la requête [_findOne_](https://docs.mongodb.com/v3.2/reference/method/db.collection.findOne/) de MongoDB pour récupérer les informations d'un policier avec un _userId_ donné à partir de la base de données, puis retournera le résultat au rappel :

```js
function fetchCopDetails(db, userId, callback) {
    db.collection("policeData").findOne({
        userId: userId
    }, function(err, results) {
        if (err) {
            console.log(err);
        } else {
            callback({
                copId: results.userId,
                displayName: results.displayName,
                phone: results.phone,
                location: results.location
            });
        }
    });
}
exports.fetchCopDetails = fetchCopDetails;
```

* **À l'intérieur de _cop.html_ :**

Maintenant que vous avez créé le point de terminaison, vous pouvez l'appeler en utilisant la fonction AJAX de JQuery pour récupérer les informations de profil du policier et les afficher à l'intérieur d'un _div id="copDetails"_ vide. Vous configurerez également la page du policier pour commencer à écouter les demandes d'aide :

```js
//Envoyer d'abord une requête GET en utilisant JQuery AJAX et obtenir les détails du policier et les enregistrer
$.ajax({
    url: "/cops/info?userId="+userId,
    type: "GET",
    dataType: "json",
    success: function(data){ //Une fois la réponse réussie
        copDetails = data.copDetails; //Enregistrer les détails du policier
        copDetails.location = {
            address: copDetails.location.address,
            longitude: copDetails.location.coordinates[0],
            latitude: copDetails.location.coordinates[1] 
        };
        document.getElementById("copDetails").innerHTML = JSON.stringify(data.copDetails);
    },
    error: function(httpRequest, status, error){
        console.log(error);
    }
});

//Écouter un événement "request-for-help"
socket.on("request-for-help", function(eventData){
    //Une fois la demande reçue, faire ceci:
    
    //Enregistrer les détails de la demande
    requestDetails = eventData; //Contient les informations du citoyen
    
    //afficher les données reçues de l'événement
    document.getElementById("notification").innerHTML = "Quelqu'un est attaqué par un sauvageon ! \n" + JSON.stringify(requestDetails);
});
```

Si vous redémarrez le serveur et allez sur [_http://localhost:8000/cop.html?userId=02_,](http://localhost:8000/cop.html?userId=02,) (en passant userId d'un policier enregistré dans les paramètres de requête) vous trouverez les informations du policier affichées sur la page. Votre page de policier a également commencé à écouter les événements _request-for-help_.

#### **À l'intérieur de _citizen.html_**

L'étape suivante consiste à créer un bouton pour le citoyen qui peut être cliqué en cas d'urgence. Une fois cliqué, il déclenchera un signal _request-for-help_ et le signal pourra renvoyer les informations du citoyen au serveur :

```html
<button onclick="requestForHelp()">
    Demander de l'aide
</button>
```

Écrivez le gestionnaire pour générer l'événement dans la balise _script_ :

```js
//Informations du citoyen
requestDetails = {
    citizenId: userId,
    location: {
        address: "Indiranagar, Bengaluru, Karnataka 560038, Inde",
        latitude: 12.9718915,
        longitude: 77.64115449999997
    }
}

//Lorsque le bouton est cliqué, déclencher request-for-help et envoyer l'userId et la localisation du citoyen
function requestForHelp(){
    socket.emit("request-for-help", requestDetails);
}
```

* Enfin, le serveur doit gérer cet événement, comme le montre l'illustration. Allez dans _db-operations.js_ et créez une nouvelle fonction qui peut être utilisée pour enregistrer les détails de la demande dans une nouvelle table _requestsData_ :

```js
//Enregistre des détails comme la localisation du citoyen, l'heure
function saveRequest(db, issueId, requestTime, location, citizenId, status, callback){

    db.collection('requestsData').insert({
        "_id": issueId,
        "requestTime": requestTime,
        "location": location,
        "citizenId": citizenId,
        "status": status
    }, function(err, results){
           if(err) {
               console.log(err);
           }else{
               callback(results);
           }
    });
}
exports.saveRequest = saveRequest;
```

Le champ _status_ indiquera si un policier a répondu à la demande ou non. Enfin, dans _routes.js_, ajoutez ceci à l'intérieur de la fonction _initialize_ :

```js
//Écouter un événement 'request-for-help' des citoyens connectés
socket.on('request-for-help', function(eventData) {
    /*
        eventData contient userId et location
        1. D'abord, enregistrer les détails de la demande dans une table requestsData
        2. APRES l'enregistrement, récupérer les policiers à proximité de la localisation du citoyen
        3. Déclencher un événement request-for-help dans chaque salle de policier
    */

    var requestTime = new Date(); //Heure de la demande

    var ObjectID = require('mongodb').ObjectID;
    var requestId = new ObjectID; //Générer un ID unique pour la demande

    //1. D'abord, enregistrer les détails de la demande dans une table requestsData.
    //Convertir la latitude et la longitude en [longitude, latitude]
    var location = {
        coordinates: [
            eventData.location.longitude,
            eventData.location.latitude
        ],
        address: eventData.location.address
    };
    dbOperations.saveRequest(db, requestId, requestTime, location, eventData.citizenId, 'waiting', function(results) {

        //2. APRES l'enregistrement, récupérer les policiers à proximité de la localisation du citoyen
        dbOperations.fetchNearestCops(db, location.coordinates, function(results) {
            eventData.requestId = requestId;
            //3. Après avoir récupéré les policiers les plus proches, déclencher un événement 'request-for-help' pour chacun d'eux
            for (var i = 0; i < results.length; i++) {
                io.sockets.in(results[i].userId).emit('request-for-help', eventData);
            }
        });
    });
});
```

C'est tout, vous avez construit le premier ensemble de fonctionnalités ! Redémarrez le serveur et testez cela en ouvrant 4 onglets, un pour un citoyen et des pages de policiers [01](http://localhost:8000/cop.html?userId=01), [02](http://localhost:8000/cop.html?userId=02) et [03](http://localhost:8000/cop.html?userId=03).

Une fois que vous appuyez sur le bouton d'aide, vous remarquerez que **le policier 01** ne reçoit pas la demande car ce policier est loin de la localisation du citoyen. Cependant, les pages des **policier 02** et **policier 03** montrent la demande d'aide.

Super, vous avez réussi à envoyer une demande d'un citoyen et à notifier tous les policiers à proximité ! Maintenant, pour le deuxième ensemble de fonctionnalités — cela implique de notifier le citoyen une fois qu'un policier accepte la demande.

#### Accepter la demande et notifier le citoyen

![Image](https://cdn-media-1.freecodecamp.org/images/1*fHiz_JjYgm-cE6HU8aQktw.png)

#### **À l'intérieur de _cop.html_**

Le policier doit pouvoir cliquer sur un bouton pour informer le citoyen que la demande a été acceptée. Lorsque ce bouton est cliqué, il déclenchera un événement _request-accepted_ et enverra également les informations du policier au serveur :

```html
<button onclick="helpCitizen()">
    Aider le citoyen
</button>
```

et le gestionnaire d'événements ressemblera à ceci :

```js
function helpCitizen(){
    //Déclencher un événement/signal "request-accepted" et envoyer les informations pertinentes au serveur
    socket.emit("request-accepted", {
        requestDetails: requestDetails,
        copDetails: copDetails
    });
 }
```

#### **À l'intérieur de _citizen.html_**

La page du citoyen commencera à écouter les événements _request-accepted_ du serveur. Une fois qu'elle reçoit le signal, vous pouvez afficher les informations du policier à l'intérieur d'un _div_ vide :

```html
//Écouter un événement "request-accepted"
socket.on("request-accepted", function(eventData){
    copDetails = data; //Enregistrer les détails du policier

   //Afficher les détails du policier
    document.getElementById("notification").innerHTML = "Un policier vient à votre secours ! \n" + JSON.stringify(copDetails);
});
```

Maintenant, le serveur doit gérer l'événement _request-accepted_ comme le montre l'illustration. Tout d'abord, vous écrirez une fonction dans _db-operations.js_ qui mettra à jour la demande dans la base de données avec l'_userId_ du policier et changera le champ _status_ de _waiting_ à _engaged_ :

```js
function updateRequest(db, requestId, copId, status, callback) {
    db.collection('requestsData').update({
        "_id": requestId //Effectuer la mise à jour pour le requestId donné
    }, {
        $set: {
            "status": status, //Mettre à jour le statut à 'engaged'
            "copId": copId  //enregistrer l'userId du policier
        }
    }, function(err, results) {
        if (err) {
            console.log(err);
        } else {
            callback("Issue updated")
        }
    });
}
exports.updateRequest = updateRequest;
```

Lorsque le serveur écoute un événement _request-accepted_, il utilisera la fonction ci-dessus pour enregistrer les détails de la demande et émettra ensuite un événement _request-accepted_ au citoyen. Alors, allez-y, écrivez ceci dans votre fichier _routes.js_ :

```js
//Écouter un événement 'request-accepted' des policiers connectés
socket.on('request-accepted', function(eventData){

    //Convertir la chaîne en type de données ObjectId de MongoDb
    var ObjectID = require('mongodb').ObjectID;
    var requestId = new ObjectID(eventData.requestDetails.requestId);
    //Pour la demande avec requestId, mettre à jour les détails de la demande
    dbOperations.updateRequest(db, requestId, eventData.copDetails.copId, 'engaged', function(results){
                               
       //Déclencher un événement 'request-accepted' au citoyen et envoyer les détails du policier
    io.sockets.in(eventData.requestDetails.citizenId).emit('request-accepted', eventData.copDetails);
       });
 
 });
```

Super, vous avez terminé de construire le deuxième ensemble de fonctionnalités ! Redémarrez votre serveur, actualisez vos pages et essayez-le !

![Image](https://cdn-media-1.freecodecamp.org/images/1*Z_mn4t8eQD0jHINokrrs9w.gif)

#### Qu'est-ce qui suit ?

À ce stade, il est peut-être devenu évident pour vous — la page du citoyen envoie une valeur codée en dur de localisation chaque fois que le bouton d'aide est cliqué. De même, les informations de localisation de tous vos policiers échantillons ont déjà été alimentées dans la base de données plus tôt et sont des valeurs fixes.

Cependant, dans le monde réel, ni le citoyen ni le policier n'ont une localisation fixe car ils se déplacent constamment — et donc vous aurez besoin d'un moyen de tester ce comportement !

### Entrée des cartes

Il existe de nombreuses options de cartographie. Les API Google Maps sont très robustes et riches en fonctionnalités. J'aime personnellement Mapbox, qui utilise les protocoles OpenStreetMap sous le capot, et voici le meilleur — c'est open source et hautement personnalisable ! Alors utilisons cela pour construire le reste de votre application.

#### Utilisation de l'API Mapbox

* Afin de commencer à utiliser ces API, vous devez d'abord créer un compte sur MapBox et obtenir la clé d'authentification [ici](https://www.mapbox.com/studio/).
En fonction de vos besoins, Mapbox propose différents [plans tarifaires](https://www.mapbox.com/pricing/) pour utiliser ces API dans vos applications — pour l'instant, le plan de démarrage gratuit est suffisant.
* Ensuite, vous chargerez la bibliothèque [_mapbox.js_](https://www.mapbox.com/mapbox.js/api/v2.4.0/) (version actuelle 2.4.0) dans les deux pages à l'aide d'une balise script. Elle est construite sur [Leaflet](http://leafletjs.com/) (une autre bibliothèque JavaScript).

```js
<script src="https://api.mapbox.com/mapbox.js/v2.4.0/mapbox.js"></script>
```

Vous chargerez également la feuille de style utilisée par mapbox.js à l'intérieur de la balise _head_ de votre HTML :

```
<link href="https://api.mapbox.com/mapbox.js/v2.4.0/mapbox.css" rel="stylesheet" />
```

Une fois que vous avez fait cela, il est temps pour vous de commencer à écrire la logique —

* Tout d'abord, chargez la carte et définissez-la pour montrer un emplacement par défaut
* Affichez un marqueur sur la carte
* Utilisez la fonction d'autocomplétion offerte par l'API de géocodage de Mapbox. Cela vous permet de saisir un lieu et de choisir parmi les suggestions d'autocomplétion. Après avoir choisi le lieu, vous pouvez extraire les informations sur le lieu et faire ce que vous voulez avec.

Leaflet expose toutes ses API à l'intérieur d'une variable globale _L._ Puisque _mapbox.js_ est construit sur Leaflet, les API que vous allez utiliser seront également exposées dans une variable globale _L_.

* **Dans _citizen.html_** — écrivez ceci dans votre JavaScript

```html
L.mapbox.accessToken = "VOTRE_CLE_API";

//Charger la carte et lui donner un style par défaut
map = L.mapbox.map("map", "mapbox.streets");

//définir à une latitude-longitude et un niveau de zoom donnés
map.setView([12.9718915, 77.64115449999997], 9);

//Afficher un marqueur par défaut
marker = L.marker([12.9718915, 77.64115449999997]).addTo(map);

//Cela affichera une boîte de saisie
map.addControl(L.mapbox.geocoderControl("mapbox.places", {
    autocomplete: true, //suggérera des lieux au fur et à mesure que vous tapez
}).on("select", function(data){
    //Cette fonction s'exécute lorsqu'un lieu est sélectionné

    //data contient les résultats de géocodage
    console.log(data);

    //Faire quelque chose avec les résultats
    //Extraire l'adresse et les coordonnées des résultats et les enregistrer
    requestDetails.location = {
        address: data.feature["place_name"],
        latitude: data.feature.center[1],
        longitude: data.feature.center[0]
    };

    //Définir le marqueur à la nouvelle localisation
    marker.setLatLng( [data.feature.center[1], data.feature.center[0]]);
}));
```

Le code ci-dessus extrait les informations sur le lieu une fois que vous avez sélectionné un lieu et met à jour les détails de localisation, donc la prochaine fois que vous cliquez sur le bouton _help_, vous enverrez la nouvelle localisation avec votre demande.

Une fois qu'un policier accepte la demande, vous pouvez montrer la localisation du policier en utilisant un marqueur personnalisé. Tout d'abord, enregistrez [cette image](https://github.com/booleanhunter/code-samples/blob/master/blog-posts/how-to-build-your-own-uber-for-x-app/public/images/police.png) à l'intérieur de _/public/images_, puis écrivez ce code à l'intérieur du gestionnaire d'événements de l'événement _request-accepted_ :

```js
//Montrer la localisation du policier sur la carte
L.marker([
    copDetails.location.latitude,
    copDetails.location.longitude
],{
    icon: L.icon({
        iconUrl: "/images/police.png", //chemin de l'image
        iconSize: [60, 28] //en pixels
    })
}).addTo(map);
```

C'est tout ! Maintenant, répétons la même chose pour la page du policier également à l'intérieur de _cop.html_.

Votre page de policier récupère les informations de localisation du policier depuis le serveur en utilisant AJAX, donc tout ce que vous avez à faire est de définir la carte et le marqueur pour pointer dessus. Écrivons ce code à l'intérieur de la fonction de rappel _success_ de votre fonction AJAX :

```js
L.mapbox.accessToken = "VOTRE_CLE_API";

//Charger la carte et lui donner un style par défaut
map = L.mapbox.map("map", "mapbox.streets");

//définir à la latitude-longitude d'un policier et au niveau de zoom
map.setView( [copDetails.location.latitude, copDetails.location.longitude ], 9);

//Afficher un marqueur par défaut
marker = L.marker([copDetails.location.latitude, copDetails.location.longitude]).addTo(map);

//Cela affichera une boîte de saisie
map.addControl(L.mapbox.geocoderControl("mapbox.places", {
    autocomplete: true, //suggérera des lieux au fur et à mesure que vous tapez
}).on("select", function(data){
    //Cette fonction s'exécute lorsqu'un lieu est sélectionné
    
    //data contient les résultats de géocodage
    console.log(data);
    
    //Faire quelque chose avec les résultats
    
    //Définir le marqueur à la nouvelle localisation
    marker.setLatLng([
        data.feature.center[1],
        data.feature.center[0]
    ]);
}));
```

Une fois qu'un policier reçoit une demande, vous pouvez utiliser un marqueur personnalisé pour afficher la localisation du citoyen. [Téléchargez](https://github.com/booleanhunter/code-samples/blob/master/blog-posts/how-to-build-your-own-uber-for-x-app/public/images/citizen.png) l'image du marqueur et enregistrez-la dans _/public/images._ Ensuite, écrivons la logique à l'intérieur du gestionnaire d'événements de votre événement _request-for-help_ :

```js
//Montrer la localisation du citoyen sur la carte
L.marker([
    requestDetails.location.latitude,
    requestDetails.location.longitude
],{
    icon: L.icon({
       iconUrl: "/images/citizen.png",
       iconSize: [50,50]
    })
}).addTo(map);
```

Cool, essayons cela — ouvrez les pages de policiers [04](http://localhost:8000/cop.html?userId=04), [05](http://localhost:8000/cop.html?userId=05) et [06](http://localhost:8000/cop.html?userId=06). Dans la page du citoyen, tapez « the forum bengaluru », sélectionnez le premier résultat et regardez l'application en action lorsque vous demandez de l'aide !

![Image](https://cdn-media-1.freecodecamp.org/images/1*buwJZzJtZEiSeoBDSLekwA.gif)

### Visualisation des données

> Une image vaut mille mots

Les gens adorent visualiser les données. Cela vous aide à mieux comprendre un certain sujet. Par exemple, dans le système métrique, je ne réalisais pas à quel point un Gigamètre est vraiment grand, mais je l'ai mieux compris après avoir vu cette image :

![Image](https://cdn-media-1.freecodecamp.org/images/1*ooJfjUNtyELxIdeh3oqV_g.png)
_[htwins.net/scale2/](http://htwins.net/scale2/" rel="noopener" target="_blank" title=")_

Contrairement aux ordinateurs, les humains ne comprennent pas facilement les nombres disposés dans des feuilles de calcul — plus l'ensemble de données est grand, plus il devient difficile pour nous d'identifier des motifs significatifs. Beaucoup d'informations significatives pourraient passer inaperçues, simplement parce que le cerveau humain n'est pas entraîné à examiner un grand nombre de tableaux remplis de texte et de chiffres.

Il est beaucoup plus facile de traiter les informations et d'identifier les motifs si les données peuvent être visualisées. Il existe de nombreuses façons de le faire, sous forme de graphiques, de tableaux, etc., et il existe plusieurs bibliothèques qui vous permettent de faire ces choses sur un écran.

À ce stade, je suppose que vous avez probablement joué un peu avec votre application et enregistré des demandes d'aide dans MongoDB. Si ce n'est pas le cas, vous pouvez [télécharger](https://raw.githubusercontent.com/booleanhunter/code-samples/master/blog-posts/how-to-build-your-own-uber-for-x-app/crime-data.json) l'ensemble de données et l'importer dans votre base de données en tapant ceci dans votre terminal :

```bash
mongoimport --db myUberApp --collection requestsData --drop --file ./path/to/jsonfile.json
```

Comme vous le savez déjà, les demandes enregistrées contiennent des informations utiles comme les détails de _localisation_, le champ _status_ qui indique si un citoyen a reçu de l'aide ou non, et ainsi de suite. Parfait pour utiliser ces informations afin de visualiser les données de criminalité sur une carte thermique ! Voici un [exemple](https://www.mapbox.com/mapbox-gl-js/example/heatmap/) de Mapbox.

Je vais utiliser [MapBox GL JS](https://www.mapbox.com/mapbox-gl-js/api/) — c'est une bibliothèque qui utilise WebGL pour aider à visualiser les données à l'intérieur des cartes et les rendre très interactives. Elle est extrêmement personnalisable — avec des fonctionnalités comme les couleurs, les transitions et l'éclairage. N'hésitez pas à essayer vos propres styles plus tard !

Pour la fonctionnalité de carte thermique, la bibliothèque accepte les ensembles de données au format GeoJSON, puis trace les points de données sur la carte. **GeoJSON** est un format pour encoder une variété de structures de données géographiques. Vous devez donc convertir vos données enregistrées pour qu'elles adhèrent à ce format.

Voici donc les étapes suivantes :

1. Un point de terminaison pour servir votre page de visualisation _data.html._
2. Ensuite, avoir un point de terminaison — _/requests/info_ qui récupère vos demandes de MongoDB, les convertit au format GeoJSON et les renvoie au client.
3. Créer une page _data.html_ qui charge la bibliothèque de visualisation et la feuille de style.
4. En utilisant AJAX, récupérer l'ensemble de données de MongoDB et créer une carte thermique !

#### Étape 1 :

Ouvrez _app.js,_ et écrivez ce code pour servir la page de visualisation :

```js
app.get('/data.html', function(req, res) {
    res.render('data.html');
});
```

#### Étape 2 :

Écrivons une fonction dans _db-operations.js_ qui récupère tous les résultats de votre table _requestsData_ :

```js
function fetchRequests(db, callback) {
    var collection = db.collection('requestsData');
    //Utilisation du flux pour traiter des enregistrements potentiellement énormes
    var stream = collection.find({}, {
        requestTime: true,
        status: true,
        location: true
    }).stream();
    
    var requestsData = [];
    
    stream.on('data', function(request) {
        requestsData.push(request);
    });
    
    //S'exécute après la récupération des résultats
    stream.on('end', function() {
        callback(requestsData);
    });
}
exports.fetchRequests = fetchRequests;
```

Dans le code ci-dessus, vous interrogez la table _requestsData_ pour retourner tous les documents. Vous pouvez spécifier quels champs inclure et exclure des résultats en utilisant des valeurs booléennes — _true_ pour inclure le champ et _false_ pour exclure le champ. Les résultats sont ensuite renvoyés à une fonction de rappel.

**À quoi ressemble GeoJSON ?**

Les informations stockées dans GeoJSON ont le format suivant :

```json
{
    type: "FeatureCollection",
    features: [
        {
             type: "Feature",
             geometry: {
                 type: "Point",
                 coordinates: [<longitude>, <latitude>]
             },
             properties: {
                 <field1>: <value1>,
                 <field2>: <value2>,
                        ...
             }
        }
        ...
    ]
}
```

Vous devrez convertir chaque objet retourné par votre fonction en objets de fonctionnalités. Le champ _properties_ peut contenir des métadonnées facultatives comme _status, requestTime, address_ etc. Vous écrirez le gestionnaire dans _routes.js_ qui appellera la fonction, la convertira en GeoJSON et la renverra :

```js
app.get('/requests/info', function(req, res){
    dbOperations.fetchRequests(db, function(results){
        var features = [];
        
        for(var i=0; i<results.length; i++){
            features.push({
                type: 'Feature',
                geometry: {
                    type: 'Point',
                    coordinates: results[i].location.coordinates
                },
                properties: {
                    status: results[i].status,
                    requestTime: results[i].requestTime,
                    address: results[i].location.address
                }
            });
        }
        var geoJsonData = {
            type: 'FeatureCollection',
            features: features
        }
        
        res.json(geoJsonData);
    });
});
```

#### Étape 3 :

Créez une page _data.html_ dans votre dossier _views_, et chargez la feuille de style et la bibliothèque pour la visualisation :

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8" />
    <title>Visualiser les données</title>
    <link href="https://api.tiles.mapbox.com/mapbox-gl-js/v0.26.0/mapbox-gl.css" rel="stylesheet" />
</head>

<body>

    <div id="map" style="width: 800px; height: 500px"> 
        <!--Charger la carte ici -->
    </div>
    
    <!-- Charger la bibliothèque cliente socket.io -->
    <script src="/socket.io/socket.io.js"></script>
    
    <!-- Charger JQuery depuis un CDN -->
    <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
    
    <!-- Charger la bibliothèque Mapbox GL -->
    <script src="https://api.tiles.mapbox.com/mapbox-gl-js/v0.26.0/mapbox-gl.js"></script>
    
    <!-- charger les bibliothèques avant votre code JS
    Écrivez le reste de votre code JS ici -->
    
    <script type="text/javascript">
        var socket = io();
        var map, marker;
        mapboxgl.accessToken = "VOTRE_TOKEN_D_ACCES";
    </script>
</body>
</html>
```

Maintenant, vous utiliserez AJAX pour appeler votre point de terminaison et récupérer les données GeoJSON :

```js
$.ajax({
    url: "/requests/info",
    type: "GET",
    dataType: "json",
    
    success: function(data) {
        console.log(data);
    }
    error: function(httpRequest, status, error) {
        console.log(error);
    }
});
```

Cool — enregistrez votre code, redémarrez votre serveur et pointez votre navigateur vers [_http://localhost:8000/data.html_](http://localhost:8000/data.html). Vous verrez les résultats de votre appel AJAX dans la console.

Maintenant, utilisons-le pour générer une carte thermique. Écrivez ceci à l'intérieur de la fonction de rappel _success_ de votre appel AJAX :

```js
var map = new mapboxgl.Map({
    container: "map",
    style: "mapbox://styles/mapbox/dark-v9",
    center: [77.64115449999997, 12.9718915],
    zoom: 10
});

map.on("load", function() {
    
    //Ajouter une nouvelle source à partir de nos données GeoJSON
    map.addSource("help-requests", {
       type: "geojson",
       data: data
    });
    
//nous pouvons spécifier différents formats de couleur et de style en ajoutant différentes couches
    
    map.addLayer({
        "id": "help-requests",
        "type": "circle",
        "source": "help-requests",
        "paint": {
        //Appliquer une couleur différente aux différents champs de statut
            "circle-color": {
                property: "status",
                type: "categorical",
                stops: [
                    //Pour waiting, afficher en rouge
                    ["waiting", "rgba(255,0,0,0.5)"],
                    
                    //Pour engaged, afficher en vert
                    ["engaged", "rgba(0,255,0,0.5)"]
                ]
            },
            "circle-radius": 20, //Rayon du cercle
            "circle-blur": 1 //Quantité de flou
        }
    });
});
```

Actualisez votre page pour voir une carte thermique cool générée à partir de votre ensemble de données !

![Image](https://cdn-media-1.freecodecamp.org/images/1*Q2XYNCot6Zuncg6YP0plyQ.png)

### Conclusion

Si vous êtes arrivé jusqu'ici, félicitations ! Espérons que cette série de tutoriels vous a donné un aperçu de la façon de construire une application web en temps réel avec facilité — tout ce dont vous avez besoin maintenant, c'est la prochaine grande idée !

Je suis sûr que vous êtes conscient qu'il reste encore beaucoup de choses à améliorer dans l'application que vous venez de construire. Vous pouvez essayer d'ajouter plus de fonctionnalités et de la rendre plus « intelligente », par exemple :

* Simuler un policier en mouvement et un citoyen en mouvement qui s'envoient continuellement des mises à jour de localisation en temps réel, et mettre à jour les icônes de marqueur sur la carte.
* Définir le champ _status_ sur _closed_ une fois que le policier a aidé le citoyen. Ensuite, vous pouvez attribuer une couleur différente pour visualiser les problèmes fermés sur une carte thermique. De cette façon, vous aurez une compréhension de l'efficacité des policiers dans une zone donnée.
* Construire un système de notation avec lequel un citoyen et un policier peuvent se noter mutuellement. De cette façon, ni le citoyen ni le policier n'abuseront du système, et les policiers peuvent obtenir des rapports de performance.
* Avoir une interface utilisateur cool, comme Material UI.
* Enfin, avoir un mécanisme d'inscription et de connexion !

L'utilisation d'une bibliothèque comme React ou d'un framework comme Angular pourrait vous aider à implémenter des fonctionnalités de manière robuste et évolutive. Vous pourriez également expérimenter avec des bibliothèques de graphiques comme D3.js pour visualiser les informations sous forme de graphiques à barres, de camemberts, de graphiques linéaires, etc.

À un moment donné, vous pourriez déployer votre application sur un fournisseur de services d'hébergement cloud — comme Amazon Web Services ou Google Cloud Platform, pour montrer aux gens ce que vous avez fait et leur faire tester les fonctionnalités. Ce sera une bonne façon d'obtenir des commentaires et des idées, et qui sait — votre application pourrait s'avérer être un sauveur de vie un jour !

![Image](https://cdn-media-1.freecodecamp.org/images/1*f7yN6VNN82Ub4QL9a_id7g.png)

### Merci d'avoir lu.

N'hésitez pas à recommander cela si cela vous a aidé. Si vous avez des questions sur un aspect de cette série de tutoriels ou si vous avez besoin de mon aide pour comprendre quelque chose, n'hésitez pas à [tweeter](https://twitter.com/booleanhunter) ou à laisser un commentaire [ici](https://forum.booleanhunter.com/t/how-to-build-your-own-uber-for-x-app-part-2/17). J'adorerais entendre parler de vos idées **Uber-for-X** ! Vous pouvez également lire d'autres articles similaires dans mon [blog technique](https://ashwinhariharan.tech/blog).

#### Et voici ce que vous attendiez, le code source complet [source code](https://github.com/booleanhunter/how-to-build-your-own-uber-for-x-app) !



Aimé ce que vous avez lu ? Vous devriez [vous abonner](https://www.freecodecamp.org/news/how-to-build-your-own-uber-for-x-app-part-2-8ba6ffa2573d/forum.booleanhunter.com). Je ne perdrai pas votre temps.

> Consultez ma page Patreon !
<a href="https://www.patreon.com/bePatron?u=20804433" data-patreon-widget-type="become-patron-button">Devenir un Patron !</a><script async src="https://c6.patreon.com/becomePatronButton.bundle.js"></script>