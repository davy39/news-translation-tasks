---
title: Learn the basics of React Hooks in <10 minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-08T15:47:03.000Z'
originalURL: https://freecodecamp.org/news/learn-the-basics-of-react-hooks-in-10-minutes-b2898287fe5d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9FSQFJgVw_Ip1a3E4rmmow.png
tags:
- name: hooks
  slug: hooks
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Emmanuel Ohans

  Early this year, the React team released a new addition, hooks, to React in version
  16.8.0.

  If React were a big bowl of candies, then hooks are the latest additions, very chewy
  candies with great taste!

  So, what exactly do hooks mea...'
---

By Emmanuel Ohans

Early this year, the React team released a new addition, hooks, to React in version 16.8.0.

If React were a big bowl of candies, then hooks are the latest additions, very chewy candies with great taste!

So, what exactly do hooks mean? And why are they worth your time?

### Introduction

One of the main reasons hooks were added to React is to offer a more powerful and expressive way to write (and share) functionality between components.

> In the longer term, we expect Hooks to be the primary way people write React components — [React Team](https://reactjs.org/docs/hooks-faq.html#should-i-use-hooks-classes-or-a-mix-of-both)

If hooks are going to be that important, why not learn about them in a fun way!

### The Candy Bowl

Consider React to be a beautiful bowl of candy.

![Image](https://cdn-media-1.freecodecamp.org/images/1*u1Ubc4Zybc5AeACy38K08w.png)

The bowl of candy has been incredibly helpful to people around the world.

![Image](https://cdn-media-1.freecodecamp.org/images/1*T-X_uzowaEqEDhRYkUfPvA.png)

The people who made this bowl of candy realized that **some** of the candies in the bowl weren’t doing people much good.

A couple of the candies tasted great, yes! But they brought about some complexity when people ate them — think render props and higher order components?

![Image](https://cdn-media-1.freecodecamp.org/images/1*9FSQFJgVw_Ip1a3E4rmmow.png)

So, what did they do?

![Image](https://cdn-media-1.freecodecamp.org/images/1*jahda3D5PnCmuyZOlqj5eA.png)

They did the right thing — not throwing away all the previous candies, but making new sets of candies.

These candies were called **Hooks**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*WqUVZyfDQX6ihazFZ21w_g.png)

These candies exist for one purpose: **to make it easier for you to do the things you were already doing**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*EG-OKgzmiZewSjEJ9l0y7Q.png)

These candies aren’t super special. In fact, as you begin to eat them you’ll realize they taste familiar — they are just **Javascript functions**!

![Image](https://cdn-media-1.freecodecamp.org/images/1*HRw5WfHH02tvoM13sDSfVA.png)

As with all good candies, these **10** new candies all have their unique names. Though they are collectively called **hooks**.

Their names always begin with the three letter word, _use …_ e.g. `useState`, `useEffect` etc.

Just like chocolate, these 10 candies all share some of the same ingredients. Knowing how one tastes, helps you relate to the other.

Sounds fun? Now let’s have these candies.

### The State Hook

As stated earlier, hooks are functions. Officially, there are 10 of them. 10 new functions that exist to make writing and sharing functionalities in your components a lot more expressive.

The first hook we’ll take a look at is called, `useState`.

For a long time, you couldn’t use the local state in a functional component. Well, not until hooks.

With `useState`, your functional component can have (and update) local state.

How interesting.

Consider the following counter application:

![Image](https://cdn-media-1.freecodecamp.org/images/1*2909ks8DqBVC23n2Ykqe0Q.gif)

With the `Counter` component shown below:

Simple, huh?

Let me ask you one simple question. Why exactly do we have this component as a Class component?

Well, the answer is simply because we need to keep track of some local state within the component.

Now, here’s the same component refactored to a functional component with access to state via the `useState` hooks.

![Image](https://cdn-media-1.freecodecamp.org/images/1*GxX7yyUGXJG2Kmf8CIG3aQ.gif)
_Class to Hooks — wait for the animation._

What’s different?

I’ll walk you through it step by step.

A functional component doesn’t have all the `Class extend ...` syntax.

```
function CounterHooks() {  }
```

It also doesn’t require a `render` method.

```
function CounterHooks() {    return (      <div>        <h3 className="center">Welcome to the Counter of Life </h3>        <button           className="center-block"           onClick={this.handleClick}> {count} </button>      </div>    ); }
```

There are two concerns with the code above.

1. You’re not supposed to use the `this` keyword in function components.
2. The `count` state variable hasn’t been defined.

Extract `handleClick` to a separate function within the functional component:

```
function CounterHooks() {  const handleClick = () => {      }  return (      <div>        <h3 className="center">Welcome to the Counter of Life </h3>        <button           className="center-block"           onClick={handleClick}> {count} </button>      </div>    ); }
```

Before the refactor, the `count` variable came from the class component’s state object.

In functional components, and with hooks, that comes from invoking the `useState` function or hook.

`useState` is called with one argument, the initial state value e.g. `useState(0)` where `0` represents the initial state value to be kept track of.

Invoking this function returns an array with two values.

```
//? returns an array with 2 values. useState(0) 
```

The first value being the current state value being tracked, and second, a function to update the state value.

Think of this as some `state` and `setState` replica - however, they aren’t quite the same.

With this new knowledge, here’s `useState` in action.

```
function CounterHooks() {  // ?   const [count, setCount] = useState(0);  const handleClick = () => {    setCount(count + 1)  }  return (      <div>        <h3 className="center">Welcome to the Counter of Life </h3>        <button           className="center-block"           onClick={handleClick}> {count} </button>      </div>    ); } 
```

There are a few things to note here, apart from the obvious simplicity of the code!

One, since invoking `useState` returns an array of values, the values could be easily destructed into separate values as shown below:

```
const [count, setCount] = useState(0);
```

Also, note how the `handleClick` function in the refactored code doesn’t need any reference to `prevState` or anything like that.

It just calls `setCount` with the new value `count + 1`.

```
  const handleClick = () => {    setCount(count + 1) }
```

This is because of the correct value of the `count` state variable will always be kept across re-renders.

So, need to update count state variable, just call `setCount` with the new value e.g. `setCount(count + 1)`

Simple as it sounds, you’ve built your very first component using hooks. I know it’s a contrived example, but that’s a good start!

**Nb**: it’s also possible to pass a function to the state updater function. This is usually recommended as with class’ `setState` when a state update depends on a previous value of state e.g. `setCount(prevCount => prevCount +` 1)

#### Multiple useState calls

With class components, we all got used to set state values in an object whether they contained a single property or more.

```
// single property state = {  count: 0}// multiple properties state = { count: 0, time: '07:00'}
```

With `useState` you may have noticed a subtle difference.

In the example above, we only called `useState` with the actual initial value. Not an object to hold the value.

```
useState(0)
```

So, what if we wanted to another state value?

Can multiple `useState` calls be used?

Consider the component below. Same as before but this time it tracks time of click.

![Image](https://cdn-media-1.freecodecamp.org/images/1*E_BJDnVGUB8BLBs1tN2DKA.gif)

As you can see, the hooks usage is quite the same, except for having a new `useState` call.

```
const [time, setTime] = useState(new Date())
```

Now `time` is used in the rendered `JSX` to retrieve the hour, minute and second of the click.

```
<p className="center">    at: { `${time.getHours()} : ${time.getMinutes()} : ${time.getSeconds()}`}</p>
```

Great!

However, is it possible to use an object with `useState` as opposed to multiple `useState` calls?

Absolutely!

If you choose to do this, you should note that unlike `setState` calls, the values passed into `useState` replaces the state value. `setState` merges object properties but `useState` replaces the entire value.

### The Effect Hook

With class components you’ve likely performed side effects such as logging, fetching data or managing subscriptions.

These side effects may be called “effects” for short, and the effect hook, `useEffect` was created for this purpose.

How’s it used?

Well, the `useEffect` hook is called by passing it a function within which you can perform your side effects.

Here’s a quick example.

```
useEffect(() => {  // ? you can perform side effects here  console.log("useEffect first timer here.")}) 
```

To `useEffect` I’ve passed an anonymous function with some side effect called within it.

The next logical question is, when is the `useEffect` function called?

Well, remember that in class components you had lifecycle methods such as `componentDidMount` and `componentDidUpdate`.

Since functional components don’t have these lifecycle methods, `useEffect` _kinda_ takes their place.

Thus, in the example above, the function within `useEffect` also known as the effect function, will be invoked when the functional component mounts (`componentDidMount`) and when the component updates `componentDidUpdate`).

Here’s that in action.

By adding the `useEffect` call above to the counter app, here’s the behavior we get.

![Image](https://cdn-media-1.freecodecamp.org/images/1*0lmKYgp9IoA0ELj4Pfn7vw.gif)

**NB**: The `useEffect` hook isn’t entirely the same as `componentDidMount` + `componentDidUpdate`. It can be viewed as such, but the implementation differs with some subtle differences.

It’s interesting that the effect function was invoked every time there was an update. That’s great, but it’s not always the desired functionality.

What if you only want to run the effect function only when the component mounts?

That’s a common use case and `useEffect` takes a second parameter, an array of dependencies to handle this.

If you pass in an empty array, the effect function is run only on mount — subsequent re-renders don’t trigger the effect function.

```
useEffect(() => {    console.log("useEffect first timer here.")}, []) 
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*RsAP38Wj8zUihrVXNwKcsw.gif)

If you pass any values into this array, then the effect function will be run on mount, and anytime the values passed are updated. i.e if any of the values are changed, the effected call will re-run.

```
useEffect(() => {    console.log("useEffect first timer here.")}, [count]) 
```

The effect function will be run on mount, and whenever the count function changes.

![Image](https://cdn-media-1.freecodecamp.org/images/1*0lmKYgp9IoA0ELj4Pfn7vw.gif)
_count changes when the button is clicked, so the effect function re-runs_

What about subscriptions?

It’s common to subscribe and unsubscribe from certain effects in certain apps.

Consider the following:

```
useEffect(() => {  const clicked = () => console.log('window clicked');  window.addEventListener('click', clicked);}, [])
```

In the effect above, upon mounting, a click event listener is attached to the window.

How do we unsubscribe from this listener when the component is unmounted?

Well, `useEffect` allows for this.

If you return a function within your effect function, it will be invoked when the component unmounts. This is the perfect place to cancel subscriptions as shown below:

```
useEffect(() => {    const clicked = () => console.log('window clicked');    window.addEventListener('click', clicked);    return () => {      window.removeEventListener('click', clicked)    } }, [])
```

There’s a lot more you can do with the `useEffect` hook such as making API calls.

### Build Your own Hooks

From the start of this article we’ve taken (and used) candies from the candy box React provides.

However, React also provides a way for you to make your own unique candies — called custom hooks.

So, how does that work?

A custom hook is just a regular function. However, its name must begin with the word, `use` and if needed, it may call any of the React hooks within itself.

Below’s an example:

### The Rules of Hooks

There are two rules to adhere to while using hooks.

1. Only Call Hooks at the [Top Level](https://reactjs.org/docs/hooks-rules.html#only-call-hooks-at-the-top-level) i.e. _not_ within conditionals, loops or nested functions.
2. Only Call Hooks from React Functions i.e. Functional Components and Custom Hooks.

This ESLint [plugin](https://www.npmjs.com/package/eslint-plugin-react-hooks) is great to ensure you adhere to these rules within your projects.

### Other Candies

We have considered a few of the hooks React provides, but there’s more!

This introduction should have prepared you to take on the perhaps more dense [documentation](https://reactjs.org/docs/hooks-intro.html). Also checkout my live editable react [hooks cheatsheet](https://react-hooks-cheatsheet.com).

