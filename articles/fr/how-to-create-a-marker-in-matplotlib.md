---
title: Marqueur Matplotlib - Comment créer un marqueur dans Matplotlib
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2023-03-14T15:05:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-marker-in-matplotlib
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/isaac-smith-6EnTPvPPL6I-unsplash--2--1.jpg
tags:
- name: Matplotlib
  slug: matplotlib
- name: Python
  slug: python
seo_title: Marqueur Matplotlib - Comment créer un marqueur dans Matplotlib
seo_desc: "In this article, you'll learn how to use markers in Matplotlib to indicate\
  \ specific points in a plot. \nThe marker parameter can be used to create \"markers\"\
  \ in a plot. You can specify the shape of the marker by passing a value to the parameter.\
  \ \nHere'..."
---

Dans cet article, vous apprendrez à utiliser les marqueurs dans Matplotlib pour indiquer des points spécifiques dans un graphique. 

Le paramètre `marker` peut être utilisé pour créer des « marqueurs » dans un graphique. Vous pouvez spécifier la forme du marqueur en passant une valeur au paramètre. 

Voici à quoi ressemble un graphique Matplotlib normal :

```python
import matplotlib.pyplot as plt
import numpy as np

x = [2,4,6,8]
y = [1,3,9,7]

plt.plot(x,y)
plt.show()
```

![Image](https://www.freecodecamp.org/news/content/images/2023/03/plot-without-marker.PNG)
_un graphique matplotlib sans marqueur_

Voici un graphique avec un marqueur :

```python
import matplotlib.pyplot as plt
import numpy as np

x = [2,4,6,8]
y = [1,3,9,7]

plt.plot(x,y, marker = 'o')
plt.show()
```

![Image](https://www.freecodecamp.org/news/content/images/2023/03/plot-with-markers.PNG)
_un graphique matplotlib avec un marqueur « o »_

Comme on peut le voir sur l'image ci-dessus, chaque point de rencontre des deux axes dans le graphique est désigné par un marqueur qui ressemble à un cercle.

Nous pouvons le faire en définissant la valeur du paramètre `marker` sur "o" : `plt.plot(x,y, marker = 'o')`.

## Liste des marqueurs Matplotlib

Voici une liste (issue de la [documentation Matplotlib](https://matplotlib.org/stable/api/markers_api.html)) des valeurs de marqueur qui peuvent être assignées au paramètre `marker` :

| Marqueur | Description |
|----------|:-------------:|
| "." | point |
| "," | pixel |
| "o" | cercle |
| "v" | triangle_bas |
| "^" | triangle_haut |
| "<" | triangle_gauche |
| ">" | triangle_droite |
| "1" | tri_bas |
| "2" | tri_haut |
| "3" | tri_gauche |
| "4" | tri_droite |
| "8" | octogone |
| "s" | carré |
| "p" | pentagone |
| "P" | plus (rempli) |
| "h" | hexagone1 |
| "H" | hexagone2 |
| "+" | plus |
| "*" | étoile |
| "x" | x |
| "X" | x (rempli) |
| "D" | diamant |
| "d" | diamant_fin |
| "_" | ligne_horizontale |
| "s" | carré |
| 0 | graduation_gauche |
| 1 | graduation_droite |
| 2 | graduation_haut |
| 3 | graduation_bas |
| 4 | caret_gauche |
| 5 | caret_droite |
| 6 | caret_haut |
| 7 | caret_bas |
| 8 | caret_gauche (centré à la base) |
| 9 | caret_droite (centré à la base) |
| 10 | caret_haut (centré à la base) |
| 11 | caret_bas (centré à la base) |

Cette liste ci-dessus présente les différentes valeurs que vous pouvez utiliser pour changer le style d'un marqueur dans un graphique. 

## Résumé

Dans cet article, nous avons parlé des marqueurs dans Matplotlib. Ils peuvent être utilisés pour marquer/indiquer des points spécifiques dans un graphique. 

Nous avons vu quelques exemples de code montrant l'application du paramètre `marker`. 

Enfin, nous avons vu une liste de valeurs `marker` qui peuvent être utilisées pour changer le style d'un marqueur. 

Bon codage !