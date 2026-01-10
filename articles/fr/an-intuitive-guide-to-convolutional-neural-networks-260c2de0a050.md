---
title: Un guide intuitif des réseaux de neurones convolutifs
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-24T16:21:46.000Z'
originalURL: https://freecodecamp.org/news/an-intuitive-guide-to-convolutional-neural-networks-260c2de0a050
coverImage: https://cdn-media-1.freecodecamp.org/images/1*caaTn6qbHTVuo__Hro5iLA.png
tags:
- name: Data Science
  slug: data-science
- name: Deep Learning
  slug: deep-learning
- name: Machine Learning
  slug: machine-learning
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Un guide intuitif des réseaux de neurones convolutifs
seo_desc: 'By Daphne Cornelisse

  In this article, we will explore Convolutional Neural Networks (CNNs) and, on a
  high level, go through how they are inspired by the structure of the brain. If you
  want to read more about the brain specifically, there are more res...'
---

Par Daphne Cornelisse

Dans cet article, nous allons explorer les réseaux de neurones convolutifs (CNN) et, à un niveau élevé, voir comment ils sont inspirés par la structure du cerveau. Si vous souhaitez en savoir plus sur le cerveau spécifiquement, il y a plus de ressources à la fin de l'article pour vous aider.

### **Le Cerveau**

Nous analysons constamment le monde qui nous entoure. Sans effort conscient, nous faisons des prédictions sur tout ce que nous voyons, et agissons en conséquence. Lorsque nous voyons quelque chose, nous étiquetons chaque objet en fonction de ce que nous avons appris dans le passé. Pour illustrer cela, regardez cette image pendant un moment.

