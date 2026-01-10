---
title: Comment intégrer des vidéos et des audios dans votre HTML
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-23T16:35:11.000Z'
originalURL: https://freecodecamp.org/news/video-audio-in-html-a-short-guide-69f721878b47
coverImage: https://cdn-media-1.freecodecamp.org/images/1*jB3XGWVtrr8qOl21gCOAmQ.gif
tags:
- name: audio
  slug: audio
- name: HTML
  slug: html
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment intégrer des vidéos et des audios dans votre HTML
seo_desc: 'By Abhishek Jakhar

  HTML allows us to create standards-based video and audio players that don’t require
  the use of any plugins. Adding video and audio to a webpage is almost as easy as
  adding an image or formatting some text.

  There are two different w...'
---

Par Abhishek Jakhar

HTML nous permet de créer des lecteurs vidéo et audio basés sur des standards qui ne nécessitent pas l'utilisation de plugins. Ajouter des vidéos et des audios à une page web est presque aussi simple que d'ajouter une image ou de formater du texte.

Il existe deux façons différentes d'inclure des éléments vidéo. Nous allons discuter des deux ci-dessous.

#### Élément Vidéo

L'élément `<video>` nous permet d'intégrer des fichiers vidéo dans un HTML, de manière très similaire à l'intégration des images.

Les attributs que nous pouvons inclure sont :

* `src` Cet attribut représente la source, très similaire à l'attribut src utilisé dans l'élément image. Nous ajouterons le lien vers un fichier vidéo dans l'attribut src.
* `type` Cela sera video/mp4 car .mp4 est le format de la vidéo que nous utilisons. Nous pouvons également utiliser différents formats vidéo comme .ogg ou .webm, alors la valeur de l'attribut type changera en video/ogg ou video/webm respectivement.

> **Note :** certains formats vidéo courants sont WebM, Ogg, MP4.

![Image](https://cdn-media-1.freecodecamp.org/images/1*4epxHpB0Z94ZaNq64bL9WA.png)
_<video> dans une page web_

Nous avons maintenant cette vidéo sur notre page. Mais il y a un problème. Cette vidéo ne se lance pas automatiquement et il n'y a pas non plus de contrôles pour démarrer la vidéo. 
Nous devrons ajouter des contrôles manuellement en utilisant l'attribut `controls` à notre élément vidéo.

Cet attribut ne prend aucune valeur, car c'est un attribut booléen. Cela signifie qu'il peut être vrai ou faux.

Maintenant, en ayant l'attribut `controls` dans notre élément vidéo, cela signifie qu'il est vrai et qu'il affichera les contrôles de lecture.

![Image](https://cdn-media-1.freecodecamp.org/images/1*FKJojPyvDky1kM3gK5Z7KA.png)
_<video> + Contrôles_

Maintenant, si nous supprimons les contrôles, nous pourrions également faire en sorte que la vidéo se lance automatiquement, en utilisant l'attribut autoplay. C'est aussi un attribut booléen.

![Image](https://cdn-media-1.freecodecamp.org/images/1*TOOc_dxlcW6q7Cr3AUbxJQ.gif)
_Élément <video> + attribut autoplay (sans attribut controls)_

Maintenant, comme vous pouvez le voir, la vidéo se lance toute seule, et il n'y a pas de contrôle. Donc, nous n'avons pas réellement démarré la vidéo, mais nous ne pouvons pas non plus l'arrêter.

Nous pouvons également avoir des contrôles et une lecture automatique ensemble.

![Image](https://cdn-media-1.freecodecamp.org/images/1*jB3XGWVtrr8qOl21gCOAmQ.gif)
_Élément <video> avec attributs autoplay et controls_

Vous pouvez fournir différents attributs à l'élément vidéo, selon les besoins.

J'ai mentionné ci-dessus qu'il existe deux façons différentes d'ajouter l'élément vidéo. Essayons l'autre façon.

#### Élément Source

Auparavant, nous avons utilisé un élément vidéo avec une balise auto-fermante, mais ici nous allons fermer l'élément vidéo. Nous avons donc une balise d'ouverture et une balise de fermeture maintenant.

Nous allons également supprimer les attributs type et source de l'élément vidéo et les coller dans un autre élément.

```
<video>  <source src="http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerEscapes.mp4" type="video/mp4"></video>
```

Nous venons de déplacer les attributs vers l'élément source.

Maintenant, pourquoi voudrions-nous faire cela ?

Eh bien, dans la plupart des cas, avec la vidéo, nous aurons plusieurs sources car nous devons fournir différents types de fichiers selon le navigateur qui visualise votre vidéo, car différents navigateurs supportent différents types de fichiers.

![Image](https://cdn-media-1.freecodecamp.org/images/1*pHYI6GbxxHUL5A_FDTdK1A.png)

La vidéo aura exactement le même aspect. Mais maintenant nous avons un support plus large des navigateurs.

![Image](https://cdn-media-1.freecodecamp.org/images/1*P4pGSwzIVaFxWtT6tenhsA.png)
_Vidéo avec un support plus large des navigateurs (sans attributs)_

Maintenant, si nous voulons ajouter des attributs comme `controls`, `autoplay`, `loop`, etc., nous les ajouterons à l'élément `<video>`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ff1qRhcSQfqvHgcjbSrcsg.gif)
_Vidéo avec un support plus large des navigateurs et d'autres attributs_

#### Élément Audio

L'élément `<audio>` est très similaire à l'élément vidéo. Cependant, la seule différence majeure est qu'il n'y a pas de visuels.

Nous pouvons utiliser l'élément audio pour lire un fichier audio sur notre page web — comme un fichier mp3.

Maintenant, tout comme la balise vidéo, il existe deux façons différentes de procéder.

* Utiliser une seule balise représentant tout l'élément.
* Balise d'ouverture et de fermeture avec les éléments enfants entre les deux.

Maintenant, nous aurons une balise audio d'ouverture et de fermeture, puis nous ajouterons l'élément source entre les deux.

La structure du dossier pourrait ressembler à ceci :

```
|-- projet    |-- audio      |-- sample.mp3      |-- sample.ogg    |-- css      |-- main.css      |-- normalize.css    index.html
```

Il n'y a pas d'attribut controls donné à l'élément `<audio>` dans l'exemple ci-dessus, donc l'élément `<audio>` n'apparaîtra pas dans le document HTML.

Maintenant, vous pouvez voir qu'il y a seulement quelques différences clés ici. La valeur dans l'attribut `type` est changée de « video/mp4 » à « audio/mp3 ». Dans l'attribut `src`, nous avons changé d'un fichier vidéo avec l'extension .mp4 à un fichier audio avec l'extension .mp3.

Maintenant, tout comme l'élément vidéo, nous ne pourrons pas réellement arrêter ou démarrer l'audio sans aucun contrôle. Nous ajouterons donc l'attribut `controls` à l'élément audio.

![Image](https://cdn-media-1.freecodecamp.org/images/1*_d_AaBpz1QWH8csBB_-m8w.gif)
_Élément audio(<audio></audio>) avec plusieurs sources pour un support plus large des navigateurs_

Vous pouvez également ajouter d'autres attributs dans l'élément `<audio>` comme autoplay, loop, etc.

Nous avons couvert les essentiels des éléments audio et vidéo en HTML.

Vous pouvez en apprendre davantage sur l'audio et la vidéo dans les liens ci-dessous :

* [MDN Web docs — Vidéo](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video)
* [MDN Web docs — Audio](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/audio)

J'espère que vous avez trouvé cet article informatif et utile. J'adorerais avoir votre retour !

Merci pour votre lecture !