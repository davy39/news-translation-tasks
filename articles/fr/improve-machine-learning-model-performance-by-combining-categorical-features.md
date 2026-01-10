---
title: Comment améliorer les performances d'un modèle de machine learning en combinant
  des caractéristiques catégorielles
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-05-27T17:55:23.000Z'
originalURL: https://freecodecamp.org/news/improve-machine-learning-model-performance-by-combining-categorical-features
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/zVaxL0LohRUpfDQhznRQ9z3y5tj1-g7c32kc.jpeg
tags:
- name: Machine Learning
  slug: machine-learning
- name: performance
  slug: performance
seo_title: Comment améliorer les performances d'un modèle de machine learning en combinant
  des caractéristiques catégorielles
seo_desc: 'By Davis David

  When you''re training a machine learning model, you can have some features in your
  dataset that represent categorical values. Categorical features are types of data
  that you can divide into groups.

  There are three common categorical dat...'
---

Par Davis David

Lorsque vous entraînez un modèle de machine learning, vous pouvez avoir certaines caractéristiques dans votre ensemble de données qui représentent des valeurs catégorielles. Les caractéristiques catégorielles sont des types de données que vous pouvez diviser en groupes.

Il existe trois types courants de données catégorielles :

1. **Ordinal** – un ensemble de valeurs dans l'ordre croissant ou décroissant. Exemple : évaluer le bonheur sur une échelle de 1 à 10
2. **Binaire** – un ensemble avec seulement deux valeurs. Exemple : chaud ou froid.
3. **Nominal** – un ensemble contenant des valeurs sans ordre particulier. Exemple : une liste de pays

La plupart des algorithmes de machine learning nécessitent des variables d'entrée et de sortie numériques. Cela signifie que vous devrez transformer les caractéristiques catégorielles de votre ensemble de données en entiers ou en flottants afin que les algorithmes de machine learning puissent les utiliser.

