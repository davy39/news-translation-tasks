---
title: Comment supprimer un répertoire sous Linux – Commande pour supprimer un dossier
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-06-08T17:11:56.000Z'
originalURL: https://freecodecamp.org/news/how-to-remove-a-directory-in-linux
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/delete-folders-command.png
tags:
- name: command line
  slug: command-line
- name: Linux
  slug: linux
seo_title: Comment supprimer un répertoire sous Linux – Commande pour supprimer un
  dossier
seo_desc: 'By Dillion Megida

  If you''re using a user interface, you can right-click on a directory and select
  "Delete" or "Move to Bin". But how do you do this on the terminal? I''ll explain
  that in this article.

  How to Remove a Directory in Linux

  There are two w...'
---

Par Dillion Megida

Si vous utilisez une interface utilisateur, vous pouvez faire un clic droit sur un répertoire et sélectionner "Supprimer" ou "Déplacer vers la corbeille". Mais comment faire cela dans le terminal ? Je vais expliquer cela dans cet article.

## Comment supprimer un répertoire sous Linux

Il existe deux façons de supprimer des répertoires sous Linux : les commandes **rm** et **rmdir**.

En résumé, la commande **rm** supprime des répertoires qui peuvent contenir du contenu tel que des fichiers et des sous-répertoires, tandis que **rmdir** supprime UNIQUEMENT les répertoires vides.

De plus, les deux commandes suppriment les répertoires de manière permanente (plutôt que de les déplacer vers la corbeille), alors soyez prudent lorsque vous les utilisez.

Examinons les deux commandes plus en détail.

## Comment utiliser la commande Linux `rm`

Vous utilisez la commande `rm` pour supprimer des fichiers et des répertoires sous Linux. Pour les répertoires, cette commande peut être utilisée pour supprimer entièrement un répertoire, c'est-à-dire qu'elle supprime un répertoire et tous les fichiers et sous-répertoires qu'il contient.

Voici la syntaxe de cette commande :

```bash
rm [options] [fichiers et/ou répertoires]
```

Pour supprimer un fichier, par exemple `test.txt`, vous pouvez utiliser la commande sans options comme ceci :

```bash
rm test.txt
```

Pour les répertoires, vous devez fournir certaines options de drapeau.

### Comment supprimer un dossier avec son contenu

Pour un répertoire contenant du contenu, vous devez fournir le drapeau `-r`. Sans utiliser ce drapeau comme ceci :

```bash
rm test
```

Vous obtiendrez cette erreur : **rm : test : est un répertoire**

Le drapeau `-r` informe la commande `rm` de supprimer récursivement le contenu d'un répertoire (qu'il s'agisse de fichiers ou de sous-répertoires). Vous pouvez donc supprimer un répertoire comme ceci :

```bash
rm -r test
```

### Comment supprimer un dossier vide

Pour un dossier vide, vous pouvez toujours fournir le drapeau `-r`, mais le drapeau dédié `-d` s'applique à ce cas. Sans ce drapeau, vous obtiendrez la même erreur **rm : [dossier] : est un répertoire**.

Pour supprimer un répertoire vide, vous pouvez utiliser cette commande :

```bash
rm -d test
```

Il est recommandé d'utiliser le drapeau `-d` pour les cas de répertoires vides plutôt que le drapeau `-r` car le drapeau `-d` garantit qu'un répertoire est vide.

S'il n'est pas vide, vous obtiendrez l'erreur **rm : test : Répertoire non vide**. Donc, pour être sûr que vous effectuez l'opération de répertoire vide appropriée, utilisez le drapeau `-d`.

## Comment utiliser la commande Linux `rmdir`

La commande `rmdir` est spécifiquement utilisée pour supprimer des répertoires vides. La syntaxe est :

```bash
rmdir [dossiers]
```

C'est l'équivalent de la commande `rm` avec le drapeau `-d` : `rm -d`.

Lorsque vous utilisez `rmdir` sur un répertoire non vide, vous obtenez cette erreur : **rmdir : [dossier] : Répertoire non vide**.

Pour supprimer un répertoire vide, utilisez cette commande sans options :

```bash
rmdir test
```

La commande `rmdir` dispose également du drapeau `-p`, qui vous permet de supprimer un répertoire ainsi que son parent dans l'arborescence. Par exemple, si vous avez cette structure de fichiers :

```bash
> Test
---> Test22
```

Dans ce cas, **Test** est un répertoire qui contient le sous-répertoire **Test2**. Si vous supprimez le répertoire **Test2**, **Test** devient un répertoire vide. Au lieu de faire :

```bash
rmdir Test/Test2 Test
# suppression de Test2 puis de Test
```

Vous pouvez utiliser le drapeau `-p` comme ceci :

```bash
rmdir -p Test/Test2
```

Cette commande supprimera **Test2** puis supprimera **Test**, le parent dans l'arborescence. Mais cette commande générera une erreur si l'un des répertoires n'est pas vide.

## Comment supprimer des répertoires correspondant à un motif sous Linux

Vous pouvez également utiliser **rm** et **rmdir** avec des motifs glob. [Le globbing est similaire à Regex](https://dillionmegida.com/p/regex-vs-glob-patterns/), mais le premier est utilisé pour faire correspondre des noms de fichiers dans le terminal.

Par exemple, si vous souhaitez supprimer les répertoires **test1**, **test2** et **test3**, au lieu d'exécuter :

```bash
rm -r test1 test2 test3

# ou s'ils sont vides

rmdir test1 test2 test3
```

Vous pouvez utiliser un motif glob avec un caractère générique comme ceci :

```bash
rm -r test*

# ou s'ils sont vides

rmdir test*
```

L'**astérisque \*** correspond à tout mélange de caractères après le mot "test". Vous pouvez également appliquer d'autres motifs glob. Pour en savoir plus, consultez la [documentation sur le globbing](https://linux.die.net/man/7/glob)

## Conclusion

Maintenant, vous savez comment supprimer des répertoires sous Linux à partir de la ligne de commande. Vous avez appris les commandes `rm` et `rmdir` et quand utiliser chacune.

Bonne programmation !