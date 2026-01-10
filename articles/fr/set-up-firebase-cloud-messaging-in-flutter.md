---
title: Comment configurer Firebase Cloud Messaging dans Flutter en utilisant Firebase
subtitle: ''
author: Arunachalam B
co_authors: []
series: null
date: '2023-07-05T16:38:21.000Z'
originalURL: https://freecodecamp.org/news/set-up-firebase-cloud-messaging-in-flutter
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/A-Complete-Guide-to-FCM-Integration-in-Flutter-Using-Firebase.png
tags:
- name: Android
  slug: android
- name: Firebase
  slug: firebase
- name: Flutter
  slug: flutter
- name: mobile app development
  slug: mobile-app-development
seo_title: Comment configurer Firebase Cloud Messaging dans Flutter en utilisant Firebase
seo_desc: "In today's highly competitive mobile app landscape, effectively engaging\
  \ your app's users and delivering timely information is key. \nFirebase Cloud Messaging\
  \ (FCM) is a powerful push notification service provided by Firebase. It offers\
  \ a seamless way..."
---

Dans le paysage hautement concurrentiel des applications mobiles d'aujourd'hui, engager efficacement les utilisateurs de votre application et leur fournir des informations en temps opportun est essentiel.

Firebase Cloud Messaging (FCM) est un service puissant de notifications push fourni par Firebase. Il offre un moyen transparent de se connecter avec les utilisateurs de votre application et de les maintenir engagés.

Dans ce tutoriel, nous allons approfondir l'intégration de FCM dans Flutter. Nous explorerons ses avantages et présenterons des exemples concrets de la manière dont il peut améliorer l'engagement des utilisateurs et les performances de l'application.

## Qu'est-ce que Firebase Cloud Messaging ?

Firebase Cloud Messaging (FCM) fournit une connexion fiable et économe en batterie entre votre serveur et les appareils. Il vous permet d'envoyer et de recevoir des messages et des notifications sur iOS, Android et le web sans frais.

Dans ce tutoriel, nous allons explorer le processus de configuration et d'utilisation de Firebase Cloud Messaging (FCM) dans Flutter en utilisant Firebase comme service backend. Bien que l'accent principal sera mis sur l'implémentation Android, il est important de noter que le processus est similaire pour iOS et Android (avec quelques différences de configuration).

Voici ce que nous allons couvrir :

1. Comment créer une application dans Firebase
2. Comment configurer Firebase dans Flutter
3. Comment implémenter les notifications push en utilisant les jetons FCM

Dans ce tutoriel, vous apprendrez comment envoyer une notification simple en utilisant Firebase à l'application en cours d'exécution dans Flutter. Commençons.

## Comment créer une application dans Firebase

Je vais créer un nouveau projet dans la console Firebase pour commencer. Je vais passer par les étapes nécessaires, y compris la configuration du projet, comment configurer Firebase Cloud Messaging, et comment obtenir les informations d'identification et les fichiers de configuration requis pour notre application Flutter.

Avant de créer l'application, vous devez vous inscrire à la console Firebase (https://console.firebase.google.com/) si vous n'avez pas de compte. Après l'inscription, essayez de créer un projet.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-292.png)
_Créer un projet dans Firebase_

Cela prendra un peu de temps pour créer un projet.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-293.png)
_Création de projet dans Firebase_

Après avoir créé le projet, il vous redirigera vers le tableau de bord du projet.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-2.png)
_Aperçu du projet dans la console Firebase_

Une fois que vous avez créé le projet dans la console Firebase, il est temps de commencer avec notre application Flutter.

## Comment configurer Firebase dans Flutter

J'ai créé un projet Flutter simple en utilisant Visual Studio Code. Si vous n'êtes pas familier avec la création d'un projet Flutter, vous pouvez vous référer à mon [tutoriel précédent](https://www.freecodecamp.org/news/how-to-build-a-simple-login-app-with-flutter/). (Si vous êtes déjà familier, vous pouvez sauter cette étape.)

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-296.png)
_Application Flutter simple en cours d'exécution sur un appareil Android_

