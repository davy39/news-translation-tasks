---
title: 'Handling State in React: Four Immutable Approaches to Consider'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-06-13T14:54:29.000Z'
originalURL: https://freecodecamp.org/news/handling-state-in-react-four-immutable-approaches-to-consider-d1f5c00249d5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*OEjZQSVvWnGgUF-dTrTS_w.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: React Native
  slug: react-native
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Cory House

  Perhaps the most common point of confusion in React today: state.

  Imagine you have a form for editing a user. It’s common to create a single change
  handler to handle changes to all form fields. It may look something like this:

  updateSta...'
---

By Cory House

Perhaps the most common point of confusion in React today: state.

Imagine you have a form for editing a user. It’s common to create a single change handler to handle changes to all form fields. It may look something like this:

```js
updateState(event) {
 const {name, value} = event.target;
 let user = this.state.user; // this is a reference, not a copy...
 user[name] = value; // so this mutates state ?
 return this.setState({user});
}
```

The concern is on line 4. Line 4 actually mutates state because the user variable is a _reference_ to state. React state should be treated as immutable.

From the [React docs](https://facebook.github.io/react/docs/react-component.html#state):

> Never mutate `this.state` directly, as calling `setState()` afterwards may replace the mutation you made. Treat `this.state` as if it were immutable.

Why?

1. setState batches work behind the scenes. This means a manual state mutation may be overridden when setState is processed.
2. If you declare a shouldComponentUpdate method, you can’t use a === equality check inside because _the object reference will not change_. So the approach above has a potential performance impact as well.

**Bottom line**: The example above often works okay, but to avoid edge cases, treat state as immutable.

Here are four ways to treat state as immutable:

### Approach #1: Object.assign

[Object.assign](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign) creates a copy of an object. The first parameter is the target, then you specify one or more parameters for properties you’d like to tack on. So fixing the example above involves a simple change to line 3:

```js
updateState(event) {
 const {name, value} = event.target;
 let user = Object.assign({}, this.state.user);
 user[name] = value;
 return this.setState({user});
}
```

On line 3, I’m saying “Create a new empty object and add all the properties on this.state.user to it.” This creates a separate copy of the user object that’s stored in state. Now I’m safe to mutate the user object on line 4 — it’s a completely separate object from the object in state.

Be sure to polyfill Object.assign since it’s [unsupported in IE](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign) and [not transpiled by Babel](https://babeljs.io/docs/usage/polyfill/). Four options to consider:

1. [object-assign](https://www.npmjs.com/package/object-assign)
2. [The MDN docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign)
3. [Babel Polyfill](https://babeljs.io/docs/usage/polyfill/)
4. [Polyfill.io](https://polyfill.io/v2/docs/features/#Object_assign)

### Approach #2: Object Spread

Object spread is currently a [stage 3 feature](https://github.com/tc39/proposal-object-rest-spread), and can be [transpiled by Babel](http://babeljs.io/docs/plugins/transform-object-rest-spread/#example). This approach is more concise:

```js
updateState(event) {
 const {name, value} = event.target;
 let user = {...this.state.user, [name]: value};
 this.setState({user});
}
```

On line 3 I’m saying “Use all the properties on this.state.user to create a new object, then set the property represented by [name] to a new value passed on event.target.value”. So this approach works similarly to the Object.assign approach, but has two benefits:

1. No polyfill required, since Babel can transpile
2. More concise

You can even use destructuring and inlining to make this a one-liner:

```js
updateState({target}) {
 this.setState({user: {...this.state.user, [target.name]: target.value}});
}
```

I’m destructuring event in the method signature to get a reference to event.target. Then I’m declaring that state should be set to a copy of this.state.user with the relevant property set to a new value. I like how terse this is. This is currently my favorite approach to writing change handlers. ?

These two approaches above are the most common and straightforward ways to handle immutable state. Want more power? Check out the other two options below.

### Approach #3: Immutability Helper

[Immutability-helper](https://github.com/kolodny/immutability-helper) is a handy library for mutating a copy of data without changing the source. This library is suggested in [React’s docs](https://facebook.github.io/react/docs/update.html).

```js
// Import at the top:
import update from 'immutability-helper';

updateState({target}) {
 let user = update(this.state.user, {$merge: {[target.name]: target.value}});
 this.setState({user});
}
```

On line 5, I’m calling merge, which is [one of many commands](https://github.com/kolodny/immutability-helper#available-commands) provided by immutability-helper. Much like Object.assign, I pass it the target object as the first parameter, then specify the property I’d like to merge in.

There’s much more to immutability helper than this. It uses a syntax inspired from MongoDB’s query language and offers a [variety of powerful ways to work with immutable data](https://github.com/kolodny/immutability-helper#available-commands).

### Approach #4: Immutable.js

Want to programatically enforce immutability? Consider [immutable.js](https://facebook.github.io/immutable-js/). This library provides immutable data structures.

Here’s an example, using an immutable map:

```js

// At top, import immutable
import { Map } from 'immutable';

// Later, in constructor...
this.state = {
  // Create an immutable map in state using immutable.js
  user: Map({ firstName: 'Cory', lastName: 'House'})
};

updateState({target}) {
 // this line returns a new user object assuming an immutable map is stored in state.
 let user = this.state.user.set(target.name, target.value);
 this.setState({user});
}
```

There are three basic steps above:

1. Import immutable.
2. Set state to an immutable map in the constructor
3. Use the set method in the change handler to create a new copy of user.

The beauty of immutable.js: **If you try to mutate state directly, it will fail**. With the other approaches above, it’s easy to forget, and React won’t warn you when you mutate state directly.

The downsides of immutable?

1. **Bloat**. Immutable.js adds 57K minified to your bundle. Considering libraries like [Preact can replace React in only 3K](https://preactjs.com), that’s hard to accept.
2. **Syntax**. You have to reference object properties via strings and method calls instead of directly. I prefer user.name over user.get(‘name’).
3. **YATTL** (Yet another thing to learn) — Anyone joining your team needs to learn yet another API for getting and setting data, as well as a new set of datatypes.

A couple other interesting alternatives to consider:

* [seamless-immutable](https://github.com/rtfeldman/seamless-immutable)
* [react-copy-write](https://github.com/aweary/react-copy-write)

### Warning: Watch Out For Nested Objects!

Option #1 and #2 above (Object.assign and Object spread) only do a _shallow_ clone. So if your object contains nested objects, **those nested objects will be copied by reference instead of by value**. So if you change the nested object, you’ll mutate the original object. ?

Be surgical about what you’re cloning. Don’t clone all the things. Clone the objects that have changed. Immutability-helper (mentioned above) makes that easy. As do alternatives like [immer](https://github.com/mweststrate/immer), [updeep](https://github.com/substantial/updeep), or a [long list of alternatives](https://github.com/markerikson/redux-ecosystem-links/blob/master/immutable-data.md#immutable-update-utilities).

You might be tempted to reach for deep merging tools like [clone-deep](https://www.npmjs.com/package/clone-deep), or [lodash.merge](https://lodash.com/docs/#merge), but **avoid blindly deep cloning**.

Here’s why:

1. Deep cloning is expensive.
2. Deep cloning is typically wasteful (instead, only clone what has actually changed)
3. Deep cloning causes unnecessary renders since React thinks everything has changed when in fact perhaps only a specific child object has changed.

Thanks to Dan Abramov for the suggestions I’ve mentioned above:

%[https://twitter.com/dan_abramov/status/988546679115800577?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed&ref_url=https%3A%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Ftype%3Dtext%252Fhtml%26key%3Da19fcc184b9711e1b4764040d3dc5c07%26schema%3Dtwitter%26url%3Dhttps%253A%2F%2Ftwitter.com%2Fdan_abramov%2Fstatus%2F988546679115800577%26image%3Dhttps%253A%2F%2Fi.embed.ly%2F1%2Fimage%253Furl%253Dhttps%25253A%25252F%25252Fpbs.twimg.com%25252Fprofile_images%25252F906557353549598720%25252FoapgW_Fp_400x400.jpg%2526key%253Da19fcc184b9711e1b4764040d3dc5c07]

### Final Tip: Consider Using Functional setState

One other wrinkle can bite you:

> setState() does not immediately mutate this.state but creates a pending state transition. Accessing this.state after calling this method can potentially return the existing value.

Since setState calls are batched, code like this leads to a bug:

```js
updateState({target}) {
 this.setState({user: {...this.state.user, [target.name]: target.value}});
 doSomething(this.state.user) // Uh oh, setState merely schedules a state change, so this.state.user may still have old value
}
```

If you want to run code after a setState call has completed, use the callback form of setState:

```js
updateState({target}) {
   this.setState((prevState) => {
     const updatedUser = {...prevState.user, [target.name]: target.value}; // use previous value in state to build new state...     
     return { user: updatedUser }; // And what I return here will be set as the new state
   }, () => this.doSomething(this.state.user); // Now I can safely utilize the new state I've created to call other funcs...
     );
 }
```

### My Take

I admire the simplicity and light weight of option #2 above: Object spread. It doesn’t require a polyfill or separate library, I can declare a change handler on a single line, and I can be surgical about what has changed. ? Working with nested object structures? I currently prefer [Immer.](https://github.com/mweststrate/immer)

Have other ways you like to handle state in React? Please chime in via the comments!

### Looking for More on React? ⚛

I’ve authored [multiple React and JavaScript courses](http://bit.ly/psauthorpageimmutablepost) on Pluralsight ([free trial](http://bit.ly/pstrialimmutablepost)). My latest, “[Creating Reusable React Components](http://bit.ly/psreactcomponentsimmutablepost)” just published! ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*BkPc3o2d2bz0YEO7z5C2JQ.png)

[Cory House](https://twitter.com/housecor) is the author of [multiple courses on JavaScript, React, clean code, .NET, and more on Pluralsight](http://pluralsight.com/author/cory-house). He is principal consultant at [reactjsconsulting.com](http://www.reactjsconsulting.com), a Software Architect at VinSolutions, a Microsoft MVP, and trains software developers internationally on software practices like front-end development and clean coding. Cory tweets about JavaScript and front-end development on Twitter as [@housecor](http://www.twitter.com/housecor).

