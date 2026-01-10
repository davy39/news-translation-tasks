---
title: Shoebox — mon groupe virtuel dessiné et codé à la main
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-07-24T12:31:46.000Z'
originalURL: https://freecodecamp.org/news/shoebox-my-virtual-hand-drawn-hand-coded-live-band-454368d0e66f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*S5cb-FocP5-yPvK-UeEDIw.png
tags:
- name: Design
  slug: design
- name: music
  slug: music
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Shoebox — mon groupe virtuel dessiné et codé à la main
seo_desc: 'By Michael Forrest

  I wrote this song and then made this realtime animation engine for “virtual live
  performances” so my song could be played by some funny stylized characters. I hand-coded
  and hand-drew just about every element during this 12 month p...'
---

Par Michael Forrest

J'ai écrit cette chanson puis créé ce moteur d'animation en temps réel pour des "performances live virtuelles" afin que ma chanson puisse être jouée par des personnages stylisés et amusants. J'ai presque tout dessiné et codé à la main durant ce projet de 12 mois. La vidéo ci-dessus est le premier rendu des résultats, mais j'ai conçu le système pour que différentes chansons et animations puissent être utilisées sans trop de difficulté. C'est principalement du CoffeeScript et three.js.

### **Recherche + disposition de la scène**

J'ai d'abord regardé quelques performances live sur YouTube pour voir comment elles étaient éclairées et filmées.

