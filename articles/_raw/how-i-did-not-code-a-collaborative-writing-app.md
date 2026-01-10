---
title: How I did NOT code a collaborative writing app
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-18T17:19:33.000Z'
originalURL: https://freecodecamp.org/news/how-i-did-not-code-a-collaborative-writing-app
coverImage: https://www.freecodecamp.org/news/content/images/2020/02/code-free-1200-2.png
tags:
- name: bubble
  slug: bubble
- name: code
  slug: code
- name: Entrepreneurship
  slug: entrepreneurship
- name: lean startup
  slug: lean-startup
- name: web
  slug: web
seo_title: null
seo_desc: 'By Eric Burel

  Twaikura, haikus but funnier

  As easy as ABC: some stranger on the Internet starts a 120 characters story, some
  stranger on the Internet finishes it. And that makes a Twaiku (tweet + haiku). Twaikus
  can be funny, serious, artistic, it’s ...'
---

By Eric Burel

## Twaikura, haikus but funnier

As easy as ABC: some stranger on the Internet starts a 120 characters story, some stranger on the Internet finishes it. And that makes a Twaiku (tweet + haiku). Twaikus can be funny, serious, artistic, it’s up to you. 

![Image](https://www.freecodecamp.org/news/content/images/2020/02/logo_256.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/02/twaiku.png)

So, as a developer, implementing something like that shouldn't be hard, right? Yes, but no. Here is the story of how it took me multiple years to create Twaikura and how you could do the same in a matter of hours.

## Back to TwentyParts and why it never came to existence

TwentyParts was my first “entrepreneurial concept” back in 2015. As you may guess, the idea is to write a story in 20 parts, with each part written by a different author. 

I was a CS student at the time and it took me 2 months to release a first draft. The result was disastrous. I didn’t even know about the concept of a “framework”, picture the code. The concept was too complex, the interface unusable.

I did not give up. A few months later, in 2016, I came up with a simplified version of TwentyParts, HiKoo.  I limited the length of a story to 3 tweets. And instead of rushing to development, I created mocks using a marvelous tool named MarvelApp.

Now I had a great UI and all, but no working code. One more app that never came to existence.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/hikoo.png)
_Looks good, doesn't work_

Fast forward to now. I’ve graduated. I’ve built my consulting company, LBKE. I’ve developed complex SaaS platforms for multiple clients. And I've kept this question running in my head:

> What prevents me from recreating TwentyParts, now I am fast and skilled and over-confident?

After all, it would only take a full work week nowadays. Yet there’s a problem: I am not a student anymore. With one spare hour here and there, a “full work week“ can span over a few months. Too slow.

## How to code fast: don’t.

I’ve explored thoroughly the realms of fast web development. You may have read my previous articles on freeCodeCamp about [Vulcan, a framework based on Meteor that makes me very productive.](https://www.freecodecamp.org/news/how-i-built-an-app-with-vulcan-js-in-four-days-6368814077b1/)

Those researches all lead me to the same conclusion: the best code is the code you don’t write. 

There are a lot of ways NOT to write code, even for a developer. Scaffolding, declarative programming, using snippets, or using an ORM are all methods to circumvent writing code. Using open source is another great example. Some may even think that developers are a bit lazy – but aren't they?

Yet minimal skills in web development are still necessary. That means careful thinking, lots of doc reading, debugging and so on. In the end, the time needed to create a fully functional app can only be reduced this much.

You know what? Using a massive framework to speed up developments feels like cheating sometimes. What if I did not have those skills? What if I was not a developer? I would have no other choice than embracing the “no-code way”. And that’s what I’ve done.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/code-free-1200.png)
_Relax, Code will be on vacation for the remainder of this article_

## Sparkling innovations for web non-developers

No-code solutions have been pretty bad in the past. Limited, difficult to extend, proprietary, expensive, the list is long. But some recent tools are starting to be worthy enough.

I will focus specifically on Bubble. Its plugin system coupled with its data management features makes it the most complete solution on the market currently. Here are a few key features and how I used them to build Twaikura.

### The UI editor

Bubble proposes a WYSIWYG editor (What You See Is What You Get) to create the app user interface. You put your blocks of content wherever you want, and configure their content.

It’s grid-based so you can have pixel perfect alignment. It handles responsiveness. So you should be able to create designs as complex as you wish.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/ui-bubble.png)
_Building Twaikura's interface using the WYSIWYG editor._

But I’ll be honest, I am not the hugest fan. More precisely, I am not very good with it. It’s very different both from writing HTML/CSS and from using web-based design tools like Figma, so there is a learning curve.

I ended up sticking myself to an old school Windows 98-ish style. With a little bit of imagination you could even believe it has some “V a p o r w a v e” aesthetic.

### Thinking in workflows

The most impressive feature of Bubble to me is its “Workflows”. It lets you describe complex process in a visual language. It can mix data management (validating and storing a Twaiku, sending an email) and user experience (resetting a form, refreshing the page) transparently. You don’t need to mentally split the workflow between frontend and backend as you would do in a traditional web app.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/workflows.png)
_Twaiku creation workflow_

This example workflow is triggered when the user wants to submit the second part of a Twaiku. It will create a "Twaiku End" in the database, link it with a "Twaiku Begin", and reset the form. I could also display a success message, send a mail to a moderator and so on. Visualizing the full workflow in a single timeline is very intuitive.

### Complete data management

Bubbles comes with a relational database and complete filtering features. That means you can easily create both forms and list of data. For example, the “Read latest Twaikus” block will load all valid Twaikus.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/twaikus-list.png)

Plugins can help secure your content. For example, there is a ReCaptcha plugin to add CAPTCHAs to your form in a matter of minutes. This is important as security is usually left behind in the prototyping steps. Malevolent bots and hackers don't care that you are a "lean startup-er", and they won't miss an opportunity to spam or hack your website.

## A few hours of work for an app that works

I won’t describe all features of Bubble, because it has a lot more. The conclusion is that it's been powerful enough to write an app like Twaikura. Instead of writing tons of crappy code that will end up in a dumpster, instead of creating a visual prototype as lively as Frankenstein’s Creature, I just created something that works.

Is my website great? Honestly, not yet. Does it do the job? Hell yes. I had fun creating it, it cost me no more than a few hours, and I am able to test the concept in the most direct possible way. The longest part was writing this article.

I especially recommend no-code tools for people who want to learn web development. Taking a lot of time to produce simple features can feel frustrating at first. Using a no-code tool alongside traditional programming is a way to keep having fun. It's instructive too, because, even if you don't write code, you still have to think like a developer: designing conditional workflows, structuring a database, validating forms... That's a win-win.

I won't become a no-code evangelist, but Bubble is a great addition to my tool belt. And it could be great addition to yours too!

Thanks for the read. If you liked this article, come try a Bubble app by creating your first Twaiku on [twaikura.com](http://twaikura.com)!

<a href="https://twitter.com/lbke_fr">
<img src="https://www.freecodecamp.org/news/content/images/2019/10/Medium-follow-2019.png" alt="LBKE banner twitter" />
</a>


