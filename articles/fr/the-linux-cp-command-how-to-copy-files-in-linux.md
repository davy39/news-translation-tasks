---
title: La commande Linux cp – Comment copier des fichiers sous Linux
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-06-06T16:06:41.000Z'
originalURL: https://freecodecamp.org/news/the-linux-cp-command-how-to-copy-files-in-linux
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/linux-cp-command.png
tags:
- name: Linux
  slug: linux
seo_title: La commande Linux cp – Comment copier des fichiers sous Linux
seo_desc: 'By Dillion Megida

  There are a couple different ways to copy and paste content when you''re working
  on your computer.

  If you spend more time in the user interface of your device, you''ll probably use
  your mouse to do this. You can copy files by right-cl...'
---

Par Dillion Megida

Il existe plusieurs façons de copier et coller du contenu lorsque vous travaillez sur votre ordinateur.

Si vous passez plus de temps dans l'interface utilisateur de votre appareil, vous utiliserez probablement votre souris pour cela. Vous pouvez copier des fichiers en faisant un clic droit sur le fichier et en sélectionnant "Copier", puis en allant dans un autre répertoire et en sélectionnant "Coller".

Pour mes amis du terminal, vous pouvez également effectuer des opérations de copie-coller de fichiers sans quitter le terminal. Dans un terminal basé sur Linux, vous le faites en utilisant la commande `cp`.

Dans cet article, je vais expliquer ce qu'est la commande `cp` et vous montrer comment copier et coller des fichiers et des répertoires sous Linux en utilisant le terminal.

## Qu'est-ce que la commande `cp` ?

Vous utilisez la commande `cp` pour copier des fichiers d'un emplacement à un autre. Cette commande peut également copier des répertoires (dossiers).

La syntaxe de cette commande est :

```bash
cp [...fichier/répertoires-sources] [destination]
```

`[fichier/répertoires-sources]` spécifie les sources des fichiers ou des répertoires que vous souhaitez copier. Et l'argument `[destination]` spécifie l'emplacement où vous souhaitez copier le fichier.

Pour comprendre le reste de cet article, je vais utiliser cet exemple de structure de dossier. Supposons qu'un répertoire appelé **DirectoryA** contient deux répertoires : **DirectoryA_1** et **DirectoryA_2**. Ces sous-répertoires contiennent de nombreux fichiers et sous-répertoires.

Je vais également supposer que vous êtes actuellement dans l'emplacement **DirectoryA** dans le terminal, alors si ce n'est pas le cas, assurez-vous de vous y trouver :

```bash
cd DirectoryA
```

## Comment copier des fichiers avec la commande `cp`

Si vous souhaitez copier un fichier, par exemple **README.txt** de **DirectoryA_1** vers **DirectoryA_2**, vous utiliserez la commande `cp` comme ceci :

```bash
cp ./DirectoryA_1/README.txt ./DirectoryA_2
# ./DirectoryA_1/README.txt est le fichier source
# ./DirectoryA_2 est la destination
```

Si vous souhaitez copier plus d'un fichier de **DirectoryA_1** vers **DirectoryA_2**, vous utiliserez la commande `cp` comme ceci :

```bash
cp ./DirectoryA_1/README.txt ./DirectoryA_1/ANOTHER_FILE.txt ./DirectoryA_2
```

Comme vous pouvez le voir, vous mettrez tous les fichiers sources en premier, et le dernier argument sera la destination.

## Comment copier des répertoires avec la commande `cp`

Par défaut, la commande `cp` fonctionne avec des fichiers. Donc si vous essayez de copier un répertoire comme ceci :

```bash
cp ./DirectoryA_1/Folder/ ./DirectoryA_2
```

Vous obtiendrez une erreur indiquant :

**./DirectoryA_1/Folder/ est un répertoire**

Pour copier des répertoires, vous devez passer le drapeau `-r`. Ce drapeau informe la commande `cp` de copier récursivement un répertoire et son contenu (qui peut être des fichiers ou d'autres sous-répertoires). Donc pour la commande précédente, vous pouvez ajouter le drapeau avant les sources de répertoire comme ceci :

```bash
cp -r ./DirectoryA_1/Folder/ ./DirectoryA_2
```

Cette commande copiera récursivement le répertoire **Folder** dans **./DirectoryA_1/** ainsi que tous les fichiers et répertoires dans le répertoire **Folder**.

## Comment copier des fichiers correspondant à un motif glob

Un motif glob est similaire à Regex, qui vous permet de faire correspondre plusieurs fichiers avec des noms correspondant à un motif spécifique. En savoir plus sur la différence ici : [Regex vs Glob patterns](https://dillionmegida.com/p/regex-vs-glob-patterns/).

Par exemple, si vous souhaitez copier tous les fichiers dans **DirectoryA_1** avec l'extension **.txt**, vous pouvez exécuter cette commande :

```bash
cp ./DirectoryA_1/*.txt ./DirectoryA_2
```

`./DirectoryA_1/*.txt` correspond aux fichiers avec l'extension `.txt` dans leurs noms, et la commande `cp` peut copier tous ces fichiers vers la destination.

Vous pouvez consulter la [documentation glob](https://linux.die.net/man/7/glob) pour en savoir plus sur les motifs et caractères de globbing que vous pouvez utiliser.

Maintenant, vous savez comment copier des fichiers (et des répertoires) directement depuis la ligne de commande. Merci d'avoir lu !