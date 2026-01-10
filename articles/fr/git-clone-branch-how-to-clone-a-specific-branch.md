---
title: Git Clone Branch – Comment cloner une branche spécifique
subtitle: ''
author: Bolaji Ayodeji
co_authors: []
series: null
date: '2020-06-30T18:56:31.000Z'
originalURL: https://freecodecamp.org/news/git-clone-branch-how-to-clone-a-specific-branch
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/article-banner--1-.gif
tags:
- name: 100DaysOfCode
  slug: 100daysofcode
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: programing
  slug: programing
- name: terminal
  slug: terminal
seo_title: Git Clone Branch – Comment cloner une branche spécifique
seo_desc: Unlike older centralized version control systems such as SVN and CVS, Git
  is distributed. Every developer has the full history and control of their code locally
  or remotely. They can also access or manipulate several parts of the code as they
  deem fi...
---

Contrairement aux anciens systèmes centralisés de contrôle de version tels que SVN et CVS, Git est distribué. Chaque développeur dispose de l'historique complet et du contrôle de son code localement ou à distance. Ils peuvent également accéder ou manipuler plusieurs parties du code comme ils le jugent approprié depuis différents emplacements.

Depuis que Linus Torvalds (le célèbre créateur du noyau du système d'exploitation Linux) a créé Git en 2005 pour le développement du noyau Linux, il est devenu le système de contrôle de version moderne le plus utilisé au monde.

Dans cet article, je vais vous présenter les workflows Git clone et Git branch, et je vais vous montrer comment vous pouvez cloner une branche spécifique en fonction de vos besoins. Commençons ! 💡

## Prérequis

* Connaissance de base du terminal

* Capacité à taper des commandes dans le terminal

* Git installé (je vais quand même vous montrer comment faire)

* Un compte GitHub

* Un sourire sur votre visage (Mettez ce sourire, ami 😊)

## Brève introduction à Git et GitHub

Selon [Wikipedia](https://en.wikipedia.org/wiki/Git),

> **Git** est un système de contrôle de version distribué conçu pour suivre les modifications d'un projet (code) dans le développement logiciel. Il est destiné à renforcer la coordination, la collaboration, la vitesse et l'efficacité parmi les développeurs.

**GitHub**, en revanche, est un service d'hébergement basé sur le web pour le contrôle de version utilisant Git. Il offre toutes les fonctionnalités de contrôle de version distribué et de gestion du code source de Git, ainsi que des fonctionnalités supplémentaires pour le code informatique.

## Comment installer Git sur Windows

Téléchargez et installez le dernier [installateur Git pour Windows ici](https://git-for-windows.github.io/).

## Comment installer Git sur Linux

Voici les commandes en fonction de votre distribution Linux :

### Debian ou Ubuntu

```python
sudo apt-get update
sudo apt-get install git
```

### Fedora

```python
sudo dnf install git
```

### CentOS

```python
sudo yum install git
```

### Arch Linux

```python
sudo pacman -Sy git
```

### Gentoo

```python
sudo emerge --ask --verbose dev-vcs/git
```

## Comment installer Git sur un Mac

Téléchargez et installez le dernier [installateur Git pour Mac ici](https://sourceforge.net/projects/git-osx-installer/files/).

Ou vous pouvez taper cette commande :

```python
brew install git
```

Maintenant que nous avons installé Git, passons au tutoriel.

## Introduction à Git Clone

Git vous permet de gérer et de versionner votre/vos projet(s) dans un "dépôt". Ce dépôt est stocké sur un service d'hébergement basé sur le web pour le contrôle de version, comme GitHub.

Vous pouvez ensuite cloner ce dépôt sur votre machine locale et avoir tous les fichiers et branches localement (j'expliquerai plus sur les branches bientôt).

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-23-at-5.47.48-AM.png align="left")

Par exemple, vous pouvez cloner le dépôt de freeCodeCamp avec SSH comme suit :

```python
git clone git@github.com:freeCodeCamp/freeCodeCamp.git
```

## Introduction aux branches Git

Lorsque vous travaillez sur un projet, vous aurez probablement différentes fonctionnalités. Et plusieurs contributeurs travailleront sur ce projet et ses fonctionnalités.

Les branches vous permettent de créer un "bac à sable" avec les mêmes fichiers que dans la branche `master`. Vous pouvez utiliser cette branche pour construire des fonctionnalités indépendantes, tester de nouvelles fonctionnalités, apporter des modifications majeures, créer des correctifs, rédiger des documents ou essayer des idées sans casser ou affecter le code de production. Une fois terminé, vous fusionnez la branche dans la branche de production `master`.

La gestion des branches est un concept central dans Git, également utilisé dans GitHub pour gérer les workflows de différentes versions d'un même projet. La branche `master` est toujours la branche par défaut dans un dépôt, souvent considérée comme "code de production et déployable". De nouvelles branches comme `passwordless-auth` ou `refactor-signup-ux` peuvent être créées à partir de la branche `master`.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-22-at-2.47.53-AM.png align="left")

*Toutes les branches dans le dépôt de freeCodeCamp*

## Comment cloner des branches Git

Bien que vous puissiez cloner des dépôts avec la commande `git clone`, gardez à l'esprit que cela clone la branche et le `HEAD` distant. Il s'agit généralement de `master` par défaut et inclut toutes les autres branches du dépôt.

Ainsi, lorsque vous clonez un dépôt, vous clonez le `master` et toutes les autres branches. Cela signifie que vous devrez basculer vers une autre branche vous-même.

Supposons que votre tâche sur un projet est de travailler sur une fonctionnalité pour ajouter une authentification sans mot de passe à un tableau de bord utilisateur. Et cette fonctionnalité se trouve dans la branche `passwordless-auth`.

Vous n'avez vraiment pas besoin de la branche `master` puisque votre "branche de fonctionnalité" sera fusionnée dans `master` par la suite. Comment alors cloner cette branche `passwordless-auth` sans récupérer toutes les autres branches avec "un tas de fichiers dont vous n'avez pas besoin" ?

J'ai créé ce dépôt d'exemple pour expliquer cela. Ce dépôt contient un simple blog construit avec Nextjs et a quatre branches factices :

* master

* dev

* staging

* passwordless-auth

Dans Nextjs, tout fichier à l'intérieur du dossier `pages/api` est mappé au chemin `/api/*` et sera traité comme un point de terminaison API au lieu d'une `page`. Dans notre dépôt, j'ai créé différentes API factices [dans ce répertoire](https://github.com/BolajiAyodeji/nextjs-blog/tree/master/pages/api) pour rendre chaque branche différente.

La branche `master` contient le fichier **pages/api/hello.js** tandis que `passwordless-auth` contient le fichier **pages/api/auth.js**. Chaque fichier retourne simplement une réponse texte factice. Voir la réponse de l'API hello de `master` [ici](https://nextjs-blog.bolajiayodeji.vercel.app/api/hello) (avec un message spécial pour vous 😊).

Clonons le dépôt :

```python
git clone git@github.com:BolajiAyodeji/nextjs-blog.git
```

Cela nous donne accès à toutes les branches de ce dépôt et vous pouvez facilement basculer entre chacune pour voir chaque version et ses fichiers.

```python
git branch -a
```

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-22-at-4.51.56-AM.png align="left")

Vous vous demandez d'où viennent les branches **remotes/origin/..** ?

Lorsque vous clonez un dépôt, vous tirez des données d'un dépôt sur Internet ou d'un serveur interne connu sous le nom de **remote**. Le mot origin est un alias créé par votre Git pour remplacer l'URL distante (vous pouvez changer ou spécifier un autre alias si vous le souhaitez).

Ces branches **remotes/origin/..** vous renvoient au dépôt d'origine que vous avez cloné depuis Internet afin que vous puissiez toujours effectuer des opérations de pull/push depuis l'origine.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-23-at-5.24.43-AM.png align="left")

Ainsi, lorsque vous clonez `master` sur votre machine, `remotes/origin/master` est la branche `master` d'origine sur Internet, et `master` est sur votre machine locale. Vous allez donc effectuer des opérations de pull/push depuis et vers `remotes/origin/master`.

En résumé, **Remote** est l'URL qui pointe vers le dépôt sur Internet tandis que **Origin** est un alias pour cette URL distante.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-23-at-5.28.06-AM.png align="left")

## Comment cloner une branche spécifique

Maintenant, clonons une branche spécifique à partir de notre dépôt de démonstration. Il existe deux façons de cloner une branche spécifique. Vous pouvez soit :

* Cloner le dépôt, récupérer toutes les branches et basculer immédiatement vers une branche spécifique.

* Cloner le dépôt et ne récupérer qu'une seule branche.

### Option Une

```python
git clone --branch <nomdelabranche> <url-du-depot-distant>
```

ou

```python
git clone -b <nomdelabranche> <url-du-depot-distant>
```

Avec cela, vous récupérez toutes les branches du dépôt, basculez vers celle que vous avez spécifiée, et la branche spécifique devient la branche locale configurée pour `git push` et `git pull`. Mais vous avez toujours récupéré tous les fichiers de chaque branche. Ce n'est peut-être pas ce que vous voulez, n'est-ce pas ? 🤔

Testons cela :

```python
 git clone -b passwordless-auth git@github.com:BolajiAyodeji/nextjs-blog.git
```

Cela configure automatiquement `passwordless-auth` comme branche locale mais suit toujours les autres branches.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-23-at-5.30.01-AM.png align="left")

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-30-at-3.27.31-AM.png align="left")

