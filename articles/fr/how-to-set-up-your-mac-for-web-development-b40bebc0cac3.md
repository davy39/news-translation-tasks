---
title: Comment configurer un Mac pour le développement web
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-20T15:15:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-your-mac-for-web-development-b40bebc0cac3
coverImage: https://cdn-media-1.freecodecamp.org/images/0*dzQLqKvHf4nNk1gp.jpg
tags:
- name: beginner
  slug: beginner
- name: Git
  slug: git
- name: Homebrew
  slug: homebrew
- name: JavaScript
  slug: javascript
- name: mac
  slug: mac
- name: node
  slug: node
- name: Node.js
  slug: nodejs
- name: Web Development
  slug: web-development
seo_title: Comment configurer un Mac pour le développement web
seo_desc: 'By Michael Uloth

  While you can build basic websites with nothing more than a text editor and browser,
  you may want to up your game by adding a JavaScript framework like React or Vue
  and useful tools like Git to your workflow.

  But wait! Your Mac isn’t...'
---

Par Michael Uloth

Bien que vous puissiez créer des sites web basiques avec rien de plus qu'un éditeur de texte et un navigateur, vous pourriez vouloir améliorer votre jeu en ajoutant un framework JavaScript comme [React](https://reactjs.org/) ou [Vue](https://vuejs.org/) et des outils utiles comme [Git](https://git-scm.com/) à votre flux de travail.

Mais attendez ! Votre Mac n'est pas prêt. Avant de plonger, vous devrez installer quelques éléments qui vous éviteront des erreurs déroutantes plus tard. ?

Cet article vous guidera à travers la configuration minimale dont vous aurez besoin pour démarrer avec le développement web basé sur JavaScript sur votre Mac.

C'est parti !

#### Mettre à jour votre Mac

Avant d'installer un nouveau logiciel, suivez [ces instructions](https://support.apple.com/en-ca/HT201541) d'Apple pour mettre à niveau macOS et vos logiciels actuels vers la dernière version.

#### Choisir une application de terminal

Puisque vous allez interagir avec votre Mac en utilisant la ligne de commande dans cet article, vous aurez besoin d'une application de terminal.

Voici quelques bonnes options :

