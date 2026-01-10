---
title: Exemples de transitions CSS – Comment utiliser l'animation de survol, changer
  l'opacité et plus
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-10-13T17:18:52.000Z'
originalURL: https://freecodecamp.org/news/css-transition-examples
coverImage: https://www.freecodecamp.org/news/content/images/2020/10/Untitled--2--1.png
tags:
- name: animation
  slug: animation
- name: CSS
  slug: css
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: Exemples de transitions CSS – Comment utiliser l'animation de survol, changer
  l'opacité et plus
seo_desc: 'By Said Hayani

  If you are working with web technologies like CSS, HTML, and JavaScript, it''s important
  to have some basic knowledge about CSS animations and transitions.

  In this article we are going to learn how to make some basic transition animatio...'
---

Par Said Hayani

Si vous travaillez avec des technologies web comme CSS, HTML et JavaScript, il est important d'avoir quelques connaissances de base sur les animations et transitions CSS.

Dans cet article, nous allons apprendre comment créer quelques animations de transition de base en utilisant CSS.

%[https://codesandbox.io/s/background-transition-hcosp?file=/index.html:0-1294]

## Comment animer un élément avec une transition de base au survol

Dans cet exemple, nous allons faire en sorte que l'opacité d'un élément change lorsque l'utilisateur survole ou passe la souris sur l'élément.

```html
<!DOCTYPE html>
<html lang="fr">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title>Modèle Statique</title>
  </head>
  <style>
    .elem {
      background: blueviolet;
      width: 300px;
      height: 150px;
    }
    .elem:hover {
      opacity: 0.5;
    }
  </style>
  <body>
    <div class="elem"></div>
  </body>
</html>
```

![Image](https://www.freecodecamp.org/news/content/images/2020/10/hover.gif)

Il s'agit d'une transition simple qui peut être déclenchée lorsque nous survolons l'élément. Nous pouvons ajouter plus d'une transition qui s'exécutera en même temps.

Ajoutons une propriété de transformation d'échelle pour ajouter une transition d'échelle à l'élément.

```css
 .elem:hover {
      transform: scale(1.1);
    }
```

![Image](https://www.freecodecamp.org/news/content/images/2020/10/scale.gif)

Mais la transition ne semble pas fluide, car nous n'avons pas défini la durée de la transition ni utilisé de fonction de temporisation. 

Si nous ajoutons la propriété `transition`, cela rendra le mouvement de l'élément plus fluide.

```css
 .elem {
      background: blueviolet;
      width: 300px;
      height: 150px;
      margin: 20px auto;
      transition: 500ms linear; 
    }
```

![Image](https://www.freecodecamp.org/news/content/images/2020/10/transition.gif)

Décomposons comment fonctionne la propriété de transition :

```css
  transition: 500ms linear;
```

* `500ms` : la durée de la transition en millisecondes
* `linear` : la fonction de temporisation

```css
div {
    transition: <property> <duration> <timing-function> <delay>;
}
```

Nous pouvons ajouter plus d'options comme ci-dessous (exemples de [MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Transitions/Using_CSS_transitions)) :

```css
#delay {
  transition-property: font-size;
  transition-duration: 4s;
  transition-delay: 2s;
}
```

Alors, que fait ce code ?

* transition-property : la propriété que vous souhaitez animer. Cela peut être n'importe quel élément CSS comme `background`, `height`, `translateY`, `translateX`, et ainsi de suite. 
* transition-duration : la durée de la transition
* transition-delay : le délai avant que la transition ne commence

Vous pouvez en apprendre davantage sur les différentes utilisations de `transition` en CSS [ici](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Transitions/Using_CSS_transitions).

## Comment rendre les transitions plus interactives en utilisant la propriété d'animation et les keyframes

Nous pouvons faire plus avec les transitions CSS pour rendre cette animation plus créative et interactive.

### Comment déplacer un élément avec des Keyframes

Examinons un exemple où l'élément se déplace du point A au point B. Nous utiliserons translateX et translateY.

```html
<!DOCTYPE html>
<html lang="fr">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title>Modèle Statique</title>
  </head>
  <style>
    .elem {
      background: orange;
      width: 300px;
      height: 150px;
      animation: moveToRight 2s ease-in-out;
      animation-delay: 1000ms;
    }

    @keyframes moveToRight {
      0% {
        transform: translateX(0px);
      }
      100% {
        transform: translateX(300px);
      }
    }
  </style>
  <body>
    <div class="elem"></div>
  </body>
</html>
```

Et voici ce que nous obtenons :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/translatex.gif)

Cette fois, nous avons utilisé de nouvelles propriétés comme animation et keyframes. Nous avons utilisé la propriété `animation` pour définir le nom et la durée de l'animation, et les keyframes nous permettent de décrire comment l'élément doit se déplacer.

```css
  animation: moveToRight 2s ease-in-out;
```

Ici, j'ai nommé l'animation `moveToRight` – mais vous pouvez utiliser n'importe quel nom que vous souhaitez. La durée est de `2s`, et `ease-in-out` est une fonction de temporisation. 

Il existe d'autres fonctions de temporisation que vous pouvez utiliser comme `ease-in`, `linear`, `ease-out` qui rendent essentiellement l'animation plus fluide. Vous pouvez en apprendre davantage sur les [fonctions de temporisation ici](https://developer.mozilla.org/en-US/docs/Web/CSS/animation-timing-function). 

`@keyframes` prend le nom de l'animation. Dans ce cas, c'est `moveToRight`.

```css
 @keyframes moveToRight {
      0% {
        transform: translateX(0px);
      }
      100% {
        transform: translateX(300px);
      }
    }
```

`keyframes` exécutera l'animation en plusieurs étapes. L'exemple ci-dessus utilise un pourcentage pour représenter la plage ou l'ordre des transitions. Nous pourrions également utiliser les méthodes `from` et `to`, comme ci-dessous :

```css
 @keyframes moveToRight {
     from {
        transform: translateX(0px);
      }
     to {
        transform: translateX(300px);
      }
    }
```

`from` représente le point de départ ou la première étape de l'animation.

`to` est le point final ou la dernière étape de l'animation à exécuter.

Vous pouvez vouloir utiliser un pourcentage dans certains cas. Par exemple, disons que vous voulez ajouter plus de deux transitions qui seront exécutées en séquence, comme suit :

```css
 @keyframes moveToRight {
     0% {
        transform: translateX(0px);
      }
     50% {
        transform: translateX(150px);
      }
       100% {
        transform: translateX(300px);
      }
    }
```

Nous pouvons être plus créatifs et animer plusieurs propriétés en même temps comme dans l'exemple suivant :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/multiple-transitions.gif)

Vous pouvez jouer avec les propriétés et les techniques d'animation dans le bac à sable ici :

%[https://codesandbox.io/s/css-transition-examples-how-to-use-a-hover-animation-change-opacity-and-mor-forked-lcblf?fontsize=14&hidenavigation=1&theme=dark]

Il y a beaucoup plus de choses que nous pouvons faire avec les keyframes. D'abord, ajoutons plus de transitions à notre animation. 

### Comment animer plus de propriétés et les inclure dans la transition

Cette fois, nous allons animer l'arrière-plan, et nous allons faire bouger l'élément selon un motif carré. Nous allons faire en sorte que l'animation s'exécute indéfiniment en utilisant la propriété `infinite` comme fonction de temporisation.

%[https://codesandbox.io/s/background-transition-hcosp?file=/index.html]

```html
<!DOCTYPE html>
<html lang="fr">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title>Modèle Statique</title>
  </head>
  <style>
    .elem {
      background: orange;
      width: 250px;
      height: 250px;
      border-radius: 10px;
      animation: moveToLeft 5s linear infinite;
      animation-delay: 1000ms;
    }

    @keyframes moveToLeft {
      0% {
        transform: translateX(0px);
        background: linear-gradient(
          to right,
          #ff8177 0%,
          #ff867a 0%,
          #ff8c7f 21%,
          #f99185 52%,
          #cf556c 78%,
          #b12a5b 100%
        );
      }
      25% {
        transform: translateX(400px);
        background: linear-gradient(120deg, #84fab0 0%, #8fd3f4 100%);
      }
      50% {
        transform: translateY(200px) translateX(400px);
        background: linear-gradient(to top, #30cfd0 0%, #330867 100%);
      }

      75% {
        transform: translateX(0px) translateY(200px);
        background: linear-gradient(120deg, #f6d365 0%, #fda085 100%);
      }
      100% {
        transform: translateY(0px);
      }
    }
  </style>
  <body>
    <div class="elem"></div>
  </body>
</html>

```

Décomposons cela. D'abord, nous ajoutons `infinite` pour faire en sorte que l'animation s'exécute indéfiniment.

```css
animation: moveToLeft 5s linear infinite;
```

Ensuite, nous divisons l'animation en quatre étapes. À chaque étape, nous exécuterons une transition différente et toute l'animation s'exécutera en séquence.

* Première étape : définir l'élément horizontalement à `translateX(0px)`, et changer l'arrière-plan en dégradé. 

```css
 0% {
        transform: translateX(0px);
        background: linear-gradient(
          to right,
          #ff8177 0%,
          #ff867a 0%,
          #ff8c7f 21%,
          #f99185 52%,
          #cf556c 78%,
          #b12a5b 100%
        );
      }
```

* La deuxième animation déplacera l'élément de gauche à droite et changera la couleur de l'arrière-plan.

```css
 25% {
        transform: translateX(400px);
        background: linear-gradient(120deg, #84fab0 0%, #8fd3f4 100%);
      }
```

* La troisième animation déplacera l'élément vers le bas en utilisant `translateY` et changera à nouveau la couleur de l'arrière-plan.
* À la quatrième étape, l'élément se déplacera vers la gauche et changera la couleur de l'arrière-plan.
* Dans la cinquième animation, l'élément devrait revenir à sa place d'origine.

## Conclusion

Dans cet article, nous avons couvert diverses choses que vous pouvez faire avec les transitions CSS. Vous pouvez utiliser les transitions CSS de nombreuses manières dans vos applications pour créer une meilleure expérience utilisateur.

Après avoir appris les bases des animations CSS, vous pouvez aller plus loin et créer des choses plus complexes qui nécessitent une interaction utilisateur. Pour cela, vous pouvez utiliser JavaScript ou toute bibliothèque d'animation tierce disponible.

> Bonjour, je m'appelle Said Hayani, j'ai créé [subscribi.io](https://subscribi.io/) pour aider les créateurs, blogueurs et influenceurs à développer leur audience grâce à une newsletter.