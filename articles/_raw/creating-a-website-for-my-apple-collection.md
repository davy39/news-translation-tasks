---
title: How I created a website for my Apple collection
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-08T16:42:49.000Z'
originalURL: https://freecodecamp.org/news/creating-a-website-for-my-apple-collection
coverImage: https://www.freecodecamp.org/news/content/images/2019/11/collection.jpg
tags:
- name: mac
  slug: mac
- name: projects
  slug: projects
- name: Website design
  slug: website-design
seo_title: null
seo_desc: "By Leonardo Faria\nA while ago I started an Apple collection. I've been\
  \ following Apple hardware (and its aesthetics) since I was a teenager, but at that\
  \ time I didn't the have money to own a Mac. \nI got my first Mac when I was 19.\
  \ It was an iBook 700..."
---

By Leonardo Faria

A while ago I started an Apple collection. I've been following Apple hardware (and its aesthetics) since I was a teenager, but at that time I didn't the have money to own a Mac. 

I got my first Mac when I was 19. It was an iBook 700 Mhz, acquired on an eBay-like website in Brazil. The money came from a Flash project. 

After living in Canada for a few years now, I have some extra money to spend on a hobby. Most of the time I buy the devices from people on Craigslist.

After a few laptops and iDevices, I decided that I should start collecting info about my iThings. In the beginning, I created a Gist containing the model, serial number, how I got the device, the minimum/maximum OS, and so on.

The list kept getting bigger and bigger, and the content started looking messy. I thought showing this content on a website would be perfect, and I didn't need to hire a developer :D 

At first, I decided I would organize my data in an SQL database, with the information distributed in different columns and tables. After that, I would create a graphQL API to provide me the data needed to populate my UI – probably written in React, compiled with Babel and packed with Webpack.

Reading the previous paragraph aloud, you can see that there are many technologies, and that I even ignored the backend language and UI details like SASS or styled-components. It all sounded a bit overwhelming when my ultimate goal was showing a list of items in a nice design.

That being said, I thought about how I can deliver this content without:

- An API or any backend work
- Any JS framework/library
- Any JS tooling (Webpack, Babel, etc.)
- Any CSS work

On top of these constraints, I had a few stretch goals:

- Create a website with good accessibility
- Create a website that works on old browsers, since I have computers running Mac OS 9.2 and iDevices running iOS 3

Challenge accepted. One index.html, a few vanilla JS files, and no custom CSS. I'd like to share the experience of building the site with you.

TL,DR:

