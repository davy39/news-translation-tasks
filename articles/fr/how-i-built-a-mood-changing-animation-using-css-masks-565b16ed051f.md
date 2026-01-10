---
title: Comment j'ai créé une animation de changement d'humeur en utilisant des masques
  CSS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-02T17:02:26.000Z'
originalURL: https://freecodecamp.org/news/how-i-built-a-mood-changing-animation-using-css-masks-565b16ed051f
coverImage: https://cdn-media-1.freecodecamp.org/images/0*tTAVggfIn612FqCu
tags:
- name: CSS
  slug: css
- name: image masking
  slug: image-masking
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment j'ai créé une animation de changement d'humeur en utilisant des
  masques CSS
seo_desc: 'By Ankit Karnany

  Remember the cartoons we used to watch during our childhood? At that time they were
  the epitome of animations. Nowadays, animations aren’t just limited to cartoons
  — we come across them almost everyday when we check our phone or look...'
---

Par Ankit Karnany

Vous souvenez-vous des dessins animés que nous regardions pendant notre enfance ? À cette époque, ils étaient l'apogée des animations. De nos jours, les animations ne se limitent plus aux dessins animés — nous en rencontrons presque tous les jours lorsque nous consultons notre téléphone ou regardons un appareil avec un écran.

Aujourd'hui, l'animation est utilisée non seulement pour attirer l'attention, mais aussi pour améliorer l'expérience utilisateur et guider le flux utilisateur. Dans tout bon design, les animations sont ajoutées de manière à s'intégrer au flux commun, créant ainsi une expérience utilisateur fluide.

Alors, dans cet article, nous allons créer une simple animation d'un visage avec différentes expressions, et nous apprendrons un peu de CSS dans ce processus.

### Installation

Nous allons utiliser une technique CSS qui est quelque peu rare parmi les développeurs web, mais que les designers utilisent assez souvent. Elle s'appelle le **masquage**.

Alors, à quoi pensez-vous lorsque vous entendez "masque" ?

Vous imaginez probablement une couverture sur quelque chose. C'est tout ce que nous devons comprendre.

Attendez — mais cet article est lié à la programmation et à l'utilisation de l'animation CSS...

Ne vous inquiétez pas ! Nous allons y venir.

### Création du masque de base

Disons que nous avons un `<div>` avec un `background: green;` et qu'il ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/2XO9bGq7nwPzRnJwEVIGM18CnBW1sMXO0Hav)

Maintenant, disons que j'ai un `face.svg` :

![Image](https://cdn-media-1.freecodecamp.org/images/rtGKXNWrhwS0GfhGmUpb228Tu137Z4FvgMkc)

Si nous appliquons une propriété CSS `mask-image: url(face.svg);` sur le `<div>`, vous serez émerveillé de voir ce que nous obtenons :

![Image](https://cdn-media-1.freecodecamp.org/images/vKQ3qFzMOVQLuHbur4KZ19hm5Rn7PMfGtmoq)

Vous pensez peut-être que quelque chose cloche ici. Le `face.svg` a été placé sur le `<div>`, mais il a pris la couleur du `background`. C'est l'inverse de ce que vous auriez pu attendre. Cela se produit à cause de la propriété `mask-type` qui rend la partie opaque du svg transparente. Cela permet à la couleur de fond d'être visible.

Ne nous attardons pas là-dessus pour l'instant. Gardez simplement à l'esprit que nous pouvons utiliser `background-color` pour changer la couleur du masque. Si vous êtes familier avec les différentes façons d'utiliser `background-color`, nous pouvons également utiliser des dégradés et écrire un simple dégradé qui remplit en rouge au centre et se répand radialement en noir vers l'extérieur. Le code pour cela est le suivant :

```
background-image: -webkit-radial-gradient( hsla(0, 100%, 50%, .7), hsla(0, 100%, 20%, .8), hsla(0, 100%, 10%, 1));
```

Ce qui donne ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/aX8BzmkSrurnCCGxBX6B1FTTfk0RA35SNVxe)

### Ajout de l'animation

Maintenant, ajoutons un peu d'animation à ce visage vide. Pour cela, j'ai `expression.svg` qui ressemble à l'image ci-dessous. Pour simplifier, j'ai créé tous les svgs avec la même largeur et la même hauteur, afin que nous évitions d'aligner manuellement le visage et l'expression.

![Image](https://cdn-media-1.freecodecamp.org/images/SOtVpTHeSekjDBcZsh2fJWOnLoYPRe6CQvNg)

Maintenant, `mask-image` a cette option cool qui permet d'utiliser plusieurs images comme masques. Nous pouvons donc faire ceci : `mask-image: url(face.svg), url(expression.svg);`. Voici ce que nous avons maintenant :

![Image](https://cdn-media-1.freecodecamp.org/images/A6H-X9gCRAHHBWFo62WsClZqPbsqGgTrl0U4)

L'une des propriétés les plus importantes des masques CSS est `mask-position`, qui positionne le masque à partir du coin supérieur gauche par rapport à son parent. Et je peux positionner plusieurs masques en utilisant la propriété `mask-position` tout comme `mask-image`.

Ainsi, pour rendre le visage triste, nous pouvons utiliser quelque chose comme ceci : `mask-position: 0 0, 0 12px;`. Et le résultat est le suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/G3LPJQJhJulrprRLpA6-3abAq1L1-sv319pp)

La première position `0 0` est pour le `face.svg`, et la seconde `0 12px` est pour le `expression.svg`. Cela le pousse de **12px** depuis le haut et donne l'expression ci-dessus.

#### Application de la fonctionnalité

Maintenant, animons ces expressions au survol. Le code complet que nous obtenons après avoir appliqué la pseudo-classe hover est le suivant :

```
i {  background-image: -webkit-radial-gradient(hsla(0, 100%, 50%, .7), hsla(0, 100%, 20%, .8) 60%, hsla(0, 100%, 10%, 1));
    mask-image: url('face.svg'), url('expression.svg');
  mask-position: 0 0, 0 12px; /* Pour faire l'expression triste */
```

```
  transition: mask-position .5s ease-out;}
```

```
i:hover {  background-image: -webkit-radial-gradient(hsla(120, 100%, 50%, .7), hsla(120, 100%, 20%, .8) 60%, hsla(120, 100%, 10%, 1));
```

```
  mask-position: 0 0, 0 0; /* Pour faire l'expression heureuse */
```

```
  transition: mask-position .1s linear;}
```

Après avoir joué un peu plus avec le CSS, nous pouvons faire ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/ipIKP8u6LWV6ikxw-HJv-1xrJWBYPYXQfqOv)

C'est l'une des méthodes que nous pouvons utiliser pour créer ces animations captivantes que nous rencontrons presque quotidiennement.

#### **Une note importante**

Les propriétés de masquage peuvent ne pas fonctionner dans tous les navigateurs. Pour les faire fonctionner dans tous les navigateurs, ajoutez simplement des préfixes spécifiques aux navigateurs comme `-webkit-`, `-moz-` et `-o-`.

Vous pouvez consulter le code complet ici sur [github](https://github.com/nktkarnany/mask-css) et [codepen](https://codepen.io/nktkarnany/pen/bjmZOQ).

Merci d'avoir lu ! J'espère que vous avez appris quelque chose.