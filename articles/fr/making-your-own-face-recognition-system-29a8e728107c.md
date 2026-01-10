---
title: Créer votre propre système de reconnaissance faciale
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-11T19:12:58.000Z'
originalURL: https://freecodecamp.org/news/making-your-own-face-recognition-system-29a8e728107c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*EJ1JjEMRShfcI0N5-GP29g.jpeg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: education
  slug: education
- name: Life lessons
  slug: life-lessons
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: Créer votre propre système de reconnaissance faciale
seo_desc: 'By Sigurður Skúli

  Face recognition is the latest trend when it comes to user authentication. Apple
  recently launched their new iPhone X which uses Face ID to authenticate users. OnePlus
  5 is getting the Face Unlock feature from theOnePlus 5T soon. An...'
---

Par Sigurður Skúli

La reconnaissance faciale est la dernière tendance en matière d'authentification des utilisateurs. Apple a récemment lancé son nouveau iPhone X qui utilise [Face ID](https://www.macworld.com/article/3225406/iphone-ipad/face-id-iphone-x-faq.html) pour authentifier les utilisateurs. Le OnePlus 5 recevra bientôt [la fonctionnalité de déverrouillage par reconnaissance faciale](https://gadgets.ndtv.com/mobiles/news/oneplus-5-face-unlock-feature-oxygenos-open-beta-3-now-available-download-1794682) du OnePlus 5T. Et [Baidu utilise la reconnaissance faciale au lieu de cartes d'identité pour permettre à ses employés d'entrer dans leurs bureaux](https://www.youtube.com/watch?v=wr4rx0Spihs). Ces applications peuvent sembler magiques pour beaucoup de gens. Mais dans cet article, nous visons à démystifier le sujet en vous apprenant à créer votre propre version simplifiée d'un système de reconnaissance faciale en Python.

