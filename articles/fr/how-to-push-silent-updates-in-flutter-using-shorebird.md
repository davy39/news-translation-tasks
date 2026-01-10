---
title: Comment publier des mises à jour silencieuses dans Flutter en utilisant Shorebird
subtitle: ''
author: Atuoha Anthony
co_authors: []
series: null
date: '2025-08-01T15:57:59.733Z'
originalURL: https://freecodecamp.org/news/how-to-push-silent-updates-in-flutter-using-shorebird
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1754063853545/725d429a-1bc1-40af-b089-3f742879a9bb.png
tags:
- name: Flutter
  slug: flutter
- name: flutter-aware
  slug: flutter-aware
- name: '#shorebird'
  slug: shorebird
seo_title: Comment publier des mises à jour silencieuses dans Flutter en utilisant
  Shorebird
seo_desc: Imagine you've just launched a major feature. Your app is climbing the charts,
  but then the first bug report arrives. It's a critical payment validation error.
  The fix is a single line of Dart code, but now you face the dreaded app store review
  queue...
---

Imaginez que vous venez de lancer une fonctionnalité majeure. Votre application grimpe dans les charts, mais puis le premier rapport de bug arrive. Il s'agit d'une erreur critique de validation de paiement. La correction est une seule ligne de code Dart, mais vous devez maintenant faire face à la redoutable file d'attente de révision de l'app store, des heures, voire des jours de retard, alors que vos utilisateurs et vos revenus sont impactés.

Et si vous pouviez contourner le store et livrer cette correction directement à vos utilisateurs en quelques minutes ?

C'est le pouvoir que Shorebird apporte à votre flux de travail Flutter. Il ne s'agit pas seulement de vitesse, mais aussi de contrôle, de fiabilité et de livrer une expérience utilisateur supérieure.

Ce guide vous mènera de novice à pro, couvrant tout, de la configuration de Shorebird à la mise en œuvre de stratégies de mise à jour robustes et de qualité production avec le package `upgrader`.

### Table des matières :

