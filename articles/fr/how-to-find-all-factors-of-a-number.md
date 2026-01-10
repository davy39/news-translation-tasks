---
title: Comment trouver tous les facteurs d'un nombre
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-31T22:58:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-find-all-factors-of-a-number
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d37740569d1a4ca3687.jpg
tags:
- name: Math
  slug: math
- name: toothbrush
  slug: toothbrush
seo_title: Comment trouver tous les facteurs d'un nombre
seo_desc: 'All Factors of a Number

  You can think of factors as the numbers that you multiply to get another number.


  In this case 2, 3, 6, and 7 are all numbers you can multiply to get 42. So, they
  are all factors of 42. However, they are not all the factors of...'
---

## **Tous les facteurs d'un nombre**

Vous pouvez considérer les facteurs comme les nombres que vous multipliez pour obtenir un autre nombre.

![Image](https://upload.wikimedia.org/wikipedia/commons/e/e8/Factor_Tree_of_42.png)

Dans ce cas, 2, 3, 6 et 7 sont tous des nombres que vous pouvez multiplier pour obtenir 42. Ils sont donc tous des facteurs de 42. Cependant, ils ne sont pas tous les facteurs de 42. Pour trouver tous les facteurs, nous pouvons utiliser l'algorithme ou le processus étape par étape ci-dessous.

Commencez par 1.

1 * 42 = 42

Facteurs : 1…42

Essayez 2.

2 * 21 = 42

Facteurs : 1, 2…21, 42

Essayez 3.

3 * 14 = 42

Facteurs : 1, 2, 3…14, 21, 42

Essayez 4.

Aucun nombre entier ne peut être multiplié par 4 pour obtenir 42, nous le sautons donc.

Essayez 5.

Aucun nombre entier ne peut être multiplié par 5 pour obtenir 42, nous le sautons donc.

Essayez 6.

6 * 7 = 42

1, 2, 3, 6…7, 14, 21, 42

Puisqu'il n'y a pas de nombres entiers entre 6 et 7, tous les facteurs positifs ont été trouvés. Tous les nombres ci-dessus peuvent avoir leur signe inversé et continueront à être des facteurs de 42. En conclusion, tous les facteurs de 42 sont ci-dessous.

1, 2, 3, 6, 7, 14, 21, 42, -1, -2, -3, -6, -7, -14, -21, -42

## **Confirmer que le nombre de facteurs est correct**

Nous pouvons rapidement confirmer que nous avons identifié tous les facteurs positifs avec les étapes suivantes :

1. Prenez la factorisation première (fournie par l'arbre ci-dessus)

2<sup>1</sup> * 3<sup>1</sup> * 7*<sup>1</sup>

1. Ajoutez un à chacun des exposants :

Exposant de 2 : 1 + 1 = 2   
Exposant de 3 : 1 + 1 = 2   
Exposant de 7 : 1 + 1 = 2

1. Multipliez chacun des nombres ci-dessus :

2 * 2 * 2 = 8

1. Confirmez que 42 a 8 facteurs :

1, 2, 3, 6…7, 14, 21, 42