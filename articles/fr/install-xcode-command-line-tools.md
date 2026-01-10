---
title: Comment installer les outils en ligne de commande Xcode sur un Mac
subtitle: ''
author: Daniel Kehoe
co_authors: []
series: null
date: '2021-07-19T22:25:44.000Z'
originalURL: https://freecodecamp.org/news/install-xcode-command-line-tools
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/Terminal_Mac.png
tags:
- name: Apple
  slug: apple
- name: command line
  slug: command-line
- name: macOS
  slug: macos
- name: software development
  slug: software-development
- name: Xcode
  slug: xcode
seo_title: Comment installer les outils en ligne de commande Xcode sur un Mac
seo_desc: 'Developers need to install Xcode Command Line Tools before they can develop
  software on a Mac.

  Apple provides a complete development environment for programmers named Xcode. If
  you are developing software for macOS, iOS, tvOS, and watchOS, you must i...'
---

Les développeurs doivent installer les outils en ligne de commande Xcode avant de pouvoir développer des logiciels sur un Mac.

Apple fournit un environnement de développement complet pour les programmeurs nommé Xcode. Si vous développez des logiciels pour macOS, iOS, tvOS et watchOS, vous devez installer l'application Xcode complète.

Elle n'est pas préinstallée, mais vous pouvez l'installer depuis le [site web des développeurs Apple](https://developer.apple.com/download/) ou l'App Store sur votre Mac.

## Qu'est-ce que les outils en ligne de commande Xcode ?

Si vous ne développez pas de logiciels pour un appareil Apple, vous n'aurez pas besoin de l'application Xcode complète (elle nécessite plus de 40 Go d'espace disque !).

Au lieu de cela, vous installerez les outils en ligne de commande Xcode. Il s'agit d'un package plus petit pour les développeurs de logiciels avec des outils qui s'exécutent en ligne de commande, c'est-à-dire dans l'application Terminal.

Les programmeurs utilisent ces outils sur les systèmes d'exploitation Unix depuis les débuts de l'informatique, et ils servent de fondation à presque tous les développements logiciels.

Heureusement, le package des outils en ligne de commande Xcode ne nécessite que 1,2 Go d'espace sur votre disque.

Vous avez trois choix pour installer les outils en ligne de commande Xcode sur un Mac :

* installer le package complet Xcode
* installer les outils en ligne de commande Xcode lorsqu'ils sont déclenchés par une commande
* installer les outils en ligne de commande Xcode dans le cadre d'une installation Homebrew.

Je ne recommande pas d'installer le package complet Xcode sauf si vous développez des logiciels pour un appareil Apple. Le téléchargement prendra trop de temps et consommera un espace disque inutile. Essayez plutôt l'une des deux méthodes plus rapides.

## Comment installer les outils en ligne de commande Xcode à partir d'une invite de commande

Apple a facilité l'installation des outils en ligne de commande Xcode car certaines commandes vous inviteront à commencer l'installation.

Voici des exemples de commandes qui déclencheront une invite pour installer les outils en ligne de commande Xcode :

* `clang` – un compilateur qui transforme le code source en un programme exécutable
* `gcc` – le compilateur GNU
* `git` – le système de contrôle de version "sauvegardez au fur et à mesure"

L'exécution de l'une de ces commandes dans le terminal fera apparaître une invite pour installer les outils en ligne de commande Xcode. J'ai écrit ailleurs sur [Comment ouvrir le Terminal sur macOS](https://mac.install.guide/terminal/index.html) – cliquez simplement sur l'icône Spotlight dans la barre de menu et tapez "terminal".

Vous pouvez également entrer la commande `xcode-select --install` dans le terminal pour commencer le processus d'installation. Vous verrez un panneau qui vous demande d'installer les outils en ligne de commande Xcode.

![Image](https://mac.install.guide/assets/images/ruby/install-Xcode-CLT.png)

Cliquez sur 'Installer' pour commencer le téléchargement et le processus d'installation.

![Image](https://mac.install.guide/assets/images/ruby/install-Xcode-CLT-progress.png)

L'installation prend 8 minutes sur un Mac M1 Mini 2021, avec une connexion Internet de 100 Mbps. Elle est significativement plus lente sur les Mac Intel avec une connexion Internet lente.

![Image](https://mac.install.guide/assets/images/ruby/install-Xcode-CLT-done.png)

Vous verrez un message de confirmation lorsque l'installation sera terminée.

Vérifiez que vous avez installé avec succès les outils en ligne de commande Xcode :

```bash
$ xcode-select -p

```

Vous devriez voir ce qui suit :

```bash
/Library/Developer/CommandLineTools

```

## Comment utiliser Homebrew pour installer les outils en ligne de commande Xcode

Aussi facile que soit l'utilisation de l'invite de commande pour installer les outils en ligne de commande Xcode, je recommande une méthode encore plus facile : utiliser Homebrew.

Cette option a été ajoutée récemment à Homebrew, donc de nombreux développeurs ne sont pas au courant.

Homebrew est le gestionnaire de packages populaire pour Mac. La plupart des développeurs ont besoin de langages de programmation et d'utilitaires qui ne sont pas installés sur macOS et ne sont pas inclus dans le package des outils en ligne de commande Xcode. Homebrew peut installer presque tous les outils open source pour les développeurs.

Puisque vous aurez probablement besoin de Homebrew, vous pouvez aussi bien laisser Homebrew installer les outils en ligne de commande Xcode pour vous.

Tout d'abord, vérifiez si Homebrew est déjà installé.

```bash
$ brew

```

Si Homebrew n'est pas installé, vous verrez :

```bash
zsh: command not found: brew

```

Homebrew fournit un script d'installation que vous pouvez exécuter avec une seule commande (vérifiez qu'il n'a pas changé sur le [site Homebrew](https://brew.sh/)).

```bash
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

```

Le script d'installation de Homebrew vous demandera d'entrer votre mot de passe utilisateur Mac. Il s'agit du mot de passe que vous utilisez pour vous connecter à votre Mac.

```bash
Password:

```

Vous ne verrez pas les caractères lorsque vous tapez. Appuyez sur Entrée lorsque vous avez terminé.

![Image](https://mac.install.guide/assets/images/ruby/homebrew-enter-password.png)

Si vous n'avez pas déjà installé les outils en ligne de commande Xcode, vous verrez un message indiquant que "Les outils en ligne de commande Xcode seront installés." Appuyez sur Entrée pour continuer lorsque vous y êtes invité par le script d'installation de Homebrew.

![Image](https://mac.install.guide/assets/images/ruby/install-homebrew.png)

Vous verrez des messages de diagnostic et de progression. L'installation de Homebrew prend de 2 à 15 minutes sur un Mac M1 Mini 2021, avec une connexion Internet de 100 Mbps. Elle est significativement plus lente sur les Mac Intel avec une connexion Internet lente.

![Image](https://mac.install.guide/assets/images/ruby/homebrew-complete.png)

Sur les machines Mac Intel, c'est tout ce que vous avez à faire – Homebrew est prêt à être utilisé. Sur Mac Intel, Homebrew s'installe dans le répertoire `/usr/local/bin`, qui est déjà configuré pour être accessible par le shell avec le `$PATH` par défaut de macOS.

Sur les machines Apple Silicon, il y a une étape supplémentaire. Les fichiers Homebrew sont installés dans le dossier `/opt/homebrew`. Mais le dossier ne fait pas partie du `$PATH` par défaut. Suivez les conseils de Homebrew et créez un fichier `~/.zprofile` qui contient une commande pour configurer Homebrew. Homebrew affiche les instructions à la fin du processus d'installation :

```bash
- Ajoutez Homebrew à votre PATH dans ~/.zprofile :
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"

```

Après avoir installé Homebrew, vérifiez que Homebrew est installé correctement.

```bash
$ brew doctor

```

Vous devriez voir ceci :

```bash
Votre système est prêt à utiliser Homebrew.

```

Si Homebrew est installé avec succès, il y aura des fichiers Homebrew dans `/usr/local` (pour macOS Intel) ou `/opt/homebrew` (pour Apple Silicon).

Maintenant, vous avez à la fois les outils en ligne de commande Xcode et Homebrew installés. Si vous souhaitez en savoir plus sur l'ajout de packages Homebrew pour configurer votre environnement de développement, consultez [Installer un package Homebrew](https://mac.install.guide/homebrew/6.html).

## Plus d'informations

J'ai écrit un guide approfondi sur [Installer les outils en ligne de commande Xcode](https://mac.install.guide/commandlinetools/index.html) qui va au-delà de ces bases.

Dans le guide, j'explique comment vérifier si [les outils en ligne de commande Xcode sont déjà installés](https://mac.install.guide/commandlinetools/2.html). Je donne plus de détails sur comment [installer les outils en ligne de commande Xcode avec Homebrew](https://mac.install.guide/commandlinetools/3.html). Enfin, j'explique comment [désinstaller les outils en ligne de commande Xcode](https://mac.install.guide/commandlinetools/6.html), [réinstaller les outils en ligne de commande Xcode](https://mac.install.guide/commandlinetools/7.html), et je fournis une [liste des outils en ligne de commande Xcode](https://mac.install.guide/commandlinetools/8.html) que vous pouvez utiliser.

Il y a aussi un guide complet sur [Installer Homebrew pour Mac](https://mac.install.guide/homebrew/index.html) qui explique comment [mettre à jour Homebrew](https://mac.install.guide/homebrew/4.html), [désinstaller Homebrew](https://mac.install.guide/homebrew/5.html), et suivre d'autres [tâches de maintenance pour Homebrew](https://mac.install.guide/homebrew/8.html).

## Votre environnement de développement

MacOS est la plateforme la plus populaire pour le développement logiciel car le système d'exploitation est basé sur Unix, la norme de longue date pour le développement logiciel.

Avec les outils en ligne de commande Xcode installés, vous aurez une base solide pour ajouter presque tous les outils de développement open source.

Ajoutez Homebrew et vous aurez un gestionnaire de packages qui peut installer des gestionnaires de versions, des langages de programmation et presque tous les autres outils dont vous pourriez avoir besoin.

Combiné avec un éditeur de texte et une application terminal, vous serez prêt pour tout tutoriel que vous trouverez sur freeCodeCamp.