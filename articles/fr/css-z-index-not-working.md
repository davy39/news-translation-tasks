---
title: CSS Z-Index ne fonctionne pas ? Comment le corriger en utilisant l'ordre de
  superposition
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-12-21T14:59:29.000Z'
originalURL: https://freecodecamp.org/news/css-z-index-not-working
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5fd7de8ae6787e098393efd5.jpg
tags:
- name: CSS
  slug: css
- name: Web Design
  slug: web-design
seo_title: CSS Z-Index ne fonctionne pas ? Comment le corriger en utilisant l'ordre
  de superposition
seo_desc: "By Cem Eygi\nThe z-index property of CSS is a tricky one. It won't work\
  \ easily by itself if you don't know how to use it properly. \nSo in this post,\
  \ I'm going to explain what the z-index property is, what stacking order is, and\
  \ how to use them in the ..."
---

Par Cem Eygi

La propriété `z-index` de CSS est délicate. Elle ne fonctionnera pas facilement toute seule si vous ne savez pas comment l'utiliser correctement. 

Dans cet article, je vais expliquer ce qu'est la propriété `z-index`, ce qu'est l'ordre de superposition et comment les utiliser de la bonne manière.

Je vais également donner quelques exemples courants de pourquoi la propriété `z-index` pourrait ne pas fonctionner et vous montrer les solutions.

## Qu'est-ce que le Z-index ?

Tout d'abord, le caractère Z provient de la représentation des trois dimensions x, y et z. x et y représentent la largeur et la hauteur, et la 3ème dimension, Z, représente la profondeur :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/xyz.png)

CSS fournit une propriété appelée `z-index` afin que nous puissions l'utiliser pour déterminer la profondeur d'un élément. À mesure que la valeur `z-index` d'un élément augmente, il sera positionné devant d'autres éléments en termes de la 3ème dimension.

Poursuivons avec quelques exemples et voyons comment utiliser le `z-index` de la bonne manière.

## Z-Index ne fonctionne pas sans une position définie ou Position : Static

La première chose importante à savoir est que chaque élément sur une page web a une position par défaut – en d'autres termes, une position définie de manière statique (par défaut). Disons que nous avons une boîte rouge et une boîte bleue sur notre page :

```html
<div class="box box-red"></div>
<div class="box box-blue"></div>
```

