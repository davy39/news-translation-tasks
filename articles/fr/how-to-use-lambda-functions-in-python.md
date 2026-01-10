---
title: Fonction Anonyme Python – Comment Utiliser les Fonctions Lambda
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2023-02-15T17:17:35.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-lambda-functions-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/lambda-functions-in-python.png
tags:
- name: functions
  slug: functions
- name: lambda
  slug: lambda
- name: Python
  slug: python
seo_title: Fonction Anonyme Python – Comment Utiliser les Fonctions Lambda
seo_desc: 'You can use functions in programming to store a piece of code that can
  be invoked when needed. This prevents you from retyping the same logic every time
  you need that code.

  In this article, you''ll learn how to create and use anonymous functions in Py...'
---

Vous pouvez utiliser des fonctions en programmation pour stocker un morceau de code qui peut être invoqué lorsque nécessaire. Cela vous évite de retaper la même logique chaque fois que vous avez besoin de ce code.

Dans cet article, vous apprendrez à créer et à utiliser des fonctions anonymes en Python. Elles sont également appelées fonctions lambda.

Nous commencerons par un aperçu rapide de la création de fonctions régulières en Python. Ensuite, vous apprendrez la syntaxe et les applications pratiques des fonctions anonymes en Python.

Vous verrez également certaines des différences entre les fonctions lambda et les fonctions régulières en Python, et quand utiliser les fonctions lambda.

## Comment Utiliser les Fonctions en Python

Les fonctions vous évitent de réinventer la roue lorsque certaines logiques sont requises plusieurs fois.

Considérez le code ci-dessous :

```python
first_addition = 2+3 
print(first_addition) # 5 

second_addition = 3+5 
print(second_addition) # 8
```

Nous avons dû recréer la logique pour l'addition plusieurs fois dans différentes variables. Imaginez si vous deviez faire cela cent fois.

Avec une fonction, vous pouvez créer la logique une fois et la réutiliser autant que vous le souhaitez. Voici un exemple en Python :

```python
def add_numbers(a,b): return a + b 

print(add_numbers(2,3)) # 5 
print(add_numbers(3,5)) # 8 
print(add_numbers(5,7)) # 12
```

En utilisant le mot-clé `def`, nous avons créé une fonction appelée `add_numbers(a,b)`. Elle prend deux paramètres – `a` et `b`. La fonction retourne la somme de `a` et `b`.

Ainsi, pour utiliser la logique plusieurs fois, nous avons simplement dû appeler la fonction et passer différents paramètres pour différentes opérations :

```python
print(add_numbers(2,3)) # 5 
print(add_numbers(3,5)) # 8 
print(add_numbers(5,7)) # 12 
```

Maintenant, examinons les fonctions anonymes/lambda en Python.

## Comment Utiliser les Fonctions Lambda en Python

Une fonction anonyme en Python est une fonction sans nom. Elle peut être immédiatement invoquée ou stockée dans une variable.

Les fonctions anonymes en Python sont également connues sous le nom de fonctions lambda.

Voici la syntaxe pour créer une fonction lambda en Python :

```python
lambda parametre(s) : expression
```

Il y a trois valeurs qui définissent une fonction lambda comme on peut le voir dans la syntaxe ci-dessus :

* Une fonction lambda est créée en utilisant le mot-clé `lambda`.
* Le mot-clé est suivi d'un ou plusieurs paramètres.
* Enfin, une expression est fournie pour la fonction. C'est la partie du code qui est exécutée/retournée.

Les paramètre(s) et l'expression sont séparés par un deux-points.

Voici un exemple :

```python
add_numbers = lambda a,b : a + b 
  
print(add_numbers(2,3)) # 5       
```

Dans le code ci-dessus, nous avons créé une fonction lambda avec deux paramètres – `a` et `b`. La fonction retourne la somme des paramètres.

C'est-à-dire : `lambda a,b : a + b`

