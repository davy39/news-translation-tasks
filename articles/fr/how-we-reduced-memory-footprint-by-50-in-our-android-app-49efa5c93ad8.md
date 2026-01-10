---
title: Comment nous avons réduit de 50 % l'empreinte mémoire de notre application
  Android
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-01-19T11:44:29.000Z'
originalURL: https://freecodecamp.org/news/how-we-reduced-memory-footprint-by-50-in-our-android-app-49efa5c93ad8
coverImage: https://cdn-media-1.freecodecamp.org/images/1*IqiQOSbYUgaA_166irZLUg.jpeg
tags:
- name: Android
  slug: android
- name: android app development
  slug: android-app-development
- name: Java
  slug: java
- name: mobile app development
  slug: mobile-app-development
- name: General Programming
  slug: programming
seo_title: Comment nous avons réduit de 50 % l'empreinte mémoire de notre application
  Android
seo_desc: 'By Rohit Arya

  Like any other startup momentum-obsessed startup, we didn’t spend a lot of time
  to building an efficient product on the first go. We shipped our Android app, and
  it was working “just fine.”

  As we started scaling up in terms of our offer...'
---

Par Rohit Arya

Comme toute autre startup obsédée par la croissance, nous n'avons pas passé beaucoup de temps à construire un produit efficace dès le premier essai. Nous avons lancé notre application Android, et elle fonctionnait "juste bien".

Alors que nous commencions à développer notre offre pour les clients, notre application est devenue volumineuse — avec des tonnes d'images — et nous avons commencé à voir des problèmes de performance. Notre application est devenue lente et gelait sur les appareils bas de gamme. La consommation de batterie a également augmenté.

Pour déboguer ce problème, nous avons utilisé un outil de surveillance de la mémoire fourni par Android Studio. Alors que nous faisions défiler une très longue liste d'images de produits, voici ce que nous avons observé :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Xl1mzt7IxkIMNqaufLc2qA.png)
_L'utilisation de la mémoire de l'application Android Jumbotail au fil du temps_

Pour expliquer ces graphiques un peu mieux :

* La chute soudaine de la mémoire allouée est due aux événements de Garbage Collection (GC).
* La taille de la mémoire libre augmente lorsqu'Android tue les processus d'autres applications (qui sont en arrière-plan) pour allouer plus de mémoire à l'application au premier plan.
* L'utilisation du CPU a augmenté lorsque nous avons fait défiler la liste des produits.

Rien qu'en ouvrant la page de liste des produits, l'application consommait 15 mégaoctets de mémoire. Si nous faisions défiler jusqu'en bas de la page de liste des produits, l'application consommait 50 mégaoctets de mémoire, avec beaucoup d'événements GC.

En faisant défiler d'autres listes de produits, nous avons observé des schémas similaires. Voici les graphiques :

