---
title: Comment supprimer un fichier ou un répertoire sous Linux – Commande pour supprimer
  un dossier et son contenu
date: '2023-05-04T15:15:36.000Z'
authorURL: ''
originalURL: https://freecodecamp.org/news/how-to-delete-a-file-or-directory-in-linux
posteditor: ''
proofreader: ''
author: freeCodeCamp
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/Shittu-Olumide-How-to-Delete-a-File-or-Directory-in-Linux---Command-to-Remove-a-Folder-and-its-Contents.png
tags:
- name: Linux
  slug: linux
seo_desc: 'By Shittu Olumide

  In Linux, deleting files or directories is a fundamental operation that every user
  must know. Although it may seem like a straightforward task, there are different
  methods to delete files or directories, each with its specific use c...'
---


Par Shittu Olumide

<!-- more -->

Sous Linux, la suppression de fichiers ou de répertoires est une opération fondamentale que chaque utilisateur doit connaître. Bien que cela puisse sembler être une tâche simple, il existe différentes méthodes pour supprimer des fichiers ou des répertoires, chacune ayant son cas d'utilisation spécifique.

Ce tutoriel fournira un guide étape par étape sur la façon de supprimer des fichiers ou des répertoires sous Linux. Nous passerons également en revue les commandes que vous pouvez utiliser pour supprimer des fichiers et des dossiers ainsi que leur contenu.

## Comment supprimer un fichier sous Linux

La suppression d'un fichier consiste à retirer la référence du fichier du système de fichiers. Le fichier lui-même n'est pas immédiatement retiré du périphérique de stockage, mais son espace est marqué comme disponible pour être réutilisé.

Il existe plusieurs façons de supprimer un fichier sous Linux. Voici quelques-unes des méthodes les plus courantes :

### Utiliser le gestionnaire de fichiers graphique (GUI)

La plupart des distributions Linux sont livrées avec un gestionnaire de fichiers GUI qui vous permet de supprimer des fichiers à l'aide d'une interface graphique. Naviguez simplement jusqu'au fichier que vous souhaitez supprimer, faites un clic droit dessus et sélectionnez "Supprimer" ou "Déplacer vers la corbeille".

### Utiliser la commande `rm`

Vous pouvez également utiliser la commande `rm` (remove) pour supprimer des fichiers et des répertoires sous Linux. Pour supprimer un fichier à l'aide de la commande `rm`, tapez la commande suivante dans le terminal :

```
rm filename
```

Assurez-vous de remplacer `filename` par le nom du fichier que vous souhaitez supprimer. Si le fichier est protégé en écriture ou si vous n'avez pas les permissions suffisantes pour le supprimer, vous serez invité à confirmer la suppression.

### Utiliser la commande `shred`

La commande `shred` est un moyen plus sûr de supprimer des fichiers en écrasant le contenu du fichier plusieurs fois avant de le supprimer. Cela rend la récupération du fichier supprimé difficile pour quiconque.

Pour utiliser la commande `shred`, tapez la commande suivante dans le terminal :

```
shred -u filename
```

Assurez-vous de remplacer `filename` par le nom du fichier que vous souhaitez supprimer. L'option `-u` indique à `shred` de supprimer le fichier après l'avoir écrasé.

### Utiliser la commande `trash-cli`

La commande `trash-cli` offre un moyen plus sûr de supprimer des fichiers en les déplaçant vers la corbeille au lieu de les supprimer immédiatement. Pour pouvoir utiliser la commande `trash-cli`, vous devez d'abord l'installer :

```
sudo apt-get install trash-cli
```

Après l'installation, vous pouvez supprimer un fichier à l'aide de la commande suivante :

```
trash filename
```

## Comment supprimer un répertoire sous Linux

Pour supprimer un répertoire sous Linux, vous pouvez utiliser la commande `rmdir` ou `rm`. Vous utilisez la commande `rmdir` pour supprimer un répertoire vide, tandis que la commande `rm` supprime un répertoire et tout son contenu.

### Utiliser la commande `rm`

Voici les étapes pour supprimer un répertoire sous Linux à l'aide de la commande `rm` :

