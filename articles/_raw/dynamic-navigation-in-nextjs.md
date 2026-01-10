---
title: Dynamic Navigation in Next.js – How to Render Nav-Items Dynamically in a Next
  App
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-09-16T17:32:33.000Z'
originalURL: https://freecodecamp.org/news/dynamic-navigation-in-nextjs
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/dynamic-nav-cover.jpg
tags:
- name: Next.js
  slug: nextjs
- name: Web Applications
  slug: web-applications
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Caleb Olojo

  I''ve lately been noticing a pattern in React applications: developers protect certain
  routes on a web app from unauthorized users.

  In such cases, the navigation item (nav-item) on the navigation bar/Header of the
  web won''t be visible t...'
---

By Caleb Olojo

I've lately been noticing a pattern in React applications: developers protect certain routes on a web app from unauthorized users.

In such cases, the navigation item (nav-item) on the navigation bar/Header of the web won't be visible to an unauthorized user.

In this short guide, we're going to take a look at how to do this in NextJS. We are going to render a nav-item dynamically on the navigation bar of a simple webpage that we'll be building here.

### Prerequisites

Before you read this article any further, you should have some basic knowledge of:

* How React works
* NextJS, a production ready framework of React.
* Conditional rendering in React.
* PropTypes checking in React
* import and export statements in JavaScript. You can take a look at this [article](https://seven.hashnode.dev/understanding-import-and-export-statements-in-javascript) to get familiar with it.

## Getting Started

Since this article focuses on Next.js, we'll start by creating a Next.js project. Type the command below in your terminal to install it:

```bash
npx create-next-app [name-of-your-webapp/website]
```

The command above gets all the dependencies we need to get our Next app up and running in no time. 

Keep in mind that the file structure of a Next app is quite different from the ubiquitous create-react-app architecture.

Let's take a look at the important files that we will be interacting with in this article: 

```md
|--pages
|   |-- _app.js
|   |-- index.js
|   |-- about.js
|   |-- blog.js
|   |__ services.js
|--src
|   |-- components
|   |      |-- Header.js
|   |      |__ NavItem.js 
|   |-- data.js
|__
```

The file structure above is an excerpt of the files in the Next.js app architecture. Now let's see what's going on here.

## The Components in Our Next.js App

We'll take a look at all the components you see above and their roles. We'll start by breaking down the files in the `pages` folder.

* `_app.js`: this is the root file of the code base. It is quite like the `index.js` file in `create-react-app`. Here, you can apply any global style(s), add new themes, provide context to the whole application, and so on.

```js
import Head from "next/head";
import React from "react";

function MyApp({ Component, pageProps }) {
  return (
    <React.Fragment>
      <Head>
        <meta name="theme-color" content="#3c1742" />
      </Head>
      <Component {...pageProps} />
    </React.Fragment>
  );
}

export default MyApp;

```

The snippet above shows the content of `_app.js`. The `Head` component that gets imported from `"next/head"` is so we can add document titles to the unique pages and a lot of `meta` tags for the sake of SEO.

* `index.js`: Nextjs abstracts away the need to start using `BrowserRouter` from the `react-router-dom` library to set up the routes in your applications. Instead, any file that is inside the `pages` folder becomes a route. `index.js` becomes accessible at `https://localhost:3000/` once we start the development server with `npm run dev`.

You might notice that we've already imported the `Header` component from the `src/component` folder. Do not fret. We'll get to that section soon.

```js
import Head from "next/head";
import Header from "../src/components/Header";

export default function Home() {
  return (
    <>
      <Head>
        <title>Caleb's article examples</title>
        <link rel="icon" type="image/ico" href="/img/goals.ico" />
      </Head>
      <Header />
      <section>
        <h1>Home Page</h1>
        <section id="contact">
          <h3 className="section-title">Contact Us</h3>
          <p className="section-body">
            You can Contact us via our various social media handles
          </p>
        </section>
      </HomeWrapper>
    </>
  );
}

```

* The remaining page components: `about.js`, `blog.js` and `services.js` can be accessed at `http://localhost:3000/about`, `http://localhost:3000/blog` and `http://localhost:3000/about` respectively

## How to Map Array Items onto the Header Component

Instead of hard-coding the user interface of the nav-bar, we can use JavaScript's `map()` function to render a list of items on the Header component.

To do this, we need to move into the `data.js` file in the `src: source` folder. We'll create an array of objects that will hold the information or items that we would like to render.

The snippet below shows the list of items we want to render. Notice that the last object has a `path` property that is quite different from the others. Instead of a `"/contact"` value, it has a `"#contact"` value. This is because the contact section is on the home page.

```js
export const navLinks = [
  { name: "Home", 
   path: "/" 
  },
  {
    name: "About Us",
    path: "/about",
  },
  {
    name: "Services",
    path: "/services",
  },
  {
    name: "Blog",
    path: "/blog",
  },
  {
    name: "Contact Us",
    path: "#contact",
  },
];
```

Let's continue on to create the Header component by mapping the array of objects that we have in `data.js`. To do that, we have to import the array from that file so we can have access to its properties.

```js
import React from "react";
import { navLinks } from "../utils/data";
import Link from "next/link";

export default function Header() {
  return (
    <header>
      <div className="brand">
        <h3>Example</h3>
      </div>
      <nav>
        {navLinks.map((link, index) => {
          return (
            <ul>
              <Link href={link.path}>
                <li key={index}>{link.name}</li>
              </Link>
            </ul>
          );
        })}
      </nav>
    </header>
  );
}

```

With what we have in the snippet above, if we click on the **"Contact Us"** nav-item, the current route will be: `https://localhost:3000/#contact`. 

The browser scrolls to the HTML element that has an id of "contact". If there isn't any such section, nothing is being scrolled to in the viewport.   
  
That is why we need to render this particular nav-item only on pages that have the corresponding section. Let's take a look at how to achieve that in the next section.

## How to Conditionally Render the Nav-Item with the Next.js `useRouter` Hook

We have to know when another page/route is currently active or "in-view" in a browser tab so that we can set a condition for rendering the nav-item in the appropriate page.

Fortunately for us, Next's `useRouter` hook lets us do that. Let's see how:

```js
import React from "react";
import { useRouter } from "next/router";
import propTypes from "prop-types";

const NavItem = ({ item }) => {
  const router = useRouter();
  return <>{router.pathname === "/" ? item : ""}</>;
};

export default NavItem;

// proptypes check
NavItem.propTypes = {
  item: propTypes.string,
};
```

The snippet above is quite straightforward. We're passing `item` as props to the `NavItem` component so that it makes it dynamic to use in any case, not for the contact nav-item only.

See how we assigned the `useRouter()` hook to the `router` variable? With that, we can access the properties of the hook itself. You can read about the properties of the hook [here](https://nextjs.org/docs/api-reference/next/router#router-object).

```js
router.pathname === "/" ? item : ""
```

The ternary operation above checks if the `pathname` of the page is equal to the homepage, that is `"/"`.

If the result is true, it assigns the value as props to the component (which will always be a string, because of the prop validation check). If not, it assigns an empty string to the component, which in turn ends up as nothing in the Header component.

## Final Touches

Now, let's edit the last item in the `navLinks` array to look like the following:

```js
import NavLink from "./NavLink";

export const navLinks = [
  { name: "Home", 
   path: "/" 
  },
  {
    name: "About Us",
    path: "/about",
  },
  {
    name: "Services",
    path: "/services",
  },
  {
    name: "Blog",
    path: "/blog",
  },
  {
    name: <NavLink item="Contact Us" />,
    path: "#contact",
  },
];
```

## Conclusion

Here's the end result of what we've been building. You'll see that I added some content to illustrate the smooth scroll behaviour to the contact section.

At the click event of the other routes, the contact nav-item isn't on the Header anymore.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/fixed.gif)

Thank you for reading this article! I hope it has helped you gain insight on how to render UI dynamically, based on certain conditions. Kindly share this piece with your peers. 

