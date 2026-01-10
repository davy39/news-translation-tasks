---
title: Algorithmes de retour sur trace expliqués
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-26T22:05:00.000Z'
originalURL: https://freecodecamp.org/news/backtracking-algorithms-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d7a740569d1a4ca37fa.jpg
tags:
- name: algorithms
  slug: algorithms
- name: toothbrush
  slug: toothbrush
seo_title: Algorithmes de retour sur trace expliqués
seo_desc: 'Backtracking Algorithms

  Backtracking is a general algorithm for finding all (or some) solutions to some
  computational problems, notably constraint satisfaction problems. It incrementally
  builds candidates to the solutions, and abandons each partial c...'
---

# **Algorithmes de retour sur trace**

Le retour sur trace (backtracking) est un algorithme général pour trouver toutes (ou certaines) solutions à certains problèmes computationnels, notamment les problèmes de satisfaction de contraintes. Il construit incrémentiellement des candidats pour les solutions, et abandonne chaque candidat partiel (_"retour sur trace"_) dès qu'il détermine que le candidat ne peut pas être complété en une solution valide.

### **Problème d'exemple (Le problème du tour du cavalier)**

_Le cavalier est placé sur la première case d'un échiquier vide et, se déplaçant selon les règles des échecs, doit visiter chaque case exactement une fois._

### **Chemin suivi par le Cavalier pour couvrir toutes les cases**

Voici un échiquier avec 8 x 8 cases. Les nombres dans les cases indiquent le numéro de mouvement du Cavalier.

![La solution du tour du cavalier - par Euler](https://upload.wikimedia.org/wikipedia/commons/d/df/Knights_tour_%28Euler%29.png)

### **Algorithme naïf pour le tour du Cavalier**

L'algorithme naïf consiste à générer tous les tours un par un et à vérifier si le tour généré satisfait les contraintes.

```text
while there are untried tours
{ 
   generate the next tour 
   if this tour covers all squares 
   { 
      print this path;
   }
}
```

### **Algorithme de retour sur trace pour le tour du Cavalier**

Voici l'algorithme de retour sur trace pour le problème du tour du Cavalier.

```text
If all squares are visited 
    print the solution
Else
   a) Add one of the next moves to solution vector and recursively 
   check if this move leads to a solution. (A Knight can make maximum 
   eight moves. We choose one of the 8 moves in this step).
   b) If the move chosen in the above step doesn't lead to a solution
   then remove this move from the solution vector and try other 
   alternative moves.
   c) If none of the alternatives work then return false (Returning false 
   will remove the previously added item in recursion and if false is 
   returned by the initial call of recursion then "no solution exists" )
```

###