---
title: Compréhension de dictionnaire en Python – Dict Comprehensions Explained
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-09-16T18:47:35.000Z'
originalURL: https://freecodecamp.org/news/dictionary-comprehension-in-python-dict-comprehensions-explained
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/element5-digital-OyCl7Y4y0Bk-unsplash.jpg
tags:
- name: dictionary
  slug: dictionary
- name: Python
  slug: python
seo_title: Compréhension de dictionnaire en Python – Dict Comprehensions Explained
seo_desc: "You can use Dictionaries in Python to store data in key and value pairs.\
  \ \nAnd you can use dictionary comprehension to create a new dictionary from an\
  \ already existing one. \nWhen creating a new dictionary using dictionary comprehension,\
  \ you can perfor..."
---

Vous pouvez utiliser les [Dictionnaires](https://www.freecodecamp.org/news/python-add-to-dictionary-adding-an-item-to-a-dict/) en Python pour stocker des données en paires clé-valeur. 

Et vous pouvez utiliser la compréhension de dictionnaire pour créer un nouveau dictionnaire à partir d'un dictionnaire existant. 

Lors de la création d'un nouveau dictionnaire en utilisant la compréhension de dictionnaire, vous pouvez effectuer diverses opérations en utilisant des expressions pour déterminer les données (clé et/ou valeur) qui seront stockées dans le nouveau dictionnaire. 

Dans cet article, vous apprendrez comment créer des dictionnaires en Python en utilisant la compréhension de dictionnaire. Vous verrez également diverses expressions que vous pouvez utiliser pour modifier les données à stocker dans le nouveau dictionnaire. 

Commençons !

## Comment utiliser la compréhension de dictionnaire en Python

Avant de regarder quelques exemples, voici à quoi ressemble la syntaxe de la compréhension de dictionnaire :

```txt
new_dictionary = {key: value for (key,value) in iterable}
```

Dans la syntaxe ci-dessus, `key` et `value` représentent la clé et la valeur dans le dictionnaire initial. Toute opération que vous effectuez sur eux détermine les clés/valeurs dans le nouveau dictionnaire — vous comprendrez mieux cela bientôt avec quelques exemples. 

Le `key` et `value` entre parenthèses — `(key, value)` — sont toujours les mêmes que ceux que nous avons mentionnés ci-dessus. Dans ce cas, ils sont utilisés dans une boucle `for`. 

Ainsi, toute opération que vous effectuez sur `key` et `value` sera utilisée par la boucle pour appliquer cette opération sur chaque élément associé à l'opération dans le dictionnaire initial.

`iterable`, dans la syntaxe, désigne un objet itérable. Dans notre cas, il désigne le dictionnaire initial.

Regardons quelques exemples pour vous aider à comprendre les explications ci-dessus.

```python
items_in_cm = {'pen': 40, 'book': 50, 'keyboard': 60}
```

Dans le code ci-dessus, nous avons créé un dictionnaire avec trois éléments. Les clés sont les noms des éléments tandis que les valeurs sont la longueur de ces éléments en centimètres. 

En utilisant une compréhension de dictionnaire, nous allons créer un nouveau dictionnaire avec la longueur de chaque élément en mètres. 

Voici comment cela fonctionne :

```python
items_in_cm = {'pen': 40, 'book': 50, 'keyboard': 60}

items_in_meters = {key: value/100 for (key, value) in items_in_cm.items()}

print(items_in_meters)
# {'pen': 0.4, 'book': 0.5, 'keyboard': 0.6}
```

Ce qu'il faut observer est dans la deuxième ligne ci-dessus : `items_in_meters = {key: value/100 for (key, value) in items_in_cm.items()}`

Décomposons cela.

La première partie contient ceci : `key: value/100`. Cela implique que chaque `value` dans le dictionnaire doit être divisée par 100. 

Mais la compréhension de dictionnaire ne comprend pas encore où appliquer la commande ci-dessus. 

Cela nous amène à la deuxième partie : `for (key, value) in items_in_cm.items()`. Cette partie du code contient une boucle `for` qui prend deux paramètres — `key` et `value`. 

Ainsi, cela parcourra chaque clé et valeur dans le dictionnaire `items_in_cm` et divisera chaque valeur par 100. 

Nous sommes en mesure d'accéder aux éléments de ce dictionnaire en utilisant la méthode `items()` qui retourne chaque paire clé-valeur dans un dictionnaire. 

En imprimant le nouveau dictionnaire (`items_in_meters`), nous obtenons ceci : `{'pen': 0.4, 'book': 0.5, 'keyboard': 0.6}`. Chaque valeur dans le nouveau dictionnaire a été divisée par 100. 

Vous remarquerez que nous n'avons modifié que les données dans les valeurs du dictionnaire. Vous pouvez également modifier les clés. Voici un exemple : 

```python
items_in_cm = {'pen': 40, 'book': 50, 'keyboard': 60}

items_in_meters = {key + ' in meters': value/100 for (key, value) in items_in_cm.items()}

print(items_in_meters)
# {'pen in meters': 0.4, 'book in meters': 0.5, 'keyboard in meters': 0.6}

```

Dans l'exemple ci-dessus, nous avons ajouté une chaîne à chaque clé dans la compréhension de dictionnaire : `key + ' in meters'`. 

## Comment utiliser les instructions conditionnelles dans la compréhension de dictionnaire en Python

Dans cette section et la suivante, vous apprendrez d'autres expressions que vous pouvez utiliser pour modifier les éléments stockés dans les dictionnaires créés en utilisant la compréhension de dictionnaire. 

Nous commencerons par les instructions conditionnelles.

```python
developers = {'Jane': 'Python', 'Jade': 'JavaScript', 'John': 'Python', 'Doe': 'JavaScript'}

python_developers = {key: value for (key, value) in developers.items() if value == 'Python'}

print(python_developers)
# {'Jane': 'Python', 'John': 'Python'}

```

Dans l'exemple ci-dessus, nous avons créé un dictionnaire appelé `developers` qui stocke une liste de développeurs avec leurs langages préférés : `{'Jane': 'Python', 'Jade': 'JavaScript', 'John': 'Python', 'Doe': 'JavaScript'}`.

Dans la compréhension de dictionnaire, nous avons ajouté une expression à la fin : `if value == 'Python'`. Cela parcourra et retournera tous les éléments dont la `value` a une valeur de 'Python'. 

Lors de l'impression, nous obtenons ceci dans la console : `{'Jane': 'Python', 'John': 'Python'}`. 

Nous pouvons également utiliser une instruction `if/else` dans les compréhensions de dictionnaire. Voici un exemple :

```python
random_items = {'monitor': 100, 'pen': 40, 'keyboard': 60, 'pencil': 30}

items_length_check = {key: ('above 50' if value > 50 else 'below 50') for (key, value) in random_items.items()}

print(items_length_check)
# {'monitor': 'above 50', 'pen': 'below 50', 'keyboard': 'above 50', 'pencil': 'below 50'}
```

En utilisant une instruction `if/else` ci-dessus, nous avons modifié les valeurs dans le nouveau dictionnaire. La `value` pour chaque élément sera "above 50" si la valeur dans le dictionnaire initial est supérieure à 50 et "below 50" si elle est inférieure à 50.

Le code dans la compréhension de dictionnaire commence à paraître encombrant. Nous allons le nettoyer dans la section suivante en utilisant une fonction. 

## Comment utiliser une fonction dans la compréhension de dictionnaire en Python

Lors de l'utilisation de la compréhension de dictionnaire, vous pouvez utiliser des fonctions pour remplacer/extraire la logique qui doit aller dans les accolades de la compréhension de dictionnaire. Cela aide à garder le code propre et lisible. 

```python
random_items = {'monitor': 100, 'pen': 40, 'keyboard': 60, 'pencil': 30}

def check_length(value):
    if value >50:
        return 'above 50'
    else:
        return 'below 50'

items_length_check = {key: check_length(value) for (key, value) in random_items.items()}


print(items_length_check)
# {'monitor': 'above 50', 'pen': 'below 50', 'keyboard': 'above 50', 'pencil': 'below 50'}

```

L'exemple ci-dessus est similaire à celui de la dernière section. 

Nous avons apporté un changement majeur — extraire la logique dans la compréhension de dictionnaire et la mettre dans une fonction. C'est-à-dire :

```python
def check_length(value):
    if value >50:
        return 'above 50'
    else:
        return 'below 50'
```

Nous avons ensuite mis le nom de la fonction dans la compréhension de dictionnaire : `items_length_check = {key: check_length(value) for (key, value) in random_items.items()}`.

Lorsque le code dans la compréhension de dictionnaire s'exécute, la fonction est déclenchée. 

## Résumé

Dans cet article, nous avons parlé de la compréhension de dictionnaire en Python. Vous pouvez l'utiliser pour créer de nouveaux dictionnaires à partir de dictionnaires existants.

Nous avons vu la syntaxe et comment utiliser la compréhension de dictionnaire.

Nous avons également vu des exemples qui ont montré comment utiliser des instructions conditionnelles et des fonctions lors de l'utilisation de la compréhension de dictionnaire. 

Bon codage !