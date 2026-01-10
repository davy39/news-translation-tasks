---
title: Longueur d'une liste Python – Comment obtenir la taille d'une liste en Python
date: '2022-03-03T18:21:33.000Z'
author: Kolade Chris
authorURL: https://www.freecodecamp.org/news/author/koladechris/
originalURL: https://freecodecamp.org/news/python-list-length-how-to-get-the-size-of-a-list-in-python
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/calendar-g2ed8847ef_1280.jpg
tags:
- name: Python
  slug: python
seo_desc: 'In Python, you use a list to store various types of data such as strings
  and numbers.

  A list is identifiable by the square brackets that surround it, and individual values
  are separated by a comma.

  To get the length of a list in Python, you can use t...'
---


En Python, on utilise une liste pour stocker divers types de données tels que des chaînes de caractères et des nombres.

<!-- more -->

Une liste est identifiable par les crochets qui l'entourent, et les valeurs individuelles sont séparées par une virgule.

Pour obtenir la longueur d'une liste en Python, vous pouvez utiliser la fonction intégrée `len()`.

En plus de la fonction `len()`, vous pouvez également utiliser une boucle for et la fonction `length_hint()` pour obtenir la longueur d'une liste.

Dans cet article, je vais vous montrer comment obtenir la longueur d'une liste de 3 manières différentes.

## Comment obtenir la longueur d'une liste en Python avec une boucle For

Vous pouvez utiliser la boucle for native de Python pour obtenir la longueur d'une liste car, tout comme un tuple et un dictionnaire, une liste est un itérable.

Cette méthode est couramment appelée la méthode naïve.

L'exemple ci-dessous vous montre comment utiliser la méthode naïve pour obtenir la longueur d'une liste en Python :

```
demoList = ["Python", 1, "JavaScript", True, "HTML", "CSS", 22]

# Initializing counter variable
counter = 0

for item in demoList:
    # Incrementing counter variable to get each item in the list
    counter = counter + 1

    # Printing the result to the console by converting counter to string in order to get the number
print("The length of the list using the naive method is: " + str(counter))
# Output: The length of the list using the naive method is: 7
```

## Comment obtenir la longueur d'une liste avec la fonction len()

L'utilisation de la fonction `len()` est le moyen le plus courant d'obtenir la longueur d'un itérable.

C'est plus direct que d'utiliser une boucle for.

La syntaxe pour utiliser la méthode `len()` est `len(listName)`.

L'extrait de code ci-dessous montre comment utiliser la fonction `len()` pour obtenir la longueur d'une liste :

```
demoList = ["Python", 1, "JavaScript", True, "HTML", "CSS", 22]

sizeOfDemoList = len(demoList)

print("The length of the list using the len() method is: " + str(sizeOfDemoList))
# Output: The length of the list using the len() method is: 7
```

## Comment obtenir la longueur d'une liste avec la fonction length_hint()

La méthode `length_hint()` est un moyen moins connu d'obtenir la longueur d'une liste et d'autres itérables.

`length_hint()` est définie dans le module operator, vous devez donc l'importer de là avant de pouvoir l'utiliser.

La syntaxe pour utiliser la méthode `length_hint()` est `length_hint(listName)`.

L'exemple ci-dessous vous montre comment utiliser la méthode `length_hint()` pour obtenir la longueur d'une liste :

```
from operator import length_hint:
demoList = ["Python", 1, "JavaScript", True, "HTML", "CSS", 22]

sizeOfDemoList = length_hint(demoList)
print("The length of the list using the length_hint() method is: " + str(sizeOfDemoList))
# The length of the list using the length_hint() method is: 7
```

## Dernières réflexions

Cet article vous a montré comment obtenir la taille d'une liste avec 3 méthodes différentes : une boucle for, la fonction `len()`, et la fonction `length_hint()` du module operator.

Vous vous demandez peut-être laquelle de ces 3 méthodes utiliser.

Je vous conseillerais d'utiliser `len()` car elle ne nécessite pas beaucoup d'efforts par rapport à la boucle for et à `length_hint()`.

De plus, `len()` semble être plus rapide que la boucle for et `length_hint()`.

Si vous trouvez cet article utile, partagez-le afin qu'il puisse aider d'autres personnes.