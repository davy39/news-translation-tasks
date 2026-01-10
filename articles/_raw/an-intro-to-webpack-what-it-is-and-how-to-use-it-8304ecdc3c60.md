---
title: 'An intro to Webpack: what it is and how to use it'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-15T17:37:32.000Z'
originalURL: https://freecodecamp.org/news/an-intro-to-webpack-what-it-is-and-how-to-use-it-8304ecdc3c60
coverImage: https://cdn-media-1.freecodecamp.org/images/1*6ItHoU8x6M-m7-Pt2UG7cw.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: reactjs
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
- name: webpack
  slug: webpack
seo_title: null
seo_desc: 'By Ashish Nandan Singh

  Introduction

  Okay, so I assume you have heard of webpack — that’s why you are here, right? The
  real question is what do you know about it? You might know a few things about it,
  like how it works, or you might have absolutely no...'
---

By Ashish Nandan Singh

### Introduction

Okay, so I assume you have heard of webpack — that’s why you are here, right? The real question is what do you know about it? You might know a few things about it, like how it works, or you might have absolutely no clue. Either way, I can assure you that after reading this article, you’ll likely feel comfortable enough with the whole **webpack situation**.

After all — **necessity** is the mother of **invention…**

A perfect way to say why webpack exists is the above quote. But to understand it better we need to go back, way back, to when JavaScript was not the new sexy thing, in those old timey ages when a website was just a small bundle of good old _._html, CSS, and probably one or a few JavaScript files in some cases. But very soon all of this was going to change.

#### What was the problem?

The entire dev community was involved in a constant quest of improving the overall user and developer experience around using and building javascript/web applications. Therefore, we saw a lot of new **libraries and frameworks** introduced.

A few **design patterns** also evolved over time to give developers a better, more powerful yet very simple way of writing complex JavaScript applications. Websites before were no more just a small package with an odd number of files in them. They stated getting bulky, with the introduction of **JavaScript modules**, as writing encapsulated small chunks of code was the new trend. Eventually all of this lead to a situation where we had 4x or 5x he of files in the overall application package.

**Not only was the overall size of the application a challenge,** but also there was a huge gap in the kind of code developers were writing and the kind of code browsers could understand. Developers had to use a lot of helper code called **polyfills** to make sure that the browsers were able to interpret the code in their packages.

To answer these issues, webpack was created. **Webpack is a static module bundler.**

#### So how was Webpack the answer?

In brief, Webpack goes through your package and creates what it calls a **dependency graph** which consists of various **modules** which your webapp would require to function as expected. Then, depending on this graph, it creates a new package which consists of the very bare minimum number of files required, often just a single bundle.js file which can be plugged in to the html file easily and used for the application.

Over the next part part of this article I will take you through the step by step setup of webpack. By the end of it, I hope you understand the basics of Webpack. So lets get this rolling…

### What are we building ?

You have probably heard of **ReactJS.** If you know reactJS, you likely know what **create-react-app** is. For those of you who have no idea what either of those two things are, **ReactJS is a UI library** which is very helpful in building intelligent complex UIs, and **create-react-app is a CLI tool** for setting up or bootstrapping a boilerplate dev setup to make React applications.

Today we will be creating a simple React application but without using the create-react-app CLI. I hope this sounds fun enough to you. :)

### Installation Phase

#### npm int

Thats right, thats how almost all good things start: plain old npm init. I will be using VS Code, but feel free to use any code editor you like to get things started.

