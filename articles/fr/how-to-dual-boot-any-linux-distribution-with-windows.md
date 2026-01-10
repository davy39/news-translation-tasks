---
title: Comment faire un dual boot avec n'importe quelle distribution Linux et Windows
  – et s'en débarrasser si nécessaire
subtitle: ''
author: Farhan Hasin Chowdhury
co_authors: []
series: null
date: '2021-12-23T16:32:46.000Z'
originalURL: https://freecodecamp.org/news/how-to-dual-boot-any-linux-distribution-with-windows
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/How-to-Dual-Boot-Any-Linux-Distribution-With-Windows.png
tags:
- name: Linux
  slug: linux
- name: Ubuntu
  slug: ubuntu
- name: Windows
  slug: windows
seo_title: Comment faire un dual boot avec n'importe quelle distribution Linux et
  Windows – et s'en débarrasser si nécessaire
seo_desc: Gone are the days when Linux and Windows were like two opposing forces.
  Microsoft has embraced the open-source community quite cordially in recent years,
  and as a result we have things like Windows Subsystem for Linux baked right into
  our Windows ins...
---

Les jours où Linux et Windows étaient comme deux forces opposées sont révolus. Microsoft a embrassé la communauté open-source de manière assez cordiale ces dernières années, et en conséquence, nous avons des choses comme le [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/) intégré directement dans nos installations Windows.

Cela ne signifie pas que nous n'avons plus besoin d'une installation complète de Linux. En fait, les machines avec Windows et Linux fonctionnant côte à côte sont assez courantes.

Mais savez-vous ce qui est plus courant que les machines exécutant les deux systèmes d'exploitation ? Les propriétaires de machines qui ont tenté de faire un dual boot et ont fini par perdre beaucoup de données dans le processus.

Alors, si vous êtes l'une des victimes ou l'un de ceux qui essaient d'éviter les catastrophes possibles dans leur prochaine aventure de dual boot, cet article est pour vous. Ici, vous apprendrez :

* Comment installer n'importe quelle distribution Linux aux côtés de Windows
* Comment se débarrasser de Linux sans tout casser sous Windows si nécessaire
* Les problèmes courants, les idées fausses et leurs solutions, et
* Quelques trucs geek en général pour impressionner vos pairs

Sans plus attendre, prenons une tasse de café ou de thé ou au moins d'eau et plongeons directement dans le processus.

## Quelques hypothèses que je fais

Avant de plonger dans le cœur du tutoriel, je veux clarifier quelques choses. Pour rendre cet article entier abordable, je fais les hypothèses suivantes sur votre système :

* Votre ordinateur utilise UEFI et non BIOS
* Vous avez déjà Windows installé sur votre machine
* Vous avez une clé USB suffisamment grande (4 Go) pour démarrer Linux
* Vous avez assez d'espace (25 Go) pour installer Linux sur votre HDD ou SSD

C'est à peu près tout. Si vous avez tout ce qui précède prêt, vous êtes bon pour continuer.

## Comment créer une clé USB Linux bootable

Il existe plusieurs outils qui peuvent vous aider à créer une clé USB Linux bootable. Parmi tous ces outils, mes préférés sont :

* [balenaEtcher](https://www.balena.io/etcher/)
* [Fedora Media Writer](https://getfedora.org/en/workstation/download/)

Ces deux outils sont open-source, gratuits et disponibles sur presque toutes les plateformes majeures. Pour cet article, je vais utiliser Fedora Media Writer simplement parce qu'il n'y a pas beaucoup de tutoriels qui en parlent et parce que je l'utilise personnellement.

Comme son nom l'indique, Fedora Media Writer est un outil créé par Red Hat pour faire des clés USB Linux bootables. Une fois que vous avez téléchargé le programme, installez-le sur votre système et lancez-le.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/fedora-media-writer.png)

Voici à quoi il ressemble. Comme vous pouvez le voir, vous avez l'option de télécharger les dernières ISO Fedora ainsi qu'une option pour choisir une image personnalisée depuis vos disques.

Sauf si vous prévoyez d'installer Fedora (spoiler ! c'est ma préférée) sur votre machine, vous devrez télécharger votre fichier ISO souhaité.

Dans cet article, j'utiliserai [Ubuntu](https://ubuntu.com/) parce qu'il est plus populaire parmi les nouveaux venus. Mais les choses que vous apprendrez ici peuvent être appliquées à n'importe quelle autre distribution Linux.

Allez-y et téléchargez l'ISO pour Ubuntu depuis leur page de [téléchargement](https://ubuntu.com/download/desktop). Ubuntu 20.04 LTS (la dernière version à long terme au moment de l'écriture) fait environ 2,67 Go. Une fois que vous avez fini de télécharger le fichier, retournez à Fedora Media Writer, cliquez sur "Custom Image", et sélectionnez le fichier ISO que vous venez de télécharger.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/fmw-ready-to-write.png)

