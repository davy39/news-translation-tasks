---
title: Comment concevoir, coder et animer des SVGs
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-07-12T17:04:01.000Z'
originalURL: https://freecodecamp.org/news/a-guide-to-svg-on-web-c5932dadca03
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ftD823GY_L-c4A-5hY8ozA.png
tags:
- name: animation
  slug: animation
- name: CSS
  slug: css
- name: Design
  slug: design
- name: Web Design
  slug: web-design
- name: women in tech
  slug: women-in-tech
seo_title: Comment concevoir, coder et animer des SVGs
seo_desc: 'By Surbhi Oberoi

  You can think of Scalable Vector Graphics (SVG’s) as responsive graphics. SVG is
  an XML-based format that allows you to create an image by using defined tags and
  attributes. Your code will render an image that you can edit right in y...'
---

Par Surbhi Oberoi

Vous pouvez considérer les graphiques vectoriels scalables (SVG) comme des graphiques réactifs. SVG est un format basé sur XML qui vous permet de créer une image en utilisant des balises et des attributs définis. Votre code rendra une image que vous pouvez éditer directement dans votre éditeur de code.

Voici un exemple de SVG. Si vous regardez son code, vous remarquerez qu'il est composé de balises et d'attributs, tout comme un document HTML. Le tout est contenu dans une balise <svg>. Tout d'abord, il y a une balise <rect> avec des contours noirs et un remplissage blanc. Et à l'intérieur, il y a une ellipse (presque un cercle, mais remarquez les attributs ry et rx) qui est remplie de couleur rouge.

Nous pouvons utiliser les SVG sur le web de deux manières. Nous pouvons utiliser les fichiers SVG comme attribut src des balises <img>. Ainsi, vous pouvez avoir <img src="japan.svg"> comme vous le feriez avec les PNG et les JPEG.

Mais le cas le plus intéressant (au cas où vous auriez remarqué que les balises ont un attribut id comme en HTML) est que nous pouvons coller directement la source du SVG dans une balise <div> à l'intérieur de notre HTML. Nous pouvons ensuite styliser ces divs comme des blocs de construction individuels — ou même des groupes de blocs de construction — de la manière dont nous le souhaitons. Nous pouvons appliquer du CSS, des animations, ou même ajouter de l'interactivité en utilisant JavaScript. C'est ce qui fait des SVG l'un des éléments les plus polyvalents et les plus populaires en HTML actuellement.

Les SVG sont infiniment scalables, réactifs, ont une taille de fichier plus petite, sont adaptés aux écrans à très haute densité de pixels de nouvelle génération, et peuvent être stylisés, animés et interactifs en utilisant des technologies web connues — notamment CSS et JavaScript.

Remarquez que toutes ces choses étaient auparavant possibles uniquement avec un embed Flash — qui nécessitait un lecteur Flash et beaucoup de travail spécialisé. Et il n'y a pas beaucoup d'amour pour Flash ces jours-ci.

#### Images vectorielles vs images matricielle

Les images matricielles sont composées de pixels pour former une image complète. Les JPEG, GIF et PNG sont des types courants d'images matricielles. Presque toutes les photos trouvées sur le web sont des images matricielles.

Les images matricielles sont composées d'un nombre fixe de pixels, donc les redimensionner sans affecter leur résolution n'est pas possible. Vous avez peut-être remarqué que le redimensionnement de la plupart des images leur donne un aspect granulaire et flou. C'est à cause de leur nombre fixe de pixels.

Voici ce qui se passe lorsque vous zoomez sur une image matricielle :

