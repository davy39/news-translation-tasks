---
title: What Every React Developer Should Know About State
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2021-04-16T17:31:00.000Z'
originalURL: https://freecodecamp.org/news/what-every-react-developer-should-know-about-state
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/5-things-every-react-developer-should-know-about-state.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
- name: 'State Management '
  slug: state-management
seo_title: null
seo_desc: "One of the most important concepts for every React developer to understand\
  \ is state – what it is, how to properly use it, and how to avoid common pitfalls\
  \ as you build your applications. \nLet's cover five of the most essential parts\
  \ of state that you..."
---

One of the most important concepts for every React developer to understand is state – what it is, how to properly use it, and how to avoid common pitfalls as you build your applications. 

Let's cover five of the most essential parts of state that you need to know. Each of these parts build upon each other to aid your overall understanding of a somewhat complex topic.

To make these abstract concepts as clear as possible, I've included many practical examples that you can run in Code Sandbox or any React project you have set up.

## 1. State updates with useState are not merged

One challenge many React developers face when moving from class-based components to function components with React hooks is that state updates using objects are no longer automatically merged.

A great advantage of the useState hook is that we are able to call it as many times as we like to use as many state variables as we need. 

In this example, we have a basic form with an email and password input. We are managing the email and password state as individual state variables:

```js
import React from "react";

export default function App() {
  const [email, setEmail] = React.useState("");
  const [password, setPassword] = React.useState("");

  return (
    <form>
      <input
        name="email"
        type="email"
        placeholder="Email"
        onChange={(e) => setEmail(e.target.value)}
      />
      <input
        name="password"
        type="password"
        placeholder="Password"
        onChange={(e) => setPassword(e.target.value)}
      />
      <button type="submit">Submit</button>
    </form>
  );
}
```

Let's change our example to manage our form state within a single object. This allows us to call useState just once, where email and password are not managed by individual state variables but as properties of this one state variable called `state`. 

_How do we appropriately update state with the `setState` function when it is an object?_

If we were to use a generic event handler that is connected to the `onChange` prop of each of our form's inputs, it would look something like this:

```js
import React from "react";

export default function App() {
  const [state, setState] = React.useState({
    email: '',
    password: ''
  })

  function handleInputChange(e) {
    setState({
      [e.target.name]: e.target.value
    })
  }

  return (
    <form>
      <input
        name="email"
        type="email"
        onChange={handleInputChange}
      />
      <input
        name="password"
        type="password"
        onChange={handleInputChange}
      />
      <button type="submit">Submit</button>
    </form>
  );
}
```

We're now updating each input's value in state according to the name of the input our user is currently typing in.

This pattern is commonly used to update state in class-based components, but this does not work with the useState hook. State updates with useState's `setState` function are not automatically merged. 

_What does that mean?_ 

It means that whenever we set state as our user types in, the previous state is not included in the new state. If we were to log our newly updated state as we type into our form, we see the following:

