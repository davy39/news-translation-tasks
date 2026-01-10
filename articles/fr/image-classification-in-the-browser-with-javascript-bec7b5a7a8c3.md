---
title: Classification d'images dans le navigateur avec JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-21T19:50:51.000Z'
originalURL: https://freecodecamp.org/news/image-classification-in-the-browser-with-javascript-bec7b5a7a8c3
coverImage: https://cdn-media-1.freecodecamp.org/images/0*GYFA_HewF-gOUuHQ.jpg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Deep Learning
  slug: deep-learning
- name: image classification
  slug: image-classification
- name: Machine Learning
  slug: machine-learning
- name: TensorFlow
  slug: tensorflow
seo_title: Classification d'images dans le navigateur avec JavaScript
seo_desc: 'By Kevin Scott

  Machine Learning has a reputation for demanding lots of data and powerful GPU computations.
  This leads many people to believe that building custom machine learning models for
  their specific dataset is impractical without a large invest...'
---

Par Kevin Scott

Le Machine Learning a la réputation de nécessiter beaucoup de données et des calculs puissants sur GPU. Cela conduit de nombreuses personnes à croire que la création de modèles de machine learning personnalisés pour leur ensemble de données spécifique est irréalisable sans un investissement important en temps et en ressources. En fait, vous pouvez exploiter le Transfer Learning sur le web pour entraîner un classificateur d'images précis en moins d'une minute avec seulement quelques images étiquetées.

### À quoi sert la classification d'images ?

