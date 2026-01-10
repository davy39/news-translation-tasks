---
title: Comment fonctionnent les fichiers de configuration Zsh ?
subtitle: ''
author: Daniel Kehoe
co_authors: []
series: null
date: '2024-01-09T20:37:28.000Z'
originalURL: https://freecodecamp.org/news/how-do-zsh-configuration-files-work
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/pexels-mike-468229-1181772.jpg
tags:
- name: macOS
  slug: macos
- name: shell
  slug: shell
- name: terminal
  slug: terminal
- name: zsh
  slug: zsh
seo_title: Comment fonctionnent les fichiers de configuration Zsh ?
seo_desc: "Beginners often get confused when configuring Zsh shell on a Mac.\nZsh\
  \ shell offers four configuration files with no discernible differences. Particularly,\
  \ ~/.zshrc and ~/.zprofile appear to be identical, leaving us wondering which one\
  \ to use. \nIn thi..."
---

Les débutants sont souvent confus lorsqu'ils configurent le shell Zsh sur un Mac.

Le shell Zsh offre quatre fichiers de configuration sans différences discernables. Particulièrement, `~/.zshrc` et `~/.zprofile` semblent identiques, nous laissant nous demander lequel utiliser. 

Dans cet article, vous apprendrez la différence et une directive simple pour votre configuration de shell.

## Pourquoi avez-vous besoin de configuration ?

Pour la programmation sur un Mac, l'application Terminal est un outil essentiel dans votre environnement de développement. Le Terminal est une interface en ligne de commande (CLI) qui vous permet d'interagir avec le système d'exploitation et d'exécuter des commandes. 

Le Terminal ou la console vous donne accès à la ligne de commande Unix, ou shell. 

[Zsh](https://en.wikipedia.org/wiki/Z_shell), également connu sous le nom de Z shell, est un programme qui s'exécute dans le Terminal, interprète les commandes Unix et interagit avec le système d'exploitation. Zsh est le programme de shell par défaut sur MacOS.

Avant de commencer la programmation sur le Mac, vous devrez configurer le shell. Il existe des paramètres optionnels et pratiques, tels que des alias pour les commandes difficiles à retenir et un prompt personnalisé qui peut afficher le répertoire dans lequel vous vous trouvez, entre autres. 

Il existe également certaines variables d'environnement critiques qui rendent les programmes disponibles ou altèrent le comportement du shell. La variable d'environnement `EDITOR`, par exemple, peut définir votre éditeur de texte préféré. Souvent, lors de l'installation d'un langage de programmation ou d'utilitaires logiciels, vous devez définir la variable d'environnement `PATH`.

## Par où commencer

Les fichiers de configuration Zsh sont conservés dans le répertoire personnel de l'utilisateur et sont nommés avec un point comme premier caractère pour les garder cachés par défaut. 

Zsh reconnaît quatre fichiers de configuration différents dans le répertoire personnel de l'utilisateur : `~/.zshenv`, `~/.zprofile`, `~/.zshrc` et `~/.zlogin`. 

C'est là que la configuration Zsh devient déroutante, même pour les développeurs expérimentés. Les tutoriels expliquent rarement les différences, surtout entre les fichiers `zprofile` et `zshrc`, laissant les développeurs curieux se gratter la tête et suivre aveuglément les instructions.

### Comment le shell est-il utilisé ?

Pour comprendre les différences entre les fichiers de configuration Zsh, considérons les diverses utilisations du shell, qui peuvent être classées comme interactives ou non interactives, login ou non-login.

1. Sur macOS, chaque nouvelle session de terminal est traitée comme un shell de login, donc l'ouverture de toute fenêtre de terminal démarre une session interactive de login. De plus, un administrateur système qui se connecte à un serveur distant via SSH initie une session interactive de login.
2. Si une fenêtre de terminal est déjà ouverte et que vous exécutez la commande `zsh` pour démarrer un sous-shell, il sera interactif et non-login. Les débutants utilisent rarement les sous-shells.
3. Les scripts shell automatisés s'exécutent sans login ni aucune invite utilisateur. Ceux-ci sont non interactifs et non-login.
4. Peu de gens rencontrent jamais une session de shell de login non interactive. Cela nécessite de démarrer un script avec un drapeau spécial ou de rediriger la sortie d'une commande dans une connexion SSH.

### Comment fonctionnent les fichiers de configuration ?

Ces cas d'utilisation nécessitent différentes configurations de shell, ce qui explique pourquoi Zsh supporte quatre fichiers de configuration différents. Voici comment les fichiers de configuration sont utilisés :

* `~/.zshenv` : Ce fichier est chargé universellement pour tous les types de sessions shell (interactives ou non interactives, login ou non-login). C'est le seul fichier de configuration qui est chargé pour les scripts non interactifs et non-login comme les tâches cron. Cependant, macOS remplace cela pour les paramètres `PATH` des shells interactifs.
* `~/.zprofile` : Chargé pour les shells de login (à la fois interactifs et les rares sessions non interactives). MacOS utilise ce fichier pour configurer le shell pour toute nouvelle fenêtre de terminal. Les sous-shells qui démarrent dans la fenêtre de terminal héritent des paramètres mais ne rechargent pas `~/.zprofile`.
* `~/.zshrc` : Chargé uniquement pour les sessions shell interactives. Il est chargé chaque fois que vous ouvrez une nouvelle fenêtre de terminal ou lancez un sous-shell à partir d'une fenêtre de terminal.
* `~/.zlogin` : Utilisé uniquement pour les configurations de shell de login, chargé après `.zprofile`. Ce fichier est chargé chaque fois que vous ouvrez une nouvelle fenêtre de terminal.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/zsh-diagram.png)

