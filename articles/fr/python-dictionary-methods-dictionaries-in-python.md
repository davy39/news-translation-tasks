---
title: Méthodes des dictionnaires Python – Les dictionnaires en Python
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-07-28T15:32:21.000Z'
originalURL: https://freecodecamp.org/news/python-dictionary-methods-dictionaries-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/python_dict.png
tags:
- name: dictionary
  slug: dictionary
- name: Python
  slug: python
seo_title: Méthodes des dictionnaires Python – Les dictionnaires en Python
seo_desc: "In Python, a dictionary is one of the core data structures. It is a sequence\
  \ of key-value pairs separated by commas and surrounded by curly braces. \n\nIf\
  \ you’re familiar with JavaScript, Python dictionaries are like JavaScript objects.\n\
  Python provides..."
---

En Python, un dictionnaire est l'une des structures de données principales. Il s'agit d'une séquence de paires clé-valeur séparées par des virgules et entourées d'accolades.

![keyvalue](https://www.freecodecamp.org/news/content/images/2022/07/keyvalue.png)

Si vous connaissez JavaScript, les dictionnaires Python sont similaires aux objets JavaScript.

Python fournit plus de 10 méthodes pour travailler avec les dictionnaires.

Dans cet article, je vais vous montrer comment créer un dictionnaire en Python et travailler avec celui-ci en utilisant ces méthodes.

## Ce que nous allons couvrir
- [Comment créer un dictionnaire en Python](#comment-creer-un-dictionnaire-en-python)
- [Méthodes pour travailler avec les dictionnaires Python](#methodes-pour-travailler-avec-les-dictionnaires-python)
  - [Comment utiliser la méthode de dictionnaire `get()`](#comment-utiliser-la-methode-de-dictionnaire-get)
  - [Comment utiliser la méthode de dictionnaire `items()`](#comment-utiliser-la-methode-de-dictionnaire-items)
  - [Comment utiliser la méthode de dictionnaire `keys()`](#comment-utiliser-la-methode-de-dictionnaire-keys)
  - [Comment utiliser la méthode de dictionnaire `values()`](#comment-utiliser-la-methode-de-dictionnaire-values)
  - [Comment utiliser la méthode de dictionnaire `pop()`](#comment-utiliser-la-methode-de-dictionnaire-pop)
  - [Comment utiliser la méthode de dictionnaire `popitem()`](#comment-utiliser-la-methode-de-dictionnaire-popitem)
  - [Comment utiliser la méthode de dictionnaire `update()`](#comment-utiliser-la-methode-de-dictionnaire-update)
  - [Comment utiliser la méthode de dictionnaire `copy()`](#comment-utiliser-la-methode-de-dictionnaire-copy)
  - [Comment utiliser la méthode de dictionnaire `clear()`](#comment-utiliser-la-methode-de-dictionnaire-clear)
- [Conclusion](#heading-conclusion)


## Comment créer un dictionnaire en Python
Pour créer un dictionnaire, vous ouvrez une accolade et placez les données en paires clé-valeur séparées par des virgules.

La syntaxe de base d'un dictionnaire ressemble à ceci :
```py
demo_dict = {
"key1": "value1",
"key2": "value2", 
"key3": "value3"
}
```

Notez que les valeurs peuvent être de n'importe quel type de données et peuvent être dupliquées, mais la clé ne doit pas être dupliquée. Si les clés sont dupliquées, vous obtiendrez une erreur de syntaxe invalide.
 

## Méthodes pour travailler avec les dictionnaires Python
Je vais travailler avec le dictionnaire ci-dessous pour vous montrer comment fonctionnent les méthodes de dictionnaire :
```py
first_dict = {
    "name": "freeCodeCamp", 
    "founder": "Quincy Larson",
    "type": "charity", 
    "age": 8, 
    "price": "free", 
    "work-style": "remote",
}
```
### Comment utiliser la méthode de dictionnaire `get()`
La méthode get retourne la valeur d'une clé spécifiée. 

Dans le code ci-dessous, j'ai pu obtenir le fondateur de freeCodeCamp en passant la clé `founder` à l'intérieur de la méthode `get()` :
```py
first_dict = {
    "name": "freeCodeCamp", 
    "founder": "Quincy Larson",
    "type": "charity", 
    "age": 8, 
    "price": "free", 
    "work-style": "remote",
}

founder = first_dict.get("founder")
print(founder)

# Output: Quincy Larson
```

### Comment utiliser la méthode de dictionnaire `items()`

La méthode `items()` retourne toutes les entrées du dictionnaire dans une liste. Dans la liste se trouve un tuple représentant chacun des éléments.
```py
first_dict = {
    "name": "freeCodeCamp", 
    "founder": "Quincy Larson",
    "type": "charity", 
    "age": 8, 
    "price": "free", 
    "work-style": "remote",
}

items = first_dict.items()
print(items)

# Output: dict_items([('name', 'freeCodeCamp'), ('founder', 'Quincy Larson'), ('type', 'charity'), ('age', 8), ('price', 'free'), ('work-style', 'remote')])
```

### Comment utiliser la méthode de dictionnaire `keys()`

La méthode `keys()` retourne toutes les clés du dictionnaire. Elle retourne les clés dans un tuple – une autre structure de données Python.
```py
first_dict = {
    "name": "freeCodeCamp", 
    "founder": "Quincy Larson",
    "type": "charity", 
    "age": 8, 
    "price": "free", 
    "work-style": "remote",
}

dict_keys = first_dict.keys()
print(dict_keys)

# Output: dict_keys(['name', 'founder', 'type', 'age', 'price', 'work-style'])
```

### Comment utiliser la méthode de dictionnaire `values()`

La méthode values accède à toutes les valeurs d'un dictionnaire. Comme la méthode `keys()`, elle retourne les valeurs dans un tuple.

```py
first_dict = {
    "name": "freeCodeCamp", 
    "founder": "Quincy Larson",
    "type": "charity", 
    "age": 8, 
    "price": "free", 
    "work-style": "remote",
}

dict_values = first_dict.values()
print(dict_values)

# Output: dict_values(['freeCodeCamp', 'Quincy Larson', 'charity', 8, 'free', 'remote'])
```

### Comment utiliser la méthode de dictionnaire `pop()`

La méthode `pop()` supprime une paire clé-valeur du dictionnaire. Pour la faire fonctionner, vous devez spécifier la clé à l'intérieur de ses parenthèses. 
```py
first_dict = {
    "name": "freeCodeCamp", 
    "founder": "Quincy Larson",
    "type": "charity", 
    "age": 8, 
    "price": "free", 
    "work-style": "remote",
}

first_dict.pop("work-style")
print(first_dict)

# Output: {'name': 'freeCodeCamp', 'founder': 'Quincy Larson', 'type': 'charity', 'age': 8, 'price': 'free'}
```
Vous pouvez voir que la clé `work-style` et sa valeur ont été supprimées du dictionnaire.

### Comment utiliser la méthode de dictionnaire `popitem()`

La méthode `popitem()` fonctionne comme la méthode `pop()`. La différence est qu'elle supprime le dernier élément du dictionnaire.

```py
first_dict = {
    "name": "freeCodeCamp", 
    "founder": "Quincy Larson",
    "type": "charity", 
    "age": 8, 
    "price": "free", 
    "work-style": "remote",
}

first_dict.popitem()
print(first_dict)

# Output: {'name': 'freeCodeCamp', 'founder': 'Quincy Larson', 'type': 'charity', 'age': 8, 'price': 'free'}
```

Vous pouvez voir que la dernière paire clé-valeur ("work-style": "remote") a été supprimée du dictionnaire.

### Comment utiliser la méthode de dictionnaire `update()`

La méthode `update()` ajoute un élément au dictionnaire. Vous devez spécifier à la fois la clé et la valeur à l'intérieur de ses accolades et les entourer d'accolades.

```py
first_dict = {
    "name": "freeCodeCamp", 
    "founder": "Quincy Larson",
    "type": "charity", 
    "age": 8, 
    "price": "free", 
    "work-style": "remote",
}

first_dict.update({"Editor": "Abbey Rennemeyer"})
print(first_dict)

# Output: {'name': 'freeCodeCamp', 'founder': 'Quincy Larson', 'type': 'charity', 'age': 8, 'price': 'free', 'work-style': 'remote', 'Editor': 'Abbey Rennemeyer'}
```
La nouvelle entrée a été ajoutée au dictionnaire.


### Comment utiliser la méthode de dictionnaire `copy()`

La méthode `copy()` fait ce que son nom implique – elle copie le dictionnaire dans la variable spécifiée.
```py
first_dict = {
    "name": "freeCodeCamp", 
    "founder": "Quincy Larson",
    "type": "charity", 
    "age": 8, 
    "price": "free", 
    "work-style": "remote",
}

second_dict = first_dict.copy()
print(second_dict)

# Output: {'name': 'freeCodeCamp', 'founder': 'Quincy Larson', 'type': 'charity', 'age': 8, 'price': 'free', 'work-style': 'remote'}
```

### Comment utiliser la méthode de dictionnaire `clear()`

La méthode clear supprime toutes les entrées du dictionnaire.
```py
first_dict = {
    "name": "freeCodeCamp", 
    "founder": "Quincy Larson",
    "type": "charity", 
    "age": 8, 
    "price": "free", 
    "work-style": "remote",
}

first_dict.clear()
print(first_dict)

# Output: {}
```

## Conclusion  

Dans cet article, vous avez appris comment créer un dictionnaire Python et comment travailler avec celui-ci en utilisant les méthodes intégrées fournies par Python.

Si vous trouvez l'article utile, n'hésitez pas à le partager avec vos amis et votre famille.

Continuez à coder :)