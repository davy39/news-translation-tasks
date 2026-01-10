---
title: Comment effectuer une classification avec l'apprentissage automatique automatisé
  (AutoML)
subtitle: ''
author: Piotr Plonski
co_authors: []
series: null
date: '2020-05-11T19:15:12.000Z'
originalURL: https://freecodecamp.org/news/classification-with-python-automl
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/Untitled-Design--1-.jpg
tags:
- name: automation
  slug: automation
- name: image classification
  slug: image-classification
- name: Machine Learning
  slug: machine-learning
seo_title: Comment effectuer une classification avec l'apprentissage automatique automatisé
  (AutoML)
seo_desc: 'In this article I will show you how to use Automated Machine Learning (AutoML)
  to build a classifier for tabular data. And don''t worry – I will explain all strange
  definitions :)

  There won''t be any math in this article (although I like math, it is co...'
---

Dans cet article, je vais vous montrer comment utiliser l'apprentissage automatique automatisé (AutoML) pour construire un classificateur pour des données tabulaires. Et ne vous inquiétez pas, je vais expliquer toutes les définitions étranges :)

Il n'y aura pas de mathématiques dans cet article (bien que j'aime les mathématiques, elles sont concises). Je vais essayer de montrer les choses de manière à ce que vous puissiez mieux comprendre l'apprentissage automatique (et l'AutoML).

## Commençons par le commencement : qu'est-ce que l'apprentissage automatique ?

**L'apprentissage automatique (ML)** est un sujet très vaste. Nous pouvons utiliser sa définition pour expliquer ce que c'est : enseigner à une machine à effectuer une tâche. Cela ressemble beaucoup à la programmation !

La différence clé est qu'en programmation, vous devez fournir une recette exacte (code) qui indique à la machine comment elle doit effectuer la tâche. En **apprentissage automatique**, vous fournissez également le code, mais ce code indiquera à la machine comment apprendre sur la base d'exemples précédents (données historiques).

Ce code est ensuite utilisé pour créer un **modèle d'apprentissage automatique**. Toutes les actions futures effectuées par la machine seront calculées par le modèle.

C'est une définition très large, mais vous devriez en obtenir une compréhension de base sur le ML. J'ai préparé quelques schémas montrant comment fonctionne la programmation par rapport à l'apprentissage automatique. J'espère qu'ils vous aideront à visualiser la différence.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/programming.jpg align="left")

*En programmation, les humains doivent fournir des étapes exactes (code) pour indiquer à une machine comment elle doit traiter les données d'entrée.*

![Image](https://www.freecodecamp.org/news/content/images/2020/05/ml.jpg align="left")

*En apprentissage automatique, les humains doivent fournir du code et des données historiques pour créer des modèles d'apprentissage automatique. Après l'entraînement du modèle ML, il peut être utilisé pour calculer des sorties sur des données invisibles.*

Sur les images ci-dessus, vous pouvez voir que la programmation est souvent beaucoup plus simple que l'apprentissage automatique (nombre moins élevé d'étapes totales, et pas besoin de données historiques).

Et il semble souvent que la programmation soit beaucoup plus facile que le ML. Mais il existe des situations où fournir le programme exact est impossible.

Par exemple : les tâches de classification d'images - disons que vous souhaitez savoir ce qu'il y a dans l'image en fonction de son contenu. Il est impossible d'écrire toutes les conditions pour reconnaître ce qu'il y a dans une image (les images peuvent avoir différentes tailles, échelles, etc.). Il est facile de le voir avec l'œil humain, mais écrire un programme exact est impossible.

Mais avec le ML, vous pouvez créer un modèle qui sera capable de reconnaître des images. Alors regardons quelques définitions supplémentaires.

### Classification

La classification est le processus d'attribution d'une étiquette (classe) à un échantillon (une instance de données). Le modèle ML qui effectue une classification est appelé un **classificateur**.

### Données tabulaires

Les données tabulaires sont simplement des données au format tableau, similaires à une feuille de calcul. D'autres formats de données peuvent être des images, des vidéos, du texte, des documents ou de l'audio. Les données au format tabulaire ont des lignes qui représentent des échantillons (observations) et des colonnes qui représentent des caractéristiques.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/tabular-data_01.png align="left")

*Exemple de données tabulaires (ensemble de données Titanic).*

Dans cet article, nous analyserons uniquement les données tabulaires. La tâche typique en ML est de prédire l'une des colonnes. Une telle colonne est appelée la colonne **cible**.

## L'ensemble de données Iris

Je vais vous montrer comment construire un modèle d'apprentissage automatique avec AutoML sur un ensemble de données très simple appelé **Iris**. Les données peuvent être téléchargées depuis de nombreux endroits (ce sont les mêmes données !) :

