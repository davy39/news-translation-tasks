---
title: Why React Hooks, and how did we even get here?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-12T21:18:18.000Z'
originalURL: https://freecodecamp.org/news/why-react-hooks-and-how-did-we-even-get-here-aa5ed5dc96af
coverImage: https://cdn-media-1.freecodecamp.org/images/0*tFj5MfPtA2bvvJWo
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: software development
  slug: software-development
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Ryan Yurkanin

  TL;DR: Hooks have learned from the trade-offs of mixins, higher order components,
  and render props to bring us new ways to create contained, composable behaviors
  that can be consumed in a flat and declarative manner. ?

  However, hooks...'
---

By Ryan Yurkanin

**TL;DR:** Hooks have learned from the trade-offs of mixins, higher order components, and render props to bring us new ways to **create** **contained, composable behaviors** that can be consumed in **a** **flat and declarative manner. ?**

However, hooks come with their own price. They are not the silver bullet solution. Sometimes you need hierarchy. So let’s take a closer look.

[React Hooks](https://reactjs.org/docs/hooks-overview.html) are here, and I immediately fell in love with them. To understand why Hooks are great, I think it helps to look at how we’ve been solving a common problem throughout React’s history.

**Here’s the situation.** You have to show the user’s mouse position. ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*skhvS29DZ6sBkCPBmaMz7g.png)
_“Well that was easy!”_

#### ⚠️ However there are some ways this can come back to bite us.

* If you need that mouse move behavior in another component you will have to rewrite the same code.
* If you add more behaviors like this, it will become harder to understand at first glance. This is because the behavior’s logic is spread across `componentDidMount` and `componentWillUnmount` ?

We’re engineers though, and we have _a ton_ of tools to help us break this pattern out. Let’s review some of the ways we’ve historically done it and their trade-offs. ?

### Mixins

Mixins get a lot of flak. They set the stage for grouping together lifecycle hooks to describe one effect.

![Image](https://cdn-media-1.freecodecamp.org/images/1*nkp3K5sbw6FuGvoLofVk8g.png)

While the general idea of encapsulating logic is great, we ended up learning some [serious lessons from mixins](https://reactjs.org/blog/2016/07/13/mixins-considered-harmful.html).

It’s not obvious where `this.state.x` is coming from. With mixins, it’s also possible for the mixin to be blindly relying on that a property exists in the component.

That becomes a huge problem as people start including and extending tons of mixins. You can’t simply search in a single file and assume you haven’t broken something somewhere else.

Refactoring needs to be easy. **These mixed-in behaviors need to be more obvious that they don’t belong to the component.** They shouldn’t be using the internals of the component. ?‍

### Higher Order Components

We can achieve a similar effect, and make it a bit less magical by creating a container that passes in props! Inheritance’s main trade-off is it makes refactoring harder, so let’s try composition!

![Image](https://cdn-media-1.freecodecamp.org/images/1*qJZXnzuAgXQsSoibXZH6Zg.png)

While this is more code, we are moving in the right direction. We have all the benefits of Mixins. Now we have a `<MouseRender` /> component that is no longer tightly coupled to the subscription behavior.

What if we wanted to render something different though? Do we always need to make a new component?

### Render Props & Children as a Function

This is the pattern that has been staring us in the face the entire time. All we want is a component that handles the mouse move behavior, and the ability to render whatever we want.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ii7bRuk2u7jBqunmIzwGrQ.png)

#### This subtle difference has some pretty awesome benefits

* It is now super obvious what is providing `x` and `y`. You can also easily rename them to prevent name collisions.
* We have flexible control over what is rendering. We don’t need to be making new components, and if we decide to, it’s just a simple copy paste.
* You can see all of this directly in a components render function. It’s in plain sight and easy for new developers coming in to identify. `cmd + f` checks out here.

The main problem with this pattern is that your components are bound to nest quite a few of these in their renders. Once you start nesting multiple render prop components, it can be incredibly hard to reason what is going on.

Also, it creates a false sense of hierarchy. Just because a behavior is “nested” under another behavior doesn’t mean it relies on the parent behavior. Take for example this snippet.

![Image](https://cdn-media-1.freecodecamp.org/images/1*sYxg-jYyqnRrNuRVkxoqrg.png)
_Reminds me of callback hell_

**If only there was a way to have all this power, in a declarative AND flat way. ?**

### Hooks

What if we could remove the nesting, and bubble everything up to the top? That way the only JSX in our render function is pure rendering logic.

![Image](https://cdn-media-1.freecodecamp.org/images/1*11zyjavrNZlqDypso2EaeQ.png)
_It’s so beautiful…_

This is everything I ever wanted.

* Not only is the behavior in its own neat little package, `useEffect` stops it from being spread across three different lifecycle hooks
* Where the component is getting this data from is incredibly clear, it’s nestled neatly inside the render function.
* No matter how many of these I need to bring in, my code won’t become increasingly nested.

[Sunil Pai](https://www.freecodecamp.org/news/why-react-hooks-and-how-did-we-even-get-here-aa5ed5dc96af/undefined) used some clever highlighting in the tweet below to illustrate how effective hooks are at not just reducing the total amount of code, but also grouping together related parts.

### However, there are some catches

When using hooks, you have to remember a couple of rules that may seem weird at first:

#### **⚠️ You should call hooks at the top level of the render function.**

This means no conditional hooks. Our contract with React is that we will call the same amount of hooks, in the same order every time.

This rule starts to make more sense when you compare it to how Mixins, and HOCs work. You can’t conditionally use them and reorder them on each render.

If you want conditional effects, you should split your hooks into other components, or consider a different pattern.

#### ️️⚠️ **You can only use hooks in React Function Components, and in Custom Hooks.**

I’m not sure if there’s actually any technical reason to not try calling them in a regular function. This ensures that the data is always visible in the component file.

#### ⚠️ **There aren’t hook primitives for componentDidCatch or getSnapshotBeforeUpdate.**

The React team says they are on their way though!

For the componentDidCatch use case, you could create an Error Boundary component, getSnapshotBeforeUpdate is a bit trickier, but fortunately pretty rare.

### Some Final Notes

I have no doubt that hooks are about to change the way we view React, and shake up some best practices. The amount of excitement and libraries coming out is inspiring!

However, I have seen the hype for all of these design patterns in the past. While most have ended up being very valuable tools in our toolboxes, they all come with a price.

I still don’t fully understand the trade-offs of hooks, and that scares me. I highly suggest playing around with them, and learning by example. You should probably wait a bit before doing a full rewrite in them though ?

If you have any questions or are looking for one-on-one React mentorship, feel free to tweet me **@yurkaninryan** any time!

If you like my writing style, here are some other articles that I’ve done.

Good luck and happy coding!! ?

