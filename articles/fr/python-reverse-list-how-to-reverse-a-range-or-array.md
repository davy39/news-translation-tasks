---
title: Python Reverse List – Comment inverser une plage ou un tableau
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2021-11-22T14:54:14.000Z'
originalURL: https://freecodecamp.org/news/python-reverse-list-how-to-reverse-a-range-or-array
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/markus-winkler-Q2J2qQsoYH8-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: Python Reverse List – Comment inverser une plage ou un tableau
seo_desc: 'In this tutorial, you''ll learn some of the different ways you can reverse
  lists and list ranges in Python. And we''ll look at some coding examples along the
  way.

  Let''s get started!

  How to create a range in Python

  An efficient way to create a list of a...'
---

Dans ce tutoriel, vous apprendrez différentes façons d'inverser des listes et des plages de listes en Python. Et nous examinerons quelques exemples de code en cours de route.

Commençons !

## Comment créer une plage en Python

Une façon efficace de créer une liste de plage de nombres en Python est d'utiliser la fonction intégrée `range()`.

Pour créer une liste avec une plage de nombres, vous utilisez le constructeur `list()` et à l'intérieur, la fonction `range()`.

La fonction range prend jusqu'à trois paramètres – les paramètres `start, stop, et step`, avec la syntaxe de base ressemblant à ceci :

`range(start, stop, step)`.

Le paramètre `start` est le nombre à partir duquel le comptage commence.

Le paramètre `stop` est le nombre jusqu'auquel – mais non inclus – le comptage s'arrête.

Le paramètre `step` est le nombre qui détermine comment les nombres seront incrémentés.

Parmi les trois paramètres, seul `stop` est requis et les autres sont optionnels.

Si vous n'incluez que le paramètre `stop`, gardez à l'esprit que par défaut le comptage commence à 0 et se termine un nombre avant celui que vous avez spécifié.

Par exemple :

```python
#crée une liste de nombres qui
#commence à 0 et se termine à 3, pas 4.

my_range = list(range(4))

print(my_range)
#output
#[0, 1, 2, 3]
```

Voici donc comment vous mettriez tout cela ensemble afin de créer une liste de plage de nombres :

```python
#crée une liste de plage de nombres :
#en commençant par 0
#jusqu'à, mais non inclus, 10
#et le comptage est incrémenté de 1

my_range = list(range(0, 10, 1))

#imprimer dans la console
print(my_range)

#output
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#vérifier le type en utilisant la méthode intégrée type()
print(type(my_range))

#output
#<class 'list'>
```

## Comment inverser une plage en Python

Pour inverser une plage de nombres en Python avec la fonction `range()`, vous utilisez un pas négatif, comme `-1`.

