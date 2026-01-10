---
title: How I solved and debugged my Webpack issue through trial, error, and a little
  outside help.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-02T09:34:35.000Z'
originalURL: https://freecodecamp.org/news/how-to-solve-webpack-problems-the-practical-case-79fb676417f4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*foxbYY6DryL2han-19rLEA.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: webpack
  slug: webpack
seo_title: null
seo_desc: 'By Margarita Obraztsova

  I would say that this was quite a journey. I knew that Webpack was not easy to configure:
  there are many parts with many options, there’s npm hell, and they change with new
  releases. No wonder it can easily become a troublesom...'
---

By Margarita Obraztsova

I would say that this was quite a journey. I knew that Webpack was not easy to configure: there are many parts with many options, there’s npm hell, and they change with new releases. No wonder it can easily become **a troublesome task to debug when something does not go as you expected** (that is, not as it is in the docs).

### Trying to debug

My debugging journey started with the following setup:

_webpack.config.js_

```
// webpack v4.6.0
```

```
const path = require('path');const HtmlWebpackPlugin = require('html-webpack-plugin');const WebpackMd5Hash = require('webpack-md5-hash');const CleanWebpackPlugin = require('clean-webpack-plugin');const webpack = require('webpack');
```

```
module.exports = {  entry: { main: './src/index.js' },  output: {    path: path.resolve(__dirname, 'dist'),    filename: '[name].[chunkhash].js'  },  devServer: {    contentBase: './dist',    hot: true,    open: true  },  module: {    rules: [      {         test: /\.js$/,        exclude: /node_modules/,        use: [          { loader: 'babel-loader' },          {            loader: 'eslint-loader',            options: {               formatter: require('eslint/lib/formatters/stylish')             }           }         ]       }     ]  },  plugins: [    new CleanWebpackPlugin('dist', {}),    new HtmlWebpackPlugin({      inject: false,      hash: true,      template: './src/index.html',      filename: 'index.html'    }),    new WebpackMd5Hash()  ]
```

```
};
```

_package.json_

```
{  "name": "post",  "version": "1.0.0",  "description": "",  "main": "index.js",  "scripts": {    "build": "webpack --mode production",    "dev": "webpack-dev-server"   },  "author": "",  "license": "ISC",  "devDependencies": {    "babel-cli": "^6.26.0",    "babel-core": "^6.26.0",    "babel-loader": "^7.1.4",    "babel-preset-env": "^1.6.1",    "babel-preset-react": "^6.24.1",    "babel-runtime": "^6.26.0",    "clean-webpack-plugin": "^0.1.19",    "eslint": "^4.19.1",    "eslint-config-prettier": "^2.9.0",    "eslint-loader": "^2.0.0",    "eslint-plugin-prettier": "^2.6.0",    "eslint-plugin-react": "^7.7.0",    "html-webpack-plugin": "^3.2.0",    "prettier": "^1.12.1",    "react": "^16.3.2",    "react-dom": "^16.3.2",    "webpack": "^4.6.0",    "webpack-cli": "^2.0.13",    "webpack-dev-server": "^3.1.3",    "webpack-md5-hash": "0.0.6"  }}
```

_.babelrc_

```
{  "presets": ["env", "react"]}
```

_.eslintrc.js_

```
module.exports = {  env: {    browser: true,    commonjs: true,    es6: true  },  extends: [    'eslint:recommended',    'plugin:react/recommended',    'prettier',    'plugin:prettier/recommended'  ],  parserOptions: {    ecmaFeatures: {      experimentalObjectRestSpread: true,      jsx: true    },    sourceType: 'module'  },  plugins: ['react', 'prettier'],  rules: {    indent: ['error', 2],    'linebreak-style': ['error', 'unix'],    quotes: ['warn', 'single'],    semi: ['error', 'always'],    'no-unused-vars': [      'warn',      { vars: 'all', args: 'none', ignoreRestSiblings: false }    ],    'prettier/prettier': 'error'   }};
```

_prettier.config.js_

```
// .prettierrc.js
```

```
module.exports = {  printWidth: 80,  tabWidth: 2,  semi: true,  singleQuote: true,  bracketSpacing: true};
```

And in the _src/_ folder:

_index.html_

```
<html> <head></head> <body>    <div id="app"></div>    <script src="<%= htmlWebpackPlugin.files.chunks.main.entry %>"></script> </body></html>
```

_index.js_

