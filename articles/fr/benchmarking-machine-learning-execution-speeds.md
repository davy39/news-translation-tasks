---
title: Comment mesurer la vitesse d'exécution de l'apprentissage automatique
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-25T11:23:11.000Z'
originalURL: https://freecodecamp.org/news/benchmarking-machine-learning-execution-speeds
coverImage: https://www.freecodecamp.org/news/content/images/2019/11/gpu.jpg
tags:
- name: data analysis
  slug: data-analysis
- name: Machine Learning
  slug: machine-learning
seo_title: Comment mesurer la vitesse d'exécution de l'apprentissage automatique
seo_desc: "By Pier Paolo Ippolito\nIntroduction\nThanks to recent advances in storage\
  \ capacity and memory management, it has become much easier to create machine learning\
  \ and deep learning projects from the comfort of your own home. \nIn this article,\
  \ I will intro..."
---

Par Pier Paolo Ippolito

## Introduction

Grâce aux récentes avancées en matière de capacité de stockage et de gestion de la mémoire, il est devenu beaucoup plus facile de créer des projets d'apprentissage automatique et d'apprentissage profond depuis le confort de votre propre domicile. 

Dans cet article, je vais vous présenter différentes approches possibles pour les projets d'apprentissage automatique en Python et vous donner quelques indications sur leurs compromis en termes de vitesse d'exécution. Certaines des différentes approches sont :

* Utilisation d'un CPU (Unité centrale de traitement)/GPU (Unité de traitement graphique) d'un ordinateur personnel/portable.
* Utilisation de services cloud (Kaggle, Google Colab).

Tout d'abord, nous devons importer toutes les dépendances nécessaires :

```python
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from xgboost import XGBClassifier
import xgboost as xgb
from sklearn.metrics import accuracy_score
```

Pour cet exemple, j'ai décidé de fabriquer un ensemble de données simple en utilisant des distributions gaussiennes composées de quatre caractéristiques et de deux étiquettes (0/1) :

```python
# Création d'un ensemble de données linéairement séparable en utilisant des distributions gaussiennes.
# La première moitié des nombres dans Y est 0 et l'autre moitié est 1.
# Par conséquent, j'ai rendu la première moitié des 4 caractéristiques assez différente de
# la seconde moitié des caractéristiques (en définissant la valeur des moyennes assez 
# similaires) afin de rendre la classification entre les 
# classes assez simple (les données sont linéairement séparables).
dataset_len = 40000000
dlen = int(dataset_len/2)
X_11 = pd.Series(np.random.normal(2,2,dlen))
X_12 = pd.Series(np.random.normal(9,2,dlen))
X_1 = pd.concat([X_11, X_12]).reset_index(drop=True)
X_21 = pd.Series(np.random.normal(1,3,dlen))
X_22 = pd.Series(np.random.normal(7,3,dlen))
X_2 = pd.concat([X_21, X_22]).reset_index(drop=True)
X_31 = pd.Series(np.random.normal(3,1,dlen))
X_32 = pd.Series(np.random.normal(3,4,dlen))
X_3 = pd.concat([X_31, X_32]).reset_index(drop=True)
X_41 = pd.Series(np.random.normal(1,1,dlen))
X_42 = pd.Series(np.random.normal(5,2,dlen))
X_4 = pd.concat([X_41, X_42]).reset_index(drop=True)
Y = pd.Series(np.repeat([0,1],dlen))
df = pd.concat([X_1, X_2, X_3, X_4, Y], axis=1)
df.columns = ['X1', 'X2', 'X3', 'X_4', 'Y']
df.head()
```

