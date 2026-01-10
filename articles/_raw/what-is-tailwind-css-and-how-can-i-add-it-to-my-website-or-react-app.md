---
title: What is Tailwind CSS and How Can I Add it to my Website or React App?
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-05-19T14:45:00.000Z'
originalURL: https://freecodecamp.org/news/what-is-tailwind-css-and-how-can-i-add-it-to-my-website-or-react-app
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/tailwind-1.jpg
tags:
- name: CSS
  slug: css
- name: CSS Framework
  slug: css-framework
- name: CSS3
  slug: css3
- name: Developer Tools
  slug: developer-tools
- name: framework
  slug: framework
- name: front end
  slug: front-end
- name: Front-end Development
  slug: front-end-development
- name: frontend
  slug: frontend
- name: HTML
  slug: html
- name: PostCSS
  slug: postcss
- name: tailwind
  slug: tailwind
- name: tools
  slug: tools
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "CSS is a technology that can be your best or worst friend. While it's incredibly\
  \ flexible and can produce what seems like magic, without the proper care and attention,\
  \ it can become hard to manage like any other code. \nHow can Tailwind CSS help\
  \ us to..."
---

CSS is a technology that can be your best or worst friend. While it's incredibly flexible and can produce what seems like magic, without the proper care and attention, it can become hard to manage like any other code. 

How can Tailwind CSS help us to take control of our styles?

