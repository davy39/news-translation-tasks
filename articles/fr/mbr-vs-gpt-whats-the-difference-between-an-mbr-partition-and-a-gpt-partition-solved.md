---
title: 'MBR vs GPT : Quelle est la différence entre une partition MBR et une partition
  GPT ? [Résolu]'
subtitle: ''
author: Kristofer Koishigawa
co_authors: []
series: null
date: '2020-10-12T04:12:00.000Z'
originalURL: https://freecodecamp.org/news/mbr-vs-gpt-whats-the-difference-between-an-mbr-partition-and-a-gpt-partition-solved
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9842740569d1a4ca190c.jpg
tags:
- name: hardware
  slug: hardware
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: 'MBR vs GPT : Quelle est la différence entre une partition MBR et une partition
  GPT ? [Résolu]'
seo_desc: 'If you''re building a PC, you might have been asked how you want to install
  your operating system – MBR or GPT?

  The differences between an MBR and GPT partition are pretty straightforward. But
  there''s a lot of background information that will help you...'
---

Si vous construisez un PC, on vous a peut-être demandé comment vous souhaitez installer votre système d'exploitation – MBR ou GPT ?

Les différences entre une partition MBR et GPT sont assez simples. Mais il y a beaucoup d'informations contextuelles qui vous aideront à avoir une image plus claire de chaque type de table de partition, et quand vous devriez choisir l'une plutôt que l'autre.

Dans cet article, nous allons aborder ce qu'est une partition, la différence entre une partition MBR et GPT, si vous devriez passer d'un type de partition à un autre, et plus encore.

## Qu'est-ce qu'une partition ?

Une partition est une division virtuelle d'un disque dur (HDD) ou d'un disque SSD. Chaque partition peut varier en taille et sert généralement une fonction différente.

