---
title: 'Les listes Python expliquées : Len, Pop, Index et Compréhension de liste'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/python-lists-explained-len-pop-index-and-list-comprehension
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ced740569d1a4ca34ee.jpg
tags:
- name: programming languages
  slug: programming-languages
- name: Python
  slug: python
- name: toothbrush
  slug: toothbrush
seo_title: 'Les listes Python expliquées : Len, Pop, Index et Compréhension de liste'
seo_desc: 'Lists in Python are similar to arrays in JavaScript. They are one of the
  built in data types in Python used to store collections of data.

  Basic usage

  How to create a list

  An empty list is created using a pair of square brackets:

  >>> empty_list = []

  >...'
---

Les listes en Python sont similaires aux tableaux en JavaScript. Elles font partie des types de données intégrés en Python utilisés pour stocker des collections de données.

## Utilisation de base

### Comment créer une liste

Une liste vide est créée en utilisant une paire de crochets :

```shell
>>> empty_list = []
>>> type(empty_list)
<class 'list'>
>>> len(empty_list)
0
```

Une liste peut être créée avec des éléments en enfermant une liste séparée par des virgules d'éléments avec des crochets. Les listes permettent aux éléments d'être de différents types (hétérogènes) mais sont le plus souvent d'un seul type (homogènes) :

```shell
>>> homogeneous_list = [1, 1, 2, 3, 5, 8]
>>> type(homogeneous_list)
<class 'list'>
>>> print(homogeneous_list)
[1, 1, 2, 3, 5, 8]
>>> len(homogeneous_list)
6
>>> heterogeneous_list = [1, "Hello Campers!"]
>>> print(heterogeneous_list)
[1, "Hello Campers!"]
>>> len(heterogeneous_list)
2
```

Le constructeur `list` peut également être utilisé pour créer une liste :

```shell
>>> empty_list = list()                            # Crée une liste vide
>>> print(empty_list)
[]
>>> list_from_iterable = list("Hello campers!")    # Crée une liste à partir d'un itérable.
>>> print(list_from_iterable)
['H', 'e', 'l', 'l', 'o', ' ', 'c', 'a', 'm', 'p', 'e', 'r', 's', '!']
```

Vous pouvez également utiliser la compréhension de liste pour créer des listes, ce que nous aborderons plus tard dans l'article.

### Accéder aux éléments d'une liste

```shell
>>> my_list = [1, 2, 9, 16, 25]
>>> print(my_list)
[1, 2, 9, 16, 25]
```

_Indexation à partir de zéro_

```shell
>>> my_list[0]
1
>>> my_list[1]
2
>>> my_list[2]
9
```

_Indexation avec wrap around_

```shell
>>> my_list[-1]
25
>>> my_list[-2]
16
```

_Déballage des listes pour python-3_

```shell
>>> print(*my_list)
1 2 9 16 25
```

### Les listes sont mutables

Les `listes` sont des conteneurs mutables. Les conteneurs mutables sont des conteneurs qui permettent des modifications des objets contenus dans le conteneur.

Les éléments d'une `liste` peuvent être extraits et réarrangés en utilisant une autre `liste` comme index.

```shell
>>> my_list = [1, 2, 9, 16, 25, 34, 53, 21]
>>> my_index = [5, 2, 0]
>>> my_new_list = [my_list[i] for i in my_index]
>>> print(my_new_list)
[34, 9, 1]
```

## Méthodes de liste

### `len()`

La méthode `len()` retourne la longueur d'un objet, qu'il s'agisse d'une liste, d'une chaîne, d'un tuple ou d'un dictionnaire.

`len()` prend un argument, qui peut être une séquence (comme une chaîne, des bytes, un tuple, une liste ou une plage) ou une collection (comme un dictionnaire, un ensemble ou un ensemble gelé).

```text
list1 = [123, 'xyz', 'zara'] # liste
print(len(list1)) # affiche 3 car il y a 3 éléments dans list1

str1 = 'basketball' # chaîne
print(len(str1)) # affiche 10 car str1 est composée de 10 caractères

tuple1 = (2, 3, 4, 5) # tuple 
print(len(tuple1)) # affiche 4 car il y a 4 éléments dans tuple1

dict1 = {'name': 'John', 'age': 4, 'score': 45} # dictionnaire
print(len(dict1)) # affiche 3 car il y a 3 paires clé-valeur dans dict1
```

### `index()`

`index()` retourne la première occurrence/index de l'élément dans la liste donné comme argument à la fonction.

```py
numbers = [1, 2, 2, 3, 9, 5, 6, 10]
words = ["I", "love", "Python", "I", "love"]

print(numbers.index(9)) # 4
print(numbers.index(2)) # 1
print(words.index("I")) # 0
print(words.index("am")) # retourne une ValueError car 'am' n'est pas dans la liste `words`
```

Ici, la première sortie est très évidente, mais la deuxième et la troisième peuvent sembler déroutantes au premier abord. Mais rappelez-vous que `index()` retourne la première occurrence de l'élément et donc dans ce cas, `1` et `0` sont les indices où `2` et `"I"` apparaissent en premier dans les listes respectivement.

De plus, si un élément n'est pas trouvé dans la liste, une `ValueError` est retournée comme dans le cas de l'indexation de `"am"` dans la liste `words`.

**Arguments optionnels**

Vous pouvez également utiliser des arguments optionnels pour limiter votre recherche à une sous-séquence particulière de la liste :

```py
words = ["I", "am", "a", "I", "am", "Pythonista"]

print(words.index("am", 2, 5)) # 4
```

