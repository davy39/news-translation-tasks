---
title: Comment utiliser SVG comme placeholder et autres techniques de chargement d'images
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-30T16:09:28.000Z'
originalURL: https://freecodecamp.org/news/using-svg-as-placeholders-more-image-loading-techniques-bed1b810ab2c
coverImage: https://cdn-media-1.freecodecamp.org/images/0*zJGl1vKLttcJGIL4.jpg
tags:
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: UX
  slug: ux
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Comment utiliser SVG comme placeholder et autres techniques de chargement
  d'images
seo_desc: 'By José M. Pérez

  I’m passionate about image performance optimisation and making images load fast
  on the web. One of the most interesting areas of exploration is placeholders: what
  to show when the image hasn’t loaded yet.

  During the last days I have ...'
---

Par José M. Pérez

Je suis passionné par l'optimisation des performances des images et par le fait de rendre les images rapides à charger sur le web. L'un des domaines les plus intéressants à explorer est celui des placeholders : que montrer lorsque l'image n'est pas encore chargée.

Ces derniers jours, je suis tombé sur certaines techniques de chargement qui utilisent SVG, et je voudrais les décrire dans cet article.

Dans cet article, nous aborderons les sujets suivants :

* Aperçu des différents types de placeholders
  
* Placeholders basés sur SVG (bords, formes et silhouettes)
  
* Automatisation du processus.
  

### Aperçu des différents types de placeholders

