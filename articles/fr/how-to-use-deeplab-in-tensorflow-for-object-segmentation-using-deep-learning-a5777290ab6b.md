---
title: Comment utiliser DeepLab dans TensorFlow pour la segmentation d'objets avec
  le Deep Learning
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-24T20:20:58.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-deeplab-in-tensorflow-for-object-segmentation-using-deep-learning-a5777290ab6b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*mfz-HW5TIBU0AvprtApydQ.jpeg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Deep Learning
  slug: deep-learning
- name: image processing
  slug: image-processing
- name: 'tech '
  slug: tech
- name: TensorFlow
  slug: tensorflow
seo_title: Comment utiliser DeepLab dans TensorFlow pour la segmentation d'objets
  avec le Deep Learning
seo_desc: 'By Beeren Sahu

  Modifying the DeepLab code to train on your own dataset for object segmentation
  in images


  _Photo by [Unsplash](https://unsplash.com/photos/FmD8tIkf8bo?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText"
  rel="noopener" ...'
---

Par Beeren Sahu

#### Modifier le code DeepLab pour l'entraîner sur votre propre jeu de données pour la segmentation d'objets dans les images

![Image](https://cdn-media-1.freecodecamp.org/images/1*mfz-HW5TIBU0AvprtApydQ.jpeg)
_Photo par [Unsplash](https://unsplash.com/photos/FmD8tIkf8bo?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Nick Karvounis</a> sur <a href="https://unsplash.com/search/photos/images?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

Je travaille en tant que scientifique de la recherche chez [FlixStock](http://www.flixstock.com/), en me concentrant sur des solutions de Deep Learning pour générer et/ou éditer des images. Nous identifions des régions cohérentes appartenant à divers objets dans une image en utilisant la segmentation sémantique.

[DeepLab](https://arxiv.org/abs/1706.05587) est une solution idéale pour la segmentation sémantique. Le code est disponible dans TensorFlow.

Dans cet article, je vais partager comment nous pouvons entraîner un modèle de segmentation sémantique DeepLab pour notre propre jeu de données dans TensorFlow. Mais avant de commencer...

### Qu'est-ce que DeepLab ?

[DeepLab](https://arxiv.org/abs/1706.05587) est l'une des techniques les plus prometteuses pour la **segmentation sémantique d'images** avec le Deep Learning. La segmentation sémantique consiste à comprendre une image au niveau du pixel, puis à attribuer une étiquette à chaque pixel de l'image de sorte que les pixels avec la même étiquette partagent certaines caractéristiques.

### Installation

L'implémentation de DeepLab dans TensorFlow est disponible sur GitHub [ici](https://github.com/tensorflow/models/tree/master/research/deeplab).

### Préparation du jeu de données

Avant de créer votre propre jeu de données et d'entraîner DeepLab, vous devez être très clair sur ce que vous voulez faire avec. Voici les deux scénarios :

* Entraîner le modèle à partir de zéro : vous êtes libre d'avoir n'importe quel nombre de classes d'objets (nombre d'étiquettes) pour la segmentation. Cela nécessite un temps très long pour l'entraînement.
* Utiliser le modèle pré-entraîné : vous êtes libre d'avoir n'importe quel nombre de classes d'objets pour la segmentation. Utilisez le modèle pré-entraîné et mettez à jour uniquement les poids de votre classificateur avec l'apprentissage par transfert. Cela prendra beaucoup moins de temps pour l'entraînement par rapport au scénario précédent.

Nommons votre nouveau jeu de données « PQR ». Créez un nouveau dossier « PQR » comme suit : `tensorflow/models/research/deeplab/datasets/PQR`.

Pour commencer, tout ce dont vous avez besoin, ce sont des images d'entrée et leurs images pré-segmentées comme vérité terrain pour l'entraînement. Les images d'entrée doivent être des images en couleur et les images segmentées doivent être des images indexées en couleur. Référez-vous au jeu de données PASCAL.

Créez un dossier nommé « dataset » à l'intérieur de « PQR ». Il doit avoir la structure de répertoire suivante :

```
+ dataset    -JPEGImages    -SegmentationClass    -ImageSets+ tfrecord
```

#### JPEGImages

Il contient toutes les images couleur d'entrée au format `*.jpg`.

![Image](https://cdn-media-1.freecodecamp.org/images/0*M5PBchudNjWPqxPP.jpg)
_Une image d'entrée exemple du jeu de données PASCAL VOC_

#### SegmentationClass

Ce dossier contient toutes les images d'annotations de segmentation sémantique pour chacune des images d'entrée en couleur, qui est la vérité terrain pour la segmentation sémantique.

Ces images doivent être indexées en couleur. Chaque index de couleur représente une classe unique (avec une couleur unique) connue sous le nom de carte de couleur.

![Image](https://cdn-media-1.freecodecamp.org/images/0*OjQiFBSrKsYnZzGS.)
_Carte de couleur exemple [source : [https://github.com/DrSleep/tensorflow-deeplab-resnet](https://github.com/DrSleep/tensorflow-deeplab-resnet" rel="noopener" target="_blank" title=")]_

**Note :** Les fichiers dans le dossier « SegmentationClass » doivent avoir le même nom que dans le dossier « JPEGImage » pour la paire de fichiers image-segmentation correspondante.

![Image](https://cdn-media-1.freecodecamp.org/images/0*L3AEyxEId0-95rRq.png)
_Une image de vérité terrain de segmentation sémantique exemple du jeu de données PASCAL VOC_

#### ImageSets

Ce dossier contient :

* train.txt : liste des noms d'images pour l'ensemble d'entraînement
* val.txt : liste des noms d'images pour l'ensemble de validation
* trainval.txt : liste des noms d'images pour l'ensemble d'entraînement + validation

Un fichier `*.txt` exemple ressemble à ceci :

```
pqr_000032pqr_000039pqr_000063pqr_000068pqr_000121
```

#### Supprimer la carte de couleur dans les annotations de vérité terrain

Si vos images d'annotation de segmentation sont des images RGB au lieu d'images indexées en couleur. Voici un script Python qui sera utile.

Ici, la palette définit la paire « RGB:LABEL ». Dans ce code exemple (0,0,0):0 est l'arrière-plan et (255,0,0):1 est la classe de premier plan. Notez que new_label_dir est l'emplacement où les données de segmentation brutes sont stockées.

Ensuite, la tâche consiste à convertir le jeu de données d'images en un enregistrement TensorFlow. Faites une nouvelle copie du fichier de script `./dataset/download_and_convert_voc2012.sh` sous le nom `./dataset/convert_pqr.sh`. Voici le script modifié.

Le jeu de données converti sera enregistré dans `./deeplab/datasets/PQR/tfrecord`

#### Définir la description du jeu de données

Ouvrez le fichier **segmentation_dataset.py** présent dans le dossier **research/deeplab/datasets/**. Ajoutez le segment de code suivant définissant la description pour votre jeu de données PQR.

```
_PQR_SEG_INFORMATION = DatasetDescriptor(    splits_to_sizes={        'train': 11111, # nombre de fichiers dans le dossier train        'trainval': 22222,        'val': 11111,    },    num_classes=2, # nombre de classes dans votre jeu de données    ignore_label=255, # bords blancs qui seront ignorés pour être classés)
```

Apportons les modifications suivantes comme montré ci-dessous :

```
_DATASETS_INFORMATION = {    'cityscapes': _CITYSCAPES_INFORMATION,    'pascal_voc_seg': _PASCAL_VOC_SEG_INFORMATION,    'ade20k': _ADE20K_INFORMATION,    'pqr': _PQR_SEG_INFORMATION}
```

### Entraînement

Pour entraîner le modèle sur votre jeu de données, vous devez exécuter le fichier train.py dans le dossier **research/deeplab/**. Nous avons donc écrit un fichier de script train-pqr.sh pour effectuer cette tâche pour vous.

Ici, nous avons utilisé xception_65 pour votre entraînement local. Vous pouvez spécifier le nombre d'itérations d'entraînement à la variable NUM_ITERATIONS. et définir « --tf_initial_checkpoint » à l'emplacement où vous avez téléchargé ou pré-entraîné le modèle *.ckpt. Après l'entraînement, le modèle final entraîné peut être trouvé dans le répertoire TRAIN_LOGDIR.

Enfin, exécutez le script ci-dessus à partir du répertoire .../research/deeplab.

```
# sh ./train-pqr.sh
```

Voilà ! Vous avez réussi à entraîner DeepLab sur votre jeu de données.

Dans les mois à venir, je partagerai davantage de mes expériences avec les Images et le Deep Learning. Restez à l'écoute et n'oubliez pas de partager quelques applaudissements si vous aimez cet article. Cela m'encouragera énormément.