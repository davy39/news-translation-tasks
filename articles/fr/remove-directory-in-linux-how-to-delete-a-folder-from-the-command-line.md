---
title: Supprimer un répertoire sous Linux – Comment supprimer un dossier depuis la
  ligne de commande
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2022-02-16T15:57:04.000Z'
originalURL: https://freecodecamp.org/news/remove-directory-in-linux-how-to-delete-a-folder-from-the-command-line
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/Copy-of-Cast-a-Function-in-SQL
seo_title: Supprimer un répertoire sous Linux – Comment supprimer un dossier depuis
  la ligne de commande
---

Convert-Char-to-Int-SQL-Server-Example.png
tags:
- name: ligne de commande
  slug: ligne-de-commande
- name: Linux
  slug: linux
seo_title: null
seo_desc: "L'interface en ligne de commande Linux est un outil puissant qui peut vous aider à accomplir des tâches complexes. \n  \ \nL'une des opérations courantes que vous devrez effectuer est de supprimer des éléments. Tout comme la création de fichiers et de dossiers, les supprimer depuis la ligne de commande Linux est quelque chose que vous ferez souvent. \n  \ \nDans cet article, nous allons discuter de la manière de supprimer des répertoires depuis la ligne de commande. Nous allons discuter de la syntaxe ainsi que de quelques exemples. J'utilise Ubuntu dans ces exemples."
---

L'interface en ligne de commande Linux est un outil puissant qui peut vous aider à accomplir des tâches complexes. 

L'une des opérations courantes que vous devrez effectuer est de supprimer des éléments. Tout comme la création de fichiers et de dossiers, les supprimer depuis la ligne de commande Linux est quelque chose que vous ferez souvent. 

Dans cet article, nous allons discuter de la manière de supprimer des répertoires depuis la ligne de commande. Nous allons discuter de la syntaxe ainsi que de quelques exemples. J'utilise Ubuntu dans ces exemples.

## Syntaxe de la commande Linux `rm`

Vous utilisez la commande `rm` pour supprimer quelque chose depuis la ligne de commande sous Linux. La syntaxe de la commande `rm` ressemble à ceci :

```bash
rm [flags] nom_du_répertoire
```

Voici quelques flags importants que vous devrez utiliser lors de la suppression d'un répertoire :

*  `-r`, `-R`, `--recursive` ["Récursif"] – Supprime les répertoires et leur contenu de manière récursive. 
* `-v`, `--verbose` ["Verbose"] – Cette option affiche les détails de ce qui est fait sur la CLI.
* `-f`, `--force` ["Forcer"] – Cette option ignore les fichiers inexistants et ne vous demande jamais confirmation.
* `-i` ["Interactif"] – Utilisez ce flag lorsque vous souhaitez être invité à confirmer avant chaque suppression.
* `-d` ["Répertoire"] – Cela fonctionne uniquement lorsque le répertoire est vide.

⚠️ Soyez prudent lorsque vous utilisez la commande `rm` et assurez-vous toujours que les données importantes sont sauvegardées.

## Comment identifier un dossier à supprimer

Puisque nous discutons de la manière de supprimer des dossiers, nous devons être certains que nous supprimons effectivement un dossier. Nous pouvons identifier un dossier/répertoire avec le flag `d` dans la première colonne. Notez que les fichiers ont le premier flag comme `-`.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-55.png)

## Exemples de la commande Linux `rm`

Dans notre dossier actuel, nous avons 2 dossiers `CSharpLab` et `PythonLab`. Leur contenu est montré ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-48.png)

Notez que `CSharpLab` est un répertoire vide.

### Comment supprimer un dossier qui n'est pas vide

Commençons par supprimer le dossier `PythonLab`.

```bash
rm -rvi PythonLab/
```

Où,

* `-r` supprime de manière récursive tous les fichiers et dossiers. Notez dans la sortie ci-dessous, tous les fichiers (`man.py, calculator.py, palindrome.py`) et dossiers (`/lib`) ont été supprimés.
* `-v` partage les détails.
* `-i` rend la suppression interactive, ce qui signifie qu'il demandera avant de supprimer quoi que ce soit.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-53.png)

### Comment supprimer un dossier vide

Essayons maintenant de supprimer le dossier `CSharpLab`. Comme ce dossier est vide, nous pouvons utiliser le flag `-d`.

```bash
rm -d CSharpLab/
```

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-50.png)
_Le répertoire CSharpLab est supprimé_

### Comment utiliser le flag `-f` "force"

Voyons maintenant comment fonctionne le flag `-f`. Cela force la suppression des dossiers sans aucune invite ou avertissement. En cas d'erreur, `-v` ignore toujours et supprime les fichiers qui sont valides.

Dans l'exemple ci-dessous, il y a une faute de frappe dans le nom du dossier. Notez que la faute de frappe est ignorée. Le fichier original est intact.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-51.png)

## Conclusion

Supprimer des répertoires est utile lorsque vous devez supprimer des dossiers après les avoir archivés, lorsque vous supprimez des doublons, lorsque vous supprimez des dossiers inutilisés, et bien plus encore. 

Toutes ces tâches visent à libérer de l'espace disque. J'espère que vous avez trouvé cet article utile.

Retrouvons-nous sur [Twitter](https://twitter.com/hira_zaira) !

Lisez mes autres articles [ici](https://www.freecodecamp.org/news/author/zaira/).

Discutons sur [Discord](https://discordapp.com/users/Zaira_H#2603).