![Image](https://cdn-media-1.freecodecamp.org/images/hgekwBdT-gVJSBlOMHnXIkfXmBBha3sS7Ui3)
_Source : [https://www.youtube.com/watch?v=40riCqvRoMs](https://www.youtube.com/watch?v=40riCqvRoMs" rel="noopener" target="_blank" title=")_

Vous avez probablement pensé quelque chose comme « c'est un petit garçon heureux debout sur une chaise ». Ou peut-être avez-vous pensé qu'il semble crier, sur le point d'attaquer ce gâteau devant lui.

![Image](https://cdn-media-1.freecodecamp.org/images/Qm6Wu-GLxjcnF6QtOSC9PdYrhuwdoRT0vwtl)
_Source : [https://www.youtube.com/watch?v=40riCqvRoMs](https://www.youtube.com/watch?v=40riCqvRoMs" rel="noopener" target="_blank" title=")_

C'est ce que nous faisons subconscemment toute la journée. Nous voyons, étiquetons, faisons des prédictions et reconnaissons des motifs. Mais comment faisons-nous cela ? Comment se fait-il que nous puissions interpréter tout ce que nous voyons ?

Il a fallu à la nature plus de 500 millions d'années pour créer un système capable de faire cela. La collaboration entre les yeux et le cerveau, appelée voie visuelle primaire, est la raison pour laquelle nous pouvons donner un sens au monde qui nous entoure.

![Image](https://cdn-media-1.freecodecamp.org/images/8ColleqWT2-WZC5EFh-GVf0xIZ2n9ymoIDnN)
_La Voie Visuelle. — Source : [https://commons.wikimedia.org/wiki/File:Human_visual_pathway.svg](https://commons.wikimedia.org/wiki/File:Human_visual_pathway.svg" rel="noopener" target="_blank" title=")_

Bien que la vision commence dans les yeux, l'interprétation réelle de ce que nous voyons se produit dans le cerveau, dans le **cortex visuel primaire**.

Lorsque vous voyez un objet, les récepteurs de lumière dans vos yeux envoient des signaux via le nerf optique au cortex visuel primaire, où l'entrée est traitée. Le [cortex visuel primaire](https://www.youtube.com/watch?v=unWnZvXJH2o&t=516s) donne un sens à ce que l'œil voit.

Tout cela nous semble très naturel. Nous pensons à peine à quel point il est spécial que nous soyons capables de reconnaître tous les objets et les personnes que nous voyons dans nos vies. La **structure hiérarchique profondément complexe** des neurones et des connexions dans le cerveau joue un rôle majeur dans ce processus de mémorisation et d'étiquetage des objets.

Pensez à la manière dont nous avons appris ce qu'est, par exemple, un parapluie. Ou un canard, une lampe, une bougie ou un livre. Au début, nos parents ou notre famille nous ont dit le nom des objets dans notre environnement direct. Nous avons appris par des exemples qui nous ont été donnés. Peu à peu, nous avons commencé à reconnaître certaines choses de plus en plus souvent dans notre environnement. Elles sont devenues si courantes que la prochaine fois que nous les voyions, nous saurions instantanément quel était le nom de cet objet. Elles sont devenues partie de notre **modèle** du monde.

### Réseaux de Neurones Convolutifs

De manière similaire à la façon dont un enfant apprend à reconnaître des objets, nous devons montrer à un algorithme des millions d'images avant qu'il ne soit capable de généraliser l'entrée et de faire des prédictions pour des images qu'il n'a jamais vues auparavant.

Les ordinateurs « voient » différemment de nous. Leur monde ne consiste qu'en des nombres. Chaque image peut être représentée comme des tableaux bidimensionnels de nombres, connus sous le nom de pixels.

Mais le fait qu'ils perçoivent les images différemment ne signifie pas que nous ne pouvons pas les entraîner à reconnaître des motifs, comme nous le faisons. Nous devons simplement penser à ce qu'est une image différemment.

![Image](https://cdn-media-1.freecodecamp.org/images/Mrv6CksJK-Aykq6Avbuo0VBpDHSuJAEJDpw9)
_Comment un ordinateur voit une image. — source : [http://cs231n.github.io/classification/](http://cs231n.github.io/classification/" rel="noopener" target="_blank" title=")_

Pour enseigner à un algorithme comment reconnaître des objets dans des images, nous utilisons un type spécifique de [Réseau de Neurones Artificiels](https://medium.com/@daphn3cor/building-a-3-layer-neural-network-from-scratch-99239c4af5d3) : un Réseau de Neurones Convolutifs (CNN). Leur nom provient de l'une des opérations les plus importantes du réseau : la [convolution](https://en.wikipedia.org/wiki/Convolution).

Les Réseaux de Neurones Convolutifs sont inspirés par le cerveau. Des recherches dans les années 1950 et 1960 par D.H Hubel et T.N Wiesel sur le cerveau des mammifères ont suggéré un nouveau modèle pour la façon dont les mammifères perçoivent le monde visuellement. Ils ont montré que les cortex visuels des chats et des singes incluent des neurones qui répondent exclusivement aux neurones dans leur environnement direct.

Dans leur [article](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1359523/pdf/jphysiol01247-0121.pdf), ils ont décrit deux types de base de cellules neuronales visuelles dans le cerveau qui agissent chacune différemment : les cellules simples (**cellules S**) et les cellules complexes (**cellules C**).

Les cellules simples s'activent, par exemple, lorsqu'elles identifient des formes de base comme des lignes dans une zone fixe et sous un angle spécifique. Les cellules complexes ont des champs réceptifs plus grands et leur sortie n'est pas sensible à la position spécifique dans le champ.

Les cellules complexes continuent de répondre à un certain stimulus, même si sa position absolue sur la [rétine](https://en.wikipedia.org/wiki/Retina) change. Complexe fait référence à plus flexible, dans ce cas.

En [vision](http://www.cns.nyu.edu/~david/courses/perception/lecturenotes/V1/lgn-V1.html), un **champ réceptif** d'un seul neurone sensoriel est la région spécifique de la rétine dans laquelle quelque chose affectera le déclenchement de ce neurone (c'est-à-dire, activera le neurone). Chaque cellule de neurone sensoriel a des champs réceptifs similaires, et leurs champs se chevauchent.

![Image](https://cdn-media-1.freecodecamp.org/images/pi9p2FN5bGaApL2KSKgkD8g1CSv9FMrgbqAd)
_Le champ réceptif d'un neurone. — Source : [http://neuroclusterbrain.com/neuron_model.html](http://neuroclusterbrain.com/neuron_model.html" rel="noopener" target="_blank" title=")_

De plus, le concept de **hiérarchie** joue un rôle significatif dans le cerveau. L'information est stockée en séquences de motifs, dans un ordre séquentiel. Le **néocortex**, qui est la couche la plus externe du cerveau, stocke l'information de manière hiérarchique. Elle est stockée dans des colonnes corticales, ou des regroupements uniformément organisés de neurones dans le néocortex.

En 1980, un chercheur nommé Fukushima a proposé un [modèle de réseau de neurones hiérarchique](https://en.wikipedia.org/wiki/Neocognitron). Il l'a appelé le **néocognitron**. Ce modèle était inspiré par les concepts des cellules Simples et Complexes. Le néocognitron était capable de reconnaître des motifs en apprenant les formes des objets.

Plus tard, en 1998, les Réseaux de Neurones Convolutifs ont été introduits dans un article par Bengio, Le Cun, Bottou et Haffner. Leur premier Réseau de Neurones Convolutifs s'appelait **LeNet-5** et était capable de classer des chiffres à partir de nombres écrits à la main.

Pour l'histoire complète des Réseaux de Neurones Convolutifs, vous pouvez aller [ici](http://dataconomy.com/2017/04/history-neural-networks/).

### **Architecture**

Dans le reste de cet article, je vais vous guider à travers l'architecture d'un CNN et vous montrer l'implémentation Python également.

Les Réseaux de Neurones Convolutifs ont une architecture différente de celle des Réseaux de Neurones réguliers. Les Réseaux de Neurones réguliers transforment une entrée en la faisant passer à travers une série de couches cachées. Chaque couche est composée d'un **ensemble de neurones**, où chaque couche est entièrement connectée à tous les neurones de la couche précédente. Enfin, il y a une dernière couche entièrement connectée — la couche de sortie — qui représente les prédictions.

Les Réseaux de Neurones Convolutifs sont un peu différents. Tout d'abord, les couches sont **organisées en 3 dimensions** : largeur, hauteur et profondeur. De plus, les neurones d'une couche ne se connectent pas à tous les neurones de la couche suivante mais seulement à une petite région de celle-ci. Enfin, la sortie finale sera réduite à un seul vecteur de scores de probabilité, organisé le long de la dimension de profondeur.

![Image](https://cdn-media-1.freecodecamp.org/images/Dgy6hBvOvAWofkrDM8BclOU3E3C2hqb25qBb)
_Réseau de Neurones Normal vs CNN. — Source : [http://cs231n.github.io/convolutional-networks/](http://cs231n.github.io/convolutional-networks/" rel="noopener" target="_blank" title=")_

Les CNNs ont deux composants :

* Les couches cachées/partie d'extraction de caractéristiques

Dans cette partie, le réseau effectuera une série d'opérations de **convolution** et de **pooling** au cours desquelles les **caractéristiques sont détectées**. Si vous aviez une image d'un zèbre, c'est la partie où le réseau reconnaîtrait ses rayures, ses deux oreilles et ses quatre pattes.

* La partie de classification

Ici, les couches entièrement connectées serviront de **classifieur** au-dessus de ces caractéristiques extraites. Elles attribueront une **probabilité** à l'objet sur l'image étant ce que l'algorithme prédit qu'il est.

```
# avant de commencer à construire, nous importons les bibliothèques
```

```
import numpy as np
```

```
from keras.layers import Conv2D, Activation, MaxPool2D, Flatten, Densefrom keras.models import Sequential
```

![Image](https://cdn-media-1.freecodecamp.org/images/dobVrh3SGyqQraM2ogi-P3VK2K-LFsBm7RLO)
_Architecture d'un CNN. — Source : [https://www.mathworks.com/videos/introduction-to-deep-learning-what-are-convolutional-neural-networks--1489512765771.html](https://www.mathworks.com/videos/introduction-to-deep-learning-what-are-convolutional-neural-networks--1489512765771.html" rel="noopener" target="_blank" title=")_

#### **Extraction de caractéristiques**

La convolution est l'un des principaux blocs de construction d'un CNN. Le terme [convolution](http://timdettmers.com/2015/03/26/convolution-deep-learning/) fait référence à la combinaison mathématique de deux fonctions pour produire une troisième fonction. Elle fusionne deux ensembles d'informations.

Dans le cas d'un CNN, la convolution est effectuée sur les données d'entrée à l'aide d'un **filtre** ou **noyau** (ces termes sont utilisés de manière interchangeable) pour produire ensuite une **carte de caractéristiques**.

Nous exécutons une convolution en faisant glisser le filtre sur l'entrée. À chaque emplacement, une multiplication de matrices est effectuée et la somme du résultat est ajoutée à la carte de caractéristiques.

Dans l'animation ci-dessous, vous pouvez voir l'opération de convolution. Vous pouvez voir le **filtre** (le carré vert) glisser sur notre **entrée** (le carré bleu) et la somme de la convolution va dans la **carte de caractéristiques** (le carré rouge).

La zone de notre filtre est également appelée le champ réceptif, nommé d'après les cellules neuronales ! La taille de ce filtre est de 3x3.

![Image](https://cdn-media-1.freecodecamp.org/images/Htskzls1pGp98-X2mHmVy9tCj0cYXkiCrQ4t)
_Gauche : le filtre glisse sur l'entrée. Droite : le résultat est sommé et ajouté à la carte de caractéristiques. — Source : [https://towardsdatascience.com/applied-deep-learning-part-4-convolutional-neural-networks-584bc134c1e2](https://towardsdatascience.com/applied-deep-learning-part-4-convolutional-neural-networks-584bc134c1e2" rel="noopener" target="_blank" title=")_

Pour simplifier l'explication, je vous ai montré l'opération en 2D, mais en réalité, les convolutions sont effectuées en 3D. Chaque image est représentée comme une matrice 3D avec une [dimension pour la largeur, la hauteur et la profondeur](https://www.youtube.com/watch?v=jajksuQW4mc). La profondeur est une dimension en raison des canaux de couleurs utilisés dans une image (RGB).

![Image](https://cdn-media-1.freecodecamp.org/images/Gjxh-aApWTzIRI1UNmGnNLrk8OKsQaf2tlDu)
_Le filtre glisse sur l'entrée et effectue sa sortie sur la nouvelle couche. — Source : [https://towardsdatascience.com/applied-deep-learning-part-4-convolutional-neural-networks-584bc134c1e2](https://towardsdatascience.com/applied-deep-learning-part-4-convolutional-neural-networks-584bc134c1e2" rel="noopener" target="_blank" title=")_

Nous effectuons de nombreuses convolutions sur notre entrée, où chaque opération utilise un filtre différent. Cela donne différentes cartes de caractéristiques. À la fin, nous prenons toutes ces cartes de caractéristiques et les mettons ensemble comme sortie finale de la couche de convolution.

Tout comme pour tout autre Réseau de Neurones, nous utilisons une **fonction d'activation** pour rendre notre sortie non linéaire. Dans le cas d'un Réseau de Neurones Convolutifs, la sortie de la convolution sera passée à travers la fonction d'activation. Cela pourrait être la fonction d'activation [ReLU](https://github.com/Kulbear/deep-learning-nano-foundation/wiki/ReLU-and-Softmax-Activation-Functions).

Le **pas** est la taille du pas que le filtre de convolution déplace à chaque fois. Une taille de pas est généralement de 1, ce qui signifie que le filtre glisse pixel par pixel. En augmentant la taille du pas, votre filtre glisse sur l'entrée avec un intervalle plus grand et a donc moins de chevauchement entre les cellules.

L'animation ci-dessous montre une taille de pas de 1 en action.

![Image](https://cdn-media-1.freecodecamp.org/images/d0ufdQE7LHA43cdSrVefw2I9DFceYMixqoZJ)

Parce que la taille de la carte de caractéristiques est toujours plus petite que l'entrée, nous devons faire quelque chose pour empêcher notre carte de caractéristiques de rétrécir. C'est là que nous utilisons le **remplissage**.

Une couche de pixels de valeur zéro est ajoutée pour entourer l'entrée avec des zéros, afin que notre carte de caractéristiques ne rétrécisse pas. En plus de maintenir la taille spatiale constante après avoir effectué la convolution, le remplissage améliore également les performances et garantit que la taille du noyau et du pas s'adaptera à l'entrée.

Après une couche de convolution, il est courant d'ajouter une **couche de pooling** entre les couches CNN. La fonction du pooling est de réduire continuellement la dimensionnalité pour réduire le nombre de paramètres et de calculs dans le réseau. Cela raccourcit le temps d'entraînement et contrôle le [surapprentissage](https://en.wikipedia.org/wiki/Overfitting).

Le type de pooling le plus fréquent est le **max pooling**, qui prend la valeur maximale dans chaque fenêtre. Ces tailles de fenêtre doivent être spécifiées au préalable. Cela diminue la taille de la carte de caractéristiques tout en conservant les informations significatives.

![Image](https://cdn-media-1.freecodecamp.org/images/96HH3r99NwOK818EB9ZdEbVY3zOBOYJE-I8Q)
_Le max pooling prend les plus grandes valeurs. — Source : [http://cs231n.github.io/convolutional-networks/](http://cs231n.github.io/convolutional-networks/" rel="noopener" target="_blank" title=")_

Ainsi, lors de l'utilisation d'un CNN, les quatre **hyperparamètres** importants que nous devons décider sont :

* la taille du noyau
* le nombre de filtres (c'est-à-dire, combien de filtres voulons-nous utiliser)
* le pas (quelle est la taille des pas du filtre)
* le remplissage

```
# Les images alimentées dans ce modèle sont de 512 x 512 pixels avec 3 canaux
```

```
img_shape = (28,28,1)
```

```
# Configurer le modèle
```

```
model = Sequential()
```

```
# Ajouter une couche de convolution avec 3 filtres de 3 par 3 et une taille de pas de 1# Définir le remplissage de sorte que la taille d'entrée soit égale à la taille de sortie
```

```
model.add(Conv2D(6,2,input_shape=img_shape))
```

```
# Ajouter l'activation relu à la couche 
```

```
model.add(Activation('relu'))
```

```
# Pooling
```

```
model.add(MaxPool2D(2))
```

Une belle façon de visualiser une couche de convolution est montrée ci-dessous. Essayez de la regarder un peu et comprenez vraiment ce qui se passe.

![Image](https://cdn-media-1.freecodecamp.org/images/gb08-2i83P5wPzs3SL-vosNb6Iur5kb5ZH43)
_Comment la convolution fonctionne avec K = 2 filtres, chacun avec une étendue spatiale F = 3, un pas S = 2, et un remplissage d'entrée P = 1. — Source : [http://cs231n.github.io/convolutional-networks/](http://cs231n.github.io/convolutional-networks/" rel="noopener" target="_blank" title=")_

#### **Classification**

Après les couches de convolution et de pooling, notre partie de classification se compose de quelques couches entièrement connectées. Cependant, ces couches entièrement connectées ne peuvent accepter que des données 1D. Pour convertir nos données 3D en 1D, nous utilisons la fonction `flatten` en Python. Cela organise essentiellement notre volume 3D en un vecteur 1D.

Les dernières couches d'un CNN sont des couches entièrement connectées. Les neurones dans une couche entièrement connectée ont des connexions complètes à toutes les activations de la couche précédente. Cette partie est en principe la même qu'un Réseau de Neurones régulier.

```
# Couches entièrement connectées
```

```
# Utiliser Flatten pour convertir les données 3D en 1Dmodel.add(Flatten())
```

```
# Ajouter une couche dense avec 10 neuronesmodel.add(Dense(10))
```

```
# nous utilisons la fonction d'activation softmax pour notre dernière couchemodel.add(Activation('softmax'))
```

```
# donner un aperçu de notre modèle
```

```
model.summary
```

```
_________________________________________________________________Layer (type)                 Output Shape              Param #   =================================================================conv2d_1 (Conv2D)            (None, 27, 27, 6)         30        _________________________________________________________________activation_1 (Activation)    (None, 27, 27, 6)         0         _________________________________________________________________max_pooling2d_1 (MaxPooling2 (None, 13, 13, 6)         0         _________________________________________________________________flatten_1 (Flatten)          (None, 1014)              0         _________________________________________________________________dense_1 (Dense)              (None, 10)                10150     _________________________________________________________________activation_2 (Activation)    (None, 10)                0         =================================================================Total params: 10,180Trainable params: 10,180Non-trainable params: 0__________________________________________________________________
```

### Entraînement

L'entraînement d'un CNN fonctionne de la même manière qu'un réseau de neurones régulier, en utilisant la rétropropagation ou la descente de gradient. Cependant, ici, cela est un peu plus complexe mathématiquement en raison des opérations de convolution.

Si vous souhaitez en savoir plus sur le fonctionnement des réseaux de neurones réguliers, vous pouvez lire mon [article précédent](https://medium.com/@daphn3cor/building-a-3-layer-neural-network-from-scratch-99239c4af5d3).

```
"""Avant le processus d'entraînement, nous devons mettre en place un processus d'apprentissage sous une forme particulière. Il se compose de 3 éléments : un optimiseur, une fonction de perte et une métrique."""
```

```
model.compile(loss='sparse_categorical_crossentropy', optimizer = 'adam', metrics=['acc'])
```

```
# ensemble de données avec des chiffres manuscrits pour entraîner le modèlefrom keras.datasets import mnist
```

```
(x_train, y_train), (x_test, y_test) = mnist.load_data()
```

```
x_train = np.expand_dims(x_train,-1)
```

```
x_test = np.expand_dims(x_test,-1)
```

```
# Entraîner le modèle, itérant sur les données par lots de 32 échantillons# pendant 10 époques
```

```
model.fit(x_train, y_train, batch_size=32, epochs=10, validation_data=(x_test,y_test)
```

```
# Entraînement...
```

```
Train on 60000 samples, validate on 10000 samplesEpoch 1/1060000/60000 [==============================] - 10s 175us/step - loss: 4.0330 - acc: 0.7424 - val_loss: 3.5352 - val_acc: 0.7746Epoch 2/1060000/60000 [==============================] - 10s 169us/step - loss: 3.5208 - acc: 0.7746 - val_loss: 3.4403 - val_acc: 0.7794Epoch 3/1060000/60000 [==============================] - 11s 176us/step - loss: 2.4443 - acc: 0.8372 - val_loss: 1.9846 - val_acc: 0.8645Epoch 4/1060000/60000 [==============================] - 10s 173us/step - loss: 1.8943 - acc: 0.8691 - val_loss: 1.8478 - val_acc: 0.8713Epoch 5/1060000/60000 [==============================] - 10s 174us/step - loss: 1.7726 - acc: 0.8735 - val_loss: 1.7595 - val_acc: 0.8718Epoch 6/1060000/60000 [==============================] - 10s 174us/step - loss: 1.6943 - acc: 0.8765 - val_loss: 1.7150 - val_acc: 0.8745Epoch 7/1060000/60000 [==============================] - 10s 173us/step - loss: 1.6765 - acc: 0.8777 - val_loss: 1.7268 - val_acc: 0.8688Epoch 8/1060000/60000 [==============================] - 10s 173us/step - loss: 1.6676 - acc: 0.8799 - val_loss: 1.7110 - val_acc: 0.8749Epoch 9/1060000/60000 [==============================] - 10s 172us/step - loss: 1.4759 - acc: 0.8888 - val_loss: 0.1346 - val_acc: 0.9597Epoch 10/1060000/60000 [==============================] - 11s 177us/step - loss: 0.1026 - acc: 0.9681 - val_loss: 0.1144 - val_acc: 0.9693
```

### Résumé

En résumé, les CNNs sont particulièrement utiles pour la classification et la reconnaissance d'images. Ils ont deux parties principales : une partie d'extraction de caractéristiques et une partie de classification.

La technique principale spéciale dans les CNNs est la convolution, où un filtre glisse sur l'entrée et fusionne la valeur d'entrée + la valeur du filtre sur la carte de caractéristiques. À la fin, notre objectif est de fournir de nouvelles images à notre CNN afin qu'il puisse donner une probabilité pour [l'objet qu'il pense voir](https://cs.stanford.edu/people/karpathy/neuraltalk2/demo.html) ou [décrire une image](https://cs.stanford.edu/people/karpathy/neuraltalk2/demo.html) avec du texte.

![Image](https://cdn-media-1.freecodecamp.org/images/Tt7D3r-a6nllpazQndXk2GibSjW2X6NOarO6)
— Source : [https://arxiv.org/pdf/1506.01497v3.pdf](https://arxiv.org/pdf/1506.01497v3.pdf" rel="noopener" target="_blank" title=")_

Vous pouvez trouver le code complet [ici](https://gist.github.com/JannesKlaas/a4e1caeb0e787411a03249d96aa67b3c).

#### Plus de recommandations liées au **cerveau** ?

* Lisez [cet](https://waitbutwhy.com/2017/04/neuralink.html) article vraiment cool sur le cerveau et plus encore.
* Je recommande également [ce](https://www.goodreads.com/book/show/27539.On_Intelligence) livre sur l'intelligence et le cerveau.
* [« Comment créer un esprit »](https://en.wikipedia.org/wiki/How_to_Create_a_Mind) par Ray Kurzweil.