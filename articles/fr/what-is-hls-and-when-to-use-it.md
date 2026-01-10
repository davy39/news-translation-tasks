---
title: 'Streaming vidéo HLS : qu''est-ce que c''est et quand l''utiliser'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-18T22:59:12.000Z'
originalURL: https://freecodecamp.org/news/what-is-hls-and-when-to-use-it
coverImage: https://www.freecodecamp.org/news/content/images/2019/12/HLS-video.jpg
tags:
- name: Adaptive Bitrate
  slug: adaptive-bitrate
- name: hls
  slug: hls
- name: media
  slug: media
- name: video
  slug: video
- name: Video.js
  slug: video-js
- name: VideoJS
  slug: videojs
seo_title: 'Streaming vidéo HLS : qu''est-ce que c''est et quand l''utiliser'
seo_desc: 'By Anton Garcia Diaz

  In this short article I will focus on HLS, the most extended adaptive bitrate protocol
  for video delivery. I''ll answer some of the main questions that anyone considering
  HLS for the first time will likely ask: what it is, when to...'
---

Par Anton Garcia Diaz

Dans cet article court, je me concentrerai sur le HLS, le protocole de débit adaptatif le plus répandu pour la diffusion de vidéos. Je répondrai à certaines des principales questions que toute personne envisageant le HLS pour la première fois est susceptible de se poser : qu'est-ce que c'est, quand l'utiliser et comment l'utiliser. 

