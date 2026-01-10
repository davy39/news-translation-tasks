---
title: Python Retourner Plusieurs Valeurs – Comment Retourner un Tuple, une Liste
  ou un Dictionnaire
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-20T22:17:45.000Z'
originalURL: https://freecodecamp.org/news/python-returns-multiple-values-how-to-return-a-tuple-list-dictionary
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/image1.jpeg
tags:
- name: data structures
  slug: data-structures
- name: Python
  slug: python
seo_title: Python Retourner Plusieurs Valeurs – Comment Retourner un Tuple, une Liste
  ou un Dictionnaire
seo_desc: "By Amy Haddad\nYou can return multiple values from a function in Python.\n\
  To do so, return a data structure that contains multiple values, like a list containing\
  \ the number of miles to run each week.\ndef miles_to_run(minimum_miles):\n   week_1\
  \ = minimum..."
---

Par Amy Haddad

Vous pouvez retourner plusieurs valeurs depuis une fonction en Python.

Pour ce faire, retournez une structure de données qui contient plusieurs valeurs, comme une liste contenant le nombre de miles à courir chaque semaine.

```python
def miles_to_run(minimum_miles):
   week_1 = minimum_miles + 2
   week_2 = minimum_miles + 4
   week_3 = minimum_miles + 6
   return [week_1, week_2, week_3]
 
print(miles_to_run(2))
# résultat: [4, 6, 8]
```

Les structures de données en Python sont utilisées pour stocker des collections de données, qui peuvent être retournées depuis des fonctions. Dans cet article, nous explorerons comment retourner plusieurs valeurs depuis ces structures de données : les tuples, les listes et les dictionnaires.

## Tuples

Un tuple est une séquence ordonnée et immuable. Cela signifie qu'un tuple ne peut pas changer.

Utilisez un tuple, par exemple, pour stocker des informations sur une personne : son nom, son âge et son lieu de résidence.

```python
nancy = ("nancy", 55, "chicago")
```

Voici comment vous écriviez une fonction qui retourne un tuple.

```python
def person():
   return "bob", 32, "boston"
 
print(person())
# résultat: ('bob', 32, 'boston')
```

Remarquez que nous n'avons pas utilisé de parenthèses dans l'instruction return. Cela est dû au fait que vous pouvez retourner un tuple en séparant chaque élément par une virgule, comme montré dans l'exemple ci-dessus.

« C'est en fait la virgule qui fait un tuple, pas les parenthèses », comme le souligne la [documentation](https://docs.python.org/3/library/stdtypes.html#tuple). Cependant, les [parenthèses sont requises](https://docs.python.org/3/library/stdtypes.html#tuple) avec les tuples vides ou pour éviter la confusion.

Voici un exemple de fonction qui utilise des parenthèses `()` pour retourner un tuple.

```python
def person(name, age):
   return (name, age)
print(person("henry", 5))
# résultat: ('henry', 5)
```

## Liste

Une liste est une séquence ordonnée et mutable. Cela signifie qu'une liste peut changer.

Vous pouvez utiliser une liste pour stocker des villes :

```python
cities = ["Boston", "Chicago", "Jacksonville"]
```

Ou des scores de test :

```python
test_scores = [55, 99, 100, 68, 85, 78]
```

Jetez un coup d'œil à la fonction ci-dessous. Elle retourne une liste qui contient dix nombres.

```python
def ten_numbers():
   numbers = []
   for i in range(1, 11):
       numbers.append(i)
   return numbers
 
print(ten_numbers())
# résultat: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

Voici un autre exemple. Cette fois, nous passons plusieurs arguments lorsque nous appelons la fonction.

```python
def miles_ran(week_1, week_2, week_3, week_4):
   return [week_1, week_2, week_3, week_4]
 
monthly_mileage = miles_ran(25, 30, 28, 40)
print(monthly_mileage)
# résultat: [25, 30, 28, 40]
```

Il est facile de confondre les tuples et les listes. Après tout, les deux sont des conteneurs qui stockent des objets. Cependant, souvenez-vous de ces différences clés :

* Les tuples ne peuvent pas changer.
* Les listes peuvent changer.

## Dictionnaires

Un dictionnaire contient des paires clé-valeur enveloppées dans des accolades `{}`. Chaque « clé » a une « valeur » associée.

Considérez le dictionnaire des employés ci-dessous. Chaque nom d'employé est une « clé » et leur poste est la « valeur ».

```python
employees = {
   "jack": "engineer",
   "mary": "manager",
   "henry": "writer",
}
```

Voici comment vous écriviez une fonction qui retourne un dictionnaire avec une paire clé-valeur.

```python
def city_country(city, country):
   location = {}
   location[city] = country
   return location
 
favorite_location = city_country("Boston", "United States")
print(favorite_location)
# résultat: {'Boston': 'United States'}
```

Dans l'exemple ci-dessus, « Boston » est la **clé** et « United States » est la **valeur**.

Nous avons couvert beaucoup de terrain. Le point clé est le suivant : vous pouvez retourner plusieurs valeurs depuis une fonction Python, et il existe plusieurs façons de le faire.

_Je parle des compétences en programmation que vous devez développer et des concepts que vous devez apprendre, ainsi que des meilleures façons de les apprendre sur [amymhaddad.com](https://amymhaddad.com/)._