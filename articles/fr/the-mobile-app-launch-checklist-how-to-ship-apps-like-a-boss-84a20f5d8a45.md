---
title: La Checklist de Lancement d'Applications Mobiles — Comment Livrer des Apps
  Comme un Pro
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-08T23:23:49.000Z'
originalURL: https://freecodecamp.org/news/the-mobile-app-launch-checklist-how-to-ship-apps-like-a-boss-84a20f5d8a45
coverImage: https://cdn-media-1.freecodecamp.org/images/1*19x5Ze6FU-bYSCsvUdzF2Q.png
tags:
- name: Android
  slug: android
- name: iOS
  slug: ios
- name: mobile app development
  slug: mobile-app-development
- name: Productivity
  slug: productivity
- name: 'tech '
  slug: tech
seo_title: La Checklist de Lancement d'Applications Mobiles — Comment Livrer des Apps
  Comme un Pro
seo_desc: 'By Michal Bialas

  In this article, I would like to present a short guide on how to release mobile
  apps. I’ll emphasise the internal releases. I’m also not limiting myself to Android,
  as I believe this may apply to iOS as well.

  I split this article int...'
---

Par Michal Bialas

Dans cet article, je souhaite présenter un guide concis sur la manière de publier des applications mobiles. Je mettrai l'accent sur les versions internes. Je ne me limite pas à Android, car je crois que cela peut également s'appliquer à iOS.

J'ai divisé cet article en plusieurs points pour améliorer la lisibilité. Si vous souhaitez en savoir plus, restez avec moi ! J'espère que cela vous plaira.

### **1. Assurez-vous que tous vos tests passent** ✅

