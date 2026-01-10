---
title: Comment utiliser le modèle Segment Anything (SAM) pour créer des masques
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-11-08T20:26:18.000Z'
originalURL: https://freecodecamp.org/news/use-segment-anything-model-to-create-masks
coverImage: https://www.freecodecamp.org/news/content/images/2023/11/cover-image-SAM.png
tags:
- name: Computer Vision
  slug: computer-vision
- name: Machine Learning
  slug: machine-learning
- name: Python
  slug: python
seo_title: Comment utiliser le modèle Segment Anything (SAM) pour créer des masques
seo_desc: "By Jess Wilk\nHey there! So, you know that buzz about Tesla's autopilot\
  \ being all futuristic and driverless? Ever thought about how it actually does its\
  \ magic? Well, let me tell you – it's all about image segmentation and object detection.\
  \ \nWhat is Im..."
---

Par Jess Wilk

Salut ! Vous savez, ce buzz autour de l'autopilote de Tesla, futuriste et sans conducteur ? Vous êtes-vous déjà demandé comment il fait sa magie ? Eh bien, laissez-moi vous dire – tout est question de segmentation d'image et de détection d'objets. 

## Qu'est-ce que la segmentation d'image ?

La segmentation d'image, qui consiste essentiellement à découper une image en différentes parties, aide le système à reconnaître les éléments. Elle identifie où se trouvent les humains, les autres voitures et les obstacles sur la route. C'est la technologie qui assure que ces voitures autonomes peuvent circuler en toute sécurité. Cool, non ? ud83dude97

Au cours de la dernière décennie, la vision par ordinateur a fait des progrès massifs, notamment dans la création de méthodes de segmentation et de détection d'objets super sophistiquées. 

Ces percées ont trouvé des utilisations diverses, comme la détection de tumeurs et de maladies dans les images médicales, la surveillance des cultures en agriculture, et même le guidage des robots dans la navigation. La technologie se diversifie vraiment et a un impact significatif dans différents domaines. 

Le principal défi réside dans l'obtention et la préparation des données. La construction d'un ensemble de données de segmentation d'image demande l'annotation de tas d'images pour définir les labels, ce qui est une tâche massive. Cela nécessite une tonne de ressources. 

Donc, le jeu a changé lorsque le **Segment Anything Model (SAM)** est arrivé sur la scène. SAM a révolutionné ce domaine en permettant à quiconque de créer des masques de segmentation pour ses données sans dépendre de données étiquetées.

Dans cet article, je vais vous guider à travers la compréhension de SAM, son fonctionnement, et comment vous pouvez l'utiliser pour créer des masques. Alors, prenez votre tasse de café parce que nous plongeons dedans ! 2615

### Prérequis :

Les prérequis pour cet article incluent une compréhension de base de la **programmation Python** et une connaissance fondamentale de l'**apprentissage automatique**. 

De plus, la familiarité avec les concepts de segmentation d'image, la vision par ordinateur et les défis de l'annotation des données serait également bénéfique.

## Qu'est-ce que le modèle Segment Anything ?

SAM est un grand modèle de langage développé par l'équipe de recherche de Facebook (Meta AI). Le modèle a été formé sur un ensemble de données massif de **1,1 milliard de masques de segmentation**, l'ensemble de données SA-1B. Le modèle peut bien généraliser aux données invisibles car il est formé sur un ensemble de données très diversifié et a une faible variance. 

SAM peut être utilisé pour segmenter n'importe quelle image et créer des masques sans aucune donnée étiquetée. C'est une percée, car aucune segmentation entièrement automatisée n'était possible avant SAM.

Qu'est-ce qui rend SAM unique ? C'est un modèle de **segmentation promptable** de premier ordre. Les prompts permettent d'instruire le modèle sur la sortie souhaitée via du texte et des actions interactives. Vous pouvez fournir des prompts à SAM de plusieurs manières : Points, Boîtes englobantes, textes, et même masques de base.

## Comment fonctionne SAM ?

SAM utilise une architecture basée sur les transformateurs, comme la plupart des grands modèles de langage. Examinons le flux de données à travers les différents composants de SAM. 

