---
title: Comment sécuriser les API mobiles dans Flutter
subtitle: ''
author: Atuoha Anthony
co_authors: []
series: null
date: '2025-05-06T20:26:30.104Z'
originalURL: https://freecodecamp.org/news/how-to-secure-mobile-apis-in-flutter
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1746626043471/57ea35c5-44b8-4eee-b713-ca9e735d7fe7.png
tags:
- name: Flutter
  slug: flutter
- name: Dart
  slug: dart
- name: Security
  slug: security
- name: APIs
  slug: apis
seo_title: Comment sécuriser les API mobiles dans Flutter
seo_desc: 'As mobile applications continue to evolve in functionality and scope, securing
  the APIs that power these apps has become more critical than ever.

  In the context of Flutter, a framework that enables cross-platform development,
  understanding how to sec...'
---

Alors que les applications mobiles continuent d'évoluer en termes de fonctionnalités et de portée, la sécurisation des API qui alimentent ces applications est devenue plus cruciale que jamais.

Dans le contexte de Flutter, un framework qui permet le développement multiplateforme, comprendre comment sécuriser les API mobiles est essentiel – non seulement pour maintenir la confiance des utilisateurs, mais aussi pour protéger les données sensibles de l'entreprise.

Dans cet article, nous explorerons les vulnérabilités courantes des API dans les applications mobiles, en particulier les applications Flutter, et nous décrirons des stratégies pratiques pour atténuer ces risques.

### Table des matières