* Dépôt de données UCI : [https://archive.ics.uci.edu/ml/datasets/Iris](https://archive.ics.uci.edu/ml/datasets/Iris)

* Ma collection de bons ensembles de données pour commencer avec le ML : [https://github.com/pplonski/datasets-for-start/blob/master/iris/data.csv](https://github.com/pplonski/datasets-for-start/blob/master/iris/data.csv)

* Kaggle : [https://www.kaggle.com/uciml/iris](https://www.kaggle.com/uciml/iris)

L'ensemble de données **Iris** contient 150 lignes, où chaque ligne décrit une fleur. Chaque ligne a 4 caractéristiques (colonnes) qui décrivent les propriétés de la fleur. Ces caractéristiques sont :

* longueur du sépale (cm)

* largeur du sépale (cm)

* longueur du pétale (cm)

* largeur du pétale (cm)

Une étiquette (classe) est attribuée à chaque fleur qui nous indique de quel type d'iris il s'agit. Dans cet ensemble de données, il y a 3 classes :

* setosa

* versicolor

* virginica

Prenons la première ligne des données. Nous avons :

* longueur du sépale = 5,1 cm

* largeur du sépale = 3,5 cm

* longueur du pétale = 1,4 cm

* largeur du pétale = 0,2 cm

* classe = setosa

La première ligne nous indique que quelqu'un a pris le type d'iris 'setosa', a mesuré ses propriétés de sépale et de pétale, et l'a enregistré dans l'ensemble de données.

Où est l'apprentissage automatique ici ? Supposons que nous avons un ensemble de fleurs d'iris mais que nous ne savons pas quels types (classes) elles sont. Nous savons comment mesurer la longueur et la largeur du sépale et du pétale mais nous ne pouvons pas dire de quel type ou classe d'iris il s'agit.

Nous pouvons utiliser l'apprentissage automatique pour **classifier** la fleur en fonction de nos mesures. Le modèle ML prendra en entrée les 4 nombres (nos mesures) et sortira la classe de la fleur.

## Commençons à coder !

Je vais utiliser Python dans ce tutoriel. Je suppose donc que vous avez Python installé et que vous savez comment installer des packages.

Nous aurons besoin de quelques packages, et tous seront installés avec le package AutoML [mljar-supervised](https://github.com/mljar/mljar-supervised). Pour l'installer, exécutez :

```python
pip install mljar-supervised
```

Tout le code présenté dans cet article est disponible sur [github](https://www.freecodecamp.org/news/p/49d67cd9-1642-43c6-902d-edcfd56ab013/(https://github.com/mljar/mljar-examples/blob/master/Iris_classification/Iris_classification.ipynb). Au début, importons les packages dont nous avons besoin :

```python
import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from supervised.automl import AutoML
```

Ensuite, chargeons les données :

```python
data = datasets.load_iris()
X = pd.DataFrame(data["data"], columns=data["feature_names"])
y = pd.Series(data["target"], name="target").map({i:v for i, v in enumerate(data["target_names"])})
```

Voici à quoi ressemblent nos données :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-75.png align="left")

*La variable* `X` *( `print(X)` )

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-76.png align="left")

*La variable* `y` *( `print(y)` )

Nous allons diviser nos données en deux ensembles distincts :

* **train** - échantillons qui seront utilisés pour entraîner le modèle d'apprentissage automatique

* **test** - échantillons que nous utiliserons pour vérifier comment notre modèle d'apprentissage automatique fonctionne sur des données invisibles (dans le processus d'entraînement)

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)
```

Nous utiliserons 90 % de nos données pour l'entraînement (90 % * 150 = 135 échantillons) et 10 % (15 échantillons) pour les tests.

Maintenant que nos données sont prêtes, nous pouvons entraîner le modèle d'apprentissage automatique. Peut-être avez-vous entendu dire qu'il existe de nombreux algorithmes ML. Tous peuvent être utilisés pour l'entraînement de modèles, comme les modèles suivants :

* Arbre de décision,

* Régression logistique,

* Forêt aléatoire,

* Réseaux de neurones,

* Xgboost,

pour n'en nommer que quelques-uns.

### Quel modèle devons-nous utiliser ? Lequel est le meilleur ?

Il n'y a pas de réponse unique aux questions ci-dessus. Tout dépend des données elles-mêmes. L'approche courante consiste à vérifier autant que possible et à sélectionner le modèle le mieux performant. Très souvent, les algorithmes les plus simples sont très bons pour commencer.

Mais ce n'est pas la fin de nos problèmes. Chacun des algorithmes a généralement des paramètres qui contrôlent la manière dont le modèle est entraîné. Ce sont les soi-disant **hyper-paramètres**. Ils doivent être soigneusement définis pour l'algorithme. Pour sélectionner leurs valeurs, nous devons également en vérifier quelques-unes.

Pour sélectionner l'algorithme et les hyper-paramètres, nous pouvons utiliser une validation qui peut être effectuée de nombreuses manières différentes. Je ne vais pas entrer dans les détails de la validation. Je vais simplement vous montrer l'outil qui peut gérer tous les problèmes ci-dessus. C'est l'**apprentissage automatique automatisé (AutoML)**.

AutoML peut vérifier de nombreux algorithmes ML différents et ajuster les hyper-paramètres pour eux. Il recherchera le meilleur modèle ML pour les données disponibles.

Dans la vie réelle, AutoML est utilisé pour faire encore plus, comme l'ingénierie des caractéristiques (préparation des caractéristiques pour l'analyse et construction de nouvelles) ou le déploiement de modèles en tant qu'API REST.

J'utilise `AutoML` du package `mljar-supervised` (dont je suis l'auteur). Il a une interface très simple. Entraînons le modèle :

```python
automl = AutoML(algorithms=["Decision Tree", "Linear", "Random Forest"],
                total_time_limit=5*60)
automl.fit(X_train, y_train)
```

Les deux lignes ci-dessus vérifieront 3 algorithmes différents pour nous : Arbre de décision, Régression logistique et Forêt aléatoire. Ensuite, il sélectionnera le meilleur. Il y a une limite de temps définie à 5 minutes (5*60 secondes) pour le temps total d'entraînement.

En résultat de l'exécution de `AutoML`, vous obtiendrez une sortie comme celle-ci :

```python
Create directory AutoML_1
AutoML task to be solved: multiclass_classification
AutoML will use algorithms: ['Decision Tree', 'Linear', 'Random Forest']
AutoML will optimize for metric: logloss
AutoML will try to check about 33 models
Decision Tree final logloss 0.5453226492448378 time 30.04 seconds
Decision Tree final logloss 0.6419811899692177 time 21.25 seconds
Decision Tree final logloss 0.4569697687554296 time 16.73 seconds
Linear final logloss 0.16507067466592637 time 15.68 seconds
Random Forest final logloss 0.11891177026579884 time 28.72 seconds
Random Forest final logloss 0.24256194594421207 time 28.73 seconds
Random Forest final logloss 0.2761028104749779 time 27.61 seconds
Random Forest final logloss 0.2536702528991272 time 29.0 seconds
Random Forest final logloss 0.1752405529204018 time 27.86 seconds
Random Forest final logloss 0.17394416017742964 time 27.69 seconds
Ensemble final logloss 0.11781603875353275 time 0.36 seconds
```

Les résultats de cette expérience AutoML sont disponibles sur [github](https://github.com/mljar/mljar-examples/tree/master/Iris_classification/AutoML_1#automl-leaderboard). Lorsque vous regardez dans le répertoire créé par `AutoML`, vous verrez le fichier `README.md`. Il contient le rapport de l'entraînement :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-77.png align="left")

De plus, vous pouvez vérifier chaque modèle entraîné en cliquant sur son lien :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-78.png align="left")

Pour calculer les prédictions, exécutez simplement les lignes suivantes :

```python
y_predicted = automl.predict(X_test)

print(pd.DataFrame({"Predicted": y_predicted["label"], "Target": np.array(y_test)}))
```

Vous obtiendrez ce qui suit :

```python
     Predicted      Target
0       setosa      setosa
1    virginica  versicolor
2   versicolor  versicolor
3    virginica   virginica
4   versicolor  versicolor
5       setosa      setosa
6       setosa      setosa
7   versicolor  versicolor
8       setosa      setosa
9   versicolor  versicolor
10   virginica   virginica
11  versicolor  versicolor
12   virginica   virginica
13   virginica   virginica
14  versicolor  versicolor
```

D'après ce qui précède, vous pouvez voir qu'il y a eu 1 erreur dans les prédictions (la ligne avec l'index 1). Le modèle ML a prédit la classe `virginica` mais il aurait dû être `versicolor`. La précision du modèle ML est :

```python
Accuracy = 14 (correct answers) / 15 (total samples) = 93.33%
```

## Résumé

Dans cet article, je vous ai montré les différences entre la programmation et l'apprentissage automatique. J'espère que vous le comprenez un peu mieux.

L'apprentissage automatique est un sujet très vaste et ne peut certainement pas être présenté dans un seul article. Apprendre et appliquer le ML peut vous donner beaucoup de satisfaction, alors j'encourage tout le monde à explorer davantage.

L'apprentissage automatique automatisé améliore le processus d'entraînement des modèles en automatisant la recherche d'algorithmes et d'hyper-paramètres. J'espère que l'AutoML rendra le ML plus accessible à de nombreux développeurs.

Si vous avez des questions ou si vous souhaitez lire plus d'articles comme celui-ci, faites-le moi savoir.