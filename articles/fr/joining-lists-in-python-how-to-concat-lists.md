---
title: Fusionner des listes en Python – Comment concaténer des listes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-03-14T16:30:27.000Z'
originalURL: https://freecodecamp.org/news/joining-lists-in-python-how-to-concat-lists
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/Shittu-Olumide-Joining-Lists-in-Python
seo_title: Fusionner des listes en Python – Comment concaténer des listes
---

How-to-Concat-Lists-1.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "Par Shittu Olumide\nLe processus de combinaison de deux ou plusieurs chaînes, listes ou autres structures de données en une seule entité est connu sous le nom de concaténation en programmation.\n\nLa concaténation produit un nouvel objet avec tous les composants des objets originaux, disposés..."
---

Par Shittu Olumide

Le processus de combinaison de deux ou plusieurs chaînes, listes ou autres structures de données en une seule entité est connu sous le nom de concaténation en programmation.

La concaténation produit un nouvel objet contenant tous les composants des objets originaux, disposés dans l'ordre de concaténation.

La concaténation dans le contexte des chaînes de caractères consiste à joindre une chaîne à la fin d'une autre chaîne pour créer une chaîne plus longue. Par exemple, créer la chaîne `"helloworld"` en joignant les mots `"hello"` et `"world"` ensemble.

La concaténation dans le contexte des listes signifie que vous créez une nouvelle liste qui incorpore chaque élément de deux listes ou plus. Par exemple, la liste `[1, 2, 3, 4, 5, 6]` serait créée à partir de la concaténation des deux listes `[1, 2, 3]` et `[4, 5, 6]`.

La concaténation est une opération de programmation courante utilisée pour combiner des données à des fins diverses, notamment la création de rapports, la gestion de grands ensembles de données et la création de structures de données complexes.

## Concaténation de listes en Python

La concaténation de listes est une opération courante en programmation Python. Dans de nombreuses situations, vous pourriez avoir besoin de fusionner deux ou plusieurs listes en une seule liste pour effectuer des opérations sur les données combinées.

Python propose une variété de méthodes pour concaténer des listes, des fonctions intégrées simples aux méthodes plus sophistiquées impliquant la compréhension de liste et le découpage (slicing).

Dans cet article, nous examinerons diverses techniques de concaténation en Python. À la fin de votre lecture, vous saurez exactement comment concaténer des listes en Python et serez en mesure de choisir l'approche qui convient le mieux à votre cas d'utilisation particulier.

## Comment concaténer des listes à l'aide de l'opérateur `+` 

La première technique, et la plus simple, pour concaténer deux listes consiste à utiliser l'opérateur `**+**`. Il crée une nouvelle liste en concaténant les deux listes ensemble.

Exemple :

```py
first_list = [1, 2, 3]
second_list = [4, 5, 6]

# concaténation des deux listes
concat_list = first_list + second_list

# affiche la liste concaténée
print(concat_list)

```

Sortie :

```bash
[1, 2, 3, 4, 5, 6]

```

## Comment concaténer des listes à l'aide de l'opérateur `*` 

Vous pouvez utiliser l'opérateur `*` pour répéter une liste un certain nombre de fois. En répétant une liste et en la concaténant avec elle-même, nous pouvons réaliser la concaténation de plusieurs copies d'une liste.

Exemple :

```py
first_list = [1, 2, 3]
second_list = first_list * 3

print(second_list)

```

Sortie :

```bash
[1, 2, 3, 1, 2, 3, 1, 2, 3]

```

## Comment concaténer des listes à l'aide de la compréhension de liste

La compréhension de liste est un moyen concis et lisible de créer une nouvelle liste en Python en itérant sur un objet itérable existant (comme une liste, un tuple, une chaîne de caractères, etc.) et en appliquant une transformation ou un filtre à chaque élément de l'itérable.

Syntaxe de la compréhension de liste :

```py
new_list = [expression for item in iterable if condition]

```

Ici, `expression` est l'opération ou la fonction à appliquer à chaque élément de l'itérable, `item` est une variable qui prend tour à tour chaque élément de l'itérable, `iterable` est l'objet itérable d'origine, et `condition` est une condition facultative qui filtre les éléments à inclure dans la nouvelle liste.

