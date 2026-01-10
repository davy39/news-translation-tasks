---
title: Python List .append() – Comment ajouter un élément à une liste en Python
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2022-04-14T20:03:38.000Z'
originalURL: https://freecodecamp.org/news/python-list-append-how-to-add-an-item-to-a-list-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/python-append--1-.png
tags:
- name: Python
  slug: python
seo_title: Python List .append() – Comment ajouter un élément à une liste en Python
seo_desc: 'Lists are one of the most useful and versatile data types available in
  Python. Lists are a collection of arbitrary objects, just like arrays in other programming
  languages.

  In this tutorial you will learn:


  An overview of lists and how they are defin...'
---

Les listes sont l'un des types de données les plus utiles et polyvalents disponibles en Python. Les listes sont une collection d'objets arbitraires, tout comme les tableaux dans d'autres langages de programmation.

Dans ce tutoriel, vous apprendrez :

* Un aperçu des listes et de leur définition.
* Des méthodes pour insérer des données dans une liste en utilisant : `list.append()`, `list.extend` et `list.insert()`.
* La syntaxe, des exemples de code et la sortie pour chaque méthode d'insertion de données.
* Comment implémenter une pile en utilisant des méthodes d'insertion et de suppression de liste.

### Prérequis

Pour ce tutoriel, vous avez besoin de :

* Python 3.
* Un éditeur de code de votre choix.

## Les listes en Python

Les listes ont les propriétés suivantes qui les rendent puissantes et flexibles :

* Les listes sont ordonnées.
* Les listes sont accessibles en utilisant l'index. Le premier index commence à `0`.
* Les listes sont mutables et dynamiques, ce qui signifie qu'elles peuvent être modifiées après leur création.

### Comment créer une liste en Python

Vous créez une liste en utilisant des crochets en Python.

Nous pouvons les laisser vides et fournir des valeurs plus tard dans le programme :

```python
# Créer une liste vide

programming_lang = []
```

Nous pouvons également fournir des valeurs lors de la création d'une liste :

```python
# Créer une liste remplie

programming_lang = ['P','Y','T','H','O','N']
```

Cela créerait une liste comme montré dans l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-63.png)
_Éléments de la liste contre les index_

### Comment accéder aux éléments d'une liste

Comme les éléments de la liste sont ordonnés, vous pouvez y accéder en utilisant leur index.

Syntaxe : `list[index]`.

Dans l'image ci-dessous, "P" est à l'index "0" tandis que "H" est à l'index "3".

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-63.png)

Écrivons un court programme pour définir une liste et accéder à ses éléments :

```python
programming_lang = ['P','Y','T','H','O','N']

print(programming_lang)

print("À l'index 0 :", programming_lang[0])
print("À l'index 3 :",programming_lang[3])
```

**Sortie :**

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-65.png)

Vous pouvez également accéder aux éléments en utilisant un index négatif, où `-1` représente le dernier élément de la liste. Si nous voulions accéder au dernier élément de la liste ci-dessus, nous pourrions également utiliser l'index `-1` :

```python
programming_lang = ['P','Y','T','H','O','N']

print(programming_lang)

print("À l'index -1 :", programming_lang[-1])
print("À l'index -5 :",programming_lang[-5])
```

**Sortie :**

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-66.png)

### Comment trouver la longueur d'une liste

Nous pouvons facilement trouver la longueur d'une liste en utilisant la méthode `len()`.

```
programming_lang = ['P','Y','T','H','O','N']

print("Longueur de la liste : ",len(programming_lang))
```

**Sortie :**

![Trouver la longueur d'une liste.](https://www.freecodecamp.org/news/content/images/2022/04/image-67.png)
_Trouver la longueur d'une liste._

## Méthodes pour ajouter des éléments à une liste

Nous pouvons étendre une liste en utilisant l'une des méthodes suivantes :

* `list.insert()` – insère un seul élément n'importe où dans la liste.
* `list.append()` – ajoute toujours des éléments (chaînes, nombres, listes) à la fin de la liste.
* `list.extend()` – ajoute des éléments itérables (listes, tuples, chaînes) à la fin de la liste.

### Comment insérer des éléments dans une liste avec `insert()`

Vous pouvez insérer des éléments dans une liste à n'importe quel index en utilisant la méthode `insert()`. Il existe d'autres méthodes d'insertion et nous les examinerons plus tard dans cet article.

Syntaxe de insert : `insert(index, element)`.

**Exemple de insert() :**

```
# créer une liste de nombres impairs
odd_n = [1,3,5,7,9]

# '21' est inséré à l'index 3 (4ème position)
odd_n.insert(3, 21)


print('Liste de nombres impairs :', odd_n)


```

Avant l'insertion :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-76.png)

Après l'insertion :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-77.png)

**Sortie :**

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-69.png)

