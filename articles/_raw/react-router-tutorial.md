---
title: React Router Tutorial – How to Render, Redirect, Switch, Link, and More, With
  Code Examples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-26T17:55:23.000Z'
originalURL: https://freecodecamp.org/news/react-router-tutorial
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ad1740569d1a4ca27f2.jpg
tags:
- name: React
  slug: react
- name: react router
  slug: react-router
- name: ' Single Page Applications '
  slug: single-page-applications
seo_title: null
seo_desc: "By Vijit Ail\nIf you have just started with React, you are probably still\
  \ wrapping your head around the whole Single Page Application concept. \nTraditionally\
  \ routing works like this: let's say you type in /contact in the URL. The browser\
  \ will make a G..."
---

By Vijit Ail

If you have just started with React, you are probably still wrapping your head around the whole Single Page Application concept. 

Traditionally routing works like this: let's say you type in `/contact` in the URL. The browser will make a GET request to the server, and the server will return an HTML page as the response. 

But, with the new Single Page Application paradigm, all the URL requests are served using the client-side code.

Applying this in the context of React, each page will be a React component. React-Router matches the URL and loads up the component for that particular page. 

Everything happens so fast, and seamlessly, that the user gets a native app-like experience on the browser. There is no flashy blank page in between route transitions.

In this article, you'll learn how to use React-Router and its components to create a Single Page Application. So open up your favorite text editor, and let's get started.

## Setup the project

Create a new React project by running the following command. 

```sh
yarn create react-app react-router-demo
```

I'll be using yarn to install the dependencies, but you can use npm as well.

Next, let's install `react-router-dom`.

```
yarn add react-router-dom
```

For styling the components, I'm going to use the Bulma CSS framework. So let's add that as well.

```
yarn add bulma
```

Next, import `bulma.min.css` in the `index.js` file and clean up all the boilerplate code from the `App.js` file.

```js
import "bulma/css/bulma.min.css";
```

Now that you have the project set up let's start by creating a few page components.

## Creating the Page Components

Create a pages directory inside the src folder where we will park all the page components.

For this demo, create three pages - Home, About, and Profile.

Paste the following inside the Home and About components.

```jsx
// pages/Home.js

import React from "react";

const Home = () => (
  <div>
    <h1 className="title is-1">This is the Home Page</h1>
    <p>
      Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras gravida,
      risus at dapibus aliquet, elit quam scelerisque tortor, nec accumsan eros
      nulla interdum justo. Pellentesque dignissim, sapien et congue rutrum,
      lorem tortor dapibus turpis, sit amet vestibulum eros mi et odio.
    </p>
  </div>
);

export default Home;

```

```jsx
// pages/About.js

import React from "react";

const About = () => (
  <div>
    <h1 className="title is-1">This is the About Page</h1>
    <p>
      Class aptent taciti sociosqu ad litora torquent per conubia nostra, per
      inceptos himenaeos. Vestibulum ante ipsum primis in faucibus orci luctus
      et ultrices posuere cubilia curae; Duis consequat nulla ac ex consequat,
      in efficitur arcu congue. Nam fermentum commodo egestas.
    </p>
  </div>
);

export default About;

```

We will create the Profile page later on in the article.

## Create the Navbar Component

Let's start by creating the navigation bar for our app. This component will make use of the `<NavLink />` component from `react-router-dom`.  
  
Create a directory called "components" inside the src folder.

```jsx
// components/Navbar.js

import React, { useState } from "react";
import { NavLink } from "react-router-dom";

const Navbar = () => {
  const [isOpen, setOpen] = useState(false);
  return ( 
  	<nav
      className="navbar is-primary"
      role="navigation"
      aria-label="main navigation"
    >
      <div className="container">
      	{/* ... */}
      </div>
    </nav>
  );
 };
 
 export default Navbar;
```

The `isOpen` state variable will be used to trigger the menu on mobile or tablet devices.

So let's add the hamburger menu.

```jsx
const Navbar = () => {
  const [isOpen, setOpen] = useState(false);
  return ( 
  	<nav
      className="navbar is-primary"
      role="navigation"
      aria-label="main navigation"
    >
      <div className="container">
      <div className="navbar-brand">
          <a
            role="button"
            className={`navbar-burger burger ${isOpen && "is-active"}`}
            aria-label="menu"
            aria-expanded="false"
            onClick={() => setOpen(!isOpen)}
          >
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
          </a>
        </div>
      	{/* ... */}
      </div>
    </nav>
  );
 };
```

To add the link in the menu, use the `<NavLink />` component by `react-router-dom`.

The `NavLink` component provides a declarative way to navigate around the application. It is similar to the `Link` component, except it can apply an active style to the link if it is active. 

