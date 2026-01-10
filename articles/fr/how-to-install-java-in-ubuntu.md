---
title: Comment installer Java dans Ubuntu - Tutoriel JDK Linux
subtitle: ''
author: Md. Fahim Bin Amin
co_authors: []
series: null
date: '2023-09-07T19:05:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-install-java-in-ubuntu
coverImage: https://www.freecodecamp.org/news/content/images/2023/09/How-to-Install-Java-in-Ubuntu
seo_title: Comment installer Java dans Ubuntu - Tutoriel JDK Linux
---

JDK-Linux-Tutorial.png
étiquettes:
- name: Java
  slug: java
- name: Linux
  slug: linux
- name: Ubuntu
  slug: ubuntu
seo_title: null
seo_desc: Installer des logiciels sur Linux est généralement plus facile, ou du moins c'est ce qu'il semble. Mais ce n'est généralement pas le cas car nous avons réalisé que l'installation et la configuration de certains outils spécifiques sur Linux peuvent prendre plus de temps que sur W...
---

Installer des logiciels sur Linux est généralement plus facile, ou du moins c'est ce qu'il semble. Mais ce n'est généralement pas le cas car nous avons réalisé que l'installation et la configuration de certains outils spécifiques sur Linux peuvent prendre plus de temps que sur Windows ou MacOS.

Un exemple de cela peut être vu lorsque vous souhaitez installer la dernière version de Java sur Ubuntu et en faire votre version de Java par défaut. Oui, je sais que vous vous demandez à propos d'autres distributions Linux comme Fedora ou Arch, et ainsi de suite, mais chaque distribution a certains avantages et inconvénients par rapport aux autres.

Ubuntu est l'une des distributions Linux les plus couramment utilisées, et la plupart des personnes qui souhaiteraient essayer le système d'exploitation Linux pour la première fois commencent généralement leur voyage Linux avec Ubuntu.

Cependant, si vous êtes un développeur Java qui migre d'une machine Windows vers une machine Linux basée sur Ubuntu, vous pourriez trouver fastidieux de configurer la dernière version de Java sur Ubuntu par opposition à Windows où vous devez simplement télécharger et installer la dernière version, et ajouter le répertoire à la variable de chemin.

Dans cet article, je vais couvrir tout ce que vous devez savoir et faire pour configurer votre système d'exploitation Ubuntu pour le développement Java. Je vais expliquer chacun des processus avec des captures d'écran appropriées et des exécutions de test.

J'ai également créé une vidéo complète montrant toutes les procédures. Vous pouvez trouver la vidéo à la fin de cet article. Au fait, si vous vous demandez, "Hey Fahim ! Qui t'a dit que l'installation de Java sur Windows est plus facile ?", alors vous devriez probablement consulter mon article sur [comment installer Java sur Windows](https://www.freecodecamp.org/news/how-to-install-java-on-windows/).

## Comment vérifier la version de Java sur Ubuntu

Avant de procéder plus loin, vous pourriez vouloir vérifier si vous avez déjà Java installé sur votre Ubuntu.

Vous pouvez le faire en utilisant le terminal. Si cela retourne une version, cela signifie qu'une version de Java est déjà installée sur votre machine. Mais si cela retourne quelque chose de différent, alors nous pouvons supposer que vous n'avez pas Java installé ou qu'il n'est pas configuré correctement.

Ouvrez simplement votre terminal. Vous pouvez également utiliser les touches de raccourci pour ouvrir le terminal sur Ubuntu : `Ctrl` + `Alt` + `T`

