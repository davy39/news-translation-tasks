---
title: Comment configurer un client Git en quelques minutes seulement
subtitle: ''
author: Zell Liew
co_authors: []
series: null
date: '2018-08-17T15:38:39.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-a-git-client-in-just-a-few-minutes-3d78b8d2264f
coverImage: https://cdn-media-1.freecodecamp.org/images/0*_-H01eZA61IjZIfc.png
tags:
- name: Git
  slug: git
- name: learning
  slug: learning
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment configurer un client Git en quelques minutes seulement
seo_desc: 'Today we’re going to talk about Git. You’re going to learn what Git is
  and how to set up a Git client on your computer.

  What is Git?

  Imagine you’re playing a game. In this game, you can create save points. When you
  die in the game, you need to load y...'
---

Aujourd'hui, nous allons parler de Git. Vous allez apprendre ce qu'est Git et comment configurer un client Git sur votre ordinateur.

### Qu'est-ce que Git ?

Imaginez que vous jouez à un jeu. Dans ce jeu, vous pouvez créer des points de sauvegarde. Lorsque vous mourrez dans le jeu, vous devez charger votre jeu et continuer à partir de votre point de sauvegarde.

Si vous n'avez pas créé de point de sauvegarde, vous devrez recommencer depuis le début du jeu. Ce n'est pas une expérience amusante, donc il est toujours bon de sauvegarder votre jeu.

Git est comme un système de points de sauvegarde pour votre travail. Vous pouvez créer des points de sauvegarde. Dans Git, nous appelons chaque point de sauvegarde un commit.

Lorsque vous créez un commit dans Git, vous pouvez charger votre travail à partir de ce commit. Si vous créez cinq commits, vous pouvez charger votre travail à partir de n'importe lequel de ces commits.

C'est à cela que sert Git. Nous l'appelons un système de contrôle de version, car vous pouvez sauvegarder et charger votre travail à partir de n'importe quel commit.

### Choisir un client Git

Beaucoup de gens vous apprennent à utiliser Git avec une ligne de commande, mais cela peut être effrayant pour les débutants.

Nous allons abandonner la ligne de commande et utiliser des applications pour vous aider à commencer avec Git. Ces applications sont également connues sous le nom de clients Git.

Mon client Git préféré est [Tower](https://git-tower.com/). Il est extrêmement puissant. Le seul inconvénient de Tower est qu'il coûte 55,20 $ par an. Si vous êtes nouveau en programmation, vous ne voudrez peut-être pas commencer avec Tower. Vous voudrez peut-être essayer une application gratuite à la place.

Voici quelques bonnes applications gratuites :

1. [Sourcetree](https://www.sourcetreeapp.com/)
2. [GitKraken](https://www.gitkraken.com/)
3. [Fork](https://git-fork.com/)

Sourcetree est probablement la meilleure application gratuite disponible. Elle est bonne et a des fonctionnalités comparables à celles de Tower. Mais Sourcetree peut être bogué, et vous ne pourrez peut-être pas résoudre les erreurs vous-même. (J'ai essayé, et je n'ai pas pu).

GitKraken est une autre application populaire que beaucoup de gens aiment. Je pense que GitKraken est trop sophistiqué et se concentre sur les mauvaises choses, cependant.

Fork semble propre et simple et est assez bon pour commencer. Il est en version bêta pour le moment, donc il est gratuit, mais vous devrez peut-être payer pour l'utiliser plus tard.

Je vais vous montrer comment configurer Fork.

### Installation de Fork

Voici l'écran de bienvenue lorsque vous ouvrez Fork pour la première fois :

![Image](https://cdn-media-1.freecodecamp.org/images/0*_-H01eZA61IjZIfc.png)

Il vous demandera votre nom d'utilisateur et votre adresse e-mail. Ceux-ci sont utilisés à des fins d'identification pour des utilisations avancées lorsque plusieurs personnes travaillent sur le même projet.

"Nom d'utilisateur" est un peu trompeur, car cela devrait être votre nom, et non un nom d'utilisateur réel.

#### Le répertoire source par défaut

Une chose que j'aime à propos de Fork, c'est qu'il vous demande de définir un répertoire source par défaut.

Cela signifie que les projets que vous copiez (ou clonez) avec Git iront automatiquement dans le dossier spécifié, ce qui facilite leur recherche.

#### Initialisation d'un dépôt Git

Il existe deux façons de créer un dépôt Git.

Avant de créer un dépôt Git, vous voudrez créer un dossier de projet dans votre répertoire source. Une fois que vous avez un dossier dans votre répertoire source, vous pouvez cliquer sur `Fichier` puis sur `Créer un nouveau dépôt` dans Fork pour créer votre répertoire Git.

Pour vérifier si le dépôt Git est créé, vous pouvez ouvrir le dossier du projet et rechercher un dossier `.git`. Ce dossier `.git` est un dossier caché. Vous devez [afficher vos fichiers cachés](https://ianlunn.co.uk/articles/quickly-showhide-hidden-files-mac-os-x-mavericks/) pour le voir.

La deuxième façon d'initialiser un dépôt Git est via la ligne de commande.

Pour ce faire, vous devrez d'abord créer votre dossier de projet dans votre répertoire source. Ensuite, vous faites glisser votre dossier de projet dans l'application Terminal. Cela vous naviguera automatiquement vers le dossier du projet dans le Terminal.

Si vous souhaitez en savoir plus sur le Terminal, je vous recommande de commencer par mon article sur [surmonter votre peur de la ligne de commande](https://zellwk.com/fear-of-command-line/).

Une fois que vous avez navigué vers le dossier du projet dans le terminal, vous pouvez taper `git init` pour initialiser le dépôt.

```
git init
```

### Conclusion

Git est comme un système de points de sauvegarde dans les jeux. Vous pouvez utiliser Git pour sauvegarder et charger votre travail.

Merci d'avoir lu. Cet article vous a-t-il aidé d'une manière ou d'une autre ? Si c'est le cas, [j'espère que vous envisagerez de le partager](http://twitter.com/share?text=Setting%20up%20a%20Git%20Client%20by%20@zellwk%20?%20&url=https://zellwk.com/blog/setting-up-git/&hashtags=). Vous pourriez aider quelqu'un qui se sentait comme vous avant de lire l'article. Merci.

Cet article a été initialement publié sur [mon blog](https://zellwk.com/blog/setting-up-git). Inscrivez-vous à ma [newsletter](https://zellwk.com/) si vous voulez plus d'articles pour vous aider à devenir un meilleur développeur front-end.