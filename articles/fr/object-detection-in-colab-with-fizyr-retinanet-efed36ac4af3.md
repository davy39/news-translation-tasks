---
title: Détection d'objets dans Colab avec Fizyr Retinanet
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-04T17:56:59.000Z'
originalURL: https://freecodecamp.org/news/object-detection-in-colab-with-fizyr-retinanet-efed36ac4af3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*g5nzQWVR79PK2vyznKgPAA.png
tags:
- name: Google Colab
  slug: google-colab
- name: keras
  slug: keras
- name: Machine Learning
  slug: machine-learning
- name: Python
  slug: python
- name: 'tech '
  slug: tech
seo_title: Détection d'objets dans Colab avec Fizyr Retinanet
seo_desc: 'By RomRoc

  Let’s continue our journey to explore the best machine learning frameworks in computer
  vision.

  In the first article we explored object detection with the official Tensorflow APIs.
  The second article was dedicated to an excellent framework f...'
---

Par RomRoc

Poursuivons notre voyage pour explorer les meilleurs frameworks de machine learning en vision par ordinateur.

Dans le [premier article](https://hackernoon.com/object-detection-in-google-colab-with-custom-dataset-5a7bb2b0e97e), nous avons exploré la détection d'objets avec les APIs officielles de Tensorflow. Le [deuxième article](https://hackernoon.com/instance-segmentation-in-google-colab-with-custom-dataset-b3099ac23f35) était dédié à un excellent framework pour la segmentation d'instances, Matterport Mask R-CNN basé sur Keras.

Dans cet article, nous examinons **l'implémentation Keras de la détection d'objets RetinaNet développée par [Fizyr](https://github.com/fizyr/keras-retinanet)**. RetinaNet, comme décrit dans [Focal Loss for Dense Object Detection](https://arxiv.org/abs/1708.02002), est l'état de l'art pour la détection d'objets. 
L'objet à détecter avec le modèle entraîné sera ma petite chèvre Rosa.

![Image](https://cdn-media-1.freecodecamp.org/images/gzJo8LgsXIrXkN2K65AGcJ6cfANG7XtNzsob)
_Détection d'objets avec Fizyr_

**Le notebook Colab et le jeu de données sont disponibles dans [mon dépôt Github](https://github.com/RomRoc/objdet_fizyr_colab).**

Dans cet article, nous passons par toutes les étapes dans un seul notebook Google Colab pour entraîner un modèle à partir d'un jeu de données personnalisé.

Nous garderons à l'esprit ces principes :

* illustrer comment faire le jeu de données d'annotation
* décrire toutes les étapes dans un seul notebook
* utiliser des logiciels gratuits, Google Colab et Google Drive, donc basé exclusivement sur des **_ressources cloud gratuites_**

À la fin de l'article, vous serez surpris par la simplicité d'utilisation et les bons résultats que nous obtiendrons grâce à ce framework de détection d'objets.

_Malgré sa facilité d'utilisation, Fizyr est un excellent framework, également utilisé par le [**gagnant**](https://www.kaggle.com/c/rsna-pneumonia-detection-challenge/discussion/70421) **du concours Kaggle** « RSNA Pneumonia Detection Challenge »._

### Création du jeu de données

Nous commençons par créer des annotations pour le jeu de données d'entraînement et de validation, en utilisant l'outil [**LabelImg**](https://github.com/tzutalin/labelImg). Cet excellent outil d'annotation vous permet d'annoter rapidement les boîtes englobantes des objets pour entraîner le modèle de machine learning.

![Image](https://cdn-media-1.freecodecamp.org/images/Id6MpAH6MV52QtprI-i9IcXRn7tIle0GQfsR)
_Outil d'annotation LabelImg_

LabelImg crée des annotations au format PascalVoc, nous devons donc convertir les annotations au format Fizyr :

* créer un fichier zip contenant les images du jeu de données d'entraînement et les annotations avec le même nom de fichier (vérifiez mon exemple de jeu de données sur Github)

```
objdet_dataset.zip|- img1.jpg|- img1.xml|- img2.jpg|- img2.xml...
```

* Télécharger le fichier zip dans Google Drive, obtenir l'ID du fichier Drive et substituer la valeur DATASET_DRIVEID
* Exécuter la cellule qui itère sur les fichiers xml et crée le fichier annotations.csv

_Note : vous pouvez voir [ma réponse](https://stackoverflow.com/a/48855034/9250875) sur Stackoverflow pour obtenir l'ID du fichier Drive._

### Entraînement du modèle

L'entraînement du modèle est le cœur du notebook. Fizyr offre divers paramètres, décrits dans [Github](https://github.com/fizyr/keras-retinanet/blob/c841da27f540084d27e971b6d00c178ff005d344/keras_retinanet/bin/train.py#L358), pour exécuter et optimiser cette étape.

Il est bon de commencer à partir d'un modèle pré-entraîné plutôt que d'entraîner un modèle à partir de zéro. Fizyr a publié un modèle basé sur l'architecture ResNet50, pré-entraîné sur le jeu de données Coco.

```
URL_MODEL = 'https://github.com/fizyr/keras-retinanet/releases/download/0.5.0/resnet50_coco_best_v2.1.0.h5'
```

Nous pouvons même utiliser notre modèle pré-entraîné et continuer l'entraînement à partir de celui-ci. Cette option est particulièrement utile pour entraîner pendant quelques époques, puis le sauvegarder dans Google Drive, et plus tard redémarrer l'entraînement à partir du modèle sauvegardé. De cette manière, nous pouvons contourner la limite d'exécution de 12 heures dans Colab, et nous pouvons entraîner le modèle pendant de nombreuses époques.

D'après mes tests, une valeur élevée de batch_size et steps offre de meilleurs résultats, mais ils augmentent considérablement le temps d'exécution de chaque époque.

![Image](https://cdn-media-1.freecodecamp.org/images/PntGODQ4dBvWoaqJGrEErgXfKuOiBRnGE8D8)
_Graphiques d'entraînement Tensorboard_

Nous pouvons commencer l'entraînement à partir de notre jeu de données personnalisé avec :

```
!keras_retinanet/bin/train.py --freeze-backbone --random-transform --weights {PRETRAINED_MODEL} --batch-size 8 --steps 500 --epochs 10 csv annotations.csv classes.csv
```

Analysons chaque argument passé au script train.py.

* freeze-backbone : fige les couches du backbone, particulièrement utile lorsque nous utilisons un petit jeu de données, pour éviter le surapprentissage
* random-transform : transforme aléatoirement le jeu de données pour obtenir une augmentation des données
* weights : initialise le modèle avec un modèle pré-entraîné (votre propre modèle ou un modèle publié par Fizyr)
* batch-size : taille du batch d'entraînement, une valeur plus élevée donne une courbe d'apprentissage plus lisse
* steps : nombre de steps pour les époques
* epochs : nombre d'époques à entraîner
* csv : fichiers d'annotations générés par le script ci-dessus

Le processus d'entraînement produit une description des couches et des métriques de perte pendant l'entraînement, et comme vous pouvez le voir, les métriques de perte diminuent pendant chaque époque :

```
Using TensorFlow backend....Layer (type)                    Output Shape         Param #     Connected toinput_1 (InputLayer)            (None, None, None, 3 0padding_conv1 (ZeroPadding2D)   (None, None, None, 3 0           input_1[0][0]                    ...Total params: 36,382,957Trainable params: 12,821,805Non-trainable params: 23,561,152NoneEpoch 1/10500/500 [==============================] - 1314s 3s/step - loss: 1.0659 - regression_loss: 0.6996 - classification_loss: 0.3663Epoch 2/10500/500 [==============================] - 1296s 3s/step - loss: 0.6747 - regression_loss: 0.5698 - classification_loss: 0.1048Epoch 3/10500/500 [==============================] - 1304s 3s/step - loss: 0.5763 - regression_loss: 0.5010 - classification_loss: 0.0753
```

```
Epoch 3/10500/500 [==============================] - 1257s 3s/step - loss: 0.5705 - regression_loss: 0.4974 - classification_loss: 0.0732
```

### Inférence

La dernière étape effectue l'inférence des images de test avec le modèle entraîné. 
Le framework Fizyr nous permet d'effectuer l'inférence en utilisant le CPU, même si vous avez entraîné le modèle avec le GPU. Cette fonctionnalité est importante dans les environnements de production typiques, où les gens optent généralement pour des infrastructures matérielles moins coûteuses pour l'inférence, sans GPU.

Examinons les lignes suivantes en détail :

```
model_path = os.path.join('snapshots', sorted(os.listdir('snapshots'), reverse=True)[0])print(model_path)
```

```
# load retinanet modelmodel = models.load_model(model_path, backbone_name='resnet50')model = models.convert_model(model)
```

La première ligne définit le fichier du modèle comme le dernier modèle généré par le processus d'entraînement dans le répertoire /snapshots. Ensuite, le modèle est chargé depuis le système de fichiers et converti pour exécuter l'inférence.

Vous pouvez changer les valeurs de THRES_SCORE, qui représente le seuil de confiance pour afficher une détection d'objet.

![Image](https://cdn-media-1.freecodecamp.org/images/mkkUoWpQY5-4mpXzEacDzy7bqP1QfGaVqUXZ)
_Inférence de détection d'objets_

### Conclusions

Nous avons parcouru le voyage complet pour faire de la détection d'objets avec l'implémentation Fizyr de RetinaNet. Nous avons créé un jeu de données, entraîné un modèle et exécuté l'inférence ([ici](https://github.com/RomRoc/objdet_fizyr_colab) se trouve mon dépôt Github pour le notebook et le jeu de données).

J'ai été impressionné par les aspects suivants de ce framework excellent :

* ce framework est **facile à utiliser** pour obtenir une bonne inférence, même sans beaucoup de personnalisation
* il était **simple de transformer les annotations** au format de jeu de données de Fizyr, comparé à d'autres frameworks.

En général, Fizyr est un bon choix pour démarrer un projet de détection d'objets, en particulier si vous avez besoin d'obtenir rapidement de bons résultats.

Si vous avez aimé cet article, laissez quelques applaudissements, cela m'encouragera à explorer d'autres opportunités de machine learning :)