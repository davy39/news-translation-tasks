---
title: 'Algorithmes de retour sur trace : récursivité et recherche expliquées avec
  des exemples'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-27T18:32:00.000Z'
originalURL: https://freecodecamp.org/news/backtracking-algorithms-recursive-search
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9eff740569d1a4ca4042.jpg
tags:
- name: algorithms
  slug: algorithms
- name: Computer Science
  slug: computer-science
seo_title: 'Algorithmes de retour sur trace : récursivité et recherche expliquées
  avec des exemples'
seo_desc: 'Examples where backtracking can be used to solve puzzles or problems include:


  Puzzles such as eight queens puzzle, crosswords, verbal arithmetic, Sudoku [nb 1],
  and Peg Solitaire.

  Combinatorial optimization problems such as parsing and the knapsack ...'
---

Exemples où le retour sur trace peut être utilisé pour résoudre des énigmes ou des problèmes :

1. Énigmes telles que le problème des huit dames, les mots croisés, l'arithmétique verbale, le Sudoku [nb 1] et le Peg Solitaire.
2. Problèmes d'optimisation combinatoire tels que l'analyse syntaxique et le problème du sac à dos.
3. Langages de programmation logique tels que Icon, Planner et Prolog, qui utilisent le retour sur trace en interne pour générer des réponses.

### Problème d'exemple (Le problème du parcours du cavalier)

*Le cavalier est placé sur la première case d'un échiquier vide et, se déplaçant selon les règles des échecs, doit visiter chaque case exactement une fois.*

### Chemin suivi par le Cavalier pour couvrir toutes les cellules

Voici un échiquier avec 8 x 8 cases. Les nombres dans les cases indiquent le numéro de déplacement du Cavalier.

![La solution du parcours du cavalier - par Euler](https://upload.wikimedia.org/wikipedia/commons/d/df/Knights_tour_%28Euler%29.png)

### Algorithme Naïf pour le parcours du Cavalier

L'algorithme naïf consiste à générer tous les parcours un par un et à vérifier si le parcours généré satisfait les contraintes.

```
while there are untried tours
{ 
   generate the next tour 
   if this tour covers all squares 
   { 
      print this path;
   }
}

```

### Algorithme de retour sur trace pour le parcours du Cavalier

Voici l'algorithme de retour sur trace pour le problème du parcours du Cavalier.

```
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

### Et voici une explication vidéo pour vous

%[https://www.youtube.com/watch?v=gBC_Fd8EE8A]