- [Final website](https://bit.ly/collection-website)
- [Source code](https://bit.ly/collection-source)

Let's talk about the constraints, point by point:

## No API or any backend work

A while ago I saw a SaaS product called [Stein](https://steinhq.com/). You create your data inside a Google Sheets document and they give you an endpoint with your data. Their library works like Handlebars, and it looked perfect for my use case:

```html
<div data-stein-url="https://api.steinhq.com/v1/storages/5cc158079ec99a2f484dcb40/Sheet1" data-stein-limit="2">
  <div>
    <h1>{{title}}</h1>
    <h6>By {{author}}</h6>
 
    {{content}}
 
    Read on <a href="{{link}}">Medium</a>
  </div>
</div>
```

## No JS framework/library and tooling

I decided to avoid adding a framework or library in this project since the use case didn’t need one. All JS interactions on this page are quite simple (show/hide menus, open a modal screen, handle permalinks).

Since I was not using a framework/library, I could avoid adding Webpack and Babel. No need to dig into presets and loaders.

P.S. You can argue that I could have chosen create-react-app or Next.js and get all these problems solved, but no.

## No CSS work

I love writing CSS, especially when I can use SASS, but I decided not to write any CSS here. I had a few good reasons to avoid doing it:

- I had no designs in mind, and despite the fact that I could do something decent-looking, I didn’t want to put time and energy into it
- I wanted to use [Tailwind CSS](https://tailwindcss.com)

If you've never heard about Tailwind CSS, please don’t just think, “It's just an alternative to Bootstrap.” Here is a good, short explanation from their website:

> Most CSS frameworks do too much.  
> …  
> Instead of opinionated predesigned components, Tailwind provides low-level utility classes that let you build completely custom designs without ever leaving your HTML.

This is pretty much true. A quick search gives you many web apps “rebuilt” with Tailwind CSS:

- [Whatsapp](https://tailwindcomponents.com/component/whatsapp-web-clone)
- [Telegram](https://tailwindcomponents.com/component/telegram-desktop-using-tailwindcss)
- [Facebook](https://tailwindcomponents.com/component/facebook-clone)
- [Reddit](https://tailwindcomponents.com/component/reddit-clone)
- [Youtube](https://tailwindcomponents.com/component/youtube-clone)
- [Slack](https://tailwindcomponents.com/component/slack-clone-1)
- [Coinbase](https://tailwindcomponents.com/component/coinbase-clone)
- [Github](https://tailwindcomponents.com/component/github-profile-clone)
- [Trello](https://tailwindcomponents.com/component/trello-panel-clone)
- [Twitter](https://codepen.io/drehimself/full/vpeVMx/)
- [Netlify](https://www.youtube.com/watch?v=_JhTaENzfZQ)

## Create a website with good accessibility

Last month I started taking accessibility courses at [Deque University](https://dequeuniversity.com/curriculum/packages/full). Their content is great and it reminded me that **HTML is accessible by default**. By using a semantic HTML structure and testing basic things like keyboard navigation and colour contrast you eliminate several barries that move people with disabilities away from your content. 

I am not an accessibility expert, but here are a few accessibility-related things I’ve worked on for this website:

- Disable stylesheets: By disabling stylesheets you can ensure that your content follows a logical/structural way.
- VoiceOver: VoiceOver is included in macOS and iOS. It is [very simple to use](https://webaim.org/articles/voiceover/), and by experimenting with it you can have a better understanding of how people use this feature. 
- Modals: Modals can be problematic. I decided to follow [Ire Aderinokun’s](https://bitsofco.de/accessible-modal-dialog/) approach.
- [axe](https://chrome.google.com/webstore/detail/axe-web-accessibility-tes/lhdoppojpmngadmnindnejefpokejbdd): The extension is an accessibility checker for WCAG 2 and Section 508 accessibility rules. 

It is not perfect -- there are a few things that I didn’t work on for my site, like adding a skip link to the main content. If you are curious, [here is the Pull Request with all the changes](https://github.com/leonardofaria/collection/pull/1).

## Create a website that works in old browsers

I couldn’t achieve this objective since I had no control over scripts and styles. However, it doesn’t seem to be impossible. A few things I noticed:

- [Expedite](https://github.com/SteinHQ/Expedite) (Stein client) uses [fetch](https://github.com/SteinHQ/Expedite/blob/master/index.js#L51-L54), which was only [added in Safari 10](https://caniuse.com/#feat=fetch). The request to their server could be probably replaced with an XMLHttpRequest.
- Tailwind uses Flexbox in many elements. Safari only started supporting Flexbox in iOS 7. Maybe I could write a few properties for their existing elements to achieve a decent look.
- SSL Certificates may be an issue for old browsers.

## Conclusions

Making this website was super fun. Having this kind of pet project gave me a good reason to work with tech that I don't use in my job. Maybe in the future, Stein and/or TailwindCSS will be useful to prototype a feature or build a hackathon project. 

The fact that I added “constraints” to my project made me think outside the box. Even though I didn't achive all my objectives, it helped me understand more and more about how all the pieces are connected.

I totally recommend doing something like this to give you a chance to play with different tech. It doesn't need to be an Apple collection -- you can create a site to list your favourite books or the best hikes you've done. In this case, the journey matters more than the goal. 

Out of curiosity, I tracked my time using [Clockify](https://clockify.me) and between coding, creating the data, testing and writing this post I’ve worked 13 hours on this. 

_Also posted on [my blog](http://bit.ly/collection-post). Follow me on [Twitter](https://twitter.com/leozera)_




