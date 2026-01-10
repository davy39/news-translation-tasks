---
title: Comment créer un jeu de Snake avec Phaser.js
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2025-08-29T15:37:36.593Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-snake-game-using-phaserjs
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1756416799827/d337175f-cbf1-40d1-8228-e5f3933ba3d1.png
tags:
- name: JavaScript
  slug: javascript
- name: Game Development
  slug: game-development
seo_title: Comment créer un jeu de Snake avec Phaser.js
seo_desc: 'If you’ve ever wanted to make a small game that runs in the browser, Phaser.js
  is a great place to start. It’s a simple JavaScript library that helps you build
  interactive 2-D games that you can play in the browser.

  In this guide, you’ll learn what P...'
---

Si vous avez toujours voulu créer un petit jeu qui s'exécute dans le navigateur, Phaser.js est un excellent point de départ. C'est une bibliothèque JavaScript simple qui vous aide à créer des jeux interactifs en 2D jouables dans le navigateur.

Dans ce guide, vous apprendrez ce qu'est Phaser, puis vous l'utiliserez pour construire le célèbre jeu Snake. Le serpent se déplace sur une grille. Il mange de la nourriture pour grandir. Il meurt s'il frappe un mur ou lui-même. Le projet complet tient dans deux fichiers, et le code est divisé en petits blocs pour être facile à suivre.

À la fin, vous serez en mesure de comprendre et de copier le code, de l'exécuter et de le modifier. Vous apprendrez également pourquoi chaque partie existe et comment elle s'intègre dans la méthodologie de Phaser.

