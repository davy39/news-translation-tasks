---
title: Comment construire un réseau de neurones convolutifs qui reconnaît les gestes
  de la langue des signes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-31T14:45:22.000Z'
originalURL: https://freecodecamp.org/news/asl-using-alexnet-training-from-scratch-cfec9a8acf84
coverImage: https://cdn-media-1.freecodecamp.org/images/1*vrcZTOV9qoL_pmjAXC-WsQ.png
tags:
- name: Alexnet
  slug: alexnet
- name: American Sign Language
  slug: american-sign-language
- name: Data Science
  slug: data-science
- name: Deep Learning
  slug: deep-learning
- name: 'tech '
  slug: tech
seo_title: Comment construire un réseau de neurones convolutifs qui reconnaît les
  gestes de la langue des signes
seo_desc: 'By Vagdevi Kommineni

  Sign language has been a major boon for people who are hearing- and speech-impaired.
  But it can serve its purpose only when the other person can understand sign language.
  Thus it would be really nice to have a system which could ...'
---

Par Vagdevi Kommineni

La langue des signes a été une aide majeure pour les personnes malentendantes et ayant des troubles de la parole. Mais elle ne peut servir son but que lorsque l'autre personne peut comprendre la langue des signes. Il serait donc vraiment utile d'avoir un système qui pourrait convertir l'image du geste de la main en la lettre anglaise correspondante. Ainsi, l'objectif de cet article est de construire un tel système de reconnaissance de la langue des signes américaine.