Vous pouvez soit utiliser le [LabelEncoding](https://www.freecodecamp.org/news/feature-engineering-and-feature-selection-for-beginners/?ref=hackernoon.com) pour les caractéristiques binaires, soit la méthode [One-hot-encoding](https://hackernoon.com/what-is-one-hot-encoding-why-and-when-do-you-have-to-use-it-e3c6186d008f?ref=hackernoon.com) pour les caractéristiques nominales.

Dans cet article, vous apprendrez comment la combinaison de caractéristiques catégorielles peut améliorer les performances de votre modèle de machine learning.

Alors, commençons. 🚀

## Comment combiner des caractéristiques catégorielles dans les modèles de machine learning

Vous pouvez créer une nouvelle caractéristique qui est une combinaison de deux autres caractéristiques catégorielles. Vous pouvez également combiner plus de trois, quatre ou même plus de caractéristiques catégorielles.

```python
df["new_feature"] = (
	df.feature_1.astype(str)
	 + "_"
	 + df.feature_2.astype(str)
	)
```

Dans le code ci-dessus, vous pouvez voir comment combiner deux caractéristiques catégorielles en utilisant Pandas et former une nouvelle caractéristique dans votre ensemble de données.

Quelles caractéristiques catégorielles devez-vous combiner ? Eh bien, il n'y a pas de réponse facile à cela. Cela dépend de vos données et des types de caractéristiques. Certaines connaissances du domaine peuvent être utiles pour créer de nouvelles caractéristiques comme celle-ci.

Pour illustrer tout le processus, nous allons utiliser l'ensemble de données [Financial Inclusion in Africa](https://zindi.africa/competitions/financial-inclusion-in-africa/data?ref=hackernoon.com) de la page de compétition [Zindi](https://zindi.africa/competitions/financial-inclusion-in-africa?ref=hackernoon.com). Il contient de nombreuses caractéristiques catégorielles que nous pouvons combiner pour voir si nous pouvons améliorer les performances du modèle.

L'objectif de cet ensemble de données est de prédire qui est le plus susceptible d'avoir un compte bancaire. Il s'agit donc d'un problème de classification.

## Étape 1 – Charger l'ensemble de données

Notre première étape consiste à nous assurer que nous avons téléchargé l'ensemble de données fourni dans la compétition. Vous pouvez télécharger l'ensemble de données [ici](https://zindi.africa/competitions/financial-inclusion-in-africa/data?ref=hackernoon.com).

Importez les packages Python importants comme ceci :

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
np.random.seed(123)
warnings.filterwarnings('ignore')
%matplotlib inline

```

Ensuite, chargez l'ensemble de données.

```python
# Importer les données
data = pd.read_csv('data/Train_v2.csv')

```

Regardons la forme de notre ensemble de données :

```python
# afficher la forme
print('forme des données :', data.shape)

forme des données : (23524, 13)

```

La sortie ci-dessus montre le nombre de lignes et de colonnes dans l'ensemble de données. Nous avons 13 variables dans l'ensemble de données – 12 variables indépendantes et 1 variable dépendante.

Nous pouvons voir les cinq premières lignes de notre ensemble de données en utilisant la méthode **`head()`** de la bibliothèque Pandas.

```python
# inspecter les données 

data.head()
```

![Image](https://www.freecodecamp.org/news/content/images/2021/05/zVaxL0LohRUpfDQhznRQ9z3y5tj1-oz2132qe.jpeg)

Il est important de comprendre la signification de chaque caractéristique afin de bien comprendre l'ensemble de données. Vous pouvez lire le fichier **VariableDefinition.csv** pour comprendre la signification de chaque variable présentée dans l'ensemble de données.

## Étape 2 – Interpréter l'ensemble de données

Nous pouvons obtenir plus d'informations sur les caractéristiques que nous avons en utilisant la méthode **`info()`** de Pandas.

```python
# afficher quelques informations sur l'ensemble de données

print(train_data.info())
```

![Image](https://www.freecodecamp.org/news/content/images/2021/05/zVaxL0LohRUpfDQhznRQ9z3y5tj1-h62f32t7.jpeg)

La sortie montre la liste des variables/caractéristiques, les tailles si elle contient des valeurs manquantes et le type de données pour chaque variable.

Nous n'avons aucune valeur manquante dans l'ensemble de données. Nous avons trois caractéristiques de type de données entier et 10 caractéristiques de type de données objet (la plupart sont des caractéristiques catégorielles).

## Étape 3 – Préparer les données pour les modèles de machine learning

L'étape suivante consiste à séparer les variables indépendantes et la cible (bank_account) des données. Ensuite, transformer les valeurs cibles du type de données objet en données numériques en utilisant [LabelEncoder](https://towardsdatascience.com/categorical-encoding-using-label-encoding-and-one-hot-encoder-911ef77fb5bd?ref=hackernoon.com).

```python
# importer le module de prétraitement
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler

# Convertir l'étiquette cible en données numériques
le = LabelEncoder()
data['bank_account'] = le.fit_transform(data['bank_account'])

# Séparer les caractéristiques d'entraînement de la cible
X = data.drop(['bank_account'], axis=1)
y = data['bank_account']

print(y)

```

![Image](https://www.freecodecamp.org/news/content/images/2021/05/zVaxL0LohRUpfDQhznRQ9z3y5tj1-el2r32yy--1-.jpeg)

Nous avons transformé les valeurs cibles en types de données numériques – 1 représente 'Oui' et 0 représente 'Non'.

J'ai créé une fonction de prétraitement simple pour :

* Gérer la conversion des types de données.
* Convertir les caractéristiques catégorielles en caractéristiques numériques en utilisant [One-hot Encoder et/ou Label Encoder](https://towardsdatascience.com/categorical-encoding-using-label-encoding-and-one-hot-encoder-911ef77fb5bd?ref=hackernoon.com).
* Supprimer la variable uniqueid.
* Effectuer une [mise à l'échelle des caractéristiques](https://towardsdatascience.com/preprocessing-with-sklearn-a-complete-and-comprehensive-guide-670cb98fcfb9?ref=hackernoon.com).

```python
# fonction pour prétraiter nos données 

def preprocessing_data(data):

    # Convertir les étiquettes numériques suivantes de entier en flottant
    float_array = data[["household_size", "age_of_respondent", "year"]].values.astype(float
    )
    
    # caractéristiques catégorielles à convertir en One Hot Encoding
    categ = [
        "relationship_with_head",
        "marital_status",
        "education_level",
        "job_type",
        "country",
    ]
    
    # Conversion One Hot Encoding
    data = pd.get_dummies(data, prefix_sep="_", columns=categ)
    
    # Conversion Label Encoder
    data["location_type"] = le.fit_transform(data["location_type"])
    data["cellphone_access"] = le.fit_transform(data["cellphone_access"])
    data["gender_of_respondent"] = le.fit_transform(data["gender_of_respondent"])
    
    # supprimer la colonne uniquid
    data = data.drop(["uniquid"], axis=1)
    
    # mettre à l'échelle nos données 
    scaler = StandardScaler()
    data = scaler.fit_transform(data)
    
    return data

```

Prétraitons notre ensemble de données.

```python
# prétraiter les données d'entraînement 
processed_test_data = preprocessing_data(X_train)

```

## Étape 4 – Construction du modèle et expériences

Nous utiliserons une partie de l'ensemble de données pour évaluer nos modèles.

```python
# Diviser les données d'entraînement
from sklearn.model_selection import train_test_split
X_Train, X_val, y_Train, y_val = train_test_split(processed_train_data, y_train, stratify = y, test_size = 0.1, random_state=42)

```

Nous n'utiliserons que **10%** de l'ensemble de données pour évaluer les modèles de machine learning. Le paramètre **stratify = y** garantira un équilibre égal des valeurs des deux classes ('oui' et 'non') pour les ensembles d'entraînement et de validation.

Nous utiliserons l'algorithme **Régression Logistique** pour ce problème de classification afin d'entraîner et de prédire qui est le plus susceptible d'avoir un compte bancaire.

```python
# importer l'algorithme de classification ici
from sklearn.linear_model import LogisticRegression

# créer le classificateur
lg_model = LogisticRegression()

# Entraîner le classificateur
lg_model.fit(X_Train,y_Train)

```

Après avoir entraîné le classificateur, utilisons le modèle entraîné pour prédire notre ensemble d'évaluation et voyons comment il performe. Nous utiliserons la précision comme métrique d'évaluation.

```python
# importer les métriques d'évaluation
from sklearn.metrics import confusion_matrix, accuracy_score

# évaluer le modèle
y_pred = lg_model.predict(X_val)

# Obtenir la précision
print("Score de précision du classificateur de régression logistique : ","{:.4f}".format(accuracy_score(y_val, lg_y_pred)))

```

Nous obtenons un score de précision de **0.8874** à partir du classificateur de régression logistique.

## Comment combiner les caractéristiques `education_level` et `job_type` pour améliorer les performances

Maintenant que nous connaissons les performances du modèle de base, voyons si nous pouvons les améliorer en combinant les caractéristiques **`education_level`** et **`job_type`**.

Dans notre première expérience, nous devons mettre à jour la fonction de prétraitement que nous avons créée, puis exécuter le reste du code.

```python
# fonction pour prétraiter nos données 
 
def preprocessing_data(data):

    # Convertir les étiquettes numériques suivantes de entier en flottant
    float_array = data[["household_size", "age_of_respondent", "year"]].values.astype(float)

    # combiner certaines caractéristiques cat
    data["features_combination"] = (data.education_level.astype(str) + "_" + data.job_type.astype(str) )

    # supprimer les caractéristiques individuelles qui sont combinées ensemble
    data = data.drop(['education_level','job_type'], axis=1)

    # caractéristiques catégorielles à convertir par One Hot Encoding
    categ = [
      "relationship_with_head",
      "marital_status",
      "features_combination",
      "country"
      ]

    # Conversion One Hot Encoding
    data = pd.get_dummies(data, prefix_sep="_", columns=categ)

    # Conversion Label Encoder
    data["location_type"] = le.fit_transform(data["location_type"])
    data["cellphone_access"] = le.fit_transform(data["cellphone_access"])
    data["gender_of_respondent"] = le.fit_transform(data["gender_of_respondent"])

    # supprimer la colonne uniquid
    data = data.drop(["uniqueid"], axis=1)

    # mettre à l'échelle nos données 
    scaler = StandardScaler()
    data = scaler.fit_transform(data)

    return data

```

Dans la fonction de prétraitement ci-dessus, j'ai mis à jour le code en :

* Combinant `education_level` et `job_type` pour créer une nouvelle caractéristique appelée **`features_combination`**.
* Supprimant les caractéristiques individuelles (`education_level` et `job_type`) de l'ensemble de données.
* Ajoutant une nouvelle caractéristique appelée **`feature_combination`** dans la liste des caractéristiques catégorielles que **One Hot Encoding** convertira.

**Note :** J'ai sélectionné uniquement les caractéristiques catégorielles nominales (qui ont plus de deux valeurs uniques).

Après avoir réentraîné le classificateur de régression logistique pour cette expérience, les performances du modèle sont passées de **0.8874** à **0.8882**. Cela montre que la combinaison de caractéristiques catégorielles peut améliorer les performances de notre modèle.

Gardez à l'esprit que nous n'avons rien changé, comme les hyper-paramètres dans notre classificateur de machine learning.

## Comment combiner les caractéristiques `relation_with_head` et `marital_status` pour améliorer les performances

Dans notre deuxième expérience, nous allons combiner deux autres caractéristiques catégorielles qui sont `relationship_with_head` et **`marital_status`**.

Nous devons simplement mettre à jour la fonction de prétraitement (comme dans la première expérience) puis exécuter le reste du code.

```python
# fonction pour prétraiter nos données 

def preprocessing_data(data):

    # Convertir les étiquettes numériques suivantes de entier en flottant
    float_array = data[["household_size", "age_of_respondent", "year"]].values.astype(
        float
    )
    
    # combiner certaines caractéristiques cat
    data["features_combination"] = (data.relationship_with_head.astype(str) + "_"
                           + data.marital_status.astype(str) 
                      )
    # supprimer les caractéristiques individuelles qui sont combinées ensemble
    data = data.drop(['relationship_with_head','marital_status'], axis=1)


    # caractéristiques catégorielles à convertir par One Hot Encoding
    categ = [
        "features_combination",
        "education_level",
        "job_type",
        "country",
    ]

    # Conversion One Hot Encoding
    data = pd.get_dummies(data, prefix_sep="_", columns=categ)

    # Conversion Label Encoder
    data["location_type"] = le.fit_transform(data["location_type"])
    data["cellphone_access"] = le.fit_transform(data["cellphone_access"])
    data["gender_of_respondent"] = le.fit_transform(data["gender_of_respondent"])

    # supprimer la colonne uniquid
    data = data.drop(["uniqueid"], axis=1)

    # mettre à l'échelle nos données 
    scaler = StandardScaler()
    data = scaler.fit_transform(data)

    return data
```

Dans la fonction de prétraitement ci-dessus, j'ai mis à jour le code en :

* Combinant `relation_with_head` et `marital_status` pour créer une nouvelle caractéristique appelée **`features_combination`**.
* Supprimant les caractéristiques individuelles (`relation_with_head` et `marital_status`) de l'ensemble de données.
* Ajoutant une nouvelle caractéristique appelée **`feature_combination`** dans la liste des caractéristiques catégorielles que **One Hot Encoding** convertira.

Après avoir réentraîné le classificateur de régression logistique pour la deuxième expérience, les performances du modèle ont diminué de **0.8874** à **0.8865**.

Cela montre que parfois, lorsque vous combinez des caractéristiques catégorielles, votre modèle de machine learning ne s'améliorera pas comme vous l'espériez. Par conséquent, vous devrez effectuer de nombreuses expériences jusqu'à obtenir des performances satisfaisantes de votre modèle de machine learning.

## Conclusion

Dans cet article, vous avez appris comment combiner des caractéristiques catégorielles dans votre ensemble de données afin d'améliorer les performances de votre modèle de machine learning.

Souvenez-vous simplement – pour obtenir des performances satisfaisantes de votre modèle, vous devez avoir certaines connaissances du domaine concernant le problème que vous résolvez. De plus, vous devez effectuer de nombreuses expériences qui nécessitent plus de ressources computationnelles.

Félicitations 👏👏, vous êtes arrivé à la fin de cet article ! J'espère que vous avez appris quelque chose de nouveau qui vous aidera dans votre prochain projet de machine learning ou de data science.

Si vous avez appris quelque chose de nouveau ou si vous avez apprécié la lecture de cet article, veuillez le partager afin que d'autres puissent le voir. En attendant, à la prochaine !

Vous pouvez également me trouver sur Twitter [@Davis_McDavid](https://twitter.com/Davis_McDavid?ref=hackernoon.com).

Vous pouvez lire [d'autres articles](https://hackernoon.com/u/davisdavid) ici.