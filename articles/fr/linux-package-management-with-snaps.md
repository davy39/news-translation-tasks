---
title: Gestion des paquets Linux avec Snaps
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2020-06-22T13:00:00.000Z'
originalURL: https://freecodecamp.org/news/linux-package-management-with-snaps
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/software-snap.png
tags:
- name: Linux
  slug: linux
- name: 'snaps '
  slug: snaps
- name: software-packaging
  slug: software-packaging
seo_title: Gestion des paquets Linux avec Snaps
seo_desc: "A big part of administrating Linux machines - especially remote machines\
  \ - is managing and installing software. \nWhen something goes wrong with a local\
  \ application or when something on the file system breaks and needs fixing, you're\
  \ often going to wa..."
---

Une grande partie de l'administration des machines Linux - en particulier des machines distantes - consiste à gérer et à installer des logiciels. 

Lorsque quelque chose ne fonctionne pas avec une application locale ou lorsque quelque chose dans le système de fichiers se casse et doit être réparé, vous allez souvent vouloir pousser des mises à jour sans avoir à voyager sur de nombreuses miles pour vous asseoir devant un écran physique. 

Beaucoup de problèmes peuvent être résolus grâce à des scripts Bash, bien sûr, mais il existe encore de nombreux cas d'utilisation où il n'y a pas d'alternative à un bon vieux binaire.

Imaginez que certains de vos systèmes distants nécessitent de nouvelles applications installées afin que les membres de l'équipe utilisant ces ordinateurs puissent effectuer une fonction commerciale. Pouvoir tirer parti de l'intégration et de l'automatisation de l'un des principaux systèmes de dépôt Linux - comme Debian ou RPM - peut rendre vos tâches d'administration beaucoup plus faciles. 

Dans cet article, nous allons explorer un système de gestion de paquets autonome relativement nouveau : Snap.

Comme Linus Torvalds ne cesse de nous le rappeler, le problème avec de nombreux systèmes de gestion de logiciels Linux est qu'il y a trop de systèmes de gestion de logiciels Linux. 

Le développement d'applications et même l'adoption de Linux sont devenus, au fil des ans, plus compliqués. Tout le temps et le travail que vous investissez dans la préparation de votre logiciel pour, disons, les dépôts Debian, ne vous aidera pas si vous voulez les intégrer dans les systèmes RPM. Et aucun des deux ne vous aidera pour le gestionnaire zypper de SUSE.

