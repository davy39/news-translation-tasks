---
title: 8 algorithmes de clustering en machine learning que tous les data scientists
  devraient connaître
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-09-21T16:38:33.000Z'
originalURL: https://freecodecamp.org/news/8-clustering-algorithms-in-machine-learning-that-all-data-scientists-should-know
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/analysis.png
tags:
- name: algorithms
  slug: algorithms
- name: clustering
  slug: clustering
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
seo_title: 8 algorithmes de clustering en machine learning que tous les data scientists
  devraient connaître
seo_desc: "By Milecia McGregor\nThere are three different approaches to machine learning,\
  \ depending on the data you have. You can go with supervised learning, semi-supervised\
  \ learning, or unsupervised learning. \nIn supervised learning you have labeled\
  \ data, so y..."
---

Par Milecia McGregor

Il existe trois approches différentes pour le machine learning, selon les données que vous possédez. Vous pouvez opter pour l'apprentissage supervisé, l'apprentissage semi-supervisé ou l'apprentissage non supervisé. 

Dans l'apprentissage supervisé, vous disposez de données étiquetées, donc vous avez des sorties que vous savez être les valeurs correctes pour vos entrées. C'est comme connaître les prix des voitures en fonction des caractéristiques telles que la marque, le modèle, le style, la transmission et d'autres attributs.

Avec l'apprentissage semi-supervisé, vous avez un grand ensemble de données où certaines données sont étiquetées mais la plupart ne le sont pas. 

Cela couvre une grande quantité de données du monde réel car il peut être coûteux de faire appel à un expert pour étiqueter chaque point de données. Vous pouvez contourner ce problème en utilisant une combinaison d'apprentissage supervisé et non supervisé.

L'apprentissage non supervisé signifie que vous avez un ensemble de données complètement non étiqueté. Vous ne savez pas s'il y a des motifs cachés dans les données, donc vous laissez l'algorithme trouver ce qu'il peut. 

C'est là que les algorithmes de clustering interviennent. C'est l'une des méthodes que vous pouvez utiliser dans un problème d'apprentissage non supervisé.

## Qu'est-ce que les algorithmes de clustering ?

Le clustering est une tâche d'apprentissage automatique non supervisé. Vous pouvez également entendre cela appelé analyse de clusters en raison de la manière dont cette méthode fonctionne. 

Utiliser un algorithme de clustering signifie que vous allez donner à l'algorithme beaucoup de données d'entrée sans étiquettes et le laisser trouver tout regroupement dans les données qu'il peut.

Ces regroupements sont appelés _clusters_. Un cluster est un groupe de points de données qui sont similaires les uns aux autres en fonction de leur relation avec les points de données environnants. Le clustering est utilisé pour des choses comme l'ingénierie des caractéristiques ou la découverte de motifs. 

Lorsque vous commencez avec des données que vous ne connaissez pas, le clustering peut être un bon point de départ pour obtenir des informations. 

## Types d'algorithmes de clustering

Il existe différents types d'algorithmes de clustering qui gèrent tous types de données uniques.

### Basé sur la densité

Dans le clustering basé sur la densité, les données sont regroupées par zones de fortes concentrations de points de données entourées de zones de faibles concentrations de points de données. Basiquement, l'algorithme trouve les endroits qui sont denses en points de données et appelle ceux-ci des clusters.

Le grand avantage de cela est que les clusters peuvent avoir n'importe quelle forme. Vous n'êtes pas limité à des conditions attendues. 

Les algorithmes de clustering de ce type n'essayent pas d'assigner les valeurs aberrantes aux clusters, donc elles sont ignorées.

### Basé sur la distribution

Avec une approche de clustering basée sur la distribution, tous les points de données sont considérés comme faisant partie d'un cluster en fonction de la probabilité qu'ils appartiennent à un cluster donné. 

Cela fonctionne comme suit : il y a un point central, et à mesure que la distance d'un point de données par rapport au centre augmente, la probabilité qu'il fasse partie de ce cluster diminue. 

Si vous n'êtes pas sûr de la distribution dans vos données, vous devriez considérer un autre type d'algorithme.

### Basé sur les centroïdes