Intégrons Firebase dans notre projet Flutter. Pour ce faire, nous avons besoin de l'outil de ligne de commande Firebase CLI. J'ai déjà installé le Firebase CLI. Si vous ne l'avez pas fait, vous pouvez vous référer à la [documentation officielle](https://firebase.google.com/docs/cli#setup_update_cli).

Ensuite, nous devons nous connecter à Firebase en utilisant Firebase CLI.

```
firebase login
```

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-305.png)
_Connexion à Firebase en utilisant FirebaseCLI_

Cela vous redirigera vers le navigateur pour vous connecter à Firebase. Vous serez redirigé une fois l'authentification terminée avec succès.

Après une connexion réussie, nous devons installer FlutterFire CLI. Nous pouvons utiliser le FlutterFire CLI pour configurer nos applications Flutter pour se connecter à Firebase. Exécutez la commande suivante pour activer le FlutterFire CLI :

```
dart pub global activate flutterfire_cli
```

Le FlutterFire CLI est un outil d'interface de ligne de commande qui simplifie l'intégration des services Firebase dans les applications Flutter. Il fournit un moyen pratique d'ajouter, de configurer et de gérer les plugins Firebase dans notre projet Flutter.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-306.png)
_Installation de FlutterFireCLI_

L'étape suivante consiste à ajouter la bibliothèque `firebase_core` à notre projet Flutter.

La commande suivante ajoutera automatiquement le package `firebase_core` en tant que dépendance dans le fichier `pubspec.yaml` de votre projet et récupérera la dernière version du package depuis `pub.dev`. Après avoir exécuté cette commande, vous pouvez importer le package `firebase_core` dans les fichiers Dart et utiliser les services Firebase dans notre application Flutter.

```
flutter pub add firebase_core
```

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-307.png)
_Installation du package Firebase Core_

La commande `flutterfire configure` est utilisée pour configurer les services Firebase dans notre projet Flutter en utilisant le FlutterFire CLI. Cette commande nous aide à configurer l'authentification Firebase, Firestore, Cloud Messaging et d'autres services Firebase facilement et efficacement.

```
flutterfire configure
```

La première étape consiste à choisir le projet,

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-308.png)
_Connecter l'application Flutter avec l'application Firebase_

Ensuite, il faut choisir la plateforme. Je l'utilise pour Android ici, donc je choisis Android.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-309.png)
_Choix de la plateforme_

Après la configuration réussie, l'ID de l'application Firebase sera affiché.

Enfin, nous devons ajouter quelques modifications de code à notre fichier `main.dart`.

Importez les packages suivants :

```
import 'package:firebase_core/firebase_core.dart';
import 'firebase_options.dart';
```

Ajoutez la configuration suivante pour initialiser la configuration Firebase à l'intérieur de la fonction principale du fichier `main.dart`.

```
await Firebase.initializeApp(
  options: DefaultFirebaseOptions.currentPlatform,
);
```

Très bien, nous avons réussi à terminer la configuration Firebase dans notre application Flutter ! Prenons un moment pour célébrer cette étape. Configurer les services Firebase est une étape cruciale dans la construction d'applications puissantes et riches en fonctionnalités.

## Comment implémenter les notifications push en utilisant les jetons FCM

Nous allons implémenter le processus d'enregistrement des appareils pour les notifications push et de récupération des jetons FCM uniques attribués à chaque appareil. Cette étape est cruciale pour envoyer des notifications ciblées à des appareils spécifiques.

Nous allons plonger dans l'implémentation de l'envoi de notifications push aux appareils en utilisant Firebase Cloud Messaging. Nous allons explorer comment structurer et envoyer des messages de notification depuis la console Firebase et démontrer comment gérer ces messages dans notre application Flutter.

```
flutter pub add firebase_messaging
```

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-310.png)
_Installation du package de messagerie Firebase_

