---
title: Liste vers Chaîne Python – Exemple de Syntaxe join()
subtitle: ''
author: Quincy Larson
co_authors: []
series: null
date: '2022-04-07T23:24:00.000Z'
originalURL: https://freecodecamp.org/news/python-list-to-string-join-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/david-clode-5uU8HSpfwkI-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: Liste vers Chaîne Python – Exemple de Syntaxe join()
seo_desc: 'Sometimes you want to convert your Python lists into strings. This tutorial
  will show you an example of how you can do this.

  But first, let''s explore the difference between the Python list data structure
  and the Python string data structure.

  What is ...'
---

Parfois, vous souhaitez convertir vos listes Python en chaînes de caractères. Ce tutoriel vous montrera un exemple de la manière dont vous pouvez le faire.

Mais d'abord, explorons la différence entre la structure de données de liste Python et la structure de données de chaîne Python.

## Qu'est-ce qu'une Liste en Python ?

En Python, une liste est une séquence ordonnée d'éléments. Chaque élément d'une liste a un numéro d'index correspondant que vous pouvez utiliser pour y accéder.

Vous pouvez créer des listes en utilisant des crochets et elles peuvent contenir n'importe quel mélange de types de données.

```py
>>> exampleList = ['car', 'house', 'computer']
```

Notez que je vais montrer du code à partir du REPL Python. L'entrée que je tape a `>>>` au début. La sortie n'a rien au début. Vous pouvez lancer ce REPL en allant dans votre terminal et en tapant `python` puis en appuyant sur entrée.

Une fois que vous avez initialisé une liste Python, vous pouvez accéder à ses éléments en utilisant la notation entre crochets. Gardez à l'esprit que l'index commence à zéro plutôt qu'à 1. Voici un exemple d'entrées et de sorties :

```py
>>> exampleList[0]
'car'

>>> exampleList[1] 
'house'

>>> exampleList[2] 
'computer'
```

## Qu'est-ce qu'une Chaîne en Python ?

Une chaîne est simplement une séquence d'un ou plusieurs caractères. Par exemple, `'car'` est une chaîne.

Vous pouvez l'initialiser comme ceci :

```py
>>> exampleString = 'car'
```

Ensuite, vous pouvez appeler votre structure de données de chaîne pour voir son contenu :

```py
>>> exampleString
'car'

```

## Comment Convertir une Liste Python en une Chaîne Séparée par des Virgules ?

Vous pouvez utiliser la méthode de chaîne .join pour convertir une liste en une chaîne.

```py
>>> exampleCombinedString = ','.join(exampleList)
```

Vous pouvez ensuite accéder à la nouvelle structure de données de chaîne pour voir son contenu :

```py
>>> exampleCombinedString
'car,house,computer'
```

Donc, encore une fois, la syntaxe est `[séparateur].join([liste que vous voulez convertir en chaîne])`.

Dans ce cas, j'ai utilisé une virgule comme séparateur, mais vous pourriez utiliser n'importe quel caractère que vous voulez.

Allons-y. Rejoignons cela à nouveau, mais cette fois, ajoutons un espace après la virgule pour que la chaîne résultante soit un peu plus facile à lire :

```py
>>> exampleCombinedString = ', '.join(exampleList)
>>> exampleCombinedString
'car, house, computer'

```

Voilà.

## Comment Concaténer des Listes en Python ?

Il existe plusieurs façons de concaténer des listes en Python. La plus courante est d'utiliser l'opérateur `+` :

```py
>>> list1 = [1, 2, 3]
>>> list2 = [4, 5, 6]
>>> list1 + list2
[1, 2, 3, 4, 5, 6]
```

Une autre option est d'utiliser la méthode `extend()` :

```py
>>> list1 = [1, 2, 3]
>>> list2 = [4, 5, 6]
>>> list1.extend(list2)
>>> list1
[1, 2, 3, 4, 5, 6]
```

Enfin, vous pouvez utiliser le constructeur `list()` :

```py
>>> list1 = [1, 2, 3]
>>> list2 = [4, 5, 6]
>>> list3 = list1 + list2
>>> list3
[1, 2, 3, 4, 5, 6]
```

## Comment Convertir une Liste en un Tableau en Python ?

Une façon de le faire est d'utiliser la bibliothèque NumPy.

D'abord, importez NumPy :

```py
import numpy as np
```

Ensuite, exécutez la méthode np.array() pour convertir une liste en un tableau :

```py
>>> a = np.array([1, 2, 3])
>>> print(a)
[1 2 3]
```

## Peut-on Convertir une Liste en un Dictionnaire en Python ?

Absolument. D'abord, créons un dictionnaire en utilisant la fonction intégrée `dict()`. Exemple de syntaxe `dict()` :

```py
d = dict(name='John', age=27, country='USA') 
print(d)
```

Ce qui donnera :

```py
{'age': 27, 'country': 'USA', 'name': 'John'}
```

Dans cet exemple, nous créons un objet dictionnaire en utilisant la fonction `dict()`. La fonction `dict()` accepte un objet itérable. Dans ce cas, nous utilisons un tuple.

### Comment Créer un Dictionnaire à partir d'une Liste

Vous pouvez également créer un dictionnaire à partir d'une liste en utilisant la fonction `dict()`.

```py
d = dict(zip(['a', 'b', 'c'], [1, 2, 3]))
print(d)

```

Ce qui donnera :

```py
{'a': 1, 'b': 2, 'c': 3}

```

Notez que dans cet exemple, nous avons utilisé la fonction `zip()` pour créer un tuple.

### Comment Créer un Dictionnaire à partir d'un Autre Dictionnaire :

Vous pouvez créer un dictionnaire à partir d'un autre dictionnaire. Vous pouvez utiliser la fonction dict() ou la méthode de constructeur pour le faire.

```py
d = dict(a=1, b=2, c=3) print(d)

```

Ce qui donnera :

```py
{'a': 1, 'b': 2, 'c'}

```

## Il y a tant de choses géniales que vous pouvez faire avec les Listes, Tableaux, Dictionnaires et Chaînes Python

Je ne fais vraiment qu'effleurer la surface ici. Si vous voulez aller beaucoup plus loin et appliquer beaucoup de ces méthodes et techniques sur des projets concrets, freeCodeCamp.org peut vous aider. 

Si vous voulez en savoir plus sur la programmation et la technologie, essayez [le programme de codage principal de freeCodeCamp](https://www.freecodecamp.org/learn). C'est gratuit.