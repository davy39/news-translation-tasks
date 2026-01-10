---
title: Ajouter de la couleur dans Matplotlib – Comment changer la couleur des lignes
  dans Matplotlib
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2023-03-13T21:55:25.000Z'
originalURL: https://freecodecamp.org/news/how-to-change-color-in-matplotlib
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/isaac-smith-6EnTPvPPL6I-unsplash--1-.jpg
tags:
- name: Matplotlib
  slug: matplotlib
- name: Python
  slug: python
seo_title: Ajouter de la couleur dans Matplotlib – Comment changer la couleur des
  lignes dans Matplotlib
seo_desc: "Matplotlib is a Python library used for data visualization, and creating\
  \ interactive plots and graphs. \nIn this article, you'll learn how to add colors\
  \ to your Matplotlib plots using parameter values provided by the Matplotlib plot()\
  \ function.\nYou'll..."
---

Matplotlib est une bibliothèque Python utilisée pour la [data visualization](https://www.freecodecamp.org/news/data-visualization-tools-guide), et la création de tracés et de graphiques interactifs. 

Dans cet article, vous apprendrez comment ajouter des couleurs à vos graphiques Matplotlib en utilisant les valeurs de paramètres fournies par la fonction `plot()` de Matplotlib.

Vous apprendrez comment changer la couleur d'un tracé en utilisant :

* Des noms de couleurs. 
* Des abréviations de couleurs.
* Des valeurs RGB/RGBA. 
* Des valeurs hexadécimales.

C'est parti !

## Comment changer la couleur des lignes dans Matplotlib

Par défaut, la couleur des tracés dans Matplotlib est le bleu. C'est-à-dire :

```python
import matplotlib.pyplot as plt

x = [5,10,15,20]
y = [10,20,30,40]

plt.plot(x,y)
plt.show()
```

![Image](https://www.freecodecamp.org/news/content/images/2023/03/matplotlib-default-line-color.PNG)

Pour changer la couleur d'un tracé, ajoutez simplement un paramètre `color` à la fonction `plot` et spécifiez la valeur de la couleur. 

Voici quelques exemples :

### Exemple n°1 : Comment changer la couleur des lignes dans Matplotlib

Dans cet exemple, nous allons changer la couleur du tracé en utilisant un nom de couleur. 

```python
import matplotlib.pyplot as plt

x = [5,10,15,20]
y = [10,20,30,40]

plt.plot(x,y, color='red')
plt.show()
```

![Image](https://www.freecodecamp.org/news/content/images/2023/03/matplotlib-red-line-color.PNG)

Dans l'exemple ci-dessus, nous avons assigné la valeur 'red' au paramètre `color` : `color='red'`.

### Exemple n°2 : Comment changer la couleur des lignes dans Matplotlib

Vous pouvez utiliser des abréviations pour spécifier la couleur à utiliser pour le tracé. À savoir : 

* `'b'` = bleu
* `'g'` = vert
* `'r'` = rouge
* `'c'` = cyan
* `'m'` = magenta
* `'y'` = jaune
* `'k'` = noir
* `'w'` = blanc

Voici un exemple de code :

```python
import matplotlib.pyplot as plt

x = [5,10,15,20]
y = [10,20,30,40]

plt.plot(x,y, color='m')
plt.show()
```

![Image](https://www.freecodecamp.org/news/content/images/2023/03/matplotlib-magenta-line-color.PNG)

### Exemple n°3 : Comment changer la couleur des lignes dans Matplotlib

Vous pouvez également utiliser des valeurs RGB et RGBA (rouge, vert, bleu, alpha), et des valeurs hexadécimales. 

Voici un exemple qui crée un tracé avec une couleur jaune en utilisant RGB :

```python
import matplotlib.pyplot as plt

x = [5,10,15,20]
y = [10,20,30,40]

plt.plot(x,y, color=(1.0, 0.92, 0.23))
plt.show()
```

![Image](https://www.freecodecamp.org/news/content/images/2023/03/matplotlib-yellow-line-color.PNG)

Voici un autre exemple qui utilise une valeur hexadécimale pour créer un tracé vert :

```python
import matplotlib.pyplot as plt

x = [5,10,15,20]
y = [10,20,30,40]

plt.plot(x,y, color='#00FF00')
plt.show()
```

![Image](https://www.freecodecamp.org/news/content/images/2023/03/matplotlib-green-line-color.PNG)

## Résumé

Dans cet article, nous avons expliqué comment changer la couleur des tracés dans Matplotlib. 

Nous avons vu des exemples montrant comment utiliser des noms de couleurs, des abréviations, des valeurs RGB/RGBA et des valeurs hexadécimales pour modifier la couleur d'un tracé dans Matplotlib. 

Bon codage !