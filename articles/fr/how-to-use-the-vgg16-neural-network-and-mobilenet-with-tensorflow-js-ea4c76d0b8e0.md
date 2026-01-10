---
title: Comment utiliser le réseau de neurones VGG16 et MobileNet avec TensorFlow.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-10T18:26:09.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-the-vgg16-neural-network-and-mobilenet-with-tensorflow-js-ea4c76d0b8e0
coverImage: https://cdn-media-1.freecodecamp.org/images/0*UM0vZhOyk06pdmVT
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Deep Learning
  slug: deep-learning
- name: JavaScript
  slug: javascript
- name: technology
  slug: technology
- name: TensorFlow
  slug: tensorflow
seo_title: Comment utiliser le réseau de neurones VGG16 et MobileNet avec TensorFlow.js
seo_desc: 'By ADL

  In this article, we will build a deep neural network that can recognize images with
  a high accuracy on the Client side using JavaScript & TensorFlow.js. I’ll explain
  the techniques used throughout the process as we go along.We will be using VG...'
---

Par ADL

Dans cet article, nous allons construire un réseau de neurones profond capable de reconnaître des images avec une grande précision côté client en utilisant JavaScript et TensorFlow.js. Je vais expliquer les techniques utilisées tout au long du processus.

Nous utiliserons VGG16 et MobileNet pour cette démonstration.

Si vous avez besoin d'un rappel rapide sur TensorFlow.js, lisez [cet](https://medium.freecodecamp.org/get-to-know-tensorflow-js-in-7-minutes-afcd0dfd3d2f) article.

Voici une capture d'écran de ce à quoi ressemblera l'application web finale :

![Image](https://cdn-media-1.freecodecamp.org/images/1*v7x4TywHpUsEO8yQ4eu8xA.png)
_Application Web Finale_

Pour commencer, nous allons créer un dossier **(VGG16_Keras_To_TensorflowJS)** avec deux sous-dossiers : **localserver** et **static**. Le dossier **localserver** contiendra tout le code serveur **NodeJS**, et le dossier **static** contiendra tout le code CSS, HTML et JavaScript.

![Image](https://cdn-media-1.freecodecamp.org/images/1*_TUuwX9jKmLx8O6NmHD7bA.png)
_Capture d'écran montrant la structure des dossiers_

> _Remarque : vous pouvez nommer les dossiers et fichiers comme vous le souhaitez._

### Configuration du Serveur

Nous allons créer manuellement un fichier **package.json** avec le code suivant :

```
{
```

```
"name": "tensorflowjs",
```

```
"version": "1.0.0",
```

```
"dependencies": {
```

```
"express": "latest"
```

```
}}
```

Le fichier **package.json** garde une trace de tous les packages tiers que nous utiliserons dans ce projet. Après avoir sauvegardé le fichier **package.json**, nous ouvrirons la ligne de commande et naviguerons vers le dossier **localserver**. Ensuite, nous exécuterons la commande suivante :

```
npm install
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*Mf-8wFjGxWba4k9wN_ArUw.png)
_Ligne de commande pour MacOS_

Après cela, NPM s'exécutera et s'assurera que tous les packages requis mentionnés dans **package.json** sont installés et prêts à être utilisés. Vous observerez un dossier **node_modules** dans le dossier **localserver**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*yhJuZPtxeGCp1xgZTtA89Q.png)

Nous allons créer un fichier **server.js** avec le code suivant :

**server.js** contient le code NodeJS qui permet d'héberger le serveur local qui exécutera notre application web.

### Configuration du Client

Ensuite, nous allons créer un fichier **predict_with_tfjs.html**. Voici le code :

Une fois le code HTML terminé, nous allons créer un fichier JavaScript et l'appeler **predict.js**. Voici le code :

### Configuration du Modèle

Une fois le code côté client et serveur terminé, nous avons maintenant besoin d'un modèle DL/ML pour prédire les images. Nous exportons le modèle entraîné (VGG16 et MobileNet) de Keras vers TensorFlow.js. Enregistrez la sortie dans des dossiers appelés VGG et MobileNet, respectivement, à l'intérieur du dossier static.

![Image](https://cdn-media-1.freecodecamp.org/images/1*VUIUWALn0J5V9vRZc8yerA.png)
_Capture d'écran pour Python_

### Définition des Classes

Nous allons garder **imagenet_classes.js** à l'intérieur du dossier **static**. Ce fichier contient une liste de toutes les classes ImageNet. _Vous pouvez télécharger ce fichier depuis [ici](https://github.com/ADLsourceCode/TensorflowJS/blob/master/VGG16_Keras_To_TensorflowJS/static/imagenet_classes.js)._

### Test du Code

Après avoir terminé toute la configuration, nous allons ouvrir la ligne de commande et naviguer vers le dossier **localserver** et exécuter :

```
node server.js
```

Nous devrions voir la sortie suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/1*K7jbNlFYiRdnITT06kBFrg.png)

Après la mise en œuvre réussie du code côté serveur, nous pouvons maintenant aller dans le navigateur et ouvrir [**http://localhost:8080/predict_with_tfjs.html**](http://localhost:8080/predict_with_tfjs.html).

Si le code côté client est sans bug, l'application démarrera. Ensuite, vous pouvez sélectionner un modèle différent (VGG16 et MobileNet) dans la boîte de sélection et effectuer la prédiction.

#### **Dépôt GitHub pour le projet :**

[**ADLsourceCode/TensorflowJS**](https://github.com/ADLsourceCode/TensorflowJS/tree/master/VGG16_Keras_To_TensorflowJS)
[_GitHub est l'endroit où les gens construisent des logiciels. Plus de 28 millions de personnes utilisent GitHub pour découvrir, fork et contribuer à plus degithub.com](https://github.com/ADLsourceCode/TensorflowJS/tree/master/VGG16_Keras_To_TensorflowJS)

**Vous pouvez regarder l'explication complète du code et la mise en œuvre dans la vidéo ci-dessous :**

> Mon prochain article couvrira **l'analyse des séries temporelles financières** en utilisant Tensorflow.js[Restez à l'écoute](https://goo.gl/u72j6u).

**Bonne chance ! ?**

Si vous avez aimé mon article, **veuillez cliquer sur le ? ci-dessous** et me suivre sur **Medium** et :

![Image](https://cdn-media-1.freecodecamp.org/images/1*z8B3R6kZjTkMKPv3MnUYxg.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*-etmF1WRWkvWO6cSol7f1w.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*7DWddirTA0TDNoAL34xjag.png)

Si vous avez des questions, n'hésitez pas à me le faire savoir dans les commentaires ci-dessous ou sur [**Twitter**](https://twitter.com/I_AM_ADL). Abonnez-vous à ma chaîne YouTube pour plus de vidéos tech : [**ADL**](https://goo.gl/u72j6u).