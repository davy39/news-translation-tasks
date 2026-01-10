---
title: Python .zip() – Fonction Zip en Python
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-04-13T18:28:32.000Z'
originalURL: https://freecodecamp.org/news/python-zip-zip-function-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/zip.jpg
tags:
- name: Python
  slug: python
seo_title: Python .zip() – Fonction Zip en Python
seo_desc: "When you use the zip() function in Python, it takes two or more data sets\
  \ and \"zips\" them together. This returns an object containing pairs of items derived\
  \ from the data sets. It groups these items in the order of their indexes. \nLet\
  \ me break it dow..."
---

Lorsque vous utilisez la fonction `zip()` en Python, elle prend deux ensembles de données ou plus et les "zip" ensemble. Cela retourne un objet contenant des paires d'éléments dérivés des ensembles de données. Elle groupe ces éléments dans l'ordre de leurs index. 

Laissez-moi décomposer un peu plus : le premier élément du premier ensemble de données est apparié avec le premier élément du deuxième ensemble de données, les deuxièmes éléments des deux ensembles de données sont appariés ensemble, et ainsi de suite.

Dans cet article, nous verrons comment utiliser la fonction `zip()` en Python avec quelques exemples.

## Comment Utiliser la Fonction `zip()` en Python

Voici la syntaxe de la fonction `zip()` en Python :

```txt
zip(ensembleDonnées1, ensembleDonnées2, ...)
```

Voici un exemple pour démontrer comment cela fonctionne :

```python
noms = ("John", "Jane", "Jade")
âges = (2, 4, 6)

print(zip(noms, âges))
# <zip object at 0x7f8d5915cc40>
```

Dans le code ci-dessus, nous avons créé deux `tuples` – `noms` et `âges`. 

Nous avons ensuite utilisé la fonction `zip()` : `print(zip(noms, âges))`.

Mais nous n'obtenons pas réellement les données appariées retournées. Cela est dû au fait que nous devons spécifier dans quelle structure de données elles seront zippées. Voici comment faire :

```python
noms = ("John", "Jane", "Jade")
âges = (2, 4, 6)

zippé = zip(noms, âges)

print(tuple(zippé))
# (('John', 2), ('Jane', 4), ('Jade', 6))
```

Nous avons stocké nos données zippées dans une variable appelée `zippé` et lors de l'impression, nous les avons imbriquées dans un `tuple` : `print(tuple(zippé))`.

J'ai commenté la sortie du code : `(('John', 2), ('Jane', 4), ('Jade', 6))`. Comme vous pouvez le voir ci-dessus, chaque élément à un index donné a été apparié avec un autre élément au même index de l'autre ensemble de données.

Vous pouvez également retourner les données imbriquées dans une `liste`. Voici comment :

```python
noms = ("John", "Jane", "Jade")
âges = (2, 4, 6)

zippé = zip(noms, âges)

print(list(zippé))
# [('John', 2), ('Jane', 4), ('Jade', 6)]
```

C'est la même chose que le dernier exemple, mais au lieu d'avoir `tuple(zippé)`, nous avons utilisé `list(zippé)`.

De la même manière, nous pouvons également utiliser `dict` et `set`, mais les données retournées lorsque nous utilisons `set` sont susceptibles d'être non ordonnées.

Nous pouvons parcourir les données zippées en faisant ceci :

```python
noms = ("John", "Jane", "Jade", "John")
âges = (2, 4, 6)

zippé = zip(noms, âges)

for (x, y) in zippé:
    print(x, y)

# John 2
# Jane 4
# Jade 6
```

## Conclusion

Dans cet article, nous avons appris ce qu'est la fonction `zip()` et ce qu'elle fait en Python.

Nous avons vu comment zipper deux ensembles de données et retourner leurs paires en utilisant différentes structures de données. 

Enfin, nous avons vu comment parcourir et imprimer les données zippées.

Bon codage !