Le clustering basé sur les centroïdes est celui dont vous entendez probablement le plus parler. Il est un peu sensible aux paramètres initiaux que vous lui donnez, mais il est rapide et efficace. 

Ces types d'algorithmes séparent les points de données en fonction de plusieurs centroïdes dans les données. Chaque point de données est assigné à un cluster en fonction de sa distance au carré par rapport au centroïde. C'est le type de clustering le plus couramment utilisé.

### Basé sur la hiérarchie

Le clustering basé sur la hiérarchie est généralement utilisé sur des données hiérarchiques, comme celles que vous obtiendriez à partir d'une base de données d'entreprise ou de taxonomies. Il construit un arbre de clusters afin que tout soit organisé de haut en bas. 

Cela est plus restrictif que les autres types de clustering, mais c'est parfait pour des types spécifiques d'ensembles de données.

## Quand utiliser le clustering

Lorsque vous avez un ensemble de données non étiquetées, il est très probable que vous utilisiez une sorte d'algorithme d'apprentissage non supervisé. 

Il existe de nombreuses techniques différentes d'apprentissage non supervisé, comme les réseaux de neurones, l'apprentissage par renforcement et le clustering. Le type spécifique d'algorithme que vous souhaitez utiliser dépendra de l'apparence de vos données.

Vous pourriez vouloir utiliser le clustering lorsque vous essayez de faire de la détection d'anomalies pour essayer de trouver des valeurs aberrantes dans vos données. Il aide en trouvant ces groupes de clusters et en montrant les limites qui détermineraient si un point de données est une valeur aberrante ou non. 

Si vous n'êtes pas sûr des caractéristiques à utiliser pour votre modèle de machine learning, le clustering découvre des motifs que vous pouvez utiliser pour déterminer ce qui se distingue dans les données.

Le clustering est particulièrement utile pour explorer des données que vous ne connaissez pas. Il peut prendre un certain temps pour déterminer quel type d'algorithme de clustering fonctionne le mieux, mais lorsque vous le trouvez, vous obtiendrez des informations inestimables sur vos données. Vous pourriez trouver des connexions auxquelles vous n'auriez jamais pensé.

Certaines applications réelles du clustering incluent la détection de fraudes dans l'assurance, la catégorisation de livres dans une bibliothèque et la segmentation client en marketing. Il peut également être utilisé dans des problèmes plus vastes, comme l'analyse des tremblements de terre ou la planification urbaine.

## Les 8 meilleurs algorithmes de clustering

Maintenant que vous avez quelques connaissances sur le fonctionnement des algorithmes de clustering et les différents types disponibles, nous pouvons parler des algorithmes réels que vous verrez couramment en pratique. 

