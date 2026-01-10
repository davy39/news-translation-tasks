---
title: Chihuahua ou muffin ? Ma recherche de la meilleure API de vision par ordinateur
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-12T22:50:09.000Z'
originalURL: https://freecodecamp.org/news/chihuahua-or-muffin-my-search-for-the-best-computer-vision-api-cbda4d6b425d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*bt-E2YcPafjiPbZFDMMmNQ.jpeg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Computer Vision
  slug: computer-vision
- name: Machine Learning
  slug: machine-learning
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: Chihuahua ou muffin ? Ma recherche de la meilleure API de vision par ordinateur
seo_desc: 'By Mariya Yao

  This popular internet meme demonstrates the alarming resemblance shared between
  chihuahuas and muffins. These images are commonly shared in presentations in the
  Artificial Intelligence (AI) industry (myself included).

  But one question I...'
---

Par Mariya Yao

Ce mème populaire d'Internet démontre la ressemblance alarmante partagée entre les chihuahuas et les muffins. Ces images sont couramment partagées dans les présentations de l'industrie de l'intelligence artificielle (IA) (moi y compris).

Mais une question que je n'ai vu personne répondre est **à quel point l'IA moderne est-elle bonne pour éliminer l'incertitude d'une image qui pourrait ressembler à un chihuahua ou à un muffin ?** Pour votre divertissement et votre éducation, je vais enquêter sur cette question aujourd'hui.

