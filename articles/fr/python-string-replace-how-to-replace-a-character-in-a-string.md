---
title: Python string.replace() – Comment remplacer un caractère dans une chaîne
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-09-01T21:59:34.000Z'
originalURL: https://freecodecamp.org/news/python-string-replace-how-to-replace-a-character-in-a-string
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/string-replace.png
tags:
- name: Python
  slug: python
seo_title: Python string.replace() – Comment remplacer un caractère dans une chaîne
seo_desc: "By Dillion Megida\nPython has numerous string modifying methods, and one\
  \ of them is the replace method. \nIn this article, I'll show you how this method\
  \ can be used to replace a character in a string.\nHow the replace Method Works\
  \ in Python\nThe replace ..."
---

Par Dillion Megida

Python possède de nombreuses méthodes de modification de chaînes de caractères, et l'une d'elles est la méthode `replace`.

Dans cet article, je vais vous montrer comment utiliser cette méthode pour remplacer un caractère dans une chaîne.

## Comment fonctionne la méthode `replace` en Python

La méthode `replace` de chaîne de caractères retourne une nouvelle chaîne avec certains caractères de la chaîne originale remplacés par de nouveaux. La chaîne originale n'est pas affectée ni modifiée.

La syntaxe de la méthode `replace` est :

```python
string.replace(old_char, new_char, count)
```

L'argument `old_char` est l'ensemble des caractères à remplacer.

L'argument `new_char` est l'ensemble des caractères qui remplacent `old_char`.

L'argument `count`, qui est optionnel, spécifie combien d'occurrences seront remplacées. Si cela n'est pas spécifié, toutes les occurrences de `old_char` seront remplacées par `new_char`.

Voyons quelques exemples.

## Exemples de `string.replace()`

Voici un exemple qui remplace "JavaScript" par "PHP" dans une chaîne :

```python
str = "I love JavaScript. I prefer JavaScript to Python because JavaScript looks more beautiful"

new_str = str.replace("JavaScript", "PHP")

print(new_str)
# I love PHP. I prefer PHP to Python because PHP looks more beautiful
```

Vous pouvez voir comment la méthode `replace` remplace les occurrences de "JavaScript" par "PHP".

Dans cet exemple, les trois occurrences de "JavaScript" sont remplacées par "PHP". Que faire si vous ne vouliez remplacer qu'une seule occurrence ? Vous pouvez alors utiliser l'argument `count` comme ceci :

```python
str = "I love JavaScript. I prefer JavaScript to Python because JavaScript looks more beautiful"

new_str = str.replace("JavaScript", "PHP", 1)

print(new_str)
# I love PHP. I prefer JavaScript to Python because JavaScript looks more beautiful
```

En appliquant un argument `count` de **1**, vous pouvez voir que seul le premier "JavaScript" (la première occurrence) est remplacé par "PHP". Les autres "JavaScript" restent inchangés.

## Quand utiliser la méthode `replace` en Python

Un bon cas d'utilisation de cette méthode est de remplacer des caractères dans l'entrée d'un utilisateur pour répondre à une certaine norme.

Supposons, par exemple, que vous souhaitiez que les utilisateurs entrent leurs noms d'utilisateur mais que vous ne vouliez pas de caractères d'espace dans le nom d'utilisateur. Vous pouvez utiliser la méthode `replace` pour remplacer les espaces dans les chaînes soumises par un trait d'union. Voici comment faire :

```python
user_input = "python my favorite"

updated_username = user_input.replace(" ", "-")

print(updated_username)
# python-my-favorite
```

D'après le résultat de la méthode `replace`, vous pouvez voir que les espaces ont été remplacés par des traits d'union, ce qui répond à votre norme.

## Conclusion

La méthode `replace` remplace une sous-chaîne existante dans une chaîne par une nouvelle sous-chaîne. Vous spécifiez combien d'occurrences de la sous-chaîne existante doivent être remplacées avec l'argument `count` de la méthode.