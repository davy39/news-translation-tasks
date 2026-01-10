---
title: Make multipage HTML development suck less with Pug
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-03T15:01:11.000Z'
originalURL: https://freecodecamp.org/news/make-multipage-html-development-suck-less-with-pug-fb23bc8e7874
coverImage: https://cdn-media-1.freecodecamp.org/images/1*bHG9n86BQWgllXfDw0uXhw.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
- name: technology
  slug: technology
- name: webpack
  slug: webpack
seo_title: null
seo_desc: 'By Jared Nutt

  Inspired by a true story

  Let’s take a journey…

  Imagine you are on the call list for a freelance agency in a city of your choosing.
  Now let’s say you get a nice message in your inbox. You open up the message and
  it looks pretty normal.


  ...'
---

By Jared Nutt

#### Inspired by a true story

### Let’s take a journey…

Imagine you are on the call list for a freelance agency in a city of your choosing. Now let’s say you get a nice message in your inbox. You open up the message and it looks pretty normal.

> We have an immediate need for a Developer to get started today.

the message and it looks pretty normal.

_We have an immediate need for a Developer to get started today._

Being a person who enjoys eating food to survive, you type in some info and apply.

Within five minutes of hitting that send button, you get a call. 10 minutes after that, you’re getting the server access.

Needless to say, you’re on a deadline. That deadline is by the end of the day.

You open up the HTML files and look into them…in horror.

The code is all over the place, messy and disorganized. Not to mention, you have to make adjustments to the header and footer…on five different pages.