L'exemple ci-dessous crée une liste de plage de nombres commençant par 9 jusqu'à, mais non inclus, -1 (donc le comptage s'arrête à 0) et le comptage de la séquence est décrémenté de 1 chaque fois :

```python
my_range = list(range(9, -1, -1))

print(my_range)
#output
#[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

print(type(my_range))
#<class 'list'>
```

Lorsque vous *inversez* une liste, vous devez inclure les paramètres `start` et `step`.

## Comment inverser un tableau en Python

Un tableau en programmation est une collection ordonnée d'éléments, tous du même type de données.

Chaque élément de la collection a son propre numéro d'index.

Cependant, contrairement à d'autres langages de programmation, les tableaux ne sont pas une structure de données intégrée en Python.

Au lieu de cela, vous utilisez des listes, et Python offre plusieurs façons de les inverser.

## Comment inverser une liste en Python en utilisant la méthode `.reverse()`

En utilisant cette méthode intégrée de Python, la liste change *en place*. Cela signifie que l'ordre original de la liste est affecté.

L'ordre initial des éléments est mis à jour et modifié.

Par exemple, supposons que vous avez la liste suivante :

```python
#liste initiale
my_list = [10,20,30,40,50]

print("Ma liste initiale est : ",my_list)

#output
#Ma liste initiale est :  [10, 20, 30, 40, 50]
```

Pour changer l'ordre des éléments de `my_list` pour qu'ils soient `50, 40, 30, 20,10`, vous feriez :

```python
#liste initiale
my_list = [10,20,30,40,50]

#inverser l'ordre des éléments
my_list.reverse()

print("Voici à quoi ressemble la liste maintenant : ", my_list)

#output
#Voici à quoi ressemble la liste maintenant :  [50, 40, 30, 20, 10]
```

Vous voyez que l'ordre initial de la liste a maintenant changé et que les éléments à l'intérieur ont été inversés.

## Comment inverser une liste en Python en utilisant l'opérateur de découpage

L'opérateur de découpage fonctionne de manière similaire à la fonction `range()` que vous avez vue précédemment.

Il accepte également les arguments `start`, `stop`, `step`.

La syntaxe ressemble à ceci : `start:end:step`.

Par exemple :

```python
my_list = [10,20,30,40,50]

my_list2 = my_list[1:3:1]

print(my_list2)

#output
#[20, 30]
```

Dans l'exemple ci-dessus, nous voulions récupérer les éléments commençant par l'index 1 jusqu'à, mais non inclus, l'élément avec l'index 3, en incrémentant un nombre à la fois.

L'indexation en Python commence à 0, donc le premier élément a un index de 0, le deuxième élément a un index de 1, et ainsi de suite.

Lorsque vous voulez imprimer tous les éléments, vous utilisez l'une des deux façons suivantes :

```python
my_list = [10,20,30,40,50]

my_list2 = my_list[:]

#ou...

my_list2 = my_list[::]

#imprimer dans la console
print(my_list2)

#output
#10, 20, 30, 40, 50]
```

Donc, vous utilisez soit un ou deux deux-points pour afficher tous les éléments contenus dans la liste.

Maintenant, pour inverser tous les éléments à l'intérieur de la liste en utilisant l'opérateur de découpage, vous devez inclure le pas.

Dans ce cas, vous utilisez deux deux-points pour représenter les arguments `start` et `end`, et un pas négatif pour décrémenter :

```python
my_list = [10,20,30,40,50]

my_list2 = my_list[::-1]

print(my_list2)

#output
#[50, 40, 30, 20, 10]
```

Dans ce cas, une nouvelle liste est créée, l'ordre original de la liste n'étant pas affecté.

## Comment inverser une liste en Python en utilisant la fonction `reversed()`

Ne confondez pas cela avec la méthode `.reverse()` ! La fonction intégrée `reversed()` inverse l'ordre d'une liste et vous permet d'accéder à chaque élément individuel un à la fois.

```python
my_list = [10,20,30,40,50]

for num in reversed(my_list): 
    print(num)
    
#output
#50
#40
#30
#20
#10
```

La fonction `reversed()` accepte une liste comme argument et retourne un itérable, une version inversée des éléments contenus dans la liste.

Si vous vouliez stocker la valeur de retour de la fonction `reversed()` pour une utilisation ultérieure, vous devriez plutôt l'enfermer dans le constructeur `list()` et assigner la nouvelle liste à une variable, comme ceci :

```python
#liste initiale
my_list = [10,20,30,40,50]

#utiliser la fonction reversed() pour inverser l'ordre de my_list
#stocker la nouvelle liste qui est créée dans la variable my_new_list
my_new_list = list(reversed(my_list))

print(my_new_list)
#output
#[50, 40, 30, 20, 10]
```


## Conclusion

Et voilà - vous connaissez maintenant les bases de l'inversion des listes en Python !

Si vous voulez en savoir plus sur Python, freeCodeCamp propose une [certification Python](https://www.freecodecamp.org/learn/scientific-computing-with-python/)

Dans ce programme basé sur des projets, vous commencerez à partir de zéro. Vous apprendrez les fondamentaux de la programmation et passerez à des sujets plus complexes. À la fin, vous construirez 5 projets pour mettre vos nouvelles compétences en pratique.

Merci d'avoir lu et bon codage !