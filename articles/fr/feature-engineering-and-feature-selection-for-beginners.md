---
title: Tutoriel de Machine Learning – Ingénierie des caractéristiques et sélection
  des caractéristiques pour débutants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-04-07T01:06:07.000Z'
originalURL: https://freecodecamp.org/news/feature-engineering-and-feature-selection-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/tools-864983_1920.jpg
tags:
- name: data analysis
  slug: data-analysis
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: Python
  slug: python
seo_title: Tutoriel de Machine Learning – Ingénierie des caractéristiques et sélection
  des caractéristiques pour débutants
seo_desc: 'By Davis David

  They say data is the new oil, but we don''t use oil directly from its source. It
  has to be processed and cleaned before we use it for different purposes.

  The same applies to data, we don''t use it directly from its source. It also has
  to...'
---

Par Davis David

On dit que les **données** sont le nouveau **pétrole**, mais nous n'utilisons pas le pétrole directement depuis sa source. Il doit être traité et nettoyé avant de pouvoir être utilisé pour différentes fins.

Il en va de même pour les données, nous ne les utilisons pas directement depuis leur source. Elles doivent également être traitées.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/imageonline-co-merged-image.png)
_Industrie pétrolière_

Cela peut être un défi pour les débutants en Machine Learning et en Data Science car les données proviennent de différentes sources avec différents types de données. Par conséquent, vous ne pouvez pas appliquer la même méthode de nettoyage et de traitement à différents types de données. 

> "L'information peut être extraite des données tout comme l'énergie peut être extraite du pétrole." - [Adeola Adesina](https://medium.com/@adeolaadesina)

Vous devez apprendre et appliquer des méthodes en fonction des données que vous avez. Ensuite, vous pouvez en tirer des informations ou les utiliser pour l'entraînement dans des algorithmes de machine learning ou de deep learning.

Après avoir lu cet article, vous saurez :

* Ce qu'est l'ingénierie des caractéristiques et la sélection des caractéristiques.
* Différentes méthodes pour gérer les données manquantes dans votre ensemble de données.
* Différentes méthodes pour gérer les caractéristiques continues.
* Différentes méthodes pour gérer les caractéristiques catégorielles.
* Différentes méthodes pour la sélection des caractéristiques.

Commençons.🚀

# Qu'est-ce que l'ingénierie des caractéristiques ?

L'ingénierie des caractéristiques fait référence à un processus de sélection et de **transformation** des variables/caractéristiques dans votre ensemble de données lors de la création d'un **modèle prédictif** utilisant le machine learning. 

Par conséquent, vous devez extraire les caractéristiques de l'**ensemble de données brut** que vous avez collecté avant d'entraîner vos données dans des algorithmes de machine learning.   
Sinon, il sera difficile d'obtenir de bonnes informations à partir de vos données.

> Torturez les données, et elles avoueront n'importe quoi. — Ronald Coase

L'ingénierie des caractéristiques a deux objectifs :

* Préparer l'ensemble de données d'entrée approprié, compatible avec les exigences de l'algorithme de machine learning.
* Améliorer les **performances** des modèles de machine learning.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Picture1.jpg)
_Enquête CrowdFlower_

Selon une enquête menée auprès de 80 Data Scientists par CrowdFlower, les Data Scientists passent **60%** de leur temps à nettoyer et organiser les données. C'est pourquoi avoir des compétences en ingénierie et sélection des caractéristiques est très important.  

> "À la fin de la journée, certains projets de machine learning réussissent, et d'autres échouent. Qu'est-ce qui fait la différence ? De loin, le facteur le plus important est les **caractéristiques** utilisées." — Prof. Pedro Domingos de l'Université de Washington

Vous pouvez lire son article à partir du lien suivant : "[A Few Useful Things to Know About Machine Learning](https://homes.cs.washington.edu/~pedrod/papers/cacm12.pdf)".

