---
title: Algorithmes de remplissage de frontière et carrés de remplissage de pixels
  expliqués avec des exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-27T18:34:00.000Z'
originalURL: https://freecodecamp.org/news/boundary-fill-algorithm-pixel-filling-squares
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/boundary-fill-image.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: Computer Science
  slug: computer-science
seo_title: Algorithmes de remplissage de frontière et carrés de remplissage de pixels
  expliqués avec des exemples
seo_desc: 'What are Boundary Fill Algorithms?

  Boundary fill is the algorithm used frequently in computer graphics to fill a desired
  color inside a closed polygon having the same boundary color for all of its sides.

  The most approached implementation of the algo...'
---

## Qu'est-ce que les algorithmes de remplissage de frontière ?

Le remplissage de frontière est l'algorithme fréquemment utilisé en infographie pour remplir une couleur souhaitée à l'intérieur d'un polygone fermé ayant la même couleur de frontière pour tous ses côtés.

L'implémentation la plus abordée de l'algorithme est une fonction récursive basée sur une pile.

### Exemple de fonctionnement :

Le problème est assez simple et suit généralement ces étapes :

1. Prendre la position du point de départ et la couleur de la frontière.
2. Décider si vous voulez aller dans 4 directions (N, S, O, E) ou 8 directions (N, S, O, E, NO, NE, SO, SE).
3. Choisir une couleur de remplissage.
4. Se déplacer dans ces directions.
5. Si le pixel sur lequel vous atterrissez n'est pas la couleur de remplissage ou la couleur de la frontière, remplacez-le par la couleur de remplissage.
6. Répéter les étapes 4 et 5 jusqu'à ce que vous ayez tout couvert à l'intérieur des frontières.

### Certaines restrictions :

1. La couleur de la frontière doit être la même pour tous les bords du polygone.
2. Le point de départ doit être à l'intérieur du polygone.

### Extrait de code :

```
void boundary_fill(int pos_x, int pos_y, int boundary_color, int fill_color)
{  
current_color= getpixel(pos_x,pos_y);  // obtenir la couleur de la position actuelle du pixel
if( current_color!= boundary_color || currrent_color != fill_color) // si le pixel n'est pas déjà rempli ou fait partie de la frontière alors
{    
 putpixel(pos_x,pos_y,fill_color);  // changer la couleur de ce pixel pour la couleur de remplissage souhaitée
 boundary_fill(pos_x + 1, pos_y,boundary_color,fill_color);  // effectuer la même fonction pour le pixel est
 boundary_fill(pos_x - 1, pos_y,boundary_color,fill_color);  // effectuer la même fonction pour le pixel ouest
 boundary_fill(pos_x, pos_y + 1,boundary_color,fill_color);  // effectuer la même fonction pour le pixel nord
 boundary_fill(pos_x, pos_y - 1,boundary_color,fill_color);  // effectuer la même fonction pour le pixel sud
}
}

```

À partir du code donné, vous pouvez voir que pour tout pixel sur lequel vous atterrissez, vous vérifiez d'abord s'il peut être changé en fill_color, puis vous faites de même pour ses voisins jusqu'à ce que tous les pixels à l'intérieur de la frontière aient été vérifiés.

Voici un tutoriel vidéo qui vous guidera à travers ces détails en environ 10 minutes :

%[https://www.youtube.com/watch?v=au2CslPa4xU]