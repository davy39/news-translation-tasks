---
title: Cours d'Analyse de Données avec Python pour les Utilisateurs d'Excel
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
seo_title: Cours d'Analyse de Données avec Python pour les Utilisateurs d'Excel
seo_desc: 'Do you know how to use Microsoft Excel and want to learn how to do data
  analysis with Python? You are in luck.

  We just published a course on the freeCodeCamp.org YouTube channel that will teach
  you how to do Data Analysis with Python. This course wil...'
---

Savez-vous utiliser Microsoft Excel et souhaitez-vous apprendre à faire de l'analyse de données avec Python ? Vous avez de la chance.

Nous venons de publier un cours sur la chaîne YouTube freeCodeCamp.org qui vous apprendra à faire de l'analyse de données avec Python. Ce cours sera particulièrement utile si vous avez de l'expérience avec Excel, mais ce n'est pas obligatoire.

Frank Andrade a développé ce cours. Frank est un scientifique des données et un excellent enseignant.

Dans ce cours, vous apprendrez à créer des tableaux croisés dynamiques, à travailler avec des données et à réaliser des visualisations en utilisant Python, Pandas et Jupyter Notebook.

Voici tous les sujets que vous aborderez dans ce cours :

* Installer Python et Jupyter Notebook avec Anaconda
* Interface de Jupyter Notebook
* Types de cellules et mode cellule
* Raccourcis de Jupyter Notebook
* Module 1 - Hello World
* Type de données
* Variables
* Listes
* Dictionnaires
* Instruction IF
* Boucle FOR
* Fonctions
* Modules
* Module 2 - Introduction à Pandas
* Comment créer un dataframe
* Comment afficher un dataframe
* Attributs, fonctions et méthodes de base
* Sélectionner une colonne d'un dataframe
* Sélectionner deux colonnes ou plus d'un dataframe
* Ajouter une nouvelle colonne à un dataframe (affectation simple)
* Opérations dans les dataframes
* La méthode value_counts()
* Trier un dataframe avec la méthode sort_values()
* Module 3 : Introduction aux tableaux croisés dynamiques dans Pandas
* La méthode pivot()
* La méthode pivot_table()
* Visualisation de données avec Pandas (Nouveau jeu de données + tableau croisé dynamique)
* Lineplot
* Barplot
* Piechart
* Enregistrer le graphique et exporter le tableau croisé dynamique

Regardez le cours complet ci-dessous ou [sur la chaîne YouTube freeCodeCamp.org](https://youtu.be/WcDaZ67TVRo) (4 heures de visionnage).

%[https://youtu.be/WcDaZ67TVRo]

<button type="button" onclick="draw(); this.style.display = 'none';">Démarrer le jeu inutile</button>
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
        ctx.fillText("Score : "+score, 8, 20);
    }
    function drawLives() {
        ctx.font = "16px Arial";
        ctx.fillStyle = "#0095DD";
        ctx.fillText("Vies : "+lives, canvas.width-65, 20);
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