Maintenant que vous savez pourquoi vous devez apprendre différentes techniques d'ingénierie des caractéristiques, commençons par apprendre différentes méthodes pour gérer les données manquantes.

## Comment gérer les données manquantes

Gérer les données manquantes est très important car de nombreux algorithmes de machine learning ne supportent pas les données avec des valeurs manquantes. Si vous avez des valeurs manquantes dans l'ensemble de données, cela peut causer des erreurs et de mauvaises performances avec certains algorithmes de machine learning.  
  
Voici la liste des valeurs manquantes courantes que vous pouvez trouver dans votre ensemble de données.

* N/A
* null
* Vide
* ?
* none
* vide
* -
* NaN

Apprenons différentes méthodes pour résoudre le problème des données manquantes.

### Suppression de variable

La suppression de variable consiste à supprimer des variables (colonnes) avec des valeurs manquantes au cas par cas. Cette méthode est judicieuse lorsqu'il y a beaucoup de valeurs manquantes dans une variable et si la variable est de relativement moindre importance.

Le seul cas où il peut valoir la peine de supprimer une variable est lorsque ses valeurs manquantes représentent plus de **60%** des observations.

```python
# import des packages
import numpy as np 
import pandas as pd 

# lecture de l'ensemble de données 
data = pd.read_csv('path/to/data')

# définir le seuil
threshold = 0.7

# suppression des colonnes avec un taux de valeurs manquantes supérieur au seuil
data = data[data.columns[data.isnull().mean() < threshold]]

```

Dans l'extrait de code ci-dessus, vous pouvez voir comment j'utilise NumPy et pandas pour charger l'ensemble de données et définir un seuil à **0,7**. Cela signifie que toute colonne ayant des valeurs manquantes représentant plus de **70%** des observations sera supprimée de l'ensemble de données.

Je vous recommande de définir votre valeur de seuil en fonction de la taille de votre ensemble de données.

### Imputation par la moyenne ou la médiane

Une autre technique courante consiste à utiliser la moyenne ou la médiane des observations non manquantes. Cette stratégie peut être appliquée à une caractéristique ayant des données numériques.

```python
# remplissage des valeurs manquantes avec les médianes des colonnes
data = data.fillna(data.median())
```

Dans l'exemple ci-dessus, nous utilisons la **méthode de la médiane** pour remplir les valeurs manquantes dans l'ensemble de données.

### Valeur la plus courante

Cette méthode consiste à remplacer les valeurs manquantes par la **valeur la plus fréquente** dans une colonne/caractéristique. C'est une bonne option pour gérer les colonnes/caractéristiques **catégorielles**.

```python
# remplissage des valeurs manquantes avec les médianes des colonnes
data['column_name'].fillna(data['column_name'].value_counts().idxmax(), inplace=True)
```

Ici, nous utilisons la **méthode value_counts()** de pandas pour compter l'occurrence de chaque valeur unique dans la colonne, puis nous remplissons la valeur manquante avec la valeur la plus courante.

## Comment gérer les caractéristiques continues

Les caractéristiques continues dans l'ensemble de données ont une plage de valeurs différente. Des exemples courants de caractéristiques continues sont l'âge, le salaire, les prix et les tailles.

Il est très important de gérer les caractéristiques continues dans votre ensemble de données avant d'entraîner des algorithmes de machine learning. Si vous entraînez votre modèle avec une plage de valeurs différente, le modèle ne performera pas bien.

Que veux-je dire lorsque je parle d'une plage de valeurs différente ? Supposons que vous avez un ensemble de données avec deux caractéristiques continues, **âge** et **salaire**. La plage d'âge sera différente de la plage de salaire, et cela peut causer des problèmes.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/new-op212.jpg)

Voici quelques méthodes courantes pour gérer les caractéristiques continues :

### Normalisation Min-Max

