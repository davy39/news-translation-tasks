---
title: How to Manage Assets in Flutter using  flutter_gen
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
seo_title: null
seo_desc: 'Managing assets like images, icons, and fonts in a Flutter project can
  quickly become a tedious task, especially as your application grows. Manual referencing
  is prone to typos, introduces maintenance overhead, and can hinder team collaboration.

  Fort...'
---

Managing assets like images, icons, and fonts in a Flutter project can quickly become a tedious task, especially as your application grows. Manual referencing is prone to typos, introduces maintenance overhead, and can hinder team collaboration.

Fortunately, the `flutter_gen` package provides an elegant solution by automating asset generation, bringing type safety and a streamlined workflow to your development process.

This comprehensive guide will walk you through setting up a Flutter project with `flutter_gen`, explaining each step and code block in detail so you can effortlessly integrate this powerful tool into your projects.

### Table of Contents

1. [Prerequisites](#heading-prerequisites)
    
2. [Why flutter\_gen? The Advantages of Automated Asset Management](#heading-why-fluttergen-the-advantages-of-automated-asset-management)
    
3. [Step-by-Step Implementation Guide](#heading-step-by-step-implementation-guide)
    
    * [1\. Project Setup](#heading-1-project-setup)
        
    * [2\. Organize Your Assets](#heading-2-organize-your-assets)
        
    * [3\. Run Code Generation](#heading-3-run-code-generation)
        
    * [4\. Explore the Generated Files](#heading-4-explore-the-generated-files)
        
    * [5\. Using Generated Assets in Your Code](#heading-5-using-generated-assets-in-your-code)
        
    * [Running Your Application](#heading-running-your-application)
        
4. [Important Considerations](#heading-important-considerations)
    
5. [Further Reading](#heading-further-reading)
    
6. [Conclusion](#heading-conclusion)
    

## Prerequisites

Before you begin, make sure you have the following installed:

1. **Flutter SDK:** you should have the latest stable version of Flutter installed and configured. You can check your installation with `flutter --version`.
    
2. **A code editor:** Visual Studio Code with the Flutter extension is highly recommended, but any suitable IDE will work.
    

## Why `flutter_gen`? The Advantages of Automated Asset Management

`flutter_gen` offers many benefits that can significantly improve your asset management experience in Flutter:

1. **Type safety:** This is perhaps the most significant advantage. Instead of fragile string paths, `flutter_gen` creates strongly-typed classes for each asset type (images, icons, fonts). This eliminates runtime errors caused by typos and provides excellent code completion in your IDE, making asset discovery a breeze.  
    **Reduced errors:** Manual asset path management is a common source of bugs. `flutter_gen` ensures that your asset references are always accurate and up-to-date, drastically reducing the likelihood of runtime errors related to incorrect paths.
    
2. **Improved code maintainability:** As your project scales, finding and updating assets can become a nightmare. The generated asset classes serve as a centralized, navigable reference point, making it effortless to locate and modify assets without sifting through countless files.
    
3. **Enhanced collaboration:** In a team environment, `flutter_gen` streamlines collaboration. Team members can intuitively discover and use assets through code completion, minimizing communication overhead related to asset paths and ensuring consistency across the codebase.
    

## Step-by-Step Implementation Guide

Let's dive into setting up your Flutter project with `flutter_gen`.

### 1\. Project Setup

#### Create a new Flutter project:

Start by creating a fresh Flutter project. Open your terminal or command prompt and run:

```bash
flutter create flutter_auto_assets
cd flutter_auto_assets
```

This command creates a new Flutter project named `flutter_auto_assets` and navigates you into its directory.

#### Add Dependencies:

Open the `pubspec.yaml` file located at the root of your project. This file manages your project's dependencies and assets. Add the `flutter_gen` and `flutter_gen_runner` packages, along with `build_runner`, to your `pubspec.yaml` as shown below:

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

Explanation of the `pubspec.yaml` additions:

1. `dependencies` section: `flutter_gen: ^5.12.0`: This is the main package that provides the generated asset classes for your Flutter application.
    
2. `dev_dependencies` section:
    
    * `build_runner: ^2.4.13`: `build_runner` is a powerful package that provides a concrete way of generating files in a Flutter project. `flutter_gen_runner` uses `build_runner` to execute its code generation logic.
        
    * `flutter_gen_runner: ^5.12.0`: This package contains the actual code generator that scans your `pubspec.yaml` and asset folders to create the type-safe asset references.
        
3. `flutter` section:
    
    * `assets:`: This section is crucial for telling Flutter which directories contain your assets. We've listed `assets/`, `assets/images/`, and `assets/icons/` to ensure all assets within these folders are bundled with your application.
        
    * `fonts:`: This section declares your custom fonts. Here, we've registered the `Roboto` font family, specifying the path to `Roboto-Regular.ttf`.
        

### 2\. Organize Your Assets

Create the below folder structure within your project's root directory. This organization helps keep your assets tidy and easily discoverable.

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

A few things to note here:

* **Configure Fonts:** Place your font files (for example, `Roboto-Regular.ttf`) inside the `assets/fonts/` folder.
    
* **Configure Icons:** Place your icon files (for example, `file_add.png`) inside the `assets/icons/` folder.
    
* **Configure Images:** Place your image files (for example, `img.png`) inside the `assets/images/` folder.
    

### 3\. Run Code Generation

Now it's time to generate the type-safe asset classes. Open your terminal in the project's root directory and execute the following commands:

```bash
flutter pub get
flutter pub run build_runner build
```

Here’s what these commands are doing:

1. `flutter pub get`: fetches all the packages declared in your `pubspec.yaml` file, including `flutter_gen`, `build_runner`, and `flutter_gen_runner`.
    
2. `flutter pub run build_runner build`: invokes `build_runner`, which in turn triggers `flutter_gen_runner`. The runner will scan your `pubspec.yaml` and the `assets/` directory, then generate the necessary Dart files containing your type-safe asset references.
    

After running these commands, you should see a new folder named `gen` created inside your `lib` directory. This `gen` folder will contain `assets.gen.dart` and `fonts.gen.dart`.

### 4\. Explore the Generated Files

Let's take a look at the files `flutter_gen` creates for you.

`fonts.gen.dart`: This file contains the auto-generated font family class, providing a type-safe way to reference your custom fonts.

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

Here, a `FontFamily` class is generated and for each font family declared in your `pubspec.yaml` (for example, `Roboto`), and a static constant string field is created (for example, `roboto`). This allows you to reference your font family like `FontFamily.roboto`, ensuring correctness.

`assets.gen.dart`: This file contains the auto-generated classes for your image and icon assets.

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

In this code,

1. `$AssetsIconsGen` and `$AssetsImagesGen`: These classes represent your icon and image directories, respectively. Each asset within these directories gets a getter (for example, `fileAdd`, `img`) that returns an `AssetGenImage` object.
    
2. `Assets` class: This is the main entry point for accessing all your generated assets. It provides static instances of `$AssetsIconsGen` and `$AssetsImagesGen` (for example, `Assets.icons`, `Assets.images`).
    
3. `AssetGenImage` class: This utility class wraps the asset path and provides convenience methods like `image()` to directly create an `Image` widget and `provider()` to get an `ImageProvider`. The `path` getter provides the raw asset path if needed.
    

### 5\. Using Generated Assets in Your Code

Now that your assets are type-safe and easily accessible, let's integrate them into your Flutter application.

First, create a `screens` folder inside your `lib` directory. Then, create a new file named `entry_screen.dart` inside the `lib/screens` folder and paste the following code:

`lib/screens/entry_screen.dart`:

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

What’s going on in `entry_screen.dart`:

1. `import '../gen/assets.gen.dart';`: This line imports the generated `assets.gen.dart` file, making all your type-safe image and icon assets available.
    
2. `Image.asset(Assets.images.img.path)`: Instead of a hardcoded string like `Image.asset('assets/images/img.png')`, we now use `Assets.images.img.path`. This is type-safe and benefits from IDE autocomplete, preventing errors and improving readability.
    
3. `Image.asset(Assets.icons.fileAdd.path)`: Similarly, icons are accessed through `Assets.icons.fileAdd.path`.
    

Next, modify your `main.dart` file to use the `EntryScreen` and the generated font.

`lib/main.dart`:

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

In `main.dart`:

1. `import 'gen/fonts.gen.dart';`: This imports the generated `fonts.gen.dart` file, giving you access to the `FontFamily` class.
    
2. `theme: ThemeData(fontFamily: FontFamily.roboto)`: Here, we're applying the `Roboto` font family to our entire `MaterialApp` theme using `FontFamily.roboto`. This is a type-safe way to reference your custom font.
    

### Running Your Application

Save all your changes and run your Flutter application:

```bash
flutter run
```

You should see your application launch, displaying the image and icon, all managed efficiently and type-safely by `flutter_gen`.

![Application launched](https://cdn.hashnode.com/res/hashnode/image/upload/v1702275921470/244c906f-2a2a-4630-b3a4-89d2455a95fe.png align="center")

## Important Considerations

There are a couple things to note here:

1. Whenever you add, remove, or rename assets in your `assets/` folders, or modify the asset declarations in `pubspec.yaml`, you *must* rerun the code generation commands:
    
    ```bash
    flutter pub get
    flutter pub run build_runner build
    ```
    
2. For a more seamless experience, you can use the `watch` command with `build_runner`. This will automatically regenerate your asset files whenever changes are detected:
    
    ```bash
    flutter pub run build_runner watch
    ```
    
    Keep this command running in a separate terminal window during development.
    

## Conclusion

By integrating `flutter_gen` into your Flutter workflow, you unlock a superior asset management experience characterized by type safety, reduced errors, improved maintainability, and enhanced collaboration.

This guide has provided you with a solid foundation to leverage this powerful package effectively, making your Flutter development journey smoother and more robust.

### Further Reading

To explore more advanced configurations and features of `flutter_gen`, refer to the [official `flutter_gen` package documentation page](https://pub.dev/packages/flutter_gen).
