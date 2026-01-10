---
title: A beginner’s introduction to Webpack
subtitle: ''
author: Flavio Copes
co_authors: []
series: null
date: '2018-06-13T18:34:33.000Z'
originalURL: https://freecodecamp.org/news/a-beginners-introduction-to-webpack-2620415e46b3
coverImage: https://cdn-media-1.freecodecamp.org/images/0*iCgamjcfG4fe8Yhr.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: webpack
  slug: webpack
seo_title: null
seo_desc: 'Webpack is a tool that lets you compile JavaScript modules. It’s also known
  as a module bundler.

  Given a large number of files, it generates a single file (or a few files) that
  run your app.

  It can perform many operations:


  helps you bundle your reso...'
---

Webpack is a tool that lets you compile JavaScript modules. It’s also known as a **module bundler**.

Given a large number of files, it generates a single file (or a few files) that run your app.

It can perform many operations:

* helps you bundle your resources.
* watches for changes and re-runs the tasks.
* can run Babel transpilation to ES5, allowing you to use the latest [JavaScript](https://flaviocopes.com/javascript/) features without worrying about browser support.
* can transpile CoffeeScript to JavaScript
* can convert inline images to data URIs.
* allows you to use require() for CSS files.
* can run a development webserver.
* can handle hot module replacement.
* can split the output files into multiple files to avoid having a huge JS file to load in the first page hit.
* can perform [tree shaking](https://flaviocopes.com/javascript-glossary/#tree-shaking).

Webpack is not limited to being used on the front-end, but is useful in backend Node.js development as well.

There are many predecessors of Webpack and lots of similarities in what those tools and Webpack do. The main difference is that those tools are known as **task runners**, while Webpack was born as a module bundler.

Webpack is a more focused tool. You just need to specify an entry point to your app (it could even be an HTML file with script tags) and webpack analyzes the files and bundles them in a single JavaScript output file that includes everything you need to run the app.

### Installing Webpack

Webpack can be installed globally or locally for each project.

### Global install

Here’s how to install it globally with [Yarn](https://flaviocopes.com/yarn/):

```
yarn global add webpack webpack-cli
```

with [npm](https://flaviocopes.com/npm/):

```
npm i -g webpack webpack-cli
```

once this is done, you should be able to run

```
webpack-cli
```

![Image](https://cdn-media-1.freecodecamp.org/images/D8QBAOc2eqjQsHVi4ieq-pf6wBtZfrhMv5-n)

### Local Install

Webpack can be installed locally as well. It’s the recommended setup, because Webpack can be updated per-project, and you have less resistance in using the latest features just for a small project rather than updating all the projects you have that use Webpack.

With [Yarn](https://flaviocopes.com/yarn/):

```
yarn add webpack webpack-cli -D
```

with [npm](https://flaviocopes.com/npm/):

```
npm i webpack webpack-cli --save-dev
```

Once this is done, add this to your `package.json` file:

```
{   //...   "scripts": {     "build": "webpack"   } }
```

Once this is done, you can run Webpack by typing

```
yarn build
```

in the project root.

### Webpack configuration

By default, Webpack (starting from version 4) does not require any config if you respect these conventions:

* the **entry point** of your app is `./src/index.js`
* the output is put in `./dist/main.js`.
* Webpack works in production mode

You can customize every little bit of Webpack of course, when you need. The Webpack configuration is stored in the `webpack.config.js` file, in the project root folder.

### The entry point

By default the entry point is `./src/index.js` This simple example uses the `./index.js` file as a starting point:

```
module.exports = {  /*...*/  entry: './index.js'  /*...*/}
```

### The output

By default the output is generated in `./dist/main.js`. This example puts the output bundle into `app.js`:

```
module.exports = {  /*...*/  output: {    path: path.resolve(__dirname, 'dist'),    filename: 'app.js'  }  /*...*/}
```

Using Webpack allows you to use `import` or `require` statements in your JavaScript code not just to include other JavaScript, but any kind of file (for example CSS).

Webpack aims to handle all our dependencies, not just JavaScript, and loaders are one way to do that.

For example, in your code you can use:

```
import 'style.css'
```

by using this loader configuration:

```
module.exports = {  /*...*/  module: {    rules: [      { test: /\.css$/, use: 'css-loader' },    }]  }  /*...*/}
```

The [regular expression](https://flaviocopes.com/javascript-regular-expressions/) targets any CSS file.

A loader can have options:

```
module.exports = {  /*...*/  module: {    rules: [      {        test: /\.css$/,        use: [          {            loader: 'css-loader',            options: {              modules: true            }          }        ]      }    ]  }  /*...*/}
```

You can require multiple loaders for each rule:

```
module.exports = {  /*...*/  module: {    rules: [      {        test: /\.css$/,        use:          [            'style-loader',            'css-loader',          ]      }    ]  }  /*...*/}
```

In this example, `css-loader` interprets the `import 'style.css'` directive in the CSS. `style-loader` is then responsible for injecting that CSS in the DOM, using a `<sty`le> tag.

The order matters, and it’s reversed (the last is executed first).

What kind of loaders are there? Many! [You can find the full list here](https://webpack.js.org/loaders/).

A commonly used loader is [Babel](https://flaviocopes.com/babel/), which is used to transpile modern JavaScript to ES5 code:

```
module.exports = {  /*...*/  module: {    rules: [      {        test: /\.js$/,        exclude: /(node_modules|bower_components)/,        use: {          loader: 'babel-loader',          options: {            presets: ['@babel/preset-env']          }        }      }    ]  }  /*...*/}
```

This example makes Babel preprocess all our React/JSX files:

```
module.exports = {  /*...*/  module: {    rules: [      {        test: /\.(js|jsx)$/,        exclude: /node_modules/,        use: 'babel-loader'      }    ]  },  resolve: {    extensions: [      '.js',      '.jsx'    ]  }  /*...*/}
```

See the `babel-loader` options [here](https://webpack.js.org/loaders/babel-loader/).

### Plugins

Plugins are like loaders, but on steroids. They can do things that loaders can’t do, and they are the main building blocks of Webpack.

Take this example:

```
module.exports = {  /*...*/  plugins: [    new HTMLWebpackPlugin()  ]  /*...*/}
```

The `HTMLWebpackPlugin` plugin does the job of automatically creating an HTML file and adding the output JS bundle path, so the JavaScript is ready to be served.

There are [lots of plugins available](https://webpack.js.org/plugins/).

One useful plugin, `CleanWebpackPlugin`, can be used to clear the `dist/` folder before creating any output, so you don’t leave files around when you change the names of the output files:

```
module.exports = {  /*...*/  plugins: [    new CleanWebpackPlugin(['dist']),  ]  /*...*/}
```

### The Webpack mode

This mode (introduced in Webpack 4) sets the environment on which Webpack works. It can be set to `development` or `production` (defaults to production, so you only set it when moving to development).

```
module.exports = {  entry: './index.js',  mode: 'development',  output: {    path: path.resolve(__dirname, 'dist'),    filename: 'app.js'  }}
```

Development mode:

* builds very fast
* is less optimized than production
* does not remove comments
* provides more detailed error messages and suggestions
* provides a better debugging experience

Production mode is slower to build, since it needs to generate a more optimized bundle. The resulting JavaScript file is smaller in size, as it removes many things that are not needed in production.

I made a sample app that just prints a `console.log` statement.

Here’s the production bundle:

![Image](https://cdn-media-1.freecodecamp.org/images/alm5uVDatSP2YQ6MJ6QcXBIAvq3CQggpEzIs)

Here’s the development bundle:

![Image](https://cdn-media-1.freecodecamp.org/images/OKvuW1qYszkWflVJPEDXjK8QBuheqi28UpaQ)

### Running Webpack

Webpack can be run from the command line manually if installed globally. But generally you write a script inside the `package.json` file, which is then run using `npm` or `yarn`.

For example this `package.json` scripts definition we used before:

```
"scripts": {  "build": "webpack"}
```

allows us to run `webpack` by running

```
npm run build
```

or

```
yarn run build
```

or simply

```
yarn build
```

### Watching changes

Webpack can automatically rebuild the bundle when a change in your app happens, and it keeps listening for the next change.

Just add this script:

```
"scripts": {  "watch": "webpack --watch"}
```

and run

```
npm run watch
```

or

```
yarn run watch
```

or simply

```
yarn watch
```

One nice feature of the watch mode is that the bundle is only changed if the build has no errors. If there are errors, `watch` will keep listening for changes, and try to rebuild the bundle, but the current, working bundle is not affected by those problematic builds.

### Handling images

Webpack allows you to use images in a very convenient way, using the `[file-loader](https://webpack.js.org/loaders/file-loader/)` loader.

This simple configuration:

```
module.exports = {  /*...*/  module: {    rules: [      {        test: /\.(png|svg|jpg|gif)$/,        use: [          'file-loader'        ]      }    ]  }  /*...*/}
```

Allows you to import images in your JavaScript:

```
import Icon from './icon.png'const img = new Image()img.src = Iconelement.appendChild(img)
```

Where `img` is an HTMLImageElement. Check out the [Image docs](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/Image).

`file-loader` can handle other asset types as well, like fonts, CSV files, XML, and more.

Another nice tool to work with images is the `url-loader` loader.

This example loads any PNG file smaller than 8KB as a [data URL](https://flaviocopes.com/data-urls/).

```
module.exports = {  /*...*/  module: {    rules: [      {        test: /\.png$/,        use: [          {            loader: 'url-loader',            options: {              limit: 8192            }          }        ]      }    ]  }  /*...*/}
```

### Process your SASS code and transform it to CSS

Using `sass-loader`, `css-loader` and `style-loader`:

```
module.exports = {  /*...*/  module: {    rules: [      {        test: /\.scss$/,        use: [          'style-loader',          'css-loader',          'sass-loader'        ]      }    ]  }  /*...*/}
```

### Generate Source Maps

Since Webpack bundles the code, Source Maps are mandatory to get a reference to the original file that raised an error. For example:

You tell Webpack to generate source maps using the `devtool` property of the configuration:

```
module.exports = {  /*...*/  devtool: 'inline-source-map',  /*...*/}
```

`devtool` has [many possible values](https://webpack.js.org/configuration/devtool/), the most used probably are:

* `none`: adds no source maps
* `source-map`: ideal for production, provides a separate source map that can be minimized, and adds a reference into the bundle, so development tools know that the source map is available. Of course you should configure the server to avoid shipping this, and just use it for debugging purposes
* `inline-source-map`: ideal for development, inlines the source map as a Data URL

> I publish 1 free programming tutorial per day on [flaviocopes.com](https://flaviocopes.com), check it out!

_Originally published at [flaviocopes.com](https://flaviocopes.com/webpack)._

