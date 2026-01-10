---
title: Comment obtenir l'heure actuelle en Python avec Datetime
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-03-21T13:52:01.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-the-current-time-in-python-with-datetime
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/datetime.png
tags:
- name: Python
  slug: python
seo_title: Comment obtenir l'heure actuelle en Python avec Datetime
seo_desc: 'In your Python applications, you might want to work with time to add functionalities
  like timestamps, check the time of a user’s activity, and more.

  One of the modules that helps you work with date and time in Python is datetime.

  With the datetime mo...'
---

Dans vos applications Python, vous pourriez avoir besoin de travailler avec le temps pour ajouter des fonctionnalités telles que des horodatages, vérifier l'heure de l'activité d'un utilisateur, et bien plus encore.

L'un des modules qui vous aide à travailler avec la date et l'heure en Python est `datetime`.

Avec le module `datetime`, vous pouvez obtenir la date et l'heure actuelles, ou la date et l'heure actuelles dans un fuseau horaire particulier.

Dans cet article, je vais vous montrer comment obtenir l'heure actuelle en Python avec le module `datetime`. Je vous montrerai également comment obtenir l'heure actuelle dans n'importe quel fuseau horaire du monde.

## Table des matières
- [Comment obtenir l'heure actuelle avec le module `datetime`](#heading-comment-obtenir-lheure-actuelle-avec-le-module-datetime)
- [Attributs de la fonction `datetime.now()`](#heading-attributs-de-la-fonction-datetimenow)
- [Comment obtenir l'heure actuelle d'un fuseau horaire avec `datetime`](#heading-comment-obtenir-lheure-actuelle-dun-fuseau-horaire-avec-datetime)
- [Conclusion](#heading-conclusion)

## Comment obtenir l'heure actuelle avec le module `datetime`

La première chose à faire est d'importer le module `datetime` comme ceci :

```py
from datetime import datetime
```

La chose suivante que vous pouvez faire pour obtenir rapidement la date et l'heure actuelles est d'utiliser la fonction `datetime.now()` du module `datetime` :

```py
from datetime import datetime
currentDateAndTime = datetime.now()

print("La date et l'heure actuelles sont", currentDateAndTime)
# Résultat : La date et l'heure actuelles sont 2022-03-19 10:05:39.482383
```

Pour obtenir l'heure actuelle en particulier, vous pouvez utiliser la méthode `strftime()` et lui passer la chaîne `”%H:%M:%S”` représentant les heures, les minutes et les secondes.

Cela vous donnerait l'heure actuelle au format 24 heures :
```py
from datetime import datetime
currentDateAndTime = datetime.now()

print("La date et l'heure actuelles sont", currentDateAndTime)
# Résultat : La date et l'heure actuelles sont 2022-03-19 10:05:39.482383

currentTime = currentDateAndTime.strftime("%H:%M:%S")
print("L'heure actuelle est", currentTime)
# L'heure actuelle est 10:06:55
```

## Attributs de la fonction `datetime.now()`

La fonction `datetime.now` possède plusieurs attributs avec lesquels vous pouvez obtenir l'année, le mois, la semaine, le jour, l'heure, la minute et la seconde de la date actuelle.

L'extrait de code ci-dessous affiche toutes les valeurs des attributs dans le terminal :
```py
from datetime import datetime
currentDateAndTime = datetime.now()

print("L'année actuelle est ", currentDateAndTime.year) # Résultat : L'année actuelle est 2022
print("Le mois actuel est ", currentDateAndTime.month) # Résultat : Le mois actuel est 3 
print("Le jour actuel est ", currentDateAndTime.day) # Résultat : Le jour actuel est 19
print("L'heure actuelle est ", currentDateAndTime.hour) # Résultat : L'heure actuelle est 10 
print("La minute actuelle est ", currentDateAndTime.minute) # Résultat : La minute actuelle est 49
print("La seconde actuelle est ", currentDateAndTime.second) # Résultat : La seconde actuelle est 18

``` 
## Comment obtenir l'heure actuelle d'un fuseau horaire avec `datetime`

Vous pouvez obtenir l'heure actuelle dans un fuseau horaire particulier en utilisant le module `datetime` avec un autre module appelé `pytz`.

Vous pouvez installer le module `pytz` via pip comme ceci :
`pip install pytz`

La première chose à faire est d'importer les modules `datetime` et `pytz` :
```py
from datetime import datetime
import pytz
```

Vous pouvez ensuite vérifier tous les fuseaux horaires disponibles avec l'extrait ci-dessous :
```py
from datetime import datetime
import pytz

zones = pytz.all_timezones

print(zones) 
# Résultat : tous les fuseaux horaires du monde. Impressionnant !
```

Dans l'extrait de code ci-dessous, j'ai pu obtenir l'heure à New York :
```py
from datetime import datetime
import pytz

newYorkTz = pytz.timezone("America/New_York") 
timeInNewYork = datetime.now(newYorkTz)
currentTimeInNewYork = timeInNewYork.strftime("%H:%M:%S")

print("L'heure actuelle à New York est :", currentTimeInNewYork)
# Résultat : L'heure actuelle à New York est : 05:36:59
```
Comment ai-je pu obtenir l'heure actuelle à New York ?
- J'ai utilisé la méthode `pytztimezone()` du module `pytz`, je lui ai passé le fuseau horaire exact de New York sous forme de chaîne de caractères, et je l'ai assignée à une variable nommée `newYorkTz` (pour le fuseau horaire de New York)
- Pour obtenir l'heure actuelle à New York, j'ai utilisé la fonction `datetime.now()` du module `datetime` et je lui ai passé la variable que j'ai créée pour stocker le fuseau horaire de New York
- Pour enfin obtenir l'heure actuelle à New York au format 24 heures, j'ai utilisé la méthode `strftime()` sur la variable `timeInNewYork` et je l'ai stockée dans une variable nommée `currentTimeInNewYork`, afin de pouvoir l'afficher dans le terminal

## Conclusion

Comme le montre cet article, le module `datetime` est très pratique pour travailler avec l'heure et les dates, et par conséquent pour obtenir l'heure actuelle dans votre région.

Lorsqu'il est combiné avec le module `pytz` que vous pouvez installer via pip, vous pouvez également l'utiliser pour obtenir l'heure actuelle dans n'importe quel fuseau horaire du monde.

Merci de votre lecture. Si vous trouvez cet article utile, vous pouvez le partager avec vos amis et votre famille.