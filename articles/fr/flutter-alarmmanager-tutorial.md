---
title: Comment définir des alarmes dans Flutter en utilisant le package Alarm Manager
  Plus
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2022-07-13T20:21:04.000Z'
originalURL: https://freecodecamp.org/news/flutter-alarmmanager-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/sonja-langford-eIkbSc3SDtI-unsplash.jpg
tags:
- name: Flutter
  slug: flutter
seo_title: Comment définir des alarmes dans Flutter en utilisant le package Alarm
  Manager Plus
seo_desc: "If you are an Android developer, when you want to schedule your application\
  \ to run at a specific time in the future, you use the AlarmManager. \nBut if you\
  \ are an iOS developer, this type of component does not exist there.\nSo if you\
  \ are a Flutter deve..."
---

Si vous êtes un développeur Android, lorsque vous souhaitez planifier votre application pour qu'elle s'exécute à un moment spécifique dans le futur, vous utilisez AlarmManager. 

Mais si vous êtes un développeur iOS, ce type de composant n'existe pas là-bas.

Alors, si vous êtes un développeur Flutter, que faites-vous ?

Comme pour la plupart des choses liées à Flutter, lorsque vous souhaitez utiliser un composant spécifique à une plateforme, vous devez exposer sa fonctionnalité.

AlarmManager ne fait pas exception.

