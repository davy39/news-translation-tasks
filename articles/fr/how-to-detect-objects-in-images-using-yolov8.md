---
title: Comment détecter des objets dans des images en utilisant le réseau de neurones
  YOLOv8
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-05-04T18:17:42.000Z'
originalURL: https://freecodecamp.org/news/how-to-detect-objects-in-images-using-yolov8
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/n2auv9i8405cgnxhru40.png
tags:
- name: Machine Learning
  slug: machine-learning
- name: neural networks
  slug: neural-networks
- name: Python
  slug: python
seo_title: Comment détecter des objets dans des images en utilisant le réseau de neurones
  YOLOv8
seo_desc: 'By Andrey Germanov

  Object detection is a computer vision task that involves identifying and locating
  objects in images or videos. It is an important part of many applications, such
  as self-driving cars, robotics, and video surveillance.

  Over the year...'
---

Par Andrey Germanov

La détection d'objets est une tâche de vision par ordinateur qui consiste à identifier et localiser des objets dans des images ou des vidéos. C'est une partie importante de nombreuses applications, telles que les voitures autonomes, la robotique et la vidéosurveillance.

Au fil des ans, de nombreuses méthodes et algorithmes ont été développés pour trouver des objets dans des images et leurs positions. La meilleure qualité dans l'exécution de ces tâches provient de l'utilisation de réseaux de neurones convolutifs. 

L'un des réseaux de neurones les plus populaires pour cette tâche est YOLO, créé en 2015 par Joseph Redmon, Santosh Divvala, Ross Girshick et Ali Farhadi dans leur célèbre article de recherche "You Only Look Once: Unified, Real-Time Object Detection".

Depuis cette époque, il y a eu plusieurs versions de YOLO. Les versions récentes peuvent faire encore plus que la détection d'objets. La dernière version est [YOLOv8](https://ultralytics.com/yolov8), que nous allons utiliser dans ce tutoriel.

Ici, je vais vous montrer les principales caractéristiques de ce réseau pour la détection d'objets. Tout d'abord, nous utiliserons un modèle pré-entraîné pour détecter des classes d'objets courants comme les chats et les chiens. Ensuite, je montrerai comment entraîner votre propre modèle pour détecter des types d'objets spécifiques que vous sélectionnez, et comment préparer les données pour ce processus. Enfin, nous créerons une application web pour détecter des objets sur des images directement dans un navigateur web en utilisant le modèle entraîné personnalisé.

