---
title: Rogner une chaîne en Python – Comment supprimer les espaces de fin
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2023-03-03T17:28:17.000Z'
originalURL: https://freecodecamp.org/news/how-to-strip-trailing-whitespace-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/pexels-christina-morillo-1181359.jpg
tags:
- name: Python
  slug: python
seo_title: Rogner une chaîne en Python – Comment supprimer les espaces de fin
seo_desc: 'Python has three built-in methods for trimming leading and trailing whitespace
  and characters from strings: strip(), lstrip(), and rstrip().

  In this article, I will explain how to remove trailing whitespace in Python using
  the rstrip() method.

  Let''s ...'
---

Python dispose de trois méthodes intégrées pour supprimer les espaces et les caractères de début et de fin des chaînes : `strip()`, `lstrip()` et `rstrip()`.

Dans cet article, je vais expliquer comment supprimer les espaces de fin en Python en utilisant la méthode `rstrip()`.

Commençons !

## Comment supprimer les espaces d'une chaîne en Python
Pour rogner une chaîne et supprimer tous les espaces, qu'ils soient en début ou en fin, utilisez la méthode `strip()`.

Lorsque la méthode `strip()` n'a pas d'argument, elle supprime à la fois les espaces de début et de fin d'une chaîne.

Ainsi, si vous avez des espaces au début ou à la fin d'un mot ou d'une phrase, `strip()` seul, par défaut, les supprimera.

Prenons l'exemple suivant :

```python
fave_phrase = " Hello World "
```

J'ai stocké la phrase `" Hello World "` dans une variable nommée `fave_phrase`.

La phrase a un espace de début — un espace avant le premier caractère, `H`.

La phrase a également un espace de fin — un espace après le dernier caractère, `d`.

J'affiche ensuite le contenu de `fave_phrase` dans la console :

```python
print(fave_phrase)

# sortie

 Hello World 
```

Pour supprimer à la fois les espaces de début *et* de fin de la phrase, appelez la méthode `strip()` sur `fave_phrase` et stockez le résultat dans la variable nommée `trimmed_fave_phrase` comme suit :

```python
fave_phrase = " Hello World "

trimmed_fave_phrase = fave_phrase.strip()

print(trimmed_fave_phrase)

# sortie

Hello World
```

Maintenant, tous les espaces au début et à la fin de la chaîne ont disparu !

### Comment supprimer uniquement les espaces de fin en Python
Mais que faire si vous souhaitez supprimer uniquement les espaces de fin (c'est-à-dire tous les espaces à la fin de la chaîne) ?

Python dispose de la méthode `rstrip()` que vous pouvez utiliser pour faire exactement cela :

```python
fave_phrase = " Hello World "

trimmed_fave_phrase = fave_phrase.rstrip()

print(trimmed_fave_phrase)

# sortie

 Hello World
```

Dans l'exemple ci-dessus, l'espace de début au début de la chaîne reste préservé, et l'espace de fin est supprimé.

Ainsi, avec `rstrip()`, les espaces sont supprimés uniquement à la fin de la chaîne.

## Conclusion
Et voilà ! Vous savez maintenant comment supprimer les espaces de fin d'une chaîne en Python.

Pour en savoir plus sur Python, consultez [le cours Python pour débutants de freeCodeCamp](https://www.freecodecamp.org/news/python-programming-course/).

Merci d'avoir lu, et bon codage !