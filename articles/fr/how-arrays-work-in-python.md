---
title: Comment fonctionnent les tableaux en Python – Méthodes de tableau expliquées
  avec des exemples de code
subtitle: ''
author: David Fagbuyiro
co_authors: []
series: null
date: '2023-07-12T22:19:23.000Z'
originalURL: https://freecodecamp.org/news/how-arrays-work-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/pexels-andreas-fickl-4405941.jpg
tags:
- name: arrays
  slug: arrays
- name: Python
  slug: python
seo_title: Comment fonctionnent les tableaux en Python – Méthodes de tableau expliquées
  avec des exemples de code
seo_desc: "In this tutorial, you'll learn what an array is in Python. You'll also\
  \ learn some possible ways to add elements to an existing array. \nIn Python, there\
  \ is no need to use a specific data type for arrays. You can simply use a list with\
  \ all the attribut..."
---

Dans ce tutoriel, vous apprendrez ce qu'est un tableau en Python. Vous apprendrez également quelques façons possibles d'ajouter des éléments à un tableau existant. 

En Python, il n'est pas nécessaire d'utiliser un type de données spécifique pour les tableaux. Vous pouvez simplement utiliser une liste avec tous les attributs d'un tableau. 

Si vous souhaitez créer un tableau qui inclut à la fois des entiers et des nombres à virgule flottante, vous pouvez utiliser le module array de Python.

## Qu'est-ce qu'un tableau ?

Un tableau est un type unique de variable qui a la capacité de stocker plus d'une valeur à la fois. 

Supposons que vous avez une liste d'objets comme des noms de pays. Vous pourriez stocker les pays dans des variables séparées comme suit :

```python
Country1 = "Germany";

Country2 = "France";

Country3 = "Denmark";

```

Mais supposons que vous vouliez rechercher dans tous les pays pour en découvrir un certain. Et si vous aviez 200 pays au lieu de seulement 3 ?

L'alternative est de stocker toutes ces valeurs dans un tableau.

Les tableaux sont utiles pour stocker et manipuler plusieurs valeurs du même type de données. Ils agissent comme une variable qui peut contenir une collection de valeurs, toutes du même type. Ces valeurs sont stockées ensemble dans une mémoire contiguë.

## Méthodes de tableau Python

Vous pouvez utiliser diverses méthodes intégrées de Python lorsque vous travaillez avec des listes et des tableaux. Voici les méthodes que vous pouvez utiliser sur les tableaux et les listes en Python.

### La méthode `Append()`

Si vous souhaitez ajouter un élément à la fin d'une liste, vous pouvez utiliser la méthode append.

**Exemple :**

```python
fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')
print(fruits)  


# Output: ['apple', 'banana', 'cherry', 'orange']

```

La méthode `append()` est utilisée pour ajouter des éléments à la fin d'une liste. Dans ce cas, 'orange' est ajouté à la liste `fruits`, ce qui donne une liste contenant quatre éléments : 'apple', 'banana', 'cherry' et 'orange'.

Voici un autre exemple pour vous :

Créons un tableau contenant les noms de voitures :

```python

cars = ["Lexus", "Toyota", "Mercedez"]

```

Vous pouvez utiliser la méthode `append()` pour ajouter un nouvel élément à une liste/tableau existant comme vu ci-dessous.

```python
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)


# Output: ['apple', 'banana', 'cherry', 'orange']

```

Output:

```
["Lexus", "Toyota", "Mercedez", "Honda"]

```

### La méthode `Clear()`

La méthode `clear()` supprime tous les éléments de la liste, comme son nom l'indique.

**Exemple :**

Voici un exemple utilisant la méthode `clear()` :

```python
cars = ["Lexus", "Toyota", "Mercedez"]

cars.clear()

print(cars)

```

Output:

Basé sur l'explication de la méthode `clear()` ci-dessus, le résultat de cette expression sera [] vide car nous avons vidé toute la liste.

### La méthode `Copy()`

Cette fonction crée et retourne une copie identique de la liste originale.

**Exemple :**

