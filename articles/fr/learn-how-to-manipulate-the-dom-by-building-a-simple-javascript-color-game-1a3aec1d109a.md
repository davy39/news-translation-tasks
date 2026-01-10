---
title: Apprenez à manipuler le DOM en créant un simple jeu de couleurs en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-20T19:01:21.000Z'
originalURL: https://freecodecamp.org/news/learn-how-to-manipulate-the-dom-by-building-a-simple-javascript-color-game-1a3aec1d109a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*5dbaz5S1Buevb-fZQDbYzg.jpeg
tags:
- name: Games
  slug: games
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Apprenez à manipuler le DOM en créant un simple jeu de couleurs en JavaScript
seo_desc: 'By Ashish Nandan Singh

  What is the DOM ?

  DOM stands for Document Object Model. It’s nothing more than the block level diagram
  of all the HTML elements loaded on the page when a browser loads a web page. It
  is presented as a tree of objects which are ...'
---

Par Ashish Nandan Singh

### Qu'est-ce que le DOM ?

DOM signifie Document Object Model. Ce n'est rien de plus que le diagramme de bloc de tous les éléments HTML chargés sur la page lorsqu'un navigateur charge une page web. Il est présenté sous forme d'arbre d'objets qui sont des éléments HTML. Regardez l'image ci-dessous et vous aurez peut-être une meilleure idée.

