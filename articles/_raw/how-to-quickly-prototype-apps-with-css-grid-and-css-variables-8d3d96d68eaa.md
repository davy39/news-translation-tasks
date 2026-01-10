---
title: How to quickly prototype apps with CSS Grid and CSS Variables
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-28T16:01:31.000Z'
originalURL: https://freecodecamp.org/news/how-to-quickly-prototype-apps-with-css-grid-and-css-variables-8d3d96d68eaa
coverImage: https://cdn-media-1.freecodecamp.org/images/1*r7YvAzkhlZ2E8Yjfdh-SBw.png
tags:
- name: Apps
  slug: apps-tag
- name: CSS
  slug: css
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Per Harald Borgen



  CSS Grid and CSS Variables are both huge wins for front-end developers. The former
  makes it dead simple to create website layouts, while the latter brings the power
  of variables to your stylesheets.

  In this tutorial, I’ll show ...'
---

By Per Harald Borgen

![Image](https://cdn-media-1.freecodecamp.org/images/1*mrEbsfQRmq0l32skF3kPOw.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*r7YvAzkhlZ2E8Yjfdh-SBw.png)

CSS Grid and CSS Variables are both huge wins for front-end developers. The former makes it dead simple to create website layouts, while the latter brings the power of variables to your stylesheets.

**In this tutorial, I’ll show you how to utilize them together in order to quickly prototype app designs.**

The example we’ll use has been pulled directly from [my free course](https://scrimba.com/g/greactchatkit?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=greactchatkit_css_var_grid_prototype) on how to build a chat app using React.js and the [Chatkit API](http://pusher.com/chatkit?utm_source=scrimba&utm_medium=medium&utm_campaign=css-grid-tut):

![Click the image to get to the course](https://cdn-media-1.freecodecamp.org/images/1*NE_xQlf9WZkO3LTpxG5TNA.png)
_[Click here to get to the course.](https://scrimba.com/g/greactchatkit?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=greactchatkit_css_var_grid_prototype)_

So if you prefer watching interactive screencasts over reading, [check out lecture number 15 and 16 of my course here.](https://scrimba.com/g/greactchatkit?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=greactchatkit_css_var_grid_prototype) In it, you’ll also get access to the code so that you can experiment for yourself as well. Feel free to do that as you follow this tutorial.

### Setting up the grid container

Our app has been laid out using CSS Grid, a module which makes it easy to construct layouts and to shuffle around on them. This is especially useful if you’re taking advantage of the `grid-template-areas` property, which I’ll show you how we’re using further down.

Let’s first have a look at what our initial chat app looks like:

![Image](https://cdn-media-1.freecodecamp.org/images/1*mrEbsfQRmq0l32skF3kPOw.png)

If we open up the dev tools in Chrome, we’ll be able to inspect how the underlying grid has been constructed. As you can see, it has six rows and six columns:

![Image](https://cdn-media-1.freecodecamp.org/images/1*_eNLVoRwxgaOftKEfv5i_w.png)

The code for creating such a grid is the following:

```css
.app {  
  display:                grid;  
  grid-template-columns:  1fr 1fr 1fr 1fr 1fr 1fr;  
  grid-template-rows:     1fr 1fr 1fr 1fr 1fr 60px;  
}

```

First, we’re setting the container to be a grid. Then we’re saying that we want six columns and that each of them should be one fraction unit (`1fr`) wide. One fraction unit means _one part of the available space._ So here we’re splitting the width into six equally wide fractions and give each column one fraction.

As for the rows, we’re not splitting all of them into equal height, as the last row isn’t as tall as the rest of them. We’ve explicitly told it to be `60px` tall instead of `1fr` tall:

```css
grid-template-rows: 1fr 1fr 1fr 1fr 1fr 60px;

```

Now that we’d laid out the structure of our grid, we can move on to the next part: positioning.

### Positioning the grid items

Each direct child of a grid _container_ is a grid _item_. We have four items, each being boxed into a rectangle in the image below:

![Image](https://cdn-media-1.freecodecamp.org/images/1*p_s6nyIhS8XqWoSaLEkBow.png)

In order to get the items to be placed in the positions they have above, we’ll need to use the `grid-template-areas` property and construct a visual representation of the grid in our styleeheet:

```css
.app {  
  display:                grid;  
  grid-template-columns:  1fr 1fr 1fr 1fr 1fr 1fr;  
  grid-template-rows:     1fr 1fr 1fr 1fr 1fr 60px;  
  grid-template-areas:  
    "r m m m m m"  
    "r m m m m m"  
    "r m m m m m"  
    "r m m m m m"  
    "r m m m m m"  
    "n s s s s s";
}

```

Each of the strings represents a row and each of the characters represents a cell in the grid. The characters have a semantical relation to the grid items they are representing (_room list_, _message list_, _new room form_ and _send message form_).

Now in order to position our items according to our `grid-template-areas` we’ll need to use the characters as their `grid-area` value. Like this:

```css
.new-room-form {  
  grid-area: n;  
}

.rooms-list {  
  grid-area: r;  
}

.message-list {  
  grid-area: m;  
}

.send-message-form {  
  grid-area: s;  
}

```

These classes have of course also been applied to our grid items in our HTML. However, I won’t go into detail about that, as I’m assuming that you know how to add classes to HTML tags.

With this in place, we’re ready to start experimenting with the layout. By just swapping a few characters in the `grid-template-areas` value, we’re able to completely flip around on the layout.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ufM_xVxd2GJ79JeOGd2v1w.gif)

In the gif above, I’m trying four different layouts through changing the positions of the _room list_ item and the _new room form_ item. The only thing I’m changing is the `grid-template-areas` property.

Below are the four variations. Try and see if you can map each of them to its corresponding layout:

```css
grid-template-areas:  
    "n m m m m m"  
    "r m m m m m"  
    "r m m m m m"  
    "r m m m m m"  
    "r m m m m m"  
    "r s s s s s";

grid-template-areas:  
    "r m m m m m"  
    "r m m m m m"  
    "r m m m m m"  
    "r m m m m m"  
    "r m m m m m"  
    "n s s s s s";

grid-template-areas:  
    "m m m m m r"  
    "m m m m m r"  
    "m m m m m r"  
    "m m m m m r"  
    "m m m m m r"  
    "s s s s s n";

grid-template-areas:  
    "m m m m m n"  
    "m m m m m r"  
    "m m m m m r"  
    "m m m m m r"  
    "m m m m m r"  
    "s s s s s r";

```

If you [take my React.js chat app course](https://scrimba.com/g/greactchatkit?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=greactchatkit_css_var_grid_prototype), you’ll get your very own copy of the code, so that you can change the layout exactly how you prefer to have it.

### Changing the colours with CSS Variables

Now we’re going to change the colours of the app using CSS Variables. If you haven’t been exposed to CSS Variables before, have a quick look at the images below, as they sum up the core of it:

![Image](https://cdn-media-1.freecodecamp.org/images/1*03NPOHNBLqOn5r22HrvlyQ.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*de4-CIacmaMo9PO6PlTkyQ.png)

As you can see from the image above, this makes your code easier to read, as the variable name is more semantical than the hexadecimal value. Secondly, it also gives you more flexibility in case you want to change the colour.

Let’s see how we’ve styled our app using CSS Variables, starting with our variable declarations:

```css
:root {  
  --main-color:            #5ea3d0;  
  --secondary-color:       white;  
  --main-text-color:       #3e5869;  
  --secondary-text-color:  #b0c7d6;  
  --new-room-form:         #d9e1e8;  
  --send-message-form:     #F5F5F5;  
}

```

These variables are reused 17 times across our entire stylesheet. But instead of going through all those places, let’s look at how the `--main-color` is used as a background colour in both the messages and in the left sidebar_._

![Image](https://cdn-media-1.freecodecamp.org/images/1*1W0jteJO2F9bdBqw_IC1aQ.png)

Here’s how that plays out in the code:

```css
.rooms-list {  
  background: var(--main-color);}

.message-text {  
  background: var(--main-color);  
}

```

The beauty of variables is that we now can change the declaration, and then that change will affect the entire app. Let’s for example do:

```css
:root {  
  --main-color: red;  
}

```

… which results in the following:

![Image](https://cdn-media-1.freecodecamp.org/images/1*zsR6ihPeq1AcaOWdglTL-Q.png)

What we now can do is simply change all the variable declarations in the `:root`, and thus change the entire look and feel of our app.

Let’s, for example, find a nice palette online and simply use it in our app:

![Image](https://cdn-media-1.freecodecamp.org/images/1*0qHtPYV_gzrQr-5F7-lJqA.png)

We’ll replace some of the colours in our `:root` with the ones from the palette above:

```css
:root {  
  --main-color: #5ea3d0;  
  --secondary-color: white;  
  --main-text-color: #3e5869;  
  --secondary-text-color: #b0c7d6;  
  --new-room-form: #d9e1e8;  
  --send-message-form: #F5F5F5;  
}

```

This results in a completely different type of chat:

![Image](https://cdn-media-1.freecodecamp.org/images/1*NB4_DfXxI_ZnqDSPI4QEiA.png)

### Combining Grid and Variables

If we combine this with changing the layout using CSS Grid, we get two unique chat applications which hardly resemble each other. Let’s do that:

![Image](https://cdn-media-1.freecodecamp.org/images/1*PrcUX5S8Eip5NmZ72L62eQ.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*r7YvAzkhlZ2E8Yjfdh-SBw.png)

Here’s how our starting point looks like compared to our final example.

```css
:root {  
  --main-color:           #ff66ff;  
  --secondary-color:      #fbd8fb; 
  --main-text-color:      #3e5869;  
  --secondary-text-color: #d8b2ff;  
  --new-room-form:        #ffb2ff;  
  --send-message-form:    #d8b2ff; 
}

.app {  
  display: grid;  
  grid-template-columns: repeat(6, 1fr);  
  grid-template-rows: 1fr 1fr 1fr 1fr 1fr 60px;  
  grid-template-areas:  
    "m m m m r r"  
    "m m m m r r"  
    "m m m m r r"  
    "m m m m r r"  
    "m m m m n n"  
    "f f f f f f"; 
}

```

Pretty cool, huh?

Now I’d recommend you to take [my entire course.](https://scrimba.com/g/greactchatkit?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=greactchatkit_css_var_grid_prototype) In it, I’ll guide you through creating this app using React.js and [the Chatkit API](http://pusher.com/chatkit?utm_source=scrimba&utm_medium=medium&utm_campaign=css-grid-tut). I’ll, of course, share the full code with you so that you can experiment with this design for yourself.

![Image](https://cdn-media-1.freecodecamp.org/images/1*zcRbKlNUmWNxStHWrQJEOw.png)

---

Thanks for reading! My name is Per Borgen, I'm the co-founder of [Scrimba](https://scrimba.com) – the easiest way to learn to code. You should check out our [responsive web design bootcamp](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=greactchatkit_css_var_grid_prototype) if want to learn to build modern website on a professional level.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/bootcamp-banner.png)
_[Click here to get to the advanced bootcamp.](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=greactchatkit_css_var_grid_prototype)_


