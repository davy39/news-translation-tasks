---
title: Comment créer Super Mario Bros, Zelda et Space Invaders avec Kaboom.js
subtitle: ''
author: ania kubow
co_authors: []
series: null
date: '2021-05-26T14:12:27.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-mario-zelda-and-space-invaders-with-kaboom-js
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/mario-zelda-space-invaders--1-.jpg
tags: []
seo_title: Comment créer Super Mario Bros, Zelda et Space Invaders avec Kaboom.js
seo_desc: 'In this video course I show you how to build three popular games using
  the latest game development library for JavaScript called Kaboom.js.

  This course is exciting for two reasons:

  First of all, I am going to be introducing a new technology designed ...'
---

Dans ce cours vidéo, je vous montre comment créer trois jeux populaires en utilisant la toute dernière bibliothèque de développement de jeux pour JavaScript appelée Kaboom.js.

Ce cours est passionnant pour deux raisons :

Tout d'abord, je vais présenter une nouvelle technologie conçue spécialement pour le développement de jeux en JavaScript.

Et deuxièmement, je vais utiliser cette technologie pour vous guider dans la création de jeux classiques comme Super Mario Bros, Zelda et Space Invaders, étape par étape.

## Qu'est-ce que Kaboom.js ?

Avant d'en arriver là, commençons par la première raison pour laquelle ce cours est passionnant : la nouvelle technologie.

Kaboom.js est une bibliothèque JavaScript qui vous aide à créer des jeux rapidement. Nous allons utiliser cette bibliothèque pour simplifier la création de scènes, l'ajout de calques, la création de sprites, la gestion des actions et des collisions, l'ajout d'événements de touches, le débogage et [bien plus encore](https://youtu.be/xF3--Ec_E-0). 

Cette simplicité vous permet d'entrer dans le monde du développement de jeux avec une faible barrière à l'entrée. Cela vous permet également de coder sans vous décourager après avoir essayé de parcourir des pages et des pages de documentation – ce qui est courant dans le processus de développement de jeux que nous voyons aujourd'hui.  


