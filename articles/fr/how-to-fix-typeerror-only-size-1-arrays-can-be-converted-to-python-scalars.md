---
title: 'TypeError: only size-1 arrays can be converted to Python scalars'
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-09-30T21:39:43.000Z'
originalURL: https://freecodecamp.org/news/how-to-fix-typeerror-only-size-1-arrays-can-be-converted-to-python-scalars
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/brett-jordan-XWar9MbNGUY-unsplash.jpg
tags:
- name: error
  slug: error
- name: error handling
  slug: error-handling
- name: Python
  slug: python
seo_title: 'TypeError: only size-1 arrays can be converted to Python scalars'
seo_desc: "In Python, you can use the numpy library when working with arrays and certain\
  \ math concepts like matrices and linear algebra. \nBut like every other aspect\
  \ of learning and working with a programming language, errors are unavoidable. \n\
  In this article, ..."
---

En Python, vous pouvez utiliser la bibliothèque `numpy` lorsque vous travaillez avec des tableaux et certains concepts mathématiques comme les matrices et l'algèbre linéaire. 

Mais comme pour tout autre aspect de l'apprentissage et du travail avec un langage de programmation, les erreurs sont inévitables. 

Dans cet article, vous apprendrez à corriger l'erreur "TypeError: only size-1 arrays can be converted to Python scalars" qui se produit principalement lors de l'utilisation de la bibliothèque `numpy`. 

## Qu'est-ce qui cause l'erreur `TypeError: only size-1 arrays can be converted to Python scalars` en Python ?

L'erreur "TypeError: only size-1 arrays can be converted to Python scalars" est levée lorsque nous passons un tableau à une méthode qui n'accepte qu'un seul paramètre. 

Voici un exemple :

```python
import numpy as np

y = np.array([1, 2, 3, 4])
x = np.int(y)

print(x)

# TypeError: only size-1 arrays can be converted to Python scalars

```

Le code ci-dessus lève l'erreur "TypeError: only size-1 arrays can be converted to Python scalars" parce que nous avons passé le tableau `y` à la méthode `int()` de NumPy. Cette méthode ne peut accepter qu'un seul paramètre. 

Dans la section suivante, vous verrez quelques solutions pour cette erreur. 

## Comment corriger l'erreur `TypeError: only size-1 arrays can be converted to Python scalars` en Python

Il existe deux solutions générales pour corriger l'erreur "TypeError: only size-1 arrays can be converted to Python scalars".

### Solution n°1 – Utiliser la fonction `np.vectorize()`

La fonction `np.vectorize()` peut accepter une séquence ou un tableau comme paramètre. Lorsqu'elle est affichée, elle retourne un tableau.

Voici un exemple :

```python
import numpy as np

vector = np.vectorize(np.int_)
y = np.array([2, 4, 6, 8])
x = vector(y)

print(x)
# [2, 4, 6, 8]
```

Dans l'exemple ci-dessus, nous avons créé une variable `vector` qui va "vectoriser" tout paramètre qui lui est passé : `np.vectorize(np.int_)`. 

Nous avons ensuite créé un tableau et l'avons stocké dans la variable `y` : `np.array([2, 4, 6, 8])`. 

En utilisant la variable `vector` créée initialement, nous avons passé le tableau `y` comme paramètre : `x = vector(y)`. 

Lors de l'affichage, nous obtenons le tableau — `[2, 4, 6, 8]`.

### Solution n°2 – Utiliser la fonction `map()`

La fonction `map()` accepte deux paramètres dans ce cas — la méthode NumPy et le tableau. 

```python
import numpy as np

y = np.array([2, 4, 6, 8])
x = np.array(list(map(np.int_, y)))

print(x)
# [2, 4, 6, 8]
```

Dans l'exemple ci-dessus, nous avons imbriqué la fonction `map()` dans une méthode `list()` afin d'obtenir le tableau retourné sous forme de liste et non d'objet map. 

### Solution n°3 – Utiliser la méthode `astype()`

Nous pouvons utiliser la méthode `astype()` pour convertir un tableau NumPy en entiers. Cela empêchera la levée de l'erreur "TypeError: only size-1 arrays can be converted to Python scalars". 

Voici comment faire : 

```python
import numpy as np

vector = np.vectorize(np.int_)
y = np.array([2, 4, 6, 8])
x = y.astype(int)

print(x)
# [2 4 6 8]
```

## Résumé

Dans cet article, nous avons parlé de l'erreur "TypeError: only size-1 arrays can be converted to Python scalars" en Python.

Elle est levée lorsque nous passons un tableau comme paramètre à une méthode `numpy` qui n'accepte qu'un seul paramètre. 

Pour corriger l'erreur, nous avons utilisé différentes méthodes comme la fonction `np.vectorize()`, la fonction `map()` et la méthode `astype()`. 

Bon codage ! 💡