![Image](https://cdn-media-1.freecodecamp.org/images/1*8aNzsnACoNyi3bCsvThYcw.png)
_Recherche vidéo_

J'ai écouté toutes les chansons de mon album (pas encore sorti) pour déterminer quels instruments seraient nécessaires si un groupe les jouait, et j'ai disposé une scène avec quatre zones — un chanteur (moi), un batteur, un bassiste et un synthétiseur/clavier. Il y avait un orgue à l'arrière.

![Image](https://cdn-media-1.freecodecamp.org/images/1*VkfdTnExo6lu1n45LUgBLw.png)
_Disposition pour une grande scène_

Cette scène m'a semblé un peu trop grande, alors j'ai décidé d'en faire une plus petite pour mes premières vidéos.

![Image](https://cdn-media-1.freecodecamp.org/images/1*bmPni-NyAYk-J7YwcmWO_A.png)
_Scène de moitié plus petite_

### **Modélisation des instruments**

J'ai défini la plupart de mes modèles comme une seule feuille pliée avec deux "joues" transparentes de chaque côté.

![Image](https://cdn-media-1.freecodecamp.org/images/1*S5cb-FocP5-yPvK-UeEDIw.png)

Cela signifiait que je pouvais décrire un instrument avec une petite quantité de code.

Je voulais que ces instruments soient imprimables, alors j'ai créé des illustrations vectorielles détaillées pour chaque instrument. Voici un gros plan de l'illustration du synthétiseur modulaire.

![Image](https://cdn-media-1.freecodecamp.org/images/1*i28nBW1y0TWZGP_bdPuOYQ.png)
_Photographie vs mon dessin sur grille de pixels_

Voici une guitare.

![Image](https://cdn-media-1.freecodecamp.org/images/1*M3TSXRUq7222DZji07-awQ.png)
_Dessin de la guitare Moog_

Comme vous pouvez le voir, tout est dessiné et codé à la main. Je ne m'amuse pas avec des fichiers .dae ou des formats binaires (à part les images…).

Toutes ces textures ont été placées dans un grand atlas de textures fait à la main.

![Image](https://cdn-media-1.freecodecamp.org/images/1*6AcA504tgCh8uZzGGMQSOg.png)
_Atlas de textures pour tous les instruments créés — disposé à la main_

J'ai décrit le décalage de coordonnées pour chaque élément dans l'atlas et utilisé les mêmes données pour mapper les textures sur les modèles 3D.

### **Modélisation du groupe**

![Image](https://cdn-media-1.freecodecamp.org/images/1*JS5jWIVRKygRRmNICu1wYw.png)
_Michael Forrest cubee original par Ann Forrest_

Ma sœur m'a fait une petite découpure en carton il y a quelques années, alors je suis parti de son œuvre.

J'ai décidé de composer mon groupe de trois autres personnages : une grenouille aux synthés, un mandrill nommé Barry à la basse et une vache Minecraft à la batterie.

![Image](https://cdn-media-1.freecodecamp.org/images/1*0iLhCJtgMbqn3xLzv06z1Q.png)
_Dessin de Barry_

Je pense que les pieds de Barry m'ont donné le plus de fil à retordre.

![Image](https://cdn-media-1.freecodecamp.org/images/1*H3lEjLKAuNdnyccDquDg_A.png)
_Les pieds de Barry_

J'ai construit ces personnages avec un minimum de code spécifiant leur disposition — ce ne sont que des primitives de boîte, vraiment.

J'ai ajouté les couches de visage ensuite — notez les zones transparentes au-dessus et en dessous pour permettre les barbes saillantes et autres.

![Image](https://cdn-media-1.freecodecamp.org/images/1*KBGK-qLix4E7TquhB9HZTA.png)

Les quatre textures des membres du groupe sont dans un atlas et la seule différence entre chaque membre est son décalage vertical dans l'atlas.

![Image](https://cdn-media-1.freecodecamp.org/images/1*U9sPXKjmiU4gMcDN8eDn2A.png)
_Atlas de textures pour les membres du groupe_

### **Lumières**

Pour créer un spectacle de scène captivant, j'ai d'abord dû apprendre à éclairer une scène. J'ai fait quelques recherches et choisi un style et des couleurs.

![Image](https://cdn-media-1.freecodecamp.org/images/1*VfvzqoGmXjJCbW856YlrZg.png)
_Recherche sur l'éclairage et schéma de couleurs choisi_

![Image](https://cdn-media-1.freecodecamp.org/images/1*u12YKUOFFk-ObcGMA9CPCQ.png)

J'ai modélisé les enceintes d'éclairage et les grilages. Ce n'était pas trop de travail lorsque je l'ai basé sur une primitive de tour.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Qcyl9czyriDxt2G9BrCZOw.png)
_Modèle de projecteur_

### **Planification d'une chanson**

J'avais besoin de planifier la structure d'une chanson pour définir tous les mouvements de caméra, l'éclairage et les animations que je voulais.

![Image](https://cdn-media-1.freecodecamp.org/images/1*aZhjbDvhlO6qhUgO8qDTKQ.png)

J'ai écrit des scripts pour convertir les données de cette feuille de calcul en quelque chose que je pouvais utiliser dans le code. Voici le fichier de données final pour l'arrangement. Il n'y a pas grand-chose à cela, compte tenu de la quantité de travail qu'il effectue.

Cela représente essentiellement toutes les données nécessaires pour rendre une performance d'une chanson.

### **Animation du groupe**

Je voulais des données minimales mais des mouvements naturels. Je pensais avoir besoin d'un outil multi-touch pour capturer les animations, mais une fois que j'ai commencé à les définir, j'ai réalisé que je pouvais poser chaque partie individuellement pour rassembler les animations étape par étape. Voici une vidéo de moi démontrant rapidement mon outil d'animation.

J'ai sauvegardé ces animations dans une base de données et généré un fichier JSON qui pouvait être référencé par le code front-end.

**Contrôleurs**

Il y a trois contrôleurs principaux responsables d'une performance — Caméra, Animation et Éclairage.

Le contrôleur de caméra interprète les différents types de "plans" en coordonnées spatiales et anime la caméra en fonction des informations minimales fournies.

Par exemple, voici comment un mouvement de caméra "orbite" est décrit.

Nous commençons donc à la `mesure 69`, et sur une durée de `8 mesures`, nous orbitons de l'`avant-gauche` de `michael` à `avant/droite/au-dessus`, en restant à `1000` unités de distance. (J'ai choisi mes unités en fonction des mesures en pixels pour faciliter certaines choses, mais avec le recul, il aurait été préférable d'utiliser des mètres).

Le contrôleur d'éclairage avait une "piste" pour chaque lumière (ou regroupement logique de lumières), puis chacune de celles-ci était définie séparément dans le fichier de configuration. Voici à quoi ressemblait la configuration pour la lumière de fond — je voulais simplement définir les numéros de mesure et les couleurs ou transitions de couleurs.

Mon outil d'animation m'a permis de créer des boucles d'animation nommées. Je les ai référencées dans mon fichier de configuration par leur nom, puis je les ai utilisées pour choisir la bonne animation pour chaque personnage pendant la chanson.

Voici les animations de Barry pour toute la chanson :

Prenons le deuxième élément comme exemple, nous utilisons l'animation nommée "barry chorus" pour 16 mesures à partir de la mesure 25. Nous spécifions qu'il tiendra la `bassGuitar` pour ces animations. Être joué par quelqu'un est une fonction de l'instrument, donc la guitare sait où elle doit se déplacer pour être jouée par Barry.

### **Shaders GL**

Je voulais que la vidéo ait une bonne cinématographie et l'effet de caméra le plus important pour moi était d'avoir des effets de profondeur de champ dans le plan (c'est-à-dire que les choses à l'arrière-plan et au premier plan doivent être floues).

Mes shaders sont assez bricolés, mais l'idée générale est que nous générons d'abord une carte de profondeur pour savoir à quelle distance chaque élément de la scène se trouve de la caméra. Ensuite, nous utilisons ces informations pour flouter les zones de l'image en conséquence.

![Image](https://cdn-media-1.freecodecamp.org/images/1*DJRVE7igIxRhx7AtUi9P_A.png)
_Voyez comme le public est flou_

L'autre effet important était l'éclairage volumétrique. Les lumières devaient sembler traverser de la fumée pour donner l'impression d'un concert. Voici l'étendue approximative de la technologie des shaders dans ma scène. (Les noms sont un peu décalés — et notez que j'ai fini avec plusieurs "faux soleils" pour que chaque lumière ait le sien).

![Image](https://cdn-media-1.freecodecamp.org/images/1*zz46sUg3WQuezA2JLIqYMw.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*YBs4SdyUlyKfZfyJldEIpA.png)
_Effets d'éclairage volumétrique_

### **Le public**

J'avais initialement créé un système où mes followers Twitch seraient mon public (avec détection faciale pour placer leurs visages sur des corps), mais cela ne semblait pas tout à fait adapté pour une vidéo YouTube. Je suis donc allé sur Cubeecraft.com, l'inspiration originale de ce style. J'ai choisi tout ce qui résonnait pour moi, y compris des personnages de Spencer et Watchmen. Ceux-ci sont tous faits à la main, alors je les ai filtrés pour ne garder que ceux avec des dispositions similaires et j'ai découvert que je pouvais copier et coller des tranches entre les personnages dans Sketch pour générer rapidement des fichiers.

J'ai utilisé TexturePacker pour générer les textures. J'aurais probablement pu me faire gagner beaucoup de temps plus tôt en faisant de même au lieu de coder à la main chaque mapping de vertex.

![Image](https://cdn-media-1.freecodecamp.org/images/1*MnbSLPg1lWfTQQ9iFpIy_w.png)
_définition des tranches pour chaque modèle_

![Image](https://cdn-media-1.freecodecamp.org/images/1*02QR1OH13Qd6eW1ao4cfxw.png)
_Atlas de textures pour tous les personnages cubeecraft_

### **Rendu**

J'ai utilisé quelques outils et j'ai opté pour CCapture pour faire des rendus 4K (non temps réel) — cela a pris environ une demi-heure pour rendre la vidéo finale. J'ai resynchronisé cela avec l'audio dans Apple Motion et utilisé Final Cut Pro pour ajouter l'intro et le générique de fin.

### **Le résultat (encore)**

### **Fonctionnalités au-delà de la démonstration vidéo**

Ce rendu vidéo n'est qu'une sortie possible. J'ai rendu une vidéo à 360 degrés (bien que je l'aie bâclée et n'aie pas réussi à faire fonctionner l'éclairage volumétrique, donc elle ne semble pas tout à fait correcte).

J'ai ce projet hébergé sur un serveur, mais je ne suis pas tout à fait prêt à le publier jusqu'à ce que je trouve un bon moyen de le rendre interactif. Je peux brancher mes performances en temps réel pour qu'elles se synchronisent avec mes spectacles live semi-improvisés. Il fonctionne sur mon iPhone, donc il est compatible avec les casques de type Google Cardboard.

J'ai modélisé d'autres instruments au-delà de ceux que vous voyez ici et j'ai beaucoup de choses réactives au son que je n'ai pas encore montrées (ce qui, incroyablement, semble aussi fonctionner sur mobile). L'une des choses les plus difficiles à faire a été de garder le scope sous contrôle alors que je réalisais de plus en plus de possibilités pour ce système.

### **Des questions ?**

J'ai vraiment survolé cette explication — je voulais commencer par souligner les éléments majeurs avant d'entrer dans plus de détails sur chaque chose.

Qu'aimeriez-vous entendre davantage ? Je prévois d'approfondir dans une série de vidéos à l'avenir, donc il serait bon de comprendre ce que les gens veulent apprendre.

Si vous êtes inspiré par le potentiel de ce projet en tant que produit. Personnellement, je peux l'imaginer comme un type de médium de publication musicale accessible, situé quelque part entre les enregistrements et les spectacles live, surtout si vous le branchez sur des services comme Twitch.

### **Aimé la chanson ?**

Si vous avez aimé la musique, venez me trouver sur [Facebook](http://facebook.com/michael.forrest.music), [Twitter](http://twitter.com/mf_music) et/ou [SoundCloud](http://soundcloud.com/michaelforrest).