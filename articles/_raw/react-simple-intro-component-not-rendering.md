---
title: REACT – Simple Intro Component Not Rendering?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-02T02:18:00.000Z'
originalURL: https://freecodecamp.org/news/react-simple-intro-component-not-rendering
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a9b740569d1a4ca269e.jpg
tags:
- name: components
  slug: components
- name: React
  slug: react
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'One of the great things about React is its flexible component system. Once
  you get a hang of it, you can break up your application into reusable components
  and include them all over your project.

  The problem is that there are a few gotchas that make ...'
---

One of the great things about React is its flexible component system. Once you get a hang of it, you can break up your application into reusable components and include them all over your project.

The problem is that there are a few gotchas that make working with components difficult for those new to React.

For example, say you have the following component, `mainIntro.js`:

```jsx
const mainIntro = props => (
    <div id="quote-box">
     <h1> Hunter x Hunter Quotes </h1>

     <div id="text">
        "When I say it doesn't hurt me, that means I can bear it."
     </div>

     <div id="author">
        - Killua Zoldyck
     </div>

     <button id="new-quote"> Next Quote </button>

     <a href="#" id="tweet-quote" target="_blank"> Tweet this quote </a>

    </div>
)

export default mainIntro;
```

And want to import it into `App.js`:

```jsx
import mainIntro from './components'

class App extends React.Component{
    render(){
        return(
            <mainIntro />
        );
    }
}


const mainNode = document.getElementById("quoter");
ReactDOM.render(<App />,mainNode);
```

But `mainIntro` isn't loading for some reason. Let's take a closer look at what's happening.

## Naming your components

For anyone familiar with Object Oriented Programming, it's common convention to name each class with an uppercase letter. For example, a class to describe a person would be called `Person` to indicate that it's a class.

In React, which uses JSX rather than plain JavaScript, the first letter of a tag indicates what kind of element it is. Uppercase first characters are used to specify React components, so `mainIntro` should instead be called `MainIntro`:

```jsx
const MainIntro = props => (
    <div id="quote-box">
     <h1> Hunter x Hunter Quotes </h1>

     <div id="text">
        "When I say it doesn't hurt me, that means I can bear it."
     </div>

     <div id="author">
        - Killua Zoldyck
     </div>

     <button id="new-quote"> Next Quote </button>

     <a href="#" id="tweet-quote" target="_blank"> Tweet this quote </a>

    </div>
)

export default MainIntro;
```

While the filename can still be `mainIntro.js`, it's a good idea to capitalize the first character, too. Later when you scan the contents of the directory, you'll quickly be able to pick out that `MainIntro.js` contains a component.

Now `App.js` should look like this:

```jsx
import MainIntro from './components/MainIntro.js';

class App extends React.Component{
    render(){
        return(
            <MainIntro />
        );
    }
}


const mainNode = document.getElementById("quoter");
ReactDOM.render(<App />,mainNode);
```

## How is React Installed?

There are two main ways to use React. First, install and set it up locally, probably through `create-react-app`. Second, through a CDN.

You might have noticed above that the code snippets don't actually include React in the project with `import React from'react';`. This will throw an error if you're working with React locally.

However, if you're using a CDN to load React, it's available globally and you don't need to import it like above.

## Arrow Functions

Before diving into React, it's important to have a solid understanding of JavaScript, particularly ES6 syntax.

Take another look at the `MainIntro` component:

```jsx
const MainIntro = props => (
    <div id="quote-box">
     <h1> Hunter x Hunter Quotes </h1>

     <div id="text">
        "When I say it doesn't hurt me, that means I can bear it."
     </div>

     <div id="author">
        - Killua Zoldyck
     </div>

     <button id="new-quote"> Next Quote </button>

     <a href="#" id="tweet-quote" target="_blank"> Tweet this quote </a>

    </div>
)

export default MainIntro;
```

If you look closely at the first line, you'll notice a syntax error:

```jsx
const MainIntro = props => (
```

You're writing a functional component, which are typically simple JavaScript functions that can accept props as an argument and return valid JSX. Of course, the syntax needs to be correct for it to return properly.

[Arrow functions](https://www.freecodecamp.org/news/arrow-function-javascript-tutorial-how-to-declare-a-js-function-with-the-new-es6-syntax/) can be written in a lot of ways, but for this example, you'll need to add the curly braces (`{}`) and make sure to return JSX from the component itself:

```jsx
const MainIntro = props => {
  return (
    <div id="quote-box">
     //... rest of the code   
    </div>
  );
}
```

After implementing all the changes mentioned above, your component should now render properly.

Though the main distinction between functional and class components in React used to be that the former was "stateless" while the latter was "statefull", React Hooks have blurred the lines between them. Read more about both components in this [overview](https://www.freecodecamp.org/news/functional-components-vs-class-components-in-react/) and this deeper dive into [functional components with React Hooks](https://www.freecodecamp.org/news/a-few-questions-on-functional-components/).

