---
title: Un guide complet pour la vérification de type de React, Redux et React-Redux
  avec Flow
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-15T04:55:36.000Z'
originalURL: https://freecodecamp.org/news/a-comprehensive-guide-to-type-checking-react-redux-and-react-redux-with-flow-4219bdc4ef89
coverImage: https://cdn-media-1.freecodecamp.org/images/1*VeM-5lsAtrrJ4jXH96h5kg.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Redux
  slug: redux
- name: 'tech '
  slug: tech
seo_title: Un guide complet pour la vérification de type de React, Redux et React-Redux
  avec Flow
seo_desc: 'By Fabian Terh

  This article is divided into 4 sections:


  Type checking Redux actions, action creators, and reducers

  Installing Flow library definitions

  Type checking application state

  Type checking Redux store and dispatch


  While there are a bunch of...'
---

Par Fabian Terh

Cet article est divisé en 4 sections :

1. Vérification de type des actions Redux, des créateurs d'actions et des réducteurs
2. Installation des définitions de bibliothèque Flow
3. Vérification de type de l'état de l'application
4. Vérification de type du magasin Redux et de la distribution

Bien qu'il existe de nombreux guides sur la première section qui sont extrêmement utiles, j'ai trouvé seulement une pénurie d'articles sur les sections 3 et 4. Après une longue session de recherches Google, de plongée dans le code source et d'essais et d'erreurs, j'ai décidé de rassembler ce que j'ai appris et d'écrire ce tutoriel comme un guide unique pour la vérification de type de votre application React + Redux + React-Redux avec Flow.

### 1. Vérification de type des actions Redux, des créateurs d'actions et des réducteurs

#### Actions

Les actions Redux sont essentiellement des objets Javascript vanilla avec une propriété `type` obligatoire :

```
// Ceci est une action{  type: 'INCREASE_COUNTER',  increment: 1}
```

