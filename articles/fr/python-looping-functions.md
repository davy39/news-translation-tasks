---
title: Comment utiliser les fonctions de boucle intégrées en Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-11-01T18:34:42.000Z'
originalURL: https://freecodecamp.org/news/python-looping-functions
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/python-looping-techniques.png
tags:
- name: Loops
  slug: loops
- name: Python
  slug: python
seo_title: Comment utiliser les fonctions de boucle intégrées en Python
seo_desc: "By Shweta Goyal\nWhen you're looping through a sequence in Python like\
  \ a list, tuple, string, or dictionary, do you ever feel like your code is messy\
  \ or you want to remove some variables from it? \nFortunately, Python has some useful\
  \ inbuilt functions ..."
---

Par Shweta Goyal

Lorsque vous parcourez une séquence en Python comme une liste, un tuple, une chaîne ou un dictionnaire, avez-vous déjà l'impression que votre code est désordonné ou souhaitez-vous supprimer certaines variables ?

Heureusement, Python dispose de certaines fonctions `intégrées` utiles qui rendent votre code plus concis et plus lisible.

Dans ce tutoriel, nous allons apprendre diverses fonctions `intégrées` avec des exemples simples pour comprendre comment elles fonctionnent.

## Comment parcourir une séquence avec la fonction enumerate() en Python

La fonction `enumerate()` de Python parcourt une séquence (liste, tuple, chaîne ou dictionnaire) tout en gardant une trace de la valeur d'index dans une variable séparée.

Voyons la syntaxe :

```
enumerate(iterable, start)
```

Elle se compose de deux arguments :

* **iterable** – Un objet itérable ou une séquence, c'est-à-dire un objet qui peut être parcouru.
* **start** – Valeur d'index ou valeur de départ du compte. Par défaut, la valeur commence à 0.

Voici le résultat que vous obtenez :

```
Output
[(0, item_1), (1, item_1), (2, item_2), . . ., (n, item_n)]
```

Comme vous pouvez le voir, nous obtenons les éléments de l'itérable ainsi que leurs indices respectifs.

Prenons un exemple sans index :

```
colour = ["Black", "Purple", "Brown", "Yellow", "Blue"]
list(enumerate(colour))
```

```
Output:
[(0, 'Black'), (1, 'Purple'), (2, 'Brown'), (3, 'Yellow'), (4, 'Blue')]
```

Comme vous pouvez le voir, l'index commence à 0. Nous n'avons pas utilisé le deuxième argument. Par défaut, la valeur de l'index commence à 0.

Prenons un autre exemple avec un index :

```
colour = ["Black", "Purple", "Brown", "Yellow", "Blue"]
list(enumerate(colour, 10))
```

```
Output:
[(10, 'Black'), (11, 'Purple'), (12, 'Brown'), (13, 'Yellow'), (14, 'Blue')]
```

Ainsi, ici notre index commence à 10 car nous avons défini l'argument start à 10, ce qui commence le compte à partir de 10.

Vous devez spécifier une liste ou un tuple pour obtenir le résultat, sinon il ne vous donnera que ce résultat :

```
colour = ["Black", "Purple", "Brown", "Yellow", "Blue"]
enumerate(colour)
```

```
Output:
<enumerate object at 0x7f6a97ad7c40>
```

Prenons un exemple avec un dictionnaire :

```
colour = {"Black": 0, 
          "Purple": 2, 
          "Brown": 4, 
          "Yellow": 9, 
          "Blue": 1}
list(enumerate(colour))
```

```
Output:
[(0, 'Black'), (1, 'Purple'), (2, 'Brown'), (3, 'Yellow'), (4, 'Blue')]
```

Lorsque nous itérons sur un dictionnaire, nous obtenons uniquement les clés et non les valeurs du dictionnaire.

Pour parcourir un dictionnaire et obtenir les valeurs, Python dispose de deux fonctions intégrées :

* `items()` – Cette fonction nous aide à obtenir des paires clé-valeur à partir du dictionnaire.
* `values()` – Cette fonction nous aide à obtenir uniquement les valeurs du dictionnaire sans les clés.

Voyons des exemples de ces fonctions :

```
colour = {"Black": 0, 
          "Purple": 2, 
          "Brown": 4, 
          "Yellow": 9, 
          "Blue": 1}
list(enumerate(colour.items()))
```

