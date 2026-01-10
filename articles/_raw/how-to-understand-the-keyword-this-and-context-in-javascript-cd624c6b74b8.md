---
title: How to understand the keyword this and context in JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-21T17:03:13.000Z'
originalURL: https://freecodecamp.org/news/how-to-understand-the-keyword-this-and-context-in-javascript-cd624c6b74b8
coverImage: https://cdn-media-1.freecodecamp.org/images/1*4Ufc1CWbaLhjEMhPgVV3Qw.jpeg
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Lukas Gisder-Dubé

  As mentioned in one of my earlier articles, mastering JavaScript fully can be a
  lengthy journey. You may have come across this on your journey as a JavaScript Developer.
  When I started out, I first saw it when using eventListener...'
---

By Lukas Gisder-Dubé

As mentioned in [one of my earlier articles](https://levelup.gitconnected.com/10-things-to-learn-on-the-way-to-become-a-javascript-master-f4fc632b2bb7), mastering JavaScript fully can be a lengthy journey. You may have come across `this` on your journey as a JavaScript Developer. When I started out, I first saw it when using `eventListeners` and with jQuery. Later on, I had to use it often with React and I am sure you also did. That does not mean that I really understood what it is and how to fully take control of it.

However, it is very useful to master the concept behind it, and when approached with a clear mind, it is not very difficult either.

#### Digging into this

> _Explaining `this` can lead to a lot of confusion, simply by the naming of the keyword._

`this` is tightly coupled to what context you are in, in your program. Let’s start all the way at the top. In our browser, if you just type `this` in the console, you will get the `window`-object, the outermost context for your JavaScript. In Node.js, if we do:

```js
console.log(this)
```

we end up with `{}`, an empty object. This is a bit weird, but it seems like Node.js behaves that way. If you do

```js
(function() {
  console.log(this);
})();
```

however, you will receive the `global` object, the outermost context. In that context `setTimeout` , `setInterval` , are stored. Feel free to play around a little bit with it to see what you can do with it. As from here, there is almost no difference between Node.js and the browser. I will be using `window`. Just remember that in Node.js it will be the `global` object, but it does not really make a difference.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ucforPRGm6kR3bdZMHzHKQ.jpeg)
_Photo by [Unsplash](https://unsplash.com/photos/e_5NhSomvS4?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Chor Hung Tsang</a> on <a href="https://unsplash.com/search/photos/top-level?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

Remember: Context only makes sense inside of functions

Imagine you write a program without nesting anything in functions. You would simply write one line after another, without going down specific structures. That means you do not have to keep track of where you are. You are always on the same level.

When you start having functions, you might have different levels of your program and `this` represents where you are, what object called the function.

#### Keeping track of the caller object

Let’s have a look at the following example and see how `this` changes depending on the context:

```js
const coffee = {
  strong: true,
  info: function() {
    console.log(`The coffee is ${this.strong ? '' : 'not '}strong`)
  },
}

coffee.info() // The coffee is strong
```

Since we call a function that is declared inside the `coffee` object, our context changes to exactly that object. We can now access all of the properties of that object through `this` . In our example above, we could also just reference it directly by doing `coffee.strong` . It gets more interesting, when we do not know what context, what object, we are in or when things simply get a bit more complex. Have a look at the following example:

```js
const drinks = [
  {
    name: 'Coffee',
    addictive: true,
    info: function() {
      console.log(`${this.name} is ${this.addictive ? '' : 'not '} addictive.`)
    },
  },
  {
    name: 'Celery Juice',
    addictive: false,
    info: function() {
      console.log(`${this.name} is ${this.addictive ? '' : 'not '} addictive.`)
    },
  },
]

function pickRandom(arr) {
  return arr[Math.floor(Math.random() * arr.length)]
}

pickRandom(drinks).info()
```

#### Classes and Instances

Classes can be used to abstract your code and share behavior. Always repeating the `info` function declaration in the last example is not good. Since classes and their instances are in fact objects, they behave in the same way. One thing to note however, is that declaring `this` in the constructor actually is a prediction for the future, when there will be an instance.

Let’s take a look:

```js
class Coffee {
  constructor(strong) {
    this.strong = !!strong
  }
  info() {
    console.log(`This coffee is ${this.strong ? '' : 'not '}strong`)
  }
}

const strongCoffee = new Coffee(true)
const normalCoffee = new Coffee(false)

strongCoffee.info() // This coffee is strong
normalCoffee.info() // This coffee is not strong
```

#### Pitfall: seamlessly nested function calls

Sometimes, we end up in a context that we did not really expect. This can happen, when we unknowingly call the function inside another object context. A very common example is when using `setTimeout` or `setInterval` :

```js
// BAD EXAMPLE
const coffee = {
  strong: true,
  amount: 120,
  drink: function() {
    setTimeout(function() {
      if (this.amount) this.amount -= 10
    }, 10)
  },
}

coffee.drink()
```

What do you think `coffee.amount` is?

...

..

.

It is still `120` . First, we were inside the `coffee` object, since the `drink` method is declared inside of it. We just did `setTimeout` and nothing else. That’s exactly it.

As I explained earlier, the `setTimeout` method is actually declared in the `window` object. When calling it, we actually switch context to the `window` again. That means that our instructions actually tried to change `window.amount`, but it ended up doing nothing because of the `if`-statement. To take care of that, we have to `bind` our functions (see below).

#### React

Using React, this will hopefully be a thing of the past soon, thanks to Hooks. At the moment, we still have to `bind` everything (more on that later) in one way or another. When I started out, I had no idea why I was doing it, but at this point, you should already know why it is necessary.

Let’s have a look at two simple React class Components:

```js
// BAD EXAMPLE
import React from 'react'

class Child extends React.Component {
  render() {
    return <button onClick = {
      this.props.getCoffee
    } > Get some Coffee! < /button>
  }
}

class Parent extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      coffeeCount: 0,
    }
    // change to turn into good example – normally we would do:
    // this._getCoffee = this._getCoffee.bind(this)
  }
  render() {
    return ( <
      React.Fragment >
      <
      Child getCoffee = {
        this._getCoffee
      }
      /> < /
      React.Fragment >
    )
  }

  _getCoffee() {
    this.setState({
      coffeeCount: this.state.coffeeCount + 1,
    })
  }
}
```

When we now click on the button rendered by the `Child` , we will receive an error. Why? Because React changed our context when calling the `_getCoffee` method.

I assume that React does call the render method of our Components in another context, through helper classes or similar (even though I would have to dig deeper to find out for sure). Therefore, `this.state` is undefined and we’re trying to access `this.state.coffeeCount` . You should receive something like `Cannot read property coffeeCount of undefined` .

To solve the issue, you have to `bind` (we’ll get there) the methods in our classes, as soon as we pass them out of the component where they are defined.

![Image](https://cdn-media-1.freecodecamp.org/images/1*nkgR5atcQtIeHQLeY8XMRQ.jpeg)
_How many coffees did you drink so far? / Photo by [Unsplash](https://unsplash.com/photos/7X96RNhpxBc?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Ozgu Ozden</a> on <a href="https://unsplash.com/search/photos/coffee?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

Let’s have a look at one more generic example:

```js
// BAD EXAMPLE
class Viking {
  constructor(name) {
    this.name = name
  }

  prepareForBattle(increaseCount) {
    console.log(`I am ${this.name}! Let's go fighting!`)
    increaseCount()
  }
}

class Battle {
  constructor(vikings) {
    this.vikings = vikings
    this.preparedVikingsCount = 0

    this.vikings.forEach(viking => {
      viking.prepareForBattle(this.increaseCount)
    })
  }

  increaseCount() {
    this.preparedVikingsCount++
    console.log(`${this.preparedVikingsCount} vikings are now ready to fight!`)
  }
}

const vikingOne = new Viking('Olaf')
const vikingTwo = new Viking('Odin')

new Battle([vikingOne, vikingTwo])
```

We’re passing the `increaseCount` from one class to another. When we call the `increaseCount` method in `Viking`, we have already changed context and `this` actually points to the `Viking` , meaning that our `increaseCount` method will not work as expected.

#### Solution — bind

The simplest solution for us is to `bind` the methods that will be passed out of our original object or class. There are different ways where you can bind functions, but the most common one (also in React) is to bind it in the constructor. So we would have to add this line in the `Battle` constructor before line 18:

```js
this.increaseCount = this.increaseCount.bind(this)
```

You can bind any function to any context. This does not mean that you always have to bind the function to the context it is declared in (this is the most common case, however). Instead, you could bind it to another context. With `bind` , you always **set the context for a function declaration**. This means that all calls for that function will receive the bound context as `this` . There are two other helpers for setting the context.

> Arrow functions `() => {}` automatically bind the function to the declaration context

![Image](https://cdn-media-1.freecodecamp.org/images/1*acg_8b0T63Aiv8TAbtn5_w.jpeg)
_Photo by [Unsplash](https://unsplash.com/photos/kMMY3V6IUrw?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Mario Klassen</a> on <a href="https://unsplash.com/search/photos/pointing?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

#### Apply and call

They both do basically the same thing, just that the syntax is different. For both, you pass the context as first argument. `apply` takes an array for the other arguments, with `call` you can just separate other arguments by comma. Now what do they do? Both of these methods set the context for **one specific function call**. When calling the function without `call` , the context is set to the default context (or even a bound context). Here is an example:

```js
class Salad {
  constructor(type) {
    this.type = type
  }
}

function showType() {
  console.log(`The context's type is ${this.type}`)
}

const fruitSalad = new Salad('fruit')
const greekSalad = new Salad('greek')

showType.call(fruitSalad) // The context's type is fruit
showType.call(greekSalad) // The context's type is greek

showType() // The context's type is undefined
```

Can you guess what the context of the last `showType()` call is?

…

..

.

You’re right, it is the outermost scope, `window` . Therefore, `type` is `undefined`, there is no `window.type`

This is it, hopefully you now have a clear understanding on how to use `this` in JavaScript. Feel free to leave suggestions for the next article in the comments.

_About the Author: Lukas Gisder-Dubé co-founded and led a startup as CTO for 1 1/2 years, building the tech team and architecture. After leaving the startup, he taught coding as Lead Instructor at [Ironhack](https://www.freecodecamp.org/news/how-to-understand-the-keyword-this-and-context-in-javascript-cd624c6b74b8/undefined) and is now building a Startup Agency & Consultancy in Berlin. Check out [dube.io](https://dube.io) to learn more._

![Image](https://cdn-media-1.freecodecamp.org/images/1*p-l0Cee1IHvX0RQkVTOceQ.png)

