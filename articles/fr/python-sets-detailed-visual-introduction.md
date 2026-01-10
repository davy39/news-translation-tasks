---
title: 'Ensembles Python : Une Introduction Visuelle Détaillée'
subtitle: ''
author: Estefania Cassingena Navone
co_authors: []
series: null
date: '2020-01-06T13:19:00.000Z'
originalURL: https://freecodecamp.org/news/python-sets-detailed-visual-introduction
coverImage: https://www.freecodecamp.org/news/content/images/2019/12/Sets-3.png
tags:
- name: Computer Science
  slug: computer-science
- name: learning to code
  slug: learning-to-code
- name: programing
  slug: programing
- name: Python
  slug: python
- name: Sets
  slug: sets
seo_title: 'Ensembles Python : Une Introduction Visuelle Détaillée'
seo_desc: "Welcome\nIn this article, you will learn the fundamentals of Sets in Python.\
  \ This is a very powerful built-in data type that you can use in your Python projects.\
  \ \nWe will explore:\n\nWhat sets are and why they are relevant for your projects.\n\
  How to crea..."
---

## Bienvenue

Dans cet article, vous apprendrez les bases des ensembles en Python. Il s'agit d'un type de données intégré très puissant que vous pouvez utiliser dans vos projets Python.

**Nous explorerons :**

* Ce que sont les ensembles et pourquoi ils sont pertinents pour vos projets.
* Comment créer un ensemble.
* Comment vérifier si un élément est dans un ensemble.
* La différence entre les ensembles et les ensembles gelés (frozensets).
* Comment opérer avec les ensembles (dans cette partie, nous plongerons dans les bases de la théorie des ensembles).
* Comment ajouter et supprimer des éléments des ensembles et comment les vider.

**Commençons ! ⭐**

## 🔹 Ensembles en Contexte

Permettez-moi de commencer par vous expliquer pourquoi vous pourriez vouloir utiliser des ensembles dans vos projets. En mathématiques, un ensemble est une collection d'objets distincts. En Python, ce qui les rend si spéciaux est le fait qu'**ils n'ont pas d'éléments en double**, ils peuvent donc être utilisés pour supprimer efficacement les éléments en double des listes et des tuples.

Selon la [Documentation Python](https://docs.python.org/3/tutorial/datastructures.html#sets) :

> Python inclut également un type de données pour les _ensembles_. Un ensemble est une collection non ordonnée sans éléments en double. Les utilisations de base incluent les tests d'appartenance et l'élimination des entrées en double.

**❗ Important :** Les éléments d'un ensemble doivent être immuables (ils ne peuvent pas être modifiés). Les types de données immuables incluent les chaînes de caractères, les tuples et les nombres tels que les entiers et les flottants.

## 🔸 Syntaxe

Pour créer un ensemble, nous commençons par écrire une paire d'accolades `{}` et à l'intérieur de ces accolades, nous incluons les éléments de l'ensemble séparés par une virgule et un espace.

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-66.png)

**💡 Astuce :** Remarquez que cette syntaxe est différente des dictionnaires Python car nous ne créons pas de paires clé-valeur, nous incluons simplement des éléments individuels à l'intérieur des accolades `{}`.

### set()

Alternativement, nous pouvons utiliser la fonction [set()](https://docs.python.org/3/library/stdtypes.html#set) pour créer un ensemble (voir ci-dessous).

Pour ce faire, nous passons un itérable (par exemple, une liste, une chaîne ou un tuple) et cet itérable est converti en un ensemble, supprimant tous les éléments en double.

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-64.png)

Voici un exemple dans IDLE :

```python
# Ensemble
>>> {1, 2, 3, 4}
{1, 2, 3, 4}

# À partir d'une liste
>>> set([1, 2, 3, 4])
{1, 2, 3, 4}

# À partir d'un tuple
>>> set((1, 2, 3, 4))
{1, 2, 3, 4}
```

