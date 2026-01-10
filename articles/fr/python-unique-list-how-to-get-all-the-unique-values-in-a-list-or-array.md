---
title: Liste Unique en Python – Comment Obtenir toutes les Valeurs Uniques dans une
  Liste ou un Tableau
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-17T16:51:44.000Z'
originalURL: https://freecodecamp.org/news/python-unique-list-how-to-get-all-the-unique-values-in-a-list-or-array
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/skye-studios-NDLLFxTELrU-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: Liste Unique en Python – Comment Obtenir toutes les Valeurs Uniques dans
  une Liste ou un Tableau
seo_desc: 'By Amy Haddad

  Say you have a list that contains duplicate numbers:

  numbers = [1, 1, 2, 3, 3, 4]


  But you want a list of unique numbers.

  unique_numbers = [1, 2, 3, 4]


  There are a few ways to get a list of unique values in Python. This article will
  sh...'
---

Par Amy Haddad

Disons que vous avez une liste qui contient des nombres en double :

```python
numbers = [1, 1, 2, 3, 3, 4]
```

Mais vous voulez une liste de nombres _uniques_.

```python
unique_numbers = [1, 2, 3, 4]
```

Il existe plusieurs façons d'obtenir une liste de valeurs uniques en Python. Cet article vous montrera comment faire.

# Option 1 – Utiliser un Set pour Obtenir des Éléments Uniques

Utiliser un **`set`** est une façon de procéder. Un set est utile car il contient des éléments uniques.

Vous pouvez utiliser un set pour obtenir les éléments uniques. Ensuite, transformez le set en une liste.

Examinons deux approches qui utilisent un set et une liste. La première approche est verbeuse, mais il est utile de voir ce qui se passe à chaque étape.

```python
numbers = [1, 2, 2, 3, 3, 4, 5]


def get_unique_numbers(numbers):

    list_of_unique_numbers = []

    unique_numbers = set(numbers)

    for number in unique_numbers:
        list_of_unique_numbers.append(number)

    return list_of_unique_numbers


print(get_unique_numbers(numbers))
# résultat : [1, 2, 3, 4, 5]
```

Examinons de plus près ce qui se passe. On me donne une liste de nombres, **`numbers`**. Je passe cette liste à la fonction, **`get_unique_numbers`**.

À l'intérieur de la fonction, je crée une liste vide, qui contiendra éventuellement tous les nombres uniques. Ensuite, j'utilise un **`set`** pour obtenir les nombres uniques de la liste **`numbers`**.

```python
unique_numbers = set(numbers)
```

J'ai ce dont j'ai besoin : les nombres uniques. Maintenant, je dois mettre ces valeurs dans une liste. Pour ce faire, j'utilise une boucle for pour itérer à travers chaque nombre dans le set.

```python
for number in unique_numbers:
       list_of_unique_numbers.append(number)
```

À chaque itération, j'ajoute le nombre actuel à la liste, `list_of_unique_numbers`. Enfin, je retourne cette liste à la fin du programme.

Il existe une façon plus courte d'utiliser un set et une liste pour obtenir des valeurs uniques en Python. C'est ce que nous allons aborder ensuite.

### Une Approche Plus Courte avec Set

Tout le code écrit dans l'exemple ci-dessus peut être condensé en une seule ligne avec l'aide des fonctions intégrées de Python.

```python
numbers = [1, 2, 2, 3, 3, 4, 5]
unique_numbers = list(set(numbers))
print(unique_numbers)
# Résultat : [1, 2, 3, 4, 5]
```

Bien que ce code semble très différent du premier exemple, l'idée est la même. Utilisez un set pour obtenir les nombres uniques. Ensuite, transformez le set en une liste.

```python
unique_numbers = list(set(numbers))
```

Il est utile de penser "de l'intérieur vers l'extérieur" lors de la lecture du code ci-dessus. Le code le plus interne est évalué en premier : **`set(numbers)`**. Ensuite, le code le plus externe est évalué : **`list(set(numbers))`**.

# Option 2 – Utiliser l'Itération pour Identifier les Valeurs Uniques

L'itération est une autre approche à considérer.

L'idée principale est de créer une liste vide qui contiendra les nombres uniques. Ensuite, utilisez une boucle for pour itérer sur chaque nombre dans la liste donnée. Si le nombre est déjà dans la liste unique, alors passez à l'itération suivante. Sinon, ajoutez le nombre à la liste.

Regardons deux façons d'utiliser l'itération pour obtenir les valeurs uniques dans une liste, en commençant par la plus verbeuse.

```python
numbers = [20, 20, 30, 30, 40]


def get_unique_numbers(numbers):
    unique = []

    for number in numbers:
        if number in unique:
            continue
        else:
            unique.append(number)
    return unique


print(get_unique_numbers(numbers))
# Résultat : [20, 30, 40]
```

Voici ce qui se passe à chaque étape. Tout d'abord, on me donne une liste de nombres, **`numbers`**. Je passe cette liste à ma fonction, **`get_unique_numbers`**.

À l'intérieur de la fonction, je crée une liste vide, **`unique`**. Finalement, cette liste contiendra tous les nombres uniques.

J'utilise une boucle for pour itérer à travers chaque nombre dans la liste **`numbers`**.

```python
 for number in numbers:
       if number in unique:
           continue
       else:
           unique.append(number)
```

La conditionnelle à l'intérieur de la boucle vérifie si le nombre de l'itération actuelle est dans la liste **`unique`**. Si c'est le cas, la boucle passe à l'itération suivante. Sinon, le nombre est ajouté à cette liste.

Voici le point important : seuls les nombres uniques sont ajoutés. Une fois la boucle terminée, je retourne **`unique`** qui contient tous les nombres uniques.

## Une Approche Plus Courte avec Itération

Il existe une autre façon d'écrire la fonction en moins de lignes.

```python
numbers = [20, 20, 30, 30, 40]


def get_unique_numbers(numbers):
    unique = []
    for number in numbers:
        if number not in unique:
            unique.append(number)
    return unique
# Résultat : [20, 30, 40]

```

La différence réside dans la conditionnelle. Cette fois, elle est configurée pour se lire comme suit : si le nombre n'est pas dans **`unique`**, alors ajoutez-le.

```python
if number not in unique:
    unique.append(number)
```

Sinon, la boucle passera au nombre suivant dans la liste, **`numbers`**.

Le résultat est le même. Cependant, il est parfois plus difficile de réfléchir et de lire le code lorsque le booléen est nié.

Il existe d'autres façons de trouver des valeurs uniques dans une liste Python. Mais vous vous retrouverez probablement à utiliser l'une des approches couvertes dans cet article.

_Je parle de l'apprentissage de la programmation et des meilleures façons de s'y prendre sur [amymhaddad.com](http://amymhaddad.com/). Suivez-moi sur Twitter : [@amymhaddad](https://twitter.com/amymhaddad)._