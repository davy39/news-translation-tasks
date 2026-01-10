---
title: 'Bootstrap 4: How to Make Top Fixed Navbar Stay in Container and Not Stretch?'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-02T02:17:00.000Z'
originalURL: https://freecodecamp.org/news/bootstrap-4-how-to-make-top-fixed-navbar-stay-in-container-and-not-stretch
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a9e740569d1a4ca26b6.jpg
tags:
- name: Bootstrap
  slug: bootstrap
- name: bootstrap 4
  slug: bootstrap-4
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: "There are many ways to make a fixed navbar stay inside a parent's div container.\
  \ We'll go over the most straightforward one here.\nImagine you have the following\
  \ code, modified slightly from the Bootstrap docs:\n<div class=\"container\">\n\
  \  <nav class=\"na..."
---

There are many ways to make a fixed navbar stay inside a parent's `div` container. We'll go over the most straightforward one here.

Imagine you have the following code, modified slightly from the [Bootstrap docs](https://v4-alpha.getbootstrap.com/components/navbar/#collapsible-content):

```html
<div class="container">
  <nav class="navbar navbar-fixed-top navbar-inverse bg-inverse">
    <button class="navbar-toggler hidden-lg-up" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
    </button>
    <div class="collapse navbar-toggleable-md" id="navbarResponsive">
      <a class="navbar-brand" href="#">
        <img src="" width="30" height="30" class="d-inline-block align-top" alt="">Navbar
      </a>
      <ul class="nav navbar-nav float-md-right">
        <li class="nav-item active">
          <a class="nav-link" href="#">Home
            <span class="sr-only">(current)</span>
          </a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Link</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Link</a>
        </li>
      </ul>
    </div>
  </nav>
  <div class="next"></div>
  hello
</div>
```

```css
div.next {
  background-color: lightblue;
  width: 100%;
  height: 60rem;
}
```

And your page looks like this:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/1.png)

## Solutions

While the docs read "Navbars and their contents are fluid by default. Use optional containers to limit their horizontal width," the easiest solution is to use CSS to set the width of the navbar directly:

```css
div.next {
  background-color: lightblue;
  width: 100%;
  height: 60rem;
}

.container {
  padding: 0px;
}

nav.navbar {
  width: inherit;
  top: 0%;
  left: 50%;
  transform: translateX(-50%);
}
```

By adding rules targeting `.container` and `nav.navbar`, your navbar is now the same width as the parent's container:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-46.png)

