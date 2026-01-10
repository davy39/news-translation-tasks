---
title: Comment enregistrer et partager des widgets Flutter sous forme d'images – Un
  guide complet prêt pour la production
subtitle: ''
author: Atuoha Anthony
co_authors: []
series: null
date: '2025-09-02T20:41:21.100Z'
originalURL: https://freecodecamp.org/news/how-to-save-and-share-flutter-widgets-as-images-a-complete-production-ready-guide
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1756845409709/5224a6ae-93a9-4424-9a28-cccff69779f2.png
tags:
- name: Flutter
  slug: flutter
- name: flutter-aware
  slug: flutter-aware
seo_title: Comment enregistrer et partager des widgets Flutter sous forme d'images
  – Un guide complet prêt pour la production
seo_desc: In many apps, you may want users to be able to save or share visual content
  generated in the UI. Flutter doesn’t ship with a “save widget to image” API, but
  with RepaintBoundary plus a few small packages, you can capture any widget, save
  it to the de...
---

Dans de nombreuses applications, vous pourriez souhaiter que les utilisateurs puissent enregistrer ou partager du contenu visuel généré dans l'interface utilisateur (UI). Flutter n'est pas livré avec une API native « enregistrer le widget en image », mais avec `RepaintBoundary` et quelques packages légers, vous pouvez capturer n'importe quel widget, l'enregistrer dans la galerie de l'appareil et le partager via la feuille de partage native.

Cet article détaillera le processus de capture et d'enregistrement d'un widget étape par étape. Nous allons construire une petite application Flutter qui affiche une Carte de Citation (Quote Card) stylisée et propose deux actions :

1. Enregistrer la carte de citation dans la galerie de l'appareil au format PNG.
    
2. Partager l'image via la feuille de partage native (WhatsApp, Gmail, Messages, etc.).
    

## Table des matières :

