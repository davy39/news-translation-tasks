---
title: How to build a responsive navbar with a toggle menu using Flexbox
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-23T10:44:52.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-responsive-navbar-with-a-toggle-menu-using-flexbox-3438e1d08783
coverImage: https://cdn-media-1.freecodecamp.org/images/0*duHsALHgV9KMBanO.
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Charlie Waite

  During a recent project, my team had to remove all traces of Bootstrap. This meant
  the extremely useful responsive navbar was going to have to be created from scratch.
  I’m relatively new to CSS, and have always relied on Bootstrap na...'
---

By Charlie Waite

During a recent project, my team had to remove all traces of Bootstrap. This meant the extremely useful responsive navbar was going to have to be created from scratch. I’m relatively new to CSS, and have always relied on Bootstrap navbars for their simplicity, so I volunteered to take on this task. Here’s what I learned and did throughout the process.

In this article, I will assume you have basic knowledge of HTML, CSS and JavaScript — you know how to link a stylesheet to your HTML or apply the styles in a `<sty`le>tag — and you know how to import a JavaScript file into your page.

_I’ve had defensive elitists criticise my way of doing things, especially with the toggle menu being `position: absolute` — if you have better ways of doing this then please respond below and we can make this better for the thousands of people reading it!_

### Getting started

Firstly, I started with some basic HTML for the layout:

```html
<div class="Navbar">
  <div class="Navbar__Link Navbar__Link-brand">
    Website title
  </div>
  <div class="Navbar__Link">
    Link
  </div>
  <div class="Navbar__Link">
    Link
  </div>
  <div class="Navbar__Link">
    Link
  </div>
  <div class="Navbar__Link">
    Link
  </div>
  <div class="Navbar__Link">
    Link
  </div>
</div>
```

You can use any naming convention for the classes.

