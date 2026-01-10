---
title: Couleur d'arrière-plan HTML – Tutoriel pour changer la couleur de fond
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-09-12T17:30:49.000Z'
originalURL: https://freecodecamp.org/news/html-background-color-change-bg-color-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/cover-template--7-.png
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
seo_title: Couleur d'arrière-plan HTML – Tutoriel pour changer la couleur de fond
seo_desc: 'When you''re building web pages, you always want to create unique layouts.
  You want your web page to be appealing to your users and not jarring to the eye.

  And to help do that, you can choose background and text colors that blend well and
  complement e...'
---

Lorsque vous construisez des pages web, vous souhaitez toujours créer des mises en page uniques. Vous voulez que votre page web soit attrayante pour vos utilisateurs et non agressante pour les yeux.

Et pour vous aider à le faire, vous pouvez choisir des couleurs de fond et de texte qui se mélangent bien et se complètent.

Par défaut, vous remarquerez que votre page web a une couleur de fond transparente, que vous pouvez changer pour n'importe quelle couleur que vous souhaitez.

Par exemple, vous pourriez vouloir créer une fonctionnalité de mode sombre sur votre page web afin que le fond ait une couleur foncée tandis que le texte a une couleur claire. Cela aide les lecteurs à éviter les couleurs vives qui peuvent affecter leurs yeux.

Dans cet article, vous apprendrez comment changer la couleur de fond de vos pages web avec HTML et CSS.

## Comment nous changions la couleur de fond

Dans le passé, avant l'introduction de HTML5, certains styles de base étaient gérés par HTML.

Par exemple, lorsque vous vouliez changer la couleur de fond de votre page, vous auriez pu facilement ajouter l'attribut `bgcolor` dans la balise d'ouverture du body et le définir à la valeur de votre couleur préférée. Cela pouvait être son code hexadécimal ou le nom.

```html
<body bgcolor="grey">

// Ou

<body bgcolor="#808080">
```

Cependant, cet attribut a été obsolète lorsque HTML5 a été introduit. Il est maintenant remplacé par une meilleure alternative, la propriété CSS `background-color`. Cela a du sens car HTML est un langage de balisage, pas un langage de style. Lorsque vous traitez du style, il est préférable d'utiliser CSS.

Au cas où vous seriez pressé de voir comment vous pouvez changer la couleur de fond de votre page web, des divs et d'autres éléments, alors voici comment faire :

```html
// Utilisation de CSS en ligne
<body style="background-color: value;"> 
  // ... 
</body>

// Utilisation de CSS interne/externe
selector {
  background-color: value;
}
```

Disons que vous avez du temps à perdre. Commençons rapidement.

## Comment changer la couleur de fond en HTML

Vous pouvez utiliser la propriété CSS background-color pour changer la couleur de vos pages web. Cette propriété fonctionne comme toute autre propriété CSS, ce qui signifie que vous pouvez l'utiliser pour styliser votre page de trois manières :

* dans vos balises HTML (style en ligne),

* dans une balise style dans la balise head (style interne),

* ou dans un fichier CSS dédié (style externe).

Selon votre préférence, vous définirez la propriété `background-color` à un nom de couleur, un code hexadécimal, une valeur RGB, ou même une valeur HSL. Vous pouvez utiliser cette propriété pour styliser non seulement le corps de votre page web, mais aussi les divs, les titres, les tableaux et bien plus encore.

Consultez l'exemple suivant dans CodePen :

