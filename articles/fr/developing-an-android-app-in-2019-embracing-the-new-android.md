---
title: 'Comment développer une application Android : adopter le "nouvel" Android'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-17T04:19:46.000Z'
originalURL: https://freecodecamp.org/news/developing-an-android-app-in-2019-embracing-the-new-android
coverImage: https://cdn-media-1.freecodecamp.org/images/1*kJIHafbx3Dzn6xWlVWDknA.png
tags:
- name: Android
  slug: android
- name: Kotlin
  slug: kotlin
- name: open source
  slug: open-source
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: 'Comment développer une application Android : adopter le "nouvel" Android'
seo_desc: 'By Aakarshit Uppal

  or how the Bitotsav ’19 app became a reality

  Background: Pantheon ’17 ⏪

  Almost two years ago, in September 2017, a friend, Ashank Anshuman convinced me
  to work on an app for the technical fest of our institute. We worked for about ...'
---

Par Aakarshit Uppal

#### *ou comment l'application Bitotsav '19 est devenue réalité*

### *Contexte : Pantheon '17 ⏩*

Il y a presque deux ans, en septembre 2017, un ami, Ashank Anshuman, m'a convaincu de travailler sur une application pour la fête technique de notre institut. Nous avons travaillé pendant environ deux semaines, jour et nuit, pour la préparer à temps pour la fête. Bien que nous étions épuisés, c'était une sensation incroyable de mettre quelque chose "en production", que les gens utilisaient réellement ! Elle a parfaitement servi son but, aidant les organisateurs à communiquer facilement tout aux participants.

