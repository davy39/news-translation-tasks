---
title: Comment créer une liste en Python – Exemple de déclaration de listes en Python
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-07-06T21:19:53.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-a-list-in-python-declare-lists-in-python-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/kelly-sikkema--1_RZL8BGBM-unsplash--2-.jpg
tags:
- name: Python
  slug: python
seo_title: Comment créer une liste en Python – Exemple de déclaration de listes en
  Python
seo_desc: "You can use some of the inbuilt data structures in Python to organize and\
  \ store a collection of variables. \nSome of these data structures include Lists,\
  \ Sets, Tuples, and Dictionaries. Each of them have their own syntax and features.\
  \ \nIn this article..."
---

Vous pouvez utiliser certaines des structures de données intégrées en Python pour organiser et stocker une collection de variables. 

Certaines de ces structures de données incluent les listes, les ensembles, les tuples et les dictionnaires. Chacune d'entre elles a sa propre syntaxe et ses propres caractéristiques. 

Dans cet article, nous nous concentrerons sur les listes. Vous verrez certaines des caractéristiques des listes en Python, comment les créer et comment ajouter, accéder, modifier et supprimer des éléments dans une liste.

## Caractéristiques d'une liste en Python

Voici quelques caractéristiques d'une liste en Python :

* Les éléments d'une liste peuvent avoir des **doublons**. Cela signifie que vous pouvez ajouter deux éléments ou plus avec le même nom.
* Les éléments d'une liste sont **ordonnés**. Ils restent dans le même ordre que celui dans lequel vous créez et ajoutez des éléments à une liste.  
* Les éléments d'une liste sont **modifiables**. Cela signifie que vous pouvez modifier la valeur d'un élément dans une liste. Vous verrez comment faire cela dans les exemples de cet article.

## Comment créer une liste en Python

Pour créer une liste en Python, nous utilisons des crochets (`[]`). Voici à quoi ressemble une liste :

```txt
NomListe = [ÉlémentListe, ÉlémentListe1, ÉlémentListe2, ÉlémentListe3, ...]
```

Notez que les listes peuvent avoir/stocker différents types de données. Vous pouvez soit stocker un type de données particulier, soit les mélanger. 

Dans la section suivante, vous verrez comment ajouter des éléments à une liste.

## Comment ajouter des éléments à une liste en Python

Avant de commencer à ajouter des éléments à la liste, créons-la. Cela vous aidera à comprendre la syntaxe de la dernière section. 

```python
noms = ["Jane", "John", "Jade", "Joe"]


```

Dans le code ci-dessus, nous avons créé une liste appelée `noms` avec quatre éléments – `Jane`, `John`, `Jade` et `Joe`. 

Nous pouvons utiliser deux méthodes pour ajouter des éléments à une liste – la méthode `append()` et la méthode `insert()`. 

### Comment ajouter des éléments à une liste en Python en utilisant la méthode `append()`

En utilisant la notation par points, nous pouvons attacher la méthode `append()` à une liste pour ajouter un élément à la liste. 

Le nouvel élément à ajouter sera passé en tant que paramètre à la méthode `append()`.

```python
noms = ["Jane", "John", "Jade", "Joe"]
noms.append("Doe")

print(noms)
# ['Jane', 'John', 'Jade', 'Joe', 'Doe']
```

Dans le code ci-dessus, nous avons ajouté "Doe" à la liste en utilisant la méthode `append()` : `noms.append("Doe")`.

### Comment ajouter des éléments à une liste en Python en utilisant la méthode `insert()`

La méthode `append()`, vue dans la dernière section, ajoute un élément au dernier index d'une liste. 

Lors de l'ajout d'éléments à une liste en utilisant la méthode `insert()`, vous spécifiez l'index où il doit être placé. 

Voici un exemple :

```python
noms = ["Jane", "John", "Jade", "Joe"]
noms.insert(2, "Doe")

print(noms)
# ['Jane', 'John', 'Doe', 'Jade', 'Joe']
```

Dans notre exemple, nous avons ajouté "Doe" au deuxième index. Les listes sont indexées à partir de zéro, donc le premier élément est 0, le deuxième élément est 1, le troisième élément est 2, et ainsi de suite. 

## Comment accéder aux éléments d'une liste en Python