Pour vous aider en cours de route, je montrerai quelques exemples en utilisant [un outil de publication vidéo en ligne](https://abraia.me/video/) que vous pouvez utiliser librement pour tester les performances du HLS par vous-même.

## Qu'est-ce que le HLS et comment fonctionne-t-il ?

Le HLS est un protocole défini par Apple pour implémenter un format de streaming à débit adaptatif qui peut être pris en charge sur leurs appareils et logiciels. Avec le temps, il a gagné un soutien généralisé. 

La caractéristique la plus importante du HLS est sa capacité à adapter le débit binaire de la vidéo à la vitesse réelle de la connexion. Cela optimise la qualité de l'expérience. 

Les vidéos HLS sont encodées dans différentes versions à différentes résolutions et débits binaires. Cela est généralement appelé l'échelle de débit binaire. Lorsque la connexion devient plus lente, le protocole ajuste automatiquement le débit binaire demandé à la bande passante disponible. 

Comparé aux vidéos progressives, le HLS évite les effets de rebuffering et de blocage ainsi que la surcharge de la connexion client. Nous pouvons le voir en action dans cette vidéo.

%[https://store.abraia.me/05bf471cbb3f9fa9ed785718e6f60e28/HLS-video/HLS_video-at-work/index.html]

En essence, le HLS offre une bien meilleure expérience utilisateur lorsque nous utilisons du contenu vidéo dans nos applications ou sites.

Il est pris en charge nativement sur iOS et Android. Il est également pris en charge par Safari, et en utilisant un peu de JavaScript, il est pris en charge dans tous les principaux navigateurs (Chrome, Firefox, Edge). Bien que l'utilisation du HLS nécessite un certain effort, ce n'est pas un gros problème. 

Voyons quand nous devrions l'utiliser et comment.

## Quand devrions-nous utiliser le HLS ?

Il existe des cas où les vidéos ne sont pas si lourdes. Par exemple, vous pourriez avoir une séquence d'images encodée en une vidéo de 1 à 2 secondes, avec un poids inférieur à 1 Mo. Dans ce cas, une vidéo progressive – qui peut être consommée, comme une image, en utilisant du HTML5 simple – est certainement la meilleure option. Le HLS n'offre aucun avantage ici.

Mais le HLS a du sens lorsque nous voulons diffuser des vidéos en haute résolution (HD ou plus) avec un poids supérieur à 3 Mo. Ce type de contenu peut ruiner notre UX web lorsqu'il est visionné sur une connexion mobile moyenne. 

Il est intéressant de noter que c'est le cas pour une quantité croissante de contenu multimédia, y compris de nombreuses vidéos courtes de moins de 20 secondes utilisées dans les contextes de commerce électronique et de marketing. Dans l'exemple au début de l'article, nous avons une vidéo Full HD de seulement 9 secondes qui pèse plus de 6 Mo.

## Comment pouvons-nous utiliser le HLS sur nos sites ?

Pour utiliser le HLS, nous devons aborder un certain nombre d'aspects. Je me concentrerai sur deux points importants : 

* la nécessité d'encoder la vidéo, et,
* la nécessité de l'intégrer dans notre page. 

Pour une vue plus complète de ce qu'implique une pipeline de publication vidéo générale, vous pouvez consulter [cet article](https://www.freecodecamp.org/news/short-videos-in-web-and-ecommerce-workflows/).

### Encodage HLS

Nous pouvons encoder des vidéos en HLS en interne ou en utilisant un service tiers. Pour construire un encodeur en interne, la meilleure option est d'utiliser FFMPEG, une puissante bibliothèque open source pour le traitement et l'encodage vidéo. Dans ce cas, nous devons analyser le contenu que nous allons encoder et définir un certain nombre de paramètres. 

Dans le HLS, nous devons définir une échelle de débit binaire (les débits binaires et les résolutions de chaque étape) et la longueur des chunks. Lorsque nous encodons une vidéo, nous obtenons un ensemble de listes de lecture et de chunks. Typiquement, nous terminons les premières avec l'extension .m3u8 et les secondes avec l'extension .ts. Nous pouvons voir un exemple dans l'image suivante.

![Image](https://www.freecodecamp.org/news/content/images/2019/12/imaxe.png)

Nous pouvons voir une liste de lecture principale, une liste de lecture supplémentaire par version, et tous les chunks de chaque version. La liste de lecture principale spécifie l'échelle de débit binaire et le chemin relatif vers chaque version.

Apple fait une recommandation générique spécifiant l'échelle de débit binaire et une durée de chunk de 10 secondes. Cependant, cela n'est pas très utile pour de nombreux types de contenu, comme les vidéos courtes courantes dans le commerce électronique et le marketing. 

En fait, la meilleure approche est d'ajuster l'échelle de débit binaire spécifiquement au contenu de la vidéo. Dans ce cas, si vous voulez tirer le meilleur parti du HLS et que vous n'êtes pas expert en encodage, un service tiers fournissant un encodage par titre (avec HLS) est probablement le bon choix.

## Lecteurs HLS

Ici, nous trouvons deux options principales. Nous pouvons nous en tenir au lecteur HTML5 ou nous pouvons utiliser un lecteur implémenté en JavaScript.

### Lecteur HTML5 

Les versions récentes de Safari prennent en charge le HLS. Dans ce cas, vous pouvez utiliser les listes de lecture HLS de la même manière que les vidéos progressives. Avec d'autres navigateurs, vous pouvez utiliser une petite bibliothèque JavaScript pour implémenter le protocole HLS et utiliser à nouveau le lecteur HTML5 pour les vidéos progressives. 

Cela peut être fait avec HLS.js. Cette bibliothèque implémente simplement la négociation des versions, en fonction de la bande passante disponible. Le support est presque universel, conditionné uniquement par le support de l'API des éléments multimédias.

### Lecteur JavaScript

Dans le cas où nous devons personnaliser l'expérience vidéo – ce qui est assez courant dans les pages de marketing et de stories –, alors nous devons utiliser autre chose que le lecteur HTML5 par défaut. 

Bien qu'il existe de nombreuses options commerciales, Video.js est un bon choix. C'est un lecteur open source qui prend en charge un haut degré de personnalisation, y compris différents skins et contrôles. 

Un lecteur comme Video.js prend également en charge le suivi des événements liés à la vidéo (comme les actions de lecture ou de pause) afin que nous puissions les inclure dans nos propres analyses. En fait, inclure ces données dans notre Google Analytics est vraiment facile.

![Image](https://www.freecodecamp.org/news/content/images/2019/12/imaxe-2.png)
_Données GA pour les événements suivis dans une vidéo visionnée avec un lecteur Video.js_

## Résumé

J'ai abordé les premières questions sur le HLS que la plupart des utilisateurs potentiels auront : qu'est-ce que c'est et quand nous devrions l'utiliser.

Bien qu'une pipeline de publication vidéo basée sur le HLS puisse être implémentée et déployée en interne avec des outils open source comme FFMPEG et video.js, il peut être judicieux d'utiliser un [service de publication vidéo](https://abraia.me/video/) si vous n'êtes pas un expert en technologie. Ils apportent des fonctionnalités avancées comme l'encodage par titre, prennent en charge tout le travail difficile et nous permettent de nous concentrer sur nos besoins de personnalisation.