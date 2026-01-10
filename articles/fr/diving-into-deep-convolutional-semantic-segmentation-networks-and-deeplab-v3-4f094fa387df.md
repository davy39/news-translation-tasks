---
title: Plongez dans les réseaux de segmentation sémantique par convolution profonde
  et Deeplab_V3
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-10T11:08:51.000Z'
originalURL: https://freecodecamp.org/news/diving-into-deep-convolutional-semantic-segmentation-networks-and-deeplab-v3-4f094fa387df
coverImage: https://cdn-media-1.freecodecamp.org/images/1*rZ1vDrOBWqISFiNL5OMEbg.jpeg
tags:
- name: Deep Learning
  slug: deep-learning
- name: Machine Learning
  slug: machine-learning
- name: neural networks
  slug: neural-networks
- name: 'tech '
  slug: tech
- name: TensorFlow
  slug: tensorflow
seo_title: Plongez dans les réseaux de segmentation sémantique par convolution profonde
  et Deeplab_V3
seo_desc: 'By Thalles Silva

  Deep Convolutional Neural Networks (DCNNs) have achieved remarkable success in various
  Computer Vision applications. Like others, the task of semantic segmentation is
  not an exception to this trend.

  This piece provides an introductio...'
---

Par Thalles Silva

Les réseaux de neurones convolutifs profonds (DCNN) ont connu un succès remarquable dans diverses applications de vision par ordinateur. Comme d'autres, la tâche de segmentation sémantique n'est pas une exception à cette tendance.

