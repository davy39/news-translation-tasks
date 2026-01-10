---
title: 'L''état de l''art du deep learning : une introduction à Mask R-CNN'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-20T05:33:28.000Z'
originalURL: https://freecodecamp.org/news/mask-r-cnn-explained-7f82bec890e3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ByJ4h3U6KGoCcd3z6_Bg9Q.png
tags:
- name: AI
  slug: ai
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Computer Vision
  slug: computer-vision
- name: Deep Learning
  slug: deep-learning
- name: Machine Learning
  slug: machine-learning
seo_title: 'L''état de l''art du deep learning : une introduction à Mask R-CNN'
seo_desc: 'By Ajay Uppili Arasanipalai

  Introduction

  From my experience as a time traveller, I can confidently say that autonomous driving
  is/was/will be all the craze. Mathematically, the hype around computer vision grows
  exponentially as a function of the inde...'
---

Par Ajay Uppili Arasanipalai

#### Introduction

D'après mon expérience en tant que voyageur temporel, je peux affirmer en toute confiance que la conduite autonome est/était/sera très tendance. Mathématiquement, l'engouement autour de la vision par ordinateur croît de manière exponentielle en fonction de l'index des itérations du temps de Planck. Je plaisante.

En tout cas, dans cet article, nous allons plonger dans certains des développements plus récents en vision par ordinateur avec le deep learning, et finalement construire un modèle appelé « Mask R-CNN ». Cet article devrait être assez intuitif, mais je m'attends à ce que vous connaissiez certains des modèles plus basiques pour la vision par ordinateur. Si vous pensez être prêt, commençons.

### Détection d'objets vs. Segmentation sémantique vs. Segmentation d'instances

