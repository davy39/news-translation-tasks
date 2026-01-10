---
title: Tutoriel de Classification Binaire avec TensorFlow
subtitle: ''
author: Arunachalam B
co_authors: []
series: null
date: '2023-09-21T14:21:22.000Z'
originalURL: https://freecodecamp.org/news/binary-classification-made-simple-with-tensorflow
coverImage: https://www.freecodecamp.org/news/content/images/2023/09/Binary-Classification-Made-Simple-with-TensorFlow.png
tags:
- name: Machine Learning
  slug: machine-learning
- name: TensorFlow
  slug: tensorflow
seo_title: Tutoriel de Classification Binaire avec TensorFlow
seo_desc: "Binary classification is a fundamental task in machine learning, where\
  \ the goal is to categorize data into one of two classes or categories. \nBinary\
  \ classification is used in a wide range of applications, such as spam email detection,\
  \ medical diagnos..."
---

La classification binaire est une tâche fondamentale en apprentissage automatique, où l'objectif est de catégoriser les données en l'une des deux classes ou catégories. 

La classification binaire est utilisée dans une large gamme d'applications, telles que la détection de spam, le diagnostic médical, l'analyse de sentiment, la détection de fraude, et bien plus encore.

Dans cet article, nous allons explorer la classification binaire en utilisant TensorFlow, l'une des bibliothèques d'apprentissage profond les plus populaires.

Avant de nous plonger dans la Classification Binaire, discutons un peu du problème de classification en Apprentissage Automatique.

## Qu'est-ce qu'un problème de Classification ?

Un problème de Classification est un type de problème d'apprentissage automatique ou statistique dans lequel l'objectif est d'assigner une catégorie ou une étiquette à un ensemble de données d'entrée en fonction de leurs caractéristiques ou attributs. L'objectif est d'apprendre une correspondance entre les données d'entrée et des classes ou catégories prédéfinies, puis d'utiliser cette correspondance pour prédire les étiquettes de classe de nouvelles données non vues.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-89.png)
_Exemple de Classification Multi-Classe_

Le diagramme ci-dessus représente un problème de classification multi-classe dans lequel les données seront classées en plus de deux (trois ici) types de classes.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-90.png)
_Exemple de Classification Binaire_

Ce diagramme définit la Classification Binaire, où les données sont classées en deux types de classes.

Ce simple concept est suffisant pour comprendre les problèmes de classification. Explorons cela avec un exemple concret.

## Prédiction de l'Analyse des Crises Cardiaques en Utilisant la Classification Binaire

Dans cet article, nous allons entreprendre le voyage de la construction d'un modèle prédictif pour l'analyse des crises cardiaques en utilisant des bibliothèques d'apprentissage profond simples. 

Le modèle que nous allons construire, bien qu'étant un réseau de neurones relativement simple, est capable d'atteindre un niveau de précision d'environ 80%.

Résoudre des problèmes réels à travers le prisme de l'apprentissage automatique implique une série d'étapes essentielles :

1. Collecte et Analyse des Données
2. Prétraitement des données
3. Construction du Modèle ML
4. Entraînement du Modèle
5. Prédiction et Évaluation

## Collecte et Analyse des Données

Il est à noter que pour ce projet, j'ai obtenu le jeu de données à partir de [Kaggle](https://www.kaggle.com/datasets/rashikrahmanpritom/heart-attack-analysis-prediction-dataset), une plateforme populaire pour les compétitions et jeux de données en science des données. 

Je vous encourage à examiner de plus près son contenu. Comprendre le jeu de données est crucial car cela vous permet de saisir les nuances et les intricacies des données, ce qui peut vous aider à prendre des décisions éclairées tout au long du pipeline d'apprentissage automatique.

Ce jeu de données est bien structuré, et il n'y a pas de besoin immédiat pour une analyse supplémentaire. Cependant, si vous collectez le jeu de données par vous-même, vous devrez effectuer l'analyse et la visualisation des données indépendamment pour obtenir une meilleure précision.

Mettons nos chaussures de codage. 

Ici, j'utilise Google Colab. Vous pouvez utiliser votre propre machine (auquel cas vous devrez créer un fichier `.ipynb`) ou Google Colab sur votre compte pour exécuter le notebook. Vous pouvez trouver mon code source [ici](https://colab.research.google.com/drive/1-LBbym1bcTP6qF9tiENCzUVLGoY_NWMj?usp=sharing).

En tant que première étape, importons les bibliothèques requises.

