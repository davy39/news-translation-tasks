---
title: Tutoriel sur la taille de police CSS – Comment changer la taille du texte en
  HTML
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-09-28T13:50:54.000Z'
originalURL: https://freecodecamp.org/news/css-font-size-tutorial-how-to-change-text-size-in-html
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/font.jpg
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: HTML
  slug: html
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Tutoriel sur la taille de police CSS – Comment changer la taille du texte
  en HTML
seo_desc: "By Amy Haddad\nUse the CSS font-size property to determine the size of\
  \ your text.\n.container {\n    font-size: 33px;\n}\n\nThis property takes several\
  \ types of values:\n\nKeywords (absolute-size and relative-size keywords),\nLength\
  \ (such as pixels (px) and e..."
---

Par Amy Haddad

Utilisez la propriété CSS **`font-size`** pour déterminer la taille de votre texte.

```css
.container {
    font-size: 33px;
}
```

Cette propriété accepte plusieurs types de valeurs :

* Mots-clés (mots-clés de taille absolue et relative),
* Longueur (comme les pixels (px) et les unités em), et
* Pourcentages.

```css
.container {
    font-size: xx-large;
}
```

La question est : quel type de valeur devez-vous choisir et pourquoi ? 

C'est la question à laquelle cet article répond. Il vous montrera comment utiliser la propriété `font-size` et les différences entre ses nombreuses valeurs. Ainsi, la prochaine fois que vous devrez changer la taille de la police de votre texte, vous saurez quelle valeur utiliser.

## Valeurs de mots-clés

Il existe deux types de valeurs de mots-clés que vous pouvez utiliser avec la taille de la police : les mots-clés `absolute-size` et `relative-size`. Commençons par les valeurs absolues.

### Mots-clés de taille absolue

Le code ci-dessous utilise le mot-clé de taille absolue **`small`** pour dimensionner le texte HTML.

```css
.childElement {
    font-size: small;
}
```

Il existe d'autres options de mots-clés de taille absolue parmi lesquelles choisir :

* xx-small
* x-small
* small
* medium
* large
* x-large
* xx-large
* xxx-large

La valeur d'un mot-clé de taille absolue est déterminée par la [taille de police par défaut](https://developer.mozilla.org/en-US/docs/Web/CSS/font-size) du navigateur. Typiquement, cette taille est medium.

## Mots-clés de taille relative

Les mots-clés de taille relative sont une autre option de mot-clé à considérer. Vous avez deux choix : **`smaller`** et **`larger`**.

```css 
.parentElement {
    font-size: smaller;
}
```

La taille de la police d'un élément avec un mot-clé de taille relative est _relative_—plus grande ou plus petite—par rapport à la taille de la police de son parent. 

En d'autres termes, la taille de la police de l'élément parent affecte la taille de la police de l'élément enfant, comme vous pouvez le voir ci-dessous.

%[https://codepen.io/amymhaddad/pen/eYZLNGN]

Dans cet exemple, le mot-clé de taille relative **`smaller`** est appliqué à l'élément enfant, et la valeur de taille absolue **`large`** est appliquée à l'élément parent.

# Valeurs de longueur

`font-size` accepte plusieurs valeurs de longueur différentes. Nous allons explorer trois d'entre elles : les pixels (px) et les unités em et rem. Malgré votre sélection, la valeur de longueur que vous utilisez doit être positive.

```css
.parentElement {
    font-size: 60px;
}
```

### Pixels

Les pixels sont une [unité de longueur absolue](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Values_and_units). Cela signifie qu'ils ne sont _pas_ affectés par d'autres éléments, comme l'élément parent, ou la taille de la fenêtre.

En conséquence, les pixels sont précis : vous définissez le nombre exact de pixels dont vous avez besoin sur un élément et c'est généralement ce que vous obtenez. Cependant, il peut y avoir de légères différences entre les navigateurs.

%[https://codepen.io/amymhaddad/pen/KKzRbMb]

Remarquez que les éléments enfants utilisent des `pixels` et ont la même taille de police dans l'exemple de code ci-dessus. 

## EMs

Alors que vous pouvez considérer les pixels comme fixes, pensez aux valeurs em comme variables. 

C'est parce que les valeurs em sont une [unité de longueur relative](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Values_and_units). La taille de la police d'un élément qui utilise une valeur em est _relative_ à la taille de la police de son parent.   

Cependant, disons que vous n'avez pas défini de taille de police pour l'élément parent. Ni n'en avez-vous défini un ailleurs plus haut dans le DOM. Dans ce cas, la valeur em est calculée en utilisant [la valeur par défaut du navigateur](https://developer.mozilla.org/en-US/docs/Web/CSS/font-size) (souvent 16px).

Rendons cette idée concrète. 

Disons que l'élément parent est défini à 30px et que l'élément enfant est défini à 2em. Alors, la taille de police rendue de l'élément enfant est de 60px (2 x 30px = 60px). Vous pouvez voir ce scénario dans le code ci-dessous.

%[https://codepen.io/amymhaddad/pen/zYqJrOJ]

Les valeurs em peuvent être problématiques en raison de leur effet de composition, qui est démontré dans l'exemple suivant.

%[https://codepen.io/amymhaddad/pen/LYNBjOp]

Lorsque vous avez plusieurs éléments qui utilisent des valeurs em imbriqués les uns dans les autres, les valeurs de taille de police se composent : elles deviennent de plus en plus grandes. C'est l'effet de composition en action.

## REMs

Voici les valeurs rem, qui ont été créées pour traiter le problème de composition des ems. 

Rappelons que les valeurs em sont relatives à l'élément parent. En revanche, les valeurs rem sont relatives à la taille de la police de l'élément racine (html).  

Cela signifie que vous pouvez appliquer une valeur rem à un élément, et elle ne sera pas affectée par la taille de la police du parent. Cela évite l'effet de composition que nous avons rencontré ci-dessus.

Cet exemple utilise la propriété `font-size` avec une valeur rem.

%[https://codepen.io/amymhaddad/pen/JjXByvd]

Voici un point clé de l'exemple ci-dessus : la taille de la police de l'élément parent n'affecte _pas_ la taille de la police des éléments enfants.

# Pourcentages

Les pourcentages offrent encore une autre façon de définir la taille de la police _relative_ à la taille de la police de l'élément parent. 

L'élément avec le pourcentage fait référence à son élément parent pour déterminer sa taille de police. La valeur en pourcentage doit être positive. 

Voici un exemple.

%[https://codepen.io/amymhaddad/pen/mdPjMjw]

Comme vous pouvez le voir, en matière de taille de police, vous avez de nombreuses options pour répondre à vos besoins.

_J'écris sur l'apprentissage de la programmation, et les meilleures façons de s'y prendre sur [amymhaddad.com](http://amymhaddad.com/)._ Je tweete également sur la programmation, l'apprentissage et la productivité : [@amymhaddad](https://twitter.com/amymhaddad).