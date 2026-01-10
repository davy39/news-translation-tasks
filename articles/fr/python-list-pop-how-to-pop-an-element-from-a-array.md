---
title: Python list.pop() – Comment supprimer un élément d'un tableau
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2023-02-09T01:31:22.000Z'
originalURL: https://freecodecamp.org/news/python-list-pop-how-to-pop-an-element-from-a-array
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/kelly-sikkema--1_RZL8BGBM-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: Python list.pop() – Comment supprimer un élément d'un tableau
seo_desc: "Python has various built-in methods you can use to interact with elements\
  \ stored in a list. These methods let you add, access, modify, and remove elements.\
  \ \nIn this article, you'll learn how to remove elements in a Python list using:\n\
  \nThe pop() metho..."
---

Python dispose de diverses méthodes intégrées que vous pouvez utiliser pour interagir avec les éléments stockés dans une [liste](https://www.freecodecamp.org/news/how-to-make-a-list-in-python-declare-lists-in-python-example/). Ces méthodes vous permettent d'ajouter, d'accéder, de modifier et de supprimer des éléments. 

Dans cet article, vous apprendrez à supprimer des éléments dans une liste Python en utilisant :

* La méthode `pop()`.
* La méthode `remove()`.
* Le mot-clé `del`. 

## Comment supprimer un élément d'une liste Python en utilisant la méthode `pop()`

Vous pouvez utiliser la méthode `pop()` pour supprimer soit un élément spécifique dans une liste, soit pour supprimer le dernier élément. 

Lorsqu'un paramètre est utilisé, vous pouvez spécifier l'élément particulier (en utilisant le numéro d'index de l'élément) à supprimer. Sans paramètre, le dernier élément est supprimé. 

Voici quelques exemples : 

### Exemple `pop()` #1

```python
names = ['Ihechikara', 'Doe', 'John', 'Jane']

names.pop(2)

print(names)
# ['Ihechikara', 'Doe', 'Jane']
```

Dans l'exemple ci-dessus, nous avons créé une liste appelée `names` avec quatre éléments : `['Ihechikara', 'Doe', 'John', 'Jane']`. 

En utilisant la méthode `pop()`, nous avons spécifié que l'élément à l'index 2 devait être supprimé : `names.pop(2)`. 

La liste résultante avait trois éléments : `['Ihechikara', 'Doe', 'Jane']`

### Exemple `pop()` #2

Dans l'exemple suivant, nous allons utiliser la méthode `pop()` sans aucun paramètre ou en spécifiant un élément particulier à supprimer. 

```python
names = ['Ihechikara', 'Doe', 'John', 'Jane']

names.pop()

print(names)
# ['Ihechikara', 'Doe', 'John']
```

Sans passer l'index d'un élément en tant que paramètre à la méthode `pop()` dans la liste ci-dessus, le dernier élément de la liste a été supprimé. 

C'est-à-dire : `names.pop()`. 

## Comment supprimer un élément d'une liste Python en utilisant la méthode `remove()`

Avec la méthode `remove()`, vous pouvez passer un paramètre — la valeur de l'élément à supprimer. 

Vous ne pouvez pas utiliser l'index des éléments comme paramètre, et vous ne pouvez pas utiliser la méthode `remove()` sans paramètre. Cela entraînera une erreur. 

Voici un exemple :

```python
names = ['Ihechikara', 'Doe', 'John', 'Jane']

names.remove("Doe")

print(names)
# ['Ihechikara', 'John', 'Jane']
```

Dans la liste ci-dessus, nous avons spécifié l'élément à supprimer en utilisant sa valeur : `names.remove("Doe")`. Ainsi, l'élément avec une valeur de "Doe" a été supprimé de la liste. 

Une erreur aurait été levée si nous avions utilisé l'index de l'élément — `names.remove(1)` — ou utilisé la méthode sans paramètre — `names.remove()`.

De même, supprimer un élément qui n'existe pas lèverait une erreur. 

## Comment supprimer un élément d'une liste Python en utilisant le mot-clé `del`

Avec le mot-clé `del`, vous pouvez spécifier quel élément vous souhaitez supprimer en utilisant son index. Vous pouvez également spécifier une plage d'éléments à supprimer. 

Voici quelques exemples :

### Exemple `del` #1

```python
names = ['Ihechikara', 'Doe', 'John', 'Jane']

del names[2]

print(names)
# ['Ihechikara', 'Doe', 'Jane']
```

Dans le code ci-dessus, nous avons supprimé l'élément à l'index 2 : `del names[2]`. 

Notez que l'index n'est pas spécifié entre parenthèses mais entre crochets.

### Exemple `del` #2

```python
names = ['Ihechikara', 'Doe', 'John', 'Jane']

del names[0:2]

print(names)
# ['John', 'Jane']
```

Dans le code ci-dessus, nous avons spécifié une plage pour les nombres à supprimer : `del names[0:2]`

Avec cela, nous disons : "supprimez tous les éléments de l'index 0 et arrêtez-vous juste avant l'index 2". L'index 2 ne sera pas supprimé — il est utilisé comme un point où la suppression s'arrêtera. 

## Résumé

Dans cet article, nous avons parlé des listes en Python. 

Nous avons vu les différentes méthodes que vous pouvez utiliser pour supprimer des éléments dans une liste. 

En utilisant des exemples de code, nous avons vu des applications pratiques de chaque méthode.

Bon codage !