---
title: 'Les instructions Return de Python expliquées : ce qu''elles sont et pourquoi
  vous les utilisez'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-04T21:22:00.000Z'
originalURL: https://freecodecamp.org/news/python-return-statements-explained-what-they-are-and-why-you-use-them
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e34740569d1a4ca3be2.jpg
tags:
- name: Python
  slug: python
seo_title: 'Les instructions Return de Python expliquées : ce qu''elles sont et pourquoi
  vous les utilisez'
seo_desc: 'All functions return a value when called.

  If a return statement is followed by an expression list, that expression list is
  evaluated and the value is returned:

  >>> def greater_than_1(n):

  ...     return n > 1

  ...

  >>> print(greater_than_1(1))

  False

  >>>...'
---

Toutes les fonctions retournent une valeur lorsqu'elles sont appelées.

Si une instruction return est suivie d'une liste d'expressions, cette liste d'expressions est évaluée et la valeur est retournée :

```text
>>> def greater_than_1(n):
...     return n > 1
...
>>> print(greater_than_1(1))
False
>>> print(greater_than_1(2))
True
```

Si aucune liste d'expressions n'est spécifiée, `None` est retourné :

```text
>>> def no_expression_list():
...     return    # Aucune liste d'expressions de retour.
...
>>> print(no_expression_list())
None
```

Si une instruction return est atteinte pendant l'exécution d'une fonction, l'appel de fonction actuel est quitté à ce point :

```text
>>> def return_middle():
...     a = 1
...     return a
...     a = 2     # Cette affectation n'est jamais atteinte.
...
>>> print(return_middle())
1
```

S'il n'y a pas d'instruction return, la fonction retourne None lorsqu'elle atteint la fin :

```text
>>> def no_return():
...     pass     # Aucune instruction return.
...
>>> print(no_return())
None
```

Une seule fonction peut avoir plusieurs instructions `return`. L'exécution de la fonction se termine lorsqu'une de ces instructions `return` est atteinte :

```text
>>> def multiple_returns(n):
...    if(n):
...        return "First Return Statement"
...    else:
...        return "Second Return Statement"
...
>>> print(multiple_returns(True))
First Return Statement
>>> print(multiple_returns(False))
Second Return Statement
```

Une seule fonction peut retourner divers types :

```text
>>> def various_return_types(n):
...     if(n==1):
...         return "Hello World."   # Retourne une chaîne de caractères
...     elif(n==2):
...         return 42               # Retourne une valeur
...     else:
...         return True             # Retourne un booléen
...
>>> print(various_return_types(1))
Hello World.
>>> print(various_return_types(2))
42
>>> print(various_return_types(3))
True
```

Il est même possible qu'une seule fonction retourne plusieurs valeurs avec un seul return :

```text
>>> def return_two_values():
...     a = 40
...     b = 2
...     return a,b
...
>>> print("First value = %d,  Second value = %d" %(return_two_values()))
First value = 40,  Second value = 2
```

Consultez la [documentation Python](https://docs.python.org/3/reference/simple_stmts.html#the-return-statement) pour plus d'informations.