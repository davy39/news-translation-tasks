---
title: How to Create Infinite Scrolling in React Using the Intersection Observer API
subtitle: ''
author: Kunal Nalawade
co_authors: []
series: null
date: '2024-07-01T09:24:18.000Z'
originalURL: https://freecodecamp.org/news/infinite-scrolling-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/photo-1563986768494-4dee2763ff3f.jpeg
tags:
- name: React
  slug: react
seo_title: null
seo_desc: 'Hi fellow developers! Have you ever wondered how social media apps like
  Facebook and Instagram keep you scrolling endlessly through your feed?

  This user experience, designed to load new content on demand, uses a technique called
  infinite scrolling. T...'
---

Hi fellow developers! Have you ever wondered how social media apps like Facebook and Instagram keep you scrolling endlessly through your feed?

This user experience, designed to load new content on demand, uses a technique called infinite scrolling. This helps keep you hooked to these apps for hours.

Traditionally, these features would have you click "Next Page" to display new content. However, infinite scrolling reduces the load on the server by fetching less data at a time and thus, provides a much more engaging user experience.

In this post, we are going to implement the same feature in JavaScript. We'll use the Intersection Observer API to load data on demand, as the user is scrolling. We'll create a simple React application that displays posts similar to a social media feed.

## How to Set Up the React App

Run `create-react-app` in your terminal or use a [modern built tool like Vite](https://www.freecodecamp.org/news/get-started-with-vite/) to create your React app. Remove the existing boilerplate code. There is no need to install any additional dependencies. Run `npm start` command to start the project.

You can find the complete code of this tutorial on [GitHub](https://github.com/KunalN25/my-tutorials/tree/main/javascript-and-react/infinite-scroll-js). Let's get started.

## How to Create the Data Fetching Function

Create a separate file called `services.js` and write the following data fetching function.

We'll use the `/posts` API from [JSONPlaceholder](https://jsonplaceholder.typicode.com) to get our data.

```js
export const fetchPosts = async (page, limit) => {
  const response = await fetch(
    `https://jsonplaceholder.typicode.com/posts?_page=${page}&_limit=${limit}`
  );
  const data = await response.json();
  return data;
};
```

Here, we have passed two params to the API:

* `page` indicates the part of data that is called. This increases each time the user scrolls and loads new data.
    
* `limit` indicates the amount of data that is called at a time. For infinite scrolling, we call just enough data that can be displayed on a single page.
    

## How to Build the Infinite Scroll Component

Let's create a component `PostsList` for displaying a list of posts with infinite scrolling.

Let's create our state variables, fetch the data, and display it:

```js
const PostsList = () => {
  const [posts, setPosts] = useState([]);
  const [page, setPage] = useState(1);
  const [loading, setLoading] = useState(false);

  return (
    <div>
      <h1>Your Feed</h1>
      <ul>
        {posts.map((post, index) => (
          <li
            key={post.id}
          >
            <h2>{post.title}</h2>
            <p>{post.body}</p>
          </li>
        ))}
      </ul>
      {loading && <p>Loading...</p>}

    </div>
  );
};
```

Here, we have defined the state variables for posts, page number and loading state. Note that the page number does not mean that we are adding pagination. It's just a parameter to load the next set of data.

Now, let's call our API with the current page number and set the loading states:

```js
const loadMorePosts = async () => {
    setLoading(true);
    const newPosts = await fetchPosts(page, 10);
    setPosts((prevPosts) => [...prevPosts, ...newPosts]);
    setLoading(false);
  };

  useEffect(() => {
    loadMorePosts();
  }, [page]);