### Option Deux

```python
git clone --branch <nomdelabranche> --single-branch <url-du-depot-distant>
```

ou

```python
git clone -b <nomdelabranche> --single-branch <url-du-depot-distant>
```

Cela effectue la même action que l'option une, sauf que l'option `--single-branch` a été introduite dans la version 1.7.10 de Git et ultérieure. Elle vous permet de ne récupérer que les fichiers de la branche spécifiée sans récupérer les autres branches.

Testons cela :

```python
git clone -b passwordless-auth --single-branch git@github.com:BolajiAyodeji/nextjs-blog.git
```

Cela configure automatiquement `passwordless-auth` comme branche locale et ne suit que cette branche.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-23-at-5.31.12-AM.png align="left")

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-30-at-3.29.07-AM.png align="left")

Si vous exécutez `cd pages/api`, vous trouverez le fichier `auth.js` dans la branche `passwordless-auth` comme prévu dans la configuration précédente.

## Conclusion

Vous pourriez manquer d'Internet ou d'espace de stockage, mais vous devez travailler sur une tâche dans une branche spécifique. Ou vous pourriez vouloir cloner une branche spécifique avec des fichiers limités pour diverses raisons. Heureusement, Git vous offre la flexibilité de le faire. Faites travailler vos muscles et essayez-le, il y a beaucoup plus de "Git" à apprendre.

Une chose à la fois, d'accord ? ✨