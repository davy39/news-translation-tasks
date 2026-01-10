---
title: L'algorithme de Lee expliqué avec des exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-28T19:35:00.000Z'
originalURL: https://freecodecamp.org/news/lees-algorithm-explained-with-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e6c740569d1a4ca3d00.jpg
tags:
- name: algorithms
  slug: algorithms
- name: toothbrush
  slug: toothbrush
seo_title: L'algorithme de Lee expliqué avec des exemples
seo_desc: 'The Lee algorithm is one possible solution for maze routing problems. It
  always gives an optimal solution, if one exists, but is slow and requires large
  memory for dense layout.

  Understanding how it works

  The algorithm is a breadth-first based algori...'
---

L'algorithme de Lee est une solution possible pour les problèmes de routage de labyrinthes. Il donne toujours une solution optimale, si elle existe, mais il est lent et nécessite une grande mémoire pour les dispositions denses.

### **Comprendre comment il fonctionne**

L'algorithme est un algorithme basé sur le `breadth-first` qui utilise des `queues` pour stocker les étapes. Il utilise généralement les étapes suivantes :

1. Choisissez un point de départ et ajoutez-le à la file d'attente.
2. Ajoutez les cellules voisines valides à la file d'attente.
3. Retirez la position sur laquelle vous vous trouvez de la file d'attente et passez à l'élément suivant.
4. Répétez les étapes 2 et 3 jusqu'à ce que la file d'attente soit vide.

Un concept clé à comprendre est que les recherches `breadth-first` vont en largeur, tandis que les recherches `depth-first` vont en profondeur.

En utilisant l'exemple d'un algorithme de résolution de labyrinthe, une approche `depth-first` essaiera chaque chemin possible un par un jusqu'à ce qu'il atteigne une impasse ou la fin et retourne le résultat. Cependant, le chemin qu'il retourne peut ne pas être le plus efficace, mais simplement le premier chemin complet vers la fin que l'algorithme a pu trouver.

Une recherche `breadth-first` ira plutôt vers chaque espace ouvert adjacent au point de départ, puis cherchera d'autres espaces ouverts possibles. Elle continuera à faire cela, en allant couche par couche et en essayant chaque chemin possible en tandem, jusqu'à ce qu'elle trouve le point de fin. Puisque vous essayez chaque chemin en même temps, vous pouvez être sûr que le premier chemin complet du début à la fin est également le plus court.

### **Implémentation**

C++ a déjà implémenté la file d'attente dans la bibliothèque `<queue>`, mais si vous utilisez autre chose, vous êtes libre d'implémenter votre propre version de la file d'attente.

Code C++ :

```cpp
int dl[] = {-1, 0, 1, 0}; // ces tableaux vous aideront à voyager dans les 4 directions plus facilement
int dc[] = {0, 1, 0, -1};

queue<int> X, Y; // les files d'attente utilisées pour obtenir les positions dans la matrice

X.push(start_x); // initialisez les files d'attente avec la position de départ
Y.push(start_y);

void lee()
{
  int x, y, xx, yy;
  while(!X.empty()) // tant qu'il y a encore des positions dans la file d'attente
  {
    x = X.front(); // définissez la position actuelle
    y = Y.front();
    for(int i = 0; i < 4; i++)
    {
      xx = x + dl[i]; // voyagez dans une cellule adjacente à partir de la position actuelle
      yy = y + dc[i];
      if('position is valid') // ici, vous devez insérer les conditions qui doivent s'appliquer pour votre position (xx, yy)
      {
          X.push(xx); // ajoutez la position à la file d'attente
          Y.push(yy);
          mat[xx][yy] = -1; // vous marquez généralement que vous avez été à cette position dans la matrice
      }
      
    }
    
    X.pop(); // éliminez la première position, car vous n'en avez plus besoin
    Y.pop();
    
  }


}
```