```
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import sklearn
import pandas as pd
import keras
from keras.models import Sequential
from keras.layers import Dense
import tensorflow as tf
from sklearn.metrics import confusion_matrix,ConfusionMatrixDisplay
from sklearn.preprocessing import MinMaxScaler
```

J'ai le jeu de données dans mon drive et je le lis à partir de mon drive. Vous pouvez télécharger le même jeu de données [ici](https://www.kaggle.com/datasets/rashikrahmanpritom/heart-attack-analysis-prediction-dataset). 

N'oubliez pas de remplacer le chemin de votre fichier dans la méthode `read_csv` :

```
df = pd.read_csv("/content/drive/MyDrive/Datasets/heart.csv")
df.head()
```

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-91.png)
_5 enregistrements d'exemple dans le jeu de données_

Le jeu de données contient treize colonnes d'entrée (âge, sexe, cp, etc.) et une colonne de sortie (`output`), qui contiendra les données soit `0` soit `1`.

En considérant les lectures d'entrée, `0` dans la colonne `output` représente que la personne ne fera pas de crise cardiaque, tandis que `1` représente que la personne sera affectée par une crise cardiaque.

Séparons nos entrées et sorties du jeu de données ci-dessus pour entraîner notre modèle :

```
target_column = "output"
numerical_column = df.columns.drop(target_column)
output_rows = df[target_column]
df.drop(target_column,axis=1,inplace=True)
```

Puisque notre objectif est de prédire la probabilité d'une crise cardiaque (0 ou 1), représentée par la colonne cible, nous la séparons dans un jeu de données distinct.

## Prétraitement des données

Le prétraitement des données est une étape cruciale dans le pipeline d'apprentissage automatique, et la classification binaire ne fait pas exception. Il implique le nettoyage, la transformation et l'organisation des données brutes dans un format adapté à l'entraînement des modèles d'apprentissage automatique.

Un jeu de données contiendra plusieurs types de données telles que des données numériques, des données catégorielles, des données de timestamp, etc. 

Mais la plupart des algorithmes d'apprentissage automatique sont conçus pour fonctionner avec des données numériques. Ils nécessitent que les données d'entrée soient dans un format numérique pour les opérations mathématiques, l'optimisation et l'entraînement du modèle.

Dans ce jeu de données, toutes les colonnes contiennent des données numériques, donc nous n'avons pas besoin d'encoder les données. Nous pouvons procéder avec une simple normalisation. 

Rappelez-vous que si vous avez des colonnes non numériques dans votre jeu de données, vous devrez peut-être les convertir en données numériques en effectuant un encodage one-hot ou en utilisant d'autres algorithmes d'encodage.

Il existe de nombreuses stratégies de normalisation. Ici, j'utilise la Normalisation Min-Max :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-92.png)
_Formule de Mise à l'Échelle Min-Max_

Ne vous inquiétez pas – nous n'avons pas besoin d'appliquer cette formule manuellement. Nous avons des bibliothèques d'apprentissage automatique pour le faire. Ici, j'utilise MinMaxScaler de sklearn :

```
scaler = MinMaxScaler()
scaler.fit(df)
t_df = scaler.transform(df)
```

`scaler.fit(df)` calcule la moyenne et l'écart-type (ou d'autres paramètres de mise à l'échelle) nécessaires pour effectuer l'opération de mise à l'échelle. La méthode `fit` apprend essentiellement ces paramètres à partir des données.

`t_df = scaler.transform(df)` : Après avoir ajusté le scaler, nous devons transformer le jeu de données. La transformation met généralement à l'échelle les caractéristiques pour qu'elles aient une moyenne de 0 et un écart-type de 1 (standardisation) ou les met à l'échelle dans une plage spécifique (par exemple, [0, 1] avec la mise à l'échelle Min-Max) selon le scaler utilisé.

Nous avons terminé le prétraitement. L'étape cruciale suivante consiste à diviser le jeu de données en ensembles d'entraînement et de test.

Pour cela, je vais utiliser la fonction `train_test_split` de `scikit-learn`.

`X_train` et `X_test` sont les variables qui contiennent les variables indépendantes.

`y_train` et `y_test` sont les variables qui contiennent la variable dépendante, qui représente la sortie que nous cherchons à prédire.

```
X_train, X_test, y_train, y_test = train_test_split(t_df, output_rows, test_size=0.25, random_state=0)
```

```
print('X_train:',np.shape(X_train))
print('y_train:',np.shape(y_train))
print('X_test:',np.shape(X_test))
print('y_test:',np.shape(y_test))
```

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-93.png)
_Taille des ensembles d'entraînement et de test_

