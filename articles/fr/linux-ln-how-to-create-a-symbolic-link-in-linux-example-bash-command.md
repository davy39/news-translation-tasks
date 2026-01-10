---
title: Linux ln – Comment créer un lien symbolique sous Linux [Exemple de commande
  Bash]
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2022-02-21T16:05:08.000Z'
originalURL: https://freecodecamp.org/news/linux-ln-how-to-create-a-symbolic-link-in-linux-example-bash-command
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/gabriel-heinzer-4Mw7nkQDByk-unsplash.jpg
tags:
- name: Bash
  slug: bash
- name: Linux
  slug: linux
seo_title: Linux ln – Comment créer un lien symbolique sous Linux [Exemple de commande
  Bash]
seo_desc: "A symlink (symbolic) is a type of file that points to other files or directories\
  \ (folders) in Linux. \nYou can create a symlink (symbolic) by using the ln command\
  \ in the command line. \nSymbolic links are useful because they act as shortcuts\
  \ to a file ..."
---

Un lien symbolique (symlink) est un type de fichier qui pointe vers d'autres fichiers ou répertoires (dossiers) sous Linux. 

Vous pouvez créer un lien symbolique (symlink) en utilisant la commande `ln` dans la ligne de commande. 

Les liens symboliques sont utiles car ils agissent comme des raccourcis vers un fichier ou un répertoire. 

Dans cet article, je vais expliquer comment utiliser la commande `ln` pour créer un lien symbolique vers un fichier ou un répertoire. 

## Quelle est la différence entre les liens symboliques et les liens physiques sous Linux ? 

Un lien symbolique ou lien souple pointera vers le fichier original sur votre système. Un lien physique créera une copie du fichier.

Les liens symboliques peuvent pointer vers d'autres fichiers ou répertoires sur un système de fichiers différent, alors que les liens physiques ne le peuvent pas. 

## Comment créer un lien symbolique vers un fichier

Vous pouvez trouver la ligne de commande en utilisant l'application Terminal sur Mac ou l'invite de commande sur Windows. 

Voici la syntaxe de base pour créer un lien symbolique vers un fichier dans votre terminal.

```bash
ln -s fichier_source_existant lien_symbolique_facultatif

```

Vous utilisez la commande `ln` pour créer les liens pour les fichiers et l'option `-s` pour spécifier que ce sera un lien symbolique. Si vous omettez l'option `-s`, alors un lien physique sera créé à la place.

Le fichier_source_existant représente le fichier sur votre ordinateur pour lequel vous souhaitez créer le lien symbolique. 

Le paramètre lien_symbolique_facultatif est le nom du lien symbolique que vous souhaitez créer. Si omis, le système créera un nouveau lien pour vous dans le répertoire courant où vous vous trouvez. 

Examinons un exemple pour mieux comprendre comment cela fonctionne.

Sur mon bureau, j'ai un fichier appelé `example_fcc_file.txt`. 

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screen-Shot-2022-02-19-at-7.48.02-PM.png)

Je dois d'abord ouvrir mon terminal, puis m'assurer que je suis dans le répertoire Bureau. Je peux exécuter la commande `cd Bureau` pour naviguer vers mon Bureau.

Après avoir exécuté cette commande, vous devriez voir que vous êtes maintenant dans le Bureau. 

```bash
jessicawilkins@Dedrias-MacBook-Pro-2 ~ % cd Bureau
jessicawilkins@Dedrias-MacBook-Pro-2 Bureau % 
```

Je peux ensuite utiliser la commande `ln` pour créer un nouveau lien symbolique appelé `fcc_link.txt`.

```bash
ln -s example_fcc_file.txt fcc_link.txt
```

Lorsque vous exécutez cette commande dans le terminal, vous remarquerez que rien n'a été retourné. C'est parce que lorsque la commande `ln` réussit, il n'y a aucune sortie et elle retourne zéro.

```bash
jessicawilkins@Dedrias-MacBook-Pro-2 Bureau % ln -s example_fcc_file.txt fcc_link.txt


jessicawilkins@Dedrias-MacBook-Pro-2 Bureau % 
```

Pour vérifier que votre lien symbolique a été créé avec succès, vous pouvez utiliser la commande `ls`. La commande `ls` listera les informations sur les fichiers et le flag `-l` représente le lien symbolique. 

```bash
ls -l fcc_link.txt
```

Lorsque vous exécutez cette commande, vous devriez voir ce type de résultat dans le terminal. 

```bash
lrwxr-xr-x  1 jessicawilkins  staff  20 Feb 19 19:56 fcc_link.txt -> example_fcc_file.txt

```

La partie `fcc_link.txt -> example_fcc_file.txt` de la sortie vous montre que le lien symbolique pointe vers le fichier appelé `example_fcc_file.txt`. 

Vous devriez également voir que le nouveau lien symbolique apparaît dans votre répertoire.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screen-Shot-2022-02-19-at-8.11.09-PM.png)

## Comment créer un lien symbolique vers un répertoire

