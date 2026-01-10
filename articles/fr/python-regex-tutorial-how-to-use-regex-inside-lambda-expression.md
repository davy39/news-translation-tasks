---
title: Tutoriel Python RegEx – Comment utiliser RegEx dans une expression Lambda
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-03-17T09:31:41.000Z'
originalURL: https://freecodecamp.org/news/python-regex-tutorial-how-to-use-regex-inside-lambda-expression
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/regexinlambda.png
tags:
- name: Lambda Expressions
  slug: lambda-expressions
- name: Python
  slug: python
- name: Python 3
  slug: python3
- name: Regex
  slug: regex
seo_title: Tutoriel Python RegEx – Comment utiliser RegEx dans une expression Lambda
seo_desc: 'It’s possible to use RegEx inside a lambda function in Python. You can
  apply this to any Python method or function that takes a function as a parameter.
  Such functions and methods include filter(), map(), any(), sort(), and more.

  Keep reading as I sh...'
---

Il est possible d'utiliser les RegEx à l'intérieur d'une fonction lambda en Python. Vous pouvez appliquer cela à n'importe quelle méthode ou fonction Python qui accepte une fonction comme paramètre. Ces fonctions et méthodes incluent `filter()`, `map()`, `any()`, `sort()`, et bien d'autres.

Continuez votre lecture pour découvrir comment utiliser les expressions régulières à l'intérieur d'une fonction lambda.


## Ce que nous allons aborder
- [Comment utiliser RegEx dans l'expression d'une fonction Lambda](#heading-comment-utiliser-regex-dans-lexpression-dune-fonction-lambda)
  - [Comment utiliser RegEx dans l'expression d'une fonction Lambda avec la fonction `filter()`](#heading-comment-utiliser-regex-dans-lexpression-dune-fonction-lambda-avec-la-fonction-filter)
  - [Comment utiliser RegEx dans l'expression d'une fonction Lambda avec la fonction `map()`](#heading-comment-utiliser-regex-dans-lexpression-dune-fonction-lambda-avec-la-fonction-map)
  - [Comment utiliser RegEx dans l'expression d'une fonction Lambda avec la méthode `sort()`](#heading-comment-utiliser-regex-dans-lexpression-dune-fonction-lambda-avec-la-methode-sort)
- [Conclusion](#heading-conclusion)


## Comment utiliser RegEx dans l'expression d'une fonction Lambda
La syntaxe avec laquelle une fonction lambda peut prendre une RegEx comme expression ressemble à ceci :

```py
lambda x: re.method(pattern, x)
```

Sachez que vous devez utiliser la fonction lambda sur quelque chose. Et c'est là que des fonctions comme `map()`, `sort()`, `filter()` et d'autres interviennent.


### Comment utiliser RegEx dans l'expression d'une fonction Lambda avec la fonction `filter()`
Le premier exemple que je vais vous montrer utilise la fonction `filter()` :
```py
import re

fruits = ['apple', 'mango', 'banana', 'cherry', 'apricot', 'raspberry', 'avocado']
filtered_fruits = filter(lambda fruit: re.match('^a', fruit), fruits)

# convertir les nouveaux fruits en une autre liste et l'afficher
print(list(filtered_fruits)) # ['apple', 'apricot', 'avocado']
```

Dans le code ci-dessus :
- `filter()` prend la fonction lambda comme fonction à exécuter et la liste `fruits` comme itérable
- pour l'expression de la fonction lambda, elle utilise la méthode `re.match()` de Python RegEx et utilise le motif `^a` sur l'argument `fruit`
- la dernière chose que j'ai faite a été de convertir tous les éléments de la liste qui correspondent au motif en une liste


### Comment utiliser RegEx dans l'expression d'une fonction Lambda avec la fonction `map()`
Pour utiliser RegEx dans une fonction lambda avec une autre fonction comme `map()`, la syntaxe est similaire :
```py
import re

fruits2 = ['opple', 'bonono', 'cherry', 'dote', 'berry']
modified_fruits = map(lambda fruit: re.sub('o', 'a', fruit), fruits2)

# convertir les nouveaux fruits en une autre liste et l'afficher
print(list(modified_fruits)) # ['apple', 'banana', 'cherry', 'date', 'berry']
```

Dans le code ci-dessus :
- `modified_fruits` parcourt la liste `fruits2` avec une fonction `map()`
- utilise la méthode `re.sub()` de Python RegEx comme expression de la fonction lambda.

La méthode `re.sub` vous permet de remplacer la première valeur par la seconde. Dans l'exemple, elle a remplacé toutes les occurrences de `o` par `a`.


### Comment utiliser RegEx dans l'expression d'une fonction Lambda avec la méthode `sort()`
Le dernier exemple que je vais vous montrer utilise la méthode `sort()` des listes :
```py
import re

fruits = [ 'banana', 'fig', 'grapefruit']

# trier les fruits en fonction du nombre de voyelles
fruits.sort(key=lambda x: len(re.findall('[aeiou]', x)))

print(fruits) #['fig', 'banana', 'grapefruit']
```

Dans le code, la fonction lambda trie la liste en fonction du nombre de voyelles. Elle le fait en combinant la méthode `len()`, la méthode `findall()` de Python RegEx et le motif `[aeiou]`.

Le mot fruit ayant le plus petit nombre de voyelles arrive en premier. Si vous utilisez `reverse=True`, il classe les fruits en fonction de ceux qui ont le plus grand nombre de voyelles – par ordre décroissant :
```py
import re

fruits = [ 'banana', 'fig', 'grapefruit']

# trier les fruits en fonction du nombre de voyelles
fruits.sort(key=lambda x: len(re.findall('[aeiou]', x)), reverse=True)

print(fruits) # ['grapefruit', 'banana', 'fig']
```


## Conclusion
Dans cet article, nous avons vu comment vous pouvez passer des RegEx à une fonction lambda en vous montrant des exemples utilisant les fonctions `filter()`, `map()` et la méthode `sort()`.

J'espère que cet article vous apportera les connaissances nécessaires pour utiliser les RegEx à l'intérieur d'une fonction lambda.

Bon code !