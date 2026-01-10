---
title: How to build a React Hooks front-end app with routing and authentication
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-09-30T20:10:37.000Z'
originalURL: https://freecodecamp.org/news/build-a-react-hooks-front-end-app-with-routing-and-authentication
coverImage: https://www.freecodecamp.org/news/content/images/2019/09/photo-1551373802-aec2b9a165aa.jpg
tags:
- name: react hooks
  slug: react-hooks
seo_title: null
seo_desc: "By Mohammad Iqbal\nIn this tutorial, we will go over how to build a complete\
  \ front end app with routing and authentication. \nI have structured this tutorial\
  \ and project as basically a boilerplate project with basic routing and auth that\
  \ can be used as..."
---

By Mohammad Iqbal

In this tutorial, we will go over how to build a complete front end app with routing and authentication. 

I have structured this tutorial and project as basically a boilerplate project with basic routing and auth that can be used as a starter project. 

If you just want the boiler plate code without the explanations here it is:  
[https://github.com/iqbal125/react-hooks-routing-auth-starter](https://github.com/iqbal125/react-hooks-routing-auth-starter)

I will use Auth0 for authentication, but this setup will work with any other token-based authentication system as well.  
  
You can watch a fullstack video version of this tutorial here  
[https://www.youtube.com/playlist?list=PLMc67XEAt-yzxRboCFHza4SBOxNr7hDD5](https://www.youtube.com/playlist?list=PLMc67XEAt-yzxRboCFHza4SBOxNr7hDD5)

> Connect with me on Twitter for more updates on future tutorials: [https://twitter.com/iqbal125sf](https://twitter.com/iqbal125sf)

### Table of Contents

1. Project Structure
2. useReducer vs useState for Global Context state
3. Global State with Context
4. Authentication and authcheck
5. React Hooks Components
6. Routing
7. App.js

## Project Structure

I will first go over the structure of our app. Our app can be broken down into 4 parts: 

* React hooks functional components
* Reducers and Actions 
* Utility files 
* Main files

We will also need 4  libraries to build our app

 `npm install auth0-js react-router react-router-dom history`

### Directory Structure:

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-148.png)



### React Hooks functional components

Here we have our React Hooks functional components. We have a fairly simple setup and we will not be using any React Class components in this app.

**callback.js:** will be used as the component that Auth0 will redirect to after the user authenticates.

**header.js:** will contain the links to the components and a login or logout button based on the user authentication state.

**home.js:** will simply display the text of home.

**hook1.js:** will contain all three ways to update state with React hooks, `useState`, `useReducer` and `useContext`. Having all three ways to update the state in one component will make it easier for you to pick apart the differences between each.

**hooks_form1.js:** Will have a form that has all three ways to update state with `useState`, `useReducer` and `useContext`.

**privatecomponent.js:** A component that is only accessible by authenticated users.

**profile.js:** A user dashboard that displays user profile data.

### Reducers and Actions files

**action_types.js:** Will hold all the string actions types in variables. This will allow easy modifying of your action types since you will only have to change them here instead having to track down where ever you used the action in your code.

**actions.js:** Will hold the actual actions that are going to be used in the reducer to update the state.

**auth_reducer.js:** Will hold the reducer to read and update state properties related authentication.

**form_reducer.js:** Will hold the reducer to read and update state properties related to our form.

**plain_reducer.js:** Will serve as a boilerplate reducer.

### Utility Files

We will also need 4 utility files to help setup our app.

**context.js:** Will hold the Context object and will be imported to every component that uses the useContext() hook.

**auth.js:** This will be the only class in the app. Note that this isn’t a React class component, but instead a vanilla javascript class. I tried to setup this file as an arrow function but it did not work well. This file is best setup as a class. This file will hold all of our authentication associated functions and variables.

**history.js:** Will hold the history object which we will use for navigation.

**authcheck.js:** Will be used to update the authentication state of the user and retrieve the user profile data and save it to the global state.

### Main Files

These are the main files and will sit at the **root /src directory**. I put all the business logic for reading and updating the global state in one file, the `context_state_config.js`. My reason for doing so is follows.

Having all the complexity in one file actually makes your app simpler and easier to debug since it's easy to track down where to make the changes and fixes. 

Having many slightly complex components in my experience will actually make your app harder to debug and change. So for this reason I put all the global state code in this one file. 

Also in the `context_state_config.js` the `<Routes />` component will be wrapped by the `<Context.Provider />`. This will allow the ability to read and update state to be passed down through the `value` prop to all the components, creating a global state.

**context_state_config.js:** This will hold all the logic for reading and updating the global state with the `useReducer` hook and `context`. 

**routes.js:** Will contain all our routing logic and will have silent authentication here as well.

**App.js:** Our root component, we will simply import and display our `context_state_config.js` component.

**index.js:** Our root file, will just render App.js here.

## useRedux vs useState for Global Context state

To manage global state we will be using **Reducers and Actions**. Using Reducers and Actions along with the `useReducer()` hook and **Context** will allow us to achieve **Redux** like functionality without actually using Redux.

It is possible  to manage our global state with the `useState` hook and **Context**, but using `useReducer` makes managing global state much more organized. The `useState` hook is far better at handling local component state. 

Having related properties of state and all the update state functions in the same `useReducer` hook makes things very simple and compartmentalized compared to using the `useState`  hook which can be much more decentralized.  

**Dispatching actions** also makes the data flow easier to follow compared to using the `setState` function from `useState` since each action will describe exactly how the state will be changed.

We also dont need to use the combine reducer function or combine our reducers in anyway. Each reducer will be passed into its own useReducer hook.

## Setting up the Global State with Context

We can begin by setting up the global state, which in my opinion makes it much easier to build the React Components. 

If you already setup the global state you can build out the component in a very straightforward way instead having to go back and forth between setting up the component and then setting up its state along with it. 

To setup the global state we will need to create our **actions, reducers and context.**

Let’s start with our actions types:

```javascript

//action_types.js

export const SUCCESS = "SUCCESS"

export const FAILURE = "FAILURE"

export const LOGIN_SUCCESS = "LOGIN_SUCCESS"

export const LOGIN_FAILURE = "LOGIN_FAILURE"

export const ADD_PROFILE = "ADD_PROFILE"

export const REMOVE_PROFILE = "REMOVE_PROFILE"

export const USER_INPUT_CHANGE = "USER_INPUT_CHANGE"

export const USER_INPUT_SUBMIT = "USER_INPUT_SUBMIT"

```

**SUCCESS** and **FAILURE:** Will be used as our boiler plate actions.

**LOGIN_SUCCESS** and **LOGIN_FAILURE**: Used to update authentication state of the user. LOGIN_SUCCESS and LOGOUT_SUCCESS will also work here but I like the dichotomy of success and failure.

**ADD_PROFILE** and **REMOVE_PROFILE:** Used to save the profile data from Auth0 to the global state.

**USER_INPUT_CHANGE** and **USER_INPUT_SUBMIT:** Used to track the changes and submit of the user submitted text of the form.

### Actions:

```javascript
//actions.js

import * as ACTION_TYPES from './action_types'

export const SUCCESS = {
  type: ACTION_TYPES.SUCCESS
}

export const FAILURE = {
  type: ACTION_TYPES.FAILURE
}


export const success = () => {
  return {
    type: ACTION_TYPES.SUCCESS
  }
}

export const failure = () => {
  return {
    type: ACTION_TYPES.FAILURE
  }
}



export const login_success = () => {
  return {
    type: ACTION_TYPES.LOGIN_SUCCESS
  }
}

export const login_failure = () => {
  return {
    type: ACTION_TYPES.LOGIN_FAILURE
  }
}


export const add_profile = (profile) => {
  return {
    type: ACTION_TYPES.ADD_PROFILE,
    payload: profile
  }
}

export const remove_profile = () => {
  return {
    type: ACTION_TYPES.REMOVE_PROFILE
  }
}

export const user_input_change = (text) => {
  return {
    type: ACTION_TYPES.USER_INPUT_CHANGE,
    payload: text
  }
}

export const user_input_submit = (text) => {
  return {
    type: ACTION_TYPES.USER_INPUT_SUBMIT,
    payload: text
  }
}

```

To keep things simple I have made all the actions into action creators instead of having some as actions and some as action creators. 

The first 2 variables `SUCCESS` and `FAILURE` are regular actions. 

### Auth Reducer:

```javascript
//auth_reducer.js

import * as ACTION_TYPES from '../actions/action_types'

export const initialState = {
  is_authenticated: false,
  profile: null
}

export const AuthReducer = (state = initialState, action) => {
    switch(action.type) {
      case ACTION_TYPES.LOGIN_SUCCESS:
        return {
          ...state,
          is_authenticated: true
        }
      case ACTION_TYPES.LOGIN_FAILURE:
        return {
          ...state,
          is_authenticated: false
        }
      case ACTION_TYPES.ADD_PROFILE:
        return {
          ...state,
          profile: action.payload
        }
      case ACTION_TYPES.REMOVE_PROFILE:
        return {
          ...state,
          profile: null
        }
      default:
        return state
    }
}

```

Here we have our `auth_reducer.js` that will hold our state properties and associated actions for **user authentication status** and **user profile data.**

Important to note that we are exporting both the reducer and initial state instead of exporting default only the reducer like we do in React Redux.

### form_reducer:

```javascript
//form_reducer.js

import * as ACTION_TYPES from '../actions/action_types'


export const initialState = {
  user_textChange: '',
  user_textSubmit: ''
}


export const FormReducer = (state, action) => {
    switch(action.type) {
      case ACTION_TYPES.USER_INPUT_CHANGE:
        return {
          ...state,
          user_textChange: action.payload
        }
      case ACTION_TYPES.USER_INPUT_SUBMIT:
        return {
          ...state,
          user_textSubmit: action.payload
        }
      default:
        throw new Error();
    }
}

```

Here we have 2 properties for a form. Our first property tracks changes to the input element and our second property adds the submitted form to the global state.

### plain_reducer: 

```javascript
//plain_reducer.js


import * as ACTION_TYPES from '../actions/action_types'

export const initialState = {
  stateprop1: false,
  stateprop2: false
}

export const Reducer1 = (state = initialState, action) => {
    switch(action.type) {
      case ACTION_TYPES.SUCCESS:
        return {
          ...state,
          stateprop1: true,
          stateprop2: true
        }
      case ACTION_TYPES.FAILURE:
        return {
          ...state,
          stateprop1: false,
          stateprop2: false
        }
      default:
        throw new Error();
    }
}
```

Like our SUCCESS and FAILURE actions, this reducer will serve as a boilerplate if we want to create new reducers.

### Setting up the Context Object

We have to now initialize our Context object. We can do this in a `context.js` file in the **utils** directory.

```javascript
import React from 'react';

const Context = React.createContext()

export default Context;

```

This is all we have to do to initialize our Context variable. We can now use it by importing it to our `context_state_config.js` file.

## Global state with Context

```jsx
import React, { useReducer } from 'react';
import Context from './utils/context';
import * as ACTIONS from './store/actions/actions';

import * as Reducer1 from './store/reducers/plain_reducer';
import * as AuthReducer from './store/reducers/auth_reducer';
import * as FormReducer from './store/reducers/form_reducer';
import Routes from './routes';

import Auth from './utils/auth';


const auth = new Auth()


const ContextState = () => {
    /*
        Plain Reducer
    */
    const [stateReducer1, dispatchReducer1] = useReducer(Reducer1.Reducer1,
                                                         Reducer1.initialState)


    const handleDispatchTrue = () => {
      //    dispatchReducer1(type: "SUCCESS")
      //    dispatchReducer1(ACTIONS.SUCCESS)
      dispatchReducer1(ACTIONS.success())
    }

    const handleDispatchFalse = () => {
      //     dispatchReducer1(type: "FAILURE")
      //    dispatchReducer1(ACTIONS.FAILURE)
      dispatchReducer1(ACTIONS.failure())
    }

    /*
      Auth Reducer
    */
    const [stateAuthReducer, dispatchAuthReducer] =                      useReducer(AuthReducer.AuthReducer,
                                                           AuthReducer.initialState)


    const handleLogin = () => {
      dispatchAuthReducer(ACTIONS.login_success())
    }

    const handleLogout = () => {
      dispatchAuthReducer(ACTIONS.login_failure())
    }

    const handleAddProfile = (profile) => {
      dispatchAuthReducer(ACTIONS.add_profile(profile))
    }

    const handleRemoveProfile = () => {
      dispatchAuthReducer(ACTIONS.remove_profile())
    }



    /*
      Form Reducer
    */

        const [stateFormReducer, dispatchFormReducer] = useReducer(FormReducer.FormReducer, FormReducer.initialState)


    const handleFormChange = (event) => {
      dispatchFormReducer(ACTIONS.user_input_change(event.target.value))
    };

    const handleFormSubmit = (event) => {
      event.preventDefault();
      event.persist();             dispatchFormReducer(ACTIONS.user_input_submit(event.target.useContext.value))
    };

    //Handle authentication from callback
    const handleAuthentication = (props) => {
      if(props.location.hash) {
        auth.handleAuth()
      }
    }



    return(
      <div>
      <Context.Provider
          value={{
            //Reducer1
            stateProp1: stateReducer1.stateprop1,
            stateProp2: stateReducer1.stateprop2,
            dispatchContextTrue: () => handleDispatchTrue(),
            dispatchContextFalse: () => handleDispatchFalse(),

            //Form Reducer
            useContextChangeState: stateFormReducer.user_textChange,
            useContextSubmitState: stateFormReducer.user_textSubmit,
            useContextSubmit: (event) => handleFormSubmit(event),
            useContextChange: (event) => handleFormChange(event),

            //Auth Reducer
            authState: stateAuthReducer.is_authenticated,
            profileState:  stateAuthReducer.profile,
            handleUserLogin: () => handleLogin(),
            handleUserLogout: () => handleLogout(),
            handleUserAddProfile: (profile) => handleAddProfile(profile),
            handleUserRemoveProfile: () => handleRemoveProfile(),

            //Handle auth
            handleAuth: (props) => handleAuthentication(props),
            authObj: auth
          }}>
          <Routes />
      </Context.Provider>
      </div>
    )
}


export default ContextState;
```

> * Note you probably dont want to have so many variables and functions in context in a real app, this is just for demonstration purposes. Simply remove the properties you don't need. 

> **Note: You can also use object destructuring on the properties inside the value prop to make the code a little cleaner. Ex:  `{ handlelogin }` instead of `handleUserLogin: () => handleLogin()`. But I have kept them separate so it will be easier to see how context properties are accessed in child components for people not familiar with destructuring. 

### Importing reducers and useReducer()

I will explain how this works using Reducer1 as the example but this applies to the other reducers as well. 

We first start at the very top by importing all our actions and reducers. We then pass in our `Reducer1` and its initial state to the `useReducer()` hook. We use the syntax `import * as Reducer1` because we want to import both the `Reducer1` and the `initialState`. Then we use the syntax `Reducer1.Reducer1` to access `Reducer1` and the `intialState` can be accessed using `Reducer1.initailState`. 

After that we save the the result of the `useReducer()` hook using array destructuring.

In the example above, `stateReducer1` is how we access the state properties we defined in the `intialState` of `Reducer1`.

`dispatchReducer1` is our dispatch function that allows us to update the state with actions.

### Reducer naming scheme

As you can probably tell, my preferred naming scheme are the words “state” and “dispatch” followed by the name of their respective reducer. 

I found this to be the most effective naming scheme because it has no ambiguity about which state and dispatch function belongs to which reducer, which is important because we are not combining reducers.

### Actions

Our actions are coming from the same actions file we setup in the last section. We import them all here and can access each action with the syntax ACTIONS.name_of_action(). 

This is what we pass into our `dispatch` function, which tells our reducer how to update the state.  

After our `useReducer()` hook call we have our `handleDispatchTrue()` and `handleDispatchFalse()` functions which dispatch our `SUCCESS` and `FAILURE` actions to change the our `stateprop1` and `stateprop2` from false to true and vice versa.

You can pass in the dispatch functions directly into the “value” prop but having them in a function right under their respective `useReducer` hook makes the code more organized and readable.

I have also left 2 other ways of dispatching actions. All three ways of dispatching actions are doing the same thing, dispatching a javascript object with a type property that has a value of the string “SUCCESS”.

### AuthReducer

Next we have our `AuthReducer`. We have set this up similar to the plain reducer. We update our user authentication state if they are logged in or not and also add and remove their user profile data from the global state. Remember to pass in the profile parameter to the action creator.

### FormReducer

After this we have our `FormReducer`, which will also be setup similar to the previous reducers.

Since these actions are going to be used with a form we need to pass in the `event` keyword as a parameter to both our functions. To access the text our user enters, we need to use the syntax `event.target.value`. This is part of vanilla javascript and the standard way to access form data. 

Our `handleFormSubmit()` function is a little bit different. First we have to use the `event.preventDefault()` function to prevent the page from reloading.

Then we use the `event.persist()` function. Since we are using Context and this data is coming from a child component, we have to use this function for the form to function properly. Then to access the user submitted text we use the syntax `event.target.useContext.value`

"useContext" is not referring to the hook, it is the user defined `id` property supplied to the form input element. I decided to name the id “useContext” because the component has 2 other forms as well and they use the "useState" and "useReducer" hooks to save the state and therefore have the id of “useState” and “useReducer”.

### Context Provider

After setting up the `useReducer` hooks we have our `<Context.Provider />` component in the JSX. We now pass in all the functions and state values we just defined to the `value` prop.

We start with `stateprop1` and `stateprop2`. Important to note that they each have to be accessed using dot notation separately since `stateReducer1` contains the entire `initialState` object.

We also define 2 other properties, `dispatchContextTrue` and `dispatchContextFalse`, and pass in an arrow function for each that calls our `handleDispatchTrue()` and `handleDispatchFalse()` functions. It might be helpful for you to name the properties different than the function names. This helps you better see whats happening in child components.

Next we will continue building our app by setting up authentication.

## Authentication and Authcheck

Here we have our `auth.js` file which will be setup as a Javascript class. And we will be using Auth0 and the `auth0-js` library to help us with authentication.

The authentication utility file will be setup as follows: 

```javascript
import auth0 from 'auth0-js'
import history from './history';

export default class Auth {
  auth0 = new auth0.WebAuth({
    domain: 'webapp1.auth0.com',
    clientID: '',
    redirectUri: 'http://localhost:3000/callback',
    responseType: 'token id_token',
    scope: 'openid profile email'
  })

  userProfile = {}

  login = () => {
      this.auth0.authorize()
  }

  handleAuth = () => {
    this.auth0.parseHash((err, authResult) => {
      if(authResult) {
        localStorage.setItem('access_token', authResult.accessToken)
        localStorage.setItem('id_token', authResult.idToken)

        let expiresAt = JSON.stringify((authResult.expiresIn * 1000 + new Date().getTime()))
        localStorage.setItem('expiresAt', expiresAt)

        this.getProfile();
        setTimeout(() => { history.replace('/authcheck') }, 600);
      } else {
        console.log(err)
      }
    })
  }

  getAccessToken = () => {
    if(localStorage.getItem('access_token')) {
      const accessToken = localStorage.getItem('access_token')
      return accessToken
    } else {
      return null
    }
  }


  getProfile = () => {
    let accessToken = this.getAccessToken()
    if(accessToken) {
      this.auth0.client.userInfo(accessToken, (err, profile) => {
          if(profile) {
            this.userProfile = { profile }
          }
      } )
    }
  }


  logout = () => {
    localStorage.removeItem('access_token')
    localStorage.removeItem('id_token')
    localStorage.removeItem('expiresAt')
    setTimeout(() => { history.replace('/authcheck') }, 200);
  }

  isAuthenticated = () => {
    let expiresAt = JSON.parse(localStorage.getItem('expiresAt'))
    return new Date().getTime() < expiresAt
  }

}

```

`auth0`**:** This is the property we will use to initialize our Auth0 app.

`userProfile`**:** This is an empty object that will hold the user profile data we get from Auth0.

`login`: This brings up the Auth0 login widget, allowing the user to login with the given `.authorize()` function.  

`handleAuth`: This function saves the id and access tokens we get from Auth0 to the local browser storage. This function also sets the token expires time.

`getAccessToken`**:**  Get the access token from local storage

`getProfile`: Parse the access token to extract the user profile data

`logout`**:** Logs out the user by removing the tokens from local storage

`isAuthenticated`**:** makes sure the user is logged in by comparing the expires time to the current time.

Now we can initialize this auth object and add authentication to the `context_state_config.js` file.

```jsx
....


import Auth from './utils/auth';


const auth = new Auth()


const ContextState = () => {

....


//Handle authentication from callback
    const handleAuthentication = (props) => {
      if(props.location.hash) {
        auth.handleAuth()
      }
    }

....

        //Handle auth
        handleAuth: (props) => handleAuthentication(props),
        authObj: auth
        }}>
       <Routes />
     </Context.Provider>

....

```

`new Auth ()` is how we initialize our class then save it in the `auth` variable. 

Next we create a `handleAuthentication()` function. If `props.location.hash` is true then we call the `auth.handleAuth()` function we just setup in the Auth class. `props.location.hash` is a given react-router functionality that checks if there is any value in the URL hash fragment. 

If Auth0 successfully authenticates a user, the access and id tokens will be included after a hash in the URL, making `props.location.hash` true, which calls our `handleAuth()` function in the Auth class.

In the `<Context.Provider />`  we have 2 properties, `handleAuth` which calls our `handleAuthentication()` function and `authObj` which we use to pass down our entire Auth class and allow all components to access our authentication functions and variables.

Here is our `authcheck.js` utility component:

```jsx
import React, { useEffect, useContext } from 'react';
import history from './history';
import Context from './context';
import * as ACTIONS from '../store/actions/actions';



const AuthCheck = () => {
  const context = useContext(Context)

  useEffect(() => {
    if(context.authObj.isAuthenticated()) {
      context.handleUserLogin()
      context.handleUserAddProfile(context.authObj.userProfile)
      history.replace('/')
    }
    else {
      context.handleUserLogout()
      context.handleUserRemoveProfile()
      history.replace('/')
      }
    }, [])

    return(
        <div>
        </div>
    )}




export default AuthCheck;

```

This component is essentially how we update the authentication state using the `useEffect()` hook. 

This component will be rendered every time a user logs in and out. Having one component render after every log in and log out will save us from having to handle and update the context authentication state in every component.

In our `AuthCheck` component we first start by setting up the `useContext()` hook. Then we define a conditional statement to check if the `isAuthenticated()` function that we setup in the Auth class returns true, indicating the auth tokens in local storage haven't expired and the user is still authenticated. 

And we access that function with the syntax `context.authObj.isAuthenticated`. 

And we can do this because we passed the entire `Auth` class down as a property called `authObj` to the `value` prop in Context. 

If `isAuthentciated()` is true we call our properties to change our **login state** to true and save the **user profile data** to the global state.  

If a user logs out, we do the opposite. 

We are returning an empty div since we are just updating the state and dont need to show anything in the UI. A loading screen would be good here but that’s for another tutorial.

But this is it, we are done setting up our global state and authentication system, we can now set up our React Hooks Components.

## React Hooks Components

First we’ll start with our **callback.js** component

```jsx
import React from 'react'

const Callback = props => (
    <div>
      Callback
    </div>
);

export default Callback;

```

This component is what the user is redirected to after logging in with Auth0. From here the user is redirected to the authcheck page then the home page

### Header.js

```jsx
import React, { useContext } from 'react';
import { Link } from 'react-router-dom';
import Context from '../utils/context';

const Header = () => {
  const context = useContext(Context)

    return(
        <div>
          <Link to='/' style={{padding: '5px'}}>
            Home
          </Link>
          <Link to='/profile' style={{padding: '5px'}}>
            Profile
          </Link>
          <Link to='/hooksform' style={{padding: '5px'}}>
            Hooks Form
          </Link>
          <Link to='/hookscontainer' style={{padding: '5px'}}>
            Hooks Container
          </Link>
          <Link to='/privateroute' style={{padding: '5px'}}>
            Private Route
          </Link>
          {!context.authState
            ? <button onClick={() => context.authObj.login()}>Login</button>
            : <button onClick={() => context.authObj.logout()}>Logout</button>
          }
        </div>
  )};


export default Header;
```

Here we have links to all our components. We also have a ternary expression that displays either a login or logout button depending on whether the user is authenticated or not.

### home.js

```jsx
import React from 'react'

const Home = props => (
    <div>
      Home
    </div>
);

export default Home;

```

a simple home.js component

### hooks1.js

```jsx
import React, { useContext, useState, useEffect, useReducer } from 'react';
import * as ACTIONS from '../store/actions/actions';
import * as Reducer1 from '../store/reducers/plain_reducer';
import Context from '../utils/context';


const HooksContainer1 = () => {
  const context = useContext(Context)

  const [value, setValue] = useState(0)

  const [useEffectValue, setUseEffectValue] = useState(null)

  const [state, dispatch] = useReducer(Reducer1.Reducer1, Reducer1.initialState)

  useEffect(() => {
      setTimeout(() => setUseEffectValue("useEffect worked"), 3000 );
  }, [value])

  const incrementValue = () => {
    setValue(value + 1 )
  }

  const decrementValue = () => {
    setValue(value - 1 )
  }

  const handleuseEffectValue = () => {
    setUseEffectValue("some string")
  }

  const handleDispatchTrue = () => {
    //    dispatch2(type: "SUCCESS")
    //    dispatch2(ACTIONS.SUCCESS)
    dispatch(ACTIONS.success())
  }

  const handleDispatchFalse = () => {
    //     dispatch2(type: "FAILURE")
    //    dispatch2(ACTIONS.FAILURE)
    dispatch(ACTIONS.failure())
  }

  return (
    <div>
      <div>
      <button onClick={() => handleuseEffectValue()}> Handle Value  </button>
      <button onClick={() => handleDispatchTrue()}>Dispatch True </button>
      <button onClick={() => handleDispatchFalse()}>Dispatch False </button>
      <button onClick={() => context.dispatchContextTrue()}>Dispatch Context True </button>
      <button onClick={() => context.dispatchContextFalse()}>Dispatch Context False </button>
      <button onClick={() => incrementValue()}> Add Local Value </button>
      <button onClick={() => decrementValue()}> Dec Local Value </button>
      <br />
      <br />
      {context.useContextSubmitState
        ? <h3> {context.useContextSubmitState} </h3>
        : <h3> No User Text </h3>
      }
      <br />
      {state.stateprop1
        ? <p> stateprop1 is true </p>
        : <p> stateprop1 is false </p>
      }
      <br />
      {context.stateProp2
        ? <p> stateprop2 is true </p>
        : <p> stateprop2 is false </p>
      }
      <br />
      {useEffectValue
        ? <p> { useEffectValue }</p>
        : <p> No value </p>
      }
      <br />
      <p>Local Value: {value}</p>
      <br />
      <br />
      </div>
    </div>
  )
}

export default HooksContainer1;
```

I created this component as a boilerplate to have all the ways to read and update state in one component. This makes it much easier to see the syntax differences.

**`incrementValue`** and **`decrementValue`** is how we update the local state with the `useState()` hook.

**`handleuseEffectValue`** is how we update the `useEffectValue` property of local state.

**`handleDispatchTrue`** and **`handleDispatchFalse`** is how we dispatch our actions to change our `stateprop1` in `Reducer1` from true to false, and vice versa. Note that this is still local state even though we are using reducers and actions. 

**`handleContextDispatchTrue`** and **`handleContextDispatchFalse`** is how we update our global state using the same actions and reducer as the `handleDispatchTrue` and `handleDispatchFalse` functions.

In our JSX we also see that each function has its own button.

**`context.useContextSubmitState`** is how we display text from a form that saves values to the global state, which we will see next

**`state.stateprop1`** is the `stateprop1` property from the `Reducer1` `initialState` that we set up a while ago and `state` is the user defined keyword from the `useRedcuer` hook at the top. The entire `initialState` is contained in `state`. 

**`context.stateProp2`** is the `stateprop2` value we are getting from our context global state.

**`useEffectValue`** is the local state from the `useState` hook call.

### hooks_form1.js

Here we have our `hooks1_form.js` that shows how to save the state from a form using the `useReducer`, `useState` and `useContext` hooks.

```jsx
import React, { useContext, useState, useReducer } from 'react';
import * as ACTIONS from '../store/actions/actions';
import * as FormReducer from '../store/reducers/form_reducer';
import Context from '../utils/context';


const HooksForm1 = () => {
  const context = useContext(Context)

  const [valueChange, setValueChange] = useState('')
  const [valueSubmit, setValueSubmit] = useState('')

  const [state, dispatch] = useReducer(FormReducer.FormReducer,
                                       FormReducer.initialState)


  const handleuseStateChange = (event) => (
    setValueChange(event.target.value)
  );

  const handleuseStateSubmit = (event) => {
    event.preventDefault();
    setValueSubmit(event.target.useState.value)
  };

  const handleuseReducerChange = (event) => (
    dispatch(ACTIONS.user_input_change(event.target.value))
  );

  const handleuseReducerSubmit = (event) => {
    event.preventDefault();
    dispatch(ACTIONS.user_input_submit(event.target.useReducer.value))
  };


    return (
      <div>
        <form onSubmit={handleuseStateSubmit}>
          <label> React useState: </label>
          <input id="useState" onChange={handleuseStateChange} type="text" />
          <button type="submit"> Submit </button>
        </form>
        <br />
        <form onSubmit={handleuseReducerSubmit}>
          <label> React useReducer: </label>
          <input id="useReducer" onChange={handleuseReducerChange} type="text" />
          <button type="submit"> Submit </button>
        </form>
        <br />
        <form onSubmit={context.useContextSubmit}>
          <label> React useContext: </label>
          <input id="useContext" onChange={context.useContextChange} type="text" />
          <button type="submit"> Submit </button>
        </form>
        <br />

        <h3>React useState:</h3>
        <p>Change: {valueChange}</p>
        <p>Submit: {valueSubmit}</p>
        
        <h3>React useReducer:</h3>
        <p>Change: {state.user_textChange}</p>
        <p>Submit: {state.user_textSubmit}</p>
        <br />
        <h3>React useContext:</h3>
        <p>Change: {context.useContextChangeState}</p>
        <p>Submit: {context.useContextSubmitState}</p>
        <br />
        <br />
      </div>
    )
}


export default HooksForm1;

```

This form shows the three ways to update state and follows the same exact methodology as we saw in the previous component.  

### privatecomponent.js

```jsx
import React from 'react'

const PrivateComponent = props => (
    <div>
      Private Component
    </div>
);

export default PrivateComponent;
```

This privatecomponent will be used in a private route and be only accessible by authenticated users.

### profile.js

```jsx
import React, { useContext } from 'react';
import Context from '../utils/context';


const Profile = () => {
  const context = useContext(Context)


  const RenderProfile = (props) => {
    return(
      <div>
        <h1>{props.profile.profile.nickname}</h1>
        <br />
        <img src={props.profile.profile.picture} alt="" />
        <br />
        <h4> {props.profile.profile.email}</h4>
        <br />
        <h5> {props.profile.profile.name} </h5>
        <br />
        <h6> Email Verified: </h6>
        {props.profile.profile.email_verified ? <p>Yes</p> : <p>No</p> }
        <br />
      </div>
     )
   }


    return(
      <div>
        <RenderProfile profile={context.authObj.userProfile} />
      </div>
  )}



export default (Profile);
```

Here we display the user profile data. The user profile data is available from Auth0 and we do not have to set it up manually. We are getting this user profile data from our `authObj` that we passed down through `context`.

## Routing

Before we can setup our routing we need to first setup the `history.js` file which is luckily very easy to do.

```javascript
import { createBrowserHistory } from 'history'

export default createBrowserHistory()

```

Finally we can setup our Routing:

```jsx
import React, { useContext, useEffect } from 'react';
import { Router, Route, Switch, Redirect } from 'react-router';
import history from './utils/history';
import Context from './utils/context';
import AuthCheck from './utils/authcheck';

import Home from './hooks/home';
import Header from './hooks/header';
import HooksContainer1 from './hooks/hook1';
import Callback from './hooks/callback';
import HooksForm from './hooks/hooks_form1';
import PrivateComponent from './hooks/privatecomponent';
import Profile from './hooks/profile';



const PrivateRoute = ({component: Component, auth }) => (
  <Route render={props => auth === true
    ? <Component auth={auth} {...props} />
    : <Redirect to={{pathname:'/'}} />
  }
  />
)



const Routes = () => {
    const context = useContext(Context)


      return(
        <div>
          <Router history={history} >
          <Header />
          <br />
          <br />
          <div>
            <Switch>
              <Route exact path='/' component={Home} />
              <Route path='/hooksform' component={HooksForm} />
              <Route path='/profile' component={Profile} />
              <Route path='/hookscontainer' component={HooksContainer1} />
              <Route path='/authcheck' component={AuthCheck} />

              <PrivateRoute path='/privateroute'
                            auth={context.authState}
                            component={PrivateComponent} />
              <PrivateRoute path="/profile"
                            auth={context.authState}
                            component={Profile} />
              <Route path='/callback'
					 render={(props) => {
                         context.handleAuth(props);                                                            return <Callback />}} />


            </Switch>
          </div>
          </Router>
        </div>
  )}

export default Routes;
```

We first start by importing all our utility files and components. And also the Router components from React Router.

We then have a `PrivateRoute` Higher Order Component that’s going to be responsible for our private routes.

A **HOC** takes in a component and returns another component. Here we are passing in a component and either returning a `<Route />` component or a `<Redirect />` component based on the user authentication state. We check for the auth state inside our our `render` prop with a ternary expression.  

Next we have our actual Router functionality. We will start with our main `<Router />` component which will wrap all of our routes and header.

We always want the header to be showing so we will of course put it outside of the `<Switch />` component. Our `<Switch />` component will then wrap all of our routes. We can define the routes and components using the `path` and `component` props of the `<Route />` component.

Our `<PrivateRoute />` component is a little bit different. We have to specify the `path` and `component` props like we did for the regular `<Route />`, but we also have to create a `auth` prop that contains the authentication state of the user. We get this value from our global context state that we went over in the authentication section, but basically this `auth` prop contains the value of the `is_authenticated` property from our `AuthReducer` from the global state.

Finally we have our `/callback` route which is setup a little bit different. Since this is the component that Auth0 redirects to, we have to call the `handleAuth()`  function here, but we also have to render the `<Callback />` component. 

We get around this by calling 2 functions in the `render` prop, which we can do by wrapping the body of the arrow function in curly brackets `{}` and separating each function with a semi-colon `;`.

Also be sure to wrap all the routes with the `<Context.Provider />`

```jsx
//context_state_config.js
...    
     <Context.Provider>
    	 <Routes />
     </Context.Provider>
      
 ...     
```

Wrapping all the routes with the `<Context.Provider />` is essentially how state gets passed down to all the components, and becomes global.

### App.js

```jsx
import React from 'react';
import ContextState from './context_state_config';

const App = () => {

    return(
      <div>
     	 <ContextState />
      </div>
    )
}

export default App;
```

Now the only thing we have left to do is import our `<ContextState />` component to our `App.js` file to finish off our app.

And we are done! Thanks for reading. 

> Connect with me on Twitter for more updates on future tutorials: [https://twitter.com/iqbal125sf](https://twitter.com/iqbal125sf)

