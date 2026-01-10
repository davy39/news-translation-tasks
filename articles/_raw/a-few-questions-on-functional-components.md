---
title: How to Use Functional Components in React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-03T08:11:26.000Z'
originalURL: https://freecodecamp.org/news/a-few-questions-on-functional-components
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/kelvyn-ornettte-sol-marte-86DcFWVMp0g-unsplash.jpg
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
seo_title: null
seo_desc: "By Cristian Salcescu\nHave you wondered how to create a component in React?\
  \ \nTo answer, it is as simple as creating a function returning an HTML-like syntax.\n\
  import React from 'react';\n\nfunction Counter({n}) {\n  return (\n    <div>{n}</div>\n\
  \  );\n}\n\nexp..."
---

By Cristian Salcescu

Have you wondered how to create a component in React? 

To answer, it is as simple as creating a function returning an HTML-like syntax.

```js
import React from 'react';

function Counter({n}) {
  return (
    <div>{n}</div>
  );
}

export default Counter;
```

Now let’s see what happened in the code above.  `Counter` is a function that transforms a number into HTML. And if you look more carefully, `Counter` is a pure function. That’s right, the kind of function that returns the result based on its inputs and has no side-effects. 

This explanation comes with a new question. What is a side-effect?

In short, a side-effect is any modification on the environment outside the function or any read information from the outside environment that can change.

You may have noticed that I used the [destructuring assignment syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment) in the parameter list to extract out the `n` input number. That’s because components take as input a single object called “props” that has all the properties sent to them. 

Here is how the `n` parameter can be set from any other component:

```js
<Counter n={1} />
```

In a sense, this syntax can be imagined like a function call `Counter({n: 1})`. Isn’t that right?

Let’s continue our journey.

Can functional components have state? As the component name suggested I want to store and change a counter. What if we just declare a variable holding a number inside the component? Will it work?

Let’s find out.

I will start by declaring the variable inside the functional component.

```js
import React from 'react';

function Counter() {
  let n = 0;
  return (
    <div>{n}</div>
  );
}

export default Counter;
```

Now let’s add the function that increments the number and logs it to the console. I will use the function as the event handler for the click event.

```js
import React from 'react';

function Counter() {
  let n = 0;
  
  function increment(){
    n = n + 1;
    console.log(n)
  }
  
  return (
      <div>
        <span>{n}</span>
        <button onClick={increment}>Increment </button>
      </div>
  );
}

export default Counter;
```

If we look at the console we see that the number is actually incremented, but that is not reflected on the screen. Any ideas?

You got it right … we need to change the number, but we need also to re-render it on the screen.

Here is where the utility function from [React Hooks](https://reactjs.org/docs/hooks-intro.html) comes into play. By the way, these utility functions are called hooks and they start with the word “use”. We are going to use one of them, [useState](https://reactjs.org/docs/hooks-state.html). I will log also the “re-render” text to console to see how many times the `Counter` function is actually called.

```js
import React, { useState } from 'react';

function Counter() {
  const [n, setN] = useState(0);
  
  console.log('re-render');
  
  function increment(){
    setN(n + 1);
    console.log(n)
  }
  
  return (
    <div>
        <span>{n}</span>
        <button onClick={increment}>Increment </button>
    </div>
  );
}

export default Counter;
```

Let’s read what `useState()` does.

**What does** `**useState**` **return?** It returns a pair of values: the current state and a function that updates it.

In our case `n` is the current state and `setN()` is the function that updates it. Have you checked the console to see how many times the “re-render” text is displayed? I will leave that for you to find out.

We can update the state not only by setting the new value but also by providing a function that returns the new value.

In our case, the function that provides the new value will be called `increment()`. As you see, `increment()` is a pure function.

```js
import React, { useState } from 'react';

function increment(n){
  return n + 1;
}

function Counter() {
  const [n, setN] = useState(0);
  
  return (
    <div>
        <span>{n}</span>
        <button 
         onClick={() => setN(increment)}>
           Increment 
        </button>
    </div>
  );
}

export default Counter;
```

To understand what `setN(increment)` does, let’s read the documentation.

_Passing an update function allows you to access the current state value inside the updater._

OK so `increment()` gets called with the current `n` state and it is used to compute the new state value.

# Final Thoughts

Let’s summarize what we found out.

In React we can simply define a component using a function that returns an HTML-like syntax.

React Hooks enables us to define state into such functional components.

And last but not least, we finally got rid of `this` pseudo-parameter in components. Maybe you have noticed that `this` becomes annoying by changing context when you don't expect it. No worries about that. We are not going to use `this` in functional components.

If you've made it this far you can also take a look at my books.

[**Discover Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE) was named one of the [**best Functional Programming books by BookAuthority**](https://bookauthority.org/books/best-functional-programming-books)**!**

For more on applying functional programming techniques to React take a look at **[Functional React](https://www.amazon.com/dp/B088FZQ1XN).**

Learn **functional React**, in a project-based way, with [**Functional Architecture with React and Redux**](https://read.amazon.com/kp/embed?asin=B0846NRJYR&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_o.hlEbDD02JB2)**.**

[Tweet me your feedback](https://twitter.com/cristi_salcescu).

