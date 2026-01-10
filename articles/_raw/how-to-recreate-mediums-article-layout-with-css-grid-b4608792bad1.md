---
title: How to recreate Medium’s article layout with CSS Grid
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-28T18:19:57.000Z'
originalURL: https://freecodecamp.org/news/how-to-recreate-mediums-article-layout-with-css-grid-b4608792bad1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*YgYXxuC1tzrUdurfhirtww.png
tags:
- name: coding
  slug: coding
- name: CSS
  slug: css
- name: Design
  slug: design
- name: responsive design
  slug: responsive-design
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Per Harald Borgen

  When people think of CSS Grid they normally envision image grid layouts and full
  web pages. However, CSS Grid is actually a superb technology for laying out articles
  as well, as it allows you to do things which previously was tri...'
---

By Per Harald Borgen

When people think of CSS Grid they normally envision image grid layouts and full web pages. However, CSS Grid is actually a superb technology for laying out articles as well, as it allows you to do things which previously was tricky to achieve.

In this tutorial, I’ll explain how to recreate the famous Medium article layout using CSS Grid.

Note: I’ve also been part of creating a free 13-part CSS Grid course at Scrimba. Get access to the course [here](https://scrimba.com/g/gR8PTE?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gR8PTE_recreate_medium_layout_article).

![Click the image to get to the full CSS Grid course.](https://cdn-media-1.freecodecamp.org/images/1*nKjp3EQrrQidw76w0qqB9A.png)
_[Click here to get to the full CSS Grid course.](https://scrimba.com/g/gR8PTE?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=gR8PTE_recreate_medium_layout_article)_

In the course, my colleague [Magnus Holm](https://medium.com/u/1a7998d688dd) will go through how to create an article layout using CSS Grid. So if you prefer watching instead of reading, be sure to check out his screencast.

### The content

We’re going to start off with a basic HTML file, which contains the type of content you’ll typically find in a Medium article. For example title, paragraphs, subtitles, images, quotes and so forth. Here’s an outtake:

```html
<article>

<h1>Running any NPM package in the browser locally</h1>

<p>JavaScript has never had any official solution for distributing packages, and every web platform (Rails, Django etc) has their own idea of how to structure and package JavaScript. In the last few years, NPM has started becoming the canonical way of distribution, with Webpack as the build system, but there’s no way to load NPM packages in the browser without a server-side component.</p>

<blockquote>

<p>Scrimba is a platform for interactive coding screencast where           
you can run the code at any moment in time.</p>

</blockquote>

<figure>

<img src="https://mave.me/img/projects/full\_placeholder.png">

</figure>

```

If you open this file in a website without adjusting any layout it’ll look like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*78oGaexa4dc4cox9b3TIwA.png)

Not particularly elegant. So let’s fix it with CSS Grid. We’ll do it step by step so that it’ll be easy for you to follow.

### Basic setup for margins

The first thing we need to do is turn the whole `article` tag into a grid and give it at least three columns.

```css
article {  
    display: grid;  
    grid-template-columns: 1fr 740px 1fr;  
}

```

The first and last columns are responsive and act as margins. They’ll contain white space in most cases. The middle column is fixed at 740 pixels and will hold the content of the article.

Notice that we’re not defining the rows as they’ll simply be as tall as they need to be in order to fit their content. Each content block in the article (paragraph, image, title) will get its own row.

The next step is to make sure all the content in the grid starts at the second column line by default.

```css
article > \* {  
    grid-column: 2;  
}

```

We now have the following result:

![Image](https://cdn-media-1.freecodecamp.org/images/1*7OmrcS4aCFyiqPBK93IpJg.png)

We can instantly see that this looks better, as the white space on each side makes the text easier to read.

However, this effect could have been achieved just as easily using by setting the left and right `margin` property to auto. So why use CSS Grid?

Well, the problem arises when we want to mimic Medium’s image features. For example creating full-width images, like this one:

![Image](https://cdn-media-1.freecodecamp.org/images/1*Tv8dyhSJfSjtcevJ3rfK6g.jpeg)

If we had used `margin: 0 auto` this would have forced us to apply negative margins to the images to make them take up the entire website width, which is hacky.

With CSS Grid though, this becomes a piece of cake, as we’ll simply use columns to set the width. To make our image take up the entire width we’ll just tell it to span from the first to the last column line.

```css
article > figure {  
    grid-column: 1 / -1;  
    margin: 20px 0;  
}

```

We’ve also set some margin on the top and bottom. And then we have a nice full-width image:

![Image](https://cdn-media-1.freecodecamp.org/images/1*50nsmqw-saQJXQNb0nuhnA.png)

### Expanding with more columns

However, this doesn’t get us all the way, as Medium has a few other layouts which we need to account for. Let’s look at a couple of them:

#### Mid-sized images

This is the image option in between the normal one and the full width one, which we’ll call a _mid-sized_ one. It looks like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*kcNKt8kvMpl3c590yOMQpg.jpeg)

  
**_NOTE: I_**_f you’re watching on mobile, this image is identical to the full width one. In this article, we focus on the desktop layout only._

This will require at least two new columns to our layout.

#### Quotes

In addition, Medium also places a **vertical line** on the left-hand side of the article if you add a quote:

← Notice the vertical line. We’ll need to add an extra column to our grid because of it.

This requires a tiny column on the left-hand side of the grid. To make things symmetric, we’ll also add a similar column on the right-hand side.

So to support both **quotes** and **mid-sized images** we’ll need to split the entire width into seven columns instead of three, like this:

```css
article {  
    display: grid;  
    **grid-template-columns: 1fr 1fr 10px 740px 10px 1fr 1fr;**  
}

```

If we use the Chrome inspector we can actually see the underlying grid lines (see image below). Plus, I’ve added pointers to make it easier to recognise the different columns.

![I’ve added pointers to make it easier to recognise the different columns.](https://cdn-media-1.freecodecamp.org/images/1*YgYXxuC1tzrUdurfhirtww.png)

  
I’ve added pointers to make it easier to recognise the different columns.

The first thing we need to do it to make all default items to start at the fourth column line instead of the second one.

```css
article > \* {  
    grid-column: 4;  
}

```

Then we can create the _mid-sized_ image by doing:

```css
article > figure {  
    grid-column: 2 / -2;  
    margin: 20px 0;  
}

```

Here’s how that looks with the Chrome inspector activated:

![Image](https://cdn-media-1.freecodecamp.org/images/1*JabCqoB2CfZzy7toJcAj3A.png)

The _quotes_ are easily created by doing the following:

```css
article > blockquote {  
    grid-column: 3 / 5;  
    padding-left: 10px;  
    color: #666;  
    border-left: 3px solid black;  
}

```

We make it span from the third to the third to the fifth column line. We’re also adding `padding-left: 10px;` so that the text will seem to start at the fourth column line (the third column is 10 pixels wide as well). Here’s how it looks on the grid.

![Image](https://cdn-media-1.freecodecamp.org/images/1*SiTYghcUyboIplQOfFQTqA.png)

### **Sidemarks**

Now there’s one last thing we need to support. Medium has a pretty nice way of signalling which content in the article is most highlighted. The text turns into green, and it gets a _Top highlight_ on the right hand side.

![Image](https://cdn-media-1.freecodecamp.org/images/1*LUik3S2fM6I5P0b_k8EmpQ.png)

The _Top highlight_ text element would be a nightmare to create if we’d used `margin: 0 auto;` instead if CSS Grid. This is because the element acts different from all the other elements in the article. Instead of appearing on a new line, it’s suppose to appear on the right hand side of the previous element. If we didn’t use CSS Grid we’d probably have to start messing with `position: absolute;` to make this work.

But with CSS Grid it’s super simple. We’ll just make that kind of element start on the fourth column line.

```css
.aside {  
    grid-column: 5;  
}

```

That’ll automatically make it place itself to the right of the article:

![Note: I haven’t highlighted the text in green, as that’s got nothing to do with CSS Grid.](https://cdn-media-1.freecodecamp.org/images/1*_6JkoriZRy1bpDDGc-YPig.png)

  
Note: I haven’t highlighted the text in green, as that’s got nothing to do with CSS Grid.

And that’s it! We’ve now recreated most of Medium’s article layout using CSS Grid. And it was actually pretty easy. Note however that we’ve not touched responsiveness, as that requires a whole new article in itself.

Check out [this Scrimba playground to look at all the code.](https://scrimba.com/c/cedLJfW?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gR8PTE_recreate_medium_layout_article)

---

Thanks for reading! My name is Per Borgen, I'm the co-founder of [Scrimba](https://scrimba.com?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gR8PTE_recreate_medium_layout_article) – the easiest way to learn to code. You should check out our [responsive web design bootcamp](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gR8PTE_recreate_medium_layout_article) if want to learn to build modern website on a professional level.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/bootcamp-banner.png)
_[Click here to get to the advanced bootcamp.](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=gR8PTE_recreate_medium_layout_article)_

