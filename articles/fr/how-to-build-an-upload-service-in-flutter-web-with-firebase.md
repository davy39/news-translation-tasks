---
title: Comment créer un service d'upload dans Flutter Web avec Firebase
subtitle: ''
author: Atuoha Anthony
co_authors: []
series: null
date: '2025-09-05T15:22:25.818Z'
originalURL: https://freecodecamp.org/news/how-to-build-an-upload-service-in-flutter-web-with-firebase
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1757085725508/3ff2d66d-5b3b-4784-904b-de7b464de41b.png
tags:
- name: Flutter
  slug: flutter
- name: Dart
  slug: dart
- name: Firebase
  slug: firebase
- name: firebase Storage
  slug: firebase-storage
seo_title: Comment créer un service d'upload dans Flutter Web avec Firebase
seo_desc: Uploading files is one of the most common requirements in modern web applications.
  Whether it’s profile pictures, documents, or bulk uploads, users expect a smooth
  and reliable experience. With Flutter Web and Firebase Storage, you can implement
  this...
---

L'upload de fichiers est l'une des exigences les plus courantes dans les applications web modernes. Qu'il s'agisse de photos de profil, de documents ou d'uploads groupés, les utilisateurs attendent une expérience fluide et fiable. Avec Flutter Web et Firebase Storage, vous pouvez implémenter cette fonctionnalité de manière propre et évolutive.

Dans cet article, vous apprendrez à créer un service d'upload réutilisable qui :

1. Télécharge des fichiers uniques et multiples vers Firebase Storage
    
2. Retourne les URLs de téléchargement des fichiers
    
3. Utilise l'Injection de Dépendances (DI) avec `injectable` pour garder le code modulaire, testable et facile à maintenir
    

À la fin, vous disposerez d'un service d'upload prêt pour la production pour votre projet Flutter Web.

### Table des matières :

