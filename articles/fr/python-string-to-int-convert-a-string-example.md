---
title: Python String to Int – Exemple de conversion d'une chaîne
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-03-17T23:53:39.000Z'
originalURL: https://freecodecamp.org/news/python-string-to-int-convert-a-string-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/integer.jpg
tags:
- name: Python
  slug: python
seo_title: Python String to Int – Exemple de conversion d'une chaîne
seo_desc: "When creating a program, you may need to get numerical input from users\
  \ and perform various mathematical operations on the value. \nSimilarly, there are\
  \ cases where you might want to perform mathematical operations on string values.\
  \ \nIn both cases, th..."
---

Lors de la création d'un programme, vous pourriez avoir besoin de récupérer une saisie numérique de la part des utilisateurs et d'effectuer diverses opérations mathématiques sur cette valeur. 

De même, il existe des cas où vous souhaiteriez effectuer des opérations mathématiques sur des valeurs de type chaîne de caractères (string). 

Dans les deux cas, les valeurs renvoyées sont des chaînes de caractères, nous ne pouvons donc pas effectuer d'opérations mathématiques avec elles, car cela générerait une erreur.

Dans cet article, nous verrons comment convertir une chaîne de caractères en un entier en Python à l'aide de quelques exemples.

## Comment convertir une chaîne en entier en Python

En Python, nous pouvons utiliser la fonction intégrée `int()` pour convertir des chaînes en entiers. Voici à quoi ressemble la syntaxe : 

```
int(string_value)
```

Nous passons donc la chaîne à convertir en tant qu'argument dans la fonction `int()`. C'est tout !

Voici un exemple pour vous aider à comprendre :

```python
userAge = "10"

print(userAge + 8)

# TypeError: peut uniquement concaténer str (pas "int") à str
```

Dans l'exemple ci-dessus, nous ajoutons 8 à la variable `userAge` qui est une chaîne – mais cela affiche une erreur car l'interpréteur suppose que nous essayons d'ajouter (concaténer) deux chaînes. 

Convertissons maintenant la variable en un entier et effectuons la même opération :

```python
userAge = "10"

convertUserAge = int(userAge)

print(convertUserAge + 8)

# 18
```

Nous avons converti la variable `userAge` et l'avons stockée dans une variable appelée `convertUserAge`, puis nous avons de nouveau effectué notre opération pour obtenir le résultat attendu. 

Dans l'exemple suivant, similaire au précédent, nous allons récupérer la saisie d'un utilisateur et effectuer quelques calculs pour afficher son âge.

```python
from datetime import date

currentDate = date.today()
currentYear = currentDate.year

userBirthYear = input("Quelle est votre année de naissance ?")

convertUserBirthYear = int(userBirthYear)

userAge = currentYear - convertUserBirthYear

print(userAge)

```

Dans le code ci-dessus, nous avons d'abord importé la classe `date` du module `datetime`. Grâce à cela, nous avons pu obtenir et stocker l'année en cours dans une variable. 

Nous avons ensuite demandé l'année de naissance de l'utilisateur : `userBirthYear = input("Quelle est votre année de naissance ?")` 

Après cela, nous avons converti l'année de naissance de l'utilisateur (qui nous a été renvoyée sous forme de chaîne) en un entier à l'aide de la fonction `int()`. Avec la valeur entière, nous avons pu soustraire l'année de naissance de l'utilisateur de l'année en cours pour obtenir et afficher son âge réel.

Vous pouvez copier le code et faire des tests.

## Conclusion

Dans cet article, nous avons appris comment convertir des chaînes de caractères en entiers en Python. Nous avons d'abord vu un exemple où nous avons dû utiliser la fonction `int()` pour convertir une chaîne en entier et effectuer une opération simple avec la valeur.

Dans le second exemple, nous avons récupéré une saisie d'un utilisateur, l'avons convertie en entier, puis avons effectué notre opération mathématique pour afficher son âge actuel.

Merci de votre lecture et bon codage !