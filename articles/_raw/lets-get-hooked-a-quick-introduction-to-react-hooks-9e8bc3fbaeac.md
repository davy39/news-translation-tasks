---
title: 'Let’s get hooked: a quick introduction to React Hooks'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-01T18:53:07.000Z'
originalURL: https://freecodecamp.org/news/lets-get-hooked-a-quick-introduction-to-react-hooks-9e8bc3fbaeac
coverImage: https://cdn-media-1.freecodecamp.org/images/1*hwW04YcPNKdDmkmDaoaXDw.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: hooks
  slug: hooks
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Lekha Surasani

  Getting Started with React Hooks

  The React team introduced React Hooks to the world at React Conf in late October
  2018. In early February 2019, they finally came in React v16.8.0. While I, like
  most others probably, won’t be able to...'
---

By Lekha Surasani

#### Getting Started with React Hooks

The React team introduced React Hooks to the world at React Conf in late October 2018. In early February 2019, they finally came in React v16.8.0. While I, like most others probably, won’t be able to use them in production for a while (until we decide to update React), I have been experimenting with them on the side.

I was actually so excited about it, I will be giving an intro talk about it at a local meetup. Additionally, I’ll be giving a talk about Hooks (and other upcoming React features) at WeRockITConf in Huntsville in May! (EDIT: I have now given these talks and you can find the presentations and the associated resources on [my website](https://lekhasurasani.com/speaking)!) But for now, here’s how to get started with React Hooks!

# What are Hooks anyway?

React Hooks let you use state, and other React features without having to define a JavaScript class. It’s like being able to take advantage of the cleanliness and simplicity of a Pure Component _and_ state and component lifecycle methods. This is because Hooks are just regular JavaScript functions! This lends itself to cleaner and less clunky code. A side by side comparison of what the code looks like with and without Hooks for a simple counting component:

```js
import './App.css';
import React, { useState } from 'react';

const HooksExample = () => {
    const [counter, setCount] = useState(0);

    return (
        <div className="App">
            <header className="App-header">
                The button is pressed: { counter } times.
                <button
                    onClick={() => setCount(counter + 1)}
                    style={{ padding: '1em 2em', margin: 10 }}
                >
                    Click me!
                </button>
            </header>
        </div>
    )
}

export default HooksExample;
```

NoHooks.js:

```js
import './App.css';
import React, { Component } from 'react';

export class NoHooks extends Component {
    constructor(props) {
        super(props;
        this.state = {
            counter: 0
        }
    }
    
    render() {
        const { counter } = this.state;
        return (
            <div className="App">
                <header className="App-header">
                    The button is pressed: { counter } times.
                    <button
                        onClick={() => this.setState({ counter: counter + 1 }) }
                        style={{ padding: '1em 2em', margin: 10 }}
                    >
                        Click me!
                    </button>
                </header>
            </div>
        )	
    }
}

export default NoHooks;
```

Not only is the code a lot smaller — the saved space certainly adds up for larger components — it’s also a lot more _readable_, which is a huge advantage of Hooks. For beginners who are just getting started with React, it’s easier for them to read the first block of code and easily see exactly what’s happening. With the second block, we have some extraneous elements, and it’s enough to make you stop and wonder what it’s for.

Another great thing about hooks is that you can create your own! This means that a lot of the stateful logic we used to have to re-write from component to component, we can now abstract out to a custom hook — and _reuse it_.

The one example where this is particularly life-changing (for me) that comes to mind is use with forms. With all of the stateful logic of forms, it’s hard to reduce the size of the component. But now, with hooks, complex forms can become much simpler without the use of other form libraries.

But before we get to that, let’s take a look at the hook at hand — useState.

# useState

useState, as the name describes, is a hook that allows you to use state in your function. We define it as follows:

const [ someState, updateState ] = useState(initialState)

Let’s break this down:

* **someState:** lets you access the current state variable, _someState_
* **updateState:** function that allows you to update the state — whatever you pass into it becomes the new _someState_
* **initialState:** what you want _someState_ to be upon initial render

(If you’re unfamiliar with array destructuring syntax, stop here and read [this](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment#Basic_variable_assignment).)

Now that we understand the basic format of useState and how to call and use it, let’s go back to the example from before.

In this example**, counter** is the state variable, **setCount** is the updater function, and **0** is the initial state. We use **setCount(counter + 1)** to increment the count when the button is pressed, making **counter + 1** the new value of **counter**. Alternatively, if we wanted to use the previous state to update the current state, we could pass in the old state to setCount:

`setCount(prevCount => prevCount + 1)`

This is a simple example that isn’t reflective of what we’d normally use in an actual application. But let’s take a look at something we’re more likely to use — a simple sign-in form for email and password:

```js
import './App.css';
import React, { useState } from 'react';

const LoginForm = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    return (
        const { handleSubmit } = this.props;
        <div className="App">
            <header className="App-header">
                <form onSubmit={handleSubmit}>
                    <input value={ email } onChange={(e) => setEmail(e.target.value) } />
                    <input value={ password } onChange={(e) => setPassword(e.target.value) } />
                    <button type="submit">Submit</button>
                </form>
            </header>
        </div>
    )
}

export default LoginForm;
```

We have two separate state fields and state updaters. This allows us to create really simple forms without creating a whole JavaScript class.

If we wanted to simplify this further, we could create an object as the state. However, useState replaces the whole state instead of updating the object (as setState would), so we can replicate the usual behavior of setState as shown below:

```js
import './App.css';
import React, { useState } from 'react';

const LoginForm = () => {
    const [login, setLogin] = useState({ email: '', password: '' });

    return (
        const { handleSubmit } = this.props;
        <div className="App">
            <header className="App-header">
                <form onSubmit={handleSubmit}>
                    <input value={ login.email } onChange={(e) => setLogin(prevState => { ...prevState, email: e.target.value }) } />
                    <input value={ login.password } onChange={(e) => setLogin(prevState => { ...prevState, password: e.target.value }) } />
                    <button type="submit">Submit</button>
                </form>
            </header>
        </div>
    )
}

export default LoginForm;
```

If you have state objects more complex than this, you would either want to break them out into separate states as in the first Login example, or use useReducer (we’ll get to that soon!).

So we’ve got state in hooks. What about component lifecycle methods?

# useEffect

useEffect is another hook that handles componentDidUpdate, componentDidMount, and componentWillUnmount all in one call. If you need to fetch data, for example, you could useEffect to do so, as seen below.

```js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

const HooksExample = () => {
    const [data, setData] = useState();

    useEffect(() => {
        const fetchGithubData = async (name) => {
            const result = await axios(`https://api.github.com/users/${name}/events`)
            setData(result.data)
        }
        fetchGithubData('lsurasani')
    }, [data])

    

    return (
        <div className="App">
            <header className="App-header">
                {data && (
                    data.map(item => <p>{item.repo.name}</p>)
                )}
            </header>
        </div>
    )
}

