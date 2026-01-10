---
title: Comment créer un jeu de mémoire pendant votre temps libre avec Easel.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-03T19:49:51.000Z'
originalURL: https://freecodecamp.org/news/matching-game-with-easel-js-free-time-series-cf803c094a9f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*vc7x8QVmi5I9qDUcAT2zSw.png
tags:
- name: game
  slug: game
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment créer un jeu de mémoire pendant votre temps libre avec Easel.js
seo_desc: 'By Yazed Jamal

  Part of my journey in the programming world is learning about game development.
  I have tried several languages such as Java and C++, but in the end I would like
  to go with Javascript. I have built one game before using JS. The game is ...'
---

Par Yazed Jamal

Une partie de mon parcours dans le monde de la programmation consiste à apprendre le développement de jeux. J'ai essayé plusieurs langages tels que Java et C++, mais au final, j'aimerais utiliser JavaScript. J'ai déjà construit un jeu en utilisant JS. Le jeu s'appelle [Pong Ping](http://yazedjamal.com/pongping/), qui est un clone du jeu Pong. Ce jeu a été construit uniquement avec du JavaScript natif.

Mais aujourd'hui, j'aimerais construire un jeu basé sur un framework de jeu JavaScript appelé Easel.js. Le jeu que je vais construire est en fait très simple : nous retournons des carrés, et s'ils sont de la même couleur, ils disparaissent. Le jeu se terminera lorsque toutes les couleurs seront appariées. Voici un exemple du jeu dans la vidéo ci-dessous, mais ils utilisent des images.

**Étape 1**

Je vais créer le fichier index.html et faire référence à la bibliothèque easel.js. Je choisis d'utiliser un CDN (Content Delivery Network) à cet effet. Je devrai également faire référence à main.js où tout mon code JavaScript sera.

```
#index.html<!DOCTYPE html><html><head> <title>Jeu de Paires</title> <script src="https://code.createjs.com/easeljs-0.8.2.min.js"></script><script src="js/main.js"></script></head><body onload="init()"> <canvas id="myCanvas" width="960" height="600"></canvas></body></html>
```

Je dois m'assurer que tous les éléments DOM sont complètement chargés avant que les scripts JavaScript ne puissent être exécutés, donc j'utilise la méthode onload pour lier le JavaScript via la fonction init().

**Étape 2**

Je vais ensuite créer le fichier main.js et configurer l'environnement easel.js.

```
#js/main.jsvar squarHeight = 200;var squareWidth = 200;
```

```
function init() { var stage = new createjs.Stage("myCanvas"); var square = drawSquare();
```

```
stage.addChild(square); stage.update();}
```

Easel utilise une classe appelée Stage comme conteneur pour afficher tout élément sur le canevas défini. Maintenant, je vais dessiner un carré via la fonction drawSquare. Je vais utiliser toutes les API disponibles de easel.js

```
#js/main.jsfunction drawSquare() { var graphics = new createjs.Graphics().setStrokeStyle(5).beginStroke("rgba(20,20,20,1)") graphics.beginFill(randomColor()).rect(5,5,squareWidth,squareHeight); var shape = new createjs.Shape(graphics); return shape;}
```

```
function randomColor() { var num1 = Math.floor(Math.random()*255); var num2 = Math.floor(Math.random()*255); var num3 = Math.floor(Math.random()*255); return "rgba("+num1+","+num2+","+num3+",1)"; }
```

D'abord, je vais définir la taille du trait que je souhaite utiliser. Ensuite, j'appliquerai le trait avec une couleur spécifique, définir la couleur du carré et créer le carré. La couleur du carré est une couleur aléatoire générée par la fonction randomColor. Voici à quoi cela ressemblera dans le navigateur.

![Image](https://cdn-media-1.freecodecamp.org/images/1*efa3EzNch2A0w_nCE1yrlA.png)

**Étape 3**

Après avoir réussi à rendre un carré avec une couleur aléatoire, je dois concevoir combien de lignes et de colonnes il y aura pour que les carrés remplissent. Je devrai également concevoir l'algorithme pour rendre un carré dans chaque colonne et ligne.

```
#js/main.js##codes mis à jourvar squarHeight = 200;var squareWidth = 200;var squareGap = 10;var column = 3;var row = 2;
```

```
function init() { var stage = new createjs.Stage("myCanvas"); var square;
```

```
for(i=0; i < column*row; i++) {    square = drawSquare();  square.x = (squareWidth+squareGap)*(i%column);  square.y = (squarHeight+squareGap)*Math.floor(i/column);   stage.addChild(square);  stage.update();   }
```

```
}
```

```
function drawSquare() { var graphics = new createjs.Graphics().setStrokeStyle(5).beginStroke("rgba(20,20,20,1)") graphics.beginFill(randomColor()).rect(5,5,squarHeight,squareWidth); var shape = new createjs.Shape(graphics); return shape;}
```

```
function randomColor() { var num1 = Math.floor(Math.random()*255); var num2 = Math.floor(Math.random()*255); var num3 = Math.floor(Math.random()*255); return "rgba("+num1+","+num2+","+num3+",1)"; }
```

À partir des codes ci-dessus, j'obtiendrai un HTML rendu comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*z0H1evsVhzgLNqjZbBHkTg.png)

Il existe de nombreuses façons de mettre en œuvre le rendu des carrés. Nous pourrions utiliser une boucle dans un tableau multidimensionnel, ou nous pourrions manipuler la taille des carrés avec une fonction mathématique. Dans ce cas, j'utiliserai cette dernière méthode. Mais voici l'algorithme si vous souhaitez utiliser la méthode multidimensionnelle :

```
#alternativevar positionX =0; var positionY = 0;
```

```
for(i=0;i<row;i++) {  for(j=0;j<column;j++) {      square = drawSquare();   square.x = positionX;   square.y = positionY;   stage.addChild(square);   stage.update();   positionX += squareWidth+squareGap;   console.log(positionX);  }  positionX = 0;  positionY += squarHeight+squareGap; }
```

**Étape 4**

Encore une fois, l'objectif de ce jeu est de faire correspondre une paire de couleurs ensemble. Je dois donc modifier le code pour qu'il génère des groupes de couleurs par paires. Pour ce faire, j'utiliserai une logique if else pour m'assurer que les deux couleurs similaires sont utilisées lors du rendu des carrés.

```
#js/main.jsvar temp;var genOnce = false;
```

```
function drawSquare() {var color = randomColor();var graphics = new createjs.Graphics().setStrokeStyle(5).beginStroke("rgba(20,20,20,1)")
```

```
 if(!genOnce) {  graphics.beginFill(color).rect(5,5,squarHeight,squareWidth);  temp = color;  genOnce = true; }else {  graphics.beginFill(temp).rect(5,5,squarHeight,squareWidth);  genOnce = false; }
```

```
 var shape = new createjs.Shape(graphics); return shape;}
```

Cela rendra un groupe de carrés comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*u6Tll_9BqW0aOHD9T67Cog.png)

**Étape 5**

Ensuite, je veux que chaque carré soit rendu dans une position aléatoire afin que les paires soient séparées les unes des autres. Cela peut être réalisé en créant d'abord un tableau contenant tous les indices des carrés, puis en mélangeant le tableau afin que le numéro d'index soit placé aléatoirement.

```
#js/main.jsvar squarePlacement = [];
```

```
##fonction pour générer un tableau avec tous les indices des carrésfunction randomDoubleColor() { for(i=0; i<totalTiles;i++) {  squarePlacement.push(i); }  squarePlacement = shuffleArray(squarePlacement);  return squarePlacement;
```

```
}
```

```
##fonction de mélange aléatoire du tableaufunction shuffleArray(array) {    for (var i = array.length - 1; i > 0; i--) {        var j = Math.floor(Math.random() * (i + 1));        [array[i], array[j]] = [array[j], array[i]];    }    return array;}
```

Ensuite, je devrai changer la façon dont je rends le carré. Au lieu d'itérer à travers la longueur du nombre total de carrés, je vais itérer à travers le tableau mélangé aléatoirement.

```
#js/main.jsfunction init() {  var stage = new createjs.Stage("myCanvas"); var square; randomDoubleColor();
```

```
for(i=0; i < squarePlacement.length; i++) {      square = drawSquare();  square.x = (squareWidth+squareGap)*(squarePlacement[i]%column);  square.y = (squarHeight+squareGap)*Math.floor(squarePlacement[i]/column);   stage.addChild(square);  stage.update();   }
```

```
}
```

Cela me donnera un groupe de carrés comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*KR02inRMlBsPSkxSMKR6Iw.png)

