---
title: 'How to Get Started With React Hooks: Controlled Forms'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-04T17:23:54.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-started-with-react-hooks-controlled-forms-826c99943b92
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0MgGEfZfLO91g1Oa2h3ebQ@2x.png
tags:
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Kevin Okeh

  React Hooks are a shiny new proposal that will allow you to write 90% cleaner React.
  According to Dan Abramov, Hooks are the future of React.

  That sounds good and all but what are Hooks and how will they help me write better
  code? Glad ...'
---

By Kevin Okeh

React Hooks are a shiny new [proposal](https://www.youtube.com/watch?v=dpw9EHDh2bM&t=54s) that will allow you to write 90% cleaner React. According to [Dan Abramov](https://overreacted.io/), [Hooks](https://reactjs.org/docs/hooks-intro.html) are the future of React.

That sounds good and all but what are Hooks and how will they help me write better code? Glad you asked.

Hooks allow you to access `state` and Lifecycle methods in a functional component. If the previous sentence sounds strange to you, then you should refresh your memory of React [here](https://medium.freecodecamp.org/the-react-handbook-b71c27b0a795#b70b).

The React team says it will help you write clean code without the baggage of Stateful Components. After implementing a barebones form using Hooks, I agree with them.

Let’s go ahead to code a simple form first in a Stateful Component. We’ll rewrite the same form using Hooks and you can decide which one you like better.

### SETUP

Head over to [codesandbox.io](https://codesandbox.io/), create an account, sign in, and create a new Sandbox. Select React when creating the Sandbox.

![Image](https://cdn-media-1.freecodecamp.org/images/1*iR8iWv8UppVwLdRFyy5Mtw.png)
_select React from the list of templates_

Now with the Sandbox open, we’ll have to make sure that we use a version of React that has support for Hooks. This is because Hooks are only accessible in Alpha versions for now.

**UPDATE: Hooks are now in the public, [stable version of React v16.8](https://t.co/didbtI06Ie).**

Look at the File Editor on the left side of the Sandbox and:

* Click on ‘Dependencies’
* Remove both ‘react’ and ‘react-dom’
* Now click on ‘Add Dependency’
* Type ‘react’ in the input box and click on the dropdown by the right of the first result.
* Select version 16.8.0-alpha.1.
* Now click on the description to install it.

![Image](https://cdn-media-1.freecodecamp.org/images/1*HrTkGB8k6v-9Yf0NLKxDAw.png)
_make sure to select the latest alpha version_

Repeat the same steps for ‘react-dom’ and we should be good to go.

### CODE

Now that we have the setup out of the way, it’s time to write some code. Hop over to the Sandbox you created, create a new file called Form.jsx and paste the following code in:

```
import React, { Component } from "react";
```

```
class Form extends Component {  constructor(props) {    super(props);
```

```
this.state = {      firstName: "",      lastName: "",      email: "",      password: "",    };
```

```
this.handleInputChange = this.handleInputChange.bind(this);  }
```

```
handleInputChange(event) {    this.setState({      [event.target.name]: event.target.value    });  }
```

```
render() {    const { firstName, lastName, email, password } = this.state;
```

```
return (      <form>        <input          value={firstName}          onChange={this.handleInputChange}          placeholder="First name"          type="text"          name="firstName"          required        />        <input          value={lastName}          onChange={this.handleInputChange}          placeholder="Last name"          type="text"          name="lastName"          required        />        <input          value={email}          onChange={this.handleInputChange}          placeholder="Email address"          type="email"          name="email"          required        />        <input          value={password}          onChange={this.handleInputChange}          placeholder="Password"          type="password"          name="password"          required        />
```

```
<button type="submit">Submit</button>      </form>    );  }}
```

```
export default Form;
```

Now open index.js and replace the contents with the following code:

```
import React from "react";import ReactDOM from "react-dom";
```

```
import Form from "./Form.jsx";import "./styles.css";
```

```
function App() {  return (    <div className="App">      <h1>A Simple Form in React</h1>      <Form />    </div>  ); }
```

```
const rootElement = document.getElementById("root");
```

```
ReactDOM.render(<App />, rootElement);
```

Test the form to see that everything works fine. Now that was the ‘old-school’ way of implementing a controlled form in React.

Notice the amount of boilerplate we needed to set up the state and the method for updating it on each input change.

Let’s code the same form using React Hooks (finally!) but first, delete all the code from Form.jsx and let’s start afresh.

Start by adding the following line to the top of the file:

```
import React, { useState } from 'react';
```

So there’s an unfamiliar method imported here called `useState`. What is it and how do we use it?

Well, `useState` is the React Hook that will allow us to access and manipulate `state` in our component. This means we won’t have to `extend Component` as our previous code does.

It’s one of several new Hooks coming to the React API to help us write cleaner code. Now let’s use it.

```
import React, { useState } from "react";import "./styles.css";
```

```
function Form() {  const [firstName, setFirstName] = useState("");  const [lastName, setLastName] = useState("");  const [email, setEmail] = useState("");  const [password, setPassword] = useState("");
```

```
return (    <form>      <input        value={firstName}        onChange={e => setFirstName(e.target.value)}        placeholder="First name"        type="text"        name="firstName"        required      />      <input        value={lastName}        onChange={e => setLastName(e.target.value)}        placeholder="Last name"        type="text"        name="lastName"        required      />      <input        value={email}        onChange={e => setEmail(e.target.value)}        placeholder="Email address"        type="email"        name="email"        required      />      <input        value={password}        onChange={e => setPassword(e.target.value)}        placeholder="Password"        type="password"        name="password"        required      />
```

```
<button type="submit">Submit</button>    </form>  );}
```

```
export default Form;
```

We’ve created our functional component but there is some unfamiliar code that I will explain. Specifically, the four declarations at the top of our component.

While that part of the code looks strange at first, it is simple to understand. We are no longer declaring a single object called `state` that holds our component’s state. Instead, we are now splitting up `state` into multiple declarations.

Say we wanted to declare a state variable called `firstName` the familiar `extends React.Component` way, we’d usually do it in the constructor and then access it by writing `this.state.firstName`.

But with `useState`, we initialize two variables called `firstName` and `setFirstName`. We then set their values to whatever `useState()` returns.

Why do we have to declare `setFirstName` too though?

Well, since this is a functional component, we don’t have `setState` to help us modify the value of the state variable. What we do have is `setFirstName` whose sole purpose is to update `firstName` every time we call it.

So when you see:

```
const [firstName, setFirstName] = useState("")
```

We’re basically declaring a state variable and a function to allow us to modify the state variable later. The empty string in the `useState` call is the initial value of `firstName` and can be set to any required value. We’ll set it to an empty string for now.

Note that you can name the `setFirstName` function whatever you want. It is a convention, however, to append ‘set’ before the name of the state variable we’re modifying.

We now know how to create a state variable in a functional component and how to update it. Let’s continue by explaining the rest of the code.

In our first input tag, we set it’s value to the state variable we declared at the top of our component. As for the `onChange` handler, we set it to an [arrow function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions) that calls the function which updates our state variable for us.

Where we had a method in our previous class component called `handleInputChange`, we now have an anonymous function that updates our state for us.

Check that everything works as it should by trying to input text into your form. If everything works, congratulations, you just used a React Hook. If not, then go through this tutorial again and ensure you don’t skip any instructions.

Add styling as you see fit and enjoy.

### REFLECTIONS

**UPDATE:** Some of us may be alarmed at the thought of using inline functions in the onClick handler. I tweeted Dan Abramov about that and he replied with [this part of the Hooks documentation](https://reactjs.org/docs/hooks-faq.html#are-hooks-slow-because-of-creating-functions-in-render) that explains why using inline functions with Hooks isn’t a bad thing.

Going through our new code and comparing it to the old one, it’s obvious how React Hooks can help us to write better code.

Comparing the class component and the functional component side by side, it is clear that the functional component is easier to reason about, uses less code, and generally looks cleaner.

If you like React Hooks, you can learn more by exploring the [official docs](https://reactjs.org/docs/hooks-intro.html) and trying to reimplement some of your projects using them.

That said, I’d like to hear your thoughts. Do you think Hooks are the future of React or do you feel that they’re just unnecessary gimmicks? Leave a comment below.

This post appeared first on [The Andela Way](https://medium.com/the-andela-way/how-to-get-started-with-react-hooks-controlled-forms-9b47e9fb8c8d).

