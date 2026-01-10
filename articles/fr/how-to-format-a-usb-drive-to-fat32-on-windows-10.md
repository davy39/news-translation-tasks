---
title: Comment formater une clé USB en FAT32 sur Windows 10
subtitle: ''
author: Kristofer Koishigawa
co_authors: []
series: null
date: '2020-10-16T06:45:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-format-a-usb-drive-to-fat32-on-windows-10
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5fa4f2e749c47664ed81ae62.jpg
tags:
- name: storage
  slug: storage
- name: usb
  slug: usb
- name: Windows
  slug: windows
- name: Windows 10
  slug: windows-10
seo_title: Comment formater une clé USB en FAT32 sur Windows 10
seo_desc: 'If you need to format a USB flash drive, HDD, SDD, or some other form of
  storage to FAT32, you''ve come to the right place.

  In this article we''ll go over what a file system is, the FAT32 standard, and several
  ways to format a storage device to FAT32 o...'
---

Si vous devez formater une clé USB, un disque dur, un SSD ou une autre forme de stockage en FAT32, vous êtes au bon endroit.

Dans cet article, nous allons aborder ce qu'est un système de fichiers, la norme FAT32 et plusieurs méthodes pour formater un périphérique de stockage en FAT32 sur Windows 10.

## Qu'est-ce qu'un système de fichiers ?

Un système de fichiers est une méthode standardisée d'organisation des données sur un périphérique de stockage informatique comme une clé USB ou un disque dur.

Un système de fichiers divise un périphérique de stockage en compartiments virtuels, presque comme un mur de boîtes aux lettres, et suit toutes les informations stockées dans chaque boîte.

Certains des formats de systèmes de fichiers les plus courants pour les périphériques de stockage portables sont FAT32, NTFS et ExFAT.

## FAT32 comparé à d'autres formats

Parmi ces trois formats courants, FAT32 est le plus ancien et le plus largement supporté. Tous les principaux systèmes d'exploitation vous permettront de lire et d'écrire sur une clé USB formatée en FAT32.

En revanche, macOS ne peut que lire les disques NTFS, et vous devriez installer un logiciel tiers pour écrire sur le disque.

Cependant, bien que FAT32 soit bien supporté, sa taille maximale de disque et de fichier est sévèrement limitée par rapport aux formats plus récents comme NTFS et ExFAT :

|  | Taille max du disque | Taille max du fichier | Windows | macOS | Linux |
| --- | --- | --- | --- | --- | --- | 
| FAT32 | 32 Go (Windows), jusqu'à 16 To (autres OS) | 4 Go | Lecture/Écriture |  Lecture/Écriture |  Lecture/Écriture |
| NTFS | 8 Po* | 16 Eo** | Lecture/Écriture |  Lecture |  Lecture/Écriture |
| ExFAT | 128 Po* | 16 Eo** |  Lecture/Écriture |  Lecture/Écriture |  Lecture/Écriture |
\* 1 pétaoctet équivaut à environ 1 mille téraoctets
\*\* 1 exaoctet équivaut à environ 1 million de téraoctets

Notez que la taille maximale de disque et de fichier de NTFS et ExFAT est si grande qu'il n'y a pratiquement pas de limite. (Mais ce serait bien d'avoir une clé USB de 128 Po, n'est-ce pas ?)

D'autre part, la taille maximale de fichier de 4 Go de FAT32 est presque insignifiante maintenant que les téléphones peuvent enregistrer des vidéos 4K. De plus, il est un peu plus difficile de formater un disque de plus de 32 Go en FAT32 sur Windows 10.

De nos jours, la seule raison pour laquelle vous choisirez de formater un disque en FAT32 est la compatibilité. Par exemple, si vous devez démarrer un ancien ordinateur, peut-être avec un système d'exploitation différent, et sauvegarder certains de ses fichiers. Mais vous devrez vous assurer qu'aucun de ces fichiers ne dépasse 4 Go.

Si vous êtes sûr de vouloir utiliser FAT32, voici comment formater un disque de stockage sur Windows 10.

**Note importante :** Avant de formater un disque, assurez-vous de sauvegarder tous vos fichiers importants. En fait, faites deux sauvegardes et conservez-en une sur un service distant comme Google Drive ou Dropbox.

Le formatage d'un disque supprimera toutes les données qui s'y trouvent actuellement.

## Comment utiliser l'Explorateur de fichiers Windows pour formater une clé USB en FAT32

Une rapide note sur cette méthode : elle ne fonctionne que sur les clés USB de moins de 32 Go. Si votre clé USB est plus grande que 32 Go, consultez l'une des méthodes suivantes.

Cela étant dit, branchez votre clé USB sur votre ordinateur et ouvrez l'Explorateur de fichiers Windows.

