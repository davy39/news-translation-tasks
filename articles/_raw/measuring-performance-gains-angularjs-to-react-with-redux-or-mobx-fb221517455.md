---
title: Migrating from AngularJS to React — how do you measure your performance gains?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-23T07:14:07.000Z'
originalURL: https://freecodecamp.org/news/measuring-performance-gains-angularjs-to-react-with-redux-or-mobx-fb221517455
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Dbqp6gglYpKlXuzA1sHuaQ.jpeg
tags:
- name: Angular
  slug: angularjs
- name: React
  slug: react
- name: Redux
  slug: redux
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Gupta Garuda

  Are you looking into migrating a large AngularJS single page application to React?
  If so, you may be wondering what sort of performance gains you are going to get
  with React and how the code will morph (with state management libraries...'
---

By Gupta Garuda

Are you looking into migrating a large AngularJS single page application to React? If so, you may be wondering what sort of performance gains you are going to get with React and how the code will morph (with state management libraries Redux or Mobx).

In this post, I’ll try to answer some of these questions, and give you a lot of data you can use to make more informed decisions.

First, I will go over the performance and memory profiles of various UI scenarios implemented using AngularJS, React/Redux and React/Mobx. We will compare and contrast the performance of these frameworks on measures like script execution time, frames per sec, and usedJSHeapSize for each scenario.

I provided the links to the test pages and source code so you can try out those scenarios and can review the code to get a feel for constructs that React (with Redux or Mobx) will bring to the table.

### Performance test setup

To evaluate the performance of AngularJS and React, I created a benchmark application, a stock ticker dashboard. This application shows a list of stocks and has some controls to automate UI test actions. For each stock, the application shows the ticker symbol, company name, sector name, current price, volume and simple moving averages (10 days, 50 days and 200 days), and a visual indicator showing whether the price went up or down. The test dataset consists of 5000 stock tickers and is loaded during the page load via a script tag.

I created three versions of this application using AngularJS, React/Redux, and React/Mobx. This enables us to easily compare the performance metrics for each scenario across the frameworks.

![Image](https://cdn-media-1.freecodecamp.org/images/EhA-FdGhYq33bnzqOERvMcuypgwCVg29k5l3)
_Performance test page_

#### Test Scenarios

* **Switching views**  
We navigate through a list of 5000 stock tickers showing 150 tickers at a time every 0.5sec. This scenario measures how quickly the framework can update the view when the visible collection data model changes.   
_Real world use-case: route changes, paging through a listview, virtual scroll, and so on._
* **Adding tickers**   
We add 50 tickers to the visible collection every 100ms until we show the entire collection of 5000 tickers. This scenario measures how quickly the framework can create new items. Showing 5000 tickers is not a realistic scenario, but we can visualize the limits where things will fall apart with each framework.  
_Real world use-case: Pinterest style infinite scroll where new UI elements are added to the DOM as the user scrolls._
* **Quick Updates on Price/Volume**  
We render 1500 tickers and start updating price/volume data for random tickers once every 10ms. This scenario measures how quickly frameworks can apply the partial updates to the UI.   
_Real world use-case: updates to presence indicators, likes, retweets, claps, stock prices, and so on._
* **Removing tickers**  
We will first add all 5000 tickers and then start removing 50 tickers from the visible collection once every 100ms.

#### Links to test pages and source

All the examples are written in Typescript and the compilation/bundling is done using Webpack. The Readme page for source URL lists the instructions to build and run the applications.

* AngularJS — [https://guptag.github.io/js-frameworks/AngularJS/examples/angularjs-perf-test/index.html](https://guptag.github.io/js-frameworks/AngularJS/examples/angularjs-perf-test/index.html) ([Source](https://github.com/guptag/js-frameworks/tree/master/AngularJS/examples/angularjs-perf-test))
* React/Redux — [https://guptag.github.io/js-frameworks/Redux/examples/redux-perf-test/index.html](https://guptag.github.io/js-frameworks/Redux/examples/redux-perf-test/index.html)   
([Source](https://github.com/guptag/js-frameworks/tree/master/Redux/examples/redux-perf-test))
* React/Mobx — [https://guptag.github.io/js-frameworks/Mobx/examples/mobx-perf-test/index.html](https://guptag.github.io/js-frameworks/Mobx/examples/mobx-perf-test/index.html)   
([Source](https://github.com/guptag/js-frameworks/tree/master/Mobx/examples/mobx-perf-test))

### Before we start…

* All the below metrics are measured on Win10/Intel Xeon E5 @ 2.4GHz, 6 core, 32GB desktop with Chrome browser v60. The numbers will change on different machines/browsers.
* To see the accurate heap memory data on the test pages, open Chrome with ‘_--enable-precise-memory-info_’ flag.
* React is a library rather than a full-fledged framework like AngularJS. In this post, I used the term framework for simplicity.
* Test pages show live JavaScript heap size as Memory.  
About javascript heap size: In Chrome TaskManager,

> In Chrome TaskManager, “_The Memory column represents native memory. DOM nodes are stored in native memory. If this value is increasing, DOM nodes are getting created. The JavaScript Memory column represents the JS heap. This column contains two values. The value you’re interested in is the live number (the number in parentheses). The live number represents how much memory the reachable objects on your page are using. If this number is increasing, either new objects are being created, or the existing objects are growing_. [From Fix Memory Issues by Kayce Basques](https://developers.google.com/web/tools/chrome-devtools/memory-problems/)

* About Frames per second:

> _Most devices today refresh their screens 60 times a second. If there’s an animation or transition running, or the user is scrolling the pages, the browser needs to match the device’s refresh rate and put up one new picture, or frame, for each of those screen refreshes. Each of those frames has a budget of just over 16ms (1 second / 60 = 16.66ms). In reality, however, the browser has housekeeping work to do, so all of your work needs to be completed inside 10ms. When you fail to meet this budget, the frame rate drops, and the content judders on screen. This is often referred to as jank, and it negatively impacts the user’s experience._ [From Rendering Performance by Paul Lewis](https://developers.google.com/web/fundamentals/performance/rendering/)

### DOM - AngularJS Components vs. React Components

AngularJS directives (or components) create an extra wrapper element around the template. For simple views, this is not an issue. However, in complex views containing a large number of directives (especially when they are repeated within ng-repeat), all the extra elements will add up to the total size of the DOM tree — potentially impacting memory, selector performance, and so on.

Although you can set ‘replace=true’ property to disable rendering the wrapper element, it causes a bunch of issues and is [currently marked as deprecated](https://github.com/angular/angular.js/commit/eec6394a342fb92fba5270eee11c83f1d895e9fb).

Here is the rendered HTML for the ticker component in AngularJS:

![Image](https://cdn-media-1.freecodecamp.org/images/kTJ0GNtycTKAdofCEjHbbiv-UIg7OlHMVCsq)
_AngularJS directive/component (left side), Rendered HTML (right side) - Wrapper element is created for each child directive._

Here is rendered HTML for the similar ticker component in React:

![Image](https://cdn-media-1.freecodecamp.org/images/s4cxv5BoHVqYqpqFkrWbnaLppQOMvqrVqFMw)
_React component (left side), Rendered HTML (right side) - No wrapper elements created for child components_

In our specific example, AngularJS created an additional 1400 DOM nodes compared to React for rendering the same number of tickers (200).

![Image](https://cdn-media-1.freecodecamp.org/images/cp0RpJDvv2Ko88EKSfogOaTmVEFGNuc-irCa)
_DOM count — AngularJS vs. React_

### Scenario 1 — Switching Views

We navigate through a list of 5000 tickers showing 150 tickers at a time every 0.5sec.

The below chart plots the script execution time for each refresh from Chrome’s performance timeline. AngularJS consistently took >200ms to delete the existing 150 tickers and to show the new ones. Whereas React/Redux did the same work within 90–100ms (half the time compared to ng1). The React/Mobx version took slightly more time than the Redux version, but not far from it.

![Image](https://cdn-media-1.freecodecamp.org/images/EavjKTdDoodsQ1DE3SGvtxxJAzRBLK2EVQ7J)
_Script execution time comparison (AngularJS vs. React/Redux vs. React/Mobx) — Replacing 150 tickers every 0.5 sec_

The below chart shows the frames per sec(fps) as the refresh happens. The Redux and Mobx versions stayed around 45fps whereas AngularJS stayed around 30 fps during the entire run.

![Image](https://cdn-media-1.freecodecamp.org/images/Pz5M93atTLYJnCuuTLKyPoPIilOAiokrT78b)

#### **Memory & GC pauses**

The below chart shows the JavaScript heap size (‘usedJSHeapSize’) measured during the refresh. Both the AngularJS and Mobx versions showed a staircase pattern for the memory consumption, indicating that Chrome kicked in the GC to reclaim the memory. The Redux version is super consistent with its low memory profile all throughout the run.

![Image](https://cdn-media-1.freecodecamp.org/images/AvWVCzs4F7DZxNSAU6-VMtmm0tIN1m4wxg5r)

Let’s closely look into the timeline profiles for all the three versions.

AngularJS execution caused several GC pauses as the ticker list gets refreshed. [V8 tries to hide GC pauses by scheduling them during the unused chunks of idle times to improve the UI responsiveness](https://v8project.blogspot.com/2015/08/getting-garbage-collection-for-free.html). Contrary to this ideal behavior, GC pauses happened during the script execution contributing to the overall execution time.

![Image](https://cdn-media-1.freecodecamp.org/images/-BtwuertIbQDuGJCblQlG0QJITNwvU6L8sDG)
_AngularJS emitted lot of GC events as the ticker list is refreshed with 150 new items_

The Redux performance profile shows no GC pauses whatsoever during the script execution.

![Image](https://cdn-media-1.freecodecamp.org/images/ZiB4Ufc9iquZQzjP1vctBmLayeAMX9aflDqF)
_React/Redux — No GC pauses_

The Mobx profile shows few GC pauses, but not as many as the AngularJS version.

![Image](https://cdn-media-1.freecodecamp.org/images/k4AUDMMOj1WtfiOAfGvhCGNIktRc-K4Cowd6)
_React/Mobx — Few GC pauses but not as many as AngularJS version_

### Scenario 2 — Adding Tickers

We will add 50 tickers to the visible collection every 100ms until we show all the tickers. The result of showing all 5000 tickers is not a realistic scenario, but it would be interesting to see how each framework handles it.

The below chart plots the script execution time from Chrome’s performance timeline. In the case of AngularJS, the script execution time linearly increased as more and more tickers were added to the page. AngularJS took more time to add new tickers right from the start compared to the other versions.

Interestingly, the Redux and Mobx versions show impressive performance even towards the right side of the chart with thousands of tickers on the page. React’s virtual DOM diffing algorithm is showing its strength compared to AngularJS’s dirty checking.

![Image](https://cdn-media-1.freecodecamp.org/images/NIeetxK6i7T8N9wH-137uWZ-Ef39pBLng936)
_Adding Tickers — Script execution time comparison_

With AngularJS, adding new items caused jank in the browser right from the start (red bars) and the number of frames per second dropped from 60 early on and never recovered (green area) during the entire add operation.

![Image](https://cdn-media-1.freecodecamp.org/images/0IM4iKnHIb795zyDko1lBWHNMYcjsnaw0Oni)
_AngularJS — Add tickers timeline_

Redux created jank once early-on, but it is all clear until we crossed the halfway point of adding new tickers. FPS also nicely recovered to 60 in between the add operations.

![Image](https://cdn-media-1.freecodecamp.org/images/9SQzLRly315H5bmYc7K1PzvYL3vXiAzP64tj)
_Redux-Add Tickers timeline_

Mobx caused jank few times more times than Redux, but nowhere close to AngularJS.

![Image](https://cdn-media-1.freecodecamp.org/images/Iu3DqyihMvKsoJPIrZZF0ZtLRuZYrdKCJ21r)
_Mobx — Add tickers timeline_

#### **Memory & GC events**

Redux consumed about half the heap size as AngularJS during the entire run. Mobx stayed in between.

![Image](https://cdn-media-1.freecodecamp.org/images/T91WZQF9HJ9p1Eb3Tkn3W47Ra3fbUqyj9ULD)
_Adding Tickers — Memory Comparison_

Adding new tickers also triggered some GC pauses with AngularJS (almost once with every add operation). Redux triggered fewer GC pauses overall. Mobx started to trigger more GC pauses towards the end as we added more and more tickers to the list.

![Image](https://cdn-media-1.freecodecamp.org/images/Oz8qWGRaltyJ1L9lrrPWLlRvOWrAnp1kMqpe)
_Adding Tickers — AngularJS GC events (partial timeline)_

![Image](https://cdn-media-1.freecodecamp.org/images/sa5nuYHeg2-h3cdu5Y4c775B5HreFKwLcFUk)
_Adding Tickers — React/Redux GC events (partial timeline)_

![Image](https://cdn-media-1.freecodecamp.org/images/B3sCDnsuAlzHYAW9Qnn4YCfW0vAaOBRfGB99)
_Adding Tickers — Mobx GC events (partial timeline)_

### Scenario 3 — Quick U**pdates to Price/Volume**

This is the most common scenario in the real-time applications. Once the view is rendered, there will be a quick succession of updates coming into the application either via web-sockets, xhr calls, and so on. Imagine the use-cases like presence updates, stock price changes, likes/retweets/claps count changes, and more. Let’s see how each framework fares in this scenario.

All the below metrics are taken with 1500 tickers on the page and when price/volume changes are happening every 10ms.

AngularJS again struggled to keep up with the updates happening in quick succession. Script execution for each update took about 35ms. Redux took 6ms to update the view. Mobx shines, updating the view within 2ms. Mobx’s derivation graph knows exactly which component to update based on which observable’s state is changed.

![Image](https://cdn-media-1.freecodecamp.org/images/OMPlXhWpNtJsRX9R69q0XpWftRvelqzOqofZ)
_Updates — Script execution comparison_

Here are the timeline profiles showing the script execution for each version.

![Image](https://cdn-media-1.freecodecamp.org/images/SKU7rg0WPZHRXoTGeMGL3UTCN6Vl1Flk4br5)
_AngularJS — Updates to Price/Volume_

![Image](https://cdn-media-1.freecodecamp.org/images/15yZ2hcVcPB9wZgc27n85oGbOHgSCb5ZDNJe)
_Redux — Updates to Price/Volume_

![Image](https://cdn-media-1.freecodecamp.org/images/2XyT5qWBw6Oz1fpdre0Ex2BHHipSfkFZ8uKJ)
_Mobx — Updates to price/volume_

FPS consistently stayed at 60 with Redux and Mobx, whereas it hovered a little below 30 with AngularJS.

![Image](https://cdn-media-1.freecodecamp.org/images/-HspGSYy0PukZo0TqJ-h-B7Zp4oLAg8IeGvJ)
_Updates to Price/Volume — Frames Per Second_

### Scenario 4 — Deleting Tickers

We will add all 5000 tickers to the page and start removing 50 tickers from the visible collection every 100ms.

The below images show the performance profile of the initial delete iterations. AngularJS is almost 4x slower compared to React versions. Redux and Mobx took a little more time in the initial iterations but settled between 50–70ms for each delete operation.

![Image](https://cdn-media-1.freecodecamp.org/images/QU4wRyQDQpK6xMCQKP95ISP6PRvxe4xtepCa)
_AngularJS — Deleting 50 tickers from 5000 tickers every 100ms (initial iterations)_

![Image](https://cdn-media-1.freecodecamp.org/images/9GESwmbGwHXE50FwaPpxJwVmmT6-LKafQ--J)
_Redux — Deleting 50 tickers from 5000 tickers every 100ms (initial iterations)_

![Image](https://cdn-media-1.freecodecamp.org/images/qeqR9f6RklGhNYRQmbvWDQ26Ljs3KtTkf5Az)
_Mobx — Deleting 50 tickers from 5ooo tickers every 100ms (initial iterations)_

It’s pretty clear from all the above tests that React gives significant performance gains when compared with AngularJS.

As the applications grow bigger and views get more complex, the runtime profile of the frameworks starts to differ in their various ways. Our objective was to replicate the scenarios we were targeting for, measure the performance/memory impact, and look at the pro/cons of the constructs with each framework.

Even with the most performant framework out there, we still need to apply a lot of discipline and follow the right patterns to make the applications scalable and performant.

I go over the core concepts, benefits, and gotchas of Redux and Mobx in a [separate post](https://hackernoon.com/introduction-to-redux-and-mobx-e6fa98b6479).

Thanks for reading. Hope this is helpful.

P.S. Thanks to [Shyam Arjarapu](https://www.freecodecamp.org/news/measuring-performance-gains-angularjs-to-react-with-redux-or-mobx-fb221517455/undefined) and [Adam Carr](https://www.freecodecamp.org/news/measuring-performance-gains-angularjs-to-react-with-redux-or-mobx-fb221517455/undefined) for reviewing this article.