Bien que l'élément soit recherché entre les indices 2 (inclus) et 5 (non inclus), l'index retourné est calculé par rapport au début de la liste complète plutôt qu'à l'argument de départ.

### `pop()`

La méthode `pop()` supprime et retourne le dernier élément d'une liste. 

Il existe un paramètre optionnel qui est l'index de l'élément à supprimer de la liste. Si aucun index n'est spécifié, `pop()` supprime et retourne le dernier élément de la liste. 

Si l'index passé à la méthode `pop()` n'est pas dans la plage, elle lance l'exception `IndexError: pop index out of range`.

```py
cities = ['New York', 'Dallas', 'San Antonio', 'Houston', 'San Francisco'];

print "City popped is: ", cities.pop() # City popped is: San Francisco
print "City at index 2 is  : ", cities.pop(2) # City at index 2 is: San Antonio
```

**Fonctionnalité de base de la pile**

La méthode `pop()` est souvent utilisée en conjonction avec `append()` pour implémenter une fonctionnalité de pile de base dans une application Python :

```py
stack = []

for i in range(5):
    stack.append(i)

while len(stack):
    print(stack.pop())
```

### Compréhension de liste

La compréhension de liste est une manière de parcourir une liste pour produire une nouvelle liste basée sur certaines conditions. Cela peut être déroutant au premier abord, mais une fois que vous êtes habitué à la syntaxe, c'est très puissant et rapide.

La première étape pour apprendre à utiliser la compréhension de liste est de regarder la manière traditionnelle de parcourir une liste. Voici un exemple simple qui retourne une nouvelle liste de nombres pairs.

```python
# Exemple de liste pour la démonstration
some_list = [1, 2, 5, 7, 8, 10]

# Liste vide qui sera remplie avec une boucle
even_list = []

for number in some_list:
  if number % 2 == 0:
    even_list.append(number)

# even_list est maintenant égale à [2, 8, 10]
```

D'abord, une liste est créée avec quelques nombres. Vous créez ensuite une liste vide qui contiendra vos résultats de la boucle. Dans la boucle, vous vérifiez si chaque nombre est divisible par 2 et, si c'est le cas, vous l'ajoutez à la `even_list`. Cela a pris 5 lignes de code, sans inclure les commentaires et les espaces blancs, ce qui n'est pas beaucoup dans cet exemple.

Voici maintenant l'exemple de compréhension de liste.

```python
# Exemple de liste pour la démonstration
some_list = [1, 2, 5, 7, 8, 10]

# Compréhension de liste
even_list = [number for number in some_list if number % 2 == 0]

# even_list est maintenant égale à [2, 8, 10]
```

Un autre exemple, avec les mêmes deux étapes : ce qui suit créera une liste de nombres qui correspondent aux nombres dans `my_starting_list` multipliés par 7.

```py
my_starting_list = [1, 2, 3, 4, 5, 6, 7, 8]
my_new_list = []

for item in my_starting_list:
my_new_list.append(item * 7)
```

Lorsque ce code est exécuté, la valeur finale de `my_new_list` est : `[7, 14, 21, 28, 35, 42, 49, 56]`

Un développeur utilisant la compréhension de liste pourrait obtenir le même résultat en utilisant la compréhension de liste suivante, ce qui donne la même `my_new_list`.

```py
my_starting_list = [1, 2, 3, 4, 5, 6, 7, 8]

my_new_list = [item * 7 for item in my_starting_list]
```

Une formule simple pour écrire de manière compréhensible une liste est :

`my_list = [{operation avec l'entrée n} for n in {itérable python}]`

Remplacez `{operation avec l'entrée n}` par la manière dont vous souhaitez modifier l'élément retourné par l'itérable. L'exemple ci-dessus utilise `n * 7` mais l'opération peut être aussi simple ou aussi complexe que nécessaire.

Remplacez `{itérable python}` par n'importe quel itérable. Les types de séquence seront les plus courants. Une liste a été utilisée dans l'exemple ci-dessus, mais les tuples et les plages sont également courants.

La compréhension de liste ajoute un élément d'une liste existante à une nouvelle liste si une certaine condition est remplie. C'est plus propre, mais c'est aussi beaucoup plus rapide dans la plupart des cas. Dans certains cas, la compréhension de liste peut nuire à la lisibilité, donc le développeur doit peser ses options lorsqu'il choisit d'utiliser la compréhension de liste.

**Exemples de compréhension de liste avec des conditionnelles**

Le flux de contrôle dans les compréhensions de liste peut être contrôlé en utilisant des conditionnelles. Par exemple :

```py
only_even_list = [i for i in range(13) if i%2==0]
```

Cela est équivalent à la boucle suivante :

```py
only_even_list = list()
for i in range(13):
  if i%2 == 0:
    only_even_list.append(i)
```

La compréhension de liste peut également contenir des conditions if imbriquées. Considérez la boucle suivante :

```py
divisible = list()
for i in range(50):
  if i%2 == 0:
    if i%3 == 0:
      divisible.append(i)
```

En utilisant la compréhension de liste, cela peut s'écrire :

```py
divisible = [i for i in range(50) if i%2==0 if i%3==0]
```

L'instruction If-Else peut également être utilisée avec la compréhension de liste.

```py
list_1 = [i if i%2==0 else i*-1 for i in range(10)]
```

#### **Plus d'informations :**

* [Les meilleurs exemples de code Python](https://www.freecodecamp.org/news/python-example/)