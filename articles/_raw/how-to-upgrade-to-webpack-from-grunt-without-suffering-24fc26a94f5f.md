---
title: See How Easily You Can Upgrade To Webpack
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-13T11:44:03.000Z'
originalURL: https://freecodecamp.org/news/how-to-upgrade-to-webpack-from-grunt-without-suffering-24fc26a94f5f
coverImage: https://cdn-media-1.freecodecamp.org/images/0*H9-QqXnBR8Rr6MhF
tags:
- name: development
  slug: development
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: General Programming
  slug: programming
seo_title: null
seo_desc: 'By Yazan Aabed

  I’ve written this article to narrate the adventure that happened to me when upgrading
  an AngularJS project from Grunt to Webpack.


  _Photo by [Unsplash](https://unsplash.com/@tfrants?utm_source=medium&utm_medium=referral"
  rel="noopener"...'
---

By Yazan Aabed

_I’ve written this article to narrate the adventure that happened to me when upgrading an AngularJS project from Grunt to Webpack._

![Image](https://cdn-media-1.freecodecamp.org/images/0*H9-QqXnBR8Rr6MhF)
_Photo by [Unsplash](https://unsplash.com/@tfrants?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Tyler Franta</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

You can follow me on [twitter](https://twitter.com/YazanAabed) or check my latest articles on [my site yaabed.com](https://www.yaabed.com/). Also, I have my publication at [medium blog.yaabed.com](https://medium.com/yazanaabed).

The main problem that existed was about 500 items thrown on the window object. This allows you to access them any place you need. It also makes the window the navigation tool for modules and components. The project becomes more coupled, and you don’t know who is using them.

Files are structured using the module architecture but without using `angular.module.` Files are divided into folder by name like HomePage. The HomePage folder contains its controller, style, and view.

The first thing that came to mind was refactoring the whole app to use webpack, modules, babel, and es6. After researching, it is possible to do this without any refactoring of the codebase. But, there are many problems to solve before I start adding webpack to the project.

### **Problems to consider before starting to work**

* How to solve the window object problem, because webpack shows files as a tree of files talking to each other.
* How to make fewer changes to the project without merging issues.
* How to split between development and production for the webpack.
* How to remove bower dependencies, because webpack mainly resolves modules from npm.
* How upgrades to webpack solve the big size of JavaScript files.

![Image](https://cdn-media-1.freecodecamp.org/images/1*8cR1c4pTuS145b7KhVrB-Q.jpeg)
_[https://www.pexels.com/photo/technology-computer-desktop-source-code-113850/](https://www.pexels.com/photo/technology-computer-desktop-source-code-113850/" rel="noopener" target="_blank" title=")_

### Start to break things into steps

#### Upgrade the node version from 0.10 to the latest version available

Before I started moving to using webpack, I needed to upgrade the Node version that webpack v3 works with. But, Grunt is using deprecated things — so when I updated the Node version, nothing worked! So I started to fix the errors one by one to make sure upgrading was possible.

First, an error accrued on old `grunt-sass` & `node-sass`. It’s not supported anymore for this version of Node. To fix this, I upgraded `grunt-sass` from ‘0.18.1’ to ‘2.0.0’, then upgraded `node-sass` to be ‘4.7.2’.

Secondly, trying to upgrade grunt from ‘0.4.5’ to ‘1.0.0’ didn’t work, because the grunt plugins need grunt@0.4.5 as peer dependency. So I stuck with 0.4.5 version.

#### Fixing errors shown on express node server

I had to fix errors with express Node server, because the bodyParser constructor is deprecated and needs to changed. I changed from

![Image](https://cdn-media-1.freecodecamp.org/images/1*zYHhQhSD4VfTrv8HWp7l4A.png)

to

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ty4Il11Y6pwJodIZcBfdYg.png)

#### Remove deprecated things

* Debug attribute from `grunt-express` because it is deprecated on the node-inspector new version.
* Remove the bower-install task from the project.

#### Start adding webpack

I added webpack to the project using `npm install webpack--save-dev`. Then I added the `webpack.config.json` file.

When I started this step, I got stuck because the project structure has no entry point. The whole project depends on one source which is the window. Webpack needs an entry point to start with and an output point to end with.

To solve this, I created an entry point. I set all the needed files on it and named it the same name on GruntJS config to concatenate it as the old Build did. But this was going to take a long time, because about 550 items were included in index.html.

To solve this problem, I used a RegExp `/”(.*?)"/ig` and replaced the values by `require(src)`to get the sources from the src attribute and convert it to `require(src).` I pasted it to the `entry.js` on the same order as the old index.html.

After this, the result was a significant JS file containing all scripts. But nothing worked! After investigating what was happening, it seemed that webpack was working by default as modules. If there are exports or export default on the same file, nothing will be exported to the outside even if you include it using require js.

Before searching for a way to solve this, I start adding module.exports to all files needing to be exported — before clearly understanding how webpack works! After two days of working, I found that there is something called loaders which solve the problem.

By adding this to `webpack.config.js`, all the files were now available as the old behavior!

![Image](https://cdn-media-1.freecodecamp.org/images/1*a1w_YDNzXTDVWfIzl5CN1g.png)

And everything was now working.

#### Next step

After I made the project works with Grunt, I needed to make sure both webpack and Grunt worked together. So I made tests to make sure I didn’t miss anything.

To make this happen, I create a new file called `inject-HTML.files.json.` This file contains all source files to use with `usemenPrepare` on Grunt and webpack to create the entries as multiple items as arrays taken from the inject-HTML files JSON.

![Image](https://cdn-media-1.freecodecamp.org/images/1*4CHmK7YvGR-5KdKkDb0shQ.jpeg)
_I love this image, write code and drink some coffee :) [https://www.pexels.com/photo/high-angle-view-of-coffee-cup-on-table-317385/](https://www.pexels.com/photo/high-angle-view-of-coffee-cup-on-table-317385/" rel="noopener" target="_blank" title=")_

#### Update the old Grunt config file

![Image](https://cdn-media-1.freecodecamp.org/images/1*_ACtb1LBsXQulfYWnZP17g.png)

#### Add files to concat

![Image](https://cdn-media-1.freecodecamp.org/images/1*2AX4IhZxSTV2sFxd2dn8qg.png)

#### Check if Webpack builds, then remove the JS from configurations

![Image](https://cdn-media-1.freecodecamp.org/images/1*YaLaQJvEGZf1-U09ii3t0g.png)

#### Add new npm script

![Image](https://cdn-media-1.freecodecamp.org/images/1*h72Fb0X9U7Fdt1d3NQ0z-Q.png)

#### Webpack.config.js file

![Image](https://cdn-media-1.freecodecamp.org/images/1*o7QEQxqK3HhR4_lMu0zvhA.png)

#### Webpack.prod.js file

![Image](https://cdn-media-1.freecodecamp.org/images/1*sZWLlMeMiXaXPdqmOYvXog.png)

### Motivations

#### Maintainability and Code Quality

* Solve the problem with creating files, as the project is growing fast.
* Solve the problem that there are too many things attached to the window without reason.
* Make the codebase easier to understand.

#### Development Efficiency

* Bower is now deprecated.
* Can’t use any things on npm packages, because the build process does not provide this.

#### Performance

* Files sizes are growing bigger every day, so need to introduce a solution to split the code.
* Being able to split files and defer loading until needed saves unnecessary transfer and parsing.

#### Code splitting

* After use, webpack Code splitting will be easier to use.
* Split new features into modules-based.

Finally, using the npm packages is a game changer. The goal was to make the codebase easy for other developers. Also, we proved that it’s possible to upgrade your system wisely even if your code base is terrible.

Rewriting the whole app is a disaster, because you are potentially wasting years of hard work. Instead, try to make your codebase more readable, maintainable, and modular. When the old code needs refactoring, you can do it step by step.

Don’t get stuck with your old codebase and say you can’t do anything to it. Try to make changes by yourself — live with new things, new updates, and new technologies that will make you happy.

This is my first time writing for people! If you liked this article, please share it with other people around you.

**_I am writing at [blog.yaabed.com](https://medium.com/yazanaabed). If you enjoyed this article please make sure to share it with other people. And don’t forget to hit the follow button for more articles like this, also [follow me on twitter](https://twitter.com/YazanAabed)._**

![Image](https://cdn-media-1.freecodecamp.org/images/1*MSPCzn3l6S8PfjbPj0m7jw.jpeg)

> Hi my name is [Yazan Aabed](https://www.yaabed.com/). Grown up in Palestine. My major was in computer science. I am a Frontend Engineer & JavaScript lover ??‍?. Mostly working with Frontend frameworks like (AngularJs, ReactJS). You can call me #Geek ?. Also, I Like to share my knowledge with other people and learn from them ???. You can find me on GitHub, [Mediu](https://github.com/YazanAabeed)m, [Twitt](https://medium.com/@yazanaabed)er[.](https://twitter.com/YazanAabed)

[**webpack learning academy**](https://webpack.academy/)  
[_webpack learning academy exists to provide curated, high-quality learning content, devoted to the webpack open source…_webpack.academy](https://webpack.academy/)[**From Grunt and Bower to Webpack, Babel and Yarn — Migrating a legacy front-end build system**](https://medium.com/appifycanada/migrate-to-webpack-from-grunt-bower-legacy-build-system-344526f47873)  
[_The build system that I had inherited for the International Cancer Genome Consortium’s Data Portal was fairly modern…_medium.com](https://medium.com/appifycanada/migrate-to-webpack-from-grunt-bower-legacy-build-system-344526f47873)[**How to Incrementally Switch to webpack**](https://medium.com/eventmobi/how-to-incrementally-switch-to-webpack-203a1b431f7a)  
[_This is the second of a two-part series on why and how we switched our JavaScript bundling system from an ad hoc system…_medium.com](https://medium.com/eventmobi/how-to-incrementally-switch-to-webpack-203a1b431f7a)[**Why We Switched to webpack**](https://medium.com/eventmobi/why-we-switched-to-webpack-69b7396f3ec5)  
[_This is the first of a two-part series on why and how we switched our JavaScript bundling system from an ad hoc system…_medium.com](https://medium.com/eventmobi/why-we-switched-to-webpack-69b7396f3ec5)[**The first steps from Grunt to Webpack**](https://advancedweb.hu/2016/02/02/the-first-steps-from-grunt-to-webpack/)  
[_Getting started with Webpack after using Grunt_advancedweb.hu](https://advancedweb.hu/2016/02/02/the-first-steps-from-grunt-to-webpack/)[**The Journey to Webpack - Server Density Blog**](https://blog.serverdensity.com/the-journey-to-webpack/)  
[_By Kerry Gallagher, of Server Density. Published on the 6th January, 2016. For the past couple of years we built the…_blog.serverdensity.com](https://blog.serverdensity.com/the-journey-to-webpack/)

> [[discussion] How did we go from Grunt to Gulp to Webpack?](https://www.reddit.com/r/javascript/comments/42z1xl/discussion_how_did_we_go_from_grunt_to_gulp_to/?ref_source=embed&ref=share) from       [javascript](https://www.reddit.com/r/javascript/)