Pour chaque valeur dans une caractéristique, la normalisation Min-Max soustrait la valeur minimale dans la caractéristique puis divise par sa plage. La plage est la différence entre le maximum original et le minimum original.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Picture2.png)

Enfin, elle met à l'échelle toutes les valeurs dans une plage fixe entre **0** et **1**.

Vous pouvez utiliser la méthode **[MinMaxScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html)** de Scikit-learn qui transforme les caractéristiques en mettant à l'échelle chaque caractéristique dans une plage donnée :

```python
from sklearn.preprocessing import MinMaxScaler
import numpy as np

# 4 échantillons/observations et 2 variables/caractéristiques
data = np.array([[4, 6], [11, 34], [10, 17], [1, 5]])

# créer la méthode de mise à l'échelle
scaler = MinMaxScaler(feature_range=(0,1))

# ajuster et transformer les données
scaled_data = scaler.fit_transform(data)

print(scaled_data)

# [[0.3        0.03448276]
#  [1.         1.        ] 
#  [0.9        0.4137931 ] 
#  [0.         0.        ]]
```

Comme vous pouvez le voir, nos données ont été transformées et la plage est entre **0** et **1**.

### Standardisation

La standardisation garantit que chaque caractéristique a une moyenne de **0** et un écart-type de **1**, ramenant toutes les caractéristiques à la même magnitude.

Si l'écart-type des caractéristiques est **différent**, leur plage différera également.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-24.png)
_x = observation, μ = moyenne, σ = écart-type_

Vous pouvez utiliser la méthode **[StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler)** de Scikit-learn pour standardiser les caractéristiques en supprimant la moyenne et en mettant à l'échelle avec un écart-type de **1** :

```python
from sklearn.preprocessing import StandardScaler
import numpy as np

# 4 échantillons/observations et 2 variables/caractéristiques
data = np.array([[4, 1], [11, 1], [10, 4], [1, 11]])

# créer la méthode de mise à l'échelle 
scaler = StandardScaler()

# ajuster et transformer les données
scaled_data = scaler.fit_transform(data)

print(scaled_data)

# [[-0.60192927 -0.79558708]
#  [ 1.08347268 -0.79558708] 
#  [ 0.84270097 -0.06119901] 
#  [-1.32424438  1.65237317]]
```

Vérifions que la moyenne de chaque caractéristique (colonne) est **0** :

```python
print(scaled_data.mean(axis=0))
```

`[0. 0.]`

Et que l'écart-type de chaque caractéristique (colonne) est **1** :

```python
print(scaled_data.std(axis=0))
```

`[1. 1.]`

## Comment gérer les caractéristiques catégorielles

Les caractéristiques catégorielles représentent des types de données qui peuvent être divisés en groupes. Par exemple, les genres et les niveaux d'éducation.

Toute valeur non numérique doit être _convertie_ en entiers ou en flottants pour être utilisée dans la plupart des bibliothèques de machine learning.

Les méthodes courantes pour gérer les caractéristiques catégorielles sont :

### Encodage par étiquette

L'encodage par étiquette consiste simplement à convertir chaque valeur catégorielle dans une colonne en un nombre.

Il est recommandé d'utiliser l'encodage par étiquette pour les convertir en variables binaires.

Dans l'exemple suivant, vous apprendrez à utiliser **[LabelEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html)** de Scikit-learn pour transformer les valeurs catégorielles en binaires :

```python
# import des packages
import numpy as np 
import pandas as pd 
from sklearn.preprocessing import LabelEncoder

# initialisation des données de listes.
data = {'Genre':['homme', 'femme', 'femme', 'homme','homme'],
        'Pays':['Tanzanie','Kenya', 'Tanzanie', 'Tanzanie','Kenya']}
  
# Création du DataFrame
data = pd.DataFrame(data)


# création de l'objet label encoder
le = LabelEncoder()
  
data['Genre']= le.fit_transform(data['Genre'])
data['Pays']= le.fit_transform(data['Pays'])

print(data) 
```

