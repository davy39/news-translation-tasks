---
title: Comment utiliser les animations en CSS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-06T23:42:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-animations-in-css
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9cbb740569d1a4ca33e0.jpg
tags:
- name: animations
  slug: animations
- name: CSS
  slug: css
- name: toothbrush
  slug: toothbrush
seo_title: Comment utiliser les animations en CSS
seo_desc: 'Using CSS Animations

  CSS animations add beauty to the webpages and make transitions from one CSS style
  to the other beautiful.

  To create a CSS animation sequence, we have different sub-properties in the animation
  property in CSS :


  animation-delay

  an...'
---

## **Utilisation des animations CSS**

Les animations CSS ajoutent de la beauté aux pages web et rendent les transitions d'un style CSS à un autre magnifiques.

Pour créer une séquence d'animation CSS, nous avons différentes sous-propriétés dans la propriété `animation` en CSS :

* `animation-delay`
* `animation-direction`
* `animation-duration`
* `animation-iteration-count`
* `animation-name`
* `animation-play-state`
* `animation-timing-function`
* `animation-fill-mode`

## Exemple de séquence d'animation CSS pour déplacer du texte à travers l'écran

Dans la partie HTML, nous aurons un `div` avec la classe `container` et un `h3` avec le texte `Hello World` :

```html
<div class="container">
    <h3> Bonjour le monde ! </h3>
</div>
```

Pour la partie CSS :

```css
.container {
    /* Nous allons définir la largeur, la hauteur et le padding du conteneur */
    /* Le text-align à center */
    width: 400px;
    height: 60px;
    padding: 32px;
    text-align: center;

    /* Utiliser l'animation `blink` pour répéter indéfiniment pendant une durée de 2,5s */
    animation-duration: 2.5s;           
    animation-iteration-count: infinite;
    animation-direction: normal;        
    animation-name: blink;              
    
    /* La même chose peut être écrite en raccourci comme */
    /* ------------------------------------------------- */
    /* animation: 2.5s infinite normal blink;           */
}
@keyframes blink {
    0%, 100% {              /* Définit les propriétés à ces frames */
        background: #333;
        color: white;
    }

    50% {                   /* Définit les propriétés à ces frames */
        background: #ccc;
        color: black;
        border-radius: 48px;
    }
}
```

![Imgur](https://imgur.com/sczZjwm.gif)

## Plus d'informations sur les animations CSS :

* [Une introduction rapide aux animations CSS](https://www.freecodecamp.org/news/a-quick-introduction-to-css-animations-a1655375ec90/)