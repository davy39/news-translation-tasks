---
title: Les bases de l'apprentissage automatique pour les développeurs
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-24T17:02:27.000Z'
originalURL: https://freecodecamp.org/news/machine-learning-basics-for-developers
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/Machine-Learning-Basics-For-Developers.png
tags:
- name: algorithms
  slug: algorithms
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Data Science
  slug: data-science
- name: Deep Learning
  slug: deep-learning
- name: Machine Learning
  slug: machine-learning
seo_title: Les bases de l'apprentissage automatique pour les développeurs
seo_desc: "By Milecia McGregor\nIn the current tech landscape, developers are expected\
  \ to have a number of different skills. And many of them do. \nThere are also a\
  \ lot of different career paths available to developers that use many of their current\
  \ skills with a..."
---

Par Milecia McGregor

Dans le paysage technologique actuel, les développeurs sont censés avoir un certain nombre de compétences différentes. Et beaucoup d'entre eux en ont. 

Il existe également de nombreux parcours de carrière différents disponibles pour les développeurs qui utilisent beaucoup de leurs compétences actuelles avec une légère variation.

Les administrateurs de bases de données, les défenseurs des développeurs et les ingénieurs en apprentissage automatique ont tous un point commun avec tous les développeurs : ils savent tous comment coder. Peu importe les langages utilisés, ils comprennent tous les concepts de base derrière l'écriture de bon code.

C'est l'une des raisons pour lesquelles de nombreux développeurs logiciels envisagent de devenir ingénieurs en apprentissage automatique. Avec tous les outils et packages disponibles, vous n'avez pas besoin d'avoir un solide bagage mathématique pour obtenir des résultats précis. 

Si vous êtes prêt à apprendre à utiliser certaines bibliothèques et à avoir une compréhension de haut niveau des mathématiques sous-jacentes, vous pouvez devenir ingénieur en apprentissage automatique.

Dans cet article, je vais vous guider à travers certains des principaux concepts de l'apprentissage automatique que vous devez comprendre en venant d'un background de développeur logiciel. 

Nous terminerons par un exemple de projet complet d'apprentissage automatique, de l'obtention des données à la prédiction d'une valeur avec un modèle. À la fin, vous devriez avoir suffisamment de connaissances pour compléter un petit projet d'apprentissage automatique de votre propre chef à partir de zéro.

## Qu'est-ce que l'apprentissage automatique ?

Il existe de nombreuses définitions. Mais l'apprentissage automatique consiste essentiellement à utiliser les mathématiques pour trouver des motifs dans des quantités massives de données afin de faire des prédictions basées sur de nouvelles données. 

Une fois qu'il a trouvé ces motifs, vous pouvez dire que vous avez un modèle d'apprentissage automatique. 

À partir de là, vous pouvez utiliser le modèle pour faire des prédictions sur de nouvelles données que le modèle n'a jamais vues auparavant.

L'objectif est de faire en sorte que les ordinateurs s'améliorent automatiquement avec l'expérience en utilisant les algorithmes qui leur sont fournis. 

Un algorithme n'est qu'une équation mathématique ou un ensemble d'équations qui vous donnent un résultat basé sur vos données d'entrée. L'apprentissage automatique utilise des algorithmes pour trouver ces motifs que nous recherchons.

À mesure que les algorithmes sont exposés à de plus en plus de données, ils commencent à faire des prédictions plus précises. Finalement, le modèle construit par les algorithmes sera capable de déterminer le résultat correct sans être explicitement programmé pour le faire. 

Cela signifie que l'ordinateur devrait être capable de prendre des données et de prendre des décisions (prédictions) sans aucune aide humaine.

## Apprentissage automatique vs. science des données vs. intelligence artificielle

Beaucoup de gens utilisent les termes apprentissage automatique, science des données et intelligence artificielle de manière interchangeable. Mais ils ne sont pas les mêmes choses.

