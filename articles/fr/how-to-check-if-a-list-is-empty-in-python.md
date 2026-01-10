---
title: Équivalent de isEmpty() en Python – Comment vérifier si une liste est vide
  en Python
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2023-04-19T04:52:49.000Z'
originalURL: https://freecodecamp.org/news/how-to-check-if-a-list-is-empty-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/kelly-sikkema--1_RZL8BGBM-unsplash--1-.jpg
tags:
- name: Python
  slug: python
seo_title: Équivalent de isEmpty() en Python – Comment vérifier si une liste est vide
  en Python
seo_desc: "A list is one of the data structures in Python that you can use to store\
  \ a collection of variables. \nIn some cases, you have to iterate through and perform\
  \ an operation on the elements of a list. But you can't loop/iterate through a list\
  \ if it has no..."
---

Une [liste](https://www.freecodecamp.org/news/how-to-make-a-list-in-python-declare-lists-in-python-example/) est l'une des structures de données en Python que vous pouvez utiliser pour stocker une collection de variables. 

Dans certains cas, vous devez itérer et effectuer une opération sur les éléments d'une liste. Mais vous ne pouvez pas parcourir/itérer une liste si elle n'a pas d'éléments. 

Dans cet article, vous apprendrez comment vérifier si une liste est vide en utilisant : 

* L'opérateur `not`. 
* La fonction `len()`. 
* En comparant la liste à une liste vide.

## Comment vérifier si une liste est vide en Python en utilisant l'opérateur `not`

L'opérateur `not` en Python est utilisé pour la négation logique. Voici un exemple :

```python
x = True
y = False

print(not x)  # Sortie : False
print(not y)  # Sortie : True

```

`not` retourne vrai lorsqu'un opérande est faux, et faux si un opérande est vrai. 

Vous pouvez vérifier si une collection est vide en utilisant la logique ci-dessus. Voici comment :

```python
people_list = [] 

if not people_list:
    print("Votre liste est vide")
else:
    print("Votre liste n'est pas vide")
    
# Votre liste est vide
```

Dans le code ci-dessus, nous avons utilisé une instruction `if` et l'opérateur `not` pour vérifier si `people_list` était vide. 

## Comment vérifier si une liste est vide en Python en utilisant la fonction `len()`

Vous pouvez utiliser la fonction `len()` en Python pour retourner le nombre d'éléments dans une structure de données. 

Voici un exemple : 

```python
people_list = ["John", "Jane", "Jade", "Doe"] 

print(len(people_list))
# 4
```

En utilisant la fonction `len()`, nous avons imprimé la longueur de la liste `people_list` qui contenait quatre éléments. 

Vous pouvez également obtenir la longueur d'une liste vide :

```python
people_list = [] 

print(len(people_list))
# 0
```

Maintenant que nous savons que la longueur d'une liste vide est 0, nous l'utilisons pour vérifier si une liste est vide :

```python
people_list = [] 

if len(people_list) == 0:
    print("Votre liste est vide")
else:
    print("Votre liste n'est pas vide")

# Votre liste est vide
```

## Comment vérifier si une liste est vide en Python en la comparant à une liste vide

Une manière intéressante de vérifier si une liste est vide est de la comparer à une autre liste vide. C'est-à-dire :

```python
people_list = [] 

if people_list == []:
    print("Votre liste est vide")
else:
    print("Votre liste n'est pas vide")

# Votre liste est vide
```

Dans l'exemple ci-dessus, nous avons comparé la liste `people_list` à une liste vide : `if people_list == []`

Vous pouvez manipuler le code en ajoutant des éléments à la liste pour voir quelle instruction `if...else` est exécutée. 

## Résumé

Dans cet article, nous avons vu comment vérifier si une liste est vide en Python en utilisant trois méthodes différentes. 

Nous avons vu comment vérifier si une liste est vide en utilisant l'opérateur `not` et la fonction `len()`. 

Nous avons également vu comment vérifier si une liste est vide en la comparant à une liste vide. 

Bon codage !