---
title: Concepts clés de l'apprentissage automatique expliqués — Division des ensembles
  de données et Forêt aléatoire
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/key-machine-learning-concepts-explained-dataset-splitting-and-random-forest
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d17740569d1a4ca35d9.jpg
tags:
- name: Machine Learning
  slug: machine-learning
- name: toothbrush
  slug: toothbrush
seo_title: Concepts clés de l'apprentissage automatique expliqués — Division des ensembles
  de données et Forêt aléatoire
seo_desc: 'Dataset Splitting

  Splitting up into Training, Cross Validation, and Test sets are common best practices.
  This allows you to tune various parameters of the algorithm without making judgements
  that specifically conform to training data.

  Motivation

  Data...'
---

## **Division des ensembles de données**

La division en ensembles d'entraînement, de validation croisée et de test est une bonne pratique courante. Cela permet d'ajuster divers paramètres de l'algorithme sans prendre de décisions qui se conforment spécifiquement aux données d'entraînement.

### **Motivation**

La division des ensembles de données émerge comme une nécessité pour éliminer le biais des données d'entraînement dans les algorithmes de ML. Modifier les paramètres d'un algorithme de ML pour qu'ils s'adaptent au mieux aux données d'entraînement entraîne généralement un algorithme surajusté qui performe mal sur les données de test réelles. Pour cette raison, nous divisons l'ensemble de données en plusieurs sous-ensembles discrets sur lesquels nous entraînons différents paramètres.

#### **L'ensemble d'entraînement**

L'ensemble d'entraînement est utilisé pour calculer le modèle réel que votre algorithme utilisera lorsqu'il sera exposé à de nouvelles données. Cet ensemble de données représente généralement 60 % à 80 % de l'ensemble de vos données disponibles (selon que vous utilisiez ou non un ensemble de validation croisée).

#### **L'ensemble de validation croisée**

Les ensembles de validation croisée sont utilisés pour la sélection de modèles (généralement ~20 % de vos données). Utilisez cet ensemble de données pour essayer différents paramètres pour l'algorithme tel qu'entraîné sur l'ensemble d'entraînement. Par exemple, vous pouvez évaluer différents paramètres de modèle (degré polynomial ou lambda, le paramètre de régularisation) sur l'ensemble de validation croisée pour voir lequel peut être le plus précis.

#### **L'ensemble de test**

L'ensemble de test est le dernier ensemble de données que vous touchez (généralement ~20 % de vos données). C'est la source de vérité. Votre précision dans la prédiction de l'ensemble de test est la précision de votre algorithme de ML.

## **Forêt aléatoire**

Une forêt aléatoire est un groupe d'arbres de décision qui prennent de meilleures décisions ensemble que individuellement.

### **Problème**

Les arbres de décision seuls sont sujets au **surajustement**. Cela signifie que l'arbre devient si habitué aux données d'entraînement qu'il a du mal à prendre des décisions pour des données qu'il n'a jamais vues auparavant.

### **Solution avec les forêts aléatoires**

Les forêts aléatoires appartiennent à la catégorie des algorithmes d'**apprentissage d'ensemble**. Cette classe d'algorithmes utilise de nombreux estimateurs pour obtenir de meilleurs résultats. Cela rend les forêts aléatoires généralement **plus précises** que les simples arbres de décision. Dans les forêts aléatoires, un ensemble d'arbres de décision est créé. Chaque arbre est **entraîné sur un sous-ensemble aléatoire des données et un sous-ensemble aléatoire des caractéristiques de ces données**. Ainsi, la possibilité que les estimateurs s'habituent aux données (surajustement) est grandement réduite, car **chacun d'eux travaille sur des données et des caractéristiques différentes** des autres. Cette méthode de création d'un ensemble d'estimateurs et de leur entraînement sur des sous-ensembles aléatoires de données est une technique en _apprentissage d'ensemble_ appelée **bagging** ou _Bootstrap AGGregatING_. Pour obtenir la prédiction, chacun des arbres de décision vote sur la prédiction correcte (classification) ou ils obtiennent la moyenne de leurs résultats (régression).

### **Exemple de Boosting en Python**

Dans cette compétition, nous recevons une liste d'événements de collision et leurs propriétés. Nous allons ensuite prédire si une désintégration τ → 3μ s'est produite lors de cette collision. Cette désintégration τ → 3μ est actuellement considérée par les scientifiques comme ne se produisant pas, et l'objectif de cette compétition était de découvrir que τ → 3μ se produit plus fréquemment que ce que les scientifiques peuvent actuellement comprendre. Le défi ici était de concevoir un problème d'apprentissage automatique pour quelque chose que personne n'a jamais observé auparavant. Les scientifiques du CERN ont développé les conceptions suivantes pour atteindre l'objectif. [https://www.kaggle.com/c/flavours-of-physics/data](https://www.kaggle.com/c/flavours-of-physics/data)

```python
# Nettoyage des données
import pandas as pd
data_test = pd.read_csv("test.csv")
data_train = pd.read_csv("training.csv")
data_train = data_train.drop('min_ANNmuon',1)
data_train = data_train.drop('production',1)
data_train = data_train.drop('mass',1)

# Données nettoyées
Y = data_train['signal']
X = data_train.drop('signal',1)

# adaboost
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
seed = 9001 # celui-ci est au-dessus de 9000 !!!
boosted_tree = AdaBoostClassifier(DecisionTreeClassifier(max_depth=1), algorithm="SAMME", 
                                  n_estimators=50, random_state = seed)
model = boosted_tree.fit(X, Y)

predictions = model.predict(data_test)
print(predictions)
# Notez que nous ne pouvons pas vraiment valider ces données car nous n'avons pas de tableau de "bonnes réponses"

# boosting de gradient stochastique
from sklearn.ensemble import GradientBoostingClassifier
gradient_boosted_tree = GradientBoostingClassifier(n_estimators=50, random_state=seed)
model2 = gradient_boosted_tree.fit(X,Y)

predictions2 = model2.predict(data_test)
print(predictions2)
```