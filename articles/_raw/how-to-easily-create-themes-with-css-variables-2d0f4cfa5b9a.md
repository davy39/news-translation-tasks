---
title: How to easily create themes with CSS Variables
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-23T17:09:46.000Z'
originalURL: https://freecodecamp.org/news/how-to-easily-create-themes-with-css-variables-2d0f4cfa5b9a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*blhp0Jh_MceZD4hnTgX6qw.png
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

  One of the best use cases for CSS Variables is theme creation. And by that, I don’t
  only mean changing themes for your entire app, as that’s probably not something
  you need to do very often. What’s more relevant is the ability to...'
---

By Per Harald Borgen

One of the best use cases for CSS Variables is theme creation. And by that, I don’t only mean changing themes for your entire app, as that’s probably not something you need to do very often. What’s more relevant is the ability to easily create _component specific themes._

This could, for example, be when you need to mark an e-commerce product as _added to cart._ Or perhaps your site has an admin section which includes a darker sidebar section.

**CSS Variables** enable you to do this in a simpler and more flexible way than was previously possible. In this article, I’ll explain exactly how.

I’ve also created a screencast about theme creation in my free [8-part CSS Variables course.](https://scrimba.com/g/gcssvariables?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gcssvariables_create_themes) If you’re interested in learning more about the course, check out [this article](https://medium.freecodecamp.org/want-to-learn-css-variables-heres-my-free-8-part-course-f2ff452e5140).

### The setup

We’ll be working with a portfolio site as an example. Our goal is to be able to feature one of the projects in our portfolio so that it stands out from the rest of the crowd. Technically, we’ll do this by adding a class to the specific item we want to feature.

Here’s how the portfolio site looks initially:

![Image](https://cdn-media-1.freecodecamp.org/images/1*Eu0wU_hiyqOqrhyxNamvsg.png)

I won’t bother talking about the HTML for the site, as it’s pretty straight forward, and I’m assuming that you know HTML. However, if you’re interested in fiddling around with the code, I’ve created a Scrimba playground for it [here.](https://scrimba.com/c/cBBeZuL?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gcssvariables_create_themes)

Now, let’s jump directly into the CSS. Here’s our stylesheet before we’ve started using CSS Variables:

```css
html, body {  
  background: #ffeead;  
  color: #ff6f69;  
}

h1, p {  
  color: #ff6f69;  
}

#navbar a {  
  color: #ff6f69;  
}

.item {  
  background: #ffcc5c;  
}

button {  
  background: #ff6f69;  
  color: #ffcc5c;  
}

```

As you can see, we’re only using three colours here: `#ffeead`, `#ff9f96` and `#ffcc5c`. However, we’re reusing them a lot. So this is a perfect use case for CSS Variables.

To start using it, we’ll first need to declare our variables. We’ll do that in the `:root` pseudo-class:

```css
:root {  
  --red: #ff6f69;  
  --beige: #ffeead;  
  --yellow: #ffcc5c;  
}

```

Then we’ll simply swap out our hexadecimal values with the variables:

```css
html, body {  
  background: var(--beige);  
  color: var(--red);  
}

h1, p {  
  color: var(--red);  
}

#navbar a {  
  color: var(--red);  
}

.item {  
  background: var(--yellow);  
}

button {  
  background: var(--red);  
  color: var(--yellow);  
}

```

Now we have the power of variables in our CSS, meaning we can simply change the `--red` to something else, and it’ll be updated throughout our entire site.

If you’re struggling to understand what’s going on here, please check out my [Learn CSS Variables in 5 minutes article](https://medium.freecodecamp.org/learn-css-variables-in-5-minutes-80cf63b4025d), or enrol in the [course.](https://scrimba.com/g/gcssvariables?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gcssvariables_create_themes)

### Creating a theme

Now let’s create the theme. We want the ability to add a `.featured` class to one of our four project items, and thereby make that item stand out from the rest. Specifically, we’ll be changing red to `#ff5564` and yellow`#ffe55b`.

Here’s how it’ll look in the markup:

```html
<div class="item **featured**">  
  <h1>project d</h1>  
  <button>learn more</button>  
</div>

```

This change should affect the styling at four different places:

* background color of the `<div>`
* color of the`<h1>`
* background color of the `<button>`
* color of the `<button>`

#### The old way

The way we had to solve this previously was by creating a custom CSS selector for each element inside the `.featured` item, like this:

```css
.featured {  
  background: #ffe55b;  
}

.featured > h1 {  
  color: #ff5564;  
}

.featured > button {  
  background: #ff5564;   
  color: #ffe55b;  
}

```

This approach isn’t very flexible. If you were to add another element inside your portfolio items, you’d have to write specific selectors for them as well.

#### The new way

With CSS Variables, however, it becomes much easier. We’ll simply override the variables inside the `.featured` a class like this:

```css
.featured {  
  --yellow: #ffe55b;  
  --red: #ff5564;  
}

```

As CSS Variables are inherited, all the elements inside `.featured` which reference `--red` or`--yellow` now use the local values and not the global ones. So the `<button>` or `<h1>` elements automatically use the local values for the variables.

Here’s how it plays out on the page.

![As you can see, the ‘project d’ item looks a bit different than the rest.](https://cdn-media-1.freecodecamp.org/images/1*QYSniAuCy5MkF202RvMUDQ.png)

  
As you can see, the ‘project d’ item looks a bit different than the rest.

Neat, or what?

Just think about how this would be if we were building a more complex component, for example, a product item in an e-commerce app. It might include titles, sub-titles, paragraphs, images, captions, buttons, ratings and much more. It’s much easier and more flexible to simply flip the value of some variables instead of creating custom selectors for each of the descendants.

If you’re interested in learning more about this technology, please check out my free [8-part interactive CSS Variables course](https://scrimba.com/g/gcssvariables?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gcssvariables_create_themes) on Scrimba.

---

Thanks for reading! My name is Per Borgen, I'm the co-founder of [Scrimba](https://scrimba.com?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gcssvariables_create_themes) – the easiest way to learn to code. You should check out our [responsive web design bootcamp](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gcssvariables_create_themes) if want to learn to build modern website on a professional level.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/bootcamp-banner.png)
_[Click here to get to the advanced bootcamp.](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=gcssvariables_create_themes)_

