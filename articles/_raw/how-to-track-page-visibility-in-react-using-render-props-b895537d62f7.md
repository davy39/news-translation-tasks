---
title: How to track page visibility in React using render props
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-05T22:40:51.000Z'
originalURL: https://freecodecamp.org/news/how-to-track-page-visibility-in-react-using-render-props-b895537d62f7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*WsI4NrSVmdM-xjYDPa-Wgw.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: Render Props
  slug: render-props
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Soumyajit Pathak

  In this article, we will create a simple reusable React component that tracks “Page
  Visibility State.”

  When creating a web application you may come across situations where you need to
  track the current visibility state of the app....'
---

By Soumyajit Pathak

In this article, we will create a simple reusable React component that tracks “Page Visibility State.”

When creating a web application you may come across situations where you need to track the current visibility state of the app. You may need to play/pause a video or animation effect, throttle some performance intensive work or simply track the user’s behaviour for analytics based on whether the browser tab is active or not.

Now, this feature seems pretty simple to implement until you actually try to implement it for the first time. It turns out tracking whether the user is actively interacting with the web application or not can be quite tricky.

There is a Page Visibility API which works fine for most cases, but it does not handle all the possible cases of browser tab inactivity. The [**Page Visibility API**](https://developer.mozilla.org/en-US/docs/Web/API/Page_Visibility_API) that sends a `visibilitychange` event to let listeners know that the visible state of the page has changed, or has some irregularities. It doesn't fire the event in some of the cases even when the window or concerned browser tab is out of sight or out of focus.

To handle some of these edge cases, we need to use a combination of `focus` and `blur` event listeners on both the `document` and the `window` element. You can find a detailed discussion about it [here](https://stereologics.wordpress.com/2015/04/02/about-page-visibility-api-hidden-visibilitychange-visibilitystate/).

We will implement the workaround logic described in the tutorial mentioned above in a small React app. Don’t worry you can read it later — we will explain every aspect of the logic that we will be using.

[**CodeSandbox**](https://codesandbox.io/embed/81x9n78qmj)  
[_CodeSandbox is an online editor tailored for web applications._codesandbox.io](https://codesandbox.io/embed/81x9n78qmj)

If you want to dive into the code or watch the demo, it is available on [**Codesandbox**](https://codesandbox.io/s/81x9n78qmj) as well as [**Github**](https://github.com/drenther/react-page-visibility-example).

### Getting Started

![Image](https://cdn-media-1.freecodecamp.org/images/1*SZoc6eC41JBxJSQ_xODPrA.gif)
_The video pauses when it is in the background_

We will use Codesandbox to bootstrap our React application (you can use **create-react-app** as well). We will create a small app that will have an HTML5 Video element that will play only when the browser tab is in focus or active otherwise it will be paused automatically. We are using a video because it will make testing our app’s functionality easy.

Let’s start by creating the simplest piece i.e. the `Video` component. It will be a simple component that will receive a Boolean props named `active` and a String props named `src` that will hold the URL for the video. If the `active` props is true, then we will play the video. Otherwise we will pause it.

We will create a simple React class component. We will render a simple video element with its source set to the URL passed using the `src` props, and we’ll use React's new `ref` API to attach a `ref` on the video DOM node. We will set the video to autoplay, assuming when we start the app the page will be active.

One thing to note here is that Safari now doesn't allow auto-playing media elements without user interaction. The `componentDidUpdate` lifecycle method is very handy in handling side effects when a component's props change. Therefore, here we will use this lifecycle method to play and pause the video based on the current value of `this.props.active`.

Browser vendor prefix differences are very annoying to deal with when using certain APIs, and the Page Visibility API is certainly one of them. Therefore, we will create a simple utility function that will handle these differences and return us the compatible API based on the user’s browser in a uniform manner. We will create and export this small function from **pageVisibilityUtils.js** under the **src** directory.

In this function, we will utilize simple if-else statement based control flow to return the browser-specific API. You can see we attached the **ms** prefix for Internet Explorer and **webkit** prefix for Webkit browsers. We will store the correct API in `hidden` and `visibilityChange` string variables and return them from the function in the form of a simple object. Lastly, we will export the function.

Next, we move onto our main component. We will encapsulate all of our Page Visibility tracking logic in a reusable React class component by leveraging the **Render Props** pattern. We will create a class component called `VisibilityManager`. This component will handle the adding and removing of all the DOM based event listeners.

We will start by importing the utility function we created earlier and invoking it to get the correct browser specific APIs. Then, we will create the React component and initialize its state with a single field `isVisible` set to `true`. This Boolean state field will be responsible for reflecting our page visibility state.

In the component's `componentDidMount` lifecycle method, we will attach an event listener on the document for the `visibilitychange` event with the `this.handleVisibilityChange` method as its handler. We will also attach event listeners for the focus and blur events on the document as well as the window element. This time we will set `this.forceVisibilityTrue` and `this.forceVisibilityFalse` as the handlers for the focus and blur events, respectively.

Next, we will create the `handleVisibilityChange` method that will accept a single argument `forcedFlag`. This `forceFlag` argument will be used to determine whether the method is called because of the `visibilitychange` event or the focus or blur events. This is so because the `forceVisibilityTrue` and `forceVisibilityFalse` methods do nothing but call the `handleVisibilityChange` method with true and false value for the `forcedFlag` argument.

Inside the `handleVisibilityChange` method, we first check whether the `forcedFlag` argument value is a Boolean (this is because if it is called from the `visibilitychange` event handler, than the argument passed on will be a [**SyntheticEvent**](https://reactjs.org/docs/events.html) object).

If it is a Boolean then we check if it's true or false. When it's true we called the `setVisibility` method with true otherwise we call the method with false as an argument. The `setVisibility` method leverages `this.setState` method to update `isVisible` field's value in the component's state.

But, if the `forcedFlag` is not a Boolean, then we check the hidden attribute value on the document and call the `setVisibility` method accordingly. This wraps up our Page Visibility State tracking logic.

To make the component reusable in nature, we use the Render Props pattern. That is, instead of rendering a component from the `render` method, we invoke `this.props.children` as a function with `this.state.isVisible`.

Lastly, we mount our React app to the DOM in our **index.js** file. We import our two React components `VisibilityManager` and `Video` and create a small functional React component `App` by composing them. We pass a function as the children of the `VisibilityManager` component that accepts `isVisible` as an argument and passes it to the `Video` component in its return statement. We also pass a video URL as `src` props to the `Video` component. This is how we consume the Render Props based `VisiblityManager` component. Finally, we use `ReactDOM.render` method to render our React app on the DOM node with id "root".

### Conclusion

Modern browser APIs are getting really powerful and can be used to do amazing things. Most of these APIs are imperative in nature and can be tricky to work with sometimes in React’s declarative paradigm. Using powerful patterns like Render Props to wrap these APIs into their own reusable React components can be very useful.

_Originally published at [able.bio](https://able.bio/drenther/track-page-visibility-in-react-using-render-props--78o9yw5)._

