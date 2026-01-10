---
title: Python List.append() – Comment ajouter à une liste en Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-07-13T15:10:46.000Z'
originalURL: https://freecodecamp.org/news/python-list-append-how-to-append-to-a-list-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/append-to-a-list.png
tags:
- name: Python
  slug: python
seo_title: Python List.append() – Comment ajouter à une liste en Python
seo_desc: 'By Dillion Megida

  How do you append (or add) new values to an already created list in Python? I will
  show you how in this article.

  But first things first...

  What is a List in Python?

  A List is a data type that allows you to store multiple values of e...'
---

Par Dillion Megida

Comment ajouter (ou insérer) de nouvelles valeurs à une liste déjà créée en Python ? Je vais vous montrer comment faire dans cet article.

Mais d'abord...

## Qu'est-ce qu'une `List` en Python ?

Une `List` est un type de données qui vous permet de stocker plusieurs valeurs de types identiques ou différents dans une seule variable.

Regardez l'exemple ci-dessous :

```python
age = 50
name = "Python"
isRunning = False
```

Dans ce code, `age`, `name` et `isRunning` ne contiennent qu'une seule valeur chacun, respectivement des types de données `number`, `string` et `boolean`.

Supposons que vous souhaitiez stocker tous les articles que vous avez achetés au marché en utilisant cette approche :

```python
item1 = "banana"
item2 = "apple"
item3 = "orange"
```

Créer trois variables séparées pour des éléments liés n'est peut-être pas la meilleure approche.

Avec les listes, vous pouvez créer une variable qui contient plusieurs valeurs. Voici comment :

```python
numbers = [1, 2, 3]

strings = ["list", "dillion", "python"]

mixed = [10, "python", False, [40, "yellow"]]
```

La variable `numbers` est une liste contenant trois valeurs numériques.

La variable `strings` est une liste contenant trois valeurs de type chaîne de caractères.

La variable `mixed` est une liste contenant un nombre, une chaîne de caractères, un booléen, et même une autre liste.

Ainsi, pour les articles que vous avez achetés au marché, vous pouvez les stocker comme ceci :

```python
items = ["banana", "apple", "orange"]
```

Et vous pouvez accéder à chaque élément en utilisant sa position d'index dans la liste, en commençant par 0 (car les listes sont indexées à partir de zéro en Python) :

```python
print(items[0], items[1], items[2])
# banana apple orange
```

## Comment ajouter des données à une liste en Python

Nous avons brièvement vu ce que sont les listes. Alors, comment mettre à jour une liste avec de nouvelles valeurs ? En utilisant la méthode `List.append()`.

La méthode `append` reçoit un argument, qui est la valeur que vous souhaitez ajouter à la fin de la liste.

Voici comment utiliser cette méthode :

```python
mixed = [10, "python", False]

mixed.append(40)

print(mixed)
# [10, 'python', False, 40]
```

En utilisant la méthode `append`, vous avez ajouté `40` à la fin de la liste `mixed`.

Vous pouvez ajouter n'importe quel type de données que vous souhaitez, y compris d'autres listes :

```python
mixed = [10, "python", False]

mixed.append([True, "hello"])

print(mixed)

# [10, 'python', False, [True, 'hello']]
```

## Conclusion

Les listes sont utiles pour créer des variables qui contiennent plusieurs valeurs (surtout lorsque ces valeurs sont liées).

Les listes disposent de nombreuses méthodes en Python que vous pouvez utiliser pour modifier, étendre ou réduire les listes. Dans cet article, nous avons examiné la méthode `append` qui ajoute des données à la fin de la liste.