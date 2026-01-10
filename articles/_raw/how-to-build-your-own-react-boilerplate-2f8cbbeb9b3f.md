---
title: How to build your own React boilerplate
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-24T16:13:13.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-your-own-react-boilerplate-2f8cbbeb9b3f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*g3L9F6AO-jUW-QuQRFI3JA.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Nick Karnik

  What is a Boilerplate?

  In programming, the term boilerplate code refers to blocks of code used over and
  over again.

  Let’s assume your development stack consists of several libraries, such as React,
  Babel, Express, Jest, Webpack, etc. W...'
---

By Nick Karnik

### What is a Boilerplate?

In programming, the term boilerplate code refers to blocks of code used over and over again.

Let’s assume your development stack consists of several libraries, such as React, Babel, Express, Jest, Webpack, etc. When you start a new project, you initialize all these libraries and configure them to work with each other.

With every new project that you start, you will be repeating yourself. You could also introduce inconsistencies in how these libraries are set up in each project. This can cause confusion when you switch between projects.

This is where boilerplates come in. A boilerplate is a template that you can clone and reuse for every project.

The modular Javascript ecosystem simplifies application development through various libraries, frameworks and tools. Boilerplates can be daunting if you don’t understand the fundamentals of their underlying components. Let’s learn about these basic building blocks while creating our own.