1.  **Ouvrez le terminal** : Pour supprimer un répertoire sous Linux, vous devez utiliser la ligne de commande. Ouvrez le terminal en appuyant sur "Ctrl+Alt+T" sur votre clavier ou en recherchant "terminal" dans le lanceur d'applications de votre système.
2.  **Naviguez vers le répertoire que vous souhaitez supprimer** : Utilisez la commande `cd` pour naviguer vers le répertoire que vous souhaitez supprimer. Par exemple, si le répertoire que vous souhaitez supprimer s'appelle `my_directory` et se trouve dans votre dossier personnel, tapez `cd ~/my_directory` et appuyez sur "Entrée".
3.  **Vérifiez le contenu du répertoire** : Avant de supprimer le répertoire, il est conseillé de vérifier son contenu pour vous assurer que vous supprimez le bon répertoire. Utilisez la commande `ls` pour lister le contenu du répertoire. Par exemple, tapez `ls` et appuyez sur "Entrée" pour voir les fichiers et dossiers à l'intérieur du dossier `my_directory`.
4.  **Supprimez le répertoire et son contenu** : Pour supprimer le répertoire et tout son contenu, utilisez la commande `rm` avec l'option `-r`, qui signifie récursif. Tapez `rm -r my_directory` et appuyez sur "Entrée". Vous serez invité à confirmer la suppression. Tapez `y` et appuyez sur "Entrée" pour confirmer.
5.  **Vérifiez que le répertoire a été supprimé** : Pour vérifier que le répertoire a été supprimé, utilisez la commande `ls` pour lister le contenu du répertoire parent. Par exemple, si le dossier `my_directory` était situé dans votre dossier personnel, tapez `ls ~/` et appuyez sur "Entrée". Le dossier `my_directory` ne devrait plus figurer dans la liste.

Note : Soyez très prudent lorsque vous utilisez la commande `rm -r`, car elle peut supprimer des fichiers et des répertoires de manière irréversible.

### Utiliser la commande `rmdir`

Voici les étapes pour supprimer un répertoire sous Linux à l'aide de la commande `rmdir` :

1.  **Ouvrez le terminal** : Ouvrez le terminal en appuyant sur "Ctrl+Alt+T" sur votre clavier ou en recherchant "terminal" dans le lanceur d'applications de votre système.
2.  **Naviguez vers le répertoire que vous souhaitez supprimer** : Utilisez la commande `cd` pour naviguer vers le répertoire que vous souhaitez supprimer. Par exemple, si le répertoire que vous souhaitez supprimer s'appelle `my_directory` et se trouve dans votre dossier personnel, tapez `cd ~/my_directory` et appuyez sur "Entrée".
3.  **Supprimez le répertoire** : Pour supprimer le répertoire, utilisez la commande `rmdir` suivie du nom du répertoire. Tapez `rmdir my_directory` et appuyez sur "Entrée". Si le répertoire n'est pas vide, vous recevrez un message d'erreur et le répertoire ne sera pas supprimé.
4.  **Vérifiez que le répertoire a été supprimé** : Pour vérifier que le répertoire a été supprimé, utilisez la commande `ls` pour lister le contenu du répertoire parent. Par exemple, si le dossier `my_directory` était situé dans votre dossier personnel, tapez `ls ~/` et appuyez sur "Entrée". Le dossier `my_directory` ne devrait plus figurer dans la liste.

## Conclusion

La commande `rm` est la commande la plus couramment utilisée pour supprimer des fichiers, tandis que les commandes `rmdir` et `rm` avec les options `-r` ou `-R` sont utilisées pour supprimer des répertoires. En suivant ce guide étape par étape, vous pouvez désormais supprimer efficacement des fichiers ou des répertoires sous Linux.

Conseils supplémentaires :

1.  Soyez prudent lorsque vous utilisez la commande `rm` avec l'option `-r` ou `-R`, car elle peut supprimer des fichiers et des répertoires de manière irréversible.
2.  Vérifiez toujours à deux reprises le nom du fichier ou du répertoire avant de le supprimer pour éviter de supprimer accidentellement le mauvais élément.
3.  N'utilisez la commande `shred` que lorsque cela est nécessaire, car elle peut prendre plus de temps pour supprimer des fichiers que les autres méthodes.
4.  Soyez attentif aux permissions des fichiers lors de la suppression, car certains fichiers ou répertoires peuvent nécessiter un accès root pour être supprimés.

Connectons-nous sur [Twitter][1] et sur [LinkedIn][2]. Vous pouvez également vous abonner à ma chaîne [YouTube][3].

Bon code !

[1]: https://www.twitter.com/Shittu_Olumide_
[2]: https://www.linkedin.com/in/olumide-shittu
[3]: https://www.youtube.com/channel/UCNhFxpk6hGt5uMCKXq0Jl8A