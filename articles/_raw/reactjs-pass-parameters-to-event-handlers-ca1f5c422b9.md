---
title: ReactJS - Parameterized Event Handlers
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-11T16:16:58.000Z'
originalURL: https://freecodecamp.org/news/reactjs-pass-parameters-to-event-handlers-ca1f5c422b9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Rxzsy_E2MgxPP5oVmh1Q_g.jpeg
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Sanket Meghani

  It is quite frequent requirement to pass parameters to event handlers of custom
  React components. There are several ways to achieve this with ES6 depending on whether
  we need reference to the event or not.

  Using the bind function

  We...'
---

By Sanket Meghani

It is quite frequent requirement to pass parameters to event handlers of custom React components. There are several ways to achieve this with ES6 depending on whether we need reference to the event or not.

### Using the bind function

We can define the event handler and bind it to `this` using JavaScript’s `Function.prototype.bind()` function.

If we need to pass custom parameters, then we can simply pass the parameters to the bind call. The SyntheticEvent will be passed as second parameter to the handler.

A `bind` call function in a JSX prop like above will create a brand new function on every single render. This is bad for performance, as it will result in the garbage collector being invoked way more than is necessary. It may also cause unnecessary re-renders if a brand new function is passed as a prop to a component that uses reference equality check on the prop to determine if it should update.

To avoid creating a brand new function on every single render, we can bind the function in the constructor.

Now, we need not to bind the function while specifying the event handler on line 13. However, the drawback here is that we cannot pass dynamic value for parameter.

### Using ES6 arrow function

Calling `bind` every time is annoying. To avoid calling `bind` we can use ES6 arrow function which binds the function with `this` automatically.

We can also pass additional parameters to event handlers.

The problem with both above syntax is that a different callback instance is created each time the component is rendered, same as with the `bind` function.

To avoid creating a brand new callback instance on every render, we can use property initializer syntax to correctly bind callbacks.

To pass parameters to event handlers while using property initializer syntax, we need to use currying.

Please note that the currying results into a new instance being created for every invocation.

### Conclusion

Provided all the different approaches above, using the arrow function with currying seems to be the cleanest & most concise (not most efficient though) way to define event handlers that accepts user defined parameters.

I would love to hear your comments, suggestions or questions on above approaches.

