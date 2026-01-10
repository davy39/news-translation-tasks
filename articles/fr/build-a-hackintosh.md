---
title: Comment construire un Hackintosh - Installer MacOS Big Sur sur un PC en utilisant
  OpenCore
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2021-06-03T18:07:17.000Z'
originalURL: https://freecodecamp.org/news/build-a-hackintosh
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/hackintosh.png
tags:
- name: hackintosh
  slug: hackintosh
- name: youtube
  slug: youtube
seo_title: Comment construire un Hackintosh - Installer MacOS Big Sur sur un PC en
  utilisant OpenCore
seo_desc: 'A Hackintosh is a non-Mac computer system, made with PC parts, that runs
  the macOS operating system. In this tutorial, you will learn how to create a Hackintosh.

  You will learn how to install macOS Big Sur (or any other version of macOS) using
  OpenCo...'
---

Un Hackintosh est un système informatique non-Mac, fabriqué avec des pièces de PC, qui exécute le système d'exploitation macOS. Dans ce tutoriel, vous apprendrez à créer un Hackintosh.

Vous apprendrez à installer macOS Big Sur (ou toute autre version de macOS) en utilisant OpenCore.

Le principal avantage d'un Hackintosh par rapport à un ordinateur Macintosh officiel est qu'il est BEAUCOUP moins cher. J'ai créé un ordinateur Hackintosh qui correspond aux spécifications du Mac Pro pour environ 1/3 du prix d'un Mac Pro. Certaines personnes ont réussi à créer un Hackintosh pour moins de 100 $.

Ce tutoriel se concentrera principalement sur l'installation de macOS sur votre matériel. J'ai également créé une version vidéo qui montre comment construire une machine complète puis installer macOS dessus.

La vidéo montre comment utiliser un ordinateur avec macOS pour créer un installateur macOS pour votre Hackintosh. Dans ce tutoriel écrit, vous apprendrez à créer l'installateur macOS en utilisant macOS ou Windows.

Vous pouvez regarder la vidéo ici :

