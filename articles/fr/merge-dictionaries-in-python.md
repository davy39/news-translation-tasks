---
title: Comment fusionner des dictionnaires en Python
subtitle: ''
author: Ashutosh Krishna
co_authors: []
series: null
date: '2021-12-09T17:16:36.000Z'
originalURL: https://freecodecamp.org/news/merge-dictionaries-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/Black-Moon-Blog-Banner--1--1.png
tags:
- name: dictionary
  slug: dictionary
- name: Python
  slug: python
seo_title: Comment fusionner des dictionnaires en Python
seo_desc: "In Python, a dictionary is a collection you use to store data in {key:value}\
  \ pairs. It is ordered and mutable, and it cannot store duplicate data. \nWe write\
  \ a dictionary using curly brackets like this:\nmy_dict = {\n    \"id\": 1,\n  \
  \  \"name\": \"Ashutosh\",..."
---

En Python, un dictionnaire est une collection que vous utilisez pour stocker des données sous forme de paires `{clé:valeur}`. Il est ordonné et mutable, et il ne peut pas stocker de données en double. 

Nous écrivons un dictionnaire en utilisant des accolades comme ceci :

```python
my_dict = {
    "id": 1,
    "name": "Ashutosh",
    "books": ["Python", "DSA"]
}

```

Parfois, nous devons fusionner deux dictionnaires ou plus pour créer un dictionnaire plus grand. Par exemple :

```python
dict_one = {
    "id": 1,
    "name": "Ashutosh",
    "books": ["Python", "DSA"]
}

dict_two = {
    "college": "NSEC",
    "city": "Kolkata",
    "country": "India"
}

merged_dict = {
    "id": 1,
    "name": "Ashutosh",
    "books": ["Python", "DSA"],
    "college": "NSEC",
    "city": "Kolkata",
    "country": "India"
}

```

Dans `merged_dict`, nous avons les paires clé-valeur de `dict_one` et `dict_two`. C'est ce que nous souhaitons réaliser de manière programmatique. 

Il existe plusieurs façons de procéder en Python :

1. En utilisant une boucle for
2. En utilisant la méthode `dict.update()`
3. En utilisant l'opérateur `**`
4. En utilisant l'opérateur `|` (Union) (pour Python 3.9 et versions ultérieures)

Explorons chaque méthode une par une.

## Comment fusionner des dictionnaires en Python en utilisant une boucle For

Nous pouvons fusionner deux dictionnaires ou plus en utilisant une boucle for comme ceci :

```bash
>>> dict_one = {
...     "id": 1,
...     "name": "Ashutosh",
... }
>>> dict_two = {
...     "books": ["Python", "DSA"],
...     "college": "NSEC",
... }
>>> dict_three = {
...     "city": "Kolkata",
...     "country": "India"
... }
>>> for key,value in dict_two.items():
...     merged_dict[key] = value
... 
>>> merged_dict
{'id': 1, 'name': 'Ashutosh', 'books': ['Python', 'DSA'], 'college': 'NSEC'}
>>> for key,value in dict_three.items():
...     merged_dict[key] = value
... 
>>> merged_dict
{'id': 1, 'name': 'Ashutosh', 'books': ['Python', 'DSA'], 'college': 'NSEC', 'city': 'Kolkata', 'country': 'India'}
```

Mais le problème avec cette méthode est que nous devons exécuter autant de boucles pour fusionner les dictionnaires. 

Alors, quelle est l'autre option ?

## Comment fusionner des dictionnaires en Python en utilisant la méthode `dict.update()`

Si vous explorez la classe `dict`, il y a diverses méthodes à l'intérieur. L'une de ces méthodes est la méthode `update()` que vous pouvez utiliser pour fusionner un dictionnaire dans un autre.

```bash
>>> dict_one = {
...     "id": 1,
...     "name": "Ashutosh",
...     "books": ["Python", "DSA"]
... }
>>> dict_two = {
...     "college": "NSEC",
...     "city": "Kolkata",
...     "country": "India"
... }
>>> dict_one.update(dict_two)
>>> dict_one
{'id': 1, 'name': 'Ashutosh', 'books': ['Python', 'DSA'], 'college': 'NSEC', 'city': 'Kolkata', 'country': 'India'}
```

Mais le problème lorsque nous utilisons la méthode `update()` est qu'elle modifie l'un des dictionnaires. Si nous souhaitons créer un troisième dictionnaire sans modifier aucun des autres dictionnaires, nous ne pouvons pas utiliser cette méthode. 

De plus, vous ne pouvez utiliser cette méthode que pour fusionner deux dictionnaires à la fois. Si vous souhaitez fusionner trois dictionnaires, vous devez d'abord fusionner les deux premiers, puis fusionner le troisième avec le dictionnaire modifié.

```bash
>>> dict_one = {
...     "id": 1,
...     "name": "Ashutosh",
... }
>>> dict_two = {
...     "books": ["Python", "DSA"],
...     "college": "NSEC",
... }
>>> dict_three = {
...     "city": "Kolkata",
...     "country": "India"
... }
>>> dict_one.update(dict_two)
>>> dict_one
{'id': 1, 'name': 'Ashutosh', 'books': ['Python', 'DSA'], 'college': 'NSEC'}
>>> dict_one.update(dict_three)
>>> dict_one
{'id': 1, 'name': 'Ashutosh', 'books': ['Python', 'DSA'], 'college': 'NSEC', 'city': 'Kolkata', 'country': 'India'}
```

Explorons d'autres options.

## Comment fusionner des dictionnaires en Python en utilisant l'opérateur `**`

Vous pouvez utiliser la méthode double astérisque (**) pour déballer ou développer un dictionnaire comme ceci : 

```bash
>>> dict_one = {
...     "id": 1,
...     "name": "Ashutosh",
... }
>>> dict_two = {
...     "books": ["Python", "DSA"]
...     "college": "NSEC",
... }
>>> dict_three = {
...     "city": "Kolkata",
...     "country": "India"
... }
>>> merged_dict = {**dict_one, **dict_two, **dict_three} 
>>> merged_dict
{'id': 1, 'name': 'Ashutosh', 'books': ['Python', 'DSA'], 'college': 'NSEC', 'city': 'Kolkata', 'country': 'India'}
```

L'utilisation de l'opérateur `**` pour fusionner les dictionnaires n'affecte aucun des dictionnaires.

## Comment fusionner des dictionnaires en Python en utilisant l'opérateur `|`

À partir de Python 3.9, nous pouvons utiliser l'opérateur Union ( `|` ) pour fusionner deux dictionnaires ou plus. 

```bash
>>> dict_one = {
...     "id": 1,
...     "name": "Ashutosh",
... }
>>> dict_two = {
...     "books": ["Python", "DSA"],
...     "college": "NSEC",
... }
>>> dict_three = {
...     "city": "Kolkata",
...     "country": "India"
... }
>>> merged_dict = dict_one | dict_two | dict_three
>>> merged_dict
{'id': 1, 'name': 'Ashutosh', 'books': ['Python', 'DSA'], 'college': 'NSEC', 'city': 'Kolkata', 'country': 'India'}
```

C'est la méthode la plus pratique disponible pour fusionner des dictionnaires en Python.

## Conclusion

Nous avons exploré plusieurs méthodes différentes pour fusionner des dictionnaires. Si vous avez Python 3.9 ou une version ultérieure, vous devriez utiliser l'opérateur `|`. Mais si vous utilisez des versions plus anciennes de Python, vous pouvez toujours utiliser les autres méthodes discutées ci-dessus.