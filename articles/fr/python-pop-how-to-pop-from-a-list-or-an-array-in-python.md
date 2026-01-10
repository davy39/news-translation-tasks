---
title: Python .pop() – Comment supprimer un élément d'une liste ou d'un tableau en
  Python
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-03-01T20:30:51.000Z'
originalURL: https://freecodecamp.org/news/python-pop-how-to-pop-from-a-list-or-an-array-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/pexels-olia-danilevich-4974912.jpg
tags:
- name: Python
  slug: python
seo_title: Python .pop() – Comment supprimer un élément d'une liste ou d'un tableau
  en Python
seo_desc: "In this article, you'll learn how to use Python's built-in pop() list method.\n\
  By the end, you'll know how to use pop() to remove an item from a list in Python.\n\
  Here is what we will cover:\n\nAn overview of lists in Python\n How to delete list\
  \ items usin..."
---

Dans cet article, vous apprendrez à utiliser la méthode intégrée `pop()` des listes en Python.

À la fin, vous saurez comment utiliser `pop()` pour supprimer un élément d'une liste en Python.

Voici ce que nous allons couvrir :

1. [Un aperçu des listes en Python](#introduction)
2. [Comment supprimer des éléments de liste en utilisant `pop()`](#pop-introduction)
    1. [Syntaxe de la méthode `pop()`](#syntaxe)
    2. [Utiliser la méthode `pop()` sans paramètre](#sans-parametre)
    3. [Utiliser la méthode `pop()` avec un paramètre optionnel](#avec-parametre)
    4. [Gérer les erreurs courantes](#erreurs)

## Qu'est-ce que les listes en Python et comment les créer <a name="introduction"></a>

Les listes sont un type de données intégré en Python. Elles agissent comme des conteneurs, stockant des collections de données.

Les listes sont créées en utilisant des crochets, `[]`, comme ceci :

```python
# une liste vide
ma_liste = []

print(ma_liste)
print(type(ma_liste))

# sortie

# []
# <class 'list'>
```

Vous pouvez également créer une liste en utilisant le constructeur `list()` :

```python
# une liste vide
ma_liste = list()

print(ma_liste)
print(type(ma_liste))

# sortie

# []
# <class 'list'>
```

Comme vous l'avez vu ci-dessus, une liste peut contenir `0` éléments, et dans ce cas, elle est considérée comme une liste vide.

Les listes peuvent également contenir des éléments, ou des éléments de liste. Les éléments de liste sont enfermés à l'intérieur des crochets et sont chacun séparés par une virgule, `,`.

Les éléments de liste peuvent être homogènes, ce qui signifie qu'ils sont du même type.

Par exemple, vous pouvez avoir une liste de nombres uniquement, ou une liste de texte uniquement :

```python
# une liste d'entiers
ma_liste_de_nombres = [10, 20, 30, 40, 50]

# une liste de chaînes de caractères
noms = ["Josie", "Jordan", "Joe"]

print(ma_liste_de_nombres)
print(noms)

# sortie

# [10, 20, 30, 40, 50]
# ['Josie', 'Jordan', 'Joe']
```

Les éléments de liste peuvent également être hétérogènes, ce qui signifie qu'ils peuvent être de différents types de données.

C'est ce qui distingue les listes des tableaux. Les tableaux nécessitent que les éléments soient du même type de données, alors que les listes ne le nécessitent pas.

```python
# une liste contenant des chaînes de caractères, des entiers et des nombres à virgule flottante
mes_informations = ["John", "Doe", 34, "London", 1.76]

print(mes_informations)

# sortie

# ['John', 'Doe', 34, 'London', 1.76]
```

Les listes sont *mutables*, ce qui signifie qu'elles sont modifiables. Les éléments de liste peuvent être mis à jour, les éléments de liste peuvent être supprimés, et de nouveaux éléments peuvent être ajoutés à la liste.


## Comment supprimer des éléments d'une liste en utilisant la méthode `pop()` en Python <a name="pop-introduction"></a>

Dans les sections suivantes, vous apprendrez à utiliser la méthode `pop()` pour supprimer des éléments de listes en Python.

### La méthode `pop()` - Aperçu de la syntaxe <a name="syntaxe"></a>

La syntaxe générale de la méthode `pop()` ressemble à ceci :

```python
nom_de_la_liste.pop(index)
```

Décomposons cela :

- `nom_de_la_liste` est le nom de la liste avec laquelle vous travaillez.
- La méthode intégrée `pop()` de Python prend un seul paramètre **optionnel**.
- Le paramètre optionnel est l'index de l'élément que vous souhaitez supprimer.

### Comment utiliser la méthode `pop()` sans paramètre <a name="sans-parametre"></a>

Par défaut, si aucun index n'est spécifié, la méthode `pop()` supprimera le **dernier** élément contenu dans la liste.

Cela signifie que lorsque la méthode `pop()` n'a aucun argument, elle supprimera le dernier élément de la liste.

Ainsi, la syntaxe pour cela ressemblerait à ceci :

```python
nom_de_la_liste.pop()
```

Regardons un exemple :

```python
# liste de langages de programmation
langages_de_programmation = ["Python", "Java", "JavaScript"]

# afficher la liste initiale
print(langages_de_programmation)

# supprimer le dernier élément, qui est "JavaScript"
langages_de_programmation.pop()

# afficher la liste à nouveau
print(langages_de_programmation)

# sortie

# ['Python', 'Java', 'JavaScript']
# ['Python', 'Java']
```

En plus de simplement supprimer l'élément, `pop()` le retourne également.

Cela est utile si vous souhaitez sauvegarder et stocker cet élément dans une variable pour une utilisation ultérieure.

```python
# liste de langages de programmation
langages_de_programmation = ["Python", "Java", "JavaScript"]

# afficher la liste initiale
print(langages_de_programmation)


# supprimer le dernier élément, qui est "JavaScript", et le stocker dans une variable
langage_front_end = langages_de_programmation.pop()

# afficher la liste à nouveau
print(langages_de_programmation)

# afficher l'élément qui a été supprimé
print(langage_front_end)

# sortie

# ['Python', 'Java', 'JavaScript']
# ['Python', 'Java']
# JavaScript
```

### Comment utiliser la méthode `pop()` avec un paramètre optionnel <a name="avec-parametre"></a>

Pour supprimer un élément spécifique de la liste, vous devez spécifier le numéro d'index de cet élément. Plus précisément, vous passez cet index, qui représente la position de l'élément, en tant que paramètre à la méthode `pop()`.

L'indexation en Python, et dans tous les langages de programmation en général, est basée sur zéro. Le comptage commence à `0` et non à `1`.

Cela signifie que le premier élément d'une liste a un index de `0`. Le deuxième élément a un index de `1`, et ainsi de suite.

Ainsi, pour supprimer le premier élément d'une liste, vous spécifiez un index de `0` en tant que paramètre de la méthode `pop()`.

Et n'oubliez pas, `pop()` retourne l'élément qui a été supprimé. Cela vous permet de le stocker dans une variable, comme vous l'avez vu dans la section précédente.

```python
# liste de langages de programmation
langages_de_programmation = ["Python", "Java", "JavaScript"]

# supprimer le premier élément et le stocker dans une variable
langage_de_programmation = langages_de_programmation.pop(0)

# afficher la liste mise à jour
print(langages_de_programmation)

# afficher la valeur qui a été supprimée de la liste originale
print(langage_de_programmation)

# sortie

# ['Java', 'JavaScript']
# Python
```

Regardons un autre exemple :

```python
# liste de langages de programmation
langages_de_programmation = ["Python", "Java", "JavaScript"]

# supprimer "Java" de la liste
# Java est le deuxième élément de la liste, ce qui signifie qu'il a un index de 1

langages_de_programmation.pop(1)

# afficher la liste
print(langages_de_programmation)

# sortie
# ['Python', 'JavaScript']
```

Dans l'exemple ci-dessus, il y avait une valeur spécifique dans la liste que vous souhaitiez supprimer. Pour supprimer avec succès une valeur spécifique, vous devez connaître sa position.

### Aperçu des erreurs courantes qui se produisent lors de l'utilisation de la méthode `pop()` <a name="erreurs"></a>

Gardez à l'esprit que vous obtiendrez une erreur si vous essayez de supprimer un élément qui est égal ou supérieur à la longueur de la liste - spécifiquement, ce sera une `IndexError`.

Regardons l'exemple suivant qui montre comment trouver la longueur d'une liste :

```python
# liste de langages de programmation
langages_de_programmation = ["Python", "Java", "JavaScript"]

# trouver la longueur de la liste
print(len(langages_de_programmation))

# sortie
# 3
```

Pour trouver la longueur de la liste, vous utilisez la fonction `len()`, qui retourne le nombre total d'éléments contenus dans la liste.

Si j'essaie de supprimer un élément à la position 3, qui est égale à la longueur de la liste, j'obtiens une erreur disant que l'index passé est hors de portée :

```python
# liste de langages de programmation
langages_de_programmation = ["Python", "Java", "JavaScript"]

langages_de_programmation.pop(3)

# sortie

# ligne 4, dans <module>
#    langages_de_programmation.pop(3)
# IndexError: pop index out of range
```

La même exception serait levée si j'avais essayé de supprimer un élément à la position 4 ou même plus haut.

Sur une note similaire, une exception serait également levée si vous utilisiez la méthode `pop()` sur une liste vide :

```python
# liste vide
langages_de_programmation = []

# essayer d'utiliser pop() sur une liste vide
langages_de_programmation.pop()

# afficher la liste mise à jour
print(langages_de_programmation)

# sortie
# ligne 5, dans <module>
#    langages_de_programmation.pop()
# IndexError: pop from empty list
```

## Conclusion

Et voilà ! Vous savez maintenant comment supprimer un élément de liste en Python en utilisant la méthode `pop()`.

J'espère que vous avez trouvé cet article utile.

Pour en savoir plus sur le langage de programmation Python, consultez la certification [Scientific Computing with Python Certification](https://www.freecodecamp.org/learn/scientific-computing-with-python/) de freeCodeCamp.

Vous commencerez par les bases et apprendrez de manière interactive et adaptée aux débutants. Vous construirez également cinq projets à la fin pour mettre en pratique et renforcer ce que vous avez appris.

Merci d'avoir lu et bon codage !