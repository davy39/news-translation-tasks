---
title: Qu'est-ce qu'un système de fichiers ? Types de systèmes de fichiers informatiques
  et fonctionnement – Explications avec exemples
date: '2022-01-11T16:49:00.000Z'
authorURL: ''
originalURL: https://freecodecamp.org/news/file-systems-architecture-explained
posteditor: ''
proofreader: ''
author: freeCodeCamp
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/pexels-photo-6571015.jpeg
tags:
- name: Computer Science
  slug: computer-science
- name: software architecture
  slug: software-architecture
- name: storage
  slug: storage
seo_desc: 'By Reza Lavarian

  It''s a bit tricky to explain what exactly a file system is in just one sentence.

  That''s why I decided to write an article about it. This post is meant to be a high-level
  overview of file systems. But I''ll sneak into the lower-level c...'
---


Par Reza Lavarian

<!-- more -->

Il est un peu délicat d'expliquer exactement ce qu'est un système de fichiers en une seule phrase.

C'est pourquoi j'ai décidé d'écrire un article à ce sujet. Ce post se veut un aperçu de haut niveau des systèmes de fichiers. Mais je me glisserai également dans des concepts de plus bas niveau, tant que cela ne devient pas ennuyeux. :)

## Qu'est-ce qu'un système de fichiers ?

Commençons par une définition simple :

Un **système de fichiers** définit la manière dont les fichiers sont **nommés**, **stockés** et **récupérés** à partir d'un périphérique de stockage.

Chaque fois que vous ouvrez un fichier sur votre ordinateur ou votre appareil intelligent, votre système d'exploitation utilise son système de fichiers en interne pour le charger depuis le périphérique de stockage.

Ou lorsque vous copiez, modifiez ou supprimez un fichier, le système de fichiers gère cela sous le capot.

Chaque fois que vous téléchargez un fichier ou accédez à une page web sur Internet, un système de fichiers est également impliqué.

Par exemple, si vous accédez à une page sur [freeCodeCamp][1], votre navigateur envoie une requête [HTTP][2] au serveur de freeCodeCamp pour récupérer la page. Si la ressource demandée est un fichier, elle est récupérée à partir d'un système de fichiers.

Lorsque les gens parlent de systèmes de fichiers, ils peuvent se référer à différents aspects d'un système de fichiers selon le contexte – c'est là que les choses commencent à paraître complexes.

Et vous pourriez finir par vous demander : QU'EST-CE QU'UN SYSTÈME DE FICHIERS AU JUSTE ? 🤯

Ce guide vous aide à comprendre les systèmes de fichiers dans de nombreux contextes. Je couvrirai également le partitionnement et le démarrage !

Pour que ce guide reste gérable, je me concentrerai sur les environnements de type Unix lors de l'explication des concepts de bas niveau ou des commandes de console.

Cependant, ces concepts restent pertinents pour d'autres environnements et systèmes de fichiers.

### Pourquoi avons-nous besoin d'un système de fichiers en premier lieu, me demanderez-vous ?

Eh bien, sans système de fichiers, le périphérique de stockage contiendrait un énorme bloc de données stockées les unes après les autres, et le système d'exploitation ne serait pas capable de les distinguer.

Le terme système de fichiers tire son nom des anciens systèmes de gestion de données sur papier, où nous conservions les documents sous forme de fichiers et les placions dans des répertoires.

Imaginez une pièce avec des piles de papiers éparpillées partout.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/pexels-photo-6571015-1.jpg)

Un périphérique de stockage sans système de fichiers serait dans la même situation – et ce serait un appareil électronique inutile.

Cependant, un système de fichiers change tout :

