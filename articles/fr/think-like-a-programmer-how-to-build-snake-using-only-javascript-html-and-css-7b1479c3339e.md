---
title: 'Pensez comme un programmeur : Comment construire Snake en utilisant uniquement
  JavaScript, HTML & CSS'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-05T21:28:34.000Z'
originalURL: https://freecodecamp.org/news/think-like-a-programmer-how-to-build-snake-using-only-javascript-html-and-css-7b1479c3339e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9xRelIyk3BRGfRoArVU6wA.png
tags:
- name: CSS
  slug: css
- name: Games
  slug: games
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: 'Pensez comme un programmeur : Comment construire Snake en utilisant uniquement
  JavaScript, HTML & CSS'
seo_desc: 'By Panayiotis Nicolaou

  Hello there ?

  Welcome on board. Today we will embark on an exciting adventure, where we will be
  making our very own snake game ?. You’ll learn how to work through a problem by
  breaking it down into smaller simpler steps. By the...'
---

Par Panayiotis Nicolaou

Bonjour ?

Bienvenue à bord. Aujourd'hui, nous allons nous lancer dans une aventure passionnante, où nous allons créer notre propre jeu de serpent ?. Vous apprendrez à résoudre un problème en le décomposant en étapes plus petites et plus simples. À la fin de ce voyage, vous aurez appris de nouvelles choses et vous vous sentirez en confiance pour explorer davantage par vous-même.

