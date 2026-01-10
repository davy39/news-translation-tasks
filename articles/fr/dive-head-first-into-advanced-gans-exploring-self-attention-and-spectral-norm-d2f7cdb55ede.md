---
title: 'Plongez tête première dans les GAN avancés : exploration de l''auto-attention
  et de la norme spectrale'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-21T17:11:56.000Z'
originalURL: https://freecodecamp.org/news/dive-head-first-into-advanced-gans-exploring-self-attention-and-spectral-norm-d2f7cdb55ede
coverImage: https://cdn-media-1.freecodecamp.org/images/1*gdU07yYr2i8DLUs2ukj32g.png
tags:
- name: Deep Learning
  slug: deep-learning
- name: Machine Learning
  slug: machine-learning
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: TensorFlow
  slug: tensorflow
seo_title: 'Plongez tête première dans les GAN avancés : exploration de l''auto-attention
  et de la norme spectrale'
seo_desc: 'By Thalles Silva

  Lately, Generative Models are drawing a lot of attention. Much of that comes from
  Generative Adversarial Networks (GANs). Invented by Goodfellow et al, GANs are a
  framework in which two players compete with one another. The two actor...'
---

Par Thalles Silva

Récemment, les modèles génératifs attirent beaucoup d'attention. Une grande partie de cela provient des réseaux antagonistes génératifs (GANs). Inventés par [Goodfellow et al](https://arxiv.org/abs/1406.2661), les GANs sont un cadre dans lequel deux joueurs sont en compétition l'un avec l'autre. Les deux acteurs, le générateur **G** et le discriminateur **D**, sont tous deux représentés par des approximateurs de fonction. De plus, ils jouent différents rôles dans le jeu.

Étant donné des données d'entraînement **Dt**, **G** crée des échantillons dans une tentative de mimiquer ceux de la même distribution de probabilité que **Dt**.

**D**, en revanche, est un classificateur binaire commun. Il a deux tâches principales. Premièrement, il catégorise si son entrée reçue provient de la vraie distribution de données (**Dt**) ou de la distribution du générateur. De plus, **D** guide également **G** pour créer des échantillons plus réalistes en passant à **G** ses gradients. En fait, prendre les gradients de **D** est le seul moyen pour **G** d'optimiser ses paramètres.

Dans ce jeu, **G** prend du bruit aléatoire comme entrée et génère une image d'échantillon `Gsample`. Cet échantillon est conçu pour maximiser la probabilité de faire en sorte que **D** le confonde avec un échantillon provenant de l'ensemble d'entraînement réel **Dt**.

Pendant l'entraînement, la moitié du temps **D** reçoit des images de l'ensemble d'entraînement **Dt**. L'autre moitié du temps, **D** reçoit des images du réseau générateur — `Gsample`. **D** est entraîné pour maximiser la probabilité d'assigner la bonne étiquette de classe aux deux : images réelles (de l'ensemble d'entraînement) et faux échantillons (de **G**). À la fin, l'espoir est que le jeu trouve un équilibre — l'équilibre de Nash.

Dans cette situation, **G** capturerait la distribution de probabilité des données. Et **D**, à son tour, ne serait pas en mesure de distinguer les échantillons réels des faux.

Les GANs ont été utilisés dans de nombreuses applications différentes au cours des dernières années. Certaines d'entre elles incluent : la génération de données synthétiques, la retouche d'images, l'apprentissage semi-supervisé, la super-résolution et la génération d'images à partir de texte.

Cependant, une grande partie des travaux récents sur les GANs se concentre sur le développement de techniques pour stabiliser l'entraînement. En effet, les GANs sont connus pour être instables pendant l'entraînement et très sensibles au choix des hyper-paramètres.

Dans ce contexte, cet article présente un aperçu de deux techniques pertinentes pour améliorer les GANs. Plus précisément, nous visons à décrire des méthodes récentes pour améliorer la qualité des échantillons de **G**. Pour ce faire, nous abordons deux techniques explorées dans l'article récent : [Self-Attention Generative Adversarial Networks](https://arxiv.org/abs/1805.08318).

Tout le code développé avec l'API Tensorflow Eager execution est disponible [ici](https://github.com/sthalles/blog-resources/tree/master/sagan).

J'ai une introduction plus approfondie [aux GANs ici](https://medium.freecodecamp.org/an-intuitive-introduction-to-generative-adversarial-networks-gans-7a2264a81394).

### Convolutional GANs

