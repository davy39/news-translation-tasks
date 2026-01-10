---
title: Suivre le Faucon Millenium avec TensorFlow
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-02T17:04:17.000Z'
originalURL: https://freecodecamp.org/news/tracking-the-millenium-falcon-with-tensorflow-c8c86419225e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*uCdxGFAuHpEwCmZ3iOIUaw.png
tags:
- name: AI
  slug: ai
- name: Machine Learning
  slug: machine-learning
- name: Python
  slug: python
- name: 'tech '
  slug: tech
- name: TensorFlow
  slug: tensorflow
seo_title: Suivre le Faucon Millenium avec TensorFlow
seo_desc: 'By Nick Bourdakos

  At the time of writing this post, most of the big tech companies (such as IBM, Google,
  Microsoft, and Amazon) have easy-to-use visual recognition APIs. Some smaller companies
  also provide similar offerings, such as Clarifai. But non...'
---

Par Nick Bourdakos

Au moment de la rédaction de cet article, la plupart des grandes entreprises technologiques (comme IBM, Google, Microsoft et Amazon) disposent d'API de reconnaissance visuelle faciles à utiliser. Certaines petites entreprises proposent également des offres similaires, comme [Clarifai](https://www.clarifai.com/). Mais aucune d'entre elles n'offre de détection d'objets.

> **Mise à jour :** IBM et Microsoft disposent désormais d'API de détection d'objets personnalisables.

Les images suivantes ont toutes deux été étiquetées à l'aide du même classificateur par défaut [Watson Visual Recognition](https://www.ibm.com/watson/services/visual-recognition/). La première, cependant, a été exécutée à travers un modèle de détection d'objets d'abord.