**💡 Astuce :** Pour créer un ensemble vide, vous devez utiliser la fonction [set()](https://docs.python.org/3/library/stdtypes.html#set) car l'utilisation d'un ensemble vide d'accolades, comme ceci `{}`, créera automatiquement un dictionnaire vide, et non un ensemble vide.

```python
# Crée un dictionnaire, pas un ensemble.
>>> type({})
<class 'dict'>

# Ceci est un ensemble
>>> type(set())
<class 'set'>
```

## 🔹 Les Éléments en Double sont Supprimés

Si l'itérable que vous passez comme argument à `set()` contient des éléments en double, ils sont supprimés pour créer l'ensemble.

Par exemple, remarquez comment les éléments en double sont supprimés lorsque nous passons cette liste :

```python
>>> a = [1, 2, 2, 2, 2, 3, 4, 1, 4]
>>> set(a)
{1, 2, 3, 4}
```

et remarquez comment les caractères en double sont supprimés lorsque nous passons cette chaîne :

```python
>>> a = "hhheeelllooo"
>>> set(a)
{'e', 'l', 'o', 'h'}
```

## 🔸 Longueur

Pour trouver la longueur d'un ensemble, vous pouvez utiliser la fonction intégrée [len()](https://docs.python.org/3/library/stdtypes.html#set) :

```python
>>> a = {1, 2, 3, 4}
>>> b = set(a)
>>> len(b)
4
```

En mathématiques, le nombre d'éléments d'un ensemble est appelé la "**cardinalité**" de l'ensemble.

## 🔹 Test d'Appartenance

Vous pouvez tester si un élément est dans un ensemble avec l'opérateur `in` :

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-65.png)

Voici un exemple :

```python
>>> a = "hhheeelllooo"
>>> b = set(a)
>>> b
{'e', 'l', 'o', 'h'}

# Test si les caractères 'e' et 'a' sont dans l'ensemble b
>>> 'e' in b
True
>>> 'a' in b
False
```

## 🔸 Ensembles vs. Ensembles Gelés (Frozensets)

Les ensembles sont mutables, ce qui signifie qu'ils peuvent être modifiés après avoir été définis.

