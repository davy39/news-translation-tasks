---
title: Une introduction rapide aux animations CSS
subtitle: ''
author: Flavio Copes
co_authors: []
series: null
date: '2018-05-03T15:47:53.000Z'
originalURL: https://freecodecamp.org/news/a-quick-introduction-to-css-animations-a1655375ec90
coverImage: https://cdn-media-1.freecodecamp.org/images/1*feAfQ6VwBLSlXlYVmUxqLQ.png
tags:
- name: CSS
  slug: css
- name: education
  slug: education
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Une introduction rapide aux animations CSS
seo_desc: "Interested in learning CSS? Get my CSS Handbook \n\nIntroduction\nAn animation\
  \ is applied to an element using the animation property.\n.container { animation:\
  \ spin 10s linear infinite;}\nspin is the name of the animation, which we need to\
  \ define separatel..."
---

> Intéressé par l'apprentissage de CSS ? Obtenez mon [CSS Handbook](https://flaviocopes.com/page/css-handbook/)

#### Introduction

Une animation est appliquée à un élément en utilisant la propriété `animation`.

```
.container { animation: spin 10s linear infinite;}
```

`spin` est le nom de l'animation, que nous devons définir séparément. Nous indiquons également à CSS de faire durer l'animation 10 secondes, de l'exécuter de manière linéaire (sans accélération ou différence de vitesse), et de la répéter indéfiniment.

Vous devez **définir comment votre animation fonctionne** en utilisant des **keyframes**. Voici un exemple d'animation qui fait tourner un élément :

```
@keyframes spin { 0% {  transform: rotateZ(0); } 100% {  transform: rotateZ(360deg); }}
```

À l'intérieur de la définition `@keyframes`, vous pouvez avoir autant de points intermédiaires que vous le souhaitez.

Dans ce cas, nous instruisons CSS à faire en sorte que la propriété transform fasse tourner l'axe Z de 0 à 360 degrés, complétant ainsi la boucle complète.

Vous pouvez utiliser n'importe quelle transformation CSS ici.

Remarquez comment cela ne dicte rien sur l'intervalle temporel que l'animation doit prendre. Cela est défini lorsque vous l'utilisez via `animation`.

#### Un exemple d'animations CSS

Je veux dessiner quatre cercles, tous avec un point de départ commun, tous à 90 degrés de distance les uns des autres.

```
<div class="container">  <div class="circle one"></div>  <div class="circle two"></div>  <div class="circle three"></div>  <div class="circle four"></div></div>
```

```
body {  display: grid;  place-items: center;  height: 100vh;}
```

```
.circle { border-radius: 50%; left: calc(50% - 6.25em); top: calc(50% - 12.5em); transform-origin: 50% 12.5em; width: 12.5em; height: 12.5em; position: absolute; box-shadow: 0 1em 2em rgba(0, 0, 0, .5);}
```

```
.one,.three { background: rgba(142, 92, 205, .75);}
```

```
.two,.four { background: rgba(236, 252, 100, .75);}
```

```
.one { transform: rotateZ(0);}
```

```
.two { transform: rotateZ(90deg);}
```

```
.three { transform: rotateZ(180deg);}
```

```
.four { transform: rotateZ(-90deg);}
```

Vous pouvez les voir dans ce Glitch :

Faisons tourner cette structure (tous les cercles ensemble). Pour ce faire, nous appliquons une animation sur le conteneur, et nous définissons cette animation comme une rotation de 360 degrés :

```
@keyframes spin { 0% {  transform: rotateZ(0); } 100% {  transform: rotateZ(360deg); }}
```

```
.container { animation: spin 10s linear infinite;}
```

Voir ici :

Vous pouvez ajouter plus de keyframes pour des animations plus amusantes :

```
@keyframes spin { 0% {  transform: rotateZ(0); } 25% {  transform: rotateZ(30deg); } 50% {  transform: rotateZ(270deg); } 75% {  transform: rotateZ(180deg); } 100% {  transform: rotateZ(360deg); }}
```

Voir l'exemple :

### Les propriétés d'animation CSS

Les animations CSS offrent de nombreux paramètres différents que vous pouvez ajuster :

* **animation-name** — le nom de l'animation qui référence une animation créée en utilisant des keyframes
* **animation-duration** — la durée de l'animation, en secondes
* **animation-timing-function** — la fonction de temporisation utilisée par l'animation (valeurs courantes : linear, ease). Par défaut : ease
* **animation-delay** — nombre de secondes optionnel à attendre avant de démarrer l'animation
* **animation-iteration-count** — le nombre de fois que l'animation doit être exécutée. Attend un nombre ou infinite. Par défaut : 1
* **animation-direction** — la direction de l'animation. Peut être normal, reverse, alternate ou alternate-reverse. Dans les deux derniers cas, elle alterne en allant vers l'avant puis vers l'arrière
* **animation-fill-mode** — définit comment styliser l'élément lorsque l'animation se termine, après avoir terminé son nombre d'itérations. None ou backwards reviennent aux styles du premier keyframe. Forwards et both utilisent le style défini dans le dernier keyframe
* **animation-play-state** — si défini sur paused, il met en pause l'animation. Par défaut, running.

La propriété `animation` est un raccourci pour toutes ces propriétés, dans cet ordre :

```
.container {  animation: name             duration             timing-function             delay             iteration-count             direction             fill-mode             play-state;}
```

Voici l'exemple que nous avons utilisé ci-dessus :

```
.container { animation: spin 10s linear infinite;}
```

### Événements JavaScript pour les animations CSS

En utilisant JavaScript, vous pouvez écouter les événements suivants :

* `animationstart`
* `animationend`
* `animationiteration`

Soyez prudent avec `animationstart`, car si l'animation commence au chargement de la page, votre code JavaScript est toujours exécuté après que le CSS a été traité. Ensuite, l'animation sera déjà démarrée et vous ne pourrez pas intercepter l'événement.

```
const container = document.querySelector('.container')container.addEventListener('animationstart', (e) => { //faire quelque chose}, false)container.addEventListener('animationend', (e) => { //faire quelque chose}, false)container.addEventListener('animationiteration', (e) => { //faire quelque chose}, false)
```

> Intéressé par l'apprentissage de CSS ? Obtenez mon [CSS Handbook](https://flaviocopes.com/page/css-handbook/)