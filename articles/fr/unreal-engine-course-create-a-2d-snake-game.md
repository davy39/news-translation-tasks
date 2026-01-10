---
title: 'Cours Unreal Engine : Créer un jeu Snake en 2D'
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2020-09-09T18:00:33.000Z'
originalURL: https://freecodecamp.org/news/unreal-engine-course-create-a-2d-snake-game
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/2dsnake.png
tags: []
seo_title: 'Cours Unreal Engine : Créer un jeu Snake en 2D'
seo_desc: 'Unreal Engine is one of the most popular game development platforms, and
  it''s completely free to use. When most people think of Unreal Engine, they think
  of 3D games. But you can also use it to build 2D games.

  We just released a full 3-hour Unreal En...'
---

Unreal Engine est l'une des plateformes de développement de jeux les plus populaires, et elle est complètement gratuite. Lorsque la plupart des gens pensent à Unreal Engine, ils pensent aux jeux 3D. Mais vous pouvez également l'utiliser pour créer des jeux 2D.

Nous venons de publier un cours complet de 3 heures sur Unreal Engine sur la chaîne YouTube freeCodeCamp.org qui vous apprendra à créer un jeu Snake en 2D. Le cours a été créé par le développeur de jeux extraordinaire Fahir d'Awesome Tuts.

Dans ce tutoriel, vous allez construire le jeu classique snake. Un joueur peut contrôler le serpent, ramasser de la nourriture, faire grandir le serpent, marquer des points, et finalement s'écraser et déclencher un game over. Il y a aussi quelques animations simples pour différents événements dans le jeu.

Vous apprendrez à utiliser les Blueprints pour créer le jeu. Les Blueprints est le système de script visuel intégré à Unreal Engine. Il permet de mettre un jeu en route plus rapidement. Vous n'aurez presque pas à écrire de code réel pour créer le jeu.

Il y a des sprites, des textures et des assets de flipbooks nécessaires pour ce jeu. Et ils sont tous inclus via un lien de téléchargement.

Après avoir terminé la création du jeu dans le tutoriel, vous pouvez utiliser les mêmes assets pour améliorer le jeu par vous-même, ou pour créer un tout nouveau jeu.

Vous pouvez regarder [le cours complet sur la chaîne YouTube freeCodeCamp.org](https://youtu.be/CU3jeNzbzqU) (3 heures de visionnage).

????

Et si vous voulez d'abord vous mettre dans l'ambiance du snake, vous pouvez jouer à un jeu snake ci-dessous en utilisant les touches fléchées. Le jeu que vous allez créer sera encore plus cool que celui-ci. ? ([Source](https://gist.github.com/straker/ff00b4b49669ad3dec890306d348adc4))


  <style>
  canvas {
    border: 1px solid black;
  }
  </style>
<canvas width="400" height="400" id="game"></canvas>
<script>
var canvas = document.getElementById('game');
var context = canvas.getContext('2d');

var grid = 16;
var count = 0;
  
var snake = {
  x: 160,
  y: 160,
  
  // vitesse du serpent. se déplace d'une longueur de grille à chaque frame dans la direction x ou y
  dx: grid,
  dy: 0,
  
  // garder une trace de toutes les grilles que le corps du serpent occupe
  cells: [],
  
  // longueur du serpent. grandit lorsqu'il mange une pomme
  maxCells: 4
};
var apple = {
  x: 320,
  y: 320
};

// obtenir des nombres entiers aléatoires dans une plage spécifique
// @see https://stackoverflow.com/a/1527820/2124254
function getRandomInt(min, max) {
  return Math.floor(Math.random() * (max - min)) + min;
}

// boucle de jeu
function loop() {
  requestAnimationFrame(loop);

  // ralentir la boucle de jeu à 15 fps au lieu de 60 (60/15 = 4)
  if (++count < 4) {
    return;
  }

  count = 0;
  context.clearRect(0,0,canvas.width,canvas.height);

  // déplacer le serpent selon sa vitesse
  snake.x += snake.dx;
  snake.y += snake.dy;

  // envelopper la position du serpent horizontalement sur le bord de l'écran
  if (snake.x < 0) {
    snake.x = canvas.width - grid;
  }
  else if (snake.x >= canvas.width) {
    snake.x = 0;
  }
  
  // envelopper la position du serpent verticalement sur le bord de l'écran
  if (snake.y < 0) {
    snake.y = canvas.height - grid;
  }
  else if (snake.y >= canvas.height) {
    snake.y = 0;
  }

  // garder une trace de l'endroit où le serpent est passé. l'avant du tableau est toujours la tête
  snake.cells.unshift({x: snake.x, y: snake.y});

  // supprimer les cellules à mesure que nous nous en éloignons
  if (snake.cells.length > snake.maxCells) {
    snake.cells.pop();
  }

  // dessiner la pomme
  context.fillStyle = 'red';
  context.fillRect(apple.x, apple.y, grid-1, grid-1);

  // dessiner le serpent une cellule à la fois
  context.fillStyle = 'green';
  snake.cells.forEach(function(cell, index) {
    
    // dessiner 1 px plus petit que la grille crée un effet de grille dans le corps du serpent pour que vous puissiez voir sa longueur
    context.fillRect(cell.x, cell.y, grid-1, grid-1);  

    // le serpent a mangé la pomme
    if (cell.x === apple.x && cell.y === apple.y) {
      snake.maxCells++;

      // le canevas est de 400x400, soit 25x25 grilles 
      apple.x = getRandomInt(0, 25) * grid;
      apple.y = getRandomInt(0, 25) * grid;
    }

    // vérifier la collision avec toutes les cellules après celle-ci (tri à bulles modifié)
    for (var i = index + 1; i < snake.cells.length; i++) {
      
      // le serpent occupe le même espace qu'une partie du corps. réinitialiser le jeu
      if (cell.x === snake.cells[i].x && cell.y === snake.cells[i].y) {
        snake.x = 160;
        snake.y = 160;
        snake.cells = [];
        snake.maxCells = 4;
        snake.dx = grid;
        snake.dy = 0;

        apple.x = getRandomInt(0, 25) * grid;
        apple.y = getRandomInt(0, 25) * grid;
      }
    }
  });
}

// écouter les événements du clavier pour déplacer le serpent
document.addEventListener('keydown', function(e) {
  // empêcher le serpent de revenir sur lui-même en vérifiant qu'il
  // ne se déplace pas déjà sur le même axe (appuyer sur la gauche en se déplaçant
  // à gauche ne fera rien, et appuyer sur la droite en se déplaçant à gauche
  // ne devrait pas vous permettre de entrer en collision avec votre propre corps)
  
  // touche flèche gauche
  if (e.which === 37 && snake.dx === 0) {
    snake.dx = -grid;
    snake.dy = 0;
  }
  // touche flèche haut
  else if (e.which === 38 && snake.dy === 0) {
    snake.dy = -grid;
    snake.dx = 0;
  }
  // touche flèche droite
  else if (e.which === 39 && snake.dx === 0) {
    snake.dx = grid;
    snake.dy = 0;
  }
  // touche flèche bas
  else if (e.which === 40 && snake.dy === 0) {
    snake.dy = grid;
    snake.dx = 0;
  }
});

// démarrer le jeu
requestAnimationFrame(loop);
</script>