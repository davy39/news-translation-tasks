---
title: List Index Out of Range – Message d'erreur Python résolu
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-01-20T16:03:30.000Z'
originalURL: https://freecodecamp.org/news/list-index-out-of-range-python-error-message-solved
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/domenico-loia-hGV2TfOh0ns-unsplash.jpg
tags:
- name: error
  slug: error
- name: Python
  slug: python
seo_title: List Index Out of Range – Message d'erreur Python résolu
seo_desc: 'In this article you''ll see a few of the reasons that cause the list index
  out of range Python error.

  Besides knowing why this error occurs in the first place, you''ll also learn some
  ways to avoid it.

  Let''s get started!

  How to Create a List in Python

  ...'
---

Dans cet article, vous verrez quelques-unes des raisons qui provoquent l'erreur `list index out of range` en Python.

En plus de savoir pourquoi cette erreur se produit en premier lieu, vous apprendrez également quelques moyens de l'éviter.

Commençons !

## Comment créer une liste en Python

Pour créer un objet liste en Python, vous devez :

- Donner un nom à la liste,
- Utiliser l'opérateur d'assignation, `=`,
- et inclure 0 ou plusieurs éléments de liste à l'intérieur de crochets, `[]`. Chaque élément de liste doit être séparé par une virgule.

Par exemple, pour créer une liste de noms, vous feriez ce qui suit :

```python
noms = ["Kelly", "Nelly", "Jimmy", "Lenny"]
```

Le code ci-dessus a créé une liste appelée `noms` qui contient quatre valeurs : `Kelly, Nelly, Jimmy, Lenny`.

### Comment vérifier la longueur d'une liste en Python

Pour vérifier la longueur d'une liste en Python, utilisez la méthode intégrée `len()` de Python.

`len()` retournera un entier, qui sera le nombre d'éléments stockés dans la liste.

```python
noms = ["Kelly", "Nelly", "Jimmy", "Lenny"]

# créer une variable appelée longueur_noms pour stocker la longueur de la liste
longueur_noms = len(noms)

# afficher la valeur de la variable dans la console
print(longueur_noms)

# sortie
# 4
```

Il y a quatre éléments stockés dans la liste, donc la longueur de la liste sera de quatre.

### Comment accéder aux éléments individuels d'une liste en Python

Chaque élément d'une liste a son propre *numéro d'index*.

L'indexation en Python, et dans la plupart des langages de programmation modernes, commence à 0.

Cela signifie que le premier élément d'une liste a un index de 0, le deuxième élément a un index de 1, et ainsi de suite.

Vous pouvez utiliser le numéro d'index pour accéder à l'élément individuel.

Pour accéder à un élément dans une liste en utilisant son numéro d'index, écrivez d'abord le nom de la liste. Ensuite, à l'intérieur de crochets, incluez l'entier qui correspond au numéro d'index de l'élément.

En reprenant l'exemple précédent, voici comment vous accéderiez à chaque élément à l'intérieur de la liste en utilisant son numéro d'index :

```python
noms = ["Kelly", "Nelly", "Jimmy", "Lenny"]

noms[0] # Kelly
noms[1] # Nelly
noms[2] # Jimmy
noms[3] # Lenny
```

Vous pouvez également utiliser l'indexation négative pour accéder aux éléments à l'intérieur des listes en Python.

Pour accéder au **dernier** élément, vous utilisez la valeur d'index -1. Pour accéder à l'avant-dernier élément, vous utilisez la valeur d'index -2.

Voici comment vous accéderiez à chaque élément à l'intérieur d'une liste en utilisant l'indexation négative :

```python
noms = ["Kelly", "Nelly", "Jimmy", "Lenny"]

noms[-4] # Kelly
noms[-3] # Nelly
noms[-2] # Jimmy
noms[-1] # Lenny
```

## Pourquoi l'erreur `IndexError: list index out of range` se produit-elle en Python ?

### Utilisation d'un numéro d'index qui est hors de la plage de la liste

Vous obtiendrez l'erreur `IndexError: list index out of range` lorsque vous essayez d'accéder à un élément en utilisant une valeur qui est hors de la plage d'index de la liste et qui n'existe pas.

Cela est assez courant lorsque vous essayez d'accéder au dernier élément d'une liste, ou au premier si vous utilisez l'indexation négative.

Revenons à la liste que nous avons utilisée jusqu'à présent.

```python
noms = ["Kelly", "Nelly", "Jimmy", "Lenny"]
```

Supposons que je veux accéder au dernier élément, "Lenny", et que j'essaie de le faire en utilisant le code suivant :

```python
print(noms[4])

# sortie

# Traceback (most recent call last):
#   File "/Users/dionysialemonaki/python_articles/demo.py", line 3, in <module>
#     print(noms[4])
# IndexError: list index out of range
```

Généralement, la plage d'index d'une liste est `0 à n-1`, où `n` est le nombre total de valeurs dans la liste.

Le nombre total de valeurs de la liste ci-dessus étant `4`, la plage d'index est `0 à 3`.

