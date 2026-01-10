---
title: Super simple Gulp tutorial for beginners
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-08T10:17:27.000Z'
originalURL: https://freecodecamp.org/news/super-simple-gulp-tutorial-for-beginners-45141974bfe8
coverImage: https://cdn-media-1.freecodecamp.org/images/1*4oEHylwkvSTcgoxgygdbcg.png
tags:
- name: coding
  slug: coding
- name: Gulp
  slug: gulp
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Jessica Chan

  These days, using a build tool is an indispensable part of your web development
  workflow.

  Gulp is one of the most popular build tools these days — along with Webpack.

  But there’s a definite learning curve to learning Gulp. One of the ...'
---

By Jessica Chan

These days, using a build tool is an indispensable part of your web development workflow.

[Gulp](https://gulpjs.com/) is one of the most popular build tools these days — along with Webpack.

But there’s a definite learning curve to learning Gulp. One of the biggest hurdles is figuring out the seemingly hundreds of different parts that go into it.

And on top of that, you have to do everything on the command line, which can be incredibly intimidating if you haven’t worked much with it.

This tutorial will walk you through the basics of npm (Node Package Manager) and setting up Gulp for your front-end projects. Once you’re done, you’ll feel way more confident setting up your workflow and using the command line!

#### **So what’s the big deal with Gulp?**

Gulp is a huge time saver. By using Gulp, you can let your computer handle tedious tasks, such as:

* Compiling Sass files to CSS
* Concatenating (combining) multiple JavaScript files
* Minifying (compressing) your CSS and JavaScript files
* And automatically running the above tasks when a file change is detected

Gulp can do a lot more complex tasks than the ones I’ve mentioned above. However, this tutorial will be focused on just the basics of Gulp and how it works.

#### **Quick outline of what we’ll be doing**

Here are the steps this tutorial will be going through:

1. Install Node.js and npm to your computer
2. Install Gulp and other packages needed for your project
3. Configure your gulpfile.js file to run the tasks you want
4. Let your computer do your work for you!

Don’t worry if you don’t totally understand all the terms above. I’ll explain everything one step at a time.

Now let’s get started!

### Set up your environment

#### **Node.js**

In order to get Gulp up and running on your computer, you need to install Node.js onto your local environment.

Node.js is self-described as a “JavaScript runtime”, which is considered the back-end of JavaScript. Gulp runs using Node, so you understandably need to install Node before getting started.

You can download it from the [Node.js](https://nodejs.org/en/) website. When you install Node, it also installs npm onto your computer.

What’s npm, you ask?

#### **Npm (Node Package Manager)**

[Npm](https://www.npmjs.com/get-npm) is a continually updated collection of JavaScript plugins (called packages), written by developers around the world. Gulp is one of those plugins. You’ll also need a few more, which we’ll get into later.

The beauty of npm is that it allows you to install packages directly on your command line. This is great, because you don’t have to manually go to the website, download and execute the file to install.

Here’s the basic syntax to install a package:

`npm install [Package Name]`

**Note for Mac users:**  
 Depending on your setup, you may need to add the “sudo” keyword at the beginning to run this with root permissions.

So for Macs if would look like: `sudo npm install [Package Name]`

Seems pretty straightforward, right?

#### **The node_modules folder**

One thing to note: when you install an npm package, npm creates a folder called node_modules and stores all the package files there.

If you’ve ever had a project with a node_modules folder and dared to see what it contained, you probably saw that it had lots (and I mean LOTS) of nested folders and files.

Why does this happen?

Well, this is because npm packages tend to rely on other npm packages in order to run their specific function. These other packages are known as dependencies.

If you’re writing a plugin, it makes sense to take advantage of the functionalities of existing packages. No one wants to reinvent the wheel every time.

So when you install a plugin into your node_modules folder, that plugin will then install additional packages that **it** needs into its own node_modules folder.

And so on and so forth until you have nested folders out the wazoo.

You don’t need to worry too much about messing in the node_modules folder at this point — just wanted to briefly explain what’s going on in that crazy folder.

### Keeping track of packages with package.json

Another cool feature of npm is that it can remember what specific packages you’ve installed for your project.

This is important in case you have to reinstall everything for some reason.

Also it makes life easier for other developers, because they can quickly and easily install all the packages for your project on their computers.

How does it manage to do this?

Npm utilizes a file called package.json to keep track of what packages and what package versions you have installed. It also stores other information about the project, like its name, author, and Git repository.

#### **Creating your package.json**

To initialize this file, you can again use the command line.

First, navigate to your project folder, wherever you have it located on your computer.

Then type in the following command:  
`npm init`

Npm will then prompt you to enter in information about the project. For the majority of options, you can hit enter and use the default value that’s in parentheses.

When you’re done, npm will generate the package.json file in your project folder! If you open it up in your editor, you should see something like this:

```json
{
  "name": "super-simple-gulp-file",
  "version": "1.0.0",
  "description": "Super simple Gulp file",
  "main": "gulpfile.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/thecodercoder/Super-Simple-Gulp-File.git"
  },
  "keywords": [
    "gulp"
  ],
  "author": "Jessica @thecodercoder",
  "license": "ISC",
  "bugs": {
    "url": "https://github.com/thecodercoder/Super-Simple-Gulp-File/issues"
  },
  "homepage": "https://github.com/thecodercoder/Super-Simple-Gulp-File#readme"
}
```

Of course, for your project you’ll have your own name and information instead of what I have here.

At this point I wouldn’t worry about getting all the fields correct. This informational part is mainly used for packages that get published to npm as public plugins.

Now, what you **will** be putting into your package.json file is the list of all the packages that you need for running Gulp.

Let’s see just how you can add them in.

#### **Installing packages**

In the previous section above, we talked about typing: `npm install [Package Name]` into your command line to download and install the package into your node_modules folder.

It will install the package and automatically save it to your package.json file as a dependency.

**Note:** Prior to npm version 5.0.0, you had to add the flag “–save” in order for npm to add the package as a dependency. You no longer have to do that with versions 5 and up.

So if we want to install Gulp to our packages, we’d type in: `npm install gulp`.

It might take a minute or two for your computer to install everything related to Gulp. You will likely see some warning messages, but I wouldn’t worry about those unless the install fails.

Now, if you open your package.json file, you’ll see at the bottom that Gulp has been added as a dependency:

```
"dependencies": { "gulp": "^3.9.1" }
```

This list of dependencies will grow as you install additional npm packages.

#### **Other packages needed for Gulp**

Initially, we wanted to use Gulp to run tasks like compiling your SCSS/CSS and JavaScript files. To accomplish this, we’ll be using the following packages:

* [gulp-sass](https://www.npmjs.com/package/gulp-sass) — compiles your Sass files into CSS
* [gulp-cssnano](https://www.npmjs.com/package/gulp-cssnano) — minifies your CSS files
* [gulp-concat](https://www.npmjs.com/package/gulp-concat) — concatenates (combines) multiple JavaScript files into one large file
* [gulp-uglify](https://www.npmjs.com/package/gulp-uglify) — minifies your JavaScript files

Just like before, install each package by typing these lines one by one. You’ll have to wait a few seconds while each one installs before going on to the next line.

```
npm install gulp-sass 
npm install gulp-cssnano 
npm install gulp-concat 
npm install gulp-uglify
```

#### **Gulp-cli vs global Gulp**

In the past, to be able to run “gulp” from your command line, you would have to install Gulp globally on your local computer, using the command:  
   
`npm install –global gulp`

However, having a single global version of Gulp could cause issues if you have multiple projects all requiring different versions of Gulp.

The current consensus recommends installing a different package, [Gulp-cli](https://gulpjs.org/getting-started), globally instead of Gulp itself.

This will allow you to still run the “gulp” command, but you’re able to use different versions of Gulp across your different projects.

Here’s the code for that:

```
npm install --global gulp-cli
```

If you’re interested, you can read more context on this [Treehouse thread](https://teamtreehouse.com/community/gulp-global-install-gulp-vs-gulpcli).

All right, once all your packages are installed, you have all the tools you need. Let’s move on to setting up our project files!

### Set up your file structure

Before we start creating files and folders, just know that there are many different ways to set up your file structure. The approach that you’ll be using is good for basic projects, but the “right” setup will depend a lot on what your particular needs are.

This basic method will help you get a grasp on the basic functionality of all the moving parts. Then you can build off or change the setup to your own liking in the future!

Here’s what the project tree will look like:

**Root Project Folder**

* index.html
* gulpfile.js
* package.json
* node_modules (folder)
* app (folder)
* script.js
* style.scss
* dist (folder)

We already went over the package.json file and the node_modules folder. And the index.html file will be, of course, your main website file.

The gulpfile.js file is where we’ll configure Gulp to run all the tasks we talked about at the beginning of this article. We’ll get into that in a bit.

But right now I want to mention the two folders, app and dist, as they’re important for the Gulp workflow.

#### **App and dist folders**

In the app folder, we have your basic JavaScript file (script.js) and your basic SCSS file (style.scss). Those files are where you will write all your JavaScript and CSS code.

The dist folder exists only to store the final compiled JavaScript and CSS files after Gulp has processed them. You shouldn’t make any changes in the dist files, only the app files. But these files in dist are what will be loaded in index.html, since we want to use the compiled files in the website.

Again, there are lots of ways you can set up your project files and folders. The main important thing to keep in mind is that your structure makes sense and allows you to work the most efficiently.

Now let’s get to the meat of this tutorial: configuring Gulp!

### Create and configure your Gulpfile

The Gulpfile contains the code to load installed packages and run different functions. The code performs two basic functions:

1. Initialize your installed packages as Node modules.
2. Create and run Gulp tasks.

#### **Initialize packages**

In order to take advantage of all the features of the npm packages you added to your project, you need to export them as modules in Node — hence the folder name “node_modules”.

At the top of your Gulpfile, add the modules like this:

```javascript
var gulp = require('gulp'); 
var cssnano = require('gulp-cssnano'); 
var sass = require('gulp-sass'); 
var concat = require('gulp-concat'); 
var uglify = require('gulp-uglify');
```

Now that the packages are added, you can then use their functions and objects in your Gulpfile scripts. You’ll also be using some built-in functions that are part of Node.js.

If you want to read more about npm packages and Node modules, the npm site has a great explanation [here](https://docs.npmjs.com/getting-started/packages).

### **Create your Gulp tasks**

Creating a Gulp task is done by using the following code:

```javascript
gulp.task('[Function Name]', function(){    
   // Do stuff here 
}
```

This allows you to run the Gulp task by typing in `gulp [Function Name]` into the command line. This is important because you can then run that named function from other Gulp tasks.

Specifically, we are building several different Gulp tasks, which will **all** be run when you run the default Gulp task.

Some of the main functions that we’ll be using are:

* `.task()` — Creates a task, as mentioned above
* `.src()` — identifies what files you will be compiling in a particular task
* `.pipe()` — adds a function to the Node stream that Gulp is using; you can pipe multiple functions in the same task (read an excellent write-up on this topic on [florian.ec](https://florian.ec/articles/gulp-js-streams/))
* `.dest()` — writes the resulting file to a specific location
* `.watch()` — identifies the files to detect any changes

If you’re curious, you can read up more on the Gulp documentation [here](https://github.com/gulpjs/gulp/tree/v3.9.1/docs).

All set? Now let’s get down to business (cue Mulan music) and write those tasks!

These are the following tasks that we want Gulp to run:

* Sass task to compile SCSS to a CSS file and minify
* JavaScript task to concatenate the JavaScript files and minify/uglify
* Watch task to detect when SCSS or JavaScript files are changed, and re-run the tasks
* Default task to run all needed tasks when you type `gulp` into the command line

#### **Sass task**

For the Sass task, first we want to create the task in Gulp using `task()`, and we will name it “sass.”

Then we add in each component that the task will run. First we will designate that the source will be the app/scss/style.scss file, using `src()`. Then we will pipe in the additional functions.

The first one runs the `sass()` function — using the gulp-sass module which we called “sass” at the top of the Gulpfile. It will automatically save the CSS file with the same name as the SCSS file, so ours will be named style.css.

The second one minifies the CSS file with `cssnano()`. And the last puts the resulting CSS file in the dist/css folder.

Here’s the code for all that:

```javascript
gulp.task('sass', function(){    
    return gulp.src('app/style.scss')       
        .pipe(sass())       
        .pipe(cssnano())       
        .pipe(gulp.dest('dist/css')); 
});
```

To test, I just put in some filler SCSS in the style.scss file:

```css
div {    
    display: block; 
   	&.content {       
        position: relative;    
    } 
} 

.red { 
    color: red; 
}
```

You can run each individual Gulp task on the command line if you type `gulp` and the name of the task. So to test the Sass task, I typed in `gulp sass` to check if it works without errors, and generates the minified dist/style.css file.

If everything works correctly, you should see messaging like this in your command line:

```
[15:04:53] Starting 'sass'... [15:04:53] Finished 'sass' after 121 ms
```

Checking in the dist folder shows that there is indeed a style.css file, and opening it shows correctly-minified CSS:

```
div{display:block}div.content{position:relative}.red{color:red}
```

Ok, our Sass task is now done. On to JavaScript!

#### JS **task**

The JS Gulp task is similar to the Sass task, but has a few different elements.

First we’ll create the task and call it “js,” then we’ll identify the source files. In the `src()` function, you can identify multiple files a couple different ways.

One is to utilize the wildcard `(*)` to tell Gulp to use all files with the `*.js` extension like this:

```
gulp.src('app/*.js')
```

However this will compile the files in alphabetical order, which could potentially cause errors if you end up loading scripts that are dependent on other scripts before those other script files.

You can control the order by manually designating each JavaScript file if you don’t have too many script files.

The `src()` function can take an array of values as a parameter, by using the square brackets like this:

```
gulp.src(['app/script.js', 'app/script2.js'])
```

If you do have a lot of JavaScript files, you can make sure that you load dependencies first by keeping them in a separate sub-folder, like say “app/js/plugins”. Then keep other JavaScript files in the parent “app/js” folder.

Then you can use the wildcard notation to load all lib (library) scripts, followed by regular scripts:

```
gulp.src(['app/js/lib/*.js', 'app/js/script/*.js'])
```

Your approach will vary depending on the number and types of JavaScript files you have.

Once you’ve set your source files, you’ll pipe in the remaining functions. The first is to concatenate the files into one large JavaScript file. The `concat()` function requires one parameter with the name of the resulting file.

Then you’ll uglify the JavaScript file, and save it in the destination location.

Here’s the complete code for the JS task:

```javascript
gulp.task('js', function(){    
    return gulp.src(['app/js/plugins/*.js', 'app/js/*.js'])          
        .pipe(concat('all.js'))       
        .pipe(uglify())       
        .pipe(gulp.dest('dist')); 
});
```

Just like the Sass task, you can test that the JS task works by typing in `gulp js` into the command line.

```
[14:38:31] Starting 'js'... [14:38:31] Finished 'js' after 36 ms
```

Now that we’ve finished our main two worker Gulp tasks, we can move on to the Watch task.

#### **Watch task**

The Watch task will watch the files that you tell it to for any changes. Once it detects a change, it will run the tasks that you designate and then continue watching for changes.

We will create two watch functions, one to watch SCSS files and the other to watch JavaScript files.

The `watch()` function takes two parameters: the source location, and then the tasks to run when a change is detected.

The Sass Watch function will watch any SCSS files in the app folder and then run the Sass task if it detects changes.

The function will look like this:

```
gulp.watch('app/*.scss', ['sass']);
```

For the JS Watch function, we’ll have to take advantage of a really useful Node feature called “globbing.” Globbing refers to using the “**” symbols as a kind of wildcard for folders and subfolders. We need it for the JavaScript files, because we have a JavaScript file in the app/js folder, and a JavaScript file in the app/js/plugins folder.

And here’s what that function will look like:

```
gulp.watch('app/js/**/*.js', ['js']);
```

The way the glob (“**”) works is it will look for JavaScript files anywhere in the app/js folder. It will look either directly in the folder or in any subsequent child folders, like the plugins folder. Globbing comes in handy so that you don’t have to designate each sub-folder as a separate source in the `watch()` function.

Here’s the complete Watch task:

```javascript
gulp.task('watch', function(){       
	gulp.watch('app/*.scss', ['sass']);          
    gulp.watch('app/js/**/*.js', ['js']); 
});
```

Now we’re almost done! The last task to create is the default Gulp task.

#### **Default Gulp task**

The default Gulp task is what you want to run when you just type in `gulp` in the command line. When you create the task, you have to call it “default” in order for Gulp to recognize that that’s what you want to run.

What we’d like to do is run the Sass and JS tasks once, then run the Watch task to re-run tasks when files are changed.

```
gulp.task('default', ['sass', 'js', 'watch']);
```

You can create other tasks to run your builds, just don’t reuse the “default” name. For instance, let’s say you want to leave your CSS and JavaScript files unminified by default, but you do want to minify them for production.

You could create separate Gulp tasks to minify your CSS and JavaScript files called “minifyCSS” and “minifyJS.” Then you wouldn’t add those tasks to your default Gulp task, but you could create a new Gulp task called “prod” that has everything the default task has, and also has your minify tasks.

#### **References in your index.html**

Once you’ve gotten your Gulp process working, make sure that your index.html file references all the correct CSS and JavaScript files.

For the examples I’ve given you here, you’ll want to add a CSS reference to `dist/style.css` in your <head>:

```html
<link rel="stylesheet" href="dist/style.css">
```

And add a script tag referencing `dist/all.js` in your <body>:

```html
<script src="dist/all.js"><;/script>
```

### In closing

Congrats on making it through! I hope that you found this basic Gulp tutorial helpful.

Like I mentioned at the beginning, this is just a very simple tutorial of the basics of npm and Gulp.

Most devs add many additional tasks to their Gulpfile. Let me know if you’d be interested to see another article on those more advanced topics!

Lastly, you can check out all the code from this tutorial on my GitHub account [here](https://github.com/thecodercoder/Super-Simple-Gulp-File).

I hope you found this post helpful! Let me know any thoughts you have in the comments below.

#### Want more?

* Read more tutorials on my blog, c[oder-coder.com.](https://coder-coder.com)
* Si[gn up here to get emails about new articles.](https://coder-coder.com/subscribe)
* Join 25,000+ others — Follow @th[ecodercoder on Instagram.](https://www.instagram.com/thecodercoder/)
* Check out coding tutorials on [my YouTube channel](https://www.youtube.com/c/codercodertv).

_This post was originally published on [Coder-Coder.com](https://coder-coder.com/gulp-tutorial-beginners/)._

