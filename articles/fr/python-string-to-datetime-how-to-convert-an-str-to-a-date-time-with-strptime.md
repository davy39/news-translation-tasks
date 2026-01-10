---
title: Python String to Datetime – Comment convertir une chaîne en date et heure avec
  Strptime
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2023-02-02T15:57:55.000Z'
originalURL: https://freecodecamp.org/news/python-string-to-datetime-how-to-convert-an-str-to-a-date-time-with-strptime
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/pexels-marko-klaric-6408282.jpg
tags:
- name: Python
  slug: python
seo_title: Python String to Datetime – Comment convertir une chaîne en date et heure
  avec Strptime
seo_desc: 'Python offers a variety of built-in modules that you can include in your
  program.

  A module is a Python file containing the necessary code to execute an individual
  functionality. This file is imported into your application to help you perform a
  specif...'
---

Python offre une variété de modules intégrés que vous pouvez inclure dans votre programme.

Un module est un fichier Python contenant le code nécessaire pour exécuter une fonctionnalité individuelle. Ce fichier est importé dans votre application pour vous aider à effectuer une tâche spécifique.

L'un de ces modules est le module `datetime` pour travailler avec et manipuler les heures et les dates.

Le module `datetime` inclut la classe `datetime`, qui fournit à son tour la méthode de classe `strptime()`. La méthode `strptime()` crée un objet datetime à partir d'une représentation sous forme de chaîne d'une date et d'une heure correspondantes.

Dans cet article, vous apprendrez à utiliser la méthode `datetime.strptime()` pour convertir des chaînes en objets datetime.

Commençons !

## Qu'est-ce que la méthode `datetime.strptime()` en Python ? Une analyse de la syntaxe `datetime.strptime()`

La syntaxe générale de la méthode `datetime.strptime()` ressemble à ceci :

```
datetime.strptime(date_string, format_code)
```

Analysons cela.

Tout d'abord, `datetime` est le nom de la classe.

Ensuite, `strptime()` est le nom de la méthode. La méthode accepte deux arguments de chaîne *requis*.

* Le premier argument requis est `date_string` – la représentation sous forme de chaîne de la date que vous souhaitez convertir en un objet datetime.
* Le second argument requis est `format_code` – un format spécifique pour vous aider à convertir la chaîne en un objet datetime.

Voici une liste des formats de code les plus couramment utilisés que vous pourriez rencontrer :

- `%d` - le jour du mois sous forme de nombre décimal avec zéro initial, comme `28`.
- `%a` - le nom abrégé d'un jour, comme `Sun`.
- `%A` - le nom complet d'un jour, comme `Sunday`.
- `%m` - le mois sous forme de nombre décimal avec zéro initial, comme `01`.
- `%b` - le nom abrégé du mois, comme `Jan`.
- `%B` - le nom complet du mois, comme `January`.
- `%y` - l'année sans siècle, comme `23`.
- `%Y` - l'année avec siècle, comme `2023`.
- `%H` - les heures du jour au format 24 heures, comme `08`.
- `%I` - les heures du jour au format 12 heures.
- `%M` - les minutes dans une heure, comme `20`.
- `%S` - les secondes dans une minute, comme `00`.

Pour voir un tableau qui montre tous les codes de format pour `datetime.strptime()`, consultez la [documentation Python](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes).

## Comment utiliser la méthode `datetime.strptime()` en Python ? Comment convertir une chaîne en un objet Datetime en Python

Supposons que j'ai la chaîne suivante qui représente une date et une heure :

```
28/01/23  08:20:00
```

Et je veux obtenir le résultat suivant :

```
2023-01-28 08:20:00
```

Comment pourrais-je y parvenir ?

Examinons le code ci-dessous :

```python
# importer la classe datetime du module datetime
from datetime import datetime

date_time_str = "28/01/23  08:20:00"

# vérifier le type de données de date_time_str
print(type(date_time_str))

# sortie

# <class 'str'>
```

Tout d'abord, j'importe le module `datetime` avec l'instruction `from datetime import datetime`.

Ensuite, je stocke la chaîne que je veux convertir en un objet datetime dans une variable nommée `date_time_str` et vérifie son type en utilisant la fonction `type()`. La sortie indique qu'il s'agit d'une chaîne.

Maintenant, convertissons la chaîne en un objet datetime en utilisant la méthode `strptime()` de la classe `datetime` et vérifions le type de données :

```python
from datetime import datetime

date_time_str = "28/01/23  08:20:00"

date_time_object = datetime.strptime(date_time_str, "%d/%m/%y %H:%M:%S")

print(date_time_object)

# vérifier le type de date_time_object
print(type(date_time_object))

# sortie

# 2023-01-28 08:20:00
# <class 'datetime.datetime'>
```

Les codes de format pour la chaîne `28/01/23  08:20:00` sont `%d/%m/%y %H:%M:%S`.

