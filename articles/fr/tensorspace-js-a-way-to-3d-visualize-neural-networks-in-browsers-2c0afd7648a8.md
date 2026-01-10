---
title: Présentation de TensorSpace.js — Un moyen de visualiser en 3D les réseaux de
  neurones dans les navigateurs
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-12T13:31:01.000Z'
originalURL: https://freecodecamp.org/news/tensorspace-js-a-way-to-3d-visualize-neural-networks-in-browsers-2c0afd7648a8
coverImage: https://cdn-media-1.freecodecamp.org/images/1*uhTVA1yCPB-M6s0MPiaBtg.png
tags:
- name: data visualization
  slug: data-visualization
- name: Deep Learning
  slug: deep-learning
- name: JavaScript
  slug: javascript
- name: Machine Learning
  slug: machine-learning
- name: 'tech '
  slug: tech
seo_title: Présentation de TensorSpace.js — Un moyen de visualiser en 3D les réseaux
  de neurones dans les navigateurs
seo_desc: 'By Chenhua Zhu

  Neural networks were always something high-level, unreachable and mysterious before
  I took my first deep learning class. To me they were just magic: neural network
  applications could complete tasks on object detection, image classifica...'
---

Par Chenhua Zhu

Les réseaux de neurones étaient toujours quelque chose de haut niveau, inaccessible et mystérieux avant que je ne suive mon premier cours de deep learning. Pour moi, ils étaient juste de la magie : les applications de réseaux de neurones pouvaient accomplir des tâches de détection d'objets, de classification d'images et même de prédiction de données dans notre vie quotidienne.

« Qu'est-ce que le modèle calcule ? » « Pourquoi devrions-nous utiliser ce réseau spécifique pour cette tâche ? » « Comment les autres ont-ils pu imaginer une structure comme celle-ci ? »

Peut-être avez-vous les mêmes questions que moi. Mes amis et moi avons constaté que parfois, il est vraiment difficile de comprendre et d'expliquer les réseaux de neurones. Ensuite, nous avons eu quelques idées :

_Pourquoi ne pas visualiser un réseau de neurones ?_   
_Et si c'était un modèle 3D ?_   
_Il peut être interactif !_

