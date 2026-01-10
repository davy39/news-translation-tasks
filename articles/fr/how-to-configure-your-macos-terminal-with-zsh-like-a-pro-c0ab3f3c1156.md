---
title: Comment configurer votre terminal macOS avec Zsh comme un pro
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-15T18:05:25.000Z'
originalURL: https://freecodecamp.org/news/how-to-configure-your-macos-terminal-with-zsh-like-a-pro-c0ab3f3c1156
coverImage: https://cdn-media-1.freecodecamp.org/images/1*REqZX2_JqQjbH9Ly3QsgLg.png
tags:
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: terminal
  slug: terminal
- name: zsh
  slug: zsh
seo_title: Comment configurer votre terminal macOS avec Zsh comme un pro
seo_desc: 'By Chiamaka Ikeanyi

  Sometimes, using the default terminal sucks. You want to go out of the ordinary,
  to add life to the boring terminal and improve your productivity.

  Z shell (Zsh) is a Unix shell built on top of bash (the default shell for macOS)
  wi...'
---

Par Chiamaka Ikeanyi

Parfois, utiliser le terminal par défaut est ennuyeux. Vous voulez sortir de l'ordinaire, ajouter de la vie au terminal ennuyeux et améliorer votre productivité.

[Z shell](https://en.wikipedia.org/wiki/Z_shell) (Zsh) est un shell Unix construit sur bash (le shell par défaut pour macOS) avec un grand nombre d'améliorations.

Dans ce guide, nous allons configurer iTerm2 avec ZSH et ses dépendances. C'est un jeu d'enfant, et après cela, vous vous demanderez pourquoi vous n'avez pas découvert ZSH plus tôt. Eh bien, puisque vous êtes déjà ici, commençons.

### Points clés

* Installation de Homebrew
* Installation de iTerm2
* Installations de ZSH et Oh My ZSH
* Configuration des dépendances pour créer un terminal magnifique

### Étape 1 : Installer Homebrew

[Homebrew](https://brew.sh/) est un système de gestion de paquets logiciels gratuit et open-source qui simplifie l'installation de logiciels sur le macOS d'Apple.

Avant d'installer Homebrew, nous devons installer les outils CLI pour Xcode. Ouvrez votre terminal et exécutez la commande :

```bash
xcode-select --install
```

Si vous obtenez une erreur, exécutez `xcode-select -r` pour réinitialiser `xcode-select`.

Ensuite, installez Homebrew.

```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

### Étape 2 : Installer iTerm2

iTerm2 est un remplacement pour le terminal et le successeur de iTerm. La plupart des ingénieurs logiciels préfèrent i[Term2](https://www.iterm2.com/) au terminal par défaut qui est fourni avec macOS en raison de [ses fonctionnalités cool](https://www.iterm2.com/features.html). Vous pouvez intégrer zsh dans iTerm2 pour augmenter la productivité.

Pour installer iTerm2, exécutez la commande :

```bash
brew cask install iterm2
```

### Étape 3 : Installer ZSH

> _Zsh est un shell conçu pour une utilisation interactive, bien qu'il soit également un langage de script puissant._

Par défaut, macOs est livré avec zsh situé dans `/bin/zsh`.

Installons zsh en utilisant brew et faisons en sorte que iTerm2 l'utilise.

```bash
brew install zsh
```

### Étape 4 : Installer Oh My Zsh

> « Oh My Zsh est un framework open source, piloté par la communauté, pour gérer votre configuration [zsh](https://www.zsh.org/). Il ne fera pas de vous un développeur 10x... mais vous pourriez vous sentir comme tel. »

> — Robby Russell

Il fonctionne sur Zsh pour fournir des fonctionnalités cool configurables dans le fichier de configuration ~/.zhrc. Installez [Oh My Zsh](https://github.com/robbyrussell/oh-my-zsh) en exécutant la commande

```
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```

Vérifiez la version installée

```bash
zsh --version
```

Vous pouvez la mettre à niveau pour obtenir les dernières fonctionnalités qu'elle offre.

```bash
upgrade_oh_my_zsh
```

Redémarrez iTerm2 pour plonger dans la nouvelle expérience d'utilisation de Zsh. Bienvenue dans le monde « Oh My Zsh » ?.

Ce n'est pas tout. Maintenant, nous allons installer les dépendances pour tirer le meilleur parti de Zsh.

### Étape 5 : Changer le thème par défaut

Oh My Zsh est livré avec de nombreux thèmes. Le thème par défaut est robbyrussell, mais vous pouvez le changer pour n'importe quel thème de votre choix. Dans ce scénario, je l'ai changé en agnoster, un thème déjà préinstallé.

Vous devez ensuite sélectionner ce thème dans votre `~/.zshrc`. Pour ouvrir le fichier de configuration (.zshrc), exécutez la commande :

```bash
nano ~/.zshrc
```

![Image](https://cdn-media-1.freecodecamp.org/images/czy8LqFZcWJnyNWPq8MLpU-u6r74ozW-ndAz)
_Thème Zsh défini sur agnoster_

Ou ouvrez le fichier dans un éditeur de texte avec

```bash
open ~/.zshrc
```

![Image](https://cdn-media-1.freecodecamp.org/images/umcC5b7qtng38UbZngNRwMXq6NzwmR8SqIes)

Définissez le thème zsh et mettez à jour vos changements

```bash
source ~/.zshrc
```

### Utilisation d'un thème personnalisé

Pour installer un autre thème non préinstallé, clonez le dépôt dans le répertoire `custom/themes`. Dans ce scénario, nous allons installer [powerlevel9k](https://github.com/bhilburn/powerlevel9k/wiki/Install-Instructions#option-2-install-for-oh-my-zsh),

```bash
$ git clone https://github.com/bhilburn/powerlevel9k.git ~/.oh-my-zsh/custom/themes/powerlevel9k
```

Ensuite, sélectionnez ce thème dans votre `~/.zshrc`

```bash
ZSH_THEME="powerlevel9k/powerlevel9k"
```

Mettez à jour vos changements en exécutant la commande `source ~/.zshrc`

Accédez à `iTerm2 > Préférences > Profils > Couleurs` si vous souhaitez changer la couleur de fond du terminal.

Le thème sélectionné dans ce scénario nécessite des polices powerline. Alors, installons cela.

### Étape 6 : Installer les polices

Je vais utiliser [Inconsolata](https://github.com/powerline/fonts/tree/master/Inconsolata). Obtenez votre police préférée parmi ces [polices powerline](https://github.com/powerline/fonts). Ensuite, téléchargez-la et installez-la.

![Image](https://cdn-media-1.freecodecamp.org/images/l-nkEZ87vggoFrm5xPNGvyNMv9hyxZc2tE1U)

Ou téléchargez l'ensemble de la police.

```bash
git clone https://github.com/powerline/fonts.git

cd fonts

./install.sh
```

Pour changer la police, accédez à `iTerm2 > Préférences > Profils > Texte > Changer la police`.

Maintenant, vous pouvez voir Inconsolata listée comme l'une des polices. Sélectionnez votre police préférée. Pour les polices qui supportent les ligatures comme [FiraCode](https://github.com/tonsky/FiraCode), cochez l'option « Utiliser les ligatures » pour voir vos flèches et autres opérateurs de manière stylisée comme ( **→** ).

![Image](https://cdn-media-1.freecodecamp.org/images/flJ1CL1uDv0QoX-TK0MBgn7CVuyG0wOG388V)
_Sélectionnez une police powerline_

### Étape 7 : Installer un schéma de couleurs

Changeons le schéma de couleurs pour faire ressortir la beauté de notre terminal. Accédez à [iTerm2-Color-Schemes](https://github.com/mbadolato/iTerm2-Color-Schemes) et téléchargez le dossier ZIP. Ensuite, extrayez le dossier téléchargé car ce dont nous avons besoin se trouve dans le dossier schemes.

Accédez à `iTerm2 > Préférences > Profil > Couleurs > Préréglages de couleurs > Importer`

* Accédez au dossier schemes et sélectionnez vos schémas de couleurs préférés pour les importer.
* Cliquez sur un schéma de couleurs spécifique pour l'activer. Dans ce scénario, j'ai activé Batman qui est mon schéma de couleurs préféré.

![Image](https://cdn-media-1.freecodecamp.org/images/0NGtEWFgLWeyM4tzGVtQ4xTNNqBdnHMdZMGw)

Tada ! ? Nous avons terminé avec les paramètres de base.

![Image](https://cdn-media-1.freecodecamp.org/images/tFnT1hiSKgWYMYYTNIzUfjD1Z5vIe2QnjSlI)
_Schéma de couleurs Batman_

### Étape 8 : Installer des plugins

Oh My ZSH est préchargé avec un plugin git. Pour en ajouter plus, par exemple, docker, auto-suggestion, surlignage de syntaxe et plus :

* Clonez le dépôt Git

```bash
git clone https://github.com/zsh-users/zsh-docker.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-docker
```

* Rendez-vous dans le répertoire `.oh-my-zsh > custom > plugins` pour voir le répertoire cloné. Pour y accéder, exécutez la commande `open ~/.oh-my-zsh`
* Ajoutez le plugin à la section des plugins du fichier de configuration `~/.zshrc` comme montré ci-dessous
* Mettez à jour vos changements en exécutant la commande `source ~/.zshrc`

![Image](https://cdn-media-1.freecodecamp.org/images/oK1lzMvgGrsycWUoueagV0a99eq00akzwiEW)

### Étape 9 : Ajouter des alias

Les alias sont des raccourcis utilisés pour réduire le temps passé à taper des commandes. Ajoutez des alias aux commandes que vous exécutez dans la section montrée ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/VmmW4SCRGXW2cQ74o4nODyLOlNgZYeJEgOyR)
_Taper `**dckimgs**` exécute la commande docker images_

**_Merci d'avoir lu_**.

Si vous connaissez d'autres moyens d'améliorer la productivité en utilisant ZSH, vous pouvez les laisser dans la section des commentaires, je serai ravi d'avoir de vos nouvelles.