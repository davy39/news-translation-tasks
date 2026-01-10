---
title: Aplatir une liste en Python – Aplatissement de listes imbriquées
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-03-20T17:02:03.000Z'
originalURL: https://freecodecamp.org/news/list-flatten-in-python-flattening-nested-lists
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/flattenList.png
tags:
- name: Python
  slug: python
seo_title: Aplatir une liste en Python – Aplatissement de listes imbriquées
seo_desc: 'Lists are one of the core data structures of Python. Due to their flexibility,
  there are a lot of things you can do with lists. And one of those things is turning
  a list of lists into a single list.

  It is also possible to turn a list of dictionaries,...'
---

Les listes sont l'une des structures de données de base de Python. Grâce à leur flexibilité, il y a énormément de choses que vous pouvez faire avec les listes. L'une de ces choses consiste à transformer une liste de listes en une seule liste.

Il est également possible de transformer une liste de dictionnaires, une liste de tuples ou une liste contenant à la fois des tuples et des dictionnaires en une seule liste. Nous allons apprendre plusieurs façons de procéder dans cet article.


## Ce que nous allons aborder
- [Comment aplatir une liste avec la fonction `sum()` ](#heading-comment-aplatir-une-liste-avec-la-fonction-sum)
- [Comment aplatir une liste avec une boucle `for` imbriquée](#heading-comment-aplatir-une-liste-avec-une-boucle-for-imbriquee)
- [Comment aplatir une liste avec la compréhension de liste](#heading-comment-aplatir-une-liste-avec-la-comprehension-de-liste)
- [Comment aplatir une liste avec Numpy](#heading-comment-aplatir-une-liste-avec-numpy)
- [Comment aplatir une liste avec le package `more_itertools`](#heading-comment-aplatir-une-liste-avec-le-package-moreitertools)
- [Conclusion](#heading-conclusion)


## Comment aplatir une liste avec la fonction `sum()` 
Vous utilisez généralement la fonction `sum()` pour faire ce que son nom indique : additionner des nombres. Mais vous pouvez également l'utiliser pour aplatir une liste de listes en une seule liste.

La fonction `sum()` prend un itérable de nombres que vous souhaitez additionner et un point de départ facultatif :

```py
sum(iterable, starting_point)
```

Si vous spécifiez la liste de listes que vous souhaitez aplatir comme itérable et une liste vide comme point de départ, la liste sera aplatie. Voici comment faire :

```py
first_list_of_lists = [[12, 45, 2], [3, 7, 3, 1], [23, 89, 10, 9]]
flattened_first_list_of_lists = sum(first_list_of_lists, [])

print(flattened_first_list_of_lists) # [12, 45, 2, 3, 7, 3, 1, 23, 89, 10, 9]
```

Vous pouvez voir que la liste a été aplatie.

Mais cette méthode ne fonctionnera pas pour une liste de tuples, une liste de dictionnaires ou une liste de tuples et de dictionnaires, car vous ne pouvez pas les concaténer.

L'utilisation de la fonction `sum()` ne fonctionnera pas non plus pour une liste bidimensionnelle contenant des chaînes de caractères ou une liste tridimensionnelle. Vous verrez comment aplatir une liste dans ces circonstances au fil de votre lecture.


## Comment aplatir une liste avec une boucle `for` imbriquée
Une boucle `for` imbriquée est une boucle `for` à l'intérieur d'une autre boucle `for`. Voici comment vous pouvez aplatir une liste de listes avec une boucle `for` :

```py
list_of_lists = [[12, 45, 2], [3, 7, 3, 1], [23, 89, 10, 9]]

flattened_list_of_lists = []
for sublist in list_of_lists:
    for num in sublist:
        flattened_list_of_lists.append(num)
        
print(flattened_list_of_lists) # [12, 45, 2, 3, 7, 3, 1, 23, 89, 10, 9]
```

Le code ci-dessus parcourt chaque dimension du tableau et les ajoute à une liste vide que j'ai appelée `flattened_list_of_lists` avec la méthode `append()`.

Cette méthode serait également idéale pour aplatir une liste imbriquée de chaînes de caractères :

```py
list_of_names = [["Olsen", "Joy"], ["Di Marco", "Ascensio"], ["Modric", "Ann"]]

flattened_list_of_names = []
for sub_list in list_of_names:
    for name in sub_list:
        flattened_list_of_names.append(name)

print(flattened_list_of_names)
```

L'utilisation d'une boucle imbriquée vous permettrait également d'aplatir une liste de tuples, une liste de dictionnaires ou une liste combinant listes, tuples et dictionnaires.

Aplatir une liste de tuples :

```py
list_of_tuples = [1, 2, 3, (4, 5), (2, 4, 24)]

flattened_list_of_tuples = []
for sub_list in list_of_lists:
    for num in sub_list:
        flattened_list_of_tuples.append(num)

print(flattened_list_of_tuples) # [12, 45, 2, 3, 7, 3, 1, 23, 89, 10, 9]
```

Aplatir une liste de dictionnaires :

```py
list_of_dicts = [ {1,  2, 3}, { "d": 4, "e": 5, "f": 6}]

flattened_list_of_dicts = []
for sub_list in list_of_dicts:
    for num in sub_list:
        flattened_list_of_dicts.append(num)

print(flattened_list_of_dicts) # [1, 2, 3, 'd', 'e', 'f']
```

Aplatir une liste contenant une liste, un tuple et un dictionnaire :

```py
multi_data_list = [[1, 2, 3], (4, 5, 6), {7, 8, 9}, {"a": 1, "b": 2, "c": 3, "z": 0}]

flattened_multi_data_lists = []
for sub_list in multi_data_list:
    for data in sub_list:
        flattened_multi_data_lists.append(data)

print(flattened_multi_data_lists)
```


## Comment aplatir une liste avec la compréhension de liste
La compréhension de liste vous aide à créer une liste à partir d'une chaîne de caractères ou d'une autre liste. Il est donc possible de créer une nouvelle liste à partir d'une liste de listes. Voici à quoi ressemble la syntaxe de la compréhension de liste :

```py
[expression for element in iterable_data if condition == True]
```

N'oubliez pas que vous pouvez itérer à travers des chaînes de caractères, vous pouvez donc créer une liste à partir d'une chaîne de cette façon :

```py
my_str = "freeCodeCamp"
list_from_letters = [letter for sub_list in my_str for letter in sub_list]

print(list_from_letters) # ['f', 'r', 'e', 'e', 'C', 'o', 'd', 'e', 'C', 'a', 'm', 'p']
```

Vous pouvez également créer une liste à partir d'une liste de listes de cette manière – en aplatissant la liste au passage :

```py
list_of_names = [["Olsen", "Joy"], ["Di Marco", "Ascensio"], ["Modric", "Ann"]]
flattened_names = [name for sub_list in list_of_names for name in sub_list]

print(flattened_names) # ['Olsen', 'Joy', 'Di Marco', 'Ascensio', 'Modric', 'Ann']
```


## Comment aplatir une liste avec Numpy
Vous pouvez utiliser la fonction `concatenate()` de la bibliothèque `numpy` pour aplatir une liste de cette manière :

```py
import numpy as np

first_list_of_lists = [[1, 2], [4, 5]]
second_list_of_lists = [[6, 7], [8, 9]]

flattened_first_list_of_lists = np.concatenate(first_list_of_lists) 
flattened_second_list_of_lists = np.concatenate(second_list_of_lists) 

print(flattened_first_list_of_lists) # [1 2 4 5]
print(flattened_second_list_of_lists) # [6 7 8 9]
```


## Comment aplatir une liste avec le package `more_itertools`
Le package `more_itertools` est un ensemble d'utilitaires qui fournit des fonctions et des méthodes pour parcourir n'importe quelle donnée itérable en Python. Vous pouvez l'installer en exécutant `pip install more_itertools` ou `pip3 install more_itertools`.

`more_itertools` possède une fonction `flatten()` pour aplatir une liste :

```py
from more_itertools import flatten

list_of_lists = [[2, 4, 5], [3, 9, 5, 2], [2, 4, 1, 2 ]]
flattened_list = list(flatten(list_of_lists)) 

print(flattened_list) # [2, 4, 5, 3, 9, 5, 2, 2, 4, 1, 2]
```

Si vous avez également une liste contenant des listes profondément imbriquées, `more_itertools` fournit une fonction `collapse()` que vous pouvez utiliser pour les décomposer toutes en une seule liste :

```py
from more_itertools import collapse

list_of_lists_2 = [[1, 2], [[3, 4]], [5, [6, 7]]]
flattened_list_of_lists_2 = list(collapse(list_of_lists_2))

print(flattened_list_of_lists_2) # [1, 2, 3, 4, 5, 6, 7]
```


## Conclusion
Aplatir une liste n'est pas une tâche insurmontable grâce à la disponibilité de la fonction `sum()`, de la compréhension de liste et de bibliothèques comme `Numpy` et `more_itertools`. 

Même si vous ne voulez pas le faire de la « manière Pythonic », vous pouvez utiliser une boucle `for` imbriquée comme vous l'avez vu ici.

Et si vous avez une liste avec des listes profondément imbriquées, la fonction `collapse()` de `more_itertools` peut vous aider à les aplatir.

Si vous avez apprécié la lecture de cet article, n'hésitez pas à le partager avec vos amis et votre famille.