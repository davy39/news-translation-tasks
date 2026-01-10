---
title: Comment ajouter des animations au défilement à une page avec l'API Intersection
  Observer de JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-03-24T17:42:18.000Z'
originalURL: https://freecodecamp.org/news/scroll-animations-with-javascript-intersection-observer-api
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/observer-api.png
tags:
- name: animation
  slug: animation
- name: api
  slug: api
- name: JavaScript
  slug: javascript
seo_title: Comment ajouter des animations au défilement à une page avec l'API Intersection
  Observer de JavaScript
seo_desc: "By Mwendwa Bundi Emma\nSometimes, when you visit a website, you'll notice\
  \ that certain elements or a particular section gets revealed dynamically as you\
  \ scroll. \nIt's like the contents of that particular section weren't available\
  \ to view until you scr..."
---

Par Mwendwa Bundi Emma

Parfois, lorsque vous visitez un site web, vous remarquerez que certains éléments ou une section particulière se révèlent de manière dynamique au fur et à mesure que vous faites défiler la page.

C'est comme si le contenu de cette section particulière n'était pas disponible avant que vous n'arriviez dessus – mais maintenant, parce que vous y êtes, le site décide de révéler ces contenus.

Parfois, cela peut se produire en quelques millisecondes, et d'autres fois, le chargement peut être différé (lazy loading). Tous ces phénomènes sont rendus possibles par l'API Intersection Observer de JavaScript.

## Qu'est-ce que l'API Intersection Observer ?

L'API Intersection Observer est une API de navigateur qui surveille les changements d'intersection d'un élément avec le viewport (la zone d'affichage) et exécute ensuite une fonction de rappel (callback) dans le code.

Elle fonctionne en vous permettant de définir une fonction d'observation qui s'exécute lorsque l'élément cible croise un autre élément ou le viewport par défaut du navigateur.

> L'API Intersection Observer permet au code d'enregistrer une fonction de rappel qui est exécutée chaque fois qu'un élément qu'on souhaite surveiller entre ou sort d'un autre élément, ou lorsque la quantité d'intersection entre les deux change d'une valeur demandée. - [MDN web docs](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API).

### Prérequis :

* Connaissances de base en HTML, CSS et JavaScript. Vous avez probablement déjà construit un projet simple avec ces outils.
* Un IDE, de préférence VS Code.
* Un navigateur, comme Chrome.

Dans cet article, vous apprendrez à construire une page web simple avec HTML, CSS et JavaScript. Ensuite, vous utiliserez l'API Intersection Observer pour implémenter une animation simple au défilement.

## Comment fonctionne l'API Intersection Observer

Vous vous demandez peut-être ce qui se passe lorsque vous définissez une fonction de rappel pour l'observateur ? Ce qui se passe, c'est que vous passez un paramètre `entries` en argument qui exécute ensuite la commande d'intersection une fois que l'utilisateur fait défiler la page jusqu'à l'élément cible.

Par exemple :

```js
const observer = new IntersectionObserver(entries => {
    // votre ensemble de conditions se place ici
})
```

Une fois que vous avez défini votre fonction d'observation, vous pouvez établir les conditions que vous souhaitez voir remplies une fois que l'intersection se produit.

Pour effectuer ces changements, l'API propose différentes options que vous pouvez passer à votre fonction de rappel. Ces options sont les seconds paramètres que vous pouvez passer en arguments. Il s'agit de :

### Seuil (Threshold)

L'option de seuil varie de 0 à 1. Vous pouvez spécifier le seuil pour signifier le pourcentage requis de l'élément cible qui doit être visible pour que `isIntersecting` soit `true`. Rappelez-vous que la valeur par défaut est 0, de sorte que dès que l'élément cible est légèrement visible, votre fonction de rappel s'exécute comme prévu.

### Marge racine (Root Margin)

La marge racine est assez importante car vous pouvez l'ajouter au viewport du conteneur et ainsi définir chaque côté du viewport. Elle vous permet également de définir votre propre zone imbriquée pour l'API. La façon dont vous définissez les marges en CSS personnalisé est exactement la même que pour la marge racine dans l'API Intersection Observer.

### Racine (Root)

Lors de la définition de la racine, gardez à l'esprit qu'elle doit être un ancêtre de l'élément cible. Selon votre projet, vous devrez peut-être ou non définir la racine, car elle utilise toujours par défaut le viewport du navigateur lorsqu'elle n'est pas définie.

Maintenant que vous connaissez les bases du fonctionnement de l'API Intersection Observer, il est temps de la voir en action.

## Comment construire une page avec HTML et CSS

