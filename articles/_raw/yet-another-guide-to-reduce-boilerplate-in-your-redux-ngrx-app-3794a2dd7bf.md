---
title: Yet another guide to reduce boilerplate in your Redux (NGRX) app
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-05T23:47:09.000Z'
originalURL: https://freecodecamp.org/news/yet-another-guide-to-reduce-boilerplate-in-your-redux-ngrx-app-3794a2dd7bf
coverImage: https://cdn-media-1.freecodecamp.org/images/1*jtOmHUt-CfaFwspj81N6kA.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: React
  slug: react
- name: Redux
  slug: redux
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Andrey Goncharov

  What are we gonna cover here?

  In this article, we’re gonna discuss several ways/tips/tricks/ancient black magic
  rituals to reduce boilerplate in our overwhelmed-with-boilerplate Redux (and NGRX!)
  apps. I’ve come up with these over...'
---

By Andrey Goncharov

### **What are we gonna cover here?**

In this article, we’re gonna discuss several ways/tips/tricks/ancient black magic rituals to reduce boilerplate in our overwhelmed-with-boilerplate Redux (and NGRX!) apps. I’ve come up with these over the years from first-hand production experience.

Let me be honest with you all. I wanted to speak just about my new micro-library [flux-action-class](https://github.com/keenondrums/flux-action-class) at first. But it seems like sometimes tech blogs look more and more like Twitter lately…and maybe you want some more meaningful long read. So I thought: “What the heck? I got some experience and best practices of my own which I spilled some sweat and blood over. Maybe, it could help some people out there. Maybe, people out there could help me to improve some of it.”

### Identifying boilerplate

Let’s take a look at a typical example of how to make AJAX requests in Redux. In this particular case let’s imagine we wanna get a list of cats from the server.

_If you’re wondering why I have selector factories (makeSelector…) take a look [here](https://redux.js.org/recipes/computing-derived-data#computing-derived-data)_

I’m leaving out side effect handling on purpose. It’s a topic for a whole different article full of teenager’s anger and criticism for the existing ecosystem :D

This code has several weak spots:

* Action creators are unique objects themselves but we still need action types for serialization purposes. Could we do better?
* As we add entities we keep duplicating the same logic for flipping `loading` flag. Actual server data and the way we want to handle it may change, but logic for `loading` is always the same. Could we get rid of it?
* Switch statement is O(n) (which is not a solid argument by itself because Redux is not very performant anyway). Redux requires a couple extra lines of code for each case and switches can not be easily combined. Could we figure out something more performant and readable?
* Do we really need to keep an error for each entity separately?
* Using selectors is a good idea. This way we have an abstraction over our store and can change its shape without breaking the whole app by just adjusting our selectors. Yet we have to create a factory for each selector due to how memoizaion works. Is there any other way?

### Tip 1: Get rid of action types

Well, not really. But we can make JS generate them for us!

Let’s take a minute here to think why we even need action types. Of course, to help the reducer somehow differentiate between incoming actions and change our state accordingly. But does it really have to be a string? If only we had a way to create objects (actions) of certain types… Classes to the rescue! We most definitely could use classes as action creators and do `switch` by type. Like this:

All good, but here’s a thing… We can no longer serialize and deserialize our actions. They are no longer simple objects with a prototype of Object. All have unique prototypes which actually makes switching over `action.constructor` work. Dang, I liked the idea of serializing my actions to a string and attaching it to bug reports. So could we do even better?

Actually, yes! Luckily each class has a name, which is a string, and we could utilize them. So for the purposes of serialization, each action needs to be a simple object with field `type` (please, take a look [here](https://github.com/redux-utilities/flux-standard-action) to learn what else any self-respecting action should have). We could add getter `type` to each one of our classes which would use class's name.

It would work, but this way we can not prefix our action types as [this](https://github.com/erikras/ducks-modular-redux) great proposal suggests (actually, I like its [successor](https://github.com/alexnm/re-ducks) even more). To work around prefixing we should stop using class’ name directly and create another getter for it. This time a static one.

Let’s polish it a little to avoid code duplication and add one more assumption to reduce boilerplate even further. If action is an error action `payload` must be an instance of `Error`.

At this point, it works perfectly with NGRX. Redux is complaining about dispatching non-plain objects (it validates the prototype chain). Fortunately, JS allows us to return an arbitrary value from the constructor and we do not really need our actions to have a prototype.

Not to make you guys copy-paste `ActionStandard` class and worry about its reliability, I created a [small library called flux-action-class](https://github.com/keenondrums/flux-action-class), which already has all that code covered with tests with 100% code coverage, written in TypeScript for TypeScript and JavaScript projects.

### Tip 2: Combine your reducers

The idea is simple: use [combineReducers](https://redux.js.org/api/combinereducers) not only for top level reducers, but for combining reducers for `loading` and other stuff. Let the code speak for itself:

### Tip 3: Switch away from switch

Use objects and pick from them by key instead! Picking a property of an object by key is O(1) and it looks much cleaner if you ask me. Like this:

I suggest we refactor `reducerLoading` a little bit. With the introduction of reducer maps, it makes sense to return a reducer map from `reducerLoading`. We could extend it if needed (unlike switches).

[Redux’s official documentation mentions this](https://redux.js.org/recipes/reducing-boilerplate#generating-reducers), but for some reason, I saw lots of people still using switch-cases. There’s already a [library](https://github.com/kolodny/redux-create-reducer) for `createReducer`. Do not hesitate to use it.

### Tip 4: Have a global error handler

It’s not necessary to keep an error for each entity. In most cases, we need to display an error dialog or something. The same error dialog for all them!

Create a global error handler. In the most simple case it could look like this:

Then in your side-effect’s `catch` block dispatch `ErrorInit`. It could look like this with [redux-thunk](https://github.com/reduxjs/redux-thunk):

Then you could stop providing a reducer for `error` part of cats' state and `CatsGetError` just to flip `loading` flag.

### Tip 5: Stop memoizing everything

Let’s take a look at a mess we have with selectors one more time.  
 _I omitted `makeSelectorCatsError` because of what we discovered in the previous section._

Why would we create memoized selectors for everything? What’s there to memoize? Picking an object’s field by key (which is exactly what’s happening here) is O(1). Just write a regular non-memoized function. Use memoization only when you want to change the shape of the data in your store in a way that requires non-constant time before returning it to your component.

Memoization could make sense only if computed some derived data. For this example let’s imagine that each cat is an object with field `name` and we need a string containing names of all cats.

### Conclusion

Let’s take a look at what we started with:

And what the result is:

Hopefully, you found something useful for your project. Feel free to communicate your feedback to me! I most certainly appreciate any criticism and questions.