Le [Deep Convolutional GAN](https://arxiv.org/abs/1511.06434) (DCGAN) a été une étape majeure pour le succès des GANs génératifs d'images. Les DCGANs sont une famille de ConvNets qui imposent certaines contraintes architecturales pour stabiliser l'entraînement des GANs.

Dans les DCGANs, **G** est composé d'une série d'opérations de convolution transposée. Ces opérations prennent un vecteur de bruit aléatoire, **z**, et le transforment en augmentant progressivement ses dimensions spatiales tout en diminuant sa profondeur de volume de caractéristiques.

![Image](https://cdn-media-1.freecodecamp.org/images/0*AzDQxRt7QiVumFk8.png)
_Crédit : [Unsupervised Representation Learning with DCNNs](https://arxiv.org/abs/1511.06434" rel="noopener" target="_blank" title=")._

DCGAN a introduit une série de directives architecturales dans le but de stabiliser l'entraînement des GANs. Il préconise l'utilisation de convolutions à pas au lieu de couches de pooling. De plus, il utilise la normalisation par lots (BN) pour les réseaux générateurs et discriminateurs. Enfin, il utilise les activations ReLU et Tanh dans le générateur et les Leaky ReLUs dans le discriminateur.

Parlons de certaines de ces directives.

**La normalisation par lots fonctionne en normalisant les caractéristiques d'entrée d'une couche pour avoir une moyenne nulle et une variance unitaire**. BN était essentielle pour faire fonctionner des modèles plus profonds sans tomber dans **l'effondrement de mode**. L'effondrement de mode est la situation dans laquelle **G** crée des échantillons avec une très faible diversité. En d'autres termes, **G** retourne les mêmes échantillons pour différents signaux d'entrée. De plus, BN aide à traiter les problèmes dus à une mauvaise initialisation des paramètres.

De plus, DCGAN utilise des activations Leaky ReLU dans le réseau discriminateur. **Contrairement à la fonction ReLU régulière, les Leaky ReLUs permettent le passage d'un petit signal de gradient pour les valeurs négatives**. En conséquence, cela rend les gradients du discriminateur plus forts dans le générateur. Au lieu de passer un gradient (pente) de 0 dans la passe de rétropropagation pour les valeurs négatives, il passe un petit gradient négatif.

![Image](https://cdn-media-1.freecodecamp.org/images/1*mhOPoQOznlEnuOXifL2gPA.png)
_Fonction ReLU (droite). Leaky ReLU (gauche). Contrairement aux ReLUs, la dérivée d'une valeur négative, sur la fonction Leaky ReLU, est non nulle._

Les directives architecturales introduites par les DCGANs sont encore présentes dans la conception des modèles récents. Cependant, une grande partie du travail se concentre sur la manière de rendre l'entraînement des GANs plus stable.

### Self-Attention GANs

Self-Attention pour les réseaux antagonistes génératifs (SAGANs) est l'une de ces conceptions. Récemment, les techniques d'attention ont été explorées, avec succès, dans des problèmes comme la traduction automatique. Les Self-Attention GANs ont une architecture qui permet à **G** de modéliser la dépendance à longue portée. L'idée clé est de permettre à **G** de produire des échantillons avec des informations de détail globales.

Si nous regardons le modèle DCGAN, nous voyons que les GANs réguliers sont fortement basés sur les convolutions. Ces opérations utilisent un champ réceptif local, le noyau de convolution, pour apprendre des représentations. **Les convolutions ont des propriétés très intéressantes telles que le partage de paramètres et l'invariance par translation**.

Un Deep ConvNet typique apprend des représentations de manière **hiérarchique**. Pour un ConvNet de classification d'images régulier, des caractéristiques simples comme les bords et les coins sont apprises dans les premières couches. Pourtant, les ConvNets sont capables d'utiliser ces représentations simples pour en apprendre de plus complexes. **En bref, les ConvNets apprennent des représentations qui sont exprimées en termes de représentations plus simples**. Par conséquent, la dépendance à longue portée peut être difficile à apprendre.

En effet, cela peut n'être possible que pour les vecteurs de caractéristiques de basse résolution. Le problème est que, à cette granularité, la quantité de perte de signal est telle qu'il devient difficile de modéliser les détails à longue portée.

Jetez un coup d'œil à ces images d'échantillons :

![Image](https://cdn-media-1.freecodecamp.org/images/0*Y6A44HjiaSmE1s0L.png)
_Crédits : [Unsupervised Representation Learning with DCNNs](https://arxiv.org/abs/1511.06434" rel="noopener" target="_blank" title=")._

Ces images proviennent du modèle DCGAN entraîné sur ImageNet. Comme le souligne [Self-Attention GANs](https://arxiv.org/abs/1805.08318), la plupart du contenu des images qui n'exhibe pas de formes élaborées semble correct. En d'autres termes, les GANs n'ont généralement pas de problèmes à modéliser du contenu moins structuré comme le ciel ou l'océan.

Néanmoins, la tâche de création de formes géométriquement complexes, telles que des animaux à quatre pattes, est bien plus difficile. Cela est dû au fait que les contours géométriques compliqués demandent des détails à longue portée que la convolution, par elle-même, pourrait ne pas saisir. C'est là que l'attention entre en jeu.

L'idée est de donner des informations provenant d'un espace de caractéristiques plus large à **G**, et non seulement de la plage du noyau de convolution. En faisant cela, **G** peut créer des échantillons avec une résolution de détails fins.

### Implémentation

En général, étant donné les caractéristiques d'entrée d'une couche de convolution **L**, la première étape consiste à transformer **L** en trois représentations différentes. Nous convoluons **L** en utilisant des convolutions **1x1** pour obtenir trois espaces de caractéristiques : **f**, **g** et **h**.

Ici, nous utilisons **f** et **g** pour calculer l'attention. Pour ce faire, nous combinons linéairement **f** et **g** en utilisant une multiplication matricielle. Le résultat est alimenté dans une couche softmax.

![Image](https://cdn-media-1.freecodecamp.org/images/0*IYNfvhOuMJcT1-3-.png)
_Crédits : [Self-Attention GANS](https://arxiv.org/abs/1805.08318" rel="noopener" target="_blank" title=")._

Le tenseur résultant est combiné linéairement avec **h** et, enfin, mis à l'échelle par **gamma**. **Notez** que gamma commence à 0.

Au début de l'entraînement, gamma annule les couches d'attention. Par conséquent, le réseau ne repose que sur les représentations locales des couches de convolution régulières. Cependant, à mesure que gamma reçoit des mises à jour de descente de gradient, le réseau permet progressivement le passage de signaux provenant de champs non locaux.

De plus, notez que les vecteurs de caractéristiques **f** et **g** ont des dimensions différentes de **h**. En fait, **f** et **g** utilisent huit fois moins de filtres de convolution que **h**.

Voici le code complet pour le module d'auto-attention :

### Normalisation spectrale

Précédemment, [Miyato et al](https://arxiv.org/abs/1802.05957) ont proposé une technique de normalisation appelée **normalisation spectrale** (SN). En quelques mots, SN contraint la constante de Lipschitz des filtres de convolution. Les auteurs ont utilisé SN comme un moyen de stabiliser l'entraînement du réseau **D**. En pratique, cela a très bien fonctionné.

Cependant, il y a un problème fondamental lors de l'entraînement d'un **D** normalisé. Les travaux antérieurs ont montré que les **D** réguliers rendent l'entraînement des GANs plus lent. Pour cette raison, certaines solutions consistent à utiliser des taux de mises à jour inégaux entre **G** et **D**. En d'autres termes, nous pouvons mettre à jour **D** plusieurs fois avant de mettre à jour **G**. Par exemple, un **D** régulier peut nécessiter cinq mises à jour ou plus pour une mise à jour de **G**.

Pour résoudre le problème de l'apprentissage lent et des mises à jour déséquilibrées, il existe une approche simple mais efficace. **Il est important de noter** que, dans le cadre des GANs, **G** et **D** s'entraînent ensemble. Dans ce contexte, [Heusel et al](https://arxiv.org/abs/1706.08500) ont introduit la règle de mise à jour à deux échelles de temps (TTUR) dans l'entraînement des GANs. Elle consiste à fournir des taux d'apprentissage différents pour optimiser **G** et **D**.

Ici, **D** s'entraîne avec un taux d'apprentissage quatre fois supérieur à celui de **G** — 0,004 et 0,001, respectivement. Un taux d'apprentissage plus élevé signifie que **D** absorbera une plus grande partie du signal de gradient. Par conséquent, un taux d'apprentissage plus élevé atténue le problème de l'apprentissage lent du **D** régulier. De plus, cette approche permet d'utiliser le même taux de mises à jour pour **G** et **D**. En fait, nous utilisons un intervalle de mise à jour 1:1 entre **G** et **D**.

De plus, [cet article](https://sthalles.github.io/advanced_gans/Retrieved) a montré que les générateurs bien conditionnés sont causalement liés à la performance des GANs. Étant donné cela, [Self-Attention for GANs](https://arxiv.org/abs/1805.08318) a proposé d'utiliser SN pour stabiliser l'entraînement du réseau générateur également. Pour **G**, la normalisation spectrale empêche les paramètres de devenir très grands et évite les gradients indésirables.

#### Implémentation

Il est **important de noter** que l'algorithme SN introduit par [Miyato et al](https://sthalles.github.io/advanced_gans/#2) est une **approximation itérative**. Il définit que, pour chaque couche W, la norme spectrale utilisée pour régulariser chaque couche de convolution **W** est la plus grande valeur singulière de **W**.

Cependant, appliquer la décomposition en valeurs singulières à chaque étape peut être coûteux en calcul. Au lieu de cela, [Miyato et al](http://arxiv.org/abs/1802.05957) utilise la **méthode de l'itération de puissance** pour estimer la SN de chaque couche.

Pour implémenter SN en utilisant l'exécution eager de Tensorflow avec les couches Keras, nous avons dû télécharger et modifier le fichier [convolutions.py](https://github.com/keras-team/keras/blob/master/keras/layers/convolutional.py). Le code complet peut être consulté [ici](https://github.com/sthalles/blog-resources/blob/master/sagan/libs/convolutions.py). Ci-dessous, nous montrons les parties essentielles de l'algorithme.

Pour commencer, nous initialisons aléatoirement un vecteur `u` comme suit :

```
self.u = K.random_normal_variable([1, units], 0, 1, dtype=self.dtype)
```

Comme le montre l'algorithme 1 ci-dessous, la méthode de l'itération de puissance calcule les distances **l2** entre la combinaison linéaire du vecteur **u** et les noyaux de convolution **Wi**. De plus, la SN est calculée sur les poids des noyaux non normalisés.

![Image](https://cdn-media-1.freecodecamp.org/images/0*5kW08LlQAMr4WmDo.png)

Notez que, pendant l'entraînement, les valeurs de 9, calculées dans l'itération de puissance, sont utilisées comme valeurs initiales de **u** dans l'itération suivante. Cette stratégie permet à l'algorithme d'obtenir de très bonnes estimations en utilisant seulement un tour de l'itération de puissance. De plus, pour normaliser les poids des noyaux, nous les divisons par l'estimation actuelle de la SN.

### Détails de l'entraînement

Nous avons entraîné une version personnalisée du modèle SAGAN en utilisant SN et l'auto-attention. Nous avons utilisé le module `tf.keras` de Tensorflow et l'API Eager execution.

**G** prend un vecteur aléatoire **z** et génère des images RGB de 128x128. Toutes les couches, y compris les couches denses, utilisent SN. De plus, **G** utilise la normalisation par lots et les activations ReLU. Il utilise également l'auto-attention entre les cartes de caractéristiques de milieu à haute résolution. Comme dans l'implémentation originale, nous avons placé la couche d'attention pour qu'elle agisse sur les cartes de caractéristiques de dimensions 32x32.

**D** utilise également la normalisation spectrale (toutes les couches). Il prend des échantillons d'images RGB de taille 128x128 et produit une probabilité non mise à l'échelle. Il utilise des Leaky ReLUs avec un paramètre alpha de 0,02. Comme **G**, il a une couche d'auto-attention fonctionnant avec des cartes de caractéristiques de dimensions 32x32.

![Image](https://cdn-media-1.freecodecamp.org/images/0*x5mm4VjCiqTy3Jfh.png)

L'objectif est de minimiser la version hinge de la perte antagoniste. Pour ce faire, nous avons entraîné **G** et **D** de manière alternée, en utilisant l'optimiseur Adam, pendant 200 étapes d'entraînement.

![Image](https://cdn-media-1.freecodecamp.org/images/0*2usKJJav9LSApkjL.png)

Pour cette tâche, nous avons utilisé le jeu de données [Large-scale CelebFaces Attributes (CelebA)](http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html).

Voici les résultats.

![Image](https://cdn-media-1.freecodecamp.org/images/0*GXgPVwbtStMlNlGI.png)

Merci d'avoir lu !

![Image](https://cdn-media-1.freecodecamp.org/images/1*RzOHqzrJEIrB5ZY0nJAcvg.gif)

Publié à l'origine sur [sthalles.github.io](https://sthalles.github.io/advanced_gans/).