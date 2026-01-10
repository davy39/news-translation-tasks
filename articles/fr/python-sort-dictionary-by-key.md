---
title: Python Trier un Dictionnaire par Clé – Comment Trier un Dict avec des Clés
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-05-25T23:57:54.000Z'
originalURL: https://freecodecamp.org/news/python-sort-dictionary-by-key
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/Shittu-Olumide-Python-Sort-Dictionary-by-Key
seo_title: Python Trier un Dictionnaire par Clé – Comment Trier un Dict avec des Clés
---

How-to-Sort-a-Dict-with-Keys.png
tags:
- name: dictionnaire
  slug: dictionnaire
- name: Python
  slug: python
seo_title: null
seo_desc: 'Par Shittu Olumide

  Le tri est une opération fondamentale en programmation informatique qui consiste à organiser
  des éléments dans un ordre spécifique.

  Que vous travailliez avec des nombres, des chaînes de caractères ou des structures de données complexes, le tri
  joue un rôle crucial dans l'organisation et la manipulation efficace des données.

  Des petits tableaux aux grands ensembles de données, les algorithmes de tri permettent aux programmeurs de résoudre une large gamme de problèmes, allant de la recherche de valeurs spécifiques à l'optimisation de l'accès et de l'analyse des données.

Dans cet article, nous allons explorer comment trier un dictionnaire par ses clés en Python. Nous allons décomposer les étapes pour un suivi et une compréhension faciles. Je recommande d'être familier avec le langage de programmation Python pour tirer le meilleur parti de cet article.

## Qu'est-ce qu'un Dictionnaire Python ?

En Python, les dictionnaires sont une structure de données puissante utilisée pour stocker des paires clé-valeur. Ils fournissent un moyen pratique d'organiser et de récupérer des données basées sur des clés uniques. Mais il peut y avoir des situations où vous devez trier un dictionnaire par ses clés dans un ordre spécifique.

Une clé en Python fait référence à l'identifiant unique associé à une valeur spécifique. Elle sert de moyen pour accéder et récupérer des valeurs du dictionnaire en fonction de leurs clés correspondantes. Les clés dans un dictionnaire peuvent être de n'importe quel type de données immutable, tels que des chaînes de caractères, des nombres (entiers ou flottants), ou des tuples. La clé doit être unique dans le dictionnaire, ce qui signifie que deux clés ne peuvent pas avoir la même valeur.

## Façons de Trier un Dict par Clés en Python

### Méthode 1 : Utilisation de la fonction `sorted()`

La manière la plus simple de trier un dictionnaire par ses clés est d'utiliser la fonction `sorted()` avec la méthode `items()` du dictionnaire.

La méthode `items()` retourne une liste de paires clé-valeur sous forme de tuples. En passant cette liste à la fonction `sorted()`, nous pouvons trier les tuples en fonction de leur premier élément (les clés).

Exemple :

```py
my_dict = {'b': 2, 'a': 1, 'c': 3}
sorted_dict = dict(sorted(my_dict.items()))

print(sorted_dict)

```

Sortie :

```bash
{'a': 1, 'b': 2, 'c': 3}

```

Dans cet exemple, la fonction `sorted()` prend la liste `my_dict.items()` et retourne une nouvelle liste triée de tuples. Nous utilisons le constructeur `dict()` pour convertir la liste triée en un dictionnaire.

### Méthode 2 : Utilisation d'une Liste de Tuples

Si vous préférez une approche plus manuelle, vous pouvez convertir le dictionnaire en une liste de tuples, trier la liste en utilisant n'importe quelle technique de tri disponible en Python, puis la convertir en dictionnaire.

Exemple :

```py
my_dict = {'b': 2, 'a': 1, 'c': 3}
sorted_list = sorted(my_dict.items())

sorted_dict = {}
for key, value in sorted_list:
    sorted_dict[key] = value

print(sorted_dict)

```

Sortie :

```bash
{'a': 1, 'b': 2, 'c': 3}

```

Dans cet exemple, nous avons utilisé la fonction `sorted()` pour trier la liste `my_dict.items()`. Ensuite, un nouveau dictionnaire vide, `sorted_dict`, est créé. La liste triée est parcourue, et chaque paire clé-valeur est ajoutée à `sorted_dict` par affectation.

### Méthode 3 : Utilisation de la classe `collections.OrderedDict`

Une autre approche pour trier un dictionnaire par clé consiste à utiliser la classe `collections.OrderedDict` de la bibliothèque standard de Python.

Cette classe est une sous-classe de dict qui conserve l'ordre de ses éléments en fonction de l'ordre d'insertion. Nous pouvons utiliser cette fonctionnalité pour obtenir un tri basé sur les clés.

Exemple :

```py
from collections import OrderedDict

my_dict = {'b': 2, 'a': 1, 'c': 3}
sorted_dict = OrderedDict(sorted(my_dict.items()))

print(sorted_dict)

```

Sortie :

```bash
OrderedDict([('a', 1), ('b', 2), ('c', 3)])

```

Dans cet exemple, la fonction `sorted()` est utilisée pour trier la liste `my_dict.items()`, puis la liste triée est passée au constructeur `OrderedDict()` pour créer un nouveau dictionnaire avec l'ordre trié.

## Conclusion

En Python, vous pouvez trier un dictionnaire par ses clés en utilisant diverses méthodes. Dans cet article, nous avons exploré trois approches : l'utilisation de la fonction `sorted()`, l'utilisation de la classe `collections.OrderedDict`, et le tri manuel d'une liste de tuples. Chaque méthode offre un niveau différent de contrôle et de flexibilité.

En utilisant la fonction `sorted()`, nous pouvons rapidement trier un dictionnaire par clé et obtenir un nouveau dictionnaire comme résultat. Si la préservation de l'ordre d'insertion est cruciale, la classe `collections.OrderedDict` est un choix approprié.

Pour ceux qui préfèrent une approche plus manuelle, la conversion du dictionnaire en une liste de tuples, le tri de la liste, puis la création d'un nouveau dictionnaire peuvent offrir plus d'options de personnalisation.

Connectons-nous sur [Twitter](https://www.twitter.com/Shittu_Olumide_) et sur [LinkedIn](https://www.linkedin.com/in/olumide-shittu). Vous pouvez également vous abonner à ma chaîne [YouTube](https://www.youtube.com/channel/UCNhFxpk6hGt5uMCKXq0Jl8A).

Bon Codage !