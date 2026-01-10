---
title: Réduire la verbosité du Reducer avec createReducer()
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-14T20:09:16.000Z'
originalURL: https://freecodecamp.org/news/reducing-the-reducer-boilerplate-with-createreducer-86c46a47f3e2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*qBvXcdtU2MeWhsdD9Cpu0g.png
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: Redux
  slug: redux
- name: Web Development
  slug: web-development
seo_title: Réduire la verbosité du Reducer avec createReducer()
seo_desc: 'By Bhuvan Malik

  First, a quick recap of what reducers in Redux are:

  Reducers are nothing but pure functions that take in the previous state and an action
  and return the new state.

  Two things to keep in mind are that they are pure and therefore don’t ...'
---

Par Bhuvan Malik

D'abord, un rapide rappel de ce que sont les reducers dans Redux :

**Les reducers ne sont rien d'autre que des fonctions pures qui prennent l'état précédent et une action et retournent le nouvel état.**

Deux choses à garder à l'esprit sont qu'ils sont **purs** et donc **ne mutent pas l'état**.

Cela étant dit, passons aux choses sérieuses.

Lorsque nous commençons avec Redux, voici comment nous écrivons un reducer :

Nous avons un reducer de recherche qui met à jour l'état en fonction de différentes actions comme la définition des résultats de recherche, la mise à jour de la chaîne de recherche ou le changement d'état d'un chargeur/spinner. Supposons qu'il s'agisse d'un [slice reducer](http://redux.js.org/docs/recipes/reducers/SplittingReducerLogic.html), que nous pouvons combiner plus tard en utilisant la fonction `combineReducers(reducers)`.

Maintenant, si vous êtes comme moi, vous n'êtes peut-être pas fan des instructions switch ?

Elles viennent avec trop de verbosité propre à elles. Un reducer gérant de nombreux types d'actions en utilisant des cas de switch serait long. Et cela n'aurait pas l'air bien, n'est-ce pas ?! L'idée est d'abandonner le switch et de passer à une approche plus fonctionnelle.

### **Repensons un peu cela**

Ce que nous pouvons faire, c'est abstraire toute notre logique de cas de switch dans des "fonctions de cas" et créer un objet qui mappe les types d'actions à leurs fonctions de cas correspondantes. Nous appellerons cet objet 'actionHandlers'.  
Voici l'objet :

Comme vous pouvez le voir, nous avons maintenant un mappage des types d'actions aux fonctions de cas.

> _Les fonctions de cas sont comme de petites fonctions de reducer qui prennent l'état et l'action entrante comme arguments et retournent une nouvelle partie de l'arbre d'état._

Maintenant, nous devons créer une fonction "créateur de reducer" pour utiliser nos `**actionHandlers**`. Cette fonction retournera une autre fonction qui sera en fait notre reducer passé à `combineReducers()`. Voici :

Comme vous pouvez le voir, `createReducer()` est une fermeture retournant une autre fonction. Cette fonction retournée satisfait la forme `(previousState, action) => newState` et sera donc notre véritable slice reducer.

La fonction de reducer retournée peut accéder aux arguments `actionHandlers` et `initialState` de sa fonction englobante grâce à la fermeture. L'`initialState` est utilisé comme argument par défaut pour `state`. À l'intérieur de la fonction de reducer, nous vérifions si nos `actionHandlers` ont une propriété correspondant au type d'action entrant. Si c'est le cas, nous exécutons cette fonction de cas à l'intérieur de `actionHandlers`, en passant l'état et l'action. Si le type d'action n'est pas une propriété à l'intérieur de `actionHandlers`, nous retournons l'état précédent.

Vous pouvez trouver `createReducer()` dans la [documentation officielle de Redux](http://redux.js.org/docs/recipes/ReducingBoilerplate.html) également.

Cette fonction de création de reducer peut maintenant être importée dans différents fichiers de reducer pour créer tous nos slice reducers !

La fonction ci-dessus est verbeuse pour le moment pour des raisons d'explication. Ajoutons un peu d'épices ! Voici le nouveau et amélioré fichier de création de reducer. ?

J'ai raccourci tout en utilisant des lambdas et la fonction 'propOr' de la bibliothèque Ramda. Ce que fait la fonction propOr, c'est prendre le 2ème argument (une clé) pour vérifier à l'intérieur du 3ème argument (un objet), et retourne sa valeur si elle est trouvée. Sinon, elle retourne la valeur par défaut fournie à partir du 1er argument. Le 1er argument, 'identity', est une fonction qui retourne simplement le paramètre qui lui est fourni.

Ainsi, une fonction est retournée si elle est trouvée dans `actionHandlers` qui est exécutée en utilisant `(state, action`. Dans le cas où l'action n'est pas trouvée, propOr retourne identity, qui est exécutée avec les mêmes arguments `(state, action)` et retourne le premier argument fourni, qui est `state` (l'état précédent dans ce cas).

Vous pouvez créer vos propres fonctions 'propOr' et 'identity', Ramda est juste ce que j'utilise.

Permettez-moi de vous montrer le nouveau fichier de reducer de recherche pour que vous ayez une vue d'ensemble de la façon dont nous utilisons notre fonction `createReducer` avec les `actionHandlers`.

La fonction `createReducer` est partiellement appliquée et retourne notre slice reducer final et est exportée vers un fichier où nous utilisons la fonction `combineReducers`.

Eh bien, voilà, une bonne façon de créer des reducers et de réduire la verbosité globale. J'espère que cela vous sera utile d'une manière ou d'une autre :)

![Image](https://cdn-media-1.freecodecamp.org/images/1*AhRFvNgwGHEH_Zzm-3MI_w.gif)

Voici quelques liens vers mes articles précédents :

[**Fonctions JavaScript ES6 : Les Bonnes Parties**](https://medium.freecodecamp.com/es6-functions-9f61c72b1e86)  
[_ES6 offre quelques nouvelles fonctionnalités fonctionnelles cool qui rendent la programmation en JavaScript beaucoup plus flexible. Parlons de..._medium.freecodecamp.com](https://medium.freecodecamp.com/es6-functions-9f61c72b1e86)[**Un guide sur le hoisting des variables JavaScript ? avec let et const**](https://medium.freecodecamp.com/what-is-variable-hoisting-differentiating-between-var-let-and-const-in-es6-f1a70bb43d)  
[_Les nouveaux développeurs JavaScript ont souvent du mal à comprendre le comportement unique du hoisting des variables/fonctions._medium.freecodecamp.com](https://medium.freecodecamp.com/what-is-variable-hoisting-differentiating-between-var-let-and-const-in-es6-f1a70bb43d)

Paix ✌️