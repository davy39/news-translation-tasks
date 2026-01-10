---
title: Comment configurer Firebase Crashlytics dans une application Flutter (iOS et
  Android)
subtitle: ''
author: Atuoha Anthony
co_authors: []
series: null
date: '2025-08-21T00:16:46.353Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-firebase-crashlytics-in-a-flutter-app-ios-and-android
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1755735394033/aa70989a-2653-4f36-a8bf-fbf953d09512.png
tags:
- name: firebase-crashlytics
  slug: firebase-crashlytics
- name: Flutter
  slug: flutter
- name: flutter-aware
  slug: flutter-aware
- name: Firebase
  slug: firebase
seo_title: Comment configurer Firebase Crashlytics dans une application Flutter (iOS
  et Android)
seo_desc: 'When you’re building mobile applications, one of the biggest challenges
  you might face is ensuring stability in real-world usage. No matter how much testing
  you do, unexpected crashes are bound to occur.

  This is where Firebase Crashlytics becomes an ...'
---

Lorsque vous créez des applications mobiles, l'un des plus grands défis auxquels vous pourriez être confronté est d'assurer la stabilité en utilisation réelle. Quel que soit le volume de tests effectués, des crashs inattendus finiront par se produire.

C'est là que **Firebase Crashlytics** devient un outil essentiel. Crashlytics est un rapporteur de crashs léger et en temps réel qui vous aide à comprendre pourquoi votre application plante et quelle est l'étendue du problème parmi les utilisateurs. Grâce à ces informations, vous pouvez corriger les bogues plus rapidement et améliorer la fiabilité de votre application.

Dans cet article, nous allons parcourir la configuration de Firebase Crashlytics dans une application Flutter pour les plateformes iOS et Android. En cours de route, vous apprendrez non seulement comment intégrer Crashlytics, mais aussi le raisonnement derrière chaque étape, afin de comprendre pleinement son fonctionnement.

### Table des matières :