```
Output:
[(0, ('Black', 0)), (1, ('Purple', 2)), (2, ('Brown', 4)), (3, ('Yellow', 9)), (4, ('Blue', 1))]
```

Vous pouvez également l'utiliser avec une boucle for comme ceci :

```
colour = {"Black": 0, 
          "Purple": 2, 
          "Brown": 4, 
          "Yellow": 9, 
          "Blue": 1}
for ind, (keys, value) in enumerate(colour.items()):
	print(ind, keys, value)
```

```
Output:
0 Black 0
1 Purple 2
2 Brown 4
3 Yellow 9
4 Blue 1
```

Dans cet exemple, nous obtenons les paires clé-valeur. Maintenant, nous allons utiliser une autre fonction,

```
colour = {"Black": 0, 
          "Purple": 2, 
          "Brown": 4, 
          "Yellow": 9, 
          "Blue": 1}
list(enumerate(colour.values()))
```

```
Output:
[(0, 0), (1, 2), (2, 4), (3, 9), (4, 1)]
```

Avec une boucle for :

```
colour = {"Black": 0, 
          "Purple": 2, 
          "Brown": 4, 
          "Yellow": 9, 
          "Blue": 1}
for ind, value in enumerate(colour.values()):
	print(ind, value)
```

```
Output:
0 0
1 2
2 4
3 9
4 1
```

Ici, vous n'obtenez que les valeurs, pas les clés lors de l'itération à travers le dictionnaire.

## Comment parcourir une séquence avec la fonction zip() en Python

La fonction `zip()` prend plus d'un itérable avec les mêmes valeurs d'index et les combine pour retourner un itérateur. Un itérateur peut être un tuple, une liste ou un dictionnaire.

Voyons la syntaxe :

```
zip(*iterables)
```

ou

```
zip(iterator1, iterator2, ... etc)
```

Arguments de la fonction zip() :

* **Iterables** peuvent être des listes, des tuples, des chaînes, des ensembles ou des dictionnaires.

Prenons un exemple :

```
color = ["Blue", "Orange", "Brown", "Red"]
code = [20, 10, 56, 84]
list(zip(color, code))
```

```
Output:
[('Blue', 20), ('Orange', 10), ('Brown', 56), ('Red', 84)]
```

Ici, deux listes sont combinées ou zippées ensemble et nous obtenons un itérateur.

Si les longueurs des itérables sont différentes, l'itérateur cesse de produire une sortie lorsque l'itérable le plus court est épuisé.

Prenons un exemple :

```
color = ["Blue", "Orange", "Brown"]
code = [20, 10, 56, 84]
list(zip(color, code))
```

```
Output:
[('Blue', 20), ('Orange', 10), ('Brown', 56)]
```

Ici, la longueur la plus courte est celle de color et nous obtenons dans la sortie jusqu'à 3 couleurs et codes. Ainsi, le 4ème code est rejeté.

Dans **Python 3.10**, il y a un nouveau paramètre `strict` qui vérifie la longueur des éléments. Il nous donnera une erreur si la longueur des éléments ne correspond pas. Prenons un exemple :

```
color = ("Blue", "Orange", "Brown", "Purple")
code = (20, 10, 56)
for col, cod in zip(color, code, strict=True):
    print(col, cod)
```

```
Output:
Blue 20
Orange 10
Brown 56
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    for col, cod in zip(color, code, strict=True):
ValueError: zip() argument 2 is shorter than argument 1
```

Vous n'avez pas besoin de prendre deux itérateurs, vous pouvez prendre n'importe quel nombre d'itérateurs. Prenons un exemple avec trois itérateurs :

```
Abbreviation = ['Bl', 'Or', 'Br', 'Gn']
Color = ['Blue', 'Orange', 'Brown', 'Green']
Code = [20, 10, 56, 88]
for ab, col, cod in zip(Abbreviation, Color, Code):
	print(ab, col, cod)
```

```
Output:
Bl Blue 20
Or Orange 10
Br Brown 56
Gn Green 88
```

Vous pouvez également créer des dictionnaires en utilisant la fonction `dict`. Prenons un exemple :

```
Color = ['Blue', 'Orange', 'Brown', 'Green']
Code = [20, 10, 56, 88]
dict(zip(Color, Code))
```

