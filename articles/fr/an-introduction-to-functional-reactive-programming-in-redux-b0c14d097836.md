---
title: Une introduction à la programmation réactive fonctionnelle dans Redux
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-28T18:40:59.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-functional-reactive-programming-in-redux-b0c14d097836
coverImage: https://cdn-media-1.freecodecamp.org/images/1*8qnkQscHUXopU2ZBwNhHrg.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: Redux
  slug: redux
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Une introduction à la programmation réactive fonctionnelle dans Redux
seo_desc: "By Bhuvan Malik\nLetss start off by getting the basic idea of what “Reactive\
  \ Programming” is:\n\nReactive Programming _is an asynchronous programming paradigm\
  \ concerned with data streams and the propagation of change.  \n- Wikipedia_\n\n\
  ReactiveX or Rx is ..."
---

Par Bhuvan Malik

Commençons par comprendre l'idée de base de ce qu'est la "Programmation Réactive" :

> **_Programmation Réactive_** _est un paradigme de programmation asynchrone concerné par les flux de données et la propagation du changement._  
> _- Wikipédia_

[ReactiveX](http://reactivex.io/) ou Rx est l'API la plus populaire pour la programmation réactive. Elle est basée sur les idéologies du motif Observable, du motif Itérateur et de la programmation fonctionnelle. Rx dispose de bibliothèques pour différents langages, mais nous utiliserons [RxJS](https://github.com/ReactiveX/rxjs).

#### Rx est basé sur les **Observables**, **Observers** et **Opérateurs**

Un Observer s'**abonne** essentiellement à un Observable.

L'Observable émet ensuite des flux de données que l'Observer écoute et auxquels il réagit, déclenchant une chaîne d'opérations sur le flux de données. La vraie puissance vient des Opérateurs ou "Reactive Extensions" (d'où le terme Rx).

Les Opérateurs vous permettent de transformer, combiner, manipuler et travailler avec les séquences d'éléments émis par les Observables.

Si vous n'êtes pas familier avec Rx, vous pourriez avoir du mal à comprendre et utiliser [Redux-Observable](https://redux-observable.js.org/). Je vous suggère donc de vous familiariser d'abord avec Rx !

Passons maintenant à l'utilisation de RxJS avec Redux.

### Redux-Observable

