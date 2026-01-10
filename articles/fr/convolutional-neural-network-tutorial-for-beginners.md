---
title: Qu'est-ce qu'un réseau de neurones convolutifs ? Un tutoriel pour débutants
  en apprentissage automatique et en deep learning
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-02-04T16:53:39.000Z'
originalURL: https://freecodecamp.org/news/convolutional-neural-network-tutorial-for-beginners
coverImage: https://cdn-media-2.freecodecamp.org/w1280/60170cab0a2838549dcbc230.jpg
tags:
- name: beginners guide
  slug: beginners-guide
- name: Deep Learning
  slug: deep-learning
- name: Machine Learning
  slug: machine-learning
- name: neural networks
  slug: neural-networks
seo_title: Qu'est-ce qu'un réseau de neurones convolutifs ? Un tutoriel pour débutants
  en apprentissage automatique et en deep learning
seo_desc: 'By Milecia McGregor

  There are a lot of different kinds of neural networks that you can use in machine
  learning projects. There are recurrent neural networks, feed-forward neural networks,
  modular neural networks, and more.

  Convolutional neural networ...'
---

Par Milecia McGregor

Il existe de nombreux types différents de réseaux de neurones que vous pouvez utiliser dans des projets d'apprentissage automatique. Il y a les réseaux de neurones récurrents, les réseaux de neurones feed-forward, les réseaux de neurones modulaires, et plus encore.

Les réseaux de neurones convolutifs sont un autre type de réseau de neurones couramment utilisé. Avant d'aborder les détails des réseaux de neurones convolutifs, commençons par parler d'un réseau de neurones régulier.

## Qu'est-ce qu'un réseau de neurones ?

Lorsque vous entendez les gens parler d'un domaine de l'apprentissage automatique appelé deep learning, ils parlent probablement des réseaux de neurones.

Les réseaux de neurones sont modélisés après notre cerveau. Il y a des nœuds individuels qui forment les couches du réseau, tout comme les neurones dans notre cerveau connectent différentes zones.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/neural-network-hidden-layers.png)
_Réseau de neurones avec plusieurs couches cachées. Chaque couche a plusieurs nœuds._

Les entrées des nœuds dans une seule couche auront un poids qui leur est assigné, ce qui change l'effet que ce paramètre a sur le résultat global de la prédiction. Puisque les poids sont assignés sur les liens entre les nœuds, chaque nœud peut être influencé par plusieurs poids.

Le réseau de neurones prend toutes les données d'entraînement dans la couche d'entrée. Ensuite, il passe les données à travers les couches cachées, transformant les valeurs en fonction des poids à chaque nœud. Enfin, il retourne une valeur dans la couche de sortie.

Il peut prendre un certain temps pour ajuster correctement un réseau de neurones afin d'obtenir des résultats cohérents et fiables. Tester et entraîner votre réseau de neurones est un processus d'équilibrage entre la décision des caractéristiques les plus importantes pour votre modèle.

## **Ce qu'un réseau de neurones convolutifs (CNN) fait différemment**

