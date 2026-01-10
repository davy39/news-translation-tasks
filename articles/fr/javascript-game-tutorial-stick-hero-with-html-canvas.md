---
title: 'Tutoriel JavaScript : Créer un clone de Stick Hero avec HTML Canvas + JavaScript'
subtitle: ''
author: Hunor Márton Borbély
co_authors: []
series: null
date: '2023-11-16T19:00:55.000Z'
originalURL: https://freecodecamp.org/news/javascript-game-tutorial-stick-hero-with-html-canvas
coverImage: https://www.freecodecamp.org/news/content/images/2023/11/_Users_hunormartonborbely_Documents_Courses_Youtube_Sticky-20Hero_index.html-High-Res-.png
tags:
- name: Game Development
  slug: game-development
- name: JavaScript
  slug: javascript
seo_title: 'Tutoriel JavaScript : Créer un clone de Stick Hero avec HTML Canvas +
  JavaScript'
seo_desc: 'In this tutorial, you''ll learn how to create a game that''s inspired by
  Stick Hero – using plain JavaScript and HTML canvas.

  We are going to recreate Stick Hero, a mobile game published by KetchApp. We''ll
  go through how the game works in general, how ...'
---

Dans ce tutoriel, vous apprendrez à créer un jeu inspiré de Stick Hero en utilisant JavaScript et HTML canvas.

