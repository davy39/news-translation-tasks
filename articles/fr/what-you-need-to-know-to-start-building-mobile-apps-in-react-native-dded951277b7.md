---
title: Ce que vous devez savoir pour commencer à construire des applications mobiles
  en React Native
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-15T16:45:50.000Z'
originalURL: https://freecodecamp.org/news/what-you-need-to-know-to-start-building-mobile-apps-in-react-native-dded951277b7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ZtaDNgOvw4DsdUPHmF9uDA.png
tags:
- name: Android
  slug: android
- name: iOS
  slug: ios
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React Native
  slug: react-native
seo_title: Ce que vous devez savoir pour commencer à construire des applications mobiles
  en React Native
seo_desc: 'By Said Hayani

  Nothing is better than building apps with JavaScript. Unless you are building mobile
  apps. JavaScript is for building web apps, and using it to build native mobile app
  used to not be possible. It was hard for any web developer to dive ...'
---

Par Said Hayani

Rien de mieux que de construire des applications avec JavaScript. Sauf si vous construisez des applications mobiles. JavaScript est destiné à la construction d'applications web, et l'utiliser pour construire des applications mobiles natives n'était pas possible. Il était difficile pour tout développeur web de se lancer dans la construction d'applications mobiles natives. Ils devaient apprendre Java, ou Objective-C … ou tout autre langage de programmation utilisé à cette fin.

