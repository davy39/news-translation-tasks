---
title: How to Improve Your ReactJS Code – Tips for Code Readability and Performance
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-09-11T20:34:10.000Z'
originalURL: https://freecodecamp.org/news/improve-reactjs-code
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/Group-5.png
tags:
- name: Code Quality
  slug: code-quality
- name: React
  slug: react
- name: React
  slug: reactjs
seo_title: null
seo_desc: "By Neha sharma\nReactJS is one of the most popular JavaScript libraries\
  \ for building scalable and performant applications. \nWhen you're working on ReactJS\
  \ projects, whether they're large or small, you'll need to focus on code quality,\
  \ readability, mai..."
---

By Neha sharma

ReactJS is one of the most popular JavaScript libraries for building scalable and performant applications. 

When you're working on ReactJS projects, whether they're large or small, you'll need to focus on code quality, readability, maintainable, and scalability. 

Writing good code will also help you reduce PR comments from your teammates (and let's be honest – who doesn't like comments like LGTM :) ).

In this tutorial, you will learn how to improve your React code. I'll share my favorite tips along with code examples to show you how everything works. These will help you write maintainable, scalable, and readable code.

You should have basic familiarity with React to get the most out of this guide.

## 1. Use Constants

In JavaScript we can declare constants by using the `const` keyword. This helps us avoid re-declaring the same value. So constants are a great choice for storing API keys and other values like that.

Constants improve the scalability, readability, and internationalization of any React codebase.  

In every ReactJS project, you should avoid hard-coding strings (content) in your components. 

This will make your project more maintainable, scalable, and readable, as it isolates the UI, data, and content layers from each other.

Constants include:

* API keys
* URLs
* Content

Many websites support multiple languages, like English, French, Spanish, and so on. This is known as internationalization (or i18n for short). 

If you're enabling i18n features on your site, you should create separate constant files for your content – for example `en.js` and `fr.js`. Even if you don't have multiple language support or no i18n, it's still a good idea to keep your content outside your code in a constant file.

You can either name your constant file`[LANGUAGE_INITIAL].js`, or `constants.js`. These are the most common file names developers use for this purpose.

### How to create your constant file:

Constants are simply JavaScript objects with key/values. We start with declaring the object with a name which reflects the content it’s holding. As these are strings, we use quotes to wrap them. Before exporting the messages, do an `Object.freeze()` – this will avoid any accidental value change from outside any key. 

To use the constants, we need to import the file into the component file. Once imported, we can use the dot operator to access the keys:

```Javascript
// constants.js or en.js
const MESSAGES = { 
    'HEADING': 'welcome to the website",
    'ENTER_YOUR_NAME': 'Enter user name',
    'HOME': [{
        'HEADING': 'welcome to the home'
     }]
}

Object.freeze(MESSAGES);

export default MESSAGES;
```

```javaScript

// Using constants.js in component
import MESSAGES from '../constants/constants

const Home = () => {
    return(
        <p>{MESSAGES.HEADING}</h1>
    )
}

export default Home;

```

## 2. Use Helpers / Utils

While working on a ReactJS codebase it's crucial to identify the parts in the code which can be independent utils or helpers, instead of tightly coupling the components.

Helpers or utils are responsible for performing a task that can be used in multiple places and by multiple devs. Examples include a Date format, string formation, API call code, and DOM manipulation, to name a few.

### Why Use Helpers / Utils?

Every component should be responsible for only one job, which is something known as the “Single responsibility principle”. 

We should identify reusable functions and move them to utils for the following reasons:

1. It results in cleaner components and cleaner code
2. No tight coupling
3. Easily scalable functionality
4. Easy to maintain and debug
5. Better reusability
6. Components are now responsible only for the UI

```javascript
```
// dateUtils.js : Moved the formatDate to a seprate util file to have reusability

export function formatDate(date) {
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    return new Date(date).toLocaleDateString(undefined, options);
}
```

```react
// Updated Blog.jsx component after util
import React, { Component } from 'react';
import { formatDate } from './dateUtils'; 

const Blog = ({title, content, date}) => {
	return (
        <div>
            <h2>{title}</h2>
            <p>{content}</p>
            <p>Published on: {formatDate(date)}</p>
        </div>
    );
}
}

