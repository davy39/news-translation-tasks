---
title: Bibliothèque Android de centrage de visage basée sur l'API Google Vision
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-07-20T11:15:42.000Z'
originalURL: https://freecodecamp.org/news/face-centering-android-library-build-on-top-of-google-vision-api-f88661b97959
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9MTjfLoGfWIRXjlhMaTucw.png
tags:
- name: Android
  slug: android
- name: android app development
  slug: android-app-development
- name: Design
  slug: design
- name: open source
  slug: open-source
- name: technology
  slug: technology
seo_title: Bibliothèque Android de centrage de visage basée sur l'API Google Vision
seo_desc: 'By Rohit Arya

  In our Android apps, when we crop photos to display them, we often encounter the
  problem of positioning faces properly.

  This inspired me to create a tool that will locate faces and in an image (if there
  are any) and center the cropped i...'
---

Par Rohit Arya

Dans nos applications Android, lorsque nous recadrons des photos pour les afficher, nous rencontrons souvent le problème de positionnement correct des visages.

Cela m'a inspiré à créer un outil qui localisera les visages dans une image (s'il y en a) et centra le recadrage de l'image autour d'eux.

Voici comment j'ai procédé.

J'ai commencé avec l'[API de détection de visage](https://developers.google.com/vision/face-detection-concepts) de Google Mobile Vision. Cette API fournit :

* Détection de visage (pas reconnaissance faciale)
* Suivi de visage (étend la détection de visage aux séquences vidéo)
* Un **point de repère** — un point d'intérêt dans un visage (comme les yeux, le nez, etc.)
* Classification d'un visage pour déterminer si le visage sourit, si les yeux sont ouverts ou fermés, et d'autres caractéristiques

Puisque je voulais seulement la position du visage, j'ai utilisé uniquement le composant de détection de visage. Pour commencer, j'ai créé le détecteur de visage :

```java
FaceDetector detector = new FaceDetector.Builder(context)
    .setTrackingEnabled(false)
    .build();
```

Maintenant, étant donné un bitmap, j'ai créé une instance de frame à partir du bitmap pour fournir au détecteur :

```java
Frame frame = new Frame.Builder().setBitmap(bitmap).build();
```

Ensuite, j'ai essayé de détecter les visages de manière synchrone dans le frame :

```java
SparseArray<Face> faces = detector.detect(frame);
```

Une fois les visages détectés, j'ai choisi un visage (pour l'instant) pour recadrer l'image autour, en gardant ce visage au centre.

Maintenant, pour commencer à recadrer l'image :

* J'ai créé un nouveau bitmap redimensionné pour s'adapter à la vue cible (ImageView).
* J'ai ensuite recalculé la position du visage dans le nouveau bitmap.
* En gardant le visage au centre, j'ai recadré le bitmap original pour obtenir un nouveau bitmap.
* Si aucun visage n'est détecté, alors je reviens au recadrage CENTER CROP.

_Vous pouvez trouver le code complet dans [mes dépôts GitHub](https://github.com/aryarohit07) ci-dessous._

Voici quelques résultats :

![Image](https://cdn-media-1.freecodecamp.org/images/uaukFMMKsp3BvFT7JUNMHn4Cvg-X4VpvIhpK)
_Image originale à recadrer._

![Image](https://cdn-media-1.freecodecamp.org/images/-yG3bvIhkNPDtAtgmbgEEsJGXjxg0eKYF6JA)
_Résultats après recadrage_

![Image](https://cdn-media-1.freecodecamp.org/images/Hms3iIRztMyLsd6gDHInDvSbhIIhrD2e2NLH)
_Image originale_

![Image](https://cdn-media-1.freecodecamp.org/images/WLQx73hHnBlvLriXqHJPA1agUmEedBcTRIsh)
_Résultats après recadrage_

![Image](https://cdn-media-1.freecodecamp.org/images/np-29WMZZdUWy6XQHjxZhAAa5EaQWtY8YBdP)
_Image originale_

![Image](https://cdn-media-1.freecodecamp.org/images/slny81MI3mfiuITJE--qFn5q2qZqkHNnOqoL)
_Résultats après recadrage_

![Image](https://cdn-media-1.freecodecamp.org/images/Lg6EwpnyTdemmnG97sljtu-o2LyucFQPNB5y)
_Image originale_

![Image](https://cdn-media-1.freecodecamp.org/images/osDqcv3pEObAsIHEaMD8VaTwM0EwfuKzkL6b)
_Résultats après recadrage_

J'ai finalement exporté cela sous forme de bibliothèque, que vous pouvez trouver ci-dessous.

Pour [Glide](https://github.com/bumptech/glide) :

[**aryarohit07/GlideFaceDetectionTransformation**](https://github.com/aryarohit07/GlideFaceDetectionTransformation)
[_GlideFaceDetectionTransformation - Une bibliothèque de transformation d'images Android fournissant un recadrage basé sur la détection de visage…_](https://github.com/aryarohit07/GlideFaceDetectionTransformation)
[github.com](https://github.com/aryarohit07/GlideFaceDetectionTransformation)

Pour [Picasso](https://github.com/square/picasso) :

[**aryarohit07/PicassoFaceDetectionTransformation**](https://github.com/aryarohit07/PicassoFaceDetectionTransformation)
[_PicassoFaceDetectionTransformation - Une bibliothèque de transformation d'images Android fournissant un recadrage basé sur la détection de visage…_](https://github.com/aryarohit07/PicassoFaceDetectionTransformation)
[github.com](https://github.com/aryarohit07/PicassoFaceDetectionTransformation)

Je prévois également de le publier pour [Fresco](https://github.com/facebook/fresco).

N'hésitez pas à utiliser cet outil et à m'aider à l'améliorer sur GitHub.

> _Si vous avez aimé lire cet article, cela signifierait beaucoup pour moi si vous le recommandiez en utilisant l'icône ❤ et le partagez avec vos collègues et amis. Merci !_