---
title: CSS REM – Qu'est-ce que le REM en CSS ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-03-17T19:47:22.000Z'
originalURL: https://freecodecamp.org/news/what-is-rem-in-css
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/rem-in-css-cover-image.jpeg
tags:
- name: CSS
  slug: css
- name: responsive design
  slug: responsive-design
seo_title: CSS REM – Qu'est-ce que le REM en CSS ?
seo_desc: "By Sliman\nIn this article I'm going to discuss some use cases of REM (Root\
  \ EM) in CSS. \nI will begin with some background knowledge about CSS properties\
  \ and values, which I think is necessary. Then I'll discuss the differences between\
  \ absolute length..."
---

Par Sliman

Dans cet article, je vais aborder certains cas d'utilisation du REM (Root EM) en CSS.

Je commencerai par quelques connaissances de base sur les propriétés et les valeurs CSS, ce qui me semble nécessaire. Ensuite, je discuterai des différences entre les valeurs de longueur absolue et les valeurs relatives. Le REM est une valeur de longueur relative.

Dans les deux dernières parties, j'expliquerai pourquoi le REM est utile pour la taille de la police et comment il peut aider à rendre les pages web réactives. C'est parti.

## Ce que vous devez savoir

Dans cette section, je vais d'abord dire quelques mots sur le CSS, en guise d'introduction.

### Qu'est-ce que le CSS ?

Le CSS (qui signifie Cascading Style Sheets) utilise des propriétés et des valeurs pour créer toute la magie esthétique des pages web.

Supposons que vous souhaitiez agrémenter votre image d'une bordure joliment travaillée et que vous vouliez que les bords soient une ligne noire continue. Dans ce cas, `border` serait la propriété à choisir, et `solid` la valeur. C'est un mot-clé en CSS qui lui indique de créer la bordure pleine souhaitée.

Comme vous l'avez peut-être deviné, il doit exister différents types de valeurs, car une simple ligne continue en guise de bordure n'est pas un grand ornement.

La propriété `border` accepte en effet des mots-clés, des couleurs et des longueurs. En réalité, c'est parce que `border` est un raccourci pour `border-width`, `border-style` et `border-color`. Ainsi, au lieu de spécifier chacune de ces propriétés, `border` accepte ces valeurs pour toutes en même temps, comme ceci :

```css
border: 2px solid #ffff00;
```

Dans l'extrait de code ci-dessus, vous voyez la valeur `2px` qui est une valeur de longueur, `solid` qui est un mot-clé pour le style de la bordure, et la valeur hexadécimale RVB `#ffff00` pour la couleur jaune. Voilà une belle bordure (pas vraiment, je sais, mais vous avez compris l'idée).

Une dernière chose à propos de ces valeurs avant de passer aux choses sérieuses. Différentes propriétés acceptent différents types de valeurs. Ces collections de valeurs sont judicieusement appelées `value types` (ou `data types`). 

Laissez-moi clarifier avec un dernier exemple : `color` est un type de valeur, et la valeur hexadécimale RVB `#ffff00` (qui représente la couleur jaune) est une valeur spécifique de ce type de valeur. Si nécessaire, considérez les types de valeurs comme des types et les valeurs comme des jetons de ces types.

Donc, si jamais vous avez besoin de savoir quelles valeurs une propriété spécifique accepte, recherchez simplement ses `value types`, et vous saurez tout.

### Qu'est-ce que le REM en CSS ?

Cet article porte sur l'une de ces valeurs, à savoir le REM, qui signifie Root EM. Le REM est une valeur du type de valeur/donnée `length`. Une autre valeur de `length` est notre bon vieux pixel (`px`). Chaque propriété qui accepte des longueurs comme valeur acceptera le REM. Certaines d'entre elles sont `margin`, `padding`, etc.

Vous vous demandez peut-être pourquoi vous devriez envisager d'utiliser le REM ? Voyons pourquoi dans la section suivante.

## Valeurs relatives vs Valeurs de longueur absolue en CSS

Il existe deux types de valeurs de longueur en CSS : les valeurs de longueur absolue et les valeurs de longueur relative.

### Valeurs de longueur absolue

Des exemples de valeurs de longueur absolue sont : `px` (qui correspond à 1/96ème de pouce), `in` (un pouce) ou `cm` (qui correspond à 37,8px ou 25,2/64in). Vous trouverez plus d'informations sur ces valeurs sur le [MDN](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Values_and_units).

Lorsque vous utilisez ces valeurs de longueur, vous pouvez être sûr qu'elles auront toujours plus ou moins la même taille. C'est particulièrement utile lorsque vous connaissez les dimensions exactes du support de sortie, ce qui est principalement le cas pour les mises en page d'impression. Mais ce n'est pas aussi utile lorsque ce n'est pas le cas, comme avec toutes les différentes tailles d'écran existantes.