Notez que la fonction n'a pas de nom. Nous avons assigné la fonction lambda à une variable appelée `add_numbers` afin de pouvoir facilement invoquer la fonction à travers la variable.

Sans assigner une fonction lambda à une variable, vous auriez quelque chose comme ceci :

```python
print(lambda a,b : a + b)
# <function <lambda> at 0x7f757922fb00>
```

Le code ci-dessus retourne simplement un objet lambda dans la console.

Vous pouvez immédiatement appeler une fonction lambda en utilisant des parenthèses :

```python
(lambda a,b : a + b)(2,3)
```

Lorsque le code ci-dessus est imprimé, vous obtiendrez 5 en retour.

## Quelle est la Différence Entre les Fonctions Lambda et les Fonctions Régulières en Python ?

Voici quelques différences entre les fonctions lambda et les fonctions régulières en Python :

| Fonctions Lambda | Fonctions Régulières |
| ------------- |:-------------:|
| Définies en utilisant le mot-clé lambda | Définies en utilisant le mot-clé def |
| Peut être écrite en une ligne  | Requiert plus d'une ligne de code |
| Aucune instruction return requise | L'instruction return doit être définie lors du retour de valeurs |
| Peut être utilisée anonymement  | Les fonctions régulières doivent être nommées |

## Quand Utiliser une Fonction Lambda en Python

Bien que vous puissiez utiliser à la fois des fonctions régulières et des fonctions lambda pour obtenir les mêmes résultats, voici quelques raisons pour lesquelles vous pourriez choisir une fonction lambda :

Tout d'abord, vous pouvez utiliser une fonction lambda lorsque vous avez besoin d'une fonction qui ne sera utilisée qu'une seule fois. Cela est particulièrement utile lorsque vous travaillez avec des fonctions comme `map`, `reduce`, `filter`. Considérez le code ci-dessous :

```python
def double_number(n):
    return n + n

numbers = [1, 3, 5, 7, 9]

double_result = map(double_number, numbers)

print(list(double_result))
# [2, 6, 10, 14, 18]
```

Dans le code ci-dessus, nous avons créé une fonction régulière appelée `double_number` qui double la valeur d'un nombre.

Bien que la fonction ait été passée en tant que paramètre à la fonction `map` — `map(double_number, numbers)`, nous avons dû écrire la logique avant de l'utiliser.

Avec les fonctions lambda, vous pouvez faire ceci :

```python
numbers = [1, 3, 5, 7, 9]

double_result = map(lambda x : x+x, numbers)

print(list(double_result))
# [2, 6, 10, 14, 18]
```

Comme vous pouvez le voir ci-dessus, nous avons simplement passé une fonction lambda — `lambda x : x+x` — en tant que paramètre à la fonction `map` : `map(lambda x : x+x, numbers)`.

Nous avons pu obtenir le même résultat avec moins de lignes de code. Il n'a pas été nécessaire de définir une fonction avant de l'utiliser.

Vous pouvez également utiliser une fonction lambda lorsque vous avez besoin d'une fonction qui doit être invoquée immédiatement. Comme vous pouvez le voir dans l'exemple du point précédent, nous avons d'abord défini la fonction régulière avant de l'utiliser. Les fonctions lambda peuvent être invoquées immédiatement après leur création.

Enfin, les lambdas sont utiles lorsque vous voulez utiliser une fonction à l'intérieur d'une fonction. Ou lorsque vous voulez créer une fonction qui retourne une fonction.

## Résumé

Dans cet article, nous avons parlé des fonctions lambda en Python. Ce sont des fonctions sans nom et qui peuvent être exécutées avec une seule ligne de code.

Nous avons vu comment utiliser des fonctions régulières en Python avec quelques exemples.

Ensuite, nous avons vu la syntaxe et un exemple pratique d'utilisation des fonctions lambda.

Enfin, nous avons parlé des différences entre les fonctions lambda et les fonctions régulières en Python, et quand utiliser les fonctions lambda.

Bon codage !