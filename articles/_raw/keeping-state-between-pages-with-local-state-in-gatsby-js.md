---
title: How to keep state between pages with local state in Gatsby.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-14T14:56:02.000Z'
originalURL: https://freecodecamp.org/news/keeping-state-between-pages-with-local-state-in-gatsby-js
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/gatsby1.jpeg
tags:
- name: Gatsby
  slug: gatsby
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Thomas Weibenfalk


  Cover Photo by Anas Alshanti on Unsplash


  The “problem”

  When using the static site generator Gatsby you don’t have a base “App” component
  to play with. That said, there’s no component that wraps around your whole application
  whe...'
---

By Thomas Weibenfalk

> Cover Photo by [Anas Alshanti](https://unsplash.com/photos/feXpdV001o4?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/search/photos/development-code?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

## **The “problem”**

When using the static site generator Gatsby you don’t have a base “App” component to play with. That said, there’s no component that wraps around your whole application where you can put your state that needs to be kept between routes/pages. Gatsby.js automatically (or automagically?) creates routes to pages you put in your page folder of your installation. Or, you create pages programmatically from your **gatsby-node.js** file.

This will get us in trouble if we need, for example, a menu that should be visible and available for interaction on all our page routes. In my case, I had a mail form menu that could be shown or hidden in the right lower corner of my application. This component has a local state that will decide if the component is being shown or not. The below image shows the menu closed and opened.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/gatsby2.jpeg)

So… this is our problem. How can we tackle it? There’s a number of ways to deal with this but one way, and the approach I took, is described below.

## **The Solution**

I’ll go straight to the point. Gatsby has a file that’s named **gatsby-browser.js. We can use this file to make components wrap around our complete App and pages!**

This is great!

This file lets us use the Gatsby **Browser API.** This API contains several useful functions but there’s one in particular that will fit our needs. It’s called **wrapPageElement.** Check out the code below. This is the actual code I used for my client’s app.

```js
// gatsby-browser.js
// Import the component at the top of the file
import MailWidgetWrapper from './src/components/MailWidgetWrapper';

export const wrapPageElement = ({ element, props }) => (
  <MailWidgetWrapper {...props}>{element}</MailWidgetWrapper>
);
```

Here, I’ve created a wrapper component that will be available on all the routes and pages in Gatsby. That’s Awesome! And just what we need. The **wrapper component** looks like this:

```js
// MailWidgetWrapper.js
import React from 'react';

import MailWidget from './MailWidget';

const MailWidgetWrapper = ({ children }) => (
  <>
    {children}
    <MailWidget />
  </>
);

export default MailWidgetWrapper;
```

This is a really simple React Component who’s only function is to wrap our app and provide it with the MailWidget component. But how does **wrapPageElement** work?

## wrapPageElement

First, I also highly recommend using gatsbyjs.org as much as you can for finding answers to anything regarding Gatsby. The site is excellent and full of really good and thorough explanations of most problems you will encounter.

In our case, if you look at the code above, we have two parameters that get created for us in the `wrapPageElement` callback function: **element and props.** 

You should be familiar with props if you use React so they need no further introduction. In this case, the props are used by the page we’re currently on. We don’t need to use any of these props, as we only need to use the children (automatically created by React) prop. 

The `MailWidgetWrapper` just renders the children and the `MailWidget`. The children are the page we’re sending into the `MailWidgetWrapper` component from the **gatsby-browser.js** file, as shown below. The actual page lives in the **element** parameter and that’s the one we’re sending in with the expression `{element}`.

```js
<MailWidgetWrapper {…props}>{element}</MailWidgetWrapper>
```

So in short, the parameters we get from `wrapPageElement` can be summarized:

**The props parameter are the props from the actual page we’re on. And the element parameter is the actual page we’re on**

## The MailWidget Component

My actual `MailWidget` component is quite large and has a lot of code that’s not relevant here. That’s why I'm just showing you a simple scaffolded example version of a `MailWidget` component below. This component is not actually relevant for the task of explaining the `wrapPageElement` function.

The component can virtually be anything you like and has nothing to do with the implementation above. In my case it’s a `MailWidget`. It’s all up to you and what stateful component/s you need to be available on all your page routes.

```js
// MailWidget.js
import React, { useState } from 'react';

const MailWidget = () => {
  const [isVisible, setIsVisible] = useState(false);

  const toggleVisible = () => {
    setIsVisible(!isVisible);
  };

  return (
    <div className={isVisible ? 'visible' : ''}>
      <button type="button" onClick={toggleVisible}>
        Hide/Show MailWidget
      </button>
      <h1>Hello, I'm your mailwidget</h1>
    </div>
  );
};
export default MailWidget;
```

By the way, I’m all in on Hooks. I love Hooks and will use them in everything I do in React! That’s why I created my state with the `useState` hook in this one. The component above just uses a local state to decide if it should show itself or not.

## Conclusion

There you have it! Hopefully, you’ve learned that it’s not difficult to have a component keeping its state between pages in Gatsby. And we all love Gatsby.js don’t we? ?

Also, thank you for reading this post. I’m a Developer from Sweden that loves to teach and code. I also create courses on React and Gatsby online. You can find me on Udemy. Just search for Thomas Weibenfalk or hook me up on Twitter **@weibenfalk**  
I also have a Youtube channel were I teach free stuff, check it out [**here**](https://www.youtube.com/channel/UCnnnWy4UTYN258FfVGeXBbg)**.**