### Comment ajouter un élément à une liste en utilisant `list.append()`

Nous pouvons ajouter un **seul élément** à la fin de la liste en utilisant `list.append()`.

**Syntaxe** : `list.append(item)`.

**Exemple :**

```python
# liste de cultures
crops = ['maïs', 'blé', 'coton']

# Ajouter 'canne' à la liste
crops.append('canne')

print('Liste de cultures mise à jour : ', crops)
```

**Sortie :**

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-71.png)

⚠️ Notez que tenter d'ajouter plus d'un élément donne une exception, car `list.append()` ne prend qu'un seul argument.

![Impossible d'ajouter plusieurs éléments en utilisant list.append().](https://www.freecodecamp.org/news/content/images/2022/04/image-70.png)
_Impossible d'ajouter plusieurs éléments en utilisant `list.append()`._

### Comment ajouter plusieurs éléments dans une liste en utilisant `list.extend()`

Nous pouvons ajouter plusieurs éléments à une liste en utilisant la méthode `extend()`.

L'exemple ci-dessous combine deux listes en une seule liste.

```python
# créer une liste
even_numbers = [2, 4, 8]

# créer une autre liste
more_even_numers = [100, 400]

# ajouter tous les éléments de even_numbers à more_even_numbers
even_numbers.extend(more_even_numers)


print('Liste après extend() :', even_numbers)

```

**Sortie :**

![Extension d'une liste en utilisant extend().](https://www.freecodecamp.org/news/content/images/2022/04/image-72.png)
_Extension d'une liste en utilisant `extend()`._

### Autres moyens d'étendre les listes en Python :

#### Découpage de liste

Le découpage nous permet de sélectionner une plage de valeurs dans une liste.

La syntaxe est montrée ci-dessous :

`list[starting index:upto index]`

Par exemple,

* list[1:3] retournerait les éléments commençant à l'index 1 jusqu'à (non inclus) l'index 3.
* L'index de gauche manquant implique de commencer à l'index 0.
    * `list[:len(list)]` signifie commencer à l'index 0 et continuer jusqu'à la fin.
* L'index de droite manquant implique jusqu'au dernier index.
    * `list[0:]` implique de commencer à l'index 0 jusqu'au dernier élément.

Voyons comment nous pouvons ajouter des listes en utilisant le découpage.

**Exemple** :

```python
A = [99, 100, 101]
B = [103, 104, 105]

# en commençant par le dernier index +1, ajouter les éléments de la liste B

A[len(A):] = B

print('A =', A)
```

**Sortie :**

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-78.png)

#### Combinaison de tableaux en utilisant l'opérateur +

Combinons deux tableaux `odd` et `even` en une seule liste en utilisant l'opérateur `+`.

**Exemple :**

```python
odd = [1, 3, 5, 7]
even = [2, 4, 6, 8]

odd += even    # odd = odd + even


# Sortie : [1, 2, 3, 4]
print('odd et even combinés =', odd)
```

**Sortie :**

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-79.png)

### Comment remplir une liste vide en utilisant `for loop` et `append()`

Il existe deux façons de remplir des listes vides : en utilisant une boucle `for` avec `append()` et en utilisant la compréhension de liste.

Utilisons d'abord `for` loop avec `append()`.

**Exemple :**

Dans cet exemple, nous calculons l'aire d'un carré et ajoutons le résultat dans un tableau.

```python
# Retourner l'aire du carré
# Aire du carré = longueur x longueur

def square_area(side_length):
     result = []
     for length in side_length:
         result.append(length*length)
     return result


lengths = [1, 4, 9, 20]
print(square_area(lengths))

```

**Sortie :**

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-80.png)

