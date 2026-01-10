---
title: Comment construire et entraîner des modèles ML de régression linéaire et logistique
  en Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-29T23:18:53.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-and-train-linear-and-logistic-regression-ml-models-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/machine-learning-pairplot.png
tags:
- name: Machine Learning
  slug: machine-learning
- name: statistics
  slug: statistics
seo_title: Comment construire et entraîner des modèles ML de régression linéaire et
  logistique en Python
seo_desc: 'By Nick McCullum

  Linear regression and logistic regression are two of the most popular machine learning
  models today.

  In the last article, you learned about the history and theory behind a linear regression
  machine learning algorithm.

  This tutorial w...'
---

Par Nick McCullum

La régression linéaire et la régression logistique sont deux des [modèles d'apprentissage automatique les plus populaires aujourd'hui.](https://gumroad.com/l/pGjwd)

Dans le [dernier article](https://www.freecodecamp.org/news/deep-learning-neural-networks-explained-in-plain-english/), vous avez appris l'histoire et la théorie derrière un algorithme d'apprentissage automatique de régression linéaire.

Ce tutoriel vous apprendra à créer, entraîner et tester votre premier modèle d'apprentissage automatique de régression linéaire en Python en utilisant la bibliothèque `scikit-learn`.

## Section 1 : Régression linéaire

### Le jeu de données que nous utiliserons dans ce tutoriel

Puisque nous commençons tout juste à apprendre la régression linéaire en apprentissage automatique, nous travaillerons avec des jeux de données créés artificiellement dans ce tutoriel. Cela vous permettra de vous concentrer sur l'apprentissage des concepts d'apprentissage automatique et d'éviter de passer un temps inutile à nettoyer ou manipuler des données.

Plus spécifiquement, nous travaillerons avec un jeu de données de données immobilières et tenterons de prédire les prix des logements. Avant de construire le modèle, nous devrons d'abord importer les bibliothèques requises.

### Les bibliothèques que nous utiliserons dans ce tutoriel

La première bibliothèque que nous devons importer est [pandas](https://nickmccullum.com/advanced-python/pandas-dataframes/), qui est un mot-valise de « panel data » et est la bibliothèque Python la plus populaire pour travailler avec des données tabulaires.

Il est conventionnel d'importer `pandas` sous l'alias `pd`. Vous pouvez importer `pandas` avec l'instruction suivante :

```

import pandas as pd

```

Ensuite, nous devrons importer [NumPy](https://nickmccullum.com/advanced-python/numpy/), qui est une bibliothèque populaire pour le calcul numérique. NumPy est connu pour sa structure de données [NumPy array](https://nickmccullum.com/advanced-python/numpy-arrays/) ainsi que pour ses méthodes utiles [reshape](https://nickmccullum.com/numpy-np-reshape/), [arange](https://nickmccullum.com/how-to-use-numpy-arange/), et [append](https://nickmccullum.com/numpy-np-append/).

Il est conventionnel d'importer NumPy sous l'alias `np`. Vous pouvez importer `numpy` avec l'instruction suivante :

```

import numpy as np

```

Ensuite, nous devons importer [matplotlib](https://nickmccullum.com/python-visualization/how-to-import-matplotlib/), qui est la bibliothèque la plus populaire de Python pour la [visualisation de données](https://nickmccullum.com/python-visualization/).

`matplotlib` est typiquement importé sous l'alias `plt`. Vous pouvez importer `matplotlib` avec l'instruction suivante :

```

import matplotlib.pyplot as plt

%matplotlib inline

```

L'instruction `%matplotlib inline` fera en sorte que nos visualisations `matplotlib` s'intègrent directement dans notre Jupyter Notebook, ce qui les rend plus faciles à accéder et à interpréter.

Enfin, vous voudrez importer `seaborn`, qui est une autre bibliothèque de visualisation de données Python qui facilite la création de belles visualisations en utilisant matplotlib.

Vous pouvez importer `seaborn` avec l'instruction suivante :

```

import seaborn as sns

```

Pour résumer, voici toutes les importations requises dans ce tutoriel :

```

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

%matplotlib inline

import seaborn as sns

```

Dans les futurs articles, je préciserai quelles importations sont nécessaires, mais je n'expliquerai pas chaque importation en détail comme je l'ai fait ici.

### Importation du jeu de données

Comme mentionné, nous utiliserons un jeu de données d'informations immobilières. Nous utiliserons

Le jeu de données a été téléchargé sur mon site web sous forme de fichier `.csv` à l'URL suivante :

```
https://nickmccullum.com/files/Housing_Data.csv

```

Pour importer le jeu de données dans votre [Jupyter Notebook](https://nickmccullum.com/python-course/jupyter-notebook-basics/), la première chose que vous devriez faire est de télécharger le fichier en copiant et collant cette URL dans votre navigateur. Ensuite, déplacez le fichier dans le même répertoire que votre Jupyter Notebook.

Une fois cela fait, l'instruction [Python](https://courses.nickmccullum.com/courses/enroll/python-for-finance/) suivante importera le jeu de données immobilier dans votre Jupyter Notebook :

```

raw_data = pd.read_csv('Housing_Data.csv')

```

Ce jeu de données a un certain nombre de caractéristiques, y compris :

* Le revenu moyen dans la zone de la maison
* Le nombre moyen de pièces totales dans la zone
* Le prix auquel la maison a été vendue
* L'adresse de la maison

Ces données sont générées aléatoirement, donc vous verrez quelques nuances qui pourraient ne pas avoir de sens normalement (comme un grand nombre de décimales après un nombre qui devrait être un entier).

### Comprendre le jeu de données

Maintenant que le jeu de données a été importé sous la variable `raw_data`, vous pouvez utiliser la méthode `info` pour obtenir quelques informations de haut niveau sur le jeu de données. Plus précisément, l'exécution de `raw_data.info()` donne :

```
<class 'pandas.core.frame.DataFrame'>

RangeIndex: 5000 entrées, 0 à 4999

Data columns (total 7 colonnes) :

Avg. Area Income                5000 non-null float64

Avg. Area House Age             5000 non-null float64

Avg. Area Number of Rooms       5000 non-null float64

Avg. Area Number of Bedrooms    5000 non-null float64

Area Population                 5000 non-null float64

Price                           5000 non-null float64

Address                         5000 non-null object

dtypes: float64(6), object(1)

memory usage: 273.6+ KB

```

Une autre façon utile d'apprendre à connaître ce jeu de données est de générer un pairplot. Vous pouvez utiliser la méthode `pairplot` de `seaborn` pour cela, et passer l'ensemble du `DataFrame` en tant que paramètre. Voici l'instruction complète pour cela :

```

sns.pairplot(raw_data)

```

La sortie de cette instruction est ci-dessous :

![Un pairplot seaborn](https://nickmccullum.com/images/python-machine-learning/linear-regression/machine-learning-pairplot.png)

Ensuite, commençons à construire notre modèle de régression linéaire.

### Construction d'un modèle de régression linéaire en apprentissage automatique

La première chose que nous devons faire est de diviser nos données en un `x-array` (qui contient les données que nous utiliserons pour faire des prédictions) et un `y-array` (qui contient les données que nous essayons de prédire.

Tout d'abord, nous devrions décider quelles colonnes inclure. Vous pouvez générer une liste des colonnes du DataFrame en utilisant `raw_data.columns`, qui produit :

```
Index(['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',

       'Avg. Area Number of Bedrooms', 'Area Population', 'Price', 'Address'],

      dtype='object')

```

Nous utiliserons toutes ces variables dans le `x-array` sauf pour `Price` (puisque c'est la variable que nous essayons de prédire) et `Address` (puisqu'il ne contient que du texte).

Créons notre `x-array` et assignons-le à une variable appelée `x`.

```

x = raw_data[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',

       'Avg. Area Number of Bedrooms', 'Area Population']]

```

Ensuite, créons notre `y-array` et assignons-le à une variable appelée `y`.

```

y = raw_data['Price']

```

Nous avons réussi à diviser notre jeu de données en un `x-array` (qui sont les valeurs d'entrée de notre modèle) et un `y-array` (qui sont les valeurs de sortie de notre modèle). Nous apprendrons comment diviser davantage notre jeu de données en données d'entraînement et données de test dans la section suivante.

### Division de notre jeu de données en données d'entraînement et données de test

`scikit-learn` facilite grandement la division de notre jeu de données en données d'entraînement et données de test. Pour ce faire, nous devrons importer la fonction `train_test_split` du module `model_selection` de `scikit-learn`.

Voici le code complet pour cela :

```

from sklearn.model_selection import train_test_split

```

La fonction `train_test_split` accepte trois arguments :

* Notre `x-array`
* Notre `y-array`
* La taille souhaitée de nos données de test

Avec ces paramètres, la fonction `train_test_split` divisera nos données pour nous ! Voici le code pour cela si nous voulons que nos données de test représentent 30 % de l'ensemble du jeu de données :

```

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3)

```

Décomposons ce qui se passe ici.

La fonction `train_test_split` retourne une [liste Python](https://nickmccullum.com/python-course/lists/) de longueur 4, où chaque élément de la liste est `x_train`, `x_test`, `y_train`, et `y_test`, respectivement. Nous utilisons ensuite le déballage de liste pour assigner les valeurs appropriées aux noms de variables corrects.

Maintenant que nous avons correctement divisé notre jeu de données, il est temps de construire et d'entraîner notre modèle d'apprentissage automatique de régression linéaire.

### Construction et entraînement du modèle

La première chose que nous devons faire est d'importer l'estimateur `LinearRegression` de `scikit-learn`. Voici l'instruction Python pour cela :

```

from sklearn.linear_model import LinearRegression

```

Ensuite, nous devons créer une instance de l'objet Python `Linear Regression`. Nous l'assignerons à une variable appelée `model`. Voici le code pour cela :

```

model = LinearRegression()

```

Nous pouvons utiliser la méthode `fit` de `scikit-learn` pour entraîner ce modèle sur nos données d'entraînement.

```

model.fit(x_train, y_train)

```

Notre modèle a maintenant été entraîné. Vous pouvez examiner chacun des coefficients du modèle en utilisant l'instruction suivante :

```

print(model.coef_)

```

Cela imprime :

```
[2.16176350e+01 1.65221120e+05 1.21405377e+05 1.31871878e+03

 1.52251955e+01]

```

De même, voici comment vous pouvez voir l'interception de l'équation de régression :

```

print(model.intercept_)

```

Cela imprime :

```
-2641372.6673013503

```

Une manière plus agréable de visualiser les coefficients est de les placer dans un DataFrame. Cela peut être fait avec l'instruction suivante :

```

pd.DataFrame(model.coef_, x.columns, columns = ['Coeff'])

```

La sortie dans ce cas est beaucoup plus facile à interpréter :

![Un DataFrame de coefficients dans un Jupyter Notebook](https://nickmccullum.com/images/python-machine-learning/linear-regression/coefficient-dataframe.png)

Prenons un moment pour comprendre ce que signifient ces coefficients. Regardons spécifiquement la variable `Area Population`, qui a un coefficient d'environ `15`.

Cela signifie que si vous gardez toutes les autres variables constantes, alors une augmentation d'une unité de `Area Population` entraînera une augmentation de `15` unités de la variable prédite - dans ce cas, `Price`.

En d'autres termes, de grands coefficients sur une variable spécifique signifient que cette variable a un grand impact sur la valeur de la variable que vous essayez de prédire. De même, de petites valeurs ont un petit impact.

Maintenant que nous avons généré notre premier modèle d'apprentissage automatique de régression linéaire, il est temps d'utiliser le modèle pour faire des prédictions à partir de notre jeu de données de test.

### Faire des prédictions à partir de notre modèle

`scikit-learn` facilite grandement la réalisation de prédictions à partir d'un modèle d'apprentissage automatique. Vous devez simplement appeler la méthode `predict` sur la variable `model` que nous avons créée précédemment.

Puisque la variable `predict` est conçue pour faire des prédictions, elle n'accepte qu'un paramètre `x-array`. Elle générera les valeurs `y` pour vous !

Voici le code dont vous aurez besoin pour générer des prédictions à partir de notre modèle en utilisant la méthode `predict` :

```

predictions = model.predict(x_test)

```

La variable `predictions` contient les valeurs _prédites_ des caractéristiques stockées dans `x_test`. Puisque nous avons utilisé la méthode `train_test_split` pour stocker les valeurs _réelles_ dans `y_test`, ce que nous voulons faire ensuite est comparer les valeurs du tableau `predictions` avec les valeurs de `y_test`.

Un moyen facile de faire cela est de tracer les deux tableaux en utilisant un nuage de points. Il est facile de construire des [nuages de points matplotlib](https://nickmccullum.com/python-visualization/scatterplot/) en utilisant la méthode `plt.scatter`. Voici le code pour cela :

```

plt.scatter(y_test, predictions)

```

Voici le nuage de points que ce code génère :

![Un nuage de points des valeurs prédites par rapport aux valeurs réalisées dans un modèle d'apprentissage automatique de régression linéaire](https://nickmccullum.com/images/python-machine-learning/linear-regression/regression-scatterplot.png)

Comme vous pouvez le voir, nos valeurs prédites sont très proches des valeurs réelles pour les observations du jeu de données. Une ligne diagonale parfaitement droite dans ce nuage de points indiquerait que notre modèle a parfaitement prédit les valeurs du `y-array`.

Une autre façon d'évaluer visuellement les performances de notre modèle est de tracer ses `résidus`, qui sont la différence entre les valeurs réelles du `y-array` et les valeurs prédites du `y-array`.

Un moyen facile de faire cela est avec l'instruction suivante :

```

plt.hist(y_test - predictions)

```

Voici la visualisation que ce code génère :

![Un histogramme des résidus de notre modèle d'apprentissage automatique de régression linéaire](https://nickmccullum.com/images/python-machine-learning/linear-regression/residuals-histogram.png)

Il s'agit d'un histogramme des résidus de notre modèle d'apprentissage automatique.

Vous pouvez remarquer que les résidus de notre modèle d'apprentissage automatique semblent être normalement distribués. C'est un très bon signe !

Cela indique que nous avons sélectionné un type de modèle approprié (dans ce cas, la régression linéaire) pour faire des prédictions à partir de notre jeu de données. Nous en apprendrons davantage sur la manière de vous assurer que vous utilisez le bon modèle plus tard dans ce cours.

### Test des performances de notre modèle

Nous avons appris au début de ce cours qu'il existe trois principales métriques de performance utilisées pour les modèles d'apprentissage automatique de régression :

* Erreur absolue moyenne
* Erreur quadratique moyenne
* Racine de l'erreur quadratique moyenne

Nous allons maintenant voir comment calculer chacune de ces métriques pour le modèle que nous avons construit dans ce tutoriel. Avant de continuer, exécutez l'instruction d'importation suivante dans votre Jupyter Notebook :

```

from sklearn import metrics

```

Erreur absolue moyenne (MAE)

Vous pouvez calculer l'erreur absolue moyenne en Python avec l'instruction suivante :

```

metrics.mean_absolute_error(y_test, predictions)

```

### Erreur quadratique moyenne (MSE)

De même, vous pouvez calculer l'erreur quadratique moyenne en Python avec l'instruction suivante :

```

metrics.mean_squared_error(y_test, predictions)

```

### **Racine de l'erreur quadratique moyenne (RMSE)**

Contrairement à l'erreur absolue moyenne et à l'erreur quadratique moyenne, `scikit-learn` ne possède pas réellement de méthode intégrée pour calculer la racine de l'erreur quadratique moyenne.

Heureusement, ce n'est pas vraiment nécessaire. Puisque la racine de l'erreur quadratique moyenne est simplement la racine carrée de l'erreur quadratique moyenne, vous pouvez utiliser la méthode `sqrt` de NumPy pour la calculer facilement :

```

np.sqrt(metrics.mean_squared_error(y_test, predictions))

```

### Le code complet pour ce tutoriel

Voici l'ensemble du code pour ce tutoriel Python sur l'apprentissage automatique de la régression linéaire. Vous pouvez également le consulter dans [ce dépôt GitHub](https://github.com/nicholasmccullum/python-machine-learning/tree/master).

```

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

import seaborn as sns

%matplotlib inline

raw_data = pd.read_csv('Housing_Data.csv')

x = raw_data[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',

       'Avg. Area Number of Bedrooms', 'Area Population']]

y = raw_data['Price']

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3)

from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(x_train, y_train)

print(model.coef_)

print(model.intercept_)

pd.DataFrame(model.coef_, x.columns, columns = ['Coeff'])

predictions = model.predict(x_test)

# plt.scatter(y_test, predictions)

plt.hist(y_test - predictions)

from sklearn import metrics

metrics.mean_absolute_error(y_test, predictions)

metrics.mean_squared_error(y_test, predictions)

np.sqrt(metrics.mean_squared_error(y_test, predictions))

```

## Section 2 : Régression logistique  


Note - si vous avez suivi ce tutoriel jusqu'à présent et construit votre modèle de régression linéaire, vous voudrez ouvrir un nouveau Jupyter Notebook (sans code) avant de continuer.

### Le jeu de données que nous utiliserons dans ce tutoriel

Le jeu de données Titanic est un jeu de données très célèbre qui contient des caractéristiques sur les passagers du Titanic. Il est souvent utilisé comme jeu de données d'introduction pour les problèmes de régression logistique.

Dans ce tutoriel, nous utiliserons le jeu de données Titanic combiné avec un modèle de régression logistique Python pour prédire si un passager a survécu ou non au naufrage du Titanic.

Le [jeu de données original du Titanic](https://www.kaggle.com/c/titanic) est disponible publiquement sur [Kaggle.com](https://www.kaggle.com/), qui est un site web hébergeant des jeux de données et des compétitions de science des données.

Pour vous faciliter la tâche en tant qu'étudiant dans ce cours, nous utiliserons une version semi-nettoyée du jeu de données Titanic, ce qui vous fera gagner du temps sur le nettoyage et la manipulation des données.

Le jeu de données Titanic nettoyé a en fait déjà été mis à votre disposition. Vous pouvez télécharger le fichier de données en cliquant sur les liens ci-dessous :

* [Données Titanic](https://nickmccullum.com/files/logistic-regression/titanic_train.csv)

Une fois ce fichier téléchargé, ouvrez un [Jupyter Notebook](https://nickmccullum.com/python-course/jupyter-notebook-basics/) dans le même répertoire de travail et nous pouvons commencer à construire notre [modèle de régression logistique.](https://nickmccullum.com/python-machine-learning/introduction-logistic-regression/)

### Les importations que nous utiliserons dans ce tutoriel

Comme précédemment, nous utiliserons plusieurs bibliothèques logicielles open-source dans ce tutoriel. Voici les importations que vous devrez exécuter pour suivre pendant que je code notre modèle de régression logistique Python :

```

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

%matplotlib inline

import seaborn as sns


```

Ensuite, nous devrons importer le jeu de données Titanic dans notre script Python.

### Importation du jeu de données dans notre script Python

Nous utiliserons la méthode `read_csv` de pandas pour importer nos fichiers `csv` dans des [DataFrames pandas](https://nickmccullum.com/advanced-python/pandas-dataframes/) appelés `titanic_data`.

Voici le code pour cela :

```

titanic_data = pd.read_csv('titanic_train.csv')


```

Ensuite, examinons quelles données sont réellement incluses dans le jeu de données Titanic. Il existe deux méthodes principales pour cela (en utilisant spécifiquement le DataFrame `titanic_data`) :

* La méthode `titanic_data.head(5)` imprimera les 5 premières lignes du DataFrame. Vous pouvez substituer `5` par le nombre que vous souhaitez.
* Vous pouvez également imprimer `titanic_data.columns`, ce qui vous montrera les noms des colonnes.

L'exécution de la deuxième commande (`titanic_data.columns`) génère la sortie suivante :

```

Index(['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',

       'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'],

      dtype='object'


```

Ce sont les noms des colonnes dans le DataFrame. Voici de brèves explications de chaque point de données :

* `PassengerId` : un identifiant numérique pour chaque passager du Titanic.
* `Survived` : un identifiant binaire qui indique si le passager a survécu ou non au naufrage du Titanic. Cette variable aura une valeur de `1` s'ils ont survécu et `0` s'ils ne l'ont pas fait.
* `Pclass` : la classe du passager en question. Cela peut avoir une valeur de `1`, `2`, ou `3`, selon l'endroit où le passager se trouvait dans le navire.
* `Name` : le nom du passager.`
* `Sex` : masculin ou féminin.
* `Age` : l'âge (en années) du passager.
* `SibSp` : le nombre de frères et sœurs et d'époux à bord du navire.
* `Parch` : le nombre de parents et d'enfants à bord du navire.
* `Ticket` : le numéro de ticket du passager.
* `Fare` : combien le passager a payé pour son ticket sur le Titanic.
* `Cabin` : le numéro de cabine du passager.
* `Embarked` : le port où le passager a embarqué (C = Cherbourg, Q = Queenstown, S = Southampton)

Ensuite, nous en apprendrons davantage sur notre jeu de données en utilisant quelques techniques d'analyse exploratoire des données.

### Apprendre à connaître notre jeu de données avec l'analyse exploratoire des données

### **La prévalence de chaque catégorie de classification**

Lors de l'utilisation de techniques d'apprentissage automatique pour modéliser des problèmes de classification, il est toujours bon d'avoir une idée du ratio entre les catégories. Pour ce problème spécifique, il est utile de voir combien de survivants par rapport aux non-survivants existent dans nos données d'entraînement.

Un moyen facile de visualiser cela est d'utiliser le tracé `countplot` de `seaborn`. Dans cet exemple, vous pourriez créer le tracé `seasborn` approprié avec le code Python suivant :

```

sns.countplot(x='Survived', data=titanic_data)


```

Cela génère le tracé suivant :

![Un countplot seaborn](https://nickmccullum.com/images/python-machine-learning/logistic-regression/seaborn-countplot.png)

Comme vous pouvez le voir, nous avons beaucoup plus d'incidences de non-survivants que de survivants.

### **Taux de survie entre les sexes**

Il est également utile de comparer les taux de survie par rapport à une autre caractéristique des données. Par exemple, nous pouvons comparer les taux de survie entre les valeurs `Male` et `Female` pour `Sex` en utilisant le code Python suivant :

```

sns.countplot(x='Survived', hue='Sex', data=titanic_data)


```

Cela génère le tracé suivant :

![Un countplot seaborn avec une teinte Sex](https://nickmccullum.com/images/python-machine-learning/logistic-regression/seaborn-countplot-hue-sex.png)

Comme vous pouvez le voir, les passagers avec un `Sex` de `Male` étaient beaucoup plus susceptibles d'être des non-survivants que les passagers avec un `Sex` de `Female`.

### **Taux de survie entre les classes de passagers**

Nous pouvons effectuer une analyse similaire en utilisant la variable `Pclass` pour voir quelle classe de passagers était la plus (et la moins) susceptible d'avoir des passagers survivants.

Voici le code pour cela :

```

sns.countplot(x='Survived', hue='Pclass', data=titanic_data)


```

Cela génère le tracé suivant :

![Un countplot seaborn avec une teinte Pclass](https://nickmccullum.com/images/python-machine-learning/logistic-regression/seaborn-countplot-hue-pclass.png)

L'observation la plus notable de ce tracé est que les passagers avec une valeur `Pclass` de `3` - ce qui indique la troisième classe, qui était la moins chère et la moins luxueuse - étaient beaucoup plus susceptibles de mourir lorsque le Titanic a coulé.

### **La distribution d'âge des passagers du Titanic**

Une autre analyse utile que nous pourrions effectuer est d'examiner la distribution d'âge des passagers du Titanic. Un [histogramme](https://nickmccullum.com/python-visualization/histogram/) est un excellent outil pour cela.

Vous pouvez générer un histogramme de la variable `Age` avec le code suivant :

```

plt.hist(titanic_data['Age'].dropna())


```

Notez que la méthode `dropna()` est nécessaire puisque le jeu de données contient plusieurs valeurs nulles.

Voici l'histogramme que ce code génère :

![Un histogramme des variables d'âge du jeu de données titanic](https://nickmccullum.com/images/python-machine-learning/logistic-regression/age-histogram.png)

Comme vous pouvez le voir, il y a une concentration de passagers du Titanic avec une valeur `Age` entre `20` et `40`.

### **La distribution des prix des billets des passagers du Titanic**

La dernière technique d'analyse exploratoire des données que nous utiliserons est l'examen de la distribution des prix des billets dans le jeu de données Titanic.

Vous pouvez faire cela avec le code suivant :

```

plt.hist(titanic_data['Fare'])


```

Cela génère le tracé suivant :

![Un histogramme des variables de tarif du jeu de données titanic](https://nickmccullum.com/images/python-machine-learning/logistic-regression/fare-histogram.png)

Comme vous pouvez le voir, il y a trois groupes distincts de prix de `Fare` dans le jeu de données Titanic. Cela a du sens car il y a également trois valeurs uniques pour la variable `Pclass`. Les différents groupes de `Fare` correspondent aux différentes catégories de `Pclass`.

Puisque le jeu de données Titanic est un jeu de données du monde réel, il contient certaines données manquantes. Nous apprendrons [comment gérer les données manquantes](https://nickmccullum.com/advanced-python/missing-data-pandas/) dans la section suivante.

### Suppression des données nulles de notre jeu de données

Pour commencer, examinons où notre jeu de données contient des données manquantes. Pour ce faire, exécutez la commande suivante :

```

titanic_data.isnull()


```

Cela générera un DataFrame de valeurs booléennes où la cellule contient `True` si c'est une valeur nulle et `False` sinon. Voici une image de ce à quoi cela ressemble :

![Un DataFrame de valeurs booléennes indiquant où les données nulles existent](https://nickmccullum.com/images/python-machine-learning/logistic-regression/missing-values-dataframe.png)

Une méthode beaucoup plus utile pour évaluer les données manquantes dans ce jeu de données est de créer une visualisation rapide. Pour ce faire, nous pouvons utiliser la bibliothèque de visualisation `seaborn`. Voici une commande rapide que vous pouvez utiliser pour créer une `heatmap` en utilisant la bibliothèque `seaborn` :

```

sns.heatmap(titanic_data.isnull(), cbar=False)


```

Voici la visualisation que cela génère :

![Un DataFrame de valeurs booléennes indiquant où les données nulles existent](https://nickmccullum.com/images/python-machine-learning/logistic-regression/missing-values-heatmap.png)

Dans cette visualisation, les lignes blanches indiquent les valeurs manquantes dans le jeu de données. Vous pouvez voir que les colonnes `Age` et `Cabin` contiennent la majorité des données manquantes dans le jeu de données Titanic.

La colonne `Age` en particulier contient une quantité suffisamment faible de données manquantes pour que nous puissions remplir les données manquantes en utilisant une forme de mathématiques. D'autre part, les données `Cabin` manquent suffisamment de données pour que nous puissions probablement les supprimer entièrement de notre modèle.

Le processus de remplissage des données manquantes avec des données moyennes du reste du jeu de données s'appelle `imputation`. Nous allons maintenant utiliser `imputation` pour remplir les données manquantes de la colonne `Age`.

La forme la plus basique de `imputation` serait de remplir les données `Age` manquantes avec la valeur moyenne `Age` sur l'ensemble du jeu de données. Cependant, il existe de meilleures méthodes.

Nous allons remplir les valeurs `Age` manquantes avec la valeur moyenne `Age` pour la classe spécifique `Pclass` à laquelle appartient le passager. Pour comprendre pourquoi cela est utile, considérons le boxplot suivant :

```

sns.boxplot(titanic_data['Pclass'], titanic_data['Age'])


```

![Un boxplot des valeurs d'âge stratifiées par classes de passagers](https://nickmccullum.com/images/python-machine-learning/logistic-regression/age-boxplot.png)

Comme vous pouvez le voir, les passagers avec une valeur `Pclass` de `1` (la classe de passagers la plus chère) tendent à être les plus âgés tandis que les passagers avec une valeur `Pclass` de `3` (la moins chère) tendent à être les plus jeunes. Cela est très logique, donc nous utiliserons la valeur moyenne `Age` au sein des différentes données `Pclass` pour `imputer` les données manquantes dans notre colonne `Age`.

Le moyen le plus simple de réaliser une `imputation` sur un jeu de données comme le jeu de données Titanic est de construire une fonction personnalisée. Pour commencer, nous devrons déterminer la valeur moyenne `Age` pour chaque valeur `Pclass`.

```

#Valeur Pclass 1

titanic_data[titanic_data['Pclass'] == 1]['Age'].mean()

#Valeur Pclass 2

titanic_data[titanic_data['Pclass'] == 2]['Age'].mean()

#Pclass 3

titanic_data[titanic_data['Pclass'] == 2]['Age'].mean()


```

Voici la fonction finale que nous utiliserons pour `imputer` nos variables `Age` manquantes :

```

def impute_missing_age(columns):

    age = columns[0]

    passenger_class = columns[1]

    

    if pd.isnull(age):

        if(passenger_class == 1):

            return titanic_data[titanic_data['Pclass'] == 1]['Age'].mean()

        elif(passenger_class == 2):

            return titanic_data[titanic_data['Pclass'] == 2]['Age'].mean()

        elif(passenger_class == 3):

            return titanic_data[titanic_data['Pclass'] == 3]['Age'].mean()

        

    else:

        return age


```

Maintenant que cette fonction d'imputation est complète, nous devons l'appliquer à chaque ligne du DataFrame `titanic_data`. La méthode `apply` de Python est un excellent outil pour cela :

```

titanic_data['Age'] = titanic_data[['Age', 'Pclass']].apply(impute_missing_age, axis = 1)


```

Maintenant que nous avons effectué une `imputation` sur chaque ligne pour traiter nos données `Age` manquantes, examinons notre boxplot original :

```

sns.heatmap(titanic_data.isnull(), cbar=False)


```

Vous remarquerez qu'il n'y a plus de données manquantes dans la colonne `Age` de notre DataFrame pandas !

Vous vous demandez peut-être pourquoi nous avons passé autant de temps à traiter les données manquantes dans la colonne `Age` spécifiquement. C'est parce que, étant donné l'impact de l'`Age` sur la survie pour la plupart des catastrophes et des maladies, il s'agit d'une variable susceptible d'avoir une valeur prédictive élevée dans notre jeu de données.

Maintenant que nous avons une compréhension de la structure de ce jeu de données et que nous avons supprimé ses données manquantes, commençons à construire notre modèle d'apprentissage automatique de régression logistique.

### Construction d'un modèle de régression logistique

Il est maintenant temps de supprimer notre modèle de régression logistique.

### **Suppression des colonnes avec trop de données manquantes**

Tout d'abord, supprimons la colonne `Cabin`. Comme nous l'avons mentionné, la forte prévalence de données manquantes dans cette colonne signifie qu'il est imprudent d'`imputer` les données manquantes, donc nous la supprimerons entièrement avec le code suivant :

```

titanic_data.drop('Cabin', axis=1, inplace = True)


```

Ensuite, supprimons les colonnes supplémentaires contenant des données manquantes avec la méthode `dropna()` de pandas :

```

titanic_data.dropna(inplace = True)


```

### **Traitement des données catégorielles avec des variables factices**

La prochaine tâche que nous devons gérer est le traitement des caractéristiques catégorielles. Plus précisément, nous devons trouver un moyen de travailler numériquement avec des observations qui ne sont pas naturellement numériques.

Un excellent exemple de cela est la colonne `Sex`, qui a deux valeurs : `Male` et `Female`. De même, la colonne `Embarked` contient une seule lettre qui indique la ville de départ du passager.

Pour résoudre ce problème, nous créerons des `variables factices`. Celles-ci attribuent une valeur numérique à chaque catégorie d'une caractéristique non numérique.

Heureusement, `pandas` dispose d'une méthode intégrée appelée `get_dummies()` qui facilite la création de variables factices. La méthode `get_dummies` a un problème - elle créera une nouvelle colonne pour chaque valeur dans la colonne du DataFrame.

Considérons un exemple pour mieux comprendre cela. Si nous appelons la méthode `get_dummies()` sur la colonne `Age`, nous obtenons la sortie suivante :

```

pd.get_dummies(titanic_data['Sex'])


```

![Un exemple de la méthode get_dummies de pandas](https://nickmccullum.com/images/python-machine-learning/logistic-regression/get-dummies.png)

Comme vous pouvez le voir, cela crée deux nouvelles colonnes : `female` et `male`. Ces colonnes seront toutes deux des prédicteurs parfaits l'une de l'autre, puisque une valeur de `0` dans la colonne `female` indique une valeur de `1` dans la colonne `male`, et vice versa.

Cela s'appelle la `multicolinéarité` et elle réduit considérablement le pouvoir prédictif de votre algorithme. Pour supprimer cela, nous pouvons ajouter l'argument `drop_first = True` à la méthode `get_dummies` comme ceci :

```

pd.get_dummies(titanic_data['Sex'], drop_first = True)


```

Maintenant, créons des colonnes de variables factices pour nos colonnes `Sex` et `Embarked`, et assignons-les à des variables appelées `sex` et `embarked`.

```

sex_data = pd.get_dummies(titanic_data['Sex'], drop_first = True)

embarked_data = pd.get_dummies(titanic_data['Embarked'], drop_first = True)


```

Il y a une chose importante à noter concernant la variable `embarked` définie ci-dessous. Elle a deux colonnes : `Q` et `S`, mais puisque nous avons déjà supprimé une autre colonne (la colonne `C`), aucune des deux colonnes restantes n'est un prédicteur parfait de l'autre, donc la `multicolinéarité` n'existe pas dans le nouveau jeu de données modifié.

### **Ajout de variables factices au DataFrame `pandas`**

Ensuite, nous devons ajouter nos colonnes `sex` et `embarked` au DataFrame.

Vous pouvez [concaténer](https://nickmccullum.com/advanced-python/how-to-concatenate-pandas-dataframes/) ces colonnes de données dans le DataFrame `pandas` existant avec le code suivant :

```

titanic_data = pd.concat([titanic_data, sex_data, embarked_data], axis = 1)


```

Maintenant, si vous exécutez la commande `print(titanic_data.columns)`, votre Jupyter Notebook générera la sortie suivante :

```

Index(['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',

       'Parch', 'Ticket', 'Fare', 'Embarked', 'male', 'Q', 'S'],

      dtype='object')


```

L'existence des colonnes `male`, `Q` et `S` montre que nos données ont été concaténées avec succès.

### Suppression des colonnes inutiles du jeu de données

Cela signifie que nous pouvons maintenant supprimer les colonnes `Sex` et `Embarked` originales du DataFrame. Il y a également d'autres colonnes (comme `Name`, `PassengerId`, `Ticket`) qui ne sont pas prédictives des taux de survie au naufrage du Titanic, donc nous les supprimerons également. Le code suivant gère cela pour nous :

```

titanic_data.drop(['Name', 'Ticket', 'Sex', 'Embarked'], axis = 1, inplace = True)


```

Si vous imprimez `titanic_data.columns` maintenant, votre Jupyter Notebook générera la sortie suivante :

```

Index(['Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare',

       'male', 'Q', 'S'],

      dtype='object'


```

Le DataFrame a maintenant l'apparence suivante :

![Le DataFrame final pour notre modèle de régression logistique](https://nickmccullum.com/images/python-machine-learning/logistic-regression/final-data-frame.png)

Comme vous pouvez le voir, chaque champ de ce jeu de données est maintenant numérique, ce qui en fait un excellent candidat pour un algorithme d'apprentissage automatique de régression logistique.

### Création de données d'entraînement et de données de test

Ensuite, il est temps de diviser notre `titanic_data` en données d'entraînement et données de test. Comme précédemment, nous utiliserons la fonctionnalité intégrée de `scikit-learn` pour cela.

Tout d'abord, nous devons diviser nos données en valeurs `x` (les données que nous utiliserons pour faire des prédictions) et valeurs `y` (les données que nous essayons de prédire). Le code suivant gère cela :

```

y_data = titanic_data['Survived']

x_data = titanic_data.drop('Survived', axis = 1)


```

Ensuite, nous devons importer la fonction `train_test_split` de `scikit-learn`. Le code suivant exécute cette importation :

```

from sklearn.model_selection import train_test_split


```

Enfin, nous pouvons utiliser la fonction `train_test_split` combinée avec le déballage de liste pour générer nos données d'entraînement et de test :

```

x_training_data, x_test_data, y_training_data, y_test_data = train_test_split(x_data, y_data, test_size = 0.3)


```

Notez que dans ce cas, les données de test représentent 30 % du jeu de données original comme spécifié avec le paramètre `test_size = 0.3`.

Nous avons maintenant créé nos données d'entraînement et de test pour notre modèle de régression logistique. Nous entraînerons notre modèle dans la section suivante de ce tutoriel.

### Entraînement du modèle de régression logistique

Pour entraîner notre modèle, nous devrons d'abord importer le modèle approprié de `scikit-learn` avec la commande suivante :

```

from sklearn.linear_model import LogisticRegression


```

Ensuite, nous devons créer notre modèle en instanciant une instance de l'objet `LogisticRegression` :

```

model = LogisticRegression()


```

Pour entraîner le modèle, nous devons appeler la méthode `fit` sur l'objet `LogisticRegression` que nous venons de créer et passer nos variables `x_training_data` et `y_training_data`, comme ceci :

```

model.fit(x_training_data, y_training_data)


```

Notre modèle a maintenant été entraîné. Nous commencerons à faire des prédictions en utilisant ce modèle dans la section suivante de ce tutoriel.

### Faire des prédictions avec notre modèle de régression logistique

Faisons un ensemble de prédictions sur nos données de test en utilisant le modèle de régression logistique `model` que nous venons de créer. Nous stockerons ces prédictions dans une variable appelée `predictions` :

```

predictions = model.predict(x_test_data)


```

Nos prédictions ont été faites. Examinons la précision de notre modèle ensuite.

### Mesure de la performance d'un modèle d'apprentissage automatique de régression logistique

`scikit-learn` dispose d'un excellent module intégré appelé `classification_report` qui facilite la mesure de la performance d'un modèle d'apprentissage automatique de classification. Nous utiliserons ce module pour mesurer la performance du modèle que nous venons de créer.

Tout d'abord, importons le module :

```

from sklearn.metrics import classification_report


```

Ensuite, utilisons le module pour calculer les métriques de performance pour notre module d'apprentissage automatique de régression logistique :

```

classification_report(y_test_data, predictions)


```

Voici la sortie de cette commande :

```

             precision    recall  f1-score   support

           0       0.83      0.87      0.85       169

           1       0.75      0.68      0.72        98

    accuracy                           0.80       267

   macro avg       0.79      0.78      0.78       267

weighted avg       0.80      0.80      0.80       267


```

Si vous êtes intéressé à voir la matrice de confusion brute et à calculer les métriques de performance manuellement, vous pouvez le faire avec le code suivant :

```

from sklearn.metrics import confusion_matrix

print(confusion_matrix(y_test_data, predictions))


```

Cela génère la sortie suivante :

```

[[145  22]

 [ 30  70]]


```

### Le code complet pour ce tutoriel

Vous pouvez consulter le code complet pour ce tutoriel dans [ce dépôt GitHub](https://github.com/nicholasmccullum/python-machine-learning). Il est également collé ci-dessous pour votre référence :

```

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

%matplotlib inline

import seaborn as sns

#Import the data set

titanic_data = pd.read_csv('titanic_train.csv')

#Exploratory data analysis

sns.heatmap(titanic_data.isnull(), cbar=False)

sns.countplot(x='Survived', data=titanic_data)

sns.countplot(x='Survived', hue='Sex', data=titanic_data)

sns.countplot(x='Survived', hue='Pclass', data=titanic_data)

plt.hist(titanic_data['Age'].dropna())

plt.hist(titanic_data['Fare'])

sns.boxplot(titanic_data['Pclass'], titanic_data['Age'])

#Imputation function

def impute_missing_age(columns):

    age = columns[0]

    passenger_class = columns[1]

    

    if pd.isnull(age):

        if(passenger_class == 1):

            return titanic_data[titanic_data['Pclass'] == 1]['Age'].mean()

        elif(passenger_class == 2):

            return titanic_data[titanic_data['Pclass'] == 2]['Age'].mean()

        elif(passenger_class == 3):

            return titanic_data[titanic_data['Pclass'] == 3]['Age'].mean()

        

    else:

        return age

#Impute the missing Age data

titanic_data['Age'] = titanic_data[['Age', 'Pclass']].apply(impute_missing_age, axis = 1)

#Reinvestigate missing data

sns.heatmap(titanic_data.isnull(), cbar=False)

#Drop null data

titanic_data.drop('Cabin', axis=1, inplace = True)

titanic_data.dropna(inplace = True)

#Create dummy variables for Sex and Embarked columns

sex_data = pd.get_dummies(titanic_data['Sex'], drop_first = True)

embarked_data = pd.get_dummies(titanic_data['Embarked'], drop_first = True)

#Add dummy variables to the DataFrame and drop non-numeric data

titanic_data = pd.concat([titanic_data, sex_data, embarked_data], axis = 1)

titanic_data.drop(['Name', 'PassengerId', 'Ticket', 'Sex', 'Embarked'], axis = 1, inplace = True)

#Print the finalized data set

titanic_data.head()

#Split the data set into x and y data

y_data = titanic_data['Survived']

x_data = titanic_data.drop('Survived', axis = 1)

#Split the data set into training data and test data

from sklearn.model_selection import train_test_split

x_training_data, x_test_data, y_training_data, y_test_data = train_test_split(x_data, y_data, test_size = 0.3)

#Create the model

from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

#Train the model and create predictions

model.fit(x_training_data, y_training_data)

predictions = model.predict(x_test_data)

#Calculate performance metrics

from sklearn.metrics import classification_report

print(classification_report(y_test_data, predictions))

#Generate a confusion matrix

from sklearn.metrics import confusion_matrix

print(confusion_matrix(y_test_data, predictions))


```

### Réflexions finales

Dans ce tutoriel, vous avez appris à construire des modèles d'apprentissage automatique de régression linéaire et logistique en Python.

Si vous êtes intéressé à en apprendre davantage sur la construction, l'entraînement et le déploiement de modèles d'apprentissage automatique de pointe, mon eBook [Pragmatic Machine Learning](https://gumroad.com/l/pGjwd) vous apprendra à construire 9 modèles d'apprentissage automatique différents en utilisant des projets du monde réel.

Vous pouvez déployer le code de l'eBook sur votre GitHub ou portfolio personnel pour le montrer à des employeurs potentiels. Le livre sera lancé le 3 août - [précommandez-le maintenant avec 50% de réduction](https://gumroad.com/l/pGjwd) !

Voici un bref résumé de ce que vous avez appris dans cet article :

* Comment importer les bibliothèques requises pour construire un algorithme d'apprentissage automatique de régression linéaire
* Comment diviser un jeu de données en données d'entraînement et données de test en utilisant `scikit-learn`
* Comment utiliser `scikit-learn` pour entraîner un modèle de régression linéaire et faire des prédictions en utilisant ce modèle
* Comment calculer les métriques de performance de régression linéaire en utilisant `scikit-learn`
* Pourquoi le jeu de données Titanic est souvent utilisé pour apprendre les techniques de classification en apprentissage automatique
* Comment effectuer une analyse exploratoire des données lors du travail avec un jeu de données pour des problèmes d'apprentissage automatique de classification
* Comment gérer les données manquantes dans un DataFrame pandas
* Ce que signifie `imputation` et comment vous pouvez l'utiliser pour remplir les données manquantes
* Comment créer des variables factices pour les données catégorielles dans les jeux de données d'apprentissage automatique
* Comment entraîner un modèle d'apprentissage automatique de régression logistique en Python
* Comment faire des prédictions en utilisant un modèle de régression logistique en Python
* Comment utiliser le `classification_report` de `scikit-learn` pour calculer rapidement les métriques de performance pour les problèmes de classification en apprentissage automatique