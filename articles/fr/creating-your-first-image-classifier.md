---
title: Comment créer un classificateur d'images simple
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-18T18:06:36.000Z'
originalURL: https://freecodecamp.org/news/creating-your-first-image-classifier
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/mnist-fashion3.png
tags:
- name: Computer Vision
  slug: computer-vision
- name: Deep Learning
  slug: deep-learning
- name: image classification
  slug: image-classification
- name: neural networks
  slug: neural-networks
seo_title: Comment créer un classificateur d'images simple
seo_desc: "By Aditya\nImage classification is an amazing application of deep learning.\
  \ We can train a powerful algorithm to model a large image dataset. This model can\
  \ then be used to classify a similar but unknown set of images. \nThere is no limit\
  \ to the applic..."
---

Par Aditya

La classification d'images est une application incroyable de l'apprentissage profond. Nous pouvons entraîner un algorithme puissant pour modéliser un grand ensemble de données d'images. Ce modèle peut ensuite être utilisé pour classer un ensemble d'images similaire mais inconnu. 

Il n'y a pas de limite aux applications de la classification d'images. Vous pouvez l'utiliser dans votre prochaine application ou vous pouvez l'utiliser pour résoudre un problème réel. Tout dépend de vous. Mais pour quelqu'un qui est relativement nouveau dans ce domaine, cela peut sembler très difficile au début. Comment obtenir mes données ? Comment construire mon modèle ? Quels outils utiliser ? 

Dans cet article, nous discuterons de tout cela - de la recherche d'un ensemble de données à l'entraînement de votre modèle. J'essaierai de rendre les choses aussi simples que possible en évitant certains détails techniques (_PS : Veuillez noter que cela ne signifie pas que ces détails ne sont pas importants. Je mentionnerai quelques excellentes ressources que vous pouvez consulter pour en savoir plus sur ces sujets_). Le but de cet article est d'expliquer le processus de base de la création d'un classificateur d'images et c'est ce sur quoi nous nous concentrerons davantage ici. 

Nous allons construire un classificateur d'images pour le [Fashion-MNIST Dataset](https://research.zalando.com/welcome/mission/research-projects/fashion-mnist/). Le jeu de données Fashion-MNIST est une collection d'images d'articles de [Zalando](https://research.zalando.com/). Il contient 60 000 images pour l'ensemble d'entraînement et 10 000 images pour l'ensemble de test (_nous discuterons des ensembles de test et d'entraînement ainsi que de l'ensemble de validation plus tard_). Ces images appartiennent aux étiquettes de 10 classes différentes. 

