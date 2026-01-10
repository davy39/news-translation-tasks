---
title: Python strip() – Comment rogner une chaîne ou une ligne
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-01-12T20:48:03.000Z'
originalURL: https://freecodecamp.org/news/python-strip-how-to-trim-a-string-or-line
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/aleksander-vlad-jiVeo0i1EB4-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: Python strip() – Comment rogner une chaîne ou une ligne
seo_desc: "In this article, you'll learn how to trim a string in Python using the\
  \ .strip() method. \nYou'll also see how to use the .lstrip() and .rstrip() methods,\
  \ which are the counterparts to .strip().\nLet's get started!\nHow to trim a string\
  \ in Python\nPython ..."
---

Dans cet article, vous apprendrez à rogner une chaîne en Python en utilisant la méthode `.strip()`.

Vous verrez également comment utiliser les méthodes `.lstrip()` et `.rstrip()`, qui sont les équivalents de `.strip()`.

Commençons !

## Comment rogner une chaîne en Python

Python dispose de **trois** méthodes intégrées pour rogner les espaces et caractères de début et de fin des chaînes.

- `.strip()`
- `.lstrip()`
- `.rstrip()`

Chaque méthode retourne une nouvelle chaîne rognée.

### Comment supprimer les espaces de début et de fin des chaînes en Python

Lorsque la méthode `.strip()` n'a pas d'argument, elle supprime tout espace de début et/ou de fin d'une chaîne.

Ainsi, si vous avez des espaces au début et/ou à la fin d'un mot ou d'une phrase, `.strip()` seul, par défaut, les supprimera.

La variable suivante `greeting` contient la chaîne "Hello" avec des espaces à droite et à gauche.

```python
greeting = "     Hello!  "

print(greeting, "How are you?")

#output
#     Hello!   How are you?
```

Pour les supprimer, vous utilisez la méthode `.strip()`, comme ceci :

```python
greeting = "     Hello!  "

stripped_greeting = greeting.strip()

print(stripped_greeting, "How are you?")

#output
#Hello! How are you?
```

Vous auriez également pu utiliser la méthode `.strip()` de cette manière :

```python
greeting = "     Hello!  "

print(greeting.strip(), "How are you?")

#output
#Hello! How are you?
```

### Comment supprimer les caractères de début et de fin des chaînes en Python

La méthode `.strip()` accepte des *caractères optionnels* passés en arguments.

Les caractères que vous ajoutez en arguments spécifient quels caractères vous souhaitez supprimer du début et de la fin de la chaîne.

Voici la syntaxe générale pour ce cas :

```python
str.strip(char)
```

Les caractères que vous spécifiez sont enfermés entre guillemets.

Par exemple, supposons que vous avez la chaîne suivante :

```python
greeting = "Hello World?"
```

Vous souhaitez supprimer "H" et "?", qui se trouvent respectivement au début et à la fin de la chaîne.

Pour les supprimer, vous passez les deux caractères en arguments à `strip()`.

```python
greeting = "Hello World?"

stripped_greeting = greeting.strip("H?")

print(stripped_greeting)

#output
#ello World
```

Remarquez ce qui se passe lorsque vous souhaitez supprimer "W" de "World", qui se trouve au milieu et non au début ou à la fin de la chaîne, et que vous l'incluez en tant qu'argument :

```python
greeting = "Hello World?"

stripped_greeting = greeting.strip("HW?")

print(stripped_greeting)
#ello World
```

Il ne sera pas supprimé ! Seuls les caractères au **début** et à la **fin** de ladite chaîne sont supprimés.

Cela dit, regardez l'exemple suivant.

Supposons que vous souhaitez supprimer les deux premiers et les deux derniers caractères de la chaîne :

```python
phrase = "Hello world?"

stripped_phrase = phrase.strip("Hed?")

print(stripped_phrase)

#output
#llo worl
```

Les deux premiers caractères ("He") et les deux derniers ("d?") de la chaîne ont été supprimés.

Une autre chose à noter est que l'argument ne supprime pas seulement la première occurrence du caractère spécifié.

Par exemple, supposons que vous avez une chaîne avec quelques points au début et quelques points d'exclamation à la fin :

```python
phrase = ".....Python !!!"
```

Lorsque vous spécifiez `.` et `!` comme arguments, toutes les occurrences des deux seront supprimées :

```python
phrase = ".....Python !!!"

stripped_phrase = phrase.strip(".!")

print(stripped_phrase)

#output
#Python 
```

### Comment supprimer uniquement les espaces et caractères de début des chaînes en Python

Pour supprimer *uniquement* les espaces et caractères de début, utilisez `.lstrip()`.

Cela est utile lorsque vous souhaitez supprimer les espaces et caractères uniquement du début de la chaîne.

Un exemple serait de supprimer le `www.` d'un nom de domaine.

```python
domain_name = "www.freecodecamp.org www."

stripped_domain = domain_name.lstrip("w.")

print(stripped_domain)

#output
#freecodecamp.org www.
```

Dans cet exemple, j'ai utilisé les caractères `w` et `.` à la fois au début et à la fin de la chaîne pour montrer comment `.lstrip()` fonctionne.

Si j'avais utilisé `.strip(w.)`, j'aurais obtenu le résultat suivant :

```python
freecodecamp.org 
```

Il en va de même pour la suppression des espaces.

Prenons un exemple d'une section précédente :

```python
greeting = "     Hello!  "

stripped_greeting = greeting.lstrip()

print(stripped_greeting, "How are you?")

#output
#Hello!   How are you?
```

Seuls les espaces du début de la chaîne ont été supprimés de la sortie.

### Comment supprimer uniquement les espaces et caractères de fin des chaînes en Python

Pour supprimer *uniquement* les espaces et caractères de fin, utilisez la méthode `.rstrip()`.

Supposons que vous souhaitiez supprimer toute la ponctuation uniquement de la fin d'une chaîne.

Vous feriez ce qui suit :

```python
enthusiastic_greeting = "!!! Hello !!!!!"

less_enthusiastic_greeting = enthusiastic_greeting.rstrip("!")

print(less_enthusiastic_greeting)

#output
#!!! Hello 
```

Il en va de même pour les espaces.

En reprenant l'exemple précédent, cette fois-ci, les espaces seraient supprimés uniquement de la fin de la sortie :

```python
greeting = "     Hello!  "

stripped_greeting = greeting.rstrip()

print(stripped_greeting, "How are you?")

#output
#     Hello! How are you?
```

## Conclusion

Et voilà ! Vous connaissez maintenant les bases de la façon de rogner une chaîne en Python.

Pour résumer :

- Utilisez la méthode `.strip()` pour supprimer les espaces et caractères du **début** et de la **fin** d'une chaîne.
- Utilisez la méthode `.lstrip()` pour supprimer les espaces et caractères uniquement du **début** d'une chaîne.
- Utilisez la méthode `.rstrip()` pour supprimer les espaces et caractères uniquement de la **fin** d'une chaîne.

Si vous souhaitez en savoir plus sur Python, consultez la [Certification Python](https://www.freecodecamp.org/learn/scientific-computing-with-python/) de freeCodeCamp. Vous commencerez à apprendre de manière interactive et adaptée aux débutants. Vous construirez également cinq projets à la fin pour mettre en pratique et renforcer ce que vous avez appris.

Merci d'avoir lu et bon codage !