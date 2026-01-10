---
title: Comment jouer à Quidditch en utilisant l'API de détection d'objets de TensorFlow
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-26T16:34:35.000Z'
originalURL: https://freecodecamp.org/news/how-to-play-quidditch-using-the-tensorflow-object-detection-api-b0742b99065d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*BBePdi1BimXkPlh1pwO98g.jpeg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: Python
  slug: python
- name: 'tech '
  slug: tech
seo_title: Comment jouer à Quidditch en utilisant l'API de détection d'objets de TensorFlow
seo_desc: 'By Bharath Raj

  Deep Learning never ceases to amaze me. It has had a profound impact on several
  domains, beating benchmarks left and right.

  Image classification using convolutional neural networks (CNNs) is fairly easy today,
  especially with the adven...'
---

Par Bharath Raj

Le Deep Learning ne cesse de m'étonner. Il a eu un impact profond sur plusieurs domaines, battant des records à gauche et à droite.

La classification d'images utilisant des réseaux de neurones convolutifs (CNN) est assez facile aujourd'hui, surtout avec l'avènement de puissants wrappers front-end comme Keras avec un back-end TensorFlow. Mais que faire si vous voulez identifier plus d'un objet dans une image ?

Ce problème est appelé « localisation et détection d'objets ». Il est beaucoup plus difficile que la simple classification. En fait, jusqu'en 2015, la localisation d'images utilisant des CNN était très lente et inefficace. Consultez cet [article de blog](https://blog.athelas.com/a-brief-history-of-cnns-in-image-segmentation-from-r-cnn-to-mask-r-cnn-34ea83205de4) de Dhruv pour lire l'histoire de la détection d'objets en Deep Learning, si vous êtes intéressé.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Mj8WKVKf_RpiAsX3SC1ZdQ.png)
_Source : CS231n Lecture 8 (2016)_

**Ça a l'air cool. Mais est-ce difficile à coder ?**

