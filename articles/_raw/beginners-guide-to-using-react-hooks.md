---
title: React Hooks for Beginners - A Brain-Friendly Guide on useState and useEffect
subtitle: ''
author: Chris Blakely
co_authors: []
series: null
date: '2020-06-02T14:53:21.000Z'
originalURL: https://freecodecamp.org/news/beginners-guide-to-using-react-hooks
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/beginners-guide-to-hooks.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: react hooks
  slug: react-hooks
- name: React
  slug: reactjs
seo_title: null
seo_desc: '"What the heck are hooks?"

  I found myself asking this just as I thought I had covered all the basis of React.
  Such is the life of a frontend developer, the game is always changing. Enter Hooks.

  It''s always nice to learn something new right? Of course...'
---

"What the heck are hooks?"

I found myself asking this just as I thought I had covered all the basis of React. Such is the life of a frontend developer, the game is always changing. Enter Hooks.

It's always nice to learn something new right? Of course! But sometimes we have to ask ourselves "Why? What's the point in this new thing? Do I have to learn it"?

With hooks, the answer is "not right away". If you have been learning React, and have been using class-based components to date, there is no rush to move to hooks. Hooks are optional and can work in tandem with your existing components. Don't you hate it when you have to rewrite your entire codebase to get some new thing to work?

Anyway, here are some reasons why hooks were introduced in the first place and why I recommend beginners should learn them.

## Using state in functional components

Before hooks, we could not use state in functional components. That means if you have a nicely crafted and tested functional component that suddenly needs to store state, you are stuck with the painful task of refactoring your functional component into a class component. 

Hurray! Allowing state within functional components means we don't have to refactor our presentation components [Check out this article for more](https://scotch.io/courses/5-essential-react-concepts-to-know-before-learning-redux/presentational-and-container-component-pattern-in-react).

## Class components are clunky

Let's face it, class components come with a lot of boilerplate. Constructors, binding, using "this" everywhere. Using functional components removes a lot of this, so our code becomes easier to follow and maintain.

