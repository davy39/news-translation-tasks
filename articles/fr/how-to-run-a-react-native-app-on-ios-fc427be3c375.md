---
title: Comment exécuter une application React Native sur iOS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-09T14:44:58.000Z'
originalURL: https://freecodecamp.org/news/how-to-run-a-react-native-app-on-ios-fc427be3c375
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Zo2V1LBkqJzI4XyuHG7VQg.jpeg
tags:
- name: iOS
  slug: ios
- name: mobile app development
  slug: mobile-app-development
- name: General Programming
  slug: programming
- name: React Native
  slug: react-native
- name: 'tech '
  slug: tech
seo_title: Comment exécuter une application React Native sur iOS
seo_desc: 'By Soujanya PS

  I recently started to develop a React-Native app on iOS. This was my first foray
  into native app development. I was surprised by the ease and level of abstraction
  provided by React-Native’s command line interface. I was also curious to...'
---

Par Soujanya PS

J'ai récemment commencé à développer une application React-Native sur iOS. C'était ma première incursion dans le développement d'applications natives. J'ai été surpris par la facilité et le niveau d'abstraction fournis par l'interface de ligne de commande de React-Native. J'étais également curieux de comprendre ce qui se passe sous le capot lorsque React-Native exécute une application sur un appareil ou un simulateur.

J'ai passé beaucoup de temps à parcourir le code pertinent. Il n'y avait pas un seul endroit qui résumait ce que React-Native fait pour faire fonctionner l'application. En partie, c'était la motivation pour venir avec cet article. Je veux aider toute autre personne qui commence fraîchement avec le développement d'applications React-Native.

React-Native fournit des utilitaires de ligne de commande pour exécuter une application sur les simulateurs/devices iOS et Android. Sans plus tarder, essayons de comprendre le quoi et le comment du processus pour exécuter des applications React-Native sur iOS.

### **Derrière les scènes**

React-Native fournit cette utilité appelée `init`. Elle crée un modèle d'application native pour vous. Ce modèle crée les fichiers de projet Xcode pertinents sous le dossier iOS de l'application.

Les applications React-Native peuvent être lancées sur les simulateurs/dispositifs physiques iOS en exécutant la commande suivante dans le dossier racine d'une application :

```
react-native run-ios
```

Une exécution réussie ouvrirait l'application sur un simulateur ou un appareil connecté. Pour que cela se produise, il y a une série d'étapes qui sont exécutées lorsque nous exécutons la commande ci-dessus.

#### **Commande run-ios**

React-Native fournit un certain nombre d'utilitaires de ligne de commande pour travailler avec l'application. Ceux-ci peuvent être trouvés sous le dossier **local-cli** du module node React-Native. **run-ios** est l'un de ces utilitaires qui invoque la fonction `runIOS()` définie dans le fichier runIOS.js. run-ios accepte certaines options telles que :

```
#Lancer l'application sur un simulateur spécifique
react-native run-ios --simulator "iPhone 5"
```

```
#Passer un emplacement non standard du répertoire iOS
react-native run-ios --project-path "./app/ios"
```

```
#Exécuter sur un appareil connecté, par exemple l'iPhone de Max
react-native run-ios --device "Max's iPhone"
```

```
#Construire l'application en mode Release
react-native run-ios --configuration Release
```

#### **Sélection de l'appareil/simulateur**

Lorsque aucun appareil n'est spécifié, `run-ios` lancera l'application en mode Debug sur un simulateur par défaut. Cela est fait en exécutant une série de commandes `xcrun simctl`. Elles vérifieront d'abord la liste des simulateurs disponibles sur Mac, en choisiront un parmi eux, puis démarreront le simulateur sélectionné.

Alternativement, si vous souhaitez exécuter l'application sur un appareil physique, branchez l'appareil sur le Mac et passez les détails de l'appareil à la commande `run-ios`.

L'étape suivante consiste à construire le projet Xcode de l'application.

#### **Construction du code de l'application**

