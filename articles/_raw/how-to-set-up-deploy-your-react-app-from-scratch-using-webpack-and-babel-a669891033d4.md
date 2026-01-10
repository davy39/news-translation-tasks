---
title: How to set up & deploy your React app from scratch using Webpack and Babel
subtitle: ''
author: Nathan Sebhastian
co_authors: []
series: null
date: '2019-02-14T21:41:52.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-deploy-your-react-app-from-scratch-using-webpack-and-babel-a669891033d4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*NluDivebM4nQi0OLMYuVHw.png
tags:
- name: Apps
  slug: apps-tag
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: So you’ve been using create-react-app a.k.a CRA for a while now. It’s great
  and you can get straight to coding. But when do you need to eject from create-react-app
  and start configuring your own React application? There will be a time when we have
  to...
---

So you’ve been using create-react-app a.k.a CRA for a while now. It’s great and you can get straight to coding. But when do you need to eject from create-react-app and start configuring your own React application? There will be a time when we have to let go of the safety check and start venturing out on our own.

This guide will cover the most simple React configuration that I’ve personally used for almost all of my React projects. By the end of this tutorial we will have our own personal boilerplate and learn some configurations from it.

#### Table of Contents

* Why create your own configuration?
* Configuring webpack 4
* Configuring Babel 7
* Adding Prettier
* Adding source map for better error logs
* Setting up ESLint
* I found errors! What do I do?
* Adding CSS LESS processor
* Deploying React app to Netlify
* Conclusion

### Why create your own configuration?

There are certain reasons that make creating your own React configuration make sense. You are likely good with React and you want to learn how to use tools like webpack and Babel on your own. These build tools are powerful, and if you have some extra time, it’s always good to learn about them.

Developers are naturally curious people, so if you feel you’d like to know how things work and which part does what, then let me help you with it.