Comme je le montre dans [mon cours Pluralsight : Maintenance et dépannage du système Linux](https://pluralsight.pxf.io/VMKQj), une solution prometteuse au problème des silos logiciels est de distribuer des applications avec leurs propres environnements autonomes qui fonctionneront sur n'importe quelle distribution Linux. 

Les deux grandes normes dans ce domaine jeune et en croissance sont AppImage et snap. Nous commencerons par les snaps.

## Travailler avec les Snaps

Le système snap - sous la direction de Canonical, la société qui sponsorise Ubuntu - installe chaque application individuelle sur votre système dans sa propre partition virtuelle. Toutes ces partitions de boucle font certainement un sacré désordre de la sortie de la commande df, mais elles représentent également une approche rationnelle pour distribuer une seule version de logiciel sur toutes les installations Linux.

```
$ df
Filesystem     1K-blocks      Used Available Use% Mounted on
udev             7101884         0   7101884   0% /dev
tmpfs            1432092      3936   1428156   1% /run
/dev/sda2      479152840 183520724 271222724  41% /
tmpfs            7160452    329336   6831116   5% /dev/shm
tmpfs               5120         4      5116   1% /run/lock
tmpfs            7160452         0   7160452   0% /sys/fs/cgroup
/dev/loop2           384       384         0 100% /snap/gnome-characters/539
/dev/loop4         56320     56320         0 100% /snap/core18/1705
/dev/loop5         56320     56320         0 100% /snap/core18/1754
/dev/loop3        145664    145664         0 100% /snap/slack/23
/dev/loop0          2560      2560         0 100% /snap/gnome-calculator/730
/dev/loop6         15360     15360         0 100% /snap/aws-cli/130
[...]
/dev/loop21       521216    521216         0 100% /snap/onlyoffice-desktopeditors/38
/dev/loop22       145664    145664         0 100% /snap/slack/22
/dev/loop23       185472    185472         0 100% /snap/spotify/36
/dev/loop25        96128     96128         0 100% /snap/core/8935
/dev/loop26       319104    319104         0 100% /snap/onlyoffice-desktopeditors/43
/dev/loop27         1152      1152         0 100% /snap/drawing/16
/dev/loop24        56192     56192         0 100% /snap/gtk-common-themes/1502
/dev/loop31         2560      2560         0 100% /snap/gnome-calculator/748
/dev/sda1         523248      6152    517096   2% /boot/efi
tmpfs            1432088        12   1432076   1% /run/user/121
tmpfs                100         0       100   0% /var/lib/lxd/shmounts
tmpfs                100         0       100   0% /var/lib/lxd/devlxd
tmpfs            1432088        68   1432020   1% /run/user/1000

```

Dans cette démonstration, je vais vous montrer comment empaqueter une application basée sur GitHub en tant que snap. Avec un tel paquet, vous pourriez théoriquement le soumettre au magasin officiel de snaps où, s'il est accepté, il serait librement disponible pour quiconque sur terre.

Maintenant, je pourrais prétendre que j'ai travaillé sans relâche pour trouver la meilleure façon de tout faire depuis la ligne de commande - mais ce ne serait pas complètement honnête. En fait, ce ne serait pas honnête du tout. 

En réalité, j'ai simplement utilisé le tutoriel "premier snap" sur [le site snapcraft.io](https://snapcraft.io/) qui vous permet de sélectionner une langue et vous guide ensuite à travers chaque étape du processus. À la toute fin, il vous montre comment soumettre votre snap au magasin officiel de snaps. 

Je vais vous guider à travers le processus depuis la ligne de commande, mais si vous le faites pour vous-même, il serait probablement judicieux de consulter le site web pour vous assurer que rien n'a changé.

Alors, commençons. Vous devrez d'abord vous assurer que le gestionnaire de machines virtuelles Multipass est correctement installé, car c'est ce que snap utilise pour créer les VM où les images seront construites. Naturellement, Multipass lui-même est disponible en tant que snap. 

De même, vous aurez besoin du paquet snapcraft. Après avoir installé snapcraft, vous devriez suivre avec "hash -r" pour rafraîchir la liste des endroits où votre shell cherchera les programmes connus.

```
$ sudo snap install multipass --classic
$ sudo snap install snapcraft --classic
$ hash -r

```

Comme j'ai choisi Python pour mon langage, le tutoriel m'a fourni un lien vers le site GitHub d'un projet open source Python de sauvegarde de courriels appelé OfflineIMAP. Ne vous sentez pas limité à Python, d'ailleurs. Et, évidemment, vous pouvez substituer votre propre projet à l'exemple. 

Lorsque j'ai cloné le projet localement, je vais me déplacer dans le nouveau répertoire offlineimap. Ensuite, j'utiliserai wget pour télécharger la version spécifique à Python du fichier de configuration YAML. 

Puisqu'il y a déjà un fichier avec ce nom dans le répertoire, celui-ci obtiendra un nom alternatif, donc je vais simplement écraser l'ancienne copie en changeant le nom du nouveau. Nous allons ensuite ouvrir le fichier et éditer les trois endroits où le mot "name" apparaît entre accolades. Je dois remplacer ceux-ci par le nom que je souhaite réellement utiliser.

```
$ git clone https://github.com/snapcraft-docs/offlineimap
$ cd offlineimap
$ wget https://snapcraft.io/first-snap/python/snapcraft.yaml

```

À partir de là, exécuter "snapcraft" prendra en charge le processus d'empaquetage. Cela peut être un processus long, surtout s'il y a des logiciels dont vous avez besoin - comme Multipass - qui ne sont pas encore installés et configurés. Vous pourriez voir quelques erreurs, mais il est probable que le script d'installation les corrige automatiquement à la volée. 

Lorsque tout cela sera terminé, vous pourrez installer le snap localement en utilisant la commande régulière "snap install", mais vous devrez ajouter --devmode et --dangerous car ce n'est pas un snap officiel et supporté, donc, techniquement, personne ne sait ce qui pourrait se passer lorsque vous le démarrerez. 

Vous pouvez prouver qu'il est installé en exécutant "snap list" et confirmer que tout a fonctionné en exécutant la commande test-offlineimap-mysnap avec -h pour obtenir l'écran d'aide. 

Profitez du logiciel - je sais que ce type de sauvegarde de courriels est quelque chose que j'ai eu l'intention de faire depuis des années.

```
$ snapcraft
$ sudo snap install --devmode --dangerous *.snap
$ snap list
$ test-offlineimap-mysnap -h

```

Si vous êtes intéressé à apprendre comment gérer les snaps dans votre environnement Linux, vous pourriez également apprécier mes articles "[Comment gérer les Snaps Ubuntu : les trucs que personne ne vous dit](https://www.freecodecamp.org/news/managing-ubuntu-snaps/)" et "[snapd rend l'administration de Nextcloud un jeu d'enfant](https://www.freecodecamp.org/news/snapd-nextcloud/)".

## Travailler avec d'autres gestionnaires de paquets

Nous venons d'avoir un bon aperçu des snaps. Mais peut-être est-ce le moment parfait pour admettre que j'ai omis d'autres grands acteurs dans le monde des gestionnaires de paquets alternatifs, en particulier [Flatpak](https://flatpak.org/setup/) et [AppImages](https://appimage.org/). 

Je discute des AppImages en profondeur [ici](https://opensource.com/article/20/6/appimages), mais un mot ou deux sur Flatpak ne serait pas déplacé ici.

L'objectif principal de Flatpak est de permettre aux développeurs de construire leurs applications dans un seul paquet et de les distribuer ensuite à n'importe quelle distribution Linux. En tant qu'utilisateur final, vous installeriez le système Flatpak en utilisant votre gestionnaire de logiciels habituel - comme Apt sur Ubuntu ou Yum sur CentOS. Flatpak est installé par défaut sur Fedora. À partir de là, c'est assez simple. Résout tous les bons problèmes, n'est-ce pas ?

Peut-être. Il y a eu quelques [critiques récentes](https://flatkill.org/) concernant des faiblesses de sécurité possibles (et significatives) dans la conception fondamentale de Flatpak. Je vous laisse décider par vous-même.

_Il y a beaucoup plus de bonnes pratiques d'administration sous forme de livres, de cours et d'articles disponibles sur mon site [bootstrap-it.com](https://bootstrap-it.com/)._