Ensuite, faites un clic droit sur le lecteur dans le volet de gauche de la fenêtre de l'Explorateur de fichiers et cliquez sur "Formater" :

![Sélection de l'option "Formater" dans l'Explorateur de fichiers Windows](https://www.freecodecamp.org/news/content/images/2020/11/windows-file-explorer-format.jpg)

Dans la fenêtre qui s'ouvre, assurez-vous que "FAT32" est sélectionné. Vous pouvez également renommer la clé USB comme vous le souhaitez :

![La fenêtre contextuelle de formatage de Windows](https://www.freecodecamp.org/news/content/images/2020/11/windows-format-window.jpg)

Vous pouvez laisser les autres options par défaut. Cliquez simplement sur Démarrer pour formater votre disque.

Une fois terminé, votre clé USB devrait être formatée pour utiliser le système de fichiers FAT32.

Pour vérifier cela, ouvrez l'Explorateur de fichiers, faites un clic droit sur votre clé USB et cliquez sur "Propriétés".

Une fenêtre s'ouvrira et vous devriez voir que le système de fichiers est maintenant FAT32 :

![Une fenêtre de propriétés de lecteur ouverte pour vérifier le format](https://www.freecodecamp.org/news/content/images/2020/11/drive-properties.jpg)

## Comment utiliser Rufus pour formater une clé USB en FAT32

Si votre clé USB est plus grande que 32 Go, vous devrez utiliser un programme tiers comme [Rufus](https://rufus.ie/) pour la formater.

Il existe de nombreux autres programmes qui peuvent formater des clés USB, mais Rufus est très petit et portable. Cela signifie que vous pouvez mettre Rufus directement sur une clé USB, la brancher sur n'importe quel ordinateur Windows et formater d'autres disques en déplacement.

Après avoir téléchargé Rufus, double-cliquez sur le fichier `.exe` pour démarrer l'application.

Assurez-vous que votre clé USB est sélectionnée. Ensuite, cliquez sur le menu déroulant "Sélection de démarrage" et sélectionnez "Non démarrable" :

![Sélection de l'option "Non démarrable" dans Rufus](https://www.freecodecamp.org/news/content/images/2020/11/rufus-boot-selection.jpg)

Ensuite, cliquez sur le menu déroulant "Système de fichiers" et sélectionnez "FAT32".

Vous pouvez également renommer votre clé USB sous "Étiquette de volume" :

![Sélection du système de fichiers et modification de l'étiquette de volume dans Rufus](https://www.freecodecamp.org/news/content/images/2020/11/rufus-file-system-and-volume-label.jpg)

Ensuite, cliquez sur le bouton "Démarrer" pour formater votre disque. Après quelques secondes, il sera formaté en FAT32.

## Comment utiliser PowerShell pour formater une clé USB en FAT32

Bien que cette méthode fonctionne avec des disques de plus de 32 Go, elle est vraiment lente – même le formatage d'un disque de 32 Go peut prendre jusqu'à une heure selon votre ordinateur.

Mais, si vous ne pouvez pas utiliser les deux méthodes précédentes pour une raison quelconque, cela fonctionnera en cas de besoin.

Tout d'abord, cliquez sur la barre de recherche Windows et tapez "powershell". Ensuite, cliquez sur "Exécuter en tant qu'administrateur" pour lancer PowerShell avec des privilèges élevés :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/powershell-as-administrator.jpg)

Dans le terminal PowerShell, entrez la commande suivante :

`format /FS:FAT32 LETTRE_DU_LECTEUR:`

Utilisez l'Explorateur de fichiers pour vérifier la lettre de votre lecteur. La lettre de mon lecteur était D, donc j'ai entré `format /FS:FAT32 D:`.

Appuyez sur Entrée, assurez-vous que votre clé USB est branchée, et appuyez à nouveau sur la touche Entrée pour démarrer le processus :

![Utilisation de PowerShell pour exécuter la commande de formatage](https://www.freecodecamp.org/news/content/images/2020/11/image-33.png)

Ensuite, allez faire des courses ou autre chose – cela prendra un certain temps.

Une fois la commande `format` terminée, votre disque devrait être formaté en FAT32.

## En conclusion

Maintenant, vous devriez être en mesure de formater une clé USB de n'importe quelle taille en FAT32 sur Windows 10. Et avec juste une petite modification, l'une de ces méthodes peut être utilisée pour formater votre disque dans un autre système de fichiers comme NTFS ou ExFAT.

Maintenant, allez-y et formatez toutes vos clés USB. (Mais seulement après avoir sauvegardé tout ce qui est important !)

Cela vous a-t-il été utile ? Connaissez-vous une meilleure méthode ? [Tweetez](https://twitter.com/kriskoishigawa) moi et faites-moi savoir comment vous formatez les choses sur Windows 10.