---
title: Les bases de la programmation Kotlin pour les débutants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-07T22:23:00.000Z'
originalURL: https://freecodecamp.org/news/kotlin-programming-basics-for-beginners
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9cb4740569d1a4ca33b8.jpg
tags:
- name: Kotlin
  slug: kotlin
- name: toothbrush
  slug: toothbrush
seo_title: Les bases de la programmation Kotlin pour les débutants
seo_desc: 'What is Kotlin?

  Kotlin is a programming language developed by Jetbrains, the company behind some
  of the world’s most popular IDEs like IntelliJ and Pycharm.

  It serves as a replacement for Java and runs on the JVM. It has been in development
  for close...'
---

## Qu'est-ce que Kotlin ?

[Kotlin](https://kotlinlang.org/) est un langage de programmation développé par [Jetbrains](https://www.jetbrains.com/), l'entreprise derrière certains des environnements de développement intégrés (IDE) les plus populaires au monde comme IntelliJ et Pycharm.

Il sert de remplacement pour Java et s'exécute sur la JVM. Il est en développement depuis près de 6 ans et a atteint la version 1.0 il y a un an.

La communauté des développeurs a adopté Kotlin à un point tel que Google a annoncé un support de première classe pour le langage pour le développement Android lors de la [Google I/O 2017](https://blog.jetbrains.com/kotlin/2017/05/kotlin-on-android-now-official/).

## **Version**

Au moment de la rédaction de cet article, la dernière version stable de Kotlin est la [version 1.2.71](https://blog.jetbrains.com/kotlin/2018/09/kotlin-1-2-70-is-out/)

## **Installation**

Avant de procéder aux instructions d'installation de Kotlin, vous devez vous assurer que vous avez configuré le **JDK (Java Development Kit)** sur votre système.

Si vous n'avez pas le JDK installé sur votre ordinateur, rendez-vous dans la **section Installation** sur [ce lien pour apprendre](https://guide.freecodecamp.org/java) comment le configurer.

Kotlin fonctionne avec le **JDK 1.6+**, assurez-vous donc d'installer la version correcte. Une fois que vous avez terminé la configuration du JDK, procédez aux étapes suivantes.

## **IntelliJ IDEA**

Le moyen le plus rapide de faire fonctionner Kotlin sur vos machines est de l'utiliser avec **IntelliJ IDEA**. Il s'agit de l'IDE recommandé pour Kotlin en raison du support d'outillage fourni par Jetbrains. Vous pouvez télécharger la [édition communautaire](http://www.jetbrains.com/idea/download/index.html) d'IntelliJ depuis [JetBrains](https://www.jetbrains.com/).

Une fois que vous avez installé IntelliJ, vous pouvez commencer votre premier projet en Kotlin sans aucune configuration supplémentaire.

Créez un **nouveau projet** et assurez-vous de sélectionner le module Java. Sélectionnez la case à cocher Kotlin sur cet écran.

![nouvel écran de projet](https://kotlinlang.org/assets/images/tutorials/getting-started/new_project_step1.png)

Donnez un nom à votre projet et cliquez sur Terminer.

![nom du projet](https://kotlinlang.org/assets/images/tutorials/getting-started/project_name.png)

Vous serez maintenant redirigé vers l'éditeur principal où vous verrez vos fichiers de projet organisés de la manière suivante.

![structure du projet](https://kotlinlang.org/assets/images/tutorials/getting-started/folders.png)

Pour vérifier votre installation, créez un nouveau fichier Kotlin dans le dossier **src** et nommez-le **app** (ou autre chose qui vous convient).

![structure du projet](https://kotlinlang.org/assets/images/tutorials/getting-started/new_file.png)

Une fois le fichier créé, tapez le code traditionnel Hello World suivant. Ne vous inquiétez pas si cela n'a pas de sens tout de suite, cela sera traité en détail plus tard dans le guide.

```text
fun main (args: Array<String>) {
    println("Hello World!")
}
```

![structure du projet](https://kotlinlang.org/assets/images/tutorials/getting-started/hello_world.png)

Vous pouvez maintenant exécuter ce programme en cliquant sur l'icône Kotlin dans la gouttière (côté gauche de votre éditeur avec les numéros de ligne).

![hello world](https://kotlinlang.org/assets/images/tutorials/getting-started/run_default.png)

Si tout se passe bien, vous devriez voir le message Hello World! dans votre fenêtre d'exécution comme montré ci-dessous.

![fenêtre d'exécution](https://kotlinlang.org/assets/images/tutorials/getting-started/run_window.png)

## **Eclipse**

Bien qu'IntelliJ soit l'IDE recommandé pour développer avec Kotlin, ce n'est définitivement pas la seule option disponible. **Eclipse** est un autre IDE populaire parmi les développeurs Java et Kotlin est également supporté par Eclipse.

Après avoir configuré le **JDK** sur votre système, suivez les instructions ci-dessous.

Téléchargez [**Eclipse Neon**](https://www.eclipse.org/downloads/) pour votre système d'exploitation et une fois que vous l'avez installé avec succès sur votre système, téléchargez le **plugin Kotlin** pour Eclipse depuis le [**Eclipse Marketplace**](http://marketplace.eclipse.org/content/kotlin-plugin-eclipse).

![marketplace eclipse](https://kotlinlang.org/assets/images/tutorials/getting-started-eclipse/marketplace.png)

**_NOTE : Vous pouvez également faire de même en allant dans Help -> Eclipse Marketplace et en recherchant Kotlin Plugin_**

Une fois le plugin installé, vous avez pratiquement terminé, mais il serait bon de tester l'IDE avec un rapide exemple Hello World.

Créez un nouveau projet Kotlin en cliquant sur File -> New -> Kotlin Project

![nouveau projet kotlin](https://kotlinlang.org/assets/images/tutorials/getting-started-eclipse/new-project.png)

Un projet vide sera créé avec une structure de répertoires assez similaire à un projet Java. Cela ressemblera à quelque chose comme ceci.

![projet kotlin vide](https://kotlinlang.org/assets/images/tutorials/getting-started-eclipse/empty-project.png)

Allez-y et créez un nouveau fichier Kotlin dans le dossier **src**

Une fois cela fait, tapez le code suivant. Ne vous inquiétez pas si cela n'a pas de sens pour l'instant, cela sera couvert plus tard dans le guide.

```text
fun main (args: Array<String>) {
    println("Hello World!")
}
```

![eclipse hello world](https://kotlinlang.org/assets/images/tutorials/getting-started-eclipse/hello-world.png)

Maintenant que vous avez terminé de taper le code Hello World, allez-y et exécutez-le. Pour exécuter le fichier, cliquez avec le bouton droit n'importe où dans l'éditeur et cliquez sur **_Run As -> Kotlin Application_**

![exécuter l'application eclipse](https://kotlinlang.org/assets/images/tutorials/getting-started-eclipse/run-as.png)

Si tout se passe bien, la fenêtre de la console s'ouvrira pour vous montrer la sortie.

![exécuter l'application eclipse](https://kotlinlang.org/assets/images/tutorials/getting-started-eclipse/output.png)

## **Utilisation du compilateur autonome sur le terminal**

Si vous êtes quelqu'un qui préfère faire les choses de manière plus manuelle et ne souhaitez pas vous lier à un éditeur/IDE, vous pourriez vouloir utiliser le compilateur Kotlin.

### **Téléchargement du compilateur**

Avec chaque version de Kotlin, Jetbrains fournit un compilateur autonome qui peut être téléchargé depuis les [versions GitHub](https://github.com/JetBrains/kotlin/releases/tag/v1.1.51). La version 1.1.51 est la dernière au moment de la rédaction de cet article.

### Installation manuelle

Une fois que vous avez téléchargé le compilateur, vous devez le décompresser et procéder à l'installation standard en utilisant l'assistant d'installation. L'ajout du répertoire **bin** au chemin du système est une étape facultative. Il contient les scripts nécessaires pour compiler et exécuter Kotlin sur Windows, Linux et macOS.

### Installation via Homebrew

Vous pouvez installer le compilateur sur macOS en utilisant [Homebrew](http://brew.sh/) qui est un gestionnaire de paquets pour macOS. Lancez l'application Terminal et exécutez les commandes suivantes

```text
$ brew update
$ brew install kotlin
```

### Installation via SDKMAN!

Une autre façon simple d'installer le compilateur Kotlin sur macOS, Linux, Cygwin, FreeBSD et Solaris est d'utiliser [SDKMAN!](http://sdkman.io/). Lancez le terminal et exécutez les commandes suivantes

`$ curl -s https://get.sdkman.io | bash`

Suivez les instructions à l'écran et une fois que SDKMAN! est configuré, exécutez la commande suivante dans le terminal

`$ sdk install kotlin`

Comme pour toutes les options d'installation précédentes, il serait bon de tester l'installation.

Ouvrez un éditeur de texte de votre choix et écrivez un programme Kotlin de base donné ci-dessous

```text
fun main(args: Array<String>) {
    println("Hello, World!")
}
```

Enregistrez ce fichier avec une extension **.kt**. Vous êtes maintenant prêt à le compiler et à voir les résultats. Pour ce faire, exécutez la commande suivante

`$ kotlinc hello.kt -include-runtime -d hello.jar`

L'option `-d` indique au compilateur ce que vous voulez que la sortie soit appelée. L'option `-include-runtime` rend le fichier .jar résultant autonome et exécutable en incluant la bibliothèque d'exécution Kotlin.

Si aucune erreur de compilation n'est survenue, exécutez l'application en utilisant la commande suivante

`$ java -jar hello.jar`

Si tout se passe bien, vous devriez voir **Hello World!** imprimé sur l'écran de votre terminal

```text
$ java -jar hello.jar       
Hello, World!
```

Félicitations, vous avez réussi à configurer le compilateur Kotlin et l'environnement de développement sur votre système. Nous couvrirons toutes les subtilités et les parties amusantes de Kotlin dans ce guide, mais vous pouvez prendre de l'avance si vous le souhaitez en allant sur le site [Try Kotlin](https://try.kotlinlang.org/) et en suivant les exercices.

## **Documentation**

L'une des meilleures choses à propos de Kotlin est sa documentation complète et bien structurée. Même si vous êtes nouveau en programmation, vous vous sentirez chez vous avec les docs. Ils font un travail assez incroyable en présentant tout de manière bien structurée. Vous pouvez consulter la documentation officielle à [ce lien](https://kotlinlang.org/docs/reference/).

## Plus d'informations sur Kotlin

* [Développer des applications Android natives avec Kotlin - Cours complet](https://www.freecodecamp.org/news/learn-how-to-develop-native-android-apps-with-kotlin-full-tutorial/)
* [Pourquoi vous devriez essayer Kotlin au lieu de Java](https://www.freecodecamp.org/news/still-using-java-for-android-development-you-should/)
* [Comment créer une application de messagerie Android avec Kotlin](https://www.freecodecamp.org/news/how-to-build-an-android-messenger-app-with-online-presence-using-kotlin-fdcb3ea9e73b/)