Furthermore, hiding React configuration by create-react-app is meant for developers starting to learn React, as [configuration should not stand in the way of getting started](https://youtu.be/G39lKaONAlA?t=873). But when things get serious, of course you need more tools to integrate in your project. Think about:

* Adding webpack loaders for less, sass
* Doing server side rendering
* Using new ES versions
* Adding MobX and Redux
* Making your own configuration just for learning sake

If you look around the Internet, there are some hacks to get around CRA limitations like [create-react-app rewired](https://github.com/timarney/react-app-rewired). But really, why not just learn React configuration on your own? I will help you get there. Step by step.

Now that you’re convinced to learn some configuration, let’s start by initializing a React project from scratch.

Open up the command line or Git bash and create a new directory

```
mkdir react-config-tutorial && cd react-config-tutorial
```

Initialize NPM project by running:

```
npm init -y
```

Now install react

```
npm install react react-dom
```

Also, you can view the [source code](https://github.com/nsebhastian/my-react-boilerplate) on GitHub while reading this tutorial for explanations about the settings.

### Configuring webpack 4

Our first stop will be the webpack. It’s a very popular and powerful tool for configuring not only React, but almost all front-end projects. The core function of webpack is that it takes a bunch of JavaScript files we write in our project and turns them into a single, minified file, so that it will be quick to serve. Starting from webpack 4, we aren’t required to write a configuration file at all to use it, but in this tutorial we will write one so that we can understand it better.

First, let’s do some installation

```
npm install --save-dev webpack webpack-dev-server webpack-cli
```

This will install:

* **webpack module** — which include all core webpack functionality
* **webpack-dev-server** — this development server automatically rerun webpack when our file is changed
* **webpack-cli** — enable running webpack from the command line

Let’s try to run webpack by adding the following script to `package.json`

```js
"scripts": {
 "start": "webpack-dev-server --mode development",
},
```

Now create an `index.html` file in your root project with the following content:

```html
<!DOCTYPE html>
<html>
 <head>
 <title>My React Configuration Setup</title>
 </head>
 <body>
 <div id="root"></div>
 <script src="./dist/bundle.js"></script>
 </body>
</html>
```

Create a new directory named `src` and inside it, create a new `index.js` file

```
mkdir src && cd src && touch index.js
```

Then write a React component into the file:

```js
import React from "react";
import ReactDOM from "react-dom";
class Welcome extends React.Component {
  render() {
    return <h1>Hello World from React boilerplate</h1>;
  }
}
ReactDOM.render(<Welcome />, document.getElementById("root"));
```

Run the webpack by using `npm run start` … And an error will be triggered.

```
You may need an appropriate loader to handle this file type
```

### Configuring Babel 7

The React component we wrote above used the `class` syntax, which is a feature of ES6. Webpack needs Babel to process ES6 into ES5 syntaxes in order for this class to work.

Let’s install Babel into our project

```
npm install --save-dev @babel/core @babel/preset-env \@babel/preset-react babel-loader
```

Why do we need these packages?

* **@babel/core** is the main dependency that includes babel transform script.
* **@babel/preset-env** is the default Babel preset used to transform ES6+ into valid ES5 code. Optionally configures browser polyfills automatically.
* **@babel/preset-react** is used for transforming JSX and React class syntax into valid JavaScript code.
* **babel-loader** is a webpack loader that hooks Babel into webpack. We will run Babel from webpack with this package.

To hook Babel into our webpack, we need to create a webpack configuration file. Let’s write a `webpack.config.js` file:

```js
module.exports = {
  entry: './src/index.js',
  output: {
    path: __dirname + '/dist',
    publicPath: '/',
    filename: 'bundle.js'
  },
  devServer: {
    contentBase: './dist',
  },
  module: {
    rules: [
    {
      test: /\.(js|jsx)$/,
      exclude: /node_modules/,
      use: ['babel-loader']
    }
    ]
  },
};
```

This webpack config is basically saying that the `entry` point of our application is from index.js, so pull everything that’s needed by that file, then put the `output` of the bundling process into the _dist_ directory, named _bundle.js_. Oh, if we’re running on `webpack-dev-server`, then tell the server to serve content from `contentBase` config, which is the same directory this config is in. For all .js or .jsx files, use `babel-loader` to transpile all of them.

In order to use Babel presets, create a new `.babelrc` file

```
touch .babelrc
```

Write the following content:

```js
{
  "presets": [
    "@babel/preset-env",
    "@babel/preset-react"
  ]
}
```

Now run `npm run start` again. This time it will work.

### Adding Prettier

To further speed up development, let’s make our code formatter using Prettier. Install the dependency locally and use the — save-exact argument since Prettier introduces stylistic changes in patch releases.

```
npm install --save-dev --save-exact prettier
```

Now we need to write the `.prettierrc` configuration file:

```js
{
 "semi": true,
 "singleQuote": true,
 "trailingComma": "es5"
}
```

The rules means that we want to add semicolon for the end of every statement, use a single quote whenever appropriate and put trailing commas for multi-line ES5 code like objects or arrays.

You can run Prettier from the command line with:

```
npx prettier --write "src/**/*.js"
```

Or add a new script to our `package.json` file:

```js
"scripts": {
 "test": "echo \"Error: no test specified\" && exit 1",
 "start": "webpack-dev-server --mode development",
 "format": "prettier --write \"src/**/*.js\""
},
```

Now we can run Prettier using `npm run format`.

Additionally, if you’re using VSCode for development, you can install the [Prettier extension](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode) and run it every time you save your changes by adding this setting:

```
"editor.formatOnSave": true
```

### Adding source map for better error logs

Since webpack bundles the code, source maps are mandatory to get a reference to the original file that raised an error. For example, if you bundle three source files (`a.js`, `b.js`, and `c.js`) into one bundle (`bundler.js`) and one of the source files contains an error, the stack trace will simply point to `bundle.js`. This is problematic as you probably want to know exactly if it’s the a, b, or c file that is causing an error.

You can tell webpack to generate source maps using the devtool property of the configuration:

```js
module.exports = {
  devtool: 'inline-source-map',
  // … the rest of the config
};
```

Although it will cause a slower build, it has no effect on production. Sourcemaps are only downloaded [if you open the browser DevTools](https://stackoverflow.com/a/44316255).

### Setting up ESLint

Linter is a program that checks our code for any error or warning that can cause bugs. JavaScript’s linter, ESLint, is a very flexible linting program that can be configured in many ways.

But before we get ahead, let’s install ESLint into our project:

```
npm --save-dev install eslint eslint-loader babel-eslint eslint-config-react eslint-plugin-react
```

* **eslint** is the core dependency for all functionalities, while eslint-loader enables us to hook eslint into webpack. Now since React used ES6+ syntax, we will add **babel-eslint** — a parser that enables eslint to lint all valid ES6+ codes.
* **eslint-config-react** and **eslint-plugin-react** are both used to enable ESLint to use pre-made rules.

Since we already have webpack, we only have to modify the config slightly:

```js
module.exports = {
  // modify the module
  module: {
    rules: [{
      test: /\.(js|jsx)$/,
      exclude: /node_modules/,
      use: ['babel-loader', 'eslint-loader'] // include eslint-loader
    }]
  },
};
```

Then create an eslint config file named `.eslintrc` with this content:

```
{
  "parser": "babel-eslint",
  "extends": "react",
  "env": {
    "browser": true,
    "node": true
  },
  "settings": {
    "react": {
      "version": "detect"
    }
  }
}
```

The config is basically saying, _“Hey ESLint, please parse the code using `babel-eslint` before you check it, and when you’re checking it, please check if all the rules from our React rules config is passed. Take global variables from the environment of browser and node. Oh, and if it’s React code, take the version from the module itself. That way the user won’t have to specify the version manually._”

Rather than specifying our own rules manually, we simply extend `react` rules which were made available by `eslint-config-react` and `eslint-plugin-react`.

### I found errors! What do I do?

Unfortunately the only way to really figure out how to fix ESLint errors is by looking at the documentation for [rules](https://eslint.org/docs/rules/). There’s a quick way to fix ESLint errors by using `eslint--fix`, and it’s actually good for a quick fix. Let’s add a script on our `package.json` file:

```js
"scripts": {
  "test": "echo \"Error: no test specified\" && exit 1",
  "start": "webpack-dev-server --mode development",
  "format": "prettier --write \"src/**/*.js\"",
  "eslint-fix": “eslint --fix \"src/**/*.js\"", // the eslint script
  "build": "webpack --mode production"
},
```

Then run it with `npm run eslint-fix`. Don’t worry if you’re still fuzzy about ESLint for now. You will learn more about ESLint as you use it.

### Adding CSS LESS processor

In order to add the LESS processor into our React application, we will require both less and loader packages from webpack:

```
npm install --save-dev less less-loader css-loader style-loader
```

`less-loader` will compile our less file into css, while `css-loader` will resolve css syntax like `import` or `url()`. The `style-loader` will get our compiled css and load it up into `<sty`le> tag in our bundle. This is great for development because it lets us update our style on the fly, without needing to refresh the browser.

Now let’s add some css files to create a new style directory in `src/style`

```
cd src && mkdir style && touch header.less && touch main.less
```

`header.less` content:

```js
.header {
  background-color: #3d3d;
}
```

`main.less` content:

```css
@import "header.less";
@color: #f5adad;
body {
  background-color: @color;
}
```

Now import our `main.less` file from `index.js`:

```
import "./style/main.less";
```

Then update our webpack configuration `module` property:

```js
module: {
  rules: [{
    test: /\.(js|jsx)$/,
    exclude: /node_modules/,
    use: ['babel-loader', 'eslint-loader']
  },
  {
    test: /\.less$/,
    use: [
      'style-loader',
      'css-loader',
      'less-loader',
    ],
  },
 ]
},
```

Run the start script and we’re good to go!

### Deploying React app to Netlify

All applications need to be deployed for the last step, and for React applications, deployment is very easy.

First, let’s change the build output and development `contentBase` from `dist` to `build` in our Webpack config.

```js
module.exports = {
  entry: './src/index.js',
  output: {
    path: path.resolve(__dirname, 'build'), // change this
    publicPath: '/',
    filename: 'bundle.js'
  },
  devServer: {
    contentBase: "./build",
  },
//…
```

Now let’s install a new Webpack plugin named HtmlWebpackPlugin

```
npm install html-webpack-plugin -D
```

This plugin will generate `index.html` file in the same directory where our `bundle.js` is created by Webpack. In this case, the `build` directory.

Why do we need this plugin? Because Netlify requires a single directory to be made the root directory, so we can’t use `index.html` in our root directory using Netlify. You need to update your webpack config to look like this:

```js
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
module.exports = {
  entry: //…
  output: {
    //…
  },
  devServer: {
    contentBase: "./build",
  },
  module: {
    //…
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: path.resolve('./index.html'),
    }),
  ]
};
```

And please remove the `script` tag from your `index.html`:

```html
<!DOCTYPE html><html>  <head>    <title>My React Configuration Setup</title>  </head>  <body>    <div id="root"></div>  </body></html><!DOCTYPE html>
<html>
  <head>
    <title>My React Configuration Setup</title>
  </head>
  <body>
    <div id="root"></div>
  </body>
</html>
```

Now you can test the config with `npm run build` command. Once it’s done, push your boilerplate into a GitHub repo. It’s time to deploy our application!

Now let’s register a [Netlify](https://netlify.com) account. If you haven’t heard of Netlify before, it’s an amazing static site hosting that provides all the tools you need to deploy a static site for free. What’s a static site? It’s a website created from a collection of static HTML pages, without any backend. Our React boilerplate as it is now counts as a static site, because we have no backend configured and its just HTML and JavaScript.

After sign up, select new site from Git and Choose GitHub as your Git provider:

![Image](https://cdn-media-1.freecodecamp.org/images/WfWqORsZjfHKwOpZ63d-nZUC6N2FF9CPzDrg)

You need to grant permissions for Netlify, and then select your React boilerplate repo.

![Image](https://cdn-media-1.freecodecamp.org/images/MtKFlYYRZVZ7JNcmP8AHiiDV5OLlJoy4hBk5)

Now you need to enter the build command and publishing directory. As you can see, this is why we need _HtmlWebpackPlugin_, because we need to serve everything from one directory only. Rather than manually updating our root `index.html` file for changes, we just generate it using the plugin.

![Image](https://cdn-media-1.freecodecamp.org/images/aecd4gyxtTE22EuPoHzXRe1yA9I9BqTaPfa1)

Make sure you have the same command as the screenshot above, or your app might not run.

![Image](https://cdn-media-1.freecodecamp.org/images/T3GN2LRCZtTIfNNOSVPV-tKgrmlllnRVcmcs)

Once the deploys status turns to `published` (number 2 above), you can go to the random site name Netlify has assigned for your application (number 1).

Your React application is deployed. Awesome!

### Conclusion

You’ve just created your very own React project boilerplate and deploy it live to Netlify. Congratulations! Granted, I didn’t go very deep on webpack configurations, because this boilerplate is meant to be a generic starter. In some cases where we need advanced features like server side rendering, we need to tweak the configuration again.

But relax! You’ve come this far, which means you already understand what webpack, Babel, Prettier and ESLint do. Webpack has many powerful loaders that can help you with many cases you’ll frequently counter when building a web application.

If you enjoyed this article and want to take your JavaScript skills to the next level, I recommend you check out my new book _Beginning Modern JavaScript_ [here](https://www.amazon.com/dp/B0CQXHMF8G).

[![beginning-js-cover](https://www.freecodecamp.org/news/content/images/2024/01/beginning-js-cover.png)](https://www.amazon.com/dp/B0CQXHMF8G)

The book is designed to be easy to understand and accessible to anyone looking to learn JavaScript. It provides a step-by-step gentle guide that will help you understand how to use JavaScript to create a dynamic application.

Here's my promise: _You will actually feel like you understand what you're doing with JavaScript._

Until next time!

