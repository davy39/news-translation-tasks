---
title: How to Automate Flutter Testing and Builds with GitHub Actions for Android
  and iOS
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
seo_title: null
seo_desc: GitHub Actions is a CI/CD (Continuous Integration and Continuous Deployment)
  tool built directly into GitHub. It allows developers to define workflows, which
  are sequences of automated steps triggered by events such as pushing code, opening
  pull requ...
---

GitHub Actions is a CI/CD (Continuous Integration and Continuous Deployment) tool built directly into GitHub. It allows developers to define **workflows**, which are sequences of automated steps triggered by events such as pushing code, opening pull requests, or creating releases.

For Flutter developers, GitHub Actions is a powerful way to automate testing, builds, and deployment across multiple platforms.

This guide will walk you through setting up GitHub Actions for a Flutter project, covering everything from prerequisites to detailed explanations of the workflow.

## Table of Contents

1. [Why Use GitHub Actions in Flutter Development?](#heading-why-use-github-actions-in-flutter-development)
    
2. [Prerequisites](#heading-prerequisites)
    
3. [Step 1: Create a New Flutter Project](#heading-step-1-create-a-new-flutter-project)
    
4. [Step 2: Push the Project to GitHub](#heading-step-2-push-the-project-to-github)
    
5. [Step 3: Create a GitHub Actions Workflow](#heading-step-3-create-a-github-actions-workflow)
    
    * [Triggers](#heading-triggers)
        
    * [Jobs](#heading-jobs)
        
6. [Step 4: Generate and Add a GitHub Token](#heading-step-4-generate-and-add-a-github-token)
    
7. [Step 5: Understanding the Workflow](#heading-step-5-understanding-the-workflow)
    
    * [Flutter Test Job](#heading-flutter-test-job)
        
    * [iOS App Build Job](#heading-ios-app-build-job)
        
    * [Android APK Build Job](#heading-android-apk-build-job)
        
8. [Step 6: Push and Enable the Workflow](#heading-step-6-push-and-enable-the-workflow)
    
9. [Final Notes](#heading-final-notes)
    

## Why Use GitHub Actions in Flutter Development?

GitHub Actions automated testing ensures that all code changes are validated with unit and integration tests. Continuous integration builds Flutter apps automatically to confirm that new code integrates correctly.

Code analysis and linting can run automatically to enforce style and maintain code quality. Automated releases streamline the process of packaging and distributing apps. Custom workflows can be tailored to fit project-specific needs. Collaboration is also improved because developers can see workflow results directly in pull requests.

By introducing GitHub Actions, Flutter projects become more reliable, maintainable, and efficient.

## Prerequisites

Before setting up GitHub Actions for your Flutter project, make sure you have:

1. **Flutter SDK installed locally** so you can create and test the project before pushing to GitHub.
    
2. **Git installed** to manage version control and push your project to GitHub.
    
3. **A GitHub account** and a **new repository** created for your Flutter project.
    
4. **Basic understanding of YAML syntax**, since workflows are defined in `.yml` files.
    
5. **A GitHub personal access token** (PAT) for releasing builds, which will be stored as a repository secret.
    

## Step 1: Create a New Flutter Project

Start by creating a new Flutter project and navigating into it:

```bash
flutter create gh_flutter
cd gh_flutter
```

Replace `gh_flutter` with your preferred project name. This initializes a Flutter project with the default structure and dependencies.

## Step 2: Push the Project to GitHub

Initialize Git inside your project and push it to GitHub:

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin <repository_url>
git push -u origin main
```

Replace `<repository_url>` with the repository URL you created on GitHub. This links your local Flutter project to GitHub, allowing GitHub Actions to run on your repository.

## Step 3: Create a GitHub Actions Workflow

Inside your project, create a workflow configuration file. Workflows must be placed inside `.github/workflows/`. Create a file named `ci.yml`:

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

This workflow is named `CI` and is meant for **Continuous Integration** (running tests and building apps automatically whenever code is pushed or a pull request is created).

### **Triggers**

In GitHub Actions, **triggers** define the events that cause a workflow to run. For this workflow, it runs automatically when certain events happen in the repository. Specifically, it listens to:

1. `push`: Whenever new code is pushed to the `main` branch, the workflow will start.
    
2. `pull_request`: Whenever a pull request is opened or updated that targets the `main` branch, the workflow will also start.
    

This ensures that both direct updates to the main branch and contributions through pull requests are validated and tested.

```yaml
on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main
```

This code runs the workflow when:

* You push commits to the `main` branch.
    
* A pull request is opened or updated targeting `main`.
    

### **Jobs**

There are 3 jobs in the workflow:

**Job 1:** `flutter_test` runs unit tests and analysis.

```yaml
jobs:
  flutter_test:
    runs-on: ubuntu-latest
```

It uses **Ubuntu** as the runner.

Here are the steps it follows:

1. Checks out code:
    
    ```yaml
    - uses: actions/checkout@v3
    ```
    
    Downloads your repo into the runner.
    
2. Sets up Java (needed for Flutter Android builds):
    
    ```yaml
    - uses: actions/setup-java@v3
      with:
        distribution: 'temurin'
        java-version: '17'
    ```
    
3. Sets up Flutter SDK:
    
    ```yaml
    - uses: subosito/flutter-action@v2
      with:
        channel: 'stable'
    ```
    
    This installs the Flutter stable channel.
    
4. Runs commands:
    
    1. `flutter pub get` installs dependencies.
        
    2. `flutter --version` checks installed Flutter version.
        
    3. `flutter analyze` analyzes Dart code for errors.
        
    4. `flutter test` runs unit/widget tests.
        

If this job fails, later jobs won’t run.

**Job 2**: `build_iOSApp` builds an iOS `.ipa` file.

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

This runs only **after** `flutter_test` succeeds and uses **macOS** runner (needed for iOS builds).

After installing CocoaPods dependencies, the workflow executes `flutter build ipa --release --no-codesign`. This shell command tells Flutter to package your iOS app into an `.ipa` file inside the runner’s build directory. The `--no-codesign` flag allows building without signing credentials, which is convenient for CI pipelines.

Here are the steps it follows:

1. Checks out repo + sets up Java (same as before).
    
2. Sets up Flutter but this time pins:
    
    ```yaml
    flutter-version: '3.19.0'
    dart-verion: '3.3.4'   # typo: should be `dart-version`
    channel: 'stable'
    ```
    
3. Runs build:
    
    1. `flutter pub get` fetches packages.
        
    2. `flutter clean` cleans old builds.
        
    3. `flutter build ios --no-codesign` builds iOS app without signing.
        
    4. After building:
        
        1. Goes into `build/ios/iphoneos`
            
        2. Creates a `Payload` folder (needed for IPA structure).
            
        3. Symlinks the generated `Runner.app` into `Payload`.
            
        4. Zips the folder to `app.ipa`.
            

Result: An unsigned `.ipa` file.

**Job 3**: `build_androidApk` builds a debug Android `.apk` and uploads it as a release artifact.

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

This runs only after tests pass.

For Android, after setting up the Flutter environment, the workflow calls `flutter build apk --release`. This command compiles and packages the Android app into an `.apk` file ready for distribution. The resulting file is placed inside the `build/app/outputs/flutter-apk` directory of the project.

Here are the steps it follows:

1. Checks out repo, sets up Java, and sets up Flutter.
    
2. Runs:
    
    1. `flutter pub get`
        
    2. `flutter clean`
        
    3. `flutter build apk --debug` creates a debug APK.
        
3. Uploads APK using `ncipollo/release-action@v1`:
    
    ```yaml
    artifacts: "build/app/outputs/apk/debug/*"
    tag: v1.0.${{ github.run_number }}
    token: ${{ secrets.TOKEN }}
    ```
    
    1. Uploads all debug APKs as release artifacts.
        
    2. Tags release as `v1.0.<run_number>` (e.g., `v1.0.5`).
        
    3. Uses a GitHub **Personal Access Token** (`TOKEN`) stored in repo secrets.
        

## Step 4: Generate and Add a GitHub Token

The Android build job releases APKs using the `release-action`. To authenticate, you must provide a GitHub personal access token. To do this, go to **GitHub Settings → Developer settings → Personal access tokens**.

Generate a new token with `repo` permissions and copy the token immediately. Then go to your repository → Settings → Secrets → New repository secret. Add the token with the name `TOKEN`.

Now the workflow can use `${{ secrets.TOKEN }}` securely.

## Step 5: Understanding the Workflow

This workflow is triggered when code is pushed to the `main` branch or when a pull request is opened against it. Let’s break it down:

### Flutter Test Job

* **Environment:** Runs on `ubuntu-latest`.
    

**Steps:**

1. `actions/checkout@v3` fetches the source code.
    
2. `actions/setup-java@v3` installs Java, required for some Flutter tools.
    
3. `subosito/flutter-action@v2` installs Flutter on the runner.
    
4. `flutter pub get` installs dependencies.
    
5. `flutter analyze` checks for code issues.
    
6. `flutter test` runs test cases.
    

This job ensures your code compiles, passes linting, and has no failing tests.

### iOS App Build Job

* **Environment:** Runs on `macos-latest` because iOS builds require macOS.
    
* **Dependencies:** This job runs only if `flutter_test` passes (`needs: [flutter_test]`).
    

**Steps:** Similar setup as before, but after cleaning old builds with `flutter clean`, it runs `flutter build ios --no-codesign` to build an iOS app without requiring a signing certificate. The shell commands package the app into an `.ipa` file.

### Android APK Build Job

* **Environment:** Runs on `ubuntu-latest`.
    
* **Dependencies:** Also depends on `flutter_test`.
    

**Steps:**

1. Installs Flutter.
    
2. Runs `flutter clean` and then builds the Android APK.
    
3. Uses `ncipollo/release-action@v1` to upload the APK as a GitHub release, tagged automatically with a version like `v1.0.<run_number>`.
    

## Step 6: Push and Enable the Workflow

Save your file as `.github/workflows/ci.yml` and push the changes:

```bash
git add .
git commit -m "Add GitHub Actions workflow"
git push
```

When you push your changes to GitHub, the workflow file is picked up automatically. To confirm that it is running, open your repository on GitHub and click on the **Actions** tab at the top of the page. You will see a list of workflow runs, each tied to the commit message that triggered them.

Click on the most recent run to expand the details. Inside, you’ll find separate jobs for **Android** and **iOS** builds. Each job will show its status in real time:

1. A **yellow dot** with “In progress” indicates the job is still running.
    
2. A **green check mark** with “Success” means the job finished successfully.
    
3. A **red cross** with “Failed” means something went wrong.
    

This way, you can immediately tell whether your Android and iOS builds passed or if one of them needs attention.

![Running for Flutter Test](https://cdn.hashnode.com/res/hashnode/image/upload/v1701417493045/31e8f9db-b4b7-445c-ab6d-caa8cbc8dfdf.png align="center")

![Building for iOS](https://cdn.hashnode.com/res/hashnode/image/upload/v1701417512470/d27378ea-5bf2-487e-a0b0-9c2a9ffaa92e.png align="center")

![Building for Android](https://cdn.hashnode.com/res/hashnode/image/upload/v1701417526668/31b6e5c9-c43f-46ef-a25c-7f2321eda443.png align="center")

![Jobs completed](https://cdn.hashnode.com/res/hashnode/image/upload/v1701417477229/cbae6ba2-f51c-4f2a-81bc-cdb3345a5319.png align="center")

![Showcase 2 app releases on the right hand side with versions](https://cdn.hashnode.com/res/hashnode/image/upload/v1701439224779/7fb85ed3-00ae-4154-8032-ffeb9bb5e1b1.png align="center")

![Detailed app release versioning showcase](https://cdn.hashnode.com/res/hashnode/image/upload/v1701439234845/02c24d1e-09cd-4b4e-b9ea-fe96d4516f0c.png align="center")

## Final Notes

With this setup, you now have:

* Automated testing whenever you push or open a pull request.
    
* Automatic iOS builds on macOS runners.
    
* Automatic Android builds with APKs released to GitHub.
    

This ensures that every change is tested and that builds are consistently generated without manual steps.

For more details, see the official GitHub Actions documentation: [https://docs.github.com/en/actions](https://docs.github.com/en/actions).
