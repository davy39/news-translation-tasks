---
title: How to Switch from jQuery to Vanilla JavaScript with Bootstrap 5
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-31T18:09:09.000Z'
originalURL: https://freecodecamp.org/news/bootstrap-5-vanilla-js-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/bootstrap-5-vanilla-js.jpg
tags:
- name: Bootstrap
  slug: bootstrap
- name: Bootstrap 5
  slug: bootstrap-5
- name: JavaScript
  slug: javascript
- name: jQuery
  slug: jquery
- name: Tutorial
  slug: tutorial
seo_title: null
seo_desc: 'By Zoltán Szőgyényi

  Bootstrap 5 is a free and open-source CSS framework directed at responsive, mobile-first
  front-end web development.

  In case you didn''t know, Bootstrap 5 alpha has been officially launched. It has
  removed jQuery as a dependency, ha...'
---

By Zoltán Szőgyényi

[Bootstrap 5](http://v5.getbootstrap.com/) is a free and open-source CSS framework directed at responsive, mobile-first front-end web development.

In case you didn't know, [Bootstrap 5 alpha has been officially launched](https://themesberg.com/blog/bootstrap/bootstrap-version-5-alpha-whats-new). It has removed jQuery as a dependency, has dropped support for Internet Explorer 9 and 10, and brings some awesome updates for the Sass files, markup, and a new Utility API.

This tutorial will show you how to start using VanillaJS instead of jQuery when building websites using the newest version of Bootstrap 5.

## Getting started

You will need to include Bootstrap 5 in your project. There are several ways to do this, but to keep it simple we will include the framework via CDN.

First of all, let's create a blank `index.html` page inside a project folder:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bootstrap 5 Vanilla JS tutorial by Themesberg</title>
</head>
<body>
    
</body>
</html>
```

Include the `bootstrap.min.css` stylesheet before the end of your `<head>` tag:

```html
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/5.0.0-alpha1/css/bootstrap.min.css" integrity="sha384-r4NyP46KrjDleawBgD5tp8Y7UzmLA05oM1iAEQ17CSuDqnUK2+k9luXQOfXJCJ4I" crossorigin="anonymous">
```

Afterwards include the Popper.js library and the main Bootstrap JavaScript file before the end of your `<body>` tag:

```html
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/5.0.0-alpha1/js/bootstrap.min.js" integrity="sha384-oesi62hOLfzrys4LxRF63OJCXdXDipiYWBnvTl9Y9/TRlw5xlKIEHpNyvvDShgf/" crossorigin="anonymous"></script>
```

Curious what the `integrity` and `crossorigin` attributes mean? Here's the explanation:

**Integrity attribute**: allows the browser to check the file source to ensure that the code is never loaded if the source has been manipulated.

**Crossorigin attribute**: is present when a request is loaded using 'CORS' which is now a requirement of SRI checking when not loaded from the 'same-origin'.

Great! Now we have successfully included the newest version of Bootstrap in our project. One of the obvious differences is that we no longer had to require jQuery as a dependency, **saving about 82.54 KB** in bandwidth if in a minified state.

## Switching from jQuery to Vanilla JS

Before we get started with this section, you should know that using Bootstrap 5 with jQuery is still possible according to the [official documentation](https://v5.getbootstrap.com/docs/5.0/getting-started/javascript/#still-want-to-use-jquery-its-possible).

We recommend using Vanilla JavaScript if the only reason you've been using jQuery was for the query selector, because you can do the same thing with the `document.querySelector('#element')` as if it was `$('#element')`.

The first step is to create a JavaScript file and include it before the end of the body tag but after the other two includes:

```html
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/5.0.0-alpha1/js/bootstrap.min.js" integrity="sha384-oesi62hOLfzrys4LxRF63OJCXdXDipiYWBnvTl9Y9/TRlw5xlKIEHpNyvvDShgf/" crossorigin="anonymous"></script>
<script src="js/app.js"></script>
```

So when do you need to actually use Javascript with Bootstrap 5? There are certain components in the framework that work only if they are initialized via Javascript, such as tooltips, popovers and toasts.

Furthermore, with components such as modals, dropdowns, and carousels you may want to be able to programmatically change them based on a user action or application logic.

### Initializing tooltips via Vanilla JavaScript

We all love tooltips, but they don't work unless they are initialized via JavaScript. Let's first start by creating a tooltip element inside our `index.html` file:

```html
<button id="tooltip" type="button" class="btn btn-secondary" data-toggle="tooltip" data-placement="top" title="Tooltip on top">
    Tooltip on top
</button>
```

Hovering over the button will not show the tooltip, because by default it is an opt-in feature of Bootstrap and it needs to be initialized manually using JavaScript. If you want to do it with jQuery, here's how it would look:

```js
$('#tooltip').tooltip();
```

Using Vanilla JS you would need to use the following code to enable the tooltip:

```js
var tooltipElement = document.getElementById('tooltip');
var tooltip = new bootstrap.Tooltip(tooltipElement);
```

What the code above does it that it selects the element with the unique id of "tooltip" and then creates a Bootstrap tooltip object. You can then use that to manipulate the state of the tooltip, such as showing or hiding the tooltip programmatically.

Here's an example on how you could show/hide it via methods:

```js
var showTooltip = true;
if (showTooltip) {
    tooltip.show();
} else {
    tooltip.hide();
}
```

If you would like to enable all of the tooltips you could also use the following code:

```js
var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-toggle="tooltip"]'));
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl)
});
```

What happens here is that we select all of the elements that have the `data-toggle="tooltip"` attribute and value and initialize a tooltip object for each one. It also saves them to a tooltipList variable.

### Toggle the visibility of your elements using the Collapse JavaScript methods

The collapse feature on Bootstrap is another very handy way to show and hide elements via data attributes or JavaScript.

Here's an example of how we can show or hide a card when a certain button is being clicked. Let's first create the HTML markup:

```html
<button id="toggleCardButton" type="button" class="btn btn-primary mb-2">Toggle Card</button>
    <div id="card" class="card collapse show" style="width: 18rem;">
        <img src="https://dev-to-uploads.s3.amazonaws.com/i/rphqzfoh2cbz3zj8m8t1.png" class="card-img-top" alt="...">
        <div class="card-body">
            <h5 class="card-title">Freecodecamp.org</h5>
            <p class="card-text">Awesome resource to learn programming from.</p>
            <a href="#" class="btn btn-primary">Learn coding for free</a>
        </div>
    </div>
