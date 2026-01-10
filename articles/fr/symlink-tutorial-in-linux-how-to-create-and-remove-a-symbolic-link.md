---
title: Tutoriel sur les liens symboliques (Symlink) sous Linux – Comment créer et
  supprimer un lien symbolique
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-02T20:51:39.000Z'
originalURL: https://freecodecamp.org/news/symlink-tutorial-in-linux-how-to-create-and-remove-a-symbolic-link
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9b4f740569d1a4ca2b02.jpg
tags:
- name: Linux
  slug: linux
- name: unix
  slug: unix
seo_title: Tutoriel sur les liens symboliques (Symlink) sous Linux – Comment créer
  et supprimer un lien symbolique
seo_desc: 'By Dillion Megida

  A symlink (also called a symbolic link) is a type of file in Linux that points to
  another file or a folder on your computer. Symlinks are similar to shortcuts in
  Windows.

  Some people call symlinks "soft links" – a type of link in Li...'
---

Par Dillion Megida

Un symlink (également appelé lien symbolique) est un type de fichier sous Linux qui pointe vers un autre fichier ou un dossier sur votre ordinateur. Les symlinks sont similaires aux raccourcis sous Windows.

Certaines personnes appellent les symlinks « soft links » – un type de lien dans les systèmes Linux/UNIX – par opposition aux « hard links ».

## Différence entre un lien symbolique et un lien physique

Les liens symboliques (soft links) sont similaires aux raccourcis et peuvent pointer vers un autre fichier ou répertoire dans n'importe quel système de fichiers.

Les liens physiques (hard links) sont également des raccourcis pour les fichiers et les dossiers, mais un lien physique ne peut pas être créé pour un dossier ou un fichier dans un système de fichiers différent.

Examinons les étapes impliquées dans la création et la suppression d'un symlink. Nous verrons également ce que sont les liens rompus et comment les supprimer.

## Comment créer un symlink

La syntaxe pour créer un symlink est :

```shell
ln -s <chemin vers le fichier/dossier à lier> <le chemin du lien à créer>

```

`ln` est la commande de lien. Le drapeau `-s` spécifie que le lien doit être symbolique (soft). `-s` peut également être saisi sous la forme `-symbolic`.

Par défaut, la commande `ln` crée des liens physiques. L'argument suivant est le `chemin vers le fichier (ou dossier)` que vous souhaitez lier. (C'est-à-dire le fichier ou le dossier pour lequel vous souhaitez créer un raccourci.) 

Et le dernier argument est le `chemin du lien` lui-même (le raccourci).

## Comment créer un symlink pour un fichier – Exemple de commande

```shell
ln -s /home/james/transactions.txt trans.txt

```

Après avoir exécuté cette commande, vous pourrez accéder à `/home/james/transactions.txt` avec `trans.txt`. Toute modification apportée à `trans.txt` sera également répercutée dans le fichier d'origine.

Notez que cette commande ci-dessus créerait le fichier de lien `trans.txt` dans votre répertoire actuel. Vous pouvez également créer un fichier lié dans un dossier comme ceci :

```shell
ln -s /home/james/transactions.txt my-stuffs/trans.txt

```

Il doit déjà y avoir un répertoire nommé « my-stuffs » dans votre répertoire actuel – sinon la commande renverra une erreur.

## Comment créer un symlink pour un dossier – Exemple de commande

De la même manière que ci-dessus, nous utiliserions :

```shell
ln -s /home/james james

```

Cela créerait un dossier lié par symlink appelé « james » qui contiendrait le contenu de `/home/james`. Toute modification apportée à ce dossier lié affectera également le dossier d'origine.

## Comment supprimer un symlink

Avant de vouloir supprimer un symlink, vous voudrez peut-être confirmer qu'un fichier ou un dossier est un symlink, afin de ne pas altérer vos fichiers. 

Une façon de le faire est :

```shell
ls -l <chemin-vers-le-symlink-suppose>

```

L'exécution de cette commande sur votre terminal affichera les propriétés du fichier. Dans le résultat, si le premier caractère est une lettre minuscule L (« l »), cela signifie que le fichier/dossier est un symlink.

Vous verrez également une flèche (->) à la fin indiquant le fichier/dossier vers lequel le symlink pointe.

Il existe deux méthodes pour supprimer un symlink :

### Comment utiliser unlink pour supprimer un symlink

La syntaxe est :

```shell
unlink <chemin-vers-le-symlink>

```

Cela supprime le symlink si le processus réussit.

Même si le symlink se présente sous la forme d'un dossier, n'ajoutez pas « / », car Linux supposera qu'il s'agit d'un répertoire et `unlink` ne peut pas supprimer de répertoires.

### Comment utiliser rm pour supprimer un symlink 

Comme nous l'avons vu, un symlink n'est qu'un autre fichier ou dossier pointant vers un fichier ou un dossier d'origine. Pour supprimer cette relation, vous pouvez supprimer le fichier lié.

Par conséquent, la syntaxe est :

```shell
rm <chemin-vers-le-symlink>

```

Par exemple :

```shell
rm trans.txt
rm james

```

Notez qu'essayer de faire `rm james/` entraînerait une erreur, car Linux supposera que « james/ » est un répertoire, ce qui nécessiterait d'autres options comme `r` et `f`. Mais ce n'est pas ce que nous voulons. Un symlink peut être un dossier, mais nous ne nous intéressons qu'au nom.

Le principal avantage de `rm` par rapport à `unlink` est que vous pouvez supprimer plusieurs symlinks à la fois, comme vous pouvez le faire avec des fichiers.

## Comment trouver et supprimer les liens rompus

Les liens rompus se produisent lorsque le fichier ou le dossier vers lequel pointe un symlink change de chemin ou est supprimé.

Par exemple, si « transactions.txt » passe de `/home/james` à `/home/james/personal`, le lien « trans.txt » devient rompu. Toute tentative d'accès au fichier entraînera une erreur « No such file or directory » (Aucun fichier ou répertoire de ce type). C'est parce que le lien n'a pas de contenu propre.

Lorsque vous découvrez des liens rompus, vous pouvez facilement supprimer le fichier. Un moyen simple de trouver des symlinks rompus est :

```shell
find /home/james -xtype l

```

Cela listera tous les symlinks rompus dans le répertoire `james` – des fichiers aux répertoires en passant par les sous-répertoires.

Passer l'option `-delete` les supprimera comme ceci :

```shell
find /home/james -xtype l -delete

```

## Conclusion

Les liens symboliques sont une fonctionnalité intéressante des systèmes Linux et UNIX. 

Vous pouvez créer des symlinks facilement accessibles pour vous référer à un fichier ou à un dossier qui ne serait autrement pas pratique d'accès. Avec un peu de pratique, vous comprendrez comment ils fonctionnent de manière intuitive, et ils vous rendront beaucoup plus efficace dans la gestion des systèmes de fichiers.