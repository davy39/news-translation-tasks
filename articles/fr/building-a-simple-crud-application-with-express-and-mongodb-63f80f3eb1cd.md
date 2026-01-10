---
title: Création d'une application CRUD simple avec Express et MongoDB
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-01-26T06:50:38.000Z'
originalURL: https://freecodecamp.org/news/building-a-simple-crud-application-with-express-and-mongodb-63f80f3eb1cd
coverImage: https://cdn-media-1.freecodecamp.org/images/1*umzW9eAqELBCuo458Rzdcw.jpeg
tags:
- name: education
  slug: education
- name: learning to code
  slug: learning-to-code
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: Création d'une application CRUD simple avec Express et MongoDB
seo_desc: 'By Zell Liew

  For a long time, I didn’t dare venture into back end development. I felt intimidated
  because of my lack of an academic background in programming.

  I remember when I eventually built up the courage to try back end development. I
  had such a...'
---

Par Zell Liew

Pendant longtemps, je n'ai pas osé me lancer dans le développement back-end. Je me sentais intimidé par mon manque de formation académique en programmation.

Je me souviens quand j'ai finalement trouvé le courage d'essayer le développement back-end. J'ai eu tant de mal à comprendre la documentation pour Express, MongoDB et Node.js que j'ai abandonné.

J'y suis finalement retourné et j'ai travaillé à clarifier ma confusion. Maintenant, un an plus tard, j'ai compris comment travailler avec ces outils. J'ai donc décidé d'écrire ce tutoriel complet pour que vous n'ayez pas à subir le même mal de tête que j'ai traversé.

### CRUD, Express et MongoDB

CRUD, Express et MongoDB sont de grands mots pour une personne qui n'a jamais touché à la programmation côté serveur de sa vie. Introduisons rapidement ce qu'ils sont avant de plonger dans le tutoriel.

