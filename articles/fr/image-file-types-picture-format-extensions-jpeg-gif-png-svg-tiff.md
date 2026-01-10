---
title: Types de fichiers image – Les extensions de format d'image .jpeg, .svg et .png
  expliquées
subtitle: ''
author: Quincy Larson
co_authors: []
series: null
date: '2022-04-09T22:26:12.000Z'
originalURL: https://freecodecamp.org/news/image-file-types-picture-format-extensions-jpeg-gif-png-svg-tiff
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/timon-klauser-3MAmj1ZKSZA-unsplash.jpg
tags:
- name: Image Compression
  slug: image-compression
seo_title: Types de fichiers image – Les extensions de format d'image .jpeg, .svg
  et .png expliquées
seo_desc: 'When you’re working with images, it’s important to understand the different
  file types. Which format is best for what application?

  In this tutorial, we’re going to explain the most common image file types, and when
  you should use them.

  Note that this...'
---

Lorsque vous travaillez avec des images, il est important de comprendre les différents types de fichiers. Quel format est le meilleur pour quelle application ?

Dans ce tutoriel, nous allons expliquer les types de fichiers image les plus courants et quand les utiliser.

Notez que cet article est court et non technique. Si vous souhaitez approfondir l'aspect performance, lisez ces guides sur [comment optimiser les images de votre site web](https://www.freecodecamp.org/news/tag/image-optimization/).

D'abord, une brève explication sur le fonctionnement de la compression d'images.

## Lossless vs Lossy – Quelle est la différence entre ces deux types de compression ?

La compression sans perte est une classe d'algorithmes de compression de données qui permet de reconstruire parfaitement les données originales à partir des données compressées.

Il n'y a qu'une certaine limite à la compression d'un fichier avant de commencer à supprimer _certaines_ des informations qu'il contient.

C'est là que la compression "Lossy" intervient. Lossy signifie qu'elle perd certaines informations.

La compression Lossy permet de reconstruire uniquement une approximation des données originales (bien que généralement avec des taux de compression considérablement améliorés).

Vous verrez les termes "Lossless" et "Lossy" apparaître ci-dessous lorsque nous décrivons différents formats de fichiers image.

## Qu'est-ce que le format JPEG ? (.jpg et .jpeg)

Le JPEG est le type de fichier le plus courant pour les images. Il est idéal pour les photos et autres images avec beaucoup de couleurs.

Au fait, JPEG signifie Joint Photographic Experts Group – l'équipe qui a développé la norme.

Les fichiers JPEG sont plus petits que les autres types de fichiers, donc ils sont faciles à télécharger et à partager.

### Les JPEGs peuvent-ils être transparents ou avoir un fond transparent ?

Non. Contrairement aux GIFs, SVGs et PNGs, les JPEGs ne peuvent pas avoir de fonds transparents. Vous devriez convertir votre JPEG vers un autre format de fichier.

### .jpeg et .jpg sont-ils identiques ?

Oui – la seule différence est que, traditionnellement, les extensions de fichiers ne font que 3 caractères de long. ".jpg" est une forme abrégée de ".jpeg".

## Qu'est-ce qu'un PNG ? Le format de fichier PNG (.png)

Le PNG est un format de compression sans perte pour les images numériques. Le PNG a été créé comme un remplacement amélioré pour le GIF. Il est devenu le format de compression d'image sans perte le plus largement utilisé sur le web.

Le PNG est un type de fichier idéal pour les images avec transparence, comme les logos. Les fichiers PNG sont généralement plus grands que les JPEGs, donc ils ne sont pas idéaux pour les grandes images.

Les PNGs peuvent avoir un fond transparent.

## Qu'est-ce qu'un GIF ? Le format d'image GIF (.gif)

Le format GIF est un autre type de fichier image couramment utilisé sur le web. Les fichiers GIF sont généralement plus petits que les autres types de fichiers image, ce qui les rend idéaux pour une utilisation sur le web.

Les GIFs peuvent être utilisés pour des images statiques. Mais ils sont plus souvent associés à des animations – une série d'images qui se jouent automatiquement. Par exemple, voici un GIF du domaine public.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Globespin.gif)
_Un GIF du domaine public représentant un globe en rotation_

