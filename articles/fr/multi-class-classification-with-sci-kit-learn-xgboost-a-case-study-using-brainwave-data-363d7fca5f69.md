---
title: 'Classification multi-classes avec Sci-kit learn & XGBoost : Une étude de cas
  utilisant des données d''ondes cérébrales'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-09T15:47:11.000Z'
originalURL: https://freecodecamp.org/news/multi-class-classification-with-sci-kit-learn-xgboost-a-case-study-using-brainwave-data-363d7fca5f69
coverImage: https://cdn-media-1.freecodecamp.org/images/1*IKujbs0wj3bls1EiaXa2nw.jpeg
tags:
- name: coding
  slug: coding
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: 'Classification multi-classes avec Sci-kit learn & XGBoost : Une étude
  de cas utilisant des données d''ondes cérébrales'
seo_desc: 'By Avishek Nag (Machine Learning expert)

  A comparison of different classifiers’ accuracy & performance for high-dimensional
  data


  Photo Credit : Pixabay

  In Machine learning, classification problems with high-dimensional data are really
  challenging. S...'
---

Par Avishek Nag (expert en Machine Learning)

#### Une comparaison de la précision et des performances de différents classificateurs pour des données de haute dimension

![Image](https://cdn-media-1.freecodecamp.org/images/HgrQEY1ls7wmdrV8KRTkFHOm8qhwMARrADSp)
_Crédit Photo : Pixabay_

En apprentissage automatique, les problèmes de classification avec des données de haute dimension sont vraiment difficiles. Parfois, des problèmes très simples deviennent extrêmement complexes en raison de ce problème de "malédiction de la dimensionnalité".

Dans cet article, nous verrons comment la précision et les performances varient selon les différents classificateurs. Nous verrons également comment, lorsque nous n'avons pas la liberté de choisir un classificateur indépendamment, nous pouvons faire de l'ingénierie des caractéristiques pour faire en sorte qu'un classificateur médiocre performe bien.

### **Comprendre la "source de données" et la formulation du problème**

Pour cet article, nous utiliserons le "Jeu de données d'ondes cérébrales EEG" de [Kaggle](https://www.kaggle.com/birdy654/eeg-brainwave-dataset-feeling-emotions). Ce jeu de données contient des signaux électroniques d'ondes cérébrales provenant d'un casque EEG et est au format temporel. Au moment de la rédaction de cet article, personne n'a créé de "Kernel" sur ce jeu de données — c'est-à-dire que, pour l'instant, aucune solution n'a été donnée sur Kaggle.

Alors, pour commencer, lisons d'abord les données pour voir ce qu'il y a.

![Image](https://cdn-media-1.freecodecamp.org/images/AzxLbSZrXH13JT0xCsCVNlveCIPB5UAH6EjI)

Il y a 2549 colonnes dans le jeu de données et "label" est la colonne cible pour notre problème de classification. Toutes les autres colonnes comme "mean_d_1_a", "mean_d2_a", etc., décrivent les caractéristiques des lectures des signaux d'ondes cérébrales. Les colonnes commençant par le préfixe "fft" sont probablement des "transformées de Fourier rapides" des signaux originaux. Notre colonne cible "label" décrit le degré de sentiment émotionnel.

Selon Kaggle, voici le défi : "Pouvons-nous prédire le sentiment émotionnel à partir des lectures d'ondes cérébrales ?"

Commençons par comprendre les distributions de classes à partir de la colonne "label" :

![Image](https://cdn-media-1.freecodecamp.org/images/oPF55uAVtTkqcK-RkZ7RaNC9BvlXBHxW0giG)
_Fig 1_

Donc, il y a trois classes, "POSITIVE", "NEGATIVE" et "NEUTRAL", pour le sentiment émotionnel. D'après le diagramme à barres, il est clair que la distribution des classes n'est pas biaisée et qu'il s'agit d'un problème de "classification multi-classes" avec la variable cible "label". Nous essaierons différents classificateurs et verrons les niveaux de précision.

Avant d'appliquer un classificateur, la colonne "label" doit être séparée des autres colonnes de caractéristiques ("mean_d_1_a", "mean_d2_a", etc., sont des caractéristiques).

```
label_df = brainwave_df['label']brainwave_df.drop('label', axis = 1, inplace=True)brainwave_df.head()
```

Comme il s'agit d'un problème de "classification", nous suivrons les conventions suivantes pour chaque "classificateur" à essayer :

1. Nous utiliserons une approche de "validation croisée" (dans notre cas, nous utiliserons une validation croisée à 10 plis) sur le jeu de données et prendrons la précision moyenne. Cela nous donnera une vue holistique de la précision du classificateur.
2. Nous utiliserons une approche basée sur un "Pipeline" pour combiner toutes les étapes de prétraitement et le calcul principal du classificateur. Un "Pipeline" ML enveloppe toutes les étapes de traitement dans une seule unité et agit comme un "classificateur" lui-même. Ainsi, toutes les étapes deviennent réutilisables et peuvent être mises en forme d'autres "pipelines".
3. Nous suivrons le temps total de construction et de test pour chaque approche. Nous appellerons cela le "temps pris".

Pour ce qui précède, nous utiliserons principalement le package scikit-learn de Python. Comme le nombre de caractéristiques ici est assez élevé, nous commencerons par un classificateur qui fonctionne bien sur des données de haute dimension.

### **Classificateur RandomForest**

"RandomForest" est un classificateur d'ensemble basé sur une approche d'arbres et de bagging. Il réduira automatiquement le nombre de caractéristiques par son approche de calcul d'entropie probabiliste. Voyons cela :

![Image](https://cdn-media-1.freecodecamp.org/images/BoP9Xlm-bsN3YmKjvOLep3l5nv8WqmyWq-35)

La précision est très bonne à 97,7 % et le "temps total pris" est assez court (3,29 secondes seulement).

Pour ce classificateur, aucune étape de prétraitement comme la mise à l'échelle ou l'élimination du bruit n'est requise, car il est complètement basé sur la probabilité et n'est pas du tout affecté par les facteurs d'échelle.

### **Classificateur de régression logistique**

La "régression logistique" est un classificateur linéaire et fonctionne de la même manière que la régression linéaire.

![Image](https://cdn-media-1.freecodecamp.org/images/Xk8t927mnTLdQUzZoFFJcNeYLkIuyMJGiDpF)

Nous pouvons voir que la précision (93,19 %) est inférieure à celle de "RandomForest" et que le "temps pris" est plus élevé (2 min 7 s).

La "régression logistique" est fortement affectée par les différentes plages de valeurs des variables dépendantes, ce qui impose une "mise à l'échelle des caractéristiques". C'est pourquoi "StandardScaler" de scikit-learn a été ajouté comme étape de prétraitement. Il met automatiquement à l'échelle les caractéristiques selon une distribution gaussienne avec une moyenne nulle et une variance unitaire, et ainsi les valeurs de toutes les variables varient de -1 à +1.

La raison du temps élevé pris est la haute dimensionnalité et le temps de mise à l'échelle requis. Il y a 2549 variables dans le jeu de données et le coefficient de chacune doit être optimisé selon le processus de régression logistique. De plus, il y a une question de multi-colinéarité. Cela signifie que les variables linéairement corrélées doivent être regroupées ensemble au lieu de les considérer séparément.

La présence de multi-colinéarité affecte la précision. Donc maintenant la question devient, "Pouvons-nous réduire le nombre de variables, réduire la multi-colinéarité et améliorer le 'temps pris' ?"

#### **Analyse en composantes principales (PCA)**

La PCA peut transformer les variables originales de bas niveau en un espace de dimension supérieure et ainsi réduire le nombre de variables requises. Toutes les variables colinéaires sont regroupées ensemble. Faisons une PCA des données et voyons quelles sont les principales composantes principales (PC) :

![Image](https://cdn-media-1.freecodecamp.org/images/440KTh6c2a31AKyZrCRZaIZpshq1f903koj2)

Nous avons mappé 2549 variables à 20 composantes principales. D'après le résultat ci-dessus, il est clair que les 10 premières PC sont importantes. Le pourcentage total du ratio de variance expliquée par les 10 premières PC est d'environ 0,737 (0,36 + 0,095 + ..+ 0,012). Ou il peut être dit que les 10 premières PC expliquent 73,7 % de la variance de l'ensemble du jeu de données.

Ainsi, avec cela, nous sommes capables de réduire 2549 variables à 10 variables. C'est un changement dramatique, n'est-ce pas ? En théorie, les composantes principales sont des variables virtuelles générées à partir d'un mappage mathématique. D'un point de vue commercial, il n'est pas possible de dire quel aspect physique des données est couvert par elles. Cela signifie que, physiquement, les composantes principales n'existent pas. Mais nous pouvons facilement utiliser ces PC comme variables d'entrée quantitatives pour tout algorithme ML et obtenir de très bons résultats.

Pour la visualisation, prenons les deux premières PC et voyons comment nous pouvons distinguer les différentes classes des données en utilisant un "nuage de points".

```
plt.figure(figsize=(25,8))sns.scatterplot(x=pca_vectors[:, 0], y=pca_vectors[:, 1], hue=label_df)plt.title('Composantes principales vs Distribution des classes', fontsize=16)plt.ylabel('Composante principale 2', fontsize=16)plt.xlabel('Composante principale 1', fontsize=16)plt.xticks(rotation='vertical');
```

![Image](https://cdn-media-1.freecodecamp.org/images/Su4sA409ETB-Cyoi02WiqDgojX7Pk3E65O1-)
_Fig 2_

Dans le graphique ci-dessus, trois classes sont représentées en différentes couleurs. Donc, si nous utilisons le même classificateur de "régression logistique" avec ces deux PC, alors d'après le graphique ci-dessus, nous pouvons probablement dire que le premier classificateur séparera les cas "NEUTRAL" des deux autres cas et le second classificateur séparera les cas "POSITIVE" et "NEGATIVE" (car il y aura deux classificateurs logistiques internes pour un problème à 3 classes). Essayons et voyons la précision.

![Image](https://cdn-media-1.freecodecamp.org/images/OsXLQnznooi6fBsBnpflEDr4e2bHAXp8PWpy)

Le temps pris (3,34 s) a été réduit mais la précision (77 %) a diminué.

Maintenant, prenons toutes les 10 PC et exécutons :

![Image](https://cdn-media-1.freecodecamp.org/images/4doVxMxtTjlSaHJcxIfAItR-LwDmrmgXtH4r)

Nous voyons une amélioration de la précision (86 %) par rapport aux cas avec 2 PC avec une augmentation marginale du "temps pris".

Donc, dans les deux cas, nous avons vu une faible précision par rapport à la régression logistique normale, mais une amélioration significative du "temps pris".

La précision peut être testée davantage avec un "solver" différent et un paramètre "max_iter". Nous avons utilisé "saga" comme "solver" avec une pénalité L1 et 200 comme "max_iter". Ces valeurs peuvent être modifiées pour obtenir un effet variable sur la précision.

Bien que la "régression logistique" donne une faible précision, il existe des situations où elle peut être nécessaire, surtout avec la PCA. Dans les jeux de données avec un espace dimensionnel très grand, la PCA devient le choix évident pour les "classificateurs linéaires".

Dans certains cas, où une référence pour les applications ML est déjà définie et où seuls des choix limités de certains "classificateurs linéaires" sont disponibles, cette analyse serait utile. Il est très courant de voir de telles situations dans les grandes organisations où les normes sont déjà définies et où il n'est pas possible de les dépasser.

### **Classificateur de réseau de neurones artificiels (ANN)**

Un classificateur ANN est non linéaire avec des techniques automatiques d'ingénierie des caractéristiques et de réduction de dimension. "MLPClassifier" dans scikit-learn fonctionne comme un ANN. Mais ici aussi, une mise à l'échelle de base est requise pour les données. Voyons comment cela fonctionne :

![Image](https://cdn-media-1.freecodecamp.org/images/GvS62mSORy1dT6dRtBoGAT2kZz9CP5uLdmv4)

La précision (97,5 %) est très bonne, bien que le temps d'exécution soit élevé (5 min).

La raison du "temps pris" élevé est le temps de formation rigoureux requis pour les réseaux de neurones, et cela avec un nombre élevé de dimensions.

Il est une convention générale de commencer avec une taille de couche cachée de 50 % de la taille totale des données et les couches suivantes seront de 50 % de la précédente. Dans notre cas, elles sont (1275 = 2549 / 2, 637 = 1275 / 2). Le nombre de couches cachées peut être pris comme hyper-paramètre et peut être ajusté pour une meilleure précision. Dans notre cas, il est de 2.

### **Classificateur de machines à vecteurs de support linéaires (SVM)**

Nous allons maintenant appliquer le "SVM linéaire" sur les données et voir comment la précision évolue. Ici aussi, une mise à l'échelle est requise comme étape de prétraitement.

![Image](https://cdn-media-1.freecodecamp.org/images/r74XbN6LHPjZW6oRUWeGucV5yscNJksuwEw0)

La précision est de 96,4 %, ce qui est légèrement inférieur à "RandomForest" ou "ANN". Le "temps pris" est de 55 s, ce qui est bien mieux que "ANN".

### **Classificateur Extreme Gradient Boosting (XGBoost)**

XGBoost est un classificateur d'ensemble basé sur des arbres boostés. Comme "RandomForest", il réduira également automatiquement l'ensemble des caractéristiques. Pour cela, nous devons utiliser une bibliothèque "xgboost" séparée qui ne vient pas avec scikit-learn. Voyons comment cela fonctionne :

![Image](https://cdn-media-1.freecodecamp.org/images/2TrRyjjIFsVSIq8w6Q5uf4ByeJZzNeq8ko8Y)

La précision (99,4 %) est exceptionnellement bonne, mais le "temps pris" (15 min) est assez élevé. De nos jours, pour les problèmes compliqués, XGBoost devient un choix par défaut pour les scientifiques des données pour ses résultats précis. Il a un temps d'exécution élevé en raison de sa structure de modèle d'ensemble interne. Cependant, XGBoost performe bien sur les machines GPU.

### **Conclusion**

De tous les classificateurs, il est clair que pour la précision, "XGBoost" est le gagnant. Mais si nous prenons le "temps pris" avec la "précision", alors "RandomForest" est un choix parfait. Mais nous avons également vu comment utiliser un simple classificateur linéaire comme la "régression logistique" avec une ingénierie des caractéristiques appropriée pour obtenir une meilleure précision. Les autres classificateurs n'ont pas besoin de tant d'efforts d'ingénierie des caractéristiques.

Cela dépend des exigences, du cas d'utilisation et de l'environnement d'ingénierie des données disponible pour choisir un "classificateur" parfait.

L'ensemble du projet sur Jupyter Notebook peut être trouvé [ici](https://github.com/avisheknag17/public_ml_models/blob/master/mental_emotional_sentiment_classification/notebooks/emotion_classifier.ipynb).

#### **Références :**

[1] Documentation XGBoost — [https://xgboost.readthedocs.io/en/latest/](https://xgboost.readthedocs.io/en/latest/)

[2] Fonctionnement de RandomForest — [http://dataaspirant.com/2017/05/22/random-forest-algorithm-machine-learing/](http://dataaspirant.com/2017/05/22/random-forest-algorithm-machine-learing/)

[3] Analyse en composantes principales — [https://towardsdatascience.com/a-one-stop-shop-for-principal-component-analysis-5582fb7e0a9c](https://towardsdatascience.com/a-one-stop-shop-for-principal-component-analysis-5582fb7e0a9c)

[4] Régression logistique — [http://ufldl.stanford.edu/tutorial/supervised/LogisticRegression/](http://ufldl.stanford.edu/tutorial/supervised/LogisticRegression/)

[5] Machines à vecteurs de support — [https://towardsdatascience.com/support-vector-machine-introduction-to-machine-learning-algorithms-934a444fca47](https://towardsdatascience.com/support-vector-machine-introduction-to-machine-learning-algorithms-934a444fca47)