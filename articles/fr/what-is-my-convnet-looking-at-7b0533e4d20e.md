---
title: Le monde à travers les yeux d'une voiture autonome
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-02-08T01:43:10.000Z'
originalURL: https://freecodecamp.org/news/what-is-my-convnet-looking-at-7b0533e4d20e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*N6jPYd98Pb5s5j2-2oiUbA.png
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Data Science
  slug: data-science
- name: Deep Learning
  slug: deep-learning
- name: self-driving cars
  slug: self-driving-cars
- name: technology
  slug: technology
seo_title: Le monde à travers les yeux d'une voiture autonome
seo_desc: 'By David Brailovsky

  Visualizing which part of an image a neural network uses to recognize traffic lights


  In my last post I described how I trained a ConvNet (Convolutional Neural Network)
  to recognize traffic lights in dash-cam images. The best perf...'
---

Par David Brailovsky

#### Visualisation de la partie d'une image qu'un réseau de neurones utilise pour reconnaître les feux de circulation

![Image](https://cdn-media-1.freecodecamp.org/images/vK9KkDwVqbLFvPzIGqGhxJGE0xUjsRJfAp5p)

Dans mon [dernier article](https://medium.com/@davidbrai/recognizing-traffic-lights-with-deep-learning-23dae23287cc), j'ai décrit comment j'ai entraîné un ConvNet (Convolutional Neural Network) à reconnaître les feux de circulation dans des images de caméra embarquée. Le meilleur réseau unique a atteint une précision impressionnante de >94%.

Bien que les ConvNets soient très bons pour apprendre à classer des images, ils sont aussi quelque peu une boîte noire. Il est difficile de dire ce qu'ils font une fois qu'ils sont entraînés. Puisque je n'ai jamais explicitement "dit" au réseau de se concentrer sur les feux de circulation, il est possible qu'il utilise d'autres indices visuels dans les images pour prédire la bonne classe. Peut-être qu'il cherche des voitures à l'arrêt pour prédire un feu rouge ? ?

Dans cet article, je décris une méthode très simple et utile pour visualiser quelle partie de l'image le réseau utilise pour sa prédiction. L'approche consiste à occulter des parties de l'image et à voir comment cela change la prédiction du réseau. Cette approche a été décrite dans "[Visualizing and Understanding Convolutional Networks](https://arxiv.org/abs/1311.2901)".

Les voitures autonomes d'aujourd'hui utilisent des méthodes beaucoup plus sophistiquées pour détecter les objets dans une scène, ainsi que de nombreux autres capteurs comme entrées. Le ConvNet que nous examinons tout au long de cet article doit être considéré comme une version simplifiée de ce que les voitures autonomes utilisent réellement. Néanmoins, la méthode de visualisation décrite dans cet article peut être utile et adaptée pour différents types d'applications de réseaux de neurones.

Vous pouvez télécharger un fichier notebook avec le code que j'ai utilisé depuis [ici](https://github.com/davidbrai/deep-learning-traffic-lights/blob/master/analysis/sliding_patch.ipynb).

### Exemple #1

J'ai commencé avec l'image suivante qui contient un feu de circulation rouge :

![Image](https://cdn-media-1.freecodecamp.org/images/KTlbrjx6JvRHMd8w82EwsyKtSwnW0aCpop7G)
_Source : [Nexar challenge](https://challenge.getnexar.com/challenge-1" rel="noopener" target="_blank" title=")_

Le réseau prédit que cette image contient un feu de circulation rouge avec une probabilité de 99,99 %. Ensuite, j'ai généré de nombreuses versions de cette image avec un patch carré gris à différentes positions. Plus précisément, un carré glissant de 64 x 64 avec un pas de 16 pixels.

![Image](https://cdn-media-1.freecodecamp.org/images/OUhtNgvyDE0AlualytC2cpZt4Y7gVQXXQzeq)
_Exemple d'image avec un patch carré gris de 64x64_

J'ai passé chaque image à travers le réseau et j'ai enregistré la probabilité qu'il prédisait pour la classe "rouge". Ci-dessous, vous pouvez voir un graphique de carte thermique de ces probabilités enregistrées.

![Image](https://cdn-media-1.freecodecamp.org/images/P2cTCJcoi3b3-CSFNp3W-W14MHfFwnV2sUgJ)

La couleur représente la probabilité de la classe "rouge" lorsqu'un patch carré couvrait cette position. Une couleur plus foncée signifie une probabilité plus faible. Il y a un effet de lissage car j'ai moyenné les probabilités que chaque pixel a obtenues pour tous les patches qui le couvraient.

J'ai ensuite tracé la carte thermique sur l'image originale :

![Image](https://cdn-media-1.freecodecamp.org/images/Y0gmlQIpJg-f9If3OZKQjepei0gNMBhcDDlt)

Très cool ! ? La probabilité la plus faible est exactement lorsque le feu de circulation est couvert. J'ai ensuite répété ce processus avec une taille de patch plus petite de 16x16 :

![Image](https://cdn-media-1.freecodecamp.org/images/IxSrdqG7RqAjBhV7BUfXIGXUShVYDQksgHGW)

Exactement sur le feu de circulation ! ?

### Exemple #2

J'ai continué à examiner plus d'images et je suis tombé sur cet exemple intéressant :

![Image](https://cdn-media-1.freecodecamp.org/images/dimBkYiFCX-xeEq3uUqqMqECBIayDn8Rj712)
_Source : [Nexar challenge](https://challenge.getnexar.com/challenge-1" rel="noopener" target="_blank" title=")_

Le ConvNet a prédit la classe "vert" avec une probabilité de 99,99 % pour cette image. J'ai généré une autre carte thermique en faisant glisser un patch de taille 32x32 avec un pas de 16 pixels :

![Image](https://cdn-media-1.freecodecamp.org/images/uDhxIZmJAzm8gqbkq5cx3cTt-5xlDtvIeB-8)

Hmm... quelque chose ne va pas ?. La probabilité la plus faible pour "vert" qu'une image patchée a obtenue était de 99,909 %, ce qui est encore très élevé. L'image avec la probabilité la plus faible était :

![Image](https://cdn-media-1.freecodecamp.org/images/baJUE9N20Z0w034a99WHzOyKEWkQMJU9gkTl)

Cela semble en fait correct, cela couvre parfaitement le feu de circulation. Alors pourquoi le réseau prédisait-il toujours "vert" avec une probabilité élevée ? Cela pourrait être dû au deuxième feu de circulation vert dans l'image. J'ai répété le processus de patch glissant sur l'image patchée ci-dessus et j'ai tracé la carte thermique :

![Image](https://cdn-media-1.freecodecamp.org/images/T0zbx1OZ4IrHsUHAmsFqLMu3gi-9ZnLOa-ah)

Beaucoup mieux ! ? Après avoir caché le deuxième feu de circulation, la probabilité pour "vert" est tombée près de zéro, à 0,25 % pour être exact.

### Examiner les erreurs

Ensuite, je voulais voir si je pouvais apprendre quelque chose d'intéressant en utilisant cette technique pour comprendre certaines des erreurs de classification du réseau. Beaucoup d'erreurs étaient causées par la présence de deux feux de circulation dans la scène, l'un vert et l'autre rouge. Il était assez évident que l'autre feu de circulation était la partie de l'image qui avait causé l'erreur dans ces cas.

Un autre type d'erreur était lorsque le réseau prédisait qu'il n'y avait pas de feu de circulation dans la scène alors qu'il y en avait un. Malheureusement, cette technique n'était pas très utile pour comprendre la raison pour laquelle le réseau s'était trompé, car il n'y avait pas de partie spécifique de l'image sur laquelle il se concentrait.

Le dernier type d'erreur que j'ai examiné était lorsque le réseau prédisait un feu de circulation alors qu'il n'y en avait pas. Voir l'exemple ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/ZImlljaGDa1q-bwDeW17Lqo5X4tC6ccX6-zE)

Et avec la carte thermique tracée par-dessus :

![Image](https://cdn-media-1.freecodecamp.org/images/h5fbcX514Ny2A4jlbc4hYGG0q3YpoDDz8Gvw)

Il semble que le réseau ait confondu la lumière du panneau de stationnement avec un feu de circulation. Intéressant de voir que c'était seulement le bon panneau de stationnement et non celui de gauche.

### Conclusion

Cette méthode est très simple mais efficace pour obtenir des informations sur ce qu'un ConvNet examine dans une image. Malheureusement, elle ne nous dit pas _pourquoi_ il se concentre sur cette partie.

J'ai également expérimenté un peu avec la génération d'une carte de saillance comme décrit dans "[Deep Inside Convolutional Networks](https://arxiv.org/abs/1312.6034)", mais je n'ai pas obtenu de résultats visuellement satisfaisants.

Si vous connaissez d'autres méthodes intéressantes pour comprendre ce que font les ConvNets, n'hésitez pas à écrire un commentaire ci-dessous ?

*Si vous avez aimé lire cet article, n'hésitez pas à cliquer sur **F496** ci-dessous !*