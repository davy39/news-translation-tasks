---
title: Comment modulariser HTML en utilisant des moteurs de template et Gulp
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2015-11-07T04:36:01.000Z'
originalURL: https://freecodecamp.org/news/how-to-modularize-html-using-template-engines-and-gulp-d1cb8af54138
coverImage: https://cdn-media-1.freecodecamp.org/images/1*uQxKWK71HvEAlKwCc78XbQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: Comment modulariser HTML en utilisant des moteurs de template et Gulp
seo_desc: 'By Zell Liew

  Template engines are tools that help you break HTML code into smaller pieces that
  you can reuse across multiple HTML files. Template engines also give you the power
  to feed data into variables that help simplify your code.

  You can only u...'
---

Par Zell Liew

Les moteurs de template sont des outils qui vous aident à diviser le code HTML en plus petits morceaux que vous pouvez réutiliser dans plusieurs fichiers HTML. Les moteurs de template vous donnent également la possibilité d'alimenter des données dans des variables qui aident à simplifier votre code.

Vous ne pouvez utiliser les moteurs de template que si vous avez un moyen de les compiler en HTML. Cela signifie que vous ne pouvez les utiliser que si vous travaillez avec un langage backend, ou si vous utilisez JavaScript côté client.

Cependant, avec Node.js, vous pouvez maintenant exploiter facilement la puissance des moteurs de template grâce à des outils comme Gulp.

Aujourd'hui, vous apprendrez ce que sont les moteurs de template, pourquoi vous devriez les utiliser, et comment en configurer un avec Gulp.

### Pourquoi vous devriez utiliser des moteurs de template

Les moteurs de template ont deux avantages majeurs :

1. Ils vous permettent de diviser le code HTML en fichiers plus petits
2. Ils vous permettent de peupler votre balisage avec des données

Passons-les en revue un par un.

#### Diviser HTML en fichiers plus petits

Il est courant qu'un fichier HTML contienne des blocs de code qui sont répétés sur le site web. Considérez ce balisage pendant un instant :

```
<body>  <nav> ... </nav>  <div class="content"> ... </div>  <footer> ... </footer></body>
```

De nombreuses lignes de code, en particulier celles dans nav et footer, sont répétées sur plusieurs pages.

Puisqu'elles sont répétées, nous pouvons les extraire et les placer dans des fichiers plus petits appelés **partiels**.

Par exemple, le partiel de navigation peut contenir une navigation simple comme ceci :

```
<!-- Partiel de Navigation --><nav>  <a href="index.html">Accueil</a>  <a href="about.html">À propos</a>  <a href="contact.html">Contact</a></nav>
```

Ensuite, nous pouvons réutiliser ce partiel dans nos fichiers HTML. Voici à quoi pourraient ressembler les fichiers HTML avec les partiels inclus :

```
<body>  {% include partials "nav" %}  <div class="content"> ... </div>  {% include partials "footer" %}</body>
```

Remarque : La syntaxe pour inclure des partiels est différente pour chaque moteur de template. Celle montrée ci-dessus est pour nunjucks ou Swig.

Il y a une chose formidable à pouvoir diviser le code comme ceci.

Imaginez simplement ce que vous feriez si vous deviez changer la navigation maintenant. Lorsque vous utilisez un partiel, tout ce que vous avez à faire est de changer le code dans le partiel de navigation et toutes vos pages seront mises à jour.

Cela est beaucoup plus facile que de devoir changer le même code dans chaque fichier où la navigation est utilisée.

Diviser le code en fichiers plus petits vous aide à écrire moins de code (dupliqué). Cela vous évite également de devenir fou lorsque vous devez plonger et changer l'ancien code.

Passons au deuxième avantage.

#### Utiliser des données pour peupler le balisage

Cet avantage est mieux expliqué avec un exemple. Supposons que vous créez une galerie d'images. Votre balisage ressemblerait à quelque chose comme ceci :

```
<div class="gallery">  <div class="gallery__item">    <img src="item-1.png" alt="item-1">  </div>  <div class="gallery__item">    <img src="item-2.png" alt="item-2">  </div>  <div class="gallery__item">    <img src="item-3.png" alt="item-3">  </div>  <div class="gallery__item">    <img src="item-4.png" alt="item-4">  </div>  <div class="gallery__item">    <img src="item-5.png" alt="item-5">  </div></div>
```

Remarquez comment la div .gallery__item a été répétée plusieurs fois ci-dessus ?

