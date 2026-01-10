---
title: Learn React – A Handbook for Beginners
subtitle: ''
author: Nathan Sebhastian
co_authors: []
series: null
date: '2024-03-01T00:34:46.000Z'
originalURL: https://freecodecamp.org/news/react-for-beginners-handbook
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/Learn-React-Cover.png
tags:
- name: beginner
  slug: beginner
- name: handbook
  slug: handbook
- name: React
  slug: react
seo_title: null
seo_desc: 'The goal of this handbook is to provide gentle step-by-step instructions
  that will help you learn the key concepts of React.

  Instead of covering all the theories and concepts of React in their entirety, I''ll
  be teaching you important building blocks ...'
---

The goal of this handbook is to provide gentle step-by-step instructions that will help you learn the key concepts of React.

Instead of covering all the theories and concepts of React in their entirety, I'll be teaching you important building blocks of the library. You'll learn about JSX, components, props, states, event handlers, creating forms, and running network requests.

## Table of Contents

- [Requirements](#heading-requirements)
- [Chapter 1: Introduction](#heading-chapter-1-introduction)
  - [Computer Setup](#heading-computer-setup)
  - [Your First React Application](#heading-your-first-react-application)
  - [Explaining the Source Code](#heading-explaining-the-source-code)
- [Chapter 2: How to Create React Components](#heading-chapter-2-how-to-create-react-components)
  - [How to Return Multiple Elements With Fragments](#heading-how-to-return-multiple-elements-with-fragments)
  - [How to Render to the Screen](#heading-how-to-render-to-the-screen)
  - [How to Write Comments in React](#heading-how-to-write-comments-in-react)
  - [How to Compose Multiple Components as One](#heading-how-to-compose-multiple-components-as-one)
- [Chapter 3: Making Sense of JSX](#heading-chapter-3-making-sense-of-jsx)
  - [How to Render a List Using JSX](#heading-how-to-render-a-list-using-jsx)
  - [How to Add the Class Attribute](#heading-how-to-add-the-class-attribute)
- [Chapter 4: Props and States](#heading-chapter-4-props-and-states)
  - [How to Pass Down Multiple Props](#heading-how-to-pass-down-multiple-props)
  - [Props are Immutable](#heading-props-are-immutable)
  - [State in React](#heading-state-in-react)
  - [How to Pass State to a Child Component](#heading-how-to-pass-state-to-a-child-component)
  - [How to Use React DevTools to Inspect States and Props](#heading-how-to-use-react-devtools-to-inspect-states-and-props)
- [Chapter 5: React Conditional Rendering](#heading-chapter-5-react-conditional-rendering)
  - [Partial Rendering with a Regular Variable](#heading-partial-rendering-with-a-regular-variable)
  - [Inline Rendering with the && Operator](#heading-inline-rendering-with-the-ampamp-operator)
  - [Inline Rendering with the Conditional (Ternary) Operator](#heading-inline-rendering-with-the-conditional-ternary-operator)
- [Chapter 6: How to Handle User Events](#heading-chapter-6-how-to-handle-user-events)
  - [How to Change the UI by Handling Events](#heading-how-to-change-the-ui-by-handling-events)
- [Chapter 7: CSS in React](#heading-chapter-7-css-in-react)
  - [React Inline Styling](#heading-react-inline-styling)
  - [CSS Files](#heading-css-files)
  - [CSS Modules](#heading-css-modules)
  - [Tailwind CSS](#heading-tailwind-css)
  - [Which One Should You Use?](#heading-which-one-should-you-use)
- [Chapter 8: How to Build Forms in React](#heading-chapter-8-how-to-build-forms-in-react)
  - [How to Handle Form Input](#heading-how-to-handle-form-input)
  - [How to Handle Form Submission](#heading-how-to-handle-form-submission)
  - [How to Handle Form Validation](#heading-how-to-handle-form-validation)
- [Chapter 9: Network Requests in React](#heading-chapter-9-network-requests-in-react)
  - [The useEffect Hook](#heading-the-useeffect-hook)
- [Wrapping Up](#heading-wrapping-up)

By covering these concepts, you'll be equipped to dive further into advanced React topics.

## Requirements

To get the full benefit of this handbook, you should have basic knowledge of HTML, CSS, and JavaScript. No previous knowledge about React is needed, as we will start from the very basics.

If you need a JavaScript refresher, you can [get my JavaScript book here](https://codewithnathan.com/beginning-modern-javascript).

## Chapter 1: Introduction

React is a very popular JavaScript front-end library. It's received lots of love from developers around the world for its **simplicity** and **fast performance**.

React was initially developed by Facebook as a solution to front end problems they were facing:

* DOM manipulation is an expensive operation and should be minimized
* No library specialized in handling front-end development at the time (there is Angular, but it's an ENTIRE framework.)
* Using a lot of vanilla JavaScript can turn a web application into a mess that's hard to maintain.

Why do developers love React? As a software developer myself, I can think of a few reasons why I love it:

* **It's minimalist**. React takes care of only ONE thing: the user interface and how it changes according to the data you feed into it. React makes your interface dynamic with minimal code.
* **It has a low learning curve**. The core concepts of React are relatively easy to learn, and you don't need months or 40 hours of video lectures to learn the basics.
* **It's unopinionated**. React can be integrated with lots of different technologies. On the front-end, you can use different libraries to handle Ajax calls (Axios, Superagent, or just plain Fetch.) On the back-end, you can use PHP/ Ruby/ Go/ Python or whatever language you prefer.
* **It has strong community support**. To enhance React's capabilities, open source contributors have built an amazing ecosystem of libraries that enables you to make even more powerful applications. But most open source libraries for React are optional. You don't need to learn them until you've mastered React fundamentals.

The bottom line is that with a low learning curve, React gives you incredible power in making your UI flexible, reusable, and spaghetti-free.

Learning React opens tremendous opportunities if you want to work as a web developer.

### Computer Setup

To start programming with React, you'll need to have three things:

1. A web browser
2. A code editor
3. Node.js

We're going to use the Chrome browser to run our JavaScript code, so if you don't have it, [you can download it here](https://www.google.com/chrome/).

The browser is available for all major operating systems. Once the download is complete, install the browser on your computer.

Next, you'll need to install a code editor if you don't already have one. There are several free code editors available on the Internet, such as Sublime Text, Visual Studio Code, and Notepad++.

Out of these editors, my favorite is Visual Studio Code, because it's fast and easy to use.

#### How to install Visual Studio Code

Visual Studio Code, or VSCode for short, is an application created for the purpose of writing code. Aside from being free, VSCode is fast and available on all major operating systems.

You can [download Visual Studio Code here](https://code.visualstudio.com/).

When you open the link above, there should be a button showing the version compatible with your operating system as shown below:

![Image](https://www.freecodecamp.org/news/content/images/2024/02/1-installvscode-2.png)
_Downloading Visual Studio Code_

Click the button to download VSCode, and install it on your computer.

Now that you have a code editor installed, the next step is to install Node.js

#### How to install Node.js

Node.js is a JavaScript runtime application that enables you to run JavaScript outside of the browser. You need to install this application on your computer to install packages required in React development.

You can download and install Node.js from [https://nodejs.org](https://nodejs.org/). Pick the recommended LTS version because it has long-term support. The installation process is pretty straightforward.

To check if Node has been properly installed, type the command below on your command line (Command Prompt on Windows or Terminal on Mac):

```sh
node -v

```

The command line should respond with the version of the Node.js you have on your computer.

### Your First React Application

It's time to run your first React application. First, create a folder on your computer that will be used to store all files related to this book. You can name the folder 'beginning_react'.

The next step is to open your terminal and run the npm command to create a new React application using Vite.

Vite (pronounced 'veet') is a build tool that you can use to bootstrap a new React project. Inside the 'beginning_react' folder, you need to run the following command to create a new React project with Vite:

```sh
npm create vite@5.1.0 my-react-app -- --template react

```

You should see npm asking to install a new package (create-vite) as shown below. Proceed by typing 'y' and pressing Enter:

```txt
Need to install the following packages:
  create-vite@5.1.0
Ok to proceed? (y) y

```

Then Vite will create a new React project named 'my-react-app' as follows:

```txt
Scaffolding project in /dev/beginning_react/my-react-app...

Done. Now run:

  cd my-react-app
  npm install
  npm run dev

```

When you're done, follow the next steps you see in the output above. Use the `cd` command to change the working directory to the application you've just created, and then run `npm install` to install the packages required by the application.

Then, you need to run the `npm run dev` command to start your application:

```txt
$ npm run dev

> my-react-app@0.0.0 dev
> vite


  VITE v5.0.10  ready in 509 ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
  ➜  press h + enter to show help

```

Now you can view the running application from the browser, at the designated localhost address:

![Image](https://www.freecodecamp.org/news/content/images/2024/02/1-vite-react-demo.png)
_Vite-React Home Page_

This means you have successfully created your first React app. Congratulations!

### Explaining the Source Code

Now that you've successfully run a React application, let's take a look at the source code generated by Vite to understand how things work.

Run the Visual Studio Code you've installed in the previous section, and open the 'my-react-app' folder inside VSCode.

Here, you should see several folders and files that make up the React application as follows:

![Image](https://www.freecodecamp.org/news/content/images/2024/02/1-vite-react-app.png)
_Vite-React Application Structure_

The `vite.config.js` is a configuration file that instructs Vite on how to run the application. Because we have a React application, you'll see the React plugin imported inside:

```js
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
})

```

When you run the `npm run dev` command, Vite will look into this file to know how to run the program.

The `package.json` file stores the information about the project, including the packages required to run the project without any issues. The `package-lock.json` file keeps track of the installed package versions.

The `.eslintrc.cjs` file contains ESLint rules. ESLint is a code analysis tool that can identify problematic code in your project without needing to run the project. It will report any errors and warnings in VSCode.

The `index.html` file is a static HTML document that's going to be used when running the React application, and the `README.md` file contains an introduction to the project.

You don't need to modify any of these files. Instead, let's go to the `src/` folder where the React application code is written.

```txt
src
├── App.css
├── App.jsx
├── assets
│   └── react.svg
├── index.css
└── main.jsx

```

First, the `App.css` file contains the CSS rules applied to the `App.jsx` file, which is the main React application code.

The `assets/` folder contains the assets required for this project. In this case, it's the React icon, which you had seen in the browser.

The `index.css` file is the root CSS file applied globally to the application, and the `main.jsx` file is the root file that access the `index.html` file to render the React application. Here's the content of `main.jsx` file:

```jsx
import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)

```

Here, you can see that the ReactDOM library creates a root at the `<div>` element that contains the `root` ID, then renders the whole React application to that element.

You can open the `App.jsx` file to view the React code:

```jsx
import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div>
        <a href="https://vitejs.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.jsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App

```

In this file, a single component named `App` is defined. The Vite and React logos are rendered with a link to the respective library, and there's a counter button that will increment the counter by 1 when you click on it.

This file is where we will be exploring the fundamentals of React. Let's delete everything in this file, and write a simple `App` component that renders a `<h1>` element:

```jsx
function App() {
  return <h1>Hello World</h1>
}

export default App

```

Next, delete the `index.css`, `app.css`, and `assets/` folder. You also need to delete the `import './index.css'` statement in your `main.jsx` file.

If you open the browser again, you should see a single heading rendered as follows:

![Image](https://www.freecodecamp.org/news/content/images/2024/02/1-react-hello-world.png)
_React Output From Code Changes_

Alright! Now you're ready to learn the fundamentals of React. We'll start your first lesson in the next chapter.

## Chapter 2: How to Create React Components

In React, a component is a single independent unit of a user interface (UI). What you write inside a component will determine what should appear on the browser screen at a given time.

In the previous chapter, we created an `App` component that returns a heading element:

```jsx
function App() {
  return <h1>Hello World</h1>
}

export default App

```

A component is made up of a function that returns a single UI element.

When you want a component to render nothing, you can return a `null` or `false` instead of an element.

```jsx
function App() {
  return null
}

```

All React components are saved under the `.jsx` file extension. As you can see in this project, you have `main.jsx` and `App.jsx`.

What is JSX? It's an extension of JavaScript that produces JavaScript-powered HTML elements. We're going to learn about it later.

### How to Return Multiple Elements With Fragments

A component must always return a single element. When you need to return multiple elements, you need to wrap all of them in a single element like a `<div>`:

```jsx
function App() {
  return (
    <div>
      <h1>Hello World!</h1>
      <h2>Learning to code with React</h2>
    </div>
  )
}

export default App

```

But this will make your application render one extra `<div>` element in the browser. To avoid cluttering your application, you can render an empty tag `<>` like this:

```jsx
function App() {
  return (
    <>
      <h1>Hello World!</h1>
      <h2>Learning to code with React</h2>
    </>
  )
}

export default App

```

The empty tag above is a React feature called a Fragment. By using a Fragment, your component won't render an extra element to the screen.

You can also import the `Fragment` module from React to make it explicit as follows:

```jsx
import { Fragment } from 'react';

function App() {
  return (
    <Fragment>
      <h1>Hello World!</h1>
      <h2>Learning to code with React</h2>
    </Fragment>
  )
}

export default App

```

But you don't need to explicitly state the `Fragment` tag. Using an empty tag `<>` is enough.

### How to Render to the Screen

To render a React component into the browser, you need to create a root React component using the ReactDOM library, which you've seen previously when viewing the `main.jsx` file.

You need to have an HTML file as the source from which your React component is rendered. 

Usually, a very basic HTML document with a `<div>` is enough, as you can see in the `index.html` file:

```html
<body>
  <div id="root"></div>
  <script type="module" src="/src/main.jsx"></script>
</body>

```

Next, you render the component into the `<div>` element. 

Notice how ReactDOM is imported from `react-dom` package, and the `document.getElementById('root')` is used to select the `<div>` element below:

```jsx
import React from 'react'
import ReactDOM from 'react-dom/client'

function App() {
  return <h1>Hello World!</h1>
}

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)

```

Here, you can see that the `App` component is placed in the same file as the ReactDOM library. You can do this if you want to remove the `App.jsx` file, so you have only a single `main.jsx` file as the source for your React application.

But it's confusing to have multiple components in one file, so let's not do this.

### How to Write Comments in React

Writing comments in React components is similar to how you comment in regular JavaScript code. You can use the double forward slash syntax `//` to comment any code.

The following example shows how to comment the `export` statement:

```jsx
function App() {
  return (
    <>
      <h1>Hello World!</h1>
      <h2>Learning to code with React</h2>
    </>
  )
}

// export default App

```

When you want to comment the code inside the `return` statement, you need to use the curly brackets, forward slash, and asterisk format `{/* comment here */}` as shown below:

```jsx
function App() {
  return (
    <>
      <h1>Hello World!</h1>
      {/* <h2>Learning to code with React</h2> */}
    </>
  )
}

```

It may seem very annoying that you need to remember two different ways of commenting when writing React applications. But don't worry, because a modern tool like VSCode knows how to generate the right comment syntax.

You only need to press the comment shortcut, which is `CTRL + /` for Windows/ Linux or `Command + /` for macOS.

### How to Compose Multiple Components as One

Up until this point, you've only rendered a single `App` component to the browser. But applications built using React can be composed of tens or hundreds of components.

**Composing components** is the process of forming the user interface by using loosely coupled components. It's kind of like making a house out of Lego blocks, as I will show you in the following example:

```jsx
export default function ParentComponent() {
  return (
    <>
      <UserComponent />
      <ProfileComponent />
      <FeedComponent />
    </>
  );
}

function UserComponent() {
  return <h1> User Component </h1>;
}

function ProfileComponent() {
  return <h1> Profile Component </h1>;
}

function FeedComponent() {
  return <h1> Feed Component</h1>;
}

```

From the example above, you can see how the `<ParentComponent>` renders three children components:

* `<UserComponent>`
* `<ProfileComponent>`
* `<FeedComponent>`

The composition of many components will form a single tree of React components in a top-down approach.

The tree will then be rendered into the DOM through the `ReactDOM.render()` method:

![Image](https://www.freecodecamp.org/news/content/images/2024/02/2-react-tree.png)
_React Component Tree Illustrated_

By composing multiple components, you can split the user interface into independent, reusable pieces, and develop each piece in isolation.

## Chapter 3: Making Sense of JSX

In the previous chapter, you learned that a component must always have a `return` statement that contains elements to render on the screen:

```jsx
function App() {
  return <h1>Hello World</h1>
}

```

The tag `<h1>` looks like a regular HTML tag, but it's actually a special template language included in React called JSX.

JSX is a syntax extension that produces JavaScript powered HTML elements. It can be assigned to JavaScript variables and can be returned from function calls. For example:

```jsx
function App() {
  const myElement = <h1>Hello World</h1>
  return myElement
}

```

Because of JSX, you can also embed JavaScript expressions inside an element by using curly brackets `{}`:

```jsx
const lowercaseClass = 'text-lowercase';
const text = 'Hello World!';
const App = <h1 className={lowercaseClass}>{text}</h1>;

```

This is what makes React elements different from HTML elements. You can't embed JavaScript directly by using curly braces in HTML.

Instead of creating a whole new templating language, you just need to use JavaScript functions to control what is being displayed on the screen.

### How to Render a List Using JSX

For example, let's say you have an array of users that you'd like to show:

```jsx
const users = [
  { id: 1, name: 'Nathan', role: 'Web Developer' },
  { id: 2, name: 'John', role: 'Web Designer' },
  { id: 3, name: 'Jane', role: 'Team Leader' },
]

```

You can use the `map()` function to loop over the array:

```jsx
function App() {
  const users = [
    { id: 1, name: 'Nathan', role: 'Web Developer' },
    { id: 2, name: 'John', role: 'Web Designer' },
    { id: 3, name: 'Jane', role: 'Team Leader' },
  ]

  return (
    <>
      <p>The currently active users list:</p>
      <ul>
      {
        users.map(function(user){
          // returns Nathan, then John, then Jane
          return (
            <li> {user.name} as the {user.role} </li>
          )
        })
      }
      </ul>
    </>
  )
}

```

Inside React, you don't need to store the return value of the `map()` function in a variable. The example above will return a `<li>` element for each array value into the component.

While the above code is already complete, React will trigger an error in the console, saying that you need to put a "key" prop in each child of a list (the element that you return from `map()` function):

![Image](https://www.freecodecamp.org/news/content/images/2024/02/3-react-array-warning.png)
_React 'key' Warning on Browser Console_

A prop (short for property) is an input that you can pass to a component when rendering that component. The `key` prop is a special prop that React will use to determine which child element has been changed, added, or removed from the list.

You won't use it actively in any part of your array rendering code, but React will ask for one when you render a list.

It is recommended that you put the unique identifier of your data as the key value. In the example above, you can use the `user.id` data. Here's how you pass a `key` prop for each `<li>` element:

```jsx
return (
  <li key={user.id}> 
    {user.name} as the {user.role} 
  </li>
)

```

When you don't have any unique identifiers for your list, you can use the array `index` value as the last resort:

```jsx
users.map(function(user, index){
  return (
    <li key={index}>
      {user.name} as the {user.role}
    </li>
  )
})

```

Props are one of the ingredients that make a React component powerful. You're going to learn more about it in the next chapter.

### How to Add the Class Attribute

You can add the `class` attribute to your elements by using the `className` keyword:

```jsx
function App() {
  return <h1 className='text-lowercase'>Hello World!</h1>
}

```

The keyword `class` is reserved for JavaScript classes, so you need to use `className` instead.

## Chapter 4: Props and States

Props and states are used to pass data inside React components. Props (or properties) are inputs passed down from a parent component to its child component.

On the other hand, states are variables defined and managed inside the components.

Let's start by understanding props. Suppose you have a `ParentComponent` that renders a `ChildComponent` like this:

```jsx
function ParentComponent() {
  return <ChildComponent />
}

```

You can pass a prop from `ParentComponent` into `ChildComponent` by adding a new attribute after the component name.

In the code below, the `name` prop with the value 'John' is passed to the `ChildComponent`:

```jsx
function ParentComponent() {
  return <ChildComponent name='John' />
}

```

When the component is rendered on the browser, the `ChildComponent` will receive the name prop into the component.

You can access the `props` object by defining it in the function component's argument:

```jsx
function ChildComponent(props){
  return <p>Hello World! my name is {props.name}</p>
}

```

The `props` parameter will always be an object, and any prop you define when rendering the component will be passed as a property to the object.

### How to Pass Down Multiple Props

You can pass as many props as you want into a single child component. Just add the props when using the component as shown below:

```jsx
function ParentComponent() {
  return (
    <ChildComponent
      name="John"
      age={29}
      hobbies={["read books", "drink coffee"]}
      occupation="Software Engineer"
    />
  )
}

```

All the props above will be passed to the ChildComponent's `props` parameter.

You can even pass a function into props like this:

```jsx
function ParentComponent() {
  function greetings() {
    return 'Hello World'
  }

  return <ChildComponent greetings={greetings} />
}

```

In the child component, you can call the function as follows:

```jsx
function ChildComponent(props) {
  return <p>{props.greetings()}</p>
}

```

Note that if you pass anything other than a string as a prop value, you need to put the value in curly brackets (numbers, functions, arrays, objects, and so on)

This is because JavaScript expressions can't be processed by JSX unless you put the expression inside curly brackets.

### Props are Immutable

Immutable means that a prop's value can't be changed no matter what happens.

In the code below, the `ChildComponent` tries to change the value of `props.name` property:

```jsx
function ChildComponent(props){
  props.name = 'Mark';
  return <p>Hello World! my name is {props.name}</p>
}

function ParentComponent() {
  return <ChildComponent name='John'/>
}

export default ParentComponent

```

But you'll get an error in the console as follows:

```txt
Uncaught TypeError: Cannot assign to read only property 'name' of object '#<Object>'

```

As you can see, React props can't be changed once you declare them. But what if your data needs to change as a user interacts with your application? This is where state comes to the rescue.

### State in React

In React, states are arbitrary data that you can declare and manage in your components. To create a state in React, you need to call the `useState` hook as shown below:

```jsx
import { useState } from 'react'

function ParentComponent() {
  const [name, setName] = useState('John')

}

export default ParentComponent

```

In React, hooks are functions that allow you to tap into the features provided by React. The `useState` hook is a function that enables you to put value into the state mechanism.

When calling the `useState()` function, you can pass an argument that will serve as the initial value of the state. The function then returns an array with two elements.

The first element holds the state value, and the second element is a function that allows you to change the state value. You need to use the destructuring array syntax to receive both elements as shown above

You can give any names to the variables returned by `useState`, but it's recommended to use `[something, setSomething]`.

To render the state value, you can embed it into JSX as follows:

```jsx
function ParentComponent() {
  const [name, setName] = useState('John')

  return <h1>Hello {name}</h1>
}

```

If you want to change the value of the `name` variable, you need to use the provided `setName()` function.

But you can't call `setName()` in the component's body, because React will refresh itself anytime you change the state value.

Instead, you can create a button that will change the value of name when you click it:

```jsx
function ParentComponent() {
  const [name, setName] = useState('John')

  return (
    <>
      <h1>Hello {name}</h1>
      <button onClick={() => setName('Mark')}>Change Name</button>
    </>
  )
}

```

In the code above, we create a `<button>` element and add the `onClick` prop, which gets executed anytime we click on the button.

Inside the prop, we pass a function that simply calls the `setName()` function, changing the state value.

### How to Pass State to a Child Component

You can pass the state into any child component. When you need to update the state from a child component, you need to pass the `setSomething` function received from the `useState` hook.

Here's an example of passing a state from `ParentComponent` to `ChildComponent`:

```jsx
function ParentComponent() {
  const [name, setName] = useState('John')

  return <ChildComponent name={name} setName={setName} />
}

```

In the `ChildComponent`, you can call the `setName()` function from `props` like this:

```jsx
function ChildComponent(props) {
  return (
    <>
      <h1>Hello {props.name}</h1>
      <button onClick={() => props.setName('Mark')}>Change Name</button>
    </>
  )
}

```

When the button on the `ChildComponent` is clicked, the value of the `name` state will change. Internally, React will refresh the application and reflect the changes in the user interface.

### How to Use React DevTools to Inspect States and Props

To help ease your development, you can install the React Developer Tools (DevTools for short) to inspect the current state and props value of your components. 

You can [install React DevTool for Chrome here](https://chromewebstore.google.com/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi).

Once installed, open the developer tool and you should have two extra tabs called _Components_ and _Profiler_ as shown below:

![Image](https://www.freecodecamp.org/news/content/images/2024/02/4-react-devtool-chrome.png)
_Opening React DevTool_

Similar to how you can inspect CSS rules applied to HTML elements, you can inspect the state and props of React components using the developer tools. Click the _Components_ tab, and inspect one of the two components we created earlier.

Below, you can see the props and state of the `ParentComponent`, as well as other details:

![Image](https://www.freecodecamp.org/news/content/images/2024/02/4-react-devtool-inspect.png)
_Inspecting Components With React DevTool_

When you click on the button, the state value will change accordingly. You can inspect the `ChildComponent` to view its details. These DevTools will come in handy when you develop React applications.

## Chapter 5: React Conditional Rendering

You can control what output is being rendered by a component by implementing conditional rendering in your JSX code.

For example, let's say you want to switch between rendering the login and logout buttons, depending on the availability of the `user` state:

```jsx
function App(props) {
  const { user } = props

  if (user) {
    return <button>Logout</button>
  }
  return <button>Login</button>
}

export default App

```

You don't need to add an `else` statement in the component because React will stop further processes once it reaches a `return` statement.

In the example above, React will render the logout button when the `user` value is truthy, and the login button when `user` is falsy.

### Partial Rendering with a Regular Variable

When developing with React, there will be cases where you want to render a part of your UI dynamically in a component.

In the example below, the JSX element is stored in a variable called `button`, and that variable is used again in the `return` statement:

```jsx
function App(props) {
  const { user } = props

  let button = <button>Login</button>

  if (user) {
    button = <button>Logout</button>
  }

  return (
    <>
      <h1>Hello there!</h1>
      {button}
    </>
  )
}

```

Instead of writing two return statements, you store the dynamic UI element inside a variable and use that variable in the `return` statement.

This way, you can have a component that has static and dynamic elements.

### Inline Rendering with the `&&` Operator

It's possible to render a component only if a certain condition is met and render null otherwise.

For example, let's say you want to render a dynamic message for users when they have new emails in their inbox:

```jsx
function App() {
  const newEmails = 2

  return (
    <>
      <h1>Hello there!</h1>
      {newEmails > 0 &&
        <h2>
          You have {newEmails} new emails in your inbox.
        </h2>
      }
    </>
  )
}

```

In this example, the `<h2>` element only gets rendered when the `newEmails` count is greater than 0.

### Inline Rendering with the Conditional (Ternary) Operator

It's also possible to use a ternary operator in order to render the UI dynamically.

Take a look at the following example:

```jsx
function App(props) {
  const { user } = props

  return (
    <>
      <h1>Hello there!</h1>
      { user? <button>Logout</button> : <button>Login</button> }
    </>
  )
}

```

Instead of using a variable to hold the `<button>` element, you can simply use the ternary operator on the `user` value and render 'Logout' or 'Login' button according to the variable's value.

## Chapter 6: How to Handle User Events

Under the hood, React has an internal event handler that connects to the native DOM event.

This is why we can add the `onClick` prop to buttons in the previous chapters, which gets executed in response to a click event.

When you call a function in response to events, the `event` object will be passed to the callback function as follows:

```jsx
function App() {
  const handleClick = (event) => {
    console.log("Hello World!");
    console.log(event);
  }
  return (
    <button onClick={handleClick}>
      Click me
    </button>
  )
}

```

When you click on the button above, the `event` variable will be logged as a `SyntheticBaseEvent` object in your console:

![Image](https://www.freecodecamp.org/news/content/images/2024/02/8-react-synthetic-event.png)
_React's SyntheticBaseEvent Log_

The `SyntheticBaseEvent` object is a built-in React object used to interact with the native DOM events. Different browsers have different implementations of the DOM event object, so the `SyntheticBaseEvent` makes React compatible with these browsers.

Whenever a DOM event is triggered, that synthetic event will be handled by React so that you can decide what to do with that event.

The use case for this Synthetic event is the same as the native DOM event. Three of the most common event handlers you're going to use are:

* `onChange`
* `onClick`
* `onSubmit`

You can respond to user interactions like clicking, hovering, focusing or typing on a form input, submitting a form, and so on.

### How to Change the UI By Handling Events

In the previous chapter, you saw how conditional logic can be used to render different outputs.

By combining conditional logic with state, props, and event handlers, you can create a dynamic component that renders different outputs based on the data it currently holds.

For example, suppose you want to show or hide a `<div>` element with a button click. Here's how you do it:

```jsx
import { useState } from 'react';

function App() {
  // State to hold the visibility status of the paragraph
  const [isParagraphVisible, setIsParagraphVisible] = useState(true);

  // Function to toggle the visibility status of the paragraph
  const toggleStatus = () => {
    setIsParagraphVisible(!isParagraphVisible);
  };

  return (
    <>
      <h1>Change UI based on click</h1>
      {isParagraphVisible && (
        <p>This paragraph will be shown/hidden on click</p>
      )}
      <button onClick={toggleStatus}>
        {isParagraphVisible ? 'Hide' : 'Show'} Paragraph
      </button>
    </>
  );
}

export default App;

```

First, you create a state to hold the visibility status of the paragraph using the `useState` hook. The default value of the state is `true`.

Next, a function named `toogleStatus()` is defined. This function will change the `status` value from `true` to `false` and vice versa.

Finally, a `return` statement is added to render the elements to the screen. When the button is clicked, the `toogleStatus()` function will be executed. This will show or hide the paragraph depending on the current status.

By using states, props, and event handlers, the code you write becomes a description of what the user interface should look like. React then takes that description and renders it on the browser.

## Chapter 7: CSS in React

There are 4 common ways you can add CSS in a React application:

1. Inline styling
2. CSS files
3. CSS modules
4. Tailwind CSS

This chapter will explore these 4 different ways to write CSS in React components, and which one you should use when starting a React application.

### React Inline Styling

React components are composed of JSX elements. But just because you're not writing regular HTML elements doesn't mean you can't use the old inline style method.

The only difference with JSX is that inline styles must be written as an object instead of a string. See the example below:

```jsx
function App() {
  return (
    <h1 style={{ color: 'red' }}>Hello World</h1>
  );
}

```

In the style attribute above, the first set of curly brackets is used to write JavaScript expressions. The second set of curly brackets initializes a JavaScript object.

Style property names that have more than one word are written in camelCase instead of using the traditional hyphenated style. For example, the usual `text-align` property is written as `textAlign` in JSX:

```jsx
function App() {
  return (
    <h1 style={{ textAlign: 'center' }}>Hello World</h1>
  );
}

```

Because the style attribute is an object, you can also separate the style by writing it as a constant. This way, you can reuse the style in other elements as needed:

```jsx
const pStyle = {
  fontSize: '16px',
  color: 'blue'
}

export default function App() {
  return (
    <>
      <p style={pStyle}>Hello World!</p>
      <p style={pStyle}>The weather is sunny today.</p>
    </>
  )
}

```

If you need to extend your paragraph style further down the line, you can use the spread operator.

This will let you add inline styles to your already declared style object. See the `<p>` element below:

```jsx
const pStyle = {
  fontSize: '16px',
  color: 'blue'
}

export default function App() {
  return (
    <p style={{ ...pStyle, color: 'green', textAlign: 'right' }}>
      When you go to work, bring your umbrella with you!
    </p>
  )
}

```

JSX inline styles allow you to write CSS directly into your component.

One of the benefits of using the inline style approach is that you will have a simple component-focused styling technique. When using an object for styling, you can extend your style by spreading the object.

But in a big and complex project where you have hundreds of React components to manage, this might not be the best choice for you.

You can't specify pseudo classes using inline styles. That means you can't define rules like `:hover`, `:focus`, `:active`, and so on.

Also, you can't specify media queries for responsive styling. Let's consider another way to style your React app.

### CSS Files

Another way to add CSS in React is to use `.css` files. Vite already knows how to handle a `.css` file, so all you need to do is import the CSS file into your JSX file and add the right `className` prop to your component.

Let's create a `style.css` file in your project folder with the following content:

```css
/* style.css */
.paragraph-text {
  font-size: 16px;
  color: #ff0000;
}

```

Now, let's import the CSS file into the `App.jsx` file and add the class prop to the component:

```jsx
import './style.css';

function App() {
  return (
      <p className="paragraph-text">
        The weather is sunny today.
      </p>
  );
}

```

This way, the CSS will be separated from your JavaScript files, and you can just write CSS syntax as usual.

You can even include a CSS framework such as Bootstrap in React with this approach. All you need to do is import the CSS file in your root component.

This method will enable you to use all CSS features, including pseudo classes and media queries.

### CSS Modules

A CSS module is a regular CSS file with all of its class and animation names scoped locally by default.

When applying this method, each React component will have its own CSS file, and you need to import that CSS file into your component.

To let React know you're using CSS modules, name your CSS file using the `[name].module.css` convention.

Here's an example:

```css
/* App.module.css */
.BlueParagraph {
  color: blue;
  text-align: left;
}
.GreenParagraph {
  color: green;
  text-align: right;
}

```

Then import it to your component file:

```jsx
import styles from "./App.module.css";

function App() {
  return (
    <>
      <p className={styles.BlueParagraph}>
        The weather is sunny today.
      </p>
      <p className={styles.GreenParagraph}>
        Still, don't forget to bring your umbrella!
      </p>
    </>
  )
} 

```

When you build your app, Vite will automatically look for CSS files that have the `.module.css` name and process the class names to a new localized name.

Using CSS Modules ensures that your CSS classes are scoped locally, preventing CSS rules from colliding with each other.

Another advantage of using CSS Modules is that you can compose a new class by inheriting from other classes that you've written. This way, you'll be able to reuse CSS code that you've written previously, like this:

```css
.MediumParagraph {
  font-size: 20px;
}
.BlueParagraph {
  composes: MediumParagraph;
  color: blue;
  text-align: left;
}
.GreenParagraph {
  composes: MediumParagraph;
  color: green;
  text-align: right;
}

```

But we're not going to explore every single feature of CSS modules here, only enough to get you familiar with them.

### Tailwind CSS

Tailwind CSS is a modern utility-first CSS framework that allows you to style elements by combining a bunch of classes together.

CSS frameworks like Bootstrap and Bulma provide you with high-level components that you can immediately use in your project. When you need to style a button, you just need to apply the classes that contain the desired CSS properties:

```html
<button className="btn btn-primary">Subscribe</button>

```

When using Bootstrap, the `btn` class provides a combination of CSS properties such as padding, color, opacity, font weight, and so on.

On the other hand, Tailwind gives you utility classes where each class has only one or two properties:

```html
<button className='px-5 py-2 text-white bg-blue-500 border-2'>
  Subscribe
</button>

```

In the example above, the `px-5` is short for padding `padding-left` and `padding-right`, while 5 is a specific size for the paddings. The `text-white` applies `color: white`, the `bg-blue-500` applies the `background-color` property, and `border` applies `border-width`.

### Which One Should You Use?

It depends on the method you feel comfortable with the most. If you're working with a team, you need to discuss and agree on the method you want to apply, because mixing the styles makes it hard to develop and maintain the application.

Remember: Always use only one way to style React components in a specific project to avoid confusion.

## Chapter 8: How to Build Forms in React

One of the most common interfaces you're going to build as a web developer is a form. In React, you can create a form by using state as the single source of that form's data.

In this chapter, I will show you how to handle form input, form submission, and form validation using React.

### How to Handle Form Input

For example, suppose you want to create a form with a single text input and a button.

You can first set up the state that will serve as the input value:

```js
import { useState } from 'react';

function Form() {
  const [username, setUsername] = useState();
}

```

Next, add the `return` statement and define the form. On the `<input>` element, assign the `username` state as the `value` prop:

```jsx
import { useState } from 'react';

function Form() {
  const [username, setUsername] = useState();
  return (
    <form>
      Username:
      <input type='text' name='username' value={username} />
    </form>
  );
}

```

Next, add the `onChange` prop to the `<input>` element. In that prop, assign the `value` of the text input as the value of the `username` state:

```jsx
import { useState } from 'react';

function Form() {
  const [username, setUsername] = useState();
  return (
    <form>
      Username:
      <input
        type='text'
        value={username}
        onChange={e => setUsername(e.target.value)}
      />
    </form>
  );
}

```

The `e` or `event` object is passed by the `onChange` prop to the callback function. From that object, we can get the value of the text input at `event.target.value` property.

Now whenever the input value changes, the state will be updated to reflect the changes.

### How to Handle Form Submission

The next step is to submit the form. Let's create a function that handles the submit event called `handleSubmit()` as follows:

```jsx
import { useState } from 'react';

function Form() {
  const [username, setUsername] = useState();

  const handleSubmit = (e) => {
    e.preventDefault();
    alert(username);
  }

  return (
    <form onSubmit={handleSubmit}>
      Username:
      <input
        type='text'
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />
      <button>Submit</button>
    </form>
  );
}

```

Here, the `handleSubmit()` function will stop the default form submission behavior, which will trigger a refresh, and then create an alert box to display the `username` value.

The function then gets passed to the `onSubmit` prop of the `<form>` element. A `<button>` is also added so that the user can submit the form.

### How to Handle Form Validation

To handle form validation, you need to create another state that will store the error message. You can name this state `usernameError` as follows:

```jsx
const [usernameError, setUsernameError] = useState();

```

Next, create a `handleUsername()` function that will run when the `username` input changes.

Inside this function, you can call the `setUsername()` function to update the state, and then write logic to validate the input value.

For example, suppose the `username` length must be longer than 6. Here's how you do it:

```jsx
const handleUsername = e => {
  const { value } = e.target;
  setUsername(value);

  // Validate username value:
  if (value.length <= 6) {
    setUsernameError('Username length must be more than 6 characters');
  } else {
    setUsernameError();
  }
};

```

Now that you have some validation logic, you need to set the `handleUsername()` function as the `onChange` prop handler.

Also, add a paragraph below the `<input>` element that will show the error message as follows:

```jsx
return (
  <form onSubmit={handleSubmit}>
    Username:
    <input type='text' value={username} onChange={handleUsername} />
    <p>{usernameError}</p>
    <button>Submit</button>
  </form>
);

```

Inside the `handleSubmit()` function, you can check if there's an error on the form by checking the `usernameError` state, then prevent the form from being submitted when there is an error:

```jsx
const handleSubmit = (e) => {
  e.preventDefault();
  if(usernameError){
    alert('Unable to submit: Form contain errors');
  } else {
    alert(username);
  }
}

```

This way, the form won't be submitted until the error is fixed.

Here's the full source code of the form if you want to try it:

```jsx
import { useState } from 'react';

function App() {
  const [username, setUsername] = useState();
  const [usernameError, setUsernameError] = useState();

  const handleSubmit = (e) => {
    e.preventDefault();
    if(usernameError){
      alert('Unable to submit: Form contain errors');
    } else {
      alert(username);
    }
  }

  const handleUsername = e => {
    const { value } = e.target;
    setUsername(value);
  
    // Validate username value:
    if (value.length <= 6) {
      setUsernameError('Username length must be more than 6 characters');
    } else {
      setUsernameError();
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      Username:
      <input
        type='text'
        value={username}
        onChange={handleUsername}
      />
      <p>{usernameError}</p>
      <button>Submit</button>
    </form>
  );
}

export default App;

```

A form can be as complex or as simple as required, but you'll use the pattern you see here no matter what form you build:

* State values are used as the source of form data and validation
* `onChange` prop as a way to update the state
* Validations are triggered by user inputs
* A `handleSubmit()` function is executed when the form is submitted

Using these building blocks, you can build any form required by your application.

## Chapter 9: Network Requests in React

Modern web applications tend to have a modular architecture, where the back end is separated from the front end. The front end app will need to send an HTTP network request to a remote endpoint.

React doesn't tell you how you should send network requests. The library only focuses on rendering UI with data management using props and states.

To fetch data using React, you can use any valid JavaScript library like Axios, Superagent, and even the native Fetch API.

In this chapter, we're going to see how to do network requests using Fetch in React.

### The useEffect Hook

When you create a React application that needs to synchronize with a system outside of React, you need to use the `useEffect` hook.

This hook allows you to run some code after rendering so that you can synchronize your component with some system outside of React.

When the hook has finished performing the data request, you can set the response into your component states and render the appropriate components based on the state values.

To show you an example, let's fetch data from [https://jsonplaceholder.typicode.com/todos/1](https://jsonplaceholder.typicode.com/todos/1) which is a dummy end point:

```jsx
function App() {
  const [title, setTitle] = useState('');

  useEffect(() => {
    getData();
  }, []);

  const getData = async () => {
    const response = await fetch('https://jsonplaceholder.typicode.com/todos/1');
    const task = await response.json();
    console.log(task)
    setTitle(task.title);
  };

  return <h1>{title}</h1>;
}

```

In the code above, we create an `App` component that has a state called `title`, and we run the Fetch API to get a todo task from the API.

When a response is received, we parse the JSON string into a JavaScript object, log the object, and then set the `title` state to the `task.title` property value.

The response is as follows:

![Image](https://www.freecodecamp.org/news/content/images/2024/02/9-useeffect-log.png)
_React useEffect Log_

Here, you can see that the `console.log()` is called twice. This is because the `<React.StrictMode>` wrapper always runs a `useEffect` hook twice to help you in development.

If you remove the `<React.StrictMode>` wrapper in `main.jsx`, the `useEffect` hook will run only once.

The `useEffect` hook itself is a function that accepts two arguments:

* A callback function to run on every render
* An array of state variables to watch for changes. `useEffect` will be skipped if none of the variables are updated.

When you want to run `useEffect` only once, you can pass an empty array as the second argument to the function, as shown in the example above.

By using the `useEffect` hook, React can send HTTP requests and fetch data from any external system, then store that data in the component state.

## Wrapping Up

Congratulations on finishing this handbook! I hope you found it useful and now feel that learning React is not impossible or confusing at all. All you need is a step-by-step guide that reveals the key concepts of React one by one.

If you're eager to dive deeper into React and expand your skills, I encourage you to check out my new book called _Beginning React_ here:

[![Beginning React Book](https://www.freecodecamp.org/news/content/images/2024/02/beginning-react-promo.png)](https://codewithnathan.com/beginning-react)

The goal of this book is to help you see how to build an application using React. There are two projects included in this book that will give you the "experience" of building a web application using React.

You will see how React concepts like components, JSX, props, states, hooks, and Context API are used to create a dynamic front-end application.

Here's my promise: _You will actually feel confident building web applications from scratch using React._

Thanks for reading!

