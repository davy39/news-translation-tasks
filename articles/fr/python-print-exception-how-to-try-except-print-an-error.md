---
title: Python Print Exception – Comment utiliser Try-Except pour afficher une erreur
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-03-15T21:31:00.000Z'
originalURL: https://freecodecamp.org/news/python-print-exception-how-to-try-except-print-an-error
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/pythonExceptionHandling.png
tags:
- name: error handling
  slug: error-handling
- name: Python
  slug: python
seo_title: Python Print Exception – Comment utiliser Try-Except pour afficher une
  erreur
seo_desc: "Every programming language has its way of handling exceptions and errors,\
  \ and Python is no exception. \nPython comes with a built-in try…except syntax with\
  \ which you can handle errors and stop them from interrupting the running of your\
  \ program.\nIn thi..."
---

Chaque langage de programmation a sa propre façon de gérer les exceptions et les erreurs, et Python ne fait pas exception.

Python est livré avec une syntaxe intégrée `try…except` qui vous permet de gérer les erreurs et d'empêcher qu'elles n'interrompent l'exécution de votre programme.

Dans cet article, vous apprendrez à utiliser cette syntaxe `try…except` pour gérer les exceptions dans votre code afin qu'elles n'arrêtent pas l'exécution de votre programme.


## Ce que nous allons aborder
- [Qu'est-ce qu'une exception ?](#heading-quest-ce-quune-exception)
- [La syntaxe `try…except`](#heading-la-syntaxe-tryexcept)
- [Comment gérer les exceptions avec `try…except`](#heading-comment-gerer-les-exceptions-avec-tryexcept)
- [Comment afficher une exception avec `try…except`](#heading-comment-afficher-une-exception-avec-tryexcept)
- [Comment afficher le nom de l'exception](#heading-comment-afficher-le-nom-de-lexception)
- [Conclusion](#heading-conclusion)


## Qu'est-ce qu'une exception ?
En Python, une exception est un objet d'erreur. C'est une erreur qui survient lors de l'exécution de votre programme et qui l'arrête — affichant par la suite un message d'erreur.

Lorsqu'une exception se produit, Python crée un objet d'exception qui contient le type de l'erreur et la ligne qu'elle affecte.

Python possède de nombreuses exceptions intégrées telles que `IndexError`, `NameError`, `TypeError`, `ValueError`, `ZeroDivisionError`, `KeyError`, et bien d'autres encore.


## La syntaxe `try…except`
Au lieu de laisser ces exceptions arrêter l'exécution de votre programme, vous pouvez placer le code que vous souhaitez exécuter dans un bloc `try` et gérer l'exception dans le bloc `except`.

La syntaxe de base de `try…except` ressemble à ceci :
```py
try:
  # code à exécuter
except:
  # gérer l'erreur
```


## Comment gérer les exceptions avec `try…except`
Vous pouvez gérer chacune des exceptions mentionnées dans cet article avec `try…except`. En fait, vous pouvez gérer toutes les exceptions en Python avec `try…except`.

Par exemple, si vous avez un programme volumineux et que vous ne savez pas si un identifiant existe ou non, vous pouvez exécuter ce que vous voulez faire avec l'identifiant dans un bloc `try` et gérer une éventuelle erreur dans le bloc `except` :

```py
try:
  print("Voici la variable x :", x)
except:
  print("Une erreur est survenue") # Une erreur est survenue
```

Vous pouvez voir que le bloc `except` s'est exécuté parce qu'il n'y a pas de variable nommée `x` dans le code.

Continuez votre lecture, car je vais vous montrer comment rendre ces erreurs plus présentables en vous expliquant comment gérer les exceptions avec élégance.


## Comment afficher une exception avec `try…except`
Mais que faire si vous souhaitez afficher l'exception exacte qui s'est produite ? Vous pouvez le faire en assignant l'`Exception` à une variable juste devant le mot-clé `except`.

Lorsque vous faites cela et que vous affichez l'Exception dans le terminal, c'est la valeur de l'`Exception` que vous obtenez.

Voici comment j'ai affiché l'exception `ZeroDivisionError` dans le terminal :

```py
try:
    res = 190 / 0
except Exception as error:
    # gérer l'exception
    print("Une exception est survenue :", error) # Une exception est survenue : division by zero
```

Et voici comment j'ai également affiché l'exception `NameError` :

```py
try:
  print("Voici la variable x :", x)
except Exception as error:
  print("Une erreur est survenue :", error) # Une erreur est survenue : name 'x' is not defined
```

Vous pouvez suivre ce modèle pour afficher n'importe quelle exception dans le terminal.


## Comment afficher le nom de l'exception
Et si vous voulez obtenir le nom exact de l'exception et l'afficher dans le terminal ? C'est également possible. Tout ce que vous avez à faire est d'utiliser la fonction `type()` pour obtenir le type de l'exception, puis d'utiliser l'attribut `__name__` pour obtenir le nom de l'exception.

Voici comment j'ai modifié l'exemple `ZeroDivisionError` pour afficher l'exception exacte :

```py
try:
    res = 190 / 0
except Exception as error:
    # gérer l'exception
    print("Une exception est survenue :", type(error).__name__) # Une exception est survenue : ZeroDivisionError
```

Et voici comment j'ai modifié l'autre exemple pour afficher l'exemple `NameError` :

```py
try:
  print("Voici la variable x :", x)
except Exception as error:
  print("Une erreur est survenue :", type(error).__name__) # Une erreur est survenue : NameError
```

Normalement, lorsque vous rencontrez une exception telle que `NameError` et `ZeroDivisionError`, par exemple, vous obtenez l'erreur dans le terminal de cette façon :

![Screenshot-2023-03-13-at-17.58.33](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-13-at-17.58.33.png)

![Screenshot-2023-03-13-at-17.58.54](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-13-at-17.58.54.png) 

Vous pouvez combiner la fonction `type()` et cette variable d'erreur pour rendre l'exception plus lisible :

```py
try:
  print("Voici la variable x :", x)
except Exception as error:
  print("Une erreur est survenue :", type(error).__name__, "–", error) # Une erreur est survenue : NameError – name 'x' is not defined
```

```py
try:
    res = 190 / 0
except Exception as error:
    # gérer l'exception
    print("Une exception est survenue :", type(error).__name__, "–", error) # Une exception est survenue : ZeroDivisionError – division by zero
    
```


## Conclusion
Comme le montre cet article, la syntaxe `try…except` est un excellent moyen de gérer les erreurs et d'empêcher votre programme de s'arrêter pendant son exécution.

Vous pouvez même afficher cette `Exception` dans le terminal en assignant l'erreur à une variable, et obtenir le type exact de l'`Exception` avec la fonction `type()`.

Bonne programmation !