export default HooksExample;
```

Taking a look at useEffect we see:

* First argument: A function. Inside of it, we fetch our data using an async function and then set **data** when we get results.
* Second argument: An array containing **data**. This defines when the component updates. As I mentioned before, useEffect runs when componentDidMount, componentWillUnmount, _and_componentDidUpdate would normally run. Inside the first argument, we’ve set some state, which would traditionally cause componentDidUpdate to run. As a result, useEffect would run again if we did not have this array. Now, useEffect will run on componentDidMount, componentWillUnmount, and if **data** was updated, componentDidUpdate. This argument can be empty— you can choose to pass in an empty array. In this case, only componentDidMount and componentWillUnmount will ever fire. But, you do have to specify this argument if you set some state inside of it.

# useReducer

For those of you who use Redux, useReducer will probably be familiar. useReducer takes in two arguments — a **reducer** and an **initial state**. A reducer is a function that you can define that takes in the current state and an “action”. The action has a type, and the reducer uses a switch statement to determine which block to execute based on the type. When it finds the correct block, it returns the state but with the modifications you define depending on the type. We can pass this reducer into useReducer, and then use this hook like this:

`const [ state, dispatch ] = useReducer(reducer, initialState)`

You use dispatch to say what action types you want to execute, like this:

`dispatch({ type: name})`

useReducer is normally used when you have to manage complex states — such as the signup form below.

```js
import React, { useReducer } from 'react';

const reducer = (state, action) => {
    switch (action.type) {
        case 'firstName': {
            return { ...state, firstName: action.value };
            }
        case 'lastName': {
            return { ...state, lastName: action.value };
            }
        case 'email': {
            return { ...state, email: action.value };
            }
        case 'password': {
            return { ...state, password: action.value };
            }
        case 'confirmPassword': {
            return { ...state, confirmPassword: action.value };
            }
        default: {
            return state;
        }
    }
};