Dans cet article, nous allons passer en revue le package [Android AlarmManager Plus](https://pub.dev/packages/android_alarm_manager_plus) et montrer comment vous pouvez l'utiliser dans votre application.

Prêt à définir votre alarme ?

## Installation du projet

Tout d'abord, ouvrez votre fichier pubspec.yaml et ajoutez ce qui suit :

```yaml
dependencies:
  android_alarm_manager_plus: ^2.0.6
```

> ❓ Avertissement ➡ Lorsque j'ai écrit cet article, la dernière version était 2.0.6

Ensuite, exécutez **`pub get`** pour télécharger la dépendance.

Nous allons utiliser le projet vanilla que vous obtenez lorsque vous créez un projet Flutter dans Android Studio (sans toute la logique de compteur).

Ouvrez votre fichier AndroidManifest.xml et ajoutez les permissions suivantes :

```xml
<uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED"/>
<uses-permission android:name="android.permission.WAKE_LOCK"/>

<!-- Pour les applications avec targetSDK=31 (Android 12) -->
<uses-permission android:name="android.permission.SCHEDULE_EXACT_ALARM"/>
```

À l'intérieur de votre balise application, ajoutez également ceci :

```xml
<service
    android:name="dev.fluttercommunity.plus.androidalarmmanager.AlarmService"
    android:permission="android.permission.BIND_JOB_SERVICE"
    android:exported="false"/>
<receiver
    android:name="dev.fluttercommunity.plus.androidalarmmanager.AlarmBroadcastReceiver"
    android:exported="false"/>
<receiver
    android:name="dev.fluttercommunity.plus.androidalarmmanager.RebootBroadcastReceiver"
    android:enabled="false"
    android:exported="false">
    <intent-filter>
        <action android:name="android.intent.action.BOOT_COMPLETED" />
    </intent-filter>
</receiver>
```

À la fin, votre fichier AndroidManifest devrait ressembler à ceci :

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.tomerpacific.alarm_manager_example">

    <uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED"/>
    <uses-permission android:name="android.permission.WAKE_LOCK"/>
    <!-- Pour les applications avec targetSDK=31 (Android 12) -->
    <uses-permission android:name="android.permission.SCHEDULE_EXACT_ALARM"/>

   <application
        android:label="alarm_manager_example"
        android:name="${applicationName}"
        android:icon="@mipmap/ic_launcher">
        <activity
            android:name=".MainActivity"
            android:exported="true"
            android:launchMode="singleTop"
            android:theme="@style/LaunchTheme"
            android:configChanges="orientation|keyboardHidden|keyboard|screenSize|smallestScreenSize|locale|layoutDirection|fontScale|screenLayout|density|uiMode"
            android:hardwareAccelerated="true"
            android:windowSoftInputMode="adjustResize">
            <!-- Spécifie un thème Android à appliquer à cette activité dès que
                 le processus Android a démarré. Ce thème est visible par l'utilisateur
                 pendant que l'UI Flutter s'initialise. Après cela, ce thème continue
                 à déterminer l'arrière-plan de la fenêtre derrière l'UI Flutter. -->
            <meta-data
              android:name="io.flutter.embedding.android.NormalTheme"
              android:resource="@style/NormalTheme"
              />
            <intent-filter>
                <action android:name="android.intent.action.MAIN"/>
                <category android:name="android.intent.category.LAUNCHER"/>
            </intent-filter>
        </activity>
        <!-- Ne supprimez pas les meta-data ci-dessous.
             Cela est utilisé par l'outil Flutter pour générer GeneratedPluginRegistrant.java -->
        <meta-data
            android:name="flutterEmbedding"
            android:value="2" />
       <service
           android:name="dev.fluttercommunity.plus.androidalarmmanager.AlarmService"
           android:permission="android.permission.BIND_JOB_SERVICE"
           android:exported="false"/>
       <receiver
           android:name="dev.fluttercommunity.plus.androidalarmmanager.AlarmBroadcastReceiver"
           android:exported="false"/>
       <receiver
           android:name="dev.fluttercommunity.plus.androidalarmmanager.RebootBroadcastReceiver"
           android:enabled="false"
           android:exported="false">
           <intent-filter>
               <action android:name="android.intent.action.BOOT_COMPLETED" />
           </intent-filter>
       </receiver>
    </application>
</manifest>
```

## Les cloches d'alarme sonnent

Le package expose un objet **AndroidAlarmManager** qui possède les méthodes suivantes (pertinentes) :

* **oneShot** – déclenche une alarme ponctuelle
* **oneShotAt** – déclenche une alarme ponctuelle à une date spécifique
* **periodic** – déclenche une alarme à intervalles de temps définis

Discutons de chaque option en détail.

### Comment fonctionne la méthode `oneShot`

La méthode **oneShot** accepte les arguments suivants :

```dart
 static Future<bool> oneShot(
    Duration delay,
    int id,
    Function callback, {
    bool alarmClock = false,
    bool allowWhileIdle = false,
    bool exact = false,
    bool wakeup = false,
    bool rescheduleOnReboot = false,
  })
```

Les trois premiers arguments (delay, id et callback) sont assez explicites, nous allons donc nous concentrer sur les autres.

* **alarmClock** – Un drapeau qui indique si le minuteur sera défini avec AlarmManagerCompact.setAlarmClock
* **allowWhileIdle** – Un drapeau qui indique si le minuteur sera défini avec AlarmManagerCompat.setExactAndAllowWhileIdle ou AlarmManagerCompat.setAndAllowWhileIdle
* **exact** – Un drapeau qui indique si le minuteur sera défini avec AlarmManagerCompat.setExact
* **wakeup** – Un drapeau qui indique si l'appareil sera réveillé lorsque l'alarme sera déclenchée
* **rescheduleOnReboot** – Un drapeau qui indique si l'alarme persistera entre les redémarrages de l'appareil

La méthode **oneShotAt** est très similaire à la méthode oneShot, avec une différence clé. Au lieu d'un délai de type Duration, le premier argument est un objet DateTime qui définit quand l'alarme sera déclenchée.

```dart
static Future<bool> oneShotAt(
    DateTime time,
    int id,
    Function callback, {
    bool alarmClock = false,
    bool allowWhileIdle = false,
    bool exact = false,
    bool wakeup = false,
    bool rescheduleOnReboot = false,
  })
```

La méthode **periodic** accepte les arguments suivants :

```dart
static Future<bool> periodic(
    Duration duration,
    int id,
    Function callback, {
    DateTime? startAt,
    bool allowWhileIdle = false,
    bool exact = false,
    bool wakeup = false,
    bool rescheduleOnReboot = false,
  })
```

Comme vous pouvez le voir, cette méthode est également similaire dans les arguments qu'elle prend. Les arguments qui comptent le plus ici sont :

* **startAt** – indique quand l'alarme doit être déclenchée pour la première fois
* **duration** – est responsable du redéclenchement de l'alarme à chaque intervalle de durée.

## N'oubliez pas de définir votre alarme

Une chose à savoir concernant le package Alarm Manager Plus est qu'il utilise des **isolates** pour exécuter les alarmes. Les isolates sont similaires aux threads sauf qu'ils ne partagent pas de mémoire. Par conséquent, ils communiquent avec des messages.

Pour cette raison, vous devez déclarer vos gestionnaires d'alarme (callbacks) comme statiques afin qu'ils puissent être accessibles.

Vous pouvez en savoir plus sur les isolates [ici](https://api.dart.dev/stable/2.0.0/dart-isolate/Isolate-class.html).

## Conclusion

Si vous souhaitez consulter un exemple de tout ce dont nous avons discuté dans cet article, rendez-vous [ici](https://github.com/TomerPacific/MediumArticles/tree/master/alarm_manager_example).

![Image](https://www.freecodecamp.org/news/content/images/2022/07/qemu-system-x86_64_MPlmZz44j0.png)