---
title: How to write better tests for drag-and-drop operations in the browser
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-20T15:41:43.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-better-tests-for-drag-and-drop-operations-in-the-browser-f9a131f0b281
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0QbvXqleQASAZ0oaAfY66w.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: React
  slug: reactjs
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Ronald Rey

  While keeping it framework-agnostic


  _Photo by [Unsplash](https://unsplash.com/photos/SHCViKw3edE?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText"
  rel="noopener" target="_blank" title="">Ash Edmonds on <a href="https:...'
---

By Ronald Rey

#### While keeping it framework-agnostic

![Image](https://cdn-media-1.freecodecamp.org/images/1*0QbvXqleQASAZ0oaAfY66w.jpeg)
_Photo by [Unsplash](https://unsplash.com/photos/SHCViKw3edE?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Ash Edmonds</a> on <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

When it comes to common interactions between a user and a web application, it’s usually pretty straightforward to simulate those actions in a testing environment to assert the correct functionality of an app. I’m referring to things like clicking buttons, filling out forms, navigating routes… the usual stuff. However, there are some less common experiences in the Web that are much harder to test. One of these is drag-and-drop functionality.

This is partly because of just how broken and inconsistent the HTML5 Drag and Drop API is. This has led many library authors to whip out their own unique approaches to the problem, often very different from each other. This means that implementing such functionality alone in your app can be quite challenging, and for an unexperienced developer it might be even more challenging to write the proper automated tests for it.

> After spending about a day and a half in testing I am forced to conclude that the HTML5 drag and drop module is not just a disaster, it’s a f*****g disaster.  
>   
> - [Peter-Paul Koch](https://www.quirksmode.org/blog/archives/2009/09/the_html5_drag.html)

To my despair, the app I’m working on at the moment full-time has a lot of drag-and-drop related features all over the place. Thankfully, though, it has been fairly easy thanks to the rich ecosystem of libraries out there that have already tackled this problem and seem to have it nailed down.

However, automatically testing these features can be non-trivial, and I’d like to share some of the lessons I’ve learned. I’m using React, and a lot of the snippets and samples are going to be React centric. But in reality, the same concepts could be applied to any stack, which is the beauty of it all.

### The initial approach

Ok, so let’s say I need to build a table that has drag and droppable rows, looking something like this (by the way, don’t get too distracted by the implementation):

<iframe src="https://codesandbox.io/embed/github/reyronald/react-dnd-integration-testing-sample/tree/3f90cacea9f99fe7868daf00ffbccaa2611c87e3/?fontsize=14" title="react-dnd-integration-testing-sample" allow="geolocation; microphone; camera; midi; vr; accelerometer; gyroscope; payment; ambient-light-sensor; encrypted-media" style="width:100%; height:500px; border:0; border-radius: 4px; overflow:hidden;" sandbox="allow-modals allow-forms allow-popups allow-scripts allow-same-origin"></iframe>

![Image](https://cdn-media-1.freecodecamp.org/images/1*U6CwIMHmeOqoMJxOZke4sQ.gif)

As you can see, I’m using the classic `react-dnd` library by the now famous Dan Abramov. The feature is done, so how would we go about testing it at this point? If you go to the documentation, you would find a neat “[Testing” section that will probably make your eyes shine](http://react-dnd.github.io/react-dnd/docs-testing.html).

There’s a suggestion about using the “test backend”. Basically you wrap the decorated component using this backend instead of the usual HTML5 backend they provide. This will allow you to test it outside of a browser environment, that is, without access to the DOM.

So in that last sentence of the previous paragraph, I threw a lot of weird concepts at you: decorated component, backend, testing backend, HTML5 backend… what? These are all internal underlying concepts of `react-dnd` and `dnd-core`, all related to how it works under the hood. The linked guide itself admits this, and states that it is the least documented part of the library because of this.

Does this mean that I must be competently familiar with how this library in particular works to be able to test it? Well, to me, this is what the documentation is suggesting. This is tricky, because it can be misleading to unexperienced developers.

In summary, I have a few gripes about their suggested approach:

1. To test this feature, I must be familiar with how this library in particular works internally and its implementation details.
2. To test this feature, I must also be familiar with how the “testing backend” works, which is something that I don’t have to be familiar with in the first place to build a drag-and-drop functionality using this library. That means I have yet another set of documentation to consume, and a whole other dimension of issues I could run into that are not necessarily shared with the regular HTML5 backend I would use for my app.
3. The fact that I have a comprehensive passing test suite using this approach doesn’t necessarily guarantee for me that it actually works as I expect from the user’s perspective. Think about it: in my tests and in the wild, the functionality would be working with completely different internals. And despite the maintainers’ best intentions, this approach doesn’t necessarily scale well to the rest of the JS ecosystem, and can give you a false sense of security.
4. If I ever decide to change the approach to the functionality and use another library instead, or write it myself, all of my tests will suddenly become obsolete and I’ll have to rewrite them all over again.

Now, don’t get me wrong — it’s great that they’ve gone to such lengths to create a “testing backend” so that the functionality can be tested without the DOM. That is certainly useful and does have its place. But it’s not something I would recommend because of the issues I just listed.

What I’m after is the following:

1. A suite of tests that will guarantee to the highest degree that the functionality works as expected (not possible to reach 100% of certainty without end-to-end tests, not what I’m focusing on at the moment). This means that I want to assert the exact behavior of the functionality from the user’s perspective in my tests.
2. I can swap or change the implementation of the feature (that includes any library used underneath) at any time with minimal impact to the tests.
3. I don’t have to be familiar with the implementation of the functionality to write the tests.
4. I only have to use my already existing and familiar knowledge of the Web and Web APIs in general to write these tests.

### Moving foward

What would I recommend then? Well, just emulate in your tests what a user would do when using the app. Basically I’m advocating that you write full-fledged integration tests for this feature instead of unit-like / isolated tests, like the documentation suggests.

Nowadays we have [jsdom](https://github.com/jsdom/jsdom) which allows us to fire up a high-fidelity browser environment in-memory, without using an actual browser. Honestly `jsdom` has become so good over the years that I almost can’t see any reasons to write any web application tests that try to not use or access the DOM. Virtually anything you can do in a browser developer console can be done in-memory with `jsdom`, with some exceptions and caveats of course, which we will see shortly.

_DISCLAIMER: I’m not saying that you should never write unit tests, or tests in this way. Certainly every scenario and problem is different. Put on your thinking cap and decide what’s best on a case-by-case basis!_

Ok so, how do we do it? Simple, just ask yourself the question: what would the user do with my application to use the drag-and-drop feature, and how does the browser behave when it happens? When you have that answer, just code that up in a test using regular DOM APIs made accessible to you by `jsdom`! Let’s see how a test for a dragging downward action would look for our particular example using `jest`:

```js
const getTableCells = () =>
  Array.from(mountNode.querySelectorAll("tr td:nth-of-type(1)"));
const createBubbledEvent = (type, props = {}) => {
  const event = new Event(type, { bubbles: true });
  Object.assign(event, props);
  return event;
};
const tableCells = getTableCells();
const startingNode = tableCells[0];
const endingNode = tableCells[2];
startingNode.dispatchEvent(
  createBubbledEvent("dragstart", { clientX: 0, clientY: 0 })
);
endingNode.dispatchEvent(
  createBubbledEvent("drop", { clientX: 0, clientY: 1 })
);
expect(getTableCells().map(cell => cell.textContent)).toEqual([
  "Bob",
  "Clark",
  "Alice",
]);
```

There’s absolutely nothing `react-dnd` or even React-related in that snippet, and it’s not even using React Test Utils’ Simulate either. That means that I could even change my UI library/framework altogether for something like Angular (heck, even Backbone, anyone?) and this test will still make sense and work as expected.

That alone is sufficient to properly test that subset of the functionality, however, there are a lot other events that happen in an actual browser (`mousedown`, `mousemove`, `dragend`, etc.) that just didn’t happen to play a role in our implementation. This means that with a different implementation, it’s possible that the test would require a few things added or removed.

(By the way, Simulate usage is openly discouraged by industry experts. Also, if you’ve spent any more than 5 minutes in any of Enzyme’s event system related GitHub issues, you will see the same opinion by the authors themselves there. [There has even been comments about its removal in upcoming versions](https://github.com/airbnb/enzyme/issues/1357#issuecomment-404673556)).

%[https://twitter.com/dan_abramov/status/980807288444383232?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed&ref_url=https%3A%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Ftype%3Dtext%252Fhtml%26key%3Da19fcc184b9711e1b4764040d3dc5c07%26schema%3Dtwitter%26url%3Dhttps%253A%2F%2Ftwitter.com%2Fdan_abramov%2Fstatus%2F980807288444383232%26image%3Dhttps%253A%2F%2Fi.embed.ly%2F1%2Fimage%253Furl%253Dhttps%25253A%25252F%25252Fpbs.twimg.com%25252Fprofile_images%25252F906557353549598720%25252FoapgW_Fp_400x400.jpg%2526key%253Da19fcc184b9711e1b4764040d3dc5c07]

The only few things that are not necessarily evident are:

* The events have to bubble, which is not the default when we create them manually with the constructor — so we need to set it explicitly. This is related to how the React’s event delegation system works. You might think that’s an implementation detail, but that’s not necessarily the case. Events do bubble up in the browser when triggered by actual real interaction anyway.
* We need to set the `clientX` and `clientY` properties of the event, because they are used to determine the direction of the dragging. Again, with other implementation, there might be other properties on the events or other methods that you’ll have to patch to make it work (like `.getBoundingClientRect()`). For instance, if the implementation was using something like `.offsetX`, `.movementX`, `.top` or any other size, position, and movement related properties.

And that’s about it. We’ve addressed all of my issues and achieved all the goals we set out for ourselves. With a few more lines of code, it’s possible to take the test coverage of this repo to a 100% fairly easy.

![Image](https://cdn-media-1.freecodecamp.org/images/1*86rgI6XsYdNw7lRs16Fz_w.png)
_Isn’t it beautiful?_

### Final thoughts

Feel free to explore the entire test suite [here](https://codesandbox.io/s/github/reyronald/react-dnd-integration-testing-sample). A few additional things are in place to get the coverage to 100%, so make sure to check it out. Note that I wrote everything in a single test just for the sake of brevity.

Something else I’d like to mention. A new developer could come into the code for the tests and know exactly what’s going on. Imagine if the tests were using the `react-dnd` oriented tests, using all kinds of internal concepts and details… that would be a huge wall in their face and could pose a substantial obstacle to their ability to contribute to the tests in a timely manner. At that point they would have to go read the `react-dnd` documentation, `dnd-core` and `react-testing-backend`’s source code… yikes!

I want to leave you with this blog post by Sophie Alpert, manager of the React Core Team at Facebook, describing how they could successfully ship an API-compatible complete rewrite of React internals from version 15 to version 16 safely without a single breaking change. Spoiler alert: the comprehensive test suites asserted the functionality of the library from an outsider’s perspective, instead of focusing on implementation details or isolated unit tests.

What’s really funny about it is that as of July 2018, all of the snippets from the official React documentation were using an outdated 0.14 version, and it turned out they worked exactly the same in version 16.x. This just goes to show what a great job they’ve done maintaining backwards compatibility, and that would not have been possible without those well written and focused tests!

[**React 16: A look inside an API-compatible rewrite of our frontend UI library**](https://code.fb.com/web/react-16-a-look-inside-an-api-compatible-rewrite-of-our-frontend-ui-library/)  
[_POSTED ON TO Web React 16: A look inside an API-compatible rewrite of our frontend UI library React makes it simple to…_](https://code.fb.com/web/react-16-a-look-inside-an-api-compatible-rewrite-of-our-frontend-ui-library/)  
[code.fb.com](https://code.fb.com/web/react-16-a-look-inside-an-api-compatible-rewrite-of-our-frontend-ui-library/)

%[https://twitter.com/dan_abramov/status/1017409804308905986?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed&ref_url=https%3A%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Ftype%3Dtext%252Fhtml%26key%3Da19fcc184b9711e1b4764040d3dc5c07%26schema%3Dtwitter%26url%3Dhttps%253A%2F%2Ftwitter.com%2Fdan_abramov%2Fstatus%2F1017409804308905986%26image%3Dhttps%253A%2F%2Fi.embed.ly%2F1%2Fimage%253Furl%253Dhttps%25253A%25252F%25252Fpbs.twimg.com%25252Fprofile_images%25252F906557353549598720%25252FoapgW_Fp_400x400.jpg%2526key%253Da19fcc184b9711e1b4764040d3dc5c07]

### Bonus: Some tips on how to figure out how to emulate browser behavior

If there’s some other functionality that you want to test in this way, but you are not sure exactly how the browser behaves when making it happen, I suggest you look into [Google Chrome’s `monitorEvents` API](https://developers.google.com/web/tools/chrome-devtools/console/events). It’s insanely helpful in these scenarios, specially when you are not sure what’s going on. I myself used it like this to explore the shape of the events fired when drag-and-dropping:

```
monitorEvents(document.body, [
  'mousedown',

  'mousemove',

  'dragstart',

  'dragenter',

  'dragover',

  'drop',

  'dragend',

  'mouseup',
  
  // …
  
])
```

In general, it would be extremely beneficial if you just whip out a browser developer console, and start playing around with the event system until you feel confident you know how it works. Create elements, trigger events, move them around, attach them to the DOM, detach them, etc.… anything it takes! Investing one or a few hours with this will serve you for the rest of your career as a web developer. Pretty sweet deal in my eyes :)

