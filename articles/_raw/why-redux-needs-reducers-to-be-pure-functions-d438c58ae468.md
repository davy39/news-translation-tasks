---
title: Why Redux need reducers to be “pure functions”
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-11-22T19:28:08.000Z'
originalURL: https://freecodecamp.org/news/why-redux-needs-reducers-to-be-pure-functions-d438c58ae468
coverImage: https://cdn-media-1.freecodecamp.org/images/1*NkvKvkRk8RcMgQLJoIIBsQ.png
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By rajaraodv

  You may have heard that Redux depends on “pure functions” from functional programming.
  Well, what exactly does that mean?

  The picture below shows a simple Todo app from Redux examples. It currently has
  four tasks. It shows the fourth one...'
---

By rajaraodv

You may have heard that Redux depends on “pure functions” from functional programming. Well, what exactly does that mean?

The picture below shows a simple Todo app from [Redux examples](https://github.com/reactjs/redux/tree/master/examples/todos). It currently has four tasks. It shows the fourth one as completed, and is set to show “All” Tasks — both completed and not completed.

The right-hand side shows the current state stored in Redux. It’s a simple JavaScript object that captures all the details in one place.

That’s the beauty of Redux.

![Image](https://cdn-media-1.freecodecamp.org/images/4eco4msoESVRWtcsEabWFpm0WWzxEO1gDURs)
_LEFT: Todo app ← →RIGHT: Redux stated_

Now, let’s say you toggled the fourth task to be not-completed. Here’s what the app would look like with a new Redux state:

![Image](https://cdn-media-1.freecodecamp.org/images/6WaOKohJOCgbgJGvAoYokKhcZR-wNmDYWVBc)
_Redux updates it’s state when the app changes_

Now, if you look at the Reducer for “TOGGLE_TODO” — the one that toggles the status of a Todo item between completed and not completed — it looks like below ([here’s the source code](https://github.com/reactjs/redux/blob/master/examples/todos/src/reducers/todos.js#L9-L17)):

![Image](https://cdn-media-1.freecodecamp.org/images/-jheepAaXFn835dchdmurqshr8-d1Dm7AVDV)

When you toggle a Todo item’s state, this is what happens: the reducer function takes an object that represents the “old” state (i.e. input to a function), then creates a brand new object by copying all the old object’s details into a it (like **id** and **text**) and overriding old properties with new ones (**completed** prop).

![Image](https://cdn-media-1.freecodecamp.org/images/Moec8tswLUsuI8-zFNT5gs-Y0HKMSAm6nqSe)

### Pure functions

At a fundamental level, any function that doesn’t alter input data and that doesn’t depend on external state (like a database, DOM, or global variable) and consistently provides the same output for the same input is a “pure” function.

For example, the below **add** function doesn’t alter “a” or “b”, doesn’t depending on external state, and always returns the same output for the same input.

```
const add = (a, b) => a + b //pure function
```

Now, if you look at our reducer function, it is a “pure” function as it has the same features.

### But _why_ should the reducer be a “pure” function?

Let’s see what happens if we make our reducer “impure.” Let’s comment out the section where it creates a new object, and instead let’s mutate the state’s completed prop directly.

```
case 'TOGGLE_TODO':      if (state.id !== action.id) {        return state;      }
```

```
            // return {      //   ...state,      //   completed: !state.completed      // }
```

```
      state.completed = !state.completed;//change original object      return state;
```

```
default: ...
```

Now if we try to toggle the TODO after this change, nothing happens!

Let’s see what’s going on in the Redux’s source.

![Image](https://cdn-media-1.freecodecamp.org/images/lxQkKAq1x7nWzokdsojlcF9gjhQi3ZUNM38Z)

Redux takes a given state (object) and passes it to each reducer in a loop. And it expects a _brand new_ object from the reducer if there are _any_ changes. And it also expects to get the old object back if there are no changes.

Redux simply checks whether the old object is the same as the new object by comparing the memory locations of the two objects. So if you mutate the old object’s property inside a reducer, the “new state” and the “old state” will both point to the same object. Hence Redux thinks nothing has changed! So this won’t work.

But, it still doesn’t answer some key questions like:

* Why is Redux designed like this?
* Why can’t Redux just make a copy of the old state some place else, then compare object props from reducers?
* Why is Redux putting this burden on individual developers?

The answer: there is only one way to know if two JavaScript objects have the same properties. To deep-compare them.

But this becomes extremely expensive in real-world apps, because of the typically large objects and the number of times they need to be compared.

So one work around is to **have a policy** to ask developers to create a **new** object whenever there is a change, then send it to the framework. And if there are no changes, then send back the old object as it is. **In other words, new objects represent new states.**

Note that you must clone old states using slice — or a similar mechanism — to copy old values into a new object.

Now, with this policy in place, you can compare two objects’ memory location using `!==` without having to compare each property within each object. And if the two objects are not the same, then you know that the object has changed state (that is, some property somewhere in the JavaScript object has changed). That’s exactly the strategy Redux employs to make things work.

So that’s why Redux needs for “Reducers” to be pure functions!

Thank you for reading! If you liked the post please ? and share it on Twitter!??

### Some of my other posts

#### React Performance:

1. [_Two Quick Ways To Reduce React App’s Size In Production_](https://medium.com/@rajaraodv/two-quick-ways-to-reduce-react-apps-size-in-production-82226605771a#.6lepbl7ae)
2. [_Using Preact Instead Of React_](https://medium.com/@rajaraodv/using-preact-instead-of-react-70f40f53107c#.7fzp0lyo3)

#### Functional Programming

1. [_JavaScript Is Turing Complete — Explained_](https://medium.com/@rajaraodv/javascript-is-turing-complete-explained-41a34287d263#.6t0b2w66p)
2. [_Functional Programming In JS — With Practical Examples (Part 1)_](https://medium.com/@rajaraodv/functional-programming-in-js-with-practical-examples-part-1-87c2b0dbc276#.fbgrmoa7g)
3. [_Functional Programming In JS — With Practical Examples (Part 2)_](https://medium.com/@rajaraodv/functional-programming-in-js-with-practical-examples-part-2-429d2e8ccc9e#.r2mglxozr)
4. [_Why Redux Need Reducers To Be “Pure Functions”_](https://medium.com/@rajaraodv/why-redux-needs-reducers-to-be-pure-functions-d438c58ae468#.bntrywxrf)

#### ES6

1. [_5 JavaScript “Bad” Parts That Are Fixed In ES6_](https://medium.com/@rajaraodv/5-javascript-bad-parts-that-are-fixed-in-es6-c7c45d44fd81#.7e2s6cghy)
2. [_Is “Class” In ES6 The New “Bad” Part?_](https://medium.com/@rajaraodv/is-class-in-es6-the-new-bad-part-6c4e6fe1ee65#.4hqgpj2uv)

#### WebPack

1. [_Webpack — The Confusing Parts_](https://medium.com/@rajaraodv/webpack-the-confusing-parts-58712f8fcad9#.6ot6deo2b)
2. [_Webpack & Hot Module Replacement [HMR]_](https://medium.com/@rajaraodv/webpack-hot-module-replacement-hmr-e756a726a07#.y667mx4lg) _(under-the-hood)_
3. [_Webpack’s HMR And React-Hot-Loader — The Missing Manual_](https://medium.com/@rajaraodv/webpacks-hmr-react-hot-loader-the-missing-manual-232336dc0d96#.fbb1e7ehl)

#### Draft.js

1. [_Why Draft.js And Why You Should Contribute_](https://medium.com/@rajaraodv/why-draft-js-and-why-you-should-contribute-460c4a69e6c8#.jp1tsvsqc)
2. [_How Draft.js Represents Rich Text Data_](https://medium.com/@rajaraodv/how-draft-js-represents-rich-text-data-eeabb5f25cf2#.hh0ue85lo)

#### React And Redux :

1. [_Step by Step Guide To Building React Redux Apps_](https://medium.com/@rajaraodv/step-by-step-guide-to-building-react-redux-apps-using-mocks-48ca0f47f9a#.s7zsgq3u1)
2. [_A Guide For Building A React Redux CRUD App_](https://medium.com/@rajaraodv/a-guide-for-building-a-react-redux-crud-app-7fe0b8943d0f#.g99gruhdz) _(3-page app)_
3. [_Using Middlewares In React Redux Apps_](https://medium.com/@rajaraodv/using-middlewares-in-react-redux-apps-f7c9652610c6#.oentrjqpj)
4. [_Adding A Robust Form Validation To React Redux Apps_](https://medium.com/@rajaraodv/adding-a-robust-form-validation-to-react-redux-apps-616ca240c124#.jq013tkr1)
5. [_Securing React Redux Apps With JWT Tokens_](https://medium.com/@rajaraodv/securing-react-redux-apps-with-jwt-tokens-fcfe81356ea0#.xci6o9s6w)
6. [_Handling Transactional Emails In React Redux Apps_](https://medium.com/@rajaraodv/handling-transactional-emails-in-react-redux-apps-8b1134748f76#.a24nenmnt)
7. [_The Anatomy Of A React Redux App_](https://medium.com/@rajaraodv/the-anatomy-of-a-react-redux-app-759282368c5a#.7wwjs8eqo)
8. [_Why Redux Need Reducers To Be “Pure Functions”_](https://medium.com/@rajaraodv/why-redux-needs-reducers-to-be-pure-functions-d438c58ae468#.bntrywxrf)
9. [_Two Quick Ways To Reduce React App’s Size In Production_](https://medium.com/@rajaraodv/two-quick-ways-to-reduce-react-apps-size-in-production-82226605771a#.6lepbl7ae)

#### Salesforce

1. [_Developing React Redux Apps In Salesforce’s Visualforce_](https://medium.com/@rajaraodv/developing-react-redux-apps-in-salesforce-s-visualforce-3ad7be560d1c#.f6bao6mtu)

