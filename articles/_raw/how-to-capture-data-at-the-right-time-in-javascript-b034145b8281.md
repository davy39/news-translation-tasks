---
title: How to capture data at the right time in JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-10T18:16:36.000Z'
originalURL: https://freecodecamp.org/news/how-to-capture-data-at-the-right-time-in-javascript-b034145b8281
coverImage: https://cdn-media-1.freecodecamp.org/images/0*TPwMsv_xEkHAdqJT
tags:
- name: data
  slug: data
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Jonathan Sexton

  I’ve always worked with the assumption that if I put enough time and effort towards
  anything, eventually I would get the outcome I desired. If I can throw enough hard
  work (and coffee :P) at my problem, I can build a great solution...'
---

By Jonathan Sexton

I’ve always worked with the assumption that if I put enough time and effort towards anything, eventually I would get the outcome I desired. If I can throw enough hard work (and coffee :P) at my problem, I can build a great solution to it.

Stubbornness has and continues to be one of my best and worst attributes. I’m learning that a heavy-handed approach seldom works in the land of coding. Sometimes the situation calls for some delicate hands and finesse to achieve the best result. That is the lesson I learned, and the genesis of this article.

I’m hoping that by sharing what I’ve learned (the hard way) it’ll save you some time and frustrations. So, without further ado, here is this week’s lesson on when and where to collect information.

### Assumptions

I’m going to make some assumptions before getting into this article, but in case I assume too much I have provided some links. If this is your introduction to any of these topics, then welcome! I’m more than happy to answer any questions you may have after checking out some information. My contact info can be found at the bottom of this article.

* You know the basics of [HTML](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics)
* You know the basics of [CSS](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics)
* Using the [<li](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/link)nk> tag within [you](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics)r HTML file to link to an ext[ernal style](https://developer.mozilla.org/en-US/docs/Web/CSS) sheet
* You know the basics of [JavaScript](https://developer.mozilla.org/en-US/docs/Glossary/JavaScript) — to include [declaring variables](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let) & [event listeners](https://developer.mozilla.org/en-US/docs/Web/API/EventListener)
* Using the [<li](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/link)nk> tag within [you](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics)r HTML file to link to an ext[ernal Java](https://developer.mozilla.org/en-US/docs/Glossary/JavaScript)Script file
* You understand that an [HTML](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics) file is loaded ([rendered](https://developers.google.com/web/fundamentals/performance/critical-rendering-path/render-tree-construction)) in a linear fashion, from top to bottom

Don’t worry if you aren’t familiar with everything on the list. I’ll provide you with some links throughout the article, so let’s get started.

### HTML Document Rendering

Throughout this article, I’ll be referencing the code below. It’s a simple HTML template with [<inp](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input)ut> fields in which the user can provide data about how much a new (hypothetical) phone costs.

![Image](https://cdn-media-1.freecodecamp.org/images/cZDjEkR41W8xmODPjsRFtgXnvh7x5UFmgqEh)

Here you can see that my <link> tag at the top of the document is pointing to my external style sheet. The <script> tag at the bottom of the document points to my external JavaScript file.

When this document is rendered (see the link above for a detailed description on browser rendering) the CSS style sheet will render before the JavaScript file. This is because a good portion of JavaScript is used to manipulate [DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction) elements.

If the <script> tag is anywhere but at the bottom of the HTML document, then the JavaScript file will be loaded and attempt to modify elements that do not exist just yet. This is a problem for us. That’s why the <script> tag goes just above the <body> tag.

Situations exist where you would want the JavaScript to load before that and thus it is placed in the <head> tag. That is beyond this article — just know it’s possible.

### Collecting Values

Below is the code within the JavaScript file that corresponds to the <script> tag in the above HTML document

![Image](https://cdn-media-1.freecodecamp.org/images/7AVj09rS2PAR5ujAaa1F8DYrmEWaiS73JeFF)

Above, you can see that I’ve declared some variables with different selectors. (Here’s my quick [guide](https://medium.freecodecamp.org/how-to-avoid-frustration-by-choosing-the-right-javascript-selector-73c64c3906b6) on choosing the right JavaScript selector for your situation). I want to log the values of those variables to the console.

My intention here is to get the value from _money_ and _newPhone_ fields before manipulating those values in later iterations of my code. There’s just one problem — the way I have my code structured results in empty variable values.

When my _console.log_ statements run, I’ll be left with _undefined_ as values for those variables. Now why is that you might ask? Think back to how the HTML is rendered in the browser. Everything essentially waits its turn to be rendered as the browser makes its way down the HTML. So when my <input> fields are rendered, they’re empty because the user hasn’t provided any information within those fields.

Then, I select those input fields with `let money = document.getElementById("money").value;`and `let newPhone = document.querySelector("#newPhone").value;` respectively setting them to nothing because they have no values yet.

After the HTML has loaded, my JavaScript selectors have worked their magic, the user then changes (provides information in the field) the data but my JavaScript selectors’ values never change.

### The Solution

The solution to this problem is an easy one, but it took me longer to figure out that I’d like to admit. I can place my variables for those input fields within my [event listener](https://developer.mozilla.org/en-US/docs/Web/API/EventListener). This will ensure that the data from those fields is not collected until the click happens. Of course at that time the information will have been input into the fields (after the HTML has been rendered) and our JavaScript will have no issues grabbing that data.

![Image](https://cdn-media-1.freecodecamp.org/images/h624UmWSsTl0jtHQKxPlZn5B-Dx2oTEa607n)

There are, as with all programming concepts, many different ways to accomplish this task. The method above just happens to be the way I solved it. If you have a different way and want to share it, I’d love for you to share it with me.

### Wrapping up

Of course there are more complicated situations that arise than the one I’ve outlined here. I hope this will give you a solid foundation as to when to collect data from the DOM and how your code is affected by that timing.

No matter how you decide to solve your particular issues with JavaScript, I hope you have taken at least something from this article. If I can help you save even five minutes of your time, then I’ll call that a win.

If you like this post or it helped you, please consider donating some claps as it helps others find my work. I’d also love to hear from you! Drop a comment or shout at me on [Twitter](https://twitter.com/jj_goose) — I’m always happy to connect with friendly faces and fellow developers!

I also have a [blog](https://www.jonathansexton.me/blog) where I post technical articles relating to front-end web development. You can sign up for my newsletter to stay up to date on all my writing adventures. Make sure to drop by and say hello!

As always, have a fantastic day full of coding, love, family, and happiness!

