---
title: La propriété CSS Position expliquée avec des exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-16T13:00:00.000Z'
originalURL: https://freecodecamp.org/news/learn-the-basics-the-css-position-property
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a3e740569d1a4ca247b.jpg
tags:
- name: 100DaysOfCode
  slug: 100daysofcode
- name: code newbie
  slug: code-newbie
- name: CSS
  slug: css
seo_title: La propriété CSS Position expliquée avec des exemples
seo_desc: "By Sarah Chima Atuonwu\nBefore you can be really good at CSS you need to\
  \ understand the basics. You have to understand CSS properties and their values.\
  \ \nIn this article, we'll focus on the CSS position property. We are going to learn\
  \ the various value..."
---

Par Sarah Chima Atuonwu

Avant de pouvoir vraiment maîtriser CSS, vous devez comprendre les bases. Vous devez comprendre les propriétés CSS et leurs valeurs. 

Dans cet article, nous allons nous concentrer sur la propriété de position CSS. Nous allons apprendre les différentes valeurs de la propriété de position CSS et comment elles fonctionnent. C'est parti !

## Qu'est-ce que la propriété de position CSS ?

La propriété de position CSS définit la position d'un élément dans un document. Cette propriété fonctionne avec les propriétés left, right, top, bottom et z-index pour déterminer la position finale d'un élément sur une page.

Il y a cinq valeurs que la propriété position peut prendre. Ce sont :

1. static
2. relative
3. absolute
4. fixed
5. sticky

Discutons de chacune d'elles.

### Static

Il s'agit de la valeur par défaut pour les éléments. L'élément est positionné selon le flux normal du document. Les propriétés left, right, top, bottom et z-index n'affectent pas un élément avec `position: static`.

Utilisons un exemple pour montrer que `position: static` n'a aucun effet sur la position d'un élément. Nous avons trois divs placées dans un conteneur parent. Nous utiliserons cet exemple tout au long de cet article.

```html
<html>
	<body>
        <div class="parent-element">
            <div class="sibling-element">
                Je suis l'autre élément frère.
            </div>
            
            <div class="main-element">
                Tous les yeux sur moi. Je suis l'élément principal.
            </div>
            
            <div class="sibling-element">
                Je suis l'autre élément frère.
            </div>
        </div>
    </body>
<html>
```

Ajoutons `position: static` à la div avec la classe `main-element` et les valeurs left, top. Nous ajoutons également quelques styles aux autres divs pour les différencier de l'élément en focus.

```css
.main-element {
    position: static;
    left: 10px;
    bottom: 10px;
    background-color: yellow;
    padding: 10px;
}

.sibling-element {
    padding: 10px;
    background-color: #f2f2f2;
}
```

Voici le résultat.

<iframe width="100%" height="300" src="//jsfiddle.net/sarahchima/4vsm3o1d/5/embedded/result,css/" allowfullscreen="allowfullscreen" allowpaymentrequest frameborder="0"></iframe>

Avez-vous remarqué qu'il n'y a pas de changement ? Cela confirme le fait que les propriétés left et bottom n'affectent pas un élément avec `position: static`.

Passons à la valeur suivante.

### Relative

Les éléments avec `position: relative` restent dans le flux normal du document. Mais, contrairement aux éléments statiques, les propriétés left, right, top, bottom et z-index affectent la position de l'élément. Un décalage, basé sur les valeurs des propriétés left, right, top et bottom, est appliqué à l'élément par rapport à lui-même.

Remplaçons `position: static` par `position: relative` dans notre exemple.

```css
.main-element {
    position: relative;
    left: 10px;
    bottom: 10px;
    background-color: yellow;
    padding: 10px;
}
```

<iframe width="100%" height="300" src="//jsfiddle.net/sarahchima/78tbavnu/14/embedded/result,css/" allowfullscreen="allowfullscreen" allowpaymentrequest frameborder="0"></iframe>

Remarquez que les propriétés left et bottom affectent maintenant la position de l'élément. Remarquez également que l'élément reste dans le flux normal du document et que le décalage est appliqué par rapport à lui-même. Prenez note de cela alors que nous passons à d'autres valeurs.

### Absolute

Les éléments avec `position: absolute` sont positionnés par rapport à leurs éléments parents. Dans ce cas, l'élément est retiré du flux normal du document. Les autres éléments se comporteront comme si cet élément n'était pas dans le document. Aucun espace n'est créé pour l'élément dans la mise en page. Les valeurs de left, top, bottom et right déterminent la position finale de l'élément.

