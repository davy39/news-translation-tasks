---
title: A bluffer’s guide to React Router v4
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-08T16:29:41.000Z'
originalURL: https://freecodecamp.org/news/bluffers-guide-to-react-router-v4-20f607a10478
coverImage: https://cdn-media-1.freecodecamp.org/images/1*4Lf1qdyphgejovy6uvWWRw.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: React
  slug: react
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Greg Byrne

  In this article, we''ll cover the important things you can quickly learn to be informed
  and confident with using and conversing on React Router v4.

  What is React Router?

  React Router is a client-side router (CSR) for use with React proje...'
---

By Greg Byrne

In this article, we'll cover the important things you can quickly learn to be informed and confident with using and conversing on React Router v4.

## What is React Router?

React Router is a client-side router (CSR) for use with React projects (_I know, duh right?_). It provides _routing_ which is the fancy term for the rendering of different components depending on URL paths within a React web application.

## How does one install and use?

Run the following command in your project to save `react-router-dom` as a project dependency:

```
npm i -S react-router-dom
```

Using the ES2015 syntax, you can import React Router into your React components using:

```
import * from 'react-router-dom'
```

### Setting up your basic routes

`Link` components can be thought of as your typical anchor links that, when clicked, redirect the user to the path specified in its `to` property.

`Route` components can be thought of as the controller for the render. When you see these components, just think this is what they say:

WHEN _I see the URL as what is specified in my_ `path` _property,_ THEN _I will render the component listed in my_ `component` _or_ `render` _property._

The basic example below is mostly lifted from [ReactTraining’s basic example](https://reacttraining.com/react-router/web/example/basic):

### Nesting Routes

Nesting routes is exactly the same as creating high-level routes, except for defining a `BrowserRouter` component (as your nested routes are composed within the high-level `BrowserRouter` component anyway). It simply needs more `Link` and `Route` components. We can indefinitely nest further routes within any other nested routes.

### Passing URL parameters

In the previous example, we had different components defined for each topic in nested routes. In the following example, we have a single `Topic` component that is rendered for the three different routes. The `Topic` component dynamically renders the `topicId`, which is passed as a property by the `Route`, and its value defined as part of the URL using the `:`.

When a `Route` defines a component to render, it passes a `match` object to its props (along with `location` and `history`, but unimportant for now). This `match` object has a `params` object which contains any variables passed by `Route` defined using the `:` notation in the `path` URL (aka Route Parameter).

In this way, we can cut down on separately creating components for each `Link` and instead make one re-usable component rendered with the information passed to it.

### Avoiding hard-coding nested links

When creating nested links, our `Link` component still needs to refer to the entire URL path instead of the location it’s really concerned with. This means that nested links would have hard-coded locations to its parent links, which isn’t great when a name change occurs and a big renaming effort is required.

Instead, using the `match` object passed by `Route`, we can dynamically refer to it’s location and use that to avoid hard-coding.

For example:  
`<Route path="/topics" component={Topics`}/> pas`ses a` match object w`ith` a url property with the `value "/t`opi`cs" .` Topics , via its props, can reus`e the mat`ch.url when defining its nested links.

### Avoiding ambiguous matches

By default, when you specify `Route` components, _each matching path will be rendered inclusively_. Using URL parameters, this becomes problematic. As the parameter effectively acts as a wildcard (so any text is found as matching), you will find that when these are mixed with hard-coded routes, they both will display. Using `exact` won’t help either.

React Router’s solution is the `Switch` component. The `Switch` component will render the child `Route` component on the _first matching path exclusively_. This means that if all hard-coded routes are specified first, then these will be rendered only.

### Multiple Route Rendering

There are times when you don’t want ambiguous matching of `Route` components, but there will be times when you do.

Remembering that we can think of `Route` as a simple “_WHEN I see this path, THEN render this component_”, which means we can have multiple `Route` components matching a single page, but providing different content.

In the below example, we use one component to pass the URL parameter to show the user their current path, and another component that renders with the content component. That means two different components are rendered for the one URL path.

### Rendering from Route directly

A `Route` component can be passed a `component` to render if one is available. It can also render a component directly using the `render` property.

```
<Route exact path={url} render={  () => <h3>Please select a topic</h3>} />
```

### Passing properties to a component using Route

URL passed parameters are fine, but what about passing in properties that require more data to components, such as objects? `Route` doesn’t allow you to append properties it doesn’t recognize.

```
<Route exact path="/" component={Home} doSomething={() => "doSomething" } /> // doesn't work
```

However what can be done to pass properties is to use `Route` _render_ method.

```
<Route exact path="/" render={(props) => <Home {...props} doSomething={() => "doSomething"} />
```

### Passing properties to a component using Link

