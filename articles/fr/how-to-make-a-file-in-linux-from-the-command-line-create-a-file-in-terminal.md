---
title: Comment créer un fichier sous Linux depuis la ligne de commande – Créer un
  fichier dans le terminal
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2023-01-05T18:58:23.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-a-file-in-linux-from-the-command-line-create-a-file-in-terminal
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/Copy-of-Copy-of-read-write-files-python--3-.png
tags:
- name: Linux
  slug: linux
seo_title: Comment créer un fichier sous Linux depuis la ligne de commande – Créer
  un fichier dans le terminal
seo_desc: "Managing files from the command line is one of the most common tasks for\
  \ a Linux user. \nFiles are created, edited, deleted, and used by many of the background\
  \ OS processes. Files are also used by regular users to accomplish daily tasks such\
  \ as taking..."
---

Gérer des fichiers depuis la ligne de commande est l'une des tâches les plus courantes pour un utilisateur Linux. 

Les fichiers sont créés, modifiés, supprimés et utilisés par de nombreux processus du système d'exploitation en arrière-plan. Les fichiers sont également utilisés par les utilisateurs réguliers pour accomplir des tâches quotidiennes telles que prendre des notes, écrire du code ou simplement dupliquer du contenu.

Dans cet article, nous verrons trois méthodes permettant de créer des fichiers en utilisant le terminal. Les trois commandes que nous allons discuter sont `touch`, `cat` et `echo`.

### Prérequis :

Vous devez avoir accès au terminal Linux pour essayer les commandes mentionnées dans ce tutoriel. Vous pouvez accéder au terminal de l'une des manières suivantes :

* Installer une distribution Linux de votre choix sur votre système. 
* Utiliser WSL (Windows Subsystem for Linux), si vous souhaitez utiliser Windows et Linux côte à côte. [Voici](https://www.freecodecamp.org/news/how-to-install-wsl2-windows-subsystem-for-linux-2-on-windows-10/) un guide pour le faire.
* Utiliser [Replit](https://replit.com/) qui est un IDE basé sur le navigateur. Vous pouvez créer un projet Bash et accéder au terminal immédiatement.

## Méthode #1 : Comment créer des fichiers en utilisant la commande `touch` 

La commande `touch` crée des fichiers vides. Vous pouvez l'utiliser pour créer plusieurs fichiers également.

**Syntaxe de la commande `touch` :**

```bash
 touch NOM_DU_FICHIER
```

**Exemples de la commande `touch` :**

Créons un seul fichier vide en utilisant la syntaxe fournie ci-dessus.

```bash
touch access.log
```

Ensuite, nous allons créer plusieurs fichiers en fournissant les noms de fichiers séparés par des espaces après la commande `touch`. 

```bash
touch mod.log messages.log security.log
```

La commande ci-dessus créera trois fichiers vides séparés nommés `mod.log`, `messages.log` et `security.log`.

## Méthode #2 : Comment créer des fichiers en utilisant la commande `cat` 

La commande `cat` est le plus souvent utilisée pour afficher le contenu d'un fichier. Mais vous pouvez également l'utiliser pour créer des fichiers.

**Syntaxe de la commande `cat` :**

```bash
cat > nomdufichier
```

Cela vous demandera de saisir le texte que vous pouvez enregistrer et quitter en appuyant sur `ctrl+c`.

```bash
cat > sample.txt
```

 Lorsque je saisis la commande ci-dessus, la sortie de mon terminal ressemble à ceci :

```bash
zaira@Zaira:~$ cat > sample.txt
Ceci est un fichier exemple créé en utilisant la commande "cat"
^C
```

Remarquez le signe `^C`, qui correspond à `Ctrl+c` et indique au terminal d'enregistrer et de quitter.

Voici le contenu du fichier créé :

```bash
zaira@Zaira:~$ more sample.txt
Ceci est un fichier exemple créé en utilisant la commande "cat"
```

## Méthode #3 : Comment créer des fichiers en utilisant la commande `echo` 

La commande `echo` est utilisée pour ajouter et ajouter du texte aux fichiers. Elle crée également le fichier s'il n'existe pas déjà.

**Syntaxe de la commande `echo` :**

```bash
echo "du texte" > sample.txt
```

ou

```bash
echo "du texte" >> sample.txt
```

La différence entre `>` et `>>` est que `>` écrase le fichier s'il existe alors que `>>` ajoute au fichier existant. 

Si vous souhaitez suivre le tutoriel vidéo de cet article, voici le lien :

%[https://youtu.be/IQ8R7br-EuY]

## Conclusion

Dans cet article, nous avons discuté de trois méthodes différentes pour créer des fichiers dans la ligne de commande Linux. J'espère que vous avez trouvé ce tutoriel utile.

Quelle est la chose préférée que vous avez apprise dans ce tutoriel ? Faites-le moi savoir sur [Twitter](https://twitter.com/hira_zaira) !

Vous pouvez lire mes autres articles [ici](https://www.freecodecamp.org/news/author/zaira/).