```python
fruits = ["apple", "banana", "cherry"]
fruits_copy = fruits.copy()
print(fruits_copy)


# Output: ['apple', 'banana', 'cherry']

```

Dans l'exemple ci-dessus, la méthode copy() crée un nouveau tableau appelé fruits_copy, qui est une copie superficielle du tableau fruits. Modifier le tableau fruits_copy n'affectera pas le tableau fruits original.

Voici un autre exemple utilisant la méthode `copy()` :

```python
cars = ["Lexus", "Toyota", "Mercedez"]


x = cars.copy()


print(x)


# Output de l'utilisation de la méthode copy () sera :


["Lexus", "Toyota", "Mercedez"]

```

### La méthode `Count()`

Cette méthode retourne le nombre d'éléments avec la valeur spécifiée.

**Exemple :** 

```python
fruits = ["apple", "banana", "cherry", "banana"]
count = fruits.count("banana")
print(count)


# Output: 2

```

Le code ci-dessus crée une liste appelée **fruits** avec quatre éléments : 'apple', 'banana', 'cherry' et une autre 'banana'. La méthode `count()` est ensuite utilisée sur la liste `fruits` pour compter le nombre d'occurrences de l'élément 'banana'. Elle retourne le compte, qui dans ce cas est 2, car 'banana' apparaît deux fois dans la liste.

Enfin, la valeur du compte est imprimée sur la console, ce qui donne le résultat : 2.

Voici un autre exemple d'utilisation de la méthode `count()` :

```python
# Retourne le nombre de fois où la valeur "Lexus" apparaît dans la liste des voitures.

cars = ["Lexus", "Toyota", "Mercedez", "Lexus"]

x = cars.count("Lexus")

print(x)

```

Le résultat de ceci retournerait l'entier "2" car "Lexus" apparaît deux fois dans la liste des voitures.

### La méthode `Extend()`

Avec cette méthode, vous pouvez ajouter les éléments d'une liste (ou tout itérable) à la fin de la liste actuelle.

**Exemple :**

```python
fruits = ["apple", "banana", "cherry"]
additional_fruits = ["orange", "grape"]
fruits.extend(additional_fruits)
print(fruits)

# Output: ['apple', 'banana', 'cherry', 'orange', 'grape']

```

Dans l'exemple ci-dessus, la méthode `extend()` est utilisée pour ajouter les éléments de la liste `additional_fruits` au tableau `fruits`. Le tableau résultant contient tous les éléments des deux tableaux.

Notez que la méthode `extend()` modifie le tableau original en place et ne retourne pas un nouveau tableau.

### La méthode `index()`

Cette méthode retourne l'index du premier élément avec la valeur spécifiée.

```python
fruits = ["apple", "banana", "cherry"]
index = fruits.index("banana")

print(index)

# Output: 1

```

Le code ci-dessus crée une liste de **fruits** contenant 'apple', 'banana' et 'cherry'. Il trouve ensuite la position de l'index de 'banana' dans la liste et l'assigne à la variable 'index'. Enfin, il imprime la valeur de 'index', qui dans ce cas serait 1.

### La méthode `insert()`

Cette méthode de tableau ajoute un élément à la position spécifiée.

```python
numbers = [1, 2, 3, 5, 6]
numbers.insert(3, 4)
print(numbers)

# Output: [1, 2, 3, 4, 5, 6]

```

D'après le code ci-dessus, nous avons un tableau numbers avec les éléments [1, 2, 3, 5, 6]. Nous voulons insérer le nombre 4 à l'index 3 (qui est la quatrième position dans le tableau, car Python est indexé à 0). En appelant insert(3, 4), nous insérons l'élément 4 à l'index spécifié, et les éléments existants sont déplacés vers la droite pour faire de la place pour le nouvel élément. Le tableau résultant est [1, 2, 3, 4, 5, 6].

### La méthode `pop()`

Cette méthode supprime l'élément à la position spécifiée.

**Exemple** :

```python
# Pour supprimer un élément d'un tableau/liste, vous pouvez utiliser la méthode pop().

# Supprimer le deuxième élément du tableau des voitures :

cars = ["Lexus", "Toyota", "Mercedez"]

cars.pop(2)

print(cars)

```