```

Until now, we have fetched the initial 10 posts on first load of the page. We want to load more data as the user scrolls down the page.

Next, we'll use the Intersection Observer API to detect when additional data should be loaded.

Before using it, let's first understand what this API is.

## What is the Intersection Observer API?

The Intersection Observer API is a web API that allows you to asynchronously observe changes in the intersection of a target element with an ancestor element or the viewport.

In simpler terms, it enables you to detect when an element enters or exits in an area of another DOM element or the viewport. Using Intersection Observer provides us with following advantages:

* Reduces the need for attaching event listeners to every scroll event.
    
* Removes the need for manual calculations of the element's position and their event listeners, thus simplifying your code.
    
* Efficient for observing multiple events compared to scroll or resize event listeners.
    

Go through the [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API) to understand more about Intersection Observer.

## How to Use the Intersection Observer API

To use this API, we'll need to create an observer object.

Here's how you create an observer object:

```python
const observer = new IntersectionObserver(callback, options);
```

* `callback` is a function called when the observed element's visibility changes. This function takes two arguments: `entries` and the `observer` object itself. Each object in `entries` array is an `IntersectionObserverEntry` object that contains information about the observed element's intersection status.
    
* `options` is an optional argument to further configure the Observer.
    

How do we use this in our application? We'll define observer object as a ref:

```js
  const observer = useRef();
```

Now, to set this observer object on an element and to detect whether that element is intersecting with the viewport, we use the following function, which is a callback ref:

```python
const lastPostElementRef = useCallback(
    (node) => {
      if (loading) return;
      if (observer.current) observer.current.disconnect();

      observer.current = new IntersectionObserver((entries) => {
        if (entries[0].isIntersecting) {
          setPage((prevPage) => prevPage + 1); // trigger loading of new posts by chaging page no
        }
      });

      if (node) observer.current.observe(node);
    },
    [loading]
  );
```

Let's understand how this function works:

* We check if the data is still loading. If it is, then we do not execute the logic.
    
* To refer to the `observer` object, we use the ref's `current` property.
    
* If an element is already being observed, then disconnect it and create a new Observer that changes the page number, thus triggering the API call if the observed element intersects with the viewport.
    
* Since we are only observing one element at a time (such as the last element of the page) the size of `entries` is one.
    
* This new Observer will now watch the current element to which the ref is attached to, which is the last element on the page.
    

Since we only want to observe the last element on the page, we add this ref according to following condition:

```python
{posts.map((post, index) => (
          <li
            key={post.id}
            ref={posts.length === index + 1 ? lastPostElementRef : null}
          >
            ...
          </li>
        ))}
```

Now, why are we using callback refs instead of the `observer` ref itself?

A ref gives us a direct reference to the element and sets the value of the ref object directly. It works well for elements that do not need to change reference dynamically.

A callback ref offers more control over the ref and can handle dynamic changes to reference more effectively. It is a function called with the element's instance, or its DOM Node when the component mounts and with null if it unmounts.

In our case, our reference changes dynamically since our last element gets updated as more data is loaded. We are also able to write some logic to observe and disconnect from a node, while setting our ref object.

We'll also wrap the `lastPostElementRef` function inside a `useCallback` hook to avoid it getting re-created on every re-render. We'll only create this function if the loading state changes when it's time to execute the function.

Run your app with `npm start`, go to `http://localhost:3000`, and open the Network Tab. As you scroll down, you'll see new API requests being made as you scroll down the page.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/image-101.png align="left")

*API requests for each new page*

You can find the complete code on [GitHub](https://github.com/KunalN25/my-tutorials/tree/main/javascript-and-react/infinite-scroll-js) and similar tutorials in JavaScript and React.

## Conclusion

When you implement infinite scrolling in your application, it provides a seamless and engaging user experience similar to what you see on popular social media apps. Instead of clicking through pages, users can effortlessly scroll through the content that loads dynamically.

In our example, we created a mock social media feed that loaded more content as the user scrolls down. We used the Intersection Observer API to detect the position of the last element according to which we loaded more data. It simplified our code and removed the need for attaching multiple event listeners.

I hope this helps you create similar features in your next web project and enables you to provide an engaging user experience. Please share your thoughts and feedback. Thank you!
