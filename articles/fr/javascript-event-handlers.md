---
title: Gestionnaires d'événements JavaScript – Comment gérer les événements en JS
subtitle: ''
author: Shruti Kapoor
co_authors: []
series: null
date: '2020-09-21T17:09:50.000Z'
originalURL: https://freecodecamp.org/news/javascript-event-handlers
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/samuel-pereira-uf2nnANWa8Q-unsplash.jpg
tags:
- name: events
  slug: events
- name: JavaScript
  slug: javascript
seo_title: Gestionnaires d'événements JavaScript – Comment gérer les événements en
  JS
seo_desc: "What are events?\nEvents are actions that happen when a user interacts\
  \ with the page - like clicking an element, typing in a field, or loading a page.\
  \ \nThe browser notifies the system that something has happened, and that it needs\
  \ to be handled. It ge..."
---

## Qu'est-ce que les événements ?
Les événements sont des actions qui se produisent lorsqu'un utilisateur interagit avec la page - comme cliquer sur un élément, taper dans un champ ou charger une page. 

Le navigateur notifie le système qu'il s'est passé quelque chose et qu'il doit être géré. Cela est géré en enregistrant une fonction, appelée `gestionnaire d'événements`, qui écoute un type particulier d'événement. 

## Que signifie "gérer un événement" ?
Pour le dire simplement, imaginez ceci - supposons que vous êtes intéressé à participer à des événements de rencontre sur le développement Web dans votre communauté locale. 

Pour ce faire, vous vous inscrivez à une rencontre locale appelée "Women Who Code" et vous abonnez aux notifications. Ainsi, chaque fois qu'une nouvelle rencontre est programmée, vous êtes alerté. C'est la gestion d'événements ! 

L'« événement » ici est une nouvelle rencontre JS. Lorsqu'une nouvelle rencontre est publiée, le site meetup.com détecte ce changement, « gérant » ainsi cet événement. Il vous notifie ensuite, prenant ainsi une « action » sur l'événement. 

Dans un navigateur, les événements sont gérés de manière similaire. Le navigateur détecte un changement et alerte une fonction (gestionnaire d'événements) qui écoute un événement particulier. Ces fonctions exécutent ensuite les actions souhaitées. 

Regardons un exemple de gestionnaire d'événement `click` :
 
```
<div class="buttons">
  <button>Press 1</button>
  <button>Press 2</button>
  <button>Press 3</button>
</div>
const buttonContainer = document.querySelector('.buttons');
console.log('buttonContainer', buttonContainer);

buttonContainer.addEventListener('click', event => {
  console.log(event.target.value)
})

```

## Quels sont les différents types d'événements ?
Un événement peut être déclenché à tout moment lorsqu'un utilisateur interagit avec la page. Ces événements peuvent être un utilisateur faisant défiler la page, cliquant sur un élément ou chargeant une page. 

Voici quelques événements courants - `onclick` `dblclick` `mousedown` `mouseup` `mousemove` `keydown` `keyup` `touchmove` `touchstart` `touchend` `onload` `onfocus` `onblur` `onerror` `onscroll` 

## Différentes phases des événements - capture, cible, bulle
Lorsque qu'un événement se déplace à travers le DOM - qu'il remonte ou redescende - on parle de propagation d'événement. L'événement se propage à travers l'arbre DOM. 

Les événements se produisent en deux phases : la phase de bulle et la phase de capture. 

Dans la phase de capture, également appelée phase de ruissellement, l'événement "ruisselle" vers l'élément qui a provoqué l'événement. 

Elle commence à partir de l'élément et du gestionnaire de niveau racine, puis se propage vers le bas jusqu'à l'élément. La phase de capture est terminée lorsque l'événement atteint la `cible`. 

Dans la phase de bulle, l'événement "remonte" vers l'arbre DOM. Il est d'abord capturé et géré par le gestionnaire le plus interne (celui qui est le plus proche de l'élément sur lequel l'événement s'est produit). Il remonte ensuite (ou se propage vers le haut) vers les niveaux supérieurs de l'arbre DOM, puis vers ses parents, et enfin vers sa racine. 

Voici un truc pour vous aider à vous en souvenir :
```
ruissellement vers le bas, remontée en bulle
```

Voici une infographie de [quirksmode](https://www.quirksmode.org/js/events_order.html) qui explique cela très bien : 
```
               / \
---------------| |-----------------
| element1     | |                |
|   -----------| |-----------     |
|   |element2  | |          |     |
|   -------------------------     |
|        ÉVÉNEMENT REMONTÉE       |
-----------------------------------

               | |
---------------| |-----------------
| element1     | |                |
|   -----------| |-----------     |
|   |element2  \ /          |     |
|   -------------------------     |
|        ÉVÉNEMENT CAPTURE        |
-----------------------------------

