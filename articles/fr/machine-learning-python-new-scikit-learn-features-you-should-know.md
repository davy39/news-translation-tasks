---
title: "Machine Learning en Python \x13 Les meilleures nouvelles fonctionnalités de\
  \ Scikit-Learn 0.24 que vous devez connaître"
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-06-04T20:58:07.000Z'
originalURL: https://freecodecamp.org/news/machine-learning-python-new-scikit-learn-features-you-should-know
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/1_osadNSUIUZkwDqBC-ozxtg.jpeg
tags:
- name: Machine Learning
  slug: machine-learning
- name: Python
  slug: python
- name: scikit learn
  slug: scikit-learn
seo_title: "Machine Learning en Python \x13 Les meilleures nouvelles fonctionnalités\
  \ de Scikit-Learn 0.24 que vous devez connaître"
seo_desc: "By Davis David\nScikit-learn is one of the most popular open-source and\
  \ free machine learning libraries for Python. \nThe scikit-learn library contains\
  \ a lot of efficient tools for machine learning and statistical modeling including\
  \ classification, reg..."
---

Par Davis David

Scikit-learn est l'une des bibliothèques d'apprentissage automatique open-source et gratuites les plus populaires pour Python. 

La bibliothèque scikit-learn contient de nombreux outils efficaces pour l'apprentissage automatique et la modélisation statistique, y compris la classification, la régression, le clustering et la réduction de dimension.