* [Prérequis](#heading-prerequisites)
    
* [Qu'est-ce que Shorebird ?](#heading-what-is-shorebird)
    
* [1\. Le "Pourquoi" : Quand corriger vs. Quand publier](#heading-1-the-why-when-to-patch-vs-when-to-release)
    
* [2\. Commencer : Installation et configuration du projet](#heading-2-getting-started-installation-amp-project-setup)
    
* [3\. Le flux de travail principal : Publication et correction](#heading-3-the-core-workflow-releasing-and-patching)
    
* [4\. Prendre le contrôle : Logique de mise à jour dans l'application Flutter](#heading-4-taking-control-in-app-update-logic-in-flutter)
    
* [5\. L'option nucléaire : Forcer les mises à jour avec upgrader](#heading-5-the-nuclear-option-forcing-updates-with-upgrader)
    
* [6\. Playbook du monde réel : Combiner Shorebird, Upgrader et Remote Config](#heading-6-real-world-playbook-combining-shorebird-upgrader-and-remote-config)
    
* [7\. Bonnes pratiques de qualité production](#heading-7-production-grade-best-practices)
    
* [8\. Sécurité, coût et limitations](#heading-8-security-cost-and-limitations)
    
* [Références](#heading-references)
    

### **Prérequis**

Avant de vous lancer, assurez-vous d'avoir les connaissances et les outils suivants configurés. Cela vous aidera à suivre le guide en douceur et à éviter les problèmes de configuration courants.

#### Connaissances et compétences

* **Connaissances fondamentales de Flutter :** Vous devez être à l'aise avec la création de projets Flutter, la gestion des packages avec `pubspec.yaml` et la compréhension du cycle de vie des widgets de base. Ce guide suppose que vous avez une application Flutter existante avec laquelle travailler.
    
* **Maîtrise de la ligne de commande :** Vous devez être à l'aise avec l'utilisation d'un terminal (comme Terminal sur macOS/Linux ou PowerShell sur Windows), car Shorebird est principalement un outil d'interface de ligne de commande (CLI). Cela inclut la navigation dans les répertoires et l'exécution de commandes.
    
* **Connaissances de base de Git et du contrôle de version :** La compréhension des concepts tels que les commits, les branches (`main`, `hotfix`) et la vérification du code est cruciale pour gérer les publications, créer des correctifs à partir d'états de code spécifiques et mettre en œuvre des stratégies de retour en arrière.
    

#### Outils et environnement

* **Un environnement de développement Flutter fonctionnel :**
    
    * La dernière version stable du **Flutter SDK**.
        
    * Un IDE configuré pour Flutter, tel que **VS Code** ou **Android Studio**.
        
* **Un compte Shorebird :**
    
    * Vous devrez vous inscrire pour un compte gratuit sur le [site web de Shorebird](https://shorebird.dev). La commande `shorebird login` nécessite cela.
        
* **Outils de construction spécifiques à la plateforme :**
    
    * **Pour Android :**
        
        * Une installation d'**Android Studio** et le **Android SDK** correspondant.
            
        * Un **keystore de signature** configuré (`key.jks`) et un fichier `key.properties` pour votre projet. Shorebird en a besoin pour créer des builds de publication signés et prêts pour la production (AAB).
            
    * **Pour iOS :**
        
        * Un ordinateur macOS avec **Xcode** installé. La construction pour iOS n'est pas possible sur Windows ou Linux.
            
        * Une adhésion active au **programme Apple Developer** est requise pour signer le code et publier des applications iOS.
            

#### Optionnel (mais recommandé pour la stratégie complète)

* **Un projet Firebase :** Pour mettre en œuvre la stratégie complète et réelle impliquant des mises à jour forcées et des indicateurs de fonctionnalités à distance, vous aurez besoin de :
    
    * Un projet Firebase lié à votre application Flutter.
        
    * Le service **Firebase Remote Config** activé.
        
    * Les packages `firebase_core` et `firebase_remote_config` ajoutés à votre `pubspec.yaml`.
        

## Qu'est-ce que Shorebird ?

Shorebird est un service de mise à jour de code spécifiquement conçu pour les applications Flutter. Il permet aux développeurs de livrer des correctifs critiques et même de nouvelles fonctionnalités directement sur les appareils des utilisateurs, en contournant le processus traditionnel de révision de l'app store. En essence, il permet les mises à jour "over-the-air" (OTA) pour les applications Flutter.

Cela signifie que, au lieu d'attendre des heures ou des jours pour l'approbation de l'app store pour une simple correction, vous pouvez déployer le changement presque instantanément, assurant une réponse beaucoup plus rapide aux problèmes, une réduction des temps d'arrêt pour les utilisateurs et un impact minimal sur les revenus. Cela vous donne un meilleur contrôle sur le cycle de vie de déploiement de votre application et aide à maintenir une expérience utilisateur plus fluide et plus fiable.

## 1\. Le "Pourquoi" : Quand corriger vs. Quand publier

Avant de plonger dans le "comment", il est crucial de comprendre le "quand/pourquoi". Toutes les mises à jour ne sont pas égales. Utiliser le bon outil pour le travail est la clé d'un cycle de développement stable et efficace.

#### Utilisez `shorebird patch` pour :

* **Corrections de bugs critiques :** Erreurs logiques dans votre code Dart (par exemple, erreurs de calcul, exceptions de pointeur nul, gestion incorrecte de l'état).
    
* **Ajustements mineurs de l'interface utilisateur :** Changer les couleurs, le texte ou la logique de mise en page sans ajouter de nouveaux actifs.
    
* **Bascules de fonctionnalités :** Pousser un changement de code qui active ou désactive une fonctionnalité que vous avez déjà construite et déployée.
    
* **Améliorations de performance :** Optimiser les algorithmes ou la logique de rendu au niveau Dart.
    

#### Utilisez une publication complète dans le store pour :

* **Changements de code natif :** Toutes les modifications des répertoires `android` ou `ios`.
    
* **Mises à jour de plugins/dépendances :** Ajout d'un nouveau package ou mise à jour d'un package existant dans `pubspec.yaml`, car cela modifie souvent le code natif ou inclut des binaires précompilés.
    
* **Changements d'actifs :** Ajout de nouvelles images, polices, fichiers JSON ou tout autre actif.
    
* **Publications de fonctionnalités majeures :** Lorsque la fonctionnalité ou l'interface utilisateur de l'application change de manière significative, il est bon de passer par une révision complète (et souvent requis par les politiques du store).
    

Pensez-y de cette manière : si le changement est **uniquement dans vos** fichiers `.dart` et ne touche pas `pubspec.yaml`, il est probablement correctible.

## 2\. Commencer : Installation et configuration du projet

Préparons votre environnement et votre projet pour Shorebird.

### Étape 1 : Installer le CLI Shorebird

Ouvrez votre terminal et exécutez le script d'installation officiel :

```bash
curl https://raw.githubusercontent.com/shorebirdtech/shorebird/main/install.sh -sSf | bash
```

### Étape 2 : Ajouter Shorebird à votre PATH

Pour utiliser la commande `shorebird` depuis n'importe où, ajoutez-la au fichier de configuration de votre shell (`.zshrc`, `.bashrc`, `.bash_profile`, etc.).

```bash
export PATH="$HOME/.shorebird/bin:$PATH"
```

Redémarrez votre terminal ou exécutez `source ~/.zshrc` (ou votre fichier respectif) pour que le changement prenne effet.

### Étape 3 : Vérifier et se connecter

Confirmez que l'installation a réussi et connectez-vous à votre compte Shorebird.

```bash
shorebird --version
shorebird login
```

Cela ouvrira une fenêtre de navigateur pour authentifier votre CLI avec le service Shorebird.

### Étape 4 : Initialiser Shorebird dans votre projet Flutter

Accédez au répertoire racine de votre projet Flutter et exécutez :

```bash
shorebird init
```

Cette commande est le point d'entrée de votre projet dans l'écosystème Shorebird. Voici ce qu'elle fait sous le capot :

1. Crée `shorebird.yaml` : Ce fichier stocke votre identifiant d'application unique. Commitez ce fichier dans le contrôle de version.
    
2. Modifie `pubspec.yaml` : Il ajoute automatiquement le package `shorebird_code_push`, qui est nécessaire pour que l'application communique avec les serveurs de Shorebird.
    
3. Met à jour `.gitignore` : Ajoute le répertoire `.shorebird/` pour empêcher les artefacts de construction temporaires d'être commis.
    

## 3\. Le flux de travail principal : Publication et correction

Le flux de travail de Shorebird repose sur un concept simple : vous créez une **version de base**, puis vous appliquez des **correctifs** à celle-ci.

### Étape 1 : Créer une version complète

Avant de pouvoir corriger quoi que ce soit, vous avez besoin d'une version complète de votre application construite avec Shorebird. Cette version sera soumise à l'App Store et au Play Store.

```bash
# Pour Android
shorebird release android

# Pour iOS
shorebird release ios
```

Cette commande compile votre application, télécharge les symboles nécessaires sur les serveurs de Shorebird afin qu'il puisse construire des correctifs plus tard, et génère l'artefact de version (AAB/IPA) pour que vous le téléchargiez dans les stores.

### Étape 2 : Créer et publier un correctif

Après avoir corrigé un bug ou fait un ajustement dans votre code Dart, vous pouvez créer un correctif. Shorebird comparera vos changements avec la version originale et créera une petite différence binaire efficace.

```bash
# Correctif de la dernière version Android
shorebird patch android

# Correctif de la dernière version iOS
shorebird patch ios
```

Ce correctif est immédiatement disponible pour les utilisateurs qui ont la version de base correspondante installée.

### Étape 3 : L'expérience utilisateur

Lorsque vous poussez un correctif, le processus est conçu pour être transparent :

1. **Téléchargement silencieux :** Au prochain lancement de l'application, le SDK `shorebird_code_push` vérifie la présence d'un nouveau correctif. Si un correctif est trouvé, il est téléchargé silencieusement en arrière-plan.
    
2. **Appliqué au prochain redémarrage :** Le correctif téléchargé est préparé et automatiquement appliqué la *prochaine fois* que l'utilisateur ferme et rouvre l'application. Cela garantit que leur session actuelle n'est pas interrompue.
    

## 4\. Prendre le contrôle : Logique de mise à jour dans l'application Flutter

Pour une expérience plus contrôlée, vous pouvez utiliser le package `shorebird_code_push` pour gérer le processus de mise à jour dans votre application.

```dart
import 'package:shorebird_code_push/shorebird_code_push.dart';

final _shorebirdCodePush = ShorebirdCodePush();

// Vérifier la présence d'un nouveau correctif au démarrage de l'application.
void checkForUpdate() async {
  // Vérifier si un nouveau correctif est disponible.
  final isUpdateAvailable = await _shorebirdCodePush.isNewPatchAvailableForDownload();

  if (isUpdateAvailable) {
    // Optionnellement, vous pouvez afficher une boîte de dialogue à l'utilisateur ici.
    // par exemple, "Une mise à jour rapide est disponible. Elle sera appliquée au prochain redémarrage."
    
    // Télécharger le nouveau correctif.
    await _shorebirdCodePush.downloadUpdateIfAvailable();
  }
}

// Pour les mises à jour critiques, vous pouvez forcer un redémarrage immédiat.
void forceRestart() async {
  // Assurez-vous qu'un correctif est téléchargé et prêt à être installé.
  if (await _shorebirdCodePush.isNewPatchReadyToInstall()) {
    // Cela forcerait l'application à se fermer et à redémarrer avec le nouveau correctif.
    // À utiliser avec précaution, car c'est une expérience utilisateur perturbante.
    await _shorebirdCodePush.installUpdateAndRestart();
  }
}
```

Appelez `checkForUpdate()` dans votre fonction `main()` ou dans l'`initState` de votre écran principal.

## 5\. L'option nucléaire : Forcer les mises à jour avec `upgrader`

Parfois, un correctif Shorebird ne suffit pas. Pour les mises à jour critiques qui impliquent du code natif, de nouveaux actifs, ou si vous devez vous assurer que chaque utilisateur est sur la dernière version immédiatement, vous avez besoin d'un écran de mise à jour bloquant. Le package `upgrader` est parfait pour cela.

### Étape 1 : Ajouter la dépendance

```yaml
dependencies:
  upgrader: ^7.0.0
```

### Étape 2 : Implémenter l'interface utilisateur bloquante

Enveloppez votre `MaterialApp` avec le widget `UpgradeAlert` pour créer une boîte de dialogue bloquante qui ne peut pas être ignorée.

```dart
import 'package:flutter/material.dart';
import 'package:upgrader/upgrader.dart';

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    // Cette configuration crée un écran bloquant "doit être mis à jour".
    final upgrader = Upgrader(
      showIgnore: false,
      showLater: false,
      canDismissDialog: false,
      dialogStyle: UpgradeDialogStyle.material,
      shouldPopScope: () => false, // Empêche la navigation en arrière
    );

    return MaterialApp(
      home: UpgradeAlert(
        upgrader: upgrader,
        child: HomeScreen(), // L'écran principal de votre application
      ),
    );
  }
}
```

## 6\. Playbook du monde réel : Combiner Shorebird, Upgrader et Remote Config

Voici comment tout assembler pour une stratégie de mise à jour infaillible. Utilisons Firebase Remote Config comme notre "interrupteur d'urgence" à distance.

**Scénario :** La version `1.2.0` de votre application a un bug critique de paiement.

### **Le Playbook :**

1. **Corrigez le bug :** Corrigez l'erreur dans votre code Dart.
    
2. **Poussez un correctif Shorebird :**
    
    ```bash
    shorebird patch android --release-version 1.2.0+10 
    # Utilisez --release-version pour cibler une build spécifique
    ```
    
    Cela livre la correction rapidement et silencieusement aux utilisateurs actifs.
    
3. **Définissez un indicateur à distance :** Dans votre console Firebase Remote Config, créez un paramètre comme `force_update_for_version` et définissez sa valeur sur `"1.2.0"`.
    
4. **Implémentez la logique dans votre application :** Au démarrage de l'application, vérifiez cet indicateur *avant* d'afficher votre interface utilisateur principale.
    
    ```dart
    import 'package:firebase_remote_config/firebase_remote_config.dart';
    import 'package:package_info_plus/package_info_plus.dart';
    
    Future<void> main() async {
      // ... code d'initialisation ...
      
      // Obtenez la version actuelle de l'application
      final packageInfo = await PackageInfo.fromPlatform();
      final currentVersion = packageInfo.version;
    
      // Récupérez la configuration à distance
      final remoteConfig = FirebaseRemoteConfig.instance;
      await remoteConfig.fetchAndActivate();
      final forceUpdateVersion = remoteConfig.getString('force_update_for_version');
    
      // Vérifiez si cette version est signalée pour une mise à jour forcée
      if (currentVersion == forceUpdateVersion) {
        // Il s'agit d'une version "mauvaise". Affichez l'écran de mise à jour bloquant.
        runApp(ForcedUpdateApp());
      } else {
        // Cette version est correcte. Exécutez l'application normale et vérifiez la présence d'un correctif Shorebird.
        checkForUpdate(); // Votre fonction de vérification Shorebird
        runApp(MyApp());
      }
    }
    
    // Une application simple qui n'affiche que l'écran de mise à jour.
    class ForcedUpdateApp extends StatelessWidget {
      @override
      Widget build(BuildContext context) {
        return MaterialApp(
          home: UpgradeAlert(
            child: Scaffold(body: Center(child: Text('Vérification des mises à jour...'))),
          ),
        );
      }
    }
    ```
    

Cette stratégie double garantit que les utilisateurs qui n'ont pas encore reçu le correctif Shorebird sont toujours bloqués pour utiliser la version boguée et sont dirigés vers le store.

## 7\. Bonnes pratiques de qualité production

Avant de cliquer sur "correctif" en production, vous devez traiter Shorebird comme tout autre pipeline de publication : tester la build, la déployer par vagues, surveiller les métriques de plantage et automatiser les parties ennuyeuses. Voici quelques bonnes pratiques à suivre :

Tout d'abord, testez toujours les correctifs. Utilisez `shorebird preview` pour tester votre correctif sur un appareil local ou un émulateur avant de le déployer auprès des utilisateurs.

```bash
shorebird preview
```

Utilisez des déploiements par vagues avec des canaux. Ne poussez pas un correctif critique à 100 % des utilisateurs en une seule fois. La fonctionnalité "canaux" de Shorebird vous permet de déployer d'abord auprès d'un public `staging`.

```bash
# Poussez le correctif aux testeurs internes
shorebird patch android --channel=staging

# Après vérification, promouvez-le à tous les utilisateurs
shorebird promote --channel=staging --release-version 1.2.0+10
```

Vous devez également avoir un plan de retour en arrière si un correctif aggrave les choses. Dans ce cas, le moyen le plus rapide de le corriger est de **corriger vers l'avant**. Vérifiez le dernier commit connu comme bon depuis Git et exécutez à nouveau `shorebird patch`. Ce nouveau correctif écrasera le mauvais.

Et assurez-vous de tout surveiller. Pour cela, vous pouvez utiliser des outils comme Firebase Crashlytics ou Sentry pour surveiller les taux de plantage et la stabilité de l'application après la publication d'un correctif.

Enfin, il est utile d'automatiser avec CI/CD, et vous pouvez intégrer Shorebird directement dans votre pipeline CI/CD (par exemple, GitHub Actions). Stockez votre `SHOREBIRD_TOKEN` en tant que secret et utilisez des commandes comme `shorebird patch android --release-version <version> --force` pour automatiser les déploiements.

## 8\. Sécurité, coût et limitations

Il y a quelques autres choses que vous devez garder à l'esprit lorsque vous utilisez Shorebird.

Tout d'abord, toutes les communications avec les serveurs de Shorebird se font via TLS. Les correctifs sont signés cryptographiquement, et le SDK `shorebird_code_push` vérifie cette signature avant d'appliquer une mise à jour, garantissant qu'elle n'a pas été altérée.

Deuxièmement, Shorebird fonctionne sur un modèle freemium avec un niveau gratuit généreux. Les plans payants sont basés sur les utilisateurs actifs mensuels (MAU) et débloquent des fonctionnalités d'équipe. Vous pouvez consulter la page officielle des prix pour les détails actuels.

De plus, gardez à l'esprit qu'il y a certaines limitations que nous avons déjà abordées un peu : par exemple, Shorebird **ne corrige que le code Dart**. Vous ne pouvez pas mettre à jour les plugins natifs, ajouter/modifier des actifs, ou modifier le code natif (dossiers `android`/`ios`) avec un correctif. Ces changements nécessitent toujours une publication complète dans le store.

## Conclusion

Shorebird est un outil transformateur pour tout développeur Flutter sérieux. Il fait passer le processus de publication d'un cycle lent et monolithique à un processus dynamique et réactif.

En combinant les correctifs rapides de Shorebird avec une stratégie de mise à jour robuste utilisant `upgrader` et Remote Config, vous obtenez un contrôle sans précédent sur votre application de production. Vous pouvez corriger des bugs en quelques minutes, atténuer les risques et garder vos utilisateurs satisfaits – tout cela sans attendre l'app store.

### Références

**1\. Shorebird**

* [Site Web Officiel](https://shorebird.dev)
    
* [Documentation CLI](https://docs.shorebird.dev/cli)
    
* [SDK Code Push](https://pub.dev/packages/shorebird_code_push)
    

**2\. Package Upgrader**

* [Page Pub.dev](http://Pub.dev) [Page](https://pub.dev/packages/upgrader)
    
* [Dépôt GitHub](https://github.com/larryaasen/upgrader)
    

**3\. Outils et concepts de support**

* [Firebase Remote Config](https://firebase.google.com/docs/remote-config)
    
* [Version sémantique](https://semver.org)
    
* [Documentation CI/CD Flutter](https://docs.flutter.dev/testing/cd)