To specify which route to navigate to, use the `to` prop and pass the path name.   
The `activeClassName` prop will add an active class to the link if it's currently active.

```jsx
<NavLink
    className="navbar-item"
    activeClassName="is-active"
    to="/"
    exact
>
	Home
</NavLink>
```

On the browser, the `NavLink` component is rendered as an `<a>` tag with an `href` attribute value that was passed in the `to` prop.

Also, here you need to specify the `exact` prop so that it is matched precisely with the URL.

Add all the links and finish up the `Navbar` component.

```jsx
import React, { useState } from "react";
import { NavLink } from "react-router-dom";

const Navbar = () => {
  const [isOpen, setOpen] = useState(false);
  return (
    <nav
      className="navbar is-primary"
      role="navigation"
      aria-label="main navigation"
    >
      <div className="container">
        <div className="navbar-brand">
          <a
            role="button"
            className={`navbar-burger burger ${isOpen && "is-active"}`}
            aria-label="menu"
            aria-expanded="false"
            onClick={() => setOpen(!isOpen)}
          >
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
          </a>
        </div>

        <div className={`navbar-menu ${isOpen && "is-active"}`}>
          <div className="navbar-start">
            <NavLink className="navbar-item" activeClassName="is-active" to="/">
              Home
            </NavLink>

            <NavLink
              className="navbar-item"
              activeClassName="is-active"
              to="/about"
            >
              About
            </NavLink>

            <NavLink
              className="navbar-item"
              activeClassName="is-active"
              to="/profile"
            >
              Profile
            </NavLink>
          </div>

          <div className="navbar-end">
            <div className="navbar-item">
              <div className="buttons">
                <a className="button is-white">Log in</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;

```

If you notice here, I've added a Login button. We will come back to the `Navbar` component again when we discuss protected routes later on in the guide.

## Rendering the pages

Now that the `Navbar` component is set up let's add that to the page and start with rendering the pages.

Since the navigation bar is a common component across all the pages, instead of calling the component in each page component, it will be a better approach to render the `Navbar` in a common layout.

```jsx
// App.js

function App() {
  return (
    <>
      <Navbar />
      <div className="container mt-2" style={{ marginTop: 40 }}>
        {/* Render the page here */}
      </div>
    </>
  );
}
```

Now, add the page components inside of the container.

```jsx
// App.js

function App() {
  return (
    <>
      <Navbar />
      <div className="container mt-2" style={{ marginTop: 40 }}>
        <Home />
      	<About />
      </div>
    </>
  );
}
```

If you check out the results now, you'll notice that both the Home and the About page component gets rendered onto the page. That's because we haven't added any routing logic yet.

You need to import the `BrowserRouter` component from React Router to add the ability to route the components. All you need to do is wrap all the page components inside of the `BrowserRouter` component. This will enable all the page components to have the routing logic. Perfect!

But again, nothing's going to change with the results – you are still going to see both the pages rendered. You need to render the page component only if the URL matches a particular path. That's where the `Route` component from React Router comes into play.

The `Router` component has a `path` prop that accepts the page's path, and the page component should be wrapped with the `Router`, as shown below.

```jsx
<Route path="/about">
  <About />
</Route>
```

So let's do the same for the `Home` component.

```jsx
<Route exact path="/">
  <Home />
</Route>
```

The `exact` prop above tells the `Router` component to match the path exactly. If you don't add the `exact` prop on the `/` path, it will match with all the routes starting with a `/` including `/about`.

If you go check out the results now, you'll still see both the components rendered. But, if you go to `/about`, you'll notice that only the `About` component gets rendered. You see this behavior because the router keeps matching the URL with the routes even after it had matched a route already. 

We need to tell the router to stop matching further once it matches a route. This is done using the `Switch` component from React Router.

```jsx
function App() {
  return (
    <BrowserRouter>
      <Navbar />
      <div className="container mt-2" style={{ marginTop: 40 }}>
        <Switch>
          <Route exact path="/">
            <Home />
          </Route>
          <Route path="/about">
            <About />
          </Route>
        </Switch>
      </div>
    </BrowserRouter>
  );
}
```

There you go! You have successfully configured routing in your React app. 

## Protected Routes and Redirect

When working on Real-world applications, you will have some routes behind an authentication system. You are going to have routes or pages that can only be accessed by a logged-in user. In this section, you'll learn how to go about implementing such routes.

**_Please note_** _that I'm not going to create any login form or have any back-end service authenticate the user. In a real application, you wouldn't implement authentication the way demonstrated here._

Let's create the Profile page component that should only be accessed by the authenticated user.

