---
title: '&lt;table&gt; prejudice and HTML xenophobia'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-11-18T13:10:58.000Z'
originalURL: https://freecodecamp.org/news/table-prejudice-and-html-xenophobia-30704984785e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*pD4gTzlobYFeNN0JtJhcjA.jpeg
tags:
- name: Accessibility
  slug: accessibility
- name: Design
  slug: design
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Anthony Ng

  I was looking over some HTML with a student the other day when we stumbled onto
  a .

  It displayed data with restaurant reservation information. The first column held
  the names for the reservation. The second column held the time of the r...'
---

By Anthony Ng

I was looking over some HTML with a student the other day when we stumbled onto a <table>.

It displayed data with restaurant reservation information. The first column held the names for the reservation. The second column held the time of the reservation.

It looked like this:

![Image](https://cdn-media-1.freecodecamp.org/images/oClTJHnHRQP3-H7pVbOriwq-I5quFfFvLvsJ)
_Table with reservation information_

> “Oh wow, I can’t believe this code is actually using a table. What is this, the 90's?” — my student

Back in the 90’s, tables were all the rage. Developers would use tables throughout their HTML to format non-tabular content.

But the pendulum swung back. Tables fell out of fashion. And their reputation as a user interface element has never recovered.

So my student started brainstorming of ways he could code this reservation information the “right” way.

> “I know — we’ll use lists.”

> “OK.” I said. “So you would use two lists? One for the name, and one for the time?”

> “Yes. And I’ll use CSS to style it to look like a table.”

His distaste for tables and the ways they’d been abused in the past was leading him to abuse a different HTML element instead.

And this got me thinking: are other developers bending over backward to avoid using tables as well?

### Why use tables? What are they for?

According to [Mozilla Developer Network](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/table)’s documentation, tables present tabular data.

I like to think of tabular data as data that has relationships within it. Was there a relationship between each reservation? Yes, each reservation time was associated with a specific name.

It’s totally appropriate and semantic to use tables to represent tabular data. CSS Frameworks like [Bootstrap](http://getbootstrap.com/css/#tables) even support styled tables. Tables are meant to be used!

So where did all this hate come from?

Back in the day, tables were used for formatting and layout purposes. Take a look at this example (or view it interactively on [Codepen](http://codepen.io/newyork-anthonyng/pen/Obyowm?editors=1010)):

```
<table align=”center”>  <tbody>    <tr><td>Welcome to this email</td></tr>  </tbody></table><table>  <tbody>    <tr>      <td>        Lorem ipsum dolor sit amet, consectetur adipiscing elit.    Vestibulum aliquet velit at lectus sodales, sit amet consequat odio eleifend. Fusce accumsan sed eros convallis imperdiet. Donec at dignissim nibh.       </td>      <td>        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum aliquet velit at lectus sodales, sit amet consequat odio eleifend. Fusce accumsan sed eros convallis imperdiet. Donec at dignissim nibh.       </td>    </tr>  </tbody></table><table align=”center”>  <tr><td>Thank you for reading this email</td></tr></table>
```

These 3 tables created this 2-column layout for us.

![Image](https://cdn-media-1.freecodecamp.org/images/S7LcU0XxI9rbeDxsxm0SaO-Cq2A99tVbpQBX)
_2 column layout_

With modern advances in CSS, we don’t need to use tables as a hack for page layout. Take a look at this rewritten example using CSS which produces the same 2 column layout (view on [Codepen](http://codepen.io/newyork-anthonyng/pen/yVYxRq?editors=1100)):

```
// html file<header>  Welcome to this email</header>
```

```
<div>  <p>     Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum aliquet velit at lectus sodales, sit amet consequat odio eleifend. Fusce accumsan sed eros convallis imperdiet. Donec at dignissim nibh.  </p>  <p>    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum aliquet velit at lectus sodales, sit amet consequat odio eleifend. Fusce accumsan sed eros convallis imperdiet. Donec at dignissim nibh.   </p></div>
```

```
<footer> Thank you for reading this email</footer>
```

```
// css fileheader,footer {  text-align: center;}
```

```
div {  display: flex;}
```

### Table layouts aren’t going away

Your stomach might wrench when looking at that code using tables for layout. But this technique isn’t going away any time soon.

Many developers find cross-browser testing to be difficult, but consider how many different email clients there are.

Email clients lack strong, consistent support for certain CSS styles. Tables provide a reliable way to achieve a consistent layout across multiple email clients and devices.

### Learn your HTML

My advice is to get a feel for which tools are available to you. Most importantly, use the correct tool for the job. Sure, you could use a hammer to drive a screw into a wall. But wouldn’t a screw driver work better?

Many of us developers will happily investing time in learning advanced JavaScript features, algorithm optimizations, and new frameworks. But when it comes to HTML elements, most of us stick with what’s already comfortable.

Have you ever consider learning about HTML elements beyond the old standbys: <div>, <span>, <h1>, and <p>?

For example, there’s the <dl> element, which might be u[seful when writing a gl](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dl)ossary.

Then there’s the <time> element. It will allow browse[rs to schedule events to your user’s ca](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/time)lendar.

Were you about to use the <b> element to make something look important by making it bold? Consider using the <strong&[gt; ele](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/strong)ment instead. Screen readers don’t communicate styling to the users. But they would communicate the semantic meaning of the <strong> element.

Are you importing a library to get a color picker or calendar on your screen? Consider using <input type=”color” /> or <input type=”date”> to use what the browser gives you.

Take a moment to familiarize yourself with some of the [HTML elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Element) that are available to you.

And next time you’re working HTML, ask yourself whether you’re reaching for the right tool.

