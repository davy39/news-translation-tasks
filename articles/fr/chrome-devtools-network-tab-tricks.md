---
title: 'Chrome DevTools : Comment filtrer les requêtes réseau'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-02T21:26:48.000Z'
originalURL: https://freecodecamp.org/news/chrome-devtools-network-tab-tricks
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a87740569d1a4ca2629.jpg
tags:
- name: browser
  slug: browser
- name: Google Chrome
  slug: chrome
- name: tips
  slug: tips
seo_title: 'Chrome DevTools : Comment filtrer les requêtes réseau'
seo_desc: "By Adeel Imran\nAs front end developers, most of our time is spent in the\
  \ browser with DevTools open (almost always, unless we are watching YouTube ...\
  \ sometimes even then). \nOne of the major sections in DevTools is the network tab.\
  \ There are a couple..."
---

Par Adeel Imran

En tant que développeurs front-end, la plupart de notre temps est passé dans le navigateur avec DevTools ouvert (presque toujours, sauf si nous regardons YouTube ... parfois même alors). 

L'une des principales sections de DevTools est l'onglet `network`. Il y a plusieurs choses que vous pouvez faire dans l'onglet `network`, comme les suivantes :

* Trouver des requêtes réseau par texte
* Trouver des requêtes réseau par expression regex
* Filtrer (exclure) les requêtes réseau
* Utiliser le filtre de propriété pour voir les requêtes réseau par un certain domaine
* Trouver des requêtes réseau par type de ressource

Pour les besoins de ce tutoriel, j'utilise la page d'accueil de [freeCodeCamp](https://www.freecodecamp.org/news/), **[freecodecamp.org/news](https://www.freecodecamp.org/news/)**. Il suffit d'aller sur la page et d'ouvrir l'onglet `network`.

Vous pouvez voir l'onglet `network` en appuyant sur `cmd + opt + j` sur votre Mac ou `ctrl + shift + j` sous Windows. Cela ouvrira par défaut l'onglet `console` dans DevTools.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-02-at-22.18.37.png)
_Cliquer sur "cmd + opt + j" ouvre le panneau de la console dans DevTools_

Une fois l'onglet `console` ouvert, cliquez simplement sur l'onglet `network` pour le rendre visible.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-02-at-22.19.57.png)
_Cliquer sur l'onglet "network" vous montrera toutes les requêtes réseau effectuées pour une certaine page_

Une fois l'onglet `network` ouvert, nous pouvons commencer notre tutoriel.

## Commençons

Assurez-vous que la page correcte est ouverte ([freecodecamp.org/news](https://www.freecodecamp.org/news/)) et que le panneau de l'onglet "network" est ouvert dans DevTools :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-02-at-23.12.01.png)
_Illustration de l'emplacement de la barre de filtre dans le panneau réseau._

* La boîte verte ici illustre l'icône qui peut masquer/afficher la zone de filtre dans l'onglet du panneau réseau.
* La boîte rouge ici illustre la zone de filtre. Avec cette boîte, nous pouvons filtrer les requêtes réseau.

### Trouver une requête réseau par texte

Tapez `analytics` dans la zone de texte du filtre. Seuls les fichiers contenant le texte `analytics` sont affichés.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-02-at-22.47.38.png)

### Trouver une requête réseau par expression regex

Tapez `/.*\min.[c]s+$/`. DevTools filtre toutes les ressources dont les noms de fichiers se terminent par `min.c` suivi d'un ou plusieurs caractères `s`.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-02-at-23.21.34.png)

### Filtrer (exclure) une requête réseau

Tapez `-min.js`. DevTools filtre tous les fichiers contenant `min.js`. Si un autre fichier correspond au motif, il sera également filtré et ne sera pas visible dans le panneau réseau.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-02-at-22.51.50.png)

### Utiliser le filtre de propriété pour voir les requêtes réseau par un certain domaine

Tapez `domain:code.jquery.com` dans la zone de filtre. Il n'affichera que les requêtes réseau appartenant à l'URL `code.jquery.com`.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-02-at-22.54.22.png)

### Trouver une requête réseau par type de ressource

Si vous souhaitez uniquement voir quel(s) fichier(s) de police est/sont utilisé(s) sur une certaine page, cliquez sur `Font` :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-02-at-23.03.41.png)
_Filtrer les requêtes réseau par les fichiers de type "font" uniquement_

Ou si vous souhaitez uniquement voir les fichiers web socket chargés sur une certaine page, cliquez sur `WS` :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-02-at-23.05.55.png)
_Filtrer les requêtes réseau par les fichiers de type "web socket" uniquement_

Vous pouvez également aller plus loin et afficher à la fois les fichiers `Font` et `WS` ensemble. Cliquez simplement sur `Font` en premier, puis `cmd` cliquez sur `WS` pour multi-sélectionner les onglets. (Si vous êtes sur une machine Windows, vous pouvez multi-sélectionner en utilisant `ctrl` clic).

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-02-at-23.08.48.png)
_Multi-sélection de plusieurs types de ressources par "cmd` clic sur les types_

---

C'est tout pour ce tutoriel. Si vous l'avez trouvé utile, partagez-le avec vos collègues et faites-moi savoir ce que vous en pensez également sur [**twitter.com/adeelibr**](https://twitter.com/adeelibr).