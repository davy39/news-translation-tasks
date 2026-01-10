---
title: Comment installer Python 3 sur Mac et mettre à jour la version avec Pyenv –
  Guide des commandes MacOS Homebrew
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-03-04T18:44:30.000Z'
originalURL: https://freecodecamp.org/news/how-to-install-python-3-on-mac-and-update-the-python-version-macos-homebrew-command-guide
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/pexels-christina-morillo-1181359--2-.jpg
tags:
- name: macOS
  slug: macos
- name: Python
  slug: python
- name: Python 3
  slug: python3
seo_title: Comment installer Python 3 sur Mac et mettre à jour la version avec Pyenv
  – Guide des commandes MacOS Homebrew
seo_desc: 'By Dillion Megida

  When using Python, you may install different version variations for different projects.
  But sometimes this can affect how your code executes, as it may not use the correct
  version.

  In this article, we''ll learn how to install new Pyt...'
---

Par Dillion Megida

Lorsque vous utilisez Python, vous pouvez installer différentes versions pour différents projets. Mais parfois, cela peut affecter l'exécution de votre code, car il peut ne pas utiliser la bonne version.

Dans cet article, nous allons apprendre comment installer de nouvelles versions de Python (Python 3 dans notre cas) et comment définir cette version comme version active pour l'exécution du code.

## Installer Pyenv

%[https://github.com/pyenv/pyenv]

Si vous êtes familier avec NodeJS, vous savez que `nvm` est utilisé pour gérer les versions de Node dans différents environnements. `pyenv` fait la même chose pour Python – c'est un outil de gestion de versions.

Cet outil vous aide à travailler sur différents environnements qui nécessitent différentes versions de Python.

Installez `pyenv` en utilisant [Homebrew](https://brew.sh/) avec la commande suivante :

Voici la commande pour installer Python 3 sur Mac :

```bash
brew install pyenv
```

Assurez-vous de suivre [le reste des étapes pour installer pyenv dans la documentation](https://github.com/pyenv/pyenv#homebrew-on-macos).

## Installer Python 3

Avec `pyenv` installé, vous n'avez plus besoin d'installer Python avec Homebrew (comme vous le faisiez peut-être déjà). Vous pouvez installer Python en utilisant `pyenv` avec la syntaxe suivante :

```bash
pyenv install [version]
```

L'argument de version suit la version sémantique qui est "majeur.mineur.patch".

Pour Python 3, disons que nous voulons installer `3.10.2`. Alors nous utiliserons cette commande :

```bash
pyenv install 3.10.2
```

Pour voir la liste des versions de Python que nous avons, nous utilisons la commande suivante :

```bash
pyenv versions
```

Dans mon cas, j'ai :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-6.png)
_Versions de Python actuellement installées sur mon système_

D'après la capture d'écran ci-dessus, l'astérisque montre la version de Python actuellement active, qui est la version par défaut du système :

```shell
python --version
# Python 2.7.18
```

Pour définir la version nouvellement installée comme version par défaut, voici comment faire ([parmi de nombreuses autres façons](https://github.com/pyenv/pyenv#choosing-the-python-version)) :

```bash
pyenv global 3.10.2

python --version
# Python 3.10.2
```

Si votre version de Python reste la même, vous devez vous assurer d'ajouter la commande d'initialisation requise comme vous pouvez le voir dans la documentation : [Basic GitHub Checkout – 2. Configure your shell's environment for Pyenv](https://github.com/pyenv/pyenv#basic-github-checkout)

Avec tout cela en place, vous pouvez maintenant utiliser Python 3.

## Mettre à jour la version de Python

Avec la sortie de nouvelles versions, vous pouvez vouloir mettre à jour votre version. Vous pouvez mettre à jour votre version en installant une nouvelle version, en la définissant comme votre version globale par défaut, et en désinstallant optionnellement l'ancienne version.

Voici les commandes pour cela :

```bash
pyenv install nouvelle.version.python

pyenv global nouvelle.version.python

pyenv uninstall ancienne.version.python
```

Merci d'avoir lu ! J'espère que vous avez maintenant la version de Python installée qui vous est la plus utile.