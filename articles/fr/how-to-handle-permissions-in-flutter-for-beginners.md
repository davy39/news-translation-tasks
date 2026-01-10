---
title: 'Comment gérer les permissions dans Flutter : Un guide complet'
subtitle: ''
author: Atuoha Anthony
co_authors: []
series: null
date: '2025-08-27T15:59:25.274Z'
originalURL: https://freecodecamp.org/news/how-to-handle-permissions-in-flutter-for-beginners
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1756310343452/8db020d5-5cec-4b88-9a02-a8dc2a81190c.png
tags:
- name: Flutter
  slug: flutter
- name: flutter-aware
  slug: flutter-aware
- name: permissions
  slug: permissions
- name: Beginner Developers
  slug: beginners
seo_title: 'Comment gérer les permissions dans Flutter : Un guide complet'
seo_desc: Permissions are crucial when building mobile applications that require access
  to device features such as location, camera, contacts, microphone, storage, and
  more. And handling permissions effectively ensures that your app provides a seamless
  user ex...
---

Les permissions sont cruciales lors de la création d'applications mobiles qui nécessitent l'accès aux fonctionnalités de l'appareil telles que la localisation, la caméra, les contacts, le microphone, le stockage, et bien plus encore. Gérer efficacement les permissions garantit que votre application offre une expérience utilisateur fluide tout en respectant les exigences de confidentialité et de sécurité.

Dans Flutter, l'un des packages les plus populaires pour gérer les permissions est [`permission_handler`](https://pub.dev/packages/permission_handler). Cet article vous guidera sur la manière de :

1. Installer et configurer `permission_handler` et `fluttertoast` 
    
2. Demander et gérer différentes permissions 
    
3. Comprendre ce que fait chaque permission et ses cas d'utilisation 
    
4. Gérer les configurations Android et iOS 
    
5. Implémenter les meilleures pratiques 
    
6. Gérer le test des permissions 
    
7. Fournir les résultats attendus et les conclusions 
    

## Table des matières :

