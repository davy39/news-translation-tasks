---
title: Comment installer Python 3 sur Mac – Tutoriel d'installation et de mise à jour
  avec Brew
subtitle: ''
author: Quincy Larson
co_authors: []
series: null
date: '2021-04-06T03:19:47.000Z'
originalURL: https://freecodecamp.org/news/python-version-on-mac-update
coverImage: https://cdn-media-2.freecodecamp.org/w1280/606ba4e1d5756f080ba94d0c.jpg
tags:
- name: mac
  slug: mac
- name: Python
  slug: python
seo_title: Comment installer Python 3 sur Mac – Tutoriel d'installation et de mise
  à jour avec Brew
seo_desc: 'MacOS comes with Python pre-installed. But it''s Python Version 2.7, which
  is now deprecated (abandoned by the Python developer community).

  The entire Python community has now moved on to using Python 3.x (the current version
  as of writing this is 3.9...'
---

MacOS est livré avec Python préinstallé. Mais il s'agit de la version Python 2.7, qui est désormais obsolète (abandonnée par la communauté des développeurs Python).

L'ensemble de la communauté Python utilise désormais Python 3.x (la version actuelle au moment de la rédaction de cet article est 3.9). Et Python 4.x sera bientôt disponible, mais il sera entièrement rétrocompatible.

Si vous essayez d'exécuter Python depuis votre terminal MacOS, vous verrez même cet avertissement :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/freecodecamp_-_freecodecamp_MacBook-Pro_-___-_-zsh_-_84-24-1.png)
_AVERTISSEMENT : Python 2.7 n'est pas recommandé. Cette version est incluse dans macOS pour la compatibilité avec les logiciels hérités. Les futures versions de macOS n'incluront pas Python 2.7. Il est plutôt recommandé de passer à l'utilisation de 'python3' depuis le Terminal._

Jusqu'à ce qu'Apple décide de définir Python 3.x comme version par défaut, vous devrez l'installer vous-même.

## Une seule commande pour exécuter Python 3

Pour certains d'entre vous qui lisez ceci, cette commande peut suffire. Vous pouvez exécuter Python 3 en utilisant cette commande (avec le 3 à la fin).

```bash
python3
```

Si c'est tout ce que vous cherchiez, pas de problème. Passez une bonne journée et bon codage.

Mais si vous voulez un système de contrôle de version Python approprié pour suivre les différentes versions et avoir un contrôle fin sur la version que vous utilisez, ce tutoriel vous montrera exactement comment y parvenir.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Megaman-810x600.jpeg)
_En passant, si vous vous demandez pourquoi je continue de faire référence à Python 3.x, le x est un substitut pour les sous-versions (ou les versions ponctuelles comme les appellent les développeurs). Cela signifie n'importe quelle version de Python 3._

## Comment installer Homebrew sur Mac

Tout d'abord, vous devez installer Homebrew, un puissant gestionnaire de paquets pour Mac.

Ouvrez votre terminal. Vous pouvez le faire en utilisant la recherche Spotlight de MacOS (commande+espace) et en tapant "terminal".

Maintenant que vous êtes dans une ligne de commande, vous pouvez installer la dernière version de Homebrew en exécutant cette commande :

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Votre terminal demandera un accès de niveau Super Utilisateur. Vous devrez taper votre mot de passe pour exécuter cette commande. Il s'agit du même mot de passe que vous tapez lorsque vous vous connectez à votre Mac. Tapez-le et appuyez sur entrée.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/freecodecamp_-__bin_bash_-c__-__bin_bash_-_sudo_-_bash_-c____bin_bash_012set_-u_012_012abort___-_012__printf___s_n_______012__exit_1_012-_012_012if___-z___-BASH_VERSION_--_____then_012__abort__Bash_is_required_to_interpret_this_script___012.png)
_Une capture d'écran de mon terminal fortement personnalisé. Votre terminal aura probablement un aspect différent._

Homebrew vous demandera de confirmer que vous souhaitez installer ce qui suit. Vous devez appuyer sur entrée pour continuer. (Ou appuyez sur une autre touche si vous avez des doutes.)

