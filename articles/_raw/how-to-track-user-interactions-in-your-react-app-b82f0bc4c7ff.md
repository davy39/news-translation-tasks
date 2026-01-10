---
title: How to track user interactions in your React app
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-13T10:11:27.000Z'
originalURL: https://freecodecamp.org/news/how-to-track-user-interactions-in-your-react-app-b82f0bc4c7ff
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ZP7MCxvL4o34z5ku4zY_vw.jpeg
tags:
- name: analytics
  slug: analytics
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Faouzi Oudouh

  Worry not about which Analytics provider you need to gather user interaction within
  your app.

  Instead, worry more about how to gather these interactions.

  A few months ago, I was involved in an Analytics project within a large E-comme...'
---

By Faouzi Oudouh

Worry not about which Analytics provider you need to gather user interaction within your app.

Instead, worry more about how to gather these interactions.

A few months ago, I was involved in an Analytics project within a large E-commerce organization. This organization has a data-driven business where the analytics are more important than anything else.

We were building a Datalayer solution to hold all the user interactions and actions before pushing them to the Analytics provider (for example, Google Tag Manager). We built our DataLayer solution without having React in mind, as the migration to React started later.

### React Time!

We started the migration to React progressively, which means React was responsible only for rendering some parts of the platform. And I was responsible for integrating the DataLayer solution we had already built with React Land.

Suddenly, the difficulties started coming up:

* The solution was jQuery based
* It was unpredictable
* It was hard to test and maintain
* Sharing knowledge with other developers who didn’t have analytics experience was scary!

I started looking in the community for ready-to-use solutions that fit our needs. There was just no chance.

