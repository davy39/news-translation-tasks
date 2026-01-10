---
title: Python Trier une Liste – Comment Ordonner par Ordre Décroissant ou Croissant
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2021-09-03T14:49:55.000Z'
originalURL: https://freecodecamp.org/news/python-sort-list-how-to-order-by-descending-or-ascending
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/thisisengineering-raeng-64YrPKiguAE-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: Python Trier une Liste – Comment Ordonner par Ordre Décroissant ou Croissant
seo_desc: "In Python, you can sort data by using the sorted() method or sort() method.\
  \ \nIn this article, I will provide code examples for the sorted() and sort() methods\
  \ and explain the differences between the two.\nWhat is the sort() method in Python?\n\
  This meth..."
---

En Python, vous pouvez trier des données en utilisant la méthode `sorted()` ou la méthode `sort()`.

Dans cet article, je vais fournir des exemples de code pour les méthodes `sorted()` et `sort()` et expliquer les différences entre les deux.

## Qu'est-ce que la méthode sort() en Python ?

Cette méthode prend une liste et la trie en place. Cette méthode n'a pas de valeur de retour.

Dans cet exemple, nous avons une liste de nombres et nous pouvons utiliser la méthode `sort()` pour trier la liste par ordre croissant.

```py
my_list = [67, 2, 999, 1, 15]

# ceci imprime la liste non triée
print("Liste non triée : ", my_list)

# trie la liste en place
my_list.sort()

# ceci imprime la liste triée
print("Liste triée : ", my_list)
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-02-at-1.41.09-PM.png)

Si la liste est déjà triée, elle retournera None dans la console.

```py
my_list = [6, 7, 8, 9, 10]

# ceci retournera None car la liste est déjà triée
print(my_list.sort())
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-02-at-1.30.28-PM.png)

La méthode `sort()` peut prendre deux arguments optionnels appelés `key` et `reverse`.

`key` a la valeur d'une fonction qui sera appelée sur chaque élément de la liste.

Dans cet exemple, nous pouvons utiliser la fonction `len()` comme valeur pour l'argument `key`. `key=len` indiquera à l'ordinateur de trier la liste des noms par longueur, du plus petit au plus grand.

```py
names = ["Jessica", "Ben", "Carl", "Jackie", "Wendy"]

print("Non trié : ", names)
names.sort(key=len)
print("Trié : ", names)
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-02-at-2.11.37-PM.png)

`reverse` a une valeur booléenne de `True` ou `False`.

Dans cet exemple, `reverse=True` indiquera à l'ordinateur de trier la liste par ordre alphabétique inverse.

```py
names = ["Jessica", "Ben", "Carl", "Jackie", "Wendy"]

print("Non trié : ", names)
names.sort(reverse=True)
print("Trié : ", names)
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-02-at-2.25.43-PM.png)

## Comment utiliser la méthode sorted() en Python

Cette méthode retournera une nouvelle liste triée à partir d'un itérable. Des exemples d'itérables seraient les listes, les chaînes de caractères et les tuples.

Une différence clé entre `sort()` et `sorted()` est que `sorted()` retournera une nouvelle liste tandis que `sort()` trie la liste en place.

Dans cet exemple, nous avons une liste de nombres qui sera triée par ordre croissant.

```py
sorted_numbers = sorted([77, 22, 9, -6, 4000])

print("Trié par ordre croissant : ", sorted_numbers)
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-02-at-8.07.42-PM.png)

La méthode `sorted()` accepte également les arguments optionnels `key` et `reverse`.

Dans cet exemple, nous avons une liste de nombres triée par ordre décroissant. `reverse=True` indique à l'ordinateur d'inverser la liste, du plus grand au plus petit.

```py
sorted_numbers = sorted([77, 22, 9, -6, 4000], reverse=True)

print("Trié par ordre décroissant : ", sorted_numbers)
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-02-at-8.15.06-PM.png)

Une autre différence clé entre `sorted()` et `sort()` est que la méthode `sorted()` accepte n'importe quel itérable alors que la méthode `sort()` ne fonctionne qu'avec les listes.

Dans cet exemple, nous avons une chaîne de caractères divisée en mots individuels en utilisant la méthode `split()`. Ensuite, nous utilisons `sorted()` pour trier les mots par longueur, du plus petit au plus grand.

```py
my_sentence = "Jessica found a dollar on the ground"

print("Phrase originale : ", my_sentence)
print(sorted(my_sentence.split(), key=len))
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-02-at-8.42.55-PM.png)

Nous pouvons également modifier cet exemple et inclure les arguments `key` et `reverse`.

Cet exemple modifié va maintenant trier la liste du plus grand au plus petit.

```py
my_sentence = "Jessica found a dollar on the ground"

print("Phrase originale : ", my_sentence)
print(sorted(my_sentence.split(), key=len, reverse=True))
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-02-at-8.48.21-PM.png)

Nous pouvons également utiliser la méthode `sorted()` sur des `tuples`.

Dans cet exemple, nous avons une collection de `tuples` qui représente le nom, l'âge et l'instrument des élèves de la fanfare.

```py
band_students = [
    ('Danny', 17, 'Trombone'),
    ('Mary', 14, 'Flute'),
    ('Josh', 15, 'Percussion')
]
```

Nous pouvons utiliser la méthode `sorted()` pour trier ces données par âge des élèves. La `key` a la valeur d'une fonction `lambda` qui indique à l'ordinateur de trier par âge dans l'ordre croissant.

Une fonction `lambda` est une fonction anonyme sans nom. Vous pouvez définir ce type de fonction en utilisant le mot-clé `lambda`.

```py
lambda student: student[1]
```

Pour accéder à une valeur dans un `tuple`, vous utilisez la notation entre crochets et le numéro d'index que vous souhaitez accéder. Puisque nous commençons à compter à zéro, la valeur de l'âge serait `[1]`.

Voici l'exemple complet.

```py
band_students = [
    ('Danny', 17, 'Trombone'),
    ('Mary', 14, 'Flute'),
    ('Josh', 15, 'Percussion')
]

print(sorted(band_students, key=lambda student: student[1]))
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-02-at-9.05.22-PM.png)

Nous pouvons modifier cet exemple et trier les données par instrument à la place. Nous pouvons utiliser `reverse` pour trier les instruments par ordre alphabétique inverse.

```py
band_students = [
    ('Danny', 17, 'Trombone'),
    ('Mary', 14, 'Flute'),
    ('Josh', 15, 'Percussion')
]

print(sorted(band_students, key=lambda student: student[2], reverse=True))

```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-02-at-9.10.16-PM.png)

## Conclusion

Dans cet article, nous avons appris à travailler avec les méthodes `sort()` et `sorted()` de Python.

La méthode `sort()` ne fonctionne qu'avec les listes et trie la liste en place. Elle n'a pas de valeur de retour.

La méthode `sorted()` fonctionne avec n'importe quel itérable et retourne une nouvelle liste triée. Des exemples d'itérables seraient les listes, les chaînes de caractères et les tuples.

Ces deux méthodes ont deux arguments optionnels : `key` et `reverse`.

`key` a la valeur d'une fonction qui sera appelée sur chaque élément de la liste.

`reverse` a une valeur booléenne de `True` ou `False`.