---
title: Comment installer et configurer Flutter sur Ubuntu 16.04+
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-08-12T15:43:09.000Z'
originalURL: https://freecodecamp.org/news/how-to-install-and-setup-flutter-on-ubuntu
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/Flutter-logo.png
tags:
- name: Flutter
  slug: flutter
- name: Ubuntu
  slug: ubuntu
seo_title: Comment installer et configurer Flutter sur Ubuntu 16.04+
seo_desc: "By Otavio Ehrenberger\nFlutter is a Dart-based toolkit that helps you build\
  \ the front end of your apps. It really shines in cross-platform mobile app development\
  \ and aims to be a viable option for web and desktop as well. \nIn its mobile app\
  \ flavor, Fl..."
---

Par Otavio Ehrenberger

Flutter est un outil basé sur Dart qui vous aide à construire l'interface utilisateur de vos applications. Il excelle particulièrement dans le développement d'applications mobiles multiplateformes et vise à devenir une option viable pour le web et le bureau également. 

Dans sa version pour applications mobiles, Flutter offre de nombreuses abstractions d'interface utilisateur pour construire des interfaces. Vous pouvez implémenter la logique en Dart, ou directement avec Kotlin ou Swift si vous avez besoin d'interactions plus spécifiques avec votre système d'exploitation choisi. 

Bien que le développement d'applications multiplateformes ne soit pas nouveau, les stratégies précédentes telles que PhoneGap et Ionic utilisaient l'implémentation WebView disponible au lieu d'interfacer directement avec le système. Cela n'est pas seulement très limitant, mais entraîne également des coûts de performance élevés. 

Le standard de référence pour le développement d'applications _natives_ multiplateformes reste à établir. Mais Flutter offre beaucoup par lui-même et s'efface élégamment lorsque vous devez interagir directement avec le système d'exploitation en utilisant le langage officiel nécessaire. 

Cela fait de Flutter un changement de jeu même avant qu'il n'ait réalisé son potentiel de partage de la même base de code avec les versions web et bureau d'une application.

Dans ce tutoriel, nous allons configurer une machine Ubuntu 16.04+ pour le développement d'applications Android avec Flutter. Vous pouvez également éditer du code Swift directement depuis Android Studio, mais malheureusement, vous n'aurez pas de support officiel pour tester l'application sur des appareils ou émulateurs iOS en raison des politiques d'Apple. 

Pour cela, nous devrons installer et configurer Java en tant que dépendance d'Android Studio, configurer Android Studio pour utiliser l'accélération matérielle et exécuter des applications Flutter, et bien sûr, installer et configurer Flutter lui-même. Alors, commençons.

## Comment installer et configurer Flutter

Tout d'abord, installons Flutter via le snap store. Si vous utilisez Ubuntu 16.04 ou une version ultérieure, vous avez probablement déjà la commande `snap` installée. 

Si ce n'est pas le cas, vous pouvez suivre les instructions disponibles pour votre distribution à la section "Install Snap Store on your Linux distribution" sur [cette](https://snapcraft.io/snap-store) page.

![Certaines des distributions Linux pour lesquelles le snap store est disponible.](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/5wgxz7mtwcps32vuq3fp.png)

Avec la commande `snap` disponible, installez Flutter comme ceci :

```bash
sudo snap install flutter --classic

```

Après que Flutter ait terminé son installation, exécutez une vérification de base qui effectuera également une configuration automatique :

```bash
flutter doctor -v

```

![Sortie de flutter doctor](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/12plekbnhxgfqz6u4efn.png)

Flutter a été installé, bien joué !

## Comment installer et configurer Java

Tout d'abord, nous devons obtenir le Kit de Développement Java Open (soutenu par la communauté) avant de pouvoir utiliser Android Studio. 

Pour obtenir la dernière version stable de Java 8, ouvrez votre terminal et exécutez : 

```bash
sudo apt-get update && sudo apt-get install openjdk-8-jdk

```

D'autres versions peuvent parfois présenter des problèmes imprévisibles lors de l'utilisation avec Flutter en mai 2021, je recommande donc d'installer OpenJDK 8. Ne vous inquiétez pas, OpenJDK 8 est prévu pour recevoir un support au moins jusqu'en 2024.

Après une installation réussie, il est temps de définir la variable d'environnement `$JAVA_HOME`. Elle est utilisée par défaut par de nombreuses applications qui interagissent avec votre installation locale de Java, dont Android Studio.

Obtenez une liste des JDK actuellement installés dans votre système avec cette commande :

