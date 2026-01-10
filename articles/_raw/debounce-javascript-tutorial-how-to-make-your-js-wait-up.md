---
title: Debounce JavaScript – How to Make your JS Wait Up
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-03T19:01:55.000Z'
originalURL: https://freecodecamp.org/news/debounce-javascript-tutorial-how-to-make-your-js-wait-up
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c996c740569d1a4ca1fa3.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'By Adeel Imran

  Debounce methods do not execute when invoked. Instead, they wait for a predetermined
  time before executing. If the same method is called again, the previous is cancelled
  and the timer restarts.

  Here is a short video walk through in whi...'
---

By Adeel Imran

Debounce methods do not execute when invoked. Instead, they wait for a predetermined time before executing. If the same method is called again, the previous is cancelled and the timer restarts.

Here is a short video walk through in which I make a debounce method:

%[https://youtu.be/NfYIiKRZTaU]

And here's the source code of the video tutorial:

%[https://codepen.io/adeelibr/pen/LYNPYmb?editors=1011]

Let's look at the code in more detail now.

Assume you have a button called like this:

```html
<button id="myBtn">Click me</button>
```

And in your JS file you have something like this:

```js
document.getElementById('myBtn').addEventListener('click', () => {
  console.log('clicked');
})
```

Every time you click on your button, you would see a message in your console saying `clicked`.

Let's add a debounce method to our `click` event listener here:

```js
document.getElementById('myBtn').addEventListener('click', debouce(() => {
  console.log('click');
}, 2000))
```

The debounce method here takes in two arguments, `callback` & `wait`. `callback` is the function you want to execute, while `wait` is the configurable time period delay after which you want your `callback` to be executed.

Here our `callback` method simply is `console.log('click');` and the `wait` is `2000 milliseconds`.

So given this debounce method, which takes in two parameters `callback` & `wait`, let's define `debounce`:

```js
function debounce(callback, wait) {
  let timerId;
  return (...args) => {
    clearTimeout(timerId);
    timerId = setTimeout(() => {
      callback(...args);
    }, wait);
  };
}
```

Function `debounce` takes in two parameters: the callback (which is the function we want to execute) and the `wait` period (after how much delay we want to execute our callback).

Inside the function, we simply return a function, which is the following:

```js
let timerId;
return (...args) => {
  clearTimeout(timerId);
  timerId = setTimeout(() => {
    callback(...args);
  }, wait);
};
```

What this function does is invoke our `callback` method after a certain period of time. And if during that period of time the same method is invoked again, the previous function is cancelled and the timer is reset and starts again.

And that is it! All you need to know about what debounce is.

Here is another bonus video on closures, because I used a `closure` inside my `debounce` function. 

%[https://youtu.be/-Q7oXxxw0-c]

Let me know on [twitter](https://twitter.com/adeelibr) if you were able to find the use of closure inside the debounce method.

Happy coding, everyone. 




