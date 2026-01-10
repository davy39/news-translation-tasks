---
title: Python Convertir une Chaîne en Entier – Comment Convertir une Chaîne en Python
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2021-11-29T16:47:01.000Z'
originalURL: https://freecodecamp.org/news/python-convert-string-to-int-how-to-cast-a-string-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/glenn-carstens-peters-npxXWgQ33ZQ-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: Python Convertir une Chaîne en Entier – Comment Convertir une Chaîne en
  Python
seo_desc: 'When you''re programming, you''ll often need to switch between data types.

  The ability to convert one data type to another gives you great flexibility when
  working with information.

  There are different built-in ways to convert, or cast, types in the Py...'
---

Lorsque vous programmez, vous devrez souvent passer d'un type de données à un autre.

La capacité de convertir un type de données en un autre vous offre une grande flexibilité lorsque vous travaillez avec des informations.

Il existe différentes méthodes intégrées pour convertir, ou caster, des types dans le langage de programmation Python.

Dans cet article, vous apprendrez à convertir une chaîne de caractères en un entier.

Commençons !

## Types de données en Python

Python prend en charge une variété de types de données.

Les types de données sont utilisés pour spécifier, représenter et catégoriser les différents types de données qui existent et sont utilisés dans les programmes informatiques.

De plus, différentes opérations sont disponibles avec différents types de données – une opération disponible dans un type de données est souvent indisponible dans un autre.

Un exemple de type de données est les chaînes de caractères.

Les chaînes de caractères sont des séquences de caractères utilisées pour transmettre des informations textuelles.

Elles sont entourées de guillemets simples ou doubles, comme ceci :

```python
fave_phrase = "Hello world!"

#Hello world! est une chaîne de caractères, entourée de guillemets doubles
```

Les entiers, ou ints, sont des nombres entiers.

Ils sont utilisés pour représenter des données numériques, et vous pouvez effectuer toute opération mathématique (comme l'addition, la soustraction, la multiplication et la division) lorsque vous travaillez avec des entiers.

Les entiers ne sont *pas* entourés de guillemets simples ou doubles.

```python
fave_number = 7

#7 est un entier
#"7" ne serait pas un entier mais une chaîne de caractères, malgré le fait que ce soit un nombre.
#Cela est dû aux guillemets qui l'entourent
```

### Conversion de type de données

Parfois, lorsque vous stockez des données, ou lorsque vous recevez une entrée d'un utilisateur dans un certain type, vous devrez manipuler et effectuer différentes sortes d'opérations sur ces données.

Puisque chaque type de données peut être manipulé de différentes manières, cela signifie souvent que vous devrez le convertir.

Convertir un type de données en un autre est également appelé type casting ou conversion de type. De nombreux langages offrent des opérateurs de casting intégrés pour faire exactement cela – convertir explicitement un type en un autre.

## Comment convertir une chaîne de caractères en un entier en Python

Pour convertir, ou caster, une chaîne de caractères en un entier en Python, vous utilisez la fonction intégrée `int()`.

La fonction prend en paramètre la chaîne initiale que vous souhaitez convertir, et retourne l'équivalent entier de la valeur que vous avez passée.

La syntaxe générale ressemble à ceci : `int("str")`.

Prenons l'exemple suivant, où il y a la version chaîne d'un nombre :

```python
#version chaîne du nombre 7
print("7")

#vérifier le type de données avec la méthode type()
print(type("7"))

#sortie

#7
#<class 'str'>
```

Pour convertir la version chaîne du nombre en son équivalent entier, vous utilisez la fonction `int()`, comme ceci :

```python
#convertir la chaîne en type de données int
print(int("7"))

#vérifier le type de données avec la méthode type()
print(type(int("7")))

#sortie

#7
#<class 'int'>
```

### Un exemple pratique de conversion d'une chaîne en un entier

Supposons que vous souhaitiez calculer l'âge d'un utilisateur. Vous le faites en recevant une entrée de sa part. Cette entrée sera toujours au format chaîne.

Ainsi, même s'ils tapent un nombre, ce nombre sera de `<class 'str'>`.

Si vous souhaitez ensuite effectuer des opérations mathématiques sur cette entrée, comme soustraire cette entrée d'un autre nombre, vous obtiendrez une erreur car vous ne pouvez pas effectuer d'opérations mathématiques sur des chaînes de caractères.

Consultez l'exemple ci-dessous pour voir cela en action :

```python
current_year = 2021

#demander à l'utilisateur de saisir son année de naissance
user_birth_year_input = input("Quelle est votre année de naissance ? ")

#soustraire l'année saisie par l'utilisateur de l'année en cours
user_age = current_year - user_birth_year_input

print(user_age)

#sortie

#Quelle est votre année de naissance ? 1993
#Traceback (most recent call last):
#  File "demo.py", line 9, in <module>
#    user_age = current_year - user_birth_year_input
#TypeError: unsupported operand type(s) for -: 'int' and 'str'
```

L'erreur mentionne que la soustraction ne peut pas être effectuée entre un entier et une chaîne de caractères.

Vous pouvez vérifier le type de données de l'entrée en utilisant la méthode `type()` :

```python
current_year = 2021

#demander à l'utilisateur de saisir son année de naissance
user_birth_year_input = input("Quelle est votre année de naissance ? ")

print(type(user_birth_year_input))

#sortie

#Quelle est votre année de naissance ? 1993
#<class 'str'>
```

La solution pour éviter les erreurs est de convertir l'entrée de l'utilisateur en un entier et de la stocker dans une nouvelle variable :

```python
current_year = 2021

#demander à l'utilisateur de saisir son année de naissance
user_birth_year_input = input("Quelle est votre année de naissance ? ")

#convertir l'entrée brute de l'utilisateur en un entier en utilisant la fonction int() et stocker dans une nouvelle variable
user_birth_year = int(user_birth_year_input)

#soustraire l'entrée convertie de l'utilisateur de l'année en cours
user_age = current_year - user_birth_year

print(user_age)

#sortie

#Quelle est votre année de naissance ? 1993
#28
```

## Conclusion

Et voilà - vous savez maintenant comment convertir des chaînes de caractères en entiers en Python !

Si vous souhaitez en apprendre davantage sur le langage de programmation Python, freeCodeCamp propose une [Certification Python](https://www.freecodecamp.org/learn/scientific-computing-with-python/) pour vous lancer.

Vous commencerez par les bases et progresserez vers des sujets plus avancés comme les structures de données et les bases de données relationnelles. À la fin, vous construirez cinq projets pour pratiquer ce que vous avez appris.

Merci d'avoir lu et bon codage !