* [Pourquoi la sécurité des API est importante dans les applications mobiles](#heading-pourquoi-la-securite-des-api-est-importante-dans-les-applications-mobiles)
    
* [Exemple de configuration de projet](#heading-exemple-dinstallation-de-projet)
    
* [Vulnérabilités courantes dans les applications Flutter](#heading-vulnerabilites-courantes-dans-les-applications-flutter)
    
* [Exemple : Appel API sécurisé dans Flutter](#heading-exemple-appel-api-securise-dans-flutter)
    
* [Bonnes pratiques pour sécuriser les API dans les applications Flutter](#heading-bonnes-pratiques-pour-securiser-les-api-dans-les-applications-flutter)
    
* [Liste de contrôle de sécurité pour les développeurs Flutter](#heading-liste-de-controle-de-securite-pour-les-developpeurs-flutter)
    
* [Considérations supplémentaires](#heading-considerations-supplementaires)
    
* [Conclusion](#heading-conclusion)
    
* [Références](#heading-references)
    

Sécuriser les clés API dans une application Flutter est essentiel pour prévenir l'accès non autorisé aux ressources sensibles. Les clés API sont souvent utilisées pour l'authentification avec des services externes – mais si elles sont exposées, elles peuvent entraîner des vulnérabilités de sécurité.

Dans ce guide, nous discuterons de la manière de stocker et de gérer les clés API de manière sécurisée en utilisant Firebase Remote Config, Flutter Secure Storage, le chiffrement AES et les identifiants spécifiques aux appareils.

Il existe plusieurs façons de gérer les clés API de manière sécurisée, notamment :

* **Solutions CI/CD** : Des services comme Codemagic, CircleCI et GitHub Actions vous permettent de stocker les clés API en tant que variables d'environnement pour les garder hors de votre base de code.
    
* **Stockage backend** : Garder les clés API sur un serveur backend et les récupérer dynamiquement est une autre approche sécurisée.
    
* **Keystore & Keychain** : Sur Android et iOS, les clés API peuvent être stockées de manière sécurisée en utilisant les mécanismes de keystore intégrés de l'appareil.
    
* **Stockage chiffré** : Utiliser des solutions de stockage local chiffré pour sauvegarder les clés API sur l'appareil.
    

## Pourquoi la sécurité des API est importante dans les applications mobiles

Les API servent de pont entre les applications mobiles et les services backend. Bien qu'elles permettent des expériences dynamiques, telles que la récupération de données utilisateur, le traitement des paiements et la gestion de contenu en temps réel, elles deviennent également un vecteur d'attaque majeur si elles sont laissées non sécurisées.

Les applications mobiles, contrairement aux applications web, sont distribuées sous forme compilée (par exemple, APK). Celles-ci peuvent être décompilées pour révéler la logique, les endpoints et parfois même des secrets comme les clés API.

Les attaquants peuvent reverse engineer les APK, intercepter le trafic en utilisant des outils proxy comme Burp Suite, ou abuser des endpoints API via des émulateurs ou des scripts. Cela peut entraîner des violations de données, une manipulation non autorisée des données ou une interruption de service.

L'exposition publique des clés API dans votre application Flutter peut entraîner un accès non autorisé et un éventuel abus. Cela peut entraîner l'épuisement des quotas, des interruptions de service ou même des violations de sécurité. En utilisant Firebase Remote Config, le chiffrement et le stockage local sécurisé, nous pouvons garder les clés API en sécurité.

### **Exemple de configuration de projet :**

Pour cet exemple, nous nous concentrerons sur l'utilisation de **Firebase Remote Config** pour récupérer de manière sécurisée les clés API, les chiffrer avant de les stocker localement et les déchiffrer lorsque cela est nécessaire.

Nous structurerons une implémentation en utilisant les éléments suivants :

* `remote_config.dart` : Gère la récupération et le chiffrement des clés API.
    
* `global_config.dart` : Initialise Firebase, charge les variables d'environnement et s'assure que les clés API sont disponibles.
    
* `main.dart` : Démarre l'application et initialise les configurations.
    
* `app_strings.dart` : Stocke les valeurs constantes utilisées dans le projet.
    

#### **Étape 1 : Configuration des variables d'environnement**

Créez un fichier `.env` dans le répertoire racine de votre projet Flutter et définissez votre clé de chiffrement :

```dart
ENCRYPTION_KEY=32-character-secure-key-here
```

Ajoutez `flutter_dotenv` à votre `pubspec.yaml` :

```dart
dependencies:
  flutter:
    sdk: flutter
  encrypt: ^5.0.3
  flutter_dotenv: ^5.2.1
  device_info_plus: ^11.3.0
  firebase_remote_config: ^5.4.0
  flutter_secure_storage: ^9.0.0
```

Exécutez :

```dart
flutter pub get
```

#### **Étape 2 : Stockage sécurisé et chiffrement**

### `app_strings.dart`

Définissez les constantes utilisées dans le projet :

```dart
class AppStrings {
  static const String ENCRYPTION_KEY = "ENCRYPTION_KEY";
  static const String DEVICE_ID = "DEVICE_ID";
  static const String YOU_VERIFY_API_KEY = "YOU_VERIFY_API_KEY";
  static const String GEMINI_API_KEY = "GEMINI_API_KEY";
}
```

### `remote_config.dart`

Gère la récupération et le stockage sécurisés des clés API en utilisant le **chiffrement AES**. C'est un gros morceau, donc je vais décomposer chaque partie après le bloc de code :

```dart
import 'dart:io';
import 'package:device_info_plus/device_info_plus.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter_secure_storage/flutter_secure_storage.dart';
import 'package:firebase_remote_config/firebase_remote_config.dart';
import '../constants/app_strings.dart';
import '../../../domain/models/custom_error/custom_error.dart';
import 'package:encrypt/encrypt.dart' as encrypt;
import 'package:flutter_dotenv/flutter_dotenv.dart';

class RemoteConfig {
  static final FlutterSecureStorage _storage = FlutterSecureStorage();
  static encrypt.Encrypter? _encrypter;

  // Initialiser le chiffrement AES
  static Future<void> initializeEncrypter() async {
    encrypt.Key key = await _generateEncryptionKey();
    _encrypter = encrypt.Encrypter(encrypt.AES(key, mode: encrypt.AESMode.cbc));
  }

  static encrypt.Encrypter getEncrypter() {
    if (_encrypter == null) {
      initializeEncrypter();
    }
    return _encrypter!;
  }

  // Générer une clé de chiffrement sécurisée en utilisant la variable d'environnement et l'ID de l'appareil
  static Future<encrypt.Key> _generateEncryptionKey() async {
    String envKey = dotenv.env[AppStrings.ENCRYPTION_KEY] ?? "default_secure_key";
    String deviceId = await _getDeviceId();
    String combinedKey = (envKey + deviceId).substring(0, 32);
    return encrypt.Key.fromUtf8(combinedKey);
  }

  // Récupérer l'ID de l'appareil et le stocker de manière sécurisée
  static Future<String> _getDeviceId() async {
    String? storedDeviceId = await _storage.read(key: AppStrings.DEVICE_ID);

    if (storedDeviceId != null) {
      return storedDeviceId;
    }

    DeviceInfoPlugin deviceInfo = DeviceInfoPlugin();
    String deviceId;

    if (Platform.isAndroid) {
      AndroidDeviceInfo androidInfo = await deviceInfo.androidInfo;
      deviceId = androidInfo.id;
    } else if (Platform.isIOS) {
      IosDeviceInfo iosInfo = await deviceInfo.iosInfo;
      deviceId = iosInfo.identifierForVendor ?? "fallbackDeviceId";
    } else {
      deviceId = "fallbackDeviceId";
    }

    await _storage.write(key: AppStrings.DEVICE_ID, value: deviceId);
    return deviceId;
  }

  // Récupérer et chiffrer les clés API
  static Future<void> fetchApiKey({required String apiKeyName}) async {
    String key = '';
    try {
      final remoteConfig = FirebaseRemoteConfig.instance;
      await remoteConfig.setConfigSettings(
        RemoteConfigSettings(
          fetchTimeout: const Duration(seconds: 10),
          minimumFetchInterval: const Duration(seconds: 10),
        ),
      );
      await remoteConfig.fetchAndActivate();
      key = remoteConfig.getString(apiKeyName);
    } catch (e) {
      if (kDebugMode) {
        print(e);
      }
      throw CustomError(
        errorMsg: "ERROR Retrieving $apiKeyName (${e.toString()})",
        code: "configuration_error",
        plugin: "",
      );
    }

    final iv = encrypt.IV.fromSecureRandom(16);
    final encryptedKey = _encrypter?.encrypt(key, iv: iv).base64;

    await _storage.write(key: apiKeyName, value: encryptedKey);
    await _storage.write(key: "${apiKeyName}_iv", value: iv.base64);
  }

  static final Map<String, String> _decryptedKeysCache = {};

  // Récupérer et déchiffrer les clés API stockées
  static Future<String?> getApiKey({required String key}) async {
    if (_decryptedKeysCache.containsKey(key)) {
      return _decryptedKeysCache[key];
    }

    try {
      final encryptedKey = await _storage.read(key: key);
      final ivString = await _storage.read(key: "${key}_iv");

      if (encryptedKey != null && ivString != null) {
        final iv = encrypt.IV.fromBase64(ivString);
        final encrypted = encrypt.Encrypted.fromBase64(encryptedKey);
        final decryptedKey = _encrypter?.decrypt(encrypted, iv: iv);

        _decryptedKeysCache[key] = decryptedKey!;
        return decryptedKey;
      }
    } catch (e) {
      throw CustomError(
        errorMsg: "ERROR Retrieving $key (${e.toString()})",
        code: "configuration_error",
        plugin: "",
      );
    }

    return null;
  }
}
```

Cette classe `RemoteConfig` récupère, chiffre, stocke et récupère de manière sécurisée les clés API sensibles en utilisant Firebase Remote Config, le chiffrement AES, le stockage sécurisé et les informations spécifiques à l'appareil.

Voici une décomposition de ce qui se passe :

**1. Dépendances et imports**

* `dart:io` : Pour les vérifications spécifiques à la plateforme (Android, iOS).
    
* `device_info_plus` : Pour obtenir un identifiant d'appareil unique.
    
* `flutter_secure_storage` : Pour le stockage local sécurisé de paires clé-valeur.
    
* `firebase_remote_config` : Pour récupérer les clés API ou les configurations depuis Firebase.
    
* `encrypt` : Pour le chiffrement et le déchiffrement AES.
    
* `flutter_dotenv` : Pour lire les variables d'environnement.
    
* `CustomError` : Un modèle d'erreur personnalisé utilisé pour la gestion des erreurs.
    
* `AppStrings` : Contient probablement des chaînes constantes comme les clés.
    

**2. Propriétés de la classe**

```dart
static final FlutterSecureStorage _storage = FlutterSecureStorage();
static encrypt.Encrypter? _encrypter;
```

* `_storage` : Pour stocker de manière sécurisée les clés chiffrées et les IV.
    
* `_encrypter` : Utilisé pour chiffrer et déchiffrer les données en utilisant AES.
    

**3. `initializeEncrypter()`**

```dart
static Future<void> initializeEncrypter() async
```

* Configure le chiffreur AES en utilisant une combinaison d'une clé `.env` et de l'ID de l'appareil pour générer une clé de 32 octets.
    
* Utilise le mode AES CBC.
    

**4. `getEncrypter()`**

```dart
static encrypt.Encrypter getEncrypter()
```

* Retourne le chiffreur existant ou appelle `initializeEncrypter()` s'il n'est pas encore initialisé.
    

**5. `_generateEncryptionKey()`**

```dart
static Future<encrypt.Key> _generateEncryptionKey()
```

* Combine une variable d'environnement (`ENCRYPTION_KEY`) et l'ID de l'appareil pour produire une clé de 32 caractères.
    
* Retourne une clé AES (`encrypt.Key.fromUtf8`).
    

**6. `_getDeviceId()`**

```dart
static Future<String> _getDeviceId()
```

* Vérifie si un ID d'appareil est déjà stocké de manière sécurisée. Si ce n'est pas le cas, l'obtient depuis l'appareil (Android : [`androidInfo.id`](http://androidInfo.id), iOS : `identifierForVendor`).
    
* Stocke l'ID de l'appareil de manière sécurisée pour une utilisation future.
    

**7. `fetchApiKey()`**

```dart
static Future<void> fetchApiKey({required String apiKeyName})
```

* Récupère la clé API spécifiée depuis Firebase Remote Config.
    
* Chiffre la clé en utilisant AES et un IV aléatoire (vecteur d'initialisation).
    
* Stocke à la fois la clé chiffrée et le IV de manière sécurisée.
    

**8. `getApiKey()`**

```dart
static Future<String?> getApiKey({required String key})
```

* Récupère et déchiffre la clé API chiffrée.
    
* Si elle est déjà déchiffrée et mise en cache en mémoire, la retourne immédiatement.
    
* Sinon :
    
    * Lit la clé chiffrée et le IV depuis le stockage sécurisé.
        
    * Déchiffre la clé et la retourne.
        
    * Met en cache le résultat déchiffré dans `_decryptedKeysCache`.
        

**9. Gestion des erreurs**

Des exceptions `CustomError` personnalisées sont levées si la récupération Firebase ou le déchiffrement échoue.

Cette classe est conçue pour :

* Récupérer les clés API de manière sécurisée depuis Firebase.
    
* Les chiffrer en utilisant une clé liée à la fois à une variable d'environnement et à l'appareil spécifique.
    
* Les stocker localement sous une forme chiffrée.
    
* Permettre la récupération et le déchiffrement avec une mise en cache en mémoire pour minimiser la surcharge de traitement.
    

#### **Étape 3 : Initialisation globale**

### `global_config.dart`

Gère l'initialisation de Firebase, l'injection de dépendances et la récupération des clés API :

```dart
import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/widgets.dart';
import 'package:flutter_dotenv/flutter_dotenv.dart';
import 'package:injectable/injectable.dart';
import 'remote_config.dart';
import 'app_strings.dart';

class GlobalConfig {
  static Future<void> fetchRequiredApiKeys() async {
    final apiKeys = [
      AppStrings.YOU_VERIFY_API_KEY,
      AppStrings.GEMINI_API_KEY,
    ];
    for (final keyName in apiKeys) {
      await RemoteConfig.fetchApiKey(apiKeyName: keyName);
    }
  }

  static Future<void> initConfig() async {
    WidgetsFlutterBinding.ensureInitialized();
    await Firebase.initializeApp();
    await dotenv.load(fileName: ".env");
    await RemoteConfig.initializeEncrypter();
    await fetchRequiredApiKeys();
  }
}
```

#### **Étape 4 : Utilisation de la clé API dans l'interface utilisateur**

### `main.dart`

Initialise l'application :

```dart
import 'package:flutter/material.dart';
import 'global_config.dart';

Future<void> main() async {
  await GlobalConfig.initConfig();
  runApp(MyApp());
}
```

#### **Étape 5 : Récupération de la clé API dans un widget**

```dart
String apiKey = "";

@override
void initState() {
  super.initState();
  fetchAPIKey();
}

void fetchAPIKey() async {
  try {
    final key = await RemoteConfig.getApiKey(key: AppStrings.GEMINI_API_KEY) ?? "";
    setState(() {
      apiKey = key;
    });
  } catch (e) {
    print("Error fetching API key: $e");
  }
}
```

## Vulnérabilités courantes dans les applications Flutter

### 1. Codage en dur des secrets

Stocker des clés API ou des secrets dans la base de code (même dans des fichiers `.env` ou `.dart`) est l'une des erreurs les plus dangereuses. Des outils comme `apktool` peuvent extraire ces secrets facilement depuis le binaire compilé.

**Évitez cela :**

```dart
// Ne codez pas en dur les clés
const apiKey = 'YOUR_SECRET_API_KEY';
```

Le codage en dur des secrets est non sécurisé car lorsque l'APK est reverse-engineered, n'importe qui peut lire ces valeurs et abuser de vos API.

**Utilisez un stockage sécurisé à la place :**

```dart
import 'package:flutter_secure_storage/flutter_secure_storage.dart';

final storage = FlutterSecureStorage();
await storage.write(key: 'api_key', value: 'your_api_key');
final apiKey = await storage.read(key: 'api_key');
```

L'utilisation de `flutter_secure_storage` stocke les secrets de manière sécurisée dans des mécanismes de stockage sécurisés spécifiques à la plateforme comme le Keystore Android ou le Keychain iOS.

### 2. Manque de renforcement SSL/TLS (attaques MITM)

Une attaque Man-in-the-Middle (MITM) se produit lorsqu'un attaquant intercepte et modifie potentiellement la communication entre deux parties. Cela est particulièrement dangereux dans les connexions HTTP non sécurisées, car des informations sensibles comme les identifiants de connexion et les clés API peuvent être volées ou modifiées.

#### Comment SSL/TLS sécurise le code :

Secure Sockets Layer (SSL) et Transport Layer Security (TLS) sont des protocoles cryptographiques qui garantissent une communication chiffrée entre un client et un serveur. Cela empêche les attaques MITM en garantissant que les données sont chiffrées et ne peuvent pas être lues ou modifiées pendant le transit. La connexion est établie via HTTPS (qui est HTTP sur SSL/TLS).

**Exemple de code pour renforcer SSL/TLS :**

```dart
import 'package:http/http.dart' as http;

void makeSecureRequest() async {
  final response = await http.get(Uri.parse('https://yourapi.com/endpoint'));
  
  if (response.statusCode == 200) {
    // Gérer la réponse réussie
  } else {
    // Gérer l'erreur
  }
}
```

Dans ce cas, s'assurer que l'URL commence par `https://` impose l'utilisation de SSL/TLS pour une communication sécurisée.

### 3. Authentification faible

Les méthodes d'authentification faibles sont celles qui sont facilement devinées ou contournées, comme des mots de passe simples, l'absence d'authentification multifactorielle ou des mécanismes de hachage faibles.

À la place, vous devriez utiliser des méthodes d'authentification robustes comme Firebase et OAuth.

* **Firebase Authentication** fournit diverses méthodes d'authentification telles que la connexion par e-mail/mot de passe, la connexion Google et l'authentification par numéro de téléphone. C'est une solution sécurisée et facile à implémenter.
    
* **OAuth** est un protocole qui permet aux services tiers (comme Google ou Facebook) d'authentifier les utilisateurs de manière sécurisée sans exposer leur mot de passe à votre application. OAuth utilise des jetons pour l'autorisation, garantissant que les informations d'identification de l'utilisateur ne sont pas compromises.
    

**Utilisez Firebase Auth ou OAuth2 :**

```dart
import 'package:firebase_auth/firebase_auth.dart';

final FirebaseAuth _auth = FirebaseAuth.instance;
UserCredential userCredential = await _auth.signInWithEmailAndPassword(
  email: 'user@example.com',
  password: 'securePassword',
);
final token = await userCredential.user?.getIdToken();
```

L'authentification basée sur les jetons permet au backend de vérifier l'identité de l'utilisateur de manière sécurisée sans dépendre des cookies de session. Firebase Authentication gère la génération, la validation et l'expiration des jetons pour vous.

### 4. Vérifications d'autorisation insuffisantes

Les vérifications d'autorisation sont nécessaires pour s'assurer que l'utilisateur authentifié dispose des permissions requises pour effectuer certaines actions. Par exemple, un utilisateur administrateur peut avoir accès à tous les endpoints, tandis qu'un utilisateur régulier peut n'avoir accès qu'à des ressources limitées.

#### Comment vérifier les rôles/permissions des utilisateurs :

Côté serveur, les rôles et permissions sont généralement stockés dans une base de données. Lorsqu'un utilisateur fait une requête, le serveur vérifie son rôle et le compare aux permissions requises pour la ressource demandée.

**Exemple de code :**

```dart
// En supposant que les rôles des utilisateurs sont stockés dans Firestore
Future<bool> checkUserRole(String userId, String requiredRole) async {
  final userDoc = await FirebaseFirestore.instance.collection('users').doc(userId).get();
  final userRole = userDoc.data()?['role'];

  if (userRole == requiredRole) {
    return true;
  } else {
    throw CustomError(errorMsg: 'User does not have the required role');
  }
}
```

L'autorisation garantit que l'utilisateur est non seulement authentifié, mais dispose également des droits pour effectuer des actions spécifiques.

### 5. Endpoints et métadonnées exposés

Exposer la documentation Swagger ou les endpoints de test en production peut permettre aux attaquants de découvrir facilement les vulnérabilités de votre API. Cela leur fournit des informations détaillées sur la structure et les capacités de votre API, qui peuvent être exploitées.

#### Comment sécuriser avec des gardes de route :

Un garde de route peut empêcher l'accès non autorisé aux routes sensibles, garantissant que seuls les utilisateurs authentifiés et autorisés peuvent accéder à certains endpoints.

```dart
void checkRouteAccess(String route) {
  if (!isUserAuthenticated()) {
    throw CustomError(errorMsg: 'User not authorized');
  }
}
```

**Évitez cela :**

* Ne déployez pas les docs Swagger sans authentification
    
* Utilisez des gardes de route pour les routes admin/dev
    
* Supprimez les symboles de débogage et les logs dans les builds de production
    

**Exemple : Appel API sécurisé dans Flutter**

Voici un exemple simple utilisant Dio, un client HTTP puissant pour Dart, pour appeler une API de manière sécurisée avec une authentification basée sur les jetons et HTTPS :

```dart
import 'package:dio/dio.dart';
import 'package:flutter_secure_storage/flutter_secure_storage.dart';

final dio = Dio();
final storage = FlutterSecureStorage();

Future<void> fetchSecureData() async {
  final token = await storage.read(key: 'auth_token');

  dio.options.headers['Authorization'] = 'Bearer $token';

  try {
    final response = await dio.get('https://yourapi.com/secure-endpoint');
    print(response.data);
  } catch (e) {
    print('API call failed: $e');
  }
}
```

Cet exemple illustre comment inclure un jeton d'autorisation dans l'en-tête de votre requête et effectuer une requête HTTPS de manière sécurisée en utilisant `dio`. Dio prend également en charge les intercepteurs, les nouvelles tentatives et des options avancées comme le pinning de certificats.

## Bonnes pratiques pour sécuriser les API dans les applications Flutter

### **Toujours utiliser HTTPS**

Évitez le HTTP en clair à tout prix. Utilisez HTTPS pour chiffrer les données en transit.

```dart
final response = await http.get(Uri.parse('https://api.secure.com/data'));
```

### **Implémenter OAuth2 ou Firebase Auth**

Utilisez des packages d'authentification modernes comme `firebase_auth` ou `oauth2_client`. Ceux-ci offrent une authentification sécurisée basée sur les jetons avec une gestion intégrée des sessions et des jetons de rafraîchissement.

### **Utiliser Firebase App Check**

Empêche l'abus de votre backend en vérifiant la légitimité de l'application cliente.

```dart
await FirebaseAppCheck.instance.activate(
  webRecaptchaSiteKey: 'your-site-key',
);
```

### **Stockage sécurisé des données sensibles**

Utilisez `flutter_secure_storage` pour stocker en toute sécurité les jetons et les secrets localement.

### **Obfuscation du code Dart**

L'obfuscation rend votre code Dart plus difficile à reverse-engineer. Vous pouvez le faire en renommant les classes, les méthodes et les variables en des noms sans signification.

```bash
flutter build apk --obfuscate --split-debug-info=build/symbols
```

Cette commande supprime les informations de débogage et renomme les classes/fonctions, rendant plus difficile pour les attaquants de comprendre votre code compilé.

### **Utiliser la limitation de débit et le throttling**

Protégez les API backend contre les abus en limitant le débit des requêtes. Implémentez une limitation de débit côté serveur en utilisant des outils de passerelle API ou des bibliothèques de middleware. [Voici un tutoriel](https://www.freecodecamp.org/news/what-is-rate-limiting-web-apis/) qui vous en apprendra plus sur cette technique.

### **Configurer la journalisation et la surveillance**

Utilisez des outils comme Firebase Crashlytics ou Sentry pour suivre les erreurs et les activités suspectes.

```dart
FirebaseCrashlytics.instance.recordError(e, stackTrace);
```

### **Passerelle API et WAF**

Utilisez des couches de gestion d'API comme Google Cloud Endpoints ou AWS API Gateway ainsi que des pare-feu d'applications web (WAF) pour contrôler et filtrer le trafic.

## Liste de contrôle de sécurité pour les développeurs Flutter

* Utilisez HTTPS pour toutes les communications
    
* Ne codez jamais en dur les secrets ou les informations d'identification
    
* Utilisez une authentification basée sur les jetons (OAuth2, Firebase Auth)
    
* Validez les jetons à la fois sur le client et le serveur
    
* Obfusquez et minifiez le code avant la production
    
* Stockez les données sensibles de manière sécurisée en utilisant `flutter_secure_storage`
    
* Activez Firebase App Check ou équivalent
    
* Utilisez des passerelles API et des WAF pour le filtrage du trafic
    
* Surveillez les journaux d'utilisation et configurez des alertes pour les anomalies
    
* Implémentez la limitation de débit pour prévenir les abus
    

### Considérations supplémentaires

#### **Épinglage de certificat :**

L'épinglage de certificat est une technique utilisée pour s'assurer que l'application ne communique qu'avec un serveur de confiance en comparant le certificat du serveur avec un certificat ou une clé publique pré-stockée. Cela empêche les attaquants d'utiliser des certificats frauduleux.

Exemple : Épinglage de certificat dans Dio

```dart
class CertPinningInterceptor extends Interceptor {
  @override
  void onRequest(RequestOptions options, RequestInterceptorHandler handler) async {
    final context = SecurityContext(withTrustedRoots: false);
    final certBytes = (await rootBundle.load('assets/certs/myserver.cer')).buffer.asUint8List();
    context.setTrustedCertificatesBytes(certBytes);

    final client = HttpClient(context: context);
    client.badCertificateCallback = (X509Certificate cert, String host, int port) {
      final serverSha = sha256.convert(cert.der).toString();
      const expectedSha = 'your_cert_sha256_fingerprint';
      return serverSha == expectedSha;
    };

    (options.extra['httpClientAdapter'] as DefaultHttpClientAdapter?)
        ?.onHttpClientCreate = (_) => client;

    handler.next(options);
  }
}
```

* `SecurityContext(withTrustedRoots: false)` : Commence avec un magasin de confiance vide, ce qui signifie qu'aucun CA système n'est approuvé par défaut.
    
* `setTrustedCertificatesBytes` : Charge le certificat de votre propre serveur depuis les actifs locaux et le définit comme le seul certificat approuvé.
    
* `HttpClient.badCertificateCallback` : Compare l'empreinte SHA-256 du certificat du serveur avec une valeur connue. Si elles correspondent, la requête se poursuit.
    
* `onHttpClientCreate` : Remplace le client HTTP Dio par défaut par le client personnalisé configuré pour l'épinglage.
    

Cela garantit que votre application n'acceptera que les connexions HTTPS de votre propre serveur de confiance, protégeant les utilisateurs contre l'usurpation de certificats ou les attaques MITM.

#### **TTL et rotation des jetons :**

**Time-to-Live (TTL)** est une mesure de sécurité qui garantit que les jetons expirent automatiquement après une période définie. Cela limite la durée pendant laquelle un jeton peut être utilisé, réduisant la surface d'attaque s'il est compromis.

**La rotation des jetons** améliore encore la sécurité en émettant un nouveau jeton de rafraîchissement chaque fois que le jeton existant est utilisé pour demander un nouveau jeton d'accès. Le jeton de rafraîchissement précédent est alors invalidé. Cela empêche les attaques par relecture où un attaquant pourrait tenter de réutiliser un jeton de rafraîchissement volé.

**Cycle de vie réel des jetons :**

1. **Jeton d'accès :**
    
    * **TTL :** Court (par exemple, 15 minutes)
        
    * **But :** Utilisé pour authentifier et autoriser les requêtes API
        
    * **Comportement :** Expire rapidement pour minimiser le risque en cas d'exposition
        
2. **Jeton de rafraîchissement :**
    
    * **TTL :** Plus long (par exemple, 7 jours)
        
    * **But :** Utilisé pour demander de nouveaux jetons d'accès sans nécessiter une nouvelle connexion de l'utilisateur
        
    * **Rotation :** Un nouveau jeton de rafraîchissement est émis à chaque utilisation
        

Voici un exemple d'implémentation (pseudo-code de type Dart) :

Générer un jeton d'accès (TTL de 15 minutes) :

```dart
String generateAccessToken(String userId) {
  final expiry = DateTime.now().add(Duration(minutes: 15));
  return createJwtToken(userId: userId, expiresAt: expiry);
}
```

Puis générer un jeton de rafraîchissement (TTL de 7 jours) :

```dart
String generateRefreshToken(String userId) {
  final expiry = DateTime.now().add(Duration(days: 7));
  return createSecureRandomToken(userId: userId, expiresAt: expiry);
}
```

Point de terminaison de rafraîchissement avec rotation :

```dart
Map<String, String> refreshAccessToken(String refreshToken) {
  if (isValidRefreshToken(refreshToken)) {
    final userId = getUserIdFromRefreshToken(refreshToken);

    // Invalider l'ancien jeton de rafraîchissement
    invalidateRefreshToken(refreshToken);

    // Rotation des jetons
    final newRefreshToken = generateRefreshToken(userId);
    final newAccessToken = generateAccessToken(userId);

    return {
      'accessToken': newAccessToken,
      'refreshToken': newRefreshToken,
    };
  } else {
    throw CustomError(errorMsg: 'Invalid or expired refresh token');
  }
}
```

Pourquoi cela compte :

* **Atténue l'exposition à long terme** : Les jetons expirent automatiquement, réduisant les risques.
    
* **Empêche les attaques par relecture** : Un jeton de rafraîchissement tourné ne peut pas être réutilisé s'il est intercepté.
    
* **Améliore la sécurité des sessions** : Même si un jeton est volé, il devient rapidement inutile.
    

#### **Validation backend :**

La validation backend garantit que les données sensibles, comme les clés API ou les jetons JWT, sont vérifiées côté serveur, empêchant la falsification par des utilisateurs malveillants.

Ne faites jamais confiance au client. Validez toujours toutes les opérations sensibles et les rôles des utilisateurs sur le backend.

Exemple :

```dart
void validateToken(String token) {
  if (isTokenExpired(token)) {
    throw CustomError(errorMsg: 'Token expired');
  }
}
```

* `validateToken(String token)` : Une fonction qui prend un jeton utilisateur comme entrée.
    
* `isTokenExpired(token)` : Une fonction hypothétique qui vérifie si le jeton a expiré (par exemple, en décodant le jeton et en vérifiant son horodatage d'expiration).
    
* `throw CustomError(...)` : Si le jeton est expiré, une erreur est levée — dans ce cas, une `CustomError` avec un message indiquant `'Token expired'`.
    

Pourquoi cela compte :

* Les jetons peuvent être volés ou manipulés côté client, donc leur faire confiance aveuglément est dangereux.
    
* Les vérifications backend comme celle-ci aident à renforcer le contrôle serveur sur l'authentification des utilisateurs et la validité des sessions.
    
* Même si un utilisateur falsifie le code côté client, il ne peut pas contourner cette validation côté serveur.
    

#### **Utiliser des outils axés sur la sécurité comme OWASP ZAP/Burp Suite/Postman :**

Utilisez des outils comme OWASP ZAP, Burp Suite et Postman pour tester manuellement et automatiquement vos endpoints API pour détecter les vulnérabilités.

* **OWASP ZAP** : Utilisé pour les tests de pénétration, trouver des vulnérabilités comme XSS, SQL Injection, etc.
    
* **Burp Suite** : Un autre outil pour tester les vulnérabilités de sécurité dans les applications web.
    
* **Postman** : Peut être utilisé pour tester les endpoints API et garantir des communications sécurisées en ajoutant les en-têtes nécessaires comme `Authorization`.
    

## Conclusion

Sécuriser les API mobiles est une exigence fondamentale dans le développement d'applications modernes. Pour les développeurs Flutter, cela signifie aller au-delà de la création d'interfaces utilisateur attrayantes pour s'assurer que l'infrastructure API sous-jacente est résiliente face aux menaces. Les risques liés aux endpoints exposés, aux secrets divulgués et aux communications non sécurisées sont bien réels, mais évitables.

La sécurité est une question de défense proactive, et vous devriez en faire une partie centrale de votre flux de travail de développement. Avec des pratiques cohérentes, des audits réguliers et une attention aux détails, vous protégerez à la fois vos utilisateurs et votre produit contre des risques inutiles. Flutter offre la flexibilité et la puissance de créer des applications rapides et multiplateformes – ne laissez donc pas une mauvaise sécurité des API compromettre ce potentiel.

En suivant les meilleures pratiques décrites dans cet article, telles que l'utilisation de HTTPS, la mise en œuvre d'une authentification et d'une autorisation appropriées, le stockage sécurisé des informations d'identification et l'utilisation d'outils comme Firebase App Check, vous pouvez réduire considérablement la surface d'attaque de votre application.

Rappelez-vous : une sécurité efficace commence par un état d'esprit. Ce n'est pas seulement une configuration ponctuelle, mais un processus continu de vigilance, de test et d'amélioration.

### Références

* [Projet de sécurité mobile OWASP](https://owasp.org/www-project-mobile-security/)
    
* [Top 10 de la sécurité des API OWASP](https://owasp.org/www-project-api-security/)
    
* [Bonnes pratiques de sécurité Android](https://developer.android.com/topic/security/best-practices)
    
* [**Flutter Secure Storage - pub.dev**](https://pub.dev/packages/flutter_secure_storage)
    
* [**Package Encrypt - pub.dev**](https://pub.dev/packages/encrypt)
    
* [**Firebase Remote Config - Docs Firebase**](https://firebase.google.com/docs/remote-config)
    
* [**Device Info Plus - pub.dev**](https://pub.dev/packages/device_info_plus)
    
* [**Flutter dotenv - pub.dev**](https://pub.dev/packages/flutter_dotenv)
    
* [**Injectable pour l'injection de dépendances - pub.dev**](https://pub.dev/packages/injectable)
    
* [**Flutter Fire (Initialisation Firebase) - Docs Firebase**](https://firebase.flutter.dev/docs/overview/)