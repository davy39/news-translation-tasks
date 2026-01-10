---
title: Comment utiliser les notifications locales dans Flutter – Un tutoriel pour
  débutants
subtitle: ''
author: Atuoha Anthony
co_authors: []
series: null
date: '2025-06-27T17:40:05.981Z'
originalURL: https://freecodecamp.org/news/how-to-use-local-notifications-in-flutter
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1751036674586/f344992e-0d1c-4f91-9cfb-f70aac5b5d14.png
tags:
- name: Flutter
  slug: flutter
- name: flutter-aware
  slug: flutter-aware
seo_title: Comment utiliser les notifications locales dans Flutter – Un tutoriel pour
  débutants
seo_desc: Mobile applications often need to communicate important information to users,
  even when the app isn't actively running. Local notifications are an excellent way
  to achieve this, allowing you to display messages, reminders, or alerts directly
  on the u...
---

Les applications mobiles doivent souvent communiquer des informations importantes aux utilisateurs, même lorsque l'application n'est pas en cours d'exécution. Les **notifications locales** sont un excellent moyen d'y parvenir, permettant d'afficher des messages, des rappels ou des alertes directement sur l'appareil de l'utilisateur. Cet article explorera comment implémenter des notifications locales dans une application Flutter en utilisant le puissant package `awesome_notifications`.

Nous discuterons des raisons pour lesquelles vous pourriez vouloir utiliser des notifications locales, de leur importance dans les applications, puis nous fournirons un guide étape par étape sur leur création, leur planification et leur annulation. Nous passerons également en revue la configuration d'un projet Flutter et l'installation des dépendances nécessaires, avec des explications détaillées de chaque bloc de code.

## Table des matières

