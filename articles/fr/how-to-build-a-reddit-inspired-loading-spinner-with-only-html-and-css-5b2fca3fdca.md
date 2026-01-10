---
title: Comment créer un indicateur de chargement inspiré de Reddit avec uniquement
  HTML et CSS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-19T17:48:42.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-reddit-inspired-loading-spinner-with-only-html-and-css-5b2fca3fdca
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Z6M1Fyrg8Hh_WKzMhSoWWg.jpeg
tags:
- name: animation
  slug: animation
- name: CSS
  slug: css
- name: Design
  slug: design
- name: 'tech '
  slug: tech
- name: UX
  slug: ux
seo_title: Comment créer un indicateur de chargement inspiré de Reddit avec uniquement
  HTML et CSS
seo_desc: 'By Daniel Miller

  Reddit’s mobile app has a rather striking loading spinner reminiscent of orbital
  bodies circling a planet or star. Most developers would reach for JavaScript or
  SVGs for a task like this, but thanks to [**animation-iteration-count**]...'
---

Par Daniel Miller

L'application mobile de [Reddit](https://www.reddit.com/) possède un indicateur de chargement plutôt frappant, rappelant des corps orbitaux tournant autour d'une planète ou d'une étoile. La plupart des développeurs utiliseraient JavaScript ou des SVGs pour une telle tâche, mais grâce à `[**animation-iteration-count**](https://developer.mozilla.org/en-US/docs/Web/CSS/animation-iteration-count)**: infinite;**` et quelques autres astuces, ce n'est même pas nécessaire. Aujourd'hui, je vais vous montrer comment coder un indicateur de chargement inspiré de Reddit purement en HTML et CSS !

Voici le résultat final :