Ensuite, nous devons déclencher la fonction `setAutoInitEnabled` pour activer l'initialisation automatique de Firebase Cloud Messaging (FCM) dans notre application Flutter. Cela signifie que FCM s'initialisera automatiquement et récupérera un jeton d'appareil lorsque l'application démarrera.

Ajoutez l'appel de fonction suivant dans la méthode `main` :

```
import 'package:firebase_messaging/firebase_messaging.dart';
...
...
await FirebaseMessaging.instance.setAutoInitEnabled(true);
```

Lançons notre application Flutter et vérifions si nous recevons la notification.

Accédez à la console de messagerie Firebase (https://console.firebase.google.com/project/_/messaging/?_gl=1*gqfrc0*_ga*NDUwNTM5NDI0LjE2ODgwNTc3NjQ.*_ga_CW55HF8NVT*MTY4ODA5ODkyMC4yLjEuMTY4ODEwMjY2NS4wLjAuMA..). Comme c'est notre premier message, nous devons sélectionner "Créer votre première campagne". Sélectionnez "Messages de notification Firebase" et cliquez sur "Créer".

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-311.png)
_Modèle de messagerie de test d'exemple_

Maintenant, nous devons entrer le titre de la notification, le texte et le nom du message.

Ensuite, nous pouvons obtenir le jeton FCM manuellement à des fins de test en utilisant le code ci-dessous. Pour récupérer le jeton d'enregistrement actuel pour une instance d'application, appelez `getToken()` dans la méthode `main()`. Cette méthode demandera à l'utilisateur les autorisations de notification si l'autorisation de notification n'a pas été accordée. Sinon, elle retourne un jeton ou rejette s'il y a une erreur.

```
final fcmToken = await FirebaseMessaging.instance.getToken();
log("FCMToken $fcmToken");
```

Copiez le jeton FCM imprimé sur la console et collez-le dans la zone de saisie "Ajouter un jeton d'enregistrement FCM".

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-1.png)
_Message de test envoyé en utilisant le jeton FCM_

Cliquez sur le bouton Test. L'appareil client ciblé (avec l'application en arrière-plan) devrait recevoir la notification.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image.png)
_Notification push reçue sur l'appareil Android_

Hourra ! Nous avons reçu la notification sur notre appareil Android. Si nous cliquons sur la notification, elle ouvrira l'application par défaut.

Lorsque nous appuyons sur une notification, le comportement par défaut sur Android et iOS est d'ouvrir l'application. Si l'application est terminée, elle sera démarrée. Si elle est en arrière-plan, elle sera amenée au premier plan.

Ici, nous pouvons voir la configuration de base pour initialiser la messagerie Firebase.

`main.dart`

```

import 'package:flutter/material.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_messaging/firebase_messaging.dart';
import 'firebase_options.dart';

void main() async {
  runApp(const MyApp());
  await Firebase.initializeApp(
    options: DefaultFirebaseOptions.currentPlatform,
  );
  final fcmToken = await FirebaseMessaging.instance.getToken();
  await FirebaseMessaging.instance.setAutoInitEnabled(true);
  log("FCMToken $fcmToken");
}
```

## Conclusion

Dans ce tutoriel, nous avons couvert les étapes essentielles pour implémenter les notifications push dans Flutter en utilisant Firebase Cloud Messaging (FCM).

En suivant les étapes décrites, vous pouvez configurer Firebase, l'intégrer dans votre projet Flutter et implémenter la fonctionnalité de notification push.

Avec la capacité d'envoyer et de recevoir des notifications de manière transparente, vous pouvez améliorer l'expérience utilisateur et engager efficacement les utilisateurs de votre application. Restez à l'écoute pour des sujets et fonctionnalités plus avancés dans les futurs tutoriels.

Si vous souhaitez en savoir plus sur Flutter, abonnez-vous à ma [newsletter par email](https://5minslearn.gogosoon.com/?ref=fcc_flutter_firebase) ([https://5minslearn.gogosoon.com/](https://5minslearn.gogosoon.com/?ref=fcc_flutter_firebase)) et suivez-moi sur les réseaux sociaux.