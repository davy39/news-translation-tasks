---
title: Python List Append – Comment ajouter un élément à un tableau, expliqué avec
  des exemples
subtitle: ''
author: Estefania Cassingena Navone
co_authors: []
series: null
date: '2020-05-08T18:29:00.000Z'
originalURL: https://freecodecamp.org/news/python-list-append-how-to-add-an-element-to-an-array-explained-with-examples
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/Append.png
tags:
- name: Python
  slug: python
- name: Tutorial
  slug: tutorial
seo_title: Python List Append – Comment ajouter un élément à un tableau, expliqué
  avec des exemples
seo_desc: 'Welcome

  Hi! If you want to learn how to use the **append()** method, then this article is
  for you. This is a powerful list method that you will definitely use in your Python
  projects.

  In this article, you will learn:


  Why and when you should use appe...'
---

## Bienvenue

Bonjour ! Si vous souhaitez apprendre à utiliser la méthode `**append()**`, alors cet article est fait pour vous. Il s'agit d'une méthode de liste puissante que vous utiliserez définitivement dans vos projets Python.

**Dans cet article, vous apprendrez :**

* Pourquoi et quand utiliser `append()`.
* Comment l'appeler.
* Son effet et sa valeur de retour.
* Comment elle peut être équivalente à `insert()` et au découpage de chaînes avec les arguments appropriés.

Vous trouverez des exemples d'utilisation de `append()` appliqués aux chaînes, entiers, flottants, booléens, listes, tuples et dictionnaires.

**Commençons ! ✨**

## 📝 Objectif

Avec cette méthode, vous pouvez **ajouter un seul élément à la fin d'une liste**.

Voici l'effet de `append()` représenté graphiquement :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-59.png)

💡 **Astuce :** Pour ajouter une séquence d'éléments individuels, vous devriez utiliser la méthode `extend()`.

## 📌 Syntaxe & Paramètres

Voici la syntaxe de base que vous devez utiliser pour appeler cette méthode :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-60.png)

💡 **Astuce :** Le point est très important puisque `append()` est une méthode. Lorsque nous appelons une méthode, nous utilisons un point après la liste pour indiquer que nous voulons "modifier" ou "affecter" cette liste particulière.

Comme vous pouvez le voir, la méthode `append()` ne prend qu'un seul argument, l'élément que vous souhaitez ajouter. Cet élément peut être de n'importe quel type de données :

* Entier
* Chaîne
* Flottant
* Booléen
* Une autre liste
* Tuple
* Dictionnaire
* Une instance d'une classe personnalisée

En gros, toute valeur que vous pouvez créer en Python peut être ajoutée à une liste.

**💡 Astuce :** Le premier élément de la syntaxe (la liste) est généralement une variable qui référence une liste.

### Exemple

Voici un exemple d'appel à `append()` :

```python
>>> musical_notes = ["C", "D", "E", "F", "G", "A"]
>>> musical_notes.append("B")
```

* Tout d'abord, la liste est définie et assignée à une variable.
* Ensuite, en utilisant cette variable, nous appelons la méthode `append()`, en passant l'élément que nous voulons ajouter (la chaîne `"B"`) comme argument.

## 📝 Effet & Valeur de retour

Cette méthode **modifie** (change) la liste originale en mémoire. Elle ne retourne pas une nouvelle copie de la liste comme nous pourrions intuitivement le penser, elle retourne `None`. Par conséquent, simplement en appelant cette méthode, vous modifiez la liste originale.

Dans notre exemple précédent :

```python
>>> musical_notes = ["C", "D", "E", "F", "G", "A"]
>>> musical_notes.append("B")
```

Vous pouvez voir (ci-dessous) que la liste originale a été modifiée après l'ajout de l'élément. Le dernier élément est maintenant `"B"` et la liste originale est maintenant la version modifiée.

```python
>>> musical_notes
['C', 'D', 'E', 'F', 'G', 'A', 'B']
```

Vous pouvez confirmer que la valeur de retour de `append()` est `None` en assignant cette valeur à une variable et en l'affichant :

```python
>>> musical_notes = ["C", "D", "E", "F", "G", "A"]
>>> a = musical_notes.append("B")
>>> print(a)
None
```

## 📌 Exemples

Maintenant que vous connaissez l'objectif, la syntaxe et l'effet de la méthode `append()`, voyons quelques exemples de son utilisation avec divers types de données.

### Ajouter une chaîne

```python
>>> top_players = ["gino234", "nor233", "lal453"]
>>> top_players.append("auop342")

# La chaîne a été ajoutée
>>> top_players
['gino234', 'nor233', 'lal453', 'auop342']
```

