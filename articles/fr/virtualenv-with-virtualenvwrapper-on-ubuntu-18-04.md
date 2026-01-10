---
title: Comment installer Virtualenv avec Virtualenvwrapper sur Ubuntu 18.04
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-01T10:34:00.000Z'
originalURL: https://freecodecamp.org/news/virtualenv-with-virtualenvwrapper-on-ubuntu-18-04
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/1-aMYnl2Ctt9Y-RZ5bodNF2g.jpeg
tags:
- name: Developer
  slug: developer
- name: 'Integrated Development Environment  '
  slug: integrated-development-environment
- name: Ubuntu
  slug: ubuntu
- name: virtualenv
  slug: virtualenv
seo_title: Comment installer Virtualenv avec Virtualenvwrapper sur Ubuntu 18.04
seo_desc: 'By Goran Aviani

  Let me tell you a story. Recently, I realized that I needed to review how to set
  up virtualenvwrapper on top of virtualenv in Ubuntu 18.04. I have completed this
  process several of times on different computers, and every time it seems...'
---

Par Goran Aviani

Permettez-moi de vous raconter une histoire. Récemment, j'ai réalisé que je devais revoir comment installer virtualenvwrapper sur virtualenv dans Ubuntu 18.04. J'ai effectué ce processus plusieurs fois sur différents ordinateurs, et à chaque fois, cela semble être un peu différent de la fois précédente.

Je viens d'avoir un nouvel ordinateur portable et sur le chemin du retour, j'ai lu plusieurs tutoriels sur « Comment installer virtualenvwrapper sur Ubuntu 18.04 ». Et laissez-moi vous dire – cela semblait vraiment facile car tous ces tutoriels étaient assez simples et expliquaient essentiellement comment faire ces trois choses :

* Installer virtualenv
* Installer virtualenvwrapper
* Modifier .bashrc/.bash_profile ou les deux

Mais même si j'ai lu tous ces tutoriels, aucun d'entre eux n'a vraiment fonctionné pour moi.

J'ai rencontré plusieurs erreurs en essayant de comprendre ce qui n'allait pas en suivant les tutoriels. 

D'abord, j'ai eu quelques « mkvirtualenv: command not found », puis un peu de « -bash: /usr/bin/virtualenvwrapper.sh: No such file or directory », et enfin une touche de « ERROR: virtualenvwrapper could not find virtualenv in your path ».

Après quelques recherches, j'ai réalisé que tous les tutoriels sur virtualenvwrapper pour Ubuntu 18.04 sont des copies d'un ancien texte écrit avant avril 2016 (la date de sortie d'Ubuntu 16.04).  

Je le sais parce que depuis Ubuntu 16.04, l'emplacement de l'installation pip de virtualenvwrapper a changé de `/usr/local/bin/virtualenvwrapper.sh` à `~/.local/bin/virtualenvwrapper.sh`. Notez que le répertoire local est caché.

Je vais donc commencer par écrire un tutoriel qui vous montrera comment éviter tous ces problèmes mentionnés ci-dessus.

## Prérequis

Dans cet article, je vais vous montrer comment installer virtualenvwrapper avec pip3 (pip pour Python 3). J'ai choisi cette version de pip plutôt qu'une version Python 2 car la fin de vie de Python 2 était le 1er janvier 2020.

> Python 2 prendra sa retraite dans... [https://pythonclock.org/](https://pythonclock.org/)

Pour suivre ce tutoriel, vous aurez besoin d'un ordinateur avec Ubuntu 18.04 installé et d'une connexion Internet :). Quelques connaissances sur les terminaux et l'éditeur Vim seraient également utiles. Je supposerai que vous avez déjà mis à jour et upgradé votre système.

## Installation d'un environnement virtuel

Ouvrez maintenant votre terminal dans le répertoire personnel en cliquant avec le bouton droit et en choisissant l'option « Ouvrir dans le Terminal ». Vous pouvez également appuyer sur les touches `CTRL`, `ALT` et `T` de votre clavier en même temps pour ouvrir automatiquement l'application Terminal.

Vous devez d'abord créer un répertoire spécial qui contiendra tous vos environnements virtuels. Procédons donc à la création d'un nouveau répertoire caché appelé virtualenv.

```
mkdir .virtualenv
```

Maintenant, vous devez installer pip pour Python3.

```
sudo apt install python3-pip
```

Confirmez l'installation de pip3.

```
pip3 --version
```

Maintenant, installez virtualenv via pip3.

```
pip3 install virtualenv
```

Pour trouver où votre virtualenv a été installé, tapez :

```
which virtualenv
```

Installez virtualenvwrapper via pip3 :

```
pip3 install virtualenvwrapper
```

Nous allons modifier votre fichier .bashrc en ajoutant une ligne qui ajustera chaque nouvel environnement virtuel pour utiliser Python 3. Nous allons pointer les environnements virtuels vers le répertoire que nous avons créé ci-dessus (.virtualenv) et nous allons également pointer vers les emplacements de virtualenv et virtualenvwrapper.

Ouvrez maintenant le fichier .bashrc en utilisant l'éditeur Vim.

```
vim .bashrc
```

Si vous n'avez pas encore utilisé l'éditeur Vim ou si vous ne l'avez pas installé sur votre ordinateur, vous devriez l'installer maintenant. C'est un éditeur Linux largement utilisé, et pour de bonnes raisons.

```
sudo apt install vim
```

Après avoir installé Vim, ouvrez le fichier .bashrc en tapant la commande _vim .bashrc_ dans votre terminal. Naviguez jusqu'en bas du fichier .bashrc, appuyez sur la lettre _i_ pour entrer en mode insertion de Vim, et ajoutez ces lignes :

```
#Paramètres Virtualenvwrapper :
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_VIRTUALENV=/home/goran/.local/bin/virtualenv
source ~/.local/bin/virtualenvwrapper.sh
```

Une fois que vous avez terminé, appuyez sur la touche _esc_. Ensuite, tapez `:wq` et appuyez sur Entrée. Cette commande enregistrera et quittera l'éditeur Vim. Fermez et rouvrez votre terminal lorsque vous avez terminé.

Pour créer un environnement virtuel en Python3 et l'activer immédiatement, utilisez cette commande dans votre terminal :

```
mkvirtualenv nom_de_votre_env
```

Vous devriez confirmer que cet environnement est configuré pour Python3 :

```
Python -V
```

Pour désactiver l'environnement, utilisez la commande deactivate.

```
deactivate
```

Pour lister tous les environnements virtuels disponibles, utilisez la commande _workon_ ou _lsvirtualenv_ (même résultat que workon mais affiché de manière plus élégante) dans votre terminal :

```
workon

lsvirtualenv
```

Pour activer un environnement spécifique, utilisez workon + nom de votre environnement :

```
workon nom_de_votre_env
```

Il existe plusieurs commandes utiles que vous pourriez avoir besoin d'utiliser un jour :

_Rmvirtualenv_ supprimera un environnement virtuel spécifique situé dans votre répertoire .virtualenv.

```
rmvirtualenv nom_de_votre_env
```

_Cpvirtualenv_ copiera l'environnement virtuel existant vers un nouvel environnement virtuel et l'activera.

```
cpvirtualenv ancien_env_virtuel nouvel_env_virtuel
```

Bien joué ! Vous avez maintenant créé votre premier environnement Python 3 isolé.

Merci d'avoir lu ! Consultez d'autres articles comme celui-ci sur [mon profil freeCodeCamp](https://www.freecodecamp.org/news/author/goran/) et d'autres choses amusantes que je construis sur [ma page GitHub](https://github.com/GoranAviani).