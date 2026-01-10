---
title: 'Z Index en CSS : Qu''est-ce que c''est et à quoi ça sert'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-11T23:17:00.000Z'
originalURL: https://freecodecamp.org/news/z-index-in-css-what-it-is-and-what-it-does
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c9f740569d1a4ca3342.jpg
tags:
- name: CSS
  slug: css
- name: toothbrush
  slug: toothbrush
seo_title: 'Z Index en CSS : Qu''est-ce que c''est et à quoi ça sert'
seo_desc: 'What is a Z Index?

  Z Index (z-index) is a CSS property that defines the order of overlapping HTML elements.
  Elements with a higher index will be placed on top of elements with a lower index.

  Note: Z index only works on positioned elements (position:a...'
---

## **Qu'est-ce qu'un Z Index ?**

Le Z Index (`z-index`) est une propriété CSS qui définit l'ordre des éléments HTML qui se chevauchent. Les éléments avec un index plus élevé seront placés au-dessus des éléments avec un index plus bas.

**Note** : Le Z index ne fonctionne que sur les éléments positionnés (`position:absolute`, `position:relative`, ou `position:fixed`).

#### **Valeurs possibles**

```css
/* Valeur par défaut si non spécifiée */
z-index: auto;

/* Valeurs entières */
z-index: 1;
z-index: 100;
z-index: 9999;
z-index: -1;

/* Valeurs globales */
z-index: inherit;
z-index: initial;
z-index: unset;
```

## Comment utiliser le Z Index

Dans cet exemple, vous pouvez voir trois boîtes affichées les unes sur les autres dans différents ordres en utilisant `z-index`.

*HTML*

```html
<div class="container">
  <div class="box" id="blue"></div>
  <div class="box" id="red"></div>
  <div class="box" id="green"></div>
</div>
```

*CSS*

```css
#blue {
  background-color: blue;
}

#red {
  background-color: red;
}

#green {
  background-color: green;
}
```

Puisque `z-index` n'a pas été défini, il aura une valeur par défaut de `auto`. Voici le résultat :

![Une image de trois boîtes, avec la bleue à l'arrière, la rouge au milieu et la verte à l'avant.](https://cdn.hashnode.com/res/hashnode/image/upload/v1731048763410/8f4d61b3-332f-42f0-be9d-7d14c3dbb818.png align="center")

Essayez de changer l'ordre en Vert, Bleu, Rouge en CSS en utilisant `z-index`.

```css
#blue {
  background-color: blue;
  z-index: 2;
}

#red {
  background-color: red;
  z-index: 1;
}

#green {
  background-color: green;
  z-index: 3;
}
```

Votre résultat sera :

![Une image de trois boîtes, avec la rouge à l'arrière, la bleue au milieu et la verte à l'avant.](https://cdn.hashnode.com/res/hashnode/image/upload/v1731048856409/96a9d38e-f200-4468-9515-e080662c5173.png align="center")

Utilisez le Z Index si vous avez besoin de placer un élément d'arrière-plan sous un conteneur. Vous pouvez facilement placer l'arrière-plan sous tous les éléments en lui donnant un Z Index négatif comme ci-dessous :

```css
#background {
  z-index: -1;
}
```