Selon la [Documentation Python](https://docs.python.org/3.8/library/stdtypes.html#set-types-set-frozenset) :

> Le type [`set`](https://docs.python.org/3.8/library/stdtypes.html#set) est **mutable** — le contenu peut être modifié en utilisant des méthodes comme `add()` et `remove()`. Puisqu'il est mutable, il n'a pas de valeur de hachage et ne peut pas être utilisé comme clé de dictionnaire ou comme élément d'un autre ensemble.

Puisqu'ils ne peuvent pas contenir de valeurs de types de données mutables, si nous essayons de créer un ensemble qui contient des ensembles comme éléments (ensembles imbriqués), nous verrons cette erreur :

```python
TypeError: unhashable type: 'set'

```

Voici un exemple dans IDLE. Remarquez comment les éléments que nous essayons d'inclure sont des ensembles :

```python
>>> a = {{1, 2, 3}, {1, 2, 4}}
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a = {{1, 2, 3}, {1, 2, 4}}
TypeError: unhashable type: 'set'
```

### Ensembles Gelés (Frozensets)

Pour résoudre ce problème, nous avons un autre type d'ensemble appelé ensembles gelés (frozensets).

Ils sont **immuables**, donc ils ne peuvent pas être modifiés et nous pouvons les utiliser pour créer des ensembles imbriqués.

Selon la [Documentation Python](https://docs.python.org/3.8/library/stdtypes.html#set-types-set-frozenset) :

> Le type [`frozenset`](https://docs.python.org/3.8/library/stdtypes.html#frozenset) est immuable et [hachable](https://docs.python.org/3.8/glossary.html#term-hashable) — son contenu ne peut pas être altéré après sa création ; il peut donc être utilisé comme clé de dictionnaire ou comme élément d'un autre ensemble.

Pour créer un ensemble gelé, nous utilisons :

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-67.png)

💡 **Astuce :** Vous pouvez créer un ensemble gelé vide avec `frozenset()`.

Voici un exemple d'un ensemble qui contient deux ensembles gelés :

```
>>> a = {frozenset([1, 2, 3]), frozenset([1, 2, 4])}
>>> a
{frozenset({1, 2, 3}), frozenset({1, 2, 4})}
```

Remarquez que nous n'obtenons aucune erreur et que l'ensemble est créé avec succès.

## 🔹 Introduction à la Théorie des Ensembles

Avant de plonger dans les opérations sur les ensembles, nous devons explorer un peu la théorie des ensembles et les diagrammes de Venn. Nous plongerons dans chaque opération sur les ensembles avec son équivalent correspondant en code Python. Commençons.

### Sous-ensembles et Sur-ensembles

Vous pouvez penser à un sous-ensemble comme une "partie plus petite" d'un ensemble. C'est ainsi que j'aime le concevoir. Si vous prenez certains des éléments d'un ensemble et faites un nouvel ensemble avec ces éléments, le nouvel ensemble est un sous-ensemble de l'ensemble original.

C'est comme si vous aviez un sac rempli de balles en caoutchouc de différentes couleurs. Si vous faites un ensemble avec toutes les balles en caoutchouc dans le sac, puis prenez certaines de ces balles en caoutchouc et faites un nouvel ensemble avec elles, le nouvel ensemble est un sous-ensemble de l'ensemble original.

Permettez-moi d'illustrer cela graphiquement. Si nous avons un ensemble A avec les éléments 1, 2, 3, 4 :

```
>>> a = {1, 2, 3, 4}
```

Nous pouvons "prendre" ou "sélectionner" certains éléments de a et faire un nouvel ensemble appelé B. Supposons que nous choisissons d'inclure les éléments 1 et 2 dans l'ensemble B :

```python
>>> a = {1, 2, 3, 4}
>>> b = {1, 2}
```

Chaque élément de B est dans A. Par conséquent, B est un sous-ensemble de A.

Cela peut être représenté graphiquement comme ceci, où le nouvel ensemble B est illustré en jaune :

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-69.png)

**💡 Note :** En théorie des ensembles, il est conventionnel d'utiliser des lettres majuscules pour désigner les ensembles. C'est pourquoi je les utiliserai pour faire référence aux ensembles (A et B), mais j'utiliserai des lettres minuscules en Python (a et b).

### .issubset()

Nous pouvons vérifier si B est un sous-ensemble de A avec la méthode [.issubset(<other>)](https://docs.python.org/3/library/stdtypes.html#frozenset.issubset) :

```python
>>> a = {1, 2, 3, 4}
>>> b = {1, 2}
>>> b.issubset(a)
True
```

Comme vous pouvez le voir, B est un sous-ensemble de A car la valeur retournée est `True`.

Mais l'inverse n'est pas vrai puisque tous les éléments de A ne sont pas dans B :

```python
>>> a.issubset(b)
False
```

Voyons quelque chose de très intéressant :

```python
>>> a = {1, 2, 3, 4}
>>> b = {1, 2, 3, 4}
>>> a.issubset(b)
True
>>> b.issubset(a)
True
```

Si deux ensembles sont égaux, l'un est un sous-ensemble de l'autre et vice versa car tous les éléments de A sont dans B et tous les éléments de B sont dans A. Cela peut être illustré comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-70.png)

### Utilisation de <=

Nous pouvons obtenir la même fonctionnalité que la méthode `.issubset()` avec l'opérateur de comparaison `<=` :

```python
>>> a = {1, 2, 3, 4}
>>> b = {1, 2, 3, 4}
>>> a <= b
True
```

Cet opérateur retourne `True` si l'opérande de gauche est un sous-ensemble de l'opérande de droite, même lorsque les deux ensembles sont égaux (quand ils ont les mêmes éléments).

### Sous-ensemble Propre

Mais que se passe-t-il si nous voulons vérifier si un ensemble est un **sous-ensemble propre** d'un autre ? Un sous-ensemble propre est un sous-ensemble qui n'est pas égal à l'ensemble (n'a pas tous les mêmes éléments).

Voici un exemple graphique d'un sous-ensemble propre. B n'a pas tous les éléments de A :

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-69.png)