> [_Click here for source on GitHub_](https://github.com/theoutlander/react-boilerplate)

> I am using Webstorm, Git, NodeJS 8.9, NPM 5.6, and React 16. Fire up your favorite IDE, create a blank project, and let’s get started!

### Git Repository: Setup

Create a project folder and initialize a Git repo:

```
mkdir react-boilerplate && cd react-boilerplategit init
```

> You can connect this project to your own repo on GitHub using [these instructions](https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/).

### Readme File

Every project should contain a landing page with useful instructions for other developers. Let’s create a README.md file under the project root with the following content:

```
# React-BoilerplateThis is my react-boilerplate
```

```
## Setupnpm installnpm run buildnpm start
```

GitHub displays the contents of the readme file on the landing page for the project.

Now, commit the above changes to Git:

```
git add .git commit -m "created readme"
```

At the end of each section, you should commit your code to Git.

### Folder Structure

Create the following folder structure for your project:

```
react-boilerplate    |--src       |--client       |--server
```

with the command:

```
mkdir -p src/client src/server
```

This folder structure is basic and will evolve as you integrate other libraries in the project.

### Git Ignore

Once we build our project, there will be a few auto-generated files and folders. Let’s tell Git to ignore some of those files that we can think of ahead of time.

Create .gitignore under the root folder with the following content:

```
# Nodenode_modules/
```

```
# Webstorm.idea/
```

```
# Projectdist/
```

Comments in a .gitignore file are prefixed with #.

### Node Package Manager

The starting point for a node project is to initialize its package manager which creates a file called package.json. This file must be checked into Git.

It generally contains:

* A description of your project for NPM
* List of references to all installed packages
* Custom command line scripts
* Configuration for installed packages

Go to your project root and type the following:

```
npm init
```

Fill out all the details, and after you accept them, npm will create a package.json file that looks something like:

```
{  "name": "react-boilerplate",  "version": "1.0.0",  "description": "Basic React Boilerplate",  "main": "index.js",  "scripts": {    "test": "echo \"Error: no test specified\" && exit 1"  },  "repository": {    "type": "git",    "url": "git+https://github.com/theoutlander/react-boilerplate.git"  },  "keywords": [    "Node",    "React"  ],  "author": "Nick Karnik",  "license": "Apache-2.0",  "bugs": {    "url": "https://github.com/theoutlander/react-boilerplate/issues"  },  "homepage": "https://github.com/theoutlander/react-boilerplate#readme"}
```

### Static Content

Let’s create a static HTML file src/client/index.html with the following content:

```
<!DOCTYPE html><html lang="en"><head>    <meta charset="UTF-8">    <title>React Boilerplate</title></head><body>    <div id="root">        Welcome to React Boilerplate!    </div></body></html>
```

### Express Web Server

To serve the static file above, we need to create a web server in [ExpressJS](http://expressjs.com/).

> NPM v5 automatically saves installed packages under the dependencies section in package.json so the --save _attribute_ is not necessary

```
npm install express
```

I would recommend following a file naming convention where file names are lower case and multiple words are separated by a dot. You will avoid running into case sensitivity issues across platforms, and will also simplify naming files with multiple words across larger teams.

Create a file src/server/web.server.js and add the following code to host a web server via an express app and serve the static HTML file:

```
const express = require('express')
```

```
export default class WebServer {  constructor () {    this.app = express()    this.app.use(express.static('dist/public'))  }
```

```
  start () {    return new Promise((resolve, reject) => {      try {        this.server = this.app.listen(3000, function () {          resolve()        })      } catch (e) {        console.error(e)        reject(e)      }    })  }
```

```
  stop () {    return new Promise((resolve, reject) => {      try {        this.server.close(() => {          resolve()        })      } catch (e) {        console.error(e.message)        reject(e)      }    })  }}
```

We have created a simple web server above with a start and stop command.

[Click here to learn more about Promises](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise).

### Startup File

Next, we need to create an index file which will initialize various high-level components. In our example, we’re going to initialize the web server. However, as your project grows, you can also initialize other components such as configuration, database, logger, etc.

Create a file src/server/index.js with the following code:

```
import WebServer from './web.server'
```

```
let webServer = new WebServer();webServer.start()  .then(() => {    console.log('Web server started!')  })  .catch(err => {    console.error(err)    console.error('Failed to start web server')  });
```

### Babel

To run the above [ES6](http://es6-features.org/) code, we need to transform it to [ES5](https://es5.github.io/) first via Babel. Let’s install [Babel](http://babeljs.io/) and the [babel-preset-env](https://github.com/babel/babel/tree/master/experimental/babel-preset-env) dependency which supports ES2015 transpilation:

```
npm i babel-cli babel-preset-env --save-dev
```

Create a Babel configuration file called .babelrc under the root and add the following details to it:

```
{  "presets": ["env"]}
```

The env preset implicitly includes babel-preset-es2015, babel-preset-es2016, and babel-preset-es2017 together, which means you can run ES6, ES7 and ES8 code.

### Build Commands

Let’s create commands to build the server and client components of the project and start the server. Under the scripts section of package.json, remove the line with the test command and add the following:

```
"scripts": {    "build": "npm run build-server && npm run build-client",    "build-server": "babel src/server --out-dir ./dist",    "build-client": "babel src/client --copy-files --out-dir ./dist/public",    "start": "node ./dist/index.js"}
```

The build command above will create a dist/public folder under the root. The build-client command is simply copying the index.html file to the dist/public folder.

### Starting up

You can run the Babel transpiler on the code above and start the web server by using the following commands:

```
npm run buildnpm start
```

Open your browser and navigate to [http://localhost:3000](http://localhost:3000/). You should see the output of your static HTML file.

![Image](https://cdn-media-1.freecodecamp.org/images/0*u2ynUivrvLjs-av0.png)

You can stop the web server by pressing <Ctrl> C

### Test Harness: Jest

I cannot stress enough the importance of introducing unit tests at the beginning of a project. We’re going to use the [Jest Testing Framework](https://facebook.github.io/jest/) which is designed to be fast and developer friendly.

First, we need to install Jest and save it to development dependencies.

```
npm i jest --save-dev
```

### Unit Tests

Let’s add two test cases to start and stop the web server.

For test files, you should add a .test.js extension. Jest will scan the src folder for all files containing .test in the filename, you can keep your test cases under the same folder as the files they’re testing.

Create a file called src/server/web.server.test.js and add the following code:

```
import WebServer from './web.server'
```

```
describe('Started', () => {  let webServer = null
```

```
  beforeAll(() => {    webServer = new WebServer()  })
```

```
  test('should start and trigger a callback', async () => {    let promise = webServer.start()    await expect(promise).resolves.toBeUndefined()  })
```

```
  test('should stop and trigger a callback', async () => {    let promise = webServer.stop()    await expect(promise).resolves.toBeUndefined()  })})
```

### Test Command

Let’s add an npm command to run the test under the scripts section of package.json. By default, Jest runs all files with the word .test in their file name. We want to limit it to running tests under the src folder.

```
"scripts": {...    "test": "jest ./src"...}
```

Babel-jest is automatically installed when installing Jest and will automatically transform files if a Babel configuration exists in your project.

Let’s run our tests via the following command:

```
npm test
```

![Image](https://cdn-media-1.freecodecamp.org/images/0*4OQroTGQMuSlEg3j.png)

Our application is set up to serve a static _HTML_ file via an _Express_ web server. We have integrated _Babel_ to enable ES6 and _Jest_ for unit testing. Let’s shift our focus to the front-end setup.

### React Setup

Install the react and react-dom libraries:

```
npm i react react-dom
```

Create a file called src/client/app.js with:

```
import React, {Component} from 'react'
```

```
export default class App extends Component {    render() {        return <div>Welcome to React Boilerplate App</div>    }}
```

Let’s render the App via an index file under src/client/index.js with:

```
import React from 'react'import ReactDOM from 'react-dom'import App from './app'
```

```
ReactDOM.render(<App />, document.getElementById('root'))
```

### Babel React

If you execute npm run build-client, you will get an error because we haven’t told Babel how to handle React / JSX.

![Image](https://cdn-media-1.freecodecamp.org/images/0*W-9sbHjloV7lyDfq.png)

Let’s fix that by installing the [babel-preset-react](http://babeljs.io/docs/plugins/preset-react/) dependency:

```
npm install --save-dev babel-preset-react
```

We also need to modify the .babelrc config file to enable transpiling react:

```
{  "presets": ["env", "react"]}
```

Now, when you run npm run build-client, it will create app.js and index.js under dist/public with ES6 code transpiled to ES5.

### Load Script in HTML

To connect our React App to the HTML file, we need to load index.js in our index.html file. Don’t forget to empty the text of the #root node since the React App will be mounted to it:

```
<!DOCTYPE html><html lang="en"><head>    <meta charset="UTF-8">    <title>React Boilerplate</title></head><body>    <div id="root"></div>    <script src="index.js"></script></body></html>
```

### Run Server

If you fire up your web server and go to [http://localhost:3000](http://localhost:3000/), you will see a blank page with an error in the console.

Uncaught ReferenceError: require is not defined.

![Image](https://cdn-media-1.freecodecamp.org/images/0*C0et_W8a6-CIWpJK.png)

This is because Babel is just a transpiler. In order to support dynamically loading modules, we will need to install Webpack.

Start by changing the build commands under scripts in package.json to build-babel:

```
"scripts": {    "build-babel": "npm run build-babel-server && npm run build-babel-client",    "build-babel-server": "babel src/server --out-dir ./dist",    "build-babel-client": "babel src/client --copy-files --out-dir ./dist/public",    "start": "node ./dist/index.js",    "test": "jest ./src"  }
```

### Webpack

Webpack allows us to easily modularize our code and bundle it into a single Javascript file. It is supported by numerous plugins, and chances are that there’s a plugin for almost any build task you can think of. Start by installing Webpack:

> This tutorial was published right before webpack v4 was released, so we will explicitly install webpack v3.

```
npm i webpack@^3
```

By default, Webpack looks for a configuration file called webpack.config.js, so let’s create it in the root folder and define two entry points, one for the web application and the other for the web server. Let’s create two config objects and export them as a collection:

```
const client = {    entry: {        'client': './src/client/index.js'    }};
```

```
const server = {    entry: {        'server': './src/server/index.js'    }};
```

```
module.exports = [client, server];
```

Now, let’s specify where Webpack will output the bundle and set the [target](https://webpack.js.org/concepts/targets/) build so that it ignores native node modules like ‘fs’ and ‘path’ from being bundled. For client, we will set it to web, and for server we will set it to node.

```
let path = require('path');
```

```
const client = {    entry: {        'client': './src/client/index.js'    },    target: 'web',    output: {        filename: '[name].js',        path: path.resolve(__dirname, 'dist/public')    }};
```

```
const server = {    entry: {        'server': './src/server/index.js'    },    target: 'node',    output: {        filename: '[name].js',        path: path.resolve(__dirname, 'dist')    }};
```

```
module.exports = [client, server];
```

### Babel Loader

Before we can run Webpack, we need configure it to handle ES6 and JSX code. This is done via loaders. Let’s start by installing [babel-loader](https://github.com/babel/babel-loader):

```
npm install babel-loader --save-dev
```

We need to modify the Webpack configuration to include babel-loader to run on all .js files. We will create a shared object defining the module section that we can re-use for both targets.

```
const path = require('path');
```

```
const moduleObj = {    loaders: [        {            test: /\.js$/,            exclude: /node_modules/,            loaders: ["babel-loader"],        }    ],};
```

```
const client = {    entry: {        'client': './src/client/index.js',    },    target: 'web',    output: {        filename: '[name].js',        path: path.resolve(__dirname, 'dist/public')    },    module: moduleObj};
```

```
const server = {    entry: {        'server': './src/server/index.js'    },    target: 'node',    output: {        filename: '[name].js',        path: path.resolve(__dirname, 'dist')    },    module: moduleObj}
```

```
module.exports = [client, server];
```

For merging nested shared objects, I would recommend checking out the [Webpack Merge](https://github.com/survivejs/webpack-merge) module.

### Excluding Files

Webpack will bundle referenced libraries, which means everything that is included from node_modules will be packaged. We don’t need to bundle external code, as those packages are generally minified, and they will also increase the build time and size.

Let’s configure Webpack to exclude all packages under the node_modules folder. This is easily accomplished via the [webpack-node-externals](https://www.npmjs.com/package/webpack-node-externals) module:

```
npm i webpack-node-externals --save-dev
```

Followed by configuring webpack.config.js to use it:

```
let path = require('path');let nodeExternals = require('webpack-node-externals');
```

```
const moduleObj = {    loaders: [        {            test: /\.js$/,            exclude: /node_modules/,            loaders: ["babel-loader"],        }    ],};
```

```
const client = {    entry: {        'client': './src/client/index.js',    },    target: 'web',    output: {        filename: '[name].js',        path: path.resolve(__dirname, 'dist')    },    module: moduleObj};
```

```
const server = {    entry: {        'server': './src/server/index.js'    },    target: 'node',    output: {        filename: '[name].js',        path: path.resolve(__dirname, 'dist')    },    module: moduleObj,    externals: [nodeExternals()]}
```

```
module.exports = [client, server];
```

### Update Build Command

Finally, we need to make changes to the scripts section under package.json to include a build command that uses Webpack, and to rename index.js to server.js for npm start as that’s what Webpack is configured to output.

```
"scripts": {    "build": "webpack",    "build-babel": "npm run build-babel-server && npm run build-babel-client",    "build-babel-server": "babel src/server --out-dir ./dist",    "build-babel-client": "babel src/client --copy-files --out-dir ./dist/public",    "start": "node ./dist/server.js",    "test": "jest ./src"  }
```

### Build Clean

Let’s add a command to clean our dist and node_modules folders so we can do a clean build and ensure our project still works as expected. Before we can do that, we need to install a package called [rimraf](https://github.com/isaacs/rimraf) (which is the rm -rfcommand).

```
npm install rimraf
```

The scripts section should now contain:

```
"scripts": {..."clean": "rimraf dist node_modules",...}
```

### Clean Build with Webpack

You can now successfully clean and build your project using Webpack:

```
npm run cleannpm installnpm run build
```

This will create dist/server.js and dist/public/client.js under the root folder.

### HTML Webpack Plugin

However, you may have noticed that index.html is missing. This is because, previously, we asked Babel to copy files that weren’t transpiled. However, Webpack isn’t able to do that, so we need to use the [HTML Webpack Plugin](https://github.com/jantimon/html-webpack-plugin).

Let’s install the HTML Webpack Plugin:

```
npm i html-webpack-plugin --save-dev
```

We need to include the plugin at the top of the webpack config file:

```
const HtmlWebPackPlugin = require('html-webpack-plugin')
```

Next, we need to add a plugins key to the client config:

```
const client = {  entry: {    'client': './src/client/index.js'  },  target: 'web',  output: {    filename: '[name].js',    path: path.resolve(__dirname, 'dist/public')  },  module: moduleObj,  plugins: [    new HtmlWebPackPlugin({      template: 'src/client/index.html'    })  ]}
```

Before we build the project, let’s modify our HTML file and remove the reference to the index.js script, because the above plugin will add that for us. This is especially useful when there are one or more files with dynamic filenames (for instance when files are generated with a unique timestamp for cache busting).

```
<!DOCTYPE html><html lang="en"><head>    <meta charset="UTF-8">    <title>React Boilerplate</title></head><body>    <div id="root"></div></body></html>
```

Lets’s rebuild the project:

```
npm run cleannpm installnpm run build
```

And, verify that our existing tests are still running:

```
npm test
```

We have further updated the boilerplate to integrate React and Webpack, created additional NPM commands, dynamically referenced index.js in the HTML file, and exported it.

### Enzyme Setup

Before we add a React test, we need to integrate [Enzyme](https://github.com/airbnb/enzyme), which will allow us to assert, manipulate and traverse react components.

Let’s start by installing Enzyme and enzyme-adapter-react-16, which is required to connect Enzyme to a project using react v16 and above.

> _enzyme-adapter-react-16 has peer dependencies on react, react-dom, and react-test-renderer_

```
npm i --save-dev enzyme enzyme-adapter-react-16 react-test-renderer
```

Create a file src/enzyme.setup.js with the following content:

```
import Enzyme from 'enzyme'import Adapter from 'enzyme-adapter-react-16'
```

```
Enzyme.configure({    adapter: new Adapter()})
```

We need to configure Jest to use src/enzyme.setup.js in package.json by adding the following section under the root object:

```
{..."jest": {    "setupTestFrameworkScriptFile": "./src/enzyme.setup.js"  }...}
```

### React Component Test

Let’s test the App Component and ensure that it renders the expected text. In addition, we will take a snapshot of that component so we can ensure that its structure hasn’t changed with every test run.

[Click here to learn more about snapshot testing](https://facebook.github.io/jest/docs/en/snapshot-testing.html).

Create a test case under src/client/app.test.js with the following content:

```
import App from './app'import React from 'react'import {shallow} from 'enzyme'
```

```
describe('App', () => {  test('should match snapshot', () => {    const wrapper = shallow(&lt;App/>)
```

```
    expect(wrapper.find('div').text()).toBe('Welcome to React Boilerplate App')    expect(wrapper).toMatchSnapshot()  })})
```

If we run this test now, it will pass with a warning:

![Image](https://cdn-media-1.freecodecamp.org/images/1*y44uqej9jGRMqLOm0lmRWw.png)

Let’s fix that by installing a polyfill called [raf](https://github.com/chrisdickinson/raf):

```
npm i --saveDev raf
```

And changing the Jest configuration under package.json to:

```
{..."jest": {    "setupTestFrameworkScriptFile": "./src/enzyme.setup.js",    "setupFiles": ["raf/polyfill"]  }...}
```

Now, you can verify that all our tests are passing:

```
npm test
```

![Image](https://cdn-media-1.freecodecamp.org/images/0*IK1jRFuIfXrdkmez.png)

After running the react test, you will notice a new file at src/client/snapshots/app.test.js.snap. It contains the serialized structure of our react component. It must be checked into Git so it can be used to compare against the dynamically generated snapshot during a test run.

### Final Run

Let’s start the web server one more time and navigate to [http://localhost:3000](http://localhost:3000/) to ensure everything works:

```
npm start 
```

![Image](https://cdn-media-1.freecodecamp.org/images/0*oNefrz8voxKjaDNY.png)

I hope this article has given you insights into streamlining the process of starting a new project from scratch with Express | React | Jest | Webpack | Babel. It is a good idea to create your own reusable boilerplate so you understand what goes on under the hood, and at the same time get a head-start when creating new projects.

We have barely scratched the surface and there is a lot of room for improvement to make this boilerplate production ready.

Here are some things for you to try:

* Enable [cache busting](https://webpack.js.org/guides/caching/) in Webpack
* CSS file bundling using [css-loader in webpack](https://github.com/webpack-contrib/css-loader)
* [Enable](https://github.com/webpack-contrib/css-loader) source maps in webpack
* Add [debug commands](https://nodejs.org/en/docs/guides/debugging-getting-started/) to package.json
* [Hot module replacement](https://webpack.js.org/concepts/hot-module-replacement/)
* Auto-restart web server when changes are detected via [nodemon](https://github.com/remy/nodemon)

If you would like to learn more about the react ecosystem, I would highly recommend taking [The Complete React Web Developer Course](https://www.udemy.com/react-2nd-edition/?couponCode=LEARNING) by [Andrew Mead](https://www.freecodecamp.org/news/how-to-build-your-own-react-boilerplate-2f8cbbeb9b3f/undefined).

#### If this article was helpful, ??? and Fol[low me on Twitter.](https://twitter.com/intent/follow?screen_name=theoutlander)

![Image](https://cdn-media-1.freecodecamp.org/images/1*X-sqS5Sd479XE60HoKAn0g.jpeg)
_[React Component Lifecycle](https://twitter.com/intent/follow?screen_name=theoutlander" rel="noopener" target="_blank" title="">You may also like my youtube tutorial on </a><a href="https://youtu.be/7iHepe36m0c" rel="noopener" target="_blank" title=")_