Before you can do any of this, thought, make sure you have the latest [nodeJS](https://nodejs.org/en/download/) and the [npm](https://www.npmjs.com/get-npm) version installed locally on your machine. Click on each of those links to know more about the process.

```
$ npm init
```

This will create a starter package and add a package.json file for us. This is where all the dependencies required to build this application will be mentioned.

Now for creating a simple React application, we need two main libraries: React and ReactDOM. So let’s get them added as dependencies into our application using npm.

```
$ npm i react react-dom --save
```

Next up we need to add webpack, so we can bundle our app together. Not only bundle, but we will also require hot reloading which is possible using the webpack dev server.

```
$ npm i webpack webpack-dev-server webpack-cli --save--dev
```

The `--save--dev` is to specify that these modules are just dev dependencies. Now since we are working with React, we must keep in mind that React uses ES6 classes and import statements, something that all the browsers may not be able to understand. To make sure that the code is readable by all browsers, we need a tool like babel to transpile our code to normal readable code for browsers.

```
$ npm i babel-core babel-loader @babel/preset-react     @babel/preset-env html-webpack-plugin --save-dev
```

Well what can I say, that was the maximum number of installs I promise. In the case of babel, we have loaded the core babel library first, then the loader, and finally 2 plugins or presets to work specifically with React and all the new ES2015 and ES6 onwards code.

Moving on, let’s add some code and let’s get the webpack configuration started.

This is how the package.json file should look after all the installations so far. You might have a different version number depending on when you are following this article.

### The Code

Let’s start by adding a **webpack.config.js** file in the root of our application structure. Add the following code in your webpack.config file.

```js
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  //This property defines where the application starts
  entry:'./src/index.js',
    
  //This property defines the file path and the file name which will be used for deploying the bundled file
  output:{
    path: path.join(__dirname, '/dist'),
    filename: 'bundle.js'
  },
    
  //Setup loaders
  module: {
    rules: [
      {
        test: /\.js$/, 
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader'
        }
      }
    ]
  },
    
  // Setup plugin to use a HTML file for serving bundled js files
  plugins: [
    new HtmlWebpackPlugin({
      template: './src/index.html'
    })
  ]
}
```

Okay so let’s understand the lines above.

First we start by requiring the default path module to access the file location and make changes to the file location.

Next we require the HTMLWebpackPlugin to generate an HTML file to be used for serving bundled JavaScript file/files. Read more about [HTMLWebpackPlugin](https://github.com/jantimon/html-webpack-plugin) by clicking the link.

Then we have the export.module object with some properties in them. The first one is the **entry property,** which is used to specify which file webpack should start with to get the internal dependency graph created.

```js
module.exports = {
  entry:'./src/index.js'
}
```

Next up is the output property specifying where the bundled file should be generated and what the name of the bundled file would be. This is done by the **output.path** and **output.filename** properties.

```js
module.exports = {
  //This property defines the file path and the file name which will be used for deploying the bundled file
  output:{
    path: path.join(__dirname, '/dist'),
    filename: 'bundle.js'
  },
}
```

Next up are the loaders. This is to specify what webpack should do for a specific type for file. Remember that webpack out of box only understands JavaScript and JSON, but if your project has any other language used, this would be the place to specify what to do with that new language.

```js
module.exports = {
  //Setup loaders
  module: {
    rules: [
      {
        test: /\.js$/, 
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader'
        }
      }
    ]
  }
}
```

The information should be specified in an object for each module property, which further has an array of rules. There will be an object for every case. I have also specified to exclude everything in my node_modules folder.

Next up is the plugin property. This is used to extend the capabilities of webpack. Before a plugin can be used in the plugin array inside the module exports object, we need to require the same.

```js
module.exports = {
  // Setup plugin to use a HTML file for serving bundled js files
  plugins: [
    new HtmlWebpackPlugin({
      template: './src/index.html'
    })
  ]
}
```

This particular plugin, as explained earlier, will use the specified file in our src folder. It’ll then use that as a template for our HTML file where all the bundled files will be automatically injected. There are a lot of other out of the box plugins that we could use — checkout the [official page](https://webpack.js.org/plugins/) for more information.

The last thing we need to do is create a .babelrc file to use the babel preset we installed and take care of the ES6 classes and import statements in our code. Add the following lines of code to the .babelrc file.

```
{
  "presets": ["env", "react"]
}
```

And just like that, now babel will be able to use those presets. Okay so enough of the setup — let’s add some React code to see how this works.

### React Code

Since the starting point for the application is the index.js file in src folder, let’s start with that. We will start by requiring both **React** and **ReactDOM** for our use in this case. Add the below code in your index.js file.

```jsx
import React from 'react';
import ReactDOM from 'react-dom';
import App from './Components/App';

ReactDOM.render(<App />, document.getElementById('app'));
```

So we simply import another file from our components folder, which you will create, and add another file in the folder called App.js. So let’s see what’s inside the App.js file:

```jsx
import React, { Component } from 'react'

class App extends Component {
  render() {
    return (
      <div>
        <h1>Webpack + React setup</h1>
      </div>
    )
  }
}

export default App;
```

We are almost done. The only thing left now is to enable hot reloading. This means that every time a change is detected, the browser auto reloads the page and has the ability to build and bundle the entire application when the time comes.

We can do this by adding script values in the package.json file. Remove the test property in the scripts object of your package.json file and add these two scripts:

```json
"start": "webpack-dev-server --mode development --open --hot",
"build": "webpack --mode production"
```

You are all set! Go to your terminal, navigate to the root folder, and run **npm start.** It should start a dev server on your computer and serve the HTML file in your browser. If you make any minor/major changes and save the code, your browser will be automatically refreshed to show the latest set of changes.

Once you think you are ready to get the app bundled, you just need to hit the command, **npm build,** and webpack will create an optimised bundle in your project folder which can be deployed on any web server.

### Conclusion

This is just a small application or use case of webpack and babel, but the applications are limitless. I hope you are excited enough to explore more options and ways of doing things with webpack and babel. Please refer to their official websites to know more and read in depth.

I have created a Github repo with all the code in it, so please refer to it incase of any questions.

[**ashishcodes4/webpack-react-setup**](https://github.com/ashishcodes4/webpack-react-setup)  
[_Setting a react application from scratch without using CLI - ashishcodes4/webpack-react-setup_github.com](https://github.com/ashishcodes4/webpack-react-setup)

My two cents about webpack? Well, at times you may think that it’s nothing more than a tool, and why should you bother too much for a tool? But trust me when I say this: the initial struggle while learning your way around webpack will save you an enormous number of hours you would otherwise invest developing without webpack.

That’s all for now, hope to be back with yet another interesting article very soon. I hope you have enjoyed reading this one!

In case you face any difficulty or issues while following any of the above mentioned steps/processes, please feel free to get in touch and leave comments.

LinkedIn: [https://www.linkedin.com/in/ashish-nandan-singh-490987130/](https://www.linkedin.com/in/ashish-nandan-singh-490987130/)

Twitter: [https://twitter.com/ashishnandansin](https://twitter.com/ashishnandansin)

