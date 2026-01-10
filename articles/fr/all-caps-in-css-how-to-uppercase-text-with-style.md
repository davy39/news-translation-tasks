---
title: Tout en majuscules en CSS - Comment mettre du texte en majuscules avec style
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-05-24T21:02:28.000Z'
originalURL: https://freecodecamp.org/news/all-caps-in-css-how-to-uppercase-text-with-style
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/how-to-uppercase-text-in-CSS.png
tags:
- name: CSS
  slug: css
- name: Web Development
  slug: web-development
seo_title: Tout en majuscules en CSS - Comment mettre du texte en majuscules avec
  style
seo_desc: "By Dillion Megida\nWhen you're designing a website or working on a project,\
  \ you might want to use uppercase text for various reasons. Maybe you want to use\
  \ an abbreviation or acronym, emphasize certain text, or use it for headings. \n\
  There are multiple..."
---

Par Dillion Megida

Lorsque vous concevez un site web ou travaillez sur un projet, vous pourriez vouloir utiliser du texte en majuscules pour diverses raisons. Peut-être souhaitez-vous utiliser une abréviation ou un acronyme, mettre en évidence un certain texte, ou l'utiliser pour les titres. 

Il existe plusieurs façons de mettre du texte en majuscules en HTML. La première façon est de coder en dur le texte en majuscules en HTML :

```html
<p>TEXTE EN MAJUSCULES</p>
```

La deuxième façon est d'utiliser la méthode de chaîne JavaScript [`toUpperCase()`](https://dillionmegida.com/p/10-useful-string-methods-in-javascirpt/#touppercase-and-tolowercase) et de la rendre sur le DOM :

```js
const upper = string.toUpperCase()

// puis rendre
```

La troisième façon, que nous allons examiner dans cet article, est d'utiliser la propriété CSS `text-transform`.

## Comment utiliser text-transform en CSS

Vous pouvez utiliser la propriété CSS `text-transform` pour mettre du texte en majuscules sous différentes formes. Cette propriété peut modifier le texte pour qu'il soit en **majuscules**, en **minuscules**, ou **capitalisé** (de sorte que chaque mot commence par une majuscule et que les caractères restants du mot conservent leur forme originale).

Pour transformer du texte en majuscules en CSS, utilisez la déclaration de style suivante :


```css
sélecteur-élément {
  text-transform: uppercase;
}
```

Cela style le texte de l'élément sélectionné en majuscules.

Cette déclaration ne change pas le contenu du DOM. Par exemple, regardez ce code HTML :


```html
<p class='paragraphe'>
  Un certain texte
</p>
```

Et ce style :

```css
.paragraphe {
  text-transform: uppercase;
}
```

Sur l'interface utilisateur, le texte est stylé comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-137.png)

Mais dans le DOM, le texte reste le même comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-139.png)

Lorsque vous copiez le texte sur le navigateur, le texte original "Un certain texte" est copié dans certains navigateurs, mais dans d'autres, la version stylée est copiée.

## Devriez-vous utiliser text-transform en CSS ou les autres méthodes ?

Si vous utilisez les majuscules à des fins de style, je recommande d'utiliser CSS. La raison est qu'il peut y avoir des incohérences dans la manière dont différents navigateurs et outils de navigateur gèrent le texte en majuscules.

Une incohérence est la différence de copie-collage que j'ai mentionnée précédemment.

Une autre incohérence est que certains lecteurs d'écran interprètent le texte en majuscules comme des abréviations. Ainsi, un texte comme "DU TEXTE" sera lu comme "D.U T.E.X.T.E", ce qui peut affecter la manière dont un lecteur comprend un message.

Cependant, il est important de noter que certains lecteurs d'écran interprètent également le texte en majuscules avec CSS comme des abréviations.

Cependant, il est recommandé de garder les styles comme styles. Si vous voulez avoir du texte en majuscules juste pour des raisons de style, utilisez CSS, et gardez le texte original en HTML. Mais si vous utilisez les majuscules pour des abréviations ou une raison spécifique d'avoir du texte en majuscules, vous pouvez le coder en dur en HTML.

Vous pouvez vous référer à [ce tweet sur la mise en majuscules sans CSS](https://twitter.com/Mandy_Kerr/status/1285866670284668930) pour voir les discussions à ce sujet.