---
title: Récapitulatif de la rencontre freeCodeCamp Nashville d'octobre
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-12T21:48:55.000Z'
originalURL: https://freecodecamp.org/news/freecodecamp-nashville-october-meetup-recap-c9004ca5794e
coverImage: https://cdn-media-1.freecodecamp.org/images/0*8ulZ8QJH7r1roTvL.jpg
tags:
- name: learning to code
  slug: learning-to-code
- name: Node.js
  slug: nodejs
- name: 'self-improvement '
  slug: self-improvement
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Récapitulatif de la rencontre freeCodeCamp Nashville d'octobre
seo_desc: 'By Seth Alexander

  On Saturday, October 7, we had our monthly freeCodeCamp Nashville meetup at Nashville
  Software School. As always it was good times.

  We were supposed to have a guest speaker. But at the last minute they couldn’t make
  it. So our very ...'
---

Par Seth Alexander

Le samedi 7 octobre, nous avons eu notre rencontre mensuelle de freeCodeCamp Nashville à la Nashville Software School. Comme toujours, ce fut un bon moment.

Nous devions avoir un conférencier invité. Mais à la dernière minute, ils n'ont pas pu venir. Donc, notre propre superstar et co-organisateur de freeCodeCamp Nashville, [Dave Harned](https://github.com/davi3blu3), est intervenu et a assuré.

Il a présenté un cours accéléré sur Node.js. Vous pouvez trouver le dépôt [ici](https://github.com/davi3blu3/fcc-node-crash). Excusez le fichier readme en cours de travail. Comme la plupart des choses, il n'est pas parfait. N'hésitez pas à ouvrir une Pull Request et à améliorer ces docs !

Je vais vous guider à travers ce que Dave a présenté afin que vous puissiez voir ce que vous avez manqué et venir à la prochaine rencontre ;-). Honnêtement, pour que vous puissiez bénéficier d'une introduction bien structurée qui vous permettra de démarrer, de fonctionner et de jouer en un rien de temps. Dave a choisi [Cloud9](https://c9.io/) comme IDE afin que tout le monde puisse suivre sans avoir à se soucier de ce que les gens pourraient, ou non, avoir sur leurs ordinateurs. Cela offre également une expérience utilisateur cohérente pour faciliter le débogage.

Alors, rendez-vous sur Cloud9, inscrivez-vous et connectez-vous. Consultez également le dépôt à partir du lien ci-dessus et lisez le fichier readme.

Ensuite, vous voudrez cliquer sur `**Créer un nouvel espace de travail**`.

