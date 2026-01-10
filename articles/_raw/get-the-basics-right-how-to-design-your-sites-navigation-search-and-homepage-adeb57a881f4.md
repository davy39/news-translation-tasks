---
title: 'Get the basics right: how to design your site’s navigation, search, and homepage'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-27T16:13:43.000Z'
originalURL: https://freecodecamp.org/news/get-the-basics-right-how-to-design-your-sites-navigation-search-and-homepage-adeb57a881f4
coverImage: https://cdn-media-1.freecodecamp.org/images/0*judVnmYTutcBhqRI
tags:
- name: Design
  slug: design
- name: technology
  slug: technology
- name: UI
  slug: ui
- name: UX
  slug: ux
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Anant Jain

  A 7-minute guide to getting these three foundational components just right.


  _Source: [Unsplash](https://unsplash.com/@naffiq?utm_source=medium&utm_medium=referral"
  rel="noopener" target="_blank" title="">Galymzhan Abdugalimov on <a hre...'
---

By Anant Jain

#### A 7-minute guide to getting these three foundational components just right.

![Image](https://cdn-media-1.freecodecamp.org/images/vIrqY20hUWlVlYv1fOfyvOY4ugEir62exVJL)
_Source: [Unsplash](https://unsplash.com/@naffiq?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Galymzhan Abdugalimov</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

If you wanted to buy a new hammer from a hardware store, imagine how you would go about doing this:

* **Option 1:** you can either look through the store — there are aisles with department names on top and, within a department, there are signs at the end of each aisle.
* **Option 2:** you can find the nearest clerk and just ask them where they keep the hammers.

It could be a mixture of the two as well — you may try to navigate a bit to see how easy it is. If you don’t find what you’re looking for, you may ask a clerk.

![Image](https://cdn-media-1.freecodecamp.org/images/sUb9RgTz1vWXzPMUgICxYdEukZGnP6d0lXoC)

If you think about it, this is exactly how we use websites as well. We go looking around for a bit (**Navigation**) and, if we cannot find what we came looking for, we hit the **Search** functionality. These are the two critical components of your site. Minor usability flaws here can cause major annoyance to your users.

This short guide, in part based on Steve Krug’s seminal book “Don’t Make Me Think,” I will teach you how to design your website’s Navigation, Search, and Homepage. Let’s start with the Navigation.

### Getting the navigation right

#### Why do we need Navigation?

Unlike our hardware store example, a website is not a physical space. It is different from a hardware store in three ways:

1. A website does not provide the user with a sense of **scale**
2. A website does not provide the user with a sense of **direction**
3. A website does not provide the user with a sense of **location**

When we want to return to something on a website, we can’t rely on a physical sense of where it is. Instead, we have to remember where it is in the **conceptual hierarchy** of the website, and then retrace our steps.

**Navigation** puts this **conceptual hierarchy** up-front and center. It should ideally be a part of every page. It tells us what’s on the website and how to use it, making it a critical part of the user experience of your site.

![Image](https://cdn-media-1.freecodecamp.org/images/cKZ17A3SyMsS0maXbcsLBN93030kLfd1xzeb)

#### How should you design the navigation?

Persistent navigation is the set of elements that appear on top of **every page.** They follow certain conventions and, unless we have a substantial reason, we should stick to them:

* **Site ID** on the top-left — this tells the user which site they are on (the Apple logo in the screenshot above).
* **Sections on top** — a way to get around various parts of the site, with the current section highlighted to indicate where you are (for example, the Mac, iPad, and iPhon sections in the screenshot above).
* **Tabs** (optional) — tabs, when done right, are self-evident, hard to miss, and slick. An active tab should be a different color and physically connect with the space below it so it “pops” to the front.
* **Utilities** like “My Account”, “Track Your Order”, and “Stores.” Don’t put more than five of these — the rest can go in the footer navigation.
* **Breadcrumbs**: this is another set of “You are here” indicators, like the highlighted section on top. Make breadcrumbs small and at the very top of a page, where they don’t interfere with the primary navigation. The best way to go about it is to use `&`gt; between levels, and boldface the last item (the item you’re currently on and — since you’re on it — it should not be a link).

![Image](https://cdn-media-1.freecodecamp.org/images/54GnJ97ntnTOaeNzAHOo4NyFT6Fhzk7ctev0)
_Breadcrumbs on Best Buy’s product page_

* **A page name:** which page are you on? Every web page should ideally have a name that matches the words clicked to get there. It needs to be prominent and in the right place. In the visual hierarchy of the page, it should appear to be framing the content that is unique to this page.
* **Local navigation** on left sidebar (optional): these are the options available at the current level.
* **Footer Navigation**: this is where all other utilities go.

![Image](https://cdn-media-1.freecodecamp.org/images/nOUQohyFKB02wR8us7BXOmMGNC5i28-a2-we)
_Footer on [NNGroup.com](https://www.nngroup.com" rel="noopener" target="_blank" title=")_

One of the most critical elements of navigation is a link to the Homepage, usually served by the Site ID (logo). It’s what the users click if they get lost — it’s the anchor that lets them return to the starting point if they want to start over.

### Making search easy

So how should we design the search functionality? Very simply, make the search box a simple box with no options, but allow limiting the scope of the search on the page of results.

Also, if scoping a search, add the word “for” so it reads like a sentence: “Search ___ for ___.” Here is a good alternative example where the placeholder text indicates that the search is scoped to just the publication:

![Image](https://cdn-media-1.freecodecamp.org/images/f2NVvqtyqvrlO8NsZx1YrPE8X81pZLPIrodW)
_When the search is scoped to just the publication, the search area indicates so._

#### How do you know if you did a good job with the navigation?

Here’s a great test to run on your friends to see if you did a good job with the navigation. Leave them on a random page somewhere deep in your website and make sure they are able to answer these questions quickly, and without hesitation:

* what site is this? (Site ID)
* what page am I on?
* what are the major sections of this site?
* what are my options at this level?
* where am I in the scheme of things?
* how can I search?

### Designing the homepage

For most websites, the homepage is the first page that the users land on. It is also the fixed north star that the users can return to if they get lost. Your Homepage has to answer these five questions that every user has in their head when they enter the site for the first time:

1. What is this?
2. What do they have here?
3. What can I do here?
4. Why should I be here — and not somewhere else?
5. Where do I start…

…if I want to search?

…if I want to browse?

…if I want to sample their best stuff?

It’s the job of the homepage to answer these questions.

There are three crucial places on the homepage where users expect to find explicit statements about the site:

1. **The tagline:** good taglines are clear and informative, and explain what your site or organization does. They are just long enough, but not too long, and convey differentiation — they don’t sound generic. It helps if they are personable, lively, and (sometimes) witty.
2. **The welcome blurb:** make sure it’s something that conveys what the site does.
3. **The “Learn More”:** innovative products tend to require a fair amount of explanation. People have become accustomed to watching short videos on their computers and mobile devices, and are often willing to watch one on the Homepage.

![Image](https://cdn-media-1.freecodecamp.org/images/B6n9gkmElDG5VDt0dk93ra6LRt5fVcQRfHoz)
_[Commonlounge](https://www.commonlounge.com" rel="noopener" target="_blank" title=") Homepage_

**NN Group** published the following [list of 10 guidelines](https://www.nngroup.com/articles/top-ten-guidelines-for-homepage-usability/) for homepage usability, which doubles up as a great checklist before you launch:

1. Include a one-sentence tagline
2. Write a page title with good visibility in search engines and bookmark lists
3. Group all corporate information in one distinct area
4. Emphasize the site’s top high-priority tasks
5. Include a search input box
6. Show examples of real site content
7. Begin link names with the most important keyword
8. Offer easy access to recent homepage features
9. Don’t over-format critical content, such as navigation areas
10. Use meaningful graphics

This is the list in action on their own site:

![Image](https://cdn-media-1.freecodecamp.org/images/un9wZKq4vaZQYMrHJv811HDvQtlEtTTrwLSW)
_[NNGroup](https://www.nngroup.com" rel="noopener" target="_blank" title=") Homepage, implementing most of their guidelines._

Remember that the homepage is a shared resource between all departments within a company — at least when it comes to what’s displayed first. Anything on top of the homepage gets promoted the most, so as a team you will have to focus and decide what needs to surface at the top.

![Image](https://cdn-media-1.freecodecamp.org/images/ldOxUIQ3-plBQqOi7VdZxLohPl-QpS-ouK10)

Thanks for reading this quick guide. This was originally published as part of the [UX Design course](https://www.commonlounge.com/discussion/d8c1c96e92024adf9f496fe41dcaad1a) on [Commonlounge](https://www.commonlounge.com/). It’s a platform that has courses with small bite-sized lessons like these on topics ranging from [Project Management](https://www.commonlounge.com/discussion/1013c511951f4c47a803c32c4e1ae0f2) to [Machine Learning](https://www.commonlounge.com/discussion/35ccdb70826e434a876d612504297232) that deliver the most value for the time you put in.

You learn by working on real-world projects and getting feedback from industry mentors. You should check it out [here](https://www.commonlounge.com/)!

![Image](https://cdn-media-1.freecodecamp.org/images/R1v85eRIzXSYTP9Jfy3tJcYe1Vxi4kuqyCys)