```jsx
// pages/Profile.js

import { useParams } from "react-router-dom";

const Profile = () => {
  const { name } = useParams();
  return (
    <div>
      <h1 className="title is-1">This is the Profile Page</h1>
      <article className="message is-dark" style={{ marginTop: 40 }}>
        <div className="message-header">
          <p>{name}</p>
        </div>
        <div className="message-body">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit.{" "}
          <strong>Pellentesque risus mi</strong>, tempus quis placerat ut, porta
          nec nulla. Vestibulum rhoncus ac ex sit amet fringilla. Nullam gravida
          purus diam, et dictum <a>felis venenatis</a> efficitur. Aenean ac{" "}
          <em>eleifend lacus</em>, in mollis lectus. Donec sodales, arcu et
          sollicitudin porttitor, tortor urna tempor ligula, id porttitor mi
          magna a neque. Donec dui urna, vehicula et sem eget, facilisis sodales
          sem.
        </div>
      </article>
    </div>
  );
};

```

We will grab the user's name from the URL using route parameters.

Add the Profile route into the router.

```jsx
<Route path="/profile/:name">
  <Profile />
</Route>
```

Currently the profile page can be accessed directly. So to make it an authenticated route, create a Higher-Order component (HOC) to wrap the authentication logic.

```jsx
const withAuth = (Component) => {
  const AuthRoute = () => {
    const isAuth = !!localStorage.getItem("token");
    // ...
  };

  return AuthRoute;
};
```

To determine if a user is authenticated or not, grab the authentication token that is stored in the browser when the user logs in. If the user is not authenticated, redirect the user to the Home page. The `Redirect` component from React Router can be used to redirect the user to another path.

```jsx
const withAuth = (Component) => {
  const AuthRoute = () => {
    const isAuth = !!localStorage.getItem("token");
    if (isAuth) {
      return <Component />;
    } else {
      return <Redirect to="/" />;
    }
  };

  return AuthRoute;
};
```

You can also pass in other user information like name and user ID using props to the wrapped component.

Next, use the `withAuth` HOC in the Profile component.

```jsx
import withAuth from "../components/withAuth";

const Profile = () => {
 // ...
}

export default withAuth(Profile);
```

Now, if you try to visit `/profile/JohnDoe`, you will get redirected to the Home page. That's because the authentication token is not yet set in your browser storage.

Alright, so, let's return to the `Navbar` component and add the login and logout functionalities. When the user is authenticated, show the Logout button and when the user is not logged in show the Login button. 

```jsx
// components/Navbar.js

const Navbar = () => {
	// ...
    return (
    	<nav
          className="navbar is-primary"
          role="navigation"
          aria-label="main navigation"
        >
        <div className="container">
        	{/* ... */}
            <div className="navbar-end">
            <div className="navbar-item">
              <div className="buttons">
                {!isAuth ? (
                  <button className="button is-white" onClick={loginUser}>
                    Log in
                  </button>
                ) : (
                  <button className="button is-black" onClick={logoutUser}>
                    Log out
                  </button>
                )}
              </div>
            </div>
          </div>
        </div>
        </nav>
    );
}


```

When the user clicks on the login button, set a dummy token in the local storage, and redirect the user to the profile page. 

But we cannot use the Redirect component in this case – we need to redirect the user programmatically. Sensitive tokens used for authentication are usually stored in cookies for security reasons.

React Router has a `withRouter` HOC that injects the `history` object in the props of the component to leverage the History API. It also passes the updated `match` and `location` props to the wrapped component.

```jsx
// components/Navbar.js

import { NavLink, withRouter } from "react-router-dom";

const Navbar = ({ history }) => { 
  const isAuth = !!localStorage.getItem("token");

  const loginUser = () => {
    localStorage.setItem("token", "some-login-token");
    history.push("/profile/Vijit");
  };

  const logoutUser = () => {
    localStorage.removeItem("token");
    history.push("/");
  };
  
  return ( 
   {/* ... */}
  );
};

export default withRouter(Navbar);
```

And _voilà_! That's it. You have conquered the land of authenticated routes as well.

Check out the live demo [here](https://react-router-demo.vijitail.dev/) and the complete code in this [repo](https://github.com/vijitail/react-router-demo) for your reference.

## Conclusion

I hope by now you have a fair idea of how client-side routing works in general and how to implement routing in React using the React Router library. 

In this guide, you learned about the vital components in React Router like `Route`, `withRouter`, `Link`, and so on, along with some advanced concepts like authenticated routes, that are required to build an application. 

Do check out the React Router [docs](https://reacttraining.com/react-router/web/guides/quick-start) to get a more detailed overview of each of the components.