C'était le cas, jusqu'à ce que [React Native](https://facebook.github.io/react-native/) de Facebook brise cette barrière. React Native offre de grands avantages comme la construction d'applications multiplateformes pour Android et iOS. Avant React Native, vous deviez écrire votre code deux fois — une pour Android et une pour iOS. Ce n'est plus le cas.

Cet article est une introduction au monde de React Native, alors préparez-vous 💡.

### Pourquoi React Native ?

Oui, alors pourquoi React Native et pas une autre technologie ?

Il nous offre de nombreuses solutions que d'autres technologies ne peuvent pas offrir. Voici ce que vous pouvez faire avec React Native :

#### Construire des applications mobiles natives

React Native nous permet d'écrire des applications natives en JavaScript pour iOS et Android. Il nous donne la possibilité d'utiliser tous les composants natifs comme les gestes, les notifications push, la caméra et la localisation. Il existe d'autres bibliothèques JavaScript pour construire des applications mobiles comme Ionic ou PhoneGap. Mais ces bibliothèques utilisent Webview, et les applications construites avec ces technologies ne sont pas natives.

#### Construire des applications mobiles multiplateformes (iOS et Android)

Oui, avec React Native, vous pouvez construire des applications mobiles qui fonctionnent sur iOS et Android. C'est l'un des grands avantages de React Native. Avant que Facebook ne le crée, vous deviez construire votre application deux fois et avec un code différent : une pour iOS en utilisant Swift ou Objective-C et une pour Android en utilisant Java ou Kotlin. React Native a résolu ce problème afin que vous puissiez construire votre application React Native et qu'elle fonctionne sur iOS et Android. Génial ! ✨

#### Écrire votre code entièrement en JavaScript et React

Lorsque vous construisez des applications React Native, vous écrivez en fait du JavaScript. Le code [Reactjs](https://reactjs.org/) nous permet de construire de grands composants d'interface utilisateur et d'expérience utilisateur.

### Commencer avec React Native

Commencer avec React Native peut être excitant, mais en même temps un peu déroutant. La première étape est de l'installer, et il existe plusieurs façons de le faire :

#### Utiliser expo-cli :

expo-cli est un outil en ligne de commande. Il télécharge et installe le modèle React Native pour vous, intégré avec l'API [expo](http://expo.io/) ([voir ici pour le guide d'installation](https://github.com/react-community/create-react-native-app)). C'est une manière facile de construire une application React Native, et c'est la manière recommandée si vous commencez avec React Native.

expo-cli vous offre de nombreuses options. Vous pouvez exécuter et tester votre application sur un appareil mobile sans aucune configuration. Scannez un code QR et votre application s'ouvrira avec l'application mobile expo. Vous pouvez explorer d'autres applications mobiles construites avec React Native sur le navigateur via une interface web appelée [appertize](https://appetize.io/) !

#### Utiliser react-native-cli

Le [react-native-cli](https://facebook.github.io/react-native/docs/understanding-cli) fait le même travail que expo-cli, mais avec une approche différente et des avantages supplémentaires. Les applications installées avec react-native-cli nous offrent l'option et la capacité de créer nos propres modules natifs dans notre application. Vous n'avez pas besoin d'éjecter votre application pour pouvoir créer des modules natifs. L'éjection vous permet d'utiliser des modules natifs et d'écrire les vôtres (_nous explorerons comment écrire des modules natifs dans une autre partie_).

Le développement d'applications React Native sur différentes plateformes est un processus différent. Parfois, nous avons besoin de configurations spécifiques pour une plateforme spécifique. Par exemple, pour construire pour Android, vous devez utiliser le SDK Android, alors explorons comment cela fonctionne !

### Construire des applications mobiles pour Android

Il y a certaines exigences que vous devez installer pour commencer à développer pour Android. Tout d'abord, vous devez télécharger et configurer à la fois le SDK Android et Android Studio. Vous pouvez les télécharger avec ce lien [ici](https://developer.android.com/studio/).

Après avoir téléchargé Android Studio, vous devez installer quelques API également. Pour ce faire, ouvrez Android Studio, puis cliquez sur l'onglet paramètres, cette fenêtre s'ouvrira :

![Image](https://cdn-media-1.freecodecamp.org/images/1*VuPXMkBtFPNpPN1CHM6HzA.png)

Tout d'abord, cochez ✔️ la plateforme que vous souhaitez que votre react-native supporte dans l'onglet Plateformes SDK (par exemple Android 6.0 Marshmallow). Puis basculez sur les outils SDK.

![Image](https://cdn-media-1.freecodecamp.org/images/1*kkEXZjmDm9wdw1Ch7sM3Ew.png)
_cliquez sur l'image pour la voir clairement_

Et cochez `Android SDK Build-Tools`, `Android SDK tools`, et `google play service`. Sous Android SDK Build-Tools, sélectionnez toutes les plateformes :

* À partir de 19.0.0 à 20.0.0
* De 22.0.0 à 24.0.0
* Et 25.0.2, 26.0.1 à 26.0.3
* 27.0.3 et 28.0.1 à 28.02

![Image](https://cdn-media-1.freecodecamp.org/images/1*1i6hBrT-IG8KdeQJiFEitA.png)

Maintenant, nous avons terminé avec le SDK et Android Studio. L'étape suivante est l'émulateur. L'émulateur (ou le simulateur) est l'endroit où nous devons exécuter et tester notre application. Il y a de nombreux choix différents.

Vous pouvez utiliser les émulateurs Android Studio. Vous pouvez vérifier ici comment créer un [émulateur à utiliser sur Android Studio](https://developer.android.com/studio/run/managing-avds). Franchement, je ne les ai jamais utilisés. Je préfère [Genymotion](https://www.genymotion.com/) ou un appareil réel.

#### **Genymotion**

[Genymotion](https://www.genymotion.com/) est une application de bureau qui fournit un émulateur virtuel pour tester votre application. J'aime beaucoup l'utiliser car c'est rapide. 💡 Il vous donne des options pour créer un téléphone personnalisé avec les fonctionnalités que vous pouvez trouver sur n'importe quel appareil réel. Par exemple, activer le WiFi, la localisation et la caméra. Je vous recommande vivement d'utiliser [Genymotion](https://www.genymotion.com/) plutôt que les émulateurs Android Studio ou tout autre émulateur.

#### **Utiliser des appareils réels**

Rien de mieux que d'utiliser des appareils réels pour exécuter et tester votre application. Cela vous permet de savoir à quoi ressemble votre application sur un appareil réel. Cela vous fait ressentir la réalité de votre travail d'une manière que l'appareil virtuel ne donne pas. Donc, si vous avez la possibilité d'utiliser un appareil, n'hésitez pas.

**À ce stade, nous sommes bons avec Android — mais qu'en est-il d'iOS ?**

### Construire des applications React Native pour iOS

Exécuter React Native pour iOS ne semble pas très différent d'Android. La même application React Native qui s'exécute sur Android peut également s'exécuter sur iOS, avec quelques exceptions.

Par exemple, si vous souhaitez exécuter sur un appareil iOS, vous devez avoir un MacOS. En parlant de MacOS et iOS, vous n'avez pas besoin de télécharger des dépendances supplémentaires telles que le SDK pour Android pour exécuter React Native sur iOS.

En ce qui concerne les émulateurs, Xcode dispose de bons émulateurs que vous pouvez utiliser pour tester votre application React Native. Vous pouvez consulter cet article qui montre [quelques astuces à utiliser](https://www.appcoda.com/ios-simulator-tips-tricks/) avec les émulateurs.

![Image](https://cdn-media-1.freecodecamp.org/images/0*wez2FnIMx3OHzook.jpg)
_crédit image [appcoda](https://www.appcoda.com/ios-simulator-tips-tricks/" rel="noopener" target="_blank" title=")_

Sur MacOS, vous pouvez exécuter à la fois iOS et Android. Vous pouvez définitivement installer Android Studio et Genymotion sur MacOS. Cette possibilité n'existe pas sur un PC où vous ne pouvez exécuter que l'émulateur Android mais pas l'émulateur iOS. Donc vous êtes chanceux 💡 si vous avez un MacOS — profitez-en 💡.

Donc maintenant nous avons l'environnement pour construire une application React Native et nous avons tout installé, mais comment le code React Native est-il écrit ? C'est si simple : vous allez en fait écrire du code [Reactjs](https://reactjs.org/).

Vous pouvez consulter [le guide officiel](https://facebook.github.io/react-native/docs/) pour vous entraîner avec React Native. Je recommande cet excellent article pour commencer « [Réplique YouTube React Native](https://medium.com/react-native-training/react-native-youtube-replica-f378200d91f0) ». Il vous guidera étape par étape pour créer votre première application React Native.

Wow ! Jusqu'à maintenant, vous allez bien et vous codez avec React Native. 💡 Mais vous devez vérifier et déboguer vos erreurs et voir les logs de votre code. Oui, les logs !! Donc nous avons besoin d'un débogueur ! Comment déboguer avec React Native ?

### Déboguer React Native

Déboguer votre code est très important, pas seulement avec React Native mais avec tout autre langage de programmation. Donc dans votre code React Native, vous devez savoir ce qui se passe. Il existe de nombreuses façons différentes de déboguer une application React Native comme :

#### Déboguer avec les outils de développement Chrome

React Native vous donne l'option d'utiliser les outils de développement Chrome pour voir les logs de votre application. Pour déboguer avec Chrome et activer le mode de débogage dans votre émulateur, sur le clavier, cliquez simplement sur `Ctrl + m`.

Cet écran apparaîtra :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Dinip_5zLvLoqyYNVH5PXQ.png)

Et choisissez `Debug Js Remotely`. Cela ouvrira un onglet dans Google Chrome avec cette adresse `http://localhost:8081/debugger-ui/`. C'est pour utiliser les outils de développement Chrome, qu'en est-il des autres options ?

#### Utiliser React-native-debugger

![Image](https://cdn-media-1.freecodecamp.org/images/0*ygMtWowJME-3BTnD.png)
_[crédit react-native-debugger](https://github.com/jhen0409/react-native-debugger" rel="noopener" target="_blank" title=")_

[React-native-debugger](https://github.com/jhen0409/react-native-debugger) est un excellent outil pour déboguer le code React Native. C'est une application de bureau qui vous offre de nombreux avantages. Il est livré avec les outils de développement Redux et l'intégration de React-devtools. Vous pouvez également déboguer le style. C'est en fait le meilleur débogueur pour React Native et c'est celui que j'utilise. Il est généralement disponible sur MacOS, Windows et Linux. Consultez [le guide d'installation et d'intégration](https://github.com/jhen0409/react-native-debugger).

Je pense que c'est suffisant à ce stade. Il s'agit de la première partie du guide absolu pour la construction d'applications mobiles avec React Native. Dans la prochaine partie, nous allons plonger dans des conseils et des problèmes plus techniques comme comment nous pouvons utiliser des composants natifs, l'API React Native, l'intégration avec d'autres bibliothèques, Redux, GraphQL et des trucs comme ça. Donc abonnez-vous à cette [liste de diffusion](http://eepurl.com/dk9OJL) pour rester à l'écoute lorsque la prochaine partie sortira. Merci pour votre temps. 💡

Vous pouvez toujours me trouver sur [Twitter](https://twitter.com/@saidHYN) 💡