* [Table des matières :](#heading-table-des-matieres)
    
* [1\. Prérequis](#heading-1-prerequis)
    
* [2\. Installation des dépendances](#heading-2-installation-des-dependances)
    
* [3\. Comprendre les états de permission](#heading-3-comprendre-les-etats-de-permission)
    
* [4\. Fonction réutilisable de gestion des permissions](#heading-4-fonction-reutilisable-de-gestion-des-permissions)
    
* [5\. Permissions, leurs cas d'utilisation et exemples](#heading-5-permissions-leurs-cas-dutilisation-et-exemples)
    
    * [5.1 Permissions de calendrier](#heading-51-permissions-de-calendrier)
        
    * [5.2 Permission de caméra](#heading-52-permission-de-camera)
        
    * [5.3 Permission de contacts](#heading-53-permission-de-contacts)
        
    * [5.4 Permissions de localisation](#heading-54-permissions-de-localisation)
        
    * [5.5 Bibliothèque multimédia (iOS uniquement)](#heading-55-bibliotheque-multimedia-ios-uniquement)
        
    * [5.6 Permission de microphone](#heading-56-permission-de-microphone)
        
    * [5.7 Permission de téléphone](#heading-57-permission-de-telephone)
        
    * [5.8 Permissions de photos](#heading-58-permissions-de-photos)
        
    * [5.9 Permission de rappels](#heading-59-permission-de-rappels)
        
    * [5.10 Permissions de capteurs](#heading-510-permissions-de-capteurs)
        
    * [5.11 Permission SMS](#heading-511-permission-sms)
        
    * [5.12 Permission de reconnaissance vocale](#heading-512-permission-de-reconnaissance-vocale)
        
    * [5.13 Permissions de stockage](#heading-513-permissions-de-stockage)
        
    * [5.14 Ignorer les optimisations de batterie](#heading-514-ignorer-les-optimisations-de-batterie)
        
    * [5.15 Notifications](#heading-515-notifications)
        
    * [5.16 Permissions Bluetooth](#heading-516-permissions-bluetooth)
        
    * [5.17 Transparence du suivi des applications (iOS uniquement)](#heading-517-transparence-du-suivi-des-applications-ios-uniquement)
        
* [6\. Configuration d'Android Manifest](#heading-6-configuration-dandroid-manifest)
    
* [7\. Configuration d'iOS Info.plist](#heading-7-configuration-dios-infoplist)
    
* [8\. Résultats attendus](#heading-8-resultats-attendus)
    
* [Meilleures pratiques pour la gestion des permissions dans Flutter](#heading-meilleures-pratiques-pour-la-gestion-des-permissions-dans-flutter)
    
    * [1\. Ne demandez que les permissions nécessaires](#heading-1-ne-demandez-que-les-permissions-necessaires)
        
    * [2\. Expliquez pourquoi les permissions sont nécessaires](#heading-2-expliquez-pourquoi-les-permissions-sont-necessaires)
        
    * [3\. Utilisez des demandes de permission au moment de l'exécution](#heading-3-utilisez-des-demandes-de-permission-au-moment-de-lexecution)
        
    * [4\. Gérez le refus avec élégance](#heading-4-gerez-le-refus-avec-elegance)
        
    * [5\. Gérez les refus permanents](#heading-5-gerez-les-refus-permanents)
        
    * [6\. Testez sur les deux plateformes](#heading-6-testez-sur-les-deux-plateformes)
        
    * [7\. Suivez les directives des plateformes](#heading-7-suivez-les-directives-des-plateformes)
        
    * [8\. Évitez l'excès de permissions](#heading-8-evitez-lexces-de-permissions)
        
    * [9\. Utilisez un gestionnaire de permissions centralisé](#heading-9-utilisez-un-gestionnaire-de-permissions-centralise)
        
    * [10\. Surveillez les changements de permission](#heading-10-surveillez-les-changements-de-permission)
        
* [Conclusion](#heading-conclusion)
    
* [Références](#heading-references)
    

## 1\. Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants :

1. SDK Flutter installé (version 3.0.0 ou supérieure recommandée)
    
2. Un éditeur de code tel qu'Android Studio ou VS Code
    
3. Compréhension de base des widgets Flutter, d'async/await en Dart et de la gestion d'état
    
4. Un appareil physique (recommandé) ou un émulateur/simulateur
    
5. Connexion Internet pour installer les dépendances
    

## 2\. Installation des dépendances

Pour commencer, ajoutez ce qui suit à votre fichier `pubspec.yaml` :

```yaml
dependencies:
  permission_handler: ^11.3.1
  fluttertoast: ^8.2.4
```

Ensuite, exécutez :

```bash
flutter pub get
```

* `permission_handler` est utilisé pour demander et vérifier les permissions sur Android et iOS.
    
* `fluttertoast` vous permet d'afficher des messages aux utilisateurs lorsque les permissions sont accordées ou refusées.
    

## 3\. Comprendre les états de permission

Lors de la demande de permissions avec `permission_handler`, vous pouvez obtenir les états suivants :

1. `isGranted` – La permission est accordée.
    
2. `isDenied` – La permission est refusée, mais peut être demandée à nouveau.
    
3. `isPermanentlyDenied` – La permission est refusée de manière permanente, ce qui signifie que l'utilisateur doit l'activer depuis les **paramètres de l'application**.
    
4. `isRestricted` – La permission est restreinte par le système (courant sur iOS).
    
5. `isLimited` – Accès partiel accordé (principalement pour la bibliothèque de photos iOS).
    

## 4\. Fonction réutilisable de gestion des permissions

Au lieu d'écrire plusieurs fonctions pour chaque permission, nous allons créer une fonction réutilisable :

```dart
import 'package:permission_handler/permission_handler.dart';
import 'package:fluttertoast/fluttertoast.dart';

Future<void> handlePermission(Permission permission, String name) async {
  var status = await permission.request();

  if (status.isGranted) {
    Fluttertoast.showToast(msg: 'Permission $name accordée');
  } else if (status.isPermanentlyDenied) {
    Fluttertoast.showToast(msg: 'Permission $name refusée de manière permanente. Activez-la dans les paramètres.');
    openAppSettings();
  } else if (status.isRestricted) {
    Fluttertoast.showToast(msg: 'Permission $name restreinte par le système.');
  } else if (status.isLimited) {
    Fluttertoast.showToast(msg: 'Accès limité accordé pour la permission $name.');
  } else {
    Fluttertoast.showToast(msg: 'Permission $name refusée');
  }
}
```

Exemple d'utilisation :

```dart
await handlePermission(Permission.camera, "Caméra");
await handlePermission(Permission.location, "Localisation");
```

## 5\. Permissions, leurs cas d'utilisation et exemples

Examinons maintenant plusieurs types de permissions que vous pourriez avoir à activer dans vos applications Flutter. J'expliquerai ce que fait la permission et ses cas d'utilisation courants.

### 5.1 Permissions de calendrier

* **Permission :** `calendar`, `calendarReadOnly`, `calendarFullAccess`
    
* **Ce qu'elle fait :** Accède au calendrier de l'utilisateur pour lire ou écrire des événements.
    
* **Cas d'utilisation :** Applications d'événements, applications de planification.
    

```dart
await handlePermission(Permission.calendar, "Calendrier");
```

### 5.2 Permission de caméra

* **Permission :** `camera`
    
* **Ce qu'elle fait :** Accède à la caméra de l'appareil pour capturer des photos/vidéos.
    
* **Cas d'utilisation :** Scan de QR codes, applications de photo, enregistrement vidéo.
    

```dart
await handlePermission(Permission.camera, "Caméra");
```

### 5.3 Permission de contacts

* **Permission :** `contacts`
    
* **Ce qu'elle fait :** Lit ou modifie les contacts de l'utilisateur.
    
* **Cas d'utilisation :** Applications de messagerie, applications de réseaux sociaux.
    

```dart
await handlePermission(Permission.contacts, "Contacts");
```

### 5.4 Permissions de localisation

* **Permission :** `location`, `locationAlways`, `locationWhenInUse`
    
* **Ce qu'elle fait :** Accède à la localisation de l'utilisateur.
    
* **Cas d'utilisation :** Applications de navigation, applications de VTC, gardiennage virtuel (geofencing).
    

```dart
await handlePermission(Permission.locationWhenInUse, "Localisation");
```

### 5.5 Bibliothèque multimédia (iOS uniquement)

* **Permission :** `mediaLibrary`
    
* **Ce qu'elle fait :** Accède aux fichiers multimédias sur les appareils iOS.
    
* **Cas d'utilisation :** Applications de partage de photos, éditeurs multimédias.
    

```dart
await handlePermission(Permission.mediaLibrary, "Bibliothèque multimédia");
```

### 5.6 Permission de microphone

* **Permission :** `microphone`
    
* **Ce qu'elle fait :** Enregistre de l'audio.
    
* **Cas d'utilisation :** Notes vocales, appels vidéo, commandes vocales.
    

```dart
await handlePermission(Permission.microphone, "Microphone");
```

### 5.7 Permission de téléphone

* **Permission :** `phone`
    
* **Ce qu'elle fait :** Accède à l'état du téléphone, passe des appels, lit les journaux d'appels.
    
* **Cas d'utilisation :** Applications de téléphonie, applications de gestion d'appels.
    

```dart
await handlePermission(Permission.phone, "Téléphone");
```

### 5.8 Permissions de photos

* **Permission :** `photos`, `photosAddOnly`
    
* **Ce qu'elle fait :** Accède ou ajoute des photos à la bibliothèque de l'utilisateur.
    
* **Cas d'utilisation :** Applications multimédias, applications sociales.
    

```dart
await handlePermission(Permission.photos, "Photos");
```

### 5.9 Permission de rappels

* **Permission :** `reminders`
    
* **Ce qu'elle fait :** Accède et gère les rappels de l'appareil.
    
* **Cas d'utilisation :** Applications de listes de tâches, applications de productivité.
    

```dart
await handlePermission(Permission.reminders, "Rappels");
```

### 5.10 Permissions de capteurs

* **Permission :** `sensors`, `sensorsAlways`
    
* **Ce qu'elle fait :** Accède aux capteurs de l'appareil comme l'accéléromètre ou le gyroscope.
    
* **Cas d'utilisation :** Applications de fitness, applications de suivi de mouvement.
    

```dart
await handlePermission(Permission.sensors, "Capteurs");
```

### 5.11 Permission SMS

* **Permission :** `sms`
    
* **Ce qu'elle fait :** Lit ou envoie des messages SMS.
    
* **Cas d'utilisation :** Vérification OTP, applications de messagerie.
    

```dart
await handlePermission(Permission.sms, "SMS");
```

### 5.12 Permission de reconnaissance vocale

* **Permission :** `speech`
    
* **Ce qu'elle fait :** Utilise les fonctionnalités de synthèse vocale.
    
* **Cas d'utilisation :** Commandes vocales, applications de dictée.
    

```dart
await handlePermission(Permission.speech, "Reconnaissance vocale");
```

### 5.13 Permissions de stockage

* **Permission :** `storage`, `manageExternalStorage`
    
* **Ce qu'elle fait :** Accède au stockage interne/externe pour lire/écrire des fichiers.
    
* **Cas d'utilisation :** Gestionnaires de fichiers, gestionnaires de téléchargement.
    

```dart
await handlePermission(Permission.storage, "Stockage");
```

### 5.14 Ignorer les optimisations de batterie

* **Permission :** `ignoreBatteryOptimizations`
    
* **Ce qu'elle fait :** Demande à exclure l'application des optimisations de batterie.
    
* **Cas d'utilisation :** Applications d'alarme, services en arrière-plan.
    

```dart
await handlePermission(Permission.ignoreBatteryOptimizations, "Optimisations de batterie");
```

### 5.15 Notifications

* **Permission :** `notification`
    
* **Ce qu'elle fait :** Autorise l'envoi de notifications.
    
* **Cas d'utilisation :** Messagerie, rappels, alertes.
    

```dart
await handlePermission(Permission.notification, "Notifications");
```

### 5.16 Permissions Bluetooth

* **Permission :** `bluetooth`, `bluetoothScan`, `bluetoothAdvertise`, `bluetoothConnect`
    
* **Ce qu'elle fait :** Gère ou se connecte à des appareils Bluetooth.
    
* **Cas d'utilisation :** Objets connectés (wearables), appareils IoT, écouteurs.
    

```dart
await handlePermission(Permission.bluetooth, "Bluetooth");
```

### 5.17 Transparence du suivi des applications (iOS uniquement)

* **Permission :** `appTrackingTransparency`
    
* **Ce qu'elle fait :** Demande la permission de suivi pour des publicités personnalisées.
    
* **Cas d'utilisation :** Analytique, publicité, suivi de l'utilisateur.
    

```dart
await handlePermission(Permission.appTrackingTransparency, "Suivi d'application");
```

## 6\. Configuration d'Android Manifest

Sur **Android**, toutes les applications doivent déclarer les permissions qu'elles ont l'intention d'utiliser dans le fichier `AndroidManifest.xml`. Cela agit comme le « contrat » de l'application avec le système, informant Android des ressources sensibles (comme Internet, la localisation, la caméra) que l'application pourrait demander.

Sans ces déclarations dans le manifeste, les demandes de permission au moment de l'exécution échoueront, même si vous avez ajouté le package `permission_handler`.

Par exemple, si vous essayez d'accéder à la caméra sans avoir préalablement déclaré la permission de caméra ici, votre application plantera ou échouera lors de la demande au moment de l'exécution.

Voici une liste complète des permissions courantes :

```xml
<!-- Accès à la caméra pour prendre des photos ou enregistrer des vidéos -->
<uses-permission android:name="android.permission.CAMERA" />

<!-- Lire les contacts de l'utilisateur (ex: pour des fonctionnalités sociales) -->
<uses-permission android:name="android.permission.READ_CONTACTS" />

<!-- Localisation précise (GPS) pour les cartes, la navigation -->
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />

<!-- Localisation approximative (basée sur le réseau) -->
<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />

<!-- Enregistrer de l'audio depuis le microphone -->
<uses-permission android:name="android.permission.RECORD_AUDIO" />

<!-- Lire le stockage externe (accéder aux fichiers de l'utilisateur) -->
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />

<!-- Écrire sur le stockage externe (sauvegarder des fichiers, des photos) -->
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />

<!-- Envoyer des SMS directement depuis l'application -->
<uses-permission android:name="android.permission.SEND_SMS" />

<!-- Recevoir des SMS (lire les messages OTP pour la connexion) -->
<uses-permission android:name="android.permission.RECEIVE_SMS" />

<!-- Lire les messages SMS (remplissage automatique OTP) -->
<uses-permission android:name="android.permission.READ_SMS" />

<!-- Utilisation du Bluetooth -->
<uses-permission android:name="android.permission.BLUETOOTH" />

<!-- Admin Bluetooth (gérer les appareils appairés) -->
<uses-permission android:name="android.permission.BLUETOOTH_ADMIN" />

<!-- Scan Bluetooth (nécessaire à partir d'Android 12+) -->
<uses-permission android:name="android.permission.BLUETOOTH_SCAN" />

<!-- Connexion Bluetooth (nécessaire à partir d'Android 12+) -->
<uses-permission android:name="android.permission.BLUETOOTH_CONNECT" />

<!-- Publicité Bluetooth (pour les applications de type balise, Android 12+) -->
<uses-permission android:name="android.permission.BLUETOOTH_ADVERTISE" />

<!-- Ignorer les optimisations de batterie -->
<uses-permission android:name="android.permission.REQUEST_IGNORE_BATTERY_OPTIMIZATIONS" />

<!-- Accès Internet -->
<uses-permission android:name="android.permission.INTERNET" />

<!-- Vérifier si une connexion réseau existe -->
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />

<!-- Accès à l'état WiFi -->
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />

<!-- Modifier l'état WiFi -->
<uses-permission android:name="android.permission.CHANGE_WIFI_STATE" />

<!-- Accéder à l'état du téléphone (ID de l'appareil, SIM) -->
<uses-permission android:name="android.permission.READ_PHONE_STATE" />

<!-- Passer des appels téléphoniques directement -->
<uses-permission android:name="android.permission.CALL_PHONE" />

<!-- Utiliser l'authentification par empreinte digitale -->
<uses-permission android:name="android.permission.USE_FINGERPRINT" />

<!-- Utiliser l'authentification biométrique (plus récent que l'empreinte) -->
<uses-permission android:name="android.permission.USE_BIOMETRIC" />
```

## 7\. Configuration d'iOS `Info.plist`

Pour iOS, vous devez fournir des clés descriptives dans le fichier `Info.plist` pour informer les utilisateurs de la raison pour laquelle votre application a besoin de permissions spécifiques. Voici les configurations pour chaque exemple de permission :

1. **Permission de caméra**
    
    ```xml
    <key>NSCameraUsageDescription</key>
    <string>Nous avons besoin d'accéder à votre caméra pour prendre des photos.</string>
    ```
    
2. **Permission de contacts**
    
    ```xml
    <key>NSContactsUsageDescription</key>
    <string>Nous avons besoin d'accéder à vos contacts pour une meilleure communication.</string>
    ```
    
3. **Permissions de localisation**
    
    ```xml
    <key>NSLocationWhenInUseUsageDescription</key>
    <string>Nous avons besoin d'accéder à votre localisation pour fournir des services géolocalisés.</string>
    <key>NSLocationAlwaysUsageDescription</key>
    <string>Nous avons besoin d'accéder à votre localisation pour suivre vos déplacements même quand l'application n'est pas active.</string>
    ```
    
4. **Permission de bibliothèque multimédia/stockage**
    
    ```xml
    <key>NSPhotoLibraryUsageDescription</key>
    <string>Nous avons besoin d'accéder à vos photos pour partager ou télécharger des médias.</string>
    ```
    
5. **Permission de microphone**
    
    ```xml
    <key>NSMicrophoneUsageDescription</key>
    <string>Nous avons besoin d'accéder à votre microphone pour l'enregistrement vocal.</string>
    ```
    
6. **Permission de téléphone**
    
    ```xml
    <key>NSPhoneUsageDescription</key>
    <string>Nous avons besoin d'accéder aux services téléphoniques pour permettre les appels.</string>
    ```
    
7. **Permission de photos**
    
    ```xml
    <key>NSPhotoLibraryAddUsageDescription</key>
    <string>Nous avons besoin de la permission d'ajouter des photos à votre bibliothèque.</string>
    ```
    
8. **Permission de rappels**
    
    ```xml
    <key>NSRemindersUsageDescription</key>
    <string>Nous avons besoin d'accéder à vos rappels pour la gestion des tâches.</string>
    ```
    
9. **Permission de capteurs**
    
    ```xml
    <key>NSSensorsUsageDescription</key>
    <string>Nous avons besoin d'accéder à vos capteurs pour le suivi de la condition physique.</string>
    ```
    
10. **Permission SMS** (Gérée automatiquement par iOS si les services SMS sont demandés)
    
11. **Permission de reconnaissance vocale**
    

```xml
<key>NSSpeechRecognitionUsageDescription</key>
<string>Nous avons besoin d'accéder à la reconnaissance vocale pour les commandes vocales.</string>
```

12. **Ignorer les optimisations de batterie** (Non applicable sur iOS)
    
13. **Permission de notifications**
    

```xml
<key>NSUserNotificationUsageDescription</key>
<string>Nous avons besoin de la permission pour envoyer des notifications.</string>
```

14. **Permission d'accès à la localisation des médias** (Gérée automatiquement sur iOS)
    
15. **Permission de reconnaissance d'activité**
    

```xml
<key>NSMotionUsageDescription</key>
<string>Nous avons besoin d'accéder aux données de mouvement pour le suivi de la condition physique.</string>
```

16. **Permissions Bluetooth**
    

```xml
<key>NSBluetoothPeripheralUsageDescription</key>
<string>Nous avons besoin d'accéder au Bluetooth pour la connectivité de l'appareil.</string>
```

17. **Transparence du suivi des applications**
    

```xml
<key>NSUserTrackingUsageDescription</key>
<string>Nous avons besoin de la permission de suivre votre activité à travers les applications et sites web pour des publicités personnalisées.</string>
```

## 8\. Résultats attendus

En implémentant les permissions et les vérifications de connectivité de cette manière, votre application Flutter :

1. Demandera les permissions dynamiquement au moment de l'exécution de manière conviviale.
    
2. Gérera tous les états possibles avec élégance, y compris accordé, refusé, refusé de manière permanente, restreint et limité.
    
3. Fournira aux utilisateurs des retours significatifs, en les guidant vers les paramètres si nécessaire.
    
4. Maintiendra la conformité avec les politiques de permission d'Android et iOS tout en garantissant sécurité et transparence.
    
5. Écoutera en continu les changements de connectivité réseau via l'écouteur global BLoC.
    
6. Notifiera instantanément les utilisateurs avec un toast/snackbar chaque fois que l'état Internet change (connecté/déconnecté).
    
7. Réduira les appels API redondants et améliorera l'UX en évitant les états « faux » hors ligne ou uniquement en cache.
    

## Meilleures pratiques pour la gestion des permissions dans Flutter

Il existe quelques meilleures pratiques courantes que vous devriez suivre lors de la gestion des permissions dans Flutter.

### 1\. Ne demandez que les permissions nécessaires

Ne demandez que les permissions dont votre application a réellement besoin. Par exemple, si votre application ne fait que télécharger des images, vous n'avez probablement besoin que de l'accès au **stockage/photos**, pas à la localisation, aux contacts ou aux SMS.

```dart
final status = await Permission.photos.request();
if (status.isGranted) {
  // Procéder au téléchargement de la photo
}
```

### 2\. Expliquez pourquoi les permissions sont nécessaires

Dites toujours à l'utilisateur *pourquoi* vous demandez une permission sensible avant que la boîte de dialogue du système n'apparaisse. Cela aide à instaurer la confiance.

Exemple d'une boîte de dialogue personnalisée avant la demande :

```dart
Future<void> _showPermissionRationale(BuildContext context) async {
  showDialog(
    context: context,
    builder: (context) => AlertDialog(
      title: Text("Accès à la caméra nécessaire"),
      content: Text("Nous avons besoin d'accéder à votre caméra pour que vous puissiez prendre des photos de profil."),
      actions: [
        TextButton(
          onPressed: () {
            Navigator.pop(context);
            Permission.camera.request();
          },
          child: Text("Autoriser"),
        ),
        TextButton(
          onPressed: () => Navigator.pop(context),
          child: Text("Annuler"),
        ),
      ],
    ),
  );
}
```

### 3\. Utilisez des demandes de permission au moment de l'exécution

Sur Android 6.0+ et iOS, les permissions doivent être demandées **au moment de l'exécution** (pas seulement déclarées dans `AndroidManifest.xml` ou `Info.plist`).

```dart
final status = await Permission.location.request();
if (status.isGranted) {
  // Utiliser la localisation
}
```

### 4\. Gérez le refus avec élégance

Ne bloquez pas toute l'application lorsque les permissions sont refusées. Proposez des flux alternatifs.

Par exemple, au lieu de forcer l'accès à la caméra :

```dart
if (await Permission.camera.isDenied) {
  // Proposer le téléchargement de fichier comme alternative
  _pickImageFromGallery();
}
```

De cette façon, les utilisateurs peuvent toujours utiliser votre application sans y être forcés.

### 5\. Gérez les refus permanents

Lorsqu'un utilisateur sélectionne *« Ne plus demander »* (Android) ou désactive une permission dans les Réglages (iOS), vous devriez le guider vers les **Paramètres**.

```dart
if (await Permission.camera.isPermanentlyDenied) {
  openAppSettings(); // Amène l'utilisateur aux paramètres de l'application
}
```

Exemple UX :

* Afficher un snackbar : *« L'accès à la caméra est requis. Activez-le dans les Paramètres. »* avec un bouton **Aller aux Paramètres**.
    

### 6\. Testez sur les deux plateformes

Les permissions se comportent différemment sur Android et iOS. Exemple :

* iOS peut renvoyer un accès limité à la bibliothèque de photos.
    
* Android 13+ a de nouvelles permissions multimédias granulaires (`READ_MEDIA_IMAGES`, `READ_MEDIA_VIDEO`).
    

Testez toujours tous les scénarios :

* Accordé
    
* Refusé une fois
    
* Refusé de manière permanente
    
* Limité (iOS uniquement)
    

### 7\. Suivez les directives des plateformes

Assurez-vous que votre manifeste et votre Info.plist contiennent des explications claires.

**Exemple Info.plist (iOS) :**

```xml
<key>NSCameraUsageDescription</key>
<string>Cette application nécessite l'accès à la caméra pour vous permettre de prendre des photos de profil.</string>
```

Ceci est requis pour l'approbation sur l'App Store.

### 8\. Évitez l'excès de permissions

Exemple : Ne demandez pas les SMS si vous avez seulement besoin du remplissage automatique du numéro de téléphone. Les utilisateurs abandonneront votre application s'ils voient des demandes non pertinentes.

**Mauvais :**

```xml
<uses-permission android:name="android.permission.SEND_SMS" />
```

Utilisez simplement `READ_PHONE_NUMBERS` si c'est le besoin réel.

### 9\. Utilisez un gestionnaire de permissions centralisé

Au lieu de disperser les demandes dans toute l'application, créez un `PermissionService` qui gère toutes les demandes de manière cohérente.

```dart
class PermissionService {
  Future<bool> requestCamera() async {
    final status = await Permission.camera.request();
    return status.isGranted;
  }

  Future<bool> requestLocation() async {
    final status = await Permission.location.request();
    return status.isGranted;
  }
}
```

Cela maintient une gestion des permissions uniforme.

### 10\. Surveillez les changements de permission

Les permissions peuvent changer pendant que l'application est ouverte (l'utilisateur va dans les Paramètres et les désactive). Vérifiez toujours avant l'utilisation.

```dart
@override
void initState() {
  super.initState();
  Timer.periodic(Duration(seconds: 5), (timer) async {
    final cameraStatus = await Permission.camera.status;
    if (!cameraStatus.isGranted) {
      // Désactiver l'UI de la caméra
    }
  });
}
```

## Conclusion

Les permissions sont fondamentales pour créer des applications mobiles entièrement fonctionnelles et sécurisées. L'utilisation de `permission_handler` dans Flutter vous permet de gérer efficacement les permissions sur Android et iOS.

Et n'oubliez pas : demandez toujours uniquement les permissions nécessaires, fournissez des explications claires et gérez tous les états possibles pour maintenir la confiance des utilisateurs.

En combinant une logique de permission correcte avec une configuration appropriée d'AndroidManifest et d'Info.plist, vous garantissez une expérience utilisateur fluide tout en restant conforme aux directives des plateformes.

## Références

1. [Documentation du package Flutter permission\_handler](https://pub.dev/packages/permission_handler)
    
2. [Documentation officielle de Flutter : Gestion des permissions](https://docs.flutter.dev/cookbook/plugins/picture-using-camera)
    
3. [Guide pour développeurs Android : Permissions](https://developer.android.com/guide/topics/permissions/overview)
    
4. [Guide pour développeurs iOS : Permissions d'application](https://developer.apple.com/documentation/bundleresources/information_property_list)
    
5. [Documentation du package Fluttertoast](https://pub.dev/packages/fluttertoast)