Ici, vous allez construire une page statique de base avec HTML et CSS. Cette page fonctionne très bien telle quelle, mais il n'y a pas d'animations au défilement pour le moment.

Nous utiliserons cette page pour démontrer les changements qui se produisent une fois que nous ajoutons la partie JS de l'API Intersection Observer.

Vous allez également ajouter une classe `animation` qui sera appelée en JS en utilisant le DOM.

N'oubliez pas de lier également votre fichier de style à votre fichier JS.

### HTML

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <script src="app.js" defer></script>
    <title>Intersection observer</title>
</head>
<body>
    
    <section>
        <h1>
            C'est parti !
        </h1>

    </section>
    <section> 
        <h2 class="animation">Ce que je fais</h2>
        <p class="animation">Bienvenue sur ma page, je m'appelle Mwendwa Bundi. Je suis développeur front-end et rédacteur technique. Parlez-moi de vous !
        </p>
    
        </section>
        <section>
        <h1 class="animation">
            C'est reparti !
        </h1>

    </section>
    
</body>
</html>
```

### CSS

Nous allons maintenant ajouter un peu de style à la page ainsi qu'une section centrale définie dans le HTML. Cela aidera à montrer les animations de défilement lorsqu'elles apparaissent progressivement.

```css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    background-color: aqua;
    color: white;
}

section {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100vh;
}
```

Voici à quoi ressemble la page pour le moment :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Animation.gif)
_Page web de base avec HTML & CSS_

## Comment mettre à jour le CSS

Avant d'ajouter le JavaScript, vous devez mettre à jour votre CSS personnalisé avec l'animation que vous souhaitez voir. Actuellement, notre page de base est statique. Voici le code à ajouter à votre CSS :

```css
.animation {
    opacity: 0;
    transform: translateX(-300px);
    transition: all 0.7s ease-out;
    transition-delay: 0.4s;
}

.scroll-animation {
    opacity: 1;
    transform: translateX(0);
}
```

L'opacité avant le défilement est réglée sur `0` pour qu'une fois que l'utilisateur fait défiler la page jusqu'à l'élément cible, les éléments puissent apparaître. C'est pourquoi l'opacité passe à `1` comme indiqué ci-dessus.

## Comment ajouter la fonctionnalité JavaScript

L'idée est qu'une fois que la balise `p` avec la classe `animation` est visible, la fonction de rappel s'exécutera avec succès.

Allez-y et utilisez le DOM pour sélectionner la classe d'animation de la page HTML.

```js
const the_animation = document.querySelectorAll('.animation')
```

Maintenant, il est temps de créer une fonction d'observation :

```js
const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        if (entry.isIntersecting) {
            entry.target.classList.add('scroll-animation')
        }
            else {
                entry.target.classList.remove('scroll-animation')
            }
        
    })
},
```

Ici, vous avez utilisé les instructions conditionnelles `if/else` pour spécifier ce qui doit se passer si `isIntersecting` est `true` et ensuite.

Pour chaque entrée, si le paramètre entry est en intersection, vous utilisez le DOM pour sélectionner la propriété d'animation que vous avez définie dans votre CSS personnalisé – sinon, elle est supprimée. Cela signifie que peu importe le nombre de fois que l'utilisateur fait défiler la page d'avant en arrière, l'animation se produira toujours. En d'autres termes, la fonction de rappel s'exécutera toujours.

Pour vous assurer que la fonction de rappel ne s'exécute pas immédiatement lorsque l'élément cible est en vue, définissez un seuil (threshold) de `0.5` à l'intérieur de la fonction.

```js
{ threshold: 0.5
   });
```

Pour mettre votre observateur en mouvement, définissez une boucle `for`. Cette boucle itérera à travers toutes les classes nommées animation et observera les conditions dans votre API Intersection Observer.

```js
  for (let i = 0; i < the_animation.length; i++) {
   const elements = the_animation[i];

    observer.observe(elements);
  } 
```

Voici à quoi ressemble la page maintenant :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Animation2.gif)

### Code JavaScript complet

```js
const the_animation = document.querySelectorAll('.animation')

const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        if (entry.isIntersecting) {
            entry.target.classList.add('scroll-animation')
        }
            else {
                entry.target.classList.remove('scroll-animation')
            }
        
    })
},
   { threshold: 0.5
   });

// Boucle pour observer chaque élément
  for (let i = 0; i < the_animation.length; i++) {
   const elements = the_animation[i];

    observer.observe(elements);
  } 
```

## Conclusion

Dans cet article, vous avez découvert l'une des API de JavaScript basées sur l'observation, l'API Intersection Observer. Vous avez également construit avec succès une page web simple pour présenter des animations au défilement avec cette API.