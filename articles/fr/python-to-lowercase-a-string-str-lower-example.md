---
title: Python pour convertir une chaîne en minuscules – exemple de str.lower()
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-08-26T20:12:09.000Z'
originalURL: https://freecodecamp.org/news/python-to-lowercase-a-string-str-lower-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/string-lowercase.png
tags:
- name: Python
  slug: python
seo_title: Python pour convertir une chaîne en minuscules – exemple de str.lower()
seo_desc: 'By Dillion Megida

  Strings can be in different formats such as lowercase, capitalized, and uppercase.
  In this article, I''ll show you how to convert a string to lowercase in Python.

  A lowercase string has all its characters in small letters. An example...'
---

Par Dillion Megida

Les chaînes de caractères peuvent être dans différents formats tels que minuscules, capitalisées et majuscules. Dans cet article, je vais vous montrer comment convertir une chaîne de caractères en minuscules en Python.

Une chaîne en minuscules a tous ses caractères en petites lettres. Un exemple est **python**.

Une chaîne capitalisée a la première lettre de chaque mot en majuscule, et les lettres restantes sont en minuscules. Un exemple est **Python**.

Une chaîne en majuscules a tous ses caractères en lettres capitales. **PYTHON** est un exemple.

Python dispose de nombreuses méthodes de chaînes pour modifier les chaînes de différentes manières. Pour convertir une chaîne en minuscules, vous pouvez utiliser la méthode `lower`.

La méthode `lower` des chaînes retourne une nouvelle chaîne à partir de l'ancienne avec tous les caractères en minuscules. Les nombres, les symboles et tous les autres caractères non alphabétiques restent les mêmes.

## Exemples de str.lower() en Python

Voici comment utiliser la méthode `lower` en Python :

```python
texte = "HellO woRLd!"

minuscules = texte.lower()

print(minuscules)
# hello world!
```

Un bon cas d'utilisation de la méthode `lower` est la comparaison de chaînes pour évaluer leur égalité indépendamment de la casse.

En Python, "Hello World" n'est pas égal à "hello world" car l'égalité est sensible à la casse comme vous pouvez le voir dans le code ci-dessous :

```python
texte1 = "Hello World"
texte2 = "hello world"

print(texte1 == texte2)
# False
```

`texte1` a un "H" et un "W" majuscules tandis que `texte2` a un "h" et un "w" minuscules. Parce que la casse de ces caractères est différente, `texte1` n'est pas égal à `texte2` même s'ils ont les mêmes caractères.

Pour comparer les deux chaînes en ignorant leur casse, vous pouvez utiliser la méthode `lower` comme ceci :

```python
texte1 = "HeLLo worLD"
texte2 = "HellO WORLd"

print(texte1 == texte2)
# False

print(texte1.lower() == texte2.lower())
# True
```

En convertissant les deux chaînes en minuscules, vous pouvez correctement vérifier si elles ont les mêmes caractères.

## Comment utiliser `upper` en Python

L'opposé de minuscules est majuscules, et Python dispose également d'une méthode pour cela. Comme vous l'avez peut-être deviné, la méthode `upper` en Python retourne une nouvelle chaîne où tous les caractères sont en majuscules.

Vous pouvez l'utiliser de manière similaire à la méthode `lower` comme ceci :

```python
texte = "hello World!"

majuscules = texte.upper()

print(majuscules)
# HELLO WORLD!
```

Vous pouvez également utiliser cette méthode pour vérifier que deux chaînes ont le même ensemble de caractères. Mais dans la plupart des applications aujourd'hui, les développeurs utilisent l'approche de comparaison en minuscules.

C'est tout ! Maintenant, vous savez comment convertir une chaîne de caractères en lettres minuscules ou majuscules en Python.