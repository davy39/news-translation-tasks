---
title: Python .sort() – Comment trier une liste en Python
date: '2022-03-08T17:38:27.000Z'
author: Dionysia Lemonaki
authorURL: https://www.freecodecamp.org/news/author/dionysialemonaki/
originalURL: https://freecodecamp.org/news/python-sort-how-to-sort-a-list-in-python
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/pexels-ken-tomita-389818.jpg
tags:
- name: Python
  slug: python
seo_desc: 'In this article, you will learn how to use Python''s sort() list method.

  You will also learn a different way of performing sorting in Python by using the
  sorted() function so you can see how it differs from sort().

  By the end, you will know the basics...'
---


Dans cet article, vous apprendrez à utiliser la méthode de liste `sort()` de Python.

<!-- more -->

Vous découvrirez également une autre manière d'effectuer un tri en Python en utilisant la fonction `sorted()`, afin de voir en quoi elle diffère de `sort()`.

À la fin de cette lecture, vous maîtriserez les bases du tri d'une liste en Python et saurez comment personnaliser le tri pour répondre à vos besoins.

Voici ce que nous allons aborder :

1.  [Syntaxe de la méthode `sort`][1]
2.  [Trier les éléments d'une liste par ordre croissant][2]
3.  [Trier les éléments d'une liste par ordre décroissant][3]
4.  [Trier les éléments d'une liste en utilisant l'argument `key`][4]
5.  [Les différences entre `sort()` et `sorted()`][5]
    1.  [Quand utiliser `sort()` et `sorted()`][6]

## La méthode `sort()` - Aperçu de la syntaxe

La méthode `sort()` est l'un des moyens de trier une liste en Python.

Lorsque vous utilisez `sort()`, vous triez une liste *in-place*. Cela signifie que la liste originale est directement modifiée. Plus précisément, l'ordre original des éléments est altéré.

La syntaxe générale de la méthode `sort()` ressemble à ceci :

```
list_name.sort(reverse=..., key=... )
```

Analysons ses composants :

-   `list_name` est le nom de la liste sur laquelle vous travaillez.
-   `sort()` est l'une des méthodes de liste de Python pour trier et modifier une liste. Elle trie les éléments de la liste par ordre *croissant* ou *décroissant*.
-   `sort()` accepte deux paramètres **optionnels**.
-   `reverse` est le premier paramètre optionnel. Il spécifie si la liste doit être triée par ordre croissant ou décroissant. Il prend une valeur booléenne, soit `True` soit `False`. La valeur par défaut est **False**, ce qui signifie que la liste est triée par ordre croissant. Le régler sur `True` trie la liste à l'envers, par ordre décroissant.
-   `key` est le second paramètre optionnel. Il prend une fonction ou une méthode utilisée pour spécifier des critères de tri détaillés.

La méthode `sort()` renvoie `None`, ce qui signifie qu'il n'y a pas de valeur de retour puisqu'elle modifie simplement la liste originale. Elle ne renvoie **pas** de nouvelle liste.

## Comment trier les éléments d'une liste par ordre croissant avec la méthode `sort()`

Comme mentionné précédemment, par défaut, `sort()` trie les éléments d'une liste par ordre croissant.

L'ordre croissant signifie que les éléments sont disposés de la valeur la plus basse à la plus élevée.

La valeur la plus basse se trouve à gauche et la plus élevée à droite.

La syntaxe générale pour effectuer cela ressemble à ceci :

```
list_name.sort()
```

Jetons un coup d'œil à l'exemple suivant qui montre comment trier une liste de nombres entiers :

```
# a list of numbers
my_numbers = [10, 8, 3, 22, 33, 7, 11, 100, 54]

#sort list in-place in ascending order
my_numbers.sort()

#print modified list
print(my_numbers)

#output

#[3, 7, 8, 10, 11, 22, 33, 54, 100]
```

Dans l'exemple ci-dessus, les nombres sont triés du plus petit au plus grand.

Vous pouvez obtenir le même résultat en travaillant avec une liste de chaînes de caractères (`strings`) :

```
# a list of strings
programming_languages = ["Python", "Swift","Java", "C++", "Go", "Rust"]

#sort list in-place in alphabetical order
programming_languages.sort()

#print modified list
print(programming_languages)

#output

#['C++', 'Go', 'Java', 'Python', 'Rust', 'Swift']
```

Dans ce cas, chaque chaîne contenue dans la liste a été triée par ordre alphabétique.

Comme vous l'avez vu dans les deux exemples, les listes originales ont été directement modifiées.

## Comment trier les éléments d'une liste par ordre décroissant avec la méthode `sort()`

L'ordre décroissant est l'opposé de l'ordre croissant : les éléments sont disposés de la valeur la plus élevée à la plus basse.

Pour trier les éléments d'une liste par ordre décroissant, vous devez utiliser le paramètre optionnel `reverse` avec la méthode `sort()` et lui assigner la valeur `True`.

La syntaxe générale pour cela ressemble à ceci :

```
list_name.sort(reverse=True)
```

Réutilisons le même exemple que dans la section précédente, mais cette fois-ci en triant les nombres dans l'ordre inverse :

```
# a list of numbers
my_numbers = [10, 8, 3, 22, 33, 7, 11, 100, 54]

#sort list in-place in descending order
my_numbers.sort(reverse=True)

#print modified list
print(my_numbers)

#output

#[100, 54, 33, 22, 11, 10, 8, 7, 3]
```

Désormais, tous les nombres sont disposés à l'envers, la plus grande valeur étant à gauche et la plus petite à droite.

Vous pouvez également obtenir le même résultat avec une liste de chaînes de caractères.

```
# a list of strings
programming_languages = ["Python", "Swift","Java", "C++", "Go", "Rust"]

#sort list in-place in  reverse alphabetical order
programming_languages.sort(reverse=True)

#print modified list
print(programming_languages)

#output

#['Swift', 'Rust', 'Python', 'Java', 'Go', 'C++']
```

Les éléments de la liste sont maintenant disposés par ordre alphabétique inverse.

## Comment trier les éléments d'une liste avec le paramètre `key` et la méthode `sort()`

Vous pouvez utiliser le paramètre `key` pour effectuer des opérations de tri plus personnalisées.

La valeur assignée au paramètre `key` doit être un `callable`.

Un `callable` est un objet qui peut être appelé, ce qui signifie qu'il peut être invoqué et référencé.

Les méthodes et les fonctions sont des exemples d'objets `callable`.

Cette méthode ou fonction assignée à `key` sera appliquée à tous les éléments de la liste avant que le tri ne se produise et spécifiera la logique des critères de tri.

Supposons que vous vouliez trier une liste de chaînes de caractères en fonction de leur longueur.

Pour cela, vous assignez la fonction intégrée `len()` au paramètre `key`.

La fonction `len()` comptera la longueur de chaque élément stocké dans la liste en comptant les caractères qu'il contient.

```
programming_languages = ["Python", "Swift","Java", "C++", "Go", "Rust"]

programming_languages.sort(key=len)

print(programming_languages)

#output

#['Go', 'C++', 'Java', 'Rust', 'Swift', 'Python']
```

Dans l'exemple ci-dessus, les chaînes sont triées par défaut par ordre croissant, mais cette fois le tri s'effectue sur la base de leur longueur.

La chaîne la plus courte est à gauche et la plus longue à droite.

Les paramètres `key` et `reverse` peuvent également être combinés.

Par exemple, vous pourriez trier les éléments de la liste en fonction de leur longueur, mais par ordre décroissant.

```
programming_languages = ["Python", "Swift","Java", "C++", "Go", "Rust"]

programming_languages.sort(key=len, reverse=True)

print(programming_languages)

#output

#['Python', 'Swift', 'Java', 'Rust', 'C++', 'Go']
```

Dans l'exemple ci-dessus, les chaînes vont de la plus longue à la plus courte.

Notez également que vous pouvez créer votre propre fonction de tri personnalisée pour définir des critères plus explicites.

Par exemple, vous pouvez créer une fonction spécifique puis trier la liste selon la valeur de retour de cette fonction.

Supposons que vous ayez une liste de dictionnaires contenant des langages de programmation et leur année de création.

```
programming_languages = [{'language':'Python','year':1991},
{'language':'Swift','year':2014},
{'language':'Java', 'year':1995},
{'language':'C++','year':1985},
{'language':'Go','year':2007},
{'language':'Rust','year':2010},
]
```

Vous pouvez définir une fonction personnalisée qui récupère la valeur d'une clé spécifique du dictionnaire.

💡 Gardez à l'esprit qu'une clé de dictionnaire et le paramètre `key` accepté par `sort()` sont deux choses différentes !

Plus précisément, la fonction récupérera et renverra la valeur de la clé `year` dans la liste de dictionnaires, laquelle spécifie l'année de création de chaque langage.

La valeur de retour servira ensuite de critère de tri pour la liste.

```
programming_languages = [{'language':'Python','year':1991},
{'language':'Swift','year':2014},
{'language':'Java', 'year':1995},
{'language':'C++','year':1985},
{'language':'Go','year':2007},
{'language':'Rust','year':2010},
]

def get_year(element):
    return element['year']
```

Vous pouvez ensuite trier selon la valeur de retour de la fonction créée précédemment en l'assignant au paramètre `key`, et trier par ordre chronologique croissant par défaut :

```
programming_languages = [{'language':'Python','year':1991},
{'language':'Swift','year':2014},
{'language':'Java', 'year':1995},
{'language':'C++','year':1985},
{'language':'Go','year':2007},
{'language':'Rust','year':2010},
]

def get_year(element):
    return element['year']

programming_languages.sort(key=get_year)

print(programming_languages)
```

Sortie :

```
[{'language': 'C++', 'year': 1985}, {'language': 'Python', 'year': 1991}, {'language': 'Java', 'year': 1995}, {'language': 'Go', 'year': 2007}, {'language': 'Rust', 'year': 2010}, {'language': 'Swift', 'year': 2014}]
```

Si vous souhaitez trier du langage le plus récent au plus ancien, soit par ordre décroissant, vous utilisez alors le paramètre `reverse=True` :

```
programming_languages = [{'language':'Python','year':1991},
{'language':'Swift','year':2014},
{'language':'Java', 'year':1995},
{'language':'C++','year':1985},
{'language':'Go','year':2007},
{'language':'Rust','year':2010},
]

def get_year(element):
    return element['year']

programming_languages.sort(key=get_year, reverse=True)

print(programming_languages)
```

Sortie :

```
[{'language': 'Swift', 'year': 2014}, {'language': 'Rust', 'year': 2010}, {'language': 'Go', 'year': 2007}, {'language': 'Java', 'year': 1995}, {'language': 'Python', 'year': 1991}, {'language': 'C++', 'year': 1985}]
```

Pour obtenir exactement le même résultat, vous pouvez créer une fonction lambda.

Au lieu d'utiliser la fonction personnalisée classique définie avec le mot-clé `def`, vous pouvez :

-   créer une expression concise sur une seule ligne,
-   et ne pas définir de nom de fonction. Les fonctions lambda sont également appelées fonctions *anonymes*.

```
programming_languages = [{'language':'Python','year':1991},
{'language':'Swift','year':2014},
{'language':'Java', 'year':1995},
{'language':'C++','year':1985},
{'language':'Go','year':2007},
{'language':'Rust','year':2010},
]

programming_languages.sort(key=lambda element: element['year'])

print(programming_languages)
```

La fonction lambda spécifiée par la ligne `key=lambda element: element['year']` trie ces langages de programmation du plus ancien au plus récent.

## Les différences entre `sort()` et `sorted()`

La méthode `sort()` fonctionne de manière similaire à la fonction `sorted()`.

La syntaxe générale de la fonction `sorted()` ressemble à ceci :

```
sorted(list_name,reverse=...,key=...)
```

Analysons ses composants :

-   `sorted()` est une fonction intégrée qui accepte un itérable. Elle le trie ensuite par ordre croissant ou décroissant.
-   `sorted()` accepte trois paramètres. Un paramètre est obligatoire et les deux autres sont optionnels.
-   `list_name` est le paramètre **obligatoire**. Dans ce cas, le paramètre est une liste, mais `sorted()` accepte n'importe quel autre objet itérable.
-   `sorted()` accepte également les paramètres optionnels `reverse` et `key`, qui sont les mêmes que ceux de la méthode `sort()`.

La différence principale entre `sort()` et `sorted()` est que la fonction `sorted()` prend une liste et **renvoie une nouvelle copie triée** de celle-ci.

La nouvelle copie contient les éléments de la liste originale dans un ordre trié.

Les éléments de la liste originale ne sont pas affectés et restent inchangés.

Pour résumer les différences :

-   La méthode `sort()` n'a pas de valeur de retour et modifie directement la liste originale, changeant l'ordre des éléments qu'elle contient.
-   D'un autre côté, la fonction `sorted()` possède une valeur de retour, qui est une copie triée de la liste originale. Cette copie contient les éléments de la liste originale dans l'ordre trié. Enfin, la liste originale reste intacte.

Jetons un coup d'œil à l'exemple suivant pour voir comment cela fonctionne :

```
#original list of numbers
my_numbers = [10, 8, 3, 22, 33, 7, 11, 100, 54]

#sort original list in default ascending order
my_numbers_sorted = sorted(my_numbers)

#print original list
print(my_numbers)

#print the copy of the original list that was created
print(my_numbers_sorted)

#output

#[10, 8, 3, 22, 33, 7, 11, 100, 54]
#[3, 7, 8, 10, 11, 22, 33, 54, 100]
```

Puisqu'aucun argument supplémentaire n'a été fourni à `sorted()`, elle a ordonné la copie de la liste originale selon l'ordre croissant par défaut, de la plus petite valeur à la plus grande.

Et en affichant la liste originale, vous voyez qu'elle est restée la même et que les éléments ont conservé leur ordre initial.

Comme vous l'avez vu dans l'exemple ci-dessus, la copie de la liste a été assignée à une nouvelle variable, `my_numbers_sorted`.

Une telle opération ne pourrait pas être réalisée avec `sort()`.

Regardez l'exemple suivant pour voir ce qui se passerait si on tentait de le faire avec la méthode `sort()`.

```
my_numbers = [10, 8, 3, 22, 33, 7, 11, 100, 54]

my_numbers_sorted = my_numbers.sort()

print(my_numbers)
print(my_numbers_sorted)

#output

#[3, 7, 8, 10, 11, 22, 33, 54, 100]
#None
```

Vous constatez que la valeur de retour de `sort()` est `None`.

Enfin, notez que les paramètres `reverse` et `key` acceptés par la fonction `sorted()` fonctionnent exactement de la même manière qu'avec la méthode `sort()` vue dans les sections précédentes.

### Quand utiliser `sort()` et `sorted()`

Voici quelques points à considérer pour décider s'il faut utiliser `sort()` ou `sorted()`.

Tout d'abord, considérez le type de données avec lesquelles vous travaillez :

-   Si vous travaillez strictement avec une liste dès le départ, vous devrez utiliser la méthode `sort()` car `sort()` ne peut être appelée que sur des listes.
-   En revanche, si vous voulez plus de flexibilité et que vous ne travaillez pas encore avec une liste, vous pouvez utiliser `sorted()`. La fonction `sorted()` accepte et trie n'importe quel itérable (comme les dictionnaires, les tuples et les ensembles) et pas seulement les listes.

Ensuite, un autre point à considérer est l'importance de conserver l'ordre original de la liste :

-   Lors de l'appel à `sort()`, la liste originale sera modifiée et l'ordre initial sera perdu. Vous ne pourrez pas récupérer les positions originales des éléments de la liste. Utilisez `sort()` lorsque vous êtes certain de vouloir modifier la liste sur laquelle vous travaillez et que vous ne souhaitez pas conserver son ordre initial.
-   D'un autre côté, `sorted()` est utile lorsque vous voulez créer une nouvelle liste tout en conservant celle sur laquelle vous travaillez. La fonction `sorted()` créera une nouvelle liste triée avec les éléments dans l'ordre souhaité.

Enfin, un autre aspect à prendre en compte lors de la manipulation de grands ensembles de données est l'efficacité en termes de temps et de mémoire :

-   La méthode `sort()` consomme moins de mémoire puisqu'elle trie la liste *in-place* et ne crée pas de nouvelle liste inutile. Pour la même raison, elle est également légèrement plus rapide car elle ne crée pas de copie. Cela peut être utile lorsque vous travaillez avec de très grandes listes contenant de nombreux éléments.

## Conclusion

Et voilà ! Vous savez maintenant comment trier une liste en Python en utilisant la méthode `sort()`.

Vous avez également examiné les différences clés entre le tri d'une liste avec `sort()` et `sorted()`.

J'espère que vous avez trouvé cet article utile.

Pour en savoir plus sur le langage de programmation Python, consultez la certification [Scientific Computing with Python][7] de freeCodeCamp.

Vous commencerez par les bases et apprendrez de manière interactive et adaptée aux débutants. Vous réaliserez également cinq projets à la fin pour mettre en pratique et renforcer vos acquis.

Merci de votre lecture et bon codage !

[1]: #heading-la-methode-sort-apercu-de-la-syntaxe
[2]: #heading-comment-trier-les-elements-d-une-liste-par-ordre-croissant-avec-la-methode-sort
[3]: #heading-comment-trier-les-elements-d-une-liste-par-ordre-decroissant-avec-la-methode-sort
[4]: #heading-comment-trier-les-elements-d-une-liste-avec-le-parametre-key-et-la-methode-sort
[5]: #heading-les-differences-entre-sort-et-sorted
[6]: #heading-quand-utiliser-sort-et-sorted
[7]: https://www.freecodecamp.org/learn/scientific-computing-with-python/