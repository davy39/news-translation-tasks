---
title: Taille de la figure Matplotlib – Comment changer la taille du graphique en
  Python avec plt.figsize()
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2023-01-12T15:29:17.000Z'
originalURL: https://freecodecamp.org/news/matplotlib-figure-size-change-plot-size-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/isaac-smith-6EnTPvPPL6I-unsplash.jpg
tags:
- name: Data Science
  slug: data-science
- name: Matplotlib
  slug: matplotlib
- name: Python
  slug: python
seo_title: Taille de la figure Matplotlib – Comment changer la taille du graphique
  en Python avec plt.figsize()
seo_desc: "When creating plots using Matplotlib, you get a default figure size of\
  \ 6.4 for the width and 4.8 for the height (in inches).\nIn this article, you'll\
  \ learn how to change the plot size using the following: \n\nThe figsize() attribute.\
  \ \nThe set_figwidth()..."
---

Lorsque vous créez des graphiques avec Matplotlib, vous obtenez une taille de figure par défaut de 6,4 pour la largeur et 4,8 pour la hauteur (en pouces).

Dans cet article, vous apprendrez à changer la taille du graphique en utilisant les éléments suivants :

* L'attribut `figsize()`.
* La méthode `set_figwidth()`.
* La méthode `set_figheight()`.
* Le paramètre `rcParams`.

Commençons !

## Comment changer la taille du graphique dans Matplotlib avec `plt.figsize()`

Comme indiqué dans la section précédente, les paramètres par défaut (en pouces) pour les graphiques Matplotlib sont 6,4 de large et 4,8 de haut. Voici un exemple de code :

```python
import matplotlib.pyplot as plt

x = [2,4,6,8]
y = [10,3,20,4]

plt.plot(x,y)

plt.show()
```

Dans le code ci-dessus, nous avons d'abord importé `matplotlib`. Nous avons ensuite créé deux listes — `x` et `y` — avec des valeurs à tracer.

En utilisant `plt.plot()`, nous avons tracé la liste `x` sur l'axe des x et la liste `y` sur l'axe des y : `plt.plot(x,y)`.

Enfin, `plt.show()` affiche le graphique. Voici à quoi ressemblerait le graphique avec les paramètres de taille de figure par défaut :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/matplotlib.PNG)
_graphique matplotlib avec les paramètres de taille de figure par défaut_

Nous pouvons changer la taille du graphique ci-dessus en utilisant l'attribut `figsize()` de la fonction `figure()`.

L'attribut `figsize()` prend deux paramètres — l'un pour la largeur et l'autre pour la hauteur.

### Voici à quoi ressemble la syntaxe :

```txt
figure(figsize=(LARGEUR,HAUTEUR))
```

Voici un exemple de code :

```python
import matplotlib.pyplot as plt

x = [2,4,6,8]
y = [10,3,20,4]

plt.figure(figsize=(10,6))
plt.plot(x,y)

plt.show()
```

Nous avons ajouté une nouvelle ligne de code : `plt.figure(figsize=(10,6))`. Cela modifiera la largeur et la hauteur du graphique.

Voici à quoi ressemblerait le graphique :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/matplotlib1.PNG)
_graphique matplotlib avec une taille de figure modifiée_

## Comment changer la largeur du graphique dans Matplotlib avec `set_figwidth()`

Vous pouvez utiliser la méthode `set_figwidth()` pour changer la largeur d'un graphique.

Nous passerons la valeur à laquelle la largeur doit être modifiée en tant que paramètre de la méthode.

Cette méthode ne changera pas la valeur par défaut ou prédéfinie de la hauteur du graphique.

Voici un exemple de code :

```python
import matplotlib.pyplot as plt

x = [2,4,6,8]
y = [10,3,20,4]

plt.figure().set_figwidth(15)
plt.plot(x,y)

plt.show()
```

En utilisant la méthode `set_figwidth()`, nous avons défini la largeur du graphique à 10. Voici à quoi ressemblerait le graphique :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/matplotlib2.PNG)
_graphique matplotlib avec une largeur modifiée_

## Comment changer la hauteur du graphique dans Matplotlib avec `set_figheight()`

Vous pouvez utiliser la méthode `set_figheight()` pour changer la hauteur d'un graphique.

Cette méthode ne changera pas la valeur par défaut ou prédéfinie de la largeur du graphique.

Voici un exemple de code :

```python
import matplotlib.pyplot as plt

x = [2,4,6,8]
y = [10,3,20,4]

plt.figure().set_figheight(2)
plt.plot(x,y)

plt.show()
```

En utilisant `set_figheight()` dans l'exemple ci-dessus, nous avons défini la hauteur du graphique à 2. Voici à quoi ressemblerait le graphique :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/matplotlib3.PNG)
_graphique matplotlib avec une hauteur modifiée_

## Comment changer la taille par défaut du graphique dans Matplotlib avec `rcParams`

Vous pouvez remplacer la taille par défaut du graphique dans Matplotlib en utilisant le paramètre `rcParams`.

Cela est utile lorsque vous souhaitez que tous vos graphiques suivent une taille particulière. Cela signifie que vous n'avez pas à changer la taille de chaque graphique que vous créez.

Voici un exemple avec deux graphiques :

```python
import matplotlib.pyplot as plt

x = [2,4,6,8]
y = [10,3,20,4]

plt.rcParams['figure.figsize'] = [4, 4]
plt.plot(x,y)

plt.show()
```

```python
a = [5,10,15,20]
b = [10,20,30,40]

plt.plot(a,b)
```

En utilisant le paramètre `figure.figsize`, nous avons défini la largeur et la hauteur par défaut à 4 : `plt.rcParams['figure.figsize'] = [4, 4]`. Ces paramètres changeront la largeur et la hauteur par défaut des deux graphiques.

Voici les graphiques :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/matplotlib4.PNG)
_graphique matplotlib avec une taille par défaut modifiée_

![Image](https://www.freecodecamp.org/news/content/images/2023/01/matplotlib5-1.PNG)
_graphique matplotlib avec une taille par défaut modifiée_

## Résumé

Dans cet article, nous avons parlé des différentes façons de changer la taille d'un graphique dans Matplotlib.

Nous avons vu des exemples de code et une représentation visuelle des graphiques. Cela nous a aidé à comprendre comment chaque méthode peut être utilisée pour changer la taille d'un graphique.

Nous avons discuté des méthodes suivantes utilisées pour changer la taille du graphique dans Matplotlib :

* L'attribut `figsize()` peut être utilisé lorsque vous souhaitez changer la taille par défaut d'un graphique spécifique.
* La méthode `set_figwidth()` peut être utilisée pour changer uniquement la largeur d'un graphique.
* La méthode `set_figheight()` peut être utilisée pour changer uniquement la hauteur d'un graphique.
* Le paramètre `rcParams` peut être utilisé lorsque vous souhaitez remplacer la taille par défaut du graphique pour tous vos graphiques. Contrairement à l'attribut `figsize()` qui cible un graphique spécifique, le paramètre `rcParams` cible tous les graphiques d'un projet.

Bon codage !