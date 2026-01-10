---
title: 'Tutoriel sur le classificateur Random Forest : Comment utiliser les algorithmes
  basés sur les arbres pour le Machine Learning'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-06T21:53:40.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-the-tree-based-algorithm-for-machine-learning
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/0_hOa0fVvazQigNgB2.jpg
tags:
- name: algorithms
  slug: algorithms
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: Trees
  slug: trees
seo_title: 'Tutoriel sur le classificateur Random Forest : Comment utiliser les algorithmes
  basés sur les arbres pour le Machine Learning'
seo_desc: 'By Davis David

  Tree-based algorithms are popular machine learning methods used to solve supervised
  learning problems. These algorithms are flexible and can solve any kind of problem
  at hand (classification or regression).

  Tree-based algorithms tend t...'
---

Par Davis David

Les algorithmes basés sur les arbres sont des méthodes populaires d'apprentissage automatique utilisées pour résoudre des problèmes d'apprentissage supervisé. Ces algorithmes sont flexibles et peuvent résoudre tout type de problème (classification ou régression).

Les algorithmes basés sur les arbres tendent à utiliser la **moyenne** pour les caractéristiques continues ou le **mode** pour les caractéristiques catégorielles lors de la réalisation de prédictions sur les échantillons d'entraînement dans les régions auxquelles ils appartiennent. Ils produisent également des prédictions avec une **grande précision**, une **stabilité** et une **facilité d'interprétation**.

# Exemples d'algorithmes basés sur les arbres

Il existe différents algorithmes basés sur les arbres que vous pouvez utiliser, tels que

* Arbres de décision
* Forêt aléatoire
* Gradient Boosting
* Bagging (Bootstrap Aggregation)

Ainsi, chaque scientifique des données devrait apprendre ces algorithmes et les utiliser dans leurs projets de machine learning.

Dans cet article, vous en apprendrez davantage sur l'algorithme de forêt aléatoire. Après avoir terminé cet article, vous devriez être compétent dans l'utilisation de l'algorithme de forêt aléatoire pour résoudre et construire des modèles prédictifs pour des problèmes de classification avec scikit-learn.

# Qu'est-ce que la forêt aléatoire ?

La forêt aléatoire est l'un des algorithmes d'apprentissage supervisé basés sur les arbres les plus populaires. C'est aussi le plus flexible et le plus facile à utiliser.

L'algorithme peut être utilisé pour résoudre à la fois des problèmes de classification et de régression. La forêt aléatoire tend à combiner des centaines d'**arbres de décision** puis entraîne chaque arbre de décision sur un échantillon différent des observations.

Les prédictions finales de la forêt aléatoire sont faites en moyennant les prédictions de chaque arbre individuel.

Les avantages des forêts aléatoires sont nombreux. Les arbres de décision individuels tendent à **surajuster** les données d'entraînement, mais la forêt aléatoire peut atténuer ce problème en **moyennant** les résultats de prédiction de différents arbres. Cela donne aux forêts aléatoires une précision prédictive plus élevée qu'un seul arbre de décision.

