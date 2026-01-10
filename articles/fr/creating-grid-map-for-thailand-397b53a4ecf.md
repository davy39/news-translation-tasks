---
title: Une méthode semi-automatique pour créer votre propre carte en grille
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-01-12T01:13:20.000Z'
originalURL: https://freecodecamp.org/news/creating-grid-map-for-thailand-397b53a4ecf
coverImage: https://cdn-media-1.freecodecamp.org/images/1*XFuuGyX5Ffi96DLWgupCtA.png
tags:
- name: D3
  slug: d3
- name: Data Science
  slug: data-science
- name: data visualization
  slug: data-visualization
- name: Design
  slug: design
- name: maps
  slug: maps
seo_title: Une méthode semi-automatique pour créer votre propre carte en grille
seo_desc: 'By Krist Wongsuphasawat

  In the past year, the grid map style visualization has gained a lot of popularity
  in the US [2,4]. It has a quite a few nice properties, which inspired me to create
  one for Thailand.

  The rest of this article will explain grid ...'
---

Par Krist Wongsuphasawat

Au cours de l'année passée, la visualisation de style carte en grille a gagné beaucoup en popularité aux États-Unis [2,4]. Elle possède plusieurs propriétés intéressantes, ce qui m'a inspiré à en créer une pour la Thaïlande.

Le reste de cet article expliquera les cartes en grille et comment j'ai créé la carte en grille pour la Thaïlande que vous voyez ci-dessus.

**Mais si vous êtes intéressé à utiliser la carte sans lire les détails de sa création, passez directement à mon dépôt GitHub [gridmap-layout-thailand](https://github.com/kristw/gridmap-layout-thailand).**

#### Qu'est-ce qu'une carte en grille et quelles sont ses propriétés ?

Dans une carte en grille, chaque région est représentée par une tuile de forme et de taille égales. Les tuiles sont placées pour s'adapter à une grille à des positions qui approximativement correspondent à la position géographique réelle. Si la tuile est un carré, la grille est rectangulaire. Si la tuile est un hexagone, alors la grille ressemble à un nid d'abeille. Voir les cartes des États-Unis ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/1*ge3DyNssY0xnjHtgn0-Urg.png)
_Cartes des États-Unis : (gauche) Carte en grille de tuiles hexagonales (centre) Carte en grille de tuiles carrées (droite) Carte géographique. Source : [NPR Blog](http://blog.apps.npr.org/2015/05/11/hex-tile-maps.html" rel="noopener" target="_blank" title=")_

La plupart des visualisations de cartes en grille sont des [_cartes choroplèthes_](https://en.wikipedia.org/wiki/Choropleth_map) qui utilisent des couleurs pour encoder des valeurs, telles que la quantité de précipitations, l'âge moyen de la population ou l'alignement politique. La création de cartes choroplèthes à partir de cartes géographiques présente certains inconvénients, car les différentes tailles de chaque région introduisent des biais lors de l'interprétation des résultats. De plus, de nombreuses petites régions sont souvent trop petites pour être remarquées sur une carte.

**Avantages :** Les cartes en grille n'introduisent pas de biais dus aux différentes tailles des régions, ce qui en fait un choix intéressant pour créer une carte choroplèthe. Les petites régions sont désormais garanties d'être assez grandes pour être vues. Elles sont également plus faciles à implémenter et plus rapides à charger qu'une carte géographique.

**Inconvénients :** Les positions des régions ne sont que des approximations et peuvent être inexactes. Par exemple, certaines régions adjacentes peuvent ne pas apparaître adjacentes sur la carte en grille. Elle déforme également la distance entre les régions.

#### Création d'une carte en grille pour la Thaïlande

Voici les exigences :

* La carte globale doit encore ressembler à la forme géographique de la Thaïlande. Les régions voisines doivent apparaître adjacentes ou proches.
* Utiliser des tuiles carrées pour faciliter la curation et l'application. Par exemple, cette carte peut être dessinée dans Excel [3] ou Google Sheets facilement.
* La carte ne doit pas avoir de trous au milieu pour éviter la confusion.

Bien sûr, l'approche la plus directe pour créer cette carte est de dessiner la carte manuellement à partir de zéro. Cependant, j'aimerais économiser de l'énergie avec une approche semi-automatique :

1. Pour chaque province, créer un rectangle centré sur son centroïde.
2. Utiliser une [simulation dirigée par force](https://github.com/mbostock/d3/wiki/Force-Layout) pour détecter les collisions entre les rectangles et supprimer les chevauchements. Chaque rectangle a son propre centre de gravité au centroïde de sa province ([disposition dirigée par force multi-foyers](http://bl.ocks.org/mbostock/1804919)). Les lignes solides dans la figure ci-dessous montrent les déplacements des rectangles par rapport à leurs positions idéales.
3. Aligner les rectangles sur une grille rectangulaire.
4. [Exporter les résultats de l'étape 3 sous forme de fichier CSV](https://gist.github.com/kristw/31be36fa0df6a85c1cbd) et les curer manuellement dans Google Sheets ou Excel. Le but de cette étape est de supprimer les espaces inutiles, de connecter la carte en un seul morceau contigu et d'ajuster les positions de certaines provinces.
5. Terminé ! La nouvelle carte ne nécessite que 40 % de l'espace original.

![Image](https://cdn-media-1.freecodecamp.org/images/1*BRBbGurtiCLcUhM1P5kJYQ.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*2D2Pm7z5jxVxTepAe1JAkA.png)

#### Utilisation

Les résultats de ce processus peuvent être utilisés sous forme de fichiers JS, CSV ou JSON. Veuillez consulter [gridmap-layout-thailand](https://github.com/kristw/gridmap-layout-thailand) sur GitHub pour les instructions. Le code que j'ai utilisé pour les étapes 1–5 ci-dessus se trouve également dans ce dépôt.

Enfin, cette méthode dépend encore beaucoup de la curation manuelle à la fin, ce qui peut ne pas produire la meilleure optimisation. Si vous avez des suggestions ou si vous souhaitez recommander une meilleure approche, la boîte de commentaires ci-dessous est à vous. :)

#### Références

[1] Mike Bostock. « [Multi-Foci Force Layout](http://bl.ocks.org/mbostock/1804919) » _bl.ocks.org_. Publié le 11 février 2012
[2] Danny DeBelius. « [Let’s Tesselate: Hexagons For Tile Grid Maps](http://blog.apps.npr.org/2015/05/11/hex-tile-maps.html) » _NPR Blog_. Publié le 11 mai 2015
[3] Caitlin Dempsey Morais. « [How to Make a Tile Grid Map Using Excel](http://www.gislounge.com/how-to-make-a-tile-grid-map-using-excel/) » _GIS Lounge_. Publié le 10 novembre 2015
[4] Nathan Yau. « [The Great Grid Map Debate of 2015](https://flowingdata.com/2015/05/12/the-great-grid-map-debate-of-2015/) » _Flowing Data_. Publié le 12 mai 2015