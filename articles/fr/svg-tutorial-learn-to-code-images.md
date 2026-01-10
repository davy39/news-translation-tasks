---
title: Tutoriel SVG – Comment coder des images avec 12 exemples
date: '2023-12-04T12:29:00.000Z'
author: Hunor Márton Borbély
authorURL: https://www.freecodecamp.org/news/author/hunor/
originalURL: https://freecodecamp.org/news/svg-tutorial-learn-to-code-images
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/Learn-SVG.001.jpeg
tags:
- name: image
  slug: image
- name: SVG
  slug: svg
seo_desc: 'Have you ever needed an icon for your website, but you couldn''t quite
  find the right one? Or perhaps you wanted to have a simple diagram, but didn''t
  want to learn a whole new library just for that?

  Well, good news – you can do all that and more witho...'
---


Avez-vous déjà eu besoin d'une icône pour votre site web sans parvenir à trouver la bonne ? Ou peut-être souhaitiez-vous un diagramme simple, mais ne vouliez pas apprendre une toute nouvelle bibliothèque juste pour cela ?

<!-- more -->

Eh bien, bonne nouvelle : vous pouvez faire tout cela et bien plus encore sans jamais quitter votre éditeur de code préféré, ni utiliser d'outils ou de bibliothèques tiers.

Depuis l'HTML5, nous pouvons inclure le code d'une image SVG à l'intérieur d'un document HTML. Nous n'avons même pas besoin d'utiliser la balise image qui renvoie à un fichier séparé. Nous pouvons inclure le code d'une image directement en "inline" dans le HTML. C'est possible car les SVG ont une syntaxe très similaire à celle du HTML.

Cela ouvre beaucoup d'options intéressantes. Soudain, nous pouvons accéder à des parties d'une image via JavaScript ou définir le style avec CSS. Nous pouvons animer des éléments d'une image depuis JavaScript ou la rendre interactive. Ou encore, nous pouvons inverser les choses et générer des graphiques à partir du code.

Pour des images plus complexes, vous utiliserez toujours un outil de design. Mais la prochaine fois que vous aurez besoin d'une icône simple, d'un diagramme ou d'une animation, vous pourrez peut-être la coder vous-même.

Alors, à quoi ressemblent les SVG sous la surface ? Dans ce tutoriel, nous allons parcourir le code source de quelques SVG pour en couvrir les bases.

Les exemples suivants proviennent de [svg-tutorial.com][1]. Vous pouvez également [regarder cet article en vidéo][2] avec encore plus d'exemples amusants.

## **La balise SVG**

Tout d'abord, nous devons parler de la balise `svg` elle-même. Cette balise contient les éléments de l'image et définit le cadre de notre image. Elle définit la taille interne et la taille externe de l'image.

Les propriétés `width` et `height` définissent l'espace que l'image occupe dans le navigateur. Il y a souvent aussi une propriété `viewBox`. Celle-ci définit un système de coordonnées pour les éléments à l'intérieur de l'image. Ces deux concepts peuvent être déroutants car ils définissent tous deux une taille.

Vous pouvez considérer la `width` et la `height` d'un SVG comme une taille externe et la `viewBox` comme une taille interne.

La taille définie par `width` et `height` correspond à la façon dont le reste du HTML perçoit l'image et à sa taille d'affichage dans le navigateur. La taille définie par `viewBox` est la façon dont les éléments de l'image se perçoivent lorsqu'ils se positionnent à l'intérieur de celle-ci.

Dans l'exemple suivant, nous avons trois SVG qui ont exactement le même contenu : un élément `circle` avec les mêmes coordonnées centrales et le même rayon. Ils paraissent pourtant assez différents.

