---
title: Comment verrouiller un angle lors du dessin sur canvas en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-18T16:16:31.000Z'
originalURL: https://freecodecamp.org/news/how-to-lock-an-angle-when-drawing-on-canvas-in-javascript-51938b5abc7c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*cWcey5rf6AkuNtkVZ7ywwg.png
tags:
- name: canvas
  slug: canvas
- name: geometry
  slug: geometry
- name: JavaScript
  slug: javascript
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: Comment verrouiller un angle lors du dessin sur canvas en JavaScript
seo_desc: 'By Thang Minh Vu

  In many drawing tools (Adobe Photoshop, Sketch, and so on), if we hold the SHIFT
  button when drawing a line, we can create perfectly straight lines horizontally
  or vertically.

  Recently, I tried implementing this feature in canvas by ...'
---

Par Thang Minh Vu

Dans de nombreux outils de dessin ([Adobe Photoshop](https://www.adobe.com/products/photoshop.html), [Sketch](https://www.sketchapp.com/), et ainsi de suite), si nous maintenons le bouton SHIFT enfoncé lors du dessin d'une ligne, nous pouvons créer des lignes parfaitement droites horizontalement ou verticalement.

Récemment, j'ai essayé d'implémenter cette fonctionnalité en canvas avec JavaScript. Le processus est vraiment intéressant. Je voudrais partager les progrès de la manière dont je l'ai abordé.

**Démonstration** : Pour mieux comprendre l'idée, vous pouvez consulter une version de démonstration sur la [page de démonstration](https://ittus.github.io/draw-lock-angle/).

### Exigences

**Entrée**

* Un point de base (B)
* Position actuelle de la souris (M)

**Sortie**

* Projection de la position actuelle de la souris sur l'axe x ou y (P)

Pour plus de commodité, dans tous les graphiques, nous marquerons le point de base par un cercle rouge et le point actuel de la souris par un cercle vert.

![Image](https://cdn-media-1.freecodecamp.org/images/zvt4t9MmiO6Uxc3zAyLDxUOta3S-j4Nl7JvE)
_Problème : Décider quelle projection est la meilleure_

### Solution simple

Lorsque j'aborde le problème, il est intuitif de voir que nous pouvons calculer la distance entre la position actuelle de la souris et la ligne horizontale et la ligne verticale. Si la position de la souris est plus proche de la ligne horizontale que de la ligne verticale, nous prendrons la projection sur la ligne horizontale, et vice versa.

![Image](https://cdn-media-1.freecodecamp.org/images/F-mQyWvLknInihDnYTgeS2CYyiHljKRB-P1R)

Le calcul est assez simple — voici le code JavaScript :

![Image](https://cdn-media-1.freecodecamp.org/images/AmQiLZ6chh1YF30QhI6MXs0Qrpwq1SkXAdti)

### Problème étendu

Et si nous voulons projeter sur la ligne bissectrice entre la ligne horizontale et la ligne verticale (similaire à [Sketch](https://www.sketchapp.com/)) ? Cela signifie que les utilisateurs peuvent projeter la position de la souris sur la ligne horizontale, la ligne verticale, la ligne à 45 degrés ou la ligne à 135 degrés.

L'approche est similaire. Cette fois, nous devons calculer la distance entre la position de la souris et 4 lignes : la ligne horizontale, la ligne verticale et 2 lignes bissectrices (ligne à 45 degrés et ligne à 135 degrés). Mais le calcul est plus complexe.

Nous pouvons toujours le diviser en 2 étapes :

1. Déterminer quelle ligne est la plus proche de la position de la souris
2. Calculer la projection de la position de la souris sur la ligne la plus proche

![Image](https://cdn-media-1.freecodecamp.org/images/yRRlpXpZg16PFuGjohkEwMBRTQ074yN4UmvH)

#### Étape 1 : Déterminer quelle ligne est la plus proche de la position de la souris

Tout d'abord, nous devons déterminer la formulation de la ligne des 4 lignes ci-dessus. Parce que nous connaissons déjà le point de base (x0, y0) et l'angle de la ligne, il est facile de déterminer la formulation de chaque ligne.

> Exemple : Pour calculer la formule de la bissectrice à 45 degrés, nous savons déjà que la ligne passera par le point de base (x0, y0) et (x0 + 1, y0 + 1). En utilisant la méthode [Find-the-Equation-of-a-Line](https://www.wikihow.com/Find-the-Equation-of-a-Line), nous pouvons déterminer la formule de la ligne.

Enfin, nous aurons les formules des 4 lignes :

![Image](https://cdn-media-1.freecodecamp.org/images/ngaxjDK6zWtgP74BOXPwMU2jZY014c7L-lu6)

Pour calculer la distance entre la position de base de la souris et chaque ligne, nous pouvons utiliser une formule mathématique populaire :

![Image](https://cdn-media-1.freecodecamp.org/images/C4Tk7kqRbwGbPtYFwK-HDSRlmVnGTRunxAso)
_Distance d'un point à une ligne_

![Image](https://cdn-media-1.freecodecamp.org/images/Adk5BQAv15Jy4IuGUBSyKiSxkU68gEgsdh7z)
_Trouver la ligne la plus proche_

#### Étape 2 : Calculer la projection orthogonale de la position de la souris sur la ligne la plus proche

Maintenant, le problème consiste à calculer la projection orthogonale de la position de la souris (M) sur la ligne la plus proche avec la formule : ax + by + c = 0 (L)

Il existe plusieurs façons de résoudre ce problème. J'ai choisi une méthode simple : d'abord, calculer la formule de la ligne qui contient la position de la souris M et qui est perpendiculaire à la ligne L, appelée L'. Ensuite, résoudre le système d'équations pour obtenir le point d'intersection entre la ligne L et L', qui est le point de projection que nous cherchons.

Après quelques calculs, j'ai déterminé la formule de L', qui passe par M (x0, y0) et qui est perpendiculaire à L (ax + by + c = 0) :

![Image](https://cdn-media-1.freecodecamp.org/images/BwlHT2VPl2baMMHQtQYI2vGkCUq0jl0ZpiLz)

Maintenant, pour trouver l'intersection, nous devons résoudre le système d'équations :

![Image](https://cdn-media-1.freecodecamp.org/images/4nJ1rFj7FrXEwZ0KK3MLEGo10DMJDUrchUxB)

En utilisant la [règle de Cramer](https://en.wikipedia.org/wiki/Cramer%27s_rule) et le déterminant de la matrice, nous pouvons résoudre cette équation facilement :

![Image](https://cdn-media-1.freecodecamp.org/images/YeHWX9l70xghLPvDkqTZA19RSbRGyRIZq4WJ)
_Résoudre les équations simultanées_

### Limite

Il existe une situation où nous voulons limiter la frontière de la projection.

Exemple :

![Image](https://cdn-media-1.freecodecamp.org/images/3WNRAcorUIwF9lwihmXCjAna8DovCrhgmUxi)
_Le point de projection est en dehors de la limite_

Dans ce cas, nous voulons limiter la projection dans la zone rectangulaire blanche, mais en utilisant la méthode discutée, le point de projection peut être en dehors de la zone de limite.

Dans cette situation, nous pouvons simplement obtenir le point d'intersection de la ligne L' avec la limite (appelé P').

![Image](https://cdn-media-1.freecodecamp.org/images/Zl5D-QVbgmra2XCyD6khtLSFE1sF9VzPz49c)
_Support de la limite de la projection_

### **Code source complet**

Vous pouvez consulter la démonstration et le code source sur [Github](https://github.com/ittus/draw-lock-angle).

Bon codage !