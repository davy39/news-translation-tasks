---
title: How to Build a Hacker News Clone Using React
subtitle: ''
author: Yogesh Chavan
co_authors: []
series: null
date: '2021-02-12T18:22:26.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-hacker-news-clone-using-react
coverImage: https://cdn-media-2.freecodecamp.org/w1280/60262bb70a2838549dcc42b6.jpg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: null
seo_desc: 'In this tutorial, we will build a mini Hacker News clone in React.

  We will be using React Hooks syntax for building this application. So if you''re
  new to React Hooks, check out my Introduction to React Hooks article to learn the
  basics of Hooks.

  So l...'
---

In this tutorial, we will build a mini [Hacker News](https://news.ycombinator.com/) clone in React.

We will be using React Hooks syntax for building this application. So if you're new to React Hooks, check out my [Introduction to React Hooks](https://levelup.gitconnected.com/an-introduction-to-react-hooks-50281fd961fe?source=friends_link&sk=89baff89ec8bc637e7c13b7554904e54) article to learn the basics of Hooks.

So let's get started.

## Introduction to the API

We will be using the Hackernews API from [this url](https://github.com/HackerNews/API).

API to get top stories, use this URL: [https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty](https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty)

API to get new stories, use this URL: [https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty](https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty)

API to get best stories, use this URL: [https://hacker-news.firebaseio.com/v0/beststories.json?print=pretty](https://hacker-news.firebaseio.com/v0/beststories.json?print=pretty)

Each of the above stories API returns only an array of IDs representing a story.

So to get the details of that particular story, we need to make another API call.

API to get story details, use this URL: [https://hacker-news.firebaseio.com/v0/item/story_id.json?print=pretty](https://hacker-news.firebaseio.com/v0/item/story_id.json?print=pretty)

For example: [https://hacker-news.firebaseio.com/v0/item/26061935.json?print=pretty](https://hacker-news.firebaseio.com/v0/item/26061935.json?print=pretty)

## How to Set Up the Project 

Create a new project using `create-react-app`:

```js
npx create-react-app hackernews-clone-react-app

```

Once the project is created, delete all files from the `src` folder and create `index.js` and `styles.scss` files inside the `src` folder. Also, create `components`, `hooks`, `router`, `utils` folders inside the `src` folder.

Install the required dependencies like this:

```js
yarn add axios@0.21.0 bootstrap@4.6.0 node-sass@4.14.1 react-bootstrap@1.4.0 react-router-dom@5.2.0

```

Open `styles.scss` and add the contents from [here](https://github.com/myogeshchavan97/hackernews-clone-react-app/blob/master/src/styles.scss) inside it.

We'll use SCSS syntax to write CSS. So if you're new to SCSS, check out [my article here](https://medium.com/better-programming/an-introduction-to-sass-scss-fdbda159b40?source=friends_link&sk=c0846e19ddb4f53919a6abaf29032d10) for an introduction to it.

## How to Create the Initial Pages

Create a new file `Header.js` inside the `components` folder with the following content:

```jsx
import React from 'react';
import { NavLink } from 'react-router-dom';

const Header = () => {
  return (
    <React.Fragment>
      <h1>Hacker News Clone</h1>
      <div className="nav-link">
        <NavLink to="/top" activeClassName="active">
          Top Stories
        </NavLink>
        <NavLink to="/new" activeClassName="active">
          Latest Stories
        </NavLink>
        <NavLink to="/best" activeClassName="active">
          Best Stories
        </NavLink>
      </div>
    </React.Fragment>
  );
};

export default Header;

```

In this file, we have added a navigation menu to see the different types of stories. Each link has added a class of `active`. So when we click on that link it will be highlighted, indicating which route we are on.

Create a new file `HomePage.js` inside the `components` folder with the following content:

```jsx
import React from 'react';

const HomePage = () => {
  return <React.Fragment>Home Page</React.Fragment>;
};

export default HomePage;

```

Create a new file `PageNotFound.js` inside the `components` folder with the following content:

```jsx
import React from 'react';
import { Link } from 'react-router-dom';

const PageNotFound = () => {
  return (
    <p>
      Page Not found. Go to <Link to="/">Home</Link>
    </p>
  );
};

export default PageNotFound;

```

Create a new file `AppRouter.js` inside the `router` folder with the following content:

```jsx
import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import Header from '../components/Header';
import HomePage from '../components/HomePage';
import PageNotFound from '../components/PageNotFound';

const AppRouter = () => {
  return (
    <BrowserRouter>
      <div className="container">
        <Header />
        <Switch>
          <Route path="/" component={HomePage} exact={true} />
          <Route component={PageNotFound} />
        </Switch>
      </div>
    </BrowserRouter>
  );
};

export default AppRouter;

```

In this file, initially, we have added two routes for the routing – one for the home page and the other for invalid routes.

If you're new to React Router, check out my free [Introduction to React Router](https://yogeshchavan1.podia.com/react-router-introduction) course.

Now, open the `src/index.js` file and add the following contents inside it:

```jsx
import React from 'react';
import ReactDOM from 'react-dom';
import AppRouter from './router/AppRouter';
import 'bootstrap/dist/css/bootstrap.min.css';
import './styles.scss';

ReactDOM.render(<AppRouter />, document.getElementById('root'));

```

Now, start the application by running the `yarn start` command and you will see the following screen:

![Initial Screen](https://gist.github.com/myogeshchavan97/aa75611665802aadfd3ba6bfeb0fe59b/raw/06ff931efc03ef42cd70a8a44c0dd211a53f5a59/initial_page_1.png)

## API Integration

Now, inside the `utils` folder create a new file called `constants.js` with the following content:

```js
export const BASE_API_URL = 'https://hacker-news.firebaseio.com/v0';

```

Create another file with the name `apis.js` inside the `utils` folder with the following content:

```jsx
import axios from 'axios';
import { BASE_API_URL } from './constants';

const getStory = async (id) => {
  try {
    const story = await axios.get(`${BASE_API_URL}/item/${id}.json`);
    return story;
  } catch (error) {
    console.log('Error while getting a story.');
  }
};

export const getStories = async (type) => {
  try {
    const { data: storyIds } = await axios.get(
      `${BASE_API_URL}/${type}stories.json`
    );
    const stories = await Promise.all(storyIds.slice(0, 30).map(getStory));
    return stories;
  } catch (error) {
    console.log('Error while getting list of stories.');
  }
};

```

In this file, for the `getStories` function we pass the type of story we want (`top`, `new` or `best`). Then we make an API call to the respective `.json` URL provided at the start of this article.

Note that we have declared the function as `async` so we can use the `await` keyword to call the API and wait for the response to come.

```js
const { data: storyIds } = await axios.get(
  `${BASE_API_URL}/${type}stories.json`
);

```

As the `axios` library always returns the result in the `.data` property of the response, we take out that property and rename it to `storyIds` because the API returns an array of story IDs.

Here, we use the ES6 destructuring syntax for renaming the `data` property to `storyIds`. This makes it easy to understand what `storyIds` contains rather than naming it `data`.

Note that the above code is the same as the below code:

```js
const response = await axios.get(
  `${BASE_API_URL}/${type}stories.json`
);
const storyIds = response.data;

```

Since we get an array of story IDs back, instead of making separate API calls for each `id` and then waiting for the previous one to finish, we use the `Promise.all` method to make API calls simultaneously for all the story ids.

```js
const stories = await Promise.all(
  storyIds.slice(0, 30).map((storyId) => getStory(storyId))
);

```

Here, we use the Array slice method to take only the first 30 story ids so the data will load faster.

Then we use the Array map method to call the `getStory` function to make an API call to the individual story item by passing the `storyId` to it.

As in the map function, we just take the storyId and pass it to the `getStory` function. We can simplify it to the following code:

```js
const stories = await Promise.all(storyIds.slice(0, 30).map(getStory));

```

So the `storyId` will be automatically passed to the `getStory` function.

Inside the `getStory` function, we use ES6 template literal syntax to create a dynamic URL based on the passed id for making an API call.

And once we have the stories available, we return that back from the `getStories` function.

## How to Create the Data Fetcher

Create a new file `dataFetcher.js` inside the `hooks` folder with the following content:

```jsx
import { useState, useEffect } from 'react';
import { getStories } from '../utils/apis';

const useDataFetcher = (type) => {
  const [stories, setStories] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    setIsLoading(true);
    getStories(type)
      .then((stories) => {
        setStories(stories);
        setIsLoading(false);
      })
      .catch(() => {
        setIsLoading(false);
      });
  }, [type]);

  return { isLoading, stories };
};

export default useDataFetcher;

```

In this file, we have declared a custom hook `useDataFetcher` that takes the type of story as a parameter and calls the `getStories` function defined in the `apis.js` file inside the `useEffect` hook.

We have added two state variables here using the `useState` hook, namely `stories` and `isLoading`. Before making the API call, we set the `isLoading` state to `true`. Once we get the complete response, we set it to `false`.

We also set the `isLoading` state to `false` inside the catch block so if there is an error, the loader will be hidden.

Once the response is received, we set the `stories` array with the response from the API and we return the `isLoading` and `stories` from the hook in an object. This means that any component using this hook will be able to get the updated value of these state values.

Also, note that we have added `type` as a dependency to the `useEffect` hook as a second parameter inside the array. So whenever we click on the navigation menu (for `top`, `latest` or `best` stories), the type will change and this `useEffect` hook will run again to make an API call to get the stories related to that type.

If you remember, inside the `apis.js` file the `getStories` function is declared as `async` so it will always return a promise. Therefore, we have added the `.then` handler to the `getStories` function to get the actual data from the response inside the `useEffect` hook inside the `dataFetcher.js` file like this:

```js
getStories(type)
      .then((stories) => {
      ...

```

## How to Display Data in the UI

Now, create a new file called `ShowStories.js` inside the `components` folder with the following content:

```jsx
import React from 'react';
import Story from './Story';
import useDataFetcher from '../hooks/dataFetcher';

const ShowStories = (props) => {
  const { type } = props.match.params;
  const { isLoading, stories } = useDataFetcher(type);

  return (
    <React.Fragment>
      {isLoading ? (
        <p className="loading">Loading...</p>
      ) : (
        <React.Fragment>
          {stories.map(({ data: story }) => (
            <Story key={story.id} story={story} />
          ))}
        </React.Fragment>
      )}
    </React.Fragment>
  );
};

export default ShowStories;

```

In this file, we use the `useDataFetcher` custom hook inside the component. Based on the `isLoading` flag, we either display the `Loading` message or the list of stories by using the Array map method for each individual story.

Create a new file `Story.js` inside the `components` folder with the following content:

```jsx
import React from 'react';

const Link = ({ url, title }) => (
  <a href={url} target="_blank" rel="noreferrer">
    {title}
  </a>
);

const Story = ({ story: { id, by, title, kids, time, url } }) => {
  return (
    <div className="story">
      <div className="story-title">
        <Link url={url} title={title} />
      </div>
      <div className="story-info">
        <span>
          by{' '}
          <Link url={`https://news.ycombinator.com/user?id=${by}`} title={by} />
        </span>
        |<span>
          {new Date(time * 1000).toLocaleDateString('en-US', {
            hour: 'numeric',
            minute: 'numeric'
          })}
        </span>|
        <span>
          <Link
            url={`https://news.ycombinator.com/item?id=${id}`}
            title={`${kids && kids.length > 0 ? kids.length : 0} comments`}
          />
        </span>
      </div>
    </div>
  );
};

export default Story;

```

In this file, we display the individual story. 

For defining the `Link` component, we use the ES6 arrow function shorthand syntax of implicit return.

So the below code:

```jsx
const Link = ({ url, title }) => (
  <a href={url} target="_blank" rel="noreferrer">
    {title}
  </a>
);
```

is the same as this code:

```jsx
const Link = ({ url, title }) => {
  return (
    <a href={url} target="_blank" rel="noreferrer">
     {title}
    </a>
  );
}
```

In an arrow function, if there is a single line statement then we can skip the curly brackets and return keyword.

So the below code:

```js
const add = (a,b) => a + b;
```

is the same as this code:

```js
const add = (a,b) => {
  return a + b;
}
```

But to make the JSX look neat and like a single line statement, we add the extra round brackets while defining the `Link` component.

Next, for the `Story` component, we have defined it like this:

```jsx
const Story = ({ story: { id, by, title, kids, time, url } }) => {
  // some code
}
```

Here, we use ES6 destructuring syntax to get the properties of the story object which was passed from the `ShowStories` component.

So the above code is the same as the below code:

```jsx
const Story = (props) => {
  const { id, by, title, kids, time, url } = props.story;
  // some code
}
```

which is the same as the below code:

```jsx
const Story = ({ story }) => {
  const { id, by, title, kids, time, url } = story;
  // some code
}
```

In the API response, we get the time of the story in seconds. So in the `Story` component, we multiply it by 1000 to convert it to milliseconds so we can display the correct date in proper format using JavaScript's `toLocaleDateString` method:

```js
{new Date(time * 1000).toLocaleDateString('en-US', {
  hour: 'numeric',
  minute: 'numeric'
})}
```

Now, open the `AppRouter.js` file and add another Route for the `ShowStories` component before the `PageNotFound` Route.

```jsx
<Switch>
  <Route path="/" component={HomePage} exact={true} />
  <Route path="/:type" component={ShowStories} />
  <Route component={PageNotFound} />
</Switch>

```

Also, add an import for the `ShowStories` component at the top:

```js
import ShowStories from '../components/ShowStories';

```

Now, restart the app by running the `yarn start` command and verify the application.

![Loading News](https://gist.github.com/myogeshchavan97/aa75611665802aadfd3ba6bfeb0fe59b/raw/06ff931efc03ef42cd70a8a44c0dd211a53f5a59/working_navigation.gif)

As you can see, the application is loading the top, latest, and best stories from the HackerNews API correctly.

## How to Handle Dynamic Redirection

If you remember, we added the `HomePage` component so we can display something when the application loads. But now we actually don't need the `HomePage` component, because we can show the top stories page when the application loads.

So open the `AppRouter.js` file and change the first two routes from the below code:

```jsx
<Route path="/" component={HomePage} exact={true} />
<Route path="/:type" component={ShowStories} />

```

to this code:

```jsx
<Route path="/" render={() => <Redirect to="/top" />} exact={true} />
<Route
  path="/:type"
  render={({ match }) => {
    const { type } = match.params;
    if (!['top', 'new', 'best'].includes(type)) {
       return <Redirect to="/" />;
    }
    return <ShowStories type={type} />;
  }}
/>

```

In the first Route, when we load the application by visiting `http://localhost:3000/`, we redirect the user to the `/top` route.

```jsx
<Route path="/" render={() => <Redirect to="/top" />} exact={true} />

```

Here, we use the render props pattern. So instead of providing a component, we use a prop with the name `render` where we can write the component code directly inside the function.

To know why we use `render` instead of `component` prop and what problem it solves, check out my free [Introduction to React Router](https://yogeshchavan1.podia.com/react-router-introduction) course.

Next, we have added a `/:type` route:

```jsx
<Route
  path="/:type"
  render={({ match }) => {
    const { type } = match.params;
    if (!['top', 'new', 'best'].includes(type)) {
      return <Redirect to="/" />;
    }
    return <ShowStories type={type} />;
  }}
/>

```

Here, if the route matches with `/top` or `/new` or `/best` then we're showing the user the `ShowStories` component. If the user enters some invalid value for a route like `/something`, we will redirect the user again to the `/top` route which will render the `ShowStories` component with `top` stories..

We use the ES7 Array `includes` method in the above code inside the if condition.

By default, the React router passes some props to each component mentioned in the `<Route />`. One of them is `match` so `props.match.params` will contain the actual passed value for the `type`.

Therefore, when we access `http://localhost:3000/top`, `props.match.params` will contain the value `top`. When we access `http://localhost:3000/new`, `props.match.params` will contain the value `new` and so on.

For the render prop function, we use destructuring to get the `match` property of the props object by using the following syntax:

```jsx
render={({ match }) => {
}

```

which is the same as:

```jsx
render={(props) => {
 const { match } = props;
}

```

Also, don't forget to import the `Redirect` component from the `react-router-dom` package at the top of the `AppRouter.js` file.

```jsx
import { BrowserRouter, Redirect, Route, Switch } from 'react-router-dom';

```

Now, open the `ShowStories.js` file and change the below code:

```jsx
const ShowStories = (props) => {
  const { type } = props.match.params;
  const { isLoading, stories } = useDataFetcher(type);

```

to this code:

```jsx
const ShowStories = ({ type }) => {
  const { isLoading, stories } = useDataFetcher(type ? type : 'top');

```

Here, we're passing the `type` prop passed from the `AppRouter` component to the `useDataFetcher` custom hook. This will render the correct type of data, based on the `type` passed.

## How to Add a Loading Overlay

Now, we have added redirection code to automatically redirect to the `/top` route on application load. The invalid route also redirects to the `/top` route.

But when the data is loading, we show a simple loading message. While the data is loading, the user can click on another link to make additional requests to the server, which is not good.

So let's add the loading message with an overlay to the screen so the user will not be able to click anywhere while the data is loading.

Create a new file `Loader.js` inside the `components` folder with the following content:

```jsx
import { useState, useEffect } from 'react';
import ReactDOM from 'react-dom';

const Loader = (props) => {
  const [node] = useState(document.createElement('div'));
  const loader = document.querySelector('#loader');

  useEffect(() => {
    loader.appendChild(node).classList.add('message');
  }, [loader, node]);

  useEffect(() => {
    if (props.show) {
      loader.classList.remove('hide');
      document.body.classList.add('loader-open');
    } else {
      loader.classList.add('hide');
      document.body.classList.remove('loader-open');
    }
  }, [loader, props.show]);

  return ReactDOM.createPortal(props.children, node);
};

export default Loader;

```

Now open `public/index.html` file and alongside the div with id `root` add another div with id `loader`, like this:

```js
<div id="root"></div>
<div id="loader"></div>

```

The `ReactDOM.createPortal` method which we have used in `Loader.js` will insert the loader inside the div with id `loader` so it will be outside our `React` application DOM hierarchy. This means that we can use it to provide an overlay for our entire application. This is the primary reason for using the `React Portal` for creating a loader.

So even if we include the `Loader` component in the `ShowStories.js` file, it will be rendered outside all the divs (but inside the div with id `loader`).

In the `Loader.js` file, we have first created a div where we will add a loader message

```js
const [node] = useState(document.createElement('div'));

```

Then, we add the `message` class to that div and finally add that div to the loader div added in `index.html`:

```js
document.querySelector('#loader').appendChild(node).classList.add('message');

```

and based on the `show` prop passed from the `ShowStories` component, we will add or remove the `hide` class. Then finally we will render the `Loader` component using this:

```js
ReactDOM.createPortal(props.children, node);

```

Then we're adding or removing the `loader-open` class from the body tag of the page which will disable or enable the scrolling of the page:

```js
document.body.classList.add('loader-open');
document.body.classList.remove('loader-open');

```

The data we pass in between the opening and closing `Loader` tag inside the `ShowStories` component will be available inside `props.children`. So we can display a simple loading message or we can include an image to be shown as a loader.

Now, let’s use this component.

Open `ShowStories.js` file and replace its contents with the following content:

```jsx
import React from 'react';
import Story from './Story';
import useDataFetcher from '../hooks/dataFetcher';
import Loader from './Loader';

const ShowStories = (props) => {
  const { type } = props.match.params;
  const { isLoading, stories } = useDataFetcher(type);

  return (
    <React.Fragment>
      <Loader show={isLoading}>Loading...</Loader>
      <React.Fragment>
        {stories.map(({ data: story }) => (
          <Story key={story.id} story={story} />
        ))}
      </React.Fragment>
    </React.Fragment>
  );
};

export default ShowStories;

```

Here, we use the Loader component by passing the show prop to it.

```jsx
<Loader show={isLoading}>Loading...</Loader>

```

Now, if you check the application, you will see the loading overlay:

![Loading Overlay](https://gist.github.com/myogeshchavan97/aa75611665802aadfd3ba6bfeb0fe59b/raw/06ff931efc03ef42cd70a8a44c0dd211a53f5a59/loader.gif)

So now the user cannot click on any link while the data is loading, which is a nice improvement.

For each story, we're showing the author and the total comments as hyperlinks. Clicking on them takes us to the Hackernews website to show the respective details as you can see in the below gif.

![Working hyperlinks](https://gist.github.com/myogeshchavan97/aa75611665802aadfd3ba6bfeb0fe59b/raw/06ff931efc03ef42cd70a8a44c0dd211a53f5a59/links.gif)

## Closing points

We're done building out the functionality of the App.

You can find the complete GitHub source code [here](https://github.com/myogeshchavan97/hackernews-clone-react-app), and a live demo [here](https://hackernews-clone-react-app.netlify.app/).

To take your skills further, you can improve the application by adding extra functionalities like:

* Add pagination functionality to load the next 30 records for each page
* Create a separate page in the application for displaying the comments using the [Hacker News API](https://github.com/HackerNews/API). When clicked on, the comments count the link instead of redirecting the user to the Hackernews website

### Thanks for reading!

Want to build more amazing projects? Check them out [here](https://github.com/myogeshchavan97#choose-pinned-repositories).

Also, you can check out my free [Introduction to React Router](https://yogeshchavan1.podia.com/react-router-introduction) course to learn React Router from scratch.

Want to learn all ES6+ features in detail including let and const, promises, various promise methods, array and object destructuring, arrow functions, async/await, import and export and a whole lot more? 

Check out my [Mastering Modern JavaScript](https://yogeshchavan1.podia.com/mastering-modern-javascript?coupon=LA1HR55) book. This book covers all the pre-requisites for learning React and helps you to become better at JavaScript and React.

**Don't forget to subscribe to my [weekly newsletter](https://yogeshchavan.dev) to get amazing tips, tricks, articles and discount deals directly in your inbox.**

