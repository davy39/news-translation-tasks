---
title: L'objet 'int' n'est pas itérable – Erreur Python [Résolu]
date: '2022-03-24T16:46:42.000Z'
author: Kolade Chris
authorURL: https://www.freecodecamp.org/news/author/koladechris/
originalURL: https://freecodecamp.org/news/int-object-is-not-iterable-python-error-solved
translator: ''
reviewer: ''
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/iterable.png
tags:
- name: Python
  slug: python
seo_desc: 'If you are running your Python code and you see the error “TypeError: ''int''
  object is not iterable”, it means you are trying to loop through an integer or other
  data type that loops cannot work on.

  In Python, iterable data are lists, tuples, sets, di...'
---


Si vous exécutez votre code Python et que vous voyez l'erreur « TypeError: 'int' object is not iterable », cela signifie que vous essayez d'itérer sur un entier ou un autre type de données sur lequel les boucles ne peuvent pas fonctionner.

<!-- more -->

En Python, les données itérables sont les listes, les tuples, les ensembles (sets), les dictionnaires, et ainsi de suite.

De plus, le fait que cette erreur soit une « TypeError » signifie que vous essayez d'effectuer une opération sur un type de données inapproprié. Par exemple, additionner une chaîne de caractères avec un entier.

C'est aujourd'hui la dernière fois que vous devriez rencontrer cette erreur en exécutant votre code Python. Car dans cet article, je vais non seulement vous montrer comment la corriger, mais je vous montrerai également comment vérifier les méthodes magiques `__iter__` afin que vous puissiez voir si un objet est itérable.

## Comment corriger l'erreur 'int' object is not iterable

Si vous essayez d'itérer sur un entier, vous obtiendrez cette erreur :

```
count = 14

for i in count:
    print(i)
# Output: TypeError: 'int' object is not iterable
```

Une façon de corriger cela est de passer la variable dans la fonction `range()`.

En Python, la fonction `range` vérifie la variable qui lui est transmise et renvoie une série de nombres commençant à 0 et s'arrêtant juste avant le nombre spécifié.

La boucle va maintenant s'exécuter :

```
count = 14

for i in range(count):
    print(i)

# Output: 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
```

Un autre exemple utilisant cette solution se trouve dans l'extrait de code ci-dessous :

```
age = int(input("Enter your age: "))

for num in range(age):
    print(num)

# Output: 
# Enter your age: 6
# 0
# 1
# 2
# 3
# 4
# 5
```

## Comment vérifier si une donnée ou un objet est itérable

Pour vérifier si certaines données particulières sont itérables, vous pouvez utiliser la méthode `dir()`. Si vous voyez la méthode magique `__iter__`, alors les données sont itérables. Sinon, les données ne sont pas itérables et vous ne devriez pas essayer de les parcourir avec une boucle.

```
perfectNum = 7

print(dir(perfectNum))

# Output:['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', 
# '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
```

La méthode magique `__iter__` ne se trouve pas dans la sortie, donc la variable `perfectNum` n'est pas itérable.

```
jerseyNums = [43, 10, 7, 6, 8]

print(dir(jerseyNums))

# Output: ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
```

La méthode magique `__iter__` a été trouvée, donc la liste `jerseyNums` est itérable.

## Conclusion

Dans cet article, vous avez découvert l'erreur « Int Object is Not Iterable » et comment la corriger.

Vous avez également pu voir qu'il est possible de vérifier si un objet ou certaines données sont itérables ou non.

Si vous cherchez la méthode magique `__iter__` dans des données et que vous ne la trouvez pas, il vaut mieux ne pas tenter d'itérer sur ces données puisqu'elles ne sont pas itérables.

Merci de votre lecture.

---

![Kolade Chris](https://cdn.hashnode.com/res/hashnode/image/upload/v1720467520534/YTa5HE3R0.jpg)

Je suis un développeur logiciel et rédacteur technique spécialisé dans les technologies frontend.

---

Si vous avez lu jusqu'ici, remerciez l'auteur pour lui montrer que vous appréciez son travail. Dites Merci

Apprenez à coder gratuitement. Le curriculum open source de freeCodeCamp a aidé plus de 40 000 personnes à obtenir des emplois de développeurs. [Commencer][1]

[1]: https://www.freecodecamp.org/learn/