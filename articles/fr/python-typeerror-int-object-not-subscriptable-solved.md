---
title: 'TypeError: ''int'' object is not subscriptable [Résolu Erreur Python]'
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-10-31T17:37:23.000Z'
originalURL: https://freecodecamp.org/news/python-typeerror-int-object-not-subscriptable-solved
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/in_not_subable.png
tags:
- name: error
  slug: error
- name: error handling
  slug: error-handling
- name: Python
  slug: python
seo_title: 'TypeError: ''int'' object is not subscriptable [Résolu Erreur Python]'
seo_desc: "The Python error \"TypeError: 'int' object is not subscriptable\" occurs\
  \ when you try to treat an integer like a subscriptable object. \nIn Python, a subscriptable\
  \ object is one you can “subscript” or iterate over. \nWhy the \"TypeError: 'int'\
  \ object is n..."
---

L'erreur Python "TypeError: 'int' object is not subscriptable" se produit lorsque vous essayez de traiter un entier comme un objet subscriptible. 

En Python, un objet subscriptible est un objet que vous pouvez "subscript" ou itérer. 

## Pourquoi l'erreur "TypeError: 'int' object is not subscriptable" se produit
Vous pouvez itérer sur une chaîne de caractères, une liste, un tuple, ou même un dictionnaire. Mais il n'est pas possible d'itérer sur un entier ou un ensemble de nombres. 

Donc, si vous obtenez cette erreur, cela signifie que vous essayez d'itérer sur un entier ou que vous traitez un entier comme un tableau.

Dans l'exemple ci-dessous, j'ai écrit la date de naissance (variable `dob`) au format ddmmyy. J'ai essayé d'obtenir le mois de naissance mais cela n'a pas fonctionné. Cela a déclenché l'erreur "TypeError: 'int' object is not subscriptable" :

```py
dob = 21031999
mob = dob[2:4]

print(mob)

# Output: Traceback (most recent call last):
#   File "int_not_subable..py", line 2, in <module>
#     mob = dob[2:4]
# TypeError: 'int' object is not subscriptable
```

## Comment corriger l'erreur "TypeError: 'int' object is not subscriptable"

Pour corriger cette erreur, vous devez convertir l'entier en un type de données itérable, par exemple, une chaîne de caractères. 

Et si vous obtenez l'erreur parce que vous avez converti quelque chose en entier, alors vous devez le convertir en ce qu'il était avant. Par exemple, une chaîne de caractères, un tuple, une liste, etc.

Dans le code qui a déclenché l'erreur ci-dessus, j'ai pu le faire fonctionner en convertissant la variable `dob` en une chaîne de caractères :

```py
dob = "21031999"
mob = dob[2:4]

print(mob)

# Output: 03
```

Si vous obtenez l'erreur après avoir converti quelque chose en entier, cela signifie que vous devez le convertir en chaîne de caractères ou le laisser tel quel. 

Dans l'exemple ci-dessous, j'ai écrit un programme Python qui imprime la date de naissance au format ddmmyy. Mais il retourne une erreur :

```py
name = input("What is your name? ")
dob = int(input("What is your date of birth in the ddmmyy order? "))
dd = dob[0:2]
mm = dob[2:4]
yy = dob[4:]
print(f"Hi, {name}, \nYour date of birth is {dd} \nMonth of birth is {mm} \nAnd year of birth is {yy}.")

#Output: What is your name? John Doe
# What is your date of birth in the ddmmyy order? 01011970
# Traceback (most recent call last):
#   File "int_not_subable.py", line 12, in <module>
#     dd = dob[0:2]
# TypeError: 'int' object is not subscriptable
```

En examinant le code, je me suis souvenu que input retourne une chaîne de caractères, donc je n'ai pas besoin de convertir le résultat de la saisie de la date de naissance de l'utilisateur en entier. Cela corrige l'erreur :

```py
name = input("What is your name? ")
dob = input("What is your date of birth in the ddmmyy order? ")
dd = dob[0:2]
mm = dob[2:4]
yy = dob[4:]
print(f"Hi, {name}, \nYour date of birth is {dd} \nMonth of birth is {mm} \nAnd year of birth is {yy}.")

#Output: What is your name? John Doe
# What is your date of birth in the ddmmyy order? 01011970
# Hi, John Doe,
# Your date of birth is 01
# Month of birth is 01
# And year of birth is 1970.
```

## Conclusion
Dans cet article, vous avez appris ce qui cause l'erreur "TypeError: 'int' object is not subscriptable" en Python et comment la corriger.

Si vous obtenez cette erreur, cela signifie que vous traitez un entier comme une donnée itérable. Les entiers ne sont pas itérables, donc vous devez utiliser un autre type de données ou convertir l'entier en un type de données itérable. 

Et si l'erreur se produit parce que vous avez converti quelque chose en entier, alors vous devez le convertir en ce type de données itérable.

Merci d'avoir lu.