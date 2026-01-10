---
title: Comment déployer une application Web Flutter sur Firebase Hosting avec GitHub
  Actions
subtitle: ''
author: Atuoha Anthony
co_authors: []
series: null
date: '2025-08-20T16:40:24.336Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-a-flutter-web-app-to-firebase-hosting-with-github-actions
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1755708006335/0ab99f10-4df5-4fbf-b293-6a6fef1bcade.png
tags:
- name: Flutter
  slug: flutter
- name: flutter-aware
  slug: flutter-aware
seo_title: Comment déployer une application Web Flutter sur Firebase Hosting avec
  GitHub Actions
seo_desc: 'Deploying a Flutter web app can feel repetitive if you’re doing it manually
  every time. GitHub Actions automates this by continuously deploying your app to
  Firebase Hosting whenever you push code to your repository.

  This guide walks you through setti...'
---

Le déploiement d'une application web Flutter peut sembler répétitif si vous le faites manuellement à chaque fois. GitHub Actions automatise cela en déployant continuellement votre application sur Firebase Hosting dès que vous poussez du code vers votre dépôt.

Ce guide vous accompagne dans la configuration de Firebase Hosting, le paramétrage de GitHub Actions et la gestion des déploiements. À la fin, vous disposerez d'un pipeline CI/CD fiable pour votre projet web Flutter.

## **Table des matières :**

