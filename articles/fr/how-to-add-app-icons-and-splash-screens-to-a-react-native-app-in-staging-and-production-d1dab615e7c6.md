---
title: Comment ajouter des icônes d'application et des écrans de démarrage à une application
  React Native en staging et production
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-24T20:08:55.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-app-icons-and-splash-screens-to-a-react-native-app-in-staging-and-production-d1dab615e7c6
coverImage: https://cdn-media-1.freecodecamp.org/images/0*JXVkvIcwnggBNCRp.jpg
tags:
- name: Apps
  slug: apps-tag
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment ajouter des icônes d'application et des écrans de démarrage à une
  application React Native en staging et production
seo_desc: 'By Khoa Pham

  React Native was designed to be “learn once, write anywhere,” and it is usually
  used to build cross platform apps for iOS and Android. And for each app that we
  build, there are times we need to reuse the same code, build and tweak it a b...'
---

Par Khoa Pham

React Native a été conçu pour être "apprendre une fois, écrire partout", et il est généralement utilisé pour créer des applications multiplateformes pour iOS et Android. Et pour chaque application que nous développons, il arrive que nous devions réutiliser le même code, le construire et le modifier un peu pour qu'il fonctionne dans différents environnements. Par exemple, nous pourrions avoir besoin de plusieurs skins, thèmes, une version gratuite et payante, ou plus souvent différents environnements de staging et de production.

Et la tâche que nous ne pouvons pas éviter est d'ajouter des icônes d'application et des écrans de démarrage à nos applications.

En fait, pour ajouter un environnement de staging et de production, et pour ajouter des icônes d'application, nous devons utiliser Xcode et Android Studio, et nous le faisons de la même manière que pour les projets iOS ou Android natifs.