![Image](https://cdn-media-1.freecodecamp.org/images/6oEOGaUYU93i90xMzNA6GjY1lVaohtAjHKkR)

#### Redux-Observable est un middleware basé sur RxJS pour Redux

Voici ce que la documentation Redux dit à propos du middleware dans Redux :

> _Le middleware fournit un point d'extension tiers entre l'envoi d'une action et le moment où elle atteint le réducteur._

Le middleware Redux peut être utilisé pour le journalisation, les rapports de plantage, la communication avec une API asynchrone, le routage, et plus encore. Ou nous pouvons dire **effets secondaires** en général.

#### Comment Redux-Observable fait-il tout cela ?

Grâce aux [Epics](https://redux-observable.js.org/docs/basics/Epics.html). Les Epics sont le primitif central de Redux-Observable. Un epic est simplement une fonction qui prend une action et retourne une autre action. **Action Entrante → Action Sortante**. Les actions sont donc traitées comme des flux.

Chaque action envoyée dans n'importe quel composant de React passera par de telles fonctions (Epics) comme un flux.

Voyons à quoi ressemble un simple Epic qui prend une `action` `'PING'` et retourne une **nouvelle** `action` `'PONG'` :

```
const pingEpic = action$ =>  action$.filter(action => action.type === 'PING')    .mapTo({ type: 'PONG' })
```

Le `$` après `action` est utilisé pour indiquer que ces variables référencent des flux. Nous avons donc un flux d'actions passant dans l'Epic sur lequel nous avons utilisé l'opérateur `filter` de RxJS.

Cet opérateur de filtre élimine toutes les actions qui ne sont pas de type `PING` ! Par conséquent, l'Epic `pingEpic` ne s'occupe que des actions de type `'PING'`. Enfin, cette `action` `'PING'` est mappée à une nouvelle `action` de type `'PONG'`, satisfaisant la règle principale des Epics : **Action Entrante → Action Sortante**.

Puisque chaque epic ne s'occupe que d'un type spécifique d'action, nous avons un opérateur spécial pour `action$` (flux) afin de filtrer les actions indésirables du flux. Cet opérateur est l'opérateur `ofType()`.

En réécrivant l'Epic précédent en utilisant `ofType`, nous obtenons :

```
const pingEpic = action$ =>  action$.ofType('PING')  .mapTo({ type: 'PONG' })
```

Si vous souhaitez que votre epic permette plus d'un type d'action, l'opérateur `ofType()` peut prendre n'importe quel nombre d'arguments comme ceci : `ofType(type1, type2, type3,...)`.

#### Entrer dans les détails de fonctionnement des Epics

Vous pourriez penser que l'action 'PING' arrive simplement et est consommée par cet epic. Ce n'est pas le cas. Il y a deux choses à toujours retenir :

1. Chaque action va toujours d'abord au réducteur
2. Ce n'est qu'après cela que l'action est reçue par l'epic

Par conséquent, le cycle Redux fonctionne normalement comme il se doit.

L'`action` `'PING'` atteint d'abord le réducteur et est ensuite reçue par l'Epic, puis transformée en une nouvelle `action` `'PONG'` qui est envoyée au réducteur.

Nous pouvons même accéder à l'état du magasin à l'intérieur d'un Epic car le deuxième argument d'un Epic est une version légère du magasin Redux ! Voir ci-dessous :  
`const myEpic = (action$, store) =>`   
Nous pouvons simplement appeler `store.getState()` et accéder à l'état à l'intérieur des Epics.

#### Chaînage des opérateurs

Entre la réception d'une action et l'envoi d'une nouvelle, nous pouvons effectuer toutes sortes d'effets secondaires asynchrones que nous voulons, tels que des appels AJAX, des websockets, des temporisateurs, et ainsi de suite. Cela est fait en utilisant les nombreux **opérateurs** fournis par Rx.

> _Ces opérateurs Rx vous permettent de composer des séquences asynchrones ensemble de manière déclarative avec tous les avantages d'efficacité des rappels mais sans les inconvénients de l'imbrication des gestionnaires de rappel qui sont typiquement associés aux systèmes asynchrones._

Nous obtenons les avantages des rappels, sans ce fameux "enfer des rappels".

Voyez comment nous pouvons tirer parti de la puissance des opérateurs ci-dessous.

#### Un cas d'utilisation courant

Supposons que nous voulons rechercher un mot avec quelque chose comme une API de dictionnaire en utilisant le texte saisi par l'utilisateur en temps réel. Nous traitons essentiellement du stockage (dans le magasin Redux) et de l'affichage des résultats de l'appel API. Nous aimerions également débouncer l'appel API afin que l'API soit appelée dans, disons, 1 seconde après que l'utilisateur ait arrêté de taper.

Voici comment cela sera fait en utilisant Epic et les opérateurs RxJS :

```
const search = (action$, store) =>  action$.ofType('SEARCH')  .debounceTime(1000)  .mergeMap(action =>    ajax.getJSON(`https://someapi/words/${action.payload}`)     .map(payload => ({ type: 'SET_RESULTS', payload }))     .catch(payload => Observable.of({type: 'API_ERROR', payload}))  )
```

Trop à gérer ?! Ne vous inquiétez pas, décomposons cela.

L'epic reçoit un flux d'actions toutes `oftype` `'SEARCH'`. Puisque l'utilisateur tape continuellement, la charge utile de chaque action entrante (`action.payload`) contient la chaîne de recherche mise à jour.

L'opérateur `debounceTime()` est utilisé pour filtrer certaines des actions dans le flux sauf la dernière. Il transmet une action uniquement si 1 seconde s'est écoulée sans qu'il ne reçoive une autre action ou observable.

Nous faisons ensuite la requête AJAX, en mappant les résultats à une autre action `'set_RESULTS'` qui prend les données de réponse (`payload`) vers le réducteur, qui est la partie Action Out.

Toute erreur d'API est capturée en utilisant l'opérateur `catch`. Une nouvelle action est émise avec les détails de l'erreur et affiche ensuite un message avec le message d'erreur.

Remarquez comment le catch est à l'intérieur du `mergeMap()` et après la requête AJAX ? Cela est dû au fait que le `mergeMap()` crée une chaîne qui est isolée. Sinon, l'erreur atteindrait `ofType()` et mettrait fin à notre Epic. Si cela se produit, l'Epic cessera d'écouter toute action future !

Nous pouvons également utiliser des promesses traditionnelles pour les requêtes AJAX. Cependant, elles ont ce problème inhérent de ne pas pouvoir être annulées. Un autre cas d'utilisation important pour l'utilisation des Epics est donc l'annulation des requêtes AJAX.

Nous utilisons l'opérateur `takeUntil` pour gérer ce problème. Cela se fait de la même manière que nous avons utilisé cet opérateur `catch` à l'intérieur de `mergeMap` et après la requête AJAX.

Cela est dû au fait que `takeUntil` doit arrêter la requête AJAX actuelle et non l'ensemble de l'Epic ! Par conséquent, l'isolement des chaînes d'opérateurs est également important ici.

Le débouncing, le throttling, le filtrage, l'annulation des requêtes AJAX et autres, ne sont que la partie émergée de l'iceberg. Nous avons une myriade d'[opérateurs](http://reactivex.io/documentation/operators.html) à notre disposition, rendant les cas d'utilisation difficiles triviaux à résoudre. En utilisant ces opérateurs, vous pouvez être aussi créatif que votre imagination vous le permet ! La programmation réactive fonctionnelle (FRP) est élégante à sa manière.

Mon objectif pour cet article était de me concentrer sur la partie explication de la FRP dans Redux en utilisant Redux-Observable. Pour configurer Redux-Observable dans React+Redux, référez-vous à la [documentation officielle](https://redux-observable.js.org/) — elle est très bien documentée, détaillée et facile à suivre.

Assurez-vous de consulter mon autre article sur Redux qui explore les meilleures pratiques pour créer des réducteurs :

[**Réduire la plaque de code des réducteurs avec createReducer()**](https://medium.freecodecamp.org/reducing-the-reducer-boilerplate-with-createreducer-86c46a47f3e2)  
[_D'abord, un rapide récapitulatif de ce que sont les réducteurs dans Redux :_medium.freecodecamp.org](https://medium.freecodecamp.org/reducing-the-reducer-boilerplate-with-createreducer-86c46a47f3e2)

Vous voulez améliorer vos bases en JavaScript ? Lisez ces articles :

[**Fonctions JavaScript ES6 : Les Bonnes Parties**](https://medium.freecodecamp.org/es6-functions-9f61c72b1e86)  
[_ES6 offre quelques nouvelles fonctionnalités fonctionnelles cool qui rendent la programmation en JavaScript beaucoup plus flexible. Parlons de..._medium.freecodecamp.org](https://medium.freecodecamp.org/es6-functions-9f61c72b1e86)[**Un guide sur le hoisting des variables JavaScript ? avec let et const**](https://medium.freecodecamp.org/what-is-variable-hoisting-differentiating-between-var-let-and-const-in-es6-f1a70bb43d)  
[_Les nouveaux développeurs JavaScript ont souvent du mal à comprendre le comportement unique du hoisting des variables/fonctions._medium.freecodecamp.org](https://medium.freecodecamp.org/what-is-variable-hoisting-differentiating-between-var-let-and-const-in-es6-f1a70bb43d) [**Hoisting des Fonctions & Questions d'Entretien sur le Hoisting**](https://medium.freecodecamp.org/function-hoisting-hoisting-interview-questions-b6f91dbc2be8)  
[_Ceci est une partie 2 de mon article précédent sur le Hoisting des Variables intitulé « Un guide sur le hoisting des variables JavaScript ? avec..._medium.freecodecamp.org](https://medium.freecodecamp.org/function-hoisting-hoisting-interview-questions-b6f91dbc2be8)

Paix ✌️