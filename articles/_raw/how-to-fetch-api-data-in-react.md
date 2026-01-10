---
title: How to Fetch API Data in React
subtitle: ''
author: Ijeoma Igboagu
co_authors: []
series: null
date: '2023-12-14T10:18:47.000Z'
originalURL: https://freecodecamp.org/news/how-to-fetch-api-data-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/Effective-Ways-for-Retrieving-API-Data-in-React-and-Python--1-.png
tags:
- name: api
  slug: api
- name: React
  slug: react
seo_title: null
seo_desc: 'When developing applications, you often need to get data from an API. This
  lets you deliver dynamic and often-updated content within your application.

  You''ll want to retrieve this data as you may need to interact with external services,
  communicate w...'
---

When developing applications, you often need to get data from an API. This lets you deliver dynamic and often-updated content within your application.

You'll want to retrieve this data as you may need to interact with external services, communicate with a distant server, or access a database.

In this article, I'll show you different methods of fetching data using React as an example.

## Prerequisites

* Install [Node.js](https://nodejs.org/en)
* Ensure you have at least a basic understanding of [React.js](https://react.dev/).
* A text editor

## What is an API?

API stands for Application Programming Interface. It enables the exchange of information and functionality between different systems, such as between a website and a server or between different software applications.

You can think of an API as being like a restaurant waiter. You don't go inside the kitchen to prepare your meal when you dine at a restaurant. Rather, you inform the waiter of your preferences, and they will take your order to the kitchen team. The kitchen team prepares the food and returns it to the waiter, who then delivers it to your table.

An API functions as a waiter for software applications. It is a set of rules that lets one program ask another for something it needs. It serves as a bridge for software apps to communicate and interact.

### Why are APIs important in web development?

There are a few reasons why APIs are important in web development. Let's go over some of them below:

* Web applications need APIs to get data from various sources, like databases or websites.
* APIs are a scalable option for managing high data or request volumes.
* Developers use APIs to leverage existing features and services. This saves them from reinventing the wheel.
* They keep things safe by ensuring that only authorized individuals or programs can use them.
* An API makes a website or mobile app more enjoyable to use by integrating data.

## What is a Hypertext Transfer Protocol (HTTP) request?

When a web browser or a mobile app sends a message to a server, it's known as an `HTTP` request. A `HTTP` request involves asking the server for specific data or an action and getting a response. The server responds by interacting with web pages and services.

Using APIs in software development makes things more flexible and efficient. It also enhances security and enables different software systems to work well together.

### Types of HTTP Requests

We use various `HTTP` request methods, such as `get`, `post`, `put`, and `delete`, to get and store data in our database. But the most common requests made are the `get` and `post` requests.

Let's discuss the meaning of these `HTTP` request methods:

* **GET:** This method retrieves data from a specific endpoint. Think of it as asking for information.
* **POST:** This method sends data to a specific endpoint. For example, you can send a message or submit a form. The information will be added to the database.
* **PUT:** This method is used to update a record or data value at a designated endpoint. You're making changes to existing information.
* **DELETE:** This method erases data from a specific endpoint. It's like discarding unnecessary things.

One widely adopted way of checking APIs is through the browser.

![Getting a response from an API](https://www.freecodecamp.org/news/content/images/2023/12/image-35.png)
_Getting a response from an API_

To learn more ways to get data, check out this article: [Getting Started with Application Programming Interfaces (APIs)](https://ijaycent.hashnode.dev/getting-started-with-application-programming-interface-api).

## How to Fetch Data in React

There are various ways to fetch data in React. Before we begin, let’s start by writing some React boilerplate code or by creating a template in our editor.

Here's the command to do that:

```js
npx create-react-app ./ or npx create-vite@latest ./
```

![creating template for our project](https://www.freecodecamp.org/news/content/images/2023/12/image-36.png)
_creating template for our project_

After this, type the following command:

```js
npm run dev
```

This will start the development server.

In the image above, you'll notice that I added a period (.) immediately following the command.

This is a convenient shorthand for creating the template within the current directory.

## Different Ways to Fetch Data in React

### 1. Use the stale-while-revalidate (SWR) method

This method is used to fetch data from a server and is used in React. It manages any issues that may arise when obtaining the data and helps you manage its storage. `SWR` includes `useState()` and `useEffect()`, so  there is no need to import them.

#### The advantages of SWR

1. `SWR` speeds up your app's loading time by showing older data while fetching the latest information.
2. It reduces the server burden by minimizing the number of requests.
3. Even if there is a bad connection, or no connection at all, SWR can still display previously fetched data.
4. SWR handles data acquisition and maintenance without the use of sophisticated coding.
5. It knows what to do if something goes wrong while gathering data.
6. You can change how SWR operates to better suit your app.
7. It provides a consistent approach to collecting and saving data across your app.

#### How to use `SWR` to get data

* In your application, create a file.
* Then install the package [SWR](https://swr.vercel.app/) into your application with the following command:

```js
npm i swr
```

* Import `useSWR`, which is a hook that has both `useState()` and `useEffect()`, into your application.
* Then define a constant variable on top called `fetcher` and assign it a function. 

This function is capable of receiving any number of arguments, denoted by the `...args` syntax.

The function looks like this:  
`const fetcher = (...args) => fetch(...args).then(res => res.json())`

Here is how then`Swr.jsx` should look like:

```javascript
import useSWR from 'swr';

// Import useSWR from swr package

// created function to handle API request
const fetcher = (...args) => fetch(...args).then((res) => res.json());

const Swr = () => {
  const {
    data: countries,
    error,
    isValidating,
  } = useSWR('https://restcountries.com/v2/all', fetcher);

  // Handles error and loading state
  if (error) return <div className='failed'>failed to load</div>;
  if (isValidating) return <div className="Loading">Loading...</div>;

  return (
    <div>
      {countries &&
        countries.map((country, index) => (
          <img key={index} src={country.flags.png} alt='flag' width={100} />
        ))}
    </div>
  );
};

export default Swr;

```

Let's see what's going on in the above code:

* The first thing we did was import the `SWR` library.
* Next, we defined a function to handle the API request.
* In return, we used the `map()` method to iterate through the list of nations.
* We put a `&&` line to ensure that if there are no issues and the data has been correctly received (meaning the `countries` variable is not null or undefined), it will proceed to map over the data and show an `image` element for each nation.
* Finally, we exported the component to the application's root `App.jsx` or `Index.jsx` so it could be viewed in the browser.

Here's the result:

![Using Swr](https://www.freecodecamp.org/news/content/images/2023/12/chrome_0YIvgfhfCl.gif)
_The result of using Swr_

### 2. Use the JavaScript `Fetch()` method

The `fetch()` method is well-known for retrieving data from APIs. It is recognized as the simplest and most used approach. 

#### The advantages of using the `fetch()` method

1. The `fetch()` method makes it simple to get information from the internet using JavaScript.
2. It lets you send extra details to the server, like who you are or what kind of data you want.
3. It's designed to work well in most of the newer web browsers.
4. The `fetch()` method supports different `HTTP` methods. These methods include get, post, put, and delete. They give you flexibility in interacting with APIs.
5. The `fetch()` method is a native JavaScript method. You can use it without any external libraries or dependencies. This makes it lightweight and efficient.

#### How to use `fetch()` to get data

* In your application, create a file.
* Then import `useState()` for [state management in React.](https://ijaycent.hashnode.dev/simplify-your-react-programming-effortlessly-with-these-8-amazing-hooks)
* Next, import `[useEffect](https://www.freecodecamp.org/news/react-useeffect-absolute-beginners/)()`, as it will make the data from the API render.

Here is how the `Fetch.jsx` should look like:

```javascript

import { useState, useEffect } from 'react';
const Fetch = () => {
  const [photos, setPhotos] = useState([]);
  useEffect(() => {
    fetch('https://jsonplaceholder.typicode.com/photos')
      .then((res) => {
        return res.json();
      })
      .then((data) => {
        console.log(data);
        setPhotos(data);
      });
  }, []);
  return (
    <div>
      
      {photos.map((photo) => (
        <img key={photo.id} src={photo.url} alt={photo.title} width={100} />
      ))}
    </div>
  );
};
export default Fetch;
```

Inside `useEffect()`, we fetch our data by sending a request with the API key. The response comes back in JSON (JavaScript Object Notation).

In the return statement, we process the received photos by utilizing a [`map()`](https://www.w3schools.com/jsref/jsref_map.asp) function to iterate through each item.

In our specific scenario, we are only interested in the photos. We render them in the browser by displaying them in the main file of the application, or root. The main file could be `App.jsx` or `Index.js`.

Here is how the `App.jsx` file looks:

![Image](https://www.freecodecamp.org/news/content/images/2023/12/image-38.png)
_The root of the application_

And here's the result:

![Image](https://www.freecodecamp.org/news/content/images/2023/12/image-39.png)
_using fetch()_

### 3. Use the `React Query` library

`React Query`, also known as `TanStack Query`, is useful for managing data in React applications. The difference between the two names is  the version.

Using React Query is easy and makes handling data in your app feel almost automatic, like it's taking care of things for you. For instance, fetching, caching, synchronizing, and updating server states in your applications.

#### Advantages of the `React Query` method

1. The data retrieved from APIs is cached by `React Query`. You can retrieve the same data from the cache again. This saves time by avoiding a new network request.
2. The program can automatically re-fetch data when specific conditions are met. These conditions include regaining focus or a set time passing.
3. `React Query` has optimistic updates that can update the UI. It shows the expected outcome of a mutation without server confirmation. A smoother user experience is achieved as a result.
4. It is made to work with React, making use of its component-based architecture to enable smooth integration.
5. `React Query` includes DevTools that offer insights into query, mutation, and caching state. These tools help with debugging and optimizing performance.

#### How to use `React Query` to get data

To begin, use this command to install the React-Query library (TanStack Query) into your application:

```js
npm i @tanstack/react-query
```

To make things work, use `QueryClientProvider` from `@tanstack/react-query`.

Wrap your application, which is the `Main.jsx` component, with it and pass `queryClient` as a prop. It comes automatically from the initialized `QueryClient`.

Here is how the [`Main.jsx`](https://www.freecodecamp.org/news/p/2cdb9f65-0c70-4a9c-832b-b073c0a83856/Main.jsx) file should look like:

```javascript
import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';

const queryClient = new QueryClient();

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <QueryClientProvider client={queryClient}>
      <App />
    </QueryClientProvider>
  </React.StrictMode>
)
```

Now that we have done this, we can fetch the data:

* In your application, create a file. 
* Import  the hook from `@tanstack/react-query` at the top of your file:

```js
import { useQuery } from '@tanstack/react-query';
```

* The `useQuery hook` is defined with two crucial parameters in object form. These parameters are `queryFn` and `queryKey`.
* `queryFn` handles fetching data from the endpoint.
* `queryKey` serves as the unique identifier for the data obtained.

As mentioned earlier, `React Query` simplifies and manages loading states and errors. You don't need a separate `useState() hook`.

```javascript
import { useQuery } from '@tanstack/react-query';
const Query = () => {
  const { data: comments, isLoading, error } = useQuery({
    queryFn: () =>
      fetch('https://jsonplaceholder.typicode.com/comments?_limit=10').then(
        (res) => res.json()
      ),
    queryKey: ['comments'],
  });
  
  // Show a loading message while data is fetching
  if (isLoading) {
    return <h2>Loading...</h2>;
  }
  
  // to handle error
  if (error) {
    return <div className="error">Error: error fetching</div>
  }
  
  return (
    <div>
      <h1 className='title'>Email address of users</h1>
      {comments.map((comment) => (
        <h2 key={comment.id} className="users">
          {comment.id}.  
            {comment.email}
        </h2>
      ))}
    </div>
  );
};
export default Query;
```

Here's the result:

![The result from the endpoint](https://www.freecodecamp.org/news/content/images/2023/12/chrome_bj4mya9YSt-1.gif)
_The result from the endpoint_

  
As previously mentioned, `useQuery()` manages the loading and error states as long as it's defined. 

When your internet service is bad, the browser may show these conditions because it couldn't get the data.

Here's an example:

![Loading and Error state](https://www.freecodecamp.org/news/content/images/2023/12/chrome_iPqmAfOUXF.gif)
_Loading and Error state_

### 4. Use the `Axios` Library

Axios is a third library package that we can add to our program to retrieve information from an API. Because Axios is used in both web browsers and server-side JavaScript, it is useful for a wide range of tasks.

#### Advantages of the `Axios` Library

1. Axios is simple and easy to understand. It's a clear and straightforward way to get data from an API.
2. It's designed to work well in most of the newer web browsers.
3. You don't have to add anything extra to your code to use Axios. It's ready to go as part of JavaScript.

#### How to use Axios Library to get data

* In your application, create a file.
* Install the package [`Axios`](https://www.npmjs.com/package/axios) into your application like this:

```js
npm i axios
```

* Import `Axios` library into your application.
* Import `useState()`, which [enables state management in React.](https://ijaycent.hashnode.dev/simplify-your-react-programming-effortlessly-with-these-8-amazing-hooks) 
* Then import `[useEffect](https://www.freecodecamp.org/news/react-useeffect-absolute-beginners/)()` which facilitates the rendering of data from the API.

Here is what the [`Axios.jsx`](https://www.freecodecamp.org/news/p/2cdb9f65-0c70-4a9c-832b-b073c0a83856/Axios.jsx) file should look like:

```javascript
import { useEffect, useState } from 'react'
import axios from 'axios'
const Axios = () => {
  const [meals, setMeals] = useState([])
  useEffect(() => {
    axios.get('https://www.themealdb.com/api/json/v1/1/random.php')
      .then((res) => {
        setMeals(res.data.meals);
      })
  }, [])
  
  return (
    <div>
      {meals.map((meal) => (
      <img key={meal.idMeal} src={meal.strMealThumb} alt={meal.strMeal} width={400}/>
      ))}
    </div>
```

Inside `useEffect()` we fetch our data by sending a request with the API key. The response comes back in JSON (JavaScript Object Notation).

We use a `map()` function in the return statement. The `map()` function helps us process the meals. It iterates through each piece of information.

In our specific scenario, we are only interested in the images of each meal.

To display them in the browser, we render them in the root of the application, which could be `App.jsx` or `Index.js`.

Here's the result:

![code](https://www.freecodecamp.org/news/content/images/2023/12/chrome_NB3f9HtpPL.gif)
_using axios library (Result)_

### 5. Use the `useFetch` custom hook from react-fetch-hook

A custom hook in React is a JavaScript function. It is reusable and leverages React's built-in hooks. The purpose is to encapsulate and share logic across multiple components. This promotes code modularity and maintainability.

A custom hook allows us to reuse the fetching logic in various components of our app.

In React, custom hooks are often named with a convention, such as `useFetch`. Typically, any custom hook follows a naming pattern that starts with the keyword `use`.

#### Advantages of a custom hook

1. Custom hooks make the reusability of logic across multiple components easy.
2. Custom hooks make the code readable, concise, and maintainable by abstracting complex logic.
3. Custom hooks allow you to test code independently, ensuring they work as expected before using them in components.
4. Custom hooks allow you to build bigger features with less code. They prevent complexity in your main code.

#### How to get data using a custom hook

* Open the terminal in your application. 
* Type this command to install the required package.

```js
npm install react-fetch-hook

```

* Once the installation is complete, navigate to the start of your application's file. Add the following line to import the `useFetch hook`:

```js
import useFetch from "react-fetch-hook";
```

Now, you can use the `useFetch` hook to interact with an API. 

1. Create variables to keep track of errors, loading states, and data by using destructuring.
2. In your application, make API calls using the `useFetch hook`. Update the variables.

Code example:

```javascript
import useFetch from "react-fetch-hook";

const UseFetch = () => {
  const { data: posts, isLoading, error } = useFetch('https://jsonplaceholder.typicode.com/posts');

  // Show a loading message while data is fetching
  if (isLoading) {
    return <h2>Loading...</h2>;
  }

  // Handle error
  if (error) {
    return <div className="error">Error: error fetching</div>;
  }

  return (
    <div>
      <h1 className='title'>Post of users</h1>
      {posts.map((post) => (
        <div key={post.id} className="card">
          <h2 className='users'>{post.title}</h2>
          <p>{post.body}</p>
        </div>
      ))}
    </div>
  );
};

```

Here's the result:

![Data called using the custom hook](https://www.freecodecamp.org/news/content/images/2023/12/chrome_Rx7VMtOqLZ.gif)
_Data called using the custom hook_

## 

## Conclusion

This article talks about different ways and tools to fetch API data in React.Understanding these methods will assist you in creating advanced applications. 

Utilizing React to construct dynamic applications and obtain data from APIs is vital. Many apps rely on data from APIs, so developers need to know the best and quickest ways to get that data. 

Whether you're a beginner or experienced developer, every method has its benefits. These benefits can improve your programming skills. They can also help you create reliable apps that use data.

If you found this tutorial helpful, please share it with other developers. They may also find it interesting. You can also stay updated on my latest projects by following me on [Twitter](https://https//twitter.com/ijaydimples) and [LinkedIn](https://www.linkedin.com/in/ijeoma-igboagu/).

Thank you for reading💖

### Resource

* [Public APIs Developers can use in their project](https://ijaycent.hashnode.dev/public-apis-developers-can-use-in-their-projects)