The first thing you do is run it through [Prettify](https://github.com/google/code-prettify) (Thank god for Prettify). That cleaned it up, but there are some more problems. This is a static HTML site, which means every change you make to the global stuff (header, footer, and so on), you’re going to have to copy in **EVERY** file. Oh, my.

What are you gonna do???

Simple, you’re gonna whip up a Webpack file to handle the crappy part of writing HTML, and you’re gonna do it quickly.

## Here’s what you’re gonna need to be familiar with:

* Javascript! (because of Webpack)
* HTML! (because that’s what the internet is made of)
* CSS! (because who likes ugly things?)
* pug! (because that’s the point of this article!)
* npm (because it is God)
* Basic command line knowledge (because doing stuff via downloads is stupid…)
* Know who Jim Carrey is (because gifs)

If you aren’t familiar with pug, you can still manage your way through this. But if you’ve got time, read up on it. I recommend learning [pug with pugs](https://codepen.io/mimoduo/post/learn-pug-js-with-pugs). Or their [docs](https://pugjs.org/api/getting-started.html). Those are alright too, I guess.

Here’s the versions I used for this:

* html-loader: 0.5.5,
* html-webpack-plugin: 3.2.0,
* pug-html-loader: 1.1.5,
* Webpack: 4.12.0
* webpack-cli: 3.0.8
* npm: 6.1.0
* node: 10.4.0

**Update:** I made a video! Check it out if you don’t want to read, but would rather listen to my voice for 30 minutes.

%[https://youtu.be/vBJwetqiX0g]

# Step 1. Organize your project structure

This is how I like to organize my folder for these types of projects.

```
src/
oldHTML/
dist/
images/
css/
webpack.config
```

I like to put all the original HTML into a separate folder that I can’t accidentally delete. Webpack is a bit kinder than say, Gulp, which I’ve had delete an entire folder before ?. This structure is good enough to get us started.

# Step 2. Rev up the npm engine

Aside: I recently reverted back to `npm` from `yarn` for a few reasons. One of which was that it stopped working and I had little patience to make it work again. Interesting article [here](https://mixmax.com/blog/to-yarn-and-back-again-npm), if you want to read more.

**Anyways, init that npm.**

```
npm init -y
```

Note: (the **-y** is if you don’t want to answer any of its questions)

## **Install development dependencies.**

Don’t worry, I’ll explain each one as we go.

```
npm install -D webpack webpack-cli pug-html-loader html-webpack-plugin html-loader
```

## **Add some scripts to the package.json**

By default, package.json has one script, but we need to add a few.

```
"dev": "webpack --watch --mode development",
"prod": "webpack --mode production"
```

These are the two that I like to include. The first will run Webpack in development mode (note: the --mode flag is new to Webpack 4) and watch for file changes. The second is when we want to run Webpack in production, this usually minifies stuff.

It should look something like this:

```
"name": "pugTut",
"version": "1.0.0",
"description": "",
"main": "index.js",
"scripts": {
"test":
  "dev": "webpack --watch --mode development",
  "prod": "webpack --mode production"
},
.....more code
```

## **Create a couple starter files to test our Webpack config**

Webpack needs an entry point, so let’s make one. Create an **app.js** in the **src/** folder. It can be blank. Doesn’t matter. It also needs an initial pug file to compile. Create a **index.pug** file in the **src/** folder, as well.

## **Create and setup webpack.config.js in root directory**

Alright, if you haven’t used Webpack before, I’m going to walk through each part individually to give you (and hopefully me) an idea of wtf is going on in this config file.

First, let’s declare our dependencies.

```
// webpack.config.js
const path = require('path');
const webpack = require('webpack');
const HtmlWebpackPlugin = require('html-webpack-plugin');
```

**path** is a native Node dependency, so you shouldn’t have to worry about that being required in your package.json.

**Webpack** is, well Webpack…

**HtmlWebpackPlugin** is how we extract HTML. I’m not an expert on how Webpack works. From what I understand, since it is designed to consume JavaScript, we have to have loaders in our config file to pull out things like HTML and CSS. **HtmlWebpackPlugin** is how we do something useful with the HTML that gets extracted from the loaders.

Cool? Next step…

```
const pug = {
  test: /\.pug$/,
  use: ['html-loader?attrs=false', 'pug-html-loader']
};
```

This method is used by [Wes Bos](https://wesbos.com/) and I really like it, so I use it. We have to define rules on how to handle certain file types, for example .pug or .css. Putting it into a variable makes it more legible, in my opinion. Anyways, we setup a test case with a regexp, then define the loaders we want to use. For whatever reason, the loaders are listed in reverse order of what you’d think. I’m sure there is an explanation but I couldn’t find it.

Confused? What that means is, if we want to use pug to compile to HTML, we write it in the order above: our **html loader** -> **pug loader**. However, in reality when the code runs, it runs the **pug loader** first…then the **HTML loader**. Yep.

Note: Don’t worry about `?attrs=false` for right now, I’ll explain it a bit later.

Cool? Next step…

```
const config = {
  entry: './src/app.js',
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: '[name].bundle.js'
  },
  module: {
    rules: [pug]
  },
  plugins: [
    new HtmlWebpackPlugin({
      filename: 'index.html',
      template: 'src/index.pug',
      inject: false
    })
 ]
};
module.exports = config;
```

Holy Crap. That’s a lot of stuff. Let’s break it down.

**entry** is simply the entry point for our JS file.

**output** defines where we want our JS file to go. This is not where our HTML files will go. As mentioned above, **path** is a node module. **__dirname** is a variable we can get from Node. The filename is what we want to call our JS file. The `[name]` is a substitution. In this case, it uses the file name of the entry file. You can also use `[hash]` if you want a unique identifier.

**module** defines the different modules. For the purpose of this tutorial, there is only one module with one set of rules. **rules** defines the rules we will use for that module. We throw the **pug** variable we made earlier into there. So nice, so clean.

Finally, plugins is where we get to add any third party stuff. In our case, we are using **HtmlWebpackPlugin** to do something with our pug files.

**filename** is what we want our HTML file to be called. **template** is the pug file that are compiling. **inject** is: “inject all assets into the given template.” I have it set to false because…well, honestly I don’t remember.

One of the crappiest things about **HtmlWebpackPlugin** is that you have to create an entry for **EVERY** HTML file. I tried to figure a way around it, but found no simple solutions.

```js
// webpack.config.js
const path = require('path');
const webpack = require('webpack');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const pug = {
  test: /\.pug$/,
  use: ['html-loader?attrs=false', 'pug-html-loader']
};
const config = {
  entry: './src/app.js',
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: '[name].bundle.js'
  },
  module: {
    rules: [pug]
  },
  plugins: [
    new HtmlWebpackPlugin({
      filename: 'index.html',
      template: 'src/index.pug',
      inject: false
    })
 ]
};
module.exports = config;
```

Before we move on, let’s make sure our code works! Run the script.

```
npm run dev
```

If all went well, you should see something like this:

![Image](https://www.freecodecamp.org/news/content/images/2019/07/1_JQLr9uvGeW2P9VQRaWmsMA.png)

We’ve come a long way. Here’s a present:



# Step 3. Break up the pages into partials

This is where magic starts happening. I know it seems like we’ve been working for a while with very little gain, but trust me…it was worth it.

One of the most important features for pug is the partials. The idea is to have one file that holds most of your global code (head, header, footer, nav, and so on) and have individual files for all your content.

Let’s make a couple files. You should have created the **index.pug** file already, but let’s make one more, **layout.pug**.

```
src/
- index.pug
- layout.pug
```

# Step 4. Setup layout file

The layout file is basically the main template for your whole site. It will have hold all the global stuff, for example head, header and footer.

```
//- layout.pug
doctype html
html
  head
    title I'm a title
  body
    block header
    block content
    block footer
  script(src="somescript.js")
```

I guess something to explain is that pug is all based on indentation, similar to YAML. It is glorious, because that means no more closing tags! However, this can throw some, especially those with crappy indentation to begin with. So just make sure to start slow and make sure everything is indented correctly and you’ll be fine.

Looking at our layout.pug file, you’ll see some familiar HTML tags mixed with unfamiliar ones. I highly suggest downloading syntax highlighting for pug in your editor of choice. If you’re using VSCode, it should come with it by default. Thanks Microsoft.

I think it’s pretty easy to figure out, but let’s take a look at the meat of the document to make sure we know what’s going on.

```
head
  title I'm a title
body
  block header
  block content
  block footer
script(src="somescript.js")
```

**head**, **body**, **title** and **script** are normal tags, but what the hell is **block**? **block** is how we define dynamic content. Basically, this is telling pug that some content is going to go in here. Hopefully it’ll make more sense when we create our individual page files.

# Step 5. Create more partials

Let’s make use of that index.pug file.

```
//- index.pug
extends layout
block content
  p Woah.
```

Looking at our index file, it seems awfully small for a whole HTML page. That’s because of that little **extends** fella. extends tells pug that you want to use another pug file as the template, in our case **layout.** Then below that **block conten**t is in reference to what we put in our **layout.pug** file.

If you have your Webpack still running in the background, it should recompile and you’ll get a fresh new **index.html** in your **dist/** folder. If not, run Webpack again.

# Step 6. Grab all the old HTML

Those starter files are fine and dandy, but we need to make some real progress. We need to start grabbing that HTML and using it! Luckily, pug will recognize regular old HTML tags, so you can literally copy all the HTML content you want and just paste it in there.

It might look something like this:

```
extends layout
block content
  <h1>blerb</h1>
  <p>Woah.</p>
```

**Alright, it’s not really that simple.**

Like I mentioned, pug is based on indentation. To make life easier on yourself, I suggest removing all indentation from the HTML file before pasting into the pug file. It will mostly work, but you’ll probably have to finagle it a bit. Lucky for us, **pug-html-loader** will tell us what’s wrong with it when it tries to compile. There are some examples of common problems in the next Step.

# Step 7. Start optimizing

I’m not gonna lie, when you first throw in HTML, Webpack is not gonna like it. Here are a few things to look out for:

## **Images**

1. Make sure the links to the images are good. For whatever reason, it often fails if the src = “images/” instead of src= “/images/”

2. I promised earlier to get back to what `?attrs=false` was, well, here we are!

This is the blurb from the [html-loader](https://www.npmjs.com/package/html-loader) site explaining what that does.

> To completely disable tag-attribute processing (for instance, if you’re handling image loading on the client side) you can pass in `attrs=false`.

```
html-loader?attrs=false

```

## **Javascript**

pug doesn’t play nice with JS in script tags. If you are pasting in regular opening and closing JS script tags, it may work okay. However, if you want to make use of the pug script tag, just make sure to add a period on the end, like this:

# Step 8. Make more pages and start converting to pug tags

Clearly it’s useless if you are only doing the index page. For whatever you’re doing, just create a new file for each page you want. Also, make sure to make new **HtmlWebpackPlugin** entries in the **plugins** section in Webpack.

It’ll end up looking like this:

```js
//webpack.config.js
...previous code...
plugins: [
    new HtmlWebpackPlugin({
      filename: 'index.html',
      template: 'src/index.pug',
      inject: false
    }),
    new HtmlWebpackPlugin({
      filename: 'contact.html',
      template: 'src/contact.pug',
      inject: false
    })
  ]
...more code...
```

You don’t have to convert everything to pug format immediately. In fact, if you have a huge site with a crap ton of HTML, then you can do it as you go, but it does make it easier.

## **Includes**

This wouldn’t be a very good tutorial if we didn’t talk about includes. Remember those blocks in the layout file? Well, if you don’t want the layout file to be giant, you can create separate files that will be pulled in at compile time. For instance, if you want to make a single file that holds all the header info. Breaking it up this way also helps substantially with indentation.

Create a new file “header” in a new folder “includes”:

```
src/
-- includes/
   header.pug
```

In that file, put whatever you want to be in the header.

```
//- header.pug
header
  h1 I'm a header
```

Now go back to layout.pug and include it.

```
//- layout.pug
doctype html
html
  head
    title I'm a title
  body
    block header
      include includes/header
    block content
    block footer
  script(src="somescript.js")
```

# Step 7. Want to get Fancy?

There’s a ton more stuff you can do with pug and webpack. However, I think we’ve reached the end of the basics. Still, check out [mixins](https://pugjs.org/language/mixins.html). Those things are amazing.

# Wrapping Up

I highly suggest bringing in HTML slowly, otherwise you’ll end up debugging 1,000 errors at once.


