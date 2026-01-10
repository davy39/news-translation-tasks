---
title: How to set up performance and user tracking in React with Google Analytics
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-31T18:37:30.000Z'
originalURL: https://freecodecamp.org/news/performance-and-user-tracking-in-react-with-google-analytics
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/guillaume-fischer--JPCZcxeqzM-unsplash.jpg
tags:
- name: Google Analytics
  slug: google-analytics
- name: React
  slug: react
- name: web performance
  slug: web-performance
seo_title: null
seo_desc: 'By Mohammad Iqbal

  Keeping track of your users and your app performance is a very crucial part of modern
  web development. You may have seen reports of companies increasing revenues by simply
  decreasing the load time of their app by a few hundred milli...'
---

By Mohammad Iqbal

Keeping track of your users and your app performance is a very crucial part of modern web development. You may have seen reports of companies increasing revenues by simply decreasing the load time of their app by a few hundred milliseconds. 

Keeping track of your user behavior is also crucial. This will allow you to modify and build your app according to your users' preferred way of interacting with your app, resulting in happier users and more traffic to your site.  

Here is the completed project: 

[https://github.com/iqbal125/react-hooks-google-analytics](https://github.com/iqbal125/react-hooks-google-analytics)

In this guide I'll give you a complete foundational guide to tracking both performance and user behavior. By the end of the tutorial you will have everything you need to build complex user and performance tracking setups. 

> Follow Me on Twitter for more tutorials in the future: [https://twitter.com/iqbal125sf](https://twitter.com/iqbal125sf)

## Table of Contents

1. Intro
2. Google Analytics
3. Tracking Pages Views
4. Tracking Load Performance
5. Tracking Rendering Performance
6. Tracking Paint
7. Tracking Scroll
8. Tracking Events
9. Quick Performance Tips and Heuristics

## Intro

I will show you the performance metrics for the development build of react to keep this tutorial concise. But in a real world situation do not test the dev version, because it contains a lot of error handling code and lack of optimizations that will give you highly skewed results. 

For this reason it is better to test on the build production version to establish some baseline metrics. 

Also, for the sake of brevity I will just refer to Google Analytics as GA. 

GA also doesn't work with local host. To get a simulation of what you might be sending to GA without actually sending it and messing up your analytics, you can just substitute a console.log wherever you plan on putting your GA hit. 

`ReactGA`  is the global function and is known as the command queue because it does not execute commands immediately but adds commands to a queue and then sends them asynchronously. This does not tie up the main thread and does not lead to your tracking code harming your app performance. 

A hit is when a GA tracker sends data to Google Analytics. 

We will mainly be focusing on the React code in this tutorial, there are far better other tutorials to learn how to use GA.  

There are 3 main functions we will use when sending hits to GA. You should know there are more but we will just focus on these 3 for the purposes of this tutorial. 

`GAReact.pageview()`: will pass in a string that contains the route. 

`GAReact.timing()`: Will take an object as a parameter. Will contain information related to our performance metrics which we will see below. The fields will be `category`, `variable`, `value` and `label`. Notice that only the value property will be coming from our app the rest of the properties are user defined.

`GAReact.event()`: Will take an object as a parameter. Will contain data about events that take place in the app (form submit, button click, etc.)  Will have fields of `category`, `action`, `label` and `value`. Note that only the value is going to come from the app, the rest of the properties are user defined.

**Synthetic testing vs RUM**  
You might be wondering why go through all this trouble of setting up Performance Observer metrics if you can just use a tool like Lighthouse or Webpage speed test and get these metrics by just entering in the url. 

Tools like those are important but they are what’s known as synthetic testing since the test will be done on your device and the test will not actually reflect what your users are experiencing. You can throttle the CPU or network when making these tests but they are still simulations. 

Using GA with Performance Observer metrics will give us real numbers from our actual end users, devices and networks. This is known as RUM or Real User Monitoring. 

Synthetic testing tools. Simply enter the URL of your app to run the synthetic tests. 

* [https://www.webpagetest.org/](https://www.webpagetest.org/)
* [https://www.thinkwithgoogle.com/feature/testmysite](https://www.thinkwithgoogle.com/feature/testmysite)
* [https://developers.google.com/speed/pagespeed/insights/](https://developers.google.com/speed/pagespeed/insights/)
* [https://www.uptrends.com/tools/website-speed-test](https://www.uptrends.com/tools/website-speed-test)
* [https://tools.pingdom.com/](https://tools.pingdom.com/)

  


## Google Analytics  


**Setup**  
If you already have Google Analytics setup on your app, feel free to skip this section there is nothing new here. 

To setup GA go on the dashboard and click on the admin tab on the side drawer. Then click add property. Fill out the required info. 

If you are reading this tutorial I'm going to assume your smart enough to setup Google Analytics with just those 3 lines of instruction. If not, here is a handy guide by Google. 

[https://support.google.com/analytics/answer/1042508?hl=en](https://support.google.com/analytics/answer/1042508?hl=en)

After you're done setting up, you will get a tracking id at the top, which we will use in our React App.

  
**Setup in react**  
We dont have to re-invent the wheel here, we can use a helper library made by the Mozilla Foundation to help us with the React setup. 

To install the library simply run

`npm install react-ga`

Then just import the ReactGA object where ever you want to use it

```javascript
import ReactGA from 'react-ga';
```

You will also need to initialize it in the root component with the tracking id from google analytics.  

```javascript
...
ReactGA.initialize('UA-00000-1');
...
```



**Observers**  
`ReactGA` cant do anything besides send data to the Google Analytics website. To actually get performance metrics to send, we will use the Performance Observer browser API. This Performance Observer API has nothing to do with GA or even React, it is a browser API that is available in most modern browsers 

How the PerformanceObserver and related APIs work exactly is a fairly big topic and is far out of the scope of this tutorial. See the Further Reading section for more info and links to tutorials. 

The basic idea of how they work is they "observe" something and then send that data asynchronously at the time of the browsers choosing. This keeps the main thread free for critical app functionality and related tasks, therefore tracking events does not affect your app performance. 

Before observers you would have to add an event listener and fire it synchronously every time something happened, this resulted  in noticeable performance issues if too many events were being fired at once. So this is the problem observers are looking to solve. 



## Track Page Views  


Tracking page views in a single page app like react may seem like it would be complicated but its relatively simple thanks to react-router and history libraries. 

```javascript
history.listen((location) => {
    ReactGA.set({ page: location.pathname });
    ReactGA.pageview(location.pathname)
  }
);
```

`history.listen()` allows you to fire a callback on route changes which in our case happens to be the GA hit. The route is contained in the `pathname` property of `location`.  But there are a couple of things to note such as: 

**Handling the intial load**  
History is listening for page changes but it doesn’t cause a hit on the initial page load.

There are a few ways to handle the initial load. I found a simple way to do it that I think requires the least amount of code and complexity and it is just to have an initial load variable and save it to the global state. In the home page just use a conditional to check if it is false then set it to true after the hit. 

Context variable in the parent component

```javascript
... 

const [initialLoad, setInitialLoad] = useState(false)

...
      <Context.Provider
            //Initial Load
            initialLoadProp: initialLoad,
            setInitialLoadProp: () => setInitialLoad(true),
       >
      </Context.Provider>
```

Then the `useEffect()` in the home child component 

```javascript
...   
useEffect(() => {
    if(!context.initialLoadProp) {
      ReactGA.pageview(props.location.pathname);  
      context.setInitialLoadProp(true)
    }
  }, [])
...

```

There are other implementations and discussions you can find here:

[https://github.com/react-ga/react-ga/wiki/React-Router-v4-withTracker](https://github.com/react-ga/react-ga/wiki/React-Router-v4-withTracker)  


**Tracking pages with User ids**  
Another thing you might want to know is how many users are visiting their private profile pages. Just using the pageviews would give you a unique url for every hit and will not work. 

Say you have the following URLs with user ids:

user/4543456/messages  
user/4543456/account  
user/3543564/messages  
user/3543564/replytomessage  
user/3543564/account

These will all give you a unique page hit. A simple fix is to just check with a conditional and then remove the unique id. You can also use a conditional to make sure you dont send these pages to google analytics. 

```javascript
...

 history.listen((location) => {
   if(location.pathname.includes('/user')) {
     let rootURL = location.pathname.split('/')[1]
     let userPage = location.pathname.split('/')[3]

     let pageHit = `/${rootURL}/${userPage}`
     ReactGA.pageview(pageHit)
   } else {
     ReactGA.set({ page: location.pathname });
     ReactGA.pageview(location.pathname)
   }
});

...
```

We are simply just parsing out the user id and then concatenating the route again before sending the hit. 

This would probably not be true for forum posts since having a unique URL for each post would be correct, since you would like to know how many people visited each post. 



## Tracking Load Performance

Getting the load performance is relatively easy. All the load performance data is under the `navigation` entry which is part of the [navigation timing API](https://developer.mozilla.org/en-US/docs/Web/API/Navigation_timing_API). 

The Performance Observer Can be setup like so in the root parent component. 

```javascript
const callback = list => {
    list.getEntries().forEach(entry => {
      ReactGA.timing({
        category: "Load Performace",
        variable: "Some metric",  
	value: "Value of Metric"
      })
  })
}

var observer = new PerformanceObserver(callback);
observer.observe({entryTypes: ['navigation'] })
```

First we define a function to be called for each entry. Then we pass this callback into our `PerformanceObserver` and finally we call the `.observe()` method on our observer and pass in `navigation` as an entryType.  

This will give you the following entry:

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-76.png)

This is a very large amount of information but really we need only 3 properties to track the main load performance: 

`requestStart`: when the browser issues a request to get the webpage from the server

`responsesStart`: when the first byte of the website arrives

`responseEnd`: When the last byte of the website arrives

There are a few things that happen before the requestStart such as DNS lookup and the TLS handshake. Use this data and see if you can combine it with other properties to make new metrics. 

With the above three properties we can create 3 important metrics. Simply substitute in the `variable` and `value` properties for the respective metric. 

```
const callback = list => {
    list.getEntries().forEach(entry => {
      ReactGA.timing({
        category: "Load Performace",
        variable: 'Server Latency',
        value: entry.responseStart - entry.requestStart 
      })
  })
}
```

Server latency:  
`entry.responseStart - entry.requestStart`

Download time:  
`entry.responseEnd - entry.responseStart`

Total app load time:  
`entry.responseEnd - entry.requestStart`

  
  
**Time to Interactive**  
This metric is essentially how long it takes for a user to be able to interact with your site.

Until a native TTI metric is available through the browser api we can use this handy polyfill npm module for now. This module is created by Google. 

`npm install tti-polyfill`

Then we can use the polyfill like so. 

```javascript
... 

import ttiPolyfill from 'tti-polyfill';


ttiPolyfill.getFirstConsistentlyInteractive().then((tti) => {
  ReactGA.timing({
    category: "Load Performace",
    variable: 'Time to Interactive',
    value: tti 
  })
});

...
```

We are simply sending a hit inside of our function with a chained `.then()` statement since we will retrieve this metric asynchronously. 



## Tracking Rendering Performance

Now we can discuss Rendering Performance, which is how long it takes for React to construct the tree of DOM nodes. We can track rendering performance with the `mark` and `measure` entries. 

`mark` is used to "mark" a point in time you want to keep track of. Just pass in a string as the name of the mark on the exact line you want mark for tracking. 

```javascript
performance.mark("name of mark")
```

`measure` is the difference between the 2 marks. Just set the name of the measure and pass in start and end marks, which will give you the difference between the marks in milliseconds. 

```javascript
performance.measure.("name of mark", startingMark, EndingMark)
```

Thankfully React comes pre-bundled with these marks and measures, which saves us from having to open up the React Source and having to write them ourselves. Simply pass in `mark` and `measure` for the entry types and you're done. 

```javascript
...

var observer = new PerformanceObserver(callback);
observer.observe({entryTypes: ['mark', 'measure'] })

...
```

This will give you the time it takes for root parent component and all child components to render in milliseconds. You will get entries that look something like this: 

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-73.png)

You will also get the time it takes for the lifecycle methods to execute. There is a wealth of information here, simply pick what you want to track and send it to GA by checking for the name in a conditional statement. 

```javascript
...
const callback = list => {
    list.getEntries().forEach(entry => {
      if(entry.name.includes('App') ) {
        ReactGA.timing({
          category: "App Render Performace",
          variable: entry.name,
          value: entry.duration
        })
      }
  })
}
...
```



## Tracking Paint Performance

Now we can track paint which is when the pixels are drawn (or "painted") to the screen after the DOM tree is rendered.  

Tracking paint performance comprises 3 metrics: First Paint, First Contentful Paint and First Meaningful paint. 

**First Paint**: First time anything besides a blank white page is present. 

**First Contentful Paint:** When the first DOM element is present. Text, image etc. 

First Paint and First Contentful Paint will be given automatically by the API. Simply do the following:

```
...

const callback = list => {
    list.getEntries().forEach(entry => {
       ReactGA.timing({
          category: "Paint",
          variable: entry.name,
          value: entry.startTime
     })
  })
}

var observer = new PerformanceObserver(callback);
observer.observe({entryTypes: ['paint'] })
```

The entries will look like this

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-74.png)

It is entirely possible that both these metrics are exactly the same, down to the millisecond. Even if they are not the same there can be an irrelevant difference between them. For this reason another more flexible metric is used, called: 

**First Meaningful Paint**: When something “meaningful” is painted to the screen. “meaningful” is kept intentionally vague, allowing the developer to decide themselves what they want to test for.  

According to Google, the First Paint and First Contentful paint answer the question of “Is it happening” and First Meaningful Paint answers “Is it useful”. “Is it useable” is answered by Time to Interactive. 

A common way to use First Meaningful paint is to test for the hero element. Which is the main element on the page. 

An example for youtube would be the video player. Suggested videos and comments would all then be non hero secondary elements. Tracking when the video player has finished painting would be the First Meaningful Paint in this case. 

A common hero element on the homepage is a background image near the header that gives the value proposition or theme of the website. Knowing this, we can use the resource timing api to measure when our image has finished loading and make this our First Meaningful paint metric. 

If your hero element is an image then you can simply look at the resource timing API and then look at `responseEnd` property and use that as your FMP. 

```javascript
...
const callback = list => {
    list.getEntries().forEach(entry => {
        ReactGA.timing({
          category: "First Meaningful Paint",
          variable: entry.name,
          value: entry.responseEnd
        })
  })
}

var observer = new PerformanceObserver(callback);
observer.observe({entryTypes: ['resource'] })
...
```

Entire resource timing response.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-75.png)

Since the loaded image doesn't technically mean its painted you can also try to set the marks manually. 

```


//jsx 

{performance.mark('start') 
<img />
{performance.mark('end')
{performance.measure('diff', 'start', 'end')


```

Again there is a lot of flexibility in this metric, really consider your use case and what your trying to measure.

## **Track Scroll**

Tracking the scroll position of your user is a fairly important part of analytics. You can for example see how many users scrolled past a certain image or section of text. Having this information you can then tweak your content and increase your conversion. 

You would have seen older implementations use **getBoundingClientRect()** but this would tie up the main thread and therefore tracking the scroll would actually decrease performance. You can execute the scroll events asynchronously with `IntersectionObserver`.  

The `IntersectionObserver` is different than the `PerformanceObserver` we have been working with in the last sections. 

The `IntersectionObserver` takes 2 arguments a callback and a options object. The options object will have 3 properties

`root`: The element you are trying to test the intersection against. In most cases this will be the viewport which will be the value of `null`. 

`rootMargin`: The margins around the root element. ex: "10px"

`threshold`: How much of the element is visible before `isIntersecting` is true. ex: 0.5 means `isIntersecting`  is true when 50% of the element is visible. 0 means the very top of the element and 1.0 means the entire element. 

The entry will return an object like so: 

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-78.png)

  
`isIntersecting`:  Essentially used to determine if the element is visible which would be true when the threshold is reached.

And now the code: 

```javascript
//Get the element you want to track with useRef
const intersectTarget = useRef(null)

//Use the observer inside the component you want to track scroll
  useEffect(() => {
    const opts = {
            root: null,
            rootMargin: '0px',
            threshold: 0
    }
    const callback = list => {
      list.forEach(entry => {
        if(entry.isIntersecting) {
            ReactGA.event({
              category: 'Scroll',
              action: 'Scrolled to heading 2',
              value: entry.intersectionRatio
            })
          }
       })
    }
    const observerScroll = new IntersectionObserver(callback, opts)

    observerScroll.observe(intersectTarget.current)
  }, [])

//jsx
  <h1 ref={intersectTarget}
      id="heading2"
		>
     Second Heading
  </h1>
```

The main idea here is to first initialize the `useRef` hook. Then use the ref on the element you want to track for scroll. The callback and observer will be called in the `useEffect` hook and the element can be passed to the `.observe()` method with the name of the ref and the `.current` property. 



**Note**: The intersection observer will fire on the initial page load even if the element is not visible. This is normal and you will see that the `isIntersecting` property is false. 

**Note also:** At the time of this writing there is also an `isVisible` property on the entry, but it does not function as its name suggests. It stays false even when the element visible. It is not documented anywhere so I cant comment on its purpose, but I would suggest using `isIntersecting`   property instead.     
  


## Track Events

The basic idea to tracking events is to send GA hits inside of the function call attached to an event handler. There really isn’t much more to it than that. 

One thing to note is if your user is submitting a form you can specify the     `transport: beacon` property in your event hit, which will let you reliably send the hit even if the page is reloaded to another page. This isn't so much of an issue in a single page app like React, but if you did want to do this, just know this option is available. 

See the [navigator beacon](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/sendBeacon) for more info 

I will show you how to track a form submit, but this pattern will work with basically any event. Again you are simply sending the hit in a function attached to the event handler.

```javascript
  
  ...
  const handleSubmit = (event) => {
    event.preventDefault();
    ReactGA.event({
     category: 'Form',
     action: 'Form Submit',
     transport: 'beacon'
   });
    apiCall('/apicall', event.target.value)
  };
  
  ...
  
  <form onSubmit={handleSubmit}>
  ...
  </form>
  
  ...
```



  
  
**Quick Performance Tips and Heuristics**  


Biggest area for improvement I see for a lot of developers is to code things from scratch instead of using a library. Tree shaking reduces bloat a little bit, but there is still considerable bloat compared to coding something yourself. Which will allow you to only write the code you need.  Try to use as little libraries as possible. Instead of using a library for a few functions, try to just look at the source code of the library and try to implement those functions yourself. Also keep in mind that most libraries have to prioritize ease of use and personalization over performance. 

Some other ones: 

* For event firing like scroll you will definitely need debouncing/throttling. You don't need to do this for observers.  
* Only import functions and variables you need and let tree shaking discard unused code. 
* Do not pass in an anonymous function to events. 
* Turn your React app into a PWA allowing users to download and install your webapp locally on their device.
* Reduce payloads with code splitting and lazy loading. 
* Decrease file size by using gzip or similar compression 
* Serve images from a CDN 
* Enable caching through your http headers on server responses. 
* Optimize images. See the google fundamentals guide for a full guide on how to do so. 
* Use the new CSS Flexbox for layout. Avoid [Layout Thrashing](https://developers.google.com/web/fundamentals/performance/rendering/avoid-large-complex-layouts-and-layout-thrashing) 
* Only Use transforms and opacity for css changes. So instead of changing height and width use scale X and scaleY 

Luckily, A lot of these optimizations, like minification and gzip, are done for automatically when you run the npm build command on a React Project.

##   
Conclusion

Thanks for reading! If you found any other creative metrics or clever ways to track users, let me know in the comments. 

> Follow me on twitter for more tutorials in the future: [https://twitter.com/iqbal125sf](https://twitter.com/iqbal125sf) 

  


**Blog Posts:**  
[https://www.searchenginejournal.com/a-technical-seo-guide-to-lighthouse-performance-metrics/292703/#close](https://www.searchenginejournal.com/a-technical-seo-guide-to-lighthouse-performance-metrics/292703/#close)

[https://infrequently.org/2017/10/can-you-afford-it-real-world-web-performance-budgets/](https://infrequently.org/2017/10/can-you-afford-it-real-world-web-performance-budgets/)

[https://speedcurve.com/blog/user-timing-and-custom-metrics/](https://speedcurve.com/blog/user-timing-and-custom-metrics/)

[https://designsystem.digital.gov/performance/](https://designsystem.digital.gov/performance/)

[https://hackernoon.com/react-performance-primer-64fe623c4821](https://hackernoon.com/react-performance-primer-64fe623c4821) 

[https://reactjs.org/docs/optimizing-performance.html](https://reactjs.org/docs/optimizing-performance.html)  


**Observers:**  
[https://css-tricks.com/paint-timing-api/](https://css-tricks.com/paint-timing-api/)

[https://css-tricks.com/breaking-performance-api/](https://css-tricks.com/breaking-performance-api/)

[https://hackernoon.com/tracking-element-visibility-with-react-and-the-intersection-observer-api-7dfaf3a47218](https://hackernoon.com/tracking-element-visibility-with-react-and-the-intersection-observer-api-7dfaf3a47218)

[https://www.smashingmagazine.com/2018/01/deferring-lazy-loading-intersection-observer-api/](https://www.smashingmagazine.com/2018/01/deferring-lazy-loading-intersection-observer-api/)

[https://www.sitepen.com/blog/improving-performance-with-the-paint-timing-api/](https://www.sitepen.com/blog/improving-performance-with-the-paint-timing-api/)  


**Google Based:**  
[https://developers.google.com/web/fundamentals/performance/user-centric-performance-metrics](https://developers.google.com/web/fundamentals/performance/user-centric-performance-metrics)

[https://developers.google.com/web/fundamentals/performance/navigation-and-resource-timing/](https://developers.google.com/web/fundamentals/performance/navigation-and-resource-timing/)

[https://developers.google.com/web/tools/chrome-devtools/speed/get-started](https://developers.google.com/web/tools/chrome-devtools/speed/get-started)

[https://marketingplatform.google.com/about/optimize/](https://marketingplatform.google.com/about/optimize/)

[https://developers.google.com/analytics/devguides/collection/analyticsjs/user-timings](https://developers.google.com/analytics/devguides/collection/analyticsjs/user-timings)

[https://support.google.com/analytics/answer/1033068#Anatomy](https://support.google.com/analytics/answer/1033068#Anatomy)

[https://developers.google.com/analytics/devguides/collection/analyticsjs/single-page-applications](https://developers.google.com/analytics/devguides/collection/analyticsjs/single-page-applications)

[https://support.google.com/analytics/answer/1033068](https://support.google.com/analytics/answer/1033068)

[https://docs.google.com/document/d/1GGiI9-7KeY3TPqS3YT271upUVimo-XiL5mwWorDUD4c/preview#](https://docs.google.com/document/d/1GGiI9-7KeY3TPqS3YT271upUVimo-XiL5mwWorDUD4c/preview#)

[https://www.doubleclickbygoogle.com/articles/mobile-speed-matters/](https://www.doubleclickbygoogle.com/articles/mobile-speed-matters/)  
  


  


  