```

So we created a button with the id `toggleCardButton` and a card with the id `card`. Let's start by selecting the two elements:

```js
var toggleButton = document.getElementById('toggleCardButton');
var card = document.getElementById('card');
```

Then we need to create a collapsable object using the newly selected card element:

```js
var collapsableCard = new bootstrap.Collapse(card, {toggle: false});
```

What the `toggle:false` flag does is that it keeps the element visible after creating the object. If not present, it would hide the card by default.

Now we need to add an event listener for the button for the click action:

```js
toggleButton.addEventListener('click', function () {
    // do something when the button is being clicked
});
```

And lastly we need to toggle the card using the collapsable object that we initialized like this:

```js
toggleButton.addEventListener('click', function () {
    collapsableCard.toggle();
});
```

That's it! Now the card will be shown/hidden whenever the button is clicked. Of course all of this could've been done using the [data attributes feature](https://v5.getbootstrap.com/docs/5.0/components/collapse/#via-data-attributes) from Bootstrap, but you may want to toggle certain elements based on an API call or a logic in your application.

## Conclusion

If you have followed along this tutorial you should now be able to use the most popular CSS framework without the need of requiring jQuery in your project. This lets you **save up to 85 KB of data** and makes your website faster! Congratulations ?

If you appreciate this tutorial and like using Bootstrap as a CSS framework for your projects, I invite you to check out some of the free and premium [Bootstrap themes, templates, and UI Kits](https://themesberg.com/templates/bootstrap) that we build at Themesberg ❤️

