---
title: Comment créer une application de cartographie en React facilement avec Leaflet
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2019-10-30T14:45:00.000Z'
originalURL: https://freecodecamp.org/news/easily-spin-up-a-mapping-app-in-react-with-leaflet
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/mapping-with-leaflet.jpg
tags:
- name: Gatsby
  slug: gatsby
- name: GatsbyJS
  slug: gatsbyjs
- name: JavaScript
  slug: javascript
- name: leaflet
  slug: leaflet
- name: Mapping
  slug: mapping
- name: maps
  slug: maps
- name: React
  slug: react
- name: react-leaflet
  slug: react-leaflet
- name: React
  slug: reactjs
seo_title: Comment créer une application de cartographie en React facilement avec
  Leaflet
seo_desc: 'Mapping is hard, but spinning up a new app that renders maps doesn’t have
  to be. Here’s how you can easily get started working with maps in a new React app.

  Not that AAA map under your car seat

  Maps have been around for thousands of years, but they’v...'
---

La cartographie est difficile, mais lancer une nouvelle application qui affiche des cartes n'a pas à l'être. Voici comment vous pouvez facilement commencer à travailler avec des cartes dans une nouvelle application React.

# Pas cette carte AAA sous votre siège de voiture

Les cartes existent depuis des milliers d'années, mais elles sont devenues plus complexes et puissantes au cours des dernières décennies, simplement parce que les ordinateurs existent. Cela a permis la création de produits que nous utilisons tous les jours - comme Google Maps qui nous aide à rentrer du travail et à éviter les embouteillages, ou les cartes météo qui nous permettent de vérifier les images radar en temps réel. En allant plus loin, les scientifiques utilisent des cartes tous les jours avec des données d'imagerie satellite pour essayer de mieux comprendre notre humble planète.

Cela semble difficile...

# Construction de cartes

Rebondissement, ce n'est pas difficile !

