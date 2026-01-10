---
title: Opérateurs de base en Python avec des exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/basic-operators-in-python-with-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d03740569d1a4ca356e.jpg
tags:
- name: Python
  slug: python
- name: toothbrush
  slug: toothbrush
seo_title: Opérateurs de base en Python avec des exemples
seo_desc: 'Operators are symbols which tells the interpreter to do a specific operation
  such as arithmetic, comparison, logical, and so on.

  The different types of operators in Python are listed below:


  Arithmetic Operators

  Relational Operators

  Bitwise Operators...'
---

Les opérateurs sont des symboles qui indiquent à l'interpréteur d'effectuer une opération spécifique telle que l'arithmétique, la comparaison, la logique, et ainsi de suite.

Les différents types d'opérateurs en Python sont listés ci-dessous :

1. Opérateurs arithmétiques
2. Opérateurs relationnels
3. Opérateurs bit à bit
4. Opérateurs d'affectation
5. Opérateurs logiques
6. Opérateurs d'appartenance
7. Opérateurs d'identité

## Opérateurs arithmétiques

Un opérateur arithmétique prend deux opérandes en entrée, effectue un calcul et retourne le résultat.

Considérons l'expression, **"a = 2 + 3"**. Ici, `2` et `3` sont les _opérandes_ et `+` est l'_opérateur arithmétique_. Le résultat de l'opération est stocké dans la variable `a`.

| Opérateur | Description | Utilisation |
| :---: | :---: | :---: |
| + | Effectue une addition sur les opérandes | 12 + 3 = 15 |
| - | Effectue une soustraction sur les opérandes | 12 - 3 = 9 |
| * | Effectue une multiplication sur les opérandes | 12 * 3 = 36 |
| / | Effectue une division sur les opérandes | 12 / 3 = 4 |
| % | Effectue un modulo sur les opérandes | 16 % 3 = 1 |
| ** | Effectue une exponentiation sur les opérandes | 12 ** 3 = 1728 |
| // | Effectue une division entière sur les opérandes | 18 // 5 = 3 |

Note : Pour obtenir un résultat de type flottant, l'un des opérandes doit également être de type flottant.

## Opérateurs relationnels

Un opérateur relationnel est utilisé pour comparer deux opérandes afin de décider d'une relation entre eux. Il retourne une valeur booléenne (vrai ou faux) en fonction de la condition.

| Opérateur | Description | Utilisation |
| :---: | :---: | :---: |
| > | Retourne True si l'opérande de gauche est supérieur à l'opérande de droite | 12 > 3 retourne True |
| < | Retourne True si l'opérande de droite est supérieur à l'opérande de gauche | 12 < 3 retourne False |
| == | Retourne True si les deux opérandes sont égaux | 12 == 3 retourne False |
| >= | Retourne True si l'opérande de gauche est supérieur ou égal à l'opérande de droite | 12 >= 3 retourne True |
| <= | Retourne True si l'opérande de droite est supérieur ou égal à l'opérande de gauche | 12 <= 3 retourne False |
| != | Retourne True si les deux opérandes ne sont pas égaux | 12 != 3 retourne True |


## Opérateurs bit à bit

Un opérateur bit à bit effectue des opérations sur les opérandes bit par bit.

Considérons a = 2 (en notation binaire, 10) et b = 3 (en notation binaire, 11) pour les utilisations ci-dessous.

| Opérateur | Description | Utilisation |
| :---: | :---: | :---: |
| & | Effectue une opération ET bit à bit sur les opérandes | a & b = 2 (Binaire : 10 & 11 = 10) |
| \| | Effectue une opération OU bit à bit sur les opérandes | a \| b = 3 (Binaire : 10 \| 11 = 11) |
| ^ | Effectue une opération XOR bit à bit sur les opérandes | a ^ b = 1 (Binaire : 10 ^ 11 = 01) |
| ~ | Effectue une opération NON bit à bit sur l'opérande. Inverse chaque bit de l'opérande | ~a = -3 (Binaire : ~(00000010) = (11111101)) |
| >> | Effectue un décalage binaire à droite. Décale les bits de l'opérande de gauche, à droite par le nombre de bits spécifié comme opérande de droite | a >> b = 0 (Binaire : 00000010 >> 00000011 = 0) |
| << | Effectue un décalage binaire à gauche. Décale les bits de l'opérande de gauche, à gauche par le nombre de bits spécifié comme opérande de droite | a << b = 16 (Binaire : 00000010 << 00000011 = 00001000) |


