---
title: Comment construire et entraîner des modèles ML K-Nearest Neighbors et K-Means
  Clustering en Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-03T19:40:58.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-and-train-k-nearest-neighbors-ml-models-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/classificaton.png
tags:
- name: Machine Learning
  slug: machine-learning
- name: Python
  slug: python
seo_title: Comment construire et entraîner des modèles ML K-Nearest Neighbors et K-Means
  Clustering en Python
seo_desc: 'By Nick McCullum

  One of machine learning''s most popular applications is in solving classification
  problems.

  Classification problems are situations where you have a data set, and you want to
  classify observations from that data set into a specific cat...'
---

Par Nick McCullum

L'une des [applications les plus populaires de l'apprentissage automatique](https://gumroad.com/l/pGjwd) est la résolution de problèmes de classification.

Les problèmes de classification sont des situations où vous avez un ensemble de données et vous souhaitez classer les observations de cet ensemble de données dans une catégorie spécifique.

Un exemple célèbre est le filtre anti-spam pour les fournisseurs de messagerie. Gmail utilise des techniques d'apprentissage automatique supervisé pour placer automatiquement les e-mails dans votre dossier de spam en fonction de leur contenu, de leur ligne d'objet et d'autres caractéristiques.

Deux modèles d'apprentissage automatique effectuent une grande partie du travail lourd lorsqu'il s'agit de problèmes de classification :

* K-nearest neighbors
* K-means clustering

Ce tutoriel vous apprendra à coder les algorithmes K-nearest neighbors et K-means clustering en Python.

# Modèles K-Nearest Neighbors

L'algorithme [K-nearest neighbors](https://nickmccullum.com/python-machine-learning/k-nearest-neighbors-python/) est l'un des modèles d'apprentissage automatique les plus populaires au monde pour résoudre les problèmes de classification.

Un exercice courant pour les étudiants explorant l'apprentissage automatique est d'appliquer l'algorithme K nearest neighbors à un ensemble de données où les catégories ne sont pas connues. Un exemple réel de cela serait si vous deviez faire des prédictions en utilisant l'apprentissage automatique sur un ensemble de données d'informations gouvernementales classifiées.

Dans ce tutoriel, vous apprendrez à écrire votre premier algorithme d'apprentissage automatique K nearest neighbors en Python. Nous travaillerons avec un ensemble de données anonymes similaire à la situation décrite ci-dessus.

## **L'ensemble de données dont vous aurez besoin dans ce tutoriel**

La première chose que vous devez faire est de télécharger l'ensemble de données que nous utiliserons dans ce tutoriel. J'ai téléchargé le fichier sur [mon site web](https://nickmccullum.com/). Vous pouvez y accéder en cliquant [ici](https://nickmccullum.com/files/k-nearest-neighbors/classified_data.csv).

Maintenant que vous avez téléchargé l'ensemble de données, vous voudrez déplacer le fichier dans le répertoire dans lequel vous travaillerez. Après cela, ouvrez un [Jupyter Notebook](https://nickmccullum.com/python-course/jupyter-notebook-basics/) et nous pouvons commencer à écrire du code Python !

## **Les bibliothèques dont vous aurez besoin dans ce tutoriel**

Pour écrire un algorithme K nearest neighbors, nous utiliserons de nombreuses bibliothèques Python open-source, notamment [NumPy](https://nickmccullum.com/advanced-python/numpy/), [pandas](https://nickmccullum.com/advanced-python/pandas-dataframes/) et [scikit-learn](https://nickmccullum.com/python-machine-learning/introduction-scikit-learn/).

Commencez votre script Python en écrivant les instructions d'importation suivantes :

```py

import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

%matplotlib inline


```

## **Importation de l'ensemble de données dans notre script Python**

Notre prochaine étape consiste à importer le fichier `classified_data.csv` dans notre script Python. La bibliothèque pandas facilite l'[importation de données dans un DataFrame pandas](https://nickmccullum.com/advanced-python/pandas-data-input-output/).

Puisque l'ensemble de données est stocké dans un fichier `csv`, nous utiliserons la méthode `read_csv` pour cela :

```py

raw_data = pd.read_csv('classified_data.csv')


```

L'impression de ce DataFrame dans votre Jupyter Notebook vous donnera une idée de l'apparence des données :

![Un DataFrame pandas](https://nickmccullum.com/images/python-machine-learning/k-nearest-neighbors/pandas-dataframe.png)

Vous remarquerez que le DataFrame commence par une colonne sans nom dont les valeurs sont égales à l'index du DataFrame. Nous pouvons corriger cela en apportant un léger ajustement à la commande qui a importé notre ensemble de données dans le script Python :

```py

raw_data = pd.read_csv('classified_data.csv', index_col = 0)


```

Ensuite, examinons les caractéristiques réelles contenues dans cet ensemble de données. Vous pouvez imprimer une liste des noms de colonnes de l'ensemble de données avec l'instruction suivante :

```py

print(raw_data.columns)


```

Cela retourne :

```py

Index(['WTT', 'PTI', 'EQW', 'SBI', 'LQE', 'QWG', 'FDJ', 'PJF', 'HQE', 'NXJ',

       'TARGET CLASS'],

      dtype='object')


```

Puisque cet ensemble de données est classé, nous n'avons aucune idée de ce que signifient ces colonnes. Pour l'instant, il suffit de reconnaître que chaque colonne est de nature numérique et donc bien adaptée à la modélisation avec des techniques d'apprentissage automatique.

## **Standardisation de l'ensemble de données**

Puisque l'algorithme K nearest neighbors fait des prédictions sur un point de données en utilisant les observations qui lui sont les plus proches, l'échelle des caractéristiques au sein d'un ensemble de données compte beaucoup.

Pour cette raison, les praticiens de l'apprentissage automatique `standardisent` généralement l'ensemble de données, ce qui signifie ajuster chaque valeur `x` afin qu'elles soient approximativement sur la même échelle.

Heureusement, `scikit-learn` inclut une excellente fonctionnalité pour cela avec très peu de tracas.

Pour commencer, nous devrons importer la classe `StandardScaler` de `scikit-learn`. Ajoutez la commande suivante à votre script Python pour cela :

```py

from sklearn.preprocessing import StandardScaler


```

Cette fonction se comporte beaucoup comme les classes `LinearRegression` et `LogisticRegression` que nous avons utilisées plus tôt dans ce cours. Nous voudrons créer une instance de cette classe puis ajuster l'instance de cette classe sur notre ensemble de données.

Tout d'abord, créons une instance de la classe `StandardScaler` nommée `scaler` avec l'instruction suivante :

```

scaler = StandardScaler()


```

Nous pouvons maintenant entraîner cette instance sur notre ensemble de données en utilisant la méthode `fit` :

```py

scaler.fit(raw_data.drop('TARGET CLASS', axis=1))


```

Nous pouvons maintenant utiliser la méthode `transform` pour standardiser toutes les caractéristiques de l'ensemble de données afin qu'elles soient approximativement sur la même échelle. Nous attribuerons ces caractéristiques mises à l'échelle à la variable nommée `scaled_features` :

```py

scaled_features = scaler.transform(raw_data.drop('TARGET CLASS', axis=1))


```

Cela crée en fait un [tableau NumPy](https://nickmccullum.com/advanced-python/numpy-arrays/) de toutes les caractéristiques de l'ensemble de données, et nous voulons qu'il soit un [DataFrame pandas](https://nickmccullum.com/advanced-python/pandas-dataframes/) à la place.

Heureusement, c'est une correction facile. Nous envelopperons simplement la variable `scaled_features` dans une méthode `pd.DataFrame` et attribuerons ce DataFrame à une nouvelle variable appelée `scaled_data` avec un argument approprié pour spécifier les noms de colonnes :

```py

scaled_data = pd.DataFrame(scaled_features, columns = raw_data.drop('TARGET CLASS', axis=1).columns)


```

Maintenant que nous avons importé notre ensemble de données et standardisé ses caractéristiques, nous sommes prêts à diviser l'ensemble de données en données d'entraînement et données de test.

## **Division de l'ensemble de données en données d'entraînement et données de test**

Nous utiliserons la fonction `train_test_split` de `scikit-learn` combinée avec le déballage de liste pour créer des données d'entraînement et des données de test à partir de notre ensemble de données classifiées.

Tout d'abord, vous devrez importer `train_test_split` du module `model_validation` de `scikit-learn` avec l'instruction suivante :

```py

from sklearn.model_selection import train_test_split


```

Ensuite, nous devrons spécifier les valeurs `x` et `y` qui seront passées dans cette fonction `train_test_split`.

Les valeurs `x` seront le DataFrame `scaled_data` que nous avons créé précédemment. Les valeurs `y` seront la colonne `TARGET CLASS` de notre DataFrame `raw_data` original.

Vous pouvez créer ces variables avec les instructions suivantes :

```py

x = scaled_data

y = raw_data['TARGET CLASS']


```

Ensuite, vous devrez exécuter la fonction `train_test_split` en utilisant ces deux arguments et une taille de test raisonnable. Nous utiliserons une `test_size` de 30 %, ce qui donne les paramètres suivants pour la fonction :

```py

x_training_data, x_test_data, y_training_data, y_test_data = train_test_split(x, y, test_size = 0.3)


```

Maintenant que notre ensemble de données a été divisé en données d'entraînement et données de test, nous sommes prêts à commencer à entraîner notre modèle !

## **Entraînement d'un modèle K Nearest Neighbors**

Commençons par importer `KNeighborsClassifier` de `scikit-learn` :

```py

from sklearn.neighbors import KNeighborsClassifier


```

Ensuite, créons une instance de la classe `KNeighborsClassifier` et attribuons-la à une variable nommée `model`

Cette classe nécessite un paramètre nommé `n_neighbors`, qui est égal à la valeur `K` de l'algorithme K nearest neighbors que vous construisez. Pour commencer, spécifions `n_neighbors = 1` :

```py

model = KNeighborsClassifier(n_neighbors = 1)


```

Nous pouvons maintenant entraîner notre modèle K nearest neighbors en utilisant la méthode `fit` et nos variables `x_training_data` et `y_training_data` :

```py

model.fit(x_training_data, y_training_data)


```

Faisons maintenant quelques prédictions avec notre nouvel algorithme K nearest neighbors fraîchement entraîné !

## **Faire des prédictions avec notre algorithme K Nearest Neighbors**

Nous pouvons faire des prédictions avec notre algorithme K nearest neighbors de la même manière que nous l'avons fait avec nos modèles de [régression linéaire](https://nickmccullum.com/python-machine-learning/linear-regression-python/) et de [régression logistique](https://nickmccullum.com/python-machine-learning/logistic-regression-python/) plus tôt dans ce cours : en utilisant la méthode `predict` et en passant notre variable `x_test_data`.

Plus précisément, voici comment vous pouvez faire des prédictions et les attribuer à une variable appelée `predictions` :

```py

predictions = model.predict(x_test_data)


```

Explorons à quel point nos `predictions` sont précises dans la prochaine section de ce tutoriel.

## **Mesurer la précision de notre modèle**

Nous avons vu dans notre tutoriel sur la régression logistique que `scikit-learn` vient avec des fonctions intégrées qui facilitent la mesure de la performance des modèles de classification d'apprentissage automatique.

Importons deux de ces fonctions (`classification_report` et `confuson_matrix`) dans notre rapport maintenant :

```py

from sklearn.metrics import classification_report

from sklearn.metrics import confusion_matrix


```

Travaillons à travers chacune de ces fonctions une par une, en commençant par le `classfication_report`. Vous pouvez générer le rapport avec l'instruction suivante :

```py

print(classification_report(y_test_data, predictions))


```

Cela génère :

```py

             precision    recall  f1-score   support

           0       0.94      0.85      0.89       150

           1       0.86      0.95      0.90       150

    accuracy                           0.90       300

   macro avg       0.90      0.90      0.90       300

weighted avg       0.90      0.90      0.90       300


```

De même, vous pouvez générer une matrice de confusion avec l'instruction suivante :

```py

print(confusion_matrix(y_test_data, predictions))


```

Cela génère :

```py

[[141  12]

 [ 18 129]]


```

En regardant ces métriques de performance, il semble que notre modèle soit déjà assez performant. Il peut encore être amélioré.

Dans la prochaine section, nous verrons comment nous pouvons améliorer la performance de notre modèle K nearest neighbors en choisissant une meilleure valeur pour `K`.

## **Choisir une valeur optimale de `K` en utilisant la méthode du coude**

Dans cette section, nous utiliserons la méthode du coude pour choisir une valeur optimale de `K` pour notre algorithme K nearest neighbors.

La méthode du coude implique d'itérer à travers différentes valeurs de K et de sélectionner la valeur avec le taux d'erreur le plus bas lorsqu'elle est appliquée à nos données de test.

Pour commencer, créons une liste vide appelée `error_rates`. Nous allons parcourir différentes valeurs de `K` et ajouter leurs taux d'erreur à cette liste.

```py

error_rates = []


```

Ensuite, nous devons créer une boucle Python qui itère à travers les différentes valeurs de `K` que nous aimerions tester et exécute la fonctionnalité suivante à chaque itération :

* Crée une nouvelle instance de la classe `KNeighborsClassifier` de `scikit-learn`
* Entraîne le nouveau modèle en utilisant nos données d'entraînement
* Fait des prédictions sur nos données de test
* Calcule la différence moyenne pour chaque prédiction incorrecte (plus celle-ci est faible, plus notre modèle est précis)

Voici le code pour cela pour des valeurs de `K` entre `1` et `100` :

```py

for i in np.arange(1, 101):

    new_model = KNeighborsClassifier(n_neighbors = i)

    new_model.fit(x_training_data, y_training_data)

    new_predictions = new_model.predict(x_test_data)

    error_rates.append(np.mean(new_predictions != y_test_data))


```

Visualisons comment notre taux d'erreur change avec différentes valeurs de `K` en utilisant une visualisation rapide matplotlib :

```py

plt.plot(error_rates)


```

![Un graphique de nos taux d'erreur](https://nickmccullum.com/images/python-machine-learning/k-nearest-neighbors/error-rates.png)

Comme vous pouvez le voir, nos taux d'erreur tendent à être minimisés avec une valeur de `K` d'environ 50. Cela signifie que `50` est un choix approprié pour `K` qui équilibre à la fois la simplicité et la puissance prédictive.

## **Le code complet pour ce tutoriel**

Vous pouvez consulter le code complet de ce tutoriel dans [ce dépôt GitHub](https://github.com/nicholasmccullum/python-machine-learning). Il est également collé ci-dessous pour votre référence :

```py

#Importations courantes

import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

%matplotlib inline

#Importer l'ensemble de données

raw_data = pd.read_csv('classified_data.csv', index_col = 0)

#Importer les fonctions de standardisation de scikit-learn

from sklearn.preprocessing import StandardScaler

#Standardiser l'ensemble de données

scaler = StandardScaler()

scaler.fit(raw_data.drop('TARGET CLASS', axis=1))

scaled_features = scaler.transform(raw_data.drop('TARGET CLASS', axis=1))

scaled_data = pd.DataFrame(scaled_features, columns = raw_data.drop('TARGET CLASS', axis=1).columns)

#Diviser l'ensemble de données en données d'entraînement et données de test

from sklearn.model_selection import train_test_split

x = scaled_data

y = raw_data['TARGET CLASS']

x_training_data, x_test_data, y_training_data, y_test_data = train_test_split(x, y, test_size = 0.3)

#Entraîner le modèle et faire des prédictions

from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier(n_neighbors = 1)

model.fit(x_training_data, y_training_data)

predictions = model.predict(x_test_data)

#Mesure de la performance

from sklearn.metrics import classification_report

from sklearn.metrics import confusion_matrix

print(classification_report(y_test_data, predictions))

print(confusion_matrix(y_test_data, predictions))

#Sélectionner une valeur optimale de K

error_rates = []

for i in np.arange(1, 101):

    new_model = KNeighborsClassifier(n_neighbors = i)

    new_model.fit(x_training_data, y_training_data)

    new_predictions = new_model.predict(x_test_data)

    error_rates.append(np.mean(new_predictions != y_test_data))

plt.figure(figsize=(16,12))

plt.plot(error_rates)

```

# Modèles de clustering K-Means

L'algorithme de [clustering K-means](https://nickmccullum.com/python-machine-learning/k-means-clustering-python/) est généralement le premier modèle d'apprentissage automatique non supervisé que les étudiants apprendront.

Il permet aux praticiens de l'apprentissage automatique de créer des groupes de points de données au sein d'un ensemble de données avec des caractéristiques quantitatives similaires. Il est utile pour résoudre des problèmes comme la création de segments de clients ou l'identification de localités dans une ville avec des taux de criminalité élevés.

Dans cette section, vous apprendrez à construire votre premier algorithme de clustering K-means en Python.

## **L'ensemble de données que nous utiliserons dans ce tutoriel**

Dans ce tutoriel, nous utiliserons un ensemble de données généré à l'aide de `scikit-learn`.

Importons la fonction `make_blobs` de `scikit-learn` pour créer ces données artificielles. Ouvrez un [Jupyter Notebook](https://nickmccullum.com/python-course/jupyter-notebook-basics/) et commencez votre script Python avec l'instruction suivante :

```py

from sklearn.datasets import make_blobs


```

Maintenant, utilisons la fonction `make_blobs` pour créer des données artificielles !

Plus précisément, voici comment vous pourriez créer un ensemble de données avec `200` échantillons qui a `2` caractéristiques et `4` centres de clusters. L'écart-type au sein de chaque cluster sera défini à `1.8`.

```py

raw_data = make_blobs(n_samples = 200, n_features = 2, centers = 4, cluster_std = 1.8)


```

Si vous imprimez cet objet `raw_data`, vous remarquerez qu'il s'agit en fait d'un [tuple Python](https://nickmccullum.com/python-course/tuples/). Le premier élément de ce tuple est un [tableau NumPy](https://nickmccullum.com/advanced-python/numpy-arrays/) avec 200 observations. Chaque observation contient 2 caractéristiques (comme nous l'avons spécifié avec notre fonction `make_blobs` !).

Maintenant que nos données ont été créées, nous pouvons passer à l'importation d'autres bibliothèques open-source importantes dans notre script Python.

## **Les importations que nous utiliserons dans ce tutoriel**

Ce tutoriel utilisera un certain nombre de bibliothèques Python open-source populaires, notamment [pandas](https://nickmccullum.com/advanced-python/pandas/), [NumPy](https://nickmccullum.com/advanced-python/numpy/), et [matplotlib](https://nickmccullum.com/python-visualization/how-to-import-matplotlib/). Continuons notre script Python en ajoutant les importations suivantes :

```py

import pandas as pd

import numpy as np

import seaborn

import matplotlib.pyplot as plt

%matplotlib inline


```

Le premier groupe d'importations dans ce bloc de code est pour manipuler de grands ensembles de données. Le deuxième groupe d'importations est pour créer des visualisations de données.

Passons à la visualisation de notre ensemble de données ensuite.

## **Visualisation de notre ensemble de données**

Dans notre fonction `make_blobs`, nous avons spécifié que notre ensemble de données devait avoir 4 centres de clusters. La meilleure façon de vérifier que cela a été géré correctement est de créer quelques visualisations de données rapides.

Pour commencer, utilisons la commande suivante pour tracer toutes les lignes de la première colonne de notre ensemble de données par rapport à toutes les lignes de la deuxième colonne de notre ensemble de données :

![Un nuage de points de nos données artificielles](https://nickmccullum.com/images/python-machine-learning/k-means-clustering/first-scatterplot.png)

_Note : votre ensemble de données apparaîtra différemment du mien puisque ce sont des données générées aléatoirement._

Cette image semble indiquer que notre ensemble de données n'a que trois clusters. Cela est dû au fait que deux des clusters sont très proches l'un de l'autre.

Pour corriger cela, nous devons nous référer au deuxième élément de notre tuple `raw_data`, qui est un tableau NumPy contenant le cluster auquel appartient chaque observation.

Si nous colorons notre ensemble de données en utilisant le cluster de chaque observation, les clusters uniques deviendront rapidement clairs. Voici le code pour cela :

```py

plt.scatter(raw_data[0][:,0], raw_data[0][:,1], c=raw_data[1])


```

![Un nuage de points de nos données artificielles](https://nickmccullum.com/images/python-machine-learning/k-means-clustering/second-scatterplot.png)

Nous pouvons maintenant voir que notre ensemble de données a quatre clusters uniques. Passons à la construction de notre modèle de clustering K-means en Python !

## **Construction et entraînement de notre modèle de clustering K-Means**

La première étape pour construire notre algorithme de clustering K-means est de l'importer de `scikit-learn`. Pour cela, ajoutez la commande suivante à votre script Python :

```py

from sklearn.cluster import KMeans


```

Ensuite, créons une instance de cette classe `KMeans` avec un paramètre de `n_clusters=4` et attribuons-la à la variable `model` :

```py

model = KMeans(n_clusters=4)


```

Maintenant, entraîons notre modèle en invoquant la méthode `fit` sur celui-ci et en passant le premier élément de notre tuple `raw_data` :

```py

model.fit(raw_data[0])


```

Dans la section suivante, nous explorerons comment faire des prédictions avec ce modèle de clustering K-means.

Avant de continuer, je voulais souligner une différence que vous avez peut-être remarquée entre le processus de construction de cet algorithme de clustering K-means (qui est un algorithme d'apprentissage automatique non supervisé) et les algorithmes d'apprentissage automatique supervisés avec lesquels nous avons travaillé jusqu'à présent dans ce cours.

À savoir, nous n'avons pas eu à diviser l'ensemble de données en données d'entraînement et données de test. C'est une différence importante - et en fait, vous n'avez jamais besoin de faire la division train/test sur un ensemble de données lors de la construction de modèles d'apprentissage automatique non supervisés !

## **Faire des prédictions avec notre modèle de clustering K-Means**

Les praticiens de l'apprentissage automatique utilisent généralement les algorithmes de clustering K-means pour faire deux types de prédictions :

* À quel cluster chaque point de données appartient
* Où se trouve le centre de chaque cluster

Il est facile de générer ces prédictions maintenant que notre modèle a été entraîné.

Tout d'abord, prédisons à quel cluster chaque point de données appartient. Pour cela, accédez à l'attribut `labels_` de notre objet `model` en utilisant l'opérateur point, comme ceci :

```py

model.labels_


```

Cela génère un tableau NumPy avec des prédictions pour chaque point de données qui ressemble à ceci :

```py

array([3, 2, 7, 0, 5, 1, 7, 7, 6, 1, 2, 4, 6, 7, 6, 4, 4, 3, 3, 6, 0, 0,

       6, 4, 5, 6, 0, 2, 6, 5, 4, 3, 4, 2, 6, 6, 6, 5, 6, 2, 1, 1, 3, 4,

       3, 5, 7, 1, 7, 5, 3, 6, 0, 3, 5, 5, 7, 1, 3, 1, 5, 7, 7, 0, 5, 7,

       3, 4, 0, 5, 6, 5, 1, 4, 6, 4, 5, 6, 7, 2, 2, 0, 4, 1, 1, 1, 6, 3,

       3, 7, 3, 6, 7, 7, 0, 3, 4, 3, 4, 0, 3, 5, 0, 3, 6, 4, 3, 3, 4, 6,

       1, 3, 0, 5, 4, 2, 7, 0, 2, 6, 4, 2, 1, 4, 7, 0, 3, 2, 6, 7, 5, 7,

       5, 4, 1, 7, 2, 4, 7, 7, 4, 6, 6, 3, 7, 6, 4, 5, 5, 5, 7, 0, 1, 1,

       0, 0, 2, 5, 0, 3, 2, 5, 1, 5, 6, 5, 1, 3, 5, 1, 2, 0, 4, 5, 6, 3,

       4, 4, 5, 6, 4, 4, 2, 1, 7, 4, 6, 6, 0, 6, 3, 5, 0, 5, 2, 4, 6, 0,

       1, 0], dtype=int32)


```

Pour voir où se trouve le centre de chaque cluster, accédez à l'attribut `cluster_centers_` en utilisant l'opérateur point comme ceci :

```py

model.cluster_centers_


```

Cela génère un tableau NumPy à deux dimensions qui contient les coordonnées du centre de chaque cluster. Il ressemblera à ceci :

```py

array([[ -8.06473328,  -0.42044783],

       [  0.15944397,  -9.4873621 ],

       [  1.49194628,   0.21216413],

       [-10.97238157,  -2.49017206],

       [  3.54673215,  -9.7433692 ],

       [ -3.41262049,   7.80784834],

       [  2.53980034,  -2.96376999],

       [ -0.4195847 ,   6.92561289]])


```

Nous évaluerons la précision de ces prédictions dans la section suivante.

## **Visualisation de la précision de notre modèle**

La dernière chose que nous ferons dans ce tutoriel est de visualiser la précision de notre modèle. Vous pouvez utiliser le code suivant pour cela :

```py

f, (ax1, ax2) = plt.subplots(1, 2, sharey=True,figsize=(10,6))

ax1.set_title('Notre Modèle')

ax1.scatter(raw_data[0][:,0], raw_data[0][:,1],c=model.labels_)

ax2.set_title('Données Originales')

ax2.scatter(raw_data[0][:,0], raw_data[0][:,1],c=raw_data[1])


```

Cela génère deux graphiques différents côte à côte où un graphique montre les clusters selon l'ensemble de données réel et l'autre graphique montre les clusters selon notre modèle. Voici à quoi ressemble la sortie :

![Un nuage de points des prédictions de notre modèle](https://nickmccullum.com/images/python-machine-learning/k-means-clustering/k-means-clustering-subplots.png)

Bien que la coloration entre les deux graphiques soit différente, vous pouvez voir que notre modèle a fait un assez bon travail de prédiction des clusters au sein de notre ensemble de données. Vous pouvez également voir que le modèle n'était pas parfait - si vous regardez les points de données le long du bord d'un cluster, vous pouvez voir qu'il a parfois mal classé une observation de notre ensemble de données.

Il y a une dernière chose qui doit être mentionnée concernant la mesure de la prédiction de notre modèle. Dans cet exemple, nous savions à quel cluster chaque observation appartenait parce que nous avons en fait généré cet ensemble de données nous-mêmes.

Cela est très inhabituel. Le clustering K-means est plus souvent appliqué lorsque les clusters ne sont pas connus à l'avance. Au lieu de cela, les praticiens de l'apprentissage automatique utilisent le clustering K-means pour trouver des motifs qu'ils ne connaissent pas déjà au sein d'un ensemble de données.

## **Le code complet pour ce tutoriel**

Vous pouvez consulter le code complet de ce tutoriel dans [ce dépôt GitHub](https://github.com/nicholasmccullum/python-machine-learning). Il est également collé ci-dessous pour votre référence :

```py

#Créer un ensemble de données artificiel

from sklearn.datasets import make_blobs

raw_data = make_blobs(n_samples = 200, n_features = 2, centers = 4, cluster_std = 1.8)

#Importations de données

import pandas as pd

import numpy as np

#Importations de visualisation

import seaborn

import matplotlib.pyplot as plt

%matplotlib inline

#Visualiser les données

plt.scatter(raw_data[0][:,0], raw_data[0][:,1])

plt.scatter(raw_data[0][:,0], raw_data[0][:,1], c=raw_data[1])

#Construire et entraîner le modèle

from sklearn.cluster import KMeans

model = KMeans(n_clusters=4)

model.fit(raw_data[0])

#Voir les prédictions

model.labels_

model.cluster_centers_

#Tracer les prédictions par rapport à l'ensemble de données original

f, (ax1, ax2) = plt.subplots(1, 2, sharey=True,figsize=(10,6))

ax1.set_title('Notre Modèle')

ax1.scatter(raw_data[0][:,0], raw_data[0][:,1],c=model.labels_)

ax2.set_title('Données Originales')

ax2.scatter(raw_data[0][:,0], raw_data[0][:,1],c=raw_data[1])

```

## Réflexions finales

Ce tutoriel vous a appris comment construire des modèles d'apprentissage automatique K-nearest neighbors et K-means clustering en Python.

**Si vous êtes intéressé à en apprendre davantage sur l'apprentissage automatique, mon livre [Pragmatic Machine Learning](https://gumroad.com/l/pGjwd) vous enseignera des techniques pratiques d'apprentissage automatique en construisant 9 projets réels. Le livre sera lancé le 3 août. Vous pouvez le précommander avec 50 % de réduction en utilisant le lien ci-dessous :**

%[https://gumroad.com/l/pGjwd]

Voici un bref résumé de ce que vous avez appris sur les modèles K-nearest neighbors en Python :

* Comment les données classifiées sont un outil courant utilisé pour enseigner aux étudiants comment résoudre leurs premiers problèmes de K nearest neighbor
* Pourquoi il est important de standardiser votre ensemble de données lors de la construction de modèles K nearest neighbor
* Comment diviser votre ensemble de données en données d'entraînement et données de test en utilisant la fonction `train_test_split`
* Comment entraîner votre premier modèle K nearest neighbors et faire des prédictions avec celui-ci
* Comment mesurer la performance d'un modèle K nearest neighbors
* Comment utiliser la méthode du coude pour sélectionner une valeur optimale de K dans un modèle K nearest neighbors

De même, voici un bref résumé de ce que vous avez appris sur les modèles de clustering K-means en Python :

* Comment créer des données artificielles dans `scikit-learn` en utilisant la fonction `make_blobs`
* Comment construire et entraîner un modèle de clustering K-means
* Que les techniques d'apprentissage automatique non supervisées ne nécessitent pas de diviser vos données en données d'entraînement et données de test
* Comment construire et entraîner un modèle de clustering K-means en utilisant `scikit-learn`
* Comment visualiser la performance d'un algorithme de clustering K-means lorsque vous connaissez les clusters à l'avance