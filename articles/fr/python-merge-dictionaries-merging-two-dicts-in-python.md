---
title: Fusionner des dictionnaires Python – Fusion de deux dictionnaires en Python
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2023-05-11T21:51:40.000Z'
originalURL: https://freecodecamp.org/news/python-merge-dictionaries-merging-two-dicts-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/hannah-busing-Zyx1bK9mqmA-unsplash.jpg
tags:
- name: dictionary
  slug: dictionary
- name: Python
  slug: python
seo_title: Fusionner des dictionnaires Python – Fusion de deux dictionnaires en Python
seo_desc: "Dictionaries are one of the built-in data structures in Python. You can\
  \ use them to store data in key-value pairs. \nYou can read about the different\
  \ methods you can use to access, modify, add, and remove elements in a dictionary\
  \ here. \nIn this articl..."
---

Les dictionnaires sont l'une des structures de données intégrées en Python. Vous pouvez les utiliser pour stocker des données sous forme de paires clé-valeur. 

Vous pouvez lire les différentes méthodes que vous pouvez utiliser pour accéder, modifier, ajouter et supprimer des éléments dans un dictionnaire [ici](https://www.freecodecamp.org/news/python-dictionary-methods-dictionaries-in-python/). 

Dans cet article, vous apprendrez à fusionner deux dictionnaires en utilisant les méthodes suivantes :

* La méthode `update()`.
* L'opérateur double astérisque/étoile (`**`). 
* La méthode `chain()`.
* La méthode `ChainMap()`.
* L'opérateur de fusion (`|`).
* L'opérateur de mise à jour (`|=`).

## Comment fusionner deux dictionnaires en Python

Dans cette section, nous discuterons des différentes méthodes que vous pouvez utiliser pour fusionner des dictionnaires en Python, avec des exemples de code.

Tous les exemples que vous verrez dans cet article impliqueront la fusion de deux dictionnaires, mais vous pouvez en fusionner autant que vous le souhaitez.

### Comment fusionner deux dictionnaires en Python en utilisant la méthode `update()`

La méthode `update()` est une méthode intégrée que vous pouvez utiliser pour ajouter des données aux dictionnaires. 

Considérez le dictionnaire ci-dessous :

```python
devBio = {
  "name": "Ihechikara",
  "age": 500,
  "language": "Python"
}

devBio.update({"role": "Technical Writer"})

print(devBio)
# {'name': 'Ihechikara', 'age': 500, 'language': 'Python', 'role': 'Technical Writer'}
```

Dans le code ci-dessus, nous avons créé un dictionnaire appelé `devBio` avec trois paires clé-valeur : `{'name': 'Ihechikara', 'age': 50, 'language': 'Python'}`. 

En utilisant la méthode `update()`, nous avons ajouté une autre paire clé-valeur : `devBio.update({"role": "Technical Writer"})`. 

De la même manière, nous pouvons fusionner deux dictionnaires en passant un autre dictionnaire comme paramètre à la méthode `update()`. Voici un exemple :

```python
devBio = {
  "name": "Ihechikara",
  "age": 500,
  "language": "Python"
}

tools = {
  "dev environment": "JupyterLab",
  "os": "Windows",
  "visualization": "Matplotlib"
}

devBio.update(tools)

print(devBio)
# {'name': 'Ihechikara', 'age': 500, 'language': 'Python', 'dev environment': 'JupyterLab', 'os': 'Windows', 'visualization': 'Matplotlib'}
```

Dans le code ci-dessus, nous avons créé deux dictionnaires — `devBio` et `tools`. 

En utilisant la méthode `update()`, nous avons fusionné les paires clé-valeur du dictionnaire `tools` avec le dictionnaire `devBio` : `devBio.update(tools)`. 

Les dictionnaires fusionnés ressemblaient à ceci : 

```python
{
    'name': 'Ihechikara', 
    'age': 500, 
    'language': 'Python', 
    'dev environment': 'JupyterLab', 
    'os': 'Windows', 
    'visualization': 'Matplotlib'
}
```

### Comment fusionner deux dictionnaires en Python en utilisant l'opérateur double astérisque (`**`)

Vous pouvez utiliser l'opérateur double astérisque (également appelé double étoile) (`**`) pour "dépaqueter" et fusionner les paires clé-valeur de deux dictionnaires ou plus dans une variable. 

Voici un exemple de code : 

```python
devBio = {
  "name": "Ihechikara",
  "age": 500,
  "language": "Python"
}

tools = {
  "dev environment": "JupyterLab",
  "os": "Windows",
  "visualization": "Matplotlib"
}

merged_bio = { **devBio, **tools}

print(merged_bio)
# {'name': 'Ihechikara', 'age': 500, 'language': 'Python', 'dev environment': 'JupyterLab', 'os': 'Windows', 'visualization': 'Matplotlib'}
```

Dans le code ci-dessus, nous avons dépaqueté les dictionnaires `devBio` et `tools` en utilisant l'opérateur double astérisque : `{ **devBio, **tools}`. 

Nous les avons ensuite stockés dans une variable appelée `merged_bio`. 

### Comment fusionner deux dictionnaires en Python en utilisant la méthode `chain()`

La méthode `chain()` prend plusieurs objets itérables comme paramètres. Elle fusionne et retourne les objets sous forme d'un seul objet itérable. 

Vous devez importer la méthode `chain()` du module `itertools` avant de l'utiliser : 

```python
from itertools import chain

devBio = {
  "name": "Ihechikara",
  "age": 500,
  "language": "Python"
}

tools = {
  "dev environment": "JupyterLab",
  "os": "Windows",
  "visualization": "Matplotlib"
}

merged_bio = dict(chain(devBio.items(), tools.items()))

print(merged_bio)
# {'name': 'Ihechikara', 'age': 500, 'language': 'Python', 'dev environment': 'JupyterLab', 'os': 'Windows', 'visualization': 'Matplotlib'}

```

Dans le code ci-dessus, nous avons passé les dictionnaires à fusionner comme paramètres à la méthode `chain()` : `chain(devBio.items(), tools.items())`. 

Nous avons utilisé la méthode `items()` pour accéder aux paires clé-valeur de chaque dictionnaire. 

Enfin, nous avons imbriqué la méthode `chain()` et ses paramètres dans la méthode `dict()` : `dict(chain(devBio.items(), tools.items()))`.

La méthode `dict()` peut être utilisée pour créer un dictionnaire, nous l'avons donc utilisée pour convertir les objets itérables retournés (les paires clé-valeur) en un dictionnaire, et nous les avons stockés dans la variable `merged_bio`.

### Comment fusionner deux dictionnaires en Python en utilisant la méthode `ChainMap()`

La méthode `ChainMap()` fonctionne de la même manière que la méthode `chain()` en ce qui concerne la fusion de dictionnaires. La principale différence est que vous n'avez pas besoin de la méthode `items()` pour accéder aux paires clé-valeur des dictionnaires. 

Vous pouvez importer la méthode `ChainMap()` du module `collections`. 

Voici comment vous pouvez utiliser la méthode `ChainMap()` pour fusionner deux dictionnaires :

```python
from collections import ChainMap

devBio = {
  "name": "Ihechikara",
  "age": 500,
  "language": "Python"
}

tools = {
  "dev environment": "JupyterLab",
  "os": "Windows",
  "visualization": "Matplotlib"
}

merged_bio = dict(ChainMap(devBio, tools))

print(merged_bio)
# {'name': 'Ihechikara', 'age': 500, 'language': 'Python', 'dev environment': 'JupyterLab', 'os': 'Windows', 'visualization': 'Matplotlib'}
```

Vous pouvez consulter l'explication dans la dernière section pour comprendre la logique dans le code ci-dessus. 

### Comment fusionner deux dictionnaires en Python en utilisant l'opérateur de fusion (`|`)

L'opérateur de fusion (`|`) a été introduit pour la première fois dans Python 3.9. C'est une syntaxe plus courte et plus simple que vous pouvez utiliser pour fusionner des dictionnaires. 

Voici un exemple :

```python
from collections import ChainMap

devBio = {
  "name": "Ihechikara",
  "age": 500,
  "language": "Python"
}

tools = {
  "dev environment": "JupyterLab",
  "os": "Windows",
  "visualization": "Matplotlib"
}

merged_bio = devBio | tools

print(merged_bio)
# {'name': 'Ihechikara', 'age': 500, 'language': 'Python', 'dev environment': 'JupyterLab', 'os': 'Windows', 'visualization': 'Matplotlib'}
```

Ainsi, pour fusionner les dictionnaires `devBio` et `tools`, nous avons placé l'opérateur `|` entre eux : `devBio | tools`.

### Comment fusionner deux dictionnaires en Python en utilisant l'opérateur de mise à jour (`|=`)

L'opérateur de mise à jour (`|=`) est un autre opérateur qui a été introduit dans Python 3.9. 

Il fonctionne exactement comme la méthode `update()`. C'est-à-dire : 

```python
from collections import ChainMap

devBio = {
  "name": "Ihechikara",
  "age": 500,
  "language": "Python"
}

tools = {
  "dev environment": "JupyterLab",
  "os": "Windows",
  "visualization": "Matplotlib"
}

devBio |= tools

print(devBio)
# {'name': 'Ihechikara', 'age': 50, 'language': 'Python', 'dev environment': 'JupyterLab', 'os': 'Windows', 'visualization': 'Matplotlib'}
```

Dans le code ci-dessus, nous avons utilisé le `|=` pour fusionner les paires clé-valeur du dictionnaire `tools` dans le dictionnaire `devBio`.

## Résumé

Dans cet article, nous avons parlé des dictionnaires en Python. Vous pouvez les utiliser pour stocker des données sous forme de paires clé-valeur. 

Nous avons vu comment fusionner deux dictionnaires en Python en utilisant :

* La méthode `update()`.
* L'opérateur double astérisque/étoile (`**`). 
* La méthode `chain()`.
* La méthode `ChainMap()`.
* L'opérateur de fusion (`|`).
* L'opérateur de mise à jour (`|=`).

Chaque méthode avait sa propre section avec des exemples de code qui montraient comment les utiliser pour fusionner des dictionnaires. 

Bon codage ! Vous pouvez en apprendre plus sur Python sur [mon blog](https://ihechikara.com/).