---
title: How to create your first Redux middleware with ease
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-13T07:27:26.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-your-first-redux-middleware-with-ease-a75e6b1384db
coverImage: https://cdn-media-1.freecodecamp.org/images/0*G6zSXWOpLVBgghzy.
tags:
- name: JavaScript
  slug: javascript
- name: open source
  slug: open-source
- name: React
  slug: react
- name: Redux
  slug: redux
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Gabriele Cimato

  Almost every real-word React app makes extensive use of async requests. If you manage
  your app state with Redux, there are several ways to handle async actions.

  You may have heard of redux-thunkor redux-saga, the most popular solut...'
---

By Gabriele Cimato

Almost every real-word React app makes extensive use of async requests. If you manage your app state with Redux, there are several ways to handle async actions.

You may have heard of `redux-thunk`or `redux-saga`, the most popular solutions to handling async actions in Redux. Such approaches come in handy when you need to track the status of a request in your state.

A pattern that I have seen quite often that leverages `thunks` is the following:

```js
import {
  FETCH_DATA_ERROR,
  FETCH_DATA_PENDING,
  FETCH_DATA_SUCCESS,
} from 'constants/actionTypes';

function fetchMyDataError(error) {
  return {
    type: FETCH_DATA_ERROR,
    payload: error,
  };
}

function fetchDataPending() {
  return { type: FETCH_DATA_PENDING };
}

function fetchMyDataSuccess(response) {
  return {
    type: FETCH_DATA_SUCCESS.
    payload: response,
  };
}

function fetchData() {
  return (dispatch) => {
    dispatch(fetchDataPending());
      
    fetch('https://my-api.com/my-data')
      .then(res => res.json())
      .then(data => dispatch(fetchMyDataSuccess(data)))
      .catch(err => dispatch(fetchMyDataError(err)));
  };
}
```

As you can see, we wrote a good amount of code. This example can be simplified and handled with one function only. Either way, it will soon feel very repetitive and tedious, especially if you need to track the lifespan of every async request in your app. Such verbosity doesn’t help with the boilerplate necessary for an app that uses Redux.

When a pattern or a code block gets used over and over again, it’s a good practice to extract it in a function. This will abstract the logic of it, and only requires the least amount of data to “function.” That’s when I started playing with the idea of writing my own middleware. `[redux-slim-async](https://github.com/Gabri3l/redux-slim-async)` helps me skip boilerplate code and provide great control with a tiny API. Let’s see now the previous example with the new middleware:

```js
import {
  FETCH_DATA_PENDING,
  FETCH_DATA_SUCCESS,
  FETCH_DATA_ERROR,
} from 'constants/actionTypes';

function fetchData() {
  return {
    types: [
      FETCH_DATA_PENDING,
      FETCH_DATA_SUCCESS,
      FETCH_DATA_ERROR,
    ],
    callAPI: fetch(‘https://my-api.com/my-data')
      .then(res => res.json()),
  }
}
```

All those awkward functions are gone and our `fetchData` is now minimal — pretty neat! ?

Now let’s go ahead and build a smaller version of such middleware. It will help us understand the inner workings of it and hey, you’ll be able to build your own next!

### Creating a middleware

Let me show you the code for this small middleware right away. You’ll see that it’s not as overwhelming as you might think.

```js
function createSlimAsyncMiddleware({ dispatch, getState }) {
  return next => action => {
    const {
      types,
      callAPI,
      shouldCallAPI = () => true,
    } = action;
      
    if (!actionIsValid(action)) next(action);
    if (!shouldCallAPI(getState())) {
      return Promise.resolve(getState());
    }
      
    const [pendingType, successType, errorType] = types;
      
    dispatch({ type: pendingType });
      
    return callAPI()
      .then(response => {
        dispatch({
          type: successType,
          payload: response,
        });
        
        return Promise.resolve(getState());
      })
      .catch(error => {
        dispatch({
          type: errorType,
          payload: error,
        });
        
        return Promise.reject(error);
     });
  };
}
```

Wait a second…that’s it? Absolutely!

Let’s go one line at a time. This middleware is a function that returns a function, that returns a function that returns a `Promise`. As funky as it sounds, you’ll find that it’s much simpler than it seems.

