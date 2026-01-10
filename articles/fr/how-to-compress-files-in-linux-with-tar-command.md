---
title: Commande Linux tar – Comment compresser des fichiers sous Linux
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2021-10-06T16:19:13.000Z'
originalURL: https://freecodecamp.org/news/how-to-compress-files-in-linux-with-tar-command
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/Linux-File-Tar-Compression.png
tags:
- name: compression
  slug: compression
- name: data compression
  slug: data-compression
- name: Linux
  slug: linux
seo_title: Commande Linux tar – Comment compresser des fichiers sous Linux
seo_desc: "File compression is an essential utility across all platforms. It helps\
  \ you reduce file size and share files efficiently. And compressed files are also\
  \ easier to copy to remote servers. \nYou can also compress older and rarely used\
  \ files and save them..."
---

La compression de fichiers est une utilité essentielle sur toutes les plateformes. Elle vous aide à réduire la taille des fichiers et à partager des fichiers efficacement. Les fichiers compressés sont également plus faciles à copier sur des serveurs distants.

Vous pouvez également compresser des fichiers anciens et rarement utilisés et les sauvegarder pour une utilisation future, ce qui vous aide à économiser de l'espace disque.

Dans cet article, nous allons voir comment compresser des fichiers avec la commande `tar` sous Linux, ainsi que quelques exemples de `tar` en action.

## Qu'est-ce que la commande tar ?

Nous utilisons la commande `tar` pour compresser et décompresser des fichiers depuis la ligne de commande. La syntaxe est présentée ci-dessous :

```bash
tar [flags] destinationFileName sourceFileName
```

La commande `tar` utilise les flags suivants pour personnaliser l'entrée de la commande :

<table>
<thead>
<tr>
<th>Flag</th>
<th>Explication</th>
<th>Utilisation</th>
</tr>
</thead>
<tbody>
<tr>
<td>-c</td>
<td>Créer une nouvelle archive.</td>
<td>Nous utilisons ce flag chaque fois que nous devons créer une nouvelle archive.</td>
</tr>
<tr>
<td>-z</td>
<td>Utiliser la compression gzip.</td>
<td>Lorsque nous spécifions ce flag, cela signifie que l'archive sera créée en utilisant la compression gzip.</td>
</tr>
<tr>
<td>-v</td>
<td>Fournir une sortie verbeuse.</td>
<td>Fournir le flag -v affiche les détails des fichiers compressés.</td>
</tr>
<tr>
<td>-f</td>
<td>Nom du fichier d'archive.</td>
<td>Les noms de fichiers d'archive sont mappés en utilisant le flag -f.</td>
</tr>
<tr>
<td>-x</td>
<td>Extraire d'un fichier compressé.</td>
<td>Nous utilisons ce flag lorsque les fichiers doivent être extraits d'une archive.</td>
</tr>
</tbody>
</table>

### Comment créer une archive

Nous avons une liste des fichiers suivants que nous allons compresser avec `tar`.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-1.png)
_Liste des fichiers à compresser._

Pour les compresser, nous allons utiliser `tar` comme ceci :

```bash
tar -czvf logs_archive.tar.gz *
```

Décortiquons cette commande et examinons chaque flag.

`-c` crée une archive.

`-z` utilise la compression gzip.

`-v` fournit les détails des fichiers qui ont été archivés.

`-f` crée une archive avec le nom 'logs_archive.tar.gz' comme fourni dans la commande ci-dessus.

Dans les résultats ci-dessous, nous pouvons voir que l'archive a été créée avec succès.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-13.png)
_L'archive a été créée avec la commande fournie._

### Comment supprimer des fichiers après compression

Supposons que nous ne voulons pas conserver les fichiers originaux après avoir créé une archive. Pour cela, nous pouvons utiliser le flag `--remove-files`.

```bash
tar -czvf logs_archive.tar.gz * --remove-files
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-3.png)
_Fichiers supprimés une fois l'archive créée_

Ici, les flags `-czvf` fonctionnent comme démontré précédemment, mais les fichiers originaux sont également supprimés. Une fois que nous listons les fichiers, nous ne voyons que l'archive.

### Comment afficher le contenu d'une archive

Vous pourriez avoir besoin de voir le contenu d'une archive sans l'extraire. Vous pouvez le faire avec le flag `-t`.

```bash
tar -tvf logs_archive.tar.gz
```

Dans cette commande, le flag `-t` spécifie que nous devons uniquement voir le contenu de l'archive. `-f` spécifie le nom du fichier et `-v` affiche le contenu détaillé.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-4.png)
_Affichage du contenu d'une archive._

### Comment extraire une archive

Pour extraire des fichiers d'une archive, vous utilisez le flag `-x` comme ceci :

```bash
tar -xzvf logs_archive.tar.gz
```

Décortiquons cette commande et examinons chaque flag.

`-x` extrait une archive.

`-z` spécifie que l'archive est gzip.

`-v` fournit les détails des fichiers qui ont été archivés.

`-f` extrait de l'archive nommée 'logs_archive.tar.gz'.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-14.png)
_Extraction d'une archive._

Voici un conseil utile : les commandes qui prennent beaucoup de temps à s'exécuter peuvent continuer en arrière-plan avec `&`.

L'ajout de fichiers à une archive et l'extraction d'une archive peuvent prendre un certain temps. Pour garder les commandes en cours d'exécution en arrière-plan pendant que vous continuez à travailler, associez la commande avec `&` comme ceci :

```bash
tar -xzvf logs_archive.tar.gz &
```

### Comment rechercher dans des fichiers de log compressés

Vous pourriez encore avoir besoin d'accéder à certains fichiers une fois qu'ils sont archivés. Heureusement, il existe une méthode que vous pouvez utiliser pour rechercher et afficher des fichiers de log compressés sans les décompresser et compromettre l'espace disque.

La commande que vous pouvez utiliser pour rechercher dans des fichiers compressés est `zgrep` :

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-6.png)
_Contenu d'un fichier 'audit.log' dans une archive._

Nous pouvons rechercher une chaîne dans une archive en utilisant la commande ci-dessous :

```bash
 zgrep -Hna 'string-to-search' compressedFile.tar.gz
```

Examinons brièvement les flags.

`-H` liste le nom du fichier qui contient la correspondance.

`-n` affiche le numéro de ligne qui contient la chaîne correspondante.

`-a` traite tous les fichiers comme des fichiers texte.

Voici le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-15.png)

## Conclusion

La compression de fichiers nous aide à économiser du temps et des ressources lors du partage de fichiers. Les serveurs tournent presque toujours et archivent d'énormes fichiers de log.

Vous pouvez également planifier la compression de fichiers via des tâches `cron` pour automatiser le nettoyage du disque. Je vous recommande vivement de tirer parti de cette utilité.

Merci d'avoir lu jusqu'à la fin. J'adorerais entrer en contact avec vous. Vous pouvez me trouver [ici](https://twitter.com/hira_zaira) sur Twitter. N'hésitez pas à partager vos pensées.

À bientôt.