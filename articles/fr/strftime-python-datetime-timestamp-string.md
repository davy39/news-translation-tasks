---
title: strftime – Chaîne de caractères de date et d'heure en Python
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-04-19T01:15:23.000Z'
originalURL: https://freecodecamp.org/news/strftime-python-datetime-timestamp-string
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/brooke-lark-BRBjShcA8D4-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: strftime – Chaîne de caractères de date et d'heure en Python
seo_desc: 'The datetime object lets us work with dates and times in Python. But the
  value returned when we use this object is of the datatime data type rather than
  a string.

  Here is an example that prints the current year, month, day and time to the console:

  fr...'
---

L'objet `datetime` nous permet de travailler avec des dates et des heures en Python. Mais la valeur retournée lorsque nous utilisons cet objet est du type `datetime` plutôt qu'une `string`.

Voici un exemple qui affiche l'année, le mois, le jour et l'heure actuels dans la console :

```python
from datetime import datetime

current_day = datetime.now() 

print(current_day)
# 2022-04-18 21:50:24.524022

print(type(current_day))
# <class 'datetime.datetime'>
```

Dans le code ci-dessus, nous avons d'abord importé l'objet `datetime`. `datetime.now()` nous donne toutes les informations sur le jour actuel, que nous avons stockées dans une variable appelée `current_day`.

Lorsque nous avons imprimé `current_day`, nous avons obtenu ceci : `2022-04-18 21:50:24.524022`. Cela nous montre l'année, le mois, le jour et l'heure. Et lorsque nous avons imprimé le type dans la console, nous avons obtenu `datetime`.

Dans cet article, nous allons parler de la méthode `strftime()` fournie par l'objet `datetime`. Cette méthode nous permet de convertir les objets de date et d'heure en Python en leur format `string`.

## Que fait `strftime` en Python ?

La méthode `strftime()` prend un argument (un code de format) qui spécifie ce que nous voulons retourner.

Voici un exemple :

```python
from datetime import datetime

current_day = datetime.now()

year = current_day.strftime("%Y")

print("current year:", year)
# current year: 2022

print(type(year))
# <class 'str'>
```

Le code ci-dessus est similaire au dernier exemple, sauf que nous avons créé une nouvelle variable appelée `year`. Dans cette variable, nous avons attaché la méthode `strftime()` à l'année actuelle : `current_day.strftime("%Y")`.

Vous remarquerez que nous avons passé un argument à la méthode – "%Y" – qui désigne l'année. Cela s'appelle un code de format. Dans le prochain exemple, nous verrons d'autres codes de format.

Après avoir utilisé la méthode `strftime()`, le type de données peut maintenant être vu comme une `string`.

Voici un autre exemple :

```python
from datetime import datetime

current_day = datetime.now()

year = current_day.strftime("%Y")
print("current year:", year)
# current year: 2022

month = current_day.strftime("%B")
print("current month:", month)
# current month: April

day = current_day.strftime("%A")
print("current day:", day)
# current day: Monday

time = current_day.strftime("%-I %p")
print("current time:", time)
# current time: 9 PM
```

Dans l'exemple ci-dessus, nous avons passé différents codes de format dans la méthode `strftime()` pour retourner des valeurs `string` pour les variables `month`, `day` et `time`.

Ce ne sont pas les seuls codes de format qui existent. Cliquez [ici](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes) pour voir plus de codes de format avec lesquels vous pouvez jouer pour voir ce qu'ils font.

## Conclusion

Dans cet article, nous avons parlé de la méthode `strftime()` qui nous aide à convertir les objets de date et d'heure en `strings`.

Nous avons vu divers codes de format qui peuvent être passés en arguments pour retourner différentes valeurs d'objets de date et d'heure.

Bonne programmation !