Si vous deviez changer le balisage d'un .gallery__item, vous devriez le changer en cinq endroits différents.

Maintenant, imaginez que vous avez la possibilité d'écrire du HTML en utilisant une logique de boucle. Vous écriviez probablement quelque chose de similaire à ceci :

```
<div class="gallery">  // Un peu de code pour boucler les 5 fois suivantes :   <div class="gallery__item">    <img src="$path-to-image" alt="$alt-text">  </div>  // fin de la boucle</div>
```

Les moteurs de template vous donnent la possibilité d'utiliser une telle boucle. Au lieu de boucler exactement cinq fois, il boucle à travers un ensemble de données que vous lui passez. Le HTML deviendrait :

```
<div class="gallery">  {% for image in images %}    <div class="gallery__item">      <img src="{{src}}" alt="{{alt}}">    </div>  {% endfor %}</div>
```

Les données seraient un fichier JSON qui ressemble à ceci :

```
images: [{  src: "item1.png",  alt: "texte alternatif pour item1"  }, {  src: "item2.png",  alt: "texte alternatif pour item1"  },  // ... Jusqu'à la fin de vos données]
```

Avec les données fournies, le moteur de template créerait un balisage tel que le nombre de .gallery__items correspondrait au nombre d'éléments dans le tableau images des données.

Le meilleur, c'est que vous n'avez à changer le balisage qu'une seule fois et tous les .gallery__items seront mis à jour.

### Utiliser un moteur de template avec Gulp

Avant de continuer et de créer une tâche Gulp qui utilise un moteur de template, examinons une liste de moteurs de template populaires basés sur JavaScript que Gulp est capable d'utiliser :

