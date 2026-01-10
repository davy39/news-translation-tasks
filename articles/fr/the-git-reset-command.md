---
title: La commande Git Reset
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-02T22:12:00.000Z'
originalURL: https://freecodecamp.org/news/the-git-reset-command
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e4d740569d1a4ca3c68.jpg
tags:
- name: Git
  slug: git
- name: toothbrush
  slug: toothbrush
seo_title: La commande Git Reset
seo_desc: 'Git Reset

  The git reset command allows you to RESET your current head to a specified state.
  You can reset the state of specific files as well as an entire branch.

  Reset a file or set of files

  The following command lets you selectively choose chunks o...'
---

## **Git Reset**

La commande `git reset` vous permet de RÉINITIALISER votre tête actuelle à un état spécifié. Vous pouvez réinitialiser l'état de fichiers spécifiques ainsi que d'une branche entière.

### **Réinitialiser un fichier ou un ensemble de fichiers**

La commande suivante vous permet de choisir sélectivement des morceaux de contenu et de les réinitialiser ou de les désindexer.

```shell
git reset (--patch | -p) [tree-ish] [--] [paths]
```

### **Désindexer un fichier**

Si vous avez déplacé un fichier dans la zone de staging avec `git add`, mais que vous ne souhaitez plus qu'il fasse partie d'un commit, vous pouvez utiliser `git reset` pour désindexer ce fichier :

```shell
git reset HEAD FICHIER-A-DESINDEXER
```

Les modifications que vous avez apportées seront toujours dans le fichier, cette commande supprime simplement ce fichier de votre zone de staging.

### **Réinitialiser une branche à un commit précédent**

La commande suivante réinitialise la tête de votre branche actuelle au `COMMIT` donné et met à jour l'index. Elle revient essentiellement à l'état précédent de votre branche, puis tous les commits que vous faites par la suite écrasent tout ce qui est venu après le point de réinitialisation. Si vous omettez le `MODE`, il est par défaut `--mixed` :

```shell
git reset MODE COMMIT
```

Les options pour `MODE` sont :

* `--soft` : ne réinitialise pas le fichier d'index ou l'arborescence de travail, mais réinitialise HEAD à `commit`. Change tous les fichiers en "Changes to be commited"
* `--mixed` : réinitialise l'index mais pas l'arborescence de travail et rapporte ce qui n'a pas été mis à jour
* `--hard` : réinitialise l'index et l'arborescence de travail. Toutes les modifications apportées aux fichiers suivis dans l'arborescence de travail depuis `commit` sont supprimées
* `--merge` : réinitialise l'index et met à jour les fichiers dans l'arborescence de travail qui sont différents entre `commit` et HEAD, mais conserve ceux qui sont différents entre l'index et l'arborescence de travail
* `--keep` : réinitialise les entrées d'index et met à jour les fichiers dans l'arborescence de travail qui sont différents entre `commit` et HEAD. Si un fichier qui est différent entre `commit` et HEAD a des modifications locales, la réinitialisation est abandonnée