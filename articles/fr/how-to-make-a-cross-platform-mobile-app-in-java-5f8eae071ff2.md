---
title: Comment créer une application mobile multiplateforme en Java
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-23T14:53:37.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-a-cross-platform-mobile-app-in-java-5f8eae071ff2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0Yjn597lhtYUQR98fnfNiQ.png
tags:
- name: Android
  slug: android
- name: iOS
  slug: ios
- name: Java
  slug: java
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment créer une application mobile multiplateforme en Java
seo_desc: 'By Adrian D. Finlay

  Did you know that you can use Java to make cross platform mobile apps? Yes, pinch
  yourself, you read that right the first time! I’ll teach you the basics of how to
  use your existing Java knowledge to create performant apps on Andr...'
---

Par Adrian D. Finlay

Saviez-vous que vous pouvez utiliser Java pour créer des applications mobiles multiplateformes ? Oui, pincez-vous, vous avez bien lu dès la première fois ! Je vais vous apprendre les bases de l'utilisation de vos connaissances existantes en Java pour créer des applications performantes sur Android et iOS en 12 étapes faciles. Nous allons tout faire en utilisant JavaFX comme boîte à outils d'interface graphique.

Mais d'abord, un peu plus de contexte. Vous devrez répondre aux exigences suivantes pour pouvoir créer une application pour **Android** et iOS. Cependant, si vous ne souhaitez pas créer une application iOS, vous pouvez développer sur n'importe quelle machine x64 bits qui supporte Java SE 8. Ce projet sera un dépôt Git construit avec Gradle. Mais vous n'avez pas besoin de créer un dépôt Git.

Les exigences suivantes sont :

* Un JVM compatible JDK 1.8
* Les outils en ligne de commande Android (SDK v.27)
* XCode 9.2
* Gradle 4.2
* Git Large File Storage (v.2.5.0) (Inutile si vous ne souhaitez pas créer un dépôt git)
* De préférence au moins 4 Go de RAM

Impatient ? Vous voulez voir un résultat final ? Consultez le projet terminé ci-dessous.

