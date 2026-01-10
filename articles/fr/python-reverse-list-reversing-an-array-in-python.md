---
title: Python Inverser une Liste – Inverser un Tableau en Python
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-09-06T19:36:06.000Z'
originalURL: https://freecodecamp.org/news/python-reverse-list-reversing-an-array-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/pexels-breakingpic-3243.jpg
tags:
- name: Python
  slug: python
seo_title: Python Inverser une Liste – Inverser un Tableau en Python
seo_desc: 'In this article, you will learn how to reverse a list in Python.

  Firstly, I''ll introduce you to lists in Python and you''ll learn how to write them.
  After that, you will see three different ways you can reverse the list items inside
  any list you creat...'
---

Dans cet article, vous apprendrez à inverser une liste en Python.

Tout d'abord, je vous présenterai les listes en Python et vous apprendrez à les écrire. Ensuite, vous verrez trois façons différentes d'inverser les éléments de la liste à l'intérieur de n'importe quelle liste que vous créez.

Voici ce que nous allons couvrir :

1. [Qu'est-ce qu'une liste en Python et comment en créer une](#introduction)
2. [Comment inverser les éléments d'une liste en utilisant la méthode `.reverse()`](#reverse-method)
3. [Comment inverser les éléments d'une liste en utilisant la fonction `reversed()`](#reversed-function)
4. [Comment inverser les éléments d'une liste en utilisant le découpage](#slicing)


## Qu'est-ce qu'une Liste en Python ? Comment Écrire une Liste en Python Exemple <a name="introduction"></a>

Les listes sont un type de données intégré en Python et l'une des structures de données les plus puissantes.

Vous pouvez les considérer comme des conteneurs pour stocker plusieurs collections d'éléments (généralement liés) sous le même nom de variable.

Pour créer une liste en Python, vous devez :

- Donner un nom à la liste.
- Utiliser l'opérateur d'assignation, `=`.
- Inclure `0` ou plus d'éléments de liste à l'intérieur de crochets, `[]` – et veiller à séparer chaque élément de la liste par une virgule.

Les éléments de la liste peuvent être homogènes, ce qui signifie qu'ils sont du même type.

Par exemple, vous pouvez créer une liste de nombres uniquement ou une liste de chaînes de caractères uniquement (ou de texte).

Voici comment vous créeriez une liste de noms :

```python
names = ["Johny", "Lenny", "Jimmy", "Timmy"]

# afficher le contenu de la liste dans la console
print(names)

# vérifier le type de données pour names en utilisant la fonction type()
print(type(names))

# sortie
# ['Johny', 'Lenny', 'Jimmy', 'Timmy']
# <class 'list'>
```

L'exemple ci-dessus a créé une liste de noms avec quatre valeurs : `Johny`, `Lenny`, `Jimmy` et `Timmy`.

Vous pouvez également créer une liste de nombres entiers uniquement :

```python
my_numbers = [1, 2, 3, 4, 5]

# afficher le contenu de la liste dans la console
print(my_numbers)

# vérifier le type de données pour my_numbers en utilisant la fonction type()
print(type(my_numbers))

# sortie
# [1, 2, 3, 4, 5]
# <class 'list'>
```

Les éléments de la liste peuvent également être hétérogènes, ce qui signifie qu'ils peuvent être de différents types de données.

```python
# une liste contenant des chaînes de caractères, des entiers et des flottants (ou des nombres avec un point décimal)

my_information = ["John", "Doe", 34, "London", 1.76]

print(my_information)

# sortie
# ['John', 'Doe', 34, 'London', 1.76]
```

C'est ce qui distingue les listes des tableaux.

Contrairement aux tableaux, qui ne stockent que des éléments du même type, les listes permettent plus de flexibilité.

Les tableaux nécessitent que les éléments soient du même type de données, alors que les listes ne le nécessitent pas.

Les listes sont mutables, ce qui signifie qu'elles sont modifiables et dynamiques – vous pouvez mettre à jour, supprimer et ajouter de nouveaux éléments à la liste à tout moment tout au long de la vie du programme.

## Comment Inverser les Éléments d'une Liste en Utilisant la Méthode `.reverse()` <a name="reverse-method"></a>

La méthode `.reverse()` en Python est une méthode intégrée qui inverse la liste *en place*.

Inverser la liste *en place* signifie que la méthode modifie et change la liste originale. Elle *ne crée pas* une nouvelle liste qui est une copie de l'originale mais avec les éléments de la liste dans l'ordre inverse.

Cette méthode est utile lorsque vous ne vous souciez pas de préserver l'ordre de la liste originale.

La syntaxe générale de la méthode `.reverse()` ressemble à ceci :

```python
list_name.reverse()
```

La méthode `.reverse()` n'accepte aucun argument et n'a pas de valeur de retour – elle met simplement à jour la liste existante.

Voici comment vous utiliseriez la méthode `.reverse()` pour inverser une liste d'entiers :

```python
# liste originale
my_numbers = [1, 2, 3, 4, 5]

# inverser l'ordre des éléments dans my_numbers
my_numbers.reverse()

# afficher le contenu de my_numbers dans la console
print(my_numbers)

# sortie
# [5, 4, 3, 2, 1]
```

Dans l'exemple ci-dessus, l'ordre des éléments de la liste dans la liste originale est inversé, et la liste originale est modifiée et mise à jour.

Et voici comment vous utiliseriez la méthode sur une liste de noms :

```python
names = ["Johny", "Lenny", "Jimmy", "Timmy"]

# inverser l'ordre des éléments dans names
names.reverse()

# afficher le contenu de names dans la console
print(names)

# sortie
# ['Timmy', 'Jimmy', 'Lenny', 'Johny']
```

## Comment Inverser les Éléments d'une Liste en Utilisant la Fonction `reversed()` <a name="reversed-function"></a>

Cette fonction est utile lorsque vous souhaitez accéder aux éléments individuels de la liste dans l'ordre inverse.

La syntaxe générale de la fonction `reversed()` ressemble à ceci :

```python
reversed(list_name)
```

La fonction intégrée `reversed()` en Python retourne un itérateur inversé – un **objet itérable** qui est ensuite utilisé pour récupérer et parcourir tous les éléments de la liste dans l'ordre inverse.

Retourner un objet itérable signifie que la fonction retourne les éléments de la liste dans l'ordre inverse. Elle n'inverse pas la liste en place. Cela signifie qu'elle ne modifie pas la liste originale, ni ne crée une nouvelle liste qui est une copie de l'originale mais avec les éléments de la liste dans l'ordre inverse.

```python
my_numbers = [1, 2, 3, 4, 5]

my_numbers_reversed = reversed(my_numbers)

# afficher la liste originale
print(my_numbers)

# vérifier le type de données de my_numbers_reversed en utilisant la fonction type()
print(type(my_numbers_reversed))

# sortie
# [1, 2, 3, 4, 5]
# <class 'list_reverseiterator'>
```

Vous utilisez la fonction `reversed()` avec une boucle `for` pour itérer à travers les éléments de la liste dans l'ordre inversé. (Si vous avez besoin d'un rappel sur les boucles `for` en Python, lisez [cet article](https://www.freecodecamp.org/news/python-for-loop-example-and-tutorial/))

```python
my_numbers = [1, 2, 3, 4, 5]

for number in reversed(my_numbers):
  print(number)
  
# sortie
# 5
# 4
# 3
# 2
# 1
```

Si vous affichez ensuite le contenu de la liste originale dans la console, vous verrez que l'ordre des éléments est préservé, et la liste originale n'est pas modifiée :

```python
my_numbers = [1, 2, 3, 4, 5]

for number in reversed(my_numbers):
  print(number)

print(my_numbers)

# sortie
# 5
# 4
# 3
# 2
# 1
# [1, 2, 3, 4, 5]
```

C'est parce que la fonction `reversed()` prend une liste comme argument et retourne un itérateur dans l'ordre inverse.

Elle ne fera aucune modification à la liste existante, et elle ne créera pas de nouvelle liste.

Cette fonction n'inverse pas la liste de manière permanente, seulement temporairement pendant l'exécution de la boucle `for` sur la liste originale.

Mais que faire si vous voulez créer une nouvelle liste qui sera une copie de l'originale mais avec les éléments dans l'ordre inverse en utilisant la fonction `reversed()` ?

Vous pouvez passer le résultat de l'opération `reversed()` comme argument à la fonction `list()`, qui convertira l'itérateur en une liste, et stocker le résultat final dans une variable :

```python
my_numbers = [1, 2, 3, 4, 5]

my_numbers_reversed = list(reversed(my_numbers))

# liste originale
print(my_numbers)

# nouvelle liste, qui est une copie de l'originale avec les éléments de la liste dans l'ordre inverse
print(my_numbers_reversed)

# sortie
# [1, 2, 3, 4, 5]
# [5, 4, 3, 2, 1]
```

## Comment Inverser les Éléments d'une Liste en Utilisant le Découpage <a name="slicing"></a>

Une autre façon d'inverser les listes en Python est d'utiliser le découpage.

Le découpage est l'une des façons les plus rapides d'inverser une liste en Python et offre une syntaxe concise. Cela dit, c'est plus une fonctionnalité intermédiaire à avancée et pas très conviviale pour les débutants par rapport à la méthode `.reverse()`, qui est plus intuitive et auto-descriptive.

Passons en revue un aperçu rapide du fonctionnement du découpage.

La syntaxe générale ressemble à ceci :

```python
list_name[start:stop:step]
```

Décomposons cela :

`start` est l'index de début de la tranche, inclusif.

L'indexation en Python et en informatique commence à `0`.

La valeur par défaut de `start` est `0`, et elle prend le premier élément à partir du début de la liste.

Si vous voulez obtenir le premier élément à partir de la fin de la liste, la valeur serait `-1`.

```python
my_numbers = [1,2,3,4,5,]

slicing_my_numbers = my_numbers[-1:]

print(slicing_my_numbers)

# sortie
# [5]
```

`stop` est la position d'index de fin et où vous voulez que le découpage s'arrête, non inclusif – il n'inclut pas l'élément situé à l'index que vous spécifiez.

Par exemple, si vous voulez découper la liste à partir du début jusqu'à l'élément avec l'index `3`, voici ce que vous feriez :

```python
# l'élément à l'index 3 est l'entier 4
my_numbers = [1,2,3,4,5,]

slicing_my_numbers = my_numbers[:3]

# l'entier 4 n'est pas inclus dans le résultat
print(slicing_my_numbers)

# sortie
# [1, 2, 3]
```

`step` est la valeur d'incrément, avec la valeur par défaut étant `1`.

Maintenant, en ce qui concerne l'utilisation du découpage pour inverser une liste, vous devrez utiliser l'opérateur de découpage inverse `[::-1]` syntaxe. Cela définit le pas à `-1` et obtient tous les éléments de la liste dans l'ordre inverse.

```python
# liste originale
my_numbers = [1,2,3,4,5]

# inverser la liste originale
my_numbers_reversed = my_numbers[::-1]

# afficher la liste originale
print(my_numbers)

# afficher la nouvelle liste avec les éléments de la liste originale dans l'ordre inverse
print(my_numbers_reversed)

# sortie
# [1, 2, 3, 4, 5]
# [5, 4, 3, 2, 1]
```

L'opérateur de découpage ne modifie pas la liste originale. Il retourne plutôt une nouvelle liste, qui est une copie des éléments de la liste originale dans l'ordre inverse.

## Conclusion

Et voilà ! Vous savez maintenant comment inverser n'importe quelle liste en Python.

J'espère que vous avez trouvé ce tutoriel utile.

Pour en savoir plus sur le langage de programmation Python, consultez la [certification Python](https://www.freecodecamp.org/learn/scientific-computing-with-python/) de freeCodeCamp.

Vous commencerez par les bases et apprendrez de manière interactive et conviviale pour les débutants. Vous construirez également cinq projets à la fin pour mettre en pratique et renforcer ce que vous avez appris.

Merci d'avoir lu et bon codage !