De nombreux data scientists, ingénieurs en apprentissage automatique et chercheurs s'appuient sur cette bibliothèque pour leurs projets d'[apprentissage automatique](https://hackernoon.com/machine-learning-as-a-service-mlaas-with-sklearn-and-algorithmia-7299fbaed584?ref=hackernoon.com). Personnellement, j'adore utiliser la bibliothèque scikit-learn car elle offre une grande flexibilité et il est facile de comprendre sa documentation avec de nombreux exemples.

Dans cet article, je suis heureux de partager avec vous les cinq meilleures nouvelles fonctionnalités de scikit-learn 0.24.

### Tout d'abord, installez la dernière version de la bibliothèque Scikit-Learn

Tout d'abord, assurez-vous d'installer la dernière version (avec pip) :

```
pip install --upgrade scikit-learn
```

Si vous utilisez conda, utilisez la commande suivante :

```
conda install -c conda-forge scikit-learn
```

**Note :** Cette version supporte les versions Python **3.6** à **3.9**.

Maintenant, regardons les nouvelles fonctionnalités !

## Erreur de Pourcentage Absolue Moyenne (MAPE)

La nouvelle version de scikit-learn introduit une nouvelle métrique d'évaluation pour un problème de régression appelée Erreur de Pourcentage Absolue Moyenne (MAPE). Auparavant, vous pouviez calculer la MAPE en utilisant un morceau de code.

```python
np.mean(np.abs((y_test  preds)/y_test))
```

Mais maintenant, vous pouvez appeler une fonction appelée **mean_absolute_percentage_error** du module **sklearn.metrics** pour évaluer la performance de votre modèle de régression.

**Exemple :**

```python
from sklearn.metrics import mean_absolute_percentage_error
y_true = [3, -0.5, 2, 7]
y_pred = [2.5, 0.0, 2, 8]

print(mean_absolute_percentage_error(y_true, y_pred))
```

0.3273809523809524

**Note :** Gardez à l'esprit que la fonction ne représente pas la sortie sous forme de pourcentage dans la plage [0, 100]. Au lieu de cela, nous la représentons dans la plage [0, 1/eps]. La meilleure valeur est **0.0.**

## OneHotEncoder Supporte les Valeurs Manquantes

[OneHotEncoder](https://hackernoon.com/what-is-one-hot-encoding-why-and-when-do-you-have-to-use-it-e3c6186d008f?ref=hackernoon.com) peut maintenant gérer les valeurs manquantes si elles sont présentes dans le jeu de données. Il traite une valeur manquante comme une catégorie. Comprenons mieux comment cela fonctionne dans l'exemple suivant.

Tout d'abord, importez les packages importants :

```python
import pandas as pd 
import numpy as np
from sklearn.preprocessing import OneHotEncoder
```

Créez un simple data-frame avec une caractéristique catégorielle qui a des valeurs manquantes :

```python
# initialise les données des listes.
data = {'education_level':['primary', 'secondary', 'bachelor', np.nan,'masters',np.nan]}
  
# Créez le DataFrame
df = pd.DataFrame(data)
  
# Affichez la sortie.
print(df)
```

![Image](https://www.freecodecamp.org/news/content/images/2021/06/zVaxL0LohRUpfDQhznRQ9z3y5tj1-1f9314q.jpeg)

Comme vous pouvez le voir, nous avons deux valeurs manquantes dans notre colonne **education_level**.

Créez l'instance de OneHotEncoder :

```python
enc = OneHotEncoder()
```

Ensuite, adaptez et transformez nos données :

```python
enc.fit_transform(df).toarray()
```

![Image](https://www.freecodecamp.org/news/content/images/2021/06/zVaxL0LohRUpfDQhznRQ9z3y5tj1-pn3531g0.jpeg)

Notre colonne education_level a été transformée et toutes les valeurs manquantes traitées comme une nouvelle catégorie (vérifiez la dernière colonne du tableau ci-dessus).

## Nouvelle Méthode pour la Sélection de Caractéristiques

**SequentialFeatureSelector** est une nouvelle méthode pour la sélection de caractéristiques dans scikit-learn. Elle peut être soit une sélection progressive, soit une sélection rétrograde.

### Sélection Progressive

La Sélection Progressive trouve itérativement la meilleure nouvelle caractéristique et l'ajoute ensuite à l'ensemble des caractéristiques sélectionnées. 

Cela signifie que nous commençons avec zéro caractéristique, puis trouvons une caractéristique qui maximise le score de validation croisée d'un estimateur. La caractéristique sélectionnée est ajoutée à l'ensemble et la procédure est répétée jusqu'à ce que nous atteignions le nombre souhaité de caractéristiques sélectionnées.

### Sélection Rétrograde

Cette deuxième sélection suit la même idée mais dans une direction différente. Ici, nous commençons avec toutes les caractéristiques, puis retirons une caractéristique de l'ensemble jusqu'à ce que nous atteignions le nombre souhaité de caractéristiques sélectionnées.

#### Exemple

Importez les packages importants :

```python
from sklearn.feature_selection import SequentialFeatureSelector
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
```

Chargez le jeu de données iris et ses noms de caractéristiques :

```python
X, y = load_iris(return_X_y=True, as_frame=True)
feature_names = X.columns
```

Créez l'instance de l'estimateur :

```python
knn = KNeighborsClassifier(n_neighbors=3)
```

Créez l'instance de SequentialFeatureSelector, définissez le nombre de caractéristiques à sélectionner à **2**, et définissez la direction à "**backward**" :

```python
sfs = SequentialFeatureSelector(knn, n_features_to_select=2,direction='backward')
```

Enfin, apprenez les caractéristiques à sélectionner :

```python
sfs.fit(X,y)
```

Montrez les caractéristiques sélectionnées :

```python
print("Caractéristiques sélectionnées par sélection séquentielle rétrograde : "f{feature_names[sfs.get_support()].tolist()}")
```

Caractéristiques sélectionnées par sélection séquentielle rétrograde : [petal length (cm), petal width (cm)].

Le seul inconvénient de cette nouvelle méthode de sélection de caractéristiques est qu'elle peut être plus lente que d'autres méthodes que vous connaissez déjà (SelectFromModel & RFE) car elle évalue les modèles avec validation croisée.

## Nouvelles Méthodes pour l'Ajustement des Hyper-Paramètres

En matière d'ajustement des hyper-paramètres, GridSearchCV et RandomizedSearchCv de Scikit-learn ont été le premier choix pour de nombreux data scientists. 

Mais dans la nouvelle version, nous avons deux nouvelles classes pour l'ajustement des hyper-paramètres appelées **HalvingGridSearchCV** et **HalvingRandomSearchCV**.

HalvingGridSearchCV et HalvingRandomSearchCV utilisent une nouvelle approche appelée **successive halving** pour trouver les meilleurs hyperparamètres. Le successive halving est comme une compétition ou un tournoi parmi toutes les combinaisons d'hyperparamètres.

### Comment fonctionne le successive halving ?

Dans la première itération, ils entraînent une combinaison d'hyper-paramètres sur un sous-ensemble d'observations (données d'entraînement). 

Ensuite, dans l'itération suivante, il sélectionne uniquement une combinaison d'hyper-paramètres qui ont de bonnes performances dans la première itération et ils seront entraînés sur un grand nombre d'observations pour concourir.

Ainsi, il répète ce processus de sélection à chaque itération jusqu'à ce qu'il sélectionne la meilleure combinaison d'hyperparamètres dans l'itération finale.

**Note :** Ces classes sont encore expérimentales :

#### Exemple :

Importez les packages importants :

```python
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.experimental import enable_halving_search_cv  
from sklearn.model_selection import HalvingRandomSearchCV
from scipy.stats import randint
```

Puisque ces nouvelles classes sont encore expérimentales, pour les utiliser, nous importons explicitement **enable_halving_search_cv**.

Créez un jeu de données de classification en utilisant la méthode make_classification :

```python
X, y = make_classification(n_samples=1000)
```

Créez l'instance de l'estimateur. Ici, nous utilisons un Random Forest Classifier :

```python
clf = RandomForestClassifier(n_estimators=20)
```

Créez une distribution de paramètres pour l'ajustement :

```python
param_dist = {"max_depth": [3, None],
              "max_features": randint(1, 11),
              "min_samples_split": randint(2, 11),
              "bootstrap": [True, False],
              "criterion": ["gini", "entropy"]}
```

Ensuite, nous instancions la classe HalvingGridSearchCV avec le RandomForestClassifier comme estimateur et la liste des distributions de paramètres :

```python
rsh = HalvingRandomSearchCV(
    estimator=clf,
    param_distributions=param_dist,
    cv = 5,
    factor=2,
    min_resources = 20)
```

Il y a deux paramètres importants dans HalvingRandomSearchCV que vous devez connaître.

1. **factor**  Cela détermine la proportion de la combinaison d'hyper-paramètres qui sont sélectionnés pour chaque itération suivante. Par exemple, **_factor=3_** signifie que seulement un tiers des candidats sont sélectionnés pour l'itération suivante.
2. **min_resources** est la quantité de ressources (nombre d'observations) allouées à la première itération pour chaque combinaison d'hyper-paramètres.

Enfin, nous pouvons ajuster l'objet de recherche que nous avons créé avec notre jeu de données.

```python
rsh.fit(X,y)
```

Après l'entraînement, nous pouvons voir différentes sorties telles que :

Le nombre d'itérations

```python
print(rsh.n_iterations_ )
```

qui est 6.

Ou le nombre de paramètres candidats qui ont été évalués à chaque itération

```python
print(rsh.n_candidates_ )
```

qui est **[50, 25, 13, 7, 4, 2]**.

Ou le nombre de ressources utilisées à chaque itération :

```python
print(rsh.n_resources_)
```

qui est **[20, 40, 80, 160, 320, 640]**.

Ou le paramètre qui a donné les meilleurs résultats sur les données de validation :

```python
print(rsh.best_params_)
```

**{bootstrap: False,**  
**criterion: entropy,**  
**max_depth: None,**  
**max_features: 5,**  
**min_samples_split: 2}**

## Nouveau méta-estimateur d'auto-apprentissage pour l'apprentissage semi-supervisé

Scikit-learn 0.24 a introduit une nouvelle implémentation d'auto-apprentissage pour l'apprentissage semi-supervisé appelée **SelfTrainingclassifier**. Vous pouvez utiliser SelfTrainingClassifier avec n'importe quel classificateur supervisé qui peut retourner des estimations de probabilité pour chaque classe.

Cela signifie que n'importe quel classificateur supervisé peut fonctionner comme un classificateur semi-supervisé, lui permettant d'apprendre à partir d'observations non étiquetées dans le jeu de données.

**Note :** Les valeurs non étiquetées dans la colonne cible doivent avoir une valeur de -1.

Comprenons mieux comment cela fonctionne dans l'exemple suivant.

Importez les packages importants :

```python
import numpy as np
from sklearn import datasets
from sklearn.semi_supervised import SelfTrainingClassifier
from sklearn.svm import SVC
```

Dans cet exemple, nous utiliserons le jeu de données iris et l'algorithme de machine à vecteurs de support comme classificateur supervisé (il peut implémenter **fit** et **predict_proba**).

Ensuite, nous chargeons le jeu de données et sélectionnons aléatoirement certaines des observations pour qu'elles soient non étiquetées :

```python
rng = np.random.RandomState(42)
iris = datasets.load_iris()
random_unlabeled_points = rng.rand(iris.target.shape[0]) < 0.3
iris.target[random_unlabeled_points] = -1
```

Comme vous pouvez le voir, les valeurs non étiquetées dans la colonne cible ont une valeur de -1.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/zVaxL0LohRUpfDQhznRQ9z3y5tj1-jcah31ok.jpeg)

Créez une instance de l'estimateur supervisé :

```python
svc = SVC(probability=True, gamma="auto")
```

Créez une instance du méta-estimateur d'auto-apprentissage et ajoutez svc comme base_estimator :

```python
self_training_model = SelfTrainingClassifier(base_estimator=svc)
```

Enfin, nous pouvons entraîner self_traning_model sur le jeu de données iris qui a certaines observations non étiquetées :

```python
self_training_model.fit(iris.data, iris.target)
```

SelfTrainingClassifier(base_estimator=SVC(gamma=auto, probability=True))

## Réflexions Finales sur Scikit-Learn 0.24

Comme je l'ai dit, scikit-learn reste l'une des bibliothèques d'apprentissage automatique open-source les plus populaires. Et elle possède toutes les [fonctionnalités](https://towardsdatascience.com/14-lesser-known-impressive-features-of-scikit-learn-library-e7ea36f1149a?ref=hackernoon.com) dont vous avez besoin pour construire un projet d'apprentissage automatique de bout en bout. 

Vous pouvez également implémenter les nouvelles fonctionnalités impressionnantes présentées dans cet article dans votre projet d'apprentissage automatique.

Vous pouvez trouver les points forts des autres fonctionnalités publiées dans scikit-learn 0.24 [ici](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_24_0.html?ref=hackernoon.com).

Félicitations , vous êtes arrivé à la fin de cet article ! J'espère que vous avez appris quelque chose de nouveau qui vous aidera dans votre prochain projet d'apprentissage automatique ou de data science.

Si vous avez appris quelque chose de nouveau ou apprécié la lecture de cet article, veuillez le partager afin que d'autres puissent le voir. En attendant, à la prochaine publication !

Vous pouvez également me trouver sur Twitter [@Davis_McDavid.](https://twitter.com/Davis_McDavid?ref=hackernoon.com)

Vous pouvez lire [d'autres articles](https://hackernoon.com/u/davisdavid) ici_._