---
title: Comment changer la taille de la police de la légende dans Matplotlib
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2023-03-14T15:04:13.000Z'
originalURL: https://freecodecamp.org/news/how-to-change-legend-fontsize-in-matplotlib
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/isaac-smith-6EnTPvPPL6I-unsplash--2-.jpg
tags:
- name: Matplotlib
  slug: matplotlib
- name: Python
  slug: python
seo_title: Comment changer la taille de la police de la légende dans Matplotlib
seo_desc: "You can modify different properties of a plot — color, size, label, title\
  \ and so on — when working with Matplotlib. \nIn this article, you'll learn what\
  \ a legend is in Matplotlib, and how to use some of its parameters to make your\
  \ plots more relatable..."
---

Vous pouvez modifier différentes propriétés d'un graphique — couleur, taille, étiquette, titre, etc. — lorsque vous travaillez avec Matplotlib. 

Dans cet article, vous apprendrez ce qu'est une légende dans Matplotlib et comment utiliser certains de ses paramètres pour rendre vos graphiques plus explicites. 

Vous apprendrez ensuite comment changer la taille de la police d'une légende Matplotlib en utilisant :

* Le paramètre `fontsize`. 
* Le paramètre `prop`.

## Qu'est-ce qu'une légende dans Matplotlib ?

Une légende est une fonction Matplotlib utilisée pour décrire les éléments qui composent un graphique. 

Considérez le graphique ci-dessous :

```python
import matplotlib.pyplot as plt

# créer un graphique
x = [1, 4, 6, 8]
y = [2, 5, 6, 2]

plt.plot(x, y)

plt.legend(["Données"], loc="upper right")

plt.show()
```

![Image](https://www.freecodecamp.org/news/content/images/2023/03/matplotlib-legend.png)
_graphique matplotlib avec une légende_

Dans le graphique ci-dessus, nous avons décrit le tracé à l'aide d'une `legend`. Une description de "Données" a été attribuée à la légende, et elle a été placée dans le coin supérieur droit du graphique en utilisant la valeur `upper right` du paramètre `loc`. 

Avec la fonction `legend`, vous pouvez attribuer différentes descriptions à chaque ligne d'un graphique. 

Voici un exemple :

```python
import matplotlib.pyplot as plt

age = [1, 4, 6, 8]
nombre = [4, 5, 6, 2, 1]

plt.plot(age)
plt.plot(nombre)

plt.legend(["âge", "nombre"], loc ="upper right")

plt.show()
```

![Image](https://www.freecodecamp.org/news/content/images/2023/03/matplotlib-legend.PNG)
_graphique à deux lignes avec différentes descriptions de légende_

Dans le graphique ci-dessus, nous avons utilisé la fonction `legend` pour décrire chaque ligne du tracé. 

Cela permet à toute personne visualisant le graphique de savoir plus facilement que la ligne bleue indique l'`âge` tandis que la ligne orange indique le `nombre` dans le graphique. 

Vous pouvez changer la position de la légende en utilisant les valeurs suivantes pour le paramètre `loc` : 

* `best`
* `upper right`
* `upper left`
* `lower left`
* `lower right`
* `right`
* `center left`
* `center right`
* `lower center`
* `upper center`
* `center`

## Comment changer la taille de la police de la légende dans Matplotlib en utilisant le paramètre `fontsize` 

Vous pouvez modifier la taille de la police d'une légende Matplotlib en spécifiant une valeur de taille de police pour le paramètre `fontsize`. 

Voici à quoi ressemble la taille de police par défaut de la légende :

```python
import matplotlib.pyplot as plt

age = [1, 4, 6, 8]
nombre = [4, 5, 6, 2, 1]

plt.plot(age)
plt.plot(nombre)

plt.legend(["âge", "nombre"], loc ="upper right")

plt.show()
```

![Image](https://www.freecodecamp.org/news/content/images/2023/03/matplotlib-legend-1.PNG)
_graphique matplotlib avec la taille de police de légende par défaut_

Voici un autre exemple de code incluant le paramètre `fontsize` :

```python
import matplotlib.pyplot as plt

age = [1, 4, 6, 8]
nombre = [4, 5, 6, 2, 1]

plt.plot(age)
plt.plot(nombre)

plt.legend(["âge", "nombre"], fontsize="20", loc ="upper left")

plt.show()
```

Voici à quoi ressemblerait la légende :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/matplotlib-legend-fontsize-parameter-1.PNG)
_taille de la légende matplotlib en utilisant le paramètre fontsize_

Nous avons attribué une taille de police de 20 au paramètre `fontsize` pour obtenir la taille de la légende dans l'image ci-dessus : `fontsize="20"`. 

Vous remarquerez également que la légende a été placée dans le coin supérieur gauche du graphique en utilisant le paramètre `loc`.

## Comment changer la taille de la police de la légende dans Matplotlib en utilisant le paramètre `prop` 

Une autre façon de changer la taille de la police d'une légende est d'utiliser le paramètre `prop` de la fonction `legend`. 

Voici comment l'utiliser :

```python
import matplotlib.pyplot as plt

age = [1, 4, 6, 8]
nombre = [4, 5, 6, 2, 1]

plt.plot(age)
plt.plot(nombre)

plt.legend(["âge", "nombre"], prop = { "size": 20 }, loc ="upper left")

plt.show()
```

En utilisant le paramètre `prop`, nous avons spécifié une taille de police de 20 : `prop = { "size": 20 }`. 

Voici le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/matplotlib-legend-fontsize-parameter-2.PNG)
_taille de la légende matplotlib en utilisant le paramètre prop_

## Résumé

Dans cet article, nous avons parlé de la fonction `legend` dans Matplotlib. Elle peut être utilisée pour décrire les éléments qui composent un graphique. 

Nous avons d'abord vu ce qu'est une légende dans Matplotlib, ainsi que quelques exemples pour montrer son utilisation de base et ses paramètres. 

Nous avons ensuite vu comment utiliser les paramètres `fontsize` et `prop` pour changer la taille de la police d'une légende Matplotlib. 

Bon codage !