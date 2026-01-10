---
title: How to more accurately estimate read time for Medium articles in JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-30T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-more-accurately-estimate-read-time-for-medium-articles-in-javascript-fb563ff0282a
coverImage: https://cdn-media-1.freecodecamp.org/images/0*d-tl9IZ4vRR2hvZw
tags:
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Pritish Vaidya

  Introduction

  Read Time Estimate is the estimation of the time taken by the reader to read an
  article. It has been a part of Medium’s core features since it launched in 2013.

  As explained in the New Yorker:


  The more we know about so...'
---

By Pritish Vaidya

### Introduction

Read Time Estimate is the estimation of the time taken by the reader to read an article. It has been a part of _Medium’s_ core features since it launched in 2013.

As explained in the [_New Yorker_](https://www.newyorker.com/tech/annals-of-technology/a-list-of-reasons-why-our-brains-love-lists)_:_

> The more we know about something — including precisely how much time it will consume — the greater the chance we will commit to it.

Knowing in advance how long an article will take to read helps with better time management by allowing us to plan further ahead.

### Why should I use a new script?

Yes, there are many open source libraries available on [_npm_](https://npmjs.com) but they contain several flaws.

Before that, let’s take a look at these two articles on Medium.

* [Read Time — Medium Support](https://help.medium.com/hc/en-us/articles/214991667-Read-time)
* [Read Time and You](https://blog.medium.com/read-time-and-you-bc2048ab620c)

The above two articles have the following key features

* Average Read Time (English) — 265 Words per min
* Average Read Time (Chinese, Japanese and Korean) — 500 Characters/min
* Image Read Time — 12 seconds for the first image, 11 for the second, and minus an additional second for each subsequent image. Other images counted at 3 seconds.

Most of the libraries don’t account for the above features completely. They use HTML strings as is without omitting its _tag names_ which increases the deviation of estimation from the original value.

### Code

The code can be split into three parts:

* Constants
* Utility
* Main

#### Constants

The constants can be used as defaults to the main function. The image tag has its own use which will be defined later.

![Image](https://cdn-media-1.freecodecamp.org/images/I1qiIH1GSNr2GwXtOXCduq0ZBhLEBBv9oc-y)
_Image Credit: [GitHub](https://github.com/dawnlabs/carbon" rel="noopener" target="_blank" title="">Carbon</a>. | Code: <a href="https://github.com/pritishvaidya/read-time-estimate/blob/master/src/constants/index.js" rel="noopener" target="_blank" title=")_

#### Utility Functions

1. **Strip WhiteSpace**

It is a simple utility function to remove all leading and trailing whitespace from the string provided.

![Image](https://cdn-media-1.freecodecamp.org/images/GXs-gWsnAaFVaEhYkffcs6Do6XHAYwH4GIIG)
_Image Credit: [GitHub](https://github.com/dawnlabs/carbon" rel="noopener" target="_blank" title="">Carbon</a>. | Code: <a href="https://github.com/pritishvaidya/read-time-estimate/blob/master/src/utils/strip-whitespace.js" rel="noopener" target="_blank" title=")_

**2. Image Read Time**

It parses the string, looks for any HTML image tags based on the defaults provided in the constants and returns the count.

If the image count is greater than 10, we calculate the image read time of the first 10 images in decreasing arithmetic progression starting from 12 sec / `customReadTime` provided by the user using the simple formula `n * (a+b) / 2` and 3 sec for the remaining images.

![Image](https://cdn-media-1.freecodecamp.org/images/QZLkHjy8hKGklv1dfJUw8QIq-nyxCMUBqWVm)
_Image Credit: [GitHub](https://github.com/dawnlabs/carbon" rel="noopener" target="_blank" title="">Carbon</a>. | Code: <a href="https://github.com/pritishvaidya/read-time-estimate/blob/master/src/utils/image-read-time.js" rel="noopener" target="_blank" title=")_

**3. Strip Tags**

Next, we check for any HTML tags (both) in the string and remove it to extract only the words from it.

![Image](https://cdn-media-1.freecodecamp.org/images/7C84Iy4AhG4sE7pkRqBzljPgwll6fpXK6agy)
_Image Credit: [GitHub](https://github.com/dawnlabs/carbon" rel="noopener" target="_blank" title="">Carbon</a>. | Code: <a href="https://github.com/pritishvaidya/read-time-estimate/blob/master/src/utils/strip-tags.js" rel="noopener" target="_blank" title=")_

**4. Words Read Time**

This utility function calculates the words count and _Chinese / Korean and Japanese_ characters using the different _Unicode_ character range.

The time is calculated by dividing it with the constants defined above.

![Image](https://cdn-media-1.freecodecamp.org/images/dlVpGaguE9EaHXH268Kj6ZXNy8CenaOkSElz)
_Image Credit: [GitHub](https://github.com/dawnlabs/carbon" rel="noopener" target="_blank" title="">Carbon</a>. | Code: <a href="https://github.com/pritishvaidya/read-time-estimate/blob/master/src/utils/words-read-time.js" rel="noopener" target="_blank" title=")_

**5. Humanize Time**

Based on the [distance of time in words](https://api.rubyonrails.org/classes/ActionView/Helpers/DateHelper.html#method-i-distance_of_time_in_words), we can calculate and return the humanized duration of the time taken to read.

![Image](https://cdn-media-1.freecodecamp.org/images/y5NtDMmPJiq26c2Ry6LMdraRyaY3gmsrY0EI)
_Image Credit: [Github](https://github.com/dawnlabs/carbon" rel="noopener" target="_blank" title="">Carbon</a>. | Code: <a href="https://github.com/pritishvaidya/read-time-estimate/blob/master/src/utils/humanize-time.js" rel="noopener" target="_blank" title=")_

#### Main

The main function only consolidates all the utility methods in the correct order.

![Image](https://cdn-media-1.freecodecamp.org/images/Ja78VfX78b32iztnVrpNGz8cvTcOg9ZcpeSm)

### How accurate is this script?

Taking the tests on the HTML string (from the Chrome inspector) **before this article section.**

![Image](https://cdn-media-1.freecodecamp.org/images/jadNXZgeEEgfSft4bwnZRnTnDbEJvijjssga)

![Image](https://cdn-media-1.freecodecamp.org/images/wQ8Rqazgd3WSlbZaa0RS-rbd2LGceCxQBJ2C)

The tests and the [Pages](https://www.apple.com/in/pages/) clearly give the correct estimate about the total words from the parsed HTML and the number of images.

### Links

I’ve consolidated the complete code on [GitHub](https://github.com/pritishvaidya/read-time-estimate). It is also available as an npm package [read-time-estimate](https://www.npmjs.com/package/read-time-estimate).

More of the cool stuff can be found on my [**_StackOverflow_**](https://stackoverflow.com/users/6606831/pritish-vaidya) and [**_GitHub_**](https://github.com/pritishvaidya) profiles.

Follow me on [**_LinkedIn_**](https://www.linkedin.com/in/pritish-vaidya-506686128/), [**_Medium_**](https://medium.com/@pritishvaidya94), [**_Twitter_**](https://twitter.com/PritishVaidya) for further update new articles.

**One clap, two claps, three claps, forty?**

![Image](https://cdn-media-1.freecodecamp.org/images/i8DEAdbrJcjBay1E0rScJ481SHR9GqeWe5hG)

_Originally published at [blog.pritishvaidya.com](https://blog.pritishvaidya.com/posts/2019-01-30-a-simple-and-more-accurate-estimation-of-read-time-for-medium-articles-in-javascript/) on January 30, 2019._

