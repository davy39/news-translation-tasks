---
title: Learn React Router in 5 Minutes - A Beginner's Tutorial
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-11T19:30:00.000Z'
originalURL: https://freecodecamp.org/news/react-router-in-5-minutes
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f69740569d1a4ca4284.jpg
tags:
- name: React
  slug: react
- name: react router
  slug: react-router
- name: Tutorial
  slug: tutorial
seo_title: null
seo_desc: 'By Bob Ziroll

  Sometimes you''ve only got 5 minutes to spare. Instead of wasting it on social media,
  let''s get a 5-minute introduction to React-Router! In this tutorial, we''re going
  to learn the basics of routing in React by building navigation for a S...'
---

By Bob Ziroll

Sometimes you've only got 5 minutes to spare. Instead of wasting it on social media, let's get a 5-minute introduction to React-Router! In this tutorial, we're going to learn the basics of routing in React by building navigation for a Scrimba knitting shop website. It's not real, but maybe one day... ;)

If you want a proper introduction to this subject, you can join the waitlist for my [upcoming advanced React course](https://scrimba.com/g/greact?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=router_article), or if you're still a beginner, check out my [introductory course on React.](https://scrimba.com/g/glearnreact?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=router_article)

### What is React-Router, anyway?

Many modern websites are actually made up of a single page, they just look like multiple pages because they contain components which render like separate pages. These are usually referred to as SPAs - **s**ingle-**p**age **a**pplications. At its core, what React Router does is conditionally render certain components to display depending on the *route* being used in the URL (`/` for the home page, `/about` for the about page, etc.).

For example, we can use React Router to connect _www.knit-with-scrimba.com/_ to _www.knit-with-scrimba.com/about_ or _www.knit-with-scrimba.com/shop_

### Sounds great - how do I use it?

To use React Router, you first have to install it using NPM:

```bash
npm install react-router-dom
```

Alternatively, you can just use [this playground in Scrimba](https://scrimba.com/c/cNq8MzCr), which has the completed code already written.

You'll need to import BrowserRouter, Route, and Switch from `react-router-dom` package:

```js
import React, { Component } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
```

In my example, I link the landing page with two other "pages" (which are actually just components) called `Shop` and `About`.

First, you'll need to set up your app to work with React Router. Everything that gets rendered will need to go inside the `<BrowserRouter>` element, so wrap your App in those first. It's the component that does all the logic of displaying various components that you provide it with.

```js
// index.js
ReactDOM.render(
    <BrowserRouter>
        <App />
    </BrowserRouter>, 
    document.getElementById('root')
)
```

Next, in your App component, add the `Switch` element (open and closing tags). These ensure that only one component is rendered at a time. If we don't use this, we can default to the `Error` component, which we're going to write later.

```js
function App() {
    return (
        <main>
            <Switch>
                
            </Switch>
        </main>
    )
}
```

It's now time to add your `<Route>` tags. These are the links between the components and should be placed inside the `<Switch>` tags.

To tell the `<Route>` tags which component to load, simply add a `path` attribute and the name of the component you want to load with `component` attribute.

```js
<Route path='/' component={Home} />
```

Many homepage URLs are the site name followed by `"/"`, for example, _www.knit-with-scrimba.com/_. In this case, we add `exact` to the Route tag. This is because the other URLs also contain "/", so if we don't tell the app that it needs to look for just `/`, it loads the first one to match the route, and we get a pretty tricky bug to deal with.

```js
function App() {
    return (
        <main>
            <Switch>
                <Route path="/" component={Home} exact />
                <Route path="/about" component={About} />
                <Route path="/shop" component={Shop} />
            </Switch>
        </main>
    )
}
```

Now import the components into the app. You may wish to have them in a separate "components" folder to keep code clean and readable.

```js
import Home from './components/Home';
import About from './components/About';
import Shop from './components/Shop';
```

Onto that error message I mentioned earlier, which loads if a user types an incorrect URL. This is just like a normal `<Route>` tag, but with no path. The Error component contains `<h1>Oops! Page not found!</h1>`. Don't forget to import it into the app.

```js
function App() {
    return (
        <main>
            <Switch>
                <Route path="/" component={Home} exact />
                <Route path="/about" component={About} />
                <Route path="/shop" component={Shop} />
                <Route component={Error} />
            </Switch>
        </main>
    )
}
```

So far, our site is only navigable by typing the URLs. To add clickable links to the site, we use the `Link` element from React Router and set up a new `Navbar` component. Once again, don't forget to import the new component into the app.

Now add a `Link` for each component in the app and use `to="URL"` to link them.

```js
function Navbar() {
  return (
    <div>
      <Link to="/">Home </Link>
      <Link to="/about">About Us </Link>
      <Link to="/shop">Shop Now </Link>
    </div>
  );
};
```

Your site now has clickable links that can navigate you around your single-page app!

### Conclusion
So there we have it. If you want to easily navigate around a React app, forget the anchor tags and add React Router. It's clean, it's organized, and it makes adding and deleting pages a whole lot easier.

To learn more about React Hooks and other great features of React, you can join the waitlist for my [upcoming advanced React course.](https://scrimba.com/g/greact?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=router_article) 

Or if you're looking for something more beginner friendly, you can check out my [introductory course on React.](https://scrimba.com/g/greact?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=router_article)

Happy coding ;)



