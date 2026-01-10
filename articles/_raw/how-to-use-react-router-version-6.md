---
title: React Router Version 6 Tutorial – How to Set Up Router and Route to Other Components
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2021-12-14T21:41:14.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-react-router-version-6
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/react-router-cover.svg.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: react router
  slug: react-router
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "In this tutorial, we'll talk about what React Router is and how to use\
  \ it. Then we'll discuss its features and how to use them in your React app to navigate\
  \ to and render multiple components. \nPrerequisites\n\nA React app\nA good understanding\
  \ of what c..."
---

In this tutorial, we'll talk about what React Router is and how to use it. Then we'll discuss its features and how to use them in your React app to navigate to and render multiple components. 

### **Prerequisites**

* A React app
* A good understanding of what components are in React. 
* Node.js installed.

### Here's an interactive scrim about how to set up React Router and route to other components:

<iframe src="https://scrimba.com/scrim/crd9bBC6?embed=freecodecamp,mini-header" width="100%" height="480"></iframe>

## React as a Single Page Application (SPA)

You need to understand how pages are rendered in a React app before diving into routing. This section is aimed at beginners – you can to skip it if you already understand what a SPA is and how it relates to React. 

In non-single page applications, when you click on a link in the browser, a request is sent to the server before the HTML page gets rendered. 

In React, the page contents are created from our components. So what React Router does is intercept the request being sent to the server and then injects the contents dynamically from the components we have created. 

This is the general idea behind SPAs which allows content to be rendered faster without the page being refreshed.

When you create a new project, you'll always see an `index.html` file in the public folder. All the code you write in your `App` component which acts as the root component gets rendered to this HTML file. This means that there is only one HTML file where your code will be rendered to.

What happens when you have a different component you would prefer to render as a different page? Do you create a new HTML file? The answer is no. React Router – like the name implies – helps you route to/navigate to and render your new component in the `index.html` file.

So as a single page application, when you navigate to a new component using React Router, the `index.html` will be rewritten with the component's logic.

## How to Install React Router

To install React Router, all you have to do is run `npm install react-router-dom@6` in your project terminal and then wait for the installation to complete. 

If you are using yarn then use this command: `yarn add react-router-dom@6`.

## How to Set Up React Router

The first thing to do after installation is complete is to make React Router available anywhere in your app. 

To do this, open the `index.js` file in the `src` folder and import `BrowserRouter` from `react-router-dom` and then wrap the root component (the `App` component) in it. 

This is what the `index.js` looked like initially:

```js
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);


```

After making changes with React Router, this is what you should have:

```js
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import { BrowserRouter } from "react-router-dom";

ReactDOM.render(
  <BrowserRouter>
    <App />
  </BrowserRouter>,
  document.getElementById("root")
);
```

All we did was replace `React.StrictMode` with `BrowserRouter` which was imported from `react-router-dom`.  Now the router features are accessible from any part of your app.

## How to Route to Other Components

We are finally done setting things up, so now we'll look at routing to and rendering different components.

### Step 1 - Create multiple components

We'll create the following `Home`, `About`, and `Contact` components like this:

```js
function Home() {
  return (
    <div>
      <h1>This is the home page</h1>
    </div>
  );
}

export default Home;

```

```js
import React from 'react'

function About() {
    return (
        <div>
            <h1>This is the about page</h1>
        </div>
    )
}

export default About
```

```js
import React from 'react'

function Contact() {
    return (
        <div>
            <h1>This is the contact page</h1>
        </div>
    )
}

export default Contact
```

### Step 2 - Define routes

Since the `App` component acts as the root component where our React code gets rendered from initially, we will be creating all our routes in it. 

Don't worry if this does not make much sense – you'll understand better after looking at the example below.

```js
import { Routes, Route } from "react-router-dom"
import Home from "./Home"
import About from "./About"
import Contact from "./Contact"

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/" element={ <Home/> } />
        <Route path="about" element={ <About/> } />
        <Route path="contact" element={ <Contact/> } />
      </Routes>
    </div>
  )
}

export default App

```

We first imported the features we'll be using – `Routes` and `Route`. After that, we imported all the components we needed to attach a route to. Now let's break down the process.

`Routes` acts as a container/parent for all the individual routes that will be created in our app.

`Route` is used to create a single route. It takes in two attributes: 

* `path`, which specifies the URL path of the desired component. You can call this pathname whatever you want. Above, you'll notice that the first pathname is a backslash (/). Any component whose pathname is a backslash will get rendered first whenever the app loads for the first time. This implies that the `Home` component will be the first component to get rendered.
* `element`, which specifies the component the route should render. 

All we have done now is define our routes and their paths, and attach them to their respective components. 

If you are coming from version 5 then you'll notice that we're not using `exact` and `switch`, which is awesome. 

### Step 3 - Use `Link` to navigate to routes

If you have been coding along up to this point without any errors, your browser should be rendering the `Home` component. 

We will now use a different React Router feature to navigate to other pages based on those routes and pathnames we created in the `App` component. That is: 

```js
import { Link } from "react-router-dom";

function Home() {
  return (
    <div>
      <h1>This is the home page</h1>
      <Link to="about">Click to view our about page</Link>
      <Link to="contact">Click to view our contact page</Link>
    </div>
  );
}

export default Home;

```

The `Link` component is similar to the anchor element (<a>) in HTML. Its `to` attribute specifies which path the link takes you to. 

Recall that we created the pathnames listed in the `App` component so when you click on the link, it will look through your routes and render the component with the corresponding pathname.

Always remember to import `Link` from `react-router-dom` before using it.

## Conclusion

At this point, we have seen how to install, set up and use the basic features of React Router to navigate to different pages in your app. This pretty much covers the basics for getting started, but there are a lot more cooler features.

For example, you can use `useNavigate` to push users to various pages, and you can use `useLocation` to get the current URL. Alright, we won't start another tutorial at the end of the article. 

You can check out more features in the [React Router documentation](https://reactrouter.com/docs/en/v6).

You can find me on Twitter [@ihechikara2](https://twitter.com/Ihechikara2). Subscribe to my [newsletter](https://www.getrevue.co/profile/The-Congregation-of-Programmers) for free learning resources.

Happy coding!

