---
title: Comment construire votre premier réseau de neurones pour prédire les prix des
  maisons avec Keras
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-04T18:49:19.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-your-first-neural-network-to-predict-house-prices-with-keras-f8db83049159
coverImage: https://cdn-media-1.freecodecamp.org/images/1*93f3Bpwd9gZfy8xFl0mZrw.jpeg
tags:
- name: Data Science
  slug: data-science
- name: Deep Learning
  slug: deep-learning
- name: Machine Learning
  slug: machine-learning
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment construire votre premier réseau de neurones pour prédire les prix
  des maisons avec Keras
seo_desc: 'By Joseph Lee Wei En

  A step-by-step complete beginner’s guide to building your first Neural Network in
  a couple lines of code like a Deep Learning pro!

  Writing your first Neural Network can be done with merely a couple lines of code!
  In this post, we...'
---

Par Joseph Lee Wei En

#### Un guide complet pour débutants, étape par étape, pour construire votre premier réseau de neurones en quelques lignes de code comme un pro du Deep Learning !

Écrire votre premier réseau de neurones peut se faire avec seulement quelques lignes de code ! Dans cet article, nous allons explorer comment utiliser un package appelé Keras pour construire notre premier réseau de neurones afin de prédire si les prix des maisons sont au-dessus ou en dessous de la valeur médiane. En particulier, nous allons passer par le pipeline complet du Deep Learning, depuis :

* L'exploration et le traitement des données
* La construction et l'entraînement de notre réseau de neurones
* La visualisation de la perte et de la précision
* L'ajout de la régularisation à notre réseau de neurones

En seulement 20 à 30 minutes, vous aurez codé votre propre réseau de neurones comme le ferait un praticien du Deep Learning !

#### **Prérequis** :

Cet article suppose que vous avez configuré Jupyter notebook avec un environnement qui a les packages _keras_, _tensorflow_, _pandas_, _scikit-learn_ et _matplotlib_ installés. Si ce n'est pas le cas, veuillez suivre les instructions du tutoriel ci-dessous :

