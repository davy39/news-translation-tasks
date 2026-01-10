---
title: comment créer de belles lanternes qui s'organisent en mots
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-20T18:44:06.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-beautiful-lanterns-that-arrange-themselves-into-words-da01ae98238
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca518740569d1a4ca670f.jpg
tags:
- name: algorithms
  slug: algorithms
- name: CSS
  slug: css
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: UX
  slug: ux
seo_title: comment créer de belles lanternes qui s'organisent en mots
seo_desc: 'By Shen Huang

  In this tutorial, we will go through how to create a group of festival lanterns
  that arrange themselves into the words you choose. An online demo can be found here.

  This tutorial is a little bit more advanced than my previous tutorials....'
---

Par Shen Huang

Dans ce tutoriel, nous allons voir comment créer un groupe de lanternes de festival qui s'organisent en mots de votre choix. Une démonstration en ligne peut être trouvée [ici](https://shenhuang.github.io/demo_projects/lanterndemo.html).

Ce tutoriel est un peu plus avancé que mes précédents tutoriels. Je vais supposer que vous pouvez comprendre beaucoup de choses rudimentaires par vous-même. J'ai également réalisé quelques tutoriels pour les débutants complets, que j'ai joints à la fin sous forme de liens.

![Image](https://cdn-media-1.freecodecamp.org/images/1*YOMF0w7NSWU28TH3ViWoNA.gif)
_Lanternes de festival qui s'organisent en mots que vous aimez_

### Introduction

Puisque ce tutoriel est un peu plus long, nous allons passer en revue ce que vous allez lire. Tout d'abord, nous allons voir comment concevoir une lanterne respirante avec CSS. Après cela, nous apprendrons comment créer dynamiquement des lanternes avec JavaScript. Ensuite, nous apprendrons comment créer la boîte de saisie et comment déchiffrer le texte saisi. Après cela, nous passerons en revue quelques algorithmes qui organisent les lanternes de manière appropriée. Enfin, nous apprendrons comment animer les lanternes.

Assez parlé, commençons ! Avant de commencer, vous aurez besoin d'un site web. Si vous ne souhaitez pas utiliser l'un des vôtres, vous pouvez copier le code ci-dessous et l'enregistrer sous forme de fichier .**html**.

```html
<!--Copyright à Shen Huang, vous pouvez me contacter à shenhuang@live.ca-->
<!DOCTYPE html>
<meta name = "viewport" content = "width = device-width, initial-scale = 1.0">
<html>
 <head>
  <title>DÉMO DE LANTERNE</title>
  <style>
   body {
    background-color : #190f00;
   }
  </style>
 </head>
 <body>
</body>
 <script>
</script>
</html>
```

### 1. Conception des lanternes

Nous allons utiliser CSS pour définir les formes et les animations des lanternes, puis les construire à l'intérieur du corps HTML pour tester nos résultats.

La lanterne se compose de 3 parties :

* La **Lumière Extérieure**
* Le **Corps de la Lanterne**
* La **Lumière Intérieure**

La **Lumière Extérieure** est placée derrière le **Corps de la Lanterne**, et la **Lumière Intérieure** est placée devant le **Corps de la Lanterne**. Ces 3 éléments sont placés dans un objet **Lanterne** invisible, qui est responsable des animations de secousse gauche et droite.

![Image](https://cdn-media-1.freecodecamp.org/images/1*XSf4JLICVJK528aesMV12Q.png)
_Lumière Extérieure, Corps de la Lanterne et Lumière Intérieure_

#### **1.1 Lanterne**

L'objet **Lanterne** est essentiellement un objet invisible de la même taille que le **Corps de la Lanterne**. Il a un pivot au centre supérieur, définissant le centre de rotation du mouvement de pendule. Le code CSS suivant définit la **Lanterne**.

```css
@keyframes shake {
 0% {
  transform : rotate(10deg) scale(1);
 }
 50% {
  transform : rotate(-10deg) scale(1);
 }
 100% {
  transform : rotate(10deg) scale(1);
 }
}
.lantern {
 z-index : 999;
 position : absolute;
 height : 70px;
 width : 50px;
 transform-origin : top center;
 animation : shake 4s ease-in-out infinite;
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*OGm3e2kMUuJyPudp0KSrmg.png)
_Lanterne et Pivot de Rotation_

#### **1.2 Lumière Extérieure**

La **Lumière Extérieure** est en fait un dégradé radial d'une couleur vive à la transparence. Les animations font varier sa taille pour lui donner un effet de respiration. La **Lumière Extérieure** peut être définie par le code suivant :

```css
@keyframes outerlightbreathe {
 0% {
  height : 100px;
  width : 100px;
  top : -10px;
  left : -20px;
 }
 50% {
  height : 200px;
  width : 200px;
  top : -60px;
  left : -70px;
 }
 100% {
  height : 100px;
  width : 100px;
  top : -10px;
  left : -20px;
 }
}
.outerLight {
 z-index : -1;
 position : absolute;
 background-image:
  radial-gradient(rgba(117, 107, 60, 1.0), rgba(117, 107, 60, 0.0), rgba(117, 107, 60, 0.0));
 opacity : 0.5;
 border-radius : 50%;
 animation : outerlightbreathe 3s ease-in-out infinite;
}
```

#### **1.3 Corps de la Lanterne**

Le **Corps de la Lanterne** est un rectangle avec une bordure arrondie, avec un arrondi plus prononcé en bas. Le **Corps de la Lanterne** peut être défini par le code suivant :

```css
.lanternBody {
 position : absolute;
 background-color : #756b3c;
 height : 70px;
 width : 50px;
 border-radius : 15px 15px 25px 25px;
}
```

#### **1.4 Lumière Intérieure**

La **Lumière Intérieure**, similaire à la **Lumière Extérieure**, est également un dégradé radial d'une couleur vive à la transparence, mais avec une partie brillante plus grande. L'animation coupe également la lumière lorsqu'elle atteint une certaine taille pour donner l'impression que la lumière est contenue par le **Corps de la Lanterne**. Le code définissant la **Lumière Intérieure** peut être trouvé ci-dessous :

```css
@keyframes innerlightbreathe {
 0% {
  height : 30px;
  width : 30px;
  opacity : 0.1;
  top : 35px;
  left : 10px;
 }
 20% {
  clip-path : inset(0px 0px 0px 0px);
 }
 50% {
  height : 60px;
  width : 60px;
  opacity : 0.5;
  top : 5px;
  left : -5px;
  clip-path : inset(0px 5px 0px 5px);
 }
 80% {
  clip-path : inset(0px 0px 0px 0px);
 }
 100% {
  height : 30px;
  width : 30px;
  opacity : 0.1;
  top : 35px;
  left : 10px;
 }
}
.innerLight {
 position : absolute;
 background-image:
  radial-gradient(rgba(255, 241, 181, 1.0), rgba(255, 241, 181, 1.0), rgba(255, 241, 181, 0.0));
 border-radius : 50%;
 animation : innerlightbreathe 3s ease-in-out infinite;
}
```

#### **1.5 Construction de la Lanterne**

Pour tester notre résultat, nous pouvons utiliser le code CSS et HTML suivant pour construire une lanterne au centre de notre page HTML.

CSS :

```css
center {
 position : absolute;
 top : 50%;
 left : 50%;
}
```

HTML :

```html
<center>
 <div class = "lantern">
  <div class = "outerLight"></div>
  <div class = "lanternBody">
   <div class = "innerLight"></div>
  </div>
 </div>
</center>
```

Une démonstration complète peut être trouvée dans le CODEPEN ci-dessous.

%[https://codepen.io/shenhuang/pen/WPLxEO]

### 2. Création des Lanternes

Maintenant que nous avons appris à dessiner et animer une lanterne, nous pouvons passer au JavaScript qui crée les lanternes dynamiquement. À la fin de cette section, nous verrons également comment organiser les lanternes en mots.

#### 2.1 Création de Lanternes avec JavaScript

Avant de commencer, nous devons également changer l'échelle dans notre animation de lanterne pour la rendre deux fois plus petite. La taille était correcte pour montrer comment une seule lanterne est construite, mais trop grande lorsque nous voulons en montrer plusieurs.

```css
@keyframes shake {
 0% {
  transform : rotate(10deg) scale(0.5);
 }
 50% {
  transform : rotate(-10deg) scale(0.5);
 }
 100% {
  transform : rotate(10deg) scale(0.5);
 }
}
```

Ensuite, nous pouvons utiliser le code suivant pour générer dynamiquement des lanternes. Le **brd** est simplement un espace réservé au cas où nous souhaiterions l'intégrer à d'autres sites web. Le code crée la lanterne dans la même séquence que le script HTML que nous avons utilisé. Il y a de nombreuses autres variables dans ce code, qui auront du sens dans les sections à venir.

```js
var brd = document.createElement("DIV");
document.body.insertBefore(brd, document.getElementById("board"));
const speed = 0.5;
const fadeInTime = 3000;
const fadeOutTime = 3000;
var lanterns = [];
function generateLantern(x, y)
{
 var lantern = document.createElement("DIV");
 var ltrBdy = document.createElement("DIV");
 var otrLit = document.createElement("DIV");
 var inrLit = document.createElement("DIV");
 lantern.setAttribute('class', 'lantern');
 ltrBdy.setAttribute('class', 'lanternBody');
 otrLit.setAttribute('class', 'outerLight');
 inrLit.setAttribute('class', 'innerLight');
 ltrBdy.appendChild(inrLit);
 lantern.appendChild(ltrBdy);
 lantern.appendChild(otrLit);
 brd.appendChild(lantern);
 lantern.FIT = fadeInTime;
 lantern.FOT = fadeOutTime;
 lantern.style.opacity = 1.0;
 // 0: ALIVE, 1: DEAD.
 lantern.state = 0;
 lantern.x = x;
 lantern.y = y;
 lantern.bounce = 0;
 lantern.destination = [];
 lantern.destination.x = x;
 lantern.destination.y = y;
 lantern.arrived = true;
 lantern.style.left = lantern.x + "px";
 lantern.style.top = lantern.y + "px";
 if(lanterns == null)
  lanterns = [];
 lanterns.push(lantern);
 return lantern;
}
```

Nous pouvons tester ce code avec le code suivant, qui devrait générer une lanterne à **x:100**, **y:100**.

```
generateLantern(100, 100);
```

#### 2.2 Carte de Mots pour les Lanternes

Maintenant, pour que les lanternes affichent un mot particulier, nous aurons besoin d'une carte pour chaque lettre de l'alphabet. Une carte de mots pour lanternes peut être trouvée dans ce [GitHub Gist](https://gist.github.com/shenhuang/f88d33c2dc85c7e09ee02bc17b3e86c4), qui ne sera pas montré ici en raison de sa taille.

Une fois terminé, vous pouvez tester pour voir si la carte de mots a fonctionné avec le code ci-dessous, qui dessine le mot "LOVE".

```js
var xstart = 50;
var ystart = 100;
var xspace = 50;
var yspace = 50;
var letter = "L";
for(i = 0; i < ltrMap[letter][0].length; i++)
{
 for(j = 0; j < ltrMap[letter].length; j++)
 {
  if(ltrMap[letter][j][i] == 1)
  {
   generateLantern(xstart + i * xspace, ystart + j * yspace);
  }
 }
}
var xstart = 350;
var letter = "O";
for(i = 0; i < ltrMap[letter][0].length; i++)
{
 for(j = 0; j < ltrMap[letter].length; j++)
 {
  if(ltrMap[letter][j][i] == 1)
  {
   generateLantern(xstart + i * xspace, ystart + j * yspace);
  }
 }
}
var xstart = 650;
var letter = "V";
for(i = 0; i < ltrMap[letter][0].length; i++)
{
 for(j = 0; j < ltrMap[letter].length; j++)
 {
  if(ltrMap[letter][j][i] == 1)
  {
   generateLantern(xstart + i * xspace, ystart + j * yspace);
  }
 }
}
var xstart = 950;
var letter = "E";
for(i = 0; i < ltrMap[letter][0].length; i++)
{
 for(j = 0; j < ltrMap[letter].length; j++)
 {
  if(ltrMap[letter][j][i] == 1)
  {
   generateLantern(xstart + i * xspace, ystart + j * yspace);
  }
 }
}
```

Consultez la démonstration CODEPEN ci-dessous :

%[https://codepen.io/shenhuang/pen/vbvZgB]

### 3. Déchiffrement des Saisies de Mots

#### 3.1 Création de la Boîte de Saisie.

La **Boîte de Saisie** s'estompe et prend les entrées. Une fois les entrées prises, les lanternes doivent commencer à s'organiser. La **Boîte de Saisie** s'estompera jusqu'à ce que les lanternes soient complètement organisées. Afin d'accomplir un tel effet, nous supprimons la **Boîte de Saisie** une fois qu'elle a pris son entrée et créons une **Fausse Boîte de Saisie** au même endroit. Nous estompons ensuite la **Fausse Boîte de Saisie** à la place.

![Image](https://cdn-media-1.freecodecamp.org/images/1*WwrIOe6g_0RD9CUNGk5Tig.png)
_Mécanismes de la Boîte de Saisie_

Pour commencer, nous définissons d'abord la **Boîte de Saisie** en HTML, puis le style et les animations en CSS. Pour ce projet, notre **Boîte de Saisie** n'accepte que 5 lettres majuscules, et le contenu par défaut à l'intérieur est "**LOVE**".

HTML :

```html
<input  id   = "wordBox"
  class  = "wordInput"
  type  = "text"
  maxlength = "5"
  value  = "LOVE"
  onkeypress = "return (event.charCode > 64 && event.charCode < 91)"
>
```

CSS :

```css
@keyframes fadein {
 0% {
  opacity : 0.0;
 }
 100% {
  opacity : 1.0;
 }
}
@keyframes fadeout {
 0% {
  opacity : 1.0;
 }
 50% {
  opacity : 0.0;
 }
 100% {
  opacity : 0.0;
 }
}
.wordInput, .fakeInput{
 position : absolute;
 bottom : 25px;
 left : 25px;
}
.wordInput {
 height : 30px;
 width : 100px;
 color : #a88600;
 font-size : 25px;
 font-family : Arial;
 text-align : center;
 border : 3px;
 border-radius : 15px;
 border-style : solid;
 background-color : #fff9e5;
 border-color : #fff9e5;
 animation : fadein 1s ease-in;
}
.wordInput:hover,  .wordInput:focus{
 border-color : #a88600;
}
.fakeInput {
 height : 30px;
 width : 100px;
 color : #a88600;
 font-size : 25px;
 font-family : Arial;
 text-align : center;
 border : 3px;
 border-radius : 15px;
 border-style : solid;
 background-color : #fff9e5;
 border-color : #fff9e5;
 animation : fadeout 2s ease-out;
}
```

Maintenant, nous devrions pouvoir voir une **Boîte de Saisie** dans le coin inférieur droit de la page web. Nous utilisons ensuite le code JavaScript suivant pour qu'elle prenne les entrées. Une fois que l'utilisateur change de focus, elle crée une **Fausse Boîte de Saisie** avec la même entrée pour s'estomper.

```js
var wordBox = document.getElementById("wordBox");
var word = "";
wordBox.addEventListener("focusout", wordBoxFocusOut);
function wordBoxFocusOut()
{
 word = wordBox.value;
 var fakeBox = document.createElement("DIV");
 fakeBox.setAttribute('class', 'fakeInput');
 fakeBox.textContent = word;
 wordBox.style.display = "none";
 brd.appendChild(fakeBox);
 setTimeout(function(){
  fakeBox.parentNode.removeChild(fakeBox);
 }, 2000);
 arrangeLanterns(word);
 wordBox.addEventListener("focusout", wordBoxFocusOut);
}
```

Nous devons également ajouter le code JavaScript suivant pour qu'elle s'estompe après que la touche **Entrée** soit pressée. Le **enterPressed** est là pour empêcher le script de s'exécuter deux fois.

```js
window.onkeydown = function(e)
{
 key = e.keyCode;
 if(key == 13)
 {
  wordBox.blur();
 }
};
```

Une fois terminé, nous devrions pouvoir voir une **Boîte de Saisie** qui s'estompe, et s'estompe une fois que la touche **Entrée** est pressée ou que la boîte est hors focus.

%[https://codepen.io/shenhuang/pen/yZGXop]

#### 3.2 Traitement de l'Entrée

Maintenant que nous avons la **Boîte de Saisie** prête, nous devons tester et voir si elle peut traiter correctement l'entrée. Pour ce faire, nous ajoutons d'abord le code suivant à la fin de notre fonction **wordBoxFocusOut()**.

```
arrangeLanterns(word);
```

Ensuite, nous pouvons définir notre fonction **arrangeLanterns()**.

```js
function arrangeLanternsChar(char, charCount)
{
 for(i = 0; i < ltrMap[char][0].length; i++)
 {
  for(j = 0; j < ltrMap[char].length; j++)
  {
   if(ltrMap[char][j][i] == 1)
   {
    generateLantern(xstart + i * xspace + xsplit * charCount, ystart + j * yspace);
   }
  }
 }
}
```

Une fois terminé, nous devrions pouvoir voir quelque chose comme montré par la démonstration suivante, où un groupe de lanternes sera imprimé pour correspondre à l'entrée.

%[https://codepen.io/shenhuang/pen/jdXwza]

### 4. Organisation des Lanternes

Maintenant, cette partie peut être un peu aride. Nous ne pourrons pas voir les effets jusqu'à ce que nous animions les lanternes, et le contenu est plutôt théorique. Mais ces théories sont essentielles pour créer efficacement les effets sympas à la fin.

Nous allons d'abord passer en revue notre problème, puis introduire 2 algorithmes qui résolvent le problème de manière efficace. Pour ceux qui savent déjà, nous allons essayer de minimiser la distance totale parcourue par les lanternes. Pour ce faire, nous allons utiliser un **arbre k-d** et un peu de **programmation dynamique**.

#### 4.2 Calcul de la Distance Totale la Plus Courte

Tout d'abord, nous devons définir notre problème. Nous avons des **destinations** définies par nos entrées de mots, où les lanternes doivent se retrouver dans ces positions pour afficher le mot. Nous voudrions autant de lanternes que de **destinations**, et nous allons les générer à des emplacements aléatoires sur l'écran. Ces lanternes voleront ensuite vers les destinations, mais nous voulons que les distances totales parcourues par toutes les lanternes soient minimales. Nous voulons également une lanterne par **destination**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*dm_Iy7Mz_EzLIpwxTi0tAQ.png)
_Mauvais Routage, Bon Routage et Routage Désorganisé Démontés_

Pour accomplir cela, nous devons modifier notre code avec ce qui suit. Le code effectue 4 opérations majeures en séquence :

1. Calculer le nombre total de lanternes requises.
2. Générer des lanternes supplémentaires à des emplacements aléatoires s'il y a plus de lanternes requises que nous en avons sur le terrain.
3. Définir la destination de chaque lanterne à leur destination la plus proche avec l'aide de l'**arbre k-d**.
4. Optimiser davantage la destination de chaque lanterne avec la **programmation dynamique**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*XNavUAdtGT98jz-DxPZ4MA.png)
_Étapes de Définition de la Destination pour les Lanternes Illustrées_

Pour tester correctement notre code, nous devons commenter les parties que nous n'avons pas encore abordées. Nous entrerons dans les détails du code très bientôt.

```js
var distance = function(a, b){
 return Math.pow(a.x - b.x, 2) +  Math.pow(a.y - b.y, 2);
}
var lanternDesinationTree;
var arrivedCount = 0;
var requiredLanterns = 0;
function arrangeLanterns(word)
{
 requiredLanterns = 0;
 for(c = 0; c < word.length; c++)
 {
  requiredLanterns += ltrMap[word[c]].lanternCount;
 }
 while(lanterns.length < requiredLanterns)
 {
  generateLantern(window.innerWidth * Math.random(), window.innerHeight * Math.random());
 }
 lanternDestinationTree = new kdTree([], distance, ["x", "y"]);
 for(c = 0; c < word.length; c++)
 {
  appendLanternDestinations(word[c], c);
 }
 for(i = 0; i < lanterns.length; i++)
 {
  if(i < requiredLanterns)
  {
   var nearest = lanternDestinationTree.nearest(lanterns[i].destination, 1);
   lanternDestinationTree.remove(nearest[0][0]);
   lanterns[i].destination = nearest[0][0];
   lanterns[i].arrived = false;
  }
  else
  {
   lanterns[i].state = 1;
  }
 }
 optimizeTotalDistance();
}
```

#### 4.2.1 Arbre k-d

Pour trouver la distance totale la plus courte, nous aurons besoin de quelque chose appelé **arbre k-d**. L'**arbre k-d** est une structure de données qui nous permet de mapper des coordonnées multidimensionnelles et d'effectuer des actions sur elles plus efficacement. Si vous êtes intéressé à en apprendre davantage sur les **arbres k-d** et la complexité d'exécution, vous pouvez trouver plus d'informations [ici](https://en.wikipedia.org/wiki/K-d_tree).

![Image](https://cdn-media-1.freecodecamp.org/images/1*mXPNeON48dlKFSURIX2Cjw.png)
_Visualisation d'un arbre k-d_

Pour implémenter l'**arbre k-d**, nous devons d'abord télécharger l'**arbre k-d** de **Ubilabs**. Le fichier .**js** peut être trouvé [ici](https://github.com/ubilabs/kd-tree-javascript/blob/master/kdTree.js) sur GitHub et les guides d'implémentation peuvent être trouvés sur la page principale GitHub [ici](https://github.com/ubilabs/kd-tree-javascript). Une fois que vous l'avez dans le même dossier que votre fichier **_._html**, vous pouvez le référencer avec les scripts HTML suivants :

```html
<script src = "./kdTree.js"  type= "text/javascript" ></script>
```

Vous pouvez ensuite tester pour voir si votre **arbre k-d** a fonctionné avec le code suivant (les 2 points les plus proches retournés doivent être imprimés dans la console).

```js
var points = [
 {x: 1, y: 2},
 {x: 3, y: 4},
 {x: 5, y: 6},
 {x: 7, y: 8}
];
var distance = function(a, b){
 return Math.pow(a.x - b.x, 2) +  Math.pow(a.y - b.y, 2);
}
var tree = new kdTree(points, distance, ["x", "y"]);
var nearest = tree.nearest({ x: 5, y: 5 }, 2);
console.log(nearest);
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*_o29n8O7tT8I8pTcOIy07A.gif)
_Test de l'arbre k-d_

Et maintenant nous pouvons construire notre fonction **appendLanternDestinations()** avec l'**arbre k-d**.

```js
function appendLanternDestinations(char, charCount)
{
 for(i = 0; i < ltrMap[char][0].length; i++)
 {
  for(j = 0; j < ltrMap[char].length; j++)
  {
   if(ltrMap[char][j][i] == 1)
   {
    var destination = {};
    destination.x = xstart + i * xspace + xsplit * charCount;
    destination.y = ystart + j * yspace;
    lanternDestinationTree.insert(destination);
   }
  }
 }
}
```

Pour tester, nous pouvons modifier notre fonction **arrangeLanterns()** pour ajouter le code suivant. Nous devrions alors voir la console imprimer la distance la plus proche avec l'**arbre k-d** construit par notre entrée de mot.

```js
lanternDestinationTree = new kdTree([], distance, ["x", "y"]);
for(c = 0; c < word.length; c++)
{
 appendLanternDestinations(word[c], c);
}
// Test kdTree avec les destinations des lanternes.
var nearest = lanternDestinationTree.nearest({ x: 200, y: 200 }, 1);
console.log(nearest[0][0]);
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*Td8hiF-WrwQpVeQOqzmQ6g.gif)
_Test de appendLanternDestinations()_

Maintenant, le code sous la fonction d'ajout définit la destination de chaque lanterne à leur destination disponible la plus proche. Pour les lanternes supplémentaires, leur état est défini à 1, ce qui signifie qu'elles doivent s'estomper par le contrôleur d'animation que nous aborderons dans la section suivante.

#### 4.2.2 Programmation Dynamique

L'optimisation de l'**arbre k-d** est bonne, mais pas parfaite. Nous aurons besoin de la **programmation dynamique** pour nous assurer que l'algorithme retourne la distance totale minimale. La **programmation dynamique** est le concept où vous essayez de trouver la solution optimisée en approchant progressivement un meilleur état à partir d'un état précédemment stocké.

L'algorithme que nous utilisons est en fait similaire au **tri à bulles**, qui peut être décrit comme suit :

1. Nous itérons à travers chaque paire de lanternes.
2. Nous vérifions si l'échange des destinations d'une paire de lanternes donne une distance totale plus courte.
3. Nous échangeons leurs destinations si la distance totale est plus courte.
4. Pour les lanternes qui sont **"_MORTES_"**, leur distance par rapport à la destination est considérée comme 0, l'échange fait que l'autre lanterne a une distance de 0 par rapport à la destination.
5. Se termine lorsqu'aucun autre échange ne peut être fait pour raccourcir la distance.

![Image](https://cdn-media-1.freecodecamp.org/images/1*jak49w6h8Dra4zYUZPtexQ.png)
_Algorithme Illustré, Échange Incrémental pour une Distance Totale Plus Courte_

L'implémentation du code de cet algorithme peut être trouvée ci-dessous. Nous devons également gérer leurs états et leur statut d'arrivée, ce qui sera expliqué plus en détail dans la section suivante. Remarquez que la formule de distance n'est pas racine carrée, ce qui signifie que l'algorithme punira fortement les distances plus longues.

```js
function optimizeTotalDistance()
{
 var undone = true;
 while(undone)
 {
  undone = false;
  for(i = 0; i < lanterns.length; i++)
  {
   var lanternA = lanterns[i];
   for(j = 0; j < lanterns.length; j++)
   {
    var lanternB = lanterns[j];
    if(lanternA.state == 0 && lanternB.state == 0)
    {
     var oldDistance = distance(lanternA, lanternA.destination) + distance(lanternB, lanternB.destination);
     var newDistance = distance(lanternA, lanternB.destination) + distance(lanternB, lanternA.destination);
     if(newDistance < oldDistance)
     {
      [lanternA.destination, lanternB.destination] = [lanternB.destination, lanternA.destination];
      undone = true;
     }
    }
    else if(lanternA.state == 0 && lanternB.state == 1)
    {
     var oldDistance = distance(lanternA, lanternA.destination);
     var newDistance = distance(lanternB, lanternA.destination);
     if(newDistance < oldDistance)
     {
      lanternB.destination = {x: lanternA.destination.x, y: lanternA.destination.y};
      lanternA.destination = {x: lanternA.x, y: lanternA.y};
      lanternA.state = 1;
      lanternB.state = 0;
      lanternA.arrived = true;
      lanternB.arrived = false;
      undone = true;
     }
    }
    else if(lanternA.state == 1 && lanternB.state == 0)
    {
     var oldDistance = distance(lanternB, lanternB.destination);
     var newDistance = distance(lanternA, lanternB.destination);
     if(newDistance < oldDistance)
     {
      lanternA.destination = {x: lanternB.destination.x, y: lanternB.destination.y};
      lanternB.destination = {x: lanternB.x, y: lanternB.y};
      lanternA.state = 0;
      lanternB.state = 1;
      lanternA.arrived = false;
      lanternB.arrived = true;
      undone = true;
     }
    }
   }
  }
 }
}
```

### 5. Animation des Lanternes

C'est enfin la dernière section ! Nous allons maintenant compléter ce projet. Beaucoup de mystères mentionnés dans les sections précédentes seront expliqués ici. Accrochez-vous, le spectacle magique est sur le point de commencer.

#### 5.1 Fondu d'Entrée et de Sortie avec JavaScript

Maintenant, au cas où vous vous demandiez à quoi servent **lantern.FIT** et **lantern.FOT** dans **generateLantern()**, voici la réponse : cela permet en fait au contrôleur d'animation de faire un fondu d'entrée des lanternes après leur création, et un fondu de sortie après qu'elles soient **"_MORTES_"**.

Pour que cela se produise, nous devons d'abord apporter quelques modifications au script, afin que les lanternes soient initialement transparentes.

Nous devons changer :

```
lantern.style.opacity = 1.0;
```

en :

```
lantern.style.opacity = 0.0;
```

Après cela, nous pouvons construire notre contrôleur d'animation avec le code ci-dessous. Le **spedFctr** définit la vitesse à laquelle les lanternes doivent se déplacer. Le **arivThsh** définit la tolérance du programme pour considérer que la lanterne est arrivée à destination. Le **bonsFctr** définit la vitesse à laquelle la lanterne doit rebondir de haut en bas, et **bonsMrgn** définit l'amplitude du rebond. Ces paramètres auront plus de sens plus tard.

Le contrôleur d'animation se rafraîchit toutes les 10 millisecondes, résultant en un taux de rafraîchissement de 100 fps. Pour l'instant, il décroît lentement le compteur **lantern.FIT** et définit l'opacité en conséquence pour les lanternes nouvellement créées. Il fera l'inverse pour les lanternes qui sont mortes. Une fois que **lantern.FOT** atteint zéro pour les lanternes mortes, elles seront supprimées définitivement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*fGbd7MiAHwNYnl1joQYOuw.png)
_Animation de Fondu d'Entrée et de Sortie Expliquée_

```js
const spedFctr = 0.025;
const arivThsh = 5 * spedFctr;
const bonsFctr = 0.001;
const bonsMrgn = 5;
var before = Date.now();
var id = setInterval(frame, 10);
function frame()
{
 var current = Date.now();
 var deltaTime = current - before;
 before = current;
 for(i in lanterns)
 {
  var lantern = lanterns[i];
  switch(lantern.state)
  {
   case 0:
    if(lantern.FIT > 0)
    {
     lantern.FIT -= deltaTime;
     lantern.style.opacity = 1 - lantern.FIT / fadeOutTime;
    }
    break;
   case 1:
    if(lantern.FOT > 0)
    {
     lantern.FOT -= deltaTime;
     lantern.style.opacity = lantern.FOT / fadeOutTime;
    }
    else
    {
     lantern.parentNode.removeChild(lantern);
     lanterns.splice(i, 1);
    }
    break;
  }
 }
}
```

#### 5.2 Animations de Mouvement

Maintenant, pour animer les lanternes, nous ajoutons le code suivant sous le cas 1 à l'intérieur de la boucle for du contrôleur d'animation. Le code incrémente lentement la position des lanternes vers leurs destinations. Une fois que les lanternes atteignent leur destination, elles sont marquées comme arrivées et le compteur d'arrivée est incrémenté.

```js
var xDiff = lantern.destination.x - lantern.x;
var yDiff = lantern.destination.y - lantern.y;
var dDiff = Math.sqrt(xDiff * xDiff + yDiff * yDiff);
if(!lantern.arrived)
{
 if(Math.abs(dDiff) < arivThsh)
 {
  lantern.arrived = true;
  arrivedCount++;
 }
 else
 {
  lantern.x += xDiff / dDiff * spedFctr * deltaTime;
  lantern.y += yDiff / dDiff * spedFctr * deltaTime;
 }
 lantern.style.left = lantern.x + "px";
}
else
{
 lantern.bounce += bonsFctr * deltaTime;
}
lantern.style.top = lantern.y + Math.sin(lantern.bounce) * bonsMrgn + "px";
```

Nous utilisons le code suivant pour vérifier si toutes les lanternes sont arrivées toutes les 0,1 seconde. Une fois que toutes les lanternes sont arrivées, nous ramenons le champ de saisie.

```js
var gr = setInterval(check, 100);
function check()
{
 if(arrivedCount == requiredLanterns)
 {
  wordBox.style.display = "inline";
  arrivedCount = 0;
 }
}
function check()
{
 if(arrivedCount == requiredLanterns)
 {
  wordBox.style.display = "inline";
  arrivedCount = 0;
 }
}
```

Félicitations !!! Vous avez maintenant appris à créer un groupe de lanternes qui s'organisent pour afficher les mots que vous aimez. Une démonstration du projet complet peut être trouvée [ici](https://shenhuang.github.io/demo_projects/lanterndemo.html). J'espère que vous passerez une excellente Fête des Lanternes !!!

![Image](https://cdn-media-1.freecodecamp.org/images/1*ItI-xPxzFVNltQHf8Vt5YA.gif)
_Hello World pour la Démo de Lanternes_

### Mots à la Fin

La Fête des Lanternes Chinoises cette année est le 19 février. Si vous vivez dans une petite ville chinoise, vous verrez l'esprit du festival grandir dans les rues. À l'époque, ce festival illuminé est en fait l'équivalent chinois de la Saint-Valentin. Les garçons et les filles sortent dans les rues en espérant rencontrer leur âme sœur et envoient des lanternes artisanales qui sont censées exaucer les vœux dans le temps à venir de l'année.

J'ai quelques guides précédents sur des projets similaires.

**Débutant :**

* [comment remplir votre site web avec de jolis COEURS DE LA SAINT-VALENTIN](https://medium.com/front-end-weekly/how-to-fill-your-website-with-lovely-valentines-hearts-d30fe66d58eb)
* [comment ajouter des FEUX D'ARTIFICE à votre site web](https://medium.com/front-end-weekly/how-to-add-some-fireworks-to-your-website-18b594b06cca)
* [comment ajouter des BULLES à votre site web](https://medium.com/front-end-weekly/how-to-add-some-bubbles-to-your-website-8c51b8b72944)

**Avancé :**

* [comment faire tomber des CHAPEAUX DE LEPRECHAUN dans votre site web avec la VISION PAR ORDINATEUR](https://medium.freecodecamp.org/how-to-drop-leprechaun-hats-into-your-website-with-computer-vision-b0d115a0f1ad)

Je suis passionné par la programmation et j'adorerais apprendre de nouvelles choses. Je crois que le savoir peut rendre le monde meilleur et je suis donc motivé à partager. Faites-moi savoir si vous êtes intéressé à lire quelque chose en particulier.