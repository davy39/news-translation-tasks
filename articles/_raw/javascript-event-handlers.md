---
title: JavaScript Event Handlers – How to Handle Events in JS
subtitle: ''
author: Shruti Kapoor
co_authors: []
series: null
date: '2020-09-21T17:09:50.000Z'
originalURL: https://freecodecamp.org/news/javascript-event-handlers
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/samuel-pereira-uf2nnANWa8Q-unsplash.jpg
tags:
- name: events
  slug: events
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "What are events?\nEvents are actions that happen when a user interacts\
  \ with the page - like clicking an element, typing in a field, or loading a page.\
  \ \nThe browser notifies the system that something has happened, and that it needs\
  \ to be handled. It ge..."
---

## What are events? 
Events are actions that happen when a user interacts with the page - like clicking an element, typing in a field, or loading a page. 

The browser notifies the system that something has happened, and that it needs to be handled. It gets handled by registering a function, called an `event handler`, that listens for a particular type of event. 

## What does it mean to "handle an event"? 
To put it in simple terms, consider this - let's assume you are interested in attending Web Development meetup events in your local community. 

To do this, you sign-up for a local meetup called "Women Who Code" and subscribe to notifications. This way, anytime a new meetup is scheduled, you get alerted. That is event handling! 

The "event" here is a new JS meetup. When a new meetup is posted, the website meetup.com catches this change, thereby "handling" this event. It then notifies you, thus taking an "action" on the event. 

In a browser, events are handled similarly. The browser detects a change, and alerts a function (event handler) that is listening to a particular event. These functions then perform the actions as desired. 

Let's look at an example of a `click` event handler:
 
```
<div class="buttons">
  <button>Press 1</button>
  <button>Press 2</button>
  <button>Press 3</button>
</div>
const buttonContainer = document.querySelector('.buttons');
console.log('buttonContainer', buttonContainer);

buttonContainer.addEventListener('click', event => {
  console.log(event.target.value)
})

```

## What are the different types of events?
An event can be triggered any time a user interacts with the page. These events could be a user scrolling through the page, clicking on an item, or loading a page. 

Here are some common events - `onclick` `dblclick` `mousedown` `mouseup` `mousemove` `keydown` `keyup` `touchmove` `touchstart` `touchend` `onload` `onfocus` `onblur` `onerror ` `onscroll` 

## Different phases of events - capture, target, bubble
When an event moves through the DOM - whether bubbling up or trickling down - it is called event propagation. The event propagates through the DOM tree. 

Events happen in two phases: the bubbling phase and the capturing phase. 

In capture phase, also called the trickling phase, the event "trickles down" to the element that caused the event. 

It starts from the root level element and handler, and then propagates down to the element. The capture phase is completed when the event reaches the `target`. 

In the bubble phase, the event is "bubbled" up to the DOM tree. It is first captured and handled by the innermost handler (the one that is closest to the element on which the event occurred). It then bubbles up (or propagates up) to the higher levels of DOM tree, further up to its parents, and then finally to its root. 

Her's a trick to help you remember this:
```
trickle down, bubble up
```

Here's an infographic from [quirksmode](https://www.quirksmode.org/js/events_order.html) that explains this very well: 
```
               / \
---------------| |-----------------
| element1     | |                |
|   -----------| |-----------     |
|   |element2  | |          |     |
|   -------------------------     |
|        Event BUBBLING           |
-----------------------------------

               | |
---------------| |-----------------
| element1     | |                |
|   -----------| |-----------     |
|   |element2  \ /          |     |
|   -------------------------     |
|        Event CAPTURING          |
-----------------------------------

```

One thing to note is that, whether you register an event handler in either phase, both phases ALWAYS happen. All events bubble by default. 

You can register event handlers for either phase, bubbling or capturing, by using the function `addEventListener(type, listener, useCapture)`. If `useCapture` is set to `false`, the event handler is in the bubbling phase. Otherwise it's in the capture phase. 

The order of the phases of the event depends on the browser.


To check which browser honors capture first, you can try the following code in JSfiddle: 
```html
<div id="child-one">
    <h1>
      Child One
    </h1>
  </div>

```

```javascript
const childOne = document.getElementById("child-one");

const childOneHandler = () => {
console.log('Captured on child one')
}

const childOneHandlerCatch = () => {
console.log('Captured on child one in capture phase')
}

childOne.addEventListener("click", childOneHandler); 
childOne.addEventListener("click", childOneHandlerCatch, true); 
```

In Firefox, Safari, and Chrome, the output is the following:
![Events in capture phase are fired first](https://github.com/shrutikapoor08/blogs/blob/master/JSByte/img/events_capture_order.png?raw=true) 
 
 
## How to listen to an event
There are two ways to listen to an event: 
1.  `addEventListener` 
2.  inline events, such as `onclick`

 ```
//addEventListener
document.getElementByTag('a').addEventListener('click', onClickHandler);

//inline using onclick
<a href="#" onclick="onClickHandler">Click me</a>
```

## Which is better - an inline event or `addEventListener`?

1. `addEventListener` gives you the ability to register unlimited event handlers.
2. `removeEventListener` can also be used to remove event handlers
3. The `useCapture` flag can be used to indicate whether an event needs to be handled in the capture phase or bundled phase.

 
## Code examples and live-action

You can try out these events in JSFiddle to play around with them. 

```html
<div id="wrapper-div">
  <div id="child-one">
    <h1>
      Child One
    </h1>
  </div>
  <div id="child-two" onclick="childTwoHandler">
    <h1>
      Child Two
    </h1>
  </div>

</div>

```

```javascript
const wrapperDiv = document.getElementById("wrapper-div");
const childOne = document.getElementById("child-one");
const childTwo = document.getElementById("child-two");

const childOneHandler = () => {
console.log('Captured on child one')
}

const childTwoHandler = () => {
console.log('Captured on child two')
}

const wrapperDivHandler = () => {
console.log('Captured on wrapper div')
}

const childOneHandlerCatch = () => {
console.log('Captured on child one in capture phase')
}

const childTwoHandlerCatch = () => {
console.log('Captured on child two in capture phase')
}

const wrapperDivHandlerCatch = () => {
console.log('Captured on wrapper div in capture phase')
}


childOne.addEventListener("click", childOneHandler); 
childTwo.addEventListener("click", childTwoHandler); 
wrapperDiv.addEventListener("click", wrapperDivHandler); 

childOne.addEventListener("click", childOneHandlerCatch, true); 
childTwo.addEventListener("click", childTwoHandlerCatch, true); 
wrapperDiv.addEventListener("click", wrapperDivHandlerCatch, true); 
```


## TL;DR
Event phases are capture (DOM -> target), bubble (target-> DOM) and target. 
Events can be listened for by using `addEventListener` or inline methods such as `onclick`. 

```
    addEventListener can add multiple events, whereas with onclick this cannot be done.
    onclick can be added as an HTML attribute, whereas an addEventListener can only be added within <script> elements.
    addEventListener can take a third argument which can stop the event propagation.

```

## Futher reading 
https://www.quirksmode.org/js/events_order.html
https://jsfiddle.net/r2bc6axg/
https://stackoverflow.com/questions/6348494/addeventlistener-vs-onclick
https://www.w3.org/wiki/HTML/Attributes/_Global#Event-handler_Attributes


To keep up with more short tutorials like this, [sign up for my newsletter](https://tinyletter.com/shrutikapoor) or [follow me on Twitter](https://twitter.com/shrutikapoor08)


