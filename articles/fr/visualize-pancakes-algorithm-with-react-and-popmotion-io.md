---
title: Comment visualiser l'algorithme des pancakes avec React et Popmotion.io
subtitle: ''
author: Mihail Gaberov
co_authors: []
series: null
date: '2019-09-03T12:39:43.000Z'
originalURL: https://freecodecamp.org/news/visualize-pancakes-algorithm-with-react-and-popmotion-io
coverImage: https://www.freecodecamp.org/news/content/images/2019/09/pancakes-algorithm-1.png
tags:
- name: algorithms
  slug: algorithms
- name: Job Interview
  slug: job-interview
- name: React
  slug: react
seo_title: Comment visualiser l'algorithme des pancakes avec React et Popmotion.io
seo_desc: What you are going to see below was supposed to be part of my solution to
  an exercise given in a coding challenge. It was several months ago, and I had signed
  in for it. Due to unforeseen factors, I hadn't finished it. Now, after that time
  and the ch...
---

![Image](https://www.freecodecamp.org/news/content/images/2019/09/pancakes-algorithm.png align="left")

Ce que vous allez voir ci-dessous devait faire partie de ma solution à un exercice donné dans un défi de codage. C'était il y a plusieurs mois, et je m'étais inscrit pour cela. En raison de facteurs imprévus, je ne l'avais pas terminé. Maintenant, après tout ce temps et le défi terminé, je peux le partager ici.

Ce ne sera pas un tutoriel étape par étape. Plutôt, ce sera une revue rapide de la manière dont nous pouvons utiliser des frameworks comme React et Popmotion.io avec un algorithme. Et ensuite créer une belle visualisation de cet algorithme. D'une certaine manière, c'est agréable ! ?

L'algorithme de tri appelé [*Pancakes Sorting Algorithm*](https://en.wikipedia.org/wiki/Pancake_sorting) est un algorithme de tri célèbre (ou pas ?) que vous pouvez lire sur internet si vous êtes intéressé. Sa nature est hors du cadre de cet article. Ici, nous le voyons en action avec de belles animations, grâce à Popmotion.io.

Voici la [*démo en direct*](https://pancakes-algorithm.herokuapp.com/) avec laquelle vous pouvez jouer. Il y a deux champs de texte et deux boutons. Dans le premier champ, vous entrez l'intervalle de temps qui sera utilisé pour chaque tour d'animation, c'est-à-dire la vitesse à laquelle chaque pancake sera trié. C'est en millisecondes, ce qui signifie que si vous entrez la valeur 1000, l'animation s'exécutera pendant environ 1 seconde.

Le deuxième champ est utilisé pour définir combien de pancakes vous voulez voir trier. La valeur doit être comprise entre 2 et 50. Les boutons sont assez explicites. L'un est pour démarrer l'animation de tri, l'autre est pour la réinitialiser.

Et [*ici*](https://gitlab.com/mihailgaberov/pancake-algorithm-visualizer) est l'endroit où vous pouvez trouver le code source de l'application de démonstration. N'hésitez pas à le consulter et à y regarder de plus près. Vous pourriez essayer d'améliorer les animations que j'ai faites. Je serais plus qu'intéressé de voir vos versions. :)

C'est tout. Court et simple, parfait pour l'été ! ☀️ ?

? Merci pour la lecture ! ?