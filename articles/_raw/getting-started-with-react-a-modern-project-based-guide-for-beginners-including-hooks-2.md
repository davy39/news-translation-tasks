---
title: How to Get Started with React — A Modern Project-based Guide for Beginners
  (Including Hooks)
subtitle: ''
author: Chris Blakely
co_authors: []
series: null
date: '2020-05-16T13:18:32.000Z'
originalURL: https://freecodecamp.org/news/getting-started-with-react-a-modern-project-based-guide-for-beginners-including-hooks-2
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/getting-started-with-react.png
tags:
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
seo_title: null
seo_desc: "So you want to start learning React, eh? Then you've come to the right\
  \ place. This guide will walk you through everything you need to know when getting\
  \ started with React. \nWe'll get set up, explain the \"hows and whys\" behind the\
  \ basic concepts, and ..."
---

So you want to start learning React, eh? Then you've come to the right place. This guide will walk you through everything you need to know when getting started with React. 

We'll get set up, explain the "hows and whys" behind the basic concepts, and build a small project which pulls data from an API so we can see everything in action.

This will be a long one, so skip/re-read sections as you need using the "Jump to Section" links below. With that out of the way, grab a drink, buckle up, and let's get started.

#### Prefer Video Tutorials?

You can check out the [YouTube tutorial for this article here.](https://youtu.be/bZXjHauDNcg)


## Jump to Section

* [Prerequisites](#heading-prerequisites)
  * [Basic JavaScript](#heading-basic-javascript)
  * [Basic HTML](#heading-basic-html)
* [Development Environment](#heading-development-environment)
  * [Node.js](#heading-nodejs)
  * [VS Code](#heading-visual-studio-code)
* [Creating a React App](#heading-creating-a-react-app)
* [Exploring Create React App](#heading-exploring-create-react-app)
  * [Node Modules](#heading-node-modules)
  * [Public Folder](#heading-public-folder)
  * [Index.html](#heading-indexhtml)
* [Our First Component](#heading-our-first-component)
* [JSX](#heading-jsx)
  * [Making Things Dynamic](#heading-making-things-dynamic)
  * [Handling Events](#heading-handling-events)
  * [Calling Functions](#heading-calling-functions)
* [How a Component gets Rendered](#heading-how-a-component-gets-rendered)
* [Lets Build a Contacts List!](#heading-lets-build-a-contacts-list)
  * [Get the Styles](#heading-get-the-styles)
  * [Creating the Contact Card](#heading-creating-the-contact-card)
  * [Making Our Contact Card Reusable](#makingourcontact-card-reusable)
  * [Lets talk about State](#heading-lets-talk-about-state-the-usestate-hook)
  * [Updating State](#heading-updating-state)
  * [Introducing Props](#heading-introducing-props)
  * [Using Props within a component](#heading-using-props-within-a-component)
  * [Rendering components from a List](#heading-rendering-components-from-a-list)
  * [Pulling data from an API](#heading-pulling-data-from-an-api)
  * [Introducing useEffect](#heading-introducing-useeffect)
* [Conclusion](#heading-conclusion)


## Prerequisites

You don't need to know any React before reading this guide. But there are a few things you will need to be familiar with if you want to get the most out of this React guide:

### Basic JavaScript 

React is a JavaScript library, so it makes sense to know JavaScript before learning React, right? Don't worry, you won't need to know JavaScript inside out — you only need to know the basics:

- Variables, functions, data types
- Arrays and Objects
- ES6 Syntax (using let & const, Arrow Functions, Destructuring Assignment, classes, importing/exporting, etc)
- How JavaScript is used to manipulate the DOM 

### Basic HTML 

In React, we use what's called **JSX** to create the HTML for our webpages. We'll explain JSX in depth later, but for now make sure you have a good foundation when it comes to HTML:

- How to structure HTML (how to nest elements and so on)
- HTML attributes (like "id", "class", "onclick" and so on)


>  [Need some JavaScript review? Subscribe to get my latest book "React-Ready JavaScript" which will help you get ramped up on the JavaScript you need before getting started with React!](https://subscribe.jschris.com)


## Development Environment

The first thing we're going to do is set up a development environment. If you've already setup **Node.js** and installed **Visual Studio Code** (or your preferred IDE), you can go ahead and skip to the next section.

### Node.js

[Go here and download](https://nodejs.org/en/download/) the right package for your OS (Mac/windows etc)

When the installation completes, open a terminal  and type this command: 

```js
node -v
```

This should show output the version of Node you just installed:

![](https://jschris.com/static/75f85dfa0c07e6b38092fb8eb832a189/b5cea/node.png)

This means that the `node` command works and node has installed successfully — hurray! If you see any errors, try reinstalling Node from the package you downloaded and retry the command again.

### Visual Studio Code

Visual Studio Code is a popular open-source IDE that works well for frontend development. There are a bunch of others you can try — see what your favourite is and download that if you prefer. For now, we'll run with VS Code.

[Click here and download](https://code.visualstudio.com/download) the version for your platform: 

Follow the installation steps, and you should be good to go. Go ahead and fire up Visual Studio Code.

That's enough development setup for now. There are other nice things you can install (VS Code extensions etc) but we don't need those right now —We're here to learn React!

## Creating a React App

The next step is to create a React project. Lucky for us, the fine folk at Facebook have made this really simple. All we have to do is run a command within our terminal:

```jsx
npx create-react-app my-app
```

This creates a project for us called "my-app" and sets everything up automatically. Pretty cool.

Go ahead and open up a terminal in the directory you want to create your app, e.g. a "projects" folder, and run the command. Let the terminal do its thing, and after a while, this will complete and show you some commands:

![](https://jschris.com/static/9d651a0597f10abac0a8687011b437f1/78363/cra-install.png)

Notice the **create-react-app** output has told us what we need to do to start the app. Go ahead and run the commands in your terminal:

```
cd my-app
yarn start
```

This will start a development server and open up a web browser for you:

![](https://jschris.com/static/a1a4aeb3c265e6753ce67bb5e9c66fe0/cb922/cra-start.png)

You've just set up your first React App! If you want to learn more about what's going on, (check out the "create-react-app" GitHub:)[https://github.com/facebook/create-react-app]

## Exploring Create React App 

Open up Visual Studio code (or whatever IDE you installed) and select **File > Open…** and select the **my-app** folder that was just created for us using *create-react-app*. This will open up our shiny new react app in the IDE, so we can write some code! 

You should see the project structure to the right:

![](https://jschris.com/static/64e7647ba04867a1c923bd3d1bac51d9/fdaf8/project-tree.png)


Look at all that stuff! Don’t worry too much about a lot of it, it’s mostly boilerplate code and config that we won’t be touching too much in this tutorial — phew! However since you’re a curious developer, let’s have a look at the **project tree** and see what we have:

### Node Modules
This is where our packages go that we install through NPM (Node Package Manager). If you’re not familiar with NPM, it’s a glorious place where we can share code (usually open source) that other developers can use instead of writing their own. 

Instead of using **script tags** like we do in traditional HTML, we install these modules as part of the application. Then, we use an **import statement** to access the code from that module. We’ll see this in action later.

### Public Folder
This is where our bundled code goes. When we are ready to deploy our app, we run a ** build script**and the final files go in here. This will typically be our HTML, JavaScript, and CSS files. This is the folder we dump onto a web server somewhere, so that we can let users see our app via a URL

### Index.html
The **index.html** is the entry point, or the first thing the web browser loads when a user navigates to the URL hosting our app. 

If we look at the file, it’s a just a normal HTML file with normal HTML stuff that you will hopefully be familiar with. If we look at the body — it’s empty. React will dynamically convert our React code into HTML and load it here, in the “root” div.

With that out of the way, let’s look at the juicy parts — the code.

## Our First Component
Open up **App.js** from the project tree. This is the Main component in our application. This is the first component to get rendered. It’s the “big cheese” of components.

The first thing we’re going to do in our big cheese component is delete everything, and build our very own component from scratch, to better understand what’s going on.

Now that we have a nice blank slate to play with we will start by importing **react**. This brings the React library into _scope_ and gives us access to all the lovely features:

```jsx
import React from "react";
```

Next we will declare a function. We’ll use ES6 arrow functions here. That’s more or less what a “component” is — a function with some logic and markup. We’re also going to export this function so we can use it elsewhere:

```JSX
const App = () => {

}

export default App;

```

Within our function we want to write `return()`. This is what get’s _returned_ from this component, and contains our markup which gets converted and rendered as HTML. 

Finally let’s add a `<div>` with a `<h1>` title tag. Our finished component looks like this:

```jsx
import React from "react";

const App = () => {
  return (
    <div>
       <h1>Hello React World</h1>
       <h2>
             This is our first React App - isn't it marvellous?!
       </h2>
    </div>
  );
}

export default App;
```


Now you’re probably thinking, "Woah! HTML in a function? What is this madness?" Even though it looks like HTML, it’s actually something called **JSX (JavaScript XML)**. This basically allows us to mix JavaScript and HTML together.

This might seem a bit strange. We originally learned front end development by separating our HTML and JavaScript (and even CSS). Yet JavaScript and the way we design apps has evolved, and keeping everything together in the same “component” makes it easier to maintain and reuse our code.

Let’s see this in action. Open your terminal and run

```
npm start
```

This should open the browser and you should see the app running.


Congrats! You’ve just created your first component!

## JSX

You probably have some question marks floating above your head when thinking about this JSX thing. Let’s take a deeper look into this.

```jsx
  return (
    <div>
      <h1>Hello React World</h1>
      <h2>
          This is our first React App - isn't it marvellous?!
      </h2>
    </div>
  );
```


This looks like HTML, but it’s not. This is **JSX**! Even though it looks like normal HTML, what’s happening behind the scenes is that React is **creating the element tree**, using this syntax:


```jsx
React.createElement(component, props, ...children)
```

- component: The **HTML element** you wish to created, i.e. `h1`, `div` etc
- props: any `props` you wish to pass to that component (we’ll talk about props later)
- children: An **array of HTML elements** that are nested within this element

So, the same component we have just created can be written as so:

```jsx
const App = () => {
  return (
    React.createElement(
      "div",
      null,
      React.createElement("h1", null, "Hello React World"),
      React.createElement(
        "h2",
        null,
        "This is our first React App - isn't it marvellous?!"
      )
    )
  );
}
```


Which looks a bit nasty (it was even nastier trying to type it out). If you trace through it carefully, you can see we are creating a `div` element, which has no props (indicated by passing `null` as a second argument). Lastly we are creating 2 more elements using the `createElement` syntax — our `H1` and our `H2` elements.

If you’ve been playing with JavaScript for a while, you might have noticed that this is similar to `document.createElement`.  And it is! This is a JavaScript library after all! 

This is the advantage of JSX in React — it lets us write HTML like syntax, without the messy `React.createElement()` stuff.

In the real world, React developers almost exclusively use JSX to write their code. No, this section wasn’t a waste of time — it’s always good to understand what happens under the hood. Knowledge is power (and less questions in my inbox)!


###Making things dynamic

So we’ve seen JSX, and gotten over our fear of it (hopefully). But what’s the point? Why use this JSX thing, when we could just use HTML? They look the same? Right?

Good question my friend! Well, if we remember what JSX stands for — JavaScript XML. This means we can use JavaScript to make things dynamic. Our previous example looks like so:


```jsx
const App = () => {
  return (
    <div>
      <h1>Hello React World</h1>
      <h2>This is our first React App - isn't it marvellous?!</h2>
    </div>
  );
}
```


Now let’s say we want to make our text more dynamic. Firstly let’s add a variable to hold our message:

`cont message = "This is my first variable rendered in JSX!"`

Now to add JavaScript to this, we use ** curly braces**: 

```jsx
const App = () => {
  const message = "This is my first variable rendered in JSX!";

  return (
    <div>
      <h1>Hello React World</h1>
      <h2>{message}</h2>
    </div>
  );
}
```

If you run this in the browser, you’ll notice the text of our message variable appears. Go ahead and change the message variable text to something else and watch the magic happen. 

We use **curly braces** to tell the compiler “**_execute this code as JavaScript_**”. If we didn’t have curly braces, the **message** variable wouldn't get executed as JavaScript and instead, the text “message” would appear on the screen. Try this out and see! 


### Handling Events
The same approach can be taken when with handling events. When using JSX, React gives us access to **event listeners**  you may already be familiar with: **onClick**, **onPress**, **onSubmit** and so on. 

Let’s say we want to display an alert when the message is clicked. Firstly, we add the **onClick** property to our **h2** tag. 

The **onClick** property accepts a function (in other words, we pass a function as an argument. This function will call the alert like so:

```jsx
const App = () => {
  const message = "This is my first variable rendered in JSX!";  

  return (
    <div>
      <h1>Hello React World</h1>
      <h2 onClick={()=> alert("you clicked the message!")}>{message}</h2>
    </div>
  );
}
```

Notice how we use a **arrow** function here to create a nice, concise inline function. If you’re not familiar with this syntax, make sure to [checkout my book where I cover this and more here](https://subscribe.jschris.com).

Again, notice how we have put this code within **curly braces**, to ensure the function gets executed as JavaScript.

### Calling functions

So we looked at inline functions in the last example. Since JSX is JavaScript, we can create and reference functions **outside of the return block**. Our last example could look like this:

```jsx
const App = () => {
  const message = "This is my first variable rendered in JSX!";  

  const handleClick = () =>{
	alert("you clicked the message!");
  }

  return (
    <div>
      <h1>Hello React World</h1>
      <h2 onClick={handleClick}>{message}</h2>
    </div>
  );
}
```

Notice how we created a function called **handleClick** which alerts the message. Instead of using an inline function, we reference this function in our **onClick** property. Try this out and see what happens.

These are just some examples as to how we can use JavaScript to make things dynamic, and hopefully shows you the power of JSX. We’ll deepen our understandings later as we build out an example, so don't worry if some things don’t make sense just yet!

## How a Component gets Rendered

Hopefully I’ve cleared up some of the questions you might have around JSX. The next thing you might be wondering is — how does a component get rendered? Where? When? 

Let’s start at the beginning. If you look back to our file structure we have an **index.js** file. This is the first file to run (we often call this an “Entry Point”). This is typically by convention — you can change the entry point if you want, but for now we’ll leave it alone. 

If we dig into the file, you’ll notice we have this line:

```jsx
ReactDOM.render(<App />, document.getElementById("root"));
```

Notice we have `document.getElementById(“root”)` — finally some normal looking JavaScript! This gets the **root** element from the DOM using plain ol’ JavaScript, and renders our App Component within it. Our App component is imported like so:

```jsx
import App from "./App"
```

Remember we _exported_ our app component in App.js. This lets other files/components import and use our App component.

So where does the **root** element come from? Well, remember our *index.html* file in the public folder? This index.html file is the first HTML file to get loaded when the website loads 

Within it we have a `div` with an ID of `root`, which is empty. This is where React loads our components. Let’s have a look at this in the dev tools.

Open up Chrome (or whatever browser you use) and inspect the dev tools. You’ll see somewhere in the tree a **div with id=“root”**, as well as the **HTML rendered from our App component**. Pretty cool!

![](https://jschris.com/static/48936a3669e8feaa26c72f9908400f73/fbdcb/id-root-dev-tools.png)

## Quick Summary

Before moving on, let’s quickly summarise what we’ve learned so far:

- We have an *index.html* file, which is the skeleton of our web app
- When the app starts, *index.html* loads, and imports our App Component
- The JSX in the App component get’s converted to HTML, which is then rendered in the **index.html file at the root div**

##  Lets Build a Contacts List! 

Now that we have our feet wet with React, and have a better understanding of how things fit together, let’s build an example application using what we have learned so far. We’ll also learn some common React features that will help you well on to the road to getting started with React. Let’s go!

Our contacts list will display a number of a contacts, including their name, email, age and avatar (or, profile image). 
We’ll build this up gradually, eventually pulling data from an API. How exciting! 
  
![](https://jschris.com/static/093da2b0c6947b52d83b42183d172718/6569d/contacts-list-intro.png)

## Get the styles

Since this is a React tutorial, we’re going to focus on the inner workings of React and not worry about creating nice styles. In your source folder, create a new file `styles.css` and paste in the following code:

```css
.contact-card {
  display: flex;
  padding: 10px;
  color: #ffffff;
  background-color: rgb(42, 84, 104);
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
  box-shadow: 10px 10px 25px -16px rgba(0, 0, 0, 0.75);
  border-radius: 10px;
  max-width: 500px;
  max-height: 125px;
  margin-bottom: 10px;
}

.contact-card p {
  margin-left: 10px;
  margin-top: 0;
}

button {
  margin-left: 10px;
  margin-bottom: 10px;
}
```

Next, go into **App.js** and import the stylesheet like so:

```jsx
import "./styles.css";
```
 
## Creating the Contact Card

While we’re still in **App.js**,  let’s add the basic JSX to get our layout for the contact card in place. Remove everything from the **return** statement and add the following:

```jsx 
<div className="contact-card">
	<img src="https://via.placeholder.com/150" alt="profile" />
	<div className="user-details">
		<p>Name: Jenny Han</p>
		<p>Email: Jenny.Han@notreal.com</p>
		<p>Age: 25</p>
	</div>
</div>
```

All we’re doing here is creating a **div** to “wrap” the contact card details, adding an image (the image will use a placeholder taken from the web for now), and adding a few **p** tags to hold the details we need in the contact card. Finally we’re adding some **CSS classes** taken from `styles.css`;

> NOTE: to reference CSS classes, we need to use the **className** keyword. This is because we are writing JSX, and “class” is a reserved word in JavaScript.

Here’s what we have so far in our **App.js** file:

```jsx
import React from "react";
import "./styles.css";

const App = () => {
  return (
    <div className="contact-card">
      <img src="https://via.placeholder.com/150" alt="profile" />
      <div className="user-details">
        <p>Name: Jenny Han</p>
        <p>Email: Jenny.Han@notreal.com</p>
        <p>Age: 25</p>
      </div>
    </div>
  );
}
```

If you run this in the browser, you should see something similar to the following:

![](https://jschris.com/static/adff13952d09891bcb6c1d1c7a694bb9/89048/contac-card-template.png)

## Making our Contact Card Reusable 

OK so we have our contact card! However it’s not very reusable. We know that we are going to need to **reuse this code** if we want to render more than one card, so it makes sense to break this out **into it’s own component**

> NOTE — To make it easier to follow, I am going to a put all the components we make into **App.js** . In the real world it would be better to split these different components into their own files, and import/export them where appropriate.

Just beneath the **App** function, create a new function called **ContactCard**, and copy the JSX from **App** to  **ContactCard** like so:

```jsx
const ContactCard = () => {
  return (
    <div className="contact-card">
      <img src="https://via.placeholder.com/150" alt="profile" />
      <div className="user-details">
        <p>Name: Jenny Han</p>
        <p>Email: Jenny.Han@notreal.com</p>
        <p>Age: 25</p>
      </div>
    </div>
  );
};
```

Again, a component in React is just a **function that returns some JSX**.  Now that we’ve moved our JSX to the **ContactCard** we can use this component within our main **App component**:

```jsx
const App = () => {
  return (
    <>
      <ContactCard />
    </>
  );
}
```

We use our own components like any old HTML/JSX tag. We just put the **name of our component in angle brackets.** Our **App.js** file should look like this:

```jsx
// App.js
import React from "react";
import "./styles.css";

const App = () => {
  return (
    <>
      <ContactCard />
    </>
  );
};

const ContactCard = () => {
  return (
    <div className="contact-card">
      <img src="https://via.placeholder.com/150" alt="profile" />
      <div className="user-details">
        <p>Name: Jenny Han</p>
        <p>Email: Jenny.Han@notreal.com</p>
        <p>Age: 25</p>
      </div>
    </div>
  );
};
```

Now if you run this in the browser, things will look the same as they did before — which is what we want. We now have a **ContactCard** component that we can use as many times as we like:

```jsx
const App = () => {
  return (
    <>
      <ContactCard />
      <ContactCard />
      <ContactCard />
    </>
  );
};
```

Update the **App** component to include another 2 **ContactCard** components. The above example will render 3 contact cards in the browser. Go and check it out!

> Think of this like a “stamp” on the page. Every **ContactCard** component we add is another “stamp” and renders the same markup on the page

## Let’s talk about State — the useState Hook

If you’ve been getting started with React already, you may have heard of the term **state**. State is quite a big deal in React. So what is it?

> State is basically an object that represents a part of an app that can change, which the UI “reacts” to. State can be anything; objects, booleans, arrays, strings or integers 

Let’s take an example.

Some people who appear in our contact list are shy and do not want their age being displayed until a button is clicked. We can store **whether the age should be shown or not** in state by using the **useState hook within the component**. Which looks like this:

```jsx
const [showAge, setShowAge] = useState(false);
```

“What the hell is going on here?” Let me explain.

The **useState object** gives us a variable with the **current value**, and a function that **lets us change that value**. When we call **useState** we can define an **initial**value (in this case, **false**).

We use **destructuring assignment** on the **useState hook** to get these. You don’t have to worry about destructuring assignment right now, just remember that the first variable lets us access the state value, the second one lets us change it.

Go ahead and add the above code snippet to the **ContactCard** component like so:

```jsx
const ContactCard = () => {
  const [showAge, setShowAge] = useState(false);

  return (
    <div className="contact-card">
      <img src="https://via.placeholder.com/150" alt="profile" />
      <div className="user-details">
        <p>Name: Jenny Han</p>
        <p>Email: Jenny.Han@notreal.com</p>
        <p>Age: 25</p>
      </div>
    </div>
  );
};
```

Now we have a state object, how do we use it? Well, we can reference the `showAge` variable like any other variable. In this case, we want to _only show the age if the `showAge` variable is `true`. 

We can do this using the _ternary operator_ :

```jsx
{showAge === true ? <p>Age: 25</p> : null}
```

This example reads as _if the showAge variable is true, render the age, if not, render nothing_.

Go ahead and add this to the **ContactCard** component, like so:

```jsx
const ContactCard = () => {
  const [showAge, setShowAge] = useState(false);

  return (
    <div className="contact-card">
      <img src="https://via.placeholder.com/150" alt="profile" />
      <div className="user-details">
        <p>Name: Jenny Han</p>
        <p>Email: Jenny.Han@notreal.com</p>
        {showAge === true ? <p>Age: 25</p> : null}
      </div>
    </div>
  );
};
```

Now, if you run the app in the browser, you’ll see the **age** disappears — that’s because our `showAge` variable has been initialised with `false`. If we initialise our `showAge` variable with `true`:

```js
const [showAge, setShowAge] = useState(true);
```

The age will appear on the contact card. Nice! Although, its not great — we don’t want to change the code whenever we want to show the age on the contact card! 

Before we look at how to dynamically change our `showAge` variable, lets tidy the code a bit. Go ahead and replace this line:

```js
{showAge === true ? <p>Age: 25</p> : null}
```

With:

```js
{showAge && <p>Age: 25</p> }
```

This gives the same result, just in a more concise way.

> TIP: Shorten code where it makes sense to, don’t feel like you have to shorten every line of code you write! Readability should come first. 

## Updating State

Ok back to updating state. If we remember back, the `useState()` hook gives us a **function to update the state**. Let’s wire this up to a button, which, when clicked, will toggle showing the age on the contact card.

We can do this with the following:

```jsx
<button onClick={() => setShowAge(!showAge)}>
	Toggle Age 
</button>
```

What this is doing is calling the **setShowAge function** (which we get from the useState hook) to change the **value of show age to the opposite of what it currently is**.

> NOTE: I’m using the **Arrow Function** syntax here to pass a function to the `onClick` property. If you’re not familiar we this, a quick reminder that you can get my [book where I discuss the important bits of JavaScript to know before React here].

When the state updates, React will **re-render the component** and since the value of `showAge` is true, the age will be displayed. 

If the user clicks the button again, this will set `showAge` to `false`, React will re-render the component, and the age will be hidden:

![](https://jschris.com/46201add1931d222dde4782768435378/age-toggle.gif)

Look at our fancy toggle in action! 

> TIP: Whenever the components state changes, React will re-render the component with the new state

Notice how even though we have 3 **ContactCard** components being rendered, when we click the button the age only displays for **one** of the cards, and not all of them. This is because **state belongs to the individual component**. In other words, each **ContactCard** component that renders is a **copy**, and has its own state/data.


## Introducing Props

So now we have a lovely new **ContactCard** component that we’re reusing a few times. Although its not really reusable, since the name, email, age and avatar are the same for each of our components. Oh dear! We can make this data more dynamic with what are called **props**. 

Since you’re just getting started with React, you can think of**Props** as data that gets passed to a component, which the component can then use. For example, we can pass in our **avatar** , ** email**, **name** and **age** as props to our **Contact Card** component like so:

```jsx
<ContactCard
  avatar="https://via.placeholder.com/150"
  name="Jenny Han"
  email="jenny.han@notreal.com"
  age={25}
/>
```

As you can see, we define a prop by giving it a name. Eg. *name* and using the **equals** to assign some value to that prop e.g. **Jenny Han**.

We can have as many props as we want, and we can name these props whatever we want, so they’re pretty flexible. 

Props can hold different types of data, i.e. strings, numbers, booleans, objects, arrays and so on. 

> NOTE: Props must be defined using quoted text (e.g. name=“Jenny Han”) or within braces (e.g. `age={25}`. If we leave out the braces for anything other than strings things start to break — `age=25` );

Go ahead and replace the current **ContactCard** components within  our **App** component with the following:

```jsx
<ContactCard
  avatar="https://via.placeholder.com/150"
  name="Jenny Han"
  email="jenny.han@notreal.com"
  age={25}
/>

<ContactCard
  avatar="https://via.placeholder.com/150"
  name="Jason Long"
  email="jason.long@notreal.com"
  age={45}
/>

<ContactCard
  avatar="https://via.placeholder.com/150"
  name="Peter Pan"
  email="peter.pan@neverland.com"
  age={100}
/>
```

 
All we’re doing here is passing **the data that the component needs** to each component as props. Notice how the data is different for each component.

## Using Props within a component

We’ve sent a bunch of props down to the **ContactCard** component, so let’s tell the ** ContactCard** how to use them.

Until now, our ** ContactCard** function doesn’t accept any _parameters_. React, being the magical thing that it is, automatically puts all our props into a lovely **props object**, that gets passed into the component:

```jsx
const ContactCard = props => {
	//...other code
};
```

Notice the **props** variable. This is an object containing the props we defined previously.  We can _access our defined props_ by using the _dot notation_ like so:

```jsx
const ContactCard = props => {
	console.log(props.avatar); 
	console.log(props.name);
	console.log(props.email);
	console.log(props.age);

	//...other code
};
```

Finally, we want to replace the hardcoded values in our JSX, with the values we receive from the props:

```jsx
return (
  <div className="contact-card">
    <img src={props.avatar} alt="profile" />
    <div className="user-details">
      <p>Name: {props.name}</p>
      <p>Email: {props.email}</p>
      <button onClick={() => setShowAge(!showAge)}>Toggle Age </button>
      {showAge && <p>Age: {props.age}</p>}
    </div>
  </div>
);
```

Notice how we have set the **image source** using whatever value we received from props. We did similar for **name**, **email**, and **age**.  Also notice how we wrap this code in **curly braces**, so it gets executed as JavaScript.

Our final **App.js** file looks like this:

```jsx
// App.js
const App = () => {
  return (
    <>
      <ContactCard
        avatar="https://via.placeholder.com/150"
        name="Jenny Han"
        email="jenny.han@notreal.com"
        age={25}
      />
      <ContactCard
        avatar="https://via.placeholder.com/150"
        name="Jason Long"
        email="jason.long@notreal.com"
        age={45}
      />
      <ContactCard
        avatar="https://via.placeholder.com/150"
        name="Peter Pan"
        email="peter.pan@neverland.com"
        age={100}
      />
    </>
  );
};

const ContactCard = props => {
  const [showAge, setShowAge] = useState(false);

  return (
    <div className="contact-card">
      <img src={props.avatar} alt="profile" />
      <div className="user-details">
        <p>Name: {props.name}</p>
        <p>Email: {props.email}</p>
        <button onClick={() => setShowAge(!showAge)}>
			Toggle Age 
		</button>
        {showAge && <p>Age: {props.age}</p>}
      </div>
    </div>
  );
};
```

If you run this in the browser, you should see something similar to this:

![](https://jschris.com/static/a01167e9d19e96ec4689edbe74bfbdcc/d56e1/contact-lists-3-components.png)

Hurray! Our component works the same as before, but its now more dynamic. We can reuse the same **ContactCard** but passing in different data — whilst keeping the layout, styles, and state objects the same.

## Rendering components from a List

Our contacts list is coming along nicely, we have some well crafted, reusable code so time to leave it alone right? Wrong! Let’s take it a step further.

In a real application, data usually comes in the form of an array of data, e.g. after an API call. Let’s pretend we’ve made an API call to **retrieve some users from a database** and have received the following data:

```js
const contacts = [
    { name: "Jenny Han", email: "jenny.han@notreal.com", age: 25 },
    { name: "Jason Long", email: "jason.long@notreal.com", age: 45 },
    { name: "Peter Pan", email: "peter.pan@neverland.com", age: 100 }
];
```

Paste this into the **App()** component at the top of the function. The eagled eye amongst you will notice how this data is similar to what we already have. But how we we turn this data into **ContactCard** components? Well, remember all those days you spent learning how to loop over an array using **.map()**? Now is the day we put that into action!

To display a list of components, we:

1) Loop over the array using **.map()**
2) For each item in the array, create a new **ContactCard component**
3) Pass the data from each object in the array to the **ContactCard component** as props

Let’s see how this works. In our app**App()** component, replace the **return** statement with this:

```jsx
return (
  <>
    {contacts.map(contact => (
      <ContactCard
        avatar="https://via.placeholder.com/150"
        name={contact.name}
        email={contact.email}
        age={contact.age}
      />
    ))}
  </>
);
```

As you can see, we **map over the array**. For each object in the array, we want to create a new **ContactCard** component. For the props, we want to take the **name**,  **email**, and **age** from the **current object the map function is on**. In other words, from the **contact** variable.

> NOTE: I’ve left the “avatar” prop alone, as this is the same for now — it’ll change later in the tutorial

And that’s it! Our **App.js** file looks like this:

```jsx
//App.js
const App = () => {
  const contacts = [
    { name: "Jenny Han", email: "jenny.han@notreal.com", age: 25 },
    { name: "Jason Long", email: "jason.long@notreal.com", age: 45 },
    { name: "Peter Pan", email: "peter.pan@neverland.com", age: 100 },
    { name: "Amy McDonald", email: "amy@email.com", age: 33 }
  ];

  return (
    <>
      {contacts.map(contact => (
        <ContactCard
          avatar="https://via.placeholder.com/150"
          name={contact.name}
          email={contact.email}
          age={contact.age}
        />
      ))}
    </>
  );
};
```

Run this in the browser and things should look the same. We haven’t changed our **ContactCard**, merely changed where we got the data from. The cool thing about this is that if you added another row to the **contacts** array,  the extra component will get rendered automatically — you don’t have to do anything else! Try this for yourself and see.

## Pulling data from an API
We’ve got a nice looking React App now. It's dynamic and things are working well. Which is a good place to be since we’re just getting started with React! But there are some tidy ups we need to make. In a real application, **data will be pulled in from an API**.

For the next part of the tutorial, we are going to get real contacts (when I say real contacts, I mean fake contacts — you know what I mean) from a real API: [https://randomuser.me/](https://randomuser.me/). Feel free to browse the website and look at the response we will get back — this is where we will get our data to populate our components.

Firstly, let’s create a **state variable** to hold the data we get back from the API. Remember, state is good for holding that that can change. Our contacts list can definitely change!

In **App.js**, remove the **contacts** array add the following:

```js
const [contacts, setContacts] = useState([]);
```

Here, we’re doing here is creating a state object, and initialising it to an empty array. When we make the API call, we’ll update the state to contain a list of contacts. Since we named this state object **contacts**, our rendering logic within the JSX will look for this array instead (as opposed to the old **contacts** array we just deleted).

Next, let’s grab the data from the API.  We’ll use the standard **Fetch API**. For now, we’ll log the data to the console. Add the following below the state object we just created:

```js
fetch("https://randomuser.me/api/?results=3")
  .then(response => response.json())
  .then(data => {
    console.log(data);
  });
```

All we’re doing here is:

- Making a GET request to the **randomuser** API, asking for **three** results
- Convert the response into **JSON**
- Logging the **JSON** to the console.

If you run this in the browser, you’ll notice the **ContactCard** components no longer render - thats fine, we haven’t saved any new data to state yet, and our state variable is currently empty. If you look at the console (in your browser dev tools) you’ll notice the response object is logged. Which will look something like this:

![](https://jschris.com/static/2327d21e950dd2b2d3a0c7c51fac655d/587b0/response_object.png)

You’ll see we have a **results** array, which has 3 objects. Each of these objects contain the details of a user (or a “Contact” in our case). This is similar to the **contacts** array we manually created ourselves in the previous section - just an array full of objects. 

Let’s update our **App** components JSX to pick data from this object. Update the JSX like so:

```jsx
return (
  <>
    {contacts.map(contact => (
      <ContactCard
        avatar={contact.picture.large}
        name={contact.name.first + " " + contact.name.last}
        email={contact.email}
        age={contact.dob.age}
      />
    ))}
  </>
);
```

This works similar to what we had before:

- We are looping through the **contacts** variable (which, at the moment is an empty array)
- When we eventually save the response to state (the next step) we look through each object in the array, for the appropriate things we need: in this case **picture, name, email, and dob** objects.  

Next we want to store the **results** array in state, so our JSX can loop over it (using the **map()** function we seen previously) and render some lovely **ContactCards**. Within our **fetch** function, add the call to **setContacts(data.results)** like so:

```jsx
fetch("https://randomuser.me/api/?results=3")
  .then(response => response.json())
  .then(data => {
    console.log(data);
    setContacts(data.results);
  });
```

Our **App** component now looks like this:

```jsx
//App.js
const App = () => {
  const [contacts, setContacts] = useState([]);

fetch("https://randomuser.me/api/?results=3")
  .then(response => response.json())
  .then(data => {
    console.log(data);
    setContacts(data.results);
  });

  return (
    <>
      {contacts.map(contact => (
        <ContactCard
          avatar={contact.picture.large}
          name={contact.name.first + " " + contact.name.last}
          email={contact.email}
          age={contact.dob.age}
        />
      ))}
    </>
  );
};
```

 If you save this, and run it in the browser, you’ll see something like this:

![](https://jschris.com/4bd02a07f80d45810780b5db77db42b3/multiple-calls-to-api.gif)

You might be thinking, “WTF is going on? Everything is broken!” 

Don’t panic just yet. (If you’re on a slower machine or just getting a bit freaked out, you can comment out the **setContacts(data.results)** line within the **fetch** function for now).

What’s happening here is that we’re stuck in a bit of a loop:

1) We make a call to **fetch** and get some data back 
2) We then **save this data to state**
3) Remember, React does a **re-render when the state changes**
4) When the component re-renders, the **fetch** api call happens again, and sets the state
5) Since the state updated, the component re-renders again
6) After the component re-renders, fetch is called again…
7) You get the idea

So how do we stop this? We have to delete everything and start again. Nah just kidding, don’t run away yet. We can fix this with another built in React Hook - **useEffect**.

## Introducing useEffect

The **useEffect** hook is a special hook that runs a function. By default, the useEffect hook runs on every re-render. However, we can configure it to only run **under certain condition**, e.g. when a **component mounts**, or **if a variable changes**. The useEffect hook looks like this:

```js
useEffect(() => {
	// code to run 
});
```

This will run every time. If we want to specify **“only run once”** we pass in an **empty array** as a second argument like so. 

```js
useEffect(() => {
	// code to run 
},[]); //<-- notice the empty array
```

This is called a **dependency array**. When the dependency array is empty, this means the useEffect function will only run when the component loads for the first time. For additional re-renders, the useEffect function is skipped. 

This is a perfect place to put our API call, as we only want to get the data once, when the component loads. Go ahead and place a **useEffect()**function into our **App** component, and move the **fetch** API call into the useEffect function. Our  **App** component now looks like this:

```jsx
//App.js
const App = () => {
  const [contacts, setContacts] = useState([]);

  useEffect(() => {
    fetch("https://randomuser.me/api/?results=3")
      .then(response => response.json())
      .then(data => {
        setContacts(data.results);
      });
  }, []);

  return (
    <>
      {contacts.map(contact => (
        <ContactCard
          avatar={contact.picture.large}
          name={contact.name.first + " " + contact.name.last}
          email={contact.email}
          age={contact.dob.age}
        />
      ))}
    </>
  );
};
```

Now, if you run the code in your browser, you should see 3 contact cards appear! Refresh the page to see another randomised list of contacts:

![](https://jschris.com/static/093da2b0c6947b52d83b42183d172718/6569d/contacts-list-intro.png)

## Conclusion

Congrats! You just completed your first real-world app and laid the foundation to move on to more advanced topics. 

[Make sure to subscribe here to stay up to date with my latest React content, course discounts and early access, as well as some free stuff!](https://subscribe.jschris.com)


[Also don't forget to check out my new blog - www.jschris.com - where I'll be posting JavaScript/React related articles and tutorials!](https://www.jschris.com)



