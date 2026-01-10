---
title: Python Find in List – Comment trouver l'index d'un élément dans une liste
date: '2022-02-24T20:38:46.000Z'
author: Dionysia Lemonaki
authorURL: https://www.freecodecamp.org/news/author/dionysialemonaki/
originalURL: https://freecodecamp.org/news/python-find-in-list-how-to-find-the-index-of-an-item-or-element-in-a-list
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/pexels-mateusz-dach-450035.jpg
tags:
- name: Python
  slug: python
seo_desc: 'In this article you will learn how to find the index of an element contained
  in a list in the Python programming language.

  There are a few ways to achieve this, and in this article you will learn three of
  the different techniques used to find the ind...'
---


Dans cet article, vous apprendrez à trouver l'index d'un élément contenu dans une liste en langage de programmation Python.

<!-- more -->

Il existe plusieurs façons d'y parvenir, et dans cet article, vous découvrirez trois techniques différentes utilisées pour trouver l'index d'un élément de liste en Python.

Les trois techniques utilisées sont :

-   trouver l'index en utilisant la méthode de liste `index()`,
-   utiliser une boucle `for`,
-   et enfin, utiliser la compréhension de liste et la fonction `enumerate()`.

Plus précisément, voici ce que nous allons aborder en détail :

1.  [Un aperçu des listes en Python][1]
    1.  [Comment fonctionne l'indexation][2]
2.  [Utiliser la méthode `index()` pour trouver l'index d'un élément][3] 1.[Utiliser des paramètres optionnels avec la méthode `index()`][4]
3.  [Obtenir les indices de toutes les occurrences d'un élément dans une liste][5]
    1.  [Utiliser une boucle `for` pour obtenir les indices de toutes les occurrences d'un élément dans une liste][6]
    2.  [Utiliser la compréhension de liste et la fonction `enumerate()` pour obtenir les indices de toutes les occurrences d'un élément dans une liste][7]

## Que sont les listes en Python ?

Les listes sont un type de données intégré en Python, et l'une des structures de données les plus puissantes.

Elles agissent comme des conteneurs et stockent plusieurs éléments, généralement liés, sous le même nom de variable.

Les éléments sont placés et enfermés à l'intérieur de crochets, `[]`. Chaque élément à l'intérieur des crochets est séparé par une virgule, `,`.

```
# a list called 'my_information' that contains strings and numbers
my_information = ["John Doe", 34, "London", 1.76]
```

D'après l'exemple ci-dessus, vous pouvez voir que les listes peuvent contenir des éléments de n'importe quel type de données, ce qui signifie que les éléments de la liste peuvent être hétérogènes.

Contrairement aux tableaux qui ne stockent que des éléments du même type, les listes offrent plus de flexibilité.

Les listes sont également *muables*, ce qui signifie qu'elles sont modifiables et dynamiques. Les éléments de la liste peuvent être mis à jour, de nouveaux éléments peuvent être ajoutés à la liste, et n'importe quel élément peut être supprimé à tout moment pendant la durée de vie du programme.

### Un aperçu de l'indexation en Python

Comme mentionné, les listes sont une collection d'éléments. Plus précisément, elles sont une collection ordonnée d'éléments et elles conservent cet ordre défini pour l'essentiel.

Chaque élément à l'intérieur d'une liste possède une position unique qui l'identifie.

Cette position est appelée l'index de l'élément.

Les indices en Python, et dans tous les langages de programmation, commencent à `0` et **non** à `1`.

Jetons un coup d'œil à la liste utilisée dans la section précédente :

```
my_information = ["John Doe", 34, "London", 1.76]
```

La liste est indexée à partir de zéro et le comptage commence à `0`.

Le premier élément de la liste, `"John Doe"`, a un index de `0`. Le deuxième élément de la liste, `34`, a un index de `1`. Le troisième élément de la liste, `"London"`, a un index de `2`. Le quatrième élément de la liste, `1.76`, a un index de `3`.

Les indices sont utiles pour accéder à des éléments spécifiques de la liste dont vous connaissez la position (index).

Ainsi, vous pouvez récupérer n'importe quel élément de la liste en utilisant son index.

Pour accéder à un élément, indiquez d'abord le nom de la liste, puis, entre crochets, l'entier correspondant à l'index de l'élément auquel vous souhaitez accéder.

Voici comment vous accéderiez à chaque élément en utilisant son index :

```
my_information = ["John Doe", 34, "London", 1.76]

print(my_information[0])
print(my_information[1])
print(my_information[2])
print(my_information[3])

#output

#John Doe
#34
#London
#1.76
```

Mais qu'en est-il de la *recherche* de l'index d'un élément de liste en Python ?

Dans les sections qui suivent, vous verrez quelques-unes des façons de trouver l'index des éléments d'une liste.

## Trouver l'index d'un élément en utilisant la méthode de liste `index()` en Python

Jusqu'à présent, vous avez vu comment accéder à une valeur en référençant son numéro d'index.

Que se passe-t-il cependant lorsque vous ne connaissez pas le numéro d'index et que vous travaillez avec une grande liste ?

Vous pouvez fournir une valeur et trouver son index, et ainsi vérifier la position qu'elle occupe dans la liste.

Pour cela, la méthode intégrée `index()` de Python est utilisée comme outil de recherche.

La syntaxe de la méthode `index()` ressemble à ceci :

```
my_list.index(item, start, end)
```

Analysons cela :

-   `my_list` est le nom de la liste dans laquelle vous effectuez la recherche.
-   `.index()` est la méthode de recherche qui prend trois paramètres. Un paramètre est obligatoire et les deux autres sont optionnels.
-   `item` est le paramètre obligatoire. C'est l'élément dont vous recherchez l'index.
-   `start` est le premier paramètre optionnel. C'est l'index à partir duquel vous commencerez votre recherche.
-   `end` est le second paramètre optionnel. C'est l'index où vous terminerez votre recherche.

Voyons un exemple utilisant uniquement le paramètre obligatoire :

```
programming_languages = ["JavaScript","Python","Java","C++"]

print(programming_languages.index("Python"))

#output
#1
```

Dans l'exemple ci-dessus, la méthode `index()` ne prend qu'un seul argument qui est l'élément dont vous recherchez l'index.

Gardez à l'esprit que l'argument que vous passez est *sensible à la casse*. Cela signifie que si vous aviez passé "python" et non "Python", vous auriez reçu une erreur car "python" avec un "p" minuscule ne fait pas partie de la liste.

La valeur de retour est un entier, qui est le numéro d'index de l'élément de la liste passé en argument à la méthode.

Voyons un autre exemple :

```
programming_languages = ["JavaScript","Python","Java","C++"]

print(programming_languages.index("React"))

#output
#line 3, in <module>
#    print(programming_languages.index("React"))
#ValueError: 'React' is not in list
```

Si vous essayez de rechercher un élément mais qu'il n'y a pas de correspondance dans la liste, Python lèvera une erreur en tant que valeur de retour — plus précisément, il renverra une `ValueError`.

Cela signifie que l'élément que vous recherchez n'existe pas dans la liste.

Une façon d'empêcher cela est d'envelopper l'appel à la méthode `index()` dans un bloc `try/except`.

Si la valeur n'existe pas, un message s'affichera dans la console indiquant qu'elle n'est pas stockée dans la liste et qu'elle n'existe donc pas.

```
programming_languages = ["JavaScript","Python","Java","Python","C++","Python"]

try:
    print(programming_languages.index("React"))
except ValueError:
    print("That item does not exist")

#output
#That item does not exist
```

Une autre façon serait de vérifier si l'élément se trouve dans la liste avant de chercher son numéro d'index. Le résultat sera une valeur booléenne — soit True, soit False.

```
programming_languages = ["JavaScript","Python","Java","Python","C++","Python"]

print("React" in programming_languages)

#output
#False
```

### Comment utiliser les paramètres optionnels avec la méthode `index()`

Jetons un coup d'œil à l'exemple suivant :

```
programming_languages = ["JavaScript","Python","Java","Python","C++","Python"]

print(programming_languages.index("Python"))

#output
#1
```

Dans la liste `programming_languages`, il y a trois instances de la chaîne "Python" recherchée.

Pour tester, vous pourriez travailler à l'envers car, dans ce cas, la liste est petite.

Vous pourriez compter et trouver leurs numéros d'index, puis les référencer comme vous l'avez vu dans les sections précédentes :

```
programming_languages = ["JavaScript","Python","Java","Python","C++","Python"]

print(programming_languages[1])
print(programming_languages[3])
print(programming_languages[5])

#output
#Python
#Python
#Python
```

Il y en a un à la position `1`, un autre à la position `3` et le dernier à la position `5`.

Pourquoi ne s'affichent-ils pas dans la sortie lorsque la méthode `index()` est utilisée ?

Lorsque la méthode `index()` est utilisée, la valeur de retour est uniquement la **première occurrence** de l'élément dans la liste. Les autres occurrences ne sont pas renvoyées.

La méthode `index()` ne renvoie que l'index de la position où l'élément apparaît pour la **première** fois.

Vous pourriez essayer de passer les paramètres optionnels `start` et `end` à la méthode `index()`.

Vous savez déjà que la première occurrence commence à l'index `1`, cela pourrait donc être la valeur du paramètre `start`.

Pour le paramètre `end`, vous pourriez d'abord trouver la longueur de la liste.

Pour trouver la longueur, utilisez la fonction `len()` :

```
print(len(programming_languages)) 

#output is 6
```

La valeur du paramètre `end` serait alors la longueur de la liste moins 1. L'index du dernier élément d'une liste est toujours inférieur de un à la longueur de la liste.

Ainsi, en mettant tout cela ensemble, voici comment vous pourriez essayer d'obtenir les trois instances de l'élément :

```
programming_languages = ["JavaScript","Python","Java","Python","C++","Python"]

print(programming_languages.index("Python",1,5))

#output
#1
```

La sortie renvoie toujours uniquement la première instance !

Bien que les paramètres `start` et `end` fournissent une plage de positions pour votre recherche, la valeur de retour lors de l'utilisation de la méthode `index()` reste uniquement la première occurrence de l'élément dans la liste.

## Comment obtenir les indices de toutes les occurrences d'un élément dans une liste

### Utiliser une boucle `for` pour obtenir les indices de toutes les occurrences d'un élément dans une liste

Prenons le même exemple que celui utilisé jusqu'à présent.

Cette liste contient trois occurrences de la chaîne "Python".

```
programming_languages = ["JavaScript","Python","Java","Python","C++","Python"]
```

Tout d'abord, créez une nouvelle liste vide.

Ce sera la liste où tous les indices de "Python" seront stockés.

```
programming_languages = ["JavaScript","Python","Java","Python","C++","Python"]

python_indices = []
```

Ensuite, utilisez une boucle `for`. C'est un moyen d'itérer (ou de boucler) à travers la liste et d'obtenir chaque élément de la liste originale. Plus précisément, nous bouclons sur le numéro d'index de chaque élément.

```
programming_languages = ["JavaScript","Python","Java","Python","C++","Python"]

python_indices = []

for programming_language in range(len(programming_languages)):
```

Vous utilisez d'abord le mot-clé `for`.

Ensuite, créez une variable, dans ce cas `programming_language`, qui servira d'espace réservé pour la position de chaque élément dans la liste originale, pendant le processus d'itération.

Ensuite, vous devez spécifier le nombre défini d'itérations que la boucle `for` doit effectuer.

Dans ce cas, la boucle itérera sur toute la longueur de la liste, du début à la fin. La syntaxe `range(len(programming_languages))` est un moyen d'accéder à tous les éléments de la liste `programming_languages`.

La fonction `range()` prend une séquence de nombres qui spécifient le nombre à partir duquel elle doit commencer à compter et le nombre avec lequel elle doit terminer le comptage.

La fonction `len()` calcule la longueur de la liste, donc dans ce cas, le comptage commencerait à `0` et se terminerait à — mais sans inclure — `6`, qui est la fin de la liste.

Enfin, vous devez définir une condition logique.

Essentiellement, vous voulez dire : « Si pendant l'itération, la valeur à la position donnée est égale à 'Python', ajoute cette position à la nouvelle liste que j'ai créée précédemment ».

Vous utilisez la méthode `append()` pour ajouter un élément à une liste.

```
programming_languages = ["JavaScript","Python","Java","Python","C++","Python"]

python_indices = []

for programming_language in range(len(programming_languages)):
    if programming_languages[programming_language] == "Python":
      python_indices.append(programming_language)

print(python_indices)

#output

#[1, 3, 5]
```

### Utiliser la compréhension de liste et la fonction `enumerate()` pour obtenir les indices de toutes les occurrences d'un élément dans une liste

Une autre façon de trouver les indices de toutes les occurrences d'un élément particulier est d'utiliser la compréhension de liste.

La compréhension de liste est un moyen de créer une nouvelle liste basée sur une liste existante.

Voici comment vous obtiendriez tous les indices de chaque occurrence de la chaîne "Python", en utilisant la compréhension de liste :

```
programming_languages = ["JavaScript","Python","Java","Python","C++","Python"]

python_indices  = [index for (index, item) in enumerate(programming_languages) if item == "Python"]

print(python_indices)

#[1, 3, 5]
```

Avec la fonction `enumerate()`, vous pouvez stocker les indices des éléments qui remplissent la condition que vous avez définie.

Elle fournit d'abord une paire (`index, item`) pour chaque élément de la liste (`programming_languages`) passé en argument à la fonction.

`index` correspond au numéro d'index de l'élément de la liste et `item` correspond à l'élément de la liste lui-même.

Ensuite, elle agit comme un compteur qui commence à compter à partir de `0` et s'incrémente chaque fois que la condition que vous avez définie est remplie, sélectionnant et déplaçant les indices des éléments qui répondent à vos critères.

Associée à la compréhension de liste, une nouvelle liste est créée avec tous les indices de la chaîne "Python".

## Conclusion

Et voilà ! Vous connaissez maintenant quelques-unes des façons de trouver l'index d'un élément, ainsi que les moyens de trouver les indices de plusieurs occurrences d'un élément, dans une liste en Python.

J'espère que vous avez trouvé cet article utile.

Pour en savoir plus sur le langage de programmation Python, consultez la [Certification Scientific Computing with Python][8] de freeCodeCamp.

Vous partirez des bases et apprendrez de manière interactive et adaptée aux débutants. Vous réaliserez également cinq projets à la fin pour mettre en pratique et renforcer ce que vous avez appris.

Merci de votre lecture et bon codage !

[1]: #heading-que-sont-les-listes-en-python
[2]: #heading-un-apercu-de-l-indexation-en-python
[3]: #heading-trouver-l-index-d-un-element-en-utilisant-la-methode-de-liste-index-en-python
[4]: #heading-comment-utiliser-les-parametres-optionnels-avec-la-methode-index
[5]: #heading-comment-obtenir-les-indices-de-toutes-les-occurrences-d-un-element-dans-une-liste
[6]: #heading-utiliser-une-boucle-for-pour-obtenir-les-indices-de-toutes-les-occurrences-d-un-element-dans-une-liste
[7]: #heading-utiliser-la-comprehension-de-liste-et-la-fonction-enumerate-pour-obtenir-les-indices-de-toutes-les-occurrences-d-un-element-dans-une-liste
[8]: https://www.freecodecamp.org/learn/scientific-computing-with-python/