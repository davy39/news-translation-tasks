---
title: Propriété CSS Opacity et Opacité des Images Expliquées
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-13T18:08:00.000Z'
originalURL: https://freecodecamp.org/news/css-opacity
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9eb9740569d1a4ca3eb6.jpg
tags:
- name: CSS
  slug: css
seo_title: Propriété CSS Opacity et Opacité des Images Expliquées
seo_desc: 'The opacity property controls how opaque an element is on a scale of 0.0
  to 1.0. The lower the value, the more transparent the element is.

  You can choose up to what extent you want to make the element transparent. You have
  to add the following CSS pr...'
---

La propriété `opacity` contrôle le niveau d'opacité d'un élément sur une échelle de 0,0 à 1,0. Plus la valeur est basse, plus l'élément est transparent.

Vous pouvez choisir jusqu'à quel point vous souhaitez rendre l'élément transparent. Vous devez ajouter la propriété CSS suivante pour obtenir les niveaux de transparence.

**Totalement opaque**

```css
.class-name {
  opacity: 1;
}

/* OU */

.class-name {
  opacity: 1.0;
}
```

**Semi-transparent**

```css
.class-name {
  opacity: 0.5;
}
```

**Totalement transparent**

```css
.class-name {
  opacity: 0;
}

/* OU */

.class-name {
  opacity: 0.0;
}
```

Alternativement, vous pouvez utiliser `rgba` pour définir l'opacité d'un élément :

```css
.class-name {
  background-color: rgba(0, 0, 0, 0.5);
}
```

Cela définit la `background-color` d'un élément en noir avec une opacité de 50 %. La dernière valeur dans une valeur `rgba` est la _valeur alpha_. Une valeur alpha de 1 est égale à 100 % d'opacité, et 0,5 (ou .5 comme ci-dessus) est égale à 50 % d'opacité.

## **Opacité et Transparence des Images**

La propriété `opacity` vous permet de rendre une image transparente en réduisant son opacité.

`Opacity` prend une valeur entre 0,0 et 1,0.

1,0 est la valeur par défaut pour toute image. Elle est totalement opaque.

Exemple

```css
img {
    opacity: 0.3;
}
```

Incluez `filter: alpha(opacity=x)` pour IE8 et les versions antérieures. Le x prend une valeur de 0 à 100.

```css
img {
   opacity: 0.3;
   filter: alpha(opacity=30);
}
```

Voici un exemple d'une image définie avec les paramètres de l'exemple ci-dessus.

![image à 30 % d'opacité](https://github.com/lvcoulter/images/blob/master/Opacity30percent.jpg?raw=true)

Vous pouvez associer `opacity` avec `:hover` pour créer un effet dynamique au survol de la souris.

Exemple :

```css
img {
    opacity: 0.3;
    filter: alpha(opacity=30);
}
img:hover {
   opacity: 1.0;
   filter: alpha(opacity=100);
}
```

[Un exemple CodePen pour montrer une image transparente devenant opaque au survol](https://codepen.io/lvcoulter/full/JrzxXa/)

Vous pouvez créer l'effet inverse avec moins de code puisque l'image est à 1,0 d'opacité par défaut.

Exemple :

```css
img:hover {
   opacity: 0.3;
   filter: alpha(opacity=30);
}
```

Voici un [exemple CodePen pour montrer la transparence au survol de la souris](https://codepen.io/lvcoulter/full/xXBQoR/).

## Plus sur CSS

### **Cascading Style Sheets (CSS)**

CSS est l'acronyme de Cascading Style Sheets. Il a été inventé pour la première fois en 1996 et est maintenant une fonctionnalité standard de tous les principaux navigateurs web.

CSS permet aux développeurs de contrôler l'apparence des pages web en "stylant" la structure HTML de cette page.

Les spécifications CSS sont maintenues par le [World Wide Web Consortium (W3C)](https://www.w3.org/).

Vous pouvez créer des choses assez incroyables avec CSS seul, comme ce jeu [Minesweeper en CSS pur](https://codepen.io/bali_balo/pen/BLJONk) (qui n'utilise pas de JavaScript).