Nous avons divisé le jeu de données en 75% et 25%, où 75% est utilisé pour entraîner notre modèle et 25% pour tester notre modèle.

## Construction du Modèle ML

Un modèle d'apprentissage automatique est une représentation computationnelle d'un problème ou d'un système conçu pour apprendre des motifs, des relations et des associations à partir des données. Il sert de cadre mathématique et algorithmique capable de faire des prédictions, des classifications ou des décisions basées sur les données d'entrée. 

En essence, un modèle encapsule les connaissances extraites des données, lui permettant de généraliser et de faire des réponses éclairées à de nouvelles données, précédemment non vues.

Ici, je construis un modèle séquentiel simple avec une couche d'entrée et une couche de sortie. Étant un modèle simple, je n'utilise aucune couche cachée car cela pourrait augmenter la complexité du concept.

### Initialiser le Modèle Séquentiel

```
basic_model = Sequential()
```

`Sequential` est un type de modèle dans Keras qui vous permet de créer des réseaux de neurones couche par couche de manière séquentielle. Chaque couche est ajoutée au-dessus de la précédente.

### Couche d'Entrée

```
basic_model.add(Dense(units=16, activation='relu', input_shape=(13,)))
```

`Dense` est un type de couche dans Keras, représentant une couche entièrement connectée. Elle a 16 unités, ce qui signifie qu'elle a 16 neurones.

`activation='relu'` spécifie la fonction d'activation Rectified Linear Unit (ReLU), qui est couramment utilisée dans les couches d'entrée ou cachées des réseaux de neurones.

`input_shape=(13,)` indique la forme des données d'entrée pour cette couche. Dans ce cas, nous utilisons 13 caractéristiques d'entrée (colonnes).

### Couche de Sortie

```
basic_model.add(Dense(1, activation='sigmoid'))
```

Cette ligne ajoute la couche de sortie au modèle. 

C'est un seul neurone (1 unité) car il s'agit apparemment d'un problème de classification binaire, où vous prédisez l'une des deux classes (0 ou 1). 

La fonction d'activation utilisée ici est `'sigmoid'`, qui est couramment utilisée pour les tâches de classification binaire. Elle écrase la sortie dans une plage entre 0 et 1, représentant la probabilité d'appartenir à l'une des classes.

### Optimiseur

```
adam = keras.optimizers.Adam(learning_rate=0.001)
```

Cette ligne initialise l'optimiseur Adam avec un taux d'apprentissage de 0,001. L'optimiseur est responsable de la mise à jour des poids du modèle pendant l'entraînement pour minimiser la fonction de perte définie.

### Compiler le Modèle

```
basic_model.compile(loss='binary_crossentropy', optimizer=adam, metrics=["accuracy"])
```

Ici, nous allons compiler le modèle.

`loss='binary_crossentropy'` est la fonction de perte utilisée pour la classification binaire. Elle mesure la différence entre les valeurs prédites et réelles et est minimisée pendant l'entraînement.

`metrics=["accuracy"]` : Pendant l'entraînement, nous voulons surveiller la métrique de précision, qui vous indique à quel point le modèle performe en termes de prédictions correctes.

### Entraîner le modèle avec le jeu de données

Hourra, nous avons construit le modèle. Maintenant, il est temps d'entraîner le modèle avec notre jeu de données d'entraînement.

```
basic_model.fit(X_train, y_train, epochs=100)
```

`X_train` représente les données d'entraînement, qui consistent en les variables indépendantes (caractéristiques). Le modèle apprendra à partir de ces caractéristiques pour faire des prédictions ou des classifications.

`y_train` sont les étiquettes cibles correspondantes ou les variables dépendantes pour les données d'entraînement. Le modèle utilisera ces informations pour apprendre les motifs et les relations entre les caractéristiques et la variable cible.

`epochs=100` : Le paramètre `epochs` spécifie le nombre de fois où le modèle itérera sur l'ensemble du jeu de données d'entraînement. Chaque passage à travers le jeu de données est appelé une époque. Dans ce cas, nous avons 100 époques, ce qui signifie que le modèle verra l'ensemble du jeu de données d'entraînement 100 fois pendant l'entraînement.

```
loss_and_metrics = basic_model.evaluate(X_test, y_test)
print(loss_and_metrics)
print('Loss = ',loss_and_metrics[0])
print('Accuracy = ',loss_and_metrics[1])
```

