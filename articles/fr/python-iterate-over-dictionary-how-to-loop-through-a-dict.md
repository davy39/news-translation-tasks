---
title: Python Itérer sur un Dictionnaire – Comment Parcourir un Dict
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-03-10T21:10:23.000Z'
originalURL: https://freecodecamp.org/news/python-iterate-over-dictionary-how-to-loop-through-a-dict
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/Shittu-Olumide-Python-Iterate-Over-Dictionary
seo_title: Python Itérer sur un Dictionnaire – Comment Parcourir un Dict
---

How-to-Loop-Through-a-Dict-2.png
tags:
- name: dictionary
  slug: dictionnaire
- name: Python
  slug: python
seo_title: null
seo_desc: 'Par Shittu Olumide

Dans cet article, nous allons parler des dictionnaires et apprendre comment parcourir un dictionnaire en Python.

## Dictionnaires Python

En Python, un dictionnaire est une structure de données intégrée utilisée pour stocker et organiser des données en paires clé-valeur.

Un dictionnaire a deux parties pour chaque entrée : une clé et une valeur. La valeur associée peut être accessible en utilisant la clé, un identifiant spécial. N'importe quel type de données, y compris un nombre, une chaîne, une liste ou un autre dictionnaire, peut être utilisé comme valeur.

Les dictionnaires peuvent être créés en attribuant explicitement des valeurs aux clés ou en utilisant la fonction constructeur `dict()`. Ils sont indiqués par des accolades `{ }`. Voici un exemple de dictionnaire de base :

```py
DemoDict = {'name': 'John', 'age': 25, 'city': 'New Jersey'}

```

Dans cet exemple, les clés sont `'name'`, `'age'` et `'city'`, et les valeurs correspondantes sont `'John'`, `25` et `'New Jersey'`, respectivement.

Nous allons maintenant examiner les différentes méthodes pour parcourir un dictionnaire : la méthode `items()`, la méthode `keys()`, la méthode `values()` et l'utilisation de la compréhension de liste.

## Comment Itérer à Travers un Dict en Utilisant la Méthode `items()`

Nous pouvons utiliser la méthode `items()` pour parcourir un dictionnaire et obtenir à la fois les paires clé-valeur.

Considérons un exemple :

```py
DemoDict = {'apple': 1, 'banana': 2, 'orange': 3}

# Parcourir le dictionnaire
for key, value in my_dict.items():
    print(key, value)

```

Sortie :

```bash
apple 1
banana 2
orange 3

```

## Comment Itérer à Travers un Dict en Utilisant la Méthode `keys()`

Si nous voulons uniquement parcourir les clés du dictionnaire, nous pouvons utiliser la méthode `keys()`.

```py
DemoDict = {'apple': 1, 'banana': 2, 'orange': 3}

# Parcourir les clés du dictionnaire
for key in my_dict.keys():
    print(key)

```

Sortie :

```bash
apple
banana
orange

```

## Comment Itérer à Travers un Dict en Utilisant la Méthode `values()`

De même, si nous voulons uniquement parcourir les valeurs du dictionnaire, nous pouvons utiliser la méthode `values()`.

```py
my_dict = {'apple': 1, 'banana': 2, 'orange': 3}

# Parcourir les valeurs du dictionnaire
for value in my_dict.values():
    print(value)

```

Sortie :

```bash
1
2
3

```

## Comment Itérer à Travers un Dict en Utilisant la Compréhension de Liste

Enfin, nous pouvons également utiliser la compréhension de liste pour parcourir un dictionnaire et obtenir à la fois les paires clé-valeur.

Démontrons cela avec un exemple :

```py
my_dict = {'apple': 2, 'banana': 3, 'orange': 4}

# Parcourir le dictionnaire en utilisant la compréhension de liste
[(key, value) for key, value in my_dict.items()]

```

Sortie :

```bash
[('apple', 1), ('banana', 2), ('orange', 3)]

```

**Note** : La sortie de la compréhension de liste est une liste de tuples où chaque tuple contient une paire clé-valeur du dictionnaire.

## Différences Clés Entre les Méthodes de Parcours d'un Dictionnaire en Python

### Compatibilité avec différentes versions de Python :

* Les méthodes `items()` et `values()` ont été introduites dans Python 3, donc elles ne sont pas compatibles avec Python 2. Si vous devez écrire du code compatible avec Python 2 et 3, vous devriez utiliser une boucle for de base pour itérer à travers les clés du dictionnaire.
* La méthode `keys()` est compatible avec Python 2 et 3, donc c'est une bonne option si vous devez écrire du code qui fonctionne sur les deux versions de Python.

### Performance :

* En général, l'utilisation d'une boucle for de base pour itérer à travers les clés d'un dictionnaire est la méthode la plus rapide pour parcourir un dictionnaire en Python. Cela évite le surcoût de création d'une liste des clés ou des éléments du dictionnaire.
* La méthode `items()` est plus lente qu'une boucle for de base car elle crée une nouvelle liste de tuples contenant les paires clé-valeur du dictionnaire.
* La méthode `values()` est également plus lente qu'une boucle for de base car elle crée une nouvelle liste des valeurs du dictionnaire.

### Accès aux clés, valeurs ou aux deux :

* Lorsque vous utilisez une boucle for de base pour itérer à travers un dictionnaire, vous n'avez accès qu'aux clés du dictionnaire. Pour accéder aux valeurs correspondantes, vous devez utiliser les clés comme index du dictionnaire.
* La méthode `items()` fournit un moyen d'accéder à la fois aux clés et aux valeurs du dictionnaire dans une seule boucle. Cela est pratique lorsque vous devez travailler avec les clés et les valeurs d'un dictionnaire.
* La méthode `values()`, en revanche, vous permet d'accéder uniquement aux valeurs du dictionnaire. Cela peut être utile lorsque vous n'avez pas besoin des clés mais souhaitez simplement travailler avec les valeurs elles-mêmes.

## Conclusion

Les dictionnaires sont incroyablement utiles pour stocker et récupérer des données de manière flexible et efficace. Ils sont couramment utilisés en programmation Python pour des tâches telles que l'analyse de données, le développement web et l'apprentissage automatique.

Connectons-nous sur [Twitter](https://www.twitter.com/Shittu_Olumide_) et sur [LinkedIn](https://www.linkedin.com/in/olumide-shittu). Vous pouvez également vous abonner à ma chaîne [YouTube](https://www.youtube.com/channel/UCNhFxpk6hGt5uMCKXq0Jl8A).

Bon Codage !