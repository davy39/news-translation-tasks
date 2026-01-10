---
title: Python Set – Comment créer des ensembles en Python
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-06-30T22:43:42.000Z'
originalURL: https://freecodecamp.org/news/python-set-how-to-create-sets-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/kelly-sikkema--1_RZL8BGBM-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: Python Set – Comment créer des ensembles en Python
seo_desc: "You can use sets in Python to store a collection of data in a single variable.\
  \ \nEach of the built-in data structures in Python like lists, dictionaries, and\
  \ tuples have their distinguishing features. \nHere are some of the features of\
  \ sets in Python: ..."
---

Vous pouvez utiliser des ensembles en Python pour stocker une collection de données dans une seule variable. 

Chacune des structures de données intégrées en Python comme les listes, les dictionnaires et les tuples ont leurs propres caractéristiques distinctives. 

Voici quelques-unes des caractéristiques des ensembles en Python : 

* Les éléments dupliqués ne sont pas autorisés. Si des éléments apparaissent plusieurs fois, un seul sera reconnu dans l'ensemble.
* Les éléments d'un ensemble sont non ordonnés. L'ordre de l'ensemble change à chaque fois qu'il est utilisé. 
* La valeur des éléments dans un ensemble ne peut pas être modifiée/changée une fois que l'ensemble a été créé. 

Dans cet article, vous apprendrez comment créer des ensembles. Vous apprendrez également comment accéder, ajouter et supprimer des éléments dans un ensemble en Python. 

Nous conclurons en parlant de certains cas d'utilisation des ensembles en programmation Python et en mathématiques.

## Comment créer des ensembles en Python

Nous utilisons des accolades pour stocker les éléments dans un ensemble. Voici à quoi ressemble un ensemble :

```python
nameSet = {"John", "Jane", "Doe"}

print(nameSet)
# {'Jane', 'Doe', 'John'}
```

Dans le code ci-dessus, nous avons créé un ensemble appelé `nameSet`. 

Vous remarquerez que lorsque l'ensemble a été imprimé, les valeurs sont apparues dans un ordre différent. C'est l'une des caractéristiques des ensembles en Python dont j'ai parlé ci-dessus.

Voici un autre exemple avec un élément dupliqué :

```python
nameSet = {"John", "Jane", "Doe", "Jane"}

print(nameSet)
# {'Jane', 'Doe', 'John'}
```

Le duplicata de "Jane" a été ignoré dans l'exemple ci-dessus. Cela est dû au fait que les éléments dupliqués ne sont pas autorisés. 

## Comment accéder aux éléments d'un ensemble en Python

Vous pouvez utiliser une boucle pour accéder et imprimer les éléments d'un ensemble. Vous ne pouvez pas utiliser l'index des éléments pour y accéder puisque l'ordre change toujours – aucun élément ne conserve son index.

Voici un exemple :

```python
nameSet = {"John", "Jane", "Doe"}

for names in nameSet:
    print(names)
    # John
    # Doe
    # Jane
```

Nous utilisons une boucle `for` pour imprimer les éléments de `nameSet`.

Dans la section suivante, vous verrez comment ajouter des éléments à un ensemble. 

## Comment ajouter des éléments à un ensemble en Python

Vous pouvez ajouter un élément à un ensemble en Python en utilisant la méthode `add()` avec le nouvel élément à ajouter passé en tant que paramètre. 

Voici un exemple :

```python
nameSet = {"John", "Jane", "Doe"}

nameSet.add("Ihechikara")

print(nameSet)
# {'John', 'Ihechikara', 'Doe', 'Jane'}
```

Nous avons ajouté un nouvel élément – "Ihechikara" – à l'ensemble : `nameSet.add("Ihechikara")`. 

Vous pouvez également ajouter un élément d'un autre ensemble ou d'autres structures de données (listes, dictionnaires et tuples) à un ensemble en utilisant la méthode `update()`.

Voici un exemple :

