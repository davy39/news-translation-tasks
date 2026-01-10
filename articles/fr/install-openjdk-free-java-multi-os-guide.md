---
title: Comment installer OpenJDK (Java gratuit) – Guide multi-OS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-09-19T20:52:44.000Z'
originalURL: https://freecodecamp.org/news/install-openjdk-free-java-multi-os-guide
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/pexels-simon-berger-1323550.jpg
tags:
- name: Java
  slug: java
- name: open source
  slug: open-source
seo_title: Comment installer OpenJDK (Java gratuit) – Guide multi-OS
seo_desc: 'By Otavio Ehrenberger

  In a nutshell, there are two coexisting branches of Java: the proprietary, closed-source
  Oracle Java and the community-maintained open-source OpenJDK.

  OpenJDK is licensed under GPL-2.0, and it consists of a Java Virtual Machine ...'
---

Par Otavio Ehrenberger

En résumé, il existe deux branches coexistantes de Java : le Java propriétaire et fermé d'Oracle et le [OpenJDK open-source](https://github.com/openjdk/jdk) maintenu par la communauté.

OpenJDK est sous licence [GPL-2.0](https://github.com/openjdk/jdk/blob/master/LICENSE), et il se compose d'une machine virtuelle Java et d'un compilateur de bytecode Java. Comme c'est le moyen le plus simple et le moins cher, c'est celui que nous allons utiliser dans ce tutoriel.

Ici, vous apprendrez comment installer OpenJDK sur Windows, Mac et Linux de plusieurs manières différentes.

# Comment installer OpenJDK

## Mode semi-automatique très facile – pour Windows et macOS

Gardez à l'esprit que cela nécessitera un accès administrateur.

Si vous êtes pressé et que vous voulez simplement une installation plug-and-play avec un désinstalleur facile et une configuration automatique, c'est bien – je ne jugerai pas. :)

Rendez-vous sur le site [Adopt Open JDK](https://adoptopenjdk.net/), soutenu par la communauté et la [Eclipse Foundation](https://blog.adoptopenjdk.net/2021/03/transition-to-eclipse-an-update/), pour obtenir le lien de votre installeur (si vous avez un doute, optez pour OpenJDK 11 LTS sur HotSpot JVM).

De plus, Eclipse est le principal IDE Java open-source, au cas où vous ne le sauriez pas.

Vous serez redirigé vers une page avec une liste de liens d'installation. Recherchez votre OS, choisissez l'installeur packagé (`.msi` pour Windows ou `.pkg` pour macOS) et téléchargez-le. **N'oubliez pas d'installer TOUTES les fonctionnalités**, car cela ne fonctionnera pas immédiatement si vous n'autorisez pas l'installeur à définir JAVA_HOME. Ensuite, exécutez-le et voilà ! C'est terminé.

## Mode semi-automatique très facile – pour Linux

Cette méthode nécessite également un accès administrateur, bien sûr.

Tout d'abord, n'oubliez pas d'exécuter cette commande :

`sudo apt-get update`

Votre OS aura très probablement son propre paquet OpenJDK disponible dans le gestionnaire de dépôt.

Pour Ubuntu/Debian, les noms des paquets sont généralement de la forme `openjdk-<version_number>-jre-headless`. Par exemple :

`sudo apt install openjdk-8-jre-headless # installe pour java 8`  
ou  
`sudo apt install openjdk-13-jre-headless # installe pour java 13`

C'est tout, la communauté open-source sauve encore la journée.

## Mode encore assez facile, principalement manuel – pour Windows, macOS et Linux

Vous pouvez obtenir votre OpenJDK compressé auprès de divers fournisseurs tels que Microsoft, Red Hat, Intel ou quiconque proposant leur fork d'OpenJDK. Ils peuvent même offrir leur propre fichier d'installation. Mais pour garder les choses simples, nous utilisons à nouveau [Adopt Open JDK](https://adoptopenjdk.net/).

Sélectionnez votre version préférée et votre JVM (OpenJDK 11 LTS sur HotSpot JVM si vous n'êtes pas sûr) et téléchargez le JDK compressé.

Pourquoi choisir cette option plutôt que les méthodes beaucoup plus faciles décrites ci-dessus ? Peut-être que vous n'avez pas les droits d'administrateur sur votre machine actuelle ou peut-être que vous mettez en place votre propre stratégie pour gérer plusieurs versions de Java. Je ne sais pas, mais cela a ses cas d'utilisation.

### Étapes pour Windows

1. Stockez les fichiers extraits dans l'arborescence des répertoires

Tout d'abord, extrayez le fichier zip dans un dossier (`C:\Program Files\OpenJDK` serait le [choix judicieux](https://www.makeuseof.com/tag/default-windows-files-folders/). Notez que `\OpenJDK` a été ajouté manuellement). Cela créera le dossier pour l'installation du JDK, avec `\bin` comme l'un de ses sous-répertoires.

Vous aurez besoin de privilèges d'administrateur pour extraire le fichier zip à cet emplacement.

Si vous ne pouvez pas utiliser les droits d'administrateur pour une raison quelconque, extrayez-le à un emplacement sous votre espace utilisateur, tel que `C:\Users\%YOUR_USERNAME%\OpenJDK`.

2. Ouvrez les variables d'environnement

Ouvrez le Panneau de configuration > Système et sécurité > Système > Paramètres système avancés (il sera sous 'Spécifications de l'appareil' dans Windows 10+).

Dans la fenêtre Propriétés système, sélectionnez l'onglet Avancé, puis Variables d'environnement.

3. Définissez JAVA_HOME :

Sous Variables système, cliquez sur Nouveau. Entrez le nom de la variable comme JAVA_HOME. Entrez la valeur de la variable comme le chemin d'installation du JDK (en ajoutant le sous-dossier `\bin` à la fin du chemin). Le mien était `C:\Program Files\OpenJDK\OpenJDK11U-jdk_x64_windows_hotspot_11.0.15_10\jdk-11.0.15+10\bin`.

Cliquez sur OK et Appliquer les modifications. Si vous effectuez ce processus en tant que non-administrateur, choisissez `Variables utilisateur` à la place.

4. Ajoutez les exécutables binaires au PATH :

Restez dans la fenêtre Variables d'environnement. Cliquez sur la variable nommée `Path` (soit pour Système ou Utilisateur, selon votre choix dans la dernière section).

Vous verrez une liste de choses. Ce sont les exécutables auxquels vous avez accès depuis votre CLI (comme le Terminal Windows, l'Invite de commandes ou Poweshell).

Cliquez sur 'Nouveau' en haut à droite et ajoutez `%JAVA_HOME%` comme variable.

Cliquez sur OK et Appliquer les modifications.

5. Testez l'installation

Ouvrez une interface de ligne de commande. Tapez `java -version`. Si la sortie était la version, tout était OK, félicitations !

Si ce n'était pas le cas, redémarrez votre ordinateur et essayez à nouveau. Si cela ne fonctionne toujours pas, vérifiez ce tutoriel, essayez de lire votre chemin JAVA_HOME et voyez s'il pointe vers le dossier bin dans le chemin du dossier téléchargé.

### Étapes pour Linux/macOS :

1. Stockez les fichiers extraits dans l'arborescence des répertoires :

Ensuite, extrayez le fichier compressé approprié à votre OS. Au cas où vous ne pourriez pas ou ne voudriez pas utiliser les permissions d'administrateur, extrayez-le quelque part dans votre espace utilisateur (comme `~/.openjdk`).

Si vous voulez un emplacement plus conventionnel, extrayez-le dans `/usr/local/`, qui est l'endroit où les logiciels installés manuellement par l'utilisateur vont conventionnellement dans les systèmes POSIX.

Ma commande (pour Linux) était celle-ci : `sudo tar -xf OpenJDK11U-jdk_x64_linux_hotspot_11.0.16.1_1.tar.gz -C /usr/local`.

2. Définissez JAVA_HOME et ajoutez-le au PATH :

Définissez JAVA_HOME là où vous avez extrait votre installation OpenJDK. Pointez-le vers le répertoire OpenJDK, pas vers son sous-dossier `/bin`, car JAVA_HOME ne sera pas seulement utilisé pour déterminer l'emplacement des exécutables.

Cela devrait se trouver dans votre fichier d'initialisation de shell. Par exemple, supposons que ce sont les deux dernières lignes de mon fichier `~/.zshrc` :

```
   export JAVA_HOME="/usr/local/jdk-11.0.16.1+1"
   export PATH="$JAVA_HOME/bin:$PATH"

```

3. Vérifiez l'installation

Maintenant, actualisez votre shell en sourçant le fichier d'init ou en ouvrant un autre onglet/fenêtre.

Vous pouvez vérifier l'installation avec `java -version`. Si aucune erreur n'est affichée, félicitations ! Il est temps de faire un peu de Java.

## Conclusion

Et voilà ! Maintenant, vous devriez avoir OpenJDK installé et prêt à être utilisé sur votre machine. Merci d'avoir lu.