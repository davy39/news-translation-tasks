---
title: A developer's guide to web design for non-designers
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-10T23:14:16.000Z'
originalURL: https://freecodecamp.org/news/a-developers-guide-to-web-design-for-non-designers-1f64ce28c38d
coverImage: https://cdn-media-1.freecodecamp.org/images/0*oxy0rmCY12MH-J2r
tags:
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: UX
  slug: ux
- name: Web Design
  slug: web-design
seo_title: null
seo_desc: 'By Patrik Krupař

  I created my first website as a school project when I was 14. The task was simple:
  create a very basic site including some text, images, and a table. My usual attitude
  to school projects was to completely forget about them and later ...'
---

By Patrik Krupař

I created my first website as a school project when I was 14. The task was simple: create a very basic site including some text, images, and a table. My usual attitude to school projects was to completely forget about them and later come up with some last-minute solution. But, this time, I went nuts.

Since my first website, I’ve always prioritized making stuff look good. Admit it or not, people judge things based on looks. If what you make looks good, like you know what you’re doing, people are going to trust it more. That’s just how things are.

![Image](https://cdn-media-1.freecodecamp.org/images/oqhMscYYKfC7BC4SRi7eBsvnUVaUCZzOlxo7)

Over years of making side projects, I shifted my focus more and more on developing my design skills rather than just perfecting my programming. You see, being an algorithm writing monstrum gets you just so far. While pursuing the dream of bootstrapping a profitable side project, you’ll have to do a lot of different jobs. Being a designer is one of them. Just like Cross-fit athletes, solo-founders have to be well rounded to perform well.

A superb design isn’t necessarily the one with the most Dribbble upvotes. It’s the one you won’t notice in the first place. It’s a perfect balance of “your grandma could do that” and “wow, that’s damn nice”. Design can be your competitive advantage or the nail in the coffin.

### It’s not about talent

When I was younger, I played a lot of Minecraft. I saw all these awesome buildings people made. But when I made something, it looked like a box. Ugly and with no style. How do you even make something nice in Minecraft, right?

So, I found a guy on YouTube and built an exact copy of what he built. A few weeks later, I had developed my own style and could build on my own. Suddenly, my creations didn’t look like crap. Heck, I even won a building contest.

Design is a skill, and like any other skill, it can be learned.

![Image](https://cdn-media-1.freecodecamp.org/images/CaiScvTDfplQ-vwIKAQvtv8e-awwd9wMTAUD)

#### Picking the right tool for the job

In programming, you can use Notepad and write an app that’s as good as if it were written in a full-blown IDE…though your life might be pretty miserable doing it and it will probably take noticeably longer. In the world of web design, MS Paint would take the role of Notepad, and like Notepad, few people actually choose to design with it… I hope.

![Image](https://cdn-media-1.freecodecamp.org/images/pU1EqmUdzzDezkZOzoDTAu1GwpQ8dKyECLhI)

#### **The most popular design tools for the web are:**

* [Sketch](https://www.sketchapp.com/), a MacOS only tool that, similar to React, seems to be hard-coded in every job listing. $99/year.
* [Adobe XD](https://www.adobe.com/products/xd.html), a free to use, cross-platform tool that takes the role of Vue. It has a smaller community, but it’s very easy to get started.
* [Adobe Photoshop](https://www.adobe.com/products/photoshop.html), the swiss knife for any design task known by everyone. It’s taken the spot of…you guessed it, jQuery. $9.99/mo.

There’s almost no difference whether you use Sublime or VS code to write apps. Or whether you use React or Vue for the frontend. It’s just a matter of preference. The same goes for design tools, as each one has its pros and cons.

I use Adobe XD. The main reason for me is that it’s cross-platform, so I’m not held hostage by the Apple ecosystem. It’s also backed by Adobe, so it’s gonna be here for a while. The best thing for newcomers is that, since May 2018, Adobe XD is free to use with just a few limitations (that you’re unlikely to stumble upon anyway).

### Adjusting your mindset

The biggest challenge coming to the web design world for me was adjusting my mindset. I was used to coming up with the design as I coded the website. Everything had an order. The flow was from left to right and from top to bottom. The fact is, this approach makes you a worse designer.

Design tools are chaotic because they force you to design like every element is positioned absolutely. Embrace this change. It’ll give you the freedom to change things quickly and makes experimenting easy. And that is essential, because design is an ongoing process. It’s expected that you’ll be changing things a lot before you get a great result.

### Learning the tools

When coding, you use HTML elements like divs, spans, and inputs and let the browser render them into something visual. With design tools, you have the power to skip the middleman and use visual elements like shapes and text directly.

I picked the 4 most used design tools so you can spend less time learning and more time designing. That way, you can start practicing as soon as possible. Below, I’ll show you how they work and how to use them.

#### Rectangle tool

Rectangles are the most universal shape. You’ll find yourself using them all the time. Think of it as a div. It’s useful for all sorts of stuff, from creating text inputs to containers.

![Image](https://cdn-media-1.freecodecamp.org/images/2y3CKLWwGu8EgVir8JwjTiRqMZLvrIk8ulUR)

#### Text tool (label)

Text tool, as the title suggests, allows you to create text. It’s not that simple though, because the text tool has two states: one for single line text and the other one for multiple paragraphs. Fortunately, they’re extremely easy to learn to use correctly.

The first state is a single line text container that adjusts its size based on text size. It’s similar to a <span> with the exception that it won’t wrap unless you make a line break. The benefit of this state is that it’ll automatically adjust the text box size based on line height and font size.

To create it you simply click with the Text tool selected and write. As a rule of thumb, use this state for anything that doesn’t need a specific width and is a single line. For example, single line headlines and labels.

![Image](https://cdn-media-1.freecodecamp.org/images/gGq1dRqeXNvBXpNb4IGzQ7K4Q1fmerBfNPdO)

#### Text tool (paragraph)

The second state is a text container with a specific size that behaves like a <p> with a specific width or <p> inside a grid column. The benefit of this state is that you can control the text box size. To create a paragraph, you click with the text tool selected and hold to create a selection. As a rule of thumb, use this state for paragraphs and headlines on more than one line.

![Image](https://cdn-media-1.freecodecamp.org/images/8zvbn97rmkMs5n8419DGfB2fvPOgq-BXjbBA)

#### Select tool

Move, resize, duplicate. This is the tool for that. Those pink lines show you the distance from surrounding elements. The blue lines help you get elements to align properly.

![Image](https://cdn-media-1.freecodecamp.org/images/aeVtUcAoaPKGkloLjESzXHcctRzNGGb4RhEk)

#### Line tool

Sometimes a line is handy to make parts of design separate. That’s why the line tool is here. You could technically use rectangle tools instead, but hey, so the div could be used for anything.

![Image](https://cdn-media-1.freecodecamp.org/images/LfZZ73IG2CcCPP-hQKvwTS-ScUCISsInsQlk)

### Design tips and techniques

#### Layout

In web development, a layout is most commonly described as a header, menu, content, and footer. That’s a part of it, but a layout is more than that. It’s literally the way that all the elements are laid out.

For example, when I was designing the project information for [Sidemail](https://sidemail.io/), I distributed elements inside of a card evenly which makes it feel more complete and looks cleaner.

![Image](https://cdn-media-1.freecodecamp.org/images/HouX0X2FdRy9EfcIouqDcijoZuxvIp1XKq43)

#### Colors

To help you find the perfect color for your next project, consider keeping in mind the psychology of colors ([colorpsychology.org](https://www.colorpsychology.org/)). A helpful tool to find the perfect color combination based on your primary color is [Paletton](http://paletton.com).

Use shades of primary colors and text colors to create a visual hierarchy. Try darker or lighter shades for your text when using a colored background.

![Image](https://cdn-media-1.freecodecamp.org/images/8rw2o2Ub4Krxb3thxO-IFq6OVDfz0asCkRp0)

#### Typography

Typeface largely affects the branding of your project, so choose wisely. Premium typefaces tend to look better than those on Google Fonts, but when you’re just starting out, don’t buy one. Even on Google Fonts, there are some hidden gems.

A trick that I very often use to visually break up text is to make labels uppercase with larger letter spacing. Uppercase text is symmetrical and looks good from a visual standpoint, but don’t overuse it because it’s much harder to read.

![Image](https://cdn-media-1.freecodecamp.org/images/oOmDF-bv6qdYzwptaxgv-XnygSPVjs1lO5gO)

### Designing a homepage (or a landing page)

I always try to avoid the temptation to design trendy elements and then cram my message into it. Rather, I come up with benefits (not features), put them into a story, and tell that story by a visually appealing page.

After I establish what I want to say, I usually look for some inspiration. A great resource for that is [land-book.com](https://land-book.com/), a vast directory of great looking landing pages that people can vote on. Another great page with design inspiration is [interfaces.pro](https://interfaces.pro/) where you can filter by categories like pricing, 404, or about us. I just browse through until I find enough sites that I like and match my desired style.

![Image](https://cdn-media-1.freecodecamp.org/images/TvNk8LNOUBysBYLyvFD6MQkn7mDGRWBQ215N)

The hard part is putting it all together. Unfortunately, there’s no shortcut. You just have to iterate a lot until you get a result you’re happy with.

You may find yourself wondering whether it’s normal that a design you were completely happy with a week ago suddenly feels not good enough or even ugly today. The answer is that it’s perfectly normal and actually a good thing. It’s essentially because you grow, learn, and become better. Yesterday’s challenge is not so challenging today. Keep this in mind so you don’t get stuck in a rat race.

#### Takeaways:

* Unique typeface makes a huge difference
* Graphics are very important, try to use at least some illustration or images
* Get visual importance right by using multiple shades of colors. Text and primary colors aren’t enough.
* Don’t use containers that are too wide — around 1100 px is wide enough
* Embrace the negative space
* Talk about benefits, not features
* Look around for inspiration if you get stuck

### Designing a web app (or a dashboard)

As with designing a landing page, don’t jump straight into designing. This time, you’re not trying to tell a story. Instead, the goal is ease of use. Grab a pen and paper and make a plan of how your app should work, what should depend on what, and how to navigate easily.

Make some sketches or wire-frames if necessary. Do a proper competitor design inspection to see for yourself what’s lacking and can be done better, or possibly even turned into a competitive advantage. Sometimes, it’s better to take a break before making plans on paper and designing.

The best advice I can give that’s not use case specific is to choose a proper page layout. Generally, all web apps use two different page layouts based on the app’s purpose: fixed width container or fluid container that fills your entire screen.

![Image](https://cdn-media-1.freecodecamp.org/images/auTuV6Yns5sidXSDFFtV5LhdAkslL1vzoYaK)

#### Fixed container

I prefer the fixed container, because it’s much easier to focus on a tight area as it prevents unnecessary eye movement. Fixed container apps also tend to be cleaner looking and less overwhelming for new users. However, because of the smaller width, fixed container apps are harder to design.

Examples: [Twitter](https://twitter.com/), [Buffer](https://buffer.com), [DigitalOcean](https://www.digitalocean.com/), [Netlify](https://www.netlify.com/), [GitHub](https://github.com/)

#### Fluid container

Fluid container apps are a great fit for chat apps, spreadsheet apps, and other apps where more stuff on a screen is essential. But be aware that loads of data on a screen can get overwhelming.

Examples: [Slack](https://slack.com/), [Intercom](https://www.intercom.com/), [Hotjar](https://www.hotjar.com/), [Google Sheets](https://docs.google.com/spreadsheets), [Trello](https://trello.com), [Spotify](https://open.spotify.com/)

It’s important to pick the right container, because your whole page layout will depend on it and changing it later is a lot of work. Each project is unique and calls for unique solutions, so don’t be afraid to experiment!

#### **Takeaways:**

* Keep it simple
* Use readable typeface
* Use visual hierarchy when displaying lots of data
* Take advantage of competitor’s poor design choices

### Wrapping up

Remember, design can be your competitive advantage — so use it and make something awesome.

Kick start your designing journey by [getting an Adobe XD template](https://hosted.sidemail.io/5d03f67a4e7f1600fda5ae11) I made for my newest project’s landing page. Simply [subscribe to my brand new email list](https://hosted.sidemail.io/5d03f67a4e7f1600fda5ae11) and it’ll land in your mailbox.

Also, you’ll be the first to get notified about my next post where I’ll share 69 days of progress I made on [Sidemail](https://sidemail.io/) — a SaaS project I work on. It’ll include things like subscriber counts, site visits, spendings, and design drafts. It should go without saying, but I guarantee absolutely no spam. I don’t even have time for that crap.

_My Twitter DMs are open so if you get stuck making your designs or have some further questions, [feel free to hit me up](https://twitter.com/pkrupar)._

