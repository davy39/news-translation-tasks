---
title: Tri de listes Python – Comment ordonner les listes en Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-07-26T16:31:59.000Z'
originalURL: https://freecodecamp.org/news/python-list-sorting-how-to-order-lists-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/sort-list-in-python.png
tags:
- name: Python
  slug: python
seo_title: Tri de listes Python – Comment ordonner les listes en Python
seo_desc: "By Dillion Megida\nThere are many reasons you might want to sort lists\
  \ in your Python applications. \nIn this article, I'll show you how to order lists\
  \ in ascending and descending order depending on what you need to do.\nWhat is a\
  \ List in Python?\nA list..."
---

Par Dillion Megida

Il existe de nombreuses raisons pour lesquelles vous pourriez vouloir trier des listes dans vos applications Python.

Dans cet article, je vais vous montrer comment ordonner des listes par ordre croissant et décroissant en fonction de ce que vous devez faire.

## Qu'est-ce qu'une `List` en Python ?

Une liste est un type de données en Python où vous pouvez stocker plusieurs valeurs de différents types de données (y compris des listes imbriquées).

Voici des exemples de listes :

```python
numList = [1, 2, 3, 4, 5]

stringList = ["banana", "orange", "apple"]

mixedList = [1, "banana", "orange", [5, 6]]
```

Vous pouvez accéder aux éléments d'une liste en utilisant leur position d'index. Les positions d'index commencent à 0 dans les listes :

```python
stringList = ["banana", "orange", "apple"]

print(stringList[1])
# "orange"
```

## Comment trier des listes en Python

Vous pouvez trier une liste en Python en utilisant la méthode `sort()`.

La méthode `sort()` vous permet d'ordonner les éléments d'une liste. Voici la syntaxe :

```python
list.sort(reverse=True|False, key=sortFunction)
```

La méthode accepte deux arguments optionnels :
* `reverse` : qui trie la liste dans l'ordre inverse (décroissant) si `True` ou dans l'ordre régulier (croissant) si `False` (ce qui est le cas par défaut)
* `key` : une fonction que vous fournissez pour décrire la méthode de tri

Par défaut, vous pouvez ordonner des chaînes de caractères et des nombres par ordre croissant, sans passer d'argument à cette méthode :

```python
items = ["orange", "cashew", "banana"]

items.sort()
# ['banana', 'cashew', 'orange']
```

Dans l'exemple ci-dessus, vous pouvez voir que la liste triée a **b** en premier (dans banana), puis **c** (dans cashew), car cela vient après b, et enfin, **o** (dans orange) qui est plus tard dans l'ordre alphabétique.

Notez que cette méthode modifie le tableau original.

Pour l'ordre décroissant, vous pouvez passer l'argument reverse :

```python
items = [6, 8, 10, 5, 7, 2]

items.sort(reverse=True)
# [10, 8, 7, 6, 5, 2]
```

En passant `True` à l'argument `reverse`, vous voyez les nombres dans la liste `items` triés dans l'ordre inverse, c'est-à-dire l'ordre décroissant.

### Comment spécifier une fonction de tri

Que se passe-t-il si vous essayez cela sur une liste de dictionnaires ? Voyons cela :

```python
items = [{
    'name': 'John',
    'age': 40
}, {
    'name': 'Mike',
    'age': 45
}, {
    'name': 'Jane',
    'age': 33
}, {
    'name': 'Asa',
    'age': 42
}]

items.sort()
```

Vous obtiendrez une erreur car les dictionnaires ne sont pas ordonnables. C'est là que vous pouvez spécifier un critère de tri en utilisant l'argument `key` :

```python
items = [
  {
  'name': 'John',
  'age': 40
  },
  {   
    'name': 'Mike',
    'age': 45
  },
  {   
    'name': 'Jane',
    'age': 33
  },
  {   
    'name': 'Asa',
    'age': 42
  }
]

def sortFn(dict):
  return dict['age']

items.sort(key=sortFn)
# [
#   {'name': 'Jane', 'age': 33},
#   {'name': 'John', 'age': 40},
#   {'name': 'Asa', 'age': 42},
#   {'name': 'Mike', 'age': 45}
# ]
```

Comme vous pouvez le remarquer dans le bloc de code ci-dessus, en utilisant une fonction de tri, nous avons spécifié que la décision de tri doit être basée sur la clé `age` dans chaque dictionnaire.

Si l'argument `reverse` est passé à `True` ici, les dictionnaires triés seront dans l'ordre décroissant.

Voici un autre exemple utilisant une fonction de tri :

```python
items = ["cow", "elephant", "duck"]

def sortFn(value):
    return len(value)

items.sort(key=sortFn, reverse=True)
# ['elephant', 'duck', 'cow']
```

Dans ce cas, la fonction de tri retourne la longueur des valeurs dans la liste comme critère pour le processus de tri. En passant `reverse` à `True`, vous pouvez voir que la liste triée a la chaîne de caractères la plus longue en premier, suivie de la plus courte.

## Conclusion

Lors de la création d'applications, il existe de nombreux scénarios pour trier des listes. Cela pourrait être le tri d'une liste de fichiers basée sur une clé `last_opened`. Cela pourrait être le tri de produits basée sur une clé `price`. Comme vous pouvez le voir, il existe de nombreux critères que vous pouvez utiliser dans des applications réelles.

Dans cet article, nous avons vu comment trier des listes en Python par ordre croissant et décroissant en utilisant différentes méthodes.