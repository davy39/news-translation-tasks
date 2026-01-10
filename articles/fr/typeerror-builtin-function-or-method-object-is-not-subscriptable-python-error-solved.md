---
title: 'TypeError: builtin_function_or_method object is not subscriptable Erreur Python
  [RÉSOLU]'
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-11-02T23:43:20.000Z'
originalURL: https://freecodecamp.org/news/typeerror-builtin-function-or-method-object-is-not-subscriptable-python-error-solved
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/built_in_not_subable.png
tags:
- name: error
  slug: error
- name: error handling
  slug: error-handling
- name: Python
  slug: python
seo_title: 'TypeError: builtin_function_or_method object is not subscriptable Erreur
  Python [RÉSOLU]'
seo_desc: "As the name suggests, the error TypeError: builtin_function_or_method object\
  \ is not subscriptable is a “typeerror” that occurs when you try to call a built-in\
  \ function the wrong way. \nWhen a \"typeerror\" occurs, the program is telling\
  \ you that you’re ..."
---

Comme le suggère le nom, l'erreur `TypeError: builtin_function_or_method object is not subscriptable` est une "typeerror" qui se produit lorsque vous essayez d'appeler une fonction intégrée de la mauvaise manière. 

Lorsque qu'une "typeerror" se produit, le programme vous indique que vous mélangez les types. Cela signifie, par exemple, que vous essayez peut-être de concaténer une chaîne avec un entier.

Dans cet article, je vais vous montrer pourquoi l'erreur TypeError: builtin_function_or_method object is not subscriptable se produit et comment vous pouvez la corriger. 

## Pourquoi l'erreur TypeError: builtin_function_or_method object is not subscriptable se produit 
Chaque fonction intégrée de Python telle que `print()`, `append()`, `sorted()`, `max()`, et autres doit être appelée avec des parenthèses ou des crochets ronds (`()`). 

Si vous essayez d'utiliser des crochets, Python ne le traitera pas comme un appel de fonction. Au lieu de cela, Python pensera que vous essayez d'accéder à quelque chose depuis une liste ou une chaîne et lancera alors l'erreur.

Par exemple, le code ci-dessous lance l'erreur parce que j'ai essayé d'imprimer la valeur de la variable avec des crochets devant la fonction `print()` :
 
Et si vous entourez ce que vous voulez imprimer avec des crochets même si l'élément est itérable, vous obtenez toujours l'erreur :

```py
gadgets = ["Mouse", "Monitor", "Laptop"]
print[gadgets[0]]

# Output: Traceback (most recent call last):
#   File "built_in_obj_not_subable.py", line 2, in <module>
#     print[gadgets[0]]
# TypeError: 'builtin_function_or_method' object is not subscriptable
``` 

Ce problème n'est pas particulier à la fonction `print()`. Si vous essayez d'appeler une autre fonction intégrée avec des crochets, vous obtenez également l'erreur. 

Dans l'exemple ci-dessous, j'ai essayé d'appeler `max()` avec des crochets et j'ai obtenu l'erreur :

```py
numbers = [5, 7, 24, 6, 90]
max_num = max(numbers)
print[max_num]

# Traceback (most recent call last):
#   File "built_in_obj_not_subable.py", line 11, in <module>
#     print[max_num]
# TypeError: 'builtin_function_or_method' object is not subscriptable

```

## Comment corriger l'erreur TypeError: builtin_function_or_method object is not subscriptable 

Pour corriger cette erreur, tout ce que vous avez à faire est de vous assurer d'utiliser des parenthèses pour appeler la fonction.

Vous n'avez besoin d'utiliser des crochets que si vous voulez accéder à un élément depuis des données itérables telles qu'une chaîne, une liste ou un tuple :

```py
gadgets = ["Mouse", "Monitor", "Laptop"]
print(gadgets[0])

# Output: Mouse
```
```py
numbers = [5, 7, 24, 6, 90]
max_num = max(numbers)
print(max_num)

# Output: 90
```

## Conclusion
Cet article vous a montré pourquoi l'erreur TypeError: builtin_function_or_method object is not subscriptable se produit et comment la corriger.

Rappelez-vous que vous n'avez besoin d'utiliser des crochets (`[]`) que pour accéder à un élément depuis des données itérables et que vous ne devriez pas les utiliser pour appeler une fonction.

Si vous obtenez cette erreur, vous devriez chercher dans votre code tout point où vous appelez une fonction intégrée avec des crochets et les remplacer par des parenthèses.

Merci d'avoir lu.