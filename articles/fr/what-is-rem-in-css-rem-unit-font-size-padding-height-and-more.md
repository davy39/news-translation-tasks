---
title: Qu'est-ce que le rem en CSS ? Taille de police, padding, hauteur et plus encore
  avec l'unité rem
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-10-03T22:57:54.000Z'
originalURL: https://freecodecamp.org/news/what-is-rem-in-css-rem-unit-font-size-padding-height-and-more
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/rem-units.png
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Qu'est-ce que le rem en CSS ? Taille de police, padding, hauteur et plus
  encore avec l'unité rem
seo_desc: 'By Dillion Megida

  The rem measurement unit is a relative unit that you can use for length values in
  CSS. I will explain what this unit is, and how it is different from other units
  in this article.

  In my previous article, I explained the two categorie...'
---

Par Dillion Megida

L'unité de mesure `rem` est une unité relative que vous pouvez utiliser pour les valeurs de longueur en CSS. Dans cet article, j'expliquerai ce qu'est cette unité et en quoi elle diffère des autres unités.

Dans mon article précédent, j'ai expliqué les deux catégories d'unités en CSS : [les unités **absolues** et **relatives**](https://www.freecodecamp.org/news/absolute-and-relative-css-units/). Je vous recommande de le consulter afin de comprendre ce que sont les unités relatives et pourquoi le `rem` appartient à cette catégorie.

Pour expliquer brièvement, les unités relatives sont utilisées pour des valeurs qui dépendent (sont relatives à) d'autres valeurs.

## Qu'est-ce que l'unité rem ?

`rem` signifie **root em**, ce qui est une unité de mesure faisant référence à la `font-size` de l'élément `root` (racine) d'un document. 

C'est une unité relative, ce qui signifie que toutes les valeurs qui l'utilisent changent lorsque la `font-size` de la racine change. L'élément `root` dans ce cas fait référence à l'élément `html`.

**1rem** signifie **1 fois la font-size racine**.

Ainsi, si vous déclarez la `font-size` de la racine à 16px (qui est la taille de police par défaut) comme ceci :

```css
html {
  font-size: 16px;
}
```

alors, partout où vous utiliserez `1rem`, cela sera interprété comme `16px`. `2rem` sera interprété comme `32px`. `0.5rem` sera interprété comme `8px`, et ainsi de suite.

## Différence entre rem et em

Le `rem` fait référence à la `font-size` de l'élément `html` tandis que l' `em` fait référence à la `font-size` de l'élément sur lequel il est utilisé (dans certains cas, la `font-size` de l'élément parent).

Voyons quelques exemples pour l' `em` :

```html
<div>
    <p>Je suis un texte</p>
</div>
```

Le CSS :

```css
div {
  font-size: 20px;
}

p {
  font-size: 1.5em;
  width: 2em;
}
```

Pour la `font-size` de la balise `p`, l' `em` fait référence à la `font-size` de son élément parent, qui dans ce cas est le `div`. Ainsi, `font-size: 1.5em` sur la balise `p` sera interprété comme **1,5 fois 20px**, soit **30px**.

Pour la `width` de la balise `p`, l' `em` fait référence à la `font-size` de la balise `p` elle-même. Ainsi, `width: 2em` sur la balise `p` sera interprété comme **2 fois 30px**, soit **60px**.

Et pour l'exemple montrant le `rem` :

```html
<div>
    <p>Je suis un texte</p>
</div>
```

Voici le CSS :

```css
html {
  font-size: 18px;
}

div {
  font-size: 20px;
}

p {
  font-size: 1.5rem;
  width: 10rem;
  padding: 0.2rem;
  height: 4rem;
  border: 1rem solid red;
}
```

Voici le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-36.png)

Pour la `font-size` de la balise `p`, le `rem` fait référence à la `font-size` de l'élément racine (`html`). Ainsi, `font-size: 1.5rem` sur la balise `p` sera interprété comme **1,5 fois 18px**, soit **27px**.

Pour la `width` de la balise `p`, le `rem` fait également référence à la `font-size` de l'élément racine. Ainsi, `width: 10rem` sur la balise `p` sera interprété comme **10 fois 18px**, soit **180px**.

Pour le `padding` de la balise `p`, le `rem` fait référence à la `font-size` de l'élément racine. Ainsi, `padding: 0.2rem` sur la balise `p` sera interprété comme **0,2 fois 18px**, soit **3,6px**.

Pour la `height` de la balise `p`, le `rem` fait référence à la `font-size` de l'élément racine. Ainsi, `height: 4rem` sur la balise `p` sera interprété comme **4 fois 18px**, soit **72px**.

Et enfin, pour la `border-width` de la balise `p`, le `rem` fait toujours référence à la `font-size` de l'élément racine. Ainsi, `border: 1rem...` sur la balise `p` sera interprété comme **1 fois 18px**, soit **18px**.

Vous pouvez utiliser le `rem` avec d'autres valeurs de longueur en CSS.

## Conclusion

Contrairement aux unités fixes, les unités relatives facilitent la création de designs réactifs dans la plupart des situations. Lorsque vous modifiez la valeur dont dépendent les unités, toutes les valeurs utilisant l'unité relative s'adaptent en conséquence.

Le `rem` est une unité relative qui vous permet de définir une `font-size` globale, et toutes les autres valeurs utilisant l'unité `rem` dépendent de cette taille globale. Si l'utilisateur d'un navigateur modifie sa taille de police racine par défaut, les valeurs en unité `rem` s'adapteront également. Dans le cas de valeurs fixes, la préférence de l'utilisateur sera ignorée.

Alors que l' `em` fait référence à la `font-size` de l'élément lui-même (ou de son parent), le `rem` fait référence à la `font-size` racine.