![Image](https://cdn-media-1.freecodecamp.org/images/oMvWjS8YhmpWSXhmyrwVOeb7PcG2gT9gTiag)

Si vous écrivez des tests unitaires et d'intégration de bout en bout, vous devez toujours vérifier leur résultat. S'ils échouent, faites en sorte qu'ils fonctionnent.

### **2. Effectuez une construction complète propre de votre application** ✅

![Image](https://cdn-media-1.freecodecamp.org/images/WTgYEm7Lso7UbJX8l6z2-7ruJAUQDv4d-bCb)

Si vous obfusquez le code sur Android et utilisez [**ProGuard**](https://stuff.mit.edu/afs/sipb/project/android/sdk/android-sdk-linux/tools/proguard/docs/index.html#manual/introduction.html), assurez-vous qu'il ne supprime pas de code qui pourrait entraîner le plantage de l'application. Vous pouvez lire sur la réduction de code [ici](https://developer.android.com/studio/build/shrink-code).

La construction complète peut être effectuée sur votre machine locale ainsi qu'en utilisant l'**Intégration Continue**.

Si vous ou votre entreprise possédez un serveur, vous pouvez configurer votre flux **CI** en utilisant [**Jenkins**](https://jenkins.io/) (qui est un serveur d'automatisation open source gratuit). Sinon, vous pouvez facilement utiliser l'un des nombreux services CI disponibles sur le marché. Je peux recommander, par exemple, [**Bitrise**](https://app.bitrise.io/users/sign_up?referrer=6ee27e581bdc8285), [CircleCI](https://circleci.com/), [Travis](https://travis-ci.org/) et [**Bitbucket Pipelines**](https://bitbucket.org/product/features/pipelines).

Travis est déjà intégré avec Github, donc si vous avez un plan payant, cela pourrait être votre choix. Si vous utilisez Bitbucket, c'est la même chose pour Bitbucket Pipelines.  
[**Bitrise**](https://app.bitrise.io/users/sign_up?referrer=6ee27e581bdc8285) dispose de nombreuses intégrations avec des services comme Slack, Fabric, [XCode Archive](https://www.bitrise.io/integrations/steps/xcode-archive), [CocoaPods](https://cocoapods.org/), [Gradle Runner](https://www.bitrise.io/integrations/steps/gradle-runner), [Jira](https://pl.atlassian.com/software/jira) et bien d'autres. J'ai écrit un court article sur **CircleCI** il y a quelque temps, donc si vous êtes intéressé, vous pouvez le consulter sur [**mon blog**](http://mmbs.github.io/tools/ci/2016/07/31/circleci-for-android-projects/).

### **3. Effectuez une analyse statique du code** ✅

![Image](https://cdn-media-1.freecodecamp.org/images/rQ9hAVdxxBuUeNotoGJK2KIjetGv3ULNPz-R)

Assurez-vous d'utiliser des outils comme :

* Lint (_pour Java et Kotlin, disponible par défaut dans Android Studio version 3.1 et supérieure_), [ktlint](https://github.com/shyiko/ktlint), pmd, checkstyle, findbugs, [detekt](https://github.com/arturbosch/detekt), [gradle-static-analysis-plugin](https://github.com/novoda/gradle-static-analysis-plugin) **pour Android**
* [OCLint](http://oclint.org/), [tailor](https://github.com/sleekbyte/tailor), [SwiftLint](https://github.com/realm/SwiftLint), [Clang Static Analyzer](http://clang-analyzer.llvm.org/), [Infer](https://fbinfer.com/), [SwiftFormat](https://github.com/nicklockwood/SwiftFormat), [Swimat](https://github.com/Jintin/Swimat), [Faux Pas](http://fauxpasapp.com/) **pour iOS**

Bien sûr, utilisez uniquement les outils que vous trouvez utiles pour améliorer la qualité du projet sur lequel vous travaillez actuellement.

### **4. Préparez les versions de débogage et de production pour les besoins internes** ✅

![Image](https://cdn-media-1.freecodecamp.org/images/aXzbdMWWClSnIPiaS0fQuZsiVBUnYikB2ksi)

Assurez-vous de préparer une version de débogage et de production de votre application et de la publier en interne pour les tests. Vous devriez également utiliser des outils de rapport de plantage comme [**les rapports de plantage d'Instabug**](https://instabug.com/crash-reporting) ou [**Fabric**](https://get.fabric.io/) **(Crashlytics)**.

Il est vital de vérifier comment votre application fonctionne avec une API de débogage/staging et ensuite avec la production. Pour Android, il est également important d'obfusquer le code et de vérifier s'il est correctement réduit.

Lors de la publication de la version pour votre équipe, vous pouvez utiliser [**TestFlight**](https://developer.apple.com/testflight/) pour iOS et [**Google Play Test channel**](https://developer.android.com/distribute/best-practices/launch/test-tracks) pour Android. Vous pouvez également envisager des outils gratuits comme **Fabric** (qui sera [fermé à la mi-2019](https://fabric.io/blog/the-future-of-fabric)) ou [**Hockey App**](https://hockeyapp.net/#s) qui est actuellement en transition vers [**App Center**](https://appcenter.ms/).

### **5. Automatisez** ✅

![Image](https://cdn-media-1.freecodecamp.org/images/hD6g7L5PJDEvC8sG7hJkltvIiIGE9RNbjTVy)

La préparation des builds peut également être automatisée. Vous avez probablement entendu parler de [**fastlane**](https://fastlane.tools/). C'est un outil gratuit pour automatiser les captures d'écran, le déploiement bêta, le déploiement sur l'App Store / Google Play et la signature de code. Il est pris en charge par tous les services CI et de distribution que j'ai mentionnés précédemment.

![Image](https://cdn-media-1.freecodecamp.org/images/gpYGx-FA1FhJ-Lk6jRtECZOYN4iEQTUJlKtt)

La configuration pour [Android](https://docs.fastlane.tools/getting-started/android/setup/) et pour [iOS](https://docs.fastlane.tools/getting-started/ios/setup/) est assez simple mais n'est possible que si vous avez macOS. Malheureusement, il n'y a [pas de support pour les plateformes non-macOS](https://github.com/fastlane/fastlane/issues/11687) pour le moment. Cela est pénible pour les développeurs Android qui codent sur Linux et Windows. Mais il y a une solution ! 💡

![Image](https://cdn-media-1.freecodecamp.org/images/82tqd9S1PXAXrNFhQT8b9uNlCZSiU7B4trNT)

[**Gradle Play Publisher**](https://github.com/Triple-T/gradle-play-publisher) est un plugin Gradle qui automatise le téléchargement d'un App Bundle ou APK et d'autres détails de l'application sur le Google Play Store. Et c'est une excellente alternative à Fastlane. Je l'ai utilisé il y a quelque temps, il fonctionne vraiment bien et je peux le recommander. [La documentation](https://github.com/Triple-T/gradle-play-publisher/blob/master/README.md) est complète et permet de faciliter la configuration de l'outil.

### **6. Connaissez et écoutez vos utilisateurs** ✅

![Image](https://cdn-media-1.freecodecamp.org/images/eZ1SkkFnARgSIoHKlcnlIQSNsCKYu4bc8dBR)

Vous avez vérifié votre code, configuré des outils d'automatisation, préparé une version entièrement opérationnelle et testée, et l'avez publiée pour votre équipe afin qu'elle la teste. Mais combien de fois avez-vous eu l'impression que personne ne se soucie ou n'a le temps de vous donner des retours ? Je sais par expérience qu'il est vraiment difficile d'engager l'équipe à vérifier et à tester votre nouvelle application.

La solution à cela est [**Instabug**](https://instabug.com/). J'ai fait beaucoup de recherches sur les outils qui aident à recueillir des retours, des bugs, des rapports, etc., il y a presque 3 ans, et depuis, je suis resté fidèle à Instabug.

![Image](https://cdn-media-1.freecodecamp.org/images/l8tko24ko7ifXOJkv7nbYitOPvSOrAuCVoNW)

Il est vraiment facile à intégrer dans n'importe laquelle de vos applications (il prend en charge Android, iOS, React Native, Xamarin, Unity, Cordova) — il suffit de quelques lignes de code.

Comment vous pouvez utiliser cet outil :

* Vos utilisateurs peuvent simplement secouer le téléphone et [écrire un retour avec des captures d'écran déjà prises](https://instabug.com/bug-reporting). Ils peuvent même dessiner ou enregistrer une vidéo pour montrer ce qui manque ou comment reproduire un bug. C'est super utile.
* Au lieu de contacter les développeurs via des formulaires de contact, les utilisateurs finaux peuvent [demander des fonctionnalités ou donner des retours en utilisant le Chat In-App](https://instabug.com/in-app-chat). Cela aide beaucoup à rester en contact avec les utilisateurs en permanence.  
De plus, les développeurs peuvent facilement répondre aux utilisateurs qui ont signalé des bugs ou des plantages pour obtenir plus de contexte, les remercier ou même leur dire que le bug/plantage a été corrigé et qu'ils peuvent mettre à jour l'application vers la dernière version.
* Utilisez [les Demandes de Fonctionnalités In-App](https://instabug.com/feature-requests) et soutenez votre backlog par une priorisation pilotée par les utilisateurs. Grâce à cette fonctionnalité, l'équipe et le propriétaire du produit sauront quelle fonctionnalité publier en premier.

### **7. Surveillez l'engagement** ✅

![Image](https://cdn-media-1.freecodecamp.org/images/g9HjIh0lKL55vSryvS5rFTpHats3OEIDJcbC)

L'application est en production, mais vous avez l'impression que les gens n'utilisent pas votre application. Que faire alors ?

Vous pouvez intégrer des outils comme **Google Analytics**, **Fabric**, [**Amazon Pinpoint**](https://aws.amazon.com/pinpoint/), [**Mixpanel**](https://mixpanel.com/) ou [**Segment.io**](http://segment.io) pour vérifier :

* les utilisateurs actifs,
* les intervalles de session,
* le temps passé dans l'application,
* le flux d'écrans,
* la rétention,
* la conversion,
* la valeur à vie.

Vérifier ces KPI est également vital lors de la publication de nouvelles fonctionnalités d'application en production. Ne les sous-estimez pas. 💡

Je crois que c'est tout. J'espère que vous avez apprécié la checklist. Si vous avez des idées ou d'autres outils qui peuvent aider à la publication d'applications, faites-le moi savoir dans les commentaires. Vous pouvez également consulter mes autres articles :

* [Lucky 7 new tools and plugins for Android developers & designers](https://proandroiddev.com/lucky-7-new-tools-and-plugins-for-android-developers-designers-1545e5c59f27)
* [25 new Android libraries and projects to check at the beginning of 2018](https://proandroiddev.com/25-new-android-libraries-and-projects-to-check-at-the-beginning-of-2018-ba3b422bbbb4)
* [Terminal on steroids](https://medium.com/@mmbialas/terminal-on-steroids-bbf88f3dcbdb)

Si vous aimez mon article, n'oubliez pas de cliquer sur 👏 pour le recommander aux autres 👏.

Aussi, pour être informé de mes nouveaux articles et histoires, suivez-moi sur [Medium](https://medium.com/@mmbialas) et [Twitter](https://twitter.com/mmbialas). Vous pouvez également me trouver sur [LinkedIn](https://www.linkedin.com/in/mmbialas). Santé !