![Image](https://cdn-media-1.freecodecamp.org/images/1*QTOLCnPd_rg5Fum9l9PNSA.jpeg)
_Représentation DOM d'un simple fichier .html_

Un beau diagramme de bloc propre de votre fichier .html laid — n'est-ce pas génial ! Mais maintenant vous vous demandez, comment cela m'aide-t-il ? Quel est le cas d'utilisation ? Pourquoi dois-je connaître cela ?

Pour faire simple, le DOM vous permet d'apporter de la dynamique à votre site web statique. Avec l'utilisation du DOM, vous pouvez faire un tas de choses utiles sur la page web comme :

* ajouter et supprimer des éléments et attributs HTML
* ajouter et supprimer des règles CSS sur un événement déclenché par l'utilisateur
* créer de nouveaux événements pour des événements utilisateur synthétiques

Et c'est exactement ce que vous apprendrez tout au long de cet article.

Pour vous donner une idée de ce que nous allons réaliser à la fin de cet article, consultez [ce lien](https://colorgame-f0a09.firebaseapp.com/).

### **Mise en route**

Nous allons construire un simple jeu de devinette de couleurs. Chaque fois que le jeu est lancé, un code de couleur RGB aléatoire sera sélectionné. Selon le mode du jeu, nous aurons trois (facile) ou six (difficile) options ou blocs de couleurs à l'écran parmi lesquels choisir. Chaque fois qu'un bloc de couleur incorrect est sélectionné, le bloc disparaîtra jusqu'à ce que l'utilisateur sélectionne la bonne couleur (ou qu'il reste la dernière option).

Voici un diagramme approximatif de ce que nous allons construire :

C'est quelque chose que j'ai appris alors que je suivais un cours de [Colt Steele](https://www.linkedin.com/in/coltsteele), un formateur phénoménal lorsqu'il s'agit d'enseigner les concepts de base. Vous devriez tous regarder ses vidéos sur la chaîne YouTube d'Udemy.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ezY7AYaRb8oAbfmjyNeGaw.png)
_Diagramme de maquettage_

#### Partie 1

Nous commencerons par créer une simple structure de base pour le web, qui sera composée des fichiers index.html, app.css et app.js. Voyons à quoi ressemblent ces fichiers lorsque nous commençons.

Mais d'abord, veuillez noter : juste pour garder cela simple pour quiconque lit ceci sans aucune expérience de développement préalable, je continuerai à montrer le code source chaque fois que nous changerons quelque chose de majeur.

* **index.html**

```
<!DOCTYPE html><html>
```

```
<head><title>Jeu de Couleurs</title><link rel="stylesheet" type="text/css" href="app.css"></head>
```

```
<body>
```

```
<h1>The Great<br><span id="colorDisplay">RGB</span><br>Jeu de Couleurs</h1>
```

```
<div id="stripe">
```

```
<button id="reset">Nouvelles Couleurs</button><span id="message"></span><button class="mode">Facile</button><button class="mode selected">Difficile</button>
```

```
</div>
```

```
<div id="container">
```

```
<div class="square"></div><div class="square"></div><div class="square"></div><div class="square"></div><div class="square"></div><div class="square"></div>
```

```
</div>
```

```
<script type="text/javascript" src="app.js"></script></body></html>
```

C'est aussi simple que cela. Nous pouvons simplement diviser l'ensemble de la page web en trois blocs principaux.

Tout d'abord, nous avons la section d'en-tête, qui contient le texte et peut contenir d'autres informations si vous souhaitez les ajouter.

Ensuite, il y a le panneau de contrôle, qui contient des boutons pour réinitialiser le jeu et pour basculer entre les modes de jeu.

Troisièmement — et la partie la plus intéressante — est la zone de jeu principale, qui contient six divs. Ces divs servent d'options pour chaque code de couleur RGB aléatoire qui peut être sélectionné par une logique sophistiquée (que nous verrons dans un instant).

* **app.css**

```
body {
```

```
background-color: #232323;margin: 0;font-family: "Montserrat", "Avenir";}
```

```
h1 {
```

```
text-align: center;line-height: 1.1;font-weight: normal;color: white;background: steelblue;margin: 0;text-transform: uppercase;padding: 20px 0;}
```

```
#container {
```

```
margin: 20px auto;max-width: 600px;}
```

```
.square {
```

```
width: 30%;background: purple;padding-bottom: 30%;float: left;margin: 1.66%;border-radius: 15%;transition: background 0.6s;-webkit-transition: background 0.6s;-moz-transition: background 0.6s;}
```

Des styles de base ont été ajoutés pour le corps, le texte et les carrés qui servent d'options de jeu.

* **app.js**

```
var numSquares = 6;var colors = [];var pickedColor;var squares = document.querySelectorAll(".square");var resetButton = document.querySelector("#reset");var modeButtons = document.querySelectorAll(".mode");
```

Nous avons stocké tous les éléments HTML sous forme de variables. Cela nous aidera à effectuer certaines actions en ajoutant des événements à chacune de ces variables, et en les appelant à l'intérieur de diverses fonctions logiques que nous créerons au cours de cet article.

En fait, décomposons chacune de ces variables et voyons quelle est leur signification :

* La variable **numSquares** stocke le nombre de carrés qui seront disponibles dans le jeu selon le mode. Pour simplifier, j'ai codé en dur la valeur à six toujours — nous pouvons revenir à cela et ajouter une logique pour la faire changer.
* **colors** est un tableau vide qui contient les six ou trois codes de couleur RGB générés aléatoirement chaque fois que le jeu est réinitialisé ou que le mode est changé.
* **pickedColor** est le bloc de couleur/option sélectionné par l'utilisateur à chaque clic.
* **squares** est un tableau de tous les carrés sur la page qui sont disponibles comme options. Ce tableau peut avoir trois ou six éléments selon le mode du jeu.
* La variable **reset** est le bouton "nouveau jeu" dans le panneau de contrôle.
* **modeButtons** est à nouveau un tableau qui contient les boutons de mode facile et difficile.

Si vous avez suivi jusqu'à ce point, vous devriez avoir une version assez basique de ce jeu. Vous pouvez ouvrir le fichier index.html dans n'importe quel navigateur et le vérifier. Très bien, maintenant que nous avons posé les bases, passons aux choses sérieuses.

#### Partie 2

Dans cette section, nous travaillerons principalement avec le fichier JavaScript et quelques fois avec le fichier CSS.

**Génération de couleurs aléatoires**

Notre premier objectif sera de générer des couleurs aléatoires chaque fois que le jeu est démarré, redémarré ou que le mode est changé. Voyons comment nous pouvons faire cela.

Pour comprendre le principe sous-jacent de la génération de quelque chose de manière aléatoire, nous devrions commencer par un tableau codé en dur de six codes de couleur RGB. Essayons de définir ces couleurs comme les couleurs de fond des six carrés/options disponibles sur la page web.

```
var colors = [
```

```
    "rgb(255, 0, 0)",    "rgb(255, 0, 255)",    "rgb(255, 225, 0)",    "rgb(255, 0, 255)",    "rgb(0, 255, 255)",    "rgb(0, 255, 0)"
```

```
];
```

```
var squares = document.querySelectorAll(.squares);
```

```
for (i=0; i<squares.length; i++) {squares.style.backgroundColor = colors[i]}
```

* J'ai ajouté six codes de couleur RGB statiques au tableau de couleurs
* J'ai utilisé le tableau de carrés déjà créé pour exécuter une boucle sur tous les carrés présents dans le tableau.
* J'ai fait correspondre la couleur de fond de chaque carré à son index correspondant dans le tableau de couleurs.

Si vous ajoutez cela au fichier app.js et que vous actualisez le navigateur, vous verrez que chaque carré est maintenant d'une couleur unique.

![Image](https://cdn-media-1.freecodecamp.org/images/1*LSsJbHhndKH8n7PxPf8UzA.png)
*_capture d'écran du navigateur_

Vous avez peut-être remarqué que les boutons ne sont pas encore stylisés, mais laissez cela pour l'instant. Nous y viendrons plus tard.

#### Activer la fonctionnalité de clic

Tout ce dont nous avons besoin, ce sont des **écouteurs d'événements** activés sur chaque option/bloc de couleur à l'écoute des événements de clic. La manière la plus simple de faire cela est — encore une fois, vous avez deviné juste — en parcourant le tableau de carrés. Cette boucle ressemblerait à celle qui a été utilisée pour styliser le fond des blocs de couleur. Regardons le code :

```
for(i=0; i<= squares.length; i++) {  squares[i].addeventListeners('click', function() {    alert('une option a été cliquée');  });}
```

Maintenant, chaque fois que vous cliquez sur un bloc, vous recevrez ce message d'alerte du navigateur. C'était facile ! Maintenant, nos options sont réactives et répondent à l'entrée de l'utilisateur. Tout ce que nous devons faire maintenant est de définir la logique qui indique ce qui se passe si la couleur choisie par le jeu et celle choisie par l'utilisateur sont les mêmes.

À ce stade, vous avez peut-être déjà la solution si vous avez prêté attention aux parties ci-dessus. Alors, voyons comment nous pouvons faire cela.

#### **Vérifier si la couleur est correcte ou non**

Explorons les possibilités que nous avons avec nos options/blocs de couleur étant réactifs et répondant. Nous pouvons effectuer un petit test et voir si les deux couleurs correspondent ou non. Très bientôt, nous aurons des couleurs générées aléatoirement chaque fois que nous actualisons la page ou chaque fois que nous réinitialisons le jeu ou changeons le mode de jeu. Mais pour l'instant, nous allons nous entraîner avec l'ensemble des six codes de couleur RGB que nous avons assignés dans le fichier.

Regardons un peu de code, puis je le décomposerai pour vous.

```
for(i=0; i<= squares.length; i++) {  squares[i].addeventListeners('click', function() {    //si le bon bloc est cliqué, faire quelque chose....    //si le mauvais bloc est cliqué, faire quelque chose....  });}
```

Comme vous le savez peut-être déjà, nous utiliserons un simple bloc **if-else**.

```
pickedColor = colors[3];for (i=0; i <= squares.length; i++) { //appliquer la couleur de fond à tous les carrés... squares[i].style.backgroundColor = colors[i]   //activer l'événement de clic sur chaque carré.....     squares[i].addEventListener('click', function() {
```

```
       //si l'utilisateur a sélectionné la bonne couleur....         var clickedColor = this.style.backgroundColor;
```

```
        //vérifier si la couleur sélectionnée correspond à la couleur par défaut...
```

```
         if(pickedColor === clickedColor) {             changeColors(pickedColor);           }         //si l'utilisateur a sélectionné la mauvaise couleur....         else {           this.style.backgroundColor = "#232323";           messageDisplay.text = "Mauvais Choix !";         }    })};
```

Je sais — c'est beaucoup de code. Mais voyons ce que cela signifie vraiment :

* Nous commençons par définir quelle sera la couleur par défaut choisie par le jeu, avec la variable **pickedColour.**
* Ensuite, nous exécutons notre **boucle for** qui nous permet de parcourir le tableau des blocs de couleur/options.
* Ensuite, nous activons les **événements de clic** sur chaque bloc de couleur/option. Nous faisons cela en utilisant une **fonction de rappel.** Cette fonction ne fait rien d'autre que sélectionner la couleur de fond du bloc de couleur/option sélectionné simplement en l'assignant à la variable appelée **clickedColour.**
* Maintenant, nous avons les deux couleurs : celle qui a été sélectionnée par le jeu et celle par l'utilisateur. Il ne reste plus qu'à les faire correspondre et voir si le choix était correct ou non.
* Nous pouvons faire cela facilement en utilisant le bloc **if else**. Si le choix est correct, alors faites ceci, sinon faites autre chose.
* Si la bonne couleur est sélectionnée, nous ajoutons un texte sur la page pour confirmer le bon choix et ajoutons un effet visuel pour le confirmer à nouveau. Sinon, nous faisons correspondre la couleur de cette option de couleur/bloc particulière pour correspondre à la couleur de fond de la page. Cela produit un effet comme si le bloc de couleur/option venait de disparaître.
* Maintenant, vous avez vu que si la même couleur est sélectionnée, alors une fonction est exécutée. Voyons de quoi cette fonction est composée :

```
function changeColors(color) { for (i=0; i <= squares.length; i++) {  squares[i].style.backgroundColor = color;  messageDisplay.text = "Vous êtes bon pour deviner !"; }}
```

Cette fonction parcourt le tableau des blocs de couleur/options et réinitialise la couleur de fond pour qu'elle soit celle de la couleur sélectionnée ou de la couleur par défaut.

Dans le cas où les couleurs ne sont pas les mêmes, nous définissons simplement la couleur de fond de la sélection actuelle pour qu'elle soit celle de la page web.

```
else {  this.style.backgroundColor = "#232323";  messageDisplay.text = "Mauvais Choix !";}
```

Très bien, maintenant que nous avons le jeu principal configuré, nous devons simplement nous soucier des problèmes de conception minimaux et ajouter la fonctionnalité dans le panneau de contrôle.

Mais d'abord, voyons à quoi ressemble le dossier de code à ce stade si vous avez suivi toutes les étapes correctement :

**index.html**

**app.css**

**app.js**

#### Étape 3

Tout va bien. Mais maintenant, nous devons créer de nouveaux codes de couleur RGB générés aléatoirement dans notre jeu qui ne sont pas le même ensemble de couleurs qui seraient assignés dans les blocs de couleur/options.

Si cela vous fait penser aux fonctions, alors c'est le bon choix. Nous allons créer une nouvelle fonction avec des codes de couleur totalement aléatoires (nouveaux), et nous les assignerons au tableau des couleurs. Ensuite, nous les récupérerons dans le tableau des blocs de couleur/options.

Voyons à quoi ressemble le code, puis nous le passerons en revue ligne par ligne.

Une méthode intégrée en JavaScript nous aide à générer un nombre aléatoire entre 0 et 1. Ensuite, nous faisons quelques manipulations pour nous assurer que la plage de ce nombre aléatoire reste entre les chiffres 0 et 255.

* Tout d'abord, nous implémentons **Math.random**, en sélectionnant un nombre aléatoire entre 0 et 1, puis nous multiplions le nombre par 256 puisque nous ne voulons pas que le nombre soit plus grand que 255. Une fois que nous avons un nombre aléatoire, nous utilisons **Math.floor** et nous assurons que nous n'avons que le chiffre avant les valeurs décimales (un nombre entier).
* Nous assignons ces nombres aléatoires générés à des variables appelées r, g et b. Chacun signifie son propre nombre RGB respectif pour le code de couleur.
* Enfin, nous additionnons tous ces nombres ou variables pour former une chaîne. Nous retournons la chaîne pour qu'elle ressemble à ceci : **rgb(23, 45, 112).**
* Tout ce qu'il reste à faire est d'exécuter cette fonction en fonction du mode du jeu, et de générer trois ou six codes de couleur RGB aléatoires et de les assigner dans le tableau des couleurs.

Mais cela ne retournera qu'une chaîne qui ressemble à un code RGB. Comment cela sera-t-il ajouté au tableau des couleurs que nous avons ? Comment une couleur aléatoire sera-t-elle sélectionnée chaque fois que le jeu est démarré ou réinitialisé ?

Pour accomplir ces deux choses, nous créerons quelques fonctions supplémentaires et verrons comment elles nous aident à résoudre ce problème.

**Sélectionner une couleur aléatoire dans le tableau**

Pour ce faire, nous créerons une nouvelle fonction appelée **pickColor()**. Voyons à quoi ressemble la fonction, puis nous la décomposerons.

```
function pickColor() {  var random = Math.floor(Math.random() * colors.length);  return colors[random];}
```

Aussi simple que cela puisse être, voyons ce que ces deux lignes puissantes font pour nous.

* Comme nous l'avons déjà vu avec la magie de **Math.random** et **Math.floor**, nous utilisons la même fonction pour obtenir un nombre aléatoire généré entre 0 et la longueur du tableau.
* Ensuite, nous obtenons le code RGB correspondant dans le tableau des couleurs en utilisant le nombre aléatoire dans l'index.

**Ajouter six (ou trois) codes RGB aléatoires dans le tableau des couleurs**

Pour ce faire, nous utilisons les deux fonctions ci-dessus, qui sont **randomColors()** et **pickColors()**. Ce que la fonction randomColors() fait en particulier, c'est qu'elle exécute la fonction randomColors() six ou trois fois (selon le mode du jeu) et ajoute le nombre correspondant de codes de couleur RGB au tableau des couleurs. Nous nommerons cette fonction generateRandomColor(num*). Voyons à quoi ressemble le code et décomposons-le ligne par ligne.

*_num sera décidé sur la base du mode du jeu._

* Tout d'abord, nous ferons un simple tableau vide
* Ensuite, nous exécutons une boucle selon le mode du jeu
* Chaque fois que cette boucle est exécutée, un nouveau code RGB est poussé dans le tableau créé
* Enfin, nous retournons ce tableau

Maintenant, après toutes ces nouvelles fonctions et toutes ces manipulations de code, notre base de code pour **app.js** a pas mal changé. Voyons à quoi elle ressemble maintenant :

### Réinitialiser le jeu

Après avoir presque établi la logique principale, cela peut sembler une promenade de santé. Il s'agit simplement de créer une fonction et de laisser cette fonction faire son travail contre toute entrée utilisateur donnée (dans ce cas, un clic sur le bouton **réinitialiser**).

Tout ce que nous voulons avec le bouton de réinitialisation, c'est

* générer un ensemble de six couleurs aléatoires
* choisir une couleur aléatoire parmi le nouveau tableau de couleurs créé.

Voyons à quoi ressemblerait le pseudo-code :

```
function reset() {  //créer un nouveau tableau de 6 couleurs aléatoires  //choisir une nouvelle couleur aléatoire  //remplir les carrés avec un nouvel ensemble de couleurs générées}
```

Je recommande fortement d'écrire du pseudo-code lors de la résolution de problèmes complexes. Cette habitude d'écrire du pseudo-code m'a aidé à gagner beaucoup de temps chaque fois que je suis bloqué sur des défis algorithmiques complexes.

Très bien, revenons à notre bouton de réinitialisation : voyons à quoi ressemblerait la fonction réelle :

Décomposons-la ligne par ligne :

* Nous commençons par ajouter l'écouteur d'événements pour le bouton de réinitialisation. Nous déclenchons ensuite une fonction de rappel qui fait un tas de choses lorsque l'événement de clic est déclenché.
* Lorsqu'il est déclenché, nous commençons par générer un nouveau tableau de six couleurs aléatoires.
* Ensuite, nous choisissons une couleur aléatoire.
* Enfin, nous réinitialisons la couleur de fond pour tous les blocs de couleur.

Voici à quoi ressemble le fichier **app.js** mis à jour après toutes les modifications que nous avons apportées :

Cela semble assez bien pour l'instant ! Je n'ajoute pas la fonctionnalité pour configurer le mode dans cet article, car il devient déjà trop long et je ne veux pas vous ennuyer :). Mais si vous avez aimé tout cela, je serai plus que ravi d'écrire un autre article couvrant le reste.

Voici le [lien](https://github.com/ashishcodes4/DOM-manipulation) vers le dépôt GitHub où le code final optimisé peut être trouvé.

J'espère que cet article inspirera certains d'entre vous à en apprendre davantage sur la manipulation du DOM et ce beau langage qu'est JavaScript. À la prochaine fois !