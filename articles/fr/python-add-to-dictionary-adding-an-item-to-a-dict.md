---
title: 'Python : Ajouter à un dictionnaire – Ajouter un élément à un dictionnaire'
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-03-15T00:33:07.000Z'
originalURL: https://freecodecamp.org/news/python-add-to-dictionary-adding-an-item-to-a-dict
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/dictionaary.jpg
tags:
- name: dictionary
  slug: dictionary
- name: Python
  slug: python
seo_title: 'Python : Ajouter à un dictionnaire – Ajouter un élément à un dictionnaire'
seo_desc: "Data structures help us organize and store collections of data. Python\
  \ has built-in data structures like Lists, Sets, Tuples and Dictionaries. \nEach\
  \ of these structures have their own syntax and methods for interacting with the\
  \ data stored. \nIn this ..."
---

Les structures de données nous aident à organiser et à stocker des collections de données. Python possède des structures de données intégrées telles que les listes (Lists), les ensembles (Sets), les tuples (Tuples) et les dictionnaires (Dictionaries). 

Chacune de ces structures possède sa propre syntaxe et ses propres méthodes pour interagir avec les données stockées. 

Dans cet article, nous allons parler des dictionnaires, de leurs caractéristiques et de la manière d'y ajouter des éléments. 

## Comment créer un dictionnaire en Python

Les dictionnaires sont composés de paires clé-valeur imbriquées dans des accolades. Voici un exemple de dictionnaire :

```python
devBio = {
  "name": "Ihechikara",
  "age": 120,
  "language": "JavaScript"
}
print(devBio)
# {'name': 'Ihechikara', 'age': 120, 'language': 'JavaScript'}
```

Dans le code ci-dessus, nous avons créé un dictionnaire appelé `devBio` avec des informations sur un développeur – l'âge du développeur est assez impressionnant.

Chaque clé du dictionnaire – `name`, `age` et `language` – possède une valeur correspondante. Une virgule sépare chaque paire clé-valeur d'une autre. L'omission de la virgule génère une erreur.

Avant de découvrir comment ajouter des éléments à nos dictionnaires, jetons un coup d'œil à certaines des caractéristiques d'un dictionnaire. Cela vous aidera à les distinguer facilement des autres structures de données en Python. 

## Caractéristiques d'un dictionnaire

Voici quelques-unes des caractéristiques d'un dictionnaire en Python :

### Les clés en double ne sont pas autorisées

Si nous créons un dictionnaire qui contient deux ou plusieurs clés identiques, la dernière clé remplacera les autres. Voici un exemple :

```python
devBio = {
  "name": "Ihechikara",
  "name": "Vincent",
  "name": "Chikara",
  "age": 120,
  "language": "JavaScript"
}
print(devBio)
# {'name': 'Chikara', 'age': 120, 'language': 'JavaScript'}
```

Nous avons créé trois clés avec un nom de clé identique `name`. Lorsque nous avons affiché notre dictionnaire dans la console, la dernière clé ayant la valeur "Chikara" a écrasé les autres.

Voyons la caractéristique suivante.

### Les éléments d'un dictionnaire sont modifiables

Après avoir assigné un élément à un dictionnaire, vous pouvez changer sa valeur pour quelque chose de différent. 

```python
devBio = {
  "name": "Ihechikara",
  "age": 120,
  "language": "JavaScript"
}

devBio["age"] = 1

print(devBio)

# {'name': 'Chikara', 'age': 120, 'language': 'JavaScript'}
```

Dans l'exemple ci-dessus, nous avons réassigné une nouvelle valeur à `age`. Cela remplacera la valeur initiale que nous avions assignée lors de la création du dictionnaire. 

Nous pouvons également utiliser la méthode `update()` pour modifier la valeur des éléments de notre dictionnaire. Nous pouvons obtenir le même résultat que dans l'exemple précédent en utilisant la méthode `update()` – c'est-à-dire : `devBio.update({"age": 1})`. 

### Les éléments d'un dictionnaire sont ordonnés

Le fait d'être ordonné signifie que les éléments d'un dictionnaire conservent l'ordre dans lequel ils ont été créés ou ajoutés. Cet ordre ne peut pas changer. 

Avant Python 3.7, les dictionnaires en Python n'étaient pas ordonnés.

Dans la section suivante, nous verrons comment ajouter des éléments à un dictionnaire.

## Comment ajouter un élément à un dictionnaire

La syntaxe pour ajouter des éléments à un dictionnaire est la même que celle que nous avons utilisée lors de la mise à jour d'un élément. La seule différence ici est que la clé d'index inclura le nom de la nouvelle clé à créer et sa valeur correspondante.

Voici à quoi ressemble la syntaxe : `devBio[**newKey**] = **newValue**`**.**

Nous pouvons également utiliser la méthode `update()` pour ajouter de nouveaux éléments à un dictionnaire. Voici à quoi cela ressemblerait : `devBio.**update**({"**newKey**": **newValue**})`. 

Voyons quelques exemples.

```python
devBio = {
  "name": "Ihechikara",
  "age": 120,
  "language": "JavaScript"
}

devBio["role"] = "Developer"

print(devBio)

# {'name': 'Ihechikara', 'age': 120, 'language': 'JavaScript', 'role': 'Developer'}
```

Ci-dessus, en utilisant la clé d'index `devBio["role"]`, nous avons créé une nouvelle clé avec la valeur `Developer`.

Dans l'exemple suivant, nous utiliserons la méthode `update()`. 

```python
devBio = {
  "name": "Ihechikara",
  "age": 120,
  "language": "JavaScript"
}

devBio.update({"role": "Developer"})

print(devBio)

# {'name': 'Ihechikara', 'age': 120, 'language': 'JavaScript', 'role': 'Developer'}
```

Ci-dessus, nous avons obtenu le même résultat que dans l'exemple précédent en passant la nouvelle clé et sa valeur dans la méthode `update()` – c'est-à-dire : `devBio.update({"role": "Developer"})`.

## Conclusion

Dans cet article, nous avons appris ce que sont les dictionnaires en Python, comment les créer et certaines de leurs caractéristiques. Nous avons ensuite vu deux façons d'ajouter des éléments à nos dictionnaires. 

Bon codage !