---
title: Comment coder Pong en Python – un tutoriel étape par étape avec Turtle
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-02-20T21:01:47.000Z'
originalURL: https://freecodecamp.org/news/how-to-code-pong-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/Brown-Colorful-Mental-Health-Blog-Banner--2-.png
tags:
- name: Game Development
  slug: game-development
- name: Python
  slug: python
seo_title: Comment coder Pong en Python – un tutoriel étape par étape avec Turtle
seo_desc: "By Shane Duggan\nPong is a classic video game that has stood the test of\
  \ time. It's a crowd favorite that many among you might recognise. \nFor the programmers\
  \ out there, coding Pong in Python is a fun and challenging way to learn the language\
  \ and basi..."
---

Par Shane Duggan

Pong est un jeu vidéo classique qui a résisté à l'épreuve du temps. C'est un favori du public que beaucoup d'entre vous pourraient reconnaître. 

Pour les programmeurs, coder Pong en Python est une manière amusante et stimulante d'apprendre le langage et les concepts de base du développement de jeux.

Mais il peut être intimidant de penser à la manière dont tous les composants s'assemblent pour former un jeu cohérent et interactif, surtout pour les programmeurs débutants.

Eh bien, ne vous inquiétez pas, car c'est là que ce tutoriel étape par étape entre en jeu.

En utilisant le module Turtle, je vais vous guider à travers le processus de codage de Pong en Python, de la configuration de votre environnement de développement à la mise en œuvre des mécaniques du jeu. Ce sera une excellente mention dans votre portfolio de projets, et une excellente manière de tester vos compétences en Python, quel que soit votre niveau de programmation jusqu'à présent. 

Le meilleur, c'est que vous pourrez jouer au jeu contre vos amis ou votre famille, car nous allons le mettre en œuvre comme un jeu joueur contre joueur.

**Alors, prenez votre ordinateur ou votre portable et commençons à coder !**

