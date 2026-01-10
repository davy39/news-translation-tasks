---
title: How to Import SVGs in a React and Vite app
subtitle: ''
author: Israel Oyetunji
co_authors: []
series: null
date: '2022-07-01T22:15:02.000Z'
originalURL: https://freecodecamp.org/news/how-to-import-svgs-in-react-and-vite
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/Blog-article-cover-images--3-.png
tags:
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: SVG
  slug: svg
- name: vite
  slug: vite
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'Are you having difficulties importing SVGs into your React app? This is
  a problem that many developers face, especially when setting up a new React app
  with a module bundler.

  In this article, I will share with you the different ways of importing SVGs...'
---

Are you having difficulties importing SVGs into your React app? This is a problem that many developers face, especially when setting up a new React app with a module bundler.

In this article, I will share with you the different ways of importing SVGs in React, as well as how the process works under the hood.

Let's get started.

## What Is an SVG?

SVG, short for Scalable Vector Graphic, is an image format used for rendering two-dimensional (2D) graphics on the internet.

The SVG format stores images as **vectors** which are graphics made up of points, lines, and curves based on geometry and mathematical formulas.

Because they are based on numbers and values rather than a grid of pixels like [raster images](https://en.wikipedia.org/wiki/Raster_graphics)(.png and.jpg), they do not lose quality when zoomed or resized.

They're also great for creating responsive websites that need to look good and function well across a variety of screen sizes.

Overall, SVGs are great as they are scalable, lightweight, customizable, and can be animated using CSS when used [inline](#2usingsvgsbyaddingdirectlyasjsx).

## How to Import SVGs in React Apps

Let's go through some of the most used methods when importing SVGs into React Apps.

### 1\. How to Import SVGs Using the Image Tag

Importing SVGs using the image tag is one of the easiest ways to use an SVG. If you initialize your app using CRA (Create React App), you can import the SVG file in the image source attribute, as it supports it off the bat.

```jsx
import YourSvg from "/path/to/image.svg";

const App = () => {
  return (
    <div className="App">
      <img src={YourSvg} alt="Your SVG" />
    </div>
  );
};
export default App;
```

But if you are not using CRA, you have to set up a file loader system in the bundler you're using (Webpack, Parcel, Rollup, and so on).

Webpack, for instance, has a loader for handling SVGs called [file-loader](https://v4.webpack.js.org/loaders/file-loader/).

To install the file-loader, add the following command:

```bash
npm install file-loader --save-dev
```

Next, add the loader to the `webpack.config.js` file:

```js
module.exports = {
  module: {
    rules: [
      {
        test: /\.(png|jpe?g|gif)$/i,
        use: [
          {
            loader: "file-loader",
          },
        ],
      },
    ],
  },
};
```

Now, you can import your SVG files and use them:

```jsx
import YourSvg from "/path/to/image.svg";

const App = () => {
  return (
    <div className="App">
      <img src={YourSvg} alt="Your SVG" />
    </div>
  );
};
export default App;
```

NOTE: While this approach is straightforward, it does have one disadvantage: unlike the other methods for importing, you cannot style the SVG imported in a `img` element. As a result, it will be suitable for an SVG that does not need customization, like logos.

### 2\. How to Import SVGs by Adding them Directly as JSX

JSX supports the `svg` tag, so we can copy-paste the SVG directly into our React components. This method is straightforward as it helps you take full advantage of SVGs without using a bundler.

The approach is possible because SVGs are in XML format, just like HTML. So, we can convert it to JSX syntax. You can also use a [compiler](https://transform.tools/html-to-jsx) instead of manually converting.

```jsx
const App = () => {
  return (
    <div className="App">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        className="ionicon"
        viewBox="0 0 512 512"
      >
        <path
          d="M160 136c0-30.62 4.51-61.61 16-88C99.57 81.27 48 159.32 48 248c0 119.29 96.71 216 216 216 88.68 0 166.73-51.57 200-128-26.39 11.49-57.38 16-88 16-119.29 0-216-96.71-216-216z"
          fill="none"
          stroke="currentColor"
          strokeLinecap="round"
          strokeLinejoin="round"
          strokeWidth={32}
        />
      </svg>
    </div>
  );
};
export default App;
```

The advantage of including SVGs inline is that we have access to their different properties, which allows us to style and customize them as we see fit.

One thing to keep in mind is that if your SVG file size is large, your code may become complex, reducing readability and productivity. If this is the case, use a png or jpeg file..

### 3\. How to Import SVGs as React Components

If you use CRA, there's a chance you have imported and used SVGs directly as a React component at one point in time.

This method, which is possible with the help of a file loader, works by loading the image alongside the HTML rather than as a separate file.

```jsx
import { ReactComponent as Logo } from "./logo.svg";

const App = () => {
  return (
    <div className="App">
      <Logo />
    </div>
  );
};

export default App;
```

### 4\. How to Convert SVGs to React Components

This approach is similar to the one previously mentioned. Here, we can convert an SVG to a React component by returning it from inside a class or functional component.

To do this, open up the SVG file in a text editor, and copy-paste the code into a new component:

```jsx
export const ArrowUndo = () => {
  return (
    <svg
      xmlns="http://www.w3.org/2000/svg"
      className="ionicon"
      viewBox="0 0 512 512"
    >
      <path d="M245.09 327.74v-37.32c57.07 0 84.51 13.47 108.58 38.68 5.4 5.65 15 1.32 14.29-6.43-5.45-61.45-34.14-117.09-122.87-117.09v-37.32a8.32 8.32 0 00-14.05-6L146.58 242a8.2 8.2 0 000 11.94L231 333.71a8.32 8.32 0 0014.09-5.97z" />
      <path
        d="M256 64C150 64 64 150 64 256s86 192 192 192 192-86 192-192S362 64 256 64z"
        fill="none"
        stroke="currentColor"
        strokeMiterlimit={10}
        strokeWidth={32}
      />
    </svg>
  );
};
```

Now, you can import and render the SVG component in another component like this:

```jsx
import { ArrowUndo } from "./path/to/ArrowUndo.jsx";

export const Button = () => {
  return (
    <button>
      <ArrowUndo />
    </button>
  );
};
```

Again, this approach is only possible if your React app has a loader like SVGR's [Webpack loader](https://www.npmjs.com/package/@svgr/webpack) included.

### 5\. How to Import SVGs Using SVGR

[SVGR](https://react-svgr.com/) is a tool that takes raw SVG files and transforms them into React components. It also has a large ecosystem with support for Create React App, Gatsby, Parcel, Rollup, and other technologies.

So, how do we set it up?

First, install the package by running the code below:

```bash
# with npm
npm install --save-dev @svgr/webpack

# with yarn
yarn add --dev @svgr/webpack
```

Next, update your `webpack.config.js`:

```js
module.exports = {
  module: {
    rules: [
      {
        test: /\.svg$/i,
        issuer: /\.[jt]sx?$/,
        use: ["@svgr/webpack"],
      },
    ],
  },
};
```

Now, you can import an SVG file as a React component:

```jsx
import Logo from "./logo.svg";

const App = () => {
  return (
    <div className="App">
      <Logo />
    </div>
  );
};

export default App;
```

### 6\. How to Import SVGs Using the Vite Plugin for SVGR

[`vite-plugin-svgr`](https://www.npmjs.com/package/vite-plugin-svgr) is a plugin for Vite that uses svgr under the hood to transform SVGs into React components.

You can install it by running the following command:

```bash
# with npm
npm i vite-plugin-svgr

# with yarn
yarn add vite-plugin-svgr
```

Next, add the plugin inside your app's `vite.config.js`:

```js
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import svgr from "vite-plugin-svgr";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [svgr(), react()],
});
```

Now, you can import the SVG files as [React components](#3importingsvgsasreactcomponents):

```jsx
import { ReactComponent as Logo } from "./logo.svg";
```

## Conclusion

And it's a wrap! In this article, we've covered how to import SVGs in a React App using custom configuration from specific packages, how importing React components works, and how to use them in a Vite setup.

When working with Vite, I use the vite svgr plugin, which works flawlessly. You can also experiment with the other ways discussed in this article.

I hope you found this article insightful. If you do have any questions, feel free to send a message on [Twitter](https://twitter.com/israelmitolu) or [LinkedIn](https://www.linkedin.com/in/israeloyetunji/).

Thanks for reading, and happy coding!

Before you go, check out these resources:

* [Why You Should Ditch Create-React-App for Vite](https://israelmitolu.hashnode.dev/why-you-should-ditch-create-react-app-for-vite)
    
* [Working with SVGs in React](https://rossbulat.medium.com/working-with-svgs-in-react-d09d1602a219)
    
* [Twitter Community for Devs](https://twitter.com/i/communities/1532313139810906114)