%[https://www.youtube.com/watch?v=Gaosub7FRf4]

Il n'est pas illégal de créer un Hackintosh pour un usage personnel, mais cela va à l'encontre de l'accord de licence de l'utilisateur final d'Apple. Donc, ne prévoyez pas d'emmener cela dans un Apple Store pour réparation. Et dans de nombreux endroits, il est illégal de vendre un Hackintosh.

## Le Matériel

De nombreuses pièces d'ordinateur fonctionnent pour les Hackintoshes. Mais certaines ne fonctionnent pas. [Consultez ce site web](https://dortania.github.io/OpenCore-Install-Guide/macos-limits.html) pour voir quel matériel est compatible avec un Hackintosh.

Dans la vidéo ci-dessus, je démontre étape par étape comment construire un ordinateur qui fonctionnera comme un Hackintosh. Dans la description de la vidéo se trouve une liste des pièces spécifiques que j'ai utilisées.

Si vous voulez être prudent, vous pouvez utiliser les mêmes pièces que celles que j'ai utilisées dans ma construction, mais il est possible d'installer macOS sur une grande variété de matériel.

## Téléchargement de MacOS et création d'un installateur USB bootable

Pour cette étape, vous aurez besoin d'une clé USB d'au moins 16 Go. Le processus est différent selon que vous configurez l'installateur USB bootable en utilisant macOS ou Windows. Le processus est beaucoup plus simple à faire sur macOS, mais il est toujours possible sur Windows.

Si possible, trouvez une machine Mac pour créer l'installateur USB bootable. Mais je vais couvrir les étapes pour macOS et Windows.

### Utilisation de MacOS pour créer l'installateur MacOS

Il y a quelques programmes dont vous aurez besoin pendant ce processus, commencez donc par les télécharger. Voici les liens pour ce dont vous aurez besoin, suivis des instructions de téléchargement.

* [ProperTree](https://github.com/corpnewt/ProperTree) - Cliquez sur le bouton "Code", puis "Download Zip"
* [MountEFI](https://github.com/corpnewt/MountEFI) - Cliquez sur le bouton "Code", puis "Download Zip"
* [OC_GEN-X](https://github.com/Pavo-IM/OC-Gen-X/releases) - Téléchargez le fichier zip de la version la plus récente.

Ouvrez l'App Store sur macOS. Recherchez "Big Sur". Cliquez sur "Get", puis "Download".

![Image](https://www.freecodecamp.org/news/content/images/2021/05/image-69.png)

Formatez votre clé USB en utilisant l'Utilitaire de disque. Pour accéder à l'Utilitaire de disque, cliquez simplement sur la loupe et tapez "Disk Utility".

Une fois l'Utilitaire de disque ouvert, assurez-vous que la vue est réglée pour afficher tous les appareils.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/image-70.png)

Cliquez sur la clé USB, puis cliquez sur "Erase" dans le menu supérieur.

Nommez le disque "MyVolume". Assurez-vous que le format est Mac OS Extended (Journaled) et que le schéma est GUID Partition Map. Puis cliquez sur le bouton "Erase".

![Image](https://www.freecodecamp.org/news/content/images/2021/05/image-71.png)

Après que la clé USB soit préparée, ouvrez le Terminal dans MacOS. Vous utiliserez une commande dans le terminal pour transformer la clé USB en un installateur bootable pour macOS.

Si vous installez macOS Big Sur, tapez la commande suivante :

`sudo /Applications/Install\ macOS\ Big\ Sur.app/Contents/Resources/createinstallmedia --volume /Volumes/MyVolume`

Si vous installez une version différente de macOS, vous pouvez trouver [la commande pour la version que vous installez ici](https://support.apple.com/en-us/HT201372).

Vous devrez attendre un peu pour que cela s'installe. Une fois cela terminé, ouvrez le programme OC_Gen-X que vous avez téléchargé précédemment.

Pour ouvrir le programme, vous devrez faire un clic droit sur l'icône, sélectionner "open", puis sélectionner "open" à nouveau.

C'est un assistant logiciel qui nous aide à préparer facilement ce dont nous avons besoin pour installer MacOS sur notre configuration matérielle particulière. Il ira chercher tout ce dont nous avons besoin sauf les SSDTs et les placera dans un dossier pour vous.

Vous pouvez également faire cela avec une méthode plus manuelle en suivant le [Guide d'installation d'OpenCore](https://dortania.github.io/OpenCore-Install-Guide/installer-guide/mac-install.html#downloading-macos-modern-os). Mais ce programme simplifie beaucoup les choses pour nous et il n'est pas disponible pour Windows.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/image-72.png)

Sur cet premier écran, sous "System Type", choisissez le type de processeur que vous avez. Consultez la documentation de votre processeur pour déterminer le nom de la microarchitecture qu'il utilise. Il est très important de bien faire cela.

Le type de processeur que j'ai utilisé est "Coffee Lake".

Pour la plupart des onglets de ce programme, vous pouvez garder les paramètres par défaut.

Sous "Graphics", sélectionnez "WhateverGreen" et sous "Audio", sélectionnez "AppleALC". Sous "Ethernet", sélectionnez "IntelMausi". Ce sont des options très couramment utilisées, mais il y a une petite chance que vos paramètres soient différents selon votre matériel et votre cas d'utilisation spécifique.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/image-73.png)

Le SMBIOS est important et vous devrez spécifier le bon modèle de système sur cet onglet. Pour ma configuration, j'ai utilisé "iMac19,1", mais cela pourrait être différent pour vous si vous utilisez un processeur différent ou une version différente du système d'exploitation.

Pour déterminer quel modèle de système utiliser, allez dans le [Guide d'installation d'Open Core](https://dortania.github.io/OpenCore-Install-Guide/config.plist/coffee-lake.html).

Sélectionnez la section sur le côté gauche pour votre type de processeur (dans mon cas, c'est "Coffee Lake"). Ensuite, trouvez le titre "PlatformInfo". Faites défiler un peu et vous verrez un tableau avec le SMBIOS à utiliser.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/image-74.png)

Après avoir sélectionné le modèle de système approprié, cliquez sur le bouton "Generate EFI" en bas.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/image-76.png)

Un dossier EFI a maintenant été créé sur votre bureau. Nous allons maintenant apporter quelques modifications au contenu.

Vous devrez obtenir les fichiers SSDT. Cela dépend de votre processeur.

Vous pouvez trouver la liste des SSDT exacts dont vous avez besoin [à ce lien](https://dortania.github.io/Getting-Started-With-ACPI/ssdt-methods/ssdt-prebuilt.html). Il suffit de sélectionner votre type de processeur et de télécharger chacun des SSDT requis.

Voici les liens pour les SSDT nécessaires à mon système Coffee Lake.

* [SSDT-PLUG-DRTNIA](https://github.com/dortania/Getting-Started-With-ACPI/blob/master/extra-files/compiled/SSDT-PLUG-DRTNIA.aml)
* [SSDT-EC-USBX-DESKTOP](https://github.com/dortania/Getting-Started-With-ACPI/blob/master/extra-files/compiled/SSDT-EC-USBX-DESKTOP.aml)
* [SSDT-AWAC](https://github.com/dortania/Getting-Started-With-ACPI/blob/master/extra-files/compiled/SSDT-AWAC.aml)
* [SSDT-PMC](https://github.com/dortania/Getting-Started-With-ACPI/blob/master/extra-files/compiled/SSDT-PMC.aml)

Une fois tous ces fichiers téléchargés, déplacez-les dans votre dossier EFI. Ils doivent être déplacés dans ce sous-dossier : `EFI/ACPI/OC`

Maintenant, vous allez utiliser le programme MountEFI téléchargé précédemment pour monter la partition EFI cachée sur la clé USB.

Faites un clic droit sur `MountEFI.command` et cliquez sur "open", puis "open" à nouveau.

Sélectionnez votre clé USB. Elle devrait avoir un nom comme "Install macOS Big Sur" puisque nous en avons fait un installateur bootable pour MacOS. Dans la capture d'écran ci-dessous, c'est l'option 2.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/image-77.png)

Vous avez maintenant une partition EFI montée et un dossier EFI provenant de OC Gen-X. Glissez le dossier EFI dans la partition EFI.

Ouvrez `ProperTree.command` que vous avez téléchargé précédemment. Comme avant, vous pouvez l'ouvrir en faisant un clic droit et en sélectionnant "open".

Une fois ProperTree en cours d'exécution, allez dans "File -> Open". Sélectionnez la partition EFI, puis le dossier "OC", puis ouvrez le fichier "config.plist".

La première chose que nous devons faire est d'injecter tous les fichiers du dossier EFI dans le fichier "config.plist".

Alors allez dans "File", puis sélectionnez "OC Snapshot". Assurez-vous d'être sur la partition EFI. Allez dans le dossier "EFI", puis le dossier "OC". Et cliquez sur le bouton "Choose".

Une boîte de dialogue peut apparaître ici concernant la version à utiliser. Si cela se produit, cliquez sur "Yes".

Maintenant, retournez dans "File", puis sélectionnez "OC Clean Snapshot" et sélectionnez "Choose".

Le programme OC Gen-X a aidé à simplifier toute la configuration requise. À ce stade, vous devriez vérifier que tout est configuré correctement selon le guide d'installation officiel.

[Voici le guide pour Coffee Lake](https://dortania.github.io/OpenCore-Install-Guide/config.plist/comet-lake.html#starting-point). Si vous utilisez un type de processeur différent, sélectionnez simplement votre type dans le menu de gauche.

Vous pouvez vérifier que les quirks sont correctement définis dans le fichier `config.plist`. Ils devraient tous être corrects.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/image-78.png)

Vous devez effectuer une configuration supplémentaire dans le fichier config.plist pour vous assurer que les graphiques intégrés fonctionnent. Trouvez la section "DeviceProperties", puis copiez les caractères suivants à ajouter.

`PciRoot(0x0)/Pci(0x2,0x0)`

Notez que si votre processeur n'est pas Coffee Lake, la chose exacte que vous devez ajouter sous "DeviceProperties" pourrait être différente. Recherchez "Device Properties" dans le guide OpenCore pour votre type de processeur pour confirmer ce qu'il faut ajouter sous "DeviceProperties" dans le fichier `config.plist`.

Sous "DeviceProperties", cliquez sur "Add". Puis faites un clic droit et choisissez "New child under 'Add' (+)".

![Image](https://www.freecodecamp.org/news/content/images/2021/05/image-79.png)

![Image](https://www.freecodecamp.org/news/content/images/2021/05/image-80.png)

Double-cliquez où il est écrit "New String" et collez simplement le texte dans le champ et appuyez sur Entrée. Puis sélectionnez dans la colonne suivante où il est écrit "String" et assurez-vous qu'il est défini sur "Dictionary".

![Image](https://www.freecodecamp.org/news/content/images/2021/05/image-81.png)

Ensuite, nous devons ajouter plus d'enfants en dessous et cela devrait finalement ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/05/image-82.png)

Ci-dessous se trouve le texte de l'image ci-dessus que vous devez ajouter (si votre système est Coffee Lake).

| Name | Type | Value |
|----|----|----|
| AAPL,ig-platform-id | Data | 07009B3E |
| framebuffer-patch-enable | Data | 01000000 |
| framebuffer-stolenmem | Data | 00003001 |

Maintenant, dans le fichier `config.plist`, trouvez la section NVRAM.

Mettez à jour le "boot-args" pour que le texte soit "-v keepsyms=1 debug=0x100 alcid=1".

![Image](https://www.freecodecamp.org/news/content/images/2021/05/image-83.png)

Maintenant, nous allons changer la langue en anglais. Donc, à côté de "prev-lang:kbd", changez "data" en "String" et définissez la valeur sur "en-US:0" et appuyez sur Entrée.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/image-84.png)

Si vous voulez une langue différente, allez simplement à [ce lien](https://github.com/acidanthera/OpenCorePkg/blob/master/Utilities/AppleKeyboardLayouts/AppleKeyboardLayouts.txt) pour trouver le code de langue à utiliser.

Le fichier config.plist est maintenant terminé. Donc, allez dans "file", puis "save". Vous avez maintenant complètement terminé la configuration du lecteur bootable. Donc, éjectez simplement le lecteur, et vous pouvez le brancher sur votre Hackintosh.

Passez la section suivante sur Windows et allez à la section "Configuration du BIOS".

### Utilisation de Windows pour créer l'installateur macOS

La première étape pour créer un installateur macOS sur Windows est de télécharger [OpenCore](https://github.com/acidanthera/opencorepkg/releases). Assurez-vous de télécharger le fichier zip de la version la plus récente.

Décompressez OpenCore, puis allez dans `/Utilities/macrecovery/`. Ensuite, copiez le chemin du dossier pour le dossier `macrecovery` :

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-10.png)
_Source : [OpenCore Docs](https://dortania.github.io/OpenCore-Install-Guide/installer-guide/winblows-install.html#downloading-macos)_

Ouvrez une invite de commande et changez de répertoire pour le dossier `macrecovery` que vous venez de copier en utilisant la commande `cd [PASTE_FOLDER_NAME]`.

Cela devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-12.png)
_Source : [OpenCore Docs](https://dortania.github.io/OpenCore-Install-Guide/installer-guide/winblows-install.html#downloading-macos)_

Maintenant, dans l'invite de commande, exécutez l'une des commandes suivantes en fonction de la version de macOS que vous souhaitez. Si vous n'avez pas déjà Python, vous devrez [l'installer d'abord](https://www.python.org/downloads/).

```sh
# Mojave(10.14)
python macrecovery.py -b Mac-7BA5B2DFE22DDD8C -m 00000000000KXPG00 download

# Catalina(10.15)
python macrecovery.py -b Mac-00BE6ED71E35EB86 -m 00000000000000000 download

# Big Sur(11)
python macrecovery.py -b Mac-E43C1C25D4880AD6 -m 00000000000000000 download
```

Cela prendra un certain temps, mais une fois terminé, vous devriez obtenir soit des fichiers BaseSystem, soit RecoveryImage :

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-13.png)
_Source : [OpenCore Docs](https://dortania.github.io/OpenCore-Install-Guide/installer-guide/winblows-install.html#downloading-macos)_

Ouvrez maintenant la Gestion des disques et formatez la clé USB en FAT32. Suivez ces étapes de la [documentation OpenCore](https://dortania.github.io/OpenCore-Install-Guide/installer-guide/winblows-install.html#downloading-macos) :

1. Faites un clic droit sur le bouton Démarrer de votre barre des tâches et sélectionnez Gestion des disques.
2. Vous devriez voir toutes vos partitions et disques. Dans la moitié inférieure, vous verrez vos appareils. Trouvez votre clé USB.
3. Vous devrez formater la clé USB pour qu'elle ait une partition FAT32.
4. Si vous avez plusieurs partitions sur la clé USB, faites un clic droit sur chaque partition et cliquez sur Supprimer le volume pour votre clé USB.
5. Faites un clic droit sur l'espace non alloué et créez un nouveau volume simple. Assurez-vous qu'il est en FAT32 et d'au moins un ou deux gigaoctets. Nommez-le "EFI".
6. Sinon, faites un clic droit sur la partition de la clé USB et cliquez sur Formater et définissez-le sur FAT32.

![Image](https://dortania.github.io/OpenCore-Install-Guide/assets/img/DiskManagement.aac12f25.jpg)
_Source : [OpenCore Docs](https://dortania.github.io/OpenCore-Install-Guide/installer-guide/winblows-install.html#downloading-macos)_

Ensuite, allez à la racine de cette clé USB et créez un dossier appelé `com.apple.recovery.boot`. Ensuite, déplacez les fichiers BaseSystem ou RecoveryImage téléchargés. Veuillez vous assurer de copier à la fois les fichiers .dmg et .chunklist dans ce dossier :

![Image](https://dortania.github.io/OpenCore-Install-Guide/assets/img/com-recovery.805dc41f.png)
_Source : [OpenCore Docs](https://dortania.github.io/OpenCore-Install-Guide/installer-guide/winblows-install.html#downloading-macos)_

Maintenant, prenez OpenCorePkg que vous avez téléchargé précédemment et ouvrez-le :

![Image](https://dortania.github.io/OpenCore-Install-Guide/assets/img/base-oc-folder.9a1a058a.png)
_Source : [OpenCore Docs](https://dortania.github.io/OpenCore-Install-Guide/installer-guide/winblows-install.html#downloading-macos)_

Ici, nous voyons les dossiers IA32 (CPU 32 bits) et X64 (CPU 64 bits), choisissez celui qui est le plus approprié pour votre matériel et ouvrez-le. Ensuite, prenez le dossier EFI à l'intérieur et placez-le à la racine de la clé USB à côté de com.apple.recovery.boot. Une fois terminé, cela devrait ressembler à ceci :

![Image](https://dortania.github.io/OpenCore-Install-Guide/assets/img/com-efi-done.a6fb730e.png)
_Source : [OpenCore Docs](https://dortania.github.io/OpenCore-Install-Guide/installer-guide/winblows-install.html#downloading-macos)_

À ce stade, vous devrez continuer à configurer votre dossier EFI. En raison de la complexité de cette étape et de toutes les différentes options possibles en fonction de votre configuration, vous devez suivre la documentation officielle pour les prochaines étapes.

Voici les liens vers les instructions pour les prochaines étapes lors de l'utilisation de Windows pour créer l'installateur USB bootable. Notez que les captures d'écran dans la documentation montrent un mac, mais les étapes s'appliquent également à Windows. Pour la configuration en utilisant un mac, vous n'avez pas à passer par ces étapes car il y a un assistant qui les fait toutes automatiquement.

[Ajout des fichiers de base OpenCore](https://dortania.github.io/OpenCore-Install-Guide/installer-guide/opencore-efi.html)

[Collecte des fichiers](https://dortania.github.io/OpenCore-Install-Guide/ktext.html#firmware-drivers)

[Prise en main de l'ACPI](https://dortania.github.io/Getting-Started-With-ACPI/)

## Configuration du BIOS

Je vais vous montrer comment j'ai configuré mon BIOS pour mon Hackintosh. Le logiciel du BIOS est spécifique à ma carte mère et le vôtre peut être un peu différent. Si le vôtre est différent, faites de votre mieux pour trouver des paramètres équivalents dans votre logiciel. Notez que les paramètres du BIOS sont faciles à expérimenter et vous n'avez pas besoin d'avoir tous les mêmes paramètres que moi pour que tout fonctionne.

Démarrez l'ordinateur, puis appuyez sur la touche "Delete" pour accéder au BIOS.

La plupart des paramètres peuvent être laissés par défaut. Voici les paramètres qui doivent être mis à jour :

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-14.png)

Dans Avancé, "Above 4G Decoding" doit être Activé.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-15.png)

Dans Avancé, puis dans Configuration du port série, mettez "Serial Port" sur Off.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-16.png)

Dans Avancé, puis dans Configuration USB, définissez "XHCI Hand-off" sur Activé.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-17.png)

Dans Boot, puis dans Configuration de Boot, définissez "Fast Boot" sur Désactivé.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-18.png)

Dans Boot, puis dans Secure Boot, définissez "OS Type" sur Windows UEFI mode.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-19.png)

La dernière chose que vous devez faire est d'aller dans Boot > Secure Boot > Key Management. Ensuite, sélectionnez "Clear Secure Boot Keys".

Maintenant, allez dans Exit et sélectionnez "Save Changes & Reset".

## Configuration de MacOS

Après le redémarrage de l'ordinateur, appuyez sur F12 pour accéder au menu de démarrage. Choisissez "Install MacOS Big Sur (External)".

> Les prochaines captures d'écran sont un peu floues car je filmais mon moniteur et n'ai pas fait la mise au point correctement. Désolé pour cela.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-21.png)

Après le chargement, l'écran des utilitaires macOS devrait apparaître. Sélectionnez "Disk Utility".

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-22.png)

Cliquez sur le menu déroulant vers le haut et cliquez sur "Show All Devices". Ensuite, sélectionnez votre disque dur et cliquez sur "Erase" en haut.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-23.png)

Vous pouvez nommer le disque comme vous le souhaitez. Pour le format, assurez-vous de choisir "Mac OS Extended (Journaled) et pour le schéma, choisissez "GUID Partition Map".

Après que le disque soit effacé, fermez l'Utilitaire de disque et sélectionnez "Install MacOS Big Sur". Vous devrez choisir le disque dur que vous venez de formater. Ensuite, vous devrez attendre pendant que macOS est installé.

L'ordinateur devrait redémarrer dans le menu de démarrage. Sélectionnez "MacOS Installer".

À ce stade, vous allez configurer l'ordinateur comme vous le feriez pour un tout nouvel ordinateur Mac. Après la configuration, macOS Big Sur se chargera.

Il reste une chose à faire. Vous devez copier le dossier EFI de la partition EFI cachée sur la clé USB vers la partition EFI du disque dur sur lequel vous avez installé macOS.

Sur le nouveau Hackintosh, allez dans le navigateur web et [téléchargez MountEFI](https://github.com/corpnewt/MountEFI). C'est le même programme que vous avez utilisé auparavant, si vous avez créé l'installateur sur un mac. Après avoir cliqué sur le lien, cliquez sur le bouton "Code", puis "Download ZIP".

Allez dans le dossier des téléchargements et faites un clic droit sur `MountEFI.command` et ouvrez-le.

Utilisez le programme pour monter les partitions EFI du disque dur de votre Hackintosh et de la clé USB appelée "Install MacOS Big Sur". Sélectionnez d'abord l'une, puis l'autre.

Après que les deux partitions soient montées, vous devrez copier le dossier EFI de la partition EFI de la clé USB vers la partition EFI du disque dur.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-24.png)

À ce stade, vous pouvez redémarrer l'ordinateur et retirer la clé USB. Le Hackintosh est complet !