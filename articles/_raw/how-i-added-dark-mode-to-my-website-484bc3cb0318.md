---
title: How I added dark mode to my website
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-11T15:47:25.000Z'
originalURL: https://freecodecamp.org/news/how-i-added-dark-mode-to-my-website-484bc3cb0318
coverImage: https://cdn-media-1.freecodecamp.org/images/0*fTme9ip4kqGbZuHc.png
tags:
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Jonathan Sexton

  Same website, two different color schemes

  Last year I made it a point to redesign my website from scratch. I wanted something
  simple and minimalist looking that clearly stated what this was — a portfolio website.

  After I rebuilt my...'
---

By Jonathan Sexton

#### Same website, two different color schemes

Last year I made it a point to redesign my website from scratch. I wanted something simple and minimalist looking that clearly stated what this was — a portfolio website.

After I rebuilt my website from the ground up it seemed like everywhere I turned there was another article about adding a dark mode to your website.

At first I didn’t think it would make that big of a difference because, while I am partial to darker colors, I felt like my website was a good balance between bright, fun colors and darker fonts.

![Image](https://cdn-media-1.freecodecamp.org/images/0UKp9ooxLroDJHXifQ0UPa6JAZ2aczd0KtXw)

I read some of the articles I mentioned earlier and the more I thought about it the more I decided to go for it.

I took some inspiration from Flavio Copes who wrote a [terrific article](https://flaviocopes.com/dark-mode/) on this very subject. Unlike what Flavio decided to do with his site, I didn’t add the user’s choice to local storage.

This is due, in part, to the differences between our sites. I have a static site and there are no redirects/separate pages aside from the blog which is on a different platform so users generally won’t be refreshing the page. It is a neat option and one that I may add in later on.

Ok, let’s dig into the nuts and bolts of how I accomplished my dark mode toggle.

### The Code

The code to achieve this was fairly simple. I took the same approach as Flavio did and added the style changes through CSS. I had to take a few more steps because I have an image on my landing page.

![Image](https://cdn-media-1.freecodecamp.org/images/k3elVGlxhWNo9FKBbPzIdsfJ6MUBiMfFMPYy)

I had to use the **!important** flag on some of the rules because they were not being applied properly. This was the easiest approach to implement and I know it’s not advised to use this flag so I’ll be looking for an alternative in the near future.

Here is the JavaScript I used to get my toggle switch working correctly:

![Image](https://cdn-media-1.freecodecamp.org/images/uVO2mmQZyc5W7lzYqxb2fLIY5-OJeYGctlrH)

I start by selecting my `div` with an id of `light-dark-mode-container` and adding an [event listener](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener) to it.

Next, I set my variables of `everything`, which selects all content on the page, and `projectTiles` because this class belongs to a particular set of overlays I do not want to have a background of a solid color.

Next, since I’m using `[querySelectorAll](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelectorAll)` which returns a static [NodeList](https://developer.mozilla.org/en-US/docs/Web/API/NodeList), I loop over all of the elements within both NodeLists and either toggle the class `dark` or completely remove it from the elements returned by the variable `projectTiles`.

What I’m left with is a container at the top of my website with a toggle switch that allows the user to toggle between light and dark mode.

![Image](https://cdn-media-1.freecodecamp.org/images/8daEF9V6p0lk6rkCgsPced5rILn0wR95ms5x)
_The final product_

![Image](https://cdn-media-1.freecodecamp.org/images/OVHTig0pHG90YyP9FMF4E62xOgLCwHT5KEKo)
_The next screen down on dark mode_

I hope you enjoyed this post and maybe you learned something too! If you decide to implement this on your own website or your next project please share it with me (leave me a comment or shout at me on [Twitter](https://twitter.com/jj_goose)). I’m always happy to see the work and projects that others create.

This post was posted on my [blog](https://jonathansexton.me/blog) where I write articles related to front end web development. I also cross post over at [Dev.to](https://dev.to/jsgoose), so if you’re on that platform you can find my work as well!

While you’re there why not sign up for my **Newsletter**? I promise I’ll never spam your inbox and your information will not be shared with anyone else.

Have an awesome day filled with love, joy, and coding!

