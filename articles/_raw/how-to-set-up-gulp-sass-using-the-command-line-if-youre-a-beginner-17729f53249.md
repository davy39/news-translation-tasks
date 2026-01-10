---
title: How to set up Gulp-sass using the command line if you’re a beginner
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-30T17:23:30.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-gulp-sass-using-the-command-line-if-youre-a-beginner-17729f53249
coverImage: https://cdn-media-1.freecodecamp.org/images/1*4Ua25jOkgtszd4brxFG0pQ.png
tags:
- name: coding
  slug: coding
- name: CSS
  slug: css
- name: Gulp
  slug: gulp
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Simeon Bello

  I intern at a tech firm presently, and few days ago I got a challenge from my boss
  about writing an article. So I decided to write something on Gulp-sass.Setting it
  up can be frustrating sometimes, especially when you are new to it. I...'
---

By Simeon Bello

I intern at a tech firm presently, and few days ago I got a challenge from my boss about writing an article. So I decided to write something on Gulp-sass.   
Setting it up can be frustrating sometimes, especially when you are new to it. I use Windows, and searching for an article that would solve my problem was like getting Jack in Black-ish to spell “decrease”.

Ok I think I got a little bit carried away there…enough about me, let’s get started!

P.S. this is my first published article and I hope you love it. :)

### Installing node

First, open the command line and install [node.js](https://nodejs.org) on your computer. It comes with a Node Package Manager(npm) which you can use to install Gulp. After installing, you can install Gulp by running `npm install gulp -g`. The `**-g**` instructs **npm** to install Gulp globally on your computer (this means that you can use gulp commands anywhere on your computer.)

Before I continue, I am assuming you are familiar with the command line!

Navigate to your project directory and run `npm init`. This will create a package.json file, press enter and it will add what you need into  
the package.json file.

Yeah, you may be wondering what a package.json file is right?  
A [package.json file](https://docs.nodejitsu.com/articles/getting-started/npm/what-is-the-file-package-json/) holds various metadata relevant to your project. This file gives information to npm and allows it to identify the project as well as handle the project’s dependencies. It also makes it easier to install all the tasks that are used in a Gulp project.

If you still don’t get it, you probably need Diane to explain it better — what is my problem/obsession with Black-ish??

After running `npm-init`, type `npm install gulp --save-dev`**,** this instructs **npm** to install Gulp into your project. By using `--save-dev` we store Gulp as a dev dependency in the package.json.

### Creating a Gulpfile

Now that you’ve installed Gulp, you’re ready to install the first task. You have to `require` Gulp. Create a new file called gulpfile.js in your project directory — You can do this by using any text editor. Start by adding the code below to your gulpfile.

```
‘use strict’;
```

```
var gulp = require(‘gulp’);
```

### Setting up a task

Now you can install a **gulp task —** in this case we would install Gulp-sass. This task makes it possible to convert _Sass to CSS_. Still using the command line, you can install Gulp-sass by running `**npm** install gulp-sass --save-dev`. After that, require Gulp-sass in your gulpfile.js.

Put `var sass = require(‘gulp-sass’);`under the line you required gulp.

### Structuring your project

Before you use the lines below, I am also assuming you know how to structure a web app. Here I am going to use the structure of common web apps.

![Image](https://cdn-media-1.freecodecamp.org/images/Qe0oi9tR9oQ1WTgIJxWTV0VTBnZEHAkHEE2s)

### Compiling sass/scss

The last thing then is to instruct gulp what files it needs to convert and where the destination should be — where the output file will be stored.

Use the following;

```
//compile gulp.task(‘sass’, function () { gulp.src(‘app/scss/app.scss’) .pipe(sass().on(‘error’, sass.logError)) .pipe(gulp.dest(‘app/css’)); });
```

The file in **gulp.src** will be converted, you can also select all .scss files in a directory by using `“app/scss/*.scss”`. This will select all your .scss files in the folder scss.

The **gulp.dest** is the output. The output will be stored in the CSS folder inside the app folder.

### Gulp-watch-sass

Gulp has a watch syntax which allows it to monitor source files and then “watch” for changes made to your code. Just add the syntax to your gulpfile.js by typing:

```
//compile and watch gulp.task(‘sass:watch’, function() { gulp.watch(‘app/scss/app.scss’, [‘sass’]);});
```

That’s pretty much everything you have to do! It wasn’t that stressful, or was it?

Thanks for reading!