> [**Pantheon '17 - Applications sur Google Play**](https://play.google.com/store/apps/details?id=in.pantheon17)  
> [_Dans son effort pour fournir une plateforme nationale aux jeunes pour montrer leurs compétences techniques ; affichant..._play.google.com](https://play.google.com/store/apps/details?id=in.pantheon17)

Elle était notée 4,9 avec environ 120 avis, que les robots de Google ont supprimés pour une raison quelconque, mais c'est une autre histoire. Nous avons reçu quelques demandes pour partager le code source de l'application, mais nous avons refusé, pour plusieurs raisons — mais surtout parce que nous n'étions pas satisfaits du code, surtout des parties bâclées à la fin. Nous n'avions tout simplement pas assez de temps et d'expérience pour écrire du code suffisamment bon pour que les gens puissent en apprendre et/ou l'utiliser.

### On recommence ! ?

Avance rapide jusqu'en novembre 2018 : Ankit Agrawal (c'est ce "type de fête") me demande de rejoindre l'équipe pour Bitotsav, notre fête socio-culturelle annuelle, à laquelle j'accepte, car je cherchais une excuse pour revenir à Android. Cette fois, j'ai convaincu Ashank (il a fallu beaucoup de persuasion !) de travailler sur l'application.

Nous n'avons pas fait grand-chose en décembre, mais j'ai commencé à lire sur des sujets comme les composants d'architecture, AndroidX, Jetpack, etc. Je m'étais également familiarisé avec Kotlin au cours des derniers mois, avec quelques cours qui ont été instrumentaux : un cours en deux parties par le seul et unique [Hadi Hariri](https://twitter.com/hhariri) et un autre plus récent par Svetlana Isakova et Andrey Breslav (qu'il a présenté à KotlinConf 2018). Kotlin était donc le choix évident pour l'application.

> [**Introduction à la programmation Kotlin**](http://shop.oreilly.com/product/0636920052982.do)  
> [_Kotlin 1.0 a été publié en février 2016, et depuis ce temps, il a été adopté par des développeurs du monde entier..._shop.oreilly.com](http://shop.oreilly.com/product/0636920052982.do)

> [**Kotlin pour les développeurs Java | Coursera**](https://www.coursera.org/learn/kotlin-for-java-developers)  
> [_Kotlin pour les développeurs Java de JetBrains. Le langage de programmation Kotlin est un langage moderne qui vous donne plus..._www.coursera.org](https://www.coursera.org/learn/kotlin-for-java-developers)

### **Décisions ?**

La première moitié de janvier est également passée sans que beaucoup de code soit écrit, car j'étais occupé et je n'ai pas pu me rendre à l'université avant le 16 janvier. Nous avons cependant pris quelques décisions majeures :

* **Utiliser** [**Kotlin**](https://developer.android.com/kotlin) **exclusivement**
    
* **Utiliser** [**l'emballage basé sur les fonctionnalités**](https://hackernoon.com/package-by-features-not-layers-2d076df1964d)
    
* **Utiliser** [**Jetpack**](https://developer.android.com/jetpack) [**Architecture Components**](https://developer.android.com/topic/libraries/architecture/) **avec** [**AndroidX**](https://developer.android.com/jetpack/androidx/releases)
    
* **Utiliser** [**API 21 comme API minimale**](https://developer.android.com/about/dashboards/) *(22 aurait peut-être été un meilleur choix)*
    
* **Utiliser** [**Android Studio Canary**](https://developer.android.com/studio/preview)
    
* Utiliser [Git Flow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) & [SemVer](https://semver.org/)
    
* Écrire du code suffisamment bon pour le rendre public après la fête ?
    

![Image](https://cdn-media-1.freecodecamp.org/images/G3zLWh-8mSzeAdIsNmP5YL6ahsna4m2mqm8o align="left")

*Jetpack avec AndroidX*

Donc, en gros, une réinitialisation complète de toute l'expérience de développement d'une application en 2017 à la pointe en 2019. C'était vraiment excitant, mais aussi un grand défi.

### Code Code Code! ?

Nous avons décidé qu'Ashank s'occuperait du backend de l'application (BD & Réseau, Notifications avec FCM, Traitement en arrière-plan) et que je m'occuperais du frontend et de l'intégration, comme nous l'avions fait pour Pantheon '17. De nombreuses ressources se sont avérées utiles pour commencer et pendant que nous travaillions, mais les meilleures de loin étaient ces excellents codelabs proposés par Google :

* [Room with a View - Kotlin](https://codelabs.developers.google.com/codelabs/android-room-with-a-view-kotlin) (ViewModel, LiveData & Room avec Coroutines)
    
* [Utiliser les coroutines Kotlin dans votre application Android](https://codelabs.developers.google.com/codelabs/kotlin-coroutines)
    
* [Codelab de liaison de données](https://codelabs.developers.google.com/codelabs/android-databinding)
    
* [Codelab de navigation](https://codelabs.developers.google.com/codelabs/android-navigation) : (Composant d'architecture de navigation)
    
* [Travail en arrière-plan avec WorkManager](https://codelabs.developers.google.com/codelabs/android-workmanager/#0)
    

> [**Google Codelabs**](https://codelabs.developers.google.com/?cat=Android)  
> [_Les Google Developers Codelabs offrent une expérience de codage guidée, tutorielle et pratique. La plupart des codelabs vous guideront à travers..._codelabs.developers.google.com](https://codelabs.developers.google.com/?cat=Android)

De plus, les applications [Sunflower](https://github.com/googlesamples/android-sunflower) et [Google IO 18](https://github.com/google/iosched) de Google étaient des bases de code idéales pour référence. L'application [Android Dev Summit](https://github.com/google/iosched/tree/adssched) aurait également été une bonne source de référence, si je l'avais connue avant !

> [**googlesamples/android-sunflower**](https://github.com/googlesamples/android-sunflower)  
> [_Une application de jardinage illustrant les meilleures pratiques de développement Android avec Android Jetpack. - googlesamples/android-sunflower_github.com](https://github.com/googlesamples/android-sunflower)

Avec ces outils dans notre arsenal, nous avons commencé à coder. J'ai décidé d'utiliser le nouveau [**composant d'architecture de navigation**](https://developer.android.com/topic/libraries/architecture/navigation) **pour implémenter une** [**architecture d'application à activité unique**](https://www.youtube.com/watch?v=2k8x8V77CrU). Ashank a commencé avec Room et FCM. J'avais également pensé à utiliser [**Koin**](https://insert-koin.io/) **pour l'IoC**, mais je n'étais pas sûr.

Par coïncidence, Joe Birch a lancé un cours sur Koin à peu près à cette époque sur [caster.io](https://caster.io) (propose de petits cours précis par des professionnels, chacun gratuit pendant une semaine au lancement !), et j'ai décidé de l'utiliser. Aucun regret ! Sérieusement, le support Android est incroyable et la [documentation](https://beta.insert-koin.io/docs/2.0/documentation/reference/index.html#_koin_for_android_developers) est fabuleuse ❤️

> [**Koin**](https://caster.io/courses/koin)  
> [_Dans ce cours, nous allons apprendre un framework d'injection de dépendances connu sous le nom de Koin en construisant une application entièrement fonctionnelle..._caster.io](https://caster.io/courses/koin)

Avec Navigation et Koin configurés, j'ai commencé avec l'UI, en décidant d'**utiliser exclusivement les composants de design matériel** pour l'UI pour lesquels les [**directives**](https://material.io/design/components/) **et** [**docs**](https://material.io/develop/android/components/bottom-app-bar/) se sont avérées utiles. De plus, je *devais* **utiliser** [**Data Binding**](https://developer.android.com/topic/libraries/data-binding) parce que je l'adore ! Pendant ce temps, Ashank a implémenté [WorkManager](https://developer.android.com/topic/libraries/architecture/workmanager), que nous avons décidé d'**utiliser au lieu de Firebase Job Dispatcher**, en adoptant pleinement Jetpack !

La première chose que j'ai développée était l'UI de l'emploi du temps, ce qui m'a aidé à me familiariser avec les composants d'architecture. Une fois cela fait, je suis passé à l'UI du flux d'inscription, probablement la partie la plus complexe de l'application, qui présentait une utilisation avancée de LiveData et Navigation pour implémenter trois étapes avec des formulaires validés en direct (valant un article de blog à part entière, à venir bientôt ?). Cela m'a rendu beaucoup plus confiant dans ces composants, et le reste s'est déroulé sans encombre. Nous avons terminé les fonctionnalités prévues, découvert quelques pièges, corrigé quelques bugs.

### Lancement ?

Avec les principales fonctionnalités implémentées, nous avons fait quelques retouches d'UI, terminé quelques TODOs finaux, et étions prêts pour le lancement ! En touche finale, j'ai ajouté quelque chose que je prévoyais depuis le début :

Un thème de couleur différent à chaque changement de configuration ! Cela a été fait pour compléter le thème de la fête : « *Couleurs de l'Asie* »

L'application était en ligne sur le Play Store le 11 février 2019 ! ??

> [**Bitotsav '19 - Applications sur Google Play**](https://play.google.com/store/apps/details?id=in.bitotsav)  
> [_Bitotsav '19 la 29e édition de la fête socio-culturelle annuelle de l'Institut de Technologie Birla, Mesra est prête à..._play.google.com](https://play.google.com/store/apps/details?id=in.bitotsav)

![Image](https://cdn-media-1.freecodecamp.org/images/r2U-QsAbLp7bc-Z69tXP9dNi1OyqTxZzKt24 align="left")

*Application Bitotsav '19*

#### Corrections et mises à jour

Nous avons rencontré (les seuls !) deux bugs en quelques heures, que nous avons corrigés immédiatement. Le premier était lié aux méthodes DAO marquées `suspend`, mais je ne suis toujours pas sûr à 100 % de la raison exacte pour laquelle cela se produisait ?. Le second était dû à l'obfuscation provoquant une défaillance de sérialisation, et a été facilement corrigé avec une annotation K\_eep.

Ensuite, j'ai commencé à travailler sur la prochaine mise à jour, dans laquelle j'ai ajouté le tableau des leaders dans le flux et les événements nocturnes de la fête dans l'emploi du temps, ainsi que quelques autres changements. Une troisième mise à jour a suivi, ajoutant quelques fonctionnalités mineures supplémentaires.

**La fête s'est bien déroulée, et l'application a été utilisée par plus de 1000 participants !**

Nous avons rencontré un problème mineur dû à une entrée incorrecte dans la base de données sur les serveurs par notre ami Sushant Gupta, qui a ensuite écrit un article de blog plutôt dramatique à ce sujet.

> [**Attaque DDoS sur le site web de Bitotsav '19**](https://cs.sonudoo.com/2019/02/ddos-attack-on-bitotsav-19-website.html)  
> [_Ce n'est pas un compte rendu technique. C'est une histoire que je veux partager et qui pourrait être une leçon pour plusieurs développeurs Web et d'applications..._cs.sonudoo.com](https://cs.sonudoo.com/2019/02/ddos-attack-on-bitotsav-19-website.html)

Après la fête, nous avons publié une dernière mise à jour, stockant les détails des événements, le flux, etc., sous forme de JSONs dans l'application et supprimant les numéros de contact des organisateurs pour des raisons de confidentialité.

#### Passage en open source !

Il était temps de rendre le code open source ! Cette fois-ci, nous avions veillé à écrire un code compréhensible, et il était prêt pour le monde. J'ai préparé un README élégant, et pour supprimer les numéros de contact de l'historique du dépôt, nous avons utilisé l'outil incroyable [BFG Repo Cleaner](https://rtyley.github.io/bfg-repo-cleaner).

Le code de l'application Bitotsav '19 est maintenant public, pour que chacun puisse le consulter, s'y référer, en apprendre ou l'utiliser ! Jetez un coup d'œil et n'oubliez pas de laisser un ? ?

> [**aksh1618/Bitotsav-19**](https://github.com/aksh1618/Bitotsav-19)  
> [_Application officielle pour Bitotsav '19. Contribuez au développement de aksh1618/Bitotsav-19 en créant un compte sur GitHub._github.com](https://github.com/aksh1618/Bitotsav-19)

### Défis ?

Nous avons rencontré quelques défis pendant le développement :

* **Limitations de temps :** Le principal défi que nous avons rencontré était d'avoir très peu de temps pour apprendre des concepts très nouveaux et les utiliser pour créer une application destinée à être utilisée par des centaines de personnes. Cette contrainte de temps a conduit à de nombreuses heures de travail continu, entraînant du stress et de la fatigue, mais nous avons réussi à persévérer et à livrer !
    
* **WorkManager avec Coroutines :** Sur le plan technique, nous avons rencontré quelques défis mineurs avec WorkManager et Coroutines, mais nous avons réussi à les surmonter. Espérons un meilleur support pour les coroutines dans tout le SDK Android à mesure que le développement continue ?.
    
* **API 21 :** Nous avons choisi l'API 21 comme version minimale pour éviter d'avoir à adapter tout pour les versions plus anciennes, car la plupart des appareils Android sont sur l'API 21 ou supérieure de toute façon. Mais étrangement, [certaines choses](https://stackoverflow.com/a/29756195/6346531) ont refusé de fonctionner sur l'API 21, surtout les arrière-plans de vue. C'était vraiment frustrant, me faisant regretter que nous n'ayons pas fixé l'API minimale à 22, d'autant plus que nous avons découvert que l'application n'avait été installée que sur deux appareils API 21 : ceux sur lesquels nous avions testé ?.
    
* **Manque d'appareils :** Un autre défi que nous avons rencontré était de ne pas avoir assez d'appareils pour tester. Pendant Pantheon '17, nous avions un foyer avec ~200 personnes, et donc les tests étaient faciles. Cette fois-ci, la plupart des gens étaient partis pour des stages, donc nous devions nous fier à la confiance dans le code !
    
* **Pas de relecteurs de code :** Beaucoup de ce que nous avons utilisé était nouveau pour nous, et nous avons fait de notre mieux pour nous assurer que nous faisions tout correctement. Mais avoir un relecteur aurait été très utile. Même maintenant, si vous pensez pouvoir faire une relecture rapide du code de l'application, nous vous en serions très reconnaissants !
    
* **L'Apocalypse :** Nous avons également rencontré ce problème de "DDoS", lisez l'article de blog de Sushant lié ci-dessus, vous ne le regretterez pas !
    

### Leçons apprises ✅

* **Kotlin + Jetpack = ❤️ :** La principale leçon est que le développement Android a parcouru un long chemin et avec Kotlin et Jetpack, c'est définitivement beaucoup plus amusant et purement joyeux ! Sérieusement, il y a eu plusieurs moments *orgasmique* pendant le processus de codage !
    
* **Rien n'est impossible :** Un peu cliché mais vrai : si vous avez la volonté de travailler dur, vous pouvez tout faire, peu importe la difficulté. Bien sûr, il y aura des phases stressantes, mais continuez à avancer. Croyez simplement en vous !
    

### Regrets ?

* **Pas d'Instant App / App Bundles :** Nous avons simplement manqué celle-ci. Nous n'y avons même pas pensé. Eh bien, peut-être la prochaine fois.
    
* **Pas de tests :** Je sais, c'est un gros point ! Avoir des tests appropriés aurait pu nous aider beaucoup, mais en raison des contraintes de temps, nous avons décidé de ne pas écrire de tests jusqu'à un moment "ultérieur", qui n'est pas encore arrivé ?.
    

### TL;DR. ?

Commencer avec une application en 2019 ?

#### Utiliser Kotlin & Coroutines

* [Apprendre](http://shop.oreilly.com/product/0636920052982.do) Kotlin et [l'utiliser](https://codelabs.developers.google.com/codelabs/taking-advantage-of-kotlin) exclusivement !
    
* [Apprendre à utiliser](https://codelabs.developers.google.com/codelabs/kotlin-coroutines) les coroutines avec Android.
    

#### Utiliser les composants Jetpack avec AndroidX

* [Apprendre à utiliser](https://codelabs.developers.google.com/codelabs/android-navigation) le composant de navigation pour l'architecture à activité unique.
    
* [Apprendre à utiliser](https://codelabs.developers.google.com/codelabs/android-room-with-a-view-kotlin) les composants de cycle de vie pour l'UI & Room pour la persistance.
    
* Faites-vous une faveur et [utilisez](https://codelabs.developers.google.com/codelabs/android-databinding) la liaison de données !
    
* [Apprendre à utiliser](https://codelabs.developers.google.com/codelabs/android-workmanager/#0) WorkManager pour le traitement en arrière-plan.
    

#### Utiliser les composants Material

* [Directives des composants Material](https://material.io/design/components/)
    
* [Docs des composants Material Android](https://material.io/develop/android/components/bottom-app-bar/)
    

#### Écrire des tests !

Nous n'avons pas pu, mais vous devriez absolument ! Ne sautez pas les tests.

#### Se référer au code source

.. des applications qui font ces choses : [Application Sunflower](https://github.com/googlesamples/android-sunflower), [Application IO](https://github.com/google/iosched), [Application Dev Summit](https://github.com/google/iosched/tree/adssched) ou, bien sûr, l'[Application Bitotsav '19](https://github.com/aksh1618/Bitotsav-19) ! (et laissez une étoile ?)

#### Rester à jour

Abonnez-vous aux blogs et newsletters pour rester à jour ! En voici quelques-uns pour commencer : [Android Weekly](https://androidweekly.net/), [ProAndroidDev](https://proandroiddev.com), [AndroidPub](https://android.jlelse.eu), [Kotlin Weekly](http://www.kotlinweekly.net/). Submergé ? Consultez cette conférence géniale de [Huyen Tue Dao](https://www.freecodecamp.org/news/developing-an-android-app-in-2019-embracing-the-new-android/undefined) :

> [**Soyez comme l'eau : rester à jour avec Android**](https://academy.realm.io/posts/360-andev-2017-keynote-huyen-tue-keeping-up-with-android)  
> [_Si vous aimez les conférences de 360 AnDev, soutenez la conférence via Patreon ! La seule constante du travail dans le mobile est..._academy.realm.io](https://academy.realm.io/posts/360-andev-2017-keynote-huyen-tue-keeping-up-with-android)

Eh bien, nous y voilà. C'est un excellent moment pour le développement Android, alors lancez-vous avec votre nouvelle application, et n'oubliez pas de vous amuser en le faisant !

Si vous avez appris quelque chose, laissez un commentaire. Les critiques constructives sont les bienvenues ?

Retrouvez-moi sur [Twitter](https://twitter.com/aksh1618) ?, [LinkedIn](https://www.linkedin.com/in/aakarshit-uppal/?lipi=urn%3Ali%3Apage%3Ad_flagship3_feed%3BdcfpLfCgSPiW0Cox1OEGIQ%3D%3D&licu=urn%3Ali%3Acontrol%3Ad_flagship3_feed-identity_welcome_message) ? ou [GitHub ?](https://github.com/aksh1618)?

À la prochaine ??