![Image](https://www.freecodecamp.org/news/content/images/2023/08/2023-08-16_01-38.png)
_Ouvrir le terminal_

Ensuite, exécutez la commande : `java --version`

![Image](https://www.freecodecamp.org/news/content/images/2023/08/2023-08-18_00-00.png)
_java --version_

Si cela dit "java not found" (comme vous le voyez dans l'image ci-dessus), alors vous pouvez être sûr que votre système n'a pas Java installé.

Mais si cela retourne une version de Java ou JDK (Java Development Kit), alors Java est déjà installé sur votre machine. En fonction de la version installée et de votre besoin pour les autres versions, vous pouvez supprimer l'ancienne et installer la nouvelle version ou vous pouvez garder les deux et faire d'une version la version par défaut.

## Comment installer Java sur Ubuntu

Il existe de nombreuses façons d'installer Java sur Ubuntu. Vous pouvez utiliser le CLI (Command Line Interface) où vous installerez via le terminal, ou vous pouvez télécharger le package et l'installer en utilisant le GUI (Graphical User Interface).

Dans cet article, je vais vous montrer comment vous pouvez télécharger le dernier Java depuis [Oracle](https://www.oracle.com/) et l'installer sur votre machine Ubuntu. Mais pour cela, vous devez choisir entre installer la version JRE (Java Runtime Environment) ou JDK (Java Development Kit) pour Java.

Si vous ne comprenez pas les différences entre elles ou laquelle vous avez besoin pour vos tâches, alors voici une comparaison pour vous :

## JDK vs JRE en Java

Voici quelques différences entre JDK et JRE en Java :

| JDK | JRE |
| ----- | ---- |
| Il est utilisé pour développer des applications Java et contient des outils de développement comme des débogueurs. | Il est utilisé uniquement pour exécuter des programmes Java. |
| Comme il s'agit d'un package complet pour le développement Java, il contient presque tout ce dont vous pourriez avoir besoin en tant que développeur Java. | Il est principalement utilisé pour les utilisateurs finaux, qui ne développent pas d'applications Java mais exécutent uniquement des applications Java en tant que logiciels ou outils dans leurs systèmes. |
| Comme il est responsable du développement Java, vous obtiendrez tous les outils de développement et de débogage dont vous avez besoin en tant que développeur Java. | Si vous voulez quelque chose de léger, uniquement pour exécuter des applications Java, alors c'est le bon choix pour vous. Mais gardez à l'esprit qu'il ne contient aucun outil comme des compilateurs, des débogueurs, ou toute autre fonctionnalité de développement ou de débogage nécessaire. Le seul but est de supporter les fichiers requis pour les exécuter sur les systèmes finaux.

Si vous êtes un développeur, alors vous devriez installer le JDK au lieu du JRE. En revanche, si vous êtes simplement un utilisateur normal qui ne programmera ou n'écrira pas de code du tout, vous pouvez installer le JRE.

Dans cet article, nous allons installer la version JDK car cela couvre tout. Si vous avez déjà un JDK, alors vous n'avez pas besoin d'installer le JRE séparément.

## Comment mettre à jour Ubuntu

Avant d'installer Java, nous devons nous assurer que nous avons installé toutes les mises à jour nécessaires pour le système d'exploitation Ubuntu.

Pour mettre à jour votre système d'exploitation Ubuntu, utilisez simplement la commande `sudo apt update`. Ensuite, fournissez votre mot de passe et appuyez sur la touche Entrée.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/2023-08-18_01-24.png)
_Mettre à jour le système_

Après la mise à jour, si vous obtenez un message indiquant que quelque chose doit être mis à niveau, vous pouvez les mettre à niveau en utilisant `sudo apt upgrade`.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/2023-08-18_01-25.png)
_23 packages peuvent être mis à niveau sur mon système en ce moment. Dans votre cas, cela peut être différent._

Assurez-vous d'appuyer sur "y" ou "Y" lors de la mise à niveau.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/2023-08-18_01-27.png)
_Mise à niveau du système_

La mise à niveau peut prendre un certain temps en fonction des tailles de fichiers qu'elle doit télécharger et de votre vitesse Internet.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/2023-08-18_01-31.png)

Assurez-vous que tout a été mis à niveau sans créer d'erreurs.

## Comment télécharger Oracle JDK

Vous pouvez télécharger le JDK officiel depuis le [site web d'Oracle](https://www.oracle.com/).

![Image](https://www.freecodecamp.org/news/content/images/2023/09/2023-09-05_22-00.png)

Une fois la page d'accueil chargée, cliquez sur **Produits** dans la barre de navigation supérieure :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-43.png)
_Options de navigation du site Oracle_

Ensuite, cliquez sur **Java** sous la section **Matériel et Logiciel**.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-45.png)

Cliquez sur **Télécharger Java**.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-46.png)

Ici, vous obtiendrez tous les derniers fichiers JDK. Pour des fins de développement, il est recommandé d'utiliser les versions LTS (Long Term Support) car elles reçoivent des mises à jour de version stable pour une période prolongée.

Je vais installer la version JDK 20 (qui est la dernière version au moment de la rédaction de cet article). Ce n'est pas la version LTS bien sûr, mais si vous suivez cet article, alors vous serez en mesure d'installer n'importe quelle version que vous voulez rapidement !

Dans votre cas, je recommanderais d'installer la dernière version LTS de JDK. Mais si vous voulez un accès continu aux dernières fonctionnalités de JDK (ces fonctionnalités peuvent ne pas être stables), alors vous pouvez télécharger le dernier JDK.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-47.png)

Pour télécharger, sélectionnez **Linux** dans la section du système d'exploitation et téléchargez le fichier pour **x64 Debian Package**. Cliquer sur le lien de téléchargement lancera le téléchargement du fichier du package Debian.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-48.png)

En fonction de votre vitesse Internet, cela peut prendre un temps plus court ou plus long. Comme je rédige cet article la nuit et que ma vitesse Internet reste lente la nuit, cela prend plus de temps pour télécharger le fichier du package dans mon système.

## Comment installer le JDK

J'ai téléchargé le fichier du package en utilisant le navigateur Mozilla Firefox et par défaut, il télécharge les fichiers dans le répertoire **Téléchargements**. 

Allez simplement dans le répertoire où vous avez téléchargé le fichier et ouvrez le terminal là-bas.

Généralement, si vous allez dans un répertoire et que vous faites un clic droit, vous verrez un menu contextuel qui dit **Ouvrir dans le Terminal**. En utilisant cela, vous pouvez ouvrir votre terminal dans ce répertoire.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/2023-09-05_23-01.png)

Alternativement, si vous ouvrez le terminal ailleurs, vous pouvez utiliser la commande `cd` pour aller dans un répertoire spécifique.

Par exemple, j'ai ouvert mon terminal ailleurs. J'utilise la commande `cd` pour aller dans mon répertoire **Téléchargements** comme on peut le voir dans l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/2023-09-05_23-03.png)

Vous pouvez utiliser la commande `ls` pour voir tous les fichiers et dossiers disponibles dans un répertoire particulier :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/2023-09-05_23-04.png)