Le bouton "Write to Disk" est grisé parce qu'il n'y a pas de clés USB connectées à l'ordinateur. Connectez votre clé USB et le bouton devrait devenir rouge vif.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/fmw-ready-to-write-with-usb-drive.png)

Vérifiez que la bonne clé USB est sélectionnée dans le menu déroulant et cliquez sur le bouton "Write to Disk". Selon le taux de transfert de votre machine, ce processus peut prendre quelques minutes. Une fois terminé, débranchez la clé USB et mettez-la de côté. Vous en aurez besoin bientôt.

## Comment préparer votre ordinateur pour installer Linux

Encore une fois, il n'est pas rare de trouver des personnes qui n'ont pas réussi à démarrer à partir d'une clé USB Linux. Cela peut arriver si vous n'avez pas configuré correctement votre ordinateur.

Pour ce faire, allez dans votre Panneau de configuration. Pas la nouvelle application Paramètres, mais le Panneau de configuration d'origine.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/control-panel-1.png)

Assurez-vous que le Panneau de configuration est soit en mode "Petites icônes" ou "Grandes icônes" et non en "Mode Catégorie". Allez ensuite dans "Options d'alimentation" et dans la barre latérale gauche, cliquez sur "Choisir le comportement des boutons d'alimentation".

![Image](https://www.freecodecamp.org/news/content/images/2021/12/turn-off-fast-startup.png)

Cliquez sur le lien "Modifier les paramètres actuellement non disponibles" et décochez l'option "Activer le démarrage rapide (recommandé)" et cliquez sur "Enregistrer les modifications".

Selon l'article de Walter Glenn [article](https://www.howtogeek.com/243901/the-pros-and-cons-of-windows-10s-fast-startup-mode/),

> Le démarrage rapide combine des éléments d'un arrêt à froid et de la fonction d'hibernation. Lorsque vous éteignez votre ordinateur avec le démarrage rapide activé, Windows ferme toutes les applications et déconnecte tous les utilisateurs, comme dans un arrêt à froid normal.
>
> À ce stade, Windows est dans un état très similaire à celui d'un démarrage frais : aucun utilisateur n'a ouvert de session et lancé de programmes, mais le noyau Windows est chargé et la session système est en cours d'exécution.
>
> Windows alerte ensuite les pilotes de périphériques qui le supportent pour se préparer à l'hibernation, sauvegarde l'état actuel du système dans le fichier d'hibernation et éteint l'ordinateur.
>
> Lorsque vous redémarrez l'ordinateur, Windows n'a pas besoin de recharger le noyau, les pilotes et l'état du système individuellement. Au lieu de cela, il rafraîchit simplement votre RAM avec l'image chargée à partir du fichier d'hibernation et vous amène à l'écran de connexion. Cette technique peut réduire considérablement le temps de démarrage.

Je sais que cela semble être une fonctionnalité agréable à avoir, mais le problème est que si vous gardez le démarrage rapide activé dans un système dual boot, Linux ne pourra pas utiliser les disques partagés entre les deux systèmes d'exploitation car ils sont hibernés et détenus par Windows.

Ensuite, démarrez dans l'écran de configuration UEFI de votre carte mère. Selon votre carte mère ou la marque de votre ordinateur portable, la touche peut changer, mais dans la plupart des cas, appuyer sur la touche "Del" devrait vous y amener.

Une fois que vous y êtes, vous devrez changer un paramètre en particulier :

* **Désactiver le démarrage sécurisé** – c'est l'une des fonctionnalités de l'UEFI qui aide à prévenir les attaques et les logiciels malveillants pendant le démarrage. Le désactiver n'est pas strictement nécessaire, mais selon la distribution que vous avez choisie, vous pouvez ou non rencontrer des problèmes pendant l'installation. Désactivez-le pour être sûr.

Enregistrez les paramètres mis à jour et redémarrez sous Windows. Il est maintenant temps de préparer de l'espace disque pour que Linux s'y installe.

## Comment créer des partitions supplémentaires pour installer Linux

Il est maintenant temps de faire de la place pour le nouveau système d'exploitation. Selon l'état de votre HDD ou SSD, cela peut être très simple ou assez compliqué.

Permettez-moi de vous expliquer ce que nous allons faire. Il existe un utilitaire intégré à Windows appelé "Gestion des disques" qui est utile lorsque vous voulez manipuler vos partitions.

Vous pouvez utiliser cela pour extraire de l'espace de vos partitions existantes. Pour ce faire, ouvrez la Gestion des disques en la recherchant dans le menu démarrer.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/disk-management-in-start-menu.png)

Gardez à l'esprit qu'elle peut apparaître sous le nom "Créer et formater des partitions de disque dur" au lieu de Gestion des disques. Lancez-la et examinez bien son interface utilisateur :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/disk-management.jpg)

