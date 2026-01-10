---
title: How to implement horizontal scrolling using Flexbox
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-05T04:36:23.000Z'
originalURL: https://freecodecamp.org/news/horizontal-scrolling-using-flexbox-f9d16817f742
coverImage: https://cdn-media-1.freecodecamp.org/images/1*8MiXDWg3C4evyq1WtRWTcw.png
tags:
- name: CSS
  slug: css
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Software Engineering
  slug: software-engineering
- name: technology
  slug: technology
seo_title: null
seo_desc: 'Horizontal scrolling using Flexbox

  If you create websites, chances are you have been asked to create a horizontal scrolling
  component. It is extremely easy to implement this using just a few lines of Flexbox.
  Let me show you how.

  Project Layout

  We ne...'
---

![Image](https://cdn-media-1.freecodecamp.org/images/4d5EkVE0IxLXQkRlSL3MOAYRnKtvmaqpqR2M)
_Horizontal scrolling using Flexbox_

If you create websites, chances are you have been asked to create a horizontal scrolling component. It is extremely easy to implement this using just a few lines of Flexbox. Let me show you how.

#### Project Layout

We need to create a container that will contain all the images that we want to scroll. Here is the code:

```html
<div class="container">
  <img src="images/bhutan1.jpg" alt="Bhutan" />
  <img src="images/bhutan2.jpg" alt="Bhutan" />
  <img src="images/bhutan3.jpg" alt="Bhutan" />
  <img src="images/bhutan4.jpg" alt="Bhutan" />
  <img src="images/bhutan5.jpg" alt="Bhutan" />
  <img src="images/bhutan6.jpg" alt="Bhutan" />
  <img src="images/bhutan7.jpg" alt="Bhutan" />
</div>

```

#### Styling the Project

Next step is to add styling so that the container scrolls horizontally. To do this I make the container display as Flexbox. In addition I am setting the overflow-x value to auto. Here is the style:

```css
.container {
  display: flex;
  overflow-x: auto;
}

```

This is what the horizontal scroll looks like:

![Image](https://cdn-media-1.freecodecamp.org/images/OtTK-LibpJ6mcBOeHSmI2wIcXrlzMzzw5VND)
_The initial version of our horizontal scroll_

That does provide our requirement of a horizontal scroll area. I am not satisfied with how it looks. There are three things I want to change:

* Add white space between the images
* Get rid of the horizontal scrollbar
* Place the scroller in the middle of the screen

The images are touching. Let’s add some white space between them. Here is the CSS for this:

```css
.container img {
  margin-right: 15px;
}

```

Next I want to get rid of the horizontal scrollbar which I can do with this code:

```css
.container::-webkit-scrollbar {
  display: none;
}

```

The last change that I want to do is to center the scrolling are in the center of the screen. By default, the hight of the html is the height of the elements. I need to make the height to be 100% of the viewport. Flexbox provides a way to center items with the align-items setting. To use this functionality, I am going to convert the `body` to display as Flexbox. Here is the code that I am going to add for the body:

```css
body {
  display: flex;
  align-items: center;
  height: 100vh;
}

```

With these changes, here is what our final horizontal scroll area looks like.

![Image](https://cdn-media-1.freecodecamp.org/images/qJCD4OP64IdYdHTGPKnFVBKhFLrkiIWDrKSe)

### Conclusion

It is very easy to create a horizontal scroll area using Flexbox. Thanks for reading.

Here are some more articles you might like to read:

[**Here are 5 Layouts That You Can Make With FlexBox**](https://hackernoon.com/here-are-5-layouts-that-you-can-make-with-flexbox-6ca1e941f33d)  
[_The CSS Flexible Box Layout — Flexbox — provides a simple solution to the design and layout problems designers and…_hackernoon.com](https://hackernoon.com/here-are-5-layouts-that-you-can-make-with-flexbox-6ca1e941f33d)

[**Think outside the box with CSS shape-outside**](https://hackernoon.com/mastering-css-series-shape-outside-44d626270b25)  
[_CSS is based off a box model. If you have an image that is a circle that you want to wrap text around, it will wrap…_hackernoon.com](https://hackernoon.com/mastering-css-series-shape-outside-44d626270b25)

[**Learn the CSS border-radius property by building a calculator**](https://medium.freecodecamp.org/learn-css-border-radius-property-by-building-a-calculator-53497cd8071d)  
[_Have you ever seen a button on a web page that has rounded edges? Have you ever seen an image that fits within a…_medium.freecodecamp.org](https://medium.freecodecamp.org/learn-css-border-radius-property-by-building-a-calculator-53497cd8071d)