## Comment utiliser chaque fichier

Avec cela en tête, considérons quels fichiers de configuration vous devriez utiliser.

* `~/.zshenv` : Il est chargé universellement, donc vous pourriez l'utiliser pour configurer le shell pour les processus automatisés comme les tâches cron. Cependant, il est préférable de configurer explicitement les variables d'environnement pour les processus automatisés dans les scripts et de ne rien laisser au hasard. En tant que débutant, vous n'utiliserez pas ce fichier de configuration. En fait, peu de développeurs macOS expérimentés l'utilisent.
* `~/.zprofile` : Homebrew recommande de définir la variable `PATH` ici. Il y a une raison pour laquelle `PATH` doit être défini dans `~/.zprofile` et non dans le fichier universel `~/.zshenv` : macOS exécute un utilitaire `path_helper` (à partir de `/etc/zprofile`) qui définit l'ordre `PATH` avant que `~/.zprofile` ne soit chargé.
* `~/.zshrc` : C'est le fichier de configuration que la plupart des développeurs utilisent. Utilisez-le pour définir des alias et un prompt personnalisé pour la fenêtre de terminal. Vous pouvez également l'utiliser pour définir le `PATH` (ce que beaucoup de gens font) mais `~/.zprofile` est préféré.
* `~/.zlogin` : Celui-ci est rarement utilisé. Il est important uniquement pour gérer l'ordre des tâches d'initialisation pour les shells de login dans des environnements complexes. Il peut être utilisé pour afficher des messages ou des données système.

## Comment éviter les complications

Ces configurations peuvent sembler compliquées. Cela avait du sens dans les premiers jours de l'informatique de démarrer des processus chronophages au login et de ne pas les répéter lorsqu'un nouveau terminal était lancé.

MacOS lance maintenant toute nouvelle fenêtre de terminal comme un shell de login, chargeant à la fois les fichiers `~/.zprofile` et `~/.zshrc` sans se soucier du temps de démarrage du shell. Alors pourquoi ne pas utiliser un seul fichier de configuration Zsh ? Un hommage à l'histoire, plus une personnalisation de la configuration pour les experts.

L'avantage clé du fichier `~/.zprofile` (par rapport à `~/.zshenv`) est qu'il définit des variables d'environnement telles que `PATH` sans être remplacé par macOS. Le fichier `~/.zshrc` pourrait être utilisé pour la même chose mais, par convention et par conception, il est destiné à personnaliser l'apparence et le comportement du terminal interactif.

## Gardez cela simple

Si vous cherchez des directives simples, voici les meilleures pratiques actuelles.

* Utilisez `~/.zprofile` pour définir les variables d'environnement `PATH` et `EDITOR`.
* Utilisez `~/.zshrc` pour les alias et un prompt personnalisé, en ajustant l'apparence et le comportement du terminal.
* Si vous écrivez des scripts shell automatisés, vérifiez et définissez les variables d'environnement dans le script.

## Plus d'informations

J'ai écrit d'autres guides qui entrent dans les détails sur les sujets suivants :

* [Terminal Mac](https://mac.install.guide/terminal/index.html)
* [Configuration du Shell](https://mac.install.guide/terminal/configuration.html)
* [PATH Mac](https://mac.install.guide/terminal/path.html).

Si vous débutez, vous devrez savoir [Comment ouvrir le Terminal Mac](https://mac.install.guide/terminal/open.html) et [Installer les outils de ligne de commande Xcode](https://mac.install.guide/commandlinetools/index.html).

Configurer le shell Zsh est une étape critique dans la préparation de votre environnement de développement Mac. Avec votre environnement de développement configuré, vous serez prêt pour tout tutoriel que vous trouverez sur freeCodeCamp.