Par exemple, dans Windows, il y a généralement une petite partition de récupération et une grande partition de système de fichiers étiquetée `C:`. La partition `C:` est celle que la plupart des gens connaissent, car c'est là que vous installez généralement vos programmes et stockez vos divers fichiers.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/disk-management.png)
_Gestionnaire de disque Windows – [Source](https://docs.microsoft.com/en-us/windows-server/storage/disk-management/overview-of-disk-management)_

Dans Linux, il y a généralement une partition racine (`/`), une pour le swap qui aide à la gestion de la mémoire, et une grande partition `/home`. La partition `/home` est similaire à la partition `C:` dans Windows en ce sens que c'est là que vous installez la plupart de vos programmes et stockez des fichiers.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/yCyXA.png)
_GParted dans Linux – [Source](https://bbs.archlinux.org/viewtopic.php?id=155698)_

Si vous avez acheté votre ordinateur dans un magasin et que le système d'exploitation est déjà installé, alors le fabricant a déjà pris en charge les partitions. Vous n'avez pas besoin de vous en soucier sauf si vous voulez faire quelque chose comme un dual-boot Windows et Linux à partir du même HDD ou SSD.

Même si vous installez vous-même le système d'exploitation, la plupart du temps l'installateur suggérera des partitions et des tailles de partition par défaut. Encore une fois, vous n'avez généralement pas besoin de faire des ajustements.

Maintenant que vous avez une vue d'ensemble de ce qu'est une partition, nous pouvons plonger dans les différences entre les partitions MBR et GPT.

**Note :** Je vais utiliser le terme "lecteur" pour désigner à la fois les HDD et les SSD à partir de maintenant.

## Aperçu des partitions MBR et GPT

Avant qu'un lecteur puisse être divisé en partitions individuelles, il doit être configuré pour utiliser un schéma ou une table de partition spécifique.

Une table de partition indique au système d'exploitation comment les partitions et les données sur le lecteur sont organisées. Par exemple, les captures d'écran ci-dessus montrent les tables de partition sur le lecteur, et chaque partition individuelle est affichée sous forme de bloc rectangulaire.

Il existe deux principaux types de tables de partition : MBR et GPT.

MBR signifie Master Boot Record, et est un peu d'espace réservé au début du lecteur qui contient les informations sur la manière dont les partitions sont organisées. Le MBR contient également du code pour lancer le système d'exploitation, et il est parfois appelé le Boot Loader.

GPT est l'abréviation de GUID Partition Table, et est un standard plus récent qui remplace lentement le MBR.

Contrairement à une table de partition MBR, GPT stocke les données sur la manière dont toutes les partitions sont organisées et comment démarrer le système d'exploitation sur l'ensemble du lecteur. Ainsi, si une partition est effacée ou corrompue, il est toujours possible de démarrer et de récupérer une partie des données.

Si vous avez acheté votre ordinateur au cours des cinq dernières années environ, il est très probable qu'il utilise des tables de partition GPT plutôt que les anciennes tables MBR.

## Différences entre les partitions MBR et GPT

Il existe un certain nombre de différences entre les partitions MBR et GPT, mais nous allons couvrir certaines des principales ici.

Tout d'abord, la capacité maximale des tables de partition MBR est d'environ 2 téraoctets. Vous pouvez utiliser un lecteur de plus de 2 téraoctets avec MBR, mais seuls les premiers 2 téraoctets du lecteur seront utilisés. Le reste de l'espace de stockage sur le lecteur sera gaspillé.

En revanche, les tables de partition GPT offrent une capacité maximale de 9,7 zettaoctets. 1 zettaoctet est d'environ 1 milliard de téraoctets, vous ne risquez donc pas de manquer d'espace de sitôt.

Ensuite, les tables de partition MBR peuvent avoir un maximum de 4 partitions séparées. Cependant, l'une de ces partitions peut être configurée pour être une partition _étendue_, qui est une partition qui peut être divisée en 23 partitions supplémentaires. Ainsi, le nombre absolu maximum de partitions qu'une table de partition MBR peut avoir est de 26 partitions.

Les tables de partition GPT permettent jusqu'à 128 partitions séparées, ce qui est plus que suffisant pour la plupart des applications réelles.

Comme le MBR est plus ancien, il est généralement associé à des systèmes Legacy BIOS plus anciens, tandis que le GPT se trouve sur des systèmes UEFI plus récents. Cela signifie que les partitions MBR ont une meilleure compatibilité logicielle et matérielle, bien que le GPT commence à rattraper son retard.

Nous allons jeter un bref coup d'œil à la fois au Legacy BIOS et à l'UEFI un peu plus tard dans l'article.

## Devez-vous passer de MBR à GPT ?

Si l'un de vos lecteurs utilise actuellement une table de partition MBR, vous vous demandez peut-être si vous devez passer au nouveau standard GPT.

En bref, probablement pas. Comme le dit le proverbe, si ce n'est pas cassé, ne le réparez pas.

Il est très facile de ruiner le secteur MBR du lecteur, rendant impossible le redémarrage. Vous devrez alors soit créer une clé USB de récupération avec Windows ou Linux et essayer de réparer le MBR, soit effacer complètement le lecteur et réinstaller le système d'exploitation.

Par expérience, cela ne vaut pas la peine.

Cela dit, il existe certains cas où vous pourriez envisager de passer de MBR à GPT.

Par exemple, peut-être que vous souhaitez mettre à niveau votre lecteur vers un lecteur de plus de 2 téraoctets, ou vous avez besoin de plus de 26 partitions. Même dans ces cas, vous devrez vous assurer que votre matériel peut même supporter une table de partition GPT et un BIOS UEFI.

Si vous avez fait des recherches et êtes sûr de vouloir passer à GPT, assurez-vous d'avoir une sauvegarde de votre lecteur et de toutes les données importantes. Dans le pire des cas, vous pourrez revenir en arrière sans avoir à tout réinstaller et recommencer à zéro.

## Aperçu du BIOS

J'ai mentionné le BIOS à plusieurs reprises auparavant. Bien que cela soit un peu en dehors du cadre de cet article, une compréhension de base du BIOS est nécessaire pour comprendre l'une des dernières différences principales entre les partitions MBR et GPT.

BIOS signifie Basic Input/Output System, et est le logiciel qui est stocké sur une puce sur la carte mère d'un ordinateur et qui s'exécute lorsque vous l'allumez pour la première fois.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/xThDu5d.jpg)
_Une puce BIOS sur une carte mère Gigabyte – [Source](https://forums.tomshardware.com/threads/gigabyte-ab350-gaming-3-cpu-led-on-no-posting.3103246/)_

Le BIOS fait des choses comme configurer le clavier, la souris et d'autres matériels, définir l'horloge du système, tester la mémoire, et ainsi de suite. Ensuite, il recherche un lecteur et charge le boot loader sur le lecteur, qui est soit une table de partition MBR, soit GPT.

Généralement, lorsque vous allumez votre ordinateur pour la première fois, vous verrez un logo de votre ordinateur ou du fabricant de la carte mère.

Souvent, il y a un message sous le logo indiquant quelle touche appuyer pour configurer le BIOS de l'ordinateur. Cette touche est généralement Supprimer, Échap ou F2, bien que cela varie selon le fabricant.

Comme mentionné précédemment, il existe deux principaux types de BIOS – Legacy BIOS et UEFI BIOS :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/windows-boot-screen-bios.jpg)
_Un écran de configuration Legacy BIOS – [Source](https://fossbytes.com/intel-end-legacy-bios-support-2020-uefi/)_

![Image](https://www.freecodecamp.org/news/content/images/2020/10/29143-uefiasus.jpg)
_Un écran de configuration UEFI BIOS – [Source](https://www.tested.com/tech/pcs/2894-what-you-should-know-about-uefi-and-windows-boot-times/)_

Les Legacy BIOS sont plus anciens et sont entièrement pilotés par clavier. Ils sont généralement simples en termes d'interface utilisateur, et ont une couleur de fond noir ou bleu écran de la mort.

UEFI signifie Unified Extensible Firmware Interface, et peut être considéré comme un nouveau type de BIOS. L'UEFI inclut souvent des graphiques pour montrer la vitesse du ventilateur, la température et les vitesses d'horloge du CPU, et peut parfois être contrôlé avec une souris ou un trackpad.

## MBR et GPT BIOS

Parce que MBR est un standard plus ancien, il est associé aux systèmes Legacy BIOS (et Legacy BIOS ne peut accéder qu'aux lecteurs avec une partition MBR). Ce n'est pas nécessairement une mauvaise chose, car le support pour Legacy BIOS est meilleur.

Mais encore une fois, l'une des limitations les plus évidentes des partitions MBR est qu'elles ne peuvent gérer que des lecteurs allant jusqu'à 2 téraoctets.

Le nouveau standard GPT est associé aux systèmes UEFI BIOS. Bien que le support pour les BIOS GPT et UEFI ne soit pas aussi bon que pour MBR/Legacy BIOS, il gagne du terrain.

De plus en plus de fabricants passent à l'UEFI BIOS, ce qui à son tour nécessite que les lecteurs utilisent le nouveau format GPT. Mais l'exigence pour les lecteurs formatés GPT s'accompagne de l'avantage d'une capacité beaucoup plus élevée et jusqu'à 128 partitions.

## En conclusion

Bien que comprendre la différence entre les partitions MBR et GPT soit un peu comme éplucher un oignon, espérons que vous l'ayez traversé sans vous mettre à pleurer.

Si tout ce que vous voulez est une référence rapide pour les différences entre les partitions MBR et GPT, voici un tableau pratique :

|   | MBR | GPT |
|---|:---:|:---:|
| Capacité maximale | 2 To | 9,7 Zo (~9,7 milliards de téraoctets) |
| Nombre maximal de partitions | 26 | 128 |
| Emplacement des données de partition/démarrage | Au début du lecteur | Sur l'ensemble du lecteur |
| Type de BIOS | Legacy BIOS | UEFI |

Et s'il vous plaît, ne soyez pas comme moi quand j'étais plus jeune – assurez-vous d'avoir une sauvegarde avant de manipuler vos partitions. En fait, faites deux sauvegardes.