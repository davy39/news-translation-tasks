---
title: Int Max en Python – Taille maximale d'un entier
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2023-04-03T18:20:55.000Z'
originalURL: https://freecodecamp.org/news/maximum-integer-size-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/thomas-t-OPpCbAAKWv8-unsplash.jpg
tags:
- name: Python
  slug: python
- name: Python 3
  slug: python3
seo_title: Int Max en Python – Taille maximale d'un entier
seo_desc: "You can check the maximum integer size in Python using the maxsize property\
  \ of the sys module. \nIn this article, you'll learn about the maximum integer size\
  \ in Python. You'll also see the differences in Python 2 and Python 3.\nThe maximum\
  \ value of an ..."
---

Vous pouvez vérifier la taille maximale d'un entier en Python en utilisant la propriété `maxsize` du module `sys`.

Dans cet article, vous apprendrez tout sur la taille maximale d'un entier en Python. Vous verrez également les différences entre Python 2 et Python 3.

La valeur maximale d'un entier ne devrait pas vous préoccuper. Avec la version actuelle de Python, le type de données `int` a la capacité de stocker des valeurs entières très grandes.

## Quelle est la taille maximale d'un entier en Python ?

En Python 2, vous pouvez vérifier la taille maximale d'un entier en utilisant la propriété `maxint` du module `sys`.

Voici un exemple :

```python
import sys

print(sys.maxint)
# 9223372036854775807
```

Python 2 a un type de données intégré appelé `long` qui stocke des valeurs entières plus grandes que ce que `int` peut gérer.

Vous pouvez faire la même chose pour Python 3 en utilisant `maxsize` :

```python
import sys

print(sys.maxsize)
# 9223372036854775807
```

Notez que la valeur dans le code ci-dessus n'est pas la capacité maximale du type de données `int` dans la version actuelle de Python.

Si vous multipliez ce nombre (9223372036854775807) par un très grand nombre en Python 2, un `long` sera retourné.

En revanche, Python 3 peut gérer l'opération :

```python
import sys

print(sys.maxsize * 7809356576809509573609874689576897365487536545894358723468)
# 72028601076372765770200707816364342373431783018070841859646251155447849538676
```

Vous pouvez effectuer des opérations avec des valeurs entières grandes en Python sans vous soucier d'atteindre la valeur maximale.

La seule limitation à l'utilisation de ces grandes valeurs est la mémoire disponible dans les systèmes où elles sont utilisées.

## Résumé

Dans cet article, vous avez appris tout sur la taille maximale d'un entier en Python. Vous avez également vu des exemples de code qui ont montré la taille maximale d'un entier en Python 2 et Python 3.

Avec Python moderne, vous n'avez pas à vous soucier d'atteindre une taille maximale d'entier. Assurez-vous simplement d'avoir suffisamment de mémoire pour gérer le calcul des opérations sur des entiers très grands, et vous êtes prêt à partir.

Bon codage !