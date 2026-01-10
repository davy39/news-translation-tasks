---
title: 'From Reduce to Redux: Understanding Redux by Building Redux'
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
seo_title: null
seo_desc: 'By Johnny Snelgrove

  The two most important techniques I’ve discovered to help with understanding a concept
  quickly are simplification and learning by doing. Redux is an extremely popular
  JavaScript library for developing “predictable state containers...'
---

By Johnny Snelgrove

The two most important techniques I’ve discovered to help with understanding a concept quickly are _simplification_ and _learning by doing_. [Redux](https://redux.js.org/) is an extremely popular JavaScript library for developing “predictable state containers for JavaScript apps.” It takes a functional approach to modeling data, which challenges the traditional MVC pattern.

Many developers, including myself, found this paradigm shift difficult. However, understanding this approach is incredibly rewarding and valuable. The concepts transcend languages and frameworks, and professionally, many modern front ends are adopting Redux and its associated functional paradigms to handle their client-side data layer.

In this post, we’ll build a simplified Redux library from scratch in order to _really_ understand Redux. Starting with a simple sum function, we’ll gradually build up to a Redux-style state management system for a simple game agent.

#### What’s Reduce?

The key to understanding Redux lies in understanding the power of the _reduce_ function. From the [Mozilla Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce):

> “The reduce() method applies a function against an accumulator and each element in the array (from left to right) to reduce it to a single value.”

If this doesn’t make sense to you, fear not. The power of _reduce_ comes from its generality, which also makes it difficult to describe. To remember what _reduce()_ does, just remember that _reduce_ rhymes with _deduce_. The reduce function deduces the next state given an existing state and a transition rule. It does this for each element in an array, from left to right, passing the result along in series, then returning the final result. Here is a possible implementation of _reduce()_:

```
function reduce (collection, transitionFn, initialState) {  let accumulator = initialState || collection[0]  for (let i = (initialState ? 0 : 1); i < collection.length; i++) {    accumulator = transitionFn(accumulator, collection[i])  }  return accumulator}
```

_Side Note: the transition function actually accepts four arguments: the accumulator, the current value (i.e. collection[i]), the index of the current value, and the collection itself. However, for demonstration purposes, the index and collection arguments are omitted here as they’re irrelevant._

Lucky for us, _reduce()_ is already a builtin array method in JavaScript, and uses the calling array as the collection to reduce. Now that we have an idea of what the reduce function is, it’s time to dive deeper and start exploring how we can use it to model the state of a game agent.

#### Using Reduce

To understand the power of _reduce_, we’ll start off with the canonical reducer function, _sum():_

```
function sum (nums) {  return nums.reduce((state, nextVal) => state + nextVal)}
```

```
sum([1, 2, 3, 4]) // => 10
```

This example never gave me that _“Aha!”_ moment. Probably because it obscures the function signature and isn’t very exciting. Here’s the same example with everything spelled out explicitly:

```
function sum (nums) {  function transition (prevState, nextVal) {    return prevState + nextVal  }  const [initialState, ...tail] = nums  return tail.reduce(transition, initialState)}
```

```
sum([1, 2, 3, 4]) // => 10
```

_note: `const [initialState, …tail] = nums` uses ES6 [destructuring](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment) to split the array into the first element (initialState) and the remaining elements (tail)._

Here we can see that the reduce function takes a transition function as its first argument, and an initial starting state as its second argument. By default, reduce uses the first item in the array as the initial state if no initial state is supplied.

#### Getting Specific

To conceptually move towards modeling more interesting data, we can rewrite _sum_ with domain-specific variable names:

```
function move (steps) {  return steps.reduce((state, direction) => state + direction)}
```

```
xPosition = -2xPosition = xPosition + move([-1, -1, 0, 1, 1, 1])console.log(xPosition) // => -1
```

This is still the same summation function, but now it’s a bit clearer how it might be used in a real-world application. Our game character starts with an initial position of -2, which we then combine with a list of directions to determine the new position. Each value in the array passed into the _move_ function can be thought of as an **action** that will tell the reducer how to mutate its state. Here our actions don’t have names, but by following some simple conventions, we arrive at the basis of redux:

```
let store = 0 // initial position
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

If we agree that all of our array elements will be objects with a _type_ field, then we can start explicitly handling actions in the reducer. Furthermore, by passing the existing store as the initial state to _reduce()_ then overwriting it with the result, we can start transforming data across multiple calls to reduce.

We also arrive at a concept similar to that of a class with instance variables and methods. In OOP, everything in _store_ might be an instance variable, and the action types would be methods:

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

#### Complex Data

At this point, our character can only move left and right, and has no other interesting properties. To make things more interesting, and to extend this concept into multidimensional data, let’s add the ability to move up and down, and give the player some health:

```
let store = { x:0, y:0, health: 100 } // initial state
```

```
const reducer = (state, action) => {  switch (action.type) {    case 'MOVE_LEFT':      return { ...state, x: state.x - action.distance }    case 'MOVE_RIGHT':      return { ...state, x: state.x + action.distance }    case 'MOVE_UP':      return { ...state, y: state.y - action.distance }    case 'MOVE_DOWN':      return { ...state, y: state.y + action.distance }    case 'TAKE_DAMAGE':      return { ...state, health: state.health - action.damage }    case 'DRINK_POTION':      return { ...state, health: state.health + action.health }    case 'WAIT':    default:      return state  }}
```

```
console.log(store) // => { x:0, y:0, health: 100 }store = [  {type: 'MOVE_LEFT', distance: 2 },  {type: 'MOVE_LEFT', distance: 3 },  {type: 'MOVE_RIGHT', distance: 7 },  {type: 'WAIT'},  {type: 'MOVE_DOWN', distance: 7 },  {type: 'TAKE_DAMAGE', damage: 50 },  {type: 'DRINK_POTION', health: 25 },  {type: 'MOVE_UP', distance: 2 },].reduce(reducer, store)console.log(store) // => { x:2, y:5, health: 75 }
```

Here the state is an object with shape `{x: Float, y: Float, health: Float}`. The reducer must return a new object with the same shape. To return a new object, we use ES6 object destructuring (e.g. `{...state}`) to create a copy of the passed-in state object, then overwrite the field we’d like to update in one concise declarative expression: `return {...oldState, key: newKeyVal}`. Now we’re cookin’ with fire!

#### Generalizing and Encapsulating

To wrap this logic up and make stores general and reusable, we can write a _createStore_ function to encapsulate the state and provide a consistent API for reading the state and dispatching actions:

```
const createStore = (reducer, initialState) => {  let store = initialState || reducer(undefined, {type: 'INIT'})  return {    dispatch: (action) => {      store = [action].reduce(reducer, store)    },    getState: _ => store  }}
```

```
var moverReducer = (state = { x:0, y:0 }, action) => {  switch (action.type) {    case 'MOVE_LEFT':      return { ...state, x: state.x - action.distance }    case 'MOVE_RIGHT':      return { ...state, x: state.x + action.distance }    case 'MOVE_UP':      return { ...state, y: state.y - action.distance }    case 'MOVE_DOWN':      return { ...state, y: state.y + action.distance }    case 'WAIT':    default:      return state  }}
```

```
let agent = createStore(moverReducer)agent.dispatch({type:'MOVE_UP', distance: 1})agent.dispatch({type:'MOVE_LEFT', distance: 2})agent.dispatch({type:'MOVE_RIGHT', distance: 4})agent.dispatch({type:'MOVE_DOWN', distance: 2})agent.getState() // => { x:-2, y:0 }
```

Here we can either pass _createStore()_ an initial state (maybe something we load from localStorage), or it will initialize using the reducer’s default state argument and a dummy action. Our state is encapsulated using a closure, and the only way to read and write to it is through the returned _getState()_ and _dispatch()_ methods, respectively.

At this point, we’ve arrived at a basic but useful version of the Redux API! We’ve omitted store enhancers and subscriptions, however, since they’re primarily used for side effects and reactively updating a view. In the final section, we’ll simply use a render loop and top-level code to handle these cases and keep things simple.

#### Pros and Cons

The first clear benefit of the reducer approach is that everything is easily serializable. We could easily use localStorage to save and load the state, serialize action sequences, send actions via WebSockets or HTTP requests, and so on, all without building out handlers to translate JSON payloads to instance method calls.

In addition, since reducers should be [pure functions](https://en.wikipedia.org/wiki/Pure_function), there’s no guarantee that unexpected side effects won’t occur in other parts of your application via updating a model’s data. A store is purely concerned with data modeling and logic. This makes our data models extremely portable, as they’re not concerned with their runtime environment. The same reducers could potentially be used in a node.js cli app, a web app, or a native app via something like React Native. Porting the application becomes a matter of writing platform-specific side effects and view code.

Finally, I personally find reducers to be elegant. The concept is closer to a mathematical equation that is setting values in a model from a controller script. Check out the [Q-learning formula](https://en.wikipedia.org/wiki/Q-learning#Algorithm) as an example. Its signature is a state/action pair! This makes it easier to translate a formula to code.

The downside is that redux doesn’t have a strong opinion on how to [handle side effects](https://github.com/reactjs/redux/issues/1528) (for example, rendering to the DOM, logging to the console, saving to localStorage, starting an Ajax request, and so on). You cannot build an interesting application without side effects, so this can be a little frustrating.

The solution is generally to put this code in action creating methods, middleware, or move it to the top level of your application (not ideal). However, it can often be beneficial to write model code with this constraint, as it forces you to write easily testable code and focus on the logic of what you’re modeling.

Other downsides include lots of boilerplate to accomplish simple tasks like incrementing a counter, and the general cognitive load it takes to move away from object-oriented concepts. However, these are what make our models so portable and powerful!

#### Wrapping Up and Wandering Around

To wrap this all up, we can add an update loop to dispatch random actions and render the agent’s state (here I’m using React, but we could use any view layer we like). At every tick, the agent either moves in a direction, waits, takes a potion or takes damage. If the agent’s health is at zero, it resets.

Notice how logic is starting to accumulate in the top level update/render loop. In addition, we’ve had to duplicate the code for the initial reducer state to reset the agent when its health hits zero.

We’ll address these and other issues in the next article, but for now, it’s enough to notice that logic can live in at least two places: the reducer or the action. In the next article, we’ll look at how to choose where to place that logic, and proceed to dive deeper, making our simulation more sophisticated using function composition, higher-order reducers, and action creators as we develop an increasingly intelligent game agent.

