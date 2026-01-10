---
title: Comment j'ai développé un C.N.N. qui reconnaît les émotions et intégré le top
  10 de Kaggle
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-01T12:21:33.000Z'
originalURL: https://freecodecamp.org/news/facial-emotion-recognition-develop-a-c-n-n-and-break-into-kaggle-top-10-f618c024faa7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*nPhyVOunxSkN76GrR2nECw.png
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Machine Learning
  slug: machine-learning
- name: neural networks
  slug: neural-networks
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment j'ai développé un C.N.N. qui reconnaît les émotions et intégré
  le top 10 de Kaggle
seo_desc: 'By Jerin Paul

  A baby starts to recognize its parents’ faces when it is just a couple of weeks
  old. As it grows, this innate ability improves. By the time it is a few months old,
  it starts to display social cues and is able to understand basic emotion...'
---

Par Jerin Paul

Un bébé commence à reconnaître les visages de ses parents lorsqu'il n'a que quelques semaines. En grandissant, cette capacité innée s'améliore. À l'âge de quelques mois, il commence à afficher des signaux sociaux et est capable de comprendre des émotions de base comme un sourire.

Grâce à des millions d'années d'évolution, nous sommes capables de nous comprendre sans utiliser un seul mot. Un simple regard suffit pour comprendre si une personne est abattue ou ravie. Eh bien, j'ai essayé d'apprendre aux ordinateurs à faire exactement cela. Cet article est un compte rendu détaillé de la manière dont toute l'expérience s'est déroulée. Suivez-moi pendant que nous recréons le réseau.

