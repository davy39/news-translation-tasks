---
title: Comment installer Java dans Ubuntu – Tutoriel JDK Linux
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-06-28T19:21:28.000Z'
originalURL: https://freecodecamp.org/news/how-to-install-java-in-ubuntu-jdk-linux-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/how-to-install-java.png
tags:
- name: Java
  slug: java
- name: Linux
  slug: linux
- name: Ubuntu
  slug: ubuntu
seo_title: Comment installer Java dans Ubuntu – Tutoriel JDK Linux
seo_desc: "By Sebastian Sigl\nJava is one of the most popular programming languages\
  \ in use today. And a clean setup lets you seamlessly install Java and switch between\
  \ different versions when you're building applications. \nIn this tutorial you will\
  \ learn how to:..."
---

Par Sebastian Sigl

Java est l'un des langages de programmation les plus populaires utilisés aujourd'hui. Une installation propre vous permet d'installer Java de manière transparente et de basculer entre différentes versions lorsque vous construisez des applications. 

Dans ce tutoriel, vous apprendrez comment :

* Installer n'importe quelle version de Java,
* Basculer entre les versions de Java,
* Mettre à jour vers la dernière version de Java.

Le guide fourni devrait fonctionner pour la plupart des systèmes d'exploitation. Je l'ai testé pour les versions Linux suivantes :

* Ubuntu
* Debian
* MacOS

## Java Development Kit

