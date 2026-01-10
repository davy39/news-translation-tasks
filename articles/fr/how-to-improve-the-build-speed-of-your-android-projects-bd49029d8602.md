---
title: Comment améliorer la vitesse de build de vos projets Android
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-17T15:53:54.000Z'
originalURL: https://freecodecamp.org/news/how-to-improve-the-build-speed-of-your-android-projects-bd49029d8602
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ePDs8qm8U0AHF6chIqHvnA.jpeg
tags:
- name: Android
  slug: android
- name: Java
  slug: java
- name: Kotlin
  slug: kotlin
- name: Productivity
  slug: productivity
- name: 'tech '
  slug: tech
seo_title: Comment améliorer la vitesse de build de vos projets Android
seo_desc: "By Prateek Phoenix\nRecently, I undertook the task of migrating the Android\
  \ codebase at Kure to AndroidX. It seemed like the perfect opportunity to try and\
  \ fix the build speeds of the project. \nGradle has always had a bad rep for being\
  \ slow and resour..."
---

Par Prateek Phoenix

Récemment, j'ai entrepris la tâche de migrer la base de code Android chez [Kure](http://kureapp.com) vers AndroidX. Cela semblait être l'occasion parfaite pour essayer de corriger les vitesses de build du projet. 

Gradle a toujours eu une mauvaise réputation pour être lent et gourmand en ressources, mais j'ai été assez surpris de voir comment des modifications mineures de la configuration de build du projet pouvaient améliorer massivement les vitesses de build.

Pour vous donner un aperçu du temps que j'ai pu économiser sur nos builds propres, voici une métrique avant et après à partir de l'analyse de build.

