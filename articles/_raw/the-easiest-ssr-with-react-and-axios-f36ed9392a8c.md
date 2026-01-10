---
title: The easiest way to set up server-side rendering with React and axios
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-19T11:38:22.000Z'
originalURL: https://freecodecamp.org/news/the-easiest-ssr-with-react-and-axios-f36ed9392a8c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*xHyQy7jPsssJTQaWcrgc3A.jpeg
tags:
- name: axios
  slug: axios
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Simone Busoli

  Server-side rendering (SSR) is a double-edged sword. It’s terribly important for
  certain applications that require SEO support and meeting certain performance requirements,
  but it’s nasty to implement properly.

  Some of the major diff...'
---

By Simone Busoli

Server-side rendering (SSR) is a double-edged sword. It’s terribly important for certain applications that require SEO support and meeting certain performance requirements, but it’s nasty to implement properly.

Some of the major difficulties revolve around user authentication and data pre-loading, especially because there are no established patterns around these.

When building a SPA, often you would use JWT for user authentication, sent via HTTP headers to the server. For data loading instead, you may use React component hooks like `componentWillMount`. But none of these work when rendering your component tree on the server.

#### ? The idea

You may have heard that not so long ago React introduced support for a new feature called [hooks](https://reactjs.org/blog/2019/02/06/react-v16.8.0.html). This is particularly interesting because hooks are executed whenever the component renders, which opens up a scenario that wasn’t possible until now.

If hooks are executed when the component which uses them is rendered, it means that they’re executed both when rendering on the client and on the server. As a consequence of this, if a hook does an HTTP request and the library we use for doing that works both on the client and on the server, it means that we get HTTP requests on the client and on the server for free! ?

[axios](https://github.com/axios/axios) is one such library, besides being my favorite one.

#### ⚙️ The implementation

It turns out that the idea has a reasonably straightforward implementation.

Let’s assume that you have already implemented Server Side Rendering in your React application.

> If you haven’t done so already, there are plenty of tutorials and examples out there. My favorite is found in the Redux [documentation](https://redux.js.org/recipes/server-rendering).

Let’s assume we now create a hook called `useAxios`. In its simplest form, it would look something like this:

If you’ve used hooks this shouldn’t look too complicated.

We’re using a `React.useState` hook to keep the value of the axios response, and a `React.useEffect` hook to trigger the axios request.

Using this hook would be as simple as this:

If you think this is cool, wait until you figure out - like I did - that this approach makes it super easy to implement data loading during Server Side Rendering.

If you think about it, what’s the complexity involved in pre-loading data on the server?

All that is involved is:

* triggering HTTP requests
* waiting for responses
* sending the data to the client along with the generated markup
* make the client load the data so that it won’t execute those HTTP requests again, but simply bind the data to the components that need it

Now, even though the concept is simple, it requires a bit of coding, hence why I built a library which encapsulated all this logic. It’s basically an extension to the simple implementation seen above, but rather than a dozen lines of code it’s ~100. Considering the features it provides and that using it is still pretty much a one-liner, I find it very exciting!

#### ? Building axios-hooks

You can check out the code already. The library is called [axios-hooks](https://github.com/simoneb/axios-hooks/) and you can install it with:

`npm install axios-hooks`

You will find several examples in the documentation, with accompanying `codesandbox.io` demos to get you started quickly. The usage is very simple but what I’m more interested in explaining is how it works, especially because it’s something that can be applied to many other hooks.

Using it on the client is already useful, because it takes away the pain of using React lifecycle hooks and component state. That’s unless you use a higher-order state management library, in which case you’re probably solving this problem in a different way altogether.

The biggest benefit, though, is combining it with Server Side Rendering. Here’s how it works:

1. The server renders the component tree, i.e. via the `renderToString` function of the `react-dom/server` package
2. `useAxios` hooks are triggered and HTTP requests started
3. `axios-hooks` keeps a list of all the requests and caches the responses as they come back
4. The server code awaits for those requests to complete and extracts a serializable representation of them, which can be rendered along with the markup generated by rendering the component tree. This is sent back to the client
5. The client, before hydrating the component tree, fills the `axios-hooks` cache with the data returned by the server
6. The client hydrates the component tree and `useAxios` hooks are triggered again. Because the data is already there, no actual HTTP request is made on the client

The concept is astonishingly simple, as is the implementation.

Checkout ? a`[xios-hooks](https://github.com/simoneb/axios-hooks/)` today and post your feedback!

#### Credits

Credits for the original idea of leveraging React hooks in Server Side Rendering scenarios go to the cool guys at [NearForm](https://www.nearform.com), who built the awesome `[graphql-hooks](https://github.com/nearform/graphql-hooks)` library.