```
Output:
{'Blue': 20, 'Orange': 10, 'Brown': 56, 'Green': 88}
```

## Comment parcourir une séquence avec la fonction sorted() en Python

La fonction `sorted()` retourne les éléments dans l'ordre trié à partir d'un objet itérable.

Voyons la syntaxe :

```
sorted(iterable, key=key, reverse=reverse)
```

Elle se compose de trois arguments :

* **iterable** – une séquence qui peut être une liste, un tuple, une chaîne, etc.
* **key** – est facultatif. C'est une fonction que vous pouvez utiliser pour personnaliser l'ordre de tri. L'option par défaut est None.
* **reverse** – est également facultatif. C'est un booléen. Ici, la valeur par défaut est **False** qui est dans l'ordre _ascendant_. **True** sera dans l'ordre _descendant_.

Prenons un exemple :

```
Color = ['Blue', 'Orange', 'Brown', 'Green']
sorted(Color)
```

```
Output:
['Blue', 'Brown', 'Green', 'Orange']
```

Par défaut, votre sortie sera une liste et sera dans l'ordre ascendant. Si c'est une chaîne, elle sera triée alphabétiquement et si ce sont des nombres, elle sera triée numériquement.

La sortie ci-dessus montre une liste triée dans l'ordre ascendant. Si vous la voulez dans l'ordre descendant, vous pouvez utiliser l'argument `reverse`. Prenons un exemple :

```
Color = ('Blue', 'Orange', 'Brown', 'Green')
sorted(Color, reverse=True)
```

```
Output:
['Orange', 'Green', 'Brown', 'Blue']
```

Les valeurs originales restent inchangées car la fonction `sorted()` ne modifie pas les valeurs originales – elle ne produira que la sortie. La sortie sera une liste ordonnée.

La fonction `key` peut être intégrée ou définie par l'utilisateur, que vous pouvez utiliser pour manipuler l'ordre de la sortie.

Prenons un exemple avec une fonction intégrée d'abord :

```
Word = ('TO', 'is', 'apple', 'PEAR', 'LIKE')
sorted(Word, key=str.upper)
```

```
Output:
['apple', 'is', 'LIKE', 'PEAR', 'TO']
```

Par défaut, la sortie sera dans l'ordre ascendant. Vous devez inverser l'argument comme ceci :

```
Word = ('TO', 'is', 'apple', 'PEAR', 'LIKE')
sorted(Word, key=str.upper, reverse=True)
```

```
Output:
['TO', 'PEAR', 'LIKE', 'is', 'apple']
```

Le nombre d'arguments doit être un lors de l'utilisation d'un argument clé. Prenons un exemple avec une fonction définie par l'utilisateur :

```
numb = (22, 10, 5, 34, 29)
sorted(numb, key=lambda x: x%5)
```

```
Output:
[10, 5, 22, 34, 29]
```

J'ai utilisé la fonction lambda pour simplifier, mais vous pouvez utiliser la méthode traditionnelle pour la définition de fonction si vous le souhaitez.

## Comment parcourir une séquence avec la fonction reversed() en Python

La fonction `reversed` retourne les éléments dans l'ordre inverse à partir d'un objet itérable.

Voyons la syntaxe :

```
reversed(iterable)
```

L'argument de la fonction reversed :

* **iterable** – Il s'agit d'une séquence comme une liste, un tuple, un ensemble, etc.

Prenons un exemple :

```
numb = (22, 10, 5, 34, 29)
list(reversed(numb))
```

```
Output:
[29, 34, 5, 10, 22]
```

Vous devez spécifier une liste ou un tuple, sinon il ne vous donnera qu'une adresse comme dans l'exemple ci-dessous :

```
numb = (22, 10, 5, 34, 29)
reversed(numb)
```

```
Output:
<reversed object at 0x000001C1E7D9E110>
```

## Conclusion

Les fonctions intégrées vous aident à écrire vos fonctions Python de manière claire et concise. Elles vous aideront à exécuter votre fonction sans désordre.

Dans ce tutoriel, vous avez appris différentes fonctions intégrées en Python. Vous avez vu divers exemples, et maintenant vous pouvez pratiquer sur votre propre séquence. J'espère que vous trouverez ce tutoriel utile.

Suivez-moi sur [Twitter](https://twitter.com/Shweta_go). Bon codage !