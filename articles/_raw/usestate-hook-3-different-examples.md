---
title: How to Use the useState() Hook in React – Explained with Code Examples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-05-08T14:11:06.000Z'
originalURL: https://freecodecamp.org/news/usestate-hook-3-different-examples
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/usestate---hook-2.jpg
tags:
- name: JavaScript
  slug: javascript
- name: react hooks
  slug: react-hooks
- name: React
  slug: reactjs
seo_title: null
seo_desc: 'By Mwendwa Bundi Emma

  One of the most well-known React hooks is the useState() hook. It lets you add a
  state variable to your component. The useState() hook can conveniently hold strings,
  arrays, numbers, objects and much more.

  In this article, we ar...'
---

By Mwendwa Bundi Emma

One of the most well-known React hooks is the `useState()` hook. It lets you add a state variable to your component. The `useState()` hook can conveniently hold strings, arrays, numbers, objects and much more.

In this article, we are going to learn about the `useState()` hook and demonstrate its use with three different examples: a button with conditional rendering, form handling, and the famous counter.

## Prerequisites

* You'll need basic knowledge of HTML, CSS and JavaScript to understand the ideas behind what you are creating in this tutorial. 
* It's also helpful to have beginner's knowledge of React.
* Finally, you'll need an IDE, preferably [VS Code](https://code.visualstudio.com/).

Once you have your React application up and running, you are ready to use useState. To get started, you need to import `useState()` from React as shown below:

```js
import { UseState } from 'react';
```

## How Does `useState()` Work?

The `useState()` hook works by handling and managing state in your applications. 

The `useState()` hook takes the first (initial) value of the state variable as its argument. The second value then sets your state, which is why it's always initiated as `setState`. So how does this work?

```js
const [state, setState] = useState(initial values goes here)

const [calories, setCalories] = useState(initial value of calories)
```

In the case of the first render, it returns the initial state and updates to a different value during the re-render using the `set` function.

## Conditional Rendering with the `useState()` Hook

This example allows you to update state depending on two conditions: if the user is logged in or not. This also explains why the initial state is set to false, to mean the user is not logged in.

You are going to create a login button that uses the `useState()` hook to render two different outcomes. 

One is a sign-in button with a message asking the user to sign in. The other is a button that, once the user is signed in, gives them the choice to sign out.

```react
import React from 'react'

const Signin = () => {
  return (
    <div>
        <div>
            <button type="button">Sign Out</button>
            <p>Welcome back, good to see you in here<p>
        </div>
        <div>
            <button type="button">Sign In</button>
            <p>Please Sign in</p>
        </div>
    </div>
  )
}

export default Signin;
```

To implement the sign in and sign out functionalities, you will have to import `useState()`. Then you'll need to use conditional rendering to specify how the buttons will respond to a click.

```react
import React, { useState } from 'react'

const Signin = () => {
    const [signedin, setSignedin] = useState(false)

    const handleSignin = () => {
        setSignedin(true)
    }

    const handleSignout = () => {
        setSignedin(false)
    }
  return (
         <div>
           { signedin ? ( 
        <div>
            <button type="button" onClick={handleSignout}>Sign Out</button>
            <p>Welcome back, good to see you in here</p>
        </div>) :
        
        (<div>
            <button type="button"onClick={handleSignin}>Sign In</button>
            <p>Please Sign in</p>
        </div>)
           }
        </div>
  )
}

export default Signin;
```

What's happening in the code above?

First, you created a variable with the `useState()` hook that sets `signedin` to false. Why? Because on the first load, you don't want the user to be signed in. But once they click the sign in button, they can 'get in'.

Also, note that you imported the `useState()` hook at the top.

You then created variables that handle signing in, signing out, and setting the `set` function to `true` and `false`, respectively – that is `handleSignin` and `handleSignout`.

After that, you created an `onClick` handler that listens for a click on the button and triggers an action. This action is directed by the Conditional (ternary) Operator.

