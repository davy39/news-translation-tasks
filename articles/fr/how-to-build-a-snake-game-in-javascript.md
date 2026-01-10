---
title: Comment créer un jeu de serpent en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-12-11T16:13:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-snake-game-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/joan-gamell-ZS67i1HLllo-unsplash.jpg
tags:
- name: beginners guide
  slug: beginners-guide
- name: CSS
  slug: css
- name: Game Development
  slug: game-development
- name: Games
  slug: games
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
seo_title: Comment créer un jeu de serpent en JavaScript
seo_desc: "By Fakorede Damilola\nIn this article I am going to show you how to build\
  \ a snake game with JavaScript. \nA snake game is a simple game where a snake moves\
  \ around a box trying to eat an apple. Once it successfully eats the apple, the\
  \ length of the snak..."
---

Par Fakorede Damilola

Dans cet article, je vais vous montrer comment créer un jeu de serpent avec JavaScript. 

Un jeu de serpent est un jeu simple où un serpent se déplace dans une boîte en essayant de manger une pomme. Une fois qu'il a réussi à manger la pomme, la longueur du serpent augmente et le mouvement devient plus rapide. 

Ensuite, le jeu est terminé lorsque le serpent se heurte à lui-même ou à l'un des quatre murs de la boîte.

Très bien, commençons par le HTML et le CSS (le squelette de notre jeu). 

### HTML

```html
<h1>Nokia 3310 snake</h1>
<div class="scoreDisplay"></div>
<div class="grid"></div>
<div class="button">
  <button class="top">haut</button>
  <button class="bottom">bas</button>
  <button class="left">gauche</button>
  <button class="right">droite</button>
</div>
<div class="popup">
  <button class="playAgain">rejouer</button>
</div>

```

Le HTML ci-dessus est assez basique. 

