---
title: Qu'est-ce que l'Expotentiation ? Un Guide Algorithme avec des Exemples de Code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-28T18:36:00.000Z'
originalURL: https://freecodecamp.org/news/what-is-expotentiation-an-algorith-guide
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ef8740569d1a4ca4020.jpg
tags:
- name: algorithms
  slug: algorithms
- name: Computer Science
  slug: computer-science
seo_title: Qu'est-ce que l'Expotentiation ? Un Guide Algorithme avec des Exemples
  de Code
seo_desc: "Given two integers a and n, write a function to compute a^n.\nCode\nAlgorithmic\
  \ Paradigm: Divide and conquer.\nint power(int x, unsigned int y) { \n    if (y\
  \ == 0) \n        return 1; \n    else if (y%2 == 0) \n        return power(x, y/2)*power(x,\
  \ y/2); \n ..."
---

Étant donné deux entiers a et n, écrivez une fonction pour calculer a^n.

#### Code

Paradigme Algorithme : Diviser pour régner.

```
int power(int x, unsigned int y) { 
    if (y == 0) 
        return 1; 
    else if (y%2 == 0) 
        return power(x, y/2)*power(x, y/2); 
    else
        return x*power(x, y/2)*power(x, y/2); 
}

```

Complexité Temporelle : `O(n)` | Complexité Spatiale : `O(1)`

#### Solution Optimisée : O(logn)

```
int power(int x, unsigned int y) { 
    int temp; 
    if( y == 0) 
        return 1; 
    temp = power(x, y/2); 
    if (y%2 == 0) 
        return temp*temp; 
    else
        return x*temp*temp; 
}

```

Pourquoi est-ce plus rapide ?

Supposons que nous avons x = 5, y = 4, nous savons que notre réponse sera (5 * 5 * 5 * 5).

Si nous décomposons cela, nous remarquons que nous pouvons écrire (5 * 5 * 5 * 5) comme (5 * 5) * 2 et en outre, nous pouvons écrire (5 * 5) comme 5 * 2.

Grâce à cette observation, nous pouvons optimiser notre fonction à O(log n) en calculant power(x, y/2) une seule fois et en le stockant.

## Exponentiation Modulaire

Étant donné trois nombres x, y, et p, calculer (x^y) % p

```
int power(int x, unsigned int y, int p) { 
    int res = 1;  
    x = x % p; 
    while (y > 0) {  
        if (y & 1) 
            res = (res*x) % p; 
  
        // y doit être pair maintenant 
        y = y >> 1; 
        x = (x*x) % p;   
    } 
    return res; 
}

```

Complexité Temporelle : `O(Log y)`.