En suivant les meilleures pratiques, vous pouvez vouloir définir et utiliser des [constantes de type d'action](https://redux.js.org/basics/actions) à la place. Si c'est le cas, l'extrait ci-dessus ressemblerait probablement à ceci :

```
const INCREASE_COUNTER = 'INCREASE_COUNTER';
```

```
// Ceci est une action{  type: INCREASE_COUNTER,  increment: 1}
```

La vérification de type est facile (nous traitons avec du JavaScript régulier ici) :

```
type $action = {  type: 'INCREASE_COUNTER',  increment: number};
```

Notez que vous ne pouvez pas substituer le [type de chaîne littérale](https://flow.org/en/docs/types/literals/) avec la constante `INCREASE_COUNTER`. C'est une [limitation](https://flow.org/try/#0PTACDMBsHsHcCh6QKYBcAEAjAhgJ3QLzoDkOuxA3EmuuNNAFxZ6ElmVA) de Flow lui-même.

#### Créateurs d'actions

Puisque les créateurs d'actions sont simplement des fonctions qui retournent des actions, nous traitons toujours avec du Javascript régulier. Voici à quoi peut ressembler un créateur d'actions avec vérification de type :

```
function increaseCounter(by: number): $action {  return {    type: INCREASE_COUNTER, // il est acceptable d'utiliser la constante ici    increment: by  };}
```

#### Réducteurs

Les réducteurs sont des fonctions qui _gèrent les actions_. Ils reçoivent un état et une action, et retournent le nouvel état. À ce stade, il est important de réfléchir à la forme de votre état (forme de l'état). Dans cet exemple très simple, la forme de l'état comprend seulement une seule clé `counter` qui prend une valeur de type `number` :

```
// Forme de l'état{  counter: <number>}
```

Et ainsi votre réducteur pourrait ressembler à ceci :

```
const initialState = { counter: 0 };
```

```
function counter(state = initialState, action) {  switch (action.type) {    case INCREASE_COUNTER:      return Object.assign({}, state, {        counter: action.increment + state.counter      });        default:      return state;  }};
```

_Note : Dans cet exemple particulier,_ `Object.assign({}, state, { ... })` _est redondant parce que le magasin ne consiste qu'en une seule paire clé/valeur. Je pourrais tout aussi facilement retourner le dernier argument de la fonction. Cependant, j'ai inclus l'implémentation complète pour la correction._

Le typage de l'état et du réducteur est assez simple. Voici la version typée de l'extrait ci-dessus :

```
type $state = {  +counter: number};
```

```
const initialState: $state = { counter: 0 };
```

```
function counter(  state: $state = initialState,  action: $action): $state {    switch (action.type) {    case INCREASE_COUNTER:      return Object.assign({}, state, {        counter: action.increment + state.counter      });        default:      return state;  }};
```

### Installation des définitions de bibliothèque Flow

Les [définitions de bibliothèque](https://flow.org/en/docs/libdefs/) (ou libdefs) de Flow fournissent des définitions de type pour les modules tiers. Dans ce cas, nous utilisons React, Redux et React-Redux. Au lieu de taper ces modules et leurs fonctions manuellement, vous pouvez installer leurs définitions de type en utilisant `flow-typed` :

```
npm install -g flow-typed
```

```
// Télécharger et installer automatiquement toutes les libdefs pertinentesflow-typed install
```

```
// Ouflow-typed install <package>@<version> // par exemple, redux@4.0.0
```

Les définitions de bibliothèque sont installées dans le dossier `flow-typed`, ce qui permet à Flow de fonctionner sans aucune configuration supplémentaire ([détails](https://github.com/flowtype/flow-typed/wiki/Importing-And-Using-Type-Definitions)).

### Vérification de type de l'état de l'application

Précédemment, nous avons déjà typé l'état comme ceci :

```
type $state = {  +counter: number};
```

Bien que cela fonctionne pour un exemple simple comme celui ci-dessus, cela se brise une fois que votre état devient significativement plus grand. Vous devriez éditer manuellement `type $state` chaque fois que vous introduisez un nouveau réducteur ou modifiez un réducteur existant. Vous ne voudriez pas non plus garder tous vos réducteurs dans le même fichier. Ce que vous voulez faire à la place, c'est de refactoriser vos réducteurs en modules séparés, et d'utiliser la fonction `combineReducers` de Redux.

Puisque le focus de cet article est sur la _vérification de type_ d'une application React/Redux/React-Redux, et non sur la construction d'une telle application, je vais supposer que vous êtes familiarisé avec la fonction `combineReducers`. Si ce n'est pas le cas, rendez-vous sur le [tutoriel de Redux](https://redux.js.org/basics/reducers) pour tout apprendre à ce sujet.

Supposons que nous introduisons une nouvelle paire action/réducteur dans un module séparé :

```
// playSong.js
```

```
export const PLAY_SONG = 'PLAY_SONG';
```

```
// Typage de l'actionexport type $playSongAction = {  type: 'PLAY_SONG',  song: ?string};
```

```
// Typage du créateur d'actionexport function playSong(song: ?string): $playSongAction {  return {    type: PLAY_SONG,    song: song  };};
```

```
// Typage de l'arg1 et de la valeur de retour du réducteur [*1]export type $song = ?string;
```

```
// Typage de l'état [*1]export type $songState = {  +song: $song};
```

```
// [*1][*2]const initialValue: $song = null;
```

```
// Typage du réducteur [*1][*3]function song(  state: $song = initialValue,  action: $playSongAction): $song {    switch (action.type) {    case PLAY_SONG:      return action.song;        default:      return state;  }};
```

[*1] : Si nous utilisons la fonction `combineReducers`, il est important de noter que **votre réducteur ne devrait plus retourner l'état, mais plutôt la _valeur de la clé dans l'état_**. À cet égard, je pense que le [tutoriel de Redux](https://redux.js.org/basics/reducers) manque un peu de clarté, car il ne précise pas explicitement cela, bien que cela soit clair à partir des extraits de code d'exemple.

[*2] : Les réducteurs ne sont pas autorisés à retourner `undefined`, donc nous devons nous contenter de `null`.

[*3] : Puisque le réducteur ne reçoit plus et ne retourne plus un état sous la forme `{ song: string }`, mais plutôt la _valeur_ de la clé `song` dans l'objet d'état, nous devons changer les types de son premier argument et de sa valeur de retour de `$songState` à `$song`.

Nous modifions et refactorisons également `increaseCounter` :

```
// increaseCounter.js
```

```
export const INCREASE_COUNTER = 'INCREASE_COUNTER';
```

```
export type $increaseCounterAction = {  type: 'INCREASE_COUNTER',  increment: number};
```

```
export function increaseCounter(by: number): $action {  return {    type: INCREASE_COUNTER,    increment: by  };};
```

```
export type $counter = number;
```

```
export type $counterState = {  +counter: $counter};
```

```
const initialValue: $counter = 0;
```

```
function counter(  state: $counter = initialValue,  action: $increaseCounterAction): $counter {    switch (action.type) {    case INCREASE_COUNTER:      return action.increment + state;        default:      return state;  }};
```

Nous avons maintenant 2 paires action/réducteur.

Nous pouvons créer un nouveau type `State` pour stocker le type de notre état d'application :

```
export type State = $songState & $counterState;
```

Il s'agit d'un type d'intersection Flow, et est équivalent à :

```
export type State = {  song: $song,  counter: $counter};
```

Si vous ne voulez pas créer `$songState` et `$counterState` uniquement pour une utilisation dans le typage par intersection de l'état de l'application `State`, c'est parfaitement acceptable également — optez pour la deuxième implémentation.

### Vérification de type du magasin Redux et de la distribution

J'ai constaté que Flow signalait des erreurs dans mes conteneurs (dans le contexte du [paradigme conteneur/composant](https://medium.com/@dan_abramov/smart-and-dumb-components-7ca2f9a7c7d0)).

```
Impossible de décider quel cas sélectionner. Puisque le cas 3 [1] peut fonctionner mais si ce n'est pas le cas, le cas 6 [2] semble prometteur également. Pour corriger, ajoutez une annotation de type à dispatch [3].
```

Cela concernait ma fonction `mapDispatchToProps`. Les cas 3 et 6 sont les suivants :

```
// flow-typed/npm/react-redux_v5.x.x.js
```

```
// Cas 3declare export function connect<  Com: ComponentType<*>,  A,  S: Object,  DP: Object,  SP: Object,  RSP: Object,  RDP: Object,  CP: $Diff<$Diff<ElementConfig<Com>;, RSP>, RDP>  >(  mapStateToProps: MapStateToProps<S, SP, RSP>,  mapDispatchToProps: MapDispatchToProps<A, DP, RDP>): (component: Com) => ComponentType<CP & SP & DP>;
```

```
// Cas 6declare export function connect<  Com: ComponentType<*>,  S: Object,  SP: Object,  RSP: Object,  MDP: Object,  CP: $Diff<ElementConfig<Com>, RSP>  >(  mapStateToProps: MapStateToProps<S, SP, RSP>,  mapDispatchToPRops: MDP): (component: Com) => ComponentType<$Diff<CP, MDP> & SP>;
```

**Je ne sais pas pourquoi cette erreur se produit.** Mais comme l'erreur le suggère, le typage de `dispatch` la corrige. Et si nous typons `dispatch`, nous pouvons tout aussi bien typer `store` également.

Je n'ai pas trouvé beaucoup de documentation sur cet aspect du typage d'une application Redux/React-Redux. J'ai appris en plongeant dans les libdefs et en regardant le [code source d'autres projets](https://github.com/reduxjs/redux/tree/master/examples/todos-flow/src) (bien qu'il s'agisse d'un projet de démonstration). Si vous avez des idées, faites-le moi savoir afin que je puisse mettre à jour cet article (avec une attribution appropriée, bien sûr).

En attendant, j'ai trouvé que cela fonctionne :

```
import type {  Store as ReduxStore,  Dispatch as ReduxDispatch} from 'redux';
```

```
// importer toute autre variable et type dont vous pourriez avoir besoin,// en fonction de la manière dont vous avez organisé votre structure de fichiers.
```

```
// Reproduit plus tôtexport type State = {  song: $song,  counter: $counter};
```

```
export type Action =   | $playSongAction  | $increaseCounterAction
```

```
export type Store = ReduxStore<State, Action>;
```

```
export type Dispatch = ReduxDispatch<Action>;
```

En vous rendant dans vos modules de conteneur, vous pouvez ensuite procéder au typage de `mapDispatchToProps` comme suit : `const mapDispatchToProps = (dispatch: Dispatch) => { ...` };

### Conclusion

Cet article a été assez long, et j'espère que vous l'avez trouvé utile. Je l'ai écrit en partie à cause du manque de ressources concernant les dernières sections de cet article (et en partie pour organiser mes pensées et consolider ce que j'ai appris).

Je ne peux pas garantir que les conseils de cet article suivent les meilleures pratiques, ou sont conceptuellement solides, ou même 100% corrects. Si vous repérez des erreurs ou des problèmes, faites-le moi savoir !