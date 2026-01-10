---
title: How to Handle Async Callbacks in JavaScript...Without Callbacks?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-01-04T23:38:48.000Z'
originalURL: https://freecodecamp.org/news/how-to-handle-async-callbacks-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/museums-victoria-TVe0IEdsVc8-unsplash.jpg
tags:
- name: asynchronous
  slug: asynchronous
- name: callbacks
  slug: callbacks
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "By Tobias Parent\nNoodling about on Discord today, the same question came\
  \ up a few times on a few different servers. I thought it was a great question,\
  \ and it seems my brain doesn't work quite the way others might expect. \nHere's\
  \ the question:\n\n\"So I ..."
---

By Tobias Parent

Noodling about on Discord today, the same question came up a few times on a few different servers. I thought it was a great question, and it seems my brain doesn't work quite the way others might expect. 

Here's the question:

> "So I have a `fetch` function, and I'm doing some `then` along with it to parse out the JSON data. I want to return that, but how can I? We can't `return` something from an asynchronous function call!"

That's a great question. There's a lot going on there. We have ways of handling this within React, quite easily: we can `useState` to create some stateful variable, we can run our `fetch` within a `useEffect` and load that stateful variable, and we can use _another_ `useEffect` to listen for that stateful variable to change. When the change happens, we can trigger our custom function and do some sort of side-effect with it.

