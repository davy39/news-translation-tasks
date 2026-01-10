---
title: How to Modularize HTML Using Template Engines and Gulp
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2015-11-07T04:36:01.000Z'
originalURL: https://freecodecamp.org/news/how-to-modularize-html-using-template-engines-and-gulp-d1cb8af54138
coverImage: https://cdn-media-1.freecodecamp.org/images/1*uQxKWK71HvEAlKwCc78XbQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Zell Liew

  Template engines are tools that help you break HTML code into smaller pieces that
  you can reuse across multiple HTML files. Template engines also give you the power
  to feed data into variables that help simplify your code.

  You can only u...'
---

By Zell Liew

Template engines are tools that help you break HTML code into smaller pieces that you can reuse across multiple HTML files. Template engines also give you the power to feed data into variables that help simplify your code.

You can only use template engines if you had a way to compile them into HTML. This means that you can only use them if you’re working with a backend language, or if you’re using client-side JavaScript.

However, with Node.js, you can now harness the power of template engines easily through the use of tools like Gulp.

Today, you’ll learn what template engines are, why you should use them, and how to set one up with Gulp.

### Why you should use template engines

Template engines have two major benefits:

1. They lets you break HTML code down into smaller files
2. They let you populate your markup with data

Let’s go through them one by one.

#### Breaking HTML into smaller files

It’s common for a HTML file to contain blocks of code that are repeated across the website. Consider this markup for a second:

```
<body>  <nav> ... </nav>  <div class="content"> ... </div>  <footer> ... </footer></body>
```

Many lines of code, particularly those within nav and footer, are repeated across multiple pages.

Since they are repeated, we can pull them out and place them into smaller files called **partials**.

For example, the navigation partial may contain a simple navigation like this:

```
<!-- Navigation Partial --><nav>  <a href="index.html">Home</a>  <a href="about.html">About</a>  <a href="contact.html">Contact</a></nav>
```

Then, we can reuse this partial across our HTML files. Here’s what HTML files might look like with partials included:

```
<body>  {% include partials "nav" %}  <div class="content"> ... </div>  {% include partials "footer" %}</body>
```

Note: The syntax for including partials is different for each template engine. The one shown above is for nunjucks or Swig.

There’s one great thing about being able to break code up like this.

Just imagine what you would do if you had to change the navigation now. When you use a partial, all you have to do is change code in the navigation partial and all your pages will be updated.

This is much easier than having to change the same code across every file the navigation is used on.

Breaking code down into smaller files helps you write less (duplicated) code. It also keeps you from going insane when you need to dive in and change old code.

Let’s move on to the second benefit.

#### Using data to populate markup

This benefit is best explained with an example. Let’s say you’re creating a gallery of images. Your markup would look something similar to this:

```
<div class="gallery">  <div class="gallery__item">    <img src="item-1.png" alt="item-1">  </div>  <div class="gallery__item">    <img src="item-2.png" alt="item-2">  </div>  <div class="gallery__item">    <img src="item-3.png" alt="item-3">  </div>  <div class="gallery__item">    <img src="item-4.png" alt="item-4">  </div>  <div class="gallery__item">    <img src="item-5.png" alt="item-5">  </div></div>
```

Notice how the .gallery__item div was repeated multiple times above?

If you had to change the markup of one .gallery__item, you’d have to change it in five different places.

Now, imagine that you had the ability to write HTML using loop logic. You’d probably write something similar to this:

```
<div class="gallery">  // Some code to loop through the following 5 times:   <div class="gallery__item">    <img src="$path-to-image" alt="$alt-text">  </div>  // end loop</div>
```

Template engines gives you the ability to use such a loop. Instead of looping exactly five times, it loops through a set of data that you pass to it. The HTML would become:

```
<div class="gallery">  {% for image in images %}    <div class="gallery__item">      <img src="{{src}}" alt="{{alt}}">    </div>  {% endfor %}</div>
```

The data would be a JSON file that resembles the following:

```
images: [{  src: "item1.png",  alt: "alt text for item1"  }, {  src: "item2.png",  alt: "alt text for item1"  },  // ... Until the end of your data]
```

With the supplied data, the template engine would create a markup such that the number of .gallery__items would correspond to the number of items in the images array of the data.

The best part is that you only have to change the markup once and all .gallery__items will be updated.

