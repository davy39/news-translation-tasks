---
title: Comment effacer de manière sécurisée un disque et un fichier avec la commande
  Linux shred
date: '2022-03-14T14:55:27.000Z'
author: Zaira Hira
authorURL: https://www.freecodecamp.org/news/author/zaira/
originalURL: https://freecodecamp.org/news/securely-erasing-a-disk-and-file-using-linux-command-shred
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/shred--2-.gif
tags:
- name: Linux
  slug: linux
- name: Security
  slug: security
seo_desc: "Removing files and formatting disks is a common task for users. And Linux\
  \ provides a number of utilities to delete files and folders from the command line.\
  \ \nThe most common command to delete files and folders is rm and rmdir, respectively.\
  \ You can re..."
---


La suppression de fichiers et le formatage de disques sont des tâches courantes pour les utilisateurs. Et Linux fournit un certain nombre d'utilitaires pour supprimer des fichiers et des dossiers depuis la ligne de commande.

<!-- more -->

Les commandes les plus courantes pour supprimer des fichiers et des dossiers sont respectivement `rm` et `rmdir`. Vous pouvez lire en détail la commande `rm` [ici][1].

Dans cet article de blog, nous allons étudier une nouvelle commande nommée `shred` qui nous aide à effacer des disques et à purger des fichiers de manière sécurisée.

## Qu'est-ce que la commande Linux `shred` ?

La commande `shred` permet d'écraser les données sur place plusieurs fois. Cela rend la récupération des données beaucoup plus difficile pour les logiciels tiers et les sondes matérielles. C'est pourquoi elle est couramment utilisée pour supprimer des données de façon sécurisée.

### Syntaxe de la commande Linux shred :

```
shred [OPTION] filename
```

```
shred -vfz [/file/system/path]
```

Selon la page de manuel (`man`), voici quelques-unes des \[OPTIONS\] que vous pouvez utiliser avec `shred` :

-   `-n`, --iterations=N  
    Au lieu du nombre par défaut (3), écrase les données N fois.
-   `-z`, --zero  
    Ajoute un écrasement final avec des zéros pour masquer l'effacement.
-   `-f`, --force  
    Force les permissions pour permettre l'écriture si nécessaire.
-   `-v`, --verbose  
    Affiche la progression en détail.
-   `-u`, --remove  
    Tronque et supprime le fichier après l'écrasement.

Dans l'exemple ci-dessus, remplacez le chemin par le chemin de votre disque.

### En quoi `shred` est-elle différente de `rm` ?

L'utilisation simple de `rm` supprime le pointeur vers le système de fichiers. Les données réelles peuvent toujours être présentes sur le disque. Il existe donc une possibilité de récupération des données.

Mais lorsque vous utilisez la commande `shred`, le fichier est écrasé un nombre spécifié de fois de telle sorte que le contenu réel devient irrécupérable. Nous verrons cela dans les exemples plus loin.

Une autre différence est la vitesse d'exécution. Habituellement, `rm` est plus rapide que `shred`. Cela est dû au fait que `shred` écrase le fichier plusieurs fois avant de le supprimer. Selon le nombre d'itérations et la taille du fichier ou du disque, `shred` peut prendre plus de temps. À l'inverse, `rm` se contente de supprimer le pointeur vers le système de fichiers.

### Comment fonctionne la commande `shred` ?

La commande `shred` effectue par défaut trois passes sur le fichier. Ces trois passes garantissent que le fichier est écrasé trois fois. La valeur par défaut des passes peut également être modifiée en utilisant le drapeau `-n`.

## Quand utiliser la commande `shred`

Vous utilisez la commande `shred` pour effacer des données sensibles, ce qui garantit également la sécurité. Elle peut être utilisée par les administrateurs système, les équipes de informatique légale (digital forensics) ou les spécialistes de la sécurité de l'information pour appliquer les normes de sécurité.

## Exemples d'utilisation de `shred`