![Learn-SVG.001-1](https://www.freecodecamp.org/news/content/images/2021/12/Learn-SVG.001-1.jpeg)

Le même cercle peut paraître différent selon la taille de l'image et la propriété `viewBox`

Dans l'exemple du milieu, la taille définie par `width` et `height` correspond à celle définie par la `viewbox`. Dans le premier exemple, nous voyons ce qui se passe si `width` et `height` sont plus petits. L'image rétrécit simplement car toutes les coordonnées et tailles définies dans l'image s'alignent toujours sur la `viewbox`.

Dans le dernier exemple, nous voyons ce qui se passe si la `viewbox` se concentre sur une partie seulement de l'image. Les éléments paraissent plus grands dans ce cas, mais la taille réelle de l'image est toujours définie par les propriétés `width` et `height`.

La `viewBox` définit également le centre du système de coordonnées dans lequel les éléments de l'image se placent.

Les deux premiers chiffres définissent quelle coordonnée doit se trouver dans le coin supérieur gauche de l'image. Les coordonnées croissent vers la droite et vers le bas. Dans cet article, nous allons centrer les systèmes de coordonnées. La coordonnée 0,0 sera toujours au milieu de l'image.

Une note avant de commencer : bien que nous puissions inclure des images SVG en inline dans un fichier HTML, cela ne signifie pas que nous pouvons combiner librement n'importe quelle balise SVG avec n'importe quelle balise HTML.

La balise SVG représente le cadre de l'image et chaque élément SVG doit se trouver à l'intérieur d'une balise SVG. L'inverse est également vrai. Les balises HTML ne peuvent pas se trouver à l'intérieur d'une balise SVG ; nous ne pouvons donc pas avoir de balise `div` ou `header` à l'intérieur d'un SVG. Mais ne vous inquiétez pas, il existe des balises similaires disponibles.

## **Comment créer une décoration de Noël avec SVG**

Commençons par une simple décoration de sapin de Noël. Ici, nous n'utiliserons que des formes simples : un rectangle et deux cercles.

Nous positionnerons et styliserons ces éléments avec des attributs. Pour le cercle, nous définissons la position centrale et pour le rectangle, nous définissons le coin supérieur gauche. Ces positions sont toujours relatives au système de coordonnées défini par la viewBox.

![Learn-SVG.002-1](https://www.freecodecamp.org/news/content/images/2021/12/Learn-SVG.002-1.jpeg)

Décoration de Noël faite de cercles et d'un rectangle. À droite, vous pouvez voir les coordonnées utilisées dans cet exemple.

```html
<html>
  <svg width="200" height="200" viewBox="-100 -100 200 200”>
    <circle cx="0" cy="20" r="70" fill="#D1495B" />

    <circle
      cx="0"
      cy="-75"
      r="12"
      fill="none"
      stroke="#F79257"
      stroke-width="2"
    />

    <rect x="-17.5" y="-65" width="35" height="20" fill="#F79257" />
  </svg>
</html>
```

Rappelez-vous, nous avons déplacé le centre du système de coordonnées au milieu de l'image ; l'axe X croît vers la droite et l'axe Y croît vers le bas.

Nous avons également des attributs de présentation qui stylisent nos formes. Contrairement au HTML, nous n'utilisons pas `background-color` pour définir la couleur d'une forme, mais l'attribut `fill`.

Et pour définir une bordure pour une forme, nous utilisons `stroke` et `stroke-width`. Notez comment nous utilisons l'élément `circle` à la fois pour dessiner un anneau et une boule avec des attributs différents.

## **Comment construire un sapin de Noël avec SVG**

Passons à un sapin de Noël. Nous ne pouvons pas toujours utiliser des formes basiques pour assembler notre image. Un polygone (`polygon`) est le moyen le plus simple de dessiner une forme libre. Ici, nous définissons une liste de points qui sont reliés par des lignes droites.

![Learn-SVG.003](https://www.freecodecamp.org/news/content/images/2021/12/Learn-SVG.003.jpeg)

Sapin de Noël composé de polygones et d'un rectangle

```html
<html>
  <svg width="200" height="200" viewBox="-100 -100 200 200">
    <polygon points="0,0 80,120 -80,120" fill="#234236" />
    <polygon points="0,-40 60,60 -60,60" fill="#0C5C4C" />
    <polygon points="0,-80 40,0 -40,0" fill="#38755B" />
    <rect x="-20" y="120" width="40" height="30" fill="brown" />
  </svg>
</html>
```

Vous vous demandez peut-être comment nous savons, avant de commencer à coder, où nos coordonnées doivent se situer.

Pour être honnête, cela demande un peu d'imagination. Vous pouvez commencer avec un stylo et du papier et dessiner un brouillon pour obtenir une estimation. Ou vous pouvez simplement faire une supposition, puis ajuster vos valeurs jusqu'à ce que le résultat soit satisfaisant.

## **Comment créer un bonhomme de pain d'épices avec SVG**

Continuons avec un bonhomme de pain d'épices. Puisque notre SVG vit maintenant à l'intérieur d'un fichier HTML, nous pouvons assigner des classes CSS à chaque balise et déplacer certains attributs vers le CSS.

Nous ne pouvons cependant déplacer que les attributs de présentation. Les attributs de position et ceux qui définissent la forme doivent rester dans le HTML. Mais nous pouvons déplacer les couleurs, les contours (`stroke`) et les attributs de police vers le CSS.

![Learn-SVG.004](https://www.freecodecamp.org/news/content/images/2021/12/Learn-SVG.004.jpeg)

Exemple de bonhomme de pain d'épices. À droite, vous pouvez voir à quoi il ressemblerait si le `stroke-width` était de 1.

```html
<svg class="gingerbread" width="200" height="200" viewBox="-100 -100 200 200">
  <circle class="body" cx="0" cy="-50" r="30" />

  <circle class="eye" cx="-12" cy="-55" r="3" />
  <circle class="eye" cx="12" cy="-55" r="3" />
  <rect class="mouth" x="-10" y="-40" width="20" height="5" rx="2" />

  <line class="limb" x1="-40" y1="-10" x2="40" y2="-10" />
  <line class="limb" x1="-25" y1="50" x2="0" y2="-15" />
  <line class="limb" x1="25" y1="50" x2="0" y2="-15" />

  <circle class="button" cx="0" cy="-10" r="5" />
  <circle class="button" cx="0" cy="10" r="5" />
</svg>
```

```css
.gingerbread .body {
  fill: #cd803d;
}

.gingerbread .eye {
  fill: white;
}

.gingerbread .mouth {
  fill: none;
  stroke: white;
  stroke-width: 2px;
}

.gingerbread .limb {
  stroke: #cd803d;
  stroke-width: 35px;
  stroke-linecap: round;
}
```

Nous avons déjà vu le remplissage (`fill`) et certaines propriétés de contour, mais en voici une autre : `stroke-linecap`. Cela permet d'arrondir l'extrémité de nos lignes.

Notez que les jambes et les bras sont ici de simples lignes. Si nous retirons l'extrémité arrondie et définissons un `stroke-width` plus petit, nous verrions qu'il s'agit de simples lignes. Mais en définissant une épaisseur de trait importante et une extrémité arrondie, nous pouvons façonner les jambes et les bras de notre personnage.

Notez également la propriété `rx` sur le rectangle définissant la bouche. Cela arrondit les bords. Vous pouvez y penser comme à un `border-radius` si vous préférez.

## **Comment créer une étoile avec SVG**

Passons à une étoile. Une étoile est une forme simple, nous pourrions donc la définir comme un ensemble de polygones et définir chaque point individuellement. Mais nous devrions alors connaître chaque coordonnée.

Au lieu de cela, nous pouvons simplement définir une branche comme un groupe, puis la répéter cinq fois avec une rotation pour obtenir la forme de l'étoile. Nous utilisons l'attribut `transform` pour définir une rotation.

![Learn-SVG.005](https://www.freecodecamp.org/news/content/images/2021/12/Learn-SVG.005.jpeg)

Forme d'étoile faite de polygones transformés. À droite, nous voyons les coordonnées d'une branche de l'étoile.

```html
<svg width="200" height="200" viewBox="-100 -100 200 200">      
  <g transform="translate(0 5)">
    <g>
      <polygon points="0,0 36,-50 0,-100" fill="#EDD8B7" />
      <polygon points="0,0 -36,-50 0,-100" fill="#E5C39C" />
    </g>
    <g transform="rotate(72)">
      <polygon points="0,0 36,-50 0,-100" fill="#EDD8B7" />
      <polygon points="0,0 -36,-50 0,-100" fill="#E5C39C" />
    </g>
    <g transform="rotate(-72)">
      <polygon points="0,0 36,-50 0,-100" fill="#EDD8B7" />
      <polygon points="0,0 -36,-50 0,-100" fill="#E5C39C" />
    </g>
    <g transform="rotate(144)">
      <polygon points="0,0 36,-50 0,-100" fill="#EDD8B7" />
      <polygon points="0,0 -36,-50 0,-100" fill="#E5C39C" />
    </g>
    <g transform="rotate(-144)">
      <polygon points="0,0 36,-50 0,-100" fill="#EDD8B7" />
      <polygon points="0,0 -36,-50 0,-100" fill="#E5C39C" />
    </g>
  </g>
</svg>
```

Dans cet exemple, chaque branche se compose de deux polygones. Ils doivent être pivotés de la même manière, nous pouvons donc les regrouper avec une balise `g` et les faire pivoter ensemble.

Vous pouvez considérer la balise `g` comme la balise `div` en HTML. En soi, elle ne représente rien. Mais elle peut contenir d'autres éléments, et les attributs définis sur la balise de groupe s'appliquent à ses enfants.

Les groupes peuvent être imbriqués. Avec le groupe extérieur, nous déplaçons (`translate`) l'étoile entière vers le bas de 5 unités.

## **Comment créer un flocon de neige avec SVG**

Le regroupement d'éléments est une astuce intéressante, mais nous avons dû répéter le même code pour chaque branche cinq fois.

Au lieu de répéter le même code encore et encore, nous pouvons également créer une définition pour une forme et la réutiliser par son `id`. Ici, nous définissons une branche de flocon de neige, puis nous l'utilisons six fois avec des rotations différentes.

![Learn-SVG.006](https://www.freecodecamp.org/news/content/images/2021/12/Learn-SVG.006.jpeg)

Flocon de neige composé d'éléments d'image réutilisés. À droite, nous voyons les coordonnées utilisées pour une branche.

```html
<svg width="200" height="200" viewBox="-100 -100 200 200">
  <defs>
    <path
      id="branch"
      d="
        M 0 0 L 0 -90
        M 0 -20 L 20 -34
        M 0 -20 L -20 -34
        M 0 -40 L 20 -54
        M 0 -40 L -20 -54
        M 0 -60 L 20 -74
        M 0 -60 L -20 -74"
      stroke="#E5C39C"
      stroke-width="5"
    />
  </defs>

  <use href="#branch" />
  <use href="#branch" transform="rotate(60)" />
  <use href="#branch" transform="rotate(120)" />
  <use href="#branch" transform="rotate(180)" />
  <use href="#branch" transform="rotate(240)" />
  <use href="#branch" transform="rotate(300)" />
</svg>
```

La branche est définie comme un `path` (chemin). Le `path` est la balise SVG la plus puissante. On peut définir pratiquement n'importe quoi avec des chemins, et si vous ouvrez n'importe quel fichier SVG, vous verrez principalement des chemins.

La forme du chemin est définie par l'attribut `d`. Ici, nous définissons plusieurs commandes de dessin. Une commande commence toujours par une lettre définissant le type de commande et se termine par une coordonnée.

Ici, nous n'avons que les deux commandes les plus simples : "move to" (`M`, déplacer vers) et "line to" (`L`, ligne vers). La commande `M` déplace le curseur vers un point sans tracer de ligne, et la commande `L` trace une ligne droite à partir du point précédent.

Une commande continue toujours la commande précédente, donc quand nous traçons une ligne, nous ne définissons que le point d'arrivée. Le point de départ sera le point d'arrivée de la commande précédente.

Ce chemin est un peu inhabituel car il contient plusieurs commandes `M` pour dessiner la branche principale et chaque branche latérale avec le même chemin.

## Comment dessiner une forêt avec SVG

La rotation n'est pas le seul moyen de générer des images à partir de formes simples. Dans cet exemple, nous définissons une forme d'arbre, puis nous la plaçons à diverses positions et en différentes tailles pour dessiner une forêt.

![Screenshot-2023-11-30-at-21.21.23](https://www.freecodecamp.org/news/content/images/2023/11/Screenshot-2023-11-30-at-21.21.23.png)

Forêt composée d'éléments d'image réutilisés

Tout d'abord, nous créons un arrière-plan à partir d'un rectangle et d'un cercle. Ensuite, nous définissons une forme d'arbre à partir d'un polygone simple et d'une ligne.

Ensuite, nous pouvons le réutiliser de la même manière que pour l'exemple du flocon de neige. Nous le déplaçons dans la section `defs`, l'enveloppons dans un élément de groupe, lui attribuons un ID, puis le réutilisons avec l'élément `use`.

Ici, nous positionnons également les éléments réutilisés en définissant des coordonnées `x` et `y`, et pour ajouter de la perspective à l'image, nous utilisons la transformation `scale` (échelle).

```HTML
<svg width="200" height="200" viewBox="-100 -100 200 200">
  <defs>
    <g id="tree">
      <polygon points="-10,0 10,0 0 -50" fill="#38755b" />
      <line x1="0" y1="0" x2="0" y2="10" stroke="#778074" stroke-width="2" />
    </g>
  </defs>

  <rect x="-100" y="-100" width="200" height="200" fill="#F1DBC3" />
  <circle cx="0" cy="380" r="350" fill="#F8F4E8" />

  <use href="#tree" x="-30" y="25" transform="scale(2)" />
  <use href="#tree" x="-20" y="40" transform="scale(1.2)" />
  <use href="#tree" x="40" y="40" />
  <use href="#tree" x="50" y="30" transform="scale(1.5)" />
</svg>
```

## **Comment créer un arbre tout en courbes avec SVG**

L'élément `path` devient vraiment puissant lorsque nous commençons à utiliser des courbes. L'une d'elles est la courbe de Bézier quadratique qui non seulement définit un point d'arrivée pour un segment, mais possède également un point de contrôle. Le point de contrôle est une coordonnée invisible vers laquelle la ligne se courbe, sans toutefois la toucher.

![Learn-SVG.007](https://www.freecodecamp.org/news/content/images/2021/12/Learn-SVG.007.jpeg)

Sapin de Noël créé à l'aide de courbes de Bézier quadratiques

```html
<svg width="200" height="400" viewBox="-100 -200 200 400">
  <path
    d="
      M 0 -80
      Q 5 -75 0 -70
      Q -10 -65 0 -60
      Q 15 -55 0 -50
      Q -20 -45 0 -40
      Q 25 -35 0 -30
      Q -30 -25 0 -20
      Q 35 -15 0 -10
      Q -40 -5 0 0
      Q 45 5 0 10
      Q -50 15 0 20
      Q 55 25 0 30
      Q -60 35 0 40
      Q 65 45 0 50
      Q -70 55 0 60
      Q 75 65 0 70
      Q -80 75 0 80
      Q 85 85 0 90
      Q -90 95 0 100
      Q 95 105 0 110
      Q -100 115 0 120
      L 0 140
      L 20 140
      L -20 140"
    fill="none"
    stroke="#0C5C4C"
    stroke-width="5"
  />
</svg>
```

Ici, nous avons une série de courbes de Bézier quadratiques (`Q`) où les points de contrôle s'éloignent de plus en plus du centre de l'arbre au fur et à mesure que le chemin descend.

## **Comment créer une cloche avec SVG**

Bien que la courbe de Bézier quadratique (`Q`) soit excellente pour courber une ligne, elle n'est souvent pas assez flexible.

Avec une courbe de Bézier cubique (`C`), nous n'avons pas un seul point de contrôle, mais deux. Le premier point de contrôle définit la direction initiale de la courbe et le second définit la direction par laquelle la courbe doit arriver à son point d'arrivée.

Si ces directions correspondent aux directions de la ligne avant et de la ligne après la courbe, nous obtenons une transition fluide entre les segments du chemin.

![Learn-SVG.008](https://www.freecodecamp.org/news/content/images/2021/12/Learn-SVG.008.jpeg)

Avec les courbes de Bézier cubiques, nous pouvons définir deux points de contrôle.

L'exemple suivant utilise à la fois des courbes de Bézier quadratiques et cubiques pour former une cloche. Ici, le bas de cette cloche est défini par des lignes droites. Ensuite, une courbe de Bézier quadratique commence le manteau de la cloche. Puis, une courbe de Bézier cubique continue fluidement la courbe quadratique pour former le sommet de la cloche. Enfin, nous atteignons la partie inférieure avec une autre courbe de Bézier quadratique.

![Learn-SVG.001-2](https://www.freecodecamp.org/news/content/images/2021/12/Learn-SVG.001-2.jpeg)

Exemple de cloche composé de différentes courbes et de lignes droites

```html
<svg width="200" height="200" viewBox="-100 -100 200 200">
  <g stroke="black" stroke-width="2">
    <circle cx="0" cy="-45" r="7" fill="#4F6D7A" />
    <circle cx="0" cy="50" r="10" fill="#F79257" />
    <path
      d="
        M -50 40
        L -50 50
        L 50 50
        L 50 40
        Q 40 40 40 10
        C 40 -60 -40 -60 -40 10   
        Q -40 40 -50 40"
      fill="#FDEA96"
    />
 </g>
</svg>
```

## Comment écrire du texte le long d'un chemin

Dessiner des formes n'est pas le seul cas d'utilisation des chemins. Nous pouvons également les utiliser pour restituer du texte le long d'un chemin invisible. Nous pouvons définir un chemin dans la section des définitions et l'utiliser dans un élément `textPath` pour que le texte fasse le tour du cercle. Ici, nous utilisons à nouveau un arc, mais vous pouvez utiliser n'importe quel autre chemin et le texte suivra le tracé.

![Screenshot-2023-11-30-at-21.21.27](https://www.freecodecamp.org/news/content/images/2023/11/Screenshot-2023-11-30-at-21.21.27.png)

Avec la propriété `text-path`, nous pouvons faire en sorte qu'un texte suive un chemin.

```html
<svg width="200" height="200" viewBox="-100 -100 200 200">
  <defs>
    <path id="text-arc" d="M 0, 50 A 50 50 0 1 1 1,50" />
  </defs>

  <text
    fill="#0c5c4c"
    font-family="Tahoma"
    font-size="0.77em"
    font-weight="bold"
  >
    <textPath href="#text-arc">
      Happy Holidays! Happy Holidays! Happy Holidays!
    </textPath>
  </text>
</svg>
```

## Comment animer un SVG avec CSS

Pour continuer notre exemple de forêt, nous pouvons ajouter un effet de neige avec une animation similaire. Nous pouvons animer la propriété `transform` depuis le CSS.

![Learn-SVG](https://www.freecodecamp.org/news/content/images/2023/11/Learn-SVG.gif)

Effet d'animation réalisé avec SVG et CSS

Nous étendons notre exemple de forêt avec de simples flocons de neige réutilisables et en ajoutons un certain nombre à la scène avec diverses classes CSS pour varier la vitesse et l'apparence. Ensuite, nous ajoutons l'animation en CSS pour qu'ils ressemblent à de la neige qui tombe. C'est un peu rudimentaire et ce n'est pas l'animation la plus sophistiquée, mais vous comprenez l'idée.

```html
<svg width="200" height="200" viewBox="-100 -100 200 200">
  <defs>
    <g id="tree">
      <polygon points="-10,0 10,0 0 -50" fill="#38755b" />
      <line x2="0" y2="10" stroke="#778074" stroke-width="2" />
    </g>
    <circle id="big" cx="0" cy="0" r="5" fill="white" />
    <circle id="small" cx="0" cy="0" r="3" fill="white" />
  </defs>

  <rect x="-100" y="-100" width="200" height="200" fill="#F1DBC3" />
  <circle cx="0" cy="380" r="350" fill="#F8F4E8" />

  <use href="#tree" x="-30" y="25" transform="scale(2)" />
  <use href="#tree" x="-20" y="40" transform="scale(1.2)" />
  <use href="#tree" x="40" y="40" />
  <use href="#tree" x="50" y="30" transform="scale(1.5)" />

  <use href="#big" x="0" y="0" class="flake fast" />
  <use href="#big" x="-50" y="-20" class="flake fast opaque" />
  <use href="#big" x="30" y="-40" class="flake fast" />
  <use href="#big" x="50" y="-20" class="flake fast opaque" />
  <use href="#big" x="30" y="50" class="flake slow" />
  <use href="#big" x="-70" y="-80" class="flake slow opaque" />
  <use href="#big" x="30" y="50" class="flake slow" />
  <use href="#big" x="90" y="-80" class="flake slow opaque" />
  <use href="#small" x="10" y="-50" class="flake slow" />
  <use href="#small" x="-50" y="-60" class="flake slow opaque" />
  <use href="#small" x="30" y="70" class="flake slow" />
  <use href="#small" x="10" y="-80" class="flake slow opaque" />
</svg>
```

```CSS
.flake {
  animation-duration: inherit;
  animation-name: snowing;
  animation-iteration-count: infinite;
  animation-timing-function: linear;
}

.flake.opaque {
  opacity: 0.7;
}

.flake.slow {
  animation-duration: 5s;
}

.flake.fast {
  animation-duration: 3s;
}

@keyframes snowing {
  from {
    transform: translate(0, -100px);
  }
  to {
    transform: translate(0, 100px);
  }
}
```

## Comment créer une horloge qui affiche l'heure réelle

Les éléments SVG peuvent être manipulés depuis JavaScript de la même manière que n'importe quelle autre balise HTML.

![Screenshot-2023-11-30-at-21.21.16](https://www.freecodecamp.org/news/content/images/2023/11/Screenshot-2023-11-30-at-21.21.16.png)

Exemple d'horloge réalisé avec SVG et JavaScript

Dans cet exemple, nous utilisons un court extrait de code pour afficher l'heure réelle sur une horloge. Nous accédons aux aiguilles des heures et des minutes en JavaScript avec `getElementById`, puis nous définissons leur attribut `transform` avec une rotation qui reflète l'heure actuelle. Ci-dessous, vous voyez le SVG réel affichant l'heure actuelle.

Pour un tutoriel plus détaillé sur la création d'une horloge avec SVG et JavaScript, consultez [Comment coder une montre animée][3].

```html
<svg width="200" height="200" viewBox="-100 -100 200 200">
  <rect x="-100" y="-100" width="200" height="200" fill="#CD803D" />

  <circle r="55" stroke="#FCCE7B" stroke-width="10" fill="white" />

  <circle
    r="45"
    stroke="#B6705F"
    stroke-width="6"
    stroke-dasharray="6 17.56194490192345"
    stroke-dashoffset="3"
    fill="none"
  />

  <g stroke="#5f4c6c" stroke-linecap="round">
    <line id="hours" y2="-20" stroke-width="8" />
    <line id="minutes" y2="-35" stroke-width="6" />
  </g>
</svg>
```

```javascript
window.addEventListener("DOMContentLoaded", () => {
  const hoursElement = document.getElementById("hours");
  const minutesElement = document.getElementById("minutes");

  const hour = new Date().getHours() % 12;
  const minute = new Date().getMinutes();

  hoursElement.setAttribute("transform", `rotate(${(360 / 12) * hour})`);
  minutesElement.setAttribute("transform", `rotate(${(360 / 60) * minute})`);
});
```

## Comment créer un diagramme basé sur des données avec SVG et React

Les SVG fonctionnent également très bien avec les bibliothèques frontend. Voici un exemple de composant React qui génère un diagramme piloté par des données.

Dans cet exemple, nous faisons deux choses. Nous générons une liste de rectangles pour créer un diagramme en colonnes basé sur des données arbitraires. Et nous générons également une série de coordonnées pour une polyligne (`polyline`).

![Screenshot-2023-11-30-at-21.21.32](https://www.freecodecamp.org/news/content/images/2023/11/Screenshot-2023-11-30-at-21.21.32.png)

Nous pouvons utiliser JavaScript pour générer un diagramme basé sur des données.

Pour des cas d'utilisation simples, vous pouvez coder votre propre diagramme comme celui-ci. Mais si vous avez besoin de diagrammes plus complexes, consultez la [bibliothèque D3][4]. La bibliothèque D3 utilise les SVG sous le capot pour créer toutes sortes de diagrammes.

```JavaScript
function Diagram() {
  const dataPoints = [3, 4, 7, 5, 3, 6];
  const sineWave = Array.from({ length: 115 })
    .map((item, index) => `${index - 55},${Math.sin(index / 20) * 20 + 10}`)
    .join(" ");

  return (
    <svg width="200" height="200" viewBox="-100 -100 200 200">
      {dataPoints.map((dataPoint, index) => (
        <rect
          key={index}
          x={index * 20 - 55}
          y={50 - dataPoint * 10}
          width="15"
          height={dataPoint * 10}
          fill="#CD803D"
        />
      ))}

      <polyline points={sineWave} fill="none" stroke="black" stroke-width="5" />
    </svg>
  );
}
```

## **Étapes suivantes – Rendre les SVG interactifs avec JavaScript**

Au premier abord, les SVG peuvent être assez déroutants. Beaucoup de coordonnées, de lettres et de paramètres étranges. Une fois que vous en comprenez les fondements, vous pouvez les utiliser à votre avantage et commencer à coder des images.

Et nous n'en sommes qu'au début. Ajouter JavaScript à l'ensemble introduira un tout nouveau niveau de possibilités.

Pour plus d'exemples, consultez [svg-tutorial.com][5] ou mon [tutoriel YouTube][6] avec 12 exemples supplémentaires sur l'utilisation des SVG pour votre prochain projet !

[

SVG Tutorial: Apprenez à créer des images, formes, animations SVG et plus encore

Explorez les fondamentaux des Scalable Vector Graphics (SVG). Apprenez à créer et manipuler des images SVG avec JavaScript, à les animer avec CSS. Ou inversez les choses et générez des graphiques à partir du code.

![favicon](http://svg-tutorial.com/favicon.ico)SVG Tutorial

![image](https://svg-tutorial.com/image.png)

][7]

<iframe width="356" height="200" src="https://www.youtube.com/embed/kBT90nwUb_o?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen="" title="Learn SVG through 24 examples" name="fitvid0"></iframe>

### **************Abonnez-vous pour plus de tutoriels sur le développement Web :**************

[

Hunor Márton Borbély

Développement de jeux avec JavaScript, tutoriels de codage créatif, HTML canvas, SVG, Three.js, et un peu de React et Vue https://twitter.com/HunorBorbelyhttps://codepen.io/HunorMarton…

![favicon_144x144](https://www.youtube.com/s/desktop/2ebf064d/img/favicon_144x144.png)YouTube

![APkrFKaQ34YAITK6J0qgy6Iv6pms35dPhF68Hyy7BoYoLA=s900-c-k-c0x00ffffff-no-rj](https://yt3.googleusercontent.com/ytc/APkrFKaQ34YAITK6J0qgy6Iv6pms35dPhF68Hyy7BoYoLA=s900-c-k-c0x00ffffff-no-rj)

][8]

[1]: https://svg-tutorial.com
[2]: https://youtu.be/kBT90nwUb_o
[3]: https://www.freecodecamp.org/news/svg-javascript-tutorial/
[4]: https://d3js.org/
[5]: https://svg-tutorial.com
[6]: https://www.youtube.com/watch?v=kBT90nwUb_o
[7]: http://svg-tutorial.com
[8]: https://www.youtube.com/channel/UCxhgW0Q5XLvIoXHAfQXg9oQ