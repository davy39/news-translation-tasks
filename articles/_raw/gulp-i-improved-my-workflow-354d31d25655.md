---
title: Gulp! I Improved my Workflow!
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2015-10-17T22:33:35.000Z'
originalURL: https://freecodecamp.org/news/gulp-i-improved-my-workflow-354d31d25655
coverImage: https://cdn-media-1.freecodecamp.org/images/1*3vp5N6O1BBr79sdNtU6cQg.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: Gulp
  slug: gulp
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'By Stefano Grassi

  yet another hands-on experience with Gulp.js


  _Jökulsárlón, Iceland by [Jeremy Goldberg](https://unsplash.com/jeremy" rel="noopener"
  target="blank" title=")

  Unless you’ve been living under a rock for the past few years, the number o...'
---

By Stefano Grassi

#### yet another hands-on experience with Gulp.js

![Image](https://cdn-media-1.freecodecamp.org/images/1*3vp5N6O1BBr79sdNtU6cQg.jpeg)
_Jökulsárlón, Iceland by [Jeremy Goldberg](https://unsplash.com/jeremy" rel="noopener" target="_blank" title=")_

Unless you’ve been living under a rock for the past few years, the number of tools at the disposal of front-end developers have grown rapidly. What we have now is a wide range of projects dedicated to speed-up, automate and increase the quality of our workflow.

For example, just imagine:

* compiling [SASS](https://www.npmjs.com/package/gulp-sass)/[LESS](https://www.npmjs.com/package/gulp-less)/[PostCSS](https://www.npmjs.com/package/postcss)/[Stylus](https://www.npmjs.com/package/gulp-stylus) to a minified CSS, [tailored](https://www.npmjs.com/package/gulp-uncss) to your needs, [auto-prefixed](https://www.npmjs.com/package/gulp-autoprefixer) and in real-time
* [concatenating](https://www.npmjs.com/package/gulp-concat) and [minifying](https://www.npmjs.com/package/gulp-uglify) your scripts
* compressing html files created from [templates](https://www.npmjs.com/package/gulp-file-include) and atomic modules
* [preview](http://www.browsersync.io/) your webapp from a virtual server during the compilation, auto-refreshed and synced to all your devices
* test your web [performance](https://www.npmjs.com/package/gulp-sitespeedio)
* self-updating style-[guide](https://trulia.github.io/hologram/) of the project
* [compressing](https://www.npmjs.com/package/gulp-imagemin) images and creating [sprites](https://www.npmjs.com/package/gulp.spritesmith)

Some years ago this sounded more like a Disneyan dream but we’re living in the future, so fear not! [Grunt](http://gruntjs.com/), [Mimosa](http://mimosa.io/), [Broccoli](http://broccolijs.com/) and [Gulp](http://gulpjs.com/) to the rescue!

Each system has its own strong points. I’ve chosen Gulp for my needs but make sure to check them all out before deciding which best suits you.

#### So… gulp? What’s that?

[**gulpjs/gulp**](https://github.com/gulpjs/gulp/blob/master/docs/getting-started.md)  
[_gulp — The streaming build system_github.com](https://github.com/gulpjs/gulp/blob/master/docs/getting-started.md)

As its site states, Gulp is a “[streaming build system](http://gulpjs.com/)” which means that you can set your own tasks to be run on a pipeline, monitor a folder for a change and re-run.

And it’s **super simple**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*_PQJkvbZJNE_BjXpvIGCPQ.jpeg)
_That’s ingenious, if I understand it correctly.<br>It’s a Swiss watch.<br>Yeah, the beauty of this is its simplicity._

#### Gulp Basic Concepts

Let’s sip through the main elements

**gulp.task**  
aka the action you want to achieve. Managing CSS? Generating the docs?  
Gulp define them with [orchestrator](https://github.com/robrich/orchestrator), a module that allows us to define dependencies and maximum concurrency

```
gulp.task(‘somename’, function() { // Do stuff});
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*MRor084bOQstofwPYVjaFQ.jpeg)

**gulp.watch**  
aka the folders you want to keep checked for changes

```
gulp.watch(‘folder/*.ext’, [‘firstTask’, ‘secondTask’]);
```

Every **stream** originates from a source(s) matching a specific **glob** (a pattern that a file needs to match)

```
gulp.src(globs[, options])
```

a series of **pipes** (actions)

```
.pipe(concat()),.pipe(minify())
```

and a **destination** defined with

```
gulp.dest(path[, options])
```

To operate, gulp needs two core files, **package.json** and **gulpfile.js.**  
_(For the installation of gulp, follow the official docs)_

#### Gulpfile.js

In the **gulpfile** we’ll declare which plugins are we going to use, the tasks we want to run, which folders we’re going to watch, etc…

#### Package.json

The **package.json** file is used to store all the information regarding the dependencies of the project (gulp included!).

![Image](https://cdn-media-1.freecodecamp.org/images/1*p1_LFP4jZEH6b9asHPueyg.jpeg)

* To **create** it

```
$ npm init
```

You’ll be prompted to enter some basic info for the heading of the file, like the author name, the project name and so on.

* To **install** a plugin and save the dependency on the json file

```
$ npm install --save-dev yourPluginName
```

* To **uninstall** a plugin and remove the dependency on the json file

```
$ npm uninstall --save-dev yourPluginName
```

* If you need to **install all the dependencies** from a compiled package.json

```
$ npm install
```

#### Project Organization

This is my approach to organize the folder of a project managed with Gulp

#### Plugins FTW!

Gulp has an impressing list of plugins (**1895** at the time I’m writing this article)

[**gulp.js plugin registry**](http://gulpjs.com/plugins/)  
[_Discover gulp.js plugins_gulpjs.com](http://gulpjs.com/plugins/)

**Must Have**

* [gulp-load-plugins](https://github.com/jackfranklin/gulp-load-plugins)  
This lazy-loads the plugins installed in your project. You assign a variable to it, and use it to reference other plugins instead of repeating the requirement declaration for every other plugin.

```
var $ = require('gulp-load-plugins')();
```

```
// Example for gulp-concat.pipe($.concat('main.js'))
```

* [browsersync](http://www.browsersync.io/docs/gulp/)  
page refresh at any change on every device connected to the same URL (localhost or LAN)
* [sitespeed](https://www.sitespeed.io)  
my favourite tool for performance testing
* [uncss](https://github.com/giakki/uncss)  
are you using a CSS framework like Bootstrap for a landing page?  
You NEED this.

#### What? How do I update Gulp plugins, you ask?

```
$ npm install -g npm-check-updates
```

```
$ npm-check-updates -u
```

```
$ rm -fr node_modules
```

```
$ npm install
```

> Basically this installs **npm-check-updates** globally, runs it against your package.json and updates the dependency versions.  
> Then you just delete the node modules folder and re-install.

> from: [https://stackoverflow.com/questions/27024431/updating-gulp-plugins](https://stackoverflow.com/questions/27024431/updating-gulp-plugins)

Note: As a general rule, and as a last resort, we better **clean** the npm cache with

```
$ npm cache clean
```

#### _That’s all, folks! Thank you for reaching this point!_

#### _I hope that I kept you interested enough to check some of the links that stuffed this article. They’re there because I wanted to show my support for all the great work that fellow developers are doing for the community._