### Ajouter un entier

```python
>>> data = [435, 324, 275, 567, 123]
>>> data.append(456)

>>> data
[435, 324, 275, 567, 123, 456]
```

### Ajouter un flottant

```python
>>> data = [435.34, 324.35, 275.45, 567.34, 123.23]
>>> data.append(456.23)

>>> data
[435.34, 324.35, 275.45, 567.34, 123.23, 456.23]
```

### Ajouter une valeur booléenne

```python
>>> values = [True, True, False, True]
>>> values.append(False)

>>> values
[True, True, False, True, False]
```

### Ajouter une liste

Cette méthode ajoute un seul élément à la fin de la liste, donc si vous passez une liste comme argument, toute la liste sera ajoutée comme un seul élément (elle sera une liste imbriquée dans la liste originale).

```python
>>> data = [[4.5, 4.8, 5.7], [2.5, 2.6, 2.7]]
>>> data.append([6.7, 2.3])

>>> data
[[4.5, 4.8, 5.7], [2.5, 2.6, 2.7], [6.7, 2.3]]
```

### Ajouter un tuple

Cela fonctionne exactement de la même manière pour les tuples, tout le tuple est ajouté comme un seul élément.

```python
>>> data = [[4.5, 4.8, 5.7], [2.5, 2.6, 2.7]]
>>> data.append((6.7, 2.3))

>>> data
[[4.5, 4.8, 5.7], [2.5, 2.6, 2.7], (6.7, 2.3)]
```

**💡 Astuce :** Si vous devez ajouter les éléments d'une liste ou d'un tuple comme éléments individuels de la liste originale, vous devez utiliser la méthode `extend()` au lieu de `append()`. Pour en savoir plus, vous pouvez lire mon article : [Python List Append VS Python List Extend – The Difference Explained with Array Method Examples](https://www.freecodecamp.org/news/python-list-append-vs-python-list-extend/)

### Ajouter un dictionnaire

De même, si vous essayez d'ajouter un dictionnaire, tout le dictionnaire sera ajouté comme un seul élément de la liste.

```python
>>> data = [{"a": 1, "b": 2}]
>>> data.append({"c": 3, "d": 4})
>>> data
[{'a': 1, 'b': 2}, {'c': 3, 'd': 4}]
```

## 📝 Équivalence de Append et Insert

Une astuce intéressante est que la méthode `insert()` peut être équivalente à `append()` si nous passons les arguments corrects.

La méthode `insert()` est utilisée pour insérer un élément à un index (position) particulier dans la liste.

Voici la syntaxe utilisée pour appeler la méthode `insert()` :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-61.png)

**Pour la rendre équivalente à `append()` :**

* La valeur de l'index doit être la longueur de la liste (`len(<list>)`) car nous voulons que l'élément soit le dernier élément de la liste.

Voici un exemple qui montre que le résultat de l'utilisation de insert avec ces arguments est équivalent à `append()` :

```python
>>> musical_notes = ["C", "D", "E", "F", "G", "A"]
>>> musical_notes.insert(len(musical_notes), "B")
>>> musical_notes
['C', 'D', 'E', 'F', 'G', 'A', 'B']
```

Mais comme vous l'avez vu, `append()` est beaucoup plus concis et pratique, donc il est généralement recommandé de l'utiliser dans ce cas.

## 📌 Équivalence de Append et du découpage de liste

Il existe également une équivalence intéressante entre la méthode `append()` et le découpage de liste.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-62.png)

Cette syntaxe consiste essentiellement à assigner la liste qui contient l'élément `[<elem>]` comme dernière portion (fin) de la liste. Voici que le résultat est équivalent à `append()` :

```python
>>> musical_notes = ["C", "D", "E", "F", "G", "A"]
>>> musical_notes[len(musical_notes):] = ["B"]
>>> musical_notes
['C', 'D', 'E', 'F', 'G', 'A', 'B']
```

Ce sont des alternatives intéressantes, mais à des fins pratiques, nous utilisons généralement `append()` car c'est un outil précieux que Python offre. Il est précis, concis et facile à utiliser.

**J'espère vraiment que vous avez aimé mon article et que vous l'avez trouvé utile.** Maintenant, vous pouvez travailler avec `append()` dans vos projets Python. [Découvrez mes cours en ligne](https://www.udemy.com/user/estefania-cn/). Suivez-moi sur [Twitter](https://twitter.com/EstefaniaCassN). ⭐️