Puisqu'aucun outil de ce type n'existait que nous puissions trouver, nous nous sommes dit, pourquoi ne pas en créer un nous-mêmes ? Après 6 mois, je suis fier de présenter notre travail : [TensorSpace.js](https://github.com/tensorspace-team/tensorspace).

### Qu'est-ce que TensorSpace.js ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*_iuD-XPoKrBKG2TyftR8zA.gif)
_**Fig. 1** — Modèle LeNet interactif créé par TensorSpace.js_

> TensorSpace.js est un framework de visualisation 3D de réseaux de neurones construit avec TensorFlow.js, Three.js et Tween.js.

Puisque nous voulions pouvoir présenter facilement les modèles dans la plupart des navigateurs web, nous avons choisi JavaScript pour implémenter le framework.

D'après la Fig. 1 ci-dessus, vous pouvez facilement consulter la structure du modèle : chaque « cube » représente un objet « couche » dans le réseau de neurones.

Ensuite, vous pouvez interagir avec le modèle en cliquant, en faisant glisser et en défilant. Différents angles peuvent offrir différents points de vue du modèle. Certains objets sont extensibles, ce qui vous permet d'observer plus de détails.

De plus, nous avons conçu une architecture hybride pour TensorSpace.js afin de supporter différentes bibliothèques, telles que TensorFlow, Keras et TensorFlow.js (d'autres à venir dans le futur).

TensorSpace.js peut non seulement montrer la structure de base du modèle, mais aussi présenter les processus d'abstractions de caractéristiques internes, de manipulations de données intermédiaires et de générations d'inférences finales.

En résumé, TensorSpace.js est :

* **Interactif** — Utilise une API de type Keras pour construire des modèles interactifs dans les navigateurs.
* **Intuitif** — Visualise les informations des inférences intermédiaires.
* **Intégratif** — Supporte les modèles pré-entraînés de TensorFlow, Keras et TensorFlow.js.

### Comment fonctionne TensorSpace.js ?

La partie suivante introduit comment construire un modèle TensorSpace. J'utilise un modèle de reconnaissance d'écriture manuscrite LeNet comme exemple. Vous pouvez trouver tous les fichiers d'exemple dans le dépôt ici : [TensorSpace — HelloWorld](http://repo).

![Image](https://cdn-media-1.freecodecamp.org/images/1*sWXFqWqXOwlpabUrW5dGDg.png)
_**Fig. 2** — Flux de travail pour présenter un modèle TensorSpace_

Le flux de travail général consiste à créer ou à pré-traiter un modèle pré-entraîné avec plusieurs sorties intermédiaires. Ensuite, en fonction de la structure du réseau de neurones, nous pouvons construire un modèle TensorSpace. Enfin, nous chargeons et initialisons le modèle qui peut accepter des données d'entrée pour les inférences.

Après avoir correctement [installé TensorSpace.js](https://tensorspace.org/html/docs/startInstall.html) et correctement [pré-traité les modèles pré-entraînés](https://tensorspace.org/html/docs/preIntro.html), nous pouvons facilement créer un modèle TensorSpace de reconnaissance d'écriture manuscrite LeNet. Pour plus de commodité, nous utilisons le [modèle compatible TensorSpace pré-traité](https://github.com/tensorspace-team/tensorspace/tree/master/examples/helloworld/model) et un [fichier extrait](https://github.com/tensorspace-team/tensorspace/blob/master/examples/helloworld/data/5.json) qui est un « 5 » manuscrit comme entrée du modèle.

```
let container = document.getElementById( "container" );
```

```
// Créer un modèle séquentiel
let model = new TSP.models.Sequential( container );
```

```
// Ajouter les couches LeNet
model.add( new TSP.layers.GreyscaleInput({ shape: [28, 28, 1] }) );
model.add( new TSP.layers.Padding2d({ padding: [2, 2] }) );
model.add( new TSP.layers.Conv2d({ kernelSize: 5, filters: 6, strides: 1 }) );
model.add( new TSP.layers.Pooling2d({ poolSize: [2, 2], strides: [2, 2] }) );
model.add( new TSP.layers.Conv2d({ kernelSize: 5, filters: 16, strides: 1 }) );
model.add( new TSP.layers.Pooling2d({ poolSize: [2, 2], strides: [2, 2] }) );
model.add( new TSP.layers.Dense({ units: 120 }) );
model.add( new TSP.layers.Dense({ units: 84 }) );
model.add( new TSP.layers.Output1d({    units: 10,    outputs: ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]}) );
```

```
// Charger le modèle pré-traité
model.load({    type: "tfjs",    url: './lenetModel/mnist.json'});
```

```
// Initialiser le modèle dans le navigateur
model.init(function() {    // Prédire l'entrée "5"    model.predict( image_5 ); });
```

C'est tout !

Vous pouvez l'essayer dans le CodePen :

[_Voir dans CodePen_](https://codepen.io/syt123450/pen/667a7943b0f23727790ca38c93389689/)_._

Il est facile de construire d'autres modèles pré-traités de la même manière. Si vous êtes intéressé, veuillez consulter notre [playground](https://tensorspace.org/html/playground/index.html) pour plus de démonstrations intéressantes, telles que Yolov2-tiny, ACGAN et ResNet-50.

### Quand devriez-vous l'utiliser ?

Si vous souhaitez présenter votre modèle à d'autres, expliquer certaines caractéristiques détaillées du modèle ou construire une démonstration à partir de zéro, je pense que TensorSpace peut être un bon outil pour décrire le modèle de manière intuitive et claire. C'est amusant d'interagir et d'explorer le modèle que vous venez de construire.

### **Conclusion**

Mon équipe et moi espérons que TensorSpace peut, au moins, vous aider à faire un petit pas en avant dans la manière dont vous visualisez les réseaux de neurones. Nous croyons que cela attirera plus de personnes dans ce domaine.

Pour plus d'informations sur TensorSpace.js, veuillez consulter :

* Site officiel : [TensorSpace.org](https://tensorspace.org/)
* Dépôt GitHub : [TensorSpace-Team/TensorSpace](https://github.com/tensorspace-team/tensorspace).