Habituellement, le projet Xcode de l'application React-Native peut être trouvé dans le dossier iOS présent sous le dossier racine. Le projet Xcode est construit en utilisant la commande `xcodebuild`. Toutes les options spécifiées pour `run-ios` telles que la configuration, etc., sont transmises à cette commande.

Par défaut, le projet Xcode est construit en schéma Debug. Une fois le projet construit avec succès, l'application est installée et lancée sur le simulateur ou l'appareil connecté.

#### **Regroupement du code de l'application en mode Debug**

Pendant le processus de développement, React Native charge notre code JavaScript dynamiquement au moment de l'exécution. Pour cela, nous avons besoin d'un serveur pour regrouper notre code d'application et le fournir selon les besoins.

Pendant que le projet Xcode est en cours de construction en mode Debug, une instance du serveur Metro est également démarrée en parallèle. [Metro](https://facebook.github.io/metro/docs/en/getting-started) est le bundler utilisé par les applications créées par l'interface de ligne de commande (CLI) de React-Native. Il est utilisé pour regrouper notre code d'application en développement. Cela nous aide avec un débogage plus rapide et plus facile en permettant le rechargement à chaud, etc.

Le serveur Metro est configuré pour démarrer sur le port 8081 par défaut. Une fois l'application lancée dans le simulateur, une requête est envoyée au serveur pour le bundle.

```
#Code dans AppDelegate.m envoie la requête pour le bundle : #index.bundle au serveur
jsCodeLocation = [[RCTBundleURLProvider sharedSettings] jsBundleURLForBundleRoot:@"index" fallbackResource:nil];
```

```
RCTRootView *rootView = [[RCTRootView alloc] initWithBundleURL:jsCodeLocation  moduleName:@"MobileApp               initialProperties:nil     launchOptions:launchOptions];
```

Le serveur télécharge ensuite toutes les dépendances requises, regroupe le code de l'application JavaScript et l'envoie à l'application. Après cette étape, vous pouvez voir l'application fonctionner sur le simulateur ou un appareil connecté.

#### **Regroupement du code de l'application en mode Release — Pré-empaquetage du bundle JavaScript**

En mode Release, nous devons pré-empaqueter le bundle JavaScript et le distribuer à l'intérieur de notre application. Pour ce faire, un changement de code est nécessaire afin qu'il sache charger le bundle statique. Dans le fichier AppDelegate.m, modifiez jsCodeLocation pour pointer vers le bundle statique si vous n'êtes pas en mode debug.

```
#ifdef DEBUG
jsCodeLocation = [[RCTBundleURLProvider sharedSettings] jsBundleURLForBundleRoot:@"index" fallbackResource:nil];
```

```
#else
jsCodeLocation = [[NSBundle mainBundle] URLForResource:@"main" withExtension:@"jsbundle"];
```

```
#endif
```

Cela fera maintenant référence au fichier de ressource `main.bundle`. Ce fichier est créé pendant la phase de construction `Bundle React Native code and images` dans Xcode. Pendant cette phase, le script `react-native-xcode.sh` est exécuté, ce qui regroupe le code de l'application JavaScript. Ce script peut être trouvé sous le dossier scripts du module node React-Native.

#### **Construction de l'application à partir de Xcode**

Alternativement, le projet Xcode peut également être construit dans Xcode sur Mac au lieu d'utiliser le CLI React-Native. Une fois terminé, l'application peut être lancée sur un simulateur sélectionné à partir des options Xcode ou sur un appareil physique connecté.

![Image](https://cdn-media-1.freecodecamp.org/images/bMWy-EbznFYSdPqaUKfVbFIvv2YSfmlulDkS)
_Options de menu Xcode pour construire l'application et la lancer sur un simulateur_

J'espère que cela vous a aidé à comprendre les différentes étapes qui se produisent lorsque nous exécutons une simple commande `react-native run-ios` qui fait magiquement apparaître une application sur iOS.

Certaines parties des informations fournies ici ont été sourcées à partir de la page d'accueil de React-Native [home](https://facebook.github.io/react-native/docs/getting-started.html). Le reste est le produit de mes investigations dans le code :)