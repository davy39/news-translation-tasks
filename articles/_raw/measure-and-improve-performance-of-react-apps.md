---
title: How to Measure and Improve the Performance of a React App
subtitle: ''
author: German Cocca
co_authors: []
series: null
date: '2023-03-27T17:18:19.000Z'
originalURL: https://freecodecamp.org/news/measure-and-improve-performance-of-react-apps
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/nicolas-hoizey-poa-Ycw1W8U-unsplash.jpg
tags:
- name: performance
  slug: performance
- name: React
  slug: react
- name: web performance
  slug: web-performance
seo_title: null
seo_desc: 'Hi everyone!

  React is a popular JavaScript library for building user interfaces. As applications
  built with React become more complex, their performance can start to degrade.

  Poor performance can lead to a frustrating user experience and a negative i...'
---

Hi everyone!

React is a popular JavaScript library for building user interfaces. As applications built with React become more complex, their performance can start to degrade.

Poor performance can lead to a frustrating user experience and a negative impact on user engagement. So in this article, we will discuss how to measure and improve the performance of a React application.

# Table of Contents

* [How to define performance](#heading-how-to-define-performance)
    
* [How to measure performance](#heading-how-to-measure-performance)
    
    * [React dev tools](#heading-react-dev-tools)
        
* [How to improve performance](#heading-how-to-improve-performance)
    
    * [Optimizing images](#heading-optimizing-images)
        
    * [Code splitting and Lazy Loading](#heading-code-splitting-and-lazy-loading)
        
    * [Optimizing the DOM](#heading-optimizing-the-dom)
        
    * [Avoid unnecessary component re-renders](#heading-avoid-unnecessary-component-re-renders)
        
    * [Rendering patterns](#heading-rendering-patterns)
        
    * [CDNs](#heading-content-delivery-network-cdn)
        
* [Wrapping Up](#heading-wrapping-up)
    

# How to Define Performance

In web development, "performance" generally refers to the speed and efficiency of a website or web application. It encompasses several different factors, including:

1. **Page load time:** This refers to the time it takes for a page to fully load and display all of its content. Faster load times generally lead to a better user experience.
    
2. **Responsiveness:** This refers to the speed at which a website responds to user interactions, such as clicking a button or scrolling. A responsive website feels snappy and quick, which can also improve user experience.
    
3. **Resource usage:** This refers to the amount of server resources (such as CPU and memory) that a website uses to serve pages and respond to requests. A well-optimized website will use resources efficiently, allowing the server to handle more traffic and reducing costs.
    
4. **Scalability:** This refers to a website's ability to handle increased traffic and load without sacrificing performance. A scalable website can handle sudden spikes in traffic without slowing down or crashing.
    

Optimizing website performance is important because it can directly impact user experience, search engine rankings, and even business revenue.

# How to Measure Performance

The first step in improving the performance of a React application is to measure its current performance. There are several tools available for measuring performance, including:

1. **Lighthouse** – [Lighthouse](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk?hl=es) is an open-source tool from Google that audits web pages for performance, accessibility, and more. Lighthouse generates a report that includes suggestions for improving the performance of the application.
    
2. **WebPageTest** – [WebPageTest](https://gercocca.vercel.app/) is a free tool that allows you to test the speed of your website from multiple locations around the world. WebPageTest provides detailed reports on the performance of your website, including suggestions for improvement.
    
3. **Google PageSpeed Insights –** [Google PageSpeed Insights](https://pagespeed.web.dev/) analyzes the content of a web page and generates a report that identifies opportunities to improve the page's performance.
    

All three tools work basically in the same way. You provide the URL of the site you'd like to analyze, and the tools will run through it and provide you with a detailed report covering improvement opportunities in performance, and also accessibility, SEO and general best practices.

These tools are nice to get an objective measure of our apps. Some of them can even be integrated into CI/CD pipelines so we can monitor how changes impact in performance through time.

## React dev tools

Another useful tool for measuring performance in a React app is the profiler of [React DevTools](https://chrome.google.com/webstore/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi). React DevTools is a browser extension that allows you to inspect and debug React applications in the Chrome, Firefox, or Edge browsers.

The "profiler" is a tool that allows you to record the activity in your app, and later on generate a report showing what components were rendered, how many times and when each component was rendered, and how long each render took.

It's quite useful for detecting unnecessary component re-renders and renders that take too long, generating performance bottlenecks.

If you'd like to get a deeper dive into how profiler works, I recommend [this video](https://www.youtube.com/watch?v=00RoZflFE34&t=452s).

# How to Improve Performance

Now that we have an idea of how can we identify performance issues in our app, let's go through some of the optimization techniques we can use to make it better.

## Optimizing Images

Images are one of the primary culprits for slow loading websites. You can optimize images by compressing them without compromising their quality. Tools like [tinyPng](https://tinypng.com/) can compress your images and help you reduce the size of your website, and therefore it's load time.

Meta frameworks such as Next come with built-in image optimization.

## Code splitting and Lazy Loading

Lazy loading involves loading content only when it is needed, instead of loading everything at once. This is done through something called **"code splitting"**. This is a bundling technique that allows you to break up code in smaller chunks that are downloaded only when needed, instead of downloading the whole code in the first render.

A classic example of when this technique can come in handy is when navigating through different routes. Let's say our website has two main routes, "Home" and "Contact".

We'd only want to download the code related to the "Home" page when we're in that route, and the "Contact" code to download when we are in that other route. Code splitting allows us to do that, and in this way help reduce the initial load time of the application and improve the user experience.

You can use tools such as **React.lazy()** and **Suspense** to implement lazy loading in your application. If you'd like a deeper dive into how these tools work, [check out this video](https://www.youtube.com/watch?v=JU6sl_yyZqs).

## Optimizing the DOM

The size of the Document Object Model (DOM) can impact the performance of the application. The bigger and more complex it is, the longer it'll take to load and be modified.

You can optimize the DOM by reducing the number of elements, removing unnecessary elements, and minimizing the use of CSS animations.

### Avoid unnecessary component re-renders

As you may know, React is a library that allows us to build user interfaces. In React, each piece of the UI is represented in code by a component. When a piece of the UI needs to be modified, React re-renders the component with the updated information.

There are two things that trigger a component re-render: A change in state or a change in props. But sometimes, components can re-render unnecessarily, meaning there's no actual change in the information to be displayed.

To prevent unnecessary re-renders, we can implement some of the following techniques:

* **Memoization:** In React, memoization allows a component to "remember" the value of the state and/or props it receives. Before re-rendering, it can check if the value has actually changed. If it hasn't, then it doesn't re-render. This technique can be achieved through hooks like `useMemo` and `useCallback`. If you'd like a deeper dive on that, [check out this article I wrote](https://www.freecodecamp.org/news/memoization-in-javascript-and-react/).
    
* **Use key prop for lists:** When rendering a list of items in React, it's important to provide a unique key prop for each item. This helps React identify which items have changed and need to be re-rendered. If you don't provide a key prop, React will use the index of the item in the array, which can lead to unnecessary re-renders if the order of the items changes.
    
* **Keeping state as local as possible:** By keeping state local, I mean that the state that a component uses should be (when possible) within the component itself or as close in the component tree as possible. This is because when a component re-renders, all children components will re-render as well. It's not necessarily a terrible thing, but if we can avoid it, we probably should. So It's not a good idea to centralize all state in a single parent component, unless that states needs to be used from multiple parts of the application down the component tree. Here's [a great article about this topic](https://kentcdodds.com/blog/state-colocation-will-make-your-react-app-faster) if you're interested in learning more.
    

## Rendering patterns

Another thing that can have an impact on the performance of your app is the rendering pattern it uses. A rendering pattern refers to the way in which the HTML, CSS, and JavaScript code is all processed and rendered in a web application or website.

Different rendering patterns are used to achieve different performance and user experience goals. The most common rendering patterns in web development are:

1. **Client-side rendering (CSR)**: In CSR, the client's browser generates the HTML content of a web page on the client-side using JavaScript. This approach can provide a fast and interactive user experience but can be slower for initial loading times and bad for SEO.
    
2. **Server-side rendering (SSR)**: In SSR, the web server generates the HTML content of a web page on the server-side and sends it to the client's browser. This approach can improve initial loading times and SEO (search engine optimization) but can be slower for dynamic content.
    

Server-Side Rendering (SSR) can help improve the initial load time of the application by rendering the initial page on the server-side. This can help improve the Time-to-Interactive (TTI) and First Contentful Paint (FCP) metrics. You can use tools such as Next.js or Gatsby to implement SSR in your application.

The choice of rendering pattern depends on the specific needs and requirements of a project, such as performance, SEO, user experience, and flexibility. If your priority is to provide users with a fluid, native-like experience, CSR is probably a good choice. If you need ultra fast page load times, SSR or SSG can be a better option.

For a deeper dive into rendering patterns, check out [this article I recently wrote](https://www.freecodecamp.org/news/rendering-patterns/).

## Content Delivery Network (CDN)

A CDN, or Content Delivery Network, is a system of distributed servers or nodes that work together to deliver web content, such as images, videos, and other files, to users based on their geographic location.

When a user requests content from a website, the CDN will serve the content from the server closest to the user, which helps to reduce latency and improve website performance. CDNs can also help to reduce the load on a website's origin server by caching frequently accessed content and delivering it from the CDN's servers instead of the origin server.

CDNs are normally used to host static content (meaning content that doesn't change frequently over time), such as images, videos, blog posts and so on. Also, if you're using Static Site Generation (SSG) as a rendering pattern, you could host your rendered sites in a CDN for an even faster delivery.

Some examples of popular CDNs are Cloudflare and Amazon CloudFront.

For more detail on how CDNs work, check out [this awesome video](https://www.youtube.com/watch?v=RI9np1LWzqw).

# **Wrapping Up**

Well everyine, in this article we've discussed how to measure and improve the performance of a React application.

We defined the concept of website performance, including page load time, responsiveness, resource usage, and scalability, and outlined how to measure performance using tools such as Lighthouse, WebPageTest, Google PageSpeed Insights and React dev tools.

Finally, we've seen some optimization techniques such as optimizing images, code splitting and lazy loading, optimizing the DOM, and avoiding unnecessary component re-renders.

As always, I hope you enjoyed the article and learned something new.

If you want, you can also follow me on [LinkedIn](https://www.linkedin.com/in/germancocca/) or [Twitter](https://twitter.com/CoccaGerman). See you in the next one!

![Image](https://www.freecodecamp.org/news/content/images/2023/03/AbsoluteAnnualKoi-size_restricted.gif align="left")
