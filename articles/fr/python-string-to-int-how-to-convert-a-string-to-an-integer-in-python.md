---
title: 'Python String to Int: Comment convertir une chaîne en entier en Python'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-05T21:06:00.000Z'
originalURL: https://freecodecamp.org/news/python-string-to-int-how-to-convert-a-string-to-an-integer-in-python
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e2a740569d1a4ca3bb5.jpg
tags:
- name: data structures
  slug: data-structures
- name: Python
  slug: python
seo_title: 'Python String to Int: Comment convertir une chaîne en entier en Python'
seo_desc: 'By Chris Tse

  Unlike many other programming languages out there, Python does not implicitly typecast
  integers (or floats) to strings when you concatenate them to strings.

  Fortunately, Python has a handy built-in function str() which will convert the a...'
---

Par Chris Tse

Contrairement à de nombreux autres langages de programmation, Python ne convertit pas implicitement les entiers (ou les flottants) en chaînes de caractères lorsque vous les concaténez avec des chaînes.

Heureusement, Python dispose d'une fonction intégrée pratique `str()` qui convertit l'argument passé en format chaîne.

## La mauvaise façon de convertir une chaîne en entier en Python

Les programmeurs venant d'autres langages de programmation pourraient tenter de faire la concaténation de chaîne suivante, ce qui produira une erreur :

```py
age = 18

string = "Bonjour, j'ai " + age + " ans"
```

[Vous pouvez exécuter ce code sur repl.it](https://repl.it/@christopher_tse/int-to-string-error).

L'erreur qui apparaît est :

```text
Traceback (most recent call last):
  File "python", line 3, in <module>
TypeError: must be str, not int
```

Ici, `TypeError: must be str, not int` indique que l'entier doit d'abord être converti en chaîne avant de pouvoir être concaténé.

## La bonne façon de convertir une chaîne en entier en Python

Voici un exemple simple de concaténation :

```py
age = 18

print("Bonjour, j'ai " + str(age) + " ans")

# Sortie
# Bonjour, j'ai 18 ans
```

[Vous pouvez exécuter ce code sur repl.it](https://repl.it/@christopher_tse/int-to-string-no-error).

Voici comment imprimer `1 2 3 4 5 6 7 8 9 10` en utilisant une seule chaîne :

```py
result = ""

for i in range(1, 11):
    result += str(i) + " "

print(result)

# Sortie
# 1 2 3 4 5 6 7 8 9 10
```

[Vous pouvez exécuter le code sur repl.it](https://repl.it/@christopher_tse/int-to-string-loop).

### Voici une explication ligne par ligne de comment le code ci-dessus fonctionne :

1. Tout d'abord, une variable 'result' est assignée à une chaîne vide.
2. La boucle for est utilisée pour itérer sur une liste de nombres.
3. Cette liste de nombres est générée en utilisant la fonction range.
4. Donc, range(1,11) va générer une liste de nombres de 1 à 10.
5. À chaque itération de la boucle for, cette variable 'i' va prendre les valeurs de 1 à 10.
6. À la première itération, lorsque la variable i=1, alors la variable [result=result+str(i)+" (caractère espace)"], str(i) convertit le 'i' qui est une valeur entière en une valeur chaîne.
7. Puisque i=1, à la première itération, finalement result=1.
8. Et le même processus continue jusqu'à i=10 et finalement après la dernière itération result=1 2 3 4 5 6 7 8 9 10.
9. Par conséquent, lorsque nous imprimons enfin le résultat après la boucle for, la sortie sur la console est '1 2 3 4 5 6 7 8 9 10'.

J'espère que vous avez trouvé cela utile. Bon codage.