---
title: Comment créer un slider d'images avec jQuery
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-08T01:57:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-an-image-slider-with-jquery
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9cae740569d1a4ca3395.jpg
tags:
- name: HTML
  slug: html
- name: image
  slug: image
- name: JavaScript
  slug: javascript
- name: jQuery
  slug: jquery
- name: toothbrush
  slug: toothbrush
seo_title: Comment créer un slider d'images avec jQuery
seo_desc: 'This tutorial will walk you through building an image slider using the
  jQuery library.


  This tutorial will have four parts:


  HTML

  SCSS

  JS

  References


  HTML

  We will be using Bootstrap for this tutorial to keep things looking good, without
  spending a lo...'
---

Ce tutoriel vous guidera pas à pas pour créer un slider d'images en utilisant la bibliothèque [jQuery](https://jquery.com/).

![GIF montrant le slider en action](https://discourse-user-assets.s3.amazonaws.com/original/2X/0/08d83a22c28da836a06853b1f1ea669b398326b9.gif)

Ce tutoriel comportera quatre parties :

* [HTML](#html)
* [SCSS](#scss)
* [JS](#js)
* [Références](#references)

## **HTML**

Nous utiliserons [Bootstrap](http://getbootstrap.com/) pour ce tutoriel afin de garder les choses esthétiques sans passer trop de temps.

Notre structure sera la suivante :

```text
<div class="container">

  <!-- Le conteneur pour notre slider -->
  <div class="slider">
    <ul class="slides"><!-- Chaque image sera à l'intérieur de cette liste non ordonnée --></ul>
  </div>

  <div class="buttons"><!-- Les boutons pause et play iront ici --></div>

</div>
```

À l'intérieur de notre `ul` avec la classe `slides`, nous aurons ce qui suit :

```text
<li class="slide"><img src="#" /></li>
<li class="slide"><img src="#" /></li>
<li class="slide"><img src="#" /></li>
<li class="slide"><img src="#" /></li>
<li class="slide"><img src="#" /></li>
```

À l'intérieur de notre classe `.buttons`, vous devriez avoir ce qui suit :

```text
<button type="button" class="btn btn-default pause">
	<span class="glyphicon glyphicon-pause"></span>
</button>
<button type="button" class="btn btn-default play">
	<span class="glyphicon glyphicon-play"></span>
</button>
```

Voici un exemple de ce à quoi votre `html` devrait ressembler :

Remarque : Vous devriez remplacer l'attribut `src` des images par votre propre contenu.

```text
<div class="container">

  <div class="slider">
    <ul class="slides">
      <li class="slide"><img src="https://unsplash.it/1280/720/?image=120" /></li>
      <li class="slide"><img src="https://unsplash.it/1280/720/?image=70" /></li>
      <li class="slide"><img src="https://unsplash.it/1280/720/?image=50" /></li>
      <li class="slide"><img src="https://unsplash.it/1280/720/?image=170" /></li>
      <li class="slide"><img src="https://unsplash.it/1280/720/?image=190" /></li>
    </ul>
  </div>

  <div class="buttons">
    <button type="button" class="btn btn-default pause">
      <span class="glyphicon glyphicon-pause"></span>
    </button>
    <button type="button" class="btn btn-default play">
      <span class="glyphicon glyphicon-play"></span>
    </button>
  </div>

</div>
```

## **SCSS**

Nous utilisons [Sass](http://sass-lang.com/) et la syntaxe SCSS afin de pouvoir imbriquer et utiliser des variables.

![:heart_decoration:](https://forum.freecodecamp.com/images/emoji/emoji_one/heart_decoration.png?v=2)

Nous pouvons utiliser le SCSS suivant pour définir notre style :

```text
// Variables
$width: 720px;

.slider {
  width: $width;
  height: 400px;
  overflow: hidden;
  margin: 0 auto;
  text-align: center;

  .slides {
    display: block;
    width: 6000px;
    height: 400px;
    margin: 0;
    padding: 0;
  }

  .slide {
    float: left;
    list-style-type: none;
    width: $width;
    height: 400px;

    img {
      width: 100%;
      height: 100%;
    }
  }
}

.buttons {
  margin: 0;
  width: $width;
  position: relative;
  top: -40px;
  margin: 0 auto;

  .play {
    display: none;
  }

  .btn {
    display: flex;
    margin: 0 auto;
    text-align: center;
  }
}
```

## **JS**

#### **Variables**

_Dans l'extrait de code suivant, nous définissons les variables utilisées plus tard dans notre code._

```text
var animationSpeed = 1000; // La vitesse à laquelle la prochaine diapositive s'anime.
var pause = 3000; // La pause entre chaque diapositive.
```

Nous utiliserons une variable vide où nous appellerons la méthode `setInterval` :

```text
var interval;
```

#### **Animation Nous allons envelopper nos animations de slider à l'intérieur d'une fonction :**

```text
function startSlider() {}
```

Nous utilisons la méthode native JavaScript `setInterval()` pour automatiser le contenu de la fonction sur un déclencheur basé sur le temps.

```text
interval = setInterval(function() {}, pause);
```

Nous utilisons la variable `pause` pour voir combien de millisecondes attendre avant d'appeler à nouveau la fonction. Pour en savoir plus sur la méthode native `setInterval`, consultez : [https://developer.mozilla.org/en-US/docs/Web/API/WindowTimers/setInterval](https://developer.mozilla.org/en-US/docs/Web/API/WindowTimers/setInterval). À l'intérieur de notre fonction, nous utiliserons jQuery pour fondre entre les diapositives à la vitesse de la variable animationSpeed :

```text
$('.slides > li:first')
  .fadeOut(animationSpeed)
  .next()
  .fadeIn(animationSpeed)
  .end()
  .appendTo('.slides');
```

Nous ciblons la première diapositive en utilisant `$('.slides > li:first')`. - `.fadeOut(animationSpeed)` va estomper la première diapositive, puis en utilisant `.next()`, nous passons à la diapositive suivante. - Une fois que nous avons passé à la diapositive suivante, nous allons la faire apparaître : `.fadeIn(animationSpeed)`. - Cette séquence va continuer jusqu'à la dernière diapositive (`.end()`), puis nous arrêtons l'animation. Nous allons maintenant appeler la fonction `startSlider` pour démarrer l'animation :

startSlider();

#### **Lecture et Pause _Cette fonctionnalité est optionnelle, mais assez facile à implémenter._ Nous allons cacher le bouton lecture, afin de ne pas voir à la fois les boutons lecture et pause :**

```text
$('.play').hide(); // Masquer le bouton lecture.
```

Nous allons maintenant créer notre bouton pause (automatiquement affiché au chargement de la page) :

```text
$('.pause').click(function() {
	clearInterval(interval);
	$(this).hide();
	$('.play').show();
});
```

Nous allons appeler notre fonction chaque fois que le bouton pause est cliqué en utilisant jQuery. - Nous allons supprimer l'intervalle en utilisant la méthode `clearInterval` et en utilisant notre variable `interval` comme paramètre, indiquant quel intervalle arrêter. - Parce que notre slider est en pause, nous allons masquer le bouton pause en utilisant `$(this).hide();`. Remarque : nous utilisons `this`, qui fera référence à ce que notre parent appelle, c'est-à-dire `.pause`. - Nous allons ensuite afficher notre bouton lecture afin que l'utilisateur puisse reprendre l'animation : `$('.play').show();`. Le code suivant configure notre bouton lecture (automatiquement masqué au chargement de la page) :

```text
$('.play').click(function() {
	startSlider();
	$(this).hide();
	$('.pause').show();
});
```

Nous allons appeler notre fonction chaque fois que le bouton lecture est cliqué en utilisant jQuery.

* Nous allons démarrer ou redémarrer l'intervalle en utilisant la fonction `startSlider`.
* Parce que notre slider est actuellement en lecture, nous allons masquer le bouton lecture en utilisant `$(this).hide();`. Remarque : nous utilisons `this`, qui fera référence à ce que notre parent appelle, c'est-à-dire `.play`.
* Nous allons ensuite afficher notre bouton pause afin que l'utilisateur puisse arrêter l'animation à volonté : `$('.pause').show();`.

## **Références**

* Consultez le code source et l'exemple sur [CodePen](https://codepen.io/atjonathan/pen/BKMxxq) pour ce tutoriel.