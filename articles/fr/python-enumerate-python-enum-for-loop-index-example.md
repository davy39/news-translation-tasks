---
title: Python Enumerate – Exemple de boucle For avec index
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2021-09-22T17:53:56.000Z'
originalURL: https://freecodecamp.org/news/python-enumerate-python-enum-for-loop-index-example
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/tine-ivanic-u2d0BPZFXOY-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: Python Enumerate – Exemple de boucle For avec index
seo_desc: 'When you''re coding in Python, you can use the enumerate() function and
  a for loop  to print out each value of an iterable with a counter.

  In this article, I will show you how to use Python''s enumerate() function with
  a for loop and explain why it is ...'
---

Lorsque vous codez en Python, vous pouvez utiliser la fonction `enumerate()` et une boucle `for` pour afficher chaque valeur d'un itérable avec un compteur.

Dans cet article, je vais vous montrer comment utiliser la fonction `enumerate()` de Python avec une boucle `for` et expliquer pourquoi c'est une meilleure option que de créer votre propre compteur incrémentiel.

Mais d'abord, voyons comment accomplir cela sans la fonction `enumerate()`.

## Comment utiliser une boucle `for` sans la fonction `enumerate()` en Python

En Python, un itérable est un objet sur lequel vous pouvez itérer et retourner une valeur à la fois. Les exemples d'itérables incluent les listes, les tuples et les chaînes de caractères.

Dans cet exemple, nous avons une liste de noms de chiens et une variable appelée `count`.

```py
chiens = ['Harley', 'Phantom', 'Lucky', 'Dingo']
compteur = 1
```

Nous pouvons utiliser une boucle `for` pour parcourir la liste et afficher chaque nom. Nous allons également incrémenter la variable `compteur` de 1 à chaque fois pour suivre le nombre de fois où nous avons itéré sur la liste.

```py
for nom in chiens:
    print(compteur, nom)
    compteur += 1
```

Voici à quoi ressemblerait le résultat affiché à l'écran :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-22-at-3.12.05-AM.png)

Bien que cette approche fonctionne, elle présente une erreur possible.

Une erreur courante serait d'oublier d'incrémenter la variable `compteur`.

Si je modifiais le code, voici ce que serait le nouveau résultat affiché dans la console :

```py
chiens = ['Harley', 'Phantom', 'Lucky', 'Dingo']
compteur = 1
for nom in chiens:
    print(compteur, nom)
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-22-at-3.15.00-AM.png)

Maintenant, la variable `compteur` ne suit plus avec précision le nombre de fois où nous avons parcouru la liste.

Au lieu d'incrémenter une variable `compteur` nous-mêmes, nous pouvons utiliser la fonction `enumerate()` avec la boucle `for`.

## Qu'est-ce que la fonction `enumerate()` en Python ?

La fonction intégrée `enumerate()` de Python prend un itérable et un argument de départ optionnel.

```py
enumerate(iterable, argument de départ optionnel)
```

Si vous omettez l'argument `start` optionnel, le compteur est alors défini à zéro.

La valeur de retour de la fonction `enumerate()` est un objet.

Cette fonction suit les itérations afin que vous n'ayez pas à vous souvenir de mettre à jour la variable `compteur`.

Nous pouvons utiliser la fonction `enumerate()` avec une boucle `for` pour afficher les valeurs d'un itérable avec un compteur.

## Comment utiliser une boucle `for` et la fonction `enumerate()` en Python

Dans cet exemple, nous voulons afficher une liste de directions pour aller de Times Square à la Juilliard School of Music à New York, New York.

Nous devons d'abord créer la liste des `directions` :

```py
directions = [
    'Prendre la direction nord sur Broadway vers W 48th St',
    'Tourner à gauche sur W 58th St',
    'Tourner à droite sur 8th Ave',
    'Tourner à gauche sur Broadway',
    'Tourner à gauche sur Lincoln Center Plaza',
    'Tourner à droite sur Jaffe Dr',
    'Tourner à gauche sur Broadway',
    'Tourner à gauche sur W 65th St'
]
```

Ensuite, dans la boucle `for`, nous créons les variables de boucle `compteur` et `direction`.

La fonction `enumerate()` prendra la liste `directions` et les arguments `start`. Nous voulons commencer à compter à 1 au lieu de 0 par défaut.

```py
for compteur, direction in enumerate(directions, start=1):
```

À l'intérieur de la boucle, nous allons afficher les variables de boucle `compteur` et `direction`.

```py
print(compteur, direction)
```

Voici à quoi cela ressemble une fois tout assemblé :

```py
directions = [
    'Prendre la direction nord sur Broadway vers W 48th St',
    'Tourner à gauche sur W 58th St',
    'Tourner à droite sur 8th Ave',
    'Tourner à gauche sur Broadway',
    'Tourner à gauche sur Lincoln Center Plaza',
    'Tourner à droite sur Jaffe Dr',
    'Tourner à gauche sur Broadway',
    'Tourner à gauche sur W 65th St'
]

for compteur, direction in enumerate(directions, start=1):
    print(compteur, direction)
```

Voici à quoi ressemblent les résultats dans la console :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-22-at-3.52.27-AM.png)

Comme vous pouvez le voir, la variable `compteur` a été automatiquement mise à jour avec la fonction `enumerate()`.

Cela élimine la possibilité d'erreurs si nous oublions d'incrémenter la variable `compteur`.

## Conclusion

Vous pouvez utiliser la fonction `enumerate()` et une boucle `for` pour afficher chaque valeur d'un itérable avec un compteur.

La fonction `enumerate()` prend un itérable et un argument de départ optionnel.

```py
enumerate(iterable, argument de départ optionnel)
```

Si l'argument `start` optionnel est omis, le compteur est alors défini à zéro.

L'utilisation de la fonction `enumerate()` est une meilleure alternative que de créer votre propre compteur incrémentiel dans une boucle `for`.

La fonction `enumerate()` met automatiquement à jour le compteur, ce qui élimine la possibilité que vous oubliiez d'incrémenter le compteur.

J'espère que vous avez apprécié cet article et bonne chance dans votre apprentissage de Python.