![Image](https://www.freecodecamp.org/news/content/images/2021/04/hhhjkk-1.PNG)
_Données transformées_

### Encodage one-hot

De loin, la méthode la plus courante pour représenter les variables catégorielles est l'encodage one-hot, ou les méthodes d'encodage one-out-of-N, également connues sous le nom de variables muettes.

L'idée derrière les variables muettes est de remplacer une variable catégorielle par une ou plusieurs nouvelles caractéristiques qui peuvent avoir les valeurs 0 et 1.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-25.png)

Dans l'exemple suivant, nous utiliserons des encodeurs de la bibliothèque Scikit-learn. **[LabelEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html)** nous aidera à créer un encodage entier des étiquettes à partir de nos données et **[OneHotEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html)** créera un encodage one-hot des valeurs encodées en entiers.

```python
# import des packages 
import numpy as np 
from sklearn.preprocessing import OneHotEncoder, LabelEncoder


# définition de l'exemple
data = np.array(['froid', 'froid', 'chaud', 'froid', 'chaud', 'chaud', 'chaud', 'froid', 'chaud', 'chaud'])

# encodage entier
label_encoder = LabelEncoder()

# ajuster et transformer les données
integer_encoded = label_encoder.fit_transform(data)
print(integer_encoded)

# encodage one-hot
onehot_encoder = OneHotEncoder(sparse=False)

# remodeler les données
integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)

# ajuster et transformer les données
onehot_encoded = onehot_encoder.fit_transform(integer_encoded)

print(onehot_encoded)
```

Voici la sortie de **integer_encoded** par la méthode **LabelEncoder** :

`[0 0 2 0 1 1 2 0 2 1]`

Et voici la sortie de **onehot_encoded** par la méthode **OneHotEncoder** :

```
[[1. 0. 0.] 
 [1. 0. 0.] 
 [0. 0. 1.] 
 [1. 0. 0.] 
 [0. 1. 0.] 
 [0. 1. 0.] 
 [0. 0. 1.] 
 [1. 0. 0.] 
 [0. 0. 1.] 
 [0. 1. 0.]]
```

# Qu'est-ce que la sélection des caractéristiques ?

La sélection des caractéristiques est le processus où vous sélectionnez automatiquement ou manuellement les caractéristiques qui contribuent le plus à votre variable de prédiction ou à votre sortie.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/1_XHHToil9E5EFeEh0H0rnjA.jpeg)

Avoir des caractéristiques non pertinentes dans vos données peut _diminuer_ la précision des modèles de machine learning.

Les principales raisons d'utiliser la sélection des caractéristiques sont :

* Elle permet à l'algorithme de machine learning de s'entraîner plus rapidement.
* Elle réduit la complexité d'un modèle et le rend plus facile à interpréter.
* Elle améliore la précision d'un modèle si le bon sous-ensemble est choisi.
* Elle réduit le surapprentissage.

> "J'ai préparé un modèle en sélectionnant toutes les caractéristiques et j'ai obtenu une précision d'environ **65%**, ce qui n'est pas très bon pour un modèle prédictif, et après avoir fait une sélection de caractéristiques et une ingénierie de caractéristiques sans faire de changements logiques dans le code de mon modèle, ma précision a bondi à **81%**, ce qui est assez impressionnant" - Par Raheel Shaikh

Les méthodes courantes pour la sélection des caractéristiques sont :

### Sélection univariée

Les tests statistiques peuvent aider à sélectionner des caractéristiques indépendantes qui ont la relation la plus forte avec la caractéristique cible dans votre ensemble de données. Par exemple, le test du chi-carré.

La bibliothèque Scikit-learn fournit la classe **[SelectKBest](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectKBest.html)** qui peut être utilisée avec une suite de différents tests statistiques pour sélectionner un nombre spécifique de caractéristiques.

