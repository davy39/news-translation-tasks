---
title: 'Photoshop 101 : une introduction pour les développeurs web'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-23T21:19:02.000Z'
originalURL: https://freecodecamp.org/news/photoshop-101-introduction-for-web-developers-62d55232e62b
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9cabbc740569d1a4ca93a0.jpg
tags:
- name: Design
  slug: design
- name: photoshop
  slug: photoshop
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: 'Photoshop 101 : une introduction pour les développeurs web'
seo_desc: 'By Vincent Humeau

  Introduction

  Often, when working as web developer, we need to integrate templates. They can be
  from Photoshop or other software. In this article, we will have a look at the basics
  of Photoshop for web developers.

  This content was in...'
---

Par Vincent Humeau

### Introduction

Souvent, en travaillant en tant que développeur web, nous devons intégrer des templates. Ils peuvent provenir de Photoshop ou d'autres logiciels. Dans cet article, nous allons examiner les bases de Photoshop pour les développeurs web.

Ce contenu a été initialement écrit pour un atelier pour [DAMDigital London](http://damdigital.com/).

Adobe Photoshop est un logiciel de retouche d'images matriciel, ce qui signifie qu'il s'agit d'un programme qui permet aux utilisateurs de créer et de modifier des images.

![Image](https://cdn-media-1.freecodecamp.org/images/Hn9dRTjo6YkUp5YZ5bnr1oIGxXjjMm9G1j2V)
_Image [source](https://www.adobe.com/products/photoshop.html#hero-featured-video" rel="noopener" target="_blank" title=")_

Il a été lancé en 1988 et est devenu la norme de l'industrie pour les logiciels graphiques.

Vous pouvez télécharger une version d'essai gratuite de Photoshop sur le [site web d'Adobe](https://www.adobe.com/products/photoshop/free-trial-download.html).

### Espace de travail

L'espace de travail de Photoshop est modulaire, vous pouvez donc l'adapter en fonction du travail que vous effectuez. Certains espaces de travail par défaut sont déjà configurés dans Photoshop. Dans cet article, j'utilise celui intitulé `Graphic and Web`. Pour passer à cet espace de travail, allez dans `Fenêtre/espacedetravail/Graphic and Web`.

Examinons notre espace de travail :

![Image](https://cdn-media-1.freecodecamp.org/images/GrHsceHchCL77wzBJVYovMnh6Wumhltg6ikN)
_Photoshop_

* **A — Barre de menu** : C'est ici que vous trouverez la plupart des options de Photoshop.
* **B — Barre d'options** : Cette barre vous donnera toutes les options pour l'outil actuellement sélectionné.
* **C — Boîte à outils** : Ce panneau contient tous les outils disponibles dans Photoshop. Les outils liés sont regroupés ensemble, et vous pouvez cliquer longuement sur l'un d'eux pour voir tous les outils.
* **D — Panneaux** : C'est la zone où vous avez vos panneaux de base ouverts, tels que `Calques`, `Historique`, etc. Pour ouvrir un panneau, allez simplement dans `Fenêtre/(Panneau que vous voulez ouvrir)`.

### Créer un nouveau fichier

Lors de la création d'un nouveau fichier dans Photoshop, vous devez d'abord savoir pour quel support le design va être utilisé — c'est-à-dire, va-t-il être utilisé pour un écran (web, film ou vidéo) ou pour l'impression ?

Selon la réponse à cette question, vous devrez modifier la valeur PPI (Pixels Par Pouce).

> _Pixels par pouce (PPI) est une mesure utilisée pour définir la résolution d'un affichage d'ordinateur. Cette métrique évalue la qualité de l'image qu'un dispositif de calcul ou d'affichage particulier est capable d'afficher. Les pixels par pouce sont également connus sous le nom de densité de pixels._ [Techopedia](https://www.techopedia.com/definition/2741/pixels-per-inch-ppi)

Pour l'impression, vous avez généralement besoin de 300PPI, mais cela dépend en réalité de l'imprimante et de la taille du document imprimé. Vous devriez également changer votre couleur en CMYK, mais cela dépend à nouveau de la manière dont vous imprimez votre document. Si vous souhaitez en savoir plus sur les couleurs RGB et CMYK, consultez cet [article](https://printaura.com/difference-between-RGB-and-CMYK).

Pour les écrans et le web, vous avez besoin de 72PPI et de couleurs RGB. Ensuite, vous devez spécifier la taille de votre écran. Je recommanderais de concevoir d'abord pour mobile, puis pour tablette et bureau.

En tant que développeur web, vous n'aurez peut-être pas besoin de créer un nouveau fichier. Il est probable que vous devrez travailler avec un design fourni par des designers web.

Nous allons maintenant examiner un template `.psd` existant et travailler avec pour explorer Photoshop.

Vous pouvez télécharger et ouvrir ce [template PSD](https://shibbythemes.com/psd-freebies/surfersco-psd-template/) de [Luis Costa](http://lucaal.co/).

### Calques

L'une des fonctionnalités principales de Photoshop est les **calques**. Les calques sont comme une pile de feuilles, et vous pouvez voir à travers les zones transparentes ou les zones à faible opacité (partiellement transparentes).

Vous pouvez ouvrir le panneau des calques dans `Fenêtre/Calques`.

![Image](https://cdn-media-1.freecodecamp.org/images/tQQjIui8Q7xS3jxXIdyvWHDHNIVirFY8A93N)

Le calque supérieur dans ce panneau sera placé au-dessus de tous les autres calques en dessous. Les calques peuvent également être organisés en dossiers. Il est important de nommer correctement les calques et les dossiers. Cela aidera lors de l'intégration.

À côté de chaque dossier et calque, vous avez une icône en forme d'œil. Cela vous permet de basculer leur visibilité.

Votre PSD peut avoir beaucoup de calques et de documents. Une façon de trouver rapidement un calque est de sélectionner l'outil `déplacement (v)`. Faites un clic droit sur la toile où vous voulez trouver votre calque. Vous obtiendrez tous les calques dans la zone où vous avez cliqué droit. En cliquant sur l'un d'eux, il sélectionnera ce calque dans votre panneau de calques.

![Image](https://cdn-media-1.freecodecamp.org/images/G6F2Tk5n4XnwyY2X3J8cdswbGb-EWxZcIglZ)

### Boîte à outils

Photoshop est livré avec une multitude d'outils. Je vais vous montrer quelques-uns utiles qui vous aideront.

Tout d'abord, si vous venez d'installer Photoshop CC 2018, vous devrez restaurer tous les outils. Alors allez dans `Édition > Barre d'outils` et cliquez sur le bouton Restaurer les valeurs par défaut.

![Image](https://cdn-media-1.freecodecamp.org/images/UMkamoH1ixOjCLaOS6Z9bM-NVc1QReFOByyK)
_[Image d'Adobe](https://helpx.adobe.com/photoshop/using/tools.html" rel="noopener" target="_blank" title="https://helpx.adobe.com/photoshop/using/tools.html)_

Nous allons voir quelques-uns des outils les plus utiles que vous utiliseriez pour intégrer un template :

#### A — Outils de sélection

* **Déplacement** : Permet à l'utilisateur de déplacer un calque autour de la toile. Comme nous l'avons vu précédemment, il peut également être utilisé pour trouver un calque si vous faites un clic droit sur votre toile.
* **Sélection rectangulaire** : Cet outil est utilisé pour sélectionner une zone de la toile à copier et coller, la remplir, etc. Il peut également être utilisé pour mesurer. Lorsque votre sélection est terminée, vous pouvez trouver la taille de la zone sélectionnée dans `Fenêtre/Inf`. Vous devrez peut-être changer l'unité par défaut dans Photoshop `Édition/préférences/générales/Unités & Règles`, puis définir vos unités en pixels.

![Image](https://cdn-media-1.freecodecamp.org/images/RNWaDP1kVGLAyGz3DrKZXT-TCHYLFNYjazj8)

#### B — Outils de recadrage et de découpe

* **Recadrage** : Cet outil peut... recadrer une image. Dans les paramètres de l'outil (Barre d'options), vous pouvez définir un rapport d'aspect que vous souhaitez conserver.

#### C — Outils de mesure

* **Pipette** : La pipette vous permet d'obtenir rapidement une référence de couleur dans votre design. Il suffit de cliquer où vous voulez la couleur. Ensuite, en bas de votre boîte à outils, la couleur de premier plan changera pour la couleur sélectionnée. Si vous cliquez sur la couleur de premier plan, cela ouvrira la `fenêtre de sélection de couleur`. À partir de là, vous pouvez obtenir la valeur de votre couleur.
* **Échantillonneur de couleur** : Lors de l'intégration de votre design, vous devrez peut-être sélectionner plusieurs couleurs. Nous allons utiliser à nouveau la fenêtre d'informations `Fenêtre/Inf`. Cet outil nous permet de créer un échantillonneur de couleur. Il suffit de cliquer sur la zone de l'image dont vous voulez obtenir les couleurs. Vous obtiendrez chaque couleur dans le panneau d'informations. Vous pouvez changer le type de couleur en web en cliquant sur l'icône de la pipette sous le numéro.

![Image](https://cdn-media-1.freecodecamp.org/images/-r5ub2UTHKZWsnsIUtm4SdjRBEbGODTwmwHw)

* **Règle** : vous aide à mesurer votre template. Toutes les informations apparaîtront dans votre fenêtre d'informations. Maintenez `Maj` lors de la mesure, afin que votre règle reste droite. Vous pouvez également obtenir des angles.

#### G — Outil de navigation

* **Main** : Cet outil vous aide à vous déplacer autour de la toile. Vous pouvez accéder à cet outil à tout moment en maintenant la barre d'espace et en le faisant glisser avec votre souris.
* **Zoom** : Permet de zoomer et de dézoomer (vous pouvez utiliser `Ctrl` + `+`, ou `Ctrl` + `-` également).

### Repères

Comme vous l'avez peut-être remarqué en ouvrant notre fichier PSD, nous avons quelques lignes vertes sur notre template. Ce sont des repères. Ce sont essentiellement des aides qui vous aideront à construire ou à mesurer des choses autour de votre toile.

Vous pouvez déplacer les repères existants en utilisant l'outil `déplacement` (v).

Pour créer de nouveaux repères, vous devrez ouvrir votre règle : `Affichage/Règle` ou `Ctrl` + `R`. La règle apparaîtra dans votre espace de travail. Ensuite, à partir de la règle, vous pouvez faire glisser un nouveau repère dans votre toile.

Pour supprimer un repère, utilisez l'outil `déplacement` (v) et replacez le repère dans la règle.

Pour masquer et afficher tous vos repères, vous pouvez simplement utiliser `Ctrl` + `H`, ou aller dans `Affichage/Extras`.

### Objets dynamiques

Qu'est-ce que les objets dynamiques ?

> _Les objets dynamiques sont des calques qui contiennent des données d'image provenant d'images vectorielles ou matricielles, telles que des fichiers Photoshop ou Illustrator. Les objets dynamiques préservent le contenu source d'une image avec toutes ses caractéristiques d'origine, vous permettant d'effectuer une édition non destructive sur le calque._ [Adobe](https://helpx.adobe.com/photoshop/using/create-smart-objects.html)

Les objets dynamiques peuvent être reconnus dans vos calques lorsqu'ils ont l'icône suivante dans leurs miniatures :

![Image](https://cdn-media-1.freecodecamp.org/images/QyPI1W-pNwBcjwv8oz4WAY8oAorz4TbhcNHk)

Les objets dynamiques sont vraiment pratiques si vous travaillez avec des images de type vectoriel (SVG, EPS, AI), mais sont également utiles avec d'autres fichiers raster complexes.

Essayons d'importer un objet dynamique dans notre PSD. Téléchargez un fichier SVG depuis [flaticon](https://www.flaticon.com/free-icon/surfboard_930944#term=surf&page=1&position=10). Pour importer notre SVG dans notre toile, il suffit de faire glisser le fichier dans la toile. Nous pouvons maintenant éditer notre SVG dans Illustrator, ou tout autre logiciel vectoriel, en double-cliquant sur la miniature ou notre objet dynamique. Les modifications apparaîtront dans notre PSD.

Les objets dynamiques peuvent faire bien plus que cela, cependant. Si vous souhaitez en savoir plus à leur sujet, consultez [10 Things You Need to Know About Smart Objects in Photoshop](https://design.tutsplus.com/tutorials/10-things-you-need-to-know-about-smart-objects-in-photoshop--cms-20268).

### Exporter des ressources

Tout d'abord, un simple rappel que Photoshop est un logiciel **matriciel**, et non un logiciel **vectoriel**. Cela signifie que nous ne pouvons pas exporter de fichiers SVG depuis Photoshop. Pour ce faire, vous devrez exporter ces types de fichiers depuis Illustrator ou Inkscape, par exemple.

Sur le web, nous voulons avoir des fichiers image légers. Pour la photographie, nous utiliserions un fichier `.jpg` compressé. Si vous devez utiliser la transparence (canal Alpha), nous utiliserions un fichier `.png`. Pour une image animée, nous utiliserions un `.gif`. Si vous avez besoin d'une image vectorielle (icônes, par exemple), le mieux est d'exporter votre fichier en `.svg`. Si vous souhaitez avoir plus d'informations sur tous les fichiers disponibles dans Photoshop, vous pouvez consulter ["file formats" in the Adobe's website](https://helpx.adobe.com/photoshop/using/file-formats.html).

#### Exporter notre toile

Pour exporter la toile, suivez simplement ces étapes :

1. Allez dans `Fichier/Exporter/Enregistrer pour le Web`
2. Choisissez le format de fichier
3. Choisissez la taille de l'image
4. Choisissez la qualité
5. Enregistrez

#### Exporter uniquement une ressource de la toile

Vous devrez probablement exporter certaines ressources de votre template.

Exportons la flèche de gauche dans le carrousel de produits :

![Image](https://cdn-media-1.freecodecamp.org/images/rK3w29prW1my7q8LEhDrTfHTURlhqj9CIKh6)

En utilisant l'outil de déplacement, nous allons trouver notre calque. Faites un clic droit sur la flèche et sélectionnez le calque `Arrow Left`. Maintenant, faites simplement un clic droit sur ce calque dans le panneau des calques. Sélectionnez `exporter sous` et choisissez le type de fichier dont vous avez besoin.

Nous pouvons également exporter des dossiers.

### Actions

Qu'est-ce qu'une action dans Photoshop ?

> _Une action est une série de tâches que vous exécutez sur un seul fichier ou un lot de fichiers — commandes de menu, options de panneau, actions d'outil, etc. Par exemple, vous pouvez créer une action qui change la taille d'une image, applique un effet à l'image, puis enregistre le fichier dans le format souhaité._ [Adobe](https://helpx.adobe.com/photoshop/using/actions-actions-panel.html)

Cette fonctionnalité est vraiment pratique si vous souhaitez redimensionner un lot d'images pour le web !

Créons une nouvelle action pour recadrer une image et l'exporter :

1. Téléchargez un ensemble d'images depuis [https://unsplash.com/](https://unsplash.com/)
2. Ouvrez l'une de ces images
3. Ouvrez le panneau `Actions`, `Fenêtre/Actions`,
4. Créez une nouvelle action en cliquant sur l'icône **Créer une nouvelle action** (celle à gauche de l'icône de la corbeille). Nommons cette action **Export pour le web — nom du client.**
5. Nous enregistrons maintenant notre action. Le bouton d'enregistrement sera rouge, et vous pouvez arrêter l'enregistrement en cliquant sur l'icône d'arrêt (icône carrée à gauche).
6. Sélectionnez l'icône de recadrage et définissez le rapport à 1x1 et recadrez l'image.
7. Maintenant, nous voulons exporter notre image, `Fichier/Exporter/Enregistrer pour le Web`, sélectionnez `JPG`, qualité 50 % et largeur 500px.
8. Cliquez sur enregistrer et choisissez votre dossier de destination.
9. Fermez votre image sans l'enregistrer.
10. Pour arrêter l'enregistrement, cliquez sur l'icône d'arrêt (icône carrée à gauche).

Nous avons maintenant notre action, donc nous pouvons ouvrir une image et simplement "jouer" notre action en cliquant sur le bouton de lecture.

Si nous voulons appliquer notre action à un lot d'images, suivez simplement ces étapes :

1. Allez dans `Fichier/Automatisation/Lot`
2. Sélectionnez le dossier `Source`.
3. Sélectionnez notre action
4. Cliquez sur `Ok`

Et voilà ! Toutes vos images sont dans le dossier d'exportation.

J'espère que vous avez apprécié cette petite introduction à Photoshop 101 pour les développeurs web. Si vous souhaitez une version 102, faites-moi savoir ce que vous aimeriez savoir ou lire de plus.

* [@vince_umo](https://twitter.com/vince_umo)
* [vincent-humeau.com](http://vincent-humeau.com/)