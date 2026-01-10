---
title: Comment intégrer Google AdMob dans Flutter
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-12-03T17:04:10.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-google-admob-to-flutter
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5fc59ecb49c47664ed827e9a.jpg
tags:
- name: Flutter
  slug: flutter
- name: Google
  slug: google
- name: mobile app development
  slug: mobile-app-development
seo_title: Comment intégrer Google AdMob dans Flutter
seo_desc: "By Krissanawat\nThe Flutter mobile application development framework is\
  \ rapidly making its mark as one of the leading cross-platform app development tools\
  \ out there today. \nMany companies and developers are choosing to use Flutter to\
  \ develop their app..."
---

Par Krissanawat

Le framework de développement d'applications mobiles Flutter s'impose rapidement comme l'un des principaux outils de développement d'applications multiplateformes disponibles aujourd'hui. 

De nombreuses entreprises et développeurs choisissent d'utiliser Flutter pour développer leurs applications, et vous pouvez voir ces applications dans le [market](https://flutter.dev/showcase). Flutter propose également de nombreux modèles d'applications personnalisés pour vous aider à démarrer. 

Mais de nos jours, une fois que vous avez construit une application, vous souhaitez peut-être la monétiser. Et quelle meilleure façon de le faire qu'avec Google AdMob ? AdMob est l'une des façons les plus simples de monétiser votre application, et nous allons voir comment dans cet article.

Ici, nous allons apprendre comment intégrer Google AdMob avec l'écosystème de développement de votre application Flutter. 

L'idée est d'abord d'apprendre à configurer une application Firebase ainsi qu'AdMob étape par étape. Après cela, nous les configurerons pour l'environnement Flutter. Enfin, nous afficherons une simple bannière publicitaire comme démonstration pour que vous puissiez voir comment AdMob fonctionne.

## Comment intégrer les configurations Firebase avec Flutter

