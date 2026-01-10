---
title: How to animate page transitions in Gatsby.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-11T18:20:49.000Z'
originalURL: https://freecodecamp.org/news/how-to-animate-page-transitions-in-gatsby-js-b36e3ae14c29
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Bb4qv_rhVEVz3JRtHD2zOg.png
tags:
- name: animation
  slug: animation
- name: GatsbyJS
  slug: gatsbyjs
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Dimitri Ivashchuk

  I’m totally enjoying Gatsby for various reasons, and in this post I want to share
  how easy it is to add customized page transitions to your website to make it more
  lively and smooth.

  We will be using Gatsby default starter to mak...'
---

By Dimitri Ivashchuk

I’m totally enjoying Gatsby for various reasons, and in this post I want to share how easy it is to add customized page transitions to your website to make it more _lively_ and _smooth._

We will be using [Gatsby](https://www.gatsbyjs.org/) default starter to make this example as isolated as possible, but you can be sure that it will also work for more complex starters and projects created by you from scratch.

As a teaser, we will build something similar to what you see when you follow links on this site. ?

### Getting started ?️

If you are new to Gatsby and want to follow along with this tutorial, be sure to install Gatsby’s command line interface ([Gatsby CLI](https://www.gatsbyjs.org/docs/)) so you can quickly bootstrap new projects in the future.

`npm install --global gatsby-cli`

Navigate to your project folder and create a new Gatsby project inside of it by running the following command in the terminal:

`gatsby new .`

It will create a project with the simplest possible setup and it should look like this: (it may vary due to further iterations on starter’s design)

![Image](https://cdn-media-1.freecodecamp.org/images/1*cl5xYdPxb87Pvw2cNOPFQg.png)
_Gatsby-default-starter_

### Installing necessary dependencies ⚙️

First of all we need to install [react-transition-group](https://github.com/reactjs/react-transition-group) which is responsible for watching out for elements entering and leaving the DOM and applying animations to them.

`npm install react-transition-group`

We will also install [gatsby-plugin-layout](https://www.gatsbyjs.org/packages/gatsby-plugin-layout/) that, in our case, provides the location property required for transitions to work and injects our layout to every page.

`npm install gatsby-plugin-layout`

To make the plugin work as expected, we need to move our layout component into the layouts folder at the root of our project and rename it to `index.js`. Let's also add `transition.js` to our components folder where we will supply all the transition logic. For now leave it empty as we have a little more to configure.

The last step is adding our `gatsby-plugin-layout` to our `gatsby-config.js` file that is located in the root of our project

### Transition component ?

This holds the full logic for transition that will be applied when a user decides to follow a link to another page on our site.

Inside `transition.js` add the following code which I will explain in the comments:

Now we can import the `Transition` component into the Layout component and wrap the children which represent our pages inside of it.

At this point you may experience a bug when some of your page elements are rendered twice. To solve that, just go trough the files in the `pages` folder and make sure that they don't import the `<Layo`ut> component and use it in the return statement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*grgRx163jrF102OjEy39mw.gif)
_Jerky animation that we want to fix_

Now that everything is working as expected and you are enjoying your newly added page transitions, you may notice a slight jerky bug that appears when your page is being scrolled down and animation starts. Note that it happens when there is more content on the page and you can scroll.

We can easily fix this with the help of including the below code in our `gatsby-browser.js` which you can find in the root of our project. What we do here is actually setting a time out for animation and waiting for it to be executed until the page scrolls to the top.

On your website it should look like this

![Image](https://cdn-media-1.freecodecamp.org/images/1*ghYOAUkIT1KOSqXcYHzw3w.gif)

I hope you’ve enjoyed this small post and will use your new knowledge whenever you need it. Here you can find a [link to GitHub repo](https://github.com/d-ivashchuk/animating-gatsby-pt) with the working code for this tutorial. Subscribe to [me on twitter](https://twitter.com/DivDev_) not to miss a next post about Gatsby.js and fun things you can do with it!

_Originally published at_ [https://divdev.io](https://divdev.io) which btw uses the animation technique we have learned in this post!