La méthode `evaluate` est utilisée pour évaluer la performance du modèle entraîné sur le jeu de données de test. Elle calcule la perte (souvent la même fonction de perte utilisée pendant l'entraînement) et les métriques spécifiées (par exemple, la précision) pour les prédictions du modèle sur les données de test.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-94.png)
_Sortie d'exemple pour trouver la Perte et la Précision_

Ici, nous avons obtenu environ 82% de précision.

## Prédiction et Évaluation

```
predicted = basic_model.predict(X_test)
```

La méthode `predict` est utilisée pour générer des prédictions à partir du modèle en fonction des données d'entrée (`X_test` dans ce cas). La sortie (`predicted`) contiendra les prédictions du modèle pour chaque point de données dans le jeu de données d'entraînement. 

Puisque je n'ai qu'un jeu de données minimal, j'utilise le jeu de données de test pour la prédiction. Cependant, il est recommandé de diviser une partie du jeu de données (par exemple 10%) pour l'utiliser comme jeu de données de validation.

### Évaluation

Évaluer les prédictions en apprentissage automatique est une étape cruciale pour évaluer la performance d'un modèle. 

Un outil couramment utilisé pour évaluer les modèles de classification est la matrice de confusion. Explorons ce qu'est une matrice de confusion et comment elle est utilisée pour l'évaluation du modèle :

Dans un problème de classification binaire (deux classes, par exemple, "positif" et "négatif"), une matrice de confusion ressemble généralement à ceci :

<table><tbody><tr><td></td><td>Prédit Négatif (0)</td><td>Prédit Positif (1)</td></tr><tr><td>Actuel Négatif (0)</td><td>Vrai Négatif</td><td>Faux Positif</td></tr><tr><td>Actuel Positif (1)</td><td>Faux Négatif</td><td>Vrai Positif</td></tr></tbody></table>

Voici le code pour tracer la matrice de confusion à partir des données prédites de notre modèle :

```
predicted = tf.squeeze(predicted)
predicted = np.array([1 if x >= 0.5 else 0 for x in predicted])
actual = np.array(y_test)
conf_mat = confusion_matrix(actual, predicted)
displ = ConfusionMatrixDisplay(confusion_matrix=conf_mat)
displ.plot()
```

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-95.png)
_Matrice de confusion pour la sortie prédite_

Bravo ! Nous avons fait des progrès significatifs vers l'obtention de la sortie requise, avec environ 84% des données semblant être correctes. 

Il est à noter que nous pouvons encore optimiser ce modèle en utilisant un jeu de données plus grand et en ajustant les hyper-paramètres. Cependant, pour une compréhension fondamentale, ce que nous avons accompli jusqu'à présent est assez impressionnant.

Étant donné que ce jeu de données et les modèles d'apprentissage automatique correspondants sont à un niveau très basique, il est important de reconnaître que les scénarios réels impliquent souvent des jeux de données et des tâches d'apprentissage automatique beaucoup plus complexes. 

Bien que ce modèle puisse performer adéquatement pour des problèmes simples, il peut ne pas être adapté pour relever des défis plus complexes.

Dans les applications réelles, les jeux de données peuvent être vastes et divers, contenant une multitude de caractéristiques, de relations complexes et de motifs cachés. Par conséquent, aborder de telles complexités demande souvent une approche plus sophistiquée.

Voici quelques facteurs clés à considérer lors du travail avec des jeux de données complexes.

1. Prétraitement de Données Complexes
2. Encodage de Données Avancé
3. Compréhension de la Corrélation des Données
4. Couches Multiples de Réseaux de Neurones
5. Ingénierie des Caractéristiques
6. Régularisation

Si vous êtes déjà familiarisé avec la construction d'un réseau de neurones de base, je vous recommande vivement de vous plonger dans ces concepts pour exceller dans le monde de l'Apprentissage Automatique.

## Conclusion

Dans cet article, nous avons entrepris un voyage dans le monde fascinant de l'apprentissage automatique, en commençant par les bases. 

Nous avons exploré les fondamentaux de la classification binaire—une tâche fondamentale de l'apprentissage automatique. De la compréhension du problème à la construction d'un modèle simple, nous avons acquis des connaissances sur les concepts fondamentaux qui sous-tendent ce domaine puissant.

Alors, que vous commeniez tout juste ou que vous soyez déjà bien avancé sur le chemin, continuez à explorer, à expérimenter et à repousser les limites de ce qui est possible avec l'apprentissage automatique. Je vous retrouverai dans un autre article passionnant !

Si vous souhaitez en apprendre davantage sur l'intelligence artificielle / l'apprentissage automatique / l'apprentissage profond, abonnez-vous à mes articles en visitant mon [site](https://5minslearn.gogosoon.com/?ref=fcc_binary_classification), qui contient une liste consolidée de tous mes articles.