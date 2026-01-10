---
title: Python Set – Comment créer un Set en Python
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2022-06-09T15:52:07.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-set-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/Copy-of-read-write-files-python.png
tags:
- name: Python
  slug: python
seo_title: Python Set – Comment créer un Set en Python
seo_desc: "Sets are defined as a collection of objects. They are an important concept\
  \ in math and programming. \nProgramming languages provide different ways to group\
  \ objects. Lists, dictionaries, and arrays are some examples of grouping objects.\
  \ \nPython has its..."
---

Les ensembles sont définis comme une collection d'objets. Ils sont un concept important en mathématiques et en programmation. 

Les langages de programmation fournissent différentes façons de regrouper des objets. Les listes, les dictionnaires et les tableaux sont quelques exemples de regroupement d'objets. 

Python a ses propres méthodes pour créer une collection d'objets. En Python, la création d'ensembles est l'une des façons dont nous pouvons regrouper des éléments ensemble.

Dans ce tutoriel, nous apprendrons les différentes méthodes pour créer des ensembles en Python et découvrirons leurs caractéristiques.

## Caractéristiques d'un Set en Python

Les ensembles présentent les caractéristiques suivantes :

* Les ensembles sont non ordonnés. Cela signifie qu'ils ne préservent pas l'ordre original dans lequel ils ont été créés.

```python
>>> x = {'a','b','c'}
>>> print(x)
>>> x
{'a', 'c', 'b'}

```

* Les éléments d'un ensemble doivent être uniques, car les doublons ne sont pas autorisés. Dans le cas où une valeur en double est ajoutée, elle ne sera affichée qu'une seule fois.

```python
>>> x = {'a','b','c','c'}
>>> print(x)
{'a', 'c', 'b'}
>>>

```

* Les éléments d'un ensemble doivent être d'un type immutable. Mais l'ensemble lui-même peut être modifié par des opérations comme l'union, l'intersection, etc.

## Comment définir un Set en Python

Il existe deux méthodes principales pour créer des ensembles. L'une consiste à utiliser la fonction `set` et l'autre à utiliser des accolades et à ajouter des objets individuellement.

Tout d'abord, vous pouvez passer un itérable dans la fonction intégrée `set`.

_Syntaxe :_

```python
sample_set = set(<iterable>)
```

Ici, `<iterable>` peut être n'importe quel objet itérable tel qu'une liste, une chaîne ou un tuple.

**Passer une `liste` comme itérable :**

```python
>>> sample_set = set(['100', 'Days', 'Of', 'Code'])
>>> print(sample_set)
{'Of', '100', 'Days', 'Code'}
>>>
```

**Passer un `tuple` comme itérable :**

```python
>>> sample_set = set(('Tuple', 'as', 'an', 'iterable'))
>>> print(sample_set)
{'as', 'iterable', 'an', 'Tuple'}
```

**Passer une `chaîne` comme itérable :**

```python
>>> s = 'Alpha'
>>> set(s)
{'p', 'l', 'a', 'h', 'A'}
```

Vous pouvez également définir un ensemble vide. Vous pouvez définir un ensemble vide comme ceci :

```python
>>> s = set()
>>> type(s)
<class 'set'>
```

Vous pouvez également définir un ensemble en plaçant individuellement des objets dans des accolades.

```python
>>> s = {'I', 'Like', 'Python'}
>>> type(s)
<class 'set'>
```

Un point intéressant concernant les ensembles est que les éléments peuvent être de différents types de données :

```python
>>> s = {1947, 'cat', 1.179, None, 'w'}
>>> print(s)
{1.179, 'w', 1947, 'cat', None}
>>>

```

Mais rappelez-vous, les éléments de l'ensemble doivent être immutables. Comme les tuples sont immutables, nous pouvons les inclure dans les ensembles :

```python
>>> s = {42, 'foo', ('T','U','P','L','E'), 3.14159, None}
>>> type(s)
<class 'set'>
>>> print(s)
{3.14159, ('T', 'U', 'P', 'L', 'E'), 42, 'foo', None}

```

**Quelques exceptions :**

Mais nous ne pouvons pas inclure de listes et de dictionnaires dans les ensembles car ils sont mutables.

```python
>>> a = ['This', 'is', 'a', 'list']
>>> {a}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'

```

```python
>>> dictionary = {'month': 1, 'day': 12}
>>> {dictionary}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'dict'

```

## Comment déterminer la taille d'un Set en Python

Nous pouvons vérifier la longueur d'un ensemble en utilisant `len()`.

```python
>>> sample_set = set(['100', 'Days', 'Of', 'Code'])
>>> len(sample_set)
4
```

## Comment déterminer l'appartenance à un Set

Nous pouvons confirmer l'appartenance d'un élément en utilisant les opérateurs `in` et `not in`.

```python
>>> sample_set = set(['100', 'Days', 'Of', 'Code'])
>>> '100' in sample_set
True
>>> '100' not in sample_set
False
>>> 'red' in sample_set
False
```

# Conclusion

Dans ce tutoriel, nous avons appris les différentes méthodes pour créer des ensembles en Python. J'espère que vous êtes maintenant à l'aise avec la création d'ensembles.

J'espère que vous avez trouvé ce tutoriel utile. Merci d'avoir lu jusqu'à la fin.

Quelle est la chose préférée que vous avez apprise dans ce tutoriel ? Faites-le moi savoir sur [Twitter](https://twitter.com/hira_zaira) !

Vous pouvez également lire mes autres articles [ici](https://www.freecodecamp.org/news/author/zaira/).



<sub>Crédits de la bannière : Vecteur de révolution industrielle créé par jcomp - www.freepik.com</sub>