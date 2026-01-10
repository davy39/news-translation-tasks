---
title: Comment déployer des modèles de Machine Learning sur mobile et appareils embarqués
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-12T19:21:10.000Z'
originalURL: https://freecodecamp.org/news/machine-learning-for-mobile-and-embedded-devices
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/1_D3HyTjQ_zA2uKTwTZgd0Pg.png
tags:
- name: Machine Learning
  slug: machine-learning
- name: TensorFlow
  slug: tensorflow
seo_title: Comment déployer des modèles de Machine Learning sur mobile et appareils
  embarqués
seo_desc: 'By Pier Paolo Ippolito

  Introduction

  Thanks to libraries such as Pandas, scikit-learn, and Matplotlib, it is relatively
  easy to start exploring datasets and make some first predictions using simple Machine
  Learning (ML) algorithms in Python. Although,...'
---

Par Pier Paolo Ippolito

## Introduction

Grâce à des bibliothèques telles que Pandas, scikit-learn et Matplotlib, il est relativement facile de commencer à explorer des ensembles de données et de faire quelques premières prédictions en utilisant des algorithmes simples de Machine Learning (ML) en Python. Cependant, pour rendre ces modèles entraînés utiles dans le monde réel, il est nécessaire de les rendre disponibles pour faire des prédictions sur le Web ou sur des appareils portables.

Dans deux de mes articles précédents, j'ai expliqué comment créer et déployer un modèle simple de Machine Learning en utilisant [Heroku/Flask](https://towardsdatascience.com/flask-and-heroku-for-online-machine-learning-deployment-425beb54a274) et [Tensorflow.js](https://towardsdatascience.com/online-machine-learning-with-tensorflow-js-2ae232352901). Aujourd'hui, je vais plutôt vous expliquer comment déployer des modèles de Machine Learning sur des smartphones et des appareils embarqués en utilisant TensorFlow Lite.

## TensorFlow Lite

TensorFlow Lite est une plateforme développée par Google pour entraîner des modèles de Machine Learning sur mobile, IoT (Internet des Objets) et appareils embarqués.

En utilisant TensorFlow Lite, tout le flux de travail est exécuté au sein de l'appareil, ce qui évite d'avoir à envoyer des données vers un serveur et vice versa. Certains des principaux avantages de cette approche sont :