![Image](https://www.freecodecamp.org/news/content/images/2019/10/plot-twist.gif)
_Final Space — Quel rebondissement !_

Au moins, ce n'est pas difficile de commencer. Heureusement, les parties les plus difficiles sont déjà intégrées dans des bibliothèques qui peuvent facilement être utilisées avec JavaScript.

Entrez Leaflet...

# Bibliothèques de cartographie

Il existe quelques bibliothèques dans le domaine de la cartographie en ce moment (comme [OpenLayers](https://openlayers.org/)), mais nous aimons [Leaflet](https://leafletjs.com/).

Pour commencer avec Leaflet, incluez d'abord les ressources de la bibliothèque sur votre page. Ensuite, montez l'application sur un élément racine dans le DOM avec quelques paramètres de base. Vous pouvez un peu penser à cela comme la façon dont React se monte sur un nœud DOM, mais Leaflet lui-même n'utilise pas React. Une fois initialisé, Leaflet vous permet de commencer à utiliser son API pour projeter une carte de base, ajouter des couches, des tuiles sur ces couches, et même commencer à dessiner dessus.

### Carte de base ? Couches ? Tuiles ?

Pour comprendre l'idée de base, pensez à un gâteau. Traditionnellement, les gâteaux ont différentes couches, certaines en bas, certaines en haut, certaines peuvent simplement couvrir un côté avec du glaçage. Vos couches de carte fonctionnent de manière similaire. La couche du bas, qui est votre fondation, sera votre « carte de base ». Ci-dessous, nous voyons un instantané des incendies de forêt du Camp Fire en Californie en 2018 sur l'imagerie satellite [MODIS Aqua](https://terra.nasa.gov/about/terra-instruments/modis) de la NASA.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/modis-aqua-campfire-california-wildfires-1024x535.jpg)
_MODIS Aqua – Incendies de forêt « Campfire » en Californie_

Maintenant, pour obtenir une carte de base, nous avons besoin de l'imagerie pour la produire, c'est là que les tuiles entrent en jeu. Une tuile est un bloc d'image unique qui constitue votre groupe de tuiles représentant votre couche.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/modis-aqua-tms-tile-diagram-1024x535.jpg)
_Tuile unique MODIS Aqua et schéma URI – [Lien de la tuile](https://gibs-a.earthdata.nasa.gov/wmts/epsg3857/best/MODIS_Aqua_CorrectedReflectance_TrueColor/default/2018-11-08/EPSG3857_250m/8/97/41.jpg)_

Vos tuiles ne sont vraiment qu'une simple image, mais aux côtés des autres, coordonnées par des positions géographiques et des niveaux de zoom, constituent ce que vous voyez lorsque vous regardez une carte web comme la carte de base montrée ci-dessus. L'objectif d'inclure ces petites pièces individuelles plutôt qu'une énorme image est que, entre le traitement de l'ensemble du globe, les différents niveaux de zoom disponibles et les résolutions disponibles au-delà de cela, nous parlons de gigaoctets de ressources d'images qui ne seraient tout simplement pas fiables ou réalistes à servir en entier.

Une fois que vous avez établi votre carte de base, vous pouvez ensuite superposer des couches supplémentaires en utilisant plus d'imagerie, des tuiles vectorielles ou des points de données qui se transforment en couches. Dans la capture d'écran ci-dessous, nous avons zoomé au-delà de la résolution la plus élevée de notre carte de base. Remarquez cependant que l'imagerie de gauche est une tuile de superposition individuelle de [Digital Globe](http://blog.digitalglobe.com/news/open-data-response-for-the-california-wildfires/) qui nous fournit une résolution plus élevée d'une partie de la zone entourant la zone de feu.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/modis-aqua-with-digital-globe-tile-1024x535.jpg)
_MODIS Aqua avec tuile de superposition de Digital Globe_

Un autre exemple par-dessus cela est l'ajout de points représentant des incendies collectés à partir de l'imagerie [VIIRS](https://earthdata.nasa.gov/earth-observation-data/near-real-time/download-nrt-data/viirs-nrt) de la NASA.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/modis-aqua-with-viirs-fire-data-1024x535.jpg)
_MODIS Aqua avec couche de points de données d'incendie VIIRS_

Cela nous permet d'avoir le contexte de la carte de base ainsi que la possibilité de projeter tout type de données que nous aimerions pour mieux comprendre ses effets.

En plus des données VIIRS, il existe de nombreuses sources d'imagerie, de tuiles vectorielles et de jeux de données publiés par des gouvernements et des municipalités que vous pouvez utiliser pour aider à construire des cartes et des visualisations de données intéressantes. La NASA est une bonne source de ces types de ressources, mais de nombreux fournisseurs commerciaux publient [un accès ouvert aux jeux de données sur les catastrophes](https://www.digitalglobe.com/ecosystem/open-data) qui aident les autres à construire des solutions autour des efforts de secours.

### Qu'en est-il de dessiner des trucs ?

Habituellement, lorsque les gens utilisent des cartes, ils veulent regarder des points d'intérêt. Le dessin nous donne la possibilité de cadrer ces zones d'intérêt avec différents outils de dessin tels que la création d'un rectangle à l'aide d'un outil de boîte de délimitation ou le dessin d'un cercle. Ce sont des formes simples, mais ces formes représentent un espace géographique qui peut ensuite être utilisé pour recueillir des données sur cette zone.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/bounding-box-alexadria-va-1024x535.jpg)
_Boîte de délimitation rectangulaire autour d'Alexandria, VA_

# React ❤️ Leaflet

Leaflet en soi vous donne beaucoup à travailler, mais il y a encore beaucoup d'efforts manuels qui l'accompagnent. Si vous êtes habitué à construire une application React, vous n'êtes probablement pas aussi habitué à construire une interface utilisateur entière en utilisant rien d'autre que des API basées sur la fenêtre du navigateur, et c'est là que [React Leaflet](https://react-leaflet.js.org/) brille.

React Leaflet est une bibliothèque React qui prend la construction de cartes et la regroupe en composants intuitifs qui représentent ces parties de la carte. Considérez ce qui précède, où nous avons parlé de votre carte de base et des couches qui l'accompagnent, vous pourriez la voir ressembler à quelque chose comme :

![Image](https://www.freecodecamp.org/news/content/images/2019/10/map-component-code.png)
_Code pseudo-composant de carte_

Bien que vous pourriez probablement vous attendre à ce que ce ne soit pas _aussi_ flexible que l'utilisation directe des API Leaflet, cela ouvre complètement un monde à la possibilité de lancer facilement des solutions de carte simples de manière intuitive sans tous les efforts. Après tout, à ce stade, vous lancez une application React avec laquelle vous êtes probablement déjà familier.

# Aller un peu plus loin avec Gatsby

Vous voulez que ce soit plus facile, dites-vous ? Vous voulez que je construise la carte pour vous, dites-vous ? Eh bien, vous avez de la chance ! Tout d'abord, donnons une brève introduction à un autre outil.

Pour les non-initiés, [Gatsby](https://www.gatsbyjs.org/) est un framework JavaScript qui permet aux développeurs de lancer facilement des applications React complètes et fonctionnelles en quelques minutes. Ils ont tous les éléments de base en place et hors du chemin pour vous permettre de faire ce que vous faites de mieux : vous concentrer sur les parties importantes de votre application.

La belle partie de Gatsby est qu'il supporte les extensions de leur installation par défaut qu'ils appellent _Starters_. Quelle meilleure façon de faciliter la création de cartes pour les gens que de créer un Gatsby Starter ?

# Gatsby Starter Leaflet

En combinant la facilité d'un Gatsby Starter et la flexibilité de Leaflet, nous avons [Gatsby Starter Leaflet](https://github.com/colbyfayock/gatsby-starter-leaflet). Cet outil simple vous permet de créer une nouvelle application React exécutant Leaflet aux côtés de React Leaflet en quelques secondes (ou minutes selon votre ordinateur).

![Image](https://www.freecodecamp.org/news/content/images/2019/10/gatsby-starter-leaflet-map-1024x535.jpg)
_Page de démarrage pour Gatsby Starter Leaflet_

Avec [quelques commandes de base](https://github.com/colbyfayock/gatsby-starter-leaflet), y compris l'installation de vos dépendances, vous avez une application qui est prête pour que vous commeniez à construire dessus pour créer des cartes qui sauveront le monde. Mieux encore, il inclut quelques intégrations prêtes à l'emploi comme [OpenStreetMap](https://www.openstreetmap.org/) et une configuration de service de carte facile à mettre en place pour les API de composants React Leaflet de base qui vous permettent d'obtenir facilement un produit et d'avoir plus de flexibilité pour créer des applications de cartographie plus intelligentes.

# Il doit y avoir quelques inconvénients...

Aucune bibliothèque ou framework n'est sans ses inconvénients. Plus votre application de cartographie devient compliquée, plus vous rencontrez de points de douleur. Voici quelques-uns de notre expérience qui pourraient vous aider à vous installer.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/bad-news.gif)
_Bob Kelso — Scrubs_

# Leaflet — de la Fenêtre à React

Essayer de gérer l'état et le cycle de vie entre votre carte Leaflet et vos composants React peut s'avérer délicat. Essayer de maintenir et de mettre à jour constamment votre composant en utilisant des props commencera immédiatement à créer des problèmes entre l'état de la carte obsolète ou des fuites de mémoire dues aux cartes qui ne se démontent pas correctement lorsque le composant le fait.

**Conseil** : montez votre carte avec React, interagissez avec elle en utilisant l'API native Leaflet. Une fois votre carte rendue et stabilisée, vous pouvez utiliser Leaflet pour faire voler votre utilisateur autour du monde et dessiner sur votre carte sans rencontrer les problèmes d'état de plusieurs rendus de composants.

# Utilisation limitée des tuiles publiques

Bien qu'il existe quelques services de tuilage disponibles qui vous permettent de vous connecter facilement et de créer une carte de base, tous ne sont pas réellement destinés à être fortement utilisés. Prenez par exemple OpenStreetMap, bien que vous puissiez jouer et développer des solutions de base sur leur point de terminaison public, une utilisation intensive sera limitée et potentiellement bloquée sans autorisation explicite de ceux qui maintiennent leurs serveurs.

**Conseil** : lorsque vous commencez à jouer, vous ne devriez pas avoir à vous inquiéter trop. Dans le pire des cas, les cartes seront un peu lentes à télécharger. À mesure que votre application commence à recevoir plus de trafic, vous voudrez envisager de [lancer votre propre service de tuilage](https://github.com/Overv/openstreetmap-tile-server) ou de payer pour une solution clé en main telle que [Mapbox](https://www.mapbox.com/).

# Commencez à cartographier !

Il n'a jamais été aussi facile de construire une application web basée sur des cartes. Il existe suffisamment d'outils, de documentation et de données publiques disponibles pour vous aider à démarrer et à commencer à construire des cartes pour explorer notre monde en un temps record. Alors, qu'attendez-vous ?

![Image](https://www.freecodecamp.org/news/content/images/2019/10/dora-explorer.jpg)
_Allez explorer avec Dora !_

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Suivez-moi pour plus de Javascript, UX et autres choses intéressantes !" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">? Suivez-moi sur Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">?F4F9 Abonnez-vous à ma chaîne YouTube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;">F4E9 Inscription à ma newsletter</a>
    </li>
  </ul>
</div>

_Publié à l'origine sur [https://www.element84.com/blog/mapping-with-leaflet-and-react](https://www.element84.com/blog/mapping-with-leaflet-and-react)_