**Encodeur d'image :** Lorsque vous fournissez une image à SAM, elle est d'abord envoyée à l'encodeur d'image. Fidèle à son nom, ce composant encode l'image en vecteurs. Ces vecteurs représentent les caractéristiques de bas niveau (bords, contours) et de haut niveau comme les formes et les textures des objets extraits de l'image. L'encodeur ici est un **Vision Transformer (ViT)**, qui présente de nombreux avantages par rapport aux CNNs traditionnels.

**Encodeur de prompt :** L'entrée de prompt que l'utilisateur donne est convertie en embeddings par l'encodeur de prompt. SAM utilise des embeddings positionnels pour les points, les prompts de boîte englobante, et des encodeurs de texte pour les prompts textuels.

**Décodeur de masque :** Ensuite, SAM mappe les caractéristiques d'image extraites et les encodages de prompt pour générer le masque, qui est notre sortie. SAM générera 3 masques segmentés pour chaque prompt d'entrée, offrant aux utilisateurs des choix. 

## Pourquoi utiliser SAM ?

Avec SAM, vous pouvez sauter la configuration coûteuse généralement nécessaire pour l'IA, et obtenir tout de même des résultats rapides. Il fonctionne bien avec toutes sortes de données, comme les images médicales ou satellitaires, et s'intègre parfaitement dans le logiciel que vous utilisez déjà pour des tâches de détection rapides. 

Vous obtenez également des outils adaptés pour des travaux spécifiques comme la segmentation d'image, et il est simple d'interagir avec, que vous l'entraîniez ou que vous lui demandiez d'analyser des données. De plus, il est plus rapide que les anciens systèmes comme les CNNs, vous faisant gagner à la fois du temps et de l'argent.