Pour suivre ce tutoriel, vous devez être familier avec [Python](https://python.org) et avoir une compréhension de base de l'apprentissage automatique, des réseaux de neurones et de leur application dans la détection d'objets. Vous pouvez regarder [ce court cours vidéo](https://www.youtube.com/playlist?list=PL_IHmaMAvkVxdDOBRg2CbcJBq9SY7ZUvs) pour vous familiariser avec toute la théorie nécessaire de l'apprentissage automatique.

Une fois que vous avez rafraîchi la théorie, commençons avec la pratique ! Voici ce que nous allons couvrir :

1. [Problèmes que YOLOv8 peut résoudre](#heading-problemes-que-yolov8-peut-resoudre)
2. [Comment commencer avec YOLOv8](#heading-comment-commencer-avec-yolov8)
3. [Comment préparer les données pour entraîner le modèle YOLOv8](#heading-comment-preparer-les-donnees-pour-entrainer-le-modele-yolov8)
4. [Comment entraîner le modèle YOLOv8](#heading-comment-entrainer-le-modele-yolov8)
5. [Comment créer un service web de détection d'objets](#heading-comment-creer-un-service-web-de-detection-dobjets)
6. [Comment créer le Frontend](#heading-comment-creer-le-frontend)
7. [Comment créer le Backend](#heading-comment-creer-le-backend)
8. [Conclusion](#heading-conclusion)

<h1 id="problemes_peut_resoudre">Problèmes que YOLOv8 peut résoudre</h1>

Vous pouvez utiliser le réseau YOLOv8 pour résoudre des problèmes de classification, de détection d'objets et de segmentation d'images. Toutes ces méthodes détectent des objets dans des images ou des vidéos de différentes manières, comme vous pouvez le voir dans l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/compvision_tasks.png)
_Problèmes courants de vision par ordinateur - classification, détection et segmentation_

Le réseau de neurones créé et entraîné pour la **classification d'images** détermine une classe d'objet sur l'image et retourne son nom et la probabilité de cette prédiction. 

Par exemple, sur l'image de gauche, il a retourné que c'est un "chat" et que le niveau de confiance de cette prédiction est de 92 % (0,92).

Le réseau de neurones pour la **détection d'objets**, en plus du type d'objet et de la probabilité, retourne les coordonnées de l'objet sur l'image : x, y, largeur et hauteur, comme montré sur la deuxième image. Les réseaux de neurones de détection d'objets peuvent également détecter plusieurs objets dans l'image et leurs boîtes englobantes.

Enfin, en plus des types d'objets et des boîtes englobantes, le réseau de neurones entraîné pour la **segmentation d'images** détecte les formes des objets, comme montré sur l'image de droite.

Il existe de nombreuses architectures de réseaux de neurones différentes développées pour ces tâches, et pour chacune d'entre elles, vous deviez utiliser un réseau séparé dans le passé. Heureusement, les choses ont changé après la création de [YOLO](https://docs.ultralytics.com/). Maintenant, vous pouvez utiliser une seule plateforme pour tous ces problèmes.

Dans cet article, nous allons explorer la **détection d'objets** en utilisant YOLOv8. Je vais vous guider à travers la création d'une application web qui détectera les feux de circulation et les panneaux de signalisation dans les images. Dans les articles suivants, je couvrirai d'autres fonctionnalités, y compris la segmentation d'images.

Dans les sections suivantes, nous passerons en revue toutes les étapes nécessaires pour créer un détecteur d'objets. À la fin de ce tutoriel, vous aurez une application web complète alimentée par l'IA.

<h1 id="commencer">Comment commencer avec YOLOv8</h1>

Techniquement parlant, [YOLOv8](https://ultralytics.com/) est un groupe de modèles de réseaux de neurones convolutifs, créés et entraînés en utilisant le framework [PyTorch](https://pytorch.org/).

En outre, le package YOLOv8 fournit une seule API Python pour travailler avec tous ces modèles en utilisant les mêmes méthodes. C'est pourquoi, pour l'utiliser, vous avez besoin d'un environnement pour exécuter du code Python. Je recommande vivement d'utiliser [Jupyter Notebook](https://jupyter.org/).

Après vous être assuré que vous avez Python et Jupyter installés sur votre ordinateur, exécutez le notebook et installez le package YOLOv8 en exécutant la commande suivante :

```python
!pip install ultralytics
```

Le package `ultralytics` contient la classe `YOLO`, utilisée pour créer des modèles de réseaux de neurones.

Pour y accéder, importez-la dans votre code Python :

```python
from ultralytics import YOLO
```

Maintenant, tout est prêt pour créer le modèle de réseau de neurones :

```python
model = YOLO("yolov8m.pt")
```

Comme je l'ai mentionné précédemment, YOLOv8 est un groupe de modèles de réseaux de neurones. Ces modèles ont été créés et entraînés en utilisant PyTorch et exportés vers des fichiers avec l'extension `.pt`. 

Il existe trois types de modèles et 5 modèles de différentes tailles pour chaque type :

<table>
<tbody>
<tr>
<td>
<strong>Classification</strong>
</td>
<td>
<strong>Détection</strong>
</td>
<td>
<strong>Segmentation</strong>
</td>
<td>
<strong>Type</strong>
</td>
</tr>
<tr>
<td>
yolov8n-cls.pt
</td>
<td>
yolov8n.pt
</td>
<td>
yolov8n-seg.pt
</td>
<td>Nano</td>
</tr>
<tr>
<td>
yolov8s-cls.pt
</td>
<td>
yolov8s.pt
</td>
<td>
yolov8s-seg.pt
</td>
<td>Petit</td>
</tr>
<tr>
<td>
yolov8m-cls.pt
</td>
<td>
yolov8m.pt
</td>
<td>
yolov8m-seg.pt
</td>
<td>Moyen</td>
</tr>
<tr>
<td>
yolov8l-cls.pt
</td>
<td>
yolov8l.pt
</td>
<td>
yolov8l-seg.pt
</td>
<td>Grand</td>
</tr>
<tr>
<td>
yolov8x-cls.pt
</td>
<td>
yolov8x.pt
</td>
<td>
yolov8x-seg.pt
</td>
<td>Très grand</td>
</tr>
</tbody>
</table>

Plus le modèle que vous choisissez est grand, meilleure est la qualité de prédiction que vous pouvez atteindre, mais plus il sera lent.

Dans ce tutoriel, je couvrirai la détection d'objets - c'est pourquoi, dans l'extrait de code précédent, j'ai sélectionné "yolov8m.pt", qui est un modèle de taille moyenne pour la détection d'objets.

Lorsque vous exécutez ce code pour la première fois, il téléchargera le fichier `yolov8m.pt` depuis le serveur Ultralytics vers le dossier courant. Ensuite, il construira l'objet `model`. Maintenant, vous pouvez entraîner ce `model`, détecter des objets et l'exporter pour l'utiliser en production. Pour toutes ces tâches, il existe des méthodes pratiques :

* [train({chemin vers le fichier descriptif du jeu de données})](https://docs.ultralytics.com/modes/train/) - utilisé pour entraîner le modèle sur le jeu de données d'images.
* [predict({image})](https://docs.ultralytics.com/modes/predict) - utilisé pour faire une prédiction pour une image spécifiée, par exemple pour détecter les boîtes englobantes de tous les objets que le modèle peut trouver dans l'image.
* [export({format})](https://docs.ultralytics.com/modes/export/) - utilisé pour exporter le modèle du format PyTorch par défaut vers un format spécifié.

Tous les modèles YOLOv8 pour la détection d'objets sont déjà pré-entraînés sur le [jeu de données COCO](https://cocodataset.org/), qui est une énorme collection d'images de 80 types différents. Donc, si vous n'avez pas de besoins spécifiques, vous pouvez simplement l'exécuter tel quel, sans entraînement supplémentaire. 

Par exemple, vous pouvez télécharger cette image sous le nom "cat_dog.jpg" :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/cat_dog.jpg)
_Une image d'exemple avec un chat et un chien_

et exécuter `predict` pour détecter tous les objets qu'elle contient :

```python
results = model.predict("cat_dog.jpg")
```

La méthode `predict` accepte de nombreux types d'entrée différents, y compris un chemin vers une seule image, un tableau de chemins vers des images, l'objet Image de la bibliothèque Python bien connue [PIL](https://pillow.readthedocs.io/en/stable/), et [d'autres](https://docs.ultralytics.com/modes/predict/#sources).

Après avoir passé l'entrée à travers le modèle, il retourne un tableau de résultats pour chaque image d'entrée. Comme nous avons fourni une seule image, il retourne un tableau avec un seul élément que vous pouvez extraire comme ceci :

```python
result = results[0]
```

Le [résultat](https://docs.ultralytics.com/modes/predict/#working-with-results) contient les objets détectés et des propriétés pratiques pour travailler avec eux. La plus importante est le tableau `boxes` avec des informations sur les boîtes englobantes détectées sur l'image. Vous pouvez déterminer combien d'objets il a détectés en exécutant la fonction `len` :

```python
len(result.boxes)
```

Lorsque j'ai exécuté cela, j'ai obtenu "2", ce qui signifie qu'il y a deux boîtes détectées : une pour le chien et une pour le chat.

Ensuite, vous pouvez analyser chaque boîte soit dans une boucle, soit manuellement. Obtenons la première :

```python
box = result.boxes[0]
```

L'objet [box](https://docs.ultralytics.com/modes/predict/#boxes) contient les propriétés de la boîte englobante, y compris :

* `xyxy` - les coordonnées de la boîte sous forme de tableau [x1,y1,x2,y2]
* `cls` - l'ID du type d'objet
* `conf` - le niveau de confiance du modèle concernant cet objet. Si elle est très basse, comme < 0.5, alors vous pouvez simplement ignorer la boîte.

Affichons les informations sur la boîte détectée :

```python
print("Type d'objet :", box.cls)
print("Coordonnées :", box.xyxy)
print("Probabilité :", box.conf)
```

Pour la première boîte, vous recevrez les informations suivantes :

```bash
Type d'objet : tensor([16.])
Coordonnées : tensor([[261.1901,  94.3429, 460.5649, 312.9910]])
Probabilité : tensor([0.9528])
```

Comme je l'ai expliqué ci-dessus, YOLOv8 contient des modèles PyTorch. Les sorties des modèles PyTorch sont encodées sous forme de tableau d'objets PyTorch [Tensor](https://pytorch.org/docs/stable/tensors.html), vous devez donc extraire le premier élément de chacun de ces tableaux :

```python
print("Type d'objet :",box.cls[0])
print("Coordonnées :",box.xyxy[0])
print("Probabilité :",box.conf[0])
```

```bash
Type d'objet : tensor(16.)
Coordonnées : tensor([261.1901,  94.3429, 460.5649, 312.9910])
Probabilité : tensor(0.9528)
```

Maintenant, vous voyez les données sous forme d'objets `Tensor`. Pour extraire les valeurs réelles des tenseurs, vous devez utiliser la méthode `.tolist()` pour les tenseurs avec un tableau à l'intérieur, ainsi que la méthode `.item()` pour les tenseurs avec des valeurs scalaires. 

Extrayons les données dans les variables appropriées :

```python
cords = box.xyxy[0].tolist()
class_id = box.cls[0].item()
conf = box.conf[0].item()
print("Type d'objet :", class_id)
print("Coordonnées :", cords)
print("Probabilité :", conf)
```

```bash
Type d'objet : 16.0
Coordonnées : [261.1900634765625, 94.3428955078125, 460.5649108886719, 312.9909973144531]
Probabilité : 0.9528293609619141
```

Maintenant, vous voyez les données réelles. Les coordonnées peuvent être arrondies, et la probabilité peut également être arrondie à deux chiffres après la virgule.

Le type d'objet est `16` ici. Que signifie cela ? Parlons-en davantage.

Tous les objets que le réseau de neurones peut détecter ont des identifiants numériques. Dans le cas d'un modèle pré-entraîné YOLOv8, il y a 80 types d'objets avec des identifiants allant de 0 à 79. Les classes d'objets COCO sont bien connues et vous pouvez facilement les rechercher sur Internet. De plus, l'objet résultat YOLOv8 contient la propriété pratique `names` pour obtenir ces classes :

```python
print(result.names)
```

```bash
{0: 'personne',
 1: 'vélo',
 2: 'voiture',
 3: 'moto',
 4: 'avion',
 5: 'bus',
 6: 'train',
 7: 'camion',
 8: 'bateau',
 9: 'feu de circulation',
 10: 'bouche d'incendie',
 11: 'panneau stop',
 12: 'parcmètre',
 13: 'banc',
 14: 'oiseau',
 15: 'chat',
 16: 'chien',
 17: 'cheval',
 18: 'mouton',
 19: 'vache',
 20: 'éléphant',
 21: 'ours',
 22: 'zèbre',
 23: 'girafe',
 24: 'sac à dos',
 25: 'parapluie',
 26: 'sac à main',
 27: 'cravate',
 28: 'valise',
 29: 'frisbee',
 30: 'skis',
 31: 'planche de snowboard',
 32: 'balle de sport',
 33: 'cerf-volant',
 34: 'batte de baseball',
 35: 'gant de baseball',
 36: 'planche de skateboard',
 37: 'planche de surf',
 38: 'raquette de tennis',
 39: 'bouteille',
 40: 'verre à vin',
 41: 'tasse',
 42: 'fourchette',
 43: 'couteau',
 44: 'cuillère',
 45: 'bol',
 46: 'banane',
 47: 'pomme',
 48: 'sandwich',
 49: 'orange',
 50: 'brocoli',
 51: 'carotte',
 52: 'hot-dog',
 53: 'pizza',
 54: 'donut',
 55: 'gâteau',
 56: 'chaise',
 57: 'canapé',
 58: 'plante en pot',
 59: 'lit',
 60: 'table à manger',
 61: 'toilette',
 62: 'télévision',
 63: 'ordinateur portable',
 64: 'souris',
 65: 'télécommande',
 66: 'clavier',
 67: 'téléphone portable',
 68: 'micro-ondes',
 69: 'four',
 70: 'grille-pain',
 71: 'évier',
 72: 'réfrigérateur',
 73: 'livre',
 74: 'horloge',
 75: 'vase',
 76: 'ciseaux',
 77: 'ours en peluche',
 78: 'sèche-cheveux',
 79: 'brosse à dents'}
```

Ce dictionnaire contient tout ce que ce modèle peut détecter. Maintenant, vous pouvez voir que `16` est "chien", donc cette boîte englobante est la boîte englobante pour le chien détecté.

Modifions la sortie pour afficher les résultats de manière plus représentative :

```python
cords = box.xyxy[0].tolist()
cords = [round(x) for x in cords]
class_id = result.names[box.cls[0].item()]
conf = round(box.conf[0].item(), 2)
print("Type d'objet :", class_id)
print("Coordonnées :", cords)
print("Probabilité :", conf)
```

Dans ce code, j'ai arrondi toutes les coordonnées en utilisant la compréhension de liste Python [list comprehension](https://www.freecodecamp.org/news/list-comprehension-in-python-with-code-examples/). Ensuite, j'ai obtenu le nom de la classe d'objet détectée par ID en utilisant le dictionnaire `result.names`. J'ai également arrondi la probabilité. Vous devriez obtenir la sortie suivante :

```bash
Type d'objet : chien
Coordonnées : [261, 94, 461, 313]
Probabilité : 0.95
```

Ces données sont suffisamment bonnes pour être affichées dans l'interface utilisateur. Écrivons maintenant du code pour obtenir ces informations pour toutes les boîtes détectées dans une boucle :

```python
for box in result.boxes:
  class_id = result.names[box.cls[0].item()]
  cords = box.xyxy[0].tolist()
  cords = [round(x) for x in cords]
  conf = round(box.conf[0].item(), 2)
  print("Type d'objet :", class_id)
  print("Coordonnées :", cords)
  print("Probabilité :", conf)
  print("---")
```

Ce code fera la même chose pour chaque boîte et produira la sortie suivante :

```python
Type d'objet : chien
Coordonnées : [261, 94, 461, 313]
Probabilité : 0.95
---
Type d'objet : chat
Coordonnées : [140, 170, 256, 316]
Probabilité : 0.92
---
```

De cette manière, vous pouvez exécuter la détection d'objets pour d'autres images et voir tout ce qu'un modèle entraîné sur COCO peut détecter.

Cette vidéo montre toute la session de codage de cette section dans Jupyter Notebook, en supposant que vous l'avez [installé](https://jupyter.org/install).

%[https://youtu.be/8Q87QYlonRU]

Utiliser des modèles pré-entraînés sur des objets bien connus est bien pour commencer. Mais en pratique, vous pourriez avoir besoin d'une solution pour détecter des objets spécifiques pour un problème concret.

Par exemple, quelqu'un pourrait avoir besoin de détecter des produits spécifiques sur les étagères d'un supermarché ou de découvrir des tumeurs cérébrales sur des radiographies. Il est très probable que ces informations ne soient pas disponibles dans les jeux de données publics, et qu'il n'existe pas de modèles gratuits qui connaissent tout.

Vous devez donc enseigner à votre propre modèle à détecter ces types d'objets. Pour cela, vous devez créer une base de données d'images annotées pour votre problème et entraîner le modèle sur ces images.

<h1 id="donnees">Comment préparer les données pour entraîner le modèle YOLOv8</h1>

Pour entraîner le modèle, vous devez préparer des images annotées et les diviser en jeux de données d'entraînement et de validation. 

Vous utiliserez le jeu d'entraînement pour enseigner le modèle et le jeu de validation pour tester les résultats de l'étude et mesurer la qualité du modèle entraîné. Vous pouvez mettre 80 % des images dans le jeu d'entraînement et 20 % dans le jeu de validation.

Voici les étapes que vous devez suivre pour créer chacun des jeux de données :

1. Décidez et encodez les classes d'objets que vous souhaitez enseigner à votre modèle à détecter. Par exemple, si vous souhaitez détecter uniquement des chats et des chiens, vous pouvez indiquer que "0" est un chat et "1" est un chien.
2. Créez un dossier pour votre jeu de données et deux sous-dossiers : "images" et "labels".
3. Ajoutez les images au sous-dossier "images". Plus vous collectez d'images, mieux c'est pour l'entraînement.
4. Pour chaque image, créez un fichier texte d'annotation dans le sous-dossier "labels". Les fichiers texte d'annotation doivent avoir les mêmes noms que les fichiers image et l'extension ".txt". Dans les fichiers d'annotation, vous devez ajouter des enregistrements pour chaque objet qui existe sur l'image appropriée au format suivant :

```
{object_class_id} {x_center} {y_center} {width} {height}
```

![Image](https://www.freecodecamp.org/news/content/images/2023/04/bounding_box.png)
_Paramètres de la boîte englobante_

C'est le travail manuel le plus chronophage dans le processus d'apprentissage automatique : mesurer les boîtes englobantes pour tous les objets et les ajouter aux fichiers d'annotation. 

Vous devez également normaliser les coordonnées pour qu'elles soient comprises entre 0 et 1. Pour les calculer, vous devez utiliser les formules suivantes :

* x_center = (box_x_left+box_x_width/2)/image_width
* y_center = (box_y_top+box_height/2)/image_height
* width = box_width/image_width
* height = box_height/image_height

Par exemple, si vous souhaitez ajouter l'image "cat_dog.jpg" que nous avons utilisée précédemment au jeu de données, vous devez la copier dans le dossier "images" puis mesurer et collecter les données suivantes sur l'image et ses boîtes englobantes :

**Image :**

image_width = 612  
image_height = 415

**Objets :**

<table>
<tbody>
<tr>
<td><strong>Chien</strong></td>
<td><strong>Chat</strong></td>
</tr>
<tr>
<td>
box_x_left=261<br/> 
box_x_top=94<br/>
box_width=200<br/>
box_height=219
</td>
<td>
box_x_left=140<br/>
box_x_top=170<br/>
box_width=116<br/>
box_height=146
</td>
</tr>
</tbody>
</table>

Ensuite, créez le fichier "cat_dog.txt" dans le dossier "labels" et, en utilisant les formules ci-dessus, calculez les coordonnées :

Chien (class id=1) :

x_center = (261+200/2)/612 = 0.589869281  
y_center = (94+219/2)/415 = 0.490361446  
width = 200/612 = 0.326797386  
height = 219/415 = 0.527710843

Chat (class id=0)

x_center = (140+116/2)/612 = 0.323529412  
y_center = (170+146/2)/415 = 0.585542169  
width = 116/612 = 0.189542484  
height = 146/415 = 0.351807229

et ajoutez les lignes suivantes au fichier :

```
1 0.589869281 0.490361446 0.326797386 0.527710843
0 0.323529412 0.585542169 0.189542484 0.351807229
```

La première ligne contient une boîte englobante pour le chien (class id=1). La deuxième ligne contient une boîte englobante pour le chat (class id=0). Bien sûr, vous pouvez avoir une image avec plusieurs chiens et plusieurs chats en même temps, et vous pouvez ajouter des boîtes englobantes pour tous.

Après avoir ajouté et annoté toutes les images, le jeu de données est prêt. Vous devez créer deux jeux de données et les placer dans des dossiers différents. La structure finale des dossiers peut ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/dataset_structure.png)
_Structure du jeu de données_

Comme vous pouvez le voir, le jeu de données d'entraînement est situé dans le dossier "train" et le jeu de données de validation est situé dans le dossier "val".

Enfin, vous devez créer un fichier YAML descriptif du jeu de données qui pointe vers les jeux de données créés et décrit les classes d'objets qu'ils contiennent. Voici un exemple de ce fichier pour les données créées ci-dessus :

```yaml
train: ../train/images
val: ../val/images

nc: 2
names: ['chat','chien']
```

Dans les deux premières lignes, vous devez spécifier les chemins vers les images des jeux de données d'entraînement et de validation. Les chemins peuvent être relatifs au dossier courant ou absolus. 

Ensuite, la ligne `nc` spécifie le **n**ombre de **c**lasses qui existent dans ces jeux de données, et `names` est un tableau de noms de classes dans le bon ordre. 

Les index de ces éléments sont les nombres que vous avez utilisés lors de l'annotation des images, et ces index seront retournés par le modèle lorsqu'il détecte des objets en utilisant la méthode `predict`. Donc, si vous avez utilisé "0" pour les chats, alors il devrait être le premier élément dans le tableau `names`.

Ce fichier YAML doit être passé à la méthode `train` du modèle pour démarrer le processus d'entraînement.

Pour faciliter le processus d'annotation des images, il existe de nombreux programmes que vous pouvez utiliser pour annoter visuellement les images pour l'apprentissage automatique. Vous pouvez rechercher quelque chose comme "logiciel pour annoter des images pour l'apprentissage automatique" pour obtenir une liste de ces programmes. 

Il existe également de nombreux outils en ligne qui peuvent faire tout ce travail, comme [Roboflow Annotate](https://roboflow.com/annotate). En utilisant ce service, vous devez simplement télécharger vos images, dessiner des boîtes englobantes sur elles et définir des classes pour chaque boîte englobante. Ensuite, l'outil créera automatiquement des fichiers d'annotation, divisera vos données en jeux de données d'entraînement et de validation, et créera un fichier descriptif YAML. Ensuite, vous pouvez exporter et télécharger les données annotées sous forme de fichier ZIP.

Dans la vidéo ci-dessous, je vous montre comment utiliser Roboflow pour créer le micro-jeu de données "chats et chiens".

%[https://youtu.be/sLZRfzaRBwg]

Pour des problèmes réels, cette base de données doit être beaucoup plus grande. Pour entraîner un bon modèle, vous devez avoir des centaines ou des milliers d'images annotées.

De plus, lors de la préparation de la base de données d'images, essayez de la rendre équilibrée. Elle doit avoir un nombre égal d'objets de chaque classe, c'est-à-dire un nombre égal de chiens et de chats dans cet exemple. Sinon, le modèle entraîné sur celle-ci peut prédire une classe mieux qu'une autre.

Après que les données sont prêtes, copiez-les dans le dossier avec votre code Python que vous utiliserez pour l'entraînement et retournez à votre Jupyter Notebook pour commencer le processus d'entraînement.

<h1 id="entrainement">Comment entraîner le modèle YOLOv8</h1>

Après que les données sont prêtes, vous devez les passer à travers le modèle. Pour rendre cela plus intéressant, nous n'utiliserons pas ce petit jeu de données "chats et chiens". Nous utiliserons un autre jeu de données personnalisé pour l'entraînement qui contient des [feux de circulation et des panneaux de signalisation](https://universe.roboflow.com/roboflow-100/road-signs-6ih4y). Il s'agit d'un jeu de données gratuit que j'ai obtenu de Roboflow Universe. Appuyez sur "Télécharger le jeu de données" et sélectionnez "YOLOv8" comme format.

Si ce n'est pas disponible sur Roboflow lorsque vous lisez ceci, vous pouvez l'obtenir depuis [mon Google Drive](https://drive.google.com/file/d/1PNktsghBqIJVgxa-34FqO3yODNJbH3B0/view?usp=sharing). Vous pouvez utiliser ce jeu de données pour enseigner à YOLOv8 à détecter différents objets sur les routes, comme vous pouvez le voir dans la capture d'écran suivante.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/traffic_lights.png)
_Démo de détection des feux de circulation_

Vous pouvez ouvrir le fichier zip téléchargé et vous assurer qu'il est déjà annoté et structuré en utilisant les règles décrites ci-dessus. Vous pouvez également trouver le fichier descriptif du jeu de données `data.yaml` dans l'archive.

Si vous avez téléchargé l'archive depuis Roboflow, elle contiendra le jeu de données "test" supplémentaire, qui n'est pas utilisé par le processus d'entraînement. Vous pouvez utiliser les images de celui-ci pour des tests supplémentaires après l'entraînement.

Extrayez l'archive dans le dossier avec votre code Python et exécutez la méthode `train` pour démarrer une boucle d'entraînement :

```python
model.train(data="data.yaml", epochs=30)
```

La `data` est la seule option requise. Vous devez lui passer le fichier descriptif YAML. L'option `epochs` spécifie le nombre de cycles d'entraînement (100 par défaut). Il existe d'autres [options](https://docs.ultralytics.com/modes/train/#arguments) qui peuvent affecter le processus et la qualité du modèle entraîné.

Chaque cycle d'entraînement se compose de deux phases : une phase d'entraînement et une phase de validation.

Pendant la phase d'entraînement, la méthode `train` fait ce qui suit :

* Extrait un lot aléatoire d'images du jeu de données d'entraînement (le nombre d'images dans le lot peut être spécifié en utilisant l'option `batch`).
* Passe ces images à travers le modèle et reçoit les boîtes englobantes résultantes de tous les objets détectés et leurs classes.
* Passe le résultat à la fonction de perte qui est utilisée pour comparer la sortie reçue avec le résultat correct des fichiers d'annotation pour ces images. La fonction de perte calcule la quantité d'erreur.
* Le résultat de la fonction de perte est passé à l'`optimizer` pour ajuster les poids du modèle en fonction de la quantité d'erreur dans la bonne direction. Cela réduit les erreurs dans le cycle suivant. Par défaut, l'optimiseur [SGD (Stochastic Gradient Descent)](https://towardsdatascience.com/stochastic-gradient-descent-clearly-explained-53d239905d31) est utilisé, mais vous pouvez essayer d'autres, comme [Adam](https://www.linkedin.com/pulse/understanding-adam-optimizer-gradient-descent-evan-dunbar/), pour voir la différence.

Pendant la phase de validation, `train` fait ce qui suit :

* Extrait les images du jeu de données de validation.
* Les passe à travers le modèle et reçoit les boîtes englobantes détectées pour ces images.
* Compare le résultat reçu avec les valeurs réelles pour ces images à partir des fichiers texte d'annotation.
* Calcule la précision du modèle en fonction de la différence entre les résultats réels et attendus.

La progression et les résultats de chaque phase pour chaque époque sont affichés à l'écran. De cette manière, vous pouvez voir comment le modèle apprend et s'améliore d'époque en époque.

Lorsque vous exécutez le code `train`, vous verrez une sortie similaire à la suivante pendant la boucle d'entraînement :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/training.png)
_Processus d'entraînement_

Pour chaque époque, il montre un résumé pour les phases d'entraînement et de validation : les lignes 1 et 2 montrent les résultats de la phase d'entraînement et les lignes 3 et 4 montrent les résultats de la phase de validation pour chaque époque.

La phase d'entraînement inclut un calcul de la quantité d'erreur dans une fonction de perte, donc les métriques les plus précieuses ici sont `box_loss` et `cls_loss`.

* `box_loss` montre la quantité d'erreur dans les boîtes englobantes détectées.
* `cls_loss` montre la quantité d'erreur dans les classes d'objets détectées.

Pourquoi la perte est-elle divisée en différentes métriques ? Parce que le modèle pourrait correctement détecter les coordonnées de la boîte englobante autour de l'objet, mais incorrectement détecter la classe de l'objet dans cette boîte. Par exemple, dans ma pratique, il a détecté le chien comme un cheval, mais les dimensions de l'objet ont été détectées correctement.

Si le modèle apprend vraiment quelque chose à partir des données, alors vous devriez voir que ces valeurs diminuent d'époque en époque. Dans une capture d'écran précédente, le `box_loss` a diminué : 0.7751, 0.7473, 0.742 et le `cls_loss` a également diminué : 0.702, 0.6422, 0.6211.

Dans la phase de validation, il calcule la qualité du modèle après l'entraînement en utilisant les images du jeu de données de validation. 

La métrique de qualité la plus précieuse est mAP50-95, qui est la [Précision Moyenne Moyenne](https://www.v7labs.com/blog/mean-average-precision). Si le modèle apprend et s'améliore, la précision devrait augmenter d'époque en époque. Dans une capture d'écran précédente, vous pouvez voir qu'elle a lentement augmenté : 0.788, 0.788, 0.791.

Si après la dernière époque vous n'avez pas obtenu une précision acceptable, vous pouvez augmenter le nombre d'époques et relancer l'entraînement. Vous pouvez également ajuster d'autres paramètres comme `batch`, `lr0`, `lrf` ou changer l'`optimizer` que vous utilisez. Il n'y a pas de règles claires sur ce qu'il faut faire ici, mais il y a beaucoup de recommandations.

Le sujet de l'ajustement des paramètres du processus d'entraînement dépasse le cadre de cet article. Je pense qu'il est possible d'écrire un livre à ce sujet et beaucoup d'entre eux existent déjà. Vous pouvez facilement les trouver sur Internet. Mais en quelques mots, la plupart d'entre eux disent que vous devez expérimenter et essayer toutes les options possibles et comparer les résultats.

En plus des métriques qui sont affichées pendant le processus d'entraînement, il écrit beaucoup de statistiques sur le disque. Lorsque l'entraînement commence, il crée le sous-dossier `runs/detect/train` dans le dossier courant et après chaque époque, il enregistre différents fichiers de journalisation.

Il exporte également le modèle entraîné après chaque époque vers le fichier `/runs/detect/train/weights/last.pt` et le modèle avec la plus haute précision vers le fichier `/runs/detect/train/weights/best.pt`. Ainsi, après la fin de l'entraînement, vous pouvez obtenir le fichier `best.pt` pour l'utiliser en production.

Vous pouvez regarder cette vidéo pour en savoir plus sur le fonctionnement du processus d'entraînement. J'ai utilisé [Google Colab](https://colab.research.google.com/) qui est une version cloud de Jupyter Notebook pour accéder à du matériel avec un GPU plus puissant afin d'accélérer le processus d'entraînement. 

La vidéo montre comment entraîner le modèle sur 5 époques et télécharger le modèle final `best.pt`. Dans les problèmes du monde réel, vous devez exécuter beaucoup plus d'époques et être prêt à attendre des heures ou peut-être des jours jusqu'à ce que l'entraînement se termine.

%[https://youtu.be/HZobbSjbAUc]

Une fois terminé, il est temps d'exécuter le modèle entraîné en production. Dans la section suivante, nous créerons un service web pour détecter des objets dans des images en ligne dans un navigateur web.

<h1 id="detect">Comment créer un service web de détection d'objets
</h1>

À ce stade, nous avons terminé les expériences avec le modèle dans le Jupyter Notebook. Vous devrez écrire le prochain lot de code en tant que projet séparé, en utilisant n'importe quel IDE Python comme [VS Code](https://code.visualstudio.com/) ou [PyCharm](https://www.jetbrains.com/pycharm/).

Le service web que nous allons créer aura une page web avec un champ de saisie de fichier et un élément canvas HTML5. 

Lorsque l'utilisateur sélectionne un fichier image à l'aide du champ de saisie, l'interface l'enverra au backend. Ensuite, le backend passera l'image à travers le modèle que nous avons créé et entraîné et retournera le tableau des boîtes englobantes détectées à la page web. 

Lorsque celle-ci le reçoit, le frontend dessinera l'image sur l'élément canvas et les boîtes englobantes détectées par-dessus.

Le service fonctionnera et apparaîtra comme démontré dans cette vidéo :

%[https://youtu.be/iOIfm_5QIiw]

Dans la vidéo, j'ai utilisé le modèle entraîné sur 30 époques, et il ne détecte toujours pas certains feux de circulation. Vous pouvez essayer de l'entraîner davantage pour obtenir de meilleurs résultats. Mais la meilleure façon d'améliorer la qualité d'un modèle d'apprentissage automatique est d'ajouter de plus en plus de données. 

Ainsi, en tant qu'exercice supplémentaire, vous pouvez importer le dossier du jeu de données dans Roboflow, ajouter et annoter plus d'images, puis utiliser les données mises à jour pour continuer à entraîner le modèle.

<h2 id="frontend">Comment créer le Frontend</h2>

Pour commencer, créez un dossier pour un nouveau projet Python et un fichier `index.html` pour la page web frontend. Voici le contenu de ce fichier :

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Détection d'objets YOLOv8</title>
    <style>
        canvas {
            display:block;
            border: 1px solid black;
            margin-top:10px;
        }
    </style>
</head>
<body>
    <input id="uploadInput" type="file"/>
    <canvas></canvas>
    <script>
       /**
       * Gestionnaire "onClick" du bouton "Upload" : télécharge le fichier image sélectionné 
       * vers le backend, reçoit un tableau d'objets détectés et les dessine sur l'image
       */
       const input = document.getElementById("uploadInput");
       input.addEventListener("change",async(event) => {
           const file = event.target.files[0];
           const data = new FormData();
           data.append("image_file",file,"image_file");
           const response = await fetch("/detect",{
               method:"post",
               body:data
           });
           const boxes = await response.json();
           draw_image_and_boxes(file,boxes);
       })

       /**
       * Fonction qui dessine l'image à partir du fichier fourni
       * et les boîtes englobantes des objets détectés sur
       * le dessus de l'image
       * @param file Objet fichier téléchargé
       * @param boxes Tableau de boîtes englobantes au format
         [[x1,y1,x2,y2,object_type,probability],...]
       */
       function draw_image_and_boxes(file,boxes) {
          const img = new Image()
          img.src = URL.createObjectURL(file);
          img.onload = () => {
              const canvas = document.querySelector("canvas");
              canvas.width = img.width;
              canvas.height = img.height;
              const ctx = canvas.getContext("2d");
              ctx.drawImage(img,0,0);
              ctx.strokeStyle = "#00FF00";
              ctx.lineWidth = 3;
              ctx.font = "18px serif";
              boxes.forEach(([x1,y1,x2,y2,label]) => {
                  ctx.strokeRect(x1,y1,x2-x1,y2-y1);
                  ctx.fillStyle = "#00ff00";
                  const width = ctx.measureText(label).width;
                  ctx.fillRect(x1,y1,width+10,25);
                  ctx.fillStyle = "#000000";
                  ctx.fillText(label,x1,y1+18);
              });
          }
       }
  </script>  
</body>
</html>
```

La partie HTML est très petite et se compose uniquement du champ de saisie de fichier avec l'ID "uploadInput" et de l'élément canvas en dessous.

Ensuite, dans la partie JavaScript, l'événement "onChange" définit le gestionnaire d'événements pour le champ de saisie. Lorsque l'utilisateur sélectionne un fichier image, le gestionnaire utilise `fetch` pour faire une requête POST à l'endpoint backend `/detect` (que nous créerons plus tard) et envoie ce fichier image.

Le backend doit détecter les objets sur cette image et retourner une réponse avec un tableau `boxes` en JSON. Cette réponse est ensuite décodée et passée à la fonction `draw_image_and_boxes` ainsi que le fichier image lui-même.

La fonction `draw_image_and_boxes` charge l'image à partir du fichier. Dès qu'elle est chargée, elle la dessine sur le canvas. Ensuite, elle dessine chaque boîte englobante avec une étiquette de classe sur le dessus du canvas avec l'image.

Créons maintenant le backend avec un endpoint `/detect` pour cela.

<h2 id="backend">Comment créer le Backend</h2>

Nous créerons le backend en utilisant [Flask](https://flask.palletsprojects.com/en/2.2.x/). Flask a son propre serveur web interne, mais selon de nombreux développeurs Flask, il n'est pas assez fiable pour la production. Nous utiliserons donc le serveur web [Waitress](https://flask.palletsprojects.com/en/2.2.x/deploying/waitress/) et exécuterons notre application Flask dans celui-ci.

De plus, nous utiliserons la bibliothèque [Pillow](https://pillow.readthedocs.io/en/stable/) pour lire les fichiers binaires téléchargés en tant qu'images. Assurez-vous d'avoir tous ces packages installés sur votre système avant de continuer :

```bash
pip3 install flask
pip3 install waitress
pip3 install pillow
```

Le backend sera dans un seul fichier. Nommons-le `object_detector.py` :

```python
from ultralytics import YOLO
from flask import request, Response, Flask
from waitress import serve
from PIL import Image
import json

app = Flask(__name__)

@app.route("/")
def root():
    """
    Fonction de gestionnaire de la page principale du site.
    :return: Contenu du fichier index.html
    """
    with open("index.html") as file:
        return file.read()


@app.route("/detect", methods=["POST"])
def detect():
    """
        Gestionnaire de l'endpoint POST /detect
        Reçoit le fichier téléchargé avec le nom "image_file", 
        le passe à travers le réseau de détection d'objets YOLOv8 
        et retourne un tableau de boîtes englobantes.
        :return: un tableau JSON d'objets de boîtes englobantes au format 
        [[x1,y1,x2,y2,object_type,probability],..]
    """
    buf = request.files["image_file"]
    boxes = detect_objects_on_image(Image.open(buf.stream))
    return Response(
      json.dumps(boxes),  
      mimetype='application/json'
    )


def detect_objects_on_image(buf):
    """
    La fonction reçoit une image,
    la passe à travers le réseau de neurones YOLOv8
    et retourne un tableau d'objets détectés
    et leurs boîtes englobantes
    :param buf: Flux de fichier image d'entrée
    :return: Tableau de boîtes englobantes au format 
    [[x1,y1,x2,y2,object_type,probability],..]
    """
    model = YOLO("best.pt")
    results = model.predict(buf)
    result = results[0]
    output = []
    for box in result.boxes:
        x1, y1, x2, y2 = [
          round(x) for x in box.xyxy[0].tolist()
        ]
        class_id = box.cls[0].item()
        prob = round(box.conf[0].item(), 2)
        output.append([
          x1, y1, x2, y2, result.names[class_id], prob
        ])
    return output

serve(app, host='0.0.0.0', port=8080)
```

Tout d'abord, nous importons les bibliothèques requises :

* [ultralytics](https://github.com/ultralytics/ultralytics) pour le modèle YOLOv8.
* [flask](https://flask.palletsprojects.com/en/2.2.x/) pour créer une application web `Flask`, recevoir des `requests` du frontend et envoyer des `responses` en retour.
* [waitress](https://flask.palletsprojects.com/en/2.2.x/deploying/waitress/) pour exécuter un serveur web et `serve` l'application web `app` Flask.
* [PIL](https://pillow.readthedocs.io/en/stable/) pour charger un fichier téléchargé en tant qu'objet `Image`, requis pour YOLOv8.
* [json](https://docs.python.org/3/library/json.html) pour convertir le tableau de boîtes englobantes en JSON avant de le retourner au frontend.

Ensuite, nous avons défini deux routes :

* `/` qui sert de racine du service web. Il retourne simplement le contenu du fichier "index.html".
* `/detect` qui répond à une requête de téléchargement d'image du frontend. Il convertit le fichier RAW en objet Image Pillow, puis passe cette image à la fonction `detect_objects_on_image`.

La fonction `detect_objects_on_image` crée un objet modèle basé sur le modèle `best.pt` que nous avons entraîné dans la section précédente. Assurez-vous que ce fichier existe dans le dossier où vous écrivez le code.

Ensuite, elle appelle la méthode `predict` pour l'image. `predict` retourne les boîtes englobantes détectées. 

Ensuite, pour chaque boîte, elle extrait les coordonnées, le nom de la classe et la probabilité de la même manière que nous l'avons fait au début du tutoriel. Elle ajoute ces informations au tableau de sortie. 

Enfin, la fonction retourne le tableau des coordonnées des objets détectés et leurs classes.

Après cela, le tableau est encodé en JSON et retourné au frontend.

La dernière ligne de code démarre le serveur web sur le port 8080 qui sert l'application Flask `app`.

Pour exécuter le service, exécutez la commande suivante :

```bash
python3 object_detector.py
```

Si tout fonctionne correctement, vous pouvez ouvrir `http://localhost:8080` dans un navigateur web. Il devrait afficher la page `index.html`. Lorsque vous sélectionnez un fichier image, il le traitera et affichera des boîtes englobantes autour de tous les objets détectés (ou simplement afficher l'image si rien n'est détecté dessus).

Le service web que nous venons de créer est universel. Vous pouvez l'utiliser avec n'importe quel modèle YOLOv8. Pour l'instant, il détecte les feux de circulation et les panneaux de signalisation en utilisant le modèle `best.pt` que nous avons créé. Mais vous pouvez le modifier pour utiliser un autre modèle, comme le modèle `yolov8m.pt` que nous avons utilisé précédemment pour détecter les chats, les chiens et toutes les autres classes d'objets que les modèles pré-entraînés YOLOv8 peuvent détecter.

<h1 id="conclusion">Conclusion</h1>

Dans ce tutoriel, je vous ai guidé à travers le processus de création d'une application web alimentée par l'IA qui utilise YOLOv8, un réseau de neurones convolutifs de pointe pour la détection d'objets. 

Je vous ai montré comment créer des modèles en utilisant les modèles pré-entraînés et préparer les données pour entraîner des modèles personnalisés. Et enfin, nous avons créé une application web avec un frontend et un backend qui utilise le modèle YOLOv8 entraîné personnalisé pour détecter les feux de circulation et les panneaux de signalisation.

Vous pouvez trouver le code source de cette application dans [ce dépôt GitHub](https://github.com/AndreyGermanov/yolov8_pytorch_python). 

Pour toutes ces tâches, nous avons utilisé les API de haut niveau Ultralytics qui accompagnent le package YOLOv8 par défaut. Ces API sont basées sur le framework PyTorch, qui a été utilisé pour créer la plus grande partie des réseaux de neurones d'aujourd'hui. 

C'est assez pratique d'un côté, mais la dépendance à ces API de haut niveau a également un effet négatif. Si vous devez exécuter cette application web en production, vous devez installer tous ces environnements, y compris Python, PyTorch et les autres dépendances.

Pour exécuter cela sur un nouveau serveur propre, vous devrez télécharger et installer plus de 1 Go de bibliothèques tierces ! Ce n'est définitivement pas la meilleure façon de procéder. 

De plus, que faire si vous n'avez pas Python dans votre environnement de production ? Que faire si tout votre autre code est écrit dans un autre langage de programmation, et que vous ne prévoyez pas d'utiliser Python ? Ou que faire si vous souhaitez exécuter le modèle sur un téléphone mobile avec Android ou iOS ?

Tout cela pour dire que l'utilisation des packages Ultralytics est excellente pour expérimenter, entraîner et préparer les modèles pour la production. Mais en production elle-même, vous devez charger et utiliser le modèle directement et ne pas utiliser ces API de haut niveau. 

Pour ce faire, vous devez comprendre comment fonctionne le réseau de neurones YOLOv8 sous le capot et écrire plus de code pour fournir des entrées au modèle et traiter la sortie de celui-ci. Cela rendra vos applications plus rapides et moins gourmandes en ressources. Vous n'aurez pas besoin d'avoir PyTorch installé pour exécuter votre modèle de détection d'objets. 

De plus, vous pourrez exécuter vos modèles même sans Python, en utilisant de nombreux autres langages de programmation, y compris Julia, C++, Go, Node.js en backend, ou même sans backend du tout. Vous pouvez exécuter les modèles YOLOv8 directement dans un navigateur, en utilisant uniquement JavaScript en frontend. 

Vous voulez savoir comment ? Ce sera le sujet de mon prochain article sur YOLOv8.

Vous pouvez me trouver sur [LinkedIn](https://www.linkedin.com/in/andrey-germanov-dev/), [Twitter](https://twitter.com/GermanovDev), et [Facebook](https://www.facebook.com/AndreyGermanovDev) pour être le premier informé des nouveaux articles comme celui-ci et d'autres nouvelles sur le développement logiciel.

Amusez-vous bien en codant et ne cessez jamais d'apprendre !