---
title: How to upgrade to React Router 4
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-01T22:00:00.000Z'
originalURL: https://freecodecamp.org/news/a-guide-to-upgrading-to-react-router-4
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/react-router-4-2.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: react router
  slug: react-router
- name: react-router-4
  slug: react-router-4
seo_title: null
seo_desc: "By Lekha Surasani\n\nNot long after I started working at my current position,\
  \ the team realized that it would be necessary for us to upgrade to React 16 so\
  \ we could use a new UI library we were keen on adopting. \nTo figure out how much\
  \ time this upgrad..."
---

By Lekha Surasani

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-82.png)

Not long after I started working at my current position, the team realized that it would be necessary for us to upgrade to React 16 so we could use a new UI library we were keen on adopting. 

To figure out how much time this upgrade would require, we looked at all of our current packages to see if they were compatible with React 16, and to see if we were still using unsupported or deprecated packages. 

The beginnings of our code base had been built by developers who used whatever open source or third party library they wanted, without actually vetting them. Thus, we found that a lot of the packages were deprecated and needed to be replaced ASAP. 

One of the biggest surprises for us was the deprecation of `react-router-redux`. We were using `react-router-redux` in conjunction with react-router v3. This led us to think critically about why we were using `redux` in our router in the first place. 

Once we started to look into react router v4, we realized that the new features would pretty much eliminate any reason for us to use an additional library to connect our router and `redux`. So, that left us in the position to just upgrade from react router 3 to 4, and remove  `react-router-redux` from our application.

So, I was tasked with upgrading our router to v4 after only being in the position and working with React for about 2 months. This was because upgrading from React Router 3 to React Router 4 sounded like it should be a trivial undertaking. But, as I quickly found out, it was a little bit more involved than I anticipated. 