[Jouez au jeu](https://manishshivanandhan.com/snake-game-with-phaser/) ici pour vous faire une idée de ce que vous allez construire.

## Table des matières

* [Qu'est-ce que Phaser.js ?](#heading-quest-ce-que-phaserjs)
    
* [Configuration du projet](#heading-configuration-du-projet)
    
* [Grille, couleurs et configuration du jeu](#heading-grille-couleurs-et-configuration-du-jeu)
    
* [État de la scène et fonctions utilitaires](#heading-etat-de-la-scene-et-fonctions-utilitaires)
    
* [Preload et Create](#heading-preload-et-create)
    
* [Initialisation du jeu](#heading-initialisation-du-jeu)
    
* [Lecture des entrées à chaque frame](#heading-lecture-des-entrees-a-chaque-frame)
    
* [Déplacement du serpent, manger et dessin](#heading-deplacement-du-serpent-manger-et-dessin)
    
* [Apparition de la nourriture et augmentation de la vitesse](#heading-apparition-de-la-nourriture-et-augmentation-de-la-vitesse)
    
* [Game Over et redémarrage](#heading-game-over-et-redemarrage)
    
* [Comment tout s'articule](#heading-comment-tout-sarticule)
    
* [Prochaines étapes utiles](#heading-prochaines-etapes-utiles)
    
* [Dernières réflexions](#heading-dernieres-reflexions)
    

## Qu'est-ce que Phaser.js ?

[Phaser](https://phaser.io/) est une bibliothèque JavaScript gratuite pour les jeux 2D. Vous écrivez du JavaScript pur et laissez Phaser faire le plus dur. Vous n'avez pas besoin d'un système de build ou d'un installateur de moteur de jeu. Vous pouvez commencer avec un seul fichier HTML et un seul fichier JavaScript.

Phaser organise le code en scènes. Une scène comporte trois étapes communes. Vous chargez les ressources dans `preload`, vous configurez les images et les variables dans `create`, et vous mettez à jour votre jeu à chaque image dans `update`. Cette petite boucle est le cœur de la plupart des jeux d'arcade.

Configurons maintenant le projet.

## Configuration du projet

Créez un dossier avec deux fichiers nommés `index.html` et `main.js`. La page HTML charge Phaser depuis un CDN puis charge votre script.

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="fr">
  <head>
    <meta charset="UTF-8" />
    <title>Phaser Snake</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <style>body { margin: 0; background: #111; }</style>
  </head>
  <body>
    <div id="game"></div>
    <script src="https://cdn.jsdelivr.net/npm/phaser@3/dist/phaser.min.js"></script>
    <script src="main.js"></script>
  </body>
</html>
```

Cette page ajoute un div conteneur et inclut Phaser 3 via jsDelivr. Votre fichier `main.js` créera le jeu et l'attachera à ce div.

## Grille, couleurs et configuration du jeu

Le Snake est plus facile à gérer sur une grille. Vous choisissez une taille de tuile et un nombre de tuiles en largeur et en hauteur. Vous définissez également les couleurs pour l'arrière-plan, le serpent et la nourriture. Ensuite, vous créez une configuration de jeu Phaser qui pointe vers vos fonctions de scène.

```js
// main.js (partie 1)

// Taille d'une tuile de la grille en pixels
const TILE = 16;

// Nombre de tuiles horizontalement (colonnes) et verticalement (lignes)
// Zone de jeu = 40 * 16px de large (640px) et 30 * 16px de haut (480px)
const COLS = 40;                 
const ROWS = 30;                 

// Largeur et hauteur totales en pixels du canvas de jeu
const WIDTH = COLS * TILE;
const HEIGHT = ROWS * TILE;

// Couleurs pour l'arrière-plan, la tête du serpent, le corps et la nourriture
const COLORS = {
  bg: 0x1d1d1d,   // arrière-plan gris foncé
  head: 0x30c452, // tête vert clair
  body: 0x2aa04a, // corps vert plus foncé
  food: 0xe94f37, // nourriture rouge
};

// Directions représentées par des décalages x et y sur la grille
// Par exemple, aller à gauche signifie que x diminue de 1, y reste identique
const DIR = {
  left:  { x: -1, y:  0, name: 'left'  },
  right: { x:  1, y:  0, name: 'right' },
  up:    { x:  0, y: -1, name: 'up'    },
  down:  { x:  0, y:  1, name: 'down'  },
};

// Configuration du jeu Phaser
// - type : Phaser utilisera WebGL si possible, sinon Canvas
// - parent : attacher le canvas de jeu au <div id="game">
// - width/height : définit la taille du canvas
// - backgroundColor : arrière-plan sombre depuis COLORS
// - scene : définit les fonctions qui s'exécutent pendant preload, create et update
const config = {
  type: Phaser.AUTO,
  parent: 'game',
  width: WIDTH,
  height: HEIGHT,
  backgroundColor: COLORS.bg,
  scene: { preload, create, update }
};

// Création d'un nouveau jeu Phaser avec la config
new Phaser.Game(config);
```

La `config` indique à Phaser de créer un canvas, de définir sa taille et d'utiliser vos fonctions de scène. `Phaser.AUTO` sélectionne WebGL si possible et se replie sur Canvas sinon.

## État de la scène et fonctions utilitaires

Vous devez stocker le corps du serpent sous forme de cellules de grille, les rectangles qui dessinent ces cellules, la direction du déplacement, l'entrée en file d'attente, la cellule de nourriture, le score et le minuteur de mouvement. Quelques fonctions utilitaires permettent de garder des calculs propres.

```js
// main.js (partie 2)

// État du serpent
let snake;           // Tableau de cellules de grille [{x, y}, ...]; index 0 = tête
let snakeRects;      // Tableau de rectangles Phaser dessinés aux positions des cellules
let direction;       // Direction actuelle du mouvement (objet issu de DIR)
let nextDirection;   // Prochaine direction choisie par le joueur (appliquée au pas suivant)
let food;            // Cellule de nourriture actuelle {x, y}
let score = 0;       // Compteur de score actuel
let scoreText;       // Objet texte Phaser qui affiche le score
let moveEvent;       // Événement timer Phaser pour déplacer le serpent à intervalles fixes
let speedMs = 130;   // Délai en millisecondes entre les mouvements (plus bas = plus rapide)

// État des entrées
let cursors;         // Objet utilitaire Phaser pour les touches fléchées
let spaceKey;        // Objet Key Phaser pour la barre d'espace (redémarrer le jeu)

/**
 * Convertit une cellule de grille (x,y) en son centre en pixels (px,py) sur le canvas.
 * Exemple : (0,0) -> (8,8) si TILE=16. Assure que les rectangles sont centrés.
 */
function gridToPixelCenter(x, y) {
  return { px: x * TILE + TILE / 2, py: y * TILE + TILE / 2 };
}

/**
 * Choisit une cellule de grille aléatoire qui n'est pas occupée par snakeRects.
 * - Crée un Set de cellules occupées sous forme de chaînes "x,y" pour une recherche rapide.
 * - Continue de générer des cellules aléatoires jusqu'à en trouver une libre.
 * Utilisé pour placer la nourriture afin qu'elle n'apparaisse jamais sur le serpent.
 */
function randomFreeCell(excludeCells) {
  const occupied = new Set(excludeCells.map(c => `${c.x},${c.y}`));
  while (true) {
    const x = Math.floor(Math.random() * COLS);
    const y = Math.floor(Math.random() * ROWS);
    if (!occupied.has(`${x},${y}`)) return { x, y };
  }
}

/**
 * Vérifie si la direction 'a' est exactement l'opposée de la direction 'b'.
 * Exemple : gauche vs droite, ou haut vs bas.
 * Cela empêche le serpent de se retourner instantanément à 180° sur lui-même.
 */
function isOpposite(a, b) {
  return a.x === -b.x && a.y === -b.y;
}
```

`gridToPixelCenter` convertit une cellule de grille en point central en pixels pour que les rectangles s'alignent. `randomFreeCell` trouve une cellule non utilisée par le serpent. `isOpposite` aide à bloquer les inversions instantanées qui causeraient une collision.

## Preload et Create

Ce jeu utilise de simples rectangles vectoriels, il n'y a donc pas d'images à charger. Vous définissez tout de même les fonctions de scène puisque Phaser les appelle par nom depuis votre configuration.

```js
// main.js (partie 3)

/**
 * preload()
 * S'exécute une fois avant le début du jeu.
 * Utilisé pour charger des images, sons et autres ressources.
 * Dans cette version, nous utilisons de simples rectangles colorés (aucune ressource nécessaire).
 */
function preload() {
  // Aucune ressource à charger dans cette version.
}

/**
 * create()
 * S'exécute une fois après le preload. Configure la scène du jeu.
 * - Prépare les entrées clavier
 * - Appelle initGame() pour construire le serpent, la nourriture, l'UI du score et lancer le mouvement
 */
function create() {
  // Utilitaire Phaser qui nous donne les entrées des touches fléchées
  cursors = this.input.keyboard.createCursorKeys();

  // Enregistre la barre d'espace pour redémarrer le jeu plus tard
  spaceKey = this.input.keyboard.addKey(Phaser.Input.Keyboard.KeyCodes.SPACE);

  // Initialise l'état du jeu (serpent, nourriture, score, timer)
  // Utilisation de .call(this) pour que initGame s'exécute dans le contexte de la scène
  initGame.call(this);
}
```

L'étape `create` configure l'entrée clavier. Elle appelle ensuite `initGame` pour construire le premier serpent, placer la nourriture et démarrer le minuteur. Le `.call(this)` garantit que la fonction utilitaire peut utiliser le `this` de la scène.

## Initialisation du jeu

Lors d'un nouveau départ ou d'un redémarrage, vous devez effacer les anciens minuteurs et formes, réinitialiser le score, construire un serpent court au milieu, le dessiner, placer la nourriture et lancer la boucle de mouvement.

```js
// main.js (partie 4)

/**
 * initGame()
 * Appelée au début du jeu ou après avoir appuyé sur Espace pour redémarrer.
 * - Efface l'ancien état (serpent, nourriture, timers)
 * - Réinitialise le score
 * - Crée un nouveau serpent au centre de la grille
 * - Fait apparaître la première nourriture
 * - Configure le texte du score
 * - Lance la boucle temporisée qui déplace le serpent
 */
function initGame() {
  // Si un ancien timer de mouvement existe, on l'arrête
  if (moveEvent) moveEvent.remove(false);

  // Si d'anciens rectangles de serpent existent, on les détruit pour nettoyer l'écran
  if (snakeRects) snakeRects.forEach(r => r.destroy());

  // Réinitialise le score et la direction du serpent
  score = 0;
  direction = DIR.right;     // Le serpent commence vers la droite
  nextDirection = DIR.right; // La file d'attente des entrées pointe aussi vers la droite

  // Trouve la position de départ près du centre de la grille
  const startX = Math.floor(COLS / 2);
  const startY = Math.floor(ROWS / 2);

  // Le serpent commence avec 3 segments : tête + 2 morceaux de corps
  snake = [
    { x: startX,     y: startY },     // tête (milieu)
    { x: startX - 1, y: startY },     // segment de corps à gauche de la tête
    { x: startX - 2, y: startY },     // queue encore plus à gauche
  ];

  // Crée des objets rectangles dans Phaser pour dessiner visuellement le serpent
  snakeRects = snake.map((cell, i) => {
    const { px, py } = gridToPixelCenter(cell.x, cell.y);
    const color = i === 0 ? COLORS.head : COLORS.body;    // la tête est un vert plus vif
    const rect = this.add.rectangle(px, py, TILE - 2, TILE - 2, color); // légèrement plus petit pour l'espacement
    rect.setOrigin(0.5, 0.5);                             // point d'ancrage centré
    return rect;
  });

  // Fait apparaître la nourriture sur une cellule libre aléatoire
  food = randomFreeCell(snake);
  const { px, py } = gridToPixelCenter(food.x, food.y);

  // Si la nourriture existe déjà d'une partie précédente, on la retire d'abord
  if (this.foodRect) this.foodRect.destroy();

  // Dessine la nouvelle nourriture sous forme de rectangle rouge
  this.foodRect = this.add.rectangle(px, py, TILE - 2, TILE - 2, COLORS.food);

  // Si le texte du score n'existe pas encore, on le crée
  // Sinon (au redémarrage), on réinitialise simplement sa valeur
  if (!scoreText) {
    scoreText = this.add.text(8, 6, 'Score : 0', { fontFamily: 'monospace', fontSize: 18, color: '#fff' });
    this.add.text(8, 28, 'Flèches pour bouger. Espace pour redémarrer.', { fontFamily: 'monospace', fontSize: 14, color: '#aaa' });
  } else {
    scoreText.setText('Score : 0');
  }

  // Réinitialise la vitesse et crée un timer répétitif
  // Toutes les "speedMs" millisecondes, stepSnake() s'exécute pour déplacer le serpent
  speedMs = 130;
  moveEvent = this.time.addEvent({
    delay: speedMs,
    loop: true,
    callback: () => stepSnake.call(this)
  });

  // Si un message "Game Over" existe de la partie précédente, on le retire
  if (this.gameOverText) {
    this.gameOverText.destroy();
    this.gameOverText = null;
  }
}
```

Les rectangles sont un ou deux pixels plus petits que la tuile pour obtenir un espace net entre les cellules. L'événement temporel appelle `stepSnake` selon un rythme fixe. Ce rythme est distinct du taux de rafraîchissement (FPS), ce qui maintient un mouvement stable sur toutes les machines.

## Lecture des entrées à chaque frame

Vous lirez les touches fléchées dans `update`. Vous ne déplacez pas le serpent ici. Vous définissez seulement la prochaine direction. Le mouvement se produit via le timer pour que le jeu ait un rythme régulier.

```js
// main.js (partie 5)

/**
 * update()
 * S'exécute à chaque image (boucle de jeu de Phaser).
 * - Lit les entrées clavier
 * - Met à jour "nextDirection" pour que le serpent tourne au prochain pas
 * - Écoute l'appui sur Espace pour redémarrer si le jeu est fini
 */
function update() {
  // Vérifie si la flèche GAUCHE est pressée ET n'est pas l'opposé de la direction actuelle
  if (cursors.left.isDown && !isOpposite(DIR.left, direction)) {
    nextDirection = DIR.left;

  // Vérifie si la flèche DROITE est pressée
  } else if (cursors.right.isDown && !isOpposite(DIR.right, direction)) {
    nextDirection = DIR.right;

  // Vérifie si la flèche HAUT est pressée
  } else if (cursors.up.isDown && !isOpposite(DIR.up, direction)) {
    nextDirection = DIR.up;

  // Vérifie si la flèche BAS est pressée
  } else if (cursors.down.isDown && !isOpposite(DIR.down, direction)) {
    nextDirection = DIR.down;
  }

  // Si le jeu est fini (un texte "Game Over" existe)
  // ET que la barre d'Espace vient d'être pressée → redémarrer le jeu
  if (this.gameOverText && Phaser.Input.Keyboard.JustDown(spaceKey)) {
    initGame.call(this);
  }
}
```

Ce modèle empêche le serpent de sauter des cellules si le framerate varie. Cela rend aussi le jeu plus juste. Vos pressions sur les touches sont captées, mais le corps se déplace au rythme défini par le minuteur.

## Déplacement du serpent, manger et dessin

Cette fonction est le cœur du jeu. Elle récupère l'entrée en file d'attente, calcule la prochaine cellule de la tête, vérifie les collisions, déplace ou fait grandir le serpent, met à jour le score et rafraîchit les couleurs.

```js
// main.js (partie 6)

/**
 * stepSnake()
 * Cette fonction s'exécute à chaque "tic" (basé sur le timer).
 * - Déplace le serpent d'une cellule
 * - Vérifie les collisions (mur ou soi-même)
 * - Gère la consommation de nourriture (croissance + score)
 * - Met à jour les rectangles du serpent à l'écran
 */
function stepSnake() {
  // Applique la direction choisie dans update()
  direction = nextDirection;

  // Récupère la tête actuelle du serpent
  const head = snake[0];

  // Crée une nouvelle position de tête en déplaçant d'une cellule
  const newHead = { x: head.x + direction.x, y: head.y + direction.y };

  // === Vérification Collision #1 : Mur ===
  if (newHead.x < 0 || newHead.x >= COLS || newHead.y < 0 || newHead.y >= ROWS) {
    return endGame.call(this);
  }

  // === Vérification Collision #2 : Soi-même ===
  for (let i = 0; i < snake.length; i++) {
    if (snake[i].x === newHead.x && snake[i].y === newHead.y) {
      return endGame.call(this);
    }
  }

  // === Vérifie si la nourriture est mangée ===
  const ate = newHead.x === food.x && newHead.y === food.y;

  // Ajoute la nouvelle cellule de tête au début du tableau snake
  snake.unshift(newHead);

  if (!ate) {
    // Cas : Le serpent n'a PAS mangé → garde la même longueur
    // Retire la dernière cellule (queue)
    snake.pop();

    // Réutilise le dernier objet rectangle pour la performance
    const tailRect = snakeRects.pop();
    const { px, py } = gridToPixelCenter(newHead.x, newHead.y);
    tailRect.setPosition(px, py);       // Le déplace à la nouvelle position de la tête
    snakeRects.unshift(tailRect);       // Le place au début de la liste des rectangles
  } else {
    // Cas : Le serpent A mangé → il grandit
    const { px, py } = gridToPixelCenter(newHead.x, newHead.y);
    const headRect = this.add.rectangle(px, py, TILE - 2, TILE - 2, COLORS.head);
    snakeRects.unshift(headRect);

    score += 10;
    scoreText.setText(`Score : ${score}`);

    placeFood.call(this);
    maybeSpeedUp.call(this);
  }

  // === Mise à jour des couleurs ===
  // S'assure que seul l'index 0 est dessiné comme la "tête" (vert vif),
  // et que le segment suivant devient une partie du "corps"
  if (snakeRects[1]) snakeRects[1].setFillStyle(COLORS.body);
  snakeRects[0].setFillStyle(COLORS.head);
}
```

La règle de mouvement est simple. Ajoutez une tête dans la direction actuelle. Si vous n'avez pas mangé, retirez la queue. Si vous avez mangé, gardez la queue pour grandir d'une unité. Pour dessiner cela, vous réutilisez le dernier rectangle lorsque vous vous déplacez simplement. Vous le déplacez vers le nouvel emplacement en pixels de la tête et le mettez en tête de liste. Quand vous grandissez, vous créez un nouveau rectangle pour la nouvelle tête.

## Apparition de la nourriture et augmentation de la vitesse

Après avoir mangé, vous devez placer la nourriture dans une nouvelle cellule libre. Vous pouvez également augmenter légèrement la vitesse pour que le jeu devienne plus difficile avec le temps.

```js
// main.js (partie 7)

/**
 * placeFood()
 * Fait apparaître la nourriture sur une nouvelle cellule aléatoire hors du serpent.
 */
function placeFood() {
  food = randomFreeCell(snake);
  const { px, py } = gridToPixelCenter(food.x, food.y);
  this.foodRect.setPosition(px, py);
}

/**
 * maybeSpeedUp()
 * Rend le jeu un peu plus difficile à chaque fois que de la nourriture est mangée.
 */
function maybeSpeedUp() {
  if (speedMs > 70) {
    speedMs -= 3;
    moveEvent.remove(false);
    moveEvent = this.time.addEvent({
      delay: speedMs,
      loop: true,
      callback: () => stepSnake.call(this)
    });
  }
}
```

Il y a une limite inférieure pour la vitesse afin que le jeu ne devienne pas illisible. Vous pouvez ajuster ces nombres pour obtenir le ressenti souhaité.

## Game Over et redémarrage

Lorsque le serpent frappe un mur ou lui-même, la partie s'arrête. Vous stoppez le minuteur et affichez un message. Appuyer sur espace relance le jeu.

```js
// main.js (partie 8)

/**
 * endGame()
 * Appelée quand le serpent entre en collision.
 */
function endGame() {
  moveEvent.remove(false);

  const style = {
    fontFamily: 'monospace',
    fontSize: 28,
    color: '#fff',
    align: 'center'
  };

  const msg = `Game Over\nScore : ${score}\nAppuyez sur Espace pour redémarrer`;
  this.gameOverText = this.add.text(WIDTH / 2, HEIGHT / 2, msg, style).setOrigin(0.5, 0.5);
}
```

La fonction `update` que vous avez écrite précédemment écoute la touche espace via `JustDown`, de sorte que le redémarrage ne se produise qu'une seule fois par pression de touche.

## Comment tout s'articule

Vous avez maintenant la boucle complète d'une scène Phaser. Le `preload` est vide dans cette version car les rectangles ne nécessitent pas de ressources externes. L'étape `create` connecte l'entrée clavier et appelle `initGame`. Le minuteur créé dans `initGame` gère le temps pour le mouvement.

L'étape `update` lit les touches à chaque image et définit une direction future. La fonction `stepSnake` s'exécute via le minuteur. Elle déplace la tête, vérifie les collisions, gère la croissance, réutilise les formes pour la performance et met à jour le score. Quand la partie s'arrête, `endGame` stoppe le minuteur et affiche un message clair. Une simple pression sur une touche appelle `initGame` pour recommencer à zéro.

Ce style s'adapte bien à de nombreux autres petits jeux. Si vous pouvez exprimer l'état de votre jeu sous forme de données et le déplacer selon un calendrier, vous pouvez le dessiner avec des formes simples ou des sprites. Les événements temporels de Phaser vous donnent un battement de cœur propre. Son système d'entrée facilite la gestion des touches. Son API de dessin permet d'afficher rapidement des rectangles, du texte ou des images.

## Prochaines étapes utiles

Il existe de nombreuses petites fonctionnalités que vous pouvez ajouter sans changer le cœur du jeu. Vous pouvez stocker un record (high score) dans le `localStorage`. Vous pouvez ajouter des sons simples lorsque vous mangez ou quand le jeu se termine en chargeant de l'audio dans `preload` et en appelant `this.sound.play` aux bons endroits.

Vous pouvez faire en sorte que le monde boucle sur les bords en remplaçant la vérification du mur par un calcul modulo pour que le serpent apparaisse du côté opposé. Vous pouvez thématiser le jeu en changeant les couleurs des rectangles ou en les remplaçant par des images.

Chacune de ces additions repose sur la même base. Gardez la logique de la grille simple. Gardez l'état dans des tableaux et des objets clairs. Déplacez-vous sur un timer fixe. Dessinez en fonction de l'état. C'est le schéma à suivre.

## Dernières réflexions

Vous avez commencé avec une page blanche et avez terminé avec un jeu par navigateur fonctionnel. Vous avez configuré Phaser, construit une scène et utilisé un minuteur pour piloter le mouvement. Vous avez appris à gérer les entrées de manière sécurisée, à faire grandir le serpent, à détecter les collisions et à dessiner avec des rectangles. Vous avez gardé le code propre avec de petites fonctions utilitaires et des noms explicites.

À partir de là, vous pouvez vous orienter vers d'autres jeux sur grille comme Tetris ou le Démineur, ou essayer un style différent comme Pong ou Breakout. La structure sera similaire. Une scène pour tout mettre en place, un timer ou une étape physique pour faire avancer les choses, et quelques règles qui définissent le plaisir de jouer. C'est toute la beauté de Phaser pour les débutants.

Si vous aimez le jeu en ligne, [GameBoost](https://gameboost.com/) est l'endroit idéal. Découvrez des [Comptes GTA moddés](https://gameboost.com/grand-theft-auto-v/accounts) remplis d'améliorations exclusives. Vous trouverez également des comptes pour d'autres titres favoris des fans comme Fortnite, Grow a Garden, Clash of Clans, et plus encore – le tout sur une marketplace de confiance.