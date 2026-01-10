---
title: How to Set Up a React App with Parcel
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-29T20:16:24.000Z'
originalURL: https://freecodecamp.org/news/how-to-up-a-react-app-with-parcel
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c997b740569d1a4ca1ff3.jpg
tags:
- name: create-react-app
  slug: create-react-app
- name: Productivity
  slug: productivity
- name: React
  slug: reactjs
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "By Bob Ziroll\nFor a long time Webpack was one of the biggest barriers-to-entry\
  \ for someone wanting to learn React. There's a lot of boilerplate configuration\
  \ that can be confusing, especially if you're new to React. \nEven in a talk trying\
  \ to show how..."
---

By Bob Ziroll

For a long time [Webpack](https://webpack.js.org/) was one of the biggest barriers-to-entry for someone wanting to learn React. There's a lot of boilerplate configuration that can be confusing, especially if you're new to React. 

Even in [a talk trying to show how easy React is to set up](https://youtu.be/BXTU4NmMu8A?t=307), it can be very difficult to try and learn each and every step in the setup process.

Not too long after React was first out of beta, the team at Facebook made [create-react-app](https://github.com/facebook/create-react-app). It was an attempt to make spinning up a (very fully-loaded version of a) React app as simple as typing a single command:

```js
npx create-react-app my-app
```

Nice! And honestly, this ? method of creating a new React app is awesome if you want something that has lots of bells and whistles right from the get-go, **and** you're okay with having your app start as a fairly heavy/large app. 

That heaviness comes from the many dependencies, loaders, plugins, and so on automatically installed as `node_modules` that take up a lot of space for each app. The Finder summary image below is from one of my create-react-app apps. ?

![Image](https://coursework.vschool.io/content/images/2020/07/node_modules.png)

![Image](https://coursework.vschool.io/content/images/2020/07/tfugj4n3l6ez.png)

## Introducing Parcel

[Parcel](https://parceljs.org/) is a "Blazing fast, zero configuration web application bundler." This means it handles a lot of the hard bundling stuff for you under the hood **and** allows you to create a relatively lean setup of React (or any other web project that requires [bundling](https://medium.com/madhash/understanding-the-concept-of-bundling-for-beginners-f2db1adad724)).

So, let's see what it takes to set up the bare bones "Hello World" React app that displays an `h1` element.

### Step 1: Create a new folder for your project

Easy enough. ?

### Step 2: Create your `package.json` file

In terminal, `cd` into the new folder and run:

```bash
npm init -y
```

This automatically creates the `package.json` file.

### Step 3: Install Parcel, React, and ReactDOM

```bash
npm install --save-dev parcel-bundler
# Shorthand version: npm i -D parcel-bundler

npm install react react-dom
# Shorthand version: npm i react react-dom
# Note that npm will automatically save dependencies to package.json now, so there's no longer a need to do npm install --save ...
```

### Step 4: Add a "start" script to `package.json`

In the `package.json` file, in the "scripts" section, add the following "start" script:

```json
"start": "parcel index.html --open"
```

### Step 5: Create the `index.html` file and add a couple lines

In VS Code, you can create a new file called `index.html` and use the built-in [emmet](https://code.visualstudio.com/docs/editor/emmet) shortcut to create a standard boilerplate HTML file by typing an exclamation point and hitting the Tab key on your keyboard.

![Image](https://coursework.vschool.io/content/images/2020/07/Screen-Shot-2020-07-29-at-10.17.34-AM.png)
_Type ! and hit the Tab key_

![Image](https://coursework.vschool.io/content/images/2020/07/Screen-Shot-2020-07-29-at-10.18.10-AM.png)
_? Poof!_

Before we move on, we need to add 2 things:

1. A `div` placeholder where our React app will be inserted
2. A `script` to read in the JavaScript entry file (which we will create next)

In the `body` of `index.html`, add:

```html
<body>
    <div id="root"></div>
    <script src="./index.js"></script>
</body>
```

### Step 6: Create the `index.js` file

Create a new file called `index.js` and enter your bare bones React code:

```js
// index.js
import React from "react"
import ReactDOM from "react-dom"

ReactDOM.render(<h1>Hello world!</h1>, document.getElementById("root"))

```

### Step 7: Start it up!

That's it! Now from the terminal, run:

```bash
npm start
```

Parcel will handle the rest, and you'll have a fully-functional React app.

## Conclusion

If you're interested, take some time to [peruse the Parcel documentation](https://parceljs.org/getting_started.html) to better understand all the awesomeness that comes with using Parcel, without requiring any configuration on your end. 

Out of the box, Parcel comes with support for all kinds of common web development extensions, transpilers, syntaxes, and so on.

Although it's not _tiny_, the node_modules from a Parcel app take up 50% less space on your computer:

![Image](https://coursework.vschool.io/content/images/2020/07/Screen-Shot-2020-07-29-at-10.31.58-AM.png)

Thanks, Parcel!

