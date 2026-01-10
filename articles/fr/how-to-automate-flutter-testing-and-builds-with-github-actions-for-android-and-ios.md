---
title: Comment automatiser les tests et les builds Flutter avec GitHub Actions pour
  Android et iOS
subtitle: ''
author: Atuoha Anthony
co_authors: []
series: null
date: '2025-08-21T21:59:14.740Z'
originalURL: https://freecodecamp.org/news/how-to-automate-flutter-testing-and-builds-with-github-actions-for-android-and-ios
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1755808732085/6fdd754a-39d4-40d1-8dea-0eb16cc45063.png
tags:
- name: Flutter
  slug: flutter
- name: flutter-aware
  slug: flutter-aware
- name: github-actions
  slug: github-actions-1
seo_title: Comment automatiser les tests et les builds Flutter avec GitHub Actions
  pour Android et iOS
seo_desc: GitHub Actions is a CI/CD (Continuous Integration and Continuous Deployment)
  tool built directly into GitHub. It allows developers to define workflows, which
  are sequences of automated steps triggered by events such as pushing code, opening
  pull requ...
---

GitHub Actions est un outil de CI/CD (Intégration Continue et Déploiement Continu) directement intégré à GitHub. Il permet aux développeurs de définir des **workflows**, qui sont des séquences d'étapes automatisées déclenchées par des événements tels que le push de code, l'ouverture de pull requests ou la création de releases.

Pour les développeurs Flutter, GitHub Actions est un moyen puissant d'automatiser les tests, les builds et le déploiement sur plusieurs plateformes.

Ce guide vous accompagnera dans la configuration de GitHub Actions pour un projet Flutter, couvrant tout, des prérequis aux explications détaillées du workflow.

## Table des matières