* Nous avons une div de classe `scoreDisplay` qui affichera nos scores.
* Il y a une div de classe `grid` qui abritera le jeu (ce sera une grille de 10 par 10)
* La classe `button` contient essentiellement un bouton pour les utilisateurs jouant au jeu sur un téléphone (nous l'automatiserons avec le clavier pour les utilisateurs de bureau). 
* Et la classe `popup` contiendra notre bouton de relecture. 

Maintenant, ajoutons un peu de style avec CSS.

### CSS

```css
body {
  background: rgb(212, 211, 211);
}

.grid {
  width: 200px;
  height: 200px;
  border: 1px solid red;
  margin: 0 auto;
  display: flex;
  flex-wrap: wrap;
}

.grid div {
  width: 20px;
  height: 20px;
  /*border:1px black solid;
box-sizing:border-box*/
}

.snake {
  background: blue;
}

.apple {
  background: yellow;
  border-radius: 20px;
}

.popup {
  background: rgb(32, 31, 31);
  width: 100px;
  height: 100px;
  position: fixed;
  top: 100px;
  left: 100px;
  display: flex;
  justify-content: center;
  align-items: center;
}

```

Dans le CSS, le `grid` qui est le plateau de jeu a une dimension définie et un affichage de `flex`. Cela permet aux contenus (div) de cette grille de s'aligner horizontalement comme s'ils étaient des éléments en ligne au lieu de l'affichage en bloc normal qu'ils possèdent. 

La propriété `flex wrap` déplace simplement les divs à la ligne suivante, les empêchant de dépasser la dimension définie de leur élément parent (grid). 

Nous allons créer dynamiquement le contenu du plateau de jeu à partir de JS, mais nous pouvons donner une largeur et une hauteur ici (avec la div `.grid`). J'ai inclus les commentaires ici pour vous aider à voir les divs, donc au fil du temps, nous allons les décommenter. 

Les classes `snake` et `Apple` sont là pour nous montrer où se trouvent le serpent et le bonus dans le jeu, tandis que la classe `popup` est une div fixe qui abrite la div `replay`.

À ce stade, vous devriez avoir quelque chose comme ceci:

![Image](https://www.freecodecamp.org/news/content/images/2020/12/Screenshot--1710-.png)
_Structure avec HTML et CSS_

Maintenant, nous sommes prêts pour le JavaScript.

## JavaScript

La première chose que nous devons faire est de définir nos variables:

```js
let grid = document.querySelector(".grid");
let popup = document.querySelector(".popup");
let playAgain = document.querySelector(".playAgain");
let scoreDisplay = document.querySelector(".scoreDisplay");
let left = document.querySelector(".left");
let bottom = document.querySelector(".bottom");
let right = document.querySelector(".right");
let up = document.querySelector(".top");
let width = 10;
let currentIndex = 0;
let appleIndex = 0;
let currentSnake = [2, 1, 0];
let direction = 1;
let score = 0;
let speed = 0.8;
let intervalTime = 0;
let interval = 0;

```

La variable width est exactement ce qu'elle est (la largeur de la grille, c'est-à-dire 10). Les autres variables auront plus de sens au fur et à mesure que nous avancerons, mais croyez-le ou non, notre serpent est en fait un tableau appelé `currentSnake`.

Maintenant, commençons avec les fonctions:

```js
document.addEventListener("DOMContentLoaded", function () {
  document.addEventListener("keyup", control);
  createBoard();
  startGame();
  playAgain.addEventListener("click", replay);
});

```

Il y a un `eventListener` sur l'objet document appelé `DomContentLoaded` et cet événement est déclenché immédiatement une fois que le contenu HTML est chargé sur notre écran. 

Une fois que cela se produit, nous définissons un eventListener sur le document pour surveiller les clics sur le clavier (plus d'informations à ce sujet plus tard). Après cela, nous voulons créer le `gameBoard`, démarrer le jeu et surveiller les clics sur notre bouton de relecture.

### La fonction createBoard

```js
function createBoard() {
  popup.style.display = "none";
  for (let i = 0; i < 100; i++) {
    let div = document.createElement("div");
    grid.appendChild(div);
  }
}

```

Comme je l'ai dit plus tôt, il s'agit d'une grille de 10 par 10, ce qui signifie que nous allons avoir besoin de 100 divs. Donc, à partir de ce qui précède, nous fermons la div popup et nous bouclons jusqu'à 100 chaque fois que nous créons une nouvelle div et l'ajoutons à la grille (gameboard). 

Cela ajoutera immédiatement une partie du style que nous avons créé précédemment (la div .grid). Vous pouvez décommenter les styles CSS et vous verrez les divs créées (commentez-les à nouveau).

### La fonction startGame

```js
function startGame() {
  let squares = document.querySelectorAll(".grid div");
  randomApple(squares);
  //random apple
  direction = 1;
  scoreDisplay.innerHTML = score;
  intervalTime = 1000;
  currentSnake = [2, 1, 0];
  currentIndex = 0;
  currentSnake.forEach((index) => squares[index].classList.add("snake"));
  interval = setInterval(moveOutcome, intervalTime);
}

```

La fonction `startGame` commence par obtenir toutes les divs (puisque nous créons les divs à l'exécution, nous ne pouvons pas les obtenir en haut du code). 

Ensuite, nous sélectionnons un emplacement pour notre pomme. Nous le ferons ci-dessous dans la fonction **`randomApple`**. La `direction` fait référence à la direction dans laquelle le serpent se dirige - 1 pour la droite, -1 pour la gauche, et ainsi de suite. 

`intervalTime` définit le temps qu'il faut au serpent pour se déplacer, tandis que `currentSnake` définit exactement où sur la grille le serpent sera (notez que le serpent est essentiellement quelques divs données une couleur particulière). 

Pour afficher notre serpent à l'écran, nous allons boucler sur `currentSnake` avec `forEach`. Avec chaque valeur que nous obtenons, nous l'utiliserons avec **squares**. Rappelez-vous que nous avons accédé aux divs de la grille avec `querySelectorAll`, et nous pouvons ensuite y accéder comme à un tableau, c'est-à-dire en utilisant des nombres. Dans notre cas, ce sont les valeurs de `currentSnake`. 

Après cela, nous ajoutons simplement un appel `setInterval` (avec la fonction move `Outcome` et un temps de `intervalTime`, que nous avons défini ci-dessus) à la variable `interval`. Cela permet de pouvoir facilement appeler `clearInterval` sur cette variable. 

La fonction `moveOutcome` s'exécute toutes les 1000 ms (1 s) et définit essentiellement ce qui se passe lorsque vous déplacez le serpent.

### La fonction moveOutcome

```js
function moveOutcome() {
  let squares = document.querySelectorAll(".grid div");
  if (checkForHits(squares)) {
    alert("vous avez heurté quelque chose");
    popup.style.display = "flex";
    return clearInterval(interval);
  } else {
    moveSnake(squares);
  }
}

```

Comme la fonction `startGame` ci-dessus, nous obtenons d'abord toutes les divs de la `grid`, puis nous vérifions si la fonction **`checkForHits`** retourne vrai. 

Si c'est le cas, cela signifie que nous avons heurté quelque chose et affiche ensuite le bouton de relecture et efface l'intervalle. Si elle retourne faux, cela signifie que nous n'avons rien heurté et nous déplaçons le serpent avec la fonction **`moveSnake`**. 

Donc, essentiellement, toutes les 1 seconde, le jeu se termine si `checkForHits` est vrai ou nous déplaçons le serpent d'un pas en avant si `checkForHits` est faux. Je vais d'abord parler de la fonction `moveSnake`.

### La fonction moveSnake 

```js
function moveSnake(squares) {
  let tail = currentSnake.pop();
  squares[tail].classList.remove("snake");
  currentSnake.unshift(currentSnake[0] + direction);
  // movement ends here
  eatApple(squares, tail);
  squares[currentSnake[0]].classList.add("snake");
}

```

La fonction `moveSnake` reçoit un argument appelé `squares` afin que nous n'ayons pas à obtenir le **.grid div** à nouveau dans cette fonction.  

La première chose que nous devons faire est de supprimer le dernier élément du tableau **`currentSnake`** via pop (c'est la queue et le premier élément est toujours la tête). Essentiellement, le serpent avance d'un pas, laissant la position précédente où il se trouvait. Après cela, nous ajoutons simplement une nouvelle valeur au début du tableau avec `unShift`. 

Supposons que notre serpent vient de commencer à bouger et est tourné vers la droite (c'est-à-dire, direction = 1). Cette direction sera ajoutée à la tête de `currentSnake` et la somme sera poussée comme la nouvelle `snakeHead`. 

Par exemple, si le serpent était en position **[2,1,0]**, nous supprimons le dernier élément, le laissant en position [2,1]. Ensuite, nous prenons la tête qui est **2** et ajoutons la direction qui est **1** et faisons de cette valeur la nouvelle valeur **[3,2,1]** qui déplace notre serpent d'un pas vers la droite après une seconde.  

Si nous voulons déplacer le serpent vers le bas, la direction sera définie sur la largeur (qui est 10) et ajoutée au premier élément (c'est-à-dire 12 et poussée) **[12,2,1]**. 

Après cela, nous vérifions simplement si le serpent a mangé une pomme et affichons la nouvelle tête de serpent sur le DOM.

### La fonction checkForHits

```js
function checkForHits(squares) {
  if (
    (currentSnake[0] + width >= width * width && direction === width) ||
    (currentSnake[0] % width === width - 1 && direction === 1) ||
    (currentSnake[0] % width === 0 && direction === -1) ||
    (currentSnake[0] - width <= 0 && direction === -width) ||
    squares[currentSnake[0] + direction].classList.contains("snake")
  ) {
    return true;
  } else {
    return false;
  }
}

```

La fonction `checkForHits` a une instruction if. Selon la condition définie, elle peut retourner vrai (ce qui signifie que nous avons heurté quelque chose) ou faux. 

La première condition est si `currentSnake` [0] (la tête du serpent) + width (10) est égal à la surface totale de la largeur (c'est-à-dire, width*width = 100) et la direction est égale à la largeur. 

Donc, en gros, supposons que la tête du serpent est à la position 97 qui est la dernière couche de notre grille. Si vous deviez ajouter 10 à 97 (= 107), cela est supérieur à la grille entière qui est 100. Si la direction du serpent est toujours dirigée vers le bas, alors le serpent a heurté la bordure inférieure. 

Si le serpent était à 97, 97+10 =107, mais le joueur a pu changer la direction à, disons, 1 (comme, ils ont pressé la touche gauche), alors il n'aurait rien heurté.

Ou (**||**) si le reste lorsque la tête du serpent est divisée par la largeur = **width-1** (par exemple, 9) et la direction est **1**. Chaque dernière div du côté droit a une valeur de **9, 19, 29** et ainsi de suite. Donc, en gros, il restera toujours 9 lorsque vous divisez par 10. 

Si la tête de notre serpent est à la position 39 et que la direction est toujours 1 (c'est-à-dire que le serpent se déplace toujours vers le mur), alors il a heurté quelque chose (le mur de droite). 

Toutes les autres conditions sont exactement l'inverse des deux ci-dessus. La condition finale permet que si la tête du serpent se dirige vers un endroit qui contient déjà une classe serpent, cela signifie simplement que le serpent se mord lui-même.

Donc...si l'une des conditions ci-dessus est vraie, le serpent a heurté quelque chose et **true** sera retourné (sinon false). Et si c'est le cas, le jeu est terminé. Mais si c'est faux, déplacez le serpent d'un pas en avant avec `moveSnake`. 

### La fonction eatApple

```js
function eatApple(squares, tail) {
  if (squares[currentSnake[0]].classList.contains("apple")) {
    squares[currentSnake[0]].classList.remove("apple");
    squares[tail].classList.add("snake");
    currentSnake.push(tail);
    randomApple(squares);
    score++;
    scoreDisplay.textContent = score;
    clearInterval(interval);
    intervalTime = intervalTime * speed;
    interval = setInterval(moveOutcome, intervalTime);
  }
}

```

La fonction `eatApple` est appelée à partir de la fonction `moveSnake` chaque fois que le serpent avance d'un pas. 

Elle reçoit deux arguments, squares, **.grid div** et **tail** (essentiellement la valeur qui a été retirée du serpent dans `moveOutcome`). Elle vérifie ensuite si la position suivante où notre serpent se déplace contient une pomme. 

Si c'est le cas, elle ajoute simplement cette queue que nous avons retirée au tableau. Cela est dû au fait que chaque fois que notre serpent mange une pomme, nous voulons augmenter la longueur du serpent d'une valeur - et quelle meilleure façon que d'ajouter la queue qui a été retirée lorsqu'il s'est déplacé ?

Ensuite, nous sélectionnons simplement une nouvelle position pour notre pomme avec `randomApple` (voir ci-dessous). Après cela, nous ajoutons une valeur de **un** à notre score et l'affichons à l'utilisateur, effaçons le `timeInterval` (afin que nous puissions augmenter la vitesse du serpent, c'est-à-dire le temps que chaque mouvement prend) et ensuite nous réinitialisons simplement l'intervalle.

### La fonction randomApple

```js
function randomApple(squares) {
  do {
    appleIndex = Math.floor(Math.random() * squares.length);
  } while (squares[appleIndex].classList.contains("snake"));
  squares[appleIndex].classList.add("apple");
}

```

`randomApple` choisit simplement un endroit pour placer notre pomme en utilisant une boucle **do while**. D'abord, elle choisit une position aléatoire avec `Math.random()` dans la boucle do et vérifie si l'endroit qu'elle a choisi contient déjà une classe serpent. 

Cela signifie que la condition dans l'instruction do continuera à s'exécuter jusqu'à ce qu'elle trouve un endroit qui ne contient pas de serpent (continuez à faire cela tant que c'est vrai). Une fois qu'elle trouve un endroit, elle donne simplement à cet endroit une classe de pomme.

### Configurer les contrôles

Maintenant, nous devons configurer nos contrôles. Nous commencerons par les utilisateurs de clavier.

```js
function control(e) {
  if (e.keycode === 39) {
    direction = 1; // droite
  } else if (e.keycode === 38) {
    direction = -width; //si nous pressons la flèche vers le haut, le serpent montera de dix divs
  } else if (e.keycode === 37) {
    direction = -1; // gauche, le serpent ira à gauche d'une div
  } else if (e.keycode === 40) {
    direction = +width; // bas, la tête du serpent apparaîtra instantanément 10 divs en dessous de la div actuelle
  }
}

```

Rappelez-vous que nous avons défini un `eventListener` pour `**keyup**`. Cette fonction se déclenche immédiatement après que votre main appuie et quitte une touche sur un clavier. 

Maintenant, chaque bouton du clavier a une valeur appelée keycode (nombres) à laquelle nous avons accès et qui nous indique quel numéro a été cliqué. Essentiellement, nous allons surveiller les touches fléchées avec leurs keycodes respectifs. Avec cela, nous apportons des modifications à la direction, par exemple **-1, 10** et ainsi de suite. 

Très bien, j'espère que vous comprenez maintenant comment nous sommes capables de déplacer le serpent. 

Ensuite, cet ensemble de boutons est pour les appareils mobiles et nous faisons essentiellement la même chose :

```js
up.addEventListener("click", () => (direction = -width));
bottom.addEventListener("click", () => (direction = +width));
left.addEventListener("click", () => (direction = -1));
right.addEventListener("click", () => (direction = 1));

```

La dernière chose que nous devons faire est de créer la div **`replay`** qui apparaîtra lorsque le serpent heurtera quelque chose. Le bouton nous aide à réinitialiser le jeu.

### La fonction replay

```js
function replay() {
  grid.innerHTML = "";
  createBoard();
  startGame();
  popup.style.display = "none";
}

```

À partir de ce qui précède, nous effaçons essentiellement la grille (plateau de jeu) et exécutons les fonctions précédentes.

Félicitations - vous avez atteint la fin ! Voici le résultat final :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/Screenshot--1709-.png)
_Jeu final_

J'espère que vous avez pu coder en suivant et que vous avez apprécié. 

Dans ce tutoriel, nous avons appris comment créer notre propre jeu de serpent avec JavaScript. Certains autres concepts importants que nous avons couverts incluent **push, pop, setInterval, clearInterval** et **eventListener**. 

Vous pouvez consulter le jeu final ici : [https://codepen.io/Fako29/pen/dyppXZG](https://codepen.io/Fako29/pen/dyppXZG). 

Merci d'avoir lu. Suivez-moi sur Twitter ici : [https://twitter.com/fakoredeDami](https://twitter.com/fakoredeDami)