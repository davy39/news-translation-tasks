---
title: Comment la propriété CSS Box-sizing contrôle la taille des éléments
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-27T16:44:15.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-the-css-box-sizing-property
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/Didicodes-j.png
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: Web Design
  slug: web-design
seo_title: Comment la propriété CSS Box-sizing contrôle la taille des éléments
seo_desc: 'By Edidiong Asikpo

  The CSS box-sizing property is used to adjust or control the size of any element
  that accepts a width or height. It specifies how to calculate the total width and
  height of that element.

  In this article, I will explain how the CSS ...'
---

Par Edidiong Asikpo

La propriété CSS box-sizing est utilisée pour ajuster ou contrôler la taille de tout élément qui accepte une `width` ou `height`. Elle spécifie comment calculer la `width` et la `height` totale de cet élément.

Dans cet article, je vais expliquer comment la propriété CSS `box-sizing` peut être utilisée pour contrôler la taille des éléments.

## Prérequis

* Connaissances de base en CSS.
* Éditeur de code.
* Navigateur web.

## Sans la propriété CSS box-sizing

Si vous regardez l'extrait de code ci-dessous, vous remarquerez qu'il y a deux éléments `div` avec la même `width` et `height` – mais le premier `div` semble plus grand que le second `div`.

%[https://codepen.io/edyasikpo/pen/mdVoxrg]

C'est assez étrange, n'est-ce pas ? Parce que pourquoi quelqu'un attribuerait-il la même largeur et hauteur à deux éléments `div` à moins qu'il ne veuille idéalement que ces éléments soient identiques ? 

Continuez à lire pour découvrir pourquoi les deux éléments `div` sont différents??????. 

Par défaut, le [modèle de boîte CSS](https://kolosek.hashnode.dev/a-beginners-guide-to-box-model-in-css-ck6rnzojg03fidfs1g2kxl8ci) calcule tout élément qui accepte une largeur ou une hauteur dans ce format :

* width + padding + border = largeur rendue ou affichée de la boîte de l'élément.
* height + padding + border = hauteur rendue ou affichée de la boîte de l'élément.

Cela signifie que chaque fois que vous ajoutez un `padding` ou une `border` à l'élément, la taille d'un élément apparaîtra plus grande que la taille qui lui a été initialement attribuée. Cela est dû au fait que le contenu de cet élément inclut les propriétés `width` et `height` mais n'inclut pas les propriétés `padding` ou `border`.

Vous ne comprenez toujours pas ? Regardez l'extrait de code ci-dessous pour voir le calcul réel.

```css
.first-box {
  width: 200px;
  height: 100px;
  border: 8px solid blue;
  padding: 20px;
  background: yellow;
  /* Largeur totale : 200px + (2 * 20px) + (2 * 8px) = 256px
     Hauteur totale : 100px + (2 * 20px) + (2 * 8px) = 156px */
}

.second-box {
  width: 200px;
  height: 100px;
  border: 8px solid blue;
  background: yellow;
  /* Largeur totale : 200px + (2 * 8px) = 216px
     Hauteur totale : 100px + (2 * 8px) = 116px */
}

```

Comme on peut le voir dans l'extrait de code, CSS ajoute le `padding` et la `border` à la `width` et à la `height` déjà spécifiées. Il affiche la valeur totale comme la taille de l'élément, ignorant ainsi la taille réelle que vous avez attribuée au `div`. 

## Avec la propriété CSS box-sizing

Avec la propriété `box-sizing`, le comportement par défaut expliqué ci-dessus peut être modifié. 

En utilisant le même code, ajoutons la propriété `box-sizing` et définissons-la sur `border-box` pour voir si nous pouvons réellement contrôler la taille. 

%[https://codepen.io/edyasikpo/pen/zYrbbwP]

Vous devez avoir remarqué que les deux éléments `div` ont maintenant la même taille. 

## Syntaxe

```
box-sizing:content-box;
box-sizing:border-box;

```

## content-box

C'est le comportement par défaut de la propriété box-sizing. `content-box` ne prend pas en compte la `width` et la `height` spécifiées pour un élément. 

C'est-à-dire, si vous définissez la `width` d'un élément à **200 pixels**, puis définissez la bordure à **8 pixels** et le padding à **20 pixels**, la taille de la `border` et du `padding` sera ajoutée à la largeur rendue finale. Cela rend l'élément plus large que **200 pixels**.

```css
div{
  box-sizing:content-box;
  width: 200px;
  border: 8px solid blue;
  padding: 20px;
  background: yellow;
  /* Largeur totale : 200px + (2 * 20px) + (2 * 8px) = 256px*/
}

```

Comme on peut le voir dans l'extrait de code ci-dessus, la taille de cet élément `div` a automatiquement augmenté à 256px même lorsqu'elle était initialement définie à 200px.

## border-box

Lorsque vous définissez la propriété `box-sizing` sur `border-box`, cela indique au navigateur de prendre en compte toute `border` et tout `padding` attribué à la largeur et à la hauteur de l'élément. 

C'est-à-dire, si vous définissez la `width` d'un élément à **200 pixels**, ces 200 pixels incluront toute bordure ou padding que vous ajoutez, et la boîte de contenu se rétrécira pour absorber cette largeur supplémentaire.

```css
div{
  box-sizing:border-box;
  width: 200px;
  border: 8px solid blue;
  padding: 20px;
  background: yellow;
  /* Largeur totale : 200px - (2 * 20px) - (2 * 8px) = 144px*/
}

```

Comme on peut le voir dans l'extrait de code ci-dessus, la taille de cet élément `div` a automatiquement diminué à 144px même lorsqu'elle était initialement définie à 200px.

Fusionnons les deux extraits de code et voyons exactement à quoi ressemblera la boîte avec `content-box` et `border-box`.

%[https://codepen.io/edyasikpo/pen/xxZerWW]

## Conclusion

Avec la propriété CSS box-sizing, vous avez la possibilité de définir comment la taille des éléments dans votre code est calculée. 

Selon le [MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/box-sizing), il est souvent utile de définir `box-sizing` sur `border-box` lorsque vous disposez des éléments. Cela facilite grandement la gestion des tailles des éléments et élimine généralement un certain nombre de pièges sur lesquels vous pouvez trébucher lors de la disposition de votre contenu.  

D'autre part, lorsque vous utilisez `position: relative` ou `position: absolute`, l'utilisation de `box-sizing: content-box` permet aux valeurs de positionnement d'être relatives au contenu et indépendantes des modifications de la taille des bordures et des paddings. Parfois, vous pourriez vouloir cela.

C'est tout pour aujourd'hui ! J'espère que cela a été utile. Si c'est le cas, veuillez partager cet article et me suivre sur [Twitter](https://twitter.com/Didicodes).