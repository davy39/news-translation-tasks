---
title: Comment utiliser les objets timedelta en Python pour travailler avec des dates
subtitle: ''
author: Bala Priya C
co_authors: []
series: null
date: '2021-06-29T18:25:52.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-timedelta-objects-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/TIMEDELTA-OBJECTS-IN-PYTHON.png
tags:
- name: Python
  slug: python
seo_title: Comment utiliser les objets timedelta en Python pour travailler avec des
  dates
seo_desc: "Why do we need the timedelta object?\nWhen you're working with dates and\
  \ times in Python, you'll often use the datetime module. \nIn this post, we'll see\
  \ how we can use the timedelta object in the datetime module. It denotes a span\
  \ of time and can help..."
---

### Pourquoi avons-nous besoin de l'objet timedelta ?

Lorsque vous travaillez avec des dates et des heures en Python, vous utiliserez souvent le module `datetime`.

Dans cet article, nous verrons comment utiliser l'objet `timedelta` du module `datetime`. Il représente une durée et peut aider lorsque nous devons effectuer des opérations arithmétiques simples sur des objets datetime.

En particulier, nous apprendrons comment faire ce qui suit avec des exemples de code :

1. Créer un objet `timedelta` de base
2. Afficher la date et l'heure actuelles
3. Calculer une date dans le futur
4. Calculer une date dans le passé
5. Calculer le temps écoulé depuis un événement particulier ou le temps restant avant qu'un événement particulier ne se produise

### Importations nécessaires

Avant de commencer ces tâches, importons d'abord les modules nécessaires comme montré dans l'extrait de code ci-dessous :

```python
# Importer les modules nécessaires
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
```

## Comment créer un objet timedelta de base en Python

Créons maintenant un objet `timedelta` de base, comme ceci :

```python
time_delt1 = timedelta(days= 270, hours = 9, minutes = 18)
print(time_delt1)

# Exemple de sortie
270 days, 9:18:00
```

Nous avons créé avec succès un objet `timedelta`. Maintenant, nous devons créer une heure de référence afin de pouvoir appliquer l'objet `timedelta` que nous avons créé pour effectuer une arithmétique significative. Faisons cela à l'étape suivante.

## Comment afficher la date et l'heure actuelles en Python

Afin d'appliquer la durée que nous avons créée en utilisant l'objet `timedelta`, nous utiliserons la date et l'heure actuelles comme référence.

Nous pouvons obtenir la date et l'heure actuelles en appelant la méthode `now()` sur l'objet `datetime`, comme montré dans l'extrait de code ci-dessous :

```python
# pour créer une référence, utiliser la date et l'heure actuelles
time_now = datetime.now()
print(time_now)

# Exemple de sortie
2021-06-22 17:49:18.574503
```

## Comment calculer une date dans le futur en Python

Calculons maintenant quelle date il sera après une durée de `time_delt1` que nous avons créée dans la première étape ci-dessus.

Pour calculer un point dans le temps futur, nous devons simplement ajouter la durée définie par l'objet `timedelta` à l'heure actuelle.

```python
# vérifier quelle date il sera après time_delt1
future_date1 = time_now + time_delt1
print(future_date1)

# Exemple de sortie
2022-03-20 03:07:18.574503
```

Regardons maintenant un autre exemple où nous voulons savoir quelle date il sera après un nombre spécifique de jours, disons 189 jours.

```python
# Quel jour sera-t-il dans 189 jours
future_date2 = time_now + timedelta(days=189)
print(future_date2)

# Exemple de sortie
2021-12-28 17:49:18.574503
```

## Comment calculer une date dans le passé en Python

Comme vous l'avez peut-être deviné, pour savoir quel jour il était il y a 189 jours, nous devons simplement remplacer '+' par '-' dans l'exemple ci-dessus. Vous pouvez voir cela dans l'extrait de code ci-dessous :

```python
# Quel jour était-il il y a 189 jours
past_date1 = time_now - timedelta(days=189)
print(past_date1)

# Exemple de sortie
2020-12-15 17:49:18.574503
```

## Comment calculer le temps écoulé ou le temps restant en Python

Calculons maintenant le temps restant avant la Journée des enseignants de cette année. Nous pouvons faire cela comme suit.

Pour calculer par rapport à aujourd'hui, nous pouvons appeler la méthode `today()` sur l'objet date pour récupérer la date d'aujourd'hui :

`Syntaxe : today = date.today() # Retourne la date d'aujourd'hui`

```python
# créer des objets de référence pour aujourd'hui et la journée des enseignants
teachers_day = date(time_now.year, 9, 5)
today = date.today()
```

Nous pouvons ensuite savoir dans combien de temps aura lieu la Journée des enseignants en utilisant l'extrait de code suivant :

```python
# calculer le nombre de jours avant la journée des enseignants.
time_to_td = teachers_day - today
print(f"La journée des enseignants est dans {time_to_td.days} jours")

# Exemple de sortie
La journée des enseignants est dans 74 jours
```

Il est également possible que la Journée des enseignants de cette année soit déjà passée au moment où vous lisez cet article 😀. Si la Journée des enseignants de cette année est déjà passée, faites ce qui suit :

* Mettez à jour la date d'intérêt pour la Journée des enseignants de l'année prochaine.
* Calculez combien de jours il reste avant la Journée des enseignants de l'année prochaine.

Cela est illustré dans l'extrait de code suivant :

```python
# vérifier si la journée des enseignants est passée
if teachers_day < today:
  print(f"La journée des enseignants de cette année était il y a {(today-teachers_day).days} jours")
  time_to_td = teachers_day - today
  print(f"La journée des enseignants de l'année prochaine est dans {time_to_td.days} jours")
```

## Un rapide récapitulatif

En résumé, nous avons vu comment utiliser les objets `timedelta` pour effectuer des opérations arithmétiques simples sur des dates et calculer une date passée et future.

Nous pouvons également calculer le temps écoulé depuis un événement particulier ou le temps restant avant qu'un événement particulier ne se produise.

J'espère que vous avez trouvé cet article utile. Merci d'avoir lu !

Pour une référence plus détaillée, veuillez consulter la documentation officielle [ici](https://docs.python.org/3/library/datetime.html).