---
title: Comment créer votre propre application Uber-for-X
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-10-22T06:20:09.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-your-own-uber-for-x-app-33237955e253
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
seo_title: Comment créer votre propre application Uber-for-X
seo_desc: 'By Ashwin Hariharan

  Featured in Mybridge’s Top Ten NodeJS articles from October 2016 and Top Ten NodeJS
  articles of the year (v.2017)



  Update: Check-out the latest version on my tech blog!

  This article is now a few years old - and due to JavaScript''...'
---

Par Ashwin Hariharan

Présenté dans [Mybridge](https://medium.mybridge.co/)s [Top Ten NodeJS articles from October 2016](https://medium.mybridge.co/node-js-top-ten-articles-from-october-fbde1ebe7785#.fnr9w51pr) et [Top Ten NodeJS articles of the year (v.2017)](https://medium.mybridge.co/node-js-top-10-articles-of-the-year-v-2017-79df8269d0f3#.f82p1dork)

*****
> **Mise à jour : Consultez la dernière version sur mon [blog technique](https://ashwinhariharan.tech/blog/how-to-build-your-own-uber-for-x-app/) !**
> Cet article a maintenant quelques années et, en raison de l'écosystème JavaScript en rapide évolution, l'article est devenu légèrement obsolète. Cliquez sur le lien ci-dessus pour la version mise à jour de cet article et du projet.
*****

Uber (si vous n'en avez pas entendu parler) est une application pratique qui vous permet de prendre un taxi sans avoir à chercher. Et surtout, elle résout les problèmes de demande et d'offre qui existent entre les chauffeurs de taxi et les personnes cherchant un taxi.

Aujourd'hui, il existe une variété de startups axées sur les applications **_Uber-for-X_**. L'idée est que ce qu'Uber a fait pour les taxis, ils peuvent sûrement le faire pour d'autres problèmes d'offre/demande.

Lors d'un hackathon, un ami et moi avons décidé de créer une application citoyen-policier. Nous avons pensé qu'il serait cool de construire quelque chose qui peut aider vos amis en cas de problème !

Après quelques réflexions, voici les fonctionnalités sur lesquelles nous nous sommes mis d'accord :

1. Les civils pourront demander le policier le plus proche dans leur quartier en appuyant sur un bouton. Cela enverra un 'signal de détresse' et alertera les policiers à proximité.
2. Tout policier à proximité recevra immédiatement la localisation de l'utilisateur et pourra choisir d'accepter la demande et de résoudre le problème.
3. Un système de notation
4. Les données collectées à partir des localisations, des cas de criminalité résolus, etc. peuvent être visualisées sur une carte, ou graphées avec d'autres widgets d'interface utilisateur cool

![Image](https://cdn-media-1.freecodecamp.org/images/1*MW1nUkwxgGuUN8lbIFCfDg.png)

Dans ce tutoriel, je vais vous guider à travers les étapes de construction, afin que vous puissiez construire votre propre application **_Uber-for-X_**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*438j5EzvsD_q2cjBrKe-Tg.png)

Avant de commencer, il serait utile de garder à l'esprit les points suivants —

* Ce tutoriel ne se concentrera pas sur la construction de l'application pour la scalabilité. Ou pour la performance. Il est principalement conçu pour que vous puissiez vous amuser en le construisant, et pour que vous puissiez créer quelque chose qui imite Uber. Pensez à cela comme à la construction d'un Produit Minimum Viable pour démontrer votre idée ou startup, pour une preuve de concept.
* Comme je n'ai pas beaucoup travaillé sur les applications Android ou iPhone, je vais construire cela pour qu'il fonctionne dans un navigateur.

Maintenant, chaque application que vous construisez a quelques pièces importantes :

* une application côté client (que vous voyez dans un navigateur ou sur les écrans de votre téléphone)
* sur le backend, un serveur web pour gérer les requêtes entrantes du client et pour router les informations
* et une base de données pour stocker et interroger les informations.

Sur le backend, vous utiliserez MongoDB comme base de données. C'est plus facile à apprendre, et offre beaucoup de techniques de requêtage pour gérer les informations géospatiales, dont vous aurez besoin pour votre application.

Vous utiliserez NodeJS pour votre logique backend. Parce que c'est le même langage pour le frontend et le backend, vous n'aurez pas à vous soucier d'apprendre un nouveau langage ou une nouvelle syntaxe.

Sur le frontend, vous utiliserez HTML5, CSS3, JavaScript, ainsi que les API Google Maps et Places.

Je suppose que vous avez déjà une connaissance pratique de JavaScript, et que vous avez au moins une compréhension théorique de comment NodeJS et MongoDB fonctionnent.

Voici le contenu de ce tutoriel :

**Partie 1 (ce que vous lisez en ce moment) :**

* Conception du schéma MongoDB
* Utilisation de la console Mongo pour interroger les informations
* Connexion de votre base de données avec votre serveur Node-Express et écriture d'API RESTful

**Partie 2 :**

* Utilisation de Socket.IO pour permettre aux appareils de policier et de civil de communiquer entre eux
* Utilisation de l'API Google Maps pour afficher les civils et les policiers sur une carte

### Commençons !

Les développeurs utilisent MongoDB pour construire des applications depuis un certain temps. Il a une courbe d'apprentissage peu abrupte, et sa polyvalence permet aux développeurs de construire rapidement des applications avec facilité.

Personnellement, j'aime MongoDB car il me permet de construire rapidement des prototypes pour une idée afin de démontrer une preuve de concept.

Avant de commencer, assurez-vous d'avoir MongoDB et NodeJS installés. Au moment de la rédaction de cet article, la version actuelle de MongoDB est **3.2**.

### **Conception du Schéma**

Puisque vous utilisez MongoDB, tout ce que vous enregistrez est une collection de documents.

Créons une collection appelée _citizensData_ pour stocker les informations des citoyens, et une autre collection appelée _policeData_ pour stocker les informations des policiers. Alors, ouvrez votre terminal et tapez _mongo_ pour lancer la console mongo. Une fois ouverte, vous pouvez afficher les bases de données existantes dans MongoDB en tapant :

```
show dbs
```

Vous avez besoin d'une nouvelle base de données pour stocker les données de votre application. Appelons-la _myUberApp_. Pour créer une nouvelle base de données, vous pouvez taper :

```
use myUberApp
```

La commande _use_ a pour effet de créer une nouvelle base de données si elle n'existe pas. Si elle existe, elle indique à Mongo d'appliquer toutes les commandes suivantes à cette base de données.

Mongo stocke les documents dans des _collections_. Les collections sont comme des tables. Pour voir les collections existantes, tapez :

```
show collections
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*F7W7VRj4bSehrwmItGo8Ww.jpeg)

Pour le policier, le nom d'utilisateur pourrait être l'identifiant de badge. Vous pourriez ajouter un champ pour l'adresse e-mail et un pour le mot de passe (qui ne sera pas révélé) à des fins d'authentification.

Allez à ce [lien](https://raw.githubusercontent.com/booleanhunter/code-samples/master/blog-posts/how-to-build-your-own-uber-for-x-app/cops.json), et enregistrez le jeu de données JSON pour les informations liées aux policiers.

Pour importer les données de ce fichier JSON, tapez ceci dans votre terminal :

```
mongoimport --db myUberApp --collection policeData --drop --file ./path/to/jsonfile.json
```

Maintenant, avant de commencer à interroger votre base de données, vous devez apprendre un peu comment les _index_ dans MongoDB (ou toute base de données d'ailleurs) fonctionnent.

Un index est un arrangement spécial de données ou une structure de données qui vous permet d'interroger des informations très efficacement. Ainsi, vous pouvez rapidement récupérer des résultats sans avoir à scanner toute la base de données.

Par exemple — supposons que vous avez stocké des informations sur les étudiants dans l'ordre ascendant de leur nom dans un livre, ce qui signifie que vous avez un index sur le champ nom. Ainsi, si vous deviez récupérer les informations d'une personne nommée _Tyrion_, vous pouvez rapidement localiser ses informations sans passer par le reste des étudiants en premier.

Mais si vous avez enregistré les mêmes informations dans l'ordre ascendant de leur taille, alors interroger les informations d'une personne en utilisant leur nom deviendrait difficile. Cela pourrait prendre beaucoup de temps, car maintenant les étudiants ne sont pas enregistrés dans l'ordre de leurs noms, donc vous pourriez avoir à scanner et rechercher dans plusieurs lignes.

Mais d'autres types de requêtes deviennent possibles. Par exemple, récupérer les informations des étudiants dont la taille se situe entre 4 et 5 pieds. Dans ce cas, les informations de _Tyrion_ pourraient être récupérées rapidement, car :

![Image](https://cdn-media-1.freecodecamp.org/images/1*0YhfgYNBAXv4aLHuovNd3g.png)

Différentes bases de données supportent différents types d'index. Vous pourriez lire la liste complète des index supportés par MongoDB [ici](https://docs.mongodb.com/v3.2/indexes/).

Donc, maintenant si vous tapez cette commande :

```
 db.policeData.find().pretty()
```

qui vous retournera tous les documents qui existent dans la collection _policeData_ — qui est la liste complète des policiers. (La fonction _pretty_ rend la sortie plus facile à lire).

Si vous voulez récupérer des informations sur un policier particulier dont l'_userId_ est _01_, vous pouvez taper `db.policeData.find({userId: "01"}).pretty()`

```javascript
{
    "_id" : ObjectId("57e75af5eb1b8edc94406943"),
    "userId" : "01",
    "displayName" : "Cop 1",
    "phone" : "01",
    "email" : "cop01@gmail.com",
    "earnedRatings" : 21,
    "totalRatings" : 25,
    "location" : {
        "type" : "Point",
        "address" : "Kalyan Nagar, Bengaluru, Karnataka 560043, India",
        "coordinates" : [
            77.63997110000003,
            13.0280047
        ]
    }
}
```

#### **Utilisation des index géospatiaux de MongoDB**

Les index géospatiaux vous permettent de stocker des objets [GeoJSON](http://geojson.org/) dans des documents.

Les objets GeoJSON peuvent être de différents [types](https://docs.mongodb.com/manual/reference/geojson/#overview), tels que _Point, LineString_ et _Polygon._

Si vous observez la sortie de votre commande _.find()_, vous remarquerez que chaque _location_ est un objet qui contient le champ _type_ et le champ _coordinates_. Cela est important, car si vous stockez votre objet GeoJSON comme un type _Point_, vous pouvez utiliser la commande [$near](https://docs.mongodb.com/manual/reference/operator/query/near/) pour interroger les points à proximité pour une longitude et une latitude données.

Pour utiliser cela, vous devez créer un index [_2dsphere_](https://docs.mongodb.com/v3.2/core/2dsphere/) (qui est un index géospatial) sur le champ _location_, et avoir un champ _type_ à l'intérieur. L'index _2dsphere_ supporte les requêtes qui calculent les géométries sur une sphère de type terrestre. Cela inclut les requêtes géospatiales MongoDB : requêtes pour l'inclusion, l'intersection et la proximité.

Donc, tapez ceci dans votre console mongo :

```
db.policeData.createIndex({"location": "2dsphere"})
```

Maintenant, pour récupérer les documents du plus proche au plus éloigné d'une paire de coordonnées donnée, vous devez émettre une commande avec cette syntaxe :

```javascript
db.<collectionName>.find({
    <fieldName>: {
        $near: {
            $geometry: {
                type: "Point",
                coordinates: [<longitude>, <latitude>]
            },
            $minDistance: <distance en mètres>,
            $maxDistance: <distance en mètres>
        }
    }
}).pretty()
```

$minDistance et $maxDistance sont des champs optionnels. Maintenant, pour obtenir tous les policiers situés à moins de 2 kilomètres de la _latitude 12.9718915_ et de la _longitude 77.64115449999997_, exécutez ceci :

```javascript
db.policeData.find({
    location: {
        $near: {
            $geometry: {
                type: "Point",
                coordinates: [77.64115449999997, 12.9718915]
            },
            $maxDistance: 2000
        }
    }
}).pretty()
```

Et c'est tout — vous trouverez une liste de documents retournés dans la sortie !

Parfait ! Maintenant, essayons de faire la même chose avec un serveur web. Téléchargez ce fichier [package.json](https://github.com/booleanhunter/code-samples/blob/master/blog-posts/how-to-build-your-own-uber-for-x-app/package.json) et enregistrez-le à la racine de votre dossier de projet (assurez-vous de le nommer _package.json_), puis dans votre terminal, _cd_ vers le répertoire qui contient le fichier et exécutez

```
sudo npm install
```

Une brève explication sur certains des packages que vous allez utiliser :

* [Express](https://expressjs.com/) est un framework web pour NodeJS. Il dispose de nombreuses API, utilitaires et middlewares dans son écosystème pour vous aider à construire votre application.
* [body-parser](https://github.com/expressjs/body-parser) analyse les corps de requête entrants dans un middleware avant vos gestionnaires, disponibles sous la propriété _req.body_. Vous en avez besoin pour gérer les requêtes POST.
* [underscore](http://underscorejs.org/) simplifie l'écriture de JavaScript. N'hésitez pas à utiliser une autre bibliothèque si vous préférez.
* [socket.io](http://socket.io) vous permet d'utiliser des web sockets dans votre application Node.
* [mongodb](https://www.npmjs.com/package/mongodb) est le pilote officiel NodeJS pour MongoDB. Il aide votre application Node à communiquer avec votre base de données.

Le fichier package.json contient d'autres modules également. Vous en aurez besoin lors de la construction d'une application complète, mais je vais me concentrer sur l'utilisation du pilote _mongodb_ dans votre application express pour exécuter des requêtes. Voici ce que font certains des autres modules :

* [async](https://www.npmjs.com/package/async) est un utilitaire pour gérer le code asynchrone dans NodeJS. Il vous aide à éviter l'enfer des callbacks.
* [debug](https://www.npmjs.com/package/debug) est une bibliothèque de débogage. Cet outil pratique aide à déboguer vos programmes sans utiliser de sorties de déclarations _console.log_ laides.
* [redis](https://www.npmjs.com/package/redis) est similaire au pilote _mongodb_. Il permet à votre application NodeJS de communiquer avec votre base de données Redis.
* [connect-redis](https://www.npmjs.com/package/connect-redis) est un magasin de sessions qui utilise Redis pour gérer les sessions. Vous en aurez besoin plus tard lorsque vous déciderez d'avoir des comptes utilisateurs.

Avant d'écrire du code, il sera utile de l'organiser d'abord. Pour l'instant, vous pouvez utiliser deux fichiers :

* Un fichier pour écrire vos points de terminaison d'API
* Un fichier qui utilise les pilotes de base de données pour les opérations liées à la base de données. Le gestionnaire de route décidera quelle fonction appeler à partir du fichier de base de données. Une fois une requête effectuée, les résultats sont renvoyés à votre gestionnaire de route à l'aide d'une fonction de rappel.

Voyons à quoi cela ressemble lorsque vous écrivez votre code :

```javascript
var http = require("http");
var express = require("express");
var consolidate = require("consolidate");//1
var _ = require("underscore");
var bodyParser = require('body-parser');

var routes = require('./routes'); //Fichier qui contient nos points de terminaison
var mongoClient = require("mongodb").MongoClient;

var app = express();
app.use(bodyParser.urlencoded({
   extended: true,
}));
             
app.use(bodyParser.json({limit: '5mb'}));

app.set('views', 'views'); //Définir le nom du dossier à partir duquel vous servez la page html. 
app.use(express.static('./public')); //définir le nom du dossier (public) où tous les fichiers statiques comme css, js, images etc sont mis à disposition

app.set('view engine','html');
app.engine('html',consolidate.underscore);
var portNumber = 8000; //pour locahost:8000

http.createServer(app).listen(portNumber, function(){ //création du serveur qui écoute le numéro de port :8000, et appelle une fonction à l'intérieur qui appelle la fonction initialize(app) dans le module routeur
	console.log('Serveur à l'écoute sur le port '+ portNumber);
	
	var url = 'mongodb://localhost:27017/myUberApp';
	mongoClient.connect(url, function(err, db) { //une connexion avec mongodb est établie ici.
		console.log("Connecté à la base de données");
		routes.initialize(app, db); //fonction définie dans routes.js qui est exportée pour être accessible par d'autres modules
	});
});

/* 1. Tous les moteurs de template ne fonctionnent pas uniformément avec express, donc cette bibliothèque en js, (consolidate), est utilisée pour faire fonctionner les moteurs de template uniformément. Bien qu'elle n'ait aucun 
module propre et que tout moteur de template à utiliser doive être installé séparément !*/

```

Dans cet exemple, vous créez une nouvelle instance de l'objet _MongoClient_ à partir du module _mongodb_. Une fois que le serveur web commence, vous vous connectez à votre base de données MongoDB en utilisant la fonction _connect_ qui est exposée par votre instance _MongoClient_. Après avoir initialisé la connexion, elle retourne une instance _Db_ dans le callback.

Vous pouvez maintenant passer les instances _app_ et _db_ à la fonction _initialize_ de votre fichier _routes.js_.

Ensuite, vous devez créer un nouveau fichier appelé _routes.js_, et ajouter ce code :

```js
function initialize(app, db) { 
    //Une requête GET à /cops devrait retourner les policiers les plus proches à proximité.
    app.get('/cops', function(req, res){
    /*extraire les informations de latitude et de longitude de la requête. Ensuite, récupérer les policiers les plus proches en utilisant les requêtes géospatiales de MongoDB et les retourner au client.
    */
    });
}
exports.initialize = initialize;
```

Pour que cela fonctionne, vous devrez passer les coordonnées comme chaînes de requête dans votre requête. Vous écrirez également vos opérations de base de données dans un autre fichier. Alors, créez un nouveau fichier _db-operations.js_, et écrivez ceci :

```javascript
function fetchNearestCops(db, coordinates, callback) {
    db.collection('policeData').createIndex({
        "location": "2dsphere"
    }, function() {
        db.collection("policeData").find({
            location: {
                $near: {
                    $geometry: {
                        type: "Point",
                        coordinates: coordinates
                    },
                    $maxDistance: 2000
                }
            }
        }).toArray(function(err, results) {
            if(err) {
                console.log(err)
            }else {
                callback(results);
            }
        });
    });
}
exports.fetchNearestCops = fetchNearestCops;
```

Cette fonction accepte trois arguments : une instance de _db_, un tableau qui contient des coordonnées dans l'ordre [<longitude>,<latitude>], et une fonction de rappel, à laquelle elle retourne les résultats de votre requête.

Le _createIndex_ garantit qu'un index est créé sur le champ spécifié s'il n'existe pas, donc vous pourriez vouloir sauter cela si vous avez déjà créé un index avant d'interroger.

Maintenant, tout ce qu'il reste à faire est d'appeler cette fonction à l'intérieur de votre gestionnaire. Alors modifiez votre code _routes.js_ comme ceci :

```javascript
var dbOperations = require('./db-operations');
function initialize(app, db) {
    // '/cops?lat=12.9718915&&lng=77.64115449999997'
    app.get('/cops', function(req, res){
        //Convertir les chaînes de requête en nombres
        var latitude = Number(req.query.lat);
        var longitude = Number(req.query.lng);
        dbOperations.fetchNearestCops(db, [longitude,latitude], function(results){
        //retourner les résultats au client sous forme de JSON
            res.json({
                cops: results
            });
        });  
    });
}
exports.initialize = initialize;
```

Et c'est tout ! Exécutez

```
node app.js 
```

depuis votre terminal, puis ouvrez votre navigateur et allez sur [http://localhost:8000/cops?lat=12.9718915&&lng=77.64115449999997](http://localhost:8000/cops?lat=12.9718915&&lng=77.64115449999997)

Selon les chaînes de requête que vous avez passées, vous devriez obtenir une réponse JSON contenant un tableau vide ou un tableau contenant des données de policiers !

C'est la fin de la Partie 1. Dans la [Partie 2](https://medium.freecodecamp.com/how-to-build-your-own-uber-for-x-app-part-2-8ba6ffa2573d), vous allez passer à la vitesse supérieure et essayer d'envoyer un signal de détresse aux policiers à proximité. Ensuite, vous allez découvrir comment un policier pourrait répondre au signal en utilisant socket.io. Vous allez également voir comment afficher l'emplacement du citoyen sur une carte.

En attendant, jetez un coup d'œil au [code source](https://github.com/booleanhunter/how-to-build-your-own-uber-for-x-app) sur GitHub !

![Image](https://cdn-media-1.freecodecamp.org/images/1*aoUgLA_yDneLrALRQHYqUw.png)

Si vous avez aimé cet article, envisagez de me soutenir sur Patreon.

<a href="https://www.patreon.com/bePatron?u=20804433" data-patreon-widget-type="become-patron-button">Devenir un Patron !</a><script async src="https://c6.patreon.com/becomePatronButton.bundle.js"></script>

Vous devriez absolument [vous abonner](https://www.freecodecamp.org/news/how-to-build-your-own-uber-for-x-app-33237955e253/forum.booleanhunter.com). Je ne perdrai pas votre temps.

**Un grand merci à [Quincy Larson](https://medium.com/@quincylarson) pour m'avoir aidé à améliorer cet article.**

> Présenté dans [Mybridge](https://medium.mybridge.co/)s [Top Ten NodeJS articles from October 2016](https://medium.mybridge.co/node-js-top-ten-articles-from-october-fbde1ebe7785#.fnr9w51pr) et [Top Ten NodeJS articles of the year (v.2017)](https://medium.mybridge.co/node-js-top-10-articles-of-the-year-v-2017-79df8269d0f3#.f82p1dork)