* [What is Tailwind?](#heading-what-is-tailwind)
* [So what makes Tailwind great?](#heading-so-what-makes-tailwind-great)
* [Part 1: Adding Tailwind CSS to a static HTML page](#heading-part-1-adding-tailwind-css-to-a-static-html-page)
* [Part 2: Adding Tailwind CSS to a React app](#heading-part-2-adding-tailwind-css-to-a-react-app)

%[https://www.youtube.com/watch?v=7KeZcRMltP0]

## What is Tailwind?

[Tailwind CSS](https://tailwindcss.com/) is a "utility-first" CSS framework that provides a deep catalog of CSS classes and tools that lets you easily get started styling your website or application.

The underlying goal is that as you're building your project, you don't need to deal with cascading styles and worrying about how to override that 10-selector pileup that's been haunting your app for the last 2 years.

## So what makes Tailwind great?

Taildwind's solution is to provide a wide variety of CSS classes that each have their own focused use. Instead of a class called `.btn` that is created with a bunch of CSS attributes directly, in Tailwind, you would either apply a bunch of classes like `bg-blue-500 py-2 px-4 rounded` to the button element or build a `.btn` class by [applying](https://tailwindcss.com/docs/functions-and-directives/#apply) those utility class to that selector.

While Tailwind has a lot more going for it, we're going to focus on these basics for this tutorial, so let's dig in!

## Part 1: Adding Tailwind CSS to a static HTML page

We're going to start off by applying Tailwind CSS straight to a static HTML page. The hope is that by focusing on Tailwind and not the app, we can get a better understanding of what's actually happening with the framework.

### Step 1: Creating a new page

You can get started by simply creating a new HTML file. For the content, you can use whatever you want, but I'm going to use [fillerama.io](http://fillerama.io/) so the filler content is a bit more fun.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/html-page-with-content.jpg)
_New HTML page with content_

If you want to simplify this step, you can just [copy the file I created](https://github.com/colbyfayock/my-tailwind-static/commit/c7db11899c9cd193cdd666fd228cfaefe75623f2#diff-eacf331f0ffc35d4b482f1d15a887d3b) to get started.

[Follow along with the commit!](https://github.com/colbyfayock/my-tailwind-static/commit/c7db11899c9cd193cdd666fd228cfaefe75623f2)

### Step 2: Adding Tailwind CSS via CDN

Tailwind typically recommends that you install through [npm](https://www.npmjs.com/package/tailwindcss) to get the full functionality, but again, we're just trying to understand how this works first.

So let's add a link to the CDN file in the `<head>` of our document:

```html
<link href="https://unpkg.com/tailwindcss@^1.0/dist/tailwind.min.css" rel="stylesheet">
```

Once you save and reload the page, the first thing you'll notice is that all of the styles were stripped!

![Image](https://www.freecodecamp.org/news/content/images/2020/05/html-page-tailwind-base.jpg)
_HTML page with the Tailwind CSS base_

This is expected. Tailwind includes a set of [preflight styles](https://tailwindcss.com/docs/preflight) to fix cross-browser inconsistencies. For one, they include the popular [normalize.css](https://github.com/necolas/normalize.css/) which they build upon with their own styles.

But we're going to learn how to use Tailwind to add back our styles and set things up how we want!

[Follow along with the commit!](https://github.com/colbyfayock/my-tailwind-static/commit/b431b75cee0a03154a70b194b6dfcf028bc65942)

### Step 3: Using Tailwind CSS to add styles to your page

Now that we have Tailwind installed, we've added the ability to make use of their huge library of utility classes that we'll now use to add styles back to our page.

Let's start off by adding some margin to all of our paragraphs (`<p>`) and our list elements (`<ol>`, `<ul>`). We can do this by adding the `.my-5` class to each element like so:

```html
<p class="my-5">
  Bender, quit destroying the universe! Yeah, I do that with my stupidness. I never loved you. Moving along…
  Belligerent and numerous.
</p>

```

The class name follows a pattern that you'll notice with the rest of the utility classes – `.my-5` stands for margin (m) applied to the y-axis (y) with a value of 5 which in Tailwind's case, it uses [rem](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Values_and_units), so the value is 5rem.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/html-page-paragraph-styles.jpg)
_HTML page with basic paragraph styles_

Next, let's make our headers look like actual headers. Starting with our `h1` tag, let's add:

```html
<h1 class="text-2xl font-bold mt-8 mb-5">

```

Here's what's happening:

* `text-2xl`: set the text size (font-size) to 2xl. In Tailwind, that 2xl will equate to 1.5rem
* `font-bold`: set the weight of the text (font-weight) to bold
* `mt-8`: Similar to `my-5`, this will set the margin top (t) to 8rem
* `mb-5`: And this will set the margin bottom (b) to 5rem

![Image](https://www.freecodecamp.org/news/content/images/2020/05/html-page-header-styles.jpg)
_HTML page with styled H1_

With those classes added to the `h1`, let's apply those same exact classes to the rest of our header elements, but as we go down the list, reduce the size of the font size, so it will look like:

* h2: `text-xl`
* h3: `text-lg`

![Image](https://www.freecodecamp.org/news/content/images/2020/05/html-page-all-headers-style.jpg)
_HTML page with all headers styled_

Now let's make our list elements look like lists. Starting with our unordered list (`<ul>`), let's add these classes:

```html
<ul class="list-disc list-inside my-5 pl-2">

```

Here's what we're adding:

* `list-disc`: set the list-style-stype to disc (the markers on each line item)
* `list-inside`: sets the position of the list markers using  relative to the list items and the list itself with list-style-position to inside
* `my-5`: set the margin of the y axis to 5rem
* `pl-2`: set the left padding to 2rem

Then we can apply the exact same classes to our ordered list (`<ol>`), except instead of `list-disc`, we want to change our style type to `list-decimal`, so that we can see numbers given it's an ordered list.

```html
<ol class="list-decimal list-inside my-5 pl-2">

```

And we have our lists!

![Image](https://www.freecodecamp.org/news/content/images/2020/05/html-page-styled-lists.jpg)
_HTML page with styled lists_

Finally, let's make our content a little easier to read by setting a max width and centering the content. On the `<body>` tag, add the following:

```html
<body class="max-w-4xl mx-auto">

```

/Note: Typically you wouldn't want to apply these classes to the `<body>` itself, rather, you can wrap all of your content with a `<main>` tag, but since we're just trying to get an idea of how this works, we'll roll with this. Feel free to add the `<main>` tag with those classes instead if you prefer!/

And with that, we have our page!

![Image](https://www.freecodecamp.org/news/content/images/2020/05/html-page-content-centered.jpg)
_HTML page with centered content_

[Follow along with the commit!](https://github.com/colbyfayock/my-tailwind-static/commit/06fd719c98d17e2242b61ec2ab7034436c1c2ba6)

### Step 4: Adding a button and other components

For the last part of our static example, let's add a button.

The trick with Tailwind, is they intentionally don't provide pre-baked component classes with the idea being that likely people would need to override these components anyways to make them look how they wanted.

So that means, we're going to have to create our own using the utility classes!

First, let's add a new button. Somewhere on the page, add the following snippet. I'm going to add it right below the first paragraph (`<p>`) tag:

```html
<button>Party with Slurm!</button>

```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/html-page-unstyled-button.jpg)
_HTML page with unstyled button_

You'll notice just like all of the other elements, that it's unstyled, however, if you try clicking it, you'll notice it still has the click actions. So let's make it look like a button.

Let's add the following classes:

```html
<button class="text-white font-bold bg-purple-700 hover:bg-purple-800 py-2 px-4 rounded">
  Party with Slurm!
</button>

```

Here's a breakdown of what's happening:

* `text-white`: we're setting our text color to white
* `font-bold`: set the weight of the text to bold (font-weight)
* `bg-purple-700`: set the background color of the button to purple with a shade of 700. The 700 is relative to the other colors defined as purple, you can find these values on their [palette documentation page](https://tailwindcss.com/docs/customizing-colors#default-color-palette)
* `hover:bg-purple-800`: when someone hovers over the button, set the background color to purple shade 800. Tailwind provides these helper classes that allow us to easily define interactive stiles with things like [hover, focus, and active modifiers](https://tailwindcss.com/course/hover-focus-and-active-styles/)
* `py-2`: set the padding of the y-axis to 2rem
* `px-4`: set the padding of the  x-axis to 4rem
* `rounded`: round the corners of the element by setting the border radius. With tailwind, it sets the border-radius value to .25rem

And with all of that, we have our button!

![Image](https://www.freecodecamp.org/news/content/images/2020/05/html-page-styled-button.jpg)
_HTML page with a styled button_

You can apply this methodology to any other component that you'd like to build. Though it's a manual process, we'll find out how we can make this process easier when building in more dynamic projects like those based on React.

[Follow along with the commit!](https://github.com/colbyfayock/my-tailwind-static/commit/09312336dce316a75e8007d6c935133490f16c25)

## Part 2: Adding Tailwind CSS to a React app

For more of a real-world use case, we're going to add Tailwind CSS to an app created with [Create React App](https://reactjs.org/docs/create-a-new-react-app.html).

First, we'll walk through the steps you need to take to add tailwind to your project using a fresh install of Create React App, then we'll use our content from our last example to recreate it in React.

### Step 1: Spinning up a new React app

I'm not going to detail this step out too much. The gist is we'll bootstrap a new React app using Create React App.

To get started, you can follow along [with the directions](https://reactjs.org/docs/create-a-new-react-app.html) from the official React documentation:

[https://reactjs.org/docs/create-a-new-react-app.html](https://reactjs.org/docs/create-a-new-react-app.html)

And once you start your development server, you should now see an app!

![Image](https://www.freecodecamp.org/news/content/images/2020/05/create-react-app-starting-page.jpg)
_Create React App starting page_

Finally, let's migrate all of our old content to our app. To do this, copy everything inside of the `<body>` tag of our static example and paste it inside of the wrapper `<div className="App">` in the new React project.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/code-migrating-content.jpg)
_Migrating code to React app_

Next, change all `class="` attributes from the content we pasted in to `className="` so that it's using proper React attributes:

![Image](https://www.freecodecamp.org/news/content/images/2020/05/code-fixing-class-attribute.jpg)
_Fixing class attribute in content_

And lastly, replace the className `App` on our wrapper `<div>` to the classes we used on our static `<body>`.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/code-wrapper-styles.jpg)
_Adding wrapper styles to the app_

Once you save your changes and spin back up your server, it will look deceivingly okay.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/react-app-basic-content.jpg)
_React app with basic content_

React includes some basic styles itself, so while it looks okay, we're not actually using Tailwind yet. So let's get started by installing it!

[Follow along with the commit!](https://github.com/colbyfayock/my-tailwind-dynamic/commit/57993883c77739f71072bcc02ed2398543efc2fd)

### Step 2: Installing Tailwind in your React app

There are a few steps we'll need to go through in order to get Tailwind up and running on our app. Make sure you follow these steps carefully to ensure it's properly configured.

First, let's add our dependencies:

```
yarn add tailwindcss postcss-cli autoprefixer
# or
npm install tailwindcss postcss-cli autoprefixer

```

[Per Tailwind's documentation](https://tailwindcss.com/docs/installation#4-process-your-css-with-tailwind), we need to be able to process our styles so that they can be properly added to our pipeline. So in the above, we're adding:

* [tailwindcss](https://tailwindcss.com/): the core Tailwind package
* [postcss-cli](https://github.com/postcss/postcss): Create React App already uses postcss, but we need to configure Tailwind to be part of that build process and run it's own processing
* [autoprefixer](https://github.com/postcss/autoprefixer): Tailwind doesn't include vendor prefixes, so we want to add autoprefixer to handle this for us. This runs as part of our postcss configuration

We're also going to add two dev dependencies that make it easier to work with our code:

```
yarn add concurrently chokidar-cli -D
# or
npm install concurrently chokidar-cli --save-dev

```

* [concurrently](https://github.com/kimmobrunfeldt/concurrently): a package that lets us set up the ability to run multiple commands at once. This is helpful since we'll need to watch both the styles and React app itself.
* [chokidar-cli](https://github.com/kimmobrunfeldt/chokidar-cli): let's us watch files and run a command when changed. We'll use this to watch our CSS file and run the build process of the CSS on cahnge

Next, let's configure postcss, so create a new file in the root of your project called `postcss.config.js` and include the following:

```js
// Inside postcss.config.js
module.exports = {
    plugins: [
        require('tailwindcss'),
        require('autoprefixer')
    ],
};

```

This will add the Tailwindcss and Autoprefixer plugins to our postcss config.

With our configuration, we need to include it as part of the build and watch processes. Inside `package.json`, add the following to definitions to your `scripts` property:

```json
"build:css": "tailwind build src/App.css -o src/index.css",
"watch:css": "chokidar 'src/App.css' -c 'npm run build:css'",

```

Additionally, modify the `start` and `build` scripts to now include those commands:

```json
"start": "concurrently -n Tailwind,React 'npm run watch:css' 'react-scripts start'",
"build": "npm run build:css && react-scripts build",

```

With our configuration ready to go, let's try our styles back to where they were when we left off from the static example.

Inside the `App.css` file, replace the entire content with:

```css
@tailwind base;
@tailwind components;
@tailwind utilities;

```

This is going to import Tailwind's base styles, components, and utility classes that allow Tailwind to work as you would expect it to.

We can also remove the `App.css` import from our `App.js` file because it's now getting injected directly into our `index.css` file. So remove this line:

```js
import './App.css';

```

Once you're done, you can start back up your development server! If it was already started, make sure to restart it so all of the configuration changes take effect.

And now the page should look exactly like it did in our static example!

![Image](https://www.freecodecamp.org/news/content/images/2020/05/react-app-with-styled-content.jpg)
_React app with content styled_

[Follow along with the commit!](https://github.com/colbyfayock/my-tailwind-dynamic/commit/5f50cc218ef58f469dad7f09bdad31f36b58a896)

### Step 3: Creating a new button component class with Tailwind

Tailwind doesn't ship with prebaked component classes, but it does make it easy to create them!

We're going to use our button that we already created as an example of creating a new component. We'll create a new class `btn` as well as a color modifier `btn-purple` to accomplish this.

The first thing we'll want to do is open up our App.css file where we'll create our new class. Inside that file, let's add:

```css
.btn {
  @apply font-bold py-2 px-4 rounded;
}

```

If you remember from our HTML, we're already including those same classes to our `<button>` element.  Tailwind let's us "apply" or include the styles that make up these utility classes to another class, in this case, the `.btn` class.

And now that we're creating that class, let's apply it to our button:

```html
<button className="btn text-white bg-purple-700 hover:bg-purple-800">
  Party with Slurm!
</button>

```

And if we open up our page, we can see our button still looks the same. If we inspect the element, we can see our new `.btn` class generated with those styles.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/react-tailwind-button-class.jpg)
_.btn class in a React app with Tailwind_

Next, let's create a color modifier. Similar to what we just did, we're going to add the following rules:

```css
.btn-purple {
  @apply bg-purple-700 text-white;
}

.btn-purple:hover {
  @apply bg-purple-800;
}

```

Here, we're adding our background color and our text color to our button class. We're also applying a darker button color when someone hovers over the button.

We'll also want to update our HTML button to include our new class and remove the ones we just applied:

```html
<button className="btn btn-purple">
  Party with Slurm!
</button>

```

And with that change, we can still see that nothing has changed and we have our new button class!

![Image](https://www.freecodecamp.org/news/content/images/2020/05/react-tailwind-styled-button.jpg)
_Styled button in React with Tailwind_

[Follow along with the commit!](https://github.com/colbyfayock/my-tailwind-dynamic/commit/7a76e8a4583b0a4c523ea902d73e889c7b86f437)

## Applying these concepts to more components

Through this walkthrough, we learned how to create a new component class using the Tailwind apply directive. This allowed us to create reusable classes that represent a component like a button.

We can apply this to any number of components in our design system. For instance, if we wanted to always show our lists the way we set them up here, we could create a `.list-ul` class that represented an unordered list with the Tailwind utilities `list-disc list-inside my-5 pl-2` applied.

## What tips and tricks do you like to use with Tailwind?

Share with me on [Twitter](https://twitter.com/colbyfayock)!

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Follow me for more Javascript, UX, and other interesting things!" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">? Follow Me On Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">?️ Subscribe To My Youtube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;">✉️ Sign Up For My Newsletter</a>
    </li>
  </ul>
</div>

