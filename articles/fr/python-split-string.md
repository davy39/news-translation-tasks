---
title: Python .split() – Diviser une chaîne de caractères en Python
subtitle: ''
author: Quincy Larson
co_authors: []
series: null
date: '2022-05-29T20:27:27.000Z'
originalURL: https://freecodecamp.org/news/python-split-string
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/mariana-jm-UvdzLNj1Vmk-unsplash_jpg.png
tags:
- name: Python
  slug: python
seo_title: Python .split() – Diviser une chaîne de caractères en Python
seo_desc: 'Do you want to turn a string into an array of strings using Python? One
  way to do this is with Python''s built-in .split() method.

  Here''s an example of how to do this in the Python command line:

  >>> string1 = "test your might"

  >>> string1.split(" ");

  ...'
---

Vous souhaitez transformer une chaîne de caractères en un tableau de chaînes de caractères en utilisant Python ? Une façon de faire cela est d'utiliser la méthode intégrée `.split()` de Python.

Voici un exemple de comment faire cela dans la ligne de commande Python :

```
>>> string1 = "test your might"
>>> string1.split(" ");
# Sortie : ['test', 'your', 'might']
```

Vous pouvez ouvrir le REPL Python à partir de votre ligne de commande. Python est intégré à Linux, Mac et Windows. J'ai écrit un guide sur comment vous pouvez [ouvrir la dernière version de Python à partir de votre terminal Mac](https://www.freecodecamp.org/news/python-version-on-mac-update/).

Notez que l'argument "," dans l'exemple ci-dessus est en fait facultatif. Regardez ceci :

```py
>>> string1 = "test your might"
>>> string1.split();
# Sortie : ['test', 'your', 'might']

>>> string2 = "test,your,might"
>>> s.split();
# Sortie : ['test', 'your', 'might']
```

La méthode `.split()` de Python est assez intelligente pour déduire quel devrait être le séparateur. Dans `string1`, j'ai utilisé un espace. Dans `string2`, j'ai utilisé une virgule. Dans les deux cas, cela a fonctionné.

## Comment utiliser Python .split() avec un séparateur spécifique

En pratique, vous voudrez passer un `séparateur` comme argument. Laissez-moi vous montrer comment faire cela :

```
>>> s = "test your might"
>>> s.split(" ");
# Sortie : ['test', 'your', 'might']

>>> s2 = "test,your,might"
>>> s.split(",");
# Sortie : ['test', 'your', 'might']
```

La sortie est la même, mais c'est plus propre. Voici une chaîne plus compliquée, où la spécification du séparateur fait une plus grande différence :

```
>>> string3 = "excellent, test your might, fight, mortal kombat"
>>> string3.split(",");
# Sortie : ['excellent', ' test your might', ' fight', ' mortal kombat']

>>> string3.split(" ");
# Sortie : ['excellent,', 'test', 'your', 'might,', 'fight,', 'mortal', 'kombat']
```

Comme vous pouvez le voir, il est plus sûr de spécifier un séparateur.

Notez également que les espaces de début et de fin peuvent être inclus dans certaines des chaînes de caractères de votre tableau résultant. Juste quelque chose à surveiller. 😉

## Comment diviser une chaîne de caractères en plusieurs chaînes de caractères en Python ?

Vous pouvez diviser une chaîne de caractères en autant de parties que vous le souhaitez. Tout dépend du caractère sur lequel vous souhaitez diviser la chaîne.

Mais si vous souhaitez vous assurer qu'une chaîne de caractères ne soit pas divisée en plus d'un certain nombre de parties, vous voudrez utiliser l'argument `maxsplit` dans votre appel de fonction.

## Comment diviser une chaîne de caractères en 3 parties en Python ?

Si vous souhaitez mettre une limite supérieure au nombre de parties dans lesquelles votre chaîne de caractères sera divisée, vous pouvez spécifier cela en utilisant l'argument `maxsplit`, comme ceci :

```python
string3 = "excellent, test your might, fight, mortal kombat"

print(string.split(" ", 3))

# Sortie : ['excellent,', 'test', 'your', 'might, fight, mortal kombat']
# maxsplit=3 signifie que la chaîne sera divisée en au plus trois parties
```

Comme vous pouvez le voir, la fonction `split` arrête simplement de diviser la chaîne après le 3ème espace, de sorte qu'un total de 4 chaînes se trouvent dans le tableau résultant.

J'espère que vous trouverez cela utile. Merci d'avoir lu, et bon codage. Si vous souhaitez en apprendre davantage, consultez [le programme de base de freeCodeCamp](https://www.freecodecamp.org/learn).