Nous allons recréer [Stick Hero](https://apps.apple.com/us/app/stick-hero/id918338898), un jeu mobile publié par KetchApp. Nous verrons comment le jeu fonctionne en général, comment utiliser JavaScript pour dessiner sur un élément `<canvas>`, comment ajouter une logique de jeu et animer le jeu, et comment fonctionne la gestion des événements. 

À la fin de ce guide, vous aurez construit le jeu entier en utilisant JavaScript.

Tout au long du tutoriel, nous utiliserons JavaScript pour manipuler l'état du jeu et l'élément HTML canvas pour rendre la scène du jeu. Pour tirer le meilleur parti de ce tutoriel, vous devriez avoir une compréhension de base de JavaScript. Mais même si vous êtes débutant, vous pouvez suivre et apprendre en cours de route.

Commençons et construisons notre propre jeu Stick Hero en utilisant JavaScript et HTML canvas !

Si vous préférez le format vidéo, vous pouvez également [regarder ce tutoriel sur YouTube](https://youtu.be/eue3UdFvwPo?si=U0QItUV2sRkqVCer).

## Table des matières

1. [Le jeu Stick Hero](#heading-le-jeu-stick-hero)
2. [Phases du jeu](#heading-phases-du-jeu)
3. [Les principales parties du jeu](#heading-les-principales-parties-du-jeu)
4. [Comment initialiser le jeu](#heading-comment-initialiser-le-jeu)
5. [La fonction de dessin](#heading-la-fonction-de-dessin)
6. [Gestion des événements](#heading-gestion-des-evenements)
7. [La boucle d'animation principale](#heading-la-boucle-danimation-principale)
8. [Résumé](#heading-resume)

# Le jeu Stick Hero

Dans ce jeu, vous contrôlez un héros qui marche de plateforme en plateforme en étirant un bâton qui sert de pont. Si le bâton est de la bonne taille, alors le héros peut traverser en toute sécurité vers la plateforme suivante. Mais si le bâton est trop court ou trop long, alors le héros tombera.

Vous pouvez trouver une version jouable du jeu que nous allons créer sur [CodePen](https://codepen.io/HunorMarton/pen/xxOMQKg) où vous pouvez également voir le code source final. Essayez-le avant que nous entrions dans les détails. 

Vous pouvez également consulter le jeu original sur [iOS](https://apps.apple.com/us/app/stick-hero/id918338898) et [Android](https://play.google.com/store/apps/details?id=com.ketchapp.stickhero&hl=en&gl=US).

%[https://codepen.io/HunorMarton/pen/xxOMQKg]

# Phases du jeu

Le jeu comporte cinq phases différentes qui se répètent jusqu'à ce que le héros tombe.

1. Initialement, le jeu est en attente d'une entrée utilisateur, et rien ne se passe.
2. Ensuite, une fois que le joueur maintient le bouton de la souris enfoncé, le jeu étire un bâton vers le haut jusqu'à ce que la souris soit relâchée.
3. Ensuite, une fois que la souris est relâchée, le bâton commence à tourner et tombe, espérons-le sur la plateforme suivante.
4. Si c'est le cas, alors le héros marche le long du bâton jusqu'à la plateforme suivante.
5. Enfin, une fois que le héros atteint la plateforme suivante, toute la scène se déplace vers la gauche pour centrer le héros et la plateforme suivante devant. Ensuite, toute la boucle recommence depuis le début. Le jeu attend une entrée utilisateur, et une fois que le joueur maintient le bouton de la souris enfoncé, un nouveau bâton est dessiné.

Dans un scénario moins favorable, les mêmes phases se suivent, mais dans la phase de marche, si l'autre extrémité du bâton ne tombe pas sur la plateforme suivante, alors le héros ne marchera que jusqu'au bord du bâton, puis tombera.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Stick-Hero.gif)
_Les phases du jeu_

# Les principales parties du jeu

Comment réalisons-nous cela en code ? Ce jeu a essentiellement trois parties. L'état du jeu, la fonction `draw`, et la fonction `animate`.

Nous avons un état de jeu qui est une collection de variables définissant chaque partie du jeu. Il inclut la phase actuelle, la position du héros, les coordonnées des plateformes, la taille et la rotation des bâtons, et ainsi de suite.

```javascript
let phase = "waiting"; // waiting | stretching | turning | walking | transitioning | falling
let lastTimestamp; // Le timestamp du cycle d'animation précédent

let heroX; // Change lors du déplacement vers l'avant
let heroY; // Ne change que lors de la chute
let sceneOffset; // Déplace tout le jeu

let platforms = [];
let sticks = [];

let score = 0;

...

```

Ensuite, nous aurons deux fonctions principales : une qui peint la scène sur l'écran en fonction de cet état (ce sera la fonction `draw`), et une qui changera cet état progressivement pour qu'il ressemble à une animation (ce sera la fonction `animate`). Enfin, nous aurons également une gestion des événements qui déclenchera la boucle d'animation.

# Comment initialiser le jeu

Pour commencer, initialisons le projet avec un simple fichier HTML, CSS et JavaScript. Nous établirons le plan du code puis initialiserons l'état du jeu.

## Le HTML

La partie HTML de ce jeu est très simple. La majeure partie du jeu se trouvera à l'intérieur de l'élément `<canvas>`. Nous allons utiliser JavaScript pour dessiner sur ce canvas. Nous avons également un élément div qui affichera le score et un bouton de redémarrage.

Dans l'en-tête, nous chargeons également nos fichiers CSS et JavaScript. Notez le tag `defer` lors du chargement du script. Cela exécutera le script uniquement après que le reste du HTML soit chargé, afin que nous puissions accéder aux parties du HTML (comme l'élément canvas) directement dans notre script.

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Stick Hero</title>
    <link rel="stylesheet" href="index.css" />
    <script src="index.js" defer></script>
  </head>

  <body>
    <div class="container">
      <canvas id="game" width="375" height="375"></canvas>
      <div id="score"></div>
      <button id="restart">RECOMMENCER</button>
    </div>
  </body>
</html>

```

## Le CSS

Le CSS ne contiendra pas non plus trop de choses. Nous peignons le jeu sur l'élément canvas et le contenu de l'élément canvas ne peut pas être stylisé avec CSS. Ici, nous stylisons uniquement la position de notre canvas, de notre élément de score et du bouton de réinitialisation. 

Notez que le bouton de réinitialisation est invisible par défaut. Nous allons le rendre visible en utilisant JavaScript une fois que le jeu est terminé.

```css
html,
body {
  height: 100%;
}

body,
.container {
  display: flex;
  justify-content: center;
  align-items: center;
}

.container {
  position: relative;
  font-family: Helvetica;
}

canvas {
  border: 1px solid;
}

#score {
  position: absolute;
  top: 30px;
  right: 30px;
  font-size: 2em;
  font-weight: 900;
}

#restart {
  position: absolute;
  display: none;
}

```

## Le plan de notre fichier JavaScript

Et enfin, la partie JavaScript est là où toute la magie se trouve. Pour simplifier, j'ai tout mis dans un seul fichier, mais n'hésitez pas à le diviser en plusieurs fichiers.

Nous allons introduire quelques variables supplémentaires et quelques fonctions supplémentaires, mais voici le plan de ce fichier. Les éléments suivants sont inclus :

* Nous définissons diverses variables qui constituent ensemble l'`état du jeu`. Plus de détails sur leurs valeurs dans la section sur l'initialisation de l'état.
* Nous allons définir quelques variables comme `configuration`, comme la taille des plateformes et la vitesse à laquelle le héros doit se déplacer. Nous les couvrons dans la section de dessin et dans la boucle principale.
* Une référence à l'élément `<canvas>` en HTML, et obtenir le contexte de dessin de celui-ci. Cela sera utilisé par la fonction `draw`.
* Une référence à l'élément `score` et au bouton `restart` en HTML. Nous mettrons à jour le score chaque fois que le héros traverse une nouvelle plateforme. Et nous affichons le bouton de réinitialisation une fois que le jeu est terminé.
* Nous initialisons l'état du jeu et peignons la scène en appelant la fonction `resetGame`. C'est le seul appel de fonction de niveau supérieur.
* Nous définissons la fonction `draw` qui dessinera la scène sur l'élément canvas en fonction de l'état.
* Nous configurons les gestionnaires d'événements pour les événements `mousedown` et `mouseup`.
* Nous définissons la fonction `animate` qui manipulera l'état.
* Et nous aurons quelques fonctions utilitaires que nous discuterons plus tard.

```javascript
// État du jeu
let phase = "waiting"; // waiting | stretching | turning | walking | transitioning | falling
let lastTimestamp; // Le timestamp du cycle d'animation précédent

let heroX; // Change lors du déplacement vers l'avant
let heroY; // Ne change que lors de la chute
let sceneOffset; // Déplace tout le jeu

let platforms = [];
let sticks = [];

let score = 0;

// Configuration
...

// Obtention de l'élément canvas
const canvas = document.getElementById("game");

// Obtention du contexte de dessin
const ctx = canvas.getContext("2d");

// Autres éléments UI
const scoreElement = document.getElementById("score");
const restartButton = document.getElementById("restart");

// Démarrer le jeu
resetGame();

// Réinitialise l'état du jeu et la disposition
function resetGame() {
  ...

  draw();
}

function draw() {
  ...
}

window.addEventListener("mousedown", function (event) {
  ...
});

window.addEventListener("mouseup", function (event) {
  ...
});

function animate(timestamp) {
  ...
}

...

```

## Comment initialiser l'état

Pour démarrer le jeu, nous appelons la même fonction que nous utilisons pour le réinitialiser – la fonction `resetGame`. Elle initialise/réinitialise l'état du jeu et appelle la fonction de dessin pour peindre la scène.

L'état du jeu inclut les variables suivantes :

* `phase` : La phase actuelle du jeu. Sa valeur initiale est waiting.
* `lastTimestamp` : Utilisé par la fonction `animate` pour déterminer combien de temps s'est écoulé depuis le dernier cycle d'animation. Nous l'aborderons plus en détail plus tard.
* `platforms` : Un tableau contenant les métadonnées de chaque plateforme. Chaque plateforme est représentée par un objet avec des propriétés `x` et `w` représentant leur position X et leur largeur. La première plateforme est toujours la même – comme défini ici – pour s'assurer qu'elle a une taille et une position raisonnables. Les plateformes suivantes sont générées par une fonction utilitaire. Au fur et à mesure que le jeu progresse, de plus en plus de plateformes sont générées à la volée.
* `heroX` : La position X du héros. Par défaut, le héros se tient près du bord de la première plateforme. Cette valeur changera pendant la phase de marche.
* `heroY` : La position Y du héros. Par défaut, elle est à zéro. Elle ne change que si le héros tombe.
* `sceneOffset` : Au fur et à mesure que le héros avance, nous devons décaler tout l'écran vers l'arrière pour garder le héros centré sur l'écran. Sinon, le héros sortira de l'écran. Dans cette variable, nous gardons une trace de la quantité dont nous devons décaler tout l'écran vers l'arrière. Nous mettrons à jour cette valeur pendant la phase de transition. Par défaut, sa valeur est 0.
* `sticks` : Métadonnées des bâtons. Bien que le héros ne puisse étirer qu'un seul bâton à la fois, nous devons également stocker les bâtons précédents afin de pouvoir les rendre. Par conséquent, la variable `sticks` est également un tableau.   
  
Chaque bâton est représenté par un objet avec les propriétés `x`, `length`, et `rotation`. La propriété `x` représente la position de départ du bâton qui correspond toujours au coin supérieur droit de la plateforme correspondante. Sa propriété `length` augmentera dans la phase d'étirement, et sa propriété `rotation` passera de 0 à 90 dans la phase de rotation. Ou de 90 à 180 dans la phase de chute.   
  
Initialement, le tableau `sticks` contient un bâton 'invisible' avec une longueur de 0. Chaque fois que le héros atteint une nouvelle plateforme, un nouveau bâton est ajouté au tableau.
* `score` : Le score du jeu. Il montre combien de plateformes le héros a atteintes. Par défaut, il est à 0.

```javascript
function resetGame() {
  // Réinitialiser l'état du jeu
  phase = "waiting";
  lastTimestamp = undefined;

  // La première plateforme est toujours la même
  platforms = [{ x: 50, w: 50 }];
  generatePlatform();
  generatePlatform();
  generatePlatform();
  generatePlatform();

  // Initialiser la position du héros
  heroX = platforms[0].x + platforms[0].w - 30; // Le héros se tient un peu avant le bord
  heroY = 0;

  // De combien devons-nous décaler l'écran vers l'arrière
  sceneOffset = 0;

  // Il y a toujours un bâton, même s'il semble invisible (longueur : 0)
  sticks = [{ x: platforms[0].x + platforms[0].w, length: 0, rotation: 0 }];

  // Score
  score = 0;

  // Réinitialiser l'UI
  restartButton.style.display = "none"; // Masquer le bouton de réinitialisation
  scoreElement.innerText = score; // Réinitialiser l'affichage du score

  draw();
}

```

À la fin de cette fonction, nous réinitialisons également l'UI en nous assurant que le bouton de réinitialisation est masqué et que le score est affiché à 0.

Une fois que nous avons initialisé l'état du jeu et réinitialisé l'UI, la fonction `resetGame` appelle la fonction `draw` pour peindre l'écran pour la première fois.

La fonction `resetGame` appelle une fonction utilitaire qui génère une plateforme aléatoire. Dans cette fonction, nous définissons quelle est la distance minimale entre deux plateformes (`minimumGap`) et quelle est la distance maximale (`maximumGap`). Nous définissons également quelle est la largeur minimale d'une plateforme et quelle est la largeur maximale. 

Sur la base de ces plages et des plateformes existantes, nous générons les métadonnées d'une nouvelle plateforme.

```javascript
function generatePlatform() {
  const minimumGap = 40;
  const maximumGap = 200;
  const minimumWidth = 20;
  const maximumWidth = 100;

  // Coordonnée X du bord droit de la plateforme la plus éloignée
  const lastPlatform = platforms[platforms.length - 1];
  let furthestX = lastPlatform.x + lastPlatform.w;

  const x =
    furthestX +
    minimumGap +
    Math.floor(Math.random() * (maximumGap - minimumGap));
  const w =
    minimumWidth + Math.floor(Math.random() * (maximumWidth - minimumWidth));

  platforms.push({ x, w });
}

```

# La fonction de dessin

La fonction `draw` peint toute la toile en fonction de l'état. Elle décale toute l'UI par l'offset, place le héros en position, et peint les plateformes et les bâtons. 

Comparé à la démonstration fonctionnelle liée au début de l'article, ici nous ne passerons qu'une version simplifiée de la fonction de dessin. Nous ne couvrirons pas la peinture d'un arrière-plan, et nous simplifierons l'apparence du héros.

Nous utiliserons cette fonction à la fois pour peindre la scène initiale et tout au long de notre boucle d'animation principale. 

Pour la peinture initiale, certaines des fonctionnalités que nous couvrons ici ne seront pas nécessaires. Par exemple, nous n'avons pas encore de bâtons sur la scène. Nous les couvrirons tout de même, car ainsi nous n'aurons pas à réécrire cette fonction une fois que nous commencerons à animer l'état. 

Tout ce que nous dessinons dans cette fonction est basé sur l'état, et peu importe si l'état est dans un état initial, ou si nous sommes plus avancés dans le jeu.

Nous avons défini un élément `<canvas>` en HTML. Mais comment peinons-nous des choses dessus ? En JavaScript, nous obtenons d'abord l'élément canvas puis obtenons son contexte quelque part au début de notre fichier. Ensuite, nous pouvons utiliser ce contexte pour exécuter des commandes de dessin.

Nous définissons également quelques variables à l'avance comme configuration. Nous faisons cela parce que nous devons utiliser ces valeurs à différentes parties de notre jeu et nous voulons maintenir la cohérence.

* `canvasWidth` et `canvasHeight` représentent la taille de l'élément canvas en HTML. Ils doivent correspondre à ce que nous avons défini en HTML. Nous utilisons ces valeurs à divers endroits.
* `platformHeight` représente la hauteur des plateformes. Nous utilisons ces valeurs lors du dessin des plateformes elles-mêmes, mais aussi lors du positionnement du héros et des bâtons.

La fonction de dessin repeint tout l'écran à partir de zéro à chaque fois. Tout d'abord, assurons-nous qu'il est vide. Appeler la fonction `clearRect` sur le contexte de dessin avec les arguments corrects garantit que nous effaçons tout de celui-ci.

```javascript
...

<div class="container">
  <canvas id="game" width="375" height="375"></canvas>
  <div id="score"></div>
  <button id="restart">RECOMMENCER</button>
</div>

...

```

```javascript
...

// Obtention de l'élément canvas
const canvas = document.getElementById("game");

// Obtention du contexte de dessin
const ctx = canvas.getContext("2d");

...

// Configuration
const canvasWidth = 375;
const canvasHeight = 375;
const platformHeight = 100;

...

function draw() {
  ctx.clearRect(0, 0, canvasWidth, canvasHeight);

  ...
}

...

```

## Comment cadrer la scène

Nous voulons également nous assurer que la scène a le bon cadrage. Lorsque nous utilisons canvas, nous avons un système de coordonnées avec le centre dans le coin supérieur gauche de l'écran qui grandit vers la droite et vers le bas. En HTML, nous définissons les attributs de largeur et de hauteur à 375 pixels.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Stick-Hero.001.jpeg)
_Par défaut, le centre du système de coordonnées est dans le coin supérieur gauche_

Initialement, la coordonnée 0, 0 est dans le coin supérieur gauche de l'écran, mais au fur et à mesure que le héros avance, toute la scène doit se décaler vers la gauche. Sinon, nous sortirions de l'écran.

Au fur et à mesure que le jeu progresse, nous mettons à jour la valeur `sceneOffset` pour suivre ce décalage dans la boucle principale. Nous pouvons utiliser cette variable pour translater toute la disposition. Nous appelons la commande `translate` pour décaler la scène sur l'axe des X.

```javascript
function draw() {
  ctx.clearRect(0, 0, canvasWidth, canvasHeight);

  // Sauvegarder la transformation actuelle
  ctx.save();

  // Décaler la vue
  ctx.translate(-sceneOffset, 0);

  // Dessiner la scène
  drawPlatforms();
  drawHero();
  drawSticks();

  // Restaurer la transformation au dernier sauvegarde
  ctx.restore();
}

```

Il est important que nous fassions cela avant de peindre quoi que ce soit sur le canvas, car la commande `translate` ne déplace pas réellement quoi que ce soit sur le canvas. Tout ce que nous avons peint avant sur le canvas restera tel quel. 

Au lieu de cela, la commande `translate` décale le système de coordonnées. La coordonnée 0, 0 ne sera plus dans le coin supérieur gauche, mais elle sera hors de l'écran sur la gauche. Tout ce que nous peindrons ensuite sera peint selon ce nouveau système de coordonnées.

C'est exactement ce que nous voulons. Au fur et à mesure que nous progressons dans le jeu, le héros augmentera sa coordonnée X. En déplaçant le système de coordonnées vers l'arrière, nous nous assurons qu'il sera peint dans l'écran.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Stick-Hero.002.jpeg)
_Une fois que nous utilisons la commande `translate`, le centre du système de coordonnées se décalera vers la gauche_

Les commandes `translate` s'accumulent. Cela signifie que si nous appelons la commande `translate` deux fois, la seconde ne remplace pas simplement la première, mais ajoutera un décalage par-dessus la première commande. 

Nous allons appeler la fonction `draw` dans une boucle, il est donc important que nous réinitialisions cette transformation à chaque fois que nous dessinons. De plus, nous commençons toujours avec la coordonnée 0, 0 dans le coin supérieur gauche. Sinon, le système de coordonnées se décalera vers la gauche à l'infini.

Nous pouvons restaurer les transformations en appelant la commande `restore` une fois que nous ne voulons plus être dans ce système de coordonnées décalé. La commande `restore` réinitialise les transitions et de nombreux autres paramètres à l'état dans lequel se trouvait le canvas à la dernière commande `save`. C'est pourquoi nous commençons souvent un bloc de peinture en sauvegardant le contexte et le terminons en le restaurant.

## Comment dessiner les plateformes

C'était juste le cadrage, mais nous n'avons encore rien peint. Commençons par un simple, dessiner des plateformes. Les métadonnées des plateformes sont stockées dans le tableau `platforms`. Il contient la position de départ de la plateforme et sa largeur.

Nous pouvons itérer sur ce tableau et remplir un rectangle en définissant la position de départ, et la largeur et la hauteur de la plateforme. Nous faisons cela en appelant la fonction `fillRect` avec les coordonnées X, Y et la largeur et la hauteur du rectangle à remplir. Notez que la coordonnée Y est à l'envers - elle grandit de haut en bas.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Stick-Hero.003.jpeg)
_Dessin de la plateforme_

```javascript
// Exemple d'état des plateformes
let platforms = [
  { x: 50, w: 50 },
  { x: 90, w: 30 },
];

...

function drawPlatforms() {
  platforms.forEach(({ x, w }) => {
    // Dessiner la plateforme
    ctx.fillStyle = "black";
    ctx.fillRect(x, canvasHeight - platformHeight, w, platformHeight);
  });
}

```

Ce qui est intéressant avec le canvas, ou du moins ce qui m'a surpris, c'est que une fois que vous avez peint quelque chose sur le canvas, vous ne pouvez pas le modifier. Ce n'est pas comme si vous peigniez un rectangle, puis vous pouvez changer sa couleur. Une fois que quelque chose est sur le canvas, il reste tel quel. 

Comme avec une vraie toile, une fois que vous avez peint quelque chose, vous pouvez soit le couvrir, en peignant quelque chose par-dessus, soit essayer d'effacer le canvas. Mais vous ne pouvez pas vraiment changer les parties existantes. C'est pourquoi nous définissons la couleur ici à l'avance et non après (avec la propriété `fillStyle`).

## Comment dessiner le héros

Nous ne couvrirons pas la partie héros en détail dans ce tutoriel, mais vous pouvez trouver le code source de la démonstration ci-dessus sur [CodePen](https://codepen.io/HunorMarton/pen/xxOMQKg). Dessiner des formes plus avancées est un peu plus compliqué avec l'élément canvas, et je couvrirai le dessin plus en détail dans un futur tutoriel.

Pour l'instant, utilisons simplement un rectangle rouge comme espace réservé pour le héros. Encore une fois, nous utilisons la fonction `fillRect` et passons une coordonnée X, Y et la largeur et la hauteur du héros. 

Les positions X et Y seront basées sur l'état heroX et heroY. La position X du héros est relative au système de coordonnées, mais sa position Y est relative au haut de la plateforme (elle a une valeur de 0 une fois sur le haut d'une plateforme). Nous devons ajuster la position Y pour qu'elle soit sur le haut de la plateforme.

```javascript
function drawHero() {
  const heroWidth = 20;
  const heroHeight = 30;

  ctx.fillStyle = "red";
  ctx.fillRect(
    heroX,
    heroY + canvasHeight - platformHeight - heroHeight,
    heroWidth,
    heroHeight
  );
}

```

## Comment dessiner les bâtons

Ensuite, voyons comment peindre les bâtons. Les bâtons sont un peu plus délicats car ils peuvent être tournés. 

Les bâtons sont stockés dans un tableau de manière similaire aux plateformes mais ont des attributs différents. Ils ont tous une position de départ, une longueur et une rotation. Les deux derniers changent dans la boucle principale du jeu, et le premier - la position - doit correspondre au coin supérieur droit d'une plateforme.

Sur la base de la longueur et de la rotation, nous pourrions utiliser un peu de trigonométrie et calculer la position de fin du bâton. Mais c'est beaucoup plus intéressant si nous transformons à nouveau le système de coordonnées.

Nous pouvons utiliser à nouveau la commande `translate`, pour définir le centre du système de coordonnées au bord de la plateforme. Ensuite, nous pouvons utiliser la commande `rotate` pour faire tourner le système de coordonnées autour de ce nouveau centre.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Stick-Hero.004.jpeg)
_Après avoir utilisé les commandes `translate` et `rotate`, le système de coordonnées sera tordu autour d'un nouveau centre_

```javascript
// Exemple d'état des bâtons
let sticks = [
  { x: 100, length: 50, rotation: 60 }
];

...

function drawSticks() {
  sticks.forEach((stick) => {
    ctx.save();

    // Déplacer le point d'ancrage au début du bâton et faire tourner
    ctx.translate(stick.x, canvasHeight - platformHeight);
    ctx.rotate((Math.PI / 180) * stick.rotation);

    // Dessiner le bâton
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(0, 0);
    ctx.lineTo(0, -stick.length);
    ctx.stroke();

    // Restaurer les transformations
    ctx.restore();
  });
}

```

Après les commandes `translate` et `rotate`, le point de départ du bâton sera à la coordonnée 0, 0 et le système de coordonnées sera tourné. 

Dans cet exemple, nous dessinons une ligne vers le haut - son début et sa fin ont la même coordonnée X. Seule la coordonnée Y change. Pourtant, la ligne se dirige vers la droite car tout le système de coordonnées a tourné. Maintenant, vers le haut est dans une direction diagonale. C'est un peu déroutant, mais on peut s'y habituer.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Stick-Hero.005.jpeg)
_Tandis que nous dessinons une ligne le long de l'axe Y, la ligne apparaîtra diagonale à cause du système de coordonnées transformé_

Le dessin réel de la ligne est également intéressant. Il n'y a pas de commande simple de dessin de ligne, donc nous devons dessiner un chemin. 

Nous obtenons un chemin en connectant plusieurs points. Nous pouvons les connecter avec des arcs, des courbes et des lignes droites. Dans ce cas, nous avons un chemin très simple. Nous commençons simplement un chemin (`beginPath`), nous déplaçons vers une coordonnée (`moveTo`), puis nous dessinons une ligne droite vers la coordonnée suivante (`lineTo`). Ensuite, nous le terminons avec la commande `stroke`. 

Nous pouvons également terminer le chemin avec la commande fill, mais cela n'a de sens qu'avec des formes.

Notez que parce que nous décalons et tournons le système de coordonnées ici à nouveau, à la fin de cette fonction, nous devons restaurer les transformations (et sauvegarder la matrice de transformation au début de cette fonction). Sinon, toutes les commandes de dessin à venir seraient tordues comme ceci.

# Gestion des événements

Maintenant que nous avons dessiné la scène, lançons le jeu en gérant les interactions utilisateur. La gestion des événements est la partie la plus facile du jeu. Nous écoutons les événements `mousedown` et `mouseup`, et nous gérons l'événement `click` du bouton de redémarrage.

Une fois que l'utilisateur maintient le bouton de la souris enfoncé, nous initiions la phase d'étirement en définissant la variable `phase` sur `stretching`. Nous réinitialisons le timestamp que la boucle d'événements principale va utiliser (nous y reviendrons plus tard), et nous déclenchons la boucle d'événements principale en demandant une frame d'animation pour la fonction `animate`. 

Tout cela ne se produit que si l'état actuel du jeu est en attente. Dans tout autre cas, nous ignorons l'événement `mousedown`.

```javascript
let phase = "waiting";
let lastTimestamp;

...

const restartButton = document.getElementById("restart");

...

window.addEventListener("mousedown", function () {
  if (phase == "waiting") {
    phase = "stretching";
    lastTimestamp = undefined;
    window.requestAnimationFrame(animate);
  }
});

window.addEventListener("mouseup", function () {
  if (phase == "stretching") {
    phase = "turning";
  }
});

restartButton.addEventListener("click", function (event) {
  resetGame();
  restartButton.style.display = "none";
});

...

```

La gestion de l'événement `mouseup` est encore plus simple. Si nous étirons actuellement un bâton, alors nous arrêtons cela et passons à la phase suivante où le bâton tombe.

Enfin, nous ajoutons également un gestionnaire d'événements pour le bouton de redémarrage. Le bouton de réinitialisation est masqué par défaut et ne sera visible qu'une fois que le héros sera tombé. Mais nous pouvons déjà définir son comportement, et une fois qu'il apparaîtra, il fonctionnera. Si nous cliquons sur réinitialiser, nous appelons la fonction `resetGame` pour réinitialiser le jeu et masquer le bouton.

C'est toute la gestion des événements que nous avons. Le reste dépend maintenant de la boucle d'animation principale que nous venons d'invoquer avec un `requestAnimationFrame`.

# La boucle d'animation principale

La boucle principale est la partie la plus compliquée du jeu. Il s'agit d'une fonction qui continuera à modifier l'état du jeu et à appeler la fonction `draw` pour repeindre tout l'écran en fonction de cet état. 

Comme elle sera appelée 60 fois par seconde, le repeint constant de l'écran donnera l'impression d'une animation continue. Parce que cette fonction s'exécute si fréquemment, nous ne modifions l'état du jeu que peu à peu à chaque fois.

Cette fonction `animate` est déclenchée par un appel `requestAnimationFrame` par l'événement `mousedown` (voir ci-dessus). Avec sa dernière ligne, elle continue à s'invoquer elle-même jusqu'à ce que nous l'arrêtions en retournant de la fonction. 

Il n'y a que deux cas où nous arrêterions la boucle : lorsque nous passons à la phase `waiting` et qu'il n'y a rien à animer, ou lorsque le héros tombe et que le jeu est terminé.

Cette fonction suit le temps écoulé depuis son dernier appel. Nous allons utiliser cette information pour calculer précisément comment l'état doit changer. Par exemple, lorsque le héros marche, nous devons calculer exactement combien de pixels il se déplace en fonction de sa vitesse et du temps écoulé depuis le dernier cycle d'animation.

```javascript
let lastTimestamp;

...

function animate(timestamp) {
  if (!lastTimestamp) {
    // Premier cycle
    lastTimestamp = timestamp;
    window.requestAnimationFrame(animate);
    return;
  }

  let timePassed = timestamp - lastTimestamp;

  switch (phase) {
    case "waiting":
      return; // Arrêter la boucle
    case "stretching": {
      sticks[sticks.length - 1].length += timePassed / stretchingSpeed;
      break;
    }
    case "turning": {
      sticks[sticks.length - 1].rotation += timePassed / turningSpeed;
      ...
      break;
    }
    case "walking": {
      heroX += timePassed / walkingSpeed;
      ...
      break;
    }
    case "transitioning": {
      sceneOffset += timePassed / transitioningSpeed;
      ...
      break;
    }
    case "falling": {
      heroY += timePassed / fallingSpeed;
      ...
      break;
    }
  }
  
  draw();
  lastTimestamp = timestamp;

  window.requestAnimationFrame(animate);
}
```

## Comment calculer le temps écoulé entre deux rendus

Les fonctions invoquées avec la fonction `requestAnimationFrame` reçoivent le `timestamp` actuel comme attribut. À la fin de chaque cycle, nous sauvegardons cette valeur `timestamp` dans l'attribut `lastTimestamp`, afin que dans le cycle suivant, nous puissions calculer combien de temps s'est écoulé entre deux cycles. Dans le code ci-dessus, il s'agit de la variable `timePassed`.

Le premier cycle est une exception car à ce moment-là, nous n'avions pas encore de cycle précédent. Initialement, la valeur de `lastTimestamp` est `undefined`. Dans ce cas, nous sautons un rendu et nous ne rendons la scène que lors du deuxième cycle, où nous avons déjà toutes les valeurs dont nous avons besoin. C'est la partie au tout début de la fonction `animate`.

## Comment animer une partie de l'état

Dans chaque phase, nous animons une partie différente de l'état. La seule exception est la phase d'attente car alors nous n'avons rien à animer. Dans ce cas, nous retournons de la fonction. Cela brisera la boucle, et l'animation s'arrêtera.

Dans la phase d'étirement - lorsque le joueur maintient le bouton de la souris enfoncé - nous devons faire grandir le bâton au fur et à mesure que le temps passe. Nous calculons combien il doit être plus long en fonction du temps écoulé et d'une valeur de vitesse qui définit combien de temps il faut pour que le bâton grandisse d'un pixel.

Une chose très similaire se produit dans toutes les autres phases également. Dans la phase de rotation, nous changeons la rotation du bâton en fonction du temps écoulé. Dans la phase de marche, nous changeons la position horizontale du héros en fonction du temps. Dans la phase de transition, nous changeons la valeur de décalage de toute la scène. Dans la phase de chute, nous changeons la position verticale du héros.

Chacune de ces phases a sa propre configuration de vitesse. Ces valeurs indiquent combien de millisecondes il faut pour faire grandir le bâton d'un pixel, faire tourner le bâton d'un degré, marcher d'un pixel, et ainsi de suite.

```javascript
// Configuration
const stretchingSpeed = 4; // Millisecondes nécessaires pour dessiner un pixel
const turningSpeed = 4; // Millisecondes nécessaires pour tourner un degré
const walkingSpeed = 4;
const transitioningSpeed = 2;
const fallingSpeed = 2;

...

```

## Comment passer à la phase suivante

Dans la plupart de ces phases, nous avons également une valeur de seuil qui met fin à la phase et déclenche la suivante. Les phases d'attente et d'étirement sont les exceptions car leur fin est basée sur l'interaction de l'utilisateur. La phase d'attente se termine avec l'événement `mousedown` et la phase d'étirement se termine avec l'événement `mouseup`.

La phase de rotation s'arrête lorsque le bâton tombe à plat et que sa rotation atteint 90 degrés. La phase de marche se termine lorsque le héros atteint le bord de la plateforme suivante ou la fin du bâton. Et ainsi de suite. 

Si ces seuils sont atteints, la boucle principale du jeu définit le jeu à la phase suivante et dans la boucle suivante, il agira en conséquence. Examinons cela plus en détail.

### La phase d'attente

Si nous sommes dans la phase d'attente et que rien ne se passe, nous retournons de la fonction. Cette instruction de retour signifie que nous n'atteignons jamais la fin de la fonction et qu'il n'y aura pas une autre demande de frame d'animation. La boucle s'arrête. Nous avons besoin du gestionnaire d'entrée utilisateur pour déclencher une autre boucle.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Stick-Hero.001-1.jpeg)
_Dans la phase d'attente, rien ne se passe_

```javascript
function animate(timestamp) {
	...

  switch (phase) {
    case "waiting":
      return; // Arrêter la boucle

    ...

  }

	...
}

```

### La phase d'étirement

Dans la phase d'étirement, nous augmentons la longueur du dernier bâton en fonction du temps écoulé et attendons que l'utilisateur relâche la souris. Le dernier bâton est toujours celui devant le héros. Après chaque transition de vue, un nouveau bâton est ajouté à la plateforme actuelle.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Stick-Hero.002-1.jpeg)
_Dans la phase d'étirement, nous augmentons la longueur du dernier bâton_

```javascript
function animate(timestamp) {
	...

  switch (phase) {
		...
    case "stretching": {
      sticks[sticks.length - 1].length += timePassed / stretchingSpeed;
			break;
    }
		...
  }

  ...
}

```

### La phase de rotation

Dans la phase de rotation, nous changeons la rotation du dernier bâton. Nous ne le faisons que jusqu'à ce que le bâton atteigne 90 degrés car cela signifie que le bâton a atteint une position plate. Ensuite, nous définissons la phase à la marche, afin que le prochain `requestAnimationFrame` ajuste le héros et non le bâton.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Stick-Hero.003-1.jpeg)
_Dans la phase de rotation, nous augmentons la rotation du dernier bâton_

Une fois que le bâton atteint 90 degrés, alors si le bâton tombe sur la plateforme suivante, nous augmentons également la valeur du score. Nous augmentons l'état `score` et mettons à jour l'attribut `innerText` de l'élément `scoreElement` (voir le chapitre sur le plan du fichier JavaScript). Ensuite, nous générons une nouvelle plateforme pour être sûr de ne jamais en manquer.

Si le bâton n'est pas tombé sur la plateforme suivante, nous n'augmentons pas le score et nous ne générons pas de nouvelle plateforme. Nous ne déclenchons pas non plus la phase de chute pour l'instant, car d'abord le héros essaie toujours de marcher le long du bâton.

```javascript
function animate(timestamp) {
  ...

  switch (phase) {
    ...
    case "turning": {
      sticks[sticks.length - 1].rotation += timePassed / turningSpeed;

      if (sticks[sticks.length - 1].rotation >= 90) {
        sticks[sticks.length - 1].rotation = 90;

        const nextPlatform = thePlatformTheStickHits();
        if (nextPlatform) {
          score++;
          scoreElement.innerText = score;

          generatePlatform();
        }

        phase = "walking";
      }
      break;
    }
    ...
  }

  ...
}

```

Cette phase utilise une fonction utilitaire pour déterminer si le bâton atterrira sur la plateforme ou non. Elle calcule la position de l'extrémité droite du dernier bâton et vérifie si cette position se situe entre les bords gauche et droit d'une plateforme. Si c'est le cas, elle retourne la plateforme, sinon elle retourne undefined.

```javascript
function thePlatformTheStickHits() {
  const lastStick = sticks[sticks.length - 1];
  const stickFarX = lastStick.x + lastStick.length;

  const platformTheStickHits = platforms.find(
    (platform) => platform.x < stickFarX && stickFarX < platform.x + platform.w
  );

  return platformTheStickHits;
}

```

### La phase de marche

Dans la phase de marche, nous déplaçons le héros vers l'avant. La fin de cette phase dépend du fait que le bâton atteint la plateforme suivante ou non. Pour déterminer cela, nous utilisons la même fonction utilitaire que nous venons de définir ci-dessus.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Stick-Hero.004-1.jpeg)
_Dans la phase de marche, nous augmentons la position X du héros_

Si l'extrémité du bâton tombe sur une plateforme, alors nous limitons la position du héros au bord de cette plateforme. Ensuite, une fois qu'il l'a atteinte, nous passons à la phase de transition. Si l'extrémité du bâton n'est pas tombée sur une plateforme, cependant, nous limitons le mouvement vers l'avant du héros jusqu'à la fin du bâton et ensuite nous commençons la phase de chute.

```javascript
function animate(timestamp) {
  ...

  switch (phase) {
    ...
    case "walking": {
      heroX += timePassed / walkingSpeed;

      const nextPlatform = thePlatformTheStickHits();
      if (nextPlatform) {
        // Si le héros atteindra une autre plateforme, limiter sa position à son bord
        const maxHeroX = nextPlatform.x + nextPlatform.w - 30;
        if (heroX > maxHeroX) {
          heroX = maxHeroX;
          phase = "transitioning";
        }
      } else {
        // Si le héros n'atteindra pas une autre plateforme, limiter sa position à la fin du bâton
        const maxHeroX =
          sticks[sticks.length - 1].x +
          sticks[sticks.length - 1].length;
        if (heroX > maxHeroX) {
          heroX = maxHeroX;
          phase = "falling";
        }
      }
      break;
    }
    ...
  }

  ...
}

```

### La phase de transition

Dans la phase de transition, nous déplaçons toute la scène. Nous voulons que le héros se tienne à la même position sur l'écran où il se tenait initialement, mais maintenant il se tient sur une plateforme différente. Cela signifie que nous devons calculer de combien nous devons décaler toute la scène vers l'arrière pour obtenir la même position. Ensuite, nous définissons simplement la phase à l'attente et nous attendons un autre événement de la souris.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Stick-Hero.005-1.jpeg)
_Dans la phase de transition, nous décalons toute la vue_

```javascript
function animate(timestamp) {
	...

  switch (phase) {
		...
    case "transitioning": {
      sceneOffset += timePassed / transitioningSpeed;

      const nextPlatform = thePlatformTheStickHits();
      if (nextPlatform.x + nextPlatform.w - sceneOffset < 100) {
        sticks.push({
          x: nextPlatform.x + nextPlatform.w,
          length: 0,
          rotation: 0,
        });
        phase = "waiting";
      }
      break;
    }
		...
  }

  ...
}

```

Nous savons que nous avons atteint la bonne position lorsque le côté droit de la plateforme - décalé par l'offset - atteint la position du côté droit de la première plateforme. Si nous regardons en arrière l'initialisation de la plateforme, nous voyons que la première plateforme a toujours une position X de 50 et sa largeur est également toujours de 50. Cela signifie que son extrémité droite sera à 100.

À la fin de cette phase, nous avons également ajouté un nouveau bâton au tableau des bâtons avec des valeurs initiales.

### La phase de chute

Dans le scénario d'échec, deux choses changent : la position du héros et la rotation du dernier bâton. Ensuite, une fois que le héros est tombé hors de l'écran, nous arrêtons à nouveau la boucle de jeu en retournant de la fonction.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Stick-Hero.006.jpeg)
_Dans la phase de chute, nous augmentons à la fois la position Y du héros et la rotation du dernier bâton_

```javascript
function animate(timestamp) {
	...

  switch (phase) {
		...
    case "falling": {
      heroY += timePassed / fallingSpeed;

      if (sticks[sticks.length - 1].rotation < 180) {
        sticks[sticks.length - 1].rotation += timePassed / turningSpeed;
      }

      const maxHeroY = platformHeight + 100;
      if (heroY > maxHeroY) {
        restartButton.style.display = "block";
        return;
      }
      break;
    }
		...
  }

  ...
}

```

Voilà donc la boucle principale - comment le jeu passe d'une phase à l'autre, en modifiant une série de variables. À la fin de chaque cycle, la fonction appelle la fonction `draw` pour mettre à jour la scène et demande une autre frame. Si vous avez tout fait correctement, vous devriez avoir un jeu fonctionnel maintenant !

# Résumé

Dans ce tutoriel, nous avons couvert beaucoup de choses. Nous avons appris à peindre des formes de base sur un élément `canvas` avec JavaScript et nous avons implémenté un jeu entier. 

Malgré la longueur de cet article, il y a encore quelques choses que nous n'avons pas couvertes ici. Vous pouvez consulter le [code source](https://codepen.io/HunorMarton/pen/xxOMQKg) de ce jeu pour des fonctionnalités supplémentaires sur [CodePen](https://codepen.io/HunorMarton/pen/xxOMQKg). Celles-ci incluent :

* Comment faire en sorte que le jeu s'adapte à toute la fenêtre du navigateur et traduire l'écran en conséquence.
* Comment dessiner un arrière-plan pour la scène et comment dessiner une version plus détaillée de notre héros.
* Nous ajoutons une zone de double score au milieu de chaque plateforme. Si l'extrémité du bâton tombe dans cette très petite région, le héros marque deux points.

J'espère que vous avez apprécié ce tutoriel. Restez à l'écoute pour plus de contenu ici sur freeCodeCamp et sur ma [chaîne YouTube](https://www.youtube.com/channel/UCxhgW0Q5XLvIoXHAfQXg9oQ).

%[https://youtu.be/eue3UdFvwPo?si=ACLc9iQOzKab8LYu]

## **Abonnez-vous pour plus de tutoriels sur le** Développement Web **:**

%[https://www.youtube.com/channel/UCxhgW0Q5XLvIoXHAfQXg9oQ]