![Image](https://cdn-media-1.freecodecamp.org/images/1*uCdxGFAuHpEwCmZ3iOIUaw.png)
_[Commencez avec Watson](https://ibm.biz/Bdjh2m" rel="noopener" target="_blank" title=")_

La détection d'objets peut être bien supérieure à la reconnaissance visuelle seule. Mais si vous voulez de la détection d'objets, vous allez devoir vous retrousser les manches.

Selon votre cas d'utilisation, vous n'aurez peut-être pas besoin d'un modèle de détection d'objets personnalisé. L'API de détection d'objets de [TensorFlow](https://www.tensorflow.org/) fournit quelques modèles de vitesse et de précision variables, basés sur le [jeu de données COCO](http://cocodataset.org/#home).

Pour votre commodité, j'ai compilé une liste complète des objets détectables avec les modèles COCO :

![Image](https://cdn-media-1.freecodecamp.org/images/1*ka9VwFe4x7fGQ61WNGX8fQ.png)

Si vous souhaitez détecter des logos ou quelque chose qui ne figure pas sur cette liste, vous devrez construire votre propre détecteur d'objets personnalisé. Je voulais pouvoir détecter le Faucon Millenium et quelques chasseurs Tie. Il s'agit évidemment d'un cas d'utilisation extrêmement important, car on ne sait jamais...

### Annoter vos images

L'entraînement de votre propre modèle demande beaucoup de travail. À ce stade, vous pourriez penser : « Whoa, whoa, whoa ! Je ne veux pas faire tout ce travail ! » Si c'est le cas, vous pouvez consulter [mon autre article](https://medium.com/unsupervised-coding/dont-miss-your-target-object-detection-with-tensorflow-and-watson-488e24226ef3) sur l'utilisation du modèle fourni. C'est un trajet beaucoup plus fluide.

Vous devez collecter beaucoup d'images et les annoter toutes. Les annotations incluent la spécification des coordonnées de l'objet et une étiquette correspondante. Pour une image avec deux chasseurs Tie, une annotation pourrait ressembler à ceci :

```
<annotation>    <folder>images</folder>    <filename>image1.jpg</filename>    <size>        <width>1000</width>        <height>563</height>    </size>    <segmented>0</segmented>    <object>        <name>Tie Fighter</name>        <bndbox>            <xmin>112</xmin>            <ymin>281</ymin>            <xmax>122</xmax>            <ymax>291</ymax>        </bndbox>    </object>    <object>        <name>Tie Fighter</name>        <bndbox>            <xmin>87</xmin>            <ymin>260</ymin>            <xmax>95</xmax>            <ymax>268</ymax>        </bndbox>    </object></annotation>
```

Pour mon modèle Star Wars, j'ai collecté 308 images incluant deux ou trois objets dans chacune. Je recommande d'essayer de trouver 200 à 300 exemples de chaque objet.

« Wow », pourriez-vous penser, « je dois passer en revue des centaines d'images et écrire un tas de XML pour chacune ? »

Bien sûr que non ! Il existe de nombreux outils d'annotation, comme [labelImg](https://github.com/tzutalin/labelImg) et [RectLabel](https://rectlabel.com). J'ai utilisé [RectLabel](https://www.freecodecamp.org/news/tracking-the-millenium-falcon-with-tensorflow-c8c86419225e/undefined), mais il n'est disponible que pour macOS. C'est toujours beaucoup de travail, croyez-moi. Il m'a fallu environ trois ou quatre heures de travail non-stop pour annoter l'ensemble de mon jeu de données.

> **Mise à jour :** J'ai fini par créer mon propre outil pour annoter des images et des frames vidéo. C'est un outil en ligne gratuit appelé Cloud Annotations que vous pouvez consulter [ici](https://github.com/cloud-annotations/training).

Si vous avez de l'argent, vous pouvez payer quelqu'un d'autre, comme un stagiaire, pour le faire. Ou vous pouvez utiliser quelque chose comme [Mechanical Turk](https://www.mturk.com/mturk/welcome). Si vous êtes un étudiant fauché comme moi et/ou trouvez amusant de faire des heures de travail monotone, vous êtes seul.

Nous devons faire un peu de configuration avant de pouvoir exécuter le script pour préparer les données pour TensorFlow.

### Cloner le dépôt

Commencez par cloner mon dépôt [ici](https://github.com/bourdakos1/Custom-Object-Detection).

> **Mise à jour :** Ce dépôt est un peu obsolète, je recommande de consulter [celui-ci](https://github.com/cloud-annotations/training) pour une meilleure expérience :)

> **Note :** Les instructions suivantes sont également obsolètes, je vous invite à consulter [le nouveau guide](https://cloud-annotations.github.io/training/object-detection/cli/).

La structure du répertoire devra ressembler à ceci :

```
models|-- annotations|   |-- label_map.pbtxt|   |-- trainval.txt|   `-- xmls|       |-- 1.xml|       |-- 2.xml|       |-- 3.xml|       `-- ...|-- images|   |-- 1.jpg|   |-- 2.jpg|   |-- 3.jpg|   `-- ...|-- object_detection|   `-- ...`-- ...
```

J'ai inclus mes données d'entraînement, donc vous devriez pouvoir exécuter cela directement. Mais si vous voulez créer un modèle avec vos propres données, vous devrez ajouter vos images d'entraînement à `images`, ajouter vos annotations XML à `annotations/xmls`, mettre à jour `trainval.txt` et `label_map.pbtxt`.

`trainval.txt` est une liste de noms de fichiers qui nous permet de trouver et de corréler les fichiers JPG et XML. La liste suivante `trainval.txt` nous permettrait de trouver `abc.jpg`, `abc.xml`, `123.jpg`, `123.xml`, `xyz.jpg` et `xyz.xml` :

```
abc123xyz
```

**Note :** Assurez-vous que les noms de vos fichiers JPG et XML correspondent, à l'exception de l'extension.

`label_map.pbtxt` est notre liste d'objets que nous essayons de détecter. Elle devrait ressembler à ceci :

```
item {  id: 1  name: 'Millennium Falcon'}
```

```
item {  id: 2  name: 'Tie Fighter'}
```

### Exécuter le script

Tout d'abord, avec Python et pip installés, installez les dépendances du script :

```
pip install -r requirements.txt
```

Ajoutez `models` et `models/slim` à votre `PYTHONPATH` :

```
export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim
```

**Note importante :** Cela doit être exécuté chaque fois que vous ouvrez le terminal, ou ajouté à votre fichier `~/.bashrc`.

Exécutez le script :

```
python object_detection/create_tf_record.py
```

Une fois le script terminé, vous obtiendrez un fichier `train.record` et un fichier `val.record`. C'est ce que nous utiliserons pour entraîner le modèle.

### Télécharger un modèle de base

L'entraînement d'un détecteur d'objets à partir de zéro peut prendre des jours, même en utilisant plusieurs [GPUs](http://www.nvidia.com/object/what-is-gpu-computing.html). Pour accélérer l'entraînement, nous allons prendre un détecteur d'objets entraîné sur un autre jeu de données et réutiliser certains de ses paramètres pour initialiser notre nouveau modèle.

Vous pouvez télécharger un modèle à partir de ce [zoo de modèles](https://github.com/bourdakos1/Custom-Object-Detection/blob/master/object_detection/g3doc/detection_model_zoo.md). Chaque modèle varie en termes de précision et de vitesse. J'ai utilisé `faster_rcnn_resnet101_coco`.

Extrayez et déplacez tous les fichiers `model.ckpt` dans le répertoire racine de notre dépôt.

Vous devriez voir un fichier nommé `faster_rcnn_resnet101.config`. Il est configuré pour fonctionner avec le modèle `faster_rcnn_resnet101_coco`. Si vous avez utilisé un autre modèle, vous pouvez trouver un fichier de configuration correspondant [ici](https://github.com/bourdakos1/Custom-Object-Detection/tree/master/object_detection/samples/configs).

### Prêt à entraîner

Exécutez le script suivant, et il devrait commencer à s'entraîner !

```
python object_detection/train.py \        --logtostderr \        --train_dir=train \        --pipeline_config_path=faster_rcnn_resnet101.config
```

**Note :** Remplacez `pipeline_config_path` par l'emplacement de votre fichier de configuration.

```
global step 1:global step 2:global step 3:global step 4:...
```

Hourra ! Ça marche !

_10 minutes plus tard._

```
global step 41:global step 42:global step 43:global step 44:...
```

_L'ordinateur commence à fumer._

```
global step 71:global step 72:global step 73:global step 74:...
```

Combien de temps ce truc est censé tourner ?

Le modèle que j'ai utilisé dans la vidéo a tourné pendant environ 22 000 étapes.

Attendez, quoi ?!

J'utilise un MacBook Pro haut de gamme. Si vous exécutez cela sur quelque chose de similaire, je suppose que vous obtenez environ une étape toutes les 15 secondes. À ce rythme, il faudra environ trois à quatre jours de fonctionnement non-stop pour obtenir un modèle décent.

Bon, c'est stupide. Je n'ai pas le temps pour ça ?

[PowerAI](https://developer.ibm.com/linuxonpower/deep-learning-powerai/) à la rescousse !

### PowerAI

PowerAI nous permet d'entraîner notre modèle sur des systèmes IBM Power avec des GPUs P100 rapidement !

Il n'a fallu qu'environ une heure pour s'entraîner pendant 10 000 étapes. Cependant, cela n'était qu'avec un seul GPU. La vraie puissance de PowerAI réside dans la capacité de faire de l'apprentissage profond distribué sur des centaines de GPUs avec jusqu'à 95 % d'efficacité.

Avec l'aide de PowerAI, IBM vient de battre un nouveau record de reconnaissance d'images de 33,8 % de précision en 7 heures. Il a surpassé le précédent record de l'industrie établi par Microsoft — 29,9 % de précision en 10 jours.

BEAUCOUP plus rapide !

Puisque je ne m'entraîne pas sur des millions d'images, je n'avais définitivement pas besoin de ces ressources. Un seul GPU suffira.

#### Créer un compte Nimbix

Nimbix offre aux développeurs un compte d'essai avec dix heures de temps de traitement gratuit sur la plateforme PowerAI. Vous pouvez vous inscrire [ici](https://www.nimbix.net/cognitive-journey/).

**Note :** Ce processus n'est pas automatisé, il peut donc prendre jusqu'à 24 heures pour être examiné et approuvé.

Une fois approuvé, vous devriez recevoir un e-mail avec des instructions pour confirmer et créer votre compte. Il vous demandera un code promotionnel, mais laissez-le vide.

Vous devriez maintenant pouvoir vous connecter [ici](https://mc.jarvice.com).

#### Déployer l'application PowerAI Notebooks

Commencez par rechercher `PowerAI Notebooks`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*X41PZafFtX055NnbwBacEg.png)

Cliquez dessus, puis choisissez `TensorFlow`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*rFh7QVFGs_QzELReRFyAxQ.png)

Choisissez le type de machine `32 thread POWER8, 128GB RAM, 1x P100 GPU w/NVLink (np8g1)`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*I0ycKwK54z2MdSbuma05vg.png)

Une fois démarré, le panneau de tableau de bord suivant s'affichera. Lorsque le statut du serveur passe à `Processing`, le serveur est prêt à être accessible.

Obtenez le mot de passe en cliquant sur `(click to show)`.

Ensuite, cliquez sur `Click here to connect` pour lancer le Notebook.

![Image](https://cdn-media-1.freecodecamp.org/images/1*JLWTTJT4rUmxLN69lKdFaA.png)

Connectez-vous en utilisant le nom d'utilisateur `nimbix` et le mot de passe fourni précédemment.

![Image](https://cdn-media-1.freecodecamp.org/images/1*wXLlUuNvo_qPO-_p4kfjKA.png)

#### Commencer l'entraînement

Obtenez une nouvelle fenêtre de terminal en cliquant sur le menu déroulant `New` et en sélectionnant `Terminal`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*j8z6DLJgjyvH13-KXfMajQ.png)

Vous devriez être accueilli par une interface familière :

![Image](https://cdn-media-1.freecodecamp.org/images/1*XoGutc6f2nEC4lxexRO1Rw.png)

**Note :** Le terminal peut ne pas fonctionner dans Safari.

Les étapes pour l'entraînement sont les mêmes que lorsque nous avons exécuté cela localement. Si vous utilisez mes données d'entraînement, vous pouvez simplement cloner mon dépôt en exécutant (sinon, clonez simplement votre propre dépôt) :

```
git clone https://github.com/bourdakos1/Custom-Object-Detection.git
```

Ensuite, accédez au répertoire racine :

```
cd Custom-Object-Detection
```

Exécutez ce snippet, qui téléchargera le modèle pré-entraîné `faster_rcnn_resnet101_coco` que nous avons téléchargé précédemment.

```
wget http://storage.googleapis.com/download.tensorflow.org/models/object_detection/faster_rcnn_resnet101_coco_11_06_2017.tar.gztar -xvf faster_rcnn_resnet101_coco_11_06_2017.tar.gzmv faster_rcnn_resnet101_coco_11_06_2017/model.ckpt.* .
```

Ensuite, nous devons mettre à jour notre `PYTHONPATH` à nouveau, car cela se trouve dans un nouveau terminal :

```
export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim
```

Ensuite, nous pouvons enfin exécuter la commande d'entraînement à nouveau :

```
python object_detection/train.py \        --logtostderr \        --train_dir=train \        --pipeline_config_path=faster_rcnn_resnet101.config
```

#### Télécharger votre modèle

Quand mon modèle est-il prêt ? Cela dépend de vos données d'entraînement. Plus il y a de données, plus vous aurez besoin d'étapes. Mon modèle était assez solide à près de 4 500 étapes. Ensuite, à environ 20 000 étapes, il a atteint son pic. Je suis même allé jusqu'à l'entraîner pendant 200 000 étapes, mais il n'a pas obtenu de meilleurs résultats.

Je recommande de télécharger votre modèle toutes les 5 000 étapes environ et de l'évaluer pour vous assurer que vous êtes sur la bonne voie.

Cliquez sur le logo `Jupyter` dans le coin supérieur gauche. Ensuite, naviguez dans l'arborescence des fichiers jusqu'à `Custom-Object-Detection/train`.

Téléchargez tous les fichiers model.ckpt avec le numéro le plus élevé.

* `model.ckpt-STEP_NUMBER.data-00000-of-00001`
* `model.ckpt-STEP_NUMBER.index`
* `model.ckpt-STEP_NUMBER.meta`

**Note :** Vous ne pouvez en télécharger qu'un à la fois.

![Image](https://cdn-media-1.freecodecamp.org/images/1*2NUyMsF4SoVv1Jm0zMwc8Q.png)

**Note :** Assurez-vous de cliquer sur le bouton d'alimentation rouge de votre machine une fois terminé. Sinon, le compteur continuera à tourner indéfiniment.

#### Exporter le graphe d'inférence

Pour utiliser le modèle dans notre code, nous devons convertir les fichiers de point de contrôle (`model.ckpt-STEP_NUMBER.*`) en un graphe d'inférence gelé.

Déplacez les fichiers de point de contrôle que vous venez de télécharger dans le dossier racine du dépôt que vous avez utilisé.

Ensuite, exécutez cette commande :

```
python object_detection/export_inference_graph.py \        --input_type image_tensor \        --pipeline_config_path faster_rcnn_resnet101.config \        --trained_checkpoint_prefix model.ckpt-STEP_NUMBER \        --output_directory output_inference_graph
```

N'oubliez pas `export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim`.

Vous devriez voir un nouveau répertoire `output_inference_graph` avec un fichier `frozen_inference_graph.pb`. C'est le fichier dont nous avons besoin.

#### Tester le modèle

Maintenant, exécutez la commande suivante :

```
python object_detection/object_detection_runner.py
```

Il exécutera votre modèle de détection d'objets trouvé à `output_inference_graph/frozen_inference_graph.pb` sur toutes les images du répertoire `test_images` et sortira les résultats dans le répertoire `output/test_images`.

### Les résultats

Voici ce que nous obtenons lorsque nous exécutons notre modèle sur toutes les frames de cet extrait de Star Wars : Le Réveil de la Force.

Merci d'avoir lu ! Si vous avez des questions, n'hésitez pas à me contacter à bourdakos1@gmail.com, à vous connecter avec moi sur [LinkedIn](https://www.linkedin.com/in/nicholasbourdakos), ou à me suivre sur [Medium](https://medium.com/@bourdakos1) et [Twitter](https://twitter.com/bourdakos1).

Si vous avez trouvé cet article utile, cela signifierait beaucoup pour moi si vous lui donniez quelques applaudissements ? et le partagez pour aider les autres à le trouver ! Et n'hésitez pas à laisser un commentaire ci-dessous.