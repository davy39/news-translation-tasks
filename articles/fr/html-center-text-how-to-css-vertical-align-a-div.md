---
title: HTML Centrer le texte – Comment aligner verticalement une Div avec CSS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-12T17:53:52.000Z'
originalURL: https://freecodecamp.org/news/html-center-text-how-to-css-vertical-align-a-div
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/align-div-vertically-in-css-1.png
tags:
- name: CSS
  slug: css
- name: flexbox
  slug: flexbox
- name: HTML
  slug: html
seo_title: HTML Centrer le texte – Comment aligner verticalement une Div avec CSS
seo_desc: 'By Said Hayani

  In the HTML and CSS world, it''s all about the layout structure and the distribution
  of elements. We usually use HTML to define the markup and structure, while CSS helps
  us handle the styling and alignment of elements.

  In this post we a...'
---

Par Said Hayani

Dans le monde HTML et CSS, tout est question de structure de mise en page et de distribution des éléments. Nous utilisons généralement HTML pour définir le balisage et la structure, tandis que CSS nous aide à gérer le style et l'alignement des éléments.

Dans cet article, nous allons apprendre un peu sur les différentes façons de centrer les éléments HTML et de gérer l'alignement vertical avec CSS.

Tout d'abord, nous allons apprendre comment aligner du texte avec CSS.

Ensuite, nous verrons comment aligner une div et tout autre élément.

Et enfin, nous apprendrons comment nous pouvons mettre du texte et une `div` ensemble dans un conteneur.

## Comment centrer du texte

Il existe de nombreuses façons de centrer du texte en utilisant CSS.

### Utiliser la propriété Float

Float est un moyen facile d'aligner du texte.

Pour placer le texte sur le côté droit de la mise en page, nous pouvons simplement utiliser `right` comme valeur pour `float`.

Pour placer le texte sur le côté gauche, nous utilisons `left`, comme `float:left`. Regardez l'exemple ci-dessous :

```html
  .right {
        float: right;
      }
     
      .left {
        float: left;
      }
// HTML

    <span class="right">Droite</span>
    <span class="left">Gauche</span>
```

%[https://codesandbox.io/s/center-html-elements-dlhfu?file=/index.html]

Pour centrer le texte en utilisant float, nous pouvons utiliser `margin-left` ou `margin-right` et le définir à `50%`, comme ci-dessous.

```css
    .center {
    float: left;
    margin-left: 50%;
    }

/* HTML*/
<span class="center">Centre</span>
```

Vous pouvez en apprendre davantage sur les utilisations de `Float` [ici](https://developer.mozilla.org/en-US/docs/Web/CSS/float).

### Utiliser Text-align

`text-align` est une manière plus pratique et plus spécifique d'aligner du texte. Il nous permet de placer le texte au `center` ou à `left` ou à `right`, comme le montre l'exemple suivant :

```css
.right {
text-align: right;
}

.left {
text-align: left;
}
.center {
text-align: center;
}
/* HTML */

<p class="right">Droite</p>
<p class="center">Centre</p>
<p class="left">Gauche</p>
```

%[https://codesandbox.io/s/text-align-71d6q?file=/index.html]

En savoir plus sur `[text-align](https://developer.mozilla.org/en-US/docs/Web/CSS/text-align)`.

## Comment aligner une `div`

Il existe de nombreuses façons de le faire.

De la même manière que nous utilisons `Float` pour aligner du texte, nous pouvons l'utiliser pour aligner un élément `div` également.

%[https://codesandbox.io/s/align-a-div-pn8yw?file=/index.html]

`Float` fait le travail, mais CSS nous offre de meilleures options qui sont plus pratiques et élégantes. Avez-vous entendu parler de `Flexbox` ? Ou de [css-grid](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout) ?

Ces deux méthodes offrent des moyens très modernes pour aligner et travailler avec votre mise en page en CSS. Regardons Flexbox plus en détail.

## [Flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Basic_Concepts_of_Flexbox)

Flexbox offre un moyen facile et direct d'aligner une `div` – et c'est ma méthode préférée jusqu'à présent pour gérer les mises en page en CSS (je l'utilise tous les jours).

Regardons ce que nous ferions avec `Flexbox` pour voir comment cela fonctionne en recréant le même exemple que ci-dessus.

L'exemple :

%[https://codesandbox.io/s/align-dev-with-flexbox-2pp1m]

Le code :

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title>Flexbox</title>
    <style>
      .container {
        display: flex;
      }
      .container div {
        width: 33%;
        height: 60px;
      }

      .left {
        background: yellow;
      }
      .right {
        background: red;
      }
      .center {
        background: lightblue;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <div class="left">Div gauche</div>
      <div class="center">div centrée</div>
      <div class="right">div droite</div>
    </div>
  </body>
</html>

```

Décomposons cela

* Nous définissons toujours un parent `div` en utilisant `display:flex` pour appliquer `Flexbox`. Ainsi, nous rendons tous les enfants div à l'intérieur du parent `div` capables d'être gérés en utilisant les propriétés `Flexbox`.
* La `flex-direction` utilise la direction `row` par défaut, ce qui signifie que les éléments seront placés verticalement dans le conteneur.
* Avec la propriété `justify-content`, nous pouvons aligner les enfants d'une `div` dans différentes directions comme dans l'exemple suivant :

```css
.container{
 display: flex:
 justify-content:center /* flex-start, flex-end, space-between, space-evenly, space-around etc */

}
```

* `justify-content:center` place les éléments au centre du conteneur.
* `justify-content:flex-start` place les éléments au début du conteneur à gauche.
* `justify-content:flex-end` place les éléments à la fin du conteneur sur le côté droit.
* `justify-content:space-around` fait en sorte que les éléments s'adaptent au conteneur et met un espace égal entre tous les éléments.
* `justify-content:space-evenly` distribue les éléments dans le conteneur parent de manière égale avec le même espace et la même largeur.

L'exemple ci-dessus s'applique à tous les enfants des éléments en tant que groupe.

Imaginez si nous voulions aligner une seule `div` à l'intérieur du conteneur. Nous pouvons toujours utiliser `[align-self](https://developer.mozilla.org/en-US/docs/Web/CSS/align-self)` pour aligner un seul élément.

```css
.container div{
 align-self:center /* peut avoir: flex-start, ou flex-end*/
}
```

Nous pouvons appliquer la même chose à un texte avec `Flexbox` comme dans l'exemple suivant :

```css

<style>
.right{
    display: flex;
    align-items: flex-end;
    flex-direction: column;
}
  
</style>
<div class="right">
<span>div droite</span>
</div>
```

Voici un excellent tweet de [Julia Evans](https://twitter.com/b0rk) qui illustre le centrage en CSS en général :

![Image](https://www.freecodecamp.org/news/content/images/2020/08/centering-css-tweet.jpeg)
_[Tweet original ici ](https://twitter.com/b0rk/status/1291417463507374097)_

## Conclusion

Il existe de nombreuses façons de centrer des éléments en CSS. Et vous apprendrez toujours de nouvelles choses avec le temps à mesure que vous pratiquerez de plus en plus.

Je vous recommande donc de travailler sur quelques exemples de ce que vous avez appris aujourd'hui pour que cela reste.

* Vous devriez me suivre sur [Twitter](https://twitter.com/SaidHYN) ?
* Consultez [Mon Github](https://github.com/hayanisaid)
* Visitez mon [Blog](https://saidhayani.com/)