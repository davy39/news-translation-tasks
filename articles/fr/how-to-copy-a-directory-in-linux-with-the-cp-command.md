---
title: Comment copier un répertoire sous Linux avec la commande cp
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-05-24T22:21:19.000Z'
originalURL: https://freecodecamp.org/news/how-to-copy-a-directory-in-linux-with-the-cp-command
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/Shittu-Olumide-How-to-Copy-a-Directory-in-Linux-with-the-cp-Command.png
tags:
- name: Linux
  slug: linux
seo_title: Comment copier un répertoire sous Linux avec la commande cp
seo_desc: "By Shittu Olumide\nCopying directories is an essential task in Linux. It\
  \ allows you to duplicate directories, create backups, or transfer data between\
  \ different locations. \nOne of the most commonly used commands for copying files\
  \ and directories in Li..."
---

Par Shittu Olumide

Copier des répertoires est une tâche essentielle sous Linux. Cela vous permet de dupliquer des répertoires, de créer des sauvegardes ou de transférer des données entre différents emplacements. 

L'une des commandes les plus couramment utilisées pour copier des fichiers et des répertoires sous Linux est `cp`.

Dans ce tutoriel, nous allons explorer comment copier des répertoires efficacement en utilisant la commande `cp`, ainsi que diverses options et techniques pour personnaliser le processus de copie.

## La commande Linux `cp`

Vous utilisez la commande `cp` sous Linux pour copier des fichiers et des répertoires d'un emplacement à un autre. Elle signifie "copy" et est un utilitaire fondamental en ligne de commande pour la gestion des fichiers. 

La commande `cp` suit une syntaxe spécifique pour copier des répertoires. Comprendre la structure de base de la commande est crucial pour des copies de répertoires réussies. 

### Syntaxe de la commande `cp`

```bash
cp [options] source_directory destination_directory

```

Voici une explication de chaque composant de la syntaxe :

* `cp` : Il s'agit de la commande elle-même, qui signifie "copy".
* `[options]` : Cela représente des flags et paramètres optionnels qui peuvent modifier le comportement de la commande `cp`. Les options sont généralement précédées d'un trait d'union (-) ou d'un double trait d'union (--) et peuvent être utilisées pour spécifier des fonctionnalités supplémentaires, telles que la préservation des attributs, l'activation de la récursivité ou l'affichage de la progression.
* `source_directory` : Il s'agit du répertoire que vous souhaitez copier. Il peut être spécifié comme un chemin relatif ou absolu.
* `destination_directory` : Il s'agit du répertoire où vous souhaitez copier le répertoire source. Il peut également être spécifié comme un chemin relatif ou absolu.

Voici quelques concepts et fonctionnalités clés de la commande `cp` :

1. **Copie de fichiers** : La commande `cp` peut être utilisée pour copier des fichiers individuels. Nous fournissons le chemin et le nom du fichier source, suivis du répertoire ou du nom de fichier de destination.
2. **Copie de répertoires** : La commande `cp` peut également copier des répertoires entiers. Pour copier un répertoire et son contenu, nous devons inclure l'option `-r` (ou `--recursive`), qui active la copie récursive. Cette option garantit que tous les sous-répertoires et fichiers dans le répertoire sont copiés.
3. **Préservation des attributs de fichier** : Par défaut, la commande `cp` copie les fichiers sans préserver leurs attributs tels que les permissions, les horodatages et la propriété. Cependant, nous pouvons utiliser l'option `-p` (ou `--preserve`) pour préserver les attributs des fichiers pendant le processus de copie.
4. **Gestion des fichiers existants** : Lors de la copie de fichiers ou de répertoires, la commande `cp` gère les conflits lorsqu'il existe des fichiers ou des répertoires avec les mêmes noms dans l'emplacement de destination. Par défaut, elle écrase les fichiers existants sans demander confirmation. Nous pouvons utiliser l'option `-i` (ou `--interactive`) pour demander confirmation avant d'écraser les fichiers existants.
5. **Copie entre différents systèmes de fichiers** : La commande `cp` peut gérer la copie entre différents systèmes de fichiers. Elle ajuste automatiquement le comportement et effectue la copie en conséquence.

Démontrons comment faire cela :

```bash
cp -r /Desktop/welcome /Desktop/tutorial

```

Dans la commande ci-dessus :

* Le flag `-r` signifie "recursive" et permet à la commande `cp` de copier des répertoires et leur contenu.
* `/Desktop/welcome` est le chemin du répertoire que nous voulons copier.
* `/Desktop/tutorial` est le chemin où nous voulons copier le répertoire.

## Conclusion

Avec les connaissances et la compréhension de la syntaxe de la commande `cp`, nous pouvons copier efficacement des répertoires et leur contenu.

Tout au long de cet article, nous avons exploré le processus étape par étape de copie de répertoires vers différents emplacements, de copie récursive de répertoires avec leur contenu. Nous avons également discuté de certaines fonctionnalités importantes de la commande `cp`. 

Alors, allez-y et essayez-le :)

Restons en contact sur [Twitter](https://www.twitter.com/Shittu_Olumide_) et sur [LinkedIn](https://www.linkedin.com/in/olumide-shittu). Vous pouvez également vous abonner à ma chaîne [YouTube](https://www.youtube.com/channel/UCNhFxpk6hGt5uMCKXq0Jl8A).

Bon codage !