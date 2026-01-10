---
title: 'Un guide de la détection d''objets avec Fritz : Créez une application de surveillance
  d''animaux de compagnie sur Android avec le machine learning'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-30T18:03:22.000Z'
originalURL: https://freecodecamp.org/news/a-guide-to-object-detection-with-fritz-build-a-pet-monitoring-app-in-android-with-machine-learning-a8ed500978e5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*m7zfN9KePEAdXApefron6Q.png
tags:
- name: Android
  slug: android
- name: app development
  slug: app-development
- name: Machine Learning
  slug: machine-learning
- name: mobile app development
  slug: mobile-app-development
- name: technology
  slug: technology
seo_title: 'Un guide de la détection d''objets avec Fritz : Créez une application
  de surveillance d''animaux de compagnie sur Android avec le machine learning'
seo_desc: 'By Eric Hsiao

  Whether it is detecting plant damage for farmers, tracking vehicles on the road,
  or monitoring your pets — the applications for object detection are endless. With
  the rise of mobile frameworks like TensorFlow Lite and Core ML, more and ...'
---

Par Eric Hsiao

Qu'il s'agisse de [détecter les dommages aux plantes pour les agriculteurs](https://heartbeat.fritz.ai/community-spotlight-nuru-a-mobile-app-by-plantvillage-to-detect-crop-disease-in-africa-28d142bf63d5), de suivre les véhicules sur la route ou de surveiller vos animaux de compagnie — les applications de la [**détection d'objets**](https://fritz.ai/features/object-detection.html) sont infinies. Avec l'essor des frameworks mobiles comme **TensorFlow Lite** et **Core ML**, de plus en plus d'applications mobiles exploitent la puissance du machine learning pour créer des fonctionnalités qui nous laissent sans voix.

#### _Alors, qu'est-ce que la détection d'objets exactement ?_

En anglais simple, la détection d'objets _identifie et localise des éléments spécifiques dans une image ou une vidéo en direct avec une boîte de délimitation._

![Image](https://cdn-media-1.freecodecamp.org/images/1*134aK_z6iXpT_Yz6WoqwaQ.png)
_Celui du milieu est un caniche déguisé en Toothless pour Halloween_

Mais créer des fonctionnalités alimentées par le machine learning n'est pas facile. De nombreuses équipes d'ingénierie ne peuvent pas justifier le temps et les ressources nécessaires. Vous avez besoin de l'expertise interne appropriée pour collecter des données, entraîner un modèle et itérer sur les performances et la précision. Compréhensiblement, sous la pression des équipes produit pour livrer rapidement de la valeur aux utilisateurs finaux, les fonctionnalités potentielles sont mises de côté dans un abysse de backlog.

Dans cet article, je vais vous montrer comment tout développeur Android peut utiliser la détection d'objets en temps réel pour créer une application qui détecte et reconnaît les animaux de compagnie — le tout en moins de 30 minutes. Pour ce faire, j'utiliserai le [Fritz SDK](https://fritz.ai) (divulgation complète, je travaille chez Fritz) qui facilite l'exploitation des capacités du machine learning sans aucune expérience préalable.

### Getting started

Pour commencer à utiliser le Fritz SDK, nous allons ajouter les dépendances nécessaires dans une application exemple que nous avons créée.

#### 1. Tout d'abord, créez un compte Fritz

[Inscrivez-vous ici](https://fritz.ai?utm_source=medium&utm_campaign=freecodecamp) et suivez les [instructions de démarrage](https://docs.fritz.ai/get-started.html?utm_source=medium&utm_campaign=freecodecamp).

#### **2.** Clonez l'application exemple de la caméra

Configurez une application squelette qui inclut un flux vidéo et du code de caméra. Dans ce tutoriel, nous n'approfondirons pas l'[API Camera 2](https://developer.android.com/reference/android/hardware/camera2/package-summary), mais si vous avez des questions, n'hésitez pas à laisser un commentaire.

```
git clone https://github.com/fritzlabs/camera-sample-app
```

#### **3.** Enregistrez l'application Android dans l'application web

Vous devez enregistrer votre application avec Fritz afin d'utiliser les fonctionnalités de ML. Lorsque vous ajoutez l'application à Fritz, utilisez le même applicationId (ai.fritz.camera) que dans le **app/build.gradle.**

![Image](https://cdn-media-1.freecodecamp.org/images/1*T9Vf0XvJgy8w1-RcyBT3oQ.png)
_Dans votre app/build.gradle, remarquez le champ applicationId_

![Image](https://cdn-media-1.freecodecamp.org/images/1*8LB6zgaIzCXbeiAX4eitZQ.png)
_L'ID du package doit correspondre à l'applicationId indiqué ci-dessus pour votre application. Dans ce cas, l'ID du package est **ai.fritz.camera**_

Assurez-vous de noter la clé API pour l'étape 5. Si vous devez y accéder à nouveau, vous pouvez aller dans Paramètres du projet > Votre application (Pet Monitor) > Afficher la clé API (dans le menu des options).

#### **4.** Ajoutez FritzCore + dépendances dans **app/build.gradle**

Assurez-vous d'ajouter le dépôt Fritz. Cela vous permettra de télécharger les dépendances nécessaires :

Dans la section des dépendances, ajoutez ces 2 bibliothèques :

```
dependencies {    implementation "ai.fritz:core:2.0.0"    implementation "ai.fritz:vision-object:2.0.0"}
```

#### 5. Configurez le SDK

Appelez **Fritz.configure** dans la méthode de cycle de vie **Application** ou **MainActivity onCreate** avec la clé API que vous avez obtenue à l'étape 3.

Avec cela, vous êtes prêt à utiliser la détection d'objets dans votre application.

### Détecter les chiens et les chats en vidéo en direct

Maintenant, passons aux choses amusantes. Nous allons plonger dans le MainActivity et utiliser le prédicteur de détection d'objets sur chaque image passée dans le flux vidéo.

#### 1. Obtenez une instance de FritzVisionObjectPredictor

Le prédicteur prend une **FritzVisionImage** et retourne une liste de **FritzVisionObjects** détectés.

#### **2.** Convertissez chaque image en un objet **FritzVisionImage**

Utilisez les méthodes statiques **fromBitmap** ou **fromMediaImage** pour créer un objet à partir d'un objet **Bitmap** ou **media.Image**. Pour l'application exemple, utilisez **fromMediaImage**, qui prend également en compte la rotation appliquée sur l'image par la caméra.

La rotation dépend de la rotation de l'appareil et du capteur d'orientation de la caméra. Le **cameraId** identifie la caméra active utilisée sur l'appareil (avant, arrière, etc.), et vous pouvez obtenir l'angle de rotation avec la méthode d'assistance suivante.

```
int rotation = FritzVisionOrientation.getImageRotationFromCamera(this, cameraId);
```

Enfin, créez un objet **FritzVisionImage** avec l'**Image** et la valeur de rotation.

#### **3. Exécutez la prédiction**

Passez l'image dans le prédicteur pour détecter différents objets dans l'image.

#### **4. Filtrez le résultat et affichez les boîtes de délimitation**

Chaque **FritzVisionObject** est accompagné d'une étiquette, d'un score de confiance et d'une boîte de délimitation qui montre où il se trouve sur l'image originale. Dans ce cas, nous nous intéressons uniquement aux animaux de compagnie (plus précisément aux chats et aux chiens), nous pouvons donc filtrer les autres éléments.

Enfin, affichez les boîtes de délimitation autour de vos animaux de compagnie. **FritzVisionObject** dispose d'une méthode pratique appelée **drawOnCanvas** qui facilite l'affichage des objets détectés.

Voici le code complet après le rappel de rendu :

**Remarquez le facteur d'échelle sur les boîtes.** Cela est dû au fait que l'objet **media.Image** que nous avons utilisé pour créer l'objet FritzVisionImage est de la même taille que la fenêtre de prévisualisation. Dans l'application exemple de la caméra, elle est de 1280 x 960. Les boîtes de délimitation auront des coordonnées associées à la taille de la prévisualisation. Comme nous voulons l'afficher en plein écran, nous devons mettre à l'échelle le résultat pour l'adapter à la fenêtre de visualisation du téléphone.

Voici le résultat final :

Pour le code finalisé, consultez le [dépôt GitHub](https://github.com/fritzlabs/pet-monitor-android).

### Pourquoi cela est utile

Avec la fonctionnalité de machine learning derrière cette application de base, il existe de nombreuses fonctionnalités différentes que vous pouvez créer (à la fois pratiques et amusantes) :

* Alerter les propriétaires par un message texte si le promeneur de chien n'est pas revenu.
* Enregistrer un message disant à votre chien de "S'asseoir !" lorsqu'il court dans la pièce sans personne autour. Je parie que vous pourriez également capturer des photos amusantes de votre chien à ce moment-là.
* Afficher un message à l'utilisateur lorsqu'un chat/chien est détecté (consultez le code finalisé pour un exemple)
* Déclencher une alarme lorsque la caméra détecte des chats (je suis allergique).

Bien sûr, peu de gens ont une tablette/un téléphone Android de rechange qu'ils peuvent utiliser comme une caméra de surveillance d'animaux de compagnie coûteuse, mais ce n'est qu'un exemple simple parmi de nombreuses possibilités différentes pour créer une application avec la [détection d'objets](https://docs.fritz.ai/features/object-detection/about.html?utm_source=medium&utm_campaign=freecodecamp) en utilisant [Fritz](https://fritz.ai?utm_source=medium&utm_campaign=freecodecamp). Je suis impatient de voir ce que tous les développeurs créatifs du monde construiront en utilisant la détection d'objets.

Vous avez une idée ? Laissez un commentaire !

Je suis un développeur principal chez [Fritz](https://fritz.ai?utm_source=medium&utm_campaign=freecodecamp), spécialisé dans le machine learning mobile. Si vous cherchez à créer des fonctionnalités alimentées par l'IA/ML, nous offrons des API préconstruites ([segmentation d'image](https://docs.fritz.ai/features/image-segmentation/about.html?utm_source=medium&utm_campaign=freecodecamp), [étiquetage d'image](https://docs.fritz.ai/features/image-labeling/about.html?utm_source=medium&utm_campaign=freecodecamp), [transfert de style](https://docs.fritz.ai/features/style-transfer/about.html?utm_source=medium&utm_campaign=freecodecamp)) et un support pour les [modèles personnalisés](https://docs.fritz.ai/custom-models/overview.html?utm_source=medium&utm_campaign=freecodecamp).