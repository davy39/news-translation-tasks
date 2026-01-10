---
title: Python Not Equal – Opérateur Différent de Tutoriel
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-01-07T18:16:14.000Z'
originalURL: https://freecodecamp.org/news/python-not-equal-how-to-use-the-does-not-equal-operator
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/does-not-equal-python-operator.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: Python
  slug: python
seo_title: Python Not Equal – Opérateur Différent de Tutoriel
seo_desc: "When you're learning the basics of most programming languages, you are\
  \ bound to come across operators. \nIn this tutorial, we will talk about the not\
  \ equal operator in Python and also see a few examples of how it works. \nOperators\
  \ and Operands in Pyth..."
---

Lorsque vous apprenez les bases de la plupart des langages de programmation, vous êtes sûr de rencontrer des opérateurs. 

Dans ce tutoriel, nous allons parler de l'opérateur **différent de** en Python et voir également quelques exemples de son fonctionnement. 

## Opérateurs et Opérandes en Python

Avant de parler de l'opérateur différent de, comprenons ce que sont les opérateurs et les opérandes en général.

Les opérateurs sont des symboles qui désignent un certain type d'action ou de processus. Ils effectuent des opérations spécifiques sur certaines valeurs ou variables. Ces valeurs ou variables sont connues sous le nom d'opérandes de l'opérateur, donc l'opérateur effectue son opération sur elles et retourne une valeur.

Voici quelques exemples d'opérateurs et comment ils interagissent avec les opérandes :

#### Opérateur d'addition (`+`)

```py
a = 10
b = 10

print(a + b)

# retourne 20 
```

L'opérateur ici est le symbole `+` qui ajoute la valeur de `a` et `b` qui sont les opérandes. 

#### Opérateur de multiplication (`*`)

```py
c = 10
d = 10

print(a * b)

# retourne 100
```

Similaire au dernier exemple, `*` est l'opérateur tandis que `c` et `d` sont les opérandes.

#### Opérateur différent de (`!=`)

```py
firstNumber = 10
secondNumber = 20

print(firstNumber != secondNumber)

# retourne True
```

Encore une fois, l'opérateur est le symbole `!=` et les opérandes sont `firstNumber` et `secondNumber`.

Il existe de nombreux autres opérateurs en Python qui sont divisés en groupes, mais dans ce tutoriel, nous allons nous concentrer sur l'opérateur différent de (`!=`).

## Opérateur Différent de en Python

L'opérateur différent de est un opérateur relationnel ou de comparaison qui compare deux valeurs ou plus (opérandes). Il retourne soit vrai soit faux en fonction du résultat de l'opération. 

Si les valeurs comparées sont égales, alors une valeur de `true` est retournée. Si les valeurs comparées ne sont pas égales, alors une valeur de `false` est retournée.

`!=` est le symbole que nous utilisons pour l'opérateur différent de.

Voyons quelques exemples de son fonctionnement.

## Comment comparer des valeurs numériques en utilisant l'opérateur `!=` en Python

Ici, nous allons définir deux variables puis comparer leurs valeurs.

```py
a = 600
b = 300

print(a != b)

# True

```

Comme prévu, l'opération ci-dessus retourne `true` parce que la valeur de `a` n'est pas égale à la valeur de `b`. Si vous trouvez toujours cela difficile à comprendre, alors je vais représenter le code ci-dessus en utilisant l'anglais simple pour réécrire chaque ligne ci-dessous :

```txt
a est égal à 600
b est égal à 300

print(la valeur de a n'est pas égale à la valeur de b)

# True, la valeur de a n'est pas égale à la valeur de b
```

Cela devrait probablement simplifier les choses.

Ensuite, nous allons comparer plus de deux valeurs.

```py
a = 600
b = 300
c = 300

print(a != b & c)

# True
```

Si vous attendiez une valeur de `false`, alors vous essayiez probablement d'additionner certaines des valeurs pendant la comparaison. 

Pour simplifier la compréhension, l'opérateur ne va regarder que les valeurs de chaque opérande puis les comparer toutes sans additionner un opérande à l'autre.

Imaginez `a`, `b` et `c` comme des triplés et chaque visage de bébé est représenté par un nombre. Maintenant, l'opérateur `!=` dit : "J'ai fait mes observations et conclu que les trois bébés ne sont pas identiques facialement" et cela est complètement `True`.

Lorsque tous les opérandes sont les mêmes et que `!=` est utilisé, alors la valeur retournée sera false. C'est-à-dire :

```py
a = 600
b = 600
c = 600

print(a != b & c)

# False
```

Ici, les triplés ont tous le même visage, mais `!=` dit : "Tous les bébés n'ont pas le même visage" et cela est faux parce que leurs visages, représentés par des nombres, sont les mêmes – 600.

## Comment comparer des listes en Python en utilisant l'opérateur `!=`

Dans la section précédente, nous avons comparé les valeurs de nombres. Dans cette section, nous allons comparer des listes. Les listes sont utilisées pour stocker plus d'un élément dans une seule variable. 

```py
a = [2, 3]
b = [2, 3]

print(a != b)

# False
```

Tout comme nous l'avons vu dans la section précédente, la valeur est `False` parce que les deux listes sont les mêmes. Ce serait `True` si les deux opérandes n'étaient pas les mêmes.

Pour mieux comprendre l'idée de `True` ou `False` retourné lors de l'utilisation de l'opérateur `!=`, vous devez toujours avoir à l'esprit que la valeur sera `True` si les opérandes ne sont pas les mêmes et `False` si les opérandes sont les mêmes. 

L'opérateur `!=` peut également être utilisé pour comparer des chaînes de caractères, des dictionnaires, des tuples et des ensembles.

## Comment utiliser une instruction `if` avec l'opérateur `!=` en Python

Dans certains cas, vous pourriez préférer exécuter une certaine commande uniquement après avoir évalué deux variables. Considérez l'exemple ci-dessous :

```py
a = 21
b = 10

if ( a != b ):
   print ("True. a n'est pas égal à b")
else:
   print ("False. a est égal à b")
   
   # True. a n'est pas égal à b
```

L'instruction `if` vérifie si les valeurs des opérandes ne sont pas les mêmes puis imprime un message basé sur la valeur retournée. 

C'est un exemple très basique. En tant que développeur Python, vous vous retrouverez à créer une logique plus complexe (mais pas nécessairement difficile) pour exécuter diverses commandes.

## Conclusion

Cet article a servi d'introduction à l'utilisation de l'opérateur différent de (`!=`) en Python et a mis en évidence quelques exemples pour vous aider à comprendre son application. 

Si vous êtes un débutant intéressé par l'apprentissage de Python, freeCodeCamp propose un certificat [Scientific Computing with Python](https://www.freecodecamp.org/learn/scientific-computing-with-python/) qui est un bon point de départ.

Bon codage !