---
title: Supprimer un répertoire sous Linux – Comment supprimer des dossiers depuis
  la ligne de commande
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2022-09-07T18:18:33.000Z'
originalURL: https://freecodecamp.org/news/remove-directory-in-linux-from-the-command-line
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/Copy-of-read-write-files-python--2-.png
tags:
- name: command line
  slug: command-line
- name: Linux
  slug: linux
seo_title: Supprimer un répertoire sous Linux – Comment supprimer des dossiers depuis
  la ligne de commande
seo_desc: "Linux is a powerful OS with various command line utilities to help you\
  \ achieve your day-to-day tasks.\nRemoving folders is a very common operation that\
  \ allows you to either remove a single folder or remove them recursively (folders\
  \ within folders). \nI..."
---

Linux est un système d'exploitation puissant avec diverses utilitaires en ligne de commande pour vous aider à accomplir vos tâches quotidiennes.

Supprimer des dossiers est une opération très courante qui vous permet de supprimer un seul dossier ou de les supprimer de manière récursive (dossiers dans des dossiers).

Dans ce tutoriel, nous verrons comment supprimer des dossiers depuis la ligne de commande.

### Mais l'interface graphique ne suffit-elle pas pour supprimer des dossiers ?

Il est très simple de supprimer des dossiers depuis l'explorateur de fichiers. Tout ce dont nous avons besoin, c'est d'utiliser la touche supprimer du clavier ou de faire un clic droit et de supprimer le dossier. Mais vous pouvez être plus créatif avec le CLI (interface de ligne de commande).

Avec la ligne de commande, vous pouvez créer un script pour supprimer des fichiers périodiquement. Vous pouvez également supprimer des fichiers qui correspondent à certains critères tels que l'heure de modification ou la taille.

Les scripts de maintenance utilisent également des commandes pour supprimer des dossiers indésirables afin de maintenir l'espace disque à un niveau optimal.

En bref, vous pouvez automatiser vos tâches quotidiennes en utilisant la ligne de commande.

Faites preuve de prudence lors de la suppression depuis le CLI. Une fois que vous supprimez un dossier en utilisant le CLI, il est définitivement supprimé car il n'y a pas de corbeille. La seule façon de récupérer est par le biais d'une sauvegarde.

## Comment supprimer un dossier vide en utilisant `rmdir`

Vous utilisez la commande `rmdir` pour supprimer un répertoire vide. Elle ne fonctionne pas sur les répertoires non vides.

**Syntaxe de la commande `rmdir` :**

```bash
rmdir [OPTION] NOM_DU_RÉPERTOIRE
```

Nous pouvons fournir les options suivantes :

* `-v` : affiche la sortie détaillée pour chaque répertoire traité.
* `--ignore-fail-on-non-empty` : ignore si le répertoire n'est pas vide.
* `-p, --parents` : supprime un répertoire et ses ancêtres. Par exemple, `'rmdir -p a/b/c` supprimerait d'abord le dossier `c`, puis `b` et enfin `a`.

## Comment supprimer un dossier non vide en utilisant `rm`

Nous ne pouvons pas utiliser `rmdir` sur des dossiers non vides. Nous avons une autre commande pour cela – `rm`.

**Syntaxe de la commande `rm` :**

```bash
 rm [OPTION] [FICHIER]
```

Nous pouvons utiliser les options suivantes :

* `-r`, `-R`, `--recursive` : supprime les répertoires et leur contenu de manière récursive.
* `-d`, `--dir` : supprime les répertoires vides. Ainsi, nous pouvons également utiliser `rm` pour supprimer des répertoires vides comme la commande `rmdir`.
* `-v`, `--verbose` : explique ce qui est fait en mentionnant les détails des dossiers traités.
* `-i` : demande une confirmation avant chaque suppression.

Ainsi, la commande pour supprimer un dossier non vide serait :

```
rm -r nom-du-dossier
```

## Comment forcer la suppression de répertoires

Si vous n'avez pas les permissions d'`écriture`, vous ne pouvez pas supprimer le dossier. Si vous souhaitez le supprimer malgré tout, utilisez le drapeau `-f`. Le drapeau `-f` n'affiche aucune invite.

## Comment supprimer des dossiers en toute sécurité sous Linux

Pour éviter les suppressions accidentelles, utilisez le drapeau interactif `-i`. Ainsi, vous serez invité à confirmer avant de supprimer un dossier et son contenu.

Si vous souhaitez continuer, répondez simplement aux invites en entrant `y`. D'autre part, entrez `n` pour ignorer le fichier.

Dans l'exemple ci-dessous, notez comment nous descendons dans le dossier et vérifions chaque fichier un par un.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-309.png)
_Suppression interactive d'un dossier nommé `find-test`_

## Conclusion

Supprimer des répertoires est utile lorsque vous devez supprimer des dossiers après les avoir archivés, lorsque vous supprimez des doublons, lorsque vous supprimez des dossiers inutilisés, et bien plus encore.

Toutes ces tâches visent à créer plus d'espace disque. J'espère que vous avez trouvé ce tutoriel utile.

Quelle est la chose préférée que vous avez apprise ici ? Faites-le moi savoir sur [Twitter](https://twitter.com/hira_zaira) !

Lisez mes autres articles [ici](https://www.freecodecamp.org/news/author/zaira/).