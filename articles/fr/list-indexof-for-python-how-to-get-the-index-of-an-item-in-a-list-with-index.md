---
title: List indexOf pour Python ? Comment obtenir l'index d'un élément dans une liste
  avec .index()
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-07-12T17:51:33.000Z'
originalURL: https://freecodecamp.org/news/list-indexof-for-python-how-to-get-the-index-of-an-item-in-a-list-with-index
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/kelly-sikkema-377gw1wN0Ic-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: List indexOf pour Python ? Comment obtenir l'index d'un élément dans une
  liste avec .index()
seo_desc: "There are various techniques that we can use to get the index of a list\
  \ item in Python, such as the enumerate() function, a for loop, and the index()\
  \ method. \nIn this article, we'll focus on how to get the index of an item in a\
  \ list using the index()..."
---

Il existe diverses techniques que nous pouvons utiliser pour obtenir l'index d'un élément de liste en Python, telles que la fonction `enumerate()`, une boucle `for` et la méthode `index()`.

Dans cet article, nous nous concentrerons sur la manière d'obtenir l'index d'un élément dans une liste en utilisant la méthode `index()`.

Nous commencerons par examiner la syntaxe de la méthode `index()`, puis nous verrons quelques exemples pour vous aider à comprendre comment l'utiliser dans votre code.

## Quelle est la syntaxe de la méthode `index()` en Python ?

La méthode `index()` prend en paramètre l'élément dont l'index doit être retourné. Mais ce n'est pas le seul paramètre que vous pouvez utiliser dans la méthode `index()`.

Voici à quoi ressemble la syntaxe :

```txt
list.index(item, start, end)
```

Voici une description des paramètres ci-dessus :

* `item` désigne l'élément dont l'index doit être recherché.
* `start`, qui est un paramètre optionnel, désigne le point de départ où la recherche d'un élément doit commencer. Cela est utile lorsque vous avez un élément avec des doublons.
* `end` désigne l'index où la recherche de l'index d'un élément doit s'arrêter/se terminer. Ce paramètre est également optionnel.

## Comment obtenir l'index d'un élément dans une liste avec `.index()`

Dans cette section, vous verrez comment utiliser la méthode `index()` pour obtenir l'index d'un élément dans une liste. Vous verrez également comment utiliser tous les paramètres.

Voici le premier exemple :

```python
listOfNames = ['John', 'Jane', 'Doe', 'Ihechikara']

print(listOfNames.index('Jane'))
# 1
```

Dans le code ci-dessus, nous avons créé une liste de noms : `listOfNames = ['John', 'Jane', 'Doe', 'Ihechikara']`.

En utilisant la méthode `index()`, nous avons obtenu l'index de "Jane" dans la liste : `listOfNames.index('Jane')`

Lorsque cela a été imprimé dans la console, 1 a été affiché.

Au cas où vous ne comprenez pas pourquoi 1 a été retourné, notez que les listes sont indexées à partir de zéro – donc le premier élément est 0, le deuxième est 1 et ainsi de suite. C'est-à-dire :

'John' => index 0  
'Jane' => index 1  
'Doe' => index 2  
'Ihechikara' => index 3

### Comment utiliser les paramètres `start` et `end` avec la méthode `index()` en Python

Dans cette section, vous verrez comment utiliser les paramètres `start` et `end` avec la méthode `index()`.

```python
listOfNames = ['John', 'Jane', 'Doe', 'Ihechikara', 'John', 'Jane', 'Doe', 'Ihechikara']

print(listOfNames.index('Jane', 2))
# 5
```

Dans la liste ci-dessus, nous avons des noms avec des valeurs en double : `['John', 'Jane', 'Doe', 'Ihechikara', 'John', 'Jane', 'Doe', 'Ihechikara']`.

Mais nous voulons obtenir l'index du deuxième élément "Jane". Sachant que l'index du premier élément "Jane" est 1, nous pouvons commencer la recherche après cet élément.

Ainsi, pour commencer la recherche à partir d'un index après le premier élément "Jane", nous avons ajouté un autre paramètre à la méthode `index()` : `listOfNames.index("Jane", 2)`. Maintenant, la recherche de l'index d'un élément avec une valeur de "Jane" commencera à partir de l'index 2.

Nous avons obtenu 5 car c'est l'index du deuxième élément "Jane". Sans spécifier un index de départ, la méthode `index()` retournera le premier index d'un élément spécifié.

Voici un deuxième exemple pour comprendre comment utiliser le paramètre `end()` :

```python
listOfNames = ['John', 'Jane', 'Doe', 'Ihechikara', 'John', 'Jane', 'Doe', 'Ihechikara']

print(listOfNames.index("Jane", 2,4))
# ValueError: 'Jane' is not in list
```

Dans l'exemple ci-dessus, nous avons spécifié l'index 2 comme index `start` et l'index 4 comme index `end`. Nous recherchons l'index de "Jane" dans la plage spécifiée (index 2 et 4).

Nous avons obtenu une erreur : `ValueError: 'Jane' is not in list`. Cela est dû au fait que "Jane" ne se trouve pas dans la plage spécifiée.

Rappelons que nous avons commencé à partir de l'index 2, donc :

Index 2 (`start` index) => 'Doe'  
Index 3 => 'Ihechikara'  
Index 4 (`end` index) => 'John'

D'après les index ci-dessus, vous pouvez voir que "Jane" n'existe pas dans la plage, donc une erreur a été retournée.

Vous obtenez une ValueError dans une liste lorsque :

* L'élément recherché n'existe pas dans la liste.
* L'élément recherché ne se trouve pas dans une plage de recherche spécifiée (start et end).

## Résumé

Dans cet article, nous avons parlé de la méthode `index()` en Python. Vous l'utilisez pour trouver l'index d'un élément dans une liste.

Nous avons vu quelques exemples qui montrent comment utiliser la méthode `index()` et ses paramètres `start` et `end`.

Bon codage !