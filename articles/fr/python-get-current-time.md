---
title: Python Obtenir l'Heure Actuelle
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-07-13T22:48:46.000Z'
originalURL: https://freecodecamp.org/news/python-get-current-time
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/getCurrentTime.png
tags:
- name: Python
  slug: python
seo_title: Python Obtenir l'Heure Actuelle
seo_desc: 'In your websites and applications, you might want to add functionalities
  like timestamps or checking the time of a user’s activity.

  Every programming language has modules or methods for working with time, and Python
  is not an exception.

  With the date...'
---

Dans vos sites web et applications, vous pourriez vouloir ajouter des fonctionnalités comme des horodatages ou vérifier l'heure d'activité d'un utilisateur.

Chaque langage de programmation possède des modules ou des méthodes pour travailler avec le temps, et Python ne fait pas exception.

Avec les modules `datetime` et `time` de Python, vous pouvez obtenir la date et l'heure actuelles, ou la date et l'heure dans un fuseau horaire particulier.

Dans cet article, je vais vous montrer comment obtenir l'heure actuelle en Python avec les modules `datetime` et `time`.

## Comment Obtenir l'Heure Actuelle avec le Module Datetime

La première chose que vous pouvez faire pour obtenir rapidement la date et l'heure actuelles est d'utiliser la fonction `datetime.now()` du module datetime :

```py
from datetime import datetime
current_date_and_time = datetime.now()

print("La date et l'heure actuelles sont", current_date_and_time)

# La date et l'heure actuelles sont 2022-07-12 10:22:00.776664
```

Cela vous montre non seulement l'heure mais aussi la date.

Pour extraire l'heure, vous pouvez utiliser la fonction `strftime()` et passer `("%H:%M:%S")`

- %H obtient l'heure
- %M obtient les minutes
- %S obtient les secondes

 ```py
from datetime import datetime
time_now = datetime.now()
current_time = time_now.strftime("%H:%M:%S")

print("L'heure actuelle est", current_time)

# L'heure actuelle est 10:27:45
```

Vous pouvez également réécrire le code comme ceci :
```py
from datetime import datetime
time_now = datetime.now().strftime("%H:%M:%S")

print("L'heure actuelle est", time_now)

# L'heure actuelle est 10:30:37
```

## Comment Obtenir l'Heure Actuelle avec le Module Time

En plus du module `datetime()`, le module `time` est une autre méthode intégrée pour obtenir l'heure actuelle en Python.

Comme d'habitude, vous devez d'abord importer le module time, puis vous pouvez utiliser la méthode `ctime()` pour obtenir la date et l'heure actuelles.

```py
import time

current_time = time.ctime()
print(current_time)

# Tue Jul 12 10:37:46 2022
```

Pour extraire l'heure actuelle, vous devez également utiliser la fonction `strftime()` :

```py
import time

current_time = time.strftime("%H:%M:%S")
print("L'heure actuelle est", current_time)

# L'heure actuelle est 10:42:32
```


## Réflexions Finales

Cet article vous a montré deux façons d'obtenir l'heure actuelle avec Python.

Si vous vous demandez lequel utiliser entre les modules `time` et `datetime`, cela dépend de ce que vous voulez :

- `time` est plus précis que `datetime`
- si vous ne voulez pas d'ambiguïté avec l'heure d'été (DST), utilisez `time`
- `datetime` a plus d'objets intégrés avec lesquels vous pouvez travailler mais a un support limité pour les fuseaux horaires.

Si vous voulez travailler avec des fuseaux horaires, vous devriez envisager d'utiliser le module `pytz`.

Pour apprendre comment obtenir l'heure dans un fuseau horaire particulier, j'ai écrit un article sur [le module `pytz` ici](https://www.freecodecamp.org/news/how-to-get-the-current-time-in-python-with-datetime/#howtogetthecurrenttimeofatimezonewithdatetime).

Continuez à coder :)