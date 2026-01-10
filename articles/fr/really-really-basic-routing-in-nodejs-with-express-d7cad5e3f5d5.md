---
title: Routage vraiment très basique en Node.js avec Express
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-03T04:19:40.000Z'
originalURL: https://freecodecamp.org/news/really-really-basic-routing-in-nodejs-with-express-d7cad5e3f5d5
coverImage: https://cdn-media-1.freecodecamp.org/images/0*FWsvE-8X-T1wNDj5.
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: routing
  slug: routing
- name: 'tech '
  slug: tech
seo_title: Routage vraiment très basique en Node.js avec Express
seo_desc: 'By Pau Pavón

  The goal of this story is to briefly explain how routing works in Express while
  building a simple — very simple — Node app.

  We’ll also use EJS, a template engine that “lets you generate HTML markup with plain
  JavaScript,” according to th...'
---

Par Pau Pavón

L'objectif de cet article est d'expliquer brièvement comment fonctionne le routage dans Express tout en construisant une application Node simple — très simple.

Nous utiliserons également EJS, un moteur de template qui « vous permet de générer du balisage HTML avec du JavaScript simple », selon [leur site web](http://ejs.co/). Basiquement, cela nous permettra de créer des pages HTML qui peuvent varier en fonction de la requête du client. Nous n'utiliserons pas cette dernière fonctionnalité, mais c'est une excellente option. À la fin de cet article, vous trouverez quelques ressources pour en apprendre davantage.

### Qu'est-ce que le routage ? (En 2 lignes environ)

Tout d'abord, jetons un rapide (vraiment rapide) coup d'œil à ce qu'est le routage :

> unsiteweb.com/uneroute

C'est essentiellement amener l'utilisateur (ou des données) d'un endroit à un autre. Cet endroit est la route. Je vous avais dit que ce serait rapide.

### Création du projet

Nous allons construire un site web élégant pour apprendre comment fonctionne le routage dans Express. Regardez ça :

![Image](https://cdn-media-1.freecodecamp.org/images/zKy5qHElo1OJCfcnBBlTS0rU2RqIvIaPPHRc)

Cool, non ? Mais c'est tout ce dont nous avons besoin pour l'instant.

Tout d'abord, créons le projet et installons les packages. Exécutez simplement les commandes suivantes dans la ligne de commande :

> npm install express

> npm install ejs

Vous pouvez également ajouter _dash dash save_ (j'écris — comme « dash » car Medium le formate automatiquement, et ce n'est pas bien pour cet usage) pour l'enregistrer dans votre fichier _package.json_. Mais comment cela fonctionne est une histoire pour un autre jour.

Ensuite, nous allons requérir Express et définir le moteur de vue sur EJS dans notre fichier _app.js_ comme suit :

```
var express = require('express');var app = express();app.set('view engine', 'ejs');
```

Nous inclurons également la ligne suivante pour que notre application écoute les requêtes :

```
app.listen(3000);
```

### Gestion des requêtes GET

Félicitations, tout est prêt pour gérer les requêtes ! Il existe plusieurs types de requêtes en HTTP, mais nous ne gérerons que les requêtes GET, qui sont utilisées pour récupérer des données du serveur. Pour gérer ce type de requête dans Express, nous utilisons la méthode suivante :

```
app.get('/about', function(req, res) {  res.render('about');});
```

Examinons ce qui se passe ici. Nous disons à notre serveur que, chaque fois que quelqu'un tape _unsiteweb.com/about_, nous voulons déclencher une fonction. Cette fonction prend deux paramètres, _req_ (requête) et _res_ (réponse). En utilisant l'objet de réponse, nous rendons la _page about_.

Pour que cela fonctionne, nous devons créer une page nommée _about.ejs_ en HTML. Nous la placerons également dans un dossier appelé _views_ à l'intérieur de notre dossier de projet. C'est le dossier où Express cherchera pour rendre la vue. Voici la page mega-complexe about que nous utiliserons pour cet exemple :

![Image](https://cdn-media-1.freecodecamp.org/images/xHlH6J5GdxC1m8GhzCNtf5WRI71Lv-QEUYgt)

Bien ! Mais, que se passe-t-il si l'utilisateur ne tape aucune route ? Comme nous le faisons la plupart du temps, _unsiteweb.com_ ? Eh bien, c'est très simple. Changez _/about_ en simplement _/_, et rendez la page que vous souhaitez :

```
app.get('/', function(req, res) {  res.render('home');});
```

### Gestion des routes inexistantes

Mais que se passe-t-il si quelqu'un tape une route qui n'existe pas ? Nous ne voulons probablement pas qu'une page d'erreur par défaut s'affiche. Au lieu de cela, nous voulons une page d'erreur personnalisée et cool.

Eh bien, la bonne nouvelle est qu'il est extrêmement facile d'en créer une avec Express. Remplacez simplement le paramètre de route dans la méthode get par un astérisque et rendez votre propre page d'erreur comme suit :

```
app.get('*', function(req, res) {  res.render('error');});
```

### Essayons !

Enfin, lançons notre serveur depuis la ligne de commande (en supposant que le serveur s'appelle _app.js_)

> node app

et voyons si cela fonctionne ! Tapons le nom de notre serveur (_localhost_, car c'est un serveur local qui s'exécute sur notre ordinateur) et le port (_3000_ dans ce cas) dans notre navigateur :

> localhost:3000

![Image](https://cdn-media-1.freecodecamp.org/images/1KFP8uvz25ry2d2pNQ2QsSdQnacvlqM3E2ex)
_localhost:3000 ou localhost:3000/_

![Image](https://cdn-media-1.freecodecamp.org/images/eDCDZV5wyUWUoLFsLQQnZU5hHa9P8rgxDirO)
_localhost:3000/about_

![Image](https://cdn-media-1.freecodecamp.org/images/hkwkh0YVUHuY-0LWm6zUmlMXUXYrr2P6hSZj)
_localhost:3000/quelquechosepourlequelnousnavonspasderoute_

Incroyable !

### Pour aller plus loin

Vous pouvez apprendre tout ce que vous devez savoir sur le routage dans le [guide Express](http://expressjs.com/en/guide/routing.html), et il y a beaucoup de choses pratiques sur le [site web EJS](http://ejs.co) également !

J'espère que cet article vous a été utile. Si c'est le cas, laissez un commentaire et applaudissez-le !

Bon codage… **_Ou bon routage, je suppose !_**