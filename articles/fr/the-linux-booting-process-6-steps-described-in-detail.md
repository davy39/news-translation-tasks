---
title: Le processus de démarrage de Linux - 6 étapes décrites en détail
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/the-linux-booting-process-6-steps-described-in-detail
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9cef740569d1a4ca34fc.jpg
tags:
- name: Linux
  slug: linux
- name: toothbrush
  slug: toothbrush
seo_title: Le processus de démarrage de Linux - 6 étapes décrites en détail
seo_desc: 'An operating system (OS) is the low-level software that manages resources,
  controls peripherals, and provides basic services to other software. In Linux, there
  are 6 distinct stages in the typical booting process.


  1. BIOS

  BIOS stands for Basic Input...'
---

Un système d'exploitation (OS) est le logiciel de bas niveau qui gère les ressources, contrôle les périphériques et fournit des services de base à d'autres logiciels. Dans Linux, il y a 6 étapes distinctes dans le processus de démarrage typique.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/LinuxBootingProcess.jpg)

### **1. BIOS**

BIOS signifie Basic Input/Output System. En termes simples, le BIOS charge et exécute le Master Boot Record (MBR) boot loader. 

Lorsque vous allumez votre ordinateur pour la première fois, le BIOS effectue d'abord quelques vérifications d'intégrité du HDD ou du SSD.

Ensuite, le BIOS recherche, charge et exécute le programme de chargeur de démarrage, qui peut être trouvé dans le Master Boot Record (MBR). Le MBR peut parfois être sur une clé USB ou un CD-ROM, comme avec une installation live de Linux.

Une fois le programme de chargeur de démarrage détecté, il est chargé en mémoire et le BIOS donne le contrôle du système à celui-ci.

### **2. MBR**

MBR signifie Master Boot Record, et est responsable du chargement et de l'exécution du chargeur de démarrage GRUB. 

Le MBR est situé dans le 1er secteur du disque amorçable, qui est généralement `/dev/hda`, ou `/dev/sda`, selon votre matériel. Le MBR contient également des informations sur GRUB, ou LILO dans les systèmes très anciens.

### **3. GRUB**

Parfois appelé GNU GRUB, qui est l'abréviation de GNU GRand Unified Bootloader, est le chargeur de démarrage typique pour la plupart des systèmes Linux modernes.

L'écran de démarrage GRUB est souvent la première chose que vous voyez lorsque vous démarrez votre ordinateur. Il dispose d'un menu simple où vous pouvez sélectionner certaines options. Si vous avez plusieurs images de noyau installées, vous pouvez utiliser votre clavier pour sélectionner celle avec laquelle vous souhaitez que votre système démarre. Par défaut, la dernière image de noyau est sélectionnée.

L'écran de démarrage attendra quelques secondes pour que vous sélectionniez une option. Si vous ne le faites pas, il chargera l'image du noyau par défaut.

Dans de nombreux systèmes, vous pouvez trouver le fichier de configuration GRUB à `/boot/grub/grub.conf` ou `/etc/grub.conf`. Voici un exemple de fichier `grub.conf` simple :

```text
#boot=/dev/sda
default=0
timeout=5
splashimage=(hd0,0)/boot/grub/splash.xpm.gz
hiddenmenu
title CentOS (2.6.18-194.el5PAE)
      root (hd0,0)
      kernel /boot/vmlinuz-2.6.18-194.el5PAE ro root=LABEL=/
      initrd /boot/initrd-2.6.18-194.el5PAE.img
```

### **4. Noyau**

Le noyau est souvent appelé le cœur de tout système d'exploitation, Linux inclus. Il a un contrôle complet sur tout dans votre système.

À cette étape du processus de démarrage, le noyau qui a été sélectionné par GRUB monte d'abord le système de fichiers racine qui est spécifié dans le fichier `grub.conf`. Ensuite, il exécute le programme `/sbin/init`, qui est toujours le premier programme à être exécuté. Vous pouvez confirmer cela avec son identifiant de processus (PID), qui devrait toujours être 1.

Le noyau établit ensuite un système de fichiers racine temporaire en utilisant le disque RAM initial (initrd) jusqu'à ce que le système de fichiers réel soit monté.

### **5. Init**

À ce stade, votre système exécute les programmes de niveau d'exécution. À un moment donné, il recherchait un fichier init, généralement trouvé à `/etc/inittab` pour décider du niveau d'exécution de Linux.

Les systèmes Linux modernes utilisent systemd pour choisir un niveau d'exécution à la place. Selon [TecMint](https://www.tecmint.com/change-runlevels-targets-in-systemd/), voici les niveaux d'exécution disponibles :

> **Niveau d'exécution 0** est associé à **poweroff.target** (et **runlevel0.target** est un lien symbolique vers **poweroff.target**).  
>   
> **Niveau d'exécution 1** est associé à **rescue.target** (et **runlevel1.target** est un lien symbolique vers **rescue.target**).  
>   
> **Niveau d'exécution 3** est émulé par **multi-user.target** (et **runlevel3.target** est un lien symbolique vers **multi-user.target**).  
>   
> **Niveau d'exécution 5** est émulé par **graphical.target** (et **runlevel5.target** est un lien symbolique vers **graphical.target**).  
>   
> **Niveau d'exécution 6** est émulé par **reboot.target** (et **runlevel6.target** est un lien symbolique vers **reboot.target**).  
>   
> **Urgence** est associé à **emergency.target**.

systemd commencera alors à exécuter les programmes de niveau d'exécution.

### **6. Programmes de niveau d'exécution**

Selon la distribution Linux que vous avez installée, vous pourrez voir différents services se lancer. Par exemple, vous pourriez voir `starting sendmail …. OK`.

Ce sont les programmes de niveau d'exécution, et ils sont exécutés à partir de différents répertoires selon votre niveau d'exécution. Chacun des 6 niveaux d'exécution décrits ci-dessus a son propre répertoire :

* Niveau d'exécution 0 – `/etc/rc0.d/`
* Niveau d'exécution 1 – `/etc/rc1.d/`
* Niveau d'exécution 2 – `/etc/rc2.d/`
* Niveau d'exécution 3 – `/etc/rc3.d/`
* Niveau d'exécution 4 – `/etc/rc4.d/`
* Niveau d'exécution 5 – `/etc/rc5.d/`
* Niveau d'exécution 6 – `/etc/rc6.d/`

Notez que l'emplacement exact de ces répertoires varie d'une distribution à l'autre.

Si vous regardez dans les différents répertoires de niveaux d'exécution, vous trouverez des programmes qui commencent par un "S" ou un "K" pour startup et kill, respectivement. Les programmes de démarrage sont exécutés pendant le démarrage du système, et les programmes de kill pendant l'arrêt.

C'est tout ce que vous devez savoir sur le processus de démarrage de Linux. Maintenant, allez-y et rendez [Tux](https://en.wikipedia.org/wiki/Tux_(mascot)) fier.