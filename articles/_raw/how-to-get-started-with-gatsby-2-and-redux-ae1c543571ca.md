---
title: How to get started with Gatsby 2 and Redux
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-28T22:38:44.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-started-with-gatsby-2-and-redux-ae1c543571ca
coverImage: https://cdn-media-1.freecodecamp.org/images/1*KSVHAT4_AtBt2UpjrJNMBg.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: Redux
  slug: redux
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Carl-Johan Kihl

  Gatsby + Redux is a powerful combination when building static web-apps with dynamic
  features. With Gatsby 2, it has never been easier to get up and running. Today,
  I’m going to guide you through the steps needed.

  Not a big fan of r...'
---

By Carl-Johan Kihl

Gatsby + Redux is a powerful combination when building static web-apps with dynamic features. With Gatsby 2, it has never been easier to get up and running. Today, I’m going to guide you through the steps needed.

Not a big fan of reading? ? Head over to the Redux starter right away:  
h[ttps://github.com/caki0915/gatsby-redux-test/](https://github.com/caki0915/gatsby-redux-test/)  
or use the Gatsby CLI:

```bash
npx gatsby new gatsby-redux-test https://github.com/caki0915/gatsby-redux-test/
```

### What is Gatsby?

Gatsby is one of the most popular static site generators out there. Preconfigured with Webpack, React and GraphQL, it gives you a great head-start when building web-apps. It also comes with a rich eco-system of plugins that makes it easy to connect to a variety of data sources. [Read more about Gatsby on their website.](https://www.gatsbyjs.org/)

### What is Redux?

Redux is a state container often used together with React apps. This article will assume that you already know how Redux works. If you’re new to Redux or need a recap, you’ll [find more information on their website](https://redux.js.org/).

**? Let’s go! ?**

Start by creating a new Gatsby project. In the terminal, run: _(Replace_ **_gatsby-redux-test_** _with__a name of your choosing)_

```bash
npx gatsby new gatsby-redux-test && cd gatsby-redux-test
```

Next step is to install `redux` and `react-redux` packages from NPM.

```bash
npm install --save redux react-redux
```

![Image](https://cdn-media-1.freecodecamp.org/images/tDGPhNznARAWd8r52f0WYn-dzo4iMfHY1rAH)
_Redux and React-redux packages installed_

Ok great, let’s add a state!

Create a new folder called `state` inside of your `src` folder and create a file `app.js`. For the sake of this tutorial, we’re going to add a simple feature that lets you toggle a variable “**darkMode”** on and off.

First, add the initial state:

```js
const initialState = {
  isDarkMode: false,
};
```

Add the action creator (to toggle **darkMode** on and off):

```js
const TOGGLE_DARKMODE = 'TOGGLE_DARKMODE';

export const toggleDarkMode = isDarkMode => ({
  type: TOGGLE_DARKMODE, isDarkMode
});
```

Add the reducer:

```js
export default (state = initialState, action) => {
  switch (action.type) {
    case TOGGLE_DARKMODE:
      return { ...state, isDarkMode: action.isDarkMode };
    default:
      return state;
  }
};
```

![Image](https://cdn-media-1.freecodecamp.org/images/WXaLfdUTvndbGMYRSdXsItbuMssFsHBvLEgW)
_Initial State, Action Creator, and Reducer_

Ok great! Now, let’s add the root-reducer. Create a new file `index.js` inside the `state` folder.

```js
import { combineReducers } from 'redux';
import app from './app';

export default combineReducers({ app });
```

![Image](https://cdn-media-1.freecodecamp.org/images/SygFdoV3ZU0bJVAdkc7TCNS1xOgq94R1njfn)
_Our root reducer._

Now we going to create a Store and Provider. Create a new file `ReduxWrapper.js` in the `state` folder. This component is going to wrap our root-component in Gatsby.

```js
import React from 'react';
import { Provider } from 'react-redux';
import { createStore as reduxCreateStore } from 'redux';
import rootReducer from '.';

const createStore = () => reduxCreateStore(rootReducer);

export default ({ element }) => (
  <Provider store={createStore()}>{element}</Provider>
);
```

![Image](https://cdn-media-1.freecodecamp.org/images/dBEjRTDy9TrJl2GQxhNHBM6KGLVO0YlIwACe)
_Create a Store and a Provider_

Gatsby will render our app both on the server and in the browser, and lucky for us Gatsby has a very flexible API that lets us hook into the rendering. ? We can implement the hooks from two files: `gatsby-browser.js` and `gatsby-ssr.js`.

The hook we are interested in is called **wrapRootElement** and lets you wrap your app with a custom element. Exactly what we need for our Redux Provider. ? You can read more about **wrapRootElement** in the [documentation](https://www.gatsbyjs.org/docs/browser-apis/#wrapRootElement).

Since we want to export our **ReduxWrapper** as **wrapRootElement** from both `gatsby-browser.js` and `gatsby-ssr.js`, add this line to both files:

```js
export { default as wrapRootElement } from './src/state/ReduxWrapper';
```

![Image](https://cdn-media-1.freecodecamp.org/images/s6o3N7q-NrniTa6CrgQoDP9gLM7bV7wT0Zzg)
_Export our ReduxWrapper from gatsby-ssr.js and gatsby-browser.js_

Ok Done. Gatsby and Redux are now working together! ? Now we only need a way to test it.

Let’s go for the easiest possible way I can think of: A button on the start page where one can toggle **darkMode** on and off. When **darkMode** is on, the button will be dark with white text.

![Image](https://cdn-media-1.freecodecamp.org/images/svVswSsAToLN9w9eeilVcaH8nRNP2Upc36ZL)
_A simple test to see that Redux is actually working._

In the terminal run:

```bash
npm run develop
```

And… see the dark theme in action!

![Image](https://cdn-media-1.freecodecamp.org/images/DV4uT4GsHpfTkRhlqJ-FnCmG05W9GircsXf8)
_Minimal Redux example_

Ok, maybe that wasn’t so impressive, but the example does its job and I’m sure you will find a much better application for Redux in your Gatsby-app. ?

### Summary

Gatsby + Redux is a powerful combination if you want to build static web-apps with dynamic features. [I use it for my projects](https://carljohan.me) as well. If you find this article useful, please add a comment and a link to your awesome Gatsby/Redux-app. ? ?

![Image](https://cdn-media-1.freecodecamp.org/images/1VoLeHHA0WEqGAO4k-Dsgkm71UG0K9zVZW-4)
_[https://carljohan.me](https://carljohan.me" rel="noopener" target="_blank" title=") - A Drawer is a good use-case for Redux_

