---
title: Comment suivre les expériences d'apprentissage automatique avec HarperDB
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-07-01T17:12:06.000Z'
originalURL: https://freecodecamp.org/news/track-machine-learning-experiments-with-harperdb
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/image7.jpg
tags:
- name: Data Science
  slug: data-science
- name: database
  slug: database
- name: Machine Learning
  slug: machine-learning
seo_title: Comment suivre les expériences d'apprentissage automatique avec HarperDB
seo_desc: 'By Davis David

  Properly tracking your machine learning experiments is easier than you think.

  When working on a machine learning project, you will conduct different machine learning
  experiments before you reach the final ML model with the best perform...'
---

Par Davis David

Suivre correctement vos expériences d'apprentissage automatique est plus facile que vous ne le pensez.

Lorsque vous travaillez sur un projet d'apprentissage automatique, vous effectuerez différentes expériences d'apprentissage automatique avant d'atteindre le modèle ML final avec les meilleures performances.

Voici quelques expériences d'apprentissage automatique possibles que vous pourriez mener :

* Tester une variété d'algorithmes afin de déterminer lequel est le plus efficace pour le problème que vous essayez de résoudre (par exemple, un problème de classification).
* Sélectionner des caractéristiques importantes sur lesquelles travailler en fonction des performances du modèle.
* Affiner votre modèle afin d'améliorer ses performances (par exemple, la technique de recherche sur grille).
* Aborder les effets du surajustement et du sous-ajustement sur les performances du modèle.
* Effectuer un certain nombre d'autres tâches liées au problème que vous résolvez.

## Pourquoi est-il important de suivre les expériences ML ?

Il est important de suivre vos expériences d'apprentissage automatique car cela vous aidera à prendre une décision finale concernant le modèle ML que vous allez déployer en production. Vous serez mieux en mesure de le faire après avoir analysé les résultats des nombreuses expériences ML différentes que vous avez réalisées.

Plus vous effectuez d'expériences ML, plus il devient difficile de se souvenir de ce qui fonctionne et de ce qui ne fonctionne pas. Parfois, vous pourriez avoir un excellent résultat, mais parce qu'il a fallu des heures ou des jours pour l'entraîner, vous avez déjà modifié le code. Et maintenant, vous ne vous souvenez plus des paramètres que vous avez utilisés pour obtenir ce résultat !

Une pratique courante parmi les scientifiques des données est d'enregistrer manuellement leurs expériences ML sur du papier numérique ou physique. Mais utiliser l'instruction **print** (pour le langage de programmation Python), par exemple, pour voir la sortie de l'expérience est inefficace. Cela est dû au fait que lorsque vous effectuez une autre expérience, la sortie de la dernière expérience est perdue.

