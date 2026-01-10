---
title: 'Comment créer un générateur de mèmes avec React : un guide pour débutants'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-23T22:35:09.000Z'
originalURL: https://freecodecamp.org/news/react-for-beginners-building-a-meme-maker-with-react-7164d3d3e55f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*aMS4AGU5IYWp5F_AglY1Mw.gif
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: 'Comment créer un générateur de mèmes avec React : un guide pour débutants'
seo_desc: 'By Avanthika Meenakshi

  If you’re in the middle of learning React, you have probably already been through
  lots of tutorials on how to build a to-do list. At some point, you’ll look for alternate
  ideas to try and learn but you’ll keep bumping into diff...'
---

Par Avanthika Meenakshi

Si vous êtes en train d'apprendre React, vous avez probablement déjà suivi de nombreux tutoriels sur la création d'une liste de tâches. À un moment donné, vous chercherez des idées alternatives à essayer et à apprendre, mais vous continuerez à tomber sur différentes versions de l'exemple par défaut de la liste de tâches.

Cette idée alternative dans cet article est pour vous, les curieux. Le [codebase](https://github.com/AvanthikaMeenakshi/SpecialProject) peut être trouvé dans mon GitHub et il est initialisé à partir de [create-react-app](https://github.com/facebook/create-react-app). J'ai collecté des modèles de mèmes à partir de Google et d'autres sources. La police [Impact](https://www.wfonts.com/font/impact) peut transformer n'importe quelle image en mème, nous n'avons donc pas le choix de l'ajouter.

![Image](https://cdn-media-1.freecodecamp.org/images/1*aMS4AGU5IYWp5F_AglY1Mw.gif)

C'est un bon projet pour apprendre en faisant. Nous allons gérer de nombreux écouteurs d'événements/interactions utilisateur et mutations d'état.

### Construction de la galerie

Initialement, nous allons construire une galerie d'images pour permettre aux utilisateurs de sélectionner un modèle de mème. J'ai stocké les images que j'ai collectées sous forme de tableau, et je construis une simple galerie à partir de celui-ci.

Dans le code suivant,

1. Nous parcourons le tableau de photos, affichons chaque modèle de mème dans une balise img, et affichons une galerie.
2. Nous déterminons l'image actuellement sélectionnée via un [onClick](https://developer.mozilla.org/en-US/docs/Web/API/GlobalEventHandlers/onclick) sur la balise img.
3. Nous avons un objet initialState avec les paramètres initiaux des légendes et de leur positionnement. La position, le contenu et le statut de glisser-déposer des textes supérieur et inférieur peuvent être modifiés plus tard en déclenchant des mutations d'état.

Comme vous pouvez le comprendre, chaque image de la galerie a son propre événement onClick. Il trouve l'image actuellement sélectionnée, la convertit en [data URI](https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/toDataURL) et ouvre un [modal reactstrap](https://reactstrap.github.io/components/modals/). Le modal va être la station de travail pour créer le mème.

![Image](https://cdn-media-1.freecodecamp.org/images/1*GFJl-clGHoPntYWE11nDsQ.gif)
_Galerie de modèles de mèmes et la station de travail modale._

#### La station de travail du générateur de mèmes

Nous utilisons les balises [svg](https://developer.mozilla.org/en-US/docs/Web/SVG/Element/svg), [image](https://developer.mozilla.org/en-US/docs/Web/SVG/Element/image) et [text](https://developer.mozilla.org/en-US/docs/Web/SVG/Element/text) à l'intérieur du modal pour contenir l'image et la légende du mème. Nous préférons SVG car vous pouvez zoomer et dézoomer autant que vous le souhaitez, et cela ne perdra jamais en clarté. Et convertir SVG en PNG lors de l'exportation du mème est une tâche relativement simple.

Chaque image de la collection a une hauteur et une largeur différentes. Pour éviter d'étirer et de compresser l'image, je fais un petit contour pour fixer le rapport d'aspect. Je fixe la largeur à 600, et je calcule la hauteur en fonction du rapport largeur-hauteur. Je fournis la hauteur et la largeur calculées au SVG.

La structure globale à l'intérieur du SVG est assez simple. Il contient l'image et les légendes.

```
<svg width={newWidth} height={newHeight} ...otherAttributes>  <image xlinkHref="image-path" />  <text x="top-x-position" y="top-y-position">    {this.state.toptext}  </text>  <text x="bottom-x-position" y="bottom-y-position">    {this.state.bottomtext}  </text>  // Et nous aurons des écouteurs d'événements attachés aux balises <text /> pour les déplacer. Nous verrons cela dans la partie suivante de l'article.</svg>
```

Les coordonnées x et y des balises <text /> supérieur et inférieur sont maintenues dans l'état (référez-vous à l'objet initialState dans le composant MemeMaker). Lorsque l'utilisateur fait glisser et positionne les balises de texte, les coordonnées X et Y changent.

**_Note:_** _L'attribut xlinkHref de la balise image sera un chemin intégré (base64). Les URL src brutes ne peuvent pas être converties en PNG lors du téléchargement._

Voici à quoi ressemble tout le code :

En plus du SVG, nous avons deux balises <input /> pour permettre à l'utilisateur de saisir leurs légendes supérieure et inférieure pour le mème[. L'événement on](https://developer.mozilla.org/en-US/docs/Web/API/GlobalEventHandlers/onchange)Change capture la légende supérieure et inférieure, et les définit dans l'état au fur et à mesure que nous les changeons.

![Image](https://cdn-media-1.freecodecamp.org/images/1*l0v02K14blU_QniCY_f5jg.gif)
_? Nous avons la modification de texte qui fonctionne !_

#### Déplacer le texte !

Essayons de repositionner les légendes supérieure et inférieure maintenant. Les interactions de glisser-déposer des balises de texte sont liées à des écouteurs d'événements.

1. Appui de la souris — [onMouseDown](https://developer.mozilla.org/en-US/docs/Web/API/GlobalEventHandlers/onmousedown) — Trouve la balise de texte sélectionnée, détermine les positions X et Y actuelles, et attache un écouteur d'événement "mousemove" à celle-ci.
2. Mouvement de la souris — [onMouseMove](https://developer.mozilla.org/en-US/docs/Web/API/GlobalEventHandlers/onmousemove) — Trouve la position actuelle (x et y) de la balise de texte lorsque la souris est maintenue et déplacée.
3. Relâchement de la souris — [onMouseUp](https://developer.mozilla.org/en-US/docs/Web/API/GlobalEventHandlers/onmouseup) — Trouve la position de dépôt ou de relâchement. Détermine les coordonnées X et Y où le texte est déposé. Supprime l'écouteur d'événement "mousemove" de l'élément et termine le glisser-déposer.

Pour suivre l'appui, le maintien et le glisser de la souris. Nous incluons les écouteurs d'événements suivants aux balises de texte.

```
onMouseDown={event => this.handleMouseDown(event, 'top')}onMouseUp={event => this.handleMouseUp(event, 'top')}
```

Nous attachons ensuite l'écouteur d'événement "mousemove" pour suivre les mouvements de la souris lors du "mousedown". Une fois que la balise de texte est déposée, nous supprimons l'écouteur d'événement de mouvement de la souris attaché dans "mouseup".

Voici comment le code fait cela :

Maintenant que le glisser-déposer est terminé, vous pouvez déplacer votre texte et le repositionner où vous le souhaitez.

![Image](https://cdn-media-1.freecodecamp.org/images/1*J7ZoFB8DCXSeoC6io7uYbg.gif)
_Les écouteurs d'événements à la rescousse ! ?_

#### Télécharger le mème

Lorsque l'utilisateur clique sur le bouton de téléchargement, nous convertissons le SVG en une chaîne XML sérialisée et le dessinons dans un [canvas HTML5](https://www.w3schools.com/html/html5_canvas.asp). Nous utilisons la méthode toDataUrl() du canvas html (génère une URI d'image base64) pour générer une image de type mime "image/png" !

![Image](https://cdn-media-1.freecodecamp.org/images/1*3WBImygi1rpu_KO0XB3qwA.gif)
_Yaayyyy !_

À mesure que vous apprenez davantage, il y a beaucoup plus de choses que vous pouvez faire à ce petit projet.

1. Vous pouvez essayer de récupérer des images à partir d'API open source et construire une galerie.
2. Vous pouvez essayer d'ajouter des provisions pour les partager sur Facebook, WhatsApp et Twitter.
3. Vous pouvez essayer de permettre à l'utilisateur de télécharger sa propre image, de la redimensionner et de créer un mème.
4. Vous pouvez essayer de redimensionner la police.

Il y a beaucoup plus de choses que vous pouvez faire pour améliorer le projet, ce qui améliorera finalement vos compétences en codage. ? Bon codage ! ?