```python
nameSet = {"John", "Jane", "Doe"}

nameSet2 = {"Jade", "Jay"}

nameSet.update(nameSet2)

print(nameSet)
# {'Doe', 'Jay', 'Jane', 'Jade', 'John'}
```

Afin d'ajouter les noms de `nameSet2` à `nameSet`, nous avons passé `nameSet2` en tant que paramètre à la méthode `update()` : `nameSet.update(nameSet2)`.

## Comment supprimer des éléments dans un ensemble en Python

Il existe différentes méthodes que vous pouvez utiliser pour supprimer un ou plusieurs éléments dans un ensemble. Examinons-les maintenant.

### Comment supprimer des éléments dans un ensemble en Python en utilisant la méthode `discard()`

Vous pouvez utiliser la méthode `discard()` pour supprimer un élément spécifié. Voici un exemple : 

```python
nameSet = {"John", "Jane", "Doe"}

nameSet.discard("John")

print(nameSet)
# {'Doe', 'Jane'}
```

Dans l'exemple ci-dessus, "John" a été passé en tant que paramètre à la méthode `discard()` afin qu'il soit supprimé de l'ensemble.

### Comment supprimer des éléments dans un ensemble en Python en utilisant la méthode `remove()`

La méthode `remove()` fonctionne de la même manière que la méthode `discard()`. 

```python
nameSet = {"John", "Jane", "Doe"}

nameSet.remove("Jane")

print(nameSet)
# {'John', 'Doe'}
```

### Comment vider un ensemble en Python en utilisant la méthode `clear()`

Pour supprimer tous les éléments d'un ensemble, nous utilisons la méthode `clear()`. 

Voici un exemple :

```python
nameSet = {"John", "Jane", "Doe"}

nameSet.clear()

print(nameSet)
# set()
```

## Quand utiliser les ensembles en Python

Dans cette section, nous discuterons de deux cas d'utilisation importants des ensembles en Python. 

Nous pouvons utiliser des ensembles pour supprimer les éléments dupliqués dans d'autres structures de données. 

Nous pouvons également effectuer certaines opérations mathématiques comme obtenir l'union, l'intersection, la différence et la différence symétrique de deux ensembles ou plus.

### Comment utiliser les ensembles pour supprimer les éléments dupliqués dans d'autres structures de données

Nous pouvons utiliser des ensembles pour nous débarrasser des éléments dupliqués dans d'autres structures de données comme les listes et les tuples.

Cela est utile lorsque vous traitez un très grand ensemble de données qui nécessite uniquement l'unité individuelle des éléments retournés au lieu du nombre d'occurrences des éléments. 

Voici un exemple :

```python
numberList = [2, 2, 4, 8, 9, 10, 8, 2, 5, 7, 3, 4, 7, 9]

numberSet = set(numberList)

print(numberSet)
# {2, 3, 4, 5, 7, 8, 9, 10}
```

Dans le code ci-dessus, nous créons une liste de nombres appelée `numberList` qui avait plusieurs occurrences de certains des nombres : `[2, 2, 4, 8, 9, 10, 8, 2, 5, 7, 3, 4, 7, 9]`.

En utilisant la méthode `set()`, nous avons converti la liste `numberList` en un ensemble : `numberSet = set(numberList)`. 

Lorsque le nouvel ensemble a été imprimé, tous les duplicatas des nombres ont été supprimés – nous n'avons obtenu qu'une seule occurrence de chaque nombre retournée : `{2, 3, 4, 5, 7, 8, 9, 10}`.

### Comment effectuer des opérations mathématiques en utilisant des ensembles en Python

Les ensembles en Python sont similaires aux ensembles en mathématiques, et nous pouvons obtenir divers résultats basés sur la relation qui existe entre les ensembles. 

Dans cette section, vous verrez comment obtenir l'union, l'intersection, la différence et la différence symétrique entre des ensembles en Python.

