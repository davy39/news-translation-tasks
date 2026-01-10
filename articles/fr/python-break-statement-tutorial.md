---
title: Instruction Break en Python – Comment sortir d'une boucle For en Python
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2024-04-10T16:51:21.985Z'
originalURL: https://freecodecamp.org/news/python-break-statement-tutorial
coverImage: https://cdn.hashnode.com/res/hashnode/image/stock/unsplash/ieic5Tq8YMk/upload/1e00a0a8acc5c22dea9a4910bffecbb1.jpeg
tags:
- name: Python
  slug: python
- name: Loops
  slug: loops
seo_title: Instruction Break en Python – Comment sortir d'une boucle For en Python
seo_desc: 'You can use loops in Python to execute code logic repeatedly until a specified
  condition is met.

  Python provides some built-in control statements that let you change the behavior
  of a loop. Some of these control statements include continue, break, pa...'
---

Vous pouvez utiliser des boucles en Python pour exécuter une logique de code de manière répétée jusqu'à ce qu'une condition spécifiée soit remplie.

Python fournit certaines instructions de contrôle intégrées qui vous permettent de modifier le comportement d'une boucle. Certaines de ces instructions de contrôle incluent `continue`, `break`, `pass` et `else`.

Dans cet article, vous apprendrez à terminer la boucle actuelle ou une instruction switch en utilisant l'instruction `break`.

## Comment utiliser l'instruction `break` dans une boucle `for` en Python

Considérez la liste Python suivante :

```python
usernames = ["Jade", "John", "Jane", "Doe"]
```

Vous pouvez utiliser une boucle `for` pour parcourir et imprimer les éléments de la liste `usernames` :

```python
usernames = ["Jade", "John", "Jane", "Doe"]

for i in usernames:
    print(i)
# Jade
# John
# Jane
# Doe
```

Mais que faire si vous souhaitez arrêter la boucle lorsqu'un nom d'utilisateur particulier est trouvé ? Vous pouvez le faire en utilisant l'instruction `break`.

Voici un exemple :

```python
usernames = ["Jade", "John", "Jane", "Doe"]

for i in usernames:
    print(i)
    if i == "John":
        break
# Jade
# John
```

Dans le code ci-dessus, nous avons créé une instruction `if` qui vérifie si la valeur actuelle de `i` est "John" : `if i == "John"`.

Dans le corps de l'instruction `if`, nous avons utilisé l'instruction `break`. Ainsi, la boucle s'arrêtera lorsqu'elle trouvera un élément dans la liste avec la valeur "John".

Au lieu d'imprimer toute la liste ("Jade", "John", "Jane", "Doe"), "Jade" et "John" ont été imprimés car la boucle s'est arrêtée immédiatement après avoir trouvé "John".

## Comment utiliser l'instruction `break` dans une boucle `while` en Python

Vous pouvez terminer une boucle `while` en utilisant l'instruction `break` :

```python
usernames = ["Jade", "John", "Jane", "Doe"]

i = 0
while i < len(usernames):
    print(usernames[i])
    if usernames[i] == "John":
        break
    i += 1
```

Tout comme nous l'avons fait dans l'exemple de la boucle `for`, nous avons créé une liste `usernames` avec quatre éléments : `["Jade", "John", "Jane", "Doe"]`.

En utilisant une instruction `if` dans la boucle `while`, nous avons vérifié lorsque la boucle actuelle était à l'index avec une valeur "John". Lorsque cela se produit, la boucle est terminée.

Une fois de plus, "Jade" et "John" ont été imprimés car la boucle s'arrête lorsque "John" est trouvé.

## Conclusion

Dans cet article, vous avez appris à utiliser l'instruction `break` en Python. Vous pouvez l'utiliser pour terminer la boucle actuelle lorsqu'une condition est remplie.

D'après les exemples ci-dessus, vous avez appris comment utiliser l'instruction `break` pour terminer les boucles `for` et `while` en Python.

Bon codage !