```

For example, in the above code, you can see that we have a `formatDate` function inside the component `Blog`. Here we can move the `formatDate` to utils. Why?

* `formatDate` is responsible for formatting the date, and not for publishing the date
* `formatDate` can be used by another component
* `formatDate` can have different formats based on the business requirements. For example, now we are passing a second argument based on this component requirement. If any new requirement comes up, the developer needs to re-write the component.

## 3. Learn How to Use Props 

To communicate between components in ReactJS, [we use `props`](https://www.freecodecamp.org/news/props-in-react/). But there are different ways to do that.

It is crucial to choose only one style to consume props in the component in your codebase. This will make the codebase consistent. There's more than one way to destructure props which is why you should pick only one for consistency and readability of your code.

Let's talk about the ways you can work with props in React.

### How to Use `Props`

In this approach we have to repeat `props` every time we are using `props`.

This approach is not a great way of consuming `props` because we are repeating props whenever we want to use them. Besides being repetitive, when it comes to creating nested props, it will require too much typing.

Your time as a developer is important, and we want to optimize the code wherever possible and not repeat things unless absolutely necessary.

In the below code example, you can see why this approach isn't the best. We have the `Input` component with `props` such as `type`, `placeholder`, `name`, and `changeHandler`. In the `return` section, we are repeating `props` with every `attribute` such as `props.type`.

```javascript
const Input = (props) => {
    return <input 
    type={props.type} 
    placeholder={props.placeholder} 
    name={props.name} 
    className="block p-2 my-2 text-black" 
    onChange={props.changeHandler}/>
}

export default Input;

```

### How to destructure props 

In the second way of working with `props`, we use the [JavaScript destructuring assignment](https://www.freecodecamp.org/news/destructuring-patterns-javascript-arrays-and-objects/). 

This is an improvement over the first approach, as in this one we won't repeat `props` whenever we're using props.

Here is an example of destructuring `props`. In the first code snippet, we are getting `type`, `placeholder`, `name`, and `changeHandler` from the `props` the first thing in the component.

```js
const { type, placeholder, name, changeHandler } = props
```

In the below code example, we can see the improvement in the code. We have `Input` component with `props`  but instead of repeating `props.name` we are destructing the props. It is a huge improvement in readability, and developer experience.

```javascript
const Input = (props) => {
    const { type, placeholder, name, changeHandler } = props;
    return <input 
    type={type} 
    placeholder={placeholder} 
    name={name} 
    className="block p-2 my-2 text-black" 
    onChange={changeHandler}/>
}

```

### How to destructure props in component arguments

This is my favourite method of destructuring props. Developers can see at the start of the component which props would get used in the component. We also don't have any repetition of the `props` keywords.

Compared with the last approach, it is:

* DRY (Don't Repeat Yourself): we are not repeating the props
* Readable: At the component's first line (definition), we know which props it is expecting. This improves the readability and clarity of the component.

In the below code, we can see that we are destructing `props` in the definition of the component. This makes readability way better. As now developers can look at the first line and understand how many and what all `props` are expected in this component.

```javascript
const Input = ({ type, placeholder, name, changeHandler }) => {
    return <input 
    type={type} 
    placeholder={placeholder} 
    name={name} 
    className="block p-2 my-2 text-black" 
    onChange={changeHandler}/>
}

```

## 4. Have One File for Each Component

In ReactJS, it is important to have one file per component. This helps make your code cleaner and more maintainable.

It also follows the [single responsibility principle](https://en.wikipedia.org/wiki/Single-responsibility_principle) I mentioned earlier.

It is tempting to have one file and write all the code inside it for isolation – but we should break it into smaller components.

In the below example, we have one file `Input.jsx` which has two components `Input` and `Icon`. We are using `Icon` in the `return` section of `Input`.

It looks like `Input` and `Icon` are related and its logical to group them into one file. But we should not do this, as it is not a scalable solution (and isn't reusable, either).

```javascript
// Don't do this:
import React from 'react';

// File name: Input.jsx
// This example shows how we are exporting 2 components from one file
// We should NOT do this
const Input = ({ type, placeholder, name, changeHandler }) => {
    return <>
    <input 
    type={type} 
    placeholder={placeholder} 
    name={name} 
    className="block p-2 my-2 text-black" 
    onChange={changeHandler}/>
    
    <Icon type="warning"/>
}
        <>

const Icon = ({ type, url}) => {
    return <img src={url} data-type={type} />
}

export {Input, Icon};

```

Instead, we should be making two separate components for `Input` and `Icon`, as shown below. This will help you reuse both components and scale them individually.

```javascript
// Do this instead:
// Input.jsx: create 2 separate files for Input and InputIcon
import React from 'react';