[**afinlay5/OnyxFx**](https://github.com/afinlay5/OnyxFx)  
[_Dépôt de code source Gradle pour OnyxFx, une application JavaFX multiplateforme (Android/iOS/Linux/macOS/Windows) rendant..._github.com](https://github.com/afinlay5/OnyxFx)

Mon environnement de développement sera Fedora Linux 28 et macOS High Sierra. Maintenant que nous avons cela de côté, commençons.

### 1) Créer un dossier pour héberger le projet

J'ai hébergé mon projet, OnyxFx, comme suit : « **/home/adriandavid/Projects/OnyxFx** ». Vous êtes, bien sûr, libre d'héberger le projet où vous le souhaitez.

![Image](https://cdn-media-1.freecodecamp.org/images/1*14wz3bVNKav6LNbTAYjEhA.png)

### 2) Initialiser Gradle, Git, définir JAVA_HOME

Ouvrez un terminal dans le répertoire racine du projet. Si Gradle est correctement configuré, vous devriez voir quelque chose comme ceci après avoir exécuté la commande suivante :

```
gradle -v
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*kuAXbVwYzNd3XRsGHjRy-w.png)

Vous devez vous assurer que Gradle liste votre installation du Java Development Kit (JDK) 8 à côté de la section étiquetée « JVM ».

Bien qu'il existe de nombreuses façons de faire cela, la manière la plus simple est de s'assurer que votre variable d'environnement JAVA_HOME est correctement définie.

Selon votre environnement, il existe de nombreuses façons de faire cela. Une façon de le faire dans la plupart des environnements *nix est de définir la variable dans **/home/<user>/.bashrc** ou /etc/profile. Consultez le manuel de votre système d'exploitation pour vous assurer que votre variable d'environnement JAVA_HOME est correctement définie.

Vous pouvez inclure les lignes suivantes à la fin de .bashrc ou profile pour vous assurer que JAVA_HOME est correctement défini.

```
JAVA_HOME=/home/adriandavid/java/oracle_jdk1.8.0_181/export JAVA_HOME
```

**Note :** Vous pouvez installer le JDK 8 d'Oracle [ici](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html).

Ensuite, assurez-vous que le shell reflète les modifications ci-dessus en exécutant l'une des commandes suivantes :

```
source ~/.bashrcsource /etc/profile
```

Entrez la commande suivante pour vérifier que la variable est correctement définie :

```
echo $JAVA_HOME
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*kJZ9I_IqrhACbckpzh6ueA.png)

Si vous rencontrez toujours des difficultés ou si vous utilisez Microsoft Windows, consultez [ici](https://docs.oracle.com/cd/E19182-01/820-7851/inst_cli_jdk_javahome_t/).

Tout d'abord, exécutez `git init` dans le répertoire racine du projet pour initialiser le dépôt Git. **Note : si vous ne souhaitez pas héberger un dépôt git, vous pouvez sauter cette étape.**

Ensuite, exécutez `gradle init` dans le répertoire racine du projet pour initialiser le dépôt Gradle. Cette étape est obligatoire.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ab57WniSkAlmhElis7Aw3Q.png)

**Note :** Vous remarquerez que mon exemple semble légèrement différent. Cela est dû au fait que j'ai déjà initialisé Gradle et Git sur mon environnement local.

### 3) Devenez groovy ! Modifiez gradle.build

Espérons que _Earth, Wind, & Fire_ peut vous aider à devenir groovy ! Lancez votre éditeur de texte préféré et modifiez votre build.gradle situé dans le répertoire racine de votre projet et remplacez le contenu par le contenu du gist GitHub suivant.

Ces paramètres build.gradle configurent notre projet Gradle pour utiliser le plugin **javafxmobile**, qui est le cheval de bataille de notre projet. Vous pouvez en savoir plus sur le plugin [ici](https://github.com/javafxports/javafxmobile-plugin) et [ici](https://bitbucket.org/javafxports/javafxmobile-plugin). Parmi de nombreuses choses, le plugin javafxmobile automatise le processus de téléchargement (à partir de Maven Central ou jcenter) et d'ajout des SDK iOS et Android au chemin de classe de votre application.

Si vous êtes familier avec Gradle, Maven ou Ant, c'est super — vous avez probablement une idée de ce qui se passe. Si vous n'êtes pas familier avec Gradle, **ne vous en faites pas**. Tout ce que vous devez comprendre, c'est que Gradle est un outil de construction utilisé pour automatiser de nombreuses tâches impliquées dans la construction d'applications telles que : la récupération des dépendances, l'organisation du projet, et ainsi de suite.

Remarquez que nous ciblons Android 7.1 Nougat (version d'API 25) et iOS 11 (nous verrons où cela est fait sous peu). Vous pouvez ajuster ces valeurs comme vous le souhaitez. Notez, cependant, que dans le cas d'Android, vous devez vous assurer que la version de l'API correspond à la version du SDK que vous avez téléchargée (plus d'informations à ce sujet plus tard).

Enfin, je ne démontrerai pas la production d'exécutables signés dans ce tutoriel. Pour cette raison, _iOSSkipSigning_ est défini sur true et nous n'utilisons pas la tâche Gradle _releaseAndroid_. Vous pouvez, cependant, fournir les accommodations appropriées pour produire des applications signées.

### 4) Créez un nouveau fichier appelé gradle.properties et configurez-le

Créez un nouveau fichier dans le répertoire racine du projet appelé `gradle.properties` et ajoutez le contenu suivant au fichier.

```
robovm.device.name=iPhone-7robovm.sdk.version=11.0org.gradle.jvmargs=-Xms4g -Xmx8g
```

Ces paramètres indiquent au plugin javafxports d'utiliser un iPhone-7 comme émulateur embarqué, de cibler iOS 11, et de passer les flags Xms et Xmx au JVM, qui spécifient à la fois le pool de mémoire initial à 4 Go et le pool de mémoire heap maximum à 8 Go. Cela sera nécessaire pour la compilation de l'openJDK et le développement de la build iOS.

### 5) Installer Homebrew (iOS uniquement)

Si vous n'avez pas de Mac et que vous ne prévoyez pas de produire une build iOS, vous pouvez sauter cette étape.

Ouvrez le terminal dans macOS et collez la commande suivante.

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

### 6) Installer le socket de multiplexage USB (iOS uniquement)

Passez à cette étape uniquement si Homebrew est installé avec succès. Si vous n'avez pas de Mac et que vous ne prévoyez pas de produire une build iOS, vous pouvez sauter cette étape.

Ouvrez le terminal dans macOS et collez la commande suivante.

```
brew install usbmuxd
```

### 7) Récupérer les outils en ligne de commande Android

Récupérez les outils en ligne de commande Android pour votre plateforme [ici](https://developer.android.com/studio/#downloads). Après la fin du téléchargement, décompressez le dossier et collez le contenu dans le répertoire de votre choix. Pour moi, ce fut `/home/<user>/Android`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*cZFJp50kxOy9kORJ9VQX4Q.png)

### 8) Définir ANDROID_HOME, récupérer les packages Android nécessaires

Comme pour Java, Gradle doit savoir où chercher pour trouver les outils en ligne de commande Android. Il existe plusieurs façons de faire cela. Cependant, dans un souci de simplicité et de cohérence, nous définirons la variable d'environnement ANDROID_HOME dans ce tutoriel. Ajoutez la variable suivante de la même manière que nous l'avons fait pour JAVA_HOME. Par exemple :

```
ANDROID_HOME=/home/adriandavid/Android/ export ANDROID_HOME
```

N'oubliez pas de recharger le shell en ajoutant `source <fichier>` comme nous l'avons fait pour JAVA_HOME.

Maintenant, récupérez les outils nécessaires pour construire la build Android. Exécutez la commande suivante :

```
# *.nix./sdkmanager "platform-tools" "build-tools;25.0.3" "platforms;android-25" "extras;android;m2repository" "extras;google;m2repository"
```

```
or
```

```
#Windowssdkmanager "platform-tools" "build-tools;25.0.3" "platforms;android-25" "extras;android;m2repository" "extras;google;m2repository"
```

Faites bien attention à ce que la version du SDK et de l'API que nous avons spécifiée dans gradle.build corresponde à la version que nous avons spécifiée dans cette commande. À savoir, « 25 ». Si cela n'est pas aligné, la build ne réussira pas.

### 9) Créer la structure de répertoires de l'application

Pour automatiser le processus de création de ces répertoires, exécutez le script shell suivant.

Bourne-Again Shell / Korn Shell :

Windows Shell (cmd) :

Enregistrez le fichier sous mkpdir.bat ou mkpdir.sh et exécutez le fichier à partir du répertoire racine du projet en tant que **root** (ou **Administrateur**).

```
# *.nixchmod +x mkdir.sh-sh ./mkpdir.sh
```

```
# Windowsmkpdir
```

Remarquez que nous avons créé des répertoires pour embedded et desktop. Nous allons produire une build desktop, car cela ne nécessite pas de travail supplémentaire. Cependant, nous ne produirons aucune build pour les appareils embarqués.

### 10) Créez votre application JavaFX !

Accédez à /src/<platform>/java et commencez à développer votre application JavaFX ! Les ressources de l'application sont stockées dans /src/<platform>/resources.

Vous pouvez commencer par une simple application _Hello World_ ou consulter le code source que j'ai assemblé [ici](https://github.com/afinlay5/OnyxFx). OnyxFx est une application que j'ai créée, en suivant ces instructions, qui fait des appels REST via HTTP à l'API OnyxFx. L'API, à son tour, est un scraper web qui retournera les données statistiques (points par match, rebonds par match, passes décisives par match) pour le joueur et la saison de la NBA® spécifiés par le client. Il retourne les données au format JSON, qui sont ensuite analysées et affichées à l'écran de l'application mobile. N'hésitez pas à le modifier !

Gardez à l'esprit que bien que vous puissiez partager le code source, vous devez inclure des modifications personnalisées dans chaque copie du source, si vous souhaitez apporter des modifications spécifiques à l'appareil.

Notez également que le compilateur sous-jacent (le fork de RoboVM par MobiDevelop) ne supporte pas pleinement toutes les API Java 8. Si vous regardez de très près mon code source, vous remarquerez que dans la version iOS du code source, j'ai supprimé les API non supportées telles que **java.util.function.BiConsumer** et **java.util.Map.replace()**.

### 11) Créer un disque RAM pour les builds iOS (iOS uniquement)

Le processus de compilation pour iOS est très gourmand en ressources, car le plugin compilera l'ensemble de l'openJDK et d'autres bibliothèques deux fois pour créer un JAR fat qu'il utilisera pour construire votre application. Par conséquent, vous devriez créer un disque RAM pour répondre aux exigences de mémoire.

Cette étape, cependant, dépend de votre jugement sur les capacités de votre machine. Pour contexte, la machine macOS que j'ai utilisée pour compiler mon application iOS a 4 Go de RAM DDR2. J'ai décidé de créer un disque RAM de 8 Go. Pour ce faire, exécutez la commande suivante dans le terminal.

```
SIZE=8192 ; diskutil erasevolume HFS+ RoboVM RAM Disk `hdiutil attach -nomount ram://$((SIZE * 8192))`
```

### 12) Construisez et exécutez votre application !

Pour construire votre application, exécutez le wrapper Gradle dans le répertoire racine à partir du terminal comme suit.

```
./gradlew clean build
```

Cela produira une application de bureau empaquetée sous forme de JAR avec des scripts pour exécuter l'application fournis dans `/build/distributions/<AppName.tar>` ; et /build/distributions/<AppName.zip>. Si vous décompressez les répertoires, vous remarquerez la structure suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/1*oF-cta8Trg15kQLld7oitA.png)

Remarquez que dans /bin il y a des scripts pour exécuter l'application. Ces scripts dépendent de la préservation de la structure actuelle des dossiers. Remarquez également qu'il n'est pas nécessaire pour vous d'avoir **tree** installé. Il est utilisé ici simplement à des fins illustratives.

Il y a, en outre, un JAR autonome que vous pouvez utiliser pour exécuter l'application sur n'importe quel environnement de bureau supportant JavaFX 8. Pour exécuter l'application, exécutez l'une des commandes suivantes :

```
# Naviguez vers /build/distributions/<ProjectName>/
```

```
#Sur *.nixcd bin./<ProjectName>
```

```
#Sur Windowscd bin<ProjectName>
```

```
#Agnostique de la plateformejava -jar OnyxFxMobile.jar (ou double-cliquez, si le jvm est configuré pour exécuter les fichiers .jar)
```

```
Note : Si l'exécutable fournissant "java" n'est pas du même fournisseur et/ou de la même version que le JDK Java 8 avec lequel vous avez construit cette application, le jar peut ne pas s'exécuter. Les builds JavaFX 8 entre l'openJDK et le JDK Oracle sont incompatibles.
```

```
Sinon : /location/to/java8/bin/java -jar <ProjectName>
```

#### Voir les tâches Gradle de ce projet

Vous pouvez voir les tâches Gradle de ce projet en exécutant la commande suivante dans le répertoire racine du projet.

```
./gradlew tasks
```

#### Pour compiler, exécuter sur le bureau

La commande suivante exécutera votre projet dans l'environnement hôte.

```
./gradlew jar./gradlew run
```

Vous trouverez un jar autonome dans `build/libs/<AppName>.jar`.

#### Pour compiler, exécuter sur Android

```
./android #Génère un apk Android de débogage contenant l'application JavaFX.
```

```
./androidInstall #Lance l'application sur un appareil Android connecté.
```

```
./androidRelease #Génère un apk Android de release contenant l'application JavaFX.
```

```
Note : Vous devrez configurer un signingConfig valide lors de la publication d'un APK (javafxports).
```

Vous trouverez deux APK dans `build/javafxports/android`.  
Le premier s'appellera `<AppName>.apk`.  
Le second s'appellera `<AppName>-unaligned.apk`.

#### Pour compiler, exécuter sur iOS

```
./createIpa - Génère un ipa iOS contenant l'application JavaFX.
```

```
./launchIOSDevice - Lance l'application sur un appareil iOS connecté.
```

```
./launchIPadSimulator - Lance l'application sur un simulateur iPad.
```

```
./launchIPhoneSimulator - Lance l'application sur un simulateur iPhone.
```

Vous trouverez trois exécutables dans `build/javafxports/ios`.  
Le premier s'appellera `<AppName>.ipa`.  
Le second s'appellera `<AppName>.dSYM`.  
Le troisième s'appellera `<AppName>.app`.

### Quelques captures d'écran de mon application exemple

#### Sur le bureau

![Image](https://cdn-media-1.freecodecamp.org/images/1*0Yjn597lhtYUQR98fnfNiQ.png)

#### Sur Android

![Image](https://cdn-media-1.freecodecamp.org/images/1*YYNxKLhPNfKZe3Z3Ig9jFQ.png)

#### Sur iPhone

![Image](https://cdn-media-1.freecodecamp.org/images/1*rsyQ8wQJI-AeWeK56Z45Og.png)

#### Sur iPad

![Image](https://cdn-media-1.freecodecamp.org/images/1*rAVDpDXcdQkNzDDol5p3hQ.png)

#### Écran de démarrage

![Image](https://cdn-media-1.freecodecamp.org/images/1*_HKrh4pQXXwupdd70yomgg.png)

### Mes réflexions finales

_javafxports_ est un projet prometteur qui vise à amener JavaFX et la plateforme Java SE sur les appareils mobiles et autres. D'une certaine manière, l'outil parallèle Xamarin dans ses efforts. Cependant, le projet a encore beaucoup de travail à faire.

Pour commencer, le plugin ne supporte pas encore pleinement Java 8. Sur Android, il utilise retrolambda pour gérer les expressions lambda et les références de méthodes Java 8. Techniquement, il est à jour jusqu'à Java 6. Des dépendances supplémentaires font en sorte que vous pouvez utiliser Java 8. Cependant, le processus est simple, les builds fonctionnent comme prévu, et le temps de compilation n'est pas trop long.

Sur iOS, cependant, les builds sont extrêmement gourmands en mémoire et le processus de compilation prend très longtemps. Voici un extrait du journal pour la tâche ./gradlew createIpa.

```
:createIpa (Thread[Task worker for :,5,main]) completed. Took 1 hrs 46 mins 40.198 secs.
```

Au total, le processus a consommé environ 6 Go de RAM sur ma machine. Ce n'est pas idéal. Cependant, l'avenir est prometteur. Une entreprise appelée Gluon a développé un JVM personnalisé haute performance, entièrement modulaire, supportant pleinement Java 9, dont vous pouvez lire plus [ici](https://gluonhq.com/products/mobile/vm/).

_Cet article est initialement publié dans la section blog de ma page d'accueil, [ici](http://www.adriandavid.me/blog/24/how-to-make-a-cross-platform-mobile-app-with-java.xhtml)._

### Ressources à explorer :

* Dépôt Git du plugin JavaFxMobile : [https://github.com/javafxports/javafxmobile-plugin](https://github.com/javafxports/javafxmobile-plugin)
* Documentation JavaFxPorts : [http://docs.gluonhq.com/javafxports/#_how_it_works](http://docs.gluonhq.com/javafxports/#_how_it_works)
* Page d'accueil JavaFxPorts : [http://javafxports.org/](http://javafxports.org/)
* Documentation Gluon : [https://gluonhq.com/developers/documentation/](https://gluonhq.com/developers/documentation/)
* Page Google Groups pour JavaFxPorts : [https://groups.google.com/forum/#!forum/javafxports](https://groups.google.com/forum/#!forum/javafxports)
* Page StackOverflow pour JavaFxPorts : [https://stackoverflow.com/questions/tagged/javafxports](https://stackoverflow.com/questions/tagged/javafxports)
* Options de tarification/licence Gluon Mobile : [https://gluonhq.com/products/mobile/buy/](https://gluonhq.com/products/mobile/buy/)

![Image](https://cdn-media-1.freecodecamp.org/images/1*SWVp-cGi_ipjWWw3SU5ITQ.jpeg)
_Source : [Looney Tunes Ending](https://www.youtube.com/watch?v=0FHEeG_uq5Y" rel="noopener" target="_blank" title=")_