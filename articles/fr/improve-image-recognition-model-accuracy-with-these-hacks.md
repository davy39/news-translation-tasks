---
title: Comment améliorer la précision de vos modèles de reconnaissance d'images
subtitle: ''
author: Jason
co_authors: []
series: null
date: '2021-11-29T17:09:30.000Z'
originalURL: https://freecodecamp.org/news/improve-image-recognition-model-accuracy-with-these-hacks
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/image-recognition-model-image.jpeg
tags:
- name: data analysis
  slug: data-analysis
- name: Deep Learning
  slug: deep-learning
- name: image recognition
  slug: image-recognition
- name: neural networks
  slug: neural-networks
seo_title: Comment améliorer la précision de vos modèles de reconnaissance d'images
seo_desc: 'These 7 tricks and tips will take you from 50% to 90% accuracy for your
  image recognition models in literally minutes.

  So, you have gathered a dataset, built a neural network, and trained your model.

  But despite the hours (and sometimes days) of work...'
---

Ces 7 astuces et conseils vous permettront de passer de 50 % à 90 % de précision pour vos modèles de reconnaissance d'images en quelques minutes.

Vous avez donc rassemblé un ensemble de données, construit un réseau de neurones et entraîné votre modèle.

Mais malgré les heures (et parfois les jours) de travail que vous avez investies pour créer le modèle, il produit des prédictions avec une précision de 50 à 70 %. Il y a de fortes chances que ce ne soit pas ce à quoi vous vous attendiez.

Voici quelques stratégies, ou astuces, pour améliorer les métriques de performance de votre modèle.

## 1. Obtenez plus de données

Les modèles de deep learning ne sont aussi puissants que les données que vous utilisez. L'une des façons les plus simples d'augmenter la précision de validation est d'ajouter plus de données. Cela est particulièrement utile si vous n'avez pas beaucoup d'instances d'entraînement.

Si vous travaillez sur des modèles de reconnaissance d'images, vous pouvez envisager d'augmenter la diversité de votre ensemble de données disponible en utilisant l'augmentation de données. Ces techniques incluent tout, du retournement d'une image sur un axe et de l'ajout de bruit au zoom sur l'image. Si vous êtes un ingénieur en machine learning expérimenté, vous pouvez également essayer l'augmentation de données avec des GANs.

En savoir plus sur [l'augmentation de données ici](https://bair.berkeley.edu/blog/2019/06/07/data_aug/).

Keras dispose d'une classe incroyable de prétraitement d'images pour effectuer l'augmentation de données : [ImageDataGenerator](https://keras.io/api/preprocessing/image/#imagedatagenerator-class).

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-119.png align="left")

*Faites attention à ce que la technique d'augmentation que vous utilisez ne change pas toute la classe d'une image. Par exemple, l'image d'un 3 retourné sur l'axe y n'a pas de sens ! [Source](https://bair.berkeley.edu/blog/2019/06/07/data_aug/" rel="noopener)*

## 2. Ajoutez plus de couches

Ajouter plus de couches à votre modèle augmente sa capacité à apprendre les caractéristiques de votre ensemble de données plus en profondeur. Cela signifie qu'il sera en mesure de reconnaître des différences subtiles que vous, en tant qu'humain, n'auriez peut-être pas remarquées.

Cette astuce dépend entièrement de la nature de la tâche que vous essayez de résoudre.

Pour des tâches complexes, comme la différenciation entre les races de chats et de chiens, l'ajout de plus de couches a du sens car votre modèle sera en mesure d'apprendre les caractéristiques subtiles qui différencient un caniche d'un Shih Tzu.

Pour des tâches simples, comme la classification des chats et des chiens, un modèle simple avec peu de couches suffira.

Plus de couches -> Modèle plus nuancé.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-120.png align="left")

