---
title: Comment fonctionne le partitionnement de disque Master Boot Record sous Linux
subtitle: ''
author: Kedar Makode
co_authors: []
series: null
date: '2024-02-07T10:29:26.000Z'
originalURL: https://freecodecamp.org/news/how-mbr-works-in-linux
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/Frame-1000004568-1.png
tags:
- name: Linux
  slug: linux
- name: storage
  slug: storage
seo_title: Comment fonctionne le partitionnement de disque Master Boot Record sous
  Linux
seo_desc: 'Efficient storage management is a crucial aspect of maintaining a well-organized
  computing environment.

  In this detailed guide, we''ll explore the features of Master Boot Record (MBR)
  disk partitioning using the parted command on Linux.

  Additionally, ...'
---

Une gestion efficace du stockage est un aspect crucial pour maintenir un environnement informatique bien organisé.

Dans ce guide détaillé, nous explorerons les fonctionnalités du partitionnement de disque Master Boot Record (MBR) en utilisant la commande `parted` sur Linux.

De plus, nous aborderons le processus d'ajout d'un nouveau disque dur dans VMware, ainsi que la manière de formater et de monter une nouvelle partition créée en utilisant `mkfs` et `fstab`, respectivement.

## **Table des matières**

Voici ce que nous couvrirons dans ce guide complet :