So how does the ternary operator work? Here's [what the MDN has to say](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_operator):

> "The **conditional (ternary) operator** is the only JavaScript operator that takes three operands: a condition followed by a question mark (`?`), then an expression to execute if the condition is [truthy](https://developer.mozilla.org/en-US/docs/Glossary/Truthy) followed by a colon (`:`), and finally the expression to execute if the condition is [falsy](https://developer.mozilla.org/en-US/docs/Glossary/Falsy).   
>   
> This operator is frequently used as an alternative to an [`if...else`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else) statement."

This means that if you click the sign in button, you are ushered in and receive the welcome message. Once you click the sign out button, you are prompted to sign in, with the 'please sign in' message.

## How to Use the `useState()` Hook in a React Counter App

This example will help show how you can use `useState()` to update your state through clicks.

The idea behind this simple counter is that your clicks are counted. So, if you click the button 12 times the counter updates to 12. Note that the button updates on every click/count.

```react
import React from 'react';


const Newcounter = () => {
    return (
        <div>
            <button type="button">You will see the count here</button>
        </div>
    )
}


export default Newcounter;

```

To make the counter functional, you need to use the hook as shown below (and once again, don't forget to import `useState()` before using it):

```react
const [count, setCount] = useState(0) 
```

You will then create another variable that increments the counts from 0 to 1, 2, 3....

```react
const incrementCount = () => { setCount (count + 1) }
```

You can now go forth and return the incremented count using the `onClick` handler as shown below:

```react
import React, { useState } from 'react';


const Newcounter = () => {
    const [count, setCount] = useState(0)

    const incrementCount = () => {
        setCount(count + 1)
    
    }
    return (
        <div>
            <button type="button" onClick={incrementCount}>You clicked  
            {count} times</button>
        </div>
    )
}


export default Newcounter;

```

## How to Use the `useState()` Hook in a Form in React

Forms utilise `useState()` by allowing the developer to set an empty state that uses the `set` function to handle what the user type in as their input. 

Here, you basically want to to collect the name and email of users through a form and then submit the info.

Below is a simple form to demonstrate how the `useState()` hook makes this possible.

Here's the form you'll be working with:

```react
import React from 'react'

const Theform
 = () => {
  return (
    <div>
        <form>
            <input type="text" placeholder="enter your name" required />
            <input type="email" placeholder="enter your email" required />
            <button type="submit">Submit</button>
        </form>

    </div>
  )
}

export default Theform;

```

You will need to import the hook to your file. After that, use the `useState` hook to set the name and email to null as you wait for the user to input their details.

Afterwards, you will create an arrow function with the `handleSubmit` that executes the `preventDefault()` method. `console.log` the name of the user and their email so you can get these details using the `onSubmit()` event handler.

Once that's done you can then use the `set` function for both the name and email to target a change in the input and get the value of the input which you initialised as `user` and `email` in your `useState()` hook.

Remember that the `useState` hook uses that `set` function for re-rendering. In this, you are re-rendering the new values the user has added in the form. That's why you are setting the value in your input as `value={user}`.

```react
import React, { useState }from 'react'

const Theform
 = () => {

  const [user, setUser] = useState('')
  const [email, setEmail] = useState('')

  const handleSubmit = (e) => {
    e.preventDefault()
    console.log(user, email)

  }
  return (
    <div>
        <form onSubmit={handleSubmit}>
            <input type="text" placeholder="enter your name"  onChange={(e) 
            => {setUser(e.target.value)}} value ={user} required />
                
            <input type="email" placeholder="enter your email" onChange={(e)  
            => {setEmail(e.target.value)}} value={email} required />
            <button type="submit">Submit</button>
            
        </form>

    </div>
  )
}

export default Theform;

```

## Conclusion

In this article you have learned about the `useState()` hook in React by considering three different examples. Remember, just like all other React Hooks, the useState() hook abides by the general rules of React hooks.




