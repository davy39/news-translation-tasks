---
title: How to create a simple form with CSS Grid
subtitle: ''
author: Zell Liew
co_authors: []
series: null
date: '2018-11-08T04:51:59.000Z'
originalURL: https://freecodecamp.org/news/creating-a-simple-form-with-css-grid-a99a2706bb0f
coverImage: https://cdn-media-1.freecodecamp.org/images/0*ZwG-auUyjJiPLU3P.png
tags:
- name: CSS
  slug: css
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: UI
  slug: ui
- name: UX
  slug: ux
seo_title: null
seo_desc: 'You learned to create a simple form with Flexbox in the previous article.
  Today, you’ll understand how to create the same thing with CSS Grid.

  Here’s what we’re building:


  Building the form with CSS Grid

  From the picture above, we know the form conta...'
---

You learned to create a simple form with Flexbox in the [previous article](https://zellwk.com/blog/simple-form-with-flexbox). Today, you’ll understand how to create the same thing with CSS Grid.

Here’s what we’re building:

![Image](https://cdn-media-1.freecodecamp.org/images/h4IM1DtbqMnvHdQDWjbAjyTB8HFHB8hBc3KV)

### Building the form with CSS Grid

From the picture above, we know the form contains two elements:

1. An email field
2. A submit button

Here’s the HTML:

```
<form>   <input type="email" name="email">   <button type="submit">Send</button> </form>
```

To build the form with CSS Grid, you need to set the parent’s `display` property to `grid`.

```
form {   display: grid; }
```

Here’s what you get:

![Image](https://cdn-media-1.freecodecamp.org/images/wWF5gknxOICW0uVNJULglsbw9Tq8HjUXy7CS)

Why did we get two rows?

We get two rows because we did not specify the number of columns for the grid. Browsers will always default to one column.

For this form, we need to set two columns.

1. The first column should expand to fill up any available space
2. The second column should be sized according to its contents

For the first column, we can use the `fr` unit. For the second column, we can use `auto`.

```
form {   display: grid;   grid-template-columns: 1fr auto; }
```

With this, you have completed form’s layout. Here’s a Codepen for you to play around with:

[Simple form with CSS Grid](https://codepen.io/zellwk/pen/qMLErJ/) by Zell Liew ([@zellwk](https://codepen.io/zellwk)) on [CodePen](https://codepen.io/).

### When elements are of unequal height

We will simulate elements of unequal height by substituting the `button`’s text with an SVG. [This is the same as what we’ve done in the previous article](https://zellwk.com/blog/simple-form-with-flexbox).

```
<form action="#">   <input type="email" placeholder="Enter your email">   <button type="button"><svg> <!-- a smiley icon --> </svg></button> </form>
```

![Image](https://cdn-media-1.freecodecamp.org/images/2fkg2F6SaWOZfNDsonfP1joVRlDl-eIlHjCs)

Notice the `input`’s height increases to fit the large SVG icon too! Once again, we don’t have to write any extra code. This happens because grid items are stretched vertically to fill up any available space.

If you want to change this behavior, you can change the `align-items` property to either `start`, `end`, or `center`.

![Image](https://cdn-media-1.freecodecamp.org/images/TZFrmkspxaoTilvhtb7K2CqB9qhDZLiwSgaM)

Here’s a Codepen for you to play around with:

[Simple form with CSS Grid (with SVG Button)](https://codepen.io/zellwk/pen/jvXEzm/) by Zell Liew ([@zellwk](https://codepen.io/zellwk)) on [CodePen](https://codepen.io/).

### Wrapping up

CSS Grid makes it easy to create layouts. It doesn’t have to be used for macro layouts. It can also be used for micro layouts like the form example you’ve seen here.

Have fun with CSS Grid!

Thanks for reading. Did this article help you in any way? If you did, [I hope you consider sharing it](http://twitter.com/share?text=Creating%20a%20simple%20form%20with%20CSS%20Grid%20by%20@zellwk%20?%20&url=https://zellwk.com/blog/simple-form-with-css-grid/&hashtags=). You might help someone out. Thank you!

This article was originally posted on [my blog](https://zellwk.com/blog/simple-form-with-css-grid).  
Sign up for my [newsletter](https://zellwk.com/) if you want more articles to help you become a better front-end developer.

