---
title: Comment annuler un Git Add
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-13T17:45:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-undo-a-git-add
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9deb740569d1a4ca3a5e.jpg
tags:
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: version control
  slug: version-control
seo_title: Comment annuler un Git Add
seo_desc: 'To undo git add before a commit, run git reset <file> or git reset to unstage
  all changes.

  In older versions of Git, the commands were git reset HEAD <file> and git reset
  HEAD respectively. This was changed in Git 1.8.2

  You can read more about other ...'
---

Pour annuler `git add` avant un commit, exécutez `git reset <file>` ou `git reset` pour désindexer toutes les modifications.

Dans les anciennes versions de Git, les commandes étaient `git reset HEAD <file>` et `git reset HEAD` respectivement. Cela a été changé dans Git 1.8.2

Vous pouvez en savoir plus sur d'autres actions Git couramment utilisées dans ces articles utiles :

* [Git checkout](https://guide.freecodecamp.org/git/git-checkout/)
* [Git pull vs Git fetch](https://guide.freecodecamp.org/miscellaneous/git-pull-vs-git-fetch/)
* [Gitignore](https://guide.freecodecamp.org/git/gitignore/)

## Voici quelques informations supplémentaires sur Git

### **Comprendre les trois sections d'un projet Git**

Un projet Git aura les trois sections principales suivantes :

1. Répertoire Git
2. Répertoire de travail (ou arbre de travail)
3. Zone de staging

Le **répertoire Git** (situé dans `YOUR-PROJECT-PATH/.git/`) est l'endroit où Git stocke tout ce dont il a besoin pour suivre précisément le projet. Cela inclut les métadonnées et une base de données d'objets qui contient des versions compressées des fichiers du projet.

Le **répertoire de travail** est l'endroit où un utilisateur apporte des modifications locales à un projet. Le répertoire de travail extrait les fichiers du projet de la base de données d'objets du répertoire Git et les place sur la machine locale de l'utilisateur.

La **zone de staging** est un fichier (également appelé "index", "stage", ou "cache") qui stocke des informations sur ce qui sera inclus dans votre prochain commit. Un commit est lorsque vous dites à Git d'enregistrer ces modifications indexées. Git prend un instantané des fichiers tels qu'ils sont et stocke définitivement cet instantané dans le répertoire Git.

Avec trois sections, il y a trois états principaux qu'un fichier peut avoir à tout moment : validé, modifié, ou indexé. Vous _modifiez_ un fichier chaque fois que vous apportez des modifications dans votre répertoire de travail. Ensuite, il est _indexé_ lorsque vous le déplacez vers la zone de staging. Enfin, il est _validé_ après un commit.

## **Installer Git**

* Ubuntu : `sudo apt-get install git`
* Windows : [Télécharger](https://git-scm.com/download/win)
* Mac : [Télécharger](https://git-scm.com/download/mac)

## Configurer l'environnement Git

Git dispose d'un outil `git config` qui vous permet de personnaliser votre environnement Git. Vous pouvez modifier l'apparence et le fonctionnement de Git en définissant certaines variables de configuration. Exécutez ces commandes à partir d'une interface de ligne de commande sur votre machine (Terminal sur Mac, Invite de commandes ou Powershell sur Windows).

Il existe trois niveaux où ces variables de configuration sont stockées :

1. Système : situé dans `/etc/gitconfig`, applique les paramètres par défaut à tous les utilisateurs de l'ordinateur. Pour apporter des modifications à ce fichier, utilisez l'option `--system` avec la commande `git config`.
2. Utilisateur : situé dans `~/.gitconfig` ou `~/.config/git/config`, applique les paramètres à un seul utilisateur. Pour apporter des modifications à ce fichier, utilisez l'option `--global` avec la commande `git config`.
3. Projet : situé dans `YOUR-PROJECT-PATH/.git/config`, applique les paramètres au projet uniquement. Pour apporter des modifications à ce fichier, utilisez la commande `git config`.

Si des paramètres entrent en conflit les uns avec les autres, les configurations au niveau du projet remplaceront celles au niveau utilisateur, et les configurations au niveau utilisateur remplaceront celles au niveau système.

**Note pour les utilisateurs Windows** : Git recherche le fichier de configuration au niveau utilisateur (`.gitconfig`) dans votre répertoire `$HOME` (`C:\Users\$USER`). Git recherche également `/etc/gitconfig`, bien qu'il soit relatif à la racine MSys, qui est l'endroit où vous décidez d'installer Git sur votre système Windows lorsque vous exécutez l'installateur. Si vous utilisez la version 2.x ou ultérieure de Git pour Windows, il existe également un fichier de configuration au niveau système dans `C:\Documents and Settings\All Users\Application Data\Git\config` sur Windows XP, et dans `C:\ProgramData\Git\config` sur Windows Vista et versions ultérieures. Ce fichier de configuration ne peut être modifié que par `git config -f FILE` en tant qu'administrateur.

### Ajoutez votre nom et votre email

Git inclut le nom d'utilisateur et l'email dans les informations d'un commit. Vous voudrez configurer cela dans votre fichier de configuration au niveau utilisateur avec ces commandes :

```shell
git config --global user.name "My Name"
git config --global user.email "myemail@example.com"
```

### Changez votre éditeur de texte

Git utilise automatiquement votre éditeur de texte par défaut, mais vous pouvez le changer. Voici un exemple pour utiliser l'éditeur Atom à la place (l'option `--wait` indique au shell d'attendre l'éditeur de texte pour que vous puissiez y travailler avant que le programme ne continue) :

```shell
git config --global core.editor "atom --wait"
```

### Ajoutez de la couleur à la sortie Git

Vous pouvez configurer votre shell pour ajouter de la couleur à la sortie Git avec cette commande :

```shell
git config --global color.ui true
```

Pour voir tous vos paramètres de configuration, utilisez la commande `git config --list`.

## Initialiser Git dans un projet

Une fois Git installé et configuré sur votre ordinateur, vous devez l'initialiser dans votre projet pour commencer à utiliser ses fonctionnalités de contrôle de version. Dans la ligne de commande, utilisez la commande `cd` pour naviguer vers le dossier de niveau supérieur (ou racine) de votre projet. Ensuite, exécutez la commande `git init`. Cela installe un dossier de répertoire Git avec tous les fichiers et objets dont Git a besoin pour suivre votre projet.

Il est important que le répertoire Git soit installé dans le dossier racine du projet. Git peut suivre les fichiers dans les sous-dossiers, mais il ne suivra pas les fichiers situés dans un dossier parent par rapport au répertoire Git.

## Obtenir de l'aide dans Git

Si vous oubliez comment fonctionne une commande dans Git, vous pouvez accéder à l'aide Git depuis la ligne de commande de plusieurs manières :

```shell
git help COMMAND
git COMMAND --help
man git-COMMAND
```

Cela affiche la page de manuel pour la commande dans votre fenêtre de shell. Pour naviguer, faites défiler avec les touches fléchées haut et bas ou utilisez les raccourcis clavier suivants :

* f ou barre d'espace pour avancer d'une page
* b pour reculer d'une page
* q pour quitter