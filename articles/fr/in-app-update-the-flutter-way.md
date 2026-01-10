---
title: Mise à jour dans l'application - Comment informer les utilisateurs des mises
  à jour d'application dans Flutter
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2022-11-18T21:50:05.000Z'
originalURL: https://freecodecamp.org/news/in-app-update-the-flutter-way
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/clarisse-meyer-xXiKQ2AavlY-unsplash.jpg
tags:
- name: Android
  slug: android
- name: application
  slug: application
- name: Dart
  slug: dart
- name: Flutter
  slug: flutter
- name: iOS
  slug: ios
- name: mobile app development
  slug: mobile-app-development
seo_title: Mise à jour dans l'application - Comment informer les utilisateurs des
  mises à jour d'application dans Flutter
seo_desc: "When you roll out a new version of your application, you want your users\
  \ to know about it. Whether you fixed a critical bug, added a new feature, or the\
  \ application just runs smoother or faster – they need to know. \nAs application\
  \ developers, we want..."
---

Lorsque vous déployez une nouvelle version de votre application, vous souhaitez que vos utilisateurs en soient informés. Que vous ayez corrigé un bug critique, ajouté une nouvelle fonctionnalité, ou que l'application fonctionne simplement plus rapidement ou plus fluidement – ils doivent le savoir. 

En tant que développeurs d'applications, nous voulons que tous nos utilisateurs utilisent la version la plus récente de notre application.

Mais comment pouvons-nous nous assurer que les utilisateurs sont informés d'une nouvelle version de notre application ?

La réponse à cette question est assez simple : pourquoi ne pas les informer lorsqu'une nouvelle version de l'application est disponible ?

Vous pouvez le faire de diverses manières :

* Utiliser une notification push
* Les informer lorsque l'application est lancée

Nous ne traiterons pas des notifications push dans cet article. Au lieu de cela, nous nous concentrons sur la manière dont vous pouvez (en utilisant un ou deux packages) afficher une boîte de dialogue à vos utilisateurs pour les informer qu'une nouvelle version de l'application est disponible et comment gérer la mise à jour.

## Attendez, cela n'est-il pas déjà inclus ?

Vous pourriez penser que ce type de fonctionnalité devrait déjà être inclus dans les systèmes d'exploitation mobiles modernes. Et vous auriez raison – mais seulement pour Android.

iOS ne donne pas (actuellement) aux développeurs la possibilité de voir s'il y a une nouvelle version de l'application et d'informer les utilisateurs à ce sujet. Sur Android, vous avez la bibliothèque [In-App Update](https://developer.android.com/guide/playcore/in-app-updates/kotlin-java) qui fait partie des bibliothèques Google Play.

En raison de cela, et parce que Flutter supporte les deux plateformes, je vais passer en revue deux packages populaires qui vous aident à gérer les mises à jour de version de votre application :