![Image](https://www.freecodecamp.org/news/content/images/2020/12/1.png)

Si vous appliquez `z-index` directement aux boîtes, vous verrez que cela ne fonctionnera pas. Cela est dû au fait qu'elles n'ont pas encore de position définie :

```css
.box {
  height: 150px;
  width: 150px;
}

.box-red {
  background: red;
  z-index: 1;
}

.box-blue {
  background: #00d5f1;
  bottom: 80px;
  left: 55px;
  z-index: 2;
}
```

Ceci est l'un des exemples les plus courants de pourquoi le `z-index` ne fonctionne pas correctement. Pour le résoudre, nous pouvons appliquer une [propriété de position](https://www.freecodecamp.org/news/how-to-use-the-position-property-in-css-to-align-elements-d8f49c403a26/) à la classe de boîte qui fera l'affaire :

```css
.box {
  height: 150px;
  width: 150px;
  position: relative;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2020/12/2.png)

Vous pouvez également regarder ma vidéo tutorielle pour voir l'exemple d'utilisation de z-index :

%[https://youtu.be/vo1JBj-OAa8]

## Qu'est-ce que l'ordre de superposition ?

Si nous supprimons les propriétés `z-index` des deux boîtes, la boîte bleue sera toujours positionnée devant la boîte rouge, même s'il n'y a plus de propriété `z-index` :

```css
.box {
  height: 150px;
  width: 150px;
  position: relative;
}

.box-red {
  background: red;
}

.box-blue {
  background: #00d5f1;
  bottom: 80px;
  left: 55px;
}
```

Ce qui donne le résultat suivant :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-153.png)

Ainsi, lorsque les éléments sont tous au même niveau, un élément sera toujours devant l'autre, car ils ont également un ordre par défaut en termes de l'axe Z. Cela s'appelle l'ordre de superposition.

Comme dans l'exemple ci-dessus, lorsqu'il n'y a pas de `z-index` appliqué à un élément, les navigateurs utilisent un ordre de superposition par défaut pour superposer les éléments sur la page :

> 1. L'arrière-plan et les bordures de l'élément racine  
> 2. Les blocs descendants [non positionnés](https://developer.mozilla.org/en-US/docs/Web/CSS/position#static), dans l'ordre d'apparition dans le HTML  
> 3. Les éléments descendants [positionnés](https://developer.mozilla.org/en-US/docs/Web/CSS/position#Types_of_positioning), dans l'ordre d'apparition dans le HTML  
>   
> Source : [Superposition sans la propriété z-index](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Positioning/Understanding_z_index/Stacking_without_z-index)

Notez que l'élément racine fait référence à l'élément `<html>`, tandis que les éléments non positionnés sont ceux avec le `position: static` par défaut, et les éléments positionnés sont les éléments avec `position` définie sur une autre valeur.

Si nous ajoutons une autre boîte, mais que nous définissons son attribut `position` sur le `static` par défaut, elle apparaîtra derrière les boîtes bleue et rouge :

```html
<div class="box box-red"><p>Positionné</p></div>
<div class="box box-blue"><p>Positionné</p></div>
<div class="box box-yellow"><p>Non positionné</p></div>

```

```css
.box {
  height: 150px;
  width: 150px;
  position: absolute;
}

p {
  color: #0a0a23;
  margin: 0;
  padding-left: 5px;
}

.box-red {
  background: red;
  top: 40px;
  left: 27px;
}

.box-blue {
  background: #00d5f1;
  top: 80px;
  left: 55px;
}

.box-yellow {
  background: rgb(251, 239, 0);
  position: static;
}

```

Ce qui produit le résultat suivant :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-156.png)

Bien que nous ayons modifié les boîtes bleue et rouge pour utiliser `position: absolute` au lieu de `relative`, et ajusté leur placement un peu, cela aide à montrer l'ordre de superposition par défaut du navigateur – les éléments positionnés au même niveau apparaîtront toujours au-dessus des éléments non positionnés (ou `position: static`).

Maintenant, vous vous demandez peut-être ce qui se passe lorsque les éléments ne sont pas au même niveau. Approfondissons cela maintenant.

## Contexte de superposition : Comment le Z-index de l'élément parent s'applique également aux enfants

Disons que nous plaçons une boîte jaune entre la rouge et la bleue :

```html
<div class="box box-red">
  <div class="box box-yellow"></div>
</div>
<div class="box box-blue"></div>
```

```css
.box-red {
  background: red;
  z-index: 1;
}

.box-blue {
  background: #00d5f1;
  bottom: 80px;
  left: 55px;
  z-index: 2;
}

.box-yellow {
  background: rgb(251, 239, 0);
  left: 25px;
  top: 25px;
  z-index: 3;
}
```

Ce qui donne le résultat suivant :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/3.png)

Maintenant, comme vous le voyez dans le code, même si la boîte jaune a une valeur `z-index` plus élevée par rapport à la bleue, elle est positionnée derrière la boîte bleue.

Cela est dû au fait que la boîte jaune est l'enfant de la boîte rouge, et le `z-index` de l'élément parent s'applique toujours à ses enfants également. Puisque l'élément parent a un z-index inférieur, ses enfants héritent de la même valeur `z-index`.

Cela est dû à quelque chose appelé **contexte de superposition**. En termes simples, un contexte de superposition est comme une nouvelle instance de la liste d'ordre de superposition précédente :

1. Un élément HTML racine
2. Les éléments non positionnés (`position: static`) dans l'ordre où ils apparaissent
3. Les éléments positionnés (`position` est défini sur une autre valeur) dans l'ordre où ils apparaissent

La chose principale à retenir est qu'un élément positionné avec une valeur `z-index` autre que la valeur par défaut `auto` créera un nouveau contexte de superposition.

Ainsi, en regardant notre HTML ci-dessus, parce que la boîte rouge a un `z-index` de 1, elle crée un nouveau contexte de superposition pour son enfant, la boîte jaune. Dans ce contexte de superposition, la boîte rouge sert d'élément HTML racine, et la boîte jaune est un élément positionné à l'intérieur de celle-ci.

Ensuite, parce que la boîte bleue fait partie du même contexte de superposition que la boîte rouge (où l'élément `<html>` sert d'élément racine), elle apparaîtra toujours au-dessus de la boîte jaune.

Si vous voyez ce genre de problème, vous pouvez le résoudre soit en retirant l'élément enfant de son parent, soit en supprimant la propriété de position du parent afin que le `z-index` n'affecte pas ses enfants :

```html
<div class="box box-red"></div>
<div class="box box-yellow"></div>
<div class="box box-blue"></div>

```

```css
.box {
  height: 150px;
  width: 150px;
  position: relative;
}

.box-red {
  background: red;
  z-index: 1;
}

.box-blue {
  background: #00d5f1;
  bottom: 240px;
  left: 55px;
  z-index: 2;
}

.box-yellow {
  background: rgb(251, 239, 0);
  bottom: 120px;
  left: 25px;
  z-index: 3;
}

```

Ce qui nous donne :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-158.png)

Notez qu'il existe un certain nombre d'autres propriétés qui affectent le contexte de superposition d'un élément. Vous pouvez en lire plus à ce sujet [ici](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Positioning/Understanding_z_index/The_stacking_context).

Parce que c'est un peu contre-intuitif, c'est l'une des raisons les plus courantes pour lesquelles `z-index` ne fonctionne pas.

## Ne pas attribuer de grands nombres à Z-Index

Une autre raison courante pour laquelle `z-index` pourrait ne pas fonctionner est que parfois les gens attribuent des nombres très élevés à la propriété `z-index` :

```css
.box-blue {
  z-index: 9999;
}
```

Dans quelques projets sur lesquels j'ai travaillé dans le passé, j'ai souvent vu des gens attribuer ces très grands nombres comme 9999 au `z-index` d'un élément.

Bien sûr, cela fonctionne, mais c'est comme utiliser un marteau lorsque vous avez vraiment besoin d'un tournevis.

Imaginez cela de cette manière – vous arrivez dans un grand projet et travaillez sur du HTML, mais peu importe ce que vous essayez, vous ne parvenez pas à faire apparaître les éléments dans le bon ordre. Après avoir creusé et recherché en ligne, vous découvrez que quelqu'un à un moment donné avait défini une propriété `z-index` globale à 9999, ce qui continue d'écraser votre `z-index`.

Maintenant que vous savez comment utiliser correctement `z-index`, et que vous comprenez le contexte de superposition, vous ne devriez pas avoir à utiliser des valeurs aussi grandes comme celle-ci :)

J'espère que cet article vous a aidé à mieux comprendre comment utiliser la propriété `z-index`, ainsi que l'ordre de superposition et le contexte de superposition. Si vous souhaitez en savoir plus sur le développement web, n'oubliez pas de [vous abonner à ma chaîne](https://www.youtube.com/channel/UC1EgYPCvKCXFn8HlpoJwY3Q).

Merci d'avoir lu !