![Image](https://www.freecodecamp.org/news/content/images/2021/04/freecodecamp_-__bin_bash_-c__-__bin_bash_-_bash_-c____bin_bash_012set_-u_012_012abort___-_012__printf___s_n_______012__exit_1_012-_012_012if___-z___-BASH_VERSION_--_____then_012__abort__Bash_is_required_to_interpret_this_script___012fi_012_.png)

## Comment installer pyenv pour gérer vos versions de Python

Maintenant, prenons un moment pour installer PyEnv. Cette bibliothèque vous aidera à basculer entre différentes versions de Python (au cas où vous auriez besoin d'exécuter Python 2.x pour une raison quelconque, et en prévision de l'arrivée de Python 4.0).

Exécutez cette commande :

```bash
brew install pyenv
```

![Image](https://www.freecodecamp.org/news/content/images/2021/04/freecodecamp_-_freecodecamp_MacBook-Pro_-___-_-zsh_-_90-24.png)
_PyEnv en cours d'installation_

Maintenant, vous pouvez installer la dernière version de Python.

## Comment utiliser pyenv pour installer Python ou mettre à jour votre version de Python

Maintenant, vous devez simplement exécuter la commande suivante :

```bash
pyenv install 3.9.2
```

Notez que vous pouvez remplacer 3.9.2 par la dernière version de Python. Par exemple, une fois que Python 4.0.0 sera disponible, vous pourrez exécuter ceci :

```bash
pyenv install 4.0.0
```

## Dépannage de l'installation de pyenv

Si vous rencontrez une erreur indiquant que "Le compilateur C ne peut pas créer d'exécutables", la solution la plus simple est de réinstaller Xcode d'Apple.

Xcode est un outil créé par Apple qui inclut toutes les bibliothèques C et autres outils utilisés par Python lorsqu'il s'exécute sur MacOS. Xcode pèse environ 11 gigaoctets, mais vous voudrez être à jour. Vous pourriez vouloir exécuter cela pendant que vous dormez.

Vous pouvez [obtenir la dernière version de Xcode d'Apple ici](https://developer.apple.com/download/). J'ai dû le faire après avoir mis à jour vers MacOS Big Sur, mais une fois que ce fut fait, toutes les commandes suivantes ont fonctionné correctement. Il suffit de relancer la commande `pyenv install 3.9.2` et cela devrait maintenant fonctionner.

## Comment configurer votre PATH MacOS pour pyenv (Bash ou ZSH)

Tout d'abord, vous devez mettre à jour votre chemin Unix pour permettre à PyEnv d'interagir avec votre système.

Voici une longue explication de comment fonctionne PATH dans MacOS (et Unix), directement depuis [le dépôt GitHub de pyenv](https://github.com/pyenv/pyenv).

> Lorsque vous exécutez une commande comme `python` ou `pip`, votre système d'exploitation recherche dans une liste de répertoires un fichier exécutable avec ce nom. Cette liste de répertoires est stockée dans une variable d'environnement appelée `PATH`, chaque répertoire de la liste étant séparé par un deux-points :

```
/usr/local/bin:/usr/bin:/bin

```

> Les répertoires dans `PATH` sont recherchés de gauche à droite, donc un exécutable correspondant dans un répertoire au début de la liste prend le pas sur un autre à la fin. Dans cet exemple, le répertoire `/usr/local/bin` sera recherché en premier, puis `/usr/bin`, puis `/bin`.

Et voici leur explication de ce qu'est un Shim. Je les cite à nouveau longuement car je ne pourrais pas mieux expliquer cela moi-même.

> pyenv fonctionne en insérant un répertoire de _shims_ au début de votre `PATH` :

```
$(pyenv root)/shims:/usr/local/bin:/usr/bin:/bin

```

> Grâce à un processus appelé _rehashing_, pyenv maintient des shims dans ce répertoire pour correspondre à chaque commande Python à travers chaque version installée de Python—`python`, `pip`, et ainsi de suite.

> Les shims sont des exécutables légers qui transmettent simplement votre commande à pyenv.

Voici comment mettre à jour votre `.bash_profile` dans Bash (qui est installé par défaut dans MacOS) :

```
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
```

Puis exécutez :

```
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
```

**Note :** si vous n'avez pas de répertoire `/bin` dans votre dossier `pyenv_root` (vous pouvez n'avoir qu'un répertoire `/shims`), vous devrez peut-être exécuter cette version de la commande :

```
echo 'export PATH="$PYENV_ROOT/shims:$PATH"' >> ~/.bash_profile
```

Ensuite, vous voulez ajouter PyEnv Init à votre terminal. Exécutez cette commande si vous utilisez Bash (à nouveau, c'est le défaut avec MacOS) :

```
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bash_profile
```

Maintenant, réinitialisez votre terminal en exécutant cette commande :

```
reset
```

## Comment configurer votre PATH MacOS pour pyenv dans ZSH ou OhMyZSH

Si, au lieu d'utiliser Bash par défaut sur Mac, vous utilisez ZSH (ou OhMyZSH) comme moi, vous voudrez modifier le fichier `.zshrc` à la place :

```
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
```

Puis exécutez ceci :

```
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init --path)"\n  eval "$(pyenv init -)"\nfi' >> ~/.zshrc
```

## Comment définir une version de Python comme défaut global (Bash ou ZSH)

Vous pouvez définir la dernière version de Python comme globale, ce qui signifie qu'elle sera la version par défaut de Python utilisée par MacOS lorsque vous exécuterez des applications Python.

Exécutez cette commande :

```bash
pyenv global 3.9.2
```

Encore une fois, vous pouvez remplacer 3.9.2 par la dernière version disponible.

Maintenant, vous pouvez vérifier que cela a fonctionné en vérifiant la version globale de Python :

```bash
pyenv versions
```

Vous devriez voir cette sortie :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/freecodecamp_-_freecodecamp_MacBook-Pro_-_-zsh_-_84-24.png)
_L'étoile (*) signifie que cette version est désormais le défaut global_

## L'étape finale : Fermez votre terminal et redémarrez-le

Une fois que vous avez redémarré votre terminal, vous pouvez exécuter la commande `python` et vous lancerez la nouvelle version de Python au lieu de l'ancienne.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/freecodecamp_-_python_-_python_-_python_-_119-36.png)
_Oui. Python 3.9.2 et aucun avertissement de dépréciation_

Félicitations. Merci d'avoir lu ceci, et bon codage.