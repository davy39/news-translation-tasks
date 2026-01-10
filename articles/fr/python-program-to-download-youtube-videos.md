---
title: Comment créer un programme Python pour télécharger des vidéos YouTube
subtitle: ''
author: David Fagbuyiro
co_authors: []
series: null
date: '2022-11-14T15:56:27.000Z'
originalURL: https://freecodecamp.org/news/python-program-to-download-youtube-videos
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/pexels-christina-morillo-1181671.jpg
tags:
- name: Python
  slug: python
- name: Script
  slug: script
- name: youtube
  slug: youtube
seo_title: Comment créer un programme Python pour télécharger des vidéos YouTube
seo_desc: "YouTube is a well-known internet video streaming service. There are millions\
  \ of videos in categories such as education, entertainment, and travel. \nYou can\
  \ quickly watch videos with a few mouse clicks, but downloading videos is difficult.\
  \ But in a re..."
---

YouTube est un service de streaming vidéo bien connu sur Internet. Il existe des millions de vidéos dans des catégories telles que l'éducation, le divertissement et les voyages. 

Vous pouvez regarder des vidéos rapidement avec quelques clics de souris, mais le téléchargement de vidéos est difficile. Cependant, lors d'une récente mise à jour, YouTube permet désormais de sauvegarder des vidéos dans son dossier de téléchargement pour une lecture hors ligne. Pourtant, vous ne pouvez pas les sauvegarder localement.

Dans ce tutoriel, vous apprendrez comment utiliser du code Python pour télécharger des vidéos YouTube. Comme vous le savez peut-être, l'une des grandes forces de Python est son énorme nombre de modules et de bibliothèques. Nous allons écrire le script Python en utilisant le package populaire pytube.

## Prérequis

Voici les exigences de base pour suivre ce tutoriel :

* Compréhension du langage de programmation Python
* Vous devez avoir Python 3+ installé sur votre ordinateur
* Vous devez avoir installé la bibliothèque Python Pytube
* Vous devez avoir un éditeur de code Python tel que Pycharm, Vscode, etc.

## Présentation et installation de Pytube

Pytube est un petit module Python sans dépendance pour accéder aux vidéos depuis Internet.

La bibliothèque native n'est pas pytube – vous devez d'abord l'installer pour pouvoir l'utiliser. Lorsque vous avez pip, l'installation est simple.

Pour installer Pytube avec pip, vous devrez ouvrir votre invite de commande CLI en tant qu'administrateur et entrer la commande suivante :

```
pip install pytube
```

La bibliothèque pytube améliore les téléchargements de vidéos. Construisez l'objet du module YouTube en fournissant l'URL comme paramètre. Ensuite, obtenez l'extension et la résolution appropriées de la vidéo. Vous pouvez changer le nom du fichier à votre guise – sinon, le nom d'origine sera conservé.

Maintenant, passons à l'aspect principal de l'écriture et de l'implémentation du code pour télécharger nos vidéos préférées depuis YouTube.

```
from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("Une erreur s'est produite")
    print("Le téléchargement est terminé avec succès")

link = input("Entrez l'URL de la vidéo YouTube : ")
Download(link)
```

Vous utilisez la fonction `from pytube import YouTube` pour importer la bibliothèque Python Pytube avant de continuer avec les autres aspects. Ensuite, vous définissez la fonction de téléchargement du lien.

La commande `youtubeObject = youtubeObject.streams.get_highest_resolution()` téléchargera automatiquement la résolution la plus élevée disponible. Ensuite, j'ai implémenté Try et Except pour retourner un message d'erreur si le téléchargement échoue – sinon, il imprimera que le téléchargement est terminé avec succès.

La fonction Link demandera le lien de la vidéo YouTube préférée à télécharger, puis immédiatement après avoir appuyé sur le bouton Entrée, le téléchargement de la vidéo commencera.

### Le résultat :

![Image](https://paper-attachments.dropboxusercontent.com/s_2A6E5F7B9EF3D136021C2A8815B8956B830A35B9A863E60136A6FD8F4C45E374_1666119447422_pytube.PNG)

La vidéo que j'ai téléchargée a été un succès. Vous pouvez voir la vidéo dans le même dossier Python où se trouve le fichier sur lequel vous travaillez. Mais si vous le souhaitez, vous pouvez ensuite déplacer la vidéo vers votre emplacement de stockage préféré. Dans mon cas, le nom de la vidéo est "Ronaldo celebrates with Antony.mp4".

Cependant, il serait préférable d'avoir une connexion Internet fiable.

Cette bibliothèque possède également de nombreuses fonctionnalités sophistiquées, mais nous avons couvert toutes les principales. Vous pouvez en savoir plus sur la bibliothèque pytube en visitant sa [documentation officielle bien écrite](https://pytube.io/en/latest/).

## Conclusion

Nous avons réussi à créer notre propre script de téléchargement de vidéos YouTube en Python. Cela vous aide à éviter le stress de chercher un site web ou une application externe pour obtenir votre vidéo préférée sur votre stockage local.

Cela vous évite également d'avoir à exposer vos données sur un site web tiers ou un lien de phishing – tout cela au nom de l'obtention d'une vidéo de YouTube vers votre stockage local.

Espérons qu'après avoir parcouru cet article, vous comprendrez le processus nécessaire pour télécharger des vidéos depuis YouTube sans avoir besoin de télécharger une application externe ou de visiter un site web que vous ne connaissez pas.