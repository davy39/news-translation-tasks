---
title: Change the world, one line of code at a time
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-01T22:22:01.000Z'
originalURL: https://freecodecamp.org/news/change-the-world-one-line-of-code-at-a-time-5162b229f35e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*cHz2cUq8zLjjSsB_e9vexw.jpeg
tags:
- name: coding
  slug: coding
- name: Inspiration
  slug: inspiration
- name: JavaScript
  slug: javascript
- name: Life lessons
  slug: life-lessons
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Usheninte Dangana

  People like to look at changing the world as a big task. I believe changing the
  world can be done in little steps.

  The key is identifying a problem and taking a little step.

  My journey began on Friday, September 7th, 2018. That w...'
---

By Usheninte Dangana

People like to look at changing the world as a big task. I believe changing the world can be done in little steps.

The key is identifying a problem and taking a little step.

My journey began on Friday, **September 7th, 2018**. That was the day I decided to build a React plugin for the freeCodeCamp Test Suite. I noticed a problem and I took action.

There is a [working version](https://www.npmjs.com/package/react-fcctest) up for installation on the Node Package Manager registry. This is a milestone for me, as the project is my first Open Source contribution.

I used certain key technologies to build the project, like Webpack, React, NPM, and Node.js. I had a lot of fun building it, and I learned a lot, too.

I tried several times (for a whole day actually) before I could even succeed in making the plugin work.

After making it work, implementation in a React app was a challenge. Although I was faced with technical difficulties, in the end, the plugin worked.

### The process

The idea behind the project was simple. All I wanted to do was find a simple way to add the freeCodeCamp Test Suite to React apps.

My first plan was to build it with Create-React-App.

I felt that since I could use it to build React applications, I could use it to build a plugin. I was wrong.

Create-React-App was too heavy for what I needed to build.

I discovered that to make the plugin easy to export, I would need some extra configuration.

I went online and googled a couple of times, and came across Webpack and react-helmet. What I came across was both amazing and confusing, at first.

Still, I knew they were what I needed. I continued searching some more.

Before Webpack, I had tried exporting and publishing the plugin as a module with no extra configuration. It did not work. Newbie mistake, I know.

This was a big challenge that I had to overcome.

Thankfully, we learn as we grow!

While I was developing the plugin, there were constant power cuts. In Nigeria, the power situation is not very settled.

I had to work until my laptop powered out, then think deeply about what to do when power returned.

All of this happened on the second day (Saturday).

### The magic, the beauty

Using Webpack, I began building the plugin.

I placed the core code in an index.js file. Here is the code below:

```js
import React from 'react';
import { Helmet } from 'react-helmet';
import './styles.css';

const ReactFCCtest = () => {
  return (
    <div>
      <Helmet>
        <script type="text/javascript" 
                src="https://cdn.freecodecamp.org/testable-projects-fcc/v1/bundle.js" >
        </script>
      </Helmet>
      <h5>react-fcctest running</h5>
    </div>
  );
};

export default ReactFCCtest;
```

The code above was all I needed to add the script to the head tag of any React app I desired.

I came across an [article on Medium](https://medium.com/dailyjs/building-a-react-component-with-webpack-publish-to-npm-deploy-to-github-guide-6927f60b3220) which was a great help to me.

It helped me understand how to use Webpack to create a node module that I could successfully publish to the Node Package Manager registry.

I followed the instructions in that article. After making some changes, I built the following **webpack.config.js** file:

```js
const path = require('path');
const HtmlWebpackPlugin = require("html-webpack-plugin");
const htmlWebpackPlugin = new HtmlWebpackPlugin({
    template: path.join(__dirname, "demo/src/index.html"),
    filename: "./index.html"
});
module.exports = {
    entry: path.join(__dirname, "demo/src/index.js"),
    output: {
        path: path.join(__dirname, "demo/dist"),
        filename: "bundle.js"
    },
    module: {
        rules: [
            {
                test: /\.(js|jsx)$/,
                use: "babel-loader",
                exclude: /node_modules/
            },
            {
                test: /\.css$/,
                use: ["style-loader", "css-loader"]
            }
        ]
    },
    plugins: [htmlWebpackPlugin],
    resolve: {
        extensions: [".js", ".jsx"]
    },
    devServer: {
        port: 3001
    }
};
```

Let me explain what this file is doing:

>> First, it is using the HtmlWebpackPlugin to create an HTML file to serve my webpack bundle.

>> Next it is exporting the plugin I created as a node module.

>> It is saying that the entry point of my plugin is in the location `demo/src/index.js`. This means that this is where the code to be exported will be taken from.

>> Next, it is saying that the output directory of my plugin is  `demo/dist`. In this directory**, the react-fcctest** plugin will be exported in a file named  `bundle.js`.

>> Next it introduces a set of rules for the file that is to be exported.

>> The rules, tell the file to do two things. One, use babel-loader when working with  `.js` and `.jsx` files and do not include the `node_modules` folder. Two, use style-loader and css-loader when working with `.css` files.

>> The resolve and extensions part of the file allowed me to leave of the `.js` and `.jsx` from the end of my files while importing them.

>> Lastly, my development server was on port 3001. This port could have been any other of my choosing.

> I just noticed that beauty involves hard work…

I added Webpack to the project on Sunday, and then the plugin worked!

With this, I was able to create a module that could be easily exported. This module was **ReactFCCtest**.

I cannot say how much the **read-search-ask** methodology helped me throughout the project.

Here is [Demo](https://usheninte.github.io/react-fcctest/) of the finished plugin. It was very fun to build.

I tested it out in a freeCodeCamp project, and it worked perfectly.

![Image](https://cdn-media-1.freecodecamp.org/images/1*OL4Q9xvDLtsMcgY21--tOQ.gif)
_Credit: [https://giphy.com](https://giphy.com/" rel="noopener" target="_blank" title=")_

I created a [Github Repository](https://github.com/Usheninte/react-fcctest) that holds all the open source code for the project.

### **How to install and use `react-fcctest`**

Run `npm i react-fcctest` or `yarn add react-fcctest` to install the React plugin.

Place `import ReactFCCtest from 'react-fcctest';` in your App.js:

```js
import React, { Component } from 'react';
import ReactFCCtest from 'react-fcctest';

class App extends Component {
  render() {
    return (
      <div>
        <ReactFCCtest />
      </div>
    );
  }
};

export default App;
```

That is all there is to it!

#### Final notes

My 2018 so far has been amazing.

I am now the Developer Student Club Lead for my university, in a program powered by **Google Developers** in Sub-Saharan Africa.

I am aiming for greatness, in outer space — perhaps I might just land on a moon. [Follow me](https://twitter.com/Usheninte) on my journey.

