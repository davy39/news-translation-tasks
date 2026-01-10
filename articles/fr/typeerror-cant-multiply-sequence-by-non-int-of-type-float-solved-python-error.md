---
title: 'TypeError: can''t multiply sequence by non-int of type float [Erreur Python
  Résolue]'
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-11-02T16:36:15.000Z'
originalURL: https://freecodecamp.org/news/typeerror-cant-multiply-sequence-by-non-int-of-type-float-solved-python-error
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/pexels-pixabay-355948.jpg
tags:
- name: error
  slug: error
- name: error handling
  slug: error-handling
- name: Python
  slug: python
seo_title: 'TypeError: can''t multiply sequence by non-int of type float [Erreur Python
  Résolue]'
seo_desc: 'In this article, you will learn what the Python error TypeError: can''t
  multiply sequence by non-int of type float means.

  Firstly, I will explain why this error gets raised. You will also learn how to solve
  the error and how to avoid it in the first p...'
---

Dans cet article, vous apprendrez ce que signifie l'erreur Python `TypeError: can't multiply sequence by non-int of type float`.

Tout d'abord, je vais expliquer pourquoi cette erreur est levée. Vous apprendrez également comment résoudre l'erreur et comment l'éviter dès le départ.

Voici ce que nous allons couvrir :

1. [Qu'est-ce que l'erreur `TypeError: can't multiply sequence by non-int of type float` en Python ?](#intro)
    1. [Comment l'erreur `TypeError: can't multiply sequence by non-int of type float` se produit-elle en Python ?](#raison)
2. [Comment résoudre l'erreur `TypeError: can't multiply sequence by non-int of type float` en Python](#solution)

## Qu'est-ce que l'erreur `TypeError: can't multiply sequence by non-int of type float` en Python ? <a name="intro"></a>

Il existe deux types de nombres en Python :

- les entiers – nombres entiers qui peuvent être positifs, négatifs ou nuls.
- les nombres à virgule flottante – nombres positifs ou négatifs avec un point décimal.

Vous pouvez multiplier un entier avec une chaîne de caractères pour créer une séquence répétée de caractères :

```python
print("Python" * 3)

# sortie

# PythonPythonPython
```

Et pour rappel, les chaînes de caractères sont tous caractères enfermés dans des guillemets simples ou doubles – y compris les nombres :

```python
print("3" * 3)

# sortie

# 333
```

Mais regardez ce qui se passe lorsque vous essayez de multiplier une chaîne de caractères avec un nombre à virgule flottante :

```python
print("3" * 3.3)

# sortie

# Traceback (most recent call last):
#  File "main.py", line 1, in <module>
#    print("3" * 3.3)
# TypeError: can't multiply sequence by non-int of type 'float'
```

Une erreur est levée – spécifiquement une `TypeError`.

Une `TypeError` est une exception en Python qui est levée lorsque vous essayez d'effectuer une opération sur un type de données qui ne supporte pas cette opération spécifique.

Comme le message d'erreur vous l'indique, vous ne pouvez pas effectuer de multiplication entre une chaîne de caractères (ou séquence) et un nombre à virgule flottante (ou float), car Python ne supporte pas cette opération entre ces deux types de données.

### Comment l'erreur `TypeError: can't multiply sequence by non-int of type float` se produit-elle en Python ? <a name="raison"></a>

L'erreur `TypeError: can't multiply sequence by non-int of type float` se produit couramment lorsque vous utilisez la fonction `input()` de Python, qui prend l'entrée de l'utilisateur. Cela est dû au fait que, par défaut, la fonction `input()` retourne l'entrée de l'utilisateur sous forme de chaîne de caractères.

Prenons l'exemple hypothétique suivant. Supposons que je demande à un utilisateur d'entrer son âge et que je stocke sa réponse dans une variable nommée `user_age` :

```python
user_age = input("Veuillez entrer votre âge : ")
```

Je peux vérifier le type de données de la valeur stockée dans la variable `user_age` en utilisant la fonction `type()` puis afficher le résultat dans la console :

```python
user_age = input("Veuillez entrer votre âge : ")

print(type(user_age))

# sortie

# Veuillez entrer votre âge : 29
# <class 'str'>
```

D'après la sortie, vous pouvez voir que même si j'ai entré un entier, le type de données retourné est de type chaîne de caractères.

Si je voulais ensuite, pour une raison quelconque, multiplier l'âge de l'utilisateur avec un nombre à virgule flottante, j'obtiendrais l'erreur `TypeError: can't multiply sequence by non-int of type float` :

```python
user_age = input("Veuillez entrer votre âge : ")

print(user_age * 0.5)

# sortie

# Veuillez entrer votre âge : 29
# Traceback (most recent call last):
#  File "main.py", line 3, in <module>
#    print(user_age * 0.5)
# TypeError: can't multiply sequence by non-int of type 'float'
```

## Comment résoudre l'erreur `TypeError: can't multiply sequence by non-int of type float` en Python <a name="solution"></a>

Pour résoudre l'erreur `TypeError: can't multiply sequence by non-int of type float`, convertissez la chaîne de caractères en un nombre à virgule flottante avant de la multiplier avec un float.

Comme vous l'avez vu précédemment, ce qui suit lève l'erreur `TypeError: can't multiply sequence by non-int of type float` :

```python
print("3" * 3.3)

# sortie

# Traceback (most recent call last):
#  File "main.py", line 1, in <module>
#    print("3" * 3.3)
# TypeError: can't multiply sequence by non-int of type 'float'
```

Si vous convertissez la chaîne `"3"` en un float avant de la multiplier avec le nombre à virgule flottante `3.3`, il n'y aura pas d'erreur.

Pour convertir une chaîne en un float, utilisez la fonction `float()` :

```python
print(float("3") * 3.3)

# sortie

# 9.899999999999999
```

Et vous pouvez faire de même lorsque vous utilisez la fonction `input()`. Convertissez la valeur entrée par l'utilisateur en un nombre à virgule flottante en utilisant la fonction `float()`.

Voici comment vous réécririez l'exemple utilisant la fonction `input()` de tout à l'heure :

```python
user_age = float(input("Veuillez entrer votre âge : "))

print(user_age * 0.5)

# sortie

# Veuillez entrer votre âge : 29
# 14.5
```

La fonction `float()` convertit la valeur de chaîne retournée par la fonction `input()` en un nombre à virgule flottante, et vous pouvez multiplier cette valeur avec un nombre à virgule flottante.

## Conclusion

Et voilà ! Vous savez maintenant comment résoudre l'erreur `TypeError: can't multiply sequence by non-int of type float` en Python !

J'espère que vous avez trouvé ce tutoriel utile.

Pour en savoir plus sur le langage de programmation Python, consultez la [certification Python](https://www.freecodecamp.org/learn/scientific-computing-with-python/) de freeCodeCamp.

Vous commenerez par les bases et apprendrez de manière interactive et adaptée aux débutants. Vous construirez également cinq projets à la fin pour mettre en pratique et renforcer ce que vous avez appris.

Merci d'avoir lu, et bon codage !