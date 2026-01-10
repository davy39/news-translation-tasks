---
title: Comment ajouter des anneaux de focus pour les interactions clavier uniquement
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-11T16:16:20.000Z'
originalURL: https://freecodecamp.org/news/focus-rings-for-keyboard-interactions-only
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca21e740569d1a4ca52b4.jpg
tags:
- name: a11y
  slug: a11y
- name: Accessibility
  slug: accessibility
- name: Design
  slug: design
- name: front end
  slug: front-end
- name: Front-end Development
  slug: front-end-development
- name: frontend
  slug: frontend
seo_title: Comment ajouter des anneaux de focus pour les interactions clavier uniquement
seo_desc: 'By Ben Robertson

  One thing that inevitably makes its way into our QA process on any project is the
  unexpected appearance of focus rings.


  A wild focus ring appeared!

  We’ve had a lot of discussions about how to handle these. The project manager and
  de...'
---

Par Ben Robertson

Une chose qui finit invariablement par faire son chemin dans notre processus de QA sur n'importe quel projet est l'apparition inattendue d'anneaux de focus.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/focus-ring.png)
_Un anneau de focus sauvage est apparu !_

Nous avons eu beaucoup de discussions sur la façon de les gérer. Le chef de projet et le designer suggèrent souvent de les supprimer. Bien que ce soit la solution facile, ce serait un **anti-pattern** de conception web. Les anneaux de focus par défaut sont fournis par tous les navigateurs afin que les utilisateurs de clavier puissent déterminer quel élément est actuellement en focus. En fait, **les anneaux de focus sont nécessaires pour répondre aux normes d'accessibilité** :

> Toute interface utilisateur exploitable par clavier possède un mode de fonctionnement où l'indicateur de focus du clavier est visible.
> - [**Directives d'accessibilité du contenu Web W3**](https://www.w3.org/TR/WCAG21/#focus-visible)

Même lorsque nous décidons de ne pas supprimer les anneaux de focus, les designers sont généralement mécontents des styles par défaut. Une question qui est récemment apparue est la suivante : si les styles d'anneaux de focus sont conçus pour que les utilisateurs de clavier puissent suivre le focus sur la page, pourquoi doivent-ils apparaître lorsque je clique sur un élément ? Peut-on ajouter des anneaux de focus uniquement pour les utilisateurs de clavier ?

La réponse est oui ! Nous pouvons utiliser le [**polyfill `:focus-visible`**](https://github.com/WICG/focus-visible) pour ajouter des anneaux de focus uniquement lorsque l'utilisateur navigue avec un clavier.

## **Comment utiliser le polyfill `:focus-visible`**

Voici comment vous pouvez implémenter `:focus-visible` dans vos projets dès maintenant.

Si vous utilisez des modules ES6, installez le polyfill via npm : `npm install --save focus-visible`

Importez le module dans votre fichier JavaScript principal :

```js
import 'focus-visible';

```

Lorsque votre page se charge, votre `<body>` recevra une classe `.js-focus-visible` afin que vous puissiez masquer conditionnellement les anneaux de focus par défaut uniquement si le polyfill est chargé. De plus, lorsque vous naviguez via le clavier, les éléments en focus recevront une classe `.focus-visible`.

Maintenant, nous pouvons ajouter notre CSS :

```css
// remplacer la feuille de style UA, uniquement lorsque le polyfill est chargé
.js-focus-visible :focus:not(.focus-visible) {
    outline-width: 0;
}

// établir l'apparence souhaitée de l'anneau de focus pour les modalités d'entrée appropriées
.focus-visible {
  outline: 2px solid $bright-brand-color;
}

```

## **Autres ressources**

* [**Polyfill `:focus-visible` sur Github**](https://github.com/WICG/focus-visible)
* [**Focus-ring sur A11y Casts**](https://www.youtube.com/watch?v=ilj2P5-5CjI&feature=youtu.be)
* [**Spécification de la pseudo-classe focus-visible du CSS Working Group**](https://drafts.csswg.org/selectors-4/#the-focus-visible-pseudo)

_Voulez-vous approfondir la création de sites web accessibles ? Rejoignez mon cours par email gratuit :_ 💡 [_**Erreurs courantes d'accessibilité et comment les éviter**_](https://benrobertson.io/courses/common-accessibility-mistakes/). 30 jours, 10 leçons, 100% amusant ! 💡 [_**Inscrivez-vous ici**_](https://benrobertson.io/courses/common-accessibility-mistakes/) !

_Cet article est initialement paru sur [benrobertson.io](https://benrobertson.io/accessibility/focus-ring-keyboard-only).