---
title: Apprendre Node.js en construisant une application de microservice d'horodatage
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-22T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/microservice-8edfdb9be811
coverImage: https://cdn-media-1.freecodecamp.org/images/0*BaUWxBjXYt4i5AvZ
tags:
- name: Apps
  slug: apps-tag
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Apprendre Node.js en construisant une application de microservice d'horodatage
seo_desc: 'By Ayo Isaiah

  One of the reasons why Node.js is such a great platform for building applications
  is the abundance of libraries that have been developed by the community for practically
  all the common use cases. This makes it really easy to go from ide...'
---

Par Ayo Isaiah

L'une des raisons pour lesquelles Node.js est une plateforme si formidable pour construire des applications est l'abondance de bibliothèques qui ont été développées par la communauté pour pratiquement tous les cas d'utilisation courants. Cela rend vraiment facile de passer d'une idée à une application prête pour la production en un temps relativement court.

Cela dit, comprendre au moins les bibliothèques standard de Node.js sera toujours bénéfique pour vous, surtout si vous voulez acquérir une compréhension plus approfondie de comment Node.js fonctionne.

Dans cet article, vous apprendrez à construire un [microservice d'horodatage](https://learn.freecodecamp.org/apis-and-microservices/apis-and-microservices-projects/timestamp-microservice) en utilisant quelques modules intégrés de Node.js. Voici une [démo en direct](https://ayo-timestamp.herokuapp.com/) de ce que nous allons construire. Vous pouvez trouver le code source complet de ce projet dans ce [dépôt GitHub](https://github.com/ayoisaiah/timestamp-microservice).

### Prérequis

Vous devez avoir une expérience préalable de la construction d'applications JavaScript dans le navigateur, mais aucune expérience préalable avec Node.js n'est requise. Avant de continuer, vous devez avoir Node.js et `npm` installés.

Vous pouvez visiter le [site web de Node.js](https://nodejs.org/en/download/) pour voir les instructions d'installation pour votre système d'exploitation. [npm](https://npmjs.com/) est fourni avec Node, donc une fois que vous installez Node, vous aurez également accès à la commande `npm`.

Les versions que j'ai utilisées pour construire ce projet sont les suivantes :

* Node.js v10.9.0
* npm v6.4.1

Vous pouvez voir la version de Node et `npm` que vous avez installée en exécutant les commandes suivantes dans votre terminal :

```
node -vnpm -v
```

### Histoires utilisateur

Voici les histoires utilisateur pour ce projet :

1. Le point de terminaison de l'API est `GET [project_url]/api/timestamp/:date_string?`
2. Une chaîne de date est valide si elle peut être analysée avec succès par `new Date(date_string)`. Notez que l'horodatage unix doit être un entier (et non une chaîne) spécifiant les millisecondes. Dans notre test, nous utiliserons des chaînes de date conformes à ISO-8601 (par exemple, "2016-11-20") car cela garantira un horodatage UTC.
3. Si la chaîne de date est vide, elle doit être équivalente à déclencher `new Date()`, c'est-à-dire que le service utilise l'horodatage actuel.
4. Si la chaîne de date est valide, l'API retourne un JSON ayant la structure `{"unix": <date.getTime()>, "utc" : <date.toUTCString()> }` par exemple, {"unix": 1479663089000, "utc": "Sun, 20 Nov 2016 17:31:29 GMT"}.
5. Si la chaîne de date est invalide, l'API retourne un JSON ayant la structure `{"error" : "Invalid Date" }`.

### Getting started

Ouvrez une nouvelle instance de terminal sur votre ordinateur, puis créez un nouveau répertoire pour ce projet dans votre système de fichiers, et changez-vous en utilisant les commandes suivantes :

```
mkdir timestamp-microservicecd timestamp-microservice
```

La première étape lors du démarrage d'un nouveau projet Node est de l'initialiser avec un fichier `package.json`. Ce fichier contient certaines informations sur un projet, y compris son nom, sa description, son auteur et tous les packages dont il dépend. Voici la commande qui vous aide à créer un fichier `package.json` pour votre projet :

```
npm init
```

L'exécution de la commande ci-dessus ouvre une invite qui vous permet de saisir les informations pour des parties spécifiques de votre projet dans l'ordre suivant :

1. Le nom du projet.
2. La version initiale du projet.
3. La description du projet.
4. Le fichier d'entrée du projet.
5. La commande de test du projet.
6. Le dépôt git pour le projet,
7. Les mots-clés liés au projet.
8. La licence du projet.

Si vous êtes satisfait de la suggestion que la commande fournit à côté de chaque champ (entre crochets), appuyez simplement sur la touche Entrée pour l'accepter et passer au champ suivant jusqu'à ce que la commande se termine. Vous pouvez également utiliser `npm init -y` pour remplir rapidement un fichier `package.json` avec toutes les valeurs par défaut.

L'étape suivante consiste à créer un fichier `index.js` à la racine de votre répertoire de projet. C'est là que nous allons écrire le code pour ce projet.

```
touch index.js
```

Enfin, créez un dossier `views` à la racine de votre répertoire de projet. Ce dossier contiendra deux fichiers HTML : `index.html` et `404.html`.

```
mkdir viewstouch views/index.html views/404.html
```

Ouvrez le dossier du projet dans votre éditeur de texte préféré. Nous pouvons maintenant commencer à construire l'application.

![Image](https://cdn-media-1.freecodecamp.org/images/0*Ggd93PO-S1jpdPSG.png)

### Créer un serveur web HTTP

Ouvrez `index.js` et tapez le code suivant :

```
const http = require("http");
```

```
const requestHandler = (req, res) => {  console.log(req.url);  res.end('Hello world!');};
```

```
const server = http.createServer(requestHandler);
```

```
server.listen(process.env.PORT || 4100, err => {  if (err) throw err;
```

```
console.log(`Server running on PORT ${server.address().port}`);});
```

La première ligne nécessite le module `http` qui est fourni avec Node et le rend accessible via la variable `http`. Ensuite, nous utilisons la méthode `createServer` sur le module http pour créer une nouvelle instance d'un serveur HTTP qui est ensuite stockée dans la variable `server`.

Remarquez la fonction `requestHandler` créée sous la variable `http`. Cette fonction sera invoquée à chaque requête entrante vers le serveur web. Les arguments `req` et `res` sont des objets qui représentent la requête du client et la réponse du serveur, respectivement.

La méthode `listen` démarre le serveur et le fait écouter les connexions entrantes sur la variable d'environnement `PORT` (disponible sur l'objet `process.env`) ou `4100` s'il n'y a rien là. La fonction de rappel passée à la méthode `listen` s'exécutera lorsque le serveur démarrera. Si le port fourni est déjà pris, ou si le serveur ne peut pas démarrer pour une autre raison, une erreur est levée. Sinon, l'instruction `console.log()` est imprimée dans le terminal.

Vous pouvez démarrer le serveur en exécutant `node index.js` dans le terminal. Une fois votre serveur en cours d'exécution, visitez [http://localhost:4100](http://localhost:4100/) dans votre navigateur. Vous devriez voir les mots "Hello world!".

![Image](https://cdn-media-1.freecodecamp.org/images/0*3mSkpHq0pZ4fgr9B.png)

### Créer la route racine

Puisque le module `http` est très basique, il ne nous fournit pas de routeur. Nous devons donc vérifier manuellement l'URL pour décider quoi faire pour chaque route. Nous voulons fournir des instructions sur la façon d'utiliser le microservice d'horodatage une fois que la route racine est atteinte, comme dans la démo.

Nous pouvons faire cela en modifiant la fonction `requestHandler` comme ceci :

```
const requestHandler = (req, res) => {  if (req.url === "/") {    // Faire quelque chose  }};
```

Une simple instruction `if` peut nous aider à vérifier si l'URL de la requête entrante est exactement `/` et ensuite nous pouvons mettre la logique pour cette route entre les accolades. Dans ce cas, nous voulons retourner un peu de HTML expliquant comment fonctionne le microservice. Avant de continuer, copiez et collez ce qui suit dans le fichier `views/index.html` que nous avons créé précédemment et sauvegardez le fichier.

```
<!DOCTYPE html><html lang="en"><head>  <meta charset="UTF-8">  <meta name="viewport" content="width=device-width, initial-scale=1.0">  <meta http-equiv="X-UA-Compatible" content="ie=edge">  <title>Timestamp Microservice</title>  <style>    body {      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen-Sans, Ubuntu, Cantarell, 'Helvetica Neue', sans-serif;      color: #333;        background-color: #f6f6f6;    }
```

```
.container {      width: 100%;      max-width: 800px;      margin-left: auto;      margin-right: auto;    }
```

```
li {      margin-bottom: 10px;    }
```

```
li, p {      font-size: 18px;    }
```

```
code {      font-size: 90%;    }
```

```
a {      color: #006fc6;    }  </style></head><body>  <div class="container">    <h1>API Project: Timestamp Microservice</h1>    <h3>User Stories:</h1>    <ol class="user-stories">      <li>The API endpoint is <code>GET [project_url]/api/timestamp/:date_string</code></li>      <li>A date string is valid if can be successfully parsed by <code>new Date(date_string)</code>.<br>        Note that the unix timestamp needs to be an <strong>integer</strong> (not a string) specifying <strong>milliseconds</strong>.<br>        In our test we will use date strings compliant with ISO-8601 (e.g. <code>"2016-11-20"</code>) because this will ensure an UTC timestamp.</li>      <li>If the date string is <strong>empty</strong> it should be equivalent to trigger <code>new Date()</code>, i.e. the service uses the current timestamp.</li>      <li>If the date string is <strong>valid</strong> the api returns a JSON having the structure<br><code>{"unix": <date.getTime()>, "utc" : <date.toUTCString()> }</code><br>        e.g. <code>{"unix": 1479663089000 ,"utc": "Sun, 20 Nov 2016 17:31:29 GMT"}</code></li>      <li>If the date string is <strong>invalid</strong> the api returns a JSON having the structure <br>        <code>{"error" : "Invalid Date" }</code>.      </li>    </ol>
```

```
<h3>Example Usage:</h3>    <ul>      <li>        <a href="api/timestamp/2015-12-25">[project url]/api/timestamp/2015-12-25</a>      </li>      <li>        <a href="api/timestamp/1450137600000">[project url]/api/timestamp/1450137600</a>      </li>    </ul>
```

```
<h3>Example Output:</h3>    <p>      <code>{"unix":1451001600000, "utc":"Fri, 25 Dec 2015 00:00:00 GMT"}</code>    </p>  </div></body></html>
```

Comment envoyons-nous une réponse HTML au navigateur ? Nous pouvons utiliser le module intégré `fs` pour lire le fichier, puis envoyer le contenu du fichier au navigateur en utilisant l'argument `res` qui représente la réponse du serveur.

Exigez le module `fs` juste en dessous du module `http` comme montré ci-dessous :

```
const http = require("http");const fs = require("fs");
```

Ensuite, modifiez la fonction `requestHandler` pour qu'elle ressemble à ceci :

```
const requestHandler = (req, res) => {  if (req.url === "/") {    fs.readFile("views/index.html", "utf8", (err, html) => {      if (err) throw err;
```

```
res.writeHead(200, { "Content-Type": "text/html" });      res.end(html);    });  }};
```

La méthode `readFile()` lit de manière asynchrone le fichier fourni dans le premier argument (`views/index.html`) en utilisant l'encodage fourni (`utf8`), et exécute la fonction de rappel fournie. Si une erreur se produit lors de la lecture du fichier, une exception est levée. Sinon, le contenu du fichier devient disponible dans le deuxième argument de la fonction de rappel (`html`) dans ce cas.

Maintenant, nous pouvons envoyer le contenu de `html` au navigateur. Mais nous devons définir le [code de réponse HTTP](https://freshman.tech/http-status-codes/) ainsi que définir un en-tête de réponse pour indiquer au navigateur quel est le type de média du contenu retourné.

La méthode `writeHead()` sur l'objet de réponse du serveur est utilisée dans ce cas. Elle accepte le code de statut comme premier argument, et un objet représentant les en-têtes de réponse comme second. Nous avons défini l'en-tête `Content-Type` à `text/html` pour nous assurer que le navigateur interprète le contenu de notre réponse comme du HTML.

Ensuite, la méthode `end()` envoie le contenu du fichier `index.html` au navigateur dans le corps de la réponse et signale la fin de la réponse du serveur.

Pour essayer les nouvelles additions au code, vous devez arrêter le serveur avec Ctrl-C et le redémarrer en utilisant `node server.js`, puis rafraîchir votre navigateur. Vous devriez voir le html du fichier `views/index.html` sur la page.

### Configurer Nodemon pour redémarrer automatiquement le processus Node

Par défaut, vous devez tuer le processus du serveur et le redémarrer chaque fois que vous apportez une modification à votre code, mais il existe un moyen facile de contourner cela.

Vous devez installer un outil appelé [Nodemon](https://nodemon.io/) qui redémarre automatiquement le processus node chaque fois que votre code change. Vous pouvez installer cet outil globalement sur votre machine avec `npm` :

```
npm install -g nodemon
```

Une fois Nodemon installé, tuez le processus du serveur et redémarrez-le avec `nodemon index.js`. Maintenant, le serveur web sera redémarré automatiquement chaque fois que vous apporterez une modification à votre code. Plutôt pratique, non ?

L'étape suivante consiste à configurer une route pour le microservice d'horodatage. Selon l'histoire utilisateur #1, ce service doit être disponible sous `/api/timestamp/:date_string?` où `:date_string?` représente la chaîne de date qui sera passée au service.

Modifiez votre fichier `index.js` pour qu'il ressemble à ceci :

```
// déclarations require
```

```
const getTimestamp = date => ({  unix: date.getTime(),  utc: date.toUTCString()});
```

```
const requestHandler = (req, res) => {  if (req.url === "/") {    fs.readFile("views/index.html", (err, html) => {      if (err) throw err;
```

```
res.writeHead(200, { "Content-Type": "text/html" });      res.end(html);    });  } else if (req.url.startsWith("/api/timestamp")) {    const dateString = req.url.split("/api/timestamp/")[1];    let timestamp;
```

```
if (dateString === undefined || dateString.trim() === "") {      timestamp = getTimestamp(new Date());    } else {      const date = !isNaN(dateString)        ? new Date(parseInt(dateString))        : new Date(dateString);
```

```
if (!isNaN(date.getTime())) {        timestamp = getTimestamp(date);      } else {        timestamp = {          error: "invalid date"        };      }    }
```

```
res.writeHead(200, { "Content-Type": "application/json" });    res.end(JSON.stringify(timestamp));  }};
```

```
// reste du fichier
```

Je sais que c'est beaucoup de code à traiter, alors laissez-moi vous guider à travers cela bit par bit. Nous avons une instruction `else if` dans `requestHandler` qui vérifie si l'URL de la requête commence par `/api/timstamp`. Si c'est le cas, nous divisons l'URL de la requête en deux et récupérons la partie `dateString` du tableau résultant.

Si `dateString` est `undefined` ou une chaîne vide, cela signifie qu'aucune chaîne de date n'a été fournie dans la requête. L'histoire utilisateur #3 dicte que nous traitons cette situation comme si la date actuelle avait été demandée, et c'est ce que fait `getTimestamp(new Date())`.

Si une `dateString` existe, nous devons vérifier si elle est un horodatage unix ou une chaîne de date ISO-8601 (comme "2018-11-22") afin que nous puissions décider si nous devons passer un nombre ou une chaîne à `new Date()`. Notez que si vous passez un horodatage unix comme une chaîne à `new Date()`, vous obtiendrez un résultat invalide. C'est pourquoi cette étape est nécessaire.

Ensuite, nous vérifions si l'objet date stocké dans la variable `date` est valide. Si c'est le cas, nous obtenons l'objet timestamp comme avant, sinon nous définissons la variable `timestamp` à la structure pour les dates invalides comme spécifié dans l'histoire utilisateur #5.

La dernière étape consiste à envoyer le contenu de la variable `timestamp` au navigateur. Dans ce cas, nous définissons l'en-tête `Content-Type` à `application/json` afin que le corps de la réponse soit correctement interprété comme du JSON. Nous nous assurons également que nous envoyons une valeur JSON valide en appelant `JSON.stringify(timestamp)` et en passant la sortie à la méthode `end`.

Maintenant, testez l'application en passant une chaîne de date valide ou un horodatage unix après `/api/timestamp/` ou laissez la chaîne de date vide pour obtenir une réponse JSON pour la date actuelle. Vous pouvez également essayer de passer une chaîne de date invalide pour confirmer que le service la reconnaît comme une date invalide.

### Implémenter une page 404

Nous avons terminé toutes les histoires utilisateur pour cette application, mais il y a une dernière chose que je voudrais que nous fassions. Si le navigateur demande une URL qui n'est pas `/` ou ne commence pas par `/api/timestamp`, nous devons configurer le serveur pour envoyer une réponse 404 au navigateur.

Tout d'abord, remplissez le fichier `views/404.html` avec le code suivant :

```
<!DOCTYPE html><html lang="en"><head>  <meta charset="UTF-8">  <meta name="viewport" content="width=device-width, initial-scale=1.0">  <meta http-equiv="X-UA-Compatible" content="ie=edge">  <title>404 Not found</title></head><body>  <h1>undefined is, unfortunately, not a function</h1>  <p>You just 404'd. Maybe you should head back to the <a href="/">homepage</a>.</p><script></script></body></html>
```

Ensuite, modifiez la fonction `requestHandler` dans `index.js` pour qu'elle ressemble à ceci :

```
const requestHandler = (req, res) => {  if (req.url === "/") {    fs.readFile("views/index.html", (err, html) => {      if (err) throw err;
```

```
res.writeHead(200, { "Content-Type": "text/html" });      res.end(html);    });  } else if (req.url.startsWith("/api/timestamp")) {    const dateString = req.url.split("/api/timestamp/")[1];    let timestamp;
```

```
if (dateString === undefined || dateString.trim() === "") {      timestamp = getTimestamp(new Date());    } else {      const date = !isNaN(dateString)        ? new Date(parseInt(dateString))        : new Date(dateString);
```

```
if (!isNaN(date.getTime())) {        timestamp = getTimestamp(date);      } else {        timestamp = {          error: "invalid date"        };      }    }
```

```
res.writeHead(200, { "Content-Type": "application/json" });    res.end(JSON.stringify(timestamp));  } else {    fs.readFile("views/404.html", (err, html) => {      if (err) throw err;
```

```
res.writeHead(404, { "Content-Type": "text/html" });      res.end(html);    });  }};
```

J'ai ajouté un bloc `else` final à la fin de la fonction `requestHandler` qui lit le contenu du fichier `views/404.html` et l'envoie au navigateur pour toute URL qui ne correspond pas à `/` ou `/api/timestamp/:date_string?`.

Essayez-le. Entrez une URL comme [http://localhost:4100/foo](http://localhost:4100/foo) dans votre navigateur et confirmez que cela fonctionne !

![Image](https://cdn-media-1.freecodecamp.org/images/0*DINnMaqPyMchmBQY.png)

### Déployer sur Heroku

À quoi bon un microservice d'horodatage si personne ne peut l'utiliser ? Partageons-le avec le monde en le déployant sur [Heroku](https://heroku.com/).

La première étape consiste à [s'inscrire pour un compte Heroku gratuit](https://signup.heroku.com/). Une fois votre compte activé, [suivez ce lien](https://dashboard.heroku.com/new-app?org=personal-apps) pour créer une nouvelle application. Donnez-lui un nom unique. J'ai appelé le mien "ayo-timestamp".

Une fois votre application créée, [suivez les instructions ici](https://devcenter.heroku.com/articles/heroku-command-line) pour installer l'interface de ligne de commande Heroku sur votre machine. Ensuite, exécutez la commande `heroku login` dans le terminal pour vous connecter à votre compte Heroku.

Assurez-vous d'avoir initialisé un dépôt git pour votre projet. Si ce n'est pas le cas, exécutez la commande `git init` à la racine de votre répertoire de projet, puis exécutez la commande ci-dessous pour définir heroku comme un dépôt distant pour votre dépôt git. Remplacez `<app name>` par le nom de votre application.

```
heroku git:remote -a <app name>
```

Ensuite, créez un `Procfile` à la racine de votre répertoire de projet (`touch Procfile`) et collez le contenu suivant :

```
web: node index.js
```

Ensuite, spécifiez la version de Node que vous exécutez dans votre fichier `package.json` sous la clé `engines`. J'ai spécifié la version `10.9.0` puisque c'est la version que j'exécute sur mon ordinateur. Vous devriez changer cette valeur pour correspondre à la version de Node que vous avez sur votre machine.

```
{  "name": "timestamp-microservice",  "version": "1.0.0",  "description": "",  "main": "index.js",  "scripts": {    "test": "echo \"Error: no test specified\" && exit 1"  },  "keywords": [],  "author": "Ayo Isaiah",  "license": "MIT",  "engines": {    "node": "10.9.0"  }}
```

Enfin, validez votre code et poussez-le vers le dépôt distant Heroku en utilisant les commandes suivantes :

```
git add .git commit -m "Initial commit"git push heroku master
```

Une fois le processus de déploiement terminé, vous pouvez ouvrir `https://<your-app-name>.heroku.com` pour voir et tester votre projet.

### Conclusion

Nous avons réussi à construire un microservice d'horodatage en utilisant uniquement des modules Node intégrés, et nous l'avons déployé sur Heroku. Pour être sûr, utiliser des frameworks web comme [Express](https://expressjs.com/) est plus facile et plus pratique pour les applications non triviales, mais vous serez un bien meilleur développeur Node si vous êtes au moins un peu familier avec sa bibliothèque standard avant de voir ce que la communauté a à offrir.

J'ai un autre tutoriel qui couvre la [construction d'un site web Node.js](http://localhost:5000/learn-node/) en utilisant Express comme serveur web et [Pug](https://pugjs.org/) pour le templating. Vous pouvez le consulter si vous voulez plus de pratique avec la construction de projets Node et [vous abonner à ma newsletter](http://localhost:5000/newsletter/) pour être informé lorsque je publie de nouveaux tutoriels.

_Publié à l'origine sur [freshman.tech](https://freshman.tech/microservice/) le 22 novembre 2018._