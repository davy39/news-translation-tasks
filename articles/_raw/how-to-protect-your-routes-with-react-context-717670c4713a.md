---
title: How to protect your routes with React Context
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-19T20:22:09.000Z'
originalURL: https://freecodecamp.org/news/how-to-protect-your-routes-with-react-context-717670c4713a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*wmwNRYeBumNlEKriJxLHjg.jpeg
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
seo_desc: 'By paul christophe

  Among the changes in React 16.3 is a new stable version of the Context API. We’re
  going to take a look at how it works by building a protected route component.

  What is Context?

  Context is about encapsulating state. It allows us to ...'
---

By paul christophe

Among the changes in [React 16.3](https://reactjs.org/blog/2018/03/29/react-v-16-3.html) is a new stable version of the **Context API**. We’re going to take a look at how it works by building a **protected route component**.

#### What is Context?

Context is about encapsulating state. It allows us to pass data from a parent provider component to any subscribed component down the tree. Without state management we often have to “drill” props through every component along the way.

#### Isn’t that what Redux is for?

**Yes**, Context operates similarly to how components can connect to Redux’s global state. However, a native element like Context will often be a better solution for small to medium apps that don’t need the complex overhead of Redux.

#### Basic Concepts

There are three elements to Context:

* `createContext` — Calling this returns a pair of components, `Provider` and `Consumer`.
* `Provider` — a Component that allows for one or more `Consumers` to subscribe to changes.
* `Consumer` —a Component subscribed to a Provider

### Let’s Start Building

We’re going to build an app with **two** routes. One is **a landing page** with global access. The other is **a dashboard page** with restricted access for logged in users. You can find the [final version here](https://codesandbox.io/s/p71pr7jn50).

> _Try it out: go to /dashboard while logged out. Log in and navigate freely between routes. From the dashboard, log out and it’ll kick you out to the landing page._

#### Context Header

To demonstrate Context’s basic functionality, let’s start by building a header component that lets us log in and out. First, create our context in a new file.

```
/* AuthContext.js */
```

```
import React from 'react';
```

```
const AuthContext = React.createContext();
```

Export a component `AuthProvider` to define our state (whether the user is logged in) and pass its state to the `value` prop on the `Provider`. We’ll simply expose `AuthConsumer` with a meaningful name.

```
/* AuthContext.js */
```

```
...
```

```
class AuthProvider extends React.Component {  state = { isAuth: false }
```

```
  render() {    return (      <AuthContext.Provider        value={{ isAuth: this.state.isAuth }}      >        {this.props.children}      </AuthContext.Provider>    )  }}
```

```
const AuthConsumer = AuthContext.Consumer
```

```
export { AuthProvider, AuthConsumer }
```

In index.js, wrap our app in `AuthProvider`.

```
/* index.js */import React from 'react';import { render } from 'react-dom';import { AuthProvider } from './AuthContext';import Header from './Header';
```

```
const App = () => (  <;div>    <AuthProvider>      <Header />    </AuthProvider>  </div>);
```

```
render(<App />, document.getElementById('root'));
```

Now create our `Header` and import our `AuthConsumer` (I’m leaving styling out for clarity).

```
/* Header.js */import React from 'react'import { AuthConsumer } from './AuthContext'import { Link } from 'react-router-dom'
```

```
export default () => (  <header>    <AuthConsumer>    </AuthConsumer>  </header>)
```

Context Consumers must have a **function as their direct child.** This will be passed the value from our `Provider`.

```
/* Header.js */...export default () => (  <header>    <AuthConsumer>
```

```
      {({ isAuth }) => (        <div>          <h3>            <Link to="/">              HOME            &lt;/Link>          </h3>
```

```
          {isAuth ? (            <ul>              <Link to="/dashboard">                Dashboard              </Link>              <button>                logout              </button>            </ul>          ) : (            <button>login</button>          )}        </div>      )}
```

```
    </AuthConsumer>  </header>)
```

Because `isAuth` is set to false, only the login button will be visible. Try changing the value to `true` (it’ll switch to the logout button).

Ok, let’s try switching `isAuth` in code. We’ll pass a login and logout function from our `Provider`.

```
/* AuthContext.js */...class AuthProvider extends React.Component {  state = { isAuth: false }
```

```
  constructor() {    super()    this.login = this.login.bind(this)    this.logout = this.logout.bind(this)  }
```

```
  login() {    // setting timeout to mimic an async login    setTimeout(() => this.setState({ isAuth: true }), 1000)  }
```

```
  logout() {    this.setState({ isAuth: false })  }
```

```
  render() {    return (      <AuthContext.Provider        value={{          isAuth: this.state.isAuth,          login: this.login,          logout: this.logout        }}      >        {this.props.children}      </AuthContext.Provider>    )  }}
```

These functions will allow us to toggle our auth state in `Header`.

```
/* Header.js */...export default () => (  <header>    <AuthConsumer>      {({ isAuth, login, logout }) => (        <div>          <h3>            <Link to="/">              HOME            </Link>          </h3>
```

```
          {isAuth ? (            <ul>              <Link to="/dashboard">                Dashboard              </Link>              <button onClick={logout}>                logout              </button>            </ul>          ) : (            <button onClick={login}>login</button>          )}        </div>      )}    </AuthConsumer>  </header>)
```

### Protected Route With Context

Now that we have covered the basics, let’s extend what we’ve learned to create a protected route component.

First make `Landing` and `Dashboard` page components. Our dashboard will only be visible when the user is logged in. Both pages will be as simple, as below:

```
/* Dashboard.js */import React from 'react'
```

```
const Dashboard = () => <h2>User Dashboard</h2>
```

```
export default Dashboard
```

Now let’s route to these pages.

```
/* index.js */import React from 'react';import { render } from 'react-dom';import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';import { AuthProvider } from './AuthContext';import Landing from './Landing';import Dashboard from './Dashboard';import Header from './Header';
```

```
const App = () => (  <;div>    <Router>      <AuthProvider>;        <Header />        <Switch>          <Route path="/dashboard" component={Dashboard} />          <Route path="/" component={Landing} />        &lt;/Switch>      </AuthProvider>    </Router>  </div>);
```

```
render(<App />, document.getElementById('root'));
```

In this current state you can navigate to both `/` and `/dashboard`. We’ll make a special route component that checks if a user is logged in called `ProtectedRoute`. The set up is similar to our `Header` component.

```
/* ProtectedRoute.js */import React from 'react';import { Route, Redirect } from 'react-router-dom';import { AuthConsumer } from './AuthContext';
```

```
const ProtectedRoute = () => (  <AuthConsumer>    {({ isAuth }) => (
```

```
    )}  </AuthConsumer&gt;);
```

```
export default ProtectedRoute;
```

The private route will function just like a regular `react-router` route, so we’ll expose the component and any other props passed to it.

```
const ProtectedRoute = ({ component: Component, ...rest }) => (
```

Now the interesting part: we’ll use the `isAuth` variable to determine if it should redirect or render the protected route’s component.

```
const ProtectedRoute = ({ component: Component, ...rest }) => (  <AuthConsumer>    {({ isAuth }) => (      <Route        render={          props =>            isAuth             ? <Component {...props} />             : <Redirect to="/" />        }        {...rest}      />    )}  </AuthConsumer>)
```

In our `index` file let’s import `ProtectedRoute` and use it on our dashboard route.

```
/* index.js */...
```

```
  <ProtectedRoute path="/dashboard" component={Dashboard} />
```

Awesome, now we have protected routes! Try pointing the browser to `/dashboard` and watch it kick you back to the landing page.

Again, here’s the link for the [working demo](https://codesandbox.io/s/p71pr7jn50). Read more about Context from [React’s Official Docs](https://reactjs.org/docs/context.html).

