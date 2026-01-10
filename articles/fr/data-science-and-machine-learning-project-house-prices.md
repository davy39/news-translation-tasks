---
title: Projet de Machine Learning – Comment analyser et nettoyer des données, créer
  un modèle de ML et configurer une API
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-02-18T23:27:10.000Z'
originalURL: https://freecodecamp.org/news/data-science-and-machine-learning-project-house-prices
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/banner_cover.png
tags:
- name: api
  slug: api
- name: data analysis
  slug: data-analysis
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
seo_title: Projet de Machine Learning – Comment analyser et nettoyer des données,
  créer un modèle de ML et configurer une API
seo_desc: 'By Renan Moura Ferreira

  In this article, we''ll use Data Science and Machine Learning tools to analyze data
  from a house prices dataset.

  We will begin by performing Exploratory Data Analysis on the data. We''ll create
  a script to clean the data, then w...'
---

Par Renan Moura Ferreira

Dans cet article, nous allons utiliser des outils de Data Science et de Machine Learning pour analyser des données provenant d'un ensemble de données sur les prix des maisons.

Nous commencerons par effectuer une analyse exploratoire des données (EDA). Nous créerons un script pour nettoyer les données, puis nous utiliserons les données nettoyées pour créer un modèle de Machine Learning. Enfin, nous utiliserons le modèle de Machine Learning pour implémenter notre propre API de prédiction.

Le code source complet se trouve dans le dépôt GitHub avec des instructions claires pour exécuter ce projet de bout en bout.


