---
title: A Complete Beginner's Guide to React Router (Including Router Hooks)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-18T11:05:00.000Z'
originalURL: https://freecodecamp.org/news/a-complete-beginners-guide-to-react-router-include-router-hooks
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/cover.png
tags:
- name: React
  slug: react
- name: react router
  slug: react-router
seo_title: null
seo_desc: 'By Ibrahima Ndaw

  React is a JavaScript library for building user interfaces. We can also extend it
  to build multi-page applications with the help of React Router. This is a third-party
  library that enables routing in our React apps.

  In this tutorial,...'
---

By Ibrahima Ndaw

React is a JavaScript library for building user interfaces. We can also extend it to build multi-page applications with the help of React Router. This is a third-party library that enables routing in our React apps.

In this tutorial, we are going to cover everything you need to know to get started with React Router.

* [Setting up the project](#heading-setting-up-the-project)
* [What is routing?](#heading-what-is-routing)
* [Setting up the router](#heading-setting-up-the-router)
* [Rendering routes](#heading-rendering-routes)
* [Using Links to switch pages](#heading-using-links-to-switch-pages)
* [Passing Route parameters](#heading-passing-route-parameters)
* [Navigating programmatically](#heading-navigating-programmatically)
* [Redirecting to another page](#heading-redirecting-to-another-page)
* [Redirecting to a 404 page](#redirecting-to-404-page)
* [Guarding routes](#heading-guarding-routes)
* [Router Hooks](#heading-router-hooks)
* [useHistory](#heading-usehistory)
* [useParams](#heading-useparams)
* [useLocation](#heading-uselocation)
* [Final Thoughts](#heading-final-thoughts)
* [Next Steps](#heading-next-steps)

## Setting up the project

To be able to follow along, you will need to create a new React app by running the following command in your terminal:

```shell
npx create-react-app react-router-guide

```

Then, add these lines of code to the `App.js` file:

```jsx
import React from "react";
import "./index.css"

export default function App() {
  return (
    <main>
      <nav>
        <ul>
          <li><a href="/">Home</a></li>
          <li><a href="/about">About</a></li>
          <li><a href="/contact">Contact</a></li>
        </ul>
        </nav>
     </main>
  );
}
// Home Page
const Home = () => (
  <Fragment>
    <h1>Home</h1>
    <FakeText />
  </Fragment>
  );
// About Page
const About = () => (
  <Fragment>
    <h1>About</h1>
    <FakeText />
  </Fragment>
  );
// Contact Page
const Contact = () => (
  <Fragment>
    <h1>Contact</h1>
    <FakeText />
  </Fragment>
  );

const FakeText = () => (
  <p>
  Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
  </p>
  )

```

Then, if you're ready to go, let's start by answering an important question: what is routing?

## What is routing?

Routing is the capacity to show different pages to the user. That means the user can move between different parts of an application by entering a URL or clicking on an element.

As you may already know, by default, React comes without routing. And to enable it in our project, we need to add a library named [react-router](https://reacttraining.com/react-router/web/guides/quick-start).

To install it, you will have to run the following command in your terminal:

```shell
yarn add react-router-dom

```

Or

```shell
npm install react-router-dom

```

Now, we've successfully installed our router, let's start using it in the next section.

## Setting up the router

To enable routing in our React app, we first need to import `BrowserRouter` from `react-router-dom`.

In the `App.js` file, enter the following:

```jsx
import React, { Fragment } from "react";
import "./index.css"

import { BrowserRouter as Router } from "react-router-dom";

export default function App() {
  return (
  <Router>
    <main>
      <nav>
        <ul>
          <li><a href="/">Home</a></li>
          <li><a href="/about">About</a></li>
          <li><a href="/contact">Contact</a></li>
        </ul>
      </nav>
    </main>
</Router>
  );
}

```

This should hold everything in our app where routing is needed. That means, if we need routing in our entire app, we must wrap our higher component with `BrowserRouter`.

By the way, you don't have to rename `BrowserRouter as Router` as I do here, I just want to keep things readable.

A router alone doesn't do much. So let's add a route in the next section.

## Rendering routes

To render routes, we have to import the `Route` component from the router package.

In your `App.js` file, add the following code:

```jsx
import React, { Fragment } from "react";
import "./index.css"

import { BrowserRouter as Router, Route } from "react-router-dom";

export default function App() {
  return (
  <Router>
    <main>
      <nav>
        <ul>
          <li><a href="/">Home</a></li>
          <li><a href="/about">About</a></li>
          <li><a href="/contact">Contact</a></li>
        </ul>
      </nav>
  <Route path="/" render={() => <h1>Welcome!</h1>} />
    </main>
</Router>
  );
}

```

Then, add it where we want to render the content. The `Route` component has several properties. But here, we just need `path` and `render`.

`path`: the path of the route. Here, we use `/` to define the path of the home page.

`render`: will display the content whenever the route is reached. Here, we'll render a welcome message to the user.

In some cases serving routes like that is perfectly fine. But imagine a case when we have to deal with a real component – using `render` may not be the right solution.

So, how can we display a real component? Well, the `Route` component has another property named `component`.

Let's update our example a bit to see it in action.

In your `App.js` file, add the following code:

```jsx
import React, { Fragment } from "react";
import "./index.css"

import { BrowserRouter as Router, Route } from "react-router-dom";

export default function App() {
  return (
   <Router>
    <main>
      <nav>
        <ul>
          <li><a href="/">Home</a></li>
          <li><a href="/about">About</a></li>
          <li><a href="/contact">Contact</a></li>
        </ul>
      </nav>

    <Route path="/" component={Home} />
    </main>
</Router>
  );
}

const Home = () => (
  <Fragment>
    <h1>Home</h1>
    <FakeText />
  </Fragment>
  );

```

Now, instead of rendering a message, our route will load the `Home` component.

To get the full power of React Router, we need to have multiple pages and links to play with. We already have pages (components if you want, too), so now let's add some links so we can switch between pages.

## Using links to switch pages

To add links to our project, we will use the React Router again.

In your `App.js` file, add the following code:

```jsx
import React, { Fragment } from "react";
import "./index.css"

import { BrowserRouter as Router, Route, Link } from "react-router-dom";

export default function App() {
  return (
   <Router>
    <main>
      <nav>
        <ul>
          <li><Link to="/">Home</Link></li>
          <li><Link to="/about">About</Link></li>
          <li><Link to="/contact">Contact</Link></li>
        </ul>
      </nav>

    <Route path="/" exact component={Home} />
    <Route path="/about"  component={About} />
    <Route path="/contact"  component={Contact} />

    </main>
</Router>
  );
}

const Home = () => (
  <Fragment>
    <h1>Home</h1>
    <FakeText />
  </Fragment>
  );

const About = () => (
  <Fragment>
    <h1>About</h1>
    <FakeText />
  </Fragment>
  );

const Contact = () => (
  <Fragment>
    <h1>Contact</h1>
    <FakeText />
  </Fragment>
  );

```

After importing `Link`, we have to update our navigation bar a bit. Now, instead of using `a` tag and `href`, React Router uses `Link` and `to` to, well, be able to switch between pages without reloading it.

Then, we need to add two new routes, `About` and `Contact`, to be able to switch between pages or components.

Now, we can go to different parts of our app through links. But there is an issue with our router: the `Home` component is always displayed even if we switch to other pages.

This is because React Router will check if the `path` defined starts with `/`. If that's the case, it will render the component. And here, our first route starts with `/`, so the `Home` component will be rendered each time.

However, we can still change the default behavior by adding the `exact` property to `Route`.

In `App.js`, add:

```jsx
    <Route path="/" exact component={Home} />

```

By updating the `Home` route with `exact`, now it will be rendered only if it matches the full path.

We can still enhance it by wrapping our routes with `Switch` to tell to React Router to load only one route at a time.

In `App.js`, add:

```jsx
import { BrowserRouter as Router, Route, Link, Switch } from "react-router-dom";

  <Switch>
    <Route path="/" exact component={Home} />
    <Route path="/about"  component={About} />
    <Route path="/contact"  component={Contact} />
  </Switch>

```

Now that we have new links, let's use them to pass parameters.

## Passing route parameters

To pass data between pages, we have to update our example.

In your `App.js` file, add the following code:

```jsx
import React, { Fragment } from "react";
import "./index.css"

import { BrowserRouter as Router, Route, Link, Switch } from "react-router-dom";

export default function App() {
  const name = 'John Doe'
  return (
   <Router>
    <main>
      <nav>
        <ul>
          <li><Link to="/">Home</Link></li>
          <li><Link to={`/about/${name}`}>About</Link></li>
          <li><Link to="/contact">Contact</Link></li>
        </ul>
      </nav>
    <Switch>
      <Route path="/" exact component={Home} />
      <Route path="/about/:name"  component={About} />
      <Route path="/contact"  component={Contact} />
    </Switch>
    </main>
</Router>
  );
}

const Home = () => (
  <Fragment>
    <h1>Home</h1>
    <FakeText />
  </Fragment>
  );

const About = ({match:{params:{name}}}) => (
  // props.match.params.name
  <Fragment>
    <h1>About {name}</h1>
    <FakeText />
  </Fragment>
);

const Contact = () => (
  <Fragment>
    <h1>Contact</h1>
    <FakeText />
  </Fragment>
  );

```

As you can see here, we start by declaring a new constant `name` which will be passed as a parameter to the `About` page. And we append `name` to the corresponding link.

With that, we now have to update the `About` route by adjusting its path to receive `name` as a parameter `path="/about/:name"`.

Now, the parameter will be received as props from the `About` component. The only thing we have to do now is destructure the props and get back the `name` property. By the way, `{match:{params:{name}}}` is the same as `props.match.params.name`.

We've done a lot up to this point. But in some cases we don't want to use links to navigate between pages.

Sometimes, we have to wait for an operation to finish before navigating to the next page.

So, let's handle that case in the next section.

## Navigating programmatically

The props we receive have some convenient methods we can use to navigate between pages.

In `App.js`, add:

```jsx
const Contact = ({history}) => (
  <Fragment>
    <h1>Contact</h1>
    <button onClick={() => history.push('/') } >Go to home</button>
    <FakeText />
  </Fragment>
  );

```

Here, we pull the `history` object from the props we receive. It has some handy methods like `goBack`, `goForward`, and so on. But here, we will use the `push` method to be able to go to the Home page.

Now, let's handle the case when we want to redirect our user after an action.

## Redirecting to another page

The React Router has another component named `Redirect`. As you guessed, it helps us redirect the user to another page

In `App.js`, add:

```jsx
import { BrowserRouter as Router, Route, Link, Switch, Redirect } from "react-router-dom";

const About = ({match:{params:{name}}}) => (
  // props.match.params.name
  <Fragment>
    { name !== 'John Doe' ? <Redirect to="/" /> : null }
    <h1>About {name}</h1>
    <FakeText />
  </Fragment>
);

```

Now, if the `name` passed as a parameter is not equal to `John Doe`, the user will be redirected to the home page.

You could argue that you should redirect the user with `props.history.push('/)`. Well, the `Redirect` component replaces the page and therefore the user can't go back to the previous page. But, with the push method they can. However, you can use `props.history.replace('/)` to mimic the `Redirect` behavior.

Now let's move on and handle the case when the user hits a route that doesn't exist.

## Redirecting to a 404 page

To redirect the user to a 404 page, you can create a component to show it. But here, to keep things simple, I will just display a message with `render`.

```jsx
import React, { Fragment } from "react";
import "./index.css"

import { BrowserRouter as Router, Route, Link, Switch } from "react-router-dom";

export default function App() {
  const name = 'John Doe'
  
  return (
   <Router>
    <main>
      <nav>
        <ul>
          <li><Link to="/">Home</Link></li>
          <li><Link to={`/about/${name}`}>About</Link></li>
          <li><Link to="/contact">Contact</Link></li>
        </ul>
      </nav>
    <Switch>
      <Route path="/" exact component={Home} />
      <Route path="/about/:name"  component={About} />
      <Route path="/contact"  component={Contact} />
      <Route render={() => <h1>404: page not found</h1>} />
      
    </Switch>
    </main>
</Router>
  );
}

```

The new route we've added will catch every path that doesn't exist and redirect the user to the 404 page.

Now, let's move on and learn how to protect our routes in the next section.

## Guarding routes

There are many ways to protect routes to React. But here I will just check if the user is authenticated and redirect them to the appropriate page.

```jsx
import React, { Fragment } from "react";
import "./index.css"

import { BrowserRouter as Router, Route, Link, Switch } from "react-router-dom";

export default function App() {
  const name = 'John Doe'
  const isAuthenticated = false
  return (
   <Router>
    <main>
      <nav>
        <ul>
          <li><Link to="/">Home</Link></li>
          <li><Link to={`/about/${name}`}>About</Link></li>
          <li><Link to="/contact">Contact</Link></li>
        </ul>
      </nav>
    <Switch>
      <Route path="/" exact component={Home} />
      {
      isAuthenticated ? 
      <>
      <Route path="/about/:name"  component={About} />
      <Route path="/contact"  component={Contact} />
      </> : <Redirect to="/" />
      }
      
    </Switch>
    </main>
</Router>
  );
}

```

As you can see here, I declared a variable to mimic authentication. Then, check if the user is authenticated or not. If they are, render protected pages. Otherwise redirect them to the home page.

We've covered a lot up to this point, but an interesting part remains: router hooks.

Let's move to the final section and introduce Hooks.

## Router Hooks

Router hooks make things much easier. Now you can access the history, location, or parameters in an easy and elegant way.

### useHistory

The `useHistory` hook gives us access to the history instance without pulling it from props.

```jsx
import { useHistory } from "react-router-dom";

const Contact = () => {
const history = useHistory();
return (
  <Fragment>
    <h1>Contact</h1>
    <button onClick={() => history.push('/') } >Go to home</button>
  </Fragment>
  )
  };

```

### useParams

This hook helps us get the parameter passed on the URL without using the props object.

```jsx
import { BrowserRouter as Router, Route, Link, Switch, useParams } from "react-router-dom";

export default function App() {
  const name = 'John Doe'
  return (
   <Router>
    <main>
      <nav>
        <ul>
          <li><Link to="/">Home</Link></li>
          <li><Link to={`/about/${name}`}>About</Link></li>
        </ul>
      </nav>
    <Switch>
      <Route path="/" exact component={Home} />
      <Route path="/about/:name"  component={About} />
    </Switch>
    </main>
</Router>
  );
}

const About = () => {
  const { name } = useParams()
  return (
  // props.match.params.name
  <Fragment>
    { name !== 'John Doe' ? <Redirect to="/" /> : null }
    <h1>About {name}</h1>
    <Route component={Contact} />
  </Fragment>
)
};

```

### useLocation

This hook returns the location object that represents the current URL.

```jsx
import { useLocation } from "react-router-dom";

const Contact = () => {
const { pathname } = useLocation();

return (
  <Fragment>
    <h1>Contact</h1>
    <p>Current URL: {pathname}</p>
  </Fragment>
  )
  };

```

## Final Thoughts

React Router is an amazing library that helps us go from a single page to a multi-page application feeling with great usability. (Just keep in mind – at the end of the day, it's still a single page app). 

And now with router hooks, you can see how easy and elegant they are. They're definitely something to consider in your next project.

You can read more of my articles on [my blog](https://www.ibrahima-ndaw.com/blog/).

## Next Steps

[React Router Documentation](https://reacttraining.com/react-router/web)

Photo by [Joshua Sortino](https://unsplash.com/@sortino?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/route?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