const Input = ({ type, placeholder, name, changeHandler }) => {
    return <input 
    type={type} 
    placeholder={placeholder} 
    name={name} 
    className="block p-2 my-2 text-black" 
    onChange={changeHandler}/>
}

export default Input;


```

## 5. Don't Use Inline Functions

It is common to write inline functions in JavaScript, but it is better to avoid adding them when possible.

You should keep your JSX separate from your logical code. Inline functions are not reusable, don't help with code abstraction, and are hard to test.

This is why you should always avoid inline functions.

In the below code snippet we have the `handleIncrement` function as an inline function on `button`.  It is not reusable, and it's tightly coupled with the component:

```javascript
// Don't do this:
import React, { useState } from 'react';

function CounterInline() {
  const [count, setCount] = useState(0);

  const handleIncrement = () => {
    setCount(count + 1);
  };

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={handleIncrement}>Increment</button> 
    </div>
  );
}

export default CounterInline;


```

Then how we can move away from inline functions? Let's look at how you can refactor of the above code.

In the below code, we can have `incrementCount` used on `button` and it is expecting two arguments. We have made the function here reusable:

```javascript
// Do this instead:
import React, { useState } from 'react';

// Standalone function for incrementing
function incrementCount(currentCount, setCount) {
  setCount(currentCount + 1);
}

const CounterStandalone = () => {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => incrementCount(count, setCount)}>Increment</button>
    </div>
  );
}

export default CounterStandalone;


```

## 6. Implement a 404 Component and Route 

While implementing routing in ReactJS we should add a 404 component.

When the user tries to access a page which doesn't exist, the status code from the server will be 404. As a front-end developer, it’s a good idea to show the user an error message to give them some context here.

React-router provides an easy way to display the error when the server returns a 404.  You'll need to create a component that should be rendered when the 404 status code returns from the server.

Whenever a user types in or reaches a route which is not found, the 404 page will show the error to the user, which is better user experience (rather than just seeing an unexplained "404").

Tip: In the component, add a link to the homepage of your website. This will help the user redirect to the homepage of your website.

```JavaScript
    <route path="*" component={<Error404/>} />