1. [Prérequis](#heading-prerequis)
    
2. [Configurer le projet Flutter](#heading-configurer-le-projet-flutter)
    
3. [Connecter Flutter à Firebase](#heading-connecter-flutter-a-firebase)
    
4. [Ajouter les dépendances requises](#heading-ajouter-les-dependances-requises)
    
5. [Initialiser Crashlytics dans main.dart](#heading-initialiser-crashlytics-dans-maindart)
    
6. [Créer un écran de test simple](#heading-creer-un-ecran-de-test-simple)
    
7. [Exécuter et tester l'application](#heading-executer-et-tester-l-application)
    
8. [Comprendre le tableau de bord Crashlytics](#heading-comprendre-le-tableau-de-bord-crashlytics)
    
9. [Firebase Crashlytics avancé dans Flutter : aller au-delà des bases](#heading-firebase-crashlytics-avance-dans-flutter-aller-au-dela-des-bases)
    
    * [Comment enregistrer les erreurs non fatales](#heading-comment-enregistrer-les-erreurs-non-fatales)
        
    * [Comment ajouter des clés personnalisées pour le contexte](#heading-comment-ajouter-des-cles-personnalisees-pour-le-contexte)
        
    * [Comment enregistrer des événements personnalisés et des fils d'Ariane](#heading-comment-enregistrer-des-evenements-personnalises-et-des-fil-d-ariane)
        
    * [Comment associer les crashs aux utilisateurs](#heading-comment-associer-les-crashs-aux-utilisateurs)
        
    * [Comment assurer une symbolisation correcte](#heading-comment-assurer-une-symbolisation-correcte)
        
    * [Comment contrôler la collecte des données](#heading-comment-controler-la-collecte-des-donnees)
        
10. [Bonnes pratiques pour la production](#heading-bonnes-pratiques-pour-la-production)
    
11. [Conclusion](#heading-conclusion)
    
12. [Références](#heading-references)
    

## Prérequis

Avant de vous lancer dans la configuration, assurez-vous de disposer des éléments suivants. Ces prérequis garantissent que votre environnement est correctement configuré et que vous ne resterez pas bloqué à mi-chemin de l'intégration.

Tout d'abord, vous avez besoin d'une **installation de Flutter** fonctionnelle sur votre système. Flutter doit être correctement installé et configuré pour que vous puissiez exécuter des applications sur iOS et Android. Si vous ne l'avez pas encore configuré, suivez le guide officiel d' [installation de Flutter](https://docs.flutter.dev/get-started/install) pour préparer votre environnement de développement.

Ensuite, vous avez besoin d'un **compte Firebase**. Firebase fournit une console Web où vous créerez un projet qui sera lié à votre application Flutter. Vous pouvez vous inscrire gratuitement sur la [Console Firebase.](https://console.firebase.google.com/)

Pour un processus d'intégration plus fluide, je recommande également fortement l'installation de l'interface de ligne de commande [**Firebase CLI**](https://firebase.google.com/docs/flutter/setup?platform=ios). La CLI permet d'utiliser la commande `flutterfire configure`, qui lie automatiquement votre projet [Flutter](https://docs.flutter.dev/get-started/install) à Firebase et génère un fichier `firebase_options.dart` contenant toutes vos configurations spécifiques à chaque plateforme. Cette étape est facultative, mais elle vous fait gagner du temps par rapport à l'ajout manuel des fichiers de configuration. Vous pouvez installer la CLI en suivant les [instructions de configuration de la Firebase CLI.](https://firebase.google.com/docs/cli)

Enfin, assurez-vous d'avoir soit un **simulateur iOS** (via Xcode sur macOS), soit un **émulateur Android** (via Android Studio ou la ligne de commande) pour tester l'intégration. Crashlytics n'enregistrera les crashs qu'une fois que l'application aura été exécutée sur un appareil réel ou simulé.

Une fois ces prérequis en place, vous êtes prêt à passer aux étapes d'intégration réelles.

## Configurer le projet Flutter

Le parcours commence par la création d'un projet Flutter. Si vous n'en avez pas déjà un, exécutez la commande suivante depuis votre terminal :

```bash
flutter create my_crashlytics_app
cd my_crashlytics_app
```

Cela génère la structure de base (boilerplate) de votre application Flutter, nous donnant une base sur laquelle nous pouvons ajouter Firebase et Crashlytics.

## Connecter Flutter à Firebase

Avant que Crashlytics puisse fonctionner, votre application doit être connectée à un projet Firebase. Rendez-vous sur la console Firebase et créez un nouveau projet. Considérez le projet Firebase comme le « conteneur backend » qui gère tous les services, y compris l'analyse, l'authentification et le rapport de crashs.

Une fois le projet créé, vous devez enregistrer vos applications Flutter auprès de Firebase. Flutter prenant en charge iOS et Android, vous ajouterez les deux plateformes.

Côté iOS, Firebase vous guidera pour ajouter une application iOS, télécharger le fichier de configuration `GoogleService-Info.plist` et le placer dans le répertoire `ios/Runner` de votre projet Flutter. Sur Android, vous ferez quelque chose de similaire en téléchargeant le fichier `google-services.json` et en l'ajoutant au répertoire `android/app`.

Si vous préférez une approche plus simple, la Firebase CLI propose la commande `flutterfire configure`. Son exécution vous permettra de sélectionner votre projet Firebase et de générer automatiquement un fichier `firebase_options.dart` pour votre application Flutter. Ce fichier centralise votre configuration Firebase et réduit la configuration manuelle.

## Ajouter les dépendances requises

Une fois Firebase lié, l'étape suivante consiste à importer les packages nécessaires qui activent Crashlytics. Flutter s'intègre à Firebase via des plugins, qui sont de petites bibliothèques faisant le pont entre Flutter et les SDK natifs. Ouvrez votre fichier `pubspec.yaml` et ajoutez ce qui suit :

```yaml
dependencies:
  firebase_core: ^4.0.0
  firebase_crashlytics: ^5.0.0
```

Le package `firebase_core` initialise la communication avec Firebase, tandis que `firebase_crashlytics` est la bibliothèque qui capture et signale les crashs. Exécutez `flutter pub get` pour télécharger et installer ces dépendances.

## Initialiser Crashlytics dans `main.dart`

Maintenant que les dépendances sont installées, nous devons initialiser Firebase au démarrage de l'application et configurer Crashlytics pour capturer les erreurs synchrones et asynchrones. Remplacez le contenu de votre fichier `lib/main.dart` par le code suivant :

```dart
import 'dart:ui';
import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_crashlytics/firebase_crashlytics.dart';
import 'firebase_options.dart';
import 'presentation/home_screen.dart';
import 'package:flutter/material.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp(
    options: DefaultFirebaseOptions.currentPlatform,
  );

  // Capturer les erreurs du Framework Flutter
  FlutterError.onError = FirebaseCrashlytics.instance.recordFlutterFatalError;

  // Capturer les erreurs asynchrones non interceptées
  PlatformDispatcher.instance.onError = (error, stack) {
    FirebaseCrashlytics.instance.recordError(error, stack, fatal: true);
    return true;
  };

  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Firebase Crashlytics Demo',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
        useMaterial3: true,
      ),
      home: const HomeScreen(),
    );
  }
}
```

Arrêtons-nous un instant pour analyser cela. La ligne `FlutterError.onError` garantit que toute erreur survenant dans l'arborescence des widgets de Flutter est signalée comme un **crash fatal**. `PlatformDispatcher.instance.onError` capture les erreurs en dehors de l'arborescence des widgets, telles que les exceptions asynchrones, et les signale également à Crashlytics. Ensemble, ces configurations garantissent que pratiquement tous les problèmes inattendus sont envoyés à Firebase.

## Créer un écran de test simple

Pour vérifier que Crashlytics fonctionne, créons un écran de test où nous pouvons délibérément provoquer des erreurs. Créez un nouveau dossier nommé `presentation` dans votre répertoire `lib`, puis à l'intérieur, créez un fichier nommé `home_screen.dart` avec le contenu suivant :

```dart
import 'package:flutter/material.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  int _counter = 0;

  void _incrementCounter() {
    setState(() {
      _counter++;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: const Text('Application Firebase Crashlytics'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            const Text('Vous avez appuyé sur le bouton ce nombre de fois :'),
            Text(
              '$_counter',
              style: Theme.of(context).textTheme.headlineMedium,
            ),
            const SizedBox(height: 15),
            ElevatedButton(
              onPressed: () => throw Exception('Exception de test'),
              child: const Text('Provoquer une Exception'),
            ),
            const SizedBox(height: 10),
            ElevatedButton(
              onPressed: () {
                throw const FormatException('Une erreur de format personnalisée s\'est produite');
              },
              child: const Text('Provoquer une Exception avec Feedback'),
            ),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _incrementCounter,
        tooltip: 'Incrémenter',
        child: const Icon(Icons.add),
      ),
    );
  }
}
```

Cet écran propose deux boutons : l'un qui lance une exception générale et l'autre qui lance une exception de format. Lorsqu'ils sont cliqués, ces crashs sont signalés à Crashlytics. Cela permet de tester facilement si votre configuration fonctionne correctement.

![Boutons d'exception générale et de format](https://cdn.hashnode.com/res/hashnode/image/upload/v1701668096906/3ccf29af-d94e-479a-aebd-664c390e4ba3.png align="center")

## Exécuter et tester l'application

À ce stade, lancez l'application sur un simulateur iOS ou un émulateur Android. Interagissez avec l'écran et appuyez sur les boutons qui déclenchent des exceptions. Même si l'application plante ou affiche une erreur, Crashlytics enregistrera silencieusement les détails et les enverra à Firebase une fois que l'application aura redémarré et retrouvé une connectivité réseau.

Les crashs mettent généralement quelques minutes à apparaître dans la console Firebase. Accédez à votre projet dans la console, puis allez dans **Release & Monitor > Crashlytics**. Vous y verrez un tableau de bord répertoriant tous les crashs enregistrés, avec les traces de pile (stack traces), les informations sur l'appareil et la fréquence d'occurrence. Les captures d'écran ci-dessous montrent ce que vous pourrez voir sur Crashlytics.

![Tableau de bord Crashlytics](https://cdn.hashnode.com/res/hashnode/image/upload/v1701668003651/e43c9e64-7a64-4d7b-a94f-2f908f2c76b9.png align="center")

![Vérification des logs](https://cdn.hashnode.com/res/hashnode/image/upload/v1701668011519/354c38af-f263-4de1-9896-f6e2dc16167c.png align="center")

![Visualisation des données](https://cdn.hashnode.com/res/hashnode/image/upload/v1701668015513/3448cdaa-22eb-4cdb-8fad-07694ac6a0c9.png align="center")

![Log détaillé de l'erreur](https://cdn.hashnode.com/res/hashnode/image/upload/v1701668020390/877dee08-c182-4ec8-beca-c3c1dc27692a.png align="center")

![Trace de pile de l'erreur](https://cdn.hashnode.com/res/hashnode/image/upload/v1701668024117/a2335fcc-4e56-438c-9d88-e37d98ca051c.png align="center")

## Comprendre le tableau de bord Crashlytics

Le tableau de bord Crashlytics est plus qu'une simple liste de crashs. Il regroupe les problèmes afin que vous puissiez voir combien d'utilisateurs sont affectés par un bogue spécifique. Il met en évidence les tendances, par exemple si un crash particulier est nouveau, en augmentation ou en diminution. Il s'intègre également aux alertes, vous permettant d'être averti lorsqu'un problème grave affecte une partie importante de vos utilisateurs.

Cela signifie que vous n'apprenez pas seulement que votre application a planté, vous obtenez également des informations exploitables pour hiérarchiser les bogues nécessitant une attention immédiate.

## Firebase Crashlytics avancé dans Flutter : aller au-delà des bases

Une fois que Crashlytics est intégré avec succès dans votre application Flutter, l'étape suivante consiste à tirer pleinement parti de ses fonctionnalités avancées. Bien que la capture des crashs soit utile, le débogage en conditions réelles nécessite souvent du contexte, des informations plus approfondies et des stratégies de gestion des erreurs qui vont au-delà du simple fait de savoir qu'une application a échoué. Explorons ces concepts avancés.

### Comment enregistrer les erreurs non fatales

Tous les problèmes d'une application ne conduisent pas à un crash. Parfois, vous rencontrerez des erreurs récupérables, comme l'échec d'un appel d'API, un problème d'analyse de données (parsing) ou une action utilisateur entraînant un comportement inattendu. Ces problèmes ne font pas planter votre application mais affectent tout de même l'expérience utilisateur. Crashlytics vous permet de les enregistrer en tant qu' **erreurs non fatales**.

Dans Flutter, vous pouvez utiliser :

```dart
try {
  // Code susceptible d'échouer
  final result = int.parse("invalid_number");
} catch (e, stack) {
  FirebaseCrashlytics.instance.recordError(
    e,
    stack,
    fatal: false,
    reason: 'Échec du parsing du nombre dans la configuration du profil',
  );
}
```

Ici, le flag `fatal: false` garantit que l'erreur est enregistrée sans être traitée comme un crash complet de l'application. Le paramètre facultatif `reason` fournit un contexte supplémentaire lisible par l'homme dans le tableau de bord Crashlytics. Cette fonctionnalité est inestimable pour suivre les défaillances silencieuses qui dégradent les performances sans nécessairement arrêter votre application.

### Comment ajouter des clés personnalisées pour le contexte

L'un des défis du débogage des crashs en production est de reproduire le problème. Une trace de pile seule ne vous en dit souvent pas assez sur le parcours de l'utilisateur. Les clés personnalisées vous permettent d'attacher des métadonnées supplémentaires aux rapports Crashlytics, telles que l'état de l'application de l'utilisateur, ses préférences ou la fonctionnalité qu'il utilisait lors du crash.

Par exemple :

```dart
FirebaseCrashlytics.instance.setCustomKey('screen', 'CheckoutScreen');
FirebaseCrashlytics.instance.setCustomKey('cart_items', 3);
FirebaseCrashlytics.instance.setCustomKey('payment_method', 'Card');
```

Avec ces clés définies, tout crash ou erreur non fatale survenant alors que l'utilisateur est sur l'écran de paiement portera ce contexte. Lorsque vous ouvrirez le rapport dans la console Firebase, vous verrez immédiatement ces valeurs, ce qui facilite considérablement le débogage.

### Comment enregistrer des événements personnalisés et des fils d'Ariane

En plus des clés personnalisées, Crashlytics vous permet d'enregistrer des messages personnalisés qui agissent comme des **fils d'Ariane** (breadcrumbs). Ce sont de petits logs qui vous indiquent ce que faisait l'application avant un crash.

```dart
FirebaseCrashlytics.instance.log('L\'utilisateur a appuyé sur le bouton "Passer la commande"');
FirebaseCrashlytics.instance.log('Requête API démarrée : /checkout');
FirebaseCrashlytics.instance.log('Processus de paiement initialisé');
```

Si un crash survient par la suite, vous disposerez d'une trace d'événements expliquant la séquence ayant mené à l'échec. C'est souvent la pièce manquante pour diagnostiquer des crashs complexes.

### Comment associer les crashs aux utilisateurs

Crashlytics prend en charge les **identifiants utilisateur**, vous permettant de lier les crashs à des utilisateurs spécifiques. Bien que vous deviez éviter de stocker des données sensibles, vous pouvez attacher en toute sécurité des identifiants uniques tels que des ID utilisateur, des e-mails ou des noms d'utilisateur.

```dart
FirebaseCrashlytics.instance.setUserIdentifier('user_12345');
```

Grâce à cela, vous pouvez rechercher si des utilisateurs ou des groupes d'utilisateurs spécifiques sont affectés de manière disproportionnée par un bogue. Cela aide également les équipes de support client à lier rapidement les rapports de bogues des utilisateurs aux données réelles dans Crashlytics.

### Comment assurer une symbolisation correcte

Lorsque vous exécutez votre application en mode debug, les traces de pile sont lisibles par l'homme. Mais dans les versions de production (release), en particulier sur iOS et Android, les traces de pile peuvent être obscurcies ou dépouillées de leurs symboles. La symbolisation est le processus consistant à mapper ces traces dépouillées vers des noms de méthodes et de classes significatifs.

**Sur iOS**, vous devrez télécharger les fichiers dSYM (fichiers de symboles de débogage) vers Firebase. Ces fichiers sont générés lorsque vous compilez votre application iOS pour la production. Vous pouvez automatiser le téléchargement en ajoutant un script d'exécution (Run Script) dans Xcode sous les paramètres de build de votre projet :

```bash
"${PODS_ROOT}/FirebaseCrashlytics/upload-symbols" \
-gsp "${PROJECT_DIR}/Runner/GoogleService-Info.plist" \
-p ios "${DWARF_DSYM_FOLDER_PATH}/${DWARF_DSYM_FILE_NAME}"
```

Cela garantit que chaque fois que vous créez une version de production, les fichiers de symboles sont automatiquement téléchargés sur Firebase.

**Sur Android**, si vous utilisez ProGuard ou R8 pour la réduction de code et l'offuscation, vous devrez télécharger les fichiers de mapping. Dans votre fichier `app/build.gradle`, activez le plugin Gradle Crashlytics :

```bash
apply plugin: 'com.google.firebase.crashlytics'
```

Ce plugin se charge de télécharger automatiquement les fichiers de mapping lorsque vous compilez une version de production.

Sans symbolisation, vos rapports de crash contiendront des traces de pile illisibles, rendant le débogage presque impossible. Assurer un téléchargement correct des symboles est critique pour une surveillance de niveau production.

### Comment contrôler la collecte des données

Dans certains cas, par exemple pour se conformer au RGPD ou à d'autres lois sur la confidentialité des données, vous souhaiterez peut-être contrôler quand Crashlytics commence à collecter des données. Flutter vous permet d'activer ou de désactiver la collecte de manière dynamique :

```dart
await FirebaseCrashlytics.instance.setCrashlyticsCollectionEnabled(false);
```

Vous pouvez l'activer une fois que l'utilisateur a donné son consentement. Cette flexibilité est particulièrement utile dans les régions ayant des exigences strictes en matière de confidentialité des utilisateurs.

## Bonnes pratiques pour la production

1. **Tester avant la sortie** : Déclenchez toujours des crashs en mode debug et confirmez qu'ils apparaissent dans le tableau de bord Crashlytics avant de déployer votre application.
    
2. **Utiliser largement les logs non fatals** : De nombreux problèmes silencieux peuvent être capturés ainsi avant qu'ils ne se transforment en crashs généralisés.
    
3. **Automatiser le téléchargement des symboles** : Assurez-vous que votre CI/CD ou votre pipeline de build télécharge systématiquement les fichiers dSYM (iOS) et de mapping (Android).
    
4. **Ajouter du contexte avec des clés et des logs personnalisés** : Plus vous attachez de contexte, plus vite vous pourrez reproduire et corriger les bogues.
    
5. **Respecter la vie privée** : Ne consignez jamais d'informations personnellement identifiables ou sensibles.
    

## Conclusion

L'intégration de Firebase Crashlytics dans une application Flutter est un processus simple, mais son impact est massif. En fournissant des rapports de crash en temps réel et des analyses détaillées, Crashlytics vous aide à maintenir la stabilité, à instaurer la confiance des utilisateurs et, en fin de compte, à offrir une meilleure expérience applicative. De la configuration du projet Firebase à la capture des erreurs synchrones et asynchrones, nous avons passé en revue tout ce dont vous avez besoin pour commencer.

Crashlytics va bien au-delà du simple rapport de crash. En exploitant des fonctionnalités telles que l'enregistrement d'erreurs non fatales, les clés personnalisées, les fils d'Ariane et les identifiants utilisateur, vous pouvez transformer les données brutes de crash en informations significatives qui améliorent directement votre processus de débogage.

Avec une symbolisation appropriée en place, vous disposerez toujours de traces de pile lisibles, ce qui facilite grandement la correction des problèmes en production. Grâce à cette configuration avancée, Crashlytics devient non seulement un filet de sécurité, mais un élément central de votre flux de travail de développement, vous aidant à livrer des applications stables, à réagir rapidement aux problèmes et à instaurer la confiance avec vos utilisateurs.

La prochaine étape consiste à déployer votre application sur des appareils réels et à surveiller les crashs au fur et à mesure qu'ils se produisent sur le terrain. Au fil du temps, Crashlytics deviendra l'un de vos outils les plus précieux pour maintenir la qualité de votre application.

### **Références**

* Documentation Flutter – [Installer Flutter](https://docs.flutter.dev/get-started/install)
    
* Documentation Firebase – [Console Firebase](https://console.firebase.google.com/)
    
* Documentation Firebase – [Ajouter Firebase à votre application Flutter](https://firebase.google.com/docs/flutter/setup)
    
* Firebase Crashlytics pour Flutter – [Package firebase_crashlytics](https://pub.dev/packages/firebase_crashlytics)
    
* Firebase Core pour Flutter – [Package firebase_core](https://firebase.google.com/docs/flutter/setup)
    
* Documentation Firebase – [Présentation de Firebase Crashlytics](https://firebase.google.com/docs/flutter/setup)
    
* Documentation Firebase – [Télécharger les fichiers dSYM (iOS)](https://firebase.google.com/docs/crashlytics/get-deobfuscated-reports?platform=ios)
    
* Documentation Firebase – [Télécharger les fichiers de mapping ProGuard/R8 (Android)](https://firebase.google.com/docs/crashlytics/get-deobfuscated-reports?platform=android)
    
* Firebase CLI – [Installer et configurer la Firebase CLI](https://firebase.google.com/docs/cli)