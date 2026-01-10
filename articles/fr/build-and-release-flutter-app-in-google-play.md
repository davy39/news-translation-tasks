---
title: Comment créer et publier une application Flutter sur Google Play
subtitle: ''
author: Arunachalam B
co_authors: []
series: null
date: '2023-08-30T14:23:42.000Z'
originalURL: https://freecodecamp.org/news/build-and-release-flutter-app-in-google-play
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/Build-and-Release-the-Flutter-App-in-Google-Play.png
tags:
- name: android app development
  slug: android-app-development
- name: Flutter
  slug: flutter
seo_title: Comment créer et publier une application Flutter sur Google Play
seo_desc: "In the rapidly evolving world of mobile app development, Flutter has gained\
  \ immense popularity for its ability to create stunning and high-performance apps\
  \ across multiple platforms. \nFlutter's framework allows developers to build beautiful\
  \ user inte..."
---

Dans le monde en rapide évolution du développement d'applications mobiles, Flutter a gagné une immense popularité pour sa capacité à créer des applications magnifiques et haute performance sur plusieurs plateformes. 

Le framework de Flutter permet aux développeurs de créer de belles interfaces utilisateur, d'offrir des performances natives et de rationaliser le développement. 

Dans ce tutoriel, je vais vous guider à travers la création et la publication d'une application Flutter sur la plateforme Android, depuis la configuration de votre environnement de développement jusqu'à la distribution de votre application sur le Google Play Store.

## Prérequis :

