---
title: Faire pleuvoir du code — Style Matrix
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-04-15T00:15:54.000Z'
originalURL: https://freecodecamp.org/news/canmaking-it-rain-code-matrix-style-ec6e1386084e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*KgmujbLEB5TS1PQcPycPGg.png
tags:
- name: Design
  slug: design
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: Faire pleuvoir du code — Style Matrix
seo_desc: 'By Kurt

  An introduction to HTML 5 canvas animations

  Out of all the great things HTML 5 brought us, I love the canvas element the most.
  I hope that once you see how powerful it is, you’ll want to put in the time to master
  canvas animations yourself.

  W...'
---

Par Kurt

#### Une introduction aux animations HTML 5 canvas

Parmi toutes les grandes choses que HTML 5 nous a apportées, j'adore l'élément canvas. J'espère qu'une fois que vous verrez à quel point il est puissant, vous voudrez prendre le temps de maîtriser les animations canvas vous-même.

#### Qu'est-ce qu'un canvas ?

Un canvas est exactement ce que son nom implique. C'est une toile vierge sur laquelle vous pouvez peindre comme vous le souhaitez et la rendre dans votre navigateur sous forme d'image. La vraie beauté est qu'il permet non seulement de créer des images, mais aussi de les redessiner et de les rendre continuellement — créant ainsi une animation.

Le pouvoir du canvas est limité seulement par votre imagination. J'ai utilisé l'élément canvas pour créer tout, des images statiques à la volée aux jeux, aux interfaces utilisateur graphiques, et même un constructeur d'emails style MailChimp. Vous pouvez même rendre le canvas en 3D !

Pour moi, l'élément canvas a tout changé. Je n'étais plus limité à utiliser les balises HTML par défaut. Je pouvais créer tout ce que je voulais dans le navigateur. Et vous pouvez être sûr que cela a poussé mes compétences en JavaScript à un tout nouveau niveau.

#### Installation

Au lieu de démontrer comment simplement dessiner sur un canvas, je veux vous donner un aperçu de ce que vous pouvez créer avec. Si vous n'avez pas encore vu The Matrix, arrêtez de lire maintenant et allez le regarder. Si vous l'avez vu, vous reconnaîtrez le célèbre « code qui tombe » du titre. Créons cela avec canvas !

Au lieu de faire un tutoriel étape par étape, pour gagner du temps, je vais poster le code ci-dessous et vous l'expliquer en détaillant ce que chaque partie fait au fur et à mesure.

Le HTML :

```
<canvas id="canvas" width="600px" height="400px"></canvas><img id="logo" width="400px;" src="https://s3.amazonaws.com/freecodecamp/freecodecamp_logo.svg"/>
```

Le CSS :

```
body{ background-color:#d2d2d2;}#canvas{ background-color:#000; display:block; margin:auto;}#logo{ display:none;}
```

Le JavaScript :

```
var canvas = document.getElementById('canvas');var ctx = canvas.getContext('2d');var t = text();var logo = document.getElementById('logo');var lines = [];window.setInterval(draw, 100);
```

```
function draw() { if (Math.floor(Math.random() * 2) === 0 && lines.length < 100) {  lines.push(new textLine()); } ctx.clearRect(0, 0, canvas.width, canvas.height); lines.forEach(function(tl) {
```

```
  ctx.drawImage(tl.text, tl.posX, tl.animate(), 20, 1000); }); ctx.drawImage(logo, 100, 155, 400, 70);
```

```
}
```

```
function textLine() { this.text = t; this.posX = (function() {  return Math.floor(Math.random() * canvas.width); })(); this.offsetY = -1000; this.animate = function() {  if (this.offsetY >= 0) {   this.offsetY = -1000;  }  this.offsetY += 10;  return this.offsetY; };}
```

```
function text() { var offscreenCanvas = document.createElement('canvas'); offscreenCanvas.width = "30"; offscreenCanvas.height = "1000"; offscreenCanvas.style.display = "none"; document.body.appendChild(offscreenCanvas); var octx = offscreenCanvas.getContext('2d'); octx.textAlign = "center"; octx.shadowColor = "lightgreen"; octx.shadowOffsetX = 2; octx.shadowOffsetY = -5; octx.shadowBlur = 1; octx.fillStyle = 'darkgreen'; octx.textAlign = "left"; var step = 10; for (i = 0; i < 100; i++) {  var charCode = 0;  while (charCode < 60) {   charCode = Math.floor(Math.random() * 100);  }  octx.fillText(String.fromCharCode(charCode), 0, step);  step += 10; } return offscreenCanvas;}
```

#### Comment cela fonctionne-t-il ?

À la ligne #1, nous récupérons l'élément canvas par son id. Chaque élément canvas a son propre _contexte_ — une interface pour manipuler son contenu. C'est à cela que la variable _ctx_ à la ligne 2 fait référence.

Pour créer l'arrière-plan animé, nous aurons besoin d'une ligne verticale de texte aléatoire, que nous redessinerons plusieurs fois sur l'axe X et animerons incrémentalement sur l'axe Y pour obtenir l'effet final.

Puisque le texte est toujours rendu horizontalement, nous allons rendre le texte sur _un autre_ canvas invisible et le dessiner en tant qu'image sur notre canvas original.

À la ligne #3, nous définissons la variable _t_ comme résultat de la fonction _text()_ qui génère et retourne notre élément canvas invisible.