![Image](https://cdn-media-1.freecodecamp.org/images/M50Kuu3ZVFvaGhKpqztnSDPNo3WLIn6ZUgdj)

Le **Nom de l'espace de travail** peut être ce que vous voulez. Laissez **Espace de travail hébergé** sélectionné et choisissez **Privé** ou **Public**, cela n'a pas d'importance. Dans **Cloner depuis l'URL Git ou Mercurial**, entrez `https://github.com/davi3blu3/fcc-node-crash.git`. Ensuite, sous **Choisir un modèle**, sélectionnez `**Node.js**`. Enfin, cliquez sur `**Créer un espace de travail**`.

![Image](https://cdn-media-1.freecodecamp.org/images/vZKvdlxd49le2CDRxslYdMoFYSgEoee-dl4d)

Cela peut prendre une minute, mais finalement, vous aurez quelque chose qui ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/Jk1q9woZEiNP9D0uh-j6g7KThEUUCRD7qGS0)

Alors, première chose, allons dans le terminal en bas de l'écran et tapons `**npm install**` puis appuyez sur Entrée. Cela va importer tous les packages qui sont dans notre fichier `**package.json**`. Vous verrez un nouveau dossier dans votre arborescence de fichiers appelé `**node_modules**`. C'est là que vivent tous les packages.

Maintenant, ouvrons `**1_helloworld.js**`. Cela devrait ressembler à ceci :

```
var hello = function() {    console.log('Hello world');}hello();
// console.log(process.argv);
// var greet = process.argv[2] || "World";
// var hello = function(name) {
//     console.log('Hello ' + name + '!');
// }
// hello(greet);
```

Dans notre terminal, nous pouvons exécuter ce fichier avec `node 1_helloworld.js`. Avec le code initial, vous devriez voir "Hello World" imprimé dans votre terminal. Ce terminal est également notre console dans Cloud9. Donc, tout ce que nous `console.log` se retrouvera ici. Nous pouvons voir quelque chose d'intéressant lorsque nous décommentons la ligne 6 en supprimant le `//`.

Donc, la ligne 6 devrait maintenant ressembler à ceci : `console.log(process.argv);`. Lorsque nous exécutons `node 1_helloworld.js`, nous obtenons notre "Hello World" à nouveau, mais nous obtenons également un tableau qui contient deux éléments.

Le vôtre devrait être le même que le mien :

```
[ '/home/ubuntu/.nvm/versions/node/v6.11.2/bin/node', '/home/ubuntu/workspace/1_helloworld.js' ]
```

Ces deux éléments sont [l'invocation complète de la ligne de commande](https://stackoverflow.com/questions/22213980/could-someone-explain-what-process-argv-means-in-node-js-please#22214003). Nous pouvons faire des choses intéressantes avec cela.

Changeons un peu notre code :

```
// var hello = function() {
//     console.log('Hello world');
// }
// hello();
console.log(process.argv);
var greet = process.argv[2] || "World";
var hello = function(name) {    console.log('Hello ' + name + '!');}
hello(greet);
```

D'accord, nous n'avons pas changé grand-chose. Nous avons seulement commenté et décommenté des éléments. Donc maintenant, nous avons notre console.log d'avant, nous définissons une variable, nous définissons une fonction, et nous appelons cette fonction. Donc, si nous exécutons node `**1_helloworld.js**` maintenant, nous verrons notre tableau `process.argv` et "Hello World".

Si nous exécutons node `**1_helloworld.js "freeCodeCamp Nashville"**`, nous verrons un tableau avec 3 éléments et "Hello freeCodeCamp Nashville" imprimé. Nous pouvons passer des choses de cette manière !

Regardons maintenant `**2_hellofile.js**` :

```
const fs = require('fs');
const fileToRead = process.argv[2] || 'README.md';
const lineIndex = process.argv[3] - 1 || 3;
fs.readFile(fileToRead, function (err, data) {    if (err) throw err;    var lines = data.toString('utf-8').split("\n");    console.log(lines[lineIndex]);});
```

Exécutons cela avec `**node 2_hellofile.js**` et voyons ce que nous obtenons. Wow, d'où cela vient-il ? Passons en revue comment cela s'est produit. Je ne vais pas expliquer comment `fs` fonctionne. C'est un module qui vient avec Node.js et si vous voulez en savoir plus, vous pouvez regarder [ici](https://nodejs.org/dist/latest-v6.x/docs/api/fs.html#fs_file_system).

* Ligne 1, nous importons le module dans notre fichier JavaScript. Maintenant, nous pouvons utiliser tout ce qui vient avec lui.
* Ligne 2, nous définissons une variable égale à quelque chose que nous passons dans notre `process.argv` ou `README.md`.
* Ligne 3, nous définissons une autre variable égale à quelque chose que nous passons dans notre `process.argv` ou `3`.
* Ligne 5, nous utilisons la fonction `readFile` qui vient avec `fs` et nous passons un argument et une fonction de rappel pour gérer une erreur ou des données.
* Ligne 6, nous disons que nous lancerons une erreur si une erreur se produit.
* Ligne 8, nous définissons une variable qui prend les données que `fs` obtient pour nous et les transforme en une chaîne, puis les divise sur "\n" pour que nous obtenions un tableau de chaînes.
* Ligne 10, nous `console.log` l'élément du tableau `lines` qui se trouve à la position d'index `lineIndex`.
* Ligne 11, nous fermons la fonction.

Si vous voulez jouer avec cela, essayez `node 2_hellofile.js 'README.md' 14`. Nous prenons le **readme** et le transformons en un tableau divisé à la fin de chaque ligne, puis nous enregistrons la ligne que nous appelons par numéro.

Passons à `**3_helloweb.js**` qui devrait ressembler à ceci :

```
const http = require('http');
// sur c9.io, le nom d'hôte doit être '8080'
// localement, cela peut être presque n'importe quoi
const port = 3000;
// sur c9.io, le nom d'hôte doit être '0.0.0.0'
// localement, vous utiliseriez 'localhost' (une variable pour '127.0.0.1')
const hostname = 'localhost';
const server = http.createServer(function(request, response){    response.writeHead(200, {"Content-Type": "text/plain"});    response.write("Hello Web! XOXO, Node");    response.end();});
server.listen(port, hostname, function(){    console.log(`Server running at ${hostname}:${port}/`);});
```

Une fois de plus, sans entrer trop dans les détails de ce qu'est `http`, il fait démarrer notre serveur. Ce `**3_helloweb.js**` va être notre **serveur web** Node.js. Un serveur très simple, mais un serveur tout de même. Dave nous a laissé quelques notes. Nous devons changer la variable `port` à la ligne 5 en `8080` et la variable `hostname` à la ligne 9 en `'0.0.0.0'`. Si vous exécutiez ce code localement, les paramètres qui sont ici devraient fonctionner. Cependant, Cloud9 a des restrictions spécifiques sur la manière dont ils nous permettent d'exécuter un serveur. Donc, faites les changements et exécutez `node 3_helloweb.js` dans votre terminal.

Vous devriez être accueilli avec un `Server running at 0.0.0.0:8080/` et une boîte verte de Cloud9 avec un lien vers le serveur :

![Image](https://cdn-media-1.freecodecamp.org/images/ikYybTipTV9M5hgrz255NtalfOr4K4XCva-M)

Lorsque vous cliquez sur ce lien pour la première fois, vous obtiendrez un écran orange désagréable avec un bouton rouge. C'est Cloud9 qui vous dit de ne pas utiliser ce type de serveur pour quoi que ce soit d'important. Donc, cliquez pour passer et vous devriez voir une page web qui dit "Hello Web! XOXO, Node". Ce texte provient directement de la ligne 18 de notre fichier `**3_helloweb.js**`. Pour arrêter le serveur, cliquez sur le terminal et appuyez sur `ctrl + c` ou `cmd + c`.

Enfin, nous avons `**4_helloexpress.js**` :

```
// importer les dépendances / bibliothèques
var http = require('http');
var express = require('express');
var app = express();
var bodyParser = require('body-parser');
```

```
// variables d'environnement
var port = 8080;
var hostname = '0.0.0.0';
```

```
// analyse le contenu textuel d'une requête http
app.use(bodyParser.text({ type: 'text/html' }));
```

```
// sert des fichiers statiques comme notre html et css depuis le dossier public
app.use(express.static('public'));
```

```
// cela gère notre requête post depuis le front end
app.post('/', function(req, res, next) {    console.log('Message du navigateur : ',  req.body);    res.end('Message reçu. Bonjour depuis le back end!');})
```

```
// démarre le serveur et écoute les requêtes
var server = http.createServer(app);
```

```
server.listen(port, hostname, function(){    console.log(`Server running at ${hostname}:${port}/`);});
```

Dans cette application, nous allons utiliser [Express](https://expressjs.com/) comme framework pour notre application web. Express est super populaire. Lisez leur documentation si vous êtes intéressé, je ne vais pas entrer trop dans les détails ici.

Je ne vais pas non plus entrer trop dans les détails de ce code, sauf pour souligner quelques points. Exécutons notre serveur avec `**node 4_helloexpress.js**`. Lorsque nous allons sur le site web, nous devrions avoir un formulaire simple.

![Image](https://cdn-media-1.freecodecamp.org/images/JnUMlNeFeZwi5XXugEsbzUcNWyqyNzgsEpuo)

Cela provient de la ligne 15 où nous disons à Express de servir les fichiers dans le dossier public. Le dossier public contient trois fichiers qui composent notre front end. Jetez un coup d'œil à `**frontend.js**` dans Cloud9 :

```
var submit = document.getElementById('submit');
```

```
var captureData = function(e) {    var data = document.getElementById('data');    sendData(data.value);}
```

```
var sendData = function(message) {
```

```
    var xhr = new XMLHttpRequest();    xhr.open("POST", '/', true);    xhr.setRequestHeader("Content-type", "text/html");    xhr.onreadystatechange = function() {        if(xhr.readyState == XMLHttpRequest.DONE && xhr.status == 200) {            console.log('Envoi : ' + message + '. Réussi!');            console.log(xhr.response);        }    }    xhr.send(message); }
```

```
submit.addEventListener("click", captureData);
```

Maintenant, si vous utilisez Chrome (que nous recommandons chez freeCodeCamp Nashville), ouvrez la console sur cette page violette disgracieuse. `ctrl + shift + i` ou `cmd + shift + i` devrait le faire. Sinon, cliquez avec le bouton droit n'importe où sur la page violette et choisissez l'option "Inspecter". Vous verrez une erreur concernant **favicon.ico** et vous pouvez l'ignorer.

Ce que nous voulons montrer, c'est le front end qui parle au serveur back end. Nous allons le faire en enregistrant dans les deux consoles différentes. Donc, lorsque nous tapons quelque chose dans notre formulaire et cliquons sur "Submit", nous devrions voir ceci dans notre console de navigateur :

![Image](https://cdn-media-1.freecodecamp.org/images/NyJOX6YhyFdxAkUpVA527hg7LDZjqbPnGcsX)

et ceci dans notre terminal serveur Cloud9 :

![Image](https://cdn-media-1.freecodecamp.org/images/z1E1iIAodDcBn-IaOmGuhL4IKcW4dsK7xjGA)

Lorsque nous cliquons sur "Submit", nous effectuons une requête POST à la ligne 11 de `**frontend.js**`. À la ligne 14, nous créons ce premier message de console que nous voyons dans notre console Chrome si les données sont envoyées avec succès.

Ensuite, dans notre `**4_helloexpress.js**` à la ligne 26, nous configurons le serveur pour écouter. Notre front end a envoyé le POST donc le serveur "entend" cela et le gère à la ligne 18 parce que c'est un POST. À la ligne 19, il enregistre dans le terminal Cloud9 ce que nous avons vu auparavant et à la ligne 20, il envoie des informations au front end.

La ligne 16 dans `**frontend.js**` reçoit les informations que le back end vient d'envoyer en réponse et les enregistre dans notre console Chrome. C'est beaucoup d'allers-retours, mais cela illustre comment les navigateurs et les serveurs "communiquent" entre eux.

![Image](https://cdn-media-1.freecodecamp.org/images/IGR-SIRip0lLCoBIGSW7y2bNk4MJ18i7JQrp)
_Une photo de l'événement._

Espérons que cela a piqué votre curiosité et que vous voulez commencer à construire vos propres applications JavaScript full stack. Ou peut-être que maintenant vous en savez assez pour commencer à vous amuser et à jouer.

Si vous voulez nous rejoindre à freeCodeCamp Nashville, consultez-nous sur [Meetup à freeCodeCamp Nashville](https://www.meetup.com/freeCodeCamp-Nashville). Nous avons également une [Page Facebook Free Code Camp Nashville](https://www.facebook.com/groups/free.code.camp.nashville/).

Ma préférence est le canal #freecodecamp sur le réseau [NashDev Slack](https://nashdev.com/). Si vous voulez nous rejoindre, allez sur le lien et entrez votre email. Vous recevrez une invitation au réseau. Configurez votre compte et une fois connecté, vous serez automatiquement dans le canal #general. Tapez `/join #freecodecamp` et appuyez sur Entrée. Ensuite, vous serez directement avec nous en train de discuter.