L'algorithme de forêt aléatoire peut également vous aider à trouver les caractéristiques **importantes** dans votre ensemble de données. Il est à la base de l'[algorithme Boruta](https://towardsdatascience.com/boruta-explained-the-way-i-wish-someone-explained-it-to-me-4489d70e154a), qui sélectionne les caractéristiques importantes dans un ensemble de données.

La forêt aléatoire a été utilisée dans une variété d'applications, par exemple pour fournir des recommandations de différents produits aux clients dans le commerce électronique.

En médecine, un algorithme de forêt aléatoire peut être utilisé pour identifier la maladie du patient en analysant le dossier médical du patient.

De plus, dans le secteur bancaire, il peut être utilisé pour déterminer facilement si le client est frauduleux ou légitime.

# Comment fonctionne l'algorithme de forêt aléatoire ?

L'algorithme de forêt aléatoire fonctionne en complétant les étapes suivantes :

**Étape 1** : L'algorithme sélectionne des échantillons aléatoires à partir de l'ensemble de données fourni.

**Étape 2** : L'algorithme créera un arbre de décision pour chaque échantillon sélectionné. Ensuite, il obtiendra un résultat de prédiction de chaque arbre de décision créé.

**Étape 3** : Un vote sera ensuite effectué pour chaque résultat prédit. Pour un problème de classification, il utilisera le **mode**, et pour un problème de régression, il utilisera la **moyenne**.

**Étape 4** : Enfin, l'algorithme sélectionnera le résultat de prédiction le plus voté comme prédiction finale.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/how-random-forest-classifier-work.PNG)
_fonctionnement_

# Random Forest en pratique

Maintenant que vous connaissez les tenants et aboutissants de l'algorithme de forêt aléatoire, construisons un classificateur de forêt aléatoire.

Nous allons construire un classificateur de forêt aléatoire en utilisant l'ensemble de données sur le diabète des Indiens Pima. L'ensemble de données sur le diabète des Indiens Pima implique de prédire l'apparition du diabète dans les 5 ans sur la base des détails médicaux fournis. Il s'agit d'un problème de classification binaire.

Notre tâche consiste à analyser et à créer un modèle sur l'ensemble de données sur le diabète des Indiens Pima pour prédire si un patient particulier est à risque de développer un diabète, étant donné d'autres facteurs indépendants.

Nous commencerons par importer des packages importants que nous utiliserons pour charger l'ensemble de données et créer un classificateur de forêt aléatoire. Nous utiliserons la bibliothèque [scikit-learn](http://scikit-learn.org/stable/tutorial/index.html) pour charger et utiliser l'algorithme de forêt aléatoire.

```python
# import important packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import pandas_profiling

from matplotlib import rcParams
import warnings

warnings.filterwarnings("ignore")

# figure size in inches
rcParams["figure.figsize"] = 10, 6
np.random.seed(42)
```

### Dataset

Ensuite, chargez l'ensemble de données à partir du répertoire de données :

```python
# Load dataset
data = pd.read_csv("../data/pima_indians_diabetes.csv")
```

Maintenant, nous pouvons observer un échantillon de l'ensemble de données.

```python

# show sample of the dataset
data.sample(5)
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/5-rows.PNG)

Comme vous pouvez le voir, dans notre ensemble de données, nous avons différentes caractéristiques avec des valeurs numériques.

Comprenons la liste des caractéristiques que nous avons dans cet ensemble de données.

```python
# show columns
data.columns
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/columns.PNG)

Dans cet ensemble de données, il y a 8 caractéristiques d'entrée et 1 caractéristique de sortie / cible. Les valeurs manquantes sont censées être encodées avec des valeurs nulles. La signification des noms de variables est la suivante (de la première à la dernière caractéristique) :

* Nombre de fois enceinte.
* Concentration de glucose plasmatique à 2 heures dans un test de tolérance au glucose oral.
* Pression artérielle diastolique (mm Hg).
* Épaisseur du pli cutané du triceps (mm).
* Insuline sérique à 2 heures (mu U/ml).
* Indice de masse corporelle (poids en kg/(taille en m)^2).
* Fonction de pedigree du diabète.
* Âge (années).
* Variable de classe (0 ou 1).

Ensuite, nous divisons l'ensemble de données en caractéristiques indépendantes et en caractéristique cible. Notre caractéristique cible pour cet ensemble de données s'appelle **class.**

```python
# split data into input and taget variable(s)

X = data.drop("class", axis=1)
y = data["class"]
```

### Prétraitement de l'ensemble de données

Avant de créer un modèle, nous devons standardiser nos caractéristiques indépendantes en utilisant la méthode `standardScaler` de scikit-learn.

```python
# standardize the dataset
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

Vous pouvez en apprendre davantage sur la manière et les raisons de standardiser vos données en cliquant [ici](https://towardsdatascience.com/how-and-why-to-standardize-your-data-996926c2c832).

### Division de l'ensemble de données en données d'entraînement et de test

Nous divisons maintenant notre ensemble de données traité en données d'entraînement et de test. Les données de test représenteront 10 % de l'ensemble de données traité.

```python
# split into train and test set
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, stratify=y, test_size=0.10, random_state=42
)
```

### Construction du classificateur de forêt aléatoire

Il est maintenant temps de créer notre classificateur de forêt aléatoire et de l'entraîner sur l'ensemble d'entraînement. Nous passerons également le nombre d'arbres (100) dans la forêt que nous voulons utiliser via le paramètre appelé **n_estimators.**

```python
# create the classifier
classifier = RandomForestClassifier(n_estimators=100)

# Train the model using the training sets
classifier.fit(X_train, y_train)
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/default-parameters.PNG)

