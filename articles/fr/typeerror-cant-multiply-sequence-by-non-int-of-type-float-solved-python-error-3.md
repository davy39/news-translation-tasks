---
title: 'TypeError: impossible de multiplier une séquence par un non-int de type float
  [Erreur Python Résolue]'
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-12-21T21:13:46.000Z'
originalURL: https://freecodecamp.org/news/typeerror-cant-multiply-sequence-by-non-int-of-type-float-solved-python-error-3
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/pexels-polina-zimmerman-3747132.jpg
tags:
- name: error
  slug: error
- name: error handling
  slug: error-handling
- name: Python
  slug: python
seo_title: 'TypeError: impossible de multiplier une séquence par un non-int de type
  float [Erreur Python Résolue]'
seo_desc: "Most times when you encounter errors while coding, you can discover the\
  \ reason why the error is occurring and how you can fix it in the error message.\
  \ \nThe Python error, \"TypeError: can't multiply sequence by non-int of type float\"\
  \ is no exception to..."
---

La plupart du temps, lorsque vous rencontrez des erreurs en codant, vous pouvez découvrir la raison pour laquelle l'erreur se produit et comment la corriger dans le message d'erreur. 

L'erreur Python, "TypeError: impossible de multiplier une séquence par un non-int de type float" n'est pas une exception à cela.

J'ai préparé cet article pour vous montrer pourquoi cette erreur se produit et comment vous pouvez la corriger. Continuez à lire.

## Pourquoi l'erreur "TypeError: impossible de multiplier une séquence par un non-int de type float" se produit

Pour comprendre pourquoi vous obtenez l'erreur "TypeError: impossible de multiplier une séquence par un non-int de type float", examinons les mots-clés dans l'erreur : **Typeerror**, **multiply**, **sequence**, et **type float**.

- **Typeerror** est une exception levée lorsque vous mettez ensemble des types de données inappropriés dans une opération
- **multiply** dans l'erreur signifie que vous essayez d'effectuer une multiplication
- **sequence** est un ensemble ordonné en Python. Il peut s'agir de chaînes de caractères, de listes ou de tuples.
- **type float** signifie qu'il y a un nombre décimal dans l'opération que vous essayez d'effectuer, par exemple, 2.4 ou 5.40

Donc, si vous obtenez cette erreur, cela signifie que vous multipliez l'une de ces séquences (généralement une chaîne de caractères ou un tuple) par un nombre à virgule flottante (nombre décimal).

En effet, vous pouvez multiplier une séquence par un nombre et Python effectuera correctement le travail :

```py
site_name = 'freeCodeCamp '

print(site_name * 2)
# freeCodeCamp freeCodeCamp 

print(site_name * 3)
# freeCodeCamp freeCodeCamp freeCodeCamp
```

```py
stringfied_num = '10 '

print(stringfied_num * 3)
# 10 10 10
```

La même chose fonctionne également pour les tuples :

```py
myTuple = (4, 3, 4)
print(myTuple * 2)

# (4, 3, 4, 4, 3, 4)
```

Mais si vous essayez de faire la multiplication avec un nombre à virgule flottante, vous obtenez l'erreur "TypeError: impossible de multiplier une séquence par un non-int de type float" :

```py
site_name = 'freeCodeCamp '

print(site_name * 2.5)
# Traceback (most recent call last):  
#   File "seq.py", line 3, in <module>
#     print(site_name * 2.5)
# TypeError: impossible de multiplier une séquence par un non-int de type 'float'
```

```py
myTuple = (4, 3, 4)
print(myTuple * 2.2)

# Traceback (most recent call last):   
#   File "seq.py", line 11, in <module>
#     print(myTuple * 2.2)
# TypeError: impossible de multiplier une séquence par un non-int de type 'float'
```

## Comment corriger l'erreur "TypeError: impossible de multiplier une séquence par un non-int de type 'float'"

Pour corriger l'erreur "TypeError: impossible de multiplier une séquence par un non-int de type 'float'", assurez-vous de ne pas multiplier la chaîne de caractères ou le tuple par un nombre à virgule flottante. 

Ainsi, au lieu de multiplier la chaîne de caractères ou le tuple par un nombre à virgule flottante, utilisez un entier. Par exemple, `"freeCodeCamp" * 5` au lieu de `"freeCodeCamp" * 5.6` :

```py
site_name = 'freeCodeCamp '
print(site_name * 5)

# freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp
```

Si vous traitez un nombre sous forme de chaîne de caractères, par exemple "10", vous pouvez convertir la chaîne en entier avec la méthode `int()` et en flottant avec la méthode `float()` :

```py
stringfied_num = '10 '

print(int(stringfied_num) * 3)
# 30
```
```py
stringfied_num = '10 '

print(float(stringfied_num) * 3)
# 30
```

Si vous traitez une entrée utilisateur, vous pouvez également trouver un moyen de convertir le nombre à virgule flottante en un entier. En fait, vous devriez gérer la possibilité que l'utilisateur entre un nombre à virgule flottante au lieu d'un entier :

```py
# déclarer une variable de chaîne de caractères
site_name = 'freeCodeCamp '

# Obtenir l'entrée de l'utilisateur et la convertir en un nombre décimal
user_input = float(input("Entrez un nombre : "))

# Arrondir le nombre entré par l'utilisateur au nombre entier le plus proche
rounded_input = round(user_input)

# Multiplier la variable site_name par l'entrée de l'utilisateur
result = rounded_input * site_name

# Afficher le résultat dans la console
print(result)

# J'ai entré 3.6 et le résultat était : freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp
```

## Conclusion
Vous ne pouvez pas multiplier une séquence par un nombre à virgule flottante. Ce que vous obtenez si vous faites cela est l'erreur, TypeError: impossible de multiplier une séquence par un non-int de type 'float'. C'est pourquoi cet article était dédié à vous faire savoir comment corriger l'erreur.

Le point à retenir de cet article est que si vous utilisez une chaîne de caractères comme un nombre, vous devez vous assurer qu'elle est convertie avec la méthode `float()` — surtout si elle est utilisée dans un calcul.