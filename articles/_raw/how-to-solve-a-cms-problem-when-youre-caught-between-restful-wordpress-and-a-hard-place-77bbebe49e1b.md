---
title: How to solve a CMS problem when you’re caught between RESTful, WordPress, and
  a hard place
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-19T02:34:57.000Z'
originalURL: https://freecodecamp.org/news/how-to-solve-a-cms-problem-when-youre-caught-between-restful-wordpress-and-a-hard-place-77bbebe49e1b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*IQ9QA3Sy1kX7XdmZmFwlYg.jpeg
tags:
- name: cms
  slug: cms
- name: General Programming
  slug: programming
- name: storytelling
  slug: storytelling
- name: technology
  slug: technology
- name: WordPress
  slug: wordpress
seo_title: null
seo_desc: 'By Jessica Duffin Wolfe

  Last fall I was trying to decide on how to host and manage a small storytelling
  project built by around 40 users — my students. I wanted them to have a clean and
  easy experience uploading their content (images and audio files,...'
---

By Jessica Duffin Wolfe

Last fall I was trying to decide on how to host and manage a small [storytelling project](http://36to.ca/#/) built by around 40 users — my students. I wanted them to have a clean and easy experience uploading their content (images and audio files, along with some text). I also wanted it to be stored long-term in a format my little Vue.js app could easily pull in to display without a lot of set up and overhead on my part.

I’ve relied very happily on WordPress as a primary Content Management System (CMS) for years, but it’s been feeling a bit old lately, and it’s not quite designed for such a heavily AV-based, multi-user project, so I decided to look around for good fresh options.

### **Option 1: Google Sheets**

The simplest path seemed to be setting up a Google Sheet the students could populate with links to their own self-hosted media. I’ve had good experiences building small sites like this before pulling in the data through JSON.

For this case, though, with around fifteen different content pieces going into each user’s contribution, if I used a spreadsheet it would be a beast, and populating it would not be a good user experience for the students.

The links to the students’ self-hosted media also risked going bad over time, as accounts lapse, and services dry up. I didn’t want the project to get patchy, and I didn’t want to have to do too much maintenance on it each year to keep it solid.

So, no to Google Sheets.

### **Option 2: Contentful**

[Contentful](https://www.contentful.com/) is a headless CMS, which means it provides infrastructure for storing, editing, and serving content without providing any sort of front-end display. Traditional WordPress, in contrast, is set up to do both — store your content, and offer up all the code that retrieves and displays it. This big stack of abilities makes it pretty bulky, and increasingly it doesn’t feel as nimble as a web tool should.

I was really excited about Contentful. It’s so pretty and slick! And so smart — it permits direct geotagging of content! Ahhh. And I could set up a custom content model that exactly matched the project at hand, and it was fun! Yay.

After spending some time configuring Contentful, I desperately wanted to use it, but I began to lose interest the more I thought through how the students would upload their work.

The free tier maxes out at five users. While I could have had the students upload their content through one generic user account, this would not have been a good experience, as they would have had to wade through the back end and other people’s files to submit their work.

I also wasn’t convinced that the free tier would have covered the hosting needs of this project. It probably would have been fine — but I would have found myself keeping an eye on bandwidth and API requests and the longterm status of the content.

With the first paid tier starting at $249 per month, levelling up was too expensive to consider. That pricing deterred me from even wanting to use a free account, because I knew I would never upgrade at that price. So there was a chance I’d need to migrate everything if I started building the project on the service.

It was clear Contentful didn’t really want the business of small-scale experimental work — fair enough — and anyway it was getting too annoying to be fussing over these details for a little project.

### Option 3: RESTful WordPress

While I was trying to make Contentful work, I kept switching back to a WordPress install to play around. Bulky though the old WP can be, faced with Contentful’s nickle-and-dime approach of charging for content “records,” I was starting to feel very nostalgic for the ease and freedom of adding content in WordPress.

I thought — well, hey — why not use WordPress as a headless CMS with its new REST API feature? This would let me get around the bulk of serving content through PHP, while still allowing me to use WordPress as a CMS, an interface my students know well.

To allow the students to add all the images and audio for their projects, I would need to add a custom post type. To do that I would need to add a plugin. To use the plugin I would need to figure out how to configure it, and then create an appropriate custom post type that would provide in an easy-to-use interface inside the WP system. To do that I would need to rewrite WordPress from the ground up, because bless its heart it is not built to do anything other than look and feel like WordPress. It manages blog posts really, really, really well, and can be muddled into doing some other things sort of but not well. The whiff of the blog post never really fades.

I gave up on all this before even trying to figure out how I would use the REST API in my project. I’m still excited about it, though. It’s probably an amazing option for serving content from larger sites using JS frameworks.

### **Option 4: WordPress + Forms = CMS Sugar**

The solution I finally settled on seemed ridiculously simple and a funny amalgam of all my earlier efforts.

Using Gravity Forms, a WordPress plugin I know my way around from other projects, I built a basic form through which the students could upload all fifteen of their files, and paste in their text components.

I exported the entries as a spreadsheet with links to the uploaded content stored in the WordPress site, and I turned this file into JSON to use just as I would a Google Sheet.

So my students got a clean, familiar, and accessible experience uploading their content, and I will be able to store it long term without hassle in a format my static web app will play nicely with. Problem solved.

Ta da! Why was this solution not more obvious when I began?

For me, one moral of this story is that even in this era of increasingly fancy decoupled and well-rested deployment options, it still helps to know your way around WordPress — that despite getting a bit long in the tooth, its low-cost, and feature-rich ecosystem continues to lower barriers to digital creativity.

