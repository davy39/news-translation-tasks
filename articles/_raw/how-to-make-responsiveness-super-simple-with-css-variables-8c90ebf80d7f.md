---
title: 'CSS Variables tutorial: How to make your HTML responsive with CSS Variables'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-26T16:42:47.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-responsiveness-super-simple-with-css-variables-8c90ebf80d7f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*tLQrkgJJhKV3YrzPxsVVFA.png
tags:
- name: CSS
  slug: css
- name: mobile
  slug: mobile
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Per Harald Borgen


  _Learn how to create the following responsiveness with CSS Variables._

  A quick tutorial on how to create responsive websites in 2019.

  If you haven’t heard of CSS Variables before, it’s a new feature of CSS which gives
  you the po...'
---

By Per Harald Borgen

![Image](https://cdn-media-1.freecodecamp.org/images/IuMWwaRBH-1VTyCpRImIsyYwp36b1lR6ObIM)
_[Learn how to create the following responsiveness with CSS Variables.](https://scrimba.com/g/gcssvariables?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=gcssvariables_tutorial_article)_

#### A quick tutorial on how to create responsive websites in 2019.

If you haven’t heard of CSS Variables before, it’s a new feature of CSS which gives you the power of variables in your stylesheet, without having to do any setup.

In essence, CSS Variables allow you to skip the old way of setting styles:

```css
h1 {  
  font-size: 30px;  
}

navbar > a {  
  font-size: 30px;  
}

…in favour of this:

:root {  
  --base-font-size: 30px;  
}

h1 {  
  font-size: var(--base-font-size);  
}

navbar > a {  
  font-size: var(--base-font-size);  
}

```

While the syntax might seem a bit weird, this gives you the obvious benefit of being able to change the font sizes across your entire app through only changing the`--base-font-size` variable.

If you want to learn CSS Variables properly, please check out [my free and interactive CSS Variables course](https://scrimba.com/g/gcssvariables?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gcssvariables_tutorial_article) on Scrimba:

![The course contains eight interactive screencasts](https://cdn-media-1.freecodecamp.org/images/1*MxS9trU9nmVDttW_IqQTyA.png)

_The course contains eight interactive screencasts._

Or if you want to know more about the course, you can also read a walk-through of what you’ll learn in the article below:

[Want to learn CSS Variables? Here’s my free 8-part course!](https://medium.freecodecamp.org/want-to-learn-css-variables-heres-my-free-8-part-course-f2ff452e5140)

Now let’s see how this new technology can make your life easier when building responsive websites.

#### The setup

We’re going to add responsiveness to a portfolio website which looks like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*tLQrkgJJhKV3YrzPxsVVFA.png)

It looks nice when viewed on your desktop. However, as you can see on the left image below, this layout doesn’t work well on mobile.

![Image](https://cdn-media-1.freecodecamp.org/images/1*CZkMgq0rp9nTdChVxwq33g.png)

_How it looks on mobile initially._

![Image](https://cdn-media-1.freecodecamp.org/images/1*zpFS--eNMyAzkdZWS1lLRQ.png)

_How we want it to look._

On the right image, we’ve changed a few things on the styles to make it work better on mobile. Here’s what we have done:

1. **Rearranged** the grid so that it’s stacked vertically instead of across two columns.
2. **Moved** the entire layout a bit more up
3. **Scaled** the fonts down

In order to do this, we needed to change the following CSS:

```css
h1 {  
  font-size: 30px;  
}

#navbar {  
  margin: 30px 0;  
}

#navbar a {  
  font-size: 30px;  
}

.grid {  
  margin: 30px 0;  
  grid-template-columns: 200px 200px;  
}

```

More specifically, we needed to make the following adjustments inside of a media query:

* Reduce font size of the `h1` to 20px
* Reduce the margin above and below the `#navbar` to 15px
* Reduce the font size inside the `#navbar` to 20px
* Reduce the margin above the `.grid` to 15px
* Change the `.grid` from from two-columns to one-column

**Note:** There is, of course, much more CSS in this application, even within these selectors. However, for the sake of this tutorial, I’ve stripped away everything which we aren’t changing in the media query. Check out [this Scrimba playground](https://scrimba.com/c/cwJmLhn?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=cssvariables_tutorial_article) to get the entire code.

#### The old way

Doing all of this would be possible without CSS Variables. But it would require an unnecessary amount of code, as most of the bullet points above would need their own selector inside the media query, like this:

```css
@media all and (max-width: 450px) {  
    
  navbar {  
    margin: 15px 0;  
  }  
    
  navbar a {  
    font-size: 20px;  
  }  
    
  h1 {  
    font-size: 20px;  
  }

  .grid {  
    margin: 15px 0;  
    grid-template-columns: 200px;  
  }

}

```

#### The new way

Now let’s see how this can be solved with CSS Variables. To begin with, we’ll rather store the values which we are reusing or changing inside variables:

```css
:root {  
  --base-font-size: 30px;  
  --columns: 200px 200px;  
  --base-margin: 30px;  
}

And then we’ll simply use these variables across the app:

#navbar {  
  margin: var(--base-margin) 0;  
}

#navbar a {  
  font-size: var(--base-font-size);  
}

h1 {  
  font-size: var(--base-font-size);  
}

.grid {  
  margin: var(--base-margin) 0;  
  grid-template-columns: var(--columns);  
}

```

Once we have this setup, we can simply change the values of the variables inside the media query:

```css
@media all and (max-width: 450px) {  
  :root {  
    --columns: 200px;  
    --base-margin: 15px;  
    --base-font-size: 20px;  
}

```

This is much cleaner than what we had before. We’re only targeting the `:root`, as opposed to specifying all the selectors.

We’ve reduced our media query from **four selectors down to one** and from **thirteen lines down to four**.

And this is just a simple example. Imagine a full-blown website where, for example, the `--base-margin` control most of the free spacing around the app. It’s a lot easier to just flip the value of it, as opposed to filling your media query up with complex selectors.

To sum up, CSS Variables are definitely the future of responsiveness. If you want to learn this technology once and for all, I’d recommend that you check out my [free course on the subject on Scrimba.](https://scrimba.com/g/gcssvariables?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gcssvariables_tutorial_article)

You’ll become a CSS Variables master in no time :)

Thanks for reading! I’m Per Borgen, front-end developer and co-founder of [Scrimba.](http://scrimba.com?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gcssvariables_tutorial_article) Feel free to reach out to [me via Twitter](https://twitter.com/perborgen) if you have any questions or comments.

---

Thanks for reading! My name is Per Borgen, I'm the co-founder of [Scrimba](https://scrimba.com?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gcssvariables_tutorial_article) – the easiest way to learn to code. You should check out our [responsive web design bootcamp](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gcssvariables_tutorial_article) if want to learn to build modern website on a professional level.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/bootcamp-banner.png)
_[Click here to get to the advanced bootcamp.](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=gcssvariables_tutorial_article)_