⚠️ Avant d'exécuter l'un des exemples sur votre système, assurez-vous que votre fichier et votre système de fichiers sont correctement sauvegardés. Soyez prudent, car les contenus ne sont pas récupérables.

### Comment écraser et supprimer un fichier avec `shred`

Nous avons un exemple de fichier `poem.txt` dont le contenu est partagé ci-dessous :

![content of file poem.txt](https://www.freecodecamp.org/news/content/images/2022/03/image-53.png) _Contenu du fichier d'exemple `poem.txt`_

Écrasons son contenu en utilisant les trois passes par défaut :

```
shred -v poem.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-54.png) _Ici, nous pouvons voir que le fichier a subi 3 écrasements_

Vérifions le contenu du fichier effacé :

```
cat poem.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-55.png) _Ici, nous pouvons voir que le contenu a été modifié dans un format illisible._

Nous pouvons maintenant supprimer le fichier en toute sécurité en utilisant `rm poem.txt`.

Cependant, nous pouvons utiliser la commande `shred` de manière plus efficace pour écraser, masquer l'effacement et supprimer le fichier en une seule commande. Modifions et exécutons la commande ci-dessous :

```
shred -vzu -n5 poem.txt
```

Où :

-   `-v` signifie verbose (mode verbeux) et fournit une sortie détaillée.
-   `-z` remplace la passe finale par des zéros pour masquer l'effacement.
-   `-u` supprime le fichier après l'effacement. Avec ce drapeau, nous n'avons pas besoin de supprimer le fichier ensuite avec `rm`.
-   `-n` modifie le nombre de passes. Nous l'avons réglé sur 5.

### Sortie :

Dans la sortie ci-dessous, le fichier est écrasé 5 fois. Lors de la passe finale, le fichier est écrasé avec uniquement des zéros. Lors des étapes de suppression du fichier, le nom du fichier est également muté afin qu'il ne soit plus repérable.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-57.png) _Suppression et masquage du fichier en une seule commande_

### Comment effacer un disque ou une partition avec `shred`

Supposons que vous vendiez vos disques ou que vous ayez besoin d'effacer votre lecteur portable. Vous pouvez utiliser `shred` pour effacer votre lecteur à l'aide de la commande ci-dessous :

```
sudo shred -vfz /dev/sde
```

Où :

-   `-v` fournit une sortie détaillée.
-   `-f` force les permissions d'écriture si elles sont manquantes.
-   `-z` écrit des zéros lors de la passe finale.

Vous pouvez également utiliser `shred` sur des partitions RAID.

```
shred -vfz -n 10 /dev/md1
```

## Quand la commande shred n'est-elle pas efficace ?

Il existe certains cas où `shred` n'est pas efficace. Selon les [pages de manuel][2], voici quelques-uns de ces cas :

-   Systèmes de fichiers à structure de journal (log-structured) ou journalisés, tels que ceux fournis avec AIX et Solaris (ainsi que JFS, ReiserFS, XFS, Ext3, etc.).
-   Systèmes de fichiers qui écrivent des données redondantes, comme les systèmes de fichiers basés sur RAID.
-   Systèmes de fichiers qui effectuent des instantanés (snapshots). Les exemples incluent le serveur NFS de Network Appliance.
-   Systèmes de fichiers qui supportent la mise en cache dans des emplacements temporaires, comme les clients NFS version 3.
-   Systèmes de fichiers compressés.

## Conclusion

La commande `shred` garantit que les données d'un fichier ne sont pas récupérables. Bien qu'il existe certaines exceptions, `shred` reste une option meilleure et plus sûre que `rm`.

J'espère que vous avez trouvé ce tutoriel utile.

Partagez vos réflexions sur [Twitter][3] !

Vous pouvez lire mes autres articles [ici][4].

[1]: https://www.freecodecamp.org/news/remove-directory-in-linux-how-to-delete-a-folder-from-the-command-line/
[2]: https://linux.die.net/man/1/shred
[3]: https://twitter.com/hira_zaira
[4]: https://www.freecodecamp.org/news/author/zaira/