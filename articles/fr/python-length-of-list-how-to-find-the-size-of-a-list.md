---
title: "Longueur d'une liste en Python \x13 Comment trouver la taille d'une liste"
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-01-31T16:56:55.000Z'
originalURL: https://freecodecamp.org/news/python-length-of-list-how-to-find-the-size-of-a-list
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/18.-length-of-list.png
tags:
- name: Python
  slug: python
seo_title: "Longueur d'une liste en Python \x13 Comment trouver la taille d'une liste"
seo_desc: 'By Dillion Megida

  A list is a data structure in Python that contains multiple elements in a particular
  order. And sometimes you might need to get the size of a list. I''ll show you how
  to do that in this article.

  How to Create a List in Python

  You can...'
---

Par Dillion Megida

Une liste est une structure de données en Python qui contient plusieurs éléments dans un ordre particulier. Et parfois, vous pourriez avoir besoin d'obtenir la taille d'une liste. Je vais vous montrer comment faire cela dans cet article.

## Comment créer une liste en Python

Vous pouvez créer des listes en Python avec des crochets. Dans les crochets, vous spécifiez les différents éléments (ou valeurs) séparés par des virgules.

Vous pouvez stocker des chaînes de caractères, des nombres, des listes, etc. dans une liste :

```python
items = ["python", True, [50, 30], 80]

print(items)
# ['python', True, [50, 30], 80]

print(items[2][0])
# 30
```

Ici, nous avons également une liste imbriquée.

Alors, comment obtenir la longueur d'une liste ? Pour une liste avec seulement quelques éléments, il est facile de compter les éléments manuellement. Mais une liste plus longue peut ne pas être aussi facile.

Eh bien, vous pouvez faire cela facilement en Python. Je vais vous montrer deux méthodes : une méthode longue et une méthode plus courte.

J'ai une [courte vidéo sur ce sujet](https://youtu.be/Ao9P6zTGMgQ) que vous pouvez également consulter.

## Comment obtenir la taille d'une liste en utilisant une boucle `for` en Python

Vous pouvez obtenir la taille d'une liste en parcourant la liste et en gardant une trace de la taille à l'aide d'une variable. Voici ce que je veux dire :

```python
languages = ["python", "javascript", "ruby", "java", "go"]

# initialiser la variable size
size = 0

for value in languages:
  # incrémenter la variable à chaque boucle
  size = size + 1

print(size)
# 5
```

Dans cet exemple, nous avons un tableau de cinq valeurs. D'abord, nous initialisons une variable `size` à 0. Ensuite, nous avons l'instruction de boucle for, où nous parcourons chaque valeur dans le tableau. À chaque boucle, nous incrémentons la variable `size` de 1. À la fin, la variable `size` contiendra la taille de la liste.

Regardons maintenant la méthode courte.

## Comment obtenir la taille d'une liste en utilisant la fonction `len` en Python

La fonction `len` retourne le nombre de valeurs dans un itérable en Python. C'est une fonction simple et efficace à cet effet. Un itérable peut être une liste ou un dictionnaire.

Voyons un exemple pour obtenir la longueur d'une liste :

```python
languages = ["python", "javascript", "ruby", "java", "go"]

length = len(languages)

print(length)
# 5
```

En passant la liste `languages` comme argument à `len`, la fonction retourne le nombre de valeurs qu'elle contient, qui est 5.

La fonction `len` n'est pas seulement pour les listes comme je l'ai mentionné précédemment. Vous pouvez également l'utiliser sur des dictionnaires et des chaînes de caractères :

```python
dict = {
  "name": "Dillion",
  "age": 70,
  "language": "python"
}

print(len(dict))
# 3

sentence = "I am Dillion"

print(len(sentence))
# 12
```

Pour le dictionnaire `dict`, `len` retourne le nombre de propriétés. Pour la chaîne de caractères `sentence`, `len` retourne le nombre de caractères.

## Conclusion

Dans cet article, nous avons vu comment obtenir la taille d'une liste en utilisant une approche longue  l'instruction de boucle `for`  et une approche plus courte et plus efficace  la fonction `len`.

Si vous avez aimé cela, merci de le partager. :)