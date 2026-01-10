---
title: 'Z-Index Expliqué : Comment Empiler des Éléments avec CSS'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-18T23:18:51.000Z'
originalURL: https://freecodecamp.org/news/z-index-explained-how-to-stack-elements-using-css-7c5aa0f179b3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*TGyQ2F-PxAhKWA6p6b6rYA.jpeg
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: 'Z-Index Expliqué : Comment Empiler des Éléments avec CSS'
seo_desc: 'By Veronika Ivhed

  I have always struggled with the CSS property z-index. It sounds so easy at first.
  Elements with a higher z-index value are displayed in front of those with a lower
  z-index value. Still, a lot of times I have ended up in situations ...'
---

Par Veronika Ivhed

J'ai toujours eu du mal avec la propriété CSS [z-index](https://developer.mozilla.org/en-US/docs/Web/CSS/z-index). Cela semble si simple au premier abord. Les éléments avec une valeur z-index plus élevée sont affichés devant ceux avec une valeur z-index plus faible. Pourtant, de nombreuses fois, je me suis retrouvée dans des situations où il semblait que la valeur z-index n'avait aucun effet.

J'ai décidé que j'en avais assez des essais et erreurs avec z-index et que je voulais mieux comprendre. J'espère que cet article pourra vous aider afin que vous ne vous demandiez plus jamais pourquoi z-index ne fait pas ce que vous attendez.

### Ordre d'empilement par défaut

Mentionnons d'abord l'ordre par défaut dans lequel le navigateur empile les éléments, lorsque aucun z-index n'est appliqué :

