---
title: Comment installer Kali sur une clé USB avec un démarrage EFI pur sur un Mac
  (et ajoutons la virtualisation…
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-07T07:43:31.000Z'
originalURL: https://freecodecamp.org/news/kali-installation-on-usb-stick-with-pure-efi-boot-on-a-mac-37585b7698e2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*hnsWRU9q5i3J2bZ2ECI8zw.jpeg
tags:
- name: kali
  slug: kali
- name: Linux
  slug: linux
- name: mac
  slug: mac
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment installer Kali sur une clé USB avec un démarrage EFI pur sur un
  Mac (et ajoutons la virtualisation…
seo_desc: 'By Flavio De Stefano

  This tutorial is for everyone who wants a USB stick with a full Kali installation
  to use with your Mac(s). This is not intended to perform a Live Kali installation
  with persistence.

  The problem when you perform a Kali installatio...'
---

Par Flavio De Stefano

Ce tutoriel s'adresse à tous ceux qui souhaitent une clé USB avec une **installation complète de Kali** à utiliser avec votre/vos Mac(s). Cela n'est pas destiné à effectuer une installation Live de Kali avec persistance.

**Le problème lorsque vous effectuez une installation de Kali sur une clé USB est que Kali partitionne le disque avec le système de fichiers VFAT. Mac OS ne reconnaît que les partitions HFS+ ainsi que certains fichiers nécessaires.**

Donc, vous avez besoin de :

* Votre Mac
* Une clé USB avec l'installateur ISO de Kali
* Une clé USB cible, une carte SD ou un disque dur externe SSD où vous allez installer Kali (16 Go et USB 3.0 recommandés)

_Ce tutoriel s'est largement inspiré de ce tutoriel avec les corrections appropriées pour Kali. [https://medium.com/@mmiglier/ubuntu-installation-on-usb-stick-with-pure-efi-boot-mac-compatible-469ad33645c9](https://medium.com/@mmiglier/ubuntu-installation-on-usb-stick-with-pure-efi-boot-mac-compatible-469ad33645c9)_

#### Installation Live USB

Tout d'abord, installez Kali sur une clé USB en suivant ce [tutoriel](https://docs.kali.org/downloading/kali-linux-live-usb-install). Je ne vais pas vous ennuyer sur la manière de procéder à cette étape, mais commencez ici :

```bash
$ sudo dd if={KALI_ISO.iso} of=/dev/{USB} bs=1m 
```

Lorsque vous êtes prêt, redémarrez votre Mac. Insérez vos deux clés USB, puis appuyez sur ALT et sélectionnez le **démarrage EFI** pour lancer l'installateur Live.

![Image](https://cdn-media-1.freecodecamp.org/images/herBiK1Li76oxQJ5Fl02yfTSfXGQdm5JgrCd)

L'installateur de Kali vous posera différentes questions sur votre fuseau horaire et la disposition de votre clavier.

Procédez jusqu'à ce qu'il vous demande de partitionner les disques, ici sélectionnez : **Manuel.** Ensuite, sélectionnez votre lecteur USB **cible** (où vous souhaitez installer Kali). Vous pouvez le reconnaître par divers facteurs, par exemple par sa taille. Cliquez sur **Continuer** : cela partitionnera votre lecteur.

Maintenant, revenez à nouveau au même écran et sélectionnez l'**ESPACE LIBRE** sous le lecteur USB cible. Cliquez sur **Continuer** et sélectionnez **Partitionner automatiquement l'espace libre.** Suivez l'option recommandée. Ensuite, cliquez sur **Terminer le partitionnement et écrire les changements sur le disque.**

Le processus d'installation va maintenant copier les données sur le disque. Attendez qu'il se termine (cela prendra environ 30 minutes).

#### Démarrage depuis GRUB Live

Une fois terminé, votre Mac redémarrera et vous devrez appuyer à nouveau sur **ALT**. Sélectionnez à nouveau **EFI boot**.

Ce que nous devons faire maintenant, c'est charger notre système Kali installé via **Live GRUB**, car notre système installé n'a pas de chargeur de démarrage reconnaissable par MacOS.

Une fois GRUB chargé, appuyez sur **c** pour obtenir l'interface de ligne de commande GRUB.

Maintenant, vous devez comprendre sur quel HD se trouve votre installation Kali. Pour ce faire, lorsque l'interface de commande GRUB est chargée, tapez **ls** ; éjectez votre clé USB et tapez **ls** à nouveau.

```
grub> ls
(memdisk) (hd0) (hd1) (hd1,gpt3) (hd1, gpt2) (hd1,gpt1) ...
```

Vous remarquerez qu'un **hd{X}** a disparu : c'est votre lecteur. Maintenant, vous devez trouver votre **gpt.** _Probablement c'est le **gpt2**_, mais pour être sûr, tapez :

```
grub> ls (hdX,gpt2)/boot/grub
unicode.pf2 ...
```

_Si la commande dit `unicode..` c'est le gpt correct ; essayez d'autres **gpts** sinon._ Maintenant, trouvez l'UUID de la partition et notez-le.

```
grub> ls -l (hdX},gpt{X})
        Partition hd2,gpt2: Filesystem type ext* 〈...snip...〉 UUID e86c20b9-83e1-447d-a3be-d1ddaad6c4c6 - Partition start at [...]
```

Maintenant, nous pouvons définir les paramètres pour que GRUB démarre (utilisez la touche **tab** pour utiliser l'autocomplétion) :

```
grub> set root=(hd{X},gpt{X})
grub> linux /boot/vmlinuz〈...tab here!...〉.efi.signed root=UUID=〈the UUID〉
grub> initrd /boot/initrd〈...tab here!...〉
grub> boot
```

Cela devrait démarrer votre **installation complète de Kali** en utilisant le Live GRUB. Vous pourriez différencier l'environnement Live par le mot de passe qu'il reconnaît pendant le processus de connexion.

#### Correction de la partition EFI

Une fois connecté à votre installation Kali, ouvrez le Terminal et tapez :

```bash
$ fdisk -l
```

et trouvez votre lecteur.

Maintenant, ouvrez **gdisk** (installé par défaut sur Kali) pour partitionner le lecteur (soyez très prudent ici) :

```bash
$ gdisk /dev/sd{X}
GPT fdisk (gdisk) version 1.0.1

Partition table scan:
  MBR: hybrid
  BSD: not present
  APM: not present
  GPT: present
  
Found valid GPT with hybrid MBR; using GPT.

Command (? for help):
```

Imprimez la table de partition et confirmez que la première partition est de type EF00 :

```bash
Command (? for help): p
Disk /dev/sdd: ...

[...]

Number  Start (sector)  End (sector)  Size     Code   Name
   1         2048         1050623  512.0 MiB   EF00   EFI System Partition
   
[...]
```

Maintenant, nous devons :

* supprimer cette partition EF00
* créer une nouvelle partition HFS+ à sa place

```
Command (? for help): d
Partition number (1-3): 1

Command (? for help): n
Partition number (1-128, default 1): 1

Laissez simplement les valeurs par défaut dans la phase de secteur

Current type is 'Linux filesystem'
Hex code or GUID (L to show codes, Enter = 8300): AF00
Changed type of partition to 'Apple HFS/HFS+'

Command (? for help): w

Final checks complete. About to write GPT data. THIS WILL OVERWRITE EXISTING
PARTITIONS!!

Do you want to proceed? (Y/N): Y
OK; writing new GUID partition table (GPT) to /dev/sdd.
Warning: The kernel is still using the old partition table.
The new table will be used at the next reboot.
The operation has completed successfully.
```

Maintenant, nous avons une partition HFS+ non formatée. Pour la formater, nous avons besoin de certains outils ; mais pour obtenir ces outils, nous devons ajouter la liste des sources Debian à **apt.**

```bash
$ echo "deb http://ftp.debian.org/debian unstable main contrib non-free" > /etc/apt/sources.list.d/debian.list
$ apt update
$ apt install hfsprogs
```

Nous pouvons formater cette partition :

```bash
$ mkfs.hfsplus /dev/sd{X}1 -v Kali
Initialized /dev/sd{X}1 as a 512 MB HFS Plus volume
```

Maintenant, nous devons éditer le fichier **/etc/fstab** :

```bash
$ gedit /etc/fstab
```

Cela lancera Gedit. Dans ce fichier, localisez ces lignes :

> **# /boot/efi was on /dev/sd{X}1 during installation**  
> **UUID={XXXXXXX} /boot/efi vfat defaults 0 1**

et supprimez-les.

Maintenant, démontez la partition de démarrage, en la localisant à l'aide de :

```bash
$ mount | grep /boot/efi
/dev/sd{Y}1 on /boot/efi ...
$ umount /dev/sd{Y}1
```

Ensuite, exécutez ceci pour ajouter les entrées nécessaires à votre fichier fstab :

```bash
$ echo "UUID=$(blkid -o value -s UUID /dev/sd{X}1) /boot/efi auto defaults 0 0" >> /etc/fstab
```

Maintenant, nous devons réinstaller GRUB afin qu'il puisse utiliser la partition HFS+ nouvellement formatée pour ses données EFI :

```bash
$ mkdir -p /boot/efi/EFI/Kali

$ echo "This file is required for booting" > /boot/efi/EFI/Kali/mach_kernel
$ echo "This file is required for booting" > /boot/efi/mach_kernel

$ grub-install --target x86_64-efi --boot-directory=/boot --efi-directory=/boot/efi --bootloader-id=Kali
```

Nous devons ensuite "bénir" le code du chargeur de démarrage, afin que le chargeur de démarrage Mac le démarre. Pour cela, nous avons besoin du binaire **hfsbless** qui n'est pas disponible via apt. Pas de problème, clonez simplement le dépôt et construisez :

```bash
$ cd /root
$ git clone https://github.com/detly/mactel-boot
$ cd mactel-boot
$ make
```

Puis bénissez :

```bash
./hfs-bless /boot/efi/EFI/Kali/System/Library/CoreServices/boot.efi
```

L'étape finale consiste à créer la configuration grub :

```bash
$ sed -i 's/GRUB_HIDDEN/#GRUB_HIDDEN/g' /etc/default/grub
$ sed -i 's/GRUB_TIMEOUT=10/GRUB_TIMEOUT=0.1/' /etc/default/grub
$ grub-mkconfig -o /boot/grub/grub.cfg
```

Parfait ! Maintenant, redémarrez et vous devriez voir votre clé USB dans le chargeur de démarrage Mac en appuyant sur **ALT**.

#### Virtualisation de l'USB via Virtualbox

Si vous devez un jour démarrer cette clé USB via Virtualbox (sur Mac OSX), il existe une astuce simple pour cela.

Tout d'abord, vous devez créer un disque VMDK qui pointe vers les secteurs de votre clé USB. Alors, identifions ce disque :

```
$ diskutil list
/dev/disk0 (internal):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      GUID_partition_scheme                         500.3 GB   disk0
   1:                        EFI EFI                     314.6 MB   disk0s1
   2:                 Apple_APFS Container disk1         499.3 GB   disk0s2
   
/dev/disk1 (synthesized):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      APFS Container Scheme -                      +499.3 GB   disk1
                                 Physical Store disk0s2
   1:                APFS Volume Macintosh HD            222.0 GB   disk1s1
   2:                APFS Volume Preboot                 22.4 MB    disk1s2
   3:                APFS Volume Recovery                519.9 MB   disk1s3
   4:                APFS Volume VM                      3.2 GB     disk1s4
   
/dev/disk3 (external, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      GUID_partition_scheme                        *32.0 GB    disk3
```

Dans notre cas, c'est **/dev/disk3.** Démontons avant de continuer :

```bash
$ diskutil unmountDisk /dev/disk{X}
```

Avec VirtualBox installé, exécutez :

```bash
$ sudo VBoxManage internalcommands createrawvmdk -filename ~/Kali.vmdk -rawdisk /dev/disk{X}
$ chmod 777 ~/Kali.vmdk
$ chmod 777 /dev/disk{X}
```

Parfait. Maintenant, exécutez l'interface utilisateur de Virtualbox et créez une nouvelle machine avec les paramètres suivants :

![Image](https://cdn-media-1.freecodecamp.org/images/qS3uVh4RdvQJAFVy0jmkqZhpyQQ0PGQqmoWG)

Lorsque VirtualBox vous demande un disque, pointons vers ce VMDK créé précédemment :

![Image](https://cdn-media-1.freecodecamp.org/images/AA9j6gr54XyAfs3p8Mpd6HBZLcQK1-Rhs1Ih)

Avant de démarrer la machine, allons dans Paramètres et ajustons vos comptes de processus, vidéo et mémoire.

Les choses importantes sont de définir **Activer EFI** sous **Système > Carte mère**.

![Image](https://cdn-media-1.freecodecamp.org/images/0MGTYcD-c73t74caXSThnyGVs5tAxCckTUwj)

Cela vous permettra de démarrer via EFI. Maintenant, démarrez la machine virtuelle et appuyez immédiatement sur **F12**.

Sélectionnez **Gestionnaire de maintenance de démarrage** :

![Image](https://cdn-media-1.freecodecamp.org/images/y2JWUUCp8tBEm8CXGFsPgQrAcIiSiOuESu7y)

Sélectionnez **Démarrer à partir du fichier** :

![Image](https://cdn-media-1.freecodecamp.org/images/28WvE2oTBD8B76bqCuz82lkT5NYk9EhT44Ed)

Ensuite, sélectionnez {**SATA_DRIVE} > EFI > Kali > System > Library > CoreServices > boot.efi

![Image](https://cdn-media-1.freecodecamp.org/images/b8QCTg5i89Mlv3jGiuTWtokG0jHj4YkAgGyp)

Et, voilà :

![Image](https://cdn-media-1.freecodecamp.org/images/m4XOkbkaermzUe7hS-3tZADOBUQsGE0nOUHI)

Restez à l'écoute :)