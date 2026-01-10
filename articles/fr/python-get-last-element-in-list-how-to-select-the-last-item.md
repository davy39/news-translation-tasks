---
title: 'Python : comment obtenir le dernier élément d''une liste – Comment sélectionner
  le dernier élément'
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-03-15T23:26:34.000Z'
originalURL: https://freecodecamp.org/news/python-get-last-element-in-list-how-to-select-the-last-item
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/list.jpg
tags:
- name: Python
  slug: python
seo_title: 'Python : comment obtenir le dernier élément d''une liste – Comment sélectionner
  le dernier élément'
seo_desc: "Lists are one of the built-in data types in Python. You use them to store\
  \ multiple elements in one variable. \nLists enable us group similar data together,\
  \ and we can also perform operations on these grouped elements at the same time.\n\
  In this article,..."
---

Les listes sont l'un des types de données intégrés en Python. Vous les utilisez pour stocker plusieurs éléments dans une seule variable. 

Les listes nous permettent de regrouper des données similaires, et nous pouvons également effectuer des opérations sur ces éléments groupés en même temps.

Dans cet article, nous allons voir comment obtenir le dernier élément d'une liste. Nous commencerons par expliquer comment accéder généralement aux éléments d'une liste, puis nous examinerons certaines des méthodes permettant de sélectionner le dernier élément.

## Comment accéder aux éléments d'une liste en Python

Dans cette section, nous allons parler de l'accès aux données stockées dans une liste à l'aide de leur index.

Voici à quoi ressemble une liste :

```python
myList = ["yes", "no", "maybe"]
```

Les éléments sont imbriqués dans des crochets où chaque élément est séparé par une virgule. 

Les éléments d'une liste se voient attribuer des numéros d'index lors de la création de la liste ou au fur et à mesure que nous les ajoutons à la liste. Ce numéro d'index commence à zéro. Ainsi, le premier élément d'une liste a un numéro d'index de zéro, le deuxième a un numéro d'index de un, et ainsi de suite. 

Dans la liste que nous avons créée dans l'exemple ci-dessus, l'index de `"yes"` est 0, l'index de `"no"` est 1, et l'index de `"maybe"` est 2. 

```python
myList = ["yes", "no", "maybe"]

print(myList[0]) # yes
print(myList[1]) # no
print(myList[2]) # maybe
```

Voyons maintenant quelques-unes des méthodes que nous pouvons utiliser pour sélectionner le dernier élément de nos listes.

## Comment sélectionner le dernier élément d'une liste à l'aide de l'indexation négative

Tout comme nous l'avons établi dans la section précédente, chaque élément d'une liste possède un numéro d'index qui commence à zéro. 

En Python, nous pouvons également utiliser des valeurs négatives pour ces index. Alors que les index positifs commencent à 0 (qui désigne la position du premier élément), les index négatifs commencent à -1, ce qui désigne la position du dernier élément.

Voici un exemple :

```python
myList = ["yes", "no", "maybe"]

print(myList[-1]) # maybe

```

Nous avons passé -1 comme index et le dernier élément nous a été retourné. Dans le même ordre, si nous utilisons un index de -2, nous obtiendrions `"no"`. Si nous utilisons un index de -3, nous obtiendrions `"yes"`. 

```python
myList = ["yes", "no", "maybe"]

print(myList[-1]) # maybe
print(myList[-2]) # no
print(myList[-3]) # yes

```

L'utilisation d'un index qui n'existe pas entraînera une erreur.

Dans la section suivante, nous verrons comment sélectionner le dernier élément à l'aide de la méthode `pop()`.

## Comment sélectionner le dernier élément d'une liste à l'aide de la méthode `pop()`

Bien que la méthode `pop()` sélectionne le dernier élément, elle le supprimera également – vous ne devriez donc utiliser cette méthode que lorsque vous souhaitez réellement supprimer le dernier élément de la liste.

Voici un exemple :

```python
myList = ["yes", "no", "maybe"]

print(myList.pop()) # maybe

print(myList) # ['yes', 'no']

```

Après avoir utilisé la méthode `pop()`, nous avons obtenu la valeur du dernier élément affichée. Mais ensuite, lorsque nous affichons la liste dans la console, nous pouvons voir que le dernier élément n'existe plus.

## Conclusion

Dans cet article, nous avons appris comment sélectionner le dernier élément d'une liste en utilisant l'indexation négative et comment sélectionner et supprimer le dernier élément avec la méthode `pop()` en Python. 

Bon codage !