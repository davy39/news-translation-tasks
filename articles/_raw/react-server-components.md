---
title: React Server Components Explained
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-12-29T20:56:01.000Z'
originalURL: https://freecodecamp.org/news/react-server-components
coverImage: https://www.freecodecamp.org/news/content/images/2020/12/Untitled-design--1-.png
tags:
- name: React
  slug: react
seo_title: null
seo_desc: 'By Mehul Mohan

  Last week, the React team released a new feature called React Server Components
  (RSC). In this article, I would like to give you my perspective on a few aspects
  of RSC.

  Can''t I run React on servers already?

  Yes you can. React has suppo...'
---

By Mehul Mohan

Last week, the React team released a new feature called React Server Components (RSC). In this article, I would like to give you my perspective on a few aspects of RSC.

## Can't I run React on servers already?

Yes you can. React has supported server-side rendering for a long time using the `react-dom/server` package, which is a react renderer for static HTML from React components.

However, notice that `react-dom/server` has a simple job: it takes the React tree, and converts it into a static HTML markup. 

You have to rehydrate the state (using `ReactDOM.hydrate`), add any interactivity using client side JavaScript, and take care of navigation, caching, and a million other things yourself. 

Frameworks like Next.js do a lot of the heavy lifting for you already, but that's for another day.

## So how do React Server Components differ from Server-Side Rendering?

Server components are not a _full_ SSR. Think of a React website as a hierarchy of components like the following:

![Image](https://www.freecodecamp.org/news/content/images/2020/12/tree.png)

Let's use Next.js as an example for SSR as it is the most common SSR framework for React. Next.js (SSR) gives you the ability to do the following:

1. Complete static export of site with no JS
2. Partial static export per page (experimental Next.js feature)
3. Complete SSR of the tree (and then rehydrating it, and so on)
4. Splitting components using dynamic import rendered on client as a React module.
5. Splitting components using dynamic import rendered on server as a React module.

Can you guess what is missing (or rather _not_ missing) here? In the static exports from Next, you cannot statically export a component unless you create a page for it. 

And even if you do so, you lose the ability to have dynamic data updates triggered from some user action (unless you use another backend API server with client, making UI non-SSR).

It might be hard to see right now, but React Server Components fill this gap. Consider the above graph again and the above 5 points again:

1. Complete static export means all nodes in the graph above are complete HTML documents with no JS. Right now consider `1` node as a single page, and assuming there are multiple such roots, all pages are completely HTML based.
2. Partial static export means only the single root (single page) would be static HTML (`1` in this case)
3. Complete SSR means the whole website (or page) is rendered every time on demand. This involves rendering the page from top to bottom and then re-hydrating the page with React (add a sprinkle of caching at _expensive_ places if you want to)
4. Splitting components using dynamic import rendered on client as a React module - this means that some nodes (say `4` and `7`) will not be rendered on server and raw JS code for their components will be sent down the wire, and will run like a regular client-side JS React component. Because `4` and `7` are not rendered on the server, this automatically applies for their children, too (8, 9, 14).
5. Splitting components using dynamic import rendered on server as a React module - this is the closest approach to RSC. Here, we split the component code into different bundles (chunks), render it on server, and send it down the wire only when the client requests it (for example - typing in a search field or a button click).

So the question now becomes, how is RSC different from Next.js dynamic import rendered on server?

## RSC vs Dynamic Import Rendered on Server

Until now, dynamic import rendered on servers would always be downloaded and used as regular React components. This means that you need to spend a few CPU cycles on the dynamic chunk you got down and fit it into the client side React DOM. 

React Server Components for clients, well, are not components at all. They're _something else._

First of all, your React Server Components can update only a small part of the UI (the component). They differ from typical SSR in that they never send down static HTML on the first load. 

If you use React without SSR but with RSC, your first load will look pretty much how a regular client side React looks (with no HTML content).

Let's consider an app which uses a search bar to search for movies, linked to a database on your backend. Let's say the search results are actually a React Server Component, not a regular component. In case of a regular component, this is what might happen:

1. As soon as you type, a `fetch` request is made to some remote API for a JSON payload.
2. As soon as you get the data back, you parse it as JSON, and give it to React.
3. React renders the results component from the JSON data, and displays the movie information.

Simple enough. With RSC, the following will happen:

1. A network request is made to a backend you own which is capable of RSC rendering.
2. The component is rendered on the server itself (step 2 and 3 above), and you are sent a static markup build of the data _in a non-JSON/non-HTML format right now_ (this might change in the future)
3. The frontend renders this markup as a _static UI_ (important: not as a React component). This saves additional processing of the component on the front end.

With dynamic import rendered on server, well, it doesn't make much sense because your client cannot tell your "dynamic import" chunk to render a state dependent UI. This is because dynamic imports are just there for performance reasons.

When you use RSC, there are a bunch more things to note:

1. You cannot make your server components interactive (because they're just chunks of UI updates)
2. You can, however, include client side components inside your server side components which could be interactive and would render like you'd expect them to.
3. Your UI from server is automatically in sync with the client side state as you never "destroy and create" components while updating parts of UI on your own – React does that for you.

## Conclusion

That's all! I hope this article helps you understand RSC more clearly. The tech is new and can be integrated with frameworks like Next.js too. Let's see what the future holds. 

Want to learn more? There's a very good 57-minute official video from the React team that dives deep into RSC, demo included. You can check it out [here](https://www.youtube.com/watch?v=TQQPAU21ZUw).

If you liked the article, you can follow me on [twitter](https://twitter.com/mehulmpt) for more such stuff :)