Looking through the [documentation](https://reacttraining.com/react-router/web/guides/quick-start), the [GitHub repo](https://github.com/ReactTraining/react-router/), and many, many Stack Overflow answers, I finally pieced together the steps for the upgrade and wanted to share my findings — especially to explain how and why certain changes are made.

The biggest change to note, from the creators of React Router, is that the upgrade from React Router 3 to React Router 4 is more than just updating a few libraries and features — it allows you to fundamentally change how your Router works. The creators of React Router wanted to go back to a simple Router, allowing the developer to customize it however they would like.

I’ve split up this guide into 5 different parts:

1. Package
2. History
3. Route
4. Props
5. Redux Integration

---

# Package

React  Router v4 package structure changed such that it’s no longer necessary  to install react-router — you have to install `react-router-dom` (and  uninstall `react-router`), but you don’t lose anything since it re-exports  all of `react-router`’s exports. This means you also have to update any  `react-router` import statements to `react-router-dom`.

---

# History

History is an essential part of routing, allowing us to remember where we came from and where we are currently. History comes in many forms for react-router, and could take a while to explain. So, to keep this article on topic, I’ll simply recommend that you read through [this article](https://medium.com/@pshrmn/a-little-bit-of-history-f245306f48dd) that explains history in relation to react router 4. This article should cover most cases of your usage of history.

---

# Route

React Router v3 allowed us to place all of our application routes in one file, which we’ll call router.js. However, React Router v4 allows you to  place Routes in the components that they’re rendering. The idea here is to _dynamically route_ the application — in other words, the routing takes place as the app is rendering.

However,  if you have a decent-size legacy code base you’re working with, you probably won’t be making a change that big. Luckily, React Router v4  still allows you to place all the routes in a central file, which is how I’ll create all of our examples. There are, however, a few older components and features that will need replacing.

## IndexRoute

Previously,  `IndexRoute` was used as a route for some default UI of a parent Route. But, in v4, `IndexRoute` is no longer used, since this functionality is  now available in Route.

For providing default UI, multiple Routes that have the same path will let all of the associated components render:

```
import { BrowserRouter as Router, Route } from 'react-router-dom';

<Router>
    // example of our route components
    <Route path="/" component={Home} />
    <Route path="/" component={About} />
    <Route path="/" component={Contact} />
</Router>
```

So, all of the Components — `Home`, `About`, and `Contact` — will render. Because of this, you can no longer nest Routes, either.

Additionally, to allow for better matching without the use of `IndexRoute`, you can use the exact keyword.

```javascript
import { BrowserRouter as Router, Route } from 'react-router-dom';

<Router>
    // example of our route components
    <Route exact path="/" component={Home} />
    <Route path="/about" component={About} />
</Router>
```

## Exclusive Routing

After adding in the exact keyword, `“something.com/about”` will be routed to  when the router sees a path `“/about”`. But now what if you have another  path, `“/about/team”`? As I stated before, the router will render anything  that matches. So, the components associated with both `“/about”` and  `“/about/team”` will render. If that’s what you intended, then that’s great! However, if this isn’t what you want, you may have to put a  Switch around this group of Routes. This will allow the first path that  matches the URL to render.

```javascript
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

<Router>
    <Switch>
       <Route exact path ="/" component={Home} />
       <Route path="/about/team" component={Team} />
       <Route path="/about" component={About} />
    </Switch>
</Router>
```

Note  that the keyword exact still has to appear for the Home component —  otherwise it would match for the subsequent routes. Also note that we  have to list `“/about/team”` before `“/about”` so the route goes to the `Team` component instead of the `About` component when it sees  `“something.com/about/team”`. If it saw `“/about”` first, it would stop  there and render the `About` component because Switch only renders the  first component that matches.

## Default Route

A default route, or a “catch all” route, commonly used for 404 pages, is the route you use when none of the routes match.

In React Router v3, a default `Route` was:

`<Route path=”*” component={NotFound} />`

In React Router v4, the default `Route` was changed to:

```
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

<Router>
    <Switch>
       <Route exact path ="/" component={Home} />
       <Route path="/about/team" component={Team} />
       <Route path="/about" component={About} />
       <Route component={NotFound} /> // this is our default route
    </Switch>
</Router>
```

When  you don’t include a path in a `Route`, the component will always render.  So, as we discussed above, we can use `Switch` to get only one component  to render, and then place the “catch all” route very last (so it doesn’t  use that one before the `Router` gets a chance to check the rest of the  paths), so something will always render even if the other paths don’t  match.

## onEnter

Previously,  you could use `onEnter` to make sure the component of the `Route` has all  of the information it needs or as a check (such as to make sure the user  is authenticated) before the component rendered.

This  feature has been deprecated because the new structure of Routes is that  they should act like components, so you should take advantage of component lifecycle methods instead.

In React Router v3:

`<Route path=”/about” onEnter={fetchedInfo} component={Team}/>`

Becomes:

```
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

<Router>
    <Switch>
       <Route exact path ="/" component={Home} />
       <Route path="/about/team" component={Team} />
       <Route path="/about" component={About} />
       <Route component={NotFound} />
    </Switch>
</Router>
```

```
...

componentDidMount() {
    this.props.fetchInfo();
}

...
```

---

# Props

In  React Router v4, the props passed through the router have changed, as  did the way they are accessed. The Route now passes three props:

* `history`
* `location`
* `match`

## history

`history` contains a lot of other properties and methods, so I won’t list all of  them, but here is a selection that might be most commonly used:

* `length`: number of entries in the history stack
* `location`: contains the same information as below
* `push(path, [state])`: pushes new entry on history stack
* `goBack()`: allows you to move the pointer on the history stack back 1 entry

It’s  important to note that `history` is mutable, and while it contains a `location` property, this instance of `location` shouldn’t be used since it  could have been changed. Instead, you want to use the actual `location` prop discussed below.

## location

The location has properties:

* `pathname`
* `search`
* `hash`
* `state`

`location.search` is used to replace `location.query` and it must be parsed. I used  `URLSearchParams` to parse it. So a URL such as  `“https://something.com/about?string=’hello’”` would be parsed as such:

```
...

const query = new URLSearchParams(this.props.location.search)
const string = query.get('string') // string = 'hello'

...
```

Additionally,  the `state` property can be used to pass the `location`-specific `state` of components through props. So, if you wanted to pass some information  from one component to another, you could use it like this:

```
...
// To link to another component, we could do this:
<Link to='/path/' />

// However, if we wanted to add state to the location, we could do this:
const location = {
    pathname: '/path/',
    state: { fromDashboard: true },
}
<Link to={location} />
...
```

So, once we get to the component rendered by that path, we’ll have access to `fromDashboard` from `location.state.fromDashboard`.

## match

`match` has the following properties:

* `params`:  gets the dynamic segments of the path from the URL — for example if the  path is `“/about/:id”`, in the component, accessing  `this.props.match.params` will give you the id in the URL
* `isExact`: true if the entire URL was matched
* `path`: the path in the routes that was matched
* `url`: the matched portion of the URL

# Redux Integration

As  I addressed earlier, we found that in our case, we didn’t need to have an additional library to connect `redux` with our router, especially since our main use case for this — Blocked Updates — was covered by react  router.

## Blocked Updates

In  some cases, the app doesn’t update when the location changes. This is called a “Blocked Update”. This can happen if both of these conditions  are met:

1. The component is connected to Redux via `connect()(Component)`.
2. The component isn’t rendered by a `<Route>`

In these cases, I wrapped the component’s connect with `withRouter`.

This  allowed the router information to follow the component when it gets linked to, so the app still updates when the Redux state changes.

---

And that’s it!

This upgrade took me over a week — a few days of trying to figure out how to do it at all, and then another few days to start actually making changes. Upgrading to React Router 4 is a huge change not to be taken lightly, but it’ll make your router a lot more lightweight and easy to use.

Please don’t hesitate to comment/ask questions!