> Le Java Development Kit (JDK) est un environnement de développement pour construire des applications, des applets et des composants en utilisant le langage de programmation Java. ([Source](https://www.oracle.com/java/technologies/javase/jdk-jdk-7-readme.html))

Le JDK contient différentes applications, y compris

> `javac`, le [compilateur Java](https://en.wikipedia.org/wiki/Java_compiler), qui convertit le code source en [bytecode Java](https://en.wikipedia.org/wiki/Java_bytecode).  
>   
> `java`, le [chargeur](https://en.wikipedia.org/wiki/Loader_(computing)) pour les applications Java. Cet outil est un interpréteur et peut interpréter les fichiers de classe générés par le compilateur [javac](https://en.wikipedia.org/wiki/Javac).   
>   
> Maintenant, un seul lanceur est utilisé pour le développement et le déploiement. L'ancien lanceur de déploiement, jre, ne vient plus avec Sun JDK, et a été remplacé par ce nouveau chargeur java. ([Source](https://www.javatpoint.com/jdk))

Les outils de construction Java (Maven, Gradle, etc.) et vos éditeurs de code utilisent des applications Java en arrière-plan pour offrir aux développeurs une expérience agréable pour exécuter, créer et maintenir des applications.

Voyons comment installer Java dans un environnement Linux en utilisant le terminal. Cela vous permet d'utiliser les étapes dans votre propre environnement Linux et dans de nombreux environnements distants.

## Comment utiliser SDKMan pour gérer les versions de Java

> SDKMAN! est un outil pour gérer des versions parallèles de plusieurs kits de développement logiciel sur la plupart des systèmes basés sur Unix. Il fournit une interface de ligne de commande (CLI) et une API pratiques pour installer, basculer, supprimer et lister les candidats. ([Source](https://sdkman.io/))

SDKMan est livré avec son propre installeur, qui prend en charge de nombreux systèmes d'exploitation. Assurez-vous d'installer curl au préalable, puis exécutez le script d'installation.

### Comment installer SDKMan sur Ubuntu 22

```sh
# installer curl
$ sudo apt install curl

# installer sdkman
$ curl -s "https://get.sdkman.io" | bash
```

### Comment installer SDKMan sur Debian 11

```sh
# se connecter en tant que root
$ su

# installer curl
$ apt install curl zip

# quitter la session utilisateur root
$ exit

# installer sdkman
$ curl -s "https://get.sdkman.io" | bash
```

### Comment installer SDKMan sur MacOS

Au cas où vous n'auriez pas encore brew et curl sur Mac, vous devez les installer pour installer et mettre à jour sdkman facilement.

```sh
# installer le gestionnaire de paquets brew
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# installer curl
$ brew install curl

# installer sdkman
$ curl -s "https://get.sdkman.io" | bash
```

Maintenant, fermez et rouvrez votre terminal pour utiliser sdkman.

```sh
# imprimer la version de sdkman pour vérifier l'installation
$ sdk version
SDKMAN 5.15.0

# installer la dernière version de java
$ sdk install java

# vérifier votre installation de java et imprimer la version de java
$ java --version

Openjdk version "17.0.3" 2022-04-19
OpenJDK Runtime Environment Temurin-17.0.3+7 (build 17.0.3+7)
OpenJDK 64-Bit Server VM Temurin-17.0.3+7 (build 17.0.3+7, mixed mode, sharing)

# Afficher le chemin vers la version actuelle de java
$ which java
/home/sesigl/.sdkman/candidates/java/current/bin/java
```

Maintenant, vous êtes prêt à utiliser Java.

## Comment installer plusieurs versions de Java

Il est très utile d'installer plusieurs versions de Java. Peut-être que certaines applications nécessitent une version plus ancienne de Java. Ou vous voulez essayer une toute nouvelle version de Java et revenir facilement en arrière. 

Ensuite, vous installez également Java 18 :

```sh
$ sdk install java 18.0.1-tem
Done installing!

Do you want java 18.0.1-tem to be set as default? (Y/n): n
```

En tapant `n`, cela signifie que vous ne souhaitez pas utiliser Java 18 comme version par défaut. Vous pouvez activer manuellement des versions temporairement dans votre shell en exécutant `sdk use java <version>`.

```sh
$ sdk use java 18.0.1-tem
Using java version 18.0.1-tem in this shell.

$ java -version
openjdk version "18.0.1" 2022-04-19
OpenJDK Runtime Environment Temurin-18.0.1+10 (build 18.0.1+10)
OpenJDK 64-Bit Server VM Temurin-18.0.1+10 (build 18.0.1+10, mixed mode, sharing)
```

Si vous fermez la fenêtre ou tapez `sdk use java 17.0.3-tem`, vous pouvez revenir en arrière.

```sh
$ sdk use java 17.0.3-tem
Using java version 17.0.3-tem in this shell.

$ java -version
openjdk version "17.0.3" 2022-04-19
OpenJDK Runtime Environment Temurin-17.0.3+7 (build 17.0.3+7)
OpenJDK 64-Bit Server VM Temurin-17.0.3+7 (build 17.0.3+7, mixed mode, sharing)
```

## Comment basculer automatiquement la version de Java

Supposons que vous avez 2 projets, l'un avec Java 17 et l'autre avec Java 18. En créant un fichier `.sdkmanrc` dans un répertoire, vous pouvez basculer automatiquement les versions, ce qui augmentera votre productivité. 

Créons un fichier pour un projet Java 17 :

```sh
$ sdk env init
.sdkmanrc created.

$ tail .sdkmanrc
# Enable auto-env through the sdkman_auto_env config
# Add key=value pairs of SDKs to use below
java=17.0.3-tem
```

Ensuite, créez un autre répertoire, basculez la version de Java vers Java 18, et créez un autre `.sdkmanrc` en exécutant `sdk env init`.

```sh
$ cd ..

$ mkdir my-java-18-project

$ cd my-java-18-project/

$ sdk use java 18.0.1-tem
Using java version 18.0.1-tem in this shell.

$ sdk env init
.sdkmanrc created.

$ tail .sdkmanrc
# Enable auto-env through the sdkman_auto_env config
# Add key=value pairs of SDKs to use below
java=18.0.1-tem
```

Pour basculer automatiquement les versions de Java, vous devez éditer le fichier `$HOME/.sdkman/etc/config` et définir `sdkman_auto_env=true`. Il y a déjà une ligne, vous devez donc seulement changer `false` en `true`.

Pour activer le changement de configuration, redémarrez votre terminal. Une fois fait, sdkman imprime lorsqu'il change la version de Java automatiquement pour vous. 

Vérifions également la version de Java.

```sh
$ cd my-java-17-project/
Using java version 17.0.3-tem in this shell.

$ java -version
openjdk version "17.0.3" 2022-04-19
OpenJDK Runtime Environment Temurin-17.0.3+7 (build 17.0.3+7)
OpenJDK 64-Bit Server VM Temurin-17.0.3+7 (build 17.0.3+7, mixed mode, sharing)

$ cd ..
Restored java version to 17.0.3-tem (default)

$ cd my-java-18-project/
Using java version 18.0.1-tem in this shell.

$ java -version
openjdk version "18.0.1" 2022-04-19
OpenJDK Runtime Environment Temurin-18.0.1+10 (build 18.0.1+10)
OpenJDK 64-Bit Server VM Temurin-18.0.1+10 (build 18.0.1+10, mixed mode, sharing)
```

Si vous voulez en savoir plus sur sdkman, consultez la [documentation d'utilisation de sdkman](https://sdkman.io/usage).

## Comment mettre à jour une version de Java

Une fois qu'une nouvelle version de Java est disponible, elle devrait être listée via `sdk list java`. Mais vous pouvez également utiliser `sdk upgrade java` pour demander à sdkman de vérifier les mises à jour. 

Installons une ancienne version de Java :

```sh
$ sdk uninstall java 17.0.3-tem

$ sdk install java 17.0.2-tem

$ sdk install java 11.0.12-tem

$ sdk upgrade java
Available defaults:
java (local: 18.0.1-tem, 11.0.12-tem, 17.0.2-tem; default: 17.0.3-tem)

Use prescribed default version(s)? (Y/n): Y

Installing: java 17.0.3-tem
Done installing!
Setting java 17.0.3-tem as default.
```

En confirmant avec `y`, il télécharge la version par défaut suggérée `17.0.3-tem` et la définit comme version par défaut sur votre système. Cela facilite les futures mises à jour en exécutant `sdk upgrade java`.

## Résumé

Dans cet article, vous avez appris comment gérer facilement les JDK Java en utilisant sdkman. C'est un outil très utile, qui prend en charge de nombreuses distributions Linux, y compris Ubuntu, Debian et MacOS. 

SDKMan vous permet d'installer et de supprimer des versions de Java, de basculer entre elles et de mettre à jour vos versions de Java avec une seule commande. Cela garde votre système propre et facilite la gestion des JDK Java.

J'espère que vous avez apprécié l'article.

Si vous l'avez aimé et que vous avez envie de m'applaudir 👏 ou simplement de prendre contact 👋, [suivez-moi sur Twitter](https://twitter.com/sesigl). Je travaille chez eBay Kleinanzeigen, l'une des plus grandes entreprises de petites annonces au monde. Au fait, [nous recrutons](https://www.ebay-kleinanzeigen.de/careers) !

### Références

* [https://en.wikipedia.org/wiki/Java_Development_Kit](https://en.wikipedia.org/wiki/Java_Development_Kit)
* [https://adoptium.net/](https://adoptium.net/)
* [https://phoenixnap.com/kb/create-a-sudo-user-on-debian](https://phoenixnap.com/kb/create-a-sudo-user-on-debian)
* [https://stackoverflow.com/questions/63336131/install-sdkman-in-an-alpine-based-docker-image](https://stackoverflow.com/questions/63336131/install-sdkman-in-an-alpine-based-docker-image)
* [https://brew.sh/](https://brew.sh/)
* [https://reflectoring.io/manage-jdks-with-sdkman/](https://reflectoring.io/manage-jdks-with-sdkman/)
* [https://blog.jdriven.com/2020/10/automatic-switching-of-java-versions-with-sdkman/](https://blog.jdriven.com/2020/10/automatic-switching-of-java-versions-with-sdkman/)