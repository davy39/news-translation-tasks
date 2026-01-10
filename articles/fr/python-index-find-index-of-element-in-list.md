---
title: Index Python – Comment trouver l'index d'un élément dans une liste
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-05-02T20:59:13.000Z'
originalURL: https://freecodecamp.org/news/python-index-find-index-of-element-in-list
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/pexels-olya-kobruseva-5408919.jpg
tags:
- name: Python
  slug: python
seo_title: Index Python – Comment trouver l'index d'un élément dans une liste
seo_desc: "By Suchandra Datta\nWhen you're learning to code, you eventually learn\
  \ about lists and the different operations you can perform on them. \nIn this article,\
  \ we'll go through how you can find the index of a particular element which is stored\
  \ in a list in..."
---

Par Suchandra Datta

Lorsque vous apprenez à coder, vous finissez par apprendre les listes et les différentes opérations que vous pouvez effectuer sur elles. 

Dans cet article, nous allons voir comment trouver l'index d'un élément particulier qui est stocké dans une liste en Python.

## Qu'est-ce qu'une liste en Python ?

Une liste en Python est un type de données intégré qui nous permet de stocker un ensemble de différentes valeurs, comme des nombres, des chaînes de caractères, des objets datetime et ainsi de suite. 

Les listes sont ordonnées, ce qui signifie que la séquence dans laquelle nous stockons les valeurs est importante. 

Les indices de liste commencent à zéro et se terminent à la longueur de la liste moins un. Pour plus d'informations détaillées sur le type de données liste, consultez [ce guide complet](https://www.freecodecamp.org/news/lists-in-python-comprehensive-guide/).

Voyons un exemple de listes :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-173.png)

```python
fruits = ["apple", "orange", "grapes", "guava"]
type(fruits)
print(fruits[0])
print(fruits[1])
print(fruits[2])

```

Ici, nous avons créé une liste de 4 éléments, où nous voyons que le premier élément de la liste est à l'index zéro, le deuxième élément est à l'index 1, le troisième élément est à l'index 2, et ainsi de suite. 

Pour la liste de fruits, les indices de liste valides sont 0, 1, 2 et 3.

## Comment trouver l'index des éléments dans une liste en Python

Faisons l'inverse. C'est-à-dire, étant donné un élément de liste, trouvons l'index ou la position de cet élément dans la liste. 

```
index = fruits.index('orange')
#La valeur de l'index est 1

index = fruits.index('guava')
#La valeur de l'index est 3

index = fruits.index('banana')
#Cela lève une ValueError car banana n'est pas présent dans la liste

```

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-174.png)

Les listes Python nous fournissent la méthode index qui nous permet d'obtenir l'index de la première occurrence d'un élément de liste, comme montré ci-dessus. 

Nous pouvons également voir que la méthode index lèvera une ValueError si nous essayons de trouver l'index d'un élément qui n'existe pas dans la liste. 

Pour plus de détails sur la méthode index, consultez la documentation officielle [ici](https://docs.python.org/3/tutorial/datastructures.html).

La syntaxe de base de la méthode index est la suivante :

```python
list_var.index(item)
```

Nous pouvons également spécifier une sous-liste dans laquelle rechercher, et la syntaxe pour cela est :

```python
list_var.index(item, start_index_of_sublist, end_index_of_sublist)
```

Pour illustrer cela davantage, regardons un exemple. 

Supposons que nous avons une liste **book_shelf_genres** où l'index signifie le numéro d'étagère. Nous avons de nombreuses étagères contenant des livres de mathématiques. Les numéros d'étagères commencent également à zéro. Nous voulons savoir quelle étagère après l'étagère 4 contient des livres de mathématiques.

```python
book_shelf_genres = ["Fiction", "Math", "Non-fiction", "History", "Math", "Coding", "Cooking", "Math"]
index = book_shelf_genres.index("Math")
#La valeur de l'index est 1
```

Nous pouvons voir le problème ici : utiliser simplement `index()` donnera la première occurrence de l'élément dans la liste – mais nous voulons connaître l'index de "Math" après l'étagère 4. 

Pour ce faire, nous utilisons la méthode index et spécifions la sous-liste à rechercher. La sous-liste commence à l'index 5 jusqu'à la fin de la liste **book_shelf_genres**, comme montré dans l'extrait de code ci-dessous

```python
index = book_shelf_genres.index("Math", 5)
#La valeur de l'index est 7
```

Notez que donner l'index de fin de la sous-liste est facultatif. Pour trouver l'index de "Math" après l'étagère numéro 1 et avant l'étagère numéro 5, nous ferons simplement ceci :

```python
index = book_shelf_genres.index("Math", 2, 5)
#La valeur de l'index est 4
```

## Comment trouver l'index d'un élément de liste avec plusieurs occurrences en Python

Que faire si nous devons connaître l'index d'un élément de liste qui apparaît plusieurs fois dans une liste ? La méthode index ne nous donnera pas chaque occurrence. 

Dans ce cas, nous pouvons trouver les multiples occurrences en utilisant la compréhension de liste comme suit :

```python
book_shelf_genres = ["Fiction", "Math", "Non-fiction", "History", "Math", "Coding", \
                     "Cooking", "Math"]

[i for i in range(0, len(book_shelf_genres)) if book_shelf_genres[i]=="Math"]
```

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-229.png)

