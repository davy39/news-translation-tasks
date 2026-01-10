---
title: React Native - Commandes de base expliquées avec des exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/react-native-basic-commands-explained-with-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9cf2740569d1a4ca3510.jpg
tags:
- name: React Native
  slug: react-native
- name: toothbrush
  slug: toothbrush
- name: Tutorial
  slug: tutorial
seo_title: React Native - Commandes de base expliquées avec des exemples
seo_desc: 'Here you will find a list of basic commands to start developing iOS and
  Android apps using React Native. If you don’t have it installed yet, is highly recommended
  that you follow the official guide.

  Starting a new project

  There are different ways you...'
---

Vous trouverez ici une liste de commandes de base pour commencer à développer des applications iOS et Android en utilisant React Native. Si vous ne l'avez pas encore installé, il est fortement recommandé de suivre le [guide officiel](https://facebook.github.io/react-native/docs/getting-started.html).

## Démarrer un nouveau projet

Il existe différentes façons de démarrer une application React Native. Vous pouvez utiliser **Expo** ou `create-react-native-app` (qui utilise à son tour Expo-Cli) pour démarrer votre nouveau projet, mais avec cette méthode, vous avez plus de contrôle sur ce qui se passe dans votre projet et pouvez communiquer, ajuster et écrire vos propres modules avec des bibliothèques natives pour les plateformes mobiles iOS et Android.

```text
react-native init [NOM-DU-PROJET]
cd [NOM-DU-PROJET]
```

## Exécuter l'application dans l'émulateur Android

Cette commande est explicite et, comme elle l'indique, elle démarrera l'émulateur Android et installera l'application que vous venez de créer. Vous devez être à la racine du projet pour exécuter cette commande.

```text
react-native run-android
```

## Exécuter l'application dans l'émulateur iOS

Cette commande fait exactement la même chose que `react-native run-android`, mais au lieu de l'émulateur Android, elle ouvre le simulateur iPhone.

```text
react-native run-ios
```

## Lier les dépendances aux projets natifs

Certaines bibliothèques ont des dépendances qui doivent être liées au code natif généré pour React Native. Si quelque chose ne fonctionne pas après avoir installé une nouvelle bibliothèque, c'est peut-être parce que vous avez sauté cette étape.

```text
react-native link [NOM-DE-LA-BIBLIOTHÈQUE]
```

## Effacer le bundle

Si quelque chose ne s'exécute pas comme prévu, vous devrez peut-être effacer et créer un nouveau bundle avec cette commande.

```text
watchman watch-del-all
```

## Prise en charge des décorateurs

JSX ne prend pas en charge les décorateurs par défaut, vous devez donc installer le plugin **Babel** pour le faire fonctionner.

```text
npm install babel-plugin-transform-decorators-legacy --save
npm install babel-plugin-transform-class-properties --save
```

## Exporter l'APK pour exécuter sur un appareil

Avec les commandes suivantes, vous aurez un APK non signé que vous pourrez installer et partager avec vos collègues à des fins de test. N'oubliez pas que cet APK n'est pas prêt à être téléchargé sur l'App Store ou en production. Vous trouverez votre nouvel APK dans `android/app/build/outputs/apk/app-debug.apk`.

### 1. Bundle de build de débogage

```text
react-native bundle --dev false --platform android --entry-file index.android.js --bundle-output ./android/app/build/intermediates/assets/debug/index.android.bundle --assets-dest ./android/app/build/intermediates/res/merged/debug
```

### 2. Créer un build de débogage

```text
cd android
./gradlew assembleDebug
```

## **Plus de ressources sur React Native :**

* [Comment créer des applications mobiles avec React Native](https://www.freecodecamp.org/news/what-you-need-to-know-to-start-building-mobile-apps-in-react-native-dded951277b7/)
* [Composants fonctionnels vs Composants de classe dans React Native](https://www.freecodecamp.org/news/functional-vs-class-components-react-native/)
* [Comment tester les applications React Native avec Jest et Enzyme](https://www.freecodecamp.org/news/setting-up-jest-enzyme-for-testing-react-native-40393ca04145/)