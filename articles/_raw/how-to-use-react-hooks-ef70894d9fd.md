---
title: How to use React hooks
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-08T09:33:42.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-react-hooks-ef70894d9fd
coverImage: https://cdn-media-1.freecodecamp.org/images/0*ayfiDWDbZ9rrvmd4
tags:
- name: frontend
  slug: frontend
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Sergei Gannochenko

  React 16.7.0 is finally out. It has no hooks on-board, but sooner or later, React
  Hooks will be there. So today we will have a talk so we’re ready to use it right
  away when it is time ?

  Sometimes when you write your pure functio...'
---

By Sergei Gannochenko

React 16.7.0 is finally out. It has no hooks on-board, but sooner or later, React Hooks will be there. So today we will have a talk so we’re ready to use it right away when it is time ?

Sometimes when you write your pure function component, you realize that at some moment you need to have a sort of flag there, which indicates that a modal is open, counter increased or… whatever. And then your second thought is: “oh man, now I need to migrate to React.Component”. Well, with hooks — not anymo-o-ore!

I’ll assume you have Node of the following versions installed: 6.14.0, 8.10.0 or greater than 9.10. If not, you can always use the Node version manager to fix that. Keep in mind though, that we will have to install all global packages in case we switch the Node version.

This article requires that you have at least a basic knowledge of React, including the “_component_” and “_pure function_” concepts, “_state_” and “_component lifecycle_”. But even if you don’t, no worries, you will catch up during the process, it will be fun!

#### Step 1: The Boilerplate

Open your terminal, as we are going to use a super-famous code generator for React applications, called _create-react-app_:

```
npm install create-react-app -gcreate-react-app react-hooks
```

Now, we are able to see a folder called `./react-hooks`, so we go there and consider this to be a root of our application.

In order to actually enable hooks, we need to go to a list of versions of React at [npmjs.com](https://www.npmjs.com/package/react). By the time this article was written, the latest version with hooks enabled was [16.7.0-alpha.2](https://www.npmjs.com/package/react/v/16.7.0-alpha.2), so let’s install this. We also need to install a pair package called _react-dom_ of exactly the same version.

So,

```
npm install react@16.7.0-alpha.2 --savenpm install react-dom@16.7.0-alpha.2 axios --save
```

Don’t forget to start the application:

```
npm start
```

#### Step 2: useState()

Let’s find the `./src/App.js` file and re-write it like this:

And this is the first kind of hooks we can use: a state hook created with _useState()._ Basically, _useState()_ accepts the initial value of some value and returns an array, where the first element is a variable with the initial value, and the second one is a function which allows us to change the variable. After we call _setCounter()_, the component gets re-rendered with an updated value of the counter.

The equivalent code without hooks would be:

But with hooks, the code is way cleaner, and it does not even rely on object-oriented programming and _this_ statements, which sometimes can be really cryptic to use for non-experienced JavaScript developers.

The state could be a complex object, no problem:

But according to the philosophy of hooks, it is better to define two state values instead:

This makes your code really easy to understand.

#### Step 3: useEffect()

In the react world, a _side effect_ is an action that is usually executed on the _componentDidMount(), componentDidUpdate()_ and _componentWillUnmount()_ lifecycle methods of _React.Component_. But what if we still would like to have a side effect, but with a pure function? Sure thing! Consider the code:

The function inside _useEffect()_ is called on the first render and all consequent renders, which does not really make any difference between this and if we just put the code inside the component function directly.

But, wait. That is not all!

We could do some optimizations by telling _useEffect()_ to run only when certain values have changed. Consider this:

So, _useEffect()_ will memoize _[forBatman, forJoker]_ value and will only re-run the effect if something changed in these arguments.

Let’s consider more use cases.

#### Case A: execute code on un-mount

What if we want to catch a moment when the component gets unmounted? All we have to do is to return a function like this:

_“SubComponent unmounted_” will appear in the console as soon as you click the “_One for application_” button 5 times.

#### Case B: run only on mount and on unmount

What we could also do is to force an effect to run only on-mount and on-unmount, by passing an empty array as a dependency:

It works because _[]_ stays the same during all the time the component is there until it gets unmounted, no matter what.

#### Case C: load data asynchronously on mount and on update

The last use-case I would like to demonstrate is how to do an asynchronous effect with some data load. Just to be clear, I don’t think that having logic for rendering data and logic for loading data in one place is actually a good idea. The main principle of single responsibility tells us there should be a pure dumb rendering logic and pure rich business logic, that is why I strongly encourage you to try _Redux_ + _Saga_. But I guess this is a nice topic for some other time.

There are two important moments to notice:

* we can not use _useEffect(async () =>_ {}), asynchronous effects are not supported (yet), but we are still able to use promises there, and
* we don’t want this code to run on every render, so we need to define a second argument for _useEffect()_ in the right way. We always ask ourselves: “What needs to be changed in order to re-run the effect?”. The good answer is “_characterId”._

#### Step 4: useRef() & useMemo()

If we open the source code of _React_, we could see some other hooks available. Among them is _useRef()_. We could use it in combination with _useEffect()_ to do some stuff. Consider the code:

What it does is just sets the value of an input field and then calls _focus()_ as soon as the component is mounted.

Another nice one is _useMemo()_. It basically allows us to memoize some value during the process of rendering.

Why do so? Well in case we need to calculate something reasonably heavy (heavy when rendering, huh?), or make some remote call, but only when some certain values change, we might make use of _useMemo()_ thingy_._ It is still not as powerful as traditional ways of memoization, as it can only be used when rendering, but still…

#### Step 5: Under the hood

You may wonder, how does this functionality even work? I mean, components are just pure functions, how do variables preserve their scalar values between function calls? Well, for example, _useState()_ returns an array, from which we use the first argument as a scalar. But this array can be memoized inside _React_, so next time the rendering engine is here, it already knows which values to put into those scalars.

#### Step 6: Don't-s

* First of all, hooks are still in alpha stage, the API may be changed in future, so use it in production on your own risk.
* You can not use hooks outside a component function, it is simply how they work. But, you can make [a composition of hooks](https://reactjs.org/docs/hooks-custom.html).
* React relies on an **amount** and **order** of how hooks appear in the component function. So **don’t even think** of wrapping those calls with conditional logic of some sort. Instead, you may put your _if-s_ inside a hook body.
* At the present moment, hooks do not work for server-side rendering. I hope this to be fixed in the final release.

#### Conclusion

Even though hooks are not available officially, they are definitely going to make our life easier, and the code way cleaner. And it is always important to have understandable code, especially when working with React.

Thanks for reading! If the article was helpful for you, don’t hesitate to share it on social media! :)

#### Extras

* here is [the Proof-of-concept repository](https://github.com/awesome1888/poc_react-hooks) made for the article
* consider reading an [official Hooks reference](https://reactjs.org/docs/hooks-reference.html) by Facebook

Happy Reacting!

