---
title: How to update a component’s prop in ReactJS — oh yes, it’s possible
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-17T05:37:24.000Z'
originalURL: https://freecodecamp.org/news/how-to-update-a-components-prop-in-react-js-oh-yes-it-s-possible-f9d26f1c4c6d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Rzaf_TyulUee7xEdDs3bRw.png
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Dheeraj DeeKay

  If you have read the official React docs (and you should, as it is one great resource
  on React) you’d notice [these lines](http://this.props.onNameChanged(''New name'')):


  Whether you declare a component as a function or a class, it m...'
---

By Dheeraj DeeKay

If you have read the official React docs (and you should, as it is one great resource on React) you’d notice [these lines](http://this.props.onNameChanged('New name')):

> Whether you declare a component [as a function or a class](https://reactjs.org/docs/components-and-props.html#function-and-class-components), it must never modify its own props.  
> React is pretty flexible but it has a single strict rule:  
> **All React components must act like pure functions with respect to their props.**

Props are never to be updated. We are to use them as is. Sounds rigid right? But React has its reasons behind this rule and I’m pretty convinced by their reasoning. The only caveat is, though, that there are situations where we might need to initiate the update of a prop. And we will soon know how.

Consider the following line of code from a parent component:

`<MyChild childName={this.state.parentName}` />

This is a simple line which every React dev is probably familiar with. You are calling child component. While you are doing that, you are also passing the state of the parent (`parentName`) to the child. In the child component, this state will be accessed as `this.props.childName.` Fair enough.

Now if there is any change of name required, `parentName` will be changed in the parent and that change will automatically be communicated to the child as is the case with the React mechanism. This setup works in most of the scenarios.

But what if you need to update the prop of the child component, and the knowledge of the change required and the trigger to change it is only known to the child? Considering the ways of React, data can only flow from top-to-bottom i.e., from parent-to-child. So then how are we to communicate to the parent that a change to prop is required?

Well, although this is anti-pattern and not recommended, the devs who wrote the language have us covered. Surprise!

We can do it with Callbacks. I know, no surprise there! They seem to come in handy for every problem we face here. Okay, okay, now how?

![Image](https://cdn-media-1.freecodecamp.org/images/zdcDnVK0Okw3GBfFb8vzE3Ofi0uKUpD5KRRN)

Imagine if the above call to the child was modified this way:

`<MyChild childName={this.state.parentName} onNameChange={this.onChange}` />

Now in addition to a prop `childName` our needy-child also has an event called `onNameChange` exposed. This is the way to resolve the issue. Our child has done its part. Now it’s the parent’s turn to do what is required. And it need not fret. All it needs to do is define a function `onChange` as

```
function onChange(newName) {   this.setState({ parentName: newName });}
```

That’s it. Now whenever and wherever in the child component we wish to update the `parentName` prop, all we have to do is call ``this.props.onNameChange(' My New name')` and voilà! You’ll have what you desire. That’s it. Done and dusted.

Hope that was easy to grasp. Let me know in the comments about any difficulties or different ways in which it could have been made easier. Thanks.

**_One last thing._**

React argues against this and they are pretty right about it. This is anti-pattern. So whenever you run into a situation like this, check to see if you could lift your state up or if there is any way you could break your component down. It might sound a wee bit tedious, but know that that’s the way it is supposed to be in React!

Happy Coding.

