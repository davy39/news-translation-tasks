---
title: 5 JavaScript Tips to Improve Your React Code
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2021-07-06T15:12:00.000Z'
originalURL: https://freecodecamp.org/news/javascript-tips-to-improve-your-react-code-today
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/5-javascript-tips-to-improve-your-react-code.png
tags:
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: React
  slug: react
seo_title: null
seo_desc: "Let's look at five JavaScript tips you can use today to instantly improve\
  \ your React applications. \nBecause React is a JavaScript library, any improvements\
  \ that we make in our JavaScript skills will directly improve the applications that\
  \ we build wit..."
---

Let's look at five JavaScript tips you can use today to instantly improve your React applications. 

Because React is a JavaScript library, any improvements that we make in our JavaScript skills will directly improve the applications that we build with React.

For this reason, I've put together a number of tips to show you how to use the latest JavaScript features to make your React code even better.

## How to Use the Optional Chaining Operator in JavaScript

In JavaScript, we need to first make sure that an object exists before we can access a property from it. 

If the object has a value of `undefined` or `null`, it will result in a type error. 

In our example here, we have a React application where users can edit posts they have made. 

Only if `isPostAuthor` is true – meaning the authenticated user has the same id as the id of the author of the post – will we show the `EditButton` component.

```js
export default function EditButton({ post }) {
  const user = useAuthUser();  
  const isPostAuthor = post.author.userId !== user && user.userId;
    
  return isPostAuthor ? <EditButton /> : null;
}
```

The problem with this code is that our `user` value might have a value of `undefined`. This is why we must use the `&&` operator to make sure `user` is an object before we attempt to get the `userId` property. 

If we were to access an object within an object, we would have to include another `&&` conditional. This can cause our code to become tedious and hard to understand.

Fortunately, a new JavaScript feature that allows us to check and see if an object exists before accessing a property without using the end conditional is the **optional chaining operator.**

To make sure an object exists before attempting to access a property off of it, just put a question mark immediately afterwards:

```js
export default function EditButton({ post }) {
  const user = useAuthUser();  
  const isPostAuthor = post.author.userId !== user?.userId;
    
  return isPostAuthor ? <EditButton /> : null;
}
```

This will prevent any type errors and allows us to write much cleaner conditional logic.

## How to Use Implicit Return with Parentheses in JavaScript

In React applications, we can write components with either the function declaration syntax using the `function` keyword or we can use an arrow function, which must be set to a variable. 

It's important to note that components which use the `function` keyword must use the `return` keyword before returning any JSX.

```js
export default function App() {
  return (
    <Layout>
      <Routes />
    </Layout>
  );
}
```

We can return multiple lines of JavaScript code from a function with an implicit return (without using the `return` keyword), by wrapping the returned code in a set of parentheses.

For components made with arrow functions, we do not have to include the `return` keyword – we can just return our JSX with a set of parentheses.

```js
const App = () => (
  <Layout>
    <Routes />
  </Layout>
);

export default App;
```

Additionally, whenever you are iterating over a list of elements with the React `.map()` function, you can also skip the return keyword and return your JSX just with a set of parentheses in the body of your inner function.

```js
function PostList() {
  const posts = usePostData();  
    
  return posts.map(post => (
    <PostListItem key={post.id} post={post} />  
  ))
}
```

## How to Use the Nullish Coalescing Operator in JavaScript

In JavaScript, if a certain value is falsy (like `null`, `undefined,` `0`, `''`, `NaN`), we can use the or (`||`) conditional to provide a fallback value. 

For example, if we have a product page component and we want to display a given product's price, you can use a `||` conditional to either show the price or show the text "Product is unavailable". 

```js
export default function ProductPage({ product }) {    
  return (
     <>
       <ProductDetails />
       <span>{product.price || "Product is unavailable"} // if price is 0, we will see "Product is unavailable"
     </>
  );
}
```

However, there's a small error with our existing code. 

