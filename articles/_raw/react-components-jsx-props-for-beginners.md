---
title: React Functional Components, Props, and JSX – React.js Tutorial for Beginners
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-11-05T20:59:58.000Z'
originalURL: https://freecodecamp.org/news/react-components-jsx-props-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/Copy-of-Add-a-heading.png
tags:
- name: JavaScript
  slug: javascript
- name: JSX
  slug: jsx
- name: React
  slug: react
seo_title: null
seo_desc: "By Cem Eygi\nReact is one of the most popular JavaScript libraries for\
  \ building user interfaces. \nIf you want to become a front-end developer or find\
  \ a web development job, you would probably benefit from learning React in-depth.\n\
  In this post, you're ..."
---

By Cem Eygi

React is one of the most popular JavaScript libraries for building user interfaces. 

If you want to become a front-end developer or find a web development job, you would probably benefit from learning React in-depth.

In this post, you're going to learn some of the basics of React like creating a component, the JSX syntax, and Props. If you have no or little experience with React, this post is for you.

For starters, [here's how you can install React](https://www.freecodecamp.org/news/install-react-with-create-react-app/).

## What is JSX?

The first thing you'll realize after installing your first React project is that a JavaScript function returns some HTML code:

```jsx
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
      </header>
    </div>
  );
}
```

This is a special and valid syntax extension for React which is called JSX (JavaScript XML). Normally in frontend-related projects, we keep HTML, CSS, and JavaScript code in separate files. However in React, this works a bit differently.

In React projects, we don't create separate HTML files, because JSX allows us to write HTML and JavaScript combined together in the same file, like in the example above. You can, however, separate your CSS in another file.

In the beginning, JSX might seem a little bit weird. But don't worry, you'll get used to it. 

JSX is very practical, because we can also execute any JavaScript code (logic, functions, variables, and so on) inside the HTML directly by using curly braces { }, like this:

```jsx
function App() {
  const text = 'Hello World';
  
  return (
    <div className="App">
      <p> {text} </p>
    </div>
  );
}
```

Also, you can assign HTML tags to JavaScript variables:

```jsx
const message = <h1>React is cool!</h1>;
```

Or you can return HTML inside JavaScript logic (such as if-else cases):

```jsx
render() {
    if(true) {
        return <p>YES</p>;
    } else {
        return <p>NO</p>;
    }
}
```

I won't go into further details of JSX, but make sure that you consider the following rules while writing JSX:

* HTML and component tags must always be closed < />
* Some attributes like **“class”** become **“className”** (because class refers to JavaScript classes), **“tabindex”** becomes **“tabIndex”** and should be written camelCase
* We can’t return more than one HTML element at once, so make sure to wrap them inside a parent tag:

```jsx
return (
  <div>
    <p>Hello</p>
    <p>World</p>
  </div>
);
```

* or as an alternative, you can wrap them with empty tags:

```jsx
return (
  <>
    <p>Hello</p>
    <p>World</p>
  </>
);
```

You can also watch my React for Beginners tutorial for more info:

%[https://youtu.be/QJZ-xgt4SJo]

## What are Functional & Class Components?

After getting used to the JSX syntax, the next thing to understand is the component-based structure of React. 

If you revisit the example code at the top of this post, you'll see that the JSX code is being returned by a function. But the App( ) function is not an ordinary function – it is actually a component. So what is a component?

### What is a Component?

A component is an independent, reusable code block which divides the UI into smaller pieces. For example, if we were building the UI of Twitter with React:

![Image](https://www.freecodecamp.org/news/content/images/2020/11/twit.png)
_The components of Twitter's News Feed_

Rather than building the whole UI under one single file, we can and we should divide all the sections (marked with red) into smaller independent pieces. In other words, these are components.

React has two types of components: functional and class. Let's look at each now in more detail.

### Functional Components

The first and recommended component type in React is functional components. A functional component is basically a JavaScript/ES6 function that returns a React element (JSX). According to React's official docs, the function below is a valid functional component:

```jsx
function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}
```

Alternatively, you can also create a functional component with the arrow function definition:

```jsx
const Welcome = (props) => { 
  return <h1>Hello, {props.name}</h1>; 
}
```

> This function is a valid React component because it accepts a single “props” (which stands for properties) object argument with data and returns a React element. — [**reactjs.org**](https://reactjs.org/)

To be able to use a component later, you need to first export it so you can import it somewhere else:

```jsx
function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}

export default Welcome;
```

After importing it, you can call the component like in this example:

```jsx
import Welcome from './Welcome';

function App() { 
  return (
    <div className="App">
      <Welcome />
    </div>
  );
}
```

 So a Functional Component in React:

* is a JavaScript/ES6 function
* must return a React element (JSX)
* always starts with a capital letter (naming convention)
* takes props as a parameter if necessary

### What are Class Components?

The second type of component is the class component. Class components are ES6 classes that return JSX. Below, you see our same Welcome function, this time as a class component:

```jsx
class Welcome extends React.Component {
  render() {
    return <h1>Hello, {this.props.name}</h1>;
  }
}
```

Different from functional components, class components must have an additional render( ) method for returning JSX.

### Why Use Class Components?

We used to use class components because of "state". In the older versions of React (version < 16.8), it was not possible to use state inside functional components.

Therefore, we needed functional components for rendering UI only, whereas we'd use class components for data management and some additional operations (like life-cycle methods). 

This has changed with the introduction of React Hooks, and now we can also use states in functional components as well. (I will be covering state and hooks in my following posts, so don't mind them for now).

A Class Component:

* is an ES6 class, will be a component once it ‘extends’ a React component.
* takes Props (in the constructor) if needed
* must have a render( ) method for returning JSX

## What are Props in React?

Another important concept of components is how they communicate. React has a special object called a prop (stands for property) which we use to transport data from one component to another.

But be careful – props only transport data in a one-way flow (only from parent to child components). It is not possible with props to pass data from child to parent, or to components at the same level.

Let's revisit the App( ) function above to see how to pass data with props. 

First, we need to define a prop on the Welcome Component and assign a value to it:

```jsx
import Welcome from './Welcome';

function App() { 
  return (
    <div className="App">
      <Welcome name="John"/>
      <Welcome name="Mary"/>
      <Welcome name="Alex"/>
    </div>
  );
}
```

Props are custom values and they also make components more dynamic. Since the Welcome component is the child here, we need to define props on its parent (App), so we can pass the values and get the result simply by accessing the prop "name":

```jsx
function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2020/11/props.png)

### React Props Are Really Useful

So React developers use props to pass data and they're useful for this job. But what about managing data? Props are used for passing data, not for manipulating it. I'm going to cover managing data with React in my future posts here on freeCodeCamp.

In the meantime, if you want to learn more about React & Web development, feel free to [subscribe to my YouTube channel](https://www.youtube.com/channel/UC1EgYPCvKCXFn8HlpoJwY3Q).

Thank you for reading!

