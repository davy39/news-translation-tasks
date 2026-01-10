---
title: Les ensembles Python – Opérations et exemples
subtitle: ''
author: Jason
co_authors: []
series: null
date: '2021-10-28T18:17:35.000Z'
originalURL: https://freecodecamp.org/news/python-set-operations-explained-with-examples
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/python-sets-article-image.jpeg
tags:
- name: Python
  slug: python
- name: Sets
  slug: sets
seo_title: Les ensembles Python – Opérations et exemples
seo_desc: 'If you''re a beginner to Python, chances are you''ve come across lists.
  But have you heard about sets in Python?

  In this tutorial, we''ll explore what sets are, how to create them, and the different
  operations you can use on them.

  What are sets in Pytho...'
---

Si vous êtes débutant en Python, il est probable que vous ayez [rencontré des listes](https://www.freecodecamp.org/news/lists-in-python-comprehensive-guide/). Mais avez-vous entendu parler des ensembles en Python ?

Dans ce tutoriel, nous allons explorer ce que sont les ensembles, comment les créer et les différentes opérations que vous pouvez utiliser sur eux.

# Qu'est-ce qu'un ensemble en Python ?

En Python, les ensembles sont exactement comme les listes sauf que leurs éléments sont *immuables* (cela signifie que vous ne pouvez pas changer/muter un élément d'un ensemble une fois déclaré). Cependant, vous pouvez ajouter/supprimer des éléments de l'ensemble.

Si cela était confus, laissez-moi essayer de résumer :

> Un ensemble est un groupe mutable et non ordonné d'éléments, où les éléments eux-mêmes sont immuables.

Une autre caractéristique d'un ensemble est qu'il peut inclure des éléments de différents types. Cela signifie que vous pouvez avoir un groupe de nombres, de chaînes de caractères et même de tuples, tous dans le même ensemble !

# Comment créer un ensemble

La manière la plus courante de créer un ensemble en Python est d'utiliser la fonction intégrée `set()`.

```python
>>> premier_ensemble = set(("Connor", 32, (1, 2, 3)))
>>> premier_ensemble
{32, 'Connor', (1, 2, 3)}
>>> 
>>> second_ensemble = set("Connor")
>>> second_ensemble
{'n', 'C', 'r', 'o'}
```

Vous pouvez également créer des ensembles en utilisant la syntaxe avec les accolades `{}` :

```python
>>> troisieme_ensemble = {"Pommes", ("Bananes", "Oranges")}
>>> type(troisieme_ensemble)
<class 'set'>
```

La fonction `set()` prend un *itérable* et produit une liste d'objets qui seront insérés dans l'ensemble. La syntaxe `{}` place les objets eux-mêmes dans l'ensemble.

Comme vous l'avez probablement réalisé, que vous utilisiez la fonction `set()` ou les `{}` pour créer un ensemble, chaque élément doit être un objet immuable. Donc, si vous ajoutez une liste (qui est un objet mutable) à un ensemble, vous rencontrerez une erreur :

```py
>>> ensemble_incorrect = {"Pommes", ["Bananes", "Oranges"]}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
```

# Comment ajouter ou supprimer des éléments dans un ensemble

Nous savons déjà que les ensembles sont mutables. Cela signifie que vous pouvez ajouter/supprimer des éléments dans un ensemble.

Voici un exemple d'ajout d'éléments à un ensemble en utilisant la fonction `update()`.

```py
>>> ensemble_ajout = set((1, 2, 3, 4))
>>> ensemble_ajout
{1, 2, 3, 4}
>>>
>>> ensemble_ajout.update((1,))
>>> ensemble_ajout
{1, 2, 3, 4}
>>> ensemble_ajout.update(("violoncelle", "violin"))
>>> ensemble_ajout
{1, 2, 3, 4, 'violin', 'violoncelle'}
```

Mais remarquez comment rien ne change lorsque nous essayons d'ajouter "violoncelle" à l'ensemble à nouveau :

```py
>>> ensemble_ajout.update(("violoncelle",))
>>> ensemble_ajout
{1, 2, 3, 4, 'violin', 'violoncelle'}
```

Cela est dû au fait que les ensembles en Python *ne peuvent pas* contenir de doublons. Donc, lorsque nous avons essayé d'ajouter `"violoncelle"` à nouveau à l'ensemble, Python a reconnu que nous essayions d'ajouter un élément en double et n'a pas mis à jour l'ensemble. C'est une particularité qui différencie les ensembles des listes.

Voici comment vous supprimeriez des éléments d'un ensemble :

```py
>>> sous_ensemble = ensemble_ajout
>>> sous_ensemble.remove("violin")
>>> sous_ensemble
{1, 2, 3, 4, 'violoncelle'}
```

La fonction `remove(x)` supprime l'élément `x` d'un ensemble. Elle retourne une `KeyError` si `x` ne fait pas partie de l'ensemble :

```py
>>> sous_ensemble.remove("guitar")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'guitar'
```

Il existe quelques autres façons de supprimer un ou des éléments d'un ensemble :

* la méthode `discard(x)` supprime `x` de l'ensemble, mais *ne lève* aucune erreur si `x` n'est pas présent dans l'ensemble.

* la méthode `pop()` supprime et retourne un élément aléatoire de l'ensemble.

* la méthode `clear()` supprime tous les éléments d'un ensemble

Voici quelques exemples pour illustrer :

```py
>>> m_ensemble = set((1, 2, 3, 4))
>>> 
>>> m_ensemble.discard(5) # aucune erreur levée même si '5' n'est pas présent dans l'ensemble
>>>
>>> m_ensemble.pop()
4
>>> m_ensemble
{1, 2, 3}
>>>
>>> m_ensemble.clear()
>>> m_ensemble
set()
```

# Opérations sur les ensembles Python

Si vous vous souvenez de vos bases de mathématiques du secondaire, vous vous souviendrez probablement des opérations sur les ensembles mathématiques comme l'*union*, l'*intersection*, la *différence* et la *différence symétrique*. Eh bien, vous pouvez réaliser la même chose avec les ensembles Python.

## 1. Union d'ensembles

L'union de deux ensembles est l'ensemble de *tous les éléments* des deux ensembles sans doublons. Vous pouvez utiliser la méthode `union()` ou la syntaxe `|` pour trouver l'union d'un ensemble Python.

```py
>>> premier_ensemble = {1, 2, 3}
>>> second_ensemble = {3, 4, 5}
>>> premier_ensemble.union(second_ensemble)
{1, 2, 3, 4, 5}
>>>
>>> premier_ensemble | second_ensemble     # en utilisant l'opérateur `|`
{1, 2, 3, 4, 5}
```

## 2. Intersection d'ensembles

L'intersection de deux ensembles est l'ensemble de *tous les éléments communs* des deux ensembles. Vous pouvez utiliser la méthode `intersection()` ou l'opérateur `&` pour trouver l'intersection d'un ensemble Python.

```py
>>> premier_ensemble = {1, 2, 3, 4, 5, 6}
>>> second_ensemble = {4, 5, 6, 7, 8, 9}
>>> premier_ensemble.intersection(second_ensemble)
{4, 5, 6}
>>>
>>> premier_ensemble & second_ensemble     # en utilisant l'opérateur `&`
{4, 5, 6}
```

## 3. Différence d'ensembles

La différence entre deux ensembles est l'ensemble de tous les éléments du premier ensemble qui *ne sont pas* présents dans le second ensemble. Vous utiliseriez la méthode `difference()` ou l'opérateur `-` pour réaliser cela en Python.

```py
>>> premier_ensemble = {1, 2, 3, 4, 5, 6}
>>> second_ensemble = {4, 5, 6, 7, 8, 9}
>>> premier_ensemble.difference(second_ensemble)
{1, 2, 3}
>>>
>>> premier_ensemble - second_ensemble     # en utilisant l'opérateur `-`
{1, 2, 3}
>>>
>>> second_ensemble - premier_ensemble
{8, 9, 7}
```

## 4. Différence symétrique d'ensembles

La différence symétrique entre deux ensembles est l'ensemble de tous les éléments qui sont *soit dans* le premier ensemble *soit dans* le second ensemble *mais pas dans les deux*.

Vous avez le choix d'utiliser soit la méthode `symmetric_difference()` soit l'opérateur `^` pour faire cela en Python.

```py
>>> premier_ensemble = {1, 2, 3, 4, 5, 6}
>>> second_ensemble = {4, 5, 6, 7, 8, 9}
>>> premier_ensemble.symmetric_difference(second_ensemble)
{1, 2, 3, 7, 8, 9}
>>>
>>> premier_ensemble ^ second_ensemble     # en utilisant l'opérateur `^`
{1, 2, 3, 7, 8, 9}
```

# Comment modifier un ensemble par des opérations

Chacune des opérations `set()` que nous avons discutées ci-dessus peut être utilisée pour *modifier* un ensemble Python existant. De manière similaire à l'utilisation d'une syntaxe d'affectation augmentée telle que `+=` ou `*=` pour mettre à jour une variable, vous pouvez faire de même pour les ensembles :

```py
>>> a = {1, 2, 3, 4, 5, 6}
>>> b = {4, 5, 6, 7, 8, 9}
>>>
>>> a.update(b)          # une opération "union"
>>> a
{1, 2, 3, 4, 5, 6, 7, 8, 9}
>>>
>>> a &= b               # l'opération "intersection"
>>> a
{4, 5, 6, 7, 8, 9}
>>>
>>> a -= set((7, 8, 9))  # l'opération "différence"
>>> a
{4, 5, 6}
>>>
>>> a ^= b               # l'opération "différence symétrique"
>>> a
{7, 8, 9}
```

# Autres opérations sur les ensembles en Python

Celles-ci ne sont pas si courantes, mais elles sont utiles pour voir comment les ensembles se rapportent les uns aux autres.

* la méthode `a.issubset(b)` ou l'opérateur `<=` retourne vrai si `a` est un *sous-ensemble* de `b`

* la méthode `a.issuperset(b)` ou l'opérateur `>=` retourne vrai si `a` est un *sur-ensemble* de `b`

* la méthode `a.isdisjoint(b)` retourne vrai s'il n'y a *aucun élément commun* entre les ensembles `a` et `b`

# Ensembles gelés en Python

Parce que les ensembles sont mutables, ils ne sont pas hachables – ce qui signifie que vous ne pouvez pas les utiliser comme clés de dictionnaire.

Python vous permet de contourner cela en utilisant un `frozenset` à la place. Celui-ci a toutes les propriétés d'un ensemble, sauf qu'il est *immuable* (ce qui signifie que vous ne pouvez pas ajouter/supprimer des éléments du frozenset). Il est également hachable, donc il peut être utilisé comme clé d'un dictionnaire.

Le type de données `frozenset` a toutes les méthodes d'un ensemble (comme `difference()`, `symmetric_difference`, et `union`) mais parce qu'il est immuable, il n'a pas de méthodes pour ajouter/supprimer des éléments.

```py
>>> a = frozenset((1, 2, 3, 4))
>>> b = frozenset((3, 4, 5, 6))
>>>
>>> a.issubset(b)
False
>>> a.update(b)    # lève une erreur
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'frozenset' object has no attribute 'update'
```

Et utiliser des `frozenset` comme clés de dictionnaire est aussi simple que 1, 2, 3 :

```py
>>> a = frozenset((1, 2, 3, 4))
>>> b = frozenset(("w", "x", "y", "z"))
>>>
>>> d = {a: "hello", b: "world"}
>>> d
{frozenset({1, 2, 3, 4}): 'hello', frozenset({'w', 'x', 'y', 'z'}): 'world'}
```

# Conclusion

C'est tout ! Vous avez appris ce que sont les ensembles, comment les créer et travailler avec eux, et les différentes opérations que vous pouvez utiliser sur eux.

Avec les ensembles maîtrisés, vous devriez maintenant être à l'aise avec la plupart des fonctions intégrées de Python. Tout ce que vous avez à faire maintenant est de pratiquer. Bonne chance !

N'oubliez pas de [me suivre sur Twitter](http://twitter.com/jasmcaus) pour plus de mises à jour. Passez une bonne journée !