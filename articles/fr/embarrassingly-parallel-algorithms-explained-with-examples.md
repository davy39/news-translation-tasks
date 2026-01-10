---
title: Algorithmes embarrassingly parallel expliqués
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-25T18:28:00.000Z'
originalURL: https://freecodecamp.org/news/embarrassingly-parallel-algorithms-explained-with-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f0c740569d1a4ca4093.jpg
tags:
- name: algorithms
  slug: algorithms
- name: Computer Science
  slug: computer-science
seo_title: Algorithmes embarrassingly parallel expliqués
seo_desc: In parallel programming, an embarrassingly parallel algorithm is one that
  requires no communication or dependency between the processes. Unlike distributed
  computing problems that need communication between tasks—especially on intermediate
  results, e...
---

En programmation parallèle, un algorithme embarrassingly parallel est un algorithme qui ne nécessite aucune communication ou dépendance entre les processus. Contrairement aux problèmes de calcul distribué qui nécessitent une communication entre les tâches—surtout sur les résultats intermédiaires, les algorithmes embarrassingly parallel sont faciles à exécuter sur des fermes de serveurs qui manquent de l'infrastructure spéciale utilisée dans un vrai cluster de supercalculateurs. 

En raison de la nature des algorithmes embarrassingly parallel, ils sont bien adaptés aux grandes plateformes distribuées basées sur Internet et ne souffrent pas de ralentissement parallèle. L'opposé des problèmes embarrassingly parallel sont les problèmes intrinsèquement sériels, qui ne peuvent pas être parallélisés du tout. 

Le cas idéal des algorithmes embarrassingly parallel peut être résumé comme suit :

* Tous les sous-problèmes ou tâches sont définis avant le début des calculs.
* Toutes les sous-solutions sont stockées dans des emplacements mémoire indépendants (variables, éléments de tableau).
* Ainsi, le calcul des sous-solutions est complètement indépendant.
* Si les calculs nécessitent une communication initiale ou finale, alors nous l'appelons nearly embarrassingly parallel.

Beaucoup peuvent se demander l'étymologie du terme « embarrassingly ». Dans ce cas, embarrassingly n'a rien à voir avec l'embarras ; en fait, cela signifie une surabondance—ici, faisant référence à des problèmes de parallélisation qui sont « embarrassingly easy ».

Un exemple courant de problème embarrassingly parallel est le rendu vidéo 3D géré par une unité de traitement graphique, où chaque image ou pixel peut être traité sans interdépendance. D'autres exemples seraient les logiciels de repliement de protéines qui peuvent s'exécuter sur n'importe quel ordinateur, chaque machine effectuant une petite partie du travail, la génération de tous les sous-ensembles, les nombres aléatoires et les simulations de Monte Carlo.