Dans cet exemple, nous voulons créer un lien symbolique appelé `my_music` qui pointera vers mon dossier Musique dans le répertoire personnel de mon ordinateur.

Tout d'abord, assurez-vous que vous êtes dans le répertoire personnel. Vous pouvez exécuter `cd` pour revenir à votre répertoire personnel dans la ligne de commande.

```bash
jessicawilkins@Dedrias-MacBook-Pro-2 Bureau % cd
jessicawilkins@Dedrias-MacBook-Pro-2 ~ % 
```

Vous pouvez ensuite utiliser la commande `ln` pour créer un lien symbolique vers le répertoire Musique.

```bash
ln -s /Users/jessicawilkins/Music ~/my_music

```

Si tout se passe bien, vous devriez le voir dans le répertoire personnel.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screen-Shot-2022-02-19-at-8.38.14-PM.png)

## Comment supprimer un lien symbolique

Pour supprimer un lien symbolique, vous pouvez utiliser soit la commande `unlink`, soit la commande `rm`.

Si nous voulions supprimer le lien symbolique `fcc_link.txt` que nous avons créé précédemment, nous pourrions utiliser l'une de ces commandes :

```bash
rm fcc_link.txt
```

```bash
unlink fcc_link.txt
```

Maintenant, nous devrions voir que le lien symbolique a été supprimé de notre répertoire.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screen-Shot-2022-02-19-at-8.47.30-PM.png)

## Comment écraser les liens symboliques

Si nous essayons de créer un nouveau lien symbolique appelé `fcc_link.txt`, cela entraînera une erreur car il est déjà utilisé et pointe vers un autre fichier. 

```bash
ln: fcc_link.txt: Le fichier existe

```

Vous pouvez écraser cette erreur en utilisant l'option force (`-f`).

```bash
ln -sf example_fcc_file.txt fcc_link.txt
```

## Comment en savoir plus sur la commande ln

Si vous souhaitez en savoir plus sur la commande `ln`, vous pouvez la lire dans les pages `man` (manuel pour l'utilisation des commandes Linux).

Exécutez `man ln` dans votre terminal et vous devriez voir les pages man pour la commande `ln`.

```
LN(1)                     BSD General Commands Manual                    LN(1)

NOM
     link, ln -- créer des liens

SYNOPSIS
     ln [-Ffhinsv] fichier_source [fichier_cible]
     ln [-Ffhinsv] fichier_source ... répertoire_cible
     link fichier_source fichier_cible

DESCRIPTION
     L'utilitaire ln crée une nouvelle entrée de répertoire (fichier lié) qui a les mêmes modes que le fichier original. Il est
     utile pour maintenir plusieurs copies d'un fichier à plusieurs endroits à la fois sans utiliser d'espace de stockage pour les
     « copies » ; au lieu de cela, un lien « pointe » vers la copie originale. Il existe deux types de liens ; les liens physiques et les liens sym-
     boliques. La manière dont un lien « pointe » vers un fichier est l'une des différences entre un lien physique et un lien symbolique.

     Les options sont les suivantes :

     -F    Si le fichier cible existe déjà et est un répertoire, alors le supprimer afin que le lien puisse être créé. L'option -F
           doit être utilisée avec les options -f ou -i. Si aucune n'est spécifiée, -f est implicite. L'option -F
           est une opération nulle sauf si l'option -s est spécifiée.

     -h    Si le fichier_cible ou répertoire_cible est un lien symbolique, ne pas le suivre. Cela est le plus utile avec l'option -f,
           pour remplacer un lien symbolique qui peut pointer vers un répertoire.

     -f    Si le fichier cible existe déjà, alors le désassocier afin que le lien puisse être créé. (L'option -f remplace
```

## Conclusion

Un lien symbolique (symlink) est un type de fichier qui pointe vers d'autres fichiers ou répertoires (dossiers) sous Linux. Vous pouvez créer un lien symbolique (symlink) en utilisant la commande `ln` dans la ligne de commande. 

Les liens symboliques sont utiles car ils agissent comme des raccourcis vers un fichier ou un répertoire. 

Voici la syntaxe de base pour créer un lien symbolique vers un fichier en utilisant le terminal :

```bash
ln -s fichier_source_existant lien_symbolique_facultatif
```

Voici la syntaxe de base pour créer un lien symbolique vers un répertoire en utilisant le terminal :

```bash
ln -s chemin_vers_repertoire_existant nom_du_lien_symbolique

```

Pour supprimer un lien symbolique, vous pouvez utiliser soit la commande `unlink`, soit la commande `rm` :

```bash
rm nom_du_lien_symbolique
```

```bash
unlink nom_du_lien_symbolique
```

Si vous devez écraser un lien symbolique, vous pouvez utiliser cette commande :

```bash
ln -sf chemin_vers_repertoire_existant nom_du_lien_symbolique
```

J'espère que vous avez apprécié cet article sur les liens symboliques et je vous souhaite bonne chance dans votre parcours de programmation.