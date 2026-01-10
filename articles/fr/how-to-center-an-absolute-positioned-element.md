---
title: Comment centrer un élément positionné en absolu verticalement et horizontalement
  avec CSS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-05-06T19:56:35.000Z'
originalURL: https://freecodecamp.org/news/how-to-center-an-absolute-positioned-element
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/pexels-jack-hawley-57905.jpg
tags:
- name: CSS
  slug: css
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Comment centrer un élément positionné en absolu verticalement et horizontalement
  avec CSS
seo_desc: 'By Dillion Megida

  Absolute positioned elements are removed from the flow of a document. And sometimes,
  knowing how to correctly position such elements in the center of the page can be
  confusing.

  I mean, CSS is confusing already. 😅

  In this article, I...'
---

Par Dillion Megida

Les éléments positionnés en absolu sont retirés du flux d'un document. Et parfois, savoir comment positionner correctement de tels éléments au centre de la page peut être déroutant.

Je veux dire, CSS est déjà déroutant. 😅

Dans cet article, je vais vous montrer comment centrer un élément absolu soit verticalement, soit horizontalement – ou les deux – dans un conteneur.

## Exemple de code

Pour centrer un élément horizontalement :

```css
élément {
  position: absolute;
  left: 0;
  right: 0;
  margin: 0 auto;
}
```

Pour centrer un élément verticalement :

```css
élément {
  position: absolute;
  top: 0;
  bottom: 0;
  margin: auto 0;
}
```

Pour centrer un élément à la fois verticalement et horizontalement :

```css
  position: absolute;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  margin: auto;
```

Mais si vous souhaitez comprendre comment je suis parvenu à ces solutions, lisez la suite pour plus d'explications.

## Comment fonctionne le positionnement absolu ?

Par défaut, les éléments ont une position `static` sauf indication contraire comme `absolute`, `fixed`, `relative` ou `sticky`. Vous pouvez lire [cet article sur les styles de position CSS](https://dillionmegida.com/p/static-relative-absolute-fixed-sticky-positions/) pour comprendre la différence.

Je vais utiliser l'interface suivante pour expliquer comment les éléments `absolute` fonctionnent :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-32.png)

Voici le code pour l'interface :

```html
<div class="container">
  <div class="blue-block"></div>
  <div class="green-block"></div>
  <div class="black-block"></div>
</div>
```

```css
.container {
  margin: 20px;
  display: flex;
  border: 1px solid black;
  padding: 20px;
  width: 400px;
}

.blue-block,
.green-block,
.black-block {
  width: 100px;
  height: 100px;
}

.blue-block {
  background-color: blue;
}

.green-block {
  background-color: green;
}

.black-block {
  background-color: black;
}
```

Ce conteneur a trois blocs : bleu, vert et noir, respectivement. Tous les blocs sont actuellement `static`, donc ils sont ordonnés de la même manière dans le DOM, tout comme ils le sont dans le code.

Que se passe-t-il lorsque vous donnez au bloc vert une position `absolute` :

```css
.green-block {
  background-color: green;
  position: absolute;
  margin-left: 20px;
  margin-top: 20px;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-31.png)

Vous pouvez voir maintenant que le bloc vert a quitté le flux du document. Le conteneur n'applique l'affichage flex qu'aux éléments bleu et noir, et le bloc vert se déplace sans affecter les autres.

Alors, que faire si nous voulions positionner ce bloc vert au centre du conteneur ?

## Comment positionner les éléments absolus au centre

Le positionnement des éléments statiques au centre implique généralement des marges automatiques, donc un `margin: auto` devrait suffire, n'est-ce pas ?

```css
.green-block {
  background-color: green;
  position: absolute;
  margin: auto;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-33.png)

Cela ne fonctionne définitivement pas. En tant qu'élément `absolute`, il perd son flux dans le conteneur. Peut-être un `left: auto` et `right: auto` alors :

```css
.green-block {
  background-color: green;
  position: absolute;
  left: auto;
  right: auto;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-34.png)

Toujours rien. À ce stade, vous pourriez être tenté d'utiliser des valeurs codées en dur :

```css
.blue-block, .black-block {
  display: none;
}

.green-block {
  background-color: green;
  position: absolute;
  left: 190px;
  top: 90px;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-35.png)

Ce résultat semble parfait (ou presque) mais ce n'est pas la meilleure solution car lorsque vous changez la taille du conteneur, vous devez changer les valeurs codées en dur.

Maintenant, voyons comment vous pouvez centrer des éléments positionnés en absolu.

La première partie consiste à appliquer une position `relative` au conteneur :

```css
.container {
  // ...
  position: relative;
}
```

L'application d'une position relative au conteneur donne à l'élément absolu une frontière. Les éléments absolus sont limités par le parent positionné en relatif le plus proche. Mais si aucun de ceux-ci n'existe, ils seront limités par la fenêtre d'affichage.

Ensuite, nous allons centrer le bloc horizontalement. Appliquez une propriété `left` et `right` avec la valeur 0. Ces propriétés spécifient respectivement la distance du bord gauche (du bloc) au conteneur et du bord droit au conteneur.

```css
.green-block {
  // ...
  left: 0;
  right: 0;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-36.png)

La propriété `left` prend plus de precedence car le conteneur affiche les éléments de gauche à droite.

La beauté vient avec le style suivant :

```css
.green-block {
  // ...
  margin: 0 auto;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-37.png)

Et vous avez un élément absolu centré horizontalement. Pensez aux propriétés `left` et `right` spécifiant un conteneur interne pour le bloc. Dans ce conteneur, les marges gauche et droite peuvent être `auto` afin qu'elles soient égales et amènent l'élément au centre.

Pour centrer ce bloc verticalement, vous pouvez déjà deviner que cela se fait ainsi :

```css
.green-block {
  // ...
  top: 0;
  bottom: 0;
  margin: auto 0;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-39.png)

Les propriétés `top` et `bottom` spécifient la distance entre les bords supérieur et inférieur du bloc, ce qui ressemble à un conteneur interne. L'utilisation de `auto` crée des marges égales pour `margin-top` et `margin-bottom`.

En combinant les deux concepts, vous pouvez centrer le bloc horizontalement et verticalement comme ceci :

```css
.green-block {
  background-color: green;
  position: absolute;
  right: 0;
  left: 0;
  top: 0;
  bottom: 0;
  margin: auto;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-38.png)

Avec cette approche, l'élément reste au centre si vous redimensionnez le conteneur.

## Conclusion

Les éléments absolus se comportent différemment des éléments statiques – ils quittent le flux du document et, par défaut, ne respectent pas le conteneur dans lequel ils ont été déclarés.

Avec un élément parent positionné en `relative`, un élément positionné en `absolute` a une frontière. Et avec les propriétés `left`, `right`, `top` et `bottom` avec une valeur de **0** (spécifiant la distance des bords), et une marge **auto**, l'élément absolu est centré dans l'élément parent.

Notez que ce n'est pas la seule façon de positionner les éléments absolus au centre. J'ai vu quelqu'un en ligne utiliser un `transform: translate...` pour y parvenir, aussi. Vous pouvez vous pencher sur cette méthode si vous le souhaitez.