![Image](https://cdn-media-1.freecodecamp.org/images/0*DZ0Nry0tSMuKYFrL.gif)

Les images vectorielles, en revanche, sont flexibles et indépendantes de la résolution. Elles sont construites en utilisant des formes géométriques — lignes, rectangles, courbes — ou une séquence de commandes. Vous pouvez éditer leurs attributs, tels que la couleur, le remplissage et le contour.

Une utilisation courante des images vectorielles est pour les icônes et les petites animations d'icônes. Celles-ci apparaîtront nettes, même sur les écrans à très haute densité comme les futurs smartphones 4k.

Voici ce qui se passe lorsque vous zoomez sur une image vectorielle :

![Image](https://cdn-media-1.freecodecamp.org/images/0*9kjCwkCs_CIlJO9k.gif)

#### Balises SVG

**<svg>**

La balise <svg> intègre un document SVG à l'intérieur du document actuel, par exemple HTML. La balise a ses propres coordonnées x et y, hauteur et largeur, et son propre identifiant unique.

Voici à quoi pourrait ressembler une balise <svg> :

```
<svg width="580" height="400" xmlns="http://www.w3.org/2000/svg">
```

**<g>**

La balise <g> regroupe les éléments ensemble et agit comme un conteneur pour les éléments graphiques liés. Un élément <g> peut même contenir d'autres éléments <g> imbriqués à l'intérieur.

Voici un exemple de balise <g> :

```
<g> <title>background</title> <rect fill="#fff" id="canvas_background" height="402" width="582" y="-1" x="-1"/> <g display="none" overflow="visible" y="0" x="0" height="100%" width="100%" id="canvasGrid"> <rect fill="url(#gridpattern)" stroke-width="0" y="0" x="0" height="100%" width="100%"/> </g> </g>
```

**<rect>**

L'élément <rect> est une forme de base SVG représentant un rectangle. L'élément peut avoir divers attributs, comme des coordonnées, une hauteur, une largeur, une couleur de remplissage, une couleur de contour, et des coins pointus ou arrondis.

Voici un exemple de balise <rect> :

```
<rect id="svg_1" height="253" width="373" y="59" x="107.5" stroke-width="1.5" stroke="#000" fill="#fff"/>
```

**<use>**

L'élément <use> vous permet de cloner et de réutiliser les éléments graphiques SVG, y compris d'autres éléments comme <g> <rect> ainsi que d'autres éléments <use>.

Voici un exemple de balise <use> :

```
<text y="15">black</text> <use x="50" y="10" xlink:href="#Port" /> <text y="35">red</text> <use x="50" y="30" xlink:href="#Port"/> <text y="55">blue</text> <use x="50" y="50" xlink:href="#Port" style="fill:blue"/>
```

**<path>**

L'élément <path> définit un chemin de coordonnées pour une forme. Le code de la balise path peut sembler cryptique, mais ne vous laissez pas intimider. L'exemple de code suivant peut être lu comme ceci :
1. « M150 o » — Déplacer à (150,0)

2. « L75 200 » — Dessiner une ligne vers (75,200) depuis la dernière position (qui était (150,0)

3. « L255 200 » — Dessiner une ligne vers (225,200) depuis la dernière position (qui était (75,200)

4. « Z » — Fermer la boucle (dessiner vers le point de départ)

Vous n'avez probablement pas besoin d'apprendre cela puisque le code pour le chemin peut être généré dans n'importe quel éditeur SVG, mais c'est bien de le savoir.

Voici un exemple de balise <path> :

```
<svg height="210" width="400"> <path d="M150 0 L75 200 L225 200 Z" /> </svg>
```

**<symbol>**

Enfin, l'élément <symbol> définit des symboles qui sont réutilisables. Ces symboles ne peuvent être rendus que lorsqu'ils sont appelés par l'élément <use>.

Voici un exemple de balise <symbol> :

```
<svg> <symbol id="sym01" viewBox="0 0 150 110"> <circle cx="50" cy="50" r="40" stroke-width="8" stroke="red" fill="red"/> <circle cx="90" cy="60" r="40" stroke-width="8" stroke="green" fill="white"/> </symbol> <use xlink:href="#sym01" x="0" y="0" width="100" height="50"/> <use xlink:href="#sym01" x="0" y="50" width="75" height="38"/> <use xlink:href="#sym01" x="0" y="100" width="50" height="25"/> </svg>
```

#### Création de SVGs

Il existe de nombreux éditeurs SVG disponibles, comme Adobe Illustrator et Inkscape, qui est gratuit et open source. Puisque les fichiers SVG sont des XML en texte brut, vous pourriez également en coder un à la main en cas de besoin.

Pour cet exemple, j'utiliserai un simple éditeur en ligne [editor](http://editor.method.ac/) où vous pouvez concevoir des SVGs sans avoir à installer quoi que ce soit.

1. Tout d'abord, créez un cercle

2. Ensuite, ajoutez plus de cercles et sauvegardez le code source

**Animations CSS3**

Les SVGs peuvent être animés en ajoutant un id ou une classe au chemin SVG dans le code, puis en le stylisant en CSS3 comme tout autre document. Ci-dessous, un exemple de la manière dont les SVGs peuvent être animés.

L'animation CSS3 offre une variété de types d'animation parmi lesquels vous pouvez choisir. L'animation de ligne est un autre attribut intéressant du SVG.

Pour cet exemple suivant, j'ai écrit le texte « Hi, I am Surbhi » en utilisant un stylo dans l'éditeur. Ensuite, j'ai utilisé les keyframes CSS3 pour animer le trait.

Remarquez que chaque chemin a un id unique. C'est parce que le délai dans l'animation est important lors de l'animation d'un trait avec plus d'un mot.

#### Les animations avec la balise <animate>

<animate> est une balise d'animation intégrée à l'élément SVG lui-même. Elle définit comment l'attribut d'un élément change de la valeur initiale à la valeur finale dans la durée d'animation spécifiée. Cela est utilisé pour animer des propriétés qui ne peuvent pas être animées par CSS seul.

Les éléments courants de la balise animate sont la couleur, le mouvement et la transformation.

La balise animate est imbriquée à l'intérieur de la balise de forme de l'objet qui doit être animé. Elle ne fonctionne pas sur les coordonnées du chemin, mais uniquement à l'intérieur des balises d'objet. Remarquez l'attribut additif. Il signifie que les animations ne se remplacent pas les unes les autres, mais fonctionnent ensemble en même temps.

Voici un exemple d'animation d'un SVG en utilisant la balise animate HTML5 :

#### Animations et interactivité basées sur JavaScript

Puisque SVG est simplement un document avec des balises, nous pouvons également utiliser JavaScript pour interagir avec des éléments individuels des SVGs en obtenant leurs sélecteurs (id ou classe).

En plus de JavaScript vanilla, il existe diverses bibliothèques JavaScript disponibles pour animer et interagir avec les SVGs comme Vivus.js, Snap.svg, RaphaelJS et Velocity.js.

Dans l'exemple suivant, j'ai utilisé la bibliothèque Vivus.js avec jQuery pour réaliser une animation de trait de ligne.

#### Pourquoi ne pas utiliser les SVGs pour toutes les images ?

Les SVGs sont principalement adaptés aux images qui peuvent être construites avec quelques formes géométriques et formules. Bien que, en principe, vous puissiez convertir n'importe quoi comme votre photographie en SVG, la taille de l'image serait de plusieurs mégaoctets, ce qui annulerait le but d'économie d'espace des SVGs. Vous feriez mieux d'utiliser les SVGs pour les icônes, les logos et les petites animations.

Voici quelque chose que j'ai créé pendant que j'apprenais les SVGs, en utilisant CSS et SVGs, sans aucune bibliothèque. (Ne jugez pas !) [https://github.com/surbhioberoi/surbhi.me](https://github.com/surbhioberoi/surbhi.me)

![Image](https://cdn-media-1.freecodecamp.org/images/0*wWFcDqQBEODlYS8x.gif)

_Publié à l'origine sur [surbhioberoi.com](http://surbhioberoi.com/a-complete-guide-to-svg/) le 12 juillet 2016._