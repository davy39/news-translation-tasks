---
title: Python enumerate() – Qu'est-ce que la fonction Enumerate en Python?
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-06-08T19:56:15.000Z'
originalURL: https://freecodecamp.org/news/python-enumerate-what-is-the-enumerate-function-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/edge2edge-media-uKlneQRwaxY-unsplash--1-.jpg
tags:
- name: Python
  slug: python
seo_title: Python enumerate() – Qu'est-ce que la fonction Enumerate en Python?
seo_desc: "The enumerate() function in Python takes in a data collection as a parameter\
  \ and returns an enumerate object. \nThe enumerate object is returned in a key-value\
  \ pair format. The key is the corresponding index of each item and the value is\
  \ the items. \nI..."
---

La fonction `enumerate()` en Python prend une collection de données en tant que paramètre et retourne un objet enumerate. 

L'objet enumerate est retourné dans un format de paire clé-valeur. La clé est l'index correspondant de chaque élément et la valeur est l'élément lui-même. 

Dans cet article, nous verrons quelques exemples de l'utilisation de la fonction `enumerate()` en Python.

Nous parlerons de la syntaxe et des paramètres, de l'utilisation de `enumerate()`, et de la manière de parcourir un objet enumerate. 

## Quelle est la syntaxe de la fonction enumerate() en Python ?

Voici la syntaxe de la fonction `enumerate()` et ses paramètres :

```txt
enumerate(iterable, start)
```

La fonction `enumerate()` prend deux paramètres : `iterable` et `start`.

* `iterable` est la collection de données passée pour être retournée sous forme d'objet enumerate.
* `start` est l'index de départ pour l'objet enumerate. La valeur par défaut est 0, donc si vous omettez ce paramètre, 0 sera utilisé comme premier index. 

## Comment utiliser la fonction `enumerate()` en Python

Dans cette section, nous examinerons quelques exemples pour nous aider à comprendre la syntaxe et les paramètres présentés dans la dernière section. 

Notez que nous devons spécifier le type de format de données (comme les listes, les ensembles, etc.) dans lequel l'objet enumerate sera stocké lorsqu'il est retourné. Vous comprendrez mieux cela avec les exemples.

### Exemple #1 de la fonction `enumerate()` en Python

```python
names = ["John", "Jane", "Doe"]
enumNames = enumerate(names)

print(list(enumNames))
# [(0, 'John'), (1, 'Jane'), (2, 'Doe')]
```

Dans l'exemple ci-dessus, nous avons créé une liste appelée `names`. 

Nous avons ensuite converti la variable `names` en un objet enumerate : `enumerate(names)`, et l'avons stockée dans une variable appelée `enumNames`. 

Nous voulions que l'objet enumerate soit stocké dans une liste lorsqu'il est retourné, donc nous avons fait ceci : `list(enumNames)`. 

Lorsqu'il est imprimé dans la console, voici à quoi ressemblait le résultat : `[(0, 'John'), (1, 'Jane'), (2, 'Doe')]`

Comme vous pouvez le voir dans le résultat, ils sont en paires clé-valeur. Le premier index est 0 qui est attaché au premier élément de la liste `names`, le second est 1 et est attaché au deuxième élément de la liste `names`, et ainsi de suite. 

Dans notre exemple, nous n'avons utilisé que le premier paramètre. 

Dans l'exemple suivant, nous utiliserons les deux paramètres afin que vous puissiez comprendre comment fonctionne le deuxième paramètre. 

### Exemple #2 de la fonction `enumerate()` en Python

```python
names = ["John", "Jane", "Doe"]
enumNames = enumerate(names, 10)

print(list(enumNames))
# [(10, 'John'), (11, 'Jane'), (12, 'Doe')]
```

Dans l'exemple ci-dessus, nous avons ajouté un deuxième paramètre à la fonction `enumerate()` : `enumerate(names, 10)`.

Le deuxième paramètre est 10. Cela signifiera l'index de départ pour les clés (index) dans l'objet enumerate. 

Voici notre résultat : `[(10, 'John'), (11, 'Jane'), (12, 'Doe')]`

D'après le résultat, nous pouvons voir que le premier index est 10, le second 11, et ainsi de suite.

## Comment parcourir un objet Enumerate en Python

Voici un exemple simple qui montre comment nous pouvons parcourir un objet enumerate en Python : 

```python
names = ["John", "Jane", "Doe"]
enumNames = enumerate(names)

for item in enumNames:
    print(item)
    
# (0, 'John')
# (1, 'Jane')
# (2, 'Doe')

```

En utilisant une boucle `for`, nous avons itéré à travers l'objet enumerate : `for item in enumNames:`

Lorsqu'ils sont imprimés, nous avons obtenu les éléments de l'objet listés dans leur ordre de paire clé-valeur correspondant. 

Nous pouvons également utiliser le deuxième paramètre comme nous l'avons fait dans la dernière section pour changer la valeur de départ des clés. 

## Résumé

Dans cet article, nous avons parlé de la fonction `enumerate()` en Python. 

Nous avons commencé par examiner la syntaxe et les paramètres de la fonction. 

Nous avons ensuite vu quelques exemples qui nous ont aidés à comprendre comment utiliser la fonction `enumerate()` et ses paramètres. 

Enfin, nous avons vu comment parcourir les objets enumerate en Python en utilisant la boucle `for`. 

Bon codage !