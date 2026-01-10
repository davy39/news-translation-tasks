---
title: Tutoriel de développement de jeu JavaScript – Construisez Gorillas avec HTML
  Canvas + JavaScript
subtitle: ''
author: Hunor Márton Borbély
co_authors: []
series: null
date: '2024-01-30T18:18:55.000Z'
originalURL: https://freecodecamp.org/news/gorillas-game-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-21-at-16.02.31-1.png
tags:
- name: Game Development
  slug: game-development
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
seo_title: Tutoriel de développement de jeu JavaScript – Construisez Gorillas avec
  HTML Canvas + JavaScript
seo_desc: 'In this JavaScript game tutorial, you''ll learn how to create a modern
  version of the 1991 classic game Gorillas using plain JavaScript and the HTML canvas
  element.

  In this game, two gorillas throw explosive bananas at each other, and the first
  one to...'
---

Dans ce tutoriel de jeu JavaScript, vous apprendrez à créer une version moderne du jeu classique de 1991 Gorillas en utilisant du JavaScript simple et l'élément HTML canvas.

Dans ce jeu, deux gorilles se lancent des bananes explosives, et le premier à toucher l'autre gagne la partie.

Nous allons construire tout le jeu à partir de zéro ici. Tout d'abord, vous apprendrez à dessiner sur un élément canvas avec JavaScript. Vous verrez comment dessiner l'arrière-plan, les bâtiments, les gorilles et la bombe. Nous n'utiliserons aucune image ici – nous dessinerons tout en utilisant du code.

Ensuite, nous ajouterons des interactions et des gestionnaires d'événements. Nous couvrirons également comment viser, comment animer la bombe à travers le ciel, et comment détecter si la bombe a touché l'autre gorille, ou un bâtiment.

Tout au long du tutoriel, nous utiliserons du JavaScript simple. Pour tirer le meilleur parti de ce tutoriel, vous devriez avoir une compréhension de base de JavaScript. Mais même si vous êtes débutant, vous pouvez toujours suivre et apprendre en cours de route.

