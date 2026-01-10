---
title: Création d'un générateur de légendes d'images avec l'apprentissage profond
  dans Tensorflow
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-11T15:03:07.000Z'
originalURL: https://freecodecamp.org/news/building-an-image-caption-generator-with-deep-learning-in-tensorflow-a142722e9b1f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*YzdxLQkXFqpdiLVeeLJhpw.jpeg
tags:
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Création d'un générateur de légendes d'images avec l'apprentissage profond
  dans Tensorflow
seo_desc: 'By Cole Murray

  In my last tutorial, you learned how to create a facial recognition pipeline in
  Tensorflow with convolutional neural networks. In this tutorial, you’ll learn how
  a convolutional neural network (CNN) and Long Short Term Memory (LSTM) ca...'
---

Par Cole Murray

Dans mon [dernier tutoriel](https://hackernoon.com/building-a-facial-recognition-pipeline-with-deep-learning-in-tensorflow-66e7645015b8), vous avez appris à créer un pipeline de reconnaissance faciale dans Tensorflow avec des réseaux de neurones convolutifs. Dans ce tutoriel, vous apprendrez comment un **réseau de neurones convolutif** (CNN) et une **mémoire à long court terme** (LSTM) peuvent être combinés pour créer un générateur de légendes d'images et générer des légendes pour vos propres images.

### Aperçu

* Introduction à l'architecture du modèle de légende d'image
* Légendes en tant que problème de recherche
* Création de légendes dans Tensorflow

#### Prérequis

* Compréhension de base des réseaux de neurones convolutifs
* Compréhension de base des LSTM
* Compréhension de base de Tensorflow

### Introduction à l'architecture du modèle de légende d'image

#### Combinaison d'un CNN et d'un LSTM

En 2014, des chercheurs de Google ont publié un article, [Show And Tell: A Neural Image Caption Generator](https://arxiv.org/pdf/1411.4555.pdf). À l'époque, cette architecture était à la pointe de la technologie sur le jeu de données MSCOCO. Elle utilisait un CNN + LSTM pour prendre une image en entrée et produire une légende.

![Image](https://cdn-media-1.freecodecamp.org/images/1*E90mI7YT9F0J6b9EadxfzA.png)
_Une architecture de légende d'image CNN-LSTM [source](https://arxiv.org/pdf/1411.4555.pdf" rel="noopener" target="_blank" title=")_

#### Utilisation d'un CNN pour l'intégration d'images

Un réseau de neurones convolutif peut être utilisé pour créer un vecteur de caractéristiques dense. Ce vecteur dense, également appelé intégration, peut être utilisé comme entrée de caractéristiques dans d'autres algorithmes ou réseaux.

Pour un modèle de légende d'image, cette intégration devient une représentation dense de l'image et sera utilisée comme état initial du LSTM.

![Image](https://cdn-media-1.freecodecamp.org/images/1*tCeGt4fuK_gX1fh8OSyz1Q.png)
_Mappage de l'entrée à l'intégration [source](https://www.slideshare.net/BhaskarMitra3/vectorland-brief-notes-from-using-text-embeddings-for-search" rel="noopener" target="_blank" title=")_

#### LSTM

Un LSTM est une architecture de réseau de neurones récurrents qui est couramment utilisée dans les problèmes avec des dépendances temporelles. Il réussit à capturer des informations sur les états précédents pour mieux informer la prédiction actuelle grâce à son état de cellule mémoire.

Un LSTM se compose de trois principaux composants : une porte d'oubli, une porte d'entrée et une porte de sortie. Chacune de ces portes est responsable de la modification des mises à jour de l'état de mémoire de la cellule.

![Image](https://cdn-media-1.freecodecamp.org/images/1*J5W8FrASMi93Z81NlAui4w.png)
_Un LSTM déroulé [source](https://colah.github.io/posts/2015-08-Understanding-LSTMs/" rel="noopener" target="_blank" title=")_

Pour une compréhension plus approfondie des LSTM, visitez [l'article de Chris Olah](https://colah.github.io/posts/2015-08-Understanding-LSTMs/).

#### **Prédiction avec l'image comme état initial**

Dans un modèle de langage de phrase, un LSTM prédit le mot suivant dans une phrase. De même, dans un modèle de langage de caractères, un LSTM essaie de prédire le caractère suivant, étant donné le contexte des caractères précédemment vus.

![Image](https://cdn-media-1.freecodecamp.org/images/1*VWHR9w-zv8d20TRGs7DUFQ.png)
_Prédictions de modèle de phrase et de caractères [source](https://www.youtube.com/watch?v=UXW6Cs82UKo" rel="noopener" target="_blank" title=")_

Dans un modèle de légende d'image, vous allez créer une intégration de l'image. Cette intégration sera ensuite alimentée comme état initial dans un LSTM. Cela devient le premier état précédent du modèle de langage, influençant les mots prédits suivants.

À chaque étape, le LSTM considère l'état précédent de la cellule et produit une prédiction pour la valeur suivante la plus probable dans la séquence. Ce processus est répété jusqu'à ce que le jeton de fin soit échantillonné, signalant la fin de la légende.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Y4p7N71LK38smrjVsMyhiw.png)
_Échantillonnage de caractères à partir d'un LSTM. [source](https://www.youtube.com/watch?v=UXW6Cs82UKo" rel="noopener" target="_blank" title=")_

### **Légendes en tant que problème de recherche**

La génération d'une légende peut être vue comme un problème de recherche de graphe. Ici, les nœuds sont des mots. Les arêtes sont la probabilité de passer d'un nœud à un autre. Trouver le chemin optimal implique de maximiser la probabilité totale d'une phrase.

L'échantillonnage et le choix de la valeur suivante la plus probable est une approche [gloutonne](https://en.wikipedia.org/wiki/Greedy_algorithm) pour générer une légende. Elle est efficiente sur le plan computationnel, mais peut conduire à un résultat sous-optimal.

Étant donné tous les mots possibles, il ne serait pas efficiente sur le plan computationnel/espace de calculer toutes les phrases possibles et de déterminer la phrase optimale. Cela exclut l'utilisation d'un algorithme de recherche tel que la recherche en profondeur d'abord ou la recherche en largeur d'abord pour trouver le chemin optimal.

![Image](https://cdn-media-1.freecodecamp.org/images/1*_rTQDUNkvkG_yTTBdadOSg.png)
_[source](http://blog.murraycole.com/wp-content/uploads/2018/04/sentence_explore_graph.png.png" rel="noopener" target="_blank" title=")_

#### **Recherche par faisceau**

La recherche par faisceau est un algorithme de recherche en largeur d'abord qui explore les nœuds les plus prometteurs. Il génère tous les chemins suivants possibles, ne gardant que les N meilleurs candidats à chaque itération.

Comme le nombre de nœuds à développer est fixe, cet algorithme est efficiente en espace et permet plus de candidats potentiels qu'une recherche du meilleur d'abord.

![Image](https://cdn-media-1.freecodecamp.org/images/1*LB1wsEavM6t7C7A85s1dUg.png)
_Recherche par faisceau pour construire une phrase. [source](https://www.youtube.com/watch?v=UXW6Cs82UKo" rel="noopener" target="_blank" title=")_

### Révision

Jusqu'à présent, vous avez appris à créer une architecture de modèle pour générer une phrase, étant donné une image. Cela est fait en utilisant un CNN pour créer une intégration dense et en alimentant cela comme état initial à un LSTM. De plus, vous avez appris à générer de meilleures phrases avec la recherche par faisceau.

Dans la section suivante, vous apprendrez à générer des légendes à partir d'un modèle pré-entraîné dans Tensorflow.

### Création de légendes dans Tensorflow

```
# Structure du projet
```

```
├── Dockerfile
├── bin
│   └── download_model.py
├── etc
│   ├── show-and-tell-2M.zip
│   ├── show-and-tell.pb
│   └── word_counts.txt
├── imgs
│   └── trading_floor.jpg
├── medium_show_and_tell_caption_generator
│   ├── __init__.py
│   ├── caption_generator.py
│   ├── inference.py
│   ├── model.py
│   └── vocabulary.py
└── requirements.txt
```

#### Configuration de l'environnement

Ici, vous utiliserez **Docker** pour installer **Tensorflow**.

Docker est une plateforme de conteneurs qui simplifie le déploiement. Elle résout le problème de l'installation des dépendances logicielles sur différents environnements de serveur. Si vous êtes nouveau dans Docker, vous pouvez en lire plus [ici](https://www.docker.com/). Pour installer Docker, exécutez :

```
curl https://get.docker.com | sh
```

Après avoir installé Docker, vous allez créer deux fichiers. Un **requirements.txt** pour les dépendances Python et un **Dockerfile** pour créer votre environnement Docker.

Pour construire cette image, exécutez :

```
$ docker build -t colemurray/medium-show-and-tell-caption-generator -f Dockerfile .
```

```
# Sur MBP, ~ 3mins
# L'image peut être tirée de dockerhub ci-dessous
```

Si vous souhaitez éviter de construire à partir de la source, l'image peut être tirée de dockerhub en utilisant :

```
docker pull colemurray/medium-show-and-tell-caption-generator # Recommandé
```

#### Télécharger le modèle

![Image](https://cdn-media-1.freecodecamp.org/images/1*zKDLRi58_Lq5cTuLDGCIIA.png)
_Architecture d'inférence Show and Tell [source](http://blog.murraycole.com/wp-content/uploads/2018/04/show_and_tell_inception_expanded.png" rel="noopener" target="_blank" title=")_

Ci-dessous, vous allez télécharger le graphe du modèle et les poids pré-entraînés. Ces poids proviennent d'une session d'entraînement sur le [jeu de données MSCOCO](http://cocodataset.org/#home) pour 2 millions d'itérations.

Pour télécharger, exécutez :

```
docker run -e PYTHONPATH=$PYTHONPATH:/opt/app -v $PWD:/opt/app \
-it colemurray/medium-show-and-tell-caption-generator \
python3 /opt/app/bin/download_model.py \
--model-dir /opt/app/etc
```

Ensuite, créez une classe de modèle. Cette classe est responsable du chargement du graphe, de la création d'intégrations d'images et de l'exécution d'une étape d'inférence sur le modèle.

#### **Télécharger le vocabulaire**

Lors de l'entraînement d'un LSTM, il est courant de tokeniser l'entrée. Pour un modèle de phrase, cela signifie mapper chaque mot unique à un identifiant numérique unique. Cela permet au modèle d'utiliser un classificateur softmax pour la prédiction.

Ci-dessous, vous allez télécharger le vocabulaire utilisé pour le modèle pré-entraîné et créer une classe pour le charger en mémoire. Ici, le numéro de ligne représente l'identifiant numérique du token.

```
# Structure du fichier
# token num_of_occurrances
```

```
# on 213612
# of 202290
# the 196219
# in 182598
```

```
curl -o etc/word_counts.txt https://raw.githubusercontent.com/ColeMurray/medium-show-and-tell-caption-generator/master/etc/word_counts.txt
```

Pour stocker ce vocabulaire en mémoire, vous allez créer une classe responsable de la cartographie des mots aux identifiants.

#### Création d'un générateur de légendes

Pour générer des légendes, vous allez d'abord créer un générateur de légendes. Ce générateur de légendes utilise la recherche par faisceau pour améliorer la qualité des phrases générées.

À chaque itération, le générateur transmet l'état précédent du LSTM (l'état initial est l'intégration de l'image) et la séquence précédente pour générer le vecteur softmax suivant.

Les N candidats les plus probables sont conservés et utilisés dans l'étape d'inférence suivante. Ce processus continue jusqu'à ce que soit la longueur maximale de la phrase soit atteinte, soit que toutes les phrases aient généré le jeton de fin de phrase.

Ensuite, vous allez charger le modèle show and tell et l'utiliser avec le générateur de légendes ci-dessus pour créer des phrases candidates. Ces phrases seront imprimées avec leur probabilité logarithmique.

#### Résultats

Pour générer des légendes, vous devrez passer une ou plusieurs images au script.

```
docker run -v $PWD:/opt/app \
-e PYTHONPATH=$PYTHONPATH:/opt/app \
-it colemurray/medium-show-and-tell-caption-generator  \
python3 /opt/app/medium_show_and_tell_caption_generator/inference.py \
--model_path /opt/app/etc/show-and-tell.pb \
--input_files /opt/app/imgs/trading_floor.jpg \
--vocab_file /opt/app/etc/word_counts.txt
```

Vous devriez voir la sortie :

```
Captions for image trading_floor.jpg: 
0) a group of people sitting at tables in a room . (p=0.000306)
1) a group of people sitting around a table with laptops . (p=0.000140)
2) a group of people sitting at a table with laptops . (p=0.000069)
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*JVTNDR601aHk7NCRILdHTQ.jpeg)
_Légende générée : un groupe de personnes assises autour d'une table avec des ordinateurs portables_

### Conclusion

Dans ce tutoriel, vous avez appris :

* comment un réseau de neurones convolutif et un LSTM peuvent être combinés pour générer des légendes pour une image
* comment utiliser l'algorithme de recherche par faisceau pour considérer plusieurs légendes et sélectionner la phrase la plus probable.

Code complet [ici](https://github.com/ColeMurray/medium-show-and-tell-caption-generator).

**Prochaines étapes** :

* Essayez avec vos propres images
* Lisez l'article [Show and Tell](https://arxiv.org/abs/1411.4555)
* Créez une API pour servir des légendes

### Appel à l'action :

Si vous avez aimé ce tutoriel, suivez et recommandez !

Intéressé à en apprendre plus sur l'apprentissage profond / l'apprentissage automatique ? Consultez mes autres tutoriels :

- [Création d'un pipeline de reconnaissance faciale avec l'apprentissage profond dans Tensorflow](https://hackernoon.com/building-a-facial-recognition-pipeline-with-deep-learning-in-tensorflow-66e7645015b8)

[- Deep Learning CNN dans Tensorflow avec GPU](https://medium.com/p/cba6efe0acc2)

[- Deep Learning avec Keras sur Google Compute Engine](https://medium.com/google-cloud/keras-inception-v3-on-google-compute-engine-a54918b0058)

[- Systèmes de recommandation avec Apache Spark sur Google Compute Engine](https://medium.com/google-cloud/recommendation-systems-with-spark-on-google-dataproc-bbb276c0dafd)

Autres endroits où vous pouvez me trouver :

- Twitter : [https://twitter.com/_ColeMurray](https://twitter.com/_ColeMurray)