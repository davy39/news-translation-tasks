---
title: How to implement server-side rendering in your React app in three simple steps
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-29T11:41:00.000Z'
originalURL: https://freecodecamp.org/news/server-side-rendering-your-react-app-in-three-simple-steps-7a82b95db82e
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c5d740569d1a4ca31bc.jpg
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: progressive web app
  slug: progressive-web-app
- name: React
  slug: react
seo_title: null
seo_desc: 'By Rohit Kumar

  Here’s what we will build in this tutorial: a nice React card like this one.


  In this tutorial, we’ll use server-side rendering to deliver an HTML response when
  a user or crawler hits a page URL. We’ll handle the latter requests on the...'
---

![Image](https://www.freecodecamp.org/news/content/images/2020/03/1_wk04sWGQkw36_XLFvPACrA-1.png)

By Rohit Kumar

Here’s what we will build in this tutorial: a nice React card like this one.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/1_wk04sWGQkw36_XLFvPACrA-1.png)

In this tutorial, we’ll use server-side rendering to deliver an HTML response when a user or crawler hits a page URL. We’ll handle the latter requests on the client side.

Why do we need it?

Let me guide you to the answer.

## What’s the difference between client-side rendering and server-side rendering?

In **Client-side rendering,** your browser downloads a minimal HTML page. It renders the JavaScript and fills the content into it.

**Server-side rendering,** on the other hand, renders the React components on the server. The output is HTML content.

You can combine these two to create an isomorphic app.

## Cons of Rendering React on the Server

* SSR can improve performance if your application is small. But it can also degrade performance if it is heavy.
* It increases response time (and it can be worse if the server is busy).
* It increases response size, which means the page takes longer to load.
* It increases the complexity of the application.

## When should you use Server Side Rendering?

Despite these consequences of SSR, there are some situations in which you can and should use it.

### 1. SEO

Every website wants to appear in searches. Correct me if I’m wrong.

Unfortunately, Search engine crawlers do not yet understand/render JavaScript.

This means they see a blank page, no matter how helpful your site is.

