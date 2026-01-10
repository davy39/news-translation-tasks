---
title: Comment créer un jeu de Morpion avec Phaser.js
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2025-08-20T20:07:51.970Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-tic-tac-toe-game-with-phaserjs
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1755720429987/ba7670ba-12b0-4c0a-a09b-80936ba1a023.png
tags:
- name: JavaScript
  slug: javascript
- name: Game Development
  slug: game-development
seo_title: Comment créer un jeu de Morpion avec Phaser.js
seo_desc: 'Tic-Tac-Toe is a great project for beginners who want to learn how to build
  games. It’s simple to understand but gives you the chance to learn about game state,
  player turns, winning logic, and user input.

  In this tutorial, you’ll learn how to build ...'
---

Le Morpion est un excellent projet pour les débutants qui souhaitent apprendre à créer des jeux. C'est simple à comprendre, mais cela vous donne l'occasion d'en savoir plus sur l'état du jeu, les tours des joueurs, la logique de victoire et les entrées utilisateur.

Dans ce tutoriel, vous apprendrez à construire un Morpion en utilisant [Phaser.js](https://phaser.io/), un Framework rapide, amusant et open source pour créer des jeux 2D dans le navigateur.

Si vous débutez avec Phaser.js, ne vous inquiétez pas. Nous allons tout parcourir étape par étape. À la fin, vous aurez un jeu fonctionnel auquel vous pourrez jouer, que vous pourrez partager ou sur lequel vous pourrez vous appuyer.

Vous pouvez [jouer au jeu ici](https://manishshivanandhan.com/phaser-tic-tac-toe) pour vous faire une idée de ce que vous allez construire.

## Table des matières

* [Qu'est-ce que Phaser.js ?](#heading-qu-est-ce-que-phaser-js)
    
* [Configuration du projet](#heading-configuration-du-projet)
    
* [Comment définir la configuration du jeu](#heading-comment-definir-la-configuration-du-jeu)
    
* [Comment précharger les ressources](#heading-comment-precharger-les-ressources)
    
* [Comment créer la scène du jeu](#heading-comment-creer-la-scene-du-jeu)
    
* [Comment dessiner la grille](#heading-comment-dessiner-la-grille)
    
* [Comment initialiser et réinitialiser le jeu](#heading-comment-initialiser-et-reinitaliser-le-jeu)
    
* [Comment gérer les entrées du joueur](#heading-comment-gerer-les-entrees-du-joueur)
    
* [Comment placer des marques sur le plateau](#heading-comment-placer-des-marques-sur-le-plateau)
    
* [Comment vérifier s'il y a un gagnant](#heading-comment-verifier-s-il-y-a-un-gagnant)
    
* [Comment détecter une égalité](#heading-comment-detecter-une-egalite)
    
* [Comment dessiner la ligne de victoire](#heading-comment-dessiner-la-ligne-de-victoire)
    
* [Dernières pensées](#heading-dernieres-pensees)
    

## Qu'est-ce que Phaser.js ?

Phaser.js est un Framework de jeu JavaScript gratuit et open-source. Il aide les développeurs à créer des jeux HTML5 qui fonctionnent sur tous les navigateurs web. Phaser gère des aspects tels que le rendu des graphismes, la détection des entrées et l'exécution de la boucle de jeu.

Vous pouvez utiliser Phaser pour créer des jeux simples comme Pong et le Morpion, ou des jeux de plateforme et de rôle plus avancés. Il prend en charge le rendu Canvas et WebGL, de sorte que vos jeux fonctionneront de manière fluide sur la plupart des appareils.

## Configuration du projet

Créez un dossier pour votre projet et ajoutez deux fichiers : `index.html` et `game.js`. Le fichier HTML charge Phaser et le fichier JavaScript contient la logique du jeu. [Voici le dépôt](https://github.com/manishmshiva/phaser-tic-tac-toe) avec le code final.

Voici à quoi devrait ressembler le fichier `index.html` :

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>Tic Tac Toe — Phaser 3</title>
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <style>
    html, body { height: 100%; margin: 0; background: #0f172a; display: grid; place-items: center; }
    #game { box-shadow: 0 10px 30px rgba(0,0,0,.35); border-radius: 12px; overflow: hidden; }
    .hint { color: #e2e8f0; margin-top: 10px; font-size: 14px; text-align: center; opacity: .85; }
  </style>
  <script src="https://cdn.jsdelivr.net/npm/phaser@3.60.0/dist/phaser.min.js"></script>
</head>
<body>
  <div id="game"></div>
  <div class="hint">Click a cell to play. Tap “Restart” to start over.</div>
  <script src="./game.js"></script>
</body>
</html>
```

Ceci met en place une page HTML simple, charge Phaser à partir d'un CDN et pointe vers votre fichier `game.js`. Le conteneur `#game` est l'endroit où Phaser insérera le canvas du jeu.

## Comment définir la configuration du jeu

Les jeux Phaser sont construits à partir d'un objet de configuration qui définit des éléments tels que la largeur, la hauteur, la couleur d'arrière-plan et les fonctions à appeler pour le chargement, la création et la mise à jour du jeu.

```js
(() => {
  const GRID = 3;
  const CELL = 120;
  const BOARD = GRID * CELL;
  const HUD = 72;
  const WIDTH = BOARD;
  const HEIGHT = BOARD + HUD;

  let scene;
  let board;
  let currentPlayer;
  let gameOver;

  let gridGfx;
  let overlayGfx;
  let marks = [];
  let statusText;
  let restartText;

  const config = {
    type: Phaser.AUTO,
    parent: "game",
    width: WIDTH,
    height: HEIGHT,
    backgroundColor: "#ffffff",
    scale: { mode: Phaser.Scale.FIT, autoCenter: Phaser.Scale.CENTER_BOTH },
    scene: { preload, create, update }
  };

  new Phaser.Game(config);
```

Nous commençons par définir des constantes pour la taille de la grille et des cellules. L'objet `config` indique à Phaser de créer un jeu avec ces dimensions et d'utiliser les fonctions `preload`, `create` et `update` que nous allons définir.

## Comment précharger les ressources

Comme nous dessinons tout avec les outils graphiques et de texte de Phaser, nous n'avons pas besoin de charger d'images ou de sons externes.

```js
  function preload() {
    // No assets to load
  }
```

Il s'agit d'un espace réservé qui permet à Phaser d'appeler `preload` avant le début du jeu.

## Comment créer la scène du jeu

La fonction `create` s'exécute une fois au début de la scène. Ici, nous dessinons la grille, configurons l'état initial et ajoutons les éléments de l'interface utilisateur.

```js
  function create() {
    scene = this;

    gridGfx = scene.add.graphics({ lineStyle: { width: 4, color: 0x000000 } });
    overlayGfx = scene.add.graphics();
    drawGrid();

    initGame();

    statusText = scene.add.text(WIDTH / 2, BOARD + 12, "Player X's turn", {
      fontSize: "20px",
      color: "#111",
      fontFamily: "Arial, Helvetica, sans-serif"
    }).setOrigin(0.5, 0);

    restartText = scene.add.text(WIDTH / 2, BOARD + 38, "Restart", {
      fontSize: "18px",
      color: "#2563eb",
      fontFamily: "Arial, Helvetica, sans-serif"
    }).setOrigin(0.5, 0).setInteractive({ useHandCursor: true });

    restartText.on("pointerup", hardReset);

    scene.input.on("pointerdown", onPointerDown, scene);
  }
```

Nous avons créé deux objets `Graphics` : un pour la grille statique et un autre pour la ligne de victoire. Ensuite, nous avons appelé `drawGrid()` et `initGame()` pour configurer le plateau de jeu. Le texte d'état et le bouton de redémarrage sont placés sous la grille. Nous écoutons également les clics sur le plateau avec `pointerdown`.

## Comment dessiner la grille

La grille est composée de deux lignes verticales et deux lignes horizontales.

```js
  function drawGrid() {
    gridGfx.strokeLineShape(new Phaser.Geom.Line(CELL, 0, CELL, BOARD));
    gridGfx.strokeLineShape(new Phaser.Geom.Line(CELL * 2, 0, CELL * 2, BOARD));
    gridGfx.strokeLineShape(new Phaser.Geom.Line(0, CELL, BOARD, CELL));
    gridGfx.strokeLineShape(new Phaser.Geom.Line(0, CELL * 2, BOARD, CELL * 2));
  }
```

Nous utilisons `Phaser.Geom.Line` pour définir les points de départ et d'arrivée de chaque ligne, puis nous les dessinons avec `strokeLineShape`.

## Comment initialiser et réinitialiser le jeu

La fonction `initGame` configure une nouvelle partie, et `hardReset` est appelée lorsque l'on clique sur le bouton de redémarrage.

```js
  function initGame() {
    board = Array.from({ length: GRID }, () => Array(GRID).fill(""));
    currentPlayer = "X";
    gameOver = false;
    overlayGfx.clear();
    for (const t of marks) t.destroy();
    marks = [];
    setStatus("Player X's turn");
  }

  function hardReset() {
    initGame();
  }

  function setStatus(msg) {
    statusText && statusText.setText(msg);
  }
```

Le plateau est représenté par un tableau 2D rempli de chaînes vides. Le joueur actuel commence par X, et le tableau `marks` assure le suivi des objets texte afin que nous puissions les effacer lors de la réinitialisation.

## Comment gérer les entrées du joueur

Lorsque le joueur clique sur une cellule, nous déterminons sa ligne et sa colonne et vérifions si le mouvement est valide.

```js
  function onPointerDown(pointer) {
    if (gameOver) return;
    if (pointer.y > BOARD) return;

    const col = Math.floor(pointer.x / CELL);
    const row = Math.floor(pointer.y / CELL);
    if (!inBounds(row, col)) return;
    if (board[row][col] !== "") return;

    placeMark(row, col, currentPlayer);

    const win = checkWin(board);
    if (win) {
      gameOver = true;
      drawWinLine(win);
      setStatus(`Player ${currentPlayer} wins!`);
      return;
    }

    if (isFull(board)) {
      gameOver = true;
      setStatus("Draw! No more moves.");
      return;
    }

    currentPlayer = currentPlayer === "X" ? "O" : "X";
    setStatus(`Player ${currentPlayer}'s turn`);
  }
```

Cela garantit que nous n'agissons que si le jeu n'est pas terminé, que le clic est à l'intérieur du plateau et que la cellule choisie est vide. Après avoir placé une marque, nous vérifions s'il y a une victoire ou une égalité avant de changer de tour.

## Comment placer des marques sur le plateau

Nous affichons un X ou un O au centre de la cellule cliquée.

```js
  function inBounds(r, c) {
    return r >= 0 && r < GRID && c >= 0 && c < GRID;
  }

  function placeMark(row, col, player) {
    board[row][col] = player;
    const cx = col * CELL + CELL / 2;
    const cy = row * CELL + CELL / 2;
    const t = scene.add.text(cx, cy, player, {
      fontSize: Math.floor(CELL * 0.66) + "px",
      color: "#111111",
      fontFamily: "Arial, Helvetica, sans-serif"
    }).setOrigin(0.5);
    marks.push(t);
  }
```

Les coordonnées sont calculées de manière à ce que le texte soit centré dans la cellule. Nous stockons l'objet texte dans le tableau `marks` afin qu'il puisse être supprimé lors de la réinitialisation.

## Comment vérifier s'il y a un gagnant

Nous vérifions les lignes, les colonnes et les diagonales pour voir si le joueur actuel en a trois d'affilée.

```js
  function checkWin(b) {
    for (let r = 0; r < GRID; r++) {
      if (b[r][0] && b[r][0] === b[r][1] && b[r][1] === b[r][2]) {
        return { kind: "row", index: r };
      }
    }
    for (let c = 0; c < GRID; c++) {
      if (b[0][c] && b[0][c] === b[1][c] && b[1][c] === b[2][c]) {
        return { kind: "col", index: c };
      }
    }
    if (b[0][0] && b[0][0] === b[1][1] && b[1][1] === b[2][2]) {
      return { kind: "diag" };
    }
    if (b[0][2] && b[0][2] === b[1][1] && b[1][1] === b[2][0]) {
      return { kind: "anti" };
    }
    return null;
  }
```

Si une victoire est trouvée, nous renvoyons un objet décrivant la ligne gagnante afin qu'elle puisse être dessinée.

## Comment détecter une égalité

Si toutes les cellules sont remplies et qu'il n'y a pas de gagnant, le jeu se termine par un match nul.

```js
  function isFull(b) {
    for (let r = 0; r < GRID; r++) {
      for (let c = 0; c < GRID; c++) {
        if (b[r][c] === "") return false;
      }
    }
    return true;
  }
```

Ceci parcourt chaque cellule et renvoie false si l'une d'elles est vide.

## Comment dessiner la ligne de victoire

Une ligne rouge est dessinée sur les cellules gagnantes.

```js
  function drawWinLine(res) {
    overlayGfx.clear();
    overlayGfx.lineStyle(6, 0xef4444, 1);
    const pad = 14;
    const half = CELL / 2;

    if (res.kind === "row") {
      const y = res.index * CELL + half;
      overlayGfx.strokeLineShape(new Phaser.Geom.Line(pad, y, BOARD - pad, y));
    } else if (res.kind === "col") {
      const x = res.index * CELL + half;
      overlayGfx.strokeLineShape(new Phaser.Geom.Line(x, pad, x, BOARD - pad));
    } else if (res.kind === "diag") {
      overlayGfx.strokeLineShape(new Phaser.Geom.Line(pad, pad, BOARD - pad, BOARD - pad));
    } else if (res.kind === "anti") {
      overlayGfx.strokeLineShape(new Phaser.Geom.Line(BOARD - pad, pad, pad, BOARD - pad));
    }
  }
})();
```

Les coordonnées sont calculées en fonction du type de victoire pour s'assurer que la ligne passe par les bonnes cellules.

Super. Maintenant, ouvrez `index.html` et vous pouvez commencer à jouer au jeu !

![Jeu final](https://cdn.hashnode.com/res/hashnode/image/upload/v1754903555585/eac6d264-a50a-4bc6-8acc-6cdf7fc214eb.png align="center")

## Dernières pensées

Vous avez maintenant construit un jeu de Morpion complet avec Phaser.js. Cela inclut une grille 3x3, l'alternance des tours, la détection de victoire avec une ligne de mise en évidence, la détection d'égalité et un bouton de redémarrage. Le code utilise des concepts fondamentaux du développement de jeux tels que la gestion des entrées, la gestion de l'état du jeu et le rendu, que vous pouvez utiliser dans des projets plus importants.

Si vous aimez les jeux en ligne, découvrez [GameBoost](https://gameboost.com/), la plateforme ultime pour les joueurs. Vous pouvez y trouver des [comptes Fortnite](https://gameboost.com/fortnite/accounts) avec des skins exclusifs, ainsi que des options pour d'autres jeux populaires comme Grow a Garden, Clash of Clans, et plus encore.