Pour vérifier cela, nous pouvons utiliser l'opérateur de comparaison `<` :

```python
# B n'est pas un sous-ensemble propre de A car B est égal à A
>>> a = {1, 2, 3, 4}
>>> b = {1, 2, 3, 4}
>>> b < a
False

# B est un sous-ensemble propre de A car B n'est pas égal à A
>>> a = {1, 2, 3, 4}
>>> b = {1, 2}
>>> b < a
True
```

### Sur-ensemble

**Si B est un sous-ensemble de A, alors A est un sur-ensemble de B**. Un sur-ensemble est l'ensemble qui contient tous les éléments du sous-ensemble.

Cela peut être illustré comme ceci (voir ci-dessous), où A est un sur-ensemble de B :

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-97.png)

### .issuperset()

Nous pouvons tester si un ensemble est un sur-ensemble d'un autre avec la méthode [.issuperset()](https://docs.python.org/3/library/stdtypes.html#frozenset.issuperset) :

```python
>>> a = {1, 2, 3, 4}
>>> b = {1, 2}
>>> a.issuperset(b)
True
```

Nous pouvons également utiliser les opérateurs `>` et `>=`. Ils fonctionnent exactement comme `<` et `<=`, mais maintenant ils déterminent si l'opérande de gauche est un **sur-ensemble** de l'opérande de droite :

```python
>>> a = {1, 2, 3, 4}
>>> b = {1, 2}
>>> a > b
True
>>> a >= b
True
```

### Ensembles Disjoints

Deux ensembles sont disjoints s'ils n'ont aucun élément en commun. Par exemple, voici deux ensembles disjoints :

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-83.png)

### .isdisjoint()

Nous pouvons vérifier si deux ensembles sont disjoints avec la méthode [.isdisjoint()](https://docs.python.org/3/library/stdtypes.html#frozenset.isdisjoint) :

```python
# Éléments en commun : 3, 1
>>> a = {3, 6, 1}
>>> b = {2, 8, 3, 1}
>>> a.isdisjoint(b)
False

# Éléments en commun : Aucun
>>> a = {3, 1, 4}
>>> b = {8, 9, 0}
>>> a.isdisjoint(b)
True
```

## 🔸 Opérations sur les Ensembles

Nous pouvons opérer sur les ensembles pour créer de nouveaux ensembles, en suivant les règles de la théorie des ensembles. Explorons ces opérations.

### Union

Il s'agit de la première opération que nous allons analyser. Elle crée un nouvel ensemble qui contient tous les éléments des deux ensembles (sans répétition).

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-72.png)

Voici un exemple :

```python
>>> a = {3, 1, 7, 4}
>>> b = {2, 8, 3, 1}
>>> a | b
{1, 2, 3, 4, 7, 8}
```

💡 **Astuce :** Nous pouvons assigner cet nouvel ensemble à une variable, comme ceci :

```python
>>> a = {3, 1, 7, 4}
>>> b = {2, 8, 3, 1}
>>> c = a | b
>>> c
{1, 2, 3, 4, 7, 8}
```

Dans un diagramme, ces ensembles pourraient être représentés comme ceci (voir ci-dessous). Cela s'appelle un diagramme de Venn, et il est utilisé pour illustrer les relations entre les ensembles et le résultat des opérations sur les ensembles.

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-74.png)
_Diagramme de Venn. Union._

Nous pouvons facilement étendre cette opération pour qu'elle fonctionne avec plus de deux ensembles :

```python
>>> a = {3, 1, 7, 4}
>>> b = {2, 8, 3, 1}
>>> c = {1, 0, 4, 6}
>>> d = {8, 2, 6, 3}

# Union de ces quatre ensembles
>>> a | b | c | d
{0, 1, 2, 3, 4, 6, 7, 8}
```