Un réseau de neurones convolutifs est un type spécifique de réseau de neurones avec plusieurs couches. Il traite les données qui ont une disposition en forme de grille puis extrait les caractéristiques importantes. Un énorme avantage de l'utilisation des CNNs est que vous n'avez pas besoin de faire beaucoup de prétraitement sur les images.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/cnn-example.png)
_[Source de l'image](https://www.researchgate.net/figure/A-vanilla-Convolutional-Neural-Network-CNN-representation_fig2_339447623)_

Avec la plupart des algorithmes qui gèrent le traitement d'images, les filtres sont généralement créés par un ingénieur sur la base d'heuristiques. Les CNNs peuvent apprendre quelles caractéristiques des filtres sont les plus importantes. Cela permet d'économiser beaucoup de temps et de travail d'essais et d'erreurs puisque nous n'avons pas besoin d'autant de paramètres.

Cela ne semble pas être une énorme économie jusqu'à ce que vous travailliez avec des images haute résolution qui ont des milliers de pixels. Le principal objectif de l'algorithme du réseau de neurones convolutifs est d'obtenir des données sous des formes plus faciles à traiter sans perdre les caractéristiques importantes pour déterminer ce que les données représentent. Cela les rend également de bons candidats pour gérer de grands ensembles de données.

Une grande différence entre un CNN et un réseau de neurones régulier est que les CNNs utilisent des convolutions pour gérer les mathématiques en arrière-plan. Une convolution est utilisée au lieu de la multiplication de matrices dans au moins une couche du CNN. Les convolutions prennent deux fonctions et retournent une fonction.

Les CNNs fonctionnent en appliquant des filtres à vos données d'entrée. Ce qui les rend si spéciaux est que les CNNs sont capables d'ajuster les filtres au fur et à mesure que l'entraînement se produit. Ainsi, les résultats sont affinés en temps réel, même lorsque vous avez de grands ensembles de données, comme avec les images.

Puisque les filtres peuvent être mis à jour pour mieux entraîner le CNN, cela élimine le besoin de filtres créés à la main. Cela nous donne plus de flexibilité dans le nombre de filtres que nous pouvons appliquer à un ensemble de données et la pertinence de ces filtres. En utilisant cet algorithme, nous pouvons travailler sur des problèmes plus sophistiqués comme la reconnaissance faciale.

L'une des choses qui empêchent de nombreux problèmes d'utiliser les CNNs est le manque de données. Bien que les réseaux puissent être entraînés avec relativement peu de points de données (~10 000 >), plus il y a de données disponibles, mieux le CNN sera ajusté.

Gardez simplement à l'esprit que ces points de données doivent être propres et étiquetés pour que le CNN puisse les utiliser. C'est ce qui les rend si coûteux à utiliser.

## Comment fonctionnent les réseaux de neurones convolutifs

Les réseaux de neurones convolutifs sont basés sur des découvertes en neuroscience. Ils sont composés de couches de neurones artificiels appelés nœuds. Ces nœuds sont des fonctions qui calculent la somme pondérée des entrées et retournent une carte d'activation. C'est la partie convolution du réseau de neurones.

Chaque nœud dans une couche est défini par ses valeurs de poids. Lorsque vous donnez une couche des données, comme une image, elle prend les valeurs des pixels et en extrait certaines des caractéristiques visuelles.

Lorsque vous travaillez avec des données dans un CNN, chaque couche retourne des cartes d'activation. Ces cartes pointent les caractéristiques importantes dans l'ensemble de données. Si vous donnez au CNN une image, il pointera les caractéristiques basées sur les valeurs des pixels, comme les couleurs, et vous donnera une fonction d'activation.

Habituellement avec des images, un CNN trouvera initialement les bords de l'image. Ensuite, cette légère définition de l'image sera transmise à la couche suivante. Ensuite, cette couche commencera à détecter des choses comme les coins et les groupes de couleurs. Ensuite, cette définition d'image sera transmise à la couche suivante et le cycle continue jusqu'à ce qu'une prédiction soit faite.

À mesure que les couches deviennent plus définies, cela s'appelle le max pooling. Il ne retourne que les caractéristiques les plus pertinentes de la couche dans la carte d'activation. C'est ce qui est transmis à chaque couche successive jusqu'à ce que vous obteniez la couche finale.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/activation-map.png)
_https://www.guru99.com/convnet-tensorflow-image-classification.html_

La dernière couche d'un CNN est la couche de classification qui détermine la valeur prédite en fonction de la carte d'activation. Si vous passez un échantillon d'écriture manuscrite à un CNN, la couche de classification vous dira quelle lettre se trouve dans l'image. C'est ce que les véhicules autonomes utilisent pour déterminer si un objet est une autre voiture, une personne ou un autre obstacle.

