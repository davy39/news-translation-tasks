---
title: The best way to architect your Redux app
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-18T22:13:56.000Z'
originalURL: https://freecodecamp.org/news/the-best-way-to-architect-your-redux-app-ad9bd16c8e2d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*OxDtmLW8xodYnzAeLKXMqA.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: React
  slug: reactjs
- name: Redux
  slug: redux
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Lusan Das

  This article is about how to think in Redux. We’ll try to understand how we can
  utilise this wonderful library to make our application more stable, robust, and
  maintainable. It is language agnostic, however we will keep our scope to Redu...'
---

By Lusan Das

This article is about how to think in Redux. We’ll try to understand how we can utilise this wonderful library to make our application more stable, robust, and maintainable. It is language agnostic, however we will keep our scope to Redux with React.

For those who haven’t used Redux before, I will quote from the [docs](https://redux.js.org/):

> Redux is a predictable state container for JavaScript apps.

It is only a 2kb library that solves one of the biggest problems in maintaining large JavaScript apps: state management.

This article is not about Redux, as there are plenty of articles about it already. Rather, it is about how we should visualise a Redux app and use it effectively.

Let’s say we are building an e-commerce application where it has some basic pages like catalog, product details, and payment success.

Below are the wireframes of how the app would look:

![Image](https://cdn-media-1.freecodecamp.org/images/AOXLtZSHXOg-wHn2nL-exW2QXjHCQvMnBpMv)
_Catalog Page_

![Image](https://cdn-media-1.freecodecamp.org/images/9ozwPviyKCIKwKaeEAQ6m9UK5yLtdkvXFedE)
_Product Page_

![Image](https://cdn-media-1.freecodecamp.org/images/-ycevoUXMQz0Br2N3u-OxfunYLfs8ueaEx93)
_Payment Success_

So architecting in Redux means that we have to visualise the application as one entity, and each page is a sub-entity.

There are four stages to building a Redux app:

1. Visualise the state tree
2. Design your reducers
3. Implement Actions
4. Implement Presentation

### Step 1: Visualise state tree

From the wireframes above, let’s design our state tree.

![Image](https://cdn-media-1.freecodecamp.org/images/PxbfMiRBMWkyTYHpwT3hfv8sLRSCL-XeW2hb)
_Application state tree_

This is the most important step. After we are done visualising our state tree, implementing Redux techniques becomes really easy! Dotted circles are states that will be shared by the application, solid circles are page-specific states.

### Step 2: Design your reducers

In case you are wondering what exactly a reducer is, I will quote directly from the docs:

> **Reducers** specify how the application’s state changes in response to [actions](https://redux.js.org/basics/actions) sent to the store. Remember that actions only describe _what happened_, but don’t describe how the application’s state changes.

Each of the states that are important can have their own reducers. Later, we can combine them in one root reducer which will eventually define the store (the single source of truth of the application). This is where the real power comes in: you have total control over your states and their behaviour. Nothing goes unwatched by the store. The silent observer keeps watch.

![Image](https://cdn-media-1.freecodecamp.org/images/0J1lSXo1yvDLVPTyogpfNw7c1YONwwO0iqAQ)
_The store keeping watch_

Let’s check out an example of how to design a reducer with the help of the application state tree that we designed above.

```javascript
// Root Reducer
const rootReducer = combineReducer({  
    header: headerReducer,  
    login: loginReducer,  
    footer: footerReducer,  
    common: commonReducer,  
    product: productReducer,  
    catalog: catalogReducer,  
    payment: paymentReducer
});
```

The root reducer says it all. It contains everything the store needs to know about the application.

Now let’s look at how a sub entity headerReducer looks.

Remember how we designed our header state?

![Image](https://cdn-media-1.freecodecamp.org/images/QASD6Q8cBo1IkbTZw7LKP8sDQcbmEgRLO1TG)
_Header state tree_

```javascript
// Header Reducer

const headerReducer = combineReducer({
    menu: menuReducer,  
    search: searchReducer,  
    location: locationReducer
});
```

Our reducer is a replica of what we designed earlier in our state tree. This is the power of visualisation.

Notice how a reducer contains more reducers. We don’t need to create one huge reducer. It can be easily broken into smaller reducers, as each holds its individual identities and has its own specific operations. This helps us create separation of logic, which is very important for maintaining large apps.

Now let’s understand how a typical reducer file should be set up, for example searchReducer.

```javascript
// Search Reducer

const initialState = {  payload: [],  isLoading: false,  error: {}};

export function searchReducer( state=initialState, action ) { 	 
    switch(action.type) {    
        case FETCH_SEARCH_DATA:      
            return {        
                	...state,        
                    isLoading: true    
            };        
        case FETCH_SEARCH_SUCCESS:      
            return {        
	                ...state,        
                    payload: action.payload,        
                    isLoading: false      
                   };        
        case FETCH_SEARCH_FAILURE:      
            return {        
	                ...state,        
                    error: action.error,        
                    isLoading: false            
            };
                
        case RESET_SEARCH_DATA:      
            return { ...state, ...initialState }        
		default:      return state;
    }
}
```

This reducer pattern defines the changes possible in its search state when the search API is called.

```javascript
FETCH_SEARCH_DATA, FETCH_SEARCH_SUCCESS, FETCH_SEARCH_FAILURE, RESET_SEARCH_DATA
```

All the above are possible constants that define what possible **actions** can be performed.

> _Note: It is important to maintain a RESET_SEARCH_DATA action, in case we need to reset data during the unmounting of a component._

### Step 3: Implement Actions

Every action that has API calls usually goes through three stages in an app.

1. Loading state -> FETCH_SEARCH_DATA
2. Success -> FETCH_SEARCH_SUCCESS
3. Failure -> FETCH_SEARCH_FAILURE

Maintaining these action types helps us check the data flow when an API is called in our app.

Let’s dive into the code to understand what a typical action will look like.

```javascript
export function fetchSearchData(args) {  
	return async (dispatch) => {    
        // Initiate loading state    
        dispatch({      
            type: FETCH_SEARCH_DATA    
        });
        try {      
            // Call the API      
            const result = await fetchSearchData(
                args.pageCount, 
                args.itemsPerPage
            );           
            // Update payload in reducer on success     
            dispatch({        
                type: FETCH_SEARCH_SUCCESS,        
                payload: result,        
                currentPage: args.pageCount      
            });    
        } catch (err) {     
            // Update error in reducer on failure           
            dispatch({        
                type: FETCH_SEARCH_FAILURE,        
                error: err      
            });    
        }  
    };
}
```

Notice how the data flow is tracked by the store through actions. This holds each and every change in the app accountable.

Thus similar actions are written for each change in reducers of various states.

One of the biggest benefits of Redux is the abstraction of each and every action.

![Image](https://cdn-media-1.freecodecamp.org/images/1bOAlC9gdaJZtjvLE8VbESW0m4zGX435YDLo)
_Data Flow in a Redux App_

### Step 4: Implement Presentation

```javascript
import React, { Component } from 'react';
import { connect } from 'react-redux';;

import fetchSearchData from './action/fetchSearchData';
import SearchData from './SearchData';

const Search = (props) => (  
    <SearchData     
    	search={props.search}    
		fetchSearchData={props.fetchSearchData}   
	/>
);

const mapStateToProps = (state) => ({  
    search: state.header.search.payload
});

const mapDispatchToProps = {  fetchSearchData};

export default connect(mapStateToProps, mapDispatchToProps)(Search)
```

As you can see, the presentation component is very simple and easy to understand.

### Conclusion

I would like to mention some of the biggest benefits that I found using Redux:

1. It certainly reduces code smell.
2. Abstraction of code is easier to achieve.
3. Redux also introduces us to other principles like immutability, functional programming, and many others.
4. It allows you to visualise each and every action and track them with “time traveling.”

I hope this article helps you get a clearer picture of why Redux is truly awesome, and how we can utilise the power of visualisation to make maintainable applications.

_Follow me on [twitter](https://twitter.com/daslusan)_ to get more updates regarding new articles and to stay updated in latest frontend developments. Also share this article on twitter to help others know about it. Sharing is caring **^_^.**

### Some helpful resources

1. [https://redux.js.org/](https://redux.js.org/)
2. [https://github.com/reduxjs/redux/blob/master/examples](https://github.com/reduxjs/redux/blob/master/examples)
3. [https://medium.com/@rajaraodv/a-guide-for-building-a-react-redux-crud-app-7fe0b8943d0f#.c4yhhvk0d](https://medium.com/@rajaraodv/a-guide-for-building-a-react-redux-crud-app-7fe0b8943d0f#.c4yhhvk0d)

### My previous articles

1. [https://medium.freecodecamp.org/how-to-use-redux-persist-when-migrating-your-states-a5dee16b5ead](https://medium.freecodecamp.org/how-to-use-redux-persist-when-migrating-your-states-a5dee16b5ead)
2. [https://codeburst.io/redux-observable-to-the-rescue-b27f07406cf2](https://codeburst.io/redux-observable-to-the-rescue-b27f07406cf2)
3. [https://codeburst.io/building-webapp-for-the-future-68d69054cbbd](https://codeburst.io/building-webapp-for-the-future-68d69054cbbd)
4. [https://codeburst.io/cors-story-of-requesting-twice-85219da7172d](https://codeburst.io/cors-story-of-requesting-twice-85219da7172d)

