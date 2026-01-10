---
title: 'React hooks: a new way of working with React state'
subtitle: ''
author: Mihail Gaberov
co_authors: []
series: null
date: '2018-11-08T15:54:15.000Z'
originalURL: https://freecodecamp.org/news/hooking-with-react-hooks-964df4b23960
coverImage: https://cdn-media-1.freecodecamp.org/images/1*UNln2JsoPZEVzgGPJhs98w.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'Updated: With React 16.8, React Hooks are available in a stable release!

  Outdated: Hooks are still an experimental proposal. They’re currently in React v16.7.0-alpha

  TL;DRIn this article we will attempt to understand what are React Hooks and how
  to u...'
---

**Updated: With React 16.8,** [**React Hooks**](https://reactjs.org/docs/hooks-intro.html) **are available in a stable release!**

Outdated: Hooks are still an experimental proposal. They’re currently in React v16.7.0-alpha

**TL;DR**  
In this article we will attempt to understand what are [React Hooks](https://reactjs.org/docs/hooks-intro.html) and how to use them for our good. We will implement different examples and see the differences (gains) Hooks bring to us. If you want to skip the reading, [here](https://mihailgaberov.github.io/react-hooks/) you can find shorter version in a few slides. And [here](https://github.com/mihailgaberov/react-hooks) ? you may get the examples and try them yourself.

### What are *React Hooks*?

> Simple functions for hooking into the React state and lifecycle features from function components.

What this means is that hooks allow us to easily manipulate our function component’s state without needing to convert them into class components. This saves us from having to deal with all the boilerplate code involved.

Hooks don’t work inside classes — they let you use React without classes. And also, by using them, we can totally avoid using lifecycle methods, such as *componentDidMount*, *componentDidUpdate*, etc. Instead, we will use built-in hooks like *useEffect*, *useMutationEffect* or *useLayoutEffect*. We will see how in a moment.

Hooks are JavaScript functions, but they impose two additional [rules](https://reactjs.org/docs/hooks-rules.html):

❗️ Only call Hooks **at the top level**. Don’t call Hooks inside loops, conditions, or nested functions.

❗️ Only call Hooks **from React function components**. Don’t call Hooks from regular JavaScript functions. There is just one other valid place to call Hooks — your own custom Hooks. We’ll see them later in this article.

### Why are they *good thing?*

? R**eusing logic**  
Up until now, if we wanted to reuse some logic in React, we had two options: h[igher-order components](https://tylermcginnis.com/react-higher-order-components/) or r[ender props.](https://www.robinwieruch.de/react-render-props-pattern/) With React Hooks we have an alternative, that comes with a much easier to understand (in my personal opinion!) syntax and logic flow.

? G**iant components**  
By avoiding the boilerplate code we need to write when using classes or by removing the need for multiple nesting levels (which could come when using render props), React Hooks solve the issue of having giants components (that are really hard to maintain and debug).

? C**onfusing classes**  
Again, allowing us NOT to use classes or class components in our applications makes the developers’s (especially beginner’s) life easier. This is because we don’t have to use the ‘this’ keyword and we don’t need to have the understanding of how bindings and scopes work in React (and JavaScript).

This is NOT to say that we (the developers) don’t have to learn these concepts — on the contrary we must be aware of them. But in this case, when using React hooks, our worries are one fewer ?.

> ***So, after pointing out what issues the hooks solve, when would we use them?***

> *If you write a function component and realize you need to add some state to it, previously you had to convert it to a class. Now you can use a Hook inside the existing function component. We’re going to do that in the next examples.*

### How to use *React Hooks*?

React Hooks come to us as [built-in ones](https://reactjs.org/docs/hooks-overview.html) and [custom ones](https://reactjs.org/docs/hooks-custom.html). The later are the ones we can use for sharing logic across multiple React components.

As we’ve already learned, hooks are simple JavaScript functions, which means we will be writing just that, but in the context of React *function* components. Previously these components were called *stateless*, a term that is not valid anymore, as *hooks* give us a way to use the state in such components ?.

> *An important thing to remember is that we can use both built-in and custom hooks multiple times in our components. We just have to follow the* [*rules of hooks*](https://reactjs.org/docs/hooks-rules.html)*.*

The following examples try to illustrate that.

#### Basic built-in hooks

* [useState](https://github.com/mihailgaberov/react-hooks/blob/master/src/components/Counter/CounterHooked.js) hook — returns a stateful value and a function to update it.
    
* [useEffect](https://reactjs.org/docs/hooks-effect.html) hook — accepts a function that contains imperative, possibly effectful code (for example fetching data or subscribing to a service). This hook could return a function that is being executed every time before the effect runs and when the component is unmounted — to clean up from the last run.
    
* [useContext](https://github.com/mihailgaberov/react-hooks/blob/master/src/components/Counter/CounterHooked.js) hook — accepts a [context](https://reactjs.org/docs/context.html) object and returns the current [context](https://github.com/mihailgaberov/react-hooks/blob/master/src/ColorContext.js) value, as given by the nearest context provider for the given context.
    

#### Custom hooks

**A custom Hook is a JavaScript function whose name starts with “**`use`” and that may call other Hooks. For example, [useFriendName](https://github.com/mihailgaberov/react-hooks/blob/master/src/useFriendName.jshttps://github.com/mihailgaberov/react-hooks/blob/master/src/useFriendName.js) below is our first custom Hook:

```js
export default function useFriendName(friendName) {
  const [isPresent, setIsPresent] = useState(false);
  
  useEffect(() => {
    const data = MockedApi.fetchData();
    data.then((res) => {
      res.forEach((e) => {
        if (e.name === friendName) {
          setIsPresent(true);
        }
     });
    });
  });
    
  return isPresent;
}
```

Building your own custom hooks lets you extract component logic into reusable functions. This could be your application’s shared functionality that you can import everywhere you need it. And also, we must not forget, that our custom hooks are the other allowed ([see the rules](https://reactjs.org/docs/hooks-rules.html#only-call-hooks-from-react-functions)) places to call built-in hooks.

### Conclusion

React Hooks are not really a new feature that popped out just now. They are another (better ❓) way of doing React components that need to have *state* and/or *lifecycle* methods. Actually, they use the same internal logic that is being used currently by the class components. To use them or not — this is the question to which the future will give the best answer.

> *My personal opinion? That this is going to be the future of any React development that involves state and lifecycle usage.*

Let’s see how the community will react to the proposal ? and hopefully we will see them polished and fully functioning in the next React releases. ?

? Thanks for reading! ?

### References

Here you may find the links to the resources I found useful when writing this article:

* [https://github.com/mihailgaberov/react-hooks](https://github.com/mihailgaberov/react-hooks)/ — link to GitHub repo with the examples and presentation.
    
* [https://mihailgaberov.github.io/react-hooks/](https://mihailgaberov.github.io/react-hooks/#0) — link to presentation slides.
    
* [https://reactjs.org/docs/hooks-intro.html](https://reactjs.org/docs/hooks-intro.html) — official ReactJS blog.
    
* [https://youtu.be/dpw9EHDh2bM](https://youtu.be/dpw9EHDh2bM) — Introduction to Hooks, React Conf 2018
    
* [https://medium.com/@dan\_abramov/making-sense-of-react-hooks-fdbde8803889](https://medium.com/@dan_abramov/making-sense-of-react-hooks-fdbde8803889) — An explanatory article by Dan Abramov.
    
* [https://daveceddia.com/useeffect-hook-examples/](https://daveceddia.com/useeffect-hook-examples/) — A very useful article explaining different use cases of useEffect hook.
    
* [https://ppxnl191zx.codesandbox.io/](https://ppxnl191zx.codesandbox.io/) — An example of a React animation library experimenting with Hooks.
    
* [https://dev.to/oieduardorabelo/react-hooks-how-to-create-and-update-contextprovider-1f68](https://dev.to/oieduardorabelo/react-hooks-how-to-create-and-update-contextprovider-1f68) — A nice and short article showing how to create and update context provider with React Hooks.
