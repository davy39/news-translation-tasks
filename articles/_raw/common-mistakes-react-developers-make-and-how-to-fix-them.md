---
title: Common Mistakes React Developers Make – And How to Fix Them
subtitle: ''
author: Yogesh Chavan
co_authors: []
series: null
date: '2021-05-03T16:40:08.000Z'
originalURL: https://freecodecamp.org/news/common-mistakes-react-developers-make-and-how-to-fix-them
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/christin-hume-mfB1B1s4sMc-unsplash-1.jpg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: null
seo_desc: 'In this article, we''ll see some of the common mistakes that React developers
  make, and how you can avoid them.

  So let''s get started.

  Don''t Forget that Every Route Change Mounts and Unmounts a Component

  Whenever you''re using routing in a React applica...'
---

In this article, we'll see some of the common mistakes that React developers make, and how you can avoid them.

So let's get started.

## Don't Forget that Every Route Change Mounts and Unmounts a Component

Whenever you're using routing in a React application, you declare routes inside the `Switch` component. This means that only one component with the matching route is displayed at a time.

Therefore, whenever you go from one route to another, the previously displayed component is unmounted and the component with the new matching route is mounted.

If you need to persist some data across a route change, you need to declare it in the component which encapsulates the routes. It could be the `App` component in the following Code Sandbox, or some other way of persisting data like using [local storage or session storage](https://javascript.plainenglish.io/everything-you-need-to-know-about-html5-local-storage-and-session-storage-479c63415c0a?source=friends_link&sk=f429aa5008683a3b0359db43f976efb3)

%[https://codesandbox.io/s/hopeful-faraday-hqz9x?file=/src/App.js]

As you can see in the above Code Sandbox, whenever we change the route by clicking on the links, the corresponding `console.log` gets displayed on the console. This indicates that the previous component is unmounted and a new component is mounted.

## Don't Use the Wrong setState Syntax

Whenever you declare some state inside a class-based component, it's always an object like this:

```js
this.state = {
 counter: 0
}

```

So whenever you use the updater form of the setState syntax to update the state, it looks like this:

```js
this.setState((prevState) => {
  return {
    counter: prevState.counter + 1
  };
});

```

Since state is an object, `prevState` is also an object – so you access the `counter` using `prevState.counter`.

But when you're using functional components with React Hooks, the state can be an object or a non-object value as shown below:

```js
const [counter, setCounter] = useState(0);

```

Here, the value of `counter` is not an object but it's a number. So to update the state using updater syntax, you'll write the code like this:

```js
setCounter((prevCounter) => prevCounter + 1);

```

Here, the `prevCounter` is a number. So you don't use `prevCounter.counter` – just `prevCounter`. Or you can simplify it as shown below:

```js
setCounter((counter) => counter + 1);

```

> Check out [my article here](https://www.freecodecamp.org/news/what-is-state-in-react-explained-with-examples/) for a complete introduction to React state.

## Don't Call Hooks from Class Components

Starting with version 16.8.0, React introduced Hooks. They allow you to write better React code and make use of state and component life cycle methods inside functional components.

> Check out [my article here](https://levelup.gitconnected.com/an-introduction-to-react-hooks-50281fd961fe?source=friends_link&sk=89baff89ec8bc637e7c13b7554904e54) for an introduction to React hooks.

To make coding easier, React provides many hooks like:

* The `useParams` hook to access URL parameters when using React Routing
* The `useHistory` hook to get access to history API inside any component
* The `useRef` hook to get access to the DOM element

and many other hooks.

But all of these hooks (which usually start with the `use` keyword) work only inside functional components.

If you have a class-based component then you can't use these hooks. You need to refactor your code to convert it to functional components. If you don't, you might get an error like the one in the below screenshot:

![Image](https://www.freecodecamp.org/news/content/images/2021/05/hook_error.png)

## Don't Forget to Add a Key Prop When Using the Array `map` Method

Take a look at [this Code Sandbox Demo](https://codesandbox.io/s/quirky-shockley-bjd6z?file=/src/index.js).

Here, to display a list of items, you can use the following code:

```js
const Items = ({ items }) => (
  <ol>
    {items.map((item) => (
      <Item item={item} />
    ))}
  </ol>
);

```

In React, you'll usually use the array `map` method to display a list of items stored in an array.

But as soon as you add an item to the list in the above Code Sandbox, you will see a missing key warning displayed in the console.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/missing-key.gif)

This is because every time you're using the array `map` method to loop over the items, you need to provide a unique `key` prop. React uses this to identify which elements on the screen need to be re-rendered, so adding the `key` prop helps you avoids unnecessary re-rendering in your app.

Here's an updated [Code Sandbox Demo](https://codesandbox.io/s/boring-greider-olko7?file=/src/index.js) with the added `key` prop.

Here, I've provided a unique `key` prop to each element we're looping over like this:

```js
<Item item={item} key={index} />

```

Now if you try to add some items, you won't get any warnings in the console.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/added-key.gif)

> Note: In the above code, as the elements not re-ordered or removed, using `index` as `key` works fine. But if you're removing or changing the displayed elements' order, then you need to provide a unique key instead of using `index`.

## Don't Use Inline Functions the Wrong Way

Take a look at [this Code Sandbox Demo](https://codesandbox.io/s/stupefied-breeze-66nyr?file=/src/index.js).

Here, I've added some items to the state:

```js
const [items, setItems] = useState(["one", "two"]);

```

and we're looping over them to display on the screen:

```jsx
{items.map((item, index) => (
  <li key={index}>
    {item} <button onClick={handleRemoveItem(item)}>Remove</button>
  </li>
))}

```

If you check the application, you will see that no items are displayed on the screen. Adding new items also doesn't work as you can see below:

![Image](https://www.freecodecamp.org/news/content/images/2021/05/wrong_inline.gif)

This is because of the `onClick`  handler for the button:

```jsx
<button onClick={handleRemoveItem(item)}>Remove</button>

```

Here, we're calling the `handleRemoveItem` method when the user clicks on the button – but the way we're calling the method is wrong.

So if you don't need to pass any parameters, you use the following syntax:

```jsx
<button onClick={handleRemoveItem}>Remove</button>

```

But later if you decide to pass some parameter to the function, you need to call the handler inside the inline function like this:

```jsx
<button onClick={() => handleRemoveItem(item)}>Remove</button>

```

Most React developers forget to add an inline function and then it takes hours of debugging to understand why something does not work.

Here's an updated working [Code Sandbox Demo](https://codesandbox.io/s/polished-moon-02iug?file=/src/index.js).

### **Thanks for reading!**

Starting with ES6, there are many useful additions to JavaScript like:

* ES6 Destructuring
* Import and Export Syntax
* Arrow functions
* Promises
* Async/await
* Optional chaining operator and a lot more.

**You can learn everything about all the ES6+ features in detail in my [Mastering Modern JavaScript](https://modernjavascript.yogeshchavan.dev/) book.**

> Check out free preview contents of the book [here](https://www.freecodecamp.org/news/learn-modern-javascript/).

Also, you can check out my **free** [Introduction to React Router](https://yogeshchavan1.podia.com/react-router-introduction) course to learn React Router from scratch.

Want to stay up to date with regular content regarding JavaScript, React, Node.js? [Follow me on LinkedIn](https://www.linkedin.com/in/yogesh-chavan97/).

<a href="https://bit.ly/3w0DGum" target="_blank" rel="noreferrer noopener"><img src="https://gist.github.com/myogeshchavan97/98ae4f4ead57fde8d47fcf7641220b72/raw/c3e4265df4396d639a7938a83bffd570130483b1/banner.jpg"></a>


