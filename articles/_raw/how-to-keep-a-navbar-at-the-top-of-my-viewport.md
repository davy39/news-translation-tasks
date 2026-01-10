---
title: How to Keep a Navbar at the Top of My Viewport?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-02T02:12:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-keep-a-navbar-at-the-top-of-my-viewport
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9aab740569d1a4ca2701.jpg
tags:
- name: CSS
  slug: css
- name: toothbrush
  slug: toothbrush
- name: UI
  slug: ui
seo_title: null
seo_desc: 'If you''re working on the Product Landing Page project and are having trouble
  with some of the user stories, you''re not alone.

  User story #13 gives a lot of people trouble. It reads:


  The navbar should always be at the top of the viewport.


  Non-fixed,...'
---

If you're working on the [Product Landing Page](https://www.freecodecamp.org/learn/responsive-web-design/responsive-web-design-projects/build-a-product-landing-page) project and are having trouble with some of the user stories, you're not alone.

User story #13 gives a lot of people trouble. It reads:

> The navbar should always be at the top of the viewport.

### Non-fixed, normal navbar

Imagine you have the following HTML:

```html
...
<header id="header">
  <img src="https://static1.squarespace.com/static/54d3e88ce4b0be204d0da36a/t/566f5b70bfe873371e44c7b0/1525197822184/" alt="logo" id="header-img">
  <nav id="nav-bar">
    <ul> 
      <li><a href="#about-us" class="nav-link">About Us</a></li>
      <li><a href="#videos" class="nav-link">Demo</a></li>
      <li><a href="#photos" class="nav-link">Photo Gallery</a></li>
      <li><a href="#contact-us" class="nav-link">Contact</a></li>
  </nav>
</header>
...
```

But when you scroll down the page, the navbar eventually leaves the view:

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Peek-2020-05-25-17-46.gif)

### How to create a fixed navbar

To create a fixed navbar, or a navbar that's always at the top of the viewport even as you scroll down the page, there are a few things you need to do.

First, target the header and fix it to the page with the following rule:

```css
header {
  position: fixed;
}
```

You'll notice that the navbar contracts to its default width, so set its width to the full width of the page:

```css
header {
  position: fixed;
  width: 100%;
}
```

Depending on the `display` properties of the other elements, you may need to manually set the `top` and `left` positions of the navbar:

```css
header {
  position: fixed;
  width: 100%;
  top: 0;
  left: 0;
}
```

Then all you need to do is apply some extra styling to get things looking good:

```css
header {
  position: fixed;
  width: 100%;
  top: 0;
  left: 0;
  background-color: #cc0000;
  color: white;
  font-family: 'Exo 2', sans-serif;
  padding: 1em;
}
```

### Fixed navbar — the result

After that, your navbar should still be visible even as you scroll down the page:

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Peek-2020-05-25-17-45.gif)


