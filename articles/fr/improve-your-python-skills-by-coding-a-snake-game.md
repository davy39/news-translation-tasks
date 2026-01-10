---
title: Améliorez vos compétences en Python en codant un jeu de serpent
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2021-04-08T18:49:30.000Z'
originalURL: https://freecodecamp.org/news/improve-your-python-skills-by-coding-a-snake-game
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/snakeeng.png
tags:
- name: Python
  slug: python
- name: youtube
  slug: youtube
seo_title: Améliorez vos compétences en Python en codant un jeu de serpent
seo_desc: 'Snakes like to eat apples. At least in the game you are about to code.

  We just published a course on the freeCodeCamp.org YouTube channel that will teach
  you how to create a snake game using Python and Pygame.

  This course was developed by Dhaval Pate...'
---

Les serpents aiment manger des pommes. Au moins dans le jeu que vous allez coder.

Nous venons de publier un cours sur la chaîne YouTube freeCodeCamp.org qui vous apprendra à créer un jeu de serpent en utilisant Python et Pygame.

Ce cours a été développé par Dhaval Patel de la chaîne YouTube populaire codebasics.

Ce cours est pour les débutants. Tout ce que vous devez savoir est le Python de base. Vous apprendrez à construire un projet complet de bout en bout en Python.

Voici les sections de ce cours :

* Créer la surface de jeu
* Conversion en POO
* Déplacer le bloc avec un minuteur
* Dessiner le serpent et la pomme
* Le serpent mange la pomme et trouve le score
* Logique de fin de jeu
* Ajouter de la musique de fond et une image
* Convertir Python en .exe

Dhaval a créé ce cours en anglais et en hindi, et nous avons publié les deux ! Vous pouvez regarder la [version anglaise sur notre chaîne principale](https://www.youtube.com/watch?v=8dfePlONtls) et la [version hindi sur notre chaîne hindi](https://www.youtube.com/watch?v=k2zZp9Mbd8E&t=0s).

<style type="text/css">

canvas { border: 1px solid black;  }

</style>

    <canvas id="canvas" width="400" height="400"></canvas>

    <script>
      var canvas, ctx;

      window.onload = function() {
        canvas = document.getElementById("canvas");
        ctx = canvas.getContext("2d");

        document.addEventListener("keydown", keyDownEvent);

        // rendre X fois par seconde
        var x = 8;
        setInterval(draw, 1000 / x);
      };

      // monde du jeu
      var gridSize = (tileSize = 20); // 20 x 20 = 400
      var nextX = (nextY = 0);

      // serpent
      var defaultTailSize = 3;
      var tailSize = defaultTailSize;
      var snakeTrail = [];
      var snakeX = (snakeY = 10);

      // pomme
      var appleX = (appleY = 15);

      // dessiner
      function draw() {
        // déplacer le serpent à la position suivante
        snakeX += nextX;
        snakeY += nextY;

        // serpent hors du monde du jeu ?
        if (snakeX < 0) {
          snakeX = gridSize - 1;
        }
        if (snakeX > gridSize - 1) {
          snakeX = 0;
        }

        if (snakeY < 0) {
          snakeY = gridSize - 1;
        }
        if (snakeY > gridSize - 1) {
          snakeY = 0;
        }

        // le serpent mord la pomme ?
        if (snakeX == appleX && snakeY == appleY) {
          tailSize++;

          appleX = Math.floor(Math.random() * gridSize);
          appleY = Math.floor(Math.random() * gridSize);
        }

        // peindre l'arrière-plan
        ctx.fillStyle = "black";
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        // peindre le serpent
        ctx.fillStyle = "green";
        for (var i = 0; i < snakeTrail.length; i++) {
          ctx.fillRect(
            snakeTrail[i].x * tileSize,
            snakeTrail[i].y * tileSize,
            tileSize,
            tileSize
          );

          // le serpent se mord la queue ?
          if (snakeTrail[i].x == snakeX && snakeTrail[i].y == snakeY) {
            tailSize = defaultTailSize;
          }
        }

        // peindre la pomme
        ctx.fillStyle = "red";
        ctx.fillRect(appleX * tileSize, appleY * tileSize, tileSize, tileSize);

        // définir la trace du serpent
        snakeTrail.push({ x: snakeX, y: snakeY });
        while (snakeTrail.length > tailSize) {
          snakeTrail.shift();
        }
      }

      // entrée
      function keyDownEvent(e) {
        switch (e.keyCode) {
          case 37:
            nextX = -1;
            nextY = 0;
            break;
          case 38:
            nextX = 0;
            nextY = -1;
            break;
          case 39:
            nextX = 1;
            nextY = 0;
            break;
          case 40:
            nextX = 0;
            nextY = 1;
            break;
        }
      }

</script>
<p style="text-align:center"><small>Utilisez les flèches pour jouer à ce jeu.</small></p>

Vous pouvez également regarder le cours complet de 90 minutes ci-dessous.

%[https://youtu.be/8dfePlONtls]