![Image](https://www.freecodecamp.org/news/content/images/2019/07/mnist-fashion.png)
_[Source](https://research.zalando.com/welcome/mission/research-projects/fashion-mnist/)_

## Importation des bibliothèques

Notre objectif est d'entraîner un modèle d'apprentissage profond qui peut classer un ensemble donné d'images dans l'une de ces 10 classes. Maintenant que nous avons notre ensemble de données, nous devrions passer aux outils dont nous avons besoin. Il existe de nombreuses bibliothèques et outils que vous pouvez choisir en fonction des exigences de votre propre projet. Pour celui-ci, je vais me limiter aux suivants :

1. [**Numpy**](https://www.numpy.org/) - Bibliothèque Python pour le calcul numérique
2. [**Pandas**](https://pandas.pydata.org/) - Bibliothèque Python pour la manipulation de données
3. [**Matplotlib**](https://matplotlib.org/) - Bibliothèque Python pour la visualisation de données
4. [**Keras**](https://keras.io/) - Bibliothèque Python basée sur TensorFlow pour la création de modèles d'apprentissage profond
5. [**Jupyter**](https://jupyter.org/) - J'exécuterai tout mon code sur Jupyter Notebooks. Vous pouvez l'installer via le lien. Vous pouvez également utiliser [Google Colabs](https://colab.research.google.com/) si vous avez besoin de plus de puissance de calcul.

En plus de ces quatre, nous utiliserons également [scikit-learn](https://scikit-learn.org/). Le but de ces bibliothèques deviendra plus clair une fois que nous plongerons dans le code. 

D'accord ! Nous avons nos outils et bibliothèques prêts. Maintenant, nous devrions commencer à configurer notre code.

Commencez par importer toutes les bibliothèques mentionnées ci-dessus. En plus d'importer les bibliothèques, j'ai également importé certains modules spécifiques de ces bibliothèques. Laissez-moi les passer en revue un par un.

```python3
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
import keras 

from sklearn.model_selection import train_test_split 
from keras.utils import to_categorical 

from keras.models import Sequential 
from keras.layers import Conv2D, MaxPooling2D 
from keras.layers import Dense, Dropout 
from keras.layers import Flatten, BatchNormalization
```

**[train_test_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html) :** Ce module divise l'ensemble de données d'entraînement en données d'entraînement et de validation. La raison de cette division est de vérifier si notre modèle est en [surapprentissage](https://fr.wikipedia.org/wiki/Surapprentissage) ou non. Nous utilisons un ensemble de données d'entraînement pour entraîner notre modèle, puis nous comparerons la précision résultante à la précision de validation. Si la différence entre les deux quantités est significativement grande, alors notre modèle est probablement en surapprentissage. Nous réitérerons à travers notre processus de construction de modèle et apporterons les modifications nécessaires en cours de route. Une fois que nous serons satisfaits de nos précisions d'entraînement et de validation, nous ferons des prédictions finales sur nos données de test. 

**to_categorical :** to_categorical est un utilitaire de Keras. Il est utilisé pour convertir les étiquettes catégorielles en [encodages one-hot](https://machinelearningmastery.com/why-one-hot-encode-data-in-machine-learning/). Supposons que nous avons trois étiquettes ("pommes", "oranges", "bananes"), alors les encodages one-hot pour chacune de celles-ci seraient [1, 0, 0] -> "pommes", [0, 1, 0] -> "oranges", [0, 0, 1] -> "bananes".

Le reste des modules Keras que nous avons importés sont des couches de convolution. Nous discuterons des couches de convolution lorsque nous commencerons à construire notre modèle. Nous donnerons également un rapide aperçu de ce que fait chacune de ces couches.

## Prétraitement des données

Pour l'instant, nous allons porter notre attention sur l'obtention de nos données et leur analyse. Vous devez toujours vous rappeler l'importance du prétraitement et de l'analyse des données. Cela vous donne non seulement des informations sur les données, mais aide également à localiser les incohérences. 

Une très légère variation dans les données peut parfois conduire à un résultat dévastateur pour votre modèle. Cela rend important le prétraitement de vos données avant de les utiliser pour l'entraînement. Alors, avec cela à l'esprit, commençons le prétraitement des données.

```python3
train_df = pd.read_csv('./fashion-mnist_train.csv')
test_df = pd.read_csv('./fashion-mnist_test.csv')
```

Tout d'abord, importons notre ensemble de données (_[Voici](https://www.kaggle.com/zalando-research/fashionmnist) le lien pour télécharger cet ensemble de données sur votre système_). Une fois que vous avez importé l'ensemble de données, exécutez la commande suivante.

```python3
train_df.head()
```

Cette commande vous montrera à quoi ressemblent vos données. La capture d'écran suivante montre la sortie de cette commande.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/head_output.png)

Nous pouvons voir comment nos données d'image sont stockées sous forme de valeurs de pixels. Mais nous ne pouvons pas alimenter les données à notre modèle dans ce format. Nous devrons donc les convertir en tableaux numpy. 

```python3
train_data = np.array(train_df.iloc[:, 1:])
test_data = np.array(test_df.iloc[:, 1:])
```

Maintenant, il est temps d'obtenir nos étiquettes. 

```python3
train_labels = to_categorical(train_df.iloc[:, 0])
test_labels = to_categorical(test_df.iloc[:, 0])
```

Ici, vous pouvez voir que nous avons utilisé _to_categorical_ pour convertir nos données catégorielles en encodages one-hot.

Nous allons maintenant remodeler les données et les convertir en type _float32_ afin de pouvoir les utiliser commodément. 

```
rows, cols = 28, 28 

train_data = train_data.reshape(train_data.shape[0], rows, cols, 1)
test_data = test_data.reshape(test_data.shape[0], rows, cols, 1)

train_data = train_data.astype('float32')
test_data = test_data.astype('float32')
```

Nous avons presque terminé. Terminez simplement le prétraitement de nos données en les normalisant. La normalisation des données d'image mappera toutes les valeurs de pixels dans chaque image aux valeurs comprises entre 0 et 1. Cela nous aide à réduire les incohérences dans les données. Avant la normalisation, les données d'image peuvent avoir de grandes variations dans les valeurs de pixels, ce qui peut conduire à un comportement inhabituel pendant le processus d'entraînement. 

```
train_data /= 255.0
test_data /= 255.0
```

## Réseaux de neurones convolutionnels

Donc, le prétraitement des données est terminé. Maintenant, nous pouvons commencer à construire notre modèle. Nous allons construire un [Réseau de Neurones Convolutionnel](http://cs231n.github.io/convolutional-networks/) pour modéliser les données d'image. Les CNNs sont des versions modifiées des réseaux de neurones réguliers. Ces versions sont modifiées spécifiquement pour les données d'image. Alimenter des images dans des réseaux de neurones réguliers nécessiterait que notre réseau ait un grand nombre de neurones d'entrée. Par exemple, juste pour une image de 28x28, nous aurions besoin de 784 neurones d'entrée. Cela créerait un énorme désordre de paramètres d'entraînement.

Les CNNs résolvent ce problème en supposant déjà que l'entrée va être une image. Le principal objectif des réseaux de neurones convolutionnels est de tirer parti de la structure spatiale de l'image et d'extraire des caractéristiques de haut niveau à partir de celle-ci, puis de s'entraîner sur ces caractéristiques. Il le fait en effectuant une opération de [convolution](https://fr.wikipedia.org/wiki/Convolution) sur la matrice des valeurs de pixels.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/convSobel.gif)
_[Source](https://mlnotebook.github.io/post/CNN1/)_

La visualisation ci-dessus montre comment fonctionne l'opération de convolution. Et la couche Conv2D que nous avons importée précédemment fait la même chose. La première matrice (_à gauche_) dans la démonstration est l'entrée de la couche convolutionnelle. Ensuite, une autre matrice appelée "filtre" ou "noyau" est multipliée (multiplication de matrices) à chaque fenêtre de la matrice d'entrée. La sortie de cette multiplication est l'entrée de la couche suivante. 

Outre les couches convolutionnelles, un CNN typique possède également deux autres types de couches : 1) une [couche de pooling](https://machinelearningmastery.com/pooling-layers-for-convolutional-neural-networks/), et 2) une [couche entièrement connectée](https://stats.stackexchange.com/questions/182102/what-do-the-fully-connected-layers-do-in-cnns). 

Les couches de pooling sont utilisées pour généraliser la sortie des couches convolutionnelles. En plus de généraliser, elles réduisent également le nombre de paramètres dans le modèle en sous-échantillonnant la sortie de la couche convolutionnelle. 

Comme nous venons de l'apprendre, les couches convolutionnelles représentent des caractéristiques de haut niveau à partir des données d'image. Les couches entièrement connectées utilisent ces caractéristiques de haut niveau pour entraîner les paramètres et apprendre à classer ces images. 

Nous utiliserons également les couches [Dropout](https://machinelearningmastery.com/dropout-for-regularizing-deep-neural-networks/), [Batch-normalization](https://fr.wikipedia.org/wiki/Batch_normalization) et [Flatten](https://stackoverflow.com/questions/43237124/role-of-flatten-in-keras) en plus des couches mentionnées ci-dessus. La couche Flatten convertit la sortie des couches convolutionnelles en un vecteur de caractéristiques unidimensionnel. Il est important d'aplatir les sorties car les couches Dense (entièrement connectées) n'acceptent qu'un vecteur de caractéristiques en entrée. Les couches Dropout et Batch-normalization sont utilisées pour empêcher le modèle de [surapprendre](https://fr.wikipedia.org/wiki/Surapprentissage).

```python
train_x, val_x, train_y, val_y = train_test_split(train_data, train_labels, test_size=0.2)

batch_size = 256
epochs = 5
input_shape = (rows, cols, 1)
```

```
def baseline_model():
    model = Sequential()
    model.add(BatchNormalization(input_shape=input_shape))
    model.add(Conv2D(32, (3, 3), padding='same', activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2), strides=(2,2)))
    model.add(Dropout(0.25))
    
    model.add(BatchNormalization())
    model.add(Conv2D(32, (3, 3), padding='same', activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(10, activation='softmax'))
    return model
```

Le code que vous voyez ci-dessus est le code pour notre modèle CNN. Vous pouvez structurer ces couches de nombreuses manières différentes pour obtenir de bons résultats. Il existe de nombreuses architectures CNN populaires qui donnent des résultats de pointe. Ici, j'ai simplement créé ma propre architecture simple pour les besoins de ce problème. N'hésitez pas à essayer la vôtre et faites-moi savoir quels résultats vous obtenez :)

## Entraînement du modèle

Une fois que vous avez créé le modèle, vous pouvez l'importer puis le compiler en utilisant le code ci-dessous.

```
model = baseline_model()
model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])

```

**model.compile** configure le processus d'apprentissage pour notre modèle. Nous lui avons passé trois arguments. Ces arguments définissent la [fonction de perte](https://machinelearningmastery.com/loss-and-loss-functions-for-training-deep-learning-neural-networks/) pour notre modèle, l'[optimiseur](https://blog.algorithmia.com/introduction-to-optimizers/) et les [métriques](https://keras.io/metrics/).

```
history = model.fit(train_x, train_y,
          batch_size=batch_size,
          epochs=epochs,
          verbose=1,
          validation_data=(val_x, val_y))
          
```

Et enfin, en exécutant le code ci-dessus, vous pouvez entraîner votre modèle. J'entraîne ce modèle pour seulement cinq époques, mais vous pouvez augmenter le nombre d'époques. Une fois votre processus d'entraînement terminé, vous pouvez faire des prédictions sur l'ensemble de test en utilisant le code suivant.

```
predictions= model.predict(test_data)
```

## Conclusion

Félicitations ! Vous l'avez fait, vous avez fait votre premier pas dans le monde incroyable de la vision par ordinateur. 

Vous avez créé votre propre classificateur d'images. Bien que ce soit une grande réalisation, nous n'avons fait qu'effleurer la surface. 

Il y a beaucoup de choses que vous pouvez faire avec les CNNs. Les applications sont illimitées. J'espère que cet article vous a aidé à comprendre comment fonctionne le processus d'entraînement de ces modèles. 

Travailler sur d'autres ensembles de données par vous-même vous aidera à comprendre cela encore mieux. J'ai également créé un dépôt GitHub [repository](https://github.com/aditya2000/MNIST-Fashion-) pour le code que j'ai utilisé dans cet article. Donc, si cet article vous a été utile, faites-le moi savoir. 

Si vous avez des questions ou si vous voulez partager vos propres résultats ou si vous voulez simplement dire "bonjour", n'hésitez pas à me contacter sur [twitter](https://twitter.com/aditya_dehal), et je ferai de mon mieux pour vous aider. Et enfin **Merci beaucoup d'avoir lu cet article !!** :)