Maintenant, essayons d'accéder à un élément en utilisant l'indexation négative.

Supposons que je veux accéder au premier élément de la liste, "Kelly", en utilisant l'indexation négative.

```python
noms = ["Kelly", "Nelly", "Jimmy", "Lenny"]

print(noms[-5])

# sortie

# Traceback (most recent call last):
#   File "/Users/dionysialemonaki/python_articles/demo.py", line 3, in <module>
#     print(noms[-5])
# IndexError: list index out of range
```

Lorsque vous utilisez l'indexation négative, la plage d'index d'une liste est `-1 à -n`, où `-n` est le nombre total d'éléments contenus dans la liste.

Le nombre total d'éléments dans la liste étant `4`, la plage d'index est `-1 à -4`.

### Utilisation de la mauvaise valeur dans la fonction `range()` dans une boucle `for` Python

Vous obtiendrez l'erreur `IndexError: list index out of range` lorsque vous itérez à travers une liste et essayez d'accéder à un élément qui n'existe pas.

Un cas courant où cela peut se produire est lorsque vous utilisez le mauvais entier dans la fonction `range()` de Python.

La fonction `range()` prend généralement un nombre entier, qui indique où le comptage s'arrêtera.

Par exemple, `range(5)` indique que le comptage commencera à `0` et se terminera à `4`.

Ainsi, par défaut, le comptage commence à la position `0`, est incrémenté de `1` chaque fois, et le nombre est jusqu'à — mais non inclus — la position où le comptage s'arrêtera.

Prenons l'exemple suivant :

```python
noms = ["Kelly", "Nelly", "Jimmy", "Lenny"]

for nom in range(5):
    print(noms[nom])

# sortie

# Kelly
# Nelly
# Jimmy
# Lenny
# Traceback (most recent call last):
#   File "/Users/dionysialemonaki/python_articles/demo.py", line 7, in <module>
#     print(noms[nom])
# IndexError: list index out of range
```

Ici, la liste `noms` a quatre valeurs.

Je voulais parcourir la liste et imprimer chaque valeur.

Lorsque j'ai utilisé `range(5)`, j'ai dit à l'interpréteur Python d'imprimer les valeurs qui sont aux positions `0 à 4`.

Cependant, il n'y a pas d'élément à la position 4.

Vous pouvez voir cela en imprimant d'abord le numéro de la position et *ensuite* la valeur à cette position.

```python
# 0
# Kelly
# 1
# Nelly
# 2
# Jimmy
# 3
# Lenny
# 4
# Traceback (most recent call last):
#   File "/Users/dionysialemonaki/python_articles/demo.py", line 8, in <module>
#     print(noms[nom])
# IndexError: list index out of range
```

Vous voyez qu'à la position `0` se trouve "Kelly", à la position `1` se trouve "Nelly", à la position `2` se trouve "Jimmy" et à la position `3` se trouve "Lenny".

Lorsque cela arrive à la position quatre, qui a été spécifiée avec `range(5)` qui indique les positions de `0 à 4`, il n'y a rien à imprimer et donc l'interpréteur génère une erreur.

Une façon de corriger cela est de diminuer l'entier dans `range()` :

```python
noms = ["Kelly", "Nelly", "Jimmy", "Lenny"]

for nom in range(4):
    print(nom)
    print(noms[nom])

# sortie

# 0
# Kelly
# 1
# Nelly
# 2
# Jimmy
# 3
# Lenny
```

Une autre façon de corriger cela lors de l'utilisation d'une boucle `for` est de passer la longueur de la liste comme argument à la fonction `range()`. Vous faites cela en utilisant la fonction intégrée `len()` de Python, comme montré dans une section précédente :

```python
noms = ["Kelly", "Nelly", "Jimmy", "Lenny"]

for nom in range(len(noms)):
    print(noms[nom])

# sortie

# Kelly
# Nelly
# Jimmy
# Lenny
```

Lorsque vous passez `len()` comme argument à `range()`, assurez-vous de **ne pas** faire l'erreur suivante :

```python
noms = ["Kelly", "Nelly", "Jimmy", "Lenny"]

for nom in range(len(noms) + 1):
    print(noms[nom])
```

Après avoir exécuté le code, vous obtiendrez à nouveau une erreur `IndexError: list index out of range` :

```python
# Kelly
# Nelly
# Jimmy
# Lenny
# Traceback (most recent call last):
#   File "/Users/dionysialemonaki/python_articles/demo.py", line 4, in <module>
#     print(noms[nom])
# IndexError: list index out of range
```

## Conclusion

Espérons que cet article vous a donné un aperçu de pourquoi l'erreur `IndexError: list index out of range` se produit et quelques moyens de l'éviter.

Si vous voulez en savoir plus sur Python, consultez la [Certification Python](https://www.freecodecamp.org/learn/scientific-computing-with-python/) de freeCodeCamp. Vous commencerez à apprendre de manière interactive et adaptée aux débutants. Vous construirez également cinq projets à la fin pour mettre en pratique et renforcer ce que vous avez appris.

Merci d'avoir lu et bon codage !