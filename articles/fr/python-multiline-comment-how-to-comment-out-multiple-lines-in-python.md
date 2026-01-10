---
title: Commentaire multiligne en Python – Comment commenter plusieurs lignes en Python
date: '2022-02-28T17:54:47.000Z'
author: Kolade Chris
authorURL: https://www.freecodecamp.org/news/author/koladechris/
originalURL: https://freecodecamp.org/news/python-multiline-comment-how-to-comment-out-multiple-lines-in-python
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/ear-g3dcf79b5f_1280-1.png
tags:
- name: Python
  slug: python
- name: Python 3
  slug: python3
seo_desc: 'Commenting is an integral part of every programming language. With comments,
  you get a better understanding of your own code, make it more readable, and can
  help team members understand how it works.

  Comments are ignored by compilers and interpreters...'
---


Le commentaire est une partie intégrante de tout langage de programmation. Avec les commentaires, vous obtenez une meilleure compréhension de votre propre code, vous le rendez plus lisible et vous pouvez aider les membres de votre équipe à comprendre son fonctionnement.

<!-- more -->

Les commentaires sont ignorés par les compilateurs et les interpréteurs, ils ne sont donc pas exécutés.

En plus de rendre votre code plus lisible, les commentaires peuvent également être utiles lors du débogage – si vous avez deux lignes de code, vous pouvez en commenter une pour empêcher son exécution.

Tout comme les autres langages de programmation, Python prend en charge les commentaires.

Le problème est que Python ne dispose pas de mécanisme intégré pour les commentaires multilignes.

Ainsi, dans cet article, je ne vais pas seulement vous montrer comment créer des commentaires sur une seule ligne en Python – je vous montrerai également la solution de contournement pour créer des commentaires multilignes.

## Comment créer des commentaires sur une seule ligne en Python

Pour créer des commentaires sur une seule ligne en Python, faites précéder chaque ligne d'un dièse (`#`).

```
# print("Hello world")

print("Hello campers")
```

Sortie :

```
Hello campers
```

Comme vous pouvez le voir, la ligne commentée n'a pas été affichée dans la sortie.

## Comment créer des commentaires multilignes en Python

Contrairement à d'autres langages de programmation tels que JavaScript, Java et C++ qui utilisent `/*...*/` pour les commentaires multilignes, il n'existe pas de mécanisme intégré pour les commentaires multilignes en Python.

Pour commenter plusieurs lignes en Python, vous pouvez faire précéder chaque ligne d'un dièse (`#`).

```
# print("Hello world")
# print("Hello universe")
# print("Hello everyone")

print("Hello campers")
```

Sortie :

```
Hello campers
```

Avec cette approche, vous créez techniquement plusieurs commentaires sur une seule ligne.

La véritable solution de contournement pour créer des commentaires multilignes en Python consiste à utiliser des **docstrings**.

Si vous utilisez une docstring pour commenter plusieurs lignes de code en Python, ce bloc de code sera ignoré et seules les lignes situées à l'extérieur de la docstring seront exécutées.

```
"""
This is a multi-line comment with docstrings

print("Hello world")
print("Hello universe")
print("Hello everyone")
"""

print("Hello campers")
```

Sortie :

```
Hello campers
```

**NB :** Une chose à noter est que lors de l'utilisation de docstrings pour commenter, l'indentation compte toujours. Si vous utilisez 4 espaces (ou une tabulation) pour l'indentation, vous obtiendrez une erreur d'indentation.

Par exemple, ceci fonctionnera :

```
def addNumbers(num1, num2, num3):
    """
    A function that returns the sum of
    3 numbers
    """
    return num1 + num2 + num3
print(addNumbers(2, 3, 4))

# Output: 9
```

Mais ceci ne fonctionnera pas :

```
def addNumbers(num1, num2, num3):
"""
A function that returns the sum of
3 numbers
"""
    return num1 + num2 + num3
print(addNumbers(2, 3, 4))
```

Votre IDE renverra alors l'erreur "`IndentationError: expected an indented block`".

## Conclusion

Puisqu'il n'y a pas de support intégré pour les commentaires multilignes en Python, cet article démontre comment vous pouvez utiliser les docstrings comme solution de contournement.

Cependant, vous devriez généralement vous en tenir à l'utilisation des commentaires Python habituels avec un dièse (`#`), même si vous devez l'utiliser pour plusieurs lignes. En effet, les docstrings sont destinées à la documentation et non à la mise en commentaire du code.

Si vous avez trouvé cet article utile, n'hésitez pas à le partager avec vos amis et votre famille.

Merci de votre lecture.