1. [Pourquoi l'upload de fichiers est important dans Flutter Web](#heading-pourquoi-lupload-de-fichiers-est-important-dans-flutter-web)
    
2. [Aperçu du flux d'upload](#heading-aperçu-du-flux-dupload)
    
3. [Prérequis](#heading-prérequis)
    
4. [Comment définir le modèle de données d'upload et l'interface du service](#heading-comment-définir-le-modèle-de-données-dupload-et-linterface-du-service)
    
5. [Comment implémenter le service d'upload](#heading-comment-implémenter-le-service-dupload)
    
6. [Comment gérer les erreurs](#heading-comment-gérer-les-erreurs)
    
7. [Injection de dépendances avec injectable](#heading-injection-de-dépendances-avec-injectable)
    
8. [Comment utiliser le service d'upload](#heading-comment-utiliser-le-service-dupload)
    
9. [Bonnes pratiques](#heading-bonnes-pratiques)
    
10. [Conclusion](#heading-conclusion)
    
11. [Références](#heading-références)
    

## Pourquoi l'upload de fichiers est important dans Flutter Web

Lors du développement pour le web, les utilisateurs attendent souvent des fonctionnalités telles que l'upload d'une photo de profil, la soumission de documents ou le partage de médias. Contrairement au mobile, l'environnement web nécessite la manipulation des fichiers via les APIs du navigateur, qui doivent ensuite être intégrées à des services backend comme Firebase pour la persistance.

## Aperçu du flux d'upload

Voici un aperçu de haut niveau du fonctionnement du processus d'upload :

1. L'utilisateur sélectionne un fichier ou une image à l'aide d'un sélecteur de fichiers du navigateur.
    
2. Flutter lit le fichier sous forme de `Uint8List`.
    
3. Le fichier est uploadé vers Firebase Storage.
    
4. Une URL de téléchargement est générée et stockée dans Firestore (ou utilisée directement).
    

## Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants :

1. Un projet Flutter Web
    
    ```bash
    flutter config --enable-web
    flutter create my_web_project
    cd my_web_project
    ```
    
2. Firebase configuré dans votre application Flutter : Suivez [Ajouter Firebase à votre application Flutter (Web)](https://firebase.google.com/docs/flutter/setup?platform=web) et incluez le snippet du SDK Firebase dans `index.html`.
    
3. Firebase Storage activé dans la Console Firebase : Allez dans Build &gt; Storage &gt; Get Started et autorisez l'accès en lecture/écriture pour les tests. Exemple de règles :
    
    ```json
    service firebase.storage {
      match /b/{bucket}/o {
        match /{allPaths=**} {
          allow read, write: if true;
        }
      }
    }
    ```
    
    N'utilisez pas ces règles en production.
    
4. Dépendances requises dans votre `pubspec.yaml` :
    
    ```yaml
    dependencies:
      firebase_core: ^3.13.0
      firebase_storage: ^12.4.2
      injectable: ^2.3.2
      get_it: ^8.0.3
    
    dev_dependencies:
      build_runner: ^2.4.13
      injectable_generator: ^2.4.1
    ```
    
    Lancez `flutter pub get` pour les installer.
    

## Comment définir le modèle de données d'upload et l'interface du service

Nous commençons par un modèle de données pour représenter le fichier et une interface de service pour définir le contrat d'upload.

```dart
import 'dart:typed_data';

class UploadData {
  final Uint8List fileData;   // Fichier au format binaire
  final String folderName;    // Chemin du dossier dans Firebase Storage
  final String fileName;      // Nom du fichier

  const UploadData({
    required this.fileData,
    required this.fileName,
    required this.folderName,
  });
}
```

Ensuite, créez un service abstrait qui définit ce que la logique d'upload doit faire.

```dart
abstract class IUploadService {
  Future<String> uploadDoc({
    required UploadData file,
  });

  Future<List<String>> uploadMultipleDoc({
    required List<UploadData> files,
  });
}
```

Voici ce qui se passe dans ce code :

* `uploadDoc` : Upload un fichier et retourne son URL de téléchargement
    
* `uploadMultipleDoc` : Upload plusieurs fichiers en parallèle et retourne une liste d'URLs
    

![Diagramme : Design de l'interface](https://cdn.hashnode.com/res/hashnode/image/upload/v1756777666277/35243f4a-4f0f-40b5-92b1-f1f1a5b3474e.png align="center")

## Comment implémenter le service d'upload

Implémentons maintenant la logique d'upload avec Firebase Storage.

```dart
import 'package:firebase_storage/firebase_storage.dart';
import 'package:flutter/foundation.dart';
import 'package:injectable/injectable.dart';
import 'i_upload_service.dart';
import 'custom_error.dart';

@LazySingleton(as: IUploadService)
class UploadService extends IUploadService {
  final FirebaseStorage firebaseStorage;

  UploadService({required this.firebaseStorage});

  @override
  Future<String> uploadDoc({required UploadData file}) async {
    try {
      var storageRef = firebaseStorage.ref('${file.folderName}/${file.fileName}');
      var uploadTask = storageRef.putData(file.fileData);
      TaskSnapshot snapshot = await uploadTask;
      return await snapshot.ref.getDownloadURL();
    } on FirebaseException catch (e) {
      throw CustomError(
        errorMsg: "Échec de l'upload Firebase : ${e.message}",
        code: e.code,
        plugin: e.plugin,
      );
    } catch (e) {
      if (kDebugMode) print("Erreur inattendue : $e");
      rethrow;
    }
  }

  @override
  Future<List<String>> uploadMultipleDoc({required List<UploadData> files}) async {
    return await Future.wait(
      files.map((file) => uploadDoc(file: file)),
    );
  }
}
```

Ce code définit une **classe de service** pour l'upload de documents vers Firebase Storage dans une application Flutter. Décomposons-le étape par étape :

**1\. Imports**

1. `firebase_storage` : fournit le SDK Firebase Storage pour uploader et gérer les fichiers.
    
2. `flutter/foundation.dart` : donne accès à des constantes comme `kDebugMode` pour les logs de débogage.
    
3. `injectable.dart` : permet l'injection de dépendances en utilisant le package injectable + getIt.
    
4. `i_upload_service.dart` : définit le contrat/interface abstrait pour le service d'upload.
    
5. `custom_error.dart` : définit une classe d'erreur personnalisée pour standardiser la gestion des erreurs.
    

**2\. Configuration de l'injection de dépendances**

```dart
@LazySingleton(as: IUploadService)
class UploadService extends IUploadService {
```

1. `@LazySingleton(as: IUploadService)` enregistre `UploadService` comme l'implémentation de `IUploadService`.
    
2. Cela signifie que partout dans l'application où `IUploadService` est requis, getIt fournira une instance de `UploadService`.
    
3. C'est un singleton, donc une seule instance est créée et réutilisée dans toute l'application.
    

**3\. Constructeur**

```dart
final FirebaseStorage firebaseStorage;

UploadService({required this.firebaseStorage});
```

1. La classe nécessite une instance `FirebaseStorage`, qui sera également injectée automatiquement.
    
2. Cela rend le service plus facile à tester et à remplacer.
    

**4\. Upload d'un fichier unique**

```dart
@override
Future<String> uploadDoc({required UploadData file}) async {
  try {
    var storageRef = firebaseStorage.ref('${file.folderName}/${file.fileName}');
    var uploadTask = storageRef.putData(file.fileData);
    TaskSnapshot snapshot = await uploadTask;
    return await snapshot.ref.getDownloadURL();
  } on FirebaseException catch (e) {
    throw CustomError(
      errorMsg: "Échec de l'upload Firebase : ${e.message}",
      code: e.code,
      plugin: e.plugin,
    );
  } catch (e) {
    if (kDebugMode) print("Erreur inattendue : $e");
    rethrow;
  }
}
```

Ce que fait ce code :

1. Crée une référence dans Firebase Storage au chemin `folderName/fileName`.
    
2. Upload les octets bruts du fichier (`file.fileData`) en utilisant `putData`.
    
3. Attend que l'upload soit terminé et récupère un `TaskSnapshot`.
    
4. À partir du snapshot, obtient l'URL de téléchargement du fichier uploadé et la retourne.
    
5. Si une `FirebaseException` survient, il encapsule l'erreur dans un `CustomError` personnalisé.
    
6. Toute autre erreur inattendue est loggée (uniquement en mode debug) et relancée.
    

**5\. Upload de fichiers multiples**

```dart
@override
Future<List<String>> uploadMultipleDoc({required List<UploadData> files}) async {
  return await Future.wait(
    files.map((file) => uploadDoc(file: file)),
  );
}
```

Ce que fait le code :

1. Accepte une liste d'objets `UploadData`.
    
2. Pour chaque fichier, il appelle `uploadDoc` (la fonction d'upload unique).
    
3. `Future.wait` exécute tous les uploads **en parallèle**, attend qu'ils se terminent et retourne une liste d'URLs de téléchargement.
    

Cette classe est un service d'upload Firebase Storage. Elle peut uploader des documents uniques ou multiples. Elle suit les principes d'injection de dépendances pour la testabilité et l'évolutivité. Elle utilise une gestion d'erreurs avec `CustomError` pour fournir des messages d'erreur plus clairs. Les uploads multiples sont exécutés en parallèle par souci d'efficacité.

![Flux d'upload avec Firebase Storage](https://cdn.hashnode.com/res/hashnode/image/upload/v1756776717488/16d18b9c-309c-43a3-b595-74dabe7d7b3c.png align="center")

## Comment gérer les erreurs

Au lieu de s'appuyer sur des instructions `print` brutes, il est préférable d'utiliser une **classe d'erreur structurée**. Une classe d'erreur structurée organise toutes les informations relatives à l'erreur, comme le message, le code et la source, dans un seul objet. Cela rend la gestion des erreurs cohérente, réutilisable et facile à gérer. Vous pouvez inspecter, logger ou afficher les erreurs par programmation, ce qui est beaucoup plus maintenable que des prints dispersés.

```dart
import 'package:equatable/equatable.dart';

class CustomError extends Equatable {
  final String errorMsg;
  final String code;
  final String plugin;

  const CustomError({
    required this.errorMsg,
    required this.code,
    required this.plugin,
  });

  @override
  List<Object?> get props => [errorMsg, code, plugin];

  @override
  String toString() {
    return 'CustomError(errorMsg: $errorMsg, code: $code, plugin: $plugin)';
  }
}
```

Pourquoi devriez-vous utiliser cette approche :

* Assure la cohérence dans tout le projet.
    
* Rend les erreurs réutilisables n'importe où dans l'application.
    
* Permet une gestion programmatique (par exemple, agir différemment selon le code d'erreur).
    
* Fournit des informations de débogage claires via `toString()`.
    
* Évolue bien à mesure que votre application grandit.
    

## Injection de dépendances avec injectable

Dans une application classique, vous pourriez créer manuellement des instances de service comme `UploadService` ou `FirebaseStorage` partout où vous en avez besoin. Mais à mesure que votre application grandit, la création et la transmission manuelles des dépendances deviennent désordonnées, sujettes aux erreurs et difficiles à tester.

C'est là qu'intervient l'**Injection de Dépendances** (DI). La DI vous permet de déclarer les dépendances une seule fois et de laisser un framework s'occuper de les créer et de les fournir partout où elles sont nécessaires. Le package `injectable` dans Flutter fonctionne avec `getIt` pour automatiser ce processus.

Au lieu de créer `UploadService` manuellement, vous le configurez avec injectable pour que votre application obtienne automatiquement la bonne instance en cas de besoin, selon les patterns singleton ou lazy-loading.

### Étape 1 : Annotez votre service

```dart
@LazySingleton(as: IUploadService)
class UploadService implements IUploadService {
  // votre logique d'upload ici
}
```

`@LazySingleton(as: IUploadService)` indique à injectable :

* **Lazy** : Ne créer l'instance que lors de sa première utilisation.
    
* **Singleton** : Réutiliser la même instance dans toute l'application.
    
* **as: IUploadService** : Exposer le service via son interface, facilitant les tests et l'échange d'implémentations.
    

### Étape 2 : Lancez le générateur

```dart
flutter pub run build_runner build
```

Cette commande génère le code qui relie toutes vos dépendances injectables entre elles, de sorte que vous n'ayez pas à les instancier manuellement.

### Étape 3 : Créez un module injectable

```dart
import 'package:firebase_storage/firebase_storage.dart';
import 'package:injectable/injectable.dart';

@module
abstract class InjectableModule {
  @lazySingleton
  FirebaseStorage get firebaseStorage => FirebaseStorage.instance;
}
```

Ce code configure l'injection de dépendances pour `FirebaseStorage` en utilisant le package `injectable`. Laissez-moi vous expliquer :

1. `@module` : L'annotation `@module` indique à `injectable` que cette classe servira de fournisseur de dépendances externes (des choses que vous ne créez pas manuellement mais que vous obtenez de bibliothèques, de SDKs ou d'APIs).
    
    Dans ce cas, `FirebaseStorage` provient du SDK Firebase, vous ne le construisez donc pas vous-même. Vous obtenez simplement une instance du SDK.
    
2. `abstract class InjectableModule` : Il s'agit d'une classe de module spéciale qui contient des définitions de dépendances. Comme elle est abstraite, elle ne sera pas instanciée directement. Au lieu de cela, `injectable` génère le code pour gérer l'injection.
    
3. `@lazySingleton` : Cette annotation indique à `injectable` que la dépendance doit être créée **une seule fois** et réutilisée dans toute l'application (pattern singleton).
    
    * **Lazy** signifie qu'elle ne sera pas créée tant qu'elle n'est pas réellement nécessaire.
        
    * **Singleton** signifie que la même instance sera réutilisée partout après la première création.
        
4. `FirebaseStorage get firebaseStorage => FirebaseStorage.instance;` : Cette ligne définit quelle dépendance fournir. Ici, elle dit :
    
    * Chaque fois que quelque chose dans l'application a besoin d'une instance `FirebaseStorage`, injectez `FirebaseStorage.instance`.
        
    * De cette façon, vous ne créez pas et ne passez pas manuellement `FirebaseStorage` vous-même – `injectable` plus `getIt` s'en chargent automatiquement.
        

En pratique, cela garantit que partout dans votre application où vous avez besoin de `FirebaseStorage`, vous pouvez simplement l'injecter via l'injection par constructeur (par exemple, dans votre `UploadService`) sans l'instancier manuellement.

### Étape 4 : Résoudre le service n'importe où

```dart
final uploadService = getIt<IUploadService>();
```

#### **Pourquoi nous faisons cela**

En utilisant injectable :

1. Vous arrêtez d'instancier manuellement les dépendances partout.
    
2. Vos services sont plus faciles à tester, car vous pouvez échanger les implémentations via les interfaces.
    
3. Vous garantissez les patterns singleton et le lazy loading sans code répétitif supplémentaire.
    
4. Votre application devient plus maintenable, surtout à mesure qu'elle grandit.
    

**En pratique :**  
Partout dans votre application où `UploadService` a besoin de `FirebaseStorage`, vous l'injectez simplement via le constructeur :

```dart
class UploadService implements IUploadService {
  final FirebaseStorage _firebaseStorage;

  UploadService(this._firebaseStorage);

  // Utilisez _firebaseStorage ici
}
```

Injectable + getIt se charge de fournir automatiquement la bonne instance de `_firebaseStorage`.

![Injection de dépendances avec getIt & injectable](https://cdn.hashnode.com/res/hashnode/image/upload/v1756776761337/7a32fc39-9147-4e78-ba82-150074cdb066.png align="center")

## Comment utiliser le service d'upload

Le **Service d'Upload** est un service modulaire et réutilisable dans votre application qui gère l'upload de fichiers vers Firebase Storage. En utilisant ce service, vous faites abstraction des interactions directes avec Firebase, vous gardez votre code propre et vous exploitez l'injection de dépendances pour accéder au service n'importe où dans votre application.

Le Service d'Upload offre plusieurs options :

* **Upload de fichier unique** – Upload d'un fichier à la fois et obtention de son URL de téléchargement.
    
* **Upload de fichiers multiples** – Upload d'un lot de fichiers en une seule fois et réception d'une liste d'URLs de téléchargement.
    
* **Gestion des erreurs** – Tout problème lors de l'upload (comme des erreurs réseau ou des problèmes de permission) est capturé et peut être géré avec élégance.
    

Ci-dessous, nous allons passer en revue étape par étape comment utiliser ces options en pratique.

### **Exemple : Uploader un fichier unique.**

```dart
Future<void> uploadFile(Uint8List fileData) async {
  final file = UploadData(
    fileData: fileData,
    fileName: 'example.txt',
    folderName: 'documents',
  );

  try {
    final uploadService = getIt<IUploadService>();
    final downloadUrl = await uploadService.uploadDoc(file: file);
    print('Upload réussi : $downloadUrl');
  } catch (e) {
    print('Échec de l'upload : $e');
  }
}
```

Cette fonction `uploadFile` est une enveloppe qui prépare un fichier pour l'upload et délègue l'upload réel à votre `UploadService` via l'injection de dépendances. Laissez-moi vous expliquer cela étape par étape :

```dart
Future<void> uploadFile(Uint8List fileData) async {
  final file = UploadData(
    fileData: fileData,
    fileName: 'example.txt',
    folderName: 'documents',
  );
```

1. Tout d'abord, elle prend un fichier sous forme d'octets bruts (`Uint8List fileData`).
    
2. Ensuite, elle encapsule ces données dans un objet `UploadData`, en lui donnant un `fileName` (`example.txt`) et un `folderName` (`documents`). Cela crée essentiellement des métadonnées sur le fichier, afin que votre service d'upload sache comment l'appeler et où le stocker dans Firebase Storage.
    

```dart
  try {
    final uploadService = getIt<IUploadService>();
    final downloadUrl = await uploadService.uploadDoc(file: file);
    print('Upload réussi : $downloadUrl');
  } catch (e) {
    print('Échec de l'upload : $e');
  }
}
```

3. Ensuite, elle récupère l'instance `IUploadService` en utilisant `getIt` (votre conteneur d'injection de dépendances). Grâce à la liaison que vous avez définie plus tôt (`UploadService` enregistré en tant que `IUploadService`), `getIt` sait vous donner la bonne implémentation.
    
4. Elle appelle `uploadService.uploadDoc(file: file)` qui déclenche l'upload réel vers Firebase Storage. En cas de succès, Firebase renvoie une URL de téléchargement du fichier uploadé.
    
5. La fonction affiche ensuite :
    
    * `"Upload réussi : <downloadUrl>"` si l'upload a fonctionné.
        
    * `"Échec de l'upload : <erreur>"` si une erreur est survenue (par exemple, pas d'internet ou problèmes de permission Firebase).
        

En termes simples :

1. **Entrée** : Données brutes du fichier (octets).
    
2. **Processus** : Encapsulation dans un objet `UploadData` → envoi à Firebase via `UploadService`.
    
3. **Sortie** : Affiche l'URL publique de téléchargement si l'upload réussit, ou affiche un message d'erreur s'il échoue.
    

### **Exemple : Uploader plusieurs fichiers.**

```dart
Future<void> uploadMultiple(List<Uint8List> filesData) async {
  final uploadService = getIt<IUploadService>();

  final files = filesData.map((data) => UploadData(
    fileData: data,
    fileName: '${DateTime.now().millisecondsSinceEpoch}.txt',
    folderName: 'batch_docs',
  )).toList();

  try {
    final urls = await uploadService.uploadMultipleDoc(files: files);
    print('Tous les fichiers ont été uploadés : $urls');
  } catch (e) {
    print('Échec de l'upload groupé : $e');
  }
}
```

Cette fonction gère l'upload groupé de plusieurs fichiers vers Firebase Storage en utilisant le `IUploadService`. Décomposons-la étape par étape :

#### 1\. Accéder au service d'upload

```dart
final uploadService = getIt<IUploadService>();
```

Ici, `getIt` récupère l'instance `IUploadService` enregistrée via l'injection de dépendances. Ce service masque toute la logique d'upload des fichiers, de sorte que vous ne manipulez pas directement les APIs Firebase dans cette méthode.

#### 2\. Préparer la liste des fichiers

```dart
final files = filesData.map((data) => UploadData(
  fileData: data,
  fileName: '${DateTime.now().millisecondsSinceEpoch}.txt',
  folderName: 'batch_docs',
)).toList();
```

`filesData` est une liste de contenus de fichiers bruts (`Uint8List`). Pour chaque fichier de la liste, elle crée un objet `UploadData`.

Le nom du fichier est généré dynamiquement en utilisant l'horodatage actuel (`DateTime.now().millisecondsSinceEpoch`), garantissant que chaque fichier a un nom unique.

Tous les fichiers sont placés dans le dossier `"batch_docs"` de Firebase Storage. De cette façon, vous disposez d'une liste structurée de fichiers prêts à être uploadés.

#### 3\. Mécanisme d'upload de fichiers multiples

```dart
final urls = await uploadService.uploadMultipleDoc(files: files);
```

On demande au `uploadService` d'uploader tous les fichiers d'un coup en utilisant sa méthode `uploadMultipleDoc`. Il uploade chaque fichier vers Firebase Storage. Une fois terminé, il retourne une liste d'URLs de téléchargement, une pour chaque fichier uploadé.

#### 4\. Gérer le succès ou l'échec

```dart
print('Tous les fichiers ont été uploadés : $urls');
```

En cas de succès, elle affiche les URLs de tous les fichiers uploadés (afin que vous puissiez les utiliser plus tard, par exemple, pour afficher ou partager les documents).

```dart
print('Échec de l'upload groupé : $e');
```

Si quelque chose ne va pas, elle capture l'exception et logge le message d'erreur.

En résumé, cette fonction prend plusieurs fichiers bruts, les encapsule dans des objets `UploadData`, les uploade tous vers Firebase Storage en utilisant la couche de service, et affiche les URLs de téléchargement résultantes.

## Bonnes pratiques

1. Validez la taille du fichier avant l'upload pour éviter les fichiers trop volumineux.
    
2. Restreignez les types de fichiers (par exemple, uniquement `image/*`) pour améliorer la sécurité.
    
3. Stockez les métadonnées (comme l'ID utilisateur, l'horodatage) dans Firestore avec l'URL de téléchargement.
    
4. Utilisez des chemins uniques (`uploads/userId/filename`) pour éviter les collisions.
    

## Conclusion

Vous disposez maintenant d'un service d'upload réutilisable et modulaire pour Flutter Web qui prend en charge l'upload de fichiers uniques et multiples, gère les erreurs de manière structurée et utilise l'Injection de Dépendances pour une architecture propre.

Cette base facilite l'extension future du service, par exemple en ajoutant la suppression de fichiers, le suivi de la progression de l'upload ou les uploads authentifiés.

### Références

1. [Firebase Storage pour Flutter](https://firebase.google.com/docs/storage/flutter/start)
    
2. [Référence de l'API Firebase Storage](https://pub.dev/documentation/firebase_storage/latest/firebase_storage/firebase_storage-library.html)
    
3. [Package injectable](https://pub.dev/packages/injectable)
    
4. [Package get_it](https://pub.dev/packages/get_it)