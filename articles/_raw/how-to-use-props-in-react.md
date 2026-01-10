---
title: How to Use Props in React
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2021-11-15T23:48:49.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-props-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/g127.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'In this tutorial, we''ll talk about an important concept in React – props.
  I''ll show you how to use them to keep the flow of data in your app dynamic.

  Prerequisites

  In other to follow along with this tutorial, you will need:


  A React app.


  Additionall...'
---

In this tutorial, we'll talk about an important concept in React – props. I'll show you how to use them to keep the flow of data in your app dynamic.

### Prerequisites

In other to follow along with this tutorial, you will need:

* A React app.

Additionally, I assume that you already understand:

* What components are in React and how to use them.
* How to use ES6 features in React (Don't know how? Read [this](https://www.freecodecamp.org/news/how-to-use-es6-javascript-features-in-react/) article).
* The basics of state management in React (Don't know how it works? Read [this](https://www.freecodecamp.org/news/introduction-to-react-hooks/) article).

## What are props in React?

We use props in React to pass data from one component to another (from a parent component to a child component(s)). Props is just a shorter way of saying properties. They are useful when you want the flow of data in your app to be dynamic. 

This is what my `App.js` component looks like:

```javascript
function App() {
  return (
    <div className="App">
      
    </div>
  )
}

export default App

```

Now let's create another component named `Tool.js`. This file will show information about a product designer's favorite tool. Without props, the code will look something like this:

```javascript
function Tool() {
    return (
      <div>
        <h1>My name is Ihechikara.</h1>
        <p>My favorite design tool is Figma.</p>
      </div>
    );
}

export default Tool
```

We will now import this component into the `App` component. That is:

```javascript
import Tool from "./Tool"

function App() {
  return (
    <div className="App">
      <Tool/>
    </div>
  )
}

export default App
```

Let's assume that the `Tool` component will be reusable across different components to describe different designers and their favourite tools. 

While React makes it easy for us to import a component's logic without rewriting the code, this particular component already has its data hard coded. This means that we have to either rewrite that logic for every other component, or – you guessed right – use props to alter the data for different components.

If you don't yet understand how this works, props allow us reuse a component's logic dynamically. This means that the data in the component will not be static. So for every other component using that logic, its data can be modified to fit the requirements.

## How to use props in React

In this section, you will learn two ways to use props: one without destructuring and the other with destructuring.

### How to use props without destructuring

To use props, you have to pass in `props` as an argument in your function. This is similar to passing arguments into your regular JavaScript functions. Here's an example:

```javascript
function Tool(props) {
  const name = props.name;
  const tool = props.tool;
    return (
      <div>
        <h1>My name is {name}.</h1>
        <p>My favorite design tool is {tool}.</p>
      </div>
    );
}

export default Tool
```

Now I will explain everything that happened above step by step. 

#### Step 1 - Pass in props as an argument

We did that in the first line of the code above: `function Tool(props){}`. This automatically allows you to use props in your React app's component.

#### Step 2 - Declare props variable(s)

```javascript
const name = props.name;
const tool = props.tool;
```

As you can see above, these variables are different from regular variables because the data in them has to do with props. 

If you do not want to create variables for your props, you can go ahead and pass them directly into your template like this: `<h1> My name is {props.name} </h1>`

#### Step 3 - Use variable(s) in JSX template

Now that you have declared your variables, you can go on and place them where you want them to be in your code.

```javascript
return (
      <div>
        <h1>My name is {name}.</h1>
        <p>My favorite design tool is {tool}.</p>
      </div>
    );
```

#### Step 4 - Pass data to props in the `App` component

We are done creating our props, so the next step is to pass data to them. We have already imported the `Tool` component and this is displayed in the browser at the moment:

```
My name is .
My favorite design tool is .
```

You can create default data for your props so they don't appear empty on declaration. You will see how to do that in the last section.

Recall that this is the current state of the `App` component:

```javascript
import Tool from "./Tool"

function App() {
  return (
    <div className="App">
      <Tool/>
    </div>
  )
}

export default App
```

You must be wondering where the data will be passed to exactly. To do this, you pass in the data like attributes. It looks like this:

```javascript
import Tool from "./Tool"

function App() {
  return (
    <div className="App">
      <Tool name="Ihechikara" tool="Figma"/>
    </div>
  )
}

export default App

```

Notice the change? Here: from `<Tool/>` to `<Tool name="Ihechikara" tool="Figma"/>`. This will not throw an error your way because those attributes are attached to the props created in the `Tool` component.

You should have this displayed in your browser:

```
My name is Ihechikara.
My favorite design tool is Figma.
```

Note that the variable name is not the prop itself. If I had created a variable this way – `const myPropName = _props_.name` – and used the variable in my template like this: `<h1>My name is {myPropName}.</h1>`, then the code would still work perfectly if I were to do this: `<Tool name="Ihechikara" tool="Figma"/>`. The `name` attribute is derived from `props.name` and not from the variable name containing the prop.

Now you can create data dynamically for any component using the logic defined in the `Tool` component. You can declare as many props as you want.

Next, you will learn how to use props with destructuring. 

### How to use props with destructuring

The code for this section is entirely the same as the last section except for the method for declaring the props. If you do not know how to use destructuring in JavaScript then check out [this](https://www.freecodecamp.org/news/how-to-use-es6-javascript-features-in-react/) article

In the previous section, we declared our props this way:

```javascript
const name = props.name;
const tool = props.tool;
```

But we don't need to do this with destructuring. You simply do this:

```javascript
function Tool({name, tool}) {
  
    return (
      <div>
        <h1>My name is {name}.</h1>
        <p>My favorite design tool is {tool}.</p>
      </div>
    );
}

export default Tool
```

The difference is in the first line of code. Instead of passing `props` as an argument, we destructured and passed in the variables as the function's argument.

Everything else remains the same.

Note that you are not limited to just single variables as your props data – you can equally pass in functions and even data from objects.

### How to set default values for props

If you do not want your props data to be empty when you create them, you can pass in a default value. Here's how to do that:

```javascript
function Tool({name, tool}) {

    return (
      <div>
        <h1>My name is {name}.</h1>
        <p>My favorite design tool is {tool}.</p>
      </div>
    );

  }
  
  Tool.defaultProps = {
    name: "Designer",
    tool: "Adobe XD"
  }
export default Tool

```

Just at the end of the code before the component was exported, we declared default values for our props. To do that, we started with the component's name and a dot/period connecting it with `defaultProps` which is built in when you create a React app. 

Now, wherever we import this component, those values will be the initial values instead of being blank. When you pass in data to the child component like we did in previous sections, it overrides the default values.

## Conclusion

This article covered everything you need to get started using props and passing data dynamically across your components. 

The best way to understand these concepts is to practice and build awesome stuff with them, so make sure you don't just read through – go build, too.

You can find me on Twitter [@ihechikara2](https://twitter.com/Ihechikara2). Happy coding!