**L'apprentissage automatique** est _utilisé_ en science des données pour faire des prédictions et découvrir des motifs dans vos données. 

**La science des données** se concentre davantage sur les statistiques et les algorithmes et l'interprétation des résultats. L'apprentissage automatique est davantage axé sur le logiciel et l'automatisation des choses.

**L'intelligence artificielle** fait référence à la capacité d'un ordinateur à comprendre et à apprendre à partir de données, tout en prenant des décisions basées sur des motifs cachés qui seraient presque impossibles à découvrir pour les humains. 

L'apprentissage automatique est comme une branche de l'intelligence artificielle. Nous utiliserons l'apprentissage automatique pour _atteindre_ l'intelligence artificielle. 

L'intelligence artificielle est un sujet vaste, et elle couvre des domaines comme la vision par ordinateur, les interactions homme-machine et l'autonomie où l'apprentissage automatique serait utilisé dans chacune de ces applications.

## Différents types d'apprentissage automatique

Il existe trois types d'apprentissage automatique dont vous entendrez et lirez parler : l'apprentissage supervisé, l'apprentissage semi-supervisé et l'apprentissage non supervisé.

### Apprentissage supervisé

C'est la catégorie sous laquelle tombent la plupart des problèmes d'apprentissage automatique. C'est lorsque vous avez des variables d'entrée et de sortie et que vous essayez de faire une correspondance entre elles. 

Il est appelé apprentissage supervisé parce que nous pouvons utiliser les données pour enseigner au modèle la bonne réponse.

L'algorithme fera des prédictions basées sur les données et il sera lentement corrigé jusqu'à ce que ces prédictions correspondent à la sortie attendue. 

La plupart des problèmes couverts par l'apprentissage supervisé peuvent être résolus avec la classification ou la régression. Tant que vous avez des données étiquetées, vous travaillez avec l'apprentissage automatique supervisé.

### Apprentissage semi-supervisé

La plupart des problèmes du monde réel tombent dans cette catégorie à cause de nos ensembles de données. 

Dans de nombreux cas, vous aurez un grand ensemble de données où certaines des données sont étiquetées, mais la plupart ne le sont pas. Parfois, il peut être trop coûteux de faire appel à un expert pour passer en revue et étiqueter toutes ces données, donc vous utilisez un mélange d'apprentissage supervisé et non supervisé.

Une stratégie consiste à utiliser les données étiquetées pour faire des suppositions sur les données non étiquetées, puis à utiliser ces prédictions comme leurs étiquettes. Ensuite, vous pouvez utiliser toutes les données dans un modèle d'apprentissage supervisé.

Puisqu'il est possible de faire de l'apprentissage non supervisé sur ces ensembles de données également, envisagez si cela serait une méthode plus efficace.

### Apprentissage non supervisé

Lorsque vous n'avez que des données d'entrée et aucune donnée de sortie associée et que vous voulez qu'un modèle trouve le motif que vous recherchez, c'est là que vous entrez dans l'apprentissage non supervisé. 

Votre algorithme va inventer quelque chose qui a du sens pour lui en fonction des paramètres que vous lui donnez.

Cela est utile lorsque vous avez beaucoup de données apparemment aléatoires et que vous voulez voir s'il y a des motifs intéressants. Ces problèmes sont généralement idéaux pour les algorithmes de clustering et vous donnent des résultats inattendus.

## Utilisations pratiques de l'apprentissage automatique pour les développeurs

### Classification

Lorsque vous voulez prédire une étiquette pour certaines données d'entrée, il s'agit d'un problème de classification. 

L'apprentissage automatique gère la classification en construisant un modèle qui prend des données déjà étiquetées et les utilise pour faire des prédictions sur de nouvelles données. En gros, vous lui donnez une nouvelle entrée et il vous donne l'étiquette qu'il pense être correcte.

La prédiction de l'attrition des clients, la classification des visages et les tests de diagnostic médical utilisent tous différents types de classification. 

