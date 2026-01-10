---
title: Comment changer la couleur des marqueurs Google Maps avec JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-19T13:16:56.000Z'
originalURL: https://freecodecamp.org/news/how-to-change-javascript-google-map-marker-color-8a72131d1207
coverImage: https://cdn-media-1.freecodecamp.org/images/1*d635FJj7G3ZEAZdyLUaeSg.png
tags:
- name: google maps
  slug: google-maps
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment changer la couleur des marqueurs Google Maps avec JavaScript
seo_desc: 'By Tan Le Tian

  Make them pink, blue, green, yellow or purple!


  By default, the Google Maps marker is red in color. This article will show how to
  add different color markers to Google Maps. So, let’s get started. ?

  1. Load Google Maps

  Create an HTML f...'
---

Par Tan Le Tian

#### Rendez-les roses, bleus, verts, jaunes ou violets !

![Image](https://cdn-media-1.freecodecamp.org/images/1*d635FJj7G3ZEAZdyLUaeSg.png)

Par défaut, le marqueur Google Maps est de couleur rouge. Cet article montrera comment ajouter des marqueurs de différentes couleurs à Google Maps. Alors, commençons. ?

### 1. Charger Google Maps

Créez un fichier HTML qui charge Google Maps en suivant [Google Maps API official docs: Hello World](https://developers.google.com/maps/documentation/javascript/tutorial).

Votre code ressemblera à quelque chose comme l'extrait de code ci-dessous.

**Note :** N'oubliez pas de changer `YOUR_API_KEY` par votre véritable clé API Google Maps.

### 2. Ajouter des marqueurs de différentes couleurs

Pour ajouter un marqueur de couleur bleue, nous devons changer l'icône du marqueur. Cela se fait en ajoutant une propriété d'icône et en spécifiant une URL pour celle-ci comme ci-dessous.

```
icon: {                               url: "http://maps.google.com/mapfiles/ms/icons/blue-dot.png"                           }
```

Notez que nous spécifions `blue-dot.png` à la fin de l'URL pour obtenir un marqueur bleu. Pour ajouter un marqueur vert, changez-le simplement en `green-dot.png` afin que l'URL soit `[http://maps.google.com/mapfiles/ms/icons/green-dot.png](http://maps.google.com/mapfiles/ms/icons/blue-dot.png)`.

Quelques autres couleurs disponibles :

1. rose : `pink-dot.png`
2. jaune : `yellow-dot.png`
3. violet : `purple-dot.png`

Pour obtenir l'URL de plus d'icônes de marqueurs, veuillez vous référer à [ce site web](https://sites.google.com/site/gmapsdevelopment/).

### 3. Encapsuler dans une fonction d'ajout de marqueur

Pour rendre le code plus propre, nous pouvons définir une fonction `addMarker` qui prend en entrée `latLng` et `color` du marqueur. Notez que nous stockons les marqueurs ajoutés dans un tableau global `markersArray` au cas où nous aurions besoin d'effectuer des opérations sur les marqueurs plus tard.

Ouvrez le fichier HTML dans le navigateur. Cela devrait ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*vkqPZHbgS4iz9zOtVKvf6g.png)

Vous pouvez obtenir la version finale complète du code [ici](https://gist.github.com/getsudocode/605bf60f5de40eb3f6b00addd93c913d). Faites-moi savoir comment cela se passe dans les commentaires ci-dessous.

N'hésitez pas à consulter un autre tutoriel Google Maps que j'ai écrit :
[Implémenter un clic sur JavaScript Google Map pour ajouter des marqueurs glissables avec une polyligne](https://medium.com/@letian1997/click-javascript-google-map-add-draggable-markers-polyline-b834dd5762b2)