---
title: Tutoriel sur l'apprentissage profond – Comment utiliser PyTorch et le transfert
  d'apprentissage pour diagnostiquer les patients COVID-19
subtitle: ''
author: Juan Cruz Martinez
co_authors: []
series: null
date: '2021-11-03T19:49:35.000Z'
originalURL: https://freecodecamp.org/news/deep-learning-with-pytorch
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/Featured-Orange.png
tags:
- name: Deep Learning
  slug: deep-learning
- name: neural networks
  slug: neural-networks
- name: pytorch
  slug: pytorch
- name: Transfer learning
  slug: transfer-learning
seo_title: Tutoriel sur l'apprentissage profond – Comment utiliser PyTorch et le transfert
  d'apprentissage pour diagnostiquer les patients COVID-19
seo_desc: 'Ever since the outbreak of COVID-19 in December 2019, researchers in the
  field of artificial intelligence and machine learning have been trying to find better
  ways to diagnose the disease.

  They''ve worked on developing algorithms that would detect the...'
---

Depuis l'épidémie de COVID-19 en décembre 2019, les chercheurs dans le domaine de l'intelligence artificielle et de l'apprentissage automatique ont cherché de meilleures façons de diagnostiquer la maladie.

Ils ont travaillé sur le développement d'algorithmes qui détecteraient la maladie en quelques secondes – et uniquement en regardant des radiographies pulmonaires et/ou des images de scanner.

Certaines de ces techniques se sont avérées extrêmement utiles et précises pour diagnostiquer les cas de COVID-19.

Il existe plusieurs approches qui utilisent à la fois l'apprentissage automatique et l'apprentissage profond pour détecter et/ou classifier la maladie. Et les chercheurs ont proposé de nouvelles architectures ainsi que des approches de transfert d'apprentissage.

Dans cet article, nous examinerons une approche de transfert d'apprentissage qui classe les cas de COVID-19 en utilisant des images de radiographies pulmonaires.

Le modèle que nous allons utiliser est l'une des sept variantes de l'architecture EfficientNet. Nous utiliserons un modèle pré-entraîné sur l'immense ensemble de données ImageNet. EfficientNet est une architecture avancée et complexe basée sur des réseaux de neurones convolutifs.

Nous examinerons plus en détail les détails des réseaux de neurones convolutifs, des modèles pré-entraînés et d'EfficientNet au cours de cet article. Je l'ai divisé en cinq parties :

1. Qu'est-ce que les réseaux de neurones convolutifs ?
2. Une plongée dans le transfert d'apprentissage.
3. Qu'est-ce qu'EfficientNet ?
4. Une introduction à PyTorch.
5. Implémentation d'un classificateur COVID-19 utilisant EfficientNet avec PyTorch.