Une chose à noter est qu'un élément avec `position: absolute` est positionné par rapport à son ancêtre positionné le plus proche. Cela signifie que l'élément parent doit avoir une valeur de position autre que `position: static`. 

Si l'élément parent le plus proche n'est pas positionné, il est positionné par rapport à l'élément parent suivant qui est positionné. S'il n'y a pas d'élément ancêtre positionné, il est positionné par rapport à l'élément `<html>`.

Revenons à notre exemple. Dans ce cas, nous changeons la position de l'élément principal en `position: absolute`. Nous donnerons également à son élément parent une position relative afin qu'il ne soit pas positionné par rapport à l'élément `<html>`.

```css
.main-element {
    position: absolute;
    left: 10px;
    bottom: 10px;
    background-color: yellow;
    padding: 10px;
}

.parent-element {
    position: relative;
    height: 100px;
    padding: 10px;
    background-color: #81adc8;
}

.sibling-element {
	background: #f2f2f2;
	padding: 10px;
    border: 1px solid #81adc8;
} 
```

Voici le résultat.

<iframe width="100%" height="300" src="//jsfiddle.net/sarahchima/5qyp4m2z/5/embedded/result,css/" allowfullscreen="allowfullscreen" allowpaymentrequest frameborder="0"></iframe>

Remarquez qu'aucun espace n'a été créé dans le document pour l'élément. L'élément est maintenant positionné par rapport à l'élément parent. Prenez note de cela alors que nous passons à la valeur suivante.

### Fixed

Les éléments en position fixe sont similaires aux éléments positionnés de manière absolue. Ils sont également retirés du flux normal du document. Mais contrairement aux éléments positionnés de manière absolue, ils sont toujours positionnés par rapport à l'élément `<html>`. 

Une chose à noter est que les éléments fixes ne sont pas affectés par le défilement. Ils restent toujours dans la même position à l'écran.

```css
.main-element {
    position: fixed;
    bottom: 10px;
    left: 10px;
    background-color: yellow;
    padding: 10px;
}

html {
    height: 800px;
}
```

<iframe width="100%" height="300" src="//jsfiddle.net/sarahchima/L4gsxwft/2/embedded/result,css/" allowfullscreen="allowfullscreen" allowpaymentrequest frameborder="0"></iframe>

Dans ce cas, l'élément est positionné par rapport à l'élément `<html>`. Essayez de faire défiler pour voir que l'élément reste fixe à l'écran.

Passons à la dernière valeur.

### Sticky

`position: sticky` est un mélange de `position: relative` et `position: fixed`. Il se comporte comme un élément positionné de manière relative jusqu'à un certain point de défilement, puis il se comporte comme un élément fixe. N'ayez pas peur si vous ne comprenez pas ce que cela signifie, l'exemple vous aidera à mieux comprendre.

```css
.main-element {
    position: sticky;
    top: 10px;
    background-color: yellow;
    padding: 10px;
}

.parent-element {
    position: relative;
    height: 800px;
    padding: 50px 10px;
    background-color: #81adc8;
}
```

<iframe width="100%" height="300" src="//jsfiddle.net/sarahchima/f3m0qxgn/8/embedded/result,css/" allowfullscreen="allowfullscreen" allowpaymentrequest frameborder="0"></iframe>

Faites défiler l'onglet résultat pour voir le résultat. Vous voyez qu'il se comporte comme un élément relatif jusqu'à ce qu'il atteigne un certain point à l'écran, `top: 10px`, puis il reste là comme un élément fixe.

## Résumé

Oups ! Cela a été un long voyage. Mais j'espère vraiment que cet article vous a aidé à comprendre la propriété de position CSS et comment elle fonctionne. 

N'hésitez pas à jouer avec les exemples si vous ne les comprenez pas complètement. Vous pouvez changer les valeurs et remarquer la différence ou mieux encore, essayez d'utiliser la propriété de position pour travailler sur un projet personnel.

Rappelez-vous que pour devenir meilleur en CSS, il faut une pratique constante. Alors continuez à pratiquer et vous vous améliorerez.

_Voulez-vous être informé lorsque je publie un nouvel article ? [Cliquez ici](https://mailchi.mp/69ea601a3f64/join-sarahs-mailing-list)._