💡 **Astuce :** Si l'union contient des éléments répétés, un seul est inclus dans l'ensemble final pour éliminer la répétition.

### Intersection

L'intersection entre deux ensembles crée un autre ensemble qui contient tous les éléments qui sont **dans** **A et B**.

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-77.png)

Voici un exemple :

```python
>>> a = {3, 6, 1}
>>> b = {2, 8, 3, 1}
>>> a & b
{1, 3}
```

Le diagramme de Venn pour l'opération d'intersection serait comme ceci (voir ci-dessous), car seuls les éléments qui sont **dans A et B** sont inclus dans l'ensemble résultant :

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-78.png)
_Diagramme de Venn. Intersection._

Nous pouvons facilement étendre cette opération pour qu'elle fonctionne avec plus de deux ensembles :

```python
>>> a = {3, 1, 7, 4, 5}
>>> b = {2, 8, 3, 1, 5}
>>> c = {1, 0, 4, 6, 5}
>>> d = {8, 2, 6, 3, 5}

# Seul 5 est dans a, b, c et d.
>>> a & b & c & d
{5}
```

### Différence

La différence entre l'ensemble A et l'ensemble B est un autre ensemble qui contient tous les **éléments de l'ensemble A qui ne sont pas dans l'ensemble B**.

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-79.png)

Voici un exemple :

```python
>>> a = {3, 6, 1}
>>> b = {2, 8, 3, 1}
>>> a - b
{6}
```

Le diagramme de Venn pour cette différence serait comme ceci (voir ci-dessous), car seuls les éléments de A qui ne sont pas dans B sont inclus dans l'ensemble résultant :

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-80.png)
_Diagramme de Venn. Différence._

💡 **Astuce :** Remarquez comment nous supprimons les éléments de A qui sont également dans B (dans l'intersection).

Nous pouvons facilement étendre cela pour qu'il fonctionne avec plus de deux ensembles :

```python
>>> a = {3, 1, 7, 4, 5}
>>> b = {2, 8, 3, 1, 5}
>>> c = {1, 0, 4, 6, 5}

# Seul 7 est dans A mais pas dans B et pas dans C
>>> a - b - c
{7}
```

### Différence Symétrique

La différence symétrique entre deux ensembles A et B est un autre ensemble qui contient **tous les éléments qui sont dans A ou B, mais pas les deux**. Nous supprimons essentiellement les éléments de l'intersection.

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-81.png)

```python
>>> a = {3, 6, 1}
>>> b = {2, 8, 3, 1}
>>> a ^ b
{2, 6, 8}
```

Le diagramme de Venn pour la différence symétrique serait comme ceci (voir ci-dessous), car seuls les éléments qui sont dans A ou B, mais pas les deux, sont inclus dans l'ensemble résultant :

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-82.png)
_Diagramme de Venn. Différence Symétrique_

Nous pouvons facilement étendre cela pour qu'il fonctionne avec plus de deux ensembles :

```python
>>> a = {3, 1, 7, 4, 5}
>>> b = {2, 8, 3, 1, 5}
>>> c = {1, 0, 4, 6, 5}
>>> d = {8, 2, 6, 3, 5}

>>> a ^ b ^ c ^ d
{0, 1, 3, 7}
```

### Mettre à Jour les Ensembles Automatiquement

Si vous souhaitez mettre à jour l'ensemble A immédiatement après avoir effectué ces opérations, vous pouvez simplement ajouter un signe égal après l'opérateur. Par exemple :

```python
>>> a = {1, 2, 3, 4}
>>> b = {1, 2}

# Remarquez le &= 
>>> a &= b
>>> a
{1, 2}
```

Nous assignons l'ensemble qui résulte de `a & b` à l'ensemble `a` en une seule ligne. Vous pouvez faire de même avec les autres opérateurs : `^=` , `|=`, et `-=`.

**💡 Astuce :** Cela est très similaire à la syntaxe que nous utilisons avec les variables (par exemple : `a += 5`) mais maintenant nous travaillons avec des ensembles.

## 🔸 Méthodes des Ensembles

