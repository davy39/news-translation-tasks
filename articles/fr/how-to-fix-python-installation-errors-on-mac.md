---
title: Comment corriger les erreurs courantes d'installation de Python sur macOS
subtitle: ''
author: Daniel Kehoe
co_authors: []
series: null
date: '2024-06-10T22:57:27.000Z'
originalURL: https://freecodecamp.org/news/how-to-fix-python-installation-errors-on-mac
coverImage: https://www.freecodecamp.org/news/content/images/2024/06/python-install-errors.png
tags:
- name: error
  slug: error
- name: macOS
  slug: macos
- name: Python
  slug: python
seo_title: Comment corriger les erreurs courantes d'installation de Python sur macOS
seo_desc: "Python's popularity keeps growing as more developers adopt it for data\
  \ science and machine learning, although it is already among the most popular programming\
  \ languages. \nI recently wrote an article for freeCodeCamp titled \"How to Install\
  \ Python on a..."
---

La popularité de Python continue de croître alors que de plus en plus de développeurs l'adoptent pour la science des données et l'apprentissage automatique, bien qu'il soit déjà parmi les langages de programmation les plus populaires. 

J'ai récemment écrit un article pour freeCodeCamp intitulé "[How to Install Python on a Mac](https://www.freecodecamp.org/news/how-to-install-python-on-a-mac/)", qui fournit un guide clair pour installer Python sur macOS. 

En complément, je vais discuter des erreurs que vous pouvez rencontrer lors de l'installation de Python sur macOS et comment les corriger dans cet article.

## **Contenu**

Voici ce que nous allons couvrir ici :

