---
title: 'HTML5 Vidéo : Comment intégrer une vidéo dans votre HTML'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-27T00:43:00.000Z'
originalURL: https://freecodecamp.org/news/html5-video
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d71740569d1a4ca37cc.jpg
tags:
- name: HTML
  slug: html
- name: HTML5
  slug: html5
- name: video
  slug: video
seo_title: 'HTML5 Vidéo : Comment intégrer une vidéo dans votre HTML'
seo_desc: 'Before HTML5, in order to have a video play on a webpage, you would need
  to use a plugin like Adobe Flash Player. With the introduction of HTML5, you can
  now place videos directly into the page itself.

  This makes it possible to have videos play on pa...'
---

Avant HTML5, pour lire une vidéo sur une page web, il fallait utiliser un plugin comme Adobe Flash Player. Avec l'arrivée de HTML5, vous pouvez désormais placer des vidéos directement dans la page elle-même.

Cela permet de lire des vidéos sur des pages conçues pour les appareils mobiles, car les plugins comme Adobe Flash Player ne fonctionnent pas sur Android ou iOS.

L'élément HTML `<video>` est utilisé pour intégrer des vidéos dans les documents web. Il peut contenir une ou plusieurs sources vidéo, représentées à l'aide de l'attribut `src` ou de l'élément [source](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/source).

Pour intégrer un fichier vidéo, ajoutez simplement ce snippet de code et changez le `src` par le chemin de votre fichier vidéo :

```html
<video controls>
  <source src="tutorial.ogg" type="video/ogg">
  <source src="tutorial.mp4" type="video/mpeg">
  Votre navigateur ne prend pas en charge l'élément vidéo. Veuillez le mettre à jour vers la dernière version.
</video>
```

L'élément `<video>` est pris en charge par tous les navigateurs modernes. Cependant, tous les navigateurs ne supportent pas le même format de fichier vidéo. Les fichiers MP4 sont le format le plus largement accepté, et d'autres formats comme WebM et Ogg sont supportés dans Chrome, Firefox et Opera.

Pour vous assurer que votre vidéo est lue dans la plupart des navigateurs, il est recommandé de les encoder à la fois en Ogg et en MP4, et d'inclure les deux dans l'élément `<video>` comme dans l'exemple ci-dessus. Les navigateurs utiliseront le premier format reconnu.

Si, pour une raison quelconque, le navigateur ne reconnaît aucun des formats, le texte "Votre navigateur ne prend pas en charge l'élément vidéo. Veuillez le mettre à jour vers la dernière version" sera affiché à la place.

Vous avez peut-être également remarqué `controls` dans la balise `<video>`. Cet élément inclut de nombreux attributs utiles pour personnaliser l'expérience de lecture.

## Attributs de `<video>`

### `controls`

L'attribut `controls` gère l'affichage des contrôles tels que le bouton lecture/pause ou le curseur de volume.

Il s'agit d'un attribut booléen, ce qui signifie qu'il peut être défini sur vrai ou faux. Pour le définir sur vrai, il suffit de l'ajouter à la balise `<video>`. S'il n'est pas présent dans la balise, il sera défini sur faux et les contrôles n'apparaîtront pas.

#### `autoplay`

"autoplay" peut être défini sur vrai ou faux. Vous le définissez sur vrai en l'ajoutant à la balise ; s'il n'est pas présent dans la balise, il est défini sur faux. Si défini sur vrai, la vidéo commencera à lire dès qu'une partie suffisante de la vidéo aura été mise en mémoire tampon pour pouvoir être lue. De nombreuses personnes trouvent les vidéos en lecture automatique perturbantes ou ennuyeuses. Utilisez donc cette fonctionnalité avec parcimonie. Notez également que certains navigateurs mobiles, comme Safari pour iOS, ignorent cet attribut.

Il s'agit d'un autre attribut booléen. En incluant `autoplay` dans la balise `<video>`, la vidéo intégrée commencera à lire dès qu'une partie suffisante aura été mise en mémoire tampon.

```html
<video autoplay>
  <source src="video.mp4" type="video/mp4">
</video>
```

Gardez à l'esprit que de nombreuses personnes trouvent les vidéos en lecture automatique perturbantes ou ennuyeuses, alors utilisez cette fonctionnalité avec parcimonie. Notez également que certains navigateurs mobiles comme Safari pour iOS ignorent complètement cet attribut.

#### `poster`

L'attribut `poster` est l'image qui s'affiche sur la vidéo jusqu'à ce que l'utilisateur clique pour la lire.

```html
<video poster="poster.png">
  <source src="video.mp4" type="video/mp4">
</video>
```

### Les vidéos peuvent être coûteuses

Bien qu'il soit plus facile que jamais d'inclure des vidéos sur votre page, il est souvent préférable de télécharger vos vidéos sur un service comme YouTube, Vimeo ou Wistia et d'intégrer leur code à la place. Cela est dû au fait que la diffusion de vidéos peut être coûteuse, tant pour vous en termes de coûts de serveur que pour vos spectateurs s'ils ont des forfaits de données limités.

L'hébergement de vos propres fichiers vidéo peut également entraîner des problèmes de bande passante, ce qui pourrait signifier un chargement lent ou saccadé des vidéos. En outre, les navigateurs varient souvent en qualité en ce qui concerne la lecture vidéo, il est donc difficile de contrôler exactement ce que vos spectateurs verront. Il est également très facile de télécharger des vidéos intégrées avec la balise `<video>`, donc si vous êtes préoccupé par le piratage, vous pourriez envisager d'autres options.

Et avec cela, allez-y et intégrez des vidéos à votre guise. Ou pas – c'est à vous de décider.