---
title: Comment ajouter des icônes personnalisées à votre application Flutter
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2022-01-27T20:54:03.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-custom-icons-to-your-flutter-application
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/harpal-singh-_zKxPsGOGKg-unsplash.jpg
tags:
- name: Flutter
  slug: flutter
- name: Icons
  slug: icons
- name: mobile app development
  slug: mobile-app-development
seo_title: Comment ajouter des icônes personnalisées à votre application Flutter
seo_desc: "When you want to add some style to your application, you likely look for\
  \ ways to make your User Interface stand out. \nWhether it is using a specific font\
  \ or a different color palate, you want to make the user feel attracted to your\
  \ UI. \nOne way to cu..."
---

Lorsque vous souhaitez ajouter du style à votre application, vous cherchez probablement des moyens de faire ressortir votre interface utilisateur.

Qu'il s'agisse d'utiliser une police spécifique ou une palette de couleurs différente, vous voulez que l'utilisateur soit attiré par votre interface utilisateur.

Une façon de personnaliser est de mettre à jour vos icônes. Si vous êtes un développeur mobile, quelle que soit la plateforme pour laquelle vous développez, il existe un processus simple pour ajouter des icônes à votre application.

Dans Flutter, ce n'est pas si compliqué, mais il y a certaines choses que vous devez savoir pour éviter des erreurs chronophages.

## Comment personnaliser l'icône de lancement de l'application

Au lieu d'utiliser l'icône d'application générique fournie par Flutter, vous pouvez créer la vôtre. Pour cela, nous allons utiliser un package appelé [Flutter Launcher Icons](https://pub.dev/packages/flutter_launcher_icons). Nous allons passer par la création étape par étape.

Voici à quoi ressemble votre icône de lancement par défaut :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/1_ZmZvjWFbQa-7TVOnln390w.jpeg)

Supposons que nous voulons que cette image soit notre icône de lancement d'application :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/1_G3Ro06E4rc6F30BC9n-OBw.png)

Tout d'abord, ajoutez l'image que vous souhaitez utiliser comme icône à l'intérieur de votre projet dans le dossier assets (si vous n'avez pas de dossier assets, créez-en un) :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/1_GeYlh_ryVgmJ-133XSEO0w.jpeg)
_Emplacement de notre icône à l'intérieur du projet_

Ensuite, ajoutez la dépendance à votre fichier pubspec.yaml sous **dev_dependencies** :

```yaml
dev_dependencies:
  flutter_launcher_icons: "^0.9.2"
```

Ajoutez cette configuration à l'intérieur de votre fichier pubspec.yaml :

```yaml
flutter_icons:
  android: "launcher_icon"
  ios: true
  image_path: "assets/doughnut.png"
```

La configuration `flutter_icons` possède plusieurs clés pour modifier ce qui va être rendu et pour quelle plateforme.

* Android/iOS – spécifiez pour quelle plateforme vous souhaitez générer une icône. Vous pouvez également écrire le nom du fichier au lieu de true.
* image_path – le chemin vers l'actif que vous souhaitez transformer en icône de lancement de l'application. Par exemple, **"assets/doughnut.png"**.