La sortie ci-dessus montre différentes valeurs de paramètres du classificateur de forêt aléatoire utilisées lors du processus d'entraînement sur les données d'entraînement.

Après l'entraînement, nous pouvons effectuer une prédiction sur les données de test.

```python
# predictin on the test set
y_pred = classifier.predict(X_test)
```

Ensuite, nous vérifions la précision en utilisant les valeurs réelles et prédites des données de test.

```python
# Calculate Model Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))
```

Accuracy: 0.8051948051948052

Notre précision est d'environ 80,5 %, ce qui est bon. Mais nous pouvons toujours l'améliorer.

### Identifier les caractéristiques importantes

Comme je l'ai dit précédemment, nous pouvons également vérifier les caractéristiques importantes en utilisant la variable **feature_importances_** de l'algorithme de forêt aléatoire dans scikit-learn.

```python
# check Important features
feature_importances_df = pd.DataFrame(
    {"feature": list(X.columns), "importance": classifier.feature_importances_}
).sort_values("importance", ascending=False)

# Display
feature_importances_df
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/feature-importance-list.PNG)
_Caractéristiques importantes_

La figure ci-dessus montre l'importance relative des caractéristiques et leur contribution au modèle. Nous pouvons également visualiser ces caractéristiques et leurs scores en utilisant les bibliothèques seaborn et matplotlib.

```python
# visualize important featuers

# Creating a bar plot
sns.barplot(x=feature_importances_df.feature, y=feature_importances_df.importance)
# Add labels to your

plt.xlabel("Score d'importance des caractéristiques")
plt.ylabel("Caractéristiques")
plt.title("Visualisation des caractéristiques importantes")
plt.xticks(
    rotation=45, horizontalalignment="right", fontweight="light", fontsize="x-large"
)
plt.show()
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/visualize-feature-importance.PNG)

D'après la figure ci-dessus, vous pouvez voir que la **caractéristique triceps_skinfold_thickness** a une faible importance et ne contribue pas beaucoup à la prédiction.

Cela signifie que nous pouvons supprimer cette caractéristique et entraîner à nouveau notre classificateur de forêt aléatoire, puis voir si cela peut améliorer ses performances sur les données de test.

```python
# load data with selected features
X = data.drop(["class", "triceps_skinfold_thickness"], axis=1)
y = data["class"]

# standardize the dataset
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# split into train and test set
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, stratify=y, test_size=0.10, random_state=42
)
```

Nous allons entraîner l'algorithme de forêt aléatoire avec les caractéristiques sélectionnées et traitées de notre ensemble de données, effectuer des prédictions, puis trouver la précision du modèle.

```python
# Create a Random Classifier
clf = RandomForestClassifier(n_estimators=100)

# Train the model using the training sets
clf.fit(X_train, y_train)

# prediction on test set
y_pred = clf.predict(X_test)

# Calculate Model Accuracy,
print("Accuracy:", accuracy_score(y_test, y_pred))
```

Accuracy: 0.8181818181818182

Maintenant, la précision du modèle est passée de **80,5%** à **81,8%** après avoir supprimé la caractéristique la moins importante appelée _triceps_skinfold_thickness_.

Cela suggère qu'il est très important de vérifier les caractéristiques importantes et de voir si vous pouvez supprimer les caractéristiques les moins importantes pour augmenter les performances de votre modèle.

# Conclusion

Les algorithmes basés sur les arbres sont vraiment importants pour chaque scientifique des données à apprendre. Dans cet article, vous avez appris les bases des algorithmes basés sur les arbres et comment créer un modèle de classification en utilisant l'algorithme de forêt aléatoire.

Je vous recommande également d'essayer d'autres types d'algorithmes basés sur les arbres tels que l'[algorithme Extra-trees](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html#sklearn.ensemble.ExtraTreesClassifier).

Vous pouvez télécharger l'ensemble de données et le notebook utilisés dans cet article ici : [https://github.com/Davisy/Random-Forest-classification-Tutorial](https://github.com/Davisy/Random-Forest-classification-Tutorial)

Félicitations, vous êtes arrivé à la fin de cet article !

Si vous avez appris quelque chose de nouveau ou si vous avez apprécié la lecture de cet article, veuillez le partager afin que d'autres puissent le voir. En attendant, à la prochaine ! Vous pouvez également me joindre sur Twitter [@Davis_McDavid](https://twitter.com/Davis_McDavid)