With pure JavaScript, HTML, and CSS, it becomes a tad bit more tricky. For those who like to read the last page of the mystery novel before the rest, [this replit](https://replit.com/@TobiasParent/HandlingLateLoadEvents#script.js) is where we'll end up.

## An Ugly Beginning

Suppose we want to fetch some todos from a server, and when we've loaded them we want to update the DOM. We might need to reload them, or append to them later – we want things to happen if our asynchronous functions do some sort of update to our _state_.

And yet, I don't really know how I feel about that. When we have a block of code like this:

```js
const load = () => {
  fetch("https://jsonplaceholder.typicode.com/todos")
    .then(res => res.json())
    .then(jsonObj => {
      const todoContainer = document.querySelector(".todos-container");
      // now, take each todo, create its DOM, and poke it in.
      jsonObj.forEach( (todo)=>{
        const todoEl = document.createElement("div");
        todoEl.classList.add("todo");
        const todoTitle = document.createElement("h3");
        todoTitle.classList.add("todo-title");
        todoTitle.textContent=todo.title;

        const todoStatus = document.createElement("div");
        todoStatus.classList.add("todo-status");
        todoStatus.textContent = todo.done ? "Complete" : "Incomplete";

        todoEl.append(todoTitle, todoStatus);
        todoContainer.append(todoEl)
    })
}
```

We kind of _have_ to fill the DOM right there in the `.then()` block, because we can't really say "hey, when this is done, fire off this function." 

We could simply await each of the Promises, rather than chaining them like this, and simply return the result of the final parsing:

```js
const load = async () => {
  const result = await fetch("https://jsonplaceholder.typicode.com/todos")
  const jsonObj = await result.json();
  const todoContainer = document.querySelector(".todos-container");

  jsonObj.forEach( (todo)=>{
    const todoEl = document.createElement("div");
    todoEl.classList.add("todo");
    const todoTitle = document.createElement("h3");
    todoTitle.classList.add("todo-title");
    todoTitle.textContent=todo.title;

    const todoStatus = document.createElement("div");
    todoStatus.classList.add("todo-status");
    todoStatus.textContent = todo.done ? "Complete" : "Incomplete";

    todoEl.append(todoTitle, todoStatus);
    todoContainer.append(todoEl)
  })
  // here, if we wanted, we could even return that object:
  return jsonObj;
}

// later, we can do this:
const todos = await load();
// fills the DOM and assigns all the todos to that variable
```

Now that is better, our `load()` function can be used to not only put those elements into the DOM, but it returns the data to us. 

This is still not ideal, though – we are still having to fill that DOM when the result is loading, and we still have to wait for the loading to happen. We have no idea _when_ `todos` is going to be something. Eventually, it will be, but we don't know when.

## Callbacks, Anyone?

We do have the option of a callback function. It might be useful, instead of actually hard-coding the DOM construction stuff, to pass that off to something else. It makes the `load` function more abstract, as it isn't wired to a particular endpoint.

Let's see what that might look like:

```js
const load = async (apiEndpoint, callbackFn) => {
  const result = await fetch(apiEndpoint);
  if(!result.ok){
    throw new Error(`An error occurred: ${result.status}`)
  }
  // at this point, we have a good result:
  const jsonObj = await result.json();
  // run our callback function, passing in that object
  callbackFn(jsonObj)
}

// Let's use that. First, we'll make a callback function:
const todoHandler = (todos) => {
  const todoContainer = document.querySelector(".todos-container");

  todos.forEach( (todo)=>{
    const todoEl = document.createElement("div");
    todoEl.classList.add("todo");
    const todoTitle = document.createElement("h3");
    todoTitle.classList.add("todo-title");
    todoTitle.textContent=todo.title;

    const todoStatus = document.createElement("div");
    todoStatus.classList.add("todo-status");
    todoStatus.textContent = todo.done ? "Complete" : "Incomplete";

    todoEl.append(todoTitle, todoStatus);
    todoContainer.append(todoEl)
  })    
}

load("https://jsonplaceholder.typicode.com/todos", todoHandler);
```

That's nicer – we are now telling `load` what to load, and what to do when that fetch has completed. It works. And there isn't anything really _wrong_ with that. Still, it has some drawbacks. 

My callback is by no means complete. We aren't handling errors, we aren't really _gaining_ anything by this approach. We don't get the data out of the `load` function in any sense we can use, in a timely fashion.

And again, me being me, I wanted to try a different way.

## Callbacks Without Callbacks

Okay, that _is_ a little misleading. They're not callbacks. We are going to completely avoid _having_ callbacks at all. What will we have instead? Event listeners!

The DOM is all about communication. Events fire off all over the place – mouse events, keyboard events, gestures and media and window... The browser is a noisy place. 

But it is all _controlled_, it is all _intent-ful_ and it is all _well-formed_. Things are encapsulated nicely, completely self-contained, but they can communicate events up and down the DOM tree as needed. And we can leverage that, with the `CustomEvent` API.

Creating a `CustomEvent` is not really that difficult, simply provide the name of the event as a string, and the _payload_ – the information to be included in that event. Here's an example:

```js
const myShoutEvent = new CustomEvent('shout', {
  detail: {
    message: 'HELLO WORLD!!',
    timeSent: new Date() 
  }
})

// and later on, we can send that event:
someDomEl.dispatchEvent(myShoutEvent);
```

That's all there is to a custom event. We create the event, including custom `detail` data, and then we `dispatchEvent` on a given DOM node. When that event is fired on that DOM node, it joins the normal stream of communication, riding along on the bubbling and capturing phases just like any normal event – because it _is_ a normal event.

## How does this help us? 

What if we were to _listen_ for that custom event somewhere, and place the responsibility for handling that event (and its `detail`) with the receiver, rather than telling the `load` function what to do when we get that data?

With this approach, we don't really care _when_ the fetch completes its processing, we don't care about some returning value in some global variable – we simply tell the DOM node to dispatch an event... _and pass along the fetched data as `detail`_.

Let's start playing with this idea:

```js
const load = (apiEndpoint, elementToNotify, eventTitle) => {
  fetch(apiEndpoint)
    .then( result => result.json() )
    .then( data => {
       // here's where we do this: we want to create that custom event
       const customEvent = new CustomEvent(eventTitle, {
         detail: {
           data
         }
       });
       // now, we simply tell the element to do its thing:
      elementToNotify.dispatchEvent(customEvent)
     })
};
```

That's it. That's the whole shebang. We load some endpoint, we parse it, we wrap the data in a custom event object, and we throw it out into the DOM. 

The rest is outside of the concern of that `load` function. It doesn't _care_ about what the data looks like, it doesn't _care_ where it's coming from, it doesn't _return_ anything. It does this one thing – fetch data and then yell about it.

Now, with that in place, how might we wire that in from the other side?

```js
// a function to create the Todo element in the DOM...
const createTodo = ({id, title, completed}) => {
  const todoEl = document.createElement("div");
  todoEl.classList.add("todo");

  const todoTitle = document.createElement("h3");
  todoTitle.classList.add("todo-title");
  todoTitle.textContent=todo.title;

  const todoStatus = document.createElement("div");
  todoStatus.classList.add("todo-status");
  todoStatus.textContent = todo.done ? "Complete" : "Incomplete";

  todoEl.append(todoTitle, todoStatus);
    
  return todoEl;
}

// and when that load event gets fired, we want this to be
//  the event listener.
const handleLoad = (event)=>{
  // pull the data out of the custom event...
  const data = event.detail.data;
  // and create a new todo for each object
  data.forEach( todo => {
    event.target.append( createTodo(todo) )
  })
}

// finally, we wire in our custom event!
container.addEventListener("todo.load", handleLoad)
```

That wires up the `container` to listen for that custom `todo.load` event. When the event happens, it fires off and executes that `handleLoad` listener. 

It isn't doing anything particularly magic: it simply gets the `data` from that `event.detail` we create in the `load` function. Then the `handleLoad` calls the `createTodo` for each object in the `data`, creating our DOM node for each todo element.

Using this approach, we have nicely separated the data-fetching bits from the presentation bits. The only thing remaining is telling the one to talk to the other:

```js
// remember, the parameters we defined were:
// apiEndpoint: url,
// elementToNotify: HTMLDomNode,
// eventTitle: string
load("https://jsonplaceholder.typicode.com/todos", container, 'todo.load');
```

## To Recap

We started with an ugly spaghetti-code mess – fetching logic mixed in with parsing and presentation. No good. I mean, we all do it, we use it all the time, but it just feels sketchy. There is no clean separation, and there is no way of working with the data outside of that `.then()`.

Using `async/await`, we _can_ return that data, and we can use it outside the fetch if we need – but we have no real way of knowing when that data has been loaded. We can still process inline, loading the presentational layer in with the fetch, but that's no gain from the last.

Using callbacks, we can begin to separate – with a callback, we can load the data and, when the asynchronous operation is done, run the callback function. It does keep them nicely separated and it does pass the data into the callback as a parameter. It _is_ better than mixing the presentation inline, but we _can_ do something different.

And I mean that _different_ – using the `CustomEvent` API is no better or worse than using callbacks. Both have their strengths and weaknesses. I like the clean-ness of the `CustomEvent` system, I like that we can extend that out. Some examples:

* a Timer class, that fires off a `"timer.tick"` and `"timer.complete"` event. The parent/container of that Timer's DOM node can listen for those events, _firing asynchronously_, and respond appropriately, whether updating the displayed time or causing a reaction when the timer's done.
* our Todos – we could have the container listen for `"todo.load"`, `"todo.update"`, whatever custom events we like. We could handle updates by finding the relevant DOM node and updating its content, or removing all and replacing them on a load.

We are separating the model logic from the presentation logic _entirely_, and defining an interface between the two. Clean, clear, reliable and simple.

