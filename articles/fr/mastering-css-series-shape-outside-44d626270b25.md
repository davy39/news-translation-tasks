---
title: Pensez hors des sentiers battus avec CSS shape-outside
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-27T03:27:07.000Z'
originalURL: https://freecodecamp.org/news/mastering-css-series-shape-outside-44d626270b25
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ID4bv_7CvvjvM0CrsRUkYA.jpeg
tags:
- name: CSS
  slug: css
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Pensez hors des sentiers battus avec CSS shape-outside
seo_desc: 'By Jennifer Bland

  CSS is based off a box model. If you have an image that is a circle that you want
  to wrap text around, it will wrap around the images’ bounding box.


  Shape-outside

  A new CSS property called shape-outside lets you wrap text that conf...'
---

Par Jennifer Bland

CSS est basé sur un modèle de boîte. Si vous avez une image qui est un cercle autour duquel vous souhaitez envelopper du texte, il s'enroulera autour de la boîte de délimitation de l'image.

![Image](https://cdn-media-1.freecodecamp.org/images/QOIb5CyP4IQ3zh2DFfLujaqJTtzsc2R1GqIU)

### Shape-outside

Une nouvelle propriété CSS appelée shape-outside vous permet d'envelopper du texte qui épouse la forme de votre image.

![Image](https://cdn-media-1.freecodecamp.org/images/vQzt1aSIC6nhjSedXPFo3fFGZkCshyK0jwTj)

### Qu'est-ce que shape-outside

Shape-outside est une nouvelle propriété CSS qui change la forme des éléments qui sont enveloppés. Au lieu d'être limité à une boîte de délimitation rectangulaire autour de l'image, shape-outside nous permet de façonner le contenu pour qu'il épouse l'image.

Voici comment MDN décrit shape-outside :

> La propriété **shape-outside** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) utilise des valeurs de forme pour définir la zone de flottement d'un flottement et fera en sorte que le contenu en ligne s'enroule autour de la forme au lieu de la boîte de délimitation du flottement.

Le point le plus important à retenir de cette description est que cette nouvelle propriété s'applique aux images qui utilisent un flottement. La propriété CSS shape-outside contrôle la façon dont le texte s'enroule autour de toute image flottante. Le texte qui est enveloppé peut prendre la forme d'un cercle, d'une ellipse, d'un rectangle ou d'un polygone.

### Utilisation de shape-outside

La propriété shape-outside prend une "forme de base" et lui applique une fonction de forme. La fonction de forme est utilisée pour changer la forme de la zone de flottement de la forme. La propriété CSS shape-outside fournit des fonctionnalités pour créer ces fonctions de forme :

* cercle
* ellipse
* polygone
* rectangle
* url

L'image peut être positionnée avec ces valeurs. Les valeurs sont ajoutées à la fin :

* margin-box
* padding-box
* border-box

L'image doit avoir des dimensions intrinsèques. Vous devez définir la hauteur et la largeur de l'élément. Cela sera utilisé par la fonction de forme pour créer un système de coordonnées qui est utilisé lors de l'enveloppement du texte autour de l'image.

### Cercle

Circle() est l'une des valeurs fonctionnelles fournies avec shape-outside. La notation complète pour circle() est **_circle(r at cx cy)_** où r est le rayon du cercle et cx et cy sont les coordonnées du centre du cercle. Si vous les omettez, le centre de l'image sera utilisé comme valeurs par défaut.

Voici un exemple d'utilisation de shape-outside sur un cercle :

![Image](https://cdn-media-1.freecodecamp.org/images/8z6BO7xcccHnYv-nNK2hpIiLvVjXKjiUB24L)

```
.circle {    height: 200px;    width: 200px;    border-radius: 50%;    background-color: #7db9e8;    margin: 0 25px 5px 0;    float: left;    -webkit-shape-outside: circle();    shape-outside: circle();}
```

### Ellipse

L'ellipse est une variation du cercle où l'élément est allongé soit sur l'axe horizontal, soit sur l'axe vertical. La notation complète pour ellipse() est **_ellipse(rx ry at cx cy)_** où rx et ry sont les rayons de l'ellipse et cx et cy sont les coordonnées du centre de l'ellipse.

Voici un exemple d'utilisation de shape-outside sur l'ellipse :

![Image](https://cdn-media-1.freecodecamp.org/images/oGCsqOkrnFkc8zZjiMZ0fFNMpb1TY7oGIseW)

```
.ellipse {    width: 100px;    height: 200px;    border-radius: 50%;    background-color: #7db9e8;    margin: 0 25px 5px 0;    float: left;    -webkit-shape-outside: ellipse(50px 100px at 50% 50%);    shape-outside: ellipse(50px 100px at 50% 50%);}
```

### Polygone

La fonction polygone offre une gamme illimitée de formes. La notation complète pour polygon() est **_polygon(x1 y1, x2 y2, …)_** où chaque paire spécifie les coordonnées x y pour un sommet du polygone. Pour utiliser la fonction polygon(), vous devez spécifier un minimum de 3 paires de sommets.

Le polygone est utilisé avec un clip-path. La propriété CSS clip-path crée une région de rognage qui définit quelle partie d'un élément doit être affichée. Tout ce qui se trouve à l'intérieur de la région est affiché, tandis que ce qui se trouve à l'extérieur est masqué.

Voici un exemple d'utilisation de shape-outside pour créer deux formes triangulaires et le texte s'écoule entre elles :

![Image](https://cdn-media-1.freecodecamp.org/images/Z0k7nQxVswnodIuWaQtT8ydtNkQx0IAAgxig)

```
.leftTriangle {    width: 150px;    height: 300px;    background-color: #7db9e8;    margin: 0 25px 5px 0;    float: left;    -webkit-clip-path: polygon(0% 0%, 100% 0%, 50% 100%);    clip-path: polygon(0% 0%, 100% 0%, 50% 100%);    -webkit-shape-outside: polygon(0% 0%, 100% 0%, 50% 100%);    shape-outside: polygon(0% 0%, 100% 0%, 50% 100%);}.rightTriangle {    width: 150px;    height: 300px;    background-color: #7db9e8;    margin: 0 0 5px 25px;    float: right;    -webkit-clip-path: polygon(0% 0%, 100% 0%, 50% 100%);    clip-path: polygon(0% 0%, 100% 0%, 50% 100%);    -webkit-shape-outside: polygon(0% 0%, 100% 0%, 50% 100%);    shape-outside: polygon(0% 0%, 100% 0%, 50% 100%);}
```

### Support des navigateurs

La propriété CSS shape-outside est principalement supportée par Chrome, Opera et Safari.

![Image](https://cdn-media-1.freecodecamp.org/images/sWcg6Po3ESmOhYt-Pbqot0ArE2DDCZXyIL2Z)

### Obtenez le code

Le code de tous les exemples peut être trouvé dans [mon dépôt github ici](https://github.com/ratracegrad/mastering-css-series-shape-outside).

### Plus d'articles

Merci d'avoir lu mon article. Si vous l'aimez, veuillez cliquer sur l'icône d'applaudissements ci-dessous afin que d'autres puissent trouver l'article. Voici quelques-uns de mes autres articles qui pourraient vous intéresser :

[Voici 5 mises en page que vous pouvez réaliser avec FlexBox](https://medium.com/@ratracegrad/here-are-5-layouts-that-you-can-make-with-flexbox-6ca1e941f33d)
[Recherche en largeur d'abord en JavaScript](https://medium.com/@ratracegrad/breadth-first-search-in-javascript-e655cd824fa4)
[Modèles d'instantiation en JavaScript](https://medium.com/dailyjs/instantiation-patterns-in-javascript-8fdcf69e8f9b)