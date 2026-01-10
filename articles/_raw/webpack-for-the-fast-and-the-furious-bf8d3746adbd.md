---
title: Webpack for The Fast and The Furious
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-02-11T12:27:31.000Z'
originalURL: https://freecodecamp.org/news/webpack-for-the-fast-and-the-furious-bf8d3746adbd
coverImage: https://cdn-media-1.freecodecamp.org/images/1*SpCunp0GLPDMsjM8hsX0qA.jpeg
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: Web Development
  slug: web-development
- name: webpack
  slug: webpack
seo_title: null
seo_desc: 'By Ashwin Hariharan


  Also published in my tech blog


  This is a guide that is meant to help you ease your development workflow and save
  your time by using a bunch of awesome tools that you’ve read about on the internet
  (does React Hot Loader ring any ...'
---

By Ashwin Hariharan

> Also published in my [tech blog](https://blog.booleanhunter.com/webpack-for-the-fast-and-the-furious/)

This is a guide that is meant to help you ease your development workflow and save your time by using a bunch of awesome tools that you’ve read about on the internet (does React Hot Loader ring any bells?)

It’s also meant to help you out with some of the most commonly encountered problems while using Webpack — and save some time in the process before you begin to pull your hair out. After all, you want to go fast and tear through other important problems.

Chances are that you’ve run into one or more of the following issues:

* How do I have multiple entries?
* How do I shim modules?
* One of the libraries/plugins that I use depends on jQuery, how do I handle that?
* I keep getting _$ is not defined_ or some stupid crap like that in one of the jQuery Plugins
* My bundling takes like, forever to finish.
* I read a bunch of tutorials on How Module Replacement for ReactJS and think it’s really cool, but keep running into errors while setting it up.

If you’re running into these difficulties, finish this article before you resort to posting one of these questions on Stack Overflow.

![Image](https://cdn-media-1.freecodecamp.org/images/1*lQQ5F_hkfxFwcaWPAThRRA.jpeg)

I’m assuming that you already know about the advantages of Webpack and what it is used for. If you’re a beginner and have no clue about what Webpack is, I highly recommend reading about it [here](https://medium.com/@housecor/browserify-vs-webpack-b3d7ca08a0a9#.r4eum99hk).

I’m also assuming that you’re building a web app and not just some static page, which means that you will have a web server running on Node and Express. You most likely also use a NodeJS driver to talk to your database — probably MongoDB or Redis.

So here is what a typical _webpack.config.js_ looks like:

```js
/**
 * @Author Ashwin Hariharan
 * @Details Webpack config file for adding new vendors, defining entry points and shimming modules. 
 */

var webpack = require('webpack');
var path = require("path");

var lib_dir = __dirname + '/public/libs',
    node_dir = __dirname + '/node_modules';
   // bower_dir = __dirname + '/bower_components'

var config = {
    resolve: {
        alias: {
            react: node_dir + '/react',
            reactDom: lib_dir + '/react-dom',
            jquery: lib_dir + '/jquery-1.11.2.min.js', 
            magnificPopup: lib_dir + '/jquery.magnific-popup.js' //JQuery Plugin
        }
    },   

    entry: {
        app: ['./public/src/js/app-main'],
        vendors: ['react','reactDom','jquery','magnificPopup']
    },

    output: {
        path: path.join(__dirname, "public"),
        filename: "dist/js/[name].bundle.js"
    },

    plugins: [
        new webpack.ProvidePlugin({
            jQuery: "jquery",
            'window.jQuery': "jquery"
        }),
        new webpack.optimize.CommonsChunkPlugin('vendors', 'dist/js/vendors.js', Infinity),
    ],
    
    module: {
        noParse: [
            new RegExp(lib_dir + '/react.js'),
            new RegExp(lib_dir +'/jquery-1.11.2.min.js')
        ],
        loaders: [
            { 
                test: /\.js$/, 
                loader: 'babel',
                query: {
                    presets: ['react', 'es2015']
                }
            }, 
        ]
    }
};

module.exports = config;
```

This config assumes that you have use some node modules and dist version of few libraries saved inside a _public/libs_ folder. Now if you’ve read other tutorials, you understand what the configs in this file do, however I’m still gonna briefly explain what few things in this file are for —

* **Aliases / vendors**  
Here is where you include all of your libraries/node modules/other vendors and map each of them to aliases. Then if you use a module in any part of your application logic, you can write this (in your _app-main.js_ or any other JS file):

```js
var React = require(‘react’);
var ReactDom = require('reactDom');
var $ = require('jquery');

//Your application logic
```

Or if you prefer AMD over CommonJS:

```js
define(
    [
        ‘react’,
        ’reactDom’,
        ’jquery’
    ],
    function(React, ReactDom, $) {
        //Your application logic
    }
);
```

Or in ES6 too:

```js
import React from 'react';
import ReactDom from 'reactDom';
import $ from 'jquery';
```

* **Defining your entry points**

```js
entry: {

}
```

This block in your config allows Webpack to determine where your app begins execution, and it creates chunks out of it. Having multiple entry points in your application is always advantageous. In particular, you can add all your vendor files — like jQuery and ReactJS — into one chunk. This way, your vendor files will remain the same, even when you modify your source files.

So in the above config, there are two entry points. One for your app’s entry where your JS begins, and one for your vendors — each of them mapped to a variable name.

* **Your output directory and bundle file names**

```js
output: {
     path: path.join(__dirname, “public”),
     filename: “dist/js/[name].bundle.js”
 },
```

This block tells Webpack what to name your files after the build process, and where to place them. In our example we have two entries named _app_ and _vendors_, so after the build process you’ll have two files called _app.bundle.js_ and _vendors.bundle.js_ inside _/public/dist/js_ directory.

* **Plugins**

Webpack comes with a rich ecosystem of plugins to help meet specific needs. I’ll briefly explain few of the most commonly used ones:

* Use the _CommonsChunkPlugin_ to have Webpack determine what code/modules you use the most, and put it in a separate bundle to be used anywhere in your application.
* You can optionally use the _ProvidePlugin_ to inject globals. There are many jQuery plugins that rely on a global jQuery variable like _$,_ so by using this plugin Webpack can prepend _var $ = require(“jquery”)_ every time it encounters the global _$_ identifier. Ditto for any other plugin out there, like Bootstrap.

By including _noParse,_ you can tell Webpack not to parse certain modules. This is useful when you only have the dist version of these modules/libraries. Improves build time.

![Image](https://cdn-media-1.freecodecamp.org/images/1*C6GOoIv20fG5PZZdO4yrXQ.jpeg)

* **Loaders**

Now if you write JSX in your React code, you can either use the _jsx-loader_ or _babel-loader_ to pre-compile JSX into JavaScript. So you can run _npm install jsx-loader_ and include this in your config:

```js
loaders: [
    {                 
        test: /\.js$/,                 
        loader: 'jsx-loader'             
    },
]
```

However, if you write your code in JSX and ES6, then you’ll need to use the _babel-loader,_ along with the babel plugin for React. So run _npm install babel-core babel-loader babel-preset-es2015 babel-preset-react_ and then add this to your config instead of the above.

```js
loaders: [
    { 
         test: /\.js$/, 
         loader: ‘babel’,
         query: {
             presets: [‘react’, ‘es2015’]
         },
         include: path.join(__dirname, ‘public’)
    }
]
```

Likewise, you have loaders to compile TypeScript, CoffeeScript, etc.

### **Example**

* Your web-server file:

```js
var http = require("http");
var express = require("express");
var consolidate = require('consolidate');
var handlebars = require('handlebars');
var bodyParser = require('body-parser');

var routes = require('./routes');

var app = express();

//Set the folder-name from where you serve the html page.
app.set('views', 'views'); 

//For using handlebars as the template engine.
app.set('view engine', 'html');
app.engine('html', consolidate.handlebars);

//Set the folder from where you serve all static files like images, css, javascripts, libraries etc
app.use(express.static('./public')); 

app.use(bodyParser.urlencoded({ extended: true }));
var portNumber = 8000;

http.createServer(app).listen(portNumber, function(){
    console.log('Server listening at port '+ portNumber);
  	app.get('/', function(req, res){ 
  	    console.log('request to / received');
  		res.render('index.html');		
  	});
});
```

* app-main.js from where our front-end logic begins:

```js
define(
    [
        ‘react’,
        ’reactDom’,
        ’./components/home-page’
    ],
    function(React, ReactDom, HomePage){ 
        console.log(‘Loaded the Home Page’);
        ReactDom.render(<HomePage />, document.getElementById(‘componentContainer’));
    }
);
```

* _home-page.js_ is our parent React component which could contain something like this:

```js
define(['react', 'jquery', 'magnificPopup'], function(React, $) {
    var HomePage = React.createClass({
        getInitialState: function() {
            return {
                userName: 'ashwin'
            }
        },
        componentDidMount: function() {
            $('.test-popup-link').magnificPopup({
                type: 'image'
                // other options
            });
        },
    	render: function() {
    	    return (
      	    	<div id="homePage">
      	    	    {this.state.userName}
      	    	    <a className="test-popup-link" href="path-to-image.jpg">Open popup</a>
       	    	</div>
    	    );
    	}
    });

    return HomePage;
});
```

Opening your terminal, going to your project’s root folder and running _webpack_ will create two files: _vendors.bundle.js_ and _app.bundle.js._ Include these two files in your _index.html_ and hit [http://localhost:8000](http://localhost:8000) in your browser. This will render a component with your username displayed on the web page.

Now, as you work more on Webpack, you’ll get frustrated by constantly having to build your files manually to see changes reflected on your browser. Wouldn’t it be awesome if there was a way to automate the build process every time you make a change to a file? So if you’re tired of typing the command _webpack_ and hitting the refresh button on your browser every time you change a class name, do read on…

### Automating Builds with Webpack Dev Server and React Hot Loader

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZgWwc89ePisURX5SzcchJQ.png)

We will use this awesome module called **Webpack Dev Server**_._ It’s an express server which runs on port 8080 and emits information about the compilation state to the client via a socket connection. We will also use **React Hot Loader** which is plugin for Webpack that allows instantaneous live refresh without losing state while editing React components.

* **Step 1**: So go run _npm install webpack-dev-server — save-dev_ and then _npm install react-hot-loader — save-dev_

Then you need to tweak your Webpack config a little to use this plugin. In your loaders, add this before any other loader:

```js
{ 
    test: /\.jsx?$/, 
    loaders: [‘react-hot’],
    include: path.join(__dirname, ‘public’)
}
```

This tells Webpack to use React Hot Loader for your components. Make sure React Hot Loader comes before Babel in the loaders array. Also make sure you have _include: path.join(__dirname, ‘public’)_ to avoid processing node_modules, or you may get an error like this:

_Uncaught TypeError: Cannot read property ‘NODE_ENV’ of undefined_

* **Step 2**: Changes to your _index.html_

If your _index.html_ has something like this:

```html
<script src="/dist/js/vendors.js"></script>
<script src="/dist/js/app.bundle.js"></script>
```

Change this to point to your webpack-dev-server proxy:

```html
<script src="http://localhost:8080/dist/js/vendors.js"></script>
<script src="http://localhost:8080/dist/js/app.bundle.js"></script>
```

* **Step 3:** Run _webpack-dev-server --hot --inline_,

wait for the bundling to finish, then hit [http://localhost:8000](http://localhost:8000) (your express server port) in your browser.

If you run into any errors while setting up React Hot Loader, you’ll find this [**troubleshooting guide**](https://github.com/gaearon/react-hot-loader/blob/master/docs/Troubleshooting.md) and this awesome answer on Stack Overflow on [**Managing jQuery Plugin Dependency with Webpack**](http://stackoverflow.com/questions/28969861/managing-jquery-plugin-dependency-in-webpack) very helpful. In addition, you can take a look at the Webpack setup for my projects [here](https://github.com/ashwin01/ReactJS-AdminLTE) and [here](https://github.com/ashwin01/crew-stack).

This is only meant for development. While in production, you need to minify all your files. Just running _webpack -p_ will minify/uglify/concatenate all your files.

Wouldn’t it be awesome if there was a way to view all your file dependencies in a beautiful tree-like visualization? There is a web-app which does that.

In your terminal, run _webpack — profile — json > stats.j_son. This will generate a JSON file called stats.json. Go [to http://webpack.github.io/analy](http://webpack.github.io/analyse/)se/ and upload the file, and you’ll see all dependencies in a tree like structure.

![Image](https://cdn-media-1.freecodecamp.org/images/1*UmuieidXSVw6P6sRpYgsGQ.png)

> _Liked what you read? You should [subscribe](http://forum.booleanhunter.com). I won’t waste your time._

