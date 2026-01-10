---
title: Copier un répertoire sous Linux – Comment utiliser cp pour un dossier en ligne
  de commande sous Linux et Unix (MacOS)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-05-04T15:33:12.000Z'
originalURL: https://freecodecamp.org/news/copy-a-directory-in-linux-how-to-cp-a-folder-in-the-command-line-in-linux-and-unix-macos
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/copy-directory-linux-article.jpg
tags:
- name: Linux
  slug: linux
- name: macOS
  slug: macos
- name: unix
  slug: unix
seo_title: Copier un répertoire sous Linux – Comment utiliser cp pour un dossier en
  ligne de commande sous Linux et Unix (MacOS)
seo_desc: 'By John Mosesman

  To copy files or directories in Unix-based operating systems (Linux and MacOS),
  you use the cp command.

  The cp command is a relatively simple command, but its behavior changes slightly
  depending on the inputs (files vs directories) a...'
---

Par John Mosesman

Pour copier des fichiers ou des répertoires dans les systèmes d'exploitation basés sur Unix (Linux et MacOS), on utilise la commande `cp`.

La commande `cp` est une commande relativement simple, mais son comportement change légèrement en fonction des entrées (fichiers vs répertoires) et des options que vous lui passez.

Pour consulter la documentation ou le manuel de la commande `cp`, exécutez `man cp` dans votre terminal :

```
$ man cp

NOM
     cp -- copier des fichiers

SYNOPSIS
     cp [OPTIONS] fichier_source fichier_cible
     cp [OPTIONS] fichier_source ... répertoire_cible

...

```

La forme de base de cette commande prend une source d'entrée (ou des sources) que vous voulez copier (fichiers ou répertoires) et une destination vers laquelle copier les fichiers ou répertoires :

```
cp [OPTIONS] fichier_source fichier_cible
```

## Comment copier un fichier dans le répertoire courant

Pour copier un fichier, passez le fichier que vous voulez copier et le chemin de l'endroit où vous voulez le copier.

Si vous avez un fichier nommé `a.txt` et que vous voulez une copie de ce fichier nommée `b.txt` :

```
$ ls
a.txt

$ cp a.txt b.txt

$ ls
a.txt   b.txt
```

> Si vous ne connaissez pas la commande `ls`, `ls` « liste » tout le contenu d'un répertoire.

Par défaut, la commande `cp` utilise _votre_ _répertoire courant_ comme chemin.

### Comment copier un fichier vers un autre répertoire

Pour copier un fichier vers un répertoire qui est _différent_ de votre répertoire courant, il vous suffit de passer le chemin de l'autre répertoire comme destination :

```
$ ls ../directory-1/

$ cp a.txt ../directory-1/

$ ls ../directory-1/
a.txt

```

Après la commande `cp`, le `directory-1` précédemment vide contient désormais le fichier `a.txt`.

Par défaut, le fichier copié reçoit le nom du fichier d'origine, mais vous pouvez également passer un nom de fichier en option :

```
$ cp a.txt ../directory-1/b.txt

$ ls ../directory-1/
b.txt
```

## Comment copier plusieurs fichiers dans un répertoire

Pour copier plus d'un fichier à la fois, vous pouvez passer plusieurs sources d'entrée et un répertoire comme destination :

```
$ ls ../directory-1/

$ cp first.txt second.txt ../directory-1/

$ ls ../directory-1/
first.txt       second.txt

```

Ici, les deux sources d'entrée (`first.txt` et `second.txt`) ont toutes deux été copiées dans le répertoire `directory-1`.

> **Note :** lors du passage de plusieurs sources, le dernier argument doit être un répertoire.

## Comment copier un répertoire vers un autre répertoire

Si vous essayez de passer un répertoire comme source d'entrée, vous obtenez cette erreur :

```
$ cp directory-1 directory-2
cp: directory-1 is a directory (not copied).
```

Pour copier un répertoire, vous devez ajouter le drapeau `-r` (ou `-R`) — qui est l'abréviation de `--recursive` :

```
$ ls directory-1
a.txt

$ cp -r directory-1 directory-2

$ ls
directory-1          directory-2

$ ls directory-2
a.txt
```

Ici, `directory-1` contenant le fichier `a.txt` est copié dans un nouveau répertoire appelé `directory-2` — qui contient désormais également le fichier `a.txt`.

### Comment copier le répertoire entier vs le contenu du répertoire

Il existe un cas particulier intéressant lorsque vous copiez un répertoire : si le répertoire de destination existe déjà, vous pouvez choisir de copier **le contenu du répertoire** ou le **répertoire entier** en ajoutant ou en supprimant un `/` final à votre entrée.

Voici la description de l'option `-R` de la page `man` :

> Si fichier_source désigne un répertoire, cp copie le répertoire et toute l'arborescence connectée à ce point. Si le fichier_source se termine par un /, le contenu du répertoire est copié plutôt que le répertoire lui-même.

Si vous voulez copier _uniquement le contenu_ du répertoire dans un autre répertoire, ajoutez un `/` final à votre entrée.

Si vous voulez copier le contenu du répertoire _et le dossier du répertoire lui-même_ dans un autre répertoire, n'ajoutez pas de `/` final :

```
$ ls
directory-1          directory-2

$ ls directory-2

$ cp -r directory-1 directory-2

$ ls directory-2
directory-1

$ ls directory-2/directory-1
a.txt
```

Ici, vous pouvez voir que parce que `directory-2` existe déjà — et que la source d'entrée n'avait pas de `/` final — le contenu de `directory-1` _et_ le répertoire lui-même ont été copiés dans la destination.

## Comment empêcher l'écrasement de fichiers avec `cp`

Par défaut, la commande `cp` écrasera les fichiers existants :

```
$ cat a.txt
A

$ cat directory-1/a.txt
B

$ cp a.txt directory-1/a.txt

$ cat directory-1/a.txt
A
```

> Si vous ne connaissez pas la commande `cat` ou « concatenate », elle affiche le contenu d'un fichier.

Il existe deux façons d'empêcher cela.

### Le drapeau interactif

Pour être averti lorsqu'un écrasement est sur le point de se produire, vous pouvez ajouter le drapeau `-i` ou `--interactive` :

```
$ cp -i a.txt directory-1/a.txt
overwrite directory-1/a.txt? (y/n [n])
```

### Le drapeau no-clobber

Ou, pour empêcher les écrasements sans être sollicité, vous pouvez ajouter le drapeau `-n` ou `--no-clobber` :

```
$ cat a.txt
A

$ cat directory-1/a.txt
B

$ cp -n a.txt directory-1/a.txt

$ cat directory-1/a.txt
B
```

Ici, vous pouvez voir que grâce au drapeau `-n`, le contenu de `directory-1/a.txt` n'a pas été écrasé.

## Autres options

Il existe de nombreuses autres options utiles à passer à la commande `cp` : comme `-v` pour une sortie « verbose » (verbeuse) ou `-f` pour « force ».

Je vous encourage vivement à lire la page `man` pour toutes les autres options utiles.

Si vous avez aimé ce tutoriel, je parle aussi de sujets comme celui-ci [sur Twitter](https://twitter.com/johnmosesman), et j'écris à leur sujet sur [mon site](https://johnmosesman.com/).