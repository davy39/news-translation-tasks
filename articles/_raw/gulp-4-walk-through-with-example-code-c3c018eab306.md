---
title: Using Gulp 4 in your workflow for Sass and JS files
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-26T03:27:19.000Z'
originalURL: https://freecodecamp.org/news/gulp-4-walk-through-with-example-code-c3c018eab306
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/Gulp-4-workflow-walkthrough.png
tags:
- name: Gulp
  slug: gulp
- name: learning to code
  slug: learning-to-code
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Jessica Chan

  This post was originally published on Coder-Coder.com.


  This tutorial will explain, step by step, how to set up Gulp 4 in your workflow,
  as well as how to migrate from Gulp 3 to Gulp 4 syntax.


  Need to just quickly get your Gulp 3 gul...'
---

By Jessica Chan

<p><em>This post was originally published on <a href="https://coder-coder.com/gulp-4-walk-through/">Coder-Coder.com</a>.</em></p>

This tutorial will explain, step by step, how to set up Gulp 4 in your workflow, as well as how to migrate from Gulp 3 to Gulp 4 syntax.

> _Need to just quickly get your Gulp 3 gulpfile.js working with Gulp 4? [Click here](#migrating) to go right to that part of the post._

1. Install the gulp-cli on your command line by running `npm install gulp-cli -g`.
2. Install Gulp by running `npm install gulp`.
3. Install other npm packages for your Gulp workflow.
4. Create a `gulpfile.js` file in your project root.
5. Import your npm packages as modules in your gulpfile.
6. Add your tasks to the gulpfile to compile your SCSS/JS files and run a watch task.
7. Run the `gulp` command to run all your tasks.

### What is Gulp and what does it do?

Gulp is a tool that will run various tasks for you in your web development workflow. It might be called a bundler, build tool, or a task runner. They all mean roughly the same thing.

Similar tools are Webpack and Grunt (although Grunt is quickly becoming obsolete).

Here’s what we’re going to have Gulp do for us:

1. Compile our Sass files to CSS
2. Add vendor prefixes to our CSS
3. Minify our final CSS file
4. Concatenate (i.e. combine) our JS files
5. Uglify our final JS file
6. Move the final CSS/JS files into our `/dist` folder.

Pretty cool, right?!

So the way it works is, all your settings and tasks are stored in a `gulpfile.js` file. And you run Gulp on your command line.

The great part about that is that once you have your gulpfile all set up, you can easily reuse it for other projects. So it’s a huge time-saver!

Let’s move on to installing and setting up Gulp on your computer.

### Installing Gulp, using a working demo project

Before you can run Gulp, you will need to install a couple of things:

* Install [Node.js](https://nodejs.org/en/) if you don’t have it yet.
* Install the [Gulp Command Line Utility](https://www.npmjs.com/package/gulp-cli) by running `npm install --global gulp-cli`.

Once you have Gulp working, check out a demo project I built that uses Gulp! It’s a front-end boilerplate project that’s meant to be a quick way for me to get started with any simple front-end website.

(I also have plenty of code snippets in the rest of this tutorial, so you can just refer to those as well!)

**To set the front-end boilerplate project up:**

* Clone or download the [Git repo](https://github.com/thecodercoder/frontend-boilerplate) of this project onto your computer.
* Open the project, and in the root project folder, go to your command line and run `npm install`. This will install the npm packages listed in the `package.json` file, particularly Gulp 4.

You should now have the project files set up, and all the npm packages installed that we’ll be using to run Gulp tasks.

Since the files from the repo are ready to go, if you type in `gulp` in the command line, you should see an output like this:

```
> gulp [22:29:48] Using gulpfile ~\Documents\GitHub\frontend-boilerplate\gulpfile.js [22:29:48] Starting 'default'... [22:29:48] Starting 'scssTask'... [22:29:48] Starting 'jsTask'... [22:29:48] Finished 'jsTask' after 340 ms [22:29:48] Finished 'scssTask' after 347 ms [22:29:48] Starting 'watchTask'...
```

And you’ve run Gulp!

### What’s happening in the project when you run Gulp?

All right, you have the project successfully working! Now let’s get into more detail on what’s in the project and how it works.

First, here’s a quick rundown of the file structure of our project:

* **index.html** — your main HTML file
* **package.json** — contains all the npm packages to install when you run `npm install`.
* **gulpfile.js** — contains the config and runs all the Gulp tasks
* **/app** — working folder, you will edit SCSS/JS files in here
* **/dist** — Gulp will output files here, don’t edit these files

In your workflow, you will edit the HTML, SCSS, and JS files. Gulp will then detect any changes and compile everything. Then you will load your final CSS/JS files from the `/dist` folder in your `index.html` file.

Now that we have Gulp running, let’s take a closer look at how Gulp works.

### What exactly is in the gulpfile.js?

Here’s an in-depth explanation of each section of the gulpfile, and what they do:

#### Step 1: Initialize npm modules

At the very top of the `gulpfile.js`, we have a whole bunch of constants that import the npm packages we installed earlier, using the `require()` function.

Here’s what our packages do:

Gulp package:

* `gulp` — runs everything in the gulpfile.js. We’re exporting just the specific gulp functions that we will be using, like `src`, `dest`, `watch`, and others. This allows us to call those functions directly without the `gulp`, for example we can just type in `src()` instead of `gulp.src()`.

CSS packages:

* `gulp-sourcemaps` — maps the CSS styles back to the original SCSS file in your browser dev tools
* `gulp-sass` — compiles SCSS to CSS
* `gulp-postcss` — runs autoprefixer and cssnano (see below)
* `autoprefixer` — adds vendor prefixes to CSS
* `cssnano` — minifies CSS

> _If you’ve used Gulp before, you might be wondering why I’m using straight-up `autoprefixer` and `cssnano`, instead of `gulp-autoprefixer` and `gulp-cssnano`. For some reason, using them will work, but will prevent sourcemaps from working. Read more about that issue [here](https://github.com/gulp-sourcemaps/gulp-sourcemaps/issues/60)._

JS packages:

* `gulp-concat` — concatenates multiple JS files into one file
* `gulp-uglify` — minifies JS

Now that we have our modules added, let’s put them to work!

#### Step 2: Use the modules to run your tasks

A “task” in Gulp is basically a function that performs a specific purpose.

We’re creating a few utility tasks to compile our SCSS and JS files, and also to watch those files for any changes. Then those utility tasks will be run in our default Gulp task when we type `gulp`on the command line.

#### **Creating constants for file paths**

Before writing our tasks, though, we have a few lines of code that save our file paths as constants. This is optional, but I like using path variables so that we don’t have to manually retype them each time:

This code creates `scssPath` and `jsPath` constants that we will use to tell Gulp where files are found.

#### **Sass task**

Here’s the code for our Sass task:

```
function scssTask(){        return src(files.scssPath)        .pipe(sourcemaps.init())        .pipe(sass())        .pipe(postcss([ autoprefixer(), cssnano() ]))        .pipe(sourcemaps.write('.'))        .pipe(dest('dist')    );}
```

Our Sass task, called `scssTask()`, is doing several things. In Gulp, you can chain multiple functions by using the Gulp function `pipe()` after the first function.

In our task, Gulp is first running `src()` to load the source directory of the SCSS files. It’s using the constant we created earlier, `files.scssPath`.

Then after `src()` we’re piping everything else into the build process. You can think about it like adding more and more sections of pipe onto an existing pipe.

The functions it’s running are:

* `sourcemaps.init()` — sourcemaps needs to be added first after `src()`
* `sass()` does the compiling of all the SCSS files to one CSS file
* `postcss()` runs two other plugins:
* - `autoprefixer()` to add vendor prefixes to the CSS
* - `cssnano()` to minify the CSS file
* `sourcemaps.write()` creates the sourcemaps file in the same directory.
* `dest()` tells Gulp to put the final CSS file and CSS sourcemaps file in the `/dist` folder.

#### **JS task**

Here’s the code for our JavaScript task:

```
function jsTask(){    return src([files.jsPath])        .pipe(concat('all.js'))        .pipe(uglify())        .pipe(dest('dist')    );}
```

Our JavaScript task, called `jsTask()`, is also running multiple functions:

* `src()` to load the JS files from `files.jsPath`.
* `concat()` to concatenate all the JS files into one JS file.
* `uglify()` to uglify/minify the JS file.
* `dest()` to move the final JS file into the `/dist` folder.

#### **Watch task**

The `watch()` function is a super handy part of Gulp. When you run it, it will run continuously, waiting to detect any changes to the files you tell it to watch. When it detects changes, it will run any number of tasks you tell it to.

This is great because then you don’t have to keep manually running `gulp` after every code change.

Here’s the code for our watch task:

```
function watchTask(){    watch(        [files.scssPath, files.jsPath],        parallel(scssTask, jsTask)    );}
```

The `watch()` function takes three parameters, but we’re just using two:

* globs, meaning the file path strings,
* options (not used), and
* tasks, meaning which tasks we want to run.

What we’re having our watch task do is watch the files in our `scssPath` and `jsPath` directories. Then if any changes are made in either, run the `scssTask` and `jsTask` tasks simultaneously.

Now that we’ve gotten our utility tasks set up, we need to set up our main Gulp task.

#### **Default task**

This is the main Gulp task, which will automatically run if you type in `gulp` on the command line.

```
exports.default = series( parallel(scssTask, jsTask), watchTask);
```

Gulp will automatically search for a `default` task in your `gulpfile.js` when you use the `gulp`command. So you must export the default task in order for it to work.

Our default task will do the following:

* Run the `scssTask` and `jsTask` simultaneously using `parallel()`
* Then run the `watchTask`

You’ll also notice that we are putting all those tasks inside the `series()` function.

**This is one of the major new changes in Gulp 4 for how it handles tasks– you are required to wrap all tasks (even single ones) either in `series()` or `parallel()`.**

### A note on registering tasks: what’s changed in Gulp 4

If you’ve been using the `tasks()` function to run everything, you may have noticed that there’s a difference now.

Instead of using `gulp.task()` to contain all your task functions, we’re creating actual functions like `scssTask()` and `watchTask()`.

This is to follow Gulp’s official guidelines for creating tasks.

The Gulp team recommends using `exports` rather than `tasks()`:

> _“In the past, `task()` was used to register your functions as tasks. While that API is still available, exporting should be the primary registration mechanism, except in edge cases where exports won’t work.” [[Gulp Documentation](https://gulpjs.com/docs/en/getting-started/creating-tasks)]_

So, while they still let you use the `task()` function, it’s more current to create JS functions for each task and then export them.

<a name="migrating"></a>

If you can, I’d recommend updating your syntax to reflect this, as it’s possible that Gulp will deprecate `task()` at some point.

### Problems Migrating from Gulp 3?

If you’ve been using Gulp 3 and all you want is to get the dang thing working with Gulp 4, you’re in luck!

Before, in Gulp 3, you could simply list a single function or multiple functions in an array. However, in Gulp 4, doing so without wrapping them in either `series()` or `parallel()` will throw an error now.

Something like:

`AssertionError [ERR_ASSERTION]: Task function must be specified`

Gulp 4 introduces two new functions to run tasks: `series()` and `parallel()`. It gives you the option of running multiple tasks concurrently, or one after the other.

So to quickly fix the error, put all your tasks into either a `series()` or `parallel()`function.

**Tasks in (old) Gulp 3 syntax**

In Gulp 3, you might have run tasks this way:

`gulp.task('default', ['sass', 'js', 'watch']);`

`gulp.watch('app/scss/*.scss', ['sass']);`

**Tasks in Gulp 4 syntax**

Put those tasks into a series() function like this:

`gulp.task('default', gulp.series('sass', 'js', 'watch'));`

`gulp.watch('app/scss/*.scss', gulp.series('sass'));`

And that will fix the task function error with the smallest change possible! ?

### **Project files download**

All the code I’ve displayed here is from a GitHub repository I have for front-end boilerplate. It’s meant as a quick starter kit for any simple front-end website project.

You’re welcome to check it out, customize, and use it for your own projects!

[Check out the GitHub repository here.](https://github.com/thecodercoder/frontend-boilerplate)

### **In closing**

I hope that you’ve found this walk-through of how to get Gulp 4 running helpful!

If you enjoyed this post or have a question, feel free to leave a comment below! ?

**Want more?**

? Read more tutorials on my blog, c[oder-coder.com.](https://coder-coder.com)  
? S[ign up here to get emails about new articles.](https://coder-coder.com/subscribe)  
? Join 24,000+ others — Follow @[thecodercoder on Instagram.](https://www.instagram.com/thecodercoder/)  
? Check out coding tutorials on [my YouTube channel](https://www.youtube.com/c/codercodertv).

