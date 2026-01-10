---
title: Comment tirer parti des builds multi-étapes de Docker pour optimiser vos dockerfiles
  et images
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-28T09:49:14.000Z'
originalURL: https://freecodecamp.org/news/leveraging-docker-multi-stage-builds-to-optimize-dockerfile-image-1e708a591940
coverImage: https://cdn-media-1.freecodecamp.org/images/0*htBXuMZ5x0KT1gwv
tags:
- name: best practices
  slug: best-practices
- name: Docker
  slug: docker
- name: optimization
  slug: optimization
- name: Productivity
  slug: productivity
- name: 'tech '
  slug: tech
seo_title: Comment tirer parti des builds multi-étapes de Docker pour optimiser vos
  dockerfiles et images
seo_desc: 'By Kumar Rishav

  Multi-stage builds are a new feature requiring Docker 17.05 or higher on the daemon
  and client. They’re useful in building complex/multi step images while keeping them
  easy to read and maintain.

  Keeping the image size down is one of t...'
---

Par Kumar Rishav

Les builds multi-étapes sont une nouvelle fonctionnalité nécessitant Docker 17.05 ou supérieur sur le démon et le client. Elles sont utiles pour construire des images complexes/multi-étapes tout en les gardant faciles à lire et à maintenir.

Garder la taille de l'image réduite est l'une des tâches difficiles lors de la construction de l'image. Chaque instruction dans le Dockerfile ajoute une couche à l'image. De plus, vous devez vous souvenir de nettoyer les dépendances/artéfacts dont vous n'avez plus besoin. Auparavant, vous auriez pu utiliser des scripts shell pour garder les couches aussi légères que possible. Mais utiliser des astuces shell pour écrire un Dockerfile vraiment efficace est une tâche pénible.

### Que sont exactement les builds multi-étapes ?

En termes simples : vous pouvez utiliser le résultat final (par ex : fichier binaire/exécutable) d'une étape dans une autre étape sans vous soucier des dépendances utilisées pour construire ce binaire/fichier exécutable.

### Comment cela fonctionne-t-il ?

Avec les builds multi-étapes, vous pouvez avoir plusieurs instructions `FROM` dans un seul Dockerfile. Chaque instruction `FROM` contribue à une étape. La première étape commence par le numéro `0`.

```
FROM mhart/alpine-node:10  #étape 0
```

```
.......
```

```
FROM alpine:3.7 #étape 1
```

Ici, l'ordre des étapes compte car la première étape sera toujours `0`. Une autre façon est de donner un nom à l'`étape` en utilisant `AS`. Dans ce cas, vous n'avez pas à vous soucier de l'ordre.

```
FROM mhart/alpine-node:10 AS nodebuilder
```

```
.......
```

```
FROM alpine:3.7 AS builder
```

### Démonstration des builds multi-étapes

Infrastructure testée : [Play with Docker](https://labs.play-with-docker.com)

À des fins de démonstration, considérons une simple application nodejs et construisons un binaire à partir de celle-ci. Lorsque vous exécutez ce binaire, il appellera une [API NASA](https://api.nasa.gov/api.html) qui retourne des faits intéressants sur la date d'aujourd'hui.

#### Avant : images docker

![Image](https://cdn-media-1.freecodecamp.org/images/y9julNFQgoTabMcNhHLskgKl3tqEB7DAZW5w)
_avant:docker_images_

Actuellement, nous avons deux images que j'ai tirées de [dockerhub](https://hub.docker.com/) :

* `alpine (**~4Mo**)` - Version la plus légère du système d'exploitation linux
* `alpine-node (**~70Mo**)` - alpine + Node/Npm et autres dépendances.

#### Structure des fichiers

![Image](https://cdn-media-1.freecodecamp.org/images/V18qYpT2DGm6u5DqAqib6rbSEddTVX02k7KP)

`**Dockerfile**` **:**

* **À l'étape 0** (alias : `builder`), nous avons un OS `alpine-node` qui a `node` et `npm` intégrés. Sa taille est de `**~70Mo**`. Cette étape créera un binaire (nommé `nasa` : _Ligne 6_) dans le `WORKDIR` actuel, c'est-à-dire `app/`.
* **À l'étape 1**, nous avons l'OS `alpine`. Après cela, nous installons quelques dépendances nécessaires. À la _Ligne 14_, nous avons copié le binaire `nasa` de l'étape précédente (`builder`) vers l'étape actuelle. Ainsi, nous avons simplement copié le binaire et laissé derrière nous tout l'OS `alpine-node` lourd et d'autres dépendances comme `npm` ([gestionnaire de paquets node](https://www.npmjs.com/)) etc., car le binaire a déjà les dépendances requises (comme nodejs) intégrées.

`**app/**` **:**

* Ce n'est qu'une simple application node. Elle effectue un appel `https` et récupère des données en utilisant l'API NASA. Elle contient `index.js` et `package.json`. J'ai utilisé `[pkg](https://www.npmjs.com/package/pkg)` pour construire le binaire node. Voici le [code](https://gist.github.com/kumarrishav/36596fc94fe282d9e8dc26707fbdb7df) de l'application.

#### Après : images docker

![Image](https://cdn-media-1.freecodecamp.org/images/d0rZnHfp2mOtWo8w8biOGMozjv9OGIOtSPPG)
_après: docker images_

**multistage:1.0.0** (`56b102754f6d`) est l'image finale requise que nous avons construite. Sa taille est de `**~45Mo**`. **Presque 1/4** de l'image intermédiaire (`13bac50ebc1a`) construite à l'étape 0 et **presque la moitié** de l'image `alpine-node`.

Ainsi, ceci était un exemple simple pour montrer la fonctionnalité des builds multi-étapes. Pour les images ayant plusieurs étapes (comme 10-15 instructions FROM), vous trouverez cette fonctionnalité très utile.

#### Utiliser une image externe comme "étape"

Lorsque vous utilisez des builds multi-étapes, vous n'êtes pas limité à copier depuis les étapes que vous avez créées précédemment dans votre Dockerfile. Vous pouvez utiliser l'instruction `COPY --from` pour copier depuis une image séparée, soit en utilisant le nom de l'image locale, une balise disponible localement ou sur un registre Docker, ou un ID de balise.

`COPY --from=sampleapp:latest home/user/app/config.json app/config.json`

**Merci.**

_Merci à [Ajeet](https://twitter.com/ajeetsraina) pour la relecture du blog._

_Originalement publié sur [collabnix](http://collabnix.com/) : [https://lnkd.in/fJaC6gp](https://lnkd.in/fJaC6gp)._