---
title: Comment utiliser le templating EJS dans une application Node.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-04-03T14:59:47.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-ejs-templating-in-a-node-js-application-ea9347a96c65
coverImage: https://cdn-media-1.freecodecamp.org/images/1*TDMS2SG4EjQuDsRPDDh50w.png
tags:
- name: ejs
  slug: ejs
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: Comment utiliser le templating EJS dans une application Node.js
seo_desc: 'By Jennifer Bland

  EJS, embedded javascript, is a templating language. EJS combines data and a template
  to produce HTML. One of the most important features in EJS is its use of partials.
  Partials allow you to define something once, and then apply it t...'
---

Par Jennifer Bland

EJS, JavaScript intégré, est un langage de templating. EJS combine des données et un template pour produire du HTML. L'une des fonctionnalités les plus importantes d'EJS est son utilisation des partials. Les partials vous permettent de définir quelque chose une fois, puis de l'appliquer à n'importe quelle page de votre application.

Je vais vous montrer comment créer une application Node.js simple qui utilise EJS comme moteur de templating. Ensuite, nous créerons 2 pages pour un site web. Nous utiliserons des partials pour construire notre head, navigation, footer et contenu.

[Vous pouvez obtenir le code pour cet exemple sur github](https://github.com/ratracegrad/nodejs_ejs_boilerplate)

#### Structure des fichiers

Nous allons créer une application d'exemple qui aura deux pages : index et about.

Voici la structure des fichiers pour l'application que nous allons créer.

```
public — style.css
routes — index.js
views — pages — about.ejs — index.ejs
partials — 3columns.ejs — footer.ejs — head.ejs — nav.ejs — scripts.ejs
package.json
server.js
```

#### Mise en route

Nous allons configurer notre package.json en premier. Ce fichier contiendra tous les modules que nous utiliserons dans notre application. Nous allons utiliser :

* express
* ejs

```
{
  "name": "node_ejs_boilerplate",
  "version": "1.0.0",
  "description": "Boilerplate montrant l'utilisation de ejs comme moteur de template de vue dans une application Node.js",
  "author": "Jennifer Bland",
  "main": "server.js",
  "dependencies": {
    "ejs": "^2.4.1",
    "express": "^4.13.4"
  }
}
```

Vous pouvez ajouter les dépendances directement dans votre package.json ou vous pouvez installer les dépendances afin qu'elles soient automatiquement ajoutées au package.json. Pour installer manuellement les dépendances, entrez cette commande :

```
npm install express ejs --save
```

Si vous avez ajouté des dépendances en les ajoutant à votre package.json, vous devrez les installer en utilisant cette commande :

```
npm install
```

#### Server.js

Maintenant que nous avons toutes nos dépendances installées, nous devons construire notre application dans server.js. Voici à quoi ressemble notre fichier server.js.

```
'use strict';
```

```
// ================================================================
// get all the tools we need
// ================================================================
var express = require('express');
var routes = require('./routes/index.js');
var port = process.env.PORT || 3000;
```

```
var app = express();
```

```
// ================================================================
// setup our express application
// ================================================================
app.use('/public', express.static(process.cwd() + '/public'));
app.set('view engine', 'ejs');
```

```
// ================================================================
// setup routes
// ================================================================
routes(app);
```

```
// ================================================================
// start our server
// ================================================================
app.listen(port, function() { console.log('Server listening on port ' + port + '…');});
```

Notre serveur écoutera sur le port défini dans process.env.PORT ou 3000 s'il n'est pas défini.

Nous définissons un répertoire /public car c'est ainsi que nous accéderons à notre feuille de style style.css située dans le dossier /public.

Nous définissons notre moteur de templating comme étant ejs.

#### Routes

Pour que notre application suive la structure d'une application node.js, j'ai mis les routes pour nos pages index et about dans leur propre fichier. Ce fichier est index.js dans le dossier routes.

Puisque j'ai mis les routes dans leur propre dossier, j'ai besoin d'y accéder en les requérant dans le fichier server.js.

Nous avons 2 routes dans notre application

* / — c'est un GET pour afficher la page d'accueil
* /about — c'est un GET pour afficher la page about

Dans les routes, nous utilisons res.render pour afficher les pages appropriées. La commande render cherchera par défaut des fichiers dans un dossier appelé views. Nous nous appuyons sur ce défaut et n'ajoutons que le chemin depuis le dossier views.

Voici notre fichier index.js dans le dossier routes.

```
'use strict';
```

```
module.exports = function(app) { app.get('/', function(req, res) {   res.render('pages/index'); });
```

```
 app.get('/about', function(req, res) {   res.render('pages/about'); });};
```

#### Configuration de nos partials

Pour notre application d'exemple, je vais implémenter quatre partials.

* head — contient les éléments trouvés dans la section head d'une page web
* nav — la navigation qui sera affichée sur chaque page
* footer — pied de page statique avec un lien vers mon site web
* scripts — chargement des scripts comme jQuery et Bootstrap
* 3columns — contenu qui sera affiché sur la page d'accueil

Les partials permettent une maintenance facile de votre code. Par exemple, si vous créez une navigation sur toutes vos pages, lorsque vous devez ajouter une nouvelle entrée à la navigation, vous devez alors mettre à jour chaque page avec ce changement.

Le partial de navigation sera inséré dans chaque page qui en a besoin. Pour ajouter une nouvelle entrée à la navigation, vous devez simplement mettre à jour le partial et il sera automatiquement appliqué à chaque page qui contient le partial nav.

Voici le contenu de tous nos partials.

head.ejs

```
<! — views/partials/head.ejs →
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <! — The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags →
  <title>Démonstration du templating EJS dans une application NodeJS</title>
```

```
  <! — STYLESHEETS →
  <! — CSS (load bootstrap from a CDN) →
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
  <link rel="stylesheet" href="/public/style.css"></head>
```

nav.ejs

```
<! — views/partials/nav.ejs →
<nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">
  <div class="container">
```

```
<div class="navbar-header">
  <a class="navbar-brand" href="/">
    <span class="glyphicon glyphicon glyphicon-cog"></span> CodePrep.io
  </a>
</div>
```

```
<ul class="nav navbar-nav pull-right">
  <li><a href="/">Home</a></li>
  <li><a href="/about">About</a></li>
</ul>
```

```
</div></nav>
```

footer.ejs

```
<! — views/partials/footer.ejs →
<footer class="footer">
  <div class="container">
    <p class="text-center text-muted">© Copyright 2015 <a href="http://www.codeprep.io">CodePrep.io</a></p>
  </div>
</footer>
```

scripts.ejs

```
<! — views/partials/scripts.ejs →
```

```
<! — jQuery (necessary for Bootstrap's JavaScript plugins) →
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
<! — Bootstrap javascript file →
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
```

3columns.ejs

```
<! — views/partials/3columns.ejs →
<section name="content">
  <div class="container">
    <h2 class="text-center">Sample Data</h2>
    <div class="col-xs-12 col-md-4">
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum eget iaculis lorem. Fusce elementum magna fringilla ipsum bibendum, vitae consectetur ligula interdum. Sed mauris diam, hendrerit eget suscipit vel, luctus at odio. Etiam pellentesque a metus et pharetra. Praesent dictum, libero id tempor malesuada, erat ex cursus nibh, ac hendrerit massa neque commodo metus. Integer porttitor ante eu varius interdum. Suspendisse quis iaculis erat. Fusce eu nisl id eros tempor posuere. Donec placerat orci orci, ut ultrices neque rutrum in. Nunc dignissim ante et risus rhoncus, vel feugiat mi vestibulum. Aliquam in dictum neque, non vestibulum lorem. Sed imperdiet dolor vitae felis iaculis, id sollicitudin lectus rhoncus. Maecenas ac dolor eget tortor rutrum commodo. Aliquam luctus iaculis mi id semper. Suspendisse sem nisi, convallis at dapibus in, convallis eu neque. Curabitur maximus magna et nulla ullamcorper facilisis.</p>
    </div>
    <div class="col-xs-12 col-md-4">
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum eget iaculis lorem. Fusce elementum magna fringilla ipsum bibendum, vitae consectetur ligula interdum. Sed mauris diam, hendrerit eget suscipit vel, luctus at odio. Etiam pellentesque a metus et pharetra. Praesent dictum, libero id tempor malesuada, erat ex cursus nibh, ac hendrerit massa neque commodo metus. Integer porttitor ante eu varius interdum. Suspendisse quis iaculis erat. Fusce eu nisl id eros tempor posuere. Donec placerat orci orci, ut ultrices neque rutrum in. Nunc dignissim ante et risus rhoncus, vel feugiat mi vestibulum. Aliquam in dictum neque, non vestibulum lorem. Sed imperdiet dolor vitae felis iaculis, id sollicitudin lectus rhoncus. Maecenas ac dolor eget tortor rutrum commodo. Aliquam luctus iaculis mi id semper. Suspendisse sem nisi, convallis at dapibus in, convallis eu neque. Curabitur maximus magna et nulla ullamcorper facilisis.</p>
    </div>
    <div class="col-xs-12 col-md-4">
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum eget iaculis lorem. Fusce elementum magna fringilla ipsum bibendum, vitae consectetur ligula interdum. Sed mauris diam, hendrerit eget suscipit vel, luctus at odio. Etiam pellentesque a metus et pharetra. Praesent dictum, libero id tempor malesuada, erat ex cursus nibh, ac hendrerit massa neque commodo metus. Integer porttitor ante eu varius interdum. Suspendisse quis iaculis erat. Fusce eu nisl id eros tempor posuere. Donec placerat orci orci, ut ultrices neque rutrum in. Nunc dignissim ante et risus rhoncus, vel feugiat mi vestibulum. Aliquam in dictum neque, non vestibulum lorem. Sed imperdiet dolor vitae felis iaculis, id sollicitudin lectus rhoncus. Maecenas ac dolor eget tortor rutrum commodo. Aliquam luctus iaculis mi id semper. Suspendisse sem nisi, convallis at dapibus in, convallis eu neque. Curabitur maximus magna et nulla ullamcorper facilisis.</p>
    </div>
  </div>
</section>
```

#### Construction de nos pages

Notre application d'exemple a une page d'accueil et une page about. Nous devons créer ces deux pages. Sur ces pages, nous allons insérer les partials appropriés que nous venons de créer sur la page.

Nous avons mis tous nos partials dans un dossier appelé partials dans le dossier views. Nous allons créer un autre dossier dans le dossier views appelé pages. Ce dossier contiendra notre page d'accueil et nos pages about.

Pour insérer un partial sur une page, nous utilisons ce format :

```
<% include ../partials/head %>
```

Voici le contenu de nos deux pages :

**index.ejs**

```
<!DOCTYPE html><html lang="en">
```

```
<% include ../partials/head %>
```

```
<body>
```

```
<% include ../partials/nav %>
```

```
<section name="jumbotron">
  <div class="jumbotron text-center">
    <h1>CodePrep.io Presents</h1>
    <p>Using EJS templating with Node.js</p>
  </div>
</section>
```

```
<% include ../partials/3columns %>
```

```
<% include ../partials/footer %>
```

```
<% include ../partials/scripts %>
```

```
</body>
```

```
</html>
```

**about.ejs**

```
<!DOCTYPE html><html lang="en">
```

```
<% include ../partials/head %>
```

```
<body>
```

```
<% include ../partials/nav %>
```

```
<! — content for about page →
<div class="container" id="about">
  <div class="row">
    <h2 class="text-center">About Page</h2>
    <div class="col-xs-12">
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent sapien eros, dictum eu malesuada sagittis, pellentesque sed enim. Donec at odio volutpat, dignissim mauris tincidunt, pharetra lorem. Fusce porta neque non lorem vulputate, et commodo dolor semper. Proin sodales lacinia nibh vel semper. Nulla sed faucibus nisi. Aliquam venenatis pellentesque tortor et fringilla. Nulla porttitor massa vitae libero volutpat, id mollis neque elementum. Integer porta, enim eu pharetra interdum, diam metus mollis purus, id ornare risus enim a magna. Sed rhoncus, nulla ac hendrerit lacinia, neque lectus iaculis ligula, et euismod erat massa sit amet orci. Ut fermentum hendrerit arcu. Vestibulum quis leo ut ante eleifend fringilla.
```

```
Morbi maximus eu lorem sit amet tempor. Nunc dignissim lacus vel aliquet ornare. Aliquam eget turpis et nisi tincidunt rhoncus. Vestibulum interdum interdum aliquet. Phasellus quis erat est. Pellentesque molestie pretium quam in fermentum. Maecenas eu luctus turpis, euismod feugiat risus. Integer scelerisque cursus tempor. Phasellus in bibendum tortor.
```

```
Aenean vitae lorem augue. Cras ultricies posuere vestibulum. Integer non felis porttitor mi ultricies pretium. Sed vitae nisi accumsan, maximus lorem sed, malesuada quam. Nunc lacus est, elementum vel ultrices sit amet, suscipit eu nibh. Maecenas vel facilisis leo, id congue sem. In hac habitasse platea dictumst. Aenean est lorem, hendrerit sit amet rutrum ac, sodales eget neque. Pellentesque hendrerit, risus in bibendum varius, purus tellus accumsan leo, et suscipit lorem nulla non arcu.</p>
    </div>
```

```
</div>
</div>
<! — end of content →
```

```
<% include ../partials/footer %>
```

```
<% include ../partials/scripts %>
```

```
</body></html>
```

#### Démarrage de notre application

Pour démarrer l'application, entrez la commande suivante :

```
node server.js
```

Lorsque notre application démarre, elle affichera notre page d'accueil :

![Image](https://cdn-media-1.freecodecamp.org/images/Jw4IUCIlbgoAmUUj910htgwTuO4IMLu6fQf3)
_page d'accueil_

Si vous cliquez sur le lien about dans la navigation, vous verrez la page about :

![Image](https://cdn-media-1.freecodecamp.org/images/lKS7AgrCRU6XiLL2hqRJJDulaOGXBCzIu53d)
_page about_

### Obtenir le code

[Vous pouvez obtenir le code pour cet exemple sur github](https://github.com/ratracegrad/nodejs_ejs_boilerplate)

### Plus d'articles

Merci d'avoir lu mon article. Si vous l'aimez, veuillez cliquer sur l'icône d'applaudissement ci-dessous afin que d'autres puissent trouver l'article. Voici quelques-uns de mes autres articles qui pourraient vous intéresser :

[Utilisation de Node.js & Express.js pour sauvegarder des données dans une base de données MongoDB](https://medium.com/@ratracegrad/hitchhikers-guide-to-back-end-development-with-examples-3f97c70e0073)

[Les premières impressions comptent — Pourquoi votre dépôt Github n'a-t-il pas de fichier ReadMe ?](https://medium.com/@ratracegrad/first-impressions-count-why-doesnt-your-github-repo-have-a-readme-file-f240961a8fca)

[Pourquoi la culture d'entreprise est importante pour votre carrière en tant qu'ingénieur logiciel](https://medium.freecodecamp.org/why-company-culture-is-important-to-your-career-as-a-software-engineer-5a590bc44621)