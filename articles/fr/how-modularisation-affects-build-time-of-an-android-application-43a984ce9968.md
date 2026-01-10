---
title: Comment la modularisation peut accélérer le temps de construction de votre
  application Android
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-01-20T16:48:47.000Z'
originalURL: https://freecodecamp.org/news/how-modularisation-affects-build-time-of-an-android-application-43a984ce9968
coverImage: https://cdn-media-1.freecodecamp.org/images/1*J-1MC3QGbIuwq4tb-yr-iA.png
tags:
- name: Android
  slug: android
- name: android app development
  slug: android-app-development
- name: androiddev
  slug: androiddev
- name: gradle
  slug: gradle
- name: mobile app development
  slug: mobile-app-development
seo_title: Comment la modularisation peut accélérer le temps de construction de votre
  application Android
seo_desc: 'By Nikita Kozlov

  Developers will continue to add new features throughout an application’s lifetime.
  More code means not only longer build times — it means longer incremental build
  time.

  For teams with big projects, waiting for new builds could eventu...'
---

Par Nikita Kozlov

Les développeurs continueront à ajouter de nouvelles fonctionnalités tout au long de la durée de vie d'une application. Plus de code signifie non seulement des temps de construction plus longs — cela signifie également un temps de construction _incrémentiel_ plus long.

Pour les équipes avec de grands projets, attendre de nouvelles constructions pourrait éventuellement prendre 10-15% de leur journée de travail. Cela ne gaspille pas seulement le temps précieux des développeurs — cela rend également le développement piloté par les tests extrêmement fastidieux, ce qui nuit à la qualité globale du code.

Diviser une application en modules pourrait être une solution à ce problème. J'étais tenté de simplement diviser notre base de code par fonctionnalité, par couche, ou d'une autre manière rapide et évidente. Mais d'abord, j'ai décidé de créer une expérience et de collecter quelques données, afin de pouvoir prendre une décision mieux informée. Cet article explorera les résultats que j'ai collectés et mes conclusions.

Avant de plonger dans mon expérience, je voudrais parler de la théorie derrière tout cela, et expliquer comment nous pouvons diminuer le temps de construction incrémentiel.

### Un peu de théorie

Lorsque vous créez une application Android, vous devez avoir au moins un module _application_, c'est un module qui a appliqué le plugin d'application Gradle dans son fichier _build.gradle_ :

```
apply plugin: 'com.android.application'
```

En résultat de la construction de ce module, vous obtiendrez un fichier .APK.

Un module _application_ ne peut pas dépendre d'un autre. Il ne peut dépendre que d'une _bibliothèque_. C'est le module qui a appliqué le plugin de bibliothèque Gradle :

```
apply plugin: 'com.android.library'
```

En résultat de la publication d'un tel module, vous obtiendrez un fichier .AAR (Android Archive Library). Comparé au fichier .JAR, le .AAR a certaines choses liées à Android, par exemple, des ressources et un Manifest.

Le processus de construction pour tout module de bibliothèque ou d'application peut être _grossièrement_ divisé en cinq phases, qui peuvent être représentées avec certaines tâches Gradle :

1. **Préparation des dépendances.** Pendant cette phase, Gradle vérifie que toutes les bibliothèques dont ce module dépend sont prêtes. Si ce module dépend d'un autre, ce module serait également construit.
2. **Fusion des ressources et traitement du Manifest.** Après cette phase, les ressources et le Manifest sont prêts à être empaquetés dans le fichier résultat.
3. **Compilation.** Cette phase commence avec les Annotation Processors, au cas où vous les utilisez. Ensuite, le code source est compilé en byte code. Si vous utilisez AspectJ, le tissage se produit également ici.
4. **Post-traitement.** Toutes les tâches Gradle avec un préfixe « transform » font partie de cette phase. Les plus importantes sont : `transformClassesWithMultidexlist` et `transformClassesWithDex`. Elles produisent des fichiers .DEX.
5. **Emballage et publication.** Pour les bibliothèques, cette étape signifie créer un fichier .AAR à la fin, pour les applications — .APK.

Comme je l'ai mentionné, notre objectif est de minimiser le temps de construction incrémentiel. Il est difficile d'accélérer toutes les phases en une seule expérience, alors j'ai décidé de me concentrer sur les plus longues. Pour un projet avec un seul module, il s'agissait des phases de compilation et de post-traitement. La phase de fusion des ressources et de traitement du manifest peut également parfois être chronophage, mais si le code Java n'est pas touché, alors la construction incrémentielle est assez rapide.