```

## 7. Fetch Data Progressively

In React applications, you'll often fetch data through APIs. 

Instead of fetching and creating the UI in one go, we should fetch the data on-demand – for example, on scrolling into view, on clicking of the pagination, and so on.

This will improve the performance of the application as well as the User Experience. 

There are a few packages that can help you implement lazy-loading. Lazy loading is a technique you can use to load the data on-demand or progressively as needed. Instead of showing whole API data on the screen at one time, it'll only show the data on-demand.

Here's how you can install the `react-lazyload` package:

```javascript
// install react-lazyload package
npm install react-lazyload
```

And here's the code:

```javascript
// Create a component - ItemList.jsx
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ItemList = () => {
  const [items, setItems] = useState([]);

  useEffect(() => {
    // Fetch data from your API here
    axios.get('https://example.com/api/items')
      .then(response => {
        setItems(response.data);
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  }, []);

  return (
    <div>
      <h2>Item List</h2>
      <ul>
        {items.map(item => (
          <li key={item.id}>
            {item.name}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ItemList;


```

```javascript
// App.js
import React, { lazy, Suspense } from 'react';
import LazyLoad from 'react-lazyload';

// Import the lazy-loaded component
const ItemList = lazy(() => import('./ItemList'));

function App() {
  return (
    <div>
      <h1>React LazyLoad with API Data Example</h1>

      {/* Use React LazyLoad to lazy-load the component */}
      <LazyLoad height={200}>
        <Suspense fallback={<div>Loading...</div>}>
          <ItemList />
        </Suspense>
      </LazyLoad>
    </div>
  );
}

export default App;


```

In the above example of code, have created a component which will make the API requests and render the API data `ItemList.jsx`. While using the `ItemList` in `App`, instead of rendering whole data in one go, we will use the `LazLoad` to load the component. 

As a result, component is loaded lazily when it's close to being visible in the viewport, and the data from the API will be displayed.

Some of the packages you can use for lazy loading are `react-lazyload`, `react-infinite-scroll-component` , and `react-paginate`.

## 8. Use Unique Values for Key Attributes

One of the reasons React is popular is because of its "virtual DOM".

The virtual DOM (VDOM) helps you optimize the process of updating the UI. 

React will only update nodes that get changed and not the whole DOM unless it is required. This is one of the secrets of the most performant apps. 

React needs a `key` attribute to identify to which node the change happened. This is why we should always use a unique value for `key`. 

A good example of how to do this is to add the `id` of every item.

Note: use index as a key only when your data is static, not re-ordering or filtered.

```javascript
// List.jsx
import React from 'react';

const List = ({ items }) => (

  return(<ul>
    {items.map((item, index) => (
      <li key={index}>{item}</li>
    ))}
  </ul>)
);

export default List;

```

```javascript
// App.jsx
import List from './List';

const App = () => {
  const items = ['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5'];

  return (
    <div>
      <h1>Simple List Example</h1>
      <List items={items} />
    </div>
  );
};

export default App;
```

In the above code example, we are creating a list by mapping over the data. In the `List` component we are assigning the `index` to the `key` attribute. This will be used by ReactJS under the hood to optimize the performance whenever any `li` will be updated or changed.

## 9. Use Types

Using tools with static type checking built in (like TypeScript) can help you avoid unnecessary bugs in your code.

It will also support your code with quality and type-checking. 

If you are someone who is just starting out learning about type checking, then you can start with `proptypes` and later learn TypeScript. 

JavaScript is not strictly typed, which means there's a higher possibility that you'll have unexpected bugs or type errors. 

For example, when we expect a prop to be a number, it could end up being a string which would cause an error.

So, strict types and TypeScript can help you avoid such unexpected bugs during development.

```javascript
import React from 'react';
import PropTypes from 'prop-types';

const UserCard = ({ name, age, email }) => {
  return (
    <div>
      <h2>User Card</h2>
      <p>Name: {name}</p>
      <p>Age: {age}</p>
      <p>Email: {email}</p>
    </div>
  );
};

// Define the prop types for the UserCard component
UserCard.propTypes = {
  name: PropTypes.string.isRequired, // A required string prop
  age: PropTypes.number.isRequired,  // A required number prop
  email: PropTypes.string,           // An optional string prop
};

```

```javascript
import UserCard from 'userCard';

const App = () => {
  return (
    <div>
      <h1>PropTypes Example</h1>
      <UserCard name="John Doe" age={30} email="john@example.com" />
    </div>
  );
};

export default App;
```

In the above code example, we have created a component `UserCard`. This component expects 3 props: name, age, and email. By using `proptypes` , we will declare two things for props – datatype (what would be the datatype of the props, for example string, number, and so on), and whether it's required or optional. 

While using the `UserCard` component, if anyone passes the wrong datatype or misses a required prop, then the code will throw an error and warn them to fix it. 

## 10. Use the `lazy()`  and `Suspense()` Functions

ReactJS uses the Webpack bundler (if you are using creat-react-app). 

Webpack takes care of bundling of the code, and performs functions like [tree shaking](https://www.freecodecamp.org/news/tree-shaking-es6-modules-in-webpack-2-1add6672f31b/). 

But the way React works is it downloads the whole code on the client side even if we don't need it. This is an expensive task. If your bundle size is big then it will impact the performance of your apps. 

A good way to avoid this is to lazy load the code on demand by using `lazy()`, which will let the routes get loaded when they're needed.

```javascript
const LazyComponent = lazy(() => import('./LazyComponent'));
```

While using `lazy()` we should also use `Suspense()`, as `lazy()` is an async way of loading the components. 

We don't want to show the user a blank screen until our route is done loading. `Suspense()` helps by showing a message while the component is loading.

```javascript
 <Suspense fallback={<div>Loading...</div>}>
        {/* The LazyComponent will only be loaded when needed */}
        <LazyComponent />
 </Suspense>
```

## Wrapping Up

Phew, we have reached the end. These tips are not just limited to large codebases but to projects of any size. 

At high level we learned about the following concepts:

1. Following the DRY principle
2. Following the Single Responsibility Principle
3. Creating a good user experience by loading the data progressively 
4. Improving readability
5. Improving the developer experience
6. Avoiding bugs at the development time
7. Improving performance

Happy Learning!

Don't be shy. Come and say hi! You can find me on [Twitter](https://twitter.com/hellonehha), [LinkedIn](https://www.linkedin.com/in/nehha/), and [YouTube](https://youtube.com/@hellonehha).

Want to see some calligraphy? Check my art on instagram.com/calligraphyzen.