Dans l'exemple suivant, nous utilisons la classe **SelectKBest** avec le test du chi-carré pour trouver la meilleure caractéristique pour l'ensemble de données Iris :

```python
# Charger les packages
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
  
# Charger les données iris
iris_dataset = load_iris()
  
# Créer les caractéristiques et la cible
X = iris_dataset.data
y = iris_dataset.target
  
# Convertir en données catégorielles en convertissant les données en entiers
X = X.astype(int)
  
# Deux caractéristiques avec les statistiques de chi-carré les plus élevées sont sélectionnées
chi2_features = SelectKBest(chi2, k = 2)
X_kbest_features = chi2_features.fit_transform(X, y)
  
# Caractéristiques réduites
print('Nombre de caractéristiques originales :', X.shape[1])
print('Nombre de caractéristiques réduites :', X_kbest_features.shape[1])
```

Nombre de caractéristiques originales : 4   
Nombre de caractéristiques réduites : 2

Comme vous pouvez le voir, le test du chi-carré nous aide à sélectionner **deux caractéristiques indépendantes importantes** parmi les 4 originales qui ont la relation la plus forte avec la caractéristique cible.

Vous pouvez en apprendre plus sur le test du chi-carré ici : "[A Gentle Introduction to the Chi-Squared Test for Machine Learning](https://machinelearningmastery.com/chi-squared-test-for-machine-learning/)".

### Importance des caractéristiques

L'importance des caractéristiques vous donne un score pour chaque caractéristique de vos données. Plus le score est élevé, plus cette caractéristique est **importante** ou **pertinente** pour votre caractéristique cible.

L'importance des caractéristiques est une classe intégrée qui vient avec les classificateurs basés sur les arbres tels que :

* Classificateurs de forêt aléatoire
* Classificateurs d'arbres extra

Dans l'exemple suivant, nous allons entraîner le classificateur d'arbres extra sur l'ensemble de données iris et utiliser la classe intégrée **.feature_importances_** pour calculer l'importance de chaque caractéristique :

```python
# Charger les bibliothèques
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from sklearn.ensemble import ExtraTreesClassifier

# Charger les données iris
iris_dataset = load_iris()
  
# Créer les caractéristiques et la cible
X = iris_dataset.data
y = iris_dataset.target
  
# Convertir en données catégorielles en convertissant les données en entiers
X = X.astype(int)
 
 # Construire le modèle
extra_tree_forest = ExtraTreesClassifier(n_estimators = 5,
                                        criterion ='entropy', max_features = 2)
  
# Entraîner le modèle
extra_tree_forest.fit(X, y)
  
# Calculer l'importance de chaque caractéristique
feature_importance = extra_tree_forest.feature_importances_
  
# Normaliser les importances individuelles
feature_importance_normalized = np.std([tree.feature_importances_ for tree in 
                                        extra_tree_forest.estimators_],
                                        axis = 0)

# Tracer un graphique à barres pour comparer les modèles
plt.bar(iris_dataset.feature_names, feature_importance_normalized)
plt.xlabel('Étiquettes des caractéristiques')
plt.ylabel('Importance des caractéristiques')
plt.title('Comparaison des différentes importances des caractéristiques')
plt.show()

```

