---
title: How to integrate React Hooks into your project without changing your Redux
  code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-22T18:29:24.000Z'
originalURL: https://freecodecamp.org/news/how-to-integrate-react-hooks-into-your-project-without-changing-your-redux-code-974e6f70f0b0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*RijhIwu_gn98_W_QnYcGAA.jpeg
tags:
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Redux
  slug: redux
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Mohammad Iqbal

  In this tutorial we will be going over how to integrate React Hooks into a React
  Redux project without changing the Redux code (reducers and actions) at all.

  To save time, we can start with with a basic React Redux app instead of bu...'
---

By Mohammad Iqbal

In this tutorial we will be going over how to integrate React Hooks into a React Redux project without changing the Redux code (reducers and actions) at all.

To save time, we can start with with a basic React Redux app instead of building one from scratch. This will allow you to see the before and after code side by side and make integration for your app much easier.

You can also follow me on twitter for more tutorials in the future: [here](https://twitter.com/iqbal125sf) 

**Starter code:**

[**iqbal125/modern-react-app-sample**](https://github.com/iqbal125/modern-react-app-sample)  
[_Contribute to iqbal125/modern-react-app-sample development by creating an account on GitHub._github.com](https://github.com/iqbal125/modern-react-app-sample)

#### Using the correct Version of React

The very first thing we have to do is make sure we have the correct version of React. At the time of this writing, create-react-app does not give you the correct version. So what you can do is use create-react-app then go into your package.json and type in the correct version. So just change React and React-dom to version 16.8. Save the file and delete your node modules folder. Run npm install and you are good to go.

```javascript
{
  "name": "app2",
  "version": "0.1.0",
  "private": true,
  "dependencies": {
    "auth0-js": "^9.8.2",
    "history": "^4.7.2",
    "react": "^16.8.0",
    "react-dom": "^16.8.0",
    "react-redux": "^6.0.0",
    "react-router": "^4.3.1",
    "react-router-dom": "^4.3.1",
    "react-scripts": "2.1.1",
    "redux": "^4.0.1"
  },
```

#### Refactoring a React class to a React Hook

So the first thing we will do is refactor a React class component to a React Hook. Let’s open our App.js file and turn it into a Hook, so refactor your App.js to the following:

```javascript
import React, { Component } from 'react';
import Routes from './routes';



const App = () => {

    return(
      <div>
      React
      <Routes />
      </div>
    )
}


export default App;
```

So basically just turn the class into an arrow function and delete the render method. And that’s it, you have now created a React Hook!

#### Setting up another Hook

In the same way, we can setup up another Hook, which we will setup in a folder called Hooks.

So create a hooks_container.js file in the hooks directory and set it up like so:

```javascript
import React, { useState } from 'react';




const HooksContainer = () => {

    return(
      <div>

      </div>
    )
}


export default HooksContainer;
```

#### The useState() Hook

We will now begin to set up some basic non-global component state with the useState() hook.

The useState() hook is similar to the React setState() function. It is setup with array destructuring, where the first element in the array is the state value and the second element is a function to change the state.

Let’s just create basic increment and decrement buttons to see how the use state function.

Set up the buttons like so:

```javascript
import React, { useState } from 'react';




const HooksContainer = () => {

  const [value, setValue] = useState(0)

  const incrementValue = () => {
    setValue(value + 1 )
  }

  const decrementValue = () => {
    setValue(value - 1 )
  }

    return(
      <div>
        <button onClick={() => incrementValue()}> Add Local Value </button>
        <button onClick={() => decrementValue()}> Dec Local Value </button>
        <br />
        <div>
          Local React State: {value}
        </div>
      </div>
    )
}


export default HooksContainer;
```

Notice we don’t have to use the “props” or “state” keyword anywhere we can just use the variable and function name directly. This is one of the things that makes React Hooks so easy to work with.

Your app should look something like this.

![Image](https://cdn-media-1.freecodecamp.org/images/0*CscqAv6uPi86BjMB)

And you should be able to freely increase or decrease the number.

Now that we have a basic idea of how useState() works we can move onto something a little more complex.

#### useReducer() hook

We can now begin setting up the useReducer() hook.

Before we can use the useReducer() hook we must first setup the reducer. The actions can actually be left as is. And the change we have to make to the reducer is very minimal. All we have to do is change the export statements instead of exporting default. We have to export both the reducer and the initial state.

To save time, just create a new reducer called hooks_reducer.js in the reducer file and copy the code from Reducer1. You should have something that looks like this:

```javascript

import * as ACTION_TYPES from '../actions/action_types'

export const initialState = {
  stateprop1: false,
}

export const HooksReducer1 = (state = initialState, action) => {
    switch(action.type) {
      case ACTION_TYPES.SUCCESS:
        return {
          ...state,
          stateprop1: true
        }
      case ACTION_TYPES.FAILURE:
        return {
          ...state,
          stateprop1: false
        }
      default:
        return state
    }
}
```

Now simply import this reducer and its initial state to the hooks_container.js. And pass them both in to the useReducer() hook.

```javascript

import * as HooksReducer1 from '../store/reducers/hooks_reducer';

...

const [state, dispatch] = useReducer(HooksReducer1.HooksReducer1, HooksReducer1.initialState)
```

Let’s also create 2 buttons to change stateprop1 from false to true and then false again. And we can also create a ternary expression to display text depending on whether stateprop1 is true or false. Remember that stateprop1 is the same one we set up in the HookReducer1, but we are updating here in our container.

And we are using the same pre-existing actions to update the reducer. Notice in the comments I left two alternate methods of dispatching actions. They are all doing the same thing. Returning a javascript object with a type of a string of SUCCESS.

So your code should look like this:

```javascript
import React, { useState } from 'react';
import * as ACTIONS from '../store/actions/actions';
import * as HooksReducer1 from '../store/hooks_state/reducer1_hooks';



const HooksContainer = () => {

  const [state, dispatch] = useReducer(HooksReducer1.HooksReducer1, HooksReducer1.initialState)
  const [value, setValue] = useState(0)

  const incrementValue = () => {
    setValue(value + 1 )
  }

  const decrementValue = () => {
    setValue(value - 1 )
  }
  
  const handleDispatchTrue = () => {
    //    dispatch(type: "SUCCESS")
    //    dispatch(ACTIONS.SUCCESS)
    dispatch(ACTIONS.success())
  }

  const handleDispatchFalse = () => {
    //     dispatch(type: "FAILURE")
    //    dispatch(ACTIONS.FAILURE)
    dispatch(ACTIONS.failure())
  }

    return(
      <div>
        <button onClick={() => incrementValue()}> Add Local Value </button>
        <button onClick={() => decrementValue()}> Dec Local Value </button>
        <button onClick={() => handleDispatchTrue()}>Dispatch True </button>
        <button onClick={() => handleDispatchFalse()}>Dispatch False </button>
        <br />
        <br />
        <div>
          Local React State: {value}
        </div>
        <div>
        {state.stateprop1
          ? <p> stateprop1 is true </p>
          : <p> stateprop1 is false </p>
        }
        </div>
      </div>
    )
}


export default HooksContainer;
```

Your app should look like this and you should be able to change stateprop1 from the hooks container:

![Image](https://cdn-media-1.freecodecamp.org/images/0*YhL5unbUcK0MFbQD)

You will notice one problem when we go to another component: the state is not saved. This is because even though we are using actions and reducers, the state is still local component state and not available globally. To make the state available globally we actually have to use the React Context, which we will setup next few sections.

#### Setting up Actions and the Reducer

Before we setup Context, let’s setup the Actions and Reducer we will use with it. So let’s add a second property to the HooksReducer1 called stateprop2 and set it to 0.

We will now need to set up actions and action types to work with this new piece of state.

First let’s create 2 action types for stateprop2:

```javascript

export const INC_GLOBAL_STATE = "INC_GLOBAL_STATE"

export const DEC_GLOBAL_STATE = "DEC_GLOBAL_STATE"
```

Then we can go in our actions file and create 2 action creators to handle these actions types.

```javascript


export const inc_global_state = () => {
  return {
  type: ACTION_TYPES.INC_GLOBAL_STATE
  }
}

export const dec_global_state = () => {
  return {
  type: ACTION_TYPES.DEC_GLOBAL_STATE
  }
}
```

Finally we need to setup our reducer which should look like this:

```javascript
import * as ACTION_TYPES from '../actions/action_types'

export const initialState = {
  stateprop1: false,
  stateprop2: 0
}

export const HooksReducer1 = (state = initialState, action) => {
    switch(action.type) {
      case ACTION_TYPES.SUCCESS:
        return {
          ...state,
          stateprop1: true
        }
      case ACTION_TYPES.FAILURE:
        return {
          ...state,
          stateprop1: false
        }
      case ACTION_TYPES.INC_GLOBAL_STATE:
        return {
          ...state,
          stateprop2: state.stateprop2 + 1
        }
      case ACTION_TYPES.DEC_GLOBAL_STATE:
        return {
          ...state,
          stateprop2: state.stateprop2 - 1 
        }
      default:
        return state
    }
}
```

#### React Context

Next, we have to set up the context object. Simply create another context.js file and setup it up like so:

```javascript
import React from 'react';

const Context = React.createContext({
  prop1: false
})

export default Context;
```

Note that prop1 here is irrelevant. We will be overriding this in our App.js file. We simply supplied prop1 to initialize the Context object. All the code for updating and reading our state will be done in the App.js file.

Next let’s import this context object to our App.js file. Also import HooksReducer1 and the Actions since we will use them here.

Let’s also setup the useReducer the same way as before.

```javascript
import React, { useReducer } from 'react';
import Routes from './routes';
import Context from './utils/context';
import * as ACTIONS from './store/actions/actions';
import * as HooksReducer1 from './store/reducers/hooks_reducer';



const App = () => {
  const [valueGlobal, dispatchActionsGlobal] = useReducer(HooksReducer1.HooksReducer1, HooksReducer1.initialState)

...
```

Next we need to create 2 functions to dispatch our action creators we just created. These functions will increment and decrement stateprop2.

Also we need to wrap our routes with a <Context.Provider /> component. This is what allows us to have a global state. The <Context.Provider /> component passes down all the state to the child components. Since App.js is the root component the state is passed down to every component in the app, which is what makes the state global.

The state itself is contained in a prop called “value”. All this is similar to the <Provider /> component and “store” prop seen in React-Redux.

We then need to pass in the state and action dispatches as properties to the value prop. We will need 3 properties here: one for a function to increment our state value, one for a function to decrement our state value and one to hold the actual state value.

All together your App.js file will look like this:

```javascript
import React, { useReducer } from 'react';
import Routes from './routes';
import Context from './utils/context';
import * as ACTIONS from './store/actions/actions';
import * as HooksReducer1 from './store/reducers/hooks_reducer';



const App = () => {
  const [valueGlobal, dispatchActionsGlobal] = useReducer(HooksReducer1.HooksReducer1, HooksReducer1.initialState)

    const incrementGlobalValue = () => {
      dispatchActionsGlobal(ACTIONS.inc_global_state() )
    }

    const decrementGlobalValue = () => {
      dispatchActionsGlobal(ACTIONS.dec_global_state() )
    }

    return(
      <div>
        React
        <Context.Provider
                  value={{
                    valueGlobalState: valueGlobal,
                    addGlobalValue: () => incrementGlobalValue(),
                    decGlobalValue: () => decrementGlobalValue()
                  }}>
            <Routes />
          </Context.Provider>
      </div>
    )
}


export default App;
```

I have intentionally kept all the function and property names different so it will be easier to see where everything is coming from when we use Context in the child component.

So now, all these properties defined in the value prop can be accessed by all the child components, and we therefore have a global state!

#### Using Context in a child component with the useContext() hook.

Let’s go back to our hooks container and use these functions and state we just setup.

To use the Context in our hooks container, we first need to import it and pass the entire Context object into the useContext hooks. Like so:

```javascript

...

import Context from '../utils/context';


const HooksContainer = () => {
  const context = useContext(Context)
  
...
```

Next we can directly access the properties we set in the value prop directly through the context variable.

```javascript
...    

<button onClick={() => context.addGlobalValue()}> Add Global Value </button>
<button onClick={() => context.decGlobalValue()}> Dec Global Value </button>

...
```

Remember addGlobalValue() is the name of the _property_ we supplied to the value prop in App.js. It is not the name of the function for dispatching actions or the name of the function we set in the useReducer() hook in App.js.

Accessing the state value through Context is done in the following way:

```javascript
...

<p>Global Value: {context.valueGlobalState.stateprop2}</p>

...
```

And similar to dispatching actions, the valueGlobalState is the property name supplied to the value prop. And we have to access stateprop2 with dot notation from the valueGlobalState property, since valueGlobalState contains the entire intialState from HooksReducer1, including stateprop1.

And if you test now you will see that the state updates and persists even after you go to another component, allowing you replicate Redux functionality and have a global state.

You can use this pattern to essentially scale this up for all your Redux code.

**final code:**

[**iqbal125/react-hooks-basic**](https://github.com/iqbal125/react-hooks-basic)  
[_Contribute to iqbal125/react-hooks-basic development by creating an account on GitHub._github.com](https://github.com/iqbal125/react-hooks-basic)

#### Summary

So here is a conceptual summary of how to do it (requires basic React hooks knowledge ):

Actions do not need to be changed at all. Reducers do not need to be changed either. Simply export both the initial state and the reducer instead of just the reducer. Do not use “export default” at the bottom of the reducer file.

Import the reducer and its initial state to the root App.js file. Call the useReducer() hook in the root App.js file and save it in a variable. Similar to the useState hook, the first element in the array destructuring is the state value and the second element is the function to change the state. Then Pass in both the reducer and initialState you imported to the useReducer() hook. Import as many reducers as you want and pass each of them into a separate useReducer() Hook.

Import actions to App.js as normal. Dispatching actions is also exactly the same. Instead of using the mapDispatchToProps() function you will dispatch the actions from the change state function (second element in array destructuring) from the useReducer() hook call.

Setup and initialize the React.CreateContext() function in a another file and import it to App.js. Then Wrap your <Routes /> with <Context.Provider>. You will generally need 3 properties for each piece of state for the value prop in the provider. 1 property to set the state to a new value, 1 to pass in the actual state, and 1 to set the state back to default.

Then to use the state in the components, you first import the Context Object from context.js and then just pass it in to the useContext() hook and save this in a variable called “context” or whatever you like. Then to access the state property, just do the variable name “context” “.” then the name of property set in the value prop, followed by the name of the property set in the initialState of the reducer. To dispatch actions just do “context” “.” then call the property name.

Once this is done your context state is available globally and will work with your existing React Redux code.

For a 100% Free Video version of this tutorial and more in-dept React Hooks content please see my Udemy course or Youtube playlist:

[https://www.udemy.com/react-hooks-with-react-redux-migration](https://www.udemy.com/react-hooks-with-react-redux-migration)

[https://www.youtube.com/watch?v=l8ODM-KoDpA&list=PLMc67XEAt-ywplHhDpoj5vakceZNr8S0B](https://www.youtube.com/watch?v=l8ODM-KoDpA&list=PLMc67XEAt-ywplHhDpoj5vakceZNr8S0B)

