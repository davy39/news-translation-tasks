---
title: Comment installer Python sur un Mac
subtitle: ''
author: Daniel Kehoe
co_authors: []
series: null
date: '2024-05-09T06:33:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-install-python-on-a-mac
coverImage: https://www.freecodecamp.org/news/content/images/2024/05/python-shop.png
tags:
- name: Python
  slug: python
- name: Python 3
  slug: python3
seo_title: Comment installer Python sur un Mac
seo_desc: "Python is the most popular first language for programmers on a Mac.\nUntil\
  \ recently, the language's lack of standard development tooling, plus competing\
  \ optional-but-essential development tools, meant a rocky start for Python beginners.\
  \ \nTo cut throug..."
---

Python est le langage de programmation le plus populaire pour les débutants sur Mac.

Jusqu'à récemment, le manque d'outils de développement standard pour ce langage, ainsi que des outils de développement optionnels mais essentiels en compétition, signifiaient un début difficile pour les débutants en Python.

Pour clarifier la situation, je vais vous montrer une approche à jour pour installer Python et configurer un projet de programmation, en utilisant un seul outil nommé Rye, pour installer des versions de Python et des bibliothèques logicielles.

[Rye](https://rye-up.com/) est un outil de gestion de projet tout-en-un pour Python, écrit en Rust (pour la vitesse) et inspiré par Cargo, le gestionnaire de paquets complet de Rust, créé par Armin Ronacher, le créateur du framework web Python Flask. Il est idéal pour les débutants, empruntant une approche basée sur les dossiers pour le développement, comme d'autres langages tels que JavaScript et Ruby.

## Sommaire

Vous voudrez enregistrer l'URL de ce guide pour référence future. Voici ce qui est couvert ici :

* [Avant de commencer](#heading-avant-de-commencer)
* [Installation de Python avec Rye](#heading-installation-de-python-avec-rye)
  - [Vérifier la présence de Python](#heading-verifier-la-presence-de-python)
  - [Installer Rye](#heading-installer-rye)
  - [Configurer le PATH pour Rye](#heading-configurer-le-path-pour-rye)
  - [Vérifier l'installation de Rye](#heading-verifier-linstallation-de-rye)
  - [Vérifier l'installation de Python](#heading-verifier-linstallation-de-python)
* [Gestion des versions et des paquets avec Rye](#heading-gestion-des-versions-et-des-paquets-avec-rye)
  - [Créer un projet avec Rye](#heading-creer-un-projet-avec-rye)
  - [Définir une version](#heading-definir-une-version)
  - [Ajouter des paquets](#heading-ajouter-des-paquets)
  - [Synchroniser pour configurer le projet](#heading-synchroniser-pour-configurer-le-projet)
  - [Exécuter Python](#heading-executer-python)
* [Workflow Python avec Rye](#heading-workflow-python-avec-rye)
* [Conclusion](#heading-conclusion)

## Avant de commencer

Vous aurez besoin d'une application de terminal, soit [Terminal Mac](https://mac.install.guide/terminal/) ou une alternative telle que [Warp Terminal](https://mac.install.guide/more/download-warp) (un outil que j'appelle "le moyen le plus rapide de devenir un utilisateur avancé de la ligne de commande").

Avant de commencer, vérifiez si vous devez [mettre à jour macOS](https://mac.install.guide/commandlinetools/1).

Vous avez peut-être entendu dire que Python est préinstallé sur votre Mac. Les anciens Mac (avant macOS 12.3) étaient livrés avec Python 2.7. Il s'agit d'une ancienne version, pas du Python 3 dont vous avez besoin. Les nouveaux Mac ne sont pas livrés avec une version préinstallée de Python.

Vous devrez installer [Xcode Command Line Tools](https://mac.install.guide/commandlinetools/) avant de commencer à programmer sur un Mac. Vous devriez vérifier si [Xcode Command Line Tools est installé](https://mac.install.guide/commandlinetools/2) avant de continuer. Lorsque vous installez Xcode Command Line Tools, Apple inclut Python 3.9.6. Vous pourriez être tenté de l'utiliser, mais il s'agit d'une ancienne version, destinée uniquement aux logiciels système, c'est pourquoi vous devriez installer une nouvelle version de Python, comme montré ici.

## Installation de Python avec Rye

Il existe plusieurs façons de configurer [Python sur Mac](https://mac.install.guide/python/). Voici vos options, en bref, avec une critique.

Sur le [site web de Python.org](https://www.python.org/downloads/), il y a une application d'installation pour la version la plus récente de Python. La plupart des développeurs Python évitent de l'utiliser car elle encombre un Mac de manières difficiles à gérer.

Si vous [installez Homebrew](https://mac.install.guide/homebrew/3) pour le développement de logiciels, il est facile de faire ["brew install python."](https://mac.install.guide/python/brew) Cependant, le Python installé par Homebrew n'est pas bien adapté à la gestion de plusieurs projets Python et le développement peut être fastidieux.

Certains tutoriels suggèrent d'[installer Pyenv](https://mac.install.guide/python/install-pyenv), un gestionnaire de versions Python. Pyenv est un bon choix pour gérer plusieurs versions de Python, mais il nécessite une familiarité avec [Pip](https://pip.pypa.io/en/stable/), un gestionnaire de paquets, et [Venv](https://docs.python.org/3/library/venv) ou [Virtualenv](https://virtualenv.pypa.io/en/latest/), des gestionnaires d'environnements. Plusieurs outils rendent le développement plus complexe.

Je recommande d'installer Python avec [Rye](https://rye-up.com/). Avec cet outil tout-en-un, vous gérerez plusieurs versions de Python, configurerez des environnements basés sur des projets et installerez des bibliothèques Python sans conflits de dépendances. Je vais vous montrer comment installer Python en utilisant Rye, la manière facile, avec un script d'auto-installation.

### Vérifier la présence de Python

Il est préférable de commencer sans aucune version précédente de Python installée, à l'exception de la version de Python installée par Xcode Command Line Tools.

Essayez `python3 --version` et `which -a python3` pour vérifier si Python a été installé avec Xcode Command Line Tools :

```bash
$ python3 --version
Python 3.9.6
$ which -a python3
/usr/bin/python3
```

Vous n'utiliserez pas le Python installé par Xcode Command Line Tools, mais il est important de savoir que Xcode Command Line Tools est déjà présent. Sinon, [installez Xcode Command Line Tools](https://mac.install.guide/commandlinetools/4).

Vérifiez si une autre version de Python est déjà installée :

```bash
$ python --version
zsh: command not found: python
```

Vous verrez `zsh: command not found: python` si Python n'est pas disponible. J'ai écrit ailleurs sur la façon de [mettre à jour Python](https://mac.install.guide/python/update) si vous pensez que vous avez déjà Python, ainsi qu'un guide pour résoudre l'erreur "[command not found: python](https://mac.install.guide/python/command-not-found-python)" si vous êtes sûr que Python est installé mais non disponible.

Si vous avez plus d'une version de Python installée, ce n'est pas un problème car vous définirez le [PATH Mac](https://mac.install.guide/terminal/path) après avoir installé Rye pour rendre la version correcte de Python disponible.

### Installer Rye

Homebrew n'est pas nécessaire. Rye dispose d'un script d'auto-installation, vous pouvez donc installer Rye avec une commande `curl`.

```bash
$ curl -sSf https://rye.astral.sh/get | bash
```

[Curl](https://curl.se/) est un outil en ligne de commande qui effectue des requêtes HTTP à partir du terminal, utile pour des tâches comme le téléchargement et l'exécution de scripts d'installation.

```bash
$ curl -sSf https://rye.astral.sh/get | bash
This script will automatically download and install rye (latest) for you.
####################################################################### 100.0%
Welcome to Rye!

This installer will install rye to /Users/username/.rye
This path can be changed by exporting the RYE_HOME environment variable.

Details:
  Rye Version: 0.26.0
  Platform: macos (aarch64)

? Continue? (y/n)
```

Entrez `y` pour continuer. Rye posera des questions pour personnaliser l'installation.

```bash
? Select the preferred package installer •
✷ uv (fast, recommended)
  pip-tools (slow, higher compatibility)
```

Par défaut, Rye propose `uv`, un installateur de paquets plus rapide et plus récent. Je recommande de choisir `pip-tools` pour la compatibilité. Si vous êtes débutant, il sera plus facile de suivre des tutoriels qui font référence à `pip`. Sélectionnez `pip-tools` avec les touches fléchées.

Ensuite, le script d'auto-installation demande quelle version de Python vous utiliserez par défaut, en proposant la version installée par Rye ou les versions précédemment installées.

```bash
? What should running `python` or `python3` do when you are not inside a Rye managed project? •
✷ Run a Python installed and managed by Rye
  Run the old default Python (provided by your OS, pyenv, etc.)
```

Il est préférable d'utiliser la version installée par Rye. Acceptez le choix par défaut `Run a Python installed and managed by Rye` en appuyant sur "Entrée". Ensuite, le script d'auto-installation demande quelle version de Python installer par défaut.

```bash
? Which version of Python should be used as default toolchain? (cpython@3.12) •
```

Acceptez le choix par défaut et Rye installera la dernière version de Python. L'installation commence lorsque vous appuyez sur "Entrée".

```bash
Installed binary to /Users/username/.rye/shims/rye
Bootstrapping rye internals
Downloading cpython@3.12.1
Checking checksum
Unpacking
Downloaded cpython@3.12.1
Updated self-python installation at /Users/username/.rye/self

The rye directory /Users/username/.rye/shims was not detected on PATH.
It is highly recommended that you add it.
? Should the installer add Rye to PATH via .profile? (y/n) •
```

Remarquez que Rye installe ses fichiers Python dans `~/.rye/shims/rye`.

Rye propose de définir le `$PATH` pour donner la priorité à sa version de Python en modifiant le fichier `.profile`.

L'utilisation du fichier `.profile` est une convention Linux. Sur Mac, il est préférable de définir le `$PATH` dans les fichiers `.zprofile` ou `.zshrc`, de préférence `.zprofile`. Entrez `n` pour ignorer cette étape automatique. Plus tard, vous définirez le `$PATH` manuellement.

```bash
✓ Should the installer add Rye to PATH via .profile? · no
note: did not manipulate the path. To make it work, add this to your .profile manually:

    source "$HOME/.rye/env"

To make it work with zsh, you might need to add this to your .zprofile:

    source "$HOME/.rye/env"

For more information read https://rye.astral.sh/guide/installation/

All done!
```

Rye explique comment compléter l'installation manuellement en modifiant le fichier `.zprofile`. Je vais vous montrer comment faire.

### Configurer le PATH pour Rye

Il y a une dernière étape **importante** avant que Rye ne fonctionne correctement. Vous devez configurer le PATH Mac pour vous assurer que Rye trouve la version correcte de Python. Sinon, en entrant la commande `python`, vous obtiendrez `zsh: command not found: python` et la commande `python3` accédera à l'ancienne version de Python installée par Xcode.

Modifiez le fichier `~/.zprofile`. Le fichier `~/.zprofile` est utilisé pour configurer le `$PATH`. Alternativement, vous pouvez modifier le fichier `~/.zshrc` (voir [Comment fonctionnent les fichiers de configuration Zsh ?](https://www.freecodecamp.org/news/how-do-zsh-configuration-files-work/) pour une explication des différences). Vous pouvez utiliser TextEdit, l'éditeur de texte graphique par défaut de macOS, en ouvrant un fichier à partir du terminal :

```bash
$ open -e ~/.zprofile
```

Vous pouvez également utiliser les éditeurs de ligne de commande `nano` ou `vim` pour modifier les fichiers de configuration du shell. Voir [Configuration du shell Zsh](https://mac.install.guide/terminal/configuration) pour plus d'informations sur la modification des fichiers de configuration du shell.

Ajoutez cette commande comme dernière ligne de votre fichier de configuration pour configurer le Z shell pour Rye :

```bash
source "$HOME/.rye/env"
```

Lorsque votre session de terminal commence, le Z shell exécutera le script `~/.rye/env` pour définir des [shims](https://rye-up.com/guide/shims/) afin d'intercepter et de rediriger les commandes Python. Vous aurez besoin de guillemets doubles car la commande contient des caractères spéciaux.

Rye ajoute les shims à votre `$PATH` afin que l'exécution de la commande `python` ou `python3` lance une version de Python installée par Rye.

Les modifications apportées au fichier `~/.zprofile` ne prendront pas effet dans le Terminal tant que vous n'aurez pas quitté et redémarré le terminal. Alternativement (c'est plus facile), vous pouvez utiliser la commande `source` pour réinitialiser l'environnement du shell :

```bash
$ source ~/.zprofile
```

La commande `source` lit et exécute un fichier de script shell, dans ce cas, réinitialisant l'environnement du shell avec votre nouveau paramètre `$PATH`.

Après avoir réinitialisé votre shell, vous pouvez vérifier le paramètre `$PATH`.

```bash
$ echo $PATH
/Users/username/.rye/shims:/opt/homebrew/bin:/opt/homebrew/sbin:/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/System/Cryptexes/App/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/local/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/appleinternal/bin
```

Le répertoire `~/.rye/shims` doit être le plus à gauche, prenant la priorité sur les autres répertoires.

### Vérifier l'installation de Rye

Après avoir installé Rye, utilisez `rye --version` pour vérifier qu'il a été installé.

```bash
$ rye --version
rye 0.26.0
commit: 0.26.0 (d245f625e 2024-02-23)
platform: macos (aarch64)
self-python: cpython@3.12
symlink support: true
uv enabled: false
```

### Vérifier l'installation de Python

Vérifiez que Python est disponible :

```bash
$ python --version
Python 3.12.1
```

Super ! Vous avez installé Python. Si vous voyez `zsh: command not found: python`, vérifiez que le PATH Mac est correctement configuré.

La commande `python3` doit vous donner la version installée par Rye, et non la version installée par Xcode.

```bash
$ python3 --version
Python 3.12.1
```

La commande `which` montre le répertoire des shims de Rye lorsque vous essayez de voir où Python est installé. Gardez à l'esprit que vous avez configuré le fichier `~/.zprofile` pour utiliser les shims de Rye afin d'intercepter la commande `python` et de fournir les versions installées par Rye.

```bash
$ which python
/Users/username/.rye/shims/python
```

Vous avez installé Python avec succès avec Rye.

## Gestion des versions et des paquets avec Rye

Vous pouvez utiliser Rye pour :

1. Configurer un projet Python.
2. Installer une version spécifique de Python pour un projet.
3. Installer des bibliothèques Python pour le projet.

D'autres langages adoptent une approche basée sur les projets pour la gestion des paquets (par exemple, Cargo de Rust, Bundler de Ruby et npm de JavaScript). Python a été lent à adopter cette approche, mais Rye change cela, éliminant le besoin d'outils séparés tels que Pyenv, Pip et Venv pour gérer les versions, les bibliothèques logicielles et les environnements.

Avec Rye, vous commencerez par créer un nouveau projet et choisir une version de Python. Vous pourrez ensuite installer des paquets pour ce projet. Rye gérera la version de Python et les paquets pour vous.

### Créer un projet avec Rye

Créez un dossier pour un projet Python. Changez ensuite de répertoire pour accéder à la racine du projet :

```bash
$ mkdir myproject
$ cd myproject
```

Spécifiez une version de Python pour votre projet :

```bash
$ rye pin 3
pinned 3.12.1 in /Users/username/workspace/myproject/.python-version
```

La commande `rye pin 3` créera un fichier `.python-version` spécifiant la version la plus récente de Python pour votre projet.

Vous devez exécuter la commande `rye init` pour créer un fichier `pyproject.toml` dans le répertoire racine de votre projet. Il s'agit d'un fichier de configuration spécifique au projet que Rye utilise pour gérer les versions de Python et les paquets.

```bash
$ rye init
success: Initialized project in /Users/username/workspace/myproject/.
Run `rye sync` to get started
```

Vous pouvez maintenant récupérer une version de Python et installer des paquets.

### Définir une version

Rye peut installer et basculer entre différentes versions de Python.

Rye utilise le terme "toolchains" pour désigner les versions de Python installées. Pour installer une version de Python, vous pouvez [récupérer une toolchain](https://rye-up.com/guide/toolchains/) en utilisant Rye.

```bash
$ rye fetch
$
```

Si vous avez spécifié le Python par défaut avec `rye pin`, `rye fetch` ne fait rien. Si vous avez spécifié une version différente de Python, `rye fetch` installera la version spécifiée.

```bash
$ rye fetch
Downloading cpython@3.12.1
Checking checksum
success: Downloaded cpython@3.12.1
```

Par défaut, Rye installe tous les exécutables Python dans un dossier caché dans votre répertoire personnel `~/.rye/py/`. Les shims de Rye dans le `$PATH` Mac sélectionneront la version correcte de Python que vous avez spécifiée dans votre répertoire de projet.

### Ajouter des paquets

Les gestionnaires de paquets vous permettent de télécharger, installer et mettre à jour des bibliothèques logicielles et leurs dépendances. La plupart des paquets dépendent d'autres bibliothèques logicielles externes—le gestionnaire de paquets récupérera et installera toutes les dépendances requises par ce paquet.

Les développeurs Python expérimentés sont familiers avec [Pip](https://pip.pypa.io/en/stable/), le gestionnaire de paquets standard pour Python, inclus avec toute version de Python depuis Python 3.3.

La commande `pip install` installe les paquets "globalement" dans une version système de Python ou des versions partagées de Python, créant des conflits potentiels.

Pour installer en toute sécurité des bibliothèques Python pour un projet spécifique avec `pip`, vous devez utiliser un gestionnaire d'environnement Python tel que [Venv](https://docs.python.org/3/library/venv) pour créer et activer un environnement virtuel afin d'éviter les conflits de dépendances.

Lorsque vous utilisez Rye comme outil tout-en-un, vous n'aurez pas besoin de `venv` pour la gestion des environnements, installant les paquets directement avec Rye.

Avant d'essayer d'installer un paquet avec Rye, assurez-vous d'avoir créé un fichier `pyproject.toml` dans le répertoire racine de votre projet avec `rye init`.

Vous pouvez installer n'importe quel paquet Python depuis le [Python Package Index](https://pypi.org/). Ici, nous installerons l'utilitaire [cowsay](https://pypi.org/project/cowsay/).

```bash
$ rye add cowsay
Added cowsay>=6.1 as regular dependency
```

Si vous voyez `error: did not find pyproject.toml`, vous devez exécuter `rye init`.

### Synchroniser pour configurer le projet

Avant de pouvoir utiliser un paquet dans un projet Rye, vous devez exécuter `rye sync` pour mettre à jour les fichiers de verrouillage et installer les dépendances dans l'environnement virtuel.

```bash
$ rye sync
Initializing new virtualenv in /Users/username/workspace/python/myproject/.venv
Python version: cpython@3.12.3
Generating production lockfile: /Users/username/workspace/python/myproject/requirements.lock
Creating virtualenv for pip-tools
Generating dev lockfile: /Users/username/workspace/python/myproject/requirements-dev.lock
Installing dependencies
Looking in indexes: https://pypi.org/simple/
Obtaining file:///. (from -r /var/folders/ls/g23m524x5jbg401p12rctz7m0000gn/T/tmp06o05xiq (line 2))
  Installing build dependencies ... done
  Checking if build backend supports build_editable ... done
  Getting requirements to build editable ... done
  Installing backend dependencies ... done
  Preparing editable metadata (pyproject.toml) ... done
Collecting cowsay==6.1 (from -r /var/folders/ls/g23m524x5jbg401p12rctz7m0000gn/T/tmp06o05xiq (line 1))
  Using cached cowsay-6.1-py3-none-any.whl.metadata (5.6 kB)
Using cached cowsay-6.1-py3-none-any.whl (25 kB)
Building wheels for collected packages: myproject
  Building editable for myproject (pyproject.toml) ... done
  Created wheel for myproject: filename=myproject-0.1.0-py3-none-any.whl size=1074 sha256=0b34a41cbb517a78e5b60593c75e93a37df0bf7958e8921be5f6f6e24a26b5d1
  Stored in directory: /private/var/folders/ls/g23m524x5jbg401p12rctz7m0000gn/T/pip-ephem-wheel-cache-m03jgkok/wheels/8b/19/c8/73a63a20645e0f1ed9aae9dd5d459f0f7ad2332bb27cba6c0f
Successfully built myproject
Installing collected packages: myproject, cowsay
Successfully installed cowsay-6.1 myproject-0.1.0
Done!
```

Rye affiche toutes ses opérations, mais vous n'avez pas besoin de lire tous les détails.

### Exécuter Python

Après avoir installé un paquet et exécuté `rye sync`, vous pouvez utiliser l'interpréteur Python de manière interactive (le REPL ou Read-Eval-Print Loop).

```bash
$ python
Python 3.12.1 (main, Jan  7 2024, 23:31:12) [Clang 16.0.3 ] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import cowsay
>>> cowsay.cow('Hello World')
___________
| Hello World |
  ===========
           \
            \
              ^__^
              (oo)\_______
              (__)\       )\/\
                  ||----w |
                  ||     ||
>>>
```

Entrez `quit()` ou tapez `Control + D` pour quitter l'interpréteur Python.

Vous êtes maintenant prêt à développer n'importe quel projet Python avec Rye ! Vous pouvez lire le [Guide de l'utilisateur de Rye](https://rye-up.com/guide/) pour en savoir plus.

## Workflow Python avec Rye

Lorsque vous codez en Python, vous voudrez ajouter des bibliothèques logicielles à votre projet. Examinons un exemple.

[Requests](https://pypi.org/project/requests/) est une bibliothèque HTTP que vous utiliserez probablement dans de nombreux projets. Si vous visitez la [page Requests sur PyPI](https://pypi.org/project/requests/), vous verrez les instructions d'installation :

```bash
$ python -m pip install requests
```

La commande `python -m pip` est un peu fastidieuse, et si vous utilisez Pip, vous devez la précéder de `python -m venv .venv` (pour configurer un environnement virtuel) et `source .venv/bin/activate` (pour activer un environnement virtuel).

Avec Rye, vous pouvez ajouter Requests à votre fichier `pyproject.toml`.

```bash
$ rye add requests
```

Ensuite, exécutez `rye sync` pour installer le paquet.

```bash
$ rye sync
```

Vous pouvez maintenant utiliser la bibliothèque Requests dans votre projet Python, en l'incluant avec une instruction `import`.

Rappelez-vous, lorsque vous voyez `pip install` dans un tutoriel, vous pouvez utiliser `rye add` et `rye sync` à la place, sans commandes supplémentaires pour un environnement virtuel.

Les débutants utilisant [pip install](https://mac.install.guide/python/pip-install) rencontrent souvent des problèmes avec [command not found: pip](https://mac.install.guide/python/command-not-found-pip) et [error: externally-managed-environment](https://mac.install.guide/python/externally-managed-environment). Rye élimine ces problèmes.

## Conclusion

Cet article est basé sur un guide qui offre des détails supplémentaires sur la façon d'[installer Python sur Mac](https://mac.install.guide/python/install).

Rye est le nouveau favori pour installer et gérer Python car il offre une configuration et un système de packaging cohérents, éliminant le besoin d'outils séparés tels que Pyenv, Pip et Venv pour gérer les versions, les bibliothèques logicielles et les environnements.

Python est le premier langage de programmation pour la plupart des débutants. À mesure qu'il gagne en popularité pour le machine learning et la science des données, vous voudrez avoir Python sur votre Mac pour de nombreux tutoriels que vous trouverez sur freeCodeCamp.