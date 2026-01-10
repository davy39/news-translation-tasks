---
title: Annuler Git Add – Comment supprimer des fichiers ajoutés dans Git
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2023-03-23T18:27:08.000Z'
originalURL: https://freecodecamp.org/news/undo-git-add-how-to-remove-added-files-in-git
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/cover-template.png
tags:
- name: Git
  slug: git
seo_title: Annuler Git Add – Comment supprimer des fichiers ajoutés dans Git
seo_desc: 'Git is a powerful version control and collaboration tool. It allows developers
  to work together seamlessly on projects.

  But even the most experienced developers can make mistakes while using Git, such
  as accidentally adding files that were not meant ...'
---

Git est un puissant outil de gestion de versions et de collaboration. Il permet aux développeurs de travailler ensemble de manière fluide sur des projets.

Mais même les développeurs les plus expérimentés peuvent commettre des erreurs en utilisant Git, comme ajouter accidentellement des fichiers qui n'étaient pas censés être commités. Cela peut être un problème, surtout si les fichiers ajoutés contiennent des informations sensibles ou confidentielles.

Dans cet article, vous apprendrez comment annuler la commande « Git add », ce qui signifie supprimer des fichiers de la staging area et empêcher qu'ils ne soient commités.

## Comment ajouter des fichiers dans Git et confirmer

Vous savez probablement comment ajouter des fichiers à la staging area en utilisant la commande `git add`. Lorsque vous voulez ajouter tous les fichiers, vous utilisez le point (.), mais quand vous voulez ajouter des fichiers spécifiques, vous joignez les noms ou chemins des fichiers :

```bash
// indexer tous les fichiers du répertoire actuel
git add .

// indexer un seul fichier
git add <file>

// indexer plusieurs fichiers
git add <file1> <file2> <file3> ...
```

Lorsque vous indexez des fichiers, vous pouvez confirmer en utilisant la commande `git status`, qui affiche une liste de tous les fichiers indexés :

![](https://paper-attachments.dropboxusercontent.com/s_4E8AA27FDBD6E92188ADA8CF7AE76BB35CFED775D18B77141314D06FC8C13ADB_1679558784394_image.png align="left")

## Comment supprimer des fichiers ajoutés dans Git

Il existe deux commandes principales que vous pouvez utiliser pour annuler « git add » ou supprimer des fichiers ajoutés dans Git. En d'autres termes, vous pouvez utiliser deux commandes majeures pour retirer des fichiers indexés de la staging area.

Il s'agit des commandes `git reset` et `git rm --cached`. Mais ces commandes sont assez différentes l'une de l'autre.

### Comment supprimer des fichiers ajoutés dans Git avec `git reset`

`git reset` est utilisé pour désindexer (unstage) les modifications qui ont été ajoutées à la staging area. Cela signifie qu'il retirera les fichiers de la staging area tout en conservant les modifications dans votre « répertoire de travail » (working directory).

Pour supprimer **un seul fichier** de la staging area, vous pouvez utiliser la commande suivante :

```bash
git reset <file>
```

Pour supprimer **tous les fichiers** de la staging area, vous pouvez utiliser la commande suivante :

```bash
git reset
```

Pour ne pas vous perdre, laissez-moi vous expliquer ce que signifie le répertoire de travail. Le répertoire de travail est l'endroit où vous apportez des modifications à votre code, tandis que la staging area est une étape intermédiaire où vous préparez les modifications avant de les Commit dans votre dépôt.

Lorsque vous utilisez `git reset` pour désindexer des modifications de la staging area, Git les supprimera de l'index mais les conservera dans votre répertoire de travail. Cela signifie que les modifications que vous avez apportées aux fichiers seront toujours visibles dans vos fichiers locaux, et vous pourrez continuer à apporter d'autres modifications si nécessaire.

### Comment supprimer des fichiers ajoutés dans Git avec `git rm --cached`

D'un autre côté, `git rm` est utilisé pour supprimer un fichier de la staging area et du répertoire de travail. Cela signifie qu'il supprimera définitivement le fichier de votre dépôt.

Pour supprimer un fichier du dépôt, vous pouvez utiliser la commande suivante :

```bash
git rm <file>
```

Mais vous voulez seulement « désindexer » vos fichiers (c'est-à-dire annuler la commande `git add`) et non les « supprimer » de votre répertoire de travail. C'est là que vous utilisez l'option `--cached`. L'option cached spécifie que la suppression ne doit avoir lieu que dans l'index de la staging area. Les fichiers du répertoire de travail ne seront pas touchés.

```bash
git rm --cached <file>
```

Il est important de noter que l'utilisation de `git rm --cached` n'est pas une solution complète pour conserver des fichiers dans le dépôt. Le fichier peut toujours être supprimé du répertoire de travail accidentellement ou intentionnellement.

Parce que cela peut arriver, il est recommandé d'utiliser cette commande avec prudence et de vous assurer que vous supprimez intentionnellement des fichiers que vous n'avez plus besoin de suivre dans Git.

## Conclusion

L'un des avantages de disposer de plusieurs commandes Git pouvant obtenir des résultats similaires, comme `git rm` et `git reset`, est qu'elles offrent aux utilisateurs flexibilité et choix. Différents utilisateurs peuvent avoir des préférences ou des flux de travail différents, et avoir plusieurs options vous permet de choisir la meilleure méthode.

Cependant, avoir trop de commandes similaires peut également entraîner de la confusion et des erreurs, en particulier pour les nouveaux utilisateurs qui pourraient ne pas comprendre leurs différences subtiles. Cela peut entraîner la suppression accidentelle de fichiers ou d'autres conséquences imprévues.

Assurez-vous donc de bien comprendre les commandes Git et leurs différences afin de pouvoir les utiliser sciemment. Il est également utile de consulter la documentation ou de demander l'aide d'utilisateurs plus expérimentés si vous n'êtes pas sûr de la manière d'utiliser une commande particulière.

Bon codage !