Cette capture d'écran provient de l'une de mes machines qui n'a pas Linux installé. J'utiliserai cet appareil comme cobaye pour cet article. Il dispose d'un SSD NVME de 512 Go et de 8 Go de RAM.

L'interface utilisateur est divisée en deux parties. La partie supérieure est une liste de toutes vos partitions et la partie inférieure contient tous les disques physiques connectés à votre ordinateur listés verticalement.

La capture d'écran ci-dessous provient de ma station de travail de bureau qui dispose d'un SSD NVME de 250 Go et d'un HDD de 1 To. J'ai Windows et Linux installés sur le deuxième disque. Donc, si vous avez plusieurs disques sur votre machine également, je vous suggère d'installer le système d'exploitation sur le disque qui contient la partition EFI.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/disk-management-desktop.jpg)

Si vous regardez le début du Disque 1, cette partition FAT32 de 550 Mo est l'EFI. Sur votre machine, elle peut être beaucoup plus petite.

Revenons à notre appareil cobaye. Comme vous pouvez le voir sur la capture d'écran, la partition Windows (C:) fait presque 250 Go. Je vais en retirer 108 Go.

* 100 Go pour la racine
* 8 Go pour le swap

Dans Linux, le répertoire racine contient tous les autres répertoires et fichiers du système. Lorsque votre RAM est pleine, Linux déplace les pages inactives de la mémoire vers l'espace de swap. Avoir un espace de swap n'est pas obligatoire mais c'est bon à avoir.

Il n'y a pas de règle stricte pour déterminer l'espace de swap. La taille recommandée pour le swap lorsque vous avez une RAM de 4 Go à 8 Go est de 2 fois cette taille, et pour 8 Go à 16 Go, elle est de 1,5 fois cette taille. Considérant que je ne fais aucune tâche intensive en mémoire sur cet ordinateur portable, je vais enfreindre la règle ici.

Pour retirer de l'espace de votre partition souhaitée, faites un clic droit dessus depuis la partie inférieure et cliquez sur "Réduire". Une fois que vous avez fait cela, la Gestion des disques commencera à calculer la quantité disponible pour la réduction.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/querying-for-available-space.jpg)

Vous pourriez penser que tout l'espace libre d'une partition devrait être réductible, mais ce n'est pas vrai. Parfois, il y a des fichiers immobiles dispersés dans votre partition qui peuvent vous empêcher d'utiliser tout l'espace libre. Dans ces cas, utilisez un outil comme [Defraggler](https://www.ccleaner.com/defraggler) pour optimiser votre disque.

Une fois que la Gestion des disques a fini de calculer la partition, vous verrez la fenêtre suivante :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/shrink-window.jpg)

Comme vous pouvez le voir, j'ai 160311 Mo d'espace disponible pour la réduction. Diviser cette valeur par 1024 donne la taille en gigaoctets, ce qui dans mon cas est d'environ 156 Go.

