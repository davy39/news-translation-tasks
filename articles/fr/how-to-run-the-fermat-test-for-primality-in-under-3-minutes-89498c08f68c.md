---
title: Comment exécuter le test de Fermat pour la primalité en moins de 3 minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-22T15:24:25.000Z'
originalURL: https://freecodecamp.org/news/how-to-run-the-fermat-test-for-primality-in-under-3-minutes-89498c08f68c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ZILryLJXlIQxX1i-nKRPtw.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: Functional Programming
  slug: functional-programming
- name: Mathematics
  slug: mathematics
- name: Swift
  slug: swift
- name: technology
  slug: technology
seo_title: Comment exécuter le test de Fermat pour la primalité en moins de 3 minutes
seo_desc: 'By Devesh Shetty

  The Fermat test is based on a result from number theory known as Fermat’s little
  theorem.

  According to Fermat’s little theorem, if n is a prime number and d is any positive
  integer less than n, then d raised to the nth power is congr...'
---

Par Devesh Shetty

Le test de Fermat est basé sur un résultat de la théorie des nombres connu sous le nom de petit théorème de Fermat.

Selon le petit théorème de Fermat, si _n_ est un nombre premier et _d_ est un entier positif inférieur à _n_, alors _d_ élevé à la puissance _n_ est congru à _d_ modulo _n_.

Si deux nombres ont le même reste lorsqu'ils sont divisés par _n_, alors ils sont dits _congrus modulo n_. _d modulo n_ est simplement le reste d'un nombre _d_ lorsqu'il est divisé par _n_.

Par exemple, 34 est congru à 16 (modulo 3) car
34 modulo 3 = 1 et 16 modulo 3 = 1.

#### Test de Fermat pour la primalité

1. Pour un nombre donné _n_, choisissez un nombre positif aléatoire _d_ tel que _d < n_.
2. Calculez _(d^n) modulo n_.
3. _d modulo n_ sera toujours égal à _d_ car nous choisissons toujours _d_ qui satisfait la condition _d < n_.
4. Si le résultat de _(d^n) modulo n_ n'est pas égal à _d_, alors _d_ n'est certainement pas premier.
5. Si le résultat de _(d^n) modulo n_ est égal à _d_, alors il est probable que _n_ soit premier.
6. Choisissez un autre nombre aléatoire _d_ qui satisfait la condition _d < n_ et répétez les étapes ci-dessus.

**Note** : Les exemples de cet article utilisent [Swift 4.1](https://swift.org/blog/swift-4-1-released/)

Nous avons besoin d'une fonction pour calculer l'exponentielle d'un nombre modulo un autre nombre.

![Image](https://cdn-media-1.freecodecamp.org/images/xo3yNSnDQAS1sAk0KnD7kTLNpwDQtiqnDJlp)
_Calculer (d^n) modulo n_

Nous utilisons [l'exponentiation modulaire](https://en.wikipedia.org/wiki/Modular_exponentiation) pour calculer des valeurs lorsque l'exposant est supérieur à 1, car cela nous permet d'effectuer des calculs en ne traitant que des nombres inférieurs à _n_ (_modulo_ dans la fonction ci-dessus).

![Image](https://cdn-media-1.freecodecamp.org/images/orqRbwqC3uRbSiX15dGgDg7GmZAxYPRRS43l)
_Le test de Fermat_

Le test de Fermat choisit aléatoirement un nombre _d_ entre 1 et _n-1_ (nombre - 1 dans la fonction ci-dessus) inclus. L'objectif est de vérifier si le reste modulo n de la puissance n de d est égal à d.

![Image](https://cdn-media-1.freecodecamp.org/images/jNeeRWHFVv2TIeNPZORAqFJHH5IXXyv70sTS)
_Exécuter le test de Fermat pour le nombre spécifié_

Le test de Fermat est exécuté pour le nombre spécifié. Si un nombre échoue au test de Fermat, nous sommes assurés qu'il n'est pas premier. Si un nombre réussit le test de Fermat, il n'est pas garanti qu'il soit premier. Nous essayons de réduire la probabilité d'erreur dans notre test de primalité en exécutant le test suffisamment de fois.

En essayant de plus en plus de valeurs de _d_ (un nombre positif aléatoire entre 1 et n-1), nous pouvons augmenter notre confiance dans le résultat.