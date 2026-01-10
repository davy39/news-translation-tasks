---
title: 'Amusons-nous avec CSS 3D : comment faire défiler sur l''axe z'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-21T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/css-3d-scrolling-on-the-z-axis-92503c3ecf3f
coverImage: https://cdn-media-1.freecodecamp.org/images/0*q_H371QLdCFefNpe.png
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: 'Amusons-nous avec CSS 3D : comment faire défiler sur l''axe z'
seo_desc: 'By Vincent Humeau

  In this article, we are going to create a small 3D scene, where the user can scroll
  on the z-axis. You can find the final code of this tutorial on GitHub, and the demo
  if you follow this link.

  This article assumes that you already h...'
---

Par Vincent Humeau

Dans cet article, nous allons créer une petite scène 3D, où l'utilisateur peut faire défiler sur l'axe z. Vous pouvez trouver le code final de ce tutoriel sur [GitHub](https://github.com/vinceumo/CSS-3D-Scrolling-z-axis-demo/), et la démonstration si vous suivez ce [lien](https://vinceumo.github.io/CSS-3D-Scrolling-z-axis-demo/).

Cet article suppose que vous avez déjà quelques connaissances sur CSS et JavaScript. Nous allons utiliser les propriétés personnalisées CSS, donc si vous n'êtes pas familier avec cela, vous pouvez lire [CSS custom properties — Cheatsheet](https://vinceumo.github.io/devNotes/css/2019/02/20/css-customs-properties.html).

![Image](https://cdn-media-1.freecodecamp.org/images/0*JtrdjIlxQY89vJM_.gif)

### Introduction à CSS 3D

Lorsque nous parlons de CSS 3D, nous parlons vraiment de CSS3 transform 3D. Cette méthode nous permet d'utiliser la propriété CSS `transform` pour définir la perspective ou la rotation sur l'axe z de nos éléments DOM.

> _La propriété CSS transform vous permet de faire pivoter, redimensionner, incliner ou translater un élément. Elle modifie l'espace de coordonnées du modèle de formatage visuel CSS. [transform — MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/transform)_

Pour être autorisé à rendre nos éléments Dom dans un espace 3D, nous devons examiner les propriétés suivantes :

* Perspective
* Perspective origin
* Transform Z

### Perspective

`perspective` est une propriété CSS qui définit la distance entre z=0 et l'utilisateur. Plus la valeur de perspective est petite, plus la distorsion de notre scène sera grande. (Essayez de changer la valeur de `scenePerspective` dans l'exemple codePen ci-dessous).

```
.container-scene { perspective: 100px; }
```

La valeur de `perspective` est une [unité de longueur](https://developer.mozilla.org/en-US/docs/Web/CSS/length).

![Image](https://cdn-media-1.freecodecamp.org/images/0*CP84t13H0eHbab3R.png)

Essayez de définir la valeur de `scenePerspective` à 0 et 70 dans l'exemple ci-dessous. Vous pouvez remarquer que notre cube n'a aucune perspective si sa valeur est définie à 0. Si la valeur est définie à 70, vous pouvez voir une distorsion vraiment forte de la perspective du cube. Plus la valeur de perspective est petite, plus elle est profonde.

%[https://codepen.io/vinceumo/pen/jdJLge]

Pour pouvoir rendre un espace 3D, nous devons spécifier `transform-style: preserve-3d;` sur les éléments enfants. Dans l'exemple ci-dessus, il est défini sur notre `.cube`. Par défaut, les éléments sont aplatis.

```css
.container-scene {   
  perspective: 400px; 
}  
.container-scene .cube {
  transform-style: preserve-3d; 
}
```

### Perspective origin

> _La propriété CSS `perspective-origin` détermine la position à laquelle le spectateur regarde. Elle est utilisée comme point de fuite par la propriété perspective. [MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/perspective-origin)_

Cette propriété nous permet essentiellement de déplacer le point de fuite de notre scène 3D.

```css
.container-scene { 
  perspective: 400px; 
  perspective-origin: 50% 100%; /*Valeur de position X, Valeur de position Y*/ 
} 

.container-scene .cube { 
  transform-style: preserve-3d; 
}
```

Pour les positions x et y, nous pouvons définir la position en utilisant des pourcentages. Mais nous pouvons également utiliser les valeurs suivantes :

Position x :

* `left` = 0%
* `center` = 50%
* `right` = 100%

Position y :

* `top` = 0%
* `center` = 50%
* `bottom` = 50%

![Image](https://cdn-media-1.freecodecamp.org/images/0*q_H371QLdCFefNpe.png)

Dans l'exemple suivant, vous pouvez changer la valeur de `perspectiveOriginX` et `perspectiveOriginY`.

%[https://codepen.io/vinceumo/pen/wOwzBY]

### Transform Z

Nous avons déjà mentionné précédemment que la propriété CSS `transform` nous permet de positionner nos éléments dans un espace 3D.

Transform offre différentes fonctions pour transformer nos éléments en 3D :

* rotateX(angle) — [MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function/rotateX)
* rotateY(angle) — [MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function/rotateY)
* rotateZ(angle) — [MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function/rotateZ)
* translateZ(tz) — [MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function/translateZ)
* scaleZ(sz) — [MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function/scaleZ)

Comme nous l'avons vu dans l'illustration dans la section `perspective`, `translateZ()` nous permet de positionner un élément le long de l'axe z de l'espace 3D. Alternativement, nous pouvons utiliser la fonction CSS `translate3D(x, y, z)`.

Dans l'exemple suivant, vous pouvez jouer avec la position de l'axe Z du `.cube` et `.face-` en changeant la valeur de `cubeTranslateZ` et `cubeFacesTranslateZ`.

%[https://codepen.io/vinceumo/pen/VRZKEB]

Maintenant que nous avons une bonne compréhension de comment fonctionne CSS 3D, nous allons créer une scène 3D, où nous allons pouvoir faire défiler sur l'axe z.

### Configurer la scène

Nous allons créer une page qui liste tous les films du Studio Ghibli. Chaque film sera une carte positionnée sur l'axe z de notre scène. N'hésitez pas à fork ou [télécharger](https://codepen.io/vinceumo/share/zip/JzaXqN) le codepen suivant comme matériel de départ pour suivre. J'utilise [axios](https://github.com/axios/axios) avec [Studio Ghibli API](https://ghibliapi.herokuapp.com/) pour remplir cette page.

%[https://codepen.io/vinceumo/pen/JzaXqN]

Si vous voulez suivre avec votre propre contenu, nous aurons besoin du balisage suivant :

```html
<div class="viewport">
  <div class="scene3D-container">
    <div class="scene3D">
      <div>Card1</div>
      <div>Card2</div>
      <!--Etc.-->
    </div>
  </div>
</div>
```

#### Styling

Tout d'abord, nous allons définir nos [propriétés personnalisées CSS](https://vinceumo.github.io/devNotes/css/2019/02/20/css-customs-properties.html) (variables CSS). Certaines de ces variables vont être transformées en utilisant JS. Elles vont nous aider à interagir avec la scène.

```css
:root {
 --scenePerspective: 1;
 --scenePerspectiveOriginX: 50;
 --scenePerspectiveOriginY: 30;
 --itemZ: 2; // Espace entre chaque carte
 --cameraSpeed: 150; // Où 1 est le plus rapide, cette variable est un facteur multiplicateur de --scenePerspective et --filmZ
 --cameraZ: 0; // Position initiale de la caméra 
 --viewportHeight: 0; // La hauteur du viewport nous permettra de définir la profondeur de notre scène 
}
```

`.viewport` nous permettra de définir la hauteur de la fenêtre. Nous l'utiliserons plus tard pour définir la profondeur de la scène et utiliser la barre de défilement pour naviguer sur l'axe z.

```css
.viewport { 
  height: calc(var(--viewportHeight) * 1px);
}
```

`.scene3D-container` définit la perspective de la scène et l'origine de la perspective. Il est positionné de manière fixe pour qu'il reste toujours à l'écran. Nous allons également définir l'origine de la perspective.

```css
.viewport .scene3D-container {
 position: fixed;
 top: 0;
 left: 0;
 width: 100%;
 height: 100%;
 perspective: calc(var(--scenePerspective) * var(--cameraSpeed) * 1px);
 perspective-origin: calc(var(--scenePerspectiveOriginX) * 1%) calc( var(--scenePerspectiveOriginY) * 1% );
 will-change: perspective-origin;
 transform: translate3d( 0, 0, 0 ); // Permet l'accélération matérielle CSS, donc les transitions sont plus fluides 
}
```

`.scene3D` définit la position de notre scène sur l'axe z. Cela se comportera un peu comme le déplacement d'une caméra sur l'axe z. Mais en réalité, nous déplaçons la scène et la caméra (viewport) est fixe. Dans le reste de cet article, nous allons utiliser la comparaison de la caméra. `.scene3D` prend la hauteur et la largeur complètes du viewport.

```css
.viewport .scene3D-container .scene3D { 
 position: absolute; top: 0;
 height: 100vh;
 width: 100%;
 transform-style: preserve-3d;
 transform: translateZ(calc(var(--cameraZ) * 1px));
 will-change: transform; 
}
```

Enfin, nous allons positionner nos cartes dans la scène. Tous les éléments sont positionnés de manière absolue. Les éléments impairs sont positionnés à gauche, les éléments pairs à droite.

Nous utilisons SCSS pour translater chaque élément de manière programmatique. Sur les axes **X** et **Y**, nous les translatons aléatoirement entre -25% et 25% pour X, entre -50% et 50% pour Y. Nous utilisons une boucle `@for` pour que chaque élément puisse être translaté sur l'axe **z** multiplié par leurs index.

```css
.viewport .scene3D-container .scene3D {
 > div { 
  position: absolute; 
  display: block; 
  width: 100%; 
  top: 40%; 
  @media only screen and (min-width: 600px) { 
    width: 45%; 
  } 
  &:nth-child(2n) { left: 0; } 
  &:nth-child(2n + 1) { right: 0; } 
  @for $i from 0 through 25 { 
   &:nth-child(#{$i}) { 
    transform: translate3D( random(50) - 25 * 1%, random(100) - 50 * 1%, calc(var(--itemZ) * var(--cameraSpeed) * #{$i} * -1px) ); 
   } 
  } 
 } 
}
```

Le CSS est maintenant terminé, et nous avons une scène 3D. Dans les parties suivantes de cet article, nous allons écrire du JavaScript qui nous permettra de naviguer dans la scène.

Pour pouvoir faire défiler, nous devons d'abord définir la valeur de `--viewportHeight` qui émule la profondeur de la scène.

%[https://codepen.io/vinceumo/pen/WmgxBG]

La profondeur de la scène est égale à l'addition des éléments suivants :

* La hauteur de la fenêtre utilisateur
* La perspective `.scene3D-container` = var(--scenePerspective) * var(--cameraSpeed)
* La valeur z translatée de notre dernier élément = var(--itemZ) * var(--cameraSpeed) * items.length

Créons une fonction `setSceneHeight()` qui mettra à jour la valeur de `--viewportHeight` au chargement.

```js
document.addEventListener("DOMContentLoaded", function() {
  setSceneHeight();
});

function setSceneHeight() {
  const numberOfItems = films.length; // Ou nombre d'éléments que vous avez dans `.scene3D`
  const itemZ = parseFloat(
    getComputedStyle(document.documentElement).getPropertyValue("--itemZ")
  );
  const scenePerspective = parseFloat(
    getComputedStyle(document.documentElement).getPropertyValue(
      "--scenePerspective"
    )
  );
  const cameraSpeed = parseFloat(
    getComputedStyle(document.documentElement).getPropertyValue("--cameraSpeed")
  );

  const height =
    window.innerHeight +
    scenePerspective * cameraSpeed +
    itemZ * cameraSpeed * numberOfItems;

  // Mettre à jour la valeur --viewportHeight
  document.documentElement.style.setProperty("--viewportHeight", height);
}
```

Notre page a maintenant une barre de défilement, mais nous ne pouvons toujours pas faire défiler. Nous devons ajouter un écouteur d'événement qui écoutera le défilement de l'utilisateur. L'événement de défilement appellera une fonction `moveCamera()`. Elle mettra à jour la valeur de `--cameraZ` avec la valeur de [window.pageYOffset](https://developer.mozilla.org/en-US/docs/Web/API/Window/pageYOffset).

```js
document.addEventListener("DOMContentLoaded", function() {
  window.addEventListener("scroll", moveCamera);
  setSceneHeight();
});

function moveCamera() {
  document.documentElement.style.setProperty("--cameraZ", window.pageYOffset);
}

function setSceneHeight() {
  // ...
}
```

%[https://codepen.io/vinceumo/pen/pYxpLW]

#### Déplacer l'angle de la caméra

Enfin, rendons notre scène un peu plus dynamique. Sur l'événement [mousemove](https://developer.mozilla.org/en-US/docs/Web/API/Element/mousemove_event), nous allons changer les valeurs de `scenePerspectiveOriginX` et `scenePerspectiveOriginY`. Cela donnera l'illusion que la caméra bouge. Les éléments resteront droits dans la scène. Si vous voulez donner un mouvement de rotation de caméra plus réaliste, vous pourriez appliquer [rotate3d()](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function/rotate3d) sur la scène.

Tout d'abord, nous allons stocker les valeurs initiales de ces deux variables dans un objet `perspectiveOrigin`. Nous allons définir une valeur `perspectiveOrigin.maxGap` qui va limiter les valeurs maximales et minimales des variables. Par exemple, si `scenePerspectiveOriginY` est égal à 50%. Sur mousemove, la nouvelle valeur sera entre 40% et 60%.

```js
const perspectiveOrigin = {
  x: parseFloat(
    getComputedStyle(document.documentElement).getPropertyValue(
      "--scenePerspectiveOriginX"
    )
  ),
  y: parseFloat(
    getComputedStyle(document.documentElement).getPropertyValue(
      "--scenePerspectiveOriginY"
    )
  ),
  maxGap: 10
};
```

Si le curseur de l'utilisateur est au centre de l'écran, nous allons définir les valeurs de `--scenePerspectiveOriginX` et `--scenePerspectiveOriginX` comme les valeurs initiales. Plus le curseur s'éloigne du centre, plus ces valeurs augmenteront/diminueront. Si l'utilisateur se déplace vers le coin supérieur gauche, les valeurs augmenteront, et dans le coin inférieur droit, elles diminueront.

La fonction `moveCameraAngle()` va mettre à jour les valeurs :

* `xGap` et `yGap` retournent la position de la souris de l'utilisateur en pourcentage sur les axes X et Y, par rapport au centre de la fenêtre.
* `newPerspectiveOriginX` et `newPerspectiveOriginY` retournent la nouvelle origine de la perspective.

```js
document.addEventListener("DOMContentLoaded", function() {
  window.addEventListener("scroll", moveCamera);
  window.addEventListener("mousemove", moveCameraAngle);
  setSceneHeight();
});

function moveCameraAngle(event) {
  const xGap =
    (((event.clientX - window.innerWidth / 2) * 100) /
      (window.innerWidth / 2)) *
    -1;
  const yGap =
    (((event.clientY - window.innerHeight / 2) * 100) /
      (window.innerHeight / 2)) *
    -1;
  const newPerspectiveOriginX =
    perspectiveOrigin.x + (xGap * perspectiveOrigin.maxGap) / 100;
  const newPerspectiveOriginY =
    perspectiveOrigin.y + (yGap * perspectiveOrigin.maxGap) / 100;

  document.documentElement.style.setProperty(
    "--scenePerspectiveOriginX",
    newPerspectiveOriginX
  );
  document.documentElement.style.setProperty(
    "--scenePerspectiveOriginY",
    newPerspectiveOriginY
  );
}
```

%[https://codepen.io/vinceumo/pen/NJEwwo]

Notre scène est maintenant terminée. J'espère que vous avez apprécié cet article.

### Ressources

* [perspective — Codrops](https://tympanus.net/codrops/css_reference/perspective/)
* [perspective — MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/perspective)
* [transform-style — Codrops](https://tympanus.net/codrops/css_reference/transform-style/)
* [transform-style — MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-style)
* [perspective-origin — MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/perspective-origin)
* [Things to Watch Out for When Working with CSS 3D — CSS-tricks](https://css-tricks.com/things-watch-working-css-3d/)

_Lisez plus de mes articles de blog sur [vinceumo.github.io](https://vinceumo.github.io/devNotes/css/2019/03/21/css-3d-scrolling-on-the-z-axis.html)._

* [Suivez-moi sur twitter](https://twitter.com/vince_umo)
* [Suivez-moi sur Github](https://github.com/vinceumo)
* [Suivez-moi sur dev.to](https://dev.to/vinceumo)