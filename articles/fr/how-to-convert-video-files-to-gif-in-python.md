---
title: Comment convertir des fichiers vidéo en GIF en Python
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-03-31T16:06:08.000Z'
originalURL: https://freecodecamp.org/news/how-to-convert-video-files-to-gif-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/convert.png
tags:
- name: gif
  slug: gif
- name: Python
  slug: python
- name: video
  slug: video
seo_title: Comment convertir des fichiers vidéo en GIF en Python
seo_desc: 'Recently, I was able to convert some video files to a gif as I needed them
  in gif format for some of my articles.

  I decided to show you how I did it in 3 lines of code, so you can save yourself
  the extra effort of looking up a Saas to do it for you.

  ...'
---

Récemment, j'ai pu convertir quelques fichiers vidéo en GIF car j'en avais besoin au format GIF pour certains de mes articles.

J'ai décidé de vous montrer comment je l'ai fait en 3 lignes de code, afin que vous puissiez vous épargner l'effort supplémentaire de chercher un SaaS pour le faire à votre place.

## Comment convertir une vidéo en GIF en Python

Pour convertir une vidéo en GIF en Python, vous devez installer un package appelé `moviepy` avec pip en ouvrant votre terminal et en exécutant `pip install moviepy`.

Ce module possède plusieurs méthodes avec lesquelles vous pouvez éditer et améliorer des vidéos.
![ss1-3](https://www.freecodecamp.org/news/content/images/2022/03/ss1-3.png)

Après avoir installé `moviepy` avec succès, vous devez importer une méthode appelée `VideoFileClip`. C'est la méthode avec laquelle vous pourrez spécifier le nom du fichier vidéo et son chemin relatif.

```py
from moviepy.editor import VideoFileClip
```

La chose suivante que vous devez faire est de spécifier le chemin relatif de la vidéo que vous souhaitez convertir en GIF à l'intérieur de la méthode VideoFileClip. Ensuite, vous devez l'assigner à une variable. 

Dans l'extrait de code ci-dessous, j'appelle cette variable `videoClip` :

```py
videoClip = VideoFileClip("my-life.mp4")
```

Pour enfin convertir la vidéo en GIF, vous devez utiliser la variable `videoClip` et appliquer la méthode `write_gif()` sur celle-ci, puis spécifier le nom que vous voulez donner au GIF à l'intérieur.
```py
videoClip.write_gif("my-life.gif")
```
Ouvrez le terminal et exécutez le fichier :
![ss2-1](https://www.freecodecamp.org/news/content/images/2022/03/ss2-1.png)

Vérifiez le dossier dans lequel se trouve le fichier vidéo et vous devriez voir le fichier GIF. Si vous utilisez VS Code, ouvrez la barre latérale en appuyant sur `CTRL + B` et vous devriez voir le fichier GIF.
![ss3-1](https://www.freecodecamp.org/news/content/images/2022/03/ss3-1.png)

Vous pouvez également ouvrir le GIF avec VS Code.

L'ensemble du code qui a effectué la conversion ressemble à ceci :

```py
from moviepy.editor import VideoFileClip

videoClip = VideoFileClip("my-life.mp4")

videoClip.write_gif("my-life.gif")
```

Vous pouvez en apprendre plus sur le module `moviepy` sur [leur site officiel](https://zulko.github.io/moviepy/).

Si vous avez des questions, n'hésitez pas à me contacter sur [Twitter](https://twitter.com/Ksound22).

Merci de m'avoir lu.