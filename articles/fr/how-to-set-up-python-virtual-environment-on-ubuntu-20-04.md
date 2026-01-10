---
title: Comment configurer un environnement virtuel Python sur Ubuntu 20.04
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-12T14:36:40.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-python-virtual-environment-on-ubuntu-20-04
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/prateek-katyal-6jYnKXVxOjc-unsplash.jpg
tags:
- name: 'Integrated Development Environment  '
  slug: integrated-development-environment
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: Ubuntu
  slug: ubuntu
- name: virtualenv
  slug: virtualenv
seo_title: Comment configurer un environnement virtuel Python sur Ubuntu 20.04
seo_desc: 'By Goran Aviani

  I recently got myself a “new” laptop – a Lenovo x270 (yay)! And once again I needed
  to set up a Python virtual environment. So of course I Googled for a solution, just
  to find my previously written article on the same topic!

  So in thi...'
---

Par Goran Aviani

Je viens de me procurer un ordinateur portable "nouveau" – un Lenovo x270 (youpi) ! Et une fois de plus, j'ai dû configurer un environnement virtuel Python. Alors bien sûr, j'ai cherché une solution sur Google, pour tomber sur [mon article précédemment écrit sur le même sujet](https://www.freecodecamp.org/news/virtualenv-with-virtualenvwrapper-on-ubuntu-18-04/) !

Dans cet article, je vais mettre à jour les instructions en fonction de mes nouvelles connaissances.

Et laissez-moi vous dire, c'est plus facile qu'avant car nous allons faire seulement deux choses :

* Installer virtualenvwrapper
* Modifier le fichier .bashrc

## Prérequis

Dans cet article, je vais vous montrer comment configurer virtualenvwrapper avec pip3 (pip pour Python 3). Nous n'allons pas utiliser Python 2 car [il n'est plus supporté](https://www.python.org/doc/sunset-python-2/).

Pour suivre ce tutoriel, vous aurez besoin d'un ordinateur avec Ubuntu 20.04 installé et d'une connexion Internet. De plus, quelques connaissances du terminal et de l'éditeur Vim seraient utiles.

## Configuration d'un environnement virtuel

Ouvrez maintenant votre terminal dans le répertoire personnel en cliquant avec le bouton droit et en choisissant l'option « Ouvrir dans le Terminal ». Vous pouvez également appuyer simultanément sur les touches CTRL, ALT et T de votre clavier pour ouvrir automatiquement l'application Terminal.

Vous devez d'abord créer un répertoire spécial qui contiendra tous vos environnements virtuels. Alors, créez un nouveau répertoire caché appelé virtualenv :

```bash
mkdir .virtualenv
```

## pip3

Maintenant, vous devriez installer pip pour Python 3 :

```bash
sudo apt install python3-pip
```

Confirmez l'installation de pip3 :

```bash
pip3 -V
```

## virtualenvwrapper

virtualenvwrapper est un ensemble d'extensions pour virtualenv. Il fournit des commandes comme mkvirtualenv, lssitepackages, et surtout workon pour basculer entre différents environnements virtualenv.

Installez virtualenvwrapper via pip3 :

```bash
pip3 install virtualenvwrapper
```

## Fichier bashrc

Nous allons modifier votre fichier .bashrc en ajoutant une ligne qui ajustera chaque nouvel environnement virtuel pour utiliser Python 3. Nous allons pointer les environnements virtuels vers le répertoire que nous avons créé précédemment (.virtualenv) et nous allons également pointer vers les emplacements de virtualenv et virtualenvwrapper.

Ouvrez maintenant le fichier .bashrc en utilisant l'éditeur Vim :

```bash
vim .bashrc
```

Si vous n'avez pas encore utilisé Vim ou si vous ne l'avez pas installé sur votre ordinateur, vous devriez l'installer maintenant. C'est l'un des éditeurs Linux les plus largement utilisés et pour de bonnes raisons.

```bash
sudo apt install vim
```

Après avoir installé Vim, ouvrez le fichier .bashrc en tapant la commande `vim .bashrc` dans votre terminal. Allez au bas du fichier .bashrc, appuyez sur la lettre **_i_** pour entrer en mode insertion dans Vim, et ajoutez ces lignes :

```bash
# Paramètres de Virtualenvwrapper :
export WORKON_HOME=$HOME/.virtualenvs
VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
. /usr/local/bin/virtualenvwrapper.sh
```

Une fois que vous avez terminé, appuyez sur la touche **_échap_**, puis tapez **:_wq_** et appuyez sur Entrée. Cette commande enregistrera le fichier et quittera Vim.

Maintenant, vous devez recharger le script bashrc. Il y a deux façons de le faire : fermer et rouvrir votre terminal, ou exécuter cette commande dans le terminal :

```bash
source ~/.bashrc
```

Pour créer un environnement virtuel en Python 3 et l'activer immédiatement, utilisez cette commande dans votre terminal :

```bash
mkvirtualenv nom_de_votre_env
```

Pour désactiver l'environnement, utilisez la commande deactivate.

Pour lister tous les environnements virtuels disponibles, utilisez la commande _workon_ ou _lsvirtualenv_ (lsvirtualenv affichera le même résultat que workon mais de manière plus élégante) dans votre terminal :

```bash
workon
```

```bash
lsvirtualenv
```

Pour activer un environnement spécifique, utilisez workon + nom de votre environnement :

```bash
workon nom_de_votre_env
```

Il existe plusieurs commandes utiles que vous pourriez avoir besoin d'utiliser un jour :

_Rmvirtualenv_ supprimera un environnement virtuel spécifique situé dans votre répertoire .virtualenv.

```bash
rmvirtualenv nom_de_votre_env
```

_Cpvirtualenv_ copiera l'environnement virtuel existant vers un nouvel environnement virtuel et l'activera.

```bash
cpvirtualenv ancien_env_virtuel nouvel_env_virtuel
```

Bien joué ! Vous avez maintenant créé votre premier environnement Python 3 isolé.

Merci d'avoir lu !

Consultez d'autres articles comme celui-ci sur mon [profil freeCodeCamp](https://www.freecodecamp.org/news/author/goran/), mon [profil Medium](https://medium.com/@goranaviani), et d'autres choses amusantes que je construis sur ma [page GitHub](https://github.com/GoranAviani).