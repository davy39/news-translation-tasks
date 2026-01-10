---
title: 'Une introduction à l''art génératif : qu''est-ce que c''est et comment en
  créer'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-03T15:04:17.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-generative-art-what-it-is-and-how-you-make-it-b0b363b50a70
coverImage: https://cdn-media-1.freecodecamp.org/images/0*JPekOSiNoJpvFeDP.png
tags:
- name: Art
  slug: art
- name: creativity
  slug: creativity
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: 'Une introduction à l''art génératif : qu''est-ce que c''est et comment
  en créer'
seo_desc: 'By Ali Spittel

  Generative art can be an intimidating topic — it seems like there is a lot of math
  involved, and art is tricky in itself!

  But, it doesn’t have to be difficult — you can build some really cool things without
  a math or art degree. This p...'
---

Par Ali Spittel

L'art génératif peut être un sujet intimidant — il semble qu'il y ait beaucoup de maths impliquées, et l'art en lui-même est délicat !

Mais cela n'a pas à être difficile — vous pouvez créer des choses vraiment cool sans diplôme en maths ou en art. Cet article va décomposer ce qu'est vraiment l'art génératif et comment vous pouvez commencer à créer votre propre art génératif.

### D'abord, qu'est-ce que l'art par code ?

L'art par code est toute œuvre d'art créée à l'aide de code. Il existe d'innombrables exemples sur CodePen — par exemple [l'art CSS](https://dev.to/aspittel/learning-css-through-creating-art-54c0).

### Qu'est-ce que l'art génératif ?

Souvent, l'art génératif s'inspire de l'art moderne, en particulier du pop art qui utilise abondamment des motifs géométriques ordonnés.

Cependant, c'est une catégorie très large et riche d'art créé avec du code avec une caractéristique centrale. L'art génératif intègre un système autonome ou auto-géré d'une certaine manière.

L'aléatoire est un type de système autonome. En incorporant le hasard dans une œuvre d'art codée, vous obtenez une œuvre d'art différente et complètement unique à chaque fois que vous exécutez votre script, chargez votre page ou répondez à une interaction utilisateur.

Il existe également des systèmes autonomes plus ordonnés. Un exemple est le fractal de Mandelbrot, dérivé d'une équation simple en apparence.

Nous pouvons également intégrer les deux approches, mélangeant ordre et chaos !

L'œuvre d'art devient une collaboration entre l'ordinateur et l'artiste. Certains aspects de l'œuvre sont contrôlés par le codeur, mais pas tous. L'artiste contrôle à la fois l'aléatoire et l'ordre dans l'art.

D'une certaine manière, avec un système autonome, l'artiste renonce au contrôle de son art, et l'ordinateur le fait pour lui. Une perspective plus nuancée émerge lorsqu'un nouveau processus créatif est considéré.

Le codeur-artiste s'engage dans une boucle de rétroaction où il ajuste constamment un système pour produire des résultats plus désirables et souvent plus surprenants.

Ce processus embrasse l'expérimentation et les heureux hasards d'une manière qui redéfinit le rôle de l'artiste. En tant qu'artistes génératifs, nous utilisons les bases du code comme les boucles, le contrôle de flux et des fonctions spécialisées. Nous les mélangeons ensuite avec des forces souvent imprévisibles, pour produire des résultats complètement uniques, différents de tout ce qui existe.

### Exemples d'art génératif

[Les fleurs de Kate Compton](http://www.galaxykate.com/apps/Prototypes/LTrees/)

[Automates cellulaires et le bord du chaos](http://math.hws.edu/eck/js/edge-of-chaos/CA.html)

#### Art génératif animé multicolore par Phil Nash

#### Taches impressionnistes par Murasaki Uma

#### Arbre généré par Miriam Nadler

### Qu'est-ce qui compose une œuvre d'art génératif ?

* **L'aléatoire** est crucial pour créer de l'art génératif. L'art doit être différent à chaque fois que vous exécutez le script de génération, donc l'aléatoire en fait généralement une grande partie.
* **Les algorithmes** — Implémenter un algorithme visuellement peut souvent générer des œuvres d'art impressionnantes, par exemple, l'arbre binaire ci-dessus.
* **La géométrie** — La plupart des œuvres d'art génératif incorporent des formes, et les maths de la géométrie du lycée peuvent aider à créer des effets vraiment cool.

### Comment aborder une œuvre d'art génératif ?

Il existe deux stratégies principales pour créer de l'art génératif, bien que la plupart se situent entre ces deux stratégies.

La première consiste à ne pas avoir de résultats en tête et à voir ce que l'ordinateur génère pendant que vous jouez.

La seconde est que vous avez une idée très finalisée de ce à quoi vous voulez que l'art ressemble, et l'aléatoire ne change que légèrement le résultat final.

### Par où commencer ?

Si vous connaissez JavaScript, [p5.js](https://p5js.org/) est un excellent point de départ. Son objectif est de "rendre le codage accessible aux artistes, designers, éducateurs et débutants". C'est une surcouche de l'[API Canvas](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API), et elle simplifie beaucoup de maths. Elle se concentre sur le dessin, mais vous pouvez également faire du son, de la vidéo ou de l'interaction avec la webcam si vous êtes intéressé par ces formes d'art !

#### Une brève introduction à P5

Tout d'abord, chargez le [CDN de p5](https://cdnjs.cloudflare.com/ajax/libs/p5.js/0.7.2/p5.js). Ensuite, dans votre fichier JavaScript, vous ajouterez deux fonctions qui seront utilisées dans presque tous les scripts p5 : `setup` et `draw`. Ces noms sont nécessaires pour que p5 puisse les appeler.

`setup` est appelé lorsque le programme démarre. Vous créerez probablement un canevas pour dessiner dessus en utilisant la fonction `createCanvas`, et vous pourrez y définir certains paramètres par défaut. Il n'est appelé qu'une seule fois !

`draw` est appelé après `setup` et est exécuté constamment jusqu'à ce que vous appeliez `noLoop`, ce qui l'empêchera de s'exécuter à nouveau. Vous pouvez contrôler le nombre de fois que `draw` s'exécute chaque seconde avec la fonction `frameRate`.

Avec l'art génératif, je mets généralement `noLoop` dans la fonction `setup`, ce qui fait que `draw` ne s'exécute qu'une seule fois au lieu de continuellement.

[Voici un modèle de départ p5 sur CodePen](https://codepen.io/aspittel/pen/EeJJBm).

Puisque nous avons tant parlé de l'importance de l'aléatoire pour l'art génératif, une autre fonction importante dans p5 est `random`. Elle fonctionne de manière similaire à `Math.random` de JavaScript, mais vous pouvez définir une plage pour les nombres afin de ne pas avoir à faire autant de maths pour obtenir le nombre dans un format utile.

#### Lignes dans p5

Vous pouvez créer une ligne dans p5.js comme ceci :

```
line(startX, startY, endX, endY)
```

Ensuite, vous pouvez générer aléatoirement un ensemble de lignes et créer une simple œuvre d'art génératif comme ceci :

Même des scripts très simples peuvent générer des œuvres d'art cool !

#### Formes dans p5

Vous pouvez également créer des formes avec p5 — comme des cercles, des triangles et des carrés.

Voici un exemple de création de quelques formes avec p5 :

```
// cercle ellipse(xCoordinate, yCoordinate, width, height) 
```

```
// carré rect(xCoordinate, yCoordinate, width, height) 
```

```
// triangle triangle(xCoordinate1, yCoordinate1, x2, y2, x3, y3)
```

Ensuite, nous pouvons créer encore plus de formes pour construire quelque chose de plus amusant !

#### Mouvement dans p5

Nous pouvons ajouter du mouvement à nos dessins en supprimant l'appel de la fonction `noLoop` dans la fonction `setup` — regardez ça !

#### Couleur

Vous pouvez également jouer avec les couleurs dans l'art génératif en choisissant aléatoirement des couleurs. Vous pouvez le faire mathématiquement via des valeurs RGB, ou vous pouvez générer une palette de couleurs avec votre sélecteur de couleurs préféré (nous avons utilisé [celui-ci](https://www.colorbox.io/)).

Vous pouvez définir la couleur de remplissage avec la fonction `color`. Elle prend plusieurs formats différents, comme des couleurs nommées, des RGBA et des codes hexadécimaux.

Vous pouvez également changer la couleur du contour en utilisant `stroke`. Vous pouvez également supprimer ce contour en utilisant `noStroke` ou en faire une largeur différente avec `strokeWeight`.

#### Tout mettre ensemble

Une fois que nous avons toutes ces pièces en place, nous pouvons combiner les techniques pour construire des choses vraiment cool.

### Une autre stratégie : modifier des tutoriels

Vous pouvez également générer de l'art génératif vraiment cool en prenant le travail de quelqu'un d'autre et en vous basant dessus. Par exemple, voici le résultat d'un tutoriel de [Dan Shiffman](https://www.youtube.com/channel/UCvjgXvBlbQiydffZU7m1_aw) :

Voici deux modifications pour créer des effets différents :

[Voici](https://codepen.io/collection/nMmoem/) une collection CodePen avec encore plus d'exemples !

Vous pouvez suivre des tutoriels, forker des CodePens ou des projets Glitch et créer quelque chose de nouveau et unique. Assurez-vous simplement de donner également du crédit à l'artiste original.

### Aide-mémoire

Voici un aide-mémoire avec toutes les fonctionnalités de P5 que nous avons utilisées pour ce tutoriel.

![Image](https://cdn-media-1.freecodecamp.org/images/0*hFfffK_1TdH8MOJf.png)

### Lire plus

* [Generative Artistry](https://generativeartistry.com/)
* [Coding Train](https://www.youtube.com/channel/UCvjgXvBlbQiydffZU7m1_aw)
* [Conférence de Tim Holman](https://www.youtube.com/watch?v=4Se0_w0ISYk)

### Restez en contact

Cet article a été co-écrit avec [James Reichard](https://twitter.com/1800thehive). Si vous créez votre propre art, assurez-vous de nous le tweeter ! ([Ali](https://twitter.com/ASpittel) et [James](https://twitter.com/1800THEHIVE)).

_Publié à l'origine sur [dev.to](https://dev.to/aspittel/intro-to-generative-art-2hi7)._