![Image](https://www.freecodecamp.org/news/content/images/2021/04/5-things-every-react-developer-should-know-about-state-1.gif)

Since the previous state is not automatically merged into the new state object, we must manually merge our state object with its previous properties using the object spread operator:

```js
import React from "react";

export default function App() {
  const [state, setState] = React.useState({
    email: '',
    password: ''
  })

  function handleInputChange(e) {
    setState({
      // spread in previous state with object spread operator
      ...state,
      [e.target.name]: e.target.value
    })
  }

  return (
    <form>
      <input
        name="email"
        type="email"
        onChange={handleInputChange}
      />
      <input
        name="password"
        type="password"
        onChange={handleInputChange}
      />
      <button type="submit">Submit</button>
    </form>
  );
}
```

For the useState hook, we have the flexibility to manage multiple primitive values or use an object with multiple properties.

If you useState with an object, however, remember to spread in the previous state when performing any updates to make sure it is updated correctly.

## 2. State hooks trigger a re-render, useRef does not

React state has a very important relationship with rendering components.

Whenever we return JSX from a React component, when that component is used, it will be rendered and therefore displayed in our application. React takes care of this rendering process. 

If our component uses any state, we must understand that it needs to be rendered again – that is, re-rendered – in response to any state update. 

_Why do components need to be re-rendered upon state updates?_

Because if we did not re-render upon updating state, we would not be able to show new data. This is very simply expressed, whenever we are showing any state contained within a state variable within our JSX. 

If it did not re-render whenever we make changes to that variable, the updates would not be shown. 

This seems like a rather simple concept, but you need to understand that **whenever we update state,** **it not only causes a re-render in the component that directly manages the state – it also causes a re-render in all child components**. 

_Why does this matter?_ Because in some cases, we may not want a child component to re-render in response to a parent component re-rendering. 

_What is one such example?_ Let's say we have application where a user can type into an input whose value is managed through state. This app also has another component that displays a list of data. 

Whenever the user types into the input, our state is updated, and this causes a needless re-render in that other child component. 

The way that we can fix this is with the help of the `React.memo` function, which helps in preventing our component from being re-rendered when a parent component re-renders:

```js
export default function App() {
  const [skill, setSkill] = React.useState("");
  const [skills, setSkills] = React.useState(["HTML", "CSS", "JavaScript"]);

  function handleChangeInput(event) {
    setSkill(event.target.value);
  }

  function handleAddSkill() {
    setSkills(skills.concat(skill));
  }

  return (
    <>
      <input onChange={handleChangeInput} />
      <button onClick={handleAddSkill}>Add Skill</button>
      <SkillList skills={skills} />
    </>
  );
}

/* But the problem, if you run this code yourself, is that when we type into the input, because the parent component of SkillList (App) re-renders, due to the state being updated on every keystroke, the SkillList is rerendered constantly (as indicated by the console.log) */

/* However, once we wrap the SkillList component in React.memo (which is a higher-order function, meaning it accepts a function as an argument), it no longer re-renders unnecessarily when our parent component does. */
const SkillList = React.memo(({ skills }) => {
  console.log("rerendering");
  return (
    <ul>
      {skills.map((skill, i) => (
        <li key={i}>{skill}</li>
      ))}
    </ul>
  );
});
```

One other thing to note here is that there is technically a way to manage state without causing a re-render. We can do so with a hook that most people don't view as being a stateful React hook – `useRef`.

useRef can be used to store any value on its `.current` property. In other words, if we wanted to make a simple counter with useRef and update a count value that we stored on it, even if we update its value, it would not show the correct count after the initial render because doing so does not trigger a re-render:

```js
import React from "react";

export default function App() {
  const countRef = React.useRef(0);

  function handleAddOne() {
    countRef.current += 1;
  }

  return (
    <>
      <h1>Count: {countRef.current}</h1>

      {/* clicking this will not change display count */}
      <button onClick={handleAddOne}>+ 1</button>
    </>
  );
}
```

## 3. State updates should be immutable

A very important part of state in React is that it must be updated and managed in the correct way. 

When it comes to managing state with the useState hook, we must _only_ use the dedicated setter function as provided as the second element in the array we get back from useState to update it. If we don't do so and attempt to update it manually, with the help of just plain JavaScript for example, our application will not work like we expect. 

This point is very closely related to the previous point that we made: state, when updated _properly_, causes a re-render of our component. 

What do you think will happen if we attempt to update state in our own way instead of the "React" way? 

Again, React is what takes care of displaying and rendering our component properly when something changes. If we don't use React, then we can't expect our application to reflect any changes that we made to the state. 

In other words, **if we update state with plain JavaScript and not `setState`, it will not trigger a re-render and React will not display those (invalid) changes in state to our user.** 

This is a simple, but crucial lesson to remember. 

We must know how to update state using React and choose the appropriate state hook for our purposes. We might choose `useReducer`, `useState`, or a third-party state management library like Redux. 

Regardless of our choice in state management, we must update state in the appropriate manner and not attempt to update or mutate it directly. 

The other reason for this, aside from our React application not working properly, is that it violates a core principle of React. This is the concept of **immutability**. 

State updates should always be immutable. This means we shouldn't make our own changes or mutate the data stored in our state variables. Doing so makes our state unpredictable and can cause unintended problems in our application that are hard to debug.

```js
import React from 'react';

export default function App() {
  const [count, setCount] = React.useState(0);
  
  // Don't assign state to new (non-state) variables
  const newCount = count;
  // Don't directly mutate state
  const countPlusOne = count + 1;

  return (
    <>
      <h1>Count: {count}</h1>
    </>
  );
}
```

In addition to not mutating state variables directly, make sure to never assign state variables to other (non-state) variables.

## 4. State updates are asynchronous and scheduled

A crucial lesson to know about state updates is that they are not performed immediately. 

This can be seen if we take a look at the React documentation and see exactly what happens when we call the `setState` function. We use it to update the state variable associated with it, but we're also told:

> It accepts a new state value and enqueues a re-render of the component. 

_What does this word "enqueues" mean?_ 

In other words, it doesn't re-render the component immediately. It doesn't stop our code right at that line where we update state, but it takes place at some point in the future. This is for performance purposes and this gives us a better idea of what React is doing under the hood.

Based off of this information, we need to change our mental model when we attempt to update state: **the `setState` function does not immediately update state, it merely schedules a state update for some time in the future.** After which, React takes care of figuring out when that state update takes place. 

Therefore, it's not so easy just to be able to look at our code and see exactly when the state update occurred or will occur. 

This is important to compare to `useRef`, which we mentioned earlier as being able to hold on to the data within its current property. Any updates made with useRef are performed synchronously – we can look at our code and see exactly when a given update was performed in `useRef`, but not with useState.

## 5. Stale state can happen with closures

Finally, an important problem that can occur with React state is the problem of stale state. 

### What is stale state in React? 

Stale state is a problem that occurs whenever we're trying to update state, often within a closure.

> A closure is a type of function in JavaScript, where we're using a variable from an outer scope. 

This problem of stale state is based around the fact that closure might not capture the most up-to-date state variable value. That's what we mean by stale – we mean that it is old and not the current value that we want. 

This problem of stale state is closely related to the topic that we discussed that the previous topic of state updates being asynchronous. 

In many cases, what is a problem about state updates being asynchronous is that we don't always get the correct previous value of our state, especially if we're trying to update state based off of that previous value. 

We can express the problem of a stale closure within a simple counter application that updates the count after a second using the `setTimeout` function.

Because setTimeout creates a closure, we are accessing a stale value of our state variable, `count`, when we call `setCount`.

```js
import React from 'react';

export default function App() {
  const [count, setCount] = React.useState(0);

  function delayAddOne() {
    setTimeout(() => {
      setCount(count + 1);
    }, 1000);
  }

  return (
    <>
      <h1>Count: {count}</h1>
      <button onClick={delayAddOne}>+ 1</button>
    </>
  );
}
```

The problem is apparent when we run our application. Despite clicking the button multiple times, it is still only incremented by one every second:

![Image](https://www.freecodecamp.org/news/content/images/2021/04/5-thing-every-react-developer-should-know-about-state-2.gif)

We can fix this problem of our stale state within our closure by using a more reliable method of updating state. The state updates are still going to be scheduled, but it will make it possible to reliably get the previous value of state. 

We do this with the help of providing an inner function to the `setState` function. In the body of the function, we can get the previous state within the parameters of this function and then return what we want the next state to be. 

In our case, it will be the previous count value incremented by one:

```js
import React from 'react';

export default function App() {
  const [count, setCount] = React.useState(0);

  function delayAddOne() {
    setTimeout(() => {
      // stale state problem goes away using inner function
      setCount(prevCount => prevCount + 1);
    }, 1000);
  }

  return (
    <div>
      <h1>Count: {count}</h1>
      <button onClick={delayAddOne}>+ 1</button>
    </div>
  );
}
```

> Another interesting thing to note if you take a look at the React documentation is that if nothing is returned from this function, then no re-render is going to take place whatsoever. 

Once we provide this inner function to `setState` to reliably get the previous state and return the new state from our function, our stale state problem due to our closure goes away.

## Become a Professional React Developer

React is hard. You shouldn't have to figure it out yourself.

I've put everything I know about React into a single course, to help you reach your goals in record time:

[**Introducing: The React Bootcamp**](https://www.thereactbootcamp.com)

**It’s the one course I wish I had when I started learning React.**

Click below to try the React Bootcamp for yourself:

[![Click to join the React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Click to get started*