If the price has the value of `0`, which is falsy, instead of showing the price itself, we're going to show the text "Product is unavailable" – which is not what we want. 

We need a more precise operator to only return the right hand side of our expression if the left hand side is `null` or `undefined` instead of any falsy value. 

This is available now in the **nullish coalescing operator**. It will return its right hand operand when its left hand operand is `null` or `undefined`. Otherwise it will return its left hand side operand:

```
null ?? 'fallback';
// "fallback"

0 ?? 42;
// 0
```

The way to fix our code that we have above is simply to replace the or conditional with the nullish coalescing operator to show the correct price of `0`.

```js
export default function ProductPage({ product }) {    
  return (
     <>
       <ProductDetails />
       <span>{product.price ?? "Product is unavailable"}
     </>
  );
}
```

## How to Use the Object Spread Operator for Updating State in JavaScript

When it comes to using state in React, we have a couple options: we can create many state variables with the `useState` hook for individual primitive values or manage multiple values within one state variable using an object. 

In the example below, we have a signup page where we are keeping track of current users' username, email, and password. 

When they submit the signup form, we validate the form contents they typed in and handle signing up the user. 

```js
import React from 'react'

export default function SignUpPage() {
  const [state, setState] = React.useState({ username: '', email: '', password: '' });
    
  function handleSubmit(event) {   
    event.preventDefault();
    validateForm(state);
    signUpUser(state)
  }

  function handleChange(event) {
    const {name, value} = event.target;
    setState({ ...state, [name]: value });
  }
    
  return (
    <form onSubmit={handleSubmit}>
      <input name="username" onChange={handleChange} />
      <input name="email" onChange={handleChange} />
      <input name="password" onChange={handleChange} />
      <button type="submit">Submit</button>
    </form>
  );
}
```

Note additionally that when using the `useState` hook, you must spread in all of the previous state in order to update an individual key value pair. 

Whenever a user types into an input and the change event takes place, the `handleChange` function is called. 

Then we not only update a certain input's value according to its `name` attribute, but we also spread in all of the current state values of username, email, and password. We spread all of these values as individual properties in the new object we are setting in state with the `...` – the object spread operator.

## How to Use Ternaries to Conditionally Apply Classes / Props in JavaScript

Ternaries are an essential operator to use when writing conditionals within React components. 

We often use ternaries within our JSX because they are expressions and resolve to one or another value that can be displayed. This allows them to often be used to either show or hide components and elements.

It's worth noting, however, that we can use ternaries when it comes to any value within our JSX. 

That means, instead of using third-party libraries like `classnames` to conditionally add or remove classes to our React elements, we can do so with an inline ternary and a JavaScript template literal. 

You can see in the example here that if our user has selected dark mode, we're applying a class `body-dark`. Otherwise we apply the class `body-light` to give our application the appropriate styles to everything within our `Routes` component. 

```js
export default function App() {
  const { isDarkMode } = useDarkMode();
    
  return (
    <main className={`body ${isDarkMode ? "body-dark" : "body-light"}`}>
      <Routes />
    </main>
  );
}
```

It's worth noting that this conditional logic can be applied to any prop as well, not just classnames or inline styles. 

We have another example here in which our application is detecting whether the user's on a mobile device or not with a special hook. If so, we pass down a specific height value through the prop `height` to our `Layout` component.

```js
export default function App() {
  const { isMobile } = useDeviceDetect();
    
  return (
    <Layout height={isMobile ? '100vh' : '80vh'}>
      <Routes />
    </Layout>
  );
}
```

## Become a Professional React Developer

React is hard. You shouldn't have to figure it out yourself.

I've put everything I know about React into a single course, to help you reach your goals in record time:

[**Introducing: The React Bootcamp**](https://www.thereactbootcamp.com)

**It’s the one course I wish I had when I started learning React.**

Click below to try the React Bootcamp for yourself:

[![Click to join the React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Click to get started*