Ne vous inquiétez pas, [l'API de détection d'objets de TensorFlow](https://github.com/tensorflow/models/tree/master/research/object_detection) vient à la rescousse ! Ils ont fait la plupart du travail difficile pour vous. Tout ce que vous avez à faire est de préparer le jeu de données et de définir quelques configurations. Vous pouvez entraîner votre modèle et l'utiliser pour l'inférence.

TensorFlow fournit également des modèles pré-entraînés, entraînés sur les jeux de données MS COCO, Kitti ou Open Images. Vous pourriez les utiliser tels quels, si vous souhaitez simplement les utiliser pour la détection d'objets standard. L'inconvénient est qu'ils sont prédéfinis. Ils ne peuvent prédire que les classes définies par les jeux de données.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZeDQGWRoERxO9dW9Sqgc_w.jpeg)
_L'API de détection d'objets de TensorFlow en action_

Mais, que faire si vous voulez détecter quelque chose qui **n'est pas** dans la liste possible des classes ? C'est le but de cet article de blog. Je vais vous guider à travers la création de votre propre programme de détection d'objets personnalisé, en utilisant un exemple amusant de Quidditch de l'univers Harry Potter ! (Pour tous les fans de Star Wars, voici un [article de blog similaire](https://medium.freecodecamp.org/tracking-the-millenium-falcon-with-tensorflow-c8c86419225e) que vous pourriez aimer).

### Pour commencer

Commencez par cloner mon dépôt GitHub, disponible [ici](https://github.com/thatbrguy/Object-Detection-Quidditch). Ce sera votre répertoire de base. Tous les fichiers mentionnés dans cet article de blog sont disponibles dans le dépôt.

Alternativement, vous pouvez cloner le dépôt [models](https://github.com/tensorflow/models) de TensorFlow. Si vous choisissez cette option, vous n'avez besoin que des dossiers nommés « slim » et « object_detection », alors n'hésitez pas à supprimer le reste. Ne renommez rien à l'intérieur de ces dossiers (sauf si vous êtes sûr que cela n'interférera pas avec le code).

### Dépendances

En supposant que vous avez installé TensorFlow, vous devrez peut-être installer quelques dépendances supplémentaires, que vous pouvez faire en exécutant la commande suivante dans le répertoire de base :

```
pip install -r requirements.txt
```

L'API utilise Protobufs pour configurer et entraîner les paramètres du modèle. Nous devons compiler les bibliothèques Protobuf avant de les utiliser. Tout d'abord, vous devez installer le compilateur Protobuf en utilisant la commande suivante :

```
sudo apt-get install protobuf-compiler
```

Maintenant, vous pouvez compiler les bibliothèques Protobuf en utilisant la commande suivante :

```
protoc object_detection/protos/*.proto --python_out=.
```

Vous devez ajouter le chemin de votre répertoire de base, ainsi que votre répertoire slim à votre variable de chemin Python. Notez que vous devez compléter cette étape chaque fois que vous ouvrez un nouveau terminal. Vous pouvez le faire en exécutant la commande suivante. Alternativement, vous pouvez l'ajouter à votre fichier ~/.bashrc pour automatiser le processus.

```
export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim
```

### Préparation des entrées

Mon objectif était assez simple. Je voulais construire un chercheur de Quidditch en utilisant TensorFlow. Plus précisément, je voulais écrire un programme pour localiser le vif d'or à chaque image.

Mais ensuite, j'ai décidé d'augmenter les enjeux. Et si j'essayais d'identifier toutes les pièces d'équipement mobiles utilisées dans le Quidditch ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*ml_9ni6QrX8I654Rnw1k2g.jpeg)
_Le Quidditch a trois objets mobiles (uniques). Deux cognards, un souaffle et un vif d'or._

Nous commençons par préparer le fichier **label_map.pbtxt**. Celui-ci contiendra tous les noms des labels cibles ainsi qu'un numéro d'identification pour chaque label. Notez que l'identifiant du label doit commencer à 1. Voici le contenu du fichier que j'ai utilisé pour mon projet.

```
item { id: 1 name: 'snitch'}
```

```
item { id: 2 name: 'quaffle'}
```

```
item { id: 3 name: 'bludger'}
```

Maintenant, il est temps de collecter le jeu de données.

Amusant ! Ou ennuyeux, selon vos goûts, mais c'est une tâche fastidieuse dans tous les cas.

J'ai collecté le jeu de données en échantillonnant toutes les images d'un clip vidéo de Harry Potter, en utilisant un petit extrait de code que j'ai écrit, en utilisant le framework OpenCV. Une fois cela fait, j'ai utilisé un autre extrait de code pour échantillonner aléatoirement **300 images** à partir du jeu de données. Les extraits de code sont disponibles dans **utils.py** dans mon dépôt GitHub [repo](https://github.com/thatbrguy/Object-Detection-Quidditch) si vous souhaitez faire de même.

Vous m'avez bien entendu. Seulement 300 images. Oui, mon jeu de données n'était pas énorme. C'est principalement parce que je ne peux pas me permettre d'annoter beaucoup d'images. Si vous le souhaitez, vous pouvez opter pour des services payants comme Amazon Mechanical Turk pour annoter vos images.

### Annotations

Chaque tâche de localisation d'images nécessite des annotations de vérité terrain. Les annotations utilisées ici sont des fichiers XML avec 4 coordonnées représentant l'emplacement de la boîte englobante entourant un objet, et son label. Nous utilisons le format Pascal VOC. Une annotation d'exemple ressemblerait à ceci :

```
<annotation>  <filename>182.jpg</filename>  <size>    <width>1280</width>    <height>586</height>    <depth>3</depth>  </size>  <segmented>0</segmented>  <object>    <name>bludger</name>    <bndbox>      <xmin>581</xmin>      <ymin>106</ymin>      <xmax>618</xmax>      <ymax>142</ymax>    </bndbox>  </object>  <object>    <name>quaffle</name>    <bndbox>      <xmin>127</xmin>      <ymin>406</ymin>      <xmax>239</xmax>      <ymax>526</ymax>    </bndbox>  </object></annotation>
```

Vous pourriez penser, « Dois-je vraiment passer par la douleur de taper manuellement les annotations dans des fichiers XML ? » Absolument pas ! Il existe des outils qui vous permettent d'utiliser une interface graphique pour dessiner des boîtes sur des objets et les annoter. Amusant ! **LabelImg** est un excellent outil pour les utilisateurs de Linux/Windows. Alternativement, **RectLabel** est un bon choix pour les utilisateurs de Mac.

Quelques notes de bas de page avant de commencer à collecter votre jeu de données :

* Ne renommez pas vos fichiers image après les avoir annotés. Le code essaie de rechercher une image en utilisant le nom de fichier spécifié à l'intérieur de votre fichier XML (que LabelImg remplit automatiquement avec le nom du fichier image). Assurez-vous également que vos fichiers **image** et **XML** ont le **même nom**.
* Assurez-vous de **redimensionner** les images à la taille souhaitée **avant** de commencer à les annoter. Si vous le faites plus tard, les annotations n'auront plus de sens et vous devrez mettre à l'échelle les valeurs d'annotation à l'intérieur des XML.
* LabelImg peut produire certains éléments supplémentaires dans le fichier XML (tels que <pose>, <truncated>, <path>). Vous n'avez pas besoin de les supprimer car ils n'interféreront pas avec le code.

Au cas où vous auriez fait une erreur, le fichier **utils.py** contient quelques fonctions utilitaires qui peuvent vous aider. Si vous voulez simplement essayer Quidditch, vous pourriez télécharger mon jeu de données annoté à la place. Les deux sont disponibles dans mon dépôt GitHub [repository](https://github.com/thatbrguy/Object-Detection-Quidditch).

Enfin, créez un fichier texte nommé **trainval**. Il doit contenir les noms de tous vos fichiers image/XML. Par exemple, si vous avez img1.jpg, img2.jpg et img1.xml, img2.xml dans votre jeu de données, votre fichier trainval.txt doit ressembler à ceci :

```
img1img2
```

Séparez votre jeu de données en deux dossiers, à savoir **images** et **annotations**. Placez le **label_map.pbtxt** et **trainval.txt** à l'intérieur de votre dossier annotations. Créez un dossier nommé **xmls** à l'intérieur du dossier annotations et placez tous vos XML à l'intérieur. Votre hiérarchie de répertoires doit ressembler à ceci :

```
-base_directory|-images|-annotations||-xmls||-label_map.pbtxt||-trainval.txt
```

L'API accepte les entrées au format de fichier **TFRecords**. Ne vous inquiétez pas, vous pouvez facilement convertir votre jeu de données actuel au format requis à l'aide d'une petite fonction utilitaire. Utilisez le fichier **create_tf_record.py** fourni dans mon dépôt pour convertir votre jeu de données en TFRecords. Vous devez exécuter la commande suivante dans votre répertoire de base :

```
python create_tf_record.py \    --data_dir=`pwd` \    --output_dir=`pwd`
```

Vous trouverez deux fichiers, **train.record** et **val.record**, après que le programme ait terminé son exécution. La division standard du jeu de données est de 70 % pour l'entraînement et 30 % pour la validation. Vous pouvez modifier la fraction de division dans la fonction main() du fichier si nécessaire.

### Entraînement du modèle

Ouf, c'était un processus plutôt long pour préparer les choses. La fin est presque proche. Nous devons sélectionner un modèle de localisation à entraîner. Le problème est qu'il y a tant d'options parmi lesquelles choisir. Chacun varie en performance en termes de vitesse ou de précision. Vous devez choisir le bon modèle pour le bon travail. Si vous souhaitez en savoir plus sur le compromis, cet [article](https://arxiv.org/abs/1611.10012) est une bonne lecture.

En bref, les SSDs sont rapides mais peuvent échouer à détecter des objets plus petits avec une précision décente, tandis que les Faster RCNNs sont relativement plus lents et plus grands, mais ont une meilleure précision.

L'API de détection d'objets de TensorFlow nous a fourni un ensemble de [modèles pré-entraînés](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md). Il est fortement recommandé d'initialiser l'entraînement en utilisant un modèle pré-entraîné. Cela peut réduire considérablement le temps d'entraînement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*WF_iKJBo9__XstR9_fwLFA.png)
_Un ensemble de modèles pré-entraînés sur le jeu de données MS COCO_

Téléchargez l'un de ces modèles et extrayez le contenu dans votre répertoire de base. Comme je me concentrais davantage sur la précision, mais que je voulais également un temps d'exécution raisonnable, j'ai choisi la version ResNet-50 du modèle Faster RCNN. Après extraction, vous recevrez les points de contrôle du modèle, un graphe d'inférence gelé et un fichier pipeline.config.

Une dernière chose reste à faire ! Vous devez définir le « travail d'entraînement » dans le fichier **pipeline.config**. Placez le fichier dans le répertoire de base. Ce qui compte vraiment, ce sont les dernières lignes du fichier — vous devez simplement définir les valeurs mises en évidence à vos emplacements de fichiers respectifs.

```
gradient_clipping_by_norm: 10.0  fine_tune_checkpoint: "model.ckpt"  from_detection_checkpoint: true  num_steps: 200000}train_input_reader {  label_map_path: "annotations/label_map.pbtxt"  tf_record_input_reader {    input_path: "train.record"  }}eval_config {  num_examples: 8000  max_evals: 10  use_moving_averages: false}eval_input_reader {  label_map_path: "annotations/label_map.pbtxt"  shuffle: false  num_epochs: 1  num_readers: 1  tf_record_input_reader {    input_path: "val.record"  }}
```

Si vous avez de l'expérience dans la définition des meilleurs hyperparamètres pour votre modèle, vous pouvez le faire. Les créateurs ont donné quelques directives plutôt brèves [ici](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/configuring_jobs.md).

Vous êtes prêt à entraîner votre modèle maintenant ! Exécutez la commande suivante pour démarrer le travail d'entraînement.

```
python object_detection/train.py \--logtostderr \--pipeline_config_path=pipeline.config \--train_dir=train
```

Le GPU de mon ordinateur portable ne pouvait pas gérer la taille du modèle (Nvidia 950M, 2 Go), donc j'ai dû l'exécuter sur le CPU à la place. Il a pris environ 7 à 13 secondes par étape sur mon appareil. Après environ 10 000 étapes éprouvantes, le modèle a atteint une assez bonne précision. J'ai arrêté l'entraînement après avoir atteint 20 000 étapes, uniquement parce que cela avait déjà pris deux jours.

Vous pouvez reprendre l'entraînement à partir d'un point de contrôle en modifiant l'attribut « fine_tune_checkpoint » de model.ckpt à model.ckpt-xxxx, où xxxx représente le numéro de l'étape globale du point de contrôle enregistré.

### Exportation du modèle pour l'inférence

Quel est l'intérêt d'entraîner le modèle si vous ne pouvez pas l'utiliser pour la détection d'objets ? L'API vient à la rescousse à nouveau ! Mais il y a un hic. Leur module d'inférence nécessite un modèle de graphe gelé en entrée. Ne vous inquiétez pas cependant : en utilisant la commande suivante, vous pouvez exporter votre modèle entraîné vers un modèle de graphe gelé.

```
python object_detection/export_inference_graph.py \--input_type=image_tensor \--pipeline_config_path=pipeline.config \--trained_checkpoint_prefix=train/model.ckpt-xxxxx \--output_directory=output
```

Propre ! Vous obtiendrez un fichier nommé **frozen_inference_graph.pb**, ainsi qu'un ensemble de fichiers de point de contrôle.

Vous pouvez trouver un fichier nommé **inference.py** dans mon [dépôt GitHub](https://github.com/thatbrguy/Object-Detection-Quidditch). Vous pouvez l'utiliser pour tester ou exécuter votre module de détection d'objets. Le code est assez explicite et similaire à la démonstration de détection d'objets présentée par les créateurs. Vous pouvez l'exécuter en tapant la commande suivante :

```
python object_detection/inference.py \--input_dir={PATH} \--output_dir={PATH} \--label_map={PATH} \--frozen_graph={PATH} \--num_output_classes={NUM}
```

Remplacez les caractères mis en évidence **{PATH}** par le nom de fichier ou le chemin du fichier/répertoire respectif. Remplacez **{NUM}** par le nombre d'objets que vous avez définis pour que votre modèle détecte (dans mon cas, 3).

### Résultats

Consultez ces vidéos pour voir ses performances par vous-même ! La première vidéo démontre la capacité du modèle à distinguer les trois objets, tandis que la deuxième vidéo met en avant sa prouesse en tant que chercheur.

Assez impressionnant, je dirais ! Il a un problème avec la distinction des têtes des objets de Quidditch. Mais compte tenu de la taille de notre jeu de données, la performance est assez bonne.

L'entraîner trop longtemps a conduit à un sur-ajustement massif (il n'était plus invariant à la taille), même si cela a réduit certaines erreurs. Vous pouvez surmonter cela en ayant un jeu de données plus grand.

Merci d'avoir lu cet article ! Appuyez sur ce bouton d'applaudissements si vous l'avez fait ! J'espère que cela vous a aidé à créer votre propre programme de détection d'objets. Si vous avez des questions, vous pouvez me contacter sur [LinkedIn](https://www.linkedin.com/in/bharathrajn/) ou m'envoyer un email (bharathrajn98@gmail.com).