---
title: How to Build a Delightful Loading Screen in 5 Minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-21T04:37:37.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-delightful-loading-screen-in-5-minutes-847991da509f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*AF1rXY_iumutiVOMSXf_LQ.gif
tags:
- name: CSS
  slug: css
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Emmanuel Ohans

  First, here is what we will build. Set your timer!


  _Here’s the [DEMO](https://codepen.io/ohansemmanuel/pen/ZxOjGx" rel="noopener" target="blank"
  title=") we’ll build.

  Does this look familiar?

  If yes, that’s because you’ve seen this...'
---

By Emmanuel Ohans

First, here is what we will build. Set your timer!

![Image](https://cdn-media-1.freecodecamp.org/images/W4zbRnaocoYYCf1YLdaAsMdLXnfm7-Dhclyc)
_Here’s the [DEMO](https://codepen.io/ohansemmanuel/pen/ZxOjGx" rel="noopener" target="_blank" title=") we’ll build._

Does this look familiar?

If yes, that’s because you’ve seen this somewhere — [Slack](https://slack.com)!

Let’s learn a few things by recreating this with just CSS and some good ol’ HTML.

If you’re excited about writing some code, get on [Codepen](http://codepen.io) and create a new pen.

Now, let’s go!

#### 1. The Markup

The markup required for this is quite simple. Here it is:

```
<section class="loading">
```

```
For new sidebar colors, click your workspace name, then     Preferences > Sidebar > Theme
```

```
<span class="loading__author"> - Your friends at Slack</span>;    <span class="loading__anim"></span>
```

```
</section>
```

Simple, huh?

If you’re not sure why the class names have weird dashes, I explained the reason behind that in [this article](https://medium.freecodecamp.org/css-naming-conventions-that-will-save-you-hours-of-debugging-35cea737d849).

There’s a bunch of text, and a `.loading__anim` span to “impersonate” the animated icon.

The result of this is the simple view below.

![Image](https://cdn-media-1.freecodecamp.org/images/QVYp5Lz5g0YvKYbO1Stn2RQ9EjziWauo0a1r)
_Not so bad, huh?_

#### 2. Center the Content

The result isn’t the prettiest of stuff to behold. Let’s have the entire `.loading`section element entered in the page.

```
body {  display: flex;  justify-content: center;  align-items: center;  min-height: 100vh;}
```

![Image](https://cdn-media-1.freecodecamp.org/images/3XoIKO5ikLjWJdBaJa2S0lgf25W3djMnLsJV)
_Now centered!_

Looking better?

#### 3. Style the Loading text

I know. We will get to the animated stuff soon. For now, let’s style the `.loading` text to look a lot better.

```
.loading {  max-width: 50%;  line-height: 1.4;  font-size: 1.2rem;  font-weight: bold;  text-align: center;}
```

![Image](https://cdn-media-1.freecodecamp.org/images/ZoTXHeMu0cqNBwyUuaccOeuA6yigyvMhR7u7)

#### 4. Style the author text to look slightly different.

```
.loading__author {  font-weight: normal;  font-size: 0.9rem;  color: rgba(189,189,189 ,1);  margin: 0.6rem 0 2rem 0;  display: block;}
```

There you go!

![Image](https://cdn-media-1.freecodecamp.org/images/z6mbVcXOJZ0gBMogVez923ylx5Bqmjbkegsm)

#### 5. Create the animated loader

The much-anticipated step is here. This is going to be the longest of the steps, because I’ll be spending some time to make sure you understand how it works.

If you get stuck, drop a comment and I’ll be happy to help.

Hey, have a look at the loader again.

![Image](https://cdn-media-1.freecodecamp.org/images/3HiHd00VoFzzTMjo80NwZP6M3FTmFcgnZlRr)

You’ll notice that half of its stroke is blue and the other half is grey. Okay, that’s sorted out. Also, `HTML` elements aren’t rounded by default. Everything is a _box_ element. The first real challenge will be how to give the `.loading__anim` element half borders.

Don’t worry if you don’t understand this yet. I’ll come back to it.

First, let’s sort out the dimensions of the loader.

```
.loading__anim {  width: 35px;  height: 35px; }
```

Right now, the loader is on the same line as the text. That’s because it is a `span` element which happens to be an `HTML` **inline** element.

Let’s make sure the loader seats on another line, that is it begins on another line as opposed to the default behavior of `inline` elements.

```
.loading__anim {   width: 35px;   height: 35px;   display: inline-block;  }
```

Finally, let’s make sure the loader has some border set.

```
.loading__anim {   width: 35px;   height: 35px;   display: inline-block;   border: 5px solid rgba(189,189,189 ,0.25);  }
```

This will give a _greyish_ `5px` border around the element.

Now, here’s the result of that.

![Image](https://cdn-media-1.freecodecamp.org/images/hc9QIUgPfSH6F0T7xggQ8FD93L2S-hoXDsiZ)
_You see the grey borders, right?_

Not so great — yet. Let’s make this even better.

An element has four sides, `top`, `bottom`,`left`, and `right`

The `border` declaration we set earlier was applied to all the sides of the element.

To create the loader, we need two sides of the element to have different colors.

It doesn’t matter what sides you choose. I have used the `top` and `left` sides below

```
.loading__anim {  width: 35px;  height: 35px;  display: inline-block;  border: 5px solid rgba(189,189,189 ,0.25);  border-left-color: rgba(3,155,229 ,1);  border-top-color: rgba(3,155,229 ,1);  }
```

Now, the `left` and `top` sides will have a _blueish_ color for their borders. Here’s the result of that:

![Image](https://cdn-media-1.freecodecamp.org/images/T67pvUHFrwm8ngqtjDpRQlnsTsv5F8m-tYGE)
_hmmmm. looking nice._

We’re getting somewhere!

The loader is round, NOT rectangular. Let’s change this by giving the `.loader__anim` element a `border-radius` of `50%`

Now we have this:

![Image](https://cdn-media-1.freecodecamp.org/images/-ivf-cy5qBLeR63-BgXvQinQN1-hCHLnKHzm)

Not so bad, huh?

The final step is to animate this.

```
@keyframes rotate { to {  transform: rotate(1turn) }}
```

Hopefully, you have an idea of how [CSS animations](https://www.w3schools.com/css/css3_animations.asp) work. `1turn` is equal to `360deg` , that is a complete turn rotates 360 degrees.

And apply it like this:

```
animation: rotate 600ms infinite linear;
```

Yo! We did it. Does that all make sense?

By the way, see the result below:

![Image](https://cdn-media-1.freecodecamp.org/images/pIrqjvWR4GWuXlRnDP74790SedXbHTQvtyO3)
_lo hicimos! (Spanish)_

Pretty cool, huh?

If any of the steps confused you, drop a comment and I’ll be happy to help.

### Ready to become Pro?

I have created a free CSS guide to get your CSS skills blazing, immediately. [Get the free ebook](https://pages.convertkit.com/0c2c62e04a/60e5d19f9b).

![Image](https://cdn-media-1.freecodecamp.org/images/CguQzx6sEQ6HhauYMmL8b2Ekf-AvJgqlwZ2b)
_Seven CSS Secrets you didn’t know about_