Je peux voir l'effet mieux si plus de carrés sont rendus :

![Image](https://cdn-media-1.freecodecamp.org/images/1*N9AHVk0vIfJcplChR5vcQw.png)

**Étape 6**

Mon objectif est maintenant de créer une fonction qui comparera deux carrés qui seront sélectionnés successivement.

```
#js/main.jsvar highlight = createjs.Graphics.getRGB(255, 0, 0);var tileChecked;
```

Je vais commencer par définir une variable highlight. Cela sera utilisé pour mettre en surbrillance les premiers carrés sélectionnés et une variable tileChecked pour stocker le même carré.

```
#js/main.jsfor(i=0; i < squarePlacement.length; i++) {      square = drawSquare();  square.x = (squareWidth+squareGap)*(squarePlacement[i]%column);  square.y = (squarHeight+squareGap)*Math.floor(squarePlacement[i]/column);   stage.addChild(square);  square.addEventListener("click", handleOnPress);  stage.update();   }
```

```
}
```

Je vais ensuite créer un écouteur d'événement qui répondra à un clic de souris et déclenchera la fonction définie, handleOnPress. Maintenant, je vais définir la fonction comme suit :

```
function handleOnPress(e) {  var tile = e.target;  if(!!tileChecked === false) {   tile.graphics.setStrokeStyle(5).beginStroke(highlight).rect(5, 5, squareWidth, squarHeight);   tileChecked = tile;  }else {   if(tileChecked.graphics._fill.style === tile.graphics._fill.style && tileChecked !== tile) {    tileChecked.visible = false;    tile.visible = false;   }else {    console.log("not match");    tileChecked.graphics.setStrokeStyle(5).beginStroke("rgba(20,20,20,1)").rect(5, 5, squareWidth, squarHeight);   }   tileChecked = null;  }    stage.update();
```

```
}
```

En gros, la fonction vérifiera d'abord la variable tileChecked. Si elle est indéfinie, le carré sélectionné sera mis en surbrillance. L'objet carré sélectionné sera enregistré dans la variable tileChecked. Sinon (ce que je m'attends à ce qu'il se produise au deuxième clic), la couleur entre le carré actuellement sélectionné et celui qui est stocké dans la variable tileChecked sera comparée.

Dans cette deuxième comparaison, si la couleur correspond, je ferai disparaître les deux carrés. Si ce n'est pas une correspondance, je retirerai la surbrillance et réinitialiserai la variable tileChecked à indéfinie.

![Image](https://cdn-media-1.freecodecamp.org/images/1*vc7x8QVmi5I9qDUcAT2zSw.png)

**Étape 7**

Pour créer un vrai jeu de puzzle, aucune des couleurs ne doit être affichée. Je vais faire en sorte que les carrés soient recouverts de carrés gris, et lorsqu'on clique sur chacun d'eux, la couleur sera révélée. Ainsi, lorsqu'il n'y a pas de correspondance, le carré gris recouvrira à nouveau la case.

Pour le rendre plus jouable, je vais m'assurer que les autres carrés ne sont pas cliquables pendant la comparaison. Je vais également mettre un certain délai entre le moment où la deuxième couleur est affichée et le moment où les deux carrés disparaissent ou deviennent gris. Certaines modifications doivent être apportées pour que tout fonctionne correctement.

```
function init() {  var stage = new createjs.Stage("myCanvas");  randomDoubleColor();
```

```
for(i=0; i < squarePlacement.length; i++) {    var color =randomColor();  console.log(color);  var square = drawSquare(color);  console.log(square);    square["color"] = square.graphics._fill.style;  square.graphics._fill.style = "rgb(140, 136, 136)";    square.x = (squareWidth+squareGap)*(squarePlacement[i]%column);  square.y = (squareHeight+squareGap)*Math.floor(squarePlacement[i]/column);   stage.addChild(square);  square.addEventListener("click", handleOnPress);  stage.update();   }  function handleOnPress(e) {    var tile = e.target;
```

```
tile.graphics.beginFill(tile.color).rect(5,5,squareHeight,squareWidth);  console.log(tile.mouseEnabled);  tile.mouseEnabled = false;  console.log(tile.mouseEnabled);
```

```
if(!!tileChecked === false) {      tileChecked = tile;  }else {
```

```
stage.mouseChildren = false;   tile.graphics.beginFill(tile.color).rect(5,5,squareHeight,squareWidth);
```

```
setTimeout(function() {    console.log("in");    console.log(tile);    console.log(tileChecked);       if(tileChecked.color === tile.color && tileChecked !== tile) {         tileChecked.visible = false;     tile.visible = false;                }else {    console.log("not match");    tile.graphics.beginFill("rgb(140, 136, 136)").rect(5,5,squareHeight,squareWidth);    tileChecked.graphics.beginFill("rgb(140, 136, 136)").rect(5,5,squareHeight,squareWidth);
```

```
}   tile.mouseEnabled = true;   tileChecked.mouseEnabled = true;   stage.mouseChildren = true;   tileChecked = null;
```

```
stage.update();      }, 1000);              }    stage.update();
```

```
}
```

```
}
```

```
function drawSquare(color) {     var graphics = new createjs.Graphics().setStrokeStyle(5).beginStroke("rgba(20,20,20,1)")
```

```
if(!genOnce) {  graphics.beginFill(color).rect(5,5,squareHeight,squareWidth);  temp = color;  genOnce = true; }else {  graphics.beginFill(temp).rect(5,5,squareHeight,squareWidth);  genOnce = false; }    var shape = new createjs.Shape(graphics); return shape;}
```

Voici une vidéo du jeu en action :

Ce jeu peut être amélioré en ajoutant des règles de victoire ou de défaite, ou peut-être en ajoutant un minuteur pour enregistrer le temps de finition de chaque joueur. Pour l'instant, je vais arrêter le développement à ce stade. Le code complet peut être trouvé sur GitHub ci-dessous, et tout le monde est libre de l'utiliser pour tout autre projet.

[**muyaszed/Matching-game-using-Easel.js**](https://github.com/muyaszed/Matching-game-using-Easel.js)  
[_Contribute to Matching-game-using-Easel.js development by creating an account on GitHub._github.com](https://github.com/muyaszed/Matching-game-using-Easel.js)

[DÉMO](http://yazedjamal.com/guess/)

**Remarques** : Il existe probablement de nombreuses façons de mettre en œuvre cette fonctionnalité, mais cette méthode était la plus simple pour moi. Tout le monde est libre de commenter toute erreur ou amélioration que je peux appliquer. Ce guide est initialement pour moi afin d'apprendre et de me souvenir de ce que j'ai fait. Néanmoins, tout le monde est le bienvenu pour suivre ce guide s'il le trouve utile.