* [Pourquoi utiliser les notifications locales ?](#heading-pourquoi-utiliser-les-notifications-locales)
    
* [Prérequis](#heading-prerequis)
    
* [Exemple de projet](#heading-exemple-de-projet)
    
    * [Configurer le projet Flutter](#heading-configurer-le-projet-flutter)
        
    * [Configurer les dépendances du projet](#heading-configurer-les-dependances-du-projet)
        
    * [Ajouter les ressources du projet](#heading-ajouter-les-ressources-du-projet)
        
    * [Définir les constantes de l'application](#heading-definir-les-constantes-de-lapplication)
        
    * [Définir les couleurs de l'application](#heading-definir-les-couleurs-de-lapplication)
        
    * [Implémenter les utilitaires de notification](#heading-implementer-les-utilitaires-de-notification)
        
    * [Générer des identifiants uniques](#heading-generer-des-identifiants-uniques)
        
    * [Créer des composants UI réutilisables](#heading-creer-des-composants-ui-reutilisables)
        
    * [Construire les pages de l'application](#heading-construire-les-pages-de-notification)
        
    * [Initialiser et exécuter l'application](#heading-initialiser-et-executer-lapplication)
        
* [Conclusion](#heading-conclusion)
    

## Pourquoi utiliser les notifications locales ?

Les notifications locales jouent un rôle vital dans l'amélioration de l'engagement des utilisateurs et dans la fourniture d'une expérience utilisateur fluide. Voici quelques raisons clés d'incorporer des notifications locales dans votre application Flutter :

* **Amélioration de l'engagement des utilisateurs** : Les notifications aident à maintenir les utilisateurs engagés avec votre application en fournissant des informations, des mises à jour ou des rappels opportuns et pertinents. Par exemple, une application de fitness pourrait envoyer une notification rappelant à un utilisateur de journaliser son entraînement quotidien.
    
* **Maintien de l'attention des utilisateurs** : Dans un paysage d'applications encombré, les notifications servent de moyen pour capturer et maintenir l'attention des utilisateurs, garantissant qu'ils n'oublient pas votre application. Elles agissent comme des rappels doux pour ramener les utilisateurs dans l'application.
    
* **Expérience utilisateur améliorée** : Les notifications locales peuvent améliorer l'expérience utilisateur globale en fournissant des mises à jour en temps réel, des alertes ou des messages personnalisés sans nécessiter que l'utilisateur ouvre l'application. Pensez à une application météo envoyant une alerte concernant une tempête approchante.
    
* **Rappels de tâches** : Les applications doivent souvent rappeler aux utilisateurs des tâches, des événements ou des échéances spécifiques. Les notifications locales sont un moyen efficace d'alerter les utilisateurs de tels événements, comme une application de liste de tâches vous rappelant une tâche en retard.
    

## Prérequis

Avant de commencer, assurez-vous d'avoir installé les éléments suivants sur votre système :

* **Flutter SDK** : Assurez-vous d'avoir Flutter installé et configuré correctement. Vous pouvez suivre le guide d'installation officiel de Flutter pour votre système d'exploitation.
    
* **Dart SDK** : Dart est fourni avec Flutter, donc si vous avez Flutter installé, vous êtes prêt.
    
* **Un IDE** : Visual Studio Code ou Android Studio avec les plugins Flutter et Dart sont fortement recommandés pour une expérience de développement fluide.
    

Il sera également utile d'avoir une familiarité de base avec les widgets Flutter, la gestion d'état (en particulier `StatefulWidget`) et la programmation asynchrone (`async`/`await`).

## Exemple de projet

Dans ce projet, nous allons construire une application Flutter pour iOS et Android qui incorpore des notifications locales. Vous apprendrez comment planifier, annuler et réduire le nombre de notifications sur iOS, ainsi que comment déclencher des actions lorsqu'une notification est ouverte.

### Configurer le projet Flutter

Commençons par créer un projet Flutter. Ouvrez votre terminal ou invite de commande et exécutez les commandes suivantes :

```bash
flutter create app_notifications
cd app_notifications
```

* `flutter create app_notifications` : Cette commande crée un nouveau projet Flutter nommé `app_notifications`.
    
* `cd app_notifications` : Cette commande vous place dans le répertoire du projet nouvellement créé.
    

### Configurer les dépendances du projet

Maintenant, nous devons ajouter les packages nécessaires à notre projet. Ouvrez le fichier `pubspec.yaml` situé à la racine de votre projet et ajoutez les dépendances suivantes sous la section `dependencies` :

```yaml
dependencies:
  flutter:
    sdk: flutter
  flutter_launcher_icons: ^0.13.1
  awesome_notifications: ^0.9.2
  cool_alert: ^2.0.1
  awesome_notifications_core: ^0.9.1
```

**Explication des dépendances :**

* `flutter_launcher_icons` : Ce package permet de mettre à jour facilement l'icône de lancement de votre application Flutter pour Android et iOS. C'est un utilitaire pratique pour personnaliser votre application.
    
* `awesome_notifications` : Il s'agit du package principal que nous utiliserons pour gérer les notifications locales. Il fournit un ensemble complet de fonctionnalités pour créer, planifier et gérer les notifications.
    
* `cool_alert` : Ce package fournit des boîtes de dialogue d'alerte belles et personnalisables, que nous utiliserons pour les retours utilisateur dans notre application.
    
* `awesome_notifications_core` : Ce package contient les fonctionnalités principales de `awesome_notifications` et est souvent une dépendance du package principal `awesome_notifications`. L'inclure explicitement garantit que tous les composants nécessaires sont disponibles.
    

Ensuite, toujours dans votre fichier `pubspec.yaml`, configurez `flutter_launcher_icons` en ajoutant le code suivant sous la section `dev_dependencies` :

```yaml
flutter_icons:
  android: "launcher_icon"
  ios: true
  remove_alpha_ios: true
  image_path: "assets/imgs/icon.png"
  adaptive_icon_background: "#6C63FF"
  adaptive_icon_foreground: "assets/imgs/icon.png"
```

**Ce qui se passe dans la configuration de** `flutter_icons` **:**

* `android: "launcher_icon"` : Spécifie que l'icône de lancement Android doit être générée.
    
* `ios: true` : Active la génération d'icônes pour iOS.
    
* `remove_alpha_ios: true` : Supprime le canal alpha des icônes iOS, ce qui est souvent une exigence pour la soumission à l'App Store.
    
* `image_path: "assets/imgs/icon.png"` : Pointe vers le fichier image source pour votre icône d'application. Nous créerons ce chemin à l'étape suivante.
    
* `adaptive_icon_background: "#6C63FF"` : Définit la couleur de fond pour les icônes adaptatives Android. Cette couleur (`#6C63FF`) est une nuance de violet, que nous définirons également comme notre `primaryColor`.
    
* `adaptive_icon_foreground: "assets/imgs/icon.png"` : Définit l'image de premier plan pour les icônes adaptatives Android.
    

### Ajouter les ressources du projet

Les applications ont souvent besoin de ressources statiques comme des images. Ajoutez ce qui suit à votre fichier `pubspec.yaml` pour déclarer votre dossier de ressources :

```yaml
assets:
    - assets/imgs/
```

Cela indique à Flutter où trouver vos ressources d'image. Maintenant, créez un dossier nommé `assets` à la racine de votre projet, et à l'intérieur, créez un autre dossier nommé `imgs`. Placez vos fichiers image (`icon.png`, `cancel.png`, `eco.png`, `eco_large.png`, `network.png`, `res_notification_icon.png`, `rocket.png`, `stats.png`) dans ce dossier `imgs`.

Après avoir modifié `pubspec.yaml` et ajouté vos ressources, exécutez les commandes suivantes dans votre terminal pour appliquer les changements et générer les icônes de lancement :

```bash
flutter pub get
flutter pub run flutter_launcher_icons
```

* `flutter pub get` : Cette commande récupère toutes les nouvelles dépendances ajoutées et met à jour votre projet.
    
* `flutter pub run flutter_launcher_icons` : Cette commande exécute le package `flutter_launcher_icons` pour générer vos icônes d'application en fonction de la configuration que vous avez fournie.
    

### Définir les constantes de l'application

Il est bon de centraliser les chaînes de caractères et les clés fréquemment utilisées. À l'intérieur de votre répertoire `lib`, créez un dossier nommé `constants`. À l'intérieur de ce dossier, créez un fichier nommé `app_strings.dart` et ajoutez le code suivant :

```dart
class AppStrings {
  static const String BASIC_CHANNEL_KEY = 'basic_channel';
  static const String BASIC_CHANNEL_NAME = 'Notifications de base';
  static const String BASIC_CHANNEL_DESCRIPTION = 'Ce canal est pour les notifications de base';

  static const String SCHEDULE_CHANNEL_KEY = 'schedule_channel';
  static const String SCHEDULE_CHANNEL_NAME = 'Notifications planifiées';
  static const String SCHEDULE_CHANNEL_DESCRIPTION = 'Ce canal est pour les notifications planifiées';

  static const String DEFAULT_ICON = 'asset://assets/imgs/icon.png';

  static const String SCHEDULED_NOTIFICATION_BUTTON1_KEY = 'button_one';
  static const String SCHEDULED_NOTIFICATION_BUTTON2_KEY = 'button_two';
}
```

**Ce qui se passe dans** `AppStrings` **:**

Ce fichier contient des constantes de chaîne qui seront utilisées dans toute l'application. Ces constantes fournissent une source unique de vérité pour des valeurs comme :

* **Clés, noms et descriptions des canaux de notification** : Ceux-ci sont essentiels pour catégoriser et gérer les notifications sur Android. Chaque notification doit appartenir à un canal.
    
* `DEFAULT_ICON` : Une référence à notre icône de notification par défaut.
    
* `SCHEDULED_NOTIFICATION_BUTTON1_KEY` et `SCHEDULED_NOTIFICATION_BUTTON2_KEY` : Ces clés seront utilisées pour identifier les actions déclenchées par les boutons dans les notifications planifiées.
    

### Définir les couleurs de l'application

Pour une thématique cohérente, définissez la palette de couleurs de votre application en un seul endroit. À l'intérieur du dossier `constants`, créez un fichier nommé `colors.dart` et ajoutez le code suivant :

```dart
import 'dart:ui';

class AppColor {
  static const primaryColor = Color(0XFF6C63FF);
  static const secondaryColor = Color(0XFFF96685);
}
```

Ce fichier définit des constantes de couleur que vous pouvez utiliser pour une thématique cohérente dans votre application. `primaryColor` et `secondaryColor` seront utilisés dans divers éléments d'interface utilisateur pour maintenir une conception cohérente.

### Implémenter les utilitaires de notification

C'est ici que réside la logique principale pour gérer les notifications. Créez un dossier à l'intérieur de `lib` appelé `utilities`. À l'intérieur de ce dossier, créez un fichier nommé `notification_util.dart` et ajoutez le code suivant :

```dart
import 'dart:io';
import 'package:app_notifications/utilities/create_uid.dart';
import 'package:awesome_notifications/awesome_notifications.dart';
import 'package:flutter/material.dart';
import '../constants/app_strings.dart';
import '../constants/colors.dart';
import '../main.dart';
import '../pages/stats_page.dart';

class NotificationUtil {
  final AwesomeNotifications awesomeNotifications;

  NotificationUtil({required this.awesomeNotifications});

  /// Crée une notification de base qui apparaît immédiatement.
  Future<void> createBasicNotification({
    required int id,
    required String channelKey,
    required String title,
    required String body,
    String bigPicture = AppStrings.DEFAULT_ICON,
    NotificationLayout layout = NotificationLayout.BigPicture,
  }) async {
    awesomeNotifications.createNotification(
      content: NotificationContent(
        id: id,
        channelKey: channelKey,
        title: title,
        body: body,
        bigPicture: bigPicture,
        notificationLayout: layout,
      ),
    );
  }

  /// Crée une notification planifiée qui apparaîtra à une heure spécifique et peut se répéter.
  Future<void> createScheduledNotification({
    required int id,
    required String channelKey,
    required String title,
    required String body,
    String bigPicture = AppStrings.DEFAULT_ICON,
    NotificationLayout layout = NotificationLayout.BigPicture,
    required NotificationCalendar notificationCalendar,
  }) async {
    awesomeNotifications.createNotification(
      content: NotificationContent(
        id: id,
        channelKey: channelKey,
        title: title,
        body: body,
        bigPicture: bigPicture,
        notificationLayout: layout,
      ),
      actionButtons: [
        NotificationActionButton(
          key: AppStrings.SCHEDULED_NOTIFICATION_BUTTON1_KEY,
          label: 'Marquer comme fait',
        ),
        NotificationActionButton(
          key: AppStrings.SCHEDULED_NOTIFICATION_BUTTON2_KEY,
          label: 'Effacer',
        ),
      ],
      schedule: NotificationCalendar(
        weekday: notificationCalendar.weekday,
        hour: notificationCalendar.hour,
        minute: notificationCalendar.minute,
        repeats: true, // Cette notification se répétera chaque semaine le jour et l'heure spécifiés.
      ),
    );
  }

  /// Annule toutes les notifications planifiées actuellement.
  void cancelAllScheduledNotifications({required BuildContext context}){
    awesomeNotifications.cancelAllSchedules().then((value) => {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(
          content: Text('Toutes les notifications planifiées ont été annulées'),
          backgroundColor: AppColor.primaryColor,
        ),
      )
    });
  }

  /// Demande la permission à l'utilisateur d'envoyer des notifications. Cela est crucial pour Android 13+ et iOS.
  void requestPermissionToSendNotifications({required BuildContext context}) {
    AwesomeNotifications().requestPermissionToSendNotifications().then((value) {
      // Après avoir demandé la permission, fermez la boîte de dialogue qui a incité l'utilisateur.
      Navigator.of(context).pop();
    });
  }

  /// Méthodes statiques pour gérer les événements du cycle de vie des notifications.
  /// Ces méthodes sont marquées avec `@pragma("vm:entry-point")` pour s'assurer qu'elles sont accessibles
  /// même lorsque l'application est en cours d'exécution en arrière-plan ou fermée.

  /// Utilisez cette méthode pour détecter lorsqu'une nouvelle notification ou une planification est créée.
  @pragma("vm:entry-point")
  static Future<void> onNotificationCreatedMethod(
      ReceivedNotification receivedNotification, BuildContext context) async {
    // Affichez un SnackBar pour indiquer qu'une notification a été créée.
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Text(
          'Notification créée ${receivedNotification.channelKey}',
        ),
        backgroundColor: AppColor.primaryColor,
      ),
    );
  }

  /// Utilisez cette méthode pour détecter chaque fois qu'une nouvelle notification est affichée.
  @pragma("vm:entry-point")
  static Future<void> onNotificationDisplayedMethod(
      ReceivedNotification receivedNotification) async {
    // Votre code pour gérer l'affichage d'une notification peut aller ici.
    // Par exemple, vous pourriez journaliser l'événement ou mettre à jour un élément d'interface utilisateur.
  }

  /// Utilisez cette méthode pour détecter si l'utilisateur a ignoré une notification.
  @pragma("vm:entry-point")
  static Future<void> onDismissActionReceivedMethod(
      ReceivedAction receivedAction) async {
    // Votre code pour gérer l'ignorance d'une notification peut aller ici.
    // Cela est utile pour suivre l'interaction de l'utilisateur ou nettoyer les ressources.
  }

  /// Utilisez cette méthode pour détecter lorsque l'utilisateur appuie sur une notification ou un bouton d'action à l'intérieur.
  @pragma("vm:entry-point")
  static Future<void> onActionReceivedMethod(
      ReceivedAction receivedAction) async {
    // Réduction du compteur de badges d'icône sur iOS lorsqu'une notification de base est appuyée/agie.
    // Cela est important pour maintenir des compteurs de badges précis.
    if (receivedAction.channelKey == AppStrings.BASIC_CHANNEL_KEY &&
        Platform.isIOS) {
      AwesomeNotifications().getGlobalBadgeCounter().then((value) {
        AwesomeNotifications().setGlobalBadgeCounter(value - 1);
      });
    }

    // Navigation vers la StatsPage lorsqu'une action de notification est reçue.
    // La `navigatorKey` de `MyApp` est utilisée pour naviguer depuis n'importe où dans l'application.
    MyApp.navigatorKey.currentState?.pushAndRemoveUntil(
        MaterialPageRoute(
          builder: (context) => const StatsPage(),
        ),
        (route) => route.isFirst);
  }
}
```

**Ce qui se passe dans** `NotificationUtil` **:**

Cette classe est le cœur de notre logique de notification. Elle encapsule des méthodes pour :

* `createBasicNotification` : Cette fonction crée une notification simple et immédiate. Elle prend un `id`, `channelKey`, `title` et `body`. Les paramètres `bigPicture` et `layout` permettent un contenu de notification riche.
    
* `createScheduledNotification` : Cette fonction puissante permet de planifier des notifications pour qu'elles apparaissent à une date et une heure spécifiques. Elle inclut des `actionButtons` (comme "Marquer comme fait" ou "Effacer") avec lesquels les utilisateurs peuvent interagir directement depuis la notification, et un `NotificationCalendar` pour une planification précise avec `repeats: true` pour en faire une notification récurrente hebdomadaire.
    
* `cancelAllScheduledNotifications` : Un utilitaire pour annuler toutes les notifications qui ont été planifiées. Il affiche également un `SnackBar` pour le retour utilisateur.
    
* `requestPermissionToSendNotifications` : Cette méthode gère l'étape cruciale de demander à l'utilisateur la permission d'envoyer des notifications. Il s'agit d'une invite au niveau du système sur Android (surtout Android 13+) et iOS.
    
* **Méthodes d'écoute** (`onNotificationCreatedMethod`, `onNotificationDisplayedMethod`, `onDismissActionReceivedMethod`, `onActionReceivedMethod`) : Ces méthodes `static` sont des rappels que `awesome_notifications` invoque à différentes étapes du cycle de vie d'une notification. Elles sont marquées avec `@pragma("vm:entry-point")` pour s'assurer qu'elles peuvent s'exécuter même lorsque l'application est en arrière-plan ou complètement fermée.
    
    * `onNotificationCreatedMethod` : Déclenchée lorsqu'une nouvelle notification est créée.
        
    * `onNotificationDisplayedMethod` : Déclenchée lorsqu'une notification est effectivement affichée à l'utilisateur.
        
    * `onDismissActionReceivedMethod` : Déclenchée lorsque l'utilisateur ignore une notification.
        
    * `onActionReceivedMethod` : **C'est une méthode très importante.** Elle est déclenchée lorsque l'utilisateur appuie sur la notification elle-même ou sur l'un de ses boutons d'action. Dans notre implémentation, elle gère :
        
        * **Réduction du compteur de badges iOS** : Pour les notifications de base sur iOS, elle décrémente le compteur de badges de l'icône de l'application, fournissant un compteur de non lus plus précis.
            
        * **Navigation** : Elle dirige l'utilisateur vers la `StatsPage` quelle que soit l'action de notification reçue. Cela démontre comment vous pouvez diriger les utilisateurs vers des parties spécifiques de votre application en fonction de leur interaction avec la notification.
            

### Générer des identifiants uniques

Chaque notification a besoin d'un identifiant unique. À l'intérieur du dossier `utilities`, créez un fichier nommé `create_uid.dart` et ajoutez le code suivant :

```dart
int createUniqueId() {
  return DateTime.now().millisecondsSinceEpoch.remainder(100000);
}
```

`createUniqueId` est une fonction simple qui génère un identifiant unique entier en prenant l'horodatage actuel en millisecondes et en obtenant son reste lorsqu'il est divisé par 100000. Cela garantit un identifiant raisonnablement unique pour chaque notification sans créer de nombres excessivement grands.

### Créer des composants UI réutilisables

Pour maintenir un code propre et modulaire, nous allons créer plusieurs composants UI réutilisables. Créez un dossier nommé `components` à l'intérieur de `lib`. À l'intérieur de ce dossier, créez les fichiers suivants : `custom_alert_dialog.dart`, `custom_rich_text.dart`, `custom_elevated_button.dart`, `stats_container.dart`, et `k_cool_alert.dart`.

#### `custom_alert_dialog.dart` :

```dart
import 'dart:io';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import '../constants/colors.dart';

Future<void> customAlertDialog({
  required String title,
  required String content,
  required BuildContext context,
  required Function action,
  required String button1Title,
  required String button2Title,
}) {
  return showDialog(
    context: context,
    builder: (context) =>
        // POUR iOS
        Platform.isIOS
            ? CupertinoAlertDialog(
                title: Text(
                  title,
                  style: const TextStyle(
                    fontWeight: FontWeight.w700,
                    color: Colors.black,
                    fontSize: 16,
                  ),
                ),
                content: Text(content),
                actions: [
                  Padding(
                    padding: const EdgeInsets.all(8.0),
                    child: ElevatedButton(
                      style: ElevatedButton.styleFrom(
                        padding: const EdgeInsets.symmetric(horizontal: 5),
                        backgroundColor: AppColor.secondaryColor,
                        shape: RoundedRectangleBorder(
                          borderRadius: BorderRadius.circular(10),
                        ),
                      ),
                      onPressed: () => action(),
                      child: Text(
                        button1Title,
                        style: const TextStyle(
                          color: Colors.white,
                          fontWeight: FontWeight.normal,
                        ),
                      ),
                    ),
                  ),
                  Padding(
                    padding: const EdgeInsets.all(8.0),
                    child: ElevatedButton(
                      style: ElevatedButton.styleFrom(
                        padding: const EdgeInsets.symmetric(horizontal: 5),
                        backgroundColor: AppColor.secondaryColor,
                        shape: RoundedRectangleBorder(
                          borderRadius: BorderRadius.circular(10),
                        ),
                      ),
                      onPressed: () => Navigator.of(context).pop(),
                      child: Text(
                        button2Title,
                        style: const TextStyle(
                          color: Colors.white,
                          fontWeight: FontWeight.normal,
                        ),
                      ),
                    ),
                  ),
                ],
              )
            // POUR Android
            : AlertDialog(
                title: Text(
                  title,
                  style: const TextStyle(
                    fontWeight: FontWeight.w700,
                    color: Colors.black,
                    fontSize: 16,
                  ),
                ),
                content: Text(content),
                actions: [
                  ElevatedButton(
                    style: ElevatedButton.styleFrom(
                      backgroundColor: AppColor.secondaryColor,
                      padding: const EdgeInsets.symmetric(horizontal: 5),
                      shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(10),
                      ),
                    ),
                    onPressed: () => action(),
                    child: Text(
                      button1Title,
                      style: const TextStyle(
                        color: Colors.white,
                        fontWeight: FontWeight.normal,
                      ),
                    ),
                  ),
                  ElevatedButton(
                    style: ElevatedButton.styleFrom(
                      backgroundColor: AppColor.secondaryColor,
                      padding: const EdgeInsets.symmetric(horizontal: 5),
                      shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(10),
                      ),
                    ),
                    onPressed: () => Navigator.of(context).pop(),
                    child: Text(
                      button2Title,
                      style: const TextStyle(
                        color: Colors.white,
                        fontWeight: FontWeight.normal,
                      ),
                    ),
                  ),
                ],
              ),
  );
}
```

La fonction `customAlertDialog` fournit une boîte de dialogue d'alerte personnalisable qui adapte son apparence en fonction de la plateforme. Elle utilise `CupertinoAlertDialog` pour iOS pour fournir un look et une sensation natifs, et `AlertDialog` pour Android.

Cela garantit une expérience utilisateur cohérente sur différents appareils. Elle prend un `title`, `content`, `context`, une fonction `action` pour le bouton principal, et des titres pour les deux boutons.

#### `custom_rich_text.dart` :

```dart
import 'package:flutter/material.dart';

class CustomRichText extends StatelessWidget {
  const CustomRichText({
    Key? key,
    required this.title,
    required this.content,
  }) : super(key: key);

  final String title;
  final String content;

  @override
  Widget build(BuildContext context) {
    return RichText(
      text: TextSpan(
        text: title,
        style: TextStyle(
          color: Colors.grey.shade800,
          fontWeight: FontWeight.w800,
        ),
        children: [
          TextSpan(
            text: content,
            style: const TextStyle(
              color: Colors.grey,
            ),
          ),
        ],
      ),
    );
  }
}
```

Le widget `CustomRichText` est un simple composant `RichText` conçu pour afficher un `title` et un `content` avec différents styles de texte. Le `title` est en gras et gris foncé, tandis que le `content` est en gris plus clair, ce qui le rend idéal pour afficher des étiquettes et leurs valeurs correspondantes.

#### `custom_elevated_button.dart` :

```dart
import 'package:flutter/material.dart';
import '../constants/colors.dart';

class CustomElevatedButton extends StatelessWidget {
  const CustomElevatedButton({
    Key? key,
    required this.function,
    required this.title,
    required this.icon,
  }) : super(key: key);

  final Function function;
  final IconData icon;
  final String title;

  @override
  Widget build(BuildContext context) {
    return ElevatedButton.icon(
      style: ElevatedButton.styleFrom(
        backgroundColor: AppColor.secondaryColor,
      ),
      onPressed: () => function(),
      icon: Icon(
        icon,
        color: Colors.white,
      ),
      label: Text(
        title,
        style: const TextStyle(
          color: Colors.white,
        ),
      ),
    );
  }
}
```

Le widget `CustomElevatedButton` est un `ElevatedButton` réutilisable avec une icône et une étiquette de texte. Il prend une `function` à exécuter lorsqu'il est pressé, une `icon`, et un `title`. Il utilise notre `secondaryColor` pour son arrière-plan, assurant un look et une sensation cohérents pour les actions principales.

#### `k_cool_alert.dart` :

```dart
import 'package:cool_alert/cool_alert.dart';
import 'package:flutter/material.dart';
import '../constants/colors.dart';

Future kCoolAlert({
  required String message,
  required BuildContext context,
  required CoolAlertType alert,
  bool barrierDismissible = true,
  String confirmBtnText = 'Ok',
}) {
  return CoolAlert.show(
    backgroundColor: AppColor.primaryColor,
    confirmBtnColor: AppColor.secondaryColor,
    context: context,
    type: alert,
    text: message,
    barrierDismissible: barrierDismissible,
    confirmBtnText: confirmBtnText,
  );
}
```

La fonction `kCoolAlert` utilise le package `cool_alert` pour afficher des boîtes de dialogue d'alerte esthétiquement plaisantes. Elle permet de spécifier le `message`, `context`, `type d'alerte` (par exemple, succès, erreur, avertissement), si elle est `barrierDismissible`, et le `confirmBtnText`. Elle utilise notre `primaryColor` et `secondaryColor` pour le style.

#### `stats_container.dart` :

```dart
import 'package:flutter/material.dart';
import '../constants/colors.dart';

class StatsContainer extends StatelessWidget {
  StatsContainer({
    Key? key,
    required this.icon,
    required this.stat,
    this.iconColor = Colors.orange,
  }) : super(key: key);

  Color iconColor;
  final IconData icon;
  final String stat;

  @override
  Widget build(BuildContext context) {
    return Container(
      height: 40,
      width: 110,
      decoration: BoxDecoration(
        borderRadius: BorderRadius.circular(20),
        color: AppColor.secondaryColor,
      ),
      child: Center(
        child: Wrap(
          crossAxisAlignment: WrapCrossAlignment.center,
          spacing: 6,
          children: [
            Icon(
              icon,
              color: iconColor,
            ),
            Text(
              stat,
              style: const TextStyle(
                color: Colors.white,
                fontSize: 18,
                fontWeight: FontWeight.w700,
              ),
            )
          ],
        ),
      ),
    );
  }
}
```

Le widget `StatsContainer` est un simple conteneur conçu pour afficher une icône et une statistique numérique. Il présente un arrière-plan arrondi utilisant `AppColor.secondaryColor` et offre un moyen visuellement attrayant de présenter des métriques clés, comme nous le verrons sur la `StatsPage`.

### Construire les pages de l'application

Maintenant, créons les écrans principaux de notre application. Créez un nouveau dossier à l'intérieur de `lib` appelé `pages`. À l'intérieur de ce dossier, créez deux fichiers : `home_page.dart` et `stats_page.dart`.

#### `home_page.dart` :

```dart
import 'package:app_notifications/pages/stats_page.dart';
import 'package:awesome_notifications/awesome_notifications.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import '../components/custom_elevated_button.dart';
import '../components/custom_alert_dialog.dart';
import '../components/custom_rich_text.dart';
import '../constants/app_strings.dart';
import '../constants/colors.dart';
import '../utilities/create_uid.dart';
import '../utilities/notification_util.dart';

class HomePage extends StatefulWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  String selectedNotificationDay = '';
  int selectedDayOfTheWeek = 0;
  TimeOfDay selectedTime = TimeOfDay.now();
  bool isTimeSelected = false;
  late NotificationUtil notificationUtil;

  // liste des jours de notification
  final List<String> notificationDays = [
    'Lun',
    'Mar',
    'Mer',
    'Jeu',
    'Ven',
    'Sam',
    'Dim',
  ];

  // Fonction pour créer une notification de base
  void createBasicNotification() {
    notificationUtil.createBasicNotification(
      id: createUniqueId(), // Obtenir un identifiant unique pour cette notification
      channelKey: AppStrings.BASIC_CHANNEL_KEY,
      title: '${Emojis.clothing_backpack + Emojis.transport_air_airplane} Appel réseau',
      body:
          'Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime mollitia,molestiae quas vel sint commodi repudiandae consequuntur',
      bigPicture: 'asset://assets/imgs/eco_large.png', // Afficher une grande image
    );
  }

  // Fonction pour déclencher l'annulation de toutes les notifications planifiées
  void triggerCancelNotification() {
    notificationUtil.cancelAllScheduledNotifications(context: context);
  }

  // Fonction pour initier le processus de planification en affichant une boîte de dialogue de sélection de jour
  void triggerScheduleNotification() {
    showDialog(
      context: context,
      builder: (context) => AlertDialog(
        title: const Text('Afficher la notification chaque'),
        content: Wrap(
          spacing: 3.0,
          runSpacing: 8.0,
          children: notificationDays
              .asMap()
              .entries
              .map(
                (day) => ElevatedButton(
                  style: ElevatedButton.styleFrom(
                      backgroundColor: AppColor.secondaryColor),
                  onPressed: () {
                    int index = day.key;
                    setState(() {
                      selectedNotificationDay = day.value;
                      selectedDayOfTheWeek = index + 1; // Le jour de la semaine est indexé à 1 (Dimanche est 1, Lundi est 2, etc.)
                    });
                    Navigator.of(context).pop(); // Fermer la boîte de dialogue de sélection de jour
                    pickTime(); // Ensuite, demander la sélection de l'heure
                  },
                  child: Text(
                    day.value,
                    style: const TextStyle(
                      color: Colors.white,
                    ),
                  ),
                ),
              )
              .toList(),
        ),
      ),
    );
  }

  // Fonction pour créer la notification planifiée réelle après la sélection du jour et de l'heure
  void createScheduleNotification() {
    notificationUtil.createScheduledNotification(
      id: createUniqueId(),
      channelKey: AppStrings.SCHEDULE_CHANNEL_KEY,
      title: '${Emojis.time_alarm_clock} Vérifiez votre fusée !',
      body:
          'Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime mollitia,molestiae quas vel sint commodi repudiandae consequuntur',
      layout: NotificationLayout.Default,
      notificationCalendar: NotificationCalendar(
        hour: selectedTime.hour,
        minute: selectedTime.minute,
        weekday: selectedDayOfTheWeek, // Utiliser le jour de la semaine sélectionné
      ),
    );
  }

  // Fonction pour afficher une boîte de dialogue de sélection d'heure
  Future<TimeOfDay?> pickTime() async {
    TimeOfDay? pickedTime = await showTimePicker(
      context: context,
      initialTime: TimeOfDay.now(),
    );

    if (pickedTime != null) {
      setState(() {
        selectedTime = pickedTime;
        isTimeSelected = true;
      });
      createScheduleNotification(); // Une fois l'heure choisie, créer la notification
    }
    return null;
  }

  // Fonction pour demander les permissions de notification
  void requestPermission() {
    notificationUtil.requestPermissionToSendNotifications(context: context);
  }

  @override
  void initState() {
    super.initState();

    // Vérifier la permission de notification et demander si non autorisée
    AwesomeNotifications().isNotificationAllowed().then((isAllowed) {
      if (!isAllowed) {
        customAlertDialog(
          title: 'Autoriser les notifications',
          content: 'Rocket App a besoin d\'accès aux notifications pour vous envoyer des mises à jour et des rappels en temps opportun.',
          context: context,
          action: requestPermission,
          button1Title: 'Autoriser',
          button2Title: 'Ne pas autoriser',
        );
      }
    });

    // Initialiser NotificationUtil avec une instance de AwesomeNotifications
    notificationUtil = NotificationUtil(
      awesomeNotifications: AwesomeNotifications(),
    );

    // Configurer les écouteurs pour divers événements de notification
    AwesomeNotifications().setListeners(
      onNotificationCreatedMethod: (notification) async =>
          NotificationUtil.onNotificationCreatedMethod(notification, context),
      onActionReceivedMethod: NotificationUtil.onActionReceivedMethod,
      onDismissActionReceivedMethod: (ReceivedAction receivedAction) =>
          NotificationUtil.onDismissActionReceivedMethod(receivedAction),
      onNotificationDisplayedMethod: (ReceivedNotification receivedNotification) =>
          NotificationUtil.onNotificationDisplayedMethod(receivedNotification),
    );
  }

  @override
  void dispose() {
    // Libérer les ressources de AwesomeNotifications lorsque le widget est supprimé
    AwesomeNotifications().dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: AppColor.primaryColor,
        title: const Wrap(
          spacing: 8,
          children: [
            Icon(
              CupertinoIcons.rocket,
              color: Colors.white,
            ),
            Text(
              'Fusées',
              style: TextStyle(
                color: Colors.white,
              ),
            ),
          ],
        ),
        actions: [
          IconButton(
            onPressed: () => Navigator.of(context).push(
              MaterialPageRoute(
                builder: (context) => const StatsPage(),
              ),
            ),
            icon: const Icon(
              CupertinoIcons.chart_bar_square,
              color: Colors.white,
            ),
          )
        ],
      ),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          // Afficher le jour et l'heure sélectionnés si une planification est choisie
          if (isTimeSelected) ...[
            CustomRichText(
              title: 'Jour sélectionné : ',
              content: selectedNotificationDay,
            ),
            const SizedBox(height: 10),
            CustomRichText(
              title: 'Heure sélectionnée : ',
              content: selectedTime.format(context),
            ),
            const SizedBox(height: 10),
          ],
          Image.asset('assets/imgs/rocket.png'),
          const SizedBox(height: 20),
          // Boutons pour diverses actions de notification
          CustomElevatedButton(
            function: createBasicNotification,
            title: 'Afficher la notification de base',
            icon: Icons.notifications,
          ),
          const SizedBox(height: 20),
          CustomElevatedButton(
            function: triggerScheduleNotification,
            title: 'Planifier la notification',
            icon: Icons.schedule,
          ),
          const SizedBox(height: 20),
          CustomElevatedButton(
            function: triggerCancelNotification,
            title: 'Annuler toutes les notifications planifiées',
            icon: Icons.cancel,
          ),
        ],
      ),
    );
  }
}
```

La `HomePage` est l'écran interactif principal de notre application.

* **Variables d'état** : gère le `selectedNotificationDay`, `selectedDayOfTheWeek`, `selectedTime` et `isTimeSelected` pour gérer le processus de planification.
    
* Liste `notificationDays` : Une simple liste de chaînes représentant les jours de la semaine, utilisée pour la boîte de dialogue de sélection de planification.
    
* `createBasicNotification()` : Cette fonction est déclenchée par une pression sur un bouton et appelle `notificationUtil.createBasicNotification` pour afficher une notification immédiate avec une image.
    
* `triggerCancelNotification()` : Appelle `notificationUtil.cancelAllScheduledNotifications` pour effacer toute notification planifiée en attente.
    
* `triggerScheduleNotification()` : Cette fonction présente d'abord une `AlertDialog` où l'utilisateur peut sélectionner un jour de la semaine pour la notification planifiée. Une fois un jour sélectionné, elle appelle `pickTime()`.
    
* `createScheduleNotification()` : Après que l'utilisateur a sélectionné à la fois un jour et une heure, cette fonction est appelée pour créer la notification planifiée récurrente en utilisant `notificationUtil.createScheduledNotification`.
    
* `pickTime()` : Utilise le `showTimePicker` de Flutter pour permettre à l'utilisateur de sélectionner une heure spécifique pour la notification planifiée.
    
* `requestPermission()` : Un simple wrapper pour appeler `notificationUtil.requestPermissionToSendNotifications`.
    
* `initState()` : Cette méthode cruciale est appelée une fois lorsque le widget est inséré dans l'arborescence des widgets.
    
    * Elle vérifie d'abord si les permissions de notification sont accordées en utilisant `AwesomeNotifications().isNotificationAllowed()`. Si ce n'est pas le cas, elle affiche une `customAlertDialog` demandant à l'utilisateur la permission.
        
    * Elle initialise `notificationUtil` pour interagir avec notre classe d'assistance de notification.
        
    * **De manière cruciale, elle configure les** `awesome_notifications` **listeners** (`setListeners`). Ces listeners connectent les méthodes statiques globales dans `NotificationUtil` aux divers événements de notification (création, affichage, rejet et action reçue). Cela garantit que notre application peut réagir aux interactions de notification même lorsqu'elle n'est pas activement au premier plan.
        
* `dispose()` : Cette méthode est appelée lorsque le widget est retiré de l'arborescence des widgets. Elle appelle `AwesomeNotifications().dispose()` pour libérer toute ressource détenue par le package de notification, ce qui est une bonne pratique.
    
* **Méthode `build()`** : Cela décrit l'interface utilisateur de la page d'accueil, y compris la barre d'application, une image `rocket.png`, et trois widgets `CustomElevatedButton` qui déclenchent les différentes fonctionnalités de notification. Elle affiche également conditionnellement le jour et l'heure sélectionnés si une notification planifiée a été initiée.
    

#### `stats_page.dart` :

```dart
import 'package:flutter/material.dart';
import '../components/stats_container.dart';
import '../constants/colors.dart';

class StatsPage extends StatelessWidget {
  const StatsPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: AppColor.primaryColor,
        title: const Wrap(
          spacing: 8,
          children: [
            Icon(
              Icons.analytics,
              color: Colors.white,
            ),
            Text(
              'Statistiques',
              style: TextStyle(
                color: Colors.white,
              ),
            ),
          ],
        ),
      ),
      body: Center(
        child: Padding(
          padding: const EdgeInsets.symmetric(horizontal: 20),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              const StatsContainer(
                icon: Icons.notifications,
                stat: '10', // Données fictives pour la démonstration
              ),
              const SizedBox(height: 20),
              const StatsContainer(
                icon: Icons.schedule,
                stat: '5', // Données fictives pour la démonstration
              ),
              const SizedBox(height: 20),
              const StatsContainer(
                icon: Icons.cancel,
                stat: '2', // Données fictives pour la démonstration
              ),
            ],
          ),
        ),
      ),
    );
  }
}
```

La `StatsPage` est un écran simple conçu pour afficher certaines statistiques hypothétiques liées aux notifications.

* Elle présente une `AppBar` avec un titre et une icône d'analyse.
    
* Le `body` se compose d'un widget `Center` contenant une `Column` de trois widgets `StatsContainer`.
    
* Chaque `StatsContainer` affiche un nombre fictif pour "notifications", "notifications planifiées" et "notifications annulées". Cette page sert de placeholder pour démontrer la navigation après une action de notification, et dans une application réelle, ces nombres seraient dynamiques.
    

### Initialiser et exécuter l'application

Enfin, configurons le point d'entrée principal de notre application Flutter. Ouvrez `main.dart` et remplacez son contenu par le code suivant :

```dart
import 'package:awesome_notifications/awesome_notifications.dart';
import 'package:flutter/material.dart';
import 'pages/home_page.dart';
import 'constants/app_strings.dart'; // Importer AppStrings pour les clés de canal
import 'constants/colors.dart'; // Importer AppColor pour la couleur de canal par défaut

void main() async {
  WidgetsFlutterBinding.ensureInitialized(); // Assurer que la liaison Flutter est initialisée

  // Initialiser Awesome Notifications avec les canaux de notification
  AwesomeNotifications().initialize(
    'resource://drawable/app_icon', // L'icône à afficher pour les notifications.
                                     // Pour Android, cela pointe généralement vers une ressource drawable.
                                     // 'resource://drawable/res_notification_icon' est un autre chemin courant.
                                     // Si votre icône ne s'affiche pas, essayez d'expérimenter avec ce chemin.
    [
     // Canal de notification pour les notifications de base
      NotificationChannel(
        key: AppStrings.BASIC_CHANNEL_KEY,
        name: AppStrings.BASIC_CHANNEL_NAME,
        channelDescription: AppStrings.BASIC_CHANNEL_DESCRIPTION,
        defaultColor: AppColor.primaryColor, // Couleur par défaut pour les notifications de ce canal
        importance: NotificationImportance.High, // Les notifications de haute importance émettent un son et apparaissent à l'écran
        defaultRingtoneType: DefaultRingtoneType.Notification, // Utiliser le son de notification par défaut
      ),

      // Canal de notification pour les notifications planifiées
      NotificationChannel(
        key: AppStrings.SCHEDULE_CHANNEL_KEY,
        name: AppStrings.SCHEDULE_CHANNEL_NAME,
        channelDescription: AppStrings.SCHEDULE_CHANNEL_DESCRIPTION,
        defaultColor: AppColor.primaryColor,
        importance: NotificationImportance.High,
        defaultRingtoneType: DefaultRingtoneType.Notification,
      ),
    ],
    // Optionnel : définissez ceci sur true si vous souhaitez déboguer Awesome Notifications
    debug: false,
  );

  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  // GlobalKey est utilisé pour accéder au NavigatorState depuis n'importe où dans l'application
  // Cela est crucial pour naviguer depuis les actions de notification en arrière-plan.
  static GlobalKey<NavigatorState> navigatorKey = GlobalKey<NavigatorState>();

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      navigatorKey: navigatorKey, // Assigner la clé globale à MaterialApp
      title: 'Fusées',
      theme: ThemeData(
        primarySwatch: MaterialColor(
          AppColor.primaryColor.value, // Convertir Color en MaterialColor pour primary swatch
          <int, Color>{
            50: AppColor.primaryColor.withOpacity(0.1),
            100: AppColor.primaryColor.withOpacity(0.2),
            200: AppColor.primaryColor.withOpacity(0.3),
            300: AppColor.primaryColor.withOpacity(0.4),
            400: AppColor.primaryColor.withOpacity(0.5),
            500: AppColor.primaryColor.withOpacity(0.6),
            600: AppColor.primaryColor.withOpacity(0.7),
            700: AppColor.primaryColor.withOpacity(0.8),
            800: AppColor.primaryColor.withOpacity(0.9),
            900: AppColor.primaryColor.withOpacity(1.0),
          },
        ),
      ),
      home: const HomePage(),
    );
  }
}
```

Le fichier `main.dart` est le point d'entrée de votre application Flutter.

* **Fonction `main()`** :
    
    * `WidgetsFlutterBinding.ensureInitialized();` : Cette ligne est vitale pour s'assurer que la liaison des widgets Flutter est initialisée avant que `AwesomeNotifications().initialize()` ne soit appelée. Cela prévient les erreurs potentielles, surtout lorsqu'on traite avec les canaux de plateforme.
        
    * `AwesomeNotifications().initialize(...)` : C'est ici que `awesome_notifications` est configuré.
        
        * Le premier argument (`'resource://drawable/app_icon'`) spécifie l'icône par défaut pour les notifications. Ce chemin pointe vers une ressource drawable sur Android.
            
        * Le deuxième argument est une liste d'objets `NotificationChannel`. **Les canaux de notification sont obligatoires pour Android 8.0 (niveau d'API 26) et supérieur.** Ils permettent aux utilisateurs de contrôler les paramètres de notification (son, vibration, importance) sur une base par canal. Nous définissons deux canaux : un pour les notifications de base et un autre pour les notifications planifiées, chacun avec sa `key`, `name`, `channelDescription`, `defaultColor`, `importance` et `defaultRingtoneType`.
            
        * `debug: false` : Définissez sur `true` pendant le développement pour voir des logs plus détaillés de `awesome_notifications`.
            
* **Classe `MyApp`** :
    
    * `static GlobalKey<NavigatorState> navigatorKey = GlobalKey<NavigatorState>();` : Il s'agit d'une ligne cruciale. Une `GlobalKey` assignée à `navigatorKey` de `MaterialApp` nous permet d'accéder à `NavigatorState` depuis n'importe où dans l'application, même depuis des méthodes statiques comme `NotificationUtil.onActionReceivedMethod`. Cela nous permet d'effectuer une navigation (par exemple, vers `StatsPage`) lorsqu'une notification est tapée, quel que soit l'écran actuel.
        
    * Le widget `MaterialApp` configure la structure de base de notre application, y compris le titre, le thème (en utilisant notre `AppColor.primaryColor`), et définit `HomePage` comme écran initial. La `navigatorKey` est assignée ici pour qu'elle puisse être accessible globalement.
        

Enregistrez tous les fichiers et exécutez l'application depuis votre terminal :

```bash
flutter run
```

Cette commande lancera l'application sur votre appareil connecté ou émulateur, et vous pourrez commencer à déclencher des notifications de base et planifiées !

## **Quelques captures d'écran :**

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1707562835994/b8462f6c-2c2e-4461-ad16-45c0d6256257.png align="center")

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1707562817505/9fea68c2-fed5-4198-9430-fe22ead6e1ad.png align="center")

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1707562846027/45b5212d-df1f-4e6b-85d3-dbd1ea3d6345.png align="center")

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1707562861005/e636c37c-0cad-4364-bda9-0cd650f137ae.png align="center")

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1707562873280/95c7f91a-3700-4cc5-a531-15a5bd4227d4.png align="center")

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1707562884030/9c7f9dc5-177f-4948-b5c8-296b6ce535a3.png align="center")

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1707562896944/64a7400c-d114-4067-bf84-aedc60f896b4.png align="center")

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1707562907917/f2aee4c0-848f-448e-bfd8-9cceb5731d8a.png align="center")

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1707562917350/d9513419-f350-4ffc-81c2-8b798f42a209.png align="center")

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1707562930945/1962fd89-86d5-4d14-a38d-d632597f8a62.png align="center")

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1707562941938/2e0bff86-2c09-411f-8d46-5105d8ca0f46.png align="center")

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1707562951005/e5b378e5-4285-4028-9d45-48ac18627dba.png align="center")

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1707562963203/bcb69623-d46f-40f9-ad24-c4d53f6025fa.png align="center")

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1707562975094/4320b0b9-06f5-4830-8e18-d747f2238c10.png align="center")

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1707562985108/91566242-aca7-4b92-8297-809226078506.png align="center")

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1707562995699/1d55d56f-b0e3-4692-8618-7fb9f5554194.png align="center")

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1707563003655/8ee4c840-d16f-4b6e-a106-12ada5721cb2.png align="center")

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1707563014469/79ce425e-4f29-4877-97b1-c9d0452913c7.png align="center")

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1707563024519/0c7f15e8-4891-4cea-a16f-e9a5557190dc.png align="center")

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1707563042524/fcacf44b-a0eb-489e-8d05-0a76dc01973c.png align="center")

Pour explorer plus d'exemples et obtenir des informations détaillées sur le package `awesome_notifications`, vous pouvez vous référer à la documentation officielle et au dépôt GitHub :

1. **Documentation officielle :** [awesome\_notifications sur](https://pub.dev/packages/awesome_notifications) [pub.dev](http://pub.dev) : Il s'agit de la page officielle du package sur [pub.dev](http://pub.dev). Vous pouvez trouver de la documentation, des exemples et l'historique des versions ici.
    
2. **Dépôt GitHub :** [awesome\_notifications sur GitHub](https://github.com/rafaelsetragni/awesome_notifications) : Visitez le dépôt GitHub pour accéder au code source, aux problèmes, aux discussions et plus encore. C'est une excellente ressource pour explorer le fonctionnement interne du package.
    

La lecture de la documentation et la consultation du dépôt officiel peuvent fournir des informations supplémentaires, des scénarios d'utilisation et des mises à jour liées au package `awesome_notifications`. Il est toujours bénéfique de se référer aux sources officielles pour les informations les plus récentes et les plus complètes.

## Conclusion

L'implémentation de notifications locales dans une application Flutter est essentielle pour fournir aux utilisateurs des informations et des rappels en temps opportun. Le package `awesome_notifications` simplifie considérablement le processus de création, de planification et de gestion des notifications.

En suivant les étapes détaillées décrites dans cet article, et en comprenant le but de chaque segment de code, vous pouvez améliorer efficacement l'engagement des utilisateurs et offrir une meilleure expérience globale pour les utilisateurs de votre application Flutter.