Les ensembles incluent des méthodes intégrées utiles pour nous aider à effectuer des fonctionnalités courantes et essentielles telles que l'ajout d'éléments, la suppression d'éléments et le vidage de l'ensemble.

### Ajouter des Éléments

Pour ajouter des éléments à un ensemble, nous utilisons la méthode [.add()](https://docs.python.org/3/library/stdtypes.html#frozenset.add), en passant l'élément comme seul argument.

```
>>> a = {1, 2, 3, 4}
>>> a.add(7)
>>> a
{1, 2, 3, 4, 7}
```

### Supprimer des Éléments

Il existe trois façons de supprimer un élément d'un ensemble : `.remove(<elem>)` ,`.discard(<elem>)`, et `.pop()`. Ils ont des différences clés que nous allons explorer.

Les deux premières méthodes (.remove() et .discard()) fonctionnent exactement de la même manière lorsque l'élément est dans l'ensemble. Le nouvel ensemble est retourné :

```python
>>> a = {1, 2, 3, 4}
>>> a.remove(3)
>>> a
{1, 2, 4}

>>> a = {1, 2, 3, 4}
>>> a.discard(3)
>>> a
{1, 2, 4}
```

La différence clé entre ces deux méthodes est que si nous utilisons la méthode [.remove()](https://docs.python.org/3/library/stdtypes.html#frozenset.remove), nous risquons d'essayer de supprimer un élément qui n'existe pas dans l'ensemble et cela lèvera une `KeyError` :

```python
>>> a = {1, 2, 3, 4}
>>> a.remove(5)
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    a.remove(5)
KeyError: 5
```

Nous n'aurons jamais ce problème avec [.discard()](https://docs.python.org/3/library/stdtypes.html#frozenset.discard) car il ne lève pas d'exception si l'élément n'est pas trouvé. Cette méthode laissera simplement l'ensemble intact, comme vous pouvez le voir dans cet exemple :

```python
>>> a = {1, 2, 3, 4}
>>> a.discard(5)
>>> a
{1, 2, 3, 4}
```

La troisième méthode ([.pop()](https://docs.python.org/3/library/stdtypes.html#frozenset.pop)) supprimera et retournera un élément arbitraire de l'ensemble et lèvera une `KeyError` si l'ensemble est vide.

```python
>>> a = {1, 2, 3, 4}
>>> a.pop()
1
>>> a.pop()
2
>>> a.pop()
3
>>> a
{4}
>>> a.pop()
4
>>> a
set()
>>> a.pop()
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    a.pop()
KeyError: 'pop from an empty set'
```

### Vider l'Ensemble

Vous pouvez utiliser la méthode `.clear()` si vous devez supprimer tous les éléments d'un ensemble. Par exemple :

```python
>>> a = {1, 2, 3, 4}
>>> a.clear()
>>> a
set()
>>> len(a)
0
```

## 🔹 En Résumé

* Les ensembles sont des types de données intégrés non ordonnés qui n'ont aucun élément répété, ils nous permettent donc d'éliminer les éléments répétés des listes et des tuples.
* Ils sont mutables et ne peuvent contenir que des éléments immuables.
* Nous pouvons vérifier si un ensemble est un sous-ensemble ou un sur-ensemble d'un autre ensemble.
* Frozenset est un type d'ensemble immuable qui nous permet de créer des ensembles imbriqués.
* Nous pouvons opérer sur les ensembles avec : union (`|`), intersection (`&`), différence (`-`), et différence symétrique (`^`).
* Nous pouvons ajouter des éléments à un ensemble, les supprimer et vider complètement l'ensemble en utilisant des méthodes intégrées.

**J'espère vraiment que vous avez aimé mon article et que vous l'avez trouvé utile.** Maintenant, vous pouvez travailler avec des ensembles dans vos projets Python. [Découvrez mes cours en ligne](https://www.udemy.com/user/estefania-cn/). Suivez-moi sur [Twitter](https://twitter.com/EstefaniaCassN). ⭐