Si vous êtes nouveau en programmation, je vous recommande de consulter [freeCodeCamp](https://www.freecodecamp.org/). C'est un excellent endroit pour apprendre... vous l'avez deviné... gratuitement. C'est comme ça que j'ai commencé ?

D'accord, assez de blabla — êtes-vous prêt à commencer ?

> Vous pouvez trouver le code final [ici](https://github.com/supergoat/snake) et une démonstration en direct [ici](https://snake-cdxejlircg.now.sh).

### Installation

Commençons par créer un fichier « snake.html » qui contiendra tout notre code.

Puisque c'est un fichier HTML, la première chose dont nous avons besoin est la déclaration `[<!DOCTY](https://www.w3schools.com/tags/tag_doctype.asp)`PE>. Dans snake.html, tapez ce qui suit :

Super, maintenant ouvrez « snake.html » dans votre navigateur préféré. Vous devriez pouvoir voir **Bienvenue à Snake !**

![Image](https://cdn-media-1.freecodecamp.org/images/1*PFyqYaApjv8H6-ddH79HaQ.png)
_snake.html ouvert dans Chrome_

Nous avons bien commencé ?

### Création du canevas

Pour pouvoir créer notre jeu, nous devons utiliser le `[<canv](https://www.w3schools.com/html/html5_canvas.asp)`as> d'HTML. C'est ce qui est utilisé pour dessiner des graphiques en utilisant JavaScript.

Remplacez le message de bienvenue dans « snake.html » par ce qui suit :

```
<canvas id="gameCanvas" width="300" height="300"></canvas>
```

L'identifiant est ce qui identifie le canevas et doit toujours être spécifié. Nous l'utiliserons pour accéder au canevas plus tard. La largeur et la hauteur sont les dimensions du canevas et doivent également être spécifiées. Dans ce cas, 300 x 300 pixels.

Votre fichier snake.html devrait maintenant ressembler à ceci.

Si vous actualisez la page de votre navigateur où vous avez précédemment ouvert « snake.html », vous verrez maintenant une page blanche. C'est parce que, par défaut, le canevas est vide et n'a pas de fond. Corrigons cela. ?

#### Donner au canevas une couleur de fond et une bordure

Pour rendre notre canevas visible, nous pouvons lui donner une bordure en écrivant un peu de code JavaScript. Pour cela, nous devons insérer des balises `<script></script>` après le `</canvas>`, où tout notre code JavaScript ira.

> Si vous placez la balise `_<scri_`pt> avant le `<canv_`as>, votre code ne fonctionnera pas, car le HTML ne sera pas chargé.

Nous pouvons maintenant écrire un peu de code JavaScript, entre les balises `<script></script>`. Mettez à jour votre code comme ci-dessous.

Tout d'abord, nous obtenons l'élément canevas en utilisant l'identifiant (gameCanvas) que nous avons spécifié précédemment. Nous obtenons ensuite le contexte « 2d » du canevas, ce qui signifie que nous allons dessiner dans un espace 2D.

Enfin, nous dessinons un rectangle blanc de 300 x 300 avec une bordure noire. Cela couvre tout le canevas, en commençant par le coin supérieur gauche (0, 0).

Si vous rechargez « snake.html » dans votre navigateur, vous devriez voir une boîte blanche avec une bordure noire ! Bon travail, nous avons un canevas que nous pouvons utiliser pour créer notre jeu de serpent ! ? Passons au prochain défi !

### Représenter notre serpent

Pour que notre jeu de serpent fonctionne, nous devons connaître l'emplacement du serpent sur le canevas. Pour cela, nous pouvons représenter le serpent comme un tableau de coordonnées. Ainsi, pour créer un serpent horizontal au milieu du canevas (150, 150), nous pouvons écrire ce qui suit :

```
let snake = [  {x: 150, y: 150},  {x: 140, y: 150},  {x: 130, y: 150},  {x: 120, y: 150},  {x: 110, y: 150},];
```

Remarquez que la coordonnée y pour toutes les parties est toujours 150. La coordonnée x de chaque partie est de -10px (à gauche) de la partie précédente. La première paire de coordonnées dans le tableau `{x: 150, y: 150}` représente la tête à l'extrême droite du serpent.

Cela deviendra plus clair lorsque nous dessinerons le serpent dans la section suivante.

### Créer et dessiner notre serpent

Pour afficher le serpent sur le canevas, nous pouvons écrire une fonction pour dessiner un rectangle **pour chaque** paire de coordonnées.

```
function drawSnakePart(snakePart) {  ctx.fillStyle = 'lightgreen';  ctx.strokestyle = 'darkgreen';
```

```
  ctx.fillRect(snakePart.x, snakePart.y, 10, 10);  ctx.strokeRect(snakePart.x, snakePart.y, 10, 10);}
```

Ensuite, nous pouvons créer une autre fonction qui imprime les parties sur le canevas.

```
function drawSnake() {  snake.forEach(drawSnakePart);}
```

Notre fichier `snake.html` devrait maintenant ressembler à ceci :

Si vous actualisez votre page de navigateur maintenant, vous verrez un serpent vert au milieu du canevas. Super ! ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*BLf1mbFS-SCl4M8VQen1Qg.png)

### Permettre au serpent de se déplacer horizontalement

Ensuite, nous voulons donner au serpent la capacité de se déplacer. Mais comment faisons-nous cela ? ?

Eh bien, pour faire avancer le serpent d'un pas (10px) vers la droite, nous pouvons augmenter la coordonnée x de **chaque** partie du serpent de 10px (dx = +10px). Pour faire avancer le serpent vers la gauche, nous pouvons diminuer la coordonnée x de **chaque** partie du serpent de 10px (dx = -10).

> **dx** est la vitesse horizontale du serpent.

Créer un serpent qui a avancé de 10px vers la droite devrait alors ressembler à ceci

![Image](https://cdn-media-1.freecodecamp.org/images/1*zytaPha9jcM6N45xrOnyTw.png)

Créez une fonction appelée `advanceSnake` que nous utiliserons pour mettre à jour le serpent.

```
function advanceSnake() {  const head = {x: snake[0].x + dx, y: snake[0].y};
```

```
  snake.unshift(head);
```

```
  snake.pop();}
```

Tout d'abord, nous créons une nouvelle tête pour le serpent. Nous ajoutons ensuite la nouvelle tête au début de **snake** en utilisant [unshift](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/unshift) et nous supprimons le dernier élément de **snake** en utilisant [pop](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/pop). De cette façon, toutes les autres parties du serpent se déplacent comme montré ci-dessus.

Boom ?, vous commencez à comprendre.

### Permettre au serpent de se déplacer verticalement

Pour déplacer notre serpent vers le haut et vers le bas, nous ne pouvons pas modifier toutes les coordonnées y de 10px. Cela déplacerait tout le serpent vers le haut et vers le bas.

![Image](https://cdn-media-1.freecodecamp.org/images/1*39OySfjontvvtgrLQhyt3A.gif)

Au lieu de cela, nous pouvons modifier la coordonnée y de la tête. En la diminuant de 10px pour déplacer le serpent vers le bas, et en l'augmentant de 10px pour déplacer le serpent vers le haut. Cela fera bouger le serpent correctement.

Heureusement, grâce à la façon dont nous avons écrit la fonction `advanceSnake`, cela est très facile à faire. À l'intérieur de `advanceSnake`, mettez à jour la tête pour également augmenter la coordonnée y de la tête par **dy**.

```
const head = {x: snake[0].x + dx, y: snake[0].y + dy};
```

Pour tester comment notre fonction `advanceSnake` fonctionne, nous pouvons l'appeler temporairement avant la fonction `drawSnake`.

```
// Avancer d'un pas vers la droiteadvanceSnake()
```

```
// Changer la vitesse verticale à 0dx = 0;// Changer la vitesse horizontale à 10dy = -10;
```

```
// Avancer d'un pas vers le hautadvanceSnake();
```

```
// Dessiner le serpent sur le canevasdrawSnake();
```

Voici à quoi ressemble notre fichier `snake.html` jusqu'à présent.

En actualisant le navigateur, nous pouvons voir que notre serpent s'est déplacé. Succès !

![Image](https://cdn-media-1.freecodecamp.org/images/1*Qnmxp7sFC4TREwVFYqh2vg.png)

### Refactorisation de notre code

Avant de continuer, faisons un peu de refactorisation et déplaçons le code qui dessine le canevas à l'intérieur d'une fonction. Cela nous aidera dans la section suivante.

> **« La refactorisation de code** est le processus de restructuration du code informatique existant, sans changer son comportement externe. » -[wikipedia](https://en.wikipedia.org/wiki/Code_refactoring)

```
function clearCanvas() {  ctx.fillStyle = "white";  ctx.strokeStyle = "black";
```

```
  ctx.fillRect(0, 0, gameCanvas.width, gameCanvas.height);  ctx.strokeRect(0, 0, gameCanvas.width, gameCanvas.height);}
```

Nous faisons de grands progrès ! ?

### Faire bouger notre serpent automatiquement

D'accord, maintenant que nous avons refactorisé notre code avec succès, nous pouvons faire bouger notre serpent automatiquement.

Auparavant, pour tester que notre fonction `advanceSnake` fonctionnait, nous l'avons appelée deux fois. Une fois pour faire avancer le serpent vers la droite, et une fois pour faire avancer le serpent vers le haut.

Ainsi, si nous voulions faire avancer le serpent de cinq pas vers la droite, nous appellerions `advanceSnake()` cinq fois de suite.

```
clearCanvas();advanceSnake();advanceSnake();advanceSnake();advanceSnake();advanceSnake();drawSnake();
```

Mais, l'appeler cinq fois de suite comme montré ci-dessus, fera sauter le serpent de 50px vers l'avant.

![Image](https://cdn-media-1.freecodecamp.org/images/1*8MMmK5I75eaA_fxHFUiiwQ.gif)

Au lieu de cela, nous voulons faire avancer le serpent pas à pas.

Pour cela, nous pouvons ajouter un léger délai entre chaque appel, en utilisant [setTimeout](https://www.w3schools.com/Jsref/met_win_settimeout.asp). Nous devons également nous assurer d'appeler `drawSnake` chaque fois que nous appelons `advanceSnake`. Si nous ne le faisons pas, nous ne pourrons pas voir les étapes intermédiaires qui montrent le serpent en mouvement.

```
setTimeout(function onTick() {  clearCanvas();  advanceSnake();  drawSnake();}, 100);
```

```
setTimeout(function onTick() {  clearCanvas();  advanceSnake();  drawSnake();}, 100);
```

```
...
```

```
drawSnake();
```

Remarquez comment nous appelons également `_clearCanvas()_` à l'intérieur de chaque `_setTimeout_`. Cela permet de supprimer toutes les positions précédentes du serpent qui laisseraient une trace derrière.

![Image](https://cdn-media-1.freecodecamp.org/images/1*q59cpBnigigbLPslBUkiLw.png)

Bien qu'il y ait un problème avec le code ci-dessus. Il n'y a rien ici pour dire au programme qu'il doit attendre **setTimeout** avant de passer au **setTimeout** suivant. Cela signifie que le serpent **sautera** toujours de 50px vers l'avant mais après un **léger délai**.

Pour corriger cela, nous devons envelopper notre code à l'intérieur de fonctions, en appelant une fonction à la fois.

```
stepOne();    function stepOne() {  setTimeout(function onTick() {    clearCanvas();    advanceSnake();    drawSnake();   // Appeler la deuxième fonction   stepTwo();  }, 100)}
```

```
function stepTwo() {  setTimeout(function onTick() {    clearCanvas();    advanceSnake();    drawSnake();    // Appeler la troisième fonction    stepThree();  }, 100)}
```

```
...
```

Comment faire pour que notre serpent continue de bouger ? Au lieu de créer un nombre infini de fonctions qui s'appellent les unes les autres, nous pouvons créer une fonction `main` et l'appeler encore et encore.

```
function main() {  setTimeout(function onTick() {    clearCanvas();    advanceSnake();    drawSnake();
```

```
    // Appeler main à nouveau    main();  }, 100)}
```

Voilà ! Nous avons maintenant un serpent qui continuera à avancer vers la droite. Bien que, une fois qu'il atteint la fin du canevas, il continue son voyage infini dans l'inconnu ?. Nous corrigerons cela en temps voulu, patience jeune padawan. ?.

![Image](https://cdn-media-1.freecodecamp.org/images/1*qr0kvF_aQ2E_n6QcxfkyQA.gif)

### Changer la direction du serpent

Notre prochaine tâche est de changer la direction du serpent lorsqu'une des touches fléchées est pressée. Ajoutez le code suivant après la fonction `drawSnakePart`.

```
function changeDirection(event) {  const LEFT_KEY = 37;  const RIGHT_KEY = 39;  const UP_KEY = 38;  const DOWN_KEY = 40;
```

```
  const keyPressed = event.keyCode;  const goingUp = dy === -10;  const goingDown = dy === 10;  const goingRight = dx === 10;  const goingLeft = dx === -10;
```

```
  if (keyPressed === LEFT_KEY && !goingRight) {    dx = -10;    dy = 0;  }
```

```
  if (keyPressed === UP_KEY && !goingDown) {    dx = 0;    dy = -10;  }
```

```
  if (keyPressed === RIGHT_KEY && !goingLeft) {    dx = 10;    dy = 0;  }
```

```
  if (keyPressed === DOWN_KEY && !goingDown) {    dx = 0;    dy = 10;  }}
```

Il n'y a rien de compliqué ici. Nous vérifions si la touche pressée correspond à l'une des touches fléchées. Si c'est le cas, nous changeons la vitesse verticale et horizontale comme décrit précédemment.

Remarquez que nous vérifions également si le serpent se déplace dans la direction opposée à la nouvelle direction souhaitée. Cela est pour empêcher notre serpent de reculer, par exemple lorsque vous pressez la touche fléchée **droite** alors que le serpent se déplace vers la **gauche**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*PxB5A6SCbJlwye4PUj_Bdw.gif)
_Serpent qui recule_

Pour connecter `changeDirection` à notre jeu, nous pouvons utiliser [addEventListener](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener) sur le [document](https://www.w3schools.com/Jsref/dom_obj_document.asp) pour « écouter » lorsqu'une touche est pressée. Ensuite, nous pouvons appeler `changeDirection` avec l'événement [keydown](https://developer.mozilla.org/en-US/docs/Web/Events/keydown). Ajoutez le code suivant après la fonction `main`.

```
document.addEventListener("keydown", changeDirection)
```

Vous devriez maintenant pouvoir changer la direction du serpent en utilisant les quatre touches fléchées. Excellent travail, vous êtes en feu?!

Ensuite, voyons comment nous pouvons générer de la nourriture et faire grandir notre serpent.

### Générer de la nourriture pour le serpent

Pour la nourriture de notre serpent, nous devons générer un ensemble aléatoire de coordonnées. Nous pouvons utiliser une fonction auxiliaire `randomTen` pour produire deux nombres. Un pour la coordonnée x et un pour la coordonnée y.

Nous devons également nous assurer que la nourriture n'est pas située là où se trouve actuellement le serpent. Si c'est le cas, nous devons générer un nouvel emplacement pour la nourriture.

```
function randomTen(min, max) {  return Math.round((Math.random() * (max-min) + min) / 10) * 10;}
```

```
function createFood() {  foodX = randomTen(0, gameCanvas.width - 10);  foodY = randomTen(0, gameCanvas.height - 10);
```

```
  snake.forEach(function isFoodOnSnake(part) {    const foodIsOnSnake = part.x == foodX && part.y == foodY    if (foodIsOnSnake)      createFood();  });}
```

Nous devons ensuite créer une fonction pour dessiner la nourriture sur le canevas.

```
function drawFood() { ctx.fillStyle = 'red'; ctx.strokestyle = 'darkred'; ctx.fillRect(foodX, foodY, 10, 10); ctx.strokeRect(foodX, foodY, 10, 10);}
```

Enfin, nous pouvons appeler `createFood` avant d'appeler `main`. N'oubliez pas de mettre à jour également `main` pour utiliser la fonction `drawFood`.

```
function main() {  setTimeout(function onTick() {    clearCanvas();    drawFood()    advanceSnake();    drawSnake();
```

```
    main();  }, 100)}
```

### Faire grandir le serpent

Faire grandir notre serpent est simple. Nous pouvons mettre à jour notre fonction `advanceSnake` pour vérifier si la tête du serpent touche la nourriture. Si c'est le cas, nous pouvons sauter la suppression de la dernière partie du serpent et créer un nouvel emplacement pour la nourriture.

```
function advanceSnake() {  const head = {x: snake[0].x + dx, y: snake[0].y};
```

```
  snake.unshift(head);
```

```
  const didEatFood = snake[0].x === foodX && snake[0].y === foodY;  if (didEatFood) {    createFood();  } else {    snake.pop();  }}
```

#### Suivre le score

Pour rendre le jeu plus agréable pour le joueur, nous pouvons également ajouter un score qui augmente lorsque le serpent mange de la nourriture.

Créez une nouvelle variable score et définissez-la sur 0 après la déclaration du serpent.

```
let score = 0;
```

Ajoutez ensuite une nouvelle div avec un id « score » avant le canevas. Nous pouvons utiliser cela pour afficher le score.

```
<div id="score">0</div><canvas id="gameCanvas" width="300" height="300"></canvas>
```

Enfin, mettez à jour `advanceSnake` pour augmenter et afficher le score lorsque le serpent mange la nourriture.

```
function advanceSnake() {  ...
```

```
  if (didEatFood) {    score += 10;    document.getElementById('score').innerHTML = score;
```

```
    createFood();  } else {    ...  }}
```

Ouf, c'était beaucoup, mais nous avons parcouru un long chemin ?

### Fin du jeu

Il reste une dernière pièce, et c'est de mettre fin au jeu ?. Pour cela, nous pouvons créer une fonction `didGameEnd` qui retourne **vrai** lorsque le jeu est terminé ou **faux** sinon.

```
function didGameEnd() {  for (let i = 4; i < snake.length; i++) {    const didCollide = snake[i].x === snake[0].x &&      snake[i].y === snake[0].y
```

```
    if (didCollide) return true  }
```

```
  const hitLeftWall = snake[0].x < 0;  const hitRightWall = snake[0].x > gameCanvas.width - 10;  const hitToptWall = snake[0].y < 0;  const hitBottomWall = snake[0].y > gameCanvas.height - 10;
```

```
  return hitLeftWall ||          hitRightWall ||          hitToptWall ||         hitBottomWall}
```

Tout d'abord, nous vérifions si la tête du serpent touche une autre partie du serpent et retournons **vrai** si c'est le cas.

> Remarquez que nous commençons notre boucle à l'index 4. Il y a deux raisons à cela. La première est que **didCollide** évaluerait immédiatement à vrai si l'index était 0, donc le jeu se terminerait. La seconde est qu'il est impossible pour les trois premières parties de se toucher entre elles.

Ensuite, nous vérifions si le serpent a heurté l'un des murs du canevas et retournons **vrai** si c'est le cas, sinon nous retournons **faux**.

Maintenant, nous pouvons retourner tôt dans notre fonction `main` si `didEndGame` retourne vrai, mettant ainsi fin au jeu.

```
function main() {  if (didGameEnd()) return;
```

```
  ...}
```

Notre snake.html devrait maintenant ressembler à ceci :

Vous avez maintenant un jeu de serpent fonctionnel que vous pouvez jouer et partager avec vos amis. Mais avant de célébrer, regardons un dernier problème. Ce sera le dernier, je vous le promets.

### Bugs sournois ?

Si vous jouez au jeu suffisamment de fois, vous pourriez remarquer que parfois le jeu se termine de manière inattendue. C'est un très bon exemple de la façon dont les bugs peuvent s'infiltrer dans nos programmes et causer des problèmes ?.

Lorsque qu'un bug se produit, la meilleure façon de le résoudre est d'abord d'avoir un moyen fiable de le reproduire. C'est-à-dire, trouver les étapes précises qui mènent au comportement inattendu. Ensuite, vous devez comprendre pourquoi elles causent le comportement inattendu et ensuite trouver une solution.

#### Reproduire le bug

Dans notre cas, les étapes pour reproduire le bug sont les suivantes :

* Le serpent se déplace vers la gauche
* Le joueur appuie sur la touche fléchée vers le bas
* Le joueur appuie immédiatement sur la touche fléchée vers la droite (avant que 100ms ne se soient écoulées)
* Le jeu se termine

![Image](https://cdn-media-1.freecodecamp.org/images/1*rMOAsWJxt8uD2p3dILRHnw.gif)

#### Comprendre le bug

Décomposons ce qui se passe étape par étape.

**Le serpent se déplace vers la gauche**

* La vitesse horizontale, dx est égale à -10
* La fonction `main` est appelée
* `advanceSnake` est appelée, ce qui fait avancer le serpent de -10px vers la gauche.

**Le joueur appuie sur la touche fléchée vers le bas**

* `changeDirection` est appelée
* `keyPressed === DOWN_KEY && dy !goingUp` évalue à vrai
* dx change à 0
* dy change à +10

**Le joueur appuie immédiatement sur la touche fléchée vers la droite (avant que 100ms ne se soient écoulées)**

* `changeDirection` est appelée
* `keyPressed === RIGHT_KEY && !goingLeft` évalue à vrai
* dx change à +10
* dy change à 0

**Le jeu se termine**

* La fonction `main` est appelée **après que 100ms se soient écoulées.**
* `advanceSnake` est appelée, ce qui fait avancer le serpent de 10px vers la droite.
* `const didCollide = snake[i].x === snake[0].x && snake[i].y === snake[0].y` évalue à vrai
* `didGameEnd` retourne vrai
* La fonction `main` retourne tôt
* Le jeu se termine

#### Corriger le bug

Après avoir étudié ce qui s'est passé, nous apprenons que le jeu s'est terminé parce que le serpent a reculé.

C'est parce que lorsque le joueur a appuyé sur la touche fléchée vers le bas, dx a été défini à 0. Ainsi, `keyPressed === RIGHT_KEY && !goingLeft` a évalué à vrai, et dx a changé à 10.

Il est important de noter que le changement de direction s'est produit **avant** que 100ms ne se soient écoulées. Si 100ms s'étaient écoulées, alors le serpent aurait d'abord fait un pas vers le bas et n'aurait pas reculé.

Pour corriger notre bug, nous devons nous assurer que nous ne pouvons changer de direction qu'après que `main` et `advanceSnake` aient été appelés. Nous pouvons créer une variable **changingDirection**. Celle-ci sera définie à vrai lorsque `changeDirection` est appelée, et à faux lorsque `advanceSnake` est appelée.

À l'intérieur de notre fonction `changeDirection`, nous pouvons retourner tôt si **changingDirection** est vrai.

```
function changeDirection(event) {  const LEFT_KEY = 37;  const RIGHT_KEY = 39;  const UP_KEY = 38;  const DOWN_KEY = 40;
```

```
  if (changingDirection) return;
```

```
  changingDirection = true;
```

```
  ...}
```

```
function main() {  setTimeout(function onTick() {    changingDirection = false;        ...
```

```
  }, 100)}
```

Voici notre version finale de snake.html

> Remarquez que j'ai également ajouté quelques styles ? entre les balises &`_lt;style><_`;/style>. C'est pour faire apparaître le canevas et le score au milieu de l'écran.

### Conclusion

Félicitations !! ??

Nous avons atteint la fin de notre voyage. J'espère que vous avez apprécié apprendre avec moi et que vous vous sentez maintenant en confiance pour continuer vers votre prochaine aventure.

Mais cela ne doit pas s'arrêter ici. Mon prochain article se concentrera sur vous aider à commencer avec le monde **très** passionnant de l'**open source**.

L'[open source](https://en.wikipedia.org/wiki/Open-source_software) est un excellent moyen d'apprendre **beaucoup** de nouvelles choses et de rencontrer des personnes incroyables. C'est très gratifiant mais peut être effrayant au début ?.

Pour recevoir une notification lorsque mon prochain article sera publié, vous pouvez me suivre ! ?

C'était un plaisir d'être sur ce voyage avec vous.

À la prochaine. ✨