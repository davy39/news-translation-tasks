---
title: How to Deploy a Flutter Web App to Firebase Hosting with GitHub Actions
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
seo_title: null
seo_desc: 'Deploying a Flutter web app can feel repetitive if you’re doing it manually
  every time. GitHub Actions automates this by continuously deploying your app to
  Firebase Hosting whenever you push code to your repository.

  This guide walks you through setti...'
---

Deploying a Flutter web app can feel repetitive if you’re doing it manually every time. GitHub Actions automates this by continuously deploying your app to Firebase Hosting whenever you push code to your repository.

This guide walks you through setting up Firebase Hosting, configuring GitHub Actions, and managing deployments. By the end, you’ll have a reliable CI/CD pipeline for your Flutter web project.

## **Table of Contents:**

1. [Prerequisites](#heading-prerequisites)
    
2. [Step 1: Set Up Firebase Hosting](#heading-step-1-set-up-firebase-hosting)
    
    * [Initialize Firebase in Your Project](#heading-initialize-firebase-in-your-project)
        
3. [Step 2: Configure Firebase Hosting](#heading-step-2-configure-firebase-hosting)
    
    * [Explanation:](#heading-explanation)
        
4. [Step 3: Add Firebase Config to Flutter](#heading-step-3-add-firebase-config-to-flutter)
    
    * [Explanation:](#heading-explanation-1)
        
5. [Step 4: Configure GitHub Actions](#heading-step-4-configure-github-actions)
    
    * [Explanation of Steps:](#heading-explanation-of-steps)
        
6. [Step 5: Set Up Firebase Token](#heading-step-5-set-up-firebase-token)
    
7. [Step 6: Validate & Monitor Deployment](#heading-step-6-validate-amp-monitor-deployment)
    
8. [Advanced Configurations](#heading-advanced-configurations)
    
    * [Custom Build](#heading-custom-build)
        
    * [Multiple Environments (Staging & Production)](#heading-multiple-environments-staging-amp-production)
        
    * [Cache Dependencies (Speed up builds)](#heading-cache-dependencies-speed-up-builds)
        
9. [Troubleshooting](#heading-troubleshooting)
    

## Prerequisites

Before diving in, make sure you have these ready:

**1\. Flutter Installed**: You can install Flutter from [flutter.dev](https://flutter.dev/), then confirm installation with:

```bash
flutter --version
```

**2\. Firebase CLI Installed:** The Firebase CLI lets you interact with Firebase Hosting. Install it via npm like this:

```bash
npm install -g firebase-tools
```

Check installation with:

```bash
firebase --version
```

**3\. A GitHub Repository:** Your Flutter project should be pushed to GitHub.

**4\. Firebase Project Created:** Go to [Firebase Console](https://console.firebase.google.com/), create a project, and enable Firebase Hosting.

## Step 1: Set Up Firebase Hosting

### Initialize Firebase in Your Project

Open your terminal and navigate to your project:

```bash
cd path/to/your/flutter/project
```

Initialize Firebase Hosting:

```bash
firebase init
```

During setup, you’ll need to provide some information:

1. **Hosting**: Select Firebase Hosting.
    
2. **Public Directory**: Enter `build/web` (this is where Flutter outputs web builds).
    
3. **Single-Page App**: Select **Yes** (rewrites all routes to `/index.html`).
    
4. **Automatic Builds**: You can skip since we’ll configure GitHub Actions manually.
    

## Step 2: Configure Firebase Hosting

A file called `firebase.json` will be created. Ensure it looks like this:

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

1. `hosting.public` tells Firebase where to find your built app (`build/web`).
    
2. `ignore` files Firebase should not upload (hidden files, config files, `node_modules`).
    

You may also see a `.firebaserc` file for project aliasing:

```json
{
  "projects": {
    "default": "your-project-id"
  }
}
```

This links your local project to your Firebase project ID.

## Step 3: Add Firebase Config to Flutter

When you connect Firebase to Flutter (via the `flutterfire` CLI), it generates a file like `firebase_options.dart`.

In your `main.dart`, initialize Firebase:

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

1. `WidgetsFlutterBinding.ensureInitialized()` ensures that the Flutter engine is ready before Firebase initializes.
    
2. `Firebase.initializeApp()` connects your app to Firebase using the auto-generated options.
    

## Step 4: Configure GitHub Actions

We’ll now create a workflow that automatically builds and deploys your Flutter web app.

Create a file in your repo: `.github/workflows/firebase-hosting.yml`

```yaml
name: Deploy to Firebase Hosting

on:
  push:
    branches:
      - main  # Deploy only when code is pushed to main
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

Here’s what’s going on in this code:

1. **Checkout Repository**: Pulls your code into the runner.
    
2. **Set up Flutter**: Installs the specified Flutter version.
    
3. **Install Dependencies**: Runs `flutter pub get`.
    
4. **Build Flutter Web**: Builds the release version of your web app.
    
5. **Set up Node.js**: Needed for Firebase CLI.
    
6. **Install Firebase CLI**: Installs Firebase deploy tool.
    
7. **Deploy to Firebase Hosting**: Deploys the built files to Firebase.
    

## Step 5: Set Up Firebase Token

GitHub needs a token to authenticate with Firebase.

Run this locally:

```bash
firebase login:ci
```

Then copy the token shown.

Next, go to your **GitHub Repository → Settings → Secrets and Variables → Actions.**

Create a new secret named: `FIREBASE_TOKEN` and paste in the token you copied. This keeps your credentials safe.

## Step 6: Validate & Monitor Deployment

Commit the workflow file like this:

```bash
git add .github/workflows/firebase-hosting.yml
git commit -m "Setup GitHub Actions for Firebase Hosting"
git push origin main
```

Go to your GitHub repo, select the Actions tab, and then watch the workflow run. You will see an interface that looks like these images:

![work flow in running in progress](https://cdn.hashnode.com/res/hashnode/image/upload/v1724583714171/e9e6e064-cfb2-4597-84c9-ae5970c034d2.png align="center")

![work flow completed](https://cdn.hashnode.com/res/hashnode/image/upload/v1724752407403/aa243495-a2b8-4d2d-a62b-2691d0cf4f21.png align="center")

Once it’s successful, go to:

`https://your-project-id.web.app`

`https://your-project-id.firebaseapp.com`

## Advanced Configurations

### Custom Build

If you need a specific renderer (for example, HTML instead of CanvasKit):

```yaml
run: flutter build web --release --web-renderer html
```

### Multiple Environments (Staging & Production)

```yaml
run: firebase deploy --only hosting --project ${{ secrets.FIREBASE_PROJECT }}
```

Define `FIREBASE_PROJECT` as a secret for each environment.

### Cache Dependencies (Speed up builds)

```yaml
- name: Cache Flutter Dependencies
  uses: actions/cache@v3
  with:
    path: ~/.pub-cache
    key: ${{ runner.os }}-pub-cache-${{ github.sha }}
    restore-keys: |
      ${{ runner.os }}-pub-cache-
```

## Troubleshooting

You might encounter a few common issues. Her are some quick fixes to help you deal with them:

| Issue | Fix |
| --- | --- |
| **No active project** | Run `firebase use --add` locally and check `.firebaserc`. |
| **Node.js version mismatch** | Ensure `node-version: '18'` in workflow. |
| **Firebase CLI errors** | Reinstall with `npm install -g firebase-tools`. |
| **Deprecated warnings in index.html** | Update to latest Flutter web template. |

## Wrapping Up

By integrating Firebase Hosting with GitHub Actions, you now have a **CI/CD pipeline** for your Flutter web app.

Every push to `main` automatically triggers a build and deploy, keeping your app live with zero manual effort.

To dive deeper, check:

1. [Flutter Web Docs](https://docs.flutter.dev/platform-integration/web)
    
2. [Firebase Hosting Docs](https://firebase.google.com/docs/hosting)
    
3. [GitHub Actions Docs](https://docs.github.com/actions)