Vous pouvez accéder aux éléments d'une liste en utilisant l'index de l'élément. 

```python
noms = ["Jane", "John", "Jade", "Joe"]

print(noms[0])
# Jane
```

Dans l'exemple ci-dessus, nous avons imprimé l'élément avec l'index 0 : `print(noms[0])`. L'élément imprimé était "Jane" car c'est le premier élément de la liste. 

Index 0 = Jane  
Index 1 = John  
Index 2 = Jade  
Index 3 = Joe

En utilisant l'indexation négative, nous pouvons accéder aux éléments en commençant par la fin du tableau. Voici un exemple :

```python
noms = ["Jane", "John", "Jade", "Joe"]

print(noms[-1])
# Joe
```

Index -1 = Joe  
Index -2 = Jade  
Index -3 = John  
Index -4 = Jane

## Comment modifier la valeur des éléments dans une liste Python

Pour modifier la valeur d'un élément dans une liste, vous devez faire référence à l'index de l'élément et lui attribuer une nouvelle valeur. 

Voici un exemple :

```python
noms = ["Jane", "John", "Jade", "Joe"]
noms[0] = "Doe"

print(noms)
# ['Doe', 'John', 'Jade', 'Joe']
```

Dans le code ci-dessus, nous avons modifié la valeur du premier élément de "Jane" à "Doe" en utilisant l'index de l'élément : `noms[0] = "Doe"`.

## Comment supprimer des éléments dans une liste en Python

Nous pouvons utiliser les méthodes suivantes pour supprimer un élément d'une liste :

* La méthode `remove()`.
* La méthode `pop()`. 
* Le mot-clé `del`. 

### Comment supprimer des éléments dans une liste en Python en utilisant la méthode `remove()`

```python
noms = ["Jane", "John", "Jade", "Joe"]

noms.remove("John")

print(noms)
# ['Jane', 'Jade', 'Joe']
```

Comme vous pouvez le voir dans l'exemple ci-dessus, nous avons passé l'élément à supprimer en tant que paramètre dans la méthode `remove()` : `noms.remove("John")`.

### Comment supprimer des éléments dans une liste en Python en utilisant la méthode `pop()`

```python
noms = ["Jane", "John", "Jade", "Joe"]

noms.pop()

print(noms)
# ['Jane', 'John', 'Jade']
```

La méthode `pop()` supprime le dernier élément de la liste. 

Vous pouvez également spécifier un élément particulier à supprimer en utilisant son index. Voici un exemple :

```python
noms = ["Jane", "John", "Jade", "Joe"]

noms.pop(2)

print(noms)
# ['Jane', 'John', 'Joe']
```

### Comment supprimer des éléments dans une liste en Python en utilisant le mot-clé `del`

```python
noms = ["Jane", "John", "Jade", "Joe"]

del noms[1]

print(noms)
# ['Jane', 'Jade', 'Joe']
```

Dans le code ci-dessus, nous avons supprimé le deuxième élément en utilisant le mot-clé `del` en spécifiant l'index de l'élément : `del noms[1]`.

Si vous ne spécifiez aucun index lors de l'utilisation du mot-clé `del`, la liste entière sera supprimée. C'est-à-dire :

```python
noms = ["Jane", "John", "Jade", "Joe"]

del noms

print(noms)
# name 'noms' is not defined
```

Essayer d'accéder à une liste après l'avoir supprimée comme nous l'avons fait ci-dessus lancera une erreur indiquant que la liste n'est pas définie. 

Si vous souhaitez vider une liste et toujours avoir une référence à celle-ci sans obtenir d'erreur, vous pouvez utiliser la méthode `clear()`. Voici un exemple :

```python
noms = ["Jane", "John", "Jade", "Joe"]

noms.clear()

print(noms)
# []
```

La méthode `clear()` vide la liste. Lorsque vous essayez d'accéder à la liste, vous obtenez `[]` car tous les éléments ont été "effacés".

## Résumé

Dans cet article, nous avons parlé des listes en Python. 

Nous avons vu certaines des caractéristiques d'une liste en Python et comment créer une liste.

Nous avons également vu comment ajouter, accéder, modifier et supprimer des éléments dans une liste en Python. 

Bon codage !