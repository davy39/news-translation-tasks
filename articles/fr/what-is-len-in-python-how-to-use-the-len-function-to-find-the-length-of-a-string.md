---
title: Qu'est-ce que len() en Python ? Comment utiliser la fonction len() pour trouver
  la longueur d'une chaîne
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-02-24T18:35:06.000Z'
originalURL: https://freecodecamp.org/news/what-is-len-in-python-how-to-use-the-len-function-to-find-the-length-of-a-string
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/leninpython.png
tags:
- name: Python
  slug: python
seo_title: Qu'est-ce que len() en Python ? Comment utiliser la fonction len() pour
  trouver la longueur d'une chaîne
seo_desc: "In programming languages, getting the length of a particular data type\
  \ is a common practice. \nPython is no different because you can use the built-in\
  \ len() function to get the length of a string, tuple, list, dictionary, or any\
  \ other data type.\nIn th..."
---

Dans les langages de programmation, obtenir la longueur d'un type de données particulier est une pratique courante. 

Python ne fait pas exception car vous pouvez utiliser la fonction intégrée `len()` pour obtenir la longueur d'une chaîne, d'un tuple, d'une liste, d'un dictionnaire ou de tout autre type de données.

Dans cet article, je vais vous montrer comment obtenir la longueur d'une chaîne avec la fonction `len()`.

## Syntaxe de base pour `len()` en Python

Pour utiliser la fonction `len()` afin d'obtenir la longueur d'un type de données, affectez le type de données à une variable, puis passez le nom de la variable à la fonction `len()`.

Comme ceci :
```py
len(nomVariable)
```
## Comment trouver la longueur d'une chaîne avec la fonction `len()`

Lorsque vous utilisez la fonction `len()` pour obtenir la longueur d'une chaîne, elle retourne le nombre de caractères dans la chaîne – y compris les espaces.

Voici 3 exemples pour vous montrer comment cela fonctionne :

```py
nom = "freeCodeCamp"
print(len(nom))

# Sortie : 12
```

Cela signifie qu'il y a 12 caractères dans la chaîne.

```py
fondateur = "Quincy Larson"
print(len(fondateur))

# Sortie : 13
```

Cela signifie qu'il y a 13 caractères dans la chaîne.

```py
description = "freeCodeCamp est une plateforme pour apprendre à coder gratuitement"
print(len(description))

# Sortie : 60
```

Cela signifie qu'il y a 60 caractères dans la chaîne.

## Comment `len()` fonctionne avec d'autres types de données en Python

Vous vous demandez peut-être comment la fonction `len()` fonctionne sur d'autres types de données tels que les listes et les tuples.

Lorsque vous utilisez la fonction `len()` sur un type de données comme un tuple ou une liste, elle retourne le nombre d'éléments dans le tuple ou la liste, et non le nombre de caractères.

Par exemple, 3 est retourné pour la longueur du tuple ci-dessous, et non le nombre de caractères des mots qu'il contient.

```py
langs = ("Python", "JavaScript", "Golang")
print(len(langs))

# Sortie : 3
```

Cela dépend donc du type de données avec lequel vous travaillez.

## Conclusion

Dans cet article, vous avez appris comment obtenir la longueur d'une chaîne – le nombre de caractères.

Merci d'avoir lu.