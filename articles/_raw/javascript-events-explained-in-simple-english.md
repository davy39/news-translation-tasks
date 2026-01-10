---
title: Browser Events Explained in Plain English
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-12-29T21:14:43.000Z'
originalURL: https://freecodecamp.org/news/javascript-events-explained-in-simple-english
coverImage: https://www.freecodecamp.org/news/content/images/2020/12/events.jpg
tags:
- name: beginners guide
  slug: beginners-guide
- name: events
  slug: events
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'What are browser events?

  An event refers to an action or occurrence that happens in the system you are programming.
  The system then notifies you about the event so that you can respond to it in some
  way if necessary.

  In this article, I will focus on ...'
---

## What are browser events?

An [event](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Events) refers to an action or occurrence that happens in the system you are programming. The system then notifies you about the event so that you can respond to it in some way if necessary.

In this article, I will focus on events in the context of web browsers. Essentially, an event is an indicator which shows that a certain action has taken place so that you can make an appropriate response.

To illustrate what I am talking about, let's imagine that you are standing at a pedestrian crossing waiting for traffic lights to change so that you can safely cross the road. The event is the change in traffic light which makes you subsequently take an action – which, in this case, is crossing the road.

Similarly in web development, we can take an action whenever an event we have interest in takes place.

Some of the common events you might have come across in web development include:

1. Mouse events
    

* `click`
    
* `dblclick`
    
* `mousemove`
    
* `mouseover`
    
* `mousewheel`
    
* `mouseout`
    
* `contextmenu`
    
* `mousedown`
    
* `mouseup`
    

2. Touch events
    

* `touchstart`
    
* `touchmove`
    
* `touchend`
    
* `touchcancel`
    

3. Keyboard events
    

* `keydown`
    
* `keypress`
    
* `keyup`
    

4. Form events
    

* `focus`
    
* `blur`
    
* `change`
    
* `submit`
    

5. Window events
    

* `scroll`
    
* `resize`
    
* `hashchange`
    
* `load`
    
* `unload`
    

