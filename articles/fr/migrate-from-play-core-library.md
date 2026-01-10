---
title: Comment migrer depuis la bibliothèque Play Core
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2024-06-26T17:53:46.000Z'
originalURL: https://freecodecamp.org/news/migrate-from-play-core-library
coverImage: https://www.freecodecamp.org/news/content/images/2024/06/ben-hershey-fnRKVPx5_xY-unsplash.jpg
tags:
- name: Android
  slug: android
- name: android app development
  slug: android-app-development
seo_title: Comment migrer depuis la bibliothèque Play Core
seo_desc: 'You may have recently received an email from Google Play Store stating
  the following:


  Update your Play Core Maven dependency to an Android 14 compatible version! Your
  current Play Core library is incompatible with targetSdkVersion 34 (Android 14),
  w...'
---

Vous avez peut-être récemment reçu un e-mail du Google Play Store indiquant ce qui suit :

> _Mettez à jour votre dépendance Maven Play Core vers une version compatible avec Android 14 ! Votre bibliothèque Play Core actuelle est incompatible avec targetSdkVersion 34 (Android 14), qui introduit un changement rétro-incompatible des récepteurs de diffusion pour améliorer la sécurité des utilisateurs. Rappel : à partir du 31 août, Google Play exige que toutes les nouvelles versions d'applications ciblent Android 14. Mettez à jour vers la dernière version de la dépendance de la bibliothèque Play Core pour éviter les plantages de l'application :_ [_https://developer.android.com/guide/playcore#playcore-migration_](https://developer.android.com/guide/playcore#playcore-migration)  
>   
> _Vous ne pourrez peut-être pas publier de futures versions de votre application avec cette version du SDK en production ou en test ouvert._

Cela semble effrayant, n'est-ce pas ?

Ne vous inquiétez pas trop. C'est en réalité plus simple que cela en a l'air.

## De quoi s'agit réellement le changement

En gros, Google a cessé de publier de nouvelles versions de la bibliothèque play core dès début 2022.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/1.jpg)
_La dernière version de la bibliothèque play core publiée_

Et depuis avril 2022, ils ont divisé la bibliothèque play core originale en quatre bibliothèques distinctes :

* Bibliothèque Play Assets Delivery
* Bibliothèque Play Feature Delivery
* Bibliothèque Play In-App Reviews
* Bibliothèque Play In-App Updates

Chaque bibliothèque a sa propre fonctionnalité et responsabilité.

Puisque l'ancienne bibliothèque play core ne supporte que jusqu'à un certain niveau d'API, vous devez migrer votre application pour utiliser les nouvelles bibliothèques qui supportent les niveaux d'API les plus récents.

En essence, vous devez déterminer quelle fonctionnalité de l'ancienne bibliothèque play core vous utilisez et ensuite télécharger la partie correcte. Par exemple, si vous aviez une logique pour notifier les utilisateurs lorsqu'une nouvelle version de votre application était disponible, vous devez prendre la bibliothèque Play In-App-Updates.

Nous allons présenter deux cas d'utilisation ici :

* Application Android native
* Application Flutter

## Cas d'utilisation – Application Android native

Si vous avez une application Android native, qu'elle soit écrite en Kotlin ou en Java, vous devez faire ce qui suit :

1. Ouvrez votre fichier build.gradle au niveau de l'application
2. Très probablement, vous verrez sous le bloc des dépendances cette ligne :

```groovy
implementation 'com.google.android.play:core-ktx:1.8.1'

```

3. Vous devrez la supprimer et la remplacer selon ce que vous utilisiez dans l'ancienne bibliothèque core

4. Si vous devez prendre la bibliothèque Play In-App-Updates, alors vous devez ajouter ceci au bloc des dépendances :

```groovy
implementation 'com.google.android.play:app-update:2.1.0'
// Ajoutez la dépendance ci-dessous si vous utilisez Kotlin dans votre application
implementation 'com.google.android.play:app-update-ktx:2.1.0'
```

5. Reconstruisez votre application et vérifiez que tout fonctionne comme il se doit.

✍ Vous devrez peut-être également changer les instructions d'importation de **import com.google.android.play.core.tasks.*;** à **import com.google.android.gms.tasks.*;**.

## Cas d'utilisation – Application Flutter

Puisque Flutter est un framework qui s'adresse à la fois à Android et iOS, ce scénario est un peu différent de celui ci-dessus. Si vous recevez l'avertissement de mettre à jour la bibliothèque play core dans votre application Flutter, vous devez examiner les bibliothèques que vous utilisez dans votre fichier pubspec.yaml :

```yaml
dependencies:
  flutter:
    sdk: flutter
  ...
  in_app_update: ^3.0.0
```

Comme vous pouvez le voir ci-dessus, l'application dépend de la bibliothèque **in_app_update**, qui permet de notifier les utilisateurs lorsqu'une nouvelle version de l'application est disponible. Lorsque nous nous rendons sur la page du [journal des modifications](https://pub.dev/packages/in_app_update/changelog) de in_app_update sur pub.dev, nous pouvons voir que :

![Image](https://www.freecodecamp.org/news/content/images/2024/06/1-1.jpg)
_la version 4.1.0 a ajouté le support requis_

Nous devons donc mettre à jour notre fichier pubspec.yaml pour utiliser cette version (au minimum).

```yaml
dependencies:
  flutter:
    sdk: flutter
  ...
  in_app_update: ^4.1.0
```

Exécutez Pub get et tout devrait être bon.