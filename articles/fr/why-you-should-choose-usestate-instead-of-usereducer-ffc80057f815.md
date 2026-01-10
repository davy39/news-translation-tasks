---
title: Pourquoi vous devriez choisir useState plutôt que useReducer
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-15T16:09:31.000Z'
originalURL: https://freecodecamp.org/news/why-you-should-choose-usestate-instead-of-usereducer-ffc80057f815
coverImage: https://cdn-media-1.freecodecamp.org/images/1*H0sjMujtQTS7_BclV-vCTA.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Pourquoi vous devriez choisir useState plutôt que useReducer
seo_desc: 'By Austin Malerba

  A guide to local and global state management via useState


  Since the introduction of the React Hooks API, I’ve seen a lot of discussion about
  useState, useReducer, and when to use one over the other. From these conversations,
  one wo...'
---

Par Austin Malerba

#### Un guide pour la gestion d'état local et global via useState

![Image](https://cdn-media-1.freecodecamp.org/images/GdEbO-4fptOH0cOPppjan1ZlporpXn0rTF8c)

Depuis l'introduction de l'API React Hooks, j'ai vu beaucoup de discussions sur `useState`, `useReducer`, et quand utiliser l'un plutôt que l'autre. À partir de ces conversations, on pourrait conclure que `useState` est mieux adapté pour un état simple avec une logique de mise à jour simple et que `useReducer` est mieux pour des formes d'état complexes avec une logique de mise à jour complexe.

Je suis ici pour vous convaincre que **quand il est enveloppé dans un hook personnalisé de 4 lignes, useState peut être tout aussi puissant, sinon plus puissant que useReducer** lors de la gestion d'un état complexe.

Je n'aime pas les reducers. J'ai essayé de les utiliser, mais je finis toujours par migrer vers autre chose. Il y a quelque chose qui ne va pas avec le fait de dispatcher des actions pour déclencher une logique métier quand je pourrais le faire en invoquant une fonction avec des arguments.

Et puis il y a le fait qu'au lieu d'encapsuler ma logique métier dans des fonctions, je suis censé tout regrouper dans une seule fonction géante partitionnée par une série de cas switch ? J'ai essayé des bibliothèques comme [redux-actions](https://www.npmjs.com/package/redux-actions) pour atténuer cette préoccupation, mais je n'ai toujours pas pu m'y faire. Mon aversion pour les reducers m'a motivé à chercher une meilleure solution.

Passons en revue quelques raisons courantes pour lesquelles les gens choisissent `useReducer` plutôt que `useState` :

1. Pour que la logique métier puisse être centralisée dans le reducer plutôt que dispersée dans le composant
2. Les reducers sont des fonctions pures faciles à tester en isolation de React
3. Les reducers permettent de mettre à jour de manière prévisible des morceaux d'état qui dépendent les uns des autres (alors que plusieurs `useState` pourraient ne pas le faire)

Si l'un de ces points est confus, je recommande de jeter un œil à cet [article](https://www.robinwieruch.de/react-usereducer-vs-usestate/). Tout au long de ce guide, je ferai référence à ces éléments comme les trois avantages des reducers.

### Étape Une : Construire un Exemple

Tout d'abord, je vais vous montrer un exemple qui met en évidence les avantages des reducers que j'ai mentionnés ci-dessus, puis je vais vous montrer comment vous pouvez implémenter la même fonctionnalité via `useState` sans sacrifier aucun des avantages d'une solution `useReducer`.

#### Un Compteur Gelable

Pour illustrer les avantages/inconvénients de `useState` vs `useReducer`, je vais implémenter un simple compteur avec une touche spéciale. Le compteur peut être incrémenté, mais peut aussi être gelé. Si dans l'état gelé, l'incrémentation du compteur ne fera rien.

Comme vous pouvez le voir, j'ai implémenté notre compteur ci-dessus une fois avec `useState` et une fois avec `useReducer`. Cependant, `StateCounterV1` a quelques problèmes. En fait, il ne fonctionne même pas comme prévu.

On s'attendrait à ce que `StateCounterV1` rende `<div>1</div>` parce que nous incrémentons le compteur une fois, puis nous gelons le compteur, et ensuite nous incrémentons à nouveau. Mais en réalité, il rend `<div>2</div>` parce que le deuxième appel d'incrément n'a pas accès à la nouvelle valeur de frozen. Cela illustre l'avantage #3 de useReducer sur useState.

Il est également évident que dans `StateCounterV1`, notre logique pour incrémenter le compteur réside dans le composant lui-même, mais dans `ReducerCounter`, la logique appartient au `countReducer` (avantage #1).

Et enfin, nous voyons que pour tester la logique de comptage dans `StateCounterV1`, nous devrions le rendre, alors que pour tester la logique dans `countReducer`, nous pourrions le faire sans jamais avoir à rendre un composant. Nous pourrions le tester simplement en l'invoquant avec un état et une action et en nous assurant qu'il produit le prochain état correct (avantage #2).

### Étape Deux : Consolidation de l'État

Dans notre exemple, nous avons une transition d'état, `increment`, qui met à jour `count` mais dépend d'un _autre_ morceau d'état, `frozen`. Dans des cas comme celui-ci, je trouve qu'il est préférable de consolider l'état. En théorie, nous pourrions toujours avoir un maximum d'un hook `useState` par composant et encore atteindre toute la fonctionnalité que nous voulons. Mais il est tout à fait acceptable d'utiliser `useState` plusieurs fois _tant que les morceaux d'état ne dépendent pas les uns des autres lors de la mise à jour_. Cela dit, voyons comment la consolidation de l'état peut nous rendre l'avantage #3 des reducers.

Maintenant, le mise à jour passé à `setState` dans notre fonction `increment` est autosuffisant. Il n'a plus besoin d'atteindre `frozen` via la fermeture pour déterminer comment produire le prochain état. Au lieu de cela, `prevState` contient tout l'état nécessaire pour effectuer sa logique de mise à jour.

Parce qu'il est autosuffisant, nous n'avons plus besoin de le déclarer au moment du rendu, nous pourrions plutôt le sortir du composant.

Lorsque nous sortons les déclarations de mise à jour d'état de notre composant, non seulement nous améliorons les performances, mais nous nous empêchons de dépendre accidentellement de variables via la fermeture comme nous l'avons fait dans `StateCounterV1`. Ce modèle est un peu à côté du sujet de cet article, mais je pensais que je le mentionnerais quand même.

### Étape Trois : Extraction de la Logique Métier

À ce stade, `StateCounterV2` est encore encombré de logique de compteur. Mais ne vous inquiétez pas, tout ce que nous avons à faire est d'extraire toute notre logique métier de compteur dans un hook personnalisé. Appelons-le `useCounterApi`.

Maintenant, `StateCounterV3` a l'air bien. Je dirais qu'il a même meilleure allure que le `ReducerCounter`. Sans parler du fait que ce refactoring était simple car il n'a vraiment pris qu'un copier/coller de notre logique de compteur dans un hook personnalisé. Mais voici où les choses deviennent délicates.

Il peut être difficile parfois, en tant que développeurs, d'identifier où la logique appartient. Nos cerveaux sont erratiques et il y a des jours où il ne me viendrait pas à l'esprit d'extraire cette logique du composant dans un hook de compteur personnalisé. C'est pourquoi nous, les développeurs, avons besoin d'interfaces opinionnées pour nous guider dans la bonne direction.

### Étape Quatre : Créer un Guide

Si nous devions décrire `useCounterApi` verbalement, nous dirions probablement,

> « C'est un hook personnalisé qui crée et retourne une API de compteur. »

Ici réside notre premier indice. Il _crée et retourne une API_. Ainsi, c'est une Usine d'API. Plus spécifiquement, c'est une _Usine d'API de Compteur_.

Mais nous aimons abstraire les choses, donc la prochaine question est, comment pouvons-nous faire une _Usine d'API Générique_ ? Eh bien, enlevons la partie « Compteur » de `useCounterApi`. Maintenant, il nous reste `useApi`. Super, maintenant nous avons notre Usine d'API Générique. Mais où va notre logique métier ?

Réfléchissons davantage à la façon dont `useReducer` fonctionne.

```
const [state, dispatch] = useReducer(reducer, initialArg, init);
```

Le premier argument de `useReducer` est un reducer et le deuxième argument est l'état initial. Rappelez-vous que le reducer contient la logique métier. Essayons d'imiter cette interface.

```
const api = useApi(someApiFactoryFunction, initialArg);
```

D'accord, on a l'impression d'être proche d'une solution. Mais maintenant, nous devons déterminer ce que diantre `someApiFactoryFunction` est censé faire.

Eh bien, nous savons qu'il devrait contenir la logique métier et nous savons qu'il devrait être ignorant de React afin que nous puissions le tester sans avoir à rendre un composant. Ce que nous savons aussi, c'est que `someApiFactoryFunction` ne peut pas contenir une invocation `useState` car alors il _serait_ conscient des choses React. Mais il a sûrement besoin de `state` et `setState`. Nous devrons donc injecter `state` et `setState` d'une autre manière. Alors, comment injectons-nous des choses dans des fonctions ? Oh oui, des paramètres. En rassemblant cet exercice de réflexion, nous aboutissons à ce qui suit.

Et le voilà. `useApi` est notre hook personnalisé magique de 4 lignes qui révèle la vraie puissance de `useState`. Les fonctions d'usine d'API nous fournissent l'état actuel et un rappel `setState` et nous permettent d'exposer une API à partir de celles-ci. Réfléchissons aux types d'avantages que nous venons d'introduire avec ce simple changement de contrat.

`counterApiFactory` est ignorant de React, ce qui signifie que nous pouvons maintenant le tester simplement en passant un objet `state` et un rappel `setState` (avantage du reducer #2 atteint).

`useApi` attend une usine d'API, ce qui signifie que nous disons au développeur qu'il _doit_ écrire des fonctions d'usine d'API avec la signature `({state, setState}) =>` api. Cela signifie que, même lors de mes jours de congé où mon cerveau a du mal à reconnaître qu'un groupe de logique peut être refactorisé en une API stateful, j'ai cette belle petite fonction `useApi` qui me pousse à mettre toute ma logique métier stateful dans un emplacement centralisé.

### Étape Cinq : Optimisation

Tel qu'il est, `useApi` n'est pas aussi efficace qu'il pourrait l'être. Tout composant qui consomme `useApi` invoquera `useApi` à chaque rendu, ce qui signifie que `apiFactory` sera également invoqué à chaque rendu. Il n'est pas nécessaire d'invoquer `apiFactory` à chaque rendu, mais plutôt seulement lorsque `state` a changé. Nous pouvons optimiser `useApi` en mémorisant l'exécution de `apiFactory`.

### Tester une Usine d'API

Maintenant que nous avons implémenté notre hook `useApi`, voyons comment nous testerions une usine d'API.

Il est assez simple de créer un wrapper autour de notre `counterApiFactory` qui imite le comportement de `state`/`setState`. Avec cette fonction d'aide, nous pouvons tester notre `counterApiFactory` de manière très naturelle.

### useApi vs useReducer

Comparons maintenant ces deux solutions.

#### Encapsulation de la Logique

Dans les deux solutions, la logique de mise à jour de l'état est centralisée, ce qui permet un raisonnement, un débogage et des tests faciles. Cependant, les reducers ne fournissent qu'un mécanisme pour _mettre à jour_ l'état, ils ne fournissent pas de mécanisme pour _récupérer_ l'état. Au lieu de cela, il est courant d'écrire des sélecteurs et de les appliquer en aval du reducer. Ce qui est bien avec notre solution `useApi`, c'est qu'elle encapsule non seulement la logique de mise à jour de l'état, mais aussi la logique de _récupération_ de l'état.

#### Mise à jour de l'État

Pour mettre à jour l'état avec `useReducer`, nous devons dispatcher des actions. Pour mettre à jour l'état avec `useApi`, nous devons invoquer des méthodes de mise à jour. Un avantage potentiel des reducers dans ce scénario est que plusieurs reducers pourraient écouter la même action. Cependant, cela comporte également un inconvénient : le flux d'exécution n'est pas intuitif une fois qu'une action a été dispatchée. Si j'ai besoin de plusieurs morceaux d'état disparates pour être mis à jour en même temps, je préfère le faire explicitement avec plusieurs appels de méthodes d'API consécutifs, plutôt que par une seule action dispatchée qui est diffusée à tous les reducers.

#### Performance

Une chose agréable à propos des reducers est que, via la composition de reducers, plusieurs reducers peuvent écouter une seule action dispatchée, ce qui signifie que vous pouvez avoir de nombreuses parties de l'état changer en un seul rendu. Je n'ai pas trouvé de solution pour la composition d'usines d'API (bien que ce soit sûrement possible). Pour l'instant, ma solution est d'invoquer les mise à jour d'état consécutivement lorsque cela est nécessaire, ce qui pourrait entraîner plus de rendus qu'une approche par reducer.

#### Code Boilerplate

Les solutions basées sur les reducers sont notoirement verbeuses (surtout lorsqu'on travaille avec redux). Les déclarations de types d'actions prennent un peu d'espace supplémentaire et le dispatching d'actions tend à être un peu plus verbeux que l'invocation d'une fonction avec des arguments. Pour ces raisons, je dirais que `useApi` a un léger avantage sur `useReducer` en termes de code boilerplate.

#### Testabilité

Les reducers et les usines d'API sont tous deux faciles à tester.

### Explorer davantage useApi

Regardons quelques autres choses cool que nous pouvons faire avec `useApi`.

J'ai pris le temps d'implémenter l'exemple classique de [Liste de Todos Redux](https://redux.js.org/basics/example) via `useApi`. Voici à quoi ressemble `todosApiFactory` dans l'implémentation useApi.

Une chose dégoûtante que vous avez peut-être remarquée dans le code ci-dessus est la répétition du boilerplate suivant.

```
setState(prevState => ({  ...prevState,  /*  */}));
```

En supposant que notre `state` est un objet et parce que `setState` ne supporte pas la [fusion superficielle](https://reactjs.org/docs/hooks-reference.html#usestate), nous devons faire cela pour nous assurer que nous préservons tout état avec lequel nous ne travaillons pas actuellement.

Nous pouvons réduire une partie de ce boilerplate et obtenir quelques autres avantages cool d'une bibliothèque appelée [immer](https://github.com/immerjs/immer). Immer est une bibliothèque d'immuabilité qui vous permet d'écrire du code immuable de manière mutable.

Comme vous pouvez le voir, immer nous aide à supprimer une partie de ce code boilerplate ennuyeux requis lors de l'écriture de mises à jour immuables. Mais attention, la commodité d'immer est aussi son talon d'Achille. Un développeur qui est introduit au concept d'immuabilité par immer pourrait ne pas comprendre pleinement les conséquences des mutations.

Mais attendez une seconde, `useApi` ne fournit l'état que _localement_, mais l'[Exemple de Liste de Todos](https://redux.js.org/basics/example) utilise redux pour fournir une solution d'état _global_.

#### Stores Globaux avec les `API Factories`

Voyons comment nous pouvons créer des stores globaux à partir des API Factories.

Pas mal du tout, n'est-ce pas ? Le contexte rend l'état global super facile dans React. Nous avons donc maintenant une solution de gestion d'état global à utiliser avec les API Factories.

Ci-dessous se trouve l'exemple de liste de todos API Factory fonctionnelle.

### Conclusion

Pour conclure, cet article contient trois fonctions que vous pourriez trouver utiles.

Ces fonctions fournissent des abstractions utiles pour la gestion d'état local et global alimentée par `useState`.

Ne vous méprenez pas, les reducers viennent avec beaucoup de avantages, mais je ne peux tout simplement pas me reposer facilement avec l'interface qu'ils offrent. `useApi` et `useReducer` offrent tous deux des solutions viables pour la gestion d'état complexe. C'est vraiment une question de préférence.

Un point utile à retenir est que les bibliothèques n'ont pas besoin d'effectuer une logique complexe pour être utiles. Une grande partie de la valeur que les bibliothèques et les frameworks offrent n'a pas à voir avec la logique qu'ils effectuent, mais plutôt avec le guidage qu'ils donnent au développeur. Les bonnes bibliothèques/frameworks forcent le développeur à suivre des modèles connus via des interfaces explicites et opinionnées. `useApi` fait très peu de calculs, mais encourage le développeur à mettre sa logique métier stateful dans un emplacement centralisé, tout en évitant la pollution des composants.