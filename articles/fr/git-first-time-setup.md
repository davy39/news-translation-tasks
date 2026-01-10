---
title: Première configuration de Git
subtitle: ''
author: Bolaji Ayodeji
co_authors: []
series: null
date: '2019-07-21T20:49:25.000Z'
originalURL: https://freecodecamp.org/news/git-first-time-setup
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/article-banner--9-.png
tags:
- name: 100DaysOfCode
  slug: 100daysofcode
- name: Bash
  slug: bash
- name: Git
  slug: git
seo_title: Première configuration de Git
seo_desc: 'Git is a Free and Open Source Distributed Version Control System.

  By far, Git is the most widely used modern version control system in the world today.
  Git is a distributed and actively maintained open source project originally developed
  in 2005 by L...'
---

Git est un système de contrôle de version distribué, libre et open source.

De loin, Git est le système de contrôle de version moderne le plus largement utilisé dans le monde aujourd'hui. Git est un projet open source distribué et activement maintenu, initialement développé en 2005 par [Linus Torvalds](https://en.wikipedia.org/wiki/Linus_Torvalds), le célèbre créateur du noyau du système d'exploitation Linux.

Contrairement aux anciens systèmes de contrôle de version centralisés tels que SVN et CVS, Git est distribué : chaque développeur dispose de l'historique complet de son dépôt de code localement. Git fonctionne également bien sur une large gamme de systèmes d'exploitation et d'IDE (Environnements de Développement Intégrés).

Dans cet article, je vais vous montrer comment installer Git, le configurer pour la première fois, des conseils utiles et des ressources pour en apprendre davantage/maîtriser des concepts avancés de Git. C'est parti !

Je suppose que vous savez déjà ce qu'est le contrôle de version, si ce n'est pas le cas, consultez cette [présentation](http://slides.com/bolajiayodeji/introduction-to-version-control-with-git-and-github) pour en savoir plus.

Voici un rapide récapitulatif de ce que signifie le contrôle de version : Le contrôle de version est : le processus de gestion des modifications apportées au code source ou à un ensemble de fichiers au fil du temps.

Le contrôle de version est le processus de gestion des modifications apportées au code source ou à un ensemble de fichiers au fil du temps.

Les logiciels de contrôle de version gardent une trace de chaque modification du code dans une base de données spéciale. Si une erreur est commise, les développeurs peuvent restaurer et comparer les versions antérieures du code pour aider à corriger l'erreur tout en minimisant les perturbations pour tous les membres de l'équipe ou les contributeurs.

---

Maintenant que vous savez ce que signifient le contrôle de version et Git, installons-le.

### POUR MAC OS :

[Télécharger Git pour macOS](http://git-scm.com/download/mac) ou installer en utilisant [Homebrew](https://brew.sh/)

```python
brew install git
```

### POUR LINUX OS :

[Télécharger Git pour Linux](https://git-scm.com/download/linux) ou  
Installer pour les systèmes Linux basés sur Debian

```python
sudo apt-get update
 sudo apt-get upgrade
 sudo apt-get install git
```

ou  
Installer pour les systèmes Linux basés sur Red Hat

```python
sudo yum upgrade
 sudo yum install git
```

### POUR WINDOWS OS :

[Télécharger Git pour Windows](https://git-scm.com/download/win)

#### VOICI UN GUIDE D'INSTALLATION PLUS DÉTAILLÉ POUR DIFFÉRENTS SYSTÈMES SUR [LA DOCUMENTATION OFFICIELLE DE GIT](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

---

Maintenant que vous avez Git sur votre système, configurons l'environnement Git.  
Git est livré avec un outil appelé `git config` qui vous permet d'obtenir et de définir des variables de configuration qui contrôlent tous les aspects de l'apparence et du fonctionnement de Git.

* Tout d'abord, définissez votre identité, votre nom et votre adresse e-mail comme suit :
    

```python
git config --global user.name "bolajiayodeji"
 git config --global user.email mailtobolaji@gmail.com
```

l'option `--global` garantit que ces valeurs sont utilisées dans tout votre système

* Ensuite, configurez l'éditeur de texte par défaut que vous utiliserez chaque fois que vous devrez entrer un message dans Git. Ce n'est pas obligatoire, si vous ne configurez pas cela, Git utilisera votre éditeur par défaut. Si vous souhaitez utiliser autre chose, configurez comme suit :
    

```python
git config --global core.editor emacs
```

* Ensuite, configurez les couleurs pour votre console Git.
    

Pour les utilisateurs de Linux OS, vous pouvez utiliser des configurateurs tiers Zsh comme [oh my zsh](https://ohmyz.sh/) pour personnaliser l'apparence de votre terminal avec des thèmes :).  
Pour configurer cela, faites ceci :

```python
git config --global color.ui true
```

Le color.ui est une méta-configuration qui inclut toutes les diverses configurations de couleur.\* disponibles avec les commandes git.

Git est maintenant prêt à l'emploi.

## VÉRIFIEZ VOS PARAMÈTRES

```python
git config --list
```

```python
user.name=bolajiayodeji
 user.email=mailtobolaji@gmail.com
 color.ui=true
```

---

Vous voulez apprendre quelques commandes Git super utiles ?

J'ai écrit un article : [Git Cheat Sheet](https://www.bolajiayodeji.com/git-cheat-sheet/) qui couvre certaines commandes Git importantes dont vous aurez besoin.

# CONCLUSION

Les logiciels de contrôle de version sont une partie essentielle du quotidien des pratiques des développeurs de logiciels modernes. Une fois habitués aux puissants avantages des systèmes de contrôle de version, de nombreux développeurs n'envisageraient pas de travailler sans eux, même pour des projets non logiciels.