![Image](https://www.freecodecamp.org/news/content/images/2021/02/pexels-photo-6571015-2.jpg)

Un système de fichiers n'est pas seulement une fonction de tenue de registres.

La gestion de l'espace, les métadonnées, le chiffrement des données, le contrôle d'accès aux fichiers et l'intégrité des données relèvent également de la responsabilité du système de fichiers.

## Tout commence par le partitionnement

Les périphériques de stockage doivent être **partitionnés** et **formatés** avant la première utilisation.

Mais qu'est-ce que le partitionnement ?

Le partitionnement consiste à diviser un périphérique de stockage en plusieurs _régions logiques_, afin qu'elles puissent être gérées séparément comme s'il s'agissait de périphériques de stockage distincts.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/partitions.jpg)

Nous effectuons généralement le partitionnement via un outil de gestion de disque fourni par les systèmes d'exploitation, ou via un outil en ligne de commande fourni par le firmware du système (j'expliquerai ce qu'est le firmware).

Un périphérique de stockage doit avoir au moins une partition, ou plus si nécessaire.

Pourquoi devrions-nous diviser les périphériques de stockage en plusieurs partitions ?

La raison est que nous ne voulons pas gérer l'ensemble de l'espace de stockage comme une seule unité et pour un seul usage.

C'est exactement comme la façon dont nous partitionnons notre espace de travail pour séparer (et isoler) les salles de réunion, les salles de conférence et les différentes équipes.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/office-space.jpeg)

Par exemple, une installation Linux de base comporte trois partitions : une partition dédiée au système d'exploitation, une pour les fichiers des utilisateurs et une partition de swap optionnelle.

Une partition de swap fonctionne comme une extension de la RAM lorsque celle-ci manque d'espace.

Par exemple, l'OS peut déplacer un bloc de données (temporairement) de la RAM vers la partition de swap pour libérer de l'espace sur la RAM.

Les systèmes d'exploitation utilisent continuellement diverses techniques de [gestion de la mémoire][3] pour s'assurer que chaque processus dispose de suffisamment d'espace mémoire pour s'exécuter.

Les systèmes de fichiers sur Windows et Mac ont une disposition similaire, mais ils n'utilisent pas de partition de swap dédiée ; à la place, ils gèrent le swap à l'intérieur de la partition sur laquelle vous avez installé votre système d'exploitation.

Sur un ordinateur avec plusieurs partitions, vous pouvez installer plusieurs systèmes d'exploitation et choisir à chaque fois un système d'exploitation différent pour démarrer votre système.

Les utilitaires de récupération et de diagnostic résident également dans des partitions dédiées.

Par exemple, pour démarrer un MacBook en mode récupération, vous devez maintenir `Command + R` dès que vous redémarrez (ou allumez) votre MacBook. Ce faisant, vous demandez au firmware du système de démarrer sur une partition qui contient le programme de récupération.

Le partitionnement n'est pas seulement un moyen d'installer plusieurs systèmes d'exploitation et outils ; il nous aide également à séparer les fichiers système critiques des fichiers ordinaires.

Ainsi, quel que soit le nombre de jeux que vous installez sur votre ordinateur, cela n'aura aucun effet sur les performances du système d'exploitation, car ils résident dans des partitions différentes.

Pour en revenir à l'exemple du bureau, avoir un centre d'appels et une équipe technique dans une zone commune nuirait à la productivité des deux équipes car chaque équipe a ses propres exigences pour être efficace.

Par exemple, l'équipe technique apprécierait une zone plus calme.

Certains systèmes d'exploitation, comme Windows, attribuent une lettre de lecteur (A, B, C ou D) aux partitions. Par exemple, la _partition primaire_ sur Windows (sur laquelle Windows est installé) est connue sous le nom de **C:**, ou **lecteur C**.

Dans les systèmes d'exploitation de type Unix, cependant, les partitions apparaissent comme des répertoires ordinaires sous le répertoire racine – nous verrons cela plus tard.

Dans la section suivante, nous plongerons plus profondément dans le partitionnement et ferons connaissance avec deux concepts qui changeront votre perspective sur les systèmes de fichiers : le **firmware système** et le **démarrage (booting)**.

Êtes-vous prêt ?

C'est parti ! 🏊‍♂️

## Schémas de partitionnement, firmware système et démarrage

Lors du partitionnement d'un périphérique de stockage, nous avons le choix entre deux méthodes (ou schémas 🙄) de partitionnement :

-   **Schéma Master Boot Record (MBR)**
-   **Schéma GUID Partition Table (GPT)**

Quel que soit le schéma de partitionnement que vous choisissez, les premiers blocs du périphérique de stockage contiendront toujours des données critiques sur vos partitions.

Le _firmware_ du système utilise ces structures de données pour démarrer le système d'exploitation sur une partition.

Attendez, qu'est-ce que le firmware système ? me demanderez-vous.

Voici une explication :

Un firmware est un logiciel de bas niveau intégré dans les appareils électroniques pour faire fonctionner l'appareil, ou pour amorcer (bootstrap) un autre programme pour le faire.

Le firmware existe dans les ordinateurs, les périphériques (claviers, souris et imprimantes), ou même les appareils ménagers électroniques.

Dans les ordinateurs, le firmware fournit une interface standard pour que des logiciels complexes comme un système d'exploitation puissent démarrer et fonctionner avec les composants matériels.

Cependant, sur des systèmes plus simples comme une imprimante, le firmware est le système d'exploitation. Le menu que vous utilisez sur votre imprimante est l'interface de son firmware.

Les fabricants de matériel créent des firmwares basés sur deux spécifications :

-   **Basic Input/Output System (BIOS)**
-   **Unified Extensible Firmware Interface (UEFI)**

Les firmwares – qu'ils soient basés sur le BIOS ou l'UEFI – résident sur une _mémoire non volatile_, comme une ROM flash fixée à la carte mère.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/5794340306_caef1e6960_b.jpg) _\[CC BY 2.0\](https://www.flickr.com/photos/computerhotline/5794340306">**BIOS** Par [Thomas Bresson][4], sous licence **<a href="https://creativecommons.org/licenses/by/2.0/)**_

Lorsque vous appuyez sur le bouton d'alimentation de votre ordinateur, le firmware est le premier programme à s'exécuter.

La mission du firmware (entre autres) est de démarrer l'ordinateur, de lancer le système d'exploitation et de lui passer le contrôle de l'ensemble du système.

Un firmware exécute également des environnements pré-OS (avec support réseau), comme des outils de récupération ou de diagnostic, ou même un shell pour exécuter des commandes textuelles.

Les premiers écrans que vous voyez avant l'apparition du logo Windows sont la sortie du firmware de votre ordinateur, vérifiant la santé des composants matériels et de la mémoire.

La vérification initiale est confirmée par un bip (généralement sur les PC), indiquant que tout est prêt.

## Partitionnement MBR et firmware basé sur le BIOS

Le schéma de partitionnement MBR fait partie des spécifications du BIOS et est utilisé par les firmwares basés sur le BIOS.

Sur les disques partitionnés en MBR, le premier secteur du périphérique de stockage contient des données essentielles pour démarrer le système.

Ce secteur est appelé MBR.

Le MBR contient les informations suivantes :

-   Le bootloader, qui est un **programme simple** (en code machine) pour initier la première étape du processus de démarrage.
-   Une **table de partition**, qui contient des informations sur vos partitions.

Le firmware basé sur le BIOS démarre le système différemment du firmware basé sur l'UEFI.

Voici comment cela fonctionne :

Une fois le système sous tension, le firmware BIOS démarre et charge le programme bootloader (contenu dans le MBR) en mémoire. Une fois le programme en mémoire, le CPU commence à l'exécuter.

Le fait d'avoir le bootloader et la table de partition dans un emplacement prédéfini comme le MBR permet au BIOS de démarrer le système sans avoir à traiter de fichiers.

Si vous êtes curieux de savoir comment le CPU exécute les instructions résidant dans la mémoire, vous pouvez lire ce [guide sur le fonctionnement du CPU][5], amusant et accessible aux débutants.

Le code du bootloader dans le MBR occupe entre 434 octets et 446 octets de l'espace MBR (sur 512 octets). De plus, 64 octets sont alloués à la table de partition, qui peut contenir des informations sur un maximum de quatre partitions.

446 octets ne suffisent pas pour loger beaucoup de code. Cela dit, des bootloaders sophistiqués comme _GRUB 2_ sur Linux divisent leur fonctionnalité en morceaux ou étapes (stages).

Le plus petit morceau de code, connu sous le nom de _bootloader de première étape_ (stage 1), est stocké dans le MBR. C'est généralement un programme simple qui ne nécessite pas beaucoup d'espace.

La responsabilité du bootloader de première étape est d'initier les étapes suivantes (et plus compliquées) du processus de démarrage.

Immédiatement après le MBR, et avant le début de la première partition, il y a un petit espace d'environ 1 Mo, appelé l'**espace vide MBR (MBR gap)**.

L'espace vide MBR peut être utilisé pour placer un autre morceau du programme bootloader si nécessaire.

Un bootloader, tel que GRUB 2, utilise l'espace vide MBR pour stocker une autre étape de sa fonctionnalité. GRUB appelle cela le bootloader _stage 1.5_, qui contient un pilote de système de fichiers.

Le stage 1.5 permet aux étapes suivantes de GRUB de comprendre le concept de fichiers, plutôt que de charger des instructions brutes depuis le périphérique de stockage (comme le fait le bootloader de première étape).

Le bootloader de deuxième étape, qui est maintenant capable de travailler avec des fichiers, peut charger le fichier bootloader du système d'exploitation pour démarrer le système d'exploitation respectif.

C'est à ce moment que le logo du système d'exploitation apparaît en fondu...

Voici la disposition d'un périphérique de stockage partitionné en MBR :

![Image](https://www.freecodecamp.org/news/content/images/2021/02/mbr-partition.jpg)

Et si nous magnifions le MBR, son contenu ressemblerait à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/02/mbr.jpg)

Bien que le MBR soit simple et largement supporté, il présente certaines limitations 😑.

La structure de données du MBR limite le nombre de partitions à seulement _quatre partitions primaires_.

Une solution courante consiste à créer une partition _étendue_ à côté des partitions primaires, tant que le nombre total de partitions ne dépasse pas quatre.

Une partition étendue peut être divisée en plusieurs _partitions logiques_. La création de partitions étendues diffère selon les systèmes d'exploitation. Dans ce guide rapide, [Microsoft explique comment cela doit être fait sur Windows][6].

Lors de la création d'une partition, vous pouvez choisir entre primaire et étendue.

Une fois cela résolu, nous rencontrons la deuxième limitation.

Chaque partition peut faire un maximum de **2 TiB** 🙄.

Et attendez, il y a plus !

Le contenu du secteur MBR n'a pas de sauvegarde 😱, ce qui signifie que si le MBR est corrompu pour une raison inattendue, nous devrons trouver un moyen de recycler ce morceau de matériel inutile.

C'est là que le partitionnement GPT se démarque 😎.

## Partitionnement GPT et firmware basé sur l'UEFI

Le schéma de partitionnement **GPT** est plus sophistiqué que le MBR et n'a pas ses limitations.

Par exemple, vous pouvez avoir autant de partitions que votre système d'exploitation le permet.

Et chaque partition peut avoir la taille du plus grand périphérique de stockage disponible sur le marché – en fait, beaucoup plus.

Le GPT remplace progressivement le MBR, bien que le MBR soit toujours largement supporté sur les anciens PC comme sur les nouveaux.

Comme mentionné précédemment, le GPT fait partie de la spécification UEFI, qui remplace le bon vieux BIOS.

Cela signifie que le firmware basé sur l'UEFI utilise un périphérique de stockage partitionné en GPT pour gérer le processus de démarrage.

De nombreux matériels et systèmes d'exploitation supportent désormais l'UEFI et utilisent le schéma GPT pour partitionner les périphériques de stockage.

Dans le schéma de partitionnement GPT, le premier secteur du périphérique de stockage est réservé pour des raisons de compatibilité avec les systèmes basés sur le BIOS. La raison est que certains systèmes peuvent encore utiliser un firmware basé sur le BIOS mais avoir un périphérique de stockage partitionné en GPT.

Ce secteur est appelé **Protective MBR.** (C'est là que résiderait le bootloader de première étape dans un disque partitionné en MBR).

Après ce premier secteur, les structures de données GPT sont stockées, y compris l'**en-tête GPT (GPT header)** et les **entrées de partition**.

Les entrées GPT et l'en-tête GPT sont sauvegardés à la fin du périphérique de stockage, afin de pouvoir être récupérés si la copie primaire est corrompue.

Cette sauvegarde est appelée **Secondary GPT.**

La disposition d'un périphérique de stockage partitionné en GPT ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/02/GUID_Partition_Table_Scheme.svg) \_**\[CC BY-SA 2.5\](https://commons.wikimedia.org/wiki/File:GUID\_Partition\_Table\_Scheme.svg">GUID Partition Table Scheme** Par [Kbolino][7], sous licence **<a href="https://creativecommons.org/licenses/by-sa/2.5/)**\_

Dans le GPT, tous les services de démarrage (bootloaders, gestionnaires de démarrage, environnements pré-OS et shells) vivent dans une partition dédiée appelée **EFI System Partition (ESP)**, que le firmware UEFI peut utiliser.

L'ESP possède même son propre système de fichiers, qui est une version spécifique de **FAT**. Sur Linux, l'ESP réside sous le chemin `/sys/firmware/efi`.

Si ce chemin est introuvable sur votre système, votre firmware est probablement basé sur le BIOS.

Pour vérifier, vous pouvez essayer de changer de répertoire vers le point de montage ESP, comme ceci :

```
cd /sys/firmware/efi
```

Le firmware basé sur l'UEFI suppose que le périphérique de stockage est partitionné avec GPT et recherche l'ESP dans la table de partition GPT.

Une fois la partition EFI trouvée, il recherche le bootloader configuré – généralement un fichier se terminant par `.efi`.

Le firmware basé sur l'UEFI obtient la configuration de démarrage à partir de la **NVRAM** (une RAM non volatile).

La NVRAM contient les paramètres de démarrage et les chemins vers les fichiers bootloader du système d'exploitation.

Le firmware UEFI peut également effectuer un démarrage de style BIOS (pour démarrer le système à partir d'un disque MBR) s'il est configuré en conséquence.

Vous pouvez utiliser la commande `parted` sur Linux pour voir quel schéma de partitionnement est utilisé pour un périphérique de stockage.

```
sudo parted -l
```

Et la sortie ressemblerait à ceci :

```
Model: Virtio Block Device (virtblk)
Disk /dev/vda: 172GB
Sector size (logical/physical): 512B/512B
Partition Table: gpt
Disk Flags: 

Number  Start   End     Size    File system  Name  Flags
14      1049kB  5243kB  4194kB                     bios_grub
15      5243kB  116MB   111MB   fat32              msftdata
 1      116MB   172GB   172GB   ext4
```

D'après la sortie ci-dessus, l'ID du périphérique de stockage est `/dev/vda` avec une capacité de 172 Go. Le périphérique de stockage est partitionné sur la base du GPT et possède trois partitions ; les deuxième et troisième partitions sont formatées sur la base des systèmes de fichiers FAT32 et EXT4 respectivement.

La présence d'une partition BIOS GRUB implique que le firmware est toujours basé sur le BIOS.

Confirmons cela avec la commande `dmidecode` comme ceci :

```
sudo dmidecode -t 0
```

Et la sortie serait :

```
# dmidecode 3.2
Getting SMBIOS data from sysfs.
SMBIOS 2.4 present.

...
```

✅ Confirmé !

## Formatage des partitions

Une fois le partitionnement terminé, les partitions doivent être **formatées**.

La plupart des systèmes d'exploitation vous permettent de formater une partition sur la base d'un ensemble de systèmes de fichiers.

Par exemple, si vous formatez une partition sur Windows, vous pouvez choisir entre les systèmes de fichiers **FAT32**, **NTFS** et **exFAT**.

Le formatage implique la création de diverses **structures de données** et métadonnées utilisées pour gérer les fichiers au sein d'une partition.

Ces structures de données sont l'un des aspects d'un système de fichiers.

Prenons le système de fichiers NTFS comme exemple.

Lorsque vous formatez une partition en NTFS, le processus de formatage place les structures de données clés de NTFS et la **Master file table (MFT)** sur la partition.

Très bien, revenons aux systèmes de fichiers avec nos nouvelles connaissances sur le partitionnement, le formatage et le démarrage.

## Comment ça a commencé, où nous en sommes

Un système de fichiers est un ensemble de structures de données, d'interfaces, d'abstractions et d'API qui travaillent ensemble pour gérer tout type de fichier sur tout type de périphérique de stockage, de manière cohérente.

Chaque système d'exploitation utilise un système de fichiers particulier pour gérer les fichiers.

À ses débuts, Microsoft utilisait **FAT** (FAT12, FAT16 et FAT32) dans les familles **MS-DOS** et **Windows 9x**.

À partir de Windows **NT 3.1**, Microsoft a développé le **New Technology File System (NTFS)**, qui présentait de nombreux avantages par rapport au FAT32, tels que le support de fichiers plus volumineux, l'autorisation de noms de fichiers plus longs, le chiffrement des données, la gestion des accès, la journalisation, et bien plus encore.

NTFS est le système de fichiers par défaut de la famille Windows NT (2000, XP, Vista, 7, 10, etc.) depuis lors.

Cependant, le NTFS n'est pas adapté aux environnements non-Windows 🤷🏻.

Par exemple, vous pouvez **seulement lire** le contenu d'un périphérique de stockage formaté en NTFS (comme une mémoire flash) sur un Mac OS, mais vous ne pourrez rien y écrire – à moins d'installer un [pilote NTFS avec support d'écriture][8].

Ou vous pouvez simplement utiliser le système de fichiers **exFat**.

L'**Extended File Allocation Table (exFAT)** est une version plus légère de NTFS créée par Microsoft en 2006.

exFAT a été conçu pour les périphériques amovibles de haute capacité, tels que les disques durs externes, les clés USB et les cartes mémoire.

exFAT est le système de fichiers par défaut utilisé par les cartes **SDXC**.

Contrairement au NTFS, l'exFAT dispose également d'un support en **lecture et écriture** sur les environnements non-Windows, y compris Mac OS — ce qui en fait le meilleur système de fichiers multiplateforme pour les périphériques de stockage amovibles de haute capacité.

Donc, fondamentalement, si vous avez un disque amovible que vous souhaitez utiliser sur Windows, Mac et Linux, vous devez le formater en exFAT.

Apple a également développé et utilisé divers systèmes de fichiers au fil des ans, notamment  
**Hierarchical File System (HFS)**, **HFS+**, et récemment **Apple File System (APFS)**.

Tout comme le NTFS, l'APFS est un système de fichiers à journalisation et est utilisé depuis le lancement d'**OS X High Sierra** en 2017.

Mais qu'en est-il des systèmes de fichiers dans les distributions Linux ?

La famille de systèmes de fichiers **Extended File System (ext)** a été créée pour le noyau Linux – le cœur du système d'exploitation Linux.

La première version d'**ext** a été publiée en 1991, mais peu de temps après, elle a été remplacée par le **second extended file system** (**ext2**) en 1993.

Dans les années 2000, le **third extended filesystem** (**ext3**) et le **fourth extended filesystem (ext4)** ont été développés pour Linux avec une capacité de journalisation.

**ext4** est désormais le système de fichiers par défaut dans de nombreuses distributions Linux, notamment [Debian][9] et [Ubuntu][10].

Vous pouvez utiliser la commande `findmnt` sur Linux pour lister vos partitions formatées en ext4 :

```
findmnt -lo source,target,fstype,used -t ext4
```

La sortie ressemblerait à :

```
SOURCE    TARGET FSTYPE  USED
/dev/vda1 /      ext4    3.6G
```

## Architecture des systèmes de fichiers

Un système de fichiers installé sur un système d'exploitation se compose de trois couches :

-   **Système de fichiers physique**
-   **Système de fichiers virtuel**
-   **Système de fichiers logique**

Ces couches peuvent être implémentées comme des abstractions indépendantes ou étroitement couplées.

Lorsque les gens parlent de systèmes de fichiers, ils se réfèrent à l'une de ces couches ou aux trois comme une seule unité.

Bien que ces couches soient différentes selon les systèmes d'exploitation, le concept est le même.

La couche physique est l'implémentation concrète d'un système de fichiers ; elle est responsable du stockage et de la récupération des données ainsi que de la gestion de l'espace sur le périphérique de stockage (ou plus précisément : les partitions).

Le système de fichiers physique interagit avec le matériel de stockage via des [pilotes de périphériques (device drivers)][11].

La couche suivante est le système de fichiers virtuel ou **VFS**.

Le système de fichiers virtuel offre une **vue cohérente** des divers systèmes de fichiers montés sur le même système d'exploitation.

Cela signifie-t-il qu'un système d'exploitation peut utiliser plusieurs systèmes de fichiers en même temps ?

La réponse est oui !

Il est courant qu'un support de stockage amovible ait un système de fichiers différent de celui d'un ordinateur.

Par exemple, sur Windows (qui utilise NTFS comme système de fichiers principal), une mémoire flash peut avoir été formatée en exFAT ou FAT32.

Cela dit, le système d'exploitation doit fournir une **interface unifiée** entre les programmes informatiques (explorateurs de fichiers et autres applications travaillant avec des fichiers) et les différents systèmes de fichiers montés (tels que NTFS, APFS, ext4, FAT32, exFAT et UDF).

Par exemple, lorsque vous ouvrez votre programme d'explorateur de fichiers, vous pouvez copier une image d'un système de fichiers ext4 et la coller sur votre mémoire flash formatée en exFAT – sans avoir à savoir que les fichiers sont gérés différemment sous le capot.

Cette couche pratique entre l'utilisateur (vous) et les systèmes de fichiers sous-jacents est fournie par le VFS.

Un VFS définit un _contrat_ que tous les systèmes de fichiers physiques doivent implémenter pour être supportés par ce système d'exploitation.

Cependant, cette conformité n'est pas intégrée au cœur du système de fichiers, ce qui signifie que le code source d'un système de fichiers n'inclut pas le support pour le VFS de chaque système d'exploitation.

Au lieu de cela, il utilise un **pilote de système de fichiers** pour adhérer aux règles VFS de chaque système de fichiers. Un pilote est un programme qui permet à un logiciel de communiquer avec un autre logiciel ou matériel.

Bien que le VFS soit responsable de fournir une interface standard entre les programmes et les divers systèmes de fichiers, les programmes informatiques n'interagissent pas directement avec le VFS.

Au lieu de cela, ils utilisent une API unifiée entre les programmes et le VFS.

Pouvez-vous deviner ce que c'est ?

Oui, nous parlons du **système de fichiers logique**.

Le système de fichiers logique est la partie du système de fichiers orientée vers l'utilisateur, qui fournit une API pour permettre aux programmes utilisateurs d'effectuer diverses opérations sur les fichiers, telles que `OPEN`, `READ` et `WRITE`, sans avoir à traiter avec le matériel de stockage.

D'autre part, le VFS fournit un pont entre la couche logique (avec laquelle les programmes interagissent) et un ensemble de la couche physique de divers systèmes de fichiers.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/filesystem-1.jpg) _Une architecture de haut niveau des couches du système de fichiers_

### Que signifie monter un système de fichiers ?

Sur les systèmes de type Unix, le VFS attribue un **ID de périphérique** (par exemple, `dev/disk1s1`) à chaque partition ou périphérique de stockage amovible.

Ensuite, il crée une **arborescence de répertoires virtuelle** et place le contenu de chaque périphérique sous cette arborescence sous forme de répertoires séparés.

L'acte d'attribuer un répertoire à un périphérique de stockage (sous l'arborescence du répertoire racine) est appelé **montage**, et le répertoire attribué est appelé un **point de montage**.

Cela dit, sur un système d'exploitation de type Unix, toutes les partitions et les périphériques de stockage amovibles apparaissent comme s'ils étaient des répertoires sous le répertoire racine.

Par exemple, sur Linux, les points de montage pour un périphérique amovible (comme une carte mémoire) se trouvent généralement sous le répertoire `/media`.

Ainsi, une fois qu'une mémoire flash est attachée au système, et par conséquent _auto-montée_ au point de montage par défaut (`/media` dans ce cas), son contenu sera disponible sous le répertoire `/media`.

Cependant, il arrive que vous deviez monter un système de fichiers manuellement.

Sur Linux, cela se fait comme ceci :

```
mount /dev/disk1s1 /media/usb
```

Dans la commande ci-dessus, le premier paramètre est l'ID du périphérique (`/dev/disk1s1`), et le second paramètre (`/media/usb`) est le point de montage.

Veuillez noter que le point de montage doit déjà exister en tant que répertoire.

Si ce n'est pas le cas, il doit d'abord être créé :

```
mkdir -p /media/usb
mount /dev/disk1s1 /media/usb
```

Si le répertoire du point de montage contient déjà des fichiers, ces fichiers seront masqués tant que le périphérique est monté.

## Métadonnées des fichiers

La métadonnée d'un fichier est une structure de données qui contient des **données sur un fichier**, telles que :

-   La taille du fichier
-   Les horodatages, comme la date de création, la date du dernier accès et la date de modification
-   Le propriétaire du fichier
-   Le mode du fichier (qui peut faire quoi avec le fichier)
-   Quels blocs sur la partition sont alloués au fichier
-   et bien plus encore

Cependant, les métadonnées ne sont pas stockées avec le contenu du fichier. Au lieu de cela, elles sont stockées à un endroit différent sur le disque – mais associées au fichier.

Dans les systèmes de type Unix, les métadonnées prennent la forme de structures de données appelées **inode**.

Les inodes sont identifiés par un numéro unique appelé le _numéro d'inode._

Les inodes sont associés aux fichiers dans une table appelée _tables d'inodes_.

Chaque fichier sur le périphérique de stockage possède un inode, qui contient des informations à son sujet telles que l'heure à laquelle il a été créé, modifié, etc.

L'inode comprend également l'adresse des blocs alloués au fichier ; en d'autres termes, où il se trouve exactement sur le périphérique de stockage.

Dans un inode ext4, l'adresse des blocs alloués est stockée sous la forme d'un ensemble de structures de données appelées **extents** (à l'intérieur de l'inode).

Chaque extent contient l'adresse du _premier bloc de données_ alloué au fichier et le nombre de _blocs continus_ que le fichier a occupés.

Chaque fois que vous ouvrez un fichier sur Linux, son nom est d'abord résolu en un numéro d'inode.

Ayant le numéro d'inode, le système de fichiers récupère l'inode respectif dans la table d'inodes.

Une fois l'inode récupéré, le système de fichiers commence à composer le fichier à partir des blocs de données enregistrés dans l'inode.

Vous pouvez utiliser la commande `df` avec le paramètre `-i` sur Linux pour voir les inodes (totaux, utilisés et libres) dans vos partitions :

```
df -i
```

La sortie ressemblerait à ceci :

```
udev           4116100    378 4115722    1% /dev
tmpfs          4118422    528 4117894    1% /run
/dev/vda1      6451200 175101 6276099    3% /
```

Comme vous pouvez le voir, la partition `/dev/vda1` possède un nombre total de 6 451 200 inodes, dont 3 % ont été utilisés (175 101 inodes).

Pour voir les inodes associés aux fichiers dans un répertoire, vous pouvez utiliser la commande `ls` avec les paramètres `-il`.

```
ls -li
```

Et la sortie serait :

```
1303834 -rw-r--r--  1 root www-data  2502 Jul  8  2019 wp-links-opml.php
1303835 -rw-r--r--  1 root www-data  3306 Jul  8  2019 wp-load.php
1303836 -rw-r--r--  1 root www-data 39551 Jul  8  2019 wp-login.php
1303837 -rw-r--r--  1 root www-data  8403 Jul  8  2019 wp-mail.php
1303838 -rw-r--r--  1 root www-data 18962 Jul  8  2019 wp-settings.php
```

La première colonne est le numéro d'inode associé à chaque fichier.

Le nombre d'inodes sur une partition est décidé lors du formatage de la partition. Cela dit, tant que vous avez de l'espace libre et des inodes inutilisés, vous pouvez stocker des fichiers sur votre périphérique de stockage.

Il est peu probable qu'un OS Linux personnel manque d'inodes. Cependant, les services d'entreprise qui traitent un grand nombre de fichiers (comme les serveurs de messagerie) doivent gérer leur quota d'inodes intelligemment.

Sur NTFS, cependant, les métadonnées sont stockées différemment.

NTFS conserve les informations sur les fichiers dans une structure de données appelée la [**Master File Table (MFT)**][12].

Chaque fichier possède au moins une entrée dans la MFT, qui contient tout à son sujet, y compris son emplacement sur le périphérique de stockage – similaire à la table des inodes.

Sur la plupart des systèmes d'exploitation, vous pouvez consulter les métadonnées via l'interface utilisateur graphique.

Par exemple, lorsque vous faites un clic droit sur un fichier sur Mac OS et sélectionnez **Lire les informations** (Propriétés sous Windows), une fenêtre apparaît avec des informations sur le fichier. Ces informations sont récupérées à partir des métadonnées du fichier respectif.

## Gestion de l'espace

Les périphériques de stockage sont divisés en blocs de taille fixe appelés **secteurs**.

Un secteur est l'**unité de stockage minimale** sur un périphérique de stockage et mesure entre 512 octets et 4096 octets (Advanced Format).

Cependant, les systèmes de fichiers utilisent un concept de plus haut niveau comme unité de stockage, appelé **blocs.**

Les blocs sont une abstraction des secteurs physiques ; chaque bloc se compose généralement de plusieurs secteurs.

Selon la taille du fichier, le système de fichiers alloue un ou plusieurs blocs à chaque fichier.

En parlant de gestion de l'espace, le système de fichiers est au courant de chaque bloc _utilisé_ et _inutilisé_ sur les partitions, de sorte qu'il pourra allouer de l'espace aux nouveaux fichiers ou récupérer les fichiers existants sur demande.

L'unité de stockage la plus basique dans les partitions formatées en ext4 est le bloc. Cependant, les blocs contigus sont regroupés en **groupes de blocs** pour une gestion plus facile.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/block-group.jpg) _La disposition d'un groupe de blocs au sein d'une partition ext4_

Chaque groupe de blocs possède ses propres structures de données et blocs de données.

Voici les structures de données qu'un groupe de blocs peut contenir :

-   **Superbloc (Super Block) :** un référentiel de métadonnées, qui contient des métadonnées sur l'ensemble du système de fichiers, telles que le nombre total de blocs dans le système de fichiers, le nombre total de blocs dans les groupes de blocs, les inodes, et plus encore. Tous les groupes de blocs ne contiennent pas le superbloc, cependant. Un certain nombre de groupes de blocs stockent une copie du superbloc comme sauvegarde.
-   **Descripteurs de groupe (Group Descriptors) :** Les descripteurs de groupe contiennent également des informations de comptabilité pour chaque groupe de blocs.
-   **Bitmap d'inodes (Inode Bitmap) :** Chaque groupe de blocs possède son propre quota d'inodes pour stocker des fichiers. Un bitmap de blocs est une structure de données utilisée pour identifier les inodes _utilisés_ et _inutilisés_ au sein du groupe de blocs. `1` indique un objet inode utilisé et `0` indique un objet inutilisé.
-   **Bitmap de blocs (Block Bitmap) :** une structure de données utilisée pour identifier les blocs de données utilisés et inutilisés au sein du groupe de blocs. `1` indique des blocs de données utilisés et `0` indique des blocs de données inutilisés.
-   **Table d'inodes (Inode Table) :** une structure de données qui définit la relation entre les fichiers et leurs inodes. Le nombre d'inodes stockés dans cette zone est lié à la taille de bloc utilisée par le système de fichiers.
-   **Blocs de données (Data Blocks) :** C'est la zone au sein du groupe de blocs où le contenu des fichiers est stocké.

Le système de fichiers ext4 va même un peu plus loin (par rapport à ext3) et organise les groupes de blocs en un groupe plus grand appelé _flex block groups_.

Les structures de données de chaque groupe de blocs, y compris le bitmap de blocs, le bitmap d'inodes et la table d'inodes, sont _concaténées_ et stockées dans le _premier groupe de blocs_ au sein de chaque flex block group.

Le fait d'avoir toutes les structures de données concaténées dans un seul groupe de blocs (le premier) libère plus de blocs de données contigus sur les autres groupes de blocs au sein de chaque flex block group.

Ces concepts peuvent être déroutants, mais vous n'avez pas besoin d'en maîtriser chaque bit. C'est juste pour illustrer la profondeur des systèmes de fichiers.

La disposition du premier groupe de blocs ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/02/block-group-detail.jpg) _La disposition du premier bloc dans un flex block group ext4_

Lorsqu'un fichier est écrit sur un disque, il est écrit dans un ou plusieurs blocs au sein d'un groupe de blocs.

La gestion des fichiers au niveau du groupe de blocs améliore considérablement les performances du système de fichiers, par opposition à l'organisation des fichiers comme une seule unité.

### Taille vs taille sur le disque

Avez-vous déjà remarqué que votre explorateur de fichiers affiche deux tailles différentes pour chaque fichier : **taille** et **taille sur le disque**.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/disksize-1.jpg) _Taille et Taille sur le disque_

Pourquoi la `taille` et la `taille sur le disque` sont-elles légèrement différentes ? me demanderez-vous.

Voici une explication :

Nous savons déjà que selon la taille du fichier, un ou plusieurs blocs sont alloués à un fichier.

Un bloc est l'espace minimum qui peut être alloué à un fichier. Cela signifie que l'espace restant d'un bloc partiellement rempli ne peut pas être utilisé par un autre fichier. C'est la règle !

Étant donné que la taille du fichier _n'est pas un multiple entier de blocs_, le dernier bloc peut être partiellement utilisé, et l'espace restant resterait inutilisé – ou serait rempli de zéros.

Ainsi, la "taille" est fondamentalement la taille réelle du fichier, tandis que la "taille sur le disque" est l'espace qu'il a occupé, même s'il ne l'utilise pas entièrement.

Vous pouvez utiliser la commande `du` sur Linux pour le voir par vous-même.

```
du -b "some-file.txt"
```

La sortie serait quelque chose comme ceci :

```
623 icon-link.svg
```

Et pour vérifier la taille sur le disque :

```
du -B 1 "icon-link.svg"
```

Ce qui donnera :

```
4096    icon-link.svg
```

D'après la sortie, le bloc alloué est d'environ 4 Ko, alors que la taille réelle du fichier est de 623 octets. Cela signifie que chaque taille de bloc sur ce système d'exploitation est de 4 Ko.

### Qu'est-ce que la fragmentation du disque ?

Au fil du temps, de nouveaux fichiers sont écrits sur le disque, les fichiers existants s'agrandissent, rétrécissent ou sont supprimés.

Ces changements fréquents dans le support de stockage laissent de nombreux petits espaces vides (gaps) entre les fichiers. Ces espaces sont dus à la même raison pour laquelle la taille du fichier et la taille du fichier sur le disque sont différentes. Certains fichiers ne rempliront pas tout le bloc, et beaucoup d'espace sera gaspillé. Et avec le temps, il n'y aura plus assez de blocs consécutifs pour stocker de nouveaux fichiers.

C'est alors que les nouveaux fichiers doivent être stockés sous forme de fragments.

La **fragmentation de fichiers** se produit lorsqu'un fichier est stocké sous forme de fragments sur le périphérique de stockage parce que le système de fichiers ne peut pas trouver suffisamment de blocs contigus pour stocker l'intégralité du fichier d'un seul coup.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/disk_image-1.jpg) _Un exemple de fichier fragmenté et non fragmenté_

Rendons cela plus clair avec un exemple.

Imaginez que vous ayez un document Word nommé `myfile.docx`.

`myfile.docx` est initialement stocké dans quelques blocs contigus sur le disque ; disons que voici comment les blocs sont nommés : `LBA250`, `LBA251` et `LBA252`.

Maintenant, si vous ajoutez plus de contenu à `myfile.docx` et que vous l'enregistrez, il devra occuper plus de blocs sur le support de stockage.

Puisque `myfile.docx` est actuellement stocké sur `LBA250`, `LBA251` et `LBA252`, le nouveau contenu devrait de préférence se trouver dans `LBA253` et ainsi de suite – selon le nombre de blocs supplémentaires nécessaires pour accommoder les nouveaux changements.

Maintenant, imaginez que `LBA253` soit déjà pris par un autre fichier (peut-être est-ce le premier bloc d'un autre fichier). Dans ce cas, le nouveau contenu de `myfile.docx` doit être stocké sur des blocs différents quelque part ailleurs sur les disques, par exemple, `LBA312` et `LBA313`.

`myfile.docx` est devenu fragmenté 💔.

La fragmentation des fichiers pèse sur le système de fichiers car chaque fois qu'un fichier fragmenté est demandé par un programme utilisateur, le système de fichiers doit collecter chaque morceau du fichier à partir de divers emplacements sur un disque.

Ce surcoût s'applique également à l'enregistrement du fichier sur le disque.

La fragmentation peut également se produire lorsqu'un fichier est écrit sur le disque pour la première fois, probablement parce que le fichier est énorme et qu'il ne reste pas beaucoup de blocs continus sur la partition.

La fragmentation est l'une des raisons pour lesquelles certains systèmes d'exploitation ralentissent à mesure que le système de fichiers vieillit.

### Devons-nous nous soucier de la fragmentation de nos jours ?

La réponse courte est : plus vraiment !

Les systèmes de fichiers modernes utilisent des algorithmes intelligents pour éviter (ou détecter précocement) la fragmentation autant que possible.

Ext4 effectue également une sorte de **préallocation,** qui consiste à réserver des blocs pour un fichier avant qu'ils ne soient réellement nécessaires – en s'assurant que le fichier ne sera pas fragmenté s'il s'agrandit avec le temps.

Le nombre de _blocs préalloués_ est défini dans le _champ de longueur_ de l'extent du fichier de son objet inode.

De plus, ext4 utilise une technique d'allocation appelée **allocation retardée (delayed allocation)**.

L'idée est qu'au lieu d'écrire dans les blocs de données un par un lors d'une écriture, les demandes d'allocation sont accumulées dans un tampon et sont écrites sur le disque en une seule fois.

Le fait de ne pas avoir à appeler l'_allocateur de blocs_ du système de fichiers à chaque demande d'écriture aide le système de fichiers à faire de meilleurs choix pour la distribution de l'espace disponible. Par exemple, en plaçant les fichiers volumineux à l'écart des fichiers plus petits.

Imaginez qu'un petit fichier soit situé entre deux fichiers volumineux. Maintenant, si le petit fichier est supprimé, il laisse un petit espace entre les deux fichiers.

Répartir les fichiers de cette manière laisse suffisamment d'espaces entre les blocs de données, ce qui aide le système de fichiers à gérer (et à éviter) la fragmentation plus facilement.

L'allocation retardée réduit activement la fragmentation et augmente les performances.

## Répertoires

Un répertoire (dossier sous Windows) est un fichier spécial utilisé comme **conteneur logique** pour regrouper des fichiers et des répertoires au sein d'un système de fichiers.

Sur NTFS et Ext4, les répertoires et les fichiers sont traités de la même manière. Cela dit, les répertoires ne sont que des fichiers qui possèdent leur propre inode (sur Ext4) ou entrée MFT (on NTFS).

L'inode ou l'entrée MFT d'un répertoire contient des informations sur ce répertoire, ainsi qu'une collection d'entrées pointant vers les fichiers "sous" ce répertoire.

Les fichiers ne sont pas littéralement contenus dans le répertoire, mais ils sont associés au répertoire de telle sorte qu'ils apparaissent comme les enfants du répertoire à un niveau supérieur, comme dans un programme d'explorateur de fichiers.

Ces entrées sont appelées **entrées de répertoire (directory entries).** Les entrées de répertoire contiennent des noms de fichiers mappés à leur inode/entrée MFT.

En plus des entrées de répertoire, il existe deux autres entrées. L'entrée `.`, qui pointe vers le répertoire lui-même, et `..`, qui pointe vers le répertoire parent de ce répertoire.

Sur Linux, vous pouvez utiliser `ls` dans un répertoire pour voir les entrées de répertoire avec leurs numéros d'inode associés :

```
ls -lai
```

Et la sortie ressemblerait à ceci :

```
63756 drwxr-xr-x 14 root root   4096 Dec  1 17:24 .
     2 drwxr-xr-x 19 root root   4096 Dec  1 17:06 ..
 81132 drwxr-xr-x  2 root root   4096 Feb 18 06:25 backups
 81020 drwxr-xr-x 14 root root   4096 Dec  2 07:01 cache
 81146 drwxrwxrwt  2 root root   4096 Oct 16 21:43 crash
 80913 drwxr-xr-x 46 root root   4096 Dec  1 22:14 lib

 ...
```

## Règles de nommage des fichiers

Certains systèmes de fichiers imposent des limitations sur les noms de fichiers.

La limitation peut porter sur la **longueur du nom de fichier** ou sur la **sensibilité à la casse du nom de fichier**.

Par exemple, dans les systèmes de fichiers NTFS (Windows) et APFS (Mac), `MonFichier` et `monfichier` font référence au même fichier, tandis que sur ext4 (Linux), ils pointent vers des fichiers différents.

Pourquoi cela est-il important ? me demanderez-vous.

Imaginez que vous créiez une page web sur votre machine Windows. La page web contient le logo de votre entreprise, qui est un fichier PNG, comme ceci :

```
<!DOCTYPE html>
<html>
    <head>
        <title>Produits - Votre Site Web</title>
    </head>
    <body>
        <!--QUELQUE CONTENU-->
        <img src="img/logo.png">
        <!--ENCORE PLUS DE CONTENU-->
    </body>
</html>
```

Si le nom réel du fichier est `Logo.png` (notez le **L** majuscule), vous pouvez toujours voir l'image lorsque vous ouvrez votre page web sur votre navigateur web (sur votre machine Windows).

Cependant, une fois que vous le déployez sur un serveur Linux et que vous le visualisez en direct, vous verrez une image cassée.

Pourquoi ?

Parce que sous Linux (système de fichiers ext4), `logo.png` et `Logo.png` pointent vers deux fichiers différents.

Gardez donc cela à l'esprit lorsque vous développez sous Windows et que vous déployez sur un serveur Linux.

## Règles pour la taille des fichiers

Un aspect important des systèmes de fichiers est la **taille maximale de fichier** qu'ils supportent.

Un ancien système de fichiers comme **FAT32** (utilisé par MS-DOS +7.1, la famille Windows 9x et les mémoires flash) ne peut pas stocker de fichiers de plus de 4 Go, tandis que son successeur, **NTFS**, permet des tailles de fichiers allant jusqu'à **16 EB** (1000 To).

Comme le NTFS, l'exFAT permet également une taille de fichier de 16 EB. Cela fait de l'exFAT une option idéale pour stocker des objets de données massifs, tels que des fichiers vidéo.

En pratique, il n'y a pas de limitation sur la taille des fichiers dans les systèmes de fichiers exFAT et NTFS.

L'ext4 de Linux et l'APFS d'Apple supportent des fichiers allant respectivement jusqu'à **16 TiB** et **8 EiB**.

## Programmes de gestion de fichiers

Comme vous le savez, la couche logique du système de fichiers fournit une API pour permettre aux applications utilisateur d'effectuer des opérations sur les fichiers, telles que les opérations `read`, `write`, `delete` et `execute`.

L'API du système de fichiers est cependant un mécanisme de bas niveau, conçu pour les programmes informatiques, les environnements d'exécution et les shells – et non pour un usage quotidien.

Cela dit, les systèmes de fichiers fournissent des utilitaires de gestion de fichiers pratiques prêts à l'emploi pour votre gestion quotidienne des fichiers.

Par exemple, l'**Explorateur de fichiers** sur Windows, le **Finder** sur Mac OS et **Nautilus** sur Ubuntu sont des exemples de programmes de gestion de fichiers.

Ces utilitaires utilisent l'API du système de fichiers logique sous le capot.

En dehors de ces outils GUI, les systèmes d'exploitation exposent également les API du système de fichiers via les interfaces en ligne de commande, comme l'Invite de commandes sur Windows et le Terminal sur Mac et Linux.

Ces interfaces textuelles aident les utilisateurs à effectuer toutes sortes d'opérations sur les fichiers sous forme de commandes textuelles – comme nous l'avons fait dans les exemples précédents.

## Gestion de l'accès aux fichiers

Tout le monde ne devrait pas être capable de supprimer ou de modifier un fichier qu'il ne possède pas ou pour lequel il n'est pas autorisé.

Les systèmes de fichiers modernes fournissent des mécanismes pour contrôler l'accès et les capacités des utilisateurs concernant les fichiers.

Les données concernant les permissions des utilisateurs et la propriété des fichiers sont stockées dans une structure de données appelée Access-Control List (ACL) sur Windows ou Access-Control Entries (ACE) sur les systèmes d'exploitation de type Unix (Linux et Mac OS).

Cette fonctionnalité est également disponible dans le CLI (Invite de commandes ou Terminal), où un utilisateur peut changer la propriété des fichiers ou limiter les permissions de chaque fichier directement depuis l'interface en ligne de commande.

Par exemple, un propriétaire de fichier (sur Linux ou Mac) peut configurer un fichier pour qu'il soit accessible au public, comme ceci :

```
chmod 777 myfile.txt
```

`777` signifie que tout le monde peut effectuer toutes les opérations (lire, écrire, exécuter) sur `myfile.txt`. Veuillez noter qu'il s'agit juste d'un exemple, et vous ne devriez pas définir la permission d'un fichier sur `777`.

## Maintien de l'intégrité des données

Supposons que vous travailliez sur votre thèse depuis un mois maintenant. Un jour, vous ouvrez le fichier, effectuez quelques modifications et l'enregistrez.

Une fois que vous enregistrez le fichier, votre programme de traitement de texte envoie une requête "d'écriture" à l'API du système de fichiers (le système de fichiers logique).

La requête est finalement transmise à la couche physique pour stocker le fichier sur plusieurs blocs.

Mais que se passe-t-il si le système plante pendant que l'ancienne version du fichier est en train d'être remplacée par la nouvelle version ?

Dans les anciens systèmes de fichiers (comme FAT32 ou ext2), les données seraient corrompues car elles ont été partiellement écrites sur le disque.

Cela est moins susceptible d'arriver avec les systèmes de fichiers modernes car ils utilisent une technique appelée **journalisation (journaling).**

Les systèmes de fichiers à journalisation enregistrent chaque opération qui est sur le point de se produire dans la couche physique mais qui ne s'est pas encore produite.

L'objectif principal est de garder une trace des changements qui n'ont pas encore été validés (committed) _physiquement_ dans le système de fichiers.

Le journal est une allocation spéciale sur le disque où chaque tentative d'écriture est d'abord stockée en tant que **transaction**.

Une fois que les données sont physiquement placées sur le périphérique de stockage, le changement est validé dans le système de fichiers.

En cas de défaillance du système, le système de fichiers détectera la transaction incomplète et l'annulera (roll back) comme si elle n'avait jamais eu lieu.

Cela dit, le nouveau contenu (qui était en cours d'écriture) peut toujours être perdu, mais les données existantes resteraient intactes.

Les systèmes de fichiers modernes tels que NTFS, APFS et ext4 (même ext3) utilisent la journalisation pour éviter la corruption des données en cas de défaillance du système.

## Systèmes de fichiers de base de données

Les systèmes de fichiers typiques organisent les fichiers sous forme d'arborescences de répertoires.

Pour accéder à un fichier, vous parcourez le répertoire respectif, et vous l'avez.

```
cd /music/country/highwayman
```

Cependant, dans un système de fichiers de base de données, il n'y a pas de concept de chemins et de répertoires.

Le système de fichiers de base de données est un **système à facettes** qui regroupe les fichiers sur la base de divers _attributs_ et _dimensions_.

Par exemple, les fichiers MP3 peuvent être listés par artiste, genre, année de sortie et album – en même temps !

Un système de fichiers de base de données ressemble plus à une application de haut niveau pour vous aider à organiser et à accéder à vos fichiers plus facilement et plus efficacement. Cependant, vous ne pourrez pas accéder aux fichiers bruts en dehors de cette application.

Un système de fichiers de base de données ne peut cependant pas remplacer un système de fichiers typique. C'est juste une abstraction de haut niveau pour une gestion plus facile des fichiers sur certains systèmes.

L'application **iTunes** sur Mac OS est un bon exemple de système de fichiers de base de données.

## Conclusion

Wow ! Vous êtes arrivé à la fin, ce qui signifie que vous en savez beaucoup plus sur les systèmes de fichiers maintenant. Mais je suis sûr que ce ne sera pas la fin de vos études sur les systèmes de fichiers.

Alors encore une fois – pouvons-nous décrire ce qu'est un système de fichiers et comment il fonctionne en une seule phrase ?

Nous ne pouvons pas ! 😁

Mais finissons ce post avec la brève description que j'ai utilisée au début :

Un **système de fichiers** définit la manière dont les fichiers sont **nommés**, **stockés** et **récupérés** à partir du périphérique de stockage.

Très bien, je pense que cela suffit pour cet article. Si vous remarquez que quelque chose manque ou que je me suis trompé, n'hésitez pas à me le faire savoir dans les commentaires ci-dessous. Cela m'aiderait, ainsi que les autres !

Au fait, si vous aimez les guides plus complets comme celui-ci, visitez mon site web [decodingweb. dev][13] et suivez-moi sur [Twitter][14] car, en plus de freeCodeCamp, ce sont les canaux que j'utilise pour partager mes découvertes quotidiennes.

Merci de m'avoir lu, et bonne continuation dans votre apprentissage ! 😃

[1]: https://www.freecodecamp.org/
[2]: https://www.decodingweb.dev/books/decoding-web-development/http
[3]: https://www.decodingweb.dev/books/processing-fundamentals/operating-systems-and-memory-management
[4]: https://www.flickr.com/photos/computerhotline/
[5]: https://www.decodingweb.dev/books/processing-fundamentals/how-cpu-works
[6]: https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/configure-more-than-four-partitions-on-a-biosmbr-based-hard-disk?view=windows-11
[7]: https://en.wikipedia.org/wiki/User:Kbolino
[8]: https://www.howtogeek.com/236055/how-to-write-to-ntfs-drives-on-a-mac/
[9]: https://en.wikipedia.org/wiki/Debian
[10]: https://en.wikipedia.org/wiki/Ubuntu
[11]: https://www.decodingweb.dev/books/processing-fundamentals/how-a-computer-program-works#device-drivers
[12]: https://docs.microsoft.com/en-us/windows/win32/fileio/master-file-table
[13]: https://www.decodingweb.dev/
[14]: https://twitter.com/lavary_