![Image](https://www.freecodecamp.org/news/content/images/2023/02/PongGIF.gif)
_Ce que nous allons programmer aujourd'hui_

## De quoi ai-je besoin pour coder Pong en Python ?

Avant de plonger dans le tutoriel, assurons-nous que vous avez tout ce dont vous avez besoin pour commencer. Tout d'abord, vous aurez besoin d'un ordinateur avec Python installé. Je recommande d'utiliser Python 3, car c'est la version la plus à jour du langage. 

Vous aurez également besoin d'un éditeur de texte ou d'un environnement de développement intégré (IDE) pour écrire et modifier votre code. Certaines options populaires pour Python incluent PyCharm, IDLE et Visual Studio Code. 

Personnellement, j'utilise Visual Studio Code car je trouve qu'il a de nombreuses intégrations et fonctionnalités utiles. Je vais compléter ce tutoriel avec celui-ci.

De plus, vous aurez besoin du module Turtle, qui est une bibliothèque intégrée en Python qui vous permet de créer des graphiques et de dessiner des formes à l'écran. 

Si vous avez des connaissances préalables en [Théorie des Jeux](https://shaneduggan.com/best-books-about-game-theory), c'est génial et cela vous aidera certainement et s'appliquera bien dans ce guide. Mais ne vous inquiétez pas si vous n'avez aucune connaissance préalable – ce tutoriel vous guidera à travers tout ce que vous devez savoir pour lancer votre premier jeu.

Et si vous n'êtes pas familier avec ces outils ou concepts, je vous couvre. Je vais passer par le processus d'installation et de configuration plus en détail dans la section suivante également.

## Qu'est-ce que le module Turtle ?

Le [module Turtle](https://docs.python.org/3/library/turtle.html) est une bibliothèque intégrée en Python qui vous permet de créer des graphiques et de dessiner des formes à l'écran. Il est nommé d'après le système de graphiques turtle développé par Seymour Papert dans les années 1960, qui était conçu pour enseigner les bases de la programmation aux jeunes enfants. 

Le module Turtle fournit une interface simple pour dessiner des lignes et des formes en utilisant un curseur, ou "turtle", qui peut être déplacé autour de l'écran en utilisant des commandes comme forward, backward, left et right. Vous pouvez également personnaliser la turtle avec différentes couleurs, stylos et formes, et vous pouvez utiliser des boucles et des conditionnelles pour créer des designs plus complexes.

L'un des principaux avantages du module Turtle est qu'il est facile à apprendre et à utiliser, ce qui en fait un excellent outil pour les débutants qui sont nouveaux en programmation. Il vous permet de créer rapidement des sorties visuelles et de voir les résultats de votre code, ce qui peut être une manière amusante et engageante d'apprendre les concepts de programmation. 

De plus, vous pouvez utiliser le module Turtle pour créer une large gamme de graphiques et d'animations, des formes et motifs simples aux jeux et simulations complexes.

En raison de sa facilité d'utilisation, nous allons l'utiliser dans ce guide pour vous faire démarrer avec votre jeu Pong en Python dès que possible.

## Quelles sont les étapes pour coder Pong ?

Maintenant que vous avez une compréhension de base du module Turtle et de ce dont vous avez besoin pour commencer, il est temps de commencer à coder Pong en Python. 

Ci-dessous, j'ai décrit les étapes que vous devrez suivre afin de créer votre propre version de Pong. Ces étapes sont conçues pour être faciles à suivre et vous guideront à travers le processus de configuration de votre environnement de développement, de conception du jeu et de mise en œuvre des mécaniques du jeu. Commençons !

* **Étape 1 :** Configurer votre environnement de développement
* **Étape 2 :** Concevoir votre jeu
* **Étape 3 :** Mettre en œuvre les mécaniques du jeu
* **Étape 4 :** Ajouter des fonctionnalités supplémentaires et des personnalisations
* **Étape 5 :** Tester et déboguer votre code

## Comment configurer votre environnement de développement

La première étape pour coder Pong en Python est de configurer votre environnement de développement. Cela inclut l'installation de Python, l'installation d'un éditeur de texte ou d'un environnement de développement intégré (IDE), et l'installation du module Turtle. 

Si vous utilisez Visual Studio Code (VS Code) comme IDE, voici ce que vous devez faire :

* **Installer Python :** Si vous n'avez pas déjà Python installé sur votre ordinateur, vous devrez le télécharger et l'installer. Je recommande d'utiliser Python 3, car c'est la version la plus à jour du langage. Vous pouvez télécharger Python depuis le site officiel ou via le marketplace de VS Code.
* **Installer VS Code (ou tout autre éditeur de texte/IDE avec lequel vous êtes à l'aise) :** Une fois que vous avez installé Python, vous devrez télécharger et installer VS Code. Vous pouvez télécharger VS Code depuis le site officiel ou via le site de Python.
* **Installer le module Turtle :** Le module Turtle est une bibliothèque intégrée en Python qui vous permet de créer des graphiques et de dessiner des formes à l'écran. Pour installer le module Turtle, vous devrez ouvrir une fenêtre de terminal dans VS Code et entrer la commande suivante pour installer le module turtle :

```bash
pip install turtle
```

Une fois que vous avez terminé ces étapes, vous êtes prêt à commencer à coder Pong en Python en utilisant le module Turtle et VS Code. Dans l'étape suivante, nous discuterons de la manière de concevoir votre jeu et de créer un plan de jeu.

## Comment concevoir votre jeu

Maintenant que vous avez configuré votre environnement de développement, il est temps de commencer à concevoir votre jeu de Pong. Cette étape consiste à créer un plan de jeu et à déterminer les mécaniques de base de votre jeu.

Pour commencer, vous devez décider de la taille et de la disposition de votre écran de jeu. Le module Turtle vous permet de créer un écran avec une largeur et une hauteur spécifiques, et vous pouvez utiliser la fonction "setup" pour définir ces valeurs.

Vous devrez décider des éléments de jeu que vous souhaitez inclure dans votre jeu. Dans un jeu de Pong de base, vous aurez besoin d'au moins deux raquettes (une pour chaque joueur) et d'une balle. 

Vous pouvez créer ces éléments en utilisant la fonction "Turtle" du module Turtle, qui vous permet de créer un nouvel objet turtle avec une forme et une couleur spécifiques. 

Pour créer la balle pour votre jeu, vous pouvez utiliser la fonction "Turtle" du module Turtle et définir la forme sur "circle" et la couleur sur "white".

Vous pouvez facilement créer ces éléments avec le module Turtle comme montré ci-dessous :

```python
# Création de la balle
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
```

D'autres éléments incluent un tableau de score, une couleur de fond et un style de jeu. Nous devons également créer un ensemble de règles pour régir le déroulement du jeu. 

J'ai inclus un tableau ci-dessous pour que vous puissiez voir à quoi pourrait ressembler la configuration de base d'un jeu de Pong :

```python
import turtle

# Configuration de l'écran de jeu
turtle.setup(400, 300)
# Définir la couleur de fond de l'écran de jeu
turtle.bgcolor("black")
```

```python
paddle1 = turtle.Turtle()
paddle1.shape("square")
paddle1.color("red")
paddle1.shapesize(stretch_wid=5, stretch_len=1)  # rendre la raquette plus large
paddle1.penup()
paddle1.goto(-350, 0)
paddle1.dy = 0
```

```python
paddle2 = turtle.Turtle()
paddle2.shape("square")
paddle2.color("blue")
paddle2.shapesize(stretch_wid=5, stretch_len=1)
paddle2.penup()
paddle2.goto(350, 0)
paddle2.dy = 0
```

```python
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
```

```python
game_over = False
winner = None
points = {
    "player1": 0,
    "player2": 0
}
game_rules = {
    "max_points": 3,
    "ball_speed": 3
}
```

```python
score_display = turtle.Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Player 1: 0  Player 2: 0", align="center", font=("Arial", 24, "normal"))
```

Avec cela, vous devriez avoir tous les éléments du jeu configurés et prêts à passer à l'étape suivante de la mise en œuvre des mécaniques réelles du jeu.

## Comment implémenter les mécaniques du jeu

L'étape suivante dans la création de notre jeu de Pong consiste à configurer les mécaniques du jeu. Cela inclut la définition du mouvement de la balle, la collision de la balle avec les raquettes et les bords de l'écran, et le système de score.

Pour définir le mouvement de la balle, nous devrons mettre à jour les coordonnées x et y de l'objet turtle de la balle dans la boucle principale du jeu. Nous pouvons le faire en utilisant les fonctions **setx** et **sety**, et nous pouvons ajuster la vitesse de la balle en multipliant les valeurs **dx** et **dy** par un facteur constant.

Pour implémenter les mécaniques de collision du jeu, nous devrons vérifier la position de la balle par rapport aux raquettes et aux bords de l'écran. 

Si la balle entre en collision avec une raquette, nous devrons inverser la direction de la balle en multipliant la valeur dx par -1. Si la balle sort de l'écran, nous devrons réinitialiser la balle au centre de l'écran et mettre à jour le score.

Pour créer le système de score, nous devrons garder une trace des points pour chaque joueur. Nous pouvons le faire en créant un dictionnaire avec des clés pour chaque joueur et en mettant à jour les valeurs de ces clés chaque fois qu'un joueur marque. Nous pouvons ensuite afficher le score actuel à l'écran en utilisant la fonction **write** de l'objet turtle d'affichage du score.

En résumé, la logique de codage ressemble à ceci :

```python
paddle1.sety(paddle1.ycor() + paddle1.dy)
paddle2.sety(paddle2.ycor() + paddle2.dy)
ball.setx(ball.xcor() + ball.dx)
ball.sety(ball.ycor() + ball.dy)

# Vérifier les conditions de fin de jeu
if points["player1"] == game_rules["max_points"]:
    game_over = True
    winner = "player1"
elif points["player2"] == game_rules["max_points"]:
    game_over = True
    winner = "player2"

# Vérifier la collision de la balle avec les raquettes
if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle2.ycor() + 50 and ball.ycor() > paddle2.ycor() - 50):
    ball.setx(340)
    ball.dx *= -1
elif (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle1.ycor() + 50 and ball.ycor() > paddle1.ycor() - 50):
    ball.setx(-340)
    ball.dx *= -1

# Vérifier si la balle sort de l'écran
if ball.xcor() > 390:
    ball.goto(0, 0)
    ball.dx *= -1
    points["player1"] += 1
elif ball.xcor() < -390:
    ball.goto(0, 0)
    ball.dx *= -1
    points["player2"] += 1

# Vérifier si la balle entre en collision avec le haut ou le bas de l'écran
if ball.ycor() > 290:
    ball.sety(290)
    ball.dy *= -1
elif ball.ycor() < -290:
    ball.sety(-290)
    ball.dy *= -1

# Mettre à jour l'affichage du score
score_display.clear()
score_display.write("Player 1: {}  Player 2: {}".format(points["player1"], points["player2"]), align="center", font=("Arial", 24, "normal"))
```

## Comment ajouter des fonctionnalités supplémentaires et des personnalisations

Maintenant que nous avons les mécaniques de base du jeu en place, il est temps d'ajouter quelques fonctionnalités supplémentaires et des personnalisations pour rendre notre jeu de Pong encore plus amusant et engageant.

Une fonctionnalité simple que nous pouvons ajouter est la possibilité pour les joueurs de contrôler leurs raquettes en utilisant le clavier. 

Pour ce faire, nous devrons définir des fonctions pour déplacer les raquettes vers le haut et vers le bas, et lier ces fonctions à des touches spécifiques en utilisant la fonction **onkeypress** du module turtle.

Nous pouvons également ajouter des options de personnalisation pour rendre le jeu plus difficile ou personnalisé. Par exemple, nous pouvons permettre aux joueurs de choisir le nombre maximum de points nécessaires pour gagner le jeu, ou ajuster la vitesse de la balle pour rendre le jeu plus ou moins difficile. 

Nous pouvons également permettre aux joueurs de choisir les couleurs de leurs raquettes et de la balle, ou même ajouter différentes images de fond à l'écran de jeu (je recommande de tester différentes couleurs, [images de jeu](https://www.answeriq.com/ai-image-generators/), et esthétiques pour voir ce qui convient le mieux à votre style).

Pour ce tutoriel, j'ai créé des liaisons de touches et un écran de fin de jeu pour le jeu :

```python
# Fonction pour déplacer la raquette1 vers le haut
def paddle1_up():
    paddle1.dy = 10

# Fonction pour déplacer la raquette1 vers le bas
def paddle1_down():
    paddle1.dy = -10

# Fonction pour déplacer la raquette2 vers le haut
def paddle2_up():
    paddle2.dy = 10

# Fonction pour déplacer la raquette2 vers le bas
def paddle2_down():
    paddle2.dy = -10
```

```python
# Configurer les liaisons de touches
turtle.listen()
turtle.onkeypress(paddle1_up, "w")
turtle.onkeypress(paddle1_down, "s")
turtle.onkeypress(paddle2_up, "Up")
turtle.onkeypress(paddle2_down, "Down")
```

```python
# Écran de fin de jeu
game_over_display = turtle.Turtle()
game_over_display.color("white")
game_over_display.penup()
game_over_display.hideturtle()
game_over_display.goto(0, 0)
game_over_display.write("Game Over! {} wins!".format(winner), align="center", font=("Arial", 36, "normal"))
```

En ajoutant ces fonctionnalités supplémentaires et options de personnalisation, nous pouvons rendre notre jeu de Pong encore plus excitant et unique.

## Comment tester et déboguer votre code

Maintenant que nous avons toutes les pièces de notre jeu de Pong en place, il est temps de tester et déboguer notre code pour nous assurer que tout fonctionne comme prévu. 

C'est une étape importante dans le processus de développement, car elle nous permet de détecter toute erreur ou bug qui pourrait s'être glissé dans notre code.

Pour tester notre jeu, nous pouvons simplement exécuter le code et jouer quelques rounds pour voir si tout fonctionne correctement. En jouant, nous devons prêter attention au mouvement de la balle et des raquettes, aux mécaniques de collision et au système de score pour nous assurer qu'ils fonctionnent tous correctement.

Si nous rencontrons des erreurs ou des problèmes lors des tests, nous devrons déboguer notre code pour trouver la source du problème. Cela peut impliquer l'ajout de déclarations print pour nous aider à comprendre ce qui se passe à chaque étape de la boucle de jeu, ou l'utilisation des fonctionnalités de débogage intégrées de VS Code pour inspecter les variables et le flux de notre code.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-20-at-2.45.16-AM.png)
_Un simple jeu de Pong, jouez au jeu lui-même pour déboguer !_

## Comment passer votre jeu au niveau supérieur ?

Maintenant que vous avez une version de base du jeu en marche, vous vous demandez peut-être comment passer au niveau supérieur. Il existe plusieurs façons de le faire, selon vos objectifs et vos intérêts.

Une option consiste à ajouter des fonctionnalités et des mécaniques plus avancées au jeu. Par exemple, vous pourriez implémenter des bonus ou des capacités spéciales qui permettent aux joueurs de changer la vitesse ou la trajectoire de la balle, ou ajouter des mécaniques de collision plus complexes pour rendre le jeu plus difficile. 

Vous pourriez également incorporer une fonctionnalité multijoueur, permettant aux joueurs de rivaliser les uns contre les autres en ligne ou sur un réseau.

Une autre option consiste à se concentrer sur l'esthétique et l'expérience utilisateur du jeu. Vous pourriez ajouter des graphiques et des animations plus attrayants visuellement avec des [vidéos mises à l'échelle](https://neilchasefilm.com/ai-video-upscaling/), ou créer un paysage sonore plus immersif et engageant.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Purple-Modern-Gaming-Background-Futuristic-Game-Zone-Desktop-Wallpaper.png)
_Idées pour améliorer les graphismes de Pong (si vous en avez envie)_

Vous pourriez également travailler sur l'interface utilisateur, la rendant plus intuitive et conviviale pour les joueurs. 

Il est possible d'héberger votre jeu sur un site web. Puisque cet article est pour les débutants, la manière la plus simple de mettre votre jeu en ligne et prêt à être joué est simplement de l'héberger via un site WordPress et via la [gestion de snippets de code](https://hellodavelin.com/code-snippet-plugin). 

En termes simples, vous utilisez une intégration front-end sur WordPress à laquelle vous pouvez exécuter votre backend vers votre script Python.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-20-at-2.45.40-AM.png)
_Rendez votre page de fin de jeu plus excitante que cela avec quelques graphismes !_

Avec toutes ces additions, vous pouvez créer une expérience plus excitante et engageante pour les joueurs. 

Que vous cherchiez à ajouter des mécaniques plus avancées ou à vous concentrer sur l'esthétique du jeu, il existe de nombreuses façons de faire passer vos compétences en développement de jeux au niveau supérieur !

## Conclusion et fin

Dans ce tutoriel, nous avons couvert toutes les étapes nécessaires pour créer un jeu de Pong entièrement fonctionnel en Python en utilisant le module Turtle. 

Vous avez appris comment configurer l'écran de jeu, créer les éléments du jeu (raquettes et balles), définir les mécaniques du jeu et ajouter des fonctionnalités supplémentaires et des options de personnalisation. Nous avons également couvert comment tester et déboguer votre code pour vous assurer que tout fonctionne comme prévu.

En suivant ces étapes, vous devriez maintenant avoir une base solide en développement de jeux avec Python et le module Turtle. Utilisez ces compétences pour créer des jeux uniques et excitants ou faites passer vos compétences en développement de jeux à un niveau supérieur en ajoutant des fonctionnalités et des mécaniques plus avancées.

Coder un jeu de Pong en Python avec le module Turtle est une excellente manière d'apprendre le langage et le développement de jeux de manière amusante et pratique. J'espère que vous avez apprécié ce tutoriel et vous souhaite bonne chance dans votre parcours de développement de jeux !