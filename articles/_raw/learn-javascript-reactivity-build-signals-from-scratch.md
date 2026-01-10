---
title: 'Learn JavaScript Reactivity: How to Build Signals from Scratch'
subtitle: ''
author: Rahul gupta
co_authors: []
series: null
date: '2024-07-18T21:17:44.000Z'
originalURL: https://freecodecamp.org/news/learn-javascript-reactivity-build-signals-from-scratch
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1727437093214/d99314da-415e-4a4b-8d7e-f00aaf3db9a8.png
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'If you''re learning JavaScript, you may have heard the terms reactivity
  or signals. But perhaps you haven''t gotten to use them in practice yet. If so –
  or if you just want to learn more about these concepts – you''re in the right place.

  In this article...'
---

If you're learning JavaScript, you may have heard the terms reactivity or signals. But perhaps you haven't gotten to use them in practice yet. If so – or if you just want to learn more about these concepts – you're in the right place.

In this article, you'll learn what reactivity means, what signals are, and then you'll build your own implementation of Signals from scratch.

## What We'll Cover

* [What is Reactivity?](#heading-what-is-reactivity)
    
* [What are Signals?](#heading-what-are-signals)
    
* [How to Build Your Own Signals](#heading-how-to-build-your-own-signals)
    
* [Conclusion](#heading-conclusion)
    

## What is Reactivity?

Here's a generic definition for reactivity:

> "Reactivity is the way a system reacts to data changes."

At it's heart, reactivity in UI applications refers to changes in the UI in response to changes in the data.

Having an understanding of how Reactivity works behind the scenes gives you a deeper understanding of some of the common paradigms that you already use when developing web applications. But it also helps deepen your understanding of the frameworks / libraries you work with on a daily basis that use Reactivity under the hood.

Here are some common paradigms where reactivity comes into play behind the scenes, along with some examples:

* **React to data fetched from an API**: Show loading / error / success indicators based on the state of data being fetched.
    
* **Single data, multiple Reactive UI elements:** In an ecommerce website, when an item is added to a cart, it should be marked as added and the cart badge's count should also increment.
    
* **React to a task being completed**: Show a checkmark when a user is done uploading an image.
    
* **React to events**: Show a promotional banner when a user is at the bottom of the page.
    
* **Reactivity in CSS**: Recalculate the spacing based on the height of the component via `calc(--height)`.
    

Here are some of the popular frameworks / libraries and how they depend on Reactivity at their core:

**React** let's you save data in form of state via hooks like `useState` , anytime this state changes, the corresponding UI element where the state is used is also updated reactively.

Under the hood, React achieves this by re-constructing and comparing the Virtual DOM when some state updates so that it only updates the relevant part of the UI element on the screen.

**RxJS** uses observables to produce data and observers to consume that data, notifying them whenever new values are produced. You can [read more about this here.](https://rxjs.dev/guide/observable)

**Vue** uses objects and [proxies](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy) to provide reactivity via `ref()`. Proxy, in a nutshell, lets Vue intercept when an object's property is accessed or set, which is the basis of its reactivity system. [You can read more here](https://vuejs.org/guide/extras/reactivity-in-depth.html).

**SolidJS** uses *Signals* to achieve fine-grained reactivity. This means that it can update specific parts of the DOM when data changes, without the need of a virtual DOM.

## What are Signals?

Signals are an important concept in Reactivity within JavaScript. Signals can hold a value and then allow a piece of code to react to it when this value changes.

Signals allow you to manage the state in a more controlled manner. They also allow fine-grained reactivity where components can update selectively based on the specific state changes, rather than re-rendering entirely.

Different frameworks have their own implementations of Signals like I mentioned earlier (for example, Vue calls them `ref`, while [Angular](https://angular.io/guide/signals), [Preact](https://preactjs.com/guide/v10/signals/), [Qwik](https://qwik.builder.io/docs/components/state/#usesignal) call them signals) and they differ slightly in their implementations.

In this article, we'll try to rebuild signals from scratch as they exist within the [SolidJS](https://docs.solidjs.com/concepts/signals) framework.

### Signals in SolidJS

Let's start by understanding how signals work in SolidJS. Then we'll be recreating the same with just JavaScript.

`**createSignal**` is used to create a signal, takes `initialValue` as an argument, and returns a pair of `getter`s and `setter`s. Here's what this looks like:

```javascript
const [count, setCount] = createSignal(0);
        ^ Getter   ^ Setter
```

Here:

* `count()` is used to access the value in the signal
    
* `setCount(newValue)` is used to set a new value in the signal
    

The `**createEffect**` function allows arbitrary code ("side effects") to be reactive and re-run whenever its dependencies change. It accepts a callback function and re-executes this function whenever any signal dependencies accessed within the callback change.

Unlike [effects in React](https://react.dev/reference/react/useEffect#useeffect), there is no need to explicitly list dependencies in an array. **createEffect** automatically determines signal dependencies by tracking which signal getters are accessed within the callback.

```javascript
const [count, setCount] = createSignal(0);

// Runs once with value at this point in time
// Print 0
console.log(count());

createEffect(() => {
    // Prints 0
    // Prints 1
    console.log(count());
});


// Updates the count to 1
setCount(1);
```

In the above example, the first `console.log` is printed only once, as SolidJS runs everything just once, whereas the callback within the effect runs every time the "count" signal's value is changed.

## How to Build Your Own Signals

Let's try to re-build a simpler implementation of the above demonstrated SolidJS Signals by breaking it down:

* **Implement** `Signal` Class – which manages handling of a Pub-Sub mechanism to power `createSignal`
    
* **Implement** `**createSignal**` – uses the Signal class to implement this function, which should accept an initial value & returns getter & setters.
    
* **Implement** `createEffect` – runs the callback provided to it once, and re-runs it when a signal value changes
    

### Implement the `Signal` class

This class will use the Pub-Sub pattern, which means it should:

* Maintain a value and provide a getter to access this value
    
* Maintains a list of subscribers as an array and a method to subscribe
    
* Provides a setter to set a new value and communicate the updated value to all subscribers
    

```javascript
class Signal {
  constructor(value) {
    this.value = value;
    this.subscribers = [];
  }

  getValue() {
    return this.value;
  }

  setValue(newValue) {
    this.value = newValue;
    this.emit();
  }

  emit() {
    this.subscribers.forEach((subscriber) => subscriber(this.value));
  }

  subscribe(callback) {
    this.subscribers.push(callback);
  }
}
```

A use case for the above may look like this:

```javascript
const signal = new Signal(0);

// Subscriber callback is re-run by the class when value changes
signal.subscribe((value) => console.log(value));

// There can be as many subscribers
signa.subscribe(...);

// Updates the value within the class
// Emits the value to all subscribers
signal.setValue(1);
```

The `subscribe` method pushes callback functions provided within an array of `subscribers` while `setValue` calls the `emit` method which loops through those subscribers and runs each subscriber callback with the `newValue`.

### Implement the `createSignal` method

Let's try to use the above to implement a `createSignal` method which should:

* Accept an initial value as an argument
    
* Return an array of getter and setter methods
    

```javascript
export const createSignal = (value) => {
  const signal = new Signal(value);

  return [
    function value() {
      return signal.getValue();
    },
    function setValue(newVal) {
      signal.setValue(newVal);
    },
  ];
};

const [value, setValue] = createSignal(0);

// Logs 0
console.log(value());

setValue(1);

// Logs 1
console.log(value());
```

The above `createSignal` creates a new instance of the `Signal` class with the initial value provided to it.

It currently also returns a getter and setter which internally calls the respective getter and setter of the signal instance.

You'll notice that we're still writing `console.log(value())` twice manually when we want to access the latest `value()` as there are no subscriptions to the signal yet.

We'll achieve that with `createEffect`'s implementation next.

### Implement `createEffect`

Our `createEffect` should:

* Receive a callback as an argument
    
* Execute the callback once, immediately
    
* Subscribe to the signals used within the callback
    

```javascript
export const createEffect = (callback) => {    
  // Let's execute the callback
  callback();
    
  // Wait how do I subscribe?
};
```

So you might be wondering: how can I possibly know whether this callback uses a signal getter or not?

Short answer is, you can't. As `createEffect` is a generic method, it can't possibly know what signals are being used within the callback passed to it. It can only execute this callback with different arguments at the very best.

If we think differently, there is still a way this function can *communicate* with the code within the callback (getter).

Let's introduce a new variable, `effectCallback`, which is an intermediate variable used to communicate between the effect and signal getter method. This variable should hold the callback that an effect receives.

An effect registers a callback subscription based on signal's `getter` that has been accessed within it.

Let's modify our `createSignal` code to handle that:

```javascript
export const createSignal = (value) => {
  const signal = new Signal(value);

  return [
    function value() {
      // Subscribes the effectCallback if exists
      if (effectCallback) {
        signal.subscribe(effectCallback);
      }

      return signal.getValue();
    },
    function setValue(newVal) {
      signal.setValue(newVal);
    },
  ];
};
```

Let's see when we can set the `effectCallback`. We know that `createEffect` should execute the callback immediately once, which means we can capture the callback in this variable before executing it and clear it up after it's done executing the callback.

```javascript
export const createEffect = (callback) => {
   effectCallback = callback;
   callback();
   effectCallback = null;
};
```

Putting everything together:

```javascript
let effectCallback = null;

export const createEffect = (callback) => {
   effectCallback = callback;
   callback();
   effectCallback = null;
};

export const createSignal = (value) => {
  const signal = new Signal(value);

  return [
    function value() {
      if (effectCallback) {
        signal.subscribe(effectCallback);
      }

      return signal.getValue();
    },
    function setValue(newVal) {
      signal.setValue(newVal);
    },
  ];
};
```

Here is a [CodeSandbox](https://codesandbox.io/p/sandbox/solidjs-reactivity-diy-f5zh8x?file=%2Fsrc%2Fsignal.js%3A35%2C26-35%2C40&layout=%257B%2522sidebarPanel%2522%253A%2522EXPLORER%2522%252C%2522rootPanelGroup%2522%253A%257B%2522direction%2522%253A%2522horizontal%2522%252C%2522contentType%2522%253A%2522UNKNOWN%2522%252C%2522type%2522%253A%2522PANEL_GROUP%2522%252C%2522id%2522%253A%2522ROOT_LAYOUT%2522%252C%2522panels%2522%253A%255B%257B%2522type%2522%253A%2522PANEL_GROUP%2522%252C%2522contentType%2522%253A%2522UNKNOWN%2522%252C%2522direction%2522%253A%2522vertical%2522%252C%2522id%2522%253A%2522clyac8qxx00063b6kcdj0r3jb%2522%252C%2522sizes%2522%253A%255B100%252C0%255D%252C%2522panels%2522%253A%255B%257B%2522type%2522%253A%2522PANEL_GROUP%2522%252C%2522contentType%2522%253A%2522EDITOR%2522%252C%2522direction%2522%253A%2522horizontal%2522%252C%2522id%2522%253A%2522EDITOR%2522%252C%2522panels%2522%253A%255B%257B%2522type%2522%253A%2522PANEL%2522%252C%2522contentType%2522%253A%2522EDITOR%2522%252C%2522id%2522%253A%2522clyac8qxx00023b6kg4nyqgiz%2522%257D%255D%257D%252C%257B%2522type%2522%253A%2522PANEL_GROUP%2522%252C%2522contentType%2522%253A%2522SHELLS%2522%252C%2522direction%2522%253A%2522horizontal%2522%252C%2522id%2522%253A%2522SHELLS%2522%252C%2522panels%2522%253A%255B%257B%2522type%2522%253A%2522PANEL%2522%252C%2522contentType%2522%253A%2522SHELLS%2522%252C%2522id%2522%253A%2522clyac8qxx00033b6krfbo5b6p%2522%257D%255D%252C%2522sizes%2522%253A%255B100%255D%257D%255D%257D%252C%257B%2522type%2522%253A%2522PANEL_GROUP%2522%252C%2522contentType%2522%253A%2522DEVTOOLS%2522%252C%2522direction%2522%253A%2522vertical%2522%252C%2522id%2522%253A%2522DEVTOOLS%2522%252C%2522panels%2522%253A%255B%257B%2522type%2522%253A%2522PANEL%2522%252C%2522contentType%2522%253A%2522DEVTOOLS%2522%252C%2522id%2522%253A%2522clyac8qxx00053b6kv5v81n4d%2522%257D%255D%252C%2522sizes%2522%253A%255B100%255D%257D%255D%252C%2522sizes%2522%253A%255B50%252C50%255D%257D%252C%2522tabbedPanels%2522%253A%257B%2522clyac8qxx00023b6kg4nyqgiz%2522%253A%257B%2522tabs%2522%253A%255B%257B%2522id%2522%253A%2522clyac8qxx00013b6kq57p479j%2522%252C%2522mode%2522%253A%2522permanent%2522%252C%2522type%2522%253A%2522FILE%2522%252C%2522filepath%2522%253A%2522%252Fsrc%252Findex.js%2522%252C%2522state%2522%253A%2522IDLE%2522%257D%252C%257B%2522id%2522%253A%2522clyagpsv900023b6jketxf2fz%2522%252C%2522mode%2522%253A%2522permanent%2522%252C%2522type%2522%253A%2522FILE%2522%252C%2522initialSelections%2522%253A%255B%257B%2522startLineNumber%2522%253A35%252C%2522startColumn%2522%253A26%252C%2522endLineNumber%2522%253A35%252C%2522endColumn%2522%253A40%257D%255D%252C%2522filepath%2522%253A%2522%252Fsrc%252Fsignal.js%2522%252C%2522state%2522%253A%2522IDLE%2522%257D%255D%252C%2522id%2522%253A%2522clyac8qxx00023b6kg4nyqgiz%2522%252C%2522activeTabId%2522%253A%2522clyagpsv900023b6jketxf2fz%2522%257D%252C%2522clyac8qxx00053b6kv5v81n4d%2522%253A%257B%2522tabs%2522%253A%255B%257B%2522id%2522%253A%2522clyac8qxx00043b6k34nafcmv%2522%252C%2522mode%2522%253A%2522permanent%2522%252C%2522type%2522%253A%2522UNASSIGNED_PORT%2522%252C%2522port%2522%253A0%252C%2522path%2522%253A%2522%252F%2522%257D%255D%252C%2522id%2522%253A%2522clyac8qxx00053b6kv5v81n4d%2522%252C%2522activeTabId%2522%253A%2522clyac8qxx00043b6k34nafcmv%2522%257D%252C%2522clyac8qxx00033b6krfbo5b6p%2522%253A%257B%2522tabs%2522%253A%255B%255D%252C%2522id%2522%253A%2522clyac8qxx00033b6krfbo5b6p%2522%257D%257D%252C%2522showDevtools%2522%253Atrue%252C%2522showShells%2522%253Afalse%252C%2522showSidebar%2522%253Atrue%252C%2522sidebarPanelSize%2522%253A18.53200883002208%257D) where you can play around with this code.

The order of execution would be something like this:

* `createEffect` is executed with a callback function, and the same is stored within `effectCallback`.
    
* The callback is executed and will invoke any getter signal methods used within it.
    
* The getter method `value` within `createSignal` is executed and enters the conditional which checks whether the getter is accessed from within an effect callback.
    
* The callback is subscribed for any further value changes and re-executes when setter is called.
    

Here's something to help you visualise this process:

![Image](https://www.freecodecamp.org/news/content/images/2024/07/image-38.png align="left")

*Diagram illustrating order of execution of the final solution*

This was of course a rudimentary implementation of the concept.

SolidJS does a lot of things under the hood which can include:

* Optimisations: a signal will maintain its observers until they're manually disposed. This can become complex in web apps where nesting is common.
    
* Allowing a way to batch updates
    
* Supporting async subscribers
    

and much more.

## Conclusion

In this article, we explored the concept of reactivity and its role in web applications. We examined how various frameworks implement reactivity, with many using signals as a foundational mechanism.

By breaking down the SolidJS implementation of signals, we created our own version from scratch using the Pub-Sub pattern.

I hope this provided you with valuable insights into reactivity, signals, and enhanced your understanding of JavaScript.
