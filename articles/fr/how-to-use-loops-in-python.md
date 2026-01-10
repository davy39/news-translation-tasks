---
title: Comment utiliser les boucles en Python
subtitle: ''
author: Jeremiah Oluseye
co_authors: []
series: null
date: '2023-03-07T21:36:52.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-loops-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/Loops.JPG
tags:
- name: Loops
  slug: loops
- name: Python
  slug: python
seo_title: Comment utiliser les boucles en Python
seo_desc: 'Loops are an essential concept in programming. They allow you to execute
  a block of code repeatedly based on certain conditions.

  Python offers two types of loops: for and while loops. In this article, we will
  explore both of these loop types and prov...'
---

Les boucles sont un concept essentiel en programmation. Elles permettent d'exécuter un bloc de code plusieurs fois en fonction de certaines conditions.

Python offre deux types de boucles : les boucles for et while. Dans cet article, nous allons explorer ces deux types de boucles et fournir des exemples de leur utilisation dans votre code Python.

## Comment utiliser les boucles For en Python

Vous utiliserez une boucle for lorsque vous souhaitez itérer sur une collection d'éléments ou lorsque vous connaissez le nombre exact de fois où vous voulez exécuter un bloc de code.

Voici le code pour une boucle for en Python :

```python
for variable in iterable:
    # code à exécuter
```

* variable est une variable qui représente l'élément actuel dans l'itérable sur lequel nous itérons.

* iterable est une collection d'éléments sur lesquels nous voulons itérer, comme une liste, un tuple, une chaîne ou une plage.

Par exemple, supposons que nous avons une liste de nombres et que nous voulons imprimer chaque nombre :

```python
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)
```

Sortie

```python
1
2
3
4
5
```

Nous pouvons également utiliser la fonction `range()` pour spécifier une plage de nombres à itérer :

```python
for num in range(1, 6):
    print(num)
```

Sortie :

```python
1
2
3
4
5
```

La fonction `range()` prend deux arguments : le nombre de départ et le nombre de fin (exclusif). Dans ce cas, la boucle itérera sur les nombres de 1 à 5.

## Comment utiliser les boucles While en Python

Vous utiliserez une boucle while lorsque vous souhaitez exécuter un bloc de code plusieurs fois en fonction d'une condition.

Voici la syntaxe pour une boucle while en Python :

```python
while condition:
    # code à exécuter
```

`condition` est une expression booléenne qui détermine si la boucle doit continuer ou non.

Par exemple, supposons que nous voulons imprimer les nombres de 1 à 5 en utilisant une boucle while :

```python
num = 1
while num <= 5:
    print(num)
    num += 1
```

Dans cet exemple, nous initialisons la variable `num` à 1, puis nous exécutons la boucle tant que `num` est inférieur ou égal à 5. À l'intérieur de la boucle, nous imprimons la valeur actuelle de `num` puis nous l'incrémentons de 1.

Nous pouvons également utiliser une boucle while pour continuer à demander à l'utilisateur une entrée jusqu'à ce qu'il saisisse une réponse valide :

```python
valid_response = False
while not valid_response:
    response = input("Entrez 'yes' ou 'no': ")
    if response.lower() == 'yes' or response.lower() == 'no':
        valid_response = True
    else:
        print("Réponse invalide. Veuillez entrer 'yes' ou 'no'.")
```

Examinons quelques utilisations avancées des boucles en Python.

## Comment utiliser les boucles imbriquées en Python

Les boucles imbriquées sont des boucles qui sont contenues dans d'autres boucles. Elles nous permettent d'itérer sur une collection d'éléments plusieurs fois et sont utiles pour des tâches telles que la génération de toutes les combinaisons possibles d'éléments.

Voici un exemple de la façon d'utiliser des boucles imbriquées pour générer toutes les paires possibles de nombres à partir de deux listes :

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]

for num1 in list1:
    for num2 in list2:
        print(num1, num2)
```

Sortie :

```python
1 4
1 5
1 6
2 4
2 5
2 6
3 4
3 5
3 6
```

Dans cet exemple, nous utilisons une boucle for imbriquée pour itérer sur chaque élément de list1 et list2, et imprimer toutes les paires possibles de nombres.

## Compréhension de liste en Python

Les compréhensions de liste sont un moyen concis de créer des listes basées sur des listes existantes ou d'autres objets itérables. Elles utilisent une boucle for et une instruction conditionnelle optionnelle pour générer la nouvelle liste.

Voici un exemple de la façon d'utiliser la compréhension de liste pour créer une nouvelle liste de nombres pairs à partir d'une liste existante :

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)
```

Sortie :

```python
[2, 4, 6, 8, 10]
```

Dans cet exemple, nous utilisons une compréhension de liste pour itérer sur chaque nombre dans la liste numbers et l'ajouter à la liste `even_numbers` s'il est pair (c'est-à-dire, le reste lorsqu'il est divisé par 2 est 0).

## Comment itérer sur un dictionnaire en Python

En Python, nous pouvons itérer sur les clés, les valeurs ou les éléments (paires clé-valeur) d'un dictionnaire en utilisant une boucle for.

Voici un exemple de la façon d'itérer sur les éléments d'un dictionnaire et d'imprimer les paires clé-valeur :

```python
fruits = {'apple': 'red', 'banana': 'yellow', 'orange': 'orange'}

for fruit, color in fruits.items():
    print(f"The {fruit} is {color}.")
```

Sortie :

```python
The apple is red.
The banana is yellow.
The orange is orange.
```

Dans cet exemple, nous utilisons la méthode `items()` du dictionnaire `fruits` pour itérer sur chaque paire clé-valeur, puis nous imprimons une chaîne formatée qui inclut le fruit et sa couleur correspondante.

## Conclusion

Les boucles sont une partie essentielle de la programmation en Python. Elles nous permettent d'automatiser les tâches répétitives et de manipuler les données de manière puissante.

En comprenant les bases des boucles for et while, ainsi que des concepts plus avancés tels que les boucles imbriquées et les compréhensions de liste, vous serez en mesure d'écrire un code efficace et performant en Python.

Connectons-nous sur [Twitter](https://twitter.com/Olujerry19) et [Linkedin](https://www.linkedin.com/in/jeremiah-oluseye-58457719a/)