![Image](https://cdn-media-1.freecodecamp.org/images/0-6xszNVvl-pP-OilKYuyq7jcTByO52w3E1D)
_pré-optimisation ??_

![Image](https://cdn-media-1.freecodecamp.org/images/KcwLYxol8gNXG3VRm59SAEukx0-nGvnLoQdt)
_post-optimisation ⚡⚡_

Passer de 5,5 minutes à **17 secondes ?? C'est fou.**

Il est facile de s'emballer avec les optimisations que vous pouvez effectuer pour réduire encore plus votre temps de build. Mais je vais intentionnellement me concentrer sur les mesures mineures et indolores que j'ai prises pour approcher cette métrique, afin de garder cet article accessible aux débutants.

### Mais d'abord !

Avant de commencer l'optimisation, il est important de benchmarker notre projet pour voir combien de temps il prend actuellement pour construire. Gradle dispose d'une option d'analyse pratique que vous pouvez utiliser pour analyser les performances de votre tâche. Lancez le terminal dans Android Studio et exécutez la commande suivante :

```
./gradlew assembleDebug --scan
```

Une fois le build terminé avec succès, il vous invitera à accepter les conditions de service pour télécharger les résultats de votre analyse de build. Tapez **yes** pour continuer. Une fois la publication terminée, vous obtiendrez un lien dans le terminal pour vérifier votre analyse de build. Ouvrez le lien.

> Il y a plusieurs options sur le site, mais pour faire court, nous allons seulement jeter un coup d'œil à ce qui est le plus important.

La vue de résumé vous montre un résumé des tâches qui ont été exécutées et combien de temps elles ont pris pour se terminer. Mais ce qui nous intéresse ici, c'est la section **Performance**. Elle vous donne une ventilation plus détaillée du temps total de build comme montré ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/fQSMqur3f98DHDkLjr77fxG-DSJ3l46R-rwB)

Dans la section performance, il y a un onglet **Settings and suggestions** qui vous donne des suggestions sur la façon d'améliorer vos vitesses de build. Jetons un coup d'œil à cela.

![Image](https://cdn-media-1.freecodecamp.org/images/BPzUZVTnbe25aKNYE8csrTw37-PcaAF2STIb)

Nous pouvons trouver quelques correctifs faciles pour notre vitesse de build dans cette section. Alors, appliquons ces suggestions dans notre projet.

### Étape #1 : Mettre à jour vos outils

L'équipe Android améliore et fait évoluer constamment le système de build Android. Donc, la plupart du temps, vous pouvez recevoir des améliorations significatives simplement en adoptant la dernière version des outils.

Au moment de cette refactorisation, notre projet était sur la **version 3.2.1** du plugin Gradle pour Android Studio _(qui est quelques versions plus ancienne que la dernière sortie)._

Vous pouvez visiter [**ce lien**](https://developer.android.com/studio/releases/gradle-plugin) pour obtenir la version de la dernière sortie du plugin Gradle.

Au moment de la rédaction de cet article, la dernière version est la **version 3.4.0.**

Mais elle vient avec un piège dont nous devons nous souvenir pour plus tard :

![Image](https://cdn-media-1.freecodecamp.org/images/paGQGAiNaEorLPkxz9cyOLkXMs4XqWSXB8y8)
_[https://developer.android.com/studio/releases/gradle-plugin](https://developer.android.com/studio/releases/gradle-plugin" rel="noopener" target="_blank" title=")_

> Lorsque vous utilisez **Gradle 5.0 et au-dessus**, nous devrons explicitement augmenter la taille du tas pour nous assurer que notre vitesse de build ne se dégrade pas. Nous reviendrons sur ce point dans une minute.

Ouvrez le fichier **build.gradle** de niveau supérieur que vous trouverez à la racine de votre projet et ajoutez la ligne suivante dans la **section des dépendances** :

```
classpath 'com.android.tools.build:gradle:3.4.0'
```

Vous devrez également mettre à jour l'**URL de distribution** dans le fichier des propriétés du wrapper gradle situé à **_gradle/wrapper/gradle-wrapper.properties._** Mettez à jour l'URL comme suit.

_(Ce lien sera disponible sur la [page de sortie du plugin Android Gradle](https://developer.android.com/studio/releases/gradle-plugin).)_

```
distributionUrl=https\://services.gradle.org/distributions/gradle-5.1.1-all.zip
```

Si vous utilisez Kotlin dans votre projet, vous rencontrerez une erreur si la version de votre plugin Kotlin Gradle est inférieure à **1.3.0**. Si c'est le cas, utilisez l'invite de l'IDE pour mettre à jour votre plugin Kotlin Gradle à la dernière version _(qui, au moment de la rédaction de cet article, est la **version 1.3.31**)._

Très bien, relançons le build à partir du terminal pour voir si nous avons obtenu des améliorations.

![Image](https://cdn-media-1.freecodecamp.org/images/1VQvb91yf-nxNMXSNH6J6efMBvjoyzzMLnn4)

### Étape #2 : Mettre à jour vos configurations

Nous avons donc pu économiser environ 2,5 minutes sur le temps de build, mais ce n'est toujours pas suffisant. En examinant les logs de build dans le terminal, je suis tombé sur une ligne qui nous intéresse :

![Image](https://cdn-media-1.freecodecamp.org/images/3UtgIeJxNxWUfqwQ-aswTFqEJQpJ8kx-g8zc)

La compilation incrémentielle empêche essentiellement la compilation gaspilleuse de l'ensemble du jeu de fichiers sources et compile uniquement les fichiers qui ont changé. En regardant les logs, il est clair que nous ne tirons pas parti de cette fonctionnalité. Il nous suggère d'utiliser **_android.enableSeparateAnnotationProcessing=true_** mais comme nous utilisons Kotlin dans nos projets, nous ne devrions pas utiliser la configuration _'annotationProcessor'_ de toute façon.

Heureusement, Kotlin **version 1.3.30** a ajouté le support pour le traitement incrémentiel des annotations.

![Image](https://cdn-media-1.freecodecamp.org/images/ACEJQNcm29SbUFkkGGHdpZymgkA6-Dj911oR)
_[https://kotlinlang.org/docs/reference/kapt.html](https://kotlinlang.org/docs/reference/kapt.html" rel="noopener" target="_blank" title=")_

Alors, faisons ce qui suit :

1. Changer la configuration **annotationProcessor** en **kapt**
2. Activer le flag expérimental **incremental annotation processing**

Ouvrez votre fichier **_build.gradle_** au niveau du module et ajoutez la ligne suivante en haut du fichier :

```
apply plugin: 'kotlin-kapt'
```

Ensuite, changez toutes les configurations annotationProcessor dans la section des dépendances pour utiliser kapt. Voici un exemple :

```
//Avant
annotationProcessor 'com.google.dagger:dagger-compiler:2.9'

//Après
kapt 'com.google.dagger:dagger-compiler:2.9'
```

Ouvrez maintenant votre fichier **_gradle.properties_** situé à la racine de votre projet et ajoutez la ligne suivante :

```
kapt.incremental.apt=true
```

Relançons le build. ??????

![Image](https://cdn-media-1.freecodecamp.org/images/-Bm0-tgHPB7Q5i4VGVbhkMlk1u432-qP4VEL)

Très bien, on dirait que nous y arrivons.

### Étape #3 : Propriétés Gradle

Nous sommes dans la dernière étape maintenant. Vous souvenez-vous du piège que nous avons rencontré lors de la mise à jour de notre version du plugin Gradle ? Il s'avère que les nouvelles versions de Gradle réduisent la taille du tas à 512 Mo. Cela est fait pour s'assurer que les machines de bas de gamme ne s'étouffent pas. Je suis sur une machine de 16 gigas, donc je peux me permettre de donner environ 2-3 gigas au démon Gradle, mais cela peut varier pour vous.

Ouvrez le fichier **_gradle.properties_** situé à la racine de votre projet et ajoutez la ligne suivante. N'oubliez pas de sélectionner la taille en fonction de vos besoins et des spécifications de votre machine.

```
org.gradle.jvmargs=-Xmx3072m -XX:MaxPermSize=512m -XX:+HeapDumpOnOutOfMemoryError -Dfile.encoding=UTF-8
```

Pendant que nous y sommes, activons également les builds parallèles et configurons à la demande dans les propriétés.

Voici à quoi ressemble mon fichier **_gradle.properties_** final :

```
org.gradle.jvmargs=-Xmx3072m -XX:MaxPermSize=512m -XX:+HeapDumpOnOutOfMemoryError -Dfile.encoding=UTF-8

org.gradle.parallel=true

org.gradle.configureondemand=true

kapt.incremental.apt=true
```

* `org.gradle.parallel` - Ce flag permet à Gradle de construire des modules au sein d'un projet en parallèle au lieu de séquentiellement. Cela n'est bénéfique que dans un projet multi-modules.
* `org.gradle.configureondemand` - Ce flag configure uniquement les modules nécessaires au projet, au lieu de construire tous les modules.

Avec ces configurations, voyons où nous en sommes sur notre métrique de vitesse de build :

![Image](https://cdn-media-1.freecodecamp.org/images/n9j1jXgfMdiXBu2MHRS361dbrLARbkrv-jOc)

![Image](https://cdn-media-1.freecodecamp.org/images/tB5MZOlTI7pI7XJzeLHeGjQ295mkEoK1WGvW)

Et voilà. ???

### Remarques finales

Ceci n'est en aucun cas une couverture exhaustive de toutes les façons dont on peut optimiser la vitesse de build de leur projet. Il y a beaucoup d'autres choses que je n'ai pas abordées dans cet article, comme l'utilisation de minSdk 21 lors de l'utilisation de MultiDex, la pré-dexification de vos bibliothèques, la désactivation du crunching PNG, et ainsi de suite — pour n'en nommer que quelques-unes.

Mais la plupart de ces configurations nécessitent une compréhension plus approfondie du système de build d'Android et une expérience de travail sur de grands projets multi-modules _(c'est là que les avantages sont les plus apparents)_. Les étapes que j'ai mentionnées ci-dessus sont faciles à incorporer dans un projet même par des développeurs juniors et ont des retours considérables. J'espère que cela vous aidera à réduire vos temps de build !

Très bien, jusqu'à la prochaine fois, paix ! ✌?