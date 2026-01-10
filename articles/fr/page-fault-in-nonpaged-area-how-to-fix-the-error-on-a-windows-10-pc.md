---
title: Erreur de page dans la zone non paginée – Comment corriger l'erreur sur un
  PC Windows 10
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-08-03T16:20:21.000Z'
originalURL: https://freecodecamp.org/news/page-fault-in-nonpaged-area-how-to-fix-the-error-on-a-windows-10-pc
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/bsod.png
tags:
- name: error
  slug: error
- name: Windows
  slug: windows
seo_title: Erreur de page dans la zone non paginée – Comment corriger l'erreur sur
  un PC Windows 10
seo_desc: "In Windows, the nonpaged area is the part of the memory that contains critical\
  \ files your computer needs to function properly. \nThose critical files are stored\
  \ in the nonpaged area so the RAM won’t switch them back and forth between itself\
  \ and the pa..."
---

Dans Windows, la zone non paginée est la partie de la mémoire qui contient les fichiers critiques dont votre ordinateur a besoin pour fonctionner correctement. 

Ces fichiers critiques sont stockés dans la zone non paginée afin que la RAM ne les échange pas constamment entre elle-même et la zone paginée.

Une fois qu'il y a un problème avec cette partie de la RAM, le système génère une erreur PAGE_FAULT_IN_NONPAGED_AREA et affiche un BSOD (écran bleu de la mort). Le code d'arrêt pour cette erreur est `0x00000050`.

![iiFbeMETDFDxyU5ASamYtf](https://www.freecodecamp.org/news/content/images/2022/08/iiFbeMETDFDxyU5ASamYtf.png)
[Source de l'image](https://www.tomshardware.com/how-to/fix-page-fault-error-windows-10)

## Ce que nous allons couvrir
- [Quelles sont les causes de l'erreur de page dans la zone non paginée](#questcequicauselapagedanslazonenonpaginee)?
- [Comment corriger l'erreur de page dans la zone non paginée](#commentcorrigerlapagedanslazonenonpaginee)
  - [Redémarrez votre ordinateur](#redemarrezvotreordinateur)
  - [Vérifiez la RAM de votre ordinateur](#verifiezlaramdevotreordinateur)
  - [Mettez à jour tous les pilotes obsolètes](#mettezajourtouslespilotesobsoletes)
  - [Effectuez une analyse SFC](#effectuezuneanalysesfc)
  - [Exécutez l'analyse du vérificateur de disque Windows](#executezlanalyseduveificateurdedisquewindows)
- [Réflexions finales](#reflexionsfinales)


## Quelles sont les causes de l'erreur de page dans la zone non paginée ?

L'erreur "page fault in nonpaged area" peut être causée par l'un ou une combinaison des problèmes suivants :

- RAM corrompue ou endommagée
- Pilote défectueux 
- Incapacité de Windows à trouver les fichiers qui devraient se trouver dans la zone non paginée


## Comment corriger l'erreur de page dans la zone non paginée

### Redémarrez votre ordinateur

Vous pouvez résoudre de nombreux problèmes Windows en redémarrant simplement votre PC. Et cette erreur n'est pas une exception. 

C'est parce que lorsque vous redémarrez votre ordinateur, les fichiers temporaires sont effacés et toutes les tâches consommant trop de RAM sont arrêtées – rendant votre ordinateur plus rapide.


### Vérifiez la RAM de votre ordinateur

Puisque ce problème est principalement causé par des problèmes de RAM et de pilotes, la première chose que je vous conseillerais de faire est de vérifier la RAM de l'ordinateur. 

Si vous ne pouvez pas le vérifier vous-même, vous devriez emmener l'ordinateur chez un ingénieur agréé.

Parfois, la solution à ce problème pourrait être de nettoyer la poussière de la RAM ou de la reconnecter.

Si la vérification de votre RAM ne parvient pas à corriger l'erreur et que vous voyez toujours le BSOD (écran bleu de la mort), [démarrez votre ordinateur en mode sans échec](https://www.freecodecamp.org/news/scanning-and-repairing-drive-how-to-fix-stuck-windows-10-pc-hard-drive/#howtofixastuckscanningandrepairingdrivewithwindowspowershell) et passez aux correctifs restants dans cet article.


### Mettez à jour tous les pilotes obsolètes

Un pilote obsolète ou corrompu est également l'une des principales causes de l'erreur de page dans la zone non paginée. Donc, rechercher les pilotes obsolètes et les mettre à jour peut résoudre le problème pour vous.

Pour mettre à jour les pilotes obsolètes de votre ordinateur, faites un clic droit sur Démarrer et sélectionnez « Gestionnaire de périphériques » :
![device-manager](https://www.freecodecamp.org/news/content/images/2022/08/device-manager.png)

Une fois que vous voyez les pilotes, un symbole d'avertissement apparaîtra à côté de tout pilote obsolète.

Développez le périphérique qui a un pilote obsolète :
![ss1](https://www.freecodecamp.org/news/content/images/2022/08/ss1.png)

Faites un clic droit sur tout pilote obsolète et sélectionnez « Mettre à jour le pilote » :
![ss2](https://www.freecodecamp.org/news/content/images/2022/08/ss2.png)

Sélectionnez « Rechercher automatiquement les pilotes » pour que Windows puisse vérifier sur Internet les nouveaux pilotes :
![ss3](https://www.freecodecamp.org/news/content/images/2022/08/ss3.png)

Si un nouveau pilote est trouvé, installez-le et redémarrez votre système informatique.

### Effectuez une analyse SFC

Dans Windows, l'analyse du vérificateur de fichiers système (SFC) vérifie votre ordinateur pour les fichiers système corrompus et les restaure. Donc, cela peut vous aider à vous débarrasser de l'erreur de page dans la zone non paginée.

Pour effectuer l'analyse SFC, vous devez ouvrir l'invite de commande en tant qu'administrateur, puis taper ` sfc/scannow` et appuyer sur `ENTRÉE` :
![ss4](https://www.freecodecamp.org/news/content/images/2022/08/ss4.png)

### Exécutez l'analyse du vérificateur de disque Windows

Recherchez CMD et sélectionnez « Exécuter en tant qu'administrateur » à droite :
![ss5](https://www.freecodecamp.org/news/content/images/2022/08/ss5.png)

Dans l'invite de commande, entrez `chkdsk C: /f /r` et appuyez sur `ENTRÉE`.

Si vous obtenez un message indiquant « Impossible d'exécuter car le volume est utilisé par un autre processus », tapez `y` et appuyez sur ENTRÉE pour que l'analyse puisse s'exécuter lors du prochain redémarrage du système.
![ss6](https://www.freecodecamp.org/news/content/images/2022/08/ss6.png)

**N.B.** : Cette analyse prend beaucoup de temps, surtout si vous avez un disque plein ou lorsqu'elle est effectuée au démarrage. Donc, soyez patient.


## Réflexions finales

Cet article vous a montré ce qu'est l'erreur de page dans la zone non paginée, ses causes et comment la corriger.

J'espère que les solutions discutées dans cet article vous aideront à corriger le problème et à vous débarrasser du BSOD. 

Si tous les correctifs échouent à résoudre le problème pour vous, alors la dernière solution est de réinitialiser votre PC.