%[https://codepen.io/bronzebygold/pen/YBEjKo]

### Installation de base

Commençons par écrire quelques éléments DOM HTML sur lesquels nous pouvons attacher le cercle central et chacune des orbites rotatives.

```html
<div class="center"></div>
<div class="inner-spin">
    
  ...
    
</div>
<div class="outer-spin">
    
  ...
    
</div>
```

Les éléments `**inner-spin**` et `**outer-spin**` seront les nœuds parents de tout ce qui doit être animé, et finalement nous appliquerons les transformations CSS [keyframes](https://developer.mozilla.org/en-US/docs/Web/CSS/@keyframes) à ces nœuds parents.

Dans l'exemple de code ci-dessus, les ellipses (`**…**`) représentent les arcs et les "lunes" en orbite. Les anneaux intérieur et extérieur contiennent chacun deux arcs et deux lunes, mais pour des raisons qui deviendront claires un peu plus tard, chaque arc est en fait composé de deux formes CSS, donc nous avons besoin d'un total de huit arcs et quatre lunes. Le HTML complet ressemble à ceci :

```html
<div class="center"></div>
<div class="inner-spin">
  
  <div class="inner-arc inner-arc_start-a"></div>
  <div class="inner-arc inner-arc_end-a"></div>
  <div class="inner-arc inner-arc_start-b"></div>
  <div class="inner-arc inner-arc_end-b"></div>
  
  <div class="inner-moon-a"></div>
  <div class="inner-moon-b"></div>
  
</div>
<div class="outer-spin">
  
  <div class="outer-arc outer-arc_start-a"></div>
  <div class="outer-arc outer-arc_end-a"></div>
  <div class="outer-arc outer-arc_start-b"></div>
  <div class="outer-arc outer-arc_end-b"></div>
  
  <div class="outer-moon-a"></div>
  <div class="outer-moon-b"></div>
  
</div>
```

### Formes CSS

Il est possible de dessiner des cercles et des arcs en CSS en créant simplement un `**<div>**` carré et en définissant `**border-radius**` à 50 %.

Chaque côté de la bordure peut prendre une couleur différente ou peut être défini comme `**transparent**`. La propriété `**background-color**` définit le remplissage de la forme, le cas échéant.

![Image](https://cdn-media-1.freecodecamp.org/images/1*JTLIoQelTfWNH6hAnctYNw.gif)

Il est facile de dessiner des arcs de 90, 180 et 270 degrés en définissant simplement un ou plusieurs côtés de la bordure comme transparents. Cependant, si vous regardez attentivement l'indicateur de chargement en haut de la page, vous remarquerez que la "queue" de chaque orbite laisse un espace entre elle-même et la lune derrière elle. Cela signifie que, bien que les longueurs d'arc soient proches de 180 degrés, elles sont un peu en dessous de 180.

Pour dessiner des segments de cercle de longueurs irrégulières en CSS, il faut un peu d'astuce. Pour ce faire, nous devons dessiner deux segments d'arc adjacents de 90 degrés et faire légèrement tourner l'un d'eux afin qu'ils se chevauchent, laissant un segment d'arc apparent d'environ 160 degrés.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Xp49-EB_PhfgzkkztEeBIA.gif)

En revenant au HTML, vous pouvez maintenant deviner pourquoi nous avons défini deux nœuds pour chaque arc (un `**arc_start**` et un `**arc_end**`). Ceux-ci seront utilisés pour représenter chaque partie d'un arc chevauchant unique représentant la queue de chaque orbite.

### Configuration du CSS

Pour commencer, nous allons définir une [variable CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_variables) pour représenter la couleur de l'indicateur de chargement et une autre variable pour représenter une translation de -50 %, -50 % que nous utiliserons dans tout le CSS pour centrer les formes autour de leur centre (par opposition à leur coin supérieur gauche, qui est la valeur par défaut).

```css
html {
  --spinner: #1EAAF0;
  --center: translate(-50%, -50%);
}
```

Maintenant, nous pouvons dessiner le cercle central.

```css
.center {
   position: absolute;
   width: 30px;
   height: 30px;
   background: var(--spinner);
   border-radius: 50%;
   top: 50%;
   left: 50%;
   transform: var(--center); 
}
```

Les nœuds enfants pour chaque orbite sont enfermés dans des nœuds parents appelés `**inner-spin**` et `**outer-spin**`. Pour l'instant, nous les utiliserons simplement pour centrer l'indicateur de chargement dans la fenêtre.

```css
.outer-spin, .inner-spin {
  position: absolute;
  top: 50%;
  left: 50%;
}
```

### Dessin des orbites

L'indicateur de chargement est essentiellement une série de cercles concentriques, donc concentrons-nous d'abord sur le dessin d'un seul arc.

Puisque chaque arc se compose de deux sections qui se chevauchent, commençons par dessiner simplement deux arcs côte à côte.

```css
.inner-arc {
  width: 62px;
  height: 62px;
}
.inner-arc_start-a {
  border-color: transparent transparent transparent green;
  /* NOTE: l'ordre ici est très important ! */
  transform: var(--center) rotate(0deg); 
}
.inner-arc_end-a {
  border-color: red transparent transparent transparent;
  transform: var(--center) rotate(0deg);
}
```

La première transformation centre le `**<div>**` dans la fenêtre. La rotation est définie à zéro degré pour montrer l'état par défaut des arcs.

![Image](https://cdn-media-1.freecodecamp.org/images/1*WVV1hXzRU69KP1SQEzcEQQ.png)
_Les arcs étant formés à partir des quatre bordures d'un &lt;div&gt; carré, les arcs ne s'alignent pas avec les quadrants cartésiens par défaut._

Remarquez que les arcs ne s'alignent pas avec les croisements x sur le cercle unitaire. Pour corriger cela, et pour faciliter le travail avec les arcs, nous faisons tourner les arcs de 45 degrés. Ensuite, nous faisons légèrement tourner l'un des arcs pour créer une longueur d'arc totale d'environ 160 degrés.

```css
.inner-arc_start-a {
  border-color: transparent transparent transparent green;
  transform: var(--center) rotate(65deg); 
}
.inner-arc_end-a {
  border-color: red transparent transparent transparent;
  transform: var(--center) rotate(45deg);
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*v08tgh4nmhLyhTTClXOtTQ.png)
_Arc de 160 degrés qui se chevauche, tourné pour s'aligner avec (1, 0) sur le cercle unitaire._

Ensuite, nous pouvons positionner l'une des lunes orbitales en la déplaçant le long de l'axe des x. Malheureusement, contrairement aux graphiques vectoriels tels que les SVGs, les bordures CSS ne sont pas des [vecteurs sans largeur](https://en.wikipedia.org/wiki/Vector_graphics) qui acceptent un style de trait. Cela signifie que les distances ne sont pas automatiquement mesurées jusqu'au point central de la ligne. Nous devons prendre en compte la largeur de la bordure lors du positionnement des objets.

Cela entraîne quelques "[nombres magiques](https://en.wikipedia.org/wiki/Magic_number_(programming))" que nous pourrions probablement minimiser si nous voulions définir plus de variables CSS et utiliser la fonction `[calc()](https://developer.mozilla.org/en-US/docs/Web/CSS/calc)`. Cela semble un peu compliqué, donc je vais simplement positionner le cercle par valeur de pixel pour l'instant.

```css
.inner-moon-a {
   position: absolute;
   top:50%;
   left:50%;
   width: 12px;
   height: 12px;
   background: red;
   border-radius: 50%;
   transform: var(--center) translate(33px, 0); 
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*FneDYHF3opdCPZ7MsXBPew.png)
_Première lune alignée avec sa queue._

Ensuite, nous dessinons deux autres arcs, mais cette fois nous utilisons la transformation `scale(-1, -1)`. Cela inverse les arcs à travers les axes x et y, reflétant essentiellement la traînée.

```css
.inner-arc_start-b {
  border-color: transparent transparent transparent var(--spinner); 
  transform: var(--center) rotate(65deg) scale(-1, -1);
}
.inner-arc_end-b {
  border-color: var(--spinner) transparent transparent transparent;
  transform: var(--center) rotate(45deg) scale(-1, -1);
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*HcFpXOJ1DG3E0_aoqInbyg.png)

Enfin, pour l'orbite extérieure, nous répétons simplement le CSS de l'orbite intérieure mais définissons une hauteur et une largeur de `**<div>**` plus grandes ! (Imaginez à quel point ce CSS pourrait être court avec des [mixins SASS](https://scotch.io/tutorials/how-to-use-sass-mixins) !)

```css
.outer-arc {
  width: 100px;
  height: 100px;
}
```

### Ajout de l'animation

La dernière étape consiste à ajouter une animation. Tout d'abord, nous devons ajouter un seul élément keyframes qui définit le type de comportement d'animation et le ou les éléments CSS affectés par l'animation, dans ce cas, la rotation via une propriété `**transform**`.

```css
@keyframes spin { 100% {transform: rotate(360deg); } }
```

L'identifiant "`**spin**`" connecte les keyframes aux attributs d'animation que nous allons ajouter dans chaque élément parent `**<div>**`. La propriété d'animation définit les informations temporelles pour l'animation, ce qui signifie que chaque orbite orbitera à une vitesse différente.

```css
.outer-spin {
  animation: spin 4s linear infinite;
}
.inner-spin {
  animation: spin 3s linear infinite;
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*Z6M1Fyrg8Hh_WKzMhSoWWg.jpeg)
_([Source de l'image.](https://commons.wikimedia.org/wiki/File:Planetarium_in_Putnam_Gallery_2,_2009-11-24.jpg" rel="noopener" target="_blank" title="))_

### C'est tout !

Le code de ce tutoriel peut être trouvé [sur CodePen.io](https://codepen.io/bronzebygold/pen/bOyMQy). Veuillez commenter — ou tweeter à [@PleathrStarfish](https://twitter.com/PleathrStarfish) — si vous avez une suggestion, une observation ou une version modifiée intéressante de mon code !