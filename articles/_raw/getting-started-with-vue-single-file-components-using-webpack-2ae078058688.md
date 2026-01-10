---
title: How to get started with Vue single file components using Webpack
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-11T20:07:17.000Z'
originalURL: https://freecodecamp.org/news/getting-started-with-vue-single-file-components-using-webpack-2ae078058688
coverImage: https://cdn-media-1.freecodecamp.org/images/1*tag8gBfSQ9I4dxLJOAg3QQ@2x.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: Vue.js
  slug: vuejs
- name: webpack
  slug: webpack
seo_title: null
seo_desc: 'By Dushyant Sabharwal

  This guide assumes that you have some idea about vue. It aims to save you time,
  trying to help you understand the webpack config for starting with vue and its single
  file components. You can use vue-cli for creating the project ...'
---

By Dushyant Sabharwal

_This guide assumes that you have some idea about `vue`. It aims to save you time, trying to help you understand the `webpack` config for starting with `vue` and its single file components. You can use `vue-cli` for creating the project template but this is for people who want to dig in further._

You are probably a developer who knows the front-end. You have decided to take your app to the next level by adopting `vue` as the front-end framework. You jump into the documentation and start reading about how to develop components, all while drawing parallels in your head with use-cases for the first component in your project. The framework and documentation turns out to be awesome and you cannot wait to start using `vue`.

If this sounds familiar, then that’s great!

TL;DR you can clone or fork the repository [here](https://github.com/dushyant89/vue-webpack) and get started.

### Let’s get started

Our goal is to write our first component, but **not the way it’s done below**. Though there is nothing wrong with loading the script file like this, it gets messier when you end up loading multiple script files this way.

We will be using `[webpack](https://webpack.js.org/configuration/devtool/)` for bundling our app. If you haven’t looked into `webpack`, then now is the time to configure your first app. It looks daunting at first, but the latest version (v4) is super easy and intuitive to use.

### Installing packages

In order to get to that point, let’s install some basic packages which we’ll need. We will be using `npm` for managing the packages. If you are not confident using `npm`, don’t worry! Just follow along. Make sure you have installed `node` and `npm` on your machine.

**Note**: If you have time on your hands, then [do read up](https://hackernoon.com/things-which-every-developer-should-know-when-starting-with-modern-front-end-development-7030486bf092) on how npm works and what it means for the security of your app.

Moving along…

```
npm install vue
```

```
npm install webpack --save-dev
```

Since we will be writing our code in `ES6` and above, we need something to transpile or transform our code. We will be using `babel` with `webpack` to help us come up with a version of code which will run in browsers which still do not support full spec of `ES6` .

[This](https://www.fullstackreact.com/articles/what-are-babel-plugins-and-presets/) article gives a nice overview on babel, and will explain in more detail why we need the below packages.

```
npm install babel-core --save-dev
```

```
npm install babel-loader --save-dev
```

```
npm install babel-preset-env --save-dev
```

```
npm install babel-preset-stage-2 --save-dev
```

Your `package.json` should look something like the below. Your versions might be different when you install the below packages, which is fine as long as the app doesn’t break.

If you want to install the specific versions as you see above, then simply do

```
npm install webpack-cli@^3.0.2 --save-dev
```

Now that our basic toolset is setup, lets focus our attention on the idea of how are we gonna write the`template` or `html` part of our first component. Will it be in a separate `.html` file ? Or will it include an existing file like `index.html`? Or will it be in a `string` which is then further compiled using some library? I have been through this train of thought, as well.

`Vue` solves this problem by providing a way to write components where you can associate the `template` part and the `script` part of the component in a single file. How awesome is that?

For example, if you are building a simple `table` component, then you can name the file as `table.vue` which has everything the component needs. What if I tell you that you can have `styles` also in the same `.vue`file which are specific to that component? I know! Sounds crazy!

Let’s install the below packages so we can have single file components, or `SFCs`:

```
npm install vue-template-compiler --save-dev
```

```
npm install vue-loader --save-dev
```

```
npm install css-loader --save-dev
```

```
npm install vue-style-loader --save-dev
```

`vue-template-compiler` is for making sense of the `template` section of the component.

`vue-loader` enables `webpack` to load single file components.

`css-loader` and `vue-style-loader` allow us to author styles in the component.

Your `package.json` should look something like the below now:

### Webpack

Now that we have every package we need in our arsenal, all we need is a way to instruct `webpack`. If you are trying to deal with`webpack` and how it works, it’s best to understand the intuition of why that tool exists in the first place. It doesn’t matter if we use `webpack` or not, we just need some tool which can do things like:

* Process entry points in our app for starting the process
* Name the output/processed files and specify their location
* Process different types of files like `.css` , `.js` or `.vue`
* Hot reloading the changed files in order to rebuild the whole thing

Webpack does all these things (and much more) if you just specify what needs to be done via a config object.

We will be using `webpack-dev-server` for serving static and dynamic assets in our project, because why not.

### Looking at the code

Let’s clone or fork (if you want to improve) [this project](https://github.com/dushyant89/vue-webpack).

You will see that the project has the same `package.json` as mentioned above. Let’s install and run the project based on the instructions in the repo.

`index.html` has our first component called `main-content`:

```
<div id="mainContent">    <main-content></main-content></div>
```

Our `main-content.vue`, which is a `SFC`, looks like the below. As you can see, it has three sections: `template` , `script` and `style` . Everything is tied to our component neatly and `webpack` takes care of the rest.

Head to [http://localhost:8010/](http://localhost:8010/) in your browser and you’ll notice our `main-content` component. Now change something in the component like below:

```
<template>    <div class="main-content">        <h1> This is my first modified component in Vue </h1>        <h3> {{ webpack }} </h3>    </div></template>
```

and notice how the heading changes in the browser. To understand how it works, have a look at `webpack.config.js`. Each section in the config has comments explaining why we need it.

Let’s divide the `webpack` config into three main parts.

#### **The input/output to Webpack**

#### **Processing Vue single file components and other JS modules**

#### **Configuring the Webpack dev server**

Each of the options in the config are pretty self-explanatory, and you can tweak them to understand them better. For example, you can remove one of the properties and notice the error(s).

**Note**: every time you change the config, you have to stop (cmd + C) and run `npm run start` for the changes to reflect.

You can add more options to the app by reading through the [docs](https://webpack.js.org/configuration/devtool/), and feel free to fork the [project](https://github.com/dushyant89/vue-webpack) for improvements.

If you think this article helped you, then you can [buy me a coffee](https://www.buymeacoffee.com/dushyant) or just share with others. Cheers ?

[**Buy Dushyant Sabharwal a Coffee - BuyMeACoffee.com**](https://www.buymeacoffee.com/dushyant)  
[_I am a full stack developer who loves writing stuff which can help other developers save time_www.buymeacoffee.com](https://www.buymeacoffee.com/dushyant)

