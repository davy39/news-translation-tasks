---
title: 'Unreal Engine Course: Create a 2D Snake Game'
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2020-09-09T18:00:33.000Z'
originalURL: https://freecodecamp.org/news/unreal-engine-course-create-a-2d-snake-game
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/2dsnake.png
tags: []
seo_title: null
seo_desc: 'Unreal Engine is one of the most popular game development platforms, and
  it''s completely free to use. When most people think of Unreal Engine, they think
  of 3D games. But you can also use it to build 2D games.

  We just released a full 3-hour Unreal En...'
---

Unreal Engine is one of the most popular game development platforms, and it's completely free to use. When most people think of Unreal Engine, they think of 3D games. But you can also use it to build 2D games.

We just released a full 3-hour Unreal Engine course on the freeCodeCamp.org YouTube channel that will teach you how to create a 2D Snake game. The course was created by game developer extraordinaire Fahir from Awesome Tuts.

In this tutorial, you'll build the classic game snake. A player can control the snake, pick up food, grow the snake, score points, and eventually crash and trigger a game over. There are also some simple animations for different events in the game.

You will learn how to use Blueprints to create the game. Blueprints is the visual scripting system inside Unreal Engine. It makes it quicker to get a game up and running. You hardly have to write any actual code to create the game.

There are sprites, textures, and flipbooks assets needed for this game. And they are all included via a download link.

After you finish creating the game in the tutorial, you can use the same assets to improve the game on your own, or to create a brand new game.

You can watch the [full course on the freeCodeCamp.org YouTube channel](https://youtu.be/CU3jeNzbzqU) (3 hour watch).

????

And if you want to get into the snake mood first, you can play a snake game below using your arrow keys. The game you create will be even cooler than this. ? ([Source](https://gist.github.com/straker/ff00b4b49669ad3dec890306d348adc4))


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
  
  // snake velocity. moves one grid length every frame in either the x or y direction
  dx: grid,
  dy: 0,
  
  // keep track of all grids the snake body occupies
  cells: [],
  
  // length of the snake. grows when eating an apple
  maxCells: 4
};
var apple = {
  x: 320,
  y: 320
};

// get random whole numbers in a specific range
// @see https://stackoverflow.com/a/1527820/2124254
function getRandomInt(min, max) {
  return Math.floor(Math.random() * (max - min)) + min;
}

// game loop
function loop() {
  requestAnimationFrame(loop);

  // slow game loop to 15 fps instead of 60 (60/15 = 4)
  if (++count < 4) {
    return;
  }

  count = 0;
  context.clearRect(0,0,canvas.width,canvas.height);

  // move snake by it's velocity
  snake.x += snake.dx;
  snake.y += snake.dy;

  // wrap snake position horizontally on edge of screen
  if (snake.x < 0) {
    snake.x = canvas.width - grid;
  }
  else if (snake.x >= canvas.width) {
    snake.x = 0;
  }
  
  // wrap snake position vertically on edge of screen
  if (snake.y < 0) {
    snake.y = canvas.height - grid;
  }
  else if (snake.y >= canvas.height) {
    snake.y = 0;
  }

  // keep track of where snake has been. front of the array is always the head
  snake.cells.unshift({x: snake.x, y: snake.y});

  // remove cells as we move away from them
  if (snake.cells.length > snake.maxCells) {
    snake.cells.pop();
  }

  // draw apple
  context.fillStyle = 'red';
  context.fillRect(apple.x, apple.y, grid-1, grid-1);

  // draw snake one cell at a time
  context.fillStyle = 'green';
  snake.cells.forEach(function(cell, index) {
    
    // drawing 1 px smaller than the grid creates a grid effect in the snake body so you can see how long it is
    context.fillRect(cell.x, cell.y, grid-1, grid-1);  

    // snake ate apple
    if (cell.x === apple.x && cell.y === apple.y) {
      snake.maxCells++;

      // canvas is 400x400 which is 25x25 grids 
      apple.x = getRandomInt(0, 25) * grid;
      apple.y = getRandomInt(0, 25) * grid;
    }

    // check collision with all cells after this one (modified bubble sort)
    for (var i = index + 1; i < snake.cells.length; i++) {
      
      // snake occupies same space as a body part. reset game
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

// listen to keyboard events to move the snake
document.addEventListener('keydown', function(e) {
  // prevent snake from backtracking on itself by checking that it's 
  // not already moving on the same axis (pressing left while moving
  // left won't do anything, and pressing right while moving left
  // shouldn't let you collide with your own body)
  
  // left arrow key
  if (e.which === 37 && snake.dx === 0) {
    snake.dx = -grid;
    snake.dy = 0;
  }
  // up arrow key
  else if (e.which === 38 && snake.dy === 0) {
    snake.dy = -grid;
    snake.dx = 0;
  }
  // right arrow key
  else if (e.which === 39 && snake.dx === 0) {
    snake.dx = grid;
    snake.dy = 0;
  }
  // down arrow key
  else if (e.which === 40 && snake.dy === 0) {
    snake.dy = grid;
    snake.dx = 0;
  }
});

// start the game
requestAnimationFrame(loop);
</script>


