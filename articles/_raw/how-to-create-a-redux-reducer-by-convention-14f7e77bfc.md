---
title: How to create a Redux reducer by convention
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-12T23:16:26.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-redux-reducer-by-convention-14f7e77bfc
coverImage: https://cdn-media-1.freecodecamp.org/images/1*xGMl8gP0E8ssx_mweswYQA.jpeg
tags:
- name: coding
  slug: coding
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: Redux
  slug: redux
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Cristian Salcescu

  Discover Functional JavaScript was named one of the best new Functional Programming
  books by BookAuthority!

  Redux is a very popular state management library. It simplifies the original Flux
  architecture by combining all stores an...'
---

By Cristian Salcescu

[**Discover Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE) was named one of the [**best new Functional Programming books by BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781)**!**

Redux is a very popular state management library. It simplifies the original Flux architecture by combining all stores and the dispatcher in a single store object.

Redux promotes the use of functional programming for managing state. It introduces the reducer function concept.

### Data flow

Let’s look at the data flow inside the Redux store.

An action is a plain object that contains all information necessary to do that action.

An action creator is a function that creates an action object.

### Reducer

A reducer is a pure function that takes state and action as parameters and returns the new state.

There may be many reducers managing parts of the root state. We can combine them together with `combineReducers()` utility function and create the root reducer.

Here is how the `todos` reducer may look like:

```
import matchesProperty from "lodash/matchesProperty";
function todos(todos = [], action) {
 switch (action.type) {
  case "add_todo":
    const id = getMaxId(todos) + 1;
    const newTodo = { ...action.todo, id };
    return todos.concat([newTodo]);
  case "remove_todo":
    const index = todos.findIndex(matchesProperty("id",
                                  action.todo.id));
    return [...todos.slice(0, index), ...todos.slice(index + 1)];
  case "reset_todos":
    return action.todos;
  default:
    return state;
  }
}
export default todos;
```

The `state` in this case is the list of to-dos. We can apply to its actions like `add_todo`, `remove_todo`, `reset_todos`.

### Reducer by convention

I would like to get rid of the `switch` statement in the reducer. Functions should be small and do one thing.

Let’s split the reducer into small pure functions with names matching the action types. I will call these setter functions. Each of them takes state and action as parameters and returns the new state.

```
function remove_todo(todos, action) {
  const index = todos.findIndex(matchesProperty("id",
                                action.todo.id));
  return [...todos.slice(0, index), ...todos.slice(index + 1)];
}

function reset_todos(todos, action) {
  return action.todos;
}

function add_todo(todos, action) {
  const id = getMaxId(todos) + 1;
  const newTodo = { ...action.todo, id};
  return todos.concat([newTodo]);
}
```

#### redux-actions

I would like to combine all these small functions together to create the original reducer function. We can use the `handleActions()` utility function from [redux-actions](https://redux-actions.js.org/) for this.

```
import { handleActions } from "redux-actions";

const reducer = handleActions(
  { remove_todo, reset_todos, add_todo },
  []
);

export default reducer;
```

The setter functions will run by convention. When an action with type `remove_todo` comes in, the `remove_todo()` setter function will be executed.

[Here is the sample code on codesandbox](https://codesandbox.io/s/26m5xrxry).

[**Discover Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE&source=post_page---------------------------) was named one of the [**best new Functional Programming books by BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781&source=post_page---------------------------)**!**

**For more on applying functional programming techniques in React take a look at** [**Functional React**](https://read.amazon.com/kp/embed?asin=B07S1NLFTS&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_Pko5CbA30383Y)**.**

Learn **functional React**, in a project-based way, with [**Functional Architecture with React and Redux**](https://read.amazon.com/kp/embed?asin=B0846NRJYR&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_o.hlEbDD02JB2)**.**

[Follow on Twitter](https://twitter.com/cristi_salcescu)