Tout d'abord, nous allons intégrer les services Firebase avec notre projet Flutter. Mais d'abord, nous devons créer un projet Firebase. Vous pouvez trouver les directives de configuration dans la documentation officielle [Firebase](https://firebase.google.com/docs/flutter/setup?platform=android) pour Flutter.

Pour créer un projet Firebase, nous devons nous connecter à [Firebase](https://firebase.google.com/) et naviguer vers la console Firebase. Là, nous pouvons simplement cliquer sur 'Ajouter un projet' pour démarrer notre projet.

Au début, une fenêtre apparaîtra vous demandant de saisir le nom de votre projet. Ici, j'ai gardé le nom du projet simple - `FlutterAdmob` - comme montré dans la capture d'écran ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image.png)

Continuons à l'étape suivante jusqu'à ce que le projet soit créé. Après la création du projet, nous obtiendrons une console de projet comme montré dans la capture d'écran ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-1.png)

Ici, nous allons configurer Firebase pour la plateforme Android. Il suffit donc de cliquer sur l'icône Android comme vous le voyez dans la capture d'écran ci-dessus. Cela nous mènera à l'interface pour enregistrer Firebase dans notre application Flutter.

### ÉTAPE 1 : Enregistrer Firebase dans votre application Android

Le processus d'enregistrement est spécifique à la plateforme, nous allons donc nous enregistrer pour la plateforme Android. Après avoir cliqué sur l'icône Android, vous serez dirigé vers une interface demandant le **nom du package Android**. 

Pour ajouter le nom du package de notre projet Flutter, nous devons d'abord le localiser. Le nom du package sera disponible dans le fichier **./android/app/build.gradle** de votre projet Flutter. Vous verrez quelque chose comme ceci :

```jsx
com.example.backgroundSolution

```

Nous devons simplement le copier et le coller dans le champ de saisie du nom du package Android comme montré dans la capture d'écran ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-2.png)

Après cela, vous pouvez simplement cliquer sur le bouton 'Enregistrer l'application'. Cela nous mènera à l'interface où nous pouvons obtenir le fichier **google-services.json** qui liera notre application Flutter aux services Google de Firebase. 

Nous devons télécharger le fichier et le déplacer dans le répertoire **./android/app** de notre projet Flutter. Les instructions sont également montrées dans la capture d'écran ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-3.png)

### ÉTAPE 2 : Ajouter les configurations Firebase aux fichiers natifs dans votre projet Flutter

Maintenant, pour activer les services Firebase dans notre application Android, nous devons ajouter le [plugin google-services](https://developers.google.com/android/guides/google-services-plugin) à nos fichiers Gradle.

Tout d'abord, dans notre fichier Gradle de **niveau racine (niveau projet)** (**android/build.gradle**), nous devons ajouter des règles pour inclure le plugin Gradle des services Google. Nous devons vérifier si les configurations suivantes sont disponibles ou non :

```jsx
buildscript {
  repositories {
    // Vérifiez que vous avez la ligne suivante (si ce n'est pas le cas, ajoutez-la) :
    google()  // Dépôt Maven de Google
  }
  dependencies {
    ...
    // Ajoutez cette ligne
    classpath 'com.google.gms:google-services:4.3.4'
  }
}

allprojects {
  ...
  repositories {
    // Vérifiez que vous avez la ligne suivante (si ce n'est pas le cas, ajoutez-la) :
    google()  // Dépôt Maven de Google
    ...
  }
}

```

Si ce n'est pas le cas, nous devons ajouter les configurations comme montré dans l'extrait de code ci-dessus.

Maintenant, dans notre fichier Gradle de **module (niveau application)** (**android/app/build.gradle**), nous devons appliquer le plugin **Google Services Gradle**. 

Pour cela, nous devons ajouter le morceau de code mis en évidence dans l'extrait de code suivant au fichier **./android/app/build.gradle** de notre projet :

```jsx
// Ajoutez la ligne suivante :
apply plugin: 'com.google.gms.google-services'  // Plugin des services Google

android {
  // ...
}

```

Maintenant, nous devons exécuter la commande suivante afin que certaines configurations automatiques puissent être effectuées :

```jsx
flutter packages get

```

Maintenant, nous avons réussi à intégrer les configurations Firebase avec notre projet Flutter.

## Comment créer un compte AdMob

Maintenant, nous avons besoin d'un compte Google AdMob afin d'alimenter les publicités dans notre application. Pour cela, nous devons nous inscrire et nous connecter à [AdMob](https://admob.google.com/home/?subid=WW-EN-ET-firebase-docs). Ensuite, nous devons naviguer vers la console Google AdMob comme affiché dans la capture d'écran ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-24.png)

Maintenant, nous devons configurer une application AdMob qui nous donnera accès aux unités de publicité. Pour cela, nous devons cliquer sur le bouton 'AJOUTER VOTRE PREMIÈRE APPLICATION' montré dans la capture d'écran ci-dessus. 

Ensuite, nous serons dirigés vers l'écran où nous configurons l'application, comme montré dans la capture d'écran ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-5.png)

Ici, il est demandé si notre application est déjà disponible dans le Google Play ou l'App Store. Puisque nous faisons une démonstration de publicité de test, nous n'avons pas l'application publiée. Il suffit donc de sélectionner 'NON' ce qui vous dirigera vers un autre écran comme montré dans la capture d'écran ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-6.png)

Ici, nous devons entrer le nom de notre application ainsi que la plateforme. Vous pouvez donner le nom de votre choix. Ensuite, puisque nous travaillons avec Flutter pour Android, nous devons choisir Android et puis cliquer sur le bouton 'AJOUTER'.

Après cela, nous devons revenir à la console AdMob. Nous obtiendrons notre application AdMob dans la console des applications comme montré dans la capture d'écran ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-7.png)

Maintenant, nous devons cliquer sur 'AJOUTER UNE UNITÉ DE PUBLICITÉ' afin de créer une unité de publicité qui alimente la publicité de test. Après avoir cliqué, vous verrez un écran montrant différentes unités de publicité comme vous le voyez dans la capture d'écran ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-8.png)

Ici, nous avons une sélection de différentes publicités. Pour une implémentation simple, nous allons choisir la bannière publicitaire. 

Nous devons donc cliquer sur la publicité 'Bannière' puis choisir le nom de l'unité de publicité comme montré dans la capture d'écran ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-9.png)

Enfin, cliquez sur 'CRÉER UNE UNITÉ DE PUBLICITÉ' puis sur 'TERMINÉ' pour créer avec succès une unité de publicité, comme montré dans la capture d'écran ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-10.png)

Ici, nous avons l'unité de publicité (et gardez à l'esprit que l'ID de l'unité de publicité peut être utile lors de l'alimentation de la publicité réelle).

## Comment configurer AdMob dans un projet Flutter

Maintenant que nous avons notre application AdMob ainsi que l'unité de publicité de l'application AdMob prête, nous pouvons configurer AdMob dans notre projet Flutter. 

Pour cela, nous devons d'abord installer le plugin Firebase comme montré dans l'extrait de code ci-dessous :

```bash
firebase_admob: ^0.10.2

```

Maintenant, nous devons connecter l'application AdMob à notre plateforme native. Pour cela, nous devons ajouter un méta au fichier **[AndroidManifest.](http://androidmanifest.java)xml** comme montré dans l'extrait de code ci-dessous :

```xml
<meta-data
    android:name="com.google.android.gms.ads.APPLICATION_ID"
    android:value="[ADMOB_APP_ID]"/>

```

Ce fichier peut être trouvé dans le chemin "**./android/app/src/main/AndroidManifest.xml**". Au lieu de **[ADMOB_APP_ID]**, nous devons saisir l'ID d'application AdMob réel.

Nous pouvons l'obtenir à partir de la console **Paramètres de l'application** dans la console AbMob comme montré dans la capture d'écran ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-11.png)

Nous devons simplement copier l'ID de l'application et le coller dans l'argument `value`.

## Comment créer une bannière publicitaire

Maintenant, notre application AdMob est connectée à notre projet Flutter. Ici, nous allons créer une bannière publicitaire. L'idée est de montrer une bannière publicitaire de test en bas de l'écran de l'application.

Notez que nous utilisons le même projet d'application de fond d'écran Flutter que nous avons créé dans un [tutoriel précédent](https://kriss.io/how-to-build-wallpaper-app-with-flutter/). Le processus de configuration d'AdMob est le même dans chaque projet. Nous utilisons simplement ce projet comme démonstration.

Mais d'abord, nous devons importer certaines dépendances Firebase nécessaires dans le fichier `main.dart` comme montré dans l'extrait de code ci-dessous :

```dart
import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_admob/firebase_admob.dart';

```

Ensuite, nous devons initialiser l'appareil de test. Nous pouvons obtenir l'ID de l'appareil de test à partir des logs également :

```dart
const String testDevice = 'Kris';

```

Maintenant, nous allons créer une fonction qui retourne la bannière publicitaire. Pour cela, nous allons utiliser l'instance `BannerAd` fournie par la bibliothèque Firebase AdMob qui prend l'ID de l'unité de publicité, la taille et la fonction d'écoute comme paramètres. 

Nous pouvons utiliser l'ID de l'unité de bannière publicitaire que nous avons créé dans l'application AdMob plus tôt dans la propriété `adUnitId`. L'implémentation globale de la fonction est fournie dans l'extrait de code ci-dessous :

```dart
Future<void> main() async{
  WidgetsFlutterBinding.ensureInitialized();
  BannerAd createBannerAd() {
    return BannerAd(
      adUnitId: BannerAd.testAdUnitId,
      size: AdSize.banner,
      listener: (MobileAdEvent event) {
        print("BannerAd event $event");
      },
    );
  }
  runApp(MyApp());
}

```

Puisque nous allons afficher une bannière publicitaire de test ici, nous allons simplement utiliser le `testAdUnitId` fourni par l'instance `BannerAd`. Mais nous pouvons coller l'ID réel de l'unité de publicité que nous avons créé précédemment ici.

Maintenant, nous devons déclencher la fonction Banner Ad dans notre fonction `main`. Mais d'abord, nous devons lancer l'instance Firebase. 

Ensuite, nous devons initialiser l'instance `FirebaseAdMob` avec l'**ID d'application** que nous avons obtenu à partir de la console **Paramètres de l'application** de la console AdMob. 

Enfin, nous devons appeler la fonction `createBannerAd` puis `load` la publicité et `show` la publicité également. L'implémentation globale est fournie dans l'extrait de code ci-dessous :

```dart

 Future<void> main() async{
  .
	.
	.
  await Firebase.initializeApp();
  FirebaseAdMob.instance.initialize(appId: FirebaseAdMob.testAppId);
  createBannerAd()
    ..load()
    ..show();
  runApp(MyApp());
}

```

Ainsi, nous verrons la bannière publicitaire en bas de l'écran de l'application comme montré dans la capture d'écran de l'émulateur ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-12.png)

Comme vous pouvez le voir, il y a une bannière publicitaire de test en bas de l'écran de l'émulateur.

Félicitations - vous avez réussi à configurer AdMob dans une application Flutter !

_Notez que si nous utilisons l'ID réel de l'application et l'ID de l'unité de publicité, nous pourrons obtenir le flux publicitaire réel dans la bannière._

## Conclusion

Flutter est un framework de développement d'applications mobiles multiplateformes en croissance qui a attiré l'attention de nombreux développeurs et entreprises. Il est donc important d'apprendre certaines de ses fonctionnalités les plus utiles.

Dans cet article, nous avons intégré AdMob dans un projet Flutter. Le processus était un peu long mais simple. 

AdMob est l'un des meilleurs moyens de monétiser vos applications - mais pour en tirer le meilleur parti, vous devez savoir comment l'intégrer correctement à l'écran. 

L'objectif principal de ce tutoriel était de montrer comment configurer AdMob dans votre projet Flutter et ensuite afficher une simple bannière publicitaire. Le processus est le même pour toute application Flutter.

Maintenant, le défi est de présenter d'autres types d'unités publicitaires telles que les publicités interstitielles, les publicités natives, les publicités récompensées, etc., qui sont populaires de nos jours. Nous pouvons utiliser l'ID réel de l'application AbMob ainsi que l'ID de l'unité pour montrer le flux publicitaire réel à la place des publicités de test.

Vous pouvez voir des applications complètes avec une interface utilisateur et des fonctionnalités de pointe dans certaines applications [Flutter](http://www.instaflutter.com) sur le marché.