---
title: 'Ember QuickTips: How to breakup and import SASS/CSS files separately'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-11T17:50:43.000Z'
originalURL: https://freecodecamp.org/news/ember-quicktips-how-to-breakup-and-import-sass-css-files-separately-b0759459027d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ZVmLA6aPZFWbG6UDK5nEfw.png
tags:
- name: CSS
  slug: css
- name: ember
  slug: ember
- name: JavaScript
  slug: javascript
- name: Sass
  slug: sass
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Michael Xavier

  There are times when it’s desirable to break up your stylesheets into multiple files
  and import them into your project separately. This came up in a side project I started
  recently, and I thought y’all might benefit from what I came...'
---

By Michael Xavier

There are times when it’s desirable to **break up your stylesheets into multiple files and import them into your project separately**. This came up in a side project I started recently, and I thought y’all might benefit from what I came up with as a solution. It’s a quick and easy method, so let’s get started ?

When you begin a new EmberJS app you’ll notice that the `index.html` file imports the main stylesheet into the app like so:

```html
<head>
 ...
 <link
  integrity=""
  rel="stylesheet"
  href="{{rootURL}}assets/test-app.css"
 >
 ...
</head>
```

`test-app.css` is compiled directly from your project. When we write our custom styles in `app/styles/app.css` they get put into this file.

Now, what if we don’t want to import all of our styles into the app as a single stylesheet? **How can we breakup our styles and import multiple stylesheets into the app?** Something like this:

```html
<head>
 ...
 <link
  integrity=""
  rel="stylesheet"
  href="{{rootURL}}assets/test-app.css"
 >
 <link
  integrity=""
  rel="stylesheet"
  href="{{rootURL}}assets/second-stylesheet.css"
 >
...
</head>
```

It may be easier than you think ?

### Step One: Write styles in SCSS/SASS and compile to CSS

First, install a SASS preprocessor to compile SCSS/SASS stylesheets into CSS stylesheets. For this example I’ll use `ember-cli-sass`:

```
ember install ember-cli-sass
```

Now rename `app/styles/app.css` to `app/styles/app.scss`. The preprocessor will take care of processing and compiling your stylesheet automatically.

If you run the app the Ember welcome page should display as usual:

![Image](https://cdn-media-1.freecodecamp.org/images/aYuzVPXdJ4BtKQenSZFHhS-C-GDrL2LS7Ryf)
_Nothing has changed. That’s good._

Comment out `{{welcome-page}}` in `app/templates/application.hbs` before you continue. We now have a blank DOM to work with.

### Step Two: Create a new stylesheet

Let’s create a new stylesheet called `app/styles/second-stylesheet.scss` and add the following styles:

```css
body {
 width: 100vw;
 height: 100vh;
 background-color: red;
}
```

A glaring red background would be very obvious, yet when you run the server you see nothing but a sea of white. Why is this?

If your instinct was to import it into the project as specified above, you would be correct:

```html
<head>
 ...
 <link
  integrity=""
  rel="stylesheet"
  href="{{rootURL}}assets/second-stylesheet.css"
 >
...
</head>
```

Yet, it still doesn’t show up. Why? ? That’s because the build pipeline hasn’t been configured to build this file in the correct folder just yet.

### Step Three: Configure Ember-CLI-Build

The final step is to tell the Ember app that you have a `css` file to include in its build pipeline.

In `ember-cli-build.js` add the following:

```js
...
module.exports = function(defaults) {
  let app = new EmberApp(defaults, {
    // Add options here
    outputPaths: {
      app: {
        css: {
          'second-stylesheet': '/assets/second-stylesheet.css'
        }
      }
    }
    
  });
  ...
};
```

**That’s it!** ? This tells Ember where to output your new stylesheet so that it can be properly accessed in your i`ndex.html` ?

![Image](https://cdn-media-1.freecodecamp.org/images/EY9F7DHJAzzfJqcwOS9Ft-TyL78cFd5nYfuE)
_A Sea of Red. Remember to restart the server when you make configuration changes or you may not see the changes._

