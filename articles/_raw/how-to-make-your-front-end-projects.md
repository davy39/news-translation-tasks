---
title: How to instantly make your front end projects look better
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-09T11:07:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-your-front-end-projects
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c3f740569d1a4ca30eb.jpg
tags:
- name: Bootstrap
  slug: bootstrap
- name: colors
  slug: colors
- name: CSS
  slug: css
- name: Design
  slug: design
- name: front end
  slug: front-end
- name: Front-end Development
  slug: front-end-development
- name: frontend
  slug: frontend
- name: HTML
  slug: html
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Peter Gleeson

  We’ve all been there. You’ve been learning the basics of front end Web development,
  and you are keen to try out some new ideas.

  You take the time to code up the perfect HTML page, and add some styles and JavaScript
  for good measure.

  ...'
---

By Peter Gleeson

We’ve all been there. You’ve been learning the basics of front end Web development, and you are keen to try out some new ideas.

You take the time to code up the perfect HTML page, and add some styles and JavaScript for good measure.

Then you pause. Time to take a moment to step back and see how your efforts look in the browser.

Pretty terrible, right?

That was certainly my experience when I first learned a little front end development.

I’d put a lot of thought into the functionality of the site. But when I put everything together, it looked awful.

I wanted to share my work with a few friends to get feedback. But in its present state, my site wasn’t ready.

You see, functionality is only half the story. We humans for whatever reason are biased towards the appearance or presentation of something.

Perhaps we’re more likely to trust a site that appears professional and well-designed. Or maybe the aesthetic value of a well-designed site can help us overlook minor flaws in functionality.

