---
title: Trier un Dictionnaire par Valeur en Python – Comment Trier un Dict
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-09-13T15:16:42.000Z'
originalURL: https://freecodecamp.org/news/sort-dictionary-by-value-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/sortDictByValue.png
tags:
- name: dictionary
  slug: dictionary
- name: Python
  slug: python
seo_title: Trier un Dictionnaire par Valeur en Python – Comment Trier un Dict
seo_desc: 'In Python, a dictionary is a fat structure that is unordered by default.
  So, sometimes, you''ll want to sort dictionaries by key or value to make queries
  easier.

  The problem is that sorting a dictionary by value is never a straightforward thing
  to do....'
---

En Python, un dictionnaire est une structure riche qui est non ordonnée par défaut. Ainsi, parfois, vous voudrez trier les dictionnaires par clé ou par valeur pour faciliter les requêtes.

Le problème est que trier un dictionnaire par valeur n'est jamais une chose simple à faire. Cela est dû au fait que Python n'a pas de méthode intégrée pour le faire.

Cependant, j'ai trouvé un moyen de trier les dictionnaires par valeur, et c'est ce que je vais vous montrer comment faire dans cet article.

## Ce que nous allons couvrir
- [Comment Trier des Données avec la Méthode `sorted()`](#heading-comment-trier-des-donnees-avec-la-methode-sorted)
- [Comment la Méthode `sorted()` Fonctionne](#heading-comment-la-methode-sorted-fonctionne)
  - [Paramètres de la Méthode `sorted()`](#heading-parametres-de-la-methode-sorted)
- [Comment Trier un Dictionnaire avec la Méthode `sorted()`](#heading-comment-trier-un-dictionnaire-avec-la-methode-sorted)
  - [Comment Convertir la Liste Résultante en un Dictionnaire](#heading-comment-convertir-la-liste-resultante-en-un-dictionnaire)
  - [Comment Trier le Dictionnaire par Valeur en Ordre Ascendant ou Descendant](#heading-comment-trier-le-dictionnaire-par-valeur-en-ordre-ascendant-ou-descendant)
- [Conclusion](#heading-conclusion)


## Comment Trier des Données avec la Méthode `sorted()`

La méthode `sorted()` trie les données itérables telles que les listes, les tuples et les dictionnaires. Mais elle trie uniquement par clé.

La méthode `sorted()` place les éléments triés dans une liste. C'est un autre problème que nous devons résoudre, car nous voulons que le dictionnaire trié reste un dictionnaire.

Par exemple, `sorted()` a organisé la liste ci-dessous par ordre alphabétique :
```py
persons = ['Chris', 'Amber', 'David', 'El-dorado', 'Brad', 'Folake']
sortedPersons = sorted(persons)

print(sortedPersons)
# Output: ['Amber', 'Brad', 'Chris', 'David', 'El-dorado', 'Folake']
```

Et la méthode `sorted()` trie les nombres dans le tuple ci-dessous par ordre croissant :
```py
numbers = (14, 3, 1, 4, 2, 9, 8, 10, 13, 12)
sortedNumbers = sorted(numbers)

print(sortedNumbers)
# Output: [1, 2, 3, 4, 8, 9, 10, 12, 13, 14]
```

Si vous utilisez la méthode `sorted()` avec un dictionnaire, seules les clés seront retournées et, comme d'habitude, ce sera dans une liste :
```py
my_dict = { 'num6': 6, 'num3': 3, 'num2': 2, 'num4': 4, 'num1': 1, 'num5': 5}
sortedDict = sorted(my_dict)

print(sortedDict)
# ['num1', 'num2', 'num3', 'num4', 'num5', 'num6']
```
Ce n'est pas le comportement que vous souhaitez. Vous voulez que le dictionnaire soit trié par valeur et reste un dictionnaire. C'est ce que je vais vous montrer ensuite.

## Comment la Méthode `sorted()` Fonctionne
Pour trier un dictionnaire, nous allons toujours utiliser la fonction sorted, mais de manière plus compliquée. Ne vous inquiétez pas, je vais expliquer tout ce que vous devez savoir.

Puisque nous allons toujours utiliser la méthode `sorted()`, il est temps d'expliquer la méthode `sorted()` en détail.

### Paramètres de la Méthode `sorted()`

La méthode `sorted()` peut accepter jusqu'à 3 paramètres :

- iterable – les données à itérer. Cela pourrait être un tuple, une liste ou un dictionnaire.

- key – une valeur optionnelle, la fonction qui vous aide à effectuer une opération de tri personnalisée.

- reverse – une autre valeur optionnelle. Elle vous aide à organiser les données triées par ordre croissant ou décroissant.

Si vous devinez correctement, le paramètre key est ce que nous allons passer dans la méthode `sorted()` pour obtenir le dictionnaire trié par valeur.

Maintenant, il est temps de trier notre dictionnaire par valeur et de s'assurer qu'il reste un dictionnaire.

## Comment Trier un Dictionnaire avec la Méthode `sorted()`

Pour trier correctement un dictionnaire par valeur avec la méthode `sorted()`, vous devrez faire ce qui suit :

- passer le dictionnaire à la méthode `sorted()` en tant que première valeur
- utiliser la méthode `items()` sur le dictionnaire pour récupérer ses clés et valeurs
- écrire une fonction lambda pour obtenir les valeurs récupérées avec la méthode `item()`

Voici un exemple :
```py
footballers_goals = {'Eusebio': 120, 'Cruyff': 104, 'Pele': 150, 'Ronaldo': 132, 'Messi': 125}

sorted_footballers_by_goals = sorted(footballers_goals.items(), key=lambda x:x[1])
print(sorted_footballers_by_goals)

```
Comme je l'ai dit plus tôt, nous devons obtenir ces valeurs du dictionnaire afin de pouvoir trier le dictionnaire par valeurs. C'est pourquoi vous pouvez voir 1 dans la fonction lambda.

1 représente les index des valeurs. Les clés sont 0. Souvenez-vous qu'un programmeur commence à compter à partir de 0, et non de 1.

Avec ce code ci-dessus, j'ai obtenu le résultat ci-dessous :
```py
# [('Cruyff', 104), ('Eusebio', 120), ('Messi', 125), ('Ronaldo', 132), ('Pele', 150)]
```

Voici le code complet pour que vous ne soyez pas confus :
```py
footballers_goals = {'Eusebio': 120, 'Cruyff': 104, 'Pele': 150, 'Ronaldo': 132, 'Messi': 125}

sorted_footballers_by_goals = sorted(footballers_goals.items(), key=lambda x:x[1])
print(sorted_footballers_by_goals)

# [('Cruyff', 104), ('Eusebio', 120), ('Messi', 125), ('Ronaldo', 132), ('Pele', 150)]
```

Vous pouvez voir que le dictionnaire a été trié par valeurs en ordre croissant. Vous pouvez également le trier en ordre décroissant. Mais nous verrons cela plus tard car nous avons encore un problème avec le résultat obtenu.

Le problème est que le dictionnaire n'est plus un dictionnaire. Les clés et valeurs individuelles ont été placées dans un tuple et ensuite condensées dans une liste. Souvenez-vous que tout ce que vous obtenez comme résultat de la méthode `sorted()` est placé dans une liste.

Nous avons été capables de trier les éléments dans le dictionnaire par valeur. Ce qui reste est de le convertir à nouveau en dictionnaire.

### Comment Convertir la Liste Résultante en un Dictionnaire

Pour convertir la liste résultante en un dictionnaire, vous n'avez pas besoin d'écrire une autre fonction compliquée ou une boucle. Vous devez simplement passer la variable sauvegardant la liste résultante dans la méthode `dict()`.

```py
converted_dict = dict(sorted_footballers_by_goals)
print(converted_dict)
# Output: {'Cruyff': 104, 'Eusebio': 120, 'Messi': 125, 'Ronaldo': 132, 'Pele': 150}
```

Souvenez-vous que nous avons sauvegardé le dictionnaire trié dans la variable nommée `sorted_footballers_by_goals`, donc c'est la variable que nous devons passer à `dict()`.

Le code complet ressemble à ceci :
```py
footballers_goals = {'Eusebio': 120, 'Cruyff': 104, 'Pele': 150, 'Ronaldo': 132, 'Messi': 125}

sorted_footballers_by_goals = sorted(footballers_goals.items(), key=lambda x:x[1])
converted_dict = dict(sorted_footballers_by_goals)

print(converted_dict)
# Output: {'Cruyff': 104, 'Eusebio': 120, 'Messi': 125, 'Ronaldo': 132, 'Pele': 150}
```
C'est tout ! Nous avons été capables de trier les éléments dans le dictionnaire et de les convertir à nouveau en dictionnaire. Nous avons eu notre gâteau et nous l'avons mangé aussi !

### Comment Trier le Dictionnaire par Valeur en Ordre Ascendant ou Descendant
Souvenez-vous que la méthode `sorted()` accepte une troisième valeur appelée `reverse`.

`reverse` avec une valeur de `True` organisera le dictionnaire trié en ordre décroissant.
```py
footballers_goals = {'Eusebio': 120, 'Cruyff': 104, 'Pele': 150, 'Ronaldo': 132, 'Messi': 125}

sorted_footballers_by_goals = sorted(footballers_goals.items(), key=lambda x:x[1], reverse=True)
converted_dict = dict(sorted_footballers_by_goals)

print(converted_dict)
# Output: {'Pele': 150, 'Ronaldo': 132, 'Messi': 125, 'Eusebio': 120, 'Cruyff': 104}
```
Vous pouvez voir que la sortie est inversée car nous avons passé `reverse=True` à la méthode `sorted()`.

Si vous ne définissez pas `reverse` du tout ou si vous définissez sa valeur à false, le dictionnaire sera organisé en ordre croissant. C'est le comportement par défaut.

## Conclusion
Félicitations. Vous pouvez maintenant trier un dictionnaire par valeur malgré l'absence de méthode ou de fonction intégrée à utiliser en Python.

Cependant, il y a quelque chose qui a éveillé ma curiosité lorsque je préparais cet article. Souvenez-vous que nous avons pu utiliser `sorted()` directement sur un dictionnaire. Cela nous a donné une liste comme résultat, bien que nous n'ayons obtenu que les clés et non les valeurs.

Que se passe-t-il si nous convertissons cette liste en un dictionnaire avec la méthode `dict()` ? Pensez-vous que nous pouvons obtenir le résultat souhaité ? Voyons cela :
```py
my_dict = { 'num6': 6, 'num3': 3, 'num2': 2, 'num4': 4, 'num1': 1, 'num5': 5}
sortedDict = sorted(my_dict)

converted_dict = dict(sortedDict)
print(converted_dict)
"""
Output: 
dict_by_value.py
Traceback (most recent call last):
  File "sort_dict_by_value.py", line 17, in <module>
    converted_dict = dict(sortedDict)
ValueError: dictionary update sequence element #0 has length 4; 2 is required
"""
```

Nous avons obtenu une erreur ! Cela est dû au fait que si vous voulez créer un dictionnaire à partir d'une liste, vous devez utiliser la compréhension de dictionnaire. Et si vous utilisez la compréhension de dictionnaire pour ce type de données, vous devrez spécifier une valeur pour toutes les entrées. Cela défierait le but de trier un dictionnaire par valeur, donc ce n'est pas ce que nous voulons.

Si vous voulez en savoir plus sur la compréhension de dictionnaire, vous devriez [lire cet article](https://www.freecodecamp.org/news/dictionary-comprehension-in-python-explained-with-examples/).

Merci d'avoir lu !