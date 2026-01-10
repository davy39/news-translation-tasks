---
title: The Best React Tutorials
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-27T00:39:00.000Z'
originalURL: https://freecodecamp.org/news/best-react-javascript-tutorial
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f01740569d1a4ca404f.jpg
tags:
- name: React
  slug: react
- name: Tutorial
  slug: tutorial
seo_title: null
seo_desc: 'React is a JavaScript library for building user interfaces. It was voted
  the most loved in the “Frameworks, Libraries, and Other Technologies” category of
  Stack Overflow’s 2017 Developer Survey.

  React is a JavaScript library and React applications bu...'
---

React is a JavaScript library for building user interfaces. It was voted the most loved in the “Frameworks, Libraries, and Other Technologies” category of Stack Overflow’s 2017 Developer Survey.

React is a JavaScript library and React applications built on it run in the browser, NOT on the server. Applications of this kind only communicate with the server when necessary, which makes them very fast compared to traditional websites that force the user to wait for the server to re-render entire pages and send them to the browser.

React is used for building user interfaces - what the user sees on their screen and interacts with to use your web app. This interface is split up into components, instead of having one huge page you break it up into smaller pieces known as components. In more general terms, this approach is called Modularity.

* It’s declarative: React uses a declarative paradigm that makes it easier to reason about your application.
* It’s efficient: React computes the minimal set of changes necessary to keep your DOM up-to-date.
* And it’s flexible: React works with the libraries and frameworks that you already know.

## The Best Tutorials for Learning React

