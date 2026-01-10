---
title: 'TypeError: les indices de chaîne doivent être des entiers – Comment corriger
  en Python'
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-07-21T15:18:02.000Z'
originalURL: https://freecodecamp.org/news/typeerror-string-indices-must-be-integers-how-to-fix-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/blake-connally-B3l0g6HLxr8-unsplash.jpg
tags:
- name: error
  slug: error
- name: Python
  slug: python
seo_title: 'TypeError: les indices de chaîne doivent être des entiers – Comment corriger
  en Python'
seo_desc: "In Python, there are certain iterable objects – lists, tuples, and strings\
  \ – whose items or characters can be accessed using their index numbers. \nFor example,\
  \ to access the first character in a string, you'd do something like this:\ngreet\
  \ = \"Hello Wo..."
---

En Python, il existe certains objets itérables – listes, tuples et chaînes – dont les éléments ou caractères peuvent être accessibles en utilisant leurs numéros d'index. 

Par exemple, pour accéder au premier caractère d'une chaîne, vous feriez quelque chose comme ceci :

```python
salutation = "Bonjour le monde !"

print(salutation[0])
# B
```

Pour accéder à la valeur du premier caractère dans la chaîne `salutation` ci-dessus, nous avons utilisé son numéro d'index : `salutation[0]`.

Mais il existe des cas où vous obtiendrez une erreur indiquant « TypeError: string indices must be integers » lorsque vous essayez d'accéder à un caractère dans une chaîne. 

Dans cet article, vous verrez pourquoi cette erreur se produit et comment la corriger.

## Qu'est-ce qui provoque « TypeError: string indices must be integers » en Python ?

Il y a deux raisons courantes pour lesquelles l'erreur « TypeError: string indices must be integers » peut être levée. 

Nous allons parler de ces raisons et de leurs solutions dans deux sous-sections différentes.

### Comment corriger l'erreur `TypeError: string indices must be integers` dans les chaînes en Python

Comme nous l'avons vu dans la section précédente, pour accéder à un caractère dans une chaîne, vous utilisez l'index du caractère. 

Nous obtenons l'erreur « TypeError: string indices must be integers » lorsque nous essayons d'accéder à un caractère en utilisant sa valeur de chaîne plutôt que le numéro d'index. 

Voici un exemple pour vous aider à comprendre :

```python
salutation = "Bonjour le monde !"

print(salutation["B"])
# TypeError: string indices must be integers
```

Comme vous pouvez le voir dans le code ci-dessus, nous avons obtenu une erreur indiquant `TypeError: string indices must be integers`. 

Cela s'est produit parce que nous avons essayé d'accéder à `B` en utilisant sa valeur ("B") au lieu de son numéro d'index. 

C'est-à-dire, `salutation["B"]` au lieu de `salutation[0]`. C'est exactement comment le corriger.

La solution à ce problème est assez simple :

* N'utilisez jamais de chaînes pour accéder aux éléments/caractères lorsque vous travaillez avec des objets itérables qui nécessitent l'utilisation de numéros d'index (entiers) lors de l'accès aux éléments/caractères.

### Comment corriger l'erreur `TypeError: string indices must be integers` lors du découpage d'une chaîne en Python

Lorsque vous découpez une chaîne en Python, une plage de caractères de la chaîne est retournée en fonction des paramètres donnés (paramètres `start` et `end`). 

Voici un exemple :

```python
salutation = "Bonjour le monde !"

print(salutation[0:6])
# Bonjour
```

Dans le code ci-dessus, nous avons fourni deux paramètres – 0 et 6. Cela retourne tous les caractères entre l'index 0 et l'index 6. 

Nous obtenons l'erreur « TypeError: string indices must be integers » lorsque nous utilisons incorrectement la syntaxe de découpage. 

Voici un exemple pour démontrer cela :

```python
salutation = "Bonjour le monde !"

print(salutation[0,6])
# TypeError: string indices must be integers
```

L'erreur dans le code est très facile à manquer car nous avons utilisé des entiers – mais nous obtenons toujours une erreur. Dans des cas comme celui-ci, le message d'erreur peut sembler trompeur.

Nous obtenons cette erreur parce que nous avons utilisé la mauvaise syntaxe. Dans notre exemple, nous avons utilisé une virgule pour séparer les paramètres `start` et `end` : `[0,6]`. C'est pourquoi nous avons obtenu une erreur.

Pour corriger cela, vous pouvez changer la virgule en deux-points.

Lorsque vous découpez des chaînes en Python, vous devez séparer les paramètres `start` et `end` en utilisant un deux-points – `[0:6]`.

## Résumé

Dans cet article, nous avons parlé de l'erreur « TypeError: string indices must be integers » en Python. 

Cette erreur se produit lorsque vous travaillez avec des chaînes Python pour deux raisons principales – utiliser une chaîne au lieu d'un numéro d'index (entier) lors de l'accès à un caractère dans une chaîne, et utiliser la mauvaise syntaxe lors du découpage de chaînes en Python. 

Nous avons vu des exemples qui ont provoqué cette erreur dans deux sous-sections et appris comment les corriger.

Bon codage !