* [Getting Started with Python for Deep Learning and Data Science](https://medium.com/intuitive-deep-learning/getting-started-with-python-for-deep-learning-and-data-science-9ca785560bbc)

Il s'agit d'un compagnon de codage pour Intuitive Deep Learning Part 1. À ce titre, nous supposons que vous avez une certaine compréhension intuitive des réseaux de neurones et de leur fonctionnement, y compris certains détails, tels que ce qu'est le surapprentissage et les stratégies pour les résoudre. Si vous avez besoin d'un rappel, veuillez lire ces introductions intuitives :

* [Intuitive Deep Learning Part 1a: Introduction to Neural Networks](https://medium.com/intuitive-deep-learning/intuitive-deep-learning-part-1a-introduction-to-neural-networks-d7b16ebf6b99)
* [Intuitive Deep Learning Part 1b: Introduction to Neural Networks](https://medium.com/intuitive-deep-learning/intuitive-deep-learning-part-1b-introduction-to-neural-networks-8565d97ddd2d)

#### **Ressources dont vous avez besoin** :

Le jeu de données que nous utiliserons aujourd'hui est adapté des [données de la compétition Kaggle de prédiction des valeurs immobilières de Zillow](https://www.kaggle.com/c/zillow-prize-1/data). Nous avons réduit le nombre de caractéristiques d'entrée et changé la tâche en prédisant si le prix de la maison est au-dessus ou en dessous de la valeur médiane. Veuillez visiter le lien ci-dessous pour télécharger le jeu de données modifié et le placer dans le même répertoire que votre notebook. L'icône de téléchargement devrait se trouver en haut à droite.

[Télécharger le jeu de données](https://drive.google.com/file/d/1GfvKA0qznNVknghV4botnNxyH-KvODOC/view?usp=sharing)

Optionnellement, vous pouvez également télécharger un notebook Jupyter annoté qui contient tout le code couvert dans cet article : [Jupyter Notebook](https://github.com/josephlee94/intuitive-deep-learning/blob/master/Part%201:%20Predicting%20House%20Prices/Coding%20Companion%20for%20Intuitive%20Deep%20Learning%20Part%201%20Annotated.ipynb).

Notez que pour télécharger ce notebook depuis Github, vous devez aller à la [page d'accueil](https://github.com/josephlee94/intuitive-deep-learning) et télécharger le ZIP pour télécharger tous les fichiers :

![Image](https://cdn-media-1.freecodecamp.org/images/9pfWpU0Hxc3TZlbAN-OMamBoTW9XfPIhPTjy)

Et maintenant, commençons !

### Exploration et traitement des données

Avant de coder un algorithme de ML, la première chose que nous devons faire est de mettre nos données dans un format que l'algorithme pourra utiliser. En particulier, nous devons :

* Lire le fichier CSV (valeurs séparées par des virgules) et les convertir en tableaux. Les tableaux sont un format de données que notre algorithme peut traiter.
* Diviser notre jeu de données en caractéristiques d'entrée (que nous appelons x) et l'étiquette (que nous appelons y).
* Mettre à l'échelle les données (nous appelons cela la _normalisation_) afin que les caractéristiques d'entrée aient des ordres de grandeur similaires.
* Diviser notre jeu de données en ensemble d'entraînement, ensemble de validation et ensemble de test. Si vous avez besoin d'un rappel sur pourquoi nous avons besoin de ces trois ensembles de données, veuillez vous référer à [Intuitive Deep Learning Part 1b](https://medium.com/intuitive-deep-learning/intuitive-deep-learning-part-1b-introduction-to-neural-networks-8565d97ddd2d).

Alors commençons ! Dans le tutoriel [Getting Started with Python for Deep Learning and Data Science](https://medium.com/intuitive-deep-learning/getting-started-with-python-for-deep-learning-and-data-science-9ca785560bbc), vous devriez avoir téléchargé le package pandas dans votre environnement. Nous devons indiquer à notre notebook que nous allons utiliser ce package en l'important. Tapez le code suivant et appuyez sur Alt-Enter sur votre clavier :

```
import pandas as pd
```

Cela signifie simplement que si je veux me référer au code dans le package 'pandas', je le ferai avec le nom pd. Nous lisons ensuite le fichier CSV en exécutant cette ligne de code :

```py
df = pd.read_csv('housepricedata.csv')
```

Cette ligne de code signifie que nous allons lire le fichier csv 'housepricedata.csv' (qui devrait être dans le même répertoire que votre notebook) et le stocker dans la variable 'df'. Si nous voulons savoir ce qu'il y a dans df, tapez simplement df dans la boîte grise et cliquez sur Alt-Enter :

```py
df
```

Votre notebook devrait ressembler à quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/DBCNyPV19fTf7rGno46fQxOhy83IaUlP5dIS)

Ici, vous pouvez explorer les données un peu. Nous avons nos caractéristiques d'entrée dans les dix premières colonnes :

* Superficie du terrain (en pieds carrés)
* Qualité globale (échelle de 1 à 10)
* État global (échelle de 1 à 10)
* Superficie totale du sous-sol (en pieds carrés)
* Nombre de salles de bain complètes
* Nombre de salles de bain à moitié
* Nombre de chambres au-dessus du sol
* Nombre total de pièces au-dessus du sol
* Nombre de cheminées
* Superficie du garage (en pieds carrés)

Dans notre dernière colonne, nous avons la caractéristique que nous aimerions prédire :

* Le prix de la maison est-il au-dessus de la médiane ou non ? (1 pour oui et 0 pour non)

Maintenant que nous avons vu à quoi ressemblent nos données, nous voulons les convertir en tableaux pour que notre machine les traite :

```py
dataset = df.values
```

Pour convertir notre dataframe en un tableau, nous stockons simplement les valeurs de df (en accédant à _df.values_) dans la variable 'dataset'. Pour voir ce qu'il y a dans cette variable 'dataset', tapez simplement 'dataset' dans une boîte grise de votre notebook et exécutez la cellule (Alt-Enter) :

```py
dataset
```

Comme vous pouvez le voir, tout est stocké dans un tableau maintenant :

![Image](https://cdn-media-1.freecodecamp.org/images/Ll3wNKPdwhsm7j9OyzcbXR6ImSBg86GbBRyF)
_Conversion de notre dataframe en un tableau_

Nous divisons maintenant notre jeu de données en caractéristiques d'entrée (X) et la caractéristique que nous souhaitons prédire (Y). Pour faire cette division, nous attribuons simplement les 10 premières colonnes de notre tableau à une variable appelée X et la dernière colonne de notre tableau à une variable appelée Y. Le code pour faire la première attribution est le suivant :

```py
X = dataset[:,0:10]
```

Cela peut sembler un peu étrange, mais laissez-moi expliquer ce qu'il y a dans les crochets. Tout ce qui est avant la virgule fait référence aux lignes du tableau et tout ce qui est après la virgule fait référence aux colonnes des tableaux.

Puisque nous ne divisons pas les lignes, nous mettons ':' avant la virgule. Cela signifie prendre toutes les lignes dans dataset et les mettre dans X.

Nous voulons extraire les 10 premières colonnes, et donc le '0:10' après la virgule signifie prendre les colonnes 0 à 9 et les mettre dans X (nous n'incluons pas la colonne 10). Nos colonnes commencent à l'index 0, donc les 10 premières colonnes sont vraiment les colonnes 0 à 9.

Nous attribuons ensuite la dernière colonne de notre tableau à Y :

```py
Y = dataset[:,10]
```

Ok, maintenant nous avons divisé notre jeu de données en caractéristiques d'entrée (X) et l'étiquette de ce que nous voulons prédire (Y).

L'étape suivante dans notre traitement est de nous assurer que l'échelle des caractéristiques d'entrée est similaire. Actuellement, des caractéristiques telles que la superficie du terrain sont de l'ordre des milliers, un score pour la qualité globale est compris entre 1 et 10, et le nombre de cheminées tend à être 0, 1 ou 2.

Cela rend difficile l'initialisation du réseau de neurones, ce qui cause certains problèmes pratiques. Une façon de mettre à l'échelle les données est d'utiliser un package existant de scikit-learn (que nous avons installé dans le post [Getting Started](https://medium.com/intuitive-deep-learning/getting-started-with-python-for-deep-learning-and-data-science-9ca785560bbc)).

Nous devons d'abord importer le code que nous voulons utiliser :

```py
from sklearn import preprocessing
```

Cela signifie que je veux utiliser le code dans 'preprocessing' dans le package sklearn. Ensuite, nous utilisons une fonction appelée le min-max scaler, qui met à l'échelle le jeu de données de sorte que toutes les caractéristiques d'entrée se situent entre 0 et 1 inclus :

```py
min_max_scaler = preprocessing.MinMaxScaler()
X_scale = min_max_scaler.fit_transform(X)
```

Notez que nous avons choisi 0 et 1 intentionnellement pour aider à l'entraînement de notre réseau de neurones. Nous n'allons pas passer par la théorie derrière cela. Maintenant, notre jeu de données mis à l'échelle est stocké dans le tableau 'X_scale'. Si vous souhaitez voir à quoi ressemble 'X_scale', exécutez simplement la cellule :

```py
X_scale
```

Votre notebook Jupyter devrait maintenant ressembler un peu à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/o0mssMGKln1eRWC3dOBCKZTDKu4crA-e7BsI)

Maintenant, nous en sommes à notre dernière étape dans le traitement des données, qui est de diviser notre jeu de données en un ensemble d'entraînement, un ensemble de validation et un ensemble de test.

Nous allons utiliser le code de scikit-learn appelé 'train_test_split', qui, comme son nom l'indique, divise notre jeu de données en un ensemble d'entraînement et un ensemble de test. Nous importons d'abord le code dont nous avons besoin :

```py
from sklearn.model_selection import train_test_split
```

Ensuite, divisez votre jeu de données comme ceci :

```py
X_train, X_val_and_test, Y_train, Y_val_and_test = train_test_split(X_scale, Y, test_size=0.3)
```

Cela indique à scikit-learn que votre taille val_and_test sera de 30 % du jeu de données global. Le code stockera les données divisées dans les quatre premières variables à gauche du signe égal comme les noms de variables le suggèrent.

Malheureusement, cette fonction ne nous aide qu'à diviser notre jeu de données en deux. Puisque nous voulons un ensemble de validation et un ensemble de test séparés, nous pouvons utiliser la même fonction pour faire la division à nouveau sur val_and_test :

```py
X_val, X_test, Y_val, Y_test = train_test_split(X_val_and_test, Y_val_and_test, test_size=0.5)
```

Le code ci-dessus divisera la taille val_and_test également entre l'ensemble de validation et l'ensemble de test.

En résumé, nous avons maintenant un total de six variables pour nos jeux de données que nous allons utiliser :

* X_train _(10 caractéristiques d'entrée, 70 % du jeu de données complet)_
* X_val _(10 caractéristiques d'entrée, 15 % du jeu de données complet)_
* X_test _(10 caractéristiques d'entrée, 15 % du jeu de données complet)_
* Y_train _(1 étiquette, 70 % du jeu de données complet)_
* Y_val _(1 étiquette, 15 % du jeu de données complet)_
* Y_test _(1 étiquette, 15 % du jeu de données complet)_

Si vous voulez voir comment sont les formes des tableaux pour chacun d'eux (c'est-à-dire quelles dimensions ils ont), exécutez simplement

```py
print(X_train.shape, X_val.shape, X_test.shape, Y_train.shape, Y_val.shape, Y_test.shape)
```

Voici à quoi devrait ressembler votre notebook Jupyter :

![Image](https://cdn-media-1.freecodecamp.org/images/RK25dwBlhEsmOgOWJAIciegSMVFxWWx0zU-V)

Comme vous pouvez le voir, l'ensemble d'entraînement a 1022 points de données tandis que l'ensemble de validation et l'ensemble de test ont chacun 219 points de données. Les variables X ont 10 caractéristiques d'entrée, tandis que les variables Y n'ont qu'une seule caractéristique à prédire.

Et maintenant, nos données sont enfin prêtes ! Ouf !

**Résumé** : En traitant les données, nous avons :

* Lu le fichier CSV (valeurs séparées par des virgules) et les avons convertis en tableaux.
* Divisé notre jeu de données en caractéristiques d'entrée et en étiquette.
* Mis à l'échelle les données afin que les caractéristiques d'entrée aient des ordres de grandeur similaires.
* Divisé notre jeu de données en ensemble d'entraînement, ensemble de validation et ensemble de test.

### Construction et entraînement de notre premier réseau de neurones

Dans [Intuitive Deep Learning Part 1a](https://medium.com/intuitive-deep-learning/intuitive-deep-learning-part-1a-introduction-to-neural-networks-d7b16ebf6b99), nous avons dit que le Machine Learning consiste en deux étapes. La première étape est de spécifier un modèle (une architecture) et la deuxième étape est de trouver les meilleurs nombres à partir des données pour remplir ce modèle. Notre code à partir de maintenant suivra également ces deux étapes.

#### **Première étape : Configuration de l'architecture**

La première chose que nous devons faire est de configurer l'architecture. Réfléchissons d'abord au type d'architecture de réseau de neurones que nous voulons. Supposons que nous voulons ce réseau de neurones :

![Image](https://cdn-media-1.freecodecamp.org/images/H3eAYjXcA2asaCjCYrVT7lc2IIBQGQWzQlPG)
_Architecture du réseau de neurones que nous allons utiliser pour notre problème_

En mots, nous voulons avoir ces couches :

* Couche cachée 1 : 32 neurones, activation ReLU
* Couche cachée 2 : 32 neurones, activation ReLU
* Couche de sortie : 1 neurone, activation Sigmoid

Maintenant, nous devons décrire cette architecture à Keras. Nous allons utiliser le modèle Sequential, ce qui signifie que nous devons simplement décrire les couches ci-dessus en séquence.

Tout d'abord, importons le code nécessaire de Keras :

```py
from keras.models import Sequential
from keras.layers import Dense
```

Ensuite, nous spécifions cela dans notre modèle séquentiel Keras comme ceci :

```py
model = Sequential([
    Dense(32, activation='relu', input_shape=(10,)),
    Dense(32, activation='relu'),
    Dense(1, activation='sigmoid'),
])
```

Et juste comme ça, l'extrait de code ci-dessus a défini notre architecture ! Le code ci-dessus peut être interprété comme ceci :

`model = Sequential([ ... ])`

Cela signifie que nous allons stocker notre modèle dans la variable 'model', et nous allons le décrire séquentiellement (couche par couche) entre les crochets.

`Dense(32, activation='relu', input_shape=(10,)),`

Nous avons notre première couche comme une couche dense avec 32 neurones, activation ReLU et la forme d'entrée est 10 puisque nous avons 10 caractéristiques d'entrée. Notez que 'Dense' fait référence à une couche entièrement connectée, que nous allons utiliser.

`Dense(32, activation='relu'),`

Notre deuxième couche est également une couche dense avec 32 neurones, activation ReLU. Notez que nous n'avons pas à décrire la forme d'entrée puisque Keras peut l'inférer à partir de la sortie de notre première couche.

`Dense(1, activation='sigmoid'),`

Notre troisième couche est une couche dense avec 1 neurone, activation sigmoid.

Et juste comme ça, nous avons écrit notre architecture de modèle (modèle) en code !

#### **Deuxième étape : Remplir les meilleurs nombres**

Maintenant que nous avons spécifié notre architecture, nous devons trouver les meilleurs nombres pour celle-ci. Avant de commencer notre entraînement, nous devons configurer le modèle en

* Lui indiquant quel algorithme vous voulez utiliser pour faire l'optimisation
* Lui indiquant quelle fonction de perte utiliser
* Lui indiquant quelles autres métriques vous voulez suivre en plus de la fonction de perte

Configurer le modèle avec ces paramètres nécessite que nous appelions la fonction model.compile, comme ceci :

```py
model.compile(optimizer='sgd',
              loss='binary_crossentropy',
              metrics=['accuracy'])
```

Nous mettons les paramètres suivants à l'intérieur des parenthèses après model.compile :

`optimizer='sgd'`

'sgd' fait référence à la descente de gradient stochastique (ici, il fait référence à la descente de gradient par mini-lots), que nous avons vue dans [Intuitive Deep Learning Part 1b](https://medium.com/intuitive-deep-learning/intuitive-deep-learning-part-1b-introduction-to-neural-networks-8565d97ddd2d).

`loss='binary_crossentropy'`

La fonction de perte pour les sorties qui prennent les valeurs 1 ou 0 est appelée entropie croisée binaire.

`metrics=['accuracy']`

Enfin, nous voulons suivre la précision en plus de la fonction de perte. Maintenant, une fois que nous avons exécuté cette cellule, nous sommes prêts à entraîner !

L'entraînement sur les données est assez simple et nécessite que nous écrivions une ligne de code :

```py
hist = model.fit(X_train, Y_train,
          batch_size=32, epochs=100,
          validation_data=(X_val, Y_val))
```

La fonction est appelée 'fit' car nous ajustons les paramètres aux données. Nous devons spécifier sur quelles données nous nous entraînons, qui sont _X_train_ et _Y_train_. Ensuite, nous spécifions la taille de notre mini-lot et combien de temps nous voulons l'entraîner (époques). Enfin, nous spécifions quelles sont nos données de validation afin que le modèle nous dise comment nous nous en sortons sur les données de validation à chaque point. Cette fonction produira un historique, que nous enregistrons sous la variable hist. Nous utiliserons cette variable un peu plus tard lorsque nous passerons à la visualisation.

Maintenant, exécutez la cellule et regardez-le s'entraîner ! Votre notebook Jupyter devrait ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/VLeZkKcL18iweRJ4aVutxjnkTbSMV27fc3la)

Vous pouvez maintenant voir que le modèle s'entraîne ! En regardant les nombres, vous devriez pouvoir voir la perte diminuer et la précision augmenter avec le temps. À ce stade, vous pouvez expérimenter avec les hyper-paramètres et l'architecture du réseau de neurones. Exécutez à nouveau les cellules pour voir comment votre entraînement a changé lorsque vous avez ajusté vos hyperparamètres.

Une fois que vous êtes satisfait de votre modèle final, nous pouvons l'évaluer sur l'ensemble de test. Pour trouver la précision sur notre ensemble de test, nous exécutons ce code :

```py
model.evaluate(X_test, Y_test)[1]
```

La raison pour laquelle nous avons l'index 1 après la fonction model.evaluate est que la fonction retourne la perte comme premier élément et la précision comme deuxième élément. Pour n'afficher que la précision, accédez simplement au deuxième élément (qui est indexé par 1, puisque le premier élément commence son indexation à 0).

En raison de l'aléatoire dans la façon dont nous avons divisé le jeu de données ainsi que de l'initialisation des poids, les nombres et le graphique différeront légèrement chaque fois que nous exécuterons notre notebook. Néanmoins, vous devriez obtenir une précision de test comprise entre 80 % et 95 % si vous avez suivi l'architecture que j'ai spécifiée ci-dessus !

![Image](https://cdn-media-1.freecodecamp.org/images/xnmuiBvW0QOPJutrt5sT6zWIGFRstj3uVX7f)
_Évaluation sur l'ensemble de test_

Et voilà, vous avez codé votre tout premier réseau de neurones et l'avez entraîné ! Félicitations !

**Résumé** : Coder notre premier réseau de neurones n'a nécessité que quelques lignes de code :

* Nous spécifions l'architecture avec le modèle Sequential de Keras.
* Nous spécifions certains de nos paramètres (optimiseur, fonction de perte, métriques à suivre) avec _model.compile_
* Nous entraînons notre modèle (trouvons les meilleurs paramètres pour notre architecture) avec les données d'entraînement avec _model.fit_
* Nous évaluons notre modèle sur l'ensemble de test avec _model.evaluate_

### Visualisation de la perte et de la précision

Dans [Intuitive Deep Learning Part 1b](https://medium.com/intuitive-deep-learning/intuitive-deep-learning-part-1b-introduction-to-neural-networks-8565d97ddd2d), nous avons parlé du surapprentissage et de certaines techniques de régularisation. Comment savons-nous si notre modèle est actuellement en surapprentissage ?

Ce que nous pourrions vouloir faire, c'est tracer la perte d'entraînement et la perte de validation sur le nombre d'époques passées. Pour afficher quelques beaux graphiques, nous allons utiliser le package matplotlib. Comme d'habitude, nous devons importer le code que nous souhaitons utiliser :

```py
import matplotlib.pyplot as plt
```

Ensuite, nous voulons visualiser la perte d'entraînement et la perte de validation. Pour ce faire, exécutez cet extrait de code :

```py
plt.plot(hist.history['loss'])
plt.plot(hist.history['val_loss'])
plt.title('Perte du modèle')
plt.ylabel('Perte')
plt.xlabel('Époque')
plt.legend(['Entraînement', 'Val'], loc='upper right')
plt.show()
```

Nous allons expliquer chaque ligne de l'extrait de code ci-dessus. Les deux premières lignes indiquent que nous voulons tracer la perte et la val_loss. La troisième ligne spécifie le titre de ce graphique, "Perte du modèle". Les quatrième et cinquième lignes nous indiquent ce que les axes y et x doivent être étiquetés respectivement. La sixième ligne inclut une légende pour notre graphique, et l'emplacement de la légende sera en haut à droite. Et la septième ligne indique au notebook Jupyter d'afficher le graphique.

Votre notebook Jupyter devrait ressembler à quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/gB9CrPeAK1ebvv-z65CajZWnKNy8AenHNk0x)
_Un graphique de la perte du modèle que vous devriez voir dans votre notebook Jupyter_

Nous pouvons faire de même pour tracer notre précision d'entraînement et notre précision de validation avec le code ci-dessous :

```py
plt.plot(hist.history['acc'])
plt.plot(hist.history['val_acc'])
plt.title('Précision du modèle')
plt.ylabel('Précision')
plt.xlabel('Époque')
plt.legend(['Entraînement', 'Val'], loc='lower right')
plt.show()
```

Vous devriez obtenir un graphique qui ressemble un peu à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/IF6eidUC67Y0UxeY7NL2URaj72inDRbDTtf0)
_Tracé de la précision du modèle pour l'ensemble d'entraînement et de validation_

Puisque les améliorations de notre modèle pour l'ensemble d'entraînement semblent quelque peu correspondre aux améliorations pour l'ensemble de validation, il ne semble pas que le surapprentissage soit un _énorme_ problème dans notre modèle.

**Résumé** : Nous utilisons _matplotlib_ pour visualiser la perte et la précision d'entraînement et de validation au fil du temps afin de voir s'il y a du surapprentissage dans notre modèle.

### Ajout de la régularisation à notre réseau de neurones

Pour l'introduction de la régularisation à notre réseau de neurones, formulons avec un réseau de neurones qui va fortement surapprendre sur notre ensemble d'entraînement. Nous appellerons cela le Modèle 2.

```py
model_2 = Sequential([
    Dense(1000, activation='relu', input_shape=(10,)),
    Dense(1000, activation='relu'),
    Dense(1000, activation='relu'),
    Dense(1000, activation='relu'),
    Dense(1, activation='sigmoid'),
])

model_2.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])
              
hist_2 = model_2.fit(X_train, Y_train,
          batch_size=32, epochs=100,
          validation_data=(X_val, Y_val))
```

Ici, nous avons créé un modèle beaucoup plus grand et nous avons utilisé l'optimiseur Adam. Adam est l'un des optimiseurs les plus courants que nous utilisons, qui ajoute quelques ajustements à la descente de gradient stochastique de sorte qu'il atteint la fonction de perte inférieure plus rapidement. Si nous exécutons ce code et traçons les graphiques de perte pour hist_2 en utilisant le code ci-dessous (notez que le code est le même sauf que nous utilisons 'hist_2' au lieu de 'hist') :

```py
plt.plot(hist_2.history['loss'])
plt.plot(hist_2.history['val_loss'])
plt.title('Perte du modèle')
plt.ylabel('Perte')
plt.xlabel('Époque')
plt.legend(['Entraînement', 'Val'], loc='upper right')
plt.show()
```

Nous obtenons un tracé comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/ZritmKrZwMLvX4EtamODlvT2xubzIBMfItQ3)
_Courbes de perte pour le modèle de surapprentissage_

C'est un signe clair de surapprentissage. La perte d'entraînement diminue, mais la perte de validation est bien au-dessus de la perte d'entraînement et augmente (après le point d'inflexion de l'Époque 20). Si nous traçons la précision en utilisant le code ci-dessous :

```py
plt.plot(hist_2.history['acc'])
plt.plot(hist_2.history['val_acc'])
plt.title('Précision du modèle')
plt.ylabel('Précision')
plt.xlabel('Époque')
plt.legend(['Entraînement', 'Val'], loc='lower right')
plt.show()
```

Nous pouvons voir une divergence plus claire entre la précision d'entraînement et de validation également :

![Image](https://cdn-media-1.freecodecamp.org/images/tt-fzJPGAWdDyZL0aha8i1SYwPHQOOaxaQQ0)
_Précision d'entraînement et de validation pour notre modèle de surapprentissage_

Maintenant, essayons certaines de nos stratégies pour réduire le surapprentissage (en plus de changer notre architecture pour revenir à notre premier modèle). Rappelez-vous de [Intuitive Deep Learning Part 1b](https://medium.com/intuitive-deep-learning/intuitive-deep-learning-part-1b-introduction-to-neural-networks-8565d97ddd2d) que nous avons introduit trois stratégies pour réduire le surapprentissage.

Parmi les trois, nous allons incorporer la régularisation L2 et le dropout ici. La raison pour laquelle nous n'ajoutons pas l'arrêt précoce ici est que après avoir utilisé les deux premières stratégies, la perte de validation ne prend pas la forme en U que nous voyons ci-dessus et donc l'arrêt précoce ne sera pas aussi efficace.

Tout d'abord, importons le code dont nous avons besoin pour la régularisation L2 et le dropout :

```py
from keras.layers import Dropout
from keras import regularizers
```

Nous spécifions ensuite notre troisième modèle comme ceci :

```py
model_3 = Sequential([
    Dense(1000, activation='relu', kernel_regularizer=regularizers.l2(0.01), input_shape=(10,)),
    Dropout(0.3),
    Dense(1000, activation='relu', kernel_regularizer=regularizers.l2(0.01)),
    Dropout(0.3),
    Dense(1000, activation='relu', kernel_regularizer=regularizers.l2(0.01)),
    Dropout(0.3),
    Dense(1000, activation='relu', kernel_regularizer=regularizers.l2(0.01)),
    Dropout(0.3),
    Dense(1, activation='sigmoid', kernel_regularizer=regularizers.l2(0.01)),
])
```

Pouvez-vous repérer les différences entre le Modèle 3 et le Modèle 2 ? Il y a deux différences principales :

**Différence 1** : Pour ajouter la régularisation L2, notez que nous avons ajouté un peu de code supplémentaire dans chacune de nos couches denses comme ceci :

`kernel_regularizer=regularizers.l2(0.01)`

Cela indique à Keras d'inclure les valeurs au carré de ces paramètres dans notre fonction de perte globale, et de les pondérer par 0,01 dans la fonction de perte.

**Différence 2** : Pour ajouter le Dropout, nous avons ajouté une nouvelle couche comme ceci :

`Dropout(0.3),`

Cela signifie que les neurones de la couche précédente ont une probabilité de 0,3 de tomber pendant l'entraînement. Compilons-le et exécutons-le avec les mêmes paramètres que notre Modèle 2 (celui qui surapprend) :

```py
model_3.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])
              
hist_3 = model_3.fit(X_train, Y_train,
          batch_size=32, epochs=100,
          validation_data=(X_val, Y_val))
```

Et maintenant, traçons les graphiques de perte et de précision. Vous remarquerez que la perte est beaucoup plus élevée au début, et c'est parce que nous avons changé notre fonction de perte. Pour tracer de sorte que la fenêtre soit zoomée entre 0 et 1,2 pour la perte, nous ajoutons une ligne de code supplémentaire (plt.ylim) lors du traçage :

```py
plt.plot(hist_3.history['loss'])
plt.plot(hist_3.history['val_loss'])
plt.title('Perte du modèle')
plt.ylabel('Perte')
plt.xlabel('Époque')
plt.legend(['Entraînement', 'Val'], loc='upper right')
plt.ylim(top=1.2, bottom=0)
plt.show()
```

Nous obtiendrons un graphique de perte qui ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/dXsh4tEr-783nJk0cdPQM0F6wYFhgwn4OthE)

Vous pouvez voir que la perte de validation correspond beaucoup plus étroitement à notre perte d'entraînement. Traçons la précision avec un extrait de code similaire :

```py
plt.plot(hist_3.history['acc'])
plt.plot(hist_3.history['val_acc'])
plt.title('Précision du modèle')
plt.ylabel('Précision')
plt.xlabel('Époque')
plt.legend(['Entraînement', 'Val'], loc='lower right')
plt.show()
```

Et nous obtiendrons un tracé comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/BcP0wBP2jAhq3tpN1UKS4zFJ0cykMw9Q7325)

Comparé à notre modèle dans le Modèle 2, nous avons considérablement réduit le surapprentissage ! Et c'est ainsi que nous appliquons nos techniques de régularisation pour réduire le surapprentissage à l'ensemble d'entraînement.

**Résumé** : Pour traiter le surapprentissage, nous pouvons coder les stratégies suivantes dans notre modèle, chacune avec environ une ligne de code :

* Régularisation L2
* Dropout

Si nous visualisons la perte/précision d'entraînement et de validation, nous pouvons voir que ces ajouts ont aidé à traiter le surapprentissage !

#### **Résumé consolidé** :

Dans cet article, nous avons écrit du code Python pour :

* Explorer et traiter les données
* Construire et entraîner notre réseau de neurones
* Visualiser la perte et la précision
* Ajouter la régularisation à notre réseau de neurones

Nous avons parcouru beaucoup de choses, mais nous n'avons pas écrit trop de lignes de code ! La construction et l'entraînement de notre réseau de neurones n'ont pris que 4 à 5 lignes de code, et l'expérimentation avec différentes architectures de modèles est simplement une question de permutation de différentes couches ou de changement de différents hyperparamètres. Keras a effectivement rendu beaucoup plus facile la construction de nos réseaux de neurones, et nous continuerons à l'utiliser pour des applications plus avancées en vision par ordinateur et en traitement du langage naturel.

**Prochaine étape** : Dans notre prochain [Coding Companion Part 2](https://medium.com/intuitive-deep-learning/build-your-first-convolutional-neural-network-to-recognize-images-84b9c78fe0ce), nous explorerons comment coder nos propres réseaux de neurones convolutifs (CNN) pour faire de la reconnaissance d'images !

[**Construisez votre premier réseau de neurones convolutifs pour reconnaître des images**](https://medium.com/intuitive-deep-learning/build-your-first-convolutional-neural-network-to-recognize-images-84b9c78fe0ce)
[_Un guide étape par étape pour construire votre propre logiciel de reconnaissance d'images avec des réseaux de neurones convolutifs en utilisant Keras sur...medium.com_](https://medium.com/intuitive-deep-learning/build-your-first-convolutional-neural-network-to-recognize-images-84b9c78fe0ce)

Assurez-vous d'abord de bien comprendre les CNN ici : [Intuitive Deep Learning Part 2: CNNs for Computer Vision](https://medium.com/intuitive-deep-learning/intuitive-deep-learning-part-2-cnns-for-computer-vision-24992d050a27)

**À propos de l'auteur** :

Bonjour, je suis [Joseph](http://ai.stanford.edu/~josephlee) ! J'ai récemment obtenu mon diplôme de l'Université de Stanford, où j'ai travaillé avec Andrew Ng dans le [Stanford Machine Learning Group](https://stanfordmlgroup.github.io/). Je veux rendre les concepts du Deep Learning aussi intuitifs et aussi facilement compréhensibles que possible par tout le monde, ce qui a motivé ma publication : [Intuitive Deep Learning](https://medium.com/intuitive-deep-learning).