Whatever the reason, something of a “[halo effect](https://en.wikipedia.org/wiki/Halo_effect)” does exist in Web development.

In this article, you’ll learn a few easy tips to make your ugly af front end project look better in no time.

### The starting point

Below is an example of a simple HTML page with no styling at all.

%[https://codepen.io/pg2020/pen/PoqOQmG]

This will be the starting point for the rest of the article. Each tip will build on top of the earlier ones until you have a better looking page to work with.

We’ll go in order of impact. That is, we’ll start with the tip that gives you the quickest improvement and make smaller and smaller gains as we go.

### Add some negative space

The first tip is easy to picture, but needs to be put into practice carefully.

‘Negative space' refers to the empty space between elements on the page.

Getting the right amount of negative space goes a long way to making your page look better.

Specifically, it does two things:

* It makes the page less cluttered. It is easier to find the different elements, because the negative space helps them stand out from each other.
* It makes better use of the available screen space. Spacing the elements out carefully can help fill parts of the screen that are more central, and reduce content in parts on the edges.

Check the CSS in the example below. This adds some basic negative space to the simple example you saw earlier.

And here is the result:

%[https://codepen.io/pg2020/pen/oNXoEWK]

Notice what has happened here:

* Padding creates space within an element
* Margin creates space between the elements
* Line-size makes text less cluttered

Too much empty space isn’t a good look. It can be tricky to get the balance right.

### Pair your fonts

The next tip is another one with a quick impact.

The default system fonts are very safe and sensible. They are guaranteed to work.

But the choice of font makes a huge statement about the purpose and feel of your site.

* Light, playful fonts tell the viewer this page is fun and accessible
* Sensible, simple fonts give a more business-like appearance
* Traditional or display fonts give more of a timeless, classic look.

You get the idea.

But how to put it into practice?

The key is to use font pairs.

The idea is that using two fonts for different elements on the page provides a helpful contrast. Again, this helps make elements stand out and makes your page easier to view.

But you shouldn’t pair up any old fonts.

For [a bunch of aesthetic reasons](https://www.canva.com/learn/combining-fonts-10-must-know-tips-from-a-designer/), some font pairings look much better than others.

Don’t worry about figuring this out yourself, though. As usual, there are resources on the Internet to help you.

Check out [fontpair.co](https://www.freecodecamp.org/news/how-to-make-your-front-end-projects/fontpair.co). It lets you browse different font pairings and see how they look together.

Once you find a pairing you like, the quickest way to use them in your project is to head over to [Google Fonts](https://fonts.google.com/).

* Search for the fonts you want
* Add them to your project
* Include the link in your HTML `<head>` element
* Reference the fonts in the stylesheet

See below for an example built on top of the basic page you saw earlier.

%[https://codepen.io/pg2020/pen/ZEGaraM]

You can also improve the appearance by controlling the font size and text alignment.

Doesn’t that look considerably better? And after only two easy steps.

### Get a colour scheme

I’m no designer, but I appreciate the value of learning [the basics of colour theory](https://lifehacker.com/learn-the-basics-of-color-theory-to-know-what-looks-goo-1608972072).

In short, the colours you use on your page go a long way to creating an impression.

For example:

* Bright, exuberant colours create an energetic feel
* Light, toned down shades create a more corporate impression
* Dark, contrasting colours create a more dramatic impression
* Brand colours create a consistent identity

Again, it pays to choose your colours carefully.

The theory goes that the relationship between the colours you use also impacts the appearance of your site.

* Analogous colours can create a consistent, harmonious appearance
* Complementary colours create a pleasing contrast
* Triadic colours provide both contrast and balance

It pays to pick a colour scheme carefully.

Luckily, there are many ways to do this. Just Google "colour scheme generator" and you will be spoiled for choice.

One of my favourite tools is [colormind.io](http://colormind.io/template/paper-dashboard/). It generates a colour scheme and lets you preview it on a template.

Of course, rules can be broken. Using a more discordant colour scheme can be jarring, but used carefully can give a page an edgier, more stand-out appearance.

See the code below has been updated to use a simple colour scheme.

%[https://codepen.io/pg2020/pen/MWwOQXq]

### Add some structure

No matter how well-presented your page is right now, it can be improved by shaking things up a bit.

Adding in sections and structure can break up the monotony of a longer page.

By creating clear bounds between elements, you can create a logical structure and/or hierarchy. This will make it easier for the viewer to understand your page layout.

Keep to the same colour scheme, but vary things up a little.

See the example below has been extended to include more of a structure. The content is divided into `<header>`, `<footer>` and `<div class="content">` elements.

The example also uses a media query to make the page present better on smaller devices.

%[https://codepen.io/pg2020/pen/zYGPRVg]

If you want to learn more, try looking into:

* [CSS Grid](https://css-tricks.com/snippets/css/complete-guide-grid/) for creating a layout
* [Flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Basic_Concepts_of_Flexbox) for creating layouts
* [Bootstrap](https://getbootstrap.com/docs/3.4/css/) for creating responsive designs
* Responsive design with [media queries](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Media_queries)

It didn’t take much rewriting, but the effect is very noticeable.

### Add some images and icons

Humans are typically visual creatures. A well placed image or icon can go a long way to making a page easier to view and understand.

The code below adds a simple image to the main content. See how it is included in the `<div class="content">` element and the width is set to 100%? This keeps the structure of the page consistent.

Remember, images should be considered in the context of the overall colour scheme.

You don’t need to be a budding CSS artist or Photoshop wizard to do this. If you need access to high quality photos quickly, your can search [Unsplash](https://unsplash.com/) for free-to-use images.

Even a few free icons can make a difference.

The example below adds a simple menu icon to the top right corner. You could also add icons to your Github profile, or other online profiles.

%[https://codepen.io/pg2020/pen/zYGPWrY]

You can quickly add free icons from these resources:

* [Fontawesome](https://fontawesome.com/)
* [Bootstrap](https://icons.getbootstrap.com/)
* [Google](https://material.io/resources/icons/?style=baseline)
* [Plenty of others](https://www.keycdn.com/blog/icon-library)

### Add some animations

This final tip is a nice-to-have for sure.

As anyone who used PowerPoint during the 2000s will know, animations need to be used carefully.

Too many animations can be confusing and irritating for users.

But used properly, they can make a page much more interactive and visually appealing.

There are lots of ways to add animations to your site. You can use [CSS selectors](https://www.w3schools.com/cssref/sel_hover.asp) to change style in response to certain events, such as when the user hovers on that element.

The example below changes the image opacity to 50% when the user hovers over it.

Another option is to use is [Animate.css](https://daneden.github.io/animate.css/). This provides a number of pre-built animations that you can use straight out-of-the-box.

The code below adds a subtle animation to the buttons when it is clicked.

%[https://codepen.io/pg2020/pen/xxGPWEZ]

Remember — with animation, less is usually more!

#### The final result

See [this Github repo](https://github.com/pg0408/frontend-demo) for overall evolution of the page.

The design still has a long way to go. But just by following some simple guidelines, it looks much better than it did at the start.

Here’s a quick review of each of the tips:

1. Add some negative space
2. Choose a pair of fonts
3. Pick a coherent colour scheme
4. Add some structure
5. Add a few icons or images
6. (Optionally) add some animation

Leave a response below if you found this quick guide helpful. Do you have any tips or tricks you want to share?

Thanks for reading!