Info rapide : Vous pouvez [télécharger une version PDF de ce projet de Data Science et de Machine Learning avec le dépôt de code source complet lié dans le livre](https://renanmf.com/book-ds-ml-project-house-prices/).

Prêt à plonger ?

## Table des matières

1. [Dépôt GitHub](#heading-depot-github)
2. [EDA (Analyse Exploratoire des Données)](#heading-analyse-exploratoire-des-donnees)
3. [Script de Nettoyage des Données](#heading-script-de-nettoyage-des-donnees)
4. [Modèle de Machine Learning](#machinelearningmodel)
5. [API](#api)
6. [Conclusion](#heading-conclusion)

## Dépôt GitHub

Vous pouvez télécharger le code complet dans le [Dépôt GitHub](https://github.com/renanmouraf/data-science-house-prices).

Dans le dépôt, vous trouverez :

* requirements.txt : Les packages que vous devez installer en utilisant pip
* raw_data.csv : Les données brutes que nous utilisons dans ce projet
* Exploratory-Data-Analysis-House-Prices.ipynb : Le notebook Jupyter avec l'analyse exploratoire des données
* data_cleaning.py : Le script qui nettoie les données
* train_model.py : Le script pour entraîner le modèle de Machine Learning en utilisant les données nettoyées
* predict.py : Le fichier avec la classe HousePriceModel que nous utilisons pour charger le modèle ML et faire les prédictions
* api.py : L'API créée avec le framework [FastAPI](https://fastapi.tiangolo.com/)
* test_api.py : Le script pour tester l'API

Pour utiliser les données et le code dans le dépôt, suivez les étapes dans les sections suivantes.

### Environnement et Packages
Créez un environnement virtuel pour isoler votre projet Python :

```
python3 -m venv venv
```

Activez l'environnement virtuel comme ceci :

```
source ./venv/bin/activate
```

Puis installez les packages nécessaires :

```
pip install -r requirements.txt
```

Vous devriez voir un message similaire à ceci à la fin :

```
Successfully installed Babel-2.9.0 Jinja2-2.11.3 MarkupSafe-1.1.1 Pygments-2.8.0 Send2Trash-1.5.0 anyio-2.1.0 argon2-cffi-20.1.0 async-generator-1.10 attrs-20.3.0 backcall-0.2.0 bleach-3.3.0 certifi-2020.12.5 cffi-1.14.5 chardet-4.0.0 click-7.1.2 decorator-4.4.2 defusedxml-0.6.0 entrypoints-0.3 fastapi-0.63.0 h11-0.12.0 idna-2.10 ipykernel-5.4.3 ipython-7.20.0 ipython-genutils-0.2.0 jedi-0.18.0 joblib-1.0.1 json5-0.9.5 jsonschema-3.2.0 jupyter-client-6.1.11 jupyter-core-4.7.1 jupyter-server-1.3.0 jupyterlab-3.0.7 jupyterlab-pygments-0.1.2 jupyterlab-server-2.2.0 mistune-0.8.4 nbclassic-0.2.6 nbclient-0.5.2 nbconvert-6.0.7 nbformat-5.1.2 nest-asyncio-1.5.1 notebook-6.2.0 numpy-1.20.1 packaging-20.9 pandas-1.2.2 pandocfilters-1.4.3 parso-0.8.1 pexpect-4.8.0 pickleshare-0.7.5 prometheus-client-0.9.0 prompt-toolkit-3.0.16 ptyprocess-0.7.0 pycparser-2.20 pydantic-1.7.3 pyparsing-2.4.7 pyrsistent-0.17.3 python-dateutil-2.8.1 pytz-2021.1 pyzmq-22.0.3 requests-2.25.1 scikit-learn-0.24.1 scipy-1.6.0 six-1.15.0 sniffio-1.2.0 starlette-0.13.6 terminado-0.9.2 testpath-0.4.4 threadpoolctl-2.1.0 tornado-6.1 traitlets-5.0.5 urllib3-1.26.3 uvicorn-0.13.3 wcwidth-0.2.5 webencodings-0.5.1
```

### EDA (Analyse Exploratoire des Données)
Pour consulter l'EDA (Analyse Exploratoire des Données) :

```
jupyter-notebook Exploratory-Data-Analysis-House-Prices.ipynb
```

Ensuite, avec le notebook Jupyter ouvert, allez dans `Cell > Run All` pour exécuter toutes les commandes.

Puis exécutez les étapes suivantes dans cet ordre.

#### Nettoyer les Données

Pour effectuer le processus de nettoyage sur les données brutes, tapez la commande suivante :

```
python data_cleaning.py
```

Voici le résultat attendu :

```
Original Data: (1168, 81)
Columns with missing values: 0
Series([], dtype: int64)
After Cleaning: (1168, 73)
```

Cela générera le fichier 'cleaned_data.csv'.

#### Créer le Modèle de Machine Learning

Pour entraîner le modèle, entrez cette commande :

```
python train_model.py
```

Voici le résultat attendu :

```
Train data for modeling: (934, 73)
Test data for predictions: (234, 73)
Training the model ...
Testing the model ...
Average Price Test: 175652.0128205128
RMSE: 11098.009355519898
Model saved at model.pkl
```

Cela créera les fichiers 'train.csv', 'test.csv', et 'model.pkl'.

#### Exécuter et tester l'API

Pour exécuter l'API, tapez cette commande :

```
uvicorn api:app
```

Voici le résultat attendu :

```
INFO:     Started server process [56652]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

Pour tester l'API, sur un autre terminal, activez à nouveau l'environnement virtuel (cette fois, vous avez déjà les packages installés) :

```
source ./venv/bin/activate
```

Puis exécutez :

```
python test_api.py
```

Voici le résultat attendu :

```
The actual Sale Price: 109000
The predicted Sale Price: 109000.01144237864
```

# Analyse Exploratoire des Données

Commençons par une Analyse Exploratoire des Données, également connue sous le nom d'EDA, de l'ensemble de données "[House Prices: Advanced Regression Techniques](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data)".

Nous allons :

* Comprendre le problème
* Explorer les données et traiter les valeurs manquantes
* Sélectionner et transformer les variables, en particulier les variables catégorielles

## Le Problème

Voici la description du problème sur Kaggle :

"Demandez à un acheteur de maison de décrire sa maison de rêve, et il ne commencera probablement pas par la hauteur du plafond du sous-sol ou la proximité d'une voie ferrée est-ouest. Mais l'ensemble de données de cette compétition de jeu prouve que bien plus influence les négociations de prix que le nombre de chambres ou une clôture blanche.

Avec 79 variables explicatives décrivant (presque) tous les aspects des maisons résidentielles à Ames, Iowa, cette compétition vous défie de prédire le prix final de chaque maison."

Ainsi, nous allons explorer l'ensemble de données, essayer d'en tirer quelques informations, et utiliser quelques outils pour transformer les données en formats qui ont plus de sens.

## Exploration Initiale et Premières Informations

Dans cette section, nous allons faire une exploration initiale de l'ensemble de données.

Cette EDA a été réalisée sur un [Jupyter Notebook](https://jupyter.org/).

### Importation des Bibliothèques

Nous commençons par importer les bibliothèques que nous allons utiliser :

* Le module standard [math](https://docs.python.org/3/library/math.html) fournit un accès aux fonctions mathématiques.
* La bibliothèque [NumPy](https://numpy.org/) est fondamentale pour tout type de calcul scientifique avec Python.
* [pandas](https://pandas.pydata.org/) est un outil indispensable pour l'analyse et la manipulation des données.
* [matplotlib](https://matplotlib.org/) est le package le plus complet en Python en matière de visualisations de données.
* [seaborn](https://seaborn.pydata.org/) est basé sur matplotlib comme un ensemble de outils de visualisation de niveau supérieur, pas aussi puissant que matplotlib, mais beaucoup plus facile à utiliser et livre beaucoup avec moins de travail.


```python
import math
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt

%matplotlib inline
```

### Chargement des Données

Puisque nous avons des données tabulaires, nous allons utiliser _pandas_ pour charger les données et jeter un premier coup d'œil.

Pour charger les données, puisque le format est CSV (Comma-Separated Values), nous utilisons la fonction `read_csv()` de pandas.

Ensuite, nous imprimons sa forme, qui est 1168x81, ce qui signifie que nous avons 1168 lignes (enregistrements) et 81 colonnes (caractéristiques).

En fait, nous avons 1169 lignes dans le fichier CSV, mais l'en-tête qui décrit les colonnes ne compte pas.

Et nous avons en fait 79 caractéristiques puisque l'une des colonnes est `SalePrice`, qui est la colonne que nous allons essayer de prédire dans un modèle, et nous n'allons pas non plus utiliser la colonne `Id` et nous allons nous en débarrasser plus tard.

```python
train = pd.read_csv('raw_data.csv')
train.shape
```

```
    (1168, 81)
```

### Regarder les Données

Tout d'abord, je vous recommande de lire [cette brève description de chaque colonne](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data).

En utilisant la fonction `head()` de pandas avec un argument de 3, nous pouvons jeter un coup d'œil aux 3 premiers enregistrements.

Le `.T` signifie _Transpose_, de cette façon nous visualisons les lignes comme des colonnes et vice-versa.

Remarquez comment il ne montre pas toutes les colonnes du milieu et n'affiche que `...` parce qu'il y en a trop.

```python
train.head(3).T
```

<div>
<table>
  <thead>
    <tr>
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Id</th>
      <td>893</td>
      <td>1106</td>
      <td>414</td>
    </tr>
    <tr>
      <th>MSSubClass</th>
      <td>20</td>
      <td>60</td>
      <td>30</td>
    </tr>
    <tr>
      <th>MSZoning</th>
      <td>RL</td>
      <td>RL</td>
      <td>RM</td>
    </tr>
    <tr>
      <th>LotFrontage</th>
      <td>70</td>
      <td>98</td>
      <td>56</td>
    </tr>
    <tr>
      <th>LotArea</th>
      <td>8414</td>
      <td>12256</td>
      <td>8960</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>MoSold</th>
      <td>2</td>
      <td>4</td>
      <td>3</td>
    </tr>
    <tr>
      <th>YrSold</th>
      <td>2006</td>
      <td>2010</td>
      <td>2010</td>
    </tr>
    <tr>
      <th>SaleType</th>
      <td>WD</td>
      <td>WD</td>
      <td>WD</td>
    </tr>
    <tr>
      <th>SaleCondition</th>
      <td>Normal</td>
      <td>Normal</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>SalePrice</th>
      <td>154500</td>
      <td>325000</td>
      <td>115000</td>
    </tr>
  </tbody>
</table>
<p>81 rows × 3 columns</p>
</div>


La méthode `info()` de pandas vous donnera un résumé des données.

Remarquez comment `Alley` a 70 valeurs non nulles, ce qui signifie qu'elle n'a pas de valeur pour la plupart des 1168 enregistrements.

Nous pouvons également visualiser les types de données.


```python
train.info()
```

```
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 1168 entries, 0 to 1167
    Data columns (total 81 columns):
    Id               1168 non-null int64
    MSSubClass       1168 non-null int64
    MSZoning         1168 non-null object
    LotFrontage      964 non-null float64
    LotArea          1168 non-null int64
    Street           1168 non-null object
    Alley            70 non-null object
    LotShape         1168 non-null object
    LandContour      1168 non-null object
    Utilities        1168 non-null object
    LotConfig        1168 non-null object
    LandSlope        1168 non-null object
    Neighborhood     1168 non-null object
    Condition1       1168 non-null object
    Condition2       1168 non-null object
    BldgType         1168 non-null object
    HouseStyle       1168 non-null object
    OverallQual      1168 non-null int64
    OverallCond      1168 non-null int64
    YearBuilt        1168 non-null int64
    YearRemodAdd     1168 non-null int64
    RoofStyle        1168 non-null object
    RoofMatl         1168 non-null object
    Exterior1st      1168 non-null object
    Exterior2nd      1168 non-null object
    MasVnrType       1160 non-null object
    MasVnrArea       1160 non-null float64
    ExterQual        1168 non-null object
    ExterCond        1168 non-null object
    Foundation       1168 non-null object
    BsmtQual         1138 non-null object
    BsmtCond         1138 non-null object
    BsmtExposure     1137 non-null object
    BsmtFinType1     1138 non-null object
    BsmtFinSF1       1168 non-null int64
    BsmtFinType2     1137 non-null object
    BsmtFinSF2       1168 non-null int64
    BsmtUnfSF        1168 non-null int64
    TotalBsmtSF      1168 non-null int64
    Heating          1168 non-null object
    HeatingQC        1168 non-null object
    CentralAir       1168 non-null object
    Electrical       1167 non-null object
    1stFlrSF         1168 non-null int64
    2ndFlrSF         1168 non-null int64
    LowQualFinSF     1168 non-null int64
    GrLivArea        1168 non-null int64
    BsmtFullBath     1168 non-null int64
    BsmtHalfBath     1168 non-null int64
    FullBath         1168 non-null int64
    HalfBath         1168 non-null int64
    BedroomAbvGr     1168 non-null int64
    KitchenAbvGr     1168 non-null int64
    KitchenQual      1168 non-null object
    TotRmsAbvGrd     1168 non-null int64
    Functional       1168 non-null object
    Fireplaces       1168 non-null int64
    FireplaceQu      617 non-null object
    GarageType       1099 non-null object
    GarageYrBlt      1099 non-null float64
    GarageFinish     1099 non-null object
    GarageCars       1168 non-null int64
    GarageArea       1168 non-null int64
    GarageQual       1099 non-null object
    GarageCond       1099 non-null object
    PavedDrive       1168 non-null object
    WoodDeckSF       1168 non-null int64
    OpenPorchSF      1168 non-null int64
    EnclosedPorch    1168 non-null int64
    3SsnPorch        1168 non-null int64
    ScreenPorch      1168 non-null int64
    PoolArea         1168 non-null int64
    PoolQC           4 non-null object
    Fence            217 non-null object
    MiscFeature      39 non-null object
    MiscVal          1168 non-null int64
    MoSold           1168 non-null int64
    YrSold           1168 non-null int64
    SaleType         1168 non-null object
    SaleCondition    1168 non-null object
    SalePrice        1168 non-null int64
    dtypes: float64(3), int64(35), object(43)
    memory usage: 739.2+ KB
```

La méthode `describe()` est bonne pour avoir les premières informations sur les données.

Elle vous donne automatiquement des statistiques descriptives pour chaque caractéristique : nombre d'observations non-NA/null, _moyenne_, _écart-type_, la valeur _min_, les _quartiles_, et la valeur _max_.

Notez que les calculs ne prennent pas en compte les valeurs `NaN`.

Pour `LotFrontage`, par exemple, il utilise seulement les 964 valeurs non nulles, et exclut les 204 autres observations nulles.


```python
train.describe().T
```

<div style="font-size: 10;">
<table>
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Id</th>
      <td>1168.0</td>
      <td>720.240582</td>
      <td>420.237685</td>
      <td>1.0</td>
      <td>355.75</td>
      <td>716.5</td>
      <td>1080.25</td>
      <td>1460.0</td>
    </tr>
    <tr>
      <th>MSSubClass</th>
      <td>1168.0</td>
      <td>56.699486</td>
      <td>41.814065</td>
      <td>20.0</td>
      <td>20.00</td>
      <td>50.0</td>
      <td>70.00</td>
      <td>190.0</td>
    </tr>
    <tr>
      <th>LotFrontage</th>
      <td>964.0</td>
      <td>70.271784</td>
      <td>25.019386</td>
      <td>21.0</td>
      <td>59.00</td>
      <td>69.5</td>
      <td>80.00</td>
      <td>313.0</td>
    </tr>
    <tr>
      <th>LotArea</th>
      <td>1168.0</td>
      <td>10597.720890</td>
      <td>10684.958323</td>
      <td>1477.0</td>
      <td>7560.00</td>
      <td>9463.0</td>
      <td>11601.50</td>
      <td>215245.0</td>
    </tr>
    <tr>
      <th>OverallQual</th>
      <td>1168.0</td>
      <td>6.095034</td>
      <td>1.403402</td>
      <td>1.0</td>
      <td>5.00</td>
      <td>6.0</td>
      <td>7.00</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>OverallCond</th>
      <td>1168.0</td>
      <td>5.594178</td>
      <td>1.116842</td>
      <td>1.0</td>
      <td>5.00</td>
      <td>5.0</td>
      <td>6.00</td>
      <td>9.0</td>
    </tr>
    <tr>
      <th>YearBuilt</th>
      <td>1168.0</td>
      <td>1971.120719</td>
      <td>30.279560</td>
      <td>1872.0</td>
      <td>1954.00</td>
      <td>1972.0</td>
      <td>2000.00</td>
      <td>2009.0</td>
    </tr>
    <tr>
      <th>YearRemodAdd</th>
      <td>1168.0</td>
      <td>1985.200342</td>
      <td>20.498566</td>
      <td>1950.0</td>
      <td>1968.00</td>
      <td>1994.0</td>
      <td>2004.00</td>
      <td>2010.0</td>
    </tr>
    <tr>
      <th>MasVnrArea</th>
      <td>1160.0</td>
      <td>104.620690</td>
      <td>183.996031</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>166.25</td>
      <td>1600.0</td>
    </tr>
    <tr>
      <th>BsmtFinSF1</th>
      <td>1168.0</td>
      <td>444.345890</td>
      <td>466.278751</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>384.0</td>
      <td>706.50</td>
      <td>5644.0</td>
    </tr>
    <tr>
      <th>BsmtFinSF2</th>
      <td>1168.0</td>
      <td>46.869863</td>
      <td>162.324086</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>1474.0</td>
    </tr>
    <tr>
      <th>BsmtUnfSF</th>
      <td>1168.0</td>
      <td>562.949486</td>
      <td>445.605458</td>
      <td>0.0</td>
      <td>216.00</td>
      <td>464.5</td>
      <td>808.50</td>
      <td>2336.0</td>
    </tr>
    <tr>
      <th>TotalBsmtSF</th>
      <td>1168.0</td>
      <td>1054.165240</td>
      <td>448.848911</td>
      <td>0.0</td>
      <td>792.75</td>
      <td>984.0</td>
      <td>1299.00</td>
      <td>6110.0</td>
    </tr>
    <tr>
      <th>1stFlrSF</th>
      <td>1168.0</td>
      <td>1161.268836</td>
      <td>393.541120</td>
      <td>334.0</td>
      <td>873.50</td>
      <td>1079.5</td>
      <td>1392.00</td>
      <td>4692.0</td>
    </tr>
    <tr>
      <th>2ndFlrSF</th>
      <td>1168.0</td>
      <td>351.218322</td>
      <td>437.334802</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>730.50</td>
      <td>2065.0</td>
    </tr>
    <tr>
      <th>LowQualFinSF</th>
      <td>1168.0</td>
      <td>5.653253</td>
      <td>48.068312</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>572.0</td>
    </tr>
    <tr>
      <th>GrLivArea</th>
      <td>1168.0</td>
      <td>1518.140411</td>
      <td>534.904019</td>
      <td>334.0</td>
      <td>1133.25</td>
      <td>1467.5</td>
      <td>1775.25</td>
      <td>5642.0</td>
    </tr>
    <tr>
      <th>BsmtFullBath</th>
      <td>1168.0</td>
      <td>0.426370</td>
      <td>0.523376</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>1.00</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>BsmtHalfBath</th>
      <td>1168.0</td>
      <td>0.061644</td>
      <td>0.244146</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>FullBath</th>
      <td>1168.0</td>
      <td>1.561644</td>
      <td>0.555074</td>
      <td>0.0</td>
      <td>1.00</td>
      <td>2.0</td>
      <td>2.00</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>HalfBath</th>
      <td>1168.0</td>
      <td>0.386130</td>
      <td>0.504356</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>1.00</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>BedroomAbvGr</th>
      <td>1168.0</td>
      <td>2.865582</td>
      <td>0.817491</td>
      <td>0.0</td>
      <td>2.00</td>
      <td>3.0</td>
      <td>3.00</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>KitchenAbvGr</th>
      <td>1168.0</td>
      <td>1.046233</td>
      <td>0.218084</td>
      <td>1.0</td>
      <td>1.00</td>
      <td>1.0</td>
      <td>1.00</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>TotRmsAbvGrd</th>
      <td>1168.0</td>
      <td>6.532534</td>
      <td>1.627412</td>
      <td>2.0</td>
      <td>5.00</td>
      <td>6.0</td>
      <td>7.00</td>
      <td>14.0</td>
    </tr>
    <tr>
      <th>Fireplaces</th>
      <td>1168.0</td>
      <td>0.612158</td>
      <td>0.640872</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>1.0</td>
      <td>1.00</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>GarageYrBlt</th>
      <td>1099.0</td>
      <td>1978.586897</td>
      <td>24.608158</td>
      <td>1900.0</td>
      <td>1962.00</td>
      <td>1980.0</td>
      <td>2002.00</td>
      <td>2010.0</td>
    </tr>
    <tr>
      <th>GarageCars</th>
      <td>1168.0</td>
      <td>1.761130</td>
      <td>0.759039</td>
      <td>0.0</td>
      <td>1.00</td>
      <td>2.0</td>
      <td>2.00</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>GarageArea</th>
      <td>1168.0</td>
      <td>473.000000</td>
      <td>218.795260</td>
      <td>0.0</td>
      <td>318.75</td>
      <td>479.5</td>
      <td>577.00</td>
      <td>1418.0</td>
    </tr>
    <tr>
      <th>WoodDeckSF</th>
      <td>1168.0</td>
      <td>92.618151</td>
      <td>122.796184</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>168.00</td>
      <td>736.0</td>
    </tr>
    <tr>
      <th>OpenPorchSF</th>
      <td>1168.0</td>
      <td>45.256849</td>
      <td>64.120769</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>24.0</td>
      <td>68.00</td>
      <td>523.0</td>
    </tr>
    <tr>
      <th>EnclosedPorch</th>
      <td>1168.0</td>
      <td>20.790240</td>
      <td>58.308987</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>330.0</td>
    </tr>
    <tr>
      <th>3SsnPorch</th>
      <td>1168.0</td>
      <td>3.323630</td>
      <td>27.261055</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>407.0</td>
    </tr>
    <tr>
      <th>ScreenPorch</th>
      <td>1168.0</td>
      <td>14.023116</td>
      <td>52.498520</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>410.0</td>
    </tr>
    <tr>
      <th>PoolArea</th>
      <td>1168.0</td>
      <td>1.934075</td>
      <td>33.192538</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>648.0</td>
    </tr>
    <tr>
      <th>MiscVal</th>
      <td>1168.0</td>
      <td>42.092466</td>
      <td>538.941473</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>15500.0</td>
    </tr>
    <tr>
      <th>MoSold</th>
      <td>1168.0</td>
      <td>6.377568</td>
      <td>2.727010</td>
      <td>1.0</td>
      <td>5.00</td>
      <td>6.0</td>
      <td>8.00</td>
      <td>12.0</td>
    </tr>
    <tr>
      <th>YrSold</th>
      <td>1168.0</td>
      <td>2007.815068</td>
      <td>1.327339</td>
      <td>2006.0</td>
      <td>2007.00</td>
      <td>2008.0</td>
      <td>2009.00</td>
      <td>2010.0</td>
    </tr>
    <tr>
      <th>SalePrice</th>
      <td>1168.0</td>
      <td>181081.876712</td>
      <td>81131.228007</td>
      <td>34900.0</td>
      <td>129975.00</td>
      <td>162950.0</td>
      <td>214000.00</td>
      <td>755000.0</td>
    </tr>
  </tbody>
</table>
</div>

## Nettoyage des Données

Dans cette section, nous allons effectuer un nettoyage des données.

### La colonne `id`

La colonne `id` n'est qu'une identification sans corrélation avec `SalePrice`.

Alors supprimons l'`id` :


```python
train.drop(columns=['Id'], inplace=True)
```

### Valeurs manquantes

Lorsque nous avons utilisé `info()` pour voir le résumé des données, nous avons pu voir que de nombreuses colonnes avaient un grand nombre de données manquantes.

Voyons quelles colonnes ont des valeurs manquantes et la proportion dans chacune d'entre elles.

`isna()` de pandas retournera les valeurs manquantes pour chaque colonne, puis la fonction `sum()` les additionnera pour vous donner un total.


```python
columns_with_miss = train.isna().sum()
#filtrer uniquement les colonnes avec au moins 1 valeur manquante
columns_with_miss = columns_with_miss[columns_with_miss!=0]
#Le nombre de colonnes avec des valeurs manquantes
print('Columns with missing values:', len(columns_with_miss))
#trier les colonnes par le nombre de valeurs manquantes par ordre décroissant
columns_with_miss.sort_values(ascending=False)
```

```
    Columns with missing values: 19
```



```
    PoolQC          1164
    MiscFeature     1129
    Alley           1098
    Fence            951
    FireplaceQu      551
    LotFrontage      204
    GarageYrBlt       69
    GarageType        69
    GarageFinish      69
    GarageQual        69
    GarageCond        69
    BsmtFinType2      31
    BsmtExposure      31
    BsmtFinType1      30
    BsmtCond          30
    BsmtQual          30
    MasVnrArea         8
    MasVnrType         8
    Electrical         1
    dtype: int64
```


Sur 80 colonnes, 19 ont des valeurs manquantes. 

Les valeurs manquantes en soi ne sont pas un gros problème, mais les colonnes avec un grand nombre de valeurs manquantes peuvent causer des distorsions.

C'est le cas pour :

* PoolQC : Qualité de la piscine
* MiscFeature : Caractéristique diverse non couverte dans d'autres catégories
* Alley : Type d'accès à la propriété par l'allée
* Fence : Qualité de la clôture

Supprimons-les de l'ensemble de données pour l'instant.


```python
# Suppression des colonnes
train.drop(columns=['PoolQC', 'MiscFeature', \
 'Alley', 'Fence'], inplace=True)
```

FireplaceQu a 551 valeurs manquantes, ce qui est également assez élevé.

Dans ce cas, les valeurs manquantes ont une signification, qui est "Pas de Cheminée".

Fireplace a les catégories suivantes :

* Ex Excellent - Cheminée en maçonnerie exceptionnelle
* Gd Bonne - Cheminée en maçonnerie au niveau principal
* TA Moyenne - Cheminée préfabriquée dans la zone de vie principale ou cheminée en maçonnerie au sous-sol
* Fa Passable - Cheminée préfabriquée au sous-sol
* Po Médiocre - Poêle Ben Franklin
* NA Pas de Cheminée

Vérifions la corrélation entre FireplaceQu et SalePrice, pour voir à quel point cette caractéristique est importante pour déterminer le prix.

Tout d'abord, nous allons remplacer les valeurs manquantes par 0.

Ensuite, nous encodons les catégories en nombres de 1 à 5.


```python
train['FireplaceQu'].fillna(0, inplace=True)
train['FireplaceQu'].replace({'Po': 1, 'Fa': 2, \
'TA': 3, 'Gd': 4, 'Ex': 5}, inplace=True)
```

En utilisant un diagramme à barres, nous pouvons voir comment la catégorie de la cheminée augmente la valeur de SalePrice.

Il est également intéressant de noter à quel point la valeur est plus élevée lorsque la maison a une cheminée excellente.

Cela signifie que nous devons conserver FireplaceQu comme caractéristique.


```python
sns.set(style="whitegrid")
sns.barplot(x='FireplaceQu', y="SalePrice", data=train)
```

Cela nous donnera cette sortie :
![Bar Plot](https://www.freecodecamp.org/news/content/images/2021/02/fireplace-2.png)


### Valeurs manquantes dans les colonnes numériques

Une autre caractéristique avec un grand nombre de valeurs manquantes est LotFrontage avec un compte de 204.

Voyons la corrélation entre les caractéristiques restantes avec des valeurs manquantes et le SalePrice.


```python
columns_with_miss = train.isna().sum()
columns_with_miss = columns_with_miss[columns_with_miss!=0]
c = list(columns_with_miss.index)
c.append('SalePrice')
train[c].corr()
```

<div>
<table>
  <thead>
    <tr>
      <th></th>
      <th>LotFrontage</th>
      <th>MasVnrArea</th>
      <th>GarageYrBlt</th>
      <th>SalePrice</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>LotFrontage</th>
      <td>1.000000</td>
      <td>0.196649</td>
      <td>0.089542</td>
      <td>0.371839</td>
    </tr>
    <tr>
      <th>MasVnrArea</th>
      <td>0.196649</td>
      <td>1.000000</td>
      <td>0.253348</td>
      <td>0.478724</td>
    </tr>
    <tr>
      <th>GarageYrBlt</th>
      <td>0.089542</td>
      <td>0.253348</td>
      <td>1.000000</td>
      <td>0.496575</td>
    </tr>
    <tr>
      <th>SalePrice</th>
      <td>0.371839</td>
      <td>0.478724</td>
      <td>0.496575</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>


Notez que LotFrontage, MasVnrArea et GarageYrBlt ont une corrélation positive avec SalePrice, mais cette corrélation n'est pas très forte.

Pour simplifier cette analyse, nous allons supprimer ces colonnes pour l'instant :

```python
cols_to_be_removed = ['LotFrontage', 'GarageYrBlt', \
 'MasVnrArea']
train.drop(columns=cols_to_be_removed, inplace=True)
```

Enfin, voici les colonnes restantes avec des valeurs manquantes :

```python
columns_with_miss = train.isna().sum()
columns_with_miss = columns_with_miss[columns_with_miss!=0]
print(f'Columns with missing values: {len(columns_with_miss)}')
columns_with_miss.sort_values(ascending=False)
```

```
    Columns with missing values: 11
```


```
    GarageCond      69
    GarageQual      69
    GarageFinish    69
    GarageType      69
    BsmtFinType2    31
    BsmtExposure    31
    BsmtFinType1    30
    BsmtCond        30
    BsmtQual        30
    MasVnrType       8
    Electrical       1
    dtype: int64
```

### Variables catégorielles

Travaillons sur les variables catégorielles de notre ensemble de données.

#### Traitement des valeurs manquantes

Remplissage des NaN catégoriques que nous savons comment remplir grâce au [fichier de description](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data?select=data_description.txt).

```python
# Remplace NA à la place de NaN
for c in ['GarageType', 'GarageFinish', 'BsmtFinType2', \
'BsmtExposure', 'BsmtFinType1']:
    train[c].fillna('NA', inplace=True)
    
# Remplace None à la place de NaN
train['MasVnrType'].fillna('None', inplace=True)
```

Avec cela, nous n'avons plus que 5 colonnes avec des valeurs manquantes dans notre ensemble de données.

```python
columns_with_miss = train.isna().sum()
columns_with_miss = columns_with_miss[columns_with_miss!=0]
print(f'Columns with missing values: {len(columns_with_miss)}')
columns_with_miss.sort_values(ascending=False)
```

```
    Columns with missing values: 5
```

```
    GarageCond    69
    GarageQual    69
    BsmtCond      30
    BsmtQual      30
    Electrical     1
    dtype: int64
```

#### Ordinal

En lisant également le [fichier de description](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data?select=data_description.txt), nous pouvons identifier d'autres variables qui ont un système similaire à FireplaceQu pour catégoriser la qualité : Médiocre, Bon, Excellent, etc.

Nous allons reproduire le traitement que nous avons donné à FireplaceQu pour ces variables selon les descriptions suivantes :

ExterQual : Évalue la qualité du matériau à l'extérieur

* Ex Excellent
* Gd Bon
* TA Moyen/Typique
* Fa Passable
* Po Médiocre

ExterCond : Évalue l'état actuel du matériau à l'extérieur

* Ex Excellent
* Gd Bon
* TA Moyen/Typique
* Fa Passable
* Po Médiocre

BsmtQual : Évalue la hauteur du sous-sol

* Ex Excellent (100+ pouces)
* Gd Bon (90-99 pouces)
* TA Typique (80-89 pouces)
* Fa Passable (70-79 pouces)
* Po Médiocre ( < 70 pouces)
* NA Pas de Sous-sol

BsmtCond : Évalue l'état général du sous-sol

* Ex Excellent
* Gd Bon
* TA Typique - légère humidité autorisée
* Fa Passable - humidité ou quelques fissures ou tassements
* Po Médiocre - Fissures graves, tassements ou humidité
* NA Pas de Sous-sol

HeatingQC : Qualité et état du chauffage

* Ex Excellent
* Gd Bon
* TA Moyen/Typique
* Fa Passable
* Po Médiocre

KitchenQual : Qualité de la cuisine

* Ex Excellent
* Gd Bon
* TA Moyen/Typique
* Fa Passable
* Po Médiocre

GarageQual : Qualité du garage

* Ex Excellent
* Gd Bon
* TA Moyen/Typique
* Fa Passable
* Po Médiocre
* NA Pas de Garage

GarageCond : État du garage

* Ex Excellent
* Gd Bon
* TA Moyen/Typique
* Fa Passable
* Po Médiocre
* NA Pas de Garage


```python
ord_cols = ['ExterQual', 'ExterCond', 'BsmtQual', 'BsmtCond', \
'HeatingQC', 'KitchenQual', 'GarageQual', 'GarageCond']
for col in ord_cols:
    train[col].fillna(0, inplace=True)
    train[col].replace({'Po': 1, 'Fa': 2, 'TA': 3, 'Gd': 4, \
    'Ex': 5}, inplace=True)
```

Traçons maintenant la corrélation de ces variables avec SalePrice.

```python
ord_cols = ['ExterQual', 'ExterCond', 'BsmtQual', 'BsmtCond', \
'HeatingQC', 'KitchenQual', 'GarageQual', 'GarageCond']
f, axes = plt.subplots(2, 4, figsize=(15, 10), sharey=True)

for r in range(0, 2):
    for c in range(0, 4):
        sns.barplot(x=ord_cols.pop(), y="SalePrice", \
        data=train, ax=axes[r][c])

plt.tight_layout()
plt.show()
```

![correlation_8-1](https://www.freecodecamp.org/news/content/images/2021/02/correlation_8-1.png)

Comme vous pouvez le voir, plus la catégorie d'une variable est bonne, plus le prix est élevé, ce qui signifie que ces variables seront importantes pour un modèle de prédiction.

#### Nominal

D'autres variables catégorielles ne semblent pas suivre un ordre clair.

Voyons combien de valeurs ces colonnes peuvent prendre :


```python
cols = train.columns
num_cols = train._get_numeric_data().columns
nom_cols = list(set(cols) - set(num_cols))
print(f'Nominal columns: {len(nom_cols)}')

value_counts = {}
for c in nom_cols:
    value_counts[c] = len(train[c].value_counts())

sorted_value_counts = {k: v for k, v in \
sorted(value_counts.items(), key=lambda item: item[1])}
sorted_value_counts
```

```
    Nominal columns: 31
```

```
    {'CentralAir': 2,
     'Street': 2,
     'Utilities': 2,
     'LandSlope': 3,
     'PavedDrive': 3,
     'MasVnrType': 4,
     'GarageFinish': 4,
     'LotShape': 4,
     'LandContour': 4,
     'BsmtCond': 5,
     'MSZoning': 5,
     'Electrical': 5,
     'Heating': 5,
     'BldgType': 5,
     'BsmtExposure': 5,
     'LotConfig': 5,
     'Foundation': 6,
     'RoofStyle': 6,
     'SaleCondition': 6,
     'BsmtFinType2': 7,
     'Functional': 7,
     'GarageType': 7,
     'BsmtFinType1': 7,
     'RoofMatl': 7,
     'HouseStyle': 8,
     'Condition2': 8,
     'SaleType': 9,
     'Condition1': 9,
     'Exterior1st': 15,
     'Exterior2nd': 16,
     'Neighborhood': 25}
```

Certaines variables catégorielles peuvent prendre plusieurs valeurs différentes comme Neighborhood. 

Pour simplifier, analysons uniquement les variables avec 6 valeurs différentes ou moins.

```python
nom_cols_less_than_6 = []
for c in nom_cols:
    n_values = len(train[c].value_counts())
    if n_values < 7:
        nom_cols_less_than_6.append(c)

print(f'Nominal columns with less than 6 values: \
{len(nom_cols_less_than_6)}')
```

```
    Nominal columns with less than 6 values: 19
```

Tracer contre SalePrice pour avoir une meilleure idée de la manière dont elles l'affectent :


```python
ncols = 3
nrows = math.ceil(len(nom_cols_less_than_6) / ncols)
f, axes = plt.subplots(nrows, ncols, figsize=(15, 30))

for r in range(0, nrows):
    for c in range(0, ncols):
        if not nom_cols_less_than_6:
            continue
        sns.barplot(x=nom_cols_less_than_6.pop(), \
        y="SalePrice", data=train, ax=axes[r][c])

plt.tight_layout()
plt.show()
```
    
![correlation_many-1](https://www.freecodecamp.org/news/content/images/2021/02/correlation_many-1.png)

Nous pouvons voir une bonne corrélation de nombreuses de ces colonnes avec la variable cible.

Pour l'instant, gardons-les.

Nous avons encore des NaN dans 'Electrical'.

Comme nous avons pu le voir dans le graphique ci-dessus, 'SBrkr' est la valeur la plus fréquente dans 'Electrical'.

Utilisons cette valeur pour remplacer NaN dans Electrical.


```python
# Insère la valeur la plus fréquente à la place de NaN

train['Electrical'].fillna('SBrkr', inplace=True)
```

#### Valeurs nulles

Un autre contrôle rapide consiste à voir combien de colonnes ont beaucoup de données égales à 0.


```python
train.isin([0]).sum().sort_values(ascending=False).head(25)
```

```
    PoolArea         1164
    LowQualFinSF     1148
    3SsnPorch        1148
    MiscVal          1131
    BsmtHalfBath     1097
    ScreenPorch      1079
    BsmtFinSF2       1033
    EnclosedPorch    1007
    HalfBath          727
    BsmtFullBath      686
    2ndFlrSF          655
    WoodDeckSF        610
    Fireplaces        551
    FireplaceQu       551
    OpenPorchSF       534
    BsmtFinSF1        382
    BsmtUnfSF          98
    GarageCars         69
    GarageArea         69
    GarageCond         69
    GarageQual         69
    TotalBsmtSF        30
    BsmtCond           30
    BsmtQual           30
    FullBath            8
    dtype: int64
```


Dans ce cas, même s'il y a beaucoup de 0, ils ont une signification.

Par exemple, PoolArea (Surface de la piscine en pieds carrés) égal à 0 signifie que la maison n'a pas de surface de piscine.

C'est une information importante corrélée à la maison et ainsi, nous allons les conserver.

### Valeurs aberrantes

Nous pouvons également jeter un coup d'œil aux valeurs aberrantes dans les variables numériques.

```python
# Obtenir uniquement les colonnes numériques
numerical_columns = \
list(train.dtypes[train.dtypes == 'int64'].index)

len(numerical_columns)
```

    42

```python
# Créer la grille de graphiques
rows = 7
columns = 6

fig, axes = plt.subplots(rows,columns, figsize=(30,30))

x, y = 0, 0

for i, column in enumerate(numerical_columns):
    sns.boxplot(x=train[column], ax=axes[x, y])
    
    if y < columns-1:
        y += 1
    elif y == columns-1:
        x += 1
        y = 0
    else:
        y += 1
```

![outlier-1](https://www.freecodecamp.org/news/content/images/2021/02/outlier-1.png)

Il y a beaucoup de valeurs aberrantes dans l'ensemble de données. 

Mais, si nous vérifions le fichier de [description des données](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data?select=data_description.txt), nous voyons que, en fait, certaines variables numériques sont des variables catégorielles qui ont été enregistrées (codifiées) sous forme de nombres. 

Ainsi, certains de ces points de données qui semblent être des valeurs aberrantes sont, en fait, des données catégorielles avec un seul exemple d'une certaine catégorie.

Gardons ces valeurs aberrantes.

### Sauvegarde des données nettoyées

Voyons à quoi ressemblent les données nettoyées et combien de colonnes nous avons conservées.

Nous n'avons plus de valeurs manquantes :

```python
columns_with_miss = train.isna().sum()
columns_with_miss = columns_with_miss[columns_with_miss!=0]
print(f'Columns with missing values: {len(columns_with_miss)}')
columns_with_miss.sort_values(ascending=False)
```

```
    Columns with missing values: 0

    Series([], dtype: int64)
```


Après avoir nettoyé les données, il nous reste 73 colonnes sur les 81 initiales.

```python
train.shape
```

    (1168, 73)

Jetons un coup d'œil aux 3 premiers enregistrements des données nettoyées.

```python
train.head(3).T
```

<div style="text-align: left;">
<table>
  <thead>
    <tr style="text-align: left;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>MSSubClass</th>
      <td>20</td>
      <td>60</td>
      <td>30</td>
    </tr>
    <tr>
      <th>MSZoning</th>
      <td>RL</td>
      <td>RL</td>
      <td>RM</td>
    </tr>
    <tr>
      <th>LotArea</th>
      <td>8414</td>
      <td>12256</td>
      <td>8960</td>
    </tr>
    <tr>
      <th>Street</th>
      <td>Pave</td>
      <td>Pave</td>
      <td>Pave</td>
    </tr>
    <tr>
      <th>LotShape</th>
      <td>Reg</td>
      <td>IR1</td>
      <td>Reg</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>MoSold</th>
      <td>2</td>
      <td>4</td>
      <td>3</td>
    </tr>
    <tr>
      <th>YrSold</th>
      <td>2006</td>
      <td>2010</td>
      <td>2010</td>
    </tr>
    <tr>
      <th>SaleType</th>
      <td>WD</td>
      <td>WD</td>
      <td>WD</td>
    </tr>
    <tr>
      <th>SaleCondition</th>
      <td>Normal</td>
      <td>Normal</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>SalePrice</th>
      <td>154500</td>
      <td>325000</td>
      <td>115000</td>
    </tr>
  </tbody>
</table>
<p>73 rows × 3 columns</p>
</div>

Nous pouvons voir un résumé des données montrant que, pour les 1168 enregistrements, il n'y a pas une seule valeur manquante (nulle).

```python
train.info()
```


```
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 1168 entries, 0 to 1167
    Data columns (total 73 columns):
    MSSubClass       1168 non-null int64
    MSZoning         1168 non-null object
    LotArea          1168 non-null int64
    Street           1168 non-null object
    LotShape         1168 non-null object
    LandContour      1168 non-null object
    Utilities        1168 non-null object
    LotConfig        1168 non-null object
    LandSlope        1168 non-null object
    Neighborhood     1168 non-null object
    Condition1       1168 non-null object
    Condition2       1168 non-null object
    BldgType         1168 non-null object
    HouseStyle       1168 non-null object
    OverallQual      1168 non-null int64
    OverallCond      1168 non-null int64
    YearBuilt        1168 non-null int64
    YearRemodAdd     1168 non-null int64
    RoofStyle        1168 non-null object
    RoofMatl         1168 non-null object
    Exterior1st      1168 non-null object
    Exterior2nd      1168 non-null object
    MasVnrType       1168 non-null object
    ExterQual        1168 non-null int64
    ExterCond        1168 non-null int64
    Foundation       1168 non-null object
    BsmtQual         1168 non-null int64
    BsmtCond         1168 non-null object
    BsmtExposure     1168 non-null object
    BsmtFinType1     1168 non-null object
    BsmtFinSF1       1168 non-null int64
    BsmtFinType2     1168 non-null object
    BsmtFinSF2       1168 non-null int64
    BsmtUnfSF        1168 non-null int64
    TotalBsmtSF      1168 non-null int64
    Heating          1168 non-null object
    HeatingQC        1168 non-null int64
    CentralAir       1168 non-null object
    Electrical       1168 non-null object
    1stFlrSF         1168 non-null int64
    2ndFlrSF         1168 non-null int64
    LowQualFinSF     1168 non-null int64
    GrLivArea        1168 non-null int64
    BsmtFullBath     1168 non-null int64
    BsmtHalfBath     1168 non-null int64
    FullBath         1168 non-null int64
    HalfBath         1168 non-null int64
    BedroomAbvGr     1168 non-null int64
    KitchenAbvGr     1168 non-null int64
    KitchenQual      1168 non-null int64
    TotRmsAbvGrd     1168 non-null int64
    Functional       1168 non-null object
    Fireplaces       1168 non-null int64
    FireplaceQu      1168 non-null int64
    GarageType       1168 non-null object
    GarageFinish     1168 non-null object
    GarageCars       1168 non-null int64
    GarageArea       1168 non-null int64
    GarageQual       1168 non-null int64
    GarageCond       1168 non-null int64
    PavedDrive       1168 non-null object
    WoodDeckSF       1168 non-null int64
    OpenPorchSF      1168 non-null int64
    EnclosedPorch    1168 non-null int64
    3SsnPorch        1168 non-null int64
    ScreenPorch      1168 non-null int64
    PoolArea         1168 non-null int64
    MiscVal          1168 non-null int64
    MoSold           1168 non-null int64
    YrSold           1168 non-null int64
    SaleType         1168 non-null object
    SaleCondition    1168 non-null object
    SalePrice        1168 non-null int64
    dtypes: int64(42), object(31)
    memory usage: 666.2+ KB
```

Enfin, sauvegardons les données nettoyées dans un fichier séparé.

```python
train.to_csv('train-cleaned.csv')
```

### Résumé de l'EDA

Nous avons traité les valeurs manquantes et supprimé les colonnes suivantes : 'Id', 'PoolQC', 'MiscFeature', 'Alley', 'Fence', 'LotFrontage', 'GarageYrBlt', 'MasVnrArea'.

Nous avons également :

* Remplacé les NaN par NA dans les colonnes suivantes : 'GarageType', 'GarageFinish', 'BsmtFinType2', 'BsmtExposure', 'BsmtFinType1'.
* Remplacé les NaN par None dans 'MasVnrType'.
* Imputé la valeur la plus fréquente à la place de NaN dans 'Electrical'.

Veuillez noter que les colonnes supprimées ne sont pas inutiles et peuvent contribuer au modèle final.

Après le premier tour d'analyse et de test de l'hypothèse, si vous devez jamais améliorer votre modèle futur, vous pouvez envisager de réévaluer ces colonnes et de mieux les comprendre pour voir comment elles s'intègrent dans le problème.

L'analyse des données et le Machine Learning ne sont PAS un chemin droit.

C'est un processus où vous itérez et continuez à tester des idées jusqu'à ce que vous obteniez le résultat que vous voulez, ou jusqu'à ce que vous découvriez que le résultat dont vous avez besoin n'est pas possible.

Nous allons utiliser ces données pour créer notre modèle de Machine Learning et prédire les prix des maisons dans le prochain article de cette série.


## Script de Nettoyage des Données

Ce chapitre convertit les décisions finales prises pour nettoyer les données dans l'Analyse Exploratoire des Données en un seul script Python qui prendra les données au format CSV et écrira les données nettoyées également sous forme de CSV.

### Code

Vous pouvez sauvegarder le script dans un fichier 'data_cleaning.py' et l'exécuter directement avec `python3 data_cleaning.py` ou `python data_cleaning.py`, selon votre installation.

Le script attend le fichier 'raw_data.csv'.

Le résultat sera un fichier nommé 'cleaned_data.csv'.

Il imprimera également la forme des données originales et la forme des nouvelles données nettoyées.

```
Original Data: (1168, 81)
After Cleaning: (1168, 73)
```

Le script de nettoyage :

```python
import os
import pandas as pd

# écrit la sortie sur 'cleaned_data.csv' par défaut
def clean_data(df, output_file='cleaned_data.csv'):

    # Supprime les colonnes avec des problèmes de valeurs manquantes
    cols_to_be_removed = ['Id', 'PoolQC', 'MiscFeature', \
    'Alley', 'Fence', 'LotFrontage',
    'GarageYrBlt', 'MasVnrArea']
    df.drop(columns=cols_to_be_removed, inplace=True)

    # Transforme les colonnes ordinales en numériques
    ordinal_cols = ['FireplaceQu', 'ExterQual', 'ExterCond', \
     'BsmtQual', 'BsmtCond', 
    'HeatingQC', 'KitchenQual', 'GarageQual', 'GarageCond']
    for col in ordinal_cols:
        df[col].fillna(0, inplace=True)
        df[col].replace({'Po': 1, 'Fa': 2, 'TA': 3, \
        'Gd': 4, 'Ex': 5}, inplace=True)

    # Remplace les NaN par NA
    for c in ['GarageType', 'GarageFinish', \
     'BsmtFinType2', 'BsmtExposure', 'BsmtFinType1']:
        df[c].fillna('NA', inplace=True)

    # Remplace les NaN par None
    df['MasVnrType'].fillna('None', inplace=True)

    # Impute avec la valeur la plus fréquente
    df['Electrical'].fillna('SBrkr', inplace=True)

    # Sauvegarde une copie
    cleaned_data = os.path.join(output_file)
    df.to_csv(cleaned_data)

    return df

if __name__ == "__main__":
    # Lit le fichier train.csv
    train_file = os.path.join('train.csv')

    if os.path.exists(train_file):
        df = pd.read_csv(train_file)
        print(f'Original Data: {df.shape}')
        cleaned_df = clean_data(df)
        print(f'After Cleaning: {cleaned_df.shape}')
    else:
        print(f'File not found {train_file}')
```





## Comment Construire le Modèle de Machine Learning

Maintenant, nous allons utiliser le fichier 'cleaned_data.csv' généré avec le script de nettoyage des données pour générer le Modèle de Machine Learning.

### Entraîner le Modèle de Machine Learning

Vous pouvez sauvegarder le script dans le fichier `train_model.py` et l'exécuter directement avec `python3 train_model.py` ou `python train_model.py`, selon votre installation.

Il attend que vous ayez un fichier appelé 'cleaned_data.csv'.

Le script générera trois autres fichiers :

* model.pkl : le modèle au format binaire généré par pickle que nous pouvons réutiliser plus tard
* train.csv : les données **train** après la division des données originales en train et test
* test.csv : les données **test** après la division des données originales en train et test

La sortie sur le terminal sera similaire à ceci :

```
Train data for modeling: (934, 74)
Test data for predictions: (234, 74)
Training the model ...
Testing the model ...
Average Price Test: 175652.0128205128
RMSE: 10552.188828855931
Model saved at model.pkl
```

Cela signifie que les modèles ont utilisé 934 points de données pour l'entraînement et 234 points de données pour le test.

Le prix de vente moyen dans l'ensemble de test est de 175 000 $.

Le RMSE (racine de l'erreur quadratique moyenne) est une bonne métrique pour comprendre la sortie car vous pouvez la lire en utilisant la même échelle que votre variable dépendante, qui est le prix de vente dans ce cas.

Un RMSE de 10552 signifie que, en moyenne, nous avons manqué les prix de vente corrects d'un peu plus de 10 000 dollars.

Compte tenu d'une moyenne de 175 000, manquer la cible de 10 000 en moyenne n'est pas trop mauvais.

### Le Script d'Entraînement

```python
import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
import pickle


def create_train_test_data(dataset):
    # charge et divise les données
    data_train = dataset.sample(frac=0.8, \
    random_state=30).reset_index(drop=True)

    data_test = \
    dataset.drop(data_train.index).reset_index(drop=True)

    # sauvegarde les données
    data_train.to_csv('train.csv', index=False)
    data_test.to_csv('test.csv', index=False)

    print(f"Train data for modeling: {data_train.shape}")
    print(f"Test data for predictions: {data_test.shape}")

def train_model(x_train, y_train):

    print("Training the model ...")

    model = Pipeline(steps=[
        ("label encoding", \
        OneHotEncoder(handle_unknown='ignore')),
        ("tree model", LinearRegression())
    ])
    model.fit(x_train, y_train)

    return model

def accuracy(model, x_test, y_test):
    print("Testing the model ...")
    predictions = model.predict(x_test)
    tree_mse = mean_squared_error(y_test, predictions)
    tree_rmse = np.sqrt(tree_mse)
    return tree_rmse

def export_model(model):
    # Sauvegarde le modèle
    pkl_path = 'model.pkl'
    with open(pkl_path, 'wb') as file:
        pickle.dump(model, file)
        print(f"Model saved at {pkl_path}")

def main():
    # Charge toutes les données
    data = pd.read_csv('cleaned_data.csv', \
    keep_default_na=False, index_col=0)

    # Divise train/test
    # Crée train.csv et test.csv
    create_train_test_data(data)

    # Charge les données pour l'entraînement du modèle
    train = pd.read_csv('train.csv', keep_default_na=False)
    x_train = train.drop(columns=['SalePrice'])
    y_train = train['SalePrice']

    # Charge les données pour le test du modèle
    test = pd.read_csv('test.csv', keep_default_na=False)
    x_test = test.drop(columns=['SalePrice'])
    y_test = test['SalePrice']

    # Entraînement et Test
    model = train_model(x_train, y_train)
    rmse_test = accuracy(model, x_test, y_test)

    print(f"Average Price Test: {y_test.mean()}")
    print(f"RMSE: {rmse_test}")

    # Sauvegarde le modèle
    export_model(model)

if __name__ == '__main__':
    main()
```


## L'API

La sortie du dernier chapitre est le Modèle de Machine Learning que nous allons utiliser dans l'API.

### Classe HousePriceModel

Enregistrez ce script dans un fichier nommé `predict.py`.

Ce fichier contient la classe `HousePriceModel` et est utilisé pour charger le modèle de Machine Learning et faire les prédictions.

```python
# la bibliothèque pickle est utilisée pour charger le modèle de machine learning
import pickle
import pandas as pd


class HousePriceModel():

    def __init__(self):
        self.model = self.load_model()
        self.preds = None

    def load_model(self):
        # utilise le fichier model.pkl
        pkl_filename = 'model.pkl'

        try:
            with open(pkl_filename, 'rb') as file:
                pickle_model = pickle.load(file)
        except:
            print(f'Error loading the model at {pkl_filename}')
            return None

        return pickle_model

    def predict(self, data):

        if not isinstance(data, pd.DataFrame):
            data = pd.DataFrame(data, index=[0])

        # fait les prédictions en utilisant le modèle chargé
        self.preds = self.model.predict(data)
        return self.preds
```

### Créer l'API avec FastAPI

Pour exécuter l'API :

```
uvicorn api:app
```

Voici la sortie attendue :

```
INFO:     Started server process [56652]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

L'API est créée avec le framework [FastAPI](https://fastapi.tiangolo.com/).

Le point de terminaison "/predict" vous donnera une prédiction basée sur un échantillon.

```python
from fastapi import FastAPI
from datetime import datetime
from predict import HousePriceModel

app = FastAPI()

@app.get("/")
def root():
    return {"status": "online"}

@app.post("/predict")
def predict(inputs: dict):

    model = HousePriceModel()

    start = datetime.today()
    pred = model.predict(inputs)[0]
    dur = (datetime.today() - start).total_seconds()

    return pred
```

### Tester l'API

Vous pouvez sauvegarder le script dans le fichier `test_api.py` et l'exécuter directement avec `python3 test_api.py` ou `python test_api.py`, selon votre installation.

N'oubliez pas d'exécuter ce test sur un second terminal tandis que le premier exécute le serveur pour l'API réelle.

Voici la sortie attendue :

```
The actual Sale Price: 109000
The predicted Sale Price: 109000.01144237864
```

Et voici le code pour tester l'API :

```python
# importer la bibliothèque requests pour faire des appels API
import requests
from predict import HousePriceModel

# un exemple d'entrée avec toutes les caractéristiques que nous 
# avons utilisées pour entraîner le modèle
sample_input = {'MSSubClass': 20, 'MSZoning': 'RL', 
'LotArea': 7922, 'Street': 'Pave', 
'LotShape': 'Reg', 'LandContour': 'Lvl', 
'Utilities': 'AllPub', 'LotConfig': 'Inside', 
'LandSlope': 'Gtl', 'Neighborhood': 'NAmes', 
'Condition1': 'Norm', 'Condition2': 'Norm', 
'BldgType': '1Fam', 'HouseStyle': '1Story', 
'OverallQual': 5, 'OverallCond': 7, 
'YearBuilt': 1953, 'YearRemodAdd': 2007, 
'RoofStyle': 'Gable', 'RoofMatl': 'CompShg', 
'Exterior1st': 'VinylSd', 'Exterior2nd': 'VinylSd', 
'MasVnrType': 'None', 'ExterQual': 3,
'ExterCond': 4, 'Foundation': 'CBlock', 
'BsmtQual': 3, 'BsmtCond': 3, 
'BsmtExposure': 'No', 'BsmtFinType1': 'GLQ', 
'BsmtFinSF1': 731, 'BsmtFinType2': 'Unf', 
'BsmtFinSF2': 0, 'BsmtUnfSF': 326, 
'TotalBsmtSF': 1057, 'Heating': 'GasA', 
'HeatingQC': 3, 'CentralAir': 'Y', 
'Electrical': 'SBrkr', '1stFlrSF': 1057, 
'2ndFlrSF': 0, 'LowQualFinSF': 0, 
'GrLivArea': 1057, 'BsmtFullBath': 1, 
'BsmtHalfBath': 0, 'FullBath': 1, 
'HalfBath': 0, 'BedroomAbvGr': 3, 
'KitchenAbvGr': 1, 'KitchenQual': 4, 
'TotRmsAbvGrd': 5, 'Functional': 'Typ', 
'Fireplaces': 0, 'FireplaceQu': 0, 
'GarageType': 'Detchd', 'GarageFinish': 'Unf',
'GarageCars': 1, 'GarageArea': 246, 
'GarageQual': 3, 'GarageCond': 3, 
'PavedDrive': 'Y', 'WoodDeckSF': 0, 
'OpenPorchSF': 52, 'EnclosedPorch': 0, 
'3SsnPorch': 0, 'ScreenPorch': 0, 
'PoolArea': 0, 'MiscVal': 0, 'MoSold': 1,
'YrSold': 2010, 'SaleType': 'WD', 
'SaleCondition': 'Abnorml'}

def run_prediction_from_sample():

    url="http://127.0.0.1:8000/predict"
    headers = {"Content-Type": "application/json", \
    "Accept":"text/plain"}

    response = requests.post(url, headers=headers, \
    json=sample_input)
    print("The actual Sale Price: 109000")
    print(f"The predicted Sale Price: {response.text}")


if __name__ == "__main__":
    run_prediction_from_sample()
```

## Conclusion

C'est tout !

Félicitations pour être arrivé à la fin.

Je tiens à vous remercier d'avoir lu cet article.

Si vous souhaitez en apprendre davantage, consultez mon blog [renanmf.com](https://renanmf.com/).

N'oubliez pas de [télécharger une version PDF de ce projet de Data Science et de Machine Learning avec le dépôt de code source complet lié dans le livre](https://renanmf.com/book-ds-ml-project-house-prices/).

Vous pouvez également me trouver sur Twitter : [@renanmouraf](https://twitter.com/renanmouraf).