Dans cet article, je suppose que vous êtes à l'aise avec les tâches et modèles de base du deep learning spécifiques à la vision par ordinateur, tels que les réseaux de neurones convolutifs (CNN), la classification d'images, etc. Si ces termes vous semblent du jargon, allez-y et lisez [cet article](https://medium.com/technologymadeeasy/the-best-explanation-of-convolutional-neural-networks-on-the-internet-fbb8b1ad5df8).

D'accord, passons maintenant aux choses amusantes. En plus du classique classificateur chien vs. chat que la plupart d'entre nous auront construit lors de notre voyage en deep learning, il y a beaucoup plus que nous pouvons faire avec la même idée de réseau de neurones.

Par exemple, au lieu de simplement nous dire ce qu'il y a dans une image, nous pouvons entraîner notre CNN à nous dire quelle partie de l'image l'a convaincu de prendre cette décision. Pour voir pourquoi cela est utile, assurez-vous de regarder ce [Ted talk](https://www.youtube.com/watch?v=TRzBk_KuIaM). Cela peut être fait en demandant au CNN de dessiner une boîte autour de l'objet, comme dans l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/1*RokhyqAOGI4x6oryPZqZmg.jpeg)
_Source : [https://i.ytimg.com/vi/EhcpGpFHCrw/maxresdefault.jpg](https://i.ytimg.com/vi/EhcpGpFHCrw/maxresdefault.jpg" rel="noopener" target="_blank" title=")_

En langage de deep learning, cette tâche est appelée détection d'objets, et elle est vraiment assez facile à implémenter. Tout d'abord, lors de la préparation de nos données, nous devons utiliser un outil pour dessiner des boîtes englobantes autour des images. Cela est assez facile à faire avec des outils en ligne gratuits. Ensuite, nous changeons la couche finale/de sortie du CNN en une couche softmax qui a 4 + k sorties — la coordonnée x de la boîte englobante, la coordonnée y de la boîte englobante, la hauteur de la boîte englobante, la largeur de la boîte englobante, et les scores de probabilité de classe pour k classes.

La première chose que vous pourriez demander est pourquoi nous choisissons d'apprendre des choses étranges comme les coordonnées x, y et la hauteur, la largeur. Ne pouvons-nous pas simplement apprendre les coordonnées (x, y) de chaque coin de la boîte ? Eh bien, nous pouvons — cependant, si nous apprenons 4 paires de variables, nous devons en apprendre 8 au total pour représenter la boîte. Cependant, si nous utilisons cette technique, nous n'avons besoin que de 4.

Une autre tâche intéressante que nous pouvons résoudre est la segmentation sémantique. Encore une fois, ce n'est qu'un terme fantaisiste pour ce qui est essentiellement colorier une image comme dans un livre de colorier pour enfants.

![Image](https://cdn-media-1.freecodecamp.org/images/1*NJkAS8w4P5QWKUL6EYpmtA.png)
_Source : [http://adas.cvc.uab.es/elektra/wp-content/uploads/sites/13/2016/05/CVC10_Frame3.png](http://adas.cvc.uab.es/elektra/wp-content/uploads/sites/13/2016/05/CVC10_Frame3.png" rel="noopener" target="_blank" title=")_

Similaire au cas de la détection d'objets, un outil gratuit pourrait être utilisé pour essentiellement colorier une image manuellement, ce qui est utilisé comme exemple de vérité terrain pour préparer un ensemble de données. Ici, notre réseau de neurones est entraîné à mapper chaque pixel de l'image d'entrée à une classe particulière. De manière brute, cela peut être fait en utilisant quelque chose appelé un réseau entièrement convolutif (FCN). Ce réseau est simplement une série de couches convolutives.

![Image](https://cdn-media-1.freecodecamp.org/images/1*1F5Ryd72qdJeVDiLltbBFQ.png)
_Source : [https://cdn-media-1.freecodecamp.org/images/1*wRkj6lsQ5ckExB5BoYkrZg.png](https://cdn-media-1.freecodecamp.org/images/1*wRkj6lsQ5ckExB5BoYkrZg.png" rel="noopener" target="_blank" title=")_

Ainsi, le FCN apprendrait (à travers l'art sombre et mystique du deep learning) le mappage d'une image d'entrée à une version « colorée » de celle-ci, qui met en évidence les différentes classes dans une image.

Une chose importante à noter est que la segmentation sémantique ne met pas en évidence les instances individuelles d'une classe différemment. Par exemple, s'il y avait 3 vaches dans une image, le modèle mettrait en évidence la zone qu'elles occupent, mais il ne pourrait pas distinguer une vache d'une autre. Si nous voulons ajouter cette fonctionnalité, nous devons étendre la tâche et introduire un autre terme pour compliquer le vocabulaire déjà énormément grand du deep learning — segmentation d'instances.

D'accord, ce n'était pas si mal, n'est-ce pas ? Le terme est assez explicite. Notre objectif est de segmenter ou de séparer chaque « instance » d'une classe dans une image. Cela devrait vous aider à visualiser ce que nous essayons d'atteindre :

![Image](https://cdn-media-1.freecodecamp.org/images/1*L2hjU8Eb6SnN--rzLwixBw.png)
_Source : [https://cdn-media-1.freecodecamp.org/images/1*lMEd6AcDmpH0mDzBHyiERw.png](https://cdn-media-1.freecodecamp.org/images/1*lMEd6AcDmpH0mDzBHyiERw.png" rel="noopener" target="_blank" title=")_

Le modèle réel que nous utilisons pour résoudre ce problème est en fait beaucoup plus simple que vous ne le pensez. La segmentation d'instances peut essentiellement être résolue en 2 étapes :

1. Effectuer une version de la détection d'objets pour dessiner des boîtes englobantes autour de chaque instance d'une classe
2. Effectuer une segmentation sémantique sur chacune des boîtes englobantes

Ce modèle simple et incroyable fonctionne en fait extrêmement bien. Il fonctionne parce que si nous supposons que l'étape 1 a une haute précision, alors la segmentation sémantique dans l'étape 2 est fournie avec un ensemble d'images qui sont garanties de n'avoir qu'une seule instance de la classe principale. Le travail du modèle dans l'étape 2 est simplement de prendre une image avec exactement une classe principale, et de prédire quels pixels correspondent à la classe principale (chat/chien/humain, etc.), et quels pixels correspondent à l'arrière-plan d'une image.

Un autre fait intéressant est que si nous sommes capables de résoudre le problème des boîtes englobantes multiples et le problème de la segmentation sémantique de manière indépendante, nous avons également essentiellement résolu la tâche de la segmentation d'instances ! La bonne nouvelle est que des modèles très puissants ont été construits pour résoudre ces deux problèmes, et mettre les 2 ensemble est une tâche relativement triviale.

Ce modèle particulier a un nom — Mask R-CNN (abréviation de « regional convolutional neural network »), et il a été construit par l'équipe de recherche en IA de Facebook (FAIR) en avril 2017.

Le principe de fonctionnement de Mask R-CNN est à nouveau assez simple. Tout ce qu'ils (les chercheurs) ont fait, c'est assembler 2 modèles existants de l'état de l'art et jouer avec l'algèbre linéaire (la recherche en deep learning en un mot). Le modèle peut être grossièrement divisé en 2 parties — un réseau de proposition de régions (RPN) et un classificateur de masques binaires.

La première étape consiste à obtenir un ensemble de boîtes englobantes qui pourraient éventuellement contenir un objet pertinent. Le terme à la mode du jour ici est RoI Align. Le réseau RoI Align fonctionne sur les principes de la détection d'objets (discutés ci-dessus, vous avez déjà oublié !), mais il produit plusieurs boîtes englobantes _possibles_ plutôt qu'une seule définitive. Ces boîtes sont affinées à l'aide d'un autre modèle de régression, que nous ne discuterons pas ici. Plus de détails sur le réseau RoI Align peuvent être trouvés [ici](https://medium.com/@steve101777/roi-pooling-and-roi-align-dd13bfece1df).

La deuxième étape consiste à effectuer le colorage. Contrairement à ce que l'on pourrait penser, cette étape est également assez facile ! Tout ce que vous avez à faire est d'appliquer le modèle existant de l'état de l'art pour la segmentation sémantique à chaque boîte englobante. La partie cool est que puisque nous sommes garantis d'avoir au plus 1 classe dans chaque boîte, nous devons simplement entraîner notre modèle de segmentation sémantique comme un classificateur binaire, ce qui signifie que nous devons seulement apprendre le mappage des pixels d'entrée à un 1/0. 1 représenterait la présence d'un objet, et 0 serait l'arrière-plan. Ensuite, pour un effet supplémentaire, nous pourrions colorier chacun des pixels qui mappent à 1 pour obtenir des résultats qui ressemblent à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*ByJ4h3U6KGoCcd3z6_Bg9Q.png)
_Source : [https://cdn-media-1.freecodecamp.org/images/1*E_5qBTrotLzclyaxsekBmQ.png](https://cdn-media-1.freecodecamp.org/images/1*E_5qBTrotLzclyaxsekBmQ.png" rel="noopener" target="_blank" title=")_

#### Conclusion

Les applications de cette technologie sont vastes. Certaines des utilisations les plus lucratives incluent la capture de mouvement, la conduite autonome et les systèmes de surveillance. Mais nous laisserons toutes les applications de cette technologie dans l'esprit du lecteur.

Pour la plupart, la segmentation d'instances est maintenant assez réalisable, et il est temps de commencer à penser à des moyens innovants d'utiliser cette idée de faire des algorithmes de vision par ordinateur au niveau pixel par pixel. Un bon exemple serait un nouvel algorithme cool appelé DensePose. Pour une raison inconnue, ce modèle ne reçoit pas beaucoup de presse. Mais le potentiel est plus grand que celui de la gravitation d'un trou noir !

En termes simples, pensez à DensePose comme un kinect à moindre coût. Il peut essentiellement faire tout ce qu'un système avancé de capture de mouvement peut faire pour une fraction du coût. En théorie, vous pourriez exécuter ce modèle sur un appareil à 10 $ comme un raspberry pi !

D'un point de vue théorique (aka le plus cool), cette technologie pourrait être étendue à d'autres types de réseaux de neurones (autres que les CNN et les FCN). L'idée principale ici est de prendre la portion la plus élémentaire de certaines données (un pixel dans ce cas), et de décider comment elle contribue à la structure globale.

Hypothétiquement, nous pourrions classer chaque échantillon individuel d'un signal et décider comment il contribue à une séquence de musique. Si nous sommes encore plus ambitieux, nous pourrions identifier quelles parties d'une séquence de musique sont les plus attrayantes, et les combiner avec des parties attrayantes d'autres chansons, résultant en une nouvelle façon de fusionner nos chansons préférées ensemble !

Sur une note plus sérieuse, nous pourrions utiliser la même technique pour des données plus importantes. Par exemple, nous pourrions entraîner un modèle Mask R-CNN à mettre en évidence les zones _exactes_ d'un scan IRM qui corréleraient avec certains schémas comportementaux/psychologiques, ou quelles sous-séquences d'ADN correspondent à certains traits particuliers, potentiellement résultant en des percées dans l'IA médicale.

Le modèle Mask R-CNN, à sa base, consiste à décomposer les données en ses blocs de construction les plus fondamentaux. En tant qu'êtres humains, nous avons des biais inhérents dans la façon dont nous regardons le monde. L'IA, en revanche, a le potentiel de regarder le monde de manières que nous, humains, ne pourrions même pas comprendre, et comme il a été dit un jour par un homme qui a maîtrisé l'art de chercher les vérités les plus fondamentales :

![Image](https://cdn-media-1.freecodecamp.org/images/0*1sJ2YoLd6akGeewj.)