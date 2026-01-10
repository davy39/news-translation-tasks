---
title: Comment prévoir des données de séries temporelles avec Python Darts
subtitle: ''
author: Adejumo Ridwan Suleiman
co_authors: []
series: null
date: '2025-10-06T18:37:01.578Z'
originalURL: https://freecodecamp.org/news/how-to-forecast-time-series-data-with-python-darts
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1759775700643/6f7d18b3-2060-4708-b56e-3450acf58546.png
tags:
- name: data visualization
  slug: data-visualization
- name: Data Science
  slug: data-science
- name: data analysis
  slug: data-analysis
- name: Machine Learning
  slug: machine-learning
- name: Python
  slug: python
seo_title: Comment prévoir des données de séries temporelles avec Python Darts
seo_desc: 'When analyzing time series data, your main objective is to consider the
  period during which the data is collected and how your variable of interest changes
  over time.

  There are various libraries for time series forecasting in Python, and Darts is
  one...'
---

Lors de l'analyse de données de séries temporelles, votre objectif principal est de prendre en compte la période pendant laquelle les données sont collectées et la manière dont votre variable d'intérêt évolue au fil du temps.

Il existe diverses bibliothèques pour la prévision de séries temporelles en Python, et [Darts](https://unit8co.github.io/darts/) est l'une d'entre elles. Contrairement à d'autres bibliothèques de prévision, Darts est une bibliothèque de prévision de haut niveau dotée d'algorithmes permettant de gérer diverses données de séries temporelles, quel que soit le type de tendance qu'elles affichent.

Ce tutoriel vous guidera à travers la prévision de données de séries temporelles à l'aide de Python Darts. Cela vous aidera à obtenir des informations significatives chaque fois que vous rencontrerez des données de séries temporelles telles que des cours boursiers, des mesures météorologiques, etc.

### Voici ce que nous allons aborder :

* [Qu'est-ce que Python Darts ?](#heading-quest-ce-que-python-darts)
    
* [Prérequis](#heading-prerequis)
    
* [Comment configurer les dépendances](#heading-comment-configurer-les-dependances)
    
* [Comprendre le jeu de données](#heading-comprendre-le-jeu-de-donnees)
    
* [Comment préparer les données pour Darts](#heading-comment-preparer-les-donnees-pour-darts)
    
* [Comment construire un modèle de prévision](#heading-comment-construire-un-modele-de-prevision)
    
    * [Modèle classique](#heading-modele-classique)
        
    * [Modèles de Machine Learning](#heading-modeles-de-machine-learning)
        
    * [Comment effectuer des prévisions avec des modèles de Deep Learning](#heading-comment-effectuer-des-previsions-avec-des-modeles-de-deep-learning)
        
* [Évaluation du modèle](#heading-evaluation-du-modele)
    
* [Backtesting](#heading-backtesting)
    
* [Réglage des hyperparamètres](#heading-reglage-des-hyperparametres)
    
* [Cas d'utilisation réels](#heading-cas-dutilisation-reels)
    
* [Bonnes pratiques](#heading-bonnes-pratiques)
    
* [Conclusion](#heading-conclusion)
    

## Qu'est-ce que Python Darts ?

Python Darts est une bibliothèque open-source pour l'analyse et la prévision de séries temporelles. Elle dispose de divers modèles allant des modèles statistiques de séries temporelles comme ARIMA et SARIMA, aux modèles de Machine Learning et de Deep Learning comme Prophet et LSTM.

Elle possède divers algorithmes pour gérer les imputations manquantes dans les données de séries temporelles et peut traiter des problèmes de séries temporelles allant de l'univarié et du multivarié aux séries temporelles hiérarchiques.

## Prérequis

Avant de continuer, vous devrez disposer des éléments suivants :

* Python 3.9+ installé.
    
* Jupyter Notebook, Google Colab ou Positron pour exécuter votre code.
    
* Télécharger les [données boursières de Netflix](https://www.kaggle.com/datasets/kalilurrahman/netflix-stock-data-live-and-latest).
    
* Avoir installé les bibliothèques suivantes :
    
    * `darts` pour l'analyse des séries temporelles
        
    * `pandas` pour la manipulation des données (data wrangling)
        
    * `matplotlib` pour la visualisation des données.
        

## Comment configurer les dépendances

Chargez les bibliothèques suivantes.

```python
import matplotlib.pyplot as plt
import pandas as pd
import darts
from darts import TimeSeries
from darts.models import ARIMA
from darts.models import RegressionModel
from lightgbm import LGBMRegressor
from darts.models import RNNModel
from darts.metrics import mape
import itertools
```

## Comprendre le jeu de données

Les données boursières de Netflix contiennent les cours quotidiens historiques de l'action Netflix de l'année 2002 à aujourd'hui.

Chargez les données et visualisez-en un aperçu.

```python
netflix = pd.read_csv("/kaggle/input/netflix-stock-data-live-and-latest/Netflix_stock_history.csv")
netflix['Date'] = pd.to_datetime(netflix['Date'], utc=True).dt.tz_convert(None)
netflix.head()
```

![Image montrant les 5 premières lignes des données boursières de Netflix](https://cdn.hashnode.com/res/hashnode/image/upload/v1757927775470/2d4b542c-3869-40c5-844c-a733b5cc4bea.png align="center")

Pour prévoir des données de séries temporelles, nous avons besoin d'une colonne `Date`, que nous avons déjà, puis de la variable d'intérêt. Nous avons plusieurs variables, mais pour ce tutoriel, nous nous concentrerons sur la variable `Close` (clôture) des actions Netflix.

Visualisons les données pour voir comment le cours de clôture de Netflix a évolué au fil des ans.

```python
netflix.plot(x='Date', y='Close', figsize=(10,5))
plt.show()
```

![Image montrant un graphique linéaire des données boursières de Netflix de 2000 à aujourd'hui](https://cdn.hashnode.com/res/hashnode/image/upload/v1757928810807/75a1fa13-4f2e-4bdd-a539-5eaf2663843a.png align="center")

D'après le graphique ci-dessus, vous pouvez voir que l'action Netflix a affiché une croissance exponentielle ces dernières années. Cela signifie que les données sont non stationnaires, ce qui implique qu'il n'y a pas de changements constants au fil du temps.

Il y a beaucoup de fluctuations aléatoires dans les données, ce qui peut rendre la prévision difficile. De telles données nécessitent généralement des modèles avancés pour gérer les diverses fluctuations ou le bruit présents dans les données.

## **Comment préparer les données pour Darts**

Avant de préparer les données pour Darts, vous devez prendre note de quelques points.

Tout d'abord, si vous regardez notre aperçu des données plus tôt, vous remarquerez qu'elles sont enregistrées quotidiennement ; nous devons également remplir les dates manquantes.

Copiez et collez ce code dans votre notebook.

```python
start = netflix['Date'].min()
end = netflix['Date'].max()

netflix = (
    netflix.set_index('Date')
           .reindex(pd.date_range(start=start, end=end, freq='D'))
           .ffill()
           .reset_index()
           .rename(columns={'index': 'Date'})
)
netflix.head()
```

Le code ci-dessus garantit que le jeu de données `netflix` possède une série temporelle quotidienne continue en remplissant les dates manquantes.

Tout d'abord, il trouve les dates de début (`start`) et de fin (`end`) les plus anciennes et les plus récentes dans les données, puis crée une plage de dates quotidienne complète entre elles.

En définissant la colonne `Date` comme index et en utilisant la méthode `.reindex()`, il insère des lignes pour toutes les dates manquantes, qui contiennent initialement `NaN`.

La méthode `.ffill()` (forward fill ou remplissage vers l'avant) remplace ces lacunes en reportant la dernière valeur connue, ce qui est courant pour les données boursières lorsque les marchés sont fermés, comme les week-ends.

Enfin, l'index est réinitialisé et la colonne est renommée `Date`, produisant un jeu de données propre et continu prêt pour l'analyse de séries temporelles.

Ensuite, nous devons convertir les données en un objet `TimeSeries` de Darts pour les rendre utilisables par la bibliothèque Darts.

```python
series = TimeSeries.from_dataframe(
    netflix,
    time_col='Date',
    value_cols='Close',
)
```

Le code ci-dessus convertit le DataFrame `netflix` en un objet `TimeSeries` de Darts, qui est optimisé pour la modélisation et la prévision de séries temporelles.

Il prend la colonne `Date` (`time_col='Date'`) comme chronologie et la colonne `Close` (`value_cols='Close'`) comme valeurs cibles à prévoir.

L'objet `series` résultant est maintenant structuré pour être utilisé avec les modèles de prévision avancés de Darts comme ARIMA, Prophet, les RNN et d'autres algorithmes de séries temporelles.

Tout comme vous le feriez avec n'importe quel autre modèle de Machine Learning, vous devez diviser vos données en un ensemble d'entraînement et un ensemble de validation.

```python
train, val = series.split_before(0.8)
```

## **Comment construire un modèle de prévision**

Lors de la construction d'un modèle de prévision, vous avez le privilège d'essayer divers modèles et de choisir celui qui est le plus performant.

La bibliothèque Darts dispose de divers algorithmes pour l'analyse des séries temporelles, allant des algorithmes statistiques populaires comme les modèles Auto Regressive Integrated Moving Average (ARIMA) et Moving Average (MA), aux algorithmes de Machine Learning et de Deep Learning comme Prophet et Long Short Term Memory (LSTM).

Notez que je vais seulement démontrer le fonctionnement de ces algorithmes - il n'est pas nécessaire que nous obtenions des métriques de modèle précises. Mais avec une ingénierie des caractéristiques (feature engineering) plus poussée, un réglage des hyperparamètres et une validation croisée, vous pouvez obtenir de bons résultats par vous-même.

### Modèle classique

Le mode classique consiste à utiliser des modèles statistiques de séries temporelles tels qu'ARIMA. ARIMA est composé des éléments suivants :

* **AR (AutoRegressive) :** Prédit les valeurs passées en examinant les précédentes.
    
* **I (Integrated) :** Supprime les tendances en se concentrant sur les changements plutôt que sur les valeurs brutes.
    
* **MA (Moving Average) :** Apprend des erreurs des prédictions passées pour améliorer la précision.
    

Exécutez le code ci-dessous dans votre notebook pour ajuster un modèle ARIMA.

```python
arima_model = ARIMA()
arima_model.fit(train)
arima_forecast = arima_model.predict(len(val))
```

Pour visualiser la prévision du modèle, appelez la méthode `.plot()` sur l'objet `forecast`.

```python
series.plot(label='actual')
arima_forecast.plot(label='forecast')
plt.legend()
```

![Image montrant la prévision du modèle ARIMA pour l'action Netflix](https://cdn.hashnode.com/res/hashnode/image/upload/v1758028284156/a40f2341-cfc6-4a9f-8297-e0511c2bb254.png align="center")

Vous pouvez améliorer le modèle en ajoutant des paramètres supplémentaires à la classe `ARIMA()`. Vous pouvez en savoir plus à ce sujet dans la [documentation de Darts](https://unit8co.github.io/darts/generated_api/darts.models.forecasting.arima.html).

### **Modèles de Machine Learning**

Les modèles classiques comme ARIMA ne peuvent pas gérer les données non linéaires. Les modèles de Machine Learning comblent cette lacune. Nous utiliserons le modèle LightGBM comme exemple.

LightGBM est un modèle de Machine Learning qui construit des modèles séquentiellement basés sur des arbres de décision. Il ajoute de nouveaux arbres de décision qui corrigent les erreurs des arbres précédents.

Bien qu'il n'ait pas été conçu pour gérer les séries temporelles, avec un peu d'ingénierie des caractéristiques comme les retards (lags), les statistiques glissantes et les indicateurs saisonniers, vous pouvez lui faire apprendre des motifs à partir de données de séries temporelles.

Exécutez ce code sur votre notebook pour ajuster un modèle LightGBM sur les données Netflix.

```python
lgbm = LGBMRegressor()
lgbm_model = RegressionModel(lags=12, model=lgbm)
lgbm_model.fit(train)
lgbm_forecast = lgbm_model.predict(len(val))
```

D'après le code ci-dessus, l'argument `lag` est défini sur `12`, ce qui correspond à la valeur du cours de l'action Netflix pendant 12 jours avant un jour sélectionné.

Jetons un coup d'œil à la prévision en exécutant le code suivant.

```python
series.plot(label='actual')
lgbm_forecast.plot(label='forecast')
plt.legend()
```

![Image montrant la prévision du modèle LightGBM pour l'action Netflix](https://cdn.hashnode.com/res/hashnode/image/upload/v1758029933172/54f34a69-4f6b-4b44-85ab-d0b45931d701.png align="center")

Vous pouvez en savoir plus sur le réglage du modèle LightGBM dans la [documentation de Darts](https://unit8co.github.io/darts/generated_api/darts.models.forecasting.lgbm.html) pour améliorer le modèle ci-dessus.

### **Comment effectuer des prévisions avec des modèles de Deep Learning**

Vous pouvez opter pour des modèles de Deep Learning conçus pour les séries temporelles, tels que LSTM, un type de réseau de neurones récurrents (RNN) conçu pour capturer les dépendances à long terme dans les données séquentielles.

Exécutez le code suivant pour construire le modèle LSTM.

```python
lstm_model = RNNModel(model='LSTM', input_chunk_length=12, output_chunk_length=6, n_epochs=100)
lstm_model.fit(train)
lstm_forecast = lstm_model.predict(len(val))
```

Maintenant, visualisons la prévision et voyons ce que nous obtenons.

```python
series.plot(label='actual')
lstm_forecast.plot(label='forecast')
plt.legend()
```

![Image montrant la prévision du modèle LSTM pour l'action Netflix](https://cdn.hashnode.com/res/hashnode/image/upload/v1758116174578/2ff80218-2254-452d-8d4c-2f85c61612de.png align="center")

Vous pouvez consulter la [documentation de Darts](https://unit8co.github.io/darts/generated_api/darts.models.forecasting.rnn_model.html) pour améliorer le modèle et découvrir également d'autres modèles de Deep Learning.

## **Évaluation du modèle**

Maintenant que vous avez trois modèles, vous devez sélectionner le meilleur d'entre eux en utilisant l'erreur de pourcentage absolue moyenne (MAPE).

Elle exprime l'erreur absolue moyenne en pourcentage des valeurs réelles, et plus votre valeur est proche de 0, meilleur est votre modèle.

Exécutez ce qui suit pour imprimer la MAPE de chaque modèle respectif.

```python
arima_error = mape(val, arima_forecast)
print("MAPE:", arima_error)
lgbm_error = mape(val, lgbm_forecast)
print("MAPE:", lgbm_error)
lstm_error = mape(val, lstm_forecast)
print("MAPE:", lstm_error)
```

```bash
> MAPE: 38.33262525601514
> MAPE: 39.00241495209449
> MAPE: 38.82910057097827
```

Le modèle avec la MAPE la plus basse est le modèle ARIMA avec environ 38,33, ce qui signifie que c'est notre modèle le plus performant.

## Backtesting

Darts dispose d'une fonctionnalité appelée backtesting qui vous permet d'évaluer vos modèles sur la base de données historiques, en utilisant une prévision glissante.

Le backtesting est comme une machine à remonter le temps pour la prévision. Il simule la performance qu'aurait eue votre modèle dans le passé en l'entraînant de manière répétée sur des données historiques jusqu'à un certain point, en faisant une prédiction pour l'étape suivante, puis en avançant et en répétant le processus.

Cette évaluation glissante simule le comportement du modèle dans des conditions réelles, où les données futures sont inconnues, vous aidant à mesurer sa cohérence et sa fiabilité au fil du temps, au lieu de simplement le tester une seule fois sur un seul ensemble de validation.

Étant donné que le modèle ARIMA est actuellement notre modèle le plus performant, exécutez le code ci-dessous pour implémenter le backtesting.

```python

# Effectuer le backtesting sur la série d'entraînement + validation
backtest_series = train.concatenate(val)

# Backtest
backtest_forecast = arima_model.historical_forecasts(
    series=backtest_series,
    start=0.8,          # fraction de la série à partir de laquelle commencer la prévision
    forecast_horizon=len(val),
    stride=1,           # taille du pas de la prévision glissante
    retrain=True,       # réentraîner le modèle à chaque étape
    verbose=True
)

# Calculer les métriques
error = mape(backtest_series[-len(val):], backtest_forecast)
print(f"MAPE: {error:.2f}%")
```

```bash
> historical forecasts: 100%|██████████| 1/1 [00:02<00:00,  2.69s/it]MAPE: 47.27%
```

Dans le code ci-dessus,

* L'argument `start` définit où commencer le backtesting, qui dans ce cas est les derniers 20 % de la série de données.
    
* Le `forecast_horizon` est le nombre d'étapes à prévoir à chaque point.
    
* Le `stride` est la fréquence de réentraînement/prévision.
    
* `retrain=True` réajuste le modèle à chaque étape pour une évaluation réaliste.
    

Vous pouvez voir que la MAPE, après backtesting, est plus élevée car le backtesting est plus réaliste, et il est plus difficile d'obtenir une MAPE plus basse.

De votre côté, vous pouvez essayer de reproduire le backtesting pour les autres modèles.

## Réglage des hyperparamètres

Le modèle ARIMA possède trois hyperparamètres :

* `p` qui est l'ordre AR
    
* `d` qui est l'ordre de différenciation
    
* `q` qui est l'ordre MA
    

Vous pouvez utiliser soit une recherche par grille (grid search), soit une recherche aléatoire (random search) pour régler votre modèle ARIMA dans Darts.

```python
# Définir les valeurs possibles
p_values = range(0, 4)
d_values = range(0, 3)
q_values = range(0, 4)

best_mape = float('inf')
best_params = None

for p, d, q in itertools.product(p_values, d_values, q_values):
    try:
        arima_model = ARIMA(p=p, d=d, q=q)
        arima_model.fit(train)
        arima_forecast = arima_model.predict(len(val))
        arima_error = mape(val, arima_forecast)
        if arima_error < best_mape:
            best_mape = arima_error
            best_params = (p, d, q)
    except Exception as e:
        # Certaines combinaisons peuvent échouer
        continue

print(f"Best ARIMA params: p={best_params[0]}, d={best_params[1]}, q={best_params[2]} with MAPE={best_mape:.2f}%")
```

```bash
> Best ARIMA params: p=2, d=0, q=3 with MAPE=35.95%
```

Dans le code ci-dessus, vous définissez une plage de valeurs possibles pour les composants `p`, `d` et `q`, en itérant sur chaque combinaison de ces valeurs et en choisissant le modèle avec la meilleure MAPE parmi elles.

Notez que chaque modèle possède ses paramètres spécifiques que vous devrez régler, et vous devrez consulter [la documentation de Darts](https://unit8co.github.io/darts/userguide/hyperparameter_optimization.html) pour les hyperparamètres des autres modèles.

## **Cas d'utilisation réels**

La prévision de données de séries temporelles a de nombreuses applications dans le monde réel, dont certaines sont :

* **Prédiction du cours des actions :** Comme le jeu de données utilisé dans ce tutoriel, la prévision est utilisée en finance pour la prédiction du cours des actions, permettant aux investisseurs de gérer les risques.
    
* **Prévision de la demande pour les stocks :** En tant que propriétaire de magasin, vous pouvez prévoir la demande de produits en fonction des ventes passées d'un produit. Cela vous permet de connaître les produits qui sont en forte demande.
    
* **Prédiction de la consommation d'énergie :** Les gouvernements, les industries et les consommateurs peuvent planifier et gérer efficacement la production, la distribution et la consommation d'énergie, sur la base des données d'utilisation passées. Cela aide à éviter les pannes et le gaspillage, leur permettant de se préparer à l'avance.
    

## Bonnes pratiques

* **Toujours visualiser les résidus :** Les résidus sont la différence entre les valeurs prévues et les valeurs réelles. Vous devez les visualiser pour détecter les valeurs aberrantes et les événements inhabituels.
    
* **Effectuer un backtesting approprié :** Le backtesting vous permet de voir un modèle plus réaliste, soumis aux divers changements qui peuvent survenir dans la vie réelle. Lorsque vous effectuez un backtesting sur tous vos modèles, vous finissez par obtenir un modèle qui fonctionne bien lors de la prévision.
    
* **Éviter la fuite de données (data leakage) :** Ne formez pas vos modèles sur des ensembles de validation pour éviter les biais, et utilisez toujours la validation croisée si nécessaire.
    
* **Utiliser les connaissances du domaine pour l'ingénierie des caractéristiques :** Assurez-vous de comprendre les données avec lesquelles vous travaillez. Cela s'avère utile dans l'ingénierie des caractéristiques, lorsque vous souhaitez proposer de nouvelles caractéristiques pour aider votre modèle de prévision, en particulier dans la prévision de séries temporelles multivariées.
    

## **Conclusion**

Ce tutoriel est plutôt un aperçu, surtout si vous débutez dans les séries temporelles, mais vous pouvez construire beaucoup de choses à partir de ce que vous avez appris.

Vous avez déjà une idée de ce que sont les séries temporelles et la prévision, et comment vous pouvez utiliser la bibliothèque Python Darts pour y parvenir.

Vous avez également découvert divers modèles pour la prévision de données de séries temporelles, et comment vous pouvez appliquer des techniques telles que le backtesting et le réglage des hyperparamètres pour obtenir de meilleurs résultats.

Une autre chose intéressante avec Darts est sa capacité à gérer les [séries temporelles hiérarchiques](https://unit8co.github.io/darts/userguide/timeseries.html#hierarchical-time-series). Ici, les données sont structurées à des niveaux agrégés.

Darts est l'une des bibliothèques de séries temporelles les plus puissantes en Python et dispose de nombreux modèles pour gérer divers cas. Vous pouvez continuer à explorer des modèles tels que les [Transformers](https://unit8co.github.io/darts/generated_api/darts.models.forecasting.transformer_model.html) ainsi que la [prévision multi-séries](https://unit8co.github.io/darts/examples/01-multi-time-series-and-covariates.html), qui sont utilisés pour des cas d'utilisation spéciaux.

Si vous êtes intéressé par d'autres articles sur la science des données et les statistiques, n'oubliez pas de consulter [mon blog](https://learndata.xyz/blog).