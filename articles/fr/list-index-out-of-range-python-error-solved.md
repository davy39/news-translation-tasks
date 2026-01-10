---
title: Index de liste hors limites – Erreur Python [Résolu]
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-08-03T22:13:38.000Z'
originalURL: https://freecodecamp.org/news/list-index-out-of-range-python-error-solved
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/kelly-sikkema--1_RZL8BGBM-unsplash--3-.jpg
tags:
- name: Python
  slug: python
seo_title: Index de liste hors limites – Erreur Python [Résolu]
seo_desc: "In this article, we'll talk about the IndexError: list index out of range\
  \ error in Python. \nIn each section of the article, I'll highlight a possible cause\
  \ for the error and how to fix it.\nYou may get the IndexError: list index out of\
  \ range error for..."
---

Dans cet article, nous allons parler de l'erreur `IndexError: list index out of range` en Python. 

Dans chaque section de l'article, je mettrai en évidence une cause possible de l'erreur et comment la corriger.

Vous pouvez obtenir l'erreur `IndexError: list index out of range` pour les raisons suivantes :

* Essayer d'accéder à un index qui n'existe pas dans une liste. 
* Utiliser des index invalides dans vos boucles.
* Spécifier une plage qui dépasse les index dans une liste lors de l'utilisation de la fonction `range()`. 

Avant de procéder à la correction de l'erreur, discutons de la manière dont l'indexation fonctionne dans les listes Python. Vous pouvez sauter la section suivante si vous savez déjà comment fonctionne l'indexation.

## Comment fonctionne l'indexation dans les listes Python ?

Chaque élément d'une liste Python peut être accessible en utilisant son numéro d'index. Le premier élément d'une liste a un index de zéro. 

Considérons la liste ci-dessous :

```python
languages = ['Python', 'JavaScript', 'Java']

print(languages[1])
# JavaScript
```

Dans l'exemple ci-dessus, nous avons une liste appelée `languages`. La liste contient trois éléments — 'Python', 'JavaScript' et 'Java'. 

Pour accéder au deuxième élément, nous avons utilisé son index : `languages[1]`. Cela a affiché `JavaScript`. 

Certains débutants pourraient mal comprendre cela. Ils pourraient supposer que puisque l'index est 1, il devrait s'agir du premier élément. 

Pour faciliter la compréhension, voici une répartition des éléments de la liste selon leurs index : 

Python (élément 1) => Index 0  
JavaScript (élément 2) => Index 1  
Java (élément 3) => Index 2

Comme vous pouvez le voir ci-dessus, le premier élément a un index de 0 (parce que Python est "zero-indexé"). Pour accéder aux éléments d'une liste, vous utilisez leurs index. 

## Que se passe-t-il si vous essayez d'utiliser un index qui est hors limites dans une liste Python ?

Si vous essayez d'accéder à un élément dans une liste en utilisant un index qui est hors limites, vous obtiendrez l'erreur `IndexError: list index out of range`. 

Voici un exemple :

```python
languages = ['Python', 'JavaScript', 'Java']

print(languages[3])
# IndexError: list index out of range
```

Dans l'exemple ci-dessus, nous avons essayé d'accéder à un quatrième élément en utilisant son index : `languages[3]`. Nous avons obtenu l'erreur `IndexError: list index out of range` parce que la liste n'a pas de quatrième élément — elle n'a que trois éléments. 

La solution facile est de toujours utiliser un index qui existe dans une liste lorsque vous essayez d'accéder aux éléments de la liste. 

## Comment corriger l'erreur `IndexError: list index out of range` dans les boucles Python

Les boucles fonctionnent avec des conditions. Donc, jusqu'à ce qu'une certaine condition soit remplie, elles continueront à s'exécuter. 

Dans l'exemple ci-dessous, nous allons essayer d'imprimer tous les éléments d'une liste en utilisant une boucle `while`. 

```python
languages = ['Python', 'JavaScript', 'Java']

i = 0

while i <= len(languages):
    print(languages[i])
    i += 1

# IndexError: list index out of range
```

Le code ci-dessus retourne l'erreur `IndexError: list index out of range`. Décomposons le code pour comprendre pourquoi cela s'est produit. 

Tout d'abord, nous avons initialisé une variable `i` et lui avons donné une valeur de 0 : `i = 0`. 

