---
title: Python Datetime.now() – Comment obtenir la date et l'heure d'aujourd'hui
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-09-20T20:12:09.000Z'
originalURL: https://freecodecamp.org/news/python-datetime-now-how-to-get-todays-date-and-time
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/kevin-ku-aiyBwbrWWlo-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: Python Datetime.now() – Comment obtenir la date et l'heure d'aujourd'hui
seo_desc: "You can use the datetime module in Python to retrieve data about date and\
  \ time. \nIn this article, you'll learn how to use the datetime object from the\
  \ datetime module to get the current date and time properties.\nYou'll also learn\
  \ how to get the date ..."
---

Vous pouvez utiliser le module `datetime` en Python pour récupérer des données sur la date et l'heure. 

Dans cet article, vous apprendrez à utiliser l'objet `datetime` du module `datetime` pour obtenir les propriétés de la date et de l'heure actuelles.

Vous apprendrez également à obtenir la date et l'heure de différents endroits dans le monde en utilisant la fonction `datetime.now()` et le module `pytz`. 

## Comment utiliser l'objet `datetime` en Python

Pour utiliser l'objet `datetime`, vous devez d'abord l'importer. Voici comment faire :

```python
from datetime import datetime
```

Dans l'exemple suivant, vous verrez comment utiliser l'objet `datetime`. 

```python
from datetime import datetime

current_dateTime = datetime.now()

print(current_dateTime)
# 2022-09-20 10:27:21.240752
```

Dans le code ci-dessus, nous avons assigné le `datetime` à une variable appelée `current_dateTime`. 

Lorsque nous l'avons imprimé dans la console, nous avons obtenu l'année, le mois, le jour et l'heure actuels : `2022-09-19 17:44:17.858167`.

Notez que nous sommes en mesure d'accéder aux informations ci-dessus en utilisant la méthode `now()` : `datetime.now()`.

## Comment utiliser les attributs de `datetime.now()`

Dans la section précédente, nous avons récupéré des informations sur la date et l'heure actuelles, qui incluaient l'année, le mois, le jour et l'heure à ce moment-là. 

Mais la fonction `datetime.now()` nous fournit des attributs supplémentaires pour extraire des données individuelles. 

Par exemple, pour obtenir uniquement l'année actuelle, vous feriez quelque chose comme ceci :

```python
from datetime import datetime

current_dateTime = datetime.now()

print(current_dateTime.year)
# 2022
```

Dans l'exemple ci-dessus, nous avons assigné la fonction `datetime.now()` à une variable appelée `current_dateTime`. 

En utilisant la notation par points, nous avons attaché l'attribut `year` à la variable déclarée ci-dessus : `current_dateTime.year`. Lorsque nous l'avons imprimé dans la console, nous avons obtenu 2022. 

La fonction `datetime.now()` possède les attributs suivants :

* `year`
* `month`
* `day`
* `hour`
* `minute`
* `second`
* `microsecond`

Voici un exemple des attributs listés ci-dessus en utilisation :

```python
from datetime import datetime

current_dateTime = datetime.now()

print(current_dateTime.year) # 2022

print(current_dateTime.month) # 9

print(current_dateTime.day) # 20

print(current_dateTime.hour) # 11

print(current_dateTime.minute) # 27

print(current_dateTime.second) # 46

print(current_dateTime.microsecond) # 582035
```

## Comment obtenir un fuseau horaire particulier en Python en utilisant `datetime.now()` et `pytz`

Pour obtenir des informations sur différents fuseaux horaires à travers le monde en Python, vous pouvez utiliser la fonction `datetime.now()` et le module `pytz`. 

Voici un exemple qui montre comment obtenir la date et l'heure actuelles à Lagos, au Nigeria : 

```python
from datetime import datetime
import pytz

datetime_in_Lagos = datetime.now(pytz.timezone('Africa/Lagos'))

print(datetime_in_Lagos)
# 2022-09-20 12:53:27.225570+01:00
```

Dans le code ci-dessus, nous avons d'abord importé les modules :

```python
from datetime import datetime
import pytz

```

Ensuite, nous avons passé l'objet `pytz` en tant que paramètre à la fonction `datetime.now()` :

```python
datetime_in_Lagos = datetime.now(pytz.timezone('Africa/Lagos'))
```

L'objet `pytz` possède un attribut `timezone` qui prend des informations/paramètres du fuseau horaire spécifique que vous recherchez : `pytz.timezone('Africa/Lagos')`. 

Avec l'attribut `all_timezones`, vous pouvez obtenir une liste de tous les fuseaux horaires possibles dans la bibliothèque `pytz` qui peuvent être passés en tant que paramètres à l'attribut `timezone` - comme nous l'avons fait dans le dernier exemple. C'est-à-dire :

```python
from datetime import datetime
import pytz

all_timezones = pytz.all_timezones

print(all_timezones)
# [Liste de tous les fuseaux horaires...]
```

## Résumé

Dans cet article, nous avons parlé de l'obtention de la date et de l'heure d'aujourd'hui en utilisant la fonction `datetime.now()` en Python. 

Nous avons vu des exemples qui montraient comment utiliser la fonction `datetime.now()` et ses attributs.

Enfin, nous avons vu comment obtenir la date et l'heure dans des endroits spécifiques à travers le monde en utilisant la fonction `datetime.now()` et le module `pytz`. 

Bon codage !