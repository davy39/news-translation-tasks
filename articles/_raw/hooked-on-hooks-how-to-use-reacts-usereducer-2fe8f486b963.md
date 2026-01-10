---
title: 'Hooked on hooks: how to use React’s useReducer()'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-16T16:29:04.000Z'
originalURL: https://freecodecamp.org/news/hooked-on-hooks-how-to-use-reacts-usereducer-2fe8f486b963
coverImage: https://cdn-media-1.freecodecamp.org/images/1*YxApEKMTlenh-lDQ-uWvJw.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Adeel Imran


  _Photo by [Unsplash](https://unsplash.com/@sebastian_unrau?utm_source=ghost&utm_medium=referral&utm_campaign=api-credit">Sebastian
  Unrau / <a href="https://unsplash.com/?utm_source=ghost&utm_medium=referral&utmcampaign=api-credit)

  So ...'
---

By Adeel Imran

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-248.png)
_Photo by [Unsplash](https://unsplash.com/@sebastian_unrau?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Sebastian Unrau</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

So the React Conference just happened and as always something new happened. _Hooks happened!_ The React team talked about suspense, lazy loading, concurrent rendering, and **_hooks_** :D.

%[https://www.youtube.com/watch?v=V-QO-KO90iQ]

Now I’ll talk about my favorite hook `useReducer` and how you use it.

```
import React, { useReducer } from 'react';

const initialState = {
  loading: false,
  count: 0,
};

const reducer = (state, action) => {
  switch (action.type) {
    case 'increment': {
      return { ...state, count: state.count + 1, loading: false };
    }
    case 'decrement': {
      return { ...state, count: state.count - 1, loading: false };
    }
    case 'loading': {
      return { ...state, loading: true };
    }
    default: {
      return state;
    }
  }
};

const delay = (time = 1500) => {
  return new Promise(resolve => {
    setTimeout(() => {
      resolve(true);
    }, time);
  });
};

function PokemonInfo() {
  const [{ count, loading }, dispatch] = useReducer(reducer, initialState);
  const onHandleIncrement = async () => {
    dispatch({ type: 'loading' });
    await delay(500);
    dispatch({ type: 'increment' });
  };
  const onHandleDecrement = async () => {
    dispatch({ type: 'loading' });
    await delay(500);
    dispatch({ type: 'decrement' });
  };
  return (
    <div>
      <p>Count {loading ? 'loading..' : count}</p>
      <button type="button" onClick={onHandleIncrement}>
        +
      </button>
      <button type="button" onClick={onHandleDecrement}>
        -
      </button>
    </div>
  );
}

export default PokemonInfo;
```

In my `PokemonInfo` component, I have:

```
const [{ count, loading }, dispatch] = useReducer(reducer, initialState);
```

Which is equivalent to:

```
const [state, dispatch] = useReducer(reducer, initialState);
const { count, loading } = state;
```

So what is `const [state, dispatch] = useReducer(param1, param2)` Let’s first talk about **array destructuing** which is happening below_._

```
const [state, dispatch] = useReducer(initialState);
```

Here’s an example of array destructing:

```
let myHeroes = ['Ant man', 'Batman']; // Mixing DC & Marvel :D
let [marvelHero, dcHero] = myHeroes; // destructuring array
/**
* myHeroes[0] == marvelHero => is 'Ant man'
* myHeroes[1] == dcHero => is 'Batman'
*/
```

So the method `useReducer` has two items in its array `state` and `dispatch`. Also the `useReducer` takes in two parameters: one is `reducer` the other is `initial-state`.

In the `useReducer` param `reducer`, I pass in:

```
const reducer = (state, action) => {
  switch (action.type) {
    case 'increment': {
      return { ...state, count: state.count + 1, loading: false };
    }
    case 'decrement': {
      return { ...state, count: state.count - 1, loading: false };
    }
    case 'loading': {
      return { ...state, loading: true };
    }
    default: {
      return state;
    }
  }
};
```

What this does is it takes in two arguments. One is the current state of the reducer and the other is the action. The `action.type` decides how it will update the reducer and return a new state to us.

So if the `action.type === increment`

```
case 'increment': {      
  return { ...state, count: state.count + 1, loading: false };    
}
```

…it will return the state, which will have its count updated to **_+1_** and loading set to **false**_._ Also where it says `state.count + 1` here the `state` is actually the previous state.

In `useReducer` param `initialState` I pass in:

```
const initialState = {  
  loading: false,  
  count: 0
};
```

So if this is the initial state, the `useReducer` method returns two items from its array, `state` and `dispatch`. The `state` method is an object which has two keys `count & loading` that I destructure in my destructured array.

So I destructure an array, and inside the array, I destructure an object on the first index of the array like below.

```
const [{ count, loading }, dispatch] = useReducer(reducer, initialState);
```

Also I have a method called `delay`

```
// return true after 1500ms in time argument is passed to.
const delay = (time = 1500) => {  
  return new Promise(resolve => {    
      setTimeout(() => {      
         resolve(true);    
      }, time);  
   });
};
```

Now in my render method when I click the `+` button

```
<button type="button" onClick={onHandleIncrement}>+</button>
```

the `onHandleIncrement` function is executed, which does the following:

```
const onHandleIncrement = async () => {    
   dispatch({ type: 'loading' });    
   await delay(500);    
   dispatch({ type: 'increment' });  
};
```

It initially sets `loading` to true, adds a delay of `500ms` and then increments the counter. Now I know this is not a real world case example, but it explains the point as to how a reducer works.

Last thing:

```
<p>Count {loading ? 'loading..' : count}</p>
```

If `loading` is true, I show `Count loading..` else I show `Count {value}`.

This is how it looks in the UI:

![Image](https://cdn-media-1.freecodecamp.org/images/1*HFN4x5wAuyE6vYNkV6_tcA.gif)
_Count example using useReducer hook_

I tried replicating [Dan Abramov’s](https://twitter.com/dan_abramov) code that he showcased at the React Conference 2018. Here is the link to the [**code repository**](https://github.com/adeelibr/react-hooks-demo)**.** Enjoy. :)

> Kindly do note that hooks are in an alpha version of React, and are in no way advised to be used in production. But there is a strong possibility that they will become a huge part of the eco-system in the future. So you should start playing around with react hooks now.