*Photo par [Unsplash](https://unsplash.com/@alvannee?utm_source=medium&utm_medium=referral" rel="photo-creator noopener noopener noopener noopener noopener noopener noopener noopener noopener noopener noopener noopener noopener noopener noopener">Alvan Nee sur <a href="https://unsplash.com?utm_source=medium&utm_medium=referral" rel="photo-source noopener noopener noopener noopener noopener noopener noopener noopener noopener noopener noopener noopener noopener noopener noopener)*

## 3. Changez la taille de vos images

Lorsque vous prétraitez vos images pour l'entraînement et l'évaluation, il y a beaucoup d'expérimentations que vous pouvez faire concernant la taille de l'image.

Si vous choisissez une taille d'image trop petite, votre modèle ne sera pas en mesure de détecter les caractéristiques distinctives qui aident à la reconnaissance d'images.

À l'inverse, si vos images sont trop grandes, cela augmente les ressources informatiques requises par votre ordinateur et/ou votre modèle pourrait ne pas être assez sophistiqué pour les traiter.

Les tailles d'images courantes incluent 64x64, 128x128, 28x28 (MNIST) et 224x224 (VGG-16).

Gardez à l'esprit que la plupart des algorithmes de prétraitement ne tiennent pas compte du rapport d'aspect de l'image, donc les images de petite taille pourraient sembler avoir rétréci sur un certain axe.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-121.png align="left")

*Convertir une image d'une grande résolution à une petite taille, comme 28x28, se termine généralement par beaucoup de pixelisation qui tend à avoir des effets négatifs sur les performances de votre modèle. [Source](https://dribbble.com/shots/4829233-Pixelated-Mona-Lisa" rel="noopener)*

## 4. Augmentez les époques

Les *époques* sont essentiellement le nombre de fois où vous passez l'ensemble de données à travers le réseau de neurones. Entraînez progressivement votre modèle avec plus d'époques avec des intervalles de +25, +100, et ainsi de suite.

Augmenter les époques a du sens seulement si vous avez beaucoup de données dans votre ensemble de données. Cependant, votre modèle atteindra éventuellement un point où augmenter les époques n'améliorera pas la précision.

À ce stade, vous devriez envisager de jouer avec le taux d'apprentissage de votre modèle. Ce petit hyperparamètre dicte si votre modèle atteint son minimum global (l'objectif ultime pour les réseaux de neurones) ou se retrouve coincé dans un minimum local.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-122.png align="left")

*Le minimum global est l'objectif ultime pour les réseaux de neurones. [Source](https://www.dna-ghost.com/single-post/2018/03/13/Neural-network-Escaping-from-variety-of-non-global-minimum-traps" rel="noopener)*

## 5. Réduisez les canaux de couleur

Les canaux de couleur reflètent la dimensionalité de vos tableaux d'images. La plupart des images en couleur (RVB) sont composées de trois canaux de couleur, tandis que les images en niveaux de gris n'ont qu'un seul canal.

Plus les canaux de couleur sont complexes, plus l'ensemble de données est complexe et plus il faudra de temps pour entraîner le modèle.

Si la couleur n'est pas un facteur aussi significatif dans votre modèle, vous pouvez convertir vos images en couleur en niveaux de gris.

Vous pouvez même envisager d'autres espaces de couleur, comme HSV et L*a*b.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-123.png align="left")

*Les images RVB sont composées de trois canaux de couleur : rouge, vert et bleu. [Source](https://www.youtube.com/watch?v=ZqUotba3V5Y" rel="noopener)*

## 6. Apprentissage par transfert

L'apprentissage par transfert implique l'utilisation d'un modèle pré-entraîné, comme YOLO et ResNet, comme point de départ pour la plupart des tâches de vision par ordinateur et de traitement du langage naturel.

Les modèles pré-entraînés sont des modèles de deep learning de pointe qui ont été entraînés sur des millions et des millions d'échantillons, et souvent pendant des mois. Ces modèles ont une capacité énorme de détecter les nuances dans différentes images.

Ces modèles peuvent être utilisés comme base pour votre modèle. La plupart des modèles sont si bons que vous n'aurez pas besoin d'ajouter des couches de convolution et de pooling.

En savoir plus sur [l'utilisation de l'apprentissage par transfert](https://machinelearningmastery.com/transfer-learning-for-deep-learning/).

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-124.png align="left")

*L'apprentissage par transfert peut grandement améliorer la précision de votre modèle de ~50 % à 90 % ! Source : [Blog Nvidia](https://www.nvidia.com/content/dam/en-zz/en_sg/ai-innovation-day-2019/assets/pdf/9_NVIDIA-Transfer-Learning-Toolkit-for-Intelligent-Video-Analytics.pdf" rel="noopener)*

## Réflexions finales

Les astuces ci-dessus offrent une base pour optimiser un modèle. Pour vraiment affiner un modèle, vous devrez envisager de régler les divers hyperparamètres et fonctions impliqués dans votre modèle, comme le taux d'apprentissage (comme discuté ci-dessus), les fonctions d'activation, les fonctions de perte, et ainsi de suite.

Cette astuce vient avec un avertissement "J'espère que vous savez ce que vous faites" car il y a un champ plus large pour gâcher votre modèle.

### Toujours sauvegarder vos modèles

Toujours sauvegardez votre modèle chaque fois que vous apportez une modification à votre modèle de deep learning. Cela vous aidera à réutiliser une configuration précédente du modèle si elle offre une plus grande précision.

La plupart des frameworks de deep learning comme Tensorflow et Pytorch ont une méthode "save model".

```python
# Dans Tensorflow
model.save('model.h5') # Sauvegarde l'ensemble du modèle dans un seul artefact

# Dans Pytorch
torch.save(model, PATH)
```

Il existe d'innombrables autres façons d'optimiser davantage votre deep learning, mais les astuces décrites ci-dessus servent de base dans la partie optimisation du deep learning.

[*Tweetez-moi*](http://twitter.com/jasmcaus) pour me faire savoir quelle est votre astuce préférée !