%[https://codepen.io/olawanlejoel/pen/BaxKLdd] 

<iframe height="300" style="width:100%" src="https://codepen.io/olawanlejoel/embed/BaxKLdd?default-tab=html%2Cresult">
  See the Pen <a href="https://codepen.io/olawanlejoel/pen/BaxKLdd">
  Background-color</a> by Olawanle Joel (<a href="https://codepen.io/olawanlejoel">@olawanlejoel</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>

## Comment changer la couleur de fond en HTML avec CSS en ligne

Le CSS en ligne vous permet d'appliquer des styles directement à vos éléments HTML. Cela signifie que vous mettez du CSS directement dans une balise HTML. Vous faites cela avec l'attribut style, qui contient tous les styles que vous souhaitez appliquer à votre balise HTML.

```html
<body style="...">
  // ...
</body>
```

Vous utiliserez la propriété CSS background-color avec la valeur de couleur de votre choix :

```html
// Valeur du nom de couleur
<body style="background-color: skyblue">
  // Valeur hexadécimale
  <div style="background-color: #87CEEB">
    // Valeur RGB
    <h1 style="background-color: rgb(135,206,235)">
      // ...
    </h1>

    // Valeur HSL
    <span style="background-color: hsl(197, 71%, 73%)">
      // ...
    </span>
  </div>
</body>
```

## Comment changer la couleur de fond en HTML avec CSS interne/externe

La meilleure façon de styliser les pages web est le style externe, mais vous pouvez toujours utiliser le style interne lorsque vous n'avez que quelques lignes de styles.

Les styles interne et externe utilisent la même approche : ils utilisent tous deux des sélecteurs pour ajouter du style aux éléments HTML.

Pour le style interne, tous les styles sont ajoutés à votre fichier HTML dans la balise `<style>`. Cette balise style est placée dans la balise `<head>` comme vu ci-dessous :

```html
<!DOCTYPE html>
<html>
  <head>
    <style>
      selector {
        background-color: value;
      }
    </style>
  </head>

  // ...

</html>
```

Pour le style externe, tout ce que vous avez à faire est d'ajouter le style CSS à votre fichier CSS en utilisant la syntaxe générale :

```css
selector {
  background-color: value;
}
```

Le sélecteur peut être soit votre balise HTML, soit une `class` ou un `ID`. Par exemple :

```html
// HTML
<div> 
  <h1> Bienvenue chez freeCodeCamp ! </h1>
</div>

// CSS
div {
  background-color: skyblue;
}
```

Ou vous pourriez utiliser une `class` :

```html
// HTML
<div class="container"> 
  <h1> Bienvenue chez freeCodeCamp ! </h1>
</div>

// CSS
.container {
  background-color: skyblue;
}
```

Ou vous pourriez utiliser un `id` :

```html
// HTML
<div id="container"> 
  <h1> Bienvenue chez freeCodeCamp ! </h1>
</div>

// CSS
#container {
  background-color: skyblue;
}
```

**Note :** Comme vous l'avez vu précédemment, avec le CSS en ligne, vous pouvez utiliser le nom de couleur, le code hexadécimal, la valeur RGB et la valeur HSL avec le style interne ou externe.

## Conclusion

Dans cet article, vous avez appris comment changer la couleur de fond des éléments HTML en utilisant la propriété CSS background-color. Vous avez également appris comment les développeurs le faisaient avant l'introduction de HTML5 avec l'attribut `bgcolor`.

Il est essentiel de se rappeler que le style de vos éléments HTML avec du CSS interne ou externe est toujours préférable au style en ligne car il offre plus de flexibilité. Par exemple, au lieu d'ajouter des styles en ligne similaires à tous vos éléments de balise `<div>`, vous pouvez utiliser une seule classe CSS pour eux.

Les styles en ligne ne sont pas considérés comme des meilleures pratiques car ils entraînent beaucoup de répétition - vous ne pouvez pas réutiliser les styles ailleurs. Pour en savoir plus, vous pouvez lire [mon article sur le style en ligne en HTML](https://www.freecodecamp.org/news/inline-style-in-html/). Vous pouvez également apprendre comment [changer la taille du texte](https://www.freecodecamp.org/news/how-to-change-text-size-in-html/) dans cet article, et comment changer [la couleur du texte](https://www.freecodecamp.org/news/how-to-change-text-color-in-html/) dans cet article.

J'espère que ce tutoriel vous donne les connaissances pour changer la couleur de votre texte HTML afin de le rendre plus beau.

Amusez-vous bien à coder !