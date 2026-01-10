---
title: Comment installer Laravel en utilisant Homestead sur Windows - La méthode facile
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-06-23T14:06:29.000Z'
originalURL: https://freecodecamp.org/news/a-simplified-approach-to-installing-laravel-using-homestead-on-windows-f5fc50e59af0
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9cb46d740569d1a4cacfb2.jpg
tags:
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: 'self-improvement '
  slug: self-improvement
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: Comment installer Laravel en utilisant Homestead sur Windows - La méthode
  facile
seo_desc: 'By Charles Freeborn

  The laravel documentation recommends using Homestead (a pre-packaged all in one
  vagrant box that includes Ubuntu 16.04, PHP 7.1, Nginx, Composer) to install laravel.
  Setting up a laravel project is easy, once you have homestead ru...'
---

Par Charles Freeborn

La [documentation](https://laravel.com/docs/5.5) de Laravel recommande d'utiliser Homestead (une boîte Vagrant tout-en-un pré-packagée qui inclut Ubuntu 16.04, PHP 7.1, Nginx, Composer) pour installer Laravel. La configuration d'un projet Laravel est facile, une fois que vous avez Homestead en cours d'exécution sur votre machine.

Dans cet article, nous allons examiner une approche simple pour installer Laravel sur un système Windows.

### Prérequis

Pour commencer, installez les éléments suivants ;

**Git** : Git servira de client SSH et nous utiliserons l'invite de commande Git Bash tout au long de la configuration. Cliquez [ici](https://git-scm.com/downloads) pour télécharger et installer Git sur votre système.

**Sublime Text** : Cela servira d'éditeur de texte pour construire l'application. Cliquez [ici](https://www.sublimetext.com/3) pour télécharger et installer Sublime Text. Ou vous pouvez installer n'importe quel éditeur de texte de votre choix comme [VS Code](https://code.visualstudio.com/), et [Atom](https://atom.io/).

Après avoir installé Git, ouvrez Git Bash et générez une paire de clés SSH. Pour ce faire, allez dans le répertoire personnel et exécutez la commande :

```
ssh-keygen -t rsa -C "votreemail@mail.com"
```

## Installation principale

**Étape un** : Pour commencer l'installation, nous devons télécharger et installer VirtualBox. Cliquez [ici](https://www.virtualbox.org/wiki/Downloads) pour télécharger et installer le programme d'installation pour Windows.

**Étape deux** : À ce stade, nous allons installer Vagrant qui servira de conteneur pour Homestead. Téléchargez et installez [Vagrant](https://www.vagrantup.com/downloads.html) pour Windows.

![Image](https://cdn-media-1.freecodecamp.org/images/OcpHX9rAnU6sDIjVvldUO-CkLMmvXBnYXXle)
_Page de téléchargement de Vagrant. Source : [https://www.vagrantup.com/downloads.ht](https://www.vagrantup.com/downloads.ht" rel="noopener" target="_blank" title=")ml_

**Étape trois** : Ayant installé VirtualBox et Vagrant, nous pouvons ajouter Laravel à la boîte Vagrant. Ouvrez maintenant Git Bash, et dans le répertoire personnel, exécutez cette commande :

```
vagrant box add laravel/homestead
```

Attendez qu'il se télécharge. Sélectionnez l'option pour VirtualBox, dans mon cas, c'est 2. Appuyez sur Entrée et attendez qu'il télécharge la boîte.

**Étape quatre** : Installez Homestead dans votre répertoire personnel, en exécutant cette commande :

```
git clone https://github.com/laravel/homestead.git Homestead
```

Une fois cela fait, utilisez Git Bash pour changer de répertoire vers le dossier Homestead et exécutez cette commande :

```
init.bat
```

## Configurer Homestead

Maintenant, nous sommes prêts à configurer Homestead. Ouvrez Sublime Text, allez dans Fichier, ouvrez le dossier et sélectionnez le dossier Homestead. Il se trouve sur C:/Homestead. Ouvrez le fichier Homestead.yaml comme montré dans le diagramme ci-dessous

![Image](https://cdn-media-1.freecodecamp.org/images/gtaHVA9lRoXOwpOvtcGsW92mFujcdgnSjS5z)

Notre attention se portera sur les sections dossiers et sites dans le fichier Homestead.yaml.

-map: ~/Code

Cela signifie simplement le dossier sur votre machine locale pour vos projets.

to: /home/vagrant/Code

Cela signifie simplement le dossier sur la machine virtuelle, qui se synchronisera avec le répertoire sur la machine locale.

Créez un dossier (j'ai nommé le mien sites) pour vos projets dans le répertoire personnel de votre machine locale. Le mien se trouve à C:/Users/username/sites.

Dans le fichier Homestead.yaml, changez -map: ~/Code en -map: ~/sites.

Changez également /home/vagrant/Code en /home/vagrant/sites

## Maintenant, installez Laravel

Maintenant, téléchargez l'installateur de Laravel en exécutant cette commande :

```
Composer global require "laravel/installer"
```

Une fois cela fait, exécutez cette commande :

```
vagrant up
```

puis cette commande :

```
vagrant ssh
```

affichera le dossier sites qui a été créé sur la machine locale

![Image](https://cdn-media-1.freecodecamp.org/images/Aps74ffBP5lMv67zTfvneOXMGQqL4OgyEmCs)

Changez de répertoire pour le dossier sites et vous êtes prêt à commencer votre projet Laravel.

Exécutez cette commande :

```
laravel new testsite
```

et attendez qu'il se télécharge. Hourra ! Nous sommes prêts à commencer

> « à construire quelque chose d'extraordinaire » !

## Configurer le site Nginx

Pour accéder à notre projet Laravel sur notre navigateur web, nous devons simplement configurer la propriété sites

« La propriété sites vous permet de mapper facilement un « domaine » à un dossier sur votre environnement Homestead. » — [doc](https://laravel.com/docs/5.4/homestead)

Créons un domaine pour notre site de test. Ouvrez le bloc-notes en tant qu'administrateur, allez dans Fichier et ouvrez les hôtes qui se trouvent à C:/Windows/System32/Drivers/etc/hosts et attribuez 127.0.0.1 à testsite.dev

![Image](https://cdn-media-1.freecodecamp.org/images/GqAWM3strkx2C31MvXC1aK9jAhNCJq7ut9cH)
_127.0.0.1 testsite.dev_

Dans le fichier homestead.yaml, changez homestead.app en testsite.dev et /home/vagrant/Code/Laravel/public en /home/vagrant/sites/public et exécutez la commande :

```
vagrant provision
```

Maintenant, ouvrez votre navigateur web et entrez testsite.dev:8000. Votre navigateur affichera la page Laravel comme montré sur la photo de couverture.

*Si cet article vous a été utile, partagez-le sur les réseaux sociaux afin que d'autres puissent le voir.*