---
title: Comment entraîner votre propre FaceID ConvNet en utilisant l'exécution Eager
  de TensorFlow
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-27T00:30:39.000Z'
originalURL: https://freecodecamp.org/news/how-to-train-your-own-faceid-cnn-using-tensorflow-eager-execution-6905afe4fd5a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*A7z_szJKJywdj-0AybLLCA.jpeg
tags:
- name: Deep Learning
  slug: deep-learning
- name: Machine Learning
  slug: machine-learning
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: TensorFlow
  slug: tensorflow
seo_title: Comment entraîner votre propre FaceID ConvNet en utilisant l'exécution
  Eager de TensorFlow
seo_desc: 'By Thalles Silva

  Faces are everywhere — from photos and videos on social media websites, to consumer
  security applications like the iPhone Xs FaceID.

  In this context, computer vision, applied to faces, has many subareas. These include
  face detection,...'
---

Par Thalles Silva

Les visages sont partout — des photos et vidéos sur les sites de réseaux sociaux, aux applications de sécurité grand public comme le FaceID de l'iPhone Xs.

Dans ce contexte, la vision par ordinateur, appliquée aux visages, comporte de nombreuses sous-catégories. Celles-ci incluent la détection, la reconnaissance et le suivi des visages. De plus, avec l'avancement de l'apprentissage profond, ces solutions deviennent de plus en plus matures pour les applications commerciales.

Cet article vous montre, pièce par pièce, comment concevoir et entraîner votre propre réseau de neurones convolutifs (CNN) pour l'identification des visages. Ici, nous proposons une implémentation Tensorflow Eager des Siamese DenseNets.

