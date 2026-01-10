---
title: Improve Your Python Skills by Coding a Snake Game
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
seo_title: null
seo_desc: 'Snakes like to eat apples. At least in the game you are about to code.

  We just published a course on the freeCodeCamp.org YouTube channel that will teach
  you how to create a snake game using Python and Pygame.

  This course was developed by Dhaval Pate...'
---

Snakes like to eat apples. At least in the game you are about to code.

We just published a course on the freeCodeCamp.org YouTube channel that will teach you how to create a snake game using Python and Pygame.

This course was developed by Dhaval Patel from the popular codebasics YouTube channel. 

This course is for beginners. All you need to know is basic Python. You will learn to build a complete end-to-end project in Python.

Here are the sections in this course:

* Create the game surface
* Converting into OOP
* Moving block with timer
* Draw snake and apple
* Snake eats apple and find score
* Game over logic
* Add background music and image
* Convert python to .exe

Dhaval created this course in both English and Hindi—and we released both of them! You can watch the [English version on our main channel](https://www.youtube.com/watch?v=8dfePlONtls) and the [Hindi version on our Hindi channel](https://www.youtube.com/watch?v=k2zZp9Mbd8E&t=0s). 

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

        // render X times per second
        var x = 8;
        setInterval(draw, 1000 / x);
      };

      // game world
      var gridSize = (tileSize = 20); // 20 x 20 = 400
      var nextX = (nextY = 0);

      // snake
      var defaultTailSize = 3;
      var tailSize = defaultTailSize;
      var snakeTrail = [];
      var snakeX = (snakeY = 10);

      // apple
      var appleX = (appleY = 15);

      // draw
      function draw() {
        // move snake in next pos
        snakeX += nextX;
        snakeY += nextY;

        // snake over game world?
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

        //snake bite apple?
        if (snakeX == appleX && snakeY == appleY) {
          tailSize++;

          appleX = Math.floor(Math.random() * gridSize);
          appleY = Math.floor(Math.random() * gridSize);
        }

        //paint background
        ctx.fillStyle = "black";
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        // paint snake
        ctx.fillStyle = "green";
        for (var i = 0; i < snakeTrail.length; i++) {
          ctx.fillRect(
            snakeTrail[i].x * tileSize,
            snakeTrail[i].y * tileSize,
            tileSize,
            tileSize
          );

          //snake bites it's tail?
          if (snakeTrail[i].x == snakeX && snakeTrail[i].y == snakeY) {
            tailSize = defaultTailSize;
          }
        }

        // paint apple
        ctx.fillStyle = "red";
        ctx.fillRect(appleX * tileSize, appleY * tileSize, tileSize, tileSize);

        //set snake trail
        snakeTrail.push({ x: snakeX, y: snakeY });
        while (snakeTrail.length > tailSize) {
          snakeTrail.shift();
        }
      }

      // input
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
<p style="text-align:center"><small>Use arrows to play this game.</small></p>

You can also watch the full 90 minute course below.

%[https://youtu.be/8dfePlONtls]


