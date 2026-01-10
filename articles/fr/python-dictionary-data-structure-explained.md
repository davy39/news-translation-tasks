---
title: Structure de données de dictionnaire Python expliquée
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-04T22:12:00.000Z'
originalURL: https://freecodecamp.org/news/python-dictionary-data-structure-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e33740569d1a4ca3bdc.jpg
tags:
- name: data structures
  slug: data-structures
- name: Python
  slug: python
seo_title: Structure de données de dictionnaire Python expliquée
seo_desc: 'Dictionary is one of the most used data structures in Python. A dictionary
  is an unordered collection of items and we usually have keys and values stored in
  a dictionary. Let us look at a few examples for how the dictionary is usually used.

  # diction...'
---

Le dictionnaire est l'une des structures de données les plus utilisées en Python. Un dictionnaire est une collection non ordonnée d'éléments et nous avons généralement des clés et des valeurs stockées dans un dictionnaire. Examinons quelques exemples de la manière dont le dictionnaire est généralement utilisé.

```python
# déclaration de dictionnaire 1
dict1 = dict()

# déclaration de dictionnaire 2
dict2 = {}

# Ajouter des éléments au dictionnaire
# La syntaxe pour ajouter et récupérer des éléments est la même pour les deux objets que nous avons définis ci-dessus. 
key = "X"
value = "Y"
dict1[key] = value

# Le dictionnaire n'a pas de type de données spécifique. 
# Donc, les valeurs peuvent être assez diverses. 
dict1[key] = dict2
```

Examinons maintenant quelques méthodes de récupération.

```python
# Puisque "X" existe dans notre dictionnaire, cela récupérera la valeur
value = dict1[key]

# Cette clé n'existe pas dans le dictionnaire. 
# Donc, nous obtiendrons une `KeyError`
value = dict1["random"]
```

### **Éviter KeyError : Utiliser la fonction .get**

Dans le cas où la clé donnée n'existe pas dans le dictionnaire, Python lèvera une `KeyError`. Il existe une solution simple pour cela. Examinons comment nous pouvons éviter `KeyError` en utilisant la fonction intégrée `.get` pour les dictionnaires.

```python
dict_ = {}

# Une clé aléatoire
random_key = "random"

# La manière la plus basique de faire cela est de vérifier si la clé 
# existe dans le dictionnaire ou non et de ne récupérer que si la 
# clé existe. Sinon, ne pas récupérer. 
if random_key in dict_:
  print(dict_[random_key])
else:
  print("Key = {} doesn't exist in the dictionary".format(dict_))
```

Très souvent, nous sommes d'accord pour obtenir une valeur par défaut lorsque la clé n'existe pas. Par exemple, lors de la création d'un compteur. Il existe une meilleure façon d'obtenir des valeurs par défaut à partir du dictionnaire en cas de clés manquantes plutôt que de s'appuyer sur un `if-else` standard.

```python
# Supposons que nous voulons créer un compteur de fréquence pour les éléments dans le tableau suivant
arr = [1,2,3,1,2,3,4,1,2,1,4,1,2,3,1]

freq = {}

for item in arr:
  # Récupérer une valeur de 0 si la clé n'existe pas. Sinon, récupérer la valeur stockée
  freq[item] = freq.get(item, 0) + 1
```

Ainsi, `get(<key>, <defaultval>)` est une opération pratique pour récupérer la valeur par défaut pour toute clé donnée à partir du dictionnaire. Le problème avec cette méthode survient lorsque nous voulons traiter des structures de données mutables comme valeurs, par exemple `list` ou `set`.

```python
dict_ = {}

# Une clé aléatoire
random_key = "random"

dict_[random_key] = dict_.get(random_key, []).append("Hello World!")
print(dict_) # {'random': None}

dict_ = {}
dict_[random_key] = dict_.get(random_key, set()).add("Hello World!")
print(dict_) # {'random': None}
```

Avez-vous vu le problème ?

Le nouvel `set` ou `list` n'est pas assigné à la clé du dictionnaire. Nous devons assigner une nouvelle `list` ou un nouveau `set` à la clé en cas de valeur manquante et ensuite utiliser `append` ou `add` respectivement. Regardons un exemple pour cela.

```python
dict_ = {}
dict_[random_key] = dict_.get(random_key, set())
dict_[random_key].add("Hello World!")
print(dict_) # {'random': set(['Hello World!'])}. Hourra !
```

### **Éviter KeyError : Utiliser defaultdict**

Cela fonctionne la plupart du temps. Cependant, il existe une meilleure façon de faire cela. Une manière plus `pythonique`. Le `defaultdict` est une sous-classe de la classe dict intégrée. Le `defaultdict` assigne simplement la valeur par défaut que nous spécifions en cas de clé manquante. Ainsi, les deux étapes :

```python
dict_[random_key] = dict_.get(random_key, set())
dict_[random_key].add("Hello World!")
```

peuvent maintenant être combinées en une seule étape. Par exemple :

```python
from collections import defaultdict

# Encore une autre clé aléatoire
random_key = "random_key"

# defaultdict de liste
list_dict_ = defaultdict(list)

# defaultdict de set
set_dict_ = defaultdict(set)

# defaultdict d'entier
int_dict_ = defaultdict(int)

list_dict_[random_key].append("Hello World!")
set_dict_[random_key].add("Hello World!")
int_dict_[random_key] += 1

"""
  defaultdict(<class 'list'>, {'random_key': ['Hello World!']}) 
  defaultdict(<class 'set'>, {'random_key': {'Hello World!'}}) 
  defaultdict(<class 'int'>, {'random_key': 1})
"""
print(list_dict_, set_dict_, int_dict_)
```

[Documentation officielle](https://docs.python.org/2/library/collections.html)