* [Dust.js](http://akdubya.github.io/dustjs/)
* [Embedded JS](http://www.embeddedjs.com/) (également connu sous le nom de ejs)
* [Handlebars](http://handlebarsjs.com/)
* [Hogan.js](http://twitter.github.io/hogan.js/)
* [Jade](http://jade-lang.com/)
* [Mustache](https://mustache.github.io/)
* [Nunjucks](https://mozilla.github.io/nunjucks/)
* [Swig](http://paularmstrong.github.io/swig/) (qui n'est plus maintenu)

Chaque moteur de template est unique et a ses propres avantages et inconvénients. La syntaxe peut varier considérablement entre les moteurs de template. Pour cette raison, nous nous concentrerons sur l'utilisation d'un moteur de template dans cet article — nunjucks.

Je recommande vivement nunjucks car il est extrêmement puissant. Il a des fonctionnalités — comme l'héritage — que la plupart des moteurs de template n'ont pas. J'ai également utilisé Mustache et Handlebars précédemment, et j'ai trouvé qu'ils n'étaient pas assez puissants dans de nombreuses circonstances.

Maintenant, intégrons nunjucks dans notre flux de travail.

### Utiliser Nunjucks avec Gulp

![Image](https://cdn-media-1.freecodecamp.org/images/1*Lhl-R75OQPH6Xm3bZrs7iA.jpeg)

Nous pouvons utiliser nunjucks grâce à un plugin appelé [gulp-nunjucks-render](https://github.com/carlosl/gulp-nunjucks-render).

Commençons par installer gulp-nunjucks-render.

Remarque : Je suppose que vous savez comment utiliser Gulp, donc je n'entrerai pas dans les bases. Si vous vous sentez confus, il pourrait être bon de [vous rafraîchir les bases de Gulp avant de revenir ici.](https://css-tricks.com/gulp-for-beginners/)

```
$ npm install gulp-nunjucks-render --save-dev
```

```
var nunjucksRender = require('gulp-nunjucks-render');
```

Ensuite, nous devons créer une structure de projet qui nous permet d'utiliser facilement nunjucks. Nous utiliserons cette structure :

```
project/   |- app/       |- index.html et autres fichiers .html      |- pages/      |- templates/          |- partials/
```

**Le dossier templates** est utilisé pour stocker tous les partiels nunjucks et autres fichiers nunjucks qui seront ajoutés aux fichiers dans le dossier pages.

**Le dossier pages** est utilisé pour stocker les fichiers qui seront compilés en HTML. Une fois qu'ils sont compilés, ils seront créés dans le dossier app.

Travaillons à travers le processus de création de quelques fichiers nunjucks avant de créer la tâche Gulp.

Tout d'abord, une bonne chose à propos de nunjucks (que d'autres moteurs de template pourraient ne pas avoir) est qu'il vous permet de créer un template qui contient du code HTML de base qui peut être hérité par d'autres pages. Appelons ce HTML de base layout.nunjucks.

Créez un fichier appelé layout.nunjucks et placez-le dans votre dossier templates. Il devrait contenir un peu de code de base comme les balises <html>, <head> et <body>. Il peut également contenir des choses qui sont similaires sur toutes vos pages, comme les liens vers les fichiers CSS et JavaScript.

Voici un exemple de fichier layout.nunjucks :

```
<!-- layout.nunjucks -->
```

```
<!DOCTYPE html><html lang="en"><head>  <meta charset="UTF-8">  <title>Document</title>  <link rel="stylesheet" href="css/styles.css"></head><body>
```

```
  <!-- Vous écrivez le code pour ce bloc de contenu dans un autre fichier -->  {% block content %} {% endblock %}
```

```
  <script src="bower_components/jquery/dist/jquery.js"></script>  <script src="js/main.js"></script></body></html>
```

Au fait, je préfère utiliser l'extension .nunjucks pour les fichiers et partiels nunjucks car cela me permet de savoir que je travaille avec nunjucks. Si vous n'êtes pas à l'aise avec .nunjucks, n'hésitez pas à laisser vos fichiers en .html.

Ensuite, créons un fichier index.nunjucks dans le répertoire pages. Ce fichier sera finalement converti en index.html et placé dans le dossier app.

Il devrait étendre layouts.nunjucks pour qu'il contienne le code de base que nous avons défini dans layout.nunjucks :

```
<!-- index.nunjucks -->{% extends "layout.nunjucks" %}
```

Nous pouvons ensuite ajouter du code HTML qui est spécifique à index.nunjucks entre {% block content %} et {% endblock %}.

```
<!-- index.nunjucks -->{% extends "layout.nunjucks" %}
```

```
{% block content %} <h1>Ceci est la page d'accueil</h1>{% endblock %}
```

Nous avons terminé la configuration des fichiers nunjucks. Maintenant, créons une tâche nunjucks qui convertit index.nunjucks en index.html.

```
gulp.task('nunjucks', function() {  // contenu nunjucks ici});
```

Dans la tâche nunjucks, nous devons d'abord indiquer à nunjucks où trouver nos templates. Nous pouvons le faire avec la fonction nunjucks.configure que gulp-nunjucks-render fournit.

```
gulp.task('nunjucks', function() {  nunjucksRender.nunjucks.configure(['app/templates/']);});
```

Ensuite, nous ajoutons des fichiers depuis pages dans la tâche gulp via gulp.src. Puis, nous sortons ces fichiers dans app.

```
gulp.task('nunjucks', function() {  nunjucksRender.nunjucks.configure(['app/templates/']);
```

```
  // Obtient les fichiers .html et .nunjucks dans pages  return gulp.src('app/pages/**/*.+(html|nunjucks)')  // Rend le template avec nunjucks  .pipe(nunjucksRender())  // sortie des fichiers dans le dossier app  .pipe(gulp.dest('app'))});
```

Maintenant, essayez d'exécuter gulp nunjucks dans votre ligne de commande. Gulp aura créé un index.html et l'aura placé dans le dossier app pour vous.

![Image](https://cdn-media-1.freecodecamp.org/images/0*7qYZxfS5idGHLbof.png)

Si vous avez ouvert ce fichier index.html, vous devriez voir le code suivant :

```
<!DOCTYPE html><html lang="en"><head>  <meta charset="UTF-8">  <title>Document</title>  <link rel="stylesheet" href="css/styles.css"></head><body>
```

```
  <h1>Ceci est la page d'accueil</h1>
```

```
  <script src="js/main.js"></script></body></html>
```

Remarquez comment tout (sauf la balise <h1>) provient de layouts.nunjucks ? C'est à cela que sert layout.nunjucks. Si vous devez modifier la balise <head>, ajouter du JavaScript ou changer les fichiers CSS, vous savez que vous pouvez le faire dans layouts.nunjucks et chaque page sera mise à jour en conséquence.

À ce stade, vous avez réussi à étendre layouts.nunjucks dans index.nunjucks et à le rendre dans index.html. Il y a encore quelques choses que nous pouvons améliorer. L'une des choses que nous pouvons faire est d'apprendre à utiliser un partiel.

### Ajouter un partiel Nunjucks

Nous devons créer un partiel avant de pouvoir l'ajouter à index.nunjucks. Créons un partiel appelé navigation.nunjucks et plaçons-le dans un dossier partials qui se trouve dans le dossier templates.

![Image](https://cdn-media-1.freecodecamp.org/images/0*xTgHx0PLnJhxFNKB.png)

Ensuite, ajoutons une navigation simple à ce partiel :

```
<!-- navigation.nunjucks --><nav>  <a href="#">Accueil</a>  <a href="#">À propos</a>  <a href="#">Contact</a></nav>
```

Ajoutons maintenant le partiel à notre fichier index.nunjucks. Nous pouvons ajouter des partiels avec l'aide de l'instruction {% include "chemin-vers-le-partiel" %} que nunjucks fournit.

```
{% block content %} 
```

```
<h1>Ceci est la page d'accueil</h1><!-- Ajoute le partiel de navigation -->{% include "partials/navigation.nunjucks" %}
```

```
{% endblock %}
```

Maintenant, si vous exécutez gulp nunjucks, vous devriez obtenir un fichier index.html avec le code suivant :

```
<!-- <head> et CSS -->
```

```
<h1>Ceci est la page d'accueil</h1>
```

```
<nav>  <a href="#">Accueil</a>  <a href="#">À propos</a>  <a href="#">Contact</a></nav>
```

```
<!-- JavaScript et </body>    -->
```

Lorsque vous utilisez des partiels comme navigation, nous pouvons souvent rencontrer des situations où nous devons ajouter une classe à l'un des liens sur une page. Voici un exemple :

```
<nav>  <!-- la classe active ne doit être présente que sur la page d'accueil -->  <a href="#" class="active">Accueil</a>  <a href="#">À propos</a>  <a href="#">Contact</a></nav>
```

La classe active ne doit être présente que sur le lien de la page d'accueil si nous sommes sur la page d'accueil. Si nous sommes sur la page à propos, alors la classe active ne doit être présente que sur le lien à propos.

Nous pouvons faire cela avec une version légèrement modifiée de partiels appelée **Macros**. La seule différence est que vous pouvez ajouter des variables de la même manière que vous ajouteriez des arguments à une fonction JavaScript.

### Ajouter une macro Nunjucks

Tout d'abord, créons un fichier nav-macro.nunjucks dans un dossier macros qui se trouve dans le dossier templates. Notez que nous utilisons nav-macro pour nous assurer que vous ne confondez pas les deux fichiers nunjucks de navigation.

![Image](https://cdn-media-1.freecodecamp.org/images/0*3-VWQZddWXvgH2ER.png)

Vous pouvez commencer à écrire des macros une fois que vous avez créé le fichier nav-macro.nunjucks.

Toutes les macros commencent et se terminent avec les balises suivantes :

```
{% macro functionName() %}  <!-- Contenu de la macro ici -->{% endmacro %}
```

Créons une macro appelée active. Son but est de sortir la classe active pour notre navigation. Elle doit prendre un argument, activePage, qui par défaut est "home".

```
{% macro active(activePage='home') %}  <!-- Contenu de la macro ici -->{% endmacro %}
```

Nous allons écrire du HTML qui sera créé dans la macro. Ici, nous pouvons également utiliser la fonction if fournie par nunjucks pour vérifier si une classe active doit être ajoutée :

```
{% macro active(activePage='home') %}<nav>  <a href="#" class="{%if activePage == 'home' %} active {% endif %}">Accueil</a>  <!-- Répéter pour à propos et contact --></nav>{% endmacro %}
```

Nous avons terminé l'écriture de la macro. Apprenons maintenant à l'utiliser dans index.nunjucks.

Nous utilisons la fonction import dans nunjucks pour ajouter un fichier de macro, contrairement à la fonction include que nous avons utilisée précédemment pour ajouter un partiel.

Lorsque nous importons un fichier de macro, nous devons également le définir comme une variable. Voici un exemple :

```
<!-- index.html -->{% block content %}
```

```
<!-- Importation de la macro Nunjucks -->{% import 'macros/navigation.nunjucks' as nav %}
```

```
{% endblock %}
```

Dans ce cas, nous avons défini la variable nav comme étant l'ensemble du fichier navigation.nunjucksmacro. Nous pouvons ensuite utiliser la variable nav pour appeler toute macro écrite dans ce fichier.

```
{% import 'macros/navigation.nunjucks' as nav %}<!-- Création de la navigation avec activePage = 'home' -->{{nav.active('home')}}
```

Avec cette modification, essayez d'exécuter à nouveau gulp nunjucks et vous devriez pouvoir voir cette sortie :

```
<nav>  <a href="#" class=" active ">Accueil</a>  <a href="#" class="">À propos</a>  <a href="#" class="">Contact</a></nav>
```

C'est tout pour l'utilisation des macros. Connaître cela vous aidera invariablement beaucoup lors de l'utilisation de nunjucks :)

Il y a une chose de plus que nous pouvons faire pour améliorer notre expérience de templating avec nunjucks, et c'est de peupler le HTML avec des données.

### Peupler HTML avec des données

Commençons par créer un fichier appelé data.json qui contient vos données. Je vous recommande de placer ce data.json dans le dossier app.

```
$ cd app$ touch data.json
```

Ajoutons maintenant quelques données. Nous pouvons utiliser les données de l'exemple précédent.

```
{  "images": [{    "src": "image-one.png",    "alt": "Texte alternatif pour l'image une"  }, {    "src": "image-two.png",    "alt": "Texte alternatif pour l'image deux"  }]}
```

Nous devons ensuite légèrement modifier notre tâche nunjucks pour utiliser les données de ce fichier data.json. Pour ce faire, nous devons utiliser l'aide d'un autre plugin gulp appelé [gulp-data](https://www.npmjs.com/package/gulp-data).

Installons gulp-data avant de continuer.

```
$ npm install gulp-data --save-dev
```

```
var data = require('gulp-data');
```

Gulp-data prend en entrée une fonction qui vous permet de retourner un fichier. Nous pouvons utiliser la fonction require fournie par Node pour obtenir ce fichier de données :

```
.pipe(data(function() {  return require('./app/data.json')}))
```

Lorsque vous utilisez require pour obtenir des fichiers depuis un répertoire personnalisé (non node_modules), vous devez indiquer à Node le chemin vers le répertoire. Ici, nous commençons par un ./ qui indique à Node de commencer par le répertoire courant, puis de chercher dans app le fichier data.json.

Remarque : Une meilleure façon est d'utiliser deux fonctions, JSON.parse() et fs.readFileSync() au lieu de require. Nous verrons comment faire dans [Automatiser votre flux de travail avec Gulp](http://zell-weekeat.com/automate-your-workflow/).

Ajoutons maintenant gulp-data à notre tâche nunjucks.

```
gulp.task('nunjucks', function() {  nunjucksRender.nunjucks.configure(['app/templates/']);
```

```
  return gulp.src('app/pages/**/*.+(html|nunjucks)')    // Ajout de données à nunjucks    .pipe(data(function() {      return require('./app/data.json')    }))    .pipe(nunjucksRender())    .pipe(gulp.dest('app'))});
```

Enfin, ajoutons un peu de balisage à index.nunjucks pour qu'il utilise les données que nous avons ajoutées.

```
<!-- index.nunjucks -->{% block content %}<div class="gallery">  <!-- Boucle à travers le tableau "images" -->  {% for image in images %}  <div class="gallery__item">    <img src="{{image.src}}" alt="{{image.alt}}">  </div>  {% endfor %}</div>{% endblock %}
```

```
<!-- index.html --><div class="gallery">  <div class="gallery__item">    <img src="image-one.png" alt="Texte alternatif pour l'image une">  </div>Maintenant, si vous exécutez `gulp nunjucks`, vous devriez obtenir un fichier `index.html` avec le balisage suivant : 
```

```
  <div class="gallery__item">    <img src="image-two.png" alt="Texte alternatif pour l'image deux">  </div></div>
```

Super !

### Conclusion

Nous avons appris comment les moteurs de template rendent le développement beaucoup plus facile et quelques façons de base de les utiliser.

Nous avons ensuite approfondi un moteur de template, nunjucks, et l'avons fait fonctionner avec Gulp. Nous avons également appris comment utiliser :

* extend pour hériter d'un fichier nunjucks
* include pour inclure un partiel
* import pour importer une macro

Si vous souhaitez accélérer davantage votre flux de travail, consultez [Automatiser votre flux de travail](http://zell-weekeat.com/automate-your-workflow/). Il couvrira :

* Surveillance et compilation des fichiers nunjucks
* Prévention des erreurs de nunjucks qui interrompent la surveillance de Gulp
* Rechargement automatique du navigateur chaque fois qu'un fichier change

> Cet article est initialement paru sur mon blog à l'adresse [www.zell-weekeat.com](http://zell-weekeat.com). Consultez-le si vous voulez plus d'articles comme celui-ci