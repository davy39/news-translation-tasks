---
title: 'How a C++ developer learns JavaScript: a frustrating but ultimately satisfying
  tale'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-26T19:41:22.000Z'
originalURL: https://freecodecamp.org/news/tales-of-a-c-developer-learning-javascript-96b0a3324d25
coverImage: https://cdn-media-1.freecodecamp.org/images/1*1sxcjy4QPYQGMyOlkwqHjQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By DHARA DOSHI

  This year I started my journey into Web Development. As the umpteenth article on
  the web will profess: JavaScript is the holy grail.

  And so I began my journey into this new stack, new domain, and a whole new level
  of newness.

  So, in th...'
---

By DHARA DOSHI

This year I started my journey into Web Development. As the umpteenth article on the web will profess: JavaScript is the holy grail.

And so I began my journey into this new stack, new domain, and a whole new level of newness.

So, in the middle of the day, in the middle of a feature I was implementing, I was almost at the stage where I felt like pulling my hair out. My frustration knew no bounds, and my impostor syndrome was at an all time high.

Before I tell you any more about what issue nearly turned me insane, let me give a bit of a background about myself.

I have basically just started scratching the surface of JavaScript, and have taken a few FreeCodeCamp lessons (and have marveled at what [Quincy Larson](https://www.freecodecamp.org/news/tales-of-a-c-developer-learning-javascript-96b0a3324d25/undefined) has accomplished). Since the time I started my journey as a Computer Science graduate more than 10 years ago, I’ve never seen coding being taught in such a structured manner before.

I started JavaScript development in February 2018 (after I took a course with edX on JavaScript & JQuery, called [Programming for the Web with JavaScript](https://courses.edx.org/courses/course-v1:PennX+SD4x+2T2017/courseware/05f321f8b38c400b96330598e23d639c/66cdc9f1359c44e698177abcd5ab480e/?activate_block_id=block-v1:PennX+SD4x+2T2017+type@sequential+block@66cdc9f1359c44e698177abcd5ab480e)). This means I have been at it for five months now. I am strangely indignant that I got stuck on this issue now rather than a few months back, but a developer hardly has an choice with things like that. You just have to swallow your ego, every freaking time. And learn!

Are you wondering what specific JavaScript issue made me ask all existential questions in my life?

### An illustrated story of Mr. Monday, the button.

This is the story of a button:

![Image](https://cdn-media-1.freecodecamp.org/images/1*OZlc_3RUxnM-3KG0BnNIHA.png)
_Meet Mr. Monday (a button )_

Mr. Monday’s personality can be defined as:

```
<button type=”button” class=”btn btn-sm btn-success” id=”<mon-week-day”>MON</button>
```

But Mr. Monday isn’t as original as we want him to be. He was based on a template, and the source of his real personality was something like this:

```
<button type=”button” class=”btn btn-sm btn-success” id=”<%=day%>-week-day”>day.substr(0, 3).toUpperCase()</button>
```

```
where day is the days of the week: monday, tuesday, wednesday etc.
```

Disclaimer: The code is <%= day %&g[t;](http://ejs.co/) is EJS.

I wanted to give Mr. Monday’s personality a shade of gray in some situations.

![Image](https://cdn-media-1.freecodecamp.org/images/1*JylMwILuBZEokQBARkq_Ow.png)
_Doesn’t he look gorgeous ? :P_

But Mr. Monday just didn’t know how to have any fun. Sigh! He wouldn’t turn gray!

### How I finally brought out the best in Mr. Monday

I said to him let’s do this, so let me groom you to add class to your persona.

```
$('#'+day+'week-day').addClass('unselected')
```

He didn’t budge. I changed the addClass to toggleClass and still nothing happened. I think he wasn’t keen about being ‘unselected’, though I explained to him why it was essential.

Then I brought out the big guns, the console. And I tried to change him there. The console threw some doubt on Mr. Monday’s capability to turn.

It would say that it changed the color, but I would still see a very green Mr. Monday. So what was happening here? [My Sherlock mind](https://medium.freecodecamp.org/why-i-feel-like-i-am-sherlock-at-my-software-job-4a303ebdaf63) came to my rescue and voilà, I realized the biggest mistake ever know to mankind in the history of programming (or at least in my mind it appeared like the biggest screw up ever).

There was another element with the same id as Mr. Monday. This was why he wouldn’t budge and all the changes were probably being targeted to the other guy. An acute case of identity crisis, I must say!

How did this happen? Well, have you heard of the phrase “Too many cooks spoil the broth?” That’s what happened: two or three people had worked on the same file before, and somehow this new id matched with one of the id’s they had used before for an element. Phew, this was such an important lesson for me.

**All elements should have unique ids.**

Anyway, I changed Mr. Monday’s id, and tried again.

```
<button type=”button” class=”btn btn-sm btn-success” id=”<monday-hours-day”>MON</button>
```

```
$('#'+day+'hours-day').addClass('unselected')
```

And still, Mr. Monday wouldn’t turn gray.

### Fixing the biggest mistake ever

After a few hours of googling, wondering if this really was what I wanted to do for the rest of my life (eyeballs almost out of my eye sockets trying to find ways to turn Mr. Monday gray), I figured out what the problem was.

And I know you are dying to find out. I promise when you know, you’ll hate me for making the silliest mistake in human history.

The problem was that I missed a ‘-’(hyphen) in the id before hours, when adding class unselected.

```
$('#'+day+'hours-day').addClass('unselected')//is clearly wrong.
```

```
$('#'+day+'-hours-day').addClass('unselected') //is the perfect code ever
```

Mr. Monday finally turned gray! This gave me such immense happiness I slept like a puppy that day! Yes, just like the one in this picture.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ok7ZH_FQDizV5A8-QeyY8w.jpeg)
_Photo by [Unsplash](https://unsplash.com/photos/JCXANpeR2XI?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Adam Grabek</a> on <a href="https://unsplash.com/search/photos/happy-sleeping?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

**To read more stories about my escapades in code land, please motivate me by clicking on the ‘Applause’/’Claps’ icon multiple times — ideally 50, but if you are as lazy as I am, I’ll accept 20 of them (Nothing less than that please ;) ).**

_Originally published at [www.heisenbugtech.com](http://www.heisenbugtech.com/2018/06/26/tales-of-a-c-developer-learning-javascript/)_

