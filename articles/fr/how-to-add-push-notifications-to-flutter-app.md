---
title: Comment ajouter des notifications push à une application Flutter en utilisant
  Firebase Cloud Messaging
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-12-09T19:57:23.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-push-notifications-to-flutter-app
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5fd0362ce6787e098393c56a.jpg
tags:
- name: Firebase
  slug: firebase
- name: Flutter
  slug: flutter
- name: messaging
  slug: messaging
- name: push notification
  slug: push-notification
seo_title: Comment ajouter des notifications push à une application Flutter en utilisant
  Firebase Cloud Messaging
seo_desc: 'By Krissanawat

  Flutter has quickly become one the most popular frameworks for cross-platform mobile
  application development. It helps developers build native UIs with support for different
  device sizes, pixel densities, and orientations creating a be...'
---

Par Krissanawat

Flutter est rapidement devenu l'un des frameworks les plus populaires pour le développement d'applications mobiles multiplateformes. Il aide les développeurs à créer des interfaces utilisateur natives avec support pour différentes tailles d'écran, densités de pixels et orientations, créant ainsi une belle interface utilisateur parfaite. 

Dans ce tutoriel, nous allons apprendre comment ajouter des notifications push à une application Flutter en utilisant Firebase Cloud Messaging. Ce tutoriel ne traitera que de la configuration pour la **plateforme Android**.

### D'abord, que sont les notifications push ?

Les notifications push sont un type de messagerie pop-up qui alerte les utilisateurs de l'application sur ce qui se passe dans l'application. Elles sont également un moyen important d'amplifier l'engagement des utilisateurs dans votre application. 

Par exemple, supposons qu'un utilisateur oublie l'application une fois qu'il l'a installée. Vous pouvez alors utiliser les notifications push comme mécanisme pour regagner et retenir leur intérêt. Les notifications push aident également à générer du trafic vers votre application. 

Firebase Cloud Messaging est un service offert par Firebase qui vous permet d'envoyer ces notifications à vos utilisateurs. Vous pouvez configurer diverses options pour envoyer différentes notifications à différents publics en fonction du temps et de la routine. 

Grâce à tous ces avantages, nous allons l'utiliser pour envoyer des notifications à notre application Flutter.

## Étape 1 : Créer un projet Flutter

Tout d'abord, nous allons créer un projet Flutter. Pour cela, nous devons avoir le SDK Flutter installé sur notre système. Vous pouvez trouver des étapes simples pour l'installation de Flutter dans la [documentation officielle](https://flutter.dev/docs/get-started/install). 

Après avoir installé Flutter avec succès, vous pouvez simplement exécuter la commande suivante dans le répertoire de votre choix pour configurer un projet Flutter complet :

```jsx
flutter create pushNotification

```

Après avoir configuré le projet, naviguez à l'intérieur du répertoire du projet. Exécutez la commande suivante dans le terminal pour exécuter le projet dans un émulateur disponible ou un appareil réel :

```bash
flutter run

```

Après une compilation réussie, vous obtiendrez le résultat suivant sur l'écran de l'émulateur :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-69.png)

## Étape 2 : Intégrer la configuration Firebase avec Flutter

Dans cette étape, nous allons intégrer les services Firebase avec notre projet Flutter. Mais d'abord, nous devons créer un projet Firebase. Les directives de configuration sont également fournies dans la [documentation officielle](https://firebase.google.com/docs/flutter/setup?platform=android) de Firebase pour Flutter.

Pour créer un projet Firebase, nous devons nous connecter à [Firebase](https://firebase.google.com/) et accéder à la console. Là, nous pouvons simplement cliquer sur 'Ajouter un projet' pour démarrer notre projet.

Une fenêtre apparaîtra alors demandant de saisir le nom du projet. Ici, j'ai gardé le nom du projet comme `FlutterPushNotification` comme montré dans la capture d'écran ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-70.png)

