---
title: Que signifie // en Python ? Opérateurs en Python
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-07-21T15:30:37.000Z'
originalURL: https://freecodecamp.org/news/what-does-double-slash-mean-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/doubleSlash.png
tags:
- name: Math
  slug: math
- name: Python
  slug: python
seo_title: Que signifie // en Python ? Opérateurs en Python
seo_desc: 'In Python, you use the double slash // operator to perform floor division.
  This // operator divides the first number by the second number and rounds the result
  down to the nearest integer (or whole number).

  In this article, I will show you how to use...'
---

En Python, vous utilisez l'opérateur double barre `//` pour effectuer une division entière. Cet opérateur `//` divise le premier nombre par le second et arrondit le résultat à l'entier le plus proche (ou nombre entier).

Dans cet article, je vais vous montrer comment utiliser l'opérateur `//` et le comparer à la division régulière afin que vous puissiez voir comment il fonctionne.

Mais ce n'est pas tout, vous apprendrez également une méthode mathématique Python qui est synonyme de l'opérateur double barre `//`.

## Ce que nous allons couvrir
- [La syntaxe de base de l'opérateur `//`](#heading-la-syntaxe-de-base-de-loperateur)
- [Exemples de division entière](#heading-exemples-de-division-entiere)
- [L'opérateur double barre `//` fonctionne comme `math.floor()`](#heading-loperateur-double-barre-fonctionne-comme-mathfloor)
- [Comment l'opérateur double barre `//` fonctionne en coulisses](#heading-comment-loperateur-double-barre-fonctionne-en-coulisses)
- [Conclusion](#heading-conclusion)

## La syntaxe de base de l'opérateur `//`

Pour utiliser l'opérateur double barre `//`, vous faites presque la même chose que pour une division régulière. La seule différence est qu'au lieu d'une seule barre `/`, vous utilisez une double barre `//` :
```py
premierNombre // secondNombre
```

## Exemples de division entière

Dans l'exemple ci-dessous, la division entière de 12 par 5 donne 2 :
```py
num1 = 12
num2 = 5
num3 = num1 // num2

print("division entière de", num1, "par", num2, "=", num3)
# Sortie : division entière de 12 par 5 = 2
```
Alors que la division régulière de 12 par 5 serait égale à 2,4. C'est-à-dire 2 reste 4 :
```py
num1 = 12
num2 = 5
num3 = num1 / num2

print("division normale de", num1, "par", num2, "=", num3)
# Sortie : division normale de 12 par 5 = 2.4
```

Cela vous montre que l'opérateur `//` arrondit le résultat de la division de deux nombres à l'entier le plus proche.

Même si la partie décimale est 9, l'opérateur `//` arrondirait toujours le résultat à l'entier le plus proche.

```py
num1 = 29
num2 = 10
num3 = num1 / num2
num4 = num1 // num2

print("division normale de", num1, "par", num2, "=", num3)
print("mais division entière de", num1, "par", num2, "=", num4)

"""
Sortie :
division normale de 29 par 10 = 2.9
mais division entière de 29 par 10 = 2
"""
```
Et si vous effectuez une division entière avec un nombre négatif, le résultat serait toujours arrondi à l'entier inférieur.

Pour vous préparer à ce résultat, arrondir un nombre négatif signifie s'éloigner de 0. Donc, -12 divisé par 5 donne -3. Ne vous y trompez pas, même si à première vue il semble que le nombre devient "plus grand", il devient en réalité plus petit (plus éloigné de zéro/un nombre négatif plus grand).
```py
num1 = -12
num2 = 5
num3 = num1 // num2

print("division entière de", num1, "par", num2, "=", num3)

# division entière de -12 par 5 = -3
```

## L'opérateur double barre `//` fonctionne comme `math.floor()`
En Python, `math.floor()` arrondit un nombre à l'entier le plus proche, tout comme l'opérateur double barre `//`.

Ainsi, `math.floor()` est une alternative à l'opérateur `//` car ils font la même chose en coulisses.

Voici un exemple :
```py
import math

num1 = 12
num2 = 5
num3 = num1 // num2
num4 = math.floor(num1 / num2)

print("division entière de", num1, "par", num2, "=", num3)
print("math.floor de", num1, "divisé par", num2, "=", num4)

"""
Sortie :
division entière de 12 par 5 = 2
math.floor de 12 divisé par 5 = 2
"""
```
Vous pouvez voir que `math.floor()` fait la même chose que l'opérateur `//`.

## Comment l'opérateur double barre `//` fonctionne en coulisses

Lorsque vous utilisez l'opérateur `//` pour diviser deux nombres, la méthode appelée en coulisses est `__floordiv__()`.

Vous pouvez également utiliser cette méthode `__floordiv__()` directement à la place de l'opérateur `//` :
```py
num1 = 12
num2 = 5
num3 = num1 // num2
num4 = num1.__floordiv__(num2)

print("division entière de", num1, "par", num2, "=", num3)
print("utiliser la méthode floordiv nous donne la même valeur de", num4)

"""
Sortie :
division entière de 12 par 5 = 2
utiliser la méthode floordiv nous donne la même valeur de 2
"""
```

## Conclusion

Dans cet article, vous avez appris comment utiliser l'opérateur double barre `//` et comment il fonctionne en coulisses.

De plus, vous avez appris deux alternatives à l'opérateur `//` : `math.floor()` et la méthode `__floordiv__()`.

Ne soyez pas confus quant à celui à utiliser. Les trois façons d'effectuer une division entière fonctionnent de la même manière. Mais je vous conseille d'utiliser l'opérateur double barre `//` car vous avez moins à taper.

Merci d'avoir lu.