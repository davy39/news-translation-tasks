---
title: cmd Supprimer un Dossier – Comment Supprimer des Fichiers et Dossiers dans
  Windows
subtitle: ''
author: Kristofer Koishigawa
co_authors: []
series: null
date: '2020-11-13T04:35:00.000Z'
originalURL: https://freecodecamp.org/news/cmd-delete-folder-how-to-remove-files-and-folders-in-windows
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5fc9bc71e6787e098393991d.jpg
tags:
- name: command
  slug: command
- name: command line
  slug: command-line
- name: Windows
  slug: windows
- name: Windows 10
  slug: windows-10
seo_title: cmd Supprimer un Dossier – Comment Supprimer des Fichiers et Dossiers dans
  Windows
seo_desc: 'Sometimes it''s just faster to do things with the command line.

  In this quick tutorial we''ll go over how to open Command Prompt, some basic commands
  and flags, and how to delete files and folders in Command Prompt.

  If you''re already familiar with basi...'
---

Parfois, il est simplement plus rapide de faire les choses avec la ligne de commande.

Dans ce tutoriel rapide, nous allons voir comment ouvrir l'invite de commandes, quelques commandes et flags de base, et comment supprimer des fichiers et dossiers dans l'invite de commandes.

Si vous êtes déjà familier avec les commandes DOS de base, n'hésitez pas à [passer directement](#comment-supprimer-des-fichiers-avec-la-commande-del).

## Comment ouvrir l'invite de commandes

Pour ouvrir l'invite de commandes, appuyez sur la touche Windows et tapez "cmd".

Ensuite, cliquez sur "Exécuter en tant qu'administrateur" :

![Capture d'écran montrant comment ouvrir l'invite de commandes en tant qu'administrateur](https://www.freecodecamp.org/news/content/images/2020/12/run-command-prompt-as-administrator.jpg)

Après cela, vous verrez une fenêtre d'invite de commandes avec des privilèges administratifs :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/command-prompt-new-window.jpg)
_Capture d'écran de la fenêtre d'invite de commandes_

Si vous ne pouvez pas ouvrir l'invite de commandes en tant qu'administrateur, pas de problème. Vous pouvez ouvrir une fenêtre d'invite de commandes normale en cliquant sur "Ouvrir" au lieu de "Exécuter en tant qu'administrateur".

La seule différence est que vous ne pourrez peut-être pas supprimer certains fichiers protégés, ce qui ne devrait pas poser de problème dans la plupart des cas.

## Comment supprimer des fichiers avec la commande `del`

Maintenant que l'invite de commandes est ouverte, utilisez `cd` pour changer de répertoire vers l'endroit où se trouvent vos fichiers.

J'ai préparé un répertoire sur le bureau appelé Test Folder. Vous pouvez utiliser la commande `tree /f` pour voir un arbre de tous les fichiers et dossiers imbriqués :

![Capture d'écran après avoir exécuté tree /f dans le répertoire cible](https://www.freecodecamp.org/news/content/images/2020/12/command-prompt-tree.jpg)

Pour supprimer un fichier, utilisez la commande suivante : `del "<nom_du_fichier>"`.

Par exemple, pour supprimer `Test file.txt`, exécutez simplement `del "Test File.txt"`.

Il peut y avoir une invite vous demandant si vous souhaitez supprimer le fichier. Si c'est le cas, tapez "y" et appuyez sur Entrée.

**Note :** Tout fichier supprimé avec la commande `del` ne peut pas être récupéré. Soyez très prudent quant à l'endroit et la manière dont vous utilisez cette commande.

Après cela, vous pouvez exécuter `tree /f` pour confirmer que votre fichier a été supprimé :

![Capture d'écran après avoir supprimé le fichier avec la commande del](https://www.freecodecamp.org/news/content/images/2020/12/del-tree-check.jpg)

De plus, un conseil bonus – l'invite de commandes dispose d'une complétion automatique basique. Vous pouvez donc simplement taper `del test`, appuyer sur la touche de tabulation, et l'invite de commandes le transformera en `del "Test File.txt"`.

### Comment forcer la suppression de fichiers avec la commande `del`

Parfois, les fichiers sont marqués comme étant en lecture seule, et vous verrez l'erreur suivante lorsque vous essayez d'utiliser la commande `del` :

![Capture d'écran de l'erreur après avoir essayé de supprimer un fichier en lecture seule](https://www.freecodecamp.org/news/content/images/2020/12/read-only-error.jpg)

Pour contourner cela, utilisez le flag `/f` pour forcer la suppression du fichier. Par exemple, `del /f "Read Only Test File.txt"` :

![Capture d'écran après avoir supprimé le fichier avec le flag force](https://www.freecodecamp.org/news/content/images/2020/12/del-force-flag.jpg)

## Comment supprimer des dossiers avec la commande `rmdir`

Pour supprimer des répertoires/dossiers, vous devrez utiliser la commande `rmdir` ou `rd`. Les deux commandes fonctionnent de la même manière, mais utilisons `rmdir` car c'est un peu plus expressif.

De plus, j'utiliserai les termes répertoire et dossier de manière interchangeable pour le reste du tutoriel. "Dossier" est un terme plus récent qui est devenu populaire avec les premières interfaces graphiques de bureau, mais dossier et répertoire signifient essentiellement la même chose.

Pour supprimer un répertoire, utilisez simplement la commande `rmdir <nom_du_répertoire>`.

**Note :** Tout répertoire supprimé avec la commande `rmdir` ne peut pas être récupéré. Soyez très prudent quant à l'endroit et la manière dont vous utilisez cette commande.

Dans ce cas, je souhaite supprimer un répertoire nommé Subfolder, donc j'utiliserai la commande `rmdir Subfolder` :

![Capture d'écran d'une erreur de répertoire non vide](https://www.freecodecamp.org/news/content/images/2020/12/directory-not-empty.jpg)

Mais, si vous vous souvenez, Subfolder contient un fichier nommé Nested Test File.

Vous pourriez utiliser `cd` pour entrer dans le répertoire Subfolder et supprimer le fichier, puis revenir avec `cd ..` et exécuter à nouveau la commande `rmdir Subfolder`, mais cela deviendrait fastidieux. Et imaginez s'il y avait un tas d'autres fichiers et répertoires imbriqués !

Comme avec la commande `del`, il existe un flag utile que nous pouvons utiliser pour rendre les choses beaucoup plus rapides et plus faciles.

### Comment utiliser le flag `/s` avec `rmdir`

Pour supprimer un répertoire, y compris tous les fichiers et sous-répertoires imbriqués, utilisez simplement le flag `/s` :

![Capture d'écran après avoir exécuté rmdir avec le flag /s](https://www.freecodecamp.org/news/content/images/2020/12/rmdir-s-flag.jpg)

Il y aura probablement une invite vous demandant si vous souhaitez supprimer ce répertoire. Si c'est le cas, tapez simplement "y" et appuyez sur Entrée.

Et c'est tout ! Cela devrait être tout ce que vous devez savoir pour supprimer des fichiers et dossiers dans l'invite de commandes Windows.

Toutes ces commandes devraient fonctionner dans PowerShell, qui est essentiellement la version 2.0 de l'invite de commandes. De plus, PowerShell dispose d'un tas d'alias sympas comme `ls` et `clear` qui devraient vous sembler familiers si vous êtes habitué à la ligne de commande Mac/Linux.

Ces commandes vous ont-elles aidé ? Y a-t-il d'autres commandes que vous trouvez utiles ? Dans tous les cas, faites-le moi savoir sur Twitter.