Vous pouvez trouver le code complet [ici](https://github.com/sthalles/face-similarity).

### Siamese DenseNets

Un CNN Siamese est une classe de réseaux de neurones (NNs) qui contient deux ou plusieurs instances de réseau identiques. Le terme identique fait référence au fait que les deux NNs partagent la même configuration de conception et, surtout, leurs poids.

Pour comprendre les DenseNets, nous devons nous concentrer sur deux composants principaux de son architecture. Il s'agit du **bloc dense** et de la **couche de transition**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*lRttFe4ivoW_WurP1m6NZw.png)

En bref, un DenseNet est un empilement de blocs denses suivis de couches de transition. Un bloc se compose d'une série d'unités. Chaque unité contient deux convolutions. Chaque convolution est précédée d'une **normalisation par lots** (BN) et d'activations **unités linéaires rectifiées** (ReLU).

Chaque unité produit un nombre fixe de vecteurs de caractéristiques. Ce nombre est contrôlé par un seul paramètre — le **taux de croissance**. Essentiellement, il gère la quantité de nouvelles informations qu'une unité donnée permet de transmettre à la suivante.

De même, les couches de transition sont des composants simples. Elles sont conçues pour sous-échantillonner les vecteurs de caractéristiques traversant le réseau. Chaque couche de transition se compose d'une opération BN, suivie d'une convolution **1x1** plus un **2x2** average pooling.

La grande différence avec les autres CNNs réguliers est que chaque unité au sein d'un bloc dense est connectée à toutes les autres unités avant elle. Au sein d'un bloc, la **n-ième** unité reçoit en entrée les vecteurs de caractéristiques appris par les unités **n-1**, **n-2**, … jusqu'à la première unité de la pipeline. En d'autres termes, la conception des DenseNets permet un partage élevé de caractéristiques parmi ses unités.

![Image](https://cdn-media-1.freecodecamp.org/images/1*PrxZAYQ75OXX7KQfrR-d8w.png)
_Aperçu du DenseBlock. Chaque unité produit K vecteurs de caractéristiques. Les unités suivantes reçoivent les vecteurs de caractéristiques des unités précédentes par concaténation._

Comparés aux ResNets, les DenseNets réutilisent les caractéristiques par concaténation au lieu de sommation. Par conséquent, les DenseNets tendent à être plus compacts en nombre de paramètres que les ResNets. Intuitivement, chaque vecteur de caractéristiques appris par une unité donnée de DenseNet est réutilisé par toutes les unités suivantes au sein d'un bloc. Cela minimise la possibilité que différentes couches du réseau apprennent des caractéristiques redondantes.

Les ResNets et les DenseNets utilisent tous deux la conception populaire de la couche bottleneck. Elle se compose de 2 composants :

* une convolution **1x1** pour réduire les dimensions spatiales des caractéristiques
* une convolution plus large, dans ce cas une opération **3x3** pour l'apprentissage des caractéristiques

En ce qui concerne l'efficacité des paramètres et les opérations en virgule flottante par seconde (FLOPs), les DenseNets surpassent les ResNets d'une marge significative. Les DenseNets non seulement atteignent des taux d'erreur plus faibles sur ImageNets, mais nécessitent également moins de paramètres et moins de FLOPs que les ResNets.

![Image](https://cdn-media-1.freecodecamp.org/images/1*N4mWDkd_lW6xQE_em6TSUQ.png)

Un autre truc qui améliore la compacité du modèle est le facteur de compression. Cette procédure a lieu sur les couches de transition et vise à réduire le nombre de vecteurs de caractéristiques qui entrent dans le bloc dense suivant. Les DenseNets implémentent ce mécanisme en définissant un facteur, **θ**, entre 0 et 1. θ contrôle combien des caractéristiques actuelles sont autorisées à passer au bloc suivant. Cette technique permet aux DenseNets une réduction encore plus importante du nombre de vecteurs de caractéristiques, et d'être très efficaces en termes de paramètres.

### Apprendre les similarités de visages

Ce n'est pas une tâche de classification — nous ne voulons **pas** catégoriser les images en classes. Au lieu de cela, nous voulons apprendre une représentation qui peut décrire individuellement chaque entrée.

Plus précisément, nous voulons trouver des similarités entre les images d'entrée. Pour ce faire, nous avons besoin d'une représentation capable d'exprimer une relation entre deux choses comparables.

En pratique, nous voulons apprendre des vecteurs d'intégration pour représenter les relations entre les images de visages des personnes. Nous voulons des vecteurs avec les propriétés suivantes :

* Si deux images (**X1** et **X2**) sont similaires, nous voulons que la distance entre les 2 vecteurs de sortie soit aussi petite que possible
* Si **X1** et **X2** ne sont **pas** similaires, nous voulons que cette distance soit aussi grande que possible

Ci-dessous, nous représentons l'ensemble du **framework Siamese DenseNets pour l'apprentissage des intégrations de visages**. Les sections suivantes passent en revue les blocs de construction spécifiques de cette architecture.

![Image](https://cdn-media-1.freecodecamp.org/images/1*0YI4GLo6hy2d-9R0lGYFHw.png)

### La perte contrastive

Pour comprendre comment fonctionne la perte contrastive, la première chose à garder à l'esprit est qu'**elle fonctionne sur des paires d'images**.

Prenons les deux images ci-dessus comme exemple. À un moment donné, nous donnons la paire (**X1**, **X2**) au système avec les propriétés suivantes :

* si **X1** est considéré comme similaire à **X2**, nous lui donnons une étiquette de 0
* sinon, **X1** reçoit une étiquette de 1

Maintenant, définissons **Gw** comme une fonction paramétrique — un réseau de neurones. Son rôle est très simple, **Gw** mappe les entrées haute résolution vers des sorties basse résolution.

![Image](https://cdn-media-1.freecodecamp.org/images/1*7FUfHPZRVr5j6j6pE8Kscg.png)
_Réduction de l'entrée de haute dimension à une représentation de basse dimension (D < d)_

Nous voulons apprendre une fonction de distance paramétrée **Dw**, entre les entrées **X1** et **X2**. Il s'agit de la distance euclidienne entre les sorties de **Gw**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*bDWgZhvgdl-dhev_D7x1zA.png)

Notez que **m** est la **marge**. Elle définit le rayon autour de **Gw**. Elle contrôle comment les images dissemblables contribuent à la fonction de perte totale. C'est-à-dire, une paire d'images (**X1**, **X2**) de personnes différentes (classe) ne contribue à la perte que si la distance entre elles est dans la marge — si (**_m -Dw) >_** 0.

En d'autres termes, nous voulons optimiser le système de sorte que :

* Si la paire d'images est similaire (étiquette 0), nous minimisons la fonction de distance **Dw**.
* Si la paire d'images n'est **pas** similaire (étiquette 1), nous augmentons la fonction de distance **Dw**.

La fonction de perte finale et son implémentation dans Tensorflow sont définies comme suit :

![Image](https://cdn-media-1.freecodecamp.org/images/1*ucBtqLbzlKIyoGr4aaAxyw.png)

Il est **important** de noter comment nous calculons la distance à la ligne 2. Puisque cette fonction de perte **doit être différentiable** par rapport aux poids du modèle, nous devons nous assurer que les effets secondaires négatifs ne se produiront pas.

Notez que dans la partie **racine carrée** de l'équation, nous ajoutons un petit epsilon avant de calculer la racine carrée. Et la raison est très subtile. Dans le cas où le contenu à l'intérieur de la racine carrée est zéro, la racine carrée de 0 est également 0 — ce qui est bien.

![Image](https://cdn-media-1.freecodecamp.org/images/0*UlSeGcvopHIuWKNb.jpg)
_À w=0, la dérivée de l'opération **sqrt()** entraînerait une division par 0. Cela casserait votre code ou entraînerait un NaN en python._

Cependant, si le contenu est 0 et que nous calculons les gradients, **la dérivée de la racine carrée aurait une opération de division par 0**. Ce qui est mauvais.

En résumé, **assurez-vous toujours** que les routines que vous utilisez sont sûres sur le plan computationnel.

De plus, lors de la minimisation de la perte contrastive en utilisant la descente de gradient stochastique (SGD), il y a deux scénarios possibles.

Premièrement, si la paire d'échantillons d'entrée (**X1**, **X2**) est de la même classe (étiquette 0), la deuxième partie de l'équation est annulée. Dans cette situation, nous minimisons uniquement la distance entre les deux images de la même classe. En pratique, nous poussons les deux représentations à être aussi proches l'une de l'autre que possible.

![Image](https://cdn-media-1.freecodecamp.org/images/1*G4rPbxG5N4dCF2Hh08-p2Q.png)
_La perte contrastive regroupe les visages similaires ensemble (à l'intérieur d'une zone donnée) et éloigne les échantillons non similaires._

Dans le deuxième cas, si la paire d'entrée (**X1**, **X2**) n'est pas de la même classe (étiquette 1), la première partie de l'équation est annulée. Ensuite, dans le deuxième terme de la sommation, deux situations peuvent se produire.

Premièrement, si la distance entre les deux paires d'images **X1** et **X2** est supérieure à **m**, rien ne se passe. Notez que si **Dw >**; m, alors la différence entre eux sera également négative. Par conséquent, la dérivée de la fonction restante sera 0 — pas de gradient équivaut à pas d'apprentissage.

Cependant, si la distance **Dw** entre la paire d'entrée **X1** et **X2** est inférieure à **m**, la situation inverse se produit. Maintenant, le signal de gradient agira comme une force répulsive. En pratique, il éloignera les deux représentations l'une de l'autre.

### Dataset

Pour entraîner un CNN Siamese pour la similarité des visages, nous avons utilisé le populaire [Large-scale CelebFaces Attributes (CelebA) dataset](http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html). Il contient plus de 200k images de célébrités de 10 177 identités différentes. Pour faciliter le prétraitement des données, nous avons choisi la partie alignée et recadrée des visages du dataset. L'image suivante montre certains des échantillons du dataset.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Mu0B8Pvygp6B5d5ER7oG8A.png)
_Images d'échantillons de CelebA._

Pour utiliser la perte contrastive, nous devons construire le dataset de manière très spécifique. Basiquement, nous devons construire un dataset qui contient beaucoup de paires d'images de visages. Certaines d'entre elles provenant des mêmes personnes, d'autres de personnes différentes.

Pour simplifier, étant donné une image d'entrée **Xi**, nous devons trouver un ensemble d'échantillons **S = {X1, X2,…, Xj}** tel que **Xi** et **Xj** appartiennent à la même classe. En d'autres termes, **Xi** et **Xj** sont des images de visages de la même personne.

De la même manière, nous devons trouver un ensemble d'images **D = {S1, S2,…, Sj}** tel que **Sj** n'appartienne **pas** à la même classe que **Xi**.

Enfin, nous combinons l'image d'entrée **Xi** avec des échantillons des ensembles similaires et dissemblables. Pour chaque paire (**Xi, Xj**), si **Xj** appartient à l'ensemble des échantillons similaires **S**, nous attribuons une étiquette de 0 à la paire, sinon, elle reçoit une étiquette de 1.

### Détails de l'entraînement

Nous avons utilisé la conception DenseNet-121 [comme décrit dans l'article original](https://liuziwei7.github.io/projects/FaceAttributes.html). Le paramètre de taux de croissance (k) a été fixé à 32. Au lieu de la couche entièrement connectée 1000D à la fin, nous apprenons des vecteurs d'intégration de taille 32.

![Image](https://cdn-media-1.freecodecamp.org/images/1*1Lcn_gfoA1sZFBvvivCHhQ.png)

Pour optimiser les paramètres du modèle, nous avons utilisé l'optimiseur Adam avec un calendrier de taux d'apprentissage cyclique. Inspiré par la super-convergence de fast.ai, nous avons fixé le paramètre **beta2** d'Adam à 0,99 et appliqué une politique cyclique à **beta1**.

De cette manière, les deux paramètres : — le taux d'apprentissage et **beta1** — varient de manière cyclique entre une valeur maximale et minimale. En termes simples, tandis que le taux d'apprentissage augmente, **beta1** diminue dans un intervalle fixe.

![Image](https://cdn-media-1.freecodecamp.org/images/1*MQvSXVeQ9j896fTRBPvoqw.png)

### Résultats

Les résultats sont très bons.

Pour ces exemples, un seul seuil de 1 classerait correctement la plupart des échantillons. De plus, le réseau est invariant à de nombreuses transformations des images d'entrée. Ces transformations incluent les variations de luminosité et de contraste, la taille du visage, la pose et l'alignement. Il est invariant aux petits changements dans l'apparence des personnes tels que l'âge, la coupe de cheveux, les chapeaux et les lunettes.

La valeur de similarité ci-dessous est plus petite pour les visages similaires et plus élevée pour les visages dissemblables. Les étiquettes de 0 signifient que la paire d'images provient de la même personne.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ki0Hmvi9HrnCaSY2HOtHeA.png)

**Merci d'avoir lu !**

### Pour plus de choses intéressantes sur l'apprentissage profond, consultez

[**Plongez tête la première dans les GANs avancés : exploration de l'auto-attention et de la norme spectrale**](https://medium.freecodecamp.org/dive-head-first-into-advanced-gans-exploring-self-attention-and-spectral-norm-d2f7cdb55ede)  
[_Récemment, les modèles génératifs attirent beaucoup d'attention. Une grande partie de cela vient des réseaux adverses génératifs..._medium.freecodecamp.org](https://medium.freecodecamp.org/dive-head-first-into-advanced-gans-exploring-self-attention-and-spectral-norm-d2f7cdb55ede)[**Plongez dans les réseaux de segmentation sémantique convolutionnelle profonde et Deeplab_V3**](https://medium.freecodecamp.org/diving-into-deep-convolutional-semantic-segmentation-networks-and-deeplab-v3-4f094fa387df)  
[_Les réseaux de neurones convolutionnels profonds (DCNNs) ont connu un succès remarquable dans diverses applications de vision par ordinateur..._medium.freecodecamp.org](https://medium.freecodecamp.org/diving-into-deep-convolutional-semantic-segmentation-networks-and-deeplab-v3-4f094fa387df)

![Image](https://cdn-media-1.freecodecamp.org/images/1*RzOHqzrJEIrB5ZY0nJAcvg.gif)