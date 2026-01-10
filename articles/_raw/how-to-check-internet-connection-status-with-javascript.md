---
title: How to Check Internet Connection Status Using Async JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-31T19:00:20.000Z'
originalURL: https://freecodecamp.org/news/how-to-check-internet-connection-status-with-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/js_online_offline.png
tags:
- name: internet
  slug: internet
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "By Dave Gray\nCan you use JavaScript to check if your app is connected\
  \ to the internet?\nIn this article, I'll provide an updated answer to this Internet\
  \ connection detection question. (Whew! Say that fast five times!) \nThe solution\
  \ will use JavaScript..."
---

By Dave Gray

Can you use JavaScript to check if your app is connected to the internet?

In this article, I'll provide an updated answer to this Internet connection detection question. (Whew! Say that fast five times!) 

The solution will use JavaScript's Fetch API and asynchronous code with Async & Await. But first, let's look at an accepted solution and discuss why it may not be the best choice for your application.

## navigator.onLine

The online property of the navigator interface, `navigator.onLine`, is frequently used to detect the online and offline status of the browser. 

Combined with listeners for online and offline events, it appears to provide a simple solution for developers that is easy to implement. 

### Let's look at how we'd implement navigator.onLine

Start by adding a load event listener. When the load event fires, the listener will check the online property of the navigator interface and then display the online status. 

The online property of navigator provides a boolean (true or false) response. To finish the action of the listener, we’ll use a ternary statement to set the status display value.

```javascript
window.addEventListener("load", (event) => {
  const statusDisplay = document.getElementById("status");
  statusDisplay.textContent = navigator.onLine ? "Online" : "OFFline";
});
```

_So why the word navigator? Well, it’s a reference to the Netscape Navigator browser from the 90s._

Center an h1 element in your HTML page with the id of “status”. If you apply the JavaScript code above to your page, you should see it display “Online”. 

But this only updates the h1 element when the page loads. Let’s add offline and online event listeners to update the status display any time either of those events fires.

```javascript
window.addEventListener("offline", (event) => {
  const statusDisplay = document.getElementById("status");
  statusDisplay.textContent = "OFFline";
});

window.addEventListener("online", (event) => {
  const statusDisplay = document.getElementById("status");
  statusDisplay.textContent = "Online";
});
```

We can go to the Application tab of Chrome Dev Tools and click on ServiceWorker to set the browser to respond as if it is offline. 

Check and uncheck the Offline checkbox a few times. You should see the status display respond immediately to the offline and online events that are fired.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/offline_check_nav_online.PNG)
_Chrome Dev Tools &gt; Application Tab &gt; Service Workers &gt; Offline Checkbox_

## Let's dig a little deeper

At first impression, the above seems like a good solution which is fairly simple. Unfortunately, as we read more about the online property of navigator and the online and offline events, we find there is a problem. 

[Searching for navigator.onLine on CanIUse.com](https://caniuse.com/#search=navigator.onLine) shows widespread support for the online | offline status the property provides. However, looking at the notes below the support table, we see that 

> “Online does not always mean connection to the Internet. It can also just mean connection to some network”. 

Hmm, that throws a wrench in the works a bit.

So if you really want to determine the online status of the browser, you should develop additional means for checking.

Let’s also take a look at the [MDN docs reference for navigator.onLine](https://developer.mozilla.org/en-US/docs/Web/API/NavigatorOnLine/onLine). MDN web docs backs up the CanIUse.com information and adds additional notes. 

> _“Browsers implement this property differently...you cannot assume that a true value necessarily means that the browser can access the internet. You could be getting false positives...”_ 

And that confirms our fears about using the online property of navigator as our solution for detecting an Internet connection. It is a solution that can wreak havoc in our applications that depend on knowing when outside data sources are available. 

One such example is when we are trying to determine if a Progressive Web App is online or not. MDN even recommends, 

> _“...if you really want to determine the online status of the browser, you should develop additional means for checking.”_ 

A quick web search for _“navigator online not working”_ reveals various forum posts where those depending on this property have run into problems.

## So what’s the solution? 


We need to know when our application is truly connected to the Internet and not just a router or local network. Let’s go back to our JavaScript file and start over.

The idea is to make a request and handle it gracefully with error catching if it fails. If the request succeeds, we’re online, and if it fails, we’re not. 

We’re going to request a small image at an interval to determine the online status. Modern JavaScript provides the Fetch API and asynchronous code with Async & Await. We will use these tools to accomplish our goal.

### checkOnlineStatus()

Let’s start by creating an async arrow function named checkOnlineStatus. The function will return true or false like the online property of navigator does. 

Inside the function, we’ll set up a try block where we await a fetch request for a one pixel image. Ensure your service worker is not caching this image. 

HTTP response codes between 200 and 299 indicate success, and we’ll return the result of the status code comparison. This will be true if the response status is from 200 to 299 and false otherwise. 

We also have to provide a catch block that catches the error if the request fails. We’ll return false in the catch block to indicate we are definitely offline if this happens.

```javascript
const checkOnlineStatus = async () => {
  try {
    const online = await fetch("/1pixel.png");
    return online.status >= 200 && online.status < 300; // either true or false
  } catch (err) {
    return false; // definitely offline
  }
};
```

Next, we’ll use the setInterval method and pass it an anonymous async function. The async function will await the result of our checkOnlineStatus function. We will then use a ternary statement with the result to display the current online status. 

For testing this example, set the interval delay to every 3 seconds (3000 milliseconds). This is really too often, though. Checking every 30 seconds (30000 milliseconds) may be enough for your actual needs.

```javascript
setInterval(async () => {
  const result = await checkOnlineStatus();
  const statusDisplay = document.getElementById("status");
  statusDisplay.textContent = result ? "Online" : "OFFline";
}, 3000); // probably too often, try 30000 for every 30 seconds
```

With our new code saved, let’s revisit the Application tab in Chrome Dev Tools to test the offline response.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/offline_check_fetch.PNG)
_Chrome Dev Tools &gt; Application Tab &gt; Service Workers &gt; Offline Checkbox_

I almost forgot to include the load event listener with async functionality! The load event detection is probably only important if you have a Progressive Web App utilizing a service worker for offline availability. Otherwise, your web page or app simply won't load without a connection. 

Here's the new load event listener: 

```
window.addEventListener("load", async (event) => {
  const statusDisplay = document.getElementById("status");
  statusDisplay.textContent = (await checkOnlineStatus())
    ? "Online"
    : "OFFline";
});
```

## A Final Thought

The above interval code is good for displaying a connection status in your app. That said, I don't suggest relying on a connection status that was checked 20 or 30 seconds prior to making a critical data request in your application. 

Therefore, you should call the checkOnlineStatus function directly prior to the request and evaluate the response before requesting data.

```javascript
const yourDataRequestFunction = async () => {
    const online = await checkOnlineStatus();
    if (online) {
    	// make data request
    }
}
```

## Conclusion

While navigator.onLine is widely supported, it provides unreliable results when determining if our applications are truly connected to the Internet. Utilizing the Fetch API and asynchronous JavaScript, we can quickly code a more reliable solution. 

[Here’s a link to the code gist](https://gist.github.com/gitdagray/f310be81be217750fc9d2b233e2ae70c) on GitHub, and here's a video tutorial I put together: 

%[https://youtu.be/hIaGzJ3txqM]


