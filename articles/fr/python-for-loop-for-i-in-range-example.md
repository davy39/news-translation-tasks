---
title: Boucle For en Python - Exemple avec For i in Range
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-30T21:31:06.000Z'
originalURL: https://freecodecamp.org/news/python-for-loop-for-i-in-range-example
coverImage: https://cdn-media-2.freecodecamp.org/w1280/606365729618b008528a99ae.jpg
tags:
- name: Loops
  slug: loops
- name: Python
  slug: python
seo_title: Boucle For en Python - Exemple avec For i in Range
seo_desc: 'By Jeremy L Thompson

  Loops are one of the main control structures in any programming language, and Python
  is no different.

  In this article, we will look at a couple of examples using for loops with Python''s
  range() function.

  Here''s an Interactive Scr...'
---

Par Jeremy L Thompson

Les boucles sont l'une des principales structures de contrôle dans tout langage de programmation, et Python ne fait pas exception.

Dans cet article, nous allons examiner quelques exemples utilisant les boucles `for` avec la fonction `range()` de Python.

### Voici un Scrim Interactif d'une Boucle For en Python

<iframe src="https://scrimba.com/scrim/co4e24d97b6f708862420051b?embed=freecodecamp,mini-header,no-sidebar" width="100%" height="420"></iframe>

## Les Boucles For en Python

Les boucles `for` répètent une portion de code pour un ensemble de valeurs. 

Comme discuté dans [la documentation de Python](https://docs.python.org/3/tutorial/controlflow.html#for-statements), les boucles `for` fonctionnent légèrement différemment de ce qu'elles font dans des langages comme JavaScript ou C. 

Une boucle `for` définit la variable d'itération à chaque valeur dans une liste, un tableau ou une chaîne fournie et répète le code dans le corps de la boucle `for` pour chaque valeur de la variable d'itération.

Dans l'exemple ci-dessous, nous utilisons une boucle `for` pour imprimer chaque nombre dans notre tableau.

```python
# Exemple de boucle for
for i in [1, 2, 3, 4]:
    print(i, end=", ") # imprime : 1, 2, 3, 4,
```

Nous pouvons inclure une logique plus complexe dans le corps d'une boucle `for`. Dans cet exemple, nous imprimons le résultat d'un petit calcul basé sur la valeur de notre variable d'itération.

```python
# Exemple plus complexe
for i in [1, 3, 5, 7, 9]:
    x = i**2 - (i-1)*(i+1)
    print(x, end=", ") # imprime 1, 1, 1, 1, 1, 
```

Lorsque les valeurs dans le tableau pour notre boucle `for` sont séquentielles, nous pouvons utiliser la fonction `range()` de Python au lieu d'écrire le contenu de notre tableau.

## La Fonction Range en Python

La fonction `range()` fournit une séquence d'entiers basée sur les arguments de la fonction. Des informations supplémentaires peuvent être trouvées dans [la documentation de Python](https://docs.python.org/3/library/stdtypes.html#range) pour la fonction `range()`.

```python
range(stop)
range(start, stop[, step])

```

L'argument `start` est la première valeur dans la plage. Si `range()` est appelée avec un seul argument, alors Python suppose `start = 0`.

L'argument `stop` est la borne supérieure de la plage. Il est important de réaliser que cette valeur supérieure n'est pas incluse dans la plage.

Dans l'exemple ci-dessous, nous avons une plage commençant à la valeur par défaut de `0` et incluant les entiers inférieurs à `5`.

```python
# Exemple avec un argument
for i in range(5):
    print(i, end=", ") # imprime : 0, 1, 2, 3, 4, 
```

Dans notre prochain exemple, nous définissons `start = -1` et incluons à nouveau les entiers inférieurs à `5`.

```python
# Exemple avec deux arguments
for i in range(-1, 5):
    print(i, end=", ") # imprime : -1, 0, 1, 2, 3, 4, 
```

La valeur optionnelle `step` contrôle l'incrément entre les valeurs dans la plage. Par défaut, `step = 1`.

Dans notre dernier exemple, nous utilisons la plage d'entiers de `-1` à `5` et définissons `step = 2`.

```python
# Exemple avec trois arguments
for i in range(-1, 5, 2):
    print(i, end=", ") # imprime : -1, 1, 3, 
```

## Résumé

Dans cet article, nous avons examiné les boucles `for` en Python et la fonction `range()`.

Les boucles `for` répètent un bloc de code pour toutes les valeurs dans une liste, un tableau, une chaîne ou un `range()`.

Nous pouvons utiliser un `range()` pour simplifier l'écriture d'une boucle `for`. La valeur `stop` du `range()` doit être spécifiée, mais nous pouvons également modifier la valeur de `start` et le `step` entre les entiers dans le `range()`.