```
import React from 'react';import { render } from 'react-dom';import Hello from './Hello';
```

```
class App extends React.Component {  render() {    return (      <div>        <Hello hello={'Hello, world! And the people of the world!'} />     </div>    );  }}render(<App />, document.getElementById('app'));
```

_Hello.js_

```
import React from 'react';import PropTypes from 'prop-types';
```

```
class Hello extends React.Component {  render() {    return <div>{this.props.hello}</div>;  }}
```

```
Hello.propTypes = {  hello: PropTypes.string};
```

```
export default Hello;
```

This was the overall project structure:

![Image](https://cdn-media-1.freecodecamp.org/images/IA4bRe-OgTy6uExvsJwfk8WTW8uc-atToltw)

### So, what was the problem?

As you can see, I set up the environment, the ESLinting, and so on. I created everything so that I could start coding and add my new components to my shiny new component library.

But what if I got an error? Let’s go screw something up.

![Image](https://cdn-media-1.freecodecamp.org/images/5SfyW4tlIrnZSnRqM7h1z-5X4Kx218yWsVeN)

**If we try to backtrace the origin of the error from our Google Chrome browser console, this will be very difficult for us.** We would stumble upon something like this:

![Image](https://cdn-media-1.freecodecamp.org/images/IAUMuN5vGBRK02XiutfpKGAV-qnuQlhqjVwx)

![Image](https://cdn-media-1.freecodecamp.org/images/PiUlbODsL34GCkasgETv-gePRv-KYohgEBsU)

The source maps are not configured!

I want it to point to a file **Hello.js** and not to a bundled file, kinda like this guy did [here](http://erikaybar.name/webpack-source-maps-in-chrome/).

### This is probably a tiny thingy

Or so I thought. So I tried to set up the source maps as [described in the docs](https://webpack.js.org/guides/development/#using-webpack-dev-server) by adding [**devtool**](https://webpack.js.org/configuration/devtool/).

> When webpack bundles your source code, it can become difficult to track down errors and warnings to their original location. For example, if you bundle three source files (`a.js`, `b.js`, and `c.js`) into one bundle (`bundle.js`) and one of the source files contains an error, the stack trace will simply point to `bundle.js`. This isn't always helpful as you probably want to know exactly which source file the error came from.

> In order to make it easier to track down errors and warnings, JavaScript offers [source maps](http://blog.teamtreehouse.com/introduction-source-maps), which maps your compiled code back to your original source code. If an error originates from `b.js`, the source map will tell you exactly that. ([Source](https://webpack.js.org/guides/development/))

So I naively assumed this would work in my _webpack.config.js_:

```
...
```

```
module.exports = {  entry: { main: './src/index.js' },  output: {    path: path.resolve(__dirname, 'dist'),    filename: '[name].[chunkhash].js'  },  devtool: 'inline-source-map',  devServer: {    contentBase: './dist',    hot: true,    open: true  },  ...
```

and _package.json_

```
..."scripts": {  "build": "webpack --mode production",  "dev": "webpack-dev-server --mode development"}...
```

You have to add a development flag when doing it, otherwise it won’t work as the docs say. Yet, even with the suggested value, the source map did not act as I wanted it to.

![Image](https://cdn-media-1.freecodecamp.org/images/NN9n-KUqtxlW6sfANLqiIJHAB6Nka6XfiSkr)

If you read [this guide](https://survivejs.com/webpack/building/source-maps/#-sourcemapdevtoolplugin-and-evalsourcemapdevtoolplugin-) from SurviveJS, which you should, you will see.

After I tried every option from it, I resorted to GitHub issue hunting.

### GitHub issue hunting

Trying all the suggestions in GitHub issues did not help me.

At some point I thought something was wrong with webpack-dev-server. And it turned out that the webpack-dev-server has been in maintenance mode for a few months already.

![Image](https://cdn-media-1.freecodecamp.org/images/5bNNZcWIaA8PlUQgFKo9KprA3gkMyCY1i6Fx)

I discovered that after I stumbled upon [this issue](https://github.com/webpack/webpack-dev-server/issues/1161) where **they recommend to use webpack-serve instead of webpack-dev-server.**

Honestly, that was the first time I had heard about an alternative called **webpack-serve**. The docs did not look promising, either. But I still decided to give it a shot.

```
npm install webpack-serve --save-dev
```

I created _serve.config.js_

```
const serve = require('webpack-serve');
```

```
const config = require('./webpack.config.js');
```

```
serve({ config });
```

I replaced **webpack-dev-server with webpack serve** in my package.json.

But trying webpack-serve didn’t solve it either.

So at this point I felt like I had used **every suggestion I could find on GitHub:**

* [Webpack 4 — Sourcemaps](https://stackoverflow.com/questions/48986641/webpack-4-sourcemaps) : this issue suggests that `devtool: 'source-map'` should work out of the box, but this was not the case for me
* [how to make webpack sourcemap to original files](https://stackoverflow.com/questions/34185748/how-to-make-webpack-sourcemap-to-original-files) : adding `devtoolModuleFilenameTemplate: info =>'file://' + path.resolve(info.absoluteResourcePath).replace(/\\/g, '`/') to my output config did not help much. But instead of client.js, it showed me index.js.
* [https://github.com/webpack/webpack/issues/6400](https://github.com/webpack/webpack/issues/6400) : this one is not an accurate description of my issue, so trying the methods here did not seem to help me
* I tried to use `webpack.SourceMapDevToolPlugin` but it didn’t work with my setup, even when I deleted devtools or set them to false
* I did not use the UglifyJS plugin here, so setting up options for it was not a solution
* I know that webpack-dev-server is in maintenance now, so I tried webpack-serve, but it seemed like source maps do not work with it either
* I tried the source-map-support package as well, but no luck there. I have a similar situation as seen [here](https://github.com/webpack/webpack/issues/3165).

### The Holy StackOverflow

It took me forever to configure source maps, so I created an [issue](https://stackoverflow.com/questions/50105741/webpack-4-devtool-option-does-not-work-with-webpack-dev-server) on StackOverflow.

Debugging webpack config is usually a cumbersome task: the best way to go about it is to create a config from a scratch. If something from the documentation does not work as expected, it might be a good idea to try to find a similar issue on a branch, or create your own issue. I thought so, anyway.

The first guy who answered my issue was really trying to help. He shared his own working config. Even helped me by creating [a pull request](https://github.com/marharyta/webpack-fast-development/pull/1/files).

The only problem here: **why does his setup work**? I mean, this is probably not magic, and there is some module incompatibility there. Sadly, I could not understand why my setup was not working:

![Image](https://cdn-media-1.freecodecamp.org/images/WqPfJ5e4-WAP3mCeLTFwwA2c-0qXMBAmzwKV)

The thing is that he did it with the best intentions by restructuring the project his way.

This meant that I would have some more setup in the project and would have to change quite a few things. That might have been ok if I was doing a test setup, but **I decided to do the gradual changes to the files to see where it was breaking.**

#### Dissecting the issue

So let’s take a look at the differences between his Webpack and _package.json_ and mine. Just for the record, I used a different repo in the question, so here is my [link to the repo](https://github.com/marharyta/webpack-fast-development) and my setup.

```
// webpack v4.6.0
```

```
const path = require('path');const HtmlWebpackPlugin = require('html-webpack-plugin');const WebpackMd5Hash = require('webpack-md5-hash');const CleanWebpackPlugin = require('clean-webpack-plugin');const stylish = require('eslint/lib/formatters/stylish');const webpack = require('webpack');
```

```
module.exports = {  entry: { main: './src/index.js' },  output: {   devtoolModuleFilenameTemplate: info => 'file://' + path.resolve(info.absoluteResourcePath).replace(/\\/g, '/'),
```

```
   path: path.resolve(__dirname, 'dist'),   filename: '[name].[hash].js'  },  mode: 'development',  devtool: 'eval-cheap-module-source-map',  devServer: {    contentBase: './dist',    hot: true  },  module: {    rules: [      {        test: /\.js$/,        exclude: /node_modules/,        loader: 'babel-loader'      },      {        test: /\.js$/,        exclude: /node_modules/,        loader: 'eslint-loader',        options: {          formatter: stylish         }       }     ]   },   plugins: [    // new webpack.SourceMapDevToolPlugin({    //   filename: '[file].map',    //   moduleFilenameTemplate: undefined,    //   fallbackModuleFilenameTemplate: undefined,    //   append: null,    //   module: true,    //   columns: true,    //   lineToLine: false,    //   noSources: false,    //   namespace: ''    // }),    new CleanWebpackPlugin('dist', {}),    new HtmlWebpackPlugin({      inject: false,      hash: true,      template: './src/index.html',      filename: 'index.html'    }),    new WebpackMd5Hash(),    // new webpack.NamedModulesPlugin(),    new webpack.HotModuleReplacementPlugin()  ]
```

```
};
```

_package.json_

```
{
```

```
"name": "post","version": "1.0.0","description": "","main": "index.js","scripts": {  "storybook": "start-storybook -p 9001 -c .storybook",  "dev": "webpack-dev-server --mode development --open",  "build": "webpack --mode production"},"author": "","license": "ISC","devDependencies": {  "@storybook/addon-actions": "^3.4.3",  "@storybook/react": "v4.0.0-alpha.4",  "babel-cli": "^6.26.0",  "babel-core": "^6.26.0",  "babel-loader": "^7.1.4",  "babel-preset-env": "^1.6.1",  "babel-preset-react": "^6.24.1",  "babel-runtime": "^6.26.0",  "clean-webpack-plugin": "^0.1.19",  "eslint": "^4.19.1",  "eslint-config-prettier": "^2.9.0",  "eslint-loader": "^2.0.0",  "eslint-plugin-prettier": "^2.6.0",  "eslint-plugin-react": "^7.7.0",  "html-webpack-plugin": "^3.2.0",  "prettier": "^1.12.1",  "react": "^16.3.2",  "react-dom": "^16.3.2",  "webpack": "v4.6.0",  "webpack-cli": "^2.0.13",  "webpack-dev-server": "v3.1.3",  "webpack-md5-hash": "0.0.6",  "webpack-serve": "^0.3.1"},"dependencies": {  "source-map-support": "^0.5.5"}
```

```
}
```

I left them intact on purpose so that you can see my debugging attempts. **Everything worked except for source maps**. Below, I will share what he changed in my config — but it is of course better to check the full pull request [here](https://github.com/marharyta/webpack-fast-development/pull/1/files?diff=unified).

```
 // webpack v4.6.0 const path = require('path'); const HtmlWebpackPlugin = require('html-webpack-plugin'); // deleting this module from the config-const WebpackMd5Hash = require('webpack-md5-hash'); const CleanWebpackPlugin = require('clean-webpack-plugin'); const stylish = require('eslint/lib/formatters/stylish'); const webpack = require('webpack');  module.exports = {  // adding the mode setting here instead of a flag+  mode: 'development',   entry: { main: './src/index.js' },   output: {  // deleting the path and the template from the output-    devtoolModuleFilenameTemplate: info =>-      'file://' + path.resolve(info.absoluteResourcePath).replace(/\\/g, '/'),-    path: path.resolve(__dirname, 'dist'),     filename: '[name].[hash].js'   },  // adding resolve option here+  resolve: {+    extensions: ['.js', '.jsx']+  },   //changing the devtool option   devtool: 'eval-cheap-module-source-map',  // changing the devServer settings   devServer: {-    contentBase: './dist',-    hot: true+    hot: true,+    open: true   },   module: {     rules: [    // putting my two checks into one (later he asked me in the chat to delete eslint option completely)       {-        test: /\.js$/,-        exclude: /node_modules/,-        loader: 'babel-loader'-      },-      {-        test: /\.js$/,+        test: /\.jsx?$/,         exclude: /node_modules/,-        loader: 'eslint-loader',-        options: {-          formatter: stylish-        }+        use: [+          { loader: 'babel-loader' },+          { loader: 'eslint-loader', options: { formatter: stylish } }+        ]       }     ]   },   plugins: [    //cleaned some options-    new CleanWebpackPlugin('dist', {}),+    new CleanWebpackPlugin('dist'),    //deleted some settings from the HTMLWebpackPlugin     new HtmlWebpackPlugin({-      inject: false,-      hash: true,-      template: './src/index.html',-      filename: 'index.html'+      template: './src/index.html'     }),  //completely removed the hashing plugin and added a hot module replacement one
```

```
-    new WebpackMd5Hash(),-    new webpack.NamedModulesPlugin(),+    new webpack.HotModuleReplacementPlugin()   ] };
```

_package.json_

```
"main": "index.js",   "scripts": {     "storybook": "start-storybook -p 9001 -c .storybook",  //added different flags for webpack-dev-server-    "dev": "webpack-dev-server --mode development --open",+    "dev": "webpack-dev-server --config ./webpack.config.js",     "build": "webpack --mode production"   },   "author": "",@@ -31,11 +31,6 @@     "react-dom": "^16.3.2",     "webpack": "v4.6.0",     "webpack-cli": "^2.0.13",-    "webpack-dev-server": "v3.1.3",-    "webpack-md5-hash": "0.0.6",-    "webpack-serve": "^0.3.1"-  },-  "dependencies": {//moved dev server to dependencies
```

```
-    "source-map-support": "^0.5.5"+    "webpack-dev-server": "v3.1.3"   } }
```

As you can see, he deleted a bunch of modules and added mode inside of the config. And taking a look at the pull request, you can see that he also added some specific react-oriented HMR.

This helped the source maps work by sacrificing a lot of plugins, but there was no concrete explanation for why he did what he did. As a person who reads the docs, this was not very satisfying for me.

Later, I took my initial webpack.connfig.js and started to add the changes step by step too see when the source maps finally started to work.

**Change 1:**

```
-    new CleanWebpackPlugin('dist', {}),+    new CleanWebpackPlugin('dist'),
```

**Change 2:**

I added webpack-dev-server to dependencies, not devDependencies:

```
...
```

```
},
```

```
"dependencies": {
```

```
  "webpack-dev-server": "^3.1.3"
```

```
}
```

```
}
```

```
...
```

**Change 3:**

Next I removed some devServer settings:

```
devServer: {-    contentBase: './dist',+    hot: true,+    open: true   },
```

**Change 4:**

Let’s remove stylish:

```
...
```

```
},
```

```
devtool: 'inline-source-map',  devServer: {    hot: true,    open: true  },
```

```
...
```

```
use: [  { loader: 'babel-loader' },  {    loader: 'eslint-loader'  }
```

```
]
```

```
....
```

**Change 5:**

Let’s try to remove the WebpackMd5Hash hashing plugin now:

```
...
```

```
module.exports = {mode: 'development',entry: { main: './src/index.js' },output: {  path: path.resolve(__dirname, 'dist'),  filename: '[name].js'  },devtool: 'inline-source-map',...
```

```
plugins: [  new CleanWebpackPlugin('dist'),  new HtmlWebpackPlugin({    inject: false,    hash: true,    template: './src/index.html',    filename: 'index.html'  })-    new WebpackMd5Hash(), ]
```

```
};
```

**Change 6:**

Now let’s try to remove some settings from HtmlWebpackPlugin:

```
...
```

```
plugins: [  new CleanWebpackPlugin('dist'),  new HtmlWebpackPlugin({    template: './src/index.html'  })]};
```

```
...
```

**Change 7:**

As we can see in his code, he added some resolve options here. I personally do not understand why we need them here. And I couldn’t find the info in the docs, either.

```
...
```

```
resolve: {  extensions: ['.js', '.jsx']},module: {
```

```
...
```

**Change 8:**

Deleting output path:

```
...
```

```
entry: { main: './src/index.js' },output: {  filename: '[name].js'},devtool: 'inline-source-map',
```

```
...
```

**Change 9:**

Adding the hot module replacement plugin:

```
...
```

```
const HtmlWebpackPlugin = require('html-webpack-plugin');const CleanWebpackPlugin = require('clean-webpack-plugin');const webpack = require('webpack');
```

```
...
```

```
plugins: [  new CleanWebpackPlugin('dist'),  new HtmlWebpackPlugin({    template: './src/index.html'  }),  new webpack.HotModuleReplacementPlugin()]};
```

```
...
```

**Change 10:**

Adding — config to package.json:

```
-    "dev": "webpack-dev-server --mode development --open",+    "dev": "webpack-dev-server --config ./webpack.config.js",
```

**Let’s make something clear: at this point I had almost re-written the config.**

This is a massive issue, since we cannot just rewrite it every time something is not working!

### Create-react-app in the best source to learn about webpack

As a last resort, I went to check how create-react-app implements the source mapping. That was the right decision after all. This is the config of [webpack dev version](https://github.com/facebook/create-react-app/blob/next/packages/react-scripts/config/webpack.config.dev.js).

If we check how **devtool** is implemented there, we will see:

> // You may want ‘eval’ instead if you prefer to see the compiled output in DevTools.

> // See the discussion in [https://github.com/facebook/create-react-app/issues/343.](https://github.com/facebook/create-react-app/issues/343.)

> devtool: ‘cheap-module-source-map’

So this issue pointed me to another issue, found [here](https://github.com/facebook/create-react-app/issues/343).

```
// webpack v4
```

```
const path = require('path');const HtmlWebpackPlugin = require('html-webpack-plugin');const WebpackMd5Hash = require('webpack-md5-hash');const CleanWebpackPlugin = require('clean-webpack-plugin');
```

```
module.exports = {
```

```
mode: "development",entry: { main: './src/index.js' },output: {  path: path.resolve(__dirname, 'dist'),  filename: '[name].[hash].js'},devtool: 'cheap-module-source-map',devServer: {  contentBase: './dist',  hot: true,  open: true},module: {
```

Changing the lines still did not work — yet! I learned that source map is a long-hanging issue.

### **Ask from the right people**

Every open source project has maintainers. So, in this case, it was definitely the right move to ask the guys right away.

Although the trial and error method from Daniel did not really work out for me, I was pleasantly surprised by how mobile the maintainer team was.

![Image](https://cdn-media-1.freecodecamp.org/images/dcdxfW7u7weQbhJK1zspAgQblsQxbH9ObSzj)

![Image](https://cdn-media-1.freecodecamp.org/images/GP1mi8Ahmtigeeq-bzIxmVzcbs6LDUsf66zP)

So I created a repo with the setup you can see [here](https://github.com/marharyta/webpack-4.6.0-test). Check out the second commit there.

To make it easier for you, here is my project webpack.js where I rolled back to my initial, cleaner setup:

```
// webpack v4
```

```
const path = require('path');const HtmlWebpackPlugin = require('html-webpack-plugin');const WebpackMd5Hash = require('webpack-md5-hash');const CleanWebpackPlugin = require('clean-webpack-plugin');
```

```
module.exports = {  mode: 'development',  entry: { main: './src/index.js' },  output: {    path: path.resolve(__dirname, 'dist'),    filename: '[name].[hash].js'  },  devtool: 'inline-source-map',  devServer: {    contentBase: './dist',    hot: true,    open: true  },  module: {    rules: [      {        test: /\.js$/,        exclude: /node_modules/,        use: [          { loader: 'babel-loader' },          {            loader: 'eslint-loader',            options: {               formatter: require('eslint/lib/formatters/stylish')             }          }         ]        }      ]  },  plugins: [    new CleanWebpackPlugin('dist'),    new HtmlWebpackPlugin({      inject: false,      hash: true,      template: './src/index.html',      filename: 'index.html'    }),    new WebpackMd5Hash()  ]};
```

After checking my code, the maintainer created an [issue](https://github.com/marharyta/webpack-4.6.0-test/issues/1).

Let’s recap what he included there:

> Setting the `mode` option

> First issue I’ve found is how the `mode` option was set. In the npm scripts the mode was set as:

> **webpack --mode production**

> The correct way would be:

> **webpack --mode=production**

> Final state of npm scripts looks like this to me:

> **"scripts": {**  
>  **"build": "webpack --mode=production",**  
>  **"start": "webpack-dev-server --mode=development --hot"**  
> **}**

> I also changed `dev` to `start` since it's more standard and expected from other developers as a command. You can actually do `npm start`, without the `run` command ?

```
...
```

```
"scripts": {  "build": "webpack --mode production",  "dev": "webpack-dev-server --mode=development --hot"},
```

```
...
```

Next he suggested the following:

> devtool for source maps

> I always recommend the `inline-source-map` option, it's the most straight forward and it's included in the bundle itself as a comment at the end of it.

> **module.exports = {**  
> **+ devtool: 'inline-source-map',**  
>  **// rest of your config**  
> **}**

> I also recommend creating a separate object and populating this only on development:

> command

> **webpack-dev-server --mode=development NODE_ENV=development**

> webpack.config.js

> **const webpackConfig = {}**

> **if (process.env.NODE_ENV === 'development') {**  
>  **webpackConfig.devtool = 'inline-source-map'**  
> **}**

> This way you make sure the bundle on production doesn’t get affected by this.

Then he suggested to removing ESLint from loaders:

> Linting and developer experience

> **Honestly, I would delete `eslint` as a loader, it's super spammy and it messes with the development flow. I prefer to add a precommit githook to check this.**

> This is super easy by adding a script like this:

> **"scripts": {**  
> **+ "lint": "eslint ./src/**/*.js"**  
>  **"build": "webpack --mode=production",**  
>  **"start": "webpack-dev-server --mode=development --hot"**  
> **}**

> And then combining it with husky.

and adding it to scripts:

```
...
```

```
"scripts": {
```

```
"lint": "eslint ./src/**/*.js",
```

```
"build": "webpack --mode production",
```

```
"dev": "webpack-dev-server --mode=development --hot"
```

```
},
```

```
...
```

I made a mistake in src/_Hello.js_ **on purpose** to see how source maps worked this time.

```
import React from 'react';import PropTypes from 'prop-types';
```

```
class Hello extends React.Component {  console.log(hello.world);  render() {    return <div>{this.props.hello}</div>;  }}Hello.propTypes = {  hello: PropTypes.string};export default Hello;
```

### How I fixed the issue

The issue was EsLint. But after specifying the modes correctly and removing the eslint-loader, source maps worked fine!

Following the example the maintainer gave me, I updated my Webpack to:

```
// webpack v4
```

```
const path = require('path');const HtmlWebpackPlugin = require('html-webpack-plugin');const WebpackMd5Hash = require('webpack-md5-hash');const CleanWebpackPlugin = require('clean-webpack-plugin');module.exports = {  entry: { main: './src/index.js' },  output: {    path: path.resolve(__dirname, 'dist'),    filename: '[name].[hash].js'  },  devtool: 'inline-source-map',  devServer: {    contentBase: './dist',    hot: true,    open: true  },  module: {    rules: [     {      test: /\.js$/,      exclude: /node_modules/,      use: [{ loader: 'babel-loader' }]     }    ]  },  plugins: [    new CleanWebpackPlugin('dist'),    new HtmlWebpackPlugin({      inject: false,      hash: true,      template: './src/index.html',      filename: 'index.html'    }),    new WebpackMd5Hash()  ]};
```

and my package JSON to:

```
{
```

```
"name": "post","version": "1.0.0","description": "","main": "index.js","scripts": {  "build": "webpack --mode=production",  "start": "NODE_ENV=development webpack-dev-server --mode=development --hot"},"author": "","license": "ISC","devDependencies": {  "babel-cli": "^6.26.0",  "babel-core": "^6.26.0",  "babel-loader": "^7.1.4",  "babel-preset-env": "^1.6.1",  "babel-preset-react": "^6.24.1",  "babel-runtime": "^6.26.0",  "clean-webpack-plugin": "^0.1.19",  "eslint": "^4.19.1",  "eslint-config-prettier": "^2.9.0",  "eslint-loader": "^2.0.0",  "eslint-plugin-prettier": "^2.6.0",  "eslint-plugin-react": "^7.7.0",  "html-webpack-plugin": "^3.2.0",  "prettier": "^1.12.1",  "react": "^16.3.2",  "react-dom": "^16.3.2",  "webpack": "^4.6.0",  "webpack-cli": "^2.0.13",  "webpack-md5-hash": "0.0.6"},"dependencies": {  "webpack-dev-server": "^3.1.3"}
```

```
}
```

**Finally source maps worked!**

![Image](https://cdn-media-1.freecodecamp.org/images/XVzSiRqwXEr337uejbZq3-O2XJ5QsdmDOlrv)

![Image](https://cdn-media-1.freecodecamp.org/images/1TSTZwHiJF7pv36uyNBtEi2wbLNx-qLJLJ3K)

### **Conclusions:**

Source maps has been the subject of multiple discussions and bugs since 2016, as you can see [here](https://github.com/webpack/webpack/issues/3165).

**Webapack needs help with audit!**

After finding this bug, I submitted an [issue](https://github.com/webpack-contrib/eslint-loader/issues/227) to the ESLint loader package.

When it comes to checking source maps quality, we can use [this tool](http://sokra.github.io/source-map-visualization/).

### What can you do if you have a webpack issue?

In case if you stumble upon an issue with Webpack, do not panic! Follow these steps:

* Search in the GitHub issues similar to yours.
* Try to check boilerplates and see how the feature is implemented there, like create-react-app for instance.
* Ask questions on StackOverflow — do not be scared! Make sure that you have run out of ways to solve your issue on your own, though.
* Do not hesitate to tweet about it and ask maintainers directly.
* Create issues once you find them. This will help the contributors a lot!

In this article, I have provided you with my configuration file and the process I used to configure it step by step.

Note: since a lot of npm dependencies might change by the time you read this, the same config might not work for you! I kindly ask you to leave your errors in the comments below so that I can edit it later.

**Please, Subscribe and Clap for this article! Thanks!**

