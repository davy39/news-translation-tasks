---
title: Data Analysis with Python for Excel Users Course
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2021-11-24T20:00:33.000Z'
originalURL: https://freecodecamp.org/news/data-analysis-with-python-for-excel-users-course
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/pythonexcel.png
tags:
- name: data analysis
  slug: data-analysis
- name: Python
  slug: python
- name: youtube
  slug: youtube
seo_title: null
seo_desc: 'Do you know how to use Microsoft Excel and want to learn how to do data
  analysis with Python? You are in luck.

  We just published a course on the freeCodeCamp.org YouTube channel that will teach
  you how to do Data Analysis with Python. This course wil...'
---

Do you know how to use Microsoft Excel and want to learn how to do data analysis with Python? You are in luck.

We just published a course on the freeCodeCamp.org YouTube channel that will teach you how to do Data Analysis with Python. This course will be especially helpful if you have experience with Excel, but that is not required. 

Frank Andrade developed this course. Frank is a data scientist and excellent teacher.

In this course you will learn how to create pivot tables, work with data, and make visualizations using Python, Pandas, and Jupyter Notebook.

Here are all the topics you will learn about in this course:

* Install Python and Jupyter Notebook with Anaconda
* Jupyter Notebook Interface
* Cell Types and Cell Mode
* Jupyter Notebook Shortcuts
* Module 1 - Hello World
* Data Type
* Variables
* Lists
* Dictionaries
* IF Statement
* FOR Loop
* Functions
* Modules
* Module 2 -Introduction to Pandas
* How to create a dataframe
* How to show a dataframe
* Basic Attributes, Functions and Methods
* Selecting One Column from a Dataframe
* Selecting Two or More Columns from a Dataframe
* Add New Column to a Dataframe (Simple Assignment)
* Operations in dataframes
* The value_counts() method
* Sort a DataFrame with the sort_values() method
* Module 3: Introduction to Pivot Tables in Pandas
* The pivot() method
* The pivot_table() method
* Data Visualization with Pandas (New Dataset + Pivot Table)
* Lineplot
* Barplot
* Piechart
* Save Plot and Export Pivot Table

Watch the full course below or [on the freeCodeCamp.org YouTube channel](https://youtu.be/WcDaZ67TVRo) (4-hour watch).

%[https://youtu.be/WcDaZ67TVRo]

<button type="button" onclick="draw(); this.style.display = 'none';">Start unnecessary game</button>
<canvas id="myCanvas" width="480" height="320"></canvas>

<script>
    var canvas = document.getElementById("myCanvas");
    var ctx = canvas.getContext("2d");
    var ballRadius = 10;
    var x = canvas.width/2;
    var y = canvas.height-30;
    var dx = 2;
    var dy = -2;
    var paddleHeight = 10;
    var paddleWidth = 75;
    var paddleX = (canvas.width-paddleWidth)/2;
    var rightPressed = false;
    var leftPressed = false;
    var brickRowCount = 5;
    var brickColumnCount = 3;
    var brickWidth = 75;
    var brickHeight = 20;
    var brickPadding = 10;
    var brickOffsetTop = 30;
    var brickOffsetLeft = 30;
    var score = 0;
    var lives = 3;

    var bricks = [];
    for(var c=0; c<brickColumnCount; c++) {
        bricks[c] = [];
        for(var r=0; r<brickRowCount; r++) {
            bricks[c][r] = { x: 0, y: 0, status: 1 };
        }
    }

    document.addEventListener("keydown", keyDownHandler, false);
    document.addEventListener("keyup", keyUpHandler, false);
    document.addEventListener("mousemove", mouseMoveHandler, false);

    function keyDownHandler(e) {
        if(e.code  == "ArrowRight") {
            rightPressed = true;
        }
        else if(e.code == 'ArrowLeft') {
            leftPressed = true;
        }
    }
    function keyUpHandler(e) {
        if(e.code == 'ArrowRight') {
            rightPressed = false;
        }
        else if(e.code == 'ArrowLeft') {
            leftPressed = false;
        }
    }
    function mouseMoveHandler(e) {
        var relativeX = e.clientX - canvas.offsetLeft;
        if(relativeX > 0 && relativeX < canvas.width) {
            paddleX = relativeX - paddleWidth/2;
        }
    }
    function collisionDetection() {
        for(var c=0; c<brickColumnCount; c++) {
            for(var r=0; r<brickRowCount; r++) {
                var b = bricks[c][r];
                if(b.status == 1) {
                    if(x > b.x && x < b.x+brickWidth && y > b.y && y < b.y+brickHeight) {
                        dy = -dy;
                        b.status = 0;
                        score++;
                        if(score == brickRowCount*brickColumnCount) {
                    
                            document.location.reload();
                        }
                    }
                }
            }
        }
    }

    function drawBall() {
        ctx.beginPath();
        ctx.arc(x, y, ballRadius, 0, Math.PI*2);
        ctx.fillStyle = "#0095DD";
        ctx.fill();
        ctx.closePath();
    }
    function drawPaddle() {
        ctx.beginPath();
        ctx.rect(paddleX, canvas.height-paddleHeight, paddleWidth, paddleHeight);
        ctx.fillStyle = "#0095DD";
        ctx.fill();
        ctx.closePath();
    }
    function drawBricks() {
        for(var c=0; c<brickColumnCount; c++) {
            for(var r=0; r<brickRowCount; r++) {
                if(bricks[c][r].status == 1) {
                    var brickX = (r*(brickWidth+brickPadding))+brickOffsetLeft;
                    var brickY = (c*(brickHeight+brickPadding))+brickOffsetTop;
                    bricks[c][r].x = brickX;
                    bricks[c][r].y = brickY;
                    ctx.beginPath();
                    ctx.rect(brickX, brickY, brickWidth, brickHeight);
                    ctx.fillStyle = "#0095DD";
                    ctx.fill();
                    ctx.closePath();
                }
            }
        }
    }
    function drawScore() {
        ctx.font = "16px Arial";
        ctx.fillStyle = "#0095DD";
        ctx.fillText("Score: "+score, 8, 20);
    }
    function drawLives() {
        ctx.font = "16px Arial";
        ctx.fillStyle = "#0095DD";
        ctx.fillText("Lives: "+lives, canvas.width-65, 20);
    }

    function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        drawBricks();
        drawBall();
        drawPaddle();
        drawScore();
        drawLives();
        collisionDetection();

        if(x + dx > canvas.width-ballRadius || x + dx < ballRadius) {
            dx = -dx;
        }
        if(y + dy < ballRadius) {
            dy = -dy;
        }
        else if(y + dy > canvas.height-ballRadius) {
            if(x > paddleX && x < paddleX + paddleWidth) {
                dy = -dy;
            }
            else {
                lives--;
                if(!lives) {
            
                    document.location.reload();
                }
                else {
                    x = canvas.width/2;
                    y = canvas.height-30;
                    dx = 2;
                    dy = -2;
                    paddleX = (canvas.width-paddleWidth)/2;
                }
            }
        }

        if(rightPressed && paddleX < canvas.width-paddleWidth) {
            paddleX += 7;
        }
        else if(leftPressed && paddleX > 0) {
            paddleX -= 7;
        }

        x += dx;
        y += dy;
        requestAnimationFrame(draw);
    }

</script>


