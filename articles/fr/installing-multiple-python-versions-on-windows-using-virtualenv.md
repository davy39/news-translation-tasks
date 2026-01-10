---
title: Installer plusieurs versions de Python sur Windows en utilisant Virtualenv
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-15T09:42:20.000Z'
originalURL: https://freecodecamp.org/news/installing-multiple-python-versions-on-windows-using-virtualenv
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/download-1.png
tags:
- name: Python
  slug: python
- name: virtualenv
  slug: virtualenv
- name: Windows 10
  slug: windows-10
seo_title: Installer plusieurs versions de Python sur Windows en utilisant Virtualenv
seo_desc: 'By Dalya Gartzman

  You are here because:


  You are using Windows OS version 10+

  You would like to use multiple Python versions on the same computer

  You are tired of the internet telling you to “Just Use Virtualenv”


  TL;DR


  Open Command Prompt and enter...'
---

Par Dalya Gartzman

Vous êtes ici parce que :

1. Vous utilisez Windows OS version 10+
2. Vous souhaitez utiliser plusieurs versions de Python sur le même ordinateur
3. Vous en avez assez qu'Internet vous dise de "Juste Utiliser Virtualenv"

### TL;DR

1. Ouvrez l'`Invite de commandes` et entrez `pip install virtualenv`
2. Téléchargez la version souhaitée de `python` (ne PAS ajouter au PATH !), et souvenez-vous du `chemin\vers\nouveau_python.exe` de la version nouvellement installée
3. Pour créer un virtualenv, ouvrez l'`Invite de commandes` et entrez   
`virtualenv \chemin\vers\env -p chemin\vers\nouveau_python.exe`
4. Si vous utilisez `PyCharm`, mettez à jour l'`Interpréteur de projet` et la `Vérification de compatibilité du code`.
5. Pour installer des packages :   
(I) Activez virtualenv : ouvrez l'`Invite de commandes` et entrez `chemin\vers\env\Scripts\activate.bat`   
(II)  Installez les packages souhaités  
(III)  Désactivez avec `deactivate` .

### La version longue ; À lire

#### Prologue

Si vous utilisez l'[Application Anaconda](https://www.anaconda.com/distribution/#download-section), ce processus pourrait être plus facile en utilisant leur interface graphique. Je ne l'ai pas essayé moi-même, merci de me faire savoir comment cela s'est passé si vous empruntez cette voie :)

#### 1. Installer virtualenv

Si vous avez déjà des environnements virtuels, ou si vous utilisez Anaconda, assurez-vous que les étapes suivantes sont effectuées **en dehors** de tous ces environnements.

#### 2. Installer Python

Vous pouvez télécharger Python depuis le [site officiel](https://www.python.org/), par exemple pour `python3.7.3`, allez [ici](https://www.python.org/downloads/release/python-373/).

Le fichier que vous devriez télécharger s'appelle `Windows x86-64 executable installer`, ou `Windows x86 executable installer` si pour une raison quelconque vous utilisez un Windows 32 bits.

Une fois le téléchargement terminé, ouvrez le fichier exécutable et une invite d'installation apparaîtra.

* Vous ne voulez PAS ajouter le nouveau Python à votre PATH puisque nous allons avoir plusieurs versions de Python sur le même ordinateur, et nous aimerions que chaque application ne connaisse qu'une seule version de Python.
* Soit utilisez l'emplacement suggéré par défaut pour le nouveau Python, soit fournissez un emplacement de votre choix. Dans les deux cas, souvenez-vous de cet emplacement et désignons-le désormais par `C:\<un_chemin>\Python37` .

![Image](https://cdn-media-1.freecodecamp.org/images/1*6TY68J0S0Mls0m3fthyaCg.png)

#### 3. Créer un virtualenv

Ouvrez l'`Invite de commandes`, ou si vous utilisez Anaconda, ouvrez l'`Anaconda Prompt` .

Décidez où vous voulez que votre virtualenv soit, par exemple,   
`C:\Users\<votre_nom_utilisateur>\Anaconda3\envs\<nom_env>` .

Entrez :

`virtualenv C:\Users\<votre_nom_utilisateur>\Anaconda3\envs\<nom_env> -p C:\<un_chemin>\Python37\python.exe`

#### 4. Mettre à jour l'interpréteur PyCharm

Si vous utilisez PyCharm, ouvrez le projet sur lequel vous souhaitez travailler (qui est/sera écrit avec la nouvelle version de Python), et allez dans `Fichier -> Paramètres -> Projet -> Interpréteur de projet`, appuyez sur l'icône d'engrenage puis `Ajouter..` .

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-43.png)

Cela ouvrira une fenêtre d'invite qui vous permet de définir un nouvel interpréteur :

![Image](https://cdn-media-1.freecodecamp.org/images/1*EyUVRuDrL1NtI-6kyAylpw.png)

En supposant que vous utilisez des inspections de code, vous devrez peut-être indiquer à PyCharm quelle version de Python inspecter. Allez dans `Fichier -> Paramètres -> Éditeur -> Inspections -> Python -> Vérification de compatibilité du code`, assurez-vous que la case en haut indique le projet spécifique sur lequel vous travaillez, et cochez la case de votre version de Python.

![Image](https://cdn-media-1.freecodecamp.org/images/1*vHL71y1uLNsUGPOEOrFmkQ.png)
*Si vous ne voyez pas votre version de Python dans la liste des options, ce pourrait aussi être le moment de mettre à jour PyCharm... oui, cela m'est aussi arrivé...*

#### 5. Installer des packages

Actuellement, votre `virtualenv` ne contient que les packages cruciaux, `pip` et `setuptools`. Pour installer plus de packages :

1. Ouvrez l'`Invite de commandes` ou l'`Anaconda Prompt`, et **activez** votre virtualenv en entrant   
`C:\Users\<votre_nom_utilisateur>\Anaconda3\envs\<nom_env>\activate.bat`
2. Utilisez `pip` pour installer des packages comme vous le faites habituellement.
3. **Désactivez** votre virtualenv en entrant `deactivate` .

### Épilogue

Ce matin, lorsque j'ai décidé d'ouvrir un nouveau projet avec une version différente de Python, j'ai pensé : "Oui, je vais juste utiliser un virtualenv", parce qu'Internet disait que je pouvais "Juste le faire".

Eh bien, cela fonctionne maintenant, alors pas de rancune chère Internet, mais sérieusement, le "Juste" était-il vraiment justifié ? Est-ce que _réinstaller-PyCharm-juste-parce-que-je-veux-avoir-des-inspections-de-code-propres_ tombe sous la catégorie "Juste" ?

En tout cas, en cours de route, je suis tombée sur plusieurs guides utiles, mais chacun ne m'a prise qu'une "seule" étape du chemin, alors j'ai décidé de tout mettre en un seul endroit.

J'espère que mon voyage vous a aidé dans le vôtre, et puissions-nous tous profiter d'un codage heureux, avec aussi peu de friction IT que possible :D

![Image](https://cdn-media-1.freecodecamp.org/images/0*vaVbNQubipSg57aI.jpg)