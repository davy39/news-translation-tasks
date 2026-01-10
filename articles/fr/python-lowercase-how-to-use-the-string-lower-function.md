---
title: Python Minuscule – Comment utiliser la fonction de chaîne lower()
subtitle: ''
author: Ilenia Magoni
co_authors: []
series: null
date: '2022-05-09T22:04:42.000Z'
originalURL: https://freecodecamp.org/news/python-lowercase-how-to-use-the-string-lower-function
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/pexels-christina-morillo-1181467--1-.jpg
tags:
- name: Python
  slug: python
seo_title: Python Minuscule – Comment utiliser la fonction de chaîne lower()
seo_desc: 'Strings are a fundamental part of working with Python. And the lower()
  method is one of the many integrated methods that you can use to work with strings.

  In this article, we''ll see how to make strings lowercase with the lower() method
  in Python.

  Wha...'
---

Les chaînes de caractères sont une partie fondamentale de la programmation en Python. Et la méthode `lower()` est l'une des nombreuses méthodes intégrées que vous pouvez utiliser pour travailler avec les chaînes de caractères.

Dans cet article, nous verrons comment rendre les chaînes de caractères en minuscules avec la méthode `lower()` en Python.

## Qu'est-ce qu'une chaîne de caractères ?

Une chaîne de caractères est un type de données qui peut contenir de nombreux caractères différents. Une chaîne de caractères est écrite comme une série de caractères entre des guillemets simples ou doubles.

```python
>>> example_string = 'I am a String!'
>>> example_string
'I am a String!'
```

## Qu'est-ce qu'une méthode ?

Une méthode est une fonction qui peut être utilisée sur un type de données spécifique. Les méthodes peuvent prendre ou non des arguments.

Parfois, vous pouvez vous demander si une méthode existe. En Python, vous pouvez voir la liste complète des méthodes de chaîne de caractères en utilisant la fonction `dir()` avec une chaîne de caractères comme argument, comme ceci :

```python
>>> dir(example_string)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```

Parmi ces nombreuses méthodes de chaîne de caractères, dans cet article, vous apprendrez à connaître la méthode `lower()` et son fonctionnement.

## Comment fonctionne la méthode `lower()` ?

La méthode `lower()` est une méthode de chaîne de caractères qui retourne une nouvelle chaîne de caractères, entièrement en minuscules. Si la chaîne de caractères originale contient des lettres majuscules, dans la nouvelle chaîne, celles-ci seront en minuscules. Toute lettre minuscule ou tout caractère qui n'est pas une lettre n'est pas affecté.

```
>>> example_string.lower()
'i am a string!'

>>> 'FREECODECAMP'.lower()
'freecodecamp'
```

## Ce qu'il faut garder à l'esprit lors de l'utilisation de la méthode lower

La méthode `lower()` fait quelque chose de assez simple : elle crée une nouvelle chaîne où toutes les lettres majuscules sont maintenant en minuscules. Mais il y a quelques choses à garder à l'esprit lors de son utilisation. Examinons-les.

### Les chaînes de caractères sont immuables

Les chaînes de caractères sont un type de données immuable, ce qui signifie qu'elles ne peuvent pas être modifiées. La chaîne de caractères originale restera inchangée après l'utilisation de la méthode `lower()`.

Dans les exemples ci-dessus, la méthode `lower()` a agi sur la `example_string` mais ne l'a jamais modifiée. La vérification de la valeur de `example_string` montre toujours la valeur originale.

```python
>>> example_string
'I am a String!'

>>> example_string.lower()
'i am a string!'

>>> example_string
'I am a String!'
```

### La méthode `lower()` retourne une nouvelle chaîne de caractères

La méthode `lower()` retourne une nouvelle chaîne de caractères. Vous devrez l'enregistrer dans une variable si vous souhaitez l'utiliser à nouveau dans votre code.

```python
>>> new_string = example_string.lower()

>>> new_string
'i am a string!'
```

### Les chaînes de caractères sont sensibles à la casse

Les chaînes de caractères sont sensibles à la casse, donc une chaîne en minuscules est différente d'une chaîne en majuscules.

```python
>>> 'freecodecamp' == 'FREECODECAMP'
False
```

Cela est utile lorsque l'on pense à ce pour quoi la méthode `lower()` pourrait être utile. Dans l'exemple, vous verrez comment cette fonctionnalité rend la méthode `lower()` utile et nécessaire lors de la création d'un script ou d'un programme qui traite des chaînes de caractères.

## Exemple de la méthode `lower()` : comment vérifier si la saisie de l'utilisateur correspond

Écrivons un petit script qui pose une question à l'utilisateur et attend une réponse, puis donne un retour sur la réponse de l'utilisateur.

```python
answer = input("What color is the sun? ")
if answer == "yellow":
  print("Correct!")
else:
  print("That is not the correct color!")
```

Ce script pose une question à l'utilisateur, "What color is the sun?", et attend une réponse. Ensuite, il vérifie si la réponse est "yellow", et si c'est le cas, il imprime "Correct!". Si ce n'est pas le cas, il imprime "That is not the correct color!".

Mais il y a un problème avec ce script.

En exécutant ce script, vous aurez cette question posée dans le terminal :

```shell
$ python sun_color.py
What color is the sun? 
```

Si vous répondez "Yellow", il dit :

```shell
$ python sun_color.py
What color is the sun? Yellow
That is not the correct color!
```

Pourquoi cela se produit-il ?

Rappelez-vous que les chaînes de caractères sont sensibles à la casse. Le script vérifie si l'utilisateur a saisi la chaîne `yellow` – `Yellow`, avec un "Y" majuscule, est une chaîne différente.

Vous pouvez facilement corriger cela en utilisant la méthode `lower()`, et en apportant cette petite modification au fichier `sun_color.py` :

```python
answer = input("What color is the sun? ")
if answer.lower() == "yellow":
  print("Correct!")
else:
  print("That is not the correct color!")
```

Et maintenant, si vous essayez à nouveau...

```
>>> python sun_color.py
What color is the sun? Yellow
Correct!
```

Qu'est-ce qui a changé ? En écrivant `answer.lower()`, vous vous assurez que la chaîne vérifiée est entièrement en minuscules avant de la comparer avec la chaîne de réponse correcte "yellow". De cette manière, peu importe si l'utilisateur écrit "YELLOW" ou "yELLOW" ou "yellow" – tout est converti en minuscules.

Merci d'avoir lu ! Maintenant, vous savez comment utiliser la méthode `lower()` en JavaScript.