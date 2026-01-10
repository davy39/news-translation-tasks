---
title: Straightforward code splitting with React and webpack
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-02-07T22:02:35.000Z'
originalURL: https://freecodecamp.org/news/straightforward-code-splitting-with-react-and-webpack-4b94c28f6c3f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*CNeQyaChrTh0H3ovOd9Dgg.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Didier FRANC

  Everything seemed perfect until your app size increased too fast …


  Introduction

  You’re a big fan of React and even bigger fan of the modern JavaScript development
  stack. React, Redux, ES6, Babel, and webpack are your favorite toys, s...'
---

By Didier FRANC

#### Everything seemed perfect until your app size increased too fast …

![Image](https://cdn-media-1.freecodecamp.org/images/1*CNeQyaChrTh0H3ovOd9Dgg.png)

### Introduction

You’re a big fan of **React** and even bigger fan of the modern JavaScript development stack. React, Redux, ES6, Babel, and webpack are your favorite toys, so don’t they have any secrets for you? Sure they do — which you’ll see after you read the following.

This post does not aim to be exhaustive, but will describe a straightforward and modern method to solve a problem related to the way we like to code.

### The problem

Here is a good example. As you can see, webpack created two JavaScript files: **_bundle.js_** and _vendor.js_. It’s the first step of code splitting, separating your vendors from your own code. This is well-documented in the [new webpack documentation.](https://webpack.js.org/guides/code-splitting-libraries/)

![Image](https://cdn-media-1.freecodecamp.org/images/1*u1CSFKmreuN4KjulOJFZAg.png)
_Type **yarn build** and you’ll see the tragedy …_

It’s a prerequisite for the next steps. Sharing vendors such as React and Redux with all your components is essential. But as you can see, our app size is close to ~2MB without its images, fonts, and other assets. Our app will take seconds to load and even more with a crappy mobile connection. Why don’t we split it into multiple chunks, which will load only when we need it? Easier said than done.

### Where to start ?

There are many ways when you care about speed and performance: one of them is Server Side Rendering, but it’s not the subject today ?.

In this article, we’re exploring code splitting with webpack, and the best place to start is [the webpack repo itself](https://github.com/webpack/webpack/tree/master/examples). There are other solutions as well. That being said, we have to make a choice.. And the winner is … `import()` (formerly named `System.import()`)**_._** I call it the “modern way”.

[**System.import has been deprecated.**](https://medium.com/@cerny.mrtn/system-import-has-been-deprecated-6806b2f506d)  
[medium.com](https://medium.com/@cerny.mrtn/system-import-has-been-deprecated-6806b2f506d)

#### 1. Be smart

There is no magic tool, and to get the best compromise you’ll probably have to use your brain ?. For example, vendor.js shouldn’t contain every library, only those which are “global” like React, Redux, or moment.

![Image](https://cdn-media-1.freecodecamp.org/images/1*KHjkCbjOTrCwaUSdMabdAw.png)
_This is not **package.json**_

#### 2. Start code splitting (the real one)

Loading a component (or any ES module) this way will be interpreted as a split point by webpack.

Now, imagine we have the following at the root of our app. The problem is the `Home` component. With its exotic library, it is relatively big compared to the rest of the app. Reminder: for now everything is packed in the same bundle and loaded at the same time.

Let’s create a simple wrapper component which will asynchronously load and render our Home component. It will be loaded only when you’re logged in.

We can make it even simpler by standardizing this method. I externalized it as the tiny [react-code-splitting](https://github.com/didierfranc/react-code-splitting). And the final result is visible here:

If you want to see this snippet in context, have a look at [redux-react-starter](https://github.com/didierfranc/redux-react-starter/blob/master/src/components/App.js#L12).

#### **3. Output**

As you can see, webpack created a new file named **_0.[chunkhash].js._** It’s our old bro Home ?.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Fef7AyiO4ZCxS6gYp0knJg.png)
_The result from [didierfranc/redux-react-starter](https://github.com/didierfranc/redux-react-starter" rel="noopener" target="_blank" title=")_

#### 4. Enjoy the benefits

As you can see, the **Home** component (0.bf87aaa616cea4a1ed40.js) was loaded on demand, just after I logged in. Note that performance will be even better if you take [care with caching](https://webpack.js.org/guides/caching/) and http/2. You can make [Lighthouse Report](http://react.didierfranc.com/lighthouse.html) your favorite tool to benchmark your app performance.

![Image](https://cdn-media-1.freecodecamp.org/images/1*F4WvfKTOqiQKBw1MbKVmgw.png)
_Chrome &gt; DevTools &gt; Network Tab_

### What’s next ?

Don’t hesitate to explore long term caching, offline capabilities, and so on. To put it simply: **how to make a progressive web application,** again and again.

You don’t want to miss any of my articles _? follow me on twitter [@DidierFranc](http://twitter.com/didierfranc)_