```bash
sudo update-alternatives --config java

```

Choisissez dans la liste des versions installées localement (rappelons que Java 8 est le plus facile à utiliser avec Flutter) et définissez celle que vous souhaitez comme version par défaut du système. 

Définissez `$JAVA_HOME` sur son chemin, **sans inclure la partie `/bin` et au-delà du chemin** (dans mon cas, par exemple, le chemin correct était `/usr/lib/jvm/java-8-openjdk-amd64`) :

```bash
#JAVA_HOME=<votre_chemin_d_installation_java>, même que ci-dessous si vous avez suivi les instructions
JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64" # mon chemin local après l'installation d'openjdk-8
echo "JAVA_HOME=\"$JAVA_HOME\"" >> ~/.bashrc # définit la variable d'environnement JAVA_HOME pour l'utilisateur actuel
echo 'export PATH=$PATH:$JAVA_HOME/bin' >> .zshrc # ajoute les binaires de java à votre chemin
source ~/.bashrc && echo $JAVA_HOME # vérifie que la variable a été définie de manière permanente

```

## Comment installer et configurer Android Studio pour fonctionner avec Flutter

Vous pouvez télécharger Android Studio [ici](https://developer.android.com/studio).

Après que votre téléchargement soit terminé, extrayez le package Android Studio dans le répertoire `/usr/local/` :

```bash
sudo tar -C /usr/local -zxvf ~/Downloads/<package_android_studio>.tar.gz

```

Après l'avoir extrait avec succès, exécutez le script d'installation d'Android Studio :

```bash
bash /usr/local/android-studio/bin/studio.sh

```

Cela devrait faire apparaître l'assistant d'installation. Suivez les instructions de l'assistant pour l'installation standard et vous devriez arriver à l'écran de démarrage. 

Sélectionnez Configurations dans le coin inférieur droit et cliquez sur "Plugins" :

![Écran de démarrage d'Android Studio](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/9xaxzsat1b2kcksqkypy.png)

Installez le plugin officiel "Flutter", publié par **flutter.dev** :

![Plugin Flutter](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/o6t1w69ero8xe234idnl.png)

Vous serez invité à installer le plugin Dart (le langage de programmation de base de Flutter) avant de continuer. Cliquez sur 'Ok' et redémarrez l'IDE Android Studio. 

L'option pour démarrer un projet Flutter devrait maintenant être visible. Cliquez dessus, puis sélectionnez 'Flutter Application' et cliquez sur 'Next'.

Vous devriez être accueilli par l'écran de configuration du projet. Configurez le nom, l'emplacement et la description de votre projet comme vous le souhaitez, et pointez le champ "Flutter SDK" vers `/home/<votre_nom_d_utilisateur>/snap/flutter/common/flutter` :

![Configuration du projet Flutter](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/w4j43px47sc5o9t04jtl.png)

Au cas où le chemin ci-dessus ne serait pas disponible, ouvrez un terminal et exécutez :

```bash
flutter doctor -v

```

Vous devriez alors être accueilli par l'écran du projet de démarrage :

![Projet de démarrage Flutter](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ve413tpxbsn674bqlowx.png)

Presque terminé. Maintenant, vous devez accepter les licences Android et vérifier la propriété de votre installation Flutter afin d'éviter les erreurs de construction surprises futures dues aux ressources refusées pour Android Studio. 

Ouvrez votre terminal et exécutez :

```bash
flutter doctor --android-licenses # accepter les licences de Google, nécessaires pour construire l'application
sudo chown -R $USER:$USER /home/$USER/snap/flutter # confirmer que vous êtes le propriétaire de flutter local

```

Maintenant, Android Studio est enfin configuré pour exécuter des projets Flutter. Bien joué !

Vous devriez également activer l'entrée de bureau pour Android Studio. Dans votre écran de projet, cliquez sur "Tools" puis "Create Desktop Entry" :

![Entrée de bureau AS](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/qmw2u417r7v8x6ry2n7t.png)

Le raccourci Android Studio devrait être disponible dans le menu "Activities".

## Comment activer la virtualisation matérielle pour l'émulateur Android

Pour exécuter l'émulateur, nous devons d'abord configurer les capacités de virtualisation matérielle de votre CPU.

Exécutez `kvm-ok` dans votre terminal et la sortie devrait indiquer si vous pouvez utiliser l'accélération KVM ou non. Si vous avez un CPU AMD ou Intel, il est probable que vous puissiez le faire.

La Machine Virtuelle Kernel, en bref, est un pont entre le noyau avec des périphériques virtuels qui permet à un périphérique virtuel d'émuler son propre matériel directement à partir du matériel de l'ordinateur hôte. Vous pouvez consulter [ici](https://www.linux-kvm.org/page/FAQ#Preparing_to_use_KVM) pour plus d'informations détaillées.

À condition que vous puissiez effectivement utiliser l'accélération KVM, il est temps de configurer KVM et d'autoriser l'utilisateur actuel pour celui-ci :

```bash
sudo apt update # mettre à jour les dépôts
sudo apt install qemu-kvm libvirt-daemon-system libvirt-clients bridge-utils # packages de base
sudo addgroup kvm && sudo addgroup libvirtd # créer des groupes d'autorisation utilisateur
sudo adduser $USER kvm && sudo adduser $USER libvirtd # ajouter l'utilisateur actuel aux groupes d'autorisation
sudo virsh -c qemu:///system list # vérifie si la virtualisation est correcte
# si tout s'est bien passé, votre sortie sera quelque chose comme :
#
#  Id    Name                           State
#----------------------------------------------------

```

Et redémarrez votre session utilisateur. Sur l'ordinateur, pas seulement le terminal. Déconnectez-vous du système puis reconnectez-vous ou redémarrez le PC, je vous attends.

## Comment utiliser l'émulateur Android pour tester les applications

Maintenant, ouvrez un projet Android Studio et cliquez sur l'option 'AVD Manager' (Android Virtual Device) située dans le coin supérieur droit de la fenêtre :

![Gestionnaire AVD](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/a3hnfp08d78fu8s81qad.png)

Cliquez sur le bouton "Create Virtual Device" et une fenêtre avec une liste de périphériques devrait apparaître avec la catégorie 'Phone' présélectionnée. Je vous recommande de choisir un périphérique avec le Play Store activé au cas où vous voudriez l'utiliser plus tard dans votre périphérique émulé. Le mien était le Nexus 5.

Cliquez sur le bouton 'Next' et une liste d'images système (versions du système d'exploitation Android) devrait apparaître :

![Images système](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/lsncydy90yb8wh6yiq1p.png)

Tout d'abord, téléchargez votre image cible (en cliquant simplement sur 'Download' à côté du nom de la version), sélectionnez une image téléchargée localement, et cliquez sur 'Next'. Elle ne devrait être mise en évidence qu'après que l'image a été téléchargée avec succès.

Une fenêtre apparaîtra alors, vous offrant la possibilité de personnaliser les propriétés de votre périphérique virtuel, telles que l'orientation de l'écran au démarrage, l'utilisation de la RAM, etc. Personnalisez le périphérique à votre guise si vous le souhaitez, sinon vous pouvez cliquer en toute sécurité sur 'Finish'.

Si tout se passe bien, vous devriez maintenant voir votre périphérique listé dans la fenêtre du gestionnaire de périphériques virtuels Android :

![Liste du gestionnaire AVD](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/qsyjl24niolby6uh2np7.png)

Retournez à votre vue de projet Android Studio. Sur la même ligne où se trouve le bouton 'AVD Manager', il y a une liste déroulante de périphériques disponibles juste à gauche de 'main.dart'. Sélectionnez l'émulateur que vous venez de configurer et cliquez sur le bouton vert 'play' juste à droite de 'main.dart'. 

Au cas où l'émulateur ne serait pas encore listé, ouvrez à nouveau la fenêtre du gestionnaire AVD et cliquez sur le bouton vert 'play' sous l'étiquette 'actions' listée pour votre périphérique virtuel. Cela chargera et ouvrira l'émulateur avant d'exécuter votre code Flutter.

![Périphérique virtuel Android](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/hli5nfnywjr2i5mcf289.png)

Remarquez ce ruban 'debug' dans le coin supérieur droit ? Au cas où vous voudriez vous en débarrasser, ajoutez `debugShowCheckedModeBanner: false` en tant que champ de `MaterialApp`.

## Comment utiliser un périphérique Android physique pour tester les applications

Vous devrez avoir une installation locale du pont de débogage Android afin de permettre à votre ordinateur d'échanger des informations (telles que les builds APK) avec tout périphérique Android connecté, virtuel ou non.

L'ADB se compose d'un client (l'interface à partir de laquelle vous exécutez des commandes, qui sera le binaire ADB installé dans votre ordinateur à toutes fins utiles de ce tutoriel), d'un démon (qui exécute sur le périphérique Android les commandes initialement envoyées depuis le client) et d'un serveur (qui s'exécute localement sur le PC, qui a un emplacement d'écoute par défaut à tcp://localhost:5037, et intermédiaire la communication entre le client et le démon).

Très commodément, Android Studio est actuellement livré avec un ADB, donc si vous avez suivi les instructions ci-dessus pour installer Android Studio, vous en avez déjà un sur votre ordinateur. 

Il est possible d'installer ADB à partir des dépôts Ubuntu en même temps que celui d'Android Studio, mais cela invite à des maux de tête si votre ordinateur confond éventuellement les versions installées localement. Au lieu de cela, configurons notre utilisateur Linux pour accéder à l'ADB d'Android Studio, puis exécutons ADB :

```bash
echo 'export PATH=$PATH:$HOME"/Android/Sdk/platform-tools"' >> .bashrc # ajoute adb au chemin
export PATH=$PATH:$HOME"/Android/Sdk/platform-tools" # ajoute adb au chemin
adb start-server # lance le serveur adb
adb devices # liste les périphériques connectés

```

Après avoir exécuté `adb devices`, vous avez probablement obtenu une erreur. Cette erreur a enregistré la variable `$LOGNAME` qui contient le nom de l'utilisateur actuel. Vous l'utiliserez pour insérer votre utilisateur dans le groupe `plugdev`, au cas où vous n'y seriez pas déjà. 

Vous n'avez probablement pas non plus un ensemble de règles `udev` pour les périphériques Android. Les fichiers de règles UDEV spécifient les interactions d'Ubuntu avec les périphériques branchés, et Ubuntu refusera d'effectuer certaines interactions avec votre périphérique Android à moins qu'il ne soit préalablement autorisé dans un fichier de règles UDEV. 

Alors, corrigeons ces erreurs :

```bash
# ajouter l'utilisateur au groupe plugdev
sudo usermod -aG plugdev $LOGNAME
# télécharge un fichier de règles UDEV très complet dans le répertoire approprié
sudo wget -O /etc/udev/rules.d/51-android.rules https://raw.githubusercontent.com/NicolasBernaerts/ubuntu-scripts/master/android/51-android.rules
# donne la permission de lecture au fichier android UDEV
sudo chmod a+r /etc/udev/rules.d/51-android.rules

```

Redémarrez votre session utilisateur Linux actuelle pour appliquer ces modifications, puis ouvrez un terminal et exécutez à nouveau `adb devices`. 

Au cas où vous auriez encore une erreur liée à UDEV, l'ID du fabricant de votre périphérique n'est probablement pas listé dans `/etc/udev/rules.d/51-android.rules`. Dans ce cas, recherchez sur Internet l'ID UDEV du fabricant de votre périphérique et ajoutez-le manuellement à la liste des règles dans le même format que les autres. 

Remarquez comment le seul champ avec une valeur unique parmi les lignes est `ATTR{idVendor}`. Si vous ne recevez aucune erreur, vous remarquerez que votre périphérique est listé comme 'non autorisé'. Déverrouillons le périphérique pour le débogage USB.

## Comment activer le mode développeur et le débogage USB

Sur votre périphérique Android, ouvrez 'Paramètres', puis 'À propos du téléphone'. Appuyez sur 'Numéro de build' 5-6 fois jusqu'à ce qu'un toast indiquant que 'Vous êtes maintenant un développeur !' apparaisse.

![Vous êtes maintenant un développeur](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/skib1pnotczz49wo5s4k.png)

Retournez à 'Paramètres', ouvrez 'Système', vous devriez voir que 'Options pour les développeurs' ont été déverrouillées.

![Options pour les développeurs](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/lovbrm5eg1yg8twi3dft.png)

Appuyez sur cette nouvelle entrée et cochez 'Débogage USB' juste sous la section 'Débogage'.

![Débogage USB](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/0vp2kw9urr2dalqfvorb.png)

Branchez votre périphérique Android à votre PC via USB, puis exécutez `adb devices` sur votre terminal. La sortie devrait lister votre périphérique et indiquer également qu'il est déverrouillé pour le débogage. 

Maintenant, retournez à Android Studio, cliquez sur la liste déroulante des périphériques (celle dans laquelle vous avez sélectionné votre périphérique virtuel auparavant) et votre périphérique physique devrait maintenant être listé. Sélectionnez-le. 

Enfin, cliquez sur le bouton 'run' et vous devriez voir l'application sur votre périphérique, prête à être utilisée.

Félicitations ! Vous êtes maintenant un développeur Flutter. Bonne chance dans votre parcours de développement !

_Image de couverture de flutter.dev._