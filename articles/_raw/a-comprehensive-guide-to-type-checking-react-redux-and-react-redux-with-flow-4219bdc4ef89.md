---
title: A comprehensive guide to type checking React, Redux, and React-Redux with Flow
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
seo_title: null
seo_desc: 'By Fabian Terh

  This article is divided into 4 sections:


  Type checking Redux actions, action creators, and reducers

  Installing Flow library definitions

  Type checking application state

  Type checking Redux store and dispatch


  While there are a bunch of...'
---

By Fabian Terh

This article is divided into 4 sections:

1. Type checking Redux actions, action creators, and reducers
2. Installing Flow library definitions
3. Type checking application state
4. Type checking Redux store and dispatch

While there are a bunch of guides on the first section which are immensely helpful, I found only a paucity of articles on 3 and 4. After a long session of Google searches, diving into source code, and trial and error, I decided to put together what I’ve learned and write this tutorial as a one-stop guide to type checking your React + Redux + React-Redux application with Flow.

### 1. Type checking Redux actions, action creators, and reducers

#### Actions

Redux actions are essentially vanilla Javascript objects with a mandatory `type` property:

```
// This is an action{  type: 'INCREASE_COUNTER',  increment: 1}
```

Following best practices, you may want to define and use [action type constants](https://redux.js.org/basics/actions) instead. If so, the above snippet would probably look something like this:

```
const INCREASE_COUNTER = 'INCREASE_COUNTER';
```

```
// This is an action{  type: INCREASE_COUNTER,  increment: 1}
```

Type checking is easy (we’re dealing with regular JavaScript here):

```
type $action = {  type: 'INCREASE_COUNTER',  increment: number};
```

Note that you cannot substitute the [literal string type](https://flow.org/en/docs/types/literals/) with the constant `INCREASE_COUNTER`. This is a [limitation](https://flow.org/try/#0PTACDMBsHsHcCh6QKYBcAEAjAhgJ3QLzoDkOuxA3EmuuNNAFxZ6ElmVA) of Flow itself.

#### Action creators

Since action creators are just functions that return actions, we’re still dealing with regular Javascript. This is how a type checked action creator can look like:

```
function increaseCounter(by: number): $action {  return {    type: INCREASE_COUNTER, // it's okay to use the constant here    increment: by  };}
```

#### Reducers

Reducers are functions that _handle actions_. They receive a state and an action, and return the new state. At this juncture, it’s important to think about how your state will look like (state shape). In this very simple example, the state shape comprises of only a single key `counter` which takes on a `number` type value:

```
// State shape{  counter: <number>}
```

And so your reducer could look like this:

```
const initialState = { counter: 0 };
```

```
function counter(state = initialState, action) {  switch (action.type) {    case INCREASE_COUNTER:      return Object.assign({}, state, {        counter: action.increment + state.counter      });        default:      return state;  }};
```

_Note: In this particular example,_ `Object.assign({}, state, { ... })` _is redundant because the store consists only of 1 key/value pair. I could just as easily return the last argument to the function. However, I included the full implementation for correctness._

Typing the state and reducer is simple enough. Here is the typed version of the above snippet:

```
type $state = {  +counter: number};
```

```
const initialState: $state = { counter: 0 };
```

```
function counter(  state: $state = initialState,  action: $action): $state {    switch (action.type) {    case INCREASE_COUNTER:      return Object.assign({}, state, {        counter: action.increment + state.counter      });        default:      return state;  }};
```

### Installing Flow library definitions

Flow [library definitions](https://flow.org/en/docs/libdefs/) (or libdefs) provide type definitions for third-party modules. In this case, we are using React, Redux, and React-Redux. Instead of typing these modules and their functions manually, you can install their type definitions using `flow-typed`:

```
npm install -g flow-typed
```

```
// Automatically download and install all relevant libdefsflow-typed install
```

```
// Orflow-typed install <package>@<version> // e.g. redux@4.0.0
```

Library definitions are installed to the `flow-typed` folder, which lets Flow work out of the box without any further configuration ([details](https://github.com/flowtype/flow-typed/wiki/Importing-And-Using-Type-Definitions)).

### Type checking application state

Previously, we have already typed the state like this:

```
type $state = {  +counter: number};
```

While this works for a simple example like the one above, it breaks down once your state becomes significantly larger. You would have to manually edit `type $state` every time you introduce a new reducer or modify an existing one. You also wouldn’t want to keep all your reducers in the same file. What you want to do instead is to refactor your reducers into separate modules, and use Redux’s `combineReducers` function.

Since the focus of this article is on _type checking_ a React/Redux/React-Redux application, and not on building one, I’m going to assume you are familiar with the `combineReducers` function. If not, head over to [Redux’s tutorial](https://redux.js.org/basics/reducers) to learn all about it.

Suppose we introduce a new action/reducer pair in a separate module:

```
// playSong.js
```

```
export const PLAY_SONG = 'PLAY_SONG';
```

```
// Typing the actionexport type $playSongAction = {  type: 'PLAY_SONG',  song: ?string};
```

```
// Typing the action creatorexport function playSong(song: ?string): $playSongAction {  return {    type: PLAY_SONG,    song: song  };};
```

```
// Typing arg1 and the return value of the reducer [*1]export type $song = ?string;
```

```
// Typing the state [*1]export type $songState = {  +song: $song};
```

```
// [*1][*2]const initialValue: $song = null;
```

```
// Typing the reducer [*1][*3]function song(  state: $song = initialValue,  action: $playSongAction): $song {    switch (action.type) {    case PLAY_SONG:      return action.song;        default:      return state;  }};
```

[*1]: If we’re using the `combineReducers` function, it’s important to note that **your reducer should no longer be returning the state, but rather the _value to the key in the state_**. In this regard, I think [Redux’s tutorial](https://redux.js.org/basics/reducers) is a bit lacking in clarity, as it does not state this explicitly, although it is clear from the example code snippets.

[*2]: Reducers are not allowed to return `undefined`, so we have to settle for `null`.

[*3]: Since the reducer is no longer receiving and returning a state in the form of `{ song: string }`, but rather the _value_ to the `song` key in the state object, we need to change the types of its first argument and return value from `$songState` to `$song`.

We modify and refactor `increaseCounter` as well:

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

Now we have 2 action/reducer pairs.

We can create a new `State` type to store the type of our application state:

```
export type State = $songState & $counterState;
```

This is a Flow [intersection type](https://flow.org/en/docs/types/intersections/), and is equivalent to:

```
export type State = {  song: $song,  counter: $counter};
```

If you don’t want to create `$songState` and `$counterState` only for use in intersection-typing the application state `State`, that’s perfectly fine too — go with the second implementation.

### Type checking Redux store and dispatch

I found that Flow was reporting errors in my containers (in the context of the [container/component paradigm](https://medium.com/@dan_abramov/smart-and-dumb-components-7ca2f9a7c7d0)).

```
Could not decide which case to select. Since case 3 [1] may work but if it doesn't case 6 [2] looks promising too. To fix add a type annotation to dispatch [3].
```

This was with regard to my `mapDispatchToProps` function. Cases 3 and 6 are as follows:

```
// flow-typed/npm/react-redux_v5.x.x.js
```

```
// Case 3declare export function connect<  Com: ComponentType<*>,  A,  S: Object,  DP: Object,  SP: Object,  RSP: Object,  RDP: Object,  CP: $Diff<$Diff<ElementConfig<Com>;, RSP>, RDP>  >(  mapStateToProps: MapStateToProps<S, SP, RSP>,  mapDispatchToProps: MapDispatchToProps<A, DP, RDP>): (component: Com) => ComponentType<CP & SP & DP>;
```

```
// Case 6declare export function connect<  Com: ComponentType<*>,  S: Object,  SP: Object,  RSP: Object,  MDP: Object,  CP: $Diff<ElementConfig<Com>, RSP>  >(  mapStateToProps: MapStateToProps<S, SP, RSP>,  mapDispatchToPRops: MDP): (component: Com) => ComponentType<$Diff<CP, MDP> & SP>;
```

**I don’t know why this error occurs.** But as the error hints, typing `dispatch` fixes it. And if we’re typing `dispatch`, we might as well type `store` too.

I couldn’t find much documentation on this aspect of typing a Redux/React-Redux application. I learned by diving into the libdefs and looking at the [source code for other projects](https://github.com/reduxjs/redux/tree/master/examples/todos-flow/src) (albeit a demonstration project). If you have any insights, please let me know so I can update this post (with proper attribution, of course).

In the meantime, I’ve found that this works:

```
import type {  Store as ReduxStore,  Dispatch as ReduxDispatch} from 'redux';
```

```
// import any other variables and types you may need,// depending on how you organized your file structure.
```

```
// Reproduced from earlier onexport type State = {  song: $song,  counter: $counter};
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

Heading into your container modules, you can then proceed to type `mapDispatchToProps` as follows: `const mapDispatchToProps = (dispatch: Dispatch) => { ...` };

### Wrapping up

This has been a pretty long post, and I hope you found it useful. I wrote it partly because of a dearth of resources regarding the later sections of this article (and partly to organize my thoughts and consolidate what I’ve learned).

I can’t guarantee that the guidance in this article follows best practices, or is conceptually sound, or even 100% correct. If you spot any errors or issues, please let me know!