![Image](https://www.freecodecamp.org/news/content/images/2019/11/image-32.png)
_Figure 1 : Exemple de jeu de données_

Enfin, nous devons maintenant préparer notre jeu de données pour qu'il soit alimenté dans un modèle d'apprentissage automatique (en le divisant en caractéristiques et étiquettes, et en ensembles d'entraînement et de test) :

```python
train_size = 0.80
X = df.drop(['Y'], axis = 1).values
y = df['Y']

# L'objet label_encoder sait comment comprendre les étiquettes de mots. 
label_encoder = preprocessing.LabelEncoder() 

# Encoder les étiquettes
y = label_encoder.fit_transform(y) 

# Identifier la forme et les indices
num_rows, num_columns = df.shape
delim_index = int(num_rows * train_size)

# Division du jeu de données en ensembles d'entraînement et de test
X_train, y_train = X[:delim_index, :], y[:delim_index]
X_test, y_test = X[delim_index:, :], y[delim_index:]

# Vérification des dimensions des ensembles
print('X_train dimensions: ', X_train.shape, 'y_train: ', y_train.shape)
print('X_test dimensions:', X_test.shape, 'y_validation: ', y_test.shape)

# Vérification des dimensions en pourcentages
total = X_train.shape[0] + X_test.shape[0]
print('X_train Percentage:', (X_train.shape[0]/total)*100, '%')
print('X_test Percentage:', (X_test.shape[0]/total)*100, '%')
```

Le résultat de la division train test est affiché ci-dessous :

```
X_train dimensions:  (32000000, 4) y_train:  (32000000,)
X_test dimensions: (8000000, 4) y_validation:  (8000000,)
X_train Percentage: 80.0 %
X_test Percentage: 20.0 %
```

Nous sommes maintenant prêts à commencer à évaluer les différentes approches. Dans tous les exemples suivants, nous utiliserons [XGBoost (Gradient Boosted Decision Trees)](https://towardsdatascience.com/https-medium-com-vishalmorde-xgboost-algorithm-long-she-may-rein-edd9f99be63d) comme notre classificateur.

## 1) CPU

L'entraînement d'un XGBClassifier sur ma machine personnelle (sans utiliser de GPU) a conduit aux résultats suivants :

```python
%%time

model = XGBClassifier(tree_method='hist')
model.fit(X_train, y_train)
```

```
CPU times: user 8min 1s, sys: 5.94 s, total: 8min 7s
Wall time: 8min 6s
XGBClassifier(base_score=0.5, booster='gbtree', colsample_bylevel=1,
              colsample_bynode=1, colsample_bytree=1, gamma=0,
              learning_rate=0.1, max_delta_step=0, max_depth=3,
              min_child_weight=1, missing=None, n_estimators=100, n_jobs=1,
              nthread=None, objective='binary:logistic', random_state=0,
              reg_alpha=0, reg_lambda=1, scale_pos_weight=1, seed=None,
              silent=None, subsample=1, tree_method='hist', verbosity=1)
```

Une fois que nous avons entraîné notre modèle, nous pouvons maintenant vérifier sa précision de prédiction :

```python
sk_pred = model.predict(X_test)
sk_pred = np.round(sk_pred)
sk_acc = round(accuracy_score(y_test, sk_pred), 2)
print("XGB accuracy using Sklearn:", sk_acc*100, '%')
```

```
XGB accuracy using Sklearn: 99.0 %
```

En résumé, en utilisant une machine CPU standard, il a fallu environ 8 minutes pour entraîner notre classificateur afin d'atteindre une précision de 99 %.

## 2) GPU

Je vais maintenant utiliser une [NVIDIA TITAN RTX GPU](https://www.nvidia.com/en-gb/deep-learning-ai/products/titan-rtx/) sur ma machine personnelle pour accélérer l'entraînement. Dans ce cas, afin d'activer le mode GPU de XGB, nous devons spécifier la **_tree_method_** comme **_gpu_hist_** au lieu de **_hist_**. 

```
%%time

model = XGBClassifier(tree_method='gpu_hist')
model.fit(X_train, y_train)
```

L'utilisation de la TITAN RTX a conduit dans cet exemple à seulement 8,85 secondes de temps d'exécution (environ 50 fois plus rapide que l'utilisation du seul CPU !).

```python
sk_pred = model.predict(X_test)
sk_pred = np.round(sk_pred)
sk_acc = round(accuracy_score(y_test, sk_pred), 2)
print("XGB accuracy using Sklearn:", sk_acc*100, '%')
```

```
XGB accuracy using Sklearn: 99.0 %
```

Cette amélioration considérable de la vitesse a été possible grâce à la capacité du GPU à soulager le CPU, libérant de la mémoire RAM et parallélisant l'exécution de plusieurs tâches.

## 3) Services Cloud GPU

Je vais maintenant passer en revue deux exemples de services cloud GPU gratuits (Google Colab et Kaggle) et vous montrer les scores de référence qu'ils sont capables d'atteindre. Dans les deux cas, nous devons activer explicitement les GPU sur les notebooks respectifs et spécifier la **_tree_method_** de XGBoost comme **_gpu_hist_**.

### Google Colab

En utilisant les GPU NVIDIA TESLA T4 de Google Colab, les scores suivants ont été enregistrés :

```
CPU times: user 5.43 s, sys: 1.88 s, total: 7.31 s
Wall time: 7.59 s
```

### Kaggle

L'utilisation de Kaggle a conduit à un temps d'exécution légèrement plus élevé :

```
CPU times: user 5.37 s, sys: 5.42 s, total: 10.8 s
Wall time: 11.2 s
XGBClassifier(base_score=0.5, booster='gbtree', colsample_bylevel=1,
              colsample_bynode=1, colsample_bytree=1, gamma=0,
              learning_rate=0.1, max_delta_step=0, max_depth=3,
              min_child_weight=1, missing=None, n_estimators=100, n_jobs=1,
              nthread=None, objective='binary:logistic', random_state=0,
              reg_alpha=0, reg_lambda=1, scale_pos_weight=1, seed=None,
              silent=None, subsample=1, tree_method='gpu_hist', verbosity=1)
```

L'utilisation de Google Colab ou de Kaggle a conduit à une diminution remarquable du temps d'exécution. 

Un inconvénient de l'utilisation de ces services est la quantité limitée de CPU et de RAM disponible. En fait, l'augmentation légère des dimensions de l'ensemble de données d'exemple a provoqué un manque de mémoire RAM dans Google Colab (ce qui n'était pas un problème lors de l'utilisation de la TITAN RTX). 

Une façon possible de résoudre ce type de problème lors du travail avec des appareils à mémoire contrainte est d'optimiser le code pour consommer le moins de mémoire possible (en utilisant une précision à virgule fixe et des structures de données plus efficaces).

## 4) Point Bonus : RAPIDS

En tant que point supplémentaire, je vais maintenant vous présenter RAPIDS, une collection open-source de bibliothèques Python de NVIDIA. Dans cet exemple, nous allons utiliser son intégration avec la bibliothèque XGBoost pour accélérer notre flux de travail dans Google Colab. Le notebook complet pour cet exemple (avec des instructions sur la configuration de RAPIDS dans Google Colab) est disponible [ici](https://drive.google.com/open?id=1LZzK-iq9xEEuOfEpv2SLeCyV6ksx0kio) ou sur [mon compte GitHub](https://github.com/pierpaolo28/Artificial-Intelligence-Projects/blob/master/NVIDIA-RAPIDS%20AI/RAPIDS%20GPU%20Benchmark%20Colab.ipynb). 

RAPIDS est conçu pour être la prochaine étape évolutive dans le traitement des données. Grâce à son format Apache Arrow en mémoire, RAPIDS peut conduire à une amélioration de la vitesse jusqu'à environ 50 fois par rapport au traitement en mémoire de Spark. De plus, il est également capable de passer d'un à plusieurs GPU.

Toutes les bibliothèques RAPIDS sont basées sur Python et sont conçues pour avoir des interfaces similaires à Pandas et Sklearn afin de faciliter l'adoption.

La structure de RAPIDS est basée sur différentes bibliothèques afin d'accélérer la science des données de bout en bout. Ses principaux composants sont :

* cuDF = utilisé pour effectuer des tâches de traitement de données (similaire à Pandas).
* cuML = utilisé pour créer des modèles d'apprentissage automatique (similaire à Sklearn).
* cuGraph = utilisé pour effectuer des analyses de graphes (NetworkX).

Dans cet exemple, nous allons utiliser son intégration avec XGBoost :

```python
dtrain = xgb.DMatrix(X_train, label=y_train)
dtest = xgb.DMatrix(X_test, label=y_test)

%%time

params = {}
booster_params = {}
booster_params['tree_method'] = 'gpu_hist' 
params.update(booster_params)

clf = xgb.train(params, dtrain)
```

```
CPU times: user 1.42 s, sys: 719 ms, total: 2.14 s
Wall time: 2.51 s
```

Comme nous pouvons le voir ci-dessus, l'utilisation de RAPIDS a pris environ 2,5 secondes pour entraîner notre modèle (diminuant le temps d'exécution de près de 200 fois !). 

Enfin, nous pouvons maintenant vérifier que nous avons obtenu exactement la même précision de prédiction en utilisant RAPIDS que celle enregistrée dans les autres cas :

```
rapids_pred = clf.predict(dtest)

rapids_pred = np.round(rapids_pred)
rapids_acc = round(accuracy_score(y_test, rapids_pred), 2)
print("XGB accuracy using RAPIDS:", rapids_acc*100, '%')
```

```
XGB accuracy using RAPIDS: 99.0 %
```

Si vous êtes intéressé à en savoir plus sur RAPIDS, plus d'informations sont disponibles [ici](https://towardsdatascience.com/gpu-accelerated-data-analytics-machine-learning-963aebe956ce).

## Conclusion

Enfin, nous pouvons maintenant comparer le temps d'exécution des différentes méthodes utilisées. Comme le montre la Figure 2, l'utilisation de l'optimisation GPU peut réduire considérablement le temps d'exécution, surtout si elle est intégrée avec l'utilisation des bibliothèques RAPIDS.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/image-37.png)
_Figure 2 : Comparaison du temps d'exécution_

La Figure 3 montre combien de fois les modèles GPU sont plus rapides par rapport à nos résultats de base CPU.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/image-38.png)
_Figure 3 : Focus sur la comparaison du temps d'exécution CPU_

## Contacts

Si vous souhaitez rester informé de mes derniers articles et projets, [suivez-moi sur Medium](https://medium.com/@pierpaoloippolito28?source=post_page---------------------------) et abonnez-vous à ma [liste de diffusion](http://eepurl.com/gwO-Dr?source=post_page---------------------------). Voici quelques détails de mes contacts :

* [Linkedin](https://uk.linkedin.com/in/pier-paolo-ippolito-202917146?source=post_page---------------------------)
* [Blog Personnel](https://pierpaolo28.github.io/blog/?source=post_page---------------------------)
* [Site Web Personnel](https://pierpaolo28.github.io/?source=post_page---------------------------)
* [Profil Medium](https://towardsdatascience.com/@pierpaoloippolito28?source=post_page---------------------------)
* [GitHub](https://github.com/pierpaolo28?source=post_page---------------------------)
* [Kaggle](https://www.kaggle.com/pierpaolo28?source=post_page---------------------------)

Photo de couverture [de cet article](https://hardzone.es/noticias/tarjetas-graficas/nvidia-hopper-arquitectura-mcm/).