Apprendre à une machine à classer des images a une large gamme d'applications pratiques. Vous avez peut-être vu la classification d'images à l'œuvre dans votre application de photos, suggérant automatiquement des amis ou des lieux pour le marquage. La classification d'images peut être utilisée pour [reconnaître des cellules cancéreuses](https://www.kaggle.com/c/data-science-bowl-2017), pour [reconnaître des navires dans des images satellites](https://www.kaggle.com/c/airbus-ship-detection), ou pour [classer automatiquement des images sur Yelp](https://www.kaggle.com/c/yelp-restaurant-photo-classification). Elle peut même être utilisée au-delà du domaine des images, analysant des cartes thermiques de l'activité des utilisateurs pour détecter des fraudes potentielles, ou des transformées de Fourier d'ondes audio.

J'ai récemment [publié un outil open source](https://github.com/thekevinscott/ml-classifier) pour entraîner rapidement des modèles de classification d'images dans votre navigateur. Voici comment cela fonctionne :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Qt2zblWA9QDpqAilqovj3Q.gif)
_[https://thekevinscott.github.io/ml-classifier-ui/](https://thekevinscott.github.io/ml-classifier-ui/" rel="noopener" target="_blank" title=")_

[Intégré ici](http://thekevinscott.github.io/ml-classifier-ui/) se trouve une démonstration en direct de l'outil que vous pouvez utiliser. [J'ai préparé un ensemble de données pour les tests ici](https://github.com/thekevinscott/dataset-tutorial-for-image-classification/data%3CPaste%3E) (ou vous pouvez créer le vôtre). L'ensemble de données contient 10 images que j'ai téléchargées pour chacune des trois recherches les plus populaires sur [pexels.com](https://pexels.com) : Mobile, Wood, et Notebook.

Glissez le dossier **train** dans la zone de dépôt, et une fois le modèle entraîné, téléchargez le dossier **validation** pour voir à quel point votre modèle peut classer de nouvelles images.

#### Comment cela fonctionne-t-il ?

Le Transfer Learning est l'ingrédient secret qui permet d'entraîner des modèles extrêmement précis dans votre navigateur en une fraction du temps. Les modèles sont entraînés sur de grands corpus de données et sauvegardés sous forme de modèles pré-entraînés. Les couches finales de ces modèles pré-entraînés peuvent ensuite être ajustées pour votre cas d'utilisation spécifique.

Cela fonctionne particulièrement bien dans le domaine de la vision par ordinateur, car de nombreuses caractéristiques des images sont généralisables. Rob Fergus et Matthew Zeiler [démontrent dans leur article](https://arxiv.org/abs/1311.2901) les caractéristiques apprises aux premiers stades de leur modèle :

![Image](https://cdn-media-1.freecodecamp.org/images/0*5QnKBdFPZXYYP1EZ.png)
_Caractéristiques de bas niveau_

Le modèle commence à reconnaître des caractéristiques génériques, y compris des lignes, des cercles et des formes, applicables à tout ensemble d'images. Après quelques couches supplémentaires, il est capable de reconnaître des formes plus complexes comme des bords et des mots :

![Image](https://cdn-media-1.freecodecamp.org/images/0*1oDY_PFqmMdtvteE.png)
_Caractéristiques de haut niveau_

La grande majorité des images partagent des caractéristiques générales telles que des lignes et des cercles. Beaucoup partagent des caractéristiques de haut niveau, des choses comme un "œil" ou un "nez". Cela vous permet de réutiliser l'entraînement existant qui a déjà été fait, et d'ajuster uniquement les dernières couches sur votre ensemble de données spécifique, ce qui est plus rapide et nécessite moins de données que l'entraînement à partir de zéro.

Combien de données en moins ? **Cela dépend**. À quel point vos données diffèrent de votre modèle pré-entraîné, à quel point vos données sont complexes ou variables, et d'autres facteurs peuvent tous influencer votre précision. Avec l'exemple ci-dessus, j'ai atteint 100 % de précision avec 30 images. Pour quelque chose comme des chiens et des chats, une poignée d'images suffit pour obtenir de bons résultats. [Adrian G a réalisé une analyse plus rigoureuse sur son blog](https://medium.com/@bingobee01/how-much-data-to-you-need-ba834d074f3a).

Donc, cela dépend de votre ensemble de données, mais c'est probablement moins que vous ne le pensez.

### Montrez-moi le code !

Ensuite, nous verrons comment importer et ajuster un modèle pré-entraîné en JavaScript. Nous ajusterons [MobileNet](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md), un modèle pré-entraîné produit par Google.

> Les MobileNets sont une classe de réseau de neurones convolutifs conçus par des chercheurs de Google. Ils sont qualifiés de "mobile-first" car ils sont architecturés dès le départ pour être économes en ressources et fonctionner rapidement, directement sur votre téléphone. — [Matt Harvey](https://hackernoon.com/creating-insanely-fast-image-classifiers-with-mobilenet-in-tensorflow-f030ce0a2991)

MobileNet est entraîné sur un énorme corpus d'images appelé [ImageNet](http://www.image-net.org/), contenant plus de 14 millions d'images étiquetées appartenant à 1000 catégories différentes. Si vous téléchargez `mobilenet_v1_0.25_224`, vous verrez une structure de fichiers comme :

```
mobilenet_v1_0.25_224.ckpt.data-00000-of-00001mobilenet_v1_0.25_224.ckpt.indexmobilenet_v1_0.25_224.ckpt.metamobilenet_v1_0.25_224.tflitemobilenet_v1_0.25_224_eval.pbtxtmobilenet_v1_0.25_224_frozen.pbmobilenet_v1_0.25_224_info.txt
```

Dans `mobilenet_v1_0.25_224_eval.pbtxt`, notez l'attribut `shape` :

```
attr {    key: "shape"    value {      shape {        dim {          size: -1        }        dim {          size: 224        }        dim {          size: 224        }        dim {          size: 3        }      }    }  }
```

Cela nous indique que la première couche de ce MobileNet s'attend à recevoir un tenseur de rang 4 avec les dimensions `[any, 224, 224, 3]`. (Si vous vous demandez ce qu'est un tenseur, [consultez d'abord cet article](https://thekevinscott.com/tensors-in-javascript/).)

#### Importation et installation

[J'ai configuré un dépôt avec les packages nécessaires](https://github.com/thekevinscott/dataset-tutorial-for-image-classification) pour vous lancer. Clonez-le et suivez les instructions du readme pour installer les packages et l'exécuter. Dans `index.js`, importez Tensorflow.js avec :

```
import * as tf from '@tensorflow/tfjs';
```

Tensorflow.js fournit une fonction pour charger un modèle pré-entraîné de manière asynchrone. Nous utiliserons cela pour charger MobileNet :

```
function loadMobilenet() {  return tf.loadModel('https://storage.googleapis.com/tfjs-models/tfjs/mobilenet_v1_0.25_224/model.json');}
```

#### Pipelines de données

Au cœur de votre modèle de machine learning se trouvent les données. Construire un pipeline solide pour traiter vos données est crucial pour le succès. Souvent, une [majorité de votre temps sera passée à travailler avec votre pipeline de données](https://thekevinscott.com/dealing-with-mnist-image-data-in-tensorflowjs/).

> Il peut être surprenant pour la communauté académique de savoir qu'une infime fraction du code dans de nombreux systèmes de machine learning fait réellement du "machine learning". Lorsque nous reconnaissons qu'un système mature pourrait finir par être (au plus) 5 % de code de machine learning et (au moins) 95 % de code de colle, la réimplémentation plutôt que la réutilisation d'une API maladroite semble être une bien meilleure stratégie. — [D. Sculley et al](https://ai.google/research/pubs/pub43146)

Il existe quelques façons courantes de structurer les données d'images :

1. Une liste de dossiers contenant des images, où le nom du dossier est l'étiquette
2. Des images dans un seul dossier, avec des images nommées par étiquette (`dog-1`, `dog-2`)
3. Des images dans un seul dossier, et un fichier csv ou autre avec un mappage de l'étiquette au fichier

Il n'y a pas de bonne façon d'organiser vos images. Choisissez le format qui a du sens pour vous et votre équipe. Cet ensemble de données est organisé par dossier.

![Image](https://cdn-media-1.freecodecamp.org/images/0*1zvnB0hbDmMB3BML.gif)

Notre pipeline de traitement des données se composera de quatre parties :

1. Charger l'image (et la transformer en tenseur)
2. Rogner l'image
3. Redimensionner l'image
4. Transformer le tenseur dans un format d'entrée approprié

#### 1. Chargement de l'image

Puisque notre modèle de machine learning attend des [tenseurs](https://thekevinscott.com/tensors-in-javascript/), la première étape consiste à charger l'image et à traduire ses données de pixels en un tenseur. Les navigateurs fournissent de nombreux outils pratiques pour charger des images et lire des pixels, et Tensorflow.js fournit une fonction pour convertir un objet `Image` en un tenseur. (Si vous êtes dans Node, vous devrez gérer cela vous-même). Cette fonction prendra une URL `src` de l'image, chargera l'image et retournera une promesse se résolvant avec un tenseur 3D de forme `[width, height, color_channels]` :

```
function loadImage(src) {  return new Promise((resolve, reject) => {    const img = new Image();    img.src = src;    img.onload = () => resolve(tf.fromPixels(img));    img.onerror = (err) => reject(err);  });}
```

#### 2. Rogner l'image

De nombreux classificateurs attendent des images carrées. Ce n'est pas une exigence stricte. Si vous construisez votre propre modèle, vous pouvez spécifier n'importe quelle résolution de taille que vous souhaitez. Cependant, les architectures CNN standard attendent que les images soient d'une **taille fixe**. Étant donné cette nécessité, de nombreux modèles pré-entraînés acceptent des carrés, afin de supporter la plus large variété de ratios d'images. (Les carrés offrent également de la flexibilité pour gérer une variété de [techniques d'augmentation de données](https://medium.com/ymedialabs-innovation/data-augmentation-techniques-in-cnn-using-tensorflow-371ae43d5be9)).

Nous avons déterminé ci-dessus que MobileNet attend des images carrées de 224x224, nous devons donc d'abord rogner nos images. Nous le faisons en coupant les bords du côté le plus long :

```
function cropImage(img) {  const width = img.shape[0];  const height = img.shape[1];  // utilisez le côté le plus court comme taille à laquelle nous allons rogner  const shorterSide = Math.min(img.shape[0], img.shape[1]);  // calculez les points de début et de fin du rognage  const startingHeight = (height - shorterSide) / 2;  const startingWidth = (width - shorterSide) / 2;  const endingHeight = startingHeight + shorterSide;  const endingWidth = startingWidth + shorterSide;  // retournez les données de l'image rognées à ces points  return img.slice([startingWidth, startingHeight, 0], [endingWidth, endingHeight, 3]);}
```

#### 3. Redimensionner l'image

Maintenant que notre image est carrée, nous pouvons la redimensionner à 224x224. Cette partie est facile : Tensorflow.js fournit une méthode de redimensionnement prête à l'emploi :

```
function resizeImage(image) {  return tf.image.resizeBilinear(image, [224, 224]);}
```

#### 4. Transformer le tenseur

Rappelons que notre modèle attend un objet d'entrée de la forme `[any, 224, 224, 3]`. Il s'agit d'un tenseur de rang 4. Cette dimension fait référence au nombre d'exemples d'entraînement. Si vous avez 10 exemples d'entraînement, cela serait `[10, 224, 224, 3]`.

Nous voulons également nos données de pixels sous forme de nombre à virgule flottante entre -1 et 1, au lieu de données entières entre 0 et 255, un processus appelé normalisation. Bien que [les réseaux de neurones soient généralement agnostiques à la taille](https://stackoverflow.com/questions/4674623/why-do-we-have-to-normalize-the-input-for-an-artificial-neural-network) des nombres entrants, l'utilisation de nombres plus petits peut aider le réseau à s'entraîner plus rapidement.

Nous pouvons construire une fonction qui étend notre tenseur et traduit les entiers en flottants avec :

```
function batchImage(image) {  // Étendez notre tenseur pour avoir une dimension supplémentaire, dont la taille est 1  const batchedImage = image.expandDims(0);  // Transformez les données de pixels en un flottant entre -1 et 1.  return batchedImage.toFloat().div(tf.scalar(127)).sub(tf.scalar(1));}
```

#### Le pipeline final

En mettant toutes les fonctions ci-dessus ensemble dans une seule fonction, nous obtenons :

```
function loadAndProcessImage(image) {  const croppedImage = cropImage(image);  const resizedImage = resizeImage(croppedImage);  const batchedImage = batchImage(resizedImage);  return batchedImage;}
```

Nous pouvons maintenant utiliser cette fonction pour tester que notre pipeline de données est configuré correctement. Nous importerons une image dont l'étiquette est connue (un tambour) et verrons si la prédiction correspond à l'étiquette attendue :

![Image](https://cdn-media-1.freecodecamp.org/images/0*JSsuxhIFdn2S4w_x.jpg)

```
import drum from './data/pretrained-model-data/drum.jpg';loadMobilenet().then(pretrainedModel => {  loadImage(drum).then(img => {    const processedImage = loadAndProcessImage(img);    const prediction = pretrainedModel.predict(processedImage);    // En raison du fonctionnement de Tensorflow.js, vous devez appeler print sur un tenseur au lieu de console.log.    prediction.print();  });});
```

Vous devriez voir quelque chose comme :

```
[[0.0000273, 5e-7, 4e-7, ..., 0.0001365, 0.0001604, 0.0003134],]
```

Si nous inspectons la forme de ce tenseur, nous verrons qu'il est `[1, 1000]`. MobileNet retourne un tenseur contenant une prédiction pour chaque catégorie, et puisque MobileNet a appris 1000 classes, nous recevons 1000 prédictions, chacune représentant la probabilité que l'image donnée appartienne à une classe donnée.

Pour obtenir une prédiction réelle, nous devons déterminer la prédiction la plus probable. Nous aplatissons le tenseur à 1 dimension et obtenons la valeur maximale, qui correspond à notre prédiction la plus confiante :

```
prediction.as1D().argMax().print();
```

Cela devrait produire :

```
541
```

Dans le dépôt, vous trouverez [une copie des définitions de classes ImageNet au format JSON](https://github.com/thekevinscott/dataset-tutorial-for-image-classification/blob/master/imagenet_labels.json). Vous pouvez importer ce fichier JSON pour traduire la prédiction numérique en une chaîne réelle :

```
import labels from './imagenet_labels.json';loadMobilenet().then(pretrainedModel => {  ...  const labelPrediction = prediction.as1D().argMax().dataSync()[0];  console.log(`    Numeric prediction is ${labelPrediction}    The predicted label is ${labels[labelPrediction]}    The actual label is drum, membranophone, tympan  `);});
```

Vous devriez voir que `541` correspond à `drum, membranophone, tympan`, qui est la catégorie de notre image. À ce stade, vous avez un pipeline fonctionnel et la capacité d'exploiter MobileNet pour prédire des images ImageNet.

Maintenant, voyons comment ajuster MobileNet sur votre ensemble de données spécifique.

#### Entraînement du modèle

![Image](https://cdn-media-1.freecodecamp.org/images/0*RchavRu2U0ozZZKl.gif)

Nous voulons construire un modèle qui prédit avec succès des **données nouvelles** — c'est-à-dire des données qu'il n'a pas vues auparavant.

Pour ce faire, vous entraînez d'abord le modèle sur des données étiquetées — des données qui ont déjà été identifiées — et vous validez les performances du modèle sur d'autres données étiquetées _qu'il n'a pas vues auparavant_.

> L'apprentissage supervisé inverse ce processus, résolvant pour m et b, étant donné un ensemble de x et de y. Dans l'apprentissage supervisé, vous commencez avec de nombreux particuliers — les données — et vous inférez l'équation générale. Et la partie apprentissage signifie que vous pouvez mettre à jour l'équation lorsque vous voyez plus de x et de y, changeant la pente de la ligne pour mieux adapter les données. L'équation n'identifie presque jamais la relation entre chaque x et y avec une précision de 100 %, mais la généralisation est puissante car plus tard vous pouvez l'utiliser pour faire de l'algèbre sur de nouvelles données. — [Kathryn Hume](https://hbr.org/2017/10/how-to-spot-a-machine-learning-opportunity-even-if-you-arent-a-data-scientist)

Lorsque vous avez entraîné le modèle ci-dessus en glissant le dossier `training`, le modèle a produit un score d'entraînement. Cela indique combien d'images le classificateur a pu apprendre à prédire avec succès dans l'ensemble d'entraînement. Le deuxième nombre qu'il a produit indiquait combien d'images il pouvait prédire qu'il _n'avait pas vues auparavant_. Ce deuxième score est celui que vous voulez optimiser (bien, vous voulez optimiser les deux, mais le dernier nombre est plus applicable aux données nouvelles).

Nous allons entraîner sur l'ensemble de données **colors**. Dans le dépôt, vous trouverez un dossier `data/colors` qui contient :

```
validation/  blue/    blue-3.png  red/    red-3.pngtraining/  blue/    blue-1.png    blue-2.png  red/    red-1.png    red-2.png
```

En construisant des modèles de machine learning, j'ai constaté que les erreurs _liées au code_ — une variable manquante, une incapacité à compiler — sont assez simples à corriger, tandis que les erreurs _d'entraînement_ — les étiquettes étaient dans le mauvais ordre, ou les images étaient rognées incorrectement — sont diaboliques à déboguer. Tester de manière exhaustive et mettre en place des cas de test de bon sens peut vous aider à économiser quelques cheveux gris.

Le dossier `data/colors` fournit une liste de couleurs rouges et bleues solides qui sont garanties d'être faciles à entraîner. Nous allons utiliser celles-ci pour entraîner notre modèle et nous assurer que notre code de machine learning apprend correctement, avant d'essayer avec un ensemble de données plus compliqué.

```
import blue1 from '../data/colors/training/blue/blue-1.png';import blue2 from '../data/colors/training/blue/blue-2.png';import blue3 from '../data/colors/validation/blue/blue-3.png';import red1 from '../data/colors/training/red/red-1.png';import red2 from '../data/colors/training/red/red-2.png';import red3 from '../data/colors/validation/red/red-3.png';const training = [  blue1,  blue2,  red1,  red2,];// les étiquettes doivent correspondre aux positions de leurs images associéesconst labels = [  'blue',  'blue',  'red',  'red',];
```

Lorsque nous avons précédemment chargé MobileNet, nous avons utilisé le modèle sans aucune modification. Lors de l'entraînement, nous voulons utiliser un sous-ensemble de ses couches — spécifiquement, nous voulons ignorer les couches finales qui produisent la classification une-sur-1000. Vous pouvez inspecter la structure d'un modèle pré-entraîné avec `.summary()` :

```
loadMobilenet().then(mobilenet => {  mobilenet.summary();});
```

Dans votre console devrait être la sortie du modèle, et vers la fin vous devriez voir quelque chose comme :

```
conv_dw_13_bn (BatchNormaliz [null,7,7,256]            1024      _________________________________________________________________conv_dw_13_relu (Activation) [null,7,7,256]            0         _________________________________________________________________conv_pw_13 (Conv2D)          [null,7,7,256]            65536     _________________________________________________________________conv_pw_13_bn (BatchNormaliz [null,7,7,256]            1024      _________________________________________________________________conv_pw_13_relu (Activation) [null,7,7,256]            0         _________________________________________________________________global_average_pooling2d_1 ( [null,256]                0         _________________________________________________________________reshape_1 (Reshape)          [null,1,1,256]            0         _________________________________________________________________dropout (Dropout)            [null,1,1,256]            0         _________________________________________________________________conv_preds (Conv2D)          [null,1,1,1000]           257000    _________________________________________________________________act_softmax (Activation)     [null,1,1,1000]           0         _________________________________________________________________reshape_2 (Reshape)          [null,1000]               0         =================================================================Total params: 475544Trainable params: 470072Non-trainable params: 5472_________________________________________________________________
```

Ce que nous cherchons est la couche finale `Activation` qui n'est pas `softmax` (`[softmax](https://en.wikipedia.org/wiki/Softmax_function)` [est l'activation](https://en.wikipedia.org/wiki/Softmax_function) utilisée pour réduire les prédictions à l'une des mille catégories). Cette couche est `conv_pw_13_relu`. Nous retournons un modèle pré-entraîné qui inclut tout jusqu'à cette couche d'activation :

```
function buildPretrainedModel() {  return loadMobilenet().then(mobilenet => {    const layer = mobilenet.getLayer('conv_pw_13_relu');    return tf.model({      inputs: mobilenet.inputs,      outputs: layer.output,    });  });}
```

Écrivons une fonction pour parcourir un tableau d'images et retourner une promesse qui se résout lorsqu'elles se chargent.

```
function loadImages(images, pretrainedModel) {  let promise = Promise.resolve();  for (let i = 0; i < images.length; i++) {    const image = images[i];    promise = promise.then(data => {      return loadImage(image).then(loadedImage => {        // Notez l'utilisation de `tf.tidy` et `.dispose()`. Ce sont deux fonctions de gestion de la mémoire        // que Tensorflow.js expose.        // https://js.tensorflow.org/tutorials/core-concepts.html        //        // La gestion de la mémoire est cruciale pour construire un modèle de machine learning performant        // dans un navigateur.        return tf.tidy(() => {          const processedImage = loadAndProcessImage(loadedImage, pretrainedModel);          if (data) {            const newData = data.concat(processedImage);            data.dispose();            return newData;          }          return tf.keep(processedImage);        });      });    });  }  return promise;}
```

Nous construisons une promesse séquentielle qui itère sur chaque image et la traite. Alternativement, vous pouvez utiliser `Promise.all` pour charger les images en parallèle, mais soyez conscient des performances de l'interface utilisateur si vous faites cela.

En mettant ces fonctions ensemble, nous obtenons :

```
buildPretrainedModel().then(pretrainedModel => {  loadImages(training, pretrainedModel).then(xs => {    xs.print();  })});
```

Appeler vos données "x" et "y" est [une convention dans le monde du machine learning](https://datascience.stackexchange.com/questions/17598/why-are-variables-of-train-and-test-data-defined-using-the-capital-letter-in-py), héritée de ses origines mathématiques. Vous pouvez appeler vos variables comme vous le souhaitez, mais je trouve utile de respecter les conventions lorsque c'est possible.

#### Étiquettes

Ensuite, vous devrez convertir vos étiquettes en forme numérique. Cependant, ce n'est pas aussi simple que d'assigner un nombre à chaque catégorie. Pour démontrer, disons que vous classez trois catégories de fruits :

```
raspberry - 0blueberry - 1strawberry - 2
```

Dénoter des nombres comme ceci peut impliquer une relation là où elle n'existe pas, puisque ces nombres sont considérés comme des valeurs _ordinales_. Ils impliquent un certain ordre dans les données. Les conséquences réelles de cela pourraient être que le réseau décide qu'une myrtille est quelque chose qui est à mi-chemin entre une framboise et une fraise, ou qu'une fraise est la "meilleure" des baies.

![Image](https://cdn-media-1.freecodecamp.org/images/0*DTD_3Ji4G-O6Go8t.gif)

Pour éviter ces hypothèses incorrectes, nous utilisons un processus appelé "one hot encoding", résultant en des données qui ressemblent à :

```
raspberry  - [1, 0, 0]blueberry  - [0, 1, 0]strawberry - [0, 0, 1]
```

(Deux excellents articles qui approfondissent le one hot encoding sont [ici](https://hackernoon.com/what-is-one-hot-encoding-why-and-when-do-you-have-to-use-it-e3c6186d008f) et [ici](https://machinelearningmastery.com/why-one-hot-encode-data-in-machine-learning/).) Nous pouvons exploiter les fonctions intégrées `oneHot` de Tensorflow.js pour traduire nos étiquettes :

```
function oneHot(labelIndex, classLength) {  return tf.tidy(() => tf.oneHot(tf.tensor1d([labelIndex]).toInt(), classLength));};
```

Cette fonction prend un nombre particulier (`labelIndex`, un nombre qui correspond à une étiquette) et le traduit en un encodage one-hot, étant donné un certain nombre de classes (`classLength`). Nous pouvons utiliser la fonction avec le morceau de code suivant, qui construit d'abord un mappage de nombres-vers-étiquettes à partir du tableau entrant d'étiquettes, puis construit un tenseur contenant ces étiquettes encodées en one-hot :

```
function getLabelsAsObject(labels) {  let labelObject = {};  for (let i = 0; i < labels.length; i++) {    const label = labels[i];    if (labelObject[label] === undefined) {      // ne l'assignez que si nous ne l'avons pas vu auparavant      labelObject[label] = Object.keys(labelObject).length;    }  }  return labelObject;}function addLabels(labels) {  return tf.tidy(() => {    const classes = getLabelsAsObject(labels);    const classLength = Object.keys(classes).length;    let ys;    for (let i = 0; i < labels.length; i++) {      const label = labels[i];      const labelIndex = classes[label];      const y = oneHot(labelIndex, classLength);      if (i === 0) {        ys = y;      } else {        ys = ys.concat(y, 0);      }    }    return ys;  });};
```

Maintenant que nous avons nos données, nous pouvons construire notre modèle. Vous êtes libre d'innover à ce stade, mais je trouve que construire sur les conventions des autres tend à produire un modèle suffisamment bon dans la plupart des cas. Nous nous tournerons vers l'[exemple Webcam Tensorflow.js](https://github.com/tensorflow/tfjs-examples/tree/master/webcam-transfer-learning) pour un modèle de transfer learning bien structuré que nous réutiliserons largement mot à mot.

Les choses qui valent la peine d'être mises en évidence sont que la première couche correspond à la forme de sortie de notre modèle pré-entraîné, et la couche finale `softmax` correspond au nombre d'étiquettes, défini comme `numberOfClasses`. 100 unités sur la deuxième couche est arbitraire, et vous pouvez absolument expérimenter en changeant ce nombre pour votre cas d'utilisation particulier.

```
function getModel(numberOfClasses) {  const model = tf.sequential({    layers: [      tf.layers.flatten({inputShape: [7, 7, 256]}),      tf.layers.dense({        units: 100,        activation: 'relu',        kernelInitializer: 'varianceScaling',        useBias: true      }),      tf.layers.dense({        units: numberOfClasses,        kernelInitializer: 'varianceScaling',        useBias: false,        activation: 'softmax'      })    ],  });  model.compile({    optimizer: tf.train.adam(0.0001),    loss: 'categoricalCrossentropy',    metrics: ['accuracy'],  });  return model;}
```

Voici divers liens si vous souhaitez approfondir un peu plus les parties internes des réseaux de neurones :

* `[tf.sequential](https://js.tensorflow.org/api/0.12.0/#sequential)`
* `[tf.layers.flatten](https://js.tensorflow.org/api/0.12.0/#layers.flatten)`
* `[tf.layers.dense](https://js.tensorflow.org/api/0.12.0/#layers.dense)`
* [l'activation `relu`](https://www.kaggle.com/dansbecker/rectified-linear-units-relu-in-deep-learning)
* `[adam](https://machinelearningmastery.com/adam-optimization-algorithm-for-deep-learning/)` [optimizer](https://machinelearningmastery.com/adam-optimization-algorithm-for-deep-learning/)
* `[categoricalCrossentropy](https://keras.io/losses/)` [loss](https://keras.io/losses/)

L'étape finale consiste à entraîner réellement le modèle, ce que nous faisons en appelant `.fit()` sur le modèle. Nous mélangeons nos images d'entraînement afin que le modèle n'apprenne pas à dépendre de l'ordre des données d'entraînement entrantes, et nous entraînons pendant 20 époques. (Une époque désigne un cycle à travers l'ensemble de votre ensemble d'entraînement.)

```
function makePrediction(pretrainedModel, image, expectedLabel) {  loadImage(image).then(loadedImage => {    return loadAndProcessImage(loadedImage, pretrainedModel);  }).then(loadedImage => {    console.log('Expected Label', expectedLabel);    console.log('Predicted Label', predict(model, loadedImage));    loadedImage.dispose();  });}buildPretrainedModel().then(pretrainedModel => {  loadImages(training, pretrainedModel).then(xs => {    const ys = addLabels(labels);    const model = getModel(2);    model.fit(xs, ys, {      epochs: 20,      shuffle: true,    }).then(history => {      // faire des prédictions      makePrediction(pretrainedModel, blue3, "0");      makePrediction(pretrainedModel, red3, "1");    });  });});
```

Combien d'époques devez-vous exécuter ?

> Malheureusement, il n'y a pas de bonne réponse à cette question. La réponse est différente pour différents ensembles de données, mais vous pouvez dire que le nombre d'époques est lié à la diversité de vos données — [Sagar Sharma](https://towardsdatascience.com/epoch-vs-iterations-vs-batch-size-4dfb9c7ce9c9)

En gros, vous pouvez l'exécuter jusqu'à ce qu'il soit bon, ou jusqu'à ce qu'il soit clair qu'il ne fonctionne pas, ou jusqu'à ce que vous manquez de temps.

Vous devriez voir une précision de 100 % dans l'entraînement ci-dessus. Essayez de modifier le code pour qu'il fonctionne sur l'[ensemble de données Pexels](https://github.com/thekevinscott/dataset-tutorial-for-image-classification/tree/master/data/pexel-images). J'ai constaté dans mes tests que mes chiffres de précision baissent un peu avec cet ensemble de données plus complexe.

#### Réflexions finales

En résumé, il est bon marché et rapide de construire sur un modèle pré-entraîné et d'obtenir un classificateur qui est assez précis.

Lors du codage de l'apprentissage automatique, soyez prudent de tester votre code à chaque section du processus et validez avec des données que vous savez fonctionner. Il est payant de mettre en place un pipeline de données stable et réutilisable tôt dans votre processus, puisque tant de votre temps est passé à travailler avec vos données.

Enfin, si vous êtes intéressé à en apprendre davantage sur l'entraînement des CNN à partir de zéro, un excellent point de départ est les [tutoriels de Fast.ai](https://fastai.com) pour les hackers. Il est construit en Python mais vous pouvez traduire les idées en Node.js si vous voulez rester en Javascript.

Publié à l'origine sur [https://thekevinscott.com](https://thekevinscott.com/image-classification-with-javascript)