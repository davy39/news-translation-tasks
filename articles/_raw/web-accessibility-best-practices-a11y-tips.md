---
title: 'Web Accessibility Best Practices: a11y Tips for your website'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-13T21:31:00.000Z'
originalURL: https://freecodecamp.org/news/web-accessibility-best-practices-a11y-tips
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9eb8740569d1a4ca3eb1.jpg
tags:
- name: Accessibility
  slug: accessibility
seo_title: null
seo_desc: "This short guide will provide practical examples of how to implement accessibility\
  \ in websites. \nAccessibility was not emphasized during school nor is it being\
  \ emphasized enough in the real world of web development. It is our hope that this\
  \ article, ..."
---

This short guide will provide practical examples of how to implement accessibility in websites. 

Accessibility was not emphasized during school nor is it being emphasized enough in the real world of web development. It is our hope that this article, along with many others, will encourage developers to create accessible sites from now on. 

It has always helped to get practical hands-on examples of how to do things. So this guide will focus on real-world examples  encountered in my day to day life as a web developer.

### Skipping Navigation

In order to give visually impaired users a pleasant experience on your website, they need to be able to access content quickly and efficiently. If you have never experienced a website through a screen reader I recommend doing so. It is the best way to test how easily a site can be navigated for non-sighted users. NVDA is a very good screen reader application that is provided free of charge. If you use the screen reader and find it helpful, please consider making a donation to the development team. The screen reader can be downloaded from [nvaccess.org](https://www.nvaccess.org/download/).

To allow visually impaired users to skip to the main content of a site and avoid tabbing through all the main navigation links:

1. Create a "skip navigation link" that lives directly underneath the opening  `body`  tag.

```
<a tabindex="0" class="skip-link" href="#main-content">Skip to Main Content</a>

```

`tabindex="0"`  is added to ensure the link is keyboard focusable on all browsers. Further information about keyboard accessibility can be found at [webaim.org](https://webaim.org/techniques/keyboard/tabindex).  
2. The "skip navigation" link needs to be associated with the main html tag in your webpage document using the ID tag.

```
<main id="main-content">
...page content
</main>

```

1. Hide the "skip navigation" link by default. This ensures that the link is only visible to sighted users when the link is in focus.  
Create a class for the link that can be styled with CSS. In my example, I have added the class  `skip-link` .

```
.skip-link {
position: absolute;
width: 1px;
height: 1px;
padding: 0;
overflow: hidden;
clip: rect(0, 0, 0, 0);
white-space: nowrap;
-webkit-clip-path: inset(50%);
clip-path: inset(50%);
border: 0;
}
.skip-link:active, .skip-link:focus {
position: static;
width: auto;
height: auto;
overflow: visible;
clip: auto;
white-space: normal;
-webkit-clip-path: none;
clip-path: none;
}

```

These CSS styles hide the link by default and only display the link when it is receiving keyboard focus. For more information visit the [a11yproject](http://a11yproject.com/posts/how-to-hide-content) and this [blog post](http://hugogiraudel.com/2016/10/13/css-hide-and-seek/).

### Accessible Header Structure

* Role "banner" is added to the  `header`  tag to signify to screen readers that this tag is the top most section. The role on the  `header`  is depreciated in HTML5 but should be added still in order to support as many screen readers as possible.
* This role is added to the  `header`  element when it is the child of the  `body`  element.

```
<header role="banner">
</header>  

```

### Accessible Main Content Structure

* Role "main" is added to the  `main`  tag to signify to screen readers that this tag is the  `main`  content section. Needing to add the role on the  `main`  is depreciated in HTML5 but should still be added in order to support as many screen readers as possible.
* This role is added to the  `main`  element when it is the main content section of the page. If there is more than one  `main`  element then each element will need an  `aria-labelledby`  attribute or an  `aria-label` .
* More information can be found at the [https://www.w3.org/TR/2017/NOTE-wai-aria-practices-1.1-20171214/examples/landmarks/main.html](https://5d0c2cfff1d8938bf45c6427--freecodecamp-dev.netlify.com/guide/accessibility/W3C%20Website%20documentation%20for%20Role).

```
<main role="main">
</main>  

```

