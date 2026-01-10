---
title: Comment rendre votre application React entièrement fonctionnelle, entièrement
  réactive et capable de gérer toutes ces folies…
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-03-03T02:37:42.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-your-react-app-fully-functional-fully-reactive-and-able-to-handle-all-those-crazy-e5da8e7dac10
coverImage: https://cdn-media-1.freecodecamp.org/images/1*lD7IVk_sCcOcgVDOJPn7cA.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Redux
  slug: redux
- name: Web Development
  slug: web-development
seo_title: Comment rendre votre application React entièrement fonctionnelle, entièrement
  réactive et capable de gérer toutes ces folies…
seo_desc: 'By Luca Matteis

  Functional reactive programming (FRP) is a paradigm that has gained lots of attention
  lately, especially in the JavaScript front end world. It’s an overloaded term, but
  it describes a simple idea:


  Everything should be pure so it’s ea...'
---

Par Luca Matteis

La [programmation réactive fonctionnelle](https://gist.github.com/staltz/868e7e9bc2a7b8c1f754) (FRP) est un paradigme qui a attiré beaucoup d'attention ces derniers temps, surtout dans le monde du front-end JavaScript. C'est un terme surchargé, mais il décrit une idée simple :

> Tout devrait être pur pour faciliter les tests et le raisonnement **(fonctionnel)**, et le comportement asynchrone devrait être modélisé en utilisant des valeurs qui changent au fil du temps **(réactif)**.

React en soi n'est pas entièrement fonctionnel, ni entièrement réactif. Mais il est inspiré par certains des concepts derrière la FRP. Les [composants fonctionnels](https://facebook.github.io/react/docs/components-and-props.html), par exemple, sont des fonctions pures par rapport à leurs props. Et [ils sont réactifs aux changements de props ou d'état](https://facebook.github.io/react/docs/react-component.html#updating).

Mais lorsqu'il s'agit de **gérer les effets de bord**, React — n'étant que la couche de vue — a besoin de l'aide d'autres bibliothèques, comme [Redux](https://github.com/reactjs/redux).

Dans cet article, je vais parler de [redux-cycles](https://github.com/cyclejs-community/redux-cycles), un middleware Redux qui vous aide à gérer les effets de bord et le code asynchrone dans vos applications React de manière fonctionnelle et réactive — une caractéristique qui n'est pas encore partagée par d'autres modèles d'effets de bord de Redux — en tirant parti du framework [Cycle.js](https://cycle.js.org/).

![Image](https://cdn-media-1.freecodecamp.org/images/fj8i5IkTufxSwdZT8gq-magd5db5Gu2RvZ4J)
_Redux-cycles est à la fois déclaratif et réactif_

### Qu'est-ce que les effets de bord ?

Un effet de bord modifie le monde extérieur. Tout dans votre application qui traite des requêtes HTTP, de l'écriture dans le localStorage, ou même de la manipulation du DOM, est considéré comme un effet de bord.

Les effets de bord sont mauvais. Ils sont difficiles à tester, compliqués à maintenir, et généralement, c'est là que se trouvent la plupart de vos bugs. Votre objectif est donc de les minimiser/localiser.

![Image](https://cdn-media-1.freecodecamp.org/images/Zj6aHRQM3JtanL2sAAamQrdlItuvNkdkBeuU)
_Deux programmeurs après avoir localisé le code avec effets de bord ([source](https://www.pexels.com/photo/sunset-beach-people-sunrise-40815/" rel="noopener" target="_blank" title="))_

> « En présence d'effets de bord, le comportement d'un programme dépend de l'historique passé ; c'est-à-dire que l'ordre d'évaluation compte. Parce que la compréhension d'un programme avec effets nécessite de penser à tous les historiques possibles, les effets de bord rendent souvent un programme plus difficile à comprendre. » — [Norman Ramsey](http://stackoverflow.com/users/41661/norman-ramsey)

Voici plusieurs façons populaires de gérer les effets de bord dans Redux :

1. [redux-thunk](https://github.com/gaearon/redux-thunk) — place votre code d'effets de bord à l'intérieur des créateurs d'actions
2. [redux-saga](https://github.com/redux-saga/redux-saga) — rend votre logique d'effets de bord déclarative en utilisant des sagas
3. [redux-observable](https://github.com/redux-observable/redux-observable) — utilise la programmation réactive pour modéliser les effets de bord

Le problème est qu'aucun de ceux-ci n'est à la fois pur et réactif. Certains sont purs (redux-saga) tandis que d'autres sont réactifs (redux-observable), mais aucun d'entre eux ne partage tous les concepts que nous avons introduits précédemment sur la FRP.

[**Redux-cycles**](https://github.com/cyclejs-community/redux-cycles) **est à la fois pur et réactif.**

![Image](https://cdn-media-1.freecodecamp.org/images/OuWPUsE5lujAlWztmjGPEt0eYxSk6nxV6jZ8)
_Consultez [ces diapositives redux-cycles](http://nick.balestra.ch/talk/redux-cycles/" rel="noopener" target="_blank" title=") par [Nick Balestra](undefined)_

Nous allons d'abord expliquer plus en détail ces concepts fonctionnels et réactifs — et pourquoi vous devriez vous en soucier. Nous expliquerons ensuite comment redux-cycles fonctionne en détail.

### Gestion pure des effets de bord avec Cycle.js

Une requête HTTP est probablement l'effet de bord le plus courant. Voici un exemple de requête HTTP utilisant redux-thunk :

```
function fetchUser(user) {  return (dispatch, getState) =>     fetch(`https://api.github.com/users/${user}`)}
```

Cette fonction est impérative. Oui, elle retourne une promesse et vous pouvez la chaîner avec d'autres promesses, mais `fetch()` effectue un appel, à ce moment précis dans le temps. Elle n'est pas pure.

La même chose s'applique à redux-observable :

```
const fetchUserEpic = action$ =>  action$.ofType(FETCH_USER)    .mergeMap(action =>      ajax.getJSON(`https://api.github.com/users/${action.payload}`)        .map(fetchUserFulfilled)    );
```

`ajax.getJSON()` rend ce morceau de code impératif.

**Pour rendre une requête HTTP pure, vous ne devriez pas penser à « faire une requête HTTP maintenant » mais plutôt à « laissez-moi décrire comment je veux que ma requête HTTP soit » et ne pas vous soucier de quand elle se produit réellement ou de qui la fait.**

Dans [Cycle.js](https://cycle.js.org/), c'est essentiellement ainsi que vous codez toutes les choses. Tout ce que vous faites avec le framework consiste à créer des descriptions de ce que vous voulez faire. Ces descriptions sont ensuite envoyées à ces choses appelées [**drivers**](https://cycle.js.org/drivers.html) (via des flux réactifs) qui s'occupent réellement de faire la requête HTTP :

```
function main(sources) {  const request$ = xs.of({    url: `https://api.github.com/users/foo`,  });
```

```
  return {    HTTP: request$  };}
```

Comme vous pouvez le voir dans ce morceau de code, il n'y a pas d'appel de fonction pour faire la requête. Si vous exécutez ce code, vous verrez la requête se produire de toute façon. Alors, que se passe-t-il réellement en coulisses ?

La magie opère grâce aux drivers. Cycle.js sait que lorsque votre fonction retourne un objet avec une clé `HTTP`, il doit gérer les messages qu'il reçoit de ce flux, et effectuer une requête HTTP en conséquence (via un driver HTTP).

![Image](https://cdn-media-1.freecodecamp.org/images/C03vg0OuHaE-VLJOVeQubHd2rLM5r87tbl-j)
_Les drivers vous permettent de gérer les effets de bord de manière pure._

**Le point clé est que vous n'avez pas supprimé l'effet de bord — la requête HTTP doit toujours se produire — mais vous l'avez localisé en dehors de votre code d'application.**

Vos fonctions sont beaucoup plus faciles à comprendre, et sont surtout beaucoup plus faciles à tester car vous pouvez simplement tester si vos fonctions émettent les bons messages — aucun mocking ou timing bizarre n'est nécessaire.

### Effets de bord réactifs

Dans les exemples précédents, nous avons abordé la réactivité. Il doit y avoir un moyen de communiquer avec ces soi-disant drivers sur « faire des choses dans le monde extérieur » et être notifié sur « les choses qui se passent dans le monde extérieur ».

Les [Observables](http://reactivex.io/documentation/observable.html) (alias flux) sont l'abstraction parfaite pour ce type de communication asynchrone.

![Image](https://cdn-media-1.freecodecamp.org/images/WK-ByWZHM6zkt4s393hWDvUPaWxJ9JeiYDGL)

Chaque fois que vous voulez « faire quelque chose », vous émettez dans un flux de sortie une description de ce que vous voulez faire. Ces flux de sortie sont appelés **sinks** dans le monde Cycle.js.

Chaque fois que vous voulez « être notifié de quelque chose qui s'est passé », vous utilisez un flux d'entrée (appelé **sources**) et vous mappez simplement les valeurs du flux pour apprendre ce qui s'est passé.

Cela forme une sorte de **boucle réactive** qui nécessite une pensée différente pour être comprise par rapport au code impératif normal. Modélisons un cycle de vie de requête/réponse HTTP en utilisant ce paradigme :

```
function main(sources) {  const response$ = sources.HTTP    .select('foo')    .flatten()    .map(response => response);
```

```
  const request$ = xs.of({    url: `https://api.github.com/users/foo`,    category: 'foo',  });
```

```
  const sinks = {    HTTP: request$  };  return sinks;}
```

Le driver HTTP connaît la clé `HTTP` retournée par cette fonction. C'est un flux contenant une description de requête HTTP pour une URL GitHub. Il dit au driver HTTP : « Je veux faire une requête à cette URL ».

Le driver sait alors effectuer la requête et envoie la réponse à la fonction principale en tant que source (`sources.HTTP`) — notez que les sinks et les sources utilisent la même clé d'objet.

Expliquons cela à nouveau : **nous utilisons `sources.HTTP` pour « être notifié des réponses HTTP ». Et nous retournons `sinks.HTTP` pour « faire des requêtes HTTP ».**

Pour expliquer cette importante boucle réactive, voici une animation :

![Image](https://cdn-media-1.freecodecamp.org/images/GIMGooQplyIFHG1Gs9tebdE5ARBzzBPWltdk)
_Boucle réactive entre votre application et le monde extérieur_

Cela semble contre-intuitif par rapport à la programmation impérative normale : pourquoi le code de lecture de la réponse existerait-il avant le code responsable de la requête ?

C'est parce que cela n'a pas d'importance où se trouve le code en FRP. Tout ce que vous avez à faire est d'envoyer des descriptions et d'écouter les changements. L'ordre du code n'est pas important.

Cela permet un refactoring de code très facile.

### Présentation de redux-cycles

![Image](https://cdn-media-1.freecodecamp.org/images/BHgH4dpB3ZZ65wmu9PifY0c5WZWwtRFfvOZd)
_Redux-cycles est une combinaison de Redux et Cycle.js_

À ce stade, vous vous demandez peut-être, quel est le rapport avec mon application React ?

Vous avez appris les avantages de rendre votre code pur, en écrivant uniquement des descriptions de ce que vous voulez faire. Et vous avez appris les avantages de l'utilisation des Observables pour communiquer avec le monde extérieur.

Vous allez maintenant voir comment utiliser ces concepts dans vos applications React existantes pour, en fait, devenir entièrement fonctionnel et réactif.

#### Interception et dispatch d'actions Redux

Avec Redux, vous dispatch des actions pour dire à vos reducers que vous voulez un nouvel état.

Ce flux est synchrone, ce qui signifie que si vous voulez introduire un comportement asynchrone (pour les effets de bord), vous devez utiliser une forme de middleware qui intercepte les actions, fait l'effet de bord asynchrone et émet d'autres actions en conséquence.

C'est exactement ce que fait [redux-cycles](https://github.com/cyclejs-community/redux-cycles). C'est un middleware qui intercepte les actions Redux, entre dans la boucle réactive de Cycle.js et vous permet d'effectuer d'autres effets de bord en utilisant d'autres drivers. Il dispatch ensuite de nouvelles actions basées sur le flux de données asynchrone décrit dans vos fonctions :

```
function main(sources) {  const request$ = sources.ACTION    .filter(action => action.type === FETCH_USER)    .map(action => ({      url: `https://api.github.com/users/${action.payload}`,      category: 'users',    }));  const action$ = sources.HTTP    .select('users')    .flatten()    .map(fetchUserFulfilled);  const sinks = {    ACTION: action$,    HTTP: request$  };  return sinks;}
```

Dans l'exemple ci-dessus, il y a une nouvelle source et un nouveau sink introduits par redux-cycles — `**ACTION**`. Mais le paradigme de communication est le même.

Il écoute les actions dispatchées depuis le monde Redux en utilisant `sources.ACTION`. Et il dispatch de nouvelles actions vers le monde Redux en retournant `sinks.ACTION`.

Plus précisément, il émet des objets [Flux Standard Actions](https://github.com/acdlite/flux-standard-action).

Le truc cool est que vous pouvez combiner des choses qui se passent depuis d'autres drivers. Dans l'exemple précédent, **les choses qui se passent dans le monde `HTTP` déclenchent effectivement des changements dans le monde `ACTION`, et vice-versa**.

— Notez que la communication avec Redux se fait entièrement via la source/sink `ACTION`. Les drivers de Redux-cycles gèrent le dispatch réel pour vous.

![Image](https://cdn-media-1.freecodecamp.org/images/VIFiCfzZ9aKTIiHF3wLQX0qsUoIsQRryg14B)
_Comment différents drivers interagissent les uns avec les autres_

### Et les applications plus complexes ?

Comment développe-t-on des applications plus complexes si vous n'écrivez que des fonctions pures qui transforment des flux de données ?

Il s'avère que vous pouvez faire presque tout en utilisant des [drivers déjà construits](https://github.com/cyclejs-community/awesome-cyclejs#drivers). Ou vous pouvez facilement construire les vôtres — voici un driver simple qui journalise les messages écrits dans son sink.

```
run(main, {  LOG: msg$ => msg$.addListener({    next: msg => console.log(msg)  })});
```

`run` fait partie de Cycle.js, qui exécute votre fonction principale (premier argument) et transmet tous les drivers (deuxième argument).

Redux-cycles introduit deux drivers qui vous permettent de communiquer avec Redux ; `makeActionDriver()` & `makeStateDriver()` :

```
import { createCycleMiddleware } from 'redux-cycles';
```

```
const cycleMiddleware = createCycleMiddleware();const { makeActionDriver, makeStateDriver } = cycleMiddleware;
```

```
const store = createStore(  rootReducer,  applyMiddleware(cycleMiddleware));
```

```
run(main, {  ACTION: makeActionDriver(),  STATE: makeStateDriver()})
```

`makeStateDriver()` est un driver en lecture seule. Cela signifie que vous ne pouvez que lire `sources.STATE` dans votre fonction principale. Vous ne pouvez pas lui dire quoi faire ; vous ne pouvez que lire des données depuis celui-ci.

Chaque fois que l'état Redux change, le flux `sources.STATE` émettra le nouvel objet d'état. Cela est utile [lorsque vous devez écrire une logique spécifique](https://github.com/cyclejs-community/redux-cycles#drivers) basée sur l'état actuel de l'application.

![Image](https://cdn-media-1.freecodecamp.org/images/hOrxSvYMg9j4jR0UBfOw-NKixaSWPrhBgxK8)
_Redux et Cycle.js sont maintenus séparés. Ils ne communiquent que via les drivers de redux-cycles._

### Flux de données asynchrone complexe

![Image](https://cdn-media-1.freecodecamp.org/images/JwO1PcpN9h1lSndKsl4BRwF68hGplNnoFCxI)
_Les Observables viennent avec des opérateurs, vous permettant de construire des flux asynchrones complexes_

Un autre grand avantage de la programmation réactive est la capacité d'utiliser des opérateurs pour composer des flux en d'autres flux — traitant effectivement ceux-ci comme des tableaux de valeurs au fil du temps : vous pouvez les `[map](https://github.com/Reactive-Extensions/RxJS/blob/master/doc/gettingstarted/categories.md)`, `[filter](https://github.com/Reactive-Extensions/RxJS/blob/master/doc/gettingstarted/categories.md)` et même les `[reduce](https://github.com/Reactive-Extensions/RxJS/blob/master/doc/gettingstarted/categories.md)`.

Les opérateurs rendent possibles les graphes de flux de données explicites ; c'est-à-dire, le raisonnement des dépendances entre les opérations. Vous permettant de visualiser les données circulant à travers divers opérateurs comme dans l'animation ci-dessus.

Redux-observable vous permet également d'écrire des flux asynchrones complexes — ils utilisent un exemple de WebSocket multiplexé comme argument de vente — cependant, la puissance d'écrire ces flux de manière **pure** est ce qui distingue vraiment Cycle.js.

> Puisque tout est un flux de données pur, nous pouvons imaginer un futur où la programmation ne sera rien d'autre que l'assemblage de blocs d'opérateurs.

### Test avec des diagrammes de marbres

![Image](https://cdn-media-1.freecodecamp.org/images/IaglTAagb8kAi6lFgD0RW-fAslMuqewkPYYQ)
_Un diagramme de marbres. Chaque flèche représente un flux. Chaque cercle est une valeur émise sur ce flux._

Enfin, mais non des moindres, vient le test. C'est là que redux-cycles (et généralement toutes les applications Cycle.js) brillent vraiment.

Parce que tout est pur dans votre code d'application, pour tester votre fonction principale, vous lui donnez simplement des flux en entrée et attendez des flux spécifiques en sortie.

En utilisant le merveilleux projet [@cycle/time](https://github.com/cyclejs/time), vous pouvez même dessiner des [diagrammes de marbres](http://rxmarbles.com/) et tester vos fonctions de manière très visuelle :

```
assertSourcesSinks({  ACTION: { '-a-b-c----|': actionSource },  HTTP:   { '---r------|': httpSource },}, {  HTTP:   { '---------r|': httpSink },  ACTION: { '---a------|': actionSink },}, searchUsers, done);
```

[Ce morceau de code](https://github.com/cyclejs-community/redux-cycles/blob/master/example/cycle/test/test.js) exécute la fonction `[searchUsers](https://github.com/cyclejs-community/redux-cycles/blob/master/example/cycle/index.js#L31)`, lui passant des sources spécifiques en entrée (premier argument). Étant donné ces sources, il s'attend à ce que la fonction retourne les sinks fournis (deuxième argument). Si ce n'est pas le cas, l'assertion échoue.

Définir des flux graphiquement de cette manière est particulièrement utile lorsque vous devez tester un comportement asynchrone.

Lorsque la source `HTTP` émet `r` (réponse), vous vous attendez immédiatement à ce que `a` (action) apparaisse dans le sink `ACTION` — ils se produisent au même moment. Cependant, lorsque la source `ACTION` émet une rafale de `-a-b-c`, vous ne vous attendez pas à ce que quelque chose apparaisse à ce moment-là dans le sink `HTTP`.

C'est parce que `searchUsers` est censé débouncer les actions qu'il reçoit. Il n'enverra une requête HTTP qu'après 800 millisecondes d'inactivité sur le flux de source ACTION : il implémente une fonctionnalité de complétion automatique.

Tester ce type de comportement asynchrone est trivial avec des fonctions pures et réactives.

### Conclusion

Dans cet article, nous avons expliqué la véritable puissance de la FRP. Nous avons présenté Cycle.js et ses nouveaux paradigmes. La [liste awesome de Cycle.js](https://github.com/cyclejs-community/awesome-cyclejs) est une ressource importante si vous souhaitez en apprendre davantage sur cette technologie.

Utiliser Cycle.js seul — sans React ou Redux — nécessite un certain changement de mentalité, mais peut être fait si vous êtes prêt à abandonner certaines des technologies et ressources de la communauté React/Redux.

Redux-cycles, en revanche, vous permet de continuer à utiliser toutes les excellentes fonctionnalités de React tout en vous familiarisant avec la FRP et Cycle.js.

Un remerciement spécial à [Gosha Arinich](https://www.freecodecamp.org/news/how-to-make-your-react-app-fully-functional-fully-reactive-and-able-to-handle-all-those-crazy-e5da8e7dac10/undefined) et [Nick Balestra](https://www.freecodecamp.org/news/how-to-make-your-react-app-fully-functional-fully-reactive-and-able-to-handle-all-those-crazy-e5da8e7dac10/undefined) pour avoir maintenu le projet avec moi, et à [Nick Johnstone](https://twitter.com/widdnz) pour la relecture de cet article.