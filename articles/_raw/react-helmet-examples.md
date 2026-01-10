---
title: How to Use React Helmet – With Example Use Case
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-10-05T16:36:10.000Z'
originalURL: https://freecodecamp.org/news/react-helmet-examples
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/react-head-examples.jpg
tags:
- name: React
  slug: react
seo_title: null
seo_desc: 'By Scott Gary

  Because of the nature of single page applications (SPAs), modifying metadata in
  React apps can be tricky without using a helper library. Lucky for us, that library
  already exists – and it''s called React Helmet.

  Leveraging Helmet for met...'
---

By Scott Gary

Because of the nature of single page applications (SPAs), modifying metadata in React apps can be tricky without using a helper library. Lucky for us, that library already exists – and it's called React Helmet.

Leveraging Helmet for metadata inclusion can significantly simplify the process of making a React app SEO and social media friendly.

Helmet lets us insert metadata into the <head> tag in much the same way we would using standard HTML syntax.

In this article, we'll cover the following steps:

1. How to install and import the React Helmet library.
2. Basic usage for client and server side rendering (CSR vs SSR).
3. More advanced usage of Helmet for setting up an SEO component.

In order to understand these topics, you should have a basic knowledge of the React library.

## React Helmet Installation and Setup

If you're already familiar with using React and Node, installing Helmet should be a breeze.

However, before demonstrating, it's important to note that the standard **react-helmet** library is now considered deprecated. Instead, you should use **react-helmet-async**.

This is because react-helmet led to a few bugs that resulted in memory leaks and poor data integrity. Suffice it to say, when React developers mention Helmet, they're almost always referring to **react-helmet-async**.

Now to the installation. Simply navigate to your project's directory in the terminal, and install react-helmet-async with your package manager of choice. Here's the syntax for yarn and npm:

```
yarn add react-helmet-async
npm i react-helmet-async
```

Once the installation completes, you can move on to importing and utilizing the Helmet component library.

## React Helmet Basic Concepts and Usage

The two components we'll be importing from **react-helmet-async** are called **Helmet** and **HelmetProvider**.

1. **HelmetProvider** will wrap the entire app component in order to create context and prevent memory leaks. Therefore, this component will only need to be imported in the root **App** component.
2. **Helmet** will be imported into any page component where you want to implement meta tags. Think of **<Helmet>** as the **<head>** tag for the page in question.

We're going to start with basic usage of both client side rendering (CSR) and server side rendering (SSR). Let's start by seeing how things work in a basic CSR implementation:

```javascript
import React from 'react';
import { HelmetProvider } from 'react-helmet-async';
import NavBar from './NavBar';
import Landing from `./Landing;
export default function App() {
return (
<HelmetProvider>
<NavBar />
<Landing />
</HelmetProvider>
)}
```

As you can see, in the **App** component we only imported the `HelmetProvider` component from **react-helmet-async**. Pretty simple.

The SSR implementation is very similar, with one small addition. Let's have a look and see if you can spot the difference:

```javascript
import React from 'react';
import { HelmetProvider } from 'react-helmet-async';
import NavBar from './NavBar';
import Landing from `./Landing;
export default function App() {
const helmetContext = {};
return (
<HelmetProvider context={helmetContext}>
<NavBar />
<Landing />
</HelmetProvider>
)}
```

If you noticed the addition of the **helmetContext** variable being passed as a prop to our **HelmetProvider**, you nailed it!

This paradigm is found using most popular state management systems such as Redux, and helps ensure that context is never scoped outside of the current instance of your app.

Now, let's assume the following page component is the landing page for your React app:

```javascript
import React from 'react';
import { Helmet } from 'react-helmet-async';
export default function Landing() {
return (
<div>
<Helmet>
<title>Learning React Helmet!</title>
<meta name='description' content='Beginner friendly page for learning React Helmet.' />
</Helmet>
<h1>Cool Landing Page!</h1>
</div>
)
}
```

A quick review of the Landing page component shows that we imported the **Helmet** component, and used it to add the _title_ and _description_ metadata to the page.

We simply add the HTML equivalent meta tag inside the Helmet component, and the work of adding this to the **<head>** HTML tag is handled for us.

Awesome! We're now on the road to creating an SEO-friendly React app.

## Creating an SEO Component With React Helmet

Metadata isn't only about Google search results. We also want social media posts that reference our site to show up as cool preview cards.

When it comes to metadata and meta tags, there's a ton of different variants to remember. Facebook uses **og** (open graph) tags, Twitter uses its own **twitter** variant, and so on.

## How to Use Components for Abstraction

One cool thing about creating React components with props is that you can reuse a prop inside the component however you please.

Using this knowledge, you can create a component called SEO that abstracts away the usage for commonly used metadata tags, saving you from having to track down each tag variant every time you build an SEO-friendly app.

An example SEO component that streamlines the process of adding Facebook and Twitter tags could look like this:

```javascript
import React from 'react';
import { Helmet } from 'react-helmet-async';
export default function SEO({title, description, name, type}) {
return (
<Helmet>
{ /* Standard metadata tags */ }
<title>{title}</title>
<meta name='description' content={description} />
{ /* End standard metadata tags */ }
{ /* Facebook tags */ }
<meta property="og:type" content={type} />
<meta property="og:title" content={title} />
<meta property="og:description" content={description} />
{ /* End Facebook tags */ }
{ /* Twitter tags */ }
<meta name="twitter:creator" content={name} />}
<meta name="twitter:card" content={type} />
<meta name="twitter:title" content={title} />
<meta name="twitter:description" content={description} />
{ /* End Twitter tags */ }
</Helmet>
)
}
```

As shown above, our component accepts four props: title, description, name, and type. Using these four props, we were able to distribute the values across nine different types of meta tags!

Here’s an example of how we could implement this component in our **Landing** page component:

```javascript
import React from 'react';
import { SEO } from './SEO’;
export default function Landing() {
return (
<div>
<SEO
title=’Learning React Helmet!’
description=’Beginner friendly page for learning React Helmet.'
name=’Company name.’
type=’article’ />
<h1>Cool Landing Page!</h1>
</div>
)
}
```

So, all we had to do is pass in our four props, and our custom SEO component handles all the heavy lifting of creating the multiple different types of metadata tags. Nice.

This example is far from an exhaustive list of meta tags. It doesn't take much imagination to visualize how useful this component would be if you wanted to include all relevant meta tags for your site. 

## Conclusion

In this article we went over why React Helmet is a useful addition to your React app. You learned not only basic setup and usage, but also a more advanced implementation that helps abstract away much of the repetitive work involved in metadata tags.

Hopefully you now feel confident enough to enhance your [React SEO](https://www.ohmycrawl.com/react-seo/) and social media performance by implementing the React Helmet Async library. Good luck and happy coding!

For more information on how to set up your JavaScript websites for search engine success, check out [ohmycrawl.com](http://ohmycrawl.com/).

