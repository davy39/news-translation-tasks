---
title: 'Flexbox tutorial: Learn to code a responsive navbar with CSS Flexbox'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-29T09:07:33.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-fully-responsive-navbar-with-flexbox-a4435d175dd3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*CZikqoB4iZIIrV_rAW_qdg.gif
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Per Harald Borgen

  In this article, I’ll explain how to create a navbar which adapts to various screen
  sizes using Flexbox along with media queries.

  This tutorial can also be found as an interactive screencast in my free Flexbox
  course at Scrimba.

  ...'
---

By Per Harald Borgen

In this article, I’ll explain how to create a navbar which adapts to various screen sizes using Flexbox along with media queries.

This tutorial can also be found as an interactive screencast [in my free Flexbox course at Scrimba](https://scrimba.com/g/gflexbox?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gflexbox_tutorial_article).

To read more about the course, check out [this](https://medium.freecodecamp.org/i-just-launched-a-free-full-length-flexbox-course-where-you-can-build-projects-interactively-1860e3d3c4af) article.

#### The setup

Let’s begin with the markup for a very simple navbar:

```html
<nav>  
  <ul class="container">  
    <li>Home</li>  
    <li>Profile</li>  
    <li class="search">  
      <input type="text" class="search-input" placeholder="Search">  
    </li>  
    <li>Logout</li>  
  </ul>  
</nav>

```

The `<ul>` element is our flex container and the `<li>` elements are our flex items. To turn it into a Flexbox layout we’ll do:

```css
.container {  
  display: flex;  
}

```

Which will result in the following layout:

![I’ve added some styling, but that has nothing to do with Flexbox.](https://cdn-media-1.freecodecamp.org/images/1*bEclbRvpLBeEd8oRddNFaQ.png)

  
I’ve added some styling, but that has nothing to do with Flexbox.

As you can see, we have a bit of extra space on the right-hand side. This is because Flexbox lays out the items going from left to right, and each item is only as wide as its content forces it to be.

Since the flex container by default is a block level element (and is wider than the four items) we get the gap at the end.

The reason the search items is wider than the others is because input fields are by default set to `size="20"`, which different browsers and operating systems interpret in different ways.

### Responsiveness #1

To give our navbar basic responsiveness, we’ll simply give the search item a flex value of 1.

```css
.search {  
  flex: 1;  
}

```

This results in the search item expanding and shrinking with the width of the container, meaning we won’t get the extra space in the right-hand side.

![Image](https://cdn-media-1.freecodecamp.org/images/1*BZnmPAc4fNPNGkjCPS22kw.gif)

While it makes sense to have the search item grow while the others stay fixed, you could argue that it can become too wide compared to the others. So if you prefer to have all the items grow with the width of the container instead, you can simply give all the items a `flex` value of 1.

```css
.container > li {  
  flex: 1;  
}

```

Here’s how that plays out:

![Image](https://cdn-media-1.freecodecamp.org/images/1*pXzuCWHyvuyQ3JZQPoWclA.gif)

You can also give the items different flex values, which would make them grow with different speeds. Feel free to experiment with that [in this Scrimba playground.](https://scrimba.com/c/cpJV3S3?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gflexbox_tutorial_article)

For the rest of the tutorial, we’ll continue with the first solution, where the search items are the only one with a `flex` value.

### Responsiveness #2

Our navbar works well on wide screens. However, on more narrow ones it gets into problems, as you can see here:

![Image](https://cdn-media-1.freecodecamp.org/images/1*PCmf5iZCXLYIckEjMBbv4g.gif)

At some point, it’s not viable to have all items on the same row, as the container becomes too narrow. To solve this we’ll add a media query where we’ll split our four items into two rows. The media query will kick when the screen is 600px wide:

```css
@media all and (max-width: 600px) {  
    
  .container {  
    flex-wrap: wrap;  
  }  
    
  .container > li {  
    flex-basis: 50%;  
  }

}

```

First, we allow the Flexbox layout to wrap with `flex-wrap`. This is by default set to `nowrap`, so we’ll have to change it to `wrap`.

The next thing we do it set the items’ `flex-basis` value to 50%. This tells Flexbox to make each item take up 50% of the available width, which results in two items per row, like this:

![Note: I’ve also centred the placeholder text in the search input field.](https://cdn-media-1.freecodecamp.org/images/1*Xr3MxBFPb2-GTX7cDuKbVQ.png)

  
Note: I’ve also centred the placeholder text in the search input field.

Now we have two different states. However, this layout still doesn’t work on very small screens, like mobile screens in portrait mode.

If we continue shrinking the screen, it’ll end up like the image below.

![Image](https://cdn-media-1.freecodecamp.org/images/1*k_HzX7UVF152TVc1sfbhKg.png)

What’s happened here is that the second row can’t fit two items anymore.

The logout and the search items are simply too wide, as you can’t shrink them down to below their minimum width, which is the width they need in order to fill the content inside of them.

The home and profile items are still able to appear on the same row though, so Flexbox will allow them to do so. This isn’t optimal, as we want all of our rows to behave in the same way.

### Responsiveness #3

So as soon as _one_ of the rows can’t fit two items in the width, we want _none_ of the rows to have two items in the width. In other words, on very small screens we’ll actually make navbar vertical. We’ll stack the items on top of each other.

To achieve this we simply need to change our 50% width to 100%, so that each row only fits a single item. We’ll add this breakpoint at 400px.

```css
@media all and (max-width: 400px) {  
  .container > li {  
    flex-basis: 100%;  
  }  
  .search {  
    order: 1;  
  }  
}

```

In addition to this, I’d like to place the search item at the bottom, which is why I’m also targeting the search and give it an `order` value of 1.

This results in the following:

![Image](https://cdn-media-1.freecodecamp.org/images/1*6Xgs5YcKu9Obq3dgk4qLZA.png)

The reason `order: 1;` results in the search item being placed at the bottom are because flex items by default have a value of zero, and whatever item has a higher value than that will be placed after the others.

To see how it all plays out, here’s the gif from the top of the article:

![Image](https://cdn-media-1.freecodecamp.org/images/1*CZikqoB4iZIIrV_rAW_qdg.gif)

Congrats! You now know how to create a fully responsive navbar using Flexbox and media queries.

If you’re interested in learning more about Flexbox, I’d recommend you to check out [my free course at Scrimba.](https://scrimba.com/g/gflexbox?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gflexbox_tutorial_article)

---

Thanks for reading! My name is Per Borgen, I'm the co-founder of [Scrimba](https://scrimba.com?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gflexbox_tutorial_article) – the easiest way to learn to code. You should check out our [responsive web design bootcamp](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gflexbox_tutorial_article) if want to learn to build modern website on a professional level.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/bootcamp-banner.png)
_[Click here to get to the advanced bootcamp.](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=gflexbox_tutorial_article)_


