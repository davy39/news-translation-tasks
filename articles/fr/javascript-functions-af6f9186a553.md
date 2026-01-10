---
title: 'HTML Canvas Expliqué : Une Introduction au Canvas HTML5 et aux Fonctions JavaScript'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-03-25T01:58:19.000Z'
originalURL: https://freecodecamp.org/news/javascript-functions-af6f9186a553
coverImage: https://cdn-media-1.freecodecamp.org/images/1*fzz0bNoOcUnsihyppXAMEA.jpeg
tags:
- name: The Iron Yard
  slug: the-iron-yard
- name: Design
  slug: design
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: 'HTML Canvas Expliqué : Une Introduction au Canvas HTML5 et aux Fonctions
  JavaScript'
seo_desc: 'By Adam Recvlohe

  Before the Emoji, some background…

  I started working in the web development field about 6 months ago after spending
  most of my career in education. The transition has been great and I am very thankful
  for the opportunity to work on r...'
---

Par Adam Recvlohe

## Avant les emojis, un peu de contexte…

J'ai commencé à travailler dans le domaine du développement web il y a environ 6 mois après avoir passé la majeure partie de ma carrière dans l'éducation. La transition a été formidable et je suis très reconnaissant d'avoir l'opportunité de travailler sur des applications web réelles.

Je suis très heureux de travailler dans ce secteur, mais à mon avis, il y a encore beaucoup à apprendre. Par conséquent, depuis le jour où j'ai commencé en tant que développeur JavaScript, j'ai continué à étudier chaque soir pour améliorer mes compétences.

En plus de mes études, j'ai récemment commencé à enseigner un « Cours d'Introduction à JavaScript » à des adolescents de Tampa Bay (à The Iron Yard à St.Pete, en Floride). Cela a été une grande expérience pour plusieurs raisons. Premièrement, cela m'a permis d'approfondir mes connaissances sur les intricacies et les nuances du langage JavaScript.

Deuxièmement, j'ai eu l'occasion d'enseigner à nouveau, ce qui est l'une de mes passions. Et troisièmement, j'ai pu réexaminer comment j'ai appris à programmer et en quoi cela diffère radicalement des débutants qui ne sont même pas sûrs d'aimer le codage et qui, dans certains cas, ne se soucient pas de ce que j'ai à dire.

Vous voyez, le programme que je pensais être idéal pour cette classe était JavaScript sous trois formes : JS dans le DOM, JS sur le serveur et la programmation fonctionnelle JS.

Après le premier jour et une bonne discussion avec mes assistants d'enseignement, j'ai réalisé que je m'étais complètement trompé. Ces sujets peuvent m'intéresser, mais ils n'amusent certainement pas un jeune qui veut simplement jouer à des jeux sponsorisés dans le navigateur. J'ai complètement réévalué ce que j'allais enseigner, et dans le processus, j'ai commencé à m'amuser !

Voici la première leçon que j'ai donnée aux étudiants, où je commence par discuter des fonctions et finis par créer un emoji de visage souriant. Amusez-vous !