![Image](https://lh7-us.googleusercontent.com/tcDOfehN4GLt4bZkN_0uhOPYsZ9B8cBeQaCxf9F6OS6iUN1WESAAWNUb9_vCpTj66TvzeVocZi3i6xKkrMB2cSbj0-UBrjlR3jjBXJfRo1WAYyipmVbSiYQPj0f3X8HMc1AA1y1dQ7Zq197kxXETWDY)
_Pourquoi utiliser SAM ?_

## Comment installer et configurer SAM

Maintenant que vous savez comment SAM fonctionne, laissez-moi vous montrer comment l'installer et le configurer. La première étape consiste à installer le package dans votre notebook Jupyter ou Google Colab avec la commande suivante :

```python
pip install 'git+https://github.com/facebookresearch/segment-anything.git'

```

```python
/content Collecting git+https://github.com/facebookresearch/segment-anything.git Cloning https://github.com/facebookresearch/segment-anything.git to /tmp/pip-req-build-xzlt_n7r Running command git clone --filter=blob:none --quiet https://github.com/facebookresearch/segment-anything.git /tmp/pip-req-build-xzlt_n7r Resolved https://github.com/facebookresearch/segment-anything.git to commit 6fdee8f2727f4506cfbbe553e23b895e27956588 Preparing metadata (setup.py) ... done
```

L'étape suivante consiste à télécharger les poids pré-entraînés du modèle SAM que vous souhaitez utiliser. 

Vous pouvez choisir parmi trois options de poids de checkpoint : ViT-B (91M), ViT-L (308M), et ViT-H (636M paramètres). 

Comment choisir le bon ? Plus le nombre de paramètres est élevé, plus le temps nécessaire pour l'inférence, c'est-à-dire la génération de masque, est long. Si vous avez peu de ressources GPU et une inférence rapide, optez pour ViT-B. Sinon, choisissez ViT-H. 

Suivez les commandes ci-dessous pour configurer le chemin de checkpoint du modèle :

```python
!wget -q https://dl.fbaipublicfiles.com/segment_anything/sam_vit_h_4b8939.pth
CHECKPOINT_PATH='/content/weights/sam_vit_h_4b8939.pth'


import torch
DEVICE = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
MODEL_TYPE = "vit_h"
```

Les poids du modèle sont prêts ! Maintenant, je vais vous montrer différentes méthodes grâce auxquelles vous pouvez fournir des prompts et générer des masques dans les sections à venir. ud83dude80

## Comment SAM peut générer des masques automatiquement 

SAM peut segmenter automatiquement l'ensemble de l'image d'entrée en segments distincts sans prompt spécifique. Pour cela, vous pouvez utiliser l'utilitaire `SamAutomaticMaskGenerator`. 

Suivez les commandes ci-dessous pour l'importer et l'initialiser avec le type de modèle et le chemin de checkpoint. 

```python
from segment_anything import sam_model_registry, SamAutomaticMaskGenerator, SamPredictor


sam = sam_model_registry[MODEL_TYPE](checkpoint=CHECKPOINT_PATH).to(device=DEVICE)


mask_generator = SamAutomaticMaskGenerator(sam)
```

Par exemple, j'ai téléchargé une image de chiens dans mon notebook. Ce sera notre image d'entrée, qui doit être convertie au format RGB (Rouge-Vert-Bleu) pour être entrée dans le modèle. 

Vous pouvez faire cela en utilisant le package OpenCV Python puis utiliser la fonction `generate()` pour créer un masque, comme montré ci-dessous :

```python
# Import opencv package
import cv2


# Give the path of your image
IMAGE_PATH= '/content/dog.png'
# Read the image from the path
image= cv2.imread(IMAGE_PATH)
# Convert to RGB format
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


# Generate segmentation mask
output_mask = mask_generator.generate(image_rgb)
print(output_mask)

```

La sortie générée est un dictionnaire avec les valeurs principales suivantes :

* `Segmentation:` Un tableau qui a une forme de masque
* `area:` Un entier qui stocke la surface du masque en pixels
* `bbox:` Les coordonnées de la boîte de délimitation [xywh]
* `Predicted_iou:` IOU est un score d'évaluation pour la segmentation

![Image](https://lh7-us.googleusercontent.com/zvUNSrvPrv8-Z1idbMLHXKv8iXzWlInik9R2fdJ24HQc5EBxdAgqaiEFTeE4UalWdUvA0R0L9dQuqDDZVucoBWwTMBld9aCJ8NKRTp2vxE-fYnvsbIEL8Z1kRfnQFsCVGb4HGf0pkkuNT6Wss1iMX6c)
_La sortie générée est un dictionnaire avec les valeurs principales_

Alors, comment visualiser notre masque de sortie ?

Eh bien, c'est une simple fonction Python qui prendra le dictionnaire généré par SAM en sortie et tracera les masques de segmentation avec les valeurs de forme de masque et les coordonnées.

```python
# Function that inputs the output and plots image and mask
def show_output(result_dict,axes=None):
     if axes:
        ax = axes
     else:
        ax = plt.gca()
        ax.set_autoscale_on(False)
     sorted_result = sorted(result_dict, key=(lambda x: x['area']),      reverse=True)
     # Plot for each segment area
     for val in sorted_result:
        mask = val['segmentation']
        img = np.ones((mask.shape[0], mask.shape[1], 3))
        color_mask = np.random.random((1, 3)).tolist()[0]
        for i in range(3):
            img[:,:,i] = color_mask[i]
            ax.imshow(np.dstack((img, mask*0.5)))
```

Utilisons cette fonction pour tracer notre image d'entrée brute et le masque segmenté :

```python
_,axes = plt.subplots(1,2, figsize=(16,16))
axes[0].imshow(image_rgb)
show_output(sam_result, axes[1])

```

![Image](https://lh7-us.googleusercontent.com/m7RxR_KOL-nSBtptL-dEbsV_EN7w21sqQMiCnfvrr83hwxAhe7jgXWLUhMgjoGzpO4QHgSbnoCOtN5SB__kokKC_OykSCxEo7ntXYd1LihwL3BBlAgUNqn70-E35yQS-Xvb2JrnpYOYTjShEmCg9w9w)
_Le modèle a segmenté chaque objet_

Comme vous pouvez le voir, le modèle a segmenté chaque objet dans l'image en utilisant une méthode zero-shot en une seule fois ! ud83cudf1f

## Comment utiliser SAM avec des prompts de boîte englobante

Parfois, nous pouvons vouloir segmenter seulement une portion spécifique d'une image. Pour y parvenir, entrez des boîtes englobantes approximatives pour identifier l'objet dans la zone d'intérêt, et SAM le segmentera en conséquence.   
  
Pour implémenter cela, importez et initialisez le `SamPredictor` et utilisez la fonction `set_image()` pour passer l'image d'entrée. Ensuite, appelez la fonction `predict`, en fournissant les coordonnées de la boîte englobante comme entrée pour le paramètre `box` comme montré dans l'extrait ci-dessous. Le prompt de boîte englobante doit être au format [X-min, Y-min, X-max, Y-max].

```python
# Set up the SAM model with the encoded image
mask_predictor = SamPredictor(sam)
mask_predictor.set_image(image_rgb)


# Predict mask with bounding box prompt
masks, scores, logits = mask_predictor.predict(
box=bbox_prompt,
multimask_output=False
)


# Plot the bounding box prompt and predicted mask
plt.imshow(image_rgb)
show_mask(masks[0], plt.gca())
show_box(bbox_prompt, plt.gca())
plt.show()

```

![Image](https://lh7-us.googleusercontent.com/DoiDVGgozu4ZDeBMyJWbSlCt3CGFnxd7SFlfWFuvuUu_ByZuHc2pA75C2dbaygBwIQqmHcPCBoEsVFaqs_dxpAskPVZxXOoejgu2j0JIrkwDmjPr3aa7xgsgdpmcG2vVETURBkZ32EOKNFZrDzvmQLA)
_La boîte englobante verte était notre prompt d'entrée dans cette sortie, et le bleu représente notre masque prédit._

## Comment utiliser SAM avec des points comme prompts

Et si vous avez besoin du masque de l'objet pour un certain point dans l'image ? Vous pouvez fournir les coordonnées du point comme prompt d'entrée à SAM. Le modèle générera alors les trois masques de segmentation les plus pertinents. Cela aide en cas d'ambiguïté sur l'objet principal d'intérêt. 

Les premières étapes sont similaires à ce que nous avons fait dans les sections précédentes. Initialisez le module prédicteur avec l'image d'entrée. Ensuite, fournissez le prompt d'entrée comme coordonnées [X,Y] au paramètre `point_coords`.

```python
# Initialize the model with the input image
from segment_anything import sam_model_registry, SamPredictor
sam = sam_model_registry[MODEL_TYPE](checkpoint=CHECKPOINT_PATH).to(device=DEVICE)
mask_predictor = SamPredictor(sam)
mask_predictor.set_image(image_rgb)
# Provide points as input prompt [X,Y]-coordinates
input_point = np.array([[250, 200]])
input_label = np.array([1])


# Predict the segmentation mask at that point
masks, scores, logits = mask_predictor.predict(
point_coords=input_point,
point_labels=input_label,
multimask_output=True,
)

```

Comme nous avons défini le paramètre `multimask_output` comme True, il y aura trois masques de sortie. Visualisons cela en traçant les masques et leur prompt d'entrée.

![Image](https://lh7-us.googleusercontent.com/etMcljU5T2wlLBfbJdV46L4n1I2KUZe2nswYJVFs0Hh-xRFFs-nArO9i5rEr1xU3Er77T7TTn7uenU9Tu1_H4SuSwjGyAtOYe-Jt7_-UQpO05Rv3dOIs5Y3Q-1I41VepltOi_tyBiKSf0RMfWhwVUaQ)
_Dans la figure ci-dessus, l'étoile verte désigne le point de prompt, et le bleu représente le masque prédit. Alors que le masque 1 a une couverture médiocre, les masques 2 et 3 ont une bonne précision pour mes besoins._

J'ai également imprimé les scores IOU auto-évalués pour chaque masque. IOU signifie Intersection Over Union et mesure la déviation entre le contour de l'objet et le masque.

## Conclusion

Vous pouvez construire un ensemble de données de segmentation sur mesure pour votre domaine en collectant des images brutes et en utilisant l'outil SAM pour l'annotation. Ce modèle a montré des performances constantes, même dans des conditions difficiles comme le bruit ou l'occlusion. 

Dans la prochaine version, ils rendent les prompts textuels compatibles, visant à améliorer la convivialité. 

J'espère que ces informations vous seront utiles !

Merci d'avoir lu ! Je suis Jess, et je suis une experte chez Hyperskill. Vous pouvez consulter nos [**cours de ML**](https://hyperskill.org/tracks/42?utm_source=fc_hs&utm_medium=social&utm_campaign=jess) sur la plateforme.