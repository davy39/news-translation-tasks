---
title: How to minify your CSS with gulp
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-10T17:20:07.000Z'
originalURL: https://freecodecamp.org/news/how-to-minify-your-css-with-gulp-6ff3f4a896b5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*buKin7TOLVwnO4affvO8Qg.png
tags:
- name: CSS
  slug: css
- name: Front-end Development
  slug: front-end-development
- name: Gulp
  slug: gulp
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Vinicius Gularte

  In this article, I''m going to show a simple way to automatically minify your CSS
  files using gulp. ?

  To start — what is gulp?

  Gulp is a JavaScript task runner that lets you automate tasks such as…


  Bundling and minifying libraries...'
---

By Vinicius Gularte

In this article, I'm going to show a simple way to automatically minify your CSS files using gulp. ?

### **To start — what is gulp?**

Gulp is a JavaScript task runner that lets you automate tasks such as…

* Bundling and minifying libraries and stylesheets.
* Refreshing your browser when you save a file.
* Quickly running unit tests.
* Running code analysis.
* Less/Sass to CSS compilation.
* And much more!

The gulp workflow works as follows:

We can create tasks that we would like to fulfill. In these tasks we load files that we want gulp to work on (modifying or not), then we return them to some return folder.

It’s simple.

In this little tutorial, I will teach you how to create a task to minify all CSS files in your folder. Then put the minified ones in another folder.

### Let’s start

For this tutorial, make sure you have the latest version of the npm package installed on your machine. If you do not have it, you can download it [**here**](http://www.npmjs.com).

Once you have npm installed, in the base directory of your project we will install gulp using these commands:

`npm install gulp-cli -g`

`npm install gulp -D`

We will also use a gulp plugin to minify CSS called **gulp-clean-css**, so install it in the project type:

`npm install gulp-clean-css --save-dev`

Very good, now with the dependencies installed in the project, let’s create a file called **Gulpfile.js**. This file will be responsible for our tasks.

![Image](https://cdn-media-1.freecodecamp.org/images/1*RHjTJ_6QntCKKKnuZm_ndA.png)

We will create two folders in this repository too. One will be called styles where our style files will stay, and another called dist where the minified files will go.

In the end, our project will have this structure:

![Image](https://cdn-media-1.freecodecamp.org/images/1*dLew0FI0XbGbyxKuCIadGA.png)

### In Gulpfile.js

At the beginning of the file, we make the calls of the packages that we will use.

With the packages called, we will create the responsible task by minifying our files.

You might be wondering — you’re already able to minify your files? Yes, by executing the gulp command in the terminal followed by the task name.

But running this command all the time is a bit annoying, isn’t it? We can create a method for observing changes to files in the styles folder.

In this way, running the gulp command will wait for changes in the selected files to activate the minify-css task.

### Conclusion

This is just a small way that gulp can help us in the development of our applications.

You can find the code for this project in [this repository](https://github.com/ViniciusGularte/MinifiedCssGulp) on GitHub.

_Thank you for reading, please feel free to ? and help others find it._

_See you soon._ ?

### References

[**gulp.js**](https://gulpjs.com/)  
[_By preferring code over configuration, node best practices, and a minimal API surface - gulp makes things simple like…_gulpjs.com](https://gulpjs.com/)[**gulp-clean-css**](https://www.npmjs.com/package/gulp-clean-css)  
[_Minify css with clean-css._www.npmjs.com](https://www.npmjs.com/package/gulp-clean-css)