Si vous voulez suivre pendant que nous parlons des fonctions, ouvrez un navigateur et allez sur [repl.it](http://repl.it) et sous les langues populaires choisissez NodeJS. Un REPL (Read Evaluate Print Loop) devrait s'ouvrir pour vous et vous pouvez suivre le code.

## Qu'est-ce que les fonctions ?

Pour comprendre comment nous allons utiliser le canvas HTML5, nous devons comprendre un peu les fonctions.

« Les fonctions sont des modules de code autonomes qui accomplissent une tâche spécifique. Les fonctions prennent généralement des données, les traitent et retournent un résultat. Une fois qu'une fonction est écrite, elle peut être utilisée encore et encore. »

Maintenant, laissez-moi vous donner quelques exemples du type de fonctions avec lesquelles nous allons travailler.

## Types de Fonctions

### Fonction Régulière

Nous déclarons une fonction de base en utilisant le mot-clé JavaScript _function_.

```
function sayHelloTo(name) {    return 'Hello ' + name;}sayHelloTo('Adam');
```

Cette fonction prend un paramètre appelé _name_. C'est une variable qui est passée à la fonction _sayHelloTo_. Par conséquent, lorsque le programme s'exécute, il passera ce qui est fourni. Dans mon cas, c'est _Adam_, donc dans la console vous verrez _Hello Adam_.

### Modèle de Constructeur

Nous pouvons également créer une fonction en utilisant le modèle de constructeur.

```
function Person(name) {    this.name = name;    this.sayHello = function() {        return "Hello, my name is " + this.name;    }}var me = new Person("Adam");me.sayHello();
```

Le mot-clé JavaScript _this_ fait référence à la fonction. Cela signifie que lorsque nous passons une variable comme _name_, tout comme nous l'avons fait auparavant, nous pouvons l'assigner à la fonction et à toute instance de cette fonction. Pour créer une instance, nous utilisons le mot-clé JavaScript _new_. Lorsque cette nouvelle instance de la fonction est créée, elle a également comme propriétés une valeur _this.name_ et une méthode _this.sayHello_. Lorsque nous avons créé l'instance de la méthode, nous avons passé notre nom : _var me = new Person('Adam')_. Lorsque vous regardez la méthode _sayHello_, elle utilise ce _name_, qui fait maintenant partie de cette instance, pour créer une phrase. Si vous exécutez ce code dans le REPL NodeJS sur repl.it, vous devriez voir la sortie _Hello, my name is Adam_.

Maintenant que nous avons terminé avec les choses ennuyeuses, dessinons sur un canvas. La façon dont j'ai enseigné la section suivante était en utilisant codepen.io. Ce que je suggère, c'est que si vous voulez suivre, allez sur codepen.io, créez un compte, puis créez un nouveau pen et vous devriez être prêt. Assurez-vous d'activer votre compte si vous voulez sauvegarder votre travail.

## Dessinons sur le Canvas

Tout d'abord, nous devons créer le canvas pour pouvoir dessiner dessus. Dans votre HTML, créez une balise canvas.

```
<canvas id="canvas"></canvas>
```

Maintenant, c'est du JavaScript à partir d'ici !

Nous devons récupérer notre élément canvas du DOM et le déclarer comme une variable. Cela nous permettra de définir son contexte. Nous ne sommes pas encore très doués avec le '3d', alors nous allons rester avec un contexte '2d'.

```
var canvas = document.getElementById("canvas");var context = canvas.getContext("2d");
```

Nous pouvons également donner au canvas ses propriétés de _width_ et _height_.

```
var canvas = document.getElementById("canvas");canvas.width = 800;canvas.height = 800;var context = canvas.getContext("2d");
```

Je veux souligner ici que le _canvas_ se comporte exactement comme un objet. Il a des propriétés et des méthodes, tout comme nous l'avons vu avec notre fonction de constructeur ci-dessus. Légèrement différent dans la façon dont nous l'avons déclaré, mais fonctionnellement, il opère de manière très similaire. Vous voyez donc qu'il a des propriétés _height_ et _width_ ainsi qu'une méthode _getContext_.

Maintenant, mettons tout cela dans une fonction pour que vous puissiez vous familiariser quelque peu avec la programmation fonctionnelle.

```
function draw() {  var canvas = document.getElementById("canvas");  canvas.width = 800;  canvas.height = 800;  var context = canvas.getContext("2d");}
```

Rien ne s'affichera encore à l'écran, nous utiliserons la méthode _fillRect_ pour nous aider avec cela.

```
function draw() {  var canvas = document.getElementById("canvas");  canvas.width = 800;  canvas.height = 800;  var context = canvas.getContext("2d");  context.fillRect(10,10, 100, 200);}
```

Si vous ne l'avez pas deviné, la méthode _fillRect_ prend quatre paramètres : la coordonnée x, la coordonnée y, la largeur et la hauteur. Sur le canvas, l'axe x commence à 0 à gauche et va jusqu'à l'infini vers la droite. L'axe y commence à 0 en haut et va jusqu'à l'infini vers le bas. Donc, lorsque nous commençons à (10, 10), nous plaçons le curseur imaginaire au point (x = 10, y = 10) et allons 100 vers la droite et 200 vers le bas à partir de ce point.

Comme vous l'avez peut-être remarqué, il n'a pas encore été ajouté à la page. Ajoutez une simple fonction _window.onload_ et faites-la égale à notre fonction draw terminée.

```
function draw() {  var canvas = document.getElementById("canvas");  canvas.width = 800;  canvas.height = 800;  var context = canvas.getContext("2d");  context.fillRect(10,10, 100, 200);}window.onload = draw;
```

Vous vous demandez peut-être pourquoi la fonction draw a été exécutée alors que nous ne l'avons pas exécutée avec des parenthèses _( )_. C'est parce que _window.onload_ est une fonction. C'est la même chose que de dire :

```
window.onload = function() {// Faire des choses ici comme ce que nous avons mis dans draw();}
```

Cela signifie que _window.onload_ exécute une fonction lorsque la fenêtre est chargée, donc ce qui se passe, c'est que _window.onload_ avec ses pouvoirs magiques met des parenthèses invisibles autour de draw, l'exécutant ainsi. Beaucoup de magie est impliquée. Mais maintenant vous connaissez le truc.

Ajoutons un peu de couleur pour le fun ! Ici, nous utilisons la méthode _fillStyle_ pour cela. Elle doit venir avant _fillRect_ ou elle ne s'affichera pas.

```
function draw() {  var canvas = document.getElementById("canvas");  canvas.width = 800;  canvas.height = 800;  var context = canvas.getContext("2d");  context.fillStyle = "blue";  context.fillRect(10,10, 100, 200);}window.onload = draw;
```

Voici un exemple de cela sur codepen :

## Dessinons d'autres formes !

C'était assez simple. Dessinons maintenant d'autres formes. Comme nous l'avons fait auparavant, nous allons créer une fonction et instancier notre canvas avec une _width_, _height_ et _context_.

```
function triangle() {  var canvas = document.getElementById("canvas");  var context = canvas.getContext("2d");  canvas.width = 400;  canvas.height = 400;}
```

Pour ne pas oublier, changez la fonction _onload_ pour qu'elle prenne maintenant la fonction triangle.

```
window.onload = triangle;
```

Maintenant que nous avons notre canvas, commençons à dessiner des lignes sur le canvas pour créer notre triangle.

```
function triangle() {  var canvas = document.getElementById("canvas");  var context = canvas.getContext("2d");  canvas.width = 400;  canvas.height = 400;      context.beginPath();  context.moveTo(75, 50);}
```

Ici, nous commençons notre chemin et déplaçons le curseur au point (x = 75, y = 50).

Maintenant, dessinons quelques lignes.

```
function triangle() {  var canvas = document.getElementById("canvas");  var context = canvas.getContext("2d");  canvas.width = 400;  canvas.height = 400;      context.beginPath();  context.moveTo(75, 50);  context.lineTo(100, 75);  context.lineTo(100, 25);  context.stroke();}
```

Cela a créé les deux premières lignes dont nous avions besoin. Pour le terminer, nous retournons là où nous avons commencé.

```
function triangle() {  var canvas = document.getElementById("canvas");  var context = canvas.getContext("2d");  canvas.width = 400;  canvas.height = 400;      context.beginPath();  context.moveTo(75, 50);  context.lineTo(100, 75);  context.lineTo(100, 25);  context.lineTo(75, 50); // Retour là où nous avons commencé  context.stroke();}
```

Pour remplir le triangle, nous pouvons utiliser la méthode fill.

```
function triangle() {  var canvas = document.getElementById("canvas");  var context = canvas.getContext("2d");  canvas.width = 400;  canvas.height = 400;      context.beginPath();  context.moveTo(75, 50);  context.lineTo(100, 75);  context.lineTo(100, 25);  context.lineTo(75, 50);  context.stroke();  context.fill();}
```

Voici à quoi cela ressemble en pratique :

Nous pouvons faire la même chose maintenant et créer facilement une grande pyramide.

```
function pyramid() {  var canvas = document.getElementById("canvas");  var context = canvas.getContext("2d");  canvas.width = 400;  canvas.height = 400;}
```

N'oubliez pas de changer la fonction _onload_ en pyramid.

```
window.onload = pyramid;
```

Déplaçons maintenant le curseur là où nous voulons qu'il soit.

```
function pyramid() {  var canvas = document.getElementById("canvas");  var context = canvas.getContext("2d");  canvas.width = 400;  canvas.height = 400;      context.beginPath();  context.moveTo(200, 0);}
```

Je veux que ma pyramide occupe autant d'espace que possible, donc je commence tout en haut de mon canvas et exactement au milieu de l'axe des x.

Maintenant, nous pouvons commencer à dessiner notre forme et à la remplir.

```
context.lineTo(0, 400);context.lineTo(400, 400);context.lineTo(200, 0);context.stroke();context.fillStyle = "orange";context.fill();
```

Terminé ! Vous devriez maintenant avoir une belle pyramide orange sur votre écran parce que, bien sûr, vous faites partie de l'Illuminati. Ne mentez pas !

Voici le produit fini avec lequel vous pouvez jouer :

## Emojis !

Maintenant, ce pour quoi vous êtes venus : les Emojis !

Comme nous l'avons fait auparavant, nous configurons notre canvas.

```
function smileyFaceEmoji() {    var canvas = document.getElementById("canvas");    var context = canvas.getContext("2d");    canvas.width = 500;    canvas.height = 500;}
```

N'oubliez pas de changer _onload_ pour cette fonction.

```
window.onload = smileyFaceEmoji;
```

Maintenant, dessinons notre visage.

```
context.beginPath();context.arc(250, 250, 100,0,Math.PI*2, true);context.stroke();
```

J'ai un peu changé les choses ici en utilisant la fonction _arc_. La fonction _arc_ prend plusieurs arguments : la coordonnée x, la coordonnée y, le rayon, le point de départ en radians, le point de fin en radians et si elle est dessinée dans le sens des aiguilles d'une montre (nous avons dit true). Contrairement à la façon dont un rectangle est fait en commençant à un point et en se déplaçant vers le suivant, le point (x = 250, y = 250) est en fait le milieu du cercle et s'étend ensuite sur 100 pixels.

Cool, non ? Ensuite viennent les yeux.

```
context.moveTo(235, 225);context.arc(225, 225, 10, 0, Math.PI*2, true);context.moveTo(285, 225);context.arc(275, 225, 10, 0, Math.PI*2, true);context.stroke();
```

Puis la bouche.

```
context.moveTo(250, 275);context.arc(250, 275, 50, 0, Math.PI, false); // Pourquoi cette dernière valeur est-elle false ? Pourquoi avez-vous utilisé Math.PI ?context.moveTo(250, 275);context.lineTo(200, 275);context.stroke();
```

Voici à quoi ressemble le produit fini :

Vous l'avez fait, vous venez de créer un emoji de visage souriant ! Bon sang, je suis fier de vous ! Si vous voulez passer vos compétences en canvas au niveau supérieur, essayez l'un des exercices ci-dessous.

### Exercices

1. Dessinez un emoji de caca.
2. Dessinez vos initiales en cursive.

## En résumé

Dans cette leçon, vous avez appris les fonctions : comment créer des fonctions, exécuter des fonctions et utiliser des fonctions pour construire de petits programmes qui dessinent des lignes sur un canvas. Nous avons appris que les fonctions prennent de nombreuses formes et peuvent se voir attribuer des propriétés et des méthodes. J'espère que vous avez apprécié cette leçon, car mon intention était de vous montrer la puissance des fonctions sans vous accabler de jargon, en utilisant plutôt des stimuli visuels pour les rendre vivantes !

Si vous voulez voir tout le code de cette leçon, allez sur mon codepen [ici](http://codepen.io/arecvlohe/pen/QNGjBr/).