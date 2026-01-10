---
title: Dictionnaire Python – Comment créer un Dict en Python (Hashmap)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-03-01T15:44:00.000Z'
originalURL: https://freecodecamp.org/news/python-dictionary-how-to-create-a-dict-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/Shittu-Olumide-Python-Dictionary
seo_title: Dictionnaire Python – Comment créer un Dict en Python (Hashmap)
---

How-to-Create-a-Dict-in-Python--Hashmap--1.png
tags:
- name: dictionnaire
  slug: dictionnaire
- name: Python
  slug: python
seo_title: null
seo_desc: 'Par Shittu Olumide

  Bienvenue dans cet article Python sur la création d\'un dictionnaire.

  Un dictionnaire (également appelé hashmap dans d\'autres langues) est un regroupement non ordonné
  de paires clé-valeur en Python. Puisque chaque valeur peut être accessible par sa clé correspondante,
  ...'
---

Par Shittu Olumide

Bienvenue dans cet article Python sur la création d'un dictionnaire.

Un dictionnaire (également appelé hashmap dans d'autres langues) est un regroupement non ordonné de paires clé-valeur en Python. Puisque chaque valeur peut être accessible par sa clé correspondante, il offre un moyen pratique de stocker et de récupérer des données.

Dans ce tutoriel, nous couvrirons les bases de la création d'un dictionnaire en Python, y compris comment initialiser un dictionnaire vide, comment ajouter et supprimer des paires clé-valeur, et comment accéder et travailler avec les données du dictionnaire.

J'illustrerai chaque concept avec des exemples et démontrerai chaque opération avec des extraits de code.

À la fin de cet article, vous devriez savoir tout ce dont vous avez besoin pour utiliser les dictionnaires en Python, de leur création à leur modification. Et vous devriez être capable d'utiliser ces informations pour résoudre des problèmes et construire des programmes plus sophistiqués.

Commençons !

## Comment créer un Dict en Python

Un dictionnaire est un type de structure de données qui nous permet de stocker des paires clé-valeur. Il est également connu sous le nom de hashmap dans d'autres langages de programmation.

Les dictionnaires sont utiles lorsque nous voulons stocker des données de manière facilement accessible et modifiable. Pour créer des dictionnaires en Python, nous utilisons des accolades, le constructeur `dict()`, et la méthode `fromkeys()`.

### Comment créer un dict en utilisant des accolades

Les accolades `{ }` sont une méthode de création d'un dictionnaire en Python. Nous pouvons enfermer une liste séparée par des virgules de paires clé-valeur dans des accolades pour créer un dictionnaire. Nous utilisons un deux-points et une virgule pour séparer chaque paire de clés-valeurs des autres.

Voici un exemple :

```py
MyDict = {1: "apple", 2: "banana", 3: "orange"}

```

Dans cet exemple, nous avons créé un dictionnaire `MyDict` avec trois paires clé-valeur :
`1: "apple"`, `2: "banana"`, et `3: "orange"`. Les clés sont des entiers et les valeurs sont des chaînes de caractères.

### Comment créer un dict en utilisant le constructeur `dict()`

Une autre méthode pour créer un dictionnaire en Python est d'utiliser le constructeur `dict()`. Le constructeur `dict()` produit un dictionnaire à partir d'un itérable de paires clé-valeur en entrée. Les paires clé-valeur peuvent être passées à la fois sous forme de liste de tuples et d'arguments. Par exemple, considérons ce qui suit.

Créons un dictionnaire à partir d'un tuple.

```py
# créer un dictionnaire à partir d'un tuple en utilisant le constructeur dict()
MyDict = dict(one=1, two=2, three=3)
print(MyDict)

```

Sortie :

```py
{'one': 1, 'two': 2, 'three': 3}

```

Créons un dictionnaire à partir d'une liste de tuples.

```py
# créer un dictionnaire à partir d'une liste de tuples en utilisant le constructeur dict()
MyList = [('one', 1), ('two', 2), ('three', 3)]
MyDict = dict(MyList)
print(MyDict)

```

Sortie :

```py
{'one': 1, 'two': 2, 'three': 3}

```

Dans le premier exemple, nous avons créé un dictionnaire avec les paires clé-valeur `one:1`, `two:2`, et `three:3` en les passant comme arguments au constructeur `dict()`.

Dans le deuxième exemple, nous avons créé un dictionnaire en utilisant une liste de tuples `MyList`, qui contient les mêmes paires clé-valeur que précédemment. Nous avons passé `MyList` comme argument au constructeur `dict()`, qui retourne un dictionnaire avec les mêmes paires clé-valeur.

Le constructeur `dict()` peut également être utilisé pour créer un dictionnaire vide en ne passant aucun argument. Par exemple, `MyDict = dict()` crée un dictionnaire vide `MyDict`.

### Comment créer un dict en utilisant la méthode `fromkeys()`

Vous pouvez également utiliser la méthode intégrée `fromkeys()` pour créer un dictionnaire en sélectionnant des clés à partir d'une séquence et en définissant des valeurs par défaut.

Le premier argument de la méthode `fromkeys()` est une liste de clés, et le deuxième argument (facultatif) est la valeur qui sera attribuée à chaque clé après sa définition. Les valeurs seront automatiquement définies sur None si le deuxième argument n'est pas fourni.

Exemple

```py
keys = ['a', 'b', 'c']
values = 0  # définir la valeur par défaut à 0

MyDict = dict.fromkeys(keys, values)
print(MyDict)

```

Sortie :

```py
{'a': 0, 'b': 0, 'c': 0}

```

Dans l'exemple ci-dessus, nous avons passé une liste de clés `['a', 'b', 'c']` et une valeur par défaut `0` à la méthode `fromkeys()`. Nous obtenons un nouveau dictionnaire où toutes les clés sont définies avec la valeur `0`.

## Conclusion

Dans ce tutoriel, nous avons appris comment créer un dict en Python en nous concentrant sur trois méthodes : en utilisant des accolades, le constructeur `dict()`, et la méthode `fromkeys()`. Avec ces connaissances, vous pouvez créer et manipuler des dictionnaires en toute confiance dans votre code Python.

Restons en contact sur [Twitter](https://www.twitter.com/Shittu_Olumide_) et sur [LinkedIn](https://www.linkedin.com/in/olumide-shittu). Vous pouvez également vous abonner à ma chaîne [YouTube](https://www.youtube.com/channel/UCNhFxpk6hGt5uMCKXq0Jl8A).

Bon codage !