Appelons notre application `MyApp` et initialisons-la avec `react-native init MyApp`. Il existe bien sûr de nombreuses [bibliothèques](https://github.com/thekevinbrown/react-native-schemes-manager) pour nous aider à gérer différents environnements.

Dans cet article, nous allons procéder comme nous l'avons fait avec les applications natives, afin de connaître les étapes de base.

### Configuration de build, cible, types de build, saveur de production et variante de build

Il y a quelques terminologies que nous devons retenir. Dans iOS, les versions debug et release sont appelées [configurations de build](https://developer.apple.com/library/archive/featuredarticles/XcodeConcepts/Concept-Build_Settings.html), et les versions staging et production sont appelées [cibles](https://developer.apple.com/library/archive/featuredarticles/XcodeConcepts/Concept-Targets.html).

> Une configuration de build spécifie un ensemble de paramètres de build utilisés pour construire le produit d'une cible de manière particulière. Par exemple, il est courant d'avoir des configurations de build séparées pour les builds de debug et de release d'un produit.

> Une cible spécifie un produit à construire et contient les instructions pour construire le produit à partir d'un ensemble de fichiers dans un projet ou un espace de travail. Une cible définit un seul produit ; elle organise les entrées dans le système de build — les fichiers sources et les instructions pour traiter ces fichiers sources — nécessaires pour construire ce produit. Les projets peuvent contenir une ou plusieurs cibles, chacune produisant un produit.

Dans Android, les versions debug et release sont appelées types de build, et les versions staging et production sont appelées saveurs de produit. Ensemble, elles forment des [variantes de build](https://developer.android.com/studio/build/build-variants).

> Par exemple, une saveur de produit "demo" peut spécifier différentes fonctionnalités et exigences de périphérique, telles que du code source personnalisé, des ressources et des niveaux d'API minimum, tandis que le type de build "debug" applique différents paramètres de build et de packaging, tels que des options de debug et des clés de signature. La variante de build résultante est la version "demoDebug" de votre application, et elle inclut une combinaison des configurations et ressources incluses dans la saveur de produit "demo", le type de build "debug", et l'ensemble de sources `main/`.

### Cibles de staging et de production dans iOS

Ouvrez `MyApp.xcodeproj` dans le dossier `ios` en utilisant Xcode. Voici ce que nous obtenons après l'initialisation :

![Image](https://cdn-media-1.freecodecamp.org/images/aT6TxJtPwQZYaQFQdx5RRnMfT18AHhveEHoW)

React Native crée des applications iOS et tvOS, ainsi que deux cibles de test. Dans Xcode, un projet peut contenir plusieurs cibles, et chaque cible signifie un produit unique avec ses propres paramètres de build — Info.plist et icônes d'application.

#### Dupliquer la cible

Si nous n'avons pas besoin de l'application tvOS, nous pouvons supprimer `MyApp-tvOS` et `MyApp-tvOSTests`. Utilisons la cible `MyApp` comme notre environnement de production, et faisons un clic droit -> Dupliquer pour créer une autre cible. Appelons-la `MyApp Staging`.

![Image](https://cdn-media-1.freecodecamp.org/images/5hHjVB8EwYB5quzM26IUy9DufaCXNiRjp2N3)

Chaque cible doit avoir un identifiant de bundle unique. Changez l'identifiant de bundle de `MyApp` en `com.onmyway133.MyApp` et celui de `MyApp Staging` en `com.onmyway133.MyApp.Staging`.

![Image](https://cdn-media-1.freecodecamp.org/images/g02pyEjScSy4RYD2BlxlqndP-czHtvanJ7K7)

#### Info.plist

Lorsque nous dupliquons la cible `MyApp`, Xcode duplique également `Info.plist` en `MyApp copy-Info.plist` pour la cible de staging. Changez-le en un nom plus significatif `Info-Staging.plist` et glissez-le dans le groupe `MyApp` dans Xcode pour rester organisé. Après avoir glissé, la cible `MyApp Staging` ne peut pas trouver le plist, alors cliquez sur `Choose Info.plist File` et pointez vers `Info-Staging.plist`.

![Image](https://cdn-media-1.freecodecamp.org/images/sKyaTbgpYQfP7hRLus8TNqKb9tbsEwfqjHRU)

#### Schéma

Xcode duplique également le schéma lorsque nous dupliquons la cible, donc nous obtenons `MyApp copy` :

![Image](https://cdn-media-1.freecodecamp.org/images/ipNpPhA6cf4n6riHzYOv6L3rARKgZX78F4eb)

Cliquez sur `Manage Schemes` dans le menu déroulant des schémas pour ouvrir le gestionnaire de schémas :

![Image](https://cdn-media-1.freecodecamp.org/images/EwS7sAXkEYSz1dNAEDSAx5nXTtxgpdOrqW4W)

Je supprime généralement le schéma généré `MyApp copy`, puis je crée un nouveau schéma pour la cible `MyApp Staging`. Vous devez vous assurer que le schéma est marqué comme Partagé afin qu'il soit suivi dans git.

![Image](https://cdn-media-1.freecodecamp.org/images/pubibFLRmRXA70peau6B-lCOTsezlSw7ph5E)

Pour une raison quelconque, le schéma de staging n'a pas tout configuré comme le schéma de production. Vous pouvez rencontrer des problèmes comme `React/RCTBundleURLProvider.h file not found` ou `[RN: React/RCTBridgeModule.h file not found](https://github.com/onmyway133/notes/issues/380)`. C'est parce que la cible `React` n'est pas encore liée.

Pour résoudre cela, nous devons désactiver `Parallelise Build` et ajouter la cible `React` et la déplacer au-dessus de `MyApp Staging`.

![Image](https://cdn-media-1.freecodecamp.org/images/VhJq58o3EFkfP2OohZEOi2Mc6d2oDwcOdOE6)

#### Saveurs de produit de staging et de production dans Android

Ouvrez le dossier `android` dans Android Studio. Par défaut, il n'y a que les types de build debug et release :

![Image](https://cdn-media-1.freecodecamp.org/images/LXNMq2Tdm4QFsoWCpw-SEgUkQsk9PsUOs0Od)

Ils sont configurés dans le module `app` `build.gradle` :

```
buildTypes {    release {        minifyEnabled enableProguardInReleaseBuilds        proguardFiles getDefaultProguardFile("proguard-android.txt"), "proguard-rules.pro"    }}
```

Tout d'abord, changeons l'identifiant de l'application en `com.onmyway133.MyApp` pour correspondre à iOS. Ce n'est pas obligatoire, mais je pense que c'est bien de rester organisé. Ensuite, créez deux saveurs de produit pour le staging et la production. Pour le staging, ajoutons `.Staging` à l'identifiant de l'application.

À partir d'Android Studio 3, "toutes les saveurs doivent maintenant appartenir à une dimension de saveur nommée" — normalement, nous avons juste besoin de dimensions par défaut. Voici à quoi cela ressemble dans `build.gradle` pour notre module `app` :

```
android {    compileSdkVersion rootProject.ext.compileSdkVersion    buildToolsVersion rootProject.ext.buildToolsVersion    flavorDimensions "default"
```

```
defaultConfig {        applicationId "com.onmyway133.MyApp"        minSdkVersion rootProject.ext.minSdkVersion        targetSdkVersion rootProject.ext.targetSdkVersion        versionCode 1        versionName "1.0"        ndk {            abiFilters "armeabi-v7a", "x86"        }    }    splits {        abi {            reset()            enable enableSeparateBuildPerCPUArchitecture            universalApk false  // Si vrai, génère également un APK universel            include "armeabi-v7a", "x86"        }    }    buildTypes {        release {            minifyEnabled enableProguardInReleaseBuilds            proguardFiles getDefaultProguardFile("proguard-android.txt"), "proguard-rules.pro"        }    }
```

```
productFlavors {        staging {            applicationIdSuffix ".Staging"        }
```

```
        production {
```

```
        }    }}
```

Cliquez sur `Sync Now` pour laisser gradle faire le travail de synchronisation. Après cela, nous pouvons voir que nous avons quatre variantes de build :

![Image](https://cdn-media-1.freecodecamp.org/images/-nEATkMoAQykQ76AMDFzoYMzxU8DRidBmLm1)

#### Comment exécuter le staging et la production

Pour exécuter l'application Android, nous pouvons spécifier une variante comme `react-native run-android --variant=productionDebug`, mais je préfère aller dans Android Studio, sélectionner la variante et exécuter.

Pour exécuter l'application iOS, nous pouvons spécifier le schéma comme `react-native run-ios --simulator='iPhone X' --scheme="MyApp Staging"`. À partir de `react-native 0.57.0`, cela ne fonctionne pas. Mais cela n'a pas d'importance car je vais généralement dans Xcode, sélectionne le schéma et exécute.

#### Ajouter une icône d'application pour iOS

Selon les [Directives de l'interface humaine](https://developer.apple.com/design/human-interface-guidelines/ios/icons-and-images/app-icon/), nous avons besoin d'icônes d'application de différentes tailles pour différentes versions d'iOS, résolutions d'appareils et situations (notification, paramètres, Spring Board). J'ai créé un outil appelé [IconGenerator](https://github.com/onmyway133/IconGenerator), qui a été précédemment mentionné dans [Best Open Source Tools For Developers](https://dev.to/sarthology/best-open-source-tools-for-developers--300f). Glissez l'icône que vous voulez — je préfère celles avec 1024x1024 pixels pour les icônes d'application haute résolution — vers l'application MacOS Icon Generator.

![Image](https://cdn-media-1.freecodecamp.org/images/8ptxiQkjwO8gYHh2l5hOQ7jalJ1vMjmLUgu2)

Cliquez sur `Generate` et nous obtenons `AppIcon.appiconset`. Cela contient des icônes d'application des tailles requises qui sont prêtes à être utilisées dans le catalogue d'actifs. Glissez cela dans le catalogue d'actifs dans Xcode. C'est pour la production.

Pour le staging, il est bon de pratique d'ajouter une bannière "Staging" afin que les testeurs sachent lequel est le staging et lequel est la production. Nous pouvons facilement le faire dans Sketch.

![Image](https://cdn-media-1.freecodecamp.org/images/IZniQguM52R2egi9K3Q2RiSwDZJh1MGoIwQS)

N'oubliez pas de définir un arrière-plan, afin que nous n'ayons pas un arrière-plan transparent. Pour une icône d'application avec un arrière-plan transparent, iOS affiche l'arrière-plan en noir, ce qui est horrible.

Après avoir exporté l'image, glissez l'icône de staging vers l'IconGenerator de la même manière que nous l'avons fait précédemment. Mais cette fois, renommez le `appiconset` généré en `AppIcon-Staging.appiconset`. Ensuite, glissez cela dans le catalogue d'actifs dans Xcode.

Pour que la cible de staging utilise les icônes d'application de staging, ouvrez la cible `MyApp Staging` et choisissez `AppIcon-Staging` comme `App Icon Source`.

![Image](https://cdn-media-1.freecodecamp.org/images/gTgyPbp9meNYC3hGR14NOXkODGUCAXZuVwsg)

#### Ajouter une icône d'application pour Android

![Image](https://cdn-media-1.freecodecamp.org/images/XsdkrkclUz4Anzqe2rkViump5lmveYWNo02c)

Je préfère passer à la vue Projet, car il est plus facile de changer les icônes d'application. Cliquez sur `res -> New -> Image` Asset pour ouvrir Asset Studio. Nous pouvons utiliser les mêmes icônes d'application que celles utilisées dans iOS :

![Image](https://cdn-media-1.freecodecamp.org/images/40-HvrVL2bCPt8sYJEh0yIvwTQO-Us1MEpX7)

Android 8.0 (niveau d'API 26) a introduit des [icônes adaptatives](https://developer.android.com/guide/practices/ui_guidelines/icon_design_adaptive), nous devons donc ajuster le curseur de redimensionnement pour nous assurer que nos icônes d'application ont l'air aussi belles que possible.

> Android 8.0 (niveau d'API 26) introduit des icônes de lanceur adaptatives, qui peuvent afficher une variété de formes sur différents modèles de périphériques. Par exemple, une icône de lanceur adaptative peut afficher une forme circulaire sur un périphérique OEM et afficher un squircle sur un autre périphérique. Chaque fabricant de périphériques OEM fournit un masque, que le système utilise ensuite pour rendre toutes les icônes adaptatives avec la même forme. Les icônes de lanceur adaptatives sont également utilisées dans les raccourcis, l'application Paramètres, les dialogues de partage et l'écran de vue d'ensemble. — [Développeurs Android](https://developer.android.com/guide/practices/ui_guidelines/icon_design_adaptive)

Nous faisons d'abord pour la production, ce qui signifie le répertoire de ressources `main`. Cette étape remplacera les icônes d'application générées par Android Studio lorsque nous avons initialisé les projets React Native.

![Image](https://cdn-media-1.freecodecamp.org/images/Ejg8cMXAsfFGELEFjuDrHpW8xiJjNjOKZCPI)

Maintenant que nous avons les icônes d'application de production, créons les icônes d'application de staging. Android gère le code et les actifs via une convention. Cliquez sur `src -> New -> Directory` et créez un dossier `staging`. À l'intérieur de staging, créez un dossier appelé `res`. Tout ce que nous plaçons dans staging remplacera celui dans main — cela s'appelle des ensembles de sources.

![Image](https://cdn-media-1.freecodecamp.org/images/kwh1pi0dNor35pcf8sIVw1jSE8fhoNmFp9qu)

Vous pouvez en lire plus ici : [Build with source sets](https://developer.android.com/studio/build/build-variants).

> Vous pouvez utiliser des répertoires de jeux de sources pour contenir le code et les ressources que vous souhaitez empaqueter uniquement avec certaines configurations. Par exemple, si vous construisez la variante de build "demoDebug", qui est le produit croisé d'une saveur de produit "demo" et d'un type de build "debug", Gradle regarde ces répertoires et leur donne la priorité suivante :

> `src/demoDebug/` _(jeu de sources de la variante de build)_

> `src/debug/` _(jeu de sources du type de build)_

> `src/demo/` _(jeu de sources de la saveur de produit)_

> `src/main/` _(jeu de sources principal)_

Faites un clic droit sur `staging/res -> New -> Image` Asset pour créer des icônes d'application pour le staging. Nous utilisons également les mêmes icônes d'application de staging comme dans iOS, mais cette fois nous choisissons `staging` comme répertoire de ressources. De cette façon, Android Studio sait comment générer différentes icônes `ic_launcher` et les placer dans `staging`.

![Image](https://cdn-media-1.freecodecamp.org/images/ZDniqZf7J2-O9kGlNs4TCaK76wKrq5FWlLf4)

#### Ajouter un écran de démarrage pour iOS

L'écran de démarrage est appelé [Launch Screen](http://Launch Screen) dans iOS, et il est important.

> Un écran de démarrage apparaît instantanément lorsque votre application démarre. L'écran de démarrage est rapidement remplacé par le premier écran de votre application, donnant l'impression que votre application est rapide et réactive.

Dans le temps, nous devions utiliser des images de démarrage statiques de différentes tailles pour chaque appareil et orientation.

![Image](https://cdn-media-1.freecodecamp.org/images/vpvYxIfUWBNeC5qLkHAZu8LnIxPnUD5oi8UE)

#### Storyboard de l'écran de démarrage

Pour l'instant, la méthode recommandée est d'utiliser le `Launch Screen storyboard`. Le projet iOS de React Native est livré avec `LaunchScreen.xib`, mais `xib` est une chose du passé. Supprimons-le et créons un fichier appelé `Launch Screen.storyboard`.

Faites un clic droit sur le dossier `MyApp` -> Nouveau et choisissez Launch Screen, ajoutez-le aux deux cibles car nous montrons généralement le même écran de démarrage pour le staging et la production.

![Image](https://cdn-media-1.freecodecamp.org/images/GeAUVDHsi4usmEM1WAOIYfNKCTfMdVnk6K9u)

![Image](https://cdn-media-1.freecodecamp.org/images/fET7YnCtOakmd6bxa9EINtjvBvWDLAfIZwnd)

#### Jeu d'images

Ouvrez le catalogue d'actifs, faites un clic droit et sélectionnez `New Image Set`. Nous pouvons le nommer comme nous voulons. Cela sera utilisé dans le `Launch Screen.storyboard`.

![Image](https://cdn-media-1.freecodecamp.org/images/FOAnVwAIPlu9Sw0xTw2DKDN-D9zFRhUrgJfo)

Ouvrez Launch Screen.storyboard et ajoutez un `UIImageView`. Si vous utilisez Xcode 10, cliquez sur le bouton Bibliothèque dans le coin supérieur droit et choisissez `Show Objects Library`.

![Image](https://cdn-media-1.freecodecamp.org/images/ElDQfbXBrCnkgUv1bdTbFeSjp1FD531aCLKQ)

Définissez l'image pour Image View, et assurez-vous que `Content Mode` est défini sur `Aspect Filled`, car cela garantit que l'image couvre toujours tout l'écran (bien qu'elle puisse être rognée). Ensuite, connectez ImageView en utilisant des contraintes à la `View`, et non à la `Safe Area`. Vous faites cela en faisant `Control+drag` de l'Image View (splash) vers la `View`.

![Image](https://cdn-media-1.freecodecamp.org/images/djyPzopJFIhBCgNmR8NTzajn6yhiwWq1QCZF)

#### Contraintes sans marge

Cliquez sur chaque contrainte et décochez `Relative to Margin`. Cela fait en sorte que notre ImageView soit épinglée aux bords mêmes de la vue et sans aucune marge.

![Image](https://cdn-media-1.freecodecamp.org/images/Ca4SGVE43ZoYt2vO9xzEhCEM5OwUtYmG9IhL)

Maintenant, allez dans les deux cibles et sélectionnez `Launch Screen.storyboard` comme `Launch Screen File` :

![Image](https://cdn-media-1.freecodecamp.org/images/tWdkNOVF8YocN9aSArVkKyTeqoLT8LkVquci)

Sur iOS, l'écran de démarrage est souvent mis en cache, donc vous ne verrez probablement pas les changements. Une façon d'éviter cela est de supprimer l'application et de la relancer.

#### Ajouter un thème de lanceur pour Android

Il existe [plusieurs](https://android.jlelse.eu/the-complete-android-splash-screen-guide-c7db82bce565) [façons](https://android.jlelse.eu/right-way-to-create-splash-screen-on-android-e7f1709ba154) d'ajouter un écran de démarrage pour Android, allant de l'utilisation de thèmes de lanceur, d'une activité Splash et d'un minuteur. Pour moi, un écran de démarrage raisonnable pour Android devrait être une image très minimale.

Comme il existe de nombreux appareils Android avec différents ratios et résolutions, si vous souhaitez afficher une image de démarrage en plein écran, elle ne s'adaptera probablement pas correctement à chaque appareil. Cela concerne simplement l'UX.

Pour l'écran de démarrage, utilisons le thème de lanceur avec `splash_background.xml`.

#### Apprendre les métriques des appareils

Il n'existe pas une seule image de démarrage qui convienne à tous les appareils Android. Une approche plus logique consiste à créer plusieurs images de démarrage pour toutes les résolutions courantes en portrait et en paysage. Ou nous pouvons concevoir une image de démarrage minimale qui fonctionne. Vous pouvez trouver plus d'informations ici : [Device Metric](https://material.io/tools/devices/).

![Image](https://cdn-media-1.freecodecamp.org/images/7sCUEag7s1Bd6XQT5xUzl06wK0Fe8LMINn1f)

![Image](https://cdn-media-1.freecodecamp.org/images/W1QM52Nl-syNrLkP8DvrOtC3hc2pGVye2ZCK)

Voici comment ajouter un écran de démarrage en 4 étapes faciles :

#### Ajouter une image de démarrage

Nous avons généralement besoin d'un écran de démarrage commun pour le staging et la production. Glissez une image dans `main/res/drawable`. Android Studio semble avoir un problème avec la reconnaissance de certaines images jpg pour l'écran de démarrage, il est donc préférable de choisir des images png.

#### Ajouter splash_background.xml

Faites un clic droit sur `drawable -> New -> Drawable resource file`. Nommez-le comme vous voulez — je choisis `splash_background.xml`. Choisissez l'élément racine comme `layer-list` :

![Image](https://cdn-media-1.freecodecamp.org/images/ZpgiZzFrcfGgJ9z1PPdmrkrSU5CqIhEEeq1E)

![Image](https://cdn-media-1.freecodecamp.org/images/lCEe4-zJ4J3-xPuKXnG9TRbFqL1F0NpI8lxO)

Une [Layer List](http://Layer List) signifie "un Drawable qui gère un tableau d'autres Drawables. Ceux-ci sont dessinés dans l'ordre du tableau, donc l'élément avec le plus grand indice est dessiné au-dessus". Voici à quoi ressemble `splash_background.xml` :

```
<?xml version="1.0" encoding="utf-8"?><!-- La ligne android:opacity="opaque" est cruciale pour éviter un flash noir lors de la transition de votre thème. --><layer-list xmlns:android="http://schemas.android.com/apk/res/android"    android:opacity="opaque">    <!-- La couleur de fond, de préférence la même que votre thème normal -->    <item android:drawable="@android:color/white"/>    <!-- Votre image de démarrage -->    <item>        <bitmap            android:src="@drawable/iron_man"            android:gravity="center"/>    </item></layer-list>
```

Notez que nous pointons vers notre image de démarrage que nous avons ajoutée précédemment avec `android:src="@drawable/iron_man"`.

#### Déclarer le style

Ouvrez `styles.xml` et ajoutez `SplashTheme` :

```
<style name="SplashTheme" parent="Theme.AppCompat.NoActionBar">    <item name="android:windowBackground">@drawable/splash_background</item></style>
```

#### Utiliser SplashTheme

Allez dans `Manifest.xml` et changez le thème de l'activité de lanceur, qui a `category android:name="android.intent.category.LAUNCHER"`. Changez-le en `android:theme="@style/SplashTheme"`. Pour React Native, l'activité de lanceur est généralement `MainActivity`. Voici à quoi ressemble `Manifest.xml` :

```
<manifest xmlns:android="http://schemas.android.com/apk/res/android"    package="com.myapp">    <uses-permission android:name="android.permission.INTERNET" />    <uses-permission android:name="android.permission.SYSTEM_ALERT_WINDOW"/>    <application      android:name=".MainApplication"      android:label="@string/app_name"      android:icon="@mipmap/ic_launcher"      android:allowBackup="false"      android:theme="@style/AppTheme">      <activity        android:name=".MainActivity"        android:label="@string/app_name"        android:configChanges="keyboard|keyboardHidden|orientation|screenSize"        android:theme="@style/SplashTheme"        android:windowSoftInputMode="adjustResize">        <intent-filter>            <action android:name="android.intent.action.MAIN" />            <category android:name="android.intent.category.LAUNCHER" />        </intent-filter>      </activity>      <activity android:name="com.facebook.react.devsupport.DevSettingsActivity" />    </application></manifest>
```

Exécutez l'application maintenant et vous devriez voir l'écran de démarrage s'afficher lorsque l'application démarre.

### Gestion des configurations d'environnement

Les différences entre le staging et la production concernent principalement les noms d'application, les identifiants d'application et les icônes d'application. Nous utilisons probablement différentes clés API et URL de backend pour le staging et la production.

Actuellement, la bibliothèque la plus populaire pour gérer ces scénarios est [react-native-config](https://github.com/luggit/react-native-config), qui est censée "apporter un peu d'amour 12 facteurs à vos applications mobiles". Elle nécessite de nombreuses étapes pour commencer, et j'espère qu'il existe une solution moins verbeuse.

#### Où aller à partir de là

Dans cet article, nous avons utilisé Xcode et Android Studio plus que Visual Studio Code, mais cela était inévitable. J'espère que cet article vous a été utile. Voici quelques liens supplémentaires pour en savoir plus sur ce sujet :

* [Ajouter des icônes d'application et des écrans de démarrage aux applications React Native (iOS & Android)](https://medium.com/@scottianstewart/react-native-add-app-icons-and-launch-screens-onto-ios-and-android-apps-3bfbc20b7d4c)
* [Comment ajouter un écran de démarrage à une application React Native (iOS et Android)](https://medium.com/handlebar-labs/how-to-add-a-splash-screen-to-a-react-native-app-ios-and-android-30a3cec835ae)
* [Gestion de la configuration dans React Native](https://medium.com/differential/managing-configuration-in-react-native-cd2dfb5e6f7b)
* [Ajout de plusieurs pipelines de cibles pour les applications React Native (et déploiement Fastlane CircleCI) pt. 1](https://medium.com/@jacks205/adding-multiple-target-pipelines-for-react-native-apps-and-fastlane-circleci-deployment-pt-1-ae9590ae52f2)
* [Le guide (complet) de l'écran de démarrage Android](https://android.jlelse.eu/the-complete-android-splash-screen-guide-c7db82bce565)

Si vous avez aimé cet article, envisagez de visiter [mes autres articles](https://github.com/onmyway133/blog/issues/165) et [mes applications](https://onmyway133.github.io/) ?