You can read more about this [on the React docs:](https://reactjs.org/docs/hooks-intro.html#classes-confuse-both-people-and-machines)

## More readable code

Since hooks let us use functional components, it means there's less code compared to class components. This makes our code more readable. Well, thats the idea anyway. 

We don't have to worry about binding our functions, or remember what "this" relates too, and so on. We can worry about writing our code instead.

> [If you're just starting out with React, I have a bunch of getting started posts on my blog that might help you out! Check it out here:](https://www.jschris.com)


## React State Hook

Ah, state. A cornerstone of the React ecosystem. Let's get our feet wet with Hooks by introducing the most common hook that you will be working with - `useState()`.

Let's take a look at a class component that has state.

```jsx

import React, { Component } from 'react';
import './styles.css';

class Counter extends Component {
	state = {
		count: this.props.initialValue,
	};

	setCount = () => {
		this.setState({ count: this.state.count + 1 });
	};

	render() {
		return (
			<div>
				<h2>This is a counter using a class</h2>
				<h1>{this.state.count}</h1>

				<button onClick={this.setCount}>Click to Increment</button>
			</div>
		);
	}
}

export default Counter;

```

With React Hooks, we can rewrite this component and remove a lot of stuff, making it easier to understand:

```jsx

import React, { useState } from 'react';

function CounterWithHooks(props) {
	const [count, setCount] = useState(props.initialValue);

	return (
		<div>
			<h2>This is a counter using hooks</h2>
			<h1>{count}</h1>
			<button onClick={() => setCount(count + 1)}>Click to Increment</button>
		</div>
	);
}

export default CounterWithHooks;

```

On the face of it there is less code, but what's going on?


### React State Syntax


So we've seen our first hook! Hurrah!

```jsx
 const [count, setCount] = useState();
```

Basically, this uses destructuring assignment for arrays. The `useState()` function gives us 2 things: 

- **a variable to hold the state value**, in this case, it's called `count` - **a function to change the value**, in this case, it's called `setCount`.

You can name these whatever you want:

```jsx

const [myCount, setCount] = useState(0);

```

And you can use them throughout the code like normal variables/functions:

```jsx

function CounterWithHooks() {
	const [count, setCount] = useState();

	return (
		<div>
			<h2>This is a counter using hooks</h2>
			<h1>{count}</h1>
			<button onClick={() => setCount(count + 1)}>Click to Increment</button>
		</div>
	);
}

```

Notice the `useState` hook at the top. We're declaring/destructuring 2 things:

- `counter`: a value which will hold our state value
- `setCounter`: a function which will change our `counter` variable

As we continue through the code, you'll see this line:

```jsx

<h1>{count}</h1>

```

This is an example of how we can use a state hook variable. Within our JSX, we place our `count` variable within `{}` to execute it as JavaScript, and in turn the `count` value gets rendered on the page. 

Comparing this to the old "class-based" way of using a state variable:

```jsx

<h1>{this.state.count}</h1>

```

You'll notice we no longer need to worry about using `this`, which makes our life a lot easier - for example, the VS Code editor will give us a warning if `{count}` is not defined, allowing us to catch errors early. Whereas it won't know if `{this.state.count}` is undefined until the code is run.

On to the next line!

```jsx

 <button onClick={() => setCount(count + 1)}>Click to Increment</button>

```

Here, we're using the `setCount` function (remember we destructured/declared this from the `useState()` hook) to change the `count` variable.

When the button is clicked, we update the `count` variable by `1`. Since this is a change of state this triggers a rerender, and React updates the view with the new `count` value for us. Sweet!

### How can I set the initial state?

You can set the initial state by passing an argument to the `useState()` syntax. This can be a hardcoded value:

```jsx

 const [count, setCount] = useState(0);

```

Or can be taken from the props:

```jsx

 const [count, setCount] = useState(props.initialValue);

```

This would set the `count` value to whatever the `props.initialValue` is.

That sums up `useState()`. The beauty of it is that you can use state variables/functions like any other variable/function you would write yourself.

### How do I handle multiple state variables?

This is another cool thing about hooks. We can have as many as we like in a component:

```jsx

 const [count, setCount] = useState(props.initialValue);
 const [title, setTitle] = useState("This is my title");
 const [age, setAge] = useState(25);

```

As you can see, we have 3 seperate state objects. If we wanted to update the age for example, we just call the **setAge()** function. The same with **count** and **title**. We no longer are tied to the old clunky class component way where we have one massive state object stored using **setState()**:

```jsx

this.setState({ count: props.initialValue, title: "This is my title", age: 25 })

```


## So, what about updating things when props or state changes?

When using hooks and functional components, we no longer have access to React lifecycle methods like `componentDidMount`, `componentDidUpdate`, and so on. Oh, dear! Do not panic my friend, React has given us another hook we can use:

* _Drum Roll_ * 

## Enter useEffect!

The Effect hook (**useEffect()**) is where we put "side effects".

Eh, side effects? What? Let's go off-track for a minute and discuss what a side effect actually is. This will help us understand what `useEffect()` does, and why it's useful.

A boring computer-y explanation would be.

> "In programming, a side effect is when a procedure changes a variable from outside its scope"

In React-y terms, this means "when a component's variables or state changes based on some outside thing". For example, this could be:

- When a component receives new props that change its state
- When a component makes an API call and does something with the response (e.g, changes the state)

So why is it called a side effect? Well, *we cannot be sure what the result of the action will be*. We can never be 100% certain what props we are going to receive, or what the response from an API call would be. And, we cannot be sure how this will affect our component. 

Sure we can write code to validate, and handle errors, and so on, but ultimately we cannot be sure what the side effects of said things are. 

So for example, when we change state, based on some *outside thing* this is know as a side effect.

With that out of the way, let's get back to React and the useEffect Hook!

When using functional components we no longer have access to life cycle methods like `componentDidMount()`, `componentDidUpdate()` etc. So, in effect (pun intended), the useEffect hooks replace the current React Life Cycle hooks.

Let's compare a class-based component with how we use the useEffect hook:

```jsx
import React, { Component } from 'react';

class App extends Component {
	componentDidMount() {
		console.log('I have just mounted!');
	}

	render() {
		return <div>Insert JSX here</div>;
	}
}
```

And now using useEffect():

```jsx
function App() {
	useEffect(() => {
		console.log('I have just mounted!');
	});

	return <div>Insert JSX here</div>;
}
```

Before we continue, it's important to know that, by default, **the useEffect hook runs on every render and re-render**. So whenever the state changes in your component or your component receives new props, it will rerender and cause the useEffect hook to run again.

### Running an effect once (componentDidMount)

So, if hooks run every time a component renders, how do we ensure a hook only runs once when the component mounts? For example, if a component fetches data from an API, we don't want this happening every time the component re-renders!

The `useEffect()` hook takes a second parameter, an array, **containing the list of things that will cause the useEffect hook to run**. When changed, it will trigger the effect hook. The key to running an effect once is to pass in an empty array:

```jsx
useEffect(() => {
	console.log('This only runs once');
}, []);
```

So this means the useEffect hook will run on the first render as normal. However, when your component rerenders, the useEffect will think "well, I've already run, there's nothing in the array, so I won't have to run again. Back to sleep for me!" and simply does nothing.

> In summary, empty array = `useEffect` hook runs once on mount

### Using effects when things change (componentDidUpdate)

We've covered how to make sure a `useEffect` hook only runs once, but what about when our component receives a new prop? Or we want to run some code when the state changes? Hooks let us do this as well!

```jsx
 useEffect(() => {
	console.log("The name props has changed!")
 }, [props.name]);
```

Notice how we are passing stuff to the useEffect array this time, namely _props.name_. 

In this scenario, the useEffect hook will run on the first load as always. Whenever your component receives a new **name prop** from its parent, the useEffect hook will be triggered, and the code within it will run.

We can do the same thing with state variables:

```jsx
const [name, setName] = useState("Chris");

 useEffect(() => {
    console.log("The name state variable has changed!");
 }, [name]);
```

Whenever the `name` variable changes, the component rerenders and the useEffect hook will run and output the message. Since this is an array, we can add multiple things to it:

```jsx
const [name, setName] = useState("Chris");

 useEffect(() => {
    console.log("Something has changed!");
 }, [name, props.name]);
```

This time, when the `name` state variable changes, or the `name prop` changes, the useEffect hook will run and display the console message.

### Can we use componentWillUnmount()?

To run a hook as the component is about to unmount, we just have to return a function from the `useEffect` hook:

```jsx
useEffect(() => {
	console.log('running effect');

	return () => {
		console.log('unmounting');
	};
});
```

## Can I use different hooks together?

Yes! You can use as many hooks as you want in a component, and mix and match as you like:

```jsx
function App = () => {
	const [name, setName] = useState();
	const [age, setAge] = useState();

	useEffect(()=>{
		console.log("component has changed");
	}, [name, age])

	return(
		<div>Some jsx here...<div>
	)
}

```

## Conclusion - What Next?

There you have it. Hooks allow us to use good old fashioned JavaScript functions to create simplier React components, and reduce alot of boilerplate code. 

Now, run off into the world of Reac hooks and try building stuff yourself! Speaking of building stuff yourself...