Il existe d'autres configurations disponibles, mais nous n'entrerons pas dans les détails ici. Vous pouvez en savoir plus en allant [ici](https://github.com/fluttercommunity/flutter_launcher_icons/tree/master/example).

Maintenant, exécutez `flutter pub get` dans le terminal ou cliquez sur Pub get dans l'IDE.

Exécutez la commande suivante dans le terminal :

```bash
flutter pub run flutter_launcher_icons:main
```

Exécutez votre application et vous devriez voir que l'icône de lancement a changé.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/1_PYauSNowIcCEk4dB8FJshA.jpeg)

## Comment générer des icônes personnalisées dans Flutter

Nous pourrons générer des icônes personnalisées via [FlutterIcon.com](https://www.fluttericon.com/). Cela nous permet soit :

* Télécharger un SVG qui est converti en icône
* Choisir parmi une énorme sélection d'icônes issues de différents ensembles de packages d'icônes

![Image](https://www.freecodecamp.org/news/content/images/2022/01/1_cUVrtz2mfcum4hsK44kDNA.jpeg)

⚠️ Il existe un package appelé [FlutterIcon](https://pub.dev/packages/fluttericon) qui contient toutes les icônes affichées, mais en raison de sa taille importante, je recommande de ne choisir que les icônes dont vous avez besoin et de ne pas l'utiliser.

Démontrons comment importer des icônes personnalisées dans votre application en utilisant ce site web.

Imaginez que nous avons le formulaire suivant dans notre application :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/qemu-system-x86_64_5wbTMarncT.png)

Vous pouvez voir que nous avons utilisé des icônes pour chaque TextFormField. Voici le code pour le premier TextFormField :

```dart
TextFormField(
  controller: pillNameTextEditingController,
  decoration: const InputDecoration(
      border: OutlineInputBorder(),
      hintText: 'What is the pill\'s name?',
      prefixIcon: Icon(Icons.title)
  ),
  validator: (value) {
    if (value == null || value.isEmpty) {
      return 'Please enter a pill name';
    }
    return null;
  }
)
```

Et si nous changions l'icône du premier TextFormField en quelque chose de plus pertinent ?

Sur FlutterIcon.com :

* Choisissez les icônes que vous souhaitez utiliser/télécharger un fichier SVG
* Donnez un nom significatif à votre classe d'icônes (Nous appellerons notre classe **CustomIcons**)
* Appuyez sur Télécharger

![Image](https://www.freecodecamp.org/news/content/images/2022/01/1_pnVmm0MQLyu67JgAnWaX2w.jpeg)

Dans le dossier .zip que vous avez téléchargé, il y a plusieurs fichiers :

* Un dossier fonts avec un fichier TTF portant le nom de la classe que vous avez choisie
* Un fichier config.json utilisé pour se souvenir des icônes que vous avez choisies
* Une classe dart portant le nom de la classe que vous avez choisie

![Image](https://www.freecodecamp.org/news/content/images/2022/01/1_bMUGR_xcccd1TgSM109yEQ.jpeg)

À l'intérieur de votre projet, importez le fichier .ttf dans un dossier appelé fonts sous le **répertoire racine**. Cela devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/1_63PhBP1BuY4961WpCml9KQ.jpeg)

Placez la classe .dart à l'intérieur de votre dossier lib. Si vous regardez à l'intérieur du fichier dart, vous verrez quelque chose de similaire (vous pourriez voir plus d'objets IconData si vous avez choisi plus d'une icône à télécharger) :

```dart
import 'package:flutter/widgets.dart';

class CustomIcons {
  CustomIcons._();

  static const _kFontFam = 'CustomIcons';
  static const String? _kFontPkg = null;

  static const IconData pill = IconData(0xea60, fontFamily: _kFontFam, fontPackage: _kFontPkg);
}
```

Ajoutez ce qui suit à votre fichier pubspec.yaml :

```yaml
fonts:
      - family: CustomIcons
        fonts:
          - asset: fonts/CustomIcons.ttf
```

Exécutez `flutter pub get` dans le terminal ou cliquez sur Pub get dans l'IDE.

Allez à l'endroit où vous souhaitez utiliser vos icônes personnalisées et utilisez-les comme ceci :

```dart
TextFormField(
  controller: pillNameTextEditingController,
  decoration: const InputDecoration(
      border: OutlineInputBorder(),
      hintText: 'What is the pill\'s name?',
      prefixIcon: Icon(CustomIcons.pill)
  ),
  validator: (value) {
    if (value == null || value.isEmpty) {
      return 'Please enter a pill name';
    }
    return null;
  }
)
```

![Image](https://www.freecodecamp.org/news/content/images/2022/01/1_G7MmSKn3xVeJJcLkUO0goA.png)

## Dépannage des icônes personnalisées dans Flutter

Si vos icônes personnalisées apparaissent sous forme de carrés avec des X, quelque chose ne va pas. Vous pourriez également voir les avertissements suivants dans le journal :

```
Warning: No fonts specified for font CustomIcons
Warning: Missing family name for font.
```

Cela peut être dû à plusieurs raisons :

* Assurez-vous que votre fichier pubspec.yaml est valide. Cela signifie qu'il n'y a pas d'espaces supplémentaires, d'indentation, etc. Vous pouvez utiliser [cet](http://yaml-online-parser.appspot.com/) outil pour cela.
* Assurez-vous d'avoir correctement référencé votre police dans votre fichier pubspec.yaml.
* Assurez-vous d'avoir placé votre fichier .ttf à l'intérieur d'un répertoire **fonts** sous le répertoire racine de votre projet (et non à l'intérieur du répertoire assets).
* Désinstallez votre application et réinstallez-la sur votre appareil.

Si vous souhaitez voir une application réelle utilisant les deux types d'icônes, vous pouvez la consulter ici :

%[https://play.google.com/store/apps/details?id=com.tomerpacific.pill]

Et vous pouvez voir le code source ici :

%[https://github.com/TomerPacific/Pill]

Merci d'avoir lu !