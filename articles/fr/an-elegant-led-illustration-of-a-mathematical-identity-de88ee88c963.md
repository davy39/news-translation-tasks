---
title: Une illustration élégante à LED d'une identité mathématique
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-23T19:10:21.000Z'
originalURL: https://freecodecamp.org/news/an-elegant-led-illustration-of-a-mathematical-identity-de88ee88c963
coverImage: https://cdn-media-1.freecodecamp.org/images/1*jtP8OiDRsdDAdwBjyN5DGA.jpeg
tags:
- name: arduino
  slug: arduino
- name: coding
  slug: coding
- name: Electronics
  slug: electronics
- name: Mathematics
  slug: mathematics
- name: 'tech '
  slug: tech
seo_title: Une illustration élégante à LED d'une identité mathématique
seo_desc: 'By Chris Lam

  I am a big fan of science toys. I have been looking for one that combines the elegance
  of math and programming for a while. However, there was not much success in the
  search. So, I decided to make one myself.

  Here is a demo. The flashing...'
---

Par Chris Lam

Je suis un grand fan des jouets scientifiques. Je cherchais depuis un moment un jouet qui combine l'élégance des mathématiques et de la programmation. Cependant, je n'ai pas eu beaucoup de succès dans mes recherches. J'ai donc décidé d'en fabriquer un moi-même.

Voici une démonstration. Les LEDs clignotantes sont utilisées pour illustrer visuellement une identité mathématique.

### Mathématiques

L'identité mathématique est la suivante. Le côté gauche de l'équation est une somme arithmétique de 1 à _n-1_ et le côté droit de l'équation est «[n choose 2](https://en.wikipedia.org/wiki/Combination)», le nombre de façons uniques de choisir 2 éléments parmi _n_ éléments.

![Image](https://cdn-media-1.freecodecamp.org/images/1*XZUYnypW2Qb9XLxW7VIC7g.png)
_Identité mathématique_

Ce n'est pas l'identité elle-même qui est élégante, mais la preuve visuelle en elle-même. Regardons le diagramme ci-dessous. Il y a _n=4_ points verts dans l'illustration.

![Image](https://cdn-media-1.freecodecamp.org/images/1*jtP8OiDRsdDAdwBjyN5DGA.jpeg)
_Illustration LED_

Pour chaque paire de points verts sur la rangée du bas, il y a toujours un point rouge unique dans le triangle au-dessus qui leur correspond. Ce point rouge est le sommet d'un triangle équilatéral dont la base est définie par les points verts.

Par conséquent, le nombre de façons de choisir 2 points verts parmi _n_ points verts est égal à la somme des points rouges, 1 + 2 + 3 + … + (_n_-1).

Dans ce cas, cela donne 1 + 2 + (4 – 1) = 6.

Cette observation a été initialement faite par Loren C. Larson dans [cet article](https://www.tandfonline.com/doi/abs/10.1080/07468342.1985.11972910?journalCode=ucmj20&).

### Programmation

Bien qu'il soit facile de tracer visuellement le point rouge à partir des points verts, il est plus amusant et stimulant de spécifier cette relation en code.

Supposons que nous connaissons les indices des points verts (par exemple, i et j). Le défi de programmation consiste à spécifier l'indice correspondant du point rouge qui forme le triangle équilatéral avec les points verts.

À première vue, cela semble difficile.

Mais le problème peut être grandement simplifié si nous modifions la manière dont nous étiquetons les points rouges. Nous pouvons étiqueter les points rouges de bas en haut au lieu de haut en bas.

Avec ce schéma d'indexation, nous pouvons alors spécifier l'indice des points rouges à l'aide de la formule suivante.

![Image](https://cdn-media-1.freecodecamp.org/images/1*cNwsj8hBqeC6HF1pz1dotg.jpeg)
_Une illustration de la manière d'indexer les points rouges en utilisant les indices des points verts._

Voici le code complet utilisé pour faire clignoter les LEDs avec Arduino.

### Électronique

J'ai soudé les LEDs sur une carte et connecté les LEDs aux broches de sortie de l'Arduino via des résistances de 1k. Il est très important d'utiliser les résistances car elles protègent les LEDs.

La connexion est la suivante.

![Image](https://cdn-media-1.freecodecamp.org/images/1*AGo0vjfM8z5LmZmtOXMiJQ.jpeg)
_Schéma_

Et lorsque vous les assemblez et chargez le logiciel sur l'Arduino, cela commence à clignoter comme ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*xggk2l3AY4vi5ZtN-KZYgw.jpeg)
_Résultat final_

J'espère que vous apprécierez ce gadget !