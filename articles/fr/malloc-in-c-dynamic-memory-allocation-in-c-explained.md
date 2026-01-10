---
title: 'malloc en C : Allocation Dynamique de Mémoire en C Expliquée'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-26T21:55:00.000Z'
originalURL: https://freecodecamp.org/news/malloc-in-c-dynamic-memory-allocation-in-c-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d7d740569d1a4ca3808.jpg
tags:
- name: c programming
  slug: c-programming
- name: toothbrush
  slug: toothbrush
seo_title: 'malloc en C : Allocation Dynamique de Mémoire en C Expliquée'
seo_desc: 'What is malloc() in C?

  malloc() is a library function that allows C to allocate memory dynamically from
  the heap. The heap is an area of memory where something is stored.

  malloc() is part of stdlib.h and to be able to use it you need to use #include ...'
---

# **Qu'est-ce que malloc() en C ?**

malloc() est une fonction de bibliothèque qui permet à C d'allouer dynamiquement de la mémoire depuis le tas (heap). Le tas est une zone de mémoire où quelque chose est stocké.

malloc() fait partie de stdlib.h et pour pouvoir l'utiliser, vous devez inclure `#include <stdlib.h>`.

## **Comment Utiliser Malloc**

malloc() alloue de la mémoire d'une taille demandée et retourne un pointeur vers le début du bloc alloué. Pour stocker ce pointeur retourné, nous devons créer une variable. Le pointeur doit être du même type que celui utilisé dans l'instruction malloc.  
Ici, nous allons créer un pointeur vers un futur tableau d'entiers.

```c
int* arrayPtr;
```

Contrairement à d'autres langages, C ne connaît pas le type de données pour lequel il alloue de la mémoire ; il doit être informé. Heureusement, C dispose d'un opérateur appelé `sizeof()` que nous pouvons utiliser.

```c
arrayPtr = (int *)malloc(10 * sizeof(int));
```

Cette instruction utilise malloc pour réserver de la mémoire pour un tableau de 10 entiers. Comme les tailles peuvent varier entre les ordinateurs, il est important d'utiliser la fonction sizeof() pour calculer la taille sur l'ordinateur actuel.

Toute mémoire allouée pendant l'exécution du programme devra être libérée avant la fermeture du programme. Pour libérer la mémoire, nous pouvons utiliser la fonction free()

```c
free( arrayPtr );
```

Cette instruction désallouera la mémoire précédemment allouée. C ne dispose pas d'un `garbage collector` comme certains autres langages, tels que Java. Par conséquent, la mémoire non correctement libérée continuera d'être allouée après la fermeture du programme.

# **Avant de continuer…**

## **Un Résumé**

* Malloc est utilisé pour l'allocation dynamique de mémoire et est utile lorsque vous ne connaissez pas la quantité de mémoire nécessaire lors de la compilation.
* Allouer de la mémoire permet aux objets d'exister au-delà de la portée du bloc actuel.
* C passe par valeur plutôt que par référence. Utiliser malloc pour assigner de la mémoire, puis passer le pointeur à une autre fonction, est plus efficace que de faire recréer la structure par la fonction.

## Plus d'informations sur la programmation en C :

* [Le guide du débutant pour la programmation en C](https://www.freecodecamp.org/news/the-c-beginners-handbook/)
* [L'instruction if...else en C expliquée](https://www.freecodecamp.org/news/if-statements-in-c/)
* [L'opérateur ternaire en C expliqué](https://www.freecodecamp.org/news/c-ternary-operator/)