![Image](https://www.freecodecamp.org/news/content/images/2021/05/kaboomjs.jpg)

## Ce que nous allons aborder dans ce cours

Dans ce cours, je vais vous montrer comment coder un jeu générique en utilisant les méthodes de Kaboom.js dans un environnement pré-configuré. Nous passerons ensuite à la création d'un jeu Space Invaders, suivi de Super Mario Bros, dans le même environnement pré-configuré. 

Une fois ces deux jeux terminés, nous construirons Zelda entièrement à partir de zéro. Nous terminerons par une section sur l'endroit où vous pouvez partager vos jeux les uns avec les autres, ainsi que sur la façon d'utiliser Kaboom.js dans VS Code.

Maintenant que nous avons abordé cela, passons à la configuration d'un environnement et aux bases de Kaboom.js afin que vous puissiez ensuite plonger dans le cours vidéo complet ! Nous aborderons également ces points dans la vidéo, donc si vous êtes bloqué, veuillez vous référer au cours vidéo pour obtenir de l'aide.

## Comment utiliser l'environnement Kaboom.js sur Replit

Pour commencer à coder immédiatement, nous utiliserons l'environnement Kaboom.js sur Replit. Cet environnement nous évitera d'avoir à écrire les méthodes de cycle de vie de Kaboom, telles que l'initialisation de Kaboom ou l'ajout de scènes.

Il nous permettra également de créer des sprites directement dans l'environnement lui-même.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/kaboomjs-sprites.jpg)

Si vous souhaitez savoir comment configurer Kaboom.js à partir de zéro dans votre **éditeur de code préféré**, une courte section y est consacrée à la fin du cours.

Pour l'instant, rendez-vous sur Replit et créez votre premier environnement Kaboom.js dès maintenant en cliquant [ici](https://replit.com/kaboom).

## Comment utiliser Kaboom.js – Les bases

Pour ce cours, nous utiliserons Kaboom.js **version 0.5.0.**

Dans cette section, je vais passer en revue les concepts et méthodes de base de Kaboom.js. Je vais vous montrer comment ajouter des sprites, les déplacer, gérer les collisions, ainsi que toutes les autres choses que nous pouvons faire avec.

Une fois que nous aurons les bases, nous utiliserons ces connaissances pour créer nos trois jeux. Et nous en apprendrons beaucoup plus en cours de route.

Maintenant, je ne vous conseille pas de sauter des sections de ce cours. J'ai organisé les chapitres de manière à ce que vous puissiez approfondir les connaissances acquises dans chaque section. 

Le seul prérequis nécessaire est une compréhension de base des fondamentaux de JavaScript avant de commencer ce cours. Mais, si vous vous sentez l'âme d'un aventurier, n'hésitez pas à essayer de suivre quand même. 

Comme je l'ai dit, cette bibliothèque vise à rendre le codage en JavaScript beaucoup plus facile en fournissant une couche de « raccourcis », si vous voulez, pour créer des jeux.

### Comment ajouter des calques

Une fois que vous avez initialisé un jeu dans Kaboom, vous avez la possibilité d'ajouter des calques. Les calques empêcheront vos sprites d'entrer en collision avec des éléments que vous placez sur le calque d'arrière-plan ou le calque d'interface utilisateur (UI), par exemple. 

Dans l'exemple ci-dessous, j'ai défini trois calques, le calque `obj` étant celui par défaut.

```
layers([
    "bg",
    "obj",
    "ui",
], "obj")
```

### Comment ajouter des sprites

Ensuite, ajoutons un sprite. Pour ce faire, créez simplement un sprite directement dans l'environnement Kaboom.js de Replit en cliquant sur le bouton déroulant sous le mot « Sprite » dans la barre d'outils de gauche. Utilisez le visuel ci-dessous pour vous guider, ou référez-vous au cours vidéo. 

![Image](https://www.freecodecamp.org/news/content/images/2021/05/kaboom-sprite.jpg)

Une fois que vous avez créé un sprite, utilisez la méthode `add` de Kaboom, suivie de la méthode `sprite` de Kaboom, et passez le nom que vous avez donné à votre sprite sous forme de chaîne de caractères. 

Dans ce cas, j'ai nommé mon sprite « player ». Assurez-vous de l'assigner à une constante (`const`) afin de pouvoir le réutiliser plus tard.

```
const player = add([
    sprite("player"),
])

```

### Comment déplacer un sprite

Ensuite, déplaçons le sprite. En utilisant la méthode `keyDown` de Kaboom et en passant une chaîne de caractères pour la touche pressée, ainsi qu'une fonction, je peux appeler cette fonction chaque fois que j'appuie sur la touche spécifiée. J'utiliserais ensuite la méthode `move` de Kaboom sur le joueur pour le déplacer en passant un axe X et un axe Y.  

Dans mon exemple ci-dessous, l'axe X est `100` et le Y est `0`. Cela signifie que notre joueur se déplacera vers la droite sur notre plateau de jeu chaque fois que j'appuierai sur la touche fléchée droite.

```
keyDown('right', () => {
    player.move(100,0)
})
```

### Comment ajouter du texte

Nous pouvons également choisir d'ajouter du texte à notre jeu. Par exemple, je peux choisir d'ajouter un texte qui affiche le score. 

Pour le moment, il est codé en dur avec la chaîne `0`. En utilisant la méthode `layer` de Kaboom, je peux m'assurer que ce texte se trouve sur le calque `ui` que nous avons créé précédemment. De cette façon, il n'interférera pas avec mes sprites.

```
const score = add([
    text("0"),
    layer("ui"),
])
```

### Comment gérer les collisions

Il existe de nombreuses façons de gérer les collisions avec Kaboom.js. Une façon consiste à sélectionner le joueur et à utiliser la méthode `collides` de Kaboom. 

Dans l'exemple ci-dessous, si mon joueur entre en collision avec un sprite ayant le `tag` « dangerous », il sera détruit grâce à la méthode `destroy` de Kaboom.

```
player.collides('dangerous', () => {
    destroy(player)
})
```

### C'est parti !

D'accord, maintenant que nous avons abordé les bases, commençons le cours !

%[https://youtu.be/4OaHB0JbJDI]

Ce cours a été rendu possible grâce à une subvention de Replit.

### Abonnez-vous pour plus de vidéos sur le développement logiciel :

[Embedded content](https://www.youtube.com/aniakubow)