Après avoir téléchargé le fichier, vous verrez que le nom du fichier contient également le nom de la version qui est nécessaire, mais si vous pensez que cela pourrait être fastidieux à taper plus tard, vous pouvez également raccourcir le nom du fichier.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/2023-09-05_23-06.png)

Pour cet article, nous utiliserons le nom de fichier par défaut.

Récupérez le chemin complet du répertoire où le fichier du package JDK est téléchargé. Vous pouvez utiliser le raccourci `Ctrl` + `L` pour afficher le chemin complet du répertoire.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/2023-09-05_23-07.png)

Pour moi, le chemin du répertoire actuel où se trouve mon fichier Debian JDK est `/home/fahim/Downloads/`. Assurez-vous de copier l'adresse.

Ensuite, ouvrez le terminal. Vous pouvez le faire en utilisant le raccourci `Ctrl` + `Alt` + `T`.

J'aime installer le JDK en utilisant le terminal, mais vous pouvez également l'installer en utilisant le GUI (Graphical User Interface). Mais je recommande d'utiliser le terminal car cela vous aidera également à déboguer les problèmes que vous rencontrez pendant l'installation.

Utilisez la commande `sudo apt install /home/fahim/Downloads/jdk_filename.deb` pour commencer l'installation. Pour moi, la commande complète est `sudo apt install /home/fahim/Downloads/jdk-20_linux-x64_bin.deb`.

Appuyez sur la touche Entrée :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/2023-09-05_23-11.png)