* Une confidentialité accrue puisque les données n'ont pas à quitter l'appareil (ce qui peut vous permettre d'appliquer des techniques telles que la [Differential Privacy et Federated Learning](https://towardsdatascience.com/ai-differential-privacy-and-federated-learning-523146d46b85)).
* Une consommation d'énergie réduite, car aucune connexion Internet n'est requise.
* Une latence diminuée, puisque aucune communication avec le serveur n'est nécessaire.

TensorFlow Lite offre une prise en charge API pour différents langages tels que Python, Java, Swift et C++.

Un flux de travail typique utilisant TensorFlow Lite consisterait en :

1. Créer et entraîner un modèle de Machine Learning en Python en utilisant TensorFlow.
2. Convertir notre modèle dans un format adapté à TensorFlow Lite en utilisant le [converisseur TensorFlow Lite](https://www.tensorflow.org/lite/convert/index).
3. Déployer notre modèle de Machine Learning sur notre appareil mobile en utilisant l'[interpréteur TensorFlow Lite](https://www.tensorflow.org/lite/guide/inference).
4. Optimiser la consommation de mémoire et la précision du modèle.

Plusieurs techniques ont été développées au cours des dernières années afin de réduire la consommation de mémoire des modèles de Machine Learning [1]. Un exemple est la Quantification de Modèle.

La Quantification de Modèle vise à réduire :

1. Les représentations de précision des poids des réseaux de neurones artificiels (par exemple, convertir 34.3456657 en 34.3).
2. Les coûts d'accès à la mémoire pour la lecture et le stockage des fonctions d'activation intermédiaires.

L'utilisation de la Quantification de Modèle peut donc conduire à une réduction de la latence et de la taille du modèle. L'un des principaux inconvénients de cette technique est une légère diminution de la précision (qui peut être plus ou moins importante selon les applications).

Selon la documentation de TensorFlow Lite, en prenant l'exemple du classificateur d'images Inception_v3, l'utilisation de la Quantification de Modèle peut entraîner une diminution de la précision allant jusqu'à 0.8 %. En revanche, l'utilisation de la Quantification de Modèle a permis de réduire la taille du modèle par 4 (95.7 Mo contre 23.9 Mo) et la latence de 285 ms (1130 ms contre 845 ms) [2].

Dans l'exemple suivant, je vais démontrer comment utiliser un modèle pré-entraîné dans une application Android.

## Démonstration

En tant qu'exemple pratique, j'ai récemment créé une application Android Studio utilisant le classificateur d'images pré-entraîné Inception v3 grâce à TensorFlow Lite.

### Inception v3

Le classificateur Inception a été créé afin de résoudre certaines limitations apportées par la création de réseaux de neurones très grands et profonds pour les tâches de classification d'images.

Il y a quelques années, afin de résoudre les tâches de classification d'images, des modèles de deep learning composés d'un nombre toujours croissant de couches et de neurones dans chaque couche ont été créés. En adoptant cette approche, il était possible d'obtenir de meilleurs résultats, mais cela a également conduit à deux problèmes principaux :

1. Une augmentation de la puissance de calcul requise pour entraîner notre modèle.
2. Une probabilité croissante de surapprentissage (faire en sorte que notre modèle performe très bien pendant la phase d'entraînement mais moins bien lorsqu'il travaille avec des données entièrement nouvelles).

La création du classificateur Inception visait plutôt à résoudre ces problèmes en optimisant les caractéristiques du modèle, augmentant ainsi la vitesse d'entraînement. Au cours des dernières années, différentes versions du classificateur Inception ont été créées. Dans l'exemple suivant, j'ai décidé d'utiliser la version v3.

### Classificateur d'images Android

Afin de créer cette application, j'ai décidé d'utiliser Android Studio comme IDE. De cette manière, il a été relativement facile d'intégrer toutes les dépendances TensorFlow Lite nécessaires pour charger le modèle Inception v3.

J'ai ensuite décidé de diviser cette application en deux fenêtres principales :

* Dans la première, l'utilisateur est accueilli et est invité à sélectionner le classificateur d'images à utiliser (dans ce cas, le "Inception Quantized Classifier"). Ensuite, l'utilisateur est invité à prendre une photo de l'objet qu'il souhaite classifier et enfin, l'image est recadrée. Dans ce cas, il était nécessaire de recadrer l'image puisque le classificateur Inception prend uniquement des images carrées en entrée.
* Dans la deuxième fenêtre, l'utilisateur est finalement invité à cliquer sur le bouton "Classify Image" afin d'obtenir en retour les 3 prédictions les plus probables faites par le classificateur.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/ezgif.com-optimize.gif)
_Classificateur d'images Android simple_

Afin de réaliser ce projet, je me suis référé aux implémentations de Michael Shea et à la documentation TensorFlow Lite [3, 4].

Si vous êtes intéressé à tester cette application vous-même, tout le code et un APK de l'application sont disponibles dans [mon dépôt GitHub](https://github.com/pierpaolo28/Artificial-Intelligence-Projects/tree/master/Google%20AI%20tools/TensorFlow-Lite-Image-Classifier).

Si vous prévoyez de démarrer votre propre projet en utilisant TensorFlow Lite, leur [documentation](https://www.tensorflow.org/lite/guide/get_started) est probablement le meilleur endroit pour commencer.

## Contacts

Si vous souhaitez rester informé de mes derniers articles et projets, [suivez-moi](https://medium.com/@pierpaoloippolito28?source=post_page---------------------------) et abonnez-vous à ma [liste de diffusion](http://eepurl.com/gwO-Dr?source=post_page---------------------------). Voici quelques-unes de mes coordonnées :

* [Linkedin](https://uk.linkedin.com/in/pier-paolo-ippolito-202917146?source=post_page---------------------------)
* [Blog Personnel](https://pierpaolo28.github.io/blog/?source=post_page---------------------------)
* [Site Web Personnel](https://pierpaolo28.github.io/?source=post_page---------------------------)
* [Profil Medium](https://towardsdatascience.com/@pierpaoloippolito28?source=post_page---------------------------)
* [GitHub](https://github.com/pierpaolo28?source=post_page---------------------------)
* [Kaggle](https://www.kaggle.com/pierpaolo28?source=post_page---------------------------)

Photo de couverture [provenant de cet article](https://tipsmake.com/google-launched-tensorflow-lite-10-for-mobile-devices-and-embedded-devices).

## Bibliographie

[1] Nimit S. Sohoni, Christopher R. Aberger et al, Low-Memory Neural Network Training: A Technical Report. Consulté à l'adresse : [https://arxiv.org/pdf/1904.10631.pdf](https://arxiv.org/pdf/1904.10631.pdf)

[2] Optimisation de modèle, TensorFlow. Consulté à l'adresse : [https://www.tensorflow.org/lite/performance/model_optimization](https://www.tensorflow.org/lite/performance/model_optimization)

[3] Michael Shea, TensorFlow Lite Inception Model Android Tutorial. Consulté à l'adresse : [https://www.youtube.com/watch?v=8zQsAl2z4iU](https://www.youtube.com/watch?v=8zQsAl2z4iU)

[4] Documentation TensorFlow Lite, Exemple d'application Android de classification d'images TensorFlow Lite. Consulté à l'adresse : [https://github.com/tensorflow/examples/tree/master/lite/examples/image_classification/android](https://github.com/tensorflow/examples/tree/master/lite/examples/image_classification/android)