Ce tutoriel suppose que vous avez des connaissances préalables en apprentissage automatique et en apprentissage profond. Si vous souhaitez approfondir vos bases sur ces sujets, consultez cet article sur [l'intelligence artificielle vs l'apprentissage automatique vs l'apprentissage profond](https://livecodestream.dev/post/artificial-intelligence-vs-machine-learning-vs-deep-learning/).

De plus, bien que l'ensemble de données avec lequel nous allons travailler ici soit lié au COVID, vous pouvez appliquer l'implémentation réelle du code et l'analyse à d'autres ensembles de données.

## Qu'est-ce qu'un réseau de neurones convolutif ?

Les réseaux de neurones convolutifs (CNN) sont un type de réseau de neurones profond qui fonctionne sur des données visuelles – c'est-à-dire des images. Un CNN prend une image comme entrée et effectue des opérations de convolution bidimensionnelles ou tridimensionnelles sur l'image avec plusieurs filtres, également appelés noyaux.

Ces opérations de convolution produisent une matrice 2D ou 3D qui contient les poids et les biais apprenables concernant les informations spatiales de l'image d'entrée. Cette matrice de sortie est appelée la carte des caractéristiques de l'image.

Le traitement d'un réseau de neurones convolutif dans le processus d'entraînement peut, dans certains cas, être extrêmement lent. C'est pourquoi il est judicieux d'utiliser des GPU et des TPU pendant l'entraînement pour les techniques d'apprentissage profond, en particulier les réseaux de neurones convolutifs.

Les réseaux de neurones convolutifs apprennent les informations spatiales et temporelles sur l'image bien mieux que le réseau de neurones à propagation avant de base. De plus, les CNN peuvent réduire la taille de l'image tout en conservant les informations les plus importantes de l'image, ce qui est crucial pour l'analyse prédictive des images.

![Deep Learning – Introduction aux réseaux de neurones convolutifs - Blog de Vinod Sharma](https://lh6.googleusercontent.com/vma10ZOrxzyEEbJVvIZuygeDyqlkAKEUxWkJ8of7spwvrA9zktP1FYJQWZC6ZhMqrP2V0gMh04nqb74gNGNM3eO_g1ZwuvI753j-oS7fN_E0Txn4T3TXTW65MG3ubi67pBcX19o)
_[Source](https://i0.wp.com/vinodsblog.com/wp-content/uploads/2018/10/CNN-2.png?resize=1300%2C479&amp;ssl=1)_

Les couches initiales des réseaux de neurones convolutifs apprennent les caractéristiques abstraites et plus simples d'une image, telles que les lignes et les bords. Mais à mesure que nous avançons dans le réseau, la carte des caractéristiques se tourne vers les structures plus complexes de l'image.

Il commence à apprendre les caractéristiques plus spécifiques de l'image, telles qu'un chat, un chien ou une personne, de la même manière que nous, en tant qu'êtres humains, percevons le monde qui nous entoure. C'est un concept central dans la vision par ordinateur moderne basée sur l'apprentissage profond.

Avant de passer à des concepts avancés, il est important d'apprendre les bases de la convolution 2D.

## Qu'est-ce que la convolution 2D ?

La convolution 2D est un peu complexe à expliquer, mais voici comment cela fonctionne : si le processus de convolution (qui est largement utilisé dans le [traitement du signal 1-D](https://www.tutorialspoint.com/signals_and_systems/convolution_and_correlation.htm)) est effectué entre deux signaux – mais pas seulement le long d'une seule dimension, mais le long de deux dimensions mutuellement perpendiculaires – on l'appelle convolution 2D.

Dans le cas des images, les deux dimensions mutuellement perpendiculaires sont les lignes et les colonnes d'une image en niveaux de gris. L'opération de convolution est mathématiquement effectuée en multipliant puis en accumulant les valeurs des échantillons chevauchants des deux signaux d'entrée, où l'un des signaux est inversé. La sortie de cette multiplication et accumulation donne un seul point sur la carte des caractéristiques.

Dans le cas des CNN, l'image est un signal et le filtre/noyau est le deuxième signal qui est inversé. La taille du noyau est toujours plus petite que celle de l'image.

Le noyau inversé est ensuite balayé sur toute l'image, ligne par ligne et colonne par colonne, pour produire la carte des caractéristiques.

![https://miro.medium.com/max/700/1*kOThnLR8Fge_AJcHrkR3dg.gif](https://lh3.googleusercontent.com/p5ht8HdKUxxCwcNoas2qAusdT8dYq_XzLS2YqVORYqb0cCnXPPAlPu40Z73kVEXerQ5s6epDozQdYRsleeUncnSV4Opx2Q1CNk8wseTdXEPz8eHt5dJ0R2TSFnnhRRZzjO7xH4A)
_Convolution 2D_

Ici, un noyau 3x3 est balayé sur une image 6x6 pour produire une carte des caractéristiques 4x4. Comme vous pouvez le voir, les dimensions de la carte des caractéristiques de sortie sont plus petites que celles de l'image d'entrée. Il existe donc quelques concepts utilisés dans la convolution pour contrôler les dimensions de la carte des caractéristiques de sortie. Ceux-ci incluent le remplissage, le pas et la taille du noyau.

Le **remplissage** est l'ajout manuel de lignes et de colonnes autour de l'entrée pour garder la dimension de sortie identique à la dimension d'entrée ou la varier.

Le **pas** fait référence au saut que le noyau effectue pendant le balayage, à la fois dans les colonnes et les lignes. Dans l'exemple ci-dessus, le pas de la convolution est de 1 car le noyau se déplace d'une unité à la fois dans les lignes et les colonnes.

La **taille du noyau** fait référence aux dimensions du noyau utilisé. Le changement des dimensions du noyau à balayer modifie la taille de sortie de la carte des caractéristiques.

L'image ci-dessous décrit la convolution avec la même taille de noyau mais avec un remplissage de 1 et un pas de 2.

![https://miro.medium.com/max/395/1*1VJDP6qDY9-ExTuQVEOlVg.gif](https://lh3.googleusercontent.com/ceNWhzTPHzqGi5wMyUrqCSS2kp6-mF75BHxlNaEnGVwrsIiGamEq4pm_Mndmaz0weJnZfgOnl7L0CPy1OF19lRyRTAkDWZEzREBr8H36_mW_6bqJ-P8XzuJqTbzwNvPKXd_7N9U)

L'équation qui décrit la relation entre le pas, le remplissage, la taille du noyau et les dimensions d'entrée et de sortie est la suivante :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-2.png)

Le concept de convolution 3D est simplement une extension de la convolution 2D où à la fois l'image d'entrée et le noyau sont tridimensionnels.

Comme pour la convolution 2D, nous balayons le noyau tridimensionnel sur toute l'image dans deux dimensions mutuellement perpendiculaires, à savoir les lignes et les colonnes.

Nous ne balayons généralement pas le noyau sur les canaux de couleur car le noyau a la même troisième dimension, c'est-à-dire la longueur du canal, que l'image originale. Cela donne une carte des caractéristiques de sortie qui est bidimensionnelle au lieu de tridimensionnelle.

Pour en savoir plus sur les détails de la convolution 3D, vous pouvez lire [cet article](https://paperswithcode.com/method/3d-convolution).

## Qu'est-ce que le transfert d'apprentissage ?

Dans le transfert d'apprentissage, vous prenez un modèle d'apprentissage automatique ou profond qui est pré-entraîné sur un ensemble de données précédent et vous l'utilisez pour résoudre un problème différent sans avoir besoin de ré-entraîner tout le modèle.

Au lieu de cela, vous pouvez simplement utiliser les poids et les biais du modèle pré-entraîné pour faire une prédiction. Vous transférez les poids d'un modèle à votre propre modèle et vous les ajustez à votre propre ensemble de données sans ré-entraîner toutes les couches précédentes de l'architecture.

Nous utilisons le transfert d'apprentissage dans les applications des réseaux de neurones convolutifs et du traitement du langage naturel car il diminue le temps de calcul et la complexité du processus d'entraînement. Et, dans de nombreux cas, il fonctionne remarquablement bien.

Cela aide également dans les cas où nous avons des données limitées disponibles – puisque les réseaux de neurones demandent une quantité extrêmement grande de données pour atteindre de bonnes performances.

Cela signifie que l'utilisation de méthodes de transfert d'apprentissage peut grandement réduire la demande de données puisque les poids et les biais sont pré-ajustés et sont capables de fonctionner mieux avec juste une petite quantité de données en ajustant légèrement les poids et les biais.

Mais les modèles de transfert d'apprentissage ne vous donnent pas toujours de grandes performances (bien que les nouvelles architectures fonctionnent efficacement sur presque tous les problèmes). Pourtant, parfois le problème en question nécessite une architecture qui est pré-entraînée sur des données similaires à ce que vous avez. Ce facteur dépend de la complexité du problème que vous essayez de résoudre.

Il existe quelques façons de réaliser le transfert d'apprentissage :

1. **Utiliser un modèle pré-entraîné.**
2. **Développer un nouveau modèle.**

Vous pouvez utiliser un modèle pré-entraîné de deux manières. Premièrement, vous pouvez utiliser les poids et les biais pré-entraînés comme paramètres initiaux pour votre propre modèle, puis entraîner un modèle convolutif entier en utilisant ces poids.

L'autre façon est d'effectuer l'extraction de caractéristiques à partir du modèle pré-entraîné. Vous utilisez les paramètres du modèle pré-entraîné pour extraire des caractéristiques de votre image d'entrée et vous n'entraînez qu'un simple classificateur par-dessus.

Une autre option est que si vous avez un problème avec une petite quantité de données, vous développez un autre modèle pour un problème similaire qui a une grande quantité de données et vous entraînez le modèle. Ensuite, vous pouvez utiliser les poids entraînés du nouveau modèle pour résoudre le problème original avec moins de données.

Dans ce tutoriel, nous utiliserons un modèle pré-entraîné comme extracteur de caractéristiques et nous entraînerons un simple classificateur par-dessus pour obtenir la prédiction.

Il existe de nombreuses architectures bien connues dans le domaine de l'apprentissage profond qui sont aujourd'hui utilisées à des fins de transfert d'apprentissage. Presque toutes ces architectures sont entraînées sur l'ensemble de données ImageNet, qui est le plus grand ensemble de données open-source disponible. Il contient environ 1000 classes et compte environ quinze millions d'instances.

Parmi ces architectures pré-entraînées, LeNet est la première qui a été proposée en 1998. D'autres modèles bien connus incluent VGG, ResNet, AlexNet, GoogleNet, Inception et Xception.

EfficientNet fait également partie de la série qui a été proposée récemment, en 2019.

## Qu'est-ce qu'EfficientNet ?

EfficientNet (ou peut-être est-il préférable de dire EfficientNets) est une famille de modèles de classification d'images basés sur des réseaux de neurones convolutifs. Ils fonctionnent extrêmement bien sur l'ensemble de données ImageNet de pointe et d'autres ensembles de données populaires tels que CIFAR-100 et Flowers.

En plus de fonctionner si bien, l'architecture est petite et calcule plus rapidement que tous les modèles précédents. L'architecture a des variantes allant de EfficientNet-B0 à EfficientNet-B7.

Les variantes allant de B0 à B7 sont basées sur la méthode de mise à l'échelle composée pour mettre à l'échelle la base de B0 afin d'obtenir B1 à B7. EfficientNet-B7 a acquis une précision Top-1 de 84,4 % sur l'ensemble de données ImageNet, ce qui est le niveau le plus élevé de précision Top-1 jamais atteint sur ImageNet.

Si vous souhaitez en savoir plus sur le fonctionnement des EfficientNets, vous pouvez lire cet article [Efficientnet: Rethinking Model Scaling for Convolutional Neural Networks.](https://arxiv.org/abs/1905.11946v5)

![Image](https://lh3.googleusercontent.com/FvX6r1u1vR9kfoSb7tJbQ5I7aDgGQNhZCtU_OTGkHpOLTX3ZZnc-zIc-AO1MLaE-eLCsyfaj_grRXAJapYb9pJqhbzwH5R0qcXAxGUWIsHqm9zvDy6h4EQB63GOwaFZP1fV43mk)
_[Source](https://github.com/tensorflow/tpu/tree/master/models/official/efficientnet)_

Dans le tutoriel de codage plus loin dans cet article, nous utiliserons EfficientNet-B0 comme extracteur de caractéristiques et un classificateur par-dessus pour classer le COVID-19 en utilisant des images de radiographies pulmonaires.

## Une introduction à PyTorch

PyTorch est une bibliothèque supportée par Python qui nous aide à construire des modèles d'apprentissage profond. Contrairement à Keras (une autre bibliothèque d'apprentissage profond), PyTorch est flexible et donne au développeur plus de contrôle.

Il est similaire à NumPy en termes de traitement mais dispose d'une accélération GPU plus rapide. Pour en savoir plus sur NumPy et ses fonctionnalités, vous pouvez consulter [ce guide approfondi](https://www.freecodecamp.org/news/the-ultimate-guide-to-the-numpy-scientific-computing-library-for-python/) ainsi que sa [documentation](https://numpy.org/doc/stable/user/whatisnumpy.html).

PyTorch dispose d'une structure de données appelée 'Tensor' qui est similaire au ndarray de NumPy mais qui a l'option de fonctionner sur GPU.

PyTorch fournit un moyen simple de basculer le calcul entre un CPU et un GPU. Il supporte également le traitement des tableaux NumPy en fournissant simplement un module intégré qui peut convertir les tableaux NumPy en Tensors et vice versa.

L'un des modules les plus pratiques de PyTorch est `grad()`. Il vous permet de calculer le gradient d'un tenseur au fur et à mesure qu'il avance dans le traitement sans avoir besoin de calculer manuellement le gradient et de le stocker.

Cela vous donne un meilleur contrôle de vos opérations d'apprentissage profond, spécifiquement la rétropropagation, pendant le processus d'entraînement. Cela est utile lors du calcul de la fonction de perte qui vous permet d'ajuster les paramètres d'un modèle.

Nous pouvons également limiter un tenseur de sorte que son gradient ne soit pas calculé pendant tout le processus en rendant le module `requires_grad` égal à `False`. Pour en savoir plus sur les tenseurs et comment effectuer des calculs de gradient dans PyTorch, vous pouvez [consulter ce tutoriel](https://www.freecodecamp.org/news/pytorch-tensor-methods/) et [ce cours](https://www.freecodecamp.org/news/pytorch-full-course/).

## Comment implémenter un classificateur COVID-19 en utilisant EfficientNet avec PyTorch

Passons maintenant à l'implémentation pratique d'EfficientNet dans PyTorch. Nous utiliserons la variante B0 de la famille EfficientNet.

Tout d'abord, nous examinerons les données et les pré-traiterons. [Kaggle](https://www.kaggle.com) dispose d'une vaste bibliothèque de jeux de données disponibles pour une utilisation open-source dans des projets et des recherches. Il n'y a pas de limites quant au jeu de données qui peut être utilisé pour ce projet. Vous pouvez utiliser n'importe quel jeu de données contenant des images de radiographies pulmonaires de patients COVID-19 et de personnes sans COVID.

Pour les besoins de ce tutoriel, nous utiliserons ce jeu de données [ici](https://www.kaggle.com/asraf047/covid19-pneumonia-normal-chest-xray-pa-dataset). Mais pour que le code fonctionne sur votre jeu de données personnalisé, vous devez diviser vos données en trois répertoires : train, test et valid.

Chaque répertoire doit contenir deux autres répertoires avec les étiquettes `covid` et `normal`. Ces dossiers covid et normal contiendront les images correspondant à la classe spécifique du répertoire dans lequel ils se trouvent.

![Image](https://lh5.googleusercontent.com/aaZIPn8TEUsfqo3rA7xtJf7T-3PMSRU_jSZZ60DCeloIyadr40u1oguQycDMDeL-puqjdZ40xEGIu8i_PYdpufi_o-8pcGTlarJ37A_KJm_R0lV4mwGFKPAIhQmKd3Lr7b6dNHM)

Le jeu de données original que nous utiliserons dans cet article contient trois dossiers : covid, normal et pneumonia. Nous supprimons complètement le dossier pneumonia et divisons les autres données de la même manière que décrite ci-dessus.

Nous faisons cela pour créer une division logique entre les données utilisées pour l'entraînement et les données utilisées pour les tests et la validation. De plus, PyTorch, par défaut, prend le nom du dossier, une instance où il est présent, comme étiquette de la classe – donc nous n'avons pas de fichier d'étiquette correspondant à l'ensemble de données d'entrée.

### Les données et l'architecture

Examinons les données. Ci-dessous, nous pouvons voir les images de radiographies de patients atteints de COVID-19 :

![Image](https://lh4.googleusercontent.com/cB8kT-qcFsIqly9wi2yHiDZpD3of9wOgr7j9XggMWC0Yehva5H1QHiGmLq1g-qIz5wyk_6Kdy_roJiyTxUNFtPmGr6-0BKLy5KscJesZddQUGpKSDn8ZH5cRqDTWeSXswCxH8W8)

Et voici nous pouvons voir les images de radiographies de la catégorie normale :

![Image](https://lh4.googleusercontent.com/CRu82skVkh6fIaLuSD5ucOyjhjCk9o_j6ZO0zQLw8J4_UKk5nSJhxfiEtdwhmSCFVakoG0RLSwr6IL7b-ij30thBD_S6WYumx6XUYLSMkPdHfjvxzAfuwF_MaoUG89VmFGXUa9Y)

Il y a 237 couches au total dans l'architecture B-0. Toute l'architecture peut être condensée dans les diagrammes suivants. Nous fournissons les données de radiographie à la couche d'entrée.

![Image](https://lh3.googleusercontent.com/de9n3HWqb4kqVLV4VkPiCphCbfSDDSmKFXu826ITg1Z-LkWaB28JCkzfVlHaOVSrBHbSToDe5k45-bSGwUpQLglgoa4ai_YhhYAe9_th6pJIKts64kzbhgNS3GihARgRscJABlw)

![Image](https://lh5.googleusercontent.com/rCTjM83oPyAi-RddlHJufeDAql0ee_ExJmxqTbL7BgPk6unoZXmL5cabb0zuDrM7EBdDupxE1YXOmRCQt5Ntyn2gZYpzdEDb7kI0ea3BifBZp3q1MBYkVzxV9N4Mwd-882ciO7o)

![Image](https://lh4.googleusercontent.com/sZ34-xflacMLYBg33trm8RxJypHPxRqAHWtt_dm8fEdwhW1eFV0eEL66g8Yr8GcX8mo_6Sz4N6PkL7M_UbhG7S5n1eU5dpyrKZoJL7ROQ8TQLJjh_Nm4vokmtwi-4pOfCMzFHRk)
_[Source](https://towardsdatascience.com/complete-architectural-details-of-all-efficientnet-models-5fd5b736142)_

Nous allons geler l'apprentissage des poids à travers tous ces blocs car nous allons utiliser les poids pré-entraînés pour extraire les caractéristiques de notre propre entrée.

Nous effectuerons l'extraction des caractéristiques après que l'entrée passe le Module 7. Nous transférons ensuite la carte des caractéristiques obtenue du Module 7 à nos propres couches de classification finales (c'est pourquoi on l'appelle transfert d'apprentissage). Nous couronnons l'architecture avec les couches supérieures suivantes :

* BatchNorm1d
* Linear(neurones de sortie = 512)
* ReLU()
* BatchNorm1d()
* Linear(neurones de sortie = 128)
* ReLU()
* BatchNorm1d()
* Dropout(probabilité de mise à zéro des paramètres = 0,4)
* Linear(neurones de sortie = 2)

### Passons au code

Avant de commencer le code, il y a quelques dépendances que nous devons installer. Tout d'abord, vous devez installer PyTorch sur votre machine locale. Vous pouvez le faire en utilisant la commande pip install dans votre environnement Python. Consultez [ici](https://pytorch.org/get-started/locally/) pour l'installer en fonction de votre machine (qu'elle dispose ou non d'un GPU).

Avant de passer au code, je vous recommande vivement de travailler vous-même à travers le code. Cela rend beaucoup plus facile la compréhension. Cela dit, vous pouvez accéder au code complet dans un notebook Jupyter [ici](https://drive.google.com/file/d/1m_ATQIrNN-dVVZwZjux5305yhuseZ58R/view?usp=sharing).

Vous devez également installer le support Efficientnet pour PyTorch dans le même environnement Python. Exécutez la commande suivante pour l'installer :

```bash
pip install efficientnet_pytorch
```

En plus de cela, vous devrez importer quelques autres dépendances au début du code.

Nous commençons maintenant à construire le modèle de classification. Pour commencer, nous importons tous les modules nécessaires :

```python
#importation des modules requis
import gdown
import zipfile
import numpy as np
from glob import glob
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
from torchsummary import summary
from torchvision import datasets, transforms as T
from efficientnet_pytorch import EfficientNet
import os
import torch.optim as optim
from PIL import ImageFile
from sklearn.metrics import accuracy_score
```

Tous ces modules sont essentiels pour effectuer plusieurs fonctions à travers le modèle. Vous pouvez installer tous les modules absents en utilisant la commande pip.

Ensuite, nous téléchargeons et extrayons les données que nous avons préparées pour le modèle :

```python
#importation des données
#Adresse du jeu de données
url = 'https://drive.google.com/uc?export=download&id=1B75cOYH7VCaiqdeQYvMuUuy_Mn_5tPMY'
output = 'data.zip'
gdown.download(url, output, quiet=False)
#donner le nom du fichier zip
data_dir='./data.zip'
#Extraction des données du fichier zip
with zipfile.ZipFile(data_dir, 'r') as zf:
zf.extractall('./data/')
```

Le module `gdown.download` télécharge les données depuis l'URL fournie et `zipfile.extractall` extrait les données dans le même répertoire où vous vous trouvez actuellement (ou le même runtime si vous travaillez sur Google Colab).

Je recommande vivement de travailler sur Google Colab pour ce projet au cas où vous n'auriez pas de GPU disponible localement.

Ensuite, créez une variable de vérification pour vérifier la disponibilité d'un GPU.

```python
#Vérification de la disponibilité d'un GPU
use_cuda = torch.cuda.is_available()
```

Ce module retourne 'True' si un GPU est disponible et 'False' sinon.

Ensuite, nous devons appliquer des techniques de pré-traitement aux données. Comme nos données sont pré-augmentées, nous n'avons pas besoin d'appliquer de nombreuses techniques de pré-traitement. Nous redimensionnons simplement toutes les images à une taille unique de (224,224). Nous faisons cela parce que les images de notre ensemble de données ont toutes des dimensions différentes et nous avons besoin d'une dimension cohérente pour le modèle.

Nous convertirons également les images en tenseurs pour qu'elles soient traitées par PyTorch, puis nous normaliserons toutes les images. Cette fonction de normalisation normalise toutes les images avec une moyenne et un écart-type de 0,5.

Après cela, nous créons les emplacements pour les ensembles d'entraînement, de test et de validation qui seront donnés en entrée au module 'datasets'. Nous faisons cela pour que le modèle PyTorch sache exactement où se trouvent les données et aussi pour que ces données puissent être chargées sur le GPU. Nous gardons une taille de lot de 32.

```python
#déclaration de la taille du lot
batch_size = 32

#application des transformations requises sur le jeu de données
img_transforms = {
    'train':
    T.Compose([
        T.Resize(size=(224,224)), 
        T.ToTensor(),
        T.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5]), 
        ]),

    'valid':
    T.Compose([
        T.Resize(size=(224,224)),
        T.ToTensor(),
        T.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])
        ]),

    'test':
    T.Compose([
        T.Resize(size=(224,224)),
        T.ToTensor(),
        T.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])
        ]),
     }

# création de l'emplacement des données : entraînement, validation, test
data='./data/'

train_path=os.path.join(data,'train')
valid_path=os.path.join(data,'test')
test_path=os.path.join(data,'valid')


# création de jeux de données pour chacun des dossiers créés précédemment
train_file=datasets.ImageFolder(train_path,transform=img_transforms['train'])
valid_file=datasets.ImageFolder(valid_path,transform=img_transforms['valid'])
test_file=datasets.ImageFolder(test_path,transform=img_transforms['test'])


#Création de chargeurs pour le jeu de données
loaders_transfer={
    'train':torch.utils.data.DataLoader(train_file,batch_size,shuffle=True),
    'valid':torch.utils.data.DataLoader(valid_file,batch_size,shuffle=True),
    'test': torch.utils.data.DataLoader(test_file,batch_size,shuffle=True)
}
```

Après le pré-traitement, nous passons à la construction du modèle.

```python
#importation du modèle EfficientNet pré-entraîné

model_transfer = EfficientNet.from_pretrained('efficientnet-b0')

# Geler les poids
for param in model_transfer.parameters():
    param.requires_grad = False
in_features = model_transfer._fc.in_features


# Définition des couches denses supérieures après les couches convolutives
model_transfer._fc = nn.Sequential(
    nn.BatchNorm1d(num_features=in_features),    
    nn.Linear(in_features, 512),
    nn.ReLU(),
    nn.BatchNorm1d(512),
    nn.Linear(512, 128),
    nn.ReLU(),
    nn.BatchNorm1d(num_features=128),
    nn.Dropout(0.4),
    nn.Linear(128, 2),
    )
if use_cuda:
    model_transfer = model_transfer.cuda()
```

Tout d'abord, nous importons le modèle EfficientNet-B0 avec ses poids pré-entraînés. Ensuite, nous désactivons l'entraînement des paramètres du modèle car nous allons utiliser les paramètres pré-entraînés pour extraire les caractéristiques de nos données.

Ensuite, nous remplaçons les couches supérieures entièrement connectées du modèle par notre propre classificateur.

Batchnorm normalise tout le lot de données en un nombre de neurones donné comme argument. Cela réduit la complexité du modèle et l'empêche de surajuster. Dropout fait quelque chose de similaire – il met à zéro certains neurones dans le modèle avec une probabilité de la valeur donnée comme argument.

La couche Linear est une simple couche de réseau de neurones entièrement connectée.

Enfin, nous transférons notre modèle sur le GPU, si disponible.

```python
# sélection de la fonction de perte
criterion_transfer = nn.CrossEntropyLoss()

# utilisation du classificateur Adam
optimizer_transfer = optim.Adam(model_transfer.parameters(), lr=0.0005)
```

Ici, nous sélectionnons la fonction de perte et l'optimiseur pour notre phase d'entraînement. Nous définissons également la valeur du taux d'apprentissage pour l'optimiseur. Vous pouvez changer cette valeur pour voir comment différents taux d'apprentissage influencent le modèle de différentes manières.

Ensuite, nous passons à l'entraînement du modèle.

```python
ImageFile.LOAD_TRUNCATED_IMAGES = True

# Création de la fonction pour l'entraînement
def train(n_epochs, loaders, model, optimizer, criterion, use_cuda, save_path):
    """retourne le modèle entraîné"""
    # initialisation du suiveur pour la perte de validation minimale
    valid_loss_min = np.Inf 
    trainingloss = []
    validationloss = []

    for epoch in range(1, n_epochs+1):
        # initialisation des variables pour surveiller la perte d'entraînement et de validation
        train_loss = 0.0
        valid_loss = 0.0
        
        ###################
        # entraînement du modèle #
        ###################
        model.train()
        for batch_idx, (data, target) in enumerate(loaders['train']):
            # passage au GPU
            if use_cuda:
                data, target = data.cuda(), target.cuda()
          
            optimizer.zero_grad()
            output = model(data)
            loss = criterion(output, target)
            loss.backward()
            optimizer.step()
           
            train_loss = train_loss + ((1 / (batch_idx + 1)) * (loss.data - train_loss))
    
        ######################    
        # validation du modèle #
        ######################
        model.eval()
        for batch_idx, (data, target) in enumerate(loaders['valid']):
            if use_cuda:
                data, target = data.cuda(), target.cuda()
            
            output = model(data)
            loss = criterion(output, target)
            valid_loss = valid_loss + ((1 / (batch_idx + 1)) * (loss.data - valid_loss))
        
        train_loss = train_loss/len(train_file)
        valid_loss = valid_loss/len(valid_file)

        trainingloss.append(train_loss)
        validationloss.append(valid_loss)

        # impression des statistiques d'entraînement/validation 
        print('Epoch: {} \tTraining Loss: {:.6f} \tValidation Loss: {:.6f}'.format(
            epoch, 
            train_loss,
            valid_loss
            ))
        
        ## sauvegarde du modèle si la perte de validation a diminué
        if valid_loss < valid_loss_min:
            torch.save(model.state_dict(), save_path)
            
            valid_loss_min = valid_loss
            
    # retour du modèle entraîné
    return model, trainingloss, validationloss
```

Nous créons une fonction pour la phase d'entraînement et de validation du modèle. Nous permettons au modèle d'accepter également des images tronquées avec moins de trois canaux. Nous initialisons les valeurs des pertes d'entraînement et de validation et démarrons la boucle d'entraînement. Nous importons les données lot par lot à partir des chargeurs de données et effectuons les opérations d'entraînement.

Après la boucle d'entraînement, nous démarrons la boucle de validation où nous calculons uniquement la perte et les prédictions de sortie et ne mettons pas à jour les paramètres comme nous l'avons fait dans la boucle d'entraînement. Nous sauvegardons le modèle qui a la perte minimale pour l'ensemble de validation.

```python
# entraînement du modèle

n_epochs=10

model_transfer, train_loss, valid_loss = train(n_epochs, loaders_transfer, model_transfer, optimizer_transfer, criterion_transfer, use_cuda, 'model.pt')
```

Nous exécutons le modèle pendant 10 époques, c'est-à-dire 10 boucles. Vous pouvez changer le nombre d'époques et tester les valeurs de perte. Le modèle sauvegardé est enregistré sous le nom `model.pt`. Maintenant, nous chargeons le modèle et passons à la phase de test.

```python
# Définition de la fonction de test

def test(loaders, model, criterion, use_cuda):

    # surveillance de la perte et de la précision du test
    test_loss = 0.
    correct = 0.
    total = 0.
    preds = []
    targets = []

    model.eval()
    for batch_idx, (data, target) in enumerate(loaders['test']):
        # passage au GPU
        if use_cuda:
            data, target = data.cuda(), target.cuda()
        # passage avant
        output = model(data)
        # calcul de la perte
        loss = criterion(output, target)
        # mise à jour de la perte moyenne du test 
        test_loss = test_loss + ((1 / (batch_idx + 1)) * (loss.data - test_loss))
        # conversion des probabilités de sortie en classe prédite
        pred = output.data.max(1, keepdim=True)[1]
        preds.append(pred)
        targets.append(target)
        # comparaison des prédictions
        correct += np.sum(np.squeeze(pred.eq(target.data.view_as(pred))).cpu().numpy())
        total += data.size(0)
    
    return preds, targets

# appel de la fonction de test
preds, targets = test(loaders_transfer, model_transfer, criterion_transfer, use_cuda)
```

Nous créons maintenant une fonction de test pour appliquer notre modèle à notre ensemble de données de test et évaluer ses performances.

Nous passons l'ensemble de données lot par lot comme nous l'avons fait dans la phase d'entraînement et de test, mais nous ne le faisons qu'une seule fois ici au lieu de 10 époques. Cela est dû au fait que nous devons simplement tester le modèle et non mettre à jour les paramètres.

La fonction retourne les prédictions qu'elle a calculées pour l'ensemble de test d'entrée ainsi que les valeurs cibles originales de l'ensemble de test.

Maintenant, nous calculons la précision du modèle. Tout d'abord, nous devons convertir les tenseurs, c'est-à-dire les prédictions et les cibles, en tableaux NumPy. Nous faisons cela en les déplaçant d'abord du GPU vers le CPU, puis en les convertissant en tableaux NumPy. Le code suivant fait cela :

```python
# conversion de l'objet tenseur en une liste pour les fonctions métriques

preds2, targets2 = [],[]

for i in preds:
  for j in range(len(i)):
    preds2.append(i.cpu().numpy()[j])
for i in targets:
  for j in range(len(i)):
    targets2.append(i.cpu().numpy()[j])
```

Maintenant, nous calculons la précision en utilisant la métrique de précision de la bibliothèque sklearn.

```python
# Calcul de la précision
acc = accuracy_score(targets2, preds2)
print("Précision : ", acc)
```

Notre modèle avait une précision de 95,45 %.

![Image](https://lh3.googleusercontent.com/4_gMnxj_l_xGKOPr0Zg5V8IIA78NJIloxe9FNsKwAAW480WUpojW6PQWWgYzT7k839c27hA7svWPi4m_8XuR0ZSWY6TJ0TIc22xtCqqixeSq9mVBZzDIHW0edaueH1IE3VRW68M)

L'image suivante est la matrice de confusion pour l'exécution du test du classificateur. Dans celle-ci, vous pouvez voir la visualisation des performances du modèle. Les étiquettes réelles indiquent si la personne avait le COVID ou non, tandis que les étiquettes prédites indiquent comment notre modèle a classé les images.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/confusion-matrix.png)

Comme nous pouvons le voir, notre modèle a prédit la plupart des étiquettes correctement. La petite portion d'étiquettes prédites de manière incorrecte comprend 7 personnes qui n'avaient pas le COVID, mais notre modèle a prédit qu'elles l'avaient. Ce n'est pas trop alarmant.

D'autre part, il y avait 14 exemples où notre modèle a prédit qu'ils n'avaient pas le COVID, mais ils l'avaient. En apprentissage automatique, ce sont ce qu'on appelle les faux négatifs. C'est une situation très alarmante car nous aurions renvoyé chez eux des personnes souffrant de COVID-19. Cela augmenterait leur risque que la maladie s'aggrave.

## Conclusion

Les réseaux de neurones convolutifs se sont avérés extrêmement utiles dans les techniques de vision par ordinateur, et nous pouvons également les utiliser efficacement dans l'imagerie médicale et le diagnostic.

Le transfert d'apprentissage est une méthode efficace pour utiliser des architectures pré-entraînées afin de performer efficacement dans d'autres applications.

Mais comme nous l'avons vu ci-dessus, l'utilisation de ces modèles dépend du type de problème que nous avons et de nos objectifs. Tout comme dans la détection du COVID-19, nous préférerions avoir un modèle qui nous donne 0 faux négatifs. Mais il y a encore un grand potentiel pour que l'apprentissage profond soit utile dans le diagnostic du COVID ainsi que dans d'autres techniques de diagnostic médical.

Merci d'avoir lu ! Si vous avez apprécié l'article et que vous souhaitez lire d'autres articles intéressants sur l'informatique, Python et JavaScript, veuillez me suivre sur [Twitter](https://twitter.com/bajcmartinez).