### Using a template engine with Gulp

Before we move on and create a gulp task that uses a template engine, let’s look at a list of popular JavaScript-based template engines that Gulp is able to use:

* [Dust.js](http://akdubya.github.io/dustjs/)
* [Embedded JS](http://www.embeddedjs.com/) (also known as ejs)
* [Handlebars](http://handlebarsjs.com/)
* [Hogan.js](http://twitter.github.io/hogan.js/)
* [Jade](http://jade-lang.com/)
* [Mustache](https://mustache.github.io/)
* [Nunjucks](https://mozilla.github.io/nunjucks/)
* [Swig](http://paularmstrong.github.io/swig/) (which is no longer maintained)

Each template engine is unique and has its own pros and cons. Syntax can vary wildly between template engines. Because of this, we’ll focus on using one template engine in this article — nunjucks.

I highly recommend nunjucks because it’s extremely powerful. It has features — like inheritance — that most template engines do not have. I’ve also used Mustache and Handlebars previously, and found that they weren’t powerful enough in many circumstances.

Now, let’s incorporate nunjucks into our workflow.

### Using Nunjucks with Gulp

![Image](https://cdn-media-1.freecodecamp.org/images/1*Lhl-R75OQPH6Xm3bZrs7iA.jpeg)

We can use nunjucks through a plugin called [gulp-nunjucks-render](https://github.com/carlosl/gulp-nunjucks-render).

Let’s start by installing gulp-nunjucks-render.

Note: I’m assuming you know how to use Gulp, so I won’t go into the basics. If you find yourself feeling confused, it might be good to [brush up on your Gulp basics before coming back here.](https://css-tricks.com/gulp-for-beginners/)

```
$ npm install gulp-nunjucks-render --save-dev
```

```
var nunjucksRender = require('gulp-nunjucks-render');
```

Next, we need to create a project structure that allows us to use nunjucks easily. We will use this structure:

```
project/   |- app/       |- index.html and other .html files      |- pages/      |- templates/          |- partials/
```

**The templates folder** is used for storing all nunjucks partials and other nunjucks files that will be added to files in the pages folder.

**The pages folder** is used for storing files that will be compiled into HTML. Once they are compiled, they will be created in the app folder.

Let’s work through the process of creating some nunjucks files before creating the Gulp task.

First of all, one good thing about nunjucks (that other template engines might not have) is that it allows you to create a template that contains boilerplate HTML code which can be inherited by other pages. Let’s call this boilerplate HTML layout.nunjucks.

Create a file called layout.nunjucks and place it in your templates folder. It should contain some boilerplate code like <html>, <head> and <body> tags. It can also contain things that are similar across all your pages, like links to CSS and JavaScript files.

Here’s an example of a layout.nunjucks file:

```
<!-- layout.nunjucks -->
```

```
<!DOCTYPE html><html lang="en"><head>  <meta charset="UTF-8">  <title>Document</title>  <link rel="stylesheet" href="css/styles.css"></head><body>
```

```
  <!-- You write code for this content block in another file -->  {% block content %} {% endblock %}
```

```
  <script src="bower_components/jquery/dist/jquery.js"></script>  <script src="js/main.js"></script></body></html>
```

By the way, I prefer to use the .nunjucks extension for nunjucks files and partials because it lets me know that I’m working with nunjucks. If you’re not comfortable with .nunjucks, feel free to leave your files as .html.

Next, let’s create a index.nunjucks file in the pages directory. This file will eventually be converted into index.html and placed in the app folder.

It should extend layouts.nunjucks so it contains the boilerplate code we defined in layout.nunjucks:

```
<!-- index.nunjucks -->{% extends "layout.nunjucks" %}
```

We can then add HTML code that’s specific to index.nunjucks between {% block content %} and {% endblock %}.

```
<!-- index.nunjucks -->{% extends "layout.nunjucks" %}
```

```
{% block content %} <h1>This is the index page</h1>{% endblock %}
```

We’re done with setting up nunjucks files. Now, let’s create a nunjucks task that coverts index.nunjucks into index.html.

```
gulp.task('nunjucks', function() {  // nunjucks stuff here});
```

Within the nunjucks task, we first need tell nunjucks where to locate our templates. We can do so with the nunjucks.configure function that gulp-nunjucks-render provides.

```
gulp.task('nunjucks', function() {  nunjucksRender.nunjucks.configure(['app/templates/']);});
```

Next, we add files from pages into the gulp task through gulp.src. Then, we output these files in app.

```
gulp.task('nunjucks', function() {  nunjucksRender.nunjucks.configure(['app/templates/']);
```

```
  // Gets .html and .nunjucks files in pages  return gulp.src('app/pages/**/*.+(html|nunjucks)')  // Renders template with nunjucks  .pipe(nunjucksRender())  // output files in app folder  .pipe(gulp.dest('app'))});
```

Now, try running gulp nunjucks in your command line. Gulp will have created an index.html and placed it in the app folder for you.

![Image](https://cdn-media-1.freecodecamp.org/images/0*7qYZxfS5idGHLbof.png)

If you opened up this index.html file, you should see the following code:

```
<!DOCTYPE html><html lang="en"><head>  <meta charset="UTF-8">  <title>Document</title>  <link rel="stylesheet" href="css/styles.css"></head><body>
```

```
  <h1>This is the index page</h1>
```

```
  <script src="js/main.js"></script></body></html>
```

Notice how everything (except the <h1> tag) came from layouts.nunjucks? That’s what layout.nunjucks is for. If you need to mess around with the <head> tag, add JavaScript or change CSS files, you know you can do it in layouts.nunjucks and every single page will be updated accordingly.

At this point, you’ve successfully extended layouts.nunjucks into index.nunjucks and rendered it index.nunjucks into index.html. There’s a few more things we can improve on. One of the things we can do is to learn to use a partial.

### Adding a Nunjucks Partial

We need to create a partial before we can add it to index.nunjucks. Let’s create a partial called navigation.nunjucks and place it in a partials folder that’s within the templates folder.

![Image](https://cdn-media-1.freecodecamp.org/images/0*xTgHx0PLnJhxFNKB.png)

Then, let’s add a simple navigation to this partial:

```
<!-- navigation.nunjucks --><nav>  <a href="#">Home</a>  <a href="#">About</a>  <a href="#">Contact</a></nav>
```

Let’s now add the partial to our index.nunjucks file. We can add partials with the help of the {% include “path-to-partial” %} statement that nunjucks provides.

```
{% block content %} 
```

```
<h1>This is the index page</h1><!-- Adds the navigation partial -->{% include "partials/navigation.nunjucks" %}
```

```
{% endblock %}
```

Now, if you run gulp nunjucks, you should get a index.html file with the following code:

```
<!-- <head> and CSS -->
```

```
<h1>This is the index page</h1>
```

```
<nav>  <a href="#">Home</a>  <a href="#">About</a>  <a href="#">Contact</a></nav>
```

```
<!-- JavaScript and </body>    -->
```

When using partials like navigation, we can often run into situations where we need to add a class to one of the links on a page. Here’s an example:

```
<nav>  <!-- active class should only on be present on the homepage -->  <a href="#" class="active">Home</a>  <a href="#">About</a>  <a href="#">Contact</a></nav>
```

The active class should only be present on the homepage link if we’re on the homepage. If we’re on the about page, then the active class should only be present on the about link.

We can do this with a slightly modified version of partials called **Macros**. The only difference is that you can add variables to it in the same way you would add arguments to a JavaScript function.

### Adding a Nunjucks Macro

First, let’s create a nav-macro.nunjucks file in a macros folder that is within the templates folder. Note that we’re using nav-macro to make sure you don’t get confused between the two navigation nunjuck files.

![Image](https://cdn-media-1.freecodecamp.org/images/0*3-VWQZddWXvgH2ER.png)

You can begin writing macros once you’ve created the nav-macro.nunjucks file.

All macros begin and end with the following tags:

```
{% macro functionName() %}  <!-- Macro stuff here -->{% endmacro %}
```

Let’s create a macro called active. It’s purpose is to output the active class for our navigation. It should take one argument, activePage, that defaults to “home”.

```
{% macro active(activePage='home') %}  <!-- Macro stuff here -->{% endmacro %}
```

We’ll write HTML that will be created within the macro. Here, we can also use the if function provided by nunjucks to check if an active class should be added:

```
{% macro active(activePage='home') %}<nav>  <a href="#" class="{%if activePage == 'home' %} active {% endif %}">Home</a>  <!-- Repeat for about and contact --></nav>{% endmacro %}
```

We’re done writing the macro now. Let’s learn to use it in index.nunjucks next.

We use the import function in nunjucks to add a macro file, as opposed to the include function that we used previously to add a partial.

When we import a macro file, we have to set it as a variable as well. Here’s an example:

```
<!-- index.html -->{% block content %}
```

```
<!-- Importing Nunjucks Macro -->{% import 'macros/navigation.nunjucks' as nav %}
```

```
{% endblock %}
```

In this case, we’ve set the nav variable as the entire navigation.nunjucksmacro file. We can then use the nav variable to call any macro that’s written in that file.

```
{% import 'macros/navigation.nunjucks' as nav %}<!-- Creating the navigation with activePage = 'home' -->{{nav.active('home')}}
```

With this change, try running gulp nunjucks again and you should be able to see this output:

```
<nav>  <a href="#" class=" active ">Home</a>  <a href="#" class="">About</a>  <a href="#" class="">Contact</a></nav>
```

That’s it for using Macros. Knowing this will invariably help you out a lot while using nunjucks :)

There’s one more thing we can do to enhance our templating experience with nunjucks, and that’s populating the HTML with data.

### Populating HTML with data

Let’s start by creating a file called data.json that contains your data. I’d recommend you place this data.json in the app folder.

```
$ cd app$ touch data.json
```

Let’s add some data now. We can use the data from the earlier example.

```
{  "images": [{    "src": "image-one.png",    "alt": "Image one alt text"  }, {    "src": "image-two.png",    "alt": "Image two alt text"  }]}
```

We then have to tweak our nunjucks task slightly to use data from this data.json file. To do so, we need to use to the help of another gulp plugin called [gulp-data](https://www.npmjs.com/package/gulp-data).

Let’s install gulp-data before moving on.

```
$ npm install gulp-data --save-dev
```

```
var data = require('gulp-data');
```

Gulp-data takes in a function that allows you to return a file. We can use the require function Node provides to get this data file:

```
.pipe(data(function() {  return require('./app/data.json')}))
```

When using require to get files from a custom directory (not node_modules), we need to tell Node the path to the directory. Here, we start with a ./ that tells Node to start with the current directory, then look into app for the data.json file.

Note: A better way is to use two functions, JSON.parse() and fs.readFileSync() instead of require. We will cover how to do so in [“Automating Your Workflow with Gulp”](http://zell-weekeat.com/automate-your-workflow/).

Let’s add the gulp-data to our nunjucks task now.

```
gulp.task('nunjucks', function() {  nunjucksRender.nunjucks.configure(['app/templates/']);
```

```
  return gulp.src('app/pages/**/*.+(html|nunjucks)')    // Adding data to nunjucks    .pipe(data(function() {      return require('./app/data.json')    }))    .pipe(nunjucksRender())    .pipe(gulp.dest('app'))});
```

Finally, let’s add some markup to index.nunjucks so it uses the data we’ve added.

```
<!-- index.nunjucks -->{% block content %}<div class="gallery">  <!-- Loops through "images" array -->  {% for image in images %}  <div class="gallery__item">    <img src="{{image.src}}" alt="{{image.alt}}">  </div>  {% endfor %}</div>{% endblock %}
```

```
<!-- index.html --><div class="gallery">  <div class="gallery__item">    <img src="image-one.png" alt="Image one alt text">  </div>Now, if you run `gulp nunjucks`, you should get a `index.html` file with the following markup: 
```

```
  <div class="gallery__item">    <img src="image-two.png" alt="Image two alt text">  </div></div>
```

Nice!

### Wrapping up

We’ve learned how template engines make development much easier and some basic ways to use them.

We then dove deeper into one template engine, nunjucks, and got it to work with Gulp. We also learned how to use:

* extend to inherit a nunjucks file
* include to include a partial
* import to import a macro

If you’d like to further speed up your workflow, check out [Automating Your Workflow](http://zell-weekeat.com/automate-your-workflow/). It will cover:

* Watching and compiling nunjucks files
* Preventing errors from nunjucks from breaking Gulp’s watch
* Reloading the browser automatically whenever a file changes

> This article first appeared on my blog at [www.zell-weekeat.com](http://zell-weekeat.com). Check it out if you want more articles like this

