---
title: Le manuel d'Arch Linux – Apprendre Arch Linux pour les débutants
subtitle: ''
author: Farhan Hasin Chowdhury
co_authors: []
series: null
date: '2022-01-18T15:15:23.000Z'
originalURL: https://freecodecamp.org/news/how-to-install-arch-linux
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/Farhan-Arch-Linux-Mockup.png
tags:
- name: ArchLinux
  slug: archlinux
- name: Linux
  slug: linux
seo_title: Le manuel d'Arch Linux – Apprendre Arch Linux pour les débutants
seo_desc: 'If you ask a group of developers what Linux is, most of them will probably
  say it''s an open-source operating system. Those with more technical knowledge will
  probably call it a kernel.

  For me, though, Linux is not just an operating system or a kernel...'
---

Si vous demandez à un groupe de développeurs ce qu'est Linux, la plupart d'entre eux diront probablement que c'est un système d'exploitation open-source. Ceux qui ont des connaissances techniques plus poussées l'appelleront probablement un noyau.

Pour moi, cependant, Linux n'est pas seulement un système d'exploitation ou un noyau. Pour moi, c'est la liberté. La liberté de mettre en place un système d'exploitation selon mes besoins, et c'est là qu'intervient Arch Linux.

Selon leur [wiki](https://wiki.archlinux.org/title/Arch_Linux),

> Arch Linux est une distribution GNU/Linux généraliste x86-64 développée indépendamment, qui s'efforce de fournir les dernières versions stables de la plupart des logiciels en suivant un modèle de publication continue.   
>   
> L'installation par défaut est un système de base minimal, configuré par l'utilisateur pour n'ajouter que ce qui est expressément requis.

En d'autres termes, Arch Linux est une distribution optimisée pour l'architecture x86-64, destinée aux utilisateurs expérimentés de Linux. Elle vous permet d'avoir une responsabilité et un contrôle total sur votre système. 

Vous pourrez choisir les paquets que vous souhaitez, le noyau (oui, il y en a plusieurs), le chargeur de démarrage, l'environnement de bureau, et ainsi de suite.

Avez-vous déjà entendu quelqu'un dire,

> Oh – au fait, j'utilise Arch Linux !

C'est parce que l'installation d'Arch Linux sur une machine nécessite une connaissance approfondie du fonctionnement des différentes parties d'une distribution Linux. Ainsi, utiliser Arch Linux sur votre système est une sorte de témoignage de votre compréhension de Linux.

Par expérience, installer Arch Linux n'est pas très différent de l'installation de quelque chose comme Fedora ou Ubuntu. C'est juste que vous devez passer par les étapes individuelles manuellement au lieu d'avoir un installateur qui fait les choses pour vous. Mais une fois que vous avez terminé le processus, vous commencerez à comprendre comment les autres distributions fonctionnent en général.

Dans cet article, je vais vous guider à travers le processus complet d'installation et de configuration d'Arch Linux sur votre machine. Je discuterai également de quelques tâches courantes et de conseils de dépannage à la fin.

Alors, venez avec moi et je vous montrerai à quel point le terrier du lapin est profond.

## Table des matières

- [Quelques hypothèses que je fais](#heading-quelques-hypotheses-que-je-fais)
- [Comment créer une clé USB bootable Arch Linux](#heading-comment-creer-une-cle-usb-bootable-arch-linux)
- [Comment préparer votre ordinateur pour installer Arch Linux](#heading-comment-preparer-votre-ordinateur-pour-installer-arch-linux)
- [Comment installer Arch Linux](#heading-comment-installer-arch-linux)
    - [Comment définir la disposition du clavier et la police de la console](#heading-comment-definir-la-disposition-du-clavier-et-la-police-de-la-console)
    - [Comment vérifier le mode de démarrage](#heading-comment-verifier-le-mode-de-demarrage)
    - [Comment se connecter à Internet](#heading-comment-se-connecter-a-internet)
    - [Comment mettre à jour l'horloge du système](#heading-comment-mettre-a-jour-lhorloge-du-systeme)
    - [Comment partitionner les disques](#heading-comment-partitionner-les-disques)
    - [Comment formater les partitions](#heading-comment-formater-les-partitions)
    - [Comment monter les systèmes de fichiers](#heading-comment-monter-les-systemes-de-fichiers)
    - [Comment configurer les miroirs](#heading-comment-configurer-les-miroirs)
    - [Comment installer le système de base Arch Linux](#heading-comment-installer-le-systeme-de-base-arch-linux)
- [Comment configurer Arch Linux](#heading-comment-configurer-arch-linux)
    - [Comment générer le fichier Fstab](#heading-comment-generer-le-fichier-fstab)
    - [Comment se connecter au système nouvellement installé en utilisant Arch-Chroot](#heading-comment-se-connecter-au-systeme-nouvellement-installe-en-utilisant-arch-chroot)
    - [Comment configurer le fuseau horaire](#heading-comment-configurer-le-fuseau-horaire)
    - [Comment configurer la localisation](#heading-comment-configurer-la-localisation)
    - [Comment configurer le réseau](#heading-comment-configurer-le-reseau)
    - [Comment définir le mot de passe root](#heading-comment-definir-le-mot-de-passe-root)
    - [Comment créer un utilisateur non-root](#heading-comment-creer-un-utilisateur-non-root)
    - [Comment installer le microcode](#heading-comment-installer-le-microcode)
    - [Comment installer et configurer un chargeur de démarrage](#heading-comment-installer-et-configurer-un-chargeur-de-demarrage)
- [Comment installer Xorg](#heading-comment-installer-xorg)
- [Comment installer les pilotes graphiques](#heading-comment-installer-les-pilotes-graphiques)
- [Comment installer un environnement de bureau](#heading-comment-installer-un-environnement-de-bureau)
    - [Comment installer GNOME](#heading-comment-installer-gnome)
    - [Comment installer Plasma](#heading-comment-installer-plasma)
- [Comment finaliser l'installation](#heading-comment-finaliser-linstallation)
- [Comment basculer entre les environnements de bureau](#heading-comment-basculer-entre-les-environnements-de-bureau)
- [Comment gérer les paquets avec Pacman](#heading-comment-gerer-les-paquets-avec-pacman)
    - [Comment installer des paquets avec Pacman](#heading-comment-installer-des-paquets-avec-pacman)
    - [Comment supprimer des paquets avec Pacman](#heading-comment-supprimer-des-paquets-avec-pacman)
    - [Comment mettre à jour des paquets avec Pacman](#heading-comment-mettre-a-jour-des-paquets-avec-pacman)
    - [Comment rechercher des paquets avec Pacman](#heading-comment-rechercher-des-paquets-avec-pacman)
- [Comment utiliser AUR dans Arch Linux](#heading-comment-utiliser-aur-dans-arch-linux)
    - [Comment installer des paquets avec un assistant](#heading-comment-installer-des-paquets-avec-un-assistant)
    - [Comment installer des paquets manuellement](#heading-comment-installer-des-paquets-manuellement)
- [Comment résoudre les problèmes courants](#heading-comment-resoudre-les-problemes-courants)
- [Comment utiliser l'ISO live Arch comme média de secours](#heading-comment-utiliser-liso-live-arch-comme-media-de-secours)
- [Lectures complémentaires](#heading-lectures-complementaires)
- [Conclusion](#heading-conclusion)

## Quelques hypothèses que je fais

Avant de plonger dans le cœur du tutoriel, je veux clarifier quelques points. Pour rendre cet article accessible, je fais les hypothèses suivantes à votre sujet et à propos de votre système :

- Vous connaissez Arch Linux à un niveau basique
    - [Arch Linux](https://wiki.archlinux.org/title/Arch_Linux)
    - [Foire aux questions](https://wiki.archlinux.org/title/Frequently_asked_questions)
    - [Arch comparé à d'autres distributions](https://wiki.archlinux.org/title/Arch_compared_to_other_distributions)
- Votre ordinateur utilise UEFI et non BIOS
- Vous avez une clé USB suffisamment grande (4 Go) pour démarrer Linux
- Vous avez une expérience préalable de l'installation de Linux (Ubuntu/Fedora)
- Vous avez suffisamment d'espace pour installer Linux sur votre HDD ou SSD

C'est à peu près tout. Si vous avez tout ce qui précède, vous êtes prêt à commencer.

## Comment créer une clé USB bootable Arch Linux

Pour télécharger Arch Linux, rendez-vous sur [https://archlinux.org/download/](https://archlinux.org/download/) et téléchargez la dernière version (2022.01.01 au moment de l'écriture). L'ISO devrait faire environ 870 mégaoctets.

Une fois téléchargé, vous devrez le mettre sur votre clé USB. Vous pouvez utiliser le programme [Fedora Media Writer](https://getfedora.org/en/workstation/download/) pour cela. Téléchargez et installez l'application sur votre système. Connectez maintenant votre clé USB et ouvrez l'application :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/image-48.png)

Cliquez sur "Custom image" et utilisez le navigateur de fichiers pour sélectionner le fichier ISO Arch Linux téléchargé.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/image-49.png)

L'application vous permettra maintenant de choisir l'une de vos clés USB connectées. Soyez très prudent dans le choix de la bonne si vous avez plusieurs clés USB connectées à votre machine. Cliquez maintenant sur le bouton "Write to Disk" et attendez que le processus soit terminé.

## Comment préparer votre ordinateur pour installer Arch Linux

Dans cette étape, vous devrez apporter quelques modifications à votre système, sinon Arch Linux pourrait ne pas démarrer ou fonctionner correctement.

La première modification que vous devrez apporter est de désactiver le démarrage sécurisé dans votre configuration UEFI. Cette fonctionnalité aide à prévenir les attaques de logiciels malveillants pendant le démarrage, mais elle empêche également le programme d'installation d'Arch Linux de démarrer. 

Les instructions détaillées sur la manière de désactiver cela varient en fonction de votre carte mère ou de la marque de votre ordinateur portable. Vous devrez rechercher sur Internet vous-même pour trouver la bonne méthode cette fois-ci.

La deuxième chose que vous devriez désactiver n'est pertinente que si vous installez Arch Linux à côté de Windows. Il existe une fonctionnalité Windows appelée démarrage rapide qui réduit le temps de démarrage de votre ordinateur en le mettant partiellement en veille.

C'est généralement une fonctionnalité agréable à avoir, mais elle empêche tout autre système d'exploitation dans une configuration de double démarrage d'accéder au disque dur dans le processus.

Pour désactiver cette fonctionnalité, ouvrez le menu démarrer et recherchez "Choisir un plan d'alimentation" comme suit :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/choose-a-power-plan.png)

Ensuite, dans la fenêtre suivante, cliquez sur "Choisir l'action des boutons d'alimentation" dans la barre latérale gauche :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/image-54.png)

Ensuite, dans la fenêtre suivante, vous verrez une liste de "Paramètres d'arrêt" et l'option "Activer le démarrage rapide (recommandé)" devrait être affichée en lecture seule.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/image-55.png)

Cliquez sur "Modifier les paramètres actuellement non disponibles" en haut et vous devriez alors pouvoir modifier les paramètres.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/image-56.png)

Décochez l'option "Activer le démarrage rapide (recommandé)" et appuyez sur le bouton "Enregistrer les modifications" en bas. À partir de maintenant, le processus de démarrage peut prendre quelques instants de plus, mais cela en vaut la peine.

Dans cet article, j'installerai Arch Linux comme mon système d'exploitation par défaut. Je lui allouerai donc tout l'espace disque. 

Si vous essayez de l'installer à côté de Windows, cependant, j'ai un article dédié sur le sujet. Et dans cet article, il y a une section qui traite du processus de partitionnement en détail.

## Comment installer Arch Linux

En supposant que vous avez une clé USB bootable et que votre ordinateur est correctement configuré, vous devrez démarrer à partir de la clé USB. Le processus de démarrage à partir d'une clé USB diffère d'une machine à l'autre.

Sur ma machine, appuyer sur la touche F12 pendant le démarrage m'amène à la liste des périphériques bootables. À partir de là, je peux choisir ma clé USB bootable. Vous connaissez peut-être déjà la technique appropriée pour votre ordinateur ou vous devrez faire quelques recherches.

Une fois que vous avez réussi à accéder à la liste des périphériques bootables connectés, sélectionnez votre clé USB pour démarrer et le menu suivant devrait s'afficher :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/VirtualBox_archlinux-2022.01.01-x86_64_12_01_2022_18_39_29.png)

Choisissez le premier de la liste et attendez que l'installateur d'Arch termine le démarrage. Une fois complètement démarré, vous verrez quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/VirtualBox_archlinux-2022.01.01-x86_64_12_01_2022_18_50_39.png)

C'est tout. C'est tout ce que vous obtiendrez. Contrairement à d'autres systèmes d'exploitation que vous connaissez peut-être, l'installateur d'Arch n'a pas d'interface utilisateur graphique pour automatiser l'installation.

Il nécessite plutôt que vous investissiez votre temps et vos efforts et que vous configuriez chaque partie de la distribution pièce par pièce. Cela peut sembler intimidant, mais, pour être honnête, si vous comprenez ce que vous faites, installer Arch Linux est assez amusant.

### Comment définir la disposition du clavier et la police de la console

Comme je l'ai déjà dit, l'installateur d'Arch n'a pas d'interface utilisateur graphique, donc il y aura beaucoup de frappe. Configurer la disposition de votre clavier et une police agréable peut rendre le processus d'installation beaucoup moins frustrant.

Par défaut, la console suppose que vous avez une disposition de clavier US standard. Cela devrait convenir à la plupart des gens, mais au cas où vous auriez une disposition différente, vous pouvez la changer.

Toutes les dispositions de clavier disponibles sont généralement conservées dans le répertoire `/usr/share/kbd/keymaps` sous forme de fichiers `map.gz`. Vous pouvez voir la liste de ces fichiers en utilisant la commande `ls` :

```bash
ls /usr/share/kbd/keymaps/**/*.map.gz

```

Cela listera toutes les dispositions de clavier disponibles :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/VirtualBox_archlinux-2022.01.01-x86_64_13_01_2022_15_58_28-1.png)

Par exemple, si vous avez la disposition de clavier Mac-US, localisez le fichier `map.gz` correspondant dans cette liste, qui est le fichier `mac-us.map.gz`.

Vous pouvez utiliser la commande `loadkeys` pour charger la disposition de clavier souhaitée. Pour définir `mac-us.map.gz` comme disposition par défaut, exécutez la commande suivante :

```bash
loadkeys mac-us
```

Vous pouvez également changer la police de la console si vous n'aimez pas celle par défaut. Tout comme les dispositions de clavier, les polices de la console sont conservées dans `/usr/share/kbd/consolefonts`, que vous pouvez lister en utilisant la commande `ls` :

```bash
ls /usr/share/kbd/consolefonts
```

Cela listera toutes les polices disponibles :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/VirtualBox_archlinux-2022.01.01-x86_64_13_01_2022_16_08_01.png)

Vous pouvez maintenant utiliser la commande `setfont` pour définir l'une de ces polices. Par exemple, si vous souhaitez définir `drdos8x16` comme police par défaut, exécutez la commande suivante :

```bash
setfont drdos8x16
```

Les commandes `loadkeys` et `setfont` font partie du paquet `kbd` contenant des outils essentiels pour le clavier Linux. Elles ont une excellente [documentation](https://kbd-project.org/#documentation), alors si vous souhaitez en savoir plus, n'hésitez pas à la consulter.

### Comment vérifier le mode de démarrage

Maintenant que vous avez configuré votre console, l'étape suivante consiste à vous assurer que vous avez démarré en mode UEFI et non en mode BIOS.

Pour être honnête, cette étape me semble inutile, car il est littéralement écrit `x86_64 UEFI` dans le menu de démarrage live. Mais faisons-le pour le bien du guide d'installation officiel d'Arch.

Pour vérifier le mode de démarrage, exécutez la commande suivante :

```bash
ls /sys/firmware/efi/efivars
```

Si vous êtes en mode UEFI, il listera un tas de fichiers sur votre écran :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/VirtualBox_archlinux-2022.01.01-x86_64_13_01_2022_17_18_34.png)

En cas de démarrage BIOS, le répertoire `efi` n'existera même pas dans le répertoire `/sys/firmware`. Si vous êtes en mode UEFI (ce qui devrait être le cas si vous avez tout suivi correctement), passez à l'étape suivante.

### Comment se connecter à Internet

Contrairement à de nombreuses autres distributions live, l'environnement live d'Arch ne contient pas tous les paquets nécessaires intégrés. Il contient un certain nombre de paquets minimum que vous pouvez utiliser pour installer le reste du système. Ainsi, une connexion Internet fonctionnelle est indispensable.

Si vous utilisez un réseau filaire, vous devriez avoir une connexion Internet fonctionnelle dès le départ. Pour la tester, pingez l'une des adresses publiques disponibles :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/VirtualBox_archlinux-2022.01.01-x86_64_13_01_2022_17_40_04.png)

Je prends ces captures d'écran en utilisant VirtualBox, donc la connexion Internet fonctionne parfaitement avec la connexion filaire. Mais si vous avez une connexion sans fil, les choses peuvent devenir un peu plus compliquées.

L'environnement live est fourni avec le paquet `iwd` ou [iNet wireless daemon](https://wiki.archlinux.org/title/Iwd). Vous pouvez utiliser ce paquet pour vous connecter à un réseau sans fil à proximité.

Pour commencer, exécutez la commande suivante :

```bash
iwctl
```

Cela démarrera un prompt interactif comme suit :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/VirtualBox_archlinux-2022.01.01-x86_64_13_01_2022_17_59_34.png)

Maintenant, exécutez la commande suivante pour voir la liste des périphériques sans fil disponibles :

```bash
device list
```

Cela affichera une liste des périphériques sans fil disponibles. Par périphériques sans fil, j'entends tout adaptateur sans fil connecté à votre ordinateur. Supposons que `wlan0` est le nom du périphérique.

Pour rechercher les réseaux sans fil à proximité en utilisant le périphérique trouvé, exécutez la commande suivante :

```bash
# station <device> scan

station wlan0 scan
```

Vous pourriez penser que cette commande imprimera une liste de tous les réseaux à proximité, mais ce n'est pas le cas. Pour voir la liste des réseaux, exécutez la commande suivante :

```bash
# station <device> get-networks

station wlan0 get-networks
```

Maintenant, en supposant que le nom de votre réseau domestique est `Skynet`, vous pouvez vous y connecter en exécutant la commande suivante :

```bash
# station <device> connect <SSID>

station wlan0 connect Skynet
```

Le programme `iwctl` vous demandera le mot de passe wi-fi. Entrez-le soigneusement et, une fois connecté au réseau, quittez le programme en écrivant `exit` et en appuyant sur Entrée. Essayez de pinguer une adresse publique une fois de plus et assurez-vous que l'Internet fonctionne correctement.

### Comment mettre à jour l'horloge du système

Dans Linux, NTP ou Network Time Protocol est utilisé pour synchroniser les horloges des systèmes informatiques sur un réseau. Vous pouvez utiliser la commande `timedatectl` pour activer NTP sur votre environnement live Arch :

```bash
timedatectl set-ntp true
```

Cette commande commencera à produire une sortie et après quelques secondes. Si vous ne voyez pas le curseur de la commande réapparaître, essayez d'appuyer sur Entrée. J'ai rencontré cet inconvénient quelques fois dans le passé.

### Comment partitionner les disques

C'est probablement l'étape la plus sensible de tout le processus d'installation – car si vous vous trompez dans vos partitions, vous perdez vos précieuses données. Mon conseil serait de ne pas suivre immédiatement cette section. Au lieu de cela, lisez toute la section d'abord, puis suivez-la.

Pour commencer le processus de partitionnement, vous devrez d'abord connaître les différents disques connectés à votre ordinateur. Vous pouvez utiliser `fdisk`, qui est un programme piloté par dialogue pour la création et la manipulation de tables de partition.

```bash
fdisk -l
```

Cette commande listera les tables de partition pour tous les périphériques disponibles sur votre ordinateur.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/VirtualBox_archlinux-2022.01.01-x86_64_13_01_2022_19_53_34.png)

Comme vous pouvez le voir, il y a deux périphériques connectés à mon ordinateur (en fait, une machine virtuelle). Selon le nombre de périphériques que vous avez, cette liste peut être plus longue, alors ignorez tout périphérique se terminant par `rom`, `loop` ou `airoot` lors de l'examen de la liste. Vous ne pouvez pas utiliser ces périphériques pour l'installation.

Cela nous laisse avec le périphérique `/dev/sda`. Gardez à l'esprit que cela peut être complètement différent sur votre machine. Par exemple, si vous avez un disque NVME, vous pourriez voir `/dev/nvme0n1` à la place.

Une fois que vous avez décidé quel périphérique utiliser, il est bon de vérifier s'il y a des partitions existantes dans ce périphérique. Pour ce faire, vous pouvez utiliser la variation suivante de la même commande `fdisk` :

```bash
fdisk /dev/sda -l
```

N'oubliez pas de remplacer `/dev/sda` par ce que vous avez. Cette commande listera toutes les partitions à l'intérieur du périphérique donné.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/VirtualBox_archlinux-2022.01.01-x86_64_13_01_2022_20_13_14.png)

Bien qu'il n'y ait pas de partitions dans ce périphérique, dans une situation réelle, vous pourriez avoir des partitions créées précédemment. Ces partitions apparaîtront comme `/dev/sda1`, `/dev/sda2` ou, dans le cas d'un disque NVME, `/dev/nvme0n1p1`, `/dev/nvme0n1p2`, etc.

Le programme `fdisk` peut faire beaucoup plus que simplement lister les partitions. Consultez la [page ArchWiki correspondante](https://wiki.archlinux.org/title/Fdisk) pour connaître les tâches que vous pouvez effectuer avec ce programme.

Il existe un autre programme `cfdisk` qui est un manipulateur de table de partition de disque basé sur [curses- (bibliothèque de programmation)](https://en.wikipedia.org/wiki/Curses_(programming_library)) pour Linux. Il est similaire en fonctionnalité à `fdisk`, mais étant basé sur curses signifie qu'il a une interface qui le rend plus facile à utiliser. 

Exécutez la commande suivante pour démarrer `cfdisk` sur votre périphérique préféré :

```bash
cfdisk /dev/sda
```

N'oubliez pas de remplacer `/dev/sda` par ce que vous avez. Si le périphérique a une table de partition créée précédemment, alors `cfdisk` affichera directement la liste des partitions. Sinon, vous devrez choisir un type de table de partition pour commencer :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/VirtualBox_archlinux-2022.01.01-x86_64_13_01_2022_20_22_55.png)

Choisissez `gpt` pour votre système basé sur UEFI. Ensuite, vous arriverez sur la liste des partitions et de l'espace libre sur le périphérique :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/VirtualBox_archlinux-2022.01.01-x86_64_13_01_2022_20_24_09.png)

Vous pouvez vous déplacer verticalement le long de la liste des périphériques en utilisant les touches fléchées haut/bas et vous déplacer horizontalement le long des différentes actions en utilisant les touches fléchées gauche/droite.

Pour installer Arch, ou toute autre distribution Linux, vous aurez besoin de trois partitions séparées. Elles sont les suivantes :

* Partition système EFI – pour stocker les fichiers requis par le firmware UEFI.
* ROOT – pour installer la distribution elle-même.
* SWAP – pour servir d'espace de débordement pour votre RAM.

Assurez-vous que la bonne partition/espace libre est surlignée dans la liste et sélectionnez l'action `[ New ]`.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/VirtualBox_archlinux-2022.01.01-x86_64_13_01_2022_20_37_04.png)

Mettez la taille de partition souhaitée. Vous pouvez utiliser M pour désigner les mégaoctets, G pour les gigaoctets et T pour les téraoctets.

Pour une partition système EFI, vous devez allouer au moins 500 Mo. Une fois que vous avez mis votre taille souhaitée, appuyez sur Entrée pour finaliser. La liste mise à jour des partitions peut ressembler à ce qui suit :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/VirtualBox_archlinux-2022.01.01-x86_64_13_01_2022_20_37_29.png)

La partition système EFI est un type spécial de partition. Elle doit être d'un type et d'un format spécifiques. Pour changer le type par défaut, gardez la partition nouvellement créée surlignée et sélectionnez `[ Type ]` dans la liste des actions.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/VirtualBox_archlinux-2022.01.01-x86_64_13_01_2022_20_39_24.png)

Dans cette longue liste de types, surlignez `EFI System` et appuyez sur Entrée. Le type de la partition dans la liste devrait être mis à jour en conséquence :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/VirtualBox_archlinux-2022.01.01-x86_64_13_01_2022_20_40_37.png)

Ensuite, c'est la partition racine. Surlignez l'espace libre restant et sélectionnez `[ New ]` une fois de plus. Cette fois, attribuez 10 Go à cette partition. La taille idéale de la partition racine dépend de vos nécessités. Personnellement, j'alloue au moins 100 Go à la partition racine de toutes mes installations Linux.

Vous n'avez pas besoin de changer le type de cette partition. Le `Linux filesystem` par défaut fera l'affaire.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/VirtualBox_archlinux-2022.01.01-x86_64_13_01_2022_20_43_14.png)

Créez une dernière partition avec l'espace restant et changez son type en `Linux swap` dans le menu :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/VirtualBox_archlinux-2022.01.01-x86_64_13_01_2022_20_45_57.png)

La taille idéale d'une partition swap est un sujet de débat. Personnellement, je n'ai pas de partitions swap sur mes machines. La quantité de RAM physique que j'ai est plus que suffisante. Mais si je ressens un jour le besoin d'en avoir une plus tard, j'utilise un `swapfile` à la place. Quoi qu'il en soit, l'état final de votre périphérique devrait être le suivant :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/VirtualBox_archlinux-2022.01.01-x86_64_13_01_2022_20_48_49.png)

Si vous êtes satisfait de la configuration, surlignez `[ Write ]` dans la liste des actions et appuyez sur Entrée. Le programme vous demandera si vous souhaitez conserver ces modifications ou non. Vous devrez écrire `yes` et appuyer sur Entrée si vous êtes d'accord. Une fois que la table de partition a été modifiée, sélectionnez `[ Quit ]` pour quitter le programme.

Une chose que je voudrais mentionner pour ceux qui essaient d'installer Arch Linux à côté de Windows est que, dans ce cas, la partition système EFI devrait déjà exister dans votre périphérique. Donc ne touchez pas à cela. Créez simplement les autres partitions et continuez.

### Comment formater les partitions

Maintenant que vous avez créé les partitions nécessaires, vous devrez les formater en conséquence. Vous pouvez utiliser les programmes `mkfs` et `mkswap` pour cela. Avant le formatage, jetez un dernier coup d'œil à votre liste de partitions en exécutant la commande suivante :

```bash
fdisk /dev/sda -l
```

Cette fois, vous verrez les trois partitions nouvellement créées avec leurs détails :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/VirtualBox_archlinux-2022.01.01-x86_64_13_01_2022_21_02_23.png)

Prenez note des noms des périphériques, comme `/dev/sda1`, `/dev/sda2`, `/dev/sda3`, etc. La partition système EFI doit être au format FAT32. Exécutez la commande suivante pour formater une partition au format FAT32 :

```bash
mkfs.fat -F32 /dev/sda1
```

La suivante est la partition racine. Elle peut être dans plusieurs formats, mais je préfère utiliser EXT4 pour tous mes systèmes de fichiers Linux. Utilisez la commande suivante pour formater la partition en EXT4 :

```
mkfs.ext4 /dev/sda2
```

Cette opération peut prendre quelques instants pour se terminer en fonction de la taille de votre partition. Enfin, la partition swap. Utilisez la commande suivante pour la formater :

```bash
mkswap /dev/sda3
```

Avec cela, vous avez terminé le processus de préparation de vos partitions pour l'installation.

### Comment monter les systèmes de fichiers

Maintenant que vous avez créé et formaté vos partitions, vous êtes prêt à les monter. Vous pouvez utiliser la commande `mount` avec des points de montage appropriés pour monter n'importe quelle partition :

```bash
# mount <device> <mount point>

mount /dev/sda2 /mnt
```

J'espère que vous vous souvenez que la partition `/dev/sda2` a été créée pour être la partition racine. Le point de montage `/mnt` dans Linux est destiné au montage temporaire d'un périphérique de stockage. Comme nous avons seulement besoin de monter la partition pour installer Arch Linux dessus, le point de montage `/mnt` est parfait.

Dans le cas d'une partition swap, vous ne la monterez pas comme les autres. Vous devrez dire à Linux d'utiliser cette partition comme swap explicitement. Pour ce faire, exécutez la commande suivante :

```bash
swapon /dev/sda3
```

Comme vous l'avez peut-être deviné, la commande `swapon` indique au système de swaper sur ce périphérique. Nous travaillerons avec la partition système EFI dans une section ultérieure. Pour l'instant, monter ces deux partitions suffira.

### Comment configurer les miroirs

Il y a une dernière étape avant de pouvoir installer Arch Linux sur votre machine, et c'est la configuration des miroirs. Les miroirs sont des serveurs situés à différents points autour du monde pour servir la population à proximité.

L'installateur est fourni avec Reflector, un script Python écrit pour récupérer la dernière liste de miroirs de la page [Arch Linux Mirror Status](https://archlinux.org/mirrors/status/). Pour imprimer la dernière liste de miroirs, exécutez simplement la commande suivante :

```bash
reflector
```

Si vous avez une connexion Internet lente, vous pourriez rencontrer un message d'erreur comme suit :

```bash
failed to rate http(s) download (https://arch.jensgutermuth.de/community/os/x86_64/community.db): Download timed out after 5 second(s).
```

Cela se produit lorsque le délai d'attente par défaut (5 secondes) est inférieur au temps réel qu'il faut pour télécharger les informations.

Vous pouvez remédier à ce problème en utilisant l'option `--download-timeout` :

```bash
reflector --download-timeout 60
```

Maintenant, reflector attendra une minute entière avant de commencer à crier. Une longue liste de miroirs devrait s'afficher sur votre écran :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/VirtualBox_archlinux-2022.01.01-x86_64_13_01_2022_21_36_15-1.png)

Passer en revue toute la liste pour trouver les miroirs à proximité serait fastidieux. C'est pourquoi reflector peut le faire pour vous.

Reflector peut générer une liste de miroirs basée sur une pléthore de contraintes données. Par exemple, je veux une liste de miroirs qui ont été synchronisés au cours des 12 dernières heures et qui sont situés soit en Inde soit à Singapour (ce sont les deux plus proches de ma localisation), et trier les miroirs par vitesse de téléchargement.

Il s'avère que reflector peut faire cela :

```bash
reflector --download-timeout 60 --country India,Singapore --age 12 --protocol https --sort rate
```

Les serveurs trouvés seront listés comme avant :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/VirtualBox_archlinux-2022.01.01-x86_64_13_01_2022_21_45_25.png)

Imprimer une liste de miroirs comme celle-ci ne suffit pas. Vous devrez persister la liste dans l'emplacement `/etc/pacman.d/mirrorlist`. Pacman, le gestionnaire de paquets par défaut pour Arch Linux, utilise ce fichier pour apprendre les miroirs.

Avant d'écraser la liste de miroirs par défaut, faites une copie de celle-ci :

```bash
cp /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.bak
```

Maintenant, exécutez la commande reflector avec l'option `--save` comme suit :

```bash
reflector --download-timeout 60 --country India,Singapore --age 12 --protocol https --sort rate --save /etc/pacman.d/mirrorlist
```

Cette commande générera la liste des miroirs et écrasera celle par défaut. Maintenant, vous êtes prêt à installer le système de base Arch Linux.

### Comment installer le système de base Arch Linux

Avant d'installer le système de base, il est bon de mettre à jour le cache des paquets selon la nouvelle liste des miroirs. Pour ce faire, exécutez la commande suivante :

```bash
pacman -Sy
```

Le programme `pacman` pour Arch Linux est ce que `apt` est pour Ubuntu ou `dnf` pour Fedora. L'option `-S` signifie synchroniser, ce qui est équivalent à `install` dans les gestionnaires de paquets `apt` ou `dnf`.

Une fois le processus de mise à jour terminé, vous pouvez utiliser le script `pacstrap` pour installer le système Arch Linux. Exécutez la commande suivante pour démarrer le processus d'installation :

```bash
pacstrap /mnt base base-devel linux linux-firmware sudo nano ntfs-3g networkmanager
```

Le script `pacstrap` peut installer des paquets dans un répertoire racine spécifié. Comme vous vous en souvenez peut-être, la partition racine a été montée sur le point de montage `/mnt`, donc c'est ce que vous utiliserez avec ce script. Ensuite, vous passerez les noms des paquets que vous souhaitez installer :

* `base` – Ensemble minimal de paquets pour définir une installation basique d'Arch Linux.
* `base-devel` – Groupe de paquets nécessaires pour construire des logiciels à partir de sources.
* `linux` – Le noyau lui-même.
* `linux-firmware` – Pilotes pour le matériel courant.
* `sudo` – Vous voulez exécuter des commandes en tant que root, n'est-ce pas ?
* `nano` – Un clone de l'éditeur pico avec quelques améliorations.
* `ntfs-3g` – Pilote de système de fichiers NTFS et utilitaires nécessaires pour travailler avec les disques NTFS.
* `networkmanager` – Fournit la détection et la configuration pour que les systèmes se connectent automatiquement aux réseaux.

J'aimerais clarifier que cette liste de sept paquets n'est pas quelque chose de obligatoire. Pour avoir une installation fonctionnelle d'Arch Linux, vous avez juste besoin des paquets `base`, `linux` et `linux-firmware`. Mais étant donné que vous aurez besoin des autres de toute façon, pourquoi ne pas tous les attraper en une seule fois.

Selon votre connexion Internet, le processus d'installation peut prendre un certain temps. Asseyez-vous et détendez-vous jusqu'à ce que `pacstrap` fasse son travail. Une fois terminé, vous verrez quelque chose comme suit :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/VirtualBox_archlinux-2022.01.01-x86_64_13_01_2022_22_57_54.png)

Félicitations, vous avez installé avec succès Arch Linux sur votre ordinateur. Il ne reste plus qu'à configurer le système.

## Comment configurer Arch Linux

Installer Arch Linux n'était pas si difficile, n'est-ce pas ? En fait, à mon avis, l'installer est beaucoup plus simple que de le configurer. Il y a beaucoup à faire ici. Alors, commençons.

### Comment générer le fichier Fstab

Selon l'[ArchWiki](https://wiki.archlinux.org/title/Fstab),

> Le fichier `fstab` peut être utilisé pour définir comment les partitions de disque, divers autres périphériques de bloc ou systèmes de fichiers distants doivent être montés dans le système de fichiers.

Dans d'autres distributions comme Ubuntu ou Fedora, cela est généré automatiquement pendant l'installation. Sur Arch, cependant, vous devrez le faire manuellement. Pour ce faire, exécutez la commande suivante :

```bash
genfstab -U /mnt >> /mnt/etc/fstab
```

Le programme `genfstab` peut détecter tous les montages actuels sous un point de montage donné et les imprimer au format compatible fstab vers la sortie standard. Donc `genfstab -U /mnt` imprimera tous les montages actuels sous le point de montage `/mnt`. Nous pouvons sauvegarder cette sortie dans le fichier `/mnt/etc/fstab` en utilisant l'opérateur `>>`.

### Comment se connecter au système nouvellement installé en utilisant Arch-Chroot

Pour l'instant, vous êtes connecté à l'environnement live et non à votre système nouvellement installé. 

Pour continuer à configurer votre système nouvellement installé, vous devrez d'abord vous y connecter. Pour ce faire, exécutez la commande suivante :

```bash
arch-chroot /mnt
```

Le script bash `arch-chroot` fait partie du paquet `arch-install-scripts` et vous permet de passer à l'utilisateur `root` du système nouvellement installé sans aucun redémarrage. C'est cool, non ?

### Comment configurer le fuseau horaire

Une fois que vous avez changé de root, la première chose à configurer est le fuseau horaire. Pour voir une liste de toutes les zones disponibles, exécutez la commande suivante :

```bash
ls /usr/share/zoneinfo
```

Toutes les zones principales devraient être dans le répertoire.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/VirtualBox_archlinux-2022.01.01-x86_64_13_01_2022_23_45_19.png)

Je vis à Dhaka, au Bangladesh, qui se trouve dans la zone Asie. Si je liste le contenu de l'Asie, je devrais voir Dhaka là :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/VirtualBox_archlinux-2022.01.01-x86_64_13_01_2022_23_45_44.png)

Pour définir Asia/Dhaka comme mon fuseau horaire par défaut, je devrai créer un lien symbolique du fichier à l'emplacement `/etc/localtime` :

```bash
ln -sf /usr/share/zoneinfo/Asia/Dhaka /etc/localtime
```

La commande `ln` est utilisée pour créer des liens symboliques. Les options `-sf` indiquent respectivement soft et force.

### Comment configurer la localisation

Maintenant, vous devrez configurer vos langues. Arch Linux a une manière facile de le faire également. 

Tout d'abord, vous devrez modifier le fichier `etc/locale.gen` selon votre localisation. Ouvrez le fichier dans l'éditeur de texte nano :

```bash
nano /etc/locale.gen
```

Vous verrez une longue liste de langues :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/VirtualBox_archlinux-2022.01.01-x86_64_13_01_2022_23_46_29.png)

Vous devrez décommenter les langues que vous souhaitez activer. J'ai généralement besoin seulement de l'anglais et du bengali. Je vais donc localiser les langues `en_US.UTF-8 UTF-8`, `bn_BD UTF-8` et `bn_IN UTF-8`. Enregistrez le fichier en appuyant sur Ctrl + O et quittez nano en appuyant sur la combinaison de touches Ctrl + X.

Maintenant, vous devrez exécuter la commande suivante :

```bash
locale-gen
```

La commande `locale-gen` lira votre fichier `/etc/locale.gen` et générera les locales en conséquence.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/VirtualBox_archlinux-2022.01.01-x86_64_13_01_2022_23_57_55.png)

Maintenant que vous avez activé plusieurs langues, vous devrez dire à Arch Linux laquelle utiliser par défaut. Pour ce faire, ouvrez le fichier `/etc/locale.conf` et ajoutez la ligne suivante :

```conf
LANG=en_US.UTF-8
```

C'est tout ce que vous devez faire pour configurer votre locale. Vous pouvez toujours revenir au fichier `/etc/locale.gen` et ajouter ou supprimer des langues. N'oubliez simplement pas d'exécuter `locale-gen` chaque fois que vous faites cela.

En plus des locales, si vous avez apporté des modifications à vos dispositions de clavier de console dans la première étape de l'installation, vous pourriez vouloir les conserver maintenant. Pour ce faire, ouvrez le fichier `/etc/vconsole.conf` et ajoutez vos dispositions de clavier préférées.

Par exemple, si vous avez changé les dispositions de clavier par défaut en `mac-us` dans la première étape, vous pourriez vouloir ajouter la ligne suivante au fichier `vconsole.conf` :

```bash
KEYMAP=mac-us
```

Maintenant, chaque fois que vous utiliserez la console virtuelle, elle aura la bonne disposition de clavier et vous n'aurez pas à la configurer à chaque fois.

### Comment configurer le réseau

Configurer un réseau manuellement dans n'importe quelle distribution Linux peut être délicat. C'est pourquoi je vous ai conseillé d'installer le paquet `networkmanager` pendant l'installation du système. Si vous avez fait comme je l'ai dit, vous êtes prêt à partir. Sinon, utilisez `pacman` pour installer le paquet maintenant :

```bash
pacman -S networkmanager
```

Pacman est un gestionnaire de paquets. Vous en apprendrez plus à ce sujet plus tard. Définissons maintenant le nom d'hôte pour votre ordinateur. Un nom d'hôte est un nom unique créé pour identifier une machine sur un réseau, écrit dans le fichier `/etc/hostname`.

Ouvrez le fichier avec nano et écrivez votre nom d'hôte dedans. Vous pouvez utiliser n'importe quoi pour identifier votre machine. J'utilise généralement la marque ou le modèle de mon appareil comme nom d'hôte et comme je suis sur un ordinateur portable legion, je vais simplement écrire ce qui suit :

```
legion
```

La résolution du nom d'hôte local est fournie par `nss-myhostname` (un module NSS fourni par systemd) sans avoir à éditer le fichier `/etc/hosts`. Il est activé par défaut.

Mais certains logiciels peuvent encore lire directement le fichier `/etc/hosts`. Ouvrez le fichier dans nano et ajoutez les lignes suivantes :

```
127.0.0.1        localhost
::1              localhost
127.0.1.1        legion
```

Assurez-vous de remplacer `legion` par votre nom d'hôte. Vous pouvez maintenant installer le paquet mentionné ci-dessus :

```bash
pacman -S networkmanager
```

Activez le service `NetworkManager` en exécutant la commande suivante :

```bash
systemctl enable NetworkManager
```

Assurez-vous d'écrire `NetworkManager` et non `networkmanager` comme nom de service. Si la commande réussit, le gestionnaire de réseau démarrera automatiquement au démarrage à partir de maintenant et fera son travail.

### Comment définir le mot de passe root

Vous pourriez vouloir définir un mot de passe pour l'utilisateur root, pourquoi pas ? Pour ce faire, exécutez la commande suivante :

```bash
passwd
```

La commande `passwd` vous permet de changer le mot de passe d'un utilisateur. Par défaut, elle affecte le mot de passe de l'utilisateur actuel, qui est `root` pour le moment.

Elle vous demandera un nouveau mot de passe et un mot de passe de confirmation. Entrez-les soigneusement et assurez-vous de ne pas oublier le mot de passe.

### Comment créer un utilisateur non-root

Utiliser votre système Linux en tant qu'utilisateur root pendant longtemps n'est pas une bonne idée. Donc, créer un utilisateur non-root est important. Pour créer un nouvel utilisateur, exécutez la commande suivante :

```bash
useradd -m -G wheel farhan
```

La commande `useradd` vous permet de créer un nouvel utilisateur. Assurez-vous de remplacer mon nom par celui que vous souhaitez utiliser. L'option `-m` indique que vous souhaitez également qu'elle crée le répertoire personnel correspondant. L'option `-G` ajoutera le nouvel utilisateur au groupe `wheel`, qui est le groupe d'utilisateurs d'administration dans Arch Linux.

Vous pouvez maintenant utiliser la commande `passwd` une fois de plus pour définir le mot de passe pour le nouvel utilisateur créé :

```bash
passwd farhan
```

Le programme vous demandera un nouveau mot de passe et une confirmation de mot de passe. Encore une fois, n'oubliez pas de remplacer mon nom par celui que vous avez utilisé.

Enfin, vous devrez activer les privilèges `sudo` pour cet nouvel utilisateur. Pour ce faire, ouvrez le fichier `/etc/sudoers` en utilisant nano. Une fois ouvert, localisez la ligne suivante et décommentez-la :

```
# %wheel ALL=(ALL) ALL
```

Ce fichier signifie essentiellement que tous les utilisateurs du groupe `wheel` peuvent utiliser `sudo` en fournissant leur mot de passe. Enregistrez le fichier en appuyant sur Ctrl + O et quittez nano en appuyant sur Ctrl + X. Maintenant, le nouvel utilisateur pourra utiliser `sudo` lorsque cela sera nécessaire.

### Comment installer le microcode

Selon [PCMag](https://www.pcmag.com/encyclopedia/term/microcode),

> Un ensemble d'instructions élémentaires dans un ordinateur à jeu d'instructions complexe (CISC). Le microcode réside dans une mémoire haute vitesse séparée et fonctionne comme une couche de traduction entre les instructions machine et le niveau circuit de l'ordinateur. Le microcode permet au concepteur de l'ordinateur de créer des instructions machine sans avoir à concevoir des circuits électroniques.

Les fabricants de processeurs tels qu'Intel et AMD publient souvent des mises à jour de stabilité et de sécurité pour le processeur. Ces mises à jour sont cruciales pour la stabilité du système. 

Dans Arch Linux, les mises à jour de microcode sont disponibles via des paquets officiels que chaque utilisateur devrait installer sur ses systèmes.

```bash
# pour les processeurs amd
pacman -S amd-ucode

# pour les processeurs intel
pacman -S intel-ucode
```

Cependant, installer ces paquets ne suffit pas. Vous devrez vous assurer que votre chargeur de démarrage les charge. Vous en apprendrez plus à ce sujet dans la section suivante.

### Comment installer et configurer un chargeur de démarrage

Selon [Wikipedia](https://en.wikipedia.org/wiki/Bootloader),

> Un chargeur de démarrage, également orthographié boot loader ou appelé boot manager et bootstrap loader, est un programme informatique responsable du démarrage d'un ordinateur.

Les détails internes du chargeur de démarrage sont hors du cadre de cet article, donc je vais simplement continuer avec le processus d'installation. Si vous avez utilisé une autre distribution Linux dans le passé, vous avez peut-être rencontré le menu GRUB.

GRUB est l'un des chargeurs de démarrage les plus populaires. Bien qu'il existe un certain nombre d'options disponibles, je vais démontrer l'installation de GRUB car c'est ce que la plupart des gens utiliseront probablement.

Pour installer GRUB, vous devrez d'abord installer deux paquets.

```bash
pacman -S grub efibootmgr
```

Si vous installez à côté d'autres systèmes d'exploitation, vous aurez également besoin du paquet `os-prober` :

```bash
pacman -S os-prober
```

Ce programme recherchera les systèmes d'exploitation déjà installés sur votre système et les inclura dans le fichier de configuration de GRUB. 

Maintenant, vous devrez monter la partition système EFI que vous avez créée il y a quelques sections. Pour ce faire, vous devrez d'abord créer un répertoire `efi` :

```bash
mkdir /boot/efi
```

Selon [Wikipedia](https://en.wikipedia.org/wiki//boot/),

> Dans Linux, et d'autres systèmes d'exploitation de type Unix, le répertoire `/boot/` contient les fichiers utilisés pour démarrer le système d'exploitation.

Ce répertoire est présent dans tous les systèmes d'exploitation de type Unix. La commande mentionnée ci-dessus crée un répertoire appelé `efi` à l'intérieur du répertoire `/boot`. Après avoir créé le répertoire, vous devrez monter votre partition système EFI dans ce répertoire.

```bash
mount /dev/sda1 /boot/efi
```

J'espère que vous vous souvenez que nous avons formaté le périphérique `/dev/sda1` en tant que partition système EFI lors de la phase de partitionnement. Assurez-vous d'utiliser le bon pour votre périphérique. 

Maintenant, nous utiliserons la commande `grub-install` pour installer GRUB dans la partition système EFI nouvellement montée :

```bash
grub-install --target=x86_64-efi --bootloader-id=grub
```

Vous pouvez plus ou moins utiliser cette commande mot à mot. Vous pouvez changer le `--bootloader-id` en quelque chose de plus expressif comme `arch` ou autre chose. Si l'installation se termine sans erreur, vous devrez ensuite générer le fichier de configuration GRUB.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/VirtualBox_archlinux-2022.01.01-x86_64_14_01_2022_18_34_01.png)

Si vous installez à côté d'autres systèmes d'exploitation, vous devrez activer `os-prober` avant de générer le fichier de configuration. Pour ce faire, ouvrez le fichier `/etc/default/grub` dans l'éditeur de texte nano. Localisez la ligne suivante et décommentez-la :

```
#GRUB_DISABLE_OS_PROBER=false
```

Cela devrait être la dernière ligne dans le fichier mentionné ci-dessus, alors faites simplement défiler jusqu'en bas et décommentez-la.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/VirtualBox_archlinux-2022.01.01-x86_64_14_01_2022_18_31_41.png)

Maintenant, exécutez la commande suivante pour générer le fichier de configuration :

```bash
grub-mkconfig -o /boot/grub/grub.cfg
```

La commande `grub-mkconfig` génère le fichier de configuration GRUB et l'enregistre à un emplacement cible donné. Dans ce cas, `/boot/grub/grub.cfg` est l'emplacement cible.

La commande prendra également en compte le microcode que vous avez installé précédemment et tout autre système d'exploitation existant sur votre machine.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/VirtualBox_archlinux-2022.01.01-x86_64_14_01_2022_18_35_45.png)

Félicitations, vous avez maintenant une installation fonctionnelle d'Arch Linux. À ce stade, vous pouvez quitter l'environnement Arch-Chroot, démonter la partition et redémarrer. Mais je vous suggérerais de rester un peu plus longtemps et de configurer également l'interface utilisateur graphique.

## Comment installer Xorg

Pour exécuter des programmes avec des interfaces utilisateur graphiques sur votre système, vous devrez installer une implémentation du système de fenêtres X. La plus courante est Xorg. 

Pour installer Xorg, exécutez la commande suivante :

```bash
pacman -S xorg-server
```

Attendez que l'installation soit terminée, puis passez à l'installation des pilotes graphiques nécessaires.

## Comment installer les pilotes graphiques

L'installation des pilotes graphiques sur Arch Linux est très simple. Vous installez simplement les paquets requis par votre unité de traitement graphique et c'est tout.

```bash
# pour les unités de traitement graphique nvidia
pacman -S nvidia nvidia-utils

# pour les unités de traitement graphique amd discrètes et intégrées
pacman -S xf86-video-amdgpu

# pour les unités de traitement graphique intel intégrées
pacman -S xf86-video-intel
```

Si vous avez besoin d'une assistance supplémentaire, n'hésitez pas à consulter la page [ArchWiki](https://wiki.archlinux.org/title/Xorg).

## Comment installer un environnement de bureau

Maintenant que vous avez installé Xorg et les pilotes graphiques nécessaires, vous êtes prêt à installer un environnement de bureau comme GNOME, Plasma ou XFCE. 

Arch Linux prend en charge une longue liste d'environnements de bureau, mais j'ai seulement essayé GNOME et Plasma. Je vais vous montrer comment vous pouvez installer l'un de ces deux.

### Comment installer GNOME

Pour installer GNOME, vous devrez installer le paquet `gnome`. Pour ce faire, exécutez la commande suivante :

```bash
pacman -S gnome
```

Pendant l'installation, vous aurez plusieurs choix pour les paquets `pipwire-session-manager` et `emoji-font`. Acceptez les valeurs par défaut en appuyant sur Entrée dans les deux invites. L'installation peut prendre un certain temps pour se terminer.

Le paquet `gnome` est livré avec GDM ou Gnome Display Manager. Vous pouvez activer le service en exécutant la commande suivante :

```bash
systemctl enable gdm
```

C'est tout ce que vous devez faire pour faire fonctionner GNOME sur votre système Arch.

### Comment installer Plasma

L'installation de KDE Plasma n'est pas très différente de celle de GNOME. Vous devrez installer les paquets liés à Plasma au lieu de GNOME.

```bash
pacman -S plasma plasma-wayland-session
```

Si vous avez une carte graphique NVIDIA, évitez d'installer `plasma-wayland-session` et utilisez le bon vieux X11. Je possède deux appareils avec des GPU NVIDIA et les deux ont montré des instabilités lors de l'utilisation de Wayland.

Pendant l'installation, vous aurez plusieurs choix pour les paquets `ttf-font`, `pipwire-session-manager` et `phonon-qt5-backend`. Assurez-vous de choisir `noto-fonts` comme votre `ttf-font` et acceptez les valeurs par défaut pour les deux autres.

Comme `gdm` dans GNOME, Plasma est livré avec `sddm` comme gestionnaire d'affichage par défaut. Exécutez la commande suivante pour activer le service :

```bash
systemctl enable sddm
```

Et c'est tout ce que vous devez faire pour faire fonctionner Plasma sur votre système Arch Linux.

## Comment finaliser l'installation

Maintenant que vous avez installé Arch Linux et passé par toutes les étapes de configuration nécessaires, vous pouvez redémarrer sur votre système nouvellement installé. Pour ce faire, sortez d'abord de l'environnement Arch-Chroot :

```bash
exit
```

Ensuite, démontez la partition racine pour vous assurer qu'il n'y a pas d'opérations en attente :

```bash
umount -R /mnt
```

Maintenant, redémarrez la machine :

```bash
reboot
```

Attendez jusqu'à ce que vous voyiez le menu GRUB.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/VirtualBox_archlinux-2022.01.01-x86_64_14_01_2022_20_10_25.png)

Choisissez Arch Linux dans la liste et attendez que le système termine le démarrage.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/VirtualBox_archlinux-2022.01.01-x86_64_14_01_2022_20_11_15.png)

Connectez-vous avec vos identifiants utilisateur et voilà !

![Image](https://www.freecodecamp.org/news/content/images/2022/01/VirtualBox_archlinux-2022.01.01-x86_64_14_01_2022_20_15_41.png)

Votre nouveau système Arch Linux flambant neuf est prêt à faire des merveilles.

## Comment basculer entre les environnements de bureau

Contrairement à d'autres distributions étroitement couplées avec leur environnement de bureau par défaut, Arch est flexible. Vous pouvez passer à un autre environnement de bureau chaque fois que vous en avez envie. 

Pour ce faire, déconnectez-vous d'abord de votre session actuelle.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/VirtualBox_archlinux-2022.01.01-x86_64_14_01_2022_20_11_15.png)

Comme vous pouvez le voir, j'utilise actuellement Plasma. Passez maintenant à TTY2 en appuyant sur la combinaison de touches Ctrl + Alt + F2. Vous verrez une invite de connexion à la console :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/VirtualBox_archlinux-2022.01.01-x86_64_14_01_2022_20_18_54.png)

Connectez-vous avec les identifiants root et désactivez le gestionnaire d'affichage `sddm`.

```bash
systemctl disable sddm
```

Ensuite, désinstallez les paquets liés à Plasma que vous avez installés précédemment :

```bash
sudo pacman -Rns plasma plasma-wayland-session
```

Une fois les paquets désinstallés, installez les paquets nécessaires pour GNOME :

```bash
pacman -S gnome
```

Ensuite, effectuez l'installation selon la section que vous avez lue précédemment. Après que le paquet `gnome` ait été installé, activez le gestionnaire d'affichage `gdm` :

```bash
systemctl enable gdm
```

Redémarrez l'ordinateur.

```bash
reboot
```

Attendez que le système Arch Linux termine le démarrage.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/VirtualBox_archlinux-2022.01.01-x86_64_14_01_2022_20_24_11.png)

Et voilà, le magnifique Gnome Display Manager. Connectez-vous avec vos identifiants.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/VirtualBox_archlinux-2022.01.01-x86_64_14_01_2022_19_53_31.png)

Vous pouvez basculer entre les environnements de bureau autant que vous le souhaitez, mais je vous suggérerais de vous installer avec l'un d'eux. De plus, je ne recommanderais pas d'en avoir plusieurs installés en même temps.

## Comment gérer les paquets avec Pacman

Vous avez déjà installé un certain nombre de paquets en utilisant pacman. Il est équivalent aux gestionnaires de paquets comme apt dans Ubuntu et dnf dans Fedora.

Dans cette section, je vais vous présenter quelques-unes des commandes pacman courantes dont vous pourriez avoir besoin au quotidien.

### Comment installer des paquets avec Pacman

Pour installer un paquet en utilisant pacman, vous pouvez utiliser la syntaxe de commande suivante :

```bash
# sudo pacman -S <package name>

sudo pacman -S rust
```

Vous pouvez installer plusieurs paquets comme suit :

```bash
# sudo pacman -S <package name> <package name>

sudo pacman -S rust golang
```

Vous pouvez également spécifier le dépôt à partir duquel vous souhaitez installer le paquet, comme ceci :

```bash
# sudo pacman -S <package repository>/<package name>

sudo pacman -S extra/rust
```

Dans cette commande, l'option `-S` signifie synchroniser, ce qui est équivalent à installer dans le cas des gestionnaires de paquets apt ou dnf.

### Comment supprimer des paquets avec Pacman

Pour supprimer un paquet en utilisant pacman, vous pouvez utiliser la syntaxe suivante :

```bash
# sudo pacman -R <package name>

sudo pacman -R rust
```

Cela supprimera le paquet mais laissera les dépendances. Vous pouvez supprimer le paquet avec les dépendances si elles ne sont pas requises par un autre paquet en exécutant la commande suivante :

```bash
# sudo pacman -Rs <package name>

sudo pacman -Rs rust
```

Pacman sauvegarde souvent des fichiers de configuration importants lors de la suppression de certaines applications. Vous pouvez outrepasser ce comportement en utilisant la syntaxe suivante :

```bash
# sudo pacman -Rn <package name>

sudo pacman -Rn rust
```

J'utilise généralement `sudo pacman -Rns` chaque fois que je veux désinstaller quelque chose. Une dernière chose que je veux montrer est comment supprimer les paquets orphelins.

Dans Ubuntu, la commande `sudo apt autoremove` désinstalle tout paquet inutile. La commande équivalente dans Arch est :

```bash
sudo pacman -Qdtq | pacman -Rs -
```

Cela nettoiera tout paquet restant des paquets précédemment installés.

### Comment mettre à jour des paquets avec Pacman

Pour mettre à jour tous les paquets de votre système, vous pouvez utiliser la syntaxe suivante :

```bash
sudo pacman -Syu
```

Dans cette commande, l'option `S` synchronise les paquets, `y` rafraîchit le cache local des paquets, et `u` met à jour le système. C'est comme la commande de mise à jour ultime et je l'exécute au moins une fois par jour.

### Comment rechercher des paquets avec Pacman

Pour rechercher un paquet dans la base de données, vous pouvez utiliser la syntaxe suivante :

```bash
# sudo pacman -Ss <package name>

sudo pacman -Ss rust
```

Cela imprimera tous les paquets trouvés dans la base de données avec ce terme de recherche et indiquera également si l'un d'eux est déjà installé.

Si vous souhaitez vérifier si un paquet est déjà installé ou non, vous pouvez utiliser la commande suivante :

```bash
# sudo pacman -Qs <package name>

sudo pacman -Qs rust
```

Cela est utile lorsque vous souhaitez désinstaller un paquet mais que vous ne connaissez pas son nom exact.

## Comment utiliser AUR dans Arch Linux

Selon [It's FOSS](https://itsfoss.com/aur-arch-linux/),

> AUR signifie Arch User Repository. Il s'agit d'un dépôt communautaire pour les utilisateurs de distributions Linux basées sur Arch. Il contient des descriptions de paquets appelées PKGBUILDs qui vous permettent de compiler un paquet à partir de la source avec makepkg, puis de l'installer via pacman (gestionnaire de paquets dans Arch Linux).

AUR est l'une des fonctionnalités les plus attrayantes d'Arch Linux. C'est grâce à AUR qu'Arch Linux a un nombre de paquets presque égal à Debian. Vous avez déjà utilisé `pacman` pour installer divers paquets. Malheureusement, vous ne pouvez pas l'utiliser pour installer des paquets depuis AUR.

Vous devrez installer l'un des assistants AUR à la place. Arch Linux ne supporte aucun de ces assistants et vous conseille d'apprendre à construire des paquets manuellement. Je vais expliquer les deux techniques ici. Si vous comprenez comment fonctionne un assistant, vous serez également capable de le faire manuellement.

### Comment installer des paquets avec un assistant

Parmi les assistants AUR disponibles et actuellement maintenus, j'aime bien `yay` ou yet another yogurt package. Il est écrit en Go et est assez solide. 

Vous ne pouvez pas installer `yay` comme les autres paquets. Vous devrez obtenir le code source et compiler le programme. Vous aurez besoin de `git` et du paquet `base-devel` pour ce faire. En supposant que vous avez déjà installé `base-devel` pendant l'installation d'Arch Linux :

```bash
pacman -S git
```

Clonez le dépôt yay depuis GitHub et `cd` dedans :

```bash
git clone https://aur.archlinux.org/yay.git && cd yay
```

Pour construire et installer yay à partir de la source, exécutez la commande suivante :

```bash
makepkg -si
```

Le script makepkg automatise le processus de construction des paquets. Les options `-si` signifient synchroniser les dépendances et installer. La première option installera les dépendances requises (Golang dans ce cas) et l'option suivante installera le paquet construit.

Après la fin du processus de construction, makepkg demandera une confirmation d'installation et votre mot de passe. Saisissez votre mot de passe soigneusement et laissez l'installation se terminer.

Vérifiez si yay a été installé correctement ou non :

```bash
yay --version

# yay v11.1.0 - libalpm v13.0.1
```

Maintenant, installons quelque chose en utilisant yay. L'un des paquets courants que vous pourriez vouloir installer est le paquet [visual-studio-code-bin](https://aur.archlinux.org/packages/visual-studio-code-bin/). Pour ce faire, exécutez la commande suivante :

```bash
yay -S visual-studio-code-bin
```

Contrairement à pacman, vous ne devriez pas exécuter yay avec sudo. Yay recherchera le paquet donné et vous demandera si vous souhaitez voir le diff ou non :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/VirtualBox_archlinux-2022.01.01-x86_64_14_01_2022_21_07_26.png)

Tous les dépôts sur AUR sont livrés avec un fichier PKGBUILD qui contient les instructions pour construire ce paquet. Yay a cette fonctionnalité sympa où il vous montre ce qui a changé dans le fichier PKGBUILD depuis la dernière fois.

Pour l'instant, je vais choisir `N` pour aucun et appuyer sur entrée. Yay recherchera maintenant les dépendances et vous demandera votre mot de passe pour les installer.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/VirtualBox_archlinux-2022.01.01-x86_64_14_01_2022_21_19_58.png)

Confirmez l'installation et fournissez votre mot de passe. Yay installera ensuite les dépendances et commencera à construire le paquet. Une fois construit, yay installera le paquet et vous demandera votre mot de passe lorsque cela sera nécessaire.

Après la fin de l'installation, recherchez Visual Studio Code dans le lanceur d'applications :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/VirtualBox_archlinux-2022.01.01-x86_64_14_01_2022_21_28_42.png)

Félicitations pour l'installation de votre premier paquet depuis AUR. Les commandes de Yay sont presque identiques à celles de pacman, donc si vous pouvez faire quelque chose avec pacman, vous devriez également pouvoir le faire avec yay.

En fait, yay peut également installer des paquets depuis les dépôts officiels d'Arch Linux comme pacman. Mais je vous suggérerais d'utiliser yay uniquement pour installer des paquets depuis AUR lorsque cela est nécessaire et pacman pour tout le reste.

### Comment installer des paquets manuellement

Comme je l'ai dit dans la section précédente, l'ArchWiki suggère d'éviter tout assistant AUR et d'installer manuellement les paquets depuis AUR. Je vais maintenant vous montrer comment faire.

Assurez-vous d'avoir les paquets `git` et `base-devel` installés. Sinon, utilisez `pacman` pour les installer.

Pour la démonstration, installons Spotify cette fois. Visitez d'abord la page AUR pour le paquet spotify - [https://aur.archlinux.org/packages/spotify/](https://aur.archlinux.org/packages/spotify/) et copiez l'"URL de clonage Git" de là.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/image-68.png)

La page liste même toutes les dépendances dont vous aurez besoin. Clonez le dépôt sur votre machine :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/VirtualBox_archlinux-2022.01.01-x86_64_16_01_2022_21_16_43.png)

Chaque dépôt AUR est livré avec un fichier PKGBUILD contenant les instructions pour construire le paquet. Chaque fois que vous installez un paquet depuis AUR, c'est une excellente idée de vérifier le fichier PKGBUILD en utilisant quelque chose comme la commande `cat` :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/VirtualBox_archlinux-2022.01.01-x86_64_16_01_2022_21_22_37.png)

Assurez-vous qu'il n'y a rien de nuisible dans le fichier. Une fois que vous êtes satisfait, utilisez `makepkg` pour installer les dépendances, construire le paquet et l'installer. Idéalement, il ne devrait pas y avoir de problèmes, mais parfois, les choses peuvent prendre un tournant inattendu.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/VirtualBox_archlinux-2022.01.01-x86_64_16_01_2022_21_34_29.png)

Dans ces cas, retournez à la page AUR correspondante et vérifiez les commentaires des utilisateurs. Comme dans ce cas, j'ai trouvé le commentaire épinglé suivant :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/image-69.png)

Il s'avère que le paquet vous demande d'ajouter la clé gpg de Spotify pour Linux à la chaîne de clés utilisateur. Cette commande télécharge la clé gpg en utilisant `curl` et la transmet en entrée de la commande `gpg --import` :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/VirtualBox_archlinux-2022.01.01-x86_64_16_01_2022_21_37_50.png)

Essayez d'exécuter `makepkg -si` une fois de plus et tout devrait fonctionner correctement cette fois :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/VirtualBox_archlinux-2022.01.01-x86_64_16_01_2022_21_39_33.png)

Vous voyez, je vous l'avais dit ! L'installation manuelle de paquets implique souvent un tel dépannage, mais l'aide est presque toujours à portée de main dans les commentaires. Écoutez un peu de musique maintenant.

## Comment résoudre les problèmes courants

Écoutez, j'utilise Arch comme système principal sur tous mes appareils depuis quelques années maintenant, mais je rencontre encore des problèmes. Heureusement, il y a des endroits formidables où chercher de l'aide lorsque vous êtes bloqué :

* [ArchWiki](https://wiki.archlinux.org/)
* [Forum Arch Linux](https://bbs.archlinux.org/)
* [r/archlinux](https://www.reddit.com/r/archlinux/)

Pour la plupart, le wiki devrait avoir les informations que vous cherchez. En fait, si vous êtes sur un ordinateur portable et que vous avez des difficultés à faire fonctionner quelque chose, il existe une catégorie entière du wiki [catégorie](https://wiki.archlinux.org/title/Category:Laptops) dédiée à différents ordinateurs portables. Alors, regardez autour du wiki.

Si le wiki ne parvient pas à résoudre votre problème, demandez alors à d'autres utilisateurs sur le forum ainsi que sur le subreddit. Mais chaque fois que vous faites cela, assurez-vous de faire vos recherches d'abord et d'inclure autant de descriptions que possible dans le message. C'est vraiment ennuyeux si d'autres utilisateurs doivent continuer à vous demander plus d'informations et cela réduira également les chances que vous obteniez une réponse.

## Comment utiliser l'ISO live Arch comme média de secours

Quoi que les gens puissent dire, Arch Linux est très stable tant que vous savez ce que vous faites. Si vous vous mettez à installer chaque paquet bizarre que vous rencontrez dans l'AUR ou à changer de noyaux différents sans savoir à quoi ils servent, votre système pourrait ne pas démarrer.

Dans ces cas, vous pouvez utiliser votre clé USB live comme média de secours. Pour ce faire, reconnectez la clé USB bootable à votre ordinateur et démarrez dans l'environnement live. Une fois là, configurez l'heure, les dispositions de clavier et les polices si vous le souhaitez.

Ensuite, utilisez `fdisk` pour lister toutes vos partitions et localisez celle qui contient votre installation d'Arch Linux. Dans mon cas, c'est la partition `/dev/sda2`. Montez la partition comme vous l'avez fait auparavant :

```bash
mount /dev/sda2 /mnt
```

Maintenant, utilisez Arch-Chroot pour vous connecter en tant qu'utilisateur root.

```bash
arch-chroot /mnt
```

Maintenant, désinstallez le mauvais paquet que vous avez installé ou revenez à une version de noyau qui fonctionnait dans le passé, et ainsi de suite. Une fois terminé, quittez l'environnement Arch-Chroot, démontez la partition et redémarrez :

```bash
exit
umount -R /mnt
reboot
```

Si l'ordinateur démarre correctement, alors félicitations. Sinon, essayez le wiki, le forum ou le subreddit. Si rien ne fonctionne, vous devrez peut-être faire une nouvelle installation.

## Lectures complémentaires

Si vous êtes arrivé jusqu'ici, vous avez déjà fait beaucoup de lecture – mais ce n'est pas tout. Ce manuel entier a été écrit en combinant des informations du wiki, du forum et du subreddit. Je liste quelques pages du wiki que je pense que vous devriez lire.

* [Guide d'installation](https://wiki.archlinux.org/title/Installation_guide)
* [Configuration du réseau](https://wiki.archlinux.org/title/Network_configuration)
* [Recommandations générales](https://wiki.archlinux.org/title/General_recommendations)
* [Environnement de bureau](https://wiki.archlinux.org/title/Desktop_environment)
* [pacman](https://wiki.archlinux.org/title/pacman)
* [Arch Build System](https://wiki.archlinux.org/title/Arch_Build_System)
* [makepkg](https://wiki.archlinux.org/title/makepkg)
* [Liste des applications](https://wiki.archlinux.org/title/List_of_applications)

Je n'ai pas pu en penser d'autres pour le moment, mais je garderai cette liste à jour.

## Conclusion

Je tiens à vous remercier du fond du cœur pour le temps que vous avez passé à lire cet article. J'espère que vous avez apprécié votre temps et que vous avez appris beaucoup de choses non seulement sur Arch, mais aussi sur Linux en général.

En plus de celui-ci, j'ai écrit des manuels complets sur d'autres sujets compliqués disponibles gratuitement sur [freeCodeCamp](https://www.freecodecamp.org/news/author/farhanhasin/).

Ces manuels font partie de ma mission de simplifier les technologies difficiles à comprendre pour tout le monde. Chacun de ces manuels prend beaucoup de temps et d'efforts à écrire.

Si vous avez apprécié mon écriture et souhaitez me motiver, envisagez de laisser des étoiles sur [GitHub](https://github.com/fhsinchy/) et de m'endosser pour des compétences pertinentes sur [LinkedIn](https://www.linkedin.com/in/farhanhasin/).

Je suis toujours ouvert aux suggestions et aux discussions sur [Twitter](https://twitter.com/frhnhsin) ou [LinkedIn](https://www.linkedin.com/in/farhanhasin/). Envoyez-moi des messages directs.

Enfin, envisagez de partager les ressources avec les autres, car

> Dans l'open source, nous pensons fermement que pour vraiment faire quelque chose de bien, vous devez impliquer beaucoup de gens. — Linus Torvalds

Jusqu'au prochain, restez en sécurité et continuez à apprendre.