Many folks say that Google’s crawler [now renders JavaScript](https://www.searchenginejournal.com/googles-search-crawlers-natively-render-javascript-based-pages/226313/).

To test this, I deployed the app on Heroku. Here is what I saw on the Google Search Console:

![Image](https://cdn-media-1.freecodecamp.org/images/1*KgOtUd6XBbeZvR1FDBGcXA.png)
_Google’s crawler does not render React_

A blank page.

This was the biggest reason I explored server-side rendering. Especially when it is a [cornerstone page](https://yoast.com/what-is-cornerstone-content/) such as a landing page, blog, and so on.

To verify if Google renders your site, visit:

Search Console Dashboard > Crawl > Fetch as Google. Enter the page URL or leave it empty for the homepage.

Select FETCH AND RENDER. Once complete, click to see the result.

### 2. Improve performance

In SSR, the application performance depends on the server’s resources and user’s network speed. This makes it very useful for content-heavy sites.

_For Example_, say that you have a medium-price mobile phone with slow internet speed. You try to access a site that downloads 4MB of data before you can see anything.

Would you be able to see anything on your screen within 2–4 seconds?

Would you visit that site again?

I don’t think you would.

Another major improvement is in [First User Interaction Time](https://developers.google.com/web/tools/lighthouse/audits/time-to-interactive). This is the difference in time from when a user hits the URL to when they see content.

Here’s the comparison. I tested it on a development Mac.

#### React Rendered on Server

![Image](https://cdn-media-1.freecodecamp.org/images/1*kYMHoa7OemCHA_KBzJ1w-w.png)
_SSR performance report (Chrome)_

The first interaction time is 300ms. Hydrate finishes at 400ms. The load event exits at 500ms approximately. You can see this by checking out the image above.

#### React Rendered on Client’s Browser

![Image](https://cdn-media-1.freecodecamp.org/images/1*wquRCRboPDi7Ix2HAxvCAA.png)
_Client side performance report (Chrome)_

The first interaction time is 400ms. The load event exits at 470ms.

The result speaks for itself. There’s a 100ms difference in the First User Interaction Time for such a small app.

### How does it Work? — (4 Simple Steps)

* Create a fresh Redux Store on every request.
* Optionally dispatch some actions.
* Get the state out of the Store and perform SSR.
* Send the state obtained in the previous step along with the response.

We will use the state passed in the response for creating the initial state on client-side.

Before you get started, [clone/download the complete example from Github](https://github.com/Rohitkrops/ssr) and use it for reference.

### Getting Started by Setting up our App

First, open your favourite editor and shell. Create a new folder for your application. Let’s start.

```bash
npm init --yes
```

Fill in the details. After `package.json` is created, copy the dependencies and scripts below into it.

Install all dependencies by running:

```bash
npm install
```

You need to configure Babel and webpack for our build script to work.

Babel transforms ESM and react into Node and browser-understood code.

Create a new file `.babelrc` and put the line below in it.

```js
{
  "presets": ["@babel/env", "@babel/react"]
}

```

webpack bundles our app and its dependencies into a single file. Create another file `webpack.config.js` with the following code in it:

```js
const path = require('path');module.exports = {
    entry: {
        client: './src/client.js',
        bundle: './src/bundle.js'
    },
    output: {
        path: path.resolve(__dirname, 'assets'),
        filename: "[name].js"
    },
    module: {
        rules: [
            { test: /\.js$/, exclude: /node_modules/, loader: "babel-loader" }
        ]
    }
}
```

The build process output’s two files:

1. `assets/bundle.js` — pure client side app.
2. `assets/client.js` — client side companion for SSR.

The `src/` folder contains the source code. The Babel compiled files go into `views/`. `views` directory will be created automatically if not present.

### Why do we need to compile source files?

The reason is the syntax [difference between ESM & CommonJS](http://jsmodules.io/cjs.html). While writing React and Redux, we heavily use import and export in all files.

Unfortunately, they don’t work in Node. Here comes Babel to rescue. The script below tells Babel to compile all files in the `src` directory and put the result in `views.`

```json
"babel": "babel src -d views",
```

Now, Node can run them.

### Copy Precoded & Static files

If you have already cloned the repository, copy from it. Otherwise d[ownload ssr-static.zip file from Dropbox](https://www.dropbox.com/s/2iijlivmlye6pqp/ssr-static.zip?dl=0). Extract it and keep these three folders inside your app directory. Here’s what they contain.

1. React `App` and components resides in `src/components`.
2. Redux files in `src/redux/`.
3. `assets/ & media/`: Contain static files such as `style.css` and images.

### Server Side

Create two new files named `server.js` and `template.js` inside the `src/` folder.

### 1. src/server.js

Magic happens here. This is the code you’ve been searching for.

```jsx
import React from 'react';
import { renderToString } from 'react-dom/server';
import { Provider } from 'react-redux';
import configureStore from './redux/configureStore';
import App from './components/app';

module.exports = function render(initialState) {
  // Model the initial state  
  const store = configureStore(initialState);
  let content = renderToString(<Provider store={store} ><App /></Provider>);
  const preloadedState = store.getState();
  return {
    content,
    preloadedState
  };
};
```

Instead of rendering our app, we need to wrap it into a function and export it. The function accepts the initial state of the application.

Here’s how it works.

1. Pass `initialState` to `configureStore()`. `configureStore()`returns a new Store instance. Hold it inside the `store` variable.
2. Call `renderToString()` method, providing our App as input. It renders our app on the server and returns the HTML produced. Now, the variable `content` stores the HTML.
3. Get the state out of Redux Store by calling `getState()` on `store`. Keep it in a variable `preloadedState`.
4. Return the `content` and `preloadedState`. We will pass these to our template to get the final HTML page.

#### `2. src/template.js`

`template.js` exports a function. It takes `title`, `state` and `content` as input. It injects them into the template and returns the final HTML document.

To pass along the state, the template attaches `state` to `window.__STATE__` inside a `<scri`pt> tag.

Now you can read `state` on the client side by accessing `window.__STATE__`.

We also include the SSR companion `assets/client.js` client-side application in another script tag.

If you request the pure client version, it only puts `assets/bundle.js` inside the script tag.

### The Client Side

The client side is pretty straightforward.

### 1. src/bundle.js

This is how you write the React and Redux `Provider` wrap. It is our pure client-side app. No tricks here.

```jsx
import React from 'react';
import { render } from 'react-dom';
import { Provider } from 'react-redux';
import configureStore from './redux/configureStore';
import App from './components/app';

const store = configureStore();
render(
  <Provider store={store} > <App /> </Provider>,
  document.querySelector('#app')
);
```

### 2. src/client.js

Looks familiar? Yeah, there is nothing special except `window.__STATE__.` All we need to do is grab the initial state from `window.__STATE__` and pass it to our `configureStore()` function as the initial state.

Let’s take a look at our new client file:

```jsx
import React from 'react';
import { hydrate } from 'react-dom';
import { Provider } from 'react-redux';
import configureStore from './redux/configureStore';
import App from './components/app';

const state = window.__STATE__;
delete window.__STATE__;
const store = configureStore(state);
hydrate(
  <Provider store={store} > <App /> </Provider>,
  document.querySelector('#app')
);
```

Let’s review the changes:

1. Replace `render()` with `hydrate()`. `[hydrate()](https://reactjs.org/docs/react-dom.html#hydrate)` is the same as `render()` but is used to hydrate elements rendered by `[ReactDOMServer](https://reactjs.org/docs/react-dom-server.html)`. It ensures that the content is the same on the server and the client.
2. Read the state from the global window object `window.__STATE__`. Store it in a variable and delete the `window.__STATE__`.
3. Create a fresh store with `state` as initialState.

All done here.

## Putting it all together

### Index.js

This is the entry point of our application. It handles requests and templating.

It also declares an `initialState` variable. I have modelled it with data in the `assets/data.json` file. We will pass it to our `ssr()` function.

_Note: While referencing a file that is inside `src/` from a file outside `src/` , use normal `require()` and replace `src/` by `views/`. You know the reason (Babel compile)._

Routing

1. `/`: By default server-rendered homepage.
2. `/client`: Pure client-side rendering example.
3. `/exit`: Server stop button. Only available in development.

#### Build & Run

It’s time to build and run our application. We can do this with a single line of code.

```bash
npm run build && npm run start
```

Now, the application is running at [http://localhost:3000](http://localhost:3000/).

### Ready to become a React Pro?

I am starting a new series from next Monday to get your React skills blazing, immediately.

![Image](https://cdn-media-1.freecodecamp.org/images/1*TEecv1nLg253xmyGgddhOw.gif)
_subscription link below ?_

### Thank you for reading this.

If you like it and find it useful, follow me on [Twitter](http://twitter.com/rohitkrops) & [Webflow](http://bit.ly/2zVj1fX).

