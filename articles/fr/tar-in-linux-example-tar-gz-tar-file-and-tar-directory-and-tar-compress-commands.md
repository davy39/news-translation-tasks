---
title: Tar sous Linux – Exemples de commandes Tar GZ, Fichier Tar, Répertoire Tar
  et Compression Tar
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2019-11-02T17:57:00.000Z'
originalURL: https://freecodecamp.org/news/tar-in-linux-example-tar-gz-tar-file-and-tar-directory-and-tar-compress-commands
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/tar-article.jpg
tags:
- name: Linux
  slug: linux
seo_title: Tar sous Linux – Exemples de commandes Tar GZ, Fichier Tar, Répertoire
  Tar et Compression Tar
seo_desc: 'Do you want to combine a bunch of files and directories into a single file?
  The tar command in Linux is what you''re looking for!

  The tar command is used to compress a group of files into an archive. The command
  is also used to extract, maintain, or m...'
---

Vous souhaitez combiner un ensemble de fichiers et de répertoires en un seul fichier ? La commande `tar` sous Linux est ce qu'il vous faut !

La commande `tar` est utilisée pour compresser un groupe de fichiers dans une archive. Cette commande est également utilisée pour extraire, maintenir ou modifier des archives tar.

Les archives Tar combinent plusieurs fichiers et/ou répertoires en un seul fichier. Les archives Tar ne sont pas nécessairement compressées, mais elles peuvent l'être. Les permissions sont préservées et elle supporte de nombreux formats de compression.

Apprenez à utiliser `tar` dans cet article rapide.

## Syntaxe

`tar [options] [fichier-archive] [fichier ou répertoire à archiver]`

**Options :**  
**-c :** Crée une archive  
**-x :** Extrait l'archive  
**-f :** Crée une archive avec le nom de fichier donné  
**-t :** Affiche ou liste les fichiers dans le fichier archivé  
**-u :** Archive et ajoute à un fichier d'archive existant  
**-v :** Affiche des informations détaillées  
**-A :** Concatène les fichiers d'archive  
**-z :** Compresse le fichier tar en utilisant gzip  
**-j :** Compresse le fichier tar en utilisant bzip2  
**-W :** Vérifie un fichier d'archive  
**-r :** Met à jour ou ajoute un fichier ou un répertoire dans un fichier .tar déjà existant

## Exemples d'utilisation

**Extraire une archive :**  
`tar xfv archive.tar`  
(Options : x = extraire, f = fichier, v = détaillé)

**Créer une archive avec des fichiers ou un dossier :**  
`tar cfv archive.tar fichier1 fichier2 fichier3`  
(Options : c = créer)

**Créer des archives compressées :**  
`tar cfzv archive.tar fichier1 fichier2 fichier3`   
(Options : z = compresser avec gzip)

**Afficher tous les fichiers d'une archive :**  
`tar tvf archive.tar` 

**Créer une archive non compressée de tous les fichiers .txt dans le répertoire courant :**  
`tar cfv archive.tar *.txt`

**Extraire des fichiers d'une archive tar gzip archive.tar.gz :**  
`tar xvzf archive.tar.gz`

**Créer un fichier d'archive tar compressé en utilisant bzip2 :**  
`tar cvfj archive.tar.tbz exemple.cpp`  
(Options : j = compresser avec bzip2, taille de fichier plus petite mais prend plus de temps que `-z`)

**Mettre à jour un fichier tar existant en ajoutant le fichier todo.txt à l'archive :**  
`tar rvf archive.tar todo.txt`  
(Options : r = ajouter un fichier)

**Lister le contenu d'un fichier tar :**  
`tar tf fichier.tar`  
(Options : t = afficher, f = fichier)

**Créer une archive compressée du répertoire courant mais exclure certains répertoires :**  
`tar --exclude='./dossier' --exclude='./upload/dossier2' cfzv archive.tar .`("dossier" et "dossier2" sont exclus)