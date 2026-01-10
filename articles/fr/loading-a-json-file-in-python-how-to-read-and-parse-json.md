---
title: Charger un fichier JSON en Python – Comment lire et analyser JSON
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-07-25T14:06:45.000Z'
originalURL: https://freecodecamp.org/news/loading-a-json-file-in-python-how-to-read-and-parse-json
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/read-parse-json-files.png
tags:
- name: json
  slug: json
- name: Python
  slug: python
seo_title: Charger un fichier JSON en Python – Comment lire et analyser JSON
seo_desc: 'By Dillion Megida

  In this article, you''ll learn how to read and parse JSON in Python.

  What is JSON?

  JSON is short for JavaScript Object Notation. It''s a simple syntax for storing
  data in name-value pairs. Values can be different data types as long as...'
---

Par Dillion Megida

Dans cet article, vous apprendrez à lire et analyser JSON en Python.

## Qu'est-ce que JSON ?

JSON signifie JavaScript Object Notation. C'est une syntaxe simple pour stocker des données en paires nom-valeur. Les valeurs peuvent être de différents types de données tant qu'elles sont valides. Les types non acceptables pour JSON incluent les fonctions, les dates et `undefined`.

Les fichiers JSON sont stockés avec l'extension `.json` avec une structure JSON valide.

Voici à quoi ressemble la structure d'un fichier JSON :

```json
{
  "name": "John",
  "age": 50,
  "is_married": false,
  "profession": null,
  "hobbies": ["traveling", "photography"]
}
```

Vous utiliserez souvent JSON pour envoyer et recevoir des données depuis un serveur dans des applications web.

Lorsque les données sont reçues, le programme lit et analyse le JSON pour extraire des données spécifiques. Différents langages ont leurs propres méthodes pour faire cela. Nous verrons comment faire cela en Python ici.

## Comment lire des fichiers JSON

Supposons que le JSON dans le bloc de code ci-dessus est stocké dans un fichier `user.json`. En utilisant la fonction intégrée `open()` en Python, nous pouvons lire ce fichier et assigner le contenu à une variable. Voici comment :

```python
with open('user.json') as user_file:
  file_contents = user_file.read()
  
print(file_contents)
# {
#   "name": "John",
#   "age": 50,
#   "is_married": false,
#   "profession": null,
#   "hobbies": ["travelling", "photography"]
# }
```

Vous passez le chemin du fichier à la méthode `open` qui ouvre le fichier et assigne les données de flux du fichier à la variable `user_file`. En utilisant la méthode `read`, vous pouvez passer le contenu textuel du fichier à la variable `file_contents`.

J'ai utilisé `with` au début de l'expression afin qu'après la lecture du contenu du fichier, Python puisse fermer le fichier.

`file_contents` contient maintenant une version stringifiée du JSON. En tant qu'étape suivante, vous pouvez maintenant analyser le JSON.

## Comment analyser JSON

Python dispose de modules intégrés pour diverses opérations. Pour gérer les fichiers JSON, Python dispose du module `json`.

Ce module vient avec de nombreuses méthodes. L'une d'entre elles est la méthode `loads()` pour analyser les chaînes JSON. Ensuite, vous pouvez assigner les données analysées à une variable comme ceci :

```js
import json

with open('user.json') as user_file:
  file_contents = user_file.read()
  
print(file_contents)

parsed_json = json.loads(file_contents)
# {
#   'name': 'John',
#   'age': 50,
#   'is_married': False,
#   'profession': None,
#   'hobbies': ['travelling', 'photography']
# }
```

En utilisant la méthode `loads()`, vous pouvez voir que la variable `parsed_json` contient maintenant un dictionnaire valide. À partir de ce dictionnaire, vous pouvez accéder aux clés et aux valeurs qu'il contient.

Remarquez également comment `null` du JSON est converti en `None` en Python. Cela est dû au fait que `null` n'est pas valide en `Python`.

## Comment utiliser `json.load()` pour lire et analyser des fichiers JSON

Le module `json` dispose également de la méthode `load` que vous pouvez utiliser pour lire un objet fichier et l'analyser en même temps. En utilisant cette méthode, vous pouvez mettre à jour le code précédent comme ceci :

```python
import json

with open('user.json') as user_file:
  parsed_json = json.load(user_file)

print(parsed_json)
# {
#   'name': 'John',
#   'age': 50,
#   'is_married': False,
#   'profession': None,
#   'hobbies': ['travelling', 'photography']
# }
```

Au lieu d'utiliser la méthode `read` de l'objet fichier et la méthode `loads` du module `json`, vous pouvez directement utiliser la méthode `load` qui lit et analyse l'objet fichier.

## Conclusion

Les données JSON sont communément connues pour leur structure simple et sont populaires (un standard dans la plupart des cas) pour l'échange d'informations entre serveurs et clients.

Différents langages et technologies peuvent lire et analyser des fichiers JSON de différentes manières. Dans cet article, nous avons appris à lire des fichiers JSON et à analyser de tels fichiers en utilisant la méthode `read` des objets fichier, et les méthodes `loads` et `load` du module `json`.