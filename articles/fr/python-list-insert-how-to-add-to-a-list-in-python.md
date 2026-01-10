---
title: Python List insert() – Comment ajouter à une liste en Python
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-05-10T21:22:33.000Z'
originalURL: https://freecodecamp.org/news/python-list-insert-how-to-add-to-a-list-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/dictionaary.jpg
tags:
- name: Python
  slug: python
seo_title: Python List insert() – Comment ajouter à une liste en Python
seo_desc: 'The list data type is one of the built-in data structures in Python along
  with sets, tuples, and dictionaries. You use a list to organize, group, and store
  data.

  But each of these data structures has distinctive features that differentiates them
  from...'
---

Le type de données liste est l'une des structures de données intégrées en Python, avec les ensembles, les tuples et les dictionnaires. Vous utilisez une liste pour organiser, regrouper et stocker des données.

Mais chacune de ces structures de données a des caractéristiques distinctives qui les différencient les unes des autres.

Dans cet article, nous verrons comment créer une liste en Python. Nous verrons également comment ajouter des éléments à une liste en utilisant les méthodes `insert()`, `append()` et `extend()`.

## Comment créer une liste en Python

Pour créer une liste en Python, nous utilisons des crochets. Voici un exemple :

```python
myList = ['one', 'two', 'three']

print(myList)

# ['one', 'two', 'three']
```

Dans le code ci-dessus, nous avons créé une liste appelée `myList` avec trois éléments – "one", "two" et "three". Comme vous pouvez le voir ci-dessus, les éléments sont entre crochets.

## Comment ajouter un élément à une liste en Python ?

Il existe trois méthodes que nous pouvons utiliser pour ajouter un élément à une liste en Python. Ce sont : `insert()`, `append()` et `extend()`. Nous allons les décomposer en sous-sections distinctes.

### Comment ajouter un élément à une liste en utilisant la méthode `insert()`

Vous pouvez utiliser la méthode `insert()` pour insérer un élément à une liste à un index spécifié. Chaque élément d'une liste a un index. Le premier élément a un index de zéro (0), le deuxième a un index de un (1), et ainsi de suite.

Voici un exemple utilisant la méthode `insert()` :

```python
myList = ['one', 'two', 'three']

myList.insert(0, 'zero')

print(myList)

# ['zero', 'one', 'two', 'three']
```

Dans l'exemple ci-dessus, nous avons créé une liste avec trois éléments : `['one', 'two', 'three']`.

Nous avons ensuite utilisé la méthode `insert()` pour insérer un nouvel élément – "zero" à l'index 0 (le premier index) : `myList.insert(0, 'zero')`.

La méthode `insert()` prend deux paramètres – l'index du nouvel élément à insérer et la valeur de l'élément.

### Comment ajouter un élément à une liste en utilisant la méthode `append()`

Contrairement à la méthode `insert()` qui nous permet de spécifier où insérer un élément, la méthode `append()` ajoute l'élément à la fin de la liste. La valeur du nouvel élément est passée en tant que paramètre dans la méthode `append()`.

Voici un exemple :

```python
myList = ['one', 'two', 'three']

myList.append('four')

print(myList)

# ['one', 'two', 'three', 'four']
```

Le nouvel élément a été passé en tant que paramètre dans le code ci-dessus : `myList.append('four')`.

Lorsqu'il est imprimé dans la console, nous avons l'élément au dernier index de la liste.

### Comment ajouter un élément à une liste en utilisant la méthode `extend()`

Vous pouvez utiliser la méthode `extend()` pour ajouter une collection de données à une liste. J'utilise ici le terme "collection de données" car nous pouvons également ajouter des ensembles, des tuples, etc., à une liste.

Voyons quelques exemples.

#### Comment ajouter une liste à une liste en utilisant la méthode `extend()`

```python
myList1 = ['one', 'two', 'three']
myList2 = ['four', 'five', 'six']
```

Dans le code ci-dessus, nous avons créé deux listes – `myList1` et `myList2`. Ensuite, nous allons ajouter les éléments de la deuxième liste à la première.

Voici comment :

```python
myList1.extend(myList2)
```

Ainsi, lorsque nous imprimons `myList1`, nous obtenons ceci : `['one', 'two', 'three', 'four', 'five', 'six']`.

Voici tout le code ensemble :

```python
myList1 = ['one', 'two', 'three']
myList2 = ['four', 'five', 'six']

myList1.extend(myList2)

print(myList1)
# ['one', 'two', 'three', 'four', 'five', 'six']
```

#### Comment ajouter un tuple à une liste en utilisant la méthode `extend()`

Le processus ici est le même que dans le dernier exemple, sauf que nous ajoutons un tuple. Vous créez un tuple en utilisant des parenthèses.

C'est-à-dire :

```
myTuple = ('Hello', 'Hi')
```

Ajoutons un tuple à une liste en utilisant la méthode `extend()`.

```python
myList1 = ['one', 'two', 'three']
myList2 = ('four', 'five', 'six')

myList1.extend(myList2)

print(myList1)

# ['one', 'two', 'three', 'four', 'five', 'six']
```

Nous obtenons le même résultat que dans la section précédente.

## Conclusion

Dans cet article, nous avons parlé des listes en Python.

Nous avons vu comment créer une liste et les différentes méthodes pour ajouter des éléments à une liste.

Nous avons ajouté des éléments à notre liste en utilisant les méthodes `insert()`, `append()` et `extend()`.

La méthode `insert()` insère un nouvel élément à un index spécifié, la méthode `append()` ajoute un nouvel élément au dernier index d'une liste, tandis que la méthode `extend()` ajoute une nouvelle collection de données à une liste.

Bon codage !