Nous savons tous que Gradle exécute les tâches dans les constructions consécutives uniquement si l'entrée n'est pas la même. Il ne reconstruit également pas un module s'il n'a pas été modifié. Cela conduit à l'hypothèse suivante :

> « Le temps de construction incrémentiel pour un projet avec plusieurs modules est plus rapide que pour un projet à module unique, car seuls les modules modifiés sont recompilés. »

Très bien, découvrons si cela est vrai !

### Configuration de l'expérience

![Image](https://cdn-media-1.freecodecamp.org/images/m8SaIngTlbZkpYa4eqzV1F8hdi26pco4kVfE)

Le projet utilise les plugins Gradle v2.2.2. Le SDK Android minimal est 15, ce qui couvre la plupart des appareils selon le [tableau de bord des niveaux d'API](https://developer.android.com/about/dashboards/index.html). Tous les modules ont une dépendance sur _Butterknife_, pour rendre le projet un peu plus « vivant », puisque tous les projets ont des dépendances externes.

Dans toutes les variantes, le module d'application est appelé « app », tandis que les modules de bibliothèque sont appelés « app2 », « app3 », etc.

Chaque variante a au total environ 100 packages, 15 000 classes et 90 000 méthodes. Assemblé, cela fait deux fichiers DEX, presque trois. Le code généré est factice, pour garder toutes les méthodes dans le fichier .APK, la minification et la réduction ont été désactivées.

Toutes les mesures ont été effectuées avec le profileur intégré de Gradle. Pour l'utiliser, il suffit d'ajouter « --profile » à la fin de la commande, comme ceci :

```
./gradlew assembleDebug --profile
```

En résultat, vous obtiendrez un fichier .HTML avec les mesures.

Pour chaque configuration, j'ai répété chaque mesure 4 à 15 fois, pour m'assurer que mes résultats étaient reproductibles.

#### Générateur de code Java

Écrire toutes les 15 000 classes à la main est chronophage, alors j'ai écrit un générateur de code simple en Python. Il est disponible dans [Gist](https://gist.github.com/NikitaKozlov/ff9d8e65d9d880a2f35e1cac58a84990). Ci-dessous, vous pouvez trouver un schéma du code qu'il génère.

![Image](https://cdn-media-1.freecodecamp.org/images/OMOMY0Ji9nNhHYvfyKBdTcPmeC8fVujWWVYv)

Comme vous pouvez le voir, chaque méthode générée suivante appelle la précédente, et chaque première méthode de la classe suivante appelle la dernière méthode de la classe précédente. Cela rend le code plus couplé et augmente le temps de compilation.

#### Modules Java purs

Je n'ai pas fait d'expériences spéciales pour les modules Java purs. Mais j'ai un peu joué avec eux, et je peux dire qu'ils sont généralement plus rapides que ceux d'Android. Cela se produit parce que pendant la construction, moins de tâches sont exécutées, par exemple, il n'y a pas de ressources à fusionner.

Si vous êtes intéressé par les résultats pour les modules Java purs, veuillez écrire un commentaire. Ou vous pouvez cloner le projet depuis [GitHub](https://github.com/NikitaKozlov/GradleBuildExperiment) et le modifier selon vos besoins. Mais n'oubliez pas que les résultats réels dépendent du matériel. Pour pouvoir comparer vos résultats, veuillez répéter certaines expériences dans votre environnement également.

#### Petites pertes ici et là

Ce n'est pas une surprise que faire quelque chose en parallèle ralentit la construction. Même avoir un deuxième projet ouvert dans Android Studio peut rendre la construction 5 à 10 % plus lente. Écouter de la musique, regarder YouTube ou naviguer sur Internet augmente considérablement le temps de construction ! J'ai personnellement vu une accélération du processus de construction jusqu'à 30 % après avoir simplement fermé tout sauf Android Studio.

Toutes les expériences ont été réalisées avec seulement les onglets du navigateur nécessaires et un seul projet Android Studio ouvert.

### Faisons l'expérience

#### État initial

Comme point de départ, j'ai pris un projet avec un seul module contenant toutes les 15 000 classes. Pour cette configuration, le temps de construction incrémentiel est de _1m 10s_.

#### 3 Modules

La première étape consiste à diviser un module en trois : un module d'application et deux modules de bibliothèque. Le module d'application dépend des bibliothèques, mais les modules de bibliothèque sont indépendants les uns des autres. Chaque module a environ 5 000 classes et 30 000 méthodes.

Si des modifications sont apportées uniquement dans le module d'application, le temps de construction est d'environ 35 secondes. Presque 30 secondes de gain par rapport à l'état initial. Mais lorsqu'un des modules de bibliothèque est modifié, même si le module d'application n'est pas touché, le temps de construction incrémentiel passe à _1m 50s_. 40 secondes de plus !

Examinons le rapport de profil et voyons ce qui a pris tant de temps :

![Image](https://cdn-media-1.freecodecamp.org/images/haPhcC7iI9R6lMmNaSTWm-sEQ3LzTZg8hI41)

![Image](https://cdn-media-1.freecodecamp.org/images/4RI8AzAfrQCPVsDjVRt009zHjGdaUPo30Rbk)
_Rapporte de profil d'une construction incrémentielle avec des modifications dans le module de bibliothèque (« :app2 »). Puisque le module d'application (« :app ») dépend du module de bibliothèque, il est également recompilé._

Dans les captures d'écran ci-dessus, vous pouvez voir que la plupart du temps a été passé à construire le module de bibliothèque. Vous pouvez également remarquer que pour les modules de bibliothèque, les tâches de débogage et de publication ont été exécutées. Gradle a perdu du temps à exécuter deux ensembles de tâches au lieu d'un seul ! C'est pourquoi cela a pris 40 secondes de plus que le projet à module unique.

Nous pouvons éviter cela et rendre cette construction encore plus rapide que notre _1m 10s_ initial en divisant notre code en modules.

Mais ce n'est pas le seul problème. Examinons _comment_ notre module d'application dépend des modules de bibliothèque :

```
dependencies {    compile project(path: ':app2')    compile project(path: ':app3')}
```

Il y a un problème important dans le code ci-dessus : si une bibliothèque est ajoutée de cette manière, alors l'application dépend toujours de la variante _release_, indépendamment de son propre type de construction. Il n'a également pas d'importance quelle variante est choisie dans Android Studio. Voici ce que dit le [Guide de l'utilisateur du plugin Gradle](http://tools.android.com/tech-docs/new-build-system/user-guide#TOC-Library-Publication) à ce sujet :

> Par défaut, une bibliothèque ne publie que sa variante _release_. Cette variante sera utilisée par tous les projets référençant la bibliothèque, peu importe quelle variante ils construisent eux-mêmes. Il s'agit d'une limitation temporaire due aux limitations de Gradle sur lesquelles nous travaillons pour les supprimer.

Heureusement, il est possible de changer la variante dont dépend notre application.

Tout d'abord, ajoutez le code suivant au fichier _build.gradle_ des bibliothèques. Cela permettra à la bibliothèque de publier également la variante _debug_ :

```
android {    defaultConfig {        defaultPublishConfig 'release'        publishNonDefault true    }}
```

Deuxièmement, le module d'application doit dépendre des modules de bibliothèque comme ceci :

```
dependencies {    debugCompile project(path: ':app2', configuration: "debug")    releaseCompile project(path: ':app2', configuration: "release")    debugCompile project(path: ':app3', configuration: "debug")    releaseCompile project(path: ':app3', configuration: "release")}
```

Maintenant, la variante de débogage de notre application dépend de la variante de débogage des bibliothèques, et sa version de publication dépend de leurs versions de publication. Alors faisons quelques modifications au module _app2_ et reconstruisons-le. Après ces modifications, nous pouvons vérifier notre rapport de profil à nouveau :

![Image](https://cdn-media-1.freecodecamp.org/images/khyDy7gT4Hd8SiCz7rfoDlarUfRyGRCINpXs)

![Image](https://cdn-media-1.freecodecamp.org/images/D-udP9Ns1gkbTFHdcLh0AE7MDlkYoNb3jJ66)

La différence la plus significative est l'absence de _:app2:packageReleaseJarArtifact_, ce qui nous fait économiser environ 15 secondes. De plus, le temps est légèrement redistribué entre le reste des tâches, et nous obtenons _1m 32s_. Cela représente 18 secondes de plus que précédemment, mais toujours 22 secondes de plus que notre configuration initiale. Pour les modifications uniquement dans le module d'application, le temps de construction reste presque le même — _36 secondes_ contre _35 secondes_ dans notre configuration précédente.

Malheureusement, je n'ai pas trouvé d'explication appropriée pour laquelle il construit les deux versions. J'espère que lorsque cette limitation de Gradle sera résolue, ce problème disparaîtra également. Le même problème est discuté dans le [Suivi des problèmes AOSP](https://code.google.com/p/android/issues/detail?id=52962).

Je prévois également de passer du temps à expérimenter avec les tâches Gradle pour trouver une solution de contournement à ce problème. Une solution possible est d'exclure toutes les tâches de publication pour les constructions de débogage.

#### 5 Modules

Évidemment, le temps de construction dépend de la quantité de code. Si vous réduisez la quantité de code de moitié, la construction devrait également être environ deux fois plus rapide. Si au lieu de 3 modules, le projet est divisé en 5, alors le temps de construction devrait être environ 40 % plus rapide.

C'est presque vrai.

![Image](https://cdn-media-1.freecodecamp.org/images/JsR7H3b6U9J49HLLY6rV5BCsNnuCQIT0O4rx)

Si des modifications sont apportées uniquement dans le module d'application, le temps de construction incrémentiel est d'environ 24_s_. Pour les modifications dans un module de bibliothèque, la construction incrémentielle prend _50s_. Comparé au _1m 10s_ initial, c'est déjà un gain. Mais j'ai encore quelques astuces à ma disposition.

#### Réduire la taille du module d'application

Indépendamment du module modifié, le module d'application sera recompilé à chaque fois. Donc réduire sa taille a tout son sens. Idéalement, il devrait simplement assembler toute l'application à partir de modules séparés et pourrait également fournir un écran de démarrage, car l'écran de démarrage dépend souvent de nombreuses fonctionnalités.

C'est ainsi qu'est née l'idée des configurations _3+1_ et _5+1_. Dans les deux cas, le projet a un petit module d'application qui dépend de 3 et 5 modules de bibliothèque respectivement. Tous les modules de bibliothèque sont indépendants les uns des autres et ont des tailles égales. Voyons ce que cela nous donne :

![Image](https://cdn-media-1.freecodecamp.org/images/e5AZF2lz4WsblcBuK1WA94CRadMgF7lPrjr-)

Nous pouvons observer une nouvelle diminution du temps de construction incrémentiel. Même avec des modifications dans le module de bibliothèque, la configuration _5+1_ est construite presque deux fois plus vite qu'un projet à module unique initial. C'est un progrès décent.

#### Pourquoi le projet dépend-il réellement de Butterknife ?

C'est un point où je dois faire une confession. Il y avait une très forte raison d'ajouter une dépendance à _Butterknife_.

Dans la configuration initiale, la compilation incrémentielle prend _45s_ sur _1m 10s_, mais si _Butterknife_ est supprimé, le projet est compilé en seulement _15s_ ! Trois fois plus vite ! Toute la construction incrémentielle sans Butterknife est de _40s_.

Est-ce un problème dans la bibliothèque ?

Comme il s'est avéré — non. Sans _Butterknife_, le projet compile si rapidement grâce à la compilation incrémentielle Java réelle, qui est désactivée pour les projets utilisant des Annotation Processors. Vous pouvez trouver des problèmes liés dans [Gradle Jira](https://issues.gradle.org/browse/GRADLE-3259), dans le [Suivi des problèmes AOSP](https://code.google.com/p/android/issues/detail?id=200043), il est également suivi dans les [documents de conception de Gradle](https://github.com/gradle/gradle/blob/master/design-docs/incremental-java-compilation.md). Si vous examinez de plus près le problème du Suivi des problèmes AOSP, l'un des commentaires dit :

> « Les Annotation Processors ne sont pas encore pris en charge avec la compilation Java incrémentielle. Cela dépendra des changements dans Gradle. »

> « Nous l'avons désactivé pour les projets qui appliquent com.neenbedankt.android-apt, donc ce n'est plus un problème significatif. »

C'est pourquoi la construction devient simplement plus lente sans notification.

Personnellement, je ne supprimerai pas les Annotation Processors de tout le projet. Je trouve des bibliothèques comme _Dagger_ et _Butterknife_ utiles. Mais avoir quelques modules sans eux pourrait être une bonne idée, ce qui rendrait leurs constructions beaucoup plus rapides !

#### Une autre astuce — Augmenter le niveau de l'API

La compilation n'est pas la seule chose qui ralentit le processus de construction. La production de fichiers .DEX peut également être chronophage. Surtout si une application dépasse la limite DEX. L'utilisation de la configuration multidex augmente le temps de construction, le système de construction doit décider quelles classes vont dans quel fichier .DEX. Avec l'introduction de l'Android Runtime, la manière dont le système d'exploitation Android fonctionne avec les applications ayant plusieurs fichiers DEX a changé. Voici ce que dit la [documentation d'Android Studio](https://developer.android.com/studio/build/multidex.html#mdex-on-l) à ce sujet :

> « Android 5.0 (niveau d'API 21) et versions ultérieures utilisent un runtime appelé ART qui prend nativement en charge le chargement de plusieurs fichiers DEX à partir de fichiers APK. ART effectue une pré-compilation au moment de l'installation de l'application qui recherche les fichiers `classesN.dex` et les compile en un seul fichier `.oat` pour l'exécution par l'appareil Android. »

Cela conduit à une diminution du temps de construction. La raison est que chaque module produit ses propres fichiers DEX, qui sont inclus dans l'APK sans modification. Si vous regardez les tâches qui s'exécutent pendant la construction, vous remarquerez que `transformClassesWithMultidexlist` n'est plus exécuté. De plus, la compilation elle-même est devenue plus rapide. Vous pouvez trouver plus d'informations et des instructions sur la façon de créer une version qui utilise l'API 21 [ici](https://developer.android.com/studio/build/multidex.html#dev-build).

#### Configuration de construction la plus rapide atteinte.

Utiliser l'API 21 pour le débogage est un gain facile pour chaque projet. Je l'ai essayé pour la configuration _5+1_ et les résultats étaient incroyables :

![Image](https://cdn-media-1.freecodecamp.org/images/odoCUKJg-NQm9vl4yJKfZfh7jLCsxqEPqRAS)

Même pour les modifications dans le module de bibliothèque, le temps de construction incrémentiel était seulement de _17 secondes_ ! Mais tenez compte du fait que tous les modules sont indépendants les uns des autres. Une fois qu'une dépendance entre les modules est introduite, le temps de construction passe de _17s_ à _42s_ (dernière ligne du tableau ci-dessus) !

#### Développement du module de bibliothèque de manière pilotée par les tests

L'une des principales raisons pour lesquelles le développement piloté par les tests (TDD) est difficile pour un projet à module unique est le temps de construction. Le TDD encourage à exécuter les tests souvent. Exécuter les tests plusieurs fois par minute est une pratique normale. Mais lorsque la construction prend une minute ou deux, travailler de manière pilotée par les tests ne pourrait pas être très productif.

Avec l'introduction des modules, ce problème est résolu automatiquement. La construction d'un seul module dans la dernière configuration a pris seulement _9s_ ! Cela rend possible l'exécution des tests aussi souvent que nécessaire.

### Conclusion

![Image](https://cdn-media-1.freecodecamp.org/images/8hhEYND4vfQGxgZ-NOcL8YVohRxBHLHqjm3G)

Premièrement et surtout, l'hypothèse était correcte, la modularisation d'un projet peut considérablement accélérer le processus de construction, mais pas pour toutes les configurations.

Deuxièmement, si la division est faite de manière incorrecte, le temps de construction sera considérablement augmenté, car Gradle construit à la fois les versions release et debug des modules de bibliothèque.

Troisièmement, travailler de manière pilotée par les tests est beaucoup plus facile pour un projet avec plusieurs modules, car la construction d'un petit module de bibliothèque est bien plus rapide que celle de tout le projet.

Quatrièmement, faire beaucoup de choses en parallèle ralentit la construction. Donc avoir un matériel plus puissant est une bonne idée.

Ci-dessous, vous pouvez trouver les résultats de toutes les expériences décrites dans cet article :

![Image](https://cdn-media-1.freecodecamp.org/images/hxYQoAIaUGfb-dIVjjBmZVtiDyiPmpGyOOkw)

Veuillez voter pour les problèmes mentionnés. La résolution de l'un d'entre eux serait une énorme étape vers des constructions plus rapides. Ci-dessous, vous pouvez trouver tous les liens :

* [https://code.google.com/p/android/issues/detail?id=52962](https://code.google.com/p/android/issues/detail?id=52962)
* [_https://issues.gradle.org/browse/GRADLE-3259_](https://issues.gradle.org/browse/GRADLE-3259)
* [https://code.google.com/p/android/issues/detail?id=200043](https://code.google.com/p/android/issues/detail?id=200043)

Tout le code est publié sur [GitHub](https://github.com/NikitaKozlov/GradleBuildExperiment).

[**Nikita Kozlov (@Nikita_E_Kozlov) | Twitter**](https://twitter.com/Nikita_E_Kozlov)  
[_The latest Tweets from Nikita Kozlov (@Nikita_E_Kozlov): https://t.co/wmGSJ7snW1"_twitter.com](https://twitter.com/Nikita_E_Kozlov)

_Merci pour le temps que vous avez consacré à la lecture de cet article. Si vous l'aimez, n'oubliez pas de cliquer sur le_ ? _ci-dessous._