---
title: Comment visualiser la pollution atmosphérique à l'aide de cartes Folium - Un
  tutoriel approfondi
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-03T21:59:44.000Z'
originalURL: https://freecodecamp.org/news/visualizing-air-pollution-folium-maps
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/0_PlMoYJ9MPTjB_2Ju.jpeg
tags:
- name: Data Science
  slug: data-science
- name: data visualization
  slug: data-visualization
- name: Folium
  slug: folium
- name: GeoJSON
  slug: geojson
- name: time series
  slug: time-series
seo_title: Comment visualiser la pollution atmosphérique à l'aide de cartes Folium
  - Un tutoriel approfondi
seo_desc: 'By Bert Carremans

  In my previous story on forecasting air pollution, I looked into using recurrent
  neural networks (RNN and LSTM) to forecast air pollution in Belgium. As a small
  side project, I thought it would be interesting to plot the air polluti...'
---

Par Bert Carremans

Dans mon précédent article sur [la prévision de la pollution atmosphérique](https://www.freecodecamp.org/news/forecasting-air-pollution-recurrent-neural-networks/), j'ai étudié l'utilisation des réseaux de neurones récurrents (RNN et LSTM) pour prévoir la pollution atmosphérique en Belgique. En tant que petit projet annexe, j'ai pensé qu'il serait intéressant de **tracer la pollution atmosphérique au fil du temps sur une carte**. Le [package Folium](http://python-visualization.github.io/folium/) est un excellent outil pour cela.

Nous allons tracer les quantités de 6 polluants atmosphériques en Belgique :

* **Ozone (O3)**
* **Dioxyde d'azote (NO2)**
* **Monoxyde de carbone (CO)**
* **Dioxyde de soufre (SO2)**
* **Particules (PM10)**
* **Benzène (C6H6)**

Les données sont téléchargées depuis le site de l'[Agence européenne pour l'environnement (AEE)](https://www.eea.europa.eu/data-and-maps/data/aqereporting-2/be). Si vous souhaitez utiliser des données d'autres pays européens, je vous encourage à visiter leur site. Il contient des ensembles de données pour de nombreux pays de l'UE et est très bien documenté.

Les ensembles de données que nous allons utiliser sont :

* BE__<pollutant_ID>__20132015_aggregated_timeseries.csv
* BE_20132015_metadata.csv

Les identifiants des polluants sont décrits dans le [vocabulaire de l'AEE sur les polluants atmosphériques](http://dd.eionet.europa.eu/vocabulary/aq/pollutant).

* 1 = Dioxyde de soufre
* 5 = Particules
* 7 = Ozone
* 8 = Dioxyde d'azote
* 10 = Monoxyde de carbone
* 20 = Benzène

# Installation du projet

## Importation des packages

```python
from pathlib import Path
import pandas as pd
import numpy as np

import seaborn as sns
import folium
from folium.plugins import TimestampedGeoJson

project_dir = Path('/Users/bertcarremans/Data Science/Projecten/air_pollution_forecasting')
```

## Polluants atmosphériques

Nous allons créer un dictionnaire des polluants atmosphériques et de leur numéro de dataset, notation scientifique, nom et limites de classes. Les limites de classes sont basées sur l'échelle de cette [page Wikipedia](https://nl.wikipedia.org/wiki/Luchtvervuiling).

```python
pollutants = {
    1: {
        'notation' : 'SO2',
        'name' :'Dioxyde de soufre',
        'bin_edges' : np.array([15,30,45,60,80,100,125,165,250])
    },
    5: {
        'notation' : 'PM10',
        'name' :'Particules < 10 µm',
        'bin_edges' : np.array([10,20,30,40,50,70,100,150,200])
    },
    7: {'notation' : 'O3',
        'name' :'Ozone',
        'bin_edges' : np.array([30,50,70,90,110,145,180,240,360])
    },
    8: {'notation' : 'NO2',
        'name' :'Dioxyde d\'azote',
        'bin_edges' : np.array([25,45,60,80,110,150,200,270,400])
    },
    10: {'notation' : 'CO',
        'name' :'Monoxyde de carbone',
         'bin_edges' : np.array([1.4,2.1,2.8,3.6,4.5,5.2,6.6,8.4,13.7])
    },
    20: {'notation' : 'C6H6',
        'name' :'Benzène',
         'bin_edges' : np.array([0.5,1.0,1.25,1.5,2.75,3.5,5.0,7.5,10.0])
    }
}
```

## Chargement des métadonnées

Dans les métadonnées, nous avons les **coordonnées** pour chaque point d'échantillonnage. Nous aurons besoin de ces informations pour tracer les points d'échantillonnage sur la carte.

```python
meta = pd.read_csv(project_dir / 'data/raw/BE_2013-2015_metadata.csv', sep='\t')
```

## Échelle de couleurs

Il y a 10 limites de classes pour lesquelles nous utiliserons une couleur différente. Ces couleurs ont été créées avec [ColorBrewer](http://colorbrewer2.org/#type=diverging&scheme=RdBu&n=10).

```python
color_scale = np.array(['#053061','#2166ac','#4393c3','#92c5de','#d1e5f0','#fddbc7','#f4a582','#d6604d','#b2182b','#67001f'])
sns.palplot(sns.color_palette(color_scale))
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/1_ymG4157cHZa4dIatJQldwg.png)

# Préparation des données

## Chargement des données de séries temporelles

Nous convertissons les variables de date en datetime. Ainsi, nous pouvons facilement les utiliser plus tard pour découper le DataFrame Pandas.

```python
def load_data(pollutant_ID):
    print('> Chargement des données...')
    date_vars = ['DatetimeBegin','DatetimeEnd']
    filename = 'data/raw/BE_' + str(pollutant_ID) + '_2013-2015_aggregated_timeseries.csv'
    agg_ts = pd.read_csv(project_dir / filename, sep='\t', parse_dates=date_vars, date_parser=pd.to_datetime)
    return agg_ts
```

## Nettoyage des données

Nous allons effectuer un nettoyage de base des données :

* Conserver uniquement les enregistrements avec DataAggregationProcss de P1D pour avoir des données quotidiennes
* Supprimer les enregistrements avec UnitOfAirPollutionLevel de count
* Supprimer les variables redondantes pour la visualisation
* Supprimer les points d'échantillonnage qui ont moins de 1000 jours de mesure
* Insérer les dates manquantes et imputer le AirpollutionLevel avec la valeur de la date valide suivante

```python
def clean_data(df):
    print('> Nettoyage des données...')
    df = df.loc[df.DataAggregationProcess=='P1D', :] 
    df = df.loc[df.UnitOfAirPollutionLevel!='count', :]
    ser_avail_days = df.groupby('SamplingPoint').nunique()['DatetimeBegin']
    df = df.loc[df.SamplingPoint.isin(ser_avail_days[ser_avail_days.values >= 1000].index), :]
    vars_to_drop = ['AirPollutant','AirPollutantCode','Countrycode','Namespace','TimeCoverage','Validity','Verification','AirQualityStation',
               'AirQualityStationEoICode','DataAggregationProcess','UnitOfAirPollutionLevel', 'DatetimeEnd', 'AirQualityNetwork',
               'DataCapture', 'DataCoverage']
    df.drop(columns=vars_to_drop, axis='columns', inplace=True)
    
    dates = list(pd.period_range(min(df.DatetimeBegin), max(df.DatetimeBegin), freq='D').values)
    samplingpoints = list(df.SamplingPoint.unique())
    new_idx = []
    for sp in samplingpoints:
        for d in dates:
            new_idx.append((sp, np.datetime64(d)))

    df.set_index(keys=['SamplingPoint', 'DatetimeBegin'], inplace=True)
    df.sort_index(inplace=True)
    df = df.reindex(new_idx)
    df['AirPollutionLevel'] = df.groupby(level=0).AirPollutionLevel.bfill().fillna(0)
    return df
```

## Tracé de la pollution atmosphérique au fil du temps

Charger toutes les dates pour tous les points d'échantillonnage serait trop lourd pour la carte. Par conséquent, nous allons **rééchantillonner** les données en prenant le dernier jour de chaque mois.

**Note** : Les limites de classes que nous utilisons dans ce notebook devraient normalement être appliquées sur des moyennes (semi-)horaires pour O3, NO2 et CO. Dans les ensembles de données que nous utilisons dans ce notebook, nous n'avons que des moyennes quotidiennes. Comme ce notebook est uniquement destiné à illustrer comment tracer des données de séries temporelles sur une carte, nous continuerons avec les moyennes quotidiennes. Sur le site de l'AEE, vous pouvez cependant télécharger des moyennes horaires également.

```python
def color_coding(poll, bin_edges):    
    idx = np.digitize(poll, bin_edges, right=True)
    return color_scale[idx]

def prepare_data(df, pollutant_ID):
    print('> Préparation des données...')
    df = df.reset_index().merge(meta, how='inner', on='SamplingPoint').set_index('DatetimeBegin')
    df = df.loc[:, ['SamplingPoint','Latitude', 'Longitude', 'AirPollutionLevel']]
    df = df.groupby('SamplingPoint', group_keys=False).resample(rule='M').last().reset_index()
    df['color'] = df.AirPollutionLevel.apply(color_coding, bin_edges=pollutants[pollutant_ID]['bin_edges'])
    return df
```

Pour montrer l'évolution de la pollution au fil du temps, nous allons utiliser le **TimestampedGeoJson** [plugin Folium](https://python-visualization.github.io/folium/plugins.html). Ce plugin nécessite des fonctionnalités d'entrée GeoJSON. Afin de convertir les données du dataframe, j'ai créé une petite fonction **create_geojson_features** qui fait cela.

```python
def create_geojson_features(df):
    print('> Création des fonctionnalités GeoJSON...')
    features = []
    for _, row in df.iterrows():
        feature = {
            'type': 'Feature',
            'geometry': {
                'type':'Point', 
                'coordinates':[row['Longitude'],row['Latitude']]
            },
            'properties': {
                'time': row['DatetimeBegin'].date().__str__(),
                'style': {'color' : row['color']},
                'icon': 'circle',
                'iconstyle':{
                    'fillColor': row['color'],
                    'fillOpacity': 0.8,
                    'stroke': 'true',
                    'radius': 7
                }
            }
        }
        features.append(feature)
    return features
```

Après cela, les fonctionnalités d'entrée sont créées et nous pouvons créer une carte pour les ajouter. Le plugin TimestampedGeoJson offre quelques options pratiques pour le curseur temporel, qui sont auto-explicatives.

```python
def make_map(features):
    print('> Création de la carte...')
    coords_belgium=[50.5039, 4.4699]
    pollution_map = folium.Map(location=coords_belgium, control_scale=True, zoom_start=8)

    TimestampedGeoJson(
        {'type': 'FeatureCollection',
        'features': features}
        , period='P1M'
        , add_last_point=True
        , auto_play=False
        , loop=False
        , max_speed=1
        , loop_button=True
        , date_options='YYYY/MM'
        , time_slider_drag_update=True
    ).add_to(pollution_map)
    print('> Terminé.')
    return pollution_map

def plot_pollutant(pollutant_ID):
    print('Cartographie de la pollution par {} en Belgique en 2013-2015'.format(pollutants[pollutant_ID]['name']))
    df = load_data(pollutant_ID)
    df = clean_data(df)
    df = prepare_data(df, pollutant_ID)
    features = create_geojson_features(df)
    return make_map(features), df
```

Ci-dessous se trouvent les cartes par polluant atmosphérique. Vous pouvez cliquer sur l'image pour accéder à une page web avec la carte interactive. En cliquant sur le bouton _lecture_, vous pouvez voir l'évolution du polluant atmosphérique au fil du temps.

## Dioxyde de soufre

```python
pollution_map, df = plot_pollutant(1)
pollution_map.save('../output/pollution_so2.html')
pollution_map
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/1_BQ7PJfWRkH3Mud3CxMvKfQ.png)
_[https://bertcarremans.github.io/air_pollution_viz/pollution_so2.html](https://bertcarremans.github.io/air_pollution_viz/pollution_c6h6.html)_

## Particules

```python
pollution_map, df = plot_pollutant(5)
pollution_map.save('../output/pollution_pm.html')
pollution_map
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/1_BQ7PJfWRkH3Mud3CxMvKfQ-1.png)
_[https://bertcarremans.github.io/air_pollution_viz/pollution_pm.html](https://bertcarremans.github.io/air_pollution_viz/pollution_c6h6.html)_

Les autres visualisations peuvent être trouvées à :

* [https://bertcarremans.github.io/air_pollution_viz/pollution_c6h6.html](https://bertcarremans.github.io/air_pollution_viz/pollution_c6h6.html)
* [https://bertcarremans.github.io/air_pollution_viz/pollution_co.html](https://bertcarremans.github.io/air_pollution_viz/pollution_co.html)
* [https://bertcarremans.github.io/air_pollution_viz/pollution_no2.html](https://bertcarremans.github.io/air_pollution_viz/pollution_no2.html)
* [https://bertcarremans.github.io/air_pollution_viz/pollution_o3.html](https://bertcarremans.github.io/air_pollution_viz/pollution_o3.html)

# Conclusion

Avec cet article, je souhaite démontrer à quel point il est facile de visualiser des données de séries temporelles sur une carte avec Folium. Les cartes pour tous les polluants et le notebook Jupyter peuvent être trouvés sur [GitHub](https://github.com/bertcarremans/air_pollution_forecasting/blob/master/notebooks/Visualizing%20Air%20Pollution%20in%20Belgium.ipynb). N'hésitez pas à le réutiliser pour cartographier la pollution atmosphérique dans votre pays d'origine.