freeCodeCamp has a [React tutorial on YouTube](https://www.youtube.com/watch?v=DLX62G4lc44) that will teach you all the basics in just 5 hours. 

![Image](https://img.youtube.com/vi/DLX62G4lc44/maxresdefault.jpg)

We also have a more [in-depth intermediate React tutorial](https://www.youtube.com/watch?v=m_u6P5k0vP0) that teaches you how to build an entire social media React app using Firebase. It is 12 hours long, and if you follow along, you will learn a ton of the intricacies of React.

## **Why learn React?**

React involves Composition, that is lots of components wrapping up the functionalities into an encapsulated container. 

Many popular websites use React implementing the MVC architectural pattern. Facebook (Partially), Instagram (Completely), Khan Academy (Partially), New York Times (Partially), Yahoo Mail (Completely), Dropbox’s new photo and video gallery app Carousel (Completely) are the popular websites known to be using React. 

How are these large applications built using React? The simple answer is by building small applications or components. Example:

```jsx
const Component2 = () => {
  return (
    <div></div>
  );
};
const Component3 = () => {
  return (
    <div></div>
  );
};
const Component1 = () => {
  return (
    <div>
      <Component2 />
      <Component3 />
    </div>
  );
};

ReactDOM.render(
  <Component1 />, 
  document.getElementById("app")
);
```

React is Declarative, for the most part, which means we are concerned more with what to do rather than how to do a specific task. 

Declarative programming is a programming paradigm that expresses the logic of a computation without describing its control flow. Declarative programming comes with certain advantages such as reduced side effects (occurs when we modify any state or mutate something or make an API request), minimized mutability (as a lot of it is abstracted), enhanced readability, and fewer bugs.

React also has an unidirectional dataflow. UI in React is actually the function of the state. This means that as the state updates it updates the UI as well. So our UI progresses as the state changes.

## **Advantages of React**

Some reasons to use React are:

1. Fast. Apps made in React can handle complex updates and still feel quick and responsive.
2. Modular. Instead of writing large, dense files of code, you can write many smaller, reusable files. React’s modularity can be a beautiful solution to JavaScript’s [maintainability problems](https://en.wikipedia.org/wiki/Spaghetti_code).
3. Scalable. Large programs that display a lot of changing data are where React performs best.
4. Flexible. You can use React for interesting projects that have nothing to do with making a web app. People are still figuring out React’s potential. [There’s room to explore](https://medium.mybridge.co/22-amazing-open-source-react-projects-cb8230ec719f).

### **Virtual DOM**

React’s magic comes from its interpretation of the DOM and its strategy for creating UIs.

React uses the Virtual DOM to render an HTML tree virtually first. Then, every time a state changes and we get a new HTML tree that needs to be taken to the browser’s DOM, instead of writing the whole new tree React will only write the difference between the new tree and the previous tree (since React has both trees in memory). This process is known as Tree Reconciliation.

### **Reconciliation**

React has a smart diffing algorithm that it uses to only regenerate in its DOM node what actually needs to be regenerated while it keeps everything else as is. This diffing process is possible because of React’s virtual DOM.

Using the virtual DOM, React keeps the last DOM version in memory. When it has a new DOM version to take to the browser, that new DOM version will also be in memory, so React can compute the difference between the new and the old versions.

React will then instruct the browser to update only the computed diff and not the whole DOM node. No matter how many times we regenerate our interface, React will take to the browser only the new “partial” updates.

## **React from Scratch**

Would you like to get started learning the basics of react without getting bogged down creating a development environment? Chances are that if you are new to web development, setting up a development environment can leave you feeling a little intimidated when you are just trying to learn React.

In this article we are going to look at how we can get started with React using only a text editor and a browser and nothing else.

### **1 — Set Up Boiler Plate Code with Emmet**

Let’s get started with step 1. We’ll begin with a file in our browser called “index.html”. We’ll begin with the boiler plate HTML code. For a quick start I recommend using Emmet with whatever text editor you have. On the first line, type in `html:5` then press the shift key to get the code below. Or you can go ahead and copy and paste the code from below.

```javascript
html:5
```

This will result in the following code:

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
</head>
<body>

</body>
</html>
```

We can fill in the title of “Time to React!”.

This content will not appear in your webpage. Anything in the head section of the HTML file will be meta data that our browser will user to interpret our code in the body section. This title is going to be what appears on the tab for our page, not actually on the page.

### **2 - Get Script Tags to Harness the Power of React and Babel Libraries**

Ok, item one is checked off of our list. Let’s look at item two. We are going to set up our developer environment by using script tags to bring in React and Babel. 

This is not a real life developer environment. That would be quite an elaborate setup. It would also leave us with a lot of boiler plate code and libraries that would take us off subject of learning React basics. The goal of this series is to go over the basic syntax of React and get right into coding. We are going to use `<script>` tags to bring in the React Library, the React DOM library (why), and the Babel library.

```javascript
<head>
  ...
  <!-- REACT LIBRARY -->
  <script src="https://unpkg.com/react@15.5.4/dist/react.js"></script>
  <!-- REACT DOM LIBRARY -->
  <script src="https://unpkg.com/react-dom@15.5.4/dist/react-dom.js"></script>
  <!-- BABEL LIBRARY -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/babel-standalone/6.25.0/babel.min.js"></script>
  ...
  <title>Time to React!</title>
</head>
```

You are free to use more updated versions of these libraries as they come out. They should not create any breaking changes for the content we are covering.

What are we doing here? The HTML `<script>` element is used to embed or reference an executable script. The “src” attribute points to the external script files for the React library, ReactDOM library and Babel library. 

This is like if you have an electric razor. It is literally no good to you no matter how fancy the electric razor unless you can plug it into the wall and gain access to electricity. Our React code we will write will be no good to us if our browser can’t plug into these libraries to understand and interpret what we are going. 

This is how our application is going to gain the power of React, it is going to be how we insert React into the Dom. We have React and ReactDOM as two different libraries because there are use cases such as React Native where rendering to the DOM isn’t needed for mobile development so the library was split so people could decide what they needed depending on the project they were working on. 

Because we will need our React to make it to the DOM we’ll use both scripts. Babel is how we take advantage of ECMA script beyond ES5 and deal with something called JSX (JavaScript as XML) that we will use in React. We’ll take a deeper look at the magic of Babel in an upcoming section :) 

Alright, we have completed steps 1 and 2. We have set up our boiler plate code and set up our developer environment.

### **3 - Render React to the DOM**

Our next two steps will be to choose our location within the DOM that we want to render our React content. And we'll use another script tag for our React content within the body. Generally, as a good separations of concerns practice, this would be in its own file then linked to this html document. We’ll do that later in upcoming sections. For now, we’ll let this dwell within the body of the html document we are currently in. 

Now we are going to look at how simple it is to choose a place on the DOM to render our React content. We’ll go within the body. And best practice isn’t just to throw React into the body tag to be displayed but to create a separate element, often a div, that you can treat as a root element to insert your React content.

```javascript
<body>
  <div id="app">React has not rendered yet</div>
</body>
```

We’ll create a simple `<div>` element and give it an id of “app”. We are going to be able to target this location to insert our React content much the same way you might use CSS to target an id for styling of your choice. Any react content will be rendered within the div tags with the id of app. In the meantime we’ll leave some text saying that “React has not rendered yet”. If we see this when we preview our page it means that somewhere we missed rendering React. 

Now, let’s go ahead and create a script tag within our body where we will create with React for the first time. The syntax we are going to need for our script tag is to add an attribute of “type”. This specifies the media type of the script. Above in our head we used an src attribute that pointed to the external script files for the React library, ReactDOM library and Babel library.

```javascript
<body>
  <div id="app">React has not rendered yet</div>
  <script type="text/babel">
  </script>
</body>
```

The “type” of script that we are using will be wrapped in quotes and set to `"text/babel"`. We’ll need the ability to use babel right away as we work with JSX. 

First, we are going to render React to the DOM. We will use the `ReactDOM.render()` method to do this. This will be a method, and remember a method is just a function attached to an object. This method will take two arguments.

```javascript
<body>
  <div id="app">React has not rendered yet</div>
  <script type="text/babel">
  ReactDOM.render(React What, React Where);
</script>
</body>
```

The first argument is the “what” of React. The second argument is the “where” of the location you want it to be placed in the DOM. Let’s start by calling our ReactDOM.render() method. Our first argument is going to be our JSX.

```javascript
<body>
  <div id="app">React has not rendered yet</div>
  <script type="text/babel">
  ReactDOM.render(
    <h1>Hello World</h1>, 
    React Where
  );
</script>
</body>
```

The [official react docs state](https://reactjs.org/docs/introducing-jsx.html): “This funny tag syntax is neither a string nor HTML. It is called JSX, and it is a syntax extension to JavaScript. We recommend using it with React to describe what the UI should look like. JSX may remind you of a template language, but it comes with the full power of JavaScript. JSX produces React “elements.”

Often times, JSX freaks people out who have been developers for a while because it looks like HTML. At a very early age developers are taught separation of concerns. HTML has its place, CSS has its place and JavaScript has its place. JSX seems to blur the lines. You are using what looks like HTML but as Facebook says it comes with the full power of JavaScript.

This can freak out veterans, so many React tutorials start without JSX which can be quite complex. We won’t do that. Because this article is directed towards those who are very young in their careers you may not bring those red flags when you see this syntax.

And JSX is just really intuitive. You can probably quite easily read this code and see that this is going to be the largest header tag displaying the text “Hello World”. No mystery and pretty straightforward. Now, let’s look at what our second argument would be.

```javascript
<body>
  <div id="app">React has not rendered yet</div>
  <script type="text/babel">
    ReactDOM.render(
      <h1>Hello World</h1>, 
      document.getElementById("app")
    );
  </script>
</body>
```

This is where we want our React content rendered to the DOM. You’ve probably done this quite a few times in the past. We’ll just type in `document.getElementById()`. And we’ll pass into the argument of the id of app. And that is it. We will now target the div with the id of app to insert our React content.

We want to make sure our content is saved. Go ahead and open this up in the browser and you should see “Hello World”. As you can probably guess, using React is not the quickest or best way to create a Hello World app. We aren’t quite seeing the benefits of it yet. But now, we know that everything is working.

Go ahead and open up the console and look at the “elements”. You can do that on a Mac with command + shift + j or on Windows and Linux: Ctrl + Shift + J

If you click on the head tag, we can see our script libraries we included. Then we can go down to the body of our document. Let’s click on our div with the id of “app”. And when we do we see our `<h1>` tag with the content “Hello World”.

[View Entire Code Here](https://github.com/robgmerrill/hello-react/blob/master/section-one/index.html).

### **Recap**

So let’s do a quick recap. In our head tag we grabbed the script tags for React, ReactDOM and Babel. These are the tools our browser needs in its meta data to read our React code and JSX in specific. 

We then located the position within the DOM that we wanted to insert our React by creating an element div with the id of “app”. 

Next, we created a script tag to input our React code. We used the ReactDOM.render() method that takes two arguments. The “what” of the React content, in this case our JSX, and the second argument is the “where” that you want to insert the React content into the DOM. In this case it is the location with the id of “app”.

As an alternative to JSX, you can use ES6 and Javascript’s compiler like Babel. [https://babeljs.io/](https://babeljs.io/)

## **Installing React**

### **Creating a new React project**

You could just embed the React library in your webpage like so<sup>2</sup>:

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/react/16.0.0/cjs/react.production.min.js"></script>
```

Smart programmers want to take the more practical and productive way: [Create React App](https://github.com/facebookincubator/create-react-app)

```bash
npm install -g create-react-app
create-react-app my-app

cd my-app
npm start
```

This will set up your development environment so that you can use the latest JavaScript features, provide a nice developer experience, and optimize your app for production.

`npm start` will start up a development server which allows live reloading<sup>3</sup>.

After you finish your project and are ready to deploy your App to production, you can just use `npm run build` to create an optimized build of your app in the `build` folder.

## **Your first React App**

### **Installation**

As specified in the previous section (Installation), run the `Create React App` tool. After everything has finished, `cd` into the folder of your application and run `npm start`. This will start a development server and you are all set to start developing your app!

```bash
npm install -g react-create-app
create-react-app my-first-app

cd my-first-app
npm start
```

### **Editing the code**

Start up your editor or IDE of choice and edit the `App.js` file in the `src` folder. When created with the `react-create-app` tool, there will already be some code in this file.

The code will consist of these parts:

#### **imports**

```javascript
import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
```

This is used by [webpack](https://webpack.js.org/) to import all required modules so that your code can use them. This code imports 3 modules:

1. `React` and `Component`, which allow us to use React as it should be used. (With components)
2. `logo`, which allows us to use `logo.svg` in this file.
3. `./App.css`, which imports the stylesheet for this file.

#### **classes/components**

```javascript
class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to React</h1>
        </header>
        <p className="App-intro">
          To get started, edit <code>src/App.js</code> and save to reload.
        </p>
      </div>
    );
  }
}
```

React is a library that makes use of Components, which let you split up your UI into independent, reusable pieces, and think about each piece in isolation. There is already 1 component created, the `App` component. If you used the `create-react-app` tool, this component is the main component in the project and you should build around this central class.

We will look at components in more detail shortly.

#### **exports**

When creating a class in React, you should export them after declaration, which allows you to use the component in another file by using the `import` keyword. You can use `default` after the `export` keyword to tell React that this is the main class of this file.

```javascript
export default App;
```

### **View the results!**

When you’ve started the development server by issuing the `npm start` command, you can view the changes you add to your project live in your browser. After issuing the command, npm should open a browser automatically displaying your app.

## **React - Components**

Components are reusable in React. You can inject value into props as given below:

```jsx
function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}

const element = <Welcome name="Faisal Arkan" />;
ReactDOM.render(
  element,
  document.getElementById('root')
);
```

`name="Faisal Arkan"` will give value into `{props.name}` from the  `function Welcome(props)` and will return the component that has given value by `name="Faisal Arkan"`. After that react will render the element into HTML.

### **Other ways to declare components**

There are many ways to declare components when using React. There are two kinds of components, **_stateless_** components and **_stateful_** components.

### **Stateful**

#### **Class Type Components**

```jsx
class Cat extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      humor: 'happy'
    }
  }
  render() {
    return(
      <div>
        <h1>{this.props.name}</h1>
        <p>
          {this.props.color}
        </p>
      </div>
    );
  }
}
```

### **Stateless Components**

#### **Functional Components (Arrow Function from ES6)**

```jsx
const Cat = props => {
  return (  
    <div>
      <h1>{props.name}</h1>
      <p>{props.color}</p>
    </div>;
  );
};
```

#### **Implicit Return Components**

```jsx
const Cat = props => 
  <div>
    <h1>{props.name}</h1>
    <p>{props.color}</p>
  </div>;
```