1. [Prérequis](#heading-prerequis)
    
2. [Configuration du projet](#heading-configuration-du-projet)
    
3. [Dépendances](#heading-dependances)
    
4. [Configuration des plateformes](#heading-configuration-des-plateformes)
    
    1. [Android](#heading-android)
        
    2. [iOS](#heading-ios)
        
5. [Architecture de l'application et aperçu des fichiers](#heading-architecture-de-l-application-et-apercu-des-fichiers)
    
6. [Sections de code avec explications](#heading-sections-de-code-avec-explications)
    
    1. [lib/main.dart](#heading-a-libmaindart)
        
    2. [lib/widgets/quote\_card.dart](#heading-b-libwidgetsquotecarddart)
        
    3. [lib/utils/capture.dart](#heading-c-libutilscapturedart)
        
    4. [lib/services/permission\_service.dart](#heading-d-libservicespermissionservicedart)
        
    5. [lib/services/gallery\_saver\_service.dart](#heading-e-libservicesgallerysaverservicedart)
        
    6. [lib/services/share\_service.dart](#heading-f-libservicesshareservicedart)
        
    7. [lib/screens/quote\_screen.dart](#heading-g-libscreensquotescreendart)
        
    8. [Variables d'état](#heading-1-variables-d-etat)
        
    9. [Fonction de capture](#heading-2-fonction-de-capture)
        
    10. [Fonction d'enregistrement](#heading-3-fonction-d-enregistrement)
        
    11. [Fonction de partage](#heading-4-fonction-de-partage)
        
    12. [Résumé](#heading-resume)
        
7. [Tester le flux](#heading-tester-le-flux)
    
8. [Dépannage et pièges courants](#heading-depannage-et-pieges-courants)
    
9. [Améliorations et alternatives](#heading-ameliorations-et-alternatives)
    
10. [Conclusion](#heading-conclusion)
    
11. [Références](#heading-references)
    

## Prérequis

1. Flutter 3.x ou version ultérieure installé et configuré
    
2. Un appareil ou émulateur Android, et optionnellement un appareil ou simulateur iOS
    
3. Une connaissance de base des widgets Flutter et de la structure des projets
    

## Configuration du projet

Créez un nouveau projet et ouvrez-le dans votre IDE :

```bash
flutter create quote_share_app
cd quote_share_app
```

## Dépendances

Ajoutez les éléments suivants au fichier `pubspec.yaml` sous `dependencies:` et lancez `flutter pub get` :

```yaml
dependencies:
  flutter:
    sdk: flutter
  permission_handler: ^11.3.1
  image_gallery_saver: ^2.0.3
  path_provider: ^2.1.3
  share_plus: ^9.0.0
```

Notes sur ce code :

1. `permission_handler` gère les permissions au moment de l'exécution si nécessaire.
    
2. `image_gallery_saver` écrit les octets bruts dans la galerie photo (Android et iOS).
    
3. `path_provider` crée un emplacement de fichier temporaire avant le partage.
    
4. `share_plus` invoque la feuille de partage de la plateforme.
    

Les numéros de version ci-dessus sont des exemples fonctionnant avec Flutter 3.x au moment de la rédaction. Si vous effectuez une mise à jour, vérifiez le README de chaque package pour tout changement d'API.

## Configuration des plateformes

Les permissions de stockage modernes sur Android et iOS sont plus strictes que ce que suggèrent souvent les anciens articles de blog. Les extraits ci-dessous correspondent aux meilleures pratiques actuelles.

### Android

Ouvrez `android/app/src/main/AndroidManifest.xml`.

Pour Android 10 (API 29) et versions supérieures, `WRITE_EXTERNAL_STORAGE` est obsolète. Pour Android 13 (API 33)+, vous demandez des permissions limitées aux médias comme `READ_MEDIA_IMAGES` uniquement si vous lisez des images. Pour enregistrer votre propre image dans la collection Pictures ou DCIM, de nombreux appareils ne nécessitent pas les anciennes permissions de stockage externe lors de l'écriture via MediaStore (les plugins s'en chargent souvent). `image_gallery_saver` fonctionne généralement sans `WRITE_EXTERNAL_STORAGE` sur l'API 29+.

Ajoutez ce qui suit uniquement si vous ciblez des appareils plus anciens et que le plugin l'exige toujours. Sinon, vous pouvez omettre les permissions de stockage pour les SDK modernes.

```xml
<!-- Optionnel pour les anciens appareils pré-API 29 -->
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"
    android:maxSdkVersion="28" />
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"
    android:maxSdkVersion="32" />

<!-- Pour Android 13+ si vous devez un jour lire les images de l'utilisateur ; non requis pour écrire votre propre image -->
<uses-permission android:name="android.permission.READ_MEDIA_IMAGES" />
```

N'ajoutez pas `android:requestLegacyExternalStorage="true"`. Ce flag était un pont de compatibilité temporaire pour Android 10 et n'est plus recommandé.

Configuration Gradle : assurez-vous que votre `compileSdkVersion` et `targetSdkVersion` sont à jour (33 ou 34). Vous n'avez généralement pas besoin de modifications Gradle spéciales au-delà de ce que fournissent les templates Flutter.

### iOS

Ouvrez `ios/Runner/Info.plist` et ajoutez les clés suivantes pour expliquer pourquoi vous enregistrez dans la bibliothèque photo de l'utilisateur :

```xml
<key>NSPhotoLibraryAddUsageDescription</key>
<string>L'application a besoin d'accéder à votre galerie pour enregistrer les images générées.</string>
<key>NSPhotoLibraryUsageDescription</key>
<string>L'application a besoin d'accéder à votre bibliothèque de photos.</string>
```

Certains appareils ne requièrent que la description d'utilisation "Add" pour l'écriture, mais fournir les deux permet de clarifier l'intention.

## Architecture de l'application et aperçu des fichiers

Pour maintenir le code, nous allons le diviser en petits fichiers :

1. lib/main.dart
    
2. lib/widgets/quote\_card.dart
    
3. lib/utils/capture.dart
    
4. lib/services/permission\_service.dart
    
5. lib/services/gallery\_saver\_service.dart
    
6. lib/services/share\_service.dart
    
7. lib/screens/quote\_screen.dart
    

Voici le flux de fonctionnement :

1. `QuoteCard` affiche le widget visuel que nous voulons capturer.
    
2. `captureWidgetToPngBytes(GlobalKey)` convertit ce widget en octets PNG en utilisant `RepaintBoundary`.
    
3. `PermissionService` demande les permissions de stockage ou de bibliothèque photo si nécessaire.
    
4. `GallerySaverService` enregistre les octets dans la galerie.
    
5. `ShareService` écrit les octets dans un fichier temporaire et déclenche la feuille de partage.
    
6. `QuoteScreen` relie le tout avec deux boutons : Enregistrer et Partager.
    

## Sections de code avec explications

### 1\. lib/main.dart

```dart
import 'package:flutter/material.dart';
import 'screens/quote_screen.dart';

void main() {
  runApp(const QuoteShareApp());
}

class QuoteShareApp extends StatelessWidget {
  const QuoteShareApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Quote Share App',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        colorSchemeSeed: Colors.teal,
        useMaterial3: true,
      ),
      home: const QuoteScreen(),
    );
  }
}
```

Explication du code :

1. `runApp` démarre l'application.
    
2. `MaterialApp` fournit le thème et la navigation.
    
3. `QuoteScreen` est notre écran unique ; il affiche la carte et les boutons.
    

### 2\. lib/widgets/quote\_card.dart

```dart
import 'package:flutter/material.dart';

class QuoteCard extends StatelessWidget {
  final String quote;
  final String author;

  const QuoteCard({
    super.key,
    required this.quote,
    required this.author,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      width: double.infinity,
      padding: const EdgeInsets.all(24),
      decoration: BoxDecoration(
        color: Colors.teal.shade50,
        borderRadius: BorderRadius.circular(20),
        boxShadow: [
          BoxShadow(
            color: Colors.teal.shade200.withOpacity(0.4),
            blurRadius: 12,
            offset: const Offset(2, 6),
          ),
        ],
        border: Border.all(color: Colors.teal.shade200, width: 1),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            '"$quote"',
            style: const TextStyle(
              fontSize: 22,
              fontStyle: FontStyle.italic,
              color: Colors.black87,
              height: 1.4,
            ),
          ),
          const SizedBox(height: 16),
          Align(
            alignment: Alignment.bottomRight,
            child: Text(
              '- $author',
              style: const TextStyle(
                fontSize: 16,
                fontWeight: FontWeight.w600,
                color: Colors.black54,
              ),
            ),
          ),
        ],
      ),
    );
  }
}
```

Explication du code :

1. Interface pure (UI). Ce widget est ce que nous allons capturer en image.
    
2. Les styles (padding, ombres, coins arrondis) garantissent que le résultat sera esthétique une fois enregistré ou partagé.
    

### 3\. lib/utils/capture.dart

```dart
import 'dart:typed_data';
import 'dart:ui' as ui;
import 'package:flutter/material.dart';

/// Capture le widget référencé par [boundaryKey] en octets PNG.
/// Placez un RepaintBoundary avec la clé [boundaryKey] autour du widget à capturer.
Future<Uint8List?> captureWidgetToPngBytes(GlobalKey boundaryKey, {double pixelRatio = 3.0}) async {
  try {
    final context = boundaryKey.currentContext;
    if (context == null) return null;

    final renderObject = context.findRenderObject();
    if (renderObject is! RenderRepaintBoundary) return null;

    // Si la limite n'est pas encore dessinée, attendre un frame et réessayer.
    if (renderObject.debugNeedsPaint) {
      await Future.delayed(const Duration(milliseconds: 20));
      return captureWidgetToPngBytes(boundaryKey, pixelRatio: pixelRatio);
    }

    // Rendu vers une Image avec un pixelRatio plus élevé pour la netteté sur les écrans haute densité.
    final ui.Image image = await renderObject.toImage(pixelRatio: pixelRatio);

    // Encoder l'Image en PNG et retourner les octets.
    final byteData = await image.toByteData(format: ui.ImageByteFormat.png);
    return byteData?.buffer.asUint8List();
  } catch (e) {
    debugPrint('Erreur captureWidgetToPngBytes : $e');
    return null;
  }
}
```

Explication du code ligne par ligne :

1. Nous acceptons une `GlobalKey` qui doit être attachée à un `RepaintBoundary` enveloppant le widget cible.
    
2. `findRenderObject()` récupère le nœud de l'arbre de rendu. `RenderRepaintBoundary` peut prendre un instantané de lui-même vers une image.
    
3. `debugNeedsPaint` indique si le widget est complètement disposé et dessiné. Si ce n'est pas le cas, nous attendons brièvement et réessayons.
    
4. `toImage(pixelRatio: 3.0)` effectue le rendu avec une résolution plus élevée pour un résultat net. Augmentez-le si vous avez besoin d'images encore plus précises, mais attention à la consommation de mémoire.
    
5. Nous encodons l'`ui.Image` en PNG via `toByteData` et retournons ses octets.
    

### 4\. lib/services/permission\_service.dart

```dart
import 'dart:io';
import 'package:permission_handler/permission_handler.dart';

class PermissionService {
  /// Demande les permissions de stockage/photo nécessaires pour enregistrer une image.
  static Future<bool> requestSavePermission() async {
    if (Platform.isAndroid) {
      // Sur Android 13+, vous n'avez généralement pas besoin de permission WRITE pour enregistrer votre propre image.
      // Certains constructeurs exigent encore la permission de stockage pour certaines opérations de galerie.
      final status = await Permission.storage.request();
      if (status.isGranted) return true;

      if (status.isPermanentlyDenied) {
        await openAppSettings();
      }
      return false;
    }

    if (Platform.isIOS) {
      // Sur iOS, demande la permission Photos pour l'ajout à la bibliothèque uniquement.
      final status = await Permission.photosAddOnly.request();
      if (status.isGranted) return true;

      // Certaines versions d'iOS peuvent utiliser `Permission.photos`.
      final photos = await Permission.photos.request();
      if (photos.isGranted) return true;

      return false;
    }

    return true;
  }
}
```

Dans le code ci-dessus, les permissions de stockage Android sont fragmentées par niveau d'API et comportement du constructeur. Demander `Permission.storage` reste une approche pragmatique lors de l'utilisation de plugins de sauvegarde en galerie, bien que de nombreux appareils modernes réussissent même si l'utilisateur la refuse.

Sur iOS, nous demandons la permission d'ajout à la bibliothèque de photos.

### 5\. lib/services/gallery\_saver\_service.dart

```dart
import 'dart:typed_data';
import 'package:image_gallery_saver/image_gallery_saver.dart';

class GallerySaverService {
  /// Enregistre [pngBytes] dans la galerie et retourne une Map de résultat du plugin.
  static Future<Map?> savePngBytesToGallery(Uint8List pngBytes, {String? name}) async {
    final result = await ImageGallerySaver.saveImage(
      pngBytes,
      name: name, // Nom de base optionnel (le plugin peut ajouter l'extension/l'heure)
      quality: 100,
    );
    return result as Map?;
  }
}
```

Explication du code :

1. `image_gallery_saver` écrit les octets fournis dans la bibliothèque photo.
    
2. Nous passons `quality: 100` pour la meilleure qualité PNG possible.
    

Ce code définit une classe utilitaire qui enregistre les données d'image PNG brutes (octets) dans la galerie photo de l'appareil.

### 6\. lib/services/share\_service.dart

```dart
import 'dart:io';
import 'dart:typed_data';
import 'package:path_provider/path_provider.dart';
import 'package:share_plus/share_plus.dart';

class ShareService {
  /// Écrit [pngBytes] dans un fichier temporaire et invoque la feuille de partage de la plateforme.
  static Future<void> sharePngBytes(Uint8List pngBytes, {String? text}) async {
    final tempDir = await getTemporaryDirectory();
    final filePath = '${tempDir.path}/quote_${DateTime.now().millisecondsSinceEpoch}.png';

    final file = File(filePath);
    await file.writeAsBytes(pngBytes, flush: true);

    await Share.shareXFiles(
      [XFile(file.path)],
      text: text ?? 'Voici une citation partagée depuis mon application.',
    );
  }
}
```

Le partage nécessite généralement un chemin de fichier, pas des octets bruts. Nous créons un fichier temporaire, écrivons les octets et le passons à `share_plus` en utilisant `shareXFiles`.

### 7\. lib/screens/quote\_screen.dart

```dart
import 'dart:typed_data';
import 'package:flutter/material.dart';
import '../widgets/quote_card.dart';
import '../utils/capture.dart';
import '../services/permission_service.dart';
import '../services/gallery_saver_service.dart';
import '../services/share_service.dart';

class QuoteScreen extends StatefulWidget {
  const QuoteScreen({super.key});

  @override
  State<QuoteScreen> createState() => _QuoteScreenState();
}

class _QuoteScreenState extends State<QuoteScreen> {
  final GlobalKey _captureKey = GlobalKey();

  bool _isSaving = false;
  bool _isSharing = false;

  Future<Uint8List?> _capture() async {
    return captureWidgetToPngBytes(_captureKey, pixelRatio: 3.0);
  }

  Future<void> _saveImage() async {
    setState(() => _isSaving = true);
    try {
      final granted = await PermissionService.requestSavePermission();
      if (!granted) {
        if (mounted) {
          ScaffoldMessenger.of(context).showSnackBar(
            const SnackBar(content: Text('Permission requise pour enregistrer les images.')),
          );
        }
        return;
      }

      final bytes = await _capture();
      if (bytes == null) {
        if (mounted) {
          ScaffoldMessenger.of(context).showSnackBar(
            const SnackBar(content: Text('Échec de la capture de l\'image.')),
          );
        }
        return;
      }

      final result = await GallerySaverService.savePngBytesToGallery(
        bytes,
        name: 'quote_${DateTime.now().millisecondsSinceEpoch}',
      );

      if (mounted) {
        final ok = result != null;
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(content: Text(ok ? 'Image enregistrée dans la galerie.' : 'Échec de l\'enregistrement.')),
        );
      }
    } catch (e) {
      if (mounted) {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(content: Text('Erreur : $e')),
        );
      }
    } finally {
      if (mounted) setState(() => _isSaving = false);
    }
  }

  Future<void> _shareImage() async {
    setState(() => _isSharing = true);
    try {
      final bytes = await _capture();
      if (bytes == null) {
        if (mounted) {
          ScaffoldMessenger.of(context).showSnackBar(
            const SnackBar(content: Text('Échec de la capture de l\'image.')),
          );
        }
        return;
      }
      await ShareService.sharePngBytes(bytes, text: 'Voici une citation que je voulais partager.');
    } catch (e) {
      if (mounted) {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(content: Text('Erreur : $e')),
        );
      }
    } finally {
      if (mounted) setState(() => _isSharing = false);
    }
  }

  @override
  Widget build(BuildContext context) {
    const quote = "Croyez en vous-même et vous aurez fait la moitié du chemin.";
    const author = 'Theodore Roosevelt';

    return Scaffold(
      appBar: AppBar(
        title: const Text('Partage de Citation'),
        centerTitle: true,
      ),
      body: Padding(
        padding: const EdgeInsets.all(20.0),
        child: Column(
          children: [
            RepaintBoundary(
              key: _captureKey,
              child: const QuoteCard(
                quote: quote,
                author: author,
              ),
            ),
            const SizedBox(height: 24),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                FilledButton.icon(
                  onPressed: _isSaving ? null : _saveImage,
                  icon: _isSaving
                      ? const SizedBox(width: 16, height: 16, child: CircularProgressIndicator(strokeWidth: 2))
                      : const Icon(Icons.download),
                  label: Text(_isSaving ? 'Enregistrement...' : 'Enregistrer'),
                ),
                OutlinedButton.icon(
                  onPressed: _isSharing ? null : _shareImage,
                  icon: _isSharing
                      ? const SizedBox(width: 16, height: 16, child: CircularProgressIndicator(strokeWidth: 2))
                      : const Icon(Icons.share),
                  label: Text(_isSharing ? 'Partage...' : 'Partager'),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}
```

#### Variables d'état

`_isSaving` et `_isSharing` sont utilisés pour suivre l'état des opérations en cours. Ces drapeaux permettent de désactiver les boutons de l'interface utilisateur, d'afficher un indicateur de chargement ou d'empêcher les actions en double.

#### Fonction de capture

Cette fonction capture un widget Flutter (référencé par `_captureKey`) et le convertit en octets d'image PNG (`Uint8List`). Le paramètre `pixelRatio: 3.0` garantit que l'image capturée est en haute résolution.

#### Fonction d'enregistrement

Elle demande les permissions via `PermissionService`, capture le widget, puis utilise `GallerySaverService` pour l'ajouter à la galerie de l'utilisateur.

#### Fonction de partage

Elle capture le widget et appelle `ShareService.sharePngBytes` pour partager l'image avec un texte descriptif. Cela ouvre généralement la feuille de partage système.

#### Résumé

1. `_capture()` convertit un widget en image (octets PNG).
2. `_saveImage()` gère les permissions et l'enregistrement.
3. `_shareImage()` gère la création du fichier temporaire et le partage système.

## Tester le flux

Pour tester cette configuration, vous devriez l'exécuter sur un appareil réel pour un comportement plus précis.

Appuyez sur Partager. La feuille de partage devrait apparaître. Appuyez ensuite sur Enregistrer. Sur certains appareils, vous pourriez être sollicité pour une permission – acceptez-la. Vérifiez votre application Photos ou Galerie pour voir l'image enregistrée.

## Dépannage et pièges courants

Si l'image enregistrée est vide ou noire, assurez-vous que le widget est complètement dessiné. Vérifiez que le `RepaintBoundary` enveloppe directement le contenu cible et non un parent de taille nulle.

Si la permission est refusée sur Android alors que vous l'avez autorisée, certains constructeurs ont des politiques de stockage agressives. Confirmez que l'application a bien accès aux Photos ou aux Fichiers dans les paramètres système.

Si l'image n'est pas visible immédiatement dans la Galerie, attendez un moment – certaines galeries indexent les fichiers de manière asynchrone.

## **Améliorations et alternatives**

### Utiliser un filigrane ou un logo

Vous pouvez superposer un logo de marque ou un widget de filigrane avant de prendre la capture d'écran pour renforcer l'image de marque.

### Utiliser des arrière-plans dynamiques

Au lieu d'une couleur unie, vous pourriez rendre la citation plus attrayante avec des dégradés ou des images d'arrière-plan via `BoxDecoration`.

### Cibles de capture multiples

Si votre application doit capturer plusieurs types d'éléments, utilisez une `Map<String, GlobalKey>` pour référencer et capturer dynamiquement le bon widget.

### Packages alternatifs

* `screenshot` : Fournit une API de plus haut niveau pour simplifier la capture d'écran.
* `widgets_to_image` : Une autre option focalisée sur la conversion de widgets spécifiques.
* **Génération de PDF** (`printing` / `pdf`) : Si vous avez besoin de documents partageables plutôt que d'images.

## Conclusion

Vous disposez maintenant d'une approche complète et prête pour la production pour capturer un widget Flutter en image, l'enregistrer dans la galerie et le partager. Les éléments clés sont `RepaintBoundary` pour une capture fidèle, une gestion minutieuse des permissions et des services modulaires.

## **Références**

1. [Documentation du package share\_plus](https://pub.dev/packages/share_plus)
    
2. [Documentation du package image\_gallery\_saver](https://pub.dev/packages/image_gallery_saver)
    
3. [Documentation du package path\_provider](https://pub.dev/packages/path_provider)
    
4. [Documentation officielle Flutter : Manipulation de fichiers](https://docs.flutter.dev/cookbook/persistence/reading-writing-files)