function SignupForm() {
    const initialState = {
        firstName: '',
        lastName: '',
        email: '',
        password: '',
        confirmPassword: '',
    }
    const [formElements, dispatch] = useReducer(reducer, initialState);

    return (
        <div className="App">
            <header className="App-header">
                <div>
                    <input placeholder="First Name" value={ formElements.firstName} onChange={(e) => dispatch({ type: firstName, value: e.target.value }) } />
                    <input placeholder="Last Name" value={ formElements.lastName} onChange={(e) => dispatch({ type: lastName, value: e.target.value }) } />
                    <input placeholder="Email" value={ formElements.email} onChange={(e) => dispatch({ type: email, value: e.target.value }) } />
                    <input placeholder="Password" value={ formElements.password} onChange={(e) => dispatch({ type: password, value: e.target.value }) } />
                    <input placeholder="Confirm Password" value={ formElements.confirmPassword} onChange={(e) => dispatch({ type: confirmPassword, value: e.target.value }) } />
                </div>
            </header>
        </div>
    );
}

export default SignupForm;

```

This hook has a lot of additional applications, including allowing us to specify a few reducers throughout our application and then reusing them for each of our components, changing based on what happens in those components. On a high level, this is similar to Redux’s functionality — so we may be able to avoid using Redux for relatively simpler applications.

# Custom Hooks

So we’ve covered 3 basic hooks — let’s look at how to make our own. Remember the example I mentioned earlier with the login form? Here it is again as a reminder:

```js
import './App.css';
import React, { useState } from 'react';

const LoginForm = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    return (
        const { handleSubmit } = this.props;
        <div className="App">
            <header className="App-header">
                <form onSubmit={handleSubmit}>
                    <input value={ email } onChange={(e) => setEmail(e.target.value) } />
                    <input value={ password } onChange={(e) => setPassword(e.target.value) } />
                    <button type="submit">Submit</button>
                </form>
            </header>
        </div>
    )
}

export default LoginForm;
```

We useState for both and define a state variable and an updater function for both of the fields. What if we could simplify this further? Here’s a custom hook for handling any kind of input value changes (note: the convention for naming a custom hooks is: use<function description>).

```js
import { useState } from 'react';

export const useInputValue = (initial) => {
    const [value, setValue] = useState(initial)
    return { value, onChange: e => setValue(e.target.value) }
}
```

We use useState to handle the changes as we did in the previous example, but this time we return the value and an onChange function to update that value. So, the login form can now look like this:

```js
import React from 'react';
import { useInputValue } from './Custom'

const Form = () => {
    const email = useInputValue('')
    const password = useInputValue('')

    return (
        <div className="App">
            <header className="App-header">
                <div>
                    <input type="text" placeholder="Email" {...email} />
                </div>
                <div>
                    <input type="password" placeholder="Password" {...password} />
                </div>
            </header>
        </div>
    );
}

export default Form;
```

We initialize useInputValue with an empty string for both of our fields, and set the result to the name of the field. We can put this back in the input element so the input element renders the value and onChange functions dynamically.

Now, we’ve made this form even simpler — and our custom hook can be reused wherever we need a form input element!

I think that this is one of the most useful things about hooks — the ability to make your own and allow for this previously stateful logic that was locked inside each component to be taken out and reused, allowing for each component to become simpler.

So we’ve gone over: useState, useEffect, useReducer, and finally, custom hooks. There’s a few basic things that we haven’t gone over just yet — namely, the two general rules to follow with Hooks:

1. **Only call Hooks at the _top level_** _—_ Not in loops, nested functions, conditions, etc. This ensures that hooks are always called in the same order after each render. This is important because React relies on the order that Hooks are called to determine which state corresponds to a useState call (if you are using multiple). If one of your hooks is hidden in a loop, nested function, or a conditional, the order can change from render to render, messing up which state corresponds to which useState.
2. **Only call Hooks from React functions or custom hooks** — In other words, don’t call Hooks from JavaScript functions.

Hopefully this clears up how and when to use hooks for you! Some additional resources you can take a look at:

* [The React docs](https://reactjs.org/docs/hooks-intro.html)
* [Collection of Hooks resources](https://github.com/rehooks/awesome-react-hooks)

If you have any questions/comments, please feel free to ask below!

