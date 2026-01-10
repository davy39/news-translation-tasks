---
title: Python Set VS List – Sets et Lists en Python
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-01-05T15:52:53.000Z'
originalURL: https://freecodecamp.org/news/python-set-vs-list
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/setvlist.png
tags:
- name: Python
  slug: python
seo_title: Python Set VS List – Sets et Lists en Python
seo_desc: "In Python, set and list are both data structures for storing and organizing\
  \ any values. Those values could be numbers, strings, and booleans. \nIn this article,\
  \ we'll look at the differences between set and list. But before that, let's take\
  \ a look at ..."
---

En Python, `set` et `list` sont tous deux des structures de données pour stocker et organiser des valeurs. Ces valeurs peuvent être des nombres, des chaînes de caractères et des booléens. 

Dans cet article, nous examinerons les différences entre `set` et `list`. Mais avant cela, voyons ce que sont `set` et `list`.

## Ce que nous allons couvrir
- [Qu'est-ce qu'un `set` Python ?](#heading-quest-ce-quun-set-python)
- [Comment créer un Set en Python](#heading-comment-creer-un-set-en-python)
- [Qu'est-ce qu'une `list` Python ?](#heading-quest-ce-quune-list-python)
- [Comment créer une List en Python](#heading-comment-creer-une-list-en-python)
- [Quelle est la différence entre un Set et une List ?](#heading-quelle-est-la-difference-entre-un-set-et-une-list)
- [Conclusion](#heading-conclusion)

## Qu'est-ce qu'un `set` Python ?
Un `set` est une collection de valeurs non ordonnées et uniques. Les valeurs dans un `set` sont uniques car il ne peut pas y avoir de doublons. 

Les éléments d'un set sont également immuables – vous ne pouvez pas les changer. Mais vous pouvez toujours ajouter et supprimer de la collection.

En bref, un `set` stocke plusieurs valeurs entre accolades ou à l'intérieur du constructeur `set()`.


### Comment créer un Set en Python
Pour créer un set en Python, vous pouvez utiliser le constructeur `set()` ou des accolades.

Set avec le constructeur `set()` :

```py
country_set = set(("USA", "Ukraine", "Nigeria", "Ghana"))
print(country_set) #{'Ghana', 'USA', 'Ukraine', 'Nigeria'}
```

Remarquez que j'ai utilisé deux parenthèses pour créer la liste. C'est parce que le constructeur `set()` attend un argument. Mettre toutes les valeurs dans un autre ensemble de parenthèses fait de toutes les valeurs un seul argument.

Le set peut également contenir plusieurs types de données – chaînes de caractères, nombres ou booléens :

```py
multi_set = set(("freeCodeCamp", True, 12))
print(multi_set) #{True, 12, 'freeCodeCamp'}
```

Vous pouvez également créer un set avec des accolades comme ceci :

```py
fruit_set = {"Apple", "Avocado", "Mango", "Cashew"}
print(fruit_set) #{'Mango', 'Apple', 'Avocado', 'Cashew'}
```

Et vous pouvez inclure plusieurs types de données dans un set créé avec des accolades :

```py
random_set = {True, "Laptop", "Phone", 5}
print(random_set) #{True, 'Laptop', 5, 'Phone'}
```


## Qu'est-ce qu'une `list` Python ?
Une list est une variable pour stocker plusieurs valeurs en Python. C'est l'une des structures de données intégrées en Python avec les sets, les tuples et les dictionnaires. Si vous êtes familier avec JavaScript, une list Python est comme un tableau JavaScript.

### Comment créer une List en Python
Vous pouvez créer une list Python avec le constructeur `list()` ou des crochets :

```py
# List avec le constructeur list()
rand_list = list(("Rice", "Salad", "Eba", 4, True))
print(rand_list) # ['Rice', 'Salad', 'Eba', 4, True]

# List avec des crochets
another_rand_list = ["Pele", 1, True]
print(another_rand_list) # ['Pele', 1, True]
```

## Quelle est la différence entre un Set et une List ?

| **Base** | **Set** | **List** |
| ----------- | ----------- | ----------|
|**Création**| Vous créez un `set` avec le constructeur `set()` ou des accolades. | Vous créez une `list` avec le constructeur `list()` ou des crochets. |
| **Doublons**| Un set ne peut pas avoir de valeurs en double. Toutes les valeurs doivent être uniques.| Une list peut avoir des valeurs en double. |
| **Ordre**| Un set est non ordonné. Lorsque vous imprimez les éléments d'une list, ils n'apparaissent pas dans l'ordre où vous les avez arrangés. | Une list est ordonnée. Lorsque vous l'imprimez, les éléments de la list sont retournés dans le même ordre que celui dans lequel ils ont été mis. |
| **Mutation**| Vous ne pouvez pas changer les éléments d'un set, mais vous pouvez ajouter au set et en supprimer. | Vous pouvez changer les éléments d'une list et vous pouvez ajouter à la list.|


## Conclusion
Les sets et les lists sont des structures de données intégrées que vous pouvez utiliser pour stocker et organiser des valeurs en Python. 

Si vous vous demandez lequel utiliser, cela dépend du cas d'utilisation. Si vous ne voulez pas que les valeurs dans les données changent, vous pouvez utiliser un set. Mais si vous voulez que les éléments changent, vous pouvez utiliser une list. Vous pouvez également prendre en compte si l'ordre des éléments est important pour vous ou non.

C'est pourquoi cet article vous a expliqué ce que sont `set` et `list`, comment les créer, et surtout les différences entre les deux.

Merci d'avoir lu.