---
title: How to minify images with Gulp & gulp-imagemin and boost your site’s performance
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-06T19:47:30.000Z'
originalURL: https://freecodecamp.org/news/how-to-minify-images-with-gulp-gulp-imagemin-and-boost-your-sites-performance-6c226046e08e
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca58e740569d1a4ca6a30.jpg
tags:
- name: Gulp
  slug: gulp
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: UX
  slug: ux
seo_title: null
seo_desc: 'By Jonathan Sexton

  Images are everywhere across the internet. You would be hard pressed to find a single
  page or application that doesn’t contain at least one image in some form or another.
  Images are great way to help tell stories and emphasize crit...'
---

By Jonathan Sexton

Images are everywhere across the internet. You would be hard pressed to find a single page or application that doesn’t contain at least one image in some form or another. Images are great way to help tell stories and emphasize critical parts of our lives.

But if you’re like me you know that having a large image can seriously impact the performance of your site/app. So today, I’m going to teach you how to use Gulp and an `npm` package called `gulp-imagemin` to reduce the size of your images on the fly.

If you don’t know what all of these words mean, fear not! I have some relevant and important links/descriptions below to help bring you up to speed.

* [Minification](https://en.wikipedia.org/wiki/Minification_(programming)), or minifying as I like to call it, is the act or process of removing unnecessary parts of source code to reduce size.
* `Gulp` is a JavaScript build tool that allows you to automate parts of your workflow to streamline your process. It takes care of some not so interesting, but important, aspects of your workflow (like reducing image size) so that you can focus on the building. You can [find Gulp here](https://gulpjs.com/).
* To make use of `npm` we'll need to install `Node.js` which is, in a nutshell, the framework that allows developers to use JavaScript code in a server (back end) environment. You can [find Node here](https://nodejs.org/en/download/).
* `npm` (Node Package Manager) is and does what its name implies. It is a package manager for JavaScript and "the world's largest software registry". Just think of `npm` as a giant storage area for awesome packages/utilities to help developers. You can [find npm here](https://www.npmjs.com/).
* `gulp-imagemin` is one of those awesome packages I mentioned earlier. Using this package we'll be able to automatically reduce the size of our images every time a save occurs. You can [find gulp-imagemin here](https://www.npmjs.com/package/gulp-imagemin).

Alright, now that explanations are out of the way let’s get to the fun parts :D

### Project File Structure

Start by opening up your text editor of choice and creating a directory for your project or if you have an existing directory navigate to that directory in your terminal and skip down to the **Installing Node & npm Section**.

If you’re using [VS Code](https://code.visualstudio.com/) you can find the [built in terminal](https://code.visualstudio.com/docs/editor/integrated-terminal) by hitting `ctrl + ` (tilde)`.

Here’s how my project structure looks in my terminal:

![Image](https://cdn-media-1.freecodecamp.org/images/SFUA0D00x1r1kSEyEAha4U0uoXy5zUVKElHf)

And here’s how my project file structure looks in the explorer inside VS Code:

![Image](https://cdn-media-1.freecodecamp.org/images/8GrSHZyzovwyyYWmHSBRWhR0CBVrZPKQfUsX)

As you can see I have a separate directory for my base files and the minified files. Once you have your project directory established it’s time to start installing everything we’ll need.

### Installing Node & npm

Alright, now that our directory is up and running let’s start installing our dependencies. If you already have `Node & npm` installed, feel free to skip down to the **Installing Gulp & gulp-imagemin Section**.

1. First, enter `node --v` within your terminal to check and see if you have the Node installed. If you do, you'll get something back like `v8.9.3`
2. If you get nothing back or an error, simply download and [install Node from here](https://nodejs.org/en/download/). It could take a few minutes so +be patient.
3. Once `Node.js` is installed, you'll have `npm` installed as well because it comes bundled with `Node`. You can check the version of `npm` by typing `npm -v` in your terminal. You should get something like `6.4.1`back.
4. Next we need to create a `package.json` file for our project. We do this by using the command `npm init` (find out more about `[package.json](https://docs.nodejitsu.com/articles/getting-started/npm/what-is-the-file-package-json/)` [here](https://docs.nodejitsu.com/articles/getting-started/npm/what-is-the-file-package-json/)). You'll be asked a series of questions but if you don't want to answer them you don't have to, just hit enter until you see `Is this OK? (yes)`, then hit `Enter` one last time and you'll be finished with this section.

![Image](https://cdn-media-1.freecodecamp.org/images/ra8Rx3jITz4p8TiUA32gdv9o0PmTqoLvrYd5)

You’ll notice that this file was created in a different directory than the one I started with. This is so I can provide an example, as I have previously installed all of this in my current project directory.

### Installing Gulp & gulp-imagemin

Once `Node & npm` have been installed, we can now install `Gulp & gulp-imagemin` by following these steps:

1. First, type `npm install --save-dev gulp` in your terminal. If you want to know what the `--save-dev` flag does, check out this [Stack Overflow post](https://stackoverflow.com/questions/19223051/what-does-save-dev-mean-in-npm-install-grunt-save-dev).
2. Again, be patient as installing Gulp might take a minute but you’ll eventually end up with something like this: `gulp@4.0.0 added 318 packages from 218 contributors and audited 6376 packages in 49.362s found 0 vulnerabilities`
3. You can check your Gulp version by typing `gulp -v` in your terminal and you'll get something similar to this: `[13:06:56] CLI version 2.0.1 [13:06:56] Local version 4.0.0`
4. Now let’s install `gulp-imagemin` by typing `npm install --save-dev gulp-imagemin` and again you'll get something like this back: `gulp-imagemin@5.0.3 added 232 packages from 97 contributors and audited 10669 packages in 39.103s found 0 vulnerabilities`
5. And the final step for this section is to create our `gulpfile.js` **It is very important that your file has this exact name and is in the outer most level of your project folder structure!**

### Writing the Code — Finally the Fun!

Ok, now that we’ve taken care of installing everything in the correct place, let’s open up our `gulpfile.js` and write the actual code that will do all of the hard work.

1. Start by requiring `gulp` --&g`t; const gulp = require('gulp`');We're basically taking advantage of Node's module system to use code that is located in different files
2. Now require `gulp-imagemin` --&g`t; const imagemin = require('gulp-imagemin`'); Again we're taking advantage of the module system to use this code in our project
3. Now, we need to write the function that will do all of the image squashing:   
`function imgSquash() {`  
 **return** gulp **.**src("./img/*")  
 **.**pipe(imagemin())   
 **.**pipe(gulp**.**dest("./minified/images"));  
`}`
4. If you set your directory up following mine, the code above will work. If your directory looks different you will need to change the `.src & .dest` lines to match where your files are located and where you want them piped to after they've been minified.
5. `Gulp` operates based off of tasks and we can give it plenty of those to keep it busy. Once we've defined the actual function to do the heavy lifting, we need to tell `Gulp` what to do with that function: `gulp.task("imgSquash", imgSquash);`
6. Now, we want `Gulp` to watch our given directory for changes (new images) and when it detects those, we want it to automatically run our `imgSquash` function, minify our images, and pipe them to the destination we set. We achieve that by defining another task to watch the directory:   
`gulp**.**task("watch", () **=&**gt; {`   
 `g**u**lp.watch("./img/*", imgSquash);`  
});
7. The last step to writing the code is defining the last task to call our `imgSquash` and `watch` tasks in succession: `gulp**.**task("default",gulp**.**series("imgSquash","watch"));` Here the word "default" refers to the word `gulp` in the terminal and the `gulp.series` will ensure that the `imgSquash` function runs and immediately after Gulp will watch the directory for changes.

Here is what our finished file should look like:

![Image](https://cdn-media-1.freecodecamp.org/images/PGzForat5pR93lI2H5W4hSfBJcPFojPVcoJ6)

Save this file, open your terminal, and type `gulp` and hit enter. You should see something like this:

![Image](https://cdn-media-1.freecodecamp.org/images/tSVYnl8tIMN0VIy8KoZbE81GXwtdPAIDl4Wi)

As you can see, each time a new file was added to the base directory, our tasks kicked in because Gulp was watching and immediately ran our `imgSquash` function to minify our images. When you're finished using Gulp you can hit `ctrl + c` in your terminal to terminate the watch process.

Now you can start using your minified images on your website/app and enjoy that new found boost in performance!

### Wrap Up

Gulp is a very powerful JavaScript build tool that can help automate some of the more tedious, but important, aspects of building your project. With less than an hour’s worth of work you were able to get your images minified, thus reducing load time and increasing performance for your website/app. That’s awesome and you should be proud of yourself!

This is just one of the many ways that build tools like Gulp can help you. There are many more ways it can help (minifying/concatenating CSS/JS files) and I hope you explore some of those awesome options.

If you enjoyed this article please consider donating some claps as it helps others find my work. Also, drop a comment and let me know what you’re working on and how Gulp helps you focus on the building.

And finally, this article was originally posted on [my personal blog](https://jonathansexton.me/blog). While you’re there don’t forget to sign up for the **Newsletter** which can be found at the top right corner of my blog page. I send it out monthly (I promise not to spam your inbox) and it’s filled with awesome articles from across the web that I think you’ll find helpful.

As always, have an awesome day full of love, happiness, and coding!