* [Hyper](https://hyper.is/)
* [iTerm2](https://www.iterm2.com/)
* Le terminal intégré de [Visual Studio Code](https://code.visualstudio.com/docs/editor/integrated-terminal)
* [Terminal](https://support.apple.com/en-ca/guide/terminal/welcome/mac) (l'application par défaut qui vient avec votre Mac)

Si vous n'êtes pas sûr de laquelle choisir, optez pour Hyper.

#### Outils de développement en ligne de commande

La première chose que vous devrez installer depuis la ligne de commande sont les **outils de développement en ligne de commande** de votre Mac. Les installer maintenant évitera des [erreurs étranges](https://stackoverflow.com/questions/32893412/command-line-tools-not-working-os-x-el-capitan-macos-sierra-macos-high-sierra) plus tard.

Pour vérifier si les outils sont déjà installés, tapez la commande suivante dans votre application de terminal et appuyez sur retour :

```
xcode-select --version
```

Si le résultat n'est pas un numéro de version, installez les outils avec cette commande :

```
xcode-select --install
```

Une boîte de dialogue apparaîtra vous demandant si vous souhaitez installer les outils. Cliquez sur **Installer** et le package se téléchargera et s'installera.

Lorsque l'installation est terminée, confirmez que les outils sont maintenant installés en relançant la première commande :

```
xcode-select --version
```

Le résultat devrait maintenant être un numéro de version.

#### Homebrew

Au lieu d'installer les quelques outils suivants en allant sur le site web de chaque outil, en trouvant la page de téléchargement, en cliquant sur le lien de téléchargement, en décompressant les fichiers et en exécutant manuellement l'installateur, nous allons utiliser [Homebrew](https://brew.sh/).

**Homebrew** est un outil qui vous permet d'installer, de mettre à jour et de désinstaller des logiciels sur votre Mac depuis la ligne de commande. Cela est plus rapide et [plus sûr](https://blog.teamtreehouse.com/install-node-js-npm-mac) que l'approche manuelle et rend généralement votre vie de développeur plus facile.

Tout d'abord, vérifiez si Homebrew est déjà installé :

```
brew --version
```

Si vous ne voyez pas de numéro de version, installez Homebrew avec cette commande :

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

Je vous promets que c'est la commande la plus étrange que vous verrez dans cet article ! ? Grâce à Homebrew, les autres sont simples.

Avant de continuer, confirmez que Homebrew est maintenant installé :

```
brew --version
```

#### Node et npm

[Node.js](https://nodejs.org/) est un outil qui permet à votre Mac d'exécuter du code JavaScript en dehors d'un navigateur web. Si vous souhaitez exécuter un framework JavaScript comme React ou Vue sur votre Mac, vous devrez avoir Node installé.

Node inclut également [npm](https://www.npmjs.com/) (le Node Package Manager), qui vous donne accès à une gigantesque bibliothèque de code gratuit que vous pouvez télécharger et utiliser dans vos projets.

Tout d'abord, vérifiez si Node est déjà installé :

```
node --version
```

Si ce n'est pas le cas, installez-le avec Homebrew :

```
brew install node
```

Enfin, confirmez que Node et npm sont maintenant installés :

```
node --version
```

```
npm --version
```

#### Contrôle de version avec Git

[Git](https://git-scm.com/) est un outil qui vous aide à suivre les changements de votre code et à travailler avec d'autres développeurs sur des projets partagés.

Utiliser Git sur chaque projet est une excellente habitude à développer et vous préparera pour des projets futurs où Git pourrait être requis. Certains outils (comme [GatsbyJS](https://www.gatsbyjs.org/)) dépendent également de Git installé sur votre Mac, donc vous en aurez besoin même si vous ne prévoyez pas de l'ajouter à votre flux de travail.

Une fois de plus, commencez par vérifier si Git est déjà installé :

```
git --version
```

Si ce n'est pas le cas, installez-le :

```
brew install git
```

Et confirmez que l'installation a fonctionné :

```
git --version
```

De temps en temps, exécutez la commande suivante et tout ce que vous avez installé avec Homebrew sera mis à jour automatiquement :

```
brew update && brew upgrade && brew cleanup && brew doctor
```

Cette seule commande est tout ce dont vous avez besoin pour garder votre système à jour. ?

Je l'exécute généralement lorsque je commence un nouveau projet, mais n'hésitez pas à le faire quand vous le souhaitez. (Lorsque vous exécutez cette commande, si Homebrew suggère des commandes supplémentaires à exécuter, allez-y et exécutez-les. Si une commande commence par `sudo` et qu'un mot de passe vous est demandé, utilisez le mot de passe administrateur de votre Mac.)

C'est tout pour la ligne de commande !

#### Éditeur de code

Bien que vous puissiez écrire du code dans n'importe quel éditeur de texte, utiliser un éditeur qui met en évidence et valide votre code rendra votre vie beaucoup plus facile.

Voici quelques bonnes options :

* [Visual Studio Code](https://code.visualstudio.com/)
* [Atom](https://atom.io/)
* [Sublime Text](https://www.sublimetext.com/)

Si vous débutez, choisissez Visual Studio Code.

#### Navigateur

Alors que vous codez, il est utile de visualiser l'application ou le site web que vous construisez dans un navigateur pour confirmer qu'il fonctionne. Bien que vous puissiez utiliser n'importe quel navigateur pour cela, certains incluent des outils de développement supplémentaires qui vous montrent des détails sur votre code et comment l'améliorer.

Voici deux bonnes options :

* [Chrome](https://www.google.com/chrome/)
* [Firefox](https://www.mozilla.org/firefox/)

Si vous débutez, choisissez Chrome.

#### Finder

Un petit conseil ici : vous voudrez afficher les fichiers que votre Mac cache par défaut. (Par exemple, les fichiers git sont automatiquement cachés, mais parfois vous voudrez les éditer.)

Le moyen le plus simple d'afficher les fichiers cachés de votre Mac est avec le raccourci clavier **⌘⇧.** (Commande + Maj + Point). Cela alternera entre l'affichage et le masquage de ces fichiers afin que vous puissiez y accéder lorsque vous en avez besoin.

#### Conclusion

Vous êtes prêt ! ?

C'est tout ce dont vous avez besoin pour démarrer avec le développement front-end basé sur JavaScript sur votre Mac.

Pour éviter la confusion, j'ai omis les éléments qui ne sont pas strictement nécessaires. Si vous souhaitez approfondir les façons optionnelles de personnaliser davantage votre Mac pour le développement web, consultez les liens ci-dessous.

### Lectures complémentaires

* [Configurer un tout nouveau Mac pour le développement](https://www.taniarascia.com/setting-up-a-brand-new-mac-for-development/) par Tania Rascia
* [Configurer un MacBook pour le développement front-end](https://www.bhnywl.com/blog/setting-up-a-macbook-for-front-end-development/) par Ben Honeywill
* [Quitter Homestead : Trouver le meilleur environnement de développement local polyvalent](https://webdevstudios.com/2018/09/27/finding-the-best-all-around-local-development-environment/) par WebDevStudios (au cas où vous auriez besoin d'une configuration PHP également)

[Discuter sur Twitter](https://twitter.com/search?q=upandrunningtutorials.com/how-to-set-up-a-mac-for-web-development)

---

*Originalement publié sur [michaeluloth.com](https://www.michaeluloth.com/how-to-set-up-a-mac-for-web-development/).