[Lien Github pour ceux qui n'aiment pas lire et veulent seulement le code](https://github.com/Skuldur/facenet-face-recognition)

### Contexte

Avant d'entrer dans les détails de l'implémentation, je veux discuter des détails de FaceNet, qui est le réseau que nous allons utiliser dans notre système.

#### FaceNet

FaceNet est un réseau de neurones qui apprend une cartographie des images de visages vers un espace euclidien compact où les distances correspondent à une mesure de similarité faciale. C'est-à-dire que plus deux images de visages sont similaires, plus la distance entre elles est faible.

#### Triplet Loss

FaceNet utilise une méthode de perte distincte appelée Triplet Loss pour calculer la perte. Triplet Loss minimise la distance entre une ancre et une image positive, qui contiennent la même identité, et maximise la distance entre l'ancre et une image négative, qui contiennent des identités différentes.

![Image](https://cdn-media-1.freecodecamp.org/images/OktmhejWcRukgkbu-uITV2hxc0EendBoDXyI)
_Figure 1 : L'équation de la Triplet Loss_

* **f(a)** fait référence à l'encodage de sortie de l'ancre
* **f(p)** fait référence à l'encodage de sortie de l'image positive
* **f(n)** fait référence à l'encodage de sortie de l'image négative
* **alpha** est une constante utilisée pour s'assurer que le réseau n'essaie pas d'optimiser vers **f(a) - f(p) = f(a) - f(n) = 0.**
* **[]+** est égal à **max(0, sum)**

#### Siamese Networks

![Image](https://cdn-media-1.freecodecamp.org/images/KxuE07pBs9AXxFuteHXN8A65FQv0XMKWgHN9)
_Figure 2 : Un exemple de réseau Siamese qui utilise des images de visages comme entrée et produit un encodage de 128 nombres de l'image. Source : [Coursera](https://www.coursera.org/learn/convolutional-neural-networks" rel="noopener" target="_blank" title=")_

FaceNet est un réseau Siamese. Un réseau Siamese est un type d'architecture de réseau de neurones qui apprend à différencier deux entrées. Cela leur permet d'apprendre quelles images sont similaires et lesquelles ne le sont pas. Ces images peuvent contenir des visages.

Les réseaux Siamese se composent de deux réseaux de neurones identiques, chacun avec les mêmes poids exacts. Tout d'abord, chaque réseau prend une des deux images d'entrée comme entrée. Ensuite, les sorties des dernières couches de chaque réseau sont envoyées à une fonction qui détermine si les images contiennent la même identité.

Dans FaceNet, cela est fait en calculant la distance entre les deux sorties.

### Implémentation

Maintenant que nous avons clarifié la théorie, nous pouvons passer directement à l'implémentation.

Dans notre implémentation, nous allons utiliser [Keras](https://keras.io/) et [Tensorflow](https://www.tensorflow.org/). De plus, nous utilisons deux fichiers utilitaires que nous avons obtenus du [dépôt de deeplearning.ai](https://github.com/shahariarrabby/deeplearning.ai/tree/master/COURSE%204%20Convolutional%20Neural%20Networks/Week%2004/Face%20Recognition) pour abstraire toutes les interactions avec le réseau FaceNet :

* **fr_utils.py** contient des fonctions pour alimenter des images dans le réseau et obtenir l'encodage des images
* **inception_blocks_v2.py** contient des fonctions pour préparer et compiler le réseau FaceNet

#### Compilation du réseau FaceNet

La première chose que nous devons faire est de compiler le réseau FaceNet afin de pouvoir l'utiliser pour notre système de reconnaissance faciale.

```
import os
import glob
import numpy as np
import cv2
import tensorflow as tf
from fr_utils import *
from inception_blocks_v2 import *
from keras import backend as K
```

```
K.set_image_data_format('channels_first')
```

```
FRmodel = faceRecoModel(input_shape=(3, 96, 96))
```

```
def triplet_loss(y_true, y_pred, alpha = 0.3):
    anchor, positive, negative = y_pred[0], y_pred[1], y_pred[2]
    pos_dist = tf.reduce_sum(tf.square(tf.subtract(anchor, positive)), axis=-1)
    neg_dist = tf.reduce_sum(tf.square(tf.subtract(anchor, negative)), axis=-1)
    basic_loss = tf.add(tf.subtract(pos_dist, neg_dist), alpha)
    loss = tf.reduce_sum(tf.maximum(basic_loss, 0.0))
    return loss
```

```
FRmodel.compile(optimizer = 'adam', loss = triplet_loss, metrics = ['accuracy'])
load_weights_from_FaceNet(FRmodel)
```

Nous allons commencer par initialiser notre réseau avec une forme d'entrée de (3, 96, 96). Cela signifie que les canaux Rouge-Vert-Bleu (RGB) sont la première dimension du volume de l'image alimenté dans le réseau. Et que toutes les images alimentées dans le réseau doivent être des images de 96x96 pixels.

Ensuite, nous allons définir la fonction Triplet Loss. La fonction dans l'extrait de code ci-dessus suit la définition de l'équation Triplet Loss que nous avons définie dans la section précédente.

Si vous n'êtes pas familier avec l'une des fonctions Tensorflow utilisées pour effectuer le calcul, je vous recommande de lire la documentation (pour laquelle j'ai ajouté des liens pour chaque fonction) car cela améliorera votre compréhension du code. Mais comparer la fonction à l'équation de la Figure 1 devrait suffire.

Une fois que nous avons notre fonction de perte, nous pouvons compiler notre modèle de reconnaissance faciale en utilisant Keras. Et nous allons utiliser l'[optimiseur Adam](https://keras.io/optimizers/#adam) pour minimiser la perte calculée par la fonction Triplet Loss.

#### Préparation d'une base de données

Maintenant que nous avons compilé FaceNet, nous allons préparer une base de données d'individus que nous voulons que notre système reconnaisse. Nous allons utiliser toutes les images contenues dans notre répertoire _images_ pour notre base de données d'individus.

_NOTE : Nous n'allons utiliser qu'une seule image de chaque individu dans notre implémentation. La raison est que le réseau FaceNet est suffisamment puissant pour n'avoir besoin que d'une seule image d'un individu pour le reconnaître !_

```
def prepare_database():
    database = {}
```

```
    for file in glob.glob("images/*"):
        identity = os.path.splitext(os.path.basename(file))[0]
        database[identity] = img_path_to_encoding(file, FRmodel)
```

```
    return database
```

Pour chaque image, nous allons convertir les données de l'image en un encodage de 128 nombres flottants. Nous faisons cela en appelant la fonction **img_path_to_encoding**. La fonction prend en entrée un chemin vers une image et alimente l'image dans notre réseau de reconnaissance faciale. Ensuite, elle retourne la sortie du réseau, qui se trouve être l'encodage de l'image.

Une fois que nous avons ajouté l'encodage de chaque image à notre base de données, notre système peut enfin commencer à reconnaître les individus !

#### Reconnaissance d'un visage

Comme discuté dans la section Contexte, FaceNet est entraîné pour minimiser la distance entre les images du même individu et maximiser la distance entre les images d'individus différents. Notre implémentation utilise cette information pour déterminer à quel individu la nouvelle image alimentée dans notre système est le plus susceptible d'appartenir.

```
def who_is_it(image, database, model):
    encoding = img_to_encoding(image, model)
    min_dist = 100
    identity = None
    # Boucle sur les noms et encodages du dictionnaire de la base de données.
    for (name, db_enc) in database.items():
        dist = np.linalg.norm(db_enc - encoding)
```

```
        print('distance pour %s est %s' %(name, dist))
```

```
        if dist < min_dist:
            min_dist = dist
            identity = name
    if min_dist > 0.52:
        return None
    else:
        return identity
```

La fonction ci-dessus alimente la nouvelle image dans une fonction utilitaire appelée **img_to_encoding**. La fonction traite une image en utilisant FaceNet et retourne l'encodage de l'image. Maintenant que nous avons l'encodage, nous pouvons trouver l'individu auquel l'image appartient le plus probablement.

Pour trouver l'individu, nous parcourons notre base de données et calculons la distance entre notre nouvelle image et chaque individu dans la base de données. L'individu avec la distance la plus faible par rapport à la nouvelle image est alors choisi comme le candidat le plus probable.

Enfin, nous devons déterminer si l'image candidate et la nouvelle image contiennent la même personne ou non. À la fin de notre boucle, nous avons seulement déterminé l'individu le plus probable. C'est là que l'extrait de code suivant entre en jeu.

```
if min_dist > 0.52:
    return None
else:
    return identity
```

* Si la distance est supérieure à 0,52, alors nous déterminons que l'individu dans la nouvelle image n'existe pas dans notre base de données.
* Mais, si la distance est égale ou inférieure à 0,52, alors nous déterminons qu'ils sont le même individu !

Maintenant, la partie délicate ici est que la valeur 0,52 a été obtenue par essai et erreur de ma part pour mon ensemble de données spécifique. La meilleure valeur peut être beaucoup plus basse ou légèrement plus élevée et elle dépendra de votre implémentation et de vos données. Je recommande d'essayer différentes valeurs et de voir ce qui convient le mieux à votre système !

### Construction d'un système utilisant la reconnaissance faciale

Maintenant que nous connaissons les détails sur la façon dont nous reconnaissons une personne en utilisant un algorithme de reconnaissance faciale, nous pouvons commencer à nous amuser avec.

Dans le dépôt Github que j'ai lié au début de cet article, il y a une démonstration qui utilise la webcam d'un ordinateur portable pour alimenter des images vidéo dans notre algorithme de reconnaissance faciale. Une fois que l'algorithme reconnaît un individu dans l'image, la démonstration joue un message audio qui accueille l'utilisateur en utilisant le nom de leur image dans la base de données. La Figure 3 montre un exemple de la démonstration en action.

![Image](https://cdn-media-1.freecodecamp.org/images/j8-i3qDBRrP4EOPNdiJPEXduBDMZz45v0FCr)
_Figure 3 : Une image capturée au moment exact où le réseau a reconnu l'individu dans l'image. Le nom de l'image dans la base de données était « skuli.jpg » donc le message audio joué était « Bienvenue skuli, passe une bonne journée ! »_

### Conclusion

À présent, vous devriez être familier avec le fonctionnement des systèmes de reconnaissance faciale et comment créer votre propre système de reconnaissance faciale simplifié en utilisant une version pré-entraînée du réseau FaceNet en Python !

Si vous voulez jouer avec la démonstration dans le dépôt Github et ajouter des images de personnes que vous connaissez, alors allez-y et fork le dépôt.

Amusez-vous avec la démonstration et impressionnez tous vos amis avec votre connaissance impressionnante de la reconnaissance faciale !