You can also pass properties to a component via the `Link` component. Instead of passing in a String to the `to` property, we can pass in an object instead. On this object, we can declare the `pathname` representing to URL we want to navigate to. We also declare a `state` object that contains any custom properties we want. These properties are contained on the `location` object (in `location.state`).

In the below example (_contrived, I know…_), we pass in a message property to display on a page.

### Redirection — Using Redirect

You can use the `Redirect` component to redirect the users’ immediate URL to another.

In the below example, we see a redirect for a user depending on whether the `isAuthenticated` state on component `RedirectExample` is true or false, appropriately redirecting if they’re logged in (to _/home_) or logged out (to _/dashboard_):

### Redirection — Using withRouter()

Another way to redirect is by using the higher-order component `withRouter`. This allows you to pass the properties of `Route` (`match`, `location`, and importantly in this example `history`) to components that _aren’t_ rendered via the typical `Route` component. We do this by _wrapping_ our exported component with the `withRouter`.

Why is having `history` important? We can use `history` to force redirection by pushing a URL to the `history` object.

There are caveats to this way of routing which I don’t detail (see the [withRouter documentation](https://reacttraining.com/react-router/web/api/withRouter)). Also, the exported component must still be composed within another component that is rendering within`BrowserRouter` (which I don’t show in this example).

### Default Route Component

There will be times when a `Link` may refer to a URL that has no corresponding `<Route path='/something' component={Something`}/> . Or a user will type an incorrect URL in the browser bar.

When that happens, all we will have is a non-responsive page or link where nothing happens (which is not as bad as actually being navigated to a non-existent page).

Most times we want to at least show the user we can’t find their content, maybe with a witty image like [Github’s 404 page](https://github.com/non-existing-page). In this case, you’ll want a default component, also known as a no-match or catch-all component.

When a user clicks a link (or indeed types something incorrectly in the browser navigation bar), so long as there are no other matching components, we will be directed to the default component to be rendered.

Note the use of `Switch` (ambiguous matching with URL parameters). As this `Route` has no path, it will be effectively always rendered. We require a `Switch` to only render if it cannot find any other matching `Route` path’s.

### Custom Links

The `Link` component at its core renders an anchor element for whatever is passed as its `to` property. There are times when we would want customizations made to the Link component without having to have these customizations everywhere. React Router allows a means of doing this is by creating a custom link (see [React Router training guid](https://reacttraining.com/react-router/web/example/custom-link)e for more info — we use their example more or less below).

For a custom link, one is essentially wrapping the existing `Link` component inside a custom component, and providing additional information, not unlike the [Higher Order Component pattern](https://reactjs.org/docs/higher-order-components.html).

In our example, we only show the links for the pages that aren’t displayed. For our `CustomLink` component to have the knowledge of what page is currently displayed, we need to wrap the `Link` component in a `Route` component so that we can pass the `match` object that comes with React Router’s `Route`. We pass this wrapping our `Link` component as a child to the `Route` component.

Route, if you remember, simply checks the current path and when we match, will render “something” (either defined by the `component`/`render` properties or as as a child of `Route` — such as our Link component).

We subvert this slightly with an equality check to say if we don’t find a `match` object (if our current path doesn’t match what’s defined in the `path` property in the `Route` declared in `CustomLink`), then render a `Link`, otherwise render nothing.

### Parsing Query Strings

Query strings are parameters in the URL that look like variables and are prefixed by the question mark (such as `www.example.com/search?name=Greg` ).

I’m going to rip the band-aid off quick — React Router doesn’t come with a way to parse query strings ?. It does, however, locate query strings as a String in its passed properties, within l`ocation.search,` wherein the above example would be defined as s`earch: "?name=Greg".`

So what to do? There are a number of ways to solve this problem, including reinventing the wheel. I would like to anecdotally highlight the npm package [query string](https://www.npmjs.com/package/query-string) as a solution which I’ve used and has become my de facto query string parser.

### Prompting users when transitioning

React Router v4 comes with a `Prompt` component, which as you can guess, displays a prompt to the user. This is useful as UX feature for users when they are warned of potentially losing form data if they transition from the current form page.

The basic pattern in implementing a navigational prompt is to have a boolean state property which decides whether they should be prompted or not. This state is updated via the form based on whether there are values selected for any form field. Within the form, you render a `Prompt` component, passing in two properties: a `when` (which is your boolean state set earlier) and a `message` to display.

Below is an example (it mostly follows the example from [ReactTraining prevent transitions](https://reacttraining.com/react-router/web/example/preventing-transitions)):

## Summary

In the article, you will have learned all the basics to use React Router in your web applications. You should be even able to converse with your many friends and family about the joys of React Routing.

> If you liked this article, please share your like with a friendly clap.

> If you didn’t like this article and would like to register your resentment, you can do so by giving a hateful clap.

> _The **opinions expressed** in this publication are those of the author. They do not purport to reflect the **opinions** or views of any organization or business that the author may be connected to._