Et n'oubliez pas non plus les différents paramètres de navigateur que les gens utilisent, que ce soit par préférence ou par besoin d'accessibilité.

### Valeurs de longueur relative

Les valeurs de longueur relative sont définies par rapport à une autre valeur. Il s'agit, par exemple, du `REM`, de l' `EM` et du `vw`. Nous allons discuter du `REM` en détail ci-dessous, alors abordons brièvement les autres.

L' `EM` est défini par rapport à :

* la taille de la police de l'élément parent lorsque la propriété `font-size` est concernée, et
* la taille de la police de l'élément lui-même lorsque nous traitons d'autres propriétés comme `height`.

`vw` signifie 1 % de la largeur de la fenêtre d'affichage (viewport). C'est-à-dire que si vous définissez la propriété `width` à 10vw, l'élément occupera 10 % de la largeur disponible de la fenêtre d'affichage. Il en existe beaucoup d'autres, et vous pouvez les trouver [ici](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Values_and_units).

Ces valeurs de longueur relative présentent un avantage certain par rapport aux valeurs absolues, car elles peuvent aider à rendre votre site web réactif. C'est-à-dire que votre site web s'adapte automatiquement à la taille de l'écran disponible, et ce de manière prévisible.

## Root EM et taille de police racine

Le REM est défini par rapport à la taille de la police de l'élément racine. L'élément racine est ciblé par la pseudo-classe `:root` ou le sélecteur `html`.

`1rem` prend donc la valeur qui est donnée au `font-size` de l'élément racine. Cela signifie que 1 REM conserve la même valeur dans tout votre code CSS. Si la taille de la police de l'élément racine n'est pas modifiée par l'utilisateur, cette valeur est normalement de `16px`.

Voici un exemple :

```css
html {
	font-size: 18px; /* la valeur par défaut serait 16 */
}

h1 {
 	font-size: 2rem; /* 2 * 18px = 36px; */
}
```

Raisonner à l'envers de `2rem` vers `px` n'est pas une tâche difficile. Mais avez-vous besoin de garder une calculatrice à portée de main pour connaître la taille exacte de la police de votre sous-titre que vous avez réglée à 1,125rem (soit : 16 * 1,125 : `18px`) ?

Heureusement, il existe une manière astucieuse de gérer ce problème. En gardant à l'esprit que vous pouvez également spécifier la taille de la police de l'élément racine avec un pourcentage (%), les développeurs ont découvert que 62,5 % de la valeur par défaut de l'élément racine équivaut à `10px`. Cela simplifie vraiment les choses :

```css
html {
	font-size: 62.5%; /* 16px * 0.625 = 10px; */
}

h1 {
	font-size: 1.8rem; /* 10px * 1.8 = 18px; */
}
```

L'utilisation du REM (ou d'une autre valeur de longueur relative) pour `font-size` est indispensable pour l'accessibilité, car le `px` dans certains navigateurs ne se redimensionne pas lorsque les paramètres du navigateur sont modifiés.

Certaines personnes, par exemple, ont besoin de zoomer jusqu'à 400 % pour pouvoir lire votre texte en raison d'une déficience visuelle. En utilisant le REM, vous vous assurez que votre texte respecte ces besoins, car la taille de la police est définie par rapport à la taille de police par défaut choisie par l'utilisateur.

## Design web réactif avec le REM

Laissez-moi d'abord dire que le design web réactif est un sujet vaste, avec de nombreux aspects différents. Il existe deux certificats sur le design web réactif dans le programme de freeCodeCamp (consultez-les sur [https://www.freecodecamp.org/learn](https://www.freecodecamp.org/learn), si cela vous intéresse).

Ci-dessous, je vais me concentrer sur la manière dont le REM peut aider à rendre les pages web réactives.