Nous allons implémenter ces algorithmes sur un exemple de jeu de données de la bibliothèque [sklearn](https://scikit-learn.org/stable/) en Python.

Nous allons utiliser le jeu de données _make_classification_ de la bibliothèque sklearn pour démontrer comment différents algorithmes de clustering ne sont pas adaptés à tous les problèmes de clustering. 

Vous pouvez trouver [le code pour tous les exemples suivants ici](https://github.com/flippedcoder/probable-waddle).

### Algorithme de clustering K-means

Le clustering K-means est l'algorithme de clustering le plus couramment utilisé. C'est un algorithme basé sur les centroïdes et le plus simple algorithme d'apprentissage non supervisé. 

Cet algorithme essaie de minimiser la variance des points de données au sein d'un cluster. C'est aussi ainsi que la plupart des gens sont initiés à l'apprentissage non supervisé en machine learning.

K-means est mieux utilisé sur des ensembles de données plus petits car il itère sur _tous_ les points de données. Cela signifie qu'il prendra plus de temps pour classer les points de données s'il y en a un grand nombre dans l'ensemble de données. 

Puisque c'est ainsi que k-means regroupe les points de données, il ne se met pas à l'échelle efficacement.

**Implémentation :**

```python
from numpy import unique
from numpy import where
from matplotlib import pyplot
from sklearn.datasets import make_classification
from sklearn.cluster import KMeans

# initialiser le jeu de données avec lequel nous allons travailler
training_data, _ = make_classification(
    n_samples=1000,
    n_features=2,
    n_informative=2,
    n_redundant=0,
    n_clusters_per_class=1,
    random_state=4
)

# définir le modèle
kmeans_model = KMeans(n_clusters=2)

# assigner chaque point de données à un cluster
dbscan_result = dbscan_model.fit_predict(training_data)

# obtenir tous les clusters uniques
dbscan_clusters = unique(dbscan_result)

# tracer les clusters DBSCAN
for dbscan_cluster in dbscan_clusters:
    # obtenir les points de données qui tombent dans ce cluster
    index = where(dbscan_result == dbscan_clusters)
    # faire le tracé
    pyplot.scatter(training_data[index, 0], training_data[index, 1])

# montrer le tracé DBSCAN
pyplot.show()
```

### Algorithme de clustering DBSCAN

DBSCAN signifie clustering spatial basé sur la densité des applications avec bruit. C'est un algorithme de clustering basé sur la densité, contrairement à k-means. 

C'est un bon algorithme pour trouver les valeurs aberrantes dans un ensemble de données. Il trouve des clusters de forme arbitraire en fonction de la densité des points de données dans différentes régions. Il sépare les régions par des zones de faible densité afin de pouvoir détecter les valeurs aberrantes entre les clusters de haute densité.

Cet algorithme est meilleur que k-means lorsqu'il s'agit de travailler avec des données de forme étrange. 

DBSCAN utilise deux paramètres pour déterminer comment les clusters sont définis : _minPts_ (le nombre minimum de points de données qui doivent être regroupés pour qu'une zone soit considérée comme de haute densité) et _eps_ (la distance utilisée pour déterminer si un point de données se trouve dans la même zone que d'autres points de données). 

Choisir les bons paramètres initiaux est crucial pour que cet algorithme fonctionne.

**Implémentation :**

```python
from numpy import unique
from numpy import where
from matplotlib import pyplot
from sklearn.datasets import make_classification
from sklearn.cluster import DBSCAN

# initialiser le jeu de données avec lequel nous allons travailler
training_data, _ = make_classification(
    n_samples=1000,
    n_features=2,
    n_informative=2,
    n_redundant=0,
    n_clusters_per_class=1,
    random_state=4
)

# définir le modèle
dbscan_model = DBSCAN(eps=0.25, min_samples=9)

# entraîner le modèle
dbscan_model.fit(training_data)

# assigner chaque point de données à un cluster
dbscan_result = dbscan_model.predict(training_data)

# obtenir tous les clusters uniques
dbscan_cluster = unique(dbscan_result)

# tracer les clusters DBSCAN
for dbscan_cluster in dbscan_clusters:
    # obtenir les points de données qui tombent dans ce cluster
    index = where(dbscan_result == dbscan_clusters)
    # faire le tracé
    pyplot.scatter(training_data[index, 0], training_data[index, 1])

# montrer le tracé DBSCAN
pyplot.show()
```

### Algorithme de modèle de mélange gaussien

L'un des problèmes avec k-means est que les données doivent suivre un format circulaire. La manière dont k-means calcule la distance entre les points de données a à voir avec un chemin circulaire, donc les données non circulaires ne sont pas correctement regroupées. 

C'est un problème que les modèles de mélange gaussien résolvent. Vous n'avez pas besoin de données en forme circulaire pour qu'il fonctionne bien.

Le modèle de mélange gaussien utilise plusieurs distributions gaussiennes pour s'adapter à des données de forme arbitraire. 

Il y a plusieurs modèles gaussiens simples qui agissent comme des couches cachées dans ce modèle hybride. Ainsi, le modèle calcule la probabilité qu'un point de données appartienne à une distribution gaussienne spécifique et c'est le cluster sous lequel il tombera.

**Implémentation :**

```python
from numpy import unique
from numpy import where
from matplotlib import pyplot
from sklearn.datasets import make_classification
from sklearn.mixture import GaussianMixture

# initialiser le jeu de données avec lequel nous allons travailler
training_data, _ = make_classification(
    n_samples=1000,
    n_features=2,
    n_informative=2,
    n_redundant=0,
    n_clusters_per_class=1,
    random_state=4
)

# définir le modèle
gaussian_model = GaussianMixture(n_components=2)

# entraîner le modèle
gaussian_model.fit(training_data)

# assigner chaque point de données à un cluster
gaussian_result = gaussian_model.predict(training_data)

# obtenir tous les clusters uniques
gaussian_clusters = unique(gaussian_result)

# tracer les clusters du modèle de mélange gaussien
for gaussian_cluster in gaussian_clusters:
    # obtenir les points de données qui tombent dans ce cluster
    index = where(gaussian_result == gaussian_clusters)
    # faire le tracé
    pyplot.scatter(training_data[index, 0], training_data[index, 1])

# montrer le tracé du modèle de mélange gaussien
pyplot.show()
```

### Algorithme BIRCH

L'algorithme BIRCH (Balanced Iterative Reducing and Clustering using Hierarchies) fonctionne mieux sur de grands ensembles de données que l'algorithme k-means. 

Il divise les données en petits résumés qui sont regroupés au lieu des points de données originaux. Les résumés contiennent autant d'informations de distribution que possible sur les points de données.

Cet algorithme est couramment utilisé avec d'autres algorithmes de clustering car les autres techniques de clustering peuvent être utilisées sur les résumés générés par BIRCH. 

Le principal inconvénient de l'algorithme BIRCH est qu'il ne fonctionne que sur des valeurs de données numériques. Vous ne pouvez pas utiliser cela pour des valeurs catégorielles à moins de faire quelques transformations de données.

**Implémentation :**

```python
from numpy import unique
from numpy import where
from matplotlib import pyplot
from sklearn.datasets import make_classification
from sklearn.cluster import Birch

# initialiser le jeu de données avec lequel nous allons travailler
training_data, _ = make_classification(
    n_samples=1000,
    n_features=2,
    n_informative=2,
    n_redundant=0,
    n_clusters_per_class=1,
    random_state=4
)

# définir le modèle
birch_model = Birch(threshold=0.03, n_clusters=2)

# entraîner le modèle
birch_model.fit(training_data)

# assigner chaque point de données à un cluster
birch_result = birch_model.predict(training_data)

# obtenir tous les clusters uniques
birch_clusters = unique(birch_result)

# tracer les clusters BIRCH
for birch_cluster in birch_clusters:
    # obtenir les points de données qui tombent dans ce cluster
    index = where(birch_result == birch_clusters)
    # faire le tracé
    pyplot.scatter(training_data[index, 0], training_data[index, 1])

# montrer le tracé BIRCH
pyplot.show()

```

### Algorithme de clustering par propagation d'affinité

Cet algorithme de clustering est complètement différent des autres dans la manière dont il regroupe les données. 

Chaque point de données communique avec tous les autres points de données pour leur faire savoir à quel point ils sont similaires et cela commence à révéler les clusters dans les données. Vous n'avez pas à dire à cet algorithme combien de clusters attendre dans les paramètres d'initialisation.

À mesure que des messages sont envoyés entre les points de données, des ensembles de données appelés _exemplars_ sont trouvés et ils représentent les clusters. 

Un exemplar est trouvé après que les points de données ont échangé des messages entre eux et forment un consensus sur le point de données qui représente le mieux un cluster. 

Lorsque vous n'êtes pas sûr du nombre de clusters à attendre, comme dans un problème de vision par ordinateur, c'est un excellent algorithme pour commencer.

**Implémentation :**

```python
from numpy import unique
from numpy import where
from matplotlib import pyplot
from sklearn.datasets import make_classification
from sklearn.cluster import AffinityPropagation

# initialiser le jeu de données avec lequel nous allons travailler
training_data, _ = make_classification(
    n_samples=1000,
    n_features=2,
    n_informative=2,
    n_redundant=0,
    n_clusters_per_class=1,
    random_state=4
)

# définir le modèle
model = AffinityPropagation(damping=0.7)

# entraîner le modèle
model.fit(training_data)

# assigner chaque point de données à un cluster
result = model.predict(training_data)

# obtenir tous les clusters uniques
clusters = unique(result)

# tracer les clusters
for cluster in clusters:
    # obtenir les points de données qui tombent dans ce cluster
    index = where(result == cluster)
    # faire le tracé
    pyplot.scatter(training_data[index, 0], training_data[index, 1])

# montrer le tracé
pyplot.show()
```

### Algorithme de clustering Mean-Shift

C'est un autre algorithme qui est particulièrement utile pour traiter les images et le traitement de la vision par ordinateur. 

Mean-shift est similaire à l'algorithme BIRCH car il trouve également des clusters sans qu'un nombre initial de clusters soit défini. 

C'est un algorithme de clustering hiérarchique, mais l'inconvénient est qu'il ne se met pas à l'échelle efficacement lorsqu'il travaille avec de grands ensembles de données.

Il fonctionne en itérant sur tous les points de données et les déplace vers le mode. Le mode dans ce contexte est la zone de haute densité de points de données dans une région. 

C'est pourquoi vous pourriez entendre cet algorithme appelé l'algorithme de recherche de mode. Il passera par ce processus itératif avec chaque point de données et les déplacera plus près de l'endroit où se trouvent d'autres points de données jusqu'à ce que tous les points de données aient été assignés à un cluster.

**Implémentation :**

```python
from numpy import unique
from numpy import where
from matplotlib import pyplot
from sklearn.datasets import make_classification
from sklearn.cluster import MeanShift

# initialiser le jeu de données avec lequel nous allons travailler
training_data, _ = make_classification(
    n_samples=1000,
    n_features=2,
    n_informative=2,
    n_redundant=0,
    n_clusters_per_class=1,
    random_state=4
)

# définir le modèle
mean_model = MeanShift()

# assigner chaque point de données à un cluster
mean_result = mean_model.fit_predict(training_data)

# obtenir tous les clusters uniques
mean_clusters = unique(mean_result)

# tracer les clusters Mean-Shift
for mean_cluster in mean_clusters:
    # obtenir les points de données qui tombent dans ce cluster
    index = where(mean_result == mean_cluster)
    # faire le tracé
    pyplot.scatter(training_data[index, 0], training_data[index, 1])

# montrer le tracé Mean-Shift
pyplot.show()
```

### Algorithme OPTICS

OPTICS signifie Ordering Points to Identify the Clustering Structure. C'est un algorithme basé sur la densité similaire à DBSCAN, mais il est meilleur car il peut trouver des clusters significatifs dans des données dont la densité varie. Il le fait en ordonnant les points de données de sorte que les points les plus proches soient voisins dans l'ordonnancement.

Cela facilite la détection de différents clusters de densité. L'algorithme OPTICS ne traite chaque point de données qu'une seule fois, similaire à DBSCAN (bien qu'il s'exécute plus lentement que DBSCAN). Il y a également une distance spéciale stockée pour chaque point de données qui indique qu'un point appartient à un cluster spécifique.

**Implémentation :**

```python
from numpy import unique
from numpy import where
from matplotlib import pyplot
from sklearn.datasets import make_classification
from sklearn.cluster import OPTICS

# initialiser le jeu de données avec lequel nous allons travailler
training_data, _ = make_classification(
    n_samples=1000,
    n_features=2,
    n_informative=2,
    n_redundant=0,
    n_clusters_per_class=1,
    random_state=4
)

# définir le modèle
optics_model = OPTICS(eps=0.75, min_samples=10)

# assigner chaque point de données à un cluster
optics_result = optics_model.fit_predict(training_data)

# obtenir tous les clusters uniques
optics_clusters = unique(optics_clusters)

# tracer les clusters OPTICS
for optics_cluster in optics_clusters:
    # obtenir les points de données qui tombent dans ce cluster
    index = where(optics_result == optics_clusters)
    # faire le tracé
    pyplot.scatter(training_data[index, 0], training_data[index, 1])

# montrer le tracé OPTICS
pyplot.show()
```

### Algorithme de clustering hiérarchique agglomératif

C'est le type le plus courant d'algorithme de clustering hiérarchique. Il est utilisé pour regrouper des objets en clusters en fonction de leur similarité. 

C'est une forme de clustering ascendant, où chaque point de données est assigné à son propre cluster. Ensuite, ces clusters sont joints ensemble.

À chaque itération, des clusters similaires sont fusionnés jusqu'à ce que tous les points de données fassent partie d'un grand cluster racine. 

Le clustering agglomératif est le meilleur pour trouver de petits clusters. Le résultat final ressemble à un dendrogramme afin que vous puissiez facilement visualiser les clusters lorsque l'algorithme se termine.

**Implémentation :**

```python
from numpy import unique
from numpy import where
from matplotlib import pyplot
from sklearn.datasets import make_classification
from sklearn.cluster import AgglomerativeClustering

# initialiser le jeu de données avec lequel nous allons travailler
training_data, _ = make_classification(
    n_samples=1000,
    n_features=2,
    n_informative=2,
    n_redundant=0,
    n_clusters_per_class=1,
    random_state=4
)

# définir le modèle
agglomerative_model = AgglomerativeClustering(n_clusters=2)

# assigner chaque point de données à un cluster
agglomerative_result = agglomerative_model.fit_predict(training_data)

# obtenir tous les clusters uniques
agglomerative_clusters = unique(agglomerative_result)

# tracer les clusters
for agglomerative_cluster in agglomerative_clusters:
    # obtenir les points de données qui tombent dans ce cluster
    index = where(agglomerative_result == agglomerative_clusters)
    # faire le tracé
    pyplot.scatter(training_data[index, 0], training_data[index, 1])

# montrer le tracé de la hiérarchie agglomérative
pyplot.show()
```

## Autres types d'algorithmes de clustering

Nous avons couvert huit des meilleurs algorithmes de clustering, mais il en existe bien d'autres. Il existe des algorithmes de clustering très spécifiquement ajustés qui traitent rapidement et précisément vos données. Voici quelques autres qui pourraient vous intéresser.

Il existe un autre algorithme hiérarchique qui est l'opposé de l'approche agglomérative. Il commence par une stratégie de clustering de haut en bas. Il commence donc par un grand cluster racine et en extrait les clusters individuels. 

C'est ce qu'on appelle l'algorithme de clustering **hiérarchique divisif**. Il existe des recherches qui montrent que cela crée des hiérarchies plus précises que le clustering agglomératif, mais c'est beaucoup plus complexe.

**Mini-Batch K-means** est similaire à K-means, sauf qu'il utilise de petits morceaux aléatoires de données de taille fixe afin qu'ils puissent être stockés en mémoire. Cela l'aide à s'exécuter plus rapidement que K-means, donc il converge vers une solution en moins de temps. 

L'inconvénient de cet algorithme est que le gain de vitesse vous coûtera une certaine qualité de cluster.

Le dernier algorithme que nous allons brièvement couvrir est le **clustering spectral**. Cet algorithme est complètement différent des autres que nous avons examinés. 

Il fonctionne en tirant parti de la théorie des graphes. Cet algorithme ne fait aucune supposition initiale sur les clusters qui se trouvent dans l'ensemble de données. Il traite les points de données comme des nœuds dans un graphe et les clusters sont trouvés en fonction des communautés de nœuds qui ont des arêtes de connexion.

## Autres réflexions

Méfiez-vous des problèmes de mise à l'échelle avec les algorithmes de clustering. Votre ensemble de données pourrait contenir des millions de points de données, et comme les algorithmes de clustering fonctionnent en calculant les similarités entre toutes les paires de points de données, vous pourriez vous retrouver avec un algorithme qui ne se met pas à l'échelle efficacement.

## Conclusion

Les algorithmes de clustering sont un excellent moyen d'apprendre de nouvelles choses à partir de anciennes données. Parfois, vous serez surpris par les clusters résultants que vous obtenez et cela pourrait vous aider à comprendre un problème. 

L'une des choses les plus intéressantes concernant l'utilisation du clustering pour l'apprentissage non supervisé est que vous pouvez utiliser les résultats dans un problème d'apprentissage supervisé.

Les clusters pourraient être vos nouvelles caractéristiques que vous utilisez sur un ensemble de données complètement différent ! Vous pouvez utiliser le clustering sur presque n'importe quel problème d'apprentissage non supervisé en machine learning, mais assurez-vous de savoir comment analyser les résultats pour la précision.