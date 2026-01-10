---
title: Python Itertools
subtitle: ''
seo_title: Python Itertools, chain, isSlice, et izip Expliqués avec des Exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/python-itertools-chain-isslice-and-izip-explained-with-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d34740569d1a4ca367b.jpg
tags:
- name: Python
  slug: python
- name: toothbrush
  slug: toothbrush
---

Itertools est un module Python de fonctions qui retournent des générateurs, qui sont des objets qui ne fonctionnent que lorsqu'on itère dessus.

## chain()

La fonction chain() prend plusieurs itérateurs comme arguments. Elle parcourt chaque élément de chaque itérable passé, puis retourne un seul itérateur avec le contenu de tous les itérateurs passés.

```py
import itertools
list(itertools.chain([1, 2], [3, 4]))

# Sortie
# [1, 2, 3, 4]
```

## islice()

La fonction islice() retourne des éléments spécifiques de l'itérable passé.

Elle prend les mêmes arguments que l'opérateur slice() pour les listes : start, stop, et step. Start et stop sont optionnels.

```py
import itertools
list(itertools.islice(count(), 5))

# Sortie
# [0, 1, 2, 3, 4]
```

## izip()

izip() retourne un itérateur qui combine les éléments des itérateurs passés en tuples.

Il fonctionne de manière similaire à zip(), mais retourne un itérateur au lieu d\'une liste.

```py
import itertools
list(izip([1, 2, 3], ['a', 'b', 'c']))

# Sortie
# [(1, 'a'),(2, 'b'),(3, 'c')]
```

## Plus d'informations :

* [Apprendre l\'analyse de données avec Python – Un cours gratuit de 4 heures](https://www.freecodecamp.org/news/learn-data-analysis-with-python-course/)
* [Python Multithread : se faufiler à travers un goulot d\'étranglement I/O 🐍](https://www.freecodecamp.org/news/multithreaded-python/)