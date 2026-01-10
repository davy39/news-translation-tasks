---
title: Comment gérer les assets dans Flutter avec flutter_gen
subtitle: ''
author: Atuoha Anthony
co_authors: []
series: null
date: '2025-10-28T20:47:49.798Z'
originalURL: https://freecodecamp.org/news/how-to-manage-assets-in-flutter-using-fluttergen
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1761684457969/a8a6b9bc-780f-4e06-bf8a-19b90cd632f4.png
tags:
- name: Flutter
  slug: flutter
- name: Dart
  slug: dart
- name: flutter-aware
  slug: flutter-aware
- name: asset management
  slug: asset-management
seo_title: Comment gérer les assets dans Flutter avec flutter_gen
seo_desc: 'Managing assets like images, icons, and fonts in a Flutter project can
  quickly become a tedious task, especially as your application grows. Manual referencing
  is prone to typos, introduces maintenance overhead, and can hinder team collaboration.

  Fort...'
---

La gestion des assets tels que les images, les icônes et les polices dans un projet Flutter peut rapidement devenir une tâche fastidieuse, surtout à mesure que votre application grandit. Le référencement manuel est sujet aux fautes de frappe, introduit des coûts de maintenance et peut entraver la collaboration au sein de l'équipe.

Heureusement, le package `flutter_gen` offre une solution élégante en automatisant la génération d'assets, apportant une sécurité de typage (type safety) et un flux de travail rationalisé à votre processus de développement.

Ce guide complet vous accompagnera dans la configuration d'un projet Flutter avec `flutter_gen`, en expliquant chaque étape et bloc de code en détail afin que vous puissiez intégrer sans effort cet outil puissant dans vos projets.

### Table des matières