![Image](https://cdn-media-1.freecodecamp.org/images/C9OQH-2w3g-1Ayj08mjYLwlpI46QAbxgtyqa)

La classification binaire est possible depuis que l'algorithme [perceptron](https://en.wikipedia.org/wiki/Perceptron) a été inventé en 1957. Si vous pensez que l'IA est surévaluée maintenant, le _New York Times_ rapportait en 1958 que l'invention était le début d'un ordinateur qui serait "capable de marcher, parler, voir, écrire, se reproduire et être conscient de son existence". Bien que les machines à perceptron, comme le [Mark 1](https://blog.knoldus.com/2017/09/12/introduction-to-perceptron-neural-network/), aient été conçues pour la reconnaissance d'images, en réalité, elles ne peuvent discerner que des motifs linéairement séparables. Cela les empêche d'apprendre les motifs complexes présents dans la plupart des médias visuels.

Pas étonnant que le monde ait été désillusionné et qu'un [hiver de l'IA](https://en.wikipedia.org/wiki/AI_winter) s'ensuivit. Depuis lors, les [perceptions multicouches](https://en.wikipedia.org/wiki/Multilayer_perceptron) (populaires dans les années 1980) et les [réseaux de neurones convolutifs](https://en.wikipedia.org/wiki/Convolutional_neural_network) (pionniers par [Yann LeCun](http://yann.lecun.com/) en 1998) ont largement surpassé les [perceptions monocouches](http://lcn.epfl.ch/tutorial/english/perceptron/html/intro.html) dans les tâches de reconnaissance d'images.

Avec de grands ensembles de données étiquetées comme [ImageNet](http://www.image-net.org/) et une puissance de calcul [GPU](https://en.wikipedia.org/wiki/Graphics_processing_unit), des architectures de réseaux de neurones plus avancées comme [AlexNet](https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdfhttps://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf), [VGG](https://arxiv.org/pdf/1409.1556.pdf), [Inception](https://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Szegedy_Going_Deeper_With_2015_CVPR_paper.pdf), et [ResNet](https://arxiv.org/pdf/1512.03385.pdf) ont atteint des performances de pointe en vision par ordinateur.

#### API de vision par ordinateur et de reconnaissance d'images

Si vous êtes un ingénieur en apprentissage automatique, il est facile d'expérimenter et d'ajuster ces modèles en utilisant des modèles et des poids pré-entraînés dans [Keras/Tensorflow](https://keras.io/applications/) ou [PyTorch](http://pytorch.org/). Si vous n'êtes pas à l'aise pour ajuster les réseaux de neurones par vous-même, vous avez de la chance. Pratiquement tous les géants de la technologie et les startups prometteuses prétendent "démocratiser l'IA" en offrant des API de vision par ordinateur faciles à utiliser.

Laquelle est la meilleure ? Pour répondre à cette question, vous devriez clairement définir vos objectifs commerciaux, les cas d'utilisation du produit, les ensembles de données de test et les métriques de succès avant de pouvoir comparer les solutions les unes aux autres.

En l'absence d'une enquête sérieuse, nous pouvons au moins obtenir une idée générale des différents comportements de chaque plateforme en les testant avec notre problème de différencier un chihuahua d'un muffin.

#### Conduire le test

Pour ce faire, j'ai divisé le mème canonique en 16 images de test. Ensuite, j'utilise le [code open source](https://github.com/goberoi/cloudy_visionhttps://github.com/goberoi/cloudy_vision) écrit par l'ingénieur [Gaurav Oberoi](https://goberoi.com/) pour consolider les résultats des différentes API. Chaque image est poussée à travers les six API listées ci-dessus, qui retournent des étiquettes de haute confiance comme leurs prédictions. Les exceptions sont Microsoft, qui retourne à la fois des étiquettes et une légende, et [Cloudsight](https://cloudsight.ai/), qui utilise une technologie hybride humain-IA pour retourner une seule légende. C'est pourquoi Cloudsight peut retourner des légendes d'une précision inquiétante pour des images complexes, mais prend 10 à 20 fois plus de temps à traiter.

Voici un exemple de la sortie. Pour voir les résultats de toutes les 16 images de chihuahua contre muffin, [cliquez ici](http://www.topbots.com/downloads/code/vision/chihuahua_vs_muffin/).

![Image](https://cdn-media-1.freecodecamp.org/images/o-KK8nggi1ZmyE7EhqcGu2fqcdGkbSUbRRgW)

À quel point les API ont-elles bien performé ? À part [Microsoft](https://www.microsoft.com/en-ca), qui a confondu ce muffin avec un animal en peluche, toutes les autres API ont reconnu que l'image était de la nourriture. Mais il n'y avait pas d'accord sur le fait que la nourriture était du pain, du gâteau, des biscuits ou des muffins. Google était la seule API à identifier avec succès le muffin comme l'étiquette la plus probable.

Regardons un exemple de chihuahua.

![Image](https://cdn-media-1.freecodecamp.org/images/tX48QszsaY1RK1WmvVDWHUHt4kFIrkR-8BaK)

Encore une fois, les API ont plutôt bien performé. Toutes ont réalisé que l'image était un chien, bien que quelques-unes aient manqué la race exacte.

Il y a eu des échecs certains, cependant. Microsoft a retourné une légende clairement erronée à trois reprises, décrivant le muffin comme un animal en peluche ou un ours en peluche.

![Image](https://cdn-media-1.freecodecamp.org/images/6xtzbea81RgWkMAfu5lLoDKjj3jNY8HRZph1)

Google était l'identificateur ultime de muffins, retournant "muffin" comme son étiquette de plus haute confiance pour 6 des 7 images de muffins dans l'ensemble de test. Les autres API n'ont pas retourné "muffin" comme première étiquette pour aucune image de muffin, mais ont plutôt retourné des étiquettes moins pertinentes comme "pain", "biscuit" ou "cupcake".

Cependant, malgré sa série de succès, Google a échoué sur cette image spécifique de muffin, retournant "museau" et "groupe de races de chiens" comme prédictions.

![Image](https://cdn-media-1.freecodecamp.org/images/0ZsE4QYdBUOXYYKamg0ghO4bhncJgBL7L3WO)

Même les plateformes d'apprentissage automatique les plus avancées au monde sont trompées par notre défi facétieux de chihuahua contre muffin. Un tout-petit humain bat l'apprentissage profond lorsqu'il s'agit de déterminer ce qui est de la nourriture et ce qui est Fido.

#### Alors, quelle est la meilleure API de vision par ordinateur ?

Pour découvrir la réponse à ce mystère insaisissable, vous devrez vous rendre sur TOPBOTS pour [lire l'article original en entier](https://www.topbots.com/chihuahua-muffin-searching-best-computer-vision-api/) !