Dans cet article, nous simplifierons quelques étapes. Pour plus de détails, vous pouvez également regarder le [tutoriel étendu sur YouTube](https://www.youtube.com/watch?v=2q5EufbUEQk). Dans la version YouTube, nous couvrons également comment rendre les bâtiments destructibles, comment animer la main du gorille pour suivre le mouvement de glisser pendant le visée, avoir des graphismes plus beaux, et nous ajoutons une logique d'IA, afin que vous puissiez jouer contre l'ordinateur.

%[https://www.youtube.com/watch?v=2q5EufbUEQk]

Si vous êtes bloqué, vous pouvez également trouver le code source final du jeu que nous allons créer sur [GitHub](https://github.com/HunorMarton/gorillas).

## Table des matières :

1. [Contexte du jeu](#heading-contexte-du-jeu)
2. [Installation du projet](#heading-installation-du-projet)
3. [Aperçu de la logique du jeu](#heading-aperçu-de-la-logique-du-jeu)
4. [Comment dessiner la scène](#heading-comment-dessiner-la-scène)
5. [Comment inverser le système de coordonnées](#heading-comment-inverser-le-système-de-coordonnées)
6. [Comment dessiner les éléments du jeu](#heading-comment-dessiner-les-éléments-du-jeu)
7. [Comment adapter la taille de la ville à la fenêtre du navigateur](#heading-comment-adapter-la-taille-de-la-ville-à-la-fenêtre-du-navigateur)
8. [Comment le gorille peut lancer la bombe](#heading-comment-le-gorille-peut-lancer-la-bombe)
9. [Comment animer la bombe entrante](#heading-comment-animer-la-bombe-entrante)
10. [Prochaines étapes](#heading-prochaines-étapes)

## Contexte du jeu

[Gorillas](https://en.wikipedia.org/wiki/Gorillas_%28video_game%29) est un jeu de 1991. Dans ce jeu, deux gorilles sont debout sur le toit de bâtiments générés aléatoirement et se lancent à tour de rôle des bananes explosives.

À chaque tour, les joueurs définissent l'angle et la vitesse du lancer, et continuent à les affiner, jusqu'à ce qu'ils touchent l'autre gorille. La bombe de banane volante est affectée par la gravité et le vent.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-07-at-22.58.23-1.png)
_Le jeu original Gorillas de 1991 (source : retrogames.cz)_

Nous allons implémenter une version moderne de ce jeu. Le jeu original ne supportait pas la souris. À chaque tour, les joueurs devaient taper l'angle et la vitesse avec un clavier. Nous allons l'implémenter avec le support de la souris, et des graphismes plus beaux.

Vous pouvez essayer la version étendue du jeu sur [CodePen](https://codepen.io/HunorMarton/pen/jOJZqvp). Essayez-le avant de commencer.

%[https://codepen.io/HunorMarton/pen/jOJZqvp]

## Installation du projet

Pour implémenter ce jeu, nous allons avoir un simple fichier HTML, CSS et JavaScript. Vous pouvez diviser la logique JavaScript en plusieurs fichiers si vous le souhaitez, mais pour simplifier, nous avons tout au même endroit.

Comme nous utilisons du JavaScript simple et n'utilisons aucune bibliothèque et outils tiers, nous n'avons pas besoin de compilateurs ou de constructeurs. Nous pouvons exécuter les choses directement dans le navigateur.

Pour simplifier le processus, je recommande d'installer l'extension VS Code [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer). Avec cette extension installée, vous pouvez simplement faire un clic droit sur le fichier HTML et sélectionner 'Ouvrir avec Live Server'. Cela exécutera une version live du jeu dans le navigateur.

Cela signifie que nous n'avons pas à actualiser le navigateur à chaque fois que nous apportons une modification dans le code. Il suffit que nous sauvegardions les modifications dans le fichier et le navigateur s'actualisera automatiquement.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-18-at-21.29.22-1.png)
_Exécution du jeu avec l'extension Live Server VS Code_

## Aperçu de la logique du jeu

Avant d'entrer dans les détails, passons en revue les principales parties du jeu.

Le jeu est piloté par l'état du jeu. Il s'agit d'un objet JavaScript qui sert de métadonnées pour le jeu. De la taille des bâtiments à la position actuelle de la bombe, il inclut de nombreuses choses.

L'état du jeu inclut des éléments tels que : à qui est le tour, sommes-nous en train de viser maintenant, ou la bombe est-elle déjà en vol ? Et ainsi de suite. Ce sont toutes des variables que nous devons suivre. Lorsque nous dessinons la scène du jeu, nous la dessinerons en fonction de l'état du jeu.

Ensuite, nous avons la fonction `draw`. Cette fonction dessine presque tout ce que nous avons à l'écran. Elle peint l'arrière-plan, les bâtiments, les gorilles et les bombes de banane. Cette fonction peint tout l'écran de haut en bas à chaque fois que nous l'appelons.

Nous allons ajouter la gestion des événements pour viser les bombes et nous implémenterons la fonction `throwBomb` qui lance la boucle d'animation. La fonction `animate` déplace les bombes à travers le ciel.

Cette fonction sera responsable du calcul de la position exacte de la bombe alors qu'elle vole dans les airs à chaque cycle d'animation. En plus de cela, elle doit également déterminer quand le mouvement se termine. À chaque mouvement, nous vérifions si nous avons touché un bâtiment ou un ennemi, ou si la bombe est sortie de l'écran. Nous ajouterons également la détection des impacts.

Maintenant, passons en revue nos fichiers initiaux.

### Le fichier HTML initial

Notre fichier HTML initial sera très simple. Dans l'en-tête, nous ajouterons un lien vers notre feuille de style et notre fichier JavaScript. Notez que j'utilise le mot-clé `defer` pour m'assurer que le script ne s'exécute qu'une fois le reste du document analysé.

Dans le corps, nous ajouterons un élément `canvas`. Nous allons peindre sur cet élément avec JavaScript. Presque tout ce que nous pouvons voir à l'écran sera dans cet élément canvas. Voici le code :

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>Gorillas</title>
    <link rel="stylesheet" href="index.css" />
    <script src="index.js" defer></script>
  </head>
  <body>
    <canvas id="game"></canvas>
  </body>
</html>
```

Plus tard, nous allons ajouter plus de choses dans ce fichier. Nous ajouterons des panneaux d'information pour montrer l'angle et la vitesse du lancer actuel. Mais pour l'instant, c'est tout ce que nous avons.

### Le fichier CSS initial

Initialement, notre CSS est également très simple. Nous ne pouvons pas styliser quoi que ce soit à l'intérieur de l'élément canvas, donc ici nous stylisons uniquement les autres éléments que nous avons.

```css
body {
  margin: 0;
  padding: 0;
}
```

Plus tard, lorsque nous ajouterons plus d'éléments en HTML, nous mettrons également à jour ce fichier. Pour l'instant, assurons-nous que notre canvas peut s'adapter à toute la fenêtre. Par défaut, les navigateurs ont tendance à ajouter une petite marge ou un remplissage autour du corps. Supprimons cela.

### Les principales parties de notre fichier JavaScript

La plupart de la logique sera dans notre fichier JavaScript. Passons en revue les principales parties de ce fichier, et définissons quelques fonctions de remplissage :

* Nous déclarons l'objet `state` du jeu et un ensemble de variables utilitaires. Cela contiendra les métadonnées de notre jeu. Pour l'instant, c'est un objet vide. Nous initialiserons sa valeur lorsque nous arriverons à la fonction `newGame`.
* Ensuite, nous avons des références à chaque élément HTML que nous devons accéder depuis JavaScript. Pour l'instant, nous n'avons qu'une référence à l'élément `<canvas>`. Nous accédons à cet élément par son ID.
* Nous initialisons l'état du jeu et peignons la scène en appelant la fonction `newGame`. C'est le seul appel de fonction de niveau supérieur. Cette fonction est responsable à la fois de l'initialisation du jeu et de sa réinitialisation.
* Nous définissons la fonction `draw` qui dessine toute la scène sur l'élément canvas en fonction de l'état du jeu. Nous dessinerons l'arrière-plan, les bâtiments, les gorilles et la bombe.
* Nous configurons les gestionnaires d'événements pour les événements `mousedown`, `mousemove` et `mouseup`. Nous allons les utiliser pour le visée.
* L'événement `mouseup` déclenchera la fonction `throwBomb` qui lance la boucle d'animation principale. La fonction `animate` manipulera l'état à chaque cycle d'animation et appellera la fonction `draw` pour mettre à jour l'écran.

```js
// L'état du jeu
let state = {};
// ...

// Références aux éléments HTML
const canvas = document.getElementById("game");
// ...

newGame();

function newGame() {
  // Initialiser l'état du jeu
  state = {
    // ...
  };

  // ...

  draw();
}

function draw() {
  // ...
}

// Gestionnaires d'événements
// ...

function throwBomb() {
  // ...
}

function animate(timestamp) {
  // ...
}

```

Nous aurons quelques fonctions utilitaires supplémentaires, mais elles sont moins importantes. Nous les discuterons au fur et à mesure.

### Phases du jeu

Dans l'étape suivante, nous allons configurer notre état de jeu initial. Avant d'aborder les différentes parties de l'état, parlons de l'une de ses propriétés les plus importantes : la propriété de `phase` du jeu.

![Image](https://www.freecodecamp.org/news/content/images/2024/08/game-phases.jpg)
_Les trois phases du jeu : la phase de `visée`, la phase `en vol` et la phase de `célébration`_

Le jeu comporte trois phases différentes. Le jeu commence dans la phase de `visée`, lorsque la bombe est dans la main d'un gorille et que les gestionnaires d'événements sont actifs. Ensuite, une fois que vous lancez la bombe, le jeu passe à la phase `en vol`. Dans cette phase, les gestionnaires d'événements sont désactivés et la fonction `animate` déplace la bombe à travers le ciel. Nous ajoutons également la détection des impacts pour savoir quand nous devons arrêter l'animation.

Ces deux phases de jeu se répètent encore et encore, jusqu'à ce que l'un des gorilles touche l'autre. Une fois que nous avons touché l'ennemi, le jeu passe à la phase de `célébration`. Nous dessinons un gorille gagnant, affichons l'écran de félicitations et un bouton pour redémarrer le jeu.

### Comment initialiser le jeu

Le jeu est initialisé par la fonction `newGame`. Cela réinitialise l'état du jeu, génère un nouveau niveau et appelle la fonction `draw` pour dessiner toute la scène.

Passons en revue ce que nous avons initialement dans l'objet `state` :

* Tout d'abord, nous avons la propriété de `phase` du jeu qui peut être soit `visée`, `en vol`, ou `célébration`.
* Ensuite, la propriété `currentPlayer` nous indique à qui est le tour – le joueur de gauche ou le joueur de droite.
* L'objet `bomb` décrit la position actuelle de la bombe et sa vitesse. Sa position initiale doit être alignée avec le deuxième bâtiment, donc nous ne la définissons qu'une fois le niveau généré.
* Le tableau `buildings` définit la position et la taille des bâtiments qui apparaissent à l'écran. Nous générons les métadonnées des bâtiments avec une fonction utilitaire que nous discuterons plus tard.

```js
// L'état du jeu
let state = {};

. . .

newGame();

function newGame() {
  // Initialiser l'état du jeu
  state = {
    phase: "aiming", // aiming | in flight | celebrating
    currentPlayer: 1,
    bomb: {
      x: undefined,
      y: undefined,
      velocity: { x: 0, y: 0 },
    },
    buildings: generateBuildings(),
  };
    
  initializeBombPosition();
    
  draw();
}
```

Nous discuterons des fonctions utilitaires utilisées ci-dessus (`generateBuildings` et `initializeBombPosition`) dans le prochain chapitre alors que nous dessinons les bâtiments et la bombe. Pour l'instant, ajoutons simplement quelques fonctions de remplissage pour nous assurer que nous n'obtenons pas d'erreur de JavaScript.

```js
function generateBuildings() {
  // ...
}

function initializeBombPosition() {
  // ...
}
```

Maintenant que nous avons une structure de notre application et que nous avons initialisé certains des états, changeons de vitesse et commençons à dessiner sur le canvas tout en remplissant les pièces manquantes de l'état.

## Comment dessiner la scène

La fonction `draw` peint tout le canvas en fonction de l'état. Elle dessine l'arrière-plan et les bâtiments, dessine les gorilles et dessine la bombe. La fonction peut également dessiner différentes variations de gorille en fonction de l'état. Le gorille a une apparence différente pendant le visée, la célébration ou l'attente de l'impact.

Nous utiliserons cette fonction à la fois pour peindre la scène initiale et tout au long de notre boucle d'animation principale.

Pour la peinture initiale, certaines des fonctionnalités que nous couvrons ici ne seront pas nécessaires. Par exemple, nous couvrirons également comment dessiner le gorille célébrant, alors que nous ne le verrons qu'une fois le jeu terminé. Mais nous le couvrirons quand même car ainsi nous n'aurons pas à revenir à cette fonction une fois que nous commencerons à animer l'état.

Tout ce que nous dessinons dans cette fonction est basé sur l'état, et il n'importe pas à la fonction si le jeu est dans l'état initial, ou si nous sommes plus loin dans le jeu.

Nous avons défini un élément `<canvas>` en HTML. Comment dessinons-nous des choses dessus ?

```html
. . .

<body>
  <canvas id="game"></canvas>
</body>

. . .
```

En JavaScript, nous obtenons d'abord l'élément canvas par son ID. Ensuite, nous définissons la taille du canvas pour remplir toute la fenêtre du navigateur. Et enfin, nous obtenons son contexte de dessin.

Il s'agit d'une API intégrée avec de nombreuses méthodes et propriétés que nous pouvons utiliser pour dessiner sur le canvas. Voyons quelques exemples de l'utilisation de cette API.

```js
. . . 

// L'élément canvas et son contexte de dessin 
const canvas = document.getElementById("game"); 
canvas.width = window.innerWidth; 
canvas.height = window.innerHeight; 
const ctx = canvas.getContext("2d"); 

. . . 

function draw() {
  // ... 
} 

. . . 
```

### Exemple : Dessiner un rectangle

Regardons quelques exemples rapides. Ceux-ci ne font pas encore partie de notre jeu, ils serviront simplement d'introduction.

La chose la plus basique que nous pouvons faire est de remplir un rectangle.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-21-at-23.00.23-1.png)
_Utilisation de la méthode `fillRect` pour remplir un rectangle_

```js
const canvas = document.getElementById("game");
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
const ctx = canvas.getContext("2d");

ctx.fillStyle = "#58A8D8";

ctx.fillRect(200, 200, 440, 320);
```

Avec la méthode `fillRect`, nous spécifions la coordonnée en haut à gauche de notre rectangle (200, 200), et nous définissons sa largeur et sa hauteur (440, 320).

Par défaut, la couleur de remplissage sera noire. Nous pouvons la changer en définissant la propriété `fillStyle`.

Le fonctionnement du canvas est tel que nous devons définir les paramètres de dessin avant de peindre, et non l'inverse. Ce n'est pas comme si nous peignions un rectangle, puis nous pouvons changer sa couleur. Une fois que quelque chose est sur le canvas, il reste tel quel.

Vous pouvez le considérer comme un vrai canvas, où vous choisissez également la couleur avec votre pinceau avant de commencer à peindre avec. Ensuite, une fois que vous avez peint quelque chose, vous pouvez soit le couvrir en peignant par-dessus, soit essayer d'effacer le canvas. Mais vous ne pouvez pas vraiment changer les parties existantes. C'est pourquoi nous définissons la couleur ici à l'avance et non après.

Nous allons dessiner des rectangles pour remplir l'arrière-plan et pour montrer les bâtiments.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-21-at-19.30.36.png)
_L'arrière-plan et les bâtiments sont des rectangles simples_

### Exemple : Remplir un chemin

Nous pouvons bien sûr dessiner des formes plus compliquées également. Nous pouvons définir un chemin, comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-21-at-23.01.23-1.png)
_Remplir un chemin_

```js
const canvas = document.getElementById("game");
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
const ctx = canvas.getContext("2d");

ctx.fillStyle = "#58A8D8";

ctx.beginPath();
ctx.moveTo(200, 200);
ctx.lineTo(500, 350);
ctx.lineTo(200, 500);
ctx.fill();
```

Les chemins commencent par la méthode `beginPath` et se terminent en appelant soit la méthode `fill` soit la méthode `stroke` – ou les deux. Entre les deux, nous construisons le chemin en appelant des méthodes de construction de chemin.

Dans cet exemple, nous dessinons un triangle. Nous nous déplaçons vers la coordonnée `300,300` avec la méthode `moveTo`. Ensuite, nous appelons la méthode `lineTo` pour nous déplacer vers le côté droit de notre forme. Et ensuite, nous continuons le chemin, en appelant à nouveau la méthode `lineTo` vers `300,400`.

Rien de tout cela ne serait visible si nous n'avions pas terminé par la méthode `fill` pour remplir le chemin que nous venons de construire.

Nous allons remplir des chemins pour dessiner notre gorille et notre bombe.

![Image](https://www.freecodecamp.org/news/content/images/2024/08/paths-gorilla-drawing.jpg)
_Nous utiliserons des chemins pour dessiner le corps principal du gorille_

### Exemple : Dessiner un trait

De manière très similaire, nous pouvons également dessiner une ligne. Ici, nous commencerons par la méthode `beginPath`. Nous construirons également la forme avec une méthode `moveTo` et deux méthodes `lineTo`. Les coordonnées ici sont les mêmes. Mais à la fin, nous n'appelons pas `fill` mais la méthode `stroke`. Cela, au lieu de remplir la forme, dessinera la ligne que nous avons construite.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-21-at-23.02.34-1.png)
_Dessiner un trait_

```js
const canvas = document.getElementById("game");
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
const ctx = canvas.getContext("2d");

ctx.strokeStyle = "#58A8D8";
ctx.lineWidth = 30;

ctx.beginPath();
ctx.moveTo(200, 200);
ctx.lineTo(500, 350);
ctx.lineTo(200, 500);
ctx.stroke();
```

Les traits ont différentes propriétés de style. Au lieu de la propriété `fillStyle`, nous définissons `strokeStyle`. À cette propriété – et également à `fillStyle` – nous pouvons assigner n'importe quelle valeur de couleur qui est valide en CSS. Pour définir la largeur de la ligne, nous utilisons la propriété `lineWidth`.

Nous pouvons également construire des chemins plus complexes. Dans l'exemple ci-dessous, nous dessinons une courbe. Nous allons couvrir cela un peu plus en détail lorsque nous dessinerons les bras des gorilles.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-21-at-23.05.04-1.png)
_Dessiner une courbe_

```js
const canvas = document.getElementById("game");
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
const ctx = canvas.getContext("2d");

ctx.strokeStyle = "#58A8D8";
ctx.lineWidth = 30;

ctx.beginPath();
ctx.moveTo(200, 300);
ctx.quadraticCurveTo(500, 400, 800, 300);
ctx.stroke();
```

Nous allons utiliser la méthode `stroke` pour dessiner les bras et le visage du gorille.

![Image](https://www.freecodecamp.org/news/content/images/2024/08/gorilla-stroke-drawing.jpg)
_Nous utilisons la méthode `stroke` pour dessiner les bras et le visage du gorille_

Maintenant que nous avons terminé cette introduction, revenons à notre jeu et voyons ce qu'il y a dans la fonction `draw`.

## Comment inverser le système de coordonnées

Lorsque nous utilisons le canvas, nous avons un système de coordonnées avec l'origine dans le coin supérieur gauche de la fenêtre du navigateur qui grandit vers la droite et vers le bas. Cela est aligné avec le fonctionnement général des sites web. Les choses vont de gauche à droite et de haut en bas. C'est le comportement par défaut, mais nous pouvons le changer.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-21-at-23.09.35-1.png)
_Le système de coordonnées par défaut_

Lorsque nous parlons de jeux, il est plus pratique d'aller de bas en haut. Par exemple, lorsque nous dessinons des bâtiments, ils peuvent commencer en bas, et nous n'avons pas à déterminer où se trouve le bas de la fenêtre.

Nous pouvons utiliser la méthode `translate` pour décaler tout le système de coordonnées vers le coin inférieur gauche. Nous devons simplement déplacer le système de coordonnées vers le bas le long de l'axe Y par la taille de la fenêtre du navigateur.

Une fois que nous avons fait cela, la coordonnée Y continue de croître vers le bas. Nous pouvons l'inverser en utilisant la méthode `scale`. Définir un nombre négatif pour la direction verticale inversera tout le système de coordonnées.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-21-at-23.09.32-1.png)
_Le système de coordonnées à l'envers_

```js
// L'élément canvas et son contexte de dessin 
const canvas = document.getElementById("game"); 
canvas.width = window.innerWidth; 
canvas.height = window.innerHeight; 
const ctx = canvas.getContext("2d"); 

. . . 

function draw() { 
  ctx.save(); 
  // Inverser le système de coordonnées 
  ctx.translate(0, window.innerHeight); 
  ctx.scale(1, -1); 
  
  // Dessiner la scène 
  drawBackground(); 
  drawBuildings();
  drawGorilla(1);
  drawGorilla(2);
  drawBomb(); 
  
  // Restaurer la transformation 
  ctx.restore(); 
}
```

Maintenant, implémentons la fonction `draw`. L'une des premières choses que nous faisons est d'appeler les méthodes `translate` et `scale` pour inverser le système de coordonnées.

Nous devons faire cela avant de peindre quoi que ce soit sur le canvas car les méthodes `translate` et `scale` ne déplacent pas réellement quoi que ce soit sur le canvas. Si nous avions peint quoi que ce soit sur le canvas avant, cela resterait tel quel.

Techniquement, ces méthodes changent la matrice de transformation. Vous pouvez penser à cela comme changer le système de coordonnées. Tout ce que nous peignons après ces méthodes sera peint selon ce nouveau système de coordonnées.

Nous devons également restaurer ces transformations une fois que nous avons dessiné en appelant la méthode `restore`. La méthode `restore` vient en paire avec la méthode `save`. `save` sert de point de contrôle auquel la méthode `restore` peut revenir.

Il est courant de commencer un bloc de dessin en appelant la méthode `save` et de le terminer avec la méthode `restore` lorsque nous utilisons des transformations entre les deux.

Nous devons appeler ces deux fonctions car les méthodes `translate` et `scale` s'accumulent. Nous allons appeler la fonction `draw` plusieurs fois. Sans les méthodes `save` et `restore`, le système de coordonnées continuerait à descendre à chaque fois que nous appelons la fonction `draw`, et il finirait par sortir complètement de l'écran.

Dessiner toute la scène comprend de nombreuses parties. Nous allons le décomposer en fonctions de dessin séparées. Maintenant, commençons à dessiner en implémentant ces fonctions :

```js
function drawBackground() {
  // ...
}

function drawBuildings() {
  // ...
}

function drawGorilla(player) {
  // ...
}

function drawBomb() {
  // ...
}
```

## Comment dessiner les éléments du jeu

### Comment dessiner l'arrière-plan

Lorsque nous dessinons sur un canvas, l'ordre compte. Nous commencerons par l'arrière-plan, puis nous irons couche par couche. Dans notre cas, l'arrière-plan est un simple rectangle.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-30-at-16.00.14.png)
_Le ciel en arrière-plan_

```js
function drawBackground() {
  ctx.fillStyle = "#58A8D8";
  ctx.fillRect(0, 0, window.innerWidth, window.innerHeight);
}
```

Nous dessinons ce rectangle de la même manière que nous l'avons fait dans notre introduction. Tout d'abord, nous définissons le style de remplissage, puis nous dessinons un rectangle avec la méthode `fillRect`. Ici, nous définissons les coordonnées de départ dans le coin et définissons la taille pour remplir toute la fenêtre du navigateur.

Nous pourrions également ajouter une lune dans le ciel. Malheureusement, il n'y a pas de méthode de cercle de remplissage qui pourrait facilement faire cela, donc nous allons le sauter pour l'instant. Sur [CodePen](https://codepen.io/HunorMarton/full/jOJZqvp) vous pouvez trouver une version qui dessine également une lune dans la fonction `drawBackground`.

### Comment dessiner les bâtiments

Dessiner les bâtiments comporte deux parties. Tout d'abord, nous devons générer des métadonnées pour les bâtiments lorsque nous initialisons le niveau. Ensuite, nous implémentons la fonction `drawBuildings` qui peint les bâtiments en fonction de ces métadonnées.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-19-at-17.02.52-1.png)
_Les bâtiments et leurs métadonnées_

### Métadonnées des bâtiments

Dans la fonction `newGame`, nous avons appelé la fonction `generateBuildings` pour initialiser la propriété `buildings` dans notre état de jeu `state`. Nous n'avons pas encore implémenté cette fonction.

```js
  . . .

  state = {
    phase: "aiming", // aiming | in flight | celebrating
    currentPlayer: 1,
    bomb: {
      x: undefined,
      y: undefined,
      velocity: { x: 0, y: 0 },
    },
    buildings: generateBuildings(),
  };

  . . .

```

Voyons comment fonctionne cette fonction. Chaque bâtiment est défini par sa position `x`, sa `largeur` et sa `hauteur`.

La coordonnée `x` est toujours alignée sur le bâtiment précédent. Nous vérifions où se termine le bâtiment précédent, et nous ajoutons un petit écart. Dans le cas où il n'y a pas de bâtiment précédent – parce que nous ajoutons le premier – alors nous commençons au début de l'écran à 0.

```js
function generateBuildings() {
  const buildings = [];
  for (let index = 0; index < 8; index++) {
    const previousBuilding = buildings[index - 1];
    
    const x = previousBuilding
      ? previousBuilding.x + previousBuilding.width + 4
      : 0;

    const minWidth = 80;
    const maxWidth = 130;
    const width = minWidth + Math.random() * (maxWidth - minWidth);

    const platformWithGorilla = index === 1 || index === 6;

    const minHeight = 40;
    const maxHeight = 300;
    const minHeightGorilla = 30;
    const maxHeightGorilla = 150;

    const height = platformWithGorilla
      ? minHeightGorilla + Math.random() * (maxHeightGorilla - minHeightGorilla)
      : minHeight + Math.random() * (maxHeight - minHeight);

    buildings.push({ x, width, height });
  }
  return buildings;
}
```

Ensuite, la fonction génère une `largeur` de bâtiment aléatoire dans une plage prédéfinie. Nous définissons la largeur minimale et maximale, et choisissons un nombre aléatoire entre les deux.

Nous générons une `hauteur` de bâtiment aléatoire de manière similaire avec une différence : la `hauteur` d'un bâtiment dépend également du fait qu'un gorille se tient dessus ou non.

Si un gorille se tient sur le bâtiment, alors la plage de hauteur est plus petite. Nous voulons avoir des bâtiments relativement plus hauts entre les deux gorilles afin qu'ils ne puissent pas simplement se voir en ligne droite.

Nous saurons si un gorille se tient sur le bâtiment car ils se tiennent toujours sur les mêmes bâtiments. Le deuxième à partir de la gauche, et l'avant-dernier. Si l'index du bâtiment correspond à ces positions, nous définissons la hauteur en fonction d'une plage différente.

Ensuite, nous poussons ces trois valeurs sous forme d'objet dans le tableau `buildings`, et à la dernière ligne, nous retournons ce tableau depuis la fonction. Cela définira le tableau `buildings` dans notre état de jeu `state`.

### Comment dessiner les bâtiments

Maintenant que nous avons les métadonnées pour les bâtiments, nous pouvons les dessiner à l'écran.

La fonction `drawBuildings` est très simple. Nous itérons sur le tableau que nous venons de générer et dessinons un simple rectangle pour chacun. Nous utilisons la même méthode `fillRect` que nous avons utilisée pour dessiner le ciel. Nous appelons cette fonction avec les attributs du bâtiment (la position Y est 0 car le bâtiment commence en bas de l'écran).

```js
function drawBuildings() {
  state.buildings.forEach((building) => {
    ctx.fillStyle = "#152A47";
    ctx.fillRect(building.x, 0, building.width, building.height);
  });
}
```

Une fois que nous avons terminé cela, nous devrions voir une ligne de bâtiments. Les métadonnées sont régénérées à chaque fois que nous commençons le jeu. À chaque fois que nous actualisons la fenêtre du navigateur, nous voyons un arrière-plan différent.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-19-at-16.57.16-1.png)
_Bâtiments générés aléatoirement_

### Comment dessiner les gorilles

Dessiner les gorilles est l'une des parties les plus compliquées et les plus amusantes de ce jeu. Enfin, nous ne dessinons pas seulement des rectangles – nous dessinons des chemins.

![Image](https://www.freecodecamp.org/news/content/images/2024/08/gorilla-variations.jpg)
_Les différentes variations des gorilles_

Les gorilles ont également différentes variations en fonction de l'état du jeu. Le gorille a une apparence différente pendant le visée, l'attente de la bombe entrante et la célébration après un coup réussi.

Dans la fonction `draw`, nous appelons la fonction `drawGorilla` deux fois. Nous dessinons deux gorilles : un sur le deuxième toit et un sur l'avant-dernier toit. Ils sont principalement identiques, mais ils se reflètent l'un l'autre pendant le visée. Lorsque celui de gauche vise, il lève sa main gauche, et lorsque celui de droite vise, il lève sa main droite.

```js
function draw() {
  ctx.save();
  // Inverser le système de coordonnées
  ctx.translate(0, window.innerHeight);
  ctx.scale(1, -1);

  // Dessiner la scène
  drawBackground();
  drawBuildings();
  drawGorilla(1);
  drawGorilla(2);
  drawBomb();

  // Restaurer la transformation
  ctx.restore();
}
```

Nous allons décomposer le dessin du gorille en plusieurs étapes également. Nous utiliserons différentes fonctions pour dessiner le corps principal, pour dessiner les bras, et pour dessiner le visage du gorille.

Pour simplifier les choses, nous allons à nouveau `translater` notre système de coordonnées. Nous `translatons` le système de coordonnées vers le milieu du toit sur lequel le gorille se tient. De cette façon, nous pouvons dessiner les deux gorilles de la même manière. Nous devons simplement translater l'origine de notre système de coordonnées vers un bâtiment différent.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-30-at-16.58.41.png)
_Déplacement de l'origine du système de coordonnées vers le haut du bâtiment sur lequel le gorille se tient_

En tant qu'argument, la fonction `drawGorilla` reçoit quel `player` nous dessinons actuellement. Pour dessiner le gorille de gauche, nous translatons vers le haut du deuxième bâtiment, et pour dessiner celui de droite, nous translatons vers le haut de l'avant-dernier bâtiment.

```js
function drawGorilla(player) {
  ctx.save();
  const building =
    player === 1
      ? state.buildings.at(1) // Deuxième bâtiment
      : state.buildings.at(-2); // Avant-dernier bâtiment

  ctx.translate(building.x + building.width / 2, building.height);

  drawGorillaBody();
  drawGorillaLeftArm(player);
  drawGorillaRightArm(player);
  drawGorillaFace();
  
  ctx.restore();
}
```

Parce que nous utilisons la méthode `translate`, cette fonction commence par sauvegarder le système de coordonnées actuel et se termine par le restaurer.

Maintenant, regardons les fonctions qui dessinent les différentes parties d'un gorille.

```js
function drawGorillaBody() {
  // ...
}

function drawGorillaLeftArm(player) {
  // ...
}

function drawGorillaRightArm(player) {
  // ...
}

function drawGorillaFace() {
  // ...
}
```

#### Comment dessiner le corps du gorille

Nous dessinons le corps du gorille comme un chemin. Nous avons dessiné un chemin dans notre introduction au dessin sur un canvas. Nous utilisons la méthode `moveTo` et une série de méthodes `lineTo` pour dessiner la partie principale du gorille.

Nous définissons le style de remplissage sur noir, puis nous commençons un chemin. Nous nous déplaçons vers une coordonnée au milieu puis nous dessinons des lignes droites pour dessiner la silhouette du gorille. Une fois terminé, nous remplissons la forme avec la méthode `fill`.

![Image](https://www.freecodecamp.org/news/content/images/2024/08/gorilla-path-fill.jpg)
_Le corps, la tête et les jambes du gorille. L'image de droite montre le chemin que nous remplissons._

```js
function drawGorillaBody() {
  ctx.fillStyle = "black";
    
  ctx.beginPath(); 
  
  // Position de départ
  ctx.moveTo(0, 15); 
    
  // Jambe gauche
  ctx.lineTo(-7, 0);
  ctx.lineTo(-20, 0); 
    
  // Corps principal
  ctx.lineTo(-13, 77);
  ctx.lineTo(0, 84);
  ctx.lineTo(13, 77); 
  
  // Jambe droite
  ctx.lineTo(20, 0);
  ctx.lineTo(7, 0);
  
  ctx.fill();
}
```

Au cas où vous vous demandez comment j'ai trouvé ces coordonnées, j'ai en fait commencé par un croquis initial avec un stylo et du papier. J'ai essayé d'estimer les coordonnées, je les ai essayées avec du code, puis je les ai ajustées jusqu'à ce qu'elles commencent à prendre la bonne forme. Bien sûr, vous pourriez avoir d'autres méthodes également.

#### Comment dessiner les bras du gorille

Alors que le corps était une partie relativement simple du gorille, les mains sont un peu plus compliquées. Elles viennent en différentes variations et nous les dessinons comme une courbe.

Commençons par le bras gauche. La partie principale de celui-ci est en fait seulement deux lignes. Nous utiliserons la méthode `moveTo` pour nous déplacer vers l'épaule du gorille, puis de là, nous dessinerons le bras comme une courbe quadratique avec la méthode `quadraticCurveTo`.

Une courbe quadratique est une courbe simple avec un point de contrôle. Alors que la courbe va du point de départ (que nous définirons avec `moveTo`), la courbe se courbe vers ce point de contrôle (définie comme les deux premiers arguments de la méthode `quadraticCurveTo`) alors qu'elle atteint sa position finale (définie comme les deux derniers arguments).

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-19-at-17.33.01-1.png)
_Les différentes coordonnées d'une courbe_

```js
function drawGorillaLeftArm(player) {
  ctx.strokeStyle = "black";
  ctx.lineWidth = 18;

  ctx.beginPath();
  ctx.moveTo(-13, 50);

  if (
    (state.phase === "aiming" && state.currentPlayer === 1 && player === 1) ||
    (state.phase === "celebrating" && state.currentPlayer === player)
  ) {
    ctx.quadraticCurveTo(-44, 63, -28, 107);
  } else {
    ctx.quadraticCurveTo(-44, 45, -28, 12);
  }
  
  ctx.stroke();
}
```

Ce qui rend cette fonction compliquée, c'est qu'elle a deux variations de la même courbe. Par défaut, les mains descendent à côté du corps (deuxième cas ci-dessus).

Si nous sommes dans la phase de `visée`, le `currentPlayer` est le joueur numéro 1, et nous dessinons le `player` 1, alors la main gauche monte (premier cas ci-dessus). La main gauche monte également si nous dessinons le gorille `célébrant` (également premier cas ci-dessus).

Dans ces cas, nous commençons depuis le même point (la courbe commence avec la même méthode `moveTo`), mais nous définissons différentes coordonnées pour le point de contrôle et le point final de la courbe.

Nous dessinons les mains comme des traits. Donc au lieu de terminer le chemin avec la méthode `fill`, nous utilisons la méthode `stroke` à la place.

Nous le configurons également différemment. Au lieu d'utiliser la propriété `fillStyle`, ici nous définissons la couleur avec `strokeStyle` et donnons de l'épaisseur au bras avec la propriété `lineWidth`.

![Image](https://www.freecodecamp.org/news/content/images/2024/08/gorilla-arm-variations.jpg)
_Les différentes variations de bras des gorilles dans les phases `visée`, `en vol` et `célébration`_

Dessiner le bras droit est le même, sauf que les coordonnées horizontales et certaines conditions sont inversées. Nous pourrions fusionner ces deux fonctions, mais pour plus de clarté, je les ai gardées séparées.

```js
function drawGorillaRightArm(player) {
  ctx.strokeStyle = "black";
  ctx.lineWidth = 18;

  ctx.beginPath();
  ctx.moveTo(+13, 50);

  if (
    (state.phase === "aiming" && state.currentPlayer === 2 && player === 2) ||
    (state.phase === "celebrating" && state.currentPlayer === player)
  ) {
    ctx.quadraticCurveTo(+44, 63, +28, 107);
  } else {
    ctx.quadraticCurveTo(+44, 45, +28, 12);
  }
  
  ctx.stroke();
}
```

En conséquence, nos gorilles devraient commencer à prendre forme. Ils n'ont toujours pas de visage, mais ils ont des mains maintenant. Et pour refléter notre état de jeu, celui de gauche a les mains en l'air, se préparant à lancer la bombe.

Vous pouvez tester notre solution en changeant l'état du jeu. Vous pouvez changer le `currentPlayer` et la propriété de `phase` du jeu pour voir les différentes variations.

#### Comment dessiner le visage du gorille

Le visage du gorille se compose de quelques lignes droites. Nous dessinerons les deux yeux et la bouche comme une ligne droite. Pour chacun, nous utiliserons une paire de méthodes `moveTo` et `lineTo`. Parce que chaque segment de ligne utilise le même `strokeStyle` et `lineWidth`, nous pouvons les dessiner comme un seul chemin.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-19-at-17.08.58.png)
_Les gorilles finis_

```js
function drawGorillaFace() {
  ctx.strokeStyle = "lightgray";
  ctx.lineWidth = 3;
  
  ctx.beginPath();

  // Œil gauche
  ctx.moveTo(-5, 70);
  ctx.lineTo(-2, 70);

  // Œil droit
  ctx.moveTo(2, 70);
  ctx.lineTo(5, 70);

  // Bouche
  ctx.moveTo(-5, 62);
  ctx.lineTo(5, 62);

  ctx.stroke();
}
```

Avec cela, nous avons nos gorilles finis avec toutes les variations. Il n'y a qu'une seule chose qui manque à l'écran : la bombe de banane.

### Comment dessiner la bombe

Maintenant, nous allons dessiner la bombe. La bombe sera un simple cercle. Mais avant de la dessiner, nous devons d'abord déterminer où elle se trouve.

#### Comment initialiser la position de la bombe

Si nous regardons en arrière notre fonction `newGame`, nous pouvons voir que les métadonnées de la bombe ont une position et une vitesse. La position jusqu'à présent est encore `undefined`. Avant de dessiner la bombe, déterminons d'abord sa position.

```js
function newGame() {
  // Initialiser l'état du jeu
  state = {
    phase: "aiming", // aiming | in flight | celebrating
    currentPlayer: 1,
    bomb: {
      x: undefined,
      y: undefined,
      velocity: { x: 0, y: 0 },
    },
    buildings: generateBuildings(),
  };
    
  initializeBombPosition();
    
  draw();
}
```

À la fin de la fonction `newGame`, nous appelons également la fonction `initializeBombPosition` avant de dessiner la scène. Implémentons cette fonction.

La fonction `initializeBombPosition` place la bombe dans la main du gorille qui lance la bombe à ce tour. Nous devons appeler cette fonction après avoir généré nos métadonnées de bâtiment car la position de la bombe dépend de la position du gorille, et celle-ci dépend du bâtiment sur lequel il se tient.

Tout d'abord, nous recherchons quel `building` nous devons aligner. Si c'est le tour du premier joueur, alors la bombe doit être dans la main gauche du gorille de gauche. Et si c'est le tour du deuxième joueur, alors elle doit être dans la main droite du gorille de droite.

Tout d'abord, nous calculerons le point milieu du toit dont nous avons besoin (`gorillaX` et `gorillaY`), puis nous décalerons la position pour correspondre à la main gauche ou droite du gorille.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-30-at-17.00.32.png)
_Calcul de la position de la bombe_

```js
function initializeBombPosition() {
  const building =
    state.currentPlayer === 1
      ? state.buildings.at(1) // Deuxième bâtiment
      : state.buildings.at(-2); // Avant-dernier bâtiment

  const gorillaX = building.x + building.width / 2;
  const gorillaY = building.height;

  const gorillaHandOffsetX = state.currentPlayer === 1 ? -28 : 28;
  const gorillaHandOffsetY = 107;
  
  state.bomb.x = gorillaX + gorillaHandOffsetX;
  state.bomb.y = gorillaY + gorillaHandOffsetY;
  state.bomb.velocity.x = 0;
  state.bomb.velocity.y = 0;
}
```

Nous allons également réinitialiser la vitesse ici. Plus tard, nous allons appeler cette fonction au début de chaque tour et nous en aurons besoin pour initialiser ces valeurs.

#### Comment dessiner la bombe

Maintenant que la bombe est au bon endroit, dessinons-la. Malheureusement, nous n'avons pas de méthode simple de cercle de remplissage, comme nous en avons dans le cas des rectangles. Nous devons dessiner un `arc` à la place.

Une méthode `arc` peut être appelée dans le cadre d'un chemin. Nous commencerons par la méthode `beginPath` et terminerons par la méthode `fill`.

La méthode `arc` a beaucoup de propriétés. Cela peut sembler un peu effrayant, mais nous n'avons besoin de nous concentrer que sur les trois premières lorsque nous dessinons des cercles :

* Les deux premiers arguments sont `x` et `y`, les coordonnées du centre de l'arc. Nous les définirons pour correspondre à la position de la bombe que nous connaissons à partir de l'`état`.
* Le troisième argument est le `rayon`. Ici, nous le définirons à 6.
* Ensuite, les deux derniers arguments sont l'`angleDeDépart` et l'`angleDeFin` de l'arc en radians. Comme ici nous voulons avoir un cercle complet et non un arc, nous commencerons par 0 et terminerons par un cercle complet. Un cercle complet en radians est deux fois Pi.

Si ces deux dernières propriétés sont déroutantes, ne vous en faites pas. Ce qui est important, c'est que lorsque nous dessinons des cercles, ils sont toujours `0` et `2 * Math.PI`.

```js
function drawBomb() {
  ctx.fillStyle = "white";
  ctx.beginPath();
  ctx.arc(state.bomb.x, state.bomb.y, 6, 0, 2 * Math.PI);
  ctx.fill();
}
```

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-19-at-17.08.58-1.png)
_La scène finale avec la bombe en place_

Maintenant, nous avons tout à l'écran. Nous avons dessiné l'arrière-plan, les bâtiments, les gorilles et la bombe. Mais les choses ne sont pas centrées à l'écran. Corrigons cela.

## Comment adapter la taille de la ville à la fenêtre du navigateur

Jusqu'à présent, nous avons aligné tout sur le côté gauche de l'écran. Comme la taille des bâtiments est aléatoire, la taille totale de la ville peut être plus courte ou plus large que la taille de la fenêtre du navigateur. Il pourrait même arriver que nous ne voyions pas le deuxième gorille car il est entièrement hors écran. Ou si la fenêtre du navigateur est trop large, alors nous avons un grand espace sur le côté droit de la fenêtre.

Pour corriger cela, adaptons la taille de la ville à la largeur de la fenêtre du navigateur.

Pour ce faire, ajoutons une propriété `scale` à notre état. Dans la fonction `newGame`, ajoutons la propriété `scale` à l'objet `state`, et appelons une nouvelle fonction nommée `calculateScale` pour définir sa valeur. Cet appel de fonction doit venir après que nous avons généré nos bâtiments car la mise à l'échelle dépend de la taille de la ville. Il doit également venir avant que nous initialisions la position de la bombe, car plus tard cela dépendra de la mise à l'échelle.

```js
function newGame() {
  // Initialiser l'état du jeu
  state = {
    scale: 1,
    phase: "aiming", // aiming | in flight | celebrating
    currentPlayer: 1,
    bomb: {
      x: undefined,
      y: undefined,
      velocity: { x: 0, y: 0 },
    },
    buildings: generateBuildings(),
  };

  calculateScale();

  initializeBombPosition();

  draw();
}
```

La fonction `calculateScale` est relativement simple. Nous calculons la largeur totale de la ville et divisons la largeur intérieure de la fenêtre du navigateur par cette valeur. Cela nous donnera un ratio. Il nous indiquera comment la largeur de notre ville se rapporte à la largeur de la fenêtre du navigateur.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-19-at-17.42.09-1.png)
_Calcul du ratio entre la taille de la ville et la taille de la fenêtre du navigateur_

```js
function calculateScale() {
  const lastBuilding = state.buildings.at(-1);
  const totalWidthOfTheCity = lastBuilding.x + lastBuilding.width;
  
  state.scale = window.innerWidth / totalWidthOfTheCity;
}
```

Ensuite, nous devons utiliser cette nouvelle propriété `scale` à quelques endroits. Le plus important est de changer la mise à l'échelle de tout le jeu dans la fonction `draw`.

Au début de cette fonction – où nous inversons le système de coordonnées – nous avons maintenant un autre appel de méthode `scale` qui applique cette mise à l'échelle. Parce que cela se trouve au début de la fonction `draw`, tout ce que nous dessinons après cela sera mis à l'échelle.

```js
function draw() {
  ctx.save();
  // Inverser le système de coordonnées
  ctx.translate(0, window.innerHeight);
  ctx.scale(1, -1);
  ctx.scale(state.scale, state.scale);

  // Dessiner la scène
  drawBackground();
  drawBuildings();
  drawGorilla(1);
  drawGorilla(2);
  drawBomb();

  // Restaurer la transformation
  ctx.restore();
}
```

Et enfin, nous devons ajuster la façon dont nous dessinons notre arrière-plan. Plus tôt, lorsque nous avons dessiné l'arrière-plan, nous avons rempli tout l'écran en définissant sa largeur et sa hauteur en fonction des propriétés `innerWidth` et `innerHeight` de la fenêtre. Maintenant, comme tout est mis à l'échelle, elles ne correspondent plus à la taille de la fenêtre du navigateur. Chaque fois que nous utilisons ces propriétés, nous devons les ajuster par notre facteur d'échelle.

```js
function drawBackground() {
  ctx.fillStyle = "#58A8D8";
  ctx.fillRect(
    0,
    0,
    window.innerWidth / state.scale,
    window.innerHeight / state.scale
  );
}
```

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-19-at-17.45.05-2.png)
_Adaptation de la taille de la ville à la taille de la fenêtre du navigateur_

### Comment redimensionner la fenêtre

Maintenant, les 8 bâtiments que nous avons dessinés s'adaptent parfaitement à la taille de notre écran – mais que se passe-t-il si nous redimensionnons la fenêtre ? Nous allons avoir les mêmes problèmes que nous avions avant.

En guise de touche finale, gérons l'événement `resize` de la fenêtre. Ce gestionnaire d'événements redimensionne l'élément canvas pour s'adapter à la nouvelle taille de la fenêtre, recalcule la mise à l'échelle, réajuste la position de la bombe et redessine toute la scène en fonction de la nouvelle mise à l'échelle.

Réajuster la position de la bombe ne fait pas encore de différence, mais plus tard nous mettrons à jour cette fonction et elle dépendra de la nouvelle mise à l'échelle.

```js
window.addEventListener("resize", () => {
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
  calculateScale();
  initializeBombPosition();
  draw();
});
```

Jusqu'à présent, nous avons simplement dessiné une scène statique. Il est temps de rendre les choses interactives.

## Comment le gorille peut lancer la bombe

Lancer la bombe comporte deux parties différentes. Tout d'abord, nous devons viser. Nous attrapons la bombe avec la souris et la faisons glisser pour définir l'angle et la vitesse de lancer. Pendant le glisser, nous devons afficher l'angle et la vitesse dans des panneaux d'information en haut de l'écran. Nous peindrons également la trajectoire de lancer à l'écran. C'est la phase de `visée`.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-21-at-16.27.06-4.png)
_La phase de `visée`_

Ensuite, une fois que nous relâchons la souris, la bombe vole à travers le ciel. Nous allons avoir une boucle d'animation qui déplace la bombe à travers le ciel. C'est la phase `en vol`.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-21-at-16.27.09-4.png)
_La phase `en vol`_

Dans cette phase, cette boucle d'animation inclura également la détection des impacts. Nous devons savoir si la bombe a touché un ennemi, ou si nous avons manqué et que la bombe a touché un bâtiment ou est sortie de l'écran. Si nous touchons un bâtiment, ou que la bombe sort de l'écran, nous changeons de joueur et revenons à la phase de `visée`. Si nous touchons l'ennemi, alors nous passons à la phase de `célébration`. Nous dessinons ensuite la variante de célébration du gorille du joueur actuel et nous affichons l'écran de félicitations.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-21-at-16.27.11-4.png)
_La phase de `célébration`_

Maintenant, passons en revue ces parties en détail.

### Comment viser

Dans la phase de `visée`, nous pouvons faire glisser la bombe pour définir son angle et sa vitesse – comme nous lançons un oiseau dans Angry Birds. Nous allons configurer des gestionnaires d'événements pour cela.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screen-Recording-2024-01-21-at-16.52.12--3--1.gif)
_Visée_

Pendant le visée, nous allons montrer l'angle et la vitesse actuels dans le coin supérieur gauche ou supérieur droit de l'écran (selon le joueur). Nous allons également dessiner la trajectoire de lancer à l'écran pour montrer dans quelle direction la bombe volera.

### Panneaux d'information montrant l'angle et la vitesse

Dans le jeu original de 1991, nous devions taper l'angle et la vitesse avec le clavier, car il n'avait pas de support pour la souris. Ici, nous allons viser avec la souris – mais nous ajoutons quand même les mêmes éléments d'interface utilisateur à l'écran. Nous mettrons à jour ces champs pendant que nous déplaçons la souris en faisant glisser.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-21-at-16.02.31-2.png)
_Panneaux d'information dans le coin supérieur gauche et supérieur droit de l'écran_

Nous ajouterons ces panneaux d'information en HTML. Nous pourrions dessiner ces champs de texte sur le canvas également, mais il pourrait être plus facile d'utiliser du bon vieux HTML et CSS.

Nous ajouterons deux divs, une pour le joueur 1 et une pour le joueur 2. Les deux incluent un en-tête avec le numéro du joueur. Nous ajouterons également deux paragraphes pour l'angle et la vitesse. Les panneaux d'information doivent venir après l'élément canvas, sinon le canvas les couvrirait.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>Gorillas</title>
    <link rel="stylesheet" href="index.css" />
    <script src="index.js" defer></script>
  </head>
  <body>
    <canvas id="game"></canvas>
      
    <div id="info-left">
      <h3>Joueur 1</h3>
      <p>Angle : <span class="angle">0</span>°</p>
      <p>Vitesse : <span class="velocity">0</span></p>
    </div>
      
    <div id="info-right">
      <h3>Joueur 2</h3>
      <p>Angle : <span class="angle">0</span>°</p>
      <p>Vitesse : <span class="velocity">0</span></p>
    </div>
  </body>
</html>

```

Nous attribuerons deux IDs différents et des noms de classe appropriés. Nous utiliserons ces noms à la fois pour le style et pour accéder à ces éléments en JavaScript.

Dans le CSS, nous déplacerons ces panneaux en position et définirons un style pour les textes. Nous voulons également nous assurer que l'utilisateur ne peut pas sélectionner le texte à l'écran. Sinon, vous pourriez finir par sélectionner accidentellement ces champs de texte pendant le visée.

```css
body {
  margin: 0;
  padding: 0;
  font-family: monospace;
  font-size: 14px;
  color: white;
  user-select: none;
  -webkit-user-select: none;
}
#info-left {
  position: absolute;
  top: 20px;
  left: 25px;
}
#info-right {
  position: absolute;
  top: 20px;
  right: 25px;
  text-align: right;
}

```

Ensuite, en JavaScript, nous ajouterons quelques références aux champs d'angle et de vitesse quelque part au début de notre fichier.

```js
. . .

// Panneau d'information de gauche
const angle1DOM = document.querySelector("#info-left .angle");
const velocity1DOM = document.querySelector("#info-left .velocity");

// Panneau d'information de droite
const angle2DOM = document.querySelector("#info-right .angle");
const velocity2DOM = document.querySelector("#info-right .velocity");

. . .
```

Lorsque nous ajouterons la gestion des événements, nous mettrons à jour le contenu de ces éléments avec le mouvement de la souris. Pour l'instant, laissons cela tel quel.

### La zone de préhension de la bombe

Nous allons configurer des gestionnaires d'événements pour faire glisser la bombe. Mais que pouvons-nous même faire glisser ? L'élément canvas entier est un seul élément. Nous pourrions y attacher un gestionnaire d'événements, mais alors nous pourrions commencer à faire glisser la bombe en cliquant n'importe où sur l'écran. Nous ne voulons pas cela.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-30-at-17.04.21.png)
_La zone de préhension de la bombe_

Au lieu de cela, nous définissons un autre élément en HTML qui servira de zone de préhension. Nous ajoutons l'élément `bomb-grab-area`. Cela n'inclura pas la bombe que nous voyons à l'écran – celle-ci fait déjà partie du canvas – mais ce sera une zone invisible autour, servant de cible d'événement.

```html
  . . .

  <body>
    <canvas id="game"></canvas>
    
    <div id="info-left">
      <h3>Joueur 1</h3>
      <p>Angle : <span class="angle">0</span>°</p>
      <p>Vitesse : <span class="velocity">0</span></p>
    </div>

    <div id="info-right">
      <h3>Joueur 2</h3>
      <p>Angle : <span class="angle">0</span>°</p>
      <p>Vitesse : <span class="velocity">0</span></p>
    </div>

    <div id="bomb-grab-area"></div>
  </body>

  . . .
```

Nous ajouterons également un peu de style avec CSS. Nous voulons qu'il ait une position absolue et qu'il soit un cercle invisible avec un rayon légèrement plus grand que la bombe (pour qu'il soit plus facile de l'attraper). Nous pouvons définir la position exacte en JavaScript.

Nous changerons également le curseur une fois que la souris est dessus en `grab`. Bien que cet élément soit invisible, vous pouvez toujours remarquer que votre souris est au bon endroit grâce au curseur changeant.

```css
. . .

#bomb-grab-area {
  position: absolute;
  width: 30px;
  height: 30px;
  border-radius: 50%;
  background-color: transparent;
  cursor: grab;
}
```

Ensuite, enfin en JavaScript, nous devons faire deux choses avant de configurer la gestion des événements. Tout d'abord, obtenir une référence quelque part au début du fichier.

```js
. . .

// La zone de préhension de la bombe 
const bombGrabAreaDOM = document.getElementById("bomb-grab-area");

. . .
```

Ensuite, nous devons la déplacer à la position correcte. Nous avons déjà une fonction qui initialise la position de la bombe sur le canvas. Nous pouvons étendre la fonction `initializeBombPosition` pour positionner cet élément HTML également.

Nous déplacerons la zone de préhension au même endroit que la bombe à l'écran, mais ses coordonnées sont un peu différentes. Le contenu du canvas est mis à l'échelle, mais tout autre élément HTML ne l'est pas. Nous devons ajuster les coordonnées en fonction de la mise à l'échelle. Notez également que nous définirons la variable `grabAreaRadius` pour être la moitié de la taille que nous avons définie pour cet élément en CSS.

```js
function initializeBombPosition() {
  const building =
    state.currentPlayer === 1
      ? state.buildings.at(1) // Deuxième bâtiment
      : state.buildings.at(-2); // Avant-dernier bâtiment

  const gorillaX = building.x + building.width / 2;
  const gorillaY = building.height;

  const gorillaHandOffsetX = state.currentPlayer === 1 ? -28 : 28;
  const gorillaHandOffsetY = 107;

  state.bomb.x = gorillaX + gorillaHandOffsetX;
  state.bomb.y = gorillaY + gorillaHandOffsetY;
  state.bomb.velocity.x = 0;
  state.bomb.velocity.y = 0;

  // Initialiser la position de la zone de préhension en HTML
  const grabAreaRadius = 15;
  const left = state.bomb.x * state.scale - grabAreaRadius;
  const bottom = state.bomb.y * state.scale - grabAreaRadius;
  bombGrabAreaDOM.style.left = `${left}px`;
  bombGrabAreaDOM.style.bottom = `${bottom}px`;
}
```

Une fois que nous avons ajouté cela, nous ne verrons aucune différence à l'écran, car cet élément est invisible. Mais une fois que nous survolons la bombe, nous verrons que le curseur change en grab.

### Gestion des événements

Maintenant que tout est configuré, nous pouvons enfin configurer la gestion des événements. Cela va être une implémentation simple de glisser-déposer où nous écoutons les événements `mousedown`, `mousemove` et `mouseup`.

Tout d'abord, nous configurerons quelques variables de niveau supérieur quelque part au début du fichier. Nous avons une variable booléenne qui nous indique si nous faisons glisser actuellement ou non, et deux variables qui nous indiquent où le glisser a commencé, au cas où nous faisons glisser.

```js
. . .

let isDragging = false;
let dragStartX = undefined;
let dragStartY = undefined;

. . .
```

Nous ajoutons le premier gestionnaire d'événements pour l'événement `mousedown` sur la zone de préhension de la bombe. Pouvoir définir ce gestionnaire d'événements est la raison pour laquelle nous avons ajouté l'élément `bomb-grab-area` plus tôt.

Ce gestionnaire d'événements ne fait quelque chose que si nous sommes dans la phase de `visée`. Si c'est vrai, nous définissons la variable `isDragging` sur true, sauvegardons la position actuelle de la souris et définissons le curseur de la souris en permanence sur `grabbing` (pour que le curseur reste en grabbing même si nous quittons la zone de préhension).

```js
bombGrabAreaDOM.addEventListener("mousedown", function (e) {
  if (state.phase === "aiming") {
    isDragging = true;

    dragStartX = e.clientX;
    dragStartY = e.clientY;
    
    document.body.style.cursor = "grabbing";
  }
});
```

Ensuite, nous ajouterons un gestionnaire d'événements pour l'événement `mousemove`. Notez que maintenant la cible de l'événement n'est pas la zone de préhension de la bombe, mais l'objet `window`. Cela est dû au fait que pendant que nous faisons glisser, nous pouvons facilement déplacer la souris en dehors de la zone de préhension – ou même en dehors de la fenêtre du navigateur – et nous voulons toujours que ce gestionnaire d'événements fonctionne.

Ce gestionnaire d'événements vérifie d'abord si nous faisons glisser actuellement. Si ce n'est pas le cas, alors il ne fait rien. Si nous faisons glisser, alors il calcule le delta de la position de la souris depuis l'événement `mousedown` et le définit comme la vitesse de la bombe.

```js
window.addEventListener("mousemove", function (e) {
  if (isDragging) {
    let deltaX = e.clientX - dragStartX;
    let deltaY = e.clientY - dragStartY;

    state.bomb.velocity.x = -deltaX;
    state.bomb.velocity.y = +deltaY;
    setInfo(deltaX, deltaY);

    draw();
  }
});
```

Lorsque nous relâchons la souris, nous voulons que la bombe se déplace dans la direction opposée à celle où nous faisons glisser la souris, donc nous devons définir la vitesse horizontale et verticale avec un signe négatif. Mais avec une double torsion, nous inversons à nouveau la vitesse verticale (la coordonnée Y), pour avoir un signe positif car nous avons inversé le système de coordonnées.

Les gestionnaires d'événements supposent toujours que le système de coordonnées grandit vers le bas. À l'intérieur du canvas, il va dans la direction opposée.

Ce gestionnaire d'événements appelle également une fonction utilitaire pour afficher l'angle et la vitesse dans les panneaux d'information que nous venons d'ajouter en HTML. Ensuite, nous appelons à nouveau la fonction `draw`. Pour l'instant, appeler la fonction `draw` ici ne change rien à l'écran, mais bientôt nous mettrons à jour la fonction `drawBomb` pour dessiner la trajectoire de lancer.

Le bouton `setInfo` met à jour les éléments d'interface utilisateur que nous avons définis en HTML. Nous avons déjà des références à ces éléments en haut de notre fichier, donc ici nous devons simplement mettre à jour leur contenu lorsque nous faisons glisser la bombe.

```js
. . .

// Panneau d'information de gauche
const angle1DOM = document.querySelector("#info-left .angle");
const velocity1DOM = document.querySelector("#info-left .velocity");

// Panneau d'information de droite
const angle2DOM = document.querySelector("#info-right .angle");
const velocity2DOM = document.querySelector("#info-right .velocity");

. . .
```

Mais il y a une complication. À partir de l'événement `mousemove`, nous avons obtenu les composantes verticales et horizontales de la vitesse. Mais sur l'interface utilisateur, nous voulons afficher l'angle et la vitesse totale du lancer. Nous devons utiliser un peu de trigonométrie pour calculer ces valeurs.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-19-at-20.56.06-1.png)
_Calcul de la vitesse totale et de l'angle à partir du mouvement horizontal et vertical de la souris_

Pour la vitesse, nous calculerons l'`hypoténuse` d'un triangle imaginaire composé des composantes horizontales et verticales de la vitesse. Pour l'`angle`, nous utiliserons la fonction arc sinus (l'inverse de la fonction sinus). Nous veillerons également à mettre à jour le bon panneau d'information en fonction du joueur dont c'est le tour, et nous arrondirons les valeurs.

```js
function setInfo(deltaX, deltaY) {
  const hypotenuse = Math.sqrt(deltaX ** 2 + deltaY ** 2);
  const angleInRadians = Math.asin(deltaY / hypotenuse);
  const angleInDegrees = (angleInRadians / Math.PI) * 180;
  
  if (state.currentPlayer === 1) {
    angle1DOM.innerText = Math.round(angleInDegrees);
    velocity1DOM.innerText = Math.round(hypotenuse);
  } else {
    angle2DOM.innerText = Math.round(angleInDegrees);
    velocity2DOM.innerText = Math.round(hypotenuse);
  }
}
```

À ce stade, alors que la scène devrait rester la même, les valeurs dans le panneau d'information de gauche devraient se mettre à jour lorsque nous faisons glisser.

Enfin, nous ajouterons le gestionnaire d'événements pour l'événement `mouseup`, à nouveau sur l'objet `window`. Il ne fait quelque chose que si nous faisons glisser actuellement. Ensuite, il note que nous ne faisons plus glisser, change le curseur en mode par défaut et appelle la fonction `throwBomb`.

```js
window.addEventListener("mouseup", function () {
  if (isDragging) {
    isDragging = false;

    document.body.style.cursor = "default";
    
    throwBomb();
  }
});
```

La fonction `throwBomb` passe le jeu en phase `in flight` et lance l'animation de la bombe. Nous allons couvrir cette fonction dans le prochain chapitre, mais avant d'y arriver, mettons à jour une dernière chose.

### Comment dessiner la trajectoire de lancer

Pendant que nous visons, nous pouvons également dessiner la trajectoire de lancer. La trajectoire de lancer est la forme visualisée de la vitesse et de l'angle.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-21-at-16.27.06-5.png)
_La trajectoire de lancer montre l'angle et la vitesse sous une forme visuelle_

Pour ce faire, retournons à la fonction `drawBomb` et apportons quelques modifications. Si nous sommes dans la phase de `visée`, nous dessinerons une ligne droite du centre de la bombe à la vitesse.

```js
function drawBomb() {
  // Dessiner la trajectoire de lancer
  if (state.phase === "aiming") {
    ctx.strokeStyle = "rgba(255, 255, 255, 0.7)";
    ctx.setLineDash([3, 8]);
    ctx.lineWidth = 3;
    
    ctx.beginPath();
    ctx.moveTo(state.bomb.x, state.bomb.y);
    ctx.lineTo(
      state.bomb.x + state.bomb.velocity.x,
      state.bomb.y + state.bomb.velocity.y
    );
    ctx.stroke();
  }

  // Dessiner le cercle
  ctx.fillStyle = "white";
  ctx.beginPath();
  ctx.arc(state.bomb.x, state.bomb.y, 6, 0, 2 * Math.PI);
  ctx.fill();
}
```

Nous dessinerons cette ligne comme un chemin, comme nous l'avons fait auparavant. Nous la commencerons avec la méthode `beginPath` et la terminerons avec la méthode `stroke`. Entre les deux, nous utiliserons les méthodes `moveTo` et `lineTo`.

Il y a une nouvelle chose ici : la méthode `setLineDash`. Avec ce paramètre, nous pouvons dessiner une ligne pointillée. Nous définirons cela après chaque segment de ligne de 3 pixels, et nous voulons avoir un espace de 8 pixels. Le trait de 3 pixels correspond à la `lineWidth`, donc les traits ressembleront à des points.

Maintenant, nous avons terminé tout ce qui concerne la phase de `visée`. Il est temps de lancer la bombe.

## Comment animer la bombe entrante

Une fois que nous relâchons la souris après le visée, la bombe vole à travers le ciel. Nous ajouterons une boucle d'animation qui déplace la bombe, calcule sa position à chaque cycle d'animation et vérifie si nous avons touché quelque chose.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screen-Recording-2024-01-21-at-17.06.18-1.gif)
_Animer la bombe_

Auparavant, nous avons vu que le gestionnaire d'événements de l'événement `mouseup` se termine par l'appel de la fonction `throwBomb`. Implémentons cette fonction.

Cette fonction lance d'abord la phase `in flight`. Ensuite, elle réinitialise la variable `previousAnimationTimestamp`. Il s'agit d'une nouvelle variable utilitaire nécessaire pour la boucle d'animation. Nous allons la couvrir dans un instant. Ensuite, nous démarrons la boucle d'animation, en appelant `requestAnimationFrame` avec la fonction `animate` comme argument. Approfondissons cette fonction d'animation.

```js
. . . 

let previousAnimationTimestamp = undefined; 

. . .

function throwBomb() {
  state.phase = "in flight";
  previousAnimationTimestamp = undefined;
  requestAnimationFrame(animate);
}
```

### La boucle d'animation

La fonction `animate` déplace la bombe et appelle la fonction `draw` pour repeindre l'écran encore et encore jusqu'à ce que nous touchions l'ennemi, un bâtiment, ou que la bombe sorte de l'écran.

En appelant cette fonction avec `requestAnimationFrame` de la manière que vous voyez ci-dessous, la fonction d'animation s'exécutera environ 60 fois par seconde. Le repeint constant de l'écran apparaîtra comme une animation continue. Comme cette fonction s'exécute si fréquemment, nous ne déplaçons la bombe que peu à peu à chaque fois.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Gorillas-Keynote.006.png)
_La boucle d'animation_

Cette fonction garde une trace du temps écoulé depuis son dernier appel. Nous allons utiliser cette information pour calculer précisément de combien nous devons déplacer la bombe.

Les fonctions invoquées avec la fonction `requestAnimationFrame` reçoivent le `timestamp` actuel comme attribut. À la fin de chaque cycle, nous sauvegardons cette valeur de `timestamp` dans la variable `previousAnimationTimestamp`, afin que dans le cycle suivant nous puissions calculer combien de temps s'est écoulé entre deux cycles. Dans le code ci-dessous, il s'agit de la variable `elapsedTime`.

Le premier cycle est une exception car, à ce moment-là, nous n'avions pas encore de cycle précédent. Au début de chaque lancer, la valeur de `previousAnimationTimestamp` est `undefined` (nous nous assurons qu'elle est `undefined` dans la fonction `throwBomb`). Dans ce cas, nous sautons un rendu et nous ne rendrons la scène que dans le deuxième cycle, où nous avons déjà toutes les valeurs dont nous avons besoin. Il s'agit de la partie tout au début de la fonction `animate`.

```js
function animate(timestamp) {
  if (previousAnimationTimestamp === undefined) {
    previousAnimationTimestamp = timestamp;
    requestAnimationFrame(animate);
    return;
  }
  const elapsedTime = timestamp - previousAnimationTimestamp;

  moveBomb(elapsedTime); 
  
  // Détection des impacts
  let miss = false; // La bombe a touché un bâtiment ou est sortie de l'écran
  let hit = false; // La bombe a touché l'ennemi

  // Gérer le cas où nous touchons un bâtiment ou la bombe sort de l'écran
  if (miss) {
    // ...
    return;
  } // Gérer le cas où nous touchons l'ennemi
  if (hit) {
    // ... 
    return;
  }

  draw();
  
  // Continuer la boucle d'animation
  previousAnimationTimestamp = timestamp;
  requestAnimationFrame(animate);
}
```

À l'intérieur de la fonction, nous allons déplacer la bombe à chaque cycle en appelant la fonction `moveBomb`. Nous passerons la variable `elapsedTime` afin qu'elle puisse calculer précisément de combien elle doit déplacer la bombe.

À chaque cycle, nous détectons également si nous avons touché un ennemi, ou si nous avons manqué et que la bombe a touché un bâtiment ou est sortie de l'écran. Si rien de tout cela ne se produit, alors nous devons repeindre la scène et demander une autre image d'animation pour continuer la boucle d'animation. Mais si nous avons manqué l'ennemi ou obtenu un impact, alors nous arrêterons la boucle d'animation en retournant de la fonction. En retournant tôt de la fonction, nous n'atteignons jamais la dernière ligne, qui déclencherait le cycle d'animation suivant. La boucle s'arrête.

### Comment déplacer la bombe

Nous déplaçons la bombe en appelant la fonction `moveBomb` dans la boucle d'animation. Cette fonction calcule les nouvelles positions `x` et `y` de la bombe à chaque cycle.

Les nouvelles valeurs `x` et `y` sont calculées en fonction de la vitesse. Mais la vitesse verticale et horizontale peut être un nombre relativement élevé.

Nous ne voulons pas que la bombe traverse l'écran à la vitesse de l'éclair, donc pour ralentir le mouvement, nous multiplierons les valeurs par un nombre très petit. Ce `multiplicateur` prend également en compte le temps écoulé, afin que l'animation semble cohérente même si les cycles d'animation ne sont pas déclenchés à intervalles égaux.

À chaque cycle, la vitesse de la bombe est également ajustée par la gravité. Nous augmenterons progressivement le mouvement de la bombe vers le sol. Nous ajusterons également la vitesse verticale par une petite constante qui dépend également du temps écoulé.

```js
function moveBomb(elapsedTime) {
  const multiplier = elapsedTime / 200; // Ajuster la trajectoire par la gravité

  state.bomb.velocity.y -= 20 * multiplier; // Calculer la nouvelle position
  
  state.bomb.x += state.bomb.velocity.x * multiplier;
  state.bomb.y += state.bomb.velocity.y * multiplier;
}
```

### Détection des impacts

Notre boucle d'animation continue de déplacer la bombe à l'infini. Mais une fois que nous touchons un bâtiment, l'ennemi, ou que la bombe sort de l'écran, nous devrions arrêter ce mouvement.

Nous devons détecter ces cas et les gérer de manière appropriée. Si la bombe sort de l'écran ou si nous touchons un bâtiment, nous devrions passer au joueur suivant et revenir à la phase de `visée`. Dans le cas où nous touchons l'ennemi, nous devrions passer à la phase de `célébration` et annoncer le gagnant.

Dans tous ces cas, nous pouvons arrêter la boucle en retournant tôt de la fonction `animate`. Dans ces cas, la fonction d'animation n'atteint pas sa dernière ligne qui déclencherait un autre cycle d'animation.

### Comment améliorer la précision de la détection des impacts

Bien que nous ayons déjà ralenti le mouvement de la bombe pour avoir une belle animation à l'écran, la bombe peut encore être un peu trop rapide pour la détection des impacts.

Lorsque la bombe est en vol, elle peut se déplacer de plus de 10 pixels à la fois. Si nous faisons des détections d'impact seulement une fois par cycle d'animation, alors nous sommes complètement aveugles à ce qui se passe pendant ces mouvements de 10 pixels. La bombe peut facilement traverser des parties du gorille sans que nous remarquions que nous aurions dû avoir un impact, ou traverser le coin d'un bâtiment sans aucun impact.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-19-at-23.19.47-1.png)
_Nous devons diviser chaque cycle d'animation en plusieurs segments pour améliorer la détection des impacts_

Pour résoudre ce problème, nous ne ferons pas seulement une détection d'impact une fois par cycle d'animation, mais plusieurs fois. Nous diviserons chaque mouvement en segments plus petits, et à chaque petit mouvement, nous devons vérifier si nous avons un impact.

Nous rendrons toujours la scène une fois par cycle d'animation, mais avant d'appeler la fonction `draw`, nous diviserons le mouvement en 10 segments avec une boucle.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-30-at-17.10.02.png)
_Diviser le mouvement et la détection des impacts en 10 segments à chaque cycle d'animation_

Si nous divisons chaque cycle d'animation en dix segments, cela signifie également que nous appelons maintenant la fonction `moveBomb` dix fois de plus. Nous devons la ralentir encore plus. Comme cette fonction déplace la bombe en fonction du temps écoulé, il suffit de diviser son attribut de temps également par dix.

De cette façon, la bombe se déplace dans le ciel à la même vitesse, mais nous avons dix fois plus de précision avec la détection des impacts. Dans l'exemple ci-dessous, nous enveloppons l'appel de la fonction `moveBomb` et la logique de détection des impacts dans une boucle for.

```js
function animate(timestamp) {
  if (!previousAnimationTimestamp) {
    previousAnimationTimestamp = timestamp;
    requestAnimationFrame(animate);
    return;
  }

  const elapsedTime = timestamp - previousAnimationTimestamp;

  const hitDetectionPrecision = 10;
  for (let i = 0; i < hitDetectionPrecision; i++) {
    moveBomb(elapsedTime / hitDetectionPrecision);

    // Détection des impacts
    const miss = checkFrameHit() || checkBuildingHit();
    const hit = checkGorillaHit();

    // Gérer le cas où nous touchons un bâtiment ou la bombe sort de l'écran
    if (miss) {
      // ...
      return;
    }

    // Gérer le cas où nous touchons l'ennemi
    if (hit) {
      // ...
      return;
    }
  }

  draw();
  
  // Continuer la boucle d'animation
  previousAnimationTimestamp = timestamp;
  requestAnimationFrame(animate);
}
```

Dans l'exemple ci-dessus, nous avons également introduit quelques fonctions utilitaires pour la détection des impacts. Dans les prochaines étapes, implémentons ces fonctions.

```js
function checkFrameHit() {
  // ...
}

function checkBuildingHit() {
  // ...
}

function checkGorillaHit() {
  // ...
}
```

### Comment détecter si la bombe est hors de l'écran

Nous avons manqué la cible si nous atteignons le bord de l'écran ou si nous touchons un bâtiment. Vérifier si nous avons atteint le bord de l'écran est très facile à faire.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-30-at-17.07.56.png)
_Vérification si la bombe est sortie de l'écran_

Nous devons seulement vérifier si la bombe est sortie sur le côté gauche, le bas ou le côté droit de l'écran. Si la bombe traverse le haut de l'écran, ce n'est pas grave. La gravité la ramènera éventuellement.

Notez que, en raison de la mise à l'échelle, le côté droit de l'écran n'est pas le même que la valeur `innerWidth` de la fenêtre. Nous devons ajuster cela par le facteur de mise à l'échelle.

```js
function checkFrameHit() {
  if (
    state.bomb.y < 0 ||
    state.bomb.x < 0 ||
    state.bomb.x > window.innerWidth / state.scale
  ) {
    return true; // La bombe est hors de l'écran
  }
}
```

Si la bombe est sortie de l'écran, nous retournons `true` pour signaler à la fonction `animate` que nous pouvons arrêter la boucle d'animation.

### Comment détecter si la bombe a touché un bâtiment

Nous manquons également la cible si la bombe touche un bâtiment. Nous pouvons itérer sur le tableau des bâtiments et vérifier si un côté de la bombe est à l'intérieur du rectangle du bâtiment. Nous devons vérifier que :

* Le côté droit de la bombe est à droite du côté gauche du bâtiment,
* Le côté gauche de la bombe est à gauche du côté droit du bâtiment,
* Et que le bas de la bombe est en dessous du haut du bâtiment.

![Image](https://www.freecodecamp.org/news/content/images/2024/08/detecting-bomb-building.jpg)
_Détection si la bombe a touché un bâtiment_

```js
function checkBuildingHit() {
  for (let i = 0; i < state.buildings.length; i++) {
    const building = state.buildings[i];
    if (
      state.bomb.x + 4 > building.x &&
      state.bomb.x - 4 < building.x + building.width &&
      state.bomb.y - 4 < 0 + building.height
    ) {
      return true; // Bâtiment touché
    }
  }
}
```

Si tout cela est vrai, alors nous savons que la bombe a touché le bâtiment. Si nous obtenons un impact, la fonction se termine en retournant true. Cela signalera également à la fonction `animate` que nous pouvons arrêter la boucle d'animation.

### Comment détecter si la bombe a touché l'ennemi

Maintenant que nous pouvons détecter si la bombe est sortie de l'écran et que nous avons une détection d'impact pour les bâtiments, il est temps de détecter si nous avons touché l'ennemi.

Nous allons avoir une approche différente cette fois-ci. Détecter si nous avons obtenu un impact avec des calculs géométriques traditionnels serait beaucoup plus compliqué, car les gorilles ne sont pas construits avec des rectangles et des cercles de base.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-19-at-23.49.34-1.png)
_Capture d'écran du jeu une fois que nous avons touché l'ennemi_

Au lieu de cela, nous pouvons utiliser la méthode `isPointInPath` qui nous indique commodément si un point – dans ce cas, le centre de la bombe – est à l'intérieur d'un chemin.

Cette méthode nous indique si un point est à l'intérieur du chemin actuel ou précédent. Donc avant d'appeler la méthode, nous devons recréer le gorille. Le gorille n'est pas seulement un seul chemin, donc nous devons tester contre le chemin le plus pertinent, le corps principal du gorille.

De manière pratique – et avec une certaine planification intelligente – nous avons déjà une fonction qui peint le corps du gorille comme un seul chemin. Nous appelons la fonction `drawGorillaBody` juste avant `isPointInPath`. Mais la fonction `drawGorillaBody` peint avec des coordonnées relatives au toit d'un bâtiment, donc avant de l'appeler, nous devons translater le système de coordonnées.

En fonction du joueur actuel, nous calculerons sur quel bâtiment l'ennemi se tient, et nous translaterons le système de coordonnées vers le haut de celui-ci. En raison de cette translation, nous utilisons également les méthodes `save` et `restore`.

```js
function checkGorillaHit() {
  const enemyPlayer = state.currentPlayer === 1 ? 2 : 1;
  const enemyBuilding =
    enemyPlayer === 1
      ? state.buildings.at(1) // Deuxième bâtiment
      : state.buildings.at(-2); // Avant-dernier bâtiment

  ctx.save();

  ctx.translate(
    enemyBuilding.x + enemyBuilding.width / 2,
    enemyBuilding.height
  );

  drawGorillaBody();
  let hit = ctx.isPointInPath(state.bomb.x, state.bomb.y);

  drawGorillaLeftArm(enemyPlayer);
  hit ||= ctx.isPointInStroke(state.bomb.x, state.bomb.y);

  drawGorillaRightArm(enemyPlayer);
  hit ||= ctx.isPointInStroke(state.bomb.x, state.bomb.y);

  ctx.restore();
  
  return hit;
}
```

De même, nous pouvons également détecter si nous avons touché l'un des bras du gorille. Les bras sont dessinés comme un trait, donc dans ce cas, au lieu de `isPointInPath`, nous utiliserons la méthode `isPointInStroke`. Cette détection n'aurait pas fonctionné si nous n'avions pas augmenté la précision de la détection des impacts plus tôt, car la bombe pouvait facilement sauter par-dessus le bras.

Avec cette fonction, nous avons toutes les pièces de la détection des impacts. La boucle d'animation s'arrête si nous touchons un bâtiment, l'ennemi, ou si la bombe sort de l'écran. Il est temps de gérer ce qui se passe ensuite dans ces cas.

### Comment gérer le résultat de la détection des impacts

Une fois que nous avons une détection des impacts appropriée, il est temps de gérer enfin les cas où nous touchons un bâtiment, l'ennemi, ou la bombe sort de l'écran. Nous mettrons à jour la fonction `animate` une dernière fois. La seule nouveauté ci-dessous est le bloc de code des deux instructions `if` à l'intérieur de la boucle.

Si nous touchons le bord de l'écran ou un bâtiment, cela signifie que nous avons manqué la cible. Dans ce cas, nous changerons de joueur et reviendrons à la phase de `visée`. Nous réinitialiserons également la position de la bombe pour la déplacer vers la main du nouveau joueur.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-20-at-00.39.59-1.png)
_Une fois que nous avons manqué l'ennemi, nous changeons de joueur_

Ensuite, nous appellerons simplement la fonction `draw` pour gérer le reste. La beauté de cette structure est que nous devons seulement changer l'état du jeu et la fonction `draw` peut repeindre toute la scène en conséquence.

Ensuite, nous `retournerons` de la fonction d'animation pour arrêter la boucle d'animation. Les gestionnaires d'événements sont à nouveau actifs (parce que nous sommes de retour dans la phase de `visée`), et le joueur suivant peut tirer.

```js
function animate(timestamp) {
  if (!previousAnimationTimestamp) {
    previousAnimationTimestamp = timestamp;
    requestAnimationFrame(animate);
    return;
  }
  
  const elapsedTime = timestamp - previousAnimationTimestamp;

  const hitDetectionPrecision = 10;
  for (let i = 0; i < hitDetectionPrecision; i++) {
    moveBomb(elapsedTime / hitDetectionPrecision); // Détection des impacts

    const miss = checkFrameHit() || checkBuildingHit();
    const hit = checkGorillaHit();

    // Gérer le cas où nous touchons un bâtiment ou la bombe sort de l'écran
    if (miss) {
      state.currentPlayer = state.currentPlayer === 1 ? 2 : 1; // Changer de joueur
      state.phase = "aiming";
      initializeBombPosition();
      draw();
      return;
    }

    // Gérer le cas où nous touchons l'ennemi
    if (hit) {
      state.phase = "celebrating";
      announceWinner();
      draw();
      return;
    }
  }

  draw();

  // Continuer la boucle d'animation
  previousAnimationTimestamp = timestamp;
  requestAnimationFrame(animate);
}
```

Si nous touchons l'ennemi, nous devons passer à la phase de `célébration`. Nous annoncerons le gagnant avec une fonction que nous allons couvrir dans la section suivante. Ensuite, nous repeignons la scène avec un gorille célébrant et nous retournons pour arrêter la boucle d'animation.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-19-at-23.49.34-2.png)
_Une fois que nous touchons l'ennemi, la fonction `draw` repeint la scène avec un gorille célébrant_

Pour nous assurer que notre code ne génère pas d'erreur, ajoutons un espace réservé pour la fonction `announceWinner`.

```js
function announceWinner() { 
    // ... 
} 
```

### Comment annoncer le gagnant

Une fois que nous avons touché l'ennemi, nous devons annoncer le gagnant. Pour cela, nous ajouterons un autre panneau d'information en HTML qui inclut qui a gagné le jeu et un bouton de redémarrage. Au bas du fichier HTML maintenant terminé, vous pouvez trouver le panneau de `félicitations`.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-21-at-16.27.11-6.png)
_Le panneau de `félicitations` annonçant le gagnant_

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>Gorillas</title>
    <link rel="stylesheet" href="index.css" />
    <script src="index.js" defer></script>
  </head>
  <body>
    <canvas id="game"></canvas>

    <div id="info-left">
      <h3>Joueur 1</h3>
      <p>Angle : <span class="angle">0</span>°</p>
      <p>Vitesse : <span class="velocity">0</span></p>
    </div>

    <div id="info-right">
      <h3>Joueur 2</h3>
      <p>Angle : <span class="angle">0</span>°</p>
      <p>Vitesse : <span class="velocity">0</span></p>
    </div>

    <div id="bomb-grab-area"></div>

    <div id="congratulations">
      <h1><span id="winner">?</span> a gagné !</h1>
      <button id="new-game">Nouvelle Partie</button>
    </div>
  </body>
</html>
```

Ce panneau est masqué par défaut et il n'apparaît qu'à la fin du jeu. Lorsqu'il apparaît, il doit être au milieu de l'écran. Nous mettrons à jour notre fichier CSS en conséquence.

Notez que nous avons ajouté `display: flex` à l'élément body avec quelques propriétés supplémentaires pour centrer tout sur l'écran. Ensuite, nous avons défini `position: absolute` pour l'élément `congratulations` et l'avons masqué par défaut.

```css
body {
  margin: 0;
  padding: 0;
  font-family: monospace;
  font-size: 14px;
  color: white;
  user-select: none;
  -webkit-user-select: none;
  display: flex;
  justify-content: center;
  align-items: center;
}

#info-left {
  position: absolute;
  top: 20px;
  left: 25px;
}

#info-right {
  position: absolute;
  top: 20px;
  right: 25px;
  text-align: right;
}

#bomb-grab-area {
  position: absolute;
  width: 30px;
  height: 30px;
  border-radius: 50%;
  background-color: transparent;
  cursor: grab;
}

#congratulations {
  position: absolute;
  visibility: hidden;
}

```

Ensuite, enfin, nous pouvons utiliser ce panneau pour annoncer le gagnant une fois que le jeu se termine en JavaScript. Nous appelons déjà la fonction `announceWinner` dans notre fonction `animate`, il est donc temps de l'implémenter.

Tout d'abord, quelque part au début du fichier, nous configurerons quelques références pour le panneau de `félicitations` lui-même et le champ `winner`.

```js
. . .

// Panneau de félicitations
const congratulationsDOM = document.getElementById("congratulations");
const winnerDOM = document.getElementById("winner");

. . .
```

Ensuite, dans la fonction `announceWinner`, nous définirons le contenu du champ du gagnant pour indiquer le joueur actuel et afficher le panneau de félicitations.

```js
function announceWinner() {
  winnerDOM.innerText = `Joueur ${state.currentPlayer}`;
  congratulationsDOM.style.visibility = "visible";
}
```

Avec cette pièce, nous pouvons enfin jouer au jeu jusqu'à la fin. Nous pouvons viser, la bombe vole à travers le ciel, et les gorilles jouent à tour de rôle jusqu'à ce que l'un d'eux gagne le jeu. La seule pièce manquante est la réinitialisation du jeu pour une autre manche.

### Comment réinitialiser pour une autre manche

En guise de touche finale, ajoutons un gestionnaire d'événements pour le bouton 'Nouvelle Partie' sur notre panneau de félicitations afin de pouvoir réinitialiser le jeu. Nous avons déjà ajouté un bouton avec l'ID `new-game` dans notre HTML.

En JavaScript, nous créerons d'abord une référence à ce bouton, puis nous ajouterons un gestionnaire d'événements pour celui-ci. Ce gestionnaire d'événements appelle simplement la fonction `newGame`.

```js
. . .

// Panneau de félicitations
const congratulationsDOM = document.getElementById("congratulations");
const winnerDOM = document.getElementById("winner");
const newGameButtonDOM = document.getElementById("new-game");

. . .

newGameButtonDOM.addEventListener("click", newGame);
```

La fonction `newGame` doit tout réinitialiser et générer un nouveau niveau afin que nous puissions commencer une nouvelle partie. À ce stade, cependant, notre fonction `newGame` ne réinitialise pas tout. Elle ne réinitialise pas les éléments HTML que nous avons introduits entre-temps.

En toute dernière étape, nous nous assurerons que l'élément `congratulations` est masqué une fois que nous commençons une nouvelle partie, et nous réinitialiserons les valeurs d'angle et de vitesse dans les panneaux d'information gauche et droit à 0.

```js
function newGame() {
  // Initialiser l'état du jeu
  state = {
    scale: 1,
    phase: "aiming", // aiming | in flight | celebrating
    currentPlayer: 1,
    bomb: {
      x: undefined,
      y: undefined,
      velocity: { x: 0, y: 0 },
    },
    buildings: generateBuildings(),
  };

  calculateScale();

  initializeBombPosition();

  // Réinitialiser les éléments HTML
  congratulationsDOM.style.visibility = "hidden";
  angle1DOM.innerText = 0;
  velocity1DOM.innerText = 0;
  angle2DOM.innerText = 0;
  velocity2DOM.innerText = 0;
  
  draw();
}
```

## Prochaines étapes

Bien que nous ayons maintenant un jeu complet à deux joueurs, nous pouvons faire beaucoup plus. Sur [YouTube](https://youtu.be/2q5EufbUEQk?si=9IlOu7Ds-UeeNbIh) je couvre également comment rendre les bâtiments destructibles, comment animer la main du gorille pour suivre le mouvement de glisser pendant le visée, et nous passons plus de temps à ajouter des graphismes détaillés. Il y a aussi un chapitre entier sur comment ajouter une logique informatique au jeu, afin que vous puissiez jouer contre l'ordinateur.

Consultez-le pour en savoir plus :

%[https://youtu.be/2q5EufbUEQk?si=9IlOu7Ds-UeeNbIh]

### Abonnez-vous à ma chaîne pour plus de tutoriels de développement de jeux JavaScript :

%[https://www.youtube.com/channel/UCxhgW0Q5XLvIoXHAfQXg9oQ]