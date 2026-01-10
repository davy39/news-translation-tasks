---
title: Comment forcer la suppression d'un fichier - Invite de commande Windows cmd
  delete
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-04-08T07:11:26.000Z'
originalURL: https://freecodecamp.org/news/how-to-force-delete-a-file-windows-command-prompt-cmd-delete
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/trash-97586_1280.png
tags:
- name: command line
  slug: command-line
- name: Windows
  slug: windows
- name: Windows 10
  slug: windows-10
seo_title: Comment forcer la suppression d'un fichier - Invite de commande Windows
  cmd delete
seo_desc: 'On a Windows computer, you might want to delete files to free up disk space,
  or because you don''t want the file(s) on your computer anymore.

  But sometimes, it seems impossible to delete a file for various reasons. These include
  the file being open in...'
---

Sur un ordinateur Windows, vous pouvez vouloir supprimer des fichiers pour libérer de l'espace disque, ou parce que vous ne voulez plus du ou des fichiers sur votre ordinateur.

Mais parfois, il semble impossible de supprimer un fichier pour diverses raisons. Cela inclut le fichier ouvert dans un autre programme, le manque d'accès en écriture, une attaque de malware, une corbeille corrompue ou pleine, le fichier est un fichier système, et bien d'autres.

Dans cet article, je vais vous montrer comment forcer la suppression d'un fichier avec l'invite de commande afin que vous puissiez vous débarrasser d'un fichier indésirable et tenace.

## Comment forcer la suppression d'un fichier avec l'invite de commande Windows

Les étapes suivantes vous aideront à forcer la suppression d'un fichier avec la commande `del`.

**Étape 1** : Ouvrez l'invite de commande en cliquant sur Démarrer (ou en appuyant sur la touche du logo Windows de votre clavier), recherchez "cmd", puis appuyez sur `Entrée` :

![openCMD](https://www.freecodecamp.org/news/content/images/2022/04/openCMD.jpg)
 
**Étape 2** : Rendez-vous dans le dossier contenant le fichier, cliquez sur la barre d'adresse du dossier et copiez l'adresse :

![ss1](https://www.freecodecamp.org/news/content/images/2022/04/ss1.png)

**Étape 3** : Dans l'invite de commande, tapez `del`, faites un clic droit pour coller l'adresse du dossier, et ajoutez le nom du fichier avec son extension (`.html`, `.txt`, `.py`, etc.).

Cela ressemblera à `del C:\Users\user\folder-name\filename.extension` :

![ss2](https://www.freecodecamp.org/news/content/images/2022/04/ss2.png)

**Étape 4** : Appuyez sur `ENTRÉE` pour exécuter la commande. Ensuite, vérifiez à nouveau le dossier et vous ne devriez plus voir le fichier :

![ss3](https://www.freecodecamp.org/news/content/images/2022/04/ss3.png)

## Conclusion

La commande `del` supprimera un fichier même s'il est ouvert dans un autre programme, à l'exception des programmes Office comme MS Word.

Donc, si vous avez toujours du mal à forcer la suppression d'un fichier, assurez-vous qu'il n'est pas ouvert dans un autre programme, surtout un programme Office.
	
Merci d'avoir lu.