---
title: Fonction Pop en Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-29T23:35:00.000Z'
originalURL: https://freecodecamp.org/news/pop-function-in-python
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d49740569d1a4ca36ed.jpg
tags:
- name: Python
  slug: python
- name: toothbrush
  slug: toothbrush
seo_title: Fonction Pop en Python
seo_desc: 'What is the pop function?

  The method pop() removes and returns the last element from a list. There is an optional
  parameter which is the index of the element to be removed from the list. If no index
  is specified, a.pop() removes and returns the last ...'
---

# Qu'est-ce que la fonction pop ?

La méthode pop() supprime et retourne le dernier élément d'une liste. Il existe un paramètre optionnel qui est l'index de l'élément à supprimer de la liste. Si aucun index n'est spécifié, a.pop() supprime et retourne le dernier élément de la liste. Si l'index passé à la méthode pop() n'est pas dans la plage, elle génère une exception IndexError: pop index out of range.

### Exemple d'utilisation

```py
cities = ['New York', 'Dallas', 'San Antonio', 'Houston', 'San Francisco'];

print "La ville supprimée est : ", cities.pop()
print "La ville à l'index 2 est : ", cities.pop(2)
```

#### **Sortie**

```text
La ville supprimée est : San Francisco
La ville à l'index 2 est : San Antonio
```

### Fonctionnalité de base de la pile

La méthode `pop()` est souvent utilisée en conjonction avec `append()` pour implémenter une fonctionnalité de pile de base dans une application Python.

```py
stack = []

for i in range(5):
    stack.append(i)

while len(stack):
    print(stack.pop())
```

#### **Plus d'informations :**

La documentation officielle pour `pop()` peut être trouvée [ici](https://docs.python.org/3.6/tutorial/datastructures.html)