---
title: 'CSS Grid tutorial: Learn to prototype websites quickly with CSS Grid'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-30T19:23:33.000Z'
originalURL: https://freecodecamp.org/news/how-to-prototype-websites-quickly-with-css-grid-ffc9cba08583
coverImage: https://cdn-media-1.freecodecamp.org/images/1*F1NggJ-SsRSq306y3vCong.png
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: UX
  slug: ux
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Per Harald Borgen

  The CSS Grid module is a fantastic tool for creating mockups of websites. It allows
  you to experiment with the layout faster than any other system I’ve tried.

  In this article, I’ll teach you how.

  I’ve also created a free CSS Grid...'
---

By Per Harald Borgen

The CSS Grid module is a fantastic tool for creating mockups of websites. It allows you to experiment with the layout faster than any other system I’ve tried.

In this article, I’ll teach you how.

I’ve also created a free CSS Grid course. [Click here to get full access to it.](https://scrimba.com/g/gR8PTE?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gR8PTE_prototype_websites)

Alternatively, check out [this article](https://medium.freecodecamp.org/heres-my-free-css-grid-course-merry-christmas-3826dd24f098), which explains what you’ll learn throughout the course:

[**Want to learn CSS Grid? Here’s my free full-length course. Merry Christmas!**](https://medium.freecodecamp.org/heres-my-free-css-grid-course-merry-christmas-3826dd24f098)

### Our grid

We’re going to start out with a very basic grid which mimics a classic website:

![I’ve styled our example a little bit, but that has nothing to do with CSS Grid, so I’m leaving that out.](https://cdn-media-1.freecodecamp.org/images/1*F1NggJ-SsRSq306y3vCong.png)

  
I’ve styled our example a little bit, but that has nothing to do with CSS Grid, so I’m leaving that out.

First, I’ll explain the HTML and CSS we need to get this working, which I’ve broken down to four parts. Once you’ve understood those, we’ll move on to the layout experimentations.

If you’re completely new to CSS Grid, you might want to skim through [my 5-minute introduction article on the subject.](https://medium.freecodecamp.org/learn-css-grid-in-5-minutes-f582e87b1228)

#### 1. The markup

The first thing we need is a little bit of HTML. A container (the element we’ll turn into a grid) and the items (header, menu, content, footer).

```html
<div class="container">  
  <div class="header">HEADER</div>  
  <div class="menu">MENU</div>  
  <div class="content">CONTENT</div>  
  <div class="footer">FOOTER</div>  
</div>

```

#### 2. Basic setup in CSS

Then we need to set up our grid and specify how many rows and columns we need. Here’s the first CSS for doing that:

```css
.container {  
    display: grid;      
    grid-template-columns: repeat(12, 1fr);  
    grid-template-rows: 50px 350px 50px;  
    grid-gap: 5px;  
}

```

I’m going to add more later, but I first want you to understand this.

Here’s what the above code says: create a grid with twelve columns, each being one fraction unit wide (1/12 of the total width). Create three rows, where the first will be 50px tall, the second 350px and the third one 50px. Finally, add a gap between the items in the grid.

#### 3. Adding grid-template-areas

The feature which will allow us to experiment with layout super easily is called _template areas._

To add it to the grid we’ll simply give the container a `grid-template-areas` property. The syntax might be a bit weird, as it’s unlike any other CSS syntax out there. Here it is:

```css
.container {  
    display: grid;  
    grid-gap: 5px;      
    grid-template-columns: repeat(12, 1fr);  
    grid-template-rows: 50px 350px 50px;  
    grid-template-areas:  
        "h h h h h h h h h h h h"  
        "m m c c c c c c c c c c"  
        "f f f f f f f f f f f f";}

```

The logic behind the `grid-template-areas` property is that you create a visual representation of your grid in the code. As you can see, it has three rows and twelve columns, just like we’ve defined in `grid-template-columns` and `grid-template-rows`.

Each line represents a row and each of the characters (h, m, c, f) represent a grid cell.

Each of the four letters now forms a rectangular `grid-area`.

As you might have guessed, I’ve chosen the characters `h`, `m`, `c`, `f` because our grid consists of `header`, `menu`, `content` and `footer`. I could have called them whatever I wanted, of course, but it makes sense to use the first character of the items they’re describing.

#### 4. Giving areas to the items

Now we need to connect these characters with our items in the grid. To do that we’ll use the `grid-area` property:

```css
.header {  
    grid-area: h;  
}

.menu {  
    grid-area: m;  
}

.content {  
    grid-area: c;  
}

.footer {  
   grid-area: f;  
}

```

This results in the following layout:

![Image](https://cdn-media-1.freecodecamp.org/images/1*F1NggJ-SsRSq306y3vCong.png)

### Experimenting with the layout

Now we’ve finally reached the beauty of this feature, as we can experiment with the layout super easily. It’s just a matter of changing the characters of the `grid-template-areas` property. Let’s, for example, move the menu over to the right-hand side instead:

```css
grid-template-areas:  
        “h h h h h h h h h h h h”  
        "c c c c c c c c c c m m”  
        “f f f f f f f f f f f f”;

```

Which results in this layout:

![Image](https://cdn-media-1.freecodecamp.org/images/1*DXjJkGRM_aVa2lVTOj0NyQ.png)

We can use dots to create blank grid cells.

```css
grid-template-areas:  
        “. h h h h h h h h h h .”  
        "c c c c c c c c c c m m”  
        “. f f f f f f f f f f .”;

```

Here’s how that’ll look:

![Image](https://cdn-media-1.freecodecamp.org/images/1*Uf_PFaU_EA82a-eBA7DHmw.png)

Now I’d recommend you to check out [this screencast of my CSS Grid course](https://scrimba.com/c/c2gd3T2?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gR8PTE_prototype_websites), where you’ll be able to experiment with the code yourself.

### Adding responsiveness to the mix

Combining this with responsiveness is also a killer feature, as this simply wouldn’t have been possible to do with only HTML and CSS before. Let’s say you want the menu up beside the header when it’s being viewed on mobile. Then you can simply do like this:

```css
@media screen and (max-width: 640px) {  
    .container {  
    grid-template-areas:  
            "m m m m m m h h h h h h"  
            "c c c c c c c c c c c c"  
            "f f f f f f f f f f f f";}  
}

```

And that’ll result in the following:

![Image](https://cdn-media-1.freecodecamp.org/images/1*NDx9-qlf2I3YHv5Kjs4HOQ.gif)

Remember that all these changes are done with pure CSS, without touching the HTML. We can shuffle around however we want, regardless of how the div tags are laid out in the markup.

This is called source-order independence, and it’s a huge step forward for CSS.

It allows the HTML to be what it was intended to be: markup for content. And not for styling, as that’s the job of CSS.

If you’re interested in learning more about CSS Grid, [just click here](https://scrimba.com/g/gR8PTE?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gR8PTE_prototype_websites) to check out my full course.

---

Thanks for reading! My name is Per Borgen, I'm the co-founder of [Scrimba](https://scrimba.com?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gR8PTE_prototype_websites) – the easiest way to learn to code. You should check out our [responsive web design bootcamp](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gR8PTE_prototype_websites) if want to learn to build modern website on a professional level.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/bootcamp-banner.png)
_[Click here to get to the advanced bootcamp.](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=gR8PTE_prototype_websites)_