Vous pouvez utiliser la compréhension de liste pour concaténer plusieurs listes en une seule liste. Jetons un coup d'œil à un exemple.

```py
# définition des listes
first_list = [1, 2, 3]
second_list = [4, 5, 6]
third_list = [7, 8, 9]

# utilisation de la compréhension de liste
fourth_list = [x for lst in [first_list, second_list, third_list] for x in lst]


print(fourth_list)

```

Sortie :

```bash
[1, 2, 3, 4, 5, 6, 7, 8, 9]

```

## Comment concaténer des listes à l'aide de la méthode `append()` dans une boucle

Un élément peut être ajouté à la fin d'une liste existante en Python en utilisant la méthode `append()`, qui est une fonction intégrée des listes.

La syntaxe pour utiliser `append()` est :

```py
list_name.append(element)

```

Dans le code, `list_name` est le nom de la liste à laquelle vous souhaitez ajouter un élément, et `element` est la valeur que vous souhaitez ajouter à la liste.

Vous pouvez utiliser la méthode `append()` à l'intérieur d'une boucle pour ajouter les éléments d'une liste à une autre.

Exemple :

```py
first_list = [1, 2, 3]
second_list = [4, 5, 6]

for element in second_list:
    first_list.append(element)
    
print(first_list)

```

Sortie :

```bash
[1, 2, 3, 4, 5, 6]

```

## Comment concaténer des listes à l'aide de la méthode `extend()` 

En concaténant une liste existante avec un autre objet itérable, la méthode `extend()` des listes en Python vous permet d'ajouter plusieurs éléments à une liste existante.

La syntaxe de `extend()` est la suivante :

```py
list_name.extend(iterable)

```

Ici, `iterable` est n'importe quel objet itérable (tel qu'une liste, un tuple, une chaîne, etc.) qui contient les éléments que vous souhaitez ajouter à la liste, et `list_name` est le nom de la liste à laquelle vous souhaitez ajouter des éléments.

You pouvez utiliser la méthode `extend()` pour ajouter tous les éléments d'une liste à la fin de la liste d'origine.

Exemple :

```py
first_list = [1, 2, 3]
second_list = [4, 5, 6]

# utilisation de la méthode extend()
first_list.extend(second_list)

print(first_list)

```

Sortie :

```bash
[1, 2, 3, 4, 5, 6]

```

## Alors, quand devriez-vous utiliser chaque méthode ?

**Utilisation de l'opérateur `*`** : Vous pouvez utiliser l'opérateur `*` dans la concaténation de listes lorsque vous souhaitez répéter une liste un certain nombre de fois ou pour créer une nouvelle liste en répétant les éléments de la liste d'origine par une valeur scalaire.

**Utilisation de l'opérateur `+`** : Cette méthode est simple et facile à lire, mais elle peut être inefficace lors de la manipulation de grandes listes car elle crée une nouvelle liste à chaque fois qu'elle est utilisée.

**Utilisation de la méthode `append()`** : La méthode `append()` en Python ajoute un élément à la fin d'une liste. On ne l'utilise généralement pas pour la concaténation de listes, mais plutôt pour ajouter des éléments individuels à une liste existante.

**Utilisation de la méthode `extend()`** : Cette méthode consiste à utiliser la méthode `extend()` pour ajouter les éléments d'une liste à la fin d'une autre liste. La méthode `extend()` modifie la liste d'origine au lieu de créer une nouvelle liste, ce qui la rend plus efficace en termes de mémoire que l'opérateur `+`. Cependant, elle peut toujours être plus lente que la méthode de compréhension de liste pour de très grandes listes.

## Conclusion

Dans cet article, nous avons exploré différentes manières de concaténer des listes en Python, notamment à l'aide de l'opérateur `+`, de l'opérateur `*`, de la méthode `extend()`, de la méthode `append()` et de la compréhension de liste. Nous avons également discuté de la meilleure méthode à utiliser selon votre cas d'utilisation.

Connectons-nous sur [Twitter](https://www.twitter.com/Shittu_Olumide_) et sur [LinkedIn](https://www.linkedin.com/in/olumide-shittu). Vous pouvez également vous abonner à ma chaîne [YouTube](https://www.youtube.com/channel/UCNhFxpk6hGt5uMCKXq0Jl8A).

Bon code !