![Image](https://cdn-media-1.freecodecamp.org/images/1*pmm1lTuQgN0TxQRfE_6Cwg.png)
_Image 2 : Utilisation de la mémoire au fil du temps_

![Image](https://cdn-media-1.freecodecamp.org/images/1*Wfqo-YN5NTUqH6oOpZJIxw.png)
_Image 3 : Utilisation de la mémoire au fil du temps_

Nous avons à nouveau observé ce schéma. À ce moment-là, Android avait alloué la mémoire maximale (pour les bitmaps) — qu'il pouvait allouer à notre application en tuant les processus d'autres applications en arrière-plan — et l'allocation nette de mémoire avait atteint 57 mégaoctets avec plusieurs événements GC.

Ces graphiques proviennent de l'environnement d'exécution Android. [Dalvik se comporte encore plus mal en termes de gestion de la mémoire et de Garbage Collection](https://source.android.com/devices/tech/dalvik/).

Dans Android, les bitmaps représentent les plus grands blocs contigus de mémoire. Ils occupent des tas, ce qui entraîne beaucoup de contention pour trouver de l'espace libre afin d'allouer de nouveaux bitmaps lors du défilement. Cela entraîne ensuite plus d'événements GC afin de libérer de la mémoire pour fournir l'espace nécessaire. Comme il y avait tant d'images chargées dans la liste, ces événements GC dégradaient les performances de notre application.

![Image](https://cdn-media-1.freecodecamp.org/images/1*r7s67WCZA06DJyI3aU6JuQ.gif)

Les événements GC provoquent le gel de l'application jusqu'à ce qu'ils se terminent. Quelques-uns de ceux-ci n'ont pas d'importance, mais trop de ces événements entraîneront un taux de rafraîchissement plus faible. L'exécution d'un Garbage Collector provoque également une utilisation accrue du CPU, ce qui consomme la batterie.

De plus, plus l'utilisation de la mémoire d'une application est élevée, plus le système est susceptible de décider de la tuer lorsqu'elle s'exécute en arrière-plan.

Nous devions résoudre ce problème avant de pouvoir avancer davantage avec le développement du produit. Et pour cela, nous avons adopté le concept de pool d'objets pour les bitmaps, comme conseillé par Colt dans cette vidéo :

L'idée est donc, au lieu de créer un tout nouveau bitmap, d'utiliser une partie existante de la mémoire pour charger le bitmap :

```
mBitmapOptions.inBitmap = mCurrentBitmap;//utilisation de mCurrentBitmap pour charger le nouveau bitmapmCurrentBitmap = BitmapFactory.decodeFile(fileName, mBitmapOptions);
```

Ensuite, lorsque vous faites défiler une longue liste d'images, il n'est pas nécessaire de charger toutes les images dans des allocations de mémoire séparées. Vous pouvez simplement allouer un nombre maximum de bitmaps qui vont être visibles, puis réutiliser leur mémoire — évitant ainsi ces horribles événements GC.

Voici les résultats montrant les améliorations :

![Image](https://cdn-media-1.freecodecamp.org/images/1*wDzaQ4jwqGGfZLzGvkLCFg.png)
_Image 4 : Utilisation de la mémoire au fil du temps (améliorée)_

Nous avons fait défiler la même liste de produits à nouveau après avoir apporté les modifications. Nous avons observé qu'avec une allocation initiale de 15 mégaoctets de mémoire, il n'y avait que 27 mégaoctets d'allocation totale de mémoire effectuée au moment où nous avions fait défiler jusqu'en bas de la page (et avec très peu d'événements GC).

![Image](https://cdn-media-1.freecodecamp.org/images/1*z8owi_QAyugPeAi_JfUqHQ.png)
_Image 5 : Utilisation de la mémoire au fil du temps (améliorée)_

Nous avons fait défiler quelques listes de produits supplémentaires et nous avons observé **aucune allocation de mémoire supplémentaire** (magie du Bitmap Pool) et donc aucun événement GC majeur.

En fin de compte, nous avions réussi à réduire l'empreinte mémoire des bitmaps de près de 50 %.

Nous devons être conscients du fait qu'Android a certaines contraintes pour la réutilisation des bitmaps, concernant la taille physique des bitmaps existants :

1. Dans les versions du SDK 11 à 18, les bitmaps que nous chargeons et les bitmaps que nous réutilisons doivent être exactement de la même taille. Nous avons résolu ce problème en utilisant la taille exacte de l'ImageView dans notre liste pour toutes les versions du SDK avant la version 18.
2. Dans les versions du SDK plus récentes que 19, les bitmaps existants que nous voulons utiliser peuvent être supérieurs ou égaux en dimensions au nouveau bitmap entrant.

Nous essayons également d'utiliser le même format de pixel pour la réutilisation des bitmaps. Ainsi, pour charger une image en tant que bitmap `RGB_565`, nous utilisons l'allocation de bitmap `RGB_565`.

La bonne nouvelle est que vous n'avez pas à faire tout cela vous-même. Il existe déjà des bibliothèques incroyables comme [Glide](https://github.com/bumptech/glide) et [Fresco](https://github.com/facebook/fresco) qui ont des capacités intégrées pour réutiliser la mémoire des bitmaps. Tout ce que vous avez à faire est de vous assurer que vos bitmaps peuvent être réutilisés. (N'oubliez pas qu'il existe des contraintes concernant les dimensions des bitmaps et `Bitmap.Config`.) Si vous ne souhaitez pas utiliser celles-ci, vous pouvez simplement intégrer un [Bitmap Pool](https://github.com/amitshekhariitbhu/GlideBitmapPool) dans votre chargeur d'images existant. L'utilisation de ces bibliothèques vous aidera également à économiser de la mémoire précieuse en pré-dimensionnant les bitmaps, et bien plus encore.

Parallèlement à cela, nous avons également commencé à utiliser le format `RGB_565`, qui ne prend que 16 bits par pixel — contre `ARGB_8888` qui prend 32 bits par pixel — sur les appareils à faible mémoire. Cela réduit encore davantage notre empreinte mémoire.

Il y a beaucoup de choses géniales que vous pouvez faire pour améliorer les performances de votre application. Nous continuerons à les publier. Construisons de meilleures applications.

Si vous avez aimé lire cet article, cela signifierait beaucoup pour nous si vous le recommandiez en utilisant l'icône ❤ et le partagez avec vos collègues et amis. Merci !

De plus, connectons-nous sur [Facebook](https://www.facebook.com/aryarohit07), [Twitter](https://twitter.com/arya_rohit07), [Linkedin](https://in.linkedin.com/in/aryarohit07) et [Github](https://github.com/aryarohit07/).