![Image](https://www.freecodecamp.org/news/content/images/2021/04/feature-important.PNG)
_Caractéristiques importantes_

Le graphique ci-dessus montre que les caractéristiques les plus importantes sont **_longueur des pétales (cm)_** et **_largeur des pétales (cm)_**, et que la caractéristique la moins importante est **_largeur des sépales (cm)_**. Cela signifie que vous pouvez utiliser les caractéristiques les plus importantes pour entraîner votre modèle et obtenir les meilleures performances.

### Carte thermique de la matrice de corrélation

La corrélation montre comment les caractéristiques sont liées les unes aux autres ou à la caractéristique cible.

La corrélation peut être positive (une augmentation d'une valeur de la caractéristique augmente la valeur de la variable cible) ou négative (une augmentation d'une valeur de la caractéristique diminue la valeur de la variable cible).

Dans l'exemple suivant, nous utiliserons l'ensemble de données des prix des maisons de Boston de la bibliothèque Scikit-learn et la méthode **[corr()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.corr.html)** de pandas pour trouver la corrélation par paires de toutes les caractéristiques dans le dataframe :

```python
# Charger les bibliothèques
from sklearn.datasets import load_boston
import matplotlib.pyplot as plt
import seaborn as sns


# charger les données boston
boston_dataset = load_boston()

# créer un dataframe pour les données boston
boston = pd.DataFrame(boston_dataset.data, columns=boston_dataset.feature_names)
  
# Convertir en données catégorielles en convertissant les données en entiers
#X = X.astype(int)
 
# tracer la carte thermique pour la corrélation
ax = sns.heatmap(boston.corr().round(2), annot=True) 

```

![Image](https://www.freecodecamp.org/news/content/images/2021/04/1_Fbfj8xjr-PwQnfjQ4CBY_g.png)

Le coefficient de corrélation varie de -1 à 1. Si la valeur est proche de 1, cela signifie qu'il y a une forte corrélation positive entre les deux caractéristiques. Lorsqu'elle est proche de -1, les caractéristiques ont une forte corrélation négative.  
  
Sur la figure ci-dessus, vous pouvez voir que les caractéristiques **TAX** et **RAD** ont une _forte corrélation positive_ et que les caractéristiques **DIS** et **NOX** ont une _forte corrélation négative_.

Si vous découvrez qu'il y a certaines caractéristiques dans votre ensemble de données qui sont corrélées les unes aux autres, cela signifie qu'elles transmettent la même information. Il est recommandé de supprimer l'une d'entre elles.

Vous pouvez lire plus à ce sujet ici : [In supervised learning, why is it bad to have correlated features?](https://datascience.stackexchange.com/questions/24452/in-supervised-learning-why-is-it-bad-to-have-correlated-features)

## Conclusion 

Les méthodes que j'ai expliquées dans cet article vous aideront à préparer la plupart des **ensembles de données structurés** que vous avez. Mais si vous travaillez sur des ensembles de données non structurés tels que des images, du texte et de l'audio, vous devrez apprendre différentes méthodes qui ne sont pas expliquées dans cet article.

Les articles suivants vous aideront à apprendre comment préparer des ensembles de données d'images ou de texte pour vos projets de machine learning :

* [Best Practices for Preparing and Augmenting Image Data for CNNs-Jason Brownlee](https://machinelearningmastery.com/best-practices-for-preparing-and-augmenting-image-data-for-convolutional-neural-networks/)
* [Image Pre-processing- Prince Canuma](https://towardsdatascience.com/image-pre-processing-c1aec0be3edf)
* [NLP Text Preprocessing: A Practical Guide and Template- Jiahao Weng](https://towardsdatascience.com/nlp-text-preprocessing-a-practical-guide-and-template-d80874676e79)
* [How to Use Texthero to Prep a Text-based Dataset for Your NLP Project-Davis David](https://www.freecodecamp.org/news/how-to-work-and-understand-text-based-dataset-with-texthero/)

**Félicitations** 👏👏**,** vous êtes arrivé à la fin de cet article ! J'espère que vous avez appris quelque chose de nouveau qui vous aidera dans votre prochain projet de machine learning ou de data science.

Si vous avez appris quelque chose de nouveau ou apprécié la lecture de cet article, veuillez le partager afin que d'autres puissent le voir. En attendant, à la prochaine !

Vous pouvez également me trouver sur Twitter [@Davis_McDavid](https://twitter.com/Davis_McDavid).

Et vous pouvez lire plus d'articles comme celui-ci [ici](https://www.freecodecamp.org/news/author/davis/).