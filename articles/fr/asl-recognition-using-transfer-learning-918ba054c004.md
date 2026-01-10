---
title: Comment utiliser le transfert d'apprentissage pour la reconnaissance de la
  langue des signes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-10T18:13:51.000Z'
originalURL: https://freecodecamp.org/news/asl-recognition-using-transfer-learning-918ba054c004
coverImage: https://cdn-media-1.freecodecamp.org/images/1*tmh4aAYfP-1SGqpqAaim3w.png
tags:
- name: American Sign Language
  slug: american-sign-language
- name: Deep Learning
  slug: deep-learning
- name: Machine Learning
  slug: machine-learning
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Comment utiliser le transfert d'apprentissage pour la reconnaissance de
  la langue des signes
seo_desc: 'By Vagdevi Kommineni

  As a continuation of my previous post on ASL Recognition using AlexNet — training
  from scratch, let us now consider how to solve this problem using the transfer learning
  technique.


  Transfer learning has become so handy for compu...'
---

Par Vagdevi Kommineni

En tant que continuation de mon précédent article sur [Reconnaissance ASL utilisant AlexNet — entraînement à partir de zéro](https://medium.com/@vagdevi.k15/asl-using-alexnet-training-from-scratch-cfec9a8acf84), voyons maintenant comment résoudre ce problème en utilisant la technique de transfert d'apprentissage.

![Image](https://cdn-media-1.freecodecamp.org/images/nhxsEn9S-VwNdFKCClwfeKhKmTd1buwzF3pR)

Le transfert d'apprentissage est devenu si pratique pour les passionnés de vision par ordinateur.

C'est essentiellement un mécanisme où les connaissances acquises en entraînant un modèle pour accomplir une tâche sont modifiées ou optimisées efficacement afin d'accomplir une deuxième tâche liée.

> L'une des tâches puissantes de l'apprentissage profond est que, parfois, nous pouvons prendre les connaissances que le réseau de neurones a apprises d'une tâche (tâche A) et appliquer ces connaissances à une autre tâche (tâche B). Cela s'appelle le transfert d'apprentissage.  
>  
> — Andrew Ng

![Image](https://cdn-media-1.freecodecamp.org/images/2BSIEF-cvwEyUbDX-CPAqKmhs8Fg1VZ1jj0t)

Par exemple, un réseau de neurones entraîné sur la reconnaissance d'objets peut être utilisé pour lire des scans aux rayons X. Cela est réalisé en gelant les poids jusqu'à ce que les couches initiales ou intermédiaires soient apprises sur les données de la tâche A, en supprimant la dernière couche ou quelques-unes des dernières couches, et en ajoutant de nouvelles couches et en entraînant ces paramètres en utilisant les données de la tâche B.

Le transfert d'apprentissage a du sens lorsque les données d'entraînement pour la tâche A sont assez grandes et que celles de la tâche B sont relativement plus petites. En étant entraîné sur de telles vastes quantités de données et en montrant d'excellentes performances sur ses données de test, cela implique que le réseau de neurones a une bonne connaissance de l'extraction de caractéristiques utiles à partir des images d'entrée. Cela est essentiel et puissant pour accomplir une tâche.

Maintenant que nous avons de telles caractéristiques puissantes de ces couches (dont les poids de la tâche A sont gelés), nous devons simplement utiliser ces caractéristiques extraites pour accomplir la tâche B. Ainsi, ces caractéristiques des couches gelées sont alimentées aux nouvelles couches et les paramètres de ces couches sont entraînés sur les données de la tâche B.

Donc, essentiellement, nous stockons les connaissances de la tâche précédente sous la forme des poids des couches gelées (appelé pré-entraînement). Ensuite, nous rendons le réseau de neurones spécifique à la tâche B en entraînant (appelé ajustement fin) les couches ultérieures sur les nouvelles données. Pour plus d'informations sur le transfert d'apprentissage, veuillez visiter [ici](https://www.youtube.com/watch?v=yofjFQddwHE).

Cette technique est vraiment utile car :

* nous pouvons mettre en place un modèle qui performe élégamment pour la tâche B, même si nous avons moins de données disponibles pour la tâche B,
* il y a moins de paramètres à entraîner (seulement la dernière couche/couches) et ainsi moins de temps d'entraînement,
* il y a moins de demande pour des ressources computationnelles lourdes comme GPU, TPU (mais cela dépend toujours des données disponibles pour la tâche B).

Puisque cet article est la continuation du précédent sur [Reconnaissance ASL utilisant AlexNet — entraînement à partir de zéro](https://medium.com/@vagdevi.k15/asl-using-alexnet-training-from-scratch-cfec9a8acf84), veuillez vous référer à cet article pour les détails de prétraitement et le code (preprocess.py).

Les données utilisées pour les deux articles sont ces [données Kaggle pour ASL](https://www.kaggle.com/grassknoted/asl-alphabet). Le jeu de données se compose d'images de gestes de la main pour chaque lettre de l'alphabet anglais. Les images d'une seule classe sont de différentes variantes, comme des versions zoomées, des conditions de lumière tamisée et vive, etc. Pour chaque classe, il y a jusqu'à 3000 images. Voici les liens pour le code complet de [prétraitement et entraînement](https://github.com/vagdevik/American-Sign-Language-Recognition-System/blob/master/4_VGG16_BCVWL/asl_full.py) et [test](https://github.com/vagdevik/American-Sign-Language-Recognition-System/blob/master/4_VGG16_BCVWL/predict.py).

Pour le transfert d'apprentissage, j'ai utilisé le modèle pré-entraîné VGG16 entraîné sur le jeu de données ImageNet. Les poids sont facilement disponibles dans Keras. Nous allons d'abord importer tous les modules nécessaires comme suit :

```
import keras
from keras.optimizers import SGD
from keras.models import Sequential
from keras.applications import VGG16   # Poids pré-entraînés VGG16
from keras.preprocessing import image
from keras.layers.normalization import BatchNormalization
from keras.layers import Dense, Activation, Dropout, Flatten, Conv2D, MaxPooling2D
```

```
print("Imported Network Essentials")
```

Initions maintenant le modèle pour qu'il soit séquentiel et ajoutons d'abord le réseau VGG16 pré-entraîné à notre modèle. Notez que nous devons supprimer les dernières couches (appelées couches supérieures) et geler les poids de toutes les couches précédentes. Cela est fait par `include_top=False`. `weights='imagenet'` prend les poids du réseau VGG16 entraîné sur le jeu de données ImageNet.

```
# pour fixer la taille de l'image d'entrée
image_size=224
```

```
# Charger le modèle VGG
vgg_base = VGG16(weights='imagenet', include_top=False, input_shape=(image_size, image_size, 3))
```

Maintenant, la partie de VGG16 que nous voulons est stockée dans `vgg_base`. Nous allons également ajouter les autres couches comme les couches denses et les couches de dropout au-dessus de `vgg_base`. Ainsi, l'architecture complète du réseau de neurones que nous utilisons sera :

```
# initier un modèle
model = Sequential()
# Ajouter le modèle de base VGG
model.add(vgg_base)
# Ajouter de nouvelles couches
model.add(Flatten())
model.add(Dense(8192, activation='relu'))
model.add(Dropout(0.8))
model.add(Dense(4096, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(5, activation='softmax'))
```

Nous allons ensuite définir notre optimiseur comme SGD et régler la valeur du taux d'apprentissage `lr`. Puisque cela est une classification catégorielle, nous utilisons categorical_crossentropy comme fonction de perte dans `model.compile`. L'utilisation de points de contrôle est la meilleure façon de stocker les poids que nous avons obtenus jusqu'au point d'interruption, afin que nous puissions les utiliser plus tard. Le premier paramètre est de définir l'endroit pour stocker : sauvegardez-le sous `weights.{epoch:02d}-{val_loss:.2f}.hdf5` dans le dossier Checkpoints. Nous procédons ensuite à l'entraînement en utilisant `model.fit`.

```
# Compiler
sgd = SGD(lr=0.001)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
checkpoint = keras.callbacks.ModelCheckpoint("Weights/weights.{epoch:02d}-{val_loss:.2f}.hdf5", monitor='val_loss', verbose=0, save_best_only=False, save_weights_only=False, mode='auto', period=1)
```

```
# Entraîner
model.fit(X_train/255.0, Y_train, batch_size=32, epochs=15, verbose=1, validation_data=(X_test/255.0, Y_test/255.0), shuffle=True, callbacks=[checkpoint])
```

Nous pouvons sauvegarder le modèle et les poids comme suit :

```
# séquentialiser le modèle en JSON
model_json = model.to_json()
with open("Model/model.json", "w") as json_file:
    json_file.write(model_json)
```

```
# séquentialiser les poids en HDF5
model.save_weights("Model/model_weights.h5")
print("Saved model to disk")
```

Jetons un coup d'œil au code complet pour l'entraînement ici :

```
# train.py
```

```
import keras
from keras.optimizers import SGD
from keras.models import Sequential
from keras.applications import VGG16   # Poids pré-entraînés VGG16
from keras.preprocessing import image
from keras.layers.normalization import BatchNormalization
from keras.layers import Dense, Activation, Dropout, Flatten, Conv2D, MaxPooling2D
print("Imported Network Essentials")
```

```
# pour fixer la taille de l'image d'entrée
image_size=224
```

```
# Charger le modèle VGG
vgg_base = VGG16(weights='imagenet', include_top=False, input_shape=(image_size, image_size, 3))
```

```
# initier un modèle
model = Sequential()
# Ajouter le modèle de base VGG
model.add(vgg_base)
# Ajouter de nouvelles couches
model.add(Flatten())
model.add(Dense(8192, activation='relu'))
model.add(Dropout(0.8))
model.add(Dense(4096, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(5, activation='softmax'))
```

```
# Compiler
sgd = SGD(lr=0.001)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
checkpoint = keras.callbacks.ModelCheckpoint("Weights/weights.{epoch:02d}-{val_loss:.2f}.hdf5", monitor='val_loss', verbose=0, save_best_only=False, save_weights_only=False, mode='auto', period=1)
```

```
# Entraîner
model.fit(X_train/255.0, Y_train, batch_size=32, epochs=15, verbose=1, validation_data=(X_test/255.0, Y_test/255.0), shuffle=True, callbacks=[checkpoint])
```

```
# séquentialiser le modèle en JSON
model_json = model.to_json()
with open("Model/model.json", "w") as json_file:
    json_file.write(model_json)
```

```
# séquentialiser les poids en HDF5
model.save_weights("Model/model_weights.h5")
print("Saved model to disk")
```

Maintenant, il est temps de tester ! Voici comment charger le modèle et les poids entraînés à partir des fichiers JSON stockés et utiliser la métrique d'évaluation `accuracy_score` de `sklearn.metrics`.

```
# test.py
```

```
import numpy as np
from keras.models import model_from_json
from sklearn.metrics import accuracy_score
```

```
# dimensions de nos images
image_size = 224
with open('Model/model.json', 'r') as f:
    model = model_from_json(f.read())
    model.summary()
model.load_weights('Model/model_weights.h5')
```

```
# chargement des images de test numpy (n'hésitez pas à regarder le prétraitement)
X_test=np.load("Numpy/test_set.npy")
Y_test=np.load("Numpy/test_classes.npy")
```

```
# obtenir les prédictions et obtenir le maximum des prédictions
# puisque les prédictions sont de la forme [0.01, 0.99, 0, 0] dans Y_predict et
# sont de la forme [0,1,0,0] dans Y_test
Y_predict = model.predict(X_test)
Y_predict = [np.argmax(r) for r in Y_predict]
Y_test = [np.argmax(r) for r in Y_test]
```

```
print("##################")
acc_score = accuracy_score(Y_test, Y_predict)
print("Accuracy: "+str(acc_score))
print("##################")
```

J'ai obtenu une précision de 97 %. Vous pouvez suivre certaines étapes pour améliorer la précision comme :

* l'ajustement des hyperparamètres.
* l'utilisation d'un modèle pré-entraîné différent comme ResNet, VGG19, etc. au lieu de VGG16.

Le code complet peut être trouvé [ici](https://github.com/vagdevik/American-Sign-Language-Recognition-System/tree/master/3_VGG16_newData). J'adorerais entendre vos résultats dans la section des commentaires ci-dessous.

Bon apprentissage !