Google vous encourage, dans cet [article](https://web.dev/responsive-web-design-basics/#optimize-text-for-reading) sur le design web réactif, à limiter la longueur des lignes à pas plus de 10 mots environ. Ceci est conforme à la théorie classique de la lisibilité.

Ils conseillent d'utiliser des media queries avec des points de rupture (breakpoints) choisis de manière à ce que la largeur de votre contenu ou de vos lignes de texte ne soit pas trop longue. Cela permet d'offrir la meilleure expérience de lecture possible.

Voici un exemple inspiré par [cet](https://www.sitepoint.com/understanding-and-using-rem-units-in-css/) article d'Adrian Sandu :

```css
html {
  margin: 0;
  padding: 0;
  font-size: 62.5%;
}

#divOne {
  width: 100%;
  box-sizing: border-box;
  font-size: 1.6rem;
  padding: 0.5rem;
  background-color: lightblue;
}

@media (min-width: 27.1875rem) { /* premier point de rupture : 27.1875*16px= 435px */
  p {
    font-size: 1.6rem;
  }
#divOne {
  width: 41.8rem;
  background-color: yellow;
  margin: auto;
  }
}

@media (min-width: 40.78125rem) { /* 1.5 * premier point de rupture : 653px */
  p {
    font-size: 2.4rem; /* 1.5 * taille de police du premier point de rupture */
  }
#divOne {
  width: 62.7rem; /* 1.5 * largeur du premier point de rupture */
  background-color: green;
  padding: 0.75rem; /* 1.5 * padding du premier point de rupture */
  margin: auto;
  }
}
```

Vous pouvez consulter ce code [ici](https://codepen.io/slimattcode/pen/jOaJrjZ?editors=0100) sur CodePen. Modifiez la taille de votre fenêtre d'affichage pour voir comment la mise en page change.

Une chose qui pourrait vous frapper dans le code ci-dessus est que la valeur de `1rem` dans les media queries définies est toujours de `16px`. `1rem` à l'intérieur des blocs de media queries suit la définition racine de `font-size` de 62,5 % de `16px`, ce qui est `10px` comme nous l'avons trouvé précédemment.

Ce comportement est dû au fait que le REM à l'intérieur des media queries prend toujours la valeur par défaut de la taille de police du navigateur, qui est souvent de `16px`. Cependant, si l'utilisateur modifie ce paramètre par défaut du navigateur, le REM prendra cette valeur. Cela signifie que les préférences d'accessibilité qu'un utilisateur aurait pu spécifier sont respectées.

Le code adopte une approche de conception mobile-first. Le premier point de rupture que j'ai défini est à `435px`. Remarquez que la largeur du texte après ce point de rupture ne change jamais, mais le rapport des valeurs autour change en proportion, 1,5 pour être exact. Voici des illustrations de chaque étape :

La mise en page lorsque la fenêtre d'affichage est inférieure à 435px :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Capture-1.JPG)
_Le conteneur occupe 100 % de la largeur pour les écrans mobiles_

La mise en page lorsque la fenêtre d'affichage est comprise entre `435px` et `652px` :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Capture1.JPG)
_Le conteneur maintient le texte à environ 10 mots par ligne_

La mise en page lorsque la fenêtre d'affichage est supérieure à `652px` :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Capture2.JPG)

## Conclusion

Dans cet article, nous avons exploré l'utilisation du REM en CSS. Nous avons vu que le REM est une valeur de longueur relative qui peut être utilisée pour créer un schéma logique des tailles de police à l'intérieur de vos pages web.

Son utilisation rend également vos pages web accessibles aux personnes qui ont besoin de modifier la valeur `font-size` par défaut du navigateur pour l'adapter à leurs besoins.

Enfin, nous avons exploré comment le REM peut vous aider à rendre une page web réactive, tout en tenant compte des éventuels changements de paramètres par défaut effectués par les utilisateurs qui ont besoin ou préfèrent d'autres réglages.

Lors de la rédaction de cet article, j'ai grandement bénéficié de ces articles :

* [Learn CSS Units – Em, Rem, VH, and VW with Code Examples](https://www.freecodecamp.org/news/learn-css-units-em-rem-vh-vw-with-code-examples/), par Joy Shaheb
* [CSS Unit Guide: CSS em, rem, vh, vw, and more, Explained](https://www.freecodecamp.org/news/css-unit-guide/), de freeCodeCamp
* [CSS Unit Battle: EMs Vs. REMs…FIGHT!](https://www.freecodecamp.org/news/em-units-versus-rem-units-fight-382c16af8a67/), par ZAYDEK
* [Rem in CSS: Understanding and Using rem Units](https://www.sitepoint.com/understanding-and-using-rem-units-in-css/), par Adrian Sandu
* [CSS values and units](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Values_and_units), [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/length), [font-size](https://developer.mozilla.org/en-US/docs/Web/CSS/font-size), par MDN
* [Accessible responsive design](https://web.dev/accessible-responsive-design/), par Dave Gash, Meggin Kearney, Rachel Andrew, Rob Dodson
* [Responsive web design basics](https://web.dev/responsive-web-design-basics/), par Pete LePage et Rachel Andrew

Photo de couverture par **[Sora Shimazaki](https://www.pexels.com/nl-nl/@sora-shimazaki?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels)** via Pexels.