Bien que tous ceux-ci relèvent de différents domaines de classification, ils attribuent tous des valeurs en fonction des données que leurs modèles ont utilisées pour l'entraînement. Toutes les valeurs prédites sont exactes. Vous prédirez donc des valeurs comme un nom ou un booléen.

### Régression

La régression est intéressante car elle chevauche l'apprentissage automatique et les statistiques. Elle est similaire à la classification car elle est utilisée pour prédire des valeurs, sauf qu'elle prédit des valeurs continues au lieu de valeurs discrètes. 

Ainsi, si vous voulez prédire une fourchette de salaire basée sur les années d'expérience et les langues connues, ou si vous voulez prédire un prix de maison basé sur l'emplacement et la superficie, vous traiterez un problème de régression.

Il existe différentes techniques de régression pour gérer tous types d'ensembles de données, même les données non linéaires. 

Il existe la [régression à vecteurs de support](https://www.freecodecamp.org/news/svm-machine-learning-tutorial-what-is-the-support-vector-machine-algorithm-explained-with-code-examples/), la régression linéaire simple et la régression polynomiale, parmi beaucoup d'autres. Il existe suffisamment de techniques de régression pour s'adapter à presque n'importe quel ensemble de données que vous avez.

### Clustering

Cela entre dans un autre type d'apprentissage automatique. Le clustering gère les tâches d'apprentissage non supervisé. C'est comme la classification, mais aucune des données n'est étiquetée. C'est à l'algorithme de trouver et d'étiqueter les points de données. 

Cela est idéal lorsque vous avez un ensemble de données massif et que vous ne connaissez aucun motif entre eux, ou que vous recherchez des connexions inhabituelles.

Le clustering aide lorsque vous voulez trouver des anomalies et des valeurs aberrantes dans vos données sans passer des centaines d'heures à étiqueter manuellement les points de données. 

Dans ce cas, il n'y a souvent pas de meilleur algorithme et la meilleure façon de trouver ce qui fonctionne pour vos données est de tester différents algorithmes. 

Quelques algorithmes de clustering incluent : K-Means, DBSCAN, Clustering Agglomératif et Propagation d'Affinité. Un peu d'essais et d'erreurs vous aidera à trouver rapidement quel algorithme est le plus efficace pour vous.

### Apprentissage profond

C'est un domaine de l'apprentissage automatique qui utilise des algorithmes inspirés du fonctionnement du cerveau. Il implique des réseaux de neurones utilisant de grands ensembles de données non classées. 

Typiquement, les performances s'améliorent avec la quantité de données que vous fournissez à un algorithme d'apprentissage profond. Ces types de problèmes traitent des données non étiquetées, ce qui couvre la majorité des données disponibles.

Il existe un certain nombre d'algorithmes que vous pouvez utiliser avec cette technique, comme les Réseaux de Neurones Convolutifs, les Réseaux de Mémoire à Long et Court Terme, ou le Réseau Q Profond. 

Chacun de ceux-ci est utilisé dans des projets comme la vision par ordinateur, les véhicules autonomes, ou l'analyse des signaux EEG.

## Outils que vous pourriez utiliser

Il existe de nombreux outils disponibles que vous pouvez utiliser pour presque n'importe quel problème d'apprentissage automatique que vous avez. 

Voici une courte liste de certains des packages courants que vous trouverez dans de nombreuses applications d'apprentissage automatique.

[**Pandas**](https://pandas.pydata.org/) : C'est un outil général d'analyse de données en Python. Il aide lorsque vous devez travailler avec des données brutes. Il gère les données textuelles, les données tabulaires, les données de séries temporelles, et plus encore. 

Ce package est utilisé pour formater les données avant l'entraînement d'un modèle d'apprentissage automatique dans de nombreux cas.

[**Tensorflow**](https://www.tensorflow.org/) : Vous pouvez construire n'importe quel nombre d'applications d'apprentissage automatique avec cette bibliothèque. Vous pouvez l'exécuter sur des GPU, l'utiliser pour résoudre des problèmes d'IoT, et elle est idéale pour l'apprentissage profond. 

C'est la bibliothèque qui peut gérer presque tout, mais il faut un certain temps pour se mettre à niveau avec elle.

[**SciKit**](https://scikit-learn.org/stable/) : Cela est similaire à TensorFlow dans la portée des applications d'apprentissage automatique pour lesquelles il peut être utilisé. Une grande différence est la simplicité que vous obtenez avec ce package. 

Si vous êtes familier avec [NumPy](https://numpy.org/), [matplotlib](https://matplotlib.org/), et [SciPy](https://www.scipy.org/), vous n'aurez aucun problème à commencer avec cela. Vous pouvez créer des modèles pour gérer les données des capteurs de véhicules, les données logistiques, les données bancaires, et d'autres contextes.

[**Keras**](https://keras.io/) : Lorsque vous voulez travailler sur un projet d'apprentissage profond, comme un projet complexe de robotique, c'est une bibliothèque spécifique qui vous aidera. 

Elle est construite sur TensorFlow et facilite la création de modèles d'apprentissage profond et leur mise en production. 

Vous verrez cela utilisé beaucoup dans les applications de traitement du langage naturel et les applications de vision par ordinateur.

**NLTK** : Le traitement du langage naturel est un domaine énorme de l'apprentissage automatique et ce package est axé sur lui. 

C'est l'un des packages que vous pouvez utiliser pour rationaliser vos projets de TAL. Il est encore activement développé et il y a une bonne communauté autour.

[**BERT**](https://github.com/google-research/bert) : BERT est une bibliothèque open-source créée en 2018 chez Google. C'est une nouvelle technique pour le TAL et elle adopte une approche complètement différente pour l'entraînement des modèles par rapport à toute autre technique. B

ERT est un acronyme pour Bidirectional Encoder Representations from Transformers. Cela signifie que contrairement à la plupart des techniques qui analysent les phrases de gauche à droite ou de droite à gauche, BERT va dans les deux directions en utilisant l'encodeur Transformer. Son objectif est de générer un modèle de langage.  
  
[**Brain.js**](https://brain.js.org/) : C'est l'une des meilleures bibliothèques JavaScript pour l'apprentissage automatique. Vous pouvez convertir votre modèle en JSON ou l'utiliser directement dans le navigateur comme une fonction et vous avez toujours la flexibilité de gérer la plupart des projets courants d'apprentissage automatique. 

C'est super rapide à démarrer et il a une excellente documentation et des tutoriels.

## Exemple complet d'apprentissage automatique

Pour que vous ayez une idée de ce à quoi un projet d'apprentissage automatique pourrait ressembler, voici un exemple de l'ensemble du processus.

### Obtention des données

Arguablement, la partie la plus difficile d'un projet d'apprentissage automatique est l'obtention des données. Il existe de nombreuses ressources en ligne que vous pouvez utiliser pour obtenir des ensembles de données pour l'apprentissage automatique, et voici une liste de certaines d'entre elles.

* [Ensemble de données de soins intensifs](https://mimic.physionet.org/)
* [Tailles et poids humains](http://wiki.stat.ucla.edu/socr/index.php/SOCR_Data_Dinov_020108_HeightsWeights)
* [Fraude à la carte de crédit](https://www.kaggle.com/mlg-ulb/creditcardfraud)
* [Critiques IMDB](https://www.kaggle.com/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)
* [Sentiment des compagnies aériennes sur Twitter](https://www.kaggle.com/crowdflower/twitter-airline-sentiment)
* [Ensemble de données de chansons](https://www.kaggle.com/c/msdchallenge#description)
* [Ensemble de données sur la qualité du vin](https://archive.ics.uci.edu/ml/datasets/wine+quality)
* [Ensemble de données sur le logement de Boston](https://www.cs.toronto.edu/~delve/data/boston/bostonDetail.html)
* [Chiffres manuscrits MNIST](http://yann.lecun.com/exdb/mnist/)
* [Notations de blagues](http://eigentaste.berkeley.edu/dataset/)
* [Critiques Amazon](https://snap.stanford.edu/data/web-Amazon.html)
* [Collection de spam de messages texte](http://www.dt.fee.unicamp.br/~tiago/smsspamcollection/)
* [E-mails Enron](https://www.cs.cmu.edu/~enron/)
* [Ensembles de données de système de recommandation](https://cseweb.ucsd.edu/~jmcauley/datasets.html)
* [Ensemble de données COVID](https://www.semanticscholar.org/cord19)

Nous utiliserons l'[ensemble de données sur la qualité du vin blanc](https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/) pour cet exemple et nous essaierons de prédire la densité du vin. 

La plupart du temps, les données ne seront pas aussi propres lorsqu'elles vous parviendront et vous devrez travailler avec elles pour les mettre au format souhaité. 

Mais même avec des données comme celles-ci, nous devons encore faire un peu de nettoyage.

### Choix des caractéristiques

Nous allons choisir quelques caractéristiques pour prédire la densité du vin. Les caractéristiques avec lesquelles nous travaillerons sont : _qualité_, _pH_, _alcool_, _acidité fixe_ et _dioxyde de soufre total_. 

Cela aurait pu être n'importe quelle combinaison des caractéristiques disponibles et j'ai choisi celles-ci arbitrairement. N'hésitez pas à utiliser n'importe quelle autre caractéristique au lieu de celles-ci, ou n'hésitez pas à toutes les utiliser !

### Choix des algorithmes

Maintenant que vous connaissez le problème que vous essayez de résoudre et les données avec lesquelles vous devez travailler, vous pouvez commencer à examiner les algorithmes. 

Puisque nous essayons de prédire une valeur continue basée sur plusieurs caractéristiques, il s'agit très probablement d'un problème de régression. Si nous essayions de prédire une valeur discrète, comme le type de vin, alors il s'agirait probablement d'un problème de classification.

C'est pourquoi vous devez connaître vos données avant de vous lancer dans les outils d'apprentissage automatique. 

Cela vous aide à réduire le nombre d'algorithmes que vous pouvez choisir pour votre problème. L'algorithme de régression multivariée est celui par lequel nous allons commencer. Il est couramment utilisé lorsque vous traitez avec plusieurs paramètres qui auront un impact sur le résultat final.

L'algorithme de régression multivariée est comme l'algorithme de régression régulier sauf que vous pouvez avoir plusieurs entrées. L'équation derrière lui est :

`y = theta_0 + sum(theta_n * X_n)`

Nous initialisons à la fois les termes `theta_0` (le terme de biais) et `theta_n` à une certaine valeur, généralement 1 ou 0 sauf si vous avez d'autres informations sur lesquelles baser ces valeurs. 

Après que les valeurs initiales ont été définies, nous essayons de les optimiser pour qu'elles correspondent au problème. Nous le faisons en résolvant les équations de descente de gradient :

```python
# Initialisation des paramètres theta
theta_0 = theta_0 - alpha * (1 / m) * sum(y_n - y_i)

theta_n = theta_n - alpha * (1 / m) * sum(y_n - y_i) * X_n
```

où `y_n` est la valeur prédite basée sur les calculs de l'algorithme et `y_i` est la valeur que nous avons à partir de nos données ou la valeur attendue.

Nous voulons que la marge d'erreur entre la valeur prédite et la valeur réelle soit aussi petite que possible. C'est la raison pour laquelle nous essayons d'optimiser les valeurs theta. Cela permet de minimiser la fonction de coût pour la prédiction des valeurs de sortie. 

Voici l'équation de la fonction de coût :

`J(theta_n) = (1 / 2m) * sum(y_n - y_i)^2`

C'est tout ce dont nous avons besoin en mathématiques pour construire et entraîner le modèle, alors commençons.

### Prétraitement des données

La première chose que vous voulez faire est de vérifier à quoi ressemblent nos données. J'ai apporté quelques modifications à l'ensemble de données sur la qualité du vin afin qu'il fonctionne avec notre algorithme. 

Vous pouvez le télécharger ici : [https://github.com/flippedcoder/probable-waddle/blob/master/wine-quality-data.csv](https://github.com/flippedcoder/probable-waddle/blob/master/wine-quality-data.csv).

Tout ce que j'ai fait est de prendre le fichier original, de supprimer les caractéristiques inutiles, de déplacer la densité à la fin et de nettoyer le format.

Maintenant, nous pouvons passer à la vraie partie de prétraitement ! Créez un nouveau fichier appelé _multivariate-wine.py_. Ce fichier doit être dans le même dossier que l'ensemble de données. 

La première chose que nous ferons dans ce fichier est d'importer quelques packages et de voir à quoi ressemble l'ensemble de données.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('./wine-quality-data.csv', header=None)

print(df.head())
```

Vous devriez voir quelque chose comme ceci dans votre terminal.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/terminal-example.png)

Les données semblent prêtes pour l'algorithme de régression multivariée, donc nous pouvons commencer à construire le modèle. Je vous encourage à essayer de commencer avec l'ensemble de données brut sur le vin blanc pour voir si vous pouvez trouver un moyen de le mettre au format correct.

### Construction du modèle

Nous devons ajouter un terme de biais aux données car, comme vous l'avez vu dans l'explication de l'algorithme, nous en avons besoin car c'est le terme `theta_0`.

`df = pd.concat([pd.Series(1, index=df.index, name='00'), df], axis=1)`

Puisque les données sont prêtes, nous pouvons définir les variables indépendantes et dépendantes pour l'algorithme.

```python
X = df.drop(columns=5)
y = df.iloc[:, 6]
```

Maintenant, normalisons les données en divisant chaque colonne par la valeur maximale de cette colonne. 

Vous n'avez pas vraiment besoin de faire cette étape, mais cela aidera à accélérer le temps d'entraînement pour l'algorithme. Cela aide également à empêcher une caractéristique d'être plus dominante que d'autres.

```python
for i in range(1, len(X.columns)):
	X[i-1] = X[i-1]/np.max(X[i-1])
```

Regardons les données depuis la normalisation.

`print(X.head())`

Vous devriez voir quelque chose de similaire à ceci dans le terminal.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/terminal-output-2.png)

Les données sont prêtes maintenant et nous pouvons initialiser le paramètre theta. Cela signifie simplement que nous allons créer un tableau de uns qui a le même nombre de colonnes que la variable d'entrée, _X_.

`theta = np.array([1]*len(X.columns))`

Cela devrait ressembler à ceci si vous l'imprimez dans votre terminal, bien que vous n'ayez pas besoin de l'imprimer si vous ne le souhaitez pas.

`[1 1 1 1 1 1]`

Ensuite, nous allons définir le nombre de points d'entraînement que nous prendrons à partir des données. Nous laisserons 500 points de données de côté afin de pouvoir les utiliser pour les tests plus tard. Cela va être la valeur pour _m_ à partir de l'équation de descente de gradient que nous avons vue précédemment.

`m = len(df) - 500`

Maintenant, nous pouvons commencer à écrire les fonctions dont nous aurons besoin pour entraîner le modèle après sa construction. Nous commencerons par la fonction d'hypothèse qui est simplement la variable d'entrée multipliée par le paramètre `theta_n`.

```python
def hypothesis(theta, X):
	return theta * X
```

Ensuite, nous définirons le modèle de coût qui nous donnera la marge d'erreur entre les valeurs réelles et prédites.

```python
def calculateCost(X, y, theta):
    y1 = hypothesis(theta, X)
    y1 = np.sum(y1, axis=1)
    
    return (1 / 2 * m) * sum(np.sqrt((y1 - y) ** 2))
```

La dernière fonction dont nous avons besoin avant que notre modèle ne soit prêt à fonctionner est une fonction pour calculer les valeurs de descente de gradient.

```python
def gradientDescent(X, y, theta, alpha, i):
    J = [] # fonction de coût pour chaque itération
    k = 0
    while k < i:
        y1 = hypothesis(theta, X)
        y1 = np.sum(y1, axis=1)
        for c in range(1, len(X.columns)):
            theta[c] = theta[c] - alpha * (1 / m) * (sum((y1 - y) * X.iloc[:, c]))
        j = calculateCost(X, y, theta)
        J.append(j)
        k += 1
    return J, j, theta
```

Avec ces trois fonctions en place et nos données propres, nous pouvons enfin passer à l'entraînement du modèle.

### Entraînement du modèle

La partie entraînement est la partie amusante et aussi la plus facile. Si vous avez correctement configuré votre algorithme, alors tout ce que vous aurez à faire est de prendre les paramètres optimisés qu'il vous donne et de faire des prédictions. 

Nous retournons une liste de coûts à chaque itération, le coût final et les valeurs theta optimisées à partir de la fonction de descente de gradient. Nous obtiendrons donc les valeurs theta optimisées et les utiliserons pour les tests.

`J, j, theta = gradientDescent(X, y, theta, 0.1, 10000)`

Après tout le travail de configuration des fonctions et des données correctement, cette seule ligne de code entraîne le modèle et nous donne les valeurs theta dont nous avons besoin pour commencer à prédire des valeurs et tester la précision du modèle.

### Test du modèle

Maintenant, nous pouvons tester le modèle en faisant une prédiction en utilisant les données.

```python
y_hat = hypothesis(theta, X)
y_hat = np.sum(y_hat, axis=1)
```

Après avoir vérifié quelques valeurs, vous saurez si votre modèle est suffisamment précis ou si vous devez faire plus de réglages sur les valeurs theta. 

Si vous êtes satisfait des résultats de vos tests, vous pouvez commencer à utiliser ce modèle dans vos projets.

### Utilisation du modèle

Les valeurs theta optimisées sont vraiment tout ce dont vous avez besoin pour commencer à utiliser le modèle. Vous continuerez à utiliser les mêmes équations, même en production, mais avec les meilleures valeurs theta pour vous donner les prédictions les plus précises. 

Vous pouvez même continuer à entraîner le modèle et essayer de trouver de meilleures valeurs theta.

## Réflexions finales

L'apprentissage automatique a de nombreuses couches, mais aucune d'entre elles n'est trop complexe. Elles s'empilent simplement, ce qui le rend plus difficile qu'il ne l'est en réalité. 

Si vous êtes prêt à passer du temps à lire sur les bibliothèques et les outils d'apprentissage automatique, il est vraiment facile de commencer. Vous n'avez pas besoin de connaître les mathématiques et les statistiques avancées pour apprendre les concepts ou même pour résoudre des problèmes réels.

Les outils sont plus avancés qu'ils ne l'étaient auparavant, donc vous pouvez être ingénieur en apprentissage automatique sans comprendre la plupart des mathématiques qui se cachent derrière. 

La principale chose que vous devez comprendre est comment gérer vos données. C'est la partie dont personne n'aime parler. Les algorithmes sont amusants et passionnants, mais il peut y avoir des moments où vous devez écrire des procédures SQL pour obtenir les données brutes dont vous avez besoin avant même de commencer à les traiter.

Il existe de nombreuses applications pour l'apprentissage automatique, des jeux vidéo à la médecine en passant par l'automatisation de la fabrication. 

Prenez simplement un peu de temps et créez un petit modèle si vous êtes intéressé par l'apprentissage automatique. À mesure que vous commencez à vous sentir plus à l'aise, ajoutez à ce modèle et continuez à apprendre davantage.