* [Aperçu du MBR](#heading-apercu-du-mbr)
    
* [Introduction à l'utilitaire Parted](#heading-introduction-a-lutilitaire-parted)
    
* [Comment identifier les disques](#heading-comment-identifier-les-disques)
    
* [Comment lancer Parted](#heading-comment-lancer-parted)
    
* [Comment créer une nouvelle table de partition MBR](#heading-comment-creer-une-nouvelle-table-de-partition-mbr)
    
* [Comment créer des partitions principales](#heading-comment-creer-des-partitions-principales)
    
* [Comment afficher les informations de partition](#heading-comment-afficher-les-informations-de-partition)
    
* [Comment formater la partition avec mkfs](#heading-comment-formater-la-partition-avec-mkfs)
    
* [Comment automatiser le montage avec fstab](#heading-comment-automatiser-le-montage-avec-fstab)
    
* [Comment monter une partition](#heading-comment-monter-une-partition)
    
* [Comment créer des partitions logiques](#heading-comment-creer-des-partitions-logiques)
    
* [Conclusion](#heading-conclusion)
    

## Aperçu du MBR

Le MBR est un schéma de partitionnement hérité utilisé sur les systèmes basés sur le BIOS, avec un secteur de 512 octets au début du périphérique de stockage qui contient les informations de partition et le chargeur de démarrage.

Les 512 octets du MBR sont organisés comme suit :

* **Code de démarrage principal (446 octets) :** Cette section contient le code exécutable responsable du chargement du système d'exploitation. Il localise la partition active (amorçable) et passe le contrôle à son secteur de démarrage.
    
* **Table de partition (64 octets) :** Les 64 octets suivants sont réservés à la table de partition, qui peut décrire jusqu'à quatre partitions principales ou trois partitions principales et une partition étendue.
    
* **Signature MBR (2 octets) :** Les deux derniers octets contiennent une signature (0x55AA), indiquant qu'il s'agit d'un MBR valide.
    

## Introduction à l'utilitaire Parted

`parted` est un utilitaire en ligne de commande conçu pour créer, redimensionner et gérer les partitions de disque sur les systèmes Linux.

Il offre un ensemble complet de fonctionnalités pour gérer les tâches liées aux disques et est largement utilisé en raison de sa flexibilité et de ses capacités robustes. Les principaux objectifs de `parted` incluent :

* **Création et redimensionnement de partitions :** `parted` permet aux utilisateurs de créer de nouvelles partitions sur un disque, de redimensionner les partitions existantes et d'ajuster l'allocation de l'espace disque.
    
* **Support des systèmes de fichiers :** Il prend en charge divers systèmes de fichiers, notamment ext2, ext3, ext4, FAT, NTFS, et plus encore, permettant aux utilisateurs de choisir le système de fichiers qui répond le mieux à leurs besoins.
    
* **Manipulation des tables de partition :** `parted` facilite la gestion des tables de partition, y compris la création, la modification et la suppression de partitions au sein de ces tables.
    
* **Opérations au niveau des secteurs :** L'utilitaire fonctionne au niveau des secteurs, permettant un contrôle et une manipulation précis des structures de disque.
    

### Comment installer Parted

Vous pouvez installer `parted` sur votre système en utilisant cette commande :

```bash
sudo apt-get install parted
```

Avant de créer une partition, nous devons ajouter un nouveau disque à notre machine virtuelle. J'utilise VMware. Allez-y et démarrez la machine virtuelle RHEL.

Tout d'abord, nous devons aller à l'option Player en haut à gauche, puis à l'option Manage. En utilisant cette option, vous pouvez sélectionner les paramètres de la machine virtuelle.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot--2-.png align="left")

*Ajouter un nouveau disque dur dans VMware*

Cliquez sur "add to new hard disk". Ensuite, sélectionnez le disque dur et continuez à cliquer sur suivant jusqu'à ce qu'il demande la capacité du disque. À des fins d'apprentissage, ajoutez uniquement un disque de 5 Go.

Continuez à cliquer sur suivant jusqu'à ce que vous obteniez l'option de finition.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot--3--1.png align="left")

*Ajout d'un disque dur virtuel - 1*

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot--4--1.png align="left")

*Ajout d'un disque dur virtuel - 2*

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot--5-.png align="left")

*Ajout d'un disque dur virtuel - 3*

Nous nous concentrons sur la création de partitions, donc nous ne nous concentrerons pas sur les parties qui ne sont pas nécessaires pour les partitions.

Ensuite, redémarrez votre machine virtuelle pour refléter le nouveau disque dur ajouté.

### Comment identifier les disques

L'identification des disques est une étape cruciale dans le processus de partitionnement de disque, car elle garantit que vous travaillez avec le bon périphérique de stockage sur votre système.

Utilisez la commande `lsblk` pour afficher des informations sur les périphériques de bloc, y compris les disques durs et les partitions.

```bash
lsblk
```

Recherchez le disque que vous souhaitez partitionner. Les noms des disques sont généralement au format `/dev/sdX`, où 'X' est une lettre minuscule représentant le disque. Par exemple, `/dev/sda`, `/dev/sdb`, etc.

### Comment lancer Parted

Ouvrez un terminal et lancez `parted` pour le disque cible :

```bash
parted /dev/sdX
```

Cela initie l'utilitaire `parted` avec des privilèges élevés et le dirige pour se concentrer sur le périphérique de stockage spécifié (`/dev/sdX`).

Une fois exécuté, l'utilisateur entre dans le mode interactif `parted` pour le périphérique spécifié, permettant la configuration et la gestion des partitions sur ce périphérique de stockage particulier.

### Comment créer une nouvelle table de partition MBR

Si le disque n'est pas partitionné, créez une nouvelle table de partition MBR en utilisant cette commande :

```bash
(parted) mklabel msdos
```

Cela indique à `parted` de créer une nouvelle table de partition MBR sur le périphérique de stockage actuellement sélectionné. Cette action supprimera toutes les informations de partition existantes sur le périphérique, commençant effectivement avec une ardoise propre pour le partitionnement.

Il est important de noter que cette commande doit être utilisée avec prudence, car elle efface la table de partition existante et toutes les données associées sur le périphérique.

## Comment créer des partitions principales

Vous pouvez créer une partition principale avec un type de système de fichiers spécifié, un début et une fin :

```bash
(parted) mkpart primary [filesystem-type] [start] [end]
```

* `mkpart` : Il s'agit de la commande `parted` utilisée pour créer une nouvelle partition. Le terme "mkpart" signifie "make partition".
    
* `primary` : Cela spécifie le type de partition à créer. Dans ce cas, il s'agit d'une partition principale. Les partitions principales sont les partitions de base sur un disque, et elles peuvent être utilisées pour installer un système d'exploitation ou stocker des données.
    
* `[filesystem-type]` : Remplacez ce espace réservé par le type de système de fichiers souhaité pour la partition. Les types de systèmes de fichiers courants incluent `ext4`, `ntfs`, `fat32`, et ainsi de suite.
    
* `[start]` et `[end]` : Ces espaces réservés représentent les points de départ et de fin de la partition, spécifiés en mégaoctets (Mo) ou en pourcentage de la taille totale du disque. Par exemple, vous pouvez définir la partition pour qu'elle commence à 1 Go et se termine à 10 Go.
    

### Comment afficher les informations de partition

Utilisez cette commande pour vérifier la disposition des partitions :

```bash
(parted) print free
```

Lorsque vous entrez `(parted) print free` dans le mode interactif `parted`, il fournira un résumé de l'espace libre disponible sur le disque sélectionné, y compris des détails tels que les points de départ et de fin de l'espace non alloué, sa taille et toute contrainte sur la création de nouvelles partitions dans cet espace.

Voici le résultat :

```bash
(parted) print free
Model: ABC Storage Device
Disk /dev/sdX: 1000GB
Sector size (logical/physical): 512B/4096B
Partition Table: msdos
Disk Flags:

Number  Start   End     Size    Type  File system  Flags
        32.3kB  1049kB  1017kB  Free Space
 1      1049kB  256MB   255MB   primary  ext4         boot
 2      256MB   512MB   256MB   primary  linux-swap
 3      512MB   1000GB  1000GB  primary  ntfs
```

Appuyez sur `ctrl + d` pour sortir de parted.

### Comment formater la partition avec `mkfs`

Après le partitionnement, formatez la partition avec un système de fichiers souhaité (par exemple : ext4)

```bash
mkfs.[filesystem-type] /dev/sdX1
```

Cela indique au système de créer un système de fichiers du type spécifié sur la partition désignée. Après avoir exécuté cette commande, le système de fichiers choisi sera créé sur la partition, et il sera prêt à stocker des fichiers et des données.

### Comment automatiser le montage avec `fstab`

Vous pouvez trouver l'UUID de la partition en utilisant cette commande :

```bash
sudo blkid /dev/sdX1
```

Modifiez `/etc/fstab` pour inclure une entrée pour le montage automatique, et assurez-vous que le type de système de fichiers est le même que le type de système de fichiers de `mkfs.[filesystem-type]`

Le fichier `/etc/fstab`, abréviation de "file systems table", est un fichier de configuration crucial sur les systèmes Unix et de type Unix, y compris Linux. Il est utilisé pour définir comment les périphériques de stockage (tels que les disques durs et les partitions) doivent être montés dans le système de fichiers.

Le but principal du fichier `/etc/fstab` est de spécifier comment divers périphériques de stockage doivent être montés pendant le processus de démarrage du système.

```bash
UUID=[your-uuid] /dir-to-mount-path [filesystem-type] defaults 0 0
```

Voici un exemple :

```bash
UUID=127854Vd344HHttRpq977739 /kedar ext4 defaults 0 0
```

`UUID=127854Vd344HHttRpq977739` : Cette partie spécifie l'identifiant unique universel (UUID) du périphérique de bloc ou de la partition à monter. L'UUID est un identifiant unique attribué au système de fichiers, garantissant une référence cohérente même si les noms des périphériques changent. Dans ce cas, l'UUID est "127854Vd344HHttRpq977739".

`/kedar` : Cette partie indique le point de montage, qui est le répertoire dans le système de fichiers où le périphérique spécifié par l'UUID sera attaché. Dans cet exemple, le point de montage est "/kedar".

`ext4` : Cela spécifie le type de système de fichiers sur le périphérique. Dans ce cas, il s'agit de "ext4", qui est un système de fichiers couramment utilisé sur Linux.

`defaults` : L'option "defaults" est un raccourci pour un ensemble d'options de montage couramment utilisées. Elle inclut des options telles que l'accès en lecture/écriture et permet d'exécuter des binaires à partir du système de fichiers. Si des options plus spécifiques sont nécessaires, elles peuvent être listées explicitement.

`0` : Ce champ représente l'option de vidage. Il est utilisé par la commande `dump` pour déterminer si le système de fichiers doit être sauvegardé. Une valeur de 0 indique qu'aucune sauvegarde automatique n'est requise.

`0` : Le dernier champ représente l'option de passage. Il est utilisé par l'utilitaire `fsck` (vérification du système de fichiers) pour déterminer l'ordre dans lequel les systèmes de fichiers sont vérifiés au moment du démarrage. Une valeur de 0 indique que le système de fichiers ne doit pas être vérifié.

Cette entrée `/etc/fstab` dirige le système pour monter un périphérique, identifié par l'UUID spécifié et formaté en ext4, sur le répertoire "/kedar" pendant le processus de démarrage. Le montage est effectué avec les options par défaut, et il n'y a pas de nécessité de sauvegardes automatiques ou de vérifications du système de fichiers.

Voici quelques raisons d'utiliser l'UUID au lieu du nom de la partition :

* Les noms des périphériques (par exemple, `/dev/sda1`) peuvent changer, surtout dans les systèmes avec plusieurs périphériques de stockage ou lorsque les configurations matérielles sont modifiées. Les UUID restent constants.
    
* Pendant le processus de démarrage, plusieurs périphériques de stockage peuvent être détectés simultanément. Les UUID éliminent la possibilité de conditions de course, où le système d'exploitation peut attribuer différents noms au même périphérique physique dans différentes instances de démarrage.
    
* Si les noms des périphériques sont utilisés dans `/etc/fstab` et que les noms changent en raison de modifications matérielles, cela peut entraîner des erreurs de montage ou une corruption des données. Les UUID garantissent que le bon périphérique est toujours monté.
    
* Les UUID sont plus lisibles par l'homme et moins sujets aux fautes de frappe que les noms des périphériques, rendant le fichier `/etc/fstab` plus facile à lire et à maintenir.
    
* Les UUID restent les mêmes lors du déplacement d'un périphérique de stockage d'un système à un autre, garantissant un montage correct sans modifier `/etc/fstab` pour le nouveau système.
    

Voici un exemple d'entrée `/etc/fstab` utilisant l'UUID :

```bash
UUID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx /mnt/data ext4 defaults 0 2
```

Remplacez `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx` par l'UUID réel de la partition.

### Comment monter une partition

Une fois tout terminé, nous allons monter la partition sur l'un de vos répertoires.

```bash
mount -av
```

Si cela retourne un message "successfully mounted" sur le répertoire `kedar`, alors votre partition a été montée sur le répertoire `kedar`.

Maintenant, chaque fois que vous allumez votre système, la partition spécifiée sera automatiquement montée sur le répertoire "/kedar", assurant un accès transparent à son contenu tout au long de vos sessions informatiques.

Cette configuration de montage persistante est facilitée par l'entrée dans le fichier `/etc/fstab`, fournissant une attache cohérente et fiable de la partition pendant le processus de démarrage du système.

## Comment créer des partitions logiques

Les partitions logiques sont un concept clé dans le partitionnement de disque, en particulier dans les systèmes utilisant le schéma de partitionnement Master Boot Record (MBR).

Le MBR permet un maximum de quatre partitions principales, et pour surmonter cette limitation, l'une des partitions principales peut être désignée comme une partition étendue.

Au sein de la partition étendue, plusieurs partitions logiques peuvent ensuite être créées.

### **Identifier le disque**

Commencez par identifier le disque où vous souhaitez créer des partitions logiques. Vous pouvez utiliser les commandes `lsblk` ou `fdisk -l` pour lister les disques disponibles et leurs partitions.

```bash
lsblk
```

### **Lancer Parted pour le disque**

Utilisez la commande `parted` pour lancer l'interface interactive pour le disque choisi (remplacez 'X' par l'identifiant de disque approprié) :

```bash
parted /dev/sdX
```

### **Créer une partition étendue**

Si elle n'est pas déjà créée, vous devez établir une partition étendue au sein de laquelle les partitions logiques résideront.

Cette étape est essentielle car les partitions logiques ne peuvent exister qu'au sein d'une partition étendue. Supposons que l'espace libre est de 50% à 100% du disque :

```bash
(parted) mkpart extended 50% 100%
```

### **Créer des partitions logiques**

Maintenant, au sein de la partition étendue, vous pouvez créer des partitions logiques. L'exemple suivant crée une partition logique en utilisant le système de fichiers **ext4** de 0% à 25% de la partition étendue.

Vous pouvez également donner la taille en utilisant le format Mo. Pour cela, vous devez connaître l'espace libre. Vous pouvez le faire en utilisant la commande `print free` à l'intérieur de parted.

```bash
(parted) mkpart logical ext4 0% 25%
```

Vous pouvez répéter cette étape pour créer des partitions logiques supplémentaires avec différentes tailles ou systèmes de fichiers.

### Convention de numérotation des schémas de partitionnement

Dans le schéma de partitionnement Master Boot Record (MBR), la convention de numérotation pour les partitions logiques au sein d'une partition étendue commence généralement à partir de 5. Cela est dû au fait que les quatre partitions principales (si elles existent) sont assignées aux numéros 1 à 4, et les partitions logiques sont numérotées à partir de 5.

Voici une convention de numérotation courante :

* Partition principale 1 : `/dev/sdX1`
    
* Partition principale 2 : `/dev/sdX2`
    
* Partition principale 3 : `/dev/sdX3`
    
* Partition principale 4 : `/dev/sdX4`
    
* Partition étendue : `/dev/sdX4` (la partition étendue est comptée comme l'une des quatre)
    
* Partition logique 5 : `/dev/sdX5`
    
* Partition logique 6 : `/dev/sdX6`
    
* Partition logique 7 : `/dev/sdX7`, et ainsi de suite.
    

## **Conclusion**

Merci d'avoir exploré avec moi aujourd'hui comment fonctionne le partitionnement de disque MBR. Vous pouvez approfondir le domaine de l'expertise Linux et rester à l'écoute pour plus de contenu perspicace dans mes futurs tutoriels.

Vous pouvez me suivre sur :

* [Twitter](https://twitter.com/Kedar__98)
    
* [LinkedIn](https://www.linkedin.com/in/kedar-makode-9833321ab/?originalSubdomain=in)