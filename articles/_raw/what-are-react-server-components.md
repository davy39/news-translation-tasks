---
title: What are React Server Components?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-01-07T02:43:23.000Z'
originalURL: https://freecodecamp.org/news/what-are-react-server-components
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/English-Header-3.png
tags:
- name: React
  slug: react
seo_title: null
seo_desc: 'By Matías Hernández

  The team behind React thought it''d be a great way to end the year by dangling a
  new feature for the already popular library out in front of developers.

  On December 21st the team revealed a talk that was showing off this new featur...'
---

By Matías Hernández

The team behind React thought it'd be a great way to end the year by dangling a new feature for the already popular library out in front of developers.

On December 21st the team revealed a [talk](https://reactjs.org/blog/2020/12/21/data-fetching-with-react-server-components.html) that was showing off this new feature, called React Server Components (RCS). In the talk  [Dan Abramov](https://twitter.com/dan_abramov), [Lauren Tan](https://twitter.com/sugarpirate_), [Joseph Savona](https://twitter.com/en_JS), and [Sebastian Markbåge](https://twitter.com/sebmarkbage) explained the reasoning behind this feature and some of its use cases.

Keep in mind that this feature is a complete experiment that doesn't even have public documentation beyond the [RFC](https://github.com/reactjs/rfcs/blob/bf51f8755ddb38d92e23ad415fc4e3c02b95b331/text/0000-server-components.md) that the team published.

> We are sharing this work in the spirit of transparency and to get initial feedback from the React community. There will be plenty of time for that, so don’t feel like you have to catch up right now!

So, what is this all about?

Let's start by clarifying some of the main concepts behind React Server Components so that we can understand the proposal and some similar techniques that are available today.

## What are React Server Components?

React Server Components (RSC) are similar to **server-side rendering (SSR)** but they work slightly differently. 

Basically, SSR takes a React component and renders it in the server when a request is made. This generates an HTML **string** that is sent to the browser to be painted on the screen. Then, if it is required, it will load the related JavaScript through the hydration process. Finally, it goes through the standard application cycle: **Client Side Rendering**.

React Server Components are similar to what Next.js does with **getInitialProps**. The **Server Components** can fetch data and pass that data down to the client components, but this new technique is more _"dynamic"_. It lets you retrieve a full tree of components from the server and inject it into the client application without losing the client's state. 

Another difference with SSR is that, with this implementation, the JavaScript code generates and renders a string of HTML in the server. This creates the visible part of the website, a sort of HTML template. This template is then sent to the server along with the JavaScript code required for interactivity. 

This allows the application to have a blazing fast initial load and paint. But on the other hand, it has interactive code that could take a bit more time because of the hydration process.

Server components compliment SSR, creating a middle ground abstraction that enables the rendering process without adding any size or code to the JavaScript bundle. 

In other words, the server components are not added as JavaScript code into the bundle. This significantly decreases – by around 19% to 29% – the amount of JavaScript that the browser has to parse and execute.

> [RFC]: If we migrate the above example to a Server Component we can use the exact same code for our feature but avoid sending it to the client - a code savings of over 240K (uncompressed).

## Will SSR be replaced by React Server Components? 

There are currently some meta-frameworks that enable a very good implementation of the SSR technique. And the most well-known in this realm is [Next.js](https://nextjs.org). So you might be wondering - will Next.js be replaced by server components?

No it won't, because both involve different solutions and implementations. The initial adoption of RSC will probably be by a meta framework like Next or Gatsby.

* The server component never arrives to the client. The SSR implementation used by React delivers the component code to the client, thus increasing the size of the code in the browser.
* Server components can access the backend data in any part of the component tree. Current solutions like Next.js can access this data in a limited way by using the method `getServerProps()` (which has its own limitations – it can only be used in a first level page, you cannot fetch server data from other components or some 3rd party npm package, and so on).
* Server Components can be re-fetched while keeping the client state inside the tree. This can be done because the transport mechanism is not just HTML, but rather is similar to the VDOM node definition.

## Want to know more about React Server Components?

I recommended watching the [original talk](https://reactjs.org/blog/2020/12/21/data-fetching-with-react-server-components.html), reading the [RFC](https://github.com/reactjs/rfcs/blob/bf51f8755ddb38d92e23ad415fc4e3c02b95b331/text/0000-server-components.md), and checking out the [demo](https://github.com/reactjs/server-components-demo) of the proposal.

And remember: **you don't need to use or learn** this proposal just yet. But it's good to keep an eye on it and see how it evolves and develops.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/English-Footer-Social-Card.jpg)

🐦  [Follow me in Twitter](https://twitter.com/matiasfha)            ✉️ J[oin to my newsletter](https://matiashernandez.ck.page)            ❤️ [Support my work](https://buymeacoffee.com/matiasfha)


