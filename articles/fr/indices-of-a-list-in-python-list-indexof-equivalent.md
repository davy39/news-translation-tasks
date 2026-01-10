---
title: Indices d'une Liste en Python – Équivalent de List IndexOf()
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-04-06T07:49:00.000Z'
originalURL: https://freecodecamp.org/news/indices-of-a-list-in-python-list-indexof-equivalent
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/listIndex.png
tags:
- name: Python
  slug: python
- name: Python 3
  slug: python3
seo_title: Indices d'une Liste en Python – Équivalent de List IndexOf()
seo_desc: 'Python has several methods and hacks for getting the index of an item in
  iterable data like a list, tuple, and dictionary.

  In this article, we are looking at how you can get the index of a list item with
  the index() method. I’ll also show you a funct...'
---

Python dispose de plusieurs méthodes et astuces pour obtenir l'index d'un élément dans des données itérables comme une liste, un tuple et un dictionnaire.

Dans cet article, nous examinons comment obtenir l'index d'un élément de liste avec la méthode `index()`. Je vais également vous montrer une fonction équivalente à la méthode `index()`.


## Ce que nous allons couvrir
- [Qu'est-ce que la méthode `index()` d'une Liste ?](#heading-quest-ce-que-la-methode-index-dune-liste)
- [Comment obtenir l'Index d'un élément de Liste avec la méthode `index()`](#heading-comment-obtenir-lindex-dun-element-de-liste-avec-la-methode-index)
- [Comment utiliser les paramètres `start` et `stop` de la méthode `index()`](#heading-comment-utiliser-les-parametres-start-et-stop-de-la-methode-index)
- [Comment obtenir l'Index d'un élément de Liste avec la fonction `enumerate()`](#heading-comment-obtenir-lindex-dun-element-de-liste-avec-la-fonction-enumerate)
- [Conclusion](#heading-conclusion)


## Qu'est-ce que la méthode `index()` d'une Liste ?
La méthode `index()` fait ce que son nom implique – elle permet d'obtenir l'index d'un élément dans une liste. Elle prend l'élément dont vous souhaitez rechercher l'index dans la liste et retourne sa position dans cette liste.

Outre l'élément que vous souhaitez rechercher, la méthode `index()` prend également les paramètres optionnels `start` et `stop`. `start` est la position à partir de laquelle vous souhaitez que la méthode `index()` commence à rechercher l'élément, et `stop` est la position à laquelle vous souhaitez qu'elle arrête de rechercher l'élément.

Voici à quoi ressemble la syntaxe de `index()` :

```py
list.index(item_to_search_for, start_position, stop_position)
```

Soyez conscient que les éléments d'une liste sont indexés à partir de zéro. Ainsi, le premier élément prend l'index `0`, le deuxième élément prend `1`, le troisième prend `2`, et ainsi de suite.

Cela ne signifie pas que si `6` est le dernier index dans une liste, la longueur est 6. Dans ce cas, la longueur est `7`. Si vous souhaitez commencer à référencer une liste de 7 éléments à partir du dernier élément, le dernier élément sera `-1`, et le premier élément sera `-7`.

![start-graph--9-](https://www.freecodecamp.org/news/content/images/2023/04/start-graph--9-.png)


## Comment obtenir l'Index d'un élément de Liste avec la méthode `index()`
Pour obtenir l'index d'un élément dans une liste, attachez la méthode `index()` à la liste et passez l'élément à la méthode `index()` :

```py
herbivores = ["Giraffe", "Goat", "Sheep", "Cattle", "Antelope", "Rabbit"]

print(herbivores.index("Goat")) # Sortie : 1
```

Vous pouvez également extraire l'index dans une variable séparée de cette manière :

```py
herbivores = ["Giraffe", "Goat", "Sheep", "Cattle", "Antelope", "Rabbit"]
index_of_goat = herbivores.index("Goat") # Sortie : 1

print(index_of_goat)
```

Si l'élément est un doublon, la méthode `index()` ne prendrait en compte que la première occurrence et ignorerait les autres :

```py
herbivores = ["Goat", "Giraffe", "Sheep", "Cattle", "Antelope", "Giraffe", "Rabbit"]
index_of_giraffe = herbivores.index("Giraffe") 

print(index_of_giraffe) # Sortie : 1

omnivores = ["Pig", "Dogs", "Duck", "Bears", "Ostrich", "Hen", "Warthog", "Bears", "Dogs"]
index_of_dogs = omnivores.index("Dogs")

print(index_of_dogs) # Sortie : 1
```


## Comment utiliser les paramètres `start` et `stop` de la méthode `index()`
Comme déjà mentionné, vous pouvez utiliser les paramètres `start` et `stop` pour spécifier où la méthode `index()` doit commencer à rechercher l'élément et arrêter de le rechercher.

Voyons d'abord comment fonctionne le paramètre `start`. Dans la liste `omnivores` ci-dessous, recherchons la position de la deuxième occurrence de `Dogs` :

```py
omnivores = ["Pig", "Dogs", "Duck", "Ostrich", "Warthog", "Dogs", "Bears"]

# Sachant que la première occurrence est à l'index `1`, nous pouvons commencer la recherche à partir de l'index 2
index_of_dogs = omnivores.index("Dogs", 2 )

print(index_of_dogs) # Sortie : 5
```

Vous pouvez obtenir la position de la première occurrence de `Dogs` en spécifiant `0` comme `start` et n'importe quoi entre `2` et `4` comme `stop` :

```py
omnivores = ["Pig", "Dogs", "Duck", "Ostrich", "Warthog", "Dogs", "Bears"]
index_of_dogs = omnivores.index("Dogs", 0, 4 )

print(index_of_dogs) # Sortie : 1
```

Si l'élément n'est pas dans la plage que vous spécifiez, vous obtenez une exception `ValueError` :

```py
omnivores = ["Pig", "Dogs", "Duck", "Ostrich", "Warthog", "Dogs", "Bears"]
index_of_dogs = omnivores.index("Dogs", 2, 4 )

print(index_of_dogs) # Sortie : ValueError: 'Dogs' is not in list
```


## Comment obtenir l'Index d'un élément de Liste avec la fonction `enumerate()`
La fonction `enumerate()` peut suivre les positions des éléments dans une liste, un tuple ou d'autres séquences itérables de données. Ainsi, nous pouvons également l'utiliser pour obtenir l'index d'un élément dans une liste.

Cela fait de `enumerate()` un équivalent de la méthode `index()`. La différence est que `enumerate()` retourne les positions sous forme de liste et peut retourner les indices de plusieurs occurrences du même élément.

Voici un exemple :

```py
herbivores = ["Goat", "Ram", "Sheep", "Cattle", "Antelope", "Giraffe", "Rabbit"]
index_of_ram = [i for i, j in enumerate(herbivores) if j == 'Ram']

print(index_of_ram) # [1]
```

Dans le code ci-dessus :
* J'ai utilisé une compréhension de liste pour trouver l'index de l'élément dans la liste qui contient la chaîne `Ram`
* La fonction enumerate() a itéré sur la liste `herbivores` et a suivi la position de chaque élément dans la liste
* La fonction `enumerate()` prend un objet itérable (dans ce cas, herbivores) comme argument et retourne un itérateur qui génère des paires de la forme (index, élément) pour chaque élément dans l'itérable
* `i` représente l'index de l'élément dans la liste `herbivores` et `j` représente l'élément lui-même
* L'instruction `if` vérifie si l'élément est égal à la chaîne `Ram`. Si c'est le cas, alors l'index de l'élément (`i`) est ajouté à la liste résultante

La fonction `enumerate()` retournerait également les indices des éléments en double :

```py
omnivores = ["Pig", "Dogs", "Duck", "Ostrich", "Warthog", "Dogs", "Bears"]
indices_of_dogs = [i for i, e in enumerate(omnivores) if e == 'Dogs']

print(indices_of_dogs) # [1, 5]
```


## Conclusion
La méthode `index()` de `list` est une manière simple d'obtenir la position [ou l'index] d'un élément dans une liste.

Mais malheureusement, `index()` ne prendrait en compte que le premier élément et ignorerait les autres s'il s'agit d'un doublon. C'est pourquoi nous avons également examiné comment obtenir les indices des éléments en double dans une liste.

Donc, si ce que vous voulez faire est d'obtenir les positions de plusieurs éléments dans une liste, alors enumerate() est la bonne option pour vous.

Bon codage !