Par le passé, [j'ai écrit sur les placeholders et le lazy-loading des images](https://medium.com/@jmperezperez/lazy-loading-images-on-the-web-to-improve-loading-time-and-saving-bandwidth-ec988b710290), et j'en ai également [parlé](https://www.youtube.com/watch?v=szmVNOnkwoU). Lorsque l'on fait du lazy-loading d'images, il est bon de réfléchir à ce qu'il faut rendre comme placeholder, car cela peut avoir un grand impact sur la performance perçue par l'utilisateur. Par le passé, j'ai décrit plusieurs options :

![Image](https://cdn-media-1.freecodecamp.org/images/tq-I1q1T0DwNSNK6lLzP0t9vBta7nMaes2TA align="left")

Plusieurs stratégies pour remplir la zone d'une image avant qu'elle ne se charge.

* **Laisser l'espace vide pour l'image** : Dans un monde de design responsive, cela empêche le contenu de sauter. Ces changements de mise en page sont mauvais du point de vue de l'expérience utilisateur, mais aussi pour la performance. Le navigateur est forcé de recalculer la mise en page chaque fois qu'il récupère les dimensions d'une image, laissant de l'espace pour celle-ci.
    
* **Placeholder** : Imaginez que nous affichons l'image de profil d'un utilisateur. Nous pourrions vouloir afficher une silhouette en arrière-plan. Cela est montré pendant que l'image principale est chargée, mais aussi lorsque cette requête a échoué ou lorsque l'utilisateur n'a pas défini de photo de profil. Ces images sont généralement vectorielles, et en raison de leur petite taille, elles sont de bonnes candidates pour être intégrées.
    
* **Couleur unie** : Prendre une couleur de l'image et l'utiliser comme couleur de fond pour le placeholder. Cela peut être la couleur dominante, la plus vibrante... L'idée est qu'elle soit basée sur l'image que vous chargez et qu'elle aide à rendre la transition entre aucune image et l'image chargée plus fluide.
    
* **Image floue** : Également appelée technique de flou progressif. Vous rendez une version minuscule de l'image, puis vous passez à la version complète. L'image initiale est minuscule à la fois en pixels et en kBs. Pour supprimer les artefacts, l'image est mise à l'échelle et floutée. J'ai écrit précédemment à ce sujet sur [Comment Medium fait le chargement progressif des images](https://medium.com/@jmperezperez/how-medium-does-progressive-image-loading-fd1e4dc1ee3d), [Utiliser WebP pour créer des images de prévisualisation minuscules](https://medium.com/@jmperezperez/using-webp-to-create-tiny-preview-images-3e9b924f28d6), et [Plus d'exemples de chargement progressif d'images](https://medium.com/@jmperezperez/more-examples-of-progressive-image-loading-f258be9f440b).
    

Il s'avère qu'il existe de nombreuses autres variations et que de nombreuses personnes intelligentes développent d'autres techniques pour créer des placeholders.

L'une d'entre elles consiste à utiliser des dégradés au lieu de couleurs unies. Les dégradés peuvent créer un aperçu plus précis de l'image finale, avec très peu de surcharge (augmentation de la charge utile).

![Image](https://cdn-media-1.freecodecamp.org/images/KcH3YSwHpmuSNm6LAc5KcngIIHc6HmnxwNdH align="left")

_Utilisation de dégradés comme arrière-plans. Capture d'écran de Gradify, qui n'est plus en ligne. Code [sur GitHub](https://github.com/fraser-hemp/gradify" rel="noopener" target="*blank" title=")._

Une autre technique consiste à utiliser des SVGs basés sur l'image, ce qui gagne en popularité avec des expériences et des hacks récents.

### Placeholders basés sur SVG

Nous savons que les SVGs sont idéaux pour les images vectorielles. Dans la plupart des cas, nous voulons charger une image bitmap, donc la question est de savoir comment vectoriser une image. Certaines options consistent à utiliser des bords, des formes et des zones.

#### Bords

Dans [un article précédent](https://medium.com/@jmperezperez/drawing-images-using-edge-detection-and-svg-animation-16a1a3676d3), j'ai expliqué comment trouver les bords d'une image et créer une animation. Mon objectif initial était d'essayer de dessiner des régions, en vectorisant l'image, mais je ne savais pas comment faire. J'ai réalisé que l'utilisation des bords pouvait également être innovante et j'ai décidé de les animer en créant un effet de "dessiner".

%[https://codepen.io/jmperez/pen/oogqdp] 

[**Dessiner des images en utilisant la détection de bords et l'animation SVG**](https://medium.com/@jmperezperez/drawing-images-using-edge-detection-and-svg-animation-16a1a3676d3)  
[_À l'époque, SVG était à peine utilisé et supporté. Quelque temps après, nous avons commencé à les utiliser comme alternative aux classiques..._medium.com](https://medium.com/@jmperezperez/drawing-images-using-edge-detection-and-svg-animation-16a1a3676d3)

#### Formes

SVG peut également être utilisé pour dessiner des zones de l'image au lieu de bords/bordures. D'une certaine manière, nous vectoriserions une image bitmap pour créer un placeholder.

À l'époque, j'ai essayé de faire quelque chose de similaire avec des triangles. Vous pouvez voir le résultat dans mes conférences [à CSSConf](https://jmperezperez.com/cssconfau16/#/45) et [Render Conf](https://jmperezperez.com/renderconf17/#/46).

%[https://codepen.io/jmperez/pen/BmaWmQ] 

Le codepen ci-dessus est une preuve de concept d'un placeholder basé sur SVG composé de 245 triangles. La génération des triangles est basée sur [la triangulation de Delaunay](https://en.wikipedia.org/wiki/Delaunay_triangulation) en utilisant [le polyserver de Possan](https://github.com/possan/polyserver). Comme prévu, plus le SVG utilise de triangles, plus la taille du fichier est grande.

#### Primitive et SQIP, une technique LQIP basée sur SVG

Tobias Baldauf a travaillé sur une autre technique de Low-Quality Image Placeholder utilisant des SVGs appelée [SQIP](https://github.com/technopagan/sqip). Avant de plonger dans SQIP lui-même, je vais donner un aperçu de [Primitive](https://github.com/fogleman/primitive), une bibliothèque sur laquelle SQIP est basé.

Primitive est assez fascinant et je vous recommande définitivement de le vérifier. Il convertit une image bitmap en un SVG composé de formes superposées. Sa petite taille le rend adapté pour l'intégrer directement dans la page. Un aller-retour en moins, et un placeholder significatif dans la charge utile HTML initiale.

Primitive génère une image basée sur des formes comme des triangles, des rectangles et des cercles (et quelques autres). À chaque étape, il en ajoute une nouvelle. Plus il y a d'étapes, plus l'image résultante ressemble à l'originale. Si votre sortie est en SVG, cela signifie également que la taille du code de sortie sera plus grande.

Afin de comprendre comment Primitive fonctionne, je l'ai exécuté à travers quelques images. J'ai généré des SVGs pour l'œuvre d'art en utilisant 10 formes et 100 formes :

![Image](https://cdn-media-1.freecodecamp.org/images/wru4xpNDHyRR3JMz1eIvgtGAQHLjn-d8Cnui align="left")

![Image](https://cdn-media-1.freecodecamp.org/images/063NW6I1LucSf8Oo1Tm4UDXif7mSVXOWK8Sb align="left")

![Image](https://cdn-media-1.freecodecamp.org/images/gtkZMkLD74Bggypce65qt-1O5dltlN9-wyFo align="left")

_Traitement de [cette image](https://jmperezperez.com/static/images/posts/svg-placeholders/pexels-photo-281184-square.jpg) en utilisant Primitive, avec [10 formes](https://jmperezperez.com/static/images/posts/svg-placeholders/pexels-photo-281184-square-10.svg) et [100 formes](https://jmperezperez.com/static/images/posts/svg-placeholders/pexels-photo-281184-square-100.svg)._

![Image](https://cdn-media-1.freecodecamp.org/images/RcbRK2L4F5SN-LcbaAo3YBqi6YyisWSElWD1 align="left")

![Image](https://cdn-media-1.freecodecamp.org/images/0BUVCyRTKGT60ZzgpQi5lFlrYkZa5Rcaivjv align="left")

![Image](https://cdn-media-1.freecodecamp.org/images/VAetFfTVYQwi8ixmnMgOcJjVqdRDuVYW4lsV align="left")

_Traitement de [cette image](https://jmperezperez.com/static/images/posts/svg-placeholders/pexels-photo-618463-square.jpg) en utilisant Primitive, avec [10 formes](https://jmperezperez.com/static/images/posts/svg-placeholders/pexels-photo-618463-square-10.svg) et [100 formes](https://jmperezperez.com/static/images/posts/svg-placeholders/pexels-photo-618463-square-100.svg)._

Lorsque l'on utilise 10 formes, les images commencent à donner une idée de l'image originale. Dans le contexte des placeholders d'images, il est possible d'utiliser ce SVG comme placeholder. En fait, le code pour le SVG avec 10 formes est vraiment petit, environ 1030 octets, qui descend à ~640 octets lorsque l'on passe la sortie par SVGO.

```xml
<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024"><path fill="#817c70" d="M0 0h1024v1024H0z"/><g fill-opacity=".502"><path fill="#03020f" d="M178 994l580 92L402-62"/><path fill="#f2e2ba" d="M638 894L614 6l472 440"/><path fill="#fff8be" d="M-62 854h300L138-62"/><path fill="#76c2d9" d="M410-62L154 530-62 38"/><path fill="#62b4cf" d="M1086-2L498-30l484 508"/><path fill="#010412" d="M430-2l196 52-76 356"/><path fill="#eb7d3f" d="M598 594l488-32-308 520"/><path fill="#080a18" d="M198 418l32 304 116-448"/><path fill="#3f201d" d="M1086 1062l-344-52 248-148"/><path fill="#ebd29f" d="M630 658l-60-372 516 320"/></g></svg>
```

Les images générées avec 100 formes sont plus grandes, comme prévu, pesant ~5 ko après SVGO (8 ko avant). Elles ont un excellent niveau de détail avec une charge utile encore petite. La décision du nombre de triangles à utiliser dépendra largement du type d'image (par exemple, contraste, quantité de couleurs, complexité) et du niveau de détail.

Il serait possible de créer un script similaire à [cjpeg-dssim](https://github.com/technopagan/cjpeg-dssim) qui ajuste la quantité de formes utilisées jusqu'à ce qu'un seuil de [similarité structurelle](https://en.wikipedia.org/wiki/Structural_similarity) soit atteint (ou un nombre maximum de formes dans le pire des cas).

Ces SVGs résultants sont également excellents à utiliser comme images de fond. Étant contraints par la taille et vectoriels, ils sont de bons candidats pour les images héroïques et les grands arrière-plans qui, autrement, montreraient des artefacts.

#### SQIP

En [les propres mots de Tobias](https://github.com/technopagan/sqip) :

> *SQIP est une tentative de trouver un équilibre entre ces deux extrêmes : il utilise [Primitive](https://github.com/fogleman/primitive) pour générer un SVG composé de plusieurs formes simples qui approximient les principales caractéristiques visibles à l'intérieur de l'image, optimise le SVG en utilisant [SVGO](https://github.com/svg/svgo) et ajoute un filtre de flou gaussien. Cela produit un placeholder SVG qui ne pèse que ~800-1000 octets, qui a l'air lisse sur tous les écrans et fournit un indice visuel du contenu de l'image à venir.*

Le résultat est similaire à l'utilisation d'une minuscule image de placeholder pour la technique de flou progressif (ce que [Medium](https://medium.com/@jmperezperez/how-medium-does-progressive-image-loading-fd1e4dc1ee3d) et [d'autres sites](https://medium.com/@jmperezperez/more-examples-of-progressive-image-loading-f258be9f440b) font). La différence est que, au lieu d'utiliser une image bitmap, par exemple JPG ou WebP, le placeholder est en SVG.

Si nous exécutons SQIP contre les images originales, nous obtiendrons ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/hbNTQ6U2ikSx2bBCETSrj9QsjVlJReX-Hlqx align="left")

![Image](https://cdn-media-1.freecodecamp.org/images/8h21TmNbbC7eOxBKNkOo2TXV-Ulwx5a3Z9bd align="left")

Les images de sortie utilisant SQIP pour [la première image](https://jmperezperez.com/static/images/posts/svg-placeholders/pexels-photo-281184-square-sqip.svg) et [la seconde](https://jmperezperez.com/static/images/posts/svg-placeholders/pexels-photo-618463-square-sqip.svg).

Le SVG de sortie fait ~900 octets, et en inspectant le code, nous pouvons repérer le filtre `feGaussianBlur` appliqué au groupe de formes :

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2000 2000"><filter id="b"><feGaussianBlur stdDeviation="12" /></filter><path fill="#817c70" d="M0 0h2000v2000H0z"/><g filter="url(#b)" transform="translate(4 4) scale(7.8125)" fill-opacity=".5"><ellipse fill="#000210" rx="1" ry="1" transform="matrix(50.41098 -3.7951 11.14787 148.07886 107 194.6)"/><ellipse fill="#eee3bb" rx="1" ry="1" transform="matrix(-56.38179 17.684 -24.48514 -78.06584 205 110.1)"/><ellipse fill="#fff4bd" rx="1" ry="1" transform="matrix(35.40604 -5.49219 14.85017 95.73337 16.4 123.6)"/><ellipse fill="#79c7db" cx="21" cy="39" rx="65" ry="65"/><ellipse fill="#0c1320" cx="117" cy="38" rx="34" ry="47"/><ellipse fill="#5cb0cd" rx="1" ry="1" transform="matrix(-39.46201 77.24476 -54.56092 -27.87353 219.2 7.9)"/><path fill="#e57339" d="M271 159l-123-16 43 128z"/><ellipse fill="#47332f" cx="214" cy="237" rx="242" ry="19"/></g></svg>
```

SQIP peut également générer une balise d'image avec le contenu SVG encodé en Base 64 :

```xml
<img width="640" height="640" src="example.jpg" alt="Ajouter un texte alternatif descriptif" style="background-size: cover; background-image: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyMDAwIDIwMDAiPjxmaWx0ZXIgaWQ9ImIiPjxmZUdhdXNzaWFuQmx1ciBzdGREZXZpYXRpb249IjEyIiAvPjwvZmlsdGVyPjxwYXRoIGZpbGw9IiM4MThjNzAiIGQ9Ik0wIDBoMjAwMHYyMDAwSDB6Ii8+PGcgZmlsdGVyPSJ1cmwoI2IpIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSg0IDQpIHNjYWxlKDcuODEyNSkiIGZpbGwtb3BhY2l0eT0iLjUiPjxlbGxpcHNlIGZpbGw9IiMwMDAyMTAiIHJ4PSIxIiByeT0iMSIgdHJhbnNmb3JtPSJtYXRyaXgoNTAuNDEwOTggLTMuNzk1MSAxMS4xNDc4NyAxNDguMDc4ODYgMTA3IDE5NC42KSIvPjxlbGxpcHNlIGZpbGw9IiNlZWUzYmIiIHJ4PSIxIiByeT0iMSIgdHJhbnNmb3JtPSJtYXRyaXgoLTU2LjM4MTc5IDE3LjY4NCAyNC40ODUxNCAtNzguMDY1ODQgMjA1IDExMC4xKSIvPjxlbGxpcHNlIGZpbGw9IiNmZmY0YmQiIHJ4PSIxIiByeT0iMSIgdHJhbnNmb3JtPSJtYXRyaXgoMzUuNDA2MDQgNS40OTIxOSAxNC44NTAxNyA5NS43MzMzNyAxNi40IDEyMy42KSIvPjxlbGxpcHNlIGZpbGw9IiM3OWM3ZGIiIGN4PSIyMSIgY3k9IjM5IiByeD0iNjUiIHJ5PSI2NSIvPjxlbGxpcHNlIGZpbGw9IiMwYzEzMjAiIGN4PSIxMTciIGN5PSIzOCIgcng9IjM0IiByeT0iNDciLz48ZWxsaXBzZSBmaWxsPSIjNWNiMGNkIiByeD0iMSIgcnk9IjEiIHRyYW5zZm9ybT0ibWF0cml4KC0zOS40NjIwMSA3Ny4yNDQ3NiAtNTQuNTYwOTIgLTI3Ljg3MzUzIDIxOS4yIDcuOSkiLz48cGF0aCBmaWxsPSIjZTU3MzM5IiBkPSJNMjcxIDE1OWwtMTIzLTE2IDQzIDEyOHowIi8+PGVsbGlwc2UgZmlsbD0iIzk3MzMyZiIgY3g9IjIxNCIgY3k9IjIzNyIgcng9IjI0MiIgcnk9IjE5Ii8+PC9nPjwvc3ZnPg==);">
```

#### Silhouettes

Nous venons de voir l'utilisation de SVGs pour les bords et les formes primitives. Une autre possibilité est de vectoriser les images en les "traçant". [Mikael Ainalem](https://twitter.com/mikaelainalem) a partagé [un codepen](https://codepen.io/ainalem/full/aLKxjm/) il y a quelques jours, montrant comment utiliser une silhouette en deux couleurs comme placeholder. Le résultat est vraiment joli :

![Image](https://cdn-media-1.freecodecamp.org/images/xIKbor-mLB7y7Ju8LXLibzxgGB5NTQbQNs64 align="left")

Les SVGs dans ce cas ont été dessinés à la main, mais la technique a rapidement donné lieu à des intégrations avec des outils pour automatiser le processus.

* [Gatsby](https://www.gatsbyjs.com/), un générateur de site statique utilisant React, supporte désormais ces SVGs tracés. Il utilise [un port JS de potrace](https://www.npmjs.com/package/potrace) pour vectoriser les images.
  
* [Craft 3 CMS](https://craftcms.com/), qui a également ajouté la prise en charge des silhouettes. Il utilise [un port PHP de potrace](https://github.com/nystudio107/craft-imageoptimize/blob/develop-v5/src/lib/Potracio.php).
  
* [image-trace-loader](https://github.com/EmilTholin/image-trace-loader), un chargeur Webpack qui utilise potrace pour traiter les images.
  

Il est également intéressant de voir une comparaison de la sortie entre le chargeur webpack d'Emil (basé sur potrace) et les SVGs dessinés à la main de Mikael.

Je suppose que la sortie générée par potrace utilise les options par défaut. Cependant, il est possible de les ajuster. Vérifiez [les options pour image-trace-loader](https://github.com/EmilTholin/image-trace-loader#options), qui sont pratiquement [celles transmises à potrace](https://www.npmjs.com/package/potrace#parameters).

### Résumé

Nous avons vu différents outils et techniques pour générer des SVGs à partir d'images et les utiliser comme placeholders. De la même manière que [WebP est un format fantastique pour les miniatures](https://medium.com/@jmperezperez/using-webp-to-create-tiny-preview-images-3e9b924f28d6), SVG est également un format intéressant à utiliser dans les placeholders. Nous pouvons contrôler le niveau de détail (et donc la taille), il est hautement compressible et facile à manipuler avec CSS et JS.

#### Ressources supplémentaires

Cet article a atteint [le sommet de Hacker News](https://news.ycombinator.com/item?id=15696596). Je suis très reconnaissant pour cela, et pour tous les liens vers d'autres ressources qui ont été partagés dans les commentaires de cette page. En voici quelques-uns !

* [Geometrize](https://github.com/Tw1ddle/geometrize-haxe) est un port de Primitive écrit en Haxe. Il existe également [une implémentation JS](https://github.com/Tw1ddle/geometrize-haxe-web) que vous pouvez essayer directement [dans votre navigateur](http://www.samcodes.co.uk/project/geometrize-haxe-web/).
  
* [Primitive.js](https://github.com/ondras/primitive.js), qui est un port de Primitive en JS. Également, [primitive.nextgen](https://github.com/cielito-lindo-productions/primitive.nextgen), qui est un port de l'application de bureau Primitive utilisant Primitive.js et Electron.
  
* Il existe quelques comptes Twitter où vous pouvez voir des exemples d'images générées avec Primitive et Geometrize. Consultez [@PrimitivePic](https://twitter.com/PrimitivePic) et [@Geometrizer](https://twitter.com/Geometrizer).
  
* [imagetracerjs](https://github.com/jankovicsandras/imagetracerjs), qui est un traceur et vectoriseur d'images raster écrit en JavaScript. Il existe également des ports pour [Java](https://github.com/jankovicsandras/imagetracerjava) et [Android](https://github.com/jankovicsandras/imagetracerandroid).
  
* [Canvas-Graphics](http://thomas.weinert.info/Canvas-Graphics/), une implémentation partielle de l'API Canvas JS en PHP autour de GD.
  

### Articles connexes

Si vous avez apprécié cet article, consultez ces autres articles que j'ai écrits sur les techniques de chargement d'images :

[**Comment Medium fait le chargement progressif des images**](https://medium.com/@jmperezperez/how-medium-does-progressive-image-loading-fd1e4dc1ee3d)  
[_Récemment, je parcourais un article sur Medium et j'ai repéré un bel effet de chargement d'image. D'abord, charger une petite image floue..._medium.com](https://medium.com/@jmperezperez/how-medium-does-progressive-image-loading-fd1e4dc1ee3d)[**Utiliser WebP pour créer des images de prévisualisation minuscules**](https://medium.com/@jmperezperez/using-webp-to-create-tiny-preview-images-3e9b924f28d6)  
[_Suite au sujet de l'optimisation des images, je vais examiner plus en détail la technique de Facebook pour créer des aperçus..._medium.com](https://medium.com/@jmperezperez/using-webp-to-create-tiny-preview-images-3e9b924f28d6)[**Plus d'exemples de chargement progressif d'images**](https://medium.com/@jmperezperez/more-examples-of-progressive-image-loading-f258be9f440b)  
[_Dans un article précédent, j'ai disséqué une technique utilisée par Medium pour afficher des images, passant d'une image floue à l'image finale..._medium.com](https://medium.com/@jmperezperez/more-examples-of-progressive-image-loading-f258be9f440b)

Vous pouvez lire plus de mes articles sur [jmperezperez.com](https://jmperezperez.com/svg-placeholders/).