1. [Prérequis](#heading-prerequisites)
    
2. [Étape 1 : Configurer Firebase Hosting](#heading-etape-1-configurer-firebase-hosting)
    
    * [Initialiser Firebase dans votre projet](#heading-initialiser-firebase-dans-votre-projet)
        
3. [Étape 2 : Configurer Firebase Hosting](#heading-etape-2-configurer-firebase-hosting)
    
    * [Explication :](#heading-explication)
        
4. [Étape 3 : Ajouter la configuration Firebase à Flutter](#heading-etape-3-ajouter-la-configuration-firebase-a-flutter)
    
    * [Explication :](#heading-explication-1)
        
5. [Étape 4 : Configurer GitHub Actions](#heading-etape-4-configurer-github-actions)
    
    * [Explication des étapes :](#heading-explication-des-etapes)
        
6. [Étape 5 : Configurer le jeton Firebase](#heading-etape-5-configurer-le-jeton-firebase)
    
7. [Étape 6 : Valider et surveiller le déploiement](#heading-etape-6-valider-et-surveiller-le-deploiement)
    
8. [Configurations avancées](#heading-configurations-avancees)
    
    * [Build personnalisé](#heading-build-personnalise)
        
    * [Environnements multiples (Staging & Production)](#heading-environnements-multiples-staging-amp-production)
        
    * [Mise en cache des dépendances (Accélérer les builds)](#heading-mise-en-cache-des-dependances-accelerer-les-builds)
        
9. [Dépannage](#heading-depannage)
    

## Prérequis

Avant de commencer, assurez-vous d'avoir ces éléments prêts :

**1\. Flutter installé** : Vous pouvez installer Flutter depuis [flutter.dev](https://flutter.dev/), puis confirmer l'installation avec :

```bash
flutter --version
```

**2\. Firebase CLI installé :** La Firebase CLI vous permet d'interagir avec Firebase Hosting. Installez-la via npm comme ceci :

```bash
npm install -g firebase-tools
```

Approuvez l'installation avec :

```bash
firebase --version
```

**3\. Un dépôt GitHub :** Votre projet Flutter doit être poussé sur GitHub.

**4\. Un projet Firebase créé :** Allez sur la [Console Firebase](https://console.firebase.google.com/), créez un projet et activez Firebase Hosting.

## Étape 1 : Configurer Firebase Hosting

### Initialiser Firebase dans votre projet

Ouvrez votre terminal et naviguez vers votre projet :

```bash
cd chemin/vers/votre/projet/flutter
```

Initialisez Firebase Hosting :

```bash
firebase init
```

Pendant la configuration, vous devrez fournir quelques informations :

1. **Hosting** : Sélectionnez Firebase Hosting.
    
2. **Public Directory** : Entrez `build/web` (c'est là que Flutter génère les builds web).
    
3. **Single-Page App** : Sélectionnez **Yes** (réécrit toutes les routes vers `/index.html`).
    
4. **Automatic Builds** : Vous pouvez ignorer cette étape car nous allons configurer GitHub Actions manuellement.
    

## Étape 2 : Configurer Firebase Hosting

Un fichier nommé `firebase.json` sera créé. Assurez-vous qu'il ressemble à ceci :

```json
{
  "hosting": {
    "public": "build/web",
    "ignore": [
      "firebase.json",
      "**/.*",
      "**/node_modules/**"
    ]
  }
}
```

### Explication :

1. `hosting.public` indique à Firebase où trouver votre application compilée (`build/web`).
    
2. `ignore` liste les fichiers que Firebase ne doit pas télécharger (fichiers cachés, fichiers de configuration, `node_modules`).
    

Vous pourriez également voir un fichier `.firebaserc` pour l'aliasing du projet :

```json
{
  "projects": {
    "default": "votre-id-projet-firebase"
  }
}
```

Ceci lie votre projet local à votre ID de projet Firebase.

## Étape 3 : Ajouter la configuration Firebase à Flutter

Lorsque vous connectez Firebase à Flutter (via la CLI `flutterfire`), cela génère un fichier comme `firebase_options.dart`.

Dans votre `main.dart`, initialisez Firebase :

```dart
import 'package:flutter/material.dart';
import 'package:firebase_core/firebase_core.dart';
import 'firebase_options.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp(
    options: DefaultFirebaseOptions.currentPlatform,
  );
  runApp(MyApp());
}
```

### Explication :

1. `WidgetsFlutterBinding.ensureInitialized()` garantit que le Framework Flutter est prêt avant l'initialisation de Firebase.
    
2. `Firebase.initializeApp()` connecte votre application à Firebase en utilisant les options générées automatiquement.
    

## Étape 4 : Configurer GitHub Actions

Nous allons maintenant créer un workflow qui construit et déploie automatiquement votre application web Flutter.

Créez un fichier dans votre dépôt : `.github/workflows/firebase-hosting.yml`

```yaml
name: Deploy to Firebase Hosting

on:
  push:
    branches:
      - main  # Déploie uniquement lors d'un push sur main
  pull_request:
    branches:
      - main

jobs:
  build_and_deploy:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout Repository
      uses: actions/checkout@v2

    - name: Set up Flutter
      uses: subosito/flutter-action@v3
      with:
        flutter-version: '3.24.1'

    - name: Install Dependencies
      run: flutter pub get

    - name: Build Flutter Web
      run: flutter build web --release

    - name: Set up Node.js
      uses: actions/setup-node@v3
      with:
        node-version: '18'

    - name: Install Firebase CLI
      run: npm install -g firebase-tools

    - name: Deploy to Firebase Hosting
      run: firebase deploy --only hosting --project <firebase-project-id>
      env:
        FIREBASE_TOKEN: ${{ secrets.FIREBASE_TOKEN }}
```

### Explication des étapes :

1. **Checkout Repository** : Récupère votre code dans le runner.
    
2. **Set up Flutter** : Installe la version spécifiée de Flutter.
    
3. **Install Dependencies** : Exécute `flutter pub get`.
    
4. **Build Flutter Web** : Construit la version release de votre application web.
    
5. **Set up Node.js** : Nécessaire pour la Firebase CLI.
    
6. **Install Firebase CLI** : Installe l'outil de déploiement Firebase.
    
7. **Deploy to Firebase Hosting** : Déploie les fichiers compilés sur Firebase.
    

## Étape 5 : Configurer le jeton Firebase

GitHub a besoin d'un jeton (token) pour s'authentifier auprès de Firebase.

Exécutez ceci localement :

```bash
firebase login:ci
```

Copiez ensuite le jeton affiché.

Ensuite, allez dans votre **Dépôt GitHub → Settings → Secrets and Variables → Actions.**

Créez un nouveau secret nommé : `FIREBASE_TOKEN` et collez le jeton que vous avez copié. Cela protège vos identifiants.

## Étape 6 : Valider et surveiller le déploiement

Effectuez un Commit du fichier de workflow comme ceci :

```bash
git add .github/workflows/firebase-hosting.yml
git commit -m "Setup GitHub Actions for Firebase Hosting"
git push origin main
```

Allez sur votre dépôt GitHub, sélectionnez l'onglet **Actions**, puis observez l'exécution du workflow. Vous verrez une interface similaire à ces images :

![workflow en cours d'exécution](https://cdn.hashnode.com/res/hashnode/image/upload/v1724583714171/e9e6e064-cfb2-4597-84c9-ae5970c034d2.png align="center")

![workflow terminé](https://cdn.hashnode.com/res/hashnode/image/upload/v1724752407403/aa243495-a2b8-4d2d-a62b-2691d0cf4f21.png align="center")

Une fois réussi, allez sur :

`https://votre-id-projet.web.app`

`https://votre-id-projet.firebaseapp.com`

## Configurations avancées

### Build personnalisé

Si vous avez besoin d'un moteur de rendu spécifique (par exemple, HTML au lieu de CanvasKit) :

```yaml
run: flutter build web --release --web-renderer html
```

### Environnements multiples (Staging & Production)

```yaml
run: firebase deploy --only hosting --project ${{ secrets.FIREBASE_PROJECT }}
```

Définissez `FIREBASE_PROJECT` comme un secret pour chaque environnement.

### Mise en cache des dépendances (Accélérer les builds)

```yaml
- name: Cache Flutter Dependencies
  uses: actions/cache@v3
  with:
    path: ~/.pub-cache
    key: ${{ runner.os }}-pub-cache-${{ github.sha }}
    restore-keys: |
      ${{ runner.os }}-pub-cache-
```

## Dépannage

Vous pourriez rencontrer quelques problèmes courants. Voici quelques solutions rapides pour vous aider :

| Problème | Solution |
| --- | --- |
| **No active project** | Exécutez `firebase use --add` localement et vérifiez `.firebaserc`. |
| **Node.js version mismatch** | Assurez-vous d'avoir `node-version: '18'` dans le workflow. |
| **Firebase CLI errors** | Réinstallez avec `npm install -g firebase-tools`. |
| **Deprecated warnings in index.html** | Mettez à jour vers le dernier template web Flutter. |

## Conclusion

En intégrant Firebase Hosting avec GitHub Actions, vous disposez désormais d'un **pipeline CI/CD** pour votre application web Flutter.

Chaque push sur `main` déclenche automatiquement un build et un déploiement, maintenant votre application en ligne sans effort manuel.

Pour aller plus loin, consultez :

1. [Documentation Flutter Web](https://docs.flutter.dev/platform-integration/web)
    
2. [Documentation Firebase Hosting](https://firebase.google.com/docs/hosting)
    
3. [Documentation GitHub Actions](https://docs.github.com/actions)