1. [Upgrader](https://pub.dev/packages/upgrader)
2. [In App Update](https://pub.dev/packages/in_app_update)

Les deux peuvent vous donner le résultat souhaité, mais ils varient largement dans la manière dont ils le font.

Avant de commencer, **il est crucial de comprendre que vous devez avoir une version de votre application qui a été installée directement depuis le Google Play Store**. Cela est requis puisque les deux packages dépendent des services Google Play et de leur capacité à vérifier le propriétaire de l'application.

Si vous ne le faites pas, vous verrez l'erreur suivante lorsque vous essayez d'utiliser l'un des packages :

> _Install Error(-10): The app is not owned by any user on this device. An app is "owned" if it has been acquired from Play. (https://developer.android.com/reference/com/google/android/play/core/install/model/InstallErrorCode#ERROR_APP_NOT_OWNED)_

## Comment utiliser le package In App Update

D'emblée, vous devez savoir que ce package ne fonctionnera que sur Android. Cela est dû au fait qu'il repose sur la bibliothèque de mise à jour dans l'application pour son fonctionnement interne.

Ce package est essentiellement un wrapper pour la bibliothèque Android. Voici ses méthodes API exposées :

* `Future<AppUpdateInfo> checkForUpdate()` : Vérifie si une mise à jour est disponible
* `Future<AppUpdateResult> performImmediateUpdate()` : Effectue une mise à jour immédiate (plein écran)
* `Future<AppUpdateResult> startFlexibleUpdate()` : Démarre une mise à jour flexible (téléchargement en arrière-plan)
* `Future<void> completeFlexibleUpdate()` : Installe réellement une mise à jour flexible disponible

✍ Si vous souhaitez en savoir plus sur les différences entre une mise à jour immédiate ou une mise à jour flexible, rendez-vous [ici](https://developer.android.com/guide/playcore/in-app-updates).

### Comment configurer le package

Tout d'abord, ajoutez le package à votre fichier pubspec.yaml :

```yaml
dependencies:
  flutter:
    sdk: flutter
  in_app_update: ^3.0.0
```

Ensuite, exécutez pub get.

À l'intérieur de votre application, là où vous prévoyez d'effectuer la logique pour gérer les mises à jour dans l'application, ajoutez l'importation suivante :

```dart
import 'package:in_app_update/in_app_update.dart';
```

Nous devons d'abord ajouter une logique qui vérifie si notre application a une mise à jour. Pour cela, nous utiliserons la méthode **checkForUpdate**. Sa valeur de retour est un Future<AppUpdateInfo> qui contient des informations sur la disponibilité et la progression d'une mise à jour d'application.

Nous pouvons vérifier si une mise à jour est disponible en utilisant la propriété [updateAvailability](https://developer.android.com/reference/com/google/android/play/core/install/model/UpdateAvailability). Si une mise à jour est disponible, elle aura la valeur **UPDATE_AVAILABLE**. Ainsi, votre méthode pourrait ressembler à ceci :

```dart
InAppUpdate.checkForUpdate().then((updateInfo) {
  if (updateInfo.updateAvailability == UpdateAvailability.updateAvailable) {
      // Logique pour effectuer une mise à jour
  }
});
```

Ensuite, nous devons décider quel type de mise à jour nous voulons déclencher – soit une mise à jour flexible ou une mise à jour immédiate.

Opter pour une mise à jour immédiate devrait être réservé pour une mise à jour d'application qui est critique pour vos utilisateurs. Cela peut signifier une version qui corrige un bug critique ou offre une nouvelle fonctionnalité.

Pour démarrer une mise à jour immédiate, nous pouvons utiliser la méthode **performImmediateUpdate**. Cette méthode retourne une énumération [AppUpdateResult](https://developer.android.com/reference/com/google/android/play/core/ktx/AppUpdateResult) qui vous indique si la mise à jour a réussi ou non.

Avant d'appeler cette méthode, nous devons vérifier si nous sommes autorisés à exécuter une mise à jour immédiate. Nous le faisons en accédant au drapeau **immediateUpdateAllowed** sur l'objet AppUpdateInfo.

Si nous voulons déclencher une mise à jour flexible, nous utilisons la méthode **startFlexibleUpdate**. Cela s'exécute en arrière-plan et est similaire à la méthode de mise à jour immédiate. Elle retourne également une énumération AppUpdateResult.

Si dans ce scénario la mise à jour a réussi, nous devons appeler la méthode **completeFlexibleUpdate** pour installer la mise à jour de notre application.

Ainsi, si nous regardons l'extrait de code ci-dessus et ajoutons la logique pour les différents types de mises à jour, cela ressemblera à ceci :

```dart
InAppUpdate.checkForUpdate().then((updateInfo) {
  if (updateInfo.updateAvailability == UpdateAvailability.updateAvailable) {
      if (updateInfo.immediateUpdateAllowed) {
          // Effectuer une mise à jour immédiate
          InAppUpdate.performImmediateUpdate().then((appUpdateResult) {
              if (appUpdateResult == AppUpdateResult.success) {
                // Mise à jour de l'application réussie
              }
          });
      } else if (updateInfo.flexibleUpdateAllowed) {
        // Effectuer une mise à jour flexible
        InAppUpdate.startFlexibleUpdate().then((appUpdateResult) {
              if (appUpdateResult == AppUpdateResult.success) {
                // Mise à jour de l'application réussie
                InAppUpdate.completeFlexibleUpdate();
              }
          });
      }
  }
});
```

## Comment utiliser le package Upgrader

Contrairement à la première option, celle-ci offre une solution pour iOS et Android. Elle repose sur la collecte de données depuis le store et les vérifie par rapport aux données actuelles de l'application elle-même.

Au lieu d'avoir une API pour interroger les données, ce package dispose de widgets qui effectuent la logique en arrière-plan.

### Comment configurer le package

Tout d'abord, ajoutez le package à votre fichier pubspec.yaml :

```yaml
dependencies:
  flutter:
    sdk: flutter
  upgrader: ^5.0.0
```

Ensuite, exécutez pub get.

À l'intérieur de votre application, là où vous prévoyez d'effectuer la logique pour gérer les mises à jour dans l'application, ajoutez l'importation suivante :

```dart
import 'package:upgrader/upgrader.dart';
```

La principale différence entre ces deux options est simplement une question d'UI, alors choisissez celle qui vous convient le mieux.

Pour intégrer ce package, vous devrez envelopper votre widget body avec soit **UpgradeAlert** soit **UpgradeCard**. Voici un exemple :

```dart
class MyApp extends StatelessWidget {
  
  @override
  Widget build(BuildContext context) {
      return MaterialApp(
        title: applicationName,
        home: UpgradeAlert(                  /// <------------------
          child: MainPage(
              key: Key("YOUR_KEY"),
              title: applicationName
          ),
        )
      );
    }
}
```

Si une nouvelle version de votre application est disponible dans le store, vous verrez ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/1.jpg)

Pour tester les choses, assurez-vous d'ajouter ceci :

```dart
await Upgrader.clearSavedSettings()
```

dans votre méthode main dans votre fichier main.dart.

Juste pour que vous soyez au courant, il y a une tonne de configurations que vous pouvez définir pour le package Upgrader. Je vous recommande vivement d'aller les vérifier.

## Comment tester les packages

Quelle que soit la package que vous choisissez d'utiliser, vous devez savoir que votre logique fonctionne correctement.

Mais comment pouvez-vous faire cela sans publier une version officielle de votre application ? Vous pouvez utiliser l'option de test interne dans Google Play Console. En publiant une nouvelle version de votre application pour les testeurs internes, elle ne sera pas publique et vous permettra de tester la fonctionnalité de mise à jour.

Voici ce que vous devez faire :

1. Connectez-vous à votre compte Google Play Console et accédez à l'application sur laquelle vous travaillez pour avoir la logique de mise à jour
2. Sous Configuration → Partage d'application interne, allez dans Gérer les testeurs et assurez-vous d'autoriser les testeurs à télécharger et installer l'application partagée. Vous pouvez choisir de le faire via un lien ou par e-mail.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/1-1.jpg)

3. Ensuite, allez dans Test → Test interne et cliquez sur le bouton Créer une nouvelle version (en haut à droite).

![Image](https://www.freecodecamp.org/news/content/images/2022/11/1-2.jpg)

4. Une fois que vous avez effectué une version, vous pouvez revenir à la page principale de Test interne et cliquer sur l'onglet Testeurs. Là, vous verrez une liste contenant les e-mails des testeurs (vide pour l'instant). Cliquez sur l'icône de flèche bleue.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/1-3.jpg)

5. Dans cet écran, vous pouvez vous ajouter en tant que testeur interne (dans Ajouter des adresses e-mail).

![Image](https://www.freecodecamp.org/news/content/images/2022/11/1-4.jpg)

6. Lorsque vous avez terminé, vous pouvez revenir à la fenêtre de Test interne. Faites défiler vers le bas et vous verrez **Comment les testeurs rejoignent votre test** et vous verrez un bouton Copier le lien.

Vous pouvez maintenant cliquer sur le bouton et vous envoyer le lien afin de pouvoir télécharger la nouvelle version de votre application.

Si vous ne parvenez pas à effectuer l'une des étapes ci-dessus, le lien généré mènera à une page non trouvée (Erreur 404) :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/1-5.jpg)

Si vous avez tout fait avec succès, vous verrez ce qui suit lorsque vous cliquez sur le lien généré :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/1-6.jpg)

Si vous voyez cette erreur :

> _Install Error(-6): The download/install is not allowed, due to the current device state (e.g. low battery, low disk space, …). (https://developer.android.com/reference/com/google/android/play/core/install/model/InstallErrorCode#ERROR_INSTALL_NOT_ALLOWED)_

Cela peut signifier que vous exécutez votre application sur un appareil émulé et que vous devez avoir Google Play Store installé dessus et être connecté.

## Conclusion

J'ai écrit cet article parce que j'ai dû passer par le même processus lors de l'intégration du package de mise à jour dans l'application avec ma propre application.

Vous êtes les bienvenus pour la vérifier sur le [Google Play Store](https://play.google.com/store/apps/details?id=com.tomerpacific.birthday_calendar) :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/1-7.jpg)

Et voir le code source complet ici :

%[https://github.com/TomerPacific/BirthdayCalendar]

Merci d'avoir lu !