---
title: Bases du langage de programmation Java
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-07T21:47:00.000Z'
originalURL: https://freecodecamp.org/news/java-programming-language-basics
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ed2740569d1a4ca3f5d.jpg
tags:
- name: Java
  slug: java
- name: General Programming
  slug: programming
seo_title: Bases du langage de programmation Java
seo_desc: Java is a programming language developed by Sun Microsystems in 1995, which
  got later acquired by Oracle. It’s now a full platform with lots of standard APIs,
  open source APIs, tools, huge developer community and is used to build the most
  trusted ent...
---

[Java](https://www.oracle.com/java/index.html) est un langage de programmation développé par [Sun Microsystems](https://en.wikipedia.org/wiki/Sun_Microsystems) en 1995, qui a ensuite été acquis par [Oracle](http://www.oracle.com/index.html). C'est maintenant une plateforme complète avec de nombreuses API standard, des API open source, des outils, une immense communauté de développeurs et est utilisée pour construire les solutions d'entreprise les plus fiables par les grandes et petites entreprises. Le développement d'applications [Android](https://www.android.com/) est entièrement réalisé avec Java et son écosystème. Pour en savoir plus sur Java, lisez [ceci](https://java.com/en/download/faq/whatis_java.xml) et [ceci](http://tutorials.jenkov.com/java/what-is-java.html).

## **Version**

La dernière version est [Java 11](http://www.oracle.com/technetwork/java/javase/overview), qui a été publiée en 2018 avec [diverses améliorations](https://www.oracle.com/technetwork/java/javase/11-relnote-issues-5012449.html) par rapport à la version précédente, Java 10. Mais pour toutes les intentions et tous les buts, nous utiliserons Java 8 dans ce wiki pour tous les tutoriels.

Java est également divisé en plusieurs "Éditions" :

* [SE](http://www.oracle.com/technetwork/java/javase/overview/index.html) - Standard Edition - pour les applications de bureau et les applications de serveur autonomes
* [EE](http://www.oracle.com/technetwork/java/javaee/overview/index.html) - Enterprise Edition - pour le développement et l'exécution de composants Java qui s'exécutent intégrés dans un serveur Java
* [ME](http://www.oracle.com/technetwork/java/embedded/javame/overview/index.html) - Micro Edition - pour le développement et l'exécution d'applications Java sur les téléphones mobiles et les appareils embarqués

## **Installation : JDK ou JRE ?**

Téléchargez les derniers binaires Java depuis le [site officiel](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html). Ici, vous pourriez vous poser la question, lequel télécharger, JDK ou JRE ? JRE signifie Java Runtime Environment, qui est la machine virtuelle Java dépendante de la plateforme pour exécuter les codes Java, et JDK signifie Java Development Kit, qui comprend la plupart des outils de développement, notamment le compilateur `javac`, et également le JRE. Donc, pour un utilisateur moyen, le JRE serait suffisant, mais puisque nous allons développer avec Java, nous téléchargerons le JDK.

## **Instructions d'installation spécifiques à la plateforme**

### **Windows**

* Téléchargez le fichier [.msi](https://en.wikipedia.org/wiki/Windows_Installer) pertinent (x86 / i586 pour 32 bits, x64 pour 64 bits)
* Exécutez le fichier .msi. C'est un fichier exécutable auto-extractible qui installera Java sur votre système !

### **Linux**

* Téléchargez le fichier [tar.gz](http://www.cyberciti.biz/faq/linux-unix-bsd-extract-targz-file/) pertinent pour votre système et installez-le :

`bash $ tar zxvf jdk-8uversion-linux-x64.tar.gz`

* Les [plateformes Linux basées sur RPM](https://en.wikipedia.org/wiki/List_of_Linux_distributions#RPM-based) téléchargent le fichier [.rpm](https://en.wikipedia.org/wiki/RPM_Package_Manager) pertinent et installent :

`bash $ rpm -ivh jdk-8uversion-linux-x64.rpm`

* Les utilisateurs ont le choix d'installer une version open source de Java, OpenJDK ou l'Oracle JDK. Bien que OpenJDK soit en développement actif et synchronisé avec Oracle JDK, ils diffèrent uniquement en matière de [licence](http://openjdk.java.net/faq/). Cependant, quelques développeurs se plaignent de la stabilité d'Open JDK. Instructions pour **Ubuntu** :

Installation d'Open JDK :  
`bash sudo apt-get install openjdk-8-jdk`

Installation d'Oracle JDK :  
`bash sudo add-apt-repository ppa:webupd8team/java sudo apt-get update sudo apt-get install oracle-java8-installer`

### **Mac**

* Soit téléchargez l'exécutable Mac OSX .dmg depuis les téléchargements Oracle
* Ou utilisez [Homebrew](http://brew.sh/) pour [installer](http://stackoverflow.com/a/28635465/2861269) :

```bash
brew tap caskroom/cask  
brew install brew-cask  
brew cask install java
```

### **Vérifier l'installation**

Vérifiez que Java a été correctement installé sur votre système en ouvrant l'invite de commande (Windows) / Windows Powershell / Terminal (Mac OS et *Unix) et en vérifiant les versions de l'environnement d'exécution et du compilateur Java :

```text
$ java -version
java version "1.8.0_66"
Java(TM) SE Runtime Environment (build 1.8.0_66-b17)
Java HotSpot(TM) 64-Bit Server VM (build 25.66-b17, mixed mode)

$ javac -version
javac 1.8.0_66
```

**Astuce** : Si vous obtenez une erreur telle que "Commande introuvable" pour `java` ou `javac` ou les deux, ne paniquez pas, c'est simplement que le PATH de votre système n'est pas correctement configuré. Pour Windows, voir [cette réponse StackOverflow](http://stackoverflow.com/questions/15796855/java-is-not-recognized-as-an-internal-or-external-command) ou [cet article](http://javaandme.com/) sur la façon de le faire. Il existe également des guides pour [Ubuntu](http://stackoverflow.com/questions/9612941/how-to-set-java-environment-path-in-ubuntu) et [Mac](http://www.mkyong.com/java/how-to-set-java_home-environment-variable-on-mac-os-x/). Si vous ne parvenez toujours pas à comprendre, ne vous inquiétez pas, demandez-nous simplement dans notre [salon Gitter](https://gitter.im/FreeCodeCamp/java) !

## **JVM**

Maintenant que nous avons terminé les installations, commençons par comprendre les détails du fonctionnement de l'écosystème Java. Java est un langage [interprété et compilé](http://stackoverflow.com/questions/1326071/is-java-a-compiled-or-an-interpreted-programming-language), c'est-à-dire que le code que nous écrivons est compilé en bytecode et interprété pour s'exécuter. Nous écrivons le code dans des fichiers .java, Java les compile en [bytecodes](https://en.wikipedia.org/wiki/Java_bytecode) qui s'exécutent sur une machine virtuelle Java ou JVM pour l'exécution. Ces bytecodes ont généralement une extension .class.

Java est un langage assez sécurisé car il ne permet pas à votre programme de s'exécuter directement sur la machine. Au lieu de cela, votre programme s'exécute sur une machine virtuelle appelée JVM. Cette machine virtuelle expose plusieurs API pour les interactions de bas niveau avec la machine que vous pouvez effectuer, mais en dehors de cela, vous ne pouvez pas manipuler explicitement les instructions machine. Cela ajoute un énorme bonus de sécurité.

De plus, une fois votre bytecode compilé, il peut s'exécuter sur n'importe quelle machine virtuelle Java. Cette machine virtuelle est dépendante de la machine, c'est-à-dire qu'elle a différentes implémentations pour Windows, Linux et Mac. Mais votre programme est garanti de s'exécuter sur n'importe quel système grâce à cette VM. Cette philosophie est appelée ["Write Once, Run Anywhere"](https://en.wikipedia.org/wiki/Write_once,_run_anywhere).

## **Hello World !**

Écrivons une application Hello World de démonstration. Ouvrez n'importe quel éditeur / IDE de votre choix et créez un fichier `HelloWorld.java`.

```text
public class HelloWorld {

    public static void main(String[] args) {
        // Affiche "Hello, World" dans la fenêtre du terminal.
        System.out.println("Hello, World");
    }

}
```

**N.B.** Gardez à l'esprit que dans Java, le nom du fichier doit être le **nom exact de la classe publique** afin de compiler !

Ouvrez maintenant le terminal / l'invite de commande. Changez votre répertoire actuel dans le terminal / l'invite de commande pour le répertoire où se trouve votre fichier. Et compilez le fichier :

```text
$ javac HelloWorld.java
```

Maintenant, exécutez le fichier en utilisant la commande `java` !

```text
$ java HelloWorld
Hello, World
```

Félicitations ! Votre premier programme Java a été exécuté avec succès. Ici, nous imprimons simplement une chaîne en la passant à l'API `System.out.println`. Nous couvrirons tous les concepts du code, mais vous êtes les bienvenus pour [examiner de plus près](https://docs.oracle.com/javase/tutorial/getStarted/application/) ! Si vous avez des doutes ou avez besoin d'aide supplémentaire, n'hésitez pas à nous contacter à tout moment dans notre [salon de discussion Gitter](https://gitter.im/FreeCodeCamp/java) !

## **Documentation**

Java est largement [documenté](https://docs.oracle.com/javase/8/docs/), car il prend en charge une grande quantité d'API. Si vous utilisez un IDE majeur tel qu'Eclipse ou IntelliJ IDEA, vous trouverez la documentation Java incluse.

De plus, voici une liste d'IDE gratuits pour le codage Java :

* [NetBeans](https://netbeans.org/)
* [Eclipse](https://eclipse.org/)
* [IntelliJ IDEA](https://www.jetbrains.com/idea/features/)
* [Android Studio](https://developer.android.com/studio/index.html)
* [BlueJ](https://www.bluej.org/)
* [jEdit](http://www.jedit.org/)
* [Oracle JDeveloper](http://www.oracle.com/technetwork/developer-tools/jdev/overview/index-094652.html)