## Opérateurs d'affectation

Un opérateur d'affectation est utilisé pour assigner des valeurs à une variable. Cela est généralement combiné avec d'autres opérateurs (comme arithmétiques, bit à bit) où l'opération est effectuée sur les opérandes et le résultat est assigné à l'opérande de gauche.

Considérons les exemples suivants,  
**a = 18**. Ici `=` est un opérateur d'affectation, et le résultat est stocké dans la variable a.  
**a += 10**. Ici `+=` est un opérateur d'affectation, et le résultat est stocké dans la variable a. Cela équivaut à a = a + 10.

| Opérateur | Description |
| :---: | :---: |
| = | a = 5. La valeur 5 est assignée à la variable a |
| += | a += 5 est équivalent à a = a + 5 |
| -= | a -= 5 est équivalent à a = a - 5 |
| *= | a *= 3 est équivalent à a = a * 3 |
| /= | a /= 3 est équivalent à a = a / 3 |
| %= | a %= 3 est équivalent à a = a % 3 |
| **= | a **= 3 est équivalent à a = a ** 3 |
| //= | a //= 3 est équivalent à a = a // 3 |
| &= | a &= 3 est équivalent à a = a & 3 |
| \|= | a \|= 3 est équivalent à a = a \| 3 |
| ^= | a ^= 3 est équivalent à a = a ^ 3 |
| >>= | a >>= 3 est équivalent à a = a >> 3 |
| <<= | a <<= 3 est équivalent à a = a << 3 |

## Opérateurs logiques

Un opérateur logique est utilisé pour prendre une décision basée sur plusieurs conditions. Les opérateurs logiques utilisés en Python sont `and`, `or` et `not`.

| Opérateur | Description | Utilisation |
| :---: | :---: | :---: |
| and | Retourne True si les deux opérandes sont True | a and b |
| or | Retourne True si l'un des opérandes est True | a or b |
| not | Retourne True si l'opérande est False | not a |

## Opérateurs d'appartenance

Un opérateur d'appartenance est utilisé pour identifier l'appartenance dans une séquence (listes, chaînes de caractères, tuples).

`in` et `not in` sont des opérateurs d'appartenance. 

`in` retourne True si la valeur spécifiée est trouvée dans la séquence. Retourne False sinon.

`not in` retourne True si la valeur spécifiée n'est pas trouvée dans la séquence. Retourne False sinon.

```py
a = [1,2,3,4,5]
  
#Est-ce que 3 est dans la liste a ?
print(3 in a) # affiche True 
  
#Est-ce que 12 n'est pas dans la liste a ?
print(12 not in a) # affiche True
  
str = "Hello World"
  
#Est-ce que la chaîne str contient World ?
print("World" in str) # affiche True
  
#Est-ce que la chaîne str contient world ? (note : sensible à la casse)
print("world" in str) # affiche False  

print("code" not in str) # affiche True
```

## Opérateurs d'identité

Un opérateur d'identité est utilisé pour vérifier si deux variables partagent le même emplacement mémoire.

`is` et `is not` sont des opérateurs d'identité.

`is` retourne True si les opérandes font référence au même objet. Retourne False sinon.

`is not` retourne True si les opérandes ne font pas référence au même objet. Retourne False sinon.

Veuillez noter que deux valeurs égales n'impliquent pas nécessairement qu'elles sont identiques.

```py
a = 3
b = 3  
c = 4
print(a is b) # affiche True
print(a is not b) # affiche False
print(a is not c) # affiche True

x = 1
y = x
z = y
print(z is 1) # affiche True
print(z is x) # affiche True

str1 = "FreeCodeCamp"
str2 = "FreeCodeCamp"

print(str1 is str2) # affiche True
print("Code" is str2) # affiche False

a = [10,20,30]
b = [10,20,30]

print(a is b) # affiche False (car les listes sont mutables en Python)  
```