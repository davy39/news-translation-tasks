---
title: Comment modifier PYTHONPATH sur Windows
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-14T20:12:10.000Z'
originalURL: https://freecodecamp.org/news/how-to-edit-pythonpath-on-windows-eafd19840d44
coverImage: https://cdn-media-1.freecodecamp.org/images/1*iqGsyUGrUySN0awiYr3X8A.jpeg
tags:
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
- name: Windows 10
  slug: windows-10
seo_title: Comment modifier PYTHONPATH sur Windows
seo_desc: 'By Dalya Gartzman

  You are here because you are using:


  Windows OS version 10+

  Python version 3.3+

  Anaconda3


  And you would like to edit your PYTHONPATH permanently.

  TL;DR


  Go to C:\Users\<your_username>\Anaconda3\Lib\site-packages

  Create a file pytho...'
---

Par Dalya Gartzman

Vous êtes ici parce que vous utilisez :

1. Windows OS version 10+
2. Python version 3.3+
3. Anaconda3

Et vous souhaitez modifier votre `PYTHONPATH` de manière permanente.

### TL;DR

1. Allez dans `C:\Users\<votre_nom_d_utilisateur>\Anaconda3\Lib\site-packages`
2. Créez un fichier `python37.pth`
3. Modifiez le fichier pour inclure cette ligne `C:\\Users\\<votre_nom_d_utilisateur>\\my_module`

### La version longue ; À lire

#### Prologue

Dans la plupart des cas, modifier le `PYTHONPATH` depuis l'interface graphique des paramètres fera l'affaire. L'astuce est bien expliquée dans [cette réponse Stack Overflow](https://stackoverflow.com/a/4855685/2934048).
Si, dans un premier temps, vous cherchez uniquement à modifier votre chemin **localement**, [cette réponse utile](https://stackoverflow.com/a/43072284/2934048) fera l'affaire.

#### Élément légèrement étendu no. 1

Si vous n'avez pas `C:\Users\<votre_nom_d_utilisateur>\Anaconda3\Lib\site-packages`, remplacez `C:\Users\<votre_nom_d_utilisateur>` par le chemin vers votre Anaconda3.

#### Élément légèrement étendu no. 2

Si vous utilisez Python 3.7, créez un fichier appelé `python37.pth`. Sinon, créez un fichier appelé `python<XX>.pth` pour la version de Python que vous utilisez.

* Vous n'êtes pas sûr de la version ?
Sous `C:\Users\<votre_nom_d_utilisateur>\Anaconda3\`, recherchez un fichier de la forme `python<XX>.dll`. Le `<XX>` indique le numéro de version dont vous avez besoin pour nommer votre fichier `.pth`.
* Windows est super énervant et ne vous laisse pas créer un fichier avec un suffixe `.pth` ?
Il existe de tels fichiers dans le dossier `C:\Users\<votre_nom_d_utilisateur>\Anaconda3\Lib\site-packages`. Copiez l'un d'eux et modifiez le préfixe.
* Certains endroits disent que vous devez créer un fichier `._pth` au lieu de `.pth` ?
Un fichier `._pth` remplacera complètement votre chemin existant. Alors qu'un fichier `.pth` ajoutera son contenu au chemin que vous avez déjà. Vous pouvez trouver plus d'informations [ici](https://docs.python.org/3/using/windows.html#finding-modules).

#### Élément légèrement étendu no. 3

En supposant que la classe `SuperCoolClass` que vous souhaitez importer se trouve à
`C:\Users\<votre_nom_d_utilisateur>\my_project_folder\my_awesome_file.py`.

Ouvrez ensuite votre fichier nouvellement créé `python<XX>.pth` avec votre éditeur de texte préféré (s'il vous plaît, ne dites pas que c'est Vim) et ajoutez une ligne :
`C:\\Users\\<votre_nom_d_utilisateur>\\my_project_folder`.
Oui, avec ces doubles barres obliques ennuyeuses \\ .
Non, sans guillemets "".

Et c'est tout.
Maintenant, vous pouvez importer depuis n'importe où, comme une personne normale :
`from my_awesome_file import SuperCoolClass`.

#### Épilogue

Rien d'important à ajouter ici, vraiment.
J'espère simplement que mes 2 heures de frustration + 1 heure d'écriture de ce post vous ont fait gagner du temps.
À plus.

![Image](https://cdn-media-1.freecodecamp.org/images/UJWkKhiuU7PpnxnwgE2nBm0DE3QLQABY6Bmh)