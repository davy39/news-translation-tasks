---
title: How to make your HTML responsive by adding a single line of CSS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-08T05:37:03.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-your-html-responsive-by-adding-a-single-line-of-css-2a62de81e431
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Bx0gNW69lAXaSRqRw0_8dw.jpeg
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Per Harald Borgen

  In this article, I’ll teach you how to use CSS Grid to create a super cool image
  grid which varies the number of columns with the width of the screen.

  And the most beautiful part: the responsiveness will be added with a single li...'
---

By Per Harald Borgen

In this article, I’ll teach you how to use CSS Grid to create a super cool image grid which varies the number of columns with the width of the screen.

And the most beautiful part: **the responsiveness will be added with a single line of CSS.**

This means we don’t have to clutter up the HTML with ugly class names (i.e. `col-sm-4`, `col-md-8`) or create media queries for every single screen size.

If you want to learn to build responsive websites on a professional level, you can consider checking out [Scrimba's responsive web design bootcamp](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gresponsive_single_line_responsive), as it takes students from beginner to advanced through 15 hours of interactive tutorials.

Now let’s jump into it!

### The setup

For this article, we’ll continue on with the grid we used in [my first CSS Grid article.](https://medium.freecodecamp.org/learn-css-grid-in-5-minutes-f582e87b1228) Then we’ll add the images at the end of the article. Here’s how our initial grid looks:

![Image](https://cdn-media-1.freecodecamp.org/images/1*fJNIdDiScjhI9CZjdxv3Eg.png)

Here’s the HTML:

```html
<div class="container">  
  <div>1</div>  
  <div>2</div>  
  <div>3</div>  
  <div>4</div>  
  <div>5</div>  
  <div>6</div>  
</div>

```

And the CSS:

```css
.container {  
    display: grid;  
    grid-template-columns: 100px 100px 100px;  
    grid-template-rows: 50px 50px;  
}

```

Note: the example also has a little bit of basic styling, which I won’t go into here, as it’s got nothing to do with CSS Grid.

If this code confuses you, I’d recommend you to read my [Learn CSS Grid in 5 minutes](https://medium.freecodecamp.org/learn-css-grid-in-5-minutes-f582e87b1228) article, where I explain the basics of the layout module.

Let’s start by making the columns responsive.

### Basic responsiveness with the fraction unit

CSS Grid brings with it a whole new value called a fraction unit. The fraction unit is written like `fr`, and it allows you to split the container into as many fractions as you want.

Let’s change each of the columns to be one fraction unit wide.

```css
.container {  
    display: grid;  
    grid-template-columns: 1fr 1fr 1fr;  
    grid-template-rows: 50px 50px;  
}

```

What happens here is that the grid splits the entire width into three fractions and each of the columns take up one unit each. Here is the result:

![Image](https://cdn-media-1.freecodecamp.org/images/1*JgGPqT2AfFNDD8DhG2wPdQ.gif)

If we change the `grid-template-columns` value to`1fr 2fr 1fr`, the second column will now be twice as wide as the two other columns. The total width is now four fraction units, and the second one takes up two of them, while the others take up one each. Here’s how that looks:

![Image](https://cdn-media-1.freecodecamp.org/images/1*cpfokc1HBgCwOTNhRU9SHg.gif)

In other words, the fraction unit value makes it super easy for you to change the width of the columns.

### Advanced responsiveness

However, the example above doesn’t give us the responsiveness we want, as this grid will always be three columns wide. We want our grid to vary the number of columns with the width of the container. To achieve that, you’ll have to learn three new concepts.

#### repeat()

We’ll start with the `repeat()` function. This is a more powerful way of specifying your columns and rows. Let’s take our original grid and change it to using repeat():

```css
.container {  
    display: grid;  
    grid-template-columns: repeat(3, 100px);  
    grid-template-rows: repeat(2, 50px);  
}

```

In other words, `repeat(3, 100px)` is identical to `100px 100px 100px`. The first parameter specified how many columns or rows you want, and the second specifies their width, so this will just give us the exact same layout as we started out with:

![Image](https://cdn-media-1.freecodecamp.org/images/1*fJNIdDiScjhI9CZjdxv3Eg.png)

#### auto-fit

Then there’s auto-fit. Let’s skip having a fixed amount of columns, and rather replace 3 with `auto-fit`.

```css
.container {  
    display: grid;  
    grid-gap: 5px;  
    grid-template-columns: repeat(auto-fit, 100px);
    grid-template-rows: repeat(2, 100px);  
}

```

This results in the following behaviour:

![Image](https://cdn-media-1.freecodecamp.org/images/1*vLZ9RD3dt0Q3hCieYfRuMg.gif)

The grid now varies the number of columns with the width of the container.

It simply tries to fit as many 100px wide columns into the container as possible.

However, if we hard code all columns to be exactly 100px, we’ll never get the flexibility we want, as they’ll rarely add up to the full width. As you can see on the gif above, the grid often leaves white space on the right-hand side.

#### minmax()

The final ingredient we need in order to fix this is called `minmax()`. We’ll simply replace 100px with `minmax(100px, 1fr)`. Here’s the final CSS.

```css
.container {  
    display: grid;  
    grid-gap: 5px;  
    grid-template-columns: repeat(auto-fit, minmax(100px, 1fr));
    grid-template-rows: repeat(2, 100px);  
}

```

Notice that all the responsiveness happens in a single line of CSS.

This results in the following behaviour:

![Image](https://cdn-media-1.freecodecamp.org/images/1*1FOrkyNbaabo3_LJxcdDbg.gif)

And as you can see that works perfectly. The `minmax()` function defines a size range greater than or equal to **min** and less than or equal to max.

So the columns will now always be at least 100px. However, if there is more available space, the grid will simply distribute this equally to each of the columns, as the columns turn into a fraction unit instead of 100 px.

#### Adding the images

Now the final step is to add the images. This has nothing to do with CSS Grid, but let’s still look at the code.

We’ll start off by adding an image tag inside of each of the grid items.

```html
<div>
    <img src="img/forest.jpg"/>
</div>

```

To make the image fit into the item, we’ll set it to be as wide and tall as the item itself, and then use `object-fit: cover;`. This will make the image cover its entire container, and the browser will crop it if it’s needed.

```css
.container > div > img {  
    width: 100%;  
    height: 100%;  
    object-fit: cover;  
}

```

Which ends up like the following:

![Image](https://cdn-media-1.freecodecamp.org/images/1*jCNANupl0ECRzF6cOLuWNw.gif)

And that’s it! You now know one of the most complex concepts in CSS Grid, so give yourself a pat on the back.

#### Browser support

Before we end, I also need to mention browser support. At the time of writing this article, [93% of global website traffic supports CSS Grid](https://caniuse.com/#feat=css-grid), and it’s climbing. It's becoming more and more clear that Grid is turning into a must-have skill for front-end developers. Much like what has happened with CSS Flexbox a few years ago.

If you want to learn Flexbox, Grid and responsive design once and for all, you should check out the [responsive web design bootcamp on Scrimba](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gresponsive_single_line_responsive). It'll take your beginner to advanced through interactive tutorials that are easy to follow.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/bootcamp-banner.png)
_[Click here to get to the advanced bootcamp.](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=gresponsive_single_line_responsive)_

---

Thanks for reading! My name is Per Borgen, I'm the co-founder of Scrimba, an interactive learning platform for learning to code.