Nous pouvons continuer à l'étape suivante lorsque le projet a été créé. Après la configuration du projet, nous obtiendrons une console de projet comme montré dans la capture d'écran ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-71.png)

Ici, nous allons configurer Firebase pour la plateforme Android. Nous devons donc cliquer sur l'icône Android affichée dans la capture d'écran ci-dessus. Cela nous mènera à l'interface pour enregistrer Firebase avec notre projet d'application Flutter.

## Étape 3 : Enregistrer Firebase dans votre application Android

Comme le processus d'enregistrement est spécifique à la plateforme, nous allons enregistrer notre application pour la plateforme Android. Après avoir cliqué sur l'icône Android, nous serons dirigés vers une interface demandant le **nom du package Android**. 

Pour ajouter le nom du package de notre projet Flutter, nous devons d'abord le localiser. Le nom du package sera disponible dans le fichier **./android/app/build.gradle** de votre projet Flutter. Vous verrez quelque chose comme ceci :

```jsx
com.example.pushNotification

```

Nous devons simplement le copier et le coller dans le champ de saisie du nom du package Android comme montré dans la capture d'écran ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-72.png)

Après cela, nous pouvons simplement cliquer sur le bouton 'Enregistrer l'application'. Cela nous mènera à l'interface où nous pouvons obtenir le fichier **google-services.json** qui liera notre application Flutter aux services Google de Firebase. 

Nous devons télécharger le fichier et le déplacer dans le répertoire **./android/app** de notre projet Flutter. Les instructions sont également montrées dans la capture d'écran ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-73.png)

## Étape 4 : Ajouter les configurations Firebase aux fichiers natifs dans votre projet Flutter

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

Maintenant, dans notre fichier Gradle de module (niveau application) (**android/app/build.gradle**), nous devons appliquer le plugin **Google Services Gradle**. 

Pour cela, nous devons ajouter le morceau de code mis en évidence dans l'extrait de code suivant au fichier **./android/app/build.gradle** de notre projet :

```jsx
// Ajoutez la ligne suivante :
**apply plugin: 'com.google.gms.google-services'**  // Plugin des services Google

android {
  // ...
}

```

Maintenant, nous devons exécuter la commande suivante afin que certaines configurations automatiques puissent être effectuées :

```jsx
flutter packages get

```

Avec cela, nous avons réussi à intégrer les configurations Firebase avec notre projet Flutter.

## Étape 5 : Intégrer Firebase Messaging avec Flutter

Tout d'abord, nous devons ajouter la dépendance firebase-messaging au fichier **./android/app/build.gradle**. Dans le fichier, nous devons ajouter les dépendances suivantes :

```dart
dependencies {
    implementation "org.jetbrains.kotlin:kotlin-stdlib-jdk7:$kotlin_version"
    implementation 'com.google.firebase:firebase-messaging:20.1.0'
}

```

Ensuite, nous devons ajouter une `action` et une `catégorie` en tant que `intent-filter` dans la balise `activity` du fichier **./android/app/src/main/AndroidManifest.xml** :

```xml
<intent-filter>
    <action android:name="FLUTTER_NOTIFICATION_CLICK" />
    <category android:name="android.intent.category.DEFAULT" />
</intent-filter>

```

Maintenant, nous devons créer un fichier Java appelé **Application.java** dans le chemin **/android/app/src/main/java/<app-organization-path>**.

Ensuite, nous devons ajouter le code de l'extrait de code suivant à l'intérieur :

```java
package io.flutter.plugins.pushNotification;

import io.flutter.app.FlutterApplication;
import io.flutter.plugin.common.PluginRegistry;
import io.flutter.plugin.common.PluginRegistry.PluginRegistrantCallback;
import io.flutter.plugins.GeneratedPluginRegistrant;
import io.flutter.plugins.firebasemessaging.FirebaseMessagingPlugin;
import io.flutter.plugins.firebasemessaging.FlutterFirebaseMessagingService;

public class Application extends FlutterApplication implements PluginRegistrantCallback {
    @Override
    public void onCreate() {
        super.onCreate();
        FlutterFirebaseMessagingService.setPluginRegistrant(this);
    }

    @Override
    public void registerWith(PluginRegistry registry) {
        FirebaseMessagingPlugin.registerWith(registry.registrarFor("io.flutter.plugins.firebasemessaging.FirebaseMessagingPlugin"));
    }
}

```

