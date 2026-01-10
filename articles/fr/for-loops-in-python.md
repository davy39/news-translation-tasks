---
title: Les boucles For en Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/for-loops-in-python
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d22740569d1a4ca3615.jpg
tags:
- name: Python
  slug: python
- name: toothbrush
  slug: toothbrush
seo_title: Les boucles For en Python
seo_desc: 'For Loop Statements

  Python utilizes a for loop to iterate over a list of elements. Unlike C or Java,
  which use the for loop to change a value in steps and access something such as an
  array using that value.

  For loops iterate over collection based dat...'
---

## **Les instructions de boucle For**

Python utilise une boucle for pour itérer sur une liste d'éléments. Contrairement à C ou Java, qui utilisent la boucle for pour modifier une valeur par étapes et accéder à quelque chose comme un tableau en utilisant cette valeur.

Les boucles for itèrent sur des structures de données basées sur des collections comme les listes, les tuples et les dictionnaires.

La syntaxe de base est :

```python
for value in list_of_values:
  # utiliser value dans ce bloc
```

En général, vous pouvez utiliser n'importe quoi comme valeur d'itérateur, où les entrées de l'itérable peuvent être assignées. Par exemple, vous pouvez déballer des tuples à partir d'une liste de tuples :

```python
list_of_tuples = [(1,2), (3,4)]

for a, b in list_of_tuples:
  print("a:", a, "b:", b)
```

D'autre part, vous pouvez boucler sur tout ce qui est itérable. Vous pouvez appeler une fonction ou utiliser un littéral de liste.

```python
for person in load_persons():
  print("Le nom est:", person.name)
```

```python
for character in ["P", "y", "t", "h", "o", "n"]:
  print("Donne-moi un '{}'!".format(character))
```

Quelques façons d'utiliser les boucles For :

### Itérer sur la fonction range()

```python
for i in range(10):
    print(i)
```

Plutôt qu'une fonction, range est en fait un type de séquence immutable. La sortie contiendra des résultats de la borne inférieure, c'est-à-dire 0, à la borne supérieure, c'est-à-dire 10, mais en excluant 10. Par défaut, la borne inférieure ou l'index de départ est défini à zéro. Sortie :

```text
>
0
1
2
3
4
5
6
7
8
9
>
```

De plus, on peut spécifier la borne inférieure de la séquence et même le pas de la séquence en ajoutant un deuxième et un troisième paramètre.

```python
for i in range(4,10,2): # De 4 à 9 avec un pas de deux
    print(i)
```

Sortie :

```text
>
4
6
8
>
```

### Fonction xrange()

Pour la plupart, xrange et range sont exactement les mêmes en termes de fonctionnalité. Ils fournissent tous deux un moyen de générer une liste d'entiers pour que vous puissiez l'utiliser comme vous le souhaitez. La seule différence est que range retourne un objet liste Python et xrange retourne un objet xrange. Cela signifie que xrange ne génère pas réellement une liste statique au moment de l'exécution comme le fait range. Il crée les valeurs au fur et à mesure que vous en avez besoin avec une technique spéciale appelée yielding. Cette technique est utilisée avec un type d'objet connu sous le nom de générateurs.

Une autre chose à ajouter. Dans Python 3.x, la fonction xrange n'existe plus. La fonction range fait maintenant ce que xrange faisait dans Python 2.x.

### Itérer sur les valeurs d'une liste ou d'un tuple

```python
A = ["hello", 1, 65, "thank you", [2, 3]]
for value in A:
    print(value)
```

Sortie :

```text
>
hello
1
65
thank you
[2, 3]
>
```

### Itérer sur les clés d'un dictionnaire (aka hashmap)

```python
fruits_to_colors = {"apple": "#ff0000",
                    "lemon": "#ffff00",
                    "orange": "#ffa500"}

for key in fruits_to_colors:
    print(key, fruits_to_colors[key])
```

Sortie :

```text
>
apple #ff0000
lemon #ffff00
orange #ffa500
>
```

### Itérer sur deux listes de même taille dans une seule boucle avec la fonction zip()

```python
A = ["a", "b", "c"]
B = ["a", "d", "e"]

for a, b in zip(A, B):
  print(a, b, a == b)
  
```

Sortie :

```text
>
a a True
b d False
c e False
>
```

### Itérer sur une liste et obtenir l'index correspondant avec la fonction enumerate()

```python
A = ["this", "is", "something", "fun"]

for index, word in enumerate(A):
    print(index, word)
```

Sortie :

```text
>
0 this
1 is
2 something
3 fun
>
```

Un cas d'utilisation courant est l'itération sur un dictionnaire :

```python
for name, phonenumber in contacts.items():
  print(name, "est joignable au", phonenumber)
```

Si vous avez absolument besoin d'accéder à l'index actuel de votre itération, n'utilisez **PAS** `range(len(iterable))` ! C'est une pratique extrêmement mauvaise et vous recevrez beaucoup de moqueries de la part des développeurs Python seniors. Utilisez plutôt la fonction intégrée `enumerate()` :

```python
for index, item in enumerate(shopping_basket):
  print("Item", index, "is a", item)
```

### Instructions for/else

Python vous permet d'utiliser else avec les boucles for, le cas else est exécuté lorsque aucune des conditions dans le corps de la boucle n'est satisfaite. Pour utiliser else, nous devons utiliser l'instruction `break` afin de pouvoir sortir de la boucle lorsque la condition est satisfaite. Si nous ne sortons pas, la partie else sera exécutée.

```python
week_days = ['Monday','Tuesday','Wednesday','Thursday','Friday']
today = 'Saturday'
for day in week_days:
  if day == today:
    print('today is a week day')
    break
else:
  print('today is not a week day')
```

Dans le cas ci-dessus, la sortie sera `today is not a week day` puisque le break dans la boucle ne sera jamais exécuté.

### Itérer sur une liste en utilisant une fonction de boucle en ligne

Nous pourrions également itérer en ligne en utilisant Python, par exemple si nous devons mettre en majuscules tous les mots d'une liste, nous pourrions simplement faire ce qui suit :

```python
A = ["this", "is", "awesome", "shinning", "star"]

UPPERCASE = [word.upper() for word in A]
print(UPPERCASE)
```

Sortie :

```text
>
['THIS', 'IS', 'AWESOME', 'SHINNING', 'STAR']
>
```

#### **Plus d'informations :**

* [Documentation Python2 sur les boucles for](https://docs.python.org/2.7/tutorial/controlflow.html#for-statements)
* [Documentation Python3 sur les boucles for](https://docs.python.org/3/tutorial/controlflow.html#for-statements)