Les codes de format `%d,%m,%y,%H,%M,%S` représentent respectivement le jour du mois, le mois sous forme de nombre décimal avec zéro initial, l'année sans siècle, l'heure du jour, les minutes du jour et les secondes du jour.

Maintenant, changeons un peu la chaîne initiale.

Changeons-la de `28/01/23` à `28 January 2023` et vérifions le type de données de `date_time_str` :

```python
from datetime import datetime

date_time_str = "28 January 2023 08:20:00"

# vérifier le type de données
print(type(date_time_str))

# sortie

# <class 'str'>
```

Maintenant, convertissons `date_time_str` en un objet datetime – gardez à l'esprit que puisque la chaîne est différente, vous devez également changer les codes de format :

```python
from datetime import datetime

date_time_str = "28 January 2023 08:20:00"

date_object = datetime.strptime(date_time_str, "%d %B %Y %H:%M:%S")

print(date_object)

# vérifier le type de données
print(type(date_object))

# sortie

# 2023-01-28 08:20:00
# <class 'datetime.datetime'>
```

Les codes de format pour la chaîne `28 January 2023 08:20:00` sont `%d %B %Y %H:%M:%S`.

Parce que j'ai changé le mois de janvier de sa représentation sous forme de nombre décimal avec zéro initial, `01`, à son nom complet, `January`, j'ai également dû changer son code de format – de `%m` à `%B`.

## Comment convertir une chaîne en un objet `datetime.date()` en Python

Et si vous ne voulez convertir que la date mais pas l'heure à partir d'une chaîne ?

Vous pouvez vouloir convertir uniquement la partie `28/01/23` de la chaîne `28/01/23  08:20:00` en un objet.

Pour convertir une chaîne en un objet date, vous utiliserez la méthode `strptime()` comme vous l'avez vu dans la section précédente, mais vous utiliserez également la méthode `datetime.date()` pour extraire uniquement la date.

```python
from datetime import datetime

date_time_str = "28 January 2023 08:20:00"

date_object = datetime.strptime(date_time_str, "%d %B %Y %H:%M:%S").date()

print(date_object)

# vérifier le type de données
print(type(date_object))

# sortie

# 2023-01-28
# <class 'datetime.date'>
```

## Comment convertir une chaîne en un objet `datetime.time()` en Python

Et pour convertir uniquement la partie heure, `08:20:00` de la chaîne `28/01/23  08:20:00`, vous utiliseriez la méthode `datetime.time()` pour extraire uniquement l'heure :

```python
from datetime import datetime

date_time_str = "28 January 2023 08:20:00"

date_object = datetime.strptime(date_time_str, "%d %B %Y %H:%M:%S").time()

print(date_object)
print(type(date_object))

# sortie

# 08:20:00
# <class 'datetime.time'>
```

## Pourquoi une `ValueError` est-elle levée lors de l'utilisation de `datetime.strptime()` en Python ?

Une chose à garder à l'esprit est que la chaîne que vous passez en argument à la méthode `strptime()` doit avoir un format spécifique – toutes les chaînes ne sont pas converties en un objet datetime.

Plus précisément, l'année, le mois et le jour dans la chaîne doivent correspondre au code de format.

Par exemple, le code de format pour le mois dans la chaîne `28/01/23` doit être `%m`, qui représente le mois sous forme de nombre décimal avec zéro initial.

Que se passe-t-il si j'utilise le code de format `%B` à la place ?

```python
from datetime import datetime

date_time_str = "28/01/23  08:20:00"

date_time_object = datetime.strptime(date_time_str, "%d/%B/%y %H:%M:%S")

print(date_time_object)

# sortie

# raise ValueError("time data %r does not match format %r" %
# ValueError: time data '28/01/23  08:20:00' does not match format '%d/%B/%y # %H:%M:%S'
```

J'obtiens une `ValueError` !

Le code de format `%B` représente le nom complet du mois, comme `January`, et non `01`.

Ainsi, si la chaîne passée à `strptime()` ne correspond pas au format spécifié, une `ValueError` est levée.

Pour gérer cela, vous pouvez tester et gérer l'erreur en utilisant un bloc `try-except`, comme ceci :

```python
from datetime import datetime

date_time_str = "28/01/23  08:20:00"

try:
  date_time_object = datetime.strptime(date_time_str, "%d/%B/%y %H:%M:%S")
except ValueError as error:
  print('Une ValueError est levée car :', error)
  
# sortie

# Une ValueError est levée car : time data '28/01/23  08:20:00' does not # match format '%d/%B/%y %H:%M:%S'
```

## Conclusion

Espérons que cet article vous a aidé à comprendre comment convertir une chaîne en un objet datetime en Python en utilisant la méthode `strptime()`.

Merci d'avoir lu, et bon codage !