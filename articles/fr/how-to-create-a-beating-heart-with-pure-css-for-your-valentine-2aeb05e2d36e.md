---
title: Comment créer un cœur battant avec du CSS pur pour votre Valentine
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-08T21:19:10.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-beating-heart-with-pure-css-for-your-valentine-2aeb05e2d36e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*lsB5T7aKYZHpcKBxq6gMog.gif
tags:
- name: animation
  slug: animation
- name: CSS
  slug: css
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment créer un cœur battant avec du CSS pur pour votre Valentine
seo_desc: 'By Dimitris Kiriakakis

  Each year on February 14th, many people exchange cards, candies, gifts or flowers
  with their special “valentine”. The day of romance we call Valentine’s Day is named
  for a Christian martyr and dates back to the 5th century, but...'
---

Par Dimitris Kiriakakis

Chaque année, le 14 février, de nombreuses personnes échangent des cartes, des bonbons, des cadeaux ou des fleurs avec leur "valentin" spécial. Le jour de la romance que nous appelons la Saint-Valentin tire son nom d'un martyr chrétien et remonte au 5ᵉ siècle, mais trouve ses origines dans la fête romaine des Lupercales.

Ok, jusqu'ici tout va bien. Mais que peut faire un programmeur pour sa Valentine ?

Ma réponse est : utilisez CSS et soyez créatif !

J'adore vraiment CSS. Ce n'est pas un langage vraiment sophistiqué (il n'est même pas considéré comme un langage de programmation la plupart du temps). Mais avec un peu de géométrie, de mathématiques et quelques règles de base de CSS, vous pouvez transformer votre navigateur en une toile de votre créativité !

Alors, commençons. Comment créer un cœur avec de la géométrie pure ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*WM5VHEgYLmAdW5Z8_LlX7w.jpeg)
_Un cœur fait d'un carré et de deux cercles_

Vous avez juste besoin d'un carré et de deux cercles. N'est-ce pas ?

Et nous pouvons dessiner cela avec un seul élément, grâce aux pseudo-éléments `::after` et `::before`. En parlant de pseudo-éléments, `::after` est un pseudo-élément qui permet d'insérer du contenu dans une page à partir de CSS (sans qu'il soit nécessaire qu'il soit dans le HTML). `::before` est exactement la même chose, sauf qu'il insère le `content` avant tout autre contenu dans le HTML au lieu de après.

Pour les deux pseudo-éléments, le résultat final n'est pas réellement dans le DOM, mais il apparaît sur la page comme s'il y était.

Alors, créons notre cœur.

```css
.heart {
  background-color: red;
  display: inline-block;
  height: 50px;
  margin: 0 10px;
  position: relative;
  top: 0;
  transform: rotate(-45deg);
  position: absolute; 
  left: 45%; top: 45%;
  width: 50px;
}

.heart:before,
.heart:after {
  content: "";
  background-color: red;
  border-radius: 50%;
  height: 50px;
  position: absolute;
  width: 50px;
}

.heart:before {
  top: -25px;
  left: 0;
}

.heart:after {
  left: 25px;
  top: 0;
}
```

Vous pouvez facilement remarquer que nous définissons le carré et son positionnement en utilisant la classe principale 'heart' et les deux cercles avec les pseudo-éléments `::before` et `::after`. Les cercles sont en fait deux autres carrés dont le border-radius est réduit de moitié.

_Mais qu'est-ce qu'un cœur sans battement ?_

Créons une pulsation. Ici, nous allons utiliser la règle @keyframes. La règle CSS @keyframes est utilisée pour définir le comportement d'un cycle d'une animation CSS.

Lorsque nous utilisons la règle keyframes, nous pouvons diviser une période de temps en parties plus petites et créer une transformation/animation en la divisant en étapes (chaque étape correspond à un pourcentage de l'achèvement de la période de temps).

Alors, créons le battement de cœur. Notre animation de battement de cœur se compose de 3 étapes :

```
@keyframes heartbeat {
  0% {
    transform: scale( 1 );    
  }
  20% {
    transform: scale( 1.25 ) 
      translateX(5%) 
      translateY(5%);
  } 
  40% {
    transform: scale( 1.5 ) 
      translateX(9%) 
      translateY(10%);
  }
}
```

1. À 0% de la période de temps, nous commençons sans transformation.
2. À 20% de la période de temps, nous redimensionnons notre forme à 125% de sa taille initiale.
3. À 40% de la période de temps, nous redimensionnons notre forme à 150% de sa taille initiale.

Pour les 60% restants de la période de temps, nous laissons le temps à notre cœur de revenir à son état initial.

Enfin, nous devons assigner l'animation à notre cœur.

```
.heart {
  animation: heartbeat 1s infinite; // notre cœur a un battement infini :)
  ...
}
```

**C'est tout !**

Nous avons un cœur battant qui battra pour toujours. 
Ou peut-être aussi longtemps que votre propre amour durera...

N'hésitez pas à consulter le Codepen associé :

Je vous souhaite une merveilleuse Saint-Valentin !