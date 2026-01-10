---
title: How to Implement Vertical Scrolling in React Using react-router-hash-link
subtitle: ''
author: Israel Chidera
co_authors: []
series: null
date: '2022-09-27T17:42:42.000Z'
originalURL: https://freecodecamp.org/news/how-to-implement-vertical-scrolling-in-react-using-react-router-hash-link
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/ferenc-almasi-L8KQIPCODV8-unsplash.jpeg
tags:
- name: React
  slug: react
- name: react router
  slug: react-router
seo_title: null
seo_desc: 'Smooth scrolling is a feature that makes webpages more usable and allows
  for a better user scrolling experience in most browsers.

  Implementing a smooth page scroll while using react-router-dom has been a problem
  in React.js. So this article, you are ...'
---

Smooth scrolling is a feature that makes webpages more usable and allows for a better user scrolling experience in most browsers.

Implementing a smooth page scroll while using react-router-dom has been a problem in React.js. So this article, you are going to learn how to implement smooth vertical scrolling using the react-router-hash-link package.

### What is react-router-hash-link?

According to its [docs](https://github.com/rafgraph/react-router-hash-link), react-router-hash-link is a solution to React Router's issue of not scrolling to #hash-fragments when using link components to navigate.

### Prerequisites.

You must use _BrowserRouter_ from react-router-dom for react-router-hash-link smooth scrolling to work. To install and use react-router, enter the following command:

```js
npm i react-router-dom 
```

Or for yarn:

```js
yarn add react-router-dom 
```

To understand how to implement vertical scrolling, you will be building a simple landing page with a navbar and three sections.

## How to Use react-router-hash-link

### Step 1: Install react-router-hash-link

To install the react-router-hash-link package, run the following command:

```js
npm install --save react-router-hash-link
```

Or with yarn:

```js
yarn add react-router-hash-link
```

### Step 2: Import the react-router-hash-link package into your React app.

Open your LandingPage.js file and import _hashlink_ from your react-router-hash-link package.

```js
import React from 'react';
import { HashLink } from 'react-router-hash-link';

const LandingPage = () => {
    return (
        <>
            <nav>
            . . .
            </nav>

            <section>
            . . .
            </section>
        </>
    )
}

export default LandingPage 
```

### Step 3: Add the Hashlink component to point to different areas of your app

Add the Hashlink component to your LandingPage.js file like this:

```js
import React from 'react';
import { HashLink } from 'react-router-hash-link';

const LandingPage = () => {
    return (
    <>
        <nav>
            <HashLink smooth to="/#home">
                About
            </HashLink>
        
            <HashLink smooth to="/#services">
            	Profile
            </HashLink>
        
            <HashLink smooth to="/#testimonial">
            	Services
            </HashLink>
        </nav>
        
        <section>
        . . .
        </section>
    </>
    )
}
export default LandingPage 
```

### Step 4: Add the ID of your Hashlink to any element.

When you click on the link with your id, a scroll effect will be implemented. You will see a scroll to the element or the page that has an id that matches the #hashfragment in the link.

```js
import React from 'react';
import { HashLink } from 'react-router-hash-link';

const LandingPage = () => {

    return (
    <>
        <nav>
            <HashLink smooth to="/#home">
            	About
            </HashLink>
            
            <HashLink smooth to="/#services">
            	Profile
            </HashLink>
            
            <HashLink smooth to="/#testimonial">
            	Services
            </HashLink>
        </nav>
        
        <section id=”about”>
        	<h1> About</h1>
            
            <p>
                Lorem ipsum dolor sit, amet consectetur adipisicing elit.
                Vero, nam! Iure officia aut esse tempore accusantium
                explicabo? Corporis deleniti ipsa fuga quas aut neque
                dicta nostrum laboriosam, iusto ullam minima est porro,
                totam saepe. Facilis aliquid praesentium, voluptates rem
                quibusdam sequi numquam illo eius adipisci eaque,
                necessitatibus consectetur, labore vero et ipsum.
                Officiis, ea vero. Praesentium, et. Enim, nostrum illo.
            </p>        
        </section>
        
        <section id=”profile”>
        	<h1> Profile </h1>
            <p>
                Lorem ipsum dolor sit, amet consectetur adipisicing elit.
                Vero, nam! Iure officia aut esse tempore accusantium
                explicabo? Corporis deleniti ipsa fuga quas aut neque
                dicta nostrum laboriosam, iusto ullam minima est porro,
                totam saepe. Facilis aliquid praesentium, voluptates rem
                quibusdam sequi numquam illo eius adipisci eaque,
                necessitatibus consectetur, labore vero et ipsum.
                Officiis, ea vero. Praesentium, et. Enim, nostrum illo.
            </p>
        </section>
        
        <section id=”services”>
        	<h1> Services </h1>
            <p>
                Lorem ipsum dolor sit, amet consectetur adipisicing elit.
                Vero, nam! Iure officia aut esse tempore accusantium
                explicabo? Corporis deleniti ipsa fuga quas aut neque
                dicta nostrum laboriosam, iusto ullam minima est porro,
                totam saepe. Facilis aliquid praesentium, voluptates rem
                quibusdam sequi numquam illo eius adipisci eaque,
                necessitatibus consectetur, labore vero et ipsum.
                Officiis, ea vero. Praesentium, et. Enim, nostrum illo.
            </p>
        </section>
    </>
    )
}

export default LandingPage 
```

And there you have it! You've now implemented smooth scrolling on a simple webpage.

## Conclusion

React-router-hash-link allows you to leverage smooth scrolling seamlessly while using react-router-dom for routing. 

It has a lot of functions including Scroll to top and Scroll with offset functions, so you can explore what else it can do.  

