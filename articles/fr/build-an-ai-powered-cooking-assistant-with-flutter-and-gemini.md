---
title: Comment créer un assistant culinaire alimenté par l'IA avec Flutter et Gemini
subtitle: ''
author: Atuoha Anthony
co_authors: []
series: null
date: '2025-05-29T16:33:16.373Z'
originalURL: https://freecodecamp.org/news/build-an-ai-powered-cooking-assistant-with-flutter-and-gemini
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1748533427117/1c8c2384-c6a3-4ad8-ab40-1eee65b2c914.png
tags:
- name: Flutter
  slug: flutter
- name: flutter-aware
  slug: flutter-aware
- name: 'AISprint '
  slug: aisprint
- name: gemini
  slug: gemini
seo_title: Comment créer un assistant culinaire alimenté par l'IA avec Flutter et
  Gemini
seo_desc: After soaking in everything shared at GoogleIO, I can’t lie – I feel supercharged!
  From What’s New in Flutter to Building Agentic Apps with Flutter and Firebase AI
  Logic, and the deep dive into How Flutter Makes the Most of Your Platforms, it felt
  li...
---

Après avoir absorbé tout ce qui a été partagé lors de [GoogleIO](https://www.youtube.com/playlist?list=PLOU2XLYxmsIL4mCDJICu2vLPNw-zdcGAt), je ne peux pas mentir – je me sens superchargé ! De [What's New in Flutter](https://io.google/2025/explore/pa-keynote-12) à [Building Agentic Apps with Flutter and Firebase AI Logic](https://io.google/2025/explore/technical-session-6), en passant par l'exploration approfondie de [How Flutter Makes the Most of Your Platforms](https://io.google/2025/explore/technical-session-25), cela ressemblait à se brancher directement dans la Matrice de la puissance de développement.

Mais le véritable clou du spectacle pour moi ? La présentation de David utilisant [Firebase Studio](https://firebase.studio/) et [Builder.io](https://builder.io) était un chef-d'œuvre. Je l'ai déjà vérifié, et c'est tout aussi génial que cela en avait l'air. Associez cela à tout ce que Gemini propose... et wow. Nous entrons dans une toute nouvelle ère de développement d'applications.

L'intelligence artificielle (IA) n'est plus un concept futuriste – c'est une partie intégrante de notre vie quotidienne, transformant la manière dont nous interagissons avec la technologie et le monde qui nous entoure.

Des recommandations personnalisées sur les plateformes de streaming aux assistants intelligents qui gèrent nos emplois du temps, les applications de l'IA sont vastes et en constante expansion. Sa capacité à traiter d'énormes ensembles de données, à identifier des motifs et à prendre des décisions éclairées révolutionne les industries, de la santé à la finance... et maintenant, même la cuisine !

À l'avant-garde de cette révolution de l'IA se trouvent des plateformes puissantes comme **Vertex AI de Google** et **Gemini**. Vertex AI est une plateforme unifiée d'apprentissage automatique qui vous permet de créer, déployer et mettre à l'échelle des modèles ML plus rapidement et plus efficacement. Elle fournit une suite complète d'outils pour l'ensemble du flux de travail ML, de la préparation des données au déploiement et à la surveillance des modèles. Considérez-la comme votre atelier tout-en-un pour créer des systèmes intelligents.

Gemini, en revanche, est le modèle d'IA le plus capable et flexible de Google. C'est un grand modèle de langage multimodal (LLM), ce qui signifie qu'il peut comprendre et traiter des informations dans divers modes – texte, images, audio, et plus encore. Cela rend Gemini incroyablement polyvalent, lui permettant de gérer des tâches complexes qui nécessitent une compréhension nuancée de différents types de données. Pour les développeurs, Gemini ouvre un monde de possibilités pour créer des applications hautement intelligentes et intuitives.

Complétant ces puissants modèles d'IA, il y a **Firebase AI Studio**, une suite d'outils au sein de Firebase conçue pour simplifier l'intégration des capacités d'IA dans vos applications. Il rationalise le processus de connexion de votre application aux modèles Gemini, facilitant l'exploitation de la puissance de l'IA générative sans se perdre dans une infrastructure complexe.

### Construire un assistant culinaire alimenté par l'IA avec Flutter et Gemini

Dans cet article, je vais démontrer comment j'ai exploité la puissance combinée de Gemini et Flutter pour construire un assistant culinaire alimenté par l'IA.

Stimulé par une récente explosion de curiosité culinaire, j'ai décidé d'essayer de construire une application (Snap2Chef) qui pourrait identifier n'importe quel aliment à partir d'une photo ou d'une commande vocale, fournir une recette détaillée, donner des instructions de cuisine étape par étape, et même me lier à une vidéo YouTube pertinente pour un guide visuel.

Que j'explore de nouveaux plats ou que j'essaie de préparer un repas avec ce que j'ai sous la main, cette application alimentée par Gemini rend l'expérience culinaire plus intelligente et plus accessible.

### Prérequis

Pour tirer le meilleur parti de ce guide, assurez-vous d'avoir les prérequis suivants en place (non obligatoires) :

* **Environnement de développement Flutter** : Vous devez avoir une configuration de développement Flutter fonctionnelle, incluant le SDK Flutter, un IDE compatible (comme VS Code ou Android Studio), et des émulateurs ou appareils physiques configurés pour les tests.

* **Connaissances de base à intermédiaires en Flutter** : Familiarité avec l'arborescence des widgets Flutter, la gestion d'état (par exemple, `StatefulWidget`, `setState`), la programmation asynchrone (`Future`, `async/await`), et la gestion des entrées utilisateur est essentielle.

* **Projet Google Cloud et clé API** : Vous aurez besoin d'un projet Google Cloud actif avec l'API Vertex AI et l'API Gemini activées. Assurez-vous d'avoir une clé API générée et prête à l'emploi. Bien que nous l'utiliserons directement dans l'application à des fins de démonstration, **pour les applications de production, il est fortement recommandé d'utiliser un backend sécurisé pour proxyfier vos requêtes vers les API de Google.**

* **Compréhension de base des API REST** : Connaître le fonctionnement des requêtes HTTP (GET, POST) et des données JSON sera bénéfique, bien que le package `google_generative_ai` abstraie une grande partie de cela.

* **Configuration des ressources** : Si vous utilisez une image de remplissage locale (`placeholder.png` dans `assets/images/`), assurez-vous que votre fichier `pubspec.yaml` est correctement configuré pour inclure cette ressource.

### Voici ce que nous allons couvrir :

1. [Comment obtenir votre clé API Gemini](#heading-comment-obtenir-votre-cle-api-gemini)

2. [Configurer votre projet Flutter et les dépendances](#heading-configurer-votre-projet-flutter-et-les-dependances)

3. [Structure du projet](#heading-structure-du-projet)

* [1. Le dossier `core`](#heading-1-le-dossier-core)

* [2. Le dossier `infrastructure`](#heading-2-le-dossier-infrastructure)

* [3. Le dossier `presentation`](#heading-3-le-dossier-presentation)

4. [Permissions : Assurer la fonctionnalité de l'application et la confidentialité de l'utilisateur](#heading-permissions-assurer-la-fonctionnalite-de-lapplication-et-la-confidentialite-de-lutilisateur)

5. [Ressources : Gérer les ressources de l'application](#heading-assets-managing-application-resources)

6. [Icônes de l'application : Personnaliser l'identité de votre application](#heading-app-icons-customizing-your-applications-identity)

7. [Écran de démarrage : La première impression](#heading-splash-screen-the-first-impression)

8. [Captures d'écran de l'application](#heading-screenshots-from-the-app)

9. [Références](#heading-references)

## **Comment obtenir votre clé API Gemini**

Pour utiliser le modèle Gemini, vous aurez besoin d'une clé API. Vous pouvez en obtenir une en suivant ces étapes :

1. Allez sur [Google AI Studio](https://aistudio.google.com/app/apikey).

2. Connectez-vous avec votre compte Google.

3. Cliquez sur "Obtenir une clé API" ou "Créer une clé API dans un nouveau projet".

4. Copiez la clé API générée.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1748068929897/6e05ea8a-b80b-4bef-90c7-0ffddafa4965.png align="center")

**Note de sécurité importante :**

Dans le code fourni pour HomeScreen, la clé API est directement intégrée sous la forme String apiKey = "";. Ce n'est pas une pratique sécurisée pour les applications de production. Intégrer directement les clés API dans votre code côté client (comme une application Flutter) les expose à l'ingénierie inverse et à une utilisation abusive potentielle.

Pour sécuriser vos clés API dans une application Flutter, je vous recommande vivement de consulter mon article : [Comment sécuriser les API mobiles dans Flutter](https://www.freecodecamp.org/news/how-to-secure-mobile-apis-in-flutter/). Cet article couvre diverses bonnes pratiques, notamment :

* Utilisation de variables d'environnement ou de configurations de build.

* Stockage des clés dans un stockage local sécurisé (bien que toujours côté client).

* Proxyfication des requêtes API via un serveur backend pour masquer véritablement votre clé API.

* Utilisation de Firebase Extensions ou de Cloud Functions pour la logique côté serveur qui interagit avec les modèles d'IA, sans exposer la clé au client.

Pour ce tutoriel, nous allons garder cela simple, mais donnez toujours la priorité à la sécurité des API dans vos projets réels !

## **Configurer votre projet Flutter et les dépendances**

Pour commencer, créons un nouveau projet Flutter et configurons les dépendances nécessaires dans votre fichier `pubspec.yaml`.

Tout d'abord, créez un nouveau projet Flutter en exécutant :

```bash
flutter create snap2chef
cd snap2chef
```

Maintenant, ouvrez `pubspec.yaml` et ajoutez les dépendances suivantes :

```yaml
dependencies:
  flutter:
    sdk: flutter
  google_generative_ai: ^0.4.7
  permission_handler: ^12.0.0+1
  file_picker: ^10.1.9
  image_cropper: ^9.1.0
  image_picker: ^1.1.2
  path_provider: ^2.1.5
  fluttertoast: ^8.2.12
  gap: ^3.0.1
  iconsax: ^0.0.8
  dotted_border: ^2.1.0
  youtube_player_flutter: ^9.1.1
  flutter_markdown: ^0.7.7+1
  loader_overlay: ^5.0.0
  flutter_spinkit: ^5.2.1
  cached_network_image: ^3.4.1
  flutter_native_splash: ^2.4.4
  flutter_launcher_icons: ^0.14.3
  speech_to_text: ^7.0.0

dev_dependencies:
  flutter_test:
    sdk: flutter
  flutter_lints: ^5.0.0
  build_runner: ^2.4.13
```

Après avoir ajouté les dépendances, exécutez `flutter pub get` dans votre terminal pour les récupérer :

```bash
flutter pub get
```

## **Structure du projet**

Nous allons organiser notre projet en trois dossiers principaux (avec divers sous-dossiers) pour maintenir une architecture propre et évolutive :

* `core` : Contient les fonctionnalités principales, les utilitaires et les composants partagés.

* `infrastructure` : Gère les services externes, la manipulation des données et la logique métier.

* `presentation` : Contient la couche d'interface utilisateur, y compris les écrans, les widgets et les composants.

* `main.dart` : Le point d'entrée de notre application Flutter.

Plongeons dans les détails de chaque dossier.

### 1. Le dossier `core`

Le dossier `core` contiendra les `extensions`, les `constants` et les utilitaires `shared`.

##### Le dossier `extensions`

Ce répertoire contiendra des méthodes d'extension qui ajoutent de nouvelles fonctionnalités aux classes existantes.

`format_to_mb.dart` :

```dart
extension ByTeToMegaByte on int {
  int formatToMegaByte() {
    int bytes = this;
    return (bytes / (1024 * 1024)).ceil();
  }
}
```

Cette extension sur le type int (entiers) fournit une méthode pratique `formatToMegaByte()`. Lorsqu'elle est appelée sur un entier représentant des octets, elle convertit cette valeur d'octets en mégaoctets. La division par `(1024 * 1024)` convertit les octets en mégaoctets, et `.ceil()` arrondit le résultat au nombre entier le plus proche. Cela est utile pour afficher les tailles de fichiers dans un format plus lisible pour les humains.

`loading.dart` :

```dart
import 'package:flutter/material.dart';
import 'package:loader_overlay/loader_overlay.dart';

extension LoaderOverlayExtension on BuildContext {
  void showLoader() {
    loaderOverlay.show();
  }

  void hideLoader() {
    loaderOverlay.hide();
  }
}
```

Cette extension sur `BuildContext` simplifie le processus d'affichage et de masquage d'un overlay de chargement global dans votre application Flutter. Elle utilise le package loader_overlay.

* `showLoader()` : Appelle `loaderOverlay.show()` pour afficher l'indicateur de chargement.

* `hideLoader()` : Appelle `loaderOverlay.hide()` pour masquer l'indicateur de chargement. Ces extensions facilitent le contrôle du loader à partir de n'importe quel widget ayant accès à un `BuildContext`.

`to_file.dart` :

```dart
import 'dart:io';

import 'package:image_picker/image_picker.dart';

extension ToFile on Future<XFile?> {
  Future<File?> toFile() => then((xFile) => xFile?.path).then(
        (filePath) => filePath != null ? File(filePath) : null,
      );
}
```

Cette extension est conçue pour convertir un objet XFile (généralement obtenu à partir du package image_picker) en un objet File de dart:io.

* Elle fonctionne sur un `Future<XFile?>`, ce qui signifie qu'elle attend un futur qui pourrait se résoudre en un `XFile` ou `null`.

* `then((xFile) => xFile?.path)` : Si `xFile` n'est pas null, il extrait le chemin du fichier. Sinon, il transmet `null`.

* `then((filePath) => filePath != null ? File(filePath) : null)` : Si un `filePath` est disponible, il crée un objet `File` à partir de celui-ci. Sinon, il retourne `null`. C'est une manière concise de gérer la conversion asynchrone d'une image ou d'une vidéo `XFile` sélectionnée en un objet `File` qui peut être utilisé pour des opérations ultérieures comme l'affichage ou le téléchargement.

`to_file2.dart` :

```dart
import 'dart:io';
import 'package:image_picker/image_picker.dart';
import 'package:path_provider/path_provider.dart';

extension XFileExtension on XFile {
  Future<File> toFile() async {
    final bytes = await readAsBytes();
    final tempDir = await getTemporaryDirectory();
    final tempFile = File('${tempDir.path}/${this.name}');
    await tempFile.writeAsBytes(bytes);
    return tempFile;
  }
}
```

Cette extension sur XFile fournit une manière plus robuste de convertir un XFile en un fichier dart:io. Cela est particulièrement utile lorsque vous devez écrire le contenu du XFile dans un emplacement temporaire.

* `await readAsBytes()` : Lit le contenu du `XFile` sous forme de liste d'octets.

* `final tempDir = await getTemporaryDirectory()` : Obtient le chemin vers le répertoire temporaire sur l'appareil en utilisant `path_provider`.

* `final tempFile = File('${tempDir.path}/${this.name}')` : Crée un nouvel objet `File` dans le répertoire temporaire avec le nom original du `XFile`.

* `await tempFile.writeAsBytes(bytes)` : Écrit les octets lus à partir du `XFile` dans le nouveau fichier temporaire.

* `return tempFile` : Retourne le nouvel objet `File` créé. Cela est particulièrement utile lorsque vous travaillez avec des `XFile` qui n'ont peut-être pas un chemin de fichier facilement accessible sur l'appareil, ou si vous devez vous assurer que le fichier est persistamment disponible pour un traitement ultérieur, comme le rognage.

#### Le dossier `constants`

Ce répertoire contiendra des valeurs statiques et des énumérations utilisées dans toute l'application.

`enums/record_source.dart` :

```dart
enum RecordSource { camera, gallery }
```

Il s'agit d'une énumération (enum) simple nommée `RecordSource`. Elle définit deux valeurs possibles : `camera` et `gallery`. Cette énumération est utilisée pour représenter la source à partir de laquelle une image ou une vidéo est sélectionnée, offrant une manière claire et sécurisée de différencier la capture depuis la caméra et la sélection depuis la galerie de l'appareil.

`enums/status.dart` :

```dart
enum Status { success, error }
```

Il s'agit d'une autre énumération simple nommée `Status`. Elle définit `success` et `error` comme ses valeurs possibles. Cette énumération est couramment utilisée pour indiquer le résultat d'une opération ou d'un processus, offrant une manière standardisée de transmettre des informations de statut, par exemple pour les messages toast.

`app_strings.dart` :

```dart
// ignore_for_file: constant_identifier_names

class AppStrings {
  static const String AI_MODEL = 'gemini-2.0-flash';

  static const String APP_SUBTITLE =  "Capturez une photo ou utilisez votre voix pour obtenir des instructions étape par étape sur la préparation de vos plats ou collations préférés";
  static const String APP_TITLE = "Votre guide de recettes IA personnel";

  static const String AI_TEXT_PART = "Vous êtes un expert en recettes IA. Générez une recette basée sur cette image, incluez le nom de la recette, les étapes de préparation et une vidéo YouTube publique démontrant l'étape de préparation. Affichez l'URL de la vidéo YouTube sur une nouvelle ligne précédée de 'YouTube Video URL: ', elle doit être une URL https et l'URL de l'image sur une nouvelle ligne précédée de 'Image URL: ' et elle doit également être une URL https."
      "Si l'image n'est pas un aliment, une collation ou une boisson, informez poliment l'utilisateur que vous ne pouvez répondre qu'aux requêtes de recettes et demandez-lui de fermer et de télécharger une image d'aliment/collation/boisson.";

  static const String AI_AUDIO_PART =
  "Vous êtes un expert en recettes IA. Générez une recette basée sur ce texte, incluez le nom de la recette, les étapes de préparation. J'aimerais également que vous me montriez une image valide en ligne concernant cet aliment/boisson/collation et une vidéo YouTube publique démontrant l'étape de préparation. Si le texte ne contient pas de choses liées à un aliment, une collation ou une boisson, informez poliment l'utilisateur que vous ne pouvez répondre qu'aux requêtes de recettes et demandez-lui de fermer et de télécharger une image d'aliment/collation/boisson. Affichez l'URL de la vidéo YouTube sur une nouvelle ligne précédée de 'YouTube Video URL: ', elle doit être une URL https et l'URL de l'image sur une nouvelle ligne précédée de 'Image URL: ' et elle doit également être une URL https. Le texte est : ";

}
```

Cette classe `AppStrings` centralise toutes les constantes de chaînes statiques utilisées dans l'application. Cette approche aide à gérer les chaînes efficacement, les rendant facilement modifiables et évitant les fautes de frappe.

* `AI_MODEL` : Spécifie le modèle Gemini à utiliser, dans ce cas, `gemini-2.0-flash`.

* `APP_SUBTITLE` et `APP_TITLE` : Définissent les titres et sous-titres principaux de l'interface utilisateur de l'application.

* `AI_TEXT_PART` : Il s'agit d'une chaîne cruciale qui sert de prompt pour le modèle Gemini **lorsqu'une image est fournie**. Elle indique à l'IA d'agir en tant qu'expert en recettes, de générer une recette incluant le nom et les étapes, et de fournir une vidéo YouTube. Elle inclut également un message de repli si l'image n'est pas liée à la nourriture.

* `AI_AUDIO_PART` : Similaire à `AI_TEXT_PART`, mais ce prompt est utilisé lorsque **l'entrée audio est fournie**. Il indique également à l'IA de générer une recette, d'inclure une image en ligne pertinente et une vidéo YouTube, avec des exigences de formatage spécifiques pour les URL. Ce prompt sera concaténé avec le texte transcrit de l'entrée vocale de l'utilisateur.

`app_color.dart` :

```dart
import 'package:flutter/material.dart';

class AppColors {
  static const primaryColor = Color(0xFF7E57C2);
  static const litePrimary = Color(0xFFEDE7F6);
  static Color errorColor = const Color(0xFFEA5757);
  static const Color grey =
  Color.fromARGB(255, 170, 170, 170);

  static const Color lighterGrey =
  Color.fromARGB(255, 204, 204, 204);
}
```

La classe `AppColors` centralise toutes les définitions de couleurs personnalisées utilisées dans l'application. Cela facilite le maintien d'un schéma de couleurs cohérent dans toute l'interface utilisateur et permet des changements globaux rapides du thème de l'application. Chaque constante statique représente une couleur spécifique avec sa valeur hexadécimale ou sa valeur RVB.

#### Le dossier `shared`

Ce répertoire contiendra des classes utilitaires partagées.

`image_picker_helper.dart` :

```dart
import 'dart:developer';
import 'dart:io';

import 'package:file_picker/file_picker.dart';
import 'package:flutter/foundation.dart' show immutable;
import 'package:image_picker/image_picker.dart';
import 'package:permission_handler/permission_handler.dart';
import 'package:snap2chef/core/extensions/to_file.dart';
import 'package:snap2chef/core/extensions/to_file2.dart';
import '../../presentation/components/toast_info.dart';
import '../constants/enums/status.dart';

@immutable
class ImagePickerHelper {
  static final ImagePicker _imagePicker = ImagePicker();

  static Future<PickedFileWithInfo?> pickImageFromGallery2() async {
    final isGranted = await Permission.photos.isGranted;
    if (!isGranted) {
      await Permission.photos.request();
      toastInfo(
          msg: "Vous n'avez pas autorisé l'accès", status: Status.error);
    }
    final pickedFile =
    await _imagePicker.pickImage(source: ImageSource.gallery);
    if (pickedFile != null) {
      final file = await pickedFile.toFile();
      log(pickedFile.name.split(".").join(","));
      return PickedFileWithInfo(file: file, fileName: pickedFile.name);
    } else {
      return null;
    }
  }

  static Future<FilePickerResult?> pickFileFromGallery() =>
      FilePicker.platform.pickFiles(
          type: FileType.custom,
          allowedExtensions: ["pdf", "doc", "docx", "png", "jpg", "jpeg"]);

  static Future<File?> pickImageFromGallery() =>
      _imagePicker.pickImage(source: ImageSource.gallery).toFile();

  static Future<File?> takePictureFromCamera() =>
      _imagePicker.pickImage(source: ImageSource.camera).toFile();

  static Future<File?> pickVideoFromGallery() =>
      _imagePicker.pickVideo(source: ImageSource.gallery).toFile();

  static Future<FilePickerResult?> pickSinglePDFFileFromGallery() =>
      FilePicker.platform
          .pickFiles(type: FileType.custom, allowedExtensions: ["pdf"]);
}

class PickedFileWithInfo {
  final File file;
  final String fileName;

  PickedFileWithInfo({required this.file, required this.fileName});
}

PlatformFile? file;
```

La classe `ImagePickerHelper` fournit des méthodes statiques pour sélectionner divers types de fichiers (images, vidéos, documents) à partir de la galerie ou de la caméra de l'appareil, avec une gestion intégrée des permissions.

* `_imagePicker` : Une instance de `ImagePicker` pour interagir avec les fonctionnalités de sélection d'images et de vidéos de l'appareil.

* `pickImageFromGallery2()` :

* **Gestion des permissions** : Vérifie si la permission de la galerie de photos est accordée en utilisant `permission_handler`. Si ce n'est pas le cas, elle demande la permission et affiche un message toast si elle est refusée.

* **Sélection d'image** : Utilise `_imagePicker.pickImage(source: ImageSource.gallery)` pour permettre à l'utilisateur de sélectionner une image dans la galerie.

* **Conversion** : Si une image est sélectionnée, elle convertit le `XFile` en un objet `File` en utilisant l'extension `toFile()`.

* **Journalisation** : Journalise le nom du fichier pour le débogage.

* **Valeur de retour** : Retourne un objet `PickedFileWithInfo` contenant le `File` et `fileName`.

* `pickFileFromGallery()` : Utilise `file_picker` pour permettre la sélection de divers types de fichiers (PDF, Doc, Docx, PNG, JPG, JPEG) dans la galerie.

* `pickImageFromGallery()` : Une méthode plus simple pour sélectionner une image dans la galerie, retournant directement un `Future<File?>` en utilisant l'extension `toFile()`.

* `takePictureFromCamera()` : Capture une image en utilisant la caméra de l'appareil et retourne un `Future<File?>`.

* `pickVideoFromGallery()` : Sélectionne une vidéo dans la galerie et retourne un `Future<File?>`.

* `pickSinglePDFFileFromGallery()` : Sélectionne spécifiquement un seul fichier PDF dans la galerie.

* `PickedFileWithInfo` class : Une simple classe de données pour contenir à la fois l'objet `File` et son `fileName`.

Cette classe d'assistance centralise toute la logique de sélection de fichiers, la rendant réutilisable et plus facile à gérer les permissions et les différents scénarios de sélection.

### 2. Le dossier `infrastructure`

Ce dossier gère la logique d'interaction avec les services externes et le traitement des données.

##### `image_upload_controller.dart` :

```dart
import 'dart:async';
import 'dart:io';

import 'package:flutter/material.dart';
import 'package:gap/gap.dart';
import 'package:iconsax/iconsax.dart';
import 'package:image_cropper/image_cropper.dart';

import '../core/constants/app_colors.dart';
import '../core/constants/enums/record_source.dart';
import '../core/shared/image_picker_helper.dart';
import '../presentation/widgets/image_picker_component.dart';

class ImageUploadController {
  /// Rogner l'image
  static Future<void> _cropImage(
      File? selectedFile,
      Function assignCroppedImage,
      ) async {
    if (selectedFile != null) {
      final croppedFile = await ImageCropper().cropImage(
        sourcePath: selectedFile.path,
        compressFormat: ImageCompressFormat.jpg,
        compressQuality: 100,
        uiSettings: [
          AndroidUiSettings(
            toolbarTitle: 'Rogner l\'image',
            toolbarColor: AppColors.primaryColor,
            toolbarWidgetColor: Colors.white,
            initAspectRatio: CropAspectRatioPreset.square,
            lockAspectRatio: false,
            statusBarColor: AppColors.primaryColor,
            activeControlsWidgetColor: AppColors.primaryColor,
            aspectRatioPresets: [
              CropAspectRatioPreset.original,
              CropAspectRatioPreset.square,
              CropAspectRatioPreset.ratio4x3,
              CropAspectRatioPresetCustom(),
            ],
          ),
          IOSUiSettings(
            title: 'Rogner l\'image',
            aspectRatioPresets: [
              CropAspectRatioPreset.original,
              CropAspectRatioPreset.square,
              CropAspectRatioPreset.ratio4x3,
              CropAspectRatioPresetCustom(),
            ],
          ),
        ],
      );
      assignCroppedImage(croppedFile);
    }
  }

  // /// Sélectionner une image depuis la caméra et la galerie
  static void imagePicker(
      RecordSource recordSource,
      Completer? completer,
      BuildContext context,
      Function setFile,
      Function assignCroppedImage,
      ) async {
    if (recordSource == RecordSource.gallery) {
      final pickedFile = await ImagePickerHelper.pickImageFromGallery();
      if (pickedFile == null) {
        return;
      }
      completer?.complete(pickedFile.path);
      if (!context.mounted) {
        return;
      }
      setFile(pickedFile);

      if (context.mounted) {
        Navigator.of(context).pop();
      }
    } else if (recordSource == RecordSource.camera) {
      final pickedFile = await ImagePickerHelper.takePictureFromCamera();
      if (pickedFile == null) {
        return;
      }

      completer?.complete(pickedFile.path);
      if (!context.mounted) {
        return;
      }
      setFile(pickedFile);
      // Rogner l'image
      _cropImage(pickedFile, assignCroppedImage);

      if (context.mounted) {
        Navigator.of(context).pop();
      }
    }
  }

  /// Modal pour sélectionner la source du fichier
  static Future showFilePickerButtonSheet(BuildContext context, Completer? completer,
      Function setFile,
      Function assignCroppedImage,) {
    return showModalBottomSheet(
      shape: const RoundedRectangleBorder(
        borderRadius: BorderRadius.only(
          topLeft: Radius.circular(35),
          topRight: Radius.circular(35),
        ),
      ),
      context: context,
      builder: (context) {
        return SingleChildScrollView(
          child: Container(
            padding: const EdgeInsets.fromLTRB(10, 14, 15, 20),
            child: Column(
              children: [
                Container(
                  height: 4,
                  width: 50,
                  padding: const EdgeInsets.only(top: 5),
                  decoration: BoxDecoration(
                    borderRadius: BorderRadius.circular(7),
                    color: const Color(0xffE4E4E4),
                  ),
                ),
                Padding(
                  padding: const EdgeInsets.all(10.0),
                  child: Column(
                    mainAxisSize: MainAxisSize.min,
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      GestureDetector(
                        onTap: () => Navigator.of(context).pop(),
                        child: const Align(
                          alignment: Alignment.topRight,
                          child: Icon(Icons.close, color: Colors.grey),
                        ),
                      ),
                      const Gap(10),
                      const Text(
                        'Sélectionner la source de l\'image',
                        style: TextStyle(
                          color: AppColors.primaryColor,
                          fontSize: 16,
                          fontWeight: FontWeight.w600,
                        ),
                      ),
                      const Gap(20),
                      ImagePickerTile(
                        title: 'Capture depuis la caméra',
                        subtitle: 'Prendre une photo instantanée',
                        icon: Iconsax.camera,
                        recordSource: RecordSource.camera,
                        completer: completer,
                        context: context,
                        setFile: setFile,
                        assignCroppedImage: assignCroppedImage,
                      ),
                      const Divider(color: Color(0xffE4E4E4)),
                      ImagePickerTile(
                        title: 'Télécharger depuis la galerie',
                        subtitle: 'Sélectionner une image depuis la galerie',
                        icon: Iconsax.gallery,
                        recordSource: RecordSource.gallery,
                        completer: completer,
                        context: context,
                        setFile: setFile,
                        assignCroppedImage: assignCroppedImage,
                      ),
                    ],
                  ),
                ),
              ],
            ),
          ),
        );
      },
    );
  }
}

class CropAspectRatioPresetCustom implements CropAspectRatioPresetData {
  @override
  (int, int)? get data => (2, 3);

  @override
  String get name => '2x3 (personnalisé)';
}
```

La classe `ImageUploadController` gère le processus de sélection et de rognage éventuel des images avant qu'elles ne soient utilisées dans l'application.

* `_cropImage(File? selectedFile, Function assignCroppedImage)` :

* Cette **méthode statique privée** gère la fonctionnalité de rognage d'image en utilisant le package `image_cropper`.

* Elle prend un `selectedFile` (l'image à rogner) et une `Function assignCroppedImage` (un rappel pour mettre à jour l'interface utilisateur avec l'image rognée).

* `ImageCropper().cropImage(...)` ouvre l'interface utilisateur de rognage. Elle est configurée avec divers paramètres d'interface utilisateur pour Android et iOS, y compris `toolbarColor`, `aspectRatioPresets`, et plus encore, pour garantir une expérience cohérente et personnalisée.

* `CropAspectRatioPresetCustom()` : Il s'agit d'une classe personnalisée qui implémente `CropAspectRatioPresetData` pour définir un rapport d'aspect de rognage spécifique (2x3 dans ce cas), offrant plus de flexibilité que les préréglages intégrés.

* Une fois rognée, le `croppedFile` est passé au rappel `assignCroppedImage`.

* `imagePicker(RecordSource recordSource, Completer? completer, BuildContext context, Function setFile, Function assignCroppedImage)` :

* Cette **méthode statique** est la logique principale pour initier la sélection d'images à partir de la caméra ou de la galerie.

* Elle prend un `recordSource` (de l'énumération `RecordSource`), un `completer` optionnel (probablement pour gérer les opérations asynchrones en dehors de l'interface utilisateur), le `context` actuel, `setFile` (un rappel pour définir le fichier sélectionné dans l'interface utilisateur), et `assignCroppedImage` (le rappel pour les images rognées).

* **Sélection de la galerie (`RecordSource.gallery`) :

* Elle appelle `ImagePickerHelper.pickImageFromGallery()` pour obtenir l'image sélectionnée.

* Si un fichier est sélectionné, elle complète le `completer`, appelle `setFile` pour mettre à jour l'interface utilisateur, puis ferme la feuille de fond.

* **Capture de la caméra (`RecordSource.camera`) :

* Elle appelle `ImagePickerHelper.takePictureFromCamera()` pour capturer une image.

* De manière similaire à la sélection de la galerie, elle complète le `completer`, appelle `setFile`, puis, de manière importante, elle appelle `_cropImage` pour permettre à l'utilisateur de rogner la nouvelle image capturée avant qu'elle ne soit pleinement utilisée.

* Enfin, elle ferme la feuille de fond.

* Les vérifications `context.mounted` sont incluses pour s'assurer que les mises à jour de l'interface utilisateur ne se produisent que si le widget est toujours dans l'arborescence des widgets, empêchant ainsi les erreurs.

* `showFilePickerButtonSheet(...)` :

* Cette **méthode statique** affiche une feuille de fond modale, offrant à l'utilisateur des options pour sélectionner une source d'image (Caméra ou Galerie).

* Elle utilise `showModalBottomSheet` pour présenter une feuille élégante avec des coins arrondis.

* À l'intérieur de la feuille, elle affiche un indicateur glissant et deux widgets `ImagePickerTile` (probablement un widget personnalisé pour afficher chaque option) pour "Capture depuis la caméra" et "Télécharger depuis la galerie".

* Lorsqu'un `ImagePickerTile` est tapé, il appelle en interne la méthode `imagePicker` avec le `RecordSource` correspondant.

En résumé, `ImageUploadController` agit comme un orchestrateur central pour l'acquisition d'images, offrant des options pour sélectionner depuis la galerie ou la caméra, et intégrant des capacités de rognage d'images robustes – le tout en garantissant une expérience utilisateur fluide grâce à des rappels d'interface utilisateur et des interactions modales.

##### `recipe_controller.dart` :

```dart
import 'dart:io';

import 'package:cached_network_image/cached_network_image.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:flutter_markdown/flutter_markdown.dart';
import 'package:gap/gap.dart';
import 'package:google_generative_ai/google_generative_ai.dart';
import 'package:snap2chef/core/extensions/loading.dart';
import 'package:youtube_player_flutter/youtube_player_flutter.dart';
import '../core/constants/app_colors.dart';
import '../core/constants/app_strings.dart';
import '../core/constants/enums/status.dart';
import '../presentation/components/toast_info.dart';

class RecipeController {
  // Envoyer l'image à Gemini
  static Future<void> _sendImageToGemini(
      File? selectedFile,
      GenerativeModel model,
      BuildContext context,
      Function removeFile,
      Function removeText,
      ) async {
    toastInfo(msg: "Obtention de la recette et des préparations", status: Status.success);

    if (selectedFile == null) return;

    final bytes = await selectedFile.readAsBytes();

    final prompt = TextPart(AppStrings.AI_TEXT_PART);
    final image = DataPart('image/jpeg', bytes);

    final response = await model.generateContent([
      Content.multi([prompt, image]),
    ]);

    if (context.mounted) {
      _displayRecipe(
        response.text,
        context,
        selectedFile,
        removeFile,
        removeText,
      );
    }
  }

  // Envoyer la requête audio texte
  static Future<void> _sendAudioTextPrompt(
      GenerativeModel model,
      BuildContext context,
      String transcribedText,
      File? selectedFile,
      Function removeFile,
      Function removeText,
      ) async {
    toastInfo(msg: "Obtention de la recette et des préparations", status: Status.success);

    final prompt = '${AppStrings.AI_AUDIO_PART} ${transcribedText.trim()}.';
    final content = [Content.text(prompt)];
    final response = await model.generateContent(content);

    if (context.mounted) {
      _displayRecipe(
        response.text,
        context,
        selectedFile,
        removeFile,
        removeText,
      );
    }
  }

  static void _displayRecipe(
      String? recipeText,
      BuildContext context,
      File? selectedFile,
      Function removeFile,
      Function removeText,
      ) {
    if (recipeText == null || recipeText.isEmpty) {
      recipeText = "Aucune recette n'a pu être générée ou analysée à partir de la réponse.";
    }
    String workingRecipeText = recipeText;

    String? videoId;
    String? extractedImageUrl;

    final youtubeLineRegex = RegExp(r'YouTube Video URL:\s*(https?:\/\/\S+)', caseSensitive: false);
    final youtubeMatch = youtubeLineRegex.firstMatch(recipeText);
    if (youtubeMatch != null) {
      final youtubeUrl = youtubeMatch.group(1);
      final ytIdRegex = RegExp(r'v=([\w-]{11})');
      final ytIdMatch = ytIdRegex.firstMatch(youtubeUrl ?? '');
      if (ytIdMatch != null) {
        videoId = ytIdMatch.group(1);
      }
      workingRecipeText = workingRecipeText.replaceAll(youtubeMatch.group(0)!, '').trim();
    }

    final imageLine = RegExp(r'Image URL:\s*(https?:\/\/\S+\.(?:png|jpe?g|gif|webp|bmp|svg))');
    final imageMatch = imageLine.firstMatch(recipeText);
    if (imageMatch != null) {
      extractedImageUrl = imageMatch.group(1);
      workingRecipeText = workingRecipeText.replaceAll(imageMatch.group(0)!, '').trim();
    }

    print("Extracted Image URL: $extractedImageUrl");
    print("Extracted Video ID: $videoId");

    String? cleanedRecipeText = workingRecipeText;

    showDialog(
      barrierDismissible: false,
      context: context,
      builder: (BuildContext dialogContext) {
        YoutubePlayerController? ytController;

        if (videoId != null) {
          ytController = YoutubePlayerController(
            initialVideoId: videoId,
            flags: const YoutubePlayerFlags(
              autoPlay: false,
              mute: false,
              disableDragSeek: false,
              loop: false,
              isLive: false,
              forceHD: false,
              enableCaption: true,
            ),
          );
        }

        return AlertDialog(
          title: const Text('Recette générée'),
          content: SingleChildScrollView(
            child: Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                selectedFile != null
                    ? Container(
                  height: 150,
                  width: double.infinity,
                  decoration: BoxDecoration(
                    borderRadius: BorderRadius.circular(7),
                    border: Border.all(color: AppColors.primaryColor),
                    image: DecorationImage(
                      image: FileImage(File(selectedFile.path)),
                      fit: BoxFit.cover,
                    ),
                  ),
                )
                    :  extractedImageUrl != null
                    ? ClipRRect(
                  borderRadius: BorderRadius.circular(7),
                  child: CachedNetworkImage(
                    imageUrl: extractedImageUrl,
                    height: 150,
                    width: double.infinity,
                    fit: BoxFit.cover,
                    placeholder: (context, url) =>
                        Image.asset('assets/images/placeholder.png', fit: BoxFit.cover),
                    errorWidget: (context, url, error) =>
                        Image.asset('assets/images/placeholder.png', fit: BoxFit.cover),
                  ),
                )
                    : const SizedBox.shrink(),
                Gap(16),
                MarkdownBody(
                  data: cleanedRecipeText,
                  styleSheet: MarkdownStyleSheet(
                    h1: const TextStyle(
                      fontSize: 24,
                      fontWeight: FontWeight.bold,
                      color: Colors.deepPurple,
                    ),
                    h2: const TextStyle(
                      fontSize: 20,
                      fontWeight: FontWeight.bold,
                    ),
                    strong: const TextStyle(fontWeight: FontWeight.bold),
                  ),
                ),

                if (videoId != null && ytController != null) ...[
                  const Gap(16),
                  YoutubePlayer(
                    controller: ytController,
                    showVideoProgressIndicator: true,
                    progressIndicatorColor: AppColors.primaryColor,
                    progressColors: const ProgressBarColors(
                      playedColor: AppColors.primaryColor,
                      handleColor: Colors.amberAccent,
                    ),
                    onReady: () {
                      // Le contrôleur est prêt
                    },
                  ),
                ],
              ],
            ),
          ),
          actions: <Widget>[
            TextButton(
              onPressed: () {
                ytController?.dispose();
                Navigator.of(dialogContext).pop();
                if (selectedFile != null) {
                  removeFile();
                } else {
                  removeText();
                }
              },
              child: const Text('Fermer'),
            ),
          ],
        );
      },
    );
  }

  static void sendRequest(
      BuildContext context,
      File? selectedFile,
      GenerativeModel model,
      Function removeFile,
      String transcribedText,
      Function removeText,
      ) async {
    context.showLoader();
    toastInfo(msg: "Traitement...", status: Status.success);
    try {
      if (selectedFile != null) {
        await _sendImageToGemini(
          selectedFile,
          model,
          context,
          removeFile,
          removeText,
        );
      } else if (transcribedText.isNotEmpty) {
        await _sendAudioTextPrompt(
          model,
          context,
          transcribedText,
          selectedFile,
          removeFile,
          removeText,
        );
      }
    } catch (e) {
      if (kDebugMode) {
        print('Erreur lors de l\'envoi de la requête : $e');
      }
      toastInfo(msg: "Erreur lors de l\'envoi de la requête : $e", status: Status.error);
    } finally {
      if (context.mounted) {
        context.hideLoader();
      }
    }
  }
}
```

La classe `RecipeController` est responsable de l'interaction avec le modèle d'IA Gemini pour générer des recettes et ensuite afficher ces recettes à l'utilisateur, complètes avec les liens YouTube analysés et les URL d'images potentiellement extraites.

* `_sendImageToGemini(File? selectedFile, GenerativeModel model, BuildContext context, Function removeFile, Function removeText)` :

* Cette **méthode statique privée** gère l'envoi d'une image au modèle Gemini.

* Elle affiche un message toast "Traitement...".

* Elle lit le `selectedFile` (l'image) en tant qu'octets.

* Elle crée un `TextPart` à partir de `AppStrings.AI_TEXT_PART` (notre prompt basé sur l'image) et un `DataPart` pour les octets de l'image.

* `model.generateContent([Content.multi([prompt, image])])` : C'est là que la magie opère ! Elle envoie à la fois le prompt texte et les données de l'image au modèle Gemini pour la génération.

* Une fois la réponse reçue, elle appelle `_displayRecipe` pour montrer la recette générée à l'utilisateur.

* La vérification `context.mounted` garantit que le contexte est toujours valide avant de tenter des mises à jour de l'interface utilisateur.

* `_sendAudioTextPrompt(GenerativeModel model, BuildContext context, String transcribedText, File? selectedFile, Function removeFile, Function removeText)` :

* Cette **méthode statique privée** gère l'envoi du texte audio transcrit au modèle Gemini.

* Elle construit un prompt complet en concaténant `AppStrings.AI_AUDIO_PART` avec le `transcribedText`.

* `model.generateContent([Content.text(prompt)])` : Elle envoie uniquement le prompt texte au modèle Gemini.

* De manière similaire à la méthode d'image, elle appelle `_displayRecipe` avec le texte généré.

* `_displayRecipe(String? recipeText, BuildContext context, File? selectedFile, Function removeFile, Function removeText)` :

* Cette **méthode statique privée** est responsable de l'analyse de la réponse de l'IA et de son affichage dans une boîte de dialogue modale.

* **Gestion des erreurs** : Si `recipeText` est null ou vide, elle fournit un message par défaut.

* **Extraction de l'URL de la vidéo YouTube** : Elle utilise une `RegExp` (`youtubeLineRegex`) pour trouver une ligne dans le `recipeText` qui correspond au motif "YouTube Video URL: https://...". Si elle est trouvée, elle extrait l'URL complète et ensuite une autre `RegExp` (`ytIdRegex`) pour obtenir l'ID de la vidéo YouTube. Le texte de l'URL de la vidéo YouTube extraite est ensuite supprimé de `workingRecipeText` pour nettoyer la recette affichée.

* **Extraction de l'URL de l'image** : De manière similaire, elle utilise une autre `RegExp` (`imageLine`) pour extraire une URL d'image du `recipeText`. Le texte de l'URL de l'image extraite est également supprimé.

* **Impression de débogage** : Imprime les URL extraites pour le débogage.

* `showDialog` : Présente un `AlertDialog` à l'utilisateur.

* `YoutubePlayerController` : Si un `videoId` a été extrait, il initialise un `YoutubePlayerController` du package `Youtubeer_flutter`, configuré avec des flags de base (par exemple, `autoPlay: false`).

* **Affichage de la recette** :

* Si un `selectedFile` (image prise par l'utilisateur) est présent, il affiche cette image.

* Sinon, si une `extractedImageUrl` a été trouvée dans la réponse de l'IA, il utilise `CachedNetworkImage` pour afficher cette image. Cela est particulièrement utile pour les requêtes basées sur du texte où Gemini pourrait suggérer une image.

* `MarkdownBody` : Utilise `flutter_markdown` pour rendre le `cleanedRecipeText` (après avoir supprimé les URL YouTube et Image) en tant que Markdown, permettant un formatage de texte riche (par exemple, mise en gras, titres) directement à partir de la réponse de l'IA.

* `YoutubePlayer` : Si un `videoId` et `ytController` sont disponibles, il intègre le lecteur vidéo YouTube directement dans la boîte de dialogue, avec des couleurs de barre de progression personnalisables.

* **Bouton "Fermer"** : Dispose du `ytController` (important pour la gestion des ressources), ferme la boîte de dialogue et appelle soit `removeFile()` soit `removeText()` pour effacer les champs de saisie en fonction de ce qui a été utilisé pour la requête.

* `sendRequest(BuildContext context, File? selectedFile, GenerativeModel model, Function removeFile, String transcribedText, Function removeText)` :

* Cette **méthode statique publique** est le point d'entrée pour l'envoi de requêtes au modèle Gemini.

* `context.showLoader()` : Affiche un overlay de chargement en utilisant notre extension personnalisée.

* `toastInfo(msg: "Traitement...", status: Status.success)` : Affiche un message toast.

* **Logique conditionnelle** :

* Si `selectedFile` n'est pas null, elle appelle `_sendImageToGemini`.

* Sinon, si `transcribedText` n'est pas vide, elle appelle `_sendAudioTextPrompt`.

* **Gestion des erreurs** : Utilise un bloc `try-catch` pour gérer gracieusement toute erreur lors de la requête IA, les journalisant en mode débogage et affichant un toast d'erreur à l'utilisateur.

* **Bloc `finally`** : Garantit que `context.hideLoader()` est toujours appelé, quelle que soit la réussite ou l'erreur, pour masquer l'indicateur de chargement.

En résumé, `RecipeController` orchestrer l'ensemble du processus d'envoi de l'entrée utilisateur (image ou voix), de communication avec l'IA Gemini, d'analyse de sa réponse intelligente et de sa belle présentation à l'utilisateur avec des éléments interactifs comme les vidéos YouTube et les images pertinentes.

### 3. Le dossier `presentation`

Ce dossier contient tout le code lié à l'interface utilisateur.

##### `screens/home_screen.dart` :

```dart
import 'dart:async';
import 'dart:io';
import 'package:flutter/material.dart';
import 'package:gap/gap.dart';
import 'package:google_generative_ai/google_generative_ai.dart';
import 'package:iconsax/iconsax.dart';
import 'package:image_cropper/image_cropper.dart';
import 'package:snap2chef/core/extensions/format_to_mb.dart';
import 'package:snap2chef/infrastructure/image_upload_controller.dart';
import 'package:snap2chef/infrastructure/recipe_controller.dart';
import 'package:speech_to_text/speech_recognition_result.dart';
import 'package:speech_to_text/speech_to_text.dart';
import '../../core/constants/app_colors.dart';
import '../../core/constants/app_strings.dart';
import '../../core/constants/enums/status.dart';
import '../components/toast_info.dart';
import '../widgets/glowing_microphone.dart';
import '../widgets/image_previewer.dart';
import '../widgets/query_text_box.dart';
import '../widgets/upload_container.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  File? selectedFile;
  Completer? completer;
  String? fileName;
  int? fileSize;
  late GenerativeModel _model;
  String apiKey = ""; // <--- REMPLACER PAR VOTRE VRAIE CLÉ API
  final TextEditingController _query = TextEditingController();
  final SpeechToText _speechToText = SpeechToText();
  bool _speechEnabled = false;
  String _lastWords = '';
  bool isRecording = false;
  bool isDoneRecording = false;

  void removeText() {
    setState(() {
      _query.clear();
      isDoneRecording = false;
      _lastWords = "";
    });
    _query.clear();
  }

  void setKeyword(String prompt) {
    if (prompt.isEmpty) {
      toastInfo(msg: "Vous n'avez rien dit !", status: Status.error);
      setState(() {
        isDoneRecording = false;
        isRecording = false;
      });
      return;
    }

    setState(() {
      _lastWords = "";
      isRecording = false;
      _query.text = prompt;
      isDoneRecording = true;
    });
  }

  void _initSpeech() async {
    try {
      _speechEnabled = await _speechToText.initialize(
        onStatus: (status) => debugPrint('Statut de la parole : $status'),
        onError: (error) => debugPrint('Erreur de parole : $error'),
      );
      if (!_speechEnabled) {
        toastInfo(
          msg: "Permission du microphone non accordée ou parole non disponible.",
          status: Status.error,
        );
      }
      setState(() {});
    } catch (e) {
      debugPrint("Échec de l'initialisation de la parole : $e");
    }
  }

  void _startListening() async {
    setState(() {
      isRecording = true;
    });
    if (!_speechEnabled) {
      toastInfo(msg: "La parole n'est pas encore initialisée.", status: Status.error);
      return;
    }

    await _speechToText.listen(onResult: _onSpeechResult);
    setState(() {});
  }

  void _stopListening() async {
    await _speechToText.stop();
    setKeyword(_lastWords);
    setState(() {});
  }

  void _onSpeechResult(SpeechRecognitionResult result) {
    setState(() {
      _lastWords = result.recognizedWords;
    });
  }

  @override
  void initState() {
    super.initState();
    // TODO: Remplacer "VOTRE_CLÉ_API" par votre vraie clé API Gemini
    // Consultez https://www.freecodecamp.org/news/how-to-secure-mobile-apis-in-flutter/ pour la sécurité des clés API.
    apiKey = "VOTRE_CLÉ_API"; // Sécurisez cela !
    _model = GenerativeModel(model: AppStrings.AI_MODEL, apiKey: apiKey);
    _initSpeech();
  }

  @override
  void dispose() {
    _query.dispose();
    _speechToText.cancel(); // Annuler l'écoute pour éviter les fuites de ressources
    super.dispose();
  }

  void assignCroppedImage(CroppedFile? croppedFile) {
    if (croppedFile != null) {
      setState(() {
        selectedFile = File(croppedFile.path);
      });
    }
  }

  void setFile(File? pickedFile) {
    setState(() {
      selectedFile = pickedFile;
      fileName = pickedFile?.path.split('/').last;
      fileSize = pickedFile?.lengthSync().formatToMegaByte();
    });
  }

  void removeFile() {
    setState(() {
      selectedFile = null;
      fileSize = null;
    });
  }

  @override
  Widget build(BuildContext context) {
    Size size = MediaQuery.sizeOf(context);

    return Scaffold(
      floatingActionButton: selectedFile != null || _query.text.isNotEmpty
          ? FloatingActionButton.extended(
        onPressed: () => RecipeController.sendRequest(
          context,
          selectedFile,
          _model,
          removeFile,
          _query.text,
          removeText,
        ),
        backgroundColor: AppColors.primaryColor,
        icon: const Icon(Iconsax.send_1, color: Colors.white),
        label: const Text(
          "Envoyer la requête",
          style: TextStyle(color: Colors.white),
        ),
      )
          : null,
      body: Padding(
        padding: const EdgeInsets.all(18.0),
        child: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Text(
                AppStrings.APP_TITLE,
                textAlign: TextAlign.center,
                style: TextStyle(
                  color: Colors.black,
                  fontWeight: FontWeight.w500,
                  fontSize: 16,
                ),
              ),
              Text(
                AppStrings.APP_SUBTITLE,
                textAlign: TextAlign.center,
                style: TextStyle(
                  color: AppColors.grey,
                  fontSize: 15,
                  fontWeight: FontWeight.w300,
                ),
              ),
              const Gap(20),
              if (!isDoneRecording)
                !isRecording
                    ? selectedFile != null
                    ? ImagePreviewer(
                  size: size,
                  pickedFile: selectedFile,
                  removeFile: removeFile,
                  context: context,
                  completer: completer,
                  setFile: setFile,
                  assignCroppedImage: assignCroppedImage,
                )
                    : GestureDetector(
                  onTap: () =>
                      ImageUploadController.showFilePickerButtonSheet(
                        context,
                        completer,
                        setFile,
                        assignCroppedImage,
                      ),
                  child: UploadContainer(
                    title: 'une image d\'un aliment ou d\'une collation',
                    size: size,
                  ),
                )
                    : SizedBox.shrink(),
              const Gap(20),

              if (selectedFile == null) ...[
                if (!isDoneRecording) ...[
                  Text(
                    "ou enregistrez votre voix",
                    style: TextStyle(
                      color: AppColors.grey,
                      fontSize: 16,
                      fontWeight: FontWeight.w200,
                    ),
                  ),
                  Center(
                    child: GestureDetector(
                      onTap: () {
                        if (!_speechEnabled) {
                          toastInfo(
                            msg: "La reconnaissance vocale n\'est pas encore prête.",
                            status: Status.error,
                          );
                          return;
                        }
                        if (_speechToText.isNotListening) {
                          _startListening();
                        } else {
                          _stopListening();
                        }
                      },
                      child: GlowingMicButton(
                        isListening: !_speechToText.isNotListening,
                      ),
                    ),
                  ),
                  const Gap(10),
                  Container(
                    padding: EdgeInsets.all(16),
                    child: Text(
                      _speechToText.isListening
                          ? _lastWords
                          : _speechEnabled
                          ? 'Appuyez sur le microphone pour commencer à écouter...'
                          : 'La parole n\'est pas disponible',
                    ),
                  ),
                  const Gap(10),
                ],

                isDoneRecording
                    ? QueryTextBox(query: _query)
                    : SizedBox.shrink(),
              ],

              const Gap(20),
              selectedFile != null || _query.text.isNotEmpty
                  ? GestureDetector(
                onTap: () {
                  if (selectedFile != null) {
                    removeFile();
                  } else {
                    removeText();
                  }
                },
                child: CircleAvatar(
                  backgroundColor: AppColors.primaryColor,
                  radius: 30,
                  child: Icon(Iconsax.close_circle, color: Colors.white),
                ),
              )
                  : SizedBox.shrink(),
            ],
          ),
        ),
      ),
    );
  }
}
```

L'écran d'accueil est l'interface utilisateur principale de notre application d'assistant culinaire alimenté par l'IA. Il gère l'état de la sélection d'image, de l'entrée vocale et déclenche la génération de recettes par l'IA.

* **Variables d'état :**

* `selectedFile` : Stocke l'objet `File` de l'image sélectionnée par l'utilisateur.

* `completer` : Un objet `Completer`, souvent utilisé pour les opérations asynchrones afin de signaler l'achèvement.

* `fileName`, `fileSize` : Stocke les détails de l'image sélectionnée.

* `_model` : Une instance de `GenerativeModel` du package `google_generative_ai`, qui est notre interface avec l'API Gemini.

* `apiKey` : **C'est ici que vous insérerez votre clé API Gemini.** N'oubliez pas l'avertissement de sécurité ci-dessus !

* `_query` : Un `TextEditingController` pour le champ de saisie de texte, qui affichera le texte transcrit de l'entrée vocale.

* `_speechToText` : Une instance de `SpeechToText` pour gérer la reconnaissance vocale.

* `_speechEnabled` : Un booléen indiquant si la reconnaissance vocale est initialisée et disponible.

* `_lastWords` : Stocke les mots récemment reconnus de la parole.

* `isRecording` : Un booléen pour suivre si l'enregistrement vocal est actif.

* `isDoneRecording` : Un booléen pour suivre si un enregistrement vocal a été finalisé et transcrit.

* **Méthodes :**

* `removeText()` : Efface le champ de saisie de texte (`_query`), réinitialise `isDoneRecording` et `_lastWords` pour effacer toute entrée vocale précédente.

* `setKeyword(String prompt)` : Définit le texte `_query` sur le `prompt` (voix transcrite), et met à jour les états `isRecording` et `isDoneRecording`. Il fournit également un message toast si le prompt est vide.

* `_initSpeech()` : Initialise le plugin `SpeechToText`. Il demande la permission du microphone et définit `_speechEnabled` en fonction du succès de l'initialisation. Si les permissions ne sont pas accordées, il affiche un toast d'erreur.

* `_startListening()` : Démarre l'écouteur de reconnaissance vocale. Définit `isRecording` sur `true`.

* `_stopListening()` : Arrête l'écouteur de reconnaissance vocale et appelle `setKeyword` avec `_lastWords` pour finaliser le texte transcrit.

* `_onSpeechResult(SpeechRecognitionResult result)` : Méthode de rappel pour `SpeechToText` qui met à jour `_lastWords` avec les mots reconnus au fur et à mesure que la reconnaissance vocale progresse.

* `initState()` : Appelé lorsque le widget est inséré dans l'arborescence des widgets. Il initialise le `_model` avec la clé API Gemini et le nom du modèle, et appelle `_initSpeech()` pour configurer la reconnaissance vocale.

* `dispose()` : Appelé lorsque le widget est retiré de l'arborescence des widgets. Il dispose du contrôleur `_query` et annule l'écouteur `_speechToText` pour éviter les fuites de mémoire.

* `assignCroppedImage(CroppedFile? croppedFile)` : Fonction de rappel passée à `ImageUploadController` pour mettre à jour `selectedFile` avec le chemin de la nouvelle image rognée.

* `setFile(File? pickedFile)` : Fonction de rappel passée à `ImageUploadController` pour mettre à jour `selectedFile` avec l'image sélectionnée, et extrait également son `fileName` et `fileSize` en utilisant notre extension personnalisée.

* `removeFile()` : Efface les états `selectedFile` et `fileSize`, supprimant ainsi l'image affichée.

* `build(BuildContext context)` Méthode – Disposition de l'interface utilisateur :

* `FloatingActionButton.extended` : Ce bouton, étiqueté "Envoyer la requête", devient visible uniquement lorsqu'une image (`selectedFile`) est choisie OU lorsqu'il y a du texte dans la boîte de requête (`_query.text.isNotEmpty`). En appuyant dessus, il déclenche `RecipeController.sendRequest` avec l'entrée pertinente.

* **Titre et sous-titre de l'application** : Affiche les en-têtes principaux en utilisant `AppStrings`.

* **Section de téléchargement/prévisualisation d'image** :

* Si `!isDoneRecording` (ce qui signifie qu'aucune entrée vocale n'a été finalisée) et `!isRecording` (ne pas enregistrer actuellement la voix) :

* Si `selectedFile` n'est pas null, il affiche un widget `ImagePreviewer` pour afficher l'image choisie avec une option pour la supprimer.

* Sinon (aucune image sélectionnée), il affiche un `UploadContainer` qui agit comme une zone cliquable pour déclencher `ImageUploadController.showFilePickerButtonSheet` pour sélectionner une image.

* **Section d'entrée vocale** :

* Cette section (`if (selectedFile == null) ...`) n'apparaît que si aucune image n'est sélectionnée, offrant une méthode d'entrée alternative.

* Si `!isDoneRecording`, elle affiche un texte "ou enregistrez votre voix" et un `GlowingMicButton`.

* En appuyant sur le `GlowingMicButton`, on bascule la reconnaissance vocale (`_startListening` / `_stopListening`).

* Un widget `Text` affiche l'état actuel de la reconnaissance vocale ou `_lastWords` au fur et à mesure qu'ils sont transcrits.

* Si `isDoneRecording` (ce qui signifie que l'entrée vocale a été finalisée), il affiche un `QueryTextBox` qui affiche le texte transcrit, permettant une révision avant l'envoi de la requête.

* **Bouton de suppression de l'entrée** : Un `CircleAvatar` avec une icône de fermeture apparaît lorsqu'une image est sélectionnée ou qu'un texte est présent dans la requête. En appuyant dessus, il appelle `removeFile()` ou `removeText()` pour effacer l'entrée respective.

En résumé, `HomeScreen` adapte intelligemment son interface utilisateur en fonction de l'entrée de l'utilisateur (image ou voix) et orchestrer l'interaction avec le `ImageUploadController` pour la gestion des images et le `RecipeController` pour la génération de recettes par l'IA.

#### Le dossier `components`

Ce dossier contient des éléments d'interface utilisateur plus petits et réutilisables.

##### `toast_info.dart`

```dart
import 'package:fluttertoast/fluttertoast.dart';
import '../../core/constants/app_colors.dart';
import 'package:flutter/material.dart'; // Import pour MaterialColor/Colors

void toastInfo({
  required String msg,
  required Status status,
}) {
  Fluttertoast.showToast(
    msg: msg,
    toastLength: Toast.LENGTH_SHORT,
    gravity: ToastGravity.BOTTOM,
    timeInSecForIosWeb: 1,
    backgroundColor: status == Status.success ? AppColors.primaryColor : AppColors.errorColor,
    textColor: Colors.white,
    fontSize: 16.0,
  );
}
```

La fonction `toastInfo` fournit un moyen pratique d'afficher des messages brefs et non intrusifs (toasts) à l'utilisateur, généralement pour des retours comme les messages de "succès" ou "erreur".

Elle prend deux paramètres requis :

* `msg` : La chaîne de message à afficher dans le toast.

* `status` : Une énumération de type `Status` (`success` ou `error`) qui détermine la couleur de fond du toast.

`Fluttertoast.showToast(...)` est la fonction principale du package `fluttertoast` qui affiche le toast.

* `toastLength` : Définit la durée pendant laquelle le toast est visible (court).

* `gravity` : Positionne le toast en bas de l'écran.

* `timeInSecForIosWeb` : Durée pour le web/iOS.

* `backgroundColor` : Définit dynamiquement la couleur de fond sur `AppColors.primaryColor` pour le succès et `AppColors.errorColor` pour les erreurs, fournissant des indices visuels à l'utilisateur.

* `textColor` : Définit la couleur du texte en blanc.

* `fontSize` : Définit la taille de la police du message du toast.

Cette fonction centralise l'affichage des messages toast, garantissant une cohérence dans l'apparence et le comportement dans toute l'application.

#### Le dossier `widgets`

L'interface utilisateur de l'application est construite à l'aide d'une série de widgets Flutter bien définis et réutilisables. Chaque widget sert un objectif spécifique, contribuant à la fonctionnalité globale et à l'esthétique de Snap2Chef.

1. `glowing_microphone.dart` :

Ce widget crée un bouton de microphone animé qui indique visuellement lorsque l'application écoute activement l'entrée vocale.

```dart
import 'package:flutter/material.dart';
import 'package:iconsax/iconsax.dart';

import '../../core/constants/app_colors.dart';

class GlowingMicButton extends StatefulWidget {
  final bool isListening;

  const GlowingMicButton({super.key, required this.isListening});

  @override
  State<GlowingMicButton> createState() => _GlowingMicButtonState();
}

class _GlowingMicButtonState extends State<GlowingMicButton>
    with SingleTickerProviderStateMixin {
  late final AnimationController _controller;
  late final Animation<double> _animation;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(
      vsync: this,
      duration: const Duration(seconds: 2),
    );

    _animation = Tween<double>(begin: 0.0, end: 25.0).animate(
      CurvedAnimation(parent: _controller, curve: Curves.easeOut),
    );

    if (widget.isListening) {
      _controller.repeat(reverse: true);
    }
  }

  @override
  void didUpdateWidget(covariant GlowingMicButton oldWidget) {
    super.didUpdateWidget(oldWidget);

    if (widget.isListening && !_controller.isAnimating) {
      _controller.repeat(reverse: true);
    } else if (!widget.isListening && _controller.isAnimating) {
      _controller.stop();
    }
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      width: 100, // Suffisamment d'espace pour le glow complet
      height: 100,
      child: Stack(
        alignment: Alignment.center,
        children: [
          if (widget.isListening)
            AnimatedBuilder(
              animation: _animation,
              builder: (_, __) {
                return Container(
                  width: 60 + _animation.value,
                  height: 60 + _animation.value,
                  decoration: BoxDecoration(
                    shape: BoxShape.circle,
                    color: AppColors.primaryColor.withOpacity(0.15),
                  ),
                );
              },
            ),
          CircleAvatar(
            backgroundColor: AppColors.primaryColor,
            radius: 30,
            child: Icon(
              widget.isListening ? Iconsax.stop_circle : Iconsax.microphone,
              color: Colors.white,
            ),
          ),
        ],
      ),
    );
  }
}
```

* `GlowingMicButton` (StatefulWidget) : Il s'agit d'un `StatefulWidget` car il doit gérer son propre état d'animation. Il prend une propriété `final bool isListening`, qui dicte si le microphone doit afficher une animation de lueur ou rester statique.

* `_GlowingMicButtonState` (State avec `SingleTickerProviderStateMixin`) :

* `SingleTickerProviderStateMixin` : Ce mixin est crucial pour fournir un `Ticker` à un `AnimationController`. Un `Ticker` fait essentiellement avancer l'animation, en la liant aux rappels de frame, assurant ainsi une animation fluide.

* `_controller` (AnimationController) : Gère l'animation. Il est initialisé avec `vsync: this` (de `SingleTickerProviderStateMixin`) et une `duration` de 2 secondes.

* `_animation` (Animation<double>) : Définit la plage de valeurs que l'animation produira. Ici, un `Tween<double>(begin: 0.0, end: 25.0)` est utilisé avec une `CurvedAnimation` (spécifiquement `Curves.easeOut`) pour créer un effet fluide et décélérant à mesure que la lueur s'étend.

* `initState()` : Lorsque le widget est créé pour la première fois, le `AnimationController` et `Animation` sont initialisés. Si `isListening` est initialement `true`, l'animation est définie sur `repeat(reverse: true)` pour faire pulser la lueur en continu.

* `didUpdateWidget()` : Cette méthode de cycle de vie est appelée lorsque la configuration du widget (ses propriétés) change. Elle vérifie si `isListening` a changé et démarre ou arrête l'animation en conséquence. Cela garantit que l'animation réagit dynamiquement aux changements de l'état `isListening` de son parent.

* `dispose()` : Crucialement, la méthode `_controller.dispose()` est appelée ici pour libérer les ressources détenues par le contrôleur d'animation lorsque le widget est retiré de l'arborescence des widgets, empêchant ainsi les fuites de mémoire.

* `build()` Méthode :

* `SizedBox` : Fournit une taille fixe (100x100) pour le bouton, garantissant suffisamment d'espace pour l'effet de lueur.

* `Stack` : Permet de superposer des widgets les uns sur les autres.

* `if (widget.isListening) AnimatedBuilder(...)` : Ce conditionnel rend l'effet de lueur *uniquement* lorsque `isListening` est `true`.

* `AnimatedBuilder` : Reconstruit son enfant chaque fois que `_animation` change de valeur.

* À l'intérieur de `AnimatedBuilder`, un `Container` est utilisé pour créer la lueur circulaire. Sa `width` et `height` sont dynamiquement augmentées par `_animation.value`, créant l'effet d'expansion. La `color` est `AppColors.primaryColor` avec une opacité de `0.15`, lui donnant une lueur subtile.

* `CircleAvatar` : Il s'agit du bouton principal du microphone.

* `backgroundColor` est `AppColors.primaryColor`.

* `radius` est `30`.

* Le `child` est une `Icon` du package `Iconsax`, changeant dynamiquement entre `Iconsax.stop_circle` (lors de l'écoute) et `Iconsax.microphone` (lors de l'absence d'écoute). La couleur de l'icône est blanche.

2. `image_picker_component.dart`

Ce widget fournit une interface `ListTile` réutilisable pour que les utilisateurs puissent sélectionner des images à partir de la caméra ou de la galerie.

```dart
import 'dart:async';

import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:snap2chef/infrastructure/image_upload_controller.dart';

import '../../core/constants/app_colors.dart';
import '../../core/constants/enums/record_source.dart';

class ImagePickerTile extends StatelessWidget {
  const ImagePickerTile({
    super.key,
    required this.title,
    required this.subtitle,
    required this.icon,
    required this.recordSource,
    required this.completer,
    required this.context,
    required this.setFile,
    required this.assignCroppedImage,
  });

  final String title;
  final String subtitle;
  final IconData icon;
  final RecordSource recordSource;
  final Completer? completer;
  final BuildContext context;
  final Function setFile;
  final Function assignCroppedImage;

  @override
  Widget build(BuildContext context) {
    return ListTile(
      leading: CircleAvatar(
        backgroundColor: AppColors.litePrimary,
        child: Padding(
          padding: const EdgeInsets.all(3.0),
          child: Center(
            child: Icon(icon, color: AppColors.primaryColor, size: 20),
          ),
        ),
      ),
      title: Text(title, style: const TextStyle(color: Colors.black)),
      subtitle: Text(
        subtitle,
        style: const TextStyle(fontSize: 14, color: Colors.grey),
      ),
      trailing: const Icon(
        CupertinoIcons.chevron_right,
        size: 20,
        color: Color(0xffE4E4E4),
      ),
      onTap: () {
        ImageUploadController.imagePicker(
          recordSource,
          completer,
          context,
          setFile,
          assignCroppedImage,
        );
      },
    );
  }
}
```

* `ImagePickerTile` (StatelessWidget) : Il s'agit d'un `StatelessWidget` car il se contente de rendre du contenu basé sur ses propriétés immuables et de déclencher une fonction externe (`ImageUploadController.imagePicker`) lorsqu'il est tapé.

* **Propriétés :** Il prend plusieurs propriétés `final` pour le rendre hautement personnalisable :

* `title` et `subtitle` : Texte pour les lignes principale et secondaire de la tuile de liste.

* `icon` : Le `IconData` à afficher en tant qu'icône principale.

* `recordSource` : Une énumération (`RecordSource`) indiquant probablement si l'image doit être sélectionnée à partir de la caméra ou de la galerie.

* `completer` : Un objet `Completer`, souvent utilisé pour les opérations asynchrones afin de signaler lorsqu'une tâche est terminée.

* `context` : Le `BuildContext` pour permettre à `ImageUploadController` d'afficher des dialogues ou de naviguer.

* `setFile` : Une fonction de rappel `Function` pour mettre à jour le fichier image sélectionné dans le widget parent.

* `assignCroppedImage` : Une fonction de rappel `Function` pour gérer le résultat de toute opération de rognage d'image.

* `build()` Méthode :

* `ListTile` : Un widget Flutter standard utilisé pour organiser des éléments dans une seule ligne.

* `leading` : Affiche un `CircleAvatar` avec une couleur de fond primaire claire, contenant l'`icon` spécifiée dans la couleur primaire. Cela crée un bouton d'icône visuellement attrayant à gauche.

* `title` : Affiche le texte `title` en noir.

* `subtitle` : Affiche le texte `subtitle` en gris avec une taille de police de 14, fournissant des informations descriptives supplémentaires.

* `trailing` : Affiche une icône `CupertinoIcons.chevron_right` (flèche droite), courante pour indiquer les éléments navigables ou actionnables dans une liste.

* `onTap` : Il s'agit du point d'interaction principal. Lorsque la `ListTile` est tapée, elle appelle la méthode statique `ImageUploadController.imagePicker`, en passant tous les paramètres nécessaires. Cela centralise la logique de sélection d'image dans `ImageUploadController`, rendant `ImagePickerTile` purement un composant d'interface utilisateur.

3. `image_previewer.dart`

Ce widget est responsable de l'affichage d'une image précédemment sélectionnée et offre des options pour 'Modifier' (re-sélectionner) ou 'Supprimer' l'image.

```dart
import 'dart:async';
import 'dart:io';
import 'package:flutter/material.dart';
import 'package:iconsax/iconsax.dart';
import 'package:snap2chef/infrastructure/image_upload_controller.dart';

class ImagePreviewer extends StatelessWidget {
  const ImagePreviewer({
    super.key,
    required this.size,
    required this.pickedFile,
    required this.removeFile,
    required this.context,
    required this.completer,
    required this.setFile,
    required this.assignCroppedImage,
  });

  final Size size;
  final File? pickedFile;
  final Function removeFile;
  final BuildContext context;
  final Completer? completer;
  final Function setFile;
  final Function assignCroppedImage;

  @override
  Widget build(BuildContext context) {
    return Container(
      height: size.height * 0.13,
      width: double.infinity,
      decoration: BoxDecoration(
        borderRadius: BorderRadius.circular(7),
        // border: Border.all(
        //   color: AppColors.borderColor,
        // ),
        image: DecorationImage(
          image: FileImage(
            File(pickedFile!.path),
          ),
          fit: BoxFit.cover,
        ),
      ),
      child: Stack(
        children: [
          Container(
            decoration: BoxDecoration(
              color: Colors.black.withOpacity(0.3),
              borderRadius: BorderRadius.circular(7),
            ),
          ),
          // Contenu centré
          Center(
            child: Wrap(
              crossAxisAlignment: WrapCrossAlignment.center,
              spacing: 20,
              children: [
                GestureDetector(
                  onTap: () {
                    ImageUploadController.showFilePickerButtonSheet(context,completer,setFile,assignCroppedImage);
                  },
                  child: Column(
                    children: [
                      Icon(
                        Iconsax.edit_2,
                        size: 20,
                        color: Colors.white,
                      ),
                      const Text(
                        'Modifier',
                        style: TextStyle(
                          color: Colors.white,
                          fontSize: 15,
                        ),
                      )
                    ],
                  ),
                ),
                GestureDetector(
                  onTap: () {
                    removeFile();
                  },
                  child: Column(
                    children: [
                      Icon(
                        Iconsax.note_remove,
                        color: Colors.white,
                        size: 20,
                      ),
                      const Text(
                        'Supprimer',
                        style: TextStyle(
                          color: Colors.white,
                          fontSize: 15,
                        ),
                      )
                    ],
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
```

* `ImagePreviewer` (StatelessWidget) : Similaire à `ImagePickerTile`, il s'agit d'un `StatelessWidget` qui affiche du contenu et déclenche des rappels.

* **Propriétés :**

* `size` : La `Size` du widget parent, utilisée pour calculer la `height` du conteneur de prévisualisation de manière proportionnelle.

* `pickedFile` : Un `File?` représentant le fichier image à afficher. Il est nullable, ce qui implique que ce widget ne s'affiche que si un fichier a été sélectionné.

* `removeFile` : Une fonction de rappel `Function` pour gérer la suppression de l'image actuellement affichée.

* `context`, `completer`, `setFile`, `assignCroppedImage` : Ceux-ci sont transmis à `ImageUploadController` lorsque l'action 'Modifier' est déclenchée, similaire à `ImagePickerTile`.

* `build()` Méthode :

* `Container` : Le conteneur principal pour la prévisualisation de l'image.

* `height` : Défini à 13 % de la hauteur de l'écran, fournissant une taille réactive.

* `width` : `double.infinity` pour prendre toute la largeur disponible.

* `decoration` :

* `borderRadius` : Applique des coins arrondis au conteneur.

* `image: DecorationImage(...)` : C'est là que la magie opère. Il affiche le `pickedFile` comme image de fond pour le conteneur.

* `FileImage(File(pickedFile!.path))` : Crée un fournisseur d'image à partir du chemin de fichier local. Le `!` (opérateur d'assertion non nulle) implique que `pickedFile` est censé être non nul lorsque ce widget est affiché.

* `fit: BoxFit.cover` : Assure que l'image couvre tout le conteneur, rognant potentiellement certaines parties.

* `Stack` : Superpose le contenu sur l'image.

* `Container` (Superposition) : Un `Container` semi-transparent noir est placé sur l'image (`Colors.black.withOpacity(0.3)`) pour créer une superposition assombrie. Cela améliore la lisibilité du texte blanc et des icônes placés sur l'image.

* `Center` : Centre les boutons d'action horizontalement et verticalement dans la superposition.

* `Wrap` : Dispose les boutons 'Modifier' et 'Supprimer' horizontalement avec un `spacing` de 20. `WrapCrossAlignment.center` les aligne verticalement dans le `Wrap`.

* `GestureDetector` (pour 'Modifier') :

* `onTap` : Appelle `ImageUploadController.showFilePickerButtonSheet`, permettant à l'utilisateur de re-sélectionner ou de changer l'image. Cette méthode présente probablement une feuille de fond avec des options pour sélectionner depuis la caméra ou la galerie, similaire à la manière dont la sélection initiale d'image fonctionne.

* Son enfant est un `Column` contenant une icône `Iconsax.edit_2` et un texte 'Modifier', tous deux en blanc.

* `GestureDetector` (pour 'Supprimer') :

* `onTap` : Appelle la fonction de rappel `removeFile()`, qui effacerait généralement le `pickedFile` sélectionné dans l'état parent, faisant disparaître ce prévisualisateur ou le faisant revenir à un état de téléchargement.

* Son enfant est un `Column` contenant une icône `Iconsax.note_remove` et un texte 'Supprimer', tous deux en blanc.

4. `query_text_box.dart`

Ce widget fournit un `TextFormField` stylisé pour la saisie de texte multiligne, généralement utilisé pour les requêtes ou notes des utilisateurs.

```dart
import 'package:flutter/material.dart';

import '../../core/constants/app_colors.dart';

class QueryTextBox extends StatelessWidget {
  const QueryTextBox({
    super.key,
    required TextEditingController query,
  }) : _query = query;

  final TextEditingController _query;

  @override
  Widget build(BuildContext context) {
    return TextFormField(
      controller: _query,
      maxLines: 4,
      autofocus: true,
      decoration: InputDecoration(
        hintStyle: TextStyle(color: AppColors.lighterGrey),
        border: OutlineInputBorder(
          borderRadius: BorderRadius.circular(12.0),
          borderSide: BorderSide(color: Colors.grey.shade400),
        ),
        focusedBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(12.0),
          borderSide: const BorderSide(
            color: AppColors.primaryColor,
            width: 2.0,
          ),
        ),
        enabledBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(12.0),
          borderSide: BorderSide(color: Colors.grey.shade300),
        ),
        contentPadding: const EdgeInsets.symmetric(
          vertical: 12.0,
          horizontal: 16.0,
        ),
      ),
      style: const TextStyle(
        fontSize: 14.0,
        color: Colors.black,
      ),
      keyboardType: TextInputType.multiline,
      textInputAction: TextInputAction.newline,
    );
  }
}
```

* `QueryTextBox` (StatelessWidget) : Un `StatelessWidget` qui rend un champ de saisie de texte. Il prend un `TextEditingController` comme paramètre requis, permettant un contrôle externe sur le contenu du champ de texte.

* **Propriétés :**

* `_query` (TextEditingController) : Le contrôleur lié au `TextFormField`. Cela permet de récupérer le texte, de définir le texte initial et d'écouter les changements.

* `build()` Méthode :

* `TextFormField` : Le widget de saisie principal.

* `controller: _query` : Lie le `TextEditingController` à ce champ.

* `maxLines: 4` : Permet au champ de texte de s'étendre jusqu'à 4 lignes avant de devenir défilable.

* `autofocus: true` : Met automatiquement le focus sur le champ de texte lorsque l'écran se charge, faisant apparaître le clavier.

* `decoration: InputDecoration(...)` : Définit le style visuel du champ de saisie.

* `hintStyle` : Définit la couleur du texte d'indice sur `AppColors.lighterGrey`.

* `border` : Définit la bordure par défaut lorsque le champ n'est pas focalisé ou activé, avec des coins arrondis et une bordure grise claire.

* `focusedBorder` : Définit le style de bordure lorsque le champ est activement focalisé par l'utilisateur. Il utilise `AppColors.primaryColor` avec un trait plus large (`width: 2.0`) pour fournir un indicateur visuel clair de focus.

* `enabledBorder` : Définit le style de bordure lorsque le champ est activé mais pas focalisé, en utilisant un gris légèrement plus foncé.

* `contentPadding` : Ajoute un rembourrage interne dans le champ de texte pour un meilleur espacement du texte.

* `style` : Définit la taille de la police à 14.0 et la couleur à noir pour le texte saisi.

* `keyboardType: TextInputType.multiline` : Configure le clavier pour qu'il soit adapté à la saisie de texte multiligne, offrant souvent une touche "retour" qui crée une nouvelle ligne.

* `textInputAction: TextInputAction.newline` : Spécifie que l'appui sur la touche "Terminé" ou "Entrée" du clavier doit insérer une nouvelle ligne.

5. `upload_container.dart`

Ce widget crée un conteneur à "bordure pointillée" visuellement distinct, généralement utilisé comme une zone cliquable pour déclencher le téléchargement ou la sélection de fichiers.

```dart
import 'package:dotted_border/dotted_border.dart';
import 'package:flutter/material.dart';
import 'package:gap/gap.dart';
import 'package:iconsax/iconsax.dart';
import '../../core/constants/app_colors.dart';

class UploadContainer extends StatelessWidget {
  const UploadContainer({
    super.key,
    required this.size,
    required this.title,
  });

  final Size size;
  final String title;

  @override
  Widget build(BuildContext context) {
    return DottedBorder(
      color: AppColors.primaryColor,
      radius: const Radius.circular(15),
      borderType: BorderType.RRect,
      strokeWidth: 1,
      child: SizedBox(
        height: size.height * 0.13,
        width: double.infinity,
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Container(
              height: 70,
              width: 60,
              decoration: BoxDecoration(
                shape: BoxShape.circle,
                color: AppColors.litePrimary,
              ),
              child: Padding(
                padding: const EdgeInsets.all(13.0),
                child: Icon(
                  Iconsax.document_upload,
                  color: AppColors.primaryColor,
                ),
              ),
            ),
            const Gap(5),
            RichText(
              text: TextSpan(
                text: 'Cliquez pour sélectionner ',
                style: TextStyle(
                  color: AppColors.primaryColor,
                ),
                children: [
                  TextSpan(
                    text: title,
                    style: TextStyle(
                      color: Color(0xff555555),
                    ),
                  )
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}
```

* `UploadContainer` (StatelessWidget) : Un `StatelessWidget` principalement pour la présentation visuelle, indiquant une zone de téléchargement.

* **Propriétés :**

* `size` : La `Size` du parent, utilisée pour déterminer la hauteur du conteneur de manière proportionnelle.

* `title` : Une `String` à afficher comme partie du message "Cliquez pour sélectionner [title]".

* `build()` Méthode :

* `DottedBorder` : Ce package fournit l'effet visuel de bordure pointillée.

* `color: AppColors.primaryColor` : La couleur de la ligne pointillée.

* `radius: const Radius.circular(15)` : Applique des coins arrondis à la bordure pointillée.

* `borderType: BorderType.RRect` : Spécifie que la bordure doit suivre une forme de rectangle arrondi.

* `strokeWidth: 1` : Définit l'épaisseur de la ligne pointillée.

* `SizedBox` : Définit les dimensions internes de la zone à l'intérieur de la bordure pointillée, prenant 13 % de la hauteur de l'écran et la largeur complète.

* `Column` : Dispose l'icône et le texte verticalement, centrés dans le `SizedBox`.

* `Container` (Arrière-plan de l'icône) : Un conteneur circulaire avec un arrière-plan `AppColors.litePrimary` contient l'icône de téléchargement.

* `Iconsax.document_upload` : L'icône signifiant une action de téléchargement, colorée avec `AppColors.primaryColor`.

* `Gap(5)` : Du package `gap`, cela fournit un petit espace vertical (5 pixels) entre l'icône et le texte.

* `RichText` : Permet différents styles dans un seul bloc de texte.

* `TextSpan(text: 'Cliquez pour sélectionner ', ...)` : La première partie du message, stylisée avec `AppColors.primaryColor`.

* `children: [TextSpan(text: title, ...)]` : La deuxième partie du message, qui est la propriété `title` passée au widget, stylisée en gris plus foncé. Cette structure permet à "Cliquez pour sélectionner " d'être stylisé de manière cohérente tandis que le `title` (par exemple, "image", "document") peut avoir une apparence différente.

### Résumé de l'implémentation du code

Nous avons couvert un terrain considérable dans cette partie de l'article, transformant notre application Flutter de base en un guide de recettes alimenté par l'IA. Nous avons commencé par configurer l'interface utilisateur principale, puis nous avons approfondi l'intégration du package `google_generative_ai` pour communiquer avec les modèles Gemini de Google pour les entrées d'image et de voix.

Nous avons implémenté une logique robuste pour :

* **Entrée d'image :** Capturer des images depuis la caméra ou la galerie, les rogner et les envoyer au modèle `gemini`.

* **Entrée vocale :** Enregistrer de l'audio et préparer le terrain pour la transcription avant d'envoyer du texte au modèle `gemini`.

* **Affichage de contenu dynamique :** Analyser habilement la réponse de l'IA pour extraire et présenter non seulement le texte de la recette, mais aussi intégrer des vidéos YouTube instructives et même des images pertinentes, le tout dans une boîte de dialogue magnifiquement formatée utilisant `flutter_markdown` et `cached_network_image`. Nous avons également assuré une gestion correcte du cycle de vie pour nos lecteurs multimédias.

Cela met en évidence la facilité avec laquelle vous pouvez exploiter des capacités d'IA avancées comme la compréhension multimodale et la génération de langage naturel dans vos applications Flutter. En construisant sur ces concepts, vous pouvez créer des expériences utilisateur véritablement interactives et intelligentes.

Maintenant que nous avons la logique principale en place pour capturer les entrées, communiquer avec l'IA et afficher ses réponses riches, nous devons nous assurer que notre application peut réellement accéder aux fonctionnalités nécessaires de l'appareil.

## **Permissions : Assurer la fonctionnalité de l'application et la confidentialité de l'utilisateur**

Pour qu'une application Flutter interagisse avec des fonctionnalités système comme la caméra, le microphone ou le stockage de fichiers, elle doit déclarer des permissions spécifiques dans ses manifestes Android et iOS. Ces déclarations informent le système d'exploitation des exigences de l'application et, pour les permissions sensibles, demandent le consentement de l'utilisateur à l'exécution.

### **Permissions Android (dans `android/app/src/main/AndroidManifest.xml`)**

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
    <uses-permission android:name="android.permission.RECORD_AUDIO"/>
    <uses-permission android:name="android.permission.CAMERA" />
    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
    </manifest>
```

Voici ce qui se passe :

* `<uses-permission android:name="android.permission.RECORD_AUDIO"/>` : Cette permission est nécessaire pour que l'application accède au microphone de l'appareil et enregistre de l'audio. Elle est cruciale pour toute fonctionnalité de reconnaissance vocale ou d'entrée vocale, comme le suggère le `GlowingMicButton`.

* `<uses-permission android:name="android.permission.CAMERA" />` : Accorde à l'application l'accès à la caméra de l'appareil. Cela est essentiel pour les fonctionnalités qui permettent aux utilisateurs de prendre des photos, comme celles activées par `ImagePickerTile` ou `ImagePreviewer`.

* `<uses-permission android:name="android.permission.INTERNET" />` : Il s'agit d'une permission fondamentale requise pour presque toutes les applications modernes qui se connectent à Internet. Elle permet à l'application d'envoyer et de recevoir des données à partir de services web, comme interagir avec l'API Gemini, Firebase ou Vertex AI.

* `<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />` : Permet à l'application de lire des fichiers à partir du stockage externe partagé de l'appareil (par exemple, des photos enregistrées dans la galerie). Cela est nécessaire lors de la sélection d'images existantes dans la galerie. Pour les versions plus récentes d'Android (Android 10+), le stockage scopé peut changer la manière dont cela fonctionne, mais pour la lecture de médias sélectionnés par l'utilisateur, cette déclaration est toujours pertinente. Pour l'écriture dans le stockage externe, `WRITE_EXTERNAL_STORAGE` serait également nécessaire.

### **Permissions iOS (dans `ios/Runner/Info.plist`)**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>io.flutter.embedded_views_preview</key>
		<true/>
	<key>NSSpeechRecognitionUsageDescription</key>
		<string>Nous avons besoin d'accéder à la reconnaissance vocale.</string>
	<key>NSCameraUsageDescription</key>
		<string>Cette application a besoin d'accéder à la caméra pour capturer des photos et des vidéos.</string>
	<key>NSMicrophoneUsageDescription</key>
		<string>Cette application a besoin d'accéder au microphone pour l'enregistrement audio.</string>
	<key>NSPhotoLibraryUsageDescription</key>
		<string>Cette application a besoin d'accéder à votre bibliothèque de photos.</string>
	<key>NSPhotoLibraryAddUsageDescription</key>
		<string>Cette application a besoin de la permission pour enregistrer des photos dans votre bibliothèque de photos.</string>
	<key>NSAppTransportSecurity</key>
		<dict>
			<key>NSAllowsArbitraryLoads</key>
			<true/>
		</dict>
</dict>
</plist>
```

Voici ce qui se passe :

Les permissions iOS sont déclarées dans le fichier `Info.plist` en utilisant des clés spécifiques (`NS...UsageDescription`) et nécessitent une chaîne orientée utilisateur expliquant pourquoi la permission est nécessaire. Cette chaîne est affichée à l'utilisateur lorsque l'application demande la permission.

* `<key>io.flutter.embedded_views_preview</key><true/>` : Cette clé est souvent ajoutée lors de l'utilisation de plugins Flutter qui intègrent des composants d'interface utilisateur natifs (par exemple, aperçus de caméra, webviews). Elle active un aperçu des vues natives intégrées pendant le développement.

* `<key>NSSpeechRecognitionUsageDescription</key><string>Nous avons besoin d'accéder à la reconnaissance vocale.</string>` : Il s'agit de la description de confidentialité pour les services de reconnaissance vocale (par exemple, le reconnaisseur vocal intégré d'Apple). Elle est cruciale pour les fonctionnalités comme l'entrée vocale.

* `<key>NSCameraUsageDescription</key><string>Cette application a besoin d'accéder à la caméra pour capturer des photos et des vidéos.</string>` : La description de confidentialité pour l'accès à la caméra. Cela est requis pour capturer des images via la caméra, comme utilisé dans la fonctionnalité de sélection d'images.

* `<key>NSMicrophoneUsageDescription</key><string>Cette application a besoin d'accéder au microphone pour l'enregistrement audio.</string>` : La description de confidentialité pour l'accès au microphone. Nécessaire pour enregistrer l'audio pour l'entrée vocale.

* `<key>NSPhotoLibraryUsageDescription</key><string>Cette application a besoin d'accéder à votre bibliothèque de photos.</string>` : La description de confidentialité pour la lecture à partir de la bibliothèque de photos de l'utilisateur. Cela est requis lors de la sélection d'images ou de vidéos existantes dans la galerie.

* `<key>NSPhotoLibraryAddUsageDescription</key><string>Cette application a besoin de la permission pour enregistrer des photos dans votre bibliothèque de photos.</string>` : La description de confidentialité pour l'écriture dans la bibliothèque de photos de l'utilisateur. Cela serait nécessaire si l'application capture des photos/vidéos et les enregistre directement dans la galerie de l'appareil.

* `<key>NSAppTransportSecurity</key><dict><key>NSAllowsArbitraryLoads</key><true/></dict>` : Cette section concerne la sécurité du transport des applications (ATS) d'Apple. Par défaut, ATS impose des connexions sécurisées (HTTPS). La définition de `NSAllowsArbitraryLoads` sur `true` (comme montré ici) *désactive* cette application, permettant à l'application de faire des connexions HTTP non sécurisées. Bien que cela soit utile pendant le développement ou pour interagir avec des API spécifiques héritées, il est généralement **non recommandé pour les applications de production** en raison des implications de sécurité. Pour la production, vous devriez idéalement configurer des exceptions spécifiques ou vous assurer que toutes les requêtes réseau utilisent HTTPS.

## **Ressources : Gérer les ressources de l'application**

Les ressources sont des fichiers regroupés avec votre application et accessibles à l'exécution. Cela inclut généralement des images, des polices, des fichiers audio, et plus encore.

Dans cette application, nous avons un dossier `assets`, et à l'intérieur, un sous-dossier `images`.

```dart
assets/
[2514][2500][2500] images/
    [251c][2500][2500] placeholder.png
    [2514][2500][2500] app_logo.png
```

* `placeholder.png` : Cette image est généralement utilisée comme un indice visuel temporaire lorsque le contenu réel (comme une image en cours de chargement ou sélectionnée) n'est pas encore disponible. Elle offre une meilleure expérience utilisateur qu'un espace vide.

* `app_logo.png` : Il s'agit du logo principal de l'application. Il est utilisé à diverses fins, y compris l'icône de l'application et l'écran de démarrage.

Pour vous assurer que Flutter connaît ces ressources et les regroupe avec l'application, vous devez les déclarer dans votre fichier `pubspec.yaml` :

```yaml
flutter:
  uses-material-design: true
  assets:
    - assets/images/ # Cette ligne indique à Flutter d'inclure tous les fichiers dans le répertoire assets/images/
```

## **Icônes de l'application : Personnaliser l'identité de votre application**

Les applications Flutter utilisent le package `flutter_launcher_icons` pour simplifier le processus de génération des icônes de lancement pour différentes plateformes et résolutions. Cela garantit que votre application a une apparence cohérente et professionnelle sur les appareils Android et iOS.

### Configuration de `pubspec.yaml` pour `flutter_launcher_icons`

```yaml
flutter_icons:
  android: "launcher_icon"
  ios: true
  image_path: "assets/images/app_logo.png"
  remove_alpha_ios: true
  adaptive_icon_background: "#FFFFFF"
  adaptive_icon_foreground: "assets/images/app_logo.png"
```

Voici ce qui se passe :

* `flutter_icons:` : Il s'agit de la clé racine pour la configuration du package `flutter_launcher_icons`.

* `android: "launcher_icon"` : Spécifie que les icônes de lancement Android doivent être générées. `"launcher_icon"` est la valeur par défaut et généralement suffisante.

* `ios: true` : Active la génération des icônes de l'application iOS.

* `image_path: "assets/images/app_logo.png"` : Il s'agit du chemin absolu vers votre fichier image source qui sera utilisé pour générer les icônes. Il est crucial que ce chemin soit correct et pointe vers une image carrée haute résolution.

* `remove_alpha_ios: true` : Pour iOS, cette option supprime le canal alpha de l'icône. Les icônes iOS n'utilisent généralement pas de canal alpha pour la transparence.

* `adaptive_icon_background: "#FFFFFF"` : Cela est spécifique aux icônes adaptatives Android (introduites dans Android 8.0 Oreo). Il définit la couche d'arrière-plan de l'icône adaptative. Ici, elle est définie en blanc (`#FFFFFF`).

* `adaptive_icon_foreground: "assets/images/app_logo.png"` : Cela définit la couche de premier plan de l'icône adaptative. Elle utilise à nouveau `app_logo.png`, qui sera masquée et mise à l'échelle par le système Android.

### **Génération des icônes de l'application**

Après avoir configuré `pubspec.yaml`, vous devez exécuter les commandes suivantes dans votre terminal :

Tout d'abord, exécutez `dart run flutter_launcher_icons:generate`. Cette commande génère un fichier de configuration (souvent nommé `flutter_launcher_icons.yaml` ou similaire, ou traite directement le `pubspec.yaml`) que `flutter_launcher_icons` utilise.

*Correction* : La prompt mentionne "générer un fichier de config et configurer le chemin de l'image vers le chemin de l'app_logo.png puis exécuter dart run flutter_launcher_icons pour générer les assets". Il semble que `flutter_launcher_icons:generate` soit une commande plus ancienne ou spécifique, l'utilisation typique est d'exécuter `flutter_launcher_icons` directement après avoir défini `image_path` dans `pubspec.yaml`. Pour la configuration donnée, le `image_path` est déjà défini dans `pubspec.yaml`.

Ensuite, exécutez `dart run flutter_launcher_icons`. Cette commande exécute le package `flutter_launcher_icons`, qui prend le `image_path` spécifié dans `pubspec.yaml` et génère tous les fichiers d'icônes nécessaires à diverses résolutions pour Android et iOS, les plaçant dans les répertoires de projet natifs corrects.

## **Écran de démarrage : La première impression**

Un écran de démarrage (ou écran de lancement) est le premier écran que les utilisateurs voient lorsqu'ils ouvrent votre application. Il offre une expérience de marque pendant que l'application initialise les ressources. Le package `flutter_native_splash` simplifie la création d'écrans de démarrage natifs pour les applications Flutter.

### Configuration de `pubspec.yaml` pour `flutter_native_splash`

```yaml
flutter_native_splash:
  color: "#FFFFFF"
  image: assets/images/app_logo.png
  android: true
  android_gravity: center
  fullscreen: true
  ios: true
```

Voici ce qui se passe :

* `flutter_native_splash:` : La clé racine pour la configuration du package `flutter_native_splash`.

* `color: "#FFFFFF"` : Définit la couleur de fond de l'écran de démarrage. Ici, elle est définie en blanc.

* `image: assets/images/app_logo.png` : Spécifie le chemin vers l'image qui sera affichée sur l'écran de démarrage. Dans ce cas, il s'agit du logo de l'application.

* `android: true` : Active la génération de l'écran de démarrage pour Android.

* `android_gravity: center` : Pour Android, cela centre l'image de démarrage sur l'écran.

* `fullscreen: true` : Rend l'écran de démarrage en mode plein écran, sans barres d'état ou de navigation.

* `ios: true` : Active la génération de l'écran de démarrage pour iOS.

### **Génération de l'écran de démarrage**

Après avoir configuré `pubspec.yaml`, exécutez la commande suivante dans votre terminal : `dart run flutter_native_splash:create`. Il traite la configuration et génère les fichiers d'écran de démarrage natifs (par exemple, les images de lancement, les drawables) dans les dossiers de projet Android et iOS respectifs, en veillant à ce qu'ils soient correctement intégrés dans le processus de lancement natif.

## **Captures d'écran de l'application**

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1748068995235/d84ad92d-a686-43ee-a34c-89f2d6bf7e17.png align="center")

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1748069008469/f5fecee8-93dd-46ef-92ae-bd8c5413b3a7.png align="center")

Gardez à l'esprit que la qualité de sortie peut varier en fonction du modèle d'IA que vous utilisez. Il en va de même pour les liens YouTube et les URL d'images – parfois ils fonctionnent parfaitement, et d'autres fois, ils peuvent ne pas fonctionner. Donc, si quelque chose ne fonctionne pas comme prévu, ce n'est pas nécessairement de votre côté.

De plus, rappelez-vous qu'il existe de nombreuses façons d'y parvenir et que vous n'avez pas nécessairement besoin d'utiliser cette méthode. Je fournirai ci-dessous d'autres ressources que vous pouvez consulter. Vous pouvez utiliser `systemInstructions` au lieu de définir des contraintes dans le texte comme je l'ai fait.

**Voici le projet terminé :** [https://github.com/Atuoha/snap2chef_ai](https://github.com/Atuoha/snap2chef_ai)

## Conclusion

J'espère que cette analyse complète vous a donné une compréhension claire de la structure de l'application "Snap2Chef", de ses composants d'interface utilisateur et de ses configurations sous-jacentes. Que votre parcours de codage soit rempli de créativité et de mises en œuvre réussies.

Bon codage !

## Références

Voici quelques références pour les technologies et packages clés utilisés dans cette application :

### Packages Flutter

* `flutter/material.dart` : Le package principal de Flutter pour le design Material.

* **Référence :** [Flutter API Docs - bibliothèque material](https://api.flutter.dev/flutter/material/material-library.html)

* `iconsax/iconsax.dart` : Un ensemble d'icônes personnalisées pour Flutter.

* **Référence :** [pub.dev - iconsax](https://www.google.com/search?q=https://pub.dev/packages/iconsax)

* `gap/gap.dart` : Un package simple pour ajouter de l'espace entre les widgets.

* **Référence :** [pub.dev - gap](https://pub.dev/packages/gap)

* `dotted_border/dotted_border.dart` : Un package Flutter pour dessiner une bordure pointillée autour de n'importe quel widget.

* **Référence :** [pub.dev - dotted_border](https://pub.dev/packages/dotted_border)

* `flutter/cupertino.dart` : Le package principal des widgets Flutter de style Cupertino (iOS).

* **Référence :** [Flutter API Docs - bibliothèque cupertino](https://api.flutter.dev/flutter/cupertino/cupertino-library.html)

* `flutter_launcher_icons` : Un package pour générer des icônes de lancement d'application.

* **Référence :** [pub.dev - flutter_launcher_icons](https://pub.dev/packages/flutter_launcher_icons)

* `flutter_native_splash` : Un package pour générer des écrans de démarrage natifs.

* **Référence :** [pub.dev - flutter_native_splash](https://pub.dev/packages/flutter_native_splash)

* `image_picker` (utilisé implicitement par `ImageUploadController`) : Un plugin Flutter pour sélectionner des images dans la bibliothèque d'images ou prendre de nouvelles photos avec la caméra. (Bien que non directement importé dans les extraits fournis, `ImageUploadController` utilise probablement celui-ci ou un package similaire).

* **Référence :** [pub.dev - image_picker](https://pub.dev/packages/image_picker)

* `image_cropper` (utilisé implicitement par `ImageUploadController`) : Un plugin Flutter pour rogner des images. (Probablement utilisé en conjonction avec `image_picker` pour `assignCroppedImage`).

* **Référence :** [pub.dev - image_cropper](https://pub.dev/packages/image_cropper)

### **APIs et Plateformes**

* **API Gemini** : La famille de modèles d'IA générative de Google.

* **Référence :** [Google AI Gemini API](https://www.google.com/search?q=https://ai.google.dev/gemini)

* **Documentation :** [Google Cloud - Documentation de l'API Gemini](https://cloud.google.com/gemini/docs)

* **Firebase** : La plateforme de développement d'applications complète de Google.

* **Référence :** [Site officiel de Firebase](https://firebase.google.com/)

* **Documentation :** [Documentation de Firebase](https://firebase.google.com/docs)

* **Console/Studio Firebase** : L'interface web pour gérer les projets Firebase.

* **Vertex AI** : La plateforme d'apprentissage automatique de Google Cloud.

* **Référence :** [Google Cloud - Vertex AI](https://cloud.google.com/vertex-ai)

* **Documentation :** [Google Cloud - Documentation de Vertex AI](https://cloud.google.com/vertex-ai/docs)