[**Express**](http://www.google.com/) est un framework pour construire des applications web sur Node.js. Il simplifie le processus de création de serveur qui est déjà disponible dans Node. Au cas où vous vous poseriez la question, Node vous permet d'utiliser JavaScript comme langage côté serveur.

[**MongoDB**](https://www.mongodb.org/) est une base de données. C'est l'endroit où vous stockez les informations pour vos sites web (ou applications).

[**CRUD**](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) est un acronyme pour Create, Read, Update et Delete. C'est un ensemble d'opérations que nous demandons aux serveurs d'exécuter (POST, GET, PUT et DELETE respectivement). Voici ce que fait chaque opération :

* **Create (POST)** — Créer quelque chose
* **Read (GET)** — Obtenir quelque chose
* **Update (PUT)** — Changer quelque chose
* **Delete (DELETE)** — Supprimer quelque chose

Si nous mettons CRUD, Express et MongoDB ensemble dans un seul diagramme, voici à quoi cela ressemblerait :

![Image](https://cdn-media-1.freecodecamp.org/images/0*UKwrPtpRSGFiDomm.png)

CRUD, Express et MongoDB ont-ils plus de sens pour vous maintenant ?

Super. Continuons.

### Ce que nous construisons

Nous allons construire une application simple de liste qui vous permet de garder une trace des choses dans une liste (comme une liste de tâches, par exemple).

Bon, une liste de tâches est un peu ennuyeuse. Que diriez-vous de faire une liste de citations de personnages de Star Wars à la place ? Génial, n'est-ce pas ? N'hésitez pas à jeter un coup d'œil rapide à la [démo](https://crud-express-mongo.herokuapp.com/) avant de continuer avec le tutoriel. De plus, [c'est ici](https://github.com/zellwk/crud-express-mongo) que vous pouvez trouver le code final de l'application.

Au fait, ce que nous construisons n'est pas une application sexy sur une seule page. Nous nous concentrons principalement sur l'utilisation de CRUD, Express et MongoDB dans ce tutoriel, donc plus de choses côté serveur. Je ne vais pas insister sur le style.

Vous aurez besoin de deux choses pour commencer ce tutoriel :

1. Vous ne devriez pas avoir peur de taper des commandes dans un shell. Consultez [cet article](http://www.zell-weekeat.com/fear-of-command-line/) si c'est actuellement votre cas.
2. Vous devez avoir [Node](https://nodejs.org/) installé.

Pour vérifier si vous avez Node installé, ouvrez votre ligne de commande et exécutez le code suivant :

```
$ node -v
```

Vous devriez obtenir un numéro de version si vous avez Node installé. Si ce n'est pas le cas, vous pouvez installer Node soit en téléchargeant l'installateur depuis [le site web de Node](https://nodejs.org/), soit en le téléchargeant via des gestionnaires de paquets comme [Homebrew](http://brew.sh/) (Mac) et [Chocolatey](https://chocolatey.org/) (Windows).

### Getting started

Commencez par créer un dossier pour ce projet. N'hésitez pas à l'appeler comme vous le souhaitez. Une fois que vous y êtes, exécutez la commande npm init.

Cette commande crée un fichier package.json qui vous aide à gérer les dépendances que nous installerons plus tard dans le tutoriel.

```
$ npm init
```

Il suffit de presser Entrée pour tout ce qui apparaît. Je parlerai de ceux que vous devez connaître au fur et à mesure.

### Exécuter Node pour la première fois de votre vie

La manière la plus simple d'utiliser Node est d'exécuter la commande node et de spécifier un chemin vers un fichier. Créons un fichier appelé server.js pour exécuter Node.

```
$ touch server.js
```

Lorsque nous exécutons le fichier server.js, nous voulons nous assurer qu'il fonctionne correctement. Pour ce faire, il suffit d'écrire une instruction console.log dans server.js :

```
console.log('May Node be with you')
```

Maintenant, exécutez node server.js dans votre ligne de commande et vous devriez voir l'instruction que vous avez enregistrée :

![Image](https://cdn-media-1.freecodecamp.org/images/0*82cfsJUuV4b0Mmn2.png)

Super. Continuons et apprenons comment utiliser Express maintenant.

### Utiliser Express

Nous devons d'abord installer Express avant de pouvoir l'utiliser dans notre application. L'installation d'Express est assez facile. Tout ce que nous avons à faire est d'exécuter une commande d'installation avec le gestionnaire de paquets Node (npm), qui est fourni avec Node.

Exécutez la commande npm install express --save dans votre ligne de commande :

```
$ npm install express --save
```

Une fois terminé, vous devriez voir que npm a enregistré Express comme une dépendance dans package.json.

![Image](https://cdn-media-1.freecodecamp.org/images/0*WQ2iauA--9SEqja3.png)

Ensuite, nous utilisons express dans server.js en le requérant.

```
const express = require('express');const app = express();
```

La première chose que nous voulons faire est de créer un serveur où les navigateurs peuvent se connecter. Nous pouvons le faire avec l'aide d'une méthode listen fournie par Express :

```
app.listen(3000, function() {  console.log('listening on 3000')})
```

Maintenant, exécutez node server.js et naviguez vers localhost:3000 sur votre navigateur. Vous devriez voir un message qui dit « cannot get / ».

![Image](https://cdn-media-1.freecodecamp.org/images/0*HuIZ1G3D7TMPjbdU.png)

C'est un bon signe. Cela signifie que **nous pouvons maintenant communiquer avec notre serveur Express via le navigateur**. C'est ici que nous commençons les opérations CRUD.

### CRUD — READ

L'opération **READ** est effectuée par les navigateurs chaque fois que vous visitez une page web. En coulisses, les navigateurs envoient une requête **GET** au serveur pour effectuer une opération READ. La raison pour laquelle nous voyons l'erreur « cannot get / » est que nous n'avons pas encore envoyé quoi que ce soit au navigateur depuis notre serveur.

Dans Express, nous gérons une requête **GET** avec la méthode get :

```
app.get(path, callback)
```

**Le premier argument, path**, est le chemin de la requête GET. C'est tout ce qui vient après votre nom de domaine.

Lorsque nous visitons localhost:3000, nos navigateurs cherchent en réalité localhost:3000/. L'argument path dans ce cas est /.

**Le deuxième argument est une fonction de rappel** qui indique au serveur quoi faire lorsque le chemin est trouvé. Elle prend deux arguments, un objet de requête et un objet de réponse :

```
app.get('/', function (request, response) {  // faire quelque chose ici})
```

Pour l'instant, écrivons « Hello World » en retour au navigateur. Nous le faisons en utilisant une méthode send qui vient avec l'objet de réponse :

```
app.get('/', function(req, res) {  res.send('Hello World')})// Note : request et response sont généralement écrits req et res respectivement.
```

Je vais commencer à écrire en code ES6 et vous montrer comment convertir en ES6 en cours de route également. Tout d'abord, je remplace function() par la [fonction fléchée ES6](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Functions/Arrow_functions). Le code ci-dessous est le même que le code ci-dessus :

```
app.get('/', (req, res) => {  res.send('hello world')})
```

Maintenant, redémarrez votre serveur en faisant ce qui suit :

1. Arrêtez le serveur actuel en appuyant sur CTRL + C dans la ligne de commande.
2. Exécutez à nouveau node server.js.

Ensuite, naviguez vers localhost:3000 sur votre navigateur. Vous devriez pouvoir voir une chaîne qui dit « Hello World ».

![Image](https://cdn-media-1.freecodecamp.org/images/0*jBDbdhi2v2N82RvP.png)

Super. Changeons notre application pour servir une page index.html au navigateur à la place. Pour ce faire, nous utilisons la méthode sendFile fournie par l'objet res.

```
app.get('/', (req, res) => {  res.sendFile(__dirname + '/index.html')  // Note : __dirname est le chemin vers votre répertoire de travail actuel. Essayez de le logger et voyez ce que vous obtenez !   // Le mien était '/Users/zellwk/Projects/demo-repos/crud-express-mongo' pour cette application.})
```

Dans la méthode sendFile ci-dessus, nous avons dit à Express de servir un fichier index.html qui peut être trouvé à la racine de votre dossier de projet. Nous n'avons pas encore ce fichier. Créons-le maintenant.

```
touch index.html
```

Ajoutons également du texte dans notre fichier index.html :

```
<!DOCTYPE html><html lang="en"><head>  <meta charset="UTF-8">  <title>MY APP</title></head><body>  May Node and Express be with you.   </body></html>
```

Redémarrez votre serveur et actualisez votre navigateur. Vous devriez pouvoir voir les résultats de votre fichier HTML maintenant.

![Image](https://cdn-media-1.freecodecamp.org/images/0*oisDzT819Ex3FtDs.png)

C'est ainsi qu'Express gère une requête **GET** (opération **READ**) en un mot.

À ce stade, vous avez probablement réalisé que vous devez redémarrer votre serveur chaque fois que vous apportez une modification à server.js. Ce processus est incroyablement fastidieux, alors prenons une petite pause et simplifions-le en utilisant un package appelé [nodemon](http://nodemon.io/).

### Entrée de Nodemon

**Nodemon redémarre le serveur automatiquement** chaque fois que vous enregistrez un fichier utilisé par le serveur. Nous pouvons installer Nodemon en utilisant la commande suivante :

```
$ npm install nodemon --save-dev
```

Note : La raison pour laquelle nous utilisons un drapeau --save-dev ici est que nous utilisons Nodemon uniquement lorsque nous développons. Ce drapeau enregistrera Nodemon comme une devDependency dans votre fichier package.json.

Ensuite, Nodemon se comporte exactement comme node, ce qui signifie que nous pouvons exécuter notre serveur en appelant nodemon server.js. Cependant, nous ne pouvons pas le faire dans la ligne de commande pour l'instant car Nodemon n'est pas installé avec un drapeau -g.

Il y a une autre façon d'exécuter Nodemon — nous pouvons exécuter Nodemon depuis le dossier node_modules. Le code ressemble à ceci :

```
$ ./node_modules/.bin/nodemon server.js
```

C'est un peu long à taper. Une façon de le simplifier est de créer une clé de script dans package.json.

```
{  // ...   "scripts": {    "dev": "nodemon server.js"  }  // ...}
```

Maintenant, vous pouvez exécuter npm run dev pour déclencher nodemon server.js.

Revenons au sujet principal. Nous allons couvrir l'opération **CREATE** ensuite.

### CRUD — CREATE

L'opération **CREATE** est effectuée uniquement par le navigateur si une requête **POST** est envoyée au serveur. Cette requête POST peut être déclenchée soit avec JavaScript, soit via un élément <form>.

Découvrons comment utiliser un élément <form> pour créer de nouvelles entrées pour notre application de citations de Star Wars pour cette partie du tutoriel.

Pour ce faire, vous devez d'abord créer un élément <form> et l'ajouter à votre fichier index.html. Vous avez besoin de trois choses sur cet élément de formulaire :

1. Un attribut action
2. Un attribut method
3. Et des attributs name sur tous les éléments <input> dans le formulaire

```
<form action="/quotes" method="POST">  <input type="text" placeholder="name" name="name">  <input type="text" placeholder="quote" name="quote">  <button type="submit">Submit</button></form>
```

L'attribut action indique au navigateur où naviguer dans notre application Express. Dans ce cas, nous naviguons vers /quotes. L'attribut method indique au navigateur quelle requête envoyer. Dans ce cas, il s'agit d'une requête POST.

Sur notre serveur, nous pouvons gérer cette requête POST avec une méthode post fournie par Express. Elle prend les mêmes arguments que la méthode GET :

```
app.post('/quotes', (req, res) => {  console.log('Hellooooooooooooooooo!')})
```

Redémarrez votre serveur (espérons que vous avez configuré Nodemon pour qu'il redémarre automatiquement) et actualisez votre navigateur. Ensuite, entrez quelque chose dans votre élément de formulaire. Vous devriez pouvoir voir Hellooooooooooooooooo! dans votre ligne de commande.

![Image](https://cdn-media-1.freecodecamp.org/images/0*qsLmf8vEhBlhIfJj.png)

Super, nous savons qu'Express gère le formulaire pour nous en ce moment. La question suivante est, comment obtenons-nous les valeurs d'entrée avec Express ?

Il s'avère qu'Express ne gère pas la lecture des données de l'élément <form> par lui-même. Nous devons ajouter un autre package appelé [body-parser](https://www.npmjs.com/package/body-parser) pour obtenir cette fonctionnalité.

```
$ npm install body-parser --save
```

Express nous permet d'ajouter des middlewares comme body-parser à notre application avec la méthode use. Vous entendrez souvent le terme middleware lorsque vous traiterez avec Express. Ces éléments sont essentiellement des plugins qui modifient l'objet de requête ou de réponse avant qu'ils ne soient traités par notre application. **Assurez-vous de placer body-parser avant vos gestionnaires CRUD !**

```
const express = require('express')const bodyParser= require('body-parser')const app = express()
```

```
app.use(bodyParser.urlencoded({extended: true}))
```

```
// Tous vos gestionnaires ici...
```

La méthode urlencoded dans body-parser indique à body-parser d'extraire les données de l'élément <form> et de les ajouter à la propriété body dans l'objet de requête.

Maintenant, vous devriez pouvoir voir tout dans le champ du formulaire dans l'objet req.body. Essayez de faire un console.log et voyez ce que c'est !

```
app.post('/quotes', (req, res) => {  console.log(req.body)})
```

Vous devriez pouvoir obtenir un objet similaire à ce qui suit dans votre ligne de commande :

![Image](https://cdn-media-1.freecodecamp.org/images/0*cmNU6GQhNS7BYsLT.png)

Hmmm. Maître Yoda a parlé ! Assurons-nous de nous souvenir des mots de Yoda. C'est important. Nous voulons pouvoir le récupérer la prochaine fois que nous chargeons notre page d'index.

Entrez la base de données, MongoDB.

### MongoDB

Nous devons d'abord installer MongoDB via npm si nous voulons l'utiliser comme base de données.

```
npm install mongodb --save
```

Une fois installé, nous pouvons nous connecter à MongoDB via la méthode connect de Mongo.Client comme montré dans le code ci-dessous :

```
const MongoClient = require('mongodb').MongoClient
```

```
MongoClient.connect('link-to-mongodb', (err, database) => {  // ... start the server})
```

La partie suivante consiste à obtenir le lien correct vers notre base de données. La plupart des gens stockent leurs bases de données sur des services cloud comme [MongoLab](https://mongolab.com/). Nous allons faire de même.

Alors, allez-y et créez un compte avec MongoLab. (C'est gratuit). Une fois que vous avez terminé, créez un nouveau déploiement MongoDB et définissez le plan sur sandbox.

![Image](https://cdn-media-1.freecodecamp.org/images/0*YujCEhVovfSgPH_j.png)

Une fois que vous avez terminé la création du déploiement, allez-y et créez un utilisateur de base de données et un mot de passe de base de données. **Souvenez-vous de l'utilisateur de la base de données et du mot de passe de la base de données** car vous allez l'utiliser pour connecter la base de données que vous venez de créer.

![Image](https://cdn-media-1.freecodecamp.org/images/0*pPeHMc1EqlQRAqKU.png)

Enfin, récupérez l'URL MongoDB et ajoutez-la à votre méthode MongoClient.connect. Assurez-vous d'utiliser votre utilisateur de base de données et votre mot de passe !

![Image](https://cdn-media-1.freecodecamp.org/images/0*x5a1AplcCRyq712P.png)

```
MongoClient.connect('your-mongodb-url', (err, database) => {  // ... do something here})
```

Ensuite, nous voulons démarrer nos serveurs uniquement lorsque la base de données est connectée. Par conséquent, déplaçons app.listen dans la méthode connect. Nous allons également créer une variable db pour nous permettre d'utiliser la base de données lorsque nous traitons les requêtes du navigateur.

```
var db
```

```
MongoClient.connect('your-mongodb-url', (err, database) => {  if (err) return console.log(err)  db = database  app.listen(3000, () => {    console.log('listening on 3000')  })})
```

Nous avons terminé la configuration de MongoDB. Maintenant, créons une collection de citations pour stocker les citations de notre application.

Au fait, **une collection est un emplacement nommé pour stocker des choses**. Vous pouvez créer autant de collections que vous le souhaitez. Cela peut être des choses comme « produits », « citations », « courses », ou toute autre étiquette que vous choisissez.

Nous pouvons créer la collection de citations en utilisant la chaîne quotes lors de l'appel de la méthode db.collection() de MongoDB. Tout en créant la collection de citations, nous pouvons également enregistrer notre première entrée dans MongoDB avec la méthode save simultanément.

**Une fois que nous avons terminé l'enregistrement, nous devons rediriger l'utilisateur quelque part** (ou il sera bloqué en attendant éternellement que notre serveur bouge). Dans ce cas, nous allons les rediriger vers /, ce qui provoque le rechargement de leurs navigateurs.

```
app.post('/quotes', (req, res) => {  db.collection('quotes').save(req.body, (err, result) => {    if (err) return console.log(err)
```

```
    console.log('saved to database')    res.redirect('/')  })})
```

Maintenant, si vous entrez quelque chose dans l'élément <form>, vous pourrez voir une entrée dans votre collection MongoDB.

![Image](https://cdn-media-1.freecodecamp.org/images/0*XEGKefxWJP6SlQpM.png)

Whoohoo ! Puisque nous avons déjà quelques citations dans la collection, pourquoi ne pas essayer de les montrer à notre utilisateur lorsqu'il arrive sur notre page ?

### Afficher les citations aux utilisateurs

Nous devons faire deux choses pour montrer les citations stockées dans MongoLab à nos utilisateurs.

1. Obtenir les citations de MongoLab
2. Utiliser un moteur de template pour afficher les citations

Allons-y étape par étape.

Nous pouvons obtenir les citations de MongoLab en utilisant la méthode find disponible dans la méthode de collection.

```
app.get('/', (req, res) => {  var cursor = db.collection('quotes').find()})
```

La méthode find retourne un curseur (un objet Mongo) qui ne fait probablement pas sens si vous le console.log.

![Image](https://cdn-media-1.freecodecamp.org/images/0*IQHvKZ7Bd5mIlxT0.png)

La bonne nouvelle est que cet objet curseur contient toutes les citations de notre base de données. Il contient également un ensemble d'autres propriétés et méthodes qui nous permettent de travailler facilement avec les données. Une telle méthode est la méthode toArray.

**La méthode toArray** prend une fonction de rappel qui nous permet de faire des choses avec les citations que nous avons récupérées de MongoLab. Essayons de faire un console.log() pour les résultats et voyons ce que nous obtenons !

```
db.collection('quotes').find().toArray(function(err, results) {  console.log(results)  // send HTML file populated with quotes here})
```

![Image](https://cdn-media-1.freecodecamp.org/images/0*6McLqpFyG1xA5of1.png)

Super ! Vous voyez maintenant un tableau de citations (j'en ai seulement une pour l'instant). Nous avons terminé la première partie — obtenir des données de MongoLab. La partie suivante consiste à générer un HTML qui contient toutes nos citations.

Nous ne pouvons pas servir notre fichier index.html et nous attendre à ce que les citations apparaissent magiquement car il n'y a aucun moyen d'ajouter du contenu dynamique à un fichier HTML. Ce que nous pouvons faire à la place, c'est utiliser des moteurs de template pour nous aider. Certains moteurs de template populaires incluent Jade, Embedded JavaScript et Nunjucks.

J'ai écrit abondamment sur le comment et le pourquoi des moteurs de template dans un [article séparé](http://www.zell-weekeat.com/nunjucks-with-gulp/). Vous pourriez vouloir le consulter si vous n'avez aucune idée de ce que sont les moteurs de template. Personnellement, j'utilise (et recommande) Nunjucks comme mon moteur de template de choix. N'hésitez pas à consulter l'article pour savoir pourquoi.

Pour ce tutoriel, nous allons utiliser [Embedded JavaScript](http://www.embeddedjs.com/) (ejs) comme moteur de template car c'est le plus facile à commencer. Vous le trouverez familier dès le départ puisque vous connaissez déjà HTML et JavaScript.

Nous pouvons utiliser EJS en l'installant d'abord, puis en définissant le moteur de vue dans Express sur ejs.

```
$ npm install ejs --save
```

```
app.set('view engine', 'ejs')
```

Une fois le moteur de vue défini, nous pouvons commencer à générer le HTML avec nos citations. Ce processus est également appelé **rendering**. Nous pouvons utiliser l'objet render intégré dans l'objet de réponse pour le faire. Il a la syntaxe suivante :

```
res.render(view, locals)
```

**Le premier paramètre, views**, est le nom du fichier que nous rendons. Ce fichier doit être placé dans un dossier views.

**Le deuxième paramètre, locals**, est un objet qui passe des données dans la vue.

Créons d'abord un fichier index.ejs dans le dossier views pour que nous puissions commencer à peupler les données.

```
$ mkdir views$ touch views/index.ejs
```

Maintenant, placez le code suivant dans index.ejs.

```
<ul class="quotes">  <% for(var i=0; i<quotes.length; i++) {%>    <li class="quote">      <span><%= quotes[i].name %></span>      <span><%= quotes[i].quote %></span>    </li>  <% } %></ul>
```

Vous voyez ce que je veux dire quand je dis que vous le trouverez familier ? Dans EJS, vous pouvez écrire du JavaScript dans les balises <% et %>. Vous pouvez également sortir du JavaScript sous forme de chaînes si vous utilisez les balises <%= et %>.

Ici, vous pouvez voir que nous parcourons essentiellement le tableau de citations et créons des chaînes avec quotes[i].name et quotes[i].quote.

Une dernière chose à faire avant de passer du fichier index.ejs. N'oubliez pas de copier l'élément <form> du fichier index.html dans ce fichier également. Le fichier index.ejs complet jusqu'à présent devrait être :

```
<!DOCTYPE html><html lang="en"><head>  <meta charset="UTF-8">  <title>MY APP</title></head><body>  May Node and Express be with you.
```

```
  <ul class="quotes">  <% for(var i=0; i<quotes.length; i++) {%>    <li class="quote">      <span><%= quotes[i].name %></span>      <span><%= quotes[i].quote %></span>    </li>  <% } %>  </ul>
```

```
  <form action="/quotes" method="POST">    <input type="text" placeholder="name" name="name">    <input type="text" placeholder="quote" name="quote">    <button type="submit">Submit</button>  </form></body></html>
```

Enfin, nous devons rendre ce fichier index.ejs lors de la gestion de la requête **GET**. Ici, nous définissons les résultats (un tableau) comme le tableau de citations que nous avons utilisé dans index.ejs ci-dessus.

```
app.get('/', (req, res) => {  db.collection('quotes').find().toArray((err, result) => {    if (err) return console.log(err)    // renders index.ejs    res.render('index.ejs', {quotes: result})  })})
```

Maintenant, actualisez votre navigateur et vous devriez pouvoir voir les citations de Maître Yoda.

![Image](https://cdn-media-1.freecodecamp.org/images/0*Wy8S2Yag15rpIOlt.png)

Um. Vous n'avez peut-être qu'une seule citation si vous avez suivi le tutoriel étape par étape jusqu'à ce point. La raison pour laquelle j'ai plusieurs citations est que j'en ai silencieusement ajouté plus en travaillant sur l'application.

### Conclusion

Nous avons couvert beaucoup de terrain en seulement 3000 mots. Voici quelques points pour tout résumer. Vous avez...

* Créé un serveur Express
* Appris à exécuter les opérations CREATE et READ
* Appris à sauvegarder et lire depuis MongoDB
* Appris à utiliser un moteur de template comme Embedded JS.

Il reste deux opérations à couvrir, mais nous les laisserons pour le [prochain article](http://www.zell-weekeat.com/crud-express-and-mongodb-2/). À bientôt !

Cet article est d'abord apparu sur mon blog à l'adresse [www.zell-weekeat.com](http://zell-weekeat.com). Consultez-le si vous voulez plus d'articles comme celui-ci.