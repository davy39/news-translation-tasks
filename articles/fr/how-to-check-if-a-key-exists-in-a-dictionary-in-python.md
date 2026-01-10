---
title: Comment vérifier si une clé existe dans un dictionnaire en Python – Python
  Dict Has Key
subtitle: ''
author: Hillary Nyakundi
co_authors: []
series: null
date: '2023-06-27T16:59:26.000Z'
originalURL: https://freecodecamp.org/news/how-to-check-if-a-key-exists-in-a-dictionary-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/CoverImage-1.png
tags:
- name: dictionary
  slug: dictionary
- name: Python
  slug: python
seo_title: Comment vérifier si une clé existe dans un dictionnaire en Python – Python
  Dict Has Key
seo_desc: "Python is one of the most popular programming languages today. Its usage\
  \ cuts across multiple fields, but the most common ones are data science, machine\
  \ learning, and web development. \nWhen you're coding in Python, you'll use different\
  \ data structure..."
---

Python est l'un des langages de programmation les plus populaires aujourd'hui. Son utilisation s'étend à de multiples domaines, mais les plus courants sont la science des données, l'apprentissage automatique et le développement web. 

Lorsque vous codez en Python, vous utiliserez différentes structures de données. En Python, parmi les plus utilisées se trouve le dictionnaire. 

Un dictionnaire est une collection de paires clé-valeur qui vous permet de stocker et de récupérer des données. 

Lorsque vous travaillez avec des dictionnaires, il est courant de vérifier si une clé existe ou non. Cela peut être très utile lorsque vous travaillez avec un grand ensemble de données et que vous devez accéder aux valeurs en fonction de leurs clés. 

Dans cet article, nous allons explorer différentes façons de vérifier si une clé existe dans un dictionnaire en Python. Commençons.

## Méthode 1 : Utilisation de l'opérateur `in`
Vous pouvez utiliser l'opérateur `in` pour vérifier si une clé existe dans un dictionnaire. C'est l'une des façons les plus simples d'accomplir cette tâche. Lorsqu'il est utilisé, il retourne `True` si la clé est présente et `False` dans le cas contraire. 

Vous pouvez voir un exemple de son utilisation ci-dessous :

```python
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

if 'key1' in my_dict:
    print("La clé existe dans le dictionnaire.")
else:
    print("La clé n'existe pas dans le dictionnaire.")
```

Dans l'exemple de code ci-dessus, nous vérifions si `key1` existe dans `my_dict`. Si c'est le cas, le message de confirmation sera affiché. Sinon, le message indiquant que la clé n'existe pas sera imprimé. 

## Méthode 2 : Utilisation de la méthode `dict.get()`
La méthode `dict.get()` retournera la valeur associée à une clé donnée si elle existe et `None` si la clé demandée n'est pas trouvée. 

```python
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

if my_dict.get('key1') is not None:
    print("La clé existe dans le dictionnaire.")
else:
    print("La clé n'existe pas dans le dictionnaire.")
```

Dans l'exemple de code ci-dessus, nous avons utilisé la méthode `dict.get()` pour obtenir les valeurs associées à `key1`. Si la clé demandée est présente, `my_dict.get('key1') is not None` évalue à True, ce qui signifie que la clé demandée est présente.

## Méthode 3 : Utilisation de la gestion des exceptions
La gestion des exceptions vous permet d'abord d'essayer d'accéder à la valeur de la clé et de gérer l'exception `KeyError` si elle se produit. 

```python
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

try:
    value = my_dict['key1']
    print("La clé existe dans le dictionnaire.")
except KeyError:
    print("La clé n'existe pas dans le dictionnaire.")
```

L'exemple de code ci-dessus nous permet d'accéder à la valeur associée à `key1`. Si elle existe, le code à l'intérieur de `try` s'exécute et le message est imprimé. Mais si l'exception `KeyError` se produit, cela signifie que la clé n'existe pas et le code à l'intérieur du bloc `except` sera exécuté. 

### Points supplémentaires
* **Clé existe versus valeur existe**
Les méthodes que nous avons discutées ci-dessus ne vérifient que si une clé existe. Si nous devions vérifier si une valeur est présente, nous devrions parcourir les valeurs en utilisant des méthodes comme `dictname.values()`.

* **Considérations de performance**
Différentes méthodes peuvent avoir différentes implications de performance en fonction de la taille de votre dictionnaire. Généralement, l'opérateur `in` est le meilleur pour les dictionnaires de petite à moyenne taille, tandis que `dict.get()` et la gestion des exceptions sont adaptés aux grands dictionnaires.

* **Combinaison des méthodes**
Une bonne chose concernant le travail avec les méthodes de dictionnaire Python est que vous pouvez les combiner. Par exemple, vous pouvez utiliser l'opérateur `in` pour vérifier si une clé existe et `dict.get()` pour récupérer sa valeur si elle existe.

* **Utilisation de `dict.setdefault()`**
Cela vous permet de vérifier si une clé existe et retourne la valeur si elle est présente. Dans le cas où la clé est manquante, vous pouvez définir une valeur par défaut tout en l'ajoutant au dictionnaire en même temps.

Avec une compréhension des points ci-dessus et une bonne pratique de l'utilisation de ces méthodes, vous devriez être à l'aise pour travailler avec des dictionnaires en Python.