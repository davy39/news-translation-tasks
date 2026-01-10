---
title: Progressive Enhancement with CSS Grid
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-08T18:16:46.000Z'
originalURL: https://freecodecamp.org/news/progressive-enhancement-with-css-grid-8138d4c7508c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*W_qmeZuel90pFUHZ89TfZQ.png
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Dominic Fraser

  CSS Grid (Grid) has been out for some time now, with full support in major modern
  browsers. I’ll leave others to dive into why it’s so great and what new design possibilities
  it makes so easy to explore. If you have been looking for...'
---

By Dominic Fraser

CSS Grid (Grid) has been out for some time now, with [full support](https://caniuse.com/#search=css%20grid) in major modern browsers. I’ll leave others to dive into why it’s so great and what new design possibilities it makes so easy to explore. If you have been looking for the best way to support responsive web designs, I’ve yet to see anyone that doesn’t love Grid. It’s simple to use, yet extremely powerful and flexible.

But, I hear you say, a lot of our users aren’t using the most up-to-date browser versions, or are in markets where Chrome/Firefox don’t hold a majority share. And, really, is re-writing all our old code really worth it?

I felt similarly, until hearing a great talk given by [Natalya Shelburne](https://twitter.com/natalyathree). She described how she started using [CSS Grid alongside Bootstrap](https://open.nytimes.com/bootstrap-to-css-grid-87b3f5f830e4), without losing support for older browsers, by **enhancing** rather than **deleting** old CSS.

![Image](https://cdn-media-1.freecodecamp.org/images/DWlI6bjdjAkRW7ulEUC81RdWpFspo3qM46E8)
_[ScotlandCSS](https://twitter.com/rachelandrew" rel="noopener" target="_blank" title="">Rachel Andrew</a> by <a href="https://twitter.com/chicgeek" rel="noopener" target="_blank" title="">Laura Kishimoto‏</a> at <a href="http://scotlandcss.com/" rel="noopener" target="_blank" title=")_

Importantly, this is without using any JavaScript polyfills, but using pure CSS. As Rachel Andrew mentions:

> _As we already know, **the browsers that don’t support grid are older**, slower browsers or browsers most often found on lower powered devices in emerging markets. Why would you force a bunch of JavaScript onto those devices?_

Natalya describes how “[feature queries](https://developer.mozilla.org/en-US/docs/Web/CSS/@supports)” can be used to implement Grid in browsers that do support it, without losing existing functionality. MDN refers to this as “[progressive enhancement](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout/CSS_Grid_and_Progressive_Enhancement)”, stating that:

> It is worth noting that you do not have to use grid in an _all or nothing_ way. You could start by simply enhancing elements in your design with grid, that could otherwise display using an older method.

### Using Grid

So, how do we go about this?

In a previous post, I described a simple approach to “[keep your footer where it belongs](https://medium.freecodecamp.org/how-to-keep-your-footer-where-it-belongs-59c6aa05c59c).” This avoids the problems seen when a page’s main content is too small to push a footer to the bottom of the page.

![Image](https://cdn-media-1.freecodecamp.org/images/Ums6BuchBW-nqPBRODUiKzPx7HvwKDa19BNj)
_From “[How to keep your footer where it belongs](https://medium.freecodecamp.org/how-to-keep-your-footer-where-it-belongs-59c6aa05c59c" rel="noopener" target="_blank" title=")”_

This provides a chance to show how a feature query can be used to move to using Grid.

**It’s important to note** that this is an example of **how** you could move to using Grid in an existing codebase, **not why** it is a powerful tool_._ This example is used because it is small — so it is possible to understand the **how** without distractions found in a larger codebase.

Realistically, Grid provides no great improvement here. The benefits of using a new tool should be discussed, rather than just implementing it because it is cool!

The example is below. More explanation on the code [is here](https://medium.freecodecamp.org/how-to-keep-your-footer-where-it-belongs-59c6aa05c59c).

```html
<!DOCTYPE html>
<html>
 <head>
   <link rel="stylesheet" type="text/css" href="main.css" />
 </head>
<body>
 <div id="page-container">
   <div id="content-wrap">
     <!-- all other page content -->
   </div>
   <footer id="footer"></footer>
 </div>
</body>
</html>
```

There are two main parts to adding Grid:

* adding the needed new grid properties
* overriding any properties no longer needed.

`main.css`:

```css
#page-container {
  position: relative;
  min-height: 100vh;
}
#content-wrap {
  padding-bottom: 2.5rem;    /* Footer height */
}
#footer {
  position: absolute;
  bottom: 0;
  width: 100%;
  height: 2.5rem;            /* Footer height */
}
```

`main.css` can be extended to **add**:

```css
@supports (display: grid) {
    #page-container {
        position: static;               // override
        display: grid;                  // new   
        grid-template-rows: 1fr auto;   // new
        grid-template-columns: 100%;    // new
    }
    
    #content-wrap {
        padding-bottom: 0;              // override
    }
    #footer {
        position: static;               // override 
        height: auto;                   // override
    }
}
```

`position` is set back to its [default](https://developer.mozilla.org/en-US/docs/Web/CSS/position) of `static`, and the `padding` and `height` are reset to values that do not interfere with the new layout.

`min-height: 100vh` is not referenced. It is also used by Grid so does not need to be altered.

Three new, related,`grid` properties are added. The use of a single [fraction unit](https://css-tricks.com/snippets/css/complete-guide-grid/#fr-unit) `1fr` ensures the first child element of `page-container` (in this case `content-wrap`) will fill all the remaining space that the `auto` height of the second child element `footer` does not take up.

And that’s all there is to it! Now browsers that support Grid will use the code within the feature query, while still fully supporting browsers that don’t. This even allows for single components to add Grid one at a time — a team can see how straightforward the process is without a huge time investment.

Hopefully this illustrates the incremental approach that can be taken to using Grid.

#### More complex uses

The power of what Grid offers is best seen in the more complex examples [written by Natalya](https://open.nytimes.com/bootstrap-to-css-grid-87b3f5f830e4) that inspired this update article. This shows the power of what Grid can offer when used at a larger scale.

### Quick tips

The fallback code can be tested without access to an older browser or emulator. Temporarily change`@supports (display: grid)` to a non-existent value, for example `gridNO`, so the fallback code is used.

Firefox provides some great tools that Chrome currently doesn’t. These are the “Grid Display Settings” activated within the “Inspector” tab. These settings help to visually illustrate how Grid is being executed, which is great for complex layouts.

![Image](https://cdn-media-1.freecodecamp.org/images/P2Ilh7vTFUoXlcn31P1q1rfT5LcWOV4iLkBV)
_Firefox dev tools under Inspector_

Finally, I was inspired by a statement made by Rachel Andrew:

> It shouldn’t look the same in all browsers, it should be a good experience in all browsers.

The default of many companies is to strive for a duplicate experience in every browser. But is it worth considering that on older, slower browsers, a simpler approach might actually be a better experience?

Thanks for reading ? I hope that this helps inspire you to try using Grid not just in greenfield projects, but also alongside anything you might be using today!

### Resources

* [From Bootstrap to CSS Grid](https://open.nytimes.com/bootstrap-to-css-grid-87b3f5f830e4)
* [Keeping the Footer at the Bottom with CSS-Grid](https://dev.to/niorad/keeping-the-footer-at-the-bottom-with-css-grid-15mf)
* [A Complete Guide to Grid](https://css-tricks.com/snippets/css/complete-guide-grid/)
* [CSS Grid Layout and Progressive Enhancement](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout/CSS_Grid_and_Progressive_Enhancement)
* [Using CSS Grid: Supporting Browsers Without Grid](https://www.smashingmagazine.com/2017/11/css-grid-supporting-browsers-without-grid/)

Here are a couple of other things I’ve written recently:

* [Using Pa11y CI and Drone as accessibility testing gatekeepers](https://hackernoon.com/using-pa11y-ci-and-drone-as-accessibility-testing-gatekeepers-a8b5a3415227)
* [Mocking HTTP requests with Nock](https://codeburst.io/testing-mocking-http-requests-with-nock-480e3f164851)

