---
title: Comment utiliser la classification sonore avec TensorFlow sur une plateforme
  IoT
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-07T06:25:51.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-sound-classification-with-tensorflow-on-an-iot-platform-8997eb7bbdef
coverImage: https://cdn-media-1.freecodecamp.org/images/1*16vqdagvRZYk1FNlJkgzwA.jpeg
tags:
- name: iot
  slug: iot
- name: Machine Learning
  slug: machine-learning
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: TensorFlow
  slug: tensorflow
seo_title: Comment utiliser la classification sonore avec TensorFlow sur une plateforme
  IoT
seo_desc: 'By Nikolay Khabarov

  Introduction

  There are many different projects and services for human speech recognition, such
  as Pocketsphinx, Google’s Speech API, and many others. Such applications and services
  recognize speech and transform it to text with pr...'
---

Par Nikolay Khabarov

### Introduction

Il existe de nombreux projets et services différents pour la reconnaissance de la parole humaine, tels que Pocketsphinx, l'API Speech de Google, et bien d'autres. De telles applications et services reconnaissent la parole et la transforment en texte avec une assez bonne précision. Mais aucun d'entre eux ne peut déterminer les différents sons capturés par le microphone. Qu'y avait-il sur l'enregistrement : de la parole humaine, des sons d'animaux, ou de la musique ?

Nous avons été confrontés à cette tâche et avons décidé d'enquêter et de construire quelques projets d'exemple qui seraient capables de classifier différents sons en utilisant des algorithmes d'apprentissage automatique.

Cet article décrit quels outils nous avons choisis, quels défis nous avons rencontrés, comment nous avons entraîné notre modèle pour TensorFlow, et comment exécuter notre projet open source.

