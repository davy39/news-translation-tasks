---
title: How to load data in React with redux-thunk, redux-saga, suspense & hooks
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-31T16:49:30.000Z'
originalURL: https://freecodecamp.org/news/loading-data-in-react-redux-thunk-redux-saga-suspense-hooks-666b21da1569
coverImage: https://cdn-media-1.freecodecamp.org/images/1*JL-AhMbl0HlP4Jr3YyaxbA.jpeg
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
seo_desc: 'By Valerii Tereshchenko

  Introduction

  React is a JavaScript library for building user interfaces. Very often using React
  means using React with Redux. Redux is another JavaScript library for managing global
  state. Sadly, even with these two libraries ...'
---

By Valerii Tereshchenko

### Introduction

[React](https://reactjs.org/) is a JavaScript library for building user interfaces. Very often using React means using React with [Redux](https://redux.js.org/). [Redux](https://redux.js.org/) is another JavaScript library for managing global state. Sadly, even with these two libraries there is no one clear way how to handle asynchronous calls to the API (backend) or any other side effects.

In this article I’m trying to compare different approaches to solving this problem. Let’s define the problem first.

**_Component X is one of the many components of the web site (or mobile, or desktop application, it’s also possible). X queries and shows some data loaded from the API. X can be page or just part of the page. Important thing that X is a separate component which should be loosely coupled with the rest of the system (as much as possible). X should show loading indicator while data is retrieving and error if call fails._**

This article assumes that you already have some experience with creating React/Redux applications.

This article is going to show 4 ways of solving this problem and **compare pros and cons** of each one. **It isn’t a detailed manual on how to use thunk, saga, suspence or hooks**.

Code of these examples is available on [GitHub](https://github.com/ValeraT1982/react-data-load).

### Initial setup

#### Mock Server

For testing purposes we are going to use [json-server](https://github.com/typicode/json-server). It’s an amazing project that allows you to build fake REST APIs very fast. For our example, it looks like this.

```js
const jsonServer = require('json-server');
const server = jsonServer.create();
const router = jsonServer.router('db.json');
const middleware = jsonServer.defaults();

server.use((req, res, next) => {
   setTimeout(() => next(), 2000);
});
server.use(middleware);
server.use(router);
server.listen(4000, () => {
   console.log(`JSON Server is running...`);
});
```

Our db.json file contains test data in json format.

```json
{
 "users": [
   {
     "id": 1,
     "firstName": "John",
     "lastName": "Doe",
     "active": true,
     "posts": 10,
     "messages": 50
   },
   ...
   {
     "id": 8,
     "firstName": "Clay",
     "lastName": "Chung",
     "active": true,
     "posts": 8,
     "messages": 5
   }
 ]
}
```

After starting the server, a call to the [_http://localhost:4000/users_](http://localhost:4000/users) returns the list of the users with an imitation of delay — about 2s.

### Project and API call

Now we are ready to start coding. I assume that you already have a React project created using [create-react-app](https://github.com/facebook/create-react-app) with Redux configured and ready to use.

If you have any difficulties with it you can check out [this](https://facebook.github.io/create-react-app/) and [this](https://medium.com/backticks-tildes/setting-up-a-redux-project-with-create-react-app-e363ab2329b8).

The next step is to create a function to call the API (_api.js_):

```json
const API_BASE_ADDRESS = 'http://localhost:4000';

export default class Api {
   static getUsers() {
       const uri = API_BASE_ADDRESS + "/users";
       
       return fetch(uri, {
           method: 'GET'
       });
   }
}
```

### Redux-thunk

[Redux-thunk](https://github.com/reduxjs/redux-thunk) is a recommended middleware for basic Redux side effects logic, such as simple async logic (like a request to the API). Redux-thunk itself doesn’t do a lot. It’s just [14!!! lines](https://github.com/reduxjs/redux-thunk/blob/master/src/index.js) [of](https://github.com/reduxjs/redux-thunk/blob/master/src/index.js) [the](https://github.com/reduxjs/redux-thunk/blob/master/src/index.js) [code](https://github.com/reduxjs/redux-thunk/blob/master/src/index.js). It just adds some “syntax sugar” and nothing more.

The flowchart below helps to understand what we are going to do.

![Image](https://cdn-media-1.freecodecamp.org/images/AWinRkydsUiojdtNEqS9O7NO6xtGirYJR50Z)

Every time an action is performed, the reducer changes state accordingly. The component maps state to properties and uses these properties in the **_render()_** method to figure out what the user should see: a loading indicator, data or error message.

To make it work we need to do 5 things.

#### 1. Install thunk

```
npm install redux-thunk
```

#### 2. Add thunk middleware when configuring store (configureStore.js)

```js
import { applyMiddleware, compose, createStore } from 'redux';
import thunk from 'redux-thunk';
import rootReducer from './appReducers';

export function configureStore(initialState) {
 const middleware = [thunk];
 
 const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
 const store = createStore(rootReducer, initialState, composeEnhancers(applyMiddleware(...middleware)));
 
 return store;
}
```

In lines 12–13 we also configure [redux](https://github.com/zalmoxisus/redux-devtools-extension) [devtools](https://github.com/zalmoxisus/redux-devtools-extension). A bit later it will help to show one of the problems with this solution.

#### 3. Create actions (redux-thunk/actions.js)

```js
import Api from "../api"

export const LOAD_USERS_LOADING = 'REDUX_THUNK_LOAD_USERS_LOADING';
export const LOAD_USERS_SUCCESS = 'REDUX_THUNK_LOAD_USERS_SUCCESS';
export const LOAD_USERS_ERROR = 'REDUX_THUNK_LOAD_USERS_ERROR';

export const loadUsers = () => dispatch => {
   dispatch({ type: LOAD_USERS_LOADING });
   Api.getUsers()
       .then(response => response.json())
       .then(
           data => dispatch({ type: LOAD_USERS_SUCCESS, data }),
           error => dispatch({ type: LOAD_USERS_ERROR, error: error.message || 'Unexpected Error!!!' })
       )
};
```

It’s also recommended to have your action creators separated (it adds some additional coding), but for this simple case I think it’s acceptable to create actions “on the fly”.

#### 4. Create reducer (redux-thunk/reducer.js)

```js
import {LOAD_USERS_ERROR, LOAD_USERS_LOADING, LOAD_USERS_SUCCESS} from "./actions";

const initialState = {
   data: [],
   loading: false,
   error: ''
};

export default function reduxThunkReducer(state = initialState, action) {
   switch (action.type) {
       case LOAD_USERS_LOADING: {
           return {
               ...state,
               loading: true,
               error:''
           };
       }
       case LOAD_USERS_SUCCESS: {
           return {
               ...state,
               data: action.data,
               loading: false
           }
       }
       case LOAD_USERS_ERROR: {
           return {
               ...state,
               loading: false,
               error: action.error
           };
       }
       default: {
           return state;
       }
   }
}
```

#### 5. Create component connected to redux (redux-thunk/UsersWithReduxThunk.js)

```js
import * as React from 'react';
import { connect } from 'react-redux';
import {loadUsers} from "./actions";

class UsersWithReduxThunk extends React.Component {
   componentDidMount() {
       this.props.loadUsers();
   };
    
   render() {
       if (this.props.loading) {
           return <div>Loading</div>
       }
       
       if (this.props.error) {
           return <div style={{ color: 'red' }}>ERROR: {this.props.error}</div>
       }
    
       return (
           <table>
               <thead>
                   <tr>
                       <th>First Name</th>
                       <th>Last Name</th>
                       <th>Active?</th>
                       <th>Posts</th>
                       <th>Messages</th>
                   </tr>
               </thead>
               <tbody>
               {this.props.data.map(u =>
                   <tr key={u.id}>
                       <td>{u.firstName}</td>
                       <td>{u.lastName}</td>
                       <td>{u.active ? 'Yes' : 'No'}</td>
                       <td>{u.posts}</td>
                       <td>{u.messages}</td>
                   </tr>
               )}
               </tbody>
           </table>
       );
   }
}

const mapStateToProps = state => ({
   data: state.reduxThunk.data,
   loading: state.reduxThunk.loading,
   error: state.reduxThunk.error,
});

const mapDispatchToProps = {
   loadUsers
};

export default connect(
   mapStateToProps,
   mapDispatchToProps
)(UsersWithReduxThunk);
```

I tried to make the component as simple as possible. I understand that it looks awful :)

Loading indicator

![Image](https://cdn-media-1.freecodecamp.org/images/8QkfJzj7pl5LgP2-BgjeVPXDdf7jFmPxCXIp)

Data

![Image](https://cdn-media-1.freecodecamp.org/images/TxQRy0VYOb-Z1EwwwwdIfVHa8xYSd7443FuG)

Error

![Image](https://cdn-media-1.freecodecamp.org/images/u2AmrUXMxuxeEHJ0RRtm0Et9YpkQDbSJhZx3)

**There you have it: 3 files, 109 line of code (13(actions) + 36(reducer) + 60(component)).**

#### Pros:

* “Recommended” approach for react/redux applications.
* No additional dependencies. Almost, thunk is tiny :)
* No need to learn new things.

#### Cons:

* A lot of code in different places
* After navigation to another page, old data is still in the global state (see picture below). This data is outdated and useless information that consumes memory.
* In case of complex scenarios (multiple conditional calls in one action, etc.) code isn’t very readable

![Image](https://cdn-media-1.freecodecamp.org/images/TfXqLWBchdCUCvNjDXbfWihuWZNV2BVQaH3r)

### Redux-saga

[Redux-saga](https://github.com/redux-saga/redux-saga) is a redux middleware library designed to make handling side effects easy and readable. It leverages ES6 Generators which allows us to write asynchronous code that looks synchronous. Also, this solution is easy to test.

From a high level perspective, this solution works the same as thunk. The flowchart from the thunk example is still applicable.

To make it work we need to do 6 things.

#### 1. Install saga

```
npm install redux-saga
```

#### 2. Add saga middleware and add all sagas (configureStore.js)

```js
import { applyMiddleware, compose, createStore } from 'redux';
import createSagaMiddleware from 'redux-saga';
import rootReducer from './appReducers';
import usersSaga from "../redux-saga/sagas";

const sagaMiddleware = createSagaMiddleware();

export function configureStore(initialState) {
 const middleware = [sagaMiddleware];
    
 const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
 const store = createStore(rootReducer, initialState, composeEnhancers(applyMiddleware(...middleware)));
    
 sagaMiddleware.run(usersSaga);
    
 return store;
}
```

Sagas from line 4 will be added in step 4.

#### 3. Create action (redux-saga/actions.js)

```js
export const LOAD_USERS_LOADING = 'REDUX_SAGA_LOAD_USERS_LOADING';
export const LOAD_USERS_SUCCESS = 'REDUX_SAGA_LOAD_USERS_SUCCESS';
export const LOAD_USERS_ERROR = 'REDUX_SAGA_LOAD_USERS_ERROR';

export const loadUsers = () => dispatch => {
   dispatch({ type: LOAD_USERS_LOADING });
};
```

#### 4. Create sagas (redux-saga/sagas.js)

```js
import { put, takeEvery, takeLatest } from 'redux-saga/effects'
import {loadUsersSuccess, LOAD_USERS_ERROR, LOAD_USERS_LOADING, LOAD_USERS_SUCCESS} from "./actions";
import Api from '../api'

async function fetchAsync(func) {
   const response = await func();
    
   if (response.ok) {
       return await response.json();
   }
    
   throw new Error("Unexpected error!!!");
}

function* fetchUser() {
   try {
       const users = yield fetchAsync(Api.getUsers);
       
       yield put({type: LOAD_USERS_SUCCESS, data: users});
   } catch (e) {
       yield put({type: LOAD_USERS_ERROR, error: e.message});
   }
}

export function* usersSaga() {
   // Allows concurrent fetches of users
   yield takeEvery(LOAD_USERS_LOADING, fetchUser);
    
   // Does not allow concurrent fetches of users
   // yield takeLatest(LOAD_USERS_LOADING, fetchUser);
}

export default usersSaga;
```

Saga has quite a steep learning curve, so if you’ve never used it and have never read anything about this framework it could be difficult to understand what’s going on here. Briefly, in the **_userSaga_** function we configure saga to listen to the **LOAD_USERS_LOADING** action and trigger the **_fetchUsers_** function. The **_fetchUsers_** function calls the API. If the call succeeds, then the **LOAD_USER_SUCCESS** action is dispatched, otherwise the **LOAD_USER_ERROR** action is dispatched.

#### 5. Create reducer (redux-saga/reducer.js)

```js
import {LOAD_USERS_ERROR, LOAD_USERS_LOADING, LOAD_USERS_SUCCESS} from "./actions";

const initialState = {
   data: [],
   loading: false,
   error: ''
};

export default function reduxSagaReducer(state = initialState, action) {
   switch (action.type) {
       case LOAD_USERS_LOADING: {
           return {
               ...state,
               loading: true,
               error:''
           };
       }
       case LOAD_USERS_SUCCESS: {
           return {
               ...state,
               data: action.data,
               loading: false
           }
       }
       case LOAD_USERS_ERROR: {
           return {
               ...state,
               loading: false,
               error: action.error
           };
       }
       default: {
           return state;
       }
   }
}
```

The reducer here is absolutely the same as in the thunk example.

### 6. Create component connected to redux (redux-saga/UsersWithReduxSaga.js)

```js
import * as React from 'react';
import {connect} from 'react-redux';
import {loadUsers} from "./actions";

class UsersWithReduxSaga extends React.Component {
   componentDidMount() {
       this.props.loadUsers();
   };
    
   render() {
       if (this.props.loading) {
           return <div>Loading</div>
       }
       
       if (this.props.error) {
           return <div style={{color: 'red'}}>ERROR: {this.props.error}</div>
       }
    
       return (
           <table>
               <thead>
                   <tr>
                       <th>First Name</th>
                       <th>Last Name</th>
                       <th>Active?</th>
                       <th>Posts</th>
                       <th>Messages</th>
                   </tr>
               </thead>
               <tbody>
                   {this.props.data.map(u =>
                       <tr key={u.id}>
                           <td>{u.firstName}</td>
                           <td>{u.lastName}</td>
                           <td>{u.active ? 'Yes' : 'No'}</td>
                           <td>{u.posts}</td>
                           <td>{u.messages}</td>
                       </tr>
                   )}
               </tbody>
           </table>
       );
   }
}

const mapStateToProps = state => ({
   data: state.reduxSaga.data,
   loading: state.reduxSaga.loading,
   error: state.reduxSaga.error,
});

const mapDispatchToProps = {
   loadUsers
};

export default connect(
   mapStateToProps,
   mapDispatchToProps
)(UsersWithReduxSaga);
```

The component is also almost the same here as in the thunk example.

**So here we have 4 files, 136 line of code (7(actions) + 36(reducer) + sagas(33) + 60(component)).**

#### Pros:

* More readable code (async/await)
* Good for handling complex scenarios (multiple conditional calls in one action, action can have multiple listeners, canceling actions, etc.)
* Easy to unit test

#### Cons:

* A lot of code in different places
* After navigation to another page, old data is still in the global state. This data is outdated and useless information that consumes memory.
* Additional dependency
* A lot of concepts to learn

### Suspense

Suspense is a new feature in React 16.6.0. It allows us to defer rendering part of the component until some condition is met (for example data from the API loaded).

To make it work we need to do 4 things (it’s definitely getting better :) ).

#### 1. Create cache (suspense/cache.js)

For the cache, we are going to use a [simple-cache-provider](https://www.npmjs.com/package/simple-cache-provider) which is a basic cache provider for react applications.

```js
import {createCache} from 'simple-cache-provider';

export let cache;

function initCache() {
 cache = createCache(initCache);
}

initCache();
```

#### 2. Create Error Boundary (suspense/ErrorBoundary.js)

This is an Error Boundary to catch errors thrown by Suspense.

```js
import React from 'react';

export class ErrorBoundary extends React.Component {
 state = {};

 componentDidCatch(error) {
   this.setState({ error: error.message || "Unexpected error" });
 }

 render() {
   if (this.state.error) {
     return <div style={{ color: 'red' }}>ERROR: {this.state.error || 'Unexpected Error'}</div>;
   }

   return this.props.children;
 }
}

export default ErrorBoundary;
```

#### 3. Create Users Table (suspense/UsersTable.js)

For this example, we need to create an additional component which loads and shows data. Here we are creating a resource to get data from the API.

```js
import * as React from 'react';
import {createResource} from "simple-cache-provider";
import {cache} from "./cache";
import Api from "../api";

let UsersResource = createResource(async () => {
   const response = await Api.getUsers();
   const json = await response.json();
    
   return json;
});

class UsersTable extends React.Component {
   render() {
       let users = UsersResource.read(cache);
       
       return (
           <table>
               <thead>
               <tr>
                   <th>First Name</th>
                   <th>Last Name</th>
                   <th>Active?</th>
                   <th>Posts</th>
                   <th>Messages</th>
               </tr>
               </thead>
               <tbody>
               {users.map(u =>
                   <tr key={u.id}>
                       <td>{u.firstName}</td>
                       <td>{u.lastName}</td>
                       <td>{u.active ? 'Yes' : 'No'}</td>
                       <td>{u.posts}</td>
                       <td>{u.messages}</td>
                   </tr>
               )}
               </tbody>
           </table>
       );
   }
}

export default UsersTable;
```

#### 4. Create component (suspense/UsersWithSuspense.js)

```js
import * as React from 'react';
import UsersTable from "./UsersTable";
import ErrorBoundary from "./ErrorBoundary";

class UsersWithSuspense extends React.Component {
   render() {
       return (
           <ErrorBoundary>
               <React.Suspense fallback={<div>Loading</div>}>
                   <UsersTable/>
               </React.Suspense>
           </ErrorBoundary>
       );
   }
}

export default UsersWithSuspense;
```

**4 files, 106 line of code (9(cache) + 19(ErrorBoundary) + UsersTable(33) + 45(component)).**

**3 files, 87 line of code (9(cache) + UsersTable(33) + 45(component)) if we assume that ErrorBoundary is a reusable component.**

#### Pros:

* No redux needed. This approach can be used without redux. Component is fully independent.
* No additional dependencies ([simple-cache-provider](https://www.npmjs.com/package/simple-cache-provider) is part of React)
* Delay of showing Loading indicator by setting dellayMs property
* Fewer lines of code than in previous examples

#### Cons:

* Cache is needed even when we don’t really need caching.
* Some new concepts need to be learned (which are part of React).

### Hooks

At the time of writing this article, hooks have not officially been released yet and available only in the “next” version. Hooks are indisputably one of the most revolutionary upcoming features which can change a lot in the React world very soon. More details about hooks can be found [here](https://reactjs.org/docs/hooks-intro.html) and [here](https://reactjs.org/docs/hooks-overview.html).

To make it work for our example we need to do **one(!)** thing:

#### 1. Create and use hooks (hooks/UsersWithHooks.js)

Here we are creating 3 hooks (functions) to “hook into” React state.

```js
import React, {useState, useEffect} from 'react';
import Api from "../api";

function UsersWithHooks() {
   const [data, setData] = useState([]);
   const [loading, setLoading] = useState(true);
   const [error, setError] = useState('');
    
   useEffect(() => {
       async function fetchData() {
           try {
               const response = await Api.getUsers();
               const json = await response.json();

            setData(json);
           } catch (e) {
               setError(e.message || 'Unexpected error');
           }

           setLoading(false);
       }

       fetchData();
   }, []);
    
   if (loading) {
       return <div>Loading</div>
   }
    
   if (error) {
       return <div style={{color: 'red'}}>ERROR: {error}</div>
   }

   return (
       <table>
           <thead>
           <tr>
               <th>First Name</th>
               <th>Last Name</th>
               <th>Active?</th>
               <th>Posts</th>
               <th>Messages</th>
           </tr>
           </thead>
           <tbody>
           {data.map(u =>
               <tr key={u.id}>
                   <td>{u.firstName}</td>
                   <td>{u.lastName}</td>
                   <td>{u.active ? 'Yes' : 'No'}</td>
                   <td>{u.posts}</td>
                   <td>{u.messages}</td>
               </tr>
           )}
           </tbody>
       </table>
   );
}

export default UsersWithHooks;
```

**And that’s it — just 1 file, 56 line of code!!!**

#### Pros:

* No redux needed. This approach can be used without redux. Component is fully independent.
* No additional dependencies
* About 2 times less code than in other solutions

#### Cons:

* At first look, the code looks weird and difficult to read and understand. It will take some time to get used to hooks.
* Some new concepts need to be learned (which are part of React)
* Not officially released yet

### Conclusion

Let’s organize these metrics as a table first.

![Image](https://cdn-media-1.freecodecamp.org/images/Em2SE0unpxwElJ45-SaSNQZ15H0eGDdJQqIj)

* Redux is still a good option to manage global state (if you have it)
* Each option has pros and cons. Which approach is better depends on the project: its complexity, use cases, team knowledge, when the project is going to production, etc.
* Saga can help with complex use cases
* Suspense and Hooks are both worth considering (or at least learning) especially for new projects

That’s it — enjoy and happy coding!

