---
title: Créer une liste en Python – Syntaxe des listes en Python
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-03-23T20:32:31.000Z'
originalURL: https://freecodecamp.org/news/create-a-list-in-python-lists-in-python-syntax
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/list.png
tags:
- name: Python
  slug: python
seo_title: Créer une liste en Python – Syntaxe des listes en Python
seo_desc: 'Lists are one of the core data structures in Python. We use them for storing
  any data type, whether it''s an integer, string, boolean, or even an object.

  Because one list can store multiple types of data, lists are one of the most powerful
  and widely ...'
---

Les listes sont l'une des structures de données fondamentales en Python. Nous les utilisons pour stocker n'importe quel type de données, qu'il s'agisse d'un entier (integer), d'une chaîne de caractères (string), d'un booléen (boolean) ou même d'un objet.

Comme une liste peut stocker plusieurs types de données, les listes sont l'un des outils les plus puissants et les plus utilisés pour stocker des données en Python.

L'une des caractéristiques notables des listes est leur mutabilité. Vous pouvez modifier une liste après l'avoir déclarée et la compléter.

Dans cet article, vous n'apprendrez pas seulement à déclarer une liste – je vous montrerai également plusieurs méthodes que vous pouvez utiliser pour manipuler les listes afin que vous puissiez vous sentir à l'aise avec elles.

## Syntaxe de base des listes en Python
Pour créer une liste en Python, déclarez un nom pour la liste et placez les données individuelles séparées par des virgules à l'intérieur de crochets :

```py
listName = [valeur1, valeur2, valeur3, valeur4]
```

N'oubliez pas que les valeurs que vous mettez dans les crochets peuvent être de n'importe quel type de données.

Il peut s'agir de chaînes de caractères :
```py
langs = ["HTML", "CSS", "Python", "JavaScript"]
```

Il peut s'agir d'entiers :
```py
intList = [1, 5, 78, 76, 9, 0]
```

Il peut s'agir d'un booléen :
```py
boolList = [True, False]
```

Il peut s'agir d'un mélange de différents types de données, y compris des nombres flottants (floats) :
```py
mixedList = [23, "JavaScript", True, 34.9, 19]
```

Vous pouvez même dupliquer les données dans une liste et tout fonctionnera toujours correctement :
```py
duplicateList = [3, "Python", "Python", "JavaScript"]
print(duplicateList) 
# Sortie : [3, 'Python', 'Python', 'JavaScript']
```

## Comment accéder aux éléments d'une liste

Pour accéder aux éléments d'une liste, vous pouvez utiliser l'opérateur d'indexation (`[]`). Les listes sont indexées à partir de zéro, nous utilisons donc 0 pour obtenir le premier élément, 1 pour le deuxième élément, et ainsi de suite.

```py
langs = ["HTML", "CSS", "Python", "JavaScript", "C++", "Java", "Elixir", "R"]
firstElement = langs[0]
secondElement = langs[1]
thirdElement = langs[2]
fourthElement = langs[3]

print(firstElement) # HTML
print(secondElement) # CSS
print(thirdElement) # Python
print(fourthElement) # JavaScript

# Obtenir le dernier élément avec l'indexation négative
lastElement = langs[-1]
print(lastElement) # R
```

## Différentes méthodes que vous pouvez utiliser pour travailler avec les listes

Vous pouvez utiliser la méthode `len()` pour obtenir la longueur de la liste :
```py
langs = ["HTML", "CSS", "Python", "JavaScript", "C++", "Java", "Elixir", "R"]
print(len(langs))
# Sortie : 8
```

Vous pouvez ajouter un élément à la liste en utilisant la méthode `append()` :
```py
langs = ["HTML", "CSS", "Python", "JavaScript", "C++", "Java", "Elixir", "R"]
langs.append("C#")
print(langs)
```

**N.B. :** Vous ne pouvez ajouter qu'un seul élément à la fois avec la méthode `append()`, et l'élément est ajouté à la fin.

Continuez votre lecture et je vous montrerai comment ajouter plusieurs éléments à la liste, et comment vous pouvez ajouter quelque chose à la position (index) souhaitée dans la liste.

Vous pouvez ajouter un élément à la position que vous souhaitez dans la liste en utilisant la méthode `insert()` :
```py
langs = ["HTML", "CSS", "Python", "JavaScript", "C++", "Java", "Elixir", "R"]
# Insérer Golang à la position 4
langs.insert(4, "Golang")

print(langs)
# Sortie : ['HTML', 'CSS', 'Python', 'JavaScript', 'Golang', 'C++', 'Java', 'Elixir', 'R']
```

N'oubliez pas que les listes sont indexées à partir de zéro, donc le comptage commence à 0 et non à 1. Golang n'a pas été inséré à la position 5, il a été inséré à la position 4.

Vous pouvez ajouter plusieurs éléments à la liste en utilisant la méthode `extend()` :
```py
langs = ["HTML", "CSS", "Python", "JavaScript", "C++", "Java", "Elixir", "R"]
langs.extend(["Golang", "F#", "COBOL"])

print(langs)
# Sortie : ['HTML', 'CSS', 'Python', 'JavaScript', 'C++', 'Java', 'Elixir', 'R', 'Golang', 'F#', 'COBOL']
```

Vous pouvez supprimer un élément de la liste en utilisant la méthode `remove()` :

```py
langs = ["HTML", "CSS", "Python", "JavaScript", "C++", "Java", "Elixir", "R"]
langs.extend(["Golang", "F#", "COBOL"])

# Supprimer HTML
langs.remove("HTML")

print(langs)
# Sortie : ['CSS', 'Python', 'JavaScript', 'C++', 'Java', 'Elixir', 'R', 'Golang', 'F#', 'COBOL']
```

Vous pouvez supprimer un élément de la fin de la liste en utilisant la méthode `pop()` :

```py
langs = ["HTML", "CSS", "Python", "JavaScript", "C++", "Java", "Elixir", "R"]
# Supprimer R
langs.pop()

print(langs)
# Sortie : ['HTML', 'CSS', 'Python', 'JavaScript', 'C++', 'Java', 'Elixir']
```

Vous pouvez également supprimer un élément d'une certaine position dans la liste en utilisant la méthode `pop()` :
```py
langs = ["HTML", "CSS", "Python", "JavaScript", "C++", "Java", "Elixir", "R"]
# Supprime JavaScript
langs.pop(3)

print(langs)
# Sortie : ['HTML', 'CSS', 'Python', 'C++', 'Java', 'Elixir', 'R']
```

Si la liste ne contient que des nombres, vous pouvez utiliser la méthode `min()` pour obtenir le plus petit nombre :
```py
listOfNumbers = [3, 89, 8, 100, 2, 4, 1]
smallestNum = min(listOfNumbers)

print(smallestNum) # Sortie : 1

```

Si la liste ne contient que des nombres, vous pouvez utiliser la méthode `max()` pour obtenir le plus grand nombre :
```py
listOfNumbers = [3, 89, 8, 100, 2, 4, 1]
largestNum = max(listOfNumbers)

print(largestNum) # Sortie : 100
```

## Conclusion

Dans cet article, vous avez découvert les listes en Python, comment les indexer et plusieurs méthodes que vous pouvez utiliser pour accomplir des tâches avec elles.

Les listes sont une structure de données puissante avec laquelle vous devriez vous familiariser car elles sont très dynamiques et peuvent vous aider à accomplir des tâches de multiples façons.

Si vous trouvez cet article utile, n'hésitez pas à le partager avec vos amis et votre famille.