L'entraînement d'un CNN est similaire à l'entraînement de nombreux autres algorithmes d'apprentissage automatique. Vous commencerez avec des données d'entraînement qui sont séparées de vos données de test et vous ajusterez vos poids en fonction de la précision des valeurs prédites. Faites simplement attention à ne pas surajuster votre modèle.

## Cas d'utilisation d'un réseau de neurones convolutifs

Il existe plusieurs types de CNNs que vous pouvez utiliser selon votre problème.

### Différents types de CNNs

**1D CNN** : Avec ceux-ci, le noyau du CNN se déplace dans une direction. Les CNNs 1D sont généralement utilisés sur des données de séries temporelles.

**2D CNN** : Ces types de noyaux de CNN se déplacent dans deux directions. Vous verrez ceux-ci utilisés avec l'étiquetage et le traitement d'images.

**3D CNN** : Ce type de CNN a un noyau qui se déplace dans trois directions. Avec ce type de CNN, les chercheurs les utilisent sur des images 3D comme les scanners CT et les IRM.

Dans la plupart des cas, vous verrez des CNNs 2D car ceux-ci sont couramment associés aux données d'images. Voici quelques-unes des applications pour lesquelles vous pourriez voir des CNNs utilisés.

* Reconnaître des images avec peu de prétraitement
* Reconnaître différentes écritures manuscrites
* Applications de vision par ordinateur
* Utilisés en banque pour lire les chiffres sur les chèques
* Utilisés dans les services postaux pour lire les codes postaux sur une enveloppe

## Un exemple de CNN en Python

En tant qu'exemple d'utilisation d'un CNN sur un problème réel, nous allons identifier certains nombres manuscrits en utilisant l'ensemble de données MNIST.

La première chose que nous faisons est de définir le modèle CNN. Ensuite, nous séparons nos données d'entraînement et de test. Enfin, nous utilisons les données d'entraînement pour entraîner le modèle et testons ce modèle en utilisant les données de test.

```python
from keras import layers
from keras import models
from keras.datasets import mnist
from keras.utils import to_categorical

# Définir le modèle CNN
model = models.Sequential()

model.add(layers.Conv2D(32, (5,5), activation='relu', input_shape=(28, 28,1)))
model.add(layers.MaxPooling2D((2, 2)))

model.add(layers.Conv2D(64, (5, 5), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))

model.add(layers.Flatten())
model.add(layers.Dense(10, activation='softmax'))

model.summary()

# Diviser les données en ensembles d'entraînement et de test
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

train_images = train_images.reshape((60000, 28, 28, 1))
train_images = train_images.astype('float32') / 255

test_images = test_images.reshape((10000, 28, 28, 1))
test_images = test_images.astype('float32') / 255

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# Utiliser les données d'entraînement pour entraîner le modèle
model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])

model.fit(train_images, train_labels,
          batch_size=100,
          epochs=5,
          verbose=1)

# Tester la précision du modèle avec les données de test
test_loss, test_acc = model.evaluate(test_images, test_labels)

print('Précision du test:', test_acc)
```

## Conclusion

Les réseaux de neurones convolutifs sont des réseaux de neurones multicouches qui sont très bons pour extraire les caractéristiques des données. Ils fonctionnent bien avec les images et ils n'ont pas besoin de beaucoup de prétraitement.

En utilisant des convolutions et du pooling pour réduire une image à ses caractéristiques de base, vous pouvez identifier correctement les images.

Il est plus facile d'entraîner des modèles CNN avec moins de paramètres initiaux que avec d'autres types de réseaux de neurones. Vous n'aurez pas besoin d'un grand nombre de couches cachées car les convolutions pourront gérer une grande partie de la découverte des couches cachées pour vous.

L'une des choses intéressantes à propos des CNNs est le nombre de problèmes complexes auxquels ils peuvent être appliqués. Des voitures autonomes à la détection du diabète, les CNNs peuvent traiter ce type de données et fournir des prédictions précises.