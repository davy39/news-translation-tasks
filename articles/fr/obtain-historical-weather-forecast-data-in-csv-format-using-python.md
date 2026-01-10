---
title: Obtenir des données historiques de prévisions météorologiques au format CSV
  en utilisant Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-09T10:00:00.000Z'
originalURL: https://freecodecamp.org/news/obtain-historical-weather-forecast-data-in-csv-format-using-python
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca193740569d1a4ca4f62.jpg
tags:
- name: worldweatheronline
  slug: worldweatheronline
- name: api
  slug: api
- name: csv
  slug: csv
- name: dataframe
  slug: dataframe
- name: Machine Learning
  slug: machine-learning
- name: Python
  slug: python
- name: weather
  slug: weather
seo_title: Obtenir des données historiques de prévisions météorologiques au format
  CSV en utilisant Python
seo_desc: 'By Ekapope Viriyakovithya

  Recently, I worked on a machine learning project related to renewable energy, which
  required historical weather forecast data from multiple cities.

  Despite intense research, I had a hard time finding the good data source. Mo...'
---

Par Ekapope Viriyakovithya

Récemment, j'ai travaillé sur un projet de machine learning lié aux énergies renouvelables, qui nécessitait des **données historiques de prévisions météorologiques pour plusieurs villes**.

Malgré des recherches intensives, j'ai eu du mal à trouver une bonne source de données. La plupart des sites web restreignent l'accès aux données historiques des deux dernières semaines seulement. Si vous avez besoin de plus, vous devez payer. Dans mon cas, j'avais besoin de cinq ans de données — des prévisions historiques horaires, ce qui peut être coûteux.

### **Mes exigences sont...**

**1. Gratuit — au moins pendant la période d'essai**

Pas besoin de fournir des informations de carte de crédit.

**2. Flexible**

Flexible pour changer l'intervalle des prévisions, les périodes, les lieux.

**3. Reproductible**

Facile à reproduire et à implémenter en phase de production.

Finalement, j'ai décidé d'utiliser les données de [World Weather Online](https://www.worldweatheronline.com/developer/api/historical-weather-api.aspx). Cela m'a pris moins de deux minutes pour m'inscrire à l'essai gratuit de l'API premium — sans fournir d'informations de carte de crédit. (500 requêtes gratuites/clé/jour pendant 60 jours, en date du 30-Mai-2019).

![Image](https://cdn-media-1.freecodecamp.org/images/1*kVPI57az2iE7Kjni3AhxOw.png align="left")

[*https://www.worldweatheronline.com/developer/signup.aspx*](https://www.worldweatheronline.com/developer/signup.aspx)

Vous pouvez essayer des requêtes au format JSON ou XML [ici](https://www.worldweatheronline.com/developer/premium-api-explorer.aspx). Le résultat est un JSON imbriqué qui nécessite un peu de prétraitement avant d'être utilisé dans des modèles de ML. Par conséquent, j'ai écrit quelques [scripts](https://github.com/ekapope/WorldWeatherOnline) pour les analyser dans des DataFrames pandas et les sauvegarder en CSV pour une utilisation ultérieure.

### Présentation du package wwo-hist

Ce [package wwo-hist](https://pypi.org/project/wwo-hist/) est utilisé pour récupérer et analyser les données météorologiques historiques de [World Weather Online](https://www.worldweatheronline.com/developer/api/historical-weather-api.aspx) dans un DataFrame pandas et un fichier CSV.

**Entrée :** api_key, location_list, start_date, end_date, frequency

**Sortie :** location_name.csv

**Noms des colonnes de sortie :** date_time, maxtempC, mintempC, totalSnow_cm, sunHour, uvIndex, uvIndex, moon_illumination, moonrise, moonset, sunrise, sunset, DewPointC, FeelsLikeC, HeatIndexC, WindChillC, WindGustKmph, cloudcover, humidity, precipMM, pressure, tempC, visibility, winddirDegree, windspeedKmph

#### Installer et importer le package :

```py
pip install wwo-hist
```

```py
# importer le package et la fonction
from wwo_hist import retrieve_hist_data

# définir le répertoire de travail pour stocker le(s) fichier(s) csv de sortie
import os
os.chdir(".\YOUR_PATH")
```

**Exemple de code :**

Spécifiez les paramètres d'entrée et appelez ***retrieve_hist_data()***. Veuillez visiter [mon dépôt github](https://github.com/ekapope/WorldWeatherOnline) pour plus d'informations sur la configuration des paramètres.

Cela récupérera les **données historiques de prévisions météorologiques à intervalles de 3 heures** pour **Singapour** et **Californie** du **11-Déc-2018** au **11-Mar-2019**, sauvegardera la sortie dans la variable hist_weather_data et les **fichiers CSV**.

```py
FREQUENCY = 3
START_DATE = '11-DEC-2018'
END_DATE = '11-MAR-2019'
API_KEY = 'YOUR_API_KEY'
LOCATION_LIST = ['singapore','california']

hist_weather_data = retrieve_hist_data(API_KEY,
                                LOCATION_LIST,
                                START_DATE,
                                END_DATE,
                                FREQUENCY,
                                location_label = False,
                                export_csv = True,
                                store_df = True)
```

![Image](https://cdn-media-1.freecodecamp.org/images/0*Ga1fGBrxkoKgfzbu align="left")

*Voici ce que vous verrez dans votre console.*

![Image](https://cdn-media-1.freecodecamp.org/images/1*0-UJ7XO4ZG76oDlVvHQNVA.png align="left")

*Fichiers CSV résultants exportés vers votre répertoire de travail.*

![Image](https://cdn-media-1.freecodecamp.org/images/0*gdtco3Zi0Kv03uz9 align="left")

*Vérifiez la sortie CSV.*

Voilà ! Le script détaillé est également [documenté sur GitHub](https://github.com/ekapope/WorldWeatherOnline).

---

Merci d'avoir lu. Essayez-le et faites-moi savoir vos retours ! Si vous aimez ce que j'ai fait, envisagez de me suivre sur [GitHub](https://github.com/ekapope), [Medium](https://medium.com/@ekapope.v) et [Twitter](https://twitter.com/EkapopeV) pour obtenir plus d'articles et de tutoriels dans votre fil d'actualité.