![Image](https://cdn-media-1.freecodecamp.org/images/SkR0qk59Nc-jKggp41TAHT8TQFairUfB5oKH)

Wikipedia a défini l'ASL comme suit :

> **L'american sign language** (**ASL**) est une [langue naturelle](https://en.wikipedia.org/wiki/Natural_language) qui sert de [langue des signes](https://en.wikipedia.org/wiki/Sign_language) prédominante dans les [communautés sourdes](https://en.wikipedia.org/wiki/Deaf_communities) aux États-Unis et dans la plupart de l'Anglophone Canada.

Tout d'abord, les données : il est vraiment important de se souvenir de la diversité des classes d'images en ce qui concerne des facteurs influents comme les conditions d'éclairage, les conditions de zoom, etc. Les [données Kaggle sur l'ASL](https://www.kaggle.com/grassknoted/asl-alphabet) contiennent toutes ces différentes variantes. L'entraînement sur de telles données garantit que notre modèle a une assez bonne connaissance de chaque classe. Alors, travaillons sur les [données Kaggle](https://www.kaggle.com/grassknoted/asl-alphabet).

Le jeu de données se compose des images des gestes de la main pour chaque lettre de l'alphabet anglais. Les images d'une seule classe sont de différentes variantes — c'est-à-dire des versions zoomées, des conditions de lumière tamisée et vive, etc. Pour chaque classe, il y a jusqu'à 3000 images. Considérons la classification des images "A", "B" et "C" dans notre travail pour simplifier. Voici les liens pour le code complet pour l'[entraînement](https://github.com/vagdevik/American-Sign-Language-Recognition-System/blob/master/2_AlexNet/asl_full.py) et les [tests](https://github.com/vagdevik/American-Sign-Language-Recognition-System/blob/master/2_AlexNet/predict_full.py).

![Image](https://cdn-media-1.freecodecamp.org/images/2Ja-bVTS-nR0ToERP8duawXQ2fFxG8RsH7GS)
_Une image pour la lettre 'A' du jeu de données_

Nous allons construire un [AlexNet](https://www.learnopencv.com/understanding-alexnet/) pour accomplir cette tâche de classification. Puisque nous entraînons le CNN, assurez-vous qu'il y a le support des ressources computationnelles comme le GPU.

Nous commençons par importer les modules nécessaires.

```
import warningswarnings.filterwarnings("ignore", category=DeprecationWarning) 
```

```
import osimport cv2import randomimport numpy as npimport kerasfrom random import shufflefrom keras.utils import np_utilsfrom shutil import unpack_archive
```

```
print("Modules importés...")
```

Téléchargez le fichier zip des données depuis [Kaggle data](https://www.kaggle.com/grassknoted/asl-alphabet). Maintenant, sélectionnons les images de gestes pour A, B et C et divisons les données obtenues en données d'entraînement, données de validation et données de test.

```
# chemin du dossier de donnéesdata_folder_path = "asl_data/new" files = os.listdir(data_folder_path) 
```

```
# mélange des images dans le dossierfor i in range(10):   shuffle(files)
```

```
print("Fichiers de données mélangés")
```

```
# dictionnaire pour maintenir les étiquettes numériquesclass_dic = {"A":0,"B":1,"C":2}
```

```
# dictionnaire pour maintenir les comptesclass_count = {'A':0,'B':0,'C':0}
```

```
# listes d'entraînementX = []Y = []
```

```
# listes de validationX_val = []Y_val = []
```

```
# listes de testX_test = []Y_test = []
```

```
for file_name in files:  label = file_name[0]  if label in class_dict:    path = data_folder_path+'/'+file_name    image = cv2.imread(path)    resized_image = cv2.resize(image,(224,224))    if class_count[label]<2000:      class_count[label]+=1      X.append(resized_image)      Y.append(class_dic[label])    elif class_count[label]>=2000 and class_count[label]<2750:      class_count[label]+=1      X_val.append(resized_image)      Y_val.append(class_dic[label])    else:      X_test.append(resized_image)      Y_test.append(class_dic[label])
```

Chaque image dans le jeu de données est nommée selon une convention de nommage. La 34ème image de la classe A est nommée "A_34.jpg". Par conséquent, nous considérons uniquement le premier élément du nom de la chaîne de fichier et vérifions s'il s'agit de la classe souhaitée.

De plus, nous divisons les images en fonction des comptes et stockons ces images dans les listes X et Y — X pour l'image, et Y pour les classes correspondantes. Ici, les comptes font référence au nombre d'images que nous souhaitons mettre dans les ensembles d'entraînement, de validation et de test respectivement. Donc ici, sur 3000 images pour chaque classe, j'ai mis 2000 images dans l'ensemble d'entraînement, 750 images dans l'ensemble de validation, et le reste dans l'ensemble de test.

Certaines personnes préfèrent également diviser en fonction de l'ensemble de données total (pas pour chaque classe comme nous l'avons fait ici), mais cela ne garantit pas que toutes les classes sont apprises correctement. Les images sont lues et stockées sous forme de tableaux Numpy dans les listes.

Maintenant, les listes d'étiquettes (les Y) sont encodées pour former des vecteurs one-hot numériques. Cela est fait par np_utils.to_categorical.

```
# encodages one-hot des classesY = np_utils.to_categorical(Y)Y_val = np_utils.to_categorical(Y_val)Y_test = np_utils.to_categorical(Y_test)
```

Maintenant, stockons ces images sous forme de fichiers .npy. Basiquement, nous créons des fichiers .npy séparés pour stocker les images appartenant à chaque ensemble.

```
if not os.path.exists('Numpy_folder'):    os.makedirs('Numpy_folder')
```

```
np.save(npy_data_path+'/train_set.npy',X)np.save(npy_data_path+'/train_classes.npy',Y)
```

```
np.save(npy_data_path+'/validation_set.npy',X_val)np.save(npy_data_path+'/validation_classes.npy',Y_val)
```

```
np.save(npy_data_path+'/test_set.npy',X_test)np.save(npy_data_path+'/test_classes.npy',Y_test)
```

```
print("Prétraitement des données réussi !")
```

Maintenant que nous avons terminé la partie de prétraitement des données, jetons un coup d'œil au code complet de prétraitement des données ici :

```
# preprocess.py
```

```
import warningswarnings.filterwarnings("ignore", category=DeprecationWarning)
```

```
import osimport cv2import randomimport numpy as npimport kerasfrom random import shufflefrom keras.utils import np_utilsfrom shutil import unpack_archive
```

```
print("Modules importés...")
```

```
# chemin du dossier de donnéesdata_folder_path = "asl_data/new" files = os.listdir(data_folder_path)
```

```
# mélange des images dans le dossierfor i in range(10):   shuffle(files)
```

```
print("Fichiers de données mélangés")
```

```
# dictionnaire pour maintenir les étiquettes numériquesclass_dic = {"A":0,"B":1,"C":2}
```

```
# dictionnaire pour maintenir les comptesclass_count = {'A':0,'B':0,'C':0}
```

```
# listes d'entraînementX = []Y = []
```

```
# listes de validationX_val = []Y_val = []
```

```
# listes de testX_test = []Y_test = []
```

```
for file_name in files:  label = file_name[0]  if label in class_dict:    path = data_folder_path+'/'+file_name    image = cv2.imread(path)    resized_image = cv2.resize(image,(224,224))    if class_count[label]<2000:      class_count[label]+=1      X.append(resized_image)      Y.append(class_dic[label])    elif class_count[label]>=2000 and class_count[label]<2750:      class_count[label]+=1      X_val.append(resized_image)      Y_val.append(class_dic[label])    else:      X_test.append(resized_image)      Y_test.append(class_dic[label])
```

```
# encodages one-hot des classesY = np_utils.to_categorical(Y)Y_val = np_utils.to_categorical(Y_val)Y_test = np_utils.to_categorical(Y_test)
```

```
if not os.path.exists('Numpy_folder'):    os.makedirs('Numpy_folder')
```

```
np.save(npy_data_path+'/train_set.npy',X)np.save(npy_data_path+'/train_classes.npy',Y)
```

```
np.save(npy_data_path+'/validation_set.npy',X_val)np.save(npy_data_path+'/validation_classes.npy',Y_val)
```

```
np.save(npy_data_path+'/test_set.npy',X_test)np.save(npy_data_path+'/test_classes.npy',Y_test)
```

```
print("Prétraitement des données réussi !")
```

Maintenant, passons à la partie entraînement ! Commençons par importer les modules essentiels afin que nous puissions construire et entraîner le CNN AlexNet. Ici, cela est principalement fait en utilisant Keras.

```
# importation depuis keras.optimizers import SGDfrom keras.models import Sequentialfrom keras.preprocessing import imagefrom keras.layers.normalization import BatchNormalizationfrom keras.layers import Dense, Activation, Dropout, Flatten,Conv2D, MaxPooling2D
```

```
print("Éléments essentiels du réseau importés")
```

Nous passons ensuite au chargement des images stockées sous forme de .npy :

```
X_train=np.load(npy_data_path+"/train_set.npy")Y_train=np.load(npy_data_path+"/train_classes.npy")
```

```
X_valid=np.load(npy_data_path+"/validation_set.npy")Y_valid=np.load(npy_data_path+"/validation_classes.npy")
```

```
X_test=np.load(npy_data_path+"/test_set.npy")Y_test=np.load(npy_data_path+"/test_classes.npy")
```

Nous passons ensuite à la définition de la structure de notre CNN. En supposant une connaissance préalable de l'architecture [AlexNet](https://www.learnopencv.com/understanding-alexnet/), voici le code Keras pour cela.

```
model = Sequential()
```

```
# 1ère couche de convolutionmodel.add(Conv2D(filters=96, input_shape=(224,224,3), kernel_size=(11,11),strides=(4,4), padding='valid'))model.add(Activation('relu'))
```

```
# Max Pooling model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2), padding='valid'))
```

```
# Normalisation par lots avant de le passer à la couche suivante model.add(BatchNormalization())
```

```
# 2ème couche de convolution model.add(Conv2D(filters=256, kernel_size=(11,11), strides=(1,1), padding='valid'))model.add(Activation('relu'))
```

```
# Max Pooling model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2), padding='valid'))
```

```
# Normalisation par lots model.add(BatchNormalization())
```

```
# 3ème couche de convolution model.add(Conv2D(filters=384, kernel_size=(3,3), strides=(1,1), padding='valid'))model.add(Activation('relu'))
```

```
# Normalisation par lots model.add(BatchNormalization())
```

```
# 4ème couche de convolution model.add(Conv2D(filters=384, kernel_size=(3,3), strides=(1,1), padding='valid'))model.add(Activation('relu'))
```

```
# Normalisation par lots model.add(BatchNormalization())
```

```
# 5ème couche de convolution model.add(Conv2D(filters=256, kernel_size=(3,3), strides=(1,1), padding='valid'))model.add(Activation('relu'))
```

```
# Max Pooling model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2), padding='valid'))
```

```
# Normalisation par lots model.add(BatchNormalization())
```

```
# Passage à une couche dense model.add(Flatten())
```

```
# 1ère couche dense model.add(Dense(4096, input_shape=(224*224*3,)))model.add(Activation('relu'))
```

```
# Ajout de Dropout pour éviter le surapprentissage model.add(Dropout(0.4))
```

```
# Normalisation par lots model.add(BatchNormalization())
```

```
# 2ème couche dense model.add(Dense(4096))model.add(Activation('relu'))
```

```
# Ajout de Dropout model.add(Dropout(0.6))
```

```
# Normalisation par lots model.add(BatchNormalization())
```

```
# 3ème couche dense model.add(Dense(1000))model.add(Activation('relu'))
```

```
# Ajout de Dropout model.add(Dropout(0.5))
```

```
# Normalisation par lots model.add(BatchNormalization())
```

```
# Couche de sortie model.add(Dense(24))model.add(Activation('softmax'))
```

```
model.summary()
```

Le modèle `Sequential` est une pile linéaire de couches. Nous ajoutons les couches de convolution (appliquant des filtres), les couches d'activation (pour la non-linéarité), les couches de max-pooling (pour l'efficacité computationnelle) et les couches de normalisation par lots (pour standardiser les valeurs d'entrée de la couche précédente à la couche suivante) et le motif est répété cinq fois.

La couche de normalisation par lots a été introduite en 2014 par Ioffe et Szegedy. Elle aborde le problème du gradient qui disparaît en standardisant la sortie de la couche précédente, elle accélère l'entraînement en réduisant le nombre d'itérations requises, et elle permet l'entraînement de réseaux de neurones plus profonds.

Enfin, 3 couches denses entièrement connectées ainsi que des dropouts (pour éviter le surapprentissage) sont ajoutées.

Pour obtenir la description résumée du modèle, utilisez model.summary().

Ce qui suit est le code pour la partie compilation du modèle. Nous définissons la méthode d'optimisation à suivre comme SGD et définissons les paramètres.

```
# Compile sgd = SGD(lr=0.001)
```

```
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
```

```
checkpoint = keras.callbacks.ModelCheckpoint("Checkpoint/weights.{epoch:02d}-{val_loss:.2f}.hdf5", monitor='val_loss', verbose=0, 
```

```
save_best_only=False, save_weights_only=False, mode='auto', period=1)
```

`lr` dans SGD est le taux d'apprentissage. Puisque cela est une classification catégorielle, nous utilisons categorical_crossentropy comme fonction de perte dans `model.compile`. Nous définissons l'optimiseur comme étant `sgd`, l'objet SGD que nous avons défini et définissons la métrique d'évaluation comme étant la précision.

Lors de l'utilisation du GPU, il peut parfois arriver que son exécution soit interrompue. L'utilisation de points de contrôle est le meilleur moyen de stocker les poids que nous avions obtenus jusqu'au point d'interruption, afin que nous puissions les utiliser plus tard. Le premier paramètre est de définir l'endroit pour stocker : sauvegardez-le sous `weights.{epoch:02d}-{val_loss:.2f}.hdf5` dans le dossier Checkpoints.

Enfin, nous sauvegardons le modèle au format json et les poids au format .h5. Ceux-ci sont ainsi sauvegardés localement dans les dossiers spécifiés.

```
# séquentialiser le modèle en JSON model_json = model.to_json()with open("Weights_Full/model.json", "w") as json_file:    json_file.write(model_json)
```

```
# séquentialiser les poids en HDF5 model.save_weights("Weights_Full/model_weights.h5")print("Modèle sauvegardé sur le disque")
```

Regardons tout le code de définition et d'entraînement du réseau. Considérez cela comme un fichier séparé 'training.py'.

```
# training.py
```

```
from keras.optimizers import SGDfrom keras.models import Sequentialfrom keras.preprocessing import imagefrom keras.layers.normalization import BatchNormalizationfrom keras.layers import Dense, Activation, Dropout, Flatten,Conv2D, MaxPooling2D
```

```
print("Éléments essentiels du réseau importés")
```

```
# chargement du jeu de données .npy X_train=np.load(npy_data_path+"/train_set.npy")Y_train=np.load(npy_data_path+"/train_classes.npy")
```

```
X_valid=np.load(npy_data_path+"/validation_set.npy")Y_valid=np.load(npy_data_path+"/validation_classes.npy")
```

```
X_test=np.load(npy_data_path+"/test_set.npy")Y_test=np.load(npy_data_path+"/test_classes.npy")
```

```
X_test.shape
```

```
model = Sequential()# 1ère couche de convolution model.add(Conv2D(filters=96, input_shape=(224,224,3), kernel_size=(11,11),strides=(4,4), padding='valid'))model.add(Activation('relu'))# Pooling model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2), padding='valid'))# Normalisation par lots avant de le passer à la couche suivante model.add(BatchNormalization())
```

```
# 2ème couche de convolution model.add(Conv2D(filters=256, kernel_size=(11,11), strides=(1,1), padding='valid'))model.add(Activation('relu'))# Pooling model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2), padding='valid'))# Normalisation par lots model.add(BatchNormalization())
```

```
# 3ème couche de convolution model.add(Conv2D(filters=384, kernel_size=(3,3), strides=(1,1), padding='valid'))model.add(Activation('relu'))# Normalisation par lots model.add(BatchNormalization())
```

```
# 4ème couche de convolution model.add(Conv2D(filters=384, kernel_size=(3,3), strides=(1,1), padding='valid'))model.add(Activation('relu'))# Normalisation par lots model.add(BatchNormalization())
```

```
# 5ème couche de convolution model.add(Conv2D(filters=256, kernel_size=(3,3), strides=(1,1), padding='valid'))model.add(Activation('relu'))# Pooling model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2), padding='valid'))# Normalisation par lots model.add(BatchNormalization())
```

```
# Passage à une couche dense model.add(Flatten())# 1ère couche dense model.add(Dense(4096, input_shape=(224*224*3,)))model.add(Activation('relu'))# Ajout de Dropout pour éviter le surapprentissage model.add(Dropout(0.4))# Normalisation par lots model.add(BatchNormalization())
```

```
# 2ème couche dense model.add(Dense(4096))model.add(Activation('relu'))# Ajout de Dropout model.add(Dropout(0.6))# Normalisation par lots model.add(BatchNormalization())
```

```
# 3ème couche dense model.add(Dense(1000))model.add(Activation('relu'))# Ajout de Dropout model.add(Dropout(0.5))# Normalisation par lots model.add(BatchNormalization())
```

```
# Couche de sortie model.add(Dense(24))model.add(Activation('softmax'))
```

```
model.summary()
```

```
# (4) Compile sgd = SGD(lr=0.001)model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])checkpoint = keras.callbacks.ModelCheckpoint("Checkpoint/weights.{epoch:02d}-{val_loss:.2f}.hdf5", monitor='val_loss', verbose=0, save_best_only=False, save_weights_only=False, mode='auto', period=1)# (5) Train model.fit(X_train/255.0, Y_train, batch_size=32, epochs=50, verbose=1,validation_data=(X_valid/255.0,Y_valid/255.0), shuffle=True,callbacks=[checkpoint])
```

```
# séquentialiser le modèle en JSON model_json = model.to_json()with open("Weights_Full/model.json", "w") as json_file:    json_file.write(model_json)# séquentialiser les poids en HDF5 model.save_weights("Weights_Full/model_weights.h5")print("Modèle sauvegardé sur le disque")
```

Lorsque nous exécutons le fichier training.py, nous obtenons quelque chose comme suit :

![Image](https://cdn-media-1.freecodecamp.org/images/QPaPyUKNcBciGmQDLii7chrt-EMmvZ3lDs7T)

Par exemple, en considérant la première époque de 12 (Epoch 1/12) :

* il a fallu 1852s pour compléter cette époque
* la perte d'entraînement était de 0.2441
* la précision était de 0.9098 sur les données de validation
* 0.0069 était la perte de validation, et
* 0.9969 était la précision de validation.

Ainsi, sur la base de ces valeurs, nous connaissons les paramètres des époques qui performant mieux, où arrêter l'entraînement, et comment ajuster les valeurs des hyperparamètres.

Maintenant, il est temps de tester !

```
# test.py
```

```
import warningswarnings.filterwarnings("ignore", category=DeprecationWarning) from keras.preprocessing import imageimport numpy as npfrom keras.models import model_from_jsonfrom sklearn.metrics import accuracy_score 
```

```
# dimensions de nos images image_size = 224 
```

```
# charger le modèle au format json with open('Model/model.json', 'r') as f:    model = model_from_json(f.read())    model.summary()model.load_weights('Model/model_weights.h5')model.load_weights('Weights/weights.250-0.00.hdf5') 
```

```
X_test=np.load("Numpy/test_set.npy")Y_test=np.load("Numpy/test_classes.npy")
```

```
Y_predict = model.predict(X_test)Y_predict = [np.argmax(r) for r in Y_predict]
```

```
Y_test = [np.argmax(r) for r in Y_test] 
```

```
print("##################")acc_score = accuracy_score(Y_test, Y_predict)print("Précision: " + str(acc_score))print("##################")
```

À partir du code ci-dessus, nous chargeons l'architecture du modèle sauvegardé et les meilleurs poids. De plus, nous chargeons les fichiers .npy (la forme Numpy de l'ensemble de test) et procédons à la prédiction de cet ensemble de test d'images. En bref, nous chargeons simplement l'architecture du modèle sauvegardé et lui attribuons les poids appris.

Maintenant, la fonction d'approximation ainsi que les coefficients appris (poids) sont prêts. Nous devons simplement le tester en alimentant le modèle avec les images de l'ensemble de test et en évaluant ses performances sur cet ensemble de test. L'une des métriques d'évaluation célèbres est la précision. La précision est donnée par `_accuracy_score_` de `sklearn.metrics`.

Merci d'avoir lu ! Bon apprentissage ! :)