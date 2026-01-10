---
title: 'De Reduce à Redux : Comprendre Redux en construisant Redux'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-15T19:43:45.000Z'
originalURL: https://freecodecamp.org/news/from-reduce-to-redux-understanding-redux-by-building-redux-918ef08abafe
coverImage: https://cdn-media-1.freecodecamp.org/images/1*3-d_IpVFeG6uozLxANq2sg.png
tags:
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Redux
  slug: redux
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: 'De Reduce à Redux : Comprendre Redux en construisant Redux'
seo_desc: 'By Johnny Snelgrove

  The two most important techniques I’ve discovered to help with understanding a concept
  quickly are simplification and learning by doing. Redux is an extremely popular
  JavaScript library for developing “predictable state containers...'
---

Par Johnny Snelgrove

Les deux techniques les plus importantes que j'ai découvertes pour aider à comprendre un concept rapidement sont la _simplification_ et l'_apprentissage par la pratique_. [Redux](https://redux.js.org/) est une bibliothèque JavaScript extrêmement populaire pour développer des "conteneurs d'état prévisibles pour les applications JavaScript". Elle adopte une approche fonctionnelle pour modéliser les données, ce qui défie le modèle MVC traditionnel.

De nombreux développeurs, y compris moi-même, ont trouvé ce changement de paradigme difficile. Cependant, comprendre cette approche est incroyablement gratifiant et précieux. Les concepts transcendent les langages et les frameworks, et professionnellement, de nombreuses interfaces modernes adoptent Redux et ses paradigmes fonctionnels associés pour gérer leur couche de données côté client.

Dans cet article, nous allons construire une bibliothèque Redux simplifiée à partir de zéro afin de _vraiment_ comprendre Redux. En commençant par une simple fonction de somme, nous allons progressivement construire un système de gestion d'état de style Redux pour un agent de jeu simple.

#### Qu'est-ce que Reduce ?

La clé pour comprendre Redux réside dans la compréhension de la puissance de la fonction _reduce_. D'après la [documentation Mozilla](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce) :

> « La méthode reduce() applique une fonction contre un accumulateur et chaque élément du tableau (de gauche à droite) pour le réduire à une seule valeur. »

Si cela ne vous semble pas clair, ne vous inquiétez pas. La puissance de _reduce_ vient de sa généralité, ce qui le rend également difficile à décrire. Pour se souvenir de ce que fait _reduce()_, il suffit de se rappeler que _reduce_ rime avec _deduce_. La fonction reduce déduit l'état suivant étant donné un état existant et une règle de transition. Elle fait cela pour chaque élément d'un tableau, de gauche à droite, en passant le résultat en série, puis en retournant le résultat final. Voici une implémentation possible de _reduce()_ :

```
function reduce (collection, transitionFn, initialState) {  let accumulator = initialState || collection[0]  for (let i = (initialState ? 0 : 1); i < collection.length; i++) {    accumulator = transitionFn(accumulator, collection[i])  }  return accumulator}
```

_Note de côté : la fonction de transition accepte en réalité quatre arguments : l'accumulateur, la valeur actuelle (c'est-à-dire collection[i]), l'index de la valeur actuelle, et la collection elle-même. Cependant, à des fins de démonstration, les arguments d'index et de collection sont omis ici car ils ne sont pas pertinents._

Heureusement pour nous, _reduce()_ est déjà une méthode de tableau intégrée en JavaScript, et utilise le tableau appelant comme la collection à réduire. Maintenant que nous avons une idée de ce qu'est la fonction reduce, il est temps d'approfondir et de commencer à explorer comment nous pouvons l'utiliser pour modéliser l'état d'un agent de jeu.

#### Utilisation de Reduce

Pour comprendre la puissance de _reduce_, nous allons commencer par la fonction réductrice canonique, _sum()_ :

```
function sum (nums) {  return nums.reduce((state, nextVal) => state + nextVal)}
```

```
sum([1, 2, 3, 4]) // => 10
```

Cet exemple ne m'a jamais donné ce moment « Aha ! ». Probablement parce qu'il obscurcit la signature de la fonction et n'est pas très excitant. Voici le même exemple avec tout explicité :

```
function sum (nums) {  function transition (prevState, nextVal) {    return prevState + nextVal  }  const [initialState, ...tail] = nums  return tail.reduce(transition, initialState)}
```

```
sum([1, 2, 3, 4]) // => 10
```

_note : `const [initialState, …tail] = nums` utilise la [destructuration ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment) pour diviser le tableau en le premier élément (initialState) et les éléments restants (tail)._

Ici, nous pouvons voir que la fonction reduce prend une fonction de transition comme premier argument, et un état initial comme deuxième argument. Par défaut, reduce utilise le premier élément du tableau comme état initial si aucun état initial n'est fourni.

#### Devenir Spécifique

Pour nous rapprocher conceptuellement de la modélisation de données plus intéressantes, nous pouvons réécrire _sum_ avec des noms de variables spécifiques au domaine :

```
function move (steps) {  return steps.reduce((state, direction) => state + direction)}
```