Nous avons ensuite donné une condition pour une boucle `while` (c'est ce qui cause l'erreur) : `while i <= len(languages)`.

D'après la condition donnée, nous disons : "cette boucle doit continuer à s'exécuter tant que `i` est **inférieur** ou **égal** à la **longueur** de la liste `language`". 

La fonction `len()` retourne la longueur de la liste. Dans notre cas, 3 sera retourné. Donc la condition sera celle-ci : `while i <= 3`. La boucle s'arrêtera lorsque `i` sera égal à 3.

Faisons semblant d'être le compilateur Python. Voici ce qui se passe lorsque la boucle s'exécute.

Voici la liste : `languages = ['Python', 'JavaScript', 'Java']`. Elle a trois index — 0, 1 et 2.

Lorsque `i` est 0 => Python

Lorsque `i` est 1 => JavaScript

Lorsque `i` est 2 => Java

Lorsque `i` est 3 => Index non trouvé dans la liste. Erreur `IndexError: list index out of range` levée.

Donc l'erreur est levée lorsque `i` est égal à 3 parce qu'il n'y a pas d'élément avec un index de 3 dans la liste.

Pour résoudre ce problème, nous pouvons modifier la condition de la boucle en supprimant le signe égal. Cela arrêtera la boucle une fois qu'elle atteindra le dernier index. 

Voici comment :

```python 
languages = ['Python', 'JavaScript', 'Java']

i = 0

while i < len(languages):
    print(languages[i])
    i += 1
    
    # Python
    # JavaScript
    # Java

```

La condition est maintenant la suivante : `while i < 3`.

La boucle s'arrêtera à 2 parce que la condition ne lui permet pas d'être égale à la valeur retournée par la fonction `len()`. 

## Comment corriger l'erreur `IndexError: list index out of range` lors de l'utilisation de la fonction `range()` en Python

Par défaut, la fonction `range()` retourne une "plage" de nombres spécifiés commençant par zéro. 

Voici un exemple de l'utilisation de la fonction `range()` :

```python
for num in range(5):
  print(num)
    # 0
    # 1
    # 2
    # 3
    # 4
```

Comme vous pouvez le voir dans l'exemple ci-dessus, `range(5)` retourne 0, 1, 2, 3, 4. 

Vous pouvez utiliser la fonction `range()` avec une boucle pour imprimer les éléments d'une liste. 

Le premier exemple montrera un bloc de code qui lève l'erreur `IndexError: list index out of range`. Après avoir indiqué pourquoi l'erreur s'est produite, nous la corrigerons. 

```python
languages = ['Python', 'JavaScript', 'Java']


for language in range(4):
  print(languages[language])
    # Python
    # JavaScript
    # Java
    # Traceback (most recent call last):
    #   File "<string>", line 5, in <module>
    # IndexError: list index out of range
```

L'exemple ci-dessus imprime tous les éléments de la liste ainsi que l'erreur `IndexError: list index out of range`. 

Nous avons obtenu l'erreur parce que `range(4)` retourne 0, 1, 2, 3. Notre liste n'a pas d'index avec la valeur 3. 

Pour corriger cela, vous pouvez modifier le paramètre dans la fonction `range()`. Une meilleure solution est d'utiliser la longueur de la liste comme paramètre de la fonction `range()`. 

C'est-à-dire :

```python
languages = ['Python', 'JavaScript', 'Java']


for language in range(len(languages)):
  print(languages[language])
    # Python
    # JavaScript
    # Java
```

Le code ci-dessus s'exécute sans aucune erreur parce que la fonction `len()` retourne 3. L'utiliser avec `range(3)` retourne 0, 1, 2, ce qui correspond au nombre d'éléments dans une liste.

## Résumé

Dans cet article, nous avons parlé de l'erreur `IndexError: list index out of range` en Python. 

Cette erreur se produit généralement lorsque nous essayons d'accéder à un élément dans une liste en utilisant un index qui n'existe pas dans la liste. 

Nous avons vu quelques exemples qui ont montré comment nous pouvons obtenir l'erreur lorsque nous travaillons avec des boucles, la fonction `len()` et la fonction `range()`. 

Nous avons également vu comment corriger l'erreur `IndexError: list index out of range` pour chaque cas. 

Bon codage !