1. Élément racine (l'élément <html>)
2. Éléments non positionnés dans l'ordre où ils sont définis
3. Éléments positionnés dans l'ordre où ils sont définis

Un élément [non positionné](https://developer.mozilla.org/en-US/docs/Web/CSS/position) est un élément avec la valeur de position par défaut static. Un élément [positionné](https://developer.mozilla.org/en-US/docs/Web/CSS/position) est un élément avec une autre valeur de position. Exemples d'autres valeurs : absolute, relative, sticky ou fixed.

HTML :

```html
<div class="pink">
  <div class="orange"></div>
</div>
<div class="blue"></div>
<div class="green"></div>
```

CSS :

```css
/* Ceci est uniquement le CSS pertinent pour l'exemple. Pour le CSS complet, consultez les liens sous les images. */

.blue, .pink, .orange {
  position: absolute;
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/0ok6C2rWIvGF9pibC1xMz9q0iOmkqNWOx1cT)
_[https://codepen.io/ivhed/pen/QrdEBB](https://codepen.io/ivhed/pen/QrdEBB" rel="noopener" target="_blank" title=")_

Nous avons défini la boîte verte en dernier dans le document. Pourtant, elle apparaît derrière les autres car elle n'est pas positionnée.

### Empilement avec z-index

Si nous voulons maintenant changer l'ordre d'empilement de ces éléments, nous pouvons utiliser la propriété z-index. Un élément avec un z-index plus élevé sera affiché devant un élément avec un z-index plus faible. Une chose à noter est que z-index **ne fonctionne qu'avec les éléments positionnés**_._

```css
.blue, .pink, .orange {
  position: absolute;
}

.blue {
  z-index: 2;
}

.orange {
  z-index: 3;
}

.green {
  z-index: 100; // n'a aucun effet puisque la boîte verte n'est pas positionnée
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/NOdy4A6ZcslzfIFMD-PW5-vqD83i2Qb5vOrQ)
_[https://codepen.io/ivhed/pen/xjqmpV](https://codepen.io/ivhed/pen/xjqmpV" rel="noopener" target="_blank" title=")_

La boîte orange avec un z-index plus élevé est affichée devant la boîte bleue.

#### Contexte d'empilement

Supposons que nous ajoutons une autre boîte positionnée à la mise en page que nous voulons positionner derrière la boîte rose. Nous mettons à jour notre code comme suit :

HTML :

```html
<div class="pink">
  <div class="orange"></div>
</div>
<div class="blue"></div>
<div class="purple"></div>
<div class="green"></div>
```

CSS :

```css
.blue, .pink, .orange, .purple {
  position: absolute;
}

.purple {
  z-index: 0;
}

.pink {
  z-index: 1;
}

.blue {
  z-index: 2;
}

.orange {
  z-index: 3;
}

.green {
  z-index: 100;
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/Uuw9yAx1sVpyVHZ8sCRtVF8H5eBnyCElCH4S)
_[https://codepen.io/ivhed/pen/YLZdjx](https://codepen.io/ivhed/pen/YLZdjx" rel="noopener" target="_blank" title=")_

Notre boîte rose est affichée devant la boîte violette comme prévu, mais que s'est-il passé avec la boîte orange ? Pourquoi est-elle soudainement derrière la boîte bleue alors qu'elle a un z-index plus élevé ? Cela est dû au fait que l'ajout d'une valeur z-index à un élément forme ce qu'on appelle un [contexte d'empilement](https://www.w3.org/TR/CSS21/zindex.html)**.**

La boîte rose a une valeur z-index autre que auto, ce qui forme un nouveau contexte d'empilement. Le fait qu'elle forme un contexte d'empilement affecte la manière dont ses éléments enfants sont affichés.

Il est possible de changer l'ordre d'empilement des éléments enfants de la boîte rose. Cependant, leur **z-index n'a de sens que dans ce contexte d'empilement**. Cela signifie que nous ne pourrons pas déplacer la boîte orange devant la boîte bleue, car elles ne sont plus dans le même contexte d'empilement.

Si nous voulons que la boîte bleue et la boîte orange fassent partie du même contexte d'empilement, nous pouvons définir la boîte bleue comme un élément enfant de la boîte rose. Cela fera apparaître la boîte bleue derrière la boîte orange.

```html
<div class="pink">
  <div class="orange"></div>
  <div class="blue"></div>
</div>
<div class="purple"></div>
<div class="green"></div>
```

![Image](https://cdn-media-1.freecodecamp.org/images/T-Z7bkfgeKlqiz8WYbAlU0W9RMM4CtJgxw50)
_[https://codepen.io/ivhed/pen/erGoJE](https://codepen.io/ivhed/pen/erGoJE" rel="noopener" target="_blank" title=")_

Les contextes d'empilement ne sont pas seulement formés lors de l'application de z-index à un élément. Il existe [plusieurs autres propriétés](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Positioning/Understanding_z_index/The_stacking_context) qui amènent les éléments à former des contextes d'empilement. Certains exemples sont : filter, opacity et transform.

Revenons à notre exemple précédent. La boîte bleue est à nouveau une sœur de la boîte rose. Cette fois, au lieu d'ajouter z-index à la boîte rose, nous appliquons un [filtre](https://developer.mozilla.org/en-US/docs/Web/CSS/filter) à celle-ci.

HTML :

```html
<div class="pink">
  <div class="orange"></div>
</div>
<div class="blue"></div>
<div class="green"></div>
```

CSS :

```css
.blue, .pink, .orange {
  position: absolute;
}

.pink {
  filter: hue-rotate(20deg);
}

.blue {
  z-index: 2;
}

.orange {
  z-index: 3;
}

.green {
  z-index: 100;
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/JI1HNPrHCEUbKSZZiKSJLnBlWLyJKPclyEez)
_[https://codepen.io/ivhed/pen/LmWMQb](https://codepen.io/ivhed/pen/LmWMQb" rel="noopener" target="_blank" title=")_

La boîte orange a toujours un z-index plus élevé que la boîte bleue, mais elle est toujours affichée derrière celle-ci. Cela est dû au fait que la valeur du filtre a amené la boîte rose à former un nouveau contexte d'empilement.

#### Résumé

En utilisant z-index sur des éléments positionnés, nous pouvons changer l'ordre d'empilement par défaut.

Lors de l'application de certaines propriétés CSS, un élément peut former un contexte d'empilement. Les valeurs de z-index n'ont de sens que dans le même contexte d'empilement.

Pour plus d'informations sur z-index, je recommande [cet article](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Positioning/Understanding_z_index). Je m'en suis beaucoup inspirée lors de la rédaction de cet article.

Merci d'avoir lu ! 😊