And here’s where the idea of [React-Tracker](https://github.com/faouzioudouh/react-tracker) came in.

Why [React-tracker](https://github.com/faouzioudouh/react-tracker)?

* It’s easy to use, test, and maintain (Redux-like)
* It can be used with any Analytics provider
* It’s scalable and predictible
* It has a minimal API

With React-tracker, we were easily able to integrate two Analytics providers (Google Tag manager and Adobe Analytics).

### How?

To keep it simple, _think of it as Redux_.

* Instantiate your Tracker ~ _Store of your events_
* Create your event-listener(s) ~ _Reducer_
* Event ~ _Action_
* Provide your tracker instance to your Root Component.
* React-tracker will [magically](https://reactjs.org/docs/context.html) take care of providing your tracker instance to all your Components.

Before instantiating anything, let’s go through each term on the list above and explain it.

#### What is Tracker?

A Tracker is a bag that holds the tracking-history along with some functions to listen to/dispatch events.

* `tracker.on(eventType, callback)` the given callback will be called whenever an event with `event.type` equal to the given `eventType` is dispatched.
* `tracker.trackEvent(event)` is a function that accepts an `event` and calls all the event-listeners that listen on this `event`.
* `tracker.getHistory()` returns an Array and contains all the tracked events that were saved

#### What is an Event?

An event is a plain object that represents the user interaction, like user click, page view, and purchase.

It should be an object with `type` and associated `data` if any. Here’s an example of a `PageView` event:

```
const PageViewEvent = {  type: 'PAGE_VIEW', // Required  data: { // Optional    pageId: '123',    userId: 'UID-123'  }}
```

#### What is the Event-listener?

The event-listener is a function that will be called if its `eventType` matched the type of the dispatched event.

`eventListener.eventType === event.type`

Example of an Event-listener:

```
const pageViewListener = (event, ) => {  // For example let's push the received event to our DataLayer.  window.dataLayer.push(event);
```

```
  return event;};
```

Let’s allow our `pageViewListener` to listen only on `PAGE_VIEW` event:

```
pageViewListener.eventType = 'PAGE_VIEW';
```

There are four things to notice here:

* Returning the event will save it in the trackingHistory. Otherwise it will be ignored :)
* If no `eventType` was specified to the event-listener, it will be called on every event dispatch.
* `eventHistory` was provided as a second parameter to help you apply restrictions on your events easily, like tracking a Product-click once. In order to achieve this, you need to have the history of events in your hands.
* Pushing our event to `window.dataLayer` was just an example. You can mainly do anything in this function like calling `GTM` directly or `Facebook Pixel`

### Time to combine everything

First things first:

#### 1. Instantiate our hero `Tracker:`

```
import { Tracker } from 'react-tracker';
```

```
const tracker = new Tracker();
```

That’s it!

Now we have our `Tracker` but with no event-listener :-(

There are two ways to add event-listeners to your `Tracker` :

* On instantiating:

```
const anOtherTracker = new Tracker([  pageViewListener,  productClickListener,  ...]);
```

* Or you can add the event-listener after instantiating your `Tracker` using `on`:

```
const anOtherTracker = new Tracker();
```

```
tracker.on('PAGE_VIEW', pageViewListener);
```

#### 2. Create a page view event-listener :

I want my event-listener to push the received `PAGE_VIEW` event directly to my `dataLayer.`

```
const pageViewListener = (event, trackingHistory) {
```

```
  window.dataLayer.push(event);
```

```
};
```

Let our `tracker` know about the `pageViewListener` :

```
tracker.on('PAGE_VIEW', pageViewListener);
```

#### 3. Create Event-creator :

Event-creator is just a function that returns an event object:

```
const pageViewEvent = (pageId, userId) => ({  type: 'PAGE_VIEW',  data: {    pageId,    userId  }});
```

**Our Tracker is well configured now.**

### Introducing our `tracker` to React

![Image](https://cdn-media-1.freecodecamp.org/images/5pYC8r-p6vhMiA9nRpopQDn4QK25YObvq7oG)
_Credit: [rawpixel.com](https://unsplash.com/photos/sHzMcXkJNrw" rel="noopener" target="_blank" title=")_

#### 4. Provide our `tracker` to the Root Component:

```
import React from 'react;import ReactDOM from 'react-dom';import { TrackerProvider } from 'react-tracker'
```

```
import RootComponent from '../RootComponent';
```

```
const RootComponentWithTracking = (  <TrackerProvider tracker={tracker}>    <RootComponent />  </TrackerProvider>);
```

```
const domElement = document.getElementById('root');
```

```
ReactDOM.render(<RootComponentWithTracking />, domElement);
```

By providing our `tracker` to the root component, it will be [magically](https://reactjs.org/docs/context.html) available for all the sub-components.

So now, since we have our `tracker` available, let’s use it to track the `PAGE_VIEW` event on the `RootComponent` mount.

#### 4. Track `Page View Event.`

```
import React from 'react';import { withTracking } from 'react-tracker';// We created this function earlier at (3.)import { pageViewEvent} from '../tracking/events';
```

```
class RootComponent extends React.Component {  componentDidMount() {    this.props.trackPageView(this.props.pageId, this.props.userId)  }
```

```
  render() {    return (<h1> My App is awesome </h1>)  }};
```

```
const mapTrackingToProps = trackEvent => ({  trackPageView: (pageId, userId) =>     trackEvent(pageViewEvent(pageId, userId))});
```

```
export default withTracking(mapTrackingToProps)(RootComponent);
```

`withTracking` HOC will take care of providing us `trackEvent` from our `tracker` so we can use it to track the `pageView` event.

`mapTrackingToProps` will merge the returned object with the `RootComponent` ’s props, which means the `trackPageView` will be available as a prop within `RootComponent.`

**That’s it — you’re done ;)**

#### 5. Demo

Please refer to this [demo](https://faouzioudouh.github.io/react-tracker/) and to [GitHub](https://github.com/faouzioudouh/react-tracker) for in-depth documentation and a better way to organize your tracking files.

### Give it a try!

[React-tracker](https://github.com/faouzioudouh/react-tracker) was built to facilitate the integration of Analytics tools as much as possible, by proving a minimal API and easy integration with your react app.

### Thanks

Thank you [doha faridi](https://www.freecodecamp.org/news/how-to-track-user-interactions-in-your-react-app-b82f0bc4c7ff/undefined), [AbdelAli Eramli](https://www.freecodecamp.org/news/how-to-track-user-interactions-in-your-react-app-b82f0bc4c7ff/undefined) and [khalid benrafik](https://www.freecodecamp.org/news/how-to-track-user-interactions-in-your-react-app-b82f0bc4c7ff/undefined) for your helpful feedback.

