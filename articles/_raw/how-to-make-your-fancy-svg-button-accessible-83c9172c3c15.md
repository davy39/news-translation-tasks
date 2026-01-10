---
title: How to make your fancy SVG button accessible
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-13T14:19:09.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-your-fancy-svg-button-accessible-83c9172c3c15
coverImage: https://cdn-media-1.freecodecamp.org/images/1*3Femts-5Nx83ChD5l6_IKw.jpeg
tags:
- name: Accessibility
  slug: accessibility
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Jonathan Speek

  You may very well find yourself one day having to build some crazy button a designer
  dreamed-up. You might start reaching for that good old <div>, but easy there big-shifter
  ? — let’s try and use that <;button> element you’re avoidi...'
---

By Jonathan Speek

You may very well find yourself one day having to build some crazy button a designer dreamed-up. You might start reaching for that good old `<d`iv>, but easy there big-shifter ? — let’s try and use `that <`;button> element you’re avoiding ?

We’ll start by simply grabbing the code for an SVG icon that we want to use. I quickly made a Chemex icon you can use [here](https://codepen.io/JonathanSpeek/pen/pQxYqo) (I love me some coffee ☕️). Paste that between a `<butt`on> tag in your HTML like so (the SVG code will be pretty lengthy).

![Image](https://cdn-media-1.freecodecamp.org/images/QA6qC1qblNFuf4906Gd5zip2X65AIlLbreSY)
_Initial &lt;button&gt; with SVG code inside_

We want this button stripped of its default styling, so let’s give the button an “id” and we’ll target it with some CSS.

![Image](https://cdn-media-1.freecodecamp.org/images/9eN7Cfrt9QplVmdH5X-XkbzcIruiogzzphqk)
_Strip the default styling of the &lt;button&gt; so we can make it better ?_

Give the button a good width/height that is larger than our SVG — this will help the visibility of the outline. Speaking of, make sure the contrast ratio between your outline color and the background color [passes this](https://userway.org/contrast-checker). Get rid of that pesky border and background, make sure the cursor is set to pointer.

At this point, you have a clickable button that, when clicked, shows the default outline your browser has chosen for focus states. Let’s change that and make it better.

![Image](https://cdn-media-1.freecodecamp.org/images/JOqPbxdOEC3bTevV0lZqTGpDYsVWEGXpDzfq)
_Giving the button some focus ?_

Now when we click or tab to our button, we get a cool little dashed outline that lets us know where we’re focused.

We also want to ensure that the SVG itself does not get an outline if clicked. And we want to make certain Firefox doesn’t add its default dotted outline. While we’re at it, we can give the SVG a little hover effect.

![Image](https://cdn-media-1.freecodecamp.org/images/dqTv6Xmdit1jeW4tKrmaAUrZbY9ZzVizMfoF)
_Adding our flavorful hover effect ?_

Now we can get to the cool parts ? We don’t want to annoy or confuse our screen reader users with our button. So we need a good short description of what to expect. You would also typically want visual users to have an idea of what it is they’re clicking on as well, for now let’s keep ’em guessing...

We can easily achieve this by putting a `<sp`an> element around the text in our button and styling it out of view. Make **su**re not to set display to “none”, as this will also prevent our screen readers for accessing it.

![Image](https://cdn-media-1.freecodecamp.org/images/RAJN2axCgcQ70Dz6ZOhbiIuad51OzHmAqcXE)
_Telling our screen reader users what they’re clicking on ?_

Lastly, let’s make sure we’ve:

* hidden the SVG from anyone using assistive technology and
* set the tabindex to “0” so that the browser uses the expected tab order for any keyboard users.

![Image](https://cdn-media-1.freecodecamp.org/images/wAPj780H1xSCzWJQkOe2Z0miBrj1R2N7n3XT)
_Setting the proper tab order ⌨️_

You should now have a really accessible button that you can be proud of ?Besides patting yourself on the back — do it now — going forward you now have some reusable patterns that you can implement that help make the web just a little more accessible ?

Here’s a [link to the CodePen example](https://codepen.io/JonathanSpeek/pen/JeRwgp), feel free to fork your own copy ?

Thanks for reading. If you have some knowledge to drop on accessibility, be sure to leave a comment.

And you can [follow me on Twitter here](https://twitter.com/intent/follow?screen_name=jonspeek).