Comme montré dans cet extrait de code, nous parcourons les indices de la liste. À chaque index, nous vérifions si l'élément à cet index est Math ou non. Si c'est Math, alors nous stockons cette valeur d'index dans une liste. 

Nous effectuons ce processus entier en utilisant la compréhension de liste, qui est simplement du sucre syntaxique qui nous permet d'itérer sur une liste et d'effectuer une opération. Dans notre cas, nous prenons des décisions basées sur la valeur de l'élément de liste. Ensuite, nous créons une nouvelle liste.

Avec ce processus, nous connaissons maintenant tous les numéros d'étagères qui contiennent des livres de mathématiques.

## Comment trouver l'index des éléments de liste dans une liste de listes en Python

```python
programming_languages = [["C","C++","Java"],["Python","Rust","R"],\
                         ["JavaScript","Prolog","Python"]]

[ (i, x.index("Python")) for i, x in enumerate(programming_languages) if "Python" in x ]
```

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-230.png)

Ici, nous utilisons la compréhension de liste et la méthode index pour trouver l'index de "Python" dans chacune des sous-listes. 

Nous passons la liste programming_languages à la méthode enumerate qui parcourt chaque élément de la liste et retourne un tuple contenant l'index et l'élément de la liste à cet index. 

Chaque élément de la liste programming_languages est également une liste. L'opérateur in vérifie ensuite si "Python" est présent dans cette liste ou non. Si présent, nous stockons l'index de la sous-liste et l'index de "Python" à l'intérieur de la sous-liste sous forme de tuple. 

La sortie est une liste de tuples. Le premier élément du tuple spécifie l'index de la sous-liste, et le deuxième nombre spécifie l'index à l'intérieur de la sous-liste. 

Ainsi, (1,0) signifie que la sous-liste à l'index 1 de la liste programming_languages contient l'élément "Python" à l'index 0.

## Comment trouver l'index d'un élément de liste qui peut ne pas exister dans une liste en Python

Dans de nombreux cas, nous finirons par essayer d'obtenir l'index d'un élément, mais nous ne sommes pas sûrs que l'élément existe dans la liste ou non. 

Si nous avons un morceau de code qui essaie d'obtenir l'index d'un élément qui n'est pas présent dans la liste, la méthode index() lèvera une ValueError. En l'absence de gestion des exceptions, cette ValueError provoquera une terminaison anormale du programme. 

Voici deux façons d'éviter ou de gérer cette situation :

```python
books = ["Cracking the Coding Interview", "Clean Code", "The Pragmatic Programmer"]
ind = books.index("The Pragmatic Programmer") if "The Pragmatic Programmer" in books else -1
                                            
```

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-180.png)

Une façon est de vérifier à l'aide de l'opérateur "in" si l'élément existe dans la liste ou non. L'opérateur in a la syntaxe de base suivante

```python
var in iterable
```

où iterable pourrait être une liste, un tuple, un ensemble, une chaîne ou un dictionnaire. Si var existe en tant qu'élément dans l'iterable, l'opérateur in retourne True. Sinon, il retourne False. 

Cela est idéal pour notre cas. Nous vérifierons simplement si un élément existe dans la liste ou non et seulement lorsqu'il existe, nous appellerons la méthode index(). Cela garantit que la méthode index() ne lève pas de ValueError.

Si nous ne voulons pas passer du temps à vérifier si un élément existe dans la liste ou non, surtout pour les grandes listes, nous pouvons gérer la ValueError comme ceci :

```python
books = ["Cracking the Coding Interview", "Clean Code", "The Pragmatic Programmer"]
try:
    ind = books.index("Design Patterns")
except ValueError:
    ind = -1
ind
```

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-181.png)

## Conclusion

Aujourd'hui, nous avons appris comment trouver l'index d'un élément dans une liste en utilisant la méthode `index()`. 

Nous avons également vu comment utiliser la méthode index sur des sous-listes, comment trouver l'index des éléments dans une liste de listes, comment trouver chaque occurrence d'un élément dans une liste, et comment vérifier la présence d'éléments dans des listes qui peuvent ne pas être présents. 

J'espère que vous avez trouvé cet article utile et agréable à lire. Bon codage !