1. [Pourquoi utiliser GitHub Actions dans le développement Flutter ?](#heading-pourquoi-utiliser-github-actions-dans-le-developpement-flutter)
    
2. [Prérequis](#heading-prerequis)
    
3. [Étape 1 : Créer un nouveau projet Flutter](#heading-etape-1-creer-un-nouveau-projet-flutter)
    
4. [Étape 2 : Pousser le projet sur GitHub](#heading-etape-2-pousser-le-projet-sur-github)
    
5. [Étape 3 : Créer un workflow GitHub Actions](#heading-etape-3-creer-un-workflow-github-actions)
    
    * [Déclencheurs](#heading-declencheurs)
        
    * [Jobs](#heading-jobs)
        
6. [Étape 4 : Générer et ajouter un token GitHub](#heading-etape-4-generer-et-ajouter-un-token-github)
    
7. [Étape 5 : Comprendre le workflow](#heading-etape-5-comprendre-le-workflow)
    
    * [Job de test Flutter](#heading-job-de-test-flutter)
        
    * [Job de build d'application iOS](#heading-job-de-build-d-application-ios)
        
    * [Job de build d'APK Android](#heading-job-de-build-d-apk-android)
        
8. [Étape 6 : Pousser et activer le workflow](#heading-etape-6-pousser-et-activer-le-workflow)
    
9. [Notes finales](#heading-notes-finales)
    

## Pourquoi utiliser GitHub Actions dans le développement Flutter ?

Les tests automatisés de GitHub Actions garantissent que toutes les modifications de code sont validées par des tests unitaires et d'intégration. L'intégration continue build automatiquement les applications Flutter pour confirmer que le nouveau code s'intègre correctement.

L'analyse de code et le linting peuvent s'exécuter automatiquement pour imposer un style et maintenir la qualité du code. Les releases automatisées simplifient le processus de packaging et de distribution des applications. Les workflows personnalisés peuvent être adaptés aux besoins spécifiques du projet. La collaboration est également améliorée car les développeurs peuvent voir les résultats du workflow directement dans les pull requests.

En introduisant GitHub Actions, les projets Flutter deviennent plus fiables, maintenables et efficaces.

## Prérequis

Avant de configurer GitHub Actions pour votre projet Flutter, assurez-vous d'avoir :

1. **Le SDK Flutter installé localement** pour pouvoir créer et tester le projet avant de le pousser sur GitHub.
    
2. **Git installé** pour gérer le contrôle de version et pousser votre projet sur GitHub.
    
3. **Un compte GitHub** et un **nouveau dépôt** créé pour votre projet Flutter.
    
4. **Une compréhension de base de la syntaxe YAML**, car les workflows sont définis dans des fichiers `.yml`.
    
5. **Un token d'accès personnel GitHub** (PAT) pour publier les builds, qui sera stocké en tant que secret de dépôt.
    

## Étape 1 : Créer un nouveau projet Flutter

Commencez par créer un nouveau projet Flutter et accédez-y :

```bash
flutter create gh_flutter
cd gh_flutter
```

Remplacez `gh_flutter` par le nom de projet de votre choix. Cela initialise un projet Flutter avec la structure et les dépendances par défaut.

## Étape 2 : Pousser le projet sur GitHub

Initialisez Git dans votre projet et poussez-le vers GitHub :

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin <repository_url>
git push -u origin main
```

Remplacez `<repository_url>` par l'URL du dépôt que vous avez créé sur GitHub. Cela lie votre projet Flutter local à GitHub, permettant à GitHub Actions de s'exécuter sur votre dépôt.

## Étape 3 : Créer un workflow GitHub Actions

À l'intérieur de votre projet, créez un fichier de configuration de workflow. Les workflows doivent être placés dans `.github/workflows/`. Créez un fichier nommé `ci.yml` :

```yaml
name: CI

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  flutter_test:
    name: Run Flutter Test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-java@v3
        with:
          distribution: 'temurin'
          java-version: '17'
      - uses: subosito/flutter-action@v2
        with:
          channel: 'stable'
      - run: flutter pub get
      - run: flutter --version
      - run: flutter analyze
      - run: flutter test

  build_iOSApp:
    name: Build Flutter App (iOS)
    needs: [flutter_test]
    runs-on: macos-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-java@v3
        with:
          distribution: 'temurin'
          java-version: '17'
      - uses: subosito/flutter-action@v2
        with:
          flutter-version: '3.19.0'
          dart-verion: '3.3.4'
          channel: 'stable'
      - run: flutter pub get
      - run: flutter clean
      - run: |
          flutter build ios --no-codesign
          cd build/ios/iphoneos
          mkdir Payload
          cd Payload
          ln -s ../Runner.app
          cd ..
          zip -r app.ipa Payload
          
  build_androidApk:
    name: Build Flutter App (Android)
    needs: [flutter_test]
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-java@v3
        with:
          distribution: 'temurin'
          java-version: '17'
      - uses: subosito/flutter-action@v2
        with:
          channel: 'stable'
      - run: flutter pub get
      - run: flutter clean
      - run: flutter build apk --debug
      - uses: ncipollo/release-action@v1
        with:
          artifacts: "build/app/outputs/apk/debug/*"
          tag: v1.0.${{ github.run_number}}
          token: ${{ secrets.TOKEN}}
```

Ce workflow est nommé `CI` et est destiné à l'**Intégration Continue** (exécution de tests et build d'applications automatiquement chaque fois que du code est poussé ou qu'une pull request est créée).

### **Déclencheurs**

Dans GitHub Actions, les **déclencheurs** (triggers) définissent les événements qui provoquent l'exécution d'un workflow. Pour ce workflow, il s'exécute automatiquement lorsque certains événements se produisent dans le dépôt. Plus précisément, il écoute :

1. `push` : Chaque fois que du nouveau code est poussé vers la branche `main`, le workflow démarre.
    
2. `pull_request` : Chaque fois qu'une pull request est ouverte ou mise à jour vers la branche `main`, le workflow démarre également.
    

Cela garantit que les mises à jour directes de la branche principale et les contributions via les pull requests sont validées et testées.

```yaml
on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main
```

Ce code exécute le workflow lorsque :

* Vous poussez des commits sur la branche `main`.
    
* Une pull request est ouverte ou mise à jour ciblant `main`.
    

### **Jobs**

Il y a 3 jobs dans le workflow :

**Job 1 :** `flutter_test` exécute les tests unitaires et l'analyse.

```yaml
jobs:
  flutter_test:
    runs-on: ubuntu-latest
```

Il utilise **Ubuntu** comme runner.

Voici les étapes qu'il suit :

1. Récupère le code :
    
    ```yaml
    - uses: actions/checkout@v3
    ```
    
    Télécharge votre dépôt dans le runner.
    
2. Configure Java (nécessaire pour les builds Flutter Android) :
    
    ```yaml
    - uses: actions/setup-java@v3
      with:
        distribution: 'temurin'
        java-version: '17'
    ```
    
3. Configure le SDK Flutter :
    
    ```yaml
    - uses: subosito/flutter-action@v2
      with:
        channel: 'stable'
    ```
    
    Cela installe le canal stable de Flutter.
    
4. Exécute les commandes :
    
    1. `flutter pub get` installe les dépendances.
        
    2. `flutter --version` vérifie la version installée de Flutter.
        
    3. `flutter analyze` analyse le code Dart pour détecter les erreurs.
        
    4. `flutter test` exécute les tests unitaires/de widgets.
        

Si ce job échoue, les jobs suivants ne s'exécuteront pas.

**Job 2** : `build_iOSApp` construit un fichier iOS `.ipa`.

```yaml
  build_iOSApp:
    needs: [flutter_test]
    runs-on: macos-latest

  steps:
  - uses: actions/checkout@v3

  - uses: subosito/flutter-action@v2
    with:
      flutter-version: '3.22.0'

  - name: Install CocoaPods dependencies
    run: |
      cd ios
      pod install

  - name: Build iOS App
    run: flutter build ipa --release --no-codesign
```

Ceci ne s'exécute qu'**après** que `flutter_test` a réussi et utilise un runner **macOS** (nécessaire pour les builds iOS).

Après avoir installé les dépendances CocoaPods, le workflow exécute `flutter build ipa --release --no-codesign`. Cette commande shell indique à Flutter d'empaqueter votre application iOS dans un fichier `.ipa` à l'intérieur du répertoire de build du runner. Le drapeau `--no-codesign` permet de builder sans identifiants de signature, ce qui est pratique pour les pipelines CI.

Voici les étapes qu'il suit :

1. Récupère le dépôt + configure Java (comme précédemment).
    
2. Configure Flutter mais cette fois-ci en fixant les versions :
    
    ```yaml
    flutter-version: '3.19.0'
    dart-verion: '3.3.4'   # faute de frappe : devrait être `dart-version`
    channel: 'stable'
    ```
    
3. Exécute le build :
    
    1. `flutter pub get` récupère les packages.
        
    2. `flutter clean` nettoie les anciens builds.
        
    3. `flutter build ios --no-codesign` build l'application iOS sans signature.
        
    4. Après le build :
        
        1. Va dans `build/ios/iphoneos`
            
        2. Crée un dossier `Payload` (nécessaire pour la structure IPA).
            
        3. Crée un lien symbolique de l'application `Runner.app` générée vers `Payload`.
            
        4. Compresse le dossier en `app.ipa`.
            

Résultat : Un fichier `.ipa` non signé.

**Job 3** : `build_androidApk` build un `.apk` Android de debug et le télécharge en tant qu'artefact de release.

```yaml
  build_androidApk:
    needs: [flutter_test]
    runs-on: ubuntu-latest
 
  steps:
  - uses: actions/checkout@v3

  - uses: subosito/flutter-action@v2
    with:
      flutter-version: '3.22.0'

  - name: Build Android APK
    run: flutter build apk --release

```

Ceci ne s'exécute qu'après la réussite des tests.

Pour Android, après avoir configuré l'environnement Flutter, le workflow appelle `flutter build apk --release`. Cette commande compile et empaquette l'application Android dans un fichier `.apk` prêt pour la distribution. Le fichier résultant est placé dans le répertoire `build/app/outputs/flutter-apk` du projet.

Voici les étapes qu'il suit :

1. Récupère le dépôt, configure Java et configure Flutter.
    
2. Exécute :
    
    1. `flutter pub get`
        
    2. `flutter clean`
        
    3. `flutter build apk --debug` crée un APK de debug.
        
3. Télécharge l'APK à l'aide de `ncipollo/release-action@v1` :
    
    ```yaml
    artifacts: "build/app/outputs/apk/debug/*"
    tag: v1.0.${{ github.run_number }}
    token: ${{ secrets.TOKEN }}
    ```
    
    1. Télécharge tous les APK de debug en tant qu'artefacts de release.
        
    2. Marque la release avec le tag `v1.0.<run_number>` (ex: `v1.0.5`).
        
    3. Utilise un **Token d'Accès Personnel** GitHub (`TOKEN`) stocké dans les secrets du dépôt.
        

## Étape 4 : Générer et ajouter un token GitHub

Le job de build Android publie les APK à l'aide de `release-action`. Pour s'authentifier, vous devez fournir un token d'accès personnel GitHub. Pour ce faire, allez dans **GitHub Settings → Developer settings → Personal access tokens**.

Générez un nouveau token avec les permissions `repo` et copiez-le immédiatement. Ensuite, allez dans votre dépôt → Settings → Secrets → New repository secret. Ajoutez le token avec le nom `TOKEN`.

Désormais, le workflow peut utiliser `${{ secrets.TOKEN }}` en toute sécurité.

## Étape 5 : Comprendre le workflow

Ce workflow est déclenché lorsque du code est poussé vers la branche `main` ou lorsqu'une pull request est ouverte contre celle-ci. Analysons-le :

### Job de test Flutter

* **Environnement :** S'exécute sur `ubuntu-latest`.
    

**Étapes :**

1. `actions/checkout@v3` récupère le code source.
    
2. `actions/setup-java@v3` installe Java, requis pour certains outils Flutter.
    
3. `subosito/flutter-action@v2` installe Flutter sur le runner.
    
4. `flutter pub get` installe les dépendances.
    
5. `flutter analyze` vérifie les problèmes de code.
    
6. `flutter test` exécute les cas de test.
    

Ce job garantit que votre code compile, passe le linting et n'a pas de tests échoués.

### Job de build d'application iOS

* **Environnement :** S'exécute sur `macos-latest` car les builds iOS nécessitent macOS.
    
* **Dépendances :** Ce job ne s'exécute que si `flutter_test` réussit (`needs: [flutter_test]`).
    

**Étapes :** Configuration similaire à la précédente, mais après avoir nettoyé les anciens builds avec `flutter clean`, il exécute `flutter build ios --no-codesign` pour construire une application iOS sans nécessiter de certificat de signature. Les commandes shell empaquettent l'application dans un fichier `.ipa`.

### Job de build d'APK Android

* **Environnement :** S'exécute sur `ubuntu-latest`.
    
* **Dépendances :** Dépend également de `flutter_test`.
    

**Étapes :**

1. Installe Flutter.
    
2. Exécute `flutter clean` puis construit l'APK Android.
    
3. Utilise `ncipollo/release-action@v1` pour télécharger l'APK en tant que release GitHub, taguée automatiquement avec une version telle que `v1.0.<run_number>`.
    

## Étape 6 : Pousser et activer le workflow

Enregistrez votre fichier sous `.github/workflows/ci.yml` et poussez les modifications :

```bash
git add .
git commit -m "Add GitHub Actions workflow"
git push
```

Lorsque vous poussez vos modifications sur GitHub, le fichier de workflow est automatiquement détecté. Pour confirmer qu'il s'exécute, ouvrez votre dépôt sur GitHub et cliquez sur l'onglet **Actions** en haut de la page. Vous verrez une liste des exécutions de workflow, chacune liée au message de commit qui l'a déclenchée.

Cliquez sur l'exécution la plus récente pour voir les détails. À l'intérieur, vous trouverez des jobs séparés pour les builds **Android** et **iOS**. Chaque job affichera son statut en temps réel :

1. Un **point jaune** avec « In progress » indique que le job est toujours en cours d'exécution.
    
2. Une **coche verte** avec « Success » signifie que le job s'est terminé avec succès.
    
3. Une **croix rouge** avec « Failed » signifie que quelque chose s'est mal passé.
    

De cette façon, vous pouvez immédiatement savoir si vos builds Android et iOS ont réussi ou si l'un d'eux nécessite votre attention.

![Running for Flutter Test](https://cdn.hashnode.com/res/hashnode/image/upload/v1701417493045/31e8f9db-b4b7-445c-ab6d-caa8cbc8dfdf.png align="center")

![Building for iOS](https://cdn.hashnode.com/res/hashnode/image/upload/v1701417512470/d27378ea-5bf2-487e-a0b0-9c2a9ffaa92e.png align="center")

![Building for Android](https://cdn.hashnode.com/res/hashnode/image/upload/v1701417526668/31b6e5c9-c43f-46ef-a25c-7f2321eda443.png align="center")

![Jobs completed](https://cdn.hashnode.com/res/hashnode/image/upload/v1701417477229/cbae6ba2-f51c-4f2a-81bc-cdb3345a5319.png align="center")

![Showcase 2 app releases on the right hand side with versions](https://cdn.hashnode.com/res/hashnode/image/upload/v1701439224779/7fb85ed3-00ae-4154-8032-ffeb9bb5e1b1.png align="center")

![Detailed app release versioning showcase](https://cdn.hashnode.com/res/hashnode/image/upload/v1701439234845/02c24d1e-09cd-4b4e-b9ea-fe96d4516f0c.png align="center")

## Notes finales

Avec cette configuration, vous avez maintenant :

* Des tests automatisés chaque fois que vous poussez ou ouvrez une pull request.
    
* Des builds iOS automatiques sur les runners macOS.
    
* Des builds Android automatiques avec des APK publiés sur GitHub.
    

Cela garantit que chaque modification est testée et que les builds sont générés de manière cohérente sans étapes manuelles.

Pour plus de détails, consultez la documentation officielle de GitHub Actions : [https://docs.github.com/en/actions](https://docs.github.com/en/actions).