---
title: How I architected a single-page React application
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-13T15:21:45.000Z'
originalURL: https://freecodecamp.org/news/how-i-architected-a-single-page-react-application-3ebd90f59087
coverImage: https://cdn-media-1.freecodecamp.org/images/1*XLkAyY1s1ON4sMc3zLC2hQ.png
tags:
- name: Apps
  slug: apps-tag
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Redux
  slug: redux
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Gooi Ying Chyi

  With Data Structures, Components and integration with Redux


  _Background photo by [Unsplash](https://unsplash.com/photos/A-btl_OPYWA?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText"
  rel="noopener" target="_blank" ...'
---

By Gooi Ying Chyi

#### With Data Structures, Components and integration with Redux

![Image](https://cdn-media-1.freecodecamp.org/images/nND6eYTLXiJIuT1h3LBvVG3Vk5-UAWrU1NL2)
_Background photo by [Unsplash](https://unsplash.com/photos/A-btl_OPYWA?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Sven Mieke</a> on <a href="https://unsplash.com/search/photos/architect?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

I recently built a single-page application that interacts with a backend JSON API server. I chose to use React to deepen my understanding of React fundamentals and how each tool can help in building a scalable frontend.

The stack of this application consists of:

* Frontend with React/Redux
* A backend JSON API server with Sinatra, integrated with Postgres for database persistence
* An API client that fetches data from [OMDb API](http://www.omdbapi.com/), written in Ruby

For this post, we’ll assume that we have the backend completed. So let’s focus on how design decisions are made on the frontend.

> Side note: The decisions presented here are for reference only and may vary depending on the needs of your application. An example OMDb Movie Tracker app is used here for demonstration.

### The App

The application consists of a search input form. A user can input a movie title to return a movie result from [OMDb](http://www.omdbapi.com/). The user can also save a movie with a rating and short comment into a favorites list.

**To view the final app, [click here](https://omdb-tracker.herokuapp.com/).** To view the source code, click [here](https://github.com/YingCGooi/omdb-tracker/tree/master/public/js).

When a user searches a movie on the homepage, it looks like this:

![Image](https://cdn-media-1.freecodecamp.org/images/0gKNb-YMTg5WJIH7IsZjxZe1ql7mSfRSXvFm)
_The UI contains a search input form and a movie result below it._

For the sake of simplicity, we’ll only focus on designing the core features of the application in this article. You can also skip to [**Part II: Redux**](https://medium.com/p/d6eaf235f4d) of the series.

### Data Structure

Defining appropriate data structures should be one of the most important aspects of designing an app. This should come as the first step, as it determines not only how the frontend should render the elements, but also how the API server should return the JSON responses.

For this app, we’ll need two main pieces of information to properly render our UI: **a single movie result** and **a list of favorited movies**.

#### Movie result object

A single movie result will contain information such as the title, year, description, and poster image. With this, we need to define an object that can store these attributes:

```
{  "title": "Star Wars: Episode IV - A New Hope",  "year": "1977",  "plot": "Luke Skywalker joins forces with a Jedi Knight...",  "poster": "https://m.media-amazon.com/path/to/poster.jpg",  "imdbID": "tt0076759"}
```

The `poster` property is simply a URL to the poster image that will be displayed in the results. If there’s no poster available for that movie, it will be “N/A”, which we will display a placeholder. We will also need an `imdbID` attribute to uniquely identify each movie. This is useful for determining whether or not a movie result already exists in the favorites list. We’ll explore later on how it works.

#### Favorites list

The favorites list will contain all of the movies saved as favorites. The list will look something like this:

![Image](https://cdn-media-1.freecodecamp.org/images/yePajd0g-58FZyL3VjU4p5FpUIopTxekHRId)
_Each movie also includes additional favorite information (rating and comment)_

```
[  { title: "Star Wars", year: "1977", ..., rating: 4 },  { title: "Avatar", year: "2009", ..., rating: 5 }]
```

Keep in mind that we’ll need to look up a specific movie from the list, and the time complexity for this approach is **O(N)**. While it works fine for smaller datasets, imagine having to search for a movie in a favorites list that grows indefinitely.

With this in mind, I chose to go with a hash table with keys as `imdbID` and values as favorited movie objects:

```
{  tt0076759: {    title: "Star Wars: Episode IV - A New Hope",    year: "1977",    plot: "...",    poster: "...",    rating: "4",    comment: "May the force be with you!",  },  tt0499549: {    title: "Avatar",    year: "2009",    plot: "...",    poster: "...",    rating: "5",    comment: "Favorite movie!",  }}
```

With this, we can look up a movie in the favorites list in **O(1)** time by its `imdbID`.

> Note: the runtime complexity is probably not going to matter in most cases since the datasets are usually small on the client-side. We are also going to perform slicing and copying (also O(N) operations) in Redux anyway. But as an engineer, it’s good to be aware of potential optimizations that we can perform.

### Components

Components are at the heart of React. We’ll need to determine which ones that will interact with the Redux store, and which ones that are only for presentation. We can also reuse some of the presentational components too. Our component hierarchy will look something like this:

![Image](https://cdn-media-1.freecodecamp.org/images/CQkO-xEK5ZexcrR2ZcxtT4EEssWFfFVfjTHQ)

#### Main page

We designate our **App** component at the top level. When the root path is visited, it needs to render the **SearchContainer**. It also needs to display flash messages to the user and handle the client-side routing.

The **SearchContainer** will retrieve the movie result from our Redux store, providing information as props to **MovieItem** for rendering. It will also dispatch a search action when a user submits a search in **SearchInputForm**. More on Redux later.

![Image](https://cdn-media-1.freecodecamp.org/images/-vfxKYTuzgfogu4M6eL7rL4JjdDimzZeJgJN)
_A modal that allows users to add a rating and comment when saving a favorite._

#### Add To Favorites Form

When the user clicks on the “Add To Favorites” button, we will display the **AddFavoriteForm**, a [controlled component](https://reactjs.org/docs/forms.html).

We are constantly updating its state whenever a user changes the rating or input text in the comment text area. This is useful for validation upon form submission.

The **RatingForm** is responsible to render the yellow stars when the user clicks on them. It also informs the current rating value to **AddFavoriteForm**.

![Image](https://cdn-media-1.freecodecamp.org/images/sI9SYwjKc0LvLer5OQLAsKTnvbA7etM-Of0S)
_The FavoritesContainer contains a list of MovieItem components_

#### Favorites Tab

When a user clicks on the “Favorites” tab, the **App** renders **FavoritesContainer**.

The **FavoritesContainer** is responsible for retrieving the favorites list from the Redux store. It also dispatches actions when a user changes a rating or clicks on the “Remove” button.

Our **MovieItem** and **FavoritesInfo** are simply presentational components that receive props from **FavoritesContainer**.

We’ll reuse the **RatingForm** component here. When a user clicks on a star in the **RatingForm**, the **FavoritesContainer** receives the rating value and dispatches an update rating action to the Redux store.

### Redux Store

Our Redux store will include reducers that handle the search and favorites actions. Additionally, we’ll need to include a status reducer to track state changes when a user initiates an action. We’ll explore more on the status reducer later.

```
//store.js
```

```
import { createStore, combineReducers, applyMiddleware } from 'redux';import thunk from "redux-thunk";
```

```
import search from './reducers/searchReducer';import favorites from './reducers/favoritesReducer';import status from './reducers/statusReducer';
```

```
export default createStore(  combineReducers({    search,    favorites,    status  }),  {},  applyMiddleware(thunk))
```

We’ll also apply the Redux Thunk middleware right away. We’ll go more into detail on that later. Now, let’s figure out how we manage the state changes when a user submits a search.

### Search Reducer

When a user performs a search action, we want to update the store with a new search result via **searchReducer**. We can then render our components accordingly. The general flow of events looks like this:

![Image](https://cdn-media-1.freecodecamp.org/images/0yVmnP0XRxj058OjNxAnsYZ2mLIZCXxVL-tZ)

We’ll treat **“Get search result”** as a black box for now. We’ll explore how that works later with Redux Thunk. Now, let’s implement the reducer function.

```
//searchReducer.js
```

```
const initialState = {  "title": "",  "year": "",  "plot": "",  "poster": "",  "imdbID": "",}
```

```
export default (state = initialState, action) => {  if (action.type === 'SEARCH_SUCCESS') {    state = action.result;  }  return state;}
```

The **initialState** will represent the data structure defined earlier as a single movie result object. In the reducer function, we handle the action where a search is successful. If the action is triggered, we simply reassign the state to the new movie result object.

```
//searchActions.jsexport const searchSuccess = (result) => ({  type: 'SEARCH_SUCCESS', result});
```

We define an action called **searchSuccess** that takes in a single argument, the movie result object, and returns an action object of type “**SEARCH_SUCCESS**”. We will dispatch this action upon a successful search API call.

### Redux Thunk: Search

Let’s explore how the **“Get search result”** from earlier works. First, we need to make a remote API call to our backend API server. When the request receives a successful JSON response, we’ll dispatch the **searchSuccess** action along with the payload to **searchReducer**.

Knowing that we’ll need to dispatch after an asynchronous call completes, we’ll make use of [Redux Thunk](https://github.com/reduxjs/redux-thunk). Thunk comes into play for making multiple dispatches or delaying a dispatch. With Thunk, our updated flow of events looks like this:

![Image](https://cdn-media-1.freecodecamp.org/images/yHA6xMauC4xW6a1nEIAdacp5WFVFSdeISmD-)

For this, we define a function that takes in a single argument `title` and serves as the initial **search** action. This function is responsible for fetching the search result and dispatching a **searchSuccess** action:

```
//searchActions.jsimport apiClient from '../apiClient';
```

```
...
```

```
export function search(title) {  return (dispatch) => {    apiClient.query(title)      .then(response => {        dispatch(searchSuccess(response.data))      });  }}
```

We’ve set up our API client beforehand, and you can read more about [how I set up the API client here](https://medium.com/@gooiyingchyi/how-i-architected-a-single-page-react-application-part-i-data-structure-components-and-apis-24386cc78a6#40eb). The `apiClient.query` method simply performs an AJAX GET request to our backend server and returns a Promise with the response data.

We can then connect this function as an action dispatch to our **SearchContainer** component:

```
//SearchContainer.js
```

```
import React from 'react';import { connect } from 'react-redux';import { search } from '../actions/searchActions';
```

```
...
```

```
const mapStateToProps = (state) => (  {    result: state.search,  });
```

```
const mapDispatchToProps = (dispatch) => (  {    search(title) {      dispatch(search(title))    },  });
```

```
export default connect(mapStateToProps, mapDispatchToProps)(SearchContainer);
```

When a search request succeeds, our **SearchContainer** component will render the movie result:

![Image](https://cdn-media-1.freecodecamp.org/images/wKuIVFaH6OSKpSeLBSDal3InlrYE90kQ2G7n)
_Left: the app renders the movie result | Right: a successful search request_

### Handling Other Search Statuses

Now we have our **search** action working properly and connected to our **SearchContainer** component, we’d like to handle other cases other than a successful search.

#### Search request pending

When a user submits a search, we’ll display a loading animation to indicate that the search request is pending:

![Image](https://cdn-media-1.freecodecamp.org/images/21mRK3c6oKbo-jrWRsZJUVKIod0rOiV0aYJY)
_The app displays a spinner animation when waiting for the search result_

#### Search request succeeds

If the search fails, we’ll display an appropriate error message to the user. This is useful to provide some context. A search failure could happen in cases where a movie title is not available, or our server is experiencing issues communicating with the OMDb API.

![Image](https://cdn-media-1.freecodecamp.org/images/QaamwSGVP5uJZINbdEe9W4v5j8OpEF3TH2GZ)
_When a movie title is not found in OMDb, we display an error message_

To handle different search statuses, we’ll need a way to store and update the current status along with any error messages.

### Status Reducer

The **statusReducer** is responsible for tracking state changes whenever a user performs an action. The current state of an action can be represented by one of the three “statuses”:

* Pending (when a user first initiates the action)
* Success (when a request returns a successful response)
* Error (when a request returns an error response)

With these statuses in place, we can render different UIs based on the current status of a given action type. In this case, we’ll focus on tracking the status of the **search** action.

We’ll start by implementing the **statusReducer**. For the initial state, we need to track the current search status and any errors:

```
// statusReducer.jsconst initialState = {  search: '',      // status of the current search  searchError: '', // error message when a search fails}
```

Next, we need to define the reducer function. Whenever our **SearchContainer** dispatches a “SEARCH_[STATUS]” action, we will update the store by replacing the `search` and `searchError` properties.

```
// statusReducer.js
```

```
...
```

```
export default (state = initialState, action) => {  const actionHandlers = {    'SEARCH_REQUEST': {      search: 'PENDING',      searchError: '',    },    'SEARCH_SUCCESS': {      search: 'SUCCESS',       searchError: '',          },    'SEARCH_FAILURE': {      search: 'ERROR',      searchError: action.error,     },  }  const propsToUpdate = actionHandlers[action.type];  state = Object.assign({}, state, propsToUpdate);  return state;}
```

We use an `actionHandlers` hash table here since we are only replacing the state’s properties. Furthermore, it improves readability more than using `if/else` or `case` statements.

With our **statusReducer** in place, we can render the UI based on different search statuses. We will update our flow of events to this:

![Image](https://cdn-media-1.freecodecamp.org/images/moKAD85gibVfj7nAGAWQ0DOHWGnUCROV1Kvs)

We now have additional **searchRequest** and **searchFailure** actions available to dispatch to the store:

```
//searchActions.js
```

```
export const searchRequest = () => ({  type: 'SEARCH_REQUEST'});
```

```
export const searchFailure = (error) => ({  type: 'SEARCH_FAILURE', error});
```

To update our **search** action, we will dispatch **searchRequest** immediately and will dispatch **searchSuccess** or **searchFailure** based on the eventual success or failure of the Promise returned by Axios:

```
//searchActions.js
```

```
...
```

```
export function search(title) {  return (dispatch) => {    dispatch(searchRequest());
```

```
apiClient.query(title)      .then(response => {        dispatch(searchSuccess(response.data))      })      .catch(error => {        dispatch(searchFailure(error.response.data))      });  }}
```

We can now connect the search status state to our **SearchContainer**, passing it as a prop. Whenever our store receives the state changes, our **SearchContainer** renders a loading animation, an error message, or the search result:

```
//SearchContainer.js
```

```
...(imports omitted)
```

```
const SearchContainer = (props) => (  <main id='search-container'>    <SearchInputForm       placeholder='Search movie title...'      onSubmit={ (title) => props.search(title) }    />    {      (props.searchStatus === 'SUCCESS')      ? <MovieItem          movie={ props.result }          ...(other props)        />      : null    }    {      (props.searchStatus === 'PENDING')      ? <section className='loading'>          <img src='../../images/loading.gif' />        </section>      : null    }    {      (props.searchStatus === 'ERROR')      ? <section className='error'>           <p className='error'>            <i className="red exclamation triangle icon"></i>            { props.searchError }          </p>        </section>      : null    }  </main>);
```

```
const mapStateToProps = (state) => (  {    searchStatus: state.status.search,    searchError: state.status.searchError,    result: state.search,  });
```

```
...
```

### Favorites Reducer

We’ll need to handle CRUD actions performed by a user on the favorites list. Recalling from our API endpoints earlier, we’d like to allow users to perform the following actions and update our store accordingly:

* Save a movie into the favorites list
* Retrieve all favorited movies
* Update a favorite’s rating
* Delete a movie from the favorites list

To ensure that the reducer function is pure, we simply copy the old state into a new object together with any new properties using`Object.assign`. Note that we only handle actions with types of **_SUCCESS**:

```
//favoritesReducer.js
```

```
export default (state = {}, action) => {  switch (action.type) {    case 'SAVE_FAVORITE_SUCCESS':      state = Object.assign({}, state, action.favorite);      break;
```

```
case 'GET_FAVORITES_SUCCESS':      state = action.favorites;      break;
```

```
case 'UPDATE_RATING_SUCCESS':      state = Object.assign({}, state, action.favorite);      break;
```

```
case 'DELETE_FAVORITE_SUCCESS':      state = Object.assign({}, state);      delete state[action.imdbID];      break;
```

```
default: return state;  }  return state;}
```

We’ll leave the **initialState** as an empty object. The reason is that if our **initialState** contains placeholder movie items, our app will render them immediately before waiting for the actual favorites list response from our backend API server.

From now on, each of the favorites action will follow a general flow of events illustrated below. The pattern is similar to the search action in the previous section, except right now we’ll skip handling any “PENDING” status.

![Image](https://cdn-media-1.freecodecamp.org/images/DEOjBJXFxeZIaQDKMU5Y-4aQbLX98VRy3R4d)

#### Save Favorites Action

Take the save favorites action for example. The function makes an API call to with our **apiClient** and dispatches either a **saveFavoriteSuccess** or a **saveFavoriteFailure** action, depending on whether or not we receive a successful response:

```
//favoritesActions.jsimport apiClient from '../apiClient';
```

```
export const saveFavoriteSuccess = (favorite) => ({  type: 'SAVE_FAVORITE_SUCCESS', favorite});
```

```
export const saveFavoriteFailure = (error) => ({  type: 'SAVE_FAVORITE_FAILURE', error});
```

```
export function save(movie) {  return (dispatch) => {    apiClient.saveFavorite(movie)      .then(res => {        dispatch(saveFavoriteSuccess(res.data))      })      .catch(err => {        dispatch(saveFavoriteFailure(err.response.data))      });  }}
```

We can now connect the **save** favorite action to **AddFavoriteForm** through React Redux.

To read more about how I handled the flow to display flash messages, [click here](https://blog.usejournal.com/how-i-architected-a-single-page-react-application-part-ii-redux-d6eaf235f4d#956b).

### Conclusion

Designing the frontend of an application requires some forethought, even when using a popular JavaScript library such as React. By thinking about how the data structures, components, APIs, and state management work as a whole, we can better anticipate edge cases and effectively fix errors when they arise. By using certain design patterns such as controlled components, Redux, and handling AJAX workflow using Thunk, we can streamline managing the flow of providing UI feedback to user actions. Ultimately, how we approach the design will have an impact on usability, clarity, and future scalability.

#### References

[Fullstack React: The Complete Guide to ReactJS and Friends](https://www.fullstackreact.com/#table-of-contents)

### About me

I am a software engineer located in NYC and co-creator of [SpaceCraft](https://spacecraft-repl.com). I have experience in designing single-page applications, synchronizing state between multiple clients, and deploying scalable applications with Docker.

**I am currently looking for my next full-time opportunity! Please [get in touch](https://gooi.tech) if you think that I will be a good fit for your team.**

