---
title: Comment convertir des chaînes de caractères en entiers en Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-16T16:58:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-convert-strings-into-integers-in-python
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9dd6740569d1a4ca39e8.jpg
tags:
- name: Python
  slug: python
seo_title: Comment convertir des chaînes de caractères en entiers en Python
seo_desc: 'Similar to the built-in str() method, Python also offers the handy int()
  method that takes a string object as an argument and returns an integer.

  Example Usage:

  # Here age is a string object

  age = "18"

  print(age)


  # Converting a string to an integer

  ...'
---

Similaire à la méthode intégrée `str()`, Python offre également la méthode pratique `int()` qui prend un objet chaîne de caractères comme argument et retourne un entier.

#### **Exemple d'utilisation :**

```py
# Ici, age est un objet chaîne de caractères
age = "18"
print(age)

# Conversion d'une chaîne de caractères en entier
int_age = int(age)
print(int_age)
```

**Sortie :**

```py
18
18
```

Bien que la sortie soit visuellement similaire, gardez à l'esprit que la première ligne est un objet chaîne de caractères tandis que la ligne suivante est un objet entier. Cela est illustré plus en détail dans l'exemple suivant :

```py
age = "18"
print(age + 2)
```

**Sortie :**

```py
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: cannot concatenate 'str' and 'int' objects
```

L'erreur devrait vous indiquer clairement que vous devez convertir l'objet `age` en entier avant d'ajouter quelque chose à celui-ci.

```py
age = "18"
age_int = int(age)
print(age_int + 2)
```

**Sortie :**

```py
20
```

Mais gardez ces cas particuliers à l'esprit :

* Un nombre à virgule flottante (un entier avec une partie fractionnaire) comme argument retournera le nombre arrondi à l'entier inférieur le plus proche. Par exemple : `print(int(7.9))` affichera `7`. En revanche, `print(int("7.9"))` entraînera une erreur, car une chaîne de caractères représentant un nombre à virgule flottante ne peut pas être convertie en entier.

```py
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '7.9'
```

* Des mots donnés comme argument retourneront la même erreur. Par exemple, `print(int("one"))` retournera :

```py
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'one'
```