Nous pouvons rendre le code ci-dessus plus efficace en sautant complètement la combinaison `for loop - append()` et en utilisant la compréhension de liste à la place. Voyons comment dans la section suivante.

### Comment remplir une liste vide en utilisant la compréhension de liste

La compréhension de liste rend le code simple et lisible en combinant la boucle `for` et `append()` en une seule ligne.

Nous pouvons modifier notre exemple précédent pour atteindre la compréhension de liste. Remarquez les lignes commentées ici :

```python
# Retourner l'aire du carré
# Aire du carré = longueur x longueur

def square_area(side_length):
     #result = []
     #for length in side_length:
     #    result.append(length*length)
     return [length*length for length in side_length]


lengths = [1, 4, 9, 20]
print(square_area(lengths))

```

**Sortie :**

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-81.png)

Les deux méthodes pour remplir une liste vide sont valides et adaptées à différents scénarios.

## `Append()` vs `Insert()` vs `Extend()`

`Append()` ajoute toujours un seul élément à la fin d'une liste. Il est utile lorsqu'un seul élément doit être inséré.

Mais si vous devez faire plusieurs ajouts, `extend()` est une meilleure option car il ajoute des éléments itérables en un seul lot.

Vous devez utiliser `Insert()` lorsque l'insertion est requise à un index spécifique ou à une plage d'index.

## Comment implémenter une pile (LIFO)

### Qu'est-ce qu'une pile (LIFO) ?

Une pile est un arrangement d'éléments qui suit un ordre dernier entré, premier sorti. L'élément qui arrive en dernier est celui qui sort en premier. Un exemple de pile serait la pile d'annulation/rétablissement dans les applications de retouche photo.

Le diagramme ci-dessous explique visuellement une pile.

Vous pouvez ajouter un élément en utilisant `append()`.

Vous pouvez supprimer un élément en utilisant `pop()`. Voir les détails de la méthode `pop()` [ici](https://docs.python.org/3/tutorial/datastructures.html#:~:text=no%20such%20item.-,list.pop(%5Bi%5D),-Remove%20the%20item).

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-83.png)
_Visualisation de la pile_

### Codage des piles

Créons une classe de pile où nous déclarons d'abord une liste vide dans la méthode `init`.

La méthode `push()` ajoute un élément à la liste.

La méthode `pop()` supprime le dernier élément de la liste en utilisant `pop()`. Si aucun élément n'est présent dans la liste, une exception sera levée.

La méthode __`len`__ détermine la longueur de la pile.

Enfin, __`repr`**__** retourne la sortie dans un format lisible.

**Définition de la classe :**

```python
class Stack:
    def __init__(stack_t):
        stack_t._items = []

    def push(stack_t, item):
        stack_t._items.append(item)

    def pop(stack_t):
        try:
            return stack_t._items.pop()
        except IndexError:
            print("La pile est vide, tous les éléments sont supprimés")

    def __len__(stack_t):
        return len(stack_t._items)

    def __repr__(stack_t):
        return f"stack ({stack_t._items})"


```

**Corps du code :**

Appelons les fonctions de la classe et voyons la sortie en action.

```python
stack = Stack()

# Pousser des éléments au sommet de la pile
stack.push(3)
stack.push(5)
stack.push(8)
stack.push(99)

 # Imprimer la pile

print(stack)

# Trouver la longueur de la pile
print("La longueur de la pile est :" ,len(stack))


# Retirer des éléments de la pile
print("Retrait du dernier élément")
stack.pop()
print(stack)

print("Retrait du dernier élément à nouveau")
stack.pop()
print(stack)

print("Enfin, la pile est")

print(stack)
```

**Sortie :**

Nous avons ajouté 3, 5, 8, 99 à la pile. Ensuite, nous avons imprimé la pile et sa longueur. Par la suite, nous avons retiré deux éléments et imprimé la pile à chaque fois.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-82.png)

## Conclusion

Dans ce tutoriel, nous avons appris les méthodes de création de listes. Nous avons également examiné quelques exemples ainsi qu'une implémentation pratique de piles pour voir comment tout cela fonctionne.

Quelle est la chose préférée que vous avez apprise dans ce tutoriel ? Faites-le moi savoir sur [Twitter](https://twitter.com/hira_zaira) !

Vous pouvez lire mes autres articles [ici](https://www.freecodecamp.org/news/author/zaira/).