```
xPosition = -2xPosition = xPosition + move([-1, -1, 0, 1, 1, 1])console.log(xPosition) // => -1
```

C'est toujours la même fonction de somme, mais maintenant il est un peu plus clair comment elle pourrait être utilisée dans une application réelle. Notre personnage de jeu commence avec une position initiale de -2, que nous combinons ensuite avec une liste de directions pour déterminer la nouvelle position. Chaque valeur dans le tableau passé à la fonction _move_ peut être considérée comme une **action** qui indiquera au réducteur comment muter son état. Ici, nos actions n'ont pas de noms, mais en suivant quelques conventions simples, nous arrivons à la base de redux :

```
let store = 0 // position initiale
```

```
const reducer = (state, action) => {  switch (action.type) {    case 'MOVE_LEFT':      return state - action.distance    case 'MOVE_RIGHT':      return state + action.distance    case 'WAIT':    default:      return state  }}
```

```
console.log(store) // => 0
```

```
store = [  {type: 'MOVE_LEFT', distance: 2 },  {type: 'MOVE_LEFT', distance: 3 },  {type: 'MOVE_RIGHT', distance: 7 },  {type: 'WAIT'}].reduce(reducer, store)
```

```
console.log(store) // => 2
```

Si nous convenons que tous les éléments de notre tableau seront des objets avec un champ _type_, alors nous pouvons commencer à traiter explicitement les actions dans le réducteur. De plus, en passant le magasin existant comme état initial à _reduce()_ puis en l'écrasant avec le résultat, nous pouvons commencer à transformer les données à travers plusieurs appels à reduce.

Nous arrivons également à un concept similaire à celui d'une classe avec des variables d'instance et des méthodes. En POO, tout dans _store_ pourrait être une variable d'instance, et les types d'action seraient des méthodes :

```
class Mover {  constructor (x) {    this.x = x  }
```

```
  moveLeft (distance) {    this.x -= distance  }
```

```
  moveRight (distance) {    this.x += distance  }}
```

```
let agent = new Mover(0)agent.moveLeft(1)agent.moveLeft(1)agent.moveRight(1)
```

#### Données Complexes

À ce stade, notre personnage ne peut se déplacer que gauche et droite, et n'a pas d'autres propriétés intéressantes. Pour rendre les choses plus intéressantes, et pour étendre ce concept à des données multidimensionnelles, ajoutons la capacité de monter et descendre, et donnons au joueur un peu de santé :

```
let store = { x:0, y:0, health: 100 } // état initial
```

```
const reducer = (state, action) => {  switch (action.type) {    case 'MOVE_LEFT':      return { ...state, x: state.x - action.distance }    case 'MOVE_RIGHT':      return { ...state, x: state.x + action.distance }    case 'MOVE_UP':      return { ...state, y: state.y - action.distance }    case 'MOVE_DOWN':      return { ...state, y: state.y + action.distance }    case 'TAKE_DAMAGE':      return { ...state, health: state.health - action.damage }    case 'DRINK_POTION':      return { ...state, health: state.health + action.health }    case 'WAIT':    default:      return state  }}
```

```
console.log(store) // => { x:0, y:0, health: 100 }store = [  {type: 'MOVE_LEFT', distance: 2 },  {type: 'MOVE_LEFT', distance: 3 },  {type: 'MOVE_RIGHT', distance: 7 },  {type: 'WAIT'},  {type: 'MOVE_DOWN', distance: 7 },  {type: 'TAKE_DAMAGE', damage: 50 },  {type: 'DRINK_POTION', health: 25 },  {type: 'MOVE_UP', distance: 2 },].reduce(reducer, store)console.log(store) // => { x:2, y:5, health: 75 }
```

Ici, l'état est un objet avec la forme `{x: Float, y: Float, health: Float}`. Le réducteur doit retourner un nouvel objet avec la même forme. Pour retourner un nouvel objet, nous utilisons la destructuration d'objets ES6 (par exemple, `{...state}`) pour créer une copie de l'objet d'état passé, puis nous écrasons le champ que nous souhaitons mettre à jour dans une expression déclarative concise : `return {...oldState, key: newKeyVal}`. Maintenant, nous cuisinons avec du feu !

#### Généralisation et Encapsulation

Pour envelopper cette logique et rendre les magasins généraux et réutilisables, nous pouvons écrire une fonction _createStore_ pour encapsuler l'état et fournir une API cohérente pour lire l'état et envoyer des actions :

```
const createStore = (reducer, initialState) => {  let store = initialState || reducer(undefined, {type: 'INIT'})  return {    dispatch: (action) => {      store = [action].reduce(reducer, store)    },    getState: _ => store  }}
```

```
var moverReducer = (state = { x:0, y:0 }, action) => {  switch (action.type) {    case 'MOVE_LEFT':      return { ...state, x: state.x - action.distance }    case 'MOVE_RIGHT':      return { ...state, x: state.x + action.distance }    case 'MOVE_UP':      return { ...state, y: state.y - action.distance }    case 'MOVE_DOWN':      return { ...state, y: state.y + action.distance }    case 'WAIT':    default:      return state  }}
```

