---
title: Comment gérer les données d'image MNIST dans Tensorflow.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-13T19:37:39.000Z'
originalURL: https://freecodecamp.org/news/how-to-deal-with-mnist-image-data-in-tensorflow-js-169a2d6941dd
coverImage: https://cdn-media-1.freecodecamp.org/images/0*XDXg44q30kAtG4S8.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Machine Learning
  slug: machine-learning
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: TensorFlow
  slug: tensorflow
seo_title: Comment gérer les données d'image MNIST dans Tensorflow.js
seo_desc: 'By Kevin Scott


  There’s the joke that 80 percent of data science is cleaning the data and 20 percent
  is complaining about cleaning the data … data cleaning is a much higher proportion
  of data science than an outsider would expect. Actually training m...'
---

Par Kevin Scott

> Il y a une blague selon laquelle 80 pour cent de la science des données consiste à nettoyer les données et 20 pour cent à se plaindre de nettoyer les données... le nettoyage des données représente une proportion beaucoup plus élevée de la science des données que ce qu'un outsider pourrait imaginer. L'entraînement réel des modèles est généralement une proportion relativement faible (moins de 10 pour cent) de ce qu'un apprenant automatique ou un scientifique des données fait. 
>   
>   [Anthony Goldbloom, PDG de Kaggle](https://www.theverge.com/2017/11/1/16589246/machine-learning-data-science-dirty-data-kaggle-survey-2017)

Manipuler les données est une étape cruciale pour tout problème d'apprentissage automatique. Cet article prendra l'exemple [MNIST pour Tensorflow.js (0.11.1)](https://github.com/tensorflow/tfjs-examples/blob/master/mnist/data.js), et passera en revue le code qui gère le chargement des données ligne par ligne.

### Exemple MNIST

```
18 import * as tf from '@tensorflow/tfjs';1920 const IMAGE_SIZE = 784;21 const NUM_CLASSES = 10;22 const NUM_DATASET_ELEMENTS = 65000;2324 const NUM_TRAIN_ELEMENTS = 55000;25 const NUM_TEST_ELEMENTS = NUM_DATASET_ELEMENTS - NUM_TRAIN_ELEMENTS;2627 const MNIST_IMAGES_SPRITE_PATH =28     'https://storage.googleapis.com/learnjs-data/model-builder/mnist_images.png';29 const MNIST_LABELS_PATH =30     'https://storage.googleapis.com/learnjs-data/model-builder/mnist_labels_uint8';`
```

Tout d'abord, le code importe Tensorflow [(assurez-vous de transpiler votre code !)](https://thekevinscott.com/tensorflowjs-hello-world/), et établit certaines constantes, y compris :

* `IMAGE_SIZE`  la taille d'une image (largeur et hauteur de 28x28 = 784)
* `NUM_CLASSES`  nombre de catégories d'étiquettes (un nombre peut être de 0-9, donc il y a 10 classes)
* `NUM_DATASET_ELEMENTS`  nombre total d'images (65 000)
* `NUM_TRAIN_ELEMENTS`  nombre d'images d'entraînement (55 000)
* `NUM_TEST_ELEMENTS`  nombre d'images de test (10 000, c'est-à-dire le reste)
* `MNIST_IMAGES_SPRITE_PATH` & `MNIST_LABELS_PATH`  chemins vers les images et les étiquettes

Les images sont concaténées en une seule image géante qui ressemble à :

![Image](https://cdn-media-1.freecodecamp.org/images/0*zPqagVx10lTbl-c5.png)

#### `MNISTData`

Ensuite, à partir de la ligne 38, nous avons `MnistData`, une classe qui expose les fonctions suivantes :

* `load`  responsable du chargement asynchrone de l'image et des données d'étiquetage
* `nextTrainBatch`  charge le prochain lot d'entraînement
* `nextTestBatch`  charge le prochain lot de test
* `nextBatch`  une fonction générique pour retourner le prochain lot, selon qu'il se trouve dans l'ensemble d'entraînement ou de test

Pour les besoins de ce guide, cet article ne traitera que de la fonction `load`.

#### `load`

```
44 async load() {45   // Faire une requête pour l'image sprited MNIST.46   const img = new Image();47   const canvas = document.createElement('canvas');48   const ctx = canvas.getContext('2d');
```

`async` [est une fonctionnalité relativement nouvelle du langage JavaScript](https://thekevinscott.com/tensorflowjs-hello-world/#async-and-await) pour laquelle vous aurez besoin d'un transpileur.

L'objet `Image` est une fonction DOM native qui représente une image en mémoire. Il fournit des rappels pour lorsque l'image est chargée, ainsi qu'un accès aux attributs de l'image. `canvas` est un autre élément DOM qui permet un accès facile aux tableaux de pixels et au traitement via le `context`.

Étant donné que ces deux éléments sont des éléments DOM, si vous travaillez dans Node.js (ou un Web Worker), vous n'aurez pas accès à ces éléments. [Pour une approche alternative, voir ci-dessous](https://medium.com/p/169a2d6941dd#636b).

#### `imgRequest`

```
49 const imgRequest = new Promise((resolve, reject) => {50   img.crossOrigin = '';51   img.onload = () => {52     img.width = img.naturalWidth;53     img.height = img.naturalHeight;
```

Le code initialise une nouvelle promesse qui sera résolue une fois l'image chargée avec succès. **Cet exemple ne gère pas explicitement l'état d'erreur.**

`crossOrigin` est un attribut `img` qui permet le chargement d'images entre domaines et contourne les problèmes CORS (cross-origin resource sharing) lors de l'interaction avec le DOM. `naturalWidth` et `naturalHeight` font référence aux dimensions originales de l'image chargée et servent à garantir que la taille de l'image est correcte lors de l'exécution des calculs.

```
55     const datasetBytesBuffer =56     new ArrayBuffer(NUM_DATASET_ELEMENTS * IMAGE_SIZE * 4);5758     const chunkSize = 5000;59     canvas.width = img.width;60     canvas.height = chunkSize;
```

Le code initialise un nouveau buffer pour contenir chaque pixel de chaque image. Il multiplie le nombre total d'images par la taille de chaque image par le nombre de canaux (4).

Je **crois** que `chunkSize` est utilisé pour empêcher l'interface utilisateur de charger trop de données en mémoire à la fois, bien que je n'en sois pas sûr à 100 %.

```
62     for (let i = 0; i < NUM_DATASET_ELEMENTS / chunkSize; i++) {63       const datasetBytesView = new Float32Array(64         datasetBytesBuffer, i * IMAGE_SIZE * chunkSize * 4,65         IMAGE_SIZE * chunkSize);66       ctx.drawImage(67         img, 0, i * chunkSize, img.width, chunkSize, 0, 0, img.width,68         chunkSize);6970       const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
```

Ce code parcourt chaque image dans le sprite et initialise un nouveau `TypedArray` pour cette itération. Ensuite, l'image de contexte obtient un morceau de l'image dessiné. Enfin, cette image dessinée est transformée en données d'image en utilisant la fonction `[getImageData](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/getImageData)` du contexte, qui retourne un objet représentant les données de pixels sous-jacentes.

```
72       for (let j = 0; j < imageData.data.length / 4; j++) {73         // Tous les canaux contiennent une valeur égale puisque l'image est en niveaux de gris, donc74         // il suffit de lire le canal rouge.75         datasetBytesView[j] = imageData.data[j * 4] / 255;76       }77     }
```

Nous parcourons les pixels et divisons par 255 (la valeur maximale possible d'un pixel) pour limiter les valeurs entre 0 et 1. Seul le canal rouge est nécessaire, puisque c'est une image en niveaux de gris.

```
78     this.datasetImages = new Float32Array(datasetBytesBuffer);7980     resolve();81   };82   img.src = MNIST_IMAGES_SPRITE_PATH;83 });
```

Cette ligne prend le buffer, le recaste en un nouveau `TypedArray` qui contient nos données de pixels, puis résout la Promesse. La dernière ligne (définissant le `src`) commence réellement à charger l'image, ce qui démarre la fonction.

Une chose qui m'a d'abord dérouté était le comportement de `TypedArray` par rapport à son buffer de données sous-jacent. Vous avez peut-être remarqué que `datasetBytesView` est défini dans la boucle, mais n'est jamais retourné.

Sous le capot, `datasetBytesView` fait référence au buffer `datasetBytesBuffer` (avec lequel il est initialisé). Lorsque le code met à jour les données de pixels, il modifie indirectement les valeurs du buffer lui-même, qui à son tour est recasté en un nouveau `Float32Array` à la ligne 78.

#### Récupération des données d'image en dehors du DOM

Si vous êtes dans le DOM, vous devriez utiliser le DOM. Le navigateur (via `canvas`) se charge de déterminer le format des images et de traduire les données de buffer en pixels. Mais si vous travaillez en dehors du DOM (par exemple, dans Node.js, ou un Web Worker), vous aurez besoin d'une approche alternative.

`fetch` fournit un mécanisme, `response.arrayBuffer`, qui vous donne accès au buffer sous-jacent d'un fichier. Nous pouvons utiliser cela pour lire les octets manuellement, en évitant complètement le DOM. Voici une approche alternative pour écrire le code ci-dessus (ce code nécessite `fetch`, qui peut être polyfillé dans Node avec quelque chose comme `[isomorphic-fetch](https://github.com/matthew-andrews/isomorphic-fetch)`) :

```
const imgRequest = fetch(MNIST_IMAGES_SPRITE_PATH).then(resp => resp.arrayBuffer()).then(buffer => {  return new Promise(resolve => {    const reader = new PNGReader(buffer);    return reader.parse((err, png) => {      const pixels = Float32Array.from(png.pixels).map(pixel => {        return pixel / 255;      });      this.datasetImages = pixels;      resolve();    });  });});
```

Cela retourne un buffer de tableau pour l'image particulière. En écrivant cela, j'ai d'abord tenté de parser le buffer entrant moi-même, ce que je ne recommande pas. (Si vous êtes intéressé à faire cela, [voici quelques informations sur la façon de lire un buffer de tableau pour un png](http://www.libpng.org/pub/png/spec/1.2/PNG-Structure.html).) Au lieu de cela, j'ai choisi [d'utiliser `pngjs`](https://github.com/arian/pngjs), qui gère le parsing `png` pour vous. Lorsque vous traitez avec d'autres formats d'image, vous devrez déterminer vous-même les fonctions de parsing.

### Juste effleurer la surface

Comprendre la manipulation des données est un composant crucial de l'apprentissage automatique en JavaScript. En comprenant nos cas d'utilisation et nos exigences, nous pouvons utiliser quelques fonctions clés pour formater élégamment nos données correctement pour nos besoins.

L'équipe Tensorflow.js modifie continuellement l'API de données sous-jacente dans Tensorflow.js. Cela peut aider à répondre à plus de nos besoins à mesure que l'API évolue. Cela signifie également qu'il est utile de rester informé des [développements de l'API](https://github.com/tensorflow/tfjs) alors que Tensorflow.js continue de croître et de s'améliorer.

Publié à l'origine sur [thekevinscott.com](https://thekevinscott.com/dealing-with-mnist-image-data-in-tensorflowjs)

Remerciements spéciaux à [Ari Zilnik](https://www.freecodecamp.org/news/how-to-deal-with-mnist-image-data-in-tensorflow-js-169a2d6941dd/undefined).