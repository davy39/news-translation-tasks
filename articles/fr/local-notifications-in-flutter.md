---
title: Comment configurer les notifications locales dans Flutter
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2021-04-27T00:05:44.000Z'
originalURL: https://freecodecamp.org/news/local-notifications-in-flutter
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/ashwini-chaudhary-4SqmKiyeXbE-unsplash.jpg
tags:
- name: Flutter
  slug: flutter
- name: user experience
  slug: user-experience
- name: Web Applications
  slug: web-applications
seo_title: Comment configurer les notifications locales dans Flutter
seo_desc: 'Notifications are an excellent way to engage your users or to get them
  to go back to your application. You can also use notifications to make users pay
  attention to something while they''re using the app.

  There are two types of notifications:


  Push No...'
---

Les notifications sont un excellent moyen d'engager vos utilisateurs ou de les inciter à revenir sur votre application. Vous pouvez également utiliser les notifications pour attirer l'attention des utilisateurs sur quelque chose pendant qu'ils utilisent l'application.

Il existe deux types de notifications :

1. Les notifications Push
2. Les notifications locales

Comme le suggère le titre de cet article, nous ne nous concentrerons pas sur les notifications Push (également parce que c'est un sujet qui a été abondamment documenté). Au lieu de cela, nous nous concentrerons uniquement sur les notifications locales. La différence entre les deux provient d'un point majeur :

> _Les notifications locales proviennent de l'application elle-même, contrairement aux notifications Push qui sont déclenchées depuis un serveur distant._

Pour cet article, nous utiliserons le projet de base (vanilla) qui est créé lorsque vous ouvrez une nouvelle application Flutter (celle avec le compteur) – moins toutes les parties liées au compteur.

Au moment de la rédaction de cet article, la version la plus récente de Flutter est la 5.0.0+1, donc pour les futurs lecteurs, veuillez garder cela à l'esprit.

## Configurer le projet

Pour permettre à notre application d'utiliser les notifications locales, nous devons ajouter le package [flutter_local_notifications](https://pub.dev/packages/flutter_local_notifications) à notre projet.

Ajoutez ce qui suit à votre fichier `pubspec.yaml`, sous dependencies :

```
dependencies:
  flutter:
    sdk: flutter
  flutter_local_notifications: ^5.0.0+1
```

Ensuite, exécutez cette commande :

```
Pub get
```

Puisque le package de notifications locales doit être initialisé, nous allons créer une classe de service pour gérer cette logique pour l'ensemble de notre application. Cette classe exposera également des méthodes pour créer/envoyer/annuler des notifications.

Créez un nouveau fichier dart nommé **notification_service.dart** avec le code suivant :

```dart
import 'package:flutter_local_notifications/flutter_local_notifications.dart';

class NotificationService {
  static final NotificationService _notificationService =
      NotificationService._internal();

  factory NotificationService() {
    return _notificationService;
  }

  NotificationService._internal();
  
}
```

Le code ci-dessus se traduit par un objet Singleton en Dart. Assurez-vous d'importer le package de notification locale en haut de ce fichier.

## Intégration

Parce que Flutter est un Framework multiplateforme, chaque package créé pour lui doit supporter à la fois les appareils iOS et Android.

Et parce que les notifications sont gérées très différemment entre iOS et Android, il y a plusieurs calibrages que nous devrons effectuer lors de l'utilisation du package de notifications locales.

Tout d'abord, nous devons créer une instance pour le **FlutterLocalNotificationPlugin**. Nous utiliserons cet objet pour initialiser les paramètres pour Android et iOS et également pour d'autres besoins de notification.

```dart
final FlutterLocalNotificationsPlugin flutterLocalNotificationsPlugin = FlutterLocalNotificationsPlugin();

```

Nous devons maintenant initialiser le plugin de notification locale avec des paramètres spécifiques pour Android et iOS. Pour ce faire, nous devons créer un objet **InitializationSettings**. Il accepte des arguments pour les systèmes d'exploitation Android, iOS et MacOS.

> _Nous ne discuterons pas de MacOS ici car il a une configuration similaire à celle d'iOS._

### Android

La configuration pour Android est assez simple, car il n'y a qu'un seul argument obligatoire à passer – **defaultIcon** (String). Il représente l'icône qui sera affichée dans la notification.

Ici, vous devez passer le nom de l'icône que vous souhaitez utiliser. Vous devez placer cette icône à l'intérieur du répertoire drawable. Le chemin complet est :

_VOTRE_NOM_D_APPLICATION\\android\\app\\src\\main\\res\\drawable\\VOTRE_ICONE_D_APP.png_

![Image](https://www.freecodecamp.org/news/content/images/2021/04/studio64_yCLtTMYa3k.png)
_Emplacement de app_icon_

Il n'est pas nécessaire de demander des permissions.

### iOS

Comme pour la plupart des sujets liés à iOS, les choses se compliquent un peu ici. En raison de la manière dont les notifications sont gérées entre les différentes versions du système d'exploitation, nous devons effectuer une configuration supplémentaire ici.

À l'intérieur du fichier **AppDelegate**, vous devez ajouter les lignes de code suivantes :

```objective-c
- (BOOL)application:(UIApplication *)application 
didFinishLaunchingWithOptions:(NSDictionary<UIApplicationLaunchOptionsKey, id> *)launchOptions {
  if (@available(iOS 10.0, *)) {
    [UNUserNotificationCenter currentNotificationCenter].delegate = (id<UNUserNotificationCenterDelegate>) self;
  }
}
```

Vous devez demander la permission à l'utilisateur pour divers aspects liés aux notifications. Par conséquent, l'objet d'initialisation pour iOS possède les arguments suivants :

* [requestAlertPermission](https://pub.dev/documentation/flutter_local_notifications/latest/flutter_local_notifications/IOSInitializationSettings/requestAlertPermission.html)
* [requestBadgePermission](https://pub.dev/documentation/flutter_local_notifications/latest/flutter_local_notifications/IOSInitializationSettings/requestBadgePermission.html)
* [requestSoundPermission](https://pub.dev/documentation/flutter_local_notifications/latest/flutter_local_notifications/IOSInitializationSettings/requestSoundPermission.html)

Chacun d'eux est explicite, mais concerne un aspect différent d'une notification. Pour correspondre à ces permissions, il existe également des valeurs par défaut que vous pouvez définir pour chacune d'elles.

* [defaultPresentAlert](https://pub.dev/documentation/flutter_local_notifications/latest/flutter_local_notifications/IOSInitializationSettings/defaultPresentAlert.html)
* [defaultPresentBadge](https://pub.dev/documentation/flutter_local_notifications/latest/flutter_local_notifications/IOSInitializationSettings/defaultPresentBadge.html)
* [defaultPresentSound](https://pub.dev/documentation/flutter_local_notifications/latest/flutter_local_notifications/IOSInitializationSettings/defaultPresentSound.html)

Ces options sont présentes car l'initialisation du plugin de notifications locales peut amener le système d'exploitation à présenter des boîtes de dialogue de permission à l'utilisateur au moment où vous ne souhaitez pas qu'elles apparaissent. Si vous ne voulez pas ce comportement, vous pouvez définir toutes ces valeurs sur false.

Une autre particularité d'iOS concerne la différence de comportement entre les notifications présentées à l'utilisateur lorsque l'application est au premier plan ou lorsqu'elle est en arrière-plan.

Par défaut, le système d'exploitation n'affichera pas de notification à l'utilisateur si l'application est au premier plan.

Le plugin lui-même se chargera d'afficher une notification lorsque l'application est au premier plan. Mais en dessous d'iOS 10, vous devez fournir une méthode de rappel (callback) **onDidReceiveLocalNotification** qui gérera l'interaction de l'utilisateur avec la notification.

Après avoir configuré les initialisations spécifiques aux plateformes, il est temps de regrouper toute cette logique dans une méthode de notre service de notification. Notre meilleure approche ici est de créer une méthode init qui sera appelée depuis notre fichier **main.dart** lors du premier lancement de l'application.

```dart
void init() {
  final AndroidInitializationSettings initializationSettingsAndroid =
      AndroidInitializationSettings('app_icon');
  
  final IOSInitializationSettings initializationSettingsIOS =
      IOSInitializationSettings(
    requestSoundPermission: false,
    requestBadgePermission: false,
    requestAlertPermission: false,
    onDidReceiveLocalNotification: onDidReceiveLocalNotification,
  );
  
    final InitializationSettings initializationSettings =
        InitializationSettings(
            android: initializationSettingsAndroid, 
            iOS: initializationSettingsIOS, 
            macOS: null);
  }
```

Notez qu'après avoir créé des instances pour les paramètres d'initialisation spécifiques aux plateformes, nous devons également créer un objet **InitializationSettings** auquel nous passons nos objets de paramètres d'initialisation spécifiques aux plateformes.

Notre dernière étape ici est d'appeler la méthode initialize sur l'objet **FlutterLocalNotificationsPlugin**.

En plus des paramètres d'initialisation ci-dessus, il possède également un autre argument appelé **onSelectNotification**. Cet argument représente le rappel qui sera appelé une fois qu'une notification aura été touchée, et c'est un argument optionnel. Ce rappel a un argument appelé **payload** qui contiendra toutes les données transmises via la notification.

```dart
Future<void> init() async {
  final AndroidInitializationSettings initializationSettingsAndroid =
      AndroidInitializationSettings('app_icon');
  
  final IOSInitializationSettings initializationSettingsIOS =
      IOSInitializationSettings(
    requestSoundPermission: false,
    requestBadgePermission: false,
    requestAlertPermission: false,
    onDidReceiveLocalNotification: onDidReceiveLocalNotification,
  );
  
    final InitializationSettings initializationSettings =
        InitializationSettings(
            android: initializationSettingsAndroid, 
            iOS: initializationSettingsIOS, 
            macOS: null);
  
   await flutterLocalNotificationsPlugin.initialize(initializationSettings,
        onSelectNotification: selectNotification);
  }


   Future selectNotification(String payload) async {
      // Gérer la logique lors de l'appui sur la notification ici
   }
```

Dans notre fichier main.dart, nous appellerons la méthode init comme ceci :

```dart
Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await NotificationService().init(); // <----
  runApp(MyApp());
}
```

## Cas d'utilisation des notifications locales

### Comment afficher une notification locale

Pour afficher une notification, vous devez créer une instance de détails de notification appropriée (pour Android/iOS). Chaque plateforme a ses propres arguments spécifiques qui doivent être transmis.

```dart
const AndroidNotificationDetails androidPlatformChannelSpecifics = 
    AndroidNotificationDetails(
        channelId: String,   // Requis pour Android 8.0 ou version ultérieure
        channelName: String, // Requis pour Android 8.0 ou version ultérieure
        channelDescription: String, // Requis pour Android 8.0 ou version ultérieure
        importance: Importance,
        priority: Priority
    );
```

L'exemple ci-dessus ne montre que quelques-uns des arguments que vous pouvez passer à **AndroidNotificationDetails**. La liste complète est beaucoup plus longue et vous pouvez la consulter [ici](https://pub.dev/documentation/flutter_local_notifications/latest/flutter_local_notifications/AndroidNotificationDetails-class.html).

```dart
const IOSNotificationDetails iOSPlatformChannelSpecifics =
    IOSNotificationDetails(
        presentAlert: bool?,  // Afficher une alerte lorsque la notification est affichée et que l'application est au premier plan (uniquement à partir d'iOS 10)
        presentBadge: bool?,  // Afficher le numéro de badge lorsque la notification est affichée et que l'application est au premier plan (uniquement à partir d'iOS 10)
        presentSound: bool?,  // Jouer un son lorsque la notification est affichée et que l'application est au premier plan (uniquement à partir d'iOS 10)
        sound: String?,  // Spécifie le chemin du fichier à lire (uniquement à partir d'iOS 10)
        badgeNumber: int?, // Le numéro de badge de l'icône de l'application
        attachments: List<IOSNotificationAttachment>?, (uniquement à partir d'iOS 10)
        subtitle: String?, // Description secondaire (uniquement à partir d'iOS 10)
        threadIdentifier: String? (uniquement à partir d'iOS 10)
   );
```

Ensuite, nous allons créer un objet **NotificationDetails** et lui passer notre objet de détails de notification spécifique à la plateforme.

```dart
const NotificationDetails platformChannelSpecifics = 
  NotificationDetails(android: androidPlatformChannelSpecifics);

OU
  
const NotificationDetails platformChannelSpecifics = 
  NotificationDetails(iOS: iOSPlatformChannelSpecifics);
```

Ensuite, nous devons appeler la méthode `show` du **FlutterLocalNotificationPlugin**.

```
 await flutterLocalNotificationsPlugin.show(
    int id,
    String? title,
    String? body,
    NotificationDetails? notificationDetails,
    String? payload);
```

Les paramètres ici parlent d'eux-mêmes, mais nous allons quand même les passer en revue :

* **id** – l'identifiant de la notification. Chaque notification doit avoir un identifiant unique
* **title** – le titre de la notification
* **body** – ce que nous voulons afficher comme message principal de notre notification
* **notificationDetails** – l'objet de détails de notification dont nous avons discuté ci-dessus
* **payload** – les données que nous voulons transmettre avec cette notification afin qu'elles puissent être utilisées plus tard lorsque la notification est touchée et que notre application s'ouvre à nouveau

Un exemple ressemble à ceci :

```dart
await flutterLocalNotificationsPlugin.show(
        12345, 
        "Une notification de mon application",
        "Cette notification a été envoyée en utilisant le package Flutter Local Notifications", 
        platformChannelSpecifics,
        payload: 'data');
```

### Comment planifier une notification locale

La planification d'une notification nécessite de passer une heure et une date relatives au fuseau horaire de l'appareil de l'utilisateur. Ceci afin de surmonter les différences d'heure qui peuvent être causées par le passage à l'heure d'été.

Puisque le plugin de notifications locales contient déjà la bibliothèque timezone, nous n'avons pas besoin d'ajouter d'autre dépendance dans notre fichier pubspec.yaml. Mais nous devons l'importer dans notre service de notification et également l'initialiser.

```dart
import 'package:flutter_local_notifications/flutter_local_notifications.dart';
import 'package:timezone/data/latest.dart' as tz;
import 'package:timezone/timezone.dart' as tz;


Future<void> init() async {
  final AndroidInitializationSettings initializationSettingsAndroid =
      AndroidInitializationSettings('app_icon');
  
  final IOSInitializationSettings initializationSettingsIOS =
      IOSInitializationSettings(
    requestSoundPermission: false,
    requestBadgePermission: false,
    requestAlertPermission: false,
    onDidReceiveLocalNotification: onDidReceiveLocalNotification,
  );
  
    final InitializationSettings initializationSettings =
        InitializationSettings(
            android: initializationSettingsAndroid, 
            iOS: initializationSettingsIOS, 
            macOS: null);
  
  tz.initializeTimeZones();  // <------
  
   await flutterLocalNotificationsPlugin.initialize(initializationSettings,
        onSelectNotification: selectNotification);
  }
```

Pour planifier une notification, nous devons utiliser la méthode **zonedSchedule** :

```dart
Future<void> zonedSchedule(
              int id,
              String? title,
              String? body,
              TZDateTime scheduledDate,
              NotificationDetails notificationDetails,
              {required UILocalNotificationDateInterpretation uiLocalNotificationDateInterpretation,
              required bool androidAllowWhileIdle,
              String? payload,
              DateTimeComponents? matchDateTimeComponents}
```

Elle présente plusieurs similitudes avec la méthode show, mais elle possède des arguments qui concernent le moment où la notification doit être envoyée. Regardons-les un par un :

* **scheduledDate** – c'est le paramètre qui indique à la notification quand être envoyée. Vous pouvez obtenir la date d'aujourd'hui et y ajouter la durée souhaitée
* **uiLocalNotificationDateInterpretation** – utilisé dans les versions d'iOS inférieures à 10 (par manque de support) pour interpréter l'heure comme une heure absolue ou l'heure de l'horloge murale
* **androidAllowWhileIdle** – spécifie si la notification doit être envoyée même lorsque l'appareil est en mode veille basse consommation

Un exemple ressemble à ceci :

```dart
await flutterLocalNotificationsPlugin.zonedSchedule(
        12345,
        "Une notification de mon application",
        "Cette notification vous est proposée par le package Local Notifications",
        tz.TZDateTime.now(tz.local).add(const Duration(days: 3)),
        const NotificationDetails(
            android: AndroidNotificationDetails(CHANNEL_ID, CHANNEL_NAME,
                CHANNEL_DESCRIPTION)),
        androidAllowWhileIdle: true,
        uiLocalNotificationDateInterpretation:
            UILocalNotificationDateInterpretation.absoluteTime);
  }
```

### Comment annuler une notification locale

Lors de l'annulation d'une notification, vous avez deux options :

1. Vous pouvez annuler une notification spécifique
2. Vous pouvez annuler toutes les notifications en attente

Pour annuler une notification spécifique, vous devez utiliser l'identifiant de la notification.

```dart
await flutterLocalNotificationsPlugin.cancel(NOTIFICATION_ID);

```

Pour annuler toutes les notifications, vous utilisez la méthode **cancelAll** :

```dart
await flutterLocalNotificationsPlugin.cancelAll();

```

## Conclusion

Il y a beaucoup plus de choses que vous pouvez faire avec le package de notification locale dans Flutter, et je vous encourage vivement à en lire davantage à ce sujet et à consulter la [documentation](https://pub.dev/documentation/flutter_local_notifications/latest/index.html).

Pour voir un exemple concret d'une application utilisant les notifications locales, vous pouvez vous rendre ici :

%[https://play.google.com/store/apps/details?id=com.tomerpacific.birthday_calendar]

Pour voir le code source, rendez-vous ici :

%[https://github.com/TomerPacific/BirthdayCalendar]

Merci de votre lecture !