Maintenant, nous devons assigner cette activité `Application` à la balise `application` du fichier **AndroidManifest.xml** comme montré dans l'extrait de code ci-dessous :

```xml
<application
        android:name=".Application"

```

Cela complète notre configuration du plugin de messagerie Firebase dans le code natif Android. Maintenant, nous allons passer au projet Flutter.

## Étape 6 : Installer le package Firebase Messaging

Ici, nous allons utiliser le package `[firebase_messaging`](https://pub.dev/packages/firebase_messaging/). Pour cela, nous devons ajouter le plugin à l'option de dépendance du fichier pubspec.yaml. 

Nous devons ajouter la ligne de code suivante à l'option des dépendances :

```yaml
firebase_messaging: ^7.0.3

```

## Étape 7 : Implémenter un écran UI simple

Maintenant, à l'intérieur de la classe de widget stateful `MyHomePage` du fichier **main.dart**, nous devons initialiser l'instance `FirebaseMessaging` et quelques constantes comme montré dans l'extrait de code ci-dessous :

```dart
String messageTitle = "Empty";
String notificationAlert = "alert";

FirebaseMessaging _firebaseMessaging = FirebaseMessaging();

```

La variable `messageTitle` recevra le titre du message de notification et `notificationAlert` sera assignée à l'action qui a été complétée une fois que la notification apparaît.

Maintenant, nous devons appliquer ces variables à la fonction build à l'intérieur du corps du widget `Scaffold` comme montré dans l'extrait de code ci-dessous :

```dart
Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text(
              notificationAlert,
            ),
            Text(
              messageTitle,
              style: Theme.of(context).textTheme.headline4,
            ),
          ],
        ),
      ),
    );
  }

```

Ensuite, nous devons exécuter l'application Flutter en exécutant la commande suivante dans le terminal du projet :

```bash
flutter run

```

Nous obtiendrons le résultat que vous voyez dans l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-74.png)

Pour l'instant, le titre de la notification est vide, et l'alerte est également telle que définie. Nous devons leur assigner une valeur appropriée une fois que nous recevons le message de notification.

Nous devons donc configurer le code pour recevoir la notification et utiliser le message de notification pour l'afficher à l'écran.

Pour cela, nous devons ajouter le code de l'extrait de code suivant dans la fonction `initiState` :

```dart
@override
  void initState() {
    // TODO: implement initState
    super.initState();

    _firebaseMessaging.configure(
      onMessage: (message) async{
        setState(() {
          messageTitle = message["notification"]["title"];
          notificationAlert = "New Notification Alert";
        });

      },
      onResume: (message) async{
        setState(() {
          messageTitle = message["data"]["title"];
          notificationAlert = "Application opened from Notification";
        });

      },
    );
  }

```

Ici, nous avons utilisé la méthode `configure` fournie par l'instance `_firebaseMessaging` qui fournit à son tour les callbacks `onMessage` et `onResume`. Ces callbacks fournissent le `message` de notification comme paramètre. La réponse `message` contiendra l'objet de notification sous forme d'objet map.

La fonction `onMessage` se déclenche lorsque la notification est reçue alors que nous exécutons l'application. La fonction `onResume` se déclenche lorsque nous recevons l'alerte de notification dans la barre de notification de l'appareil et ouvrons l'application via la notification push elle-même. Dans ce cas, l'application peut s'exécuter en arrière-plan ou ne pas s'exécuter du tout.

Maintenant, nous sommes tous équipés avec l'application Flutter. Nous devons simplement configurer un message dans Firebase Cloud Messaging et l'envoyer à l'appareil.

## Étape 8 : Créer un message à partir de la console Firebase Cloud Messaging

