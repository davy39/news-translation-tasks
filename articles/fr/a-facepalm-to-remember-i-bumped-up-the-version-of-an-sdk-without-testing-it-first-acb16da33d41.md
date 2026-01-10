---
title: 'Un Facepalm à retenir : J''ai augmenté la version d''un SDK sans le tester
  d''abord.'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-01-16T06:08:31.000Z'
originalURL: https://freecodecamp.org/news/a-facepalm-to-remember-i-bumped-up-the-version-of-an-sdk-without-testing-it-first-acb16da33d41
coverImage: https://cdn-media-1.freecodecamp.org/images/1*-hj6FOiWHQDYIWJgCmbeZQ.jpeg
tags:
- name: Android
  slug: android
- name: android app development
  slug: android-app-development
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: startup
  slug: startup
seo_title: 'Un Facepalm à retenir : J''ai augmenté la version d''un SDK sans le tester
  d''abord.'
seo_desc: 'By Rahul Chowdhury

  It all started when Google made its App Shortcuts API available for developers on
  Android. I was super excited to add this to my hash tagging Android app, Magnify.
  So I started digging through their documentation for steps to imple...'
---

Par Rahul Chowdhury

Tout a commencé lorsque Google a rendu son API App Shortcuts disponible pour les développeurs sur Android. J'étais super excité à l'idée de l'ajouter à mon application Android de hash tagging, [Magnify](https://play.google.com/store/apps/details?id=com.upcurve.magnify). J'ai donc commencé à parcourir [leur documentation](https://developer.android.com/guide/topics/ui/shortcuts.html) pour les étapes à suivre afin de l'implémenter.

La première chose que j'ai remarquée était que la version d'API requise pour Android `targetSdkVersion` était plus élevée que celle que j'utilisais. « Pas de problème », ai-je pensé. Et je l'ai augmentée à une version plus récente.

### L'« Erreur »

Augmenter la version de mon SDK n'était pas une erreur. L'erreur était de ne pas avoir testé l'application de manière approfondie sur la dernière version d'Android. J'ai simplement ajouté la fonctionnalité de raccourci, testé cela à fond, puis poussé mes changements — sans réaliser qu'un changement majeur d'API avait été apporté à cette nouvelle version du SDK.

Android Nougat impose une vérification sur la portée des fichiers partagés entre les applications du système. Si vous essayez de partager un fichier qui est enregistré dans la portée de votre application avec une application externe en utilisant l'approche traditionnelle `file://`, votre application rencontrera une `FileUriExposedException`, provoquant l'affichage de ce dialogue de plantage disgracieux que aucun développeur — et certainement aucun utilisateur — ne veut jamais voir.

Comment j'ai corrigé cette exception dépasse le cadre de cet article. Laissez-moi plutôt partager comment cette petite erreur stupide a affecté mon application.

### Le « Problème »

Auparavant, lorsque je ciblais les utilisateurs d'Android Marshmallow, mon application arrivait toujours à se faufiler par cette porte cachée connue sous le nom de « mode de compatibilité » lorsqu'elle fonctionnait sur Nougat. J'étais donc totalement détendu en sachant que mon application fonctionnait bien sur la dernière version du système d'exploitation.

```
android {     defaultConfig {         minSdkVersion 18         targetSdkVersion 23 //Ciblant Marshmallow    }}
```

Mais maintenant, les choses étaient légèrement différentes pour ma pauvre petite application. Puisqu'elle indiquait qu'elle ciblait la dernière version d'Android, le système d'exploitation supposait qu'elle avait été bien testée pour toutes les nouvelles mises à jour de l'API, et devait être punie pour toute violation. Dans mon cas, il s'agissait de `FileUriExposedException`, car je partageais des photos en utilisant l'approche traditionnelle `file://` au lieu de passer à une solution sûre et robuste.

```
android {     defaultConfig {         minSdkVersion 18         targetSdkVersion 25 //Ciblant Nougat 7.1    }}
```

La peine ultime ? « Malheureusement, Magnify a cessé de fonctionner. »

### Le « Plus Gros Problème »

Bien que le plantage était un problème sérieux en soi, je devais encore découvrir un problème encore plus grand. Puisque Android Nougat n'était disponible que pour environ 0,6 % des utilisateurs de téléphones Android à cette époque — et pour environ 2-3 % des personnes utilisant mon application — il s'agissait d'un plantage qui aurait pu rester caché pendant des semaines.

Heureusement, l'un de mes utilisateurs avait un Google Pixel fonctionnant sous Nougat, et c'est elle qui a attiré mon attention sur le fait que l'application était cassée. J'ai corrigé le problème et déployé une autre mise à jour avec la correction de ce plantage, que la plupart des utilisateurs n'avaient pas remarqué, car j'ai été informé du problème en un jour ou deux.

Ouf ! C'était vraiment très proche.

### Comment l'ai-je résolu ?

Oui, oui, j'ai dit que je ne rentrerais pas dans les détails de la résolution du problème, mais c'est un peu difficile pour moi de voir un autre développeur lutter contre le même problème que j'ai eu, sachant que j'aurais pu aider et ajouter quelques moments de bonheur à leur vie.

Voici comment je l'ai fait :

[**Le schéma file:// n'est plus autorisé à être attaché à Intent sur targetSdkVersion 24 (Android Nougat...**](https://inthecheesefactory.com/blog/how-to-share-access-to-file-with-fileprovider-on-android-nougat/en)  
[_Android Nougat est presque publié. Et en tant que développeur Android, nous devons nous préparer à nous adapter..._inthecheesefactory.com](https://inthecheesefactory.com/blog/how-to-share-access-to-file-with-fileprovider-on-android-nougat/en)

### Morale de l'histoire

Ne déployez jamais — et je répète, jamais — une mise à jour de votre logiciel sans des tests très, très approfondis lorsque vous avez augmenté la version de votre SDK. Il y a des chances que des changements d'API vous aient échappé — certains d'entre eux pourraient casser votre logiciel pour de bon.

Assurez-vous de livrer vos mises à jour uniquement après des tests appropriés. Un peu de temps passé à tester peut économiser beaucoup de temps pour regagner la confiance de vos utilisateurs.

Oh, et :

> Il n'y a pas d'erreurs, sauf une : l'échec d'apprendre d'une erreur. — Robert Fripp

Parce que vous ne terminez pas un article génial sans une citation d'enfer. ? ✍️

Si vous avez aimé cette histoire, n'hésitez pas à la recommander à d'autres personnes en cliquant sur le bouton ? sur cette page, et suivez-moi pour plus d'histoires sur la programmation.