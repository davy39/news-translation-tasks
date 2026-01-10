---
title: Séquences d'échappement en Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-03T22:21:00.000Z'
originalURL: https://freecodecamp.org/news/escape-sequences-python
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e3b740569d1a4ca3c0a.jpg
tags:
- name: Python
  slug: python
- name: toothbrush
  slug: toothbrush
seo_title: Séquences d'échappement en Python
seo_desc: 'Escape sequences allow you to include special characters in strings. To
  do this, simply add a backslash (\) before the character you want to escape.

  For example, imagine you initialized a string with single quotes:

  s = ''Hey, whats up?''

  print(s)


  Outp...'
---

Les séquences d'échappement vous permettent d'inclure des caractères spéciaux dans les chaînes de caractères. Pour ce faire, il suffit d'ajouter une barre oblique inverse (`\`) avant le caractère que vous souhaitez échapper.

Par exemple, imaginez que vous avez initialisé une chaîne de caractères avec des guillemets simples :

```py
s = 'Hey, whats up?'
print(s)
```

**Sortie :**

```sh
Hey, whats up?
```

Mais si vous incluez une apostrophe sans l'échapper, vous obtiendrez une erreur :

```py
s = 'Hey, what's up?'
print(s)
```

**Sortie :**

```sh
  File "main.py", line 1
    s = 'Hey, what's up?'
                   ^
SyntaxError: invalid syntax
```

Pour corriger cela, il suffit d'échapper l'apostrophe :

```py
s = 'Hey, what\'s up?'
print(s)
```

Pour ajouter des sauts de ligne à votre chaîne de caractères, utilisez `\n` :

```
print("Multiline strings\ncan be created\nusing escape sequences.")
```

**Sortie :**

```
Multiline strings
can be created
using escape sequences.
```

Une chose importante à retenir est que, si vous souhaitez inclure un caractère de barre oblique inverse dans une chaîne de caractères, vous devrez l'échapper. Par exemple, si vous souhaitez imprimer un chemin de répertoire sous Windows, vous devrez échapper chaque barre oblique inverse dans la chaîne :

```py
print("C:\\Users\\Pat\\Desktop")
```

**Sortie :**

```
C:\Users\Pat\Desktop
```

## Chaînes de caractères brutes

Une chaîne de caractères _brute_ peut être utilisée en préférant la chaîne avec `r` ou `R`, ce qui permet d'inclure des barres obliques inverses sans avoir besoin de les échapper. Par exemple :

```py
print(r"Backslashes \ don't need to be escaped in raw strings.")

```

**Sortie :**

```
Backslashes \ don't need to be escaped in raw strings.
```

Mais gardez à l'esprit que les barres obliques inverses non échappées à la fin d'une chaîne brute provoqueront une erreur :

```
print(r"There's an unescaped backslash at the end of this string\")
```

**Sortie :**

```
  File "main.py", line 1
    print(r"There's an unescaped backslash at the end of this string\")
                                                                      ^
SyntaxError: EOL while scanning string literal
```

# Séquences d'échappement courantes

| Séquence d'échappement | Signification |
| ---- | ---- |
| \\ | Barre oblique inverse (`\`) |
| \' | Guillemet simple (`'`) |
| \" | Guillemet double (`"`) |
| \n | Saut de ligne ASCII (ajoute une nouvelle ligne) |
| \b | Retour arrière ASCII |

Une liste complète des séquences d'échappement peut être trouvée [ici](https://docs.python.org/3/reference/lexical_analysis.html#strings) dans la documentation Python.