Et voici le résultat :

```python
['Lexus', 'Toyota']
```

Le code ci-dessus supprime le deuxième élément du tableau 'cars' en utilisant la méthode 'pop()' puis imprime le tableau mis à jour.

Voici un autre exemple utilisant la méthode pop() :

```python
# Pour supprimer un élément d'un tableau/liste, vous pouvez utiliser la méthode pop().

# Supprimer le deuxième élément du tableau des voitures :

cars = ["Lexus", "Toyota", "Mercedez"]

cars.pop(2)

print(cars)

```

Output:

```

['Lexus', 'Toyota']

```

Le code supprime le deuxième élément du tableau `cars` en utilisant la méthode `pop()` puis imprime le tableau modifié. Le tableau résultant contiendra uniquement les premier et troisième éléments : ['Lexus', 'Toyota'].

### La méthode `remove()`

Cette méthode supprime le premier élément avec la valeur spécifiée.

**Exemple :**

```python
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)

# Output Below:

["apple", "cherry"]

```

Le code ci-dessus crée une liste appelée `fruits` avec trois éléments : 'apple', 'banana' et 'cherry'. La méthode `remove()` est ensuite utilisée pour supprimer l'élément 'banana' de la liste. 

Après avoir supprimé 'banana', la liste mise à jour est imprimée en utilisant la fonction `print()`. Le résultat sera `['apple', 'cherry']`, car 'banana' n'est plus présent dans la liste.

Voici un autre exemple utilisant la méthode `remove()` :

```python
cars = ["Lexus", "Toyota", "Mercedez"]

cars.remove("Toyota")

print(cars)

```

La fonction **remove()** peut également être utilisée pour supprimer un élément d'un tableau, mais il faut noter qu'elle ne supprime que la première instance de la valeur spécifiée d'une liste.

### La méthode `reverse()`

Cette méthode inverse l'ordre de la liste.

**Exemple :**

```python
fruits = ["apple", "banana", "cherry"]
fruits.reverse()
print(fruits)


# Output: ['cherry', 'banana', 'apple']

```

Le code ci-dessus crée une liste appelée fruits avec trois éléments : 'apple', 'banana' et 'cherry'. Ensuite, la méthode `reverse()` est appelée sur la liste fruits, ce qui inverse l'ordre de ses éléments. Enfin, la liste inversée est imprimée en utilisant la fonction print(), ce qui donne le résultat ['cherry', 'banana', 'apple']. Cela signifie que l'ordre original de la liste des fruits a été inversé.

### La méthode `sort()`

Cette méthode trie la liste, comme son nom l'indique.

**Exemple :**

```python
numbers = [4, 2, 1, 3]

numbers.sort()

print(numbers)

# Output: [1, 2, 3, 4]

```

Le code ci-dessus crée une liste appelée `numbers` avec les éléments `[4, 2, 1, 3]`. La méthode `sort()` est ensuite appelée sur la liste `numbers`, ce qui trie les éléments par ordre croissant. Après le tri, la liste `numbers` devient `[1, 2, 3, 4]`. Enfin, la liste triée est imprimée sur la console en utilisant `print(numbers)`, ce qui donne `[1, 2, 3, 4]`.

La méthode `sort()` en Python trie les éléments d'une liste par ordre croissant par défaut. Si vous souhaitez trier la liste par ordre décroissant, vous pouvez passer le paramètre `reverse=True` à la méthode `sort()`.

Voici un exemple de la façon de trier la liste `numbers` par ordre décroissant :

```python
numbers = [4, 2, 1, 3]

numbers.sort(reverse=True)

print(numbers)

# Output

[4, 3, 2, 1]

```

En passant `reverse=True` comme argument à la méthode `sort()`, la liste est triée par ordre décroissant.

## Conclusion

Espérons qu'après avoir lu cet article, vous devriez maintenant avoir une compréhension de base de ce qu'est un tableau en Python. 

Vous devriez également connaître les méthodes de tableau Python de base que vous utiliserez pour modifier un tableau ou une liste et comment les utiliser.