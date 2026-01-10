---
title: Opérateur ternaire Python – Opérateurs conditionnels en Python
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2023-04-26T15:29:37.000Z'
originalURL: https://freecodecamp.org/news/python-tenary-operator
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/chris-ried-ieic5Tq8YMk-unsplash.jpg
tags:
- name: Conditionals
  slug: conditionals
- name: Python
  slug: python
seo_title: Opérateur ternaire Python – Opérateurs conditionnels en Python
seo_desc: "You can use conditional operators in Python to execute code based on a\
  \ predefined condition(s). \nIn this article, you'll learn how to use the ternary\
  \ operator in Python. You'll see its syntax along with some practical examples.\
  \ \nWhat Is the Ternary O..."
---

Vous pouvez utiliser des opérateurs conditionnels en Python pour exécuter du code en fonction de condition(s) prédéfinie(s).

Dans cet article, vous apprendrez à utiliser l'opérateur ternaire en Python. Vous verrez sa syntaxe ainsi que quelques exemples pratiques.

## À quoi sert l'opérateur ternaire en Python ?

L'opérateur ternaire en Python est simplement une manière plus courte d'écrire des instructions `if` et `if...else`.

Voici à quoi ressemble une instruction `if...else` en Python :

```python
user_score = 90

if user_score > 50:
    print("Next level")
else:
    print("Repeat level")
```

Dans le code ci-dessus, nous avons créé une variable `user_score` avec une valeur de 90.

Nous avons ensuite imprimé l'une des deux instructions en fonction d'une condition prédéfinie — `if user_score > 50`.

Ainsi, si la variable `user_score` est supérieure à 50, nous imprimons "Next level". Si elle est inférieure à `user_score`, nous imprimons "Repeat level".

Vous pouvez raccourcir l'instruction `if...else` en utilisant la syntaxe de l'opérateur ternaire.

## Exemple d'opérateur ternaire Python

Dans le dernier exemple, nous avons vu comment utiliser une instruction `if...else` en Python.

Vous pouvez la raccourcir en utilisant l'opérateur ternaire. Voici à quoi ressemble la syntaxe :

```txt
[option1] if [condition] else [option2]
```

Dans la syntaxe ci-dessus, `option1` sera exécutée si la `condition` est vraie. Si la condition est fausse, alors `option2` sera exécutée.

En d'autres termes, l'opérateur ternaire est simplement une forme abrégée des instructions `if` et `if...else`. Vous pouvez l'utiliser en une seule ligne de code.

Voici un exemple plus pratique :

```python
user_score = 90

print("Next level") if user_score > 50 else print("Repeat level")
```

Dans le code ci-dessus, "Next level" sera imprimé car la condition est vraie.

## Résumé

Dans cet article, nous avons parlé de l'opérateur ternaire en Python. C'est une manière plus courte d'écrire des instructions `if` et `if...else`.

Vous pouvez utiliser des opérateurs ternaires pour exécuter du code en fonction de conditions prédéfinies.

Bonne programmation ! Je parle également de Python sur [mon blog](https://ihechikara.com/).