---
title: Comment prévoir la pollution atmosphérique avec les réseaux de neurones récurrents
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-02T21:52:42.000Z'
originalURL: https://freecodecamp.org/news/forecasting-air-pollution-recurrent-neural-networks
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/0_6XEYi4xnCQQGrEdC.jpeg
tags:
- name: Deep Learning
  slug: deep-learning
- name: forecasting
  slug: forecasting
- name: LSTM
  slug: lstm
- name: neural networks
  slug: neural-networks
- name: RNN
  slug: rnn
seo_title: Comment prévoir la pollution atmosphérique avec les réseaux de neurones
  récurrents
seo_desc: 'By Bert Carremans

  After the citizen science project of Curieuze Neuzen, I wanted to learn more about
  air pollution to see if I could make a data science project out of it. On the website
  of the European Environment Agency, you can find a huge amount ...'
---

Par Bert Carremans

Après le projet de science citoyenne de [Curieuze Neuzen](https://curieuzeneuzen.be/), je voulais en apprendre davantage sur la pollution atmosphérique pour voir si je pouvais en faire un projet de science des données. Sur le site web de l'[Agence européenne pour l'environnement](https://www.eea.europa.eu/data-and-maps/data/aqereporting-8), vous pouvez trouver une énorme quantité de données et d'informations sur la pollution atmosphérique.

Dans ce notebook, nous nous concentrerons sur la qualité de l'air en **Belgique**, et plus spécifiquement sur la pollution par le **dioxyde de soufre (SO2)**. Les données peuvent être téléchargées via [https://www.eea.europa.eu/data-and-maps/data/aqereporting-2/be](https://www.eea.europa.eu/data-and-maps/data/aqereporting-2/be).

Le fichier zip contient des fichiers séparés pour différents polluants atmosphériques et niveaux d'agrégation. Le premier chiffre représente l'ID du polluant tel que décrit dans le [vocabulaire](http://dd.eionet.europa.eu/vocabulary/aq/pollutant). Le fichier utilisé dans ce notebook est **BE_1_20132015_aggregated_timeseries.csv.** Il s'agit de la pollution par le SO2 en Belgique, mais vous pouvez également trouver des données similaires pour d'autres pays européens.

Les descriptions des champs dans les fichiers CSV sont disponibles sur la [page de téléchargement des données](https://www.eea.europa.eu/data-and-maps/data/aqereporting-2/be.). Plus d'informations sur les polluants atmosphériques peuvent être trouvées sur [Wikipedia](https://nl.wikipedia.org/wiki/Luchtvervuiling).

# Installation du projet

```python
# Importation des packages
from pathlib import Path
import pandas as pd
import numpy as np
import pandas_profiling
%matplotlib inline
import matplotlib.pyplot as plt
import warnings
warnings.simplefilter(action = 'ignore', category = FutureWarning)
from sklearn.preprocessing import MinMaxScaler

from keras.preprocessing.sequence import TimeseriesGenerator
from keras.models import Sequential
from keras.layers import Dense, LSTM, SimpleRNN
from keras.optimizers import RMSprop
from keras.callbacks import ModelCheckpoint, EarlyStopping
from keras.models import model_from_json

# Définition du répertoire du projet
project_dir = Path('/Users/bertcarremans/Data Science/Projecten/air_pollution_forecasting')
```

# Chargement des données

```python
date_vars = ['DatetimeBegin','DatetimeEnd']

agg_ts = pd.read_csv(project_dir / 'data/raw/BE_1_2013-2015_aggregated_timeseries.csv', sep='\t', parse_dates=date_vars, date_parser=pd.to_datetime)
meta = pd.read_csv(project_dir / 'data/raw/BE_2013-2015_metadata.csv', sep='\t')

print('aggregated timeseries shape:{}'.format(agg_ts.shape))
print('metadata shape:{}'.format(meta.shape))
```

# Exploration des données

Utilisons **pandas_profiling** pour inspecter les données.

```python
pandas_profiling.ProfileReport(agg_ts)
```

Je ne montrerai pas la sortie de pandas_profiling dans cette histoire afin de ne pas l'encombrer avec des graphiques. Mais vous pouvez la trouver dans mon [dépôt GitHub](https://github.com/bertcarremans/air_pollution_forecasting).

Le rapport pandas_profiling nous montre ce qui suit :

* Il y a 6 variables constantes. Nous pouvons les supprimer de l'ensemble de données.
* Aucune valeur manquante n'existe, donc probablement nous n'aurons pas besoin d'appliquer d'imputation.
* **AirPollutionLevel** a quelques zéros, mais cela pourrait être parfaitement normal. D'autre part, ces variables ont quelques valeurs extrêmes, qui pourraient être des enregistrements incorrects de la pollution atmosphérique.
* Il y a 53 **AirQualityStations**, qui sont probablement les mêmes que les **SamplingPoints**. **AirQualityStationEoICode** est simplement un code plus court pour la AirQualityStation, donc cette variable peut également être supprimée.
* Il y a 3 valeurs pour **AirQualityNetwork** (Bruxelles, Flandre et Wallonie). La plupart des mesures proviennent de Flandre.
* **DataAggregationProcess** : la plupart des lignes contiennent des données agrégées comme la moyenne sur 24 heures d'une journée de mesures (P1D). Plus d'informations sur les autres valeurs peuvent être trouvées [ici](http://dd.eionet.europa.eu/vocabulary/aq/aggregationprocess). Dans ce projet, nous ne considérerons que les valeurs P1D.
* **DataCapture** : Proportion de temps de mesure valide par rapport au temps total mesuré (couverture temporelle) dans la période de moyenne, exprimée en pourcentage. Presque toutes les lignes ont environ 100% de temps de mesure valide. Certaines lignes ont un DataCapture légèrement inférieur à 100%.
* **DataCoverage** : Proportion de mesures valides incluses dans le processus d'agrégation dans la période de moyenne, exprimée en pourcentage. Dans cet ensemble de données, nous avons un minimum de 75%. Selon la [définition de cette variable](https://www.eea.europa.eu/data-and-maps/data/aqereporting-2/be), les valeurs inférieures à 75% ne doivent pas être incluses pour les évaluations de la qualité de l'air, ce qui explique pourquoi ces lignes ne sont pas présentes dans l'ensemble de données.
* **TimeCoverage** : fortement corrélé à DataCoverage et sera supprimé des données.
* **UnitOfAirPollutionLevel** : 423 lignes ont une unité de _count_. Pour avoir une variable cible cohérente, nous supprimerons les enregistrements avec ce type d'unité.
* **DateTimeBegin** et **DateTimeEnd** : l'histogramme ne fournit pas assez de détails ici. Cela doit être analysé plus en profondeur.

# DateTimeBegin et DateTimeEnd

L'histogramme dans le pandas_profiling a combiné plusieurs jours par bin. Regardons au niveau quotidien comment ces variables se comportent.

## Plusieurs niveaux d'agrégation par date

* **DatetimeBegin** : un grand nombre d'enregistrements le 1er janvier 2013, 2014, 2015 et le 1er octobre 2013 et 2014.
* **DatetimeEnd** : un grand nombre d'enregistrements le 1er janvier 2014, 2015, 2016 et le 1er avril 2014 et 2015.

```python
plt.figure(figsize=(20,6))
plt.plot(agg_ts.groupby('DatetimeBegin').count(), 'o', color='skyblue')
plt.title('Nb de mesures par DatetimeBegin')
plt.ylabel('nombre de mesures')
plt.xlabel('DatetimeBegin')
plt.show()
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/1_nP33p0hVPjLpxTFAwDQJyQ.png)
_Nombre de lignes par date_

Les valeurs aberrantes dans le nombre d'enregistrements sont liées aux multiples niveaux d'agrégation (DataAggregationProcess). Les valeurs dans DataAggregationProcess à ces dates reflètent la période de temps entre DatetimeBegin et DatetimeEnd. Par exemple, le 1er janvier 2013 est la date de début d'une période de mesure d'un an jusqu'au 1er janvier 2014.

Comme nous ne sommes intéressés que par le niveau d'agrégation quotidien, **filtrer les autres niveaux d'agrégation** résoudra ce problème. Nous pouvons également supprimer DatetimeEnd pour cette raison.

## Pas de temps manquants au niveau d'agrégation quotidien

Comme nous pouvons le voir ci-dessous, **tous les SamplingPoints n'ont pas de données pour tous les DatetimeBegin dans la période de trois ans**. Ce sont probablement des jours où la variable DataCoverage était inférieure à 75%. Donc, ces jours-là, nous n'avons pas suffisamment de mesures valides. Plus tard dans ce notebook, nous utiliserons les mesures des jours précédents pour prédire la pollution du jour actuel.

Pour avoir des pas de temps de taille similaire, nous devrons insérer des lignes pour les DatetimeBegin manquants par SamplingPoint. Nous **insérerons les données de mesure du jour suivant avec des données valides**.

Deuxièmement, nous **supprimerons les SamplingPoints avec trop de pas de temps manquants**. Ici, nous prendrons un nombre arbitraire de 1.000 pas de temps comme nombre minimum de pas de temps requis.

```python
ser_avail_days = agg_ts.groupby('SamplingPoint').nunique()['DatetimeBegin']
plt.figure(figsize=(8,4))
plt.hist(ser_avail_days.sort_values(ascending=False))
plt.ylabel('Nb SamplingPoints')
plt.xlabel('Nb de Unique DatetimeBegin')
plt.title('Distribution des Samplingpoints par le Nb de jours de mesure disponibles')
plt.show()
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/1_tcdKTqJJjjtBZ4QbNN2uzg.png)
_Distribution des SamplingPoints par le nombre de jours de mesure disponibles_

# Préparation des données

## Nettoyage des données

Sur la base de l'exploration des données, nous ferons ce qui suit pour nettoyer les données :

* Conserver uniquement les enregistrements avec DataAggregationProcess de P1D
* Supprimer les enregistrements avec UnitOfAirPollutionLevel de count
* Supprimer les variables unaires et autres variables redondantes
* Supprimer les SamplingPoints qui ont moins de 1000 jours de mesure

```python
df = agg_ts.loc[agg_ts.DataAggregationProcess=='P1D', :] 
df = df.loc[df.UnitOfAirPollutionLevel!='count', :]
df = df.loc[df.SamplingPoint.isin(ser_avail_days[ser_avail_days.values >= 1000].index), :]
vars_to_drop = ['AirPollutant','AirPollutantCode','Countrycode','Namespace','TimeCoverage','Validity','Verification','AirQualityStation',
               'AirQualityStationEoICode','DataAggregationProcess','UnitOfAirPollutionLevel', 'DatetimeEnd', 'AirQualityNetwork',
               'DataCapture', 'DataCoverage']
df.drop(columns=vars_to_drop, axis='columns', inplace=True)
```

## Insertion de lignes pour les pas de temps manquants

Pour chaque SamplingPoint, nous insérerons d'abord des lignes (vides) pour lesquelles nous n'avons pas de DatetimeBegin. Cela peut être fait en créant un index multi-complet avec tous les SamplingPoints et sur la plage entre les DatetimeBegin minimum et maximum. Ensuite, **reindex** insérera les lignes manquantes mais avec NaN pour les colonnes.

Deuxièmement, nous utilisons **bfill** et spécifions d'imputer les valeurs manquantes avec les valeurs de la ligne suivante avec des données valides. La méthode bfill est appliquée à un objet groupby pour limiter le remplissage dans les lignes de chaque SamplingPoint. De cette façon, nous n'utilisons pas les valeurs d'un autre SamplingPoint pour remplir les valeurs manquantes.

Un point d'échantillonnage pour tester si cette opération a fonctionné correctement est _SPO-BETR223_00001_100_ pour la date _20130129_.

```python
dates = list(pd.period_range(min(df.DatetimeBegin), max(df.DatetimeBegin), freq='D').values)
samplingpoints = list(df.SamplingPoint.unique())

new_idx = []
for sp in samplingpoints:
    for d in dates:
        new_idx.append((sp, np.datetime64(d)))

df.set_index(keys=['SamplingPoint', 'DatetimeBegin'], inplace=True)
df.sort_index(inplace=True)
df = df.reindex(new_idx)
#print(df.loc['SPO-BETR223_00001_100','2013-01-29'])  # devrait contenir NaN pour les colonnes

df['AirPollutionLevel'] = df.groupby(level=0).AirPollutionLevel.bfill().fillna(0)
#print(df.loc['SPO-BETR223_00001_100','2013-01-29'])  # NaN sont remplacés par les valeurs de 2013-01-30
print('{} valeurs manquantes'.format(df.isnull().sum().sum()))
```

## Gestion de plusieurs séries temporelles

D'accord, maintenant nous avons un ensemble de données qui est nettoyé et ne contient aucune valeur manquante. Un aspect qui rend cet ensemble de données particulier est que nous avons des données pour **plusieurs points d'échantillonnage**. Donc nous avons plusieurs séries temporelles.

Une façon de gérer cela est de créer **des variables fictives pour les points d'échantillonnage** et d'utiliser tous les enregistrements pour entraîner le modèle. Une autre façon est de construire **un modèle séparé par point d'échantillonnage**.

Dans ce notebook, nous ferons cette dernière option. Nous limiterons cependant le notebook à le faire pour un seul point d'échantillonnage. Mais la même logique peut être appliquée à chaque point d'échantillonnage.

```python
df = df.loc['SPO-BETR223_00001_100',:]
```

## Division des ensembles d'entraînement, de test et de validation

Nous séparons un ensemble de test afin d'évaluer la performance du modèle. L'ensemble de test ne sera pas utilisé pendant la phase d'entraînement.

* ensemble d'entraînement : données jusqu'en juillet 2014
* ensemble de validation : 6 mois entre juillet 2014 et janvier 2015
* ensemble de test : données de 2015

```python
train = df.query('DatetimeBegin < "2014-07-01"')
valid = df.query('DatetimeBegin >= "2014-07-01" and DatetimeBegin < "2015-01-01"')
test = df.query('DatetimeBegin >= "2015-01-01"')
```

## Mise à l'échelle

```python
# Sauvegarde des noms de colonnes et des indices à utiliser lors du stockage en csv
cols = train.columns
train_idx = train.index
valid_idx = valid.index
test_idx = test.index

# normalisation de l'ensemble de données
scaler = MinMaxScaler(feature_range=(0, 1))
train = scaler.fit_transform(train)
valid = scaler.transform(valid)
test = scaler.transform(test)
```

## Sauvegarde des ensembles de données traités

De cette façon, nous n'avons pas besoin de refaire le prétraitement chaque fois que nous relançons le notebook.

```python
train = pd.DataFrame(train, columns=cols, index=train_idx)
valid = pd.DataFrame(valid, columns=cols, index=valid_idx)
test = pd.DataFrame(test, columns=cols, index=test_idx)

train.to_csv('../data/processed/train.csv')
valid.to_csv('../data/processed/valid.csv')
test.to_csv('../data/processed/test.csv')
```

# Modélisation

Tout d'abord, nous lisons les ensembles de données traités. Deuxièmement, nous créons une fonction pour tracer la perte d'entraînement et de validation pour les différents modèles que nous allons construire.

```python
train = pd.read_csv('../data/processed/train.csv', header=0, index_col=0).values.astype('float32')
valid = pd.read_csv('../data/processed/valid.csv', header=0, index_col=0).values.astype('float32')
test = pd.read_csv('../data/processed/test.csv', header=0, index_col=0).values.astype('float32')

def plot_loss(history, title):
    plt.figure(figsize=(10,6))
    plt.plot(history.history['loss'], label='Train')
    plt.plot(history.history['val_loss'], label='Validation')
    plt.title(title)
    plt.xlabel('Nb Epochs')
    plt.ylabel('Loss')
    plt.legend()
    plt.show()
    
    val_loss = history.history['val_loss']
    min_idx = np.argmin(val_loss)
    min_val_loss = val_loss[min_idx]
    print('Minimum validation loss of {} reached at epoch {}'.format(min_val_loss, min_idx))
```

## Préparation des données avec le TimeseriesGenerator

Le [TimeseriesGenerator de Keras](https://keras.io/preprocessing/sequence/#timeseriesgenerator) nous aide à construire les données dans le format correct pour la modélisation.

* **length** : nombre de pas de temps dans la séquence générée. Ici, nous voulons regarder en arrière un nombre arbitraire de _n_lag_ pas de temps. En réalité, n_lag pourrait dépendre de la façon dont les prédictions seront utilisées. Supposons que le gouvernement belge puisse prendre certaines mesures pour réduire la pollution par le SO2 autour d'un point d'échantillonnage (par exemple, interdire l'entrée des voitures diesel dans une ville pendant une certaine période). Et supposons que le gouvernement ait besoin de 14 jours avant que les actions correctives ne puissent entrer en vigueur. Il serait alors logique de définir n_lag à 14.
* **sampling_rate** : nombre de pas de temps entre les pas de temps successifs dans la séquence générée. Nous voulons conserver tous les pas de temps, donc nous laissons cela à la valeur par défaut de 1.
* **stride** : ce paramètre influence la quantité de chevauchement des séquences générées. Comme nous n'avons pas beaucoup de données, nous le laissons à la valeur par défaut de 1. Cela signifie que deux séquences générées l'une après l'autre se chevauchent avec tous les pas de temps sauf un.
* **batch_size** : nombre de séquences générées dans chaque lot

```python
n_lag = 14

train_data_gen = TimeseriesGenerator(train, train, length=n_lag, sampling_rate=1, stride=1, batch_size = 5)
valid_data_gen = TimeseriesGenerator(train, train, length=n_lag, sampling_rate=1, stride=1, batch_size = 1)
test_data_gen = TimeseriesGenerator(test, test, length=n_lag, sampling_rate=1, stride=1, batch_size = 1)
```

## Réseaux de neurones récurrents

**Les réseaux de neurones traditionnels n'ont pas de mémoire**. Par conséquent, ils ne tiennent pas compte de l'entrée précédente lors du traitement de l'entrée actuelle. Dans les ensembles de données séquentielles, comme les séries temporelles, l'information des étapes de temps précédentes est généralement pertinente pour prédire quelque chose dans l'étape actuelle. Donc, un **état** des étapes de temps précédentes doit être maintenu.

Dans notre cas, la pollution atmosphérique à l'instant t pourrait être influencée par la pollution atmosphérique dans les étapes de temps précédentes. Nous devons donc en tenir compte. Les réseaux de neurones récurrents ou RNN ont une boucle interne par laquelle ils maintiennent un état des étapes de temps précédentes. Cet état est ensuite utilisé pour la prédiction dans l'étape de temps actuelle. L'état est réinitialisé lorsqu'une nouvelle séquence est traitée.

Pour un guide illustré sur les RNN, vous devriez définitivement lire l'[article de Michael Nguyen](https://towardsdatascience.com/illustrated-guide-to-recurrent-neural-networks-79e5eb8049c9).

Pour notre cas, nous utilisons un [SimpleRNN](https://keras.io/layers/recurrent/#simplernn) du package Keras. Nous spécifions également un rappel **EarlyStopping** pour arrêter l'entraînement lorsqu'il y a eu 10 époques sans aucune amélioration de la perte de validation. Le **ModelCheckpoint** nous permet de sauvegarder les poids du meilleur modèle. L'architecture du modèle doit encore être sauvegardée séparément.

```python
simple_rnn = Sequential()
simple_rnn.add(SimpleRNN(4, input_shape=(n_lag, 1)))
simple_rnn.add(Dense(1))
simple_rnn.compile(loss='mae', optimizer=RMSprop())

checkpointer = ModelCheckpoint(filepath='../model/simple_rnn_weights.hdf5'
                               , verbose=0
                               , save_best_only=True)
earlystopper = EarlyStopping(monitor='val_loss'
                             , patience=10
                             , verbose=0)
with open("../model/simple_rnn.json", "w") as m:
    m.write(simple_rnn.to_json())

simple_rnn_history = simple_rnn.fit_generator(train_data_gen
                                              , epochs=100
                                              , validation_data=valid_data_gen
                                              , verbose=0
                                              , callbacks=[checkpointer, earlystopper])
plot_loss(simple_rnn_history, 'SimpleRNN - Train & Validation Loss')
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/1_5iUNaezYr3rlTqqmtVm_IA.png)
_Perte d'entraînement et de validation pour un SimpleRNN_

## Réseaux LSTM (Long Short Term Memory)

**Un RNN a une mémoire courte**. Il a du mal à se souvenir des informations de nombreuses étapes de temps auparavant. Cela se produit lorsque les séquences sont très longues.

En fait, cela est dû au **problème du gradient qui disparaît**. Les gradients sont des valeurs qui mettent à jour les poids d'un réseau de neurones. Lorsque vous avez beaucoup d'étapes de temps dans votre RNN, le gradient pour les premières couches devient très petit. Par conséquent, la mise à jour des poids des premières couches est négligeable. Cela signifie que le RNN n'est pas capable d'apprendre ce qui était dans les premières couches.

Nous avons donc besoin d'un moyen de transporter l'information des premières couches vers les couches ultérieures. Les LSTM sont mieux adaptés pour prendre en compte les dépendances à long terme. Michael Nguyen a écrit un excellent article avec une [description visuelle des LSTM](https://towardsdatascience.com/illustrated-guide-to-lstms-and-gru-s-a-step-by-step-explanation-44e9eb85bf21).

## Modèle LSTM simple

```python
simple_lstm = Sequential()
simple_lstm.add(LSTM(4, input_shape=(n_lag, 1)))
simple_lstm.add(Dense(1))
simple_lstm.compile(loss='mae', optimizer=RMSprop())

checkpointer = ModelCheckpoint(filepath='../model/simple_lstm_weights.hdf5'
                               , verbose=0
                               , save_best_only=True)
earlystopper = EarlyStopping(monitor='val_loss'
                             , patience=10
                             , verbose=0)
with open("../model/simple_lstm.json", "w") as m:
    m.write(simple_lstm.to_json())

simple_lstm_history = simple_lstm.fit_generator(train_data_gen
                                                , epochs=100
                                                , validation_data=valid_data_gen
                                                , verbose=0
                                                , callbacks=[checkpointer, earlystopper])
plot_loss(simple_lstm_history, 'Simple LSTM - Train & Validation Loss')

```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/1_5jE6sI6yxkGxQovhcaEC2A.png)
_Perte d'entraînement et de validation pour un LSTM simple_

## Modèle LSTM empilé

Dans ce modèle, nous allons empiler plusieurs couches LSTM. De cette façon, le modèle apprendra d'autres abstractions des données d'entrée au fil du temps. En d'autres termes, **représenter les données d'entrée à différentes échelles de temps**.

Pour ce faire dans Keras, nous devons spécifier le paramètre **return_sequences** dans la couche LSTM précédant une autre couche LSTM.

```python
stacked_lstm = Sequential()
stacked_lstm.add(LSTM(16, input_shape=(n_lag, 1), return_sequences=True))
stacked_lstm.add(LSTM(8, return_sequences=True))
stacked_lstm.add(LSTM(4))
stacked_lstm.add(Dense(1))
stacked_lstm.compile(loss='mae', optimizer=RMSprop())

checkpointer = ModelCheckpoint(filepath='../model/stacked_lstm_weights.hdf5'
                               , verbose=0
                               , save_best_only=True)
earlystopper = EarlyStopping(monitor='val_loss'
                             , patience=10
                             , verbose=0)
with open("../model/stacked_lstm.json", "w") as m:
    m.write(stacked_lstm.to_json())

stacked_lstm_history = stacked_lstm.fit_generator(train_data_gen
                                                  , epochs=100
                                                  , validation_data=valid_data_gen
                                                  , verbose=0
                                                  , callbacks=[checkpointer, earlystopper])
plot_loss(stacked_lstm_history, 'Stacked LSTM - Train & Validation Loss')
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/1_0CBPciBeReSNz2FOfuZJuw.png)
_Perte d'entraînement et de validation pour un LSTM empilé_

# Évaluation des performances

Sur la base des pertes de validation minimales, le SimpleRNN semble surpasser les modèles LSTM, bien que les métriques soient proches les unes des autres.

Avec la méthode **evaluate_generator**, nous pouvons évaluer les modèles sur les données de test (générateur). Cela nous donnera la perte sur les données de test. Nous chargerons d'abord l'architecture du modèle à partir des fichiers JSON et les poids du meilleur modèle.

```python
def eval_best_model(model):
    # Charger l'architecture du modèle à partir du JSON
    model_architecture = open('../model/'+model+'.json', 'r')
    best_model = model_from_json(model_architecture.read())
    model_architecture.close()
    # Charger les poids du meilleur modèle
    best_model.load_weights('../model/'+model+'_weights.hdf5')
    # Compiler le meilleur modèle
    best_model.compile(loss='mae', optimizer=RMSprop())
    # Évaluer sur les données de test
    perf_best_model = best_model.evaluate_generator(test_data_gen)
    print('Loss on test data for {} : {}'.format(model, perf_best_model))

eval_best_model('simple_rnn')
eval_best_model('simple_lstm')
eval_best_model('stacked_lstm')
```

* Loss on test data for simple_rnn: 0.01638169982337905
* Loss on test data for simple_lstm: 0.015934137431135205
* Loss on test data for stacked_lstm: 0.015420083056716116

# Conclusion

Dans cette histoire, nous avons utilisé un réseau de neurones récurrent et deux architectures différentes pour un LSTM. **La meilleure performance provient du LSTM empilé** composé de quelques couches cachées.

Il y a définitivement un certain nombre de choses qui valent la peine d'être étudiées plus avant et qui pourraient améliorer les performances du modèle.

* Utiliser les données horaires (un autre fichier CSV disponible sur le site de l'AEE) et essayer **d'autres stratégies d'échantillonnage** que les données quotidiennes.
* Utiliser les données sur les **autres polluants comme caractéristiques** pour prédire la pollution par le SO2. Peut-être que d'autres polluants sont corrélés à la pollution par le SO2.
* Construire d'autres **caractéristiques basées sur la date**. Un bon article peut être trouvé dans le [PDF de l'un des gagnants](https://github.com/drivendataorg/power-laws-forecasting/blob/master/3rd%20Place/Model_Documentation_and_Write_up.pdf) du concours de prévision des lois de puissance de [Driven Data](https://www.drivendata.org/).

J'ai beaucoup appris sur les réseaux de neurones récurrents en faisant ce projet. J'espère que vous l'avez apprécié. N'hésitez pas à laisser des commentaires !