Entrez votre mot de passe et tapez "y" lorsqu'il demande votre permission pour installer le package.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/2023-09-05_23-12.png)

Assurez-vous d'avoir installé le package avec succès avant de passer à l'étape suivante.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/2023-09-05_23-13.png)

Vous pourriez obtenir `N: Download is performed unsandboxed as root as file '/home/fahim/Downloads/jdk-20_linux-x64_bin.deb' couldn't be accessed by user '_apt'. - pkgAcquire::Run (13: Permission denied)`. Mais ne vous inquiétez pas de cela car nous avons effectué l'installation "unsandboxed" intentionnellement.

Vous ne rencontrerez aucun problème si vous utilisez le package Debian téléchargé depuis la bonne source.

Vous pouvez effacer le terminal en utilisant la commande `clear`.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/2023-09-05_23-15.png)

## Comment configurer Java dans Ubuntu

Nous devons nous assurer que si une mise à jour est effectuée, elle ne télécharge pas une version rétrogradée de Java.

Vous pouvez le faire en utilisant la commande `sudo update-alternatives --install /usr/bin/java java /usr/lib/jvm/jdk-version/bin/java 1`.

Comme j'utilise la version "JDK - 20", ma commande serait `sudo update-alternatives --install /usr/bin/java java /usr/lib/jvm/jdk-20/bin/java 1`.

Assurez-vous de changer `jdk-version` pour correspondre à votre version JDK installée.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/2023-09-05_23-18.png)

Nous devons faire la même chose pour la version `javac` (Java Compiler). La commande serait `sudo update-alternatives --install /usr/bin/javac javac /usr/lib/jvm/jdk-version/bin/javac 1`.

Ma commande ressemblerait à ceci : `sudo update-alternatives --install /usr/bin/javac javac /usr/lib/jvm/jdk-20/bin/javac 1`.

N'oubliez pas de changer `jdk-version` pour correspondre à votre version JDK installée.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/2023-09-05_23-20.png)

Nous allons également faire de même pour `jar`. JAR est essentiel pour exécuter des applications basées sur Java directement dans le système.

La commande serait `sudo update-alternatives --install /usr/bin/jar jar /usr/lib/jvm/jdk-version/bin/jar 1`.

Ma commande ressemblerait à ceci : `sudo update-alternatives --install /usr/bin/jar jar /usr/lib/jvm/jdk-20/bin/jar 1`.

Ensuite, changez `jdk-version` pour correspondre à votre version JDK installée.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/2023-09-05_23-23.png)

C'est tout pour la plupart des cas. Vous êtes prêt à partir !

Mais si vous rencontrez des problèmes, alors consultez la vidéo complète fournie ci-dessous. Dans cette vidéo, j'ai parlé de nombreux problèmes possibles et de la façon de les résoudre. Si vous avez plusieurs versions de Java installées sur votre système, alors vous devez en faire une la version par défaut. Cela est également couvert dans la vidéo.

De plus, si vous souhaitez apporter plus de modifications, alors la vidéo va vous aider avec cela également. Mais pour la plupart des utilisateurs, cet article est tout ce dont vous avez besoin pour installer Java sur votre système d'exploitation Ubuntu.

## Vidéo de démonstration

Consultez la vidéo complète pour résoudre tout autre problème ou si vous souhaitez apporter plus de modifications.

%[https://youtu.be/amk1hIeDK9c]

## **Conclusion**

J'espère que vous avez apprécié cet article et que vous êtes en mesure d'installer Java sur votre système d'exploitation Ubuntu.

Si vous avez des questions, n'hésitez pas à me contacter sur [Twitter](https://twitter.com/Fahim_FBA) ou [LinkedIn](https://www.linkedin.com/in/fahimfba/).

Vous pouvez également me suivre sur :
🎁GitHub : [FahimFBA](https://github.com/FahimFBA)
🎁YouTube : [@FahimAmin](https://www.youtube.com/@FahimAmin?sub_confirmation=1)

Si vous êtes intéressé, vous pouvez également consulter mon site web : [https://fahimbinamin.com/](https://fahimbinamin.com/)