Heureusement, vous pouvez automatiser le suivi des expériences ML en conservant tous les résultats dans une base de données appelée [**HarperDB**](https://harperdb.io/). Non seulement elle est simple à configurer et s'adapte facilement à votre flux de travail existant, mais vous pouvez également partager les résultats de vos expériences d'apprentissage automatique avec vos coéquipiers en utilisant une simple API Rest.

## Qu'est-ce que HarperDB ?

[HarperDB](https://harperdb.io/product/) est une plateforme de gestion de données SQL/NoSQL rapide et flexible. Vous pouvez l'utiliser pour un certain nombre de choses différentes, y compris, mais sans s'y limiter, le développement rapide d'applications, le calcul distribué, le calcul en périphérie, le SaaS, et bien plus encore.

HarperDB est entièrement indexé, ne duplique pas les données et fonctionne sur n'importe quel appareil, de la périphérie au cloud.

Il est également compatible avec n'importe quel langage de programmation, y compris Python, JavaScript, Java, et d'autres.

Voici une liste de certaines des fonctionnalités disponibles sur HarperDB :

* API à point de terminaison unique
* [Fonctions personnalisées](https://harperdb.io/docs/custom-functions/) (plateforme de développement d'applications de type Lambda avec accès direct aux méthodes principales de HarperDB)
* Permet les insertions de fichiers JSON et CSV
* Prend en charge les requêtes SQL pour les opérations CRUD complètes
* Prend en charge Math.js et GeoJSON
* Configuration de la base de données limitée requise

![Image](https://lh6.googleusercontent.com/2c-VvF_MecEumwfpfGKhnRIiYvcbpSJHa8iS06R4dFVGaAK_OIR7e19AJbrPscZxxdPP7J2nFg378esTlVc758D0fmnGnXrDhUBCpCFt5a7-Jh11Yubd52fMQylfQ_GTmr9Q3zs4_e8vkK4k)
_Logo HarperDB_

HarperDB dispose d'une API HTTP intégrée, de fonctions personnalisées pour les points de terminaison définis par l'utilisateur et d'un schéma dynamique qui peut vous aider à partager les résultats de vos expériences avec vos collègues après les avoir stockés dans une instance cloud HarperDB.

Vous pouvez également télécharger rapidement les résultats de votre expérience ML sous forme de fichier CSV afin de pouvoir effectuer des analyses supplémentaires avant de prendre une décision finale.

Dans cet article, vous apprendrez comment utiliser HarperDB pour gérer facilement les résultats de vos expériences de Machine Learning.

Commençons 🚀

## Comment configurer HarperDB

HarperDB nécessite un compte et vous devrez configurer l'instance cloud HarperDB avant de l'utiliser. Pour faire ces deux choses, vous pouvez suivre les étapes ci-dessous.

### 1. Créer un compte HarperDB

Vous pouvez visiter htttps://harperdb.io/ puis cliquer sur la barre de navigation pour voir un lien appelé « Start Free ». Cliquez dessus pour créer votre compte.

Si vous avez déjà un compte, utilisez l'URL suivante [https://studio.harperdb.io/](https://studio.harperdb.io/) pour vous connecter avec vos identifiants.

![Image](https://lh6.googleusercontent.com/k15nBjnSuQDDXAB4d2qhcUbZMlYbzXg9ZahTVXO6LCelpjKXdtz5Qv25KDRUxJtY4R-9PcfUfdpjJX5Ed6d7b8UgpHLOXiOo_-w0aQaZni-cokgldzlYCGpV_1Q-4UeFhZ9poMkwvsYBj0DF)
_Capture d'écran de harperdb.io_

Vous devrez fournir des détails tels que votre nom, votre adresse e-mail et le sous-domaine souhaité lors du processus d'inscription. HarperDB configura automatiquement un nouveau sous-domaine pour vous.

![Image](https://lh6.googleusercontent.com/lhfmzgZ7ugSGJk_WufujpG2a26cXINr-iySiEMvAOspXjMfXh0sSwcsdEYov1LoOdX1KegG2SviYzDED-EGwP7qCuOpjKxGaBEqU8g63uFfKxYZE0-duXN9r-FDwJag8ziiy9vFR_aUTrXlZ)
_capture d'écran de harperdb.io_

### 2. Ajouter le mot de passe de votre compte

L'étape suivante consiste à ajouter un mot de passe fort à votre compte pour compléter le processus d'inscription de votre compte.

![Image](https://lh4.googleusercontent.com/UEzyQHlnqyDyaEra9na4l749CDjyrzlrng7MEWoTFtV-RM7Rbk-eJOFQcOvmab3l_Hgfe3DmOvin9Ju-lfK_HbbA-HDmUc1EGPwOZtV_brZLjduREX_cLbw-AXHBKJKMfwTtk0YSnoUHprpY)
_capture d'écran de harperdb.io_

### 3. Créer une instance cloud HarperDB

Après l'inscription, vous devez créer une instance cloud pour stocker et récupérer les résultats de votre expérience d'apprentissage automatique. Vous devez cliquer sur Créer une nouvelle instance cloud HarperDB pour ajouter une nouvelle instance à votre compte.

![Image](https://lh4.googleusercontent.com/OoD5aJ3pkZbY8ngBWG8DVuv_8_EoNw2CxtGcBmq4TuJZItmIYztWg98F7wbHOg_rsQGZLlenw3QaR3mktuntLek9nvT1HKq86_SZ0Z-WARug-nBfUs5KqujTgB-oCxuIJ1edVwC1ZYA_EuvU)
_capture d'écran de harperdb.io_

Vous verrez l'image ci-dessous où vous devrez sélectionner le type d'instance. Pour ce tutoriel, vous devez sélectionner **AWS ou Verizon Wavelength HarperDB Instance**.

![Image](https://lh5.googleusercontent.com/VfmdvsRqiesL89F46VLjpqOpZ8PNJzaxp9ykrY4A65iqzfxiPpd67bGxi0zbU9dHlyGNd-aBylQ8raGbb20oOsr-qUGjCPFbg8rI15-pTOc7pDWMxZcprm_8BSwf__3gIIgOULnmjpNVs0eG)
_capture d'écran de harperdb.io_

Ensuite, vous devez choisir le fournisseur cloud. Ici, vous utiliserez l'option par défaut, puis cliquerez sur **instance info**.

![Image](https://lh6.googleusercontent.com/X9U2NG7kzW0Bp8JTKNZMnLobMx0JZKx1myto-VkUNF2YaNi4eAm6eZrKQvB86e_AzvdvLEmxK52DoLSqmUzRYOxAJGXMobIoLnDbYh2HwuR2-jER2ET7OHTl_UCK1d8wkb5oTMNQlRTPQ1pg)
_capture d'écran de harperdb.io_

Sur la page d'informations de l'instance, vous devrez fournir le nom de l'instance cloud et les identifiants pour y accéder.

![Image](https://lh3.googleusercontent.com/Ov6rNGJmKUSchALz8UtTCrDYeFnsMeHbCWJNFcI0xwuW90ET4lAJanLH-a7eNnfIQ5Hk2xA5eeHD5JyZXUQlguqzPT0D0-79FeBZTckwbMpaCsqoJI1Nbk1vq_lYnbZn2LLweS4qIoC9h9dv)
_Capture d'écran de harperdb.io_

Ensuite, cliquez sur le bouton des détails de l'instance. Sur la page de spécification, vous devez sélectionner la taille de la RAM de l'instance, la taille du stockage de l'instance et la région de l'instance.

![Image](https://lh5.googleusercontent.com/NeBnYpK4IaUay7OdG8Jq6aXhuHX5H4mZVrdjHP2f_m7k4fvopoSUAfgbomt8HAeL2K9gi3ccCLLeMZjzSvrvM9gQWjfL9WqciV1o--JF4YTvJEt1UYG4P-N6G7riLvaD7avMLIAtAIDMWrH0)
_capture d'écran de harperdb.io_

Si vous utilisez le niveau de service gratuit, vous devez conserver tous les paramètres de l'écran ci-dessus à leurs valeurs par défaut, puis cliquer sur le bouton Confirmer les détails de l'instance.

La dernière étape consiste à confirmer les détails de l'instance et à ajouter l'instance cloud HarperDB. Assurez-vous d'examiner les détails une fois de plus, puis cliquez sur le bouton Ajouter une instance.

![Image](https://lh4.googleusercontent.com/yRDZqMgrv4beJPks4BVuH0NtuifwpU0X_S_yrxrM9ePiBo2qXIE87qHBMpGXwYT3GavLOS-0LRFuo-lTJvuecuq6lvEcHld22N9iWPihXRL0SZ1B2in8GEAxq8Q6WU8a77WCHy2wiTai8Mco)
_Capture d'écran de harperdb.io_

Enfin, vous verrez que la création de l'instance cloud a commencé comme indiqué ci-dessous.

![Image](https://lh6.googleusercontent.com/VMkt99fNEwcM9SnO6ckQ34psrBbJqkC_b72tNyADNcGmHzCnHGPEectn51eOQf8Fxg6NVjTzmEJ5POYbSGcPUYwUpSqPPfHEfeTjVaxSnabR1o2ShKwlhkRziKo9sjQ7MnAnhbSDt39QuFwm)
_Capture d'écran de harperdb.io_

Après quelques minutes, lorsque l'instance cloud HarperDB a été créée avec succès, vous verrez le statut comme OK pour cette instance particulière.

![Image](https://lh6.googleusercontent.com/Qqvy3r4h9ugGEo6qRffLB1bAdvqBOTJMnh0eClWGTOWQWANb7s66g4G8Ftgd-c4lV-KLO2Q1sGT8HIl1b1yC_0GX6U5vH1b5F232Er2z1hGgo0vUih0OZzDA_Rfmg05QSnujabmM-IgNVp0r)
_capture d'écran de harperdb.io_

**Félicitations** 🎉 Vous avez réussi à compléter la troisième étape de la création d'une instance cloud.

## Comment configurer le schéma et la table HarperDB

Vous devez d'abord créer un schéma et une table afin d'insérer les résultats de votre expérience ML dans la base de données.

Pour ce faire, tout ce que vous avez à faire est de charger l'instance cloud HarperDB que vous avez déjà établie à partir du tableau de bord.

Tout d'abord, vous devez créer le schéma en spécifiant un nom de schéma. Pour ce tutoriel, le nom du schéma est machinelearning.

![Image](https://lh3.googleusercontent.com/qsbN-_y6beTPxehjyDhsm9jsHm-vOBdOXJ3fCT62jwAV6zuM7j99sF8_M1t63P3CvSznLMxjpOnCna8MzAgBE2U-Y7VPjw225beHgg_0AemfdneTMVD0A0rO1SGsBmlsRq4zj4TsBhRPd36J)
_capture d'écran de harperdb.io_

Après la création d'un schéma, vous aurez la possibilité d'ajouter des tables. Commençons par créer la première table, que nous appellerons **experiments**.

HarperDB vous demandera également de spécifier le hash_attribute, qui est équivalent à un identifiant unique.

La valeur de hash_attribute sera automatiquement générée par HarperDB. La plupart des tables de données utilisent l'id comme identifiant unique pour chaque enregistrement, et c'est ce que vous utiliserez dans cette table appelée **experiments**.

![Image](https://lh6.googleusercontent.com/Eb64mbQccGkrnqLPUYxUbxpLe-fhBB1vGgQ0imSYleoLdOxier0hb80XC6_czCZdQkPKWu-Ocj4cPriy1nWMnSgGQHJle7fLDOW6Rb6skH_tUbwXVjKk85tmLYYOMeUJH76dQs3uESlIHtE1)
_capture d'écran de harperdb.io_

Le schéma, ainsi que la table, ont tous deux été créés avec succès à ce stade.

![Image](https://lh3.googleusercontent.com/o4koPZk0ox0VuL_ElXZ9JY3DvXux0kwn3Qfb72hF18jgBPMKznDQ2LFkhvq886cZ01TNhNAl18uFLy0mnzuC2hT6bBWAgyD8Hsj5lg3As58qeBzH0bAEM-U0CoD24onN6LU-aKzdLZ5ZhvZq)
_capture d'écran de harperdb.io_

## Comment suivre vos expériences d'apprentissage automatique dans HarperDB

Je vais utiliser le jeu de données Loan pour mener des expériences d'apprentissage automatique, puis enregistrer tous les résultats des expériences ML dans la table experiments de l'instance cloud de la base de données HarperDB.

L'objectif de l'expérience ML est d'atteindre une grande précision lors de la prédiction de savoir si un consommateur mérite un prêt. Vous pouvez télécharger le jeu de données [ici](https://github.com/Davisy/Run-Machine-Learning-Experiments-with-Python-Logging-module/blob/master/data/loans_data.csv).

Voici les étapes que vous devez suivre pour exécuter et suivre vos expériences ML.

### 1. Installer les packages requis

Vous devez installer le package suivant dans votre machine.

**(a) scikit-learn**  
Il s'agit de la bibliothèque d'apprentissage automatique qui dispose de différents algorithmes pour entraîner le modèle d'apprentissage automatique sur différents problèmes tels que la classification, la régression et le clustering.

```command
pip install scikit-learn
```

**(b) harper-sdk-python**  
Il s'agit du package Python que nous utiliserons pour implémenter différentes fonctions de l'API HarperDB. Il fournit également des wrappers pour une interface orientée objet.

```command
pip install harperdb
```

### 2. Importer d'autres packages importants

L'étape suivante consiste à importer des packages Python pour charger les données et pré-traiter le jeu de données et les algorithmes pour entraîner le jeu de données de prêt.

```python
#import packages

import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.metrics import classification_report, confusion_matrix, f1_score
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV

# classifiers
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import ExtraTreesClassifier
from xgboost import XGBClassifier
from imblearn.ensemble import (
    BalancedBaggingClassifier,
    EasyEnsembleClassifier,
)

# harperdb
import harperdb

import time
import json
import warnings  # To ignore any warnings

warnings.filterwarnings("ignore")

np.random.seed(123)
```

### 3. Charger le jeu de données Loan

Nous utiliserons la bibliothèque Pandas pour charger le jeu de données Loan.

```python
data = pd.read_csv("data/loans_data.csv")

data.columns
```

Voici la liste des caractéristiques disponibles dans le jeu de données Loan.

Loan_ID  
Gender  
Married  
Dependents  
Education  
Self_Employed  
ApplicantIncome  
CoapplicantIncome  
LoanAmount  
Loan_Amount_Term  
Credit_History  
Property_Area  
Loan_Status

Nous avons 12 caractéristiques indépendantes et une cible (Loan_Status). Vous pouvez lire la description de chaque caractéristique ici.

![Image](https://lh4.googleusercontent.com/-DnVHcT6_5Tyqvk9sIAhVbHUmGH74DnWFN2gb1Agui-HHxDx7eHsQPSde7QkOzvqm2VAGT9oVg9HZneQwPLwMUishoh4WYd04Y3mx7nl7XXwqDhPmNVF9lmE4nFAXJLd5nYuJqVndqaJ-Otq)
_Définition des caractéristiques_

### 4. Créer une fonction Python

Avant l'entraînement, vous devez gérer les valeurs manquantes incluses dans le jeu de données et pré-traiter les caractéristiques. J'ai développé un outil Python simple pour les données manquantes et l'ingénierie des caractéristiques.

```python
# function to preprocessing the dataset


def preprocessing(data):
    # replace with numerical values
    data['Dependents'].replace('3+', 3, inplace=True)
    data['Loan_Status'].replace('N', 0, inplace=True)
    data['Loan_Status'].replace('Y', 1, inplace=True)

    # handle missing data
    data['Gender'].fillna(data['Gender'].mode()[0], inplace=True)
    data['Married'].fillna(data['Married'].mode()[0], inplace=True)
    data['Dependents'].fillna(data['Dependents'].mode()[0], inplace=True)
    data['Self_Employed'].fillna(data['Self_Employed'].mode()[0], inplace=True)
    data['Credit_History'].fillna(data['Credit_History'].mode()[0],
                                  inplace=True)
    data['Loan_Amount_Term'].fillna(data['Loan_Amount_Term'].mode()[0],
                                    inplace=True)
    data['LoanAmount'].fillna(data['LoanAmount'].median(), inplace=True)

    # drop ID column
    data = data.drop('Loan_ID', axis=1)

    #scale the data
    data["ApplicantIncome"] = MinMaxScaler().fit_transform(
        data["ApplicantIncome"].values.reshape(-1, 1))
    data["LoanAmount"] = MinMaxScaler().fit_transform(
        data["LoanAmount"].values.reshape(-1, 1))
    data["CoapplicantIncome"] = MinMaxScaler().fit_transform(
        data["CoapplicantIncome"].values.reshape(-1, 1))
    data["Loan_Amount_Term"] = MinMaxScaler().fit_transform(
        data["Loan_Amount_Term"].values.reshape(-1, 1))

    #change categorical features to numerical
    data = pd.get_dummies(data)

    return data
```

Et si vous êtes curieux, vous pouvez également lire plus sur [comment gérer les valeurs manquantes dans un jeu de données ici](https://www.freecodecamp.org/news/how-to-handle-missing-data-in-a-dataset/).

Prétraitons le jeu de données Loan.

```python
data = preprocessing(data)
```

### 5. Se connecter à l'instance cloud HarperDB

L'étape suivante consiste à se connecter à l'instance cloud HarperDB afin d'insérer les résultats des expériences dans la table appelée experiments.

Ici, vous devez fournir trois paramètres :

* URL complète de l'instance HarperDB
* Votre nom d'utilisateur
* Votre mot de passe

```python
# connect to harperdb

URL = "https://{project-name}.harperdbcloud.com"
USERNAME = "your-username"
PASSWORD = "your-password"

db = harperdb.HarperDB(url=URL, username=USERNAME, password=PASSWORD)

# check if you are connected
db.describe_all()
```

Lorsque vous exécutez le code ci-dessus, vous verrez une sortie similaire à celle affichée ci-dessous, indiquant une connexion réussie à votre instance cloud HarperDB.

```
{'machinelearning': {'experiments': {'__createdtime__': 1656351257480,   '__updatedtime__': 1656351257480,   'hash_attribute': 'id',   'id': 'd5333654-16c0-4ae5-bf30-0a6e607b1ee7',   'name': 'experiments',   'residence': None,   'schema': 'machinelearning',   'attributes': [{'attribute': 'id'},    {'attribute': '__createdtime__'},    {'attribute': 'accuracy_mean'},    {'attribute': '__updatedtime__'},    {'attribute': 'model_name'},    {'attribute': 'training_period'},    {'attribute': 'name'}],   'record_count': 0}}}
```

### 6. Créer une fonction pour enregistrer les résultats des expériences

Vous devez également créer une fonction qui enregistrera chaque résultat d'expérience dans la table experiments. Vous devez définir le SCHEMA et la TABLE que vous utiliserez pour insérer les enregistrements.

La fonction ci-dessous recevra le résultat de l'expérience sous forme de **data** (format dictionnaire) et l'insérera dans cette table en utilisant la **fonction insert** du package harperdb-python.

La fonction insert recevra trois paramètres :

* Nom du SCHEMA
* Nom de la TABLE
* data (résultats des expériences)

```python
# define a function to record experiment results into the table

def record_results(data):

    #define the schema and table
    SCHEMA = "machinelearning"
    TABLE = "experiments"

    # insert data into the table
    result = db.insert(SCHEMA, TABLE, [data])

    return result
```

La fonction retournera le statut de cet enregistrement particulier s'il est inséré avec succès dans la table.

### 7. Diviser les données en caractéristiques et cible

Nous devons diviser les données en caractéristiques et cible. La cible pour ce jeu de données est une colonne nommée Loan_Status.

```python
# split data into train and test

X = data.drop('Loan_Status', axis=1)
y = data.Loan_Status
```

### 8. Exécuter et suivre les expériences d'apprentissage automatique

Maintenant, vous pouvez entraîner plusieurs algorithmes de classification et enregistrer les résultats dans la table de l'instance cloud HarperDB en utilisant la **fonction record_results**.

Ici, vous enregistrerez les enregistrements suivants dans la table :

* Le nom de l'expérience, par exemple « First ».
* Le nom du modèle de classification, par exemple RandomForestClassifier.
* Les noms des paramètres du modèle sont mappés à leurs valeurs.
* La liste des précisions à partir des scores de validation croisée.
* Le score de précision moyen.
* La période d'entraînement.

Les enregistrements mentionnés ci-dessus seront insérés dans la table experiments.

```python
# create a dictionary for  classifiers
models = {
    "KNeighborsClassifier": KNeighborsClassifier(),
    "RandomForestClassifier": RandomForestClassifier(),
    "GradientBoostingClassifier": GradientBoostingClassifier(),
    "DecisionTreeClassifier": DecisionTreeClassifier(),
    "BaggingClassifier": BaggingClassifier(),
    "XGBClassifier": XGBClassifier(),
    "ExtraTreesClassifier": ExtraTreesClassifier(),
    "LogisticRegression": LogisticRegression(),
    "BalancedBaggingClassifier": BalancedBaggingClassifier(),
    "EasyEnsembleClassifier": EasyEnsembleClassifier(),
}

# cross_val_score for each classifier
for model_name, model in models.items():

    start = time.time()

    scores = cross_val_score(model, X, y, cv=3, scoring='accuracy')

    end = time.time()

    training_duration = end - start

    data = {
        "name": "First",
        "model_name": model_name,
        "model_parameters": json.dumps(model.get_params()),
        "accuracy_scores": json.dumps(list(scores)),
        "accuracy_mean": scores.mean(),
        "training_period": training_duration
    }

    # insert result into the HarperDB table
    result = record_results(data)

    print(result)
    print("-------------------------------")
```

La sortie suivante sera générée une fois le code ci-dessus en cours d'exécution.

```command
{'message': 'inserted 1 of 1 records', 'inserted_hashes': ['d6fe4a54-69ee-4c10-8bb2-c592c57b30d7'], 'skipped_hashes': []}
-------------------------------
{'message': 'inserted 1 of 1 records', 'inserted_hashes': ['fca4307e-3287-4b76-9f8c-0c22ed1b4ac4'], 'skipped_hashes': []}
-------------------------------
{'message': 'inserted 1 of 1 records', 'inserted_hashes': ['1b0aabe7-1f31-4bb7-b195-8dc598e74a46'], 'skipped_hashes': []}
-------------------------------
{'message': 'inserted 1 of 1 records', 'inserted_hashes': ['02750d9c-8876-4e0d-8849-133d72b8ca20'], 'skipped_hashes': []}
-------------------------------
{'message': 'inserted 1 of 1 records', 'inserted_hashes': ['4ab96069-a014-49bd-ba90-6edd92b08c35'], 'skipped_hashes': []}
-------------------------------
```

Le but de cette sortie est de vérifier que les résultats des expériences ont été ajoutés à la table des expériences sans aucune erreur.

### 9. Voir la table des expériences

Si vous ouvrez votre instance cloud HarperDB, vous pourrez voir tous les enregistrements de vos expériences d'apprentissage automatique.

![Image](https://lh5.googleusercontent.com/CG6b7Pxxdk7CtQv7w6ramG7hn69PgRIWjfBDxtIbUVYJqI7poawg1QKWk30d50GJA4SuVxjELI4GeX6uZNsW8uCc2AxZqq-a8sPVv2CMVd6GTIJoEMjHhiUuX-oykt_bH-KVdgv0SUeQ9ROJ)
_capture d'écran de harperdb.io_

Vous pouvez également cliquer sur un seul enregistrement dans la table des expériences pour voir toutes les données enregistrées pour cet algorithme particulier que vous avez entraîné sur le jeu de données de prêt.

![Image](https://lh6.googleusercontent.com/Etsl3dQ9GXz5a6QkWjeSKViw8F1HV3jDV0VtvCQBYaaky7UQOcFIXuvcpMrjaRacQQ81W5GFDBif4OmZHLwMUPHjN4tpnsP2ysMMIbo7v2U7UjPWxg-5CmlyFNOfB5y9a_2PiKxv0IgU6e0f)
_capture d'écran de harperdb.io_

Par exemple, le modèle LogisticRegression a une précision de **80,7 %**.

Vous êtes maintenant en mesure de continuer à exécuter une variété d'expériences ML, et les résultats de ces expériences seront insérés dans l'instance cloud HarperDB.

Lorsque vous exécuterez votre prochaine expérience, elle continuera à enregistrer les résultats des expériences dans la table des expériences sans écraser les résultats précédents. Cela signifie que vous aurez une chance d'observer et d'examiner les résultats de toutes vos expériences et de les évaluer pour trouver un meilleur moyen d'améliorer les performances de votre modèle.

## Qu'est-ce qu'une fonction personnalisée ?

Une fonction personnalisée est une nouvelle fonctionnalité de HarperDB dans le cadre de leur version 3.1+. Cette fonctionnalité vous permet d'ajouter vos propres **points de terminaison API** à l'intérieur de HarperDB.

Les fonctions personnalisées sont alimentées par Fastify, qui est extrêmement flexible et facilite l'interaction avec vos données en utilisant les méthodes principales de HarperDB.

Dans cette section, vous apprendrez comment créer votre propre fonction personnalisée en utilisant le studio HarperDB. Cela vous permettra de communiquer les résultats de vos expériences d'apprentissage automatique avec vos collègues au travail en utilisant un appel d'API.

### 1. Activer les fonctions personnalisées

La première étape consiste à cliquer sur « **functions** » dans votre studio HarperDB, puis à activer les fonctions personnalisées (elles ne sont pas activées par défaut).

![Image](https://lh3.googleusercontent.com/OwkMMKF165s-SrnNE6AFNiQiz2UC1YypxsmbsSj5jSrj48muXRmgAkTXDCjd4o-veH7u_lxX2eLqsyizXMwXrSFqjSqo3tHLjnCDf5jJ7Wxm5Ezmc7xQZm7srHw9qn8midKr8_vTCbqNnTYR)
_capture d'écran de harperdb.io_

### 2. Créer un projet

L'étape suivante consiste à créer un projet en spécifiant le nom. Par exemple **api-v1**.

![Image](https://lh3.googleusercontent.com/2rpu0rcQ50wWjWLWbk20QCB6NionD8rzEl5QqL9gpSjkM0BjJjYziCU5hLkBqPHn0wSULwGiWbV5YnTct1eOuGnDnxX6a64JPSNHCG-dl_Z2WDW1m6OWqDQHSKbyXSGBHFNYKTYIL5_c3cFP)
_capture d'écran de harperdb.io_

Il créera également des fichiers de configuration pour le projet, y compris :

* Dossier Routes
* Fichier pour ajouter des fonctions d'assistance
* Dossier Static.

**Note :** Pour cet article, vous vous concentrerez sur le dossier routes.

### 3. Définir une route

Créons la première route pour récupérer certaines données de la table experiments à partir du magasin de données HarperDB. Mais d'abord, vous devez savoir que les URL de route sont résolues de la manière suivante :

[URL de l'instance]:[Port des fonctions personnalisées]/[Nom du projet]/[URL de la route]

Il inclura :

* URL de l'instance cloud
* Port des fonctions personnalisées
* Nom du projet que vous avez créé
* La route que vous avez définie

Dans le fichier de route (example.js) de la page de fonction, vous verrez un exemple de code de modèle. Vous devez remplacer ce code par le code suivant :

```javascript
'use strict';

module.exports = async (server, { hdbCore, logger }) => {

server.route({

    url: '/',
	method: 'GET',
	handler: (request) => {
	request.body= {
	operation: 'sql',
	sql: 'SELECT model_name,accuracy_scores,accuracy_mean,training_period FROM machinelearning.experiments ORDER BY accuracy_mean'
};
return hdbCore.requestWithoutAuthentication(request);
}
});
```

Dans le code ci-dessus, la route /api-v1 est définie avec la méthode GET et la fonction handler enverra une requête SQL à la base de données pour obtenir **model_name, accuracy_scores,** et **accuracy_mean,training_period** de la **table experiments** triée par la **colonne accuracy_mean**.

Vous pouvez enregistrer les nouvelles modifications que vous avez ajoutées dans le fichier de route.

### **4. Essayer votre point de terminaison API**

Enfin, vous pouvez maintenant utiliser la route que vous avez définie pour obtenir les données de la table experiments. Vous pouvez essayer d'accéder à la route via le navigateur web, n'importe quel langage de programmation, ou des outils API (comme Postman).

L'URL de la route sera : [https://functions-1-mlproject.harperdbcloud.com/api-v1](https://functions-1-mlproject.harperdbcloud.com/api-v1)

#### Comment accéder à la route via un navigateur web

Vous devez simplement copier l'URL de la route et l'ajouter à votre navigateur web pour voir les données demandées.

![Image](https://lh3.googleusercontent.com/FhvebnTRWqoTAq7vuAwXmzEwEL3wx87DTomP-49Fuct6VoA67AfvXlM8H38lAI0Qe0_U9yWKlAismwkSj4PLCZxSQa-l2QYM1TOOZv2PBM4XbzwdlBzwNH5bjnz59o4ykOIlYCxfNUh0L5jh)
_Capture d'écran du navigateur web._

Cela affichera les données que vous avez demandées selon la requête SQL définie dans la fonction handler.

#### Comment envoyer une requête API en Python

Cette option vous permet d'envoyer une requête API en utilisant le package **requests** de Python.

```python
#send an API request 

import requests

# api-endpoint
URL = "https://functions-1-mlproject.harperdbcloud.com/api-v1"
  
# sending get request and saving the response as response object
r = requests.get(url = URL)
  
# extracting data in json format
data = r.json()

for experiment in data:
    print(experiment)
```

Voici un exemple de sortie du code ci-dessus :

```command
{'model_name': 'EasyEnsembleClassifier', 'accuracy_scores': [0.6682926829268293, 0.697560975609756, 0.6421568627450981], 'accuracy_mean': 0.6693368404272277, 'training_period': 0.8020520210266113}{'model_name': 'DecisionTreeClassifier', 'accuracy_scores': [0.7121951219512195, 0.7024390243902439, 0.6127450980392157], 'accuracy_mean': 0.6757930814602263, 'training_period': 0.023849010467529297}{'model_name': 'BalancedBaggingClassifier', 'accuracy_scores': [0.7024390243902439, 0.6926829268292682, 0.6470588235294118], 'accuracy_mean': 0.6807269249163079, 'training_period': 0.09337425231933594}{'model_name': 'EasyEnsembleClassifier', 'accuracy_scores': [0.6926829268292682, 0.7268292682926829, 0.6715686274509803], 'accuracy_mean': 0.6970269408576438, 'training_period': 0.8345751762390137}
```

Comme vous pouvez le voir, HarperDB facilite la construction de points de terminaison API, ce qui permet à vos collègues d'accéder rapidement aux résultats de toute expérience d'apprentissage automatique que vous effectuez.

## Conclusion

Félicitations 🎉, vous êtes arrivé à la fin de cet article. Vous avez appris :

* L'importance de suivre vos expériences d'apprentissage automatique.
* Comment enregistrer les résultats de vos expériences ML dans l'**instance cloud HarperDB**.
* Comment créer une **fonction personnalisée** à partir de l'instance cloud HarperDB pour partager les résultats de vos expériences ML avec vos collègues travaillant sur le projet via un point de terminaison API.

Si vous avez appris quelque chose de nouveau ou si vous avez apprécié la lecture de cet article, veuillez le partager afin que d'autres puissent le voir. En attendant, à la prochaine !

Vous pouvez également me trouver sur Twitter [@Davis_McDavid](https://twitter.com/Davis_McDavid?ref=hackernoon.com).