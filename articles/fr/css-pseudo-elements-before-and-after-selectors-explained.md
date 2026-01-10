---
title: Éléments pseudo CSS - Sélecteurs Before et After expliqués
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/css-pseudo-elements-before-and-after-selectors-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9cfa740569d1a4ca3537.jpg
tags:
- name: CSS
  slug: css
- name: toothbrush
  slug: toothbrush
seo_title: Éléments pseudo CSS - Sélecteurs Before et After expliqués
seo_desc: "Before Selector\nThe CSS ::before selector can be used to insert content\
  \ before the content of the selected element or elements. It is used by attaching\
  \ ::before to the element it is to be used on.\nLet’s look at some examples:\np::before\
  \ { \n  content: ..."
---

## **Sélecteur Before**

Le sélecteur CSS `::before` peut être utilisé pour insérer du contenu avant le contenu de l'élément ou des éléments sélectionnés. Il est utilisé en attachant `::before` à l'élément sur lequel il doit être appliqué.

Examinons quelques exemples :

```css
p::before { 
  content: "* ";
}

span.comment::before {
  content: "Commentaire : ";
  color: blue;
}
```

```html
<p> Vers l'infini, et au-delà !</p>
<p> Je suis Buzz Lightyear. Je viens en paix.</p>

<span class="comment">Que la force soit avec toi.</span>
<br/>
<span> Fais-le. Ou ne le fais pas. Il n'y a pas d'essai.</span>
```

Dans l'exemple ci-dessus, nous ajoutons un astérisque et un espace avant chaque élément de paragraphe sur la page. De plus, nous ajoutons "Commentaire : " en bleu avant chaque élément `span` avec la classe `comment`.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-186.png)

## **Sélecteur After**

Le sélecteur CSS `::after` peut être utilisé pour insérer du contenu après le contenu de l'élément ou des éléments sélectionnés. Il est utilisé en attachant `::after` à l'élément sur lequel il doit être appliqué.

Voici quelques exemples :

```css
.buzz::after { 
  content: " - Buzz Lightyear";
  color: blue;
}

.yoda::after { 
  content: " - Yoda";
  color: green;
}
```

```html
<p class="buzz"> Vers l'infini, et au-delà !</p>
<p class="yoda"> Fais-le. Ou ne le fais pas. Il n'y a pas d'essai.</p>
```

Dans l'exemple ci-dessus, nous ajoutons " - Buzz Lightyear" en bleu à l'élément avec la classe `buzz`. De plus, nous ajoutons " - Yoda" en vert à l'élément avec la classe `yoda`.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-185.png)

## **Simple deux-points vs. Double deux-points**

Il y a une certaine discussion sur la bonne façon d'utiliser les pseudo-éléments – l'ancien style simple deux-points (`:before`), utilisé dans les spécifications CSS 1 et 2, contre la recommandation CSS3, double deux-points (`::before`), principalement pour _"établir une discrimination entre les pseudo-classes et les pseudo-éléments"_.

Mais pour des raisons de compatibilité, la méthode simple deux-points est toujours acceptée. Gardez à l'esprit que IE8 ne supporte que la notation simple deux-points.

## **Plus d'informations :**

* [The CSS Handbook: a handy guide to CSS for developers](https://www.freecodecamp.org/news/the-css-handbook-a-handy-guide-to-css-for-developers-b56695917d11/)
* [The Best CSS Examples and CSS3 Examples](https://www.freecodecamp.org/news/css-example-css3/#background-color-example)