1. [Prérequis](#heading-prerequis)
    
2. [Pourquoi flutter\_gen ? Les avantages de la gestion automatisée des assets](#heading-pourquoi-fluttergen-les-avantages-de-la-gestion-automatisee-des-assets)
    
3. [Guide d'implémentation étape par étape](#heading-guide-dimplementation-etape-par-etape)
    
    * [1\. Configuration du projet](#heading-1-configuration-du-projet)
        
    * [2\. Organisez vos assets](#heading-2-organisez-vos-assets)
        
    * [3\. Exécuter la génération de code](#heading-3-executer-la-generation-de-code)
        
    * [4\. Explorer les fichiers générés](#heading-4-explorer-les-fichiers-generes)
        
    * [5\. Utiliser les assets générés dans votre code](#heading-5-utiliser-les-assets-generes-dans-votre-code)
        
    * [Exécuter votre application](#heading-executer-votre-application)
        
4. [Considérations importantes](#heading-considerations-importantes)
    
5. [Lectures complémentaires](#heading-lectures-complementaires)
    
6. [Conclusion](#heading-conclusion)
    

## Prérequis

Avant de commencer, assurez-vous d'avoir installé les éléments suivants :

1. **SDK Flutter :** vous devez avoir la dernière version stable de Flutter installée et configurée. Vous pouvez vérifier votre installation avec `flutter --version`.
    
2. **Un éditeur de code :** Visual Studio Code avec l'extension Flutter est fortement recommandé, mais n'importe quel IDE approprié fera l'affaire.
    

## Pourquoi `flutter_gen` ? Les avantages de la gestion automatisée des assets

`flutter_gen` offre de nombreux avantages qui peuvent considérablement améliorer votre expérience de gestion des assets dans Flutter :

1. **Sécurité de typage (Type safety) :** C'est peut-être l'avantage le plus significatif. Au lieu de chemins de chaînes de caractères fragiles, `flutter_gen` crée des classes fortement typées pour chaque type d'asset (images, icônes, polices). Cela élimine les erreurs d'exécution causées par des fautes de frappe et fournit une excellente complétion de code dans votre IDE, facilitant la découverte des assets.
    **Réduction des erreurs :** La gestion manuelle des chemins d'assets est une source courante de bugs. `flutter_gen` garantit que vos références d'assets sont toujours précises et à jour, réduisant considérablement la probabilité d'erreurs d'exécution liées à des chemins incorrects.
    
2. **Amélioration de la maintenabilité du code :** À mesure que votre projet évolue, trouver et mettre à jour les assets peut devenir un cauchemar. Les classes d'assets générées servent de point de référence centralisé et navigable, ce qui permet de localiser et de modifier les assets sans effort, sans avoir à passer au crible d'innombrables fichiers.
    
3. **Collaboration renforcée :** Dans un environnement d'équipe, `flutter_gen` rationalise la collaboration. Les membres de l'équipe peuvent découvrir et utiliser intuitivement les assets grâce à la complétion de code, minimisant ainsi les échanges liés aux chemins d'assets et assurant la cohérence dans toute la base de code.
    

## Guide d'implémentation étape par étape

Plongeons dans la configuration de votre projet Flutter avec `flutter_gen`.

### 1\. Configuration du projet

#### Créer un nouveau projet Flutter :

Commencez par créer un nouveau projet Flutter. Ouvrez votre terminal ou invite de commande et exécutez :

```bash
flutter create flutter_auto_assets
cd flutter_auto_assets
```

Cette commande crée un nouveau projet Flutter nommé `flutter_auto_assets` et vous dirige vers son répertoire.

#### Ajouter les dépendances :

Ouvrez le fichier `pubspec.yaml` situé à la racine de votre projet. Ce fichier gère les dépendances et les assets de votre projet. Ajoutez les packages `flutter_gen` et `flutter_gen_runner`, ainsi que `build_runner`, à votre `pubspec.yaml` comme indiqué ci-dessous :

```yaml
name: flutter_auto_assets
description: A flutter app demonstrating asset auto generation
publish_to: 'none' # Remove this line if you wish to publish to pub.dev

version: 1.0.0+1

environment:
  sdk: ^3.8.0

dependencies:
  flutter:
    sdk: flutter
  cupertino_icons: ^1.0.8
  flutter_gen: ^5.12.0 # Add flutter_gen here

dev_dependencies:
  flutter_test:
    sdk: flutter
  build_runner: ^2.4.13 # Add build_runner here
  flutter_gen_runner: ^5.12.0 # Add flutter_gen_runner here

flutter:
  uses-material-design: true
  assets:
    - assets/
    - assets/images/
    - assets/icons/

  fonts:
    - family: Roboto
      fonts:
        - asset: assets/fonts/Roboto-Regular.ttf
```

Explication des ajouts au `pubspec.yaml` :

1. Section `dependencies` : `flutter_gen: ^5.12.0` : C'est le package principal qui fournit les classes d'assets générées pour votre application Flutter.
    
2. Section `dev_dependencies` :
    
    * `build_runner: ^2.4.13` : `build_runner` est un package puissant qui offre un moyen concret de générer des fichiers dans un projet Flutter. `flutter_gen_runner` utilise `build_runner` pour exécuter sa logique de génération de code.
        
    * `flutter_gen_runner: ^5.12.0` : Ce package contient le générateur de code réel qui scanne votre `pubspec.yaml` et vos dossiers d'assets pour créer les références d'assets typées.
        
3. Section `flutter` :
    
    * `assets:` : Cette section est cruciale pour indiquer à Flutter quels répertoires contiennent vos assets. Nous avons listé `assets/`, `assets/images/` et `assets/icons/` pour nous assurer que tous les assets de ces dossiers sont inclus dans votre application.
        
    * `fonts:` : Cette section déclare vos polices personnalisées. Ici, nous avons enregistré la famille de polices `Roboto`, en spécifiant le chemin vers `Roboto-Regular.ttf`.
        

### 2\. Organisez vos assets

Créez la structure de dossiers ci-dessous à la racine de votre projet. Cette organisation aide à garder vos assets ordonnés et facilement accessibles.

```dart
flutter_auto_assets/
├── assets/
│   ├── fonts/
│   │   └── Roboto-Regular.ttf
│   ├── icons/
│   │   └── file_add.png
│   └── images/
│       └── img.png
├── lib/
│   └── main.dart
└── pubspec.yaml
```

Quelques points à noter ici :

* **Configurer les polices :** Placez vos fichiers de police (par exemple, `Roboto-Regular.ttf`) dans le dossier `assets/fonts/`.
    
* **Configurer les icônes :** Placez vos fichiers d'icônes (par exemple, `file_add.png`) dans le dossier `assets/icons/`.
    
* **Configurer les images :** Placez vos fichiers d'images (par exemple, `img.png`) dans le dossier `assets/images/`.
    

### 3\. Exécuter la génération de code

Il est maintenant temps de générer les classes d'assets typées. Ouvrez votre terminal dans le répertoire racine du projet et exécutez les commandes suivantes :

```bash
flutter pub get
flutter pub run build_runner build
```

Voici ce que font ces commandes :

1. `flutter pub get` : récupère tous les packages déclarés dans votre fichier `pubspec.yaml`, y compris `flutter_gen`, `build_runner` et `flutter_gen_runner`.
    
2. `flutter pub run build_runner build` : invoque `build_runner`, qui à son tour déclenche `flutter_gen_runner`. Le runner scannera votre `pubspec.yaml` et le répertoire `assets/`, puis générera les fichiers Dart nécessaires contenant vos références d'assets typées.
    

Après avoir exécuté ces commandes, vous devriez voir un nouveau dossier nommé `gen` créé à l'intérieur de votre répertoire `lib`. Ce dossier `gen` contiendra `assets.gen.dart` et `fonts.gen.dart`.

### 4\. Explorer les fichiers générés

Jetons un coup d'œil aux fichiers que `flutter_gen` crée pour vous.

`fonts.gen.dart` : Ce fichier contient la classe de famille de polices auto-générée, offrant un moyen typé de référencer vos polices personnalisées.

```dart
/// GENERATED CODE - DO NOT MODIFY BY HAND
/// *****************************************************
///  FlutterGen
/// *****************************************************

// coverage:ignore-file
// ignore_for_file: type=lint
// ignore_for_file: directives_ordering,unnecessary_import,implicit_dynamic_list_literal,deprecated_member_use

class FontFamily {
  FontFamily._();

  static const String roboto = 'Roboto';
}
```

Ici, une classe `FontFamily` est générée et pour chaque famille de polices déclarée dans votre `pubspec.yaml` (par exemple, `Roboto`), un champ de chaîne constante statique est créé (par exemple, `roboto`). Cela vous permet de référencer votre famille de polices comme `FontFamily.roboto`, garantissant l'exactitude.

`assets.gen.dart` : Ce fichier contient les classes auto-générées pour vos assets d'images et d'icônes.

```dart
/// GENERATED CODE - DO NOT MODIFY BY HAND
/// *****************************************************
///  FlutterGen
/// *****************************************************

// coverage:ignore-file
// ignore_for_file: type=lint
// ignore_for_file: directives_ordering,unnecessary_import,implicit_dynamic_list_literal,deprecated_member_use

import 'package:flutter/widgets.dart';

class $AssetsIconsGen {
  const $AssetsIconsGen();

  /// File path: assets/icons/file_add.png
  AssetGenImage get fileAdd => const AssetGenImage('assets/icons/file_add.png');

  /// List of all assets
  List<AssetGenImage> get values => [fileAdd];
}

class $AssetsImagesGen {
  const $AssetsImagesGen();

  /// File path: assets/images/img.png
  AssetGenImage get img => const AssetGenImage('assets/images/img.png');

  /// List of all assets
  List<AssetGenImage> get values => [img];
}

class Assets {
  Assets._();

  static const $AssetsIconsGen icons = $AssetsIconsGen();
  static const $AssetsImagesGen images = $AssetsImagesGen();
}

class AssetGenImage {
  const AssetGenImage(this._assetName);

  final String _assetName;

  Image image({
    Key? key,
    AssetBundle? bundle,
    ImageFrameBuilder? frameBuilder,
    ImageErrorWidgetBuilder? errorBuilder,
    String? semanticLabel,
    bool excludeFromSemantics = false,
    double? scale,
    double? width,
    double? height,
    Color? color,
    Animation<double>? opacity,
    BlendMode? colorBlendMode,
    BoxFit? fit,
    AlignmentGeometry alignment = Alignment.center,
    ImageRepeat repeat = ImageRepeat.noRepeat,
    Rect? centerSlice,
    bool matchTextDirection = false,
    bool gaplessPlayback = false,
    bool isAntiAlias = false,
    String? package,
    FilterQuality filterQuality = FilterQuality.low,
    int? cacheWidth,
    int? cacheHeight,
  }) {
    return Image.asset(
      _assetName,
      key: key,
      bundle: bundle,
      frameBuilder: frameBuilder,
      errorBuilder: errorBuilder,
      semanticLabel: semanticLabel,
      excludeFromSemantics: excludeFromSemantics,
      scale: scale,
      width: width,
      height: height,
      color: color,
      opacity: opacity,
      colorBlendMode: colorBlendMode,
      fit: fit,
      alignment: alignment,
      repeat: repeat,
      centerSlice: centerSlice,
      matchTextDirection: matchTextDirection,
      gaplessPlayback: gaplessPlayback,
      isAntiAlias: isAntiAlias,
      package: package,
      filterQuality: filterQuality,
      cacheWidth: cacheWidth,
      cacheHeight: cacheHeight,
    );
  }

  ImageProvider provider({
    AssetBundle? bundle,
    String? package,
  }) {
    return AssetImage(
      _assetName,
      bundle: bundle,
      package: package,
    );
  }

  String get path => _assetName;

  String get keyName => _assetName;
}
```

Dans ce code,

1. `$AssetsIconsGen` et `$AssetsImagesGen` : Ces classes représentent respectivement vos répertoires d'icônes et d'images. Chaque asset au sein de ces répertoires obtient un getter (par exemple, `fileAdd`, `img`) qui renvoie un objet `AssetGenImage`.
    
2. Classe `Assets` : C'est le point d'entrée principal pour accéder à tous vos assets générés. Elle fournit des instances statiques de `$AssetsIconsGen` et `$AssetsImagesGen` (par exemple, `Assets.icons`, `Assets.images`).
    
3. Classe `AssetGenImage` : Cette classe utilitaire enveloppe le chemin de l'asset et fournit des méthodes pratiques comme `image()` pour créer directement un widget `Image` et `provider()` pour obtenir un `ImageProvider`. Le getter `path` fournit le chemin brut de l'asset si nécessaire.
    

### 5\. Utiliser les assets générés dans votre code

Maintenant que vos assets sont typés et facilement accessibles, intégrons-les dans votre application Flutter.

Tout d'abord, créez un dossier `screens` à l'intérieur de votre répertoire `lib`. Ensuite, créez un nouveau fichier nommé `entry_screen.dart` dans le dossier `lib/screens` et collez le code suivant :

`lib/screens/entry_screen.dart` :

```dart
import 'package:flutter/material.dart';
import '../gen/assets.gen.dart'; // Import the generated assets file

class EntryScreen extends StatelessWidget {
  const EntryScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            // Using a generated Image asset
            Image.asset(Assets.images.img.path), // Access the image using Assets.images.img.path
            const SizedBox(height: 10),
            const Text(
              'Flutter Gen Assets',
              style: TextStyle(
                fontWeight: FontWeight.bold,
                fontSize: 18,
              ),
            ),
            const SizedBox(height: 10),

            // Using a generated Icon asset
            Image.asset(Assets.icons.fileAdd.path), // Access the icon using Assets.icons.fileAdd.path
          ],
        ),
      ),
    );
  }
}
```

Ce qui se passe dans `entry_screen.dart` :

1. `import '../gen/assets.gen.dart';` : Cette ligne importe le fichier `assets.gen.dart` généré, rendant tous vos assets d'images et d'icônes typés disponibles.
    
2. `Image.asset(Assets.images.img.path)` : Au lieu d'une chaîne codée en dur comme `Image.asset('assets/images/img.png')`, nous utilisons maintenant `Assets.images.img.path`. C'est typé et bénéficie de l'autocomplétion de l'IDE, évitant les erreurs et améliorant la lisibilité.
    
3. `Image.asset(Assets.icons.fileAdd.path)` : De même, les icônes sont accessibles via `Assets.icons.fileAdd.path`.
    

Ensuite, modifiez votre fichier `main.dart` pour utiliser l'écran `EntryScreen` et la police générée.

`lib/main.dart` :

```dart
import 'gen/fonts.gen.dart'; // Import the generated fonts file
import 'screens/entry_screen.dart';
import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return  MaterialApp(
      // Using generated Font asset
      theme: ThemeData(fontFamily: FontFamily.roboto), // Apply the Roboto font family using FontFamily.roboto
      debugShowCheckedModeBanner: false,
      home: const EntryScreen(),
    );
  }
}
```

Dans `main.dart` :

1. `import 'gen/fonts.gen.dart';` : Ceci importe le fichier `fonts.gen.dart` généré, vous donnant accès à la classe `FontFamily`.
    
2. `theme: ThemeData(fontFamily: FontFamily.roboto)` : Ici, nous appliquons la famille de polices `Roboto` à l'ensemble du thème de notre `MaterialApp` en utilisant `FontFamily.roboto`. C'est un moyen typé de référencer votre police personnalisée.
    

### Exécuter votre application

Enregistrez toutes vos modifications et lancez votre application Flutter :

```bash
flutter run
```

Vous devriez voir votre application se lancer, affichant l'image et l'icône, le tout géré efficacement et de manière typée par `flutter_gen`.

![Application lancée](https://cdn.hashnode.com/res/hashnode/image/upload/v1702275921470/244c906f-2a2a-4630-b3a4-89d2455a95fe.png align="center")

## Considérations importantes

Il y a quelques points à noter ici :

1. Chaque fois que vous ajoutez, supprimez ou renommez des assets dans vos dossiers `assets/`, ou que vous modifiez les déclarations d'assets dans `pubspec.yaml`, vous *devez* réexécuter les commandes de génération de code :
    
    ```bash
    flutter pub get
    flutter pub run build_runner build
    ```
    
2. Pour une expérience plus fluide, vous pouvez utiliser la commande `watch` avec `build_runner`. Cela régénérera automatiquement vos fichiers d'assets chaque fois que des changements sont détectés :
    
    ```bash
    flutter pub run build_runner watch
    ```
    
    Gardez cette commande en cours d'exécution dans une fenêtre de terminal séparée pendant le développement.
    

## Conclusion

En intégrant `flutter_gen` dans votre flux de travail Flutter, vous débloquez une expérience de gestion d'assets supérieure caractérisée par la sécurité de typage, la réduction des erreurs, une meilleure maintenabilité et une collaboration renforcée.

Ce guide vous a fourni une base solide pour exploiter efficacement ce package puissant, rendant votre parcours de développement Flutter plus fluide et plus robuste.

### Lectures complémentaires

Pour explorer des configurations et des fonctionnalités plus avancées de `flutter_gen`, reportez-vous à la [page de documentation officielle du package `flutter_gen`](https://pub.dev/packages/flutter_gen).