Cet article fournit une introduction à la segmentation sémantique avec une implémentation pratique de TensorFlow. Nous passerons en revue l'un des articles les plus pertinents sur la segmentation sémantique d'objets généraux — [Deeplab_v3](https://arxiv.org/abs/1706.05587). Vous pouvez cloner le notebook pour cet article [ici](https://github.com/sthalles/deeplab_v3).

### Segmentation sémantique

Les DCNN de classification d'images régulières ont une structure similaire. Ces modèles prennent des images en entrée et produisent une seule valeur représentant la catégorie de cette image.

Habituellement, les DCNN de classification ont quatre opérations principales : les convolutions, la fonction d'activation, le pooling et les couches entièrement connectées. Le passage d'une image à travers une série de ces opérations produit un vecteur de caractéristiques contenant les probabilités pour chaque étiquette de classe. Notez que dans cette configuration, nous catégorisons une image dans son ensemble. C'est-à-dire que nous attribuons une seule étiquette à une image entière.

![Image](https://cdn-media-1.freecodecamp.org/images/0*VMJtEUeJyA-XbDgF.jpg)
_Modèle standard de deep learning pour la reconnaissance d'images. Crédits image : [Convolutional Neural Network MathWorks](https://www.mathworks.com/discovery/convolutional-neural-network.html" rel="noopener" target="_blank" title=")._

Contrairement à la classification d'images, en segmentation sémantique, nous voulons prendre des décisions pour chaque pixel d'une image. Ainsi, pour chaque pixel, le modèle doit le classer comme l'une des classes prédéterminées. En d'autres termes, la segmentation sémantique signifie comprendre les images au niveau du pixel.

Gardez à l'esprit que la segmentation sémantique ne différencie pas les instances d'objets. Ici, nous essayons d'attribuer une étiquette individuelle à chaque pixel d'une image numérique. Ainsi, si nous avons deux objets de la même classe, ils finissent par avoir la même étiquette de catégorie. La segmentation d'instances est la classe de problèmes qui différencie les instances de la même classe.

![Image](https://cdn-media-1.freecodecamp.org/images/0*_VVeYr35i5GM6p6_.png)
_Différence entre la segmentation sémantique et la segmentation d'instances. (milieu) Bien qu'ils soient le même objet (bus), ils sont classés comme des objets différents. (gauche) Même objet, même catégorie._

Cependant, les DCNN régulières comme AlexNet et VGG ne sont pas adaptées aux tâches de prédiction dense. Premièrement, ces modèles contiennent de nombreuses couches conçues pour réduire les dimensions spatiales des caractéristiques d'entrée. Par conséquent, ces couches finissent par produire des vecteurs de caractéristiques très décimés qui manquent de détails précis. Deuxièmement, les couches entièrement connectées ont des tailles fixes et perdent des informations spatiales pendant le calcul.

Par exemple, au lieu d'avoir des couches de pooling et entièrement connectées, imaginez passer une image à travers une série de convolutions. Nous pouvons définir chaque convolution pour avoir un _stride de 1_ et un remplissage "SAME". **En faisant cela, chaque convolution préserve les dimensions spatiales de son entrée**. Nous pouvons empiler un ensemble de ces convolutions et avoir un modèle de segmentation.

![Image](https://cdn-media-1.freecodecamp.org/images/0*gAVdLPKbQphFjAYa.png)
_Réseau de neurones entièrement convolutif pour une tâche de prédiction dense. Notez l'absence de couches de pooling et entièrement connectées._

Ce modèle pourrait produire un tenseur de probabilités avec une forme _[W,H,C]_, où W et H représentent la largeur et la hauteur, et C est le nombre d'étiquettes de classe. L'application de la fonction _argmax_ (sur le troisième axe) nous donne un tenseur de forme _[W,H,1]_. Ensuite, nous calculons la perte d'entropie croisée entre chaque pixel des images de vérité terrain et nos prédictions. À la fin, nous faisons la moyenne de cette valeur et nous entraînons le réseau en utilisant la rétropropagation.

Il y a un problème avec cette approche, cependant. Comme nous l'avons mentionné, l'utilisation de convolutions avec un stride de 1 et un remplissage "SAME" préserve les dimensions d'entrée. Cependant, cela rendrait le modèle super coûteux en termes de consommation de mémoire et de complexité de calcul.

Pour atténuer ce problème, les réseaux de segmentation ont généralement trois composants principaux : les convolutions, les couches de sous-échantillonnage et de suréchantillonnage.

![Image](https://cdn-media-1.freecodecamp.org/images/0*3TxBI1xNIDm_Z615.png)
_Architecture encodeur-décodeur pour la segmentation sémantique d'images._

Il existe deux moyens courants de faire du sous-échantillonnage dans les réseaux de neurones : en utilisant le _stride de convolution_ ou les opérations de _pooling_ régulières. En général, le sous-échantillonnage a un objectif, et c'est de réduire les dimensions spatiales des cartes de caractéristiques données. Pour cette raison, le sous-échantillonnage nous permet d'effectuer des convolutions plus profondes sans trop de préoccupations de mémoire. Pourtant, ils le font au détriment de la perte de certaines caractéristiques dans le processus.

De plus, notez que la première partie de cette architecture ressemble beaucoup aux DCNN de classification habituels. Avec une exception, ils ne mettent pas en place de couches _entièrement connectées_.

Après la première partie, nous avons un vecteur de caractéristiques avec une forme [W, H, D] où W, H et D sont la largeur, la hauteur et la profondeur du tenseur de caractéristiques. Notez que les dimensions spatiales de ce vecteur compressé sont plus petites (mais plus denses) que l'entrée originale.

![Image](https://cdn-media-1.freecodecamp.org/images/0*dT0gcJavW_LQY4Dm.png)
_(Haut) Réseau VGG-16 dans sa forme originale. Notez les 3 couches entièrement connectées au sommet de la pile de convolution. (Bas) Modèle VGG-16 lors de la substitution de ses couches entièrement connectées par des convolutions 1x1. Ce changement permet au réseau de produire des cartes de chaleur grossières. Crédits image : [Fully Convolutional Networks for Semantic Segmentation](https://arxiv.org/abs/1411.4038" rel="noopener" target="_blank" title=")._

À ce stade, les DCNN de classification régulières produiraient un vecteur dense (non spatial) contenant des probabilités pour chaque étiquette de classe. Au lieu de cela, nous alimentons ce vecteur de caractéristiques compressé à une série de couches de suréchantillonnage. Ces couches travaillent à reconstruire la sortie de la première partie du réseau. **L'objectif est d'augmenter la résolution spatiale afin que le vecteur de sortie ait les mêmes dimensions que l'entrée**.

Habituellement, les couches de suréchantillonnage sont basées sur des _convolutions transposées à stride_. **Ces fonctions passent de couches profondes et étroites à des couches plus larges et moins profondes**. Ici, nous utilisons des convolutions transposées pour augmenter les dimensions du vecteur de caractéristiques à la valeur souhaitée.

Dans la plupart des articles, ces deux composants d'un réseau de segmentation sont appelés encodeur et décodeur. En bref, le premier « encode » ses informations dans un vecteur compressé utilisé pour représenter son entrée. Le second (le décodeur) travaille à reconstruire ce signal pour obtenir le résultat souhaité.

Il existe de nombreuses implémentations de réseaux basées sur des architectures encodeur-décodeur. FCNs, [SegNet](https://arxiv.org/abs/1511.00561) et [UNet](https://arxiv.org/abs/1505.04597) sont parmi les plus populaires. Par conséquent, nous avons vu de nombreux modèles de segmentation réussis dans une variété de domaines.

### Architecture du modèle

Contrairement à la plupart des conceptions encodeur-décodeur, Deeplab offre une approche différente de la segmentation sémantique. Il présente une architecture pour contrôler la décimation du signal et apprendre des caractéristiques contextuelles multi-échelles.

![Image](https://cdn-media-1.freecodecamp.org/images/0*vPNf03aFqjnKUjt8.png)

_Crédits image : [Rethinking Atrous Convolution for Semantic Image Segmentation](https://arxiv.org/abs/1706.05587)._

Deeplab utilise un ResNet pré-entraîné sur ImageNet comme principal réseau extracteur de caractéristiques. Cependant, il propose un nouveau bloc résiduel pour l'apprentissage de caractéristiques multi-échelles. Au lieu de convolutions régulières, le dernier bloc ResNet utilise des convolutions atrous. De plus, chaque convolution (dans ce nouveau bloc) utilise différents taux de dilatation pour capturer le contexte multi-échelle.

De plus, au sommet de ce nouveau bloc, il utilise le Atrous Spatial Pyramid Pooling (ASPP). ASPP utilise des convolutions dilatées avec différents taux dans une tentative de classification de régions d'une échelle arbitraire.

Pour comprendre l'architecture de Deeplab, nous devons nous concentrer sur trois composants. (i) L'architecture ResNet, (ii) les convolutions atrous et (iii) le Atrous Spatial Pyramid Pooling (ASPP). Passons en revue chacun d'eux.

### ResNets

ResNet est un DCNN très populaire qui a remporté la tâche de classification [ILSVRC 2015](http://image-net.org/challenges/LSVRC/2015/results). L'une des principales contributions de ResNets était de fournir un cadre pour faciliter l'entraînement de modèles plus profonds.

Dans sa forme originale, ResNets contient 4 blocs de calcul. Chaque bloc contient un nombre différent d'unités résiduelles. Ces unités effectuent une série de convolutions de manière spéciale. De plus, chaque bloc est entrecoupé d'opérations de max-pooling pour réduire les dimensions spatiales.

L'article original présente deux types d'unités résiduelles. Les blocs _baseline_ et _bottleneck_.

L'unité de base contient deux convolutions _3x3_ avec Batch Normalization (BN) et des activations ReLU.

![Image](https://cdn-media-1.freecodecamp.org/images/0*EDoU4Xh6XPO_0xVy.png)
_Blocs de construction ResNet. (gauche) baseline ; (droite) unité bottleneck. Image adaptée de : [Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385" rel="noopener" target="_blank" title=")._

La seconde, l'unité bottleneck, se compose de trois opérations empilées. Une série de convolutions _1x1_, _3x3_ et _1x1_ remplace la conception précédente. Les deux opérations _1x1_ sont conçues pour réduire et restaurer les dimensions. Cela laisse la convolution _3x3_, au milieu, pour opérer sur un vecteur de caractéristiques moins dense. De plus, BN est appliqué après chaque convolution et avant la non-linéarité ReLU.

Pour aider à clarifier, désignons ce groupe d'opérations comme une fonction _F_ de son entrée _x_ — _F(x)_.

Après les transformations non linéaires dans _F(x)_, l'unité combine le résultat de _F(x)_ avec l'entrée originale _x_. Cette combinaison est faite en additionnant les deux fonctions. La fusion de l'entrée originale _x_ avec la fonction non linéaire _F(x)_ offre certains avantages. Elle permet aux couches précédentes d'accéder au signal de gradient des couches ultérieures. En d'autres termes, sauter les opérations sur _F(x)_ permet aux couches précédentes d'avoir accès à un signal de gradient plus fort. Par conséquent, ce type de connectivité s'est avéré faciliter l'entraînement de réseaux plus profonds.

Les unités non-bottleneck montrent également un gain de précision à mesure que nous augmentons la capacité du modèle. Pourtant, les unités résiduelles bottleneck ont certains avantages pratiques. Premièrement, elles effectuent plus de calculs ayant presque le même nombre de paramètres. Deuxièmement, elles ont également une complexité de calcul similaire à celle de leurs homologues.

En pratique, les unités _bottleneck_ sont plus adaptées à l'entraînement de modèles plus profonds car moins de temps d'entraînement et de ressources computationnelles sont nécessaires.

Pour notre implémentation, nous utiliserons l'**_unité résiduelle à pré-activation complète_**. La seule différence avec l'unité bottleneck standard réside dans l'ordre dans lequel les activations BN et ReLU sont placées. Pour la pré-activation complète, BN et ReLU (dans cet ordre) se produisent avant les convolutions.

![Image](https://cdn-media-1.freecodecamp.org/images/0*_gCQf3VOGmHXzSgY.png)
_Différentes architectures de blocs de construction ResNet. (À gauche) le bloc ResNet original. (À droite) la version améliorée à pré-activation complète. Crédits image : [Identity Mappings in Deep Residual Networks](https://arxiv.org/abs/1603.05027" rel="noopener" target="_blank" title=")._

Comme montré dans [Identity Mappings in Deep Residual Networks](https://arxiv.org/abs/1603.05027), l'unité à pré-activation complète performe mieux que les autres variantes.

_Notez que la seule différence entre ces conceptions est l'ordre de BN et RELu dans la pile de convolution._

### Convolutions Atrous

Les convolutions atrous (ou dilatées) sont des convolutions régulières avec un facteur qui nous permet d'étendre le champ de vision du filtre.

Prenons un filtre de convolution _3x3_, par exemple. Lorsque le taux de dilatation est égal à 1, il se comporte comme une convolution standard. Mais, si nous définissons le facteur de dilatation à 2, cela a pour effet d'agrandir le noyau de convolution.

En théorie, cela fonctionne comme suit. Premièrement, il étend (dilate) le filtre de convolution selon le taux de dilatation. Deuxièmement, il remplit les espaces vides avec des zéros — créant un filtre de type sparse. Enfin, il effectue une convolution régulière en utilisant le filtre dilaté.

![Image](https://cdn-media-1.freecodecamp.org/images/0*owO24EqfB_RNfT7V.png)
_Convolutions atrous avec divers taux._

Par conséquent, une convolution avec un taux de dilatation de 2, un filtre _3x3_ serait capable de couvrir une zone équivalente à un _5x5_. Pourtant, parce qu'il agit comme un filtre sparse, seules les cellules _3x3_ originales effectueront le calcul et produiront des résultats. J'ai dit « agissent » parce que la plupart des frameworks n'implémentent pas les convolutions atrous en utilisant des filtres sparses (en raison des préoccupations de mémoire).

De manière similaire, définir le facteur atrous à 3 permet à une convolution régulière _3x3_ d'obtenir des signaux d'une zone correspondante _7x7_.

Cet effet nous permet de contrôler la résolution à laquelle nous calculons les réponses des caractéristiques. De plus, la convolution atrous ajoute un contexte plus large sans augmenter le nombre de paramètres ou la quantité de calcul.

Deeplab montre également que le taux de dilatation doit être ajusté en fonction de la taille des cartes de caractéristiques. Ils ont étudié les conséquences de l'utilisation de grands taux de dilatation sur de petites cartes de caractéristiques.

![Image](https://cdn-media-1.freecodecamp.org/images/0*Oa8JJBiKNvMVZrkg.png)
_Effets secondaires de la définition de taux de dilatation plus grands pour des cartes de caractéristiques plus petites. Pour une image d'entrée de 14x14, un filtre 3x3 avec un taux de dilatation de 15 fait que la convolution atrous se comporte comme une convolution régulière 1x1._

Lorsque le taux de dilatation est très proche de la taille de la carte de caractéristiques, un filtre atrous _3x3_ régulier agit comme une convolution standard _1x1_.

En d'autres termes, l'efficacité des convolutions atrous dépend d'un bon choix du taux de dilatation. Pour cette raison, il est important de connaître le concept de **output stride** dans les réseaux de neurones.

**L'output stride explique le rapport entre la taille de l'image d'entrée et la taille de la carte de caractéristiques de sortie. Il définit combien de décimation de signal le vecteur d'entrée subit lorsqu'il traverse le réseau.**

Pour un output stride de 16, une taille d'image de _224x224x3_ produit un vecteur de caractéristiques avec des dimensions 16 fois plus petites. C'est-à-dire _14x14_.

De plus, Deeplab débat également des effets de différents output strides sur les modèles de segmentation. **Il soutient que la décimation excessive du signal est néfaste pour les tâches de prédiction dense**. En résumé, les modèles avec un output stride plus petit — moins de décimation du signal — tendent à produire des résultats de segmentation plus fins. Pourtant, l'entraînement de modèles avec un output stride plus petit demande plus de temps d'entraînement.

Deeplab rapporte des expériences avec deux configurations d'output strides, 8 et 16. Comme prévu, l'output stride = 8 a été capable de produire des résultats légèrement meilleurs. Ici, nous choisissons l'output stride = 16 pour des raisons pratiques.

De plus, parce que le bloc atrous n'implémente pas de sous-échantillonnage, ASPP fonctionne également sur la même taille de réponse de caractéristique. Par conséquent, il permet d'apprendre des caractéristiques à partir d'un contexte multi-échelle en utilisant des taux de dilatation relativement grands.

Le nouveau bloc résiduel Atrous contient trois unités résiduelles. Au total, les 3 unités ont trois convolutions _3x3_. Motivé par les méthodes _multigrid_, Deeplab propose différents taux de dilatation pour chaque convolution. En résumé, _multigrid_ définit les taux de dilatation pour chacune des trois convolutions.

En pratique :

Pour le nouveau bloc4, lorsque l'output stride = 16 et **Multi Grid _= (1, 2, 4)_**, les trois convolutions ont **rates _= 2 215 (1, 2, 4) = (2, 4, 8)_** respectivement.

### Atrous Spatial Pyramid Pooling

Pour ASPP, l'idée est de fournir au modèle des informations multi-échelles. Pour ce faire, ASPP ajoute une série de convolutions atrous avec différents taux de dilatation. Ces taux sont conçus pour capturer le contexte à longue portée. De plus, pour ajouter des informations de contexte global, ASPP incorpore des caractéristiques au niveau de l'image via le Global Average Pooling (GAP).

Cette version de ASPP contient 4 opérations parallèles. Il s'agit d'une convolution _1x1_ et de trois convolutions _3x3_ avec des _taux de dilatation =(6,12,18)_. Comme nous l'avons mentionné, à ce stade, le stride nominal des cartes de caractéristiques est égal à 16.

Basé sur l'implémentation originale, nous utilisons des tailles de recadrage de _513x513_ pour l'entraînement et les tests. Ainsi, l'utilisation d'un output stride de 16 signifie que ASPP reçoit des vecteurs de caractéristiques de taille _32x32_.

De plus, pour ajouter plus d'informations de contexte global, ASPP incorpore des caractéristiques au niveau de l'image. Premièrement, il applique GAP aux caractéristiques de sortie du dernier bloc atrous. Deuxièmement, les caractéristiques résultantes sont alimentées à une convolution _1x1_ avec 256 filtres. Enfin, le résultat est suréchantillonné de manière bilinéaire aux dimensions correctes.

À la fin, les caractéristiques, de toutes les branches, sont combinées en un seul vecteur via concaténation. Cette sortie est ensuite convoluée avec un autre noyau _1x1_ — en utilisant BN et 256 filtres.

Après ASPP, nous alimentons le résultat à une autre convolution _1x1_ — pour produire les logits de segmentation finaux.

### Détails de l'implémentation

En utilisant ResNet-50 comme extracteur de caractéristiques, cette implémentation de [Deeplab_v3](https://arxiv.org/pdf/1704.06857) emploie la configuration de réseau suivante :

* _output stride = 16_
* _Taux de convolution atrous multi-grille fixes de (1,2,4) pour le nouveau bloc résiduel Atrous (bloc 4)._
* _ASPP avec des taux (6,12,18) après le dernier bloc résiduel Atrous._

Définir l'_output stride_ à 16 nous donne l'avantage d'un entraînement substantiellement plus rapide. Comparé à un output stride de 8, un stride de 16 fait que le bloc résiduel Atrous traite des cartes de caractéristiques qui sont quatre fois plus petites que celles que son homologue traite.

Les taux de dilatation multi-grille sont appliqués aux 3 convolutions à l'intérieur du bloc résiduel Atrous.

Enfin, chacune des trois convolutions parallèles _3x3_ dans ASPP reçoit un taux de dilatation différent — _(6,12,18)_.

Avant de calculer l'_erreur d'entropie croisée_, nous redimensionnons les logits à la taille de l'entrée. Comme argumenté dans l'article, il est préférable de redimensionner les logits plutôt que les étiquettes de vérité terrain pour conserver les détails de résolution.

Basé sur les procédures d'entraînement originales, nous mettons à l'échelle chaque image en utilisant un facteur aléatoire de 0,5 à 2. De plus, nous appliquons un retournement aléatoire gauche-droite aux images mises à l'échelle.

Enfin, nous recadrons des patches de taille _513x513_ pour l'entraînement et les tests.

Pour implémenter des convolutions atrous avec multi-grille dans le bloc4 du resnet, nous avons simplement modifié ce morceau dans le fichier _resnet_utils.py_.

### Entraînement

Pour entraîner le réseau, nous avons décidé d'utiliser le jeu de données Pascal VOC augmenté fourni par [Semantic contours from inverse detectors](http://ieeexplore.ieee.org/document/6126343/).

Les données d'entraînement sont composées de 8 252 images. Il y a 5 623 images de l'ensemble d'entraînement et 2 299 de l'ensemble de validation. Pour tester le modèle en utilisant le jeu de données de validation VOC 2012 original, j'ai retiré 558 images des 2 299 de l'ensemble de validation. Ces 558 échantillons étaient également présents dans l'ensemble de validation officiel VOC. De plus, j'ai ajouté 330 images de l'ensemble d'entraînement VOC 2012 qui n'étaient pas présentes parmi les 5 623 ni les 2 299 ensembles. Enfin, 10 % des 8 252 images (~825 échantillons) sont réservées pour la validation, laissant le reste pour l'entraînement.

Notez que cela est différent de l'article original : cette implémentation n'est pas pré-entraînée sur le jeu de données COCO. De plus, certaines des techniques décrites dans l'article pour l'entraînement et l'évaluation n'ont pas été implémentées.

### Résultats

Le modèle a été capable d'atteindre des résultats décents sur l'ensemble de validation PASCAL VOC.

* Précision des pixels : ~91%
* Précision moyenne : ~82%
* Intersection moyenne sur Union (mIoU) : ~74%
* Intersection sur Union pondérée par la fréquence : ~86%.

Ci-dessous, vous pouvez consulter certains des résultats dans une variété d'images de l'ensemble de validation PASCAL VOC.

![Image](https://cdn-media-1.freecodecamp.org/images/0*0jdZ7ybvv9xVHRqs.png)

![Image](https://cdn-media-1.freecodecamp.org/images/0*X1arsScqOqXxjnCn.png)

### Conclusion

Le domaine de la segmentation sémantique est sans aucun doute l'un des plus populaires en vision par ordinateur. Deeplab présente une alternative aux architectures encodeur-décodeur classiques. Il préconise l'utilisation de convolutions atrous pour l'apprentissage de caractéristiques dans des contextes multi-échelles. N'hésitez pas à cloner le dépôt et à ajuster le modèle pour obtenir des résultats plus proches de l'implémentation originale. Le code complet est [ici](https://github.com/sthalles/deeplab_v3).

J'espère que vous avez apprécié la lecture !

_Originalement publié sur [sthalles.github.io](https://sthalles.github.io/)._

![Image](https://cdn-media-1.freecodecamp.org/images/1*RzOHqzrJEIrB5ZY0nJAcvg.gif)