For a complete list of events and the different categories they fall into, you can check out the [MDN documentation](https://developer.mozilla.org/en-US/docs/Web/Events). Some of the events listed are standard events in official specifications, while others are events used internally by specific browsers.

## What are event handlers?

As mentioned above, we monitor events so that whenever we receive a notification that the event has occurred, the program can take the appropriate action.

This action is often taken in functions called **event handlers** which are also referred to as **event listeners**. If an event occurs and the event handler is invoked, we say an event has been registered. This is illustrated in the code below.

If the button with `id` `btn` is clicked, the event handler is invoked and an alert with the text "Button has been clicked" is displayed. The `onclick` property has been assigned to a function which is the event handler. This is one of three ways of adding an event handler to a DOM element.

```js
const button = document.getElementById("btn");
button.onclick = function(){
   alert("Button has been clicked");
}
```

It is worth pointing out that **event handlers** are mostly declared as functions, but they can also be objects.

## How to assign event handlers

There are multiple ways of attaching event handlers to HTML elements. We'll discuss these methods, along with their pros and cons, below.

### Assign an event handler with an HTML attribute

This is the easiest way of attaching an event handler to HTML elements, though it is the least recommended. It involves using an inline HTML event attribute named `on<event>` whose value is the event handler. For example `onclick`, `onchange`, `onsubmit` and so on.

Take note that it is not uncommon to find HTML event attributes named `onClick`, `onChange` or `onSubmit` because HTML attributes are not case sensitive. Essentially it is syntactically correct to use `onclick`, `onClick` or `ONCLICK`. But it's common practice to leave it in lowercase.

```html
<button onclick = "alert('Hello world!')"> Click Me </button>
<button onclick = "(() => alert('Hello World!'))()"> Click Me Too </button>
<button onclick = "(function(){alert('Hello World!')})()"> And Me </button>
```

In the above example, JavaScript code has been literally assigned to the HTML event attribute.

Take note of the Immediately Invoked Function Expression (IIFE) format in the last two `button` elements. Though this appears easy and straightforward, assigning an inline HTML event attribute is inefficient and difficult to maintain.

Assume you have over 20 such buttons in your markup. It would be repetitive to write the same JavaScript code for each button. It is always better to write JavaScript in its own file so that you can easily use the same code for multiple HTML files.

Besides, you cannot have multiple lines of JavaScript code inline. Inline JavaScript code is considered an anti-pattern due to the aforementioned reasons. So try to avoid it unless you are trying out something quick.

### Declare an event handler in a `script` tag

Instead of doing the above, you can also declare the event handler in a `script` tag and invoke it inline as shown below.

```html
<!DOCTYPE html>
<html lang="en-US">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link rel="stylesheet" href="./index.css" type="text/css" />
    <script>
      function onClickHandler(){
         alert("Hello world!");
       }
    </script> 
  </head>
  <body>
    <div class="wrapper">
       <button onclick = "onClickHandler()"> Click me </button>
    </div>
  </body>
</html>
```

Notice, though, that simply assigning the function name as a value of the HTML event attribute like `onclick = "onClickHandler"` will not work. You need to invoke it as shown above, enclosing the invocation in quotes just like the value of any HTML attribute.

### Assign an event handler using the DOM property

Instead of using inline HTML event attribute illustrated above, you can also assign the event handler as the value of an event property on the DOM element. This is only possible inside a `script` tag or in a JavaScript file.

One limitation of this approach is that you cannot have multiple event handlers for the same event. If you have multiple handlers for the same event, as illustrated below, only the last one will be applied. The others will be overwritten.

```js
const button = document.getElementById("btn");
button.onclick = function(){
   alert("Button has been clicked");
}
// Only this is applied
button.onclick = function(){
   console.log("Button has been clicked");
}
```

If you want to remove the event listener from the `onclick` event, you can simply re-assign `button.onclick` to `null`.

```js
button.onclick = null
```

### How to improve the DOM method of adding event listeners

The above method of adding event listeners is preferable to using inline JavaScript. Still, it has a limitation of restricting an element to have only one event handler for each event.

For example you cannot apply multiple event handlers for a click event on an element.

To remedy this limitation, `addEventListener` and `removeEventListener` were introduced. This enables you to add multiple event handlers for the same event on the same element.

```js
const button = document.getElementById('btn');
button.addEventListener('click', () => {
  alert('Hello World');
})
button.addEventListener('click', () => {
  console.log('Hello World');
})
```

In the code above, an element with `id` `btn` is selected and then monitored for a `click` event by attaching two event handlers. The first event handler will be invoked and an alert message of `Hello World` pops up. Subsequently `Hello World` will also be logged in the console.

As you might have noticed from the above examples, the function signature of `element.addEventListener` is:

```js
element.addEventListener(event, eventHandler, [optional parameter])
```

#### Parameters to the `addEventListener` method

1. **event**
    

The first parameter, `event` (which is a required parameter) is a string that specifies the name of the event. For example `"click"`, `"mouseover"`, `"mouseout"` and so on.

2. **eventHandler**
    

The second parameter, which like the first is also required, is a function which is invoked when the event occurs. An event object is passed as its first parameter. The event object depends on the type of event. For example, a `MouseEvent` object is passed for a click event.

3. **Optional parameter**
    

The third parameter, which is an optional parameter, is an object with the properties:

* `once`: Its value is a boolean. If `true`, the listener is removed after it triggers.
    
* `capture`: Its value is also a boolean. It sets the phase where it should handle the event, which is either in the bubbling or capturing phase. The default value is `false` , therefore the event is captured in the bubbling phase. You can read more about it [here](https://javascript.info/bubbling-and-capturing). For historical reasons, options can also be `true` or `false`.
    
* `passive`: Its value is also a boolean. If it is `true`, then the handler will not call `preventDefault()`. `preventDefault()` is a method of the event object.
    

Similarly if you want to stop monitoring the `click` event, you can use `element.removeEventListener`. But this only works if the event listener has been registered using `element.addEventListener`. The function signature is similar to that of `element.addEventListener`.

```js
element.removeEventListener(event, eventHandler, [options])
```

For us to use `element.removeEventListener` to remove an `event`, the function passed as second argument to `element.addEventListener` must be a named function when adding the event listener. This ensures that the same function can be passed to `element.removeEventListener` if we want to remove it.

It is also worth mentioning here that, if you passed the optional arguments to the event handler, then you must also pass the same optional arguments to the `removeEventListener`.

```js
const button = document.getElementById('btn');
button.removeEventListener('click', clickHandler)
```

## What are event objects?

An event handler has a parameter called **event object** which holds additional information about the event.

The information stored in the **event object** depends on the type of event. For example, the **event object** passed to a `click` event handler has a property called `target` which references the element from which the click event originated.

In the example below, if you click the element with `id` `btn`, `event.target` will reference it. All click event handlers are passed an **event object** with the `target` property. As already pointed out, different events have **event object** parameters which store different information.

```js
const button = document.getElementById("btn");
button.addEventListener("click", event => {
  console.log(event.target);
})
```

## The value of `this`

In an `event` handler, the value of `this` is the element on which the event handler is registered. Take note that the element on which the event handler is registered may not necessarily be the same as the element on which the event occurred.

For example in the code below, the event handler is registered on the wrapper. Normally, the value of `this` is the same as `event.currentTarget`. If you click the `button`, the value of `this` inside `onClickHandler` is the `div` not the `button` because it is the `div` on which the event handler is registered though the click originated from the button.

This is called `event propagation`. It is a very important concept which you can read about [here](https://www.sitepoint.com/event-bubbling-javascript/) if you are interested.

```html
<!DOCTYPE html>
<html lang="en-US">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link rel="stylesheet" href="./index.css" type="text/css" />
    <script>
      function onClickHandler(){
         console.log(this)
         alert("Hello world!");
       }
       const wrapper = document.querySelector(".wrapper");
       wrapper.addEventListener("click", onClickHandler);
    </script> 
  </head>
  <body>
    <div class="wrapper">
       <button> Click me </button>
    </div>
  </body>
</html>
```

## Conclusion

In this article we looked at:

* Browser events and what they are
    
* Different ways of adding event handlers to DOM elements
    
* Event object parameters to event handlers
    
* The value of `this` in an event handler