![Image](https://cdn-media-1.freecodecamp.org/images/PKZ128PL4nQ2RMRJ4MRuU7fLY-RijiHkyIH8)
_Image à des fins de représentation uniquement._

_Vas droit au but Paul, donne-moi le code._ Vous ne voulez pas de lecture fantaisiste ? Pas de problème. Vous pouvez trouver le code de ce projet [ici](https://github.com/AssiduousArchitect/Facial-Emotion-Recognition/blob/master/Emotion_Recognition(CNN)_FER2013.ipynb).

### Une brève introduction

> « Les meilleures et les plus belles choses du monde ne peuvent être ni vues ni même touchées. Elles doivent être senties avec le cœur » — **Helen Keller**

Hellen Keller a excellemment décrit l'essence des émotions humaines dans la citation mentionnée ci-dessus. Ce qui était autrefois réservé aux animaux ne leur est plus limité. L'apprentissage automatique se développe à un rythme vertigineux. L'avènement des réseaux de neurones convolutifs a été une percée et a changé la manière dont les ordinateurs « regardent » le monde.

Les expressions faciales ne sont rien de plus que l'arrangement des muscles du visage pour transmettre un certain état émotionnel à l'observateur. Les émotions peuvent être divisées en six grandes catégories — Colère, Dégoût, Peur, Bonheur, Tristesse, Surprise et Neutre. Dans ce projet de M.L., nous allons entraîner un modèle à différencier ces émotions.

![Image](https://cdn-media-1.freecodecamp.org/images/WxrDi7qPgW7iQIxnx5Ppr3WvpiWrWKID6S8V)
_Quelques différents types d'expressions faciales._

Nous allons entraîner un réseau de neurones convolutif en utilisant le jeu de données FER2013 et utiliser divers hyper-paramètres pour affiner le modèle. Nous allons l'entraîner sur [Google Colab](https://colab.research.google.com), qui est un projet de recherche créé pour diffuser l'éducation en ML. Ils vous alloueront certaines ressources comme un G.P.U. ou un T.P.U., et celles-ci peuvent être utilisées pour entraîner votre modèle plus rapidement. Le meilleur, c'est que c'est complètement gratuit.

### Un coup d'œil aux données

Nous allons commencer par télécharger le fichier FER2013.csv sur notre drive afin que nous puissions y accéder depuis Google Colab. Il y a 35 888 images dans ce jeu de données qui sont classées en six émotions. Le fichier de données contient 3 colonnes — Classe, Données d'image et Utilisation.

**Classe :** est un chiffre entre 0 et 6 et représente l'émotion illustrée dans l'image correspondante. Chaque émotion est mappée à un entier comme indiqué ci-dessous.

```
0 - 'Colère'1 - 'Dégoût'2 - 'Peur' 3 - 'Bonheur' 4 - 'Tristesse' 5 - 'Surprise'6 - 'Neutre'
```

**Données d'image :** est une chaîne de 2 304 nombres et ce sont les valeurs d'intensité des pixels de notre image, nous allons couvrir cela en détail dans un instant.

**Utilisation :** indique si les données correspondantes doivent être utilisées pour entraîner le réseau ou le tester.

#### Décomposer une image.

Comme nous le savons tous, les images sont composées de pixels et ces pixels ne sont rien de plus que des nombres. Les images colorées ont trois canaux de couleur — rouge, vert et bleu — et chaque canal est représenté par une grille (tableau à deux dimensions). Chaque cellule de la grille stocke un nombre entre 0 et 255 qui indique l'intensité de cette cellule.

![Image](https://cdn-media-1.freecodecamp.org/images/uQbNq15Y5ERHePR3iHaXM5Yj-eZpMM5X-srz)
_Ce que vous voyez (G) vs. ce qu'un ordinateur voit._

Lorsque ces trois canaux sont alignés ensemble, nous obtenons les images que nous voyons.

### Importation des bibliothèques nécessaires

```
%matplotlib inlineimport matplotlib.pyplot as plt
```

```
import numpy as npfrom keras.utils import to_categoricalfrom sklearn.model_selection import train_test_split
```

```
from keras.models import Sequential #Initialise notre modèle de réseau de neurones comme un réseau séquentielfrom keras.layers import Conv2D #Opération de convolutionfrom keras.layers.normalization import BatchNormalizationfrom keras.regularizers import l2from keras.layers import Activation#Applique la fonction d'activationfrom keras.layers import Dropout#Prévient le surapprentissage en convertissant aléatoirement quelques sorties en zérofrom keras.layers import MaxPooling2D # Fonction de maxpoolingfrom keras.layers import Flatten # Convertit les tableaux 2D en un vecteur linéaire 1Dfrom keras.layers import Dense # Réseau de neurones entièrement connecté régulierfrom keras import optimizersfrom keras.callbacks import ReduceLROnPlateau, EarlyStopping, TensorBoard, ModelCheckpointfrom sklearn.metrics import accuracy_score
```

### Définir le mécanisme de chargement des données

Maintenant, nous allons définir la fonction load_data() qui analysera efficacement le fichier de données, extraira les données nécessaires et les convertira ensuite en un format d'image utilisable.

Toutes les images de notre jeu de données sont de dimension 48x48. Comme ces images sont en niveaux de gris, il n'y a qu'un seul canal. Nous allons extraire les données d'image et les réorganiser en un tableau 48x48. Ensuite, les convertir en entiers non signés et les diviser par 255 pour normaliser les données. 255 est la valeur maximale possible d'une seule cellule. En divisant chaque élément par 255, nous nous assurons que toutes nos valeurs sont comprises entre 0 et 1.

Nous allons vérifier la colonne _Utilisation_ et stocker les données dans des listes séparées, une pour entraîner le réseau et l'autre pour le tester.

```
def load_data(dataset_path):
```

```
data = []  test_data = []  test_labels = []  labels =[]
```

```
  with open(dataset_path, 'r') as file:      for line_no, line in enumerate(file.readlines()):          if 0 < line_no <= 35887:            curr_class, line, set_type = line.split(',')            image_data = np.asarray([int(x) for x in line.split()]).reshape(48, 48)            image_data =image_data.astype(np.uint8)/255.0                        if (set_type.strip() == 'PrivateTest'):                            test_data.append(image_data)              test_labels.append(curr_class)            else:              data.append(image_data)              labels.append(curr_class)            test_data = np.expand_dims(test_data, -1)      test_labels = to_categorical(test_labels, num_classes = 7)      data = np.expand_dims(data, -1)         labels = to_categorical(labels, num_classes = 7)          return np.array(data), np.array(labels), np.array(test_data), np.array(test_labels)
```

Une fois nos données séparées, nous allons étendre les dimensions des données de test et d'entraînement d'une unité pour accommoder le canal. Ensuite, nous allons encoder en one-hot toutes les étiquettes en utilisant la fonction to_categorical() et retourner toutes les listes sous forme de tableaux _numpy_.

Nous allons charger les données en appelant la fonction load_data().

```
dataset_path = "/content/gdrive/My Drive/Colab Notebooks/Emotion Recognition/Data/fer2013.csv"
```

```
train_data, train_labels, test_data, test_labels = load_data(dataset_path)
```

```
print("Nombre d'images dans l'ensemble d'entraînement :", len(train_data))print("Nombre d'images dans l'ensemble de test :", len(test_data))
```

Nos données sont chargées et maintenant passons à la meilleure partie, la définition du réseau.

### Définition du modèle.

Nous allons utiliser Keras pour créer un réseau convolutif séquentiel. Cela signifie que notre réseau de neurones sera une pile linéaire de couches. Ce réseau aura les composants suivants :

1. Couches convolutives : Ces couches sont les éléments de base de notre réseau et calculent le produit scalaire entre leurs poids et les petites régions auxquelles elles sont liées. C'est ainsi que ces couches apprennent certaines caractéristiques de ces images.
2. Fonctions d'activation : sont celles qui sont appliquées aux sorties de toutes les couches du réseau. Dans ce projet, nous utiliserons deux fonctions — _Relu_ et _Softmax_.
3. Couches de pooling : Ces couches vont sous-échantillonner l'opération le long des dimensions. Cela aide à réduire les données spatiales et à minimiser la puissance de traitement requise.
4. Couches denses : Ces couches sont présentes à la fin d'un C.N.N. Elles prennent toutes les données de caractéristiques générées par les couches de convolution et prennent les décisions.
5. Couches de dropout : désactivent aléatoirement quelques neurones du réseau pour prévenir le surapprentissage.
6. Normalisation par lots : normalise la sortie d'une couche d'activation précédente en soustrayant la moyenne du lot et en divisant par l'écart-type du lot. Cela accélère le processus d'entraînement.

```
model.add(Conv2D(64, (3, 3), activation='relu', input_shape=(48, 48, 1), kernel_regularizer=l2(0.01)))model.add(Conv2D(64, (3, 3), padding='same',activation='relu'))model.add(BatchNormalization())model.add(MaxPooling2D(pool_size=(2,2), strides=(2, 2)))model.add(Dropout(0.5))    model.add(Conv2D(128, (3, 3), padding='same', activation='relu'))model.add(BatchNormalization())model.add(Conv2D(128, (3, 3), padding='same', activation='relu'))model.add(BatchNormalization())model.add(Conv2D(128, (3, 3), padding='same', activation='relu'))model.add(BatchNormalization())model.add(MaxPooling2D(pool_size=(2,2)))model.add(Dropout(0.5))    model.add(Conv2D(256, (3, 3), padding='same', activation='relu'))model.add(BatchNormalization())model.add(Conv2D(256, (3, 3), padding='same', activation='relu'))model.add(BatchNormalization())model.add(Conv2D(256, (3, 3), padding='same', activation='relu'))model.add(BatchNormalization())model.add(MaxPooling2D(pool_size=(2,2)))model.add(Dropout(0.5))    model.add(Conv2D(512, (3, 3), padding='same', activation='relu'))model.add(BatchNormalization())model.add(Conv2D(512, (3, 3), padding='same', activation='relu'))model.add(BatchNormalization())model.add(Conv2D(512, (3, 3), padding='same', activation='relu'))model.add(BatchNormalization())model.add(MaxPooling2D(pool_size=(2,2)))model.add(Dropout(0.5))    model.add(Flatten())model.add(Dense(512, activation='relu'))model.add(Dropout(0.5))model.add(Dense(256, activation='relu'))model.add(Dropout(0.5))model.add(Dense(128, activation='relu'))model.add(Dropout(0.5))model.add(Dense(64, activation='relu'))model.add(Dropout(0.5))model.add(Dense(7, activation='softmax'))
```

Nous allons compiler le réseau en utilisant l'optimiseur Adam et utiliser un taux d'apprentissage variable. Puisque nous traitons un problème de classification impliquant plusieurs catégories, nous utiliserons _categorical_crossentropy_ comme fonction de perte.

```
adam = optimizers.Adam(lr = learning_rate)
```

```
model.compile(optimizer = adam, loss = 'categorical_crossentropy', metrics = ['accuracy'])    print(model.summary()
```

#### Fonctions de rappel

Les fonctions de rappel sont celles qui sont appelées après chaque époque pendant le processus d'entraînement. Nous utiliserons les fonctions de rappel suivantes :

1. ReduceLROnPlateau : L'entraînement d'un réseau de neurones peut parfois atteindre un plateau et nous cessons de voir des progrès pendant cette phase. Par conséquent, cette fonction surveille la perte de validation pour détecter les signes d'un plateau et modifie ensuite le taux d'apprentissage par le facteur spécifié si un plateau est détecté.

```
lr_reducer = ReduceLROnPlateau(monitor='val_loss', factor=0.9, patience=3)
```

2. EarlyStopping : Parfois, les progrès s'arrêtent lors de l'entraînement d'un réseau de neurones et nous cessons de voir une amélioration de la précision de validation (dans ce cas). La plupart du temps, cela signifie que le réseau ne convergera pas davantage et qu'il n'y a aucun intérêt à continuer le processus d'entraînement. Cette fonction attend un nombre spécifié d'époques et termine l'entraînement si aucun changement dans le paramètre n'est trouvé.

```
early_stopper = EarlyStopping(monitor='val_acc', min_delta=0, patience=6, mode='auto')
```

3. ModelCheckpoint : L'entraînement des réseaux de neurones prend généralement beaucoup de temps et tout peut arriver pendant cette période, ce qui peut entraîner la perte de toutes les variables et poids. Créer des points de contrôle est une bonne habitude car cela sauvegarde votre modèle après chaque époque. Au cas où votre entraînement s'arrête, vous pouvez charger le point de contrôle et reprendre le processus.

```
checkpointer = ModelCheckpoint('/content/gdrive/My Drive/Colab Notebooks/Emotion Recognition/Model/weights.hd5', monitor='val_loss', verbose=1, save_best_only=True)
```

### Il est temps de s'entraîner

Tout notre travail acharné est sur le point d'être mis à l'épreuve. Mais avant d'ajuster le modèle, définissons quelques hyper-paramètres.

```
epochs = 100batch_size = 64learning_rate = 0.001
```

Nos données passeront à travers le modèle 100 fois et par lots de 64 images. Nous utiliserons 20 % de nos données d'entraînement pour valider le modèle après chaque époque.

```
model.fit(          train_data,          train_labels,          epochs = epochs,          batch_size = batch_size,          validation_split = 0.2,          shuffle = True,          callbacks=[lr_reducer, checkpointer, early_stopper]          )
```

Maintenant que le réseau est en cours d'entraînement, je vous suggère d'aller finir ce livre que vous avez commencé ou d'aller courir. Cela m'a pris environ une heure sur Google Colab.

### Tester le modèle

Vous vous souvenez de l'ensemble privé que nous avons stocké séparément ? C'était pour ce moment précis. C'est le moment de vérité et c'est ici que nous allons récolter les fruits de notre travail.

```
predicted_test_labels = np.argmax(model.predict(test_data), axis=1)test_labels = np.argmax(test_labels, axis=1)print ("Score de précision = ", accuracy_score(test_labels, predicted_test_labels))
```

Eh bien, les résultats sont revenus et nous avons obtenu 63,167 %. À première vue, ce n'est pas beaucoup, mais nous avons intégré la neuvième position de la [compétition Kaggle de reconnaissance des émotions faciales](https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge).

![Image](https://cdn-media-1.freecodecamp.org/images/luDy-IohSf6uUPKMqJEwQfufaNs0r0Bmu3iu)
_Ce n'est pas une grosse affaire cependant_

Maintenant, tapez-vous sur l'épaule et commencez à réfléchir aux moyens d'améliorer ce modèle. Nous pouvons utiliser de meilleurs hyper-paramètres ou créer une architecture de réseau différente pour obtenir des précisions plus élevées.

### Sauvegarder le modèle

Sauvegardez rapidement le modèle en utilisant _model_from_json_ de _keras.models_.

```
from keras.models import model_from_json
```

```
model_json = model.to_json()with open("/content/gdrive/My Drive/Colab Notebooks/Emotion Recognition/FERmodel.json", "w") as json_file:    json_file.write(model_json)# serialize weights to HDF5model.save_weights("/content/gdrive/My Drive/Colab Notebooks/Emotion Recognition/FERmodel.h5")print("Modèle sauvegardé sur le disque")
```

### Conclusion

Nous avons commencé par définir un mécanisme de chargement et charger les images. Ensuite, nous avons créé un ensemble d'entraînement et un ensemble de test. Puis nous avons défini un modèle et quelques fonctions de rappel. Nous avons passé en revue les composants de base d'un réseau de neurones convolutif et ensuite nous avons entraîné notre réseau.

J'ai étendu ce projet en créant une application Python capable de détecter les visages et de reconnaître leurs émotions en temps réel. Cela sera couvert dans un prochain article.

Nous venons d'accomplir quelque chose qui faisait partie de la science-fiction il y a quelques décennies. Pourtant, il reste beaucoup à apprendre. Internet nous fournit une pléthore d'informations pour créer et apprendre constamment. Que l'apprentissage ne cesse jamais.