* [Comment corriger l'erreur "command not found: python"](#heading-comment-corriger-l-erreur-command-not-found-python)
* [Utilisation d'une version obsolète de Python](#heading-utilisation-d-une-version-obsolete-de-python)
* [Utilisation du Python système](#heading-utilisation-du-python-systeme)
* [Utilisation du Python Homebrew](#heading-utilisation-du-python-homebrew)
* [Pip manquant](#heading-pip-manquant)
* [Erreurs d'installation de paquets Pip](#heading-erreurs-d-installation-de-paquets-pip)
* [Plus sur Mac Python](#heading-plus-sur-mac-python)
* [Conclusion](#heading-conclusion)

## Comment corriger l'erreur "command not found: python"

Vous pouvez rencontrer cette erreur :

```bash
$ python ...
zsh: command not found: python

```

Vous verrez cela lorsque vous essayez d'exécuter des commandes Python dans le terminal. Cela se produit principalement parce que Python n'est pas encore installé. Cependant, il est également possible, et plus frustrant, que l'installation de Python ne soit pas dans le PATH de Mac.

Si vous devez uniquement installer et exécuter une application Python, vous pouvez utiliser [Homebrew](https://mac.install.guide/homebrew/) pour [installer Pipx](https://mac.install.guide/python/pipx). Cela installera Python comme une dépendance. Pipx est un outil qui vous permet d'installer et d'exécuter des applications Python comme des exécutables autonomes, évitant les conflits de dépendances qui peuvent survenir lors de l'utilisation du gestionnaire de paquets Python standard [Pip](https://pip.pypa.io/en/stable/).

Si vous allez travailler sur un projet de programmation en Python, [installez Python avec Pyenv](https://mac.install.guide/python/install-pyenv), le gestionnaire de versions Python standard. Mieux encore, [installez Python avec Rye](https://mac.install.guide/python/install-rye), un outil tout-en-un pour l'installation de Python, la gestion des environnements virtuels et l'installation des paquets.

Si vous voyez l'erreur `zsh: command not found: python`, et que vous êtes certain d'avoir déjà installé Python, vous devrez peut-être mettre à jour le [Mac Python PATH](https://mac.install.guide/python/path). Vous devrez trouver où Python est installé sur votre système, ce qui nécessite une certaine investigation car il existe plusieurs façons d'installer Python sur macOS.

Voici les emplacements les plus courants pour Python sur un Mac :

1. `/usr/bin/python3` est le Python système installé avec les outils de ligne de commande Xcode. Il s'agit d'un alias ; l'emplacement réel est `/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/bin`.
2. `/opt/homebrew/opt/python@3.12/libexec/bin/python` est le Python Homebrew.
3. `/Library/Frameworks/Python.framework/Versions/3.12/bin/python3` est le Python installé avec l'installateur officiel du site Python.
4. `/Users/username/.pyenv/shims/python` est le Python installé avec Pyenv.
5. `/Users/username/.rye/shims/python` est le Python installé avec Rye.

Entrez le chemin complet suivi de `python --version` et voyez si vous obtenez un numéro de version. Si c'est le cas, vous devrez mettre à jour votre PATH en ajoutant le chemin d'installation de Python à votre fichier `.zprofile`. Pour plus d'informations, voir [Mac PATH](https://mac.install.guide/terminal/path).

L'article [Command not found: python](https://mac.install.guide/python/command-not-found-python) entre dans plus de détails si vous avez besoin d'aide.

## Utilisation d'une version obsolète de Python

La version actuelle de Python est 3.12, en octobre 2023. Les nouvelles versions de Python sortent chaque année, généralement en octobre. La prochaine version, Python 3.13, est attendue en octobre 2024. La [dernière version de Python](https://www.python.org/downloads/source/) est répertoriée sur le site Python.

Vérifiez la version de Python sur votre Mac :

```bash
$ python --version
Python 3.12.4

```

Vous devriez voir `Python 3.12.4` ou une version ultérieure. Vous ne remarquerez peut-être pas de problèmes avec une version plus ancienne de Python, mais il est bon de commencer tout projet avec la version la plus récente. L'article sur la [mise à jour de Python sur Mac](https://mac.install.guide/python/update) explique comment mettre à jour Python sur macOS.

## Utilisation du Python système

Les Mac ne viennent plus avec Python préinstallé. Mais vous avez peut-être installé [Xcode Command Line Tools](https://mac.install.guide/commandlinetools/) qui inclut Python 3.9.6, une version plus ancienne de Python qui prend en charge les utilitaires de développement Apple.

Essayez `python3 --version` et `which -a python3` pour vérifier si Python a été installé avec Xcode Command Line Tools.

```bash
$ python3 --version
Python 3.9.6
$ which -a python3
/usr/bin/python3

```

Si vous avez Python 3.9.6 installé dans `/usr/bin/python3`, vous aurez probablement le Python système installé par Xcode Command Line Tools. Vous pouvez confirmer cela avec `xcode-select -p` qui montrera si Xcode Command Line Tools est installé.

```bash
$  xcode-select -p
/Library/Developer/CommandLineTools

```

Il est possible de [créer un alias python3 vers python](https://mac.install.guide/python/alias-python3), mais je ne recommanderais pas d'utiliser le Python système pour le développement. Le Python système est destiné aux utilitaires Apple, pas pour vous, donc vous devriez installer Python sur macOS séparément si vous voulez exécuter des programmes Python ou développer en Python.

Voir mon article freeCodeCamp [How to Install Python on a Mac](https://www.freecodecamp.org/news/how-to-install-python-on-a-mac/) pour installer Python pour le développement.

## Utilisation du Python Homebrew

Si vous utilisez Homebrew comme gestionnaire de paquets logiciels, vous pouvez facilement installer Python avec `brew install python`. Le Python installé avec Homebrew est adapté pour exécuter des scripts, mais il présente des inconvénients pour l'installation d'applications Python ou le développement de logiciels Python, lorsque des paquets sont installés.

* **Mises à jour automatiques de Homebrew.** Homebrew met automatiquement à jour son Python comme une dépendance pour d'autres paquets, ce qui peut casser vos projets.
* **Plusieurs projets peuvent nécessiter différentes versions de Python.** Le Python installé avec Homebrew est une seule version et vous pouvez avoir besoin de basculer entre différentes versions pour différents projets.
* **Problèmes avec l'isolation de l'environnement.** Homebrew fournit un seul environnement Python, ce qui peut causer des conflits entre les projets. Pip, le gestionnaire de paquets Python, bloquera l'installation des paquets à moins que vous ne créiez d'abord un environnement virtuel.

Vous pouvez vérifier si Python est installé avec Homebrew :

```bash
$ brew list | grep python
python@3.12

```

Pour exécuter des applications, il est préférable d'[installer Pipx](https://mac.install.guide/python/pipx) et d'utiliser `pipx install` au lieu de `pip install` pour installer des programmes. Pour le développement Python, il est préférable d'installer Pyenv ou d'installer Rye pour la gestion des versions Python et des environnements virtuels.

## Pip manquant

Les README et les tutoriels supposent souvent que les utilisateurs sont familiers avec les outils de développement Python et leur demandent d'installer des paquets Python en utilisant Pip, le gestionnaire de paquets Python. Si vous avez suivi des instructions qui commencent par `pip install <package>`, vous avez peut-être rencontré l'erreur `zsh: command not found: pip`.

Voici l'erreur que vous verrez :

```bash
$ pip install <package>
zsh: command not found: pip

```

Pip est installé automatiquement avec Python, il est donc inhabituel d'exécuter la commande `python` avec succès puis `pip` et de voir l'erreur. Si vous avez Python installé, vous devriez pouvoir utiliser la commande `pip`. Vous pouvez essayer une commande spéciale qui installe Pip :

```bash
$ python -m ensurepip --upgrade

```

Si Pip n'est pas déjà installé, cette commande l'installera. Sinon, rien ne se passera. Avec cette erreur, il est plus probable que vous ayez une installation de Python qui n'est pas dans votre Mac Python PATH. Voir l'article [Command not found: pip](https://mac.install.guide/python/command-not-found-pip) pour plus de détails.

## Erreurs d'installation de paquets Pip

Vous devrez utiliser Pip pour installer des paquets Python, sauf si vous utilisez [Rye](https://rye.astral.sh/) comme outil tout-en-un. Cependant, Pip présente certains inconvénients.

Par défaut, la commande `pip install <package>` installe le paquet "globalement". Cela signifie que le paquet est ajouté au répertoire global Python `site-packages`, ce qui peut entraîner des conflits si différents projets nécessitent différentes versions du même paquet. 

Par exemple, si le projet A nécessite `package==1.0` et le projet B nécessite `package==2.0`, l'installation des deux paquets globalement peut entraîner des conflits et [dependency hell](https://en.wikipedia.org/wiki/Dependency_hell). Sans une isolation appropriée, l'installation des dépendances d'un projet peut causer des problèmes pour un autre. Pour éviter ces conflits, créez un environnement virtuel Python pour chaque projet.

Il existe deux outils Python pour créer des environnements virtuels et utiliser différentes versions de paquets. [Venv](https://docs.python.org/3/library/venv) est un paquet Python intégré. [Virtualenv](https://virtualenv.pypa.io/en/latest/) est un outil plus puissant avec des fonctionnalités supplémentaires. Ces outils permettent à `pip` d'installer des paquets Python dans un environnement virtuel qui a ses propres répertoires d'installation et ne partage pas de bibliothèques avec d'autres environnements virtuels. Pip doit être utilisé en conjonction avec Venv ou Virtualenv pour installer avec succès des paquets.

Lorsque vous essayez d'installer un paquet avec Pip, vous pouvez voir :

```bash
$ pip install <package>
error: externally-managed-environment

```

Les versions récentes de `pip` implémentent [PEP 668](https://peps.python.org/pep-0668/) pour empêcher les tentatives d'installation de paquets globalement, ce qui entraîne le message [error: externally-managed-environment](https://mac.install.guide/python/externally-managed-environment). Cette erreur se produit lorsque vous essayez d'installer un paquet globalement sans utiliser un environnement virtuel. Pour résoudre cette erreur, créez un environnement virtuel en utilisant Venv ou Virtualenv et installez le paquet à l'intérieur.

## Plus sur Mac Python

Vous devrez faire plus qu'installer Python pour commencer un projet de programmation, donc j'ai également écrit un article plus long sur [Mac Python](https://mac.install.guide/python/) qui explique les fondamentaux de la gestion des versions, des environnements virtuels et de la gestion des paquets, ainsi que la comparaison des différentes options d'installation.

## Conclusion

Une variété d'outils de développement concurrents signifie qu'il peut être difficile de commencer avec Python par rapport à d'autres langages de programmation tels que JavaScript, Rust ou Ruby. Python évolue vers une standardisation des outils, et il y a une innovation rapide alors que la communauté cherche à améliorer l'expérience des développeurs.

Pour l'instant, le développement des compétences Python nécessite une certaine connaissance de l'écosystème Python, des différents outils et de leur utilisation. Néanmoins, Python est populaire et puissant, et les tutoriels sur freeCodeCamp vous aideront à apprendre le langage et à devenir un meilleur développeur.