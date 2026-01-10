---
title: How to work with React the right way to avoid some common pitfalls
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-30T21:35:35.000Z'
originalURL: https://freecodecamp.org/news/how-to-work-with-react-the-right-way-to-avoid-some-common-pitfalls-fc9eb5e34d9e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*s5pDmyXqPnXV0sNmgGCIxw.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Adeel Imran


  _Photo by [Unsplash](https://unsplash.com/@swimstaralex?utm_source=ghost&utm_medium=referral&utm_campaign=api-credit">Alexander
  Sinn / <a href="https://unsplash.com/?utm_source=ghost&utm_medium=referral&utmcampaign=api-credit)

  One thi...'
---

By Adeel Imran

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-251.png)
_Photo by [Unsplash](https://unsplash.com/@swimstaralex?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Alexander Sinn</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

One thing I hear quite often is “**Let’s go for Redux**” in our new React app. It helps you scale, and the App data shouldn’t be in React local state because it is inefficient. Or when you call an API and while the promise is pending, the component get unmounted and you get the following beautiful error.

> Warning: Can’t call setState (or forceUpdate) on an unmounted component. This is a no-op, but it indicates a memory leak in your application. To fix, cancel all subscriptions and asynchronous tasks in the componentWillUnmount method.

So the solution people usually arrive at is using **Redux**. I love Redux and the work that [**Dan Abramov**](https://twitter.com/dan_abramov) is doing is simply **incredible!** That dude rocks big time — I wish I was as half talented as he is.

But I am sure that when Dan made Redux, he was just giving us a tool in our tool-belt as a helper. It’s not the Jack of all tools. You don’t use a hammer when you can screw the bolt with a screw driver.

[**Dan even agrees**](https://twitter.com/dan_abramov)**.**

I love React, and I have been working on it for almost two years now. So far, no regrets. Best decision ever. I like Vue and all the cool library/frameworks out there. But React holds a special place in my heart. It helps me focus on the work that I am suppose to do rather then taking up all my time in DOM manipulations. And it does this in the best and most efficient way possible. with its [effective reconciliation](https://github.com/acdlite/react-fiber-architecture).

I have learned a lot over these past few years, and I’ve noticed a common problem among new and experienced React developers alike: not using React the right way when dealing with subscription or asynchronous tasks. I feel that the documentation out there isn’t well put up in this case, and so I decided to write this article.

I’ll talk about subscriptions first, and then we’ll move on to handling asynchronous task cancellation to avoid memory leaks in React (the main purpose of this article). If not handled, this slows our app down.

![Image](https://cdn-media-1.freecodecamp.org/images/1*pHRQWgW6YXlirkX3BTXKeQ.jpeg)
_Let’s clear all subsciptions/async tasks, and as a reminder don’t go in the direction of Mordor_

Now let’s get back to that beautiful error message that we initially talked about:

> Warning: Can’t call setState (or forceUpdate) on an unmounted component. This is a no-op, but it indicates a memory leak in your application. To fix, cancel all subscriptions and asynchronous tasks in the componentWillUnmount method.

My goal for this article is to make sure that no one ever has to face this error and not know what to do about it again.

### What we’ll cover

* Clear subscriptions like setTimeout/setInterval
* Clear asynchronous actions when you call an XHR request using `fetch` or libraries like `axios`
* Alternate methods, some opinionated others deprecated.

Before I start, a huge shout out to [**Kent C Dodds**](https://twitter.com/kentcdodds), the coolest person on the internet right now. Thank you for taking the time & giving back to the community. His [Youtube **podcasts**](https://www.youtube.com/user/kentdoddsfamily) and egghead course on [**Advanced React Component Patterns**](https://egghead.io/courses/advanced-react-component-patterns) are amazing. Check these resources out if you want to take the next step in your React skills.

I asked Kent about a better approach to avoid **setState** on component unmount so I could better optimize React’s performance. He went above and beyond and made a video on it. If you are a video kind of person, check it out below. It’ll give you a step by step walk through with a detailed explanation.

%[https://www.youtube.com/watch?v=8BNdxFzMeVg]

So now let’s jump in get started.

### 1: Clear Subscriptions

Let’s start off with the example:

%[https://codesandbox.io/s/m3rn84m7y9?from-embed]

Let’s talk what just happened here. What I want you to focus on is the `counter.js` file which basically increments the counter after 3 seconds.

This gives an error in 5 seconds, because I unmounted a subscription without clearing it. If you want to see the error again, just hit the refresh button in the CodeSandbox editor to see the error in the console.

I have my container file `index.js` which simply toggle’s the counter component after the first five seconds.

So

> — — — →Index.js

> — — — — → Counter.js

In my Index.js, I call Counter.js and simply do this in my render:

```
{showCounter ? <Counter /> : null}
```

The `showCounter` is a state boolean which set’s itself to false after the first 5 seconds as soon as the component mounts (componentDidMount).

The real thing which illustrates our problem here is the `counter.js` file which increments the count after every 3 seconds. So after the first 3 seconds, the counter updates. But as soon as it gets to the second update, which happens at the 6th second, the `index.js` file has already unmounted the counter component at the 5th second. By the time the counter component reaches it’s 6th second, it updates the counter for the second time.

It updates its state, but then here is the problem. There is no DOM for the counter component to update the state to, and that is when React throws an error. That beautiful error we discussed above:

> Warning: Can’t call setState (or forceUpdate) on an unmounted component. This is a no-op, but it indicates a memory leak in your application. To fix, cancel all subscriptions and asynchronous tasks in the componentWillUnmount method.

Now if you are new to React, you might say, “well **Adeel …** yeah but didn’t we just unmount the Counter component at the 5th second? If there is no component for counter, how can it’s state still update at the sixth second?”

Yes, you are right. But when we do something like `setTimeout` or `setInterval` in our React components, it is not dependent on or linked with our React class like you think it may be. It will keep on running after its specified condition unless or until you cancel it’s subscription.

Now you might already be doing this when your condition is met. But what if your condition hasn’t been met yet and the user decides to change pages where this action is still happening?

The best way to clear these kinds of subscriptions is in your `componentWillUnmount` life cycle. Here is an example how you can do it. Check out the counter.js file’s componentWillUnmount method:

%[https://codesandbox.io/s/xr7j5507qp?from-embed]

And that is pretty much it for `setTimout` & `setInterval`.

### 2: API (XHR) Aborts

* The Ugly Old Approach (Deprecated)
* The Good Newer Approach (The main purpose for this article)

So, we’ve discussed subscriptions. But what if you make an asynchronous request? How do you cancel it?

#### The old way

Before I talk about that, I want to talk about a deprecated method in React called `isMounted()`

Before December 2015, there was a method called `isMounted` in React. You can read more about it in the React [**blog**](https://reactjs.org/blog/2015/12/16/ismounted-antipattern.html)**.** What it did was something like this:

```javascript
import React from 'react'
import ReactDOM from 'react-dom'
import axios from 'axios'

class RandomUser extends React.Component {
  state = {user: null}
  _isMounted = false
  handleButtonClick = async () => {
    const response = await axios.get('https://randomuser.me/api/')
    if (this._isMounted) {
      this.setState({ user: response.data })
    }
  }
  componentDidMount() {
    this._isMounted = true
  }
  componentWillUnmount() {
    this._isMounted = false
  }
  render() {
    return (
      <div>
        <button onClick={this.handleButtonClick}>Click Me</button>
        <pre>{JSON.stringify(this.state.user, null, 2)}</pre>
      </div>
    )
  }
}
```


For the purpose of this example, I am using a library called `axios` for making an XHR request.

Let’s go through it. I initially set `this_isMounted` to `false` right next to where I initialized my state. As soon as the life cycle `componentDidMount` gets called, I set `this._isMounted` to true. During that time, if an end user clicks the button, an XHR request is made. I am using `randomuser.me`. As soon as the promise gets resolved, I check if the component is still mounted with `this_isMounted`. If it’s true, I update my state, otherwise I ignore it.

The user might clicked on the button while the asynchronous call was being resolved. This would result in the user switching pages. So to avoid an unnecessary state update, we can simply handle it in our life cycle method `componentWillUnmount`. I simply set `this._isMounted` to false. So whenever the asynchronous API call gets resolved, it will check if `this_isMounted` is false and then it will not update the state.

This approach does get the job done, but as the React docs say:

> The primary use case for `isMounted()` is to avoid calling `setState()` after a component has unmounted, because calling `setState()` after a component has unmounted will emit a warning. The “setState warning” exists to help you catch bugs, because calling `setState()` on an unmounted component is an indication that your app/component has somehow failed to clean up properly. Specifically, calling `setState()` in an unmounted component means that your app is still holding a reference to the component after the component has been unmounted - which often indicates a memory leak! [Read More …](https://reactjs.org/blog/2015/12/16/ismounted-antipattern.html)

This means that although we have avoided an unnecessary setState, the memory still hasn’t cleared up. There is still an asynchronous action happening which doesn’t know that the component life cycle has ended and it is not needed anymore.

#### Let’s Talk About The Right Way

Here to save the day are [**AbortControllers**](https://developer.mozilla.org/en-US/docs/Web/API/AbortController). As per the [MDN](https://developer.mozilla.org/en-US/docs/Web/API/AbortController) documentation it states:

> The `**AbortController**` interface represents a controller object that allows you to abort one or more DOM requests as and when desired. [Read more ..](https://developer.mozilla.org/en-US/docs/Web/API/AbortController)

![Image](https://cdn-media-1.freecodecamp.org/images/1*CLnYV7AQDdgpS-LAQ6fLlg.jpeg)

Let’s look a bit more in depth here. With code, of course, because everyone ❤ code.

```javascript
var myController = new AbortController();
var mySignal = myController.signal;

var downloadBtn = document.querySelector('.download');
var abortBtn = document.querySelector('.abort');

downloadBtn.addEventListener('click', fetchVideo);

abortBtn.addEventListener('click', function() {
  myController.abort();
  console.log('Download aborted');
});

function fetchVideo() {
  ...
  fetch(url, { signal: mySignal }).then(function(response) {
    ...
  }).catch(function(e) {
    reports.textContent = 'Download error: ' + e.message;
  })
}
```

First we create a **new AbortController** and assign it to a variable called `myController`. Then we make a **signal** for that AbortController. Think of the signal as an indicator to tell our XHR requests when it’s time to abort the request.

Assume that we have 2 buttons, `Download` and `Abort` . The download button downloads a video, but what if, while downloading, we want to cancel that download request? We simply need to call `myController.abort()`. Now this controller will abort all requests associated with it.

How, you might ask?

After we did `var myController = new AbortController()` we did this `var mySignal = myController.signal` . Now in my fetch request, where I tell it the URL and the payload, I just need to pass in `mySignal` to link/signal that `FETCh` request with my awesome `AbortController`.

If you want to read an even more extensive example about `AbortController`, the cool folks at **MDN** have this really nice and elegant example on their Github. You can check it out [here](https://github.com/mdn/dom-examples/blob/master/abort-api/index.htm).

I wanted to talk about these abort requests was because not many people are aware of them. The request for an abort in fetch started in 2015. Here’s the [Original GitHub Issue On Abort](https://github.com/whatwg/fetch/issues/27) — it finally got support around October 2017. That is a gap of two years. Wow! There are a few libraries like **axios** that give support for AbortController. I will discuss how you can use it with axios, but I first wanted to show the in-depth under-the-hood version of how AbortController works.

### **Aborting An XHR Request In Axios**



> “Do, or do not. There is no try.” — Yoda

The implementation I talked about above isn’t specific to React, but that’s what we’ll discuss here. The main purpose of this article is to show you how to clear unnecessary DOM manipulations in React when an XHR request is made and the component is unmounted while the request is in pending state. Whew!

So without further ado, here we go.

```javascript
import React, { Component } from 'react';
import axios from 'axios';

class Example extends Component {
  signal = axios.CancelToken.source();

  state = {
    isLoading: false,
    user: {},
  }
  
  componentDidMount() {
    this.onLoadUser();
  }
  
  componentWillUnmount() {
    this.signal.cancel('Api is being canceled');
  }
  
  onLoadUser = async () => {
    try {
      this.setState({ isLoading: true });
      const response = await axios.get('https://randomuser.me/api/', {
        cancelToken: this.signal.token,
      })
      this.setState({ user: response.data, isLoading: true });
    } catch (err) {
      if (axios.isCancel(err)) {
        console.log('Error: ', err.message); // => prints: Api is being canceled
      } else {
        this.setState({ isLoading: false });
      }
    }
   } 
   
    
    render() {
      return (
        <div>
          <pre>{JSON.stringify(this.state.user, null, 2)}</pre>
        </div>
      )
    }
 
}
```

Let’s walk through this code

I set `this.signal` to `axios.CancelToken.source()`which basically instantiates a new `AbortController` and assigns the signal of that `AbortController` to `this.signal`. Next I call a method in `componentDidMount` called `this.onLoadUser()` which calls a random user information from a third party API `randomuser.me`. When I call that API, I also pass the signal to a property in axios called `cancelToken`

The next thing I do is in my `componentWillUnmount` where I call the abort method which is linked to that `signal`. Now let’s assume that as soon as the component was loaded, the API was called and the `XHR request went in a pending state`.

Now, the request was pending (that is, it wasn’t resolved or rejected but the user decided to go to another page. As soon as the life cycle method `componentWillUnmount` gets called up, we will abort our API request. As soon as the API get’s aborted/cancelled, the promise will get rejected and it will land in the `catch` block of that `try/catch` statement, particularly in the `if (axios.isCancel(err) {}` block.

Now we know explicitly that the API was aborted, because the component was unmounted and therefore logs an error. But we know that we no longer need to update that state since it is no longer required.

**P.S:** You can use the same signal and pass it as many XHR requests in your component as you like. When the component gets un mounted, all those XHR requests that are in a pending state will get cancelled when componentWillUnmount is called.

### Final details

Congratulations! :) If you have read this far, you’ve just learned how to abort an XHR request on your own terms.

Let’s carry on just a little bit more. Normally, your XHR requests are in one file, and your main container component is in another (from which you call that API method). How do you pass that signal to another file and still get that XHR request cancelled?

Here is how you do it:

```javascript
import React, { Component } from 'react';
import axios from 'axios';

// API
import { onLoadUser } from './UserAPI';

class Example extends Component {
  signal = axios.CancelToken.source();

  state = {
    isLoading: false,
    user: {},
  }
  
  componentDidMount() {
    this.onLoadUser();
  }
  
  componentWillUnmount() {
    this.signal.cancel('Api is being canceled');
  }
  
  onLoadUser = async () => {
    try {
      this.setState({ isLoading: true });
      const data = await onLoadUser(this.signal.token);
      this.setState({ user: data, isLoading: true });
    } catch (error) {
      if (axios.isCancel(err)) {
        console.log('Error: ', err.message); // => prints: Api is being canceled
      } else {
        this.setState({ isLoading: false });
      }
    }
  }
    
    render() {
      return (
        <div>
          <pre>{JSON.stringify(this.state.user, null, 2)}</pre>
        </div>
      )
    }
  };
 
}
```

```javascript
export const onLoadUser = async myCancelToken => {
  try {
    const { data } = await axios.get('https://randomuser.me/api/', {
      cancelToken: myCancelToken,
    })
    return data;
  } catch (error) {
    throw error;
  }
};
```

I hope this has helped you and I hope you’ve learned something. If you liked it, please give it some claps.

Thank you for taking the time out to read. Shout out to my very talented colleague [**Kinan**](http://kazmi@facebook.com) for helping me proof read this article. Thanks to **K[ent C Dodds](https://twitter.com/kentcdodds)** for being an inspiration in the JavaScript OSS community.

Again, I’d love to hear your feedback on it. You can always reach me out on [**Twitter**](http://twitter.com/adeelibr)**.**

Also there is [another amazing read](https://developers.google.com/web/updates/2017/09/abortable-fetch) on **Abort Controller** that I found through the **MDN** documentation by **Jake Archibald**. I suggest you read it, if you have a curios nature like mine.