Mais je veux réduire ma partition de 108 Go. Multiplier cette valeur par 1024 donne la valeur en mégaoctets de 110592 Mo.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/calculate-shrink-amount.jpg)

Une fois que vous avez calculé la taille souhaitée, cliquez sur le bouton "Réduire". Le processus de réduction ne prend pas si longtemps. Une fois le processus terminé, la partie inférieure de l'interface utilisateur sera mise à jour.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/disk-management-after-shrink.jpg)

Comme vous pouvez le voir, j'ai maintenant 108 Go d'espace non alloué. Pour être honnête, cela suffit pour passer à l'étape suivante. Mais pour vous faciliter la vie, je vous suggère de créer deux partitions RAW avant de continuer.

Pour ce faire, faites un clic droit sur l'espace non alloué et cliquez sur l'option "Nouveau volume simple". Une nouvelle fenêtre d'assistant apparaîtra. Appuyez sur le bouton "Suivant" et à l'étape suivante, l'assistant vous demandera la taille de la nouvelle partition :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/partition-creation-size.jpg)

Je veux créer la partition racine de 100 Go. Multiplier cette valeur par 1024 donne la valeur en mégaoctets qui est de 102400 Mo. Une fois que vous avez calculé la taille, cliquez sur "Suivant".

![Image](https://www.freecodecamp.org/news/content/images/2021/12/partition-creation-drive-letter.jpg)

À l'étape suivante, l'assistant vous demandera la lettre de lecteur. Choisissez "Ne pas attribuer de lettre de lecteur ou de chemin de lecteur" et cliquez sur "Suivant".

![Image](https://www.freecodecamp.org/news/content/images/2021/12/partition-creation-format.jpg)

À cette étape, sélectionnez l'option "Ne pas formater ce volume" et cliquez sur "Suivant". Enfin, cliquez sur Terminer à la dernière étape. Suivez le même processus pour créer votre partition de swap.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/disk-management-after-creating-partitions.jpg)

J'ai maintenant une partition RAW de 100 Go pour la racine Linux et une partition RAW de 8 Go pour le swap. Fermez l'outil de gestion des disques et prenez une autre tasse de café ou de thé ou au moins d'eau car nous allons plus loin dans le terrier du lapin.

## Comment installer Linux aux côtés de Windows

D'accord tout le monde, cela devient réel maintenant. Nous allons le faire. Mais d'abord, vous devrez déterminer quelle touche utiliser pour accéder à votre menu de démarrage.

Sur l'appareil que j'utilise, appuyer sur la touche F2 m'amène à l'écran de configuration UEFI. De là, appuyer sur F8 m'amène au menu de démarrage. Assurez-vous donc d'avoir fait des recherches pour votre appareil.

Certains tutoriels peuvent vous instruire de changer l'ordre de démarrage depuis l'écran de configuration UEFI, mais je ne recommande pas de faire cela. Le SSD ou HDD qui contient votre chargeur de démarrage doit toujours être en haut.

Maintenant, connectez le périphérique USB bootable que vous avez mis de côté dans la première section et redémarrez votre ordinateur dans le menu de démarrage. Depuis le menu de démarrage, sélectionnez le périphérique USB bootable et appuyez sur Entrée.

Le menu GNU GRUB apparaîtra. Choisissez le premier qui dit "Ubuntu". Attendez que la vérification de l'intégrité du fichier se termine ou vous pouvez simplement la sauter en appuyant sur "Ctrl + C" sur votre clavier.

Vous entendrez une belle sonnerie et avec cela, le majestueux installateur d'Ubuntu apparaîtra :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/ubuntu-installer-1.png)

Avant de cliquer sur le bouton "Continuer", je vous suggère de vous connecter à Internet. Si vous utilisez un câble Ethernet, vous devriez déjà être connecté. Mais si vous utilisez le sans fil, vérifiez le coin supérieur droit de votre écran pour l'icône WiFi :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/wifi.png)

Une fois connecté, cliquez sur le bouton "Continuer" de l'installateur :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/keyboard-layout.png)

Choisissez la bonne disposition de clavier pour vous et cliquez sur "Continuer".

![Image](https://www.freecodecamp.org/news/content/images/2021/12/updates-and-other-software.png)

L'"Installation normale" vous donnera un tas de logiciels et de jeux utiles dès le départ, tandis que l'"Installation minimale" ne vous donnera que l'essentiel.

Gardez l'option "Télécharger les mises à jour pendant l'installation d'Ubuntu" cochée. Cela téléchargera les fichiers de paquets mis à jour depuis Internet pendant l'installation.

La troisième option nécessite quelques explications. Supposons que vous utilisez un GPU NVIDIA. Lorsque Ubuntu détecte ce GPU, Ubuntu chargera les pilotes open-source pour les GPU NVIDIA connus sous le nom de "nouveau".

Si vous cochez l'option "Installer des logiciels tiers pour le matériel graphique et Wi-Fi et des formats multimédias supplémentaires", NVIDIA tentera d'installer les pilotes propriétaires fournis par NVIDIA lui-même. Il installera également des codecs pour les formats multimédias propriétaires tels que MPEG.

Cet appareil que j'utilise dispose d'un GPU AMD et utilise le pilote open-source "amdgpu". Je vais laisser cela décoché en considérant que je peux installer les codecs si nécessaire par moi-même. Faites ce que vous préférez et cliquez sur le bouton "Continuer".

![Image](https://www.freecodecamp.org/news/content/images/2021/12/installation-type.png)

D'accord, cette étape nécessite de l'attention. L'installateur d'Ubuntu est assez intelligent pour détecter si vous avez d'autres systèmes d'exploitation installés sur votre machine ou non. Si oui, l'installateur vous offrira l'option d'installer Ubuntu à côté d'eux. Ne choisissez pas cette option. Je répète, **ne choisissez pas cette option**.

Choisissez "Autre chose" et cliquez sur le bouton "Continuer".

![Image](https://www.freecodecamp.org/news/content/images/2021/12/partition-map.png)

Cette partie peut être un peu délicate. C'est pourquoi je vous ai instruit de créer la partition depuis Windows au lieu de laisser l'espace non alloué. Si vous l'aviez laissé non alloué, déterminer quelle partie du disque vous devriez utiliser serait devenu beaucoup plus difficile.

En haut, vous pouvez voir une ligne multicolore avec des légendes indiquant quelle couleur représente quelle partition. Trouvez les deux partitions que vous avez créées depuis Windows.

Sur ma machine, "nvme0n1p4" et "nvme0n1p5" sont celles-ci. Maintenant, dans la liste, trouvez celle que vous avez créée pour la racine (nvme0n1p4 dans mon cas) et double-cliquez dessus :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/edit-partition.png)

Choisissez "Ext4 journaling file system" dans le menu déroulant "Utiliser comme" et "/" comme menu déroulant "Point de montage". Selon [The Linux Information Project](http://www.linfo.org/mount_point.html) :

> Un point de montage est un répertoire (généralement vide) dans le système de fichiers actuellement accessible sur lequel un système de fichiers supplémentaire est monté (c'est-à-dire attaché logiquement).

Cliquez sur le bouton "OK". Ensuite, double-cliquez sur la partition que vous avez créée pour l'espace de swap :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/swap-partition.png)

Choisissez "swap area" dans le menu déroulant "Utiliser comme" et cliquez sur le bouton "OK". Il reste une partition à configurer. C'est la partition EFI. Faites défiler la liste et trouvez la partition FAT32.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/efi-partition.png)

Sur ma machine, "nvme0n1p1" est la partition EFI. Double-cliquez dessus :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/use-as-efi.png)

Assurez-vous que "EFI System Partition" est sélectionné dans le menu déroulant "Utiliser comme". C'est la partition qui contiendra votre chargeur de démarrage. Assurez-vous de ne pas formater cette partition. Cliquez sur le bouton "OK".

De plus, le point de montage par défaut pour la partition EFI est "/boot/efi". Certaines distributions comme Fedora vous obligeront à écrire ce point de montage manuellement. Assurez-vous donc de mettre le bon point de montage.

Vérifiez une fois de plus la configuration des partitions et si tout semble correct, cliquez sur le bouton "Installer maintenant".

![Image](https://www.freecodecamp.org/news/content/images/2021/12/where-are-you.png)

L'installateur vous demandera votre fuseau horaire. Je vis à Dhaka, au Bangladesh, c'est donc ce que j'ai choisi. Cliquez sur le bouton "Continuer".

![Image](https://www.freecodecamp.org/news/content/images/2021/12/who-are-you-1.png)

Remplissez toutes les informations comme vous le jugez approprié et cliquez sur le bouton "Continuer".

![Image](https://www.freecodecamp.org/news/content/images/2021/12/welcome-to-ubuntu.png)

Le processus d'installation ne devrait pas prendre longtemps. Quand j'étais enfant, j'adorais regarder ce diaporama.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/restart-now.png)

Une fois l'installation terminée, vous pouvez soit continuer à tester, soit redémarrer. Si vous choisissez de redémarrer, Ubuntu vous instruira de débrancher la clé USB et d'appuyer sur Entrée.

La machine redémarrera et le menu GRUB apparaîtra à nouveau. Jetez un coup d'œil à la liste, et vous verrez à la fois Ubuntu et Windows Boot Manager dans le menu. Démarrez dans Ubuntu car vous avez une dernière chose à faire.

## Comment synchroniser l'heure entre Windows et Linux

C'est l'un des problèmes courants auxquels sont confrontées les personnes avec un système dual boot. Lorsque vous démarrez dans Windows puis démarrez dans Linux, vous trouverez l'horloge de Linux complètement déréglée. La même chose se produira si vous démarrez d'abord dans Linux puis démarrez dans Windows.

Permettez-moi d'expliquer pourquoi cela se produit. Votre ordinateur (ou plutôt tous les ordinateurs du monde) a deux horloges. L'une est l'horloge système qui vit dans le système d'exploitation, et l'autre est l'horloge matérielle qui vit dans votre carte mère et suit l'heure même lorsque votre ordinateur ne fonctionne pas.

Le problème est que Windows suppose que votre horloge matérielle fonctionne à l'heure locale et Linux suppose que votre horloge matérielle fonctionne à l'heure UTC et applique un décalage selon votre emplacement.

La manière la plus simple de corriger ce problème est de faire en sorte que votre distribution Linux utilise l'heure locale comme le fait Windows. Pour ce faire, exécutez la commande suivante dans le terminal Linux :

```bash
timedatectl set-local-rtc 1 --adjust-system-clock
```

Maintenant, redémarrez votre ordinateur dans Windows, synchronisez l'horloge système et retournez à Linux. L'heure ne devrait plus être déréglée maintenant.

## Comment supprimer Linux d'un système dual boot

Disons que pour une raison quelconque, vous n'avez pas aimé votre temps avec Linux et vous voulez vous en débarrasser. Ce serait triste, mais la vie est dure, n'est-ce pas ?

Supprimer Linux d'un système dual boot est un processus en deux étapes :

1. Se débarrasser du chargeur de démarrage GRUB
2. Se débarrasser des partitions Linux

Pour vous débarrasser du chargeur de démarrage GRUB, vous devrez supprimer les fichiers correspondants de la partition EFI. Le problème est que la partition est masquée par défaut.

Pour la rendre accessible, vous devrez utiliser le programme `diskpart`. C'est un utilitaire de gestion de disque comme l'outil Gestion des disques mais c'est une interface en ligne de commande.

Démarrez dans Windows. Depuis le menu démarrer, ouvrez l'invite de commandes en tant qu'administrateur. Pour ce faire, recherchez simplement "cmd" dans votre menu démarrer et lorsque l'invite de commandes apparaît, appuyez sur la combinaison de touches "Ctrl + Maj + Entrée".

Maintenant, écrivez `diskpart` dans la fenêtre de l'invite de commandes et appuyez sur Entrée pour démarrer le programme.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/diskpart.jpg)

Ensuite, écrivez `list disk` et appuyez sur Entrée pour obtenir une liste de tous les disques connectés :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/list-disk.jpg)

Cet appareil n'a qu'un seul disque physique mais vous pouvez en avoir plusieurs. Écrivez `sel disk <numéro de disque>` pour sélectionner le disque souhaité.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/sel-disk-0.jpg)

Ensuite, écrivez `list vol` et appuyez sur Entrée pour lister toutes les partitions de ce disque.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/list-vol.jpg)

En jugeant par la taille et le format, je peux dire que le Volume 4 est la partition EFI. Gardez à l'esprit que cela peut être beaucoup plus petit sur votre système mais ce sera toujours une partition FAT32. Écrivez `sel vol <numéro de volume>` pour sélectionner le volume souhaité.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/sel-vol-4.jpg)

Enfin, écrivez `assign letter x` et appuyez sur Entrée pour attribuer la lettre `x` à cette partition.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/assign-letter-x.jpg)

Quittez `diskpart` en écrivant `exit` et en appuyant sur Entrée :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/exit.jpg)

Maintenant, la partition est devenue accessible. Depuis la même fenêtre d'invite de commandes, allez dans la partition EFI en écrivant `x:` et en appuyant sur Entrée.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/x.jpg)

Pour obtenir une liste de tous les dossiers qui s'y trouvent, écrivez `dir` et appuyez sur Entrée.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/dir.jpg)

Maintenant, écrivez `cd EFI` pour entrer dans ce dossier EFI et écrivez `dir` une fois de plus pour lister le contenu.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/cd-efi.jpg)

Vous devrez vous débarrasser de ce dossier `ubuntu`. Pour ce faire, écrivez `rmdir /s ubuntu` et appuyez sur Entrée. L'invite de commandes vous demandera si vous êtes sûr ou non. Écrivez `Y` et appuyez sur Entrée pour confirmer. Ensuite, utilisez `dir` une dernière fois pour vous assurer qu'il a disparu.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/rmdir-dir.jpg)

C'est tout. Ensuite, ouvrez à nouveau la Gestion des disques comme vous l'avez fait auparavant et depuis la partie inférieure, faites un clic droit sur les partitions orientées Linux et choisissez "Supprimer le volume" dans la liste.

Après avoir supprimé les partitions, vous pouvez soit en créer une nouvelle en utilisant l'espace non alloué, soit étendre la partition à gauche pour dissoudre l'espace non alloué.

Enfin, redémarrez votre ordinateur et vérifiez si Ubuntu a disparu de votre machine ou non.

## Et les autres distributions Linux ?

Les techniques apprises dans cet article sont pertinentes pour toutes les distributions Linux.

Donc, chaque fois que vous faites un dual boot d'un système, assurez-vous que

* Le démarrage sécurisé est désactivé
* Le démarrage rapide est désactivé

Et pendant l'installation

* Ne choisissez aucun type d'installation guidée/automatique
* Assurez-vous de ne pas formater la partition EFI/ESP
* Assurez-vous de monter vos partitions correctement

Tant que vous respectez ces quelques règles, vous devriez être bon pour continuer.

Gardez simplement à l'esprit qu'il existe quelques cas rares où une distribution peut ne pas utiliser GRUB comme chargeur de démarrage.

Prenez l'exemple de la très populaire "[Pop!_OS](https://pop.system76.com/)". Elle utilise "systemd-boot" comme chargeur de démarrage par défaut. En conséquence, vous devrez continuer à appuyer sur la touche Espace (ou peut-être n'importe quelle touche du clavier) pendant le démarrage, sinon le menu de démarrage ne s'affichera pas et vous démarrerez directement dans Pop!_OS.

Une autre chose que j'ai vue : certaines cartes mères comme ma MSI B450 Tomahawk Max choisissent le Windows Boot Manager par défaut même si j'ai une installation Linux fonctionnelle. Si vous voyez quelque chose comme cela, allez dans l'écran de configuration UEFI et cherchez les options pertinentes.

## Conclusion

Je tiens à vous remercier du fond du cœur pour le temps que vous avez passé à lire cet article.

J'ai également un blog personnel où j'écris sur des trucs tech aléatoires, donc si vous êtes intéressé par quelque chose comme ça, consultez [https://farhan.dev](https://farhan.dev). Si vous avez des questions ou si vous êtes confus à propos de quelque chose – ou si vous voulez simplement entrer en contact – je suis disponible sur [Twitter](https://twitter.com/frhnhsin) et [LinkedIn](https://www.linkedin.com/in/farhanhasin/).