---
title: Imagine React Router as your switchboard operator
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-11T19:04:43.000Z'
originalURL: https://freecodecamp.org/news/imagine-react-router-as-your-switchboard-operator-f4f1ac22188c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*MfOaLBtqjvchvWlqk6Z6Hw.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Jay Papisan

  Like an old-school telephone switchboard, React Router is a smooth, behind-the-scenes
  operator for your single page (SPA) React application. Users click a link, the URL
  changes, views change and for all they know they’ve moved on to an...'
---

By Jay Papisan

Like an old-school telephone switchboard, React Router is a smooth, behind-the-scenes operator for your single page (SPA) React application. Users click a link, the URL changes, views change and for all they know they’ve moved on to another page — except they haven’t. React Router is a key tool for giving your SPA the feel of a multi-page application while maintaining the quick rendering of React’s virtual DOM.

Let’s go through the basic components of using React Router to set up simple navigation. For a web application, you’ll run `yarn add react-router-dom`. There are many ways to spread your router components, but for explanation’s sake we’ll go with the following to illustrate needed component hierarchy. We’ll run through each of the bolded components below — **Provider, BrowserRouter, Switch** and **Route**.

```
import React from 'react';import ReactDOM from 'react-dom';import { Provider } from 'react-redux';import { createStore, applyMiddleware } from 'redux';import { BrowserRouter, Route, Switch } from 'react-router-dom';import promise from 'redux-promise';import { PostsNew, PostsShow, PostsIndex } from './components'
```

```
const createStoreWithMiddleware = applyMiddleware(promise)(createStore);
```

```
ReactDOM.render( &lt;Provider store={createStoreWithMiddleware(reducers)}&gt;  <BrowserRouter>   <div>    &lt;Switch>     <Route path="/posts/new" component={ PostsNew } />     <Route path="/posts/:id" component={ PostsShow } />     <Route path="/" component={ PostsIndex } />    </Switch>   </div>  </BrowserRouter> </Provider>, document.getElementById('root'));
```

### Operator…aka <Provider />

So what if your call got dropped and you need to try again _(page reload)_? Want to go back and call your last friend _(browser back)_? No problem, the operator — aka `Provider` has you covered. It uses the power of Redux’s `store` to hold all of your browsing history. Think of it as the ease-dropping operator (and **parent component**) of all your React Router components.

```
<Provider store={createStoreWithMiddleware(reducers)}>
```

### Phone or telegraph?…aka <BrowserRouter />

You can’t make a telephone call with a telegraph. Similarly, you need the correct router for native vs web. For most web apps, importing `BrowserRouter` , which works on HTML5 browsers, will do the trick.

### Who?..…aka <Switch />

Your operator is lazy…they run their finger down the phone book and call the first person that matches. Assuming you only want to render one component per URL, `Switch` allows exclusive rendering (by regex match behind the scenes). Careful how you order them — place the most specific first and generic last.

For example, don’t put `path="/"` first or you’ll never leave home…

```
&lt;Switch&gt;  <Route path="/posts/new" component={ PostsNew } /&gt;  <Route path="/posts/:id" component={ PostsShow } />  <Route path="/" component={ PostsIndex } /> </Switch>
```

### Phone number….aka <Route />

Did switchboard operators use phone numbers? Whatever…the `Route` component renders the specific component you set to match a URL. Notice below the `:id` —using the power of React Router’s [match object](https://reacttraining.com/react-router/core/api/match), anything after the `:` is accessible within your rendered component, for example as: `this.props.match.params.id`

```
&lt;Route path="/posts/:id" component={ PostsShow } />
```

### Redirect call…aka <Link />

This call is getting redundant, let’s quickly call someone else or back home. With React Router’s `Link` component (a fancy wrapper for an HTML anchor tag), you can drop in a link just like you would a home button or anchor tags through your components. Just put your destination in the `to` field and style as you would in-line or add a button wrapper.

```
import { Link } from 'react-router-dom';
```

```
class YourThing extends Component {   render() {     return(       <div>        <Link to="/"> Home </Link>       </div>     )   }}
```

That’s it for a few very basics, though there is much more available. Check out the excellent [docs](https://reacttraining.com/react-router/) and tutorials for the infinite ways to customize your routes. Thanks for reading my second Medium post. Give me some comments, corrections, or claps if this was helpful.

