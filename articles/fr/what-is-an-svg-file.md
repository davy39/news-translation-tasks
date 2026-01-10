---
title: Qu'est-ce qu'un fichier SVG ?
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-06-01T16:05:04.000Z'
originalURL: https://freecodecamp.org/news/what-is-an-svg-file
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/svg.png
tags:
- name: image
  slug: image
- name: SVG
  slug: svg
seo_title: Qu'est-ce qu'un fichier SVG ?
seo_desc: 'SVG stands for scalable vector graphics. It''s a web-friendly vector-based
  file format used to render two-dimensional images on the internet.

  You can identify SVG files by their extension – .svg.

  Unlike other popular image formats like PNG, JPEG, and ...'
---

SVG signifie « Scalable Vector Graphics » (graphiques vectoriels adaptables). Il s'agit d'un format de fichier vectoriel compatible avec le web, utilisé pour rendre des images en deux dimensions sur Internet.

Vous pouvez identifier les fichiers SVG par leur extension – `.svg`.

Contrairement à d'autres formats d'image populaires comme PNG, JPEG et JPG – qui stockent les informations d'image sous forme de pixels car ce sont des formats basés sur des raster – les SVG stockent les informations graphiques sous forme d'un ensemble de points et de lignes.

Cela signifie que, peu importe comment les fichiers SVG sont retravaillés, zoomés ou redimensionnés, ils ne deviennent pas flous et pixelisés comme les PNG, JPG et autres images raster.

Cet article vous montrera les possibilités des fichiers image SVG et comment vous pouvez en créer un vous-même en le codant.

## Table des matières
- [Comment créer un fichier SVG](#heading-comment-creer-un-fichier-svg)
  - [Comment créer un SVG avec des programmes d'édition d'images](#heading-comment-creer-un-svg-avec-des-programmes-dedition-dimages) 
  - [Comment créer un SVG avec XML](#heading-comment-creer-un-svg-avec-xml)
- [À quoi sert un fichier SVG ?](#heading-a-quoi-sert-un-fichier-svg)
- [Comment ouvrir un fichier SVG](#heading-comment-ouvrir-un-fichier-svg)
- [Comment convertir un fichier SVG en image ?](#heading-comment-convertir-un-fichier-svg-en-image)
- [Conclusion](#heading-conclusion)


## Comment créer un fichier SVG

### Comment créer un SVG avec des programmes d'édition d'images
Vous pouvez créer un fichier SVG avec des logiciels d'édition d'images comme Adobe Illustrator, CorelDraw, Adobe Photoshop, Microsoft Visio et GIMP.

Avec ces programmes, votre créativité est votre seule limite en ce qui concerne les SVG que vous pouvez dessiner.

Cela dépend de votre niveau de connaissance et d'expérience avec ces programmes.

De plus, si vous créez une illustration ou des dessins avec Google Docs, vous pouvez les exporter au format SVG.


### Comment créer un SVG avec XML

Si vous ne savez pas comment utiliser les programmes d'édition d'images listés ci-dessus mais que vous savez coder, vous pouvez coder un SVG avec XML.

Pour coder un SVG, créez un fichier avec l'extension `.svg` :
![ss1](https://www.freecodecamp.org/news/content/images/2022/06/ss1.png)

**Étape 1** : Définissez vos balises d'ouverture et de fermeture SVG
```xml
<svg>
    <!--  -->
</svg>
```
**Étape 2** : Définissez les attributs de version et `xmlns` dans la balise d'ouverture et réglez-les respectivement sur `1.1` et `"http://www.w3.org/2000/svg"`.

```xml
<svg version="1.1" xmlns="http://www.w3.org/2000/svg">
    
</svg>
```

**Étape 3** : Spécifiez la forme que vous souhaitez dessiner dans une balise auto-fermante. Par exemple, `<rect>` pour un rectangle.
```xml
<svg version="1.1" xmlns="http://www.w3.org/2000/svg">
    <rect />
</svg>
```

**Étape 4** : Spécifiez la largeur et la hauteur que vous souhaitez :
```xml
 width="200" height="100"
```

**Étape 5** : Définissez la couleur avec laquelle vous souhaitez remplir la forme avec l'attribut `fill` :

```xml
fill="#2ecc71"
```

Le code ressemble maintenant à ce qui est montré dans l'extrait ci-dessous :
```xml
<svg version="1.1" xmlns="http://www.w3.org/2000/svg">
    <rect width="200" height="100" fill="#2ecc71" />
</svg>
```

Et à la fin, voici ce qui s'affiche dans le navigateur :
![ss2](https://www.freecodecamp.org/news/content/images/2022/06/ss2.png)

Vous pouvez également définir un border-radius sur les axes `x` et `y` avec les attributs `rx` et `ry` :
```xml
<svg version="1.1" xmlns="http://www.w3.org/2000/svg">
    <rect width="200" height="100" fill="#2ecc71" rx="4" ry="4" />
</svg>
```
![ss3](https://www.freecodecamp.org/news/content/images/2022/06/ss3.png)

Après avoir dessiné le SVG, vous pouvez l'utiliser comme valeur pour la source (`src`) d'une image :
```html
<img src="svgdraw.svg" alt="Un rectangle créé avec SVG" />
```
Si vous le souhaitez, vous pouvez intégrer le SVG directement dans votre code HTML :
```html
<body>
    <svg version="1.1" xmlns="http://www.w3.org/2000/svg">
      <rect width="200" height="100" fill="#2ecc71" />
    </svg>
</body>
```


## À quoi sert un fichier SVG ?

Parce que les fichiers SVG restent les mêmes à vie, les icônes et logos de sites web sont généralement créés avec eux.

Un excellent avantage des SVG est que le texte qu'ils contiennent peut être lu par les moteurs de recherche comme Google, donc les fichiers SVG sont utilisés pour créer des infographies et des illustrations.

## Comment ouvrir un fichier SVG

Les navigateurs modernes comme Google Chrome, Edge, Safari et Firefox ont des fonctionnalités intégrées qui leur permettent d'ouvrir des fichiers SVG pour vous.

Vous pouvez également ouvrir des fichiers SVG dans des logiciels d'édition spécialisés que vous pouvez utiliser pour les créer. À nouveau, des exemples sont Adobe Illustrator, CorelDraw, Adobe Photoshop, Microsoft Visio et GIMP.

Si vous souhaitez éditer des fichiers SVG, vous pouvez les ouvrir avec un éditeur de code comme VS Code, Atom et Sublime Text, puis apporter vos modifications.

## Comment convertir un fichier SVG en image ?

Si vous souhaitez convertir un SVG en d'autres formats d'image comme PNG et JPG, vous pouvez utiliser des programmes d'édition d'images comme Adobe Photoshop.

Vous pouvez également utiliser un outil en ligne appelé [Convertio](https://convertio.co/svg-png/).

Tout ce que vous avez à faire est de télécharger votre SVG, puis de sélectionner le format dans lequel vous souhaitez le convertir.
![ss4](https://www.freecodecamp.org/news/content/images/2022/06/ss4.png)

## Conclusion

Il existe de nombreuses raisons pour lesquelles vous devriez utiliser les SVG.

Ma préférée parmi toutes ces raisons est que les moteurs de recherche peuvent lire le texte sur les fichiers SVG. Cela est dû au fait que les fichiers SVG sont écrits en XML pur – le langage de balisage pour la transmission de données numériques.

Si Google et d'autres moteurs de recherche trouvent des mots-clés pertinents dans les fichiers SVG, cela peut entraîner un énorme boost en SEO.

Merci d'avoir lu.