```

Une chose à noter est que, que vous enregistriez un gestionnaire d'événements dans l'une ou l'autre phase, les deux phases se produisent TOUJOURS. Tous les événements remontent par défaut. 

Vous pouvez enregistrer des gestionnaires d'événements pour l'une ou l'autre phase, remontée ou capture, en utilisant la fonction `addEventListener(type, listener, useCapture)`. Si `useCapture` est défini sur `false`, le gestionnaire d'événements est dans la phase de remontée. Sinon, il est dans la phase de capture. 

L'ordre des phases de l'événement dépend du navigateur.


Pour vérifier quel navigateur honore d'abord la capture, vous pouvez essayer le code suivant dans JSfiddle : 
```html
<div id="child-one">
    <h1>
      Enfant Un
    </h1>
  </div>

```

```javascript
const childOne = document.getElementById("child-one");

const childOneHandler = () => {
console.log('Capturé sur enfant un')
}

const childOneHandlerCatch = () => {
console.log('Capturé sur enfant un en phase de capture')
}

childOne.addEventListener("click", childOneHandler); 
childOne.addEventListener("click", childOneHandlerCatch, true); 
```

Dans Firefox, Safari et Chrome, la sortie est la suivante :
![Les événements en phase de capture sont déclenchés en premier](https://github.com/shrutikapoor08/blogs/blob/master/JSByte/img/events_capture_order.png?raw=true) 
 
 
## Comment écouter un événement
Il existe deux façons d'écouter un événement : 
1.  `addEventListener` 
2.  événements en ligne, tels que `onclick`

 ```
//addEventListener
document.getElementByTag('a').addEventListener('click', onClickHandler);

//en ligne en utilisant onclick
<a href="#" onclick="onClickHandler">Cliquez ici</a>
```

## Lequel est le meilleur - un événement en ligne ou `addEventListener` ?

1. `addEventListener` vous donne la possibilité d'enregistrer un nombre illimité de gestionnaires d'événements.
2. `removeEventListener` peut également être utilisé pour supprimer des gestionnaires d'événements
3. Le drapeau `useCapture` peut être utilisé pour indiquer si un événement doit être géré dans la phase de capture ou de remontée.

 
## Exemples de code et action en direct

Vous pouvez essayer ces événements dans JSFiddle pour jouer avec eux. 

```html
<div id="wrapper-div">
  <div id="child-one">
    <h1>
      Enfant Un
    </h1>
  </div>
  <div id="child-two" onclick="childTwoHandler">
    <h1>
      Enfant Deux
    </h1>
  </div>

</div>

```

```javascript
const wrapperDiv = document.getElementById("wrapper-div");
const childOne = document.getElementById("child-one");
const childTwo = document.getElementById("child-two");

const childOneHandler = () => {
console.log('Capturé sur enfant un')
}

const childTwoHandler = () => {
console.log('Capturé sur enfant deux')
}

const wrapperDivHandler = () => {
console.log('Capturé sur div wrapper')
}

const childOneHandlerCatch = () => {
console.log('Capturé sur enfant un en phase de capture')
}

const childTwoHandlerCatch = () => {
console.log('Capturé sur enfant deux en phase de capture')
}

const wrapperDivHandlerCatch = () => {
console.log('Capturé sur div wrapper en phase de capture')
}


childOne.addEventListener("click", childOneHandler); 
childTwo.addEventListener("click", childTwoHandler); 
wrapperDiv.addEventListener("click", wrapperDivHandler); 

childOne.addEventListener("click", childOneHandlerCatch, true); 
childTwo.addEventListener("click", childTwoHandlerCatch, true); 
wrapperDiv.addEventListener("click", wrapperDivHandlerCatch, true); 
```


## TL;DR
Les phases des événements sont la capture (DOM -> cible), la bulle (cible -> DOM) et la cible. 
Les événements peuvent être écoutés en utilisant `addEventListener` ou des méthodes en ligne telles que `onclick`. 

```
    addEventListener peut ajouter plusieurs événements, alors qu'avec onclick cela ne peut pas être fait.
    onclick peut être ajouté en tant qu'attribut HTML, alors qu'un addEventListener ne peut être ajouté qu'à l'intérieur des éléments <script>.
    addEventListener peut prendre un troisième argument qui peut arrêter la propagation de l'événement.

```

## Lectures complémentaires 
https://www.quirksmode.org/js/events_order.html
https://jsfiddle.net/r2bc6axg/
https://stackoverflow.com/questions/6348494/addeventlistener-vs-onclick
https://www.w3.org/wiki/HTML/Attributes/_Global#Event-handler_Attributes


Pour rester informé de plus de tutoriels courts comme celui-ci, [inscrivez-vous à ma newsletter](https://tinyletter.com/shrutikapoor) ou [suivez-moi sur Twitter](https://twitter.com/shrutikapoor08)