Tout d'abord, nous devons retourner à la console Cloud Messaging sur le site Firebase comme montré dans l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-75.png)

Ici, nous pouvons voir l'option 'Envoyer votre premier message' dans la fenêtre, car nous n'avons pas configuré de messages auparavant. Nous devons cliquer dessus, ce qui nous mènera à la fenêtre suivante :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-76.png)

Ici, nous pouvons entrer le titre, le texte, l'image et le nom de la notification. Le titre que nous définissons ici sera fourni comme titre dans l'objet `message` des callbacks que nous avons définis précédemment dans le projet Flutter.

Après avoir défini les champs requis, nous pouvons cliquer sur 'Suivant', ce qui nous mènera à la fenêtre suivante :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-77.png)

Ici, nous devons fournir notre application cible et cliquer sur 'Suivant'.

Pour la planification, nous pouvons garder l'option par défaut :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-78.png)

Ensuite, la fenêtre de conversion apparaîtra, que nous pouvons également garder par défaut, puis cliquer sur le bouton 'Suivant'.

Enfin, une fenêtre où nous devons entrer les données personnalisées apparaîtra, dans laquelle nous pouvons définir le `title` et `click_action`. Cet événement de clic est déclenché chaque fois que nous cliquons sur la notification qui apparaît dans la barre de notification de l'appareil. 

Après avoir cliqué sur le message de notification dans la barre de notification, l'application s'ouvrira et le callback `onResume` se déclenchera, définissant `title` comme assigné dans les données personnalisées dans la capture d'écran ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-79.png)

Maintenant, nous sommes prêts à envoyer le premier message de notification à l'appareil. Essayons d'abord avec l'appareil en cours d'exécution dans l'émulateur.

Lorsque nous cliquons sur le bouton 'Revoir' et envoyons le message, nous obtiendrons le résultat suivant dans la console Cloud Messaging ainsi que dans l'émulateur :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/pushGIF1.gif)

Ici, nous pouvons voir que le titre et l'alerte de notification sur l'écran de l'émulateur sont mis à jour dès que nous envoyons un message depuis la console. Nous pouvons être sûrs que le callback `onMessage` a été déclenché dans l'application après avoir reçu le message de notification.

Maintenant, essayons avec l'application en cours d'exécution en arrière-plan. Lorsque nous envoyons le message depuis la console, nous obtiendrons le résultat comme montré dans la démonstration ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/pushGIF2.gif)

Ici, dès que nous envoyons le message, nous recevons une notification push dans la barre de notification de l'appareil. Ensuite, lorsque nous faisons glisser la barre de notification vers le bas, nous pouvons voir le titre et le texte du message de notification. Et, en cliquant sur le message de notification, nous pouvons lancer l'application et afficher les données personnalisées à l'écran. Cela garantit que notre callback `onResume` a été déclenché.

Et c'est tout ! Nous avons réussi à ajouter une fonctionnalité de notification push dans notre application Flutter en utilisant Firebase Cloud Messaging.

## Conclusion

Les notifications push sont essentielles dans toute application. Elles peuvent être utilisées pour alerter les utilisateurs sur ce qui se passe dans l'application et peuvent aider à susciter l'intérêt des utilisateurs pour l'application. 

De plus, Firebase Cloud Messaging simplifie et facilite l'envoi d'alertes de notification. 

Dans ce tutoriel, nous avons commencé par configurer l'application Firebase, puis nous sommes passés à la configuration et à l'implémentation de la configuration de messagerie Firebase dans l'application Flutter. Enfin, nous avons pu envoyer des alertes de notification à l'application en utilisant Firebase Cloud Messaging. 

Le tutoriel était destiné à être simple et facile à comprendre. J'espère qu'il vous aidera à ajouter des notifications push à vos applications Flutter. Vous voulez voir des exemples de la façon dont vous pouvez implémenter tout cela ? Consultez ces puissants [modèles Flutter](http://instaflutter.com).