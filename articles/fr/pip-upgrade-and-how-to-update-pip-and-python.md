---
title: Mise à jour de Pip – Et comment mettre à jour Pip et Python
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-03-14T21:04:29.000Z'
originalURL: https://freecodecamp.org/news/pip-upgrade-and-how-to-update-pip-and-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/updatePip.png
tags:
- name: Python
  slug: python
seo_title: Mise à jour de Pip – Et comment mettre à jour Pip et Python
seo_desc: "Python is a widely used and powerful programming language that's relatively\
  \ simple to learn. \nPython releases patch updates every few months and major updates\
  \ around once in a year. Because of this, it is always a good idea to update the\
  \ version of P..."
---

Python est un langage de programmation largement utilisé et puissant qui est relativement simple à apprendre.

Python publie des mises à jour de correctifs tous les quelques mois et des mises à jour majeures environ une fois par an. Pour cette raison, c'est toujours une bonne idée de mettre à jour la version de Python que vous avez sur votre ordinateur.

De plus, vous devez mettre à jour Python pour avoir accès aux fonctionnalités intéressantes ajoutées lors des mises à jour majeures. Par exemple, il y a une amélioration notable de la vitesse dans Python 3.11 par rapport à 3.10.

Il existe également un gestionnaire de paquets Python appelé Pip que vous pourriez avoir besoin de mettre à jour occasionnellement. C'est à Python ce que NPM est à JavaScript.

À partir de Python 3.4, Pip est inclus dans la distribution Python standard. Mais si vous ne l'obtenez pas après l'installation de Python pour une raison quelconque, vous devez alors l'installer manuellement.

Dans cet article, je vais vous montrer comment mettre à jour Python sur votre ordinateur Mac et Windows. Je vous montrerai également comment mettre à jour Pip sur les deux systèmes d'exploitation.

## Sommaire
- [Comment mettre à jour Python et Pip sur Mac OS](#heading-comment-mettre-a-jour-python-et-pip-sur-mac-os)
- [Comment mettre à jour Python et Pip avec Homebrew](#heading-comment-mettre-a-jour-python-et-pip-avec-homebrew)
- [Comment mettre à jour seulement Pip avec le terminal](#heading-comment-mettre-a-jour-seulement-pip-avec-le-terminal)
- [Conclusion](#heading-conclusion)

## Comment mettre à jour Python et Pip sur Mac OS
L'un des moyens les plus simples de mettre à jour Python et Pip sur Mac consiste à télécharger le package depuis le site officiel de Python.

Lorsque vous mettez à jour Python, la version de Pip qui l'accompagne est également mise à jour.

Tout d'abord, vérifiez les versions de Python et de Pip que vous possédez en exécutant `python3 --version` et `pip3 --version` :

![Screenshot-2023-03-14-at-11.57.29](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-14-at-11.57.29.png)

Allez sur https://www.python.org/downloads/macos/ et sélectionnez la version que vous souhaitez :

![Screenshot-2023-03-14-at-12.16.47](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-14-at-12.16.47.png)

Pour ma part, j'ai choisi `3.11` car elle est désormais stable.

Faites défiler vers le bas et téléchargez-la pour votre système d'exploitation – que ce soit Windows ou Mac. J'ai choisi Mac parce que j'utilise un Mac :

![Screenshot-2023-03-14-at-12.18.09](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-14-at-12.18.09.png)

Lancez l'installateur et suivez toutes les instructions à l'écran.

![Screenshot-2023-03-14-at-12.19.43](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-14-at-12.19.43.png)

Confirmez l'installation en exécutant `python3 --version` et `pip3 --version` :

![Screenshot-2023-03-14-at-12.21.47](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-14-at-12.21.47.png)

## Comment mettre à jour Python et Pip avec Homebrew
Si vous utilisez un Mac, vous pouvez également mettre à jour Python et Pip avec Homebrew.

Installez `pyenv` en exécutant `brew install pyenv`. `pyenv` est un outil de gestion de version Python. C'est à Python ce que NVM (Node version manager) est à JavaScript.

![Screenshot-2023-03-14-at-13.29.50](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-14-at-13.29.50.png)

Installez n'importe quelle version de Python que vous souhaitez, par exemple, 3.9 ou 2.7 :

![Screenshot-2023-03-14-at-13.49.26](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-14-at-13.49.26.png)

Vous pouvez également mettre à jour Python en exécutant `pyenv latest-version-number`. Par exemple, `python 3.11`. Lorsque vous installez cette version de Python, vous installez également Pip.

## Comment mettre à jour seulement Pip avec le terminal
Dans les cas où vous souhaitez mettre à jour uniquement Pip, ouvrez votre terminal et exécutez `pip3 install --upgrade pip`. Vous pouvez ensuite confirmer la mise à jour en exécutant `pip3 --version` :

![Screenshot-2023-03-14-at-13.02.02](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-14-at-13.02.02.png)

## Conclusion
Cet article vous a expliqué comment mettre à jour Python et Pip en téléchargeant le package d'installation et en utilisant la ligne de commande. Nous avons également vu comment vous pouvez mettre à jour Pip seul si vous le souhaitez.

Si vous utilisez Windows et que vous souhaitez mettre à jour Python et Pip, vous pouvez également télécharger le dernier installateur et laisser l'assistant d'installation vous guider tout au long du processus.

Merci de m'avoir lu !