Vous pouvez effectuer toutes les opérations de cette section en utilisant plus de deux ensembles. Pour garder cela aussi simple que possible, nous utiliserons seulement deux ensembles pour chaque exemple.

#### Comment obtenir l'union des ensembles en Python

L'union de deux ensembles est l'ensemble de tous les éléments individuels qui existent dans les deux ensembles. Dans l'union, les duplicatas sont ignorés.

Voici un exemple :

```python
firstSet = {2, 3, 4, 5}

secondSet = {1, 3, 5, 7}

print(firstSet | secondSet)
# {1, 2, 3, 4, 5, 7}
```

Dans l'exemple ci-dessus, nous avons deux ensembles – `firstSet = {2, 3, 4, 5}` et `secondSet = {1, 3, 5, 7}`. 

En utilisant l'opérateur de barre verticale (`|`), nous avons pu obtenir l'union des deux ensembles : `firstSet | secondSet`.

L'union des ensembles est la suivante : {1, 2, 3, 4, 5, 7}. Vous pouvez voir que les deux ensembles ont été combinés pour former un seul ensemble sans aucun duplicata. 

#### Comment obtenir l'intersection des ensembles en Python

L'intersection de deux ensembles est l'ensemble des éléments qui sont communs aux deux ensembles. Dans notre cas, c'est l'ensemble des éléments qui apparaissent à la fois dans `firstSet` et `secondSet`.

Voici un exemple :

```python
firstSet = {2, 3, 4, 5}

secondSet = {1, 3, 5, 7}

print(firstSet & secondSet)
# {3, 5}
```

Dans cet exemple, nous utilisons l'opérateur `&` pour obtenir l'intersection de `firstSet` et `secondSet` : `firstSet & secondSet`.

Nous avons obtenu {3, 5} retourné car 3 et 5 apparaissent dans les deux ensembles. 

#### Comment obtenir la différence entre les ensembles en Python

La différence entre deux ensembles est l'ensemble de tous les éléments qui existent dans un ensemble mais pas dans l'autre. 

Voici un exemple :

```python
firstSet = {2, 3, 4, 5}

secondSet = {1, 3, 5, 7}

print(firstSet - secondSet)
# {2, 4}
```

Dans l'exemple ci-dessus, nous obtenons un ensemble des éléments qui existent dans `firstSet` mais pas dans `secondSet`. 

Nous avons utilisé l'opérateur `-` pour y parvenir : `firstSet - secondSet`. 

Le résultat de l'opération est 2 et 4. 

#### Comment obtenir la différence symétrique des ensembles en Python

La différence symétrique de deux ensembles est l'ensemble de tous les éléments qui existent dans l'un ou l'autre des deux ensembles mais pas dans les deux. 

Dans la dernière section, nous avons vu le résultat des éléments qui existent dans un seul ensemble mais pas dans l'autre. La différence symétrique est le résultat des éléments qui existent dans chaque ensemble mais pas dans les deux.

```python
firstSet = {2, 3, 4, 5}

secondSet = {1, 3, 5, 7}

print(firstSet ^ secondSet)
# {1, 2, 4, 7}
```

Nous avons utilisé l'opérateur `^` pour obtenir la différence symétrique de deux ensembles : `firstSet ^ secondSet`. 

Le résultat était 1, 2, 4, 7. Chacun de ces éléments n'apparaît pas dans les deux ensembles.

## Résumé

Dans cet article, nous avons parlé des ensembles et de la manière de les créer en Python.

Les ensembles n'autorisent pas les éléments dupliqués, ils sont non ordonnés et les éléments qui y sont stockés ne peuvent pas être modifiés. 

Nous avons également vu comment accéder, ajouter et supprimer des éléments dans les ensembles en utilisant différentes méthodes. 

Enfin, nous avons parlé de quand utiliser les ensembles en Python. Nous avons vu certaines des applications des ensembles en Python et leur utilisation dans les opérations mathématiques.

Bon codage !