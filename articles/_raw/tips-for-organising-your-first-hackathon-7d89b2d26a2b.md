---
title: Tips for organising your first hackathon
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-07T16:58:44.000Z'
originalURL: https://freecodecamp.org/news/tips-for-organising-your-first-hackathon-7d89b2d26a2b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*RwFLcMAsMJhdbrabPA7j-w.jpeg
tags:
- name: hackathon
  slug: hackathon
- name: learning
  slug: learning
- name: startup
  slug: startup
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Richard Middleton

  On Saturday July 14, freeCodeCamp Oslo had our first hackathon. In the spirit of
  togetherness, we decided to make our hackathon non-competitive. We have lots of
  people who are very new to coding, and wanted them to feel they coul...'
---

By Richard Middleton

On Saturday July 14, freeCodeCamp Oslo had our first hackathon. In the spirit of togetherness, we decided to make our hackathon non-competitive. We have lots of people who are very new to coding, and wanted them to feel they could participate and learn something along the way.

Here at freeCodeCamp Oslo, we try to bring a deep sense of community and togetherness.

Like many freeCodeCamp groups, we have a lot of expats — people who have moved to Norway, away from friends and family. This community helps many people, including myself, get out there and meet other developers and form relationships.

![Image](https://cdn-media-1.freecodecamp.org/images/AqfJlztuuRLRtQZSi057bUFunPpjDfXPzQNo)
_fCC Oslo Meetup._

Leading up to the hackathon, we decided whether we were going to make it a one- or two-day event, based on feedback from the group.

After securing a venue at the amazing [Explorer HQ](https://www.explorer-hq.com/) (thanks to Marek, one of our admins), we decided to ask our campers for ideas for the project.

In total we had seven ideas, and the week before the event we looked at how feasible they were for us in the 12 hours we had.

We finally settled on making a web app where users could see if any students were studying around them. We added an invite to the map to welcome collaboration, and users could post their location for others to join their study session.

Starting at 10AM, we had a few introductions and decided on how to split the tasks.

We had many beginners to web development amongst us. All were happier contributing to the front end, or interested in learning it. This meant it was up to myself to work on the back end.

![Image](https://cdn-media-1.freecodecamp.org/images/tML3FJbawSkRSMjxtZV6jZGENRKTf2M7a60k)
_Courtesy of [richardCodes](https://instagram.com/richardcodes" rel="noopener" target="_blank" title=")_

The main problem we had was being unable to use frameworks like React to keep our API calls secret. Many of the team haven’t used a framework like that before. Instead, we decided on HTML & CSS for a static front end, using jQuery to make the AJAX requests.

We also used Bootstrap 4, which allowed quick prototyping. Its strong documentation helped the front end come together.

Another one of our admins, Ekaterina, was in charge of the client-side Javascript. With Marek, she planned to oversee the general front end development.

The repo was created by Howie, another admin for freeCodeCamp Oslo, and after permissions were granted we started work.

The front end team dived into the Google Developers docs and quickly displayed a map on the front end.

The back end was going to use NodeJS with MongoDB and Express, so first a NPM init was done along with installing Express, Mongoose, Body Parser and a few other packages. Within an hour and a half, we had our API working.

While waiting for the front end, we were able to test the API using Postman to GET and POST data to and from our database.

![Image](https://cdn-media-1.freecodecamp.org/images/syfV8X3iHGDdk-PzMttuIE8aiommg2m3JtI1)
_Pizza Time, The Staple of any Hackathon._

After lunch (also kindly sponsored by Explorer HQ), we made a few incremental changes for database entries. But most of the work was for JavaScript on the front end, making sure we could send our GET and POST requests from there.

Soon, our minimal viable product was [finished](https://studyfinderoslo.herokuapp.com/).

![Image](https://cdn-media-1.freecodecamp.org/images/YC-POwZJp3XMhXxE7k69MBdN5ea39ExEARtk)
_[https://studyfinderoslo.herokuapp.com](https://studyfinderoslo.herokuapp.com/" rel="noopener" target="_blank" title=")_

It was great working in a team, which none of us had really done before.

We hosted the site on Heroku, and the database was hosted with MLab. After a long day, we had a usable product which we couldn’t be more happy with.

There were still things to work on, but our MVP was achieved. The next day, I remedied our open API by using Passport to add Facebook authentication.

Also, we added a few fixes to the site.

![Image](https://cdn-media-1.freecodecamp.org/images/hujz-3PZ2CPGMVD9jtlqfmM6gsctnJnMvz7q)

Altogether the experience was great. Working as one team of eight people helped make the environment friendly, and brought everyone together — which was our aim.

I implore you to try it yourself and set up a non-competitive hackathon for your group!

### So how can you set up your own hackathon?

1. **Keep it to one day** — a weekend day will work best. Spreading the event over multiple days means you may not get the same people attending both days, and this could be a problem for continuity. We found it best to poll our group with multiple dates and pick the most popular.
2. **Find a project in advance** — we crowdsourced our idea process, asking users to submit their ideas a week in advance. This way, the group leaders could get together and check out feasibility.
3. **Secure a venue** — this can be a tricky one, because you need a big enough space, with good wifi and power. Ideally, you want to be able to bring in your own snacks etc. Maybe someone in your group has a workplace that is free on a weekend? Don’t feel intimidated to get out there and drop some emails to people in the tech community. Failing that, get everyone round to your place.
4. **Make it collaborative, not competitive** — we are all learning and some may feel out of their depth if you make it competitive. Split the group up into different sections. Maybe you have a frontend lead and a backend lead, and they can then split people into dealing with nav-bars, modals, JavaScript, databases, etc. Don’t be afraid to step up even if you don’t feel you know what you’re doing — you may surprise yourself!

You don’t need to have run a hackathon before — I had never even been to one before! The whole experience brought our group closer together. We managed to build something cool that could go in our portfolio, and we can all claim to have won freeCodeCamp Oslo’s Summer Hackathon!

You can check out the repo [here](https://github.com/howieandersen/FreeCodeCampHackathon001). The hosted site is [here](https://studyfinderoslo.herokuapp.com/).

