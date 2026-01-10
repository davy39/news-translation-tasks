---
title: Comment ajouter à une liste en Python – Tutoriel sur l'addition de listes
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-01-19T17:51:50.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-to-a-list-in-python-list-addition-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/pexels-ono-kosuki-5999834.jpg
tags:
- name: Python
  slug: python
seo_title: Comment ajouter à une liste en Python – Tutoriel sur l'addition de listes
seo_desc: 'A list is a mutable sequence of elements surrounded by square brackets.
  If you’re familiar with JavaScript, a Python list is like a JavaScript array. It''s
  one of the built-in data structures in Python. The others are tuple, dictionary,
  and set.

  A lis...'
---

Une liste est une séquence mutable d'éléments entourée de crochets. Si vous êtes familier avec JavaScript, une liste Python est similaire à un tableau JavaScript. C'est l'une des structures de données intégrées en Python. Les autres sont le tuple, le dictionnaire et l'ensemble.

Une liste peut contenir n'importe quel type de données tel qu'un entier, un flottant, une chaîne de caractères et un booléen :

```py
num_list = [1, 2, 3, 10]

float_list = [2.9, 3.9, 4.6]

boo_list = [True, False]

string_list = ['JavaScript', 'Python', 'freeCodeCamp']
```

Elle peut également contenir un mélange de ces types de données :

```py
mixed_list = ['freeCodeCamp', 1, 1.1, True]
```

Puisque les listes sont mutables, vous pouvez ajouter des éléments ou en supprimer. Cet article vous montrera comment ajouter à une liste.

## Ce que nous allons couvrir
- [Comment ajouter à une liste en Python](#heading-comment-ajouter-a-une-liste-en-python)
  - [Comment ajouter à une liste avec la méthode `append()`](#heading-comment-ajouter-a-une-liste-avec-la-methode-append)
  - [Comment ajouter à une liste avec la méthode `insert()`](#heading-comment-ajouter-a-une-liste-avec-la-methode-insert)
  - [Comment ajouter à une liste avec la méthode `extend()`](#heading-comment-ajouter-a-une-liste-avec-la-methode-extend)
  - [Comment ajouter un dictionnaire à une liste avec la méthode `append()`](#heading-comment-ajouter-un-dictionnaire-a-une-liste-avec-la-methode-append)
- [Conclusion](#heading-conclusion)


## Comment ajouter à une liste en Python
Python fournit 3 méthodes avec lesquelles vous pouvez ajouter à une liste. Ces méthodes sont `append()`, `extend()` et `insert()`.


### Comment ajouter à une liste avec la méthode `append()`

L'élément `append()` ajoute à la fin d'une liste. 

Supposons que nous ayons la liste suivante :

```py
sports_list = ["Football", "Basketball", "Baseball", "Tennis"]
```

Si je veux ajouter "Cricket" à la fin de cette liste, je peux le faire avec la méthode `append()` de cette manière :

```py
sports_list.append("Cricket")
```

L'impression de `sports_list` dans la console donne ce résultat :

```py
['Football', 'Basketball', 'Baseball', 'Tennis', 'Cricket']
```

Vous pouvez voir que "Cricket" a été ajouté au dernier index de la liste.

Vous pouvez également inviter l'utilisateur à ajouter à la liste de cette manière : 

```py
sports_list = ["Football", "Basketball", "Baseball", "Tennis"]
new_sport = input("Veuillez ajouter un nouveau sport : ")
sports_list.append(new_sport)

print(sports_list)
```

### Comment ajouter à une liste avec la méthode `insert()`

La méthode `append()` vous aide à ajouter à la fin d'une liste, mais si vous voulez ajouter à n'importe quel index, vous pouvez utiliser la méthode `insert()`. 

Pour utiliser la méthode `insert()` pour ajouter à une liste, vous devez spécifier l'index, puis l'élément que vous voulez ajouter :

```py
insert(index, item)
```

J'ai ajouté `Athletics` au premier index (0) de la `sports_list` de cette manière :

```py
sports_list = ["Football", "Basketball", "Baseball", "Tennis"]
sports_list.insert(0, "Athletics")
print(sports_list)

# Output: ['Athletics', 'Football', 'Basketball', 'Baseball', 'Tennis']
```

J'ai également ajouté `Wrestling` à l'index 2 (le 3ème index) de cette manière :

```py
sports_list.insert(2, "Wrestling")
print(sports_list)

# Output: ['Athletics', 'Football', 'Wrestling', 'Basketball', 'Baseball', 'Tennis']
```

### Comment ajouter à une liste avec la méthode `extend()`

La méthode `extend()` ajoute un élément de données itérable à une liste ou ajoute une liste à une autre liste. Ainsi, avec elle, vous pouvez ajouter un tuple, un ensemble ou un dictionnaire à une liste.  

```py
sports_list = ["Football", "Basketball", "Baseball", "Tennis"]

# ajouter une autre liste
sports_list.extend(["Golf", "Boxing"])

# Ajouter un tuple
sports_list.extend(("Netball", "TT"))

print(sports_list)

# Output: ['Football', 'Basketball', 'Baseball', 'Tennis', 'Golf', 'Boxing', 'Netball', 'TT']
```

### Comment ajouter un dictionnaire à une liste avec la méthode `append()`

Si vous essayez d'ajouter un dictionnaire à une liste avec la méthode `extend()`, vous n'obtenez que les clés et non les valeurs :

```py
sports_list = ["Football", "Basketball", "Baseball", "Tennis"]
sports_dict = {1: "Netball", 2: "Chess"}

sports_list.extend(sports_dict)
print(sports_list)
# Output:  ['Football', 'Basketball', 'Baseball', 'Tennis', 1, 2]
```

Vous pouvez parcourir le dictionnaire et ensuite utiliser la méthode append pour l'ajouter à la liste. Cela vous donnera les clés et les valeurs du dictionnaire sous forme d'ensemble de tuples dans la liste :

```py
sports_list = ["Football", "Basketball", "Baseball", "Tennis"]
sports_dict = {1: "Netball", 2: "Chess"}

for k, v in sports_dict.items():
    sports_list.append((k, v))

print(sports_list)

# Output: ['Football', 'Basketball', 'Baseball', 'Tennis', (1, 'Netball'), (2, 'Chess')]
```

Si vous voulez le dictionnaire tel quel à l'intérieur de la liste, vous pouvez simplement utiliser la méthode append sans boucle :

```py
sports_list = ["Football", "Basketball", "Baseball", "Tennis"]
sports_dict = {1: "Netball", 2: "Chess"}

sports_list.append(sports_dict)
print(sports_list)

# Output: ['Football', 'Basketball', 'Baseball', 'Tennis', {1: 'Netball', 2: 'Chess'}]
```


## Conclusion
Dans cet article, nous avons examiné comment utiliser les méthodes `append()`, `insert()` et `extend()` pour ajouter à une liste en Python. 

Ce que vous ajoutez à une liste ne doit pas être un seul élément. C'est pourquoi je vous ai montré comment utiliser la méthode `extend()` pour vous aider à ajouter des itérables comme des listes, des tuples et des dictionnaires à une liste.

Merci d'avoir lu.