Ce n'est en réalité qu'une série d'une douzaine d'images jouées en boucle.

Notez que les GIFs peuvent également avoir un fond transparent.

### Comment prononce-t-on GIF ?

Le créateur du format GIF, Stephen Wilhite, a déclaré qu'il le prononçait "jif", comme dans "Jif", la marque de beurre de cacahuète.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/6398248857_42ff8de345_h-1.jpeg)
_Beurre de cacahuète Jif. Photo Creative Commons par Brian Cantoni._

Cela dit, presque tous les développeurs que je connais le prononcent "gif", comme dans "gift" (cadeau), et je pense que cela restera la manière la plus populaire de le dire.

%[https://twitter.com/FallonTonight/status/1011823951167750144?s=20&t=hGaYcvhV9J8H5n9pv9Em_A]

## Qu'est-ce qu'un TIFF ? Le format d'image TIFF (.tif)

Le TIFF est un type de fichier idéal pour les images de haute qualité qui doivent être éditées. Les fichiers TIFF sont volumineux, donc ils ne sont pas idéaux pour le partage en ligne.

Vous devriez utiliser un TIFF lorsque la qualité est plus importante que la taille du fichier. En pratique, un PNG est presque toujours une meilleure option – surtout lorsqu'il s'agit d'images sur le web.

## Qu'est-ce qu'un SVG ? Le format de fichier SVG (.svg)

Un SVG est un graphique vectoriel redimensionnable. Cela signifie que le graphique peut être redimensionné à n'importe quelle taille sans perdre en qualité.

Contrairement à tous les autres formats de fichiers dont nous parlons dans cet article, les fichiers SVG sont des fichiers vectoriels. (JPEG, PNG, GIF et TIFF sont des fichiers raster.)

Cela signifie que les fichiers SVG peuvent être redimensionnés à n'importe quelle taille sans perdre en qualité, tandis que les fichiers raster perdent en qualité lorsqu'ils sont agrandis.

Vous pouvez éditer les fichiers SVG en utilisant un logiciel d'édition vectorielle (ou simplement mettre à jour manuellement les coordonnées et les couleurs des graphiques). Vous ne pouvez éditer les fichiers PNG qu'en utilisant un logiciel d'édition raster.

Voici un exemple de fichier SVG provenant du [Mozilla Developer Network](https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial/Getting_Started). Voici à quoi ressemble le SVG dans sa forme native de code XML :

```xml
<svg version="1.1"
     width="300" height="200"
     xmlns="http://www.w3.org/2000/svg">

  <rect width="100%" height="100%" fill="red" />

  <circle cx="150" cy="100" r="80" fill="green" />

  <text x="150" y="125" font-size="60" text-anchor="middle" fill="white">SVG</text>

</svg>
```

Et ce simple code produit cette image :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/example-svg-file.png)
_Un carré rouge avec un point vert et les lettres "SVG" dessus._

Les fichiers SVG sont généralement plus petits que les fichiers PNG, car ils ne contiennent que les données nécessaires pour dessiner l'image, tandis que les fichiers PNG contiennent les données pour l'image entière.

Vous pouvez également animer les fichiers SVG en utilisant un outil appelé SMIL. Ainsi, ils peuvent servir de fichiers GIF extrêmement économes en espace. Et si vous êtes vraiment aventureux, vous pouvez programmer des SVGs.

## JPEGs VS PNGs – Quel format d'image est le meilleur pour le web ?

Le web pourrait avoir un aspect très différent à l'avenir, avec le déploiement de plus en plus de câbles à fibre optique et l'internet par satellite à haute vitesse devenant plus courant.

Mais pour l'instant, ma recommandation est d'utiliser des JPEGs pour la plupart de vos images.

Si vous avez un logo d'entreprise ou une photo très importante où la qualité est vitale, le PNG est une bonne option.

Pour les logos, je recommande d'utiliser un SVG, car il peut être redimensionné à l'infini et est très compact en taille.

## J'espère que vous avez appris beaucoup sur les types de fichiers image.

Et j'espère que cela vous a été utile. Si vous souhaitez en apprendre davantage sur la programmation et la technologie, essayez [le programme de codage principal de freeCodeCamp](https://www.freecodecamp.org/learn). C'est gratuit.