1. **Installer Flutter et Dart** : Assurez-vous d'avoir Flutter et Dart installés sur votre machine. Suivez le [guide d'installation officiel de Flutter](https://docs.flutter.dev/get-started/install) pour votre plateforme.
2. **Android Studio** : Téléchargez et installez Android Studio, qui comprend des outils utiles pour le développement d'applications Android.
3. **Compte Développeur Google Play** : Créez un compte sur la Google Play Console pour publier votre application sur le Play Store.

## Comment développer votre application

Dans ce guide, je vais créer et publier une [application todo simple](https://www.freecodecamp.org/news/learn-state-management-in-flutter/) que j'ai construite dans l'un de mes blogs précédents.

Cependant, vous pouvez suivre ce tutoriel et publier votre propre application basée sur ce que vous construisez. 

En tant qu'apprenant, et si vous souhaitez expérimenter le processus de publication d'une application, ce sera une bonne pratique pour vous.

Exécutez la commande suivante pour cloner mon dépôt :

```
git clone https://github.com/5minslearn/Flutter-Todo-App
```

Avant de procéder au processus de création de l'application, il est crucial de s'assurer que notre application fonctionne sans erreur sur un simulateur ou un appareil physique. 

Ouvrez le dépôt dans VS Code et appuyez sur F5 pour exécuter l'application sur votre téléphone / émulateur. 

## Comment personnaliser l'icône de lancement par défaut dans Flutter

Lorsqu'une nouvelle application Flutter est créée, elle a une icône de lancement par défaut. 

Pour personnaliser cette icône, nous devons suivre les étapes ci-dessous : 

1. Vous pouvez créer votre propre icône en suivant cette [directive](https://m3.material.io/styles/icons).
2. Dans le répertoire `[projet]/android/app/src/main/res/`, placez vos fichiers d'icône dans des dossiers. Les dossiers `mipmap-` par défaut démontrent la convention de nommage correcte.
3. Dans `AndroidManifest.xml`, mettez à jour les balises d'application de l'attribut `android:icon` pour référencer les icônes de l'étape précédente (par exemple, `<application android:icon="@mipmap/custom_icon" ...`).

J'ai créé une icône nommée `custom_icon.xml` avec plusieurs résolutions (`mdpi`, `hdpi`, `xhdpi`, `xxhdpi`, `xxxhdpi`) :

```
48 × 48 (mdpi)
72 × 72 (hdpi)
96 × 96 (xhdpi)
144 × 144 (xxhdpi)
192 × 192 (xxxhdpi)
```

J'ai également placé chaque icône dans le dossier `mipmap-` respectif. Et enfin, je les ai mentionnées dans le `AndroidManifest.xml` :

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-169.png)
_Mise à jour de custom_icon dans AndroidManifest.xml_

```
<manifest xmlns:android="http://schemas.android.com/apk/res/android" package="com.example.todo" >
    <application
        android:label="todo"
        android:name="${applicationName}"
        android:icon="@mipmap/custom_icon">
        .....
        .....
    </application>
</manifest>

```

J'utilise `ColorControlNormal` dans mon fichier d'icône personnalisé (`custom_icon.xml`) :

```
<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="48dp"
    android:height="48dp"
    android:viewportWidth="960"
    android:viewportHeight="960"
    android:tint="?attr/colorControlNormal">
  <path
      android:fillColor="@android:color/white"
      android:pathData="M380,....,453.5Q592,463 613,483Z"/>
</vector>

```

**`colorControlNormal`** est une valeur qui fait référence à un attribut de couleur qui est résolu à l'exécution, permettant au dessinable de correspondre au thème de couleur de l'application.

Comme j'utilise une ancienne version de l'API, cette fonction n'est pas accessible dans l'ancienne API. 

En tant que solution, j'ai inclus la bibliothèque `appcompat` dans mon fichier `app/build.gradle` : 

```
...
dependencies {
    ....
    implementation 'androidx.appcompat:appcompat:1.3.1'
    ....
}
....
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-146.png)
_Implémentation de la bibliothèque appcombat dans `build.gradle`_

C'est tout. Nos configurations sont terminées. Essayons d'exécuter l'application et de regarder l'icône sur l'appareil.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-168.png)
_Icône de l'application modifiée pour l'application Todo_

Celle avec le visage du lapin est celle que j'ai créée. Elle a été appliquée avec succès à notre application. 

Sans plus tarder, passons à la création de notre application Android.

## Qu'est-ce qu'un Keystore et pourquoi en avez-vous besoin dans Flutter ?

Un keystore dans Flutter, spécifiquement pour Android, est un conteneur sécurisé utilisé pour stocker des clés cryptographiques et des certificats. 

Il est important de maintenir la sécurité de votre application, surtout lorsque vous traitez des informations sensibles telles que les clés API, les jetons d'authentification et les clés de chiffrement. 

Le keystore garantit que ces actifs sensibles sont stockés de manière à ce qu'ils soient difficiles à extraire de l'appareil.

### Sécurité

Stocker des informations sensibles dans un Keystore garantit qu'elles sont protégées contre les accès non autorisés, même si l'appareil est compromis.

### Conformité

De nombreuses réglementations exigent que les applications protègent les données sensibles. Un keystore vous aide à respecter les normes de conformité.

### Chiffrement

Si votre application utilise le chiffrement, le keystore fournit un emplacement sécurisé pour stocker les clés de chiffrement.

### Identifiants

Si votre application communique avec des API ou des services nécessitant des identifiants, l'utilisation d'un keystore peut empêcher ces identifiants d'être facilement extraits.

## Comment créer un Keystore dans Flutter

Pour créer un Keystore, vous utilisez généralement l'utilitaire keytool qui vient avec le Java Development Kit (JDK) :

```
keytool -genkey -v -keystore my-release-key.jks -keyalg RSA -keysize 2048 -validity 10000 -alias my-key
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-170.png)
_Exemple de sortie pour générer un fichier keystore_

## **Comment générer un APK ou un AAB dans Flutter**

APK (Android Package) et AAB (Android App Bundle) sont des formats de distribution utilisés pour empaqueter et distribuer des applications Android. 

Il est recommandé de créer une application en tant qu'AAB plutôt qu'en APK en raison des avantages suivants :

* Téléchargements plus petits et installations plus rapides grâce aux APK optimisés
* Efficacité améliorée dans l'utilisation des ressources et réduction de la consommation de stockage
* Prise en charge de la livraison dynamique des fonctionnalités pour fournir des fonctionnalités à la demande
* Optimisation améliorée pour des configurations d'appareils spécifiques

```
flutter build appbundle
ou
flutter build apk
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-171.png)
_Exemple de sortie pour créer un AAB_

Nous ne pouvons pas installer directement un fichier Android App Bundle (AAB) sur un appareil mobile.

Un AAB n'est pas un package exécutable comme un fichier APK (Android Package) qui peut être installé directement sur un appareil. 

Au lieu de cela, l'AAB est un format de publication conçu pour une livraison optimisée sur le Google Play Store.

Lorsque vous publiez votre application sur le Google Play Store en utilisant un AAB, le Play Store l'utilise pour générer des APK adaptés à la configuration de chaque appareil utilisateur. 

Cette génération dynamique permet au Play Store de livrer uniquement les ressources et le code nécessaires pour un appareil spécifique, réduisant la taille de l'application et améliorant les performances lors de l'installation.

## Comment publier une application Flutter sur le Google Play Store

Pour publier notre application sur le Google Play Store, nous aurons besoin d'un compte développeur Google Play. Nous pouvons créer un compte en visitant ce [lien](https://play.google.com/console). 

Veuillez noter qu'il y a des frais d'inscription d'au moins 25 $ associés au processus.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-150.png)
_Tableau de bord Google Play pour créer une nouvelle application_

Cliquez sur le bouton Créer une application dans la section `Toutes les applications`. Entrez les détails de l'application dans le formulaire "Créer une application".

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-149.png)
_Création d'une application dans Google Play pour la publication_

Après avoir créé l'application, nous devons passer par plusieurs tâches pour publier l'application. 

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-151.png)
_Étapes pour tester l'application dans la console Google Play_

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-152.png)
_Étapes pour configurer l'application dans la console Google Play_

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-153.png)
_Étapes pour publier l'application dans la console Google Play_

Cependant, toutes ces étapes seront auto-explicatives. 

À chaque étape, vous serez invité à fournir des informations sur votre application, les publicités, la politique de confidentialité, et plus encore. 

Il est important de noter que vous ne pouvez procéder à la publication qu'après avoir terminé ces étapes. 

Assurez-vous de mentionner tout clairement. Surtout les questions sur la collecte de données. Car, à tout moment, si Google découvre que les informations prescrites sont fausses, votre application ne sera pas publiée ou sera retirée si elle est publiée. 

Après avoir terminé ces étapes, nous devons envoyer l'application pour examen. Notre application sera publiée une fois l'examen terminé par l'équipe Google Play. 

Il est important de noter qu'il y a une probabilité plus élevée que l'application soit rejetée si elle présente des problèmes de sécurité ou liés à la publicité. 

Par conséquent, assurez-vous de réviser minutieusement votre application pour vous assurer qu'elle n'a aucun problème potentiel dans la collecte de données. Cela contribuera à une expérience de publication d'application plus fluide et plus réussie.

## Conclusion

Tout au long de ce tutoriel, nous avons couvert le processus de changement de l'icône de l'application et de création d'une application Flutter pour Android. 

Bien que cet exemple fournisse une compréhension fondamentale du développement d'applications Flutter, il est important de noter que les complexités des applications du monde réel peuvent nécessiter des configurations personnalisées supplémentaires dans Android. 

Pour plus d'informations, je vous encourage à explorer la [documentation officielle](https://docs.flutter.dev/deployment/android), qui offre des conseils complets sur des aspects plus avancés.

J'espère que ce tutoriel vous a fourni des informations précieuses dans votre parcours Flutter.

Merci d'avoir investi votre temps, et bonne chance dans vos efforts de développement d'applications ! 

Si vous souhaitez en savoir plus sur Flutter, abonnez-vous à mes articles en visitant mon [site](https://5minslearn.gogosoon.com/?ref=fcc_flutter_publish_app) qui contient une liste consolidée de tous mes blogs.

Santé !