---
title: How to Use localStorage with React Hooks to Set and Get Items
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-02-22T14:53:30.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-localstorage-with-react-hooks-to-set-and-get-items
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/Yellow-and-Purple-Geometric-Covid-19-General-Facts-Twitter-Post.jpg
tags:
- name: localstorage
  slug: localstorage
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
seo_title: null
seo_desc: 'localStorage is a web storage object that allows JavaScript sites and apps
  to keep key-value pairs in a web browser with no expiration date.

  This means the data survives page refreshes (sessionStorage) and even browser restarts.
  This indicates that t...'
---

localStorage is a web storage object that allows JavaScript sites and apps to keep key-value pairs in a web browser with no expiration date.

This means the data survives page refreshes (sessionStorage) and even browser restarts. This indicates that the data stored in the browser will remain even when the browser window is closed.

In basic terms, local storage enables developers to store and retrieve data in the browser.

It is critical to understand, though, that using localStorage as a database for your project is not a good practice, since data will be lost when the user clears the cache, among other things.

Developers frequently use localStorage for adding a dark mode feature to an application, saving a to-do item, or persisting a user's form input values, among many other scenarios.

In this post, we'll take a look at how to use localStorage with React hooks to set and get items easily.

### Here's an interactive scrim about how to use localStorage with React Hooks to set and get items:

<iframe src="https://scrimba.com/scrim/crdLpnSG?embed=freecodecamp,mini-header" width="100%" height="480"></iframe>

## What are React Hooks?

React Hooks are JavaScript functions that you may import from the React package to add capabilities to your components.

Hooks allow React developers to use state and lifecycle methods within functional components. They also operate with existing code, making them easily adoptable into a codebase.

We will need two hooks in order to use localStorage with react hooks:

* `useState()` – The state of your application is guaranteed to change at some time. The `useState()` hook is a function that accepts one parameter, the initial state (which might be the value of a variable, an object, or any other sort of data in your component), and returns two values: the current state and a function that can be used to update the state.
    
* `useEffect()` – The Effect Hook is activated by default after the first render and each time the state is changed. As the names suggest, it is used to perform an effect each time the state changes. This hook is great for configuring listeners, retrieving data from the API, and deleting listeners before the component is removed from the DOM.
    

## How to Implement localStorage in React

localStorage provides us with access to a browser's storage object, which includes five methods:

* `setItem()`: This method is used to add a key and a value to localStorage.
    
* `getItem()`: This method is used to get an item from localStorage using the key.
    
* `removeItem()`: This technique is used to delete an item from localStorage based on its key.
    
* `clear()`: This technique is used to delete all instances of localStorage.
    
* `key()`: When you supply a number, it aids in the retrieval of a localStorage key.
    

In this post, we will only consider the most popular methods, which are the first two methods.

### How to Use the `setItem()` Method

By giving values to a key, this technique is used to store objects in localStorage. This value can be of any datatype, including text, integer, object, array, and so on.

It is vital to remember that in order to store data in localStorage, you must first stringify it with the `JSON.stringify()` function.

```bash
const [items, setItems] = useState([]);

useEffect(() => {
  localStorage.setItem('items', JSON.stringify(items));
}, [items]);
```

In the above code, we first created a state and assigned it an empty array (yours could be any other datatype). Second, we used `useEffect()` to add objects to localStorage whenever the value of our state changed. We did this by passing the state as the second argument.

Basically, this is the major code responsible for adding key-value pairs to localStorage:

```bash
localStorage.setItem('items', JSON.stringify(items));
```

Simply put, the preceding code names the key (items) and then assigns a value to it, but we had to first ensure that the data we were adding was a JSON string.

We use JSON.stringify() to convert a JSON object to JSON text stored in a string, which can then be transmitted to the web server.

![Image](https://paper-attachments.dropbox.com/s_EAEEAE9063B0CA7CBC6574F36123E82B36B6C1EC3724A86DA7C0B4C67C2DD652_1645380076460_explaining+useeffect+local+storage.jpg align="left")

*Structure of how hooks works with localstorage to set items*

How to Use the `getItem(`) Method

This method retrieves objects from localStorage. There are other methods to accomplish this with React, but we will use the `useEffect()` hook because it is the best one.

The `useEffect()` hook helps us fetch all items on first render, which means that when the component mounts or re-renders, it obtains all of our data from localStorage.

Note that this is why we passed in an empty second argument.

```bash
const [items, setItems] = useState([]);

useEffect(() => {
  const items = JSON.parse(localStorage.getItem('items'));
  if (items) {
   setItems(items);
  }
}, []);
```

It is important to remember that when we stored the data, we first converted it to a JSON string. This means that in order for us to now make use of it, we need to convert JSON string back to a JSON object. We do this with the `JSON.parse()` method.

![Image](https://paper-attachments.dropbox.com/s_EAEEAE9063B0CA7CBC6574F36123E82B36B6C1EC3724A86DA7C0B4C67C2DD652_1645369611908_explaining+useeffect+local+storage2.jpg align="left")

*Structure of how hooks works with localstorage to get items*

## Conclusion

In this article, we learnt how to use localStorage with React hooks, when to use it, and which hook to use.

If you want to see how this works in practice, you can get the source code for a simple to-do list app that makes use of localStorage and these hooks [here](https://github.com/olawanlejoel/Todo-App).

You can learn more about [state and props in this detailed article](https://joelolawanle.com/posts/understanding-state-props-react-key-differences-explained) written by me. You can also check all articles written by me in this [content repository](https://joelolawanle.com/contents).