Dans cette fonction, nous créons un nouveau canvas, définissons sa largeur et sa hauteur, définissons sa propriété d'affichage sur none pour le cacher, puis l'ajoutons au corps du document. Ensuite, nous définissons la couleur, l'ombre et le décalage pour le texte que nous allons dessiner.

Pour générer des caractères aléatoires verticaux, nous bouclons et dessinons un nouveau caractère aléatoire 100 fois et l'incrémentons de 10px sur l'axe Y à chaque intervalle. Pour générer un caractère aléatoire, j'utilise _Math.random()_ pour obtenir un nombre entre 60 et 100, puis le convertir en caractère en utilisant _String.fromCharCode()._

Cela dessine notre texte vertical avec une ombre et retourne le canvas à la variable t.

#### La boucle d'animation

Sur les 3 lignes de code suivantes, je récupère le logo FreeCodeCamp, déclare un tableau qui contiendra les lignes séparées qui composent l'arrière-plan, et utilise _window.setInterval_ pour exécuter la fonction _draw()_ toutes les 100 millisecondes.

Lors de l'animation d'un canvas, il est bon de plutôt utiliser _window.requestAnimationFrame(),_ mais j'ai pensé que cela était trop confus pour les débutants, car il est un peu délicat de définir le taux de rafraîchissement.

La première chose que fait la fonction _draw()_ est de générer un nombre aléatoire entre 1 et 0. Si le nombre est 0 et qu'il y a moins de 100 lignes de texte individuelles animées en arrière-plan, elle ajoute une nouvelle _textLine()_ dans le tableau des lignes.

La fonction _textLine()_ retourne un objet qui contient

1. Le texte vertical résultant contenu dans la variable _t_.
2. Le montant du décalage auquel il sera rendu sur l'axe X (généré aléatoirement à chaque instance de l'objet).
3. Un décalage initial de -1000px sur l'axe Y qui le place juste au-dessus du canvas.
4. Une méthode animate qui ajoute 10px à l'axe Y chaque fois qu'elle est appelée et retourne le résultat, faisant descendre le texte. Si le décalage de l'axe Y atteint 0, il est réinitialisé à -1000px, fournissant une animation continue.

Le canvas est effacé, puis la fonction _draw()_ parcourt chaque ligne de texte dans le tableau _lines_ et la dessine sur le canvas en appelant sa méthode _animate_ chaque fois qu'une ligne est dessinée pour la faire descendre.

Puisque chaque ligne a un décalage aléatoire sur l'axe X et qu'une nouvelle ligne est ajoutée à des intervalles aléatoires, les lignes de texte tombent à des rythmes différents sur le canvas, créant l'effet de code qui pleut !

Enfin, le logo FreeCodeCamp est dessiné sur l'arrière-plan, nous donnant notre animation finale.

#### Où aller maintenant ?

Si le canvas est quelque chose qui vous intéresse, vous pouvez en apprendre davantage à ce sujet dans les [Mozilla Docs](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API#Guides_and_tutorials).

Je prévois de créer une série de tutoriels plus basiques, étape par étape, expliquant les animations canvas dès que j'aurai le temps.

Si vous n'avez pas trouvé le code ci-dessus trop difficile et que vous aimeriez le modifier, voici quelques idées sympas :

1. Rendez les dimensions dynamiques afin que le canvas s'adapte et continue de s'animer lorsque vous redimensionnez votre navigateur.
2. Au lieu de générer des caractères aléatoires, récupérez un fichier de votre propre code depuis GitHub et animez-le à la place.
3. Remplacez le logo FreeCodeCamp par votre nom et faites-le ressembler à l'affiche de Matrix.
4. Au lieu de générer chaque ligne de manière aléatoire, liez un événement de clic au canvas et dessinez une nouvelle ligne aux coordonnées X de votre clic de souris.

J'espère que vous avez apprécié cette introduction. Si c'est le cas, n'hésitez pas à consulter certains des autres articles que j'ai écrits.

[**Transformer du code en argent — Comment gagner de l'argent en tant que développeur Web et vivre pour en parler.**](https://medium.com/p/f5eedc557b3e)
[_Vous venez d'apprendre à coder. Vous êtes enthousiaste et quiconque ne sait pas coder pense que vous êtes un génie, la nouvelle se répand et tout le monde..._medium.com](https://medium.com/p/f5eedc557b3e)
[**Comment écrire une bibliothèque similaire à jQuery en 71 lignes de code — Apprendre sur le DOM**](https://medium.com/p/e9fb99dbc8d2)
[_Les frameworks JavaScript sont à la mode. Il est probable que tout flux d'actualités lié à JavaScript que vous ouvrez sera rempli..._medium.com](https://medium.com/p/e9fb99dbc8d2)
[**5 choses à retenir lorsque vous apprenez à programmer**](https://medium.com/p/1ed8e734b04f)
[_Apprendre à programmer est un défi. En plus de choisir un langage ou de configurer un environnement de développement que vous..._medium.com](https://medium.com/p/1ed8e734b04f)
[**Comment je suis devenu programmeur. Et quand j'ai commencé à m'appeler ainsi**](https://medium.com/p/54a0533c4335)
[_J'ai voulu commencer à bloguer sur la programmation depuis des mois maintenant et comme tant d'autres avant moi, je me suis lancé plein d'..._medium.com](https://medium.com/p/54a0533c4335)
[**Programmation préventive — comment corriger les bugs avant qu'ils n'arrivent**](https://medium.com/p/9df82cf215c5)
[_...et pourquoi Sherlock Holmes aurait été un programmeur brillant_medium.com](https://medium.com/p/9df82cf215c5)