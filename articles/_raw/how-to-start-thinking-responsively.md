---
title: 'How to think responsively: a responsive web design tutorial'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-09-03T14:12:13.000Z'
originalURL: https://freecodecamp.org/news/how-to-start-thinking-responsively
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca084740569d1a4ca492b.jpg
tags:
- name: responsive design
  slug: responsive-design
- name: Web Design
  slug: web-design
seo_title: null
seo_desc: 'By Kevin Powell

  For a long time, responsive web design was a trend. Now it''s simply a reality.
  If we think of a website, we don''t really have to say "a responsive website", it''s
  just an expected reality.

  This means that when we are putting together a...'
---

By Kevin Powell

For a long time, responsive web design was a trend. Now it's simply a reality. If we think of a website, we don't really have to say "a responsive website", it's just an expected reality.

This means that when we are putting together a website, it must be built keeping in mind how it will look on different screen sizes. With how things are trending today, there must be a strong emphasis on the mobile experience.

*R\_ecently*, I *launched a comprehensive and detailed course on*\_ ***Scrimba*** *called* [***The Responsive Web Design Bootcamp***](https://scrimba.com/g/gresponsive)***.*** *This course covers all the technical and architectural concepts about responsive web design in great depth****.*** *This blog is based on one of* the *six* sections of the course\_:\_ ***Start****ing* ***to think responsively****.*

# Getting into the responsive frame of mind

This module of the course focuses on the importance of thinking about responsiveness before you write a single line of code, as well as some other essentials of building a responsive website:

1. How to approach a layout
    
2. CSS Units
    
3. Flexbox basics
    
4. Media query basics
    

While we use a few simple exercises to get started, the main focus of this module of the course is to build out a fully responsive 3-page website. We use it both to reinforce what we've already learned, as well as introduce a few new things into the mix.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/01.png align="left")

In this post, we'll be exploring the concepts that I explore in this module of the course that are listed above, from a dive into `em` vs `rem`, a look at the basics of flexbox and media queries, as well as overviews of some of the projects we build out in the course.

# CSS Units

The first and most fundamental concept in building a responsive web design are the units that we use to set many of our properties with.

In lesson 2 we are going to learn what are some of the CSS units available and how they are different from each other. Most importantly, we'll learn which ones to use as per the requirements.

There are three major types of CSS units available: Absolute Units, Percentage Units, and Relative Units.

## Absolute Units

The absolute units are also called fixed units.

The length expressed in any of the absolute units will appear in exact same size (hence why we called them fixed, they are a fixed size).

While `px` (pixels) are the unit that are most common, in CSS we can also use `pt`, `pc`, `in`, `cm`, `mm`, and many more, though I wouldn't really recommend those unless you're styling something for print.

`px` are a little more complicated than you might think. In the old days, a `px` was related to a pixel on your screen, but now CSS uses something called the *reference pixel* which makes it a fixed size, independent of device resolution.

## Percentages

Lessons 3-5 of the course dive into percentage. Percentage, as its name suggests, is often used to define the size as relative to the size of its parent.

This is a little different than absolute units, and takes a little getting used to. When we set the width of something using `px`, we are telling that element how big it should be. For example:

```css
.box {
    width: 500px;
    /* this element will be 500px in width */
}
```

Whereas, if we use a percentage, it's not as straight forward:

```css
.box {
    width: 80%;
    /* this element will have a width of 80% */
}
```

But, what is that `80%` of? It's of it's parent. When we use percentage for `width`, `margin`, or `padding` it is always looking at the *width of it's parent* (yes, even for `margin` and `padding` on the top and bottom).

We'll often use percentage to define the width's of elements, as it let's them be more flexible, which is essential when putting together a responsive design.

During the course, we will learn this with the help of following example:

![Image](https://www.freecodecamp.org/news/content/images/2019/08/02.png align="left")

If we keep the width of the container for the above layout to any fixed number, lets say `500px`, we know that it will look okay unless the size of the screen is less than `500px`.

In this scenario, if we want our layout to adjust as per the size of the viewport, what we can do is set the width in percentage which can be `100%` or less.

```css
.container { 
    width: 70%; 
    ...
}
```

As we updated the width to be 70% of the width of the parent container, we can now see it adjusts itself to the size of the screen:

![Image](https://www.freecodecamp.org/news/content/images/2019/08/03.jpeg align="left")

There is a problem though. Right now if we put an image inside our container, it looks like this (if the image has a width that is too big):

![Image](https://www.freecodecamp.org/news/content/images/2019/08/04.png align="left")

The problem is, unless we specify differently, images will be their actual size. To fixthis, we could apply CSS on image itself so that it starts defaulting to the size of its container.

```css
.img { 
    width: 100%;
}
```

And, as we do this, we can see that the image starts defaulting to the size of its parent container.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/05-1.jpeg align="left")

### Maximum and minimum sizes

While the above solution is great, it can actually cause the image to become bigger than it's actual size. If this happens, it will quickly start to lose quality.

To help fix that, we can instead use `max-width`.

```css
.img { 
    max-width: 100%;
}
```

This means that the images maximum width is 100% of it's parent, but that it is allowed to be smaller.

In the course, I also explore other similar properties, such as `min-width`, and `min-height` and `max-height`, which all set upper and lower limits on the size of an element.

These all take precedent over the `width` of an element as well, which is always important to remember!

## CSS Units - Relative Units

Relative units in CSS are always relative on the size of something else. Some units will look at the `font-size` of another element (or that element), while others will look at the size of the view port.

In the course, I start by introducting the two which are relative to `font-size`, the **em** and **rem**.

## The `em` unit

When you declare the `font-size` of an element, if you use `em`s, it will be relative to the parent's `font-size`.

For example, we have the following HTML code where we have some `li` elements which have few parent elements.

```html
<body> 
    <section class='class-one'>
        <div class="container">
            <ul>
                <li>Item 1</li>
                <li>Item 2</li>
                <li>Item 3</li>
            </ul>
        </div>
    </section>
</body>
```

And, we have the following CSS with the above HTML:

```css
body { 
    font-size: 25px; ...
}

ul { 
    /* 1.5em = 25 * 1.5 = 37.5  */ 
    font-size: 1.5em;
}
```

In the above case, the `ul` will take its `font-size` from its parent and apply on its `li` elements using the relative `1.5em`.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/06.jpeg align="left")

In case of *em* unit, we have to remember that it will default to the `font-size` of its immediate parent, which means that if in our above example, we change the `font-size` of class `container` to be `15px`, then the `ul` will start to size relative `15px`.

### Cascading effect of `em`s

One of the reasons I don't like to set `font-size` in `em` is because of the risk of it being hit by a cascading effect. For example, if we use the above example, but add in a `font-size` to the `li` elements, we start to run into problems!

```css
body { 
    font-size: 25px; ...
}

ul { 
    font-size: 1.5em;
}

li {
 	font-size: 1.5em;   
}
```

In this case, the `li` looks at it's parent, which then looks at the body, so we get a total font-size of 56.25px (1.5 x 1.5 x 25px). Things can quickly get out of control!

## The rem unit

As we can see, using `em` can be confusing at times since it takes it's size from its parent which may have its `font-size` defined also in `em` and that would create a cascading effect.

The `rem` unit is short for *Root Em*, meaning that it only looks at the `font-size` of the root element. In the case of websites, the root element is always the `html` element.

So if you set the font-size of something in `rem` it is *always* relative to the `font-size` of the `html` element and nothing else, making it much easier to use.

## Is it ever a good idea to use `em`s?

While `em` might seem like something you might want to avoid, they can be really useful!

When setting `font-size` with `em`, it looks to the parent element, but when we set any other property using `em`, it is relative to **that element's font-size!** That's super useful for setting things like `margin` and `padding`.

If we increase the `font-size` of our selector, it will increase the `margin` or `padding` with it, and vice versa! It's super useful.

Here is a slide from the course which sums up how I like to use the two:

![Image](https://www.freecodecamp.org/news/content/images/2019/08/07.png align="left")

# Flexbox

Once we nail down the units and what they are best suited to, I turn the course toward a look at the basics of flexbox, which allows us to create responsive layouts super easily without having to rely on floats or positioning.

All elements, by default, have the `display` property of either `block` or `inline`.

**Block elements** (`div` , `header`, `footer`, `h1` -&gt; `h6`, `p`, etc.) stack on top of each other.

**Inline elements** (`a`, `strong`, `em`, `span`, etc.) stay within the flow of what is around them.

When we change their display to flex, they start aligning side by side.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/08.png align="left")

Let's see how to design a simple architecture of a typical responsive website with some columns using flexbox. The result would be the following layout:

![Image](https://www.freecodecamp.org/news/content/images/2019/08/09.png align="left")

We will will start off with the following HTML:

```html
<body>
  <div class="container">
    <h1>This is the header</h1>
    <div class="columns">
      <div class="col">
        <h2>Section 1 - Col 1</h2>
        <p>This is column 1</p>
      </div>
      <div class="col">
        <h2>Section 1 - Col 2</h2>
        <p>This is column 2</p>
      </div>
      <div class="col">
        <h2>Section 1 - Col 3</h2>
        <p>This is column 3</p>
      </div>
    </div>
    <div class="columns">
      <div class="col">
        <h2>Section 2 - Col 1</h2>
        <p>This is column 1</p>
      </div>
      <div class="col">
        <h2>Section 2 - Col 2</h2>
        <p>This is column 2</p>
      </div>
    </div>
  </div>
</body>
```

And, we can have the following CSS:

```css
.container {
  width: 90%;
  max-width: 980px;
  margin: 0 auto;
}

.columns {
  display: flex;
  margin: 1em 0;
}
```

To add background background colors to the columns, we will add couple of modifier classes and assign them to the columns:

```css
.col-bg-beige {
  background-color: beige;
  padding: 1em;
}

.col-bg-aqua {
  background-color: aqua;
  padding: 1em;
}
```

So far the page looks like this:

![Image](https://www.freecodecamp.org/news/content/images/2019/08/10.png align="left")

In the next step, we want to set the width of columns, we will define the modifier classes and assign the fixed widths inside them.

```css
.col-1 {
  width: 25%;
}
.col-2 {
  width: 50%;
}
.col-3 {
  width: 75%;
}
.col-4 {
  width: 100%;
}
```

We will assign these classes to our columns as per the layout needs such as:

%[https://codepen.io/kevinpowell/pen/XWrRqyG] 

If we want our flex columns to align with each other, we can use the following property:

```css
.columns {
  display: flex;
  justify-content: center;
}
```

*There is a lot more detail about Flexbox basics with code samples and online code editing capability in the Scrimba course* [***The Responsive Web Design Bootcamp***](https://scrimba.com/g/gresponsive)***.***

# Media Queries

Media queries allow us to declare new CSS rules that only apply in specific situations, such as different types of media (screen, print, speech), and with different media features, such as screen width, orientation, aspect ratio and much more.

The basic syntax for a media query looks like this:

`@media _media-type_` and (*media-features*) {...}

For example the piece of code below will set `background-color` to the body if it is a screen and has `min-width` of 480px.

```css
@media screen and (min-width: 480px) {  
    body {    
        background-color: aqua;  
    }
}
```

**Going back to our example from above**, if we reduce the screen size, we see that some of the columns become way more narrow and we want to fix them by making it fully responsive.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/11.png align="left")

Since we are already using flexbox, we can change the `flex-direction` property to switch the main axis, so instead of creating columns, it will create rows of content.

```css
@media screen and (max-width: 600px) {
  .columns {
    flex-direction: column;
  }
}
```

%[https://codepen.io/kevinpowell/pen/WNejJLM] 

# Designing a responsive navigation

One of my favorite places to take a look at how to apply all of the above into a realistic example is by taking a look at setting up a responsive navigation.

We will start off with writing the HTML for the navigation bar.

```html
<header>
  <div class="container container-nav">
    <div class="site-title">
      <h1>Living the social life</h1>
      <p class="subtitle">A blog exploring minimalism in life</p>
    </div>
    <nav>
      <ul>
        <li><a href="#">Home</a></li>
        <li><a href="#">About me</a></li>
        <li><a href="#">Recent posts</a></li>
      </ul>
    </nav>
  </div>
</header>
```

And then we can use flexbox, media queries, a few other little things here and there to start styling it up in our CSS.

Here is the glimpse of some of the CSS (detailed code is available in the course lessons):

```css
body {
  margin: 0;
}

.container {
  width: 90%;
  max-width: 900px;
  margin: 0 auto;
}

.container-nav {
  display: flex;
  justify-content: space-between;
}

nav ul {
  display: flex;
  justify-content: center;
  list-style: none;
  margin: 0;
  padding: 0;
}

@media (max-width: 675px) {
  .container-nav {
    flex-direction: column;
  }
    
  header {
    text-align: center;
  }
}
```

And at the end of the lessons in this section of the module, we will have a nice, simply, fully responsive navigation:

![Image](https://www.freecodecamp.org/news/content/images/2019/08/nav-1.gif align="left")

# Building out a 3-page site

## Examining the structure

With the navigation wrapped up, I jump into the full-fledge project. This is going to be a 3-page mobile responsive website.

Below you can see the pages we're buildingout, as well as a link to Adobe XD where you can check out the artboards in more detail. In the lessons, I take a look at the similarities across the different pages, and how I start planning for something like this before starting to write any code.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/13.png align="left")

*The layouts of the web pages we will be learning to design in the course:* [*https://xd.adobe.com/spec/75d448ea-569a-4b7e-721b-9bbd3b2b97b9-03e5/grid/*](https://xd.adobe.com/spec/75d448ea-569a-4b7e-721b-9bbd3b2b97b9-03e5/grid/)

## The Home page

As we can see from the image below that there are two main sections of the home page. The left side list of articles with a featured article on top, and the right hand panel with author’s info and the recent posts.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/14.png align="left")

We will wrap the whole content in `container` div and first of all create the left hand section which is a list of articles. This is going to be created with the help of `article` tags of the HTML and then we will put content inside them

```html
<div class="container">
  <main role="main">
    <article class="article-featured">
      <h2 class="article-title"></h2> <img src="" alt="" class="article-image">
      <p class="article-info"></p>
      <p class="article-body"></p>
      <a href="#" class="article-read-more"></a>
    </article>
    ...
  </main>
</div>
```

Next up we will create the right hand panel with the help of `aside` tag of the HTML.

```html
<aside class="sidebar">
  <div class="sidebar-widget">
    <h2 class="widget-title"></h2> 
    <img src="#" alt="" class="widget-image">
    <p class="widget-body"></p>
  </div>
    
    ...
</aside>
```

Before jumping into the layout itself, I like to always start with the typography. It might not be the most exciting part of writing CSS, but when the fonts and font-sizes start to change, it can have a huge impact on the layout. Starting there, then worrying about the layout makes our lives so much easier.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/15.png align="left")

With the typography in place, it's time to start working on the layout itself. While we can start with large screens and then use a media query to redesign things at smaller sizes (like we did with the navigation above), I find it much less work to work the other way around.

Mobile layouts tend to be much simpler, so by starting mobile first, we can create our layouts without too much work.

One the mobile layout is done, then it's time to add in our media query (or queries) and start working on modifying the layout for larger screens.

One thing that's *really* important is not not force yourself to have breakpoints for specific devices. It's all too common to see the same breakpoints used all the time, but really, you should be making layout changes when your layout dictates that it's needed.

I really don't care what device someone is on, or what the size of that device is. What's important is it looks good on all devices. With the amount of different devices and screen sizes today, focus on the layout itself.

In the course itself, I dive into looking at how we can figure out when a layout needs a breakpoint (often because the lines of text are getting too long!), and then we dive into a few fun extras, looking at properties such as `order`, `object-fit` to help our images adjust much easier, and fine tuning the layout.

The second and third pages are quite easy to create once the first one is done. By having looked at all the pages before starting, and naming things with classes that can be reused across each page, there are small tweaks to do here and there, but overall things move very fast.

# Conclusion

In this article, we examined some core CSS principles to designing responsive websites, from their units to media queries and flexbox. We looked at how we can set it all up for a navgation, and how to break down and analyze a bigger design.

As I mentioned off the top, all of this content is from the *Starting to think responsively* module of the course [**The Responsive Web Design Bootcamp**](https://scrimba.com/g/gresponsive).

The course itself dives much deeper into these topics and many others, from an exploration of the fundamentals of CSS, as well as deep dives into both flexbox and grid, including building out several other projects.

It is the era of *mobile-first* websites. Good news is that we can achieve everything we need using CSS. There are lots of cool resources and tools available now using which we can create beautiful mobile friendly websites without the need for frameworks or libraries. CSS has reached a *really* fun place. I really love CSS, and I hope you join me in the course where hopefully I can help you fall in love with it too!
