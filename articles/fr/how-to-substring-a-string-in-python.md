---
title: Comment sous-chaîner une chaîne en Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-03T21:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-substring-a-string-in-python
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e45740569d1a4ca3c3e.jpg
tags:
- name: Python
  slug: python
seo_title: Comment sous-chaîner une chaîne en Python
seo_desc: 'Python offers many ways to substring a string. This is often called "slicing".

  Here is the syntax:

  string[start:end:step]


  Where,

  start: The starting index of the substring. The character at this index is included
  in the substring. If start is not in...'
---

Python offre de nombreuses façons de sous-chaîner une chaîne. Cela s'appelle souvent "slicing".

Voici la syntaxe :

```python
string[début:fin:pas]
```

Où,

`début` : L'index de départ de la sous-chaîne. Le caractère à cet index est inclus dans la sous-chaîne. Si `début` n'est pas inclus, il est supposé égal à 0.

`fin` : L'index de fin de la sous-chaîne. Le caractère à cet index n'est _pas_ inclus dans la sous-chaîne. Si `fin` n'est pas inclus, ou si la valeur spécifiée dépasse la longueur de la chaîne, il est supposé être égal à la longueur de la chaîne par défaut.

`pas` : Chaque caractère "pas" après le caractère actuel à inclure. La valeur par défaut est 1. Si `pas` n'est pas inclus, il est supposé être égal à 1.

### Voici un Scrim Interactif sur Comment Sous-chaîner une Chaîne en Python

<iframe src="https://scrimba.com/scrim/cPmJkytm?embed=freecodecamp,mini-header,no-sidebar" width="100%" height="420"></iframe>

## Utilisation Basique

`string[début:fin]` : Obtenir tous les caractères de `début` à `fin` - 1

`string[:fin]` : Obtenir tous les caractères du début de la chaîne à `fin` - 1

`string[début:]` : Obtenir tous les caractères de `début` à la fin de la chaîne

`string[début:fin:pas]` : Obtenir tous les caractères de `début` à `fin` - 1, en excluant chaque caractère `pas`

## Exemples

**1. **Obtenir les 5 premiers caractères d'une chaîne****

```python
string = "freeCodeCamp"
print(string[0:5])
```

Sortie :

```shell
> freeC
```

Note : `print(string[:5])` retourne le même résultat que `print(string[0:5])`

**2. **Obtenir une sous-chaîne de 4 caractères, commençant à partir du 3ème caractère de la chaîne****

```python
string = "freeCodeCamp"
print(string[2:6])
```

Sortie :

```shell
> eeCo
```

**3. **Obtenir le dernier caractère de la chaîne****

```python
string = "freeCodeCamp"
print(string[-1])
```

Sortie :

```shell
> p
```

Remarquez que l'index `début` ou `fin` peut être un nombre négatif. Un index négatif signifie que vous commencez à compter à partir de la fin de la chaîne au lieu du début (de droite à gauche).

L'index -1 représente le dernier caractère de la chaîne, -2 représente l'avant-dernier caractère, et ainsi de suite.

**4. **Obtenir les 5 derniers caractères d'une chaîne****

```python
string = "freeCodeCamp"
print(string[-5:])
```

Sortie :

```shell
> eCamp
```

**5. **Obtenir une sous-chaîne qui contient tous les caractères sauf les 4 derniers caractères et le 1er caractère****

```python
string = "freeCodeCamp"
print(string[1:-4])
```

Sortie :

```shell
> reeCode
```

**6. **Obtenir un caractère sur deux d'une chaîne****

```python
string = "freeCodeCamp"
print(string[::2])
```

Sortie :

```shell
> feCdCm
```