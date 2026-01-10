---
title: 'L''algorithme de Lee expliqué : Parcours de labyrinthe et recherche du plus
  court chemin'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-02T18:43:00.000Z'
originalURL: https://freecodecamp.org/news/lee-algorithm-maze-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ee6740569d1a4ca3fc8.jpg
tags:
- name: algorithms
  slug: algorithms
- name: Computer Science
  slug: computer-science
seo_title: 'L''algorithme de Lee expliqué : Parcours de labyrinthe et recherche du
  plus court chemin'
seo_desc: 'What is the Lee Algorithm?

  The Lee algorithm is one possible solution for maze routing problems. It always
  gives an optimal solution, if one exists, but is slow and requires large memory
  for dense layout.

  Understanding how it works

  The algorithm is a...'
---

## Qu'est-ce que l'algorithme de Lee ?

L'algorithme de Lee est une solution possible pour les problèmes de routage dans les labyrinthes. Il fournit toujours une solution optimale, si elle existe, mais il est lent et nécessite une grande mémoire pour les dispositions denses.

### Comprendre son fonctionnement

L'algorithme est basé sur un parcours en `largeur d'abord` et utilise des `files d'attente` pour stocker les étapes. Il suit généralement les étapes suivantes :

1. Choisissez un point de départ et ajoutez-le à la file d'attente.
2. Ajoutez les cellules voisines valides à la file d'attente.
3. Retirez la position actuelle de la file d'attente et passez à l'élément suivant.
4. Répétez les étapes 2 et 3 jusqu'à ce que la file d'attente soit vide.

### Implémentation

C++ dispose déjà de la file d'attente implémentée dans la bibliothèque `<queue>`, mais si vous utilisez autre chose, vous êtes libre d'implémenter votre propre version de file d'attente.

### Code C++ :

```
int dl[] = {-1, 0, 1, 0}; // ces tableaux vous aideront à vous déplacer dans les 4 directions plus facilement
int dc[] = {0, 1, 0, -1};

queue<int> X, Y; // les files d'attente utilisées pour obtenir les positions dans la matrice

X.push(start_x); // initialisez les files d'attente avec la position de départ
Y.push(start_y);

void lee()
{
  int x, y, xx, yy;
  while(!X.empty()) // tant qu'il reste des positions dans la file d'attente
  {
    x = X.front(); // définissez la position actuelle
    y = Y.front();
    for(int i = 0; i < 4; i++)
    {
      xx = x + dl[i]; // déplacez-vous vers une cellule adjacente depuis la position actuelle
      yy = y + dc[i];
      if('la position est valide') // ici, vous devez insérer les conditions qui s'appliquent à votre position (xx, yy)
      {
          X.push(xx); // ajoutez la position à la file d'attente
          Y.push(yy);
          mat[xx][yy] = -1; // vous marquez généralement que vous êtes passé par cette position dans la matrice
      }
    }
    
    X.pop(); // éliminez la première position, car vous n'en avez plus besoin
    Y.pop();    
  }
}

```