![Image](https://cdn-media-1.freecodecamp.org/images/1*3tYOXMsOAdUXGmcXmOt50g.png)

Now, this isn’t giving us much yet. This is just a plain list of items. But with just one line of CSS, we see the power of Flexbox.

```css
.Navbar {
  display: flex;
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*dK5IrDcMRW00HPZ-wX6cBw.png)
_Navbar divs now aligned horizontally_

One line of code, and we already have our navigation items aligned horizontally across the top of the page.

Now let’s add two `nav` elements to our HTML so we can have some items on the left and right of the navbar:

```html
<div class="Navbar">
  <nav class="Navbar__Items">
    <div class="Navbar__Link Navbar__Link-brand">
      Website title
    </div>
    <div class="Navbar__Link">
      Link
    </div>
    <div class="Navbar__Link">
      Link
    </div>
    <div class="Navbar__Link">
      Link
    </div>
  </nav>
  <nav class="Navbar__Items Navbar__Items--right">
    <div class="Navbar__Link">
      Link
    </div>
    <div class="Navbar__Link">
      Link
    </div>
  </nav>
</div>
```

And some basic styling on our `Navbar` class which wraps all the other elements:

```css
.Navbar {
  background-color: #46ACC2;
  display: flex;
  padding: 16px;
  font-family: sans-serif;
  color: white;
}
```

Of course you can choose your own color scheme, font, and padding.

Now our navbar will look like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*ulTsKdXWB72DtxfDLuzl9A.png)

Whoops, now it looks a bit better, but we can’t have our navigation items displayed vertically. Before you read on, try having a guess as to what we’re going to do next…

Now our `display:flex` in the `.Navbar` class is no longer responsible for these items. It is now responsible for their `<n`av> containers. We want both to be aligned horizontally.

So we change the `.Navbar__Items` class too:

```css
.Navbar__Items {
  display:flex;
}
```

Now lets add some padding to our links to make this just a bit prettier:

```css
.Navbar__Link {
  padding-right: 8px;
}
```

Now our nav bar looks like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*DTgVCsT7tQlQ5Qgk5mQpSQ.png)

We’re getting there. But we also want the second `<n`av> to be aligned to the right. As you may have noticed — I added an extra class to the s`econd` <`nav> tag .Navbar__`Items--right.

Let’s simply add a `margin-left:auto` to this class:

```css
.Navbar__Items--right {
  margin-left:auto;
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*wDWAi7RCETK64FeP4yLNEA.png)
_After adding the margin-left to the second nav_

![Image](https://cdn-media-1.freecodecamp.org/images/1*wzj25OyMsvenI7APSxBDCg.png)
_On mobile_

As you can see, this is now much better. We already have a fully responsive navbar. But…

What if each navigation item had longer text? What if there were more items?

![Image](https://cdn-media-1.freecodecamp.org/images/1*TRNh6xHheH7t5I3sUxLI0A.png)
_Example of link names being longer_

As you can see, this is not what we want. We either want to make all the navigation items single line for consistency, or we’d like them tucked away in a menu which the user can toggle.

We’ll go with the latter, as it’s much cleaner and we won’t have to worry about the user struggling to read the text on each navigation item.

### `flex-direction`

With an item whose display is flex, there is also a rule for the direction we want the items to flex. This defaults to row, which aligns all the items neatly across the x-axis.

In our case, we’d like a small vertical menu at the top of our page. Let’s try changing the `flex-direction` on both `.Navbar` and `.Navbar__Items` to column — this aligns all menu items across the y-axis — when the screen width is 768px or lower.

And let’s remove that `margin-left` from the second `<n`av>:

```css
@media only screen and (max-width: 768px) {
  .Navbar__Items,
  .Navbar {
    flex-direction: column;
  }
  .Navbar__Items--right {
    margin-left: 0;
  }
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*rmC0cKnio5Cg9W2CA1luPQ.png)
_Navbar at 768px screen width or below_

But now, the navigation items are always visible, which takes up a significant amount of screen real estate.

In our media query, lets add a second rule for `.Navbar__Items` so they are not visible:

```css
@media only screen and (max-width: 768px) {
  .Navbar__Items,
  .Navbar {
    flex-direction: column;
  }
  .Navbar__Items {
    display:none;
  }
  .Navbar__Items--right {
    margin-left:0;
  }
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*8ipupgzJ6_ersFfTgVvm6w.png)
_What navbar now looks like on mobile_

### The toggle button

For the toggle button, I am going to use an icon provided by [Font Awesome](https://fontawesome.com/). If you decide to follow suit, just follow the instructions on their site to get the icons integrated into your project. You can use any icon set you want, or you can use plain text if you desire.

Now let’s add this icon to our HTML:

```html
<div class="Navbar">
   <div class="Navbar__Link Navbar__Link-brand">
      Website title
    </div>
    <div class="Navbar__Link Navbar__Link-toggle">
      <i class="fas fa-bars"></i>
    </div>
  <nav class="Navbar__Items">
    <div class="Navbar__Link">
      Longer Link
    </div>
    <div class="Navbar__Link">
      Longer Link
    </div>
    <div class="Navbar__Link">
      Link
    </div>
  </nav>
  <nav class="Navbar__Items Navbar__Items--right">
    <div class="Navbar__Link">
      Link
    </div>
    <div class="Navbar__Link">
      Link
    </div>
  </nav>
</div>
```

I have bolded the new addition. You will notice that this toggle does not go within any of the `nav` tags but sits outside with the website title. Makes sense.

![Image](https://cdn-media-1.freecodecamp.org/images/1*GkN1E6ZKm7W93FKDqTiWBQ.png)
_Menu icon added_

Of course, it’s not where we want it to be. And even worse, it’s visible on desktop resolutions.

![Image](https://cdn-media-1.freecodecamp.org/images/1*K5ygf98rpZNXLxQcjsJkXw.png)

Let’s fix this. Let’s do what we did with the `.Navbar__Items` on mobile to the menu icon on desktop:

```css
.Navbar__Link-toggle {
  display: none;
}
```

Now let’s add some rules to the same class within our media query:

```css
.Navbar__Link-toggle {
  align-self: flex-end;
  display: initial;
  position: absolute;
  cursor: pointer;
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*5jybOok3eVV03DHWKitL3g.png)
_What the navbar now looks like on mobile with the toggle menu_

Now, we are pretty much done here. We have our desired look. But we need to add toggle functionality to the menu icon.

In your JavaScript, add:

```html
function classToggle() {
  const navs = document.querySelectorAll('.Navbar__Items')
  
  navs.forEach(nav => nav.classList.toggle('Navbar__ToggleShow'));
}

document.querySelector('.Navbar__Link-toggle')
  .addEventListener('click', classToggle);
```

Now lastly, add the `Navbar__ToggleShow` with the rule `display:flex`to your media query.

Now we have a fully responsive navbar with toggle menu. With Flexbox it really is that simple!

![Image](https://cdn-media-1.freecodecamp.org/images/1*k0-kcRuPaA4LeuxzcIlJMg.gif)

### The final code

#### HTML:

```html
<div class="Navbar">
   <div class="Navbar__Link Navbar__Link-brand">
      Website title
    </div>
    <div class="Navbar__Link Navbar__Link-toggle">
      <i class="fas fa-bars"></i>
    </div>
  <nav class="Navbar__Items">
    <div class="Navbar__Link">
      Longer Link
    </div>
    <div class="Navbar__Link">
      Longer Link
    </div>
    <div class="Navbar__Link">
      Link
    </div>
  </nav>
  <nav class="Navbar__Items Navbar__Items--right">
    <div class="Navbar__Link">
      Link
    </div>
    <div class="Navbar__Link">
      Link
    </div>
  </nav>
</div>
```

#### CSS:

```css
.Navbar {
  background-color: #46ACC2;
  display: flex;
  padding: 16px;
  font-family: sans-serif;
  color: white;
}

.Navbar__Link {
  padding-right: 8px;
}

.Navbar__Items {
  display: flex;
}

.Navbar__Items--right {
  margin-left:auto;
}

.Navbar__Link-toggle {
  display: none;
}

@media only screen and (max-width: 768px) {
  .Navbar__Items,
  .Navbar {
    flex-direction: column;
  }
    
.Navbar__Items {
    display:none;
  }
    
.Navbar__Items--right {
    margin-left:0;
  }
    
.Navbar__ToggleShow {
    display: flex;
  }
    
.Navbar__Link-toggle {
    align-self: flex-end;
    display: initial;
    position: absolute;
    cursor: pointer;
   } 
}
```

#### JS:

```js
function classToggle() {
  const navs = document.querySelectorAll('.Navbar__Items')
  
  navs.forEach(nav => nav.classList.toggle('Navbar__ToggleShow'));
}

document.querySelector('.Navbar__Link-toggle')
  .addEventListener('click', classToggle);
```

Read more about Flexbox at:

[**Basic concepts of flexbox**](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Basic_Concepts_of_Flexbox)  
[_The Flexible Box Module, usually referred to as flexbox, was designed as a one-dimensional layout model, and as a…_](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Basic_Concepts_of_Flexbox)

And where I learned the basics of Flexbox myself:

[**I just launched a free full-length Flexbox course where you can build projects interactively**  
_After the success of the CSS Grid course I launched with freeCodeCamp in December (over 14,000 students so far!) I…_](https://www.freecodecamp.org/news/i-just-launched-a-free-full-length-flexbox-course-where-you-can-build-projects-interactively-1860e3d3c4af/)

Follow me on [Twitter](https://twitter.com/CharlieCW90) or [GitHub](https://github.com/charliearlie).

