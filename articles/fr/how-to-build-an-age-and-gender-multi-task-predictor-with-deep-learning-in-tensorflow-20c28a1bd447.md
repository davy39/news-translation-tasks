---
title: Comment construire un prédicteur multi-tâches d'âge et de genre avec l'apprentissage
  profond dans TensorFlow
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-12T17:21:07.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-an-age-and-gender-multi-task-predictor-with-deep-learning-in-tensorflow-20c28a1bd447
coverImage: https://cdn-media-1.freecodecamp.org/images/1*EU3eKPw1MxH_0HSkto9Pfg.jpeg
tags:
- name: Data Science
  slug: data-science
- name: Deep Learning
  slug: deep-learning
- name: Machine Learning
  slug: machine-learning
- name: technology
  slug: technology
- name: TensorFlow
  slug: tensorflow
seo_title: Comment construire un prédicteur multi-tâches d'âge et de genre avec l'apprentissage
  profond dans TensorFlow
seo_desc: 'By Cole Murray

  In my last tutorial, you learned about how to combine a convolutional neural network
  and Long short-term memory (LTSM) to create captions given an image. In this tutorial,
  you’ll learn how to build and train a multi-task machine learni...'
---

Par Cole Murray

[Dans mon dernier tutoriel](https://medium.freecodecamp.org/building-an-image-caption-generator-with-deep-learning-in-tensorflow-a142722e9b1f), vous avez appris comment combiner un réseau de neurones convolutionnel et une mémoire à long terme (LTSM) pour créer des légendes à partir d'une image. Dans ce tutoriel, vous apprendrez comment construire et entraîner un modèle d'apprentissage automatique multi-tâches pour prédire l'âge et le genre d'un sujet dans une image.

### **Aperçu**

* Introduction au modèle d'âge et de genre
* Construction d'un estimateur TensorFlow multi-tâches
* Entraînement

### Prérequis

* Compréhension de base des réseaux de neurones convolutionnels (CNN)
* Compréhension de base de TensorFlow
* GPU (optionnel)

### Introduction au modèle d'âge et de genre

En 2015, des chercheurs du Computer Vision Lab, D-ITET, ont publié un article [DEX](https://www.cv-foundation.org/openaccess/content_iccv_2015_workshops/w11/papers/Rothe_DEX_Deep_EXpectation_ICCV_2015_paper.pdf) et ont rendu public leur [IMDB-WIKI](https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/) composé de plus de 500 000 images de visages avec des étiquettes d'âge et de genre.

![Image](https://cdn-media-1.freecodecamp.org/images/0*qQJwCUF-vuGEAd0W.png)
_Jeu de données IMDB-WIKI source : [https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/](https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/" rel="noopener" target="_blank" title=")_

DEX décrit une architecture de réseau de neurones impliquant un modèle vgg16 pré-entraîné sur imagenet qui estime l'âge apparent dans les images de visages. DEX a remporté la première place à [ChaLearn LAP 2015](http://chalearnlap.cvc.uab.es/) — une compétition qui traite de la reconnaissance des personnes dans une image — surpassant la référence humaine.

#### **L'âge comme problème de classification**

Une méthode conventionnelle pour aborder un problème d'estimation d'âge avec une image en entrée serait d'utiliser un modèle basé sur la régression avec l'erreur quadratique moyenne comme fonction de perte. DEX modélise ce problème comme une tâche de classification, utilisant un classificateur softmax avec chaque âge représenté comme une classe unique allant de 1 à 101 et l'entropie croisée comme fonction de perte.

#### **Apprentissage multi-tâches**

L'apprentissage multi-tâches est une technique d'entraînement sur plusieurs tâches à travers une architecture partagée. Les couches au début du réseau apprendront une représentation généralisée commune, empêchant le surapprentissage pour une tâche spécifique qui peut contenir du bruit.

En entraînant avec un réseau multi-tâches, le réseau peut être entraîné en parallèle sur les deux tâches. Cela réduit la complexité de l'infrastructure à une seule pipeline d'entraînement. De plus, la puissance de calcul requise pour l'entraînement est réduite car les deux tâches sont entraînées simultanément.

![Image](https://cdn-media-1.freecodecamp.org/images/1*2aq7M6sgJ7bglCrvsredyA.png)
_CNN multi-tâches source : https://murraycole.com_

### Construction d'un réseau multi-tâches dans TensorFlow

Ci-dessous, vous utiliserez l'abstraction d'estimateur de TensorFlow pour créer le modèle. Le modèle sera entraîné à partir d'une entrée d'image brute pour prédire l'âge et le genre de l'image du visage.

#### **Structure du projet**

```
. Dockerfile age_gender_estimation_tutorial    cnn_estimator.py    cnn_model.py    dataset.py bin    download-imdb.sh    predict.py    preprocess_imdb.py    train.py requirements.txt
```

#### **Environnement**

Pour l'environnement, vous utiliserez [Docker](https://www.docker.com/) pour installer les dépendances. Une version GPU est également fournie pour plus de commodité.

```
docker build -t colemurray/age-gender-estimation-tutorial -f Dockerfile .
```

#### Données

Pour entraîner ce modèle, vous utiliserez le jeu de données IMDB-WIKI, composé de plus de 500 000 images. Pour simplifier, vous téléchargerez les images IMDB pré-recadrées (7 Go). Exécutez le script ci-dessous pour télécharger les données.

```
chmod +x bin/download-imdb-crop.sh
```

```
./bin/download-imdb-crop.sh
```

**Prétraitement**

Vous allez maintenant traiter le jeu de données pour éliminer les images de mauvaise qualité et recadrer l'entrée à une taille d'image fixe. De plus, vous allez formater les données en CSV pour simplifier la lecture dans TensorFlow.

```
docker run -v $PWD:/opt/app \-e PYTHONPATH=$PYTHONPATH:/opt/app \-it colemurray/age-gender-estimation-tutorial \python3 /opt/app/bin/preprocess_imdb.py \--db-path /opt/app/data/imdb_crop/imdb.mat \--photo-dir /opt/app/data/imdb_crop \--output-dir /opt/app/var \--min-score 1.0 \--img-size 224
```

Après environ 20 minutes, vous aurez un jeu de données traité.

Ensuite, vous utiliserez le module de pipeline de données de TensorFlow `tf.data` pour fournir des données à l'estimateur. `Tf.data` est une abstraction pour lire et manipuler un jeu de données en parallèle, utilisant des threads C++ pour la performance.

Ici, vous utiliserez le lecteur CSV de TensorFlow pour analyser les données, prétraiter les images, créer des lots et mélanger.

#### Modèle

Ci-dessous, vous allez créer un modèle CNN de base. Le modèle se compose de trois convolutions et de deux couches entièrement connectées, avec une tête de classificateur softmax pour chaque tâche.

#### Fonction de perte conjointe

Pour l'opération d'entraînement, vous utiliserez l'optimiseur Adam. Pour une fonction de perte, vous allez moyenner l'erreur d'entropie croisée de chaque tête, créant une fonction de perte partagée entre les têtes.

![Image](https://cdn-media-1.freecodecamp.org/images/1*GmnF07fG1hBbzjcxeNfSng.gif)
_fonction de perte conjointe pour l'âge et le genre_

#### Estimateur TensorFlow

Les estimateurs TensorFlow fournissent une abstraction simple pour la création de graphes et le traitement en temps réel. TensorFlow a spécifié une interface `model_fn`, qui peut être utilisée pour créer des estimateurs personnalisés.

Ci-dessous, vous allez prendre le réseau créé ci-dessus et créer l'entraînement, l'évaluation et la prédiction. Ces spécifications seront utilisées par la classe d'estimateur de TensorFlow pour modifier le comportement du graphe.

### Entraînement

Maintenant que vous avez prétraité les données et créé l'architecture du modèle et le pipeline de données, vous allez commencer à entraîner le modèle.

```
docker run -v $PWD:/opt/app \-e PYTHONPATH=$PYTHONPATH:/opt/app \-it colemurray/age-gender-estimation-tutorial:gpu \python3 /opt/app/bin/train.py \--img-dir /opt/app/var/crop \--train-csv /opt/app/var/train.csv \--val-csv /opt/app/var/val.csv \--model-dir /opt/app/var/cnn-model \--img-size 224 \--num-steps 200000
```

### Prédiction

Ci-dessous, vous allez charger votre modèle TensorFlow d'âge et de genre. Le modèle sera chargé depuis le disque et prédira sur l'image fournie.

```
# Mettez à jour le chemin du modèle ci-dessous avec votre modèle
docker run -v $PWD:/opt/app \-e PYTHONPATH=$PYTHONPATH:/opt/app \-it colemurray/age-gender-estimation-tutorial \python3 /opt/app/bin/predict.py \--image-path /opt/app/var/crop/25/nm0000325_rm2755562752_1956-1-7_2002.jpg \--model-dir /opt/app/var/cnn-model-3/serving/<TIMESTAMP>
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*wBuO3TbAEa98-0LeQWSBfA.jpeg)
_Prédiction : M/46 Réel : M/46_

### Conclusion

Dans ce tutoriel, vous avez appris comment construire et entraîner un réseau multi-tâches pour prédire l'âge et le genre d'un sujet. En utilisant une architecture partagée, les deux cibles peuvent être entraînées et prédites simultanément.

Prochaines étapes :

* Évaluer sur votre propre jeu de données
* Essayer une architecture de réseau différente
* Expérimenter avec différents hyperparamètres

Des questions/problèmes ? Ouvrez une issue [ici sur GitHub](https://github.com/ColeMurray/age-gender-estimation-tutorial/issues)

Code complet [ici](https://github.com/ColeMurray/age-gender-estimation-tutorial).

### Appel à l'action

Si vous avez aimé ce tutoriel, suivez et recommandez !

Intéressé à en apprendre plus sur l'apprentissage profond / l'apprentissage automatique ? Consultez mes autres tutoriels :

[- Construire un générateur de légendes d'images avec l'apprentissage profond dans TensorFlow](https://medium.freecodecamp.org/building-an-image-caption-generator-with-deep-learning-in-tensorflow-a142722e9b1f)

[- Construire un pipeline de reconnaissance faciale avec l'apprentissage profond dans TensorFlow](https://hackernoon.com/building-a-facial-recognition-pipeline-with-deep-learning-in-tensorflow-66e7645015b8)

[- CNN d'apprentissage profond dans TensorFlow avec GPU](https://medium.com/p/cba6efe0acc2)

[- Apprentissage profond avec Keras sur Google Compute Engine](https://medium.com/google-cloud/keras-inception-v3-on-google-compute-engine-a54918b0058)

[- Systèmes de recommandation avec Apache Spark sur Google Compute Engine](https://medium.com/google-cloud/recommendation-systems-with-spark-on-google-dataproc-bbb276c0dafd)

Autres endroits où vous pouvez me trouver :

[**Cole Murray (@_ColeMurray) | Twitter**](https://twitter.com/@_colemurray)  
[_Les derniers Tweets de Cole Murray (@_ColeMurray). Intérêts : Machine Learning, Big Data, Android, React/flux_twitter.com](https://twitter.com/@_colemurray)