Nous pouvons également fournir les résultats de la reconnaissance à [DeviceHive](https://devicehive.com/?utm_source=medium&utm_medium=social&utm_campaign=d-spring-2018) (la plateforme IoT) pour les utiliser dans des services cloud pour des applications tierces.

### Choix des outils et d'un modèle de classification

Tout d'abord, nous devions choisir quel logiciel fonctionnerait le mieux avec les réseaux neuronaux. La première solution appropriée que nous avons trouvée était [Python Audio Analysis](https://github.com/tyiannak/pyAudioAnalysis).

Le problème principal en apprentissage automatique est de trouver un bon ensemble de données d'entraînement. Il existe de nombreux ensembles de données pour la reconnaissance vocale et la classification musicale, mais pas beaucoup pour la classification de sons aléatoires. Après quelques recherches, nous avons trouvé l'ensemble de données [urban sound dataset](https://serv.cusp.nyu.edu/projects/urbansounddataset/).

Après quelques tests, nous avons été confrontés aux problèmes suivants :

* pyAudioAnalysis n'est pas assez flexible. Il ne prend pas une grande variété de paramètres, et certains d'entre eux sont calculés à la volée (par exemple, le nombre d'expériences d'entraînement basé sur le nombre d'échantillons — et vous ne pouvez pas modifier cela).
* L'ensemble de données ne contient que 10 classes, et toutes sont "urbaines".

La solution suivante que nous avons trouvée était [Google AudioSet](https://research.google.com/audioset/index.html). Il est basé sur des segments de vidéos YouTube étiquetés et peut être téléchargé dans deux formats :

1. Fichiers CSV décrivant, pour chaque segment, l'ID de la vidéo YouTube, l'heure de début, l'heure de fin, et une ou plusieurs étiquettes.
2. Caractéristiques audio extraites qui sont stockées sous forme de fichiers TensorFlow Record.

Ces caractéristiques sont compatibles avec les [modèles YouTube-8M](https://research.google.com/youtube8m/index.html). Cette solution utilise également le [modèle TensorFlow VGGish](https://github.com/tensorflow/models/tree/master/research/audioset) comme extracteur de caractéristiques. Il couvrait beaucoup de nos exigences et était donc le meilleur choix pour nous.

### Entraînement du modèle

La tâche suivante était de comprendre comment fonctionnait l'interface YouTube-8M. Elle est conçue pour fonctionner avec des vidéos, mais heureusement, elle peut également fonctionner avec de l'audio. Cette bibliothèque est assez flexible, mais elle a un nombre codé en dur de classes d'échantillons. Nous l'avons donc modifié un peu pour passer le nombre de classes en tant que paramètre.

YouTube-8M peut fonctionner avec des données de deux types : des caractéristiques agrégées et des caractéristiques de trame. Google AudioSet peut fournir des données sous forme de caractéristiques comme nous l'avons noté précédemment. Grâce à quelques recherches supplémentaires, nous avons découvert que les caractéristiques sont au format trame. Nous devions ensuite choisir le modèle à entraîner.

### Ressources, temps et précision

Les GPU sont un choix plus adapté pour l'apprentissage automatique que les CPU. Vous pouvez trouver plus d'informations à ce sujet [ici](https://docs.devicehive.com/blog/using-gpus-for-training-tensorflow-models?utm_source=medium&utm_medium=social&utm_campaign=d-spring-2018). Nous allons donc passer ce point et aller directement à notre configuration. Pour nos expériences, nous avons utilisé un PC avec une NVIDIA GTX 970 4GB.

Dans notre cas, le temps d'entraînement n'avait pas vraiment d'importance. Nous devons mentionner qu'une à deux heures d'entraînement suffisaient pour prendre une décision initiale sur le modèle choisi et sa précision.

Bien sûr, nous voulions obtenir la meilleure précision possible. Mais pour entraîner un modèle plus complexe (potentiellement meilleure précision), vous auriez besoin de plus de RAM (RAM vidéo dans le cas d'un GPU) pour le faire tenir.

### Choix du modèle

Une liste complète des modèles YouTube-8M avec descriptions est disponible [ici](https://github.com/google/youtube-8m#overview-of-models). Parce que nos données d'entraînement étaient au format trame, des modèles de niveau trame devaient être utilisés. Google AudioSet nous a fourni un ensemble de données divisé en trois parties : entraînement équilibré, entraînement non équilibré, et évaluation. Vous pouvez obtenir plus d'informations à leur sujet [ici](https://research.google.com/audioset/download.html).

Une version modifiée de YouTube-8M a été utilisée pour l'entraînement et l'évaluation. Elle est disponible [ici](https://github.com/igor-panteleev/youtube-8m).

#### Entraînement équilibré

La commande d'entraînement ressemble à ceci :

_python train.py --train_data_pattern=/path_to_data/audioset_v1_embeddings/bal_train/*.tfrecord --num_epochs=100 --learning_rate_decay_examples=400000 --feature_names=audio_embedding --feature_sizes=128 --frame_features --batch_size=512 --num_classes=527 --train_dir=/path_to_logs --model=ModelName_

Pour LstmModel, nous avons changé le taux d'apprentissage de base à 0,001 comme suggéré par la documentation. Nous avons également changé la valeur par défaut de lstm_cells à 256, car nous n'avions pas assez de RAM pour plus.

Voyons les résultats de l'entraînement :

![Image](https://cdn-media-1.freecodecamp.org/images/XCOCdLc0cQI-idVQaMZJPkD4yVVu4xNeg68X)

![Image](https://cdn-media-1.freecodecamp.org/images/K4emt0fRmPgqfvId9FUajvtqX8LRInBsMsW-)

Nom du modèleTemps d'entraînementPrécision à la dernière étape de l'entraînementPrécision moyenne de l'évaluationLogistic14m 3s0.58590.5560Dbof31m 46s1.00000.5220Lstm1h 45m 53s0.98830.4581

Comme vous pouvez le voir, nous avons obtenu de bons résultats lors de l'étape d'entraînement — mais cela ne signifie pas que nous obtiendrions de bons résultats sur l'évaluation complète.

#### Entraînement non équilibré

Ensuite, nous avons essayé l'ensemble de données d'entraînement non équilibré. Il contient beaucoup plus d'échantillons, nous avons donc changé le nombre d'époques d'entraînement à 10 (devrait être changé à 5 au moins, car cela a pris un temps significatif pour l'entraînement).

![Image](https://cdn-media-1.freecodecamp.org/images/8nZvatG0k1S5CEcwdyqdBgZ-UZjPBjugckO2)

![Image](https://cdn-media-1.freecodecamp.org/images/FyRyG3cgEDLLBErsYFLVuCdzIs7nx3CNHj-z)

Nom du modèleTemps d'entraînementPrécision à la dernière étape de l'entraînementPrécision moyenne de l'évaluationLogistic2h 4m 14s0.87500.5125Dbof4h 39m 29s0.88480.5605Lstm9h 42m 52s0.86910.5396

### Journaux d'entraînement

Si vous souhaitez examiner nos journaux d'entraînement, vous pouvez télécharger et extraire [train_logs.tar.gz](https://s3.amazonaws.com/audioanalysis/train_logs.tar.gz). Ensuite, exécutez _tensorboard --logdir /path_to_train_logs/_ et allez sur [http://127.0.0.1:6006](http://127.0.0.1:6006/)

### Plus sur l'entraînement

YouTube-8M prend de nombreux paramètres, et beaucoup d'entre eux affectent le processus d'entraînement.

Par exemple : Vous pouvez ajuster le taux d'apprentissage et le nombre d'époques qui changeront beaucoup le processus d'entraînement. Il existe également trois fonctions différentes pour le calcul de la perte et de nombreuses autres variables utiles que vous pouvez ajuster et changer pour améliorer les résultats.

### Utilisation du modèle entraîné avec des dispositifs de capture audio

Maintenant que nous avions quelques modèles entraînés, il était temps d'ajouter du code pour interagir avec eux.

### Capture du micro

Nous devions somehow capturer les données audio d'un microphone. Nous avons utilisé [PyAudio](https://pypi.python.org/pypi/PyAudio). Il fournit une interface simple et peut fonctionner sur la plupart des plateformes.

### Préparation du son

Comme nous l'avons mentionné précédemment, nous avons utilisé le modèle TensorFlow VGGish comme extracteur de caractéristiques. Voici une brève explication du processus de transformation :

L'exemple "aboiement de chien" de l'ensemble de données UrbanSound a été utilisé pour la visualisation.

Rééchantillonner l'audio à 16 kHz mono.

![Image](https://cdn-media-1.freecodecamp.org/images/dlg4HMB3eWMKr2pOHhb1iCOHSSZPAp8O6OqT)

Calculer le spectrogramme en utilisant les magnitudes de la Transformée de Fourier à Court Terme avec une taille de fenêtre de 25 ms, un saut de fenêtre de 10 ms, et une fenêtre périodique [Hann](https://en.wikipedia.org/wiki/Hann_function).

![Image](https://cdn-media-1.freecodecamp.org/images/yYd5JZ-tJpT2ZCal8zGAT-4uvY1JRUQMXfTS)

Calculer le spectrogramme mel en mappant le spectrogramme à 64 bins mel.

![Image](https://cdn-media-1.freecodecamp.org/images/6SmF-OY1w8zyZBnjCUCa5lrTGXmXF4Br138I)

Calculer le spectrogramme mel log stabilisé en appliquant log(mel-spectrum + 0.01) où un décalage est utilisé pour éviter de prendre le logarithme de zéro.

![Image](https://cdn-media-1.freecodecamp.org/images/y8K9mWTFdh3HcvfPwCbKrLlALa28FjNypSQG)

Ces caractéristiques ont ensuite été encadrées en exemples non superposés de 0,96 seconde, où chaque exemple couvre 64 bandes mel et 96 trames de 10 ms chacune.

Ces exemples ont ensuite été alimentés dans le modèle VGGish pour extraire les intégrations.

### Classification

Et enfin, nous avions besoin d'une interface pour alimenter les données dans le réseau neuronal et obtenir les résultats.

Nous avons utilisé l'interface YouTube-8M comme exemple, mais nous l'avons modifiée pour supprimer l'étape de sérialisation/désérialisation.

[Ici](https://github.com/devicehive/devicehive-audio-analysis) vous pouvez voir les résultats de notre travail. Examinons cela de plus près.

### Installation

PyAudio utilise libportaudio2 et portaudio19-dev, vous devez donc les installer pour le faire fonctionner.

Certaines bibliothèques Python sont requises. Vous pouvez les installer en utilisant pip.

_pip install -r requirements.txt_

Vous devez également télécharger et extraire l'archive à la racine du projet avec les modèles sauvegardés. Vous pouvez le trouver [ici](https://s3.amazonaws.com/audioanalysis/models.tar.gz).

### Exécution

Notre projet fournit trois interfaces à utiliser.

1. Traiter un fichier audio préenregistré

Exécutez simplement _python parse_file.py path_to_your_file.wav_ et vous verrez dans le terminal quelque chose comme _Speech: 0.75, Music: 0.12, Inside, large room or hall: 0.03_

Le résultat dépend du fichier d'entrée. Ces valeurs sont les prédictions faites par le réseau neuronal. Une valeur plus élevée signifie une plus grande chance que le fichier d'entrée appartienne à cette classe.

#### 2. Capturer et traiter les données du micro

_python capture.py_ démarre le processus qui capturera les données de votre micro indéfiniment. Il alimentera les données à l'interface de classification toutes les 5-7 secondes (par défaut). Vous pouvez voir les résultats dans l'exemple précédent.

Vous pouvez l'exécuter avec _--save_path=/path_to_samples_dir/_ et dans ce cas, toutes les données capturées seront stockées dans le répertoire fourni dans des fichiers _wav_. Cette fonction est utile si vous souhaitez essayer différents modèles avec le(s) même(s) exemple(s). Utilisez le paramètre _--help_ pour obtenir plus d'informations.

#### 3. Interface Web

_python daemon.py_ implémente une interface web simple qui est disponible sur [http://127.0.0.1:8000](http://127.0.0.1:8000/) par défaut. Nous avons utilisé le même code que pour l'exemple précédent. Vous pouvez voir les dix dernières prédictions sur la page des événements ([http://127.0.0.1:8000/events](http://127.0.0.1:8000/events)).

![Image](https://cdn-media-1.freecodecamp.org/images/8JLrA632a9pYZmgLBazB8yBU25LytjqBIpO9)

### Intégration du service IoT

Dernier point, mais non des moindres, l'intégration avec l'infrastructure IoT. Si vous exécutez l'interface web que nous avons mentionnée dans la section précédente, vous pouvez trouver l'état et la configuration du client DeviceHive sur la page d'accueil. Tant que le client est connecté, les prédictions seront envoyées à l'appareil spécifié sous forme de notifications.

![Image](https://cdn-media-1.freecodecamp.org/images/4GtwB2dk8FuGPKSd-xMmFLGj-vxb5-SMWdan)

### Conclusion

TensorFlow est un outil très flexible, comme vous pouvez le voir, et peut être utile dans de nombreuses applications d'apprentissage automatique comme la reconnaissance d'images et de sons. Avoir une telle solution avec une plateforme IoT vous permet de construire une solution intelligente sur une très large zone.

Les villes intelligentes pourraient utiliser cela à des fins de sécurité, en écoutant en continu les vitres brisées, les coups de feu et autres sons liés aux crimes. Même dans les forêts tropicales, une telle solution pourrait être utilisée pour suivre les animaux sauvages ou les oiseaux en analysant leurs voix.

La plateforme IoT peut livrer toutes ces notifications. Cette solution peut être installée sur des appareils locaux (bien qu'elle puisse encore être déployée quelque part en tant que service cloud) pour minimiser le trafic et les dépenses cloud. Elle peut également être personnalisée pour ne livrer que des notifications au lieu d'inclure l'audio brut. N'oubliez pas que ceci est un projet open source, alors n'hésitez pas à l'utiliser.

Écrit par Nikolay Khabarov, cofondateur de [DeviceHive](https://devicehive.com/?utm_source=medium&utm_medium=social&utm_campaign=d-spring-2018).