```
let agent = createStore(moverReducer)agent.dispatch({type:'MOVE_UP', distance: 1})agent.dispatch({type:'MOVE_LEFT', distance: 2})agent.dispatch({type:'MOVE_RIGHT', distance: 4})agent.dispatch({type:'MOVE_DOWN', distance: 2})agent.getState() // => { x:-2, y:0 }
```

Ici, nous pouvons soit passer à _createStore()_ un état initial (peut-être quelque chose que nous chargeons depuis localStorage), soit il s'initialisera en utilisant l'argument d'état par défaut du réducteur et une action factice. Notre état est encapsulé en utilisant une fermeture, et la seule façon de le lire et d'y écrire est par les méthodes retournées _getState()_ et _dispatch()_, respectivement.

À ce stade, nous avons atteint une version basique mais utile de l'API Redux ! Nous avons omis les améliorateurs de magasin et les abonnements, cependant, puisque ils sont principalement utilisés pour les effets secondaires et la mise à jour réactive d'une vue. Dans la section finale, nous utiliserons simplement une boucle de rendu et du code de haut niveau pour gérer ces cas et garder les choses simples.

#### Avantages et Inconvénients

Le premier avantage clair de l'approche du réducteur est que tout est facilement sérialisable. Nous pourrions facilement utiliser localStorage pour sauvegarder et charger l'état, sérialiser des séquences d'actions, envoyer des actions via WebSockets ou des requêtes HTTP, et ainsi de suite, tout cela sans construire de gestionnaires pour traduire les charges utiles JSON en appels de méthodes d'instance.

De plus, puisque les réducteurs doivent être des [fonctions pures](https://en.wikipedia.org/wiki/Pure_function), il n'y a aucune garantie que des effets secondaires inattendus ne se produiront pas dans d'autres parties de votre application via la mise à jour des données d'un modèle. Un magasin est purement concerné par la modélisation des données et la logique. Cela rend nos modèles de données extrêmement portables, car ils ne sont pas concernés par leur environnement d'exécution. Les mêmes réducteurs pourraient potentiellement être utilisés dans une application cli node.js, une application web, ou une application native via quelque chose comme React Native. Le portage de l'application devient une question d'écriture de code spécifique à la plateforme pour les effets secondaires et la vue.

Enfin, je trouve personnellement les réducteurs élégants. Le concept est plus proche d'une équation mathématique qui définit des valeurs dans un modèle à partir d'un script de contrôleur. Consultez la [formule Q-learning](https://en.wikipedia.org/wiki/Q-learning#Algorithm) comme exemple. Sa signature est une paire état/action ! Cela facilite la traduction d'une formule en code.

L'inconvénient est que redux n'a pas d'opinion forte sur la façon de [gérer les effets secondaires](https://github.com/reactjs/redux/issues/1528) (par exemple, le rendu dans le DOM, la journalisation dans la console, la sauvegarde dans localStorage, le démarrage d'une requête Ajax, etc.). Vous ne pouvez pas construire une application intéressante sans effets secondaires, donc cela peut être un peu frustrant.

La solution consiste généralement à placer ce code dans des méthodes de création d'actions, des middlewares, ou à le déplacer au niveau supérieur de votre application (ce qui n'est pas idéal). Cependant, il peut souvent être bénéfique d'écrire du code de modèle avec cette contrainte, car cela vous force à écrire du code facilement testable et à vous concentrer sur la logique de ce que vous modélisez.

D'autres inconvénients incluent beaucoup de code standard pour accomplir des tâches simples comme l'incrémentation d'un compteur, et la charge cognitive générale qu'il faut pour s'éloigner des concepts orientés objet. Cependant, ce sont ces éléments qui rendent nos modèles si portables et puissants !

#### Conclusion et Exploration

Pour conclure, nous pouvons ajouter une boucle de mise à jour pour envoyer des actions aléatoires et rendre l'état de l'agent (ici j'utilise React, mais nous pourrions utiliser n'importe quelle couche de vue que nous aimons). À chaque tick, l'agent se déplace dans une direction, attend, prend une potion ou subit des dégâts. Si la santé de l'agent est à zéro, il réinitialise.

Remarquez comment la logique commence à s'accumuler dans la boucle de mise à jour/rendering de haut niveau. De plus, nous avons dû dupliquer le code pour l'état initial du réducteur pour réinitialiser l'agent lorsque sa santé atteint zéro.

Nous aborderons ces problèmes et d'autres dans le prochain article, mais pour l'instant, il est suffisant de remarquer que la logique peut vivre dans au moins deux endroits : le réducteur ou l'action. Dans le prochain article, nous examinerons comment choisir où placer cette logique, et nous procéderons à une exploration plus approfondie, rendant notre simulation plus sophistiquée en utilisant la composition de fonctions, des réducteurs d'ordre supérieur, et des créateurs d'actions tout en développant un agent de jeu de plus en plus intelligent.