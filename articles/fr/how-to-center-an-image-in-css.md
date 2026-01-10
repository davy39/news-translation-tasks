---
title: Comment centrer une image verticalement et horizontalement avec CSS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-14T22:29:18.000Z'
originalURL: https://freecodecamp.org/news/how-to-center-an-image-in-css
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a4c740569d1a4ca24c2.jpg
tags:
- name: CSS
  slug: css
seo_title: Comment centrer une image verticalement et horizontalement avec CSS
seo_desc: 'By Cem Eygi

  Many developers struggle while working with images. Handling responsiveness and
  alignment is particularly tough, especially centering an image in the middle of
  the page.

  So in this post, I will be showing some of the most common ways to c...'
---

Par Cem Eygi

De nombreux développeurs ont du mal à travailler avec des images. Gérer la [réactivité](https://www.freecodecamp.org/news/css-responsive-image-tutorial/) et l'alignement est particulièrement difficile, surtout pour centrer une image au milieu de la page.

Dans cet article, je vais donc montrer certaines des méthodes les plus courantes pour centrer une image à la fois verticalement et horizontalement en utilisant différentes propriétés CSS.

### Voici un scrim interactif sur la façon de centrer une image verticalement et horizontalement :

<iframe src="https://scrimba.com/scrim/cmPm8eSw?embed=freecodecamp,mini-header" width="100%" height="420"></iframe>

J'ai abordé les propriétés CSS [Position](https://www.freecodecamp.org/news/how-to-use-the-position-property-in-css-to-align-elements-d8f49c403a26/) et [Display](https://www.youtube.com/watch?v=hgoFi0fCv3w) dans mon précédent article. Si vous n'êtes pas familier avec ces propriétés, je vous recommande de consulter ces articles avant de lire celui-ci.

Voici une version vidéo si vous souhaitez la consulter :

%[https://youtu.be/mwVNVxpkly0]

## Centrer une image horizontalement

Commençons par centrer une image horizontalement en utilisant 3 propriétés CSS différentes.

### Text-Align

La première façon de centrer une image horizontalement est d'utiliser la propriété `text-align`. Cependant, cette méthode ne fonctionne que si l'image est à l'intérieur d'un conteneur de niveau bloc tel qu'un `<div>` :

```html
<style>
  div {
    text-align: center;
  }
</style>

<div>
  <img src="votre-image.jpg">
</div>
```

### Margin: Auto

Une autre façon de centrer une image est d'utiliser la propriété `margin: auto` (pour la marge gauche et la marge droite).

Cependant, utiliser `margin: auto` seul ne fonctionnera pas pour les images. Si vous devez utiliser `margin: auto`, il y a 2 propriétés supplémentaires que vous devez également utiliser.

La propriété margin-auto n'a aucun effet sur les éléments de niveau inline. Puisque la balise `<img>` est un élément inline, nous devons d'abord la convertir en élément de niveau bloc :

```css
img {
  margin: auto;
  display: block;
}
```

Deuxièmement, nous devons également définir une largeur. Ainsi, les marges gauche et droite peuvent prendre le reste de l'espace vide et s'auto-aligner, ce qui fait le travail (sauf si nous lui donnons une largeur de 100 %) :

```css
img {
  width: 60%;
  margin: auto;
  display: block;
}
```

### Display: Flex

La troisième façon de centrer une image horizontalement est d'utiliser `display: flex`. Tout comme nous avons utilisé la propriété `text-align` pour un conteneur, nous utilisons `display: flex` pour un conteneur également.

Cependant, utiliser `display: flex` seul ne sera pas suffisant. Le conteneur doit également avoir une propriété supplémentaire appelée `justify-content` :

```css
div {
  display: flex;
  justify-content: center;
}

img {
  width: 60%;
}
```

La propriété `justify-content` fonctionne avec `display: flex`, que nous pouvons utiliser pour centrer l'image horizontalement.

Enfin, la largeur de l'image doit être inférieure à la largeur du conteneur, sinon elle prend 100 % de l'espace et nous ne pouvons pas la centrer.

**Important :** La propriété `display: flex` n'est pas supportée dans les anciennes versions des navigateurs. [Voir ici](https://caniuse.com/#search=display%20flex) pour plus de détails.

## Centrer une image verticalement

### Display: Flex

Pour l'alignement vertical, utiliser `display: flex` est à nouveau vraiment utile.

Considérons un cas où notre conteneur a une hauteur de 800px, mais la hauteur de l'image est seulement de 500px :

```css
div {
  display: flex;
  justify-content: center;
  height: 800px;
}

img {
  width: 60%;
  height: 500px;
}
```

Maintenant, dans ce cas, ajouter une seule ligne de code au conteneur, `align-items: center`, fait le travail :

```css
div {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 800px;
}
```

La propriété `align-items` peut positionner les éléments verticalement si elle est utilisée avec `display: flex`.

### Position: Absolute & Transform Properties

Une autre méthode pour l'alignement vertical consiste à utiliser les propriétés `position` et `transform` ensemble. Celle-ci est un peu compliquée, alors faisons-la étape par étape.

### Étape 1 : Définir Position Absolute

Tout d'abord, nous changeons le comportement de positionnement de l'image de `static` à `absolute` :

```css
div {
  height: 800px;
  position: relative;
  background: red;
}

img {
  width: 80%;
  position: absolute;
}
```

De plus, elle doit être à l'intérieur d'un conteneur positionné de manière relative, donc nous ajoutons `position: relative` à son div conteneur.

### Étape 2 : Définir les propriétés Top & Left

Deuxièmement, nous définissons les propriétés top et left pour l'image, et les définissons à 50 %. Cela déplacera le point de départ (en haut à gauche) de l'image au centre du conteneur :

```css
img {
  width: 80%;
  position: absolute;
  top: 50%;
  left: 50%;
}
```

### Étape 3 : Définir la propriété Transform

Mais la deuxième étape a déplacé l'image partiellement à l'extérieur de son conteneur. Nous devons donc la ramener à l'intérieur.

Définir une propriété `transform` et ajouter -50 % à son axe X et Y fait le travail :

```css
img {
  width: 80%;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
```

Il existe d'autres façons de centrer les éléments horizontalement et verticalement, mais j'ai expliqué les plus courantes. J'espère que cet article vous a aidé à comprendre comment aligner vos images au centre de la page.

**Si vous souhaitez en savoir plus sur le développement Web, n'hésitez pas à visiter ma [Chaîne YouTube](https://www.youtube.com/channel/UC1EgYPCvKCXFn8HlpoJwY3Q?view_as=subscriber) pour plus de contenu.**

Merci d'avoir lu !