Our middleware function receives an object with two fields: `dispatch` and `getState`. These are [named parameters](http://2ality.com/2011/11/keyword-parameters.html) provided by Redux.

* `dispatch`: as the name suggests, this is what we use to dispatch an action. It’ll give us the power of handling actions inside the middleware
* `getState`: this is a function that returns the current state at a given time. This can be useful if we want to return the updated state after an action has been dispatched

On the **first line** we have a function with one object argument with fields `dispatch` and `getState`.

On the **second line** we return a function that takes an argument called `next`. Such a function returns a function that takes an `action` and does something. More on that later. But what is `next` for ? Why are we expected to return a function that returns a function that does something?

What Redux does under the hood is [compose](https://github.com/reactjs/redux/blob/master/src/compose.js) the middlewares so that each one has a reference to…the `next` one! The name helps a lot to make it intuitive. We are wrapping the official Redux `dispatch` function with our middleware. This builds a pipeline that an action has to go through.

Remember that you don’t HAVE TO call `next(action)`, but you need to do so if you don’t want to block the dispatching process (we’ll see a specific case in our middleware).

![Image](https://cdn-media-1.freecodecamp.org/images/n9N9siS5VEsMDiFEBrOSMK-ko91Zl8Z4SoFM)
_A flow chart that explores the middleware pipeline in a simplified way_

In our case, it’s useful because we don’t want to intercept every action, only the ones that are valid for our middleware. For simplicity, I added a check called `actionIsValid`. This function takes an `action` as an argument and returns a boolean. The returned boolean represents the validity of this action for our middleware.

`actionisValid` is a good place to check for errors and `throw` them if necessary. If it’s not valid, then I will use our reference to the `next` middleware and pass the action to it. Otherwise we can finally use the action and “do something” (the flowchart above represents a simplified version of this logic).

The rest of the middleware is pretty intuitive. We check the validity of the action to determine if our async request should proceed or not.

`shouldCallAPI` is a parameter of our middleware API. Given the state, it returns a boolean that determines if our request should execute or not. The middleware provides a default value for it (a function that returns `true` ). If we don’t need to make the API call, then we return `Promise.resolve`. This way we can use `.then` or `async/await` on any asynchronous action that goes through our middleware.

```js
const [pendingType, successType, errorType] = types;
```

The next step is to determine the action `type` field passed in as a parameter. We use array [destructuring](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment#Array_destructuring) to disassemble our `types` array parameter.

```js
dispatch({ type: pendingType });
```

Now we can finally use the `dispatch` method. This dispatches a Redux action like you would normally do. Such action represents the “pending” state of our async request.

```js
return callAPI()
  .then(response => {
    dispatch({
      type: successType,
      payload: response,
    });
    
    return Promise.resolve(getState());
  })
  .catch(error => {
    dispatch({
      type: errorType,
      payload: error,
    });
    
    return Promise.reject(error);
  });
```

We finally have our last `return` statement. Here we make the API call and, based on how the `Promise` resolves, we dispatch and return different values.

* **Success**: given the response from the API, we dispatch a success action. The payload is the response of the request. Right after that, we return a `Promise` that resolves with the up-to-date state of our app. This allows us to use `.then(updatedState => …do somethi`ng)
* **Error:** if the `Promise` rejects then we dispatch an error action. In this case the payload is the error itself.

That’s it! As shown before, we can then create actions and use them as follows:

```
// Our Action

function fetchData() {
  return {
    types: [
      FETCH_DATA_PENDING,
      FETCH_DATA_SUCCESS,
      FETCH_DATA_ERROR,
    ],
    shouldCallAPI: state => state.dataArr.length === 0,
    callAPI: () =>
      fetch('https://my-api.com/my-data').then(res => res.json()),
  }
}

// Inside the component

class MyComponent extends Component {
  componentDidMoun() {
    this.props.fetchData()
      .then(state => {
        console.log('updated state after async action:', state);
      })
      .catch(err => {
        console.log('an error occured');
      });
  }
  
// Rest of the component omitted...

}
```

In this simple case we fetch data only if our data array is empty. Then we log the updated state after the request or an error message if the `Promise` rejects..

### Conclusion

Creating Redux middlewares is intuitive. You have access to the store dispatcher and the `getState` function. Use them to access the latest state of your app or dispatch actions.

You also need to remember to use `next` when necessary and make sure not to block the dispatching pipeline. In our case, if we didn’t call `next(action)` , any action that was not valid for our middleware would be basically discarded ⚠️!!

Some implementation details were omitted here for simplicity. If you want to dig a little deeper, feel free to explore the `redux-slim-async` middleware [here](https://github.com/Gabri3l/redux-slim-async).

Give it a ⭐️ if you like it! I built this middleware and currently use it in production to avoid a lot of boilerplate. Feel free to give it a try and provide feedback anytime. Here is another valuable resource to explore middlewares even more, the [redux docs](https://redux.js.org/advanced/middleware)!

You can also follow me on twitter [@SuperGabry](https://twitter.com/SuperG4bry)

