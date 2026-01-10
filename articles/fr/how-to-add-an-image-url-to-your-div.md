---
title: Image de fond CSS – Comment ajouter une URL d'image à votre Div
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-05T11:22:36.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-an-image-url-to-your-div
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/w-qjCHPZbeXCQ-unsplash.jpg
tags:
- name: CSS
  slug: css
- name: css properties
  slug: css-properties
- name: Design
  slug: design
- name: image
  slug: image
- name: programing
  slug: programing
seo_title: Image de fond CSS – Comment ajouter une URL d'image à votre Div
seo_desc: "By Amy Haddad\nSay you want to put an image or two on a webpage. One way\
  \ is to use the background-image CSS property. \nThis property applies one or more\
  \ background images to an element, like a <div>, as the documentation explains.\
  \ Use it for aesthetic..."
---

Par Amy Haddad

Disons que vous souhaitez placer une ou deux images sur une page web. Une façon de le faire est d'utiliser la propriété CSS **`background-image`**. 

Cette propriété applique une ou plusieurs images de fond à un élément, comme un **`<div>`**, comme l'explique la [documentation](https://developer.mozilla.org/en-US/docs/Web/CSS/background-image). Utilisez-la pour des raisons esthétiques, comme ajouter un fond texturé à votre page web.

# Ajouter une image

Il est facile d'ajouter une image en utilisant la propriété `background-image`. Il suffit de fournir le chemin de l'image dans la valeur `url()`.

Le chemin de l'image peut être une URL, comme montré dans l'exemple ci-dessous :

```css
div {
   /* Motif de fond de Toptal Subtle Patterns */
   background-image: url("https://amymhaddad.s3.amazonaws.com/morocco-blue.png");
   height: 400px;
   width: 100%;
}
```
 

Ou cela peut être un chemin local. Voici un exemple :

```css
body {
   /* Motif de fond de Toptal Subtle Patterns */
   height: 400px;
   width: 100%;
   background-image: url("./images/oriental-tiles.png");
}
```

# Ajouter plusieurs images

Vous pouvez appliquer plusieurs images à la propriété `background-image`.

```css
div {
/* Motif de fond de Toptal Subtle Patterns */
   height: 400px;
   width: 100%;
   background-image: 
       url("https://amymhaddad.s3.amazonaws.com/morocco-blue.png"),
       url("https://amymhaddad.s3.amazonaws.com/oriental-tiles.png");
   background-repeat: no-repeat, no-repeat;
   background-position: right, left; 
}
```

C'est beaucoup de code. Décomposons-le.

Séparez chaque valeur d'image `url()` par une virgule.

```css
background-image: 
    url("https://amymhaddad.s3.amazonaws.com/morocco-blue.png"),
    url("https://amymhaddad.s3.amazonaws.com/oriental-tiles.png");
```

Maintenant, positionnez et améliorez vos images en appliquant des propriétés supplémentaires.

```css
background-repeat: no-repeat, no-repeat;
background-position: right, left; 
```

Il existe plusieurs [sous-propriétés](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Backgrounds_and_Borders/Using_multiple_backgrounds) que vous pouvez ajouter à vos images de fond, telles que **`background-repeat`** et **`background-position`**, que nous avons utilisées dans l'exemple ci-dessus. Vous pouvez même ajouter des [dégradés](https://developer.mozilla.org/en-US/docs/Web/CSS/gradient) à une image de fond.

Voyez à quoi cela ressemble lorsque nous mettons tout ensemble.

%[https://codepen.io/amymhaddad/pen/VwLqWbm]

# L'ordre compte

L'ordre dans lequel vous listez vos images est important en raison de l'ordre de superposition. Cela signifie que la première image listée est la plus proche de l'utilisateur, selon la [documentation](https://www.w3.org/TR/css-backgrounds-3/#layering). Ensuite, la suivante, et ainsi de suite. 

Voici un exemple.

```css
div {
/* Motif de fond de Toptal Subtle Patterns */
   height: 400px;
   width: 100%;
   background-image: 
       url("https://amymhaddad.s3.amazonaws.com/morocco-blue.png"),
       url("https://amymhaddad.s3.amazonaws.com/oriental-tiles.png");
   background-repeat: no-repeat, no-repeat;
}
```

Nous avons listé deux images dans le code ci-dessus. La première image (morocco-blue.png) sera devant la seconde (oriental-tiles.png). Les deux images sont de la même taille et n'ont pas d'opacité, donc nous ne voyons que la première image.

Mais si nous déplaçons la deuxième image (oriental-tiles.png) de 200 pixels vers la droite, alors vous pouvez en voir une partie (le reste reste caché).

Voici à quoi cela ressemble lorsque nous mettons tout ensemble.

%[https://codepen.io/amymhaddad/pen/oNXrXMo]

## Quand devez-vous utiliser l'image de fond ?

Il y a beaucoup de choses à aimer concernant la propriété `background-image`. Mais il y a un inconvénient. 

L'image peut ne pas être accessible à tous les utilisateurs, comme le souligne la [documentation](https://developer.mozilla.org/en-US/docs/Web/CSS/background-image), comme ceux qui utilisent des lecteurs d'écran.

C'est parce que vous ne pouvez pas ajouter d'informations textuelles à la propriété `background-image`. Par conséquent, l'image sera manquée par les lecteurs d'écran.

Utilisez la propriété `background-image` uniquement lorsque vous devez ajouter une décoration à votre page. Sinon, utilisez l'élément HTML **`<img>`** si une image a un sens ou un but, comme le note la [documentation](https://developer.mozilla.org/en-US/docs/Web/CSS/background-image).

De cette façon, vous pouvez ajouter du texte à un élément image, en utilisant l'attribut **`alt`**, qui [décrit l'image](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img). Le texte fourni sera capté par les lecteurs d'écran.

```html
<img class="house" 
       src="./images/farnsworth_house.jpeg"
       alt="Une maison en verre conçue par Ludwig Mies van der Rohe située à Plano, Illinois.">
```

Pensez-y de cette manière : `background-image` est une propriété CSS, et CSS se concentre sur la présentation ou le style ; HTML se concentre sur la sémantique ou le sens. 

En ce qui concerne les images, vous avez des options. Si une image est nécessaire pour la décoration, alors la propriété `background-image` peut être un bon choix pour vous.

_J'écris sur l'apprentissage de la programmation et les meilleures façons de s'y prendre (_[amymhaddad.com](https://amymhaddad.com/)).