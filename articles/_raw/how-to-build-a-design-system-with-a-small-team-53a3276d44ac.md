---
title: How to Build a Design System with a Small Team
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-24T15:47:09.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-design-system-with-a-small-team-53a3276d44ac
coverImage: https://cdn-media-1.freecodecamp.org/images/1*bPOUHDfQzUG7hVlz_CLLpA.jpeg
tags:
- name: Design
  slug: design
- name: Sketch
  slug: sketch
- name: Style Guide
  slug: style-guide
- name: 'tech '
  slug: tech
- name: UX
  slug: ux
seo_title: null
seo_desc: 'By Naema Baskanderi

  Last night my small team and I headed out to do a little networking and learn about
  Design Systems. Being that is was the buzzword of 2017, we were eager to learn how
  we could create our own.

  We had heard all the wonderful benefit...'
---

By Naema Baskanderi

Last night my small team and I headed out to do a little networking and learn about Design Systems. Being that is was the buzzword of 2017, we were eager to learn how we could create our own.

We had heard all the wonderful benefits of creating a design system: saving time, reducing debates, collaboration, adoption, and more. I was excited!

All the talks spoke about how to create a design system. However, these were **big** teams or they had dedicated resources, even a DesignOps team _(2nd buzzword of 2017)_ to build and maintain the design system.

At the end of the evening we left a little discouraged. But we were not alone. During the Q&A session many were asking:

_“How can I build a design system as a single designer?”_

_“I’m the only designer, what advice do you have for me?”_

But my team and I decided we weren’t going to let this stop us. We are still going to create our own design system. Before I dive into that, here’s a bit of background.

![Image](https://cdn-media-1.freecodecamp.org/images/w7MV47tWonjOTDKdvUFgLR76rTke2MdUeQEx)

#### What is a Design System?

> “A design system offers a library of visual style, components, and other concerns documented and released by an individual, team or community as code and design tools so that adopting products can be more efficient and cohesive.” — [Nathan Curtis](https://medium.com/eightshapes-llc/defining-design-systems-6dd4b03e0ff6)

Simply put, a design system is a collection of reusable components to tie whole products together.

Many people have written in-depth articles and books on design systems. Here are a few you may find useful:

[**A comprehensive guide to design systems - InVision Blog**](https://www.invisionapp.com/blog/guide-to-design-systems/)  
[_Companies like Airbnb, Uber, and IBM have changed the ways they design digital products by incorporating their own…_www.invisionapp.com](https://www.invisionapp.com/blog/guide-to-design-systems/)[**Design Systems, Style Guides, and Pattern Libraries: Oh My! - UXcellence**](https://uxcellence.com/2017/design-systems-style-guides-pattern-libraries)  
[_Many designers use the terms design system, pattern library, and style guide interchangeably. But they don't mean the…_uxcellence.com](https://uxcellence.com/2017/design-systems-style-guides-pattern-libraries)[**Design Systems Handbook**](https://www.designbetter.co/design-systems-handbook)  
[_A design system unites product teams around a common visual language. In this book, learn how you can create a design…_www.designbetter.co](https://www.designbetter.co/design-systems-handbook)[**Creating a Design System: The 100-Point Process Checklist**](https://www.uxpin.com/studio/ebooks/create-design-system-guide-checklist/)  
[_Know how to build a design system step-by-step. Based on real projects. Create a UI inventory, get buy-in, create color…_www.uxpin.com](https://www.uxpin.com/studio/ebooks/create-design-system-guide-checklist/)

#### Style Guide vs. Design System

You may be thinking, great but **_isn’t that just a style guide?_**

> “A style guide is an artifact of the design process. A design system is a living, funded product with a roadmap & backlog, serving an ecosystem.” — [Nathan Curtis](https://twitter.com/nathanacurtis/status/656829204235972608?lang=en)

Additionally, a design system is a bunch of different sized components (or molecules) that can be put together in endless ways to create a series of larger components. Brad Frost’s [Atomic Design](http://atomicdesign.bradfrost.com/) is the inspiration for component design.

#### Benefits of a Design System

> “The challenge we face today is that tools don’t communicate to each other very well, details fall through the cracks, there is a huge gap between design and engineering and we need to do a lot of manual work to make sure we are always on top of everything.” — [UX Bootcamp](https://blog.prototypr.io/pattern-library-style-guides-design-systems-do-you-need-one-b7857af0f255)

As a small team working on B2B enterprise software, we were diving into creating a design system with limited time, budget and resources. I wanted to remind our team of the benefits.

Overall our team would be saving time because of:

* Reduced debate — No need to waste time revisiting design decisions for the same component
* Reusable components making scale possible
* Increased collaboration — improve working remotely and in different offices

I had a selfish reason for wanting to build a design system. I quickly realized, if successful, we could ‘automate’ many tasks allowing us to have time to do something I love, **solving user problems**! That is the core of UX.

#### Design System Structure

In order to create a design system, we need to break it down and understand its parts:

![Image](https://cdn-media-1.freecodecamp.org/images/FISXXSaT45PI0BAQjM37CySskxm5WT-7aZXt)
_[UX Pin — Design System](https://www.slideshare.net/uxpin/building-a-design-system-a-practitioners-case-study" rel="noopener" target="_blank" title=")_

A bit of soul searching is involved as well. Some questions to ask when creating a design system:

* How does the system work today and in the future?
* What is our vision?
* What problems are we trying to solve?
* Who does this problem most impact?
* What impact do we want a design system to have on how we work?

How others are attempting to approach this:

[**How we’re using Component Based Design**](https://medium.com/@lewisplushumphreys/how-were-using-component-based-design-5f9e3176babb)  
[_Component Based Design is often talked about in context of large, complex projects. In this post we’re making the case…_medium.com](https://medium.com/@lewisplushumphreys/how-were-using-component-based-design-5f9e3176babb)[**Setup a design system**](https://blog.prototypr.io/design-system-ac88c6740f53)  
[_Build a system that provides a unified set of UX, design rules and patterns._blog.prototypr.io](https://blog.prototypr.io/design-system-ac88c6740f53)

![Image](https://cdn-media-1.freecodecamp.org/images/ss415zgUFpiKE8X4Vw7gtdx04Il-BimlF0sr)

### How can our small team make a design system?

Where do you start when you don’t have enough resources, time or budget?

#### 1. Don’t start from scratch

> _“If you wish to make apple pie from scratch, you must first invent the universe.”_ — Carl Sagan

Our team is reviewing existing design systems out in the wild so we can — as Austin Kleon says:

![Image](https://cdn-media-1.freecodecamp.org/images/sYXNsuwQhjfgXgcC7KsiSB1iwFkhrKVnRTNM)
_[Steal like and Artist — Austin Kleon](https://www.amazon.com/Steal-Like-Artist-Things-Creative/dp/0761169253" rel="noopener" target="_blank" title=")_

Many companies have made their design systems public and have even shared sketch files. I have shared a list below. This fact, and the many other sketch resources, makes it a no-brainer to use Sketch as our tool of choice.

Additionally, there are tools out there which can help you quickly create a baseline for your design system:

[**Frames for Sketch - Web Design System**](http://framesforsketch.com/)  
[_Carefully crafted components and best sketch techniques combined into a powerful web design system._framesforsketch.com](http://framesforsketch.com/)[**Symbols & Styleguides**](http://symbols.janlosert.com/)  
[_The smartest template and your future starting point for every User Interfaces in Sketch. Stop wasting your time by…_symbols.janlosert.com](http://symbols.janlosert.com/)[**Sketch App Sources - Free design resources and plugins - Icons, UI Kits, Wireframes, iOS, Android…**](https://www.sketchappsources.com/search_bootstrap.html)  
[_Sketch App Sources is the largest collection of icons, UI kits, wireframes, and free design resources for Sketch._www.sketchappsources.com](https://www.sketchappsources.com/search_bootstrap.html)

#### 2. Know what you’re working with

We have decided that it is a must to complete a UI Audit of all our sites and properties. We may have to call in a few favors to get this done. But since it is just documenting what exists, enlisting help from others may not be that difficult. This will be time consuming, but in the end it will be worth it. We will be able to design holistically when creating new components.

This may be useful for learning how to conduct a UI audit:

[**The step-by-step guide to an effective UX audit — InVision Blog**](https://www.invisionapp.com/blog/guide-to-effective-ux-audit/)  
[_This step-by-step guide will teach you how to audit your user experience. But before we dive in, let’s first…_www.invisionapp.com](https://www.invisionapp.com/blog/guide-to-effective-ux-audit/)

#### 3. Build as you go

A design system is a living document. Realizing that the work is never done, we’ve decided to jump in and build as we go. As we iteratively work on our projects, we will design with components in mind and will eventually have a design system. Fortunately, there are a few of us, which allows us to be collaborative and “steal” from each other.

**Quick tip**: Build symbols in Sketch. I know, it seems time-consuming, but once you see the power of symbols you will appreciate the old saying:

> **“You have to go slow in order to go fast.”**

#### 4. Know your limits

Start small.

Some design systems include code snippets. That is the ultimate goal, because it will increase adoption across the company and create a consistent user experience. However, my small team can’t do that. Not yet, that is.

We are planning to start with a sketch file of simple components. Once we are far enough, we will work with our frontend devs to create CSS. Allowing developers to use their ‘weapon of choice’ when it comes to code may allow the design system to live. And with code bases changing on what seems to be a daily basis, keeping our hands out of it may be best.

#### 5. Stay organized

Sounds simple, but with projects piling up and looming deadlines, it feels easier to do things the ‘quick and dirty’ way. Staying organized does take time and is never done, but it keeps everyone sane and reduces the email or slack clutter of files flying back and forth. As we start working on new things using a UI kit that we are going to build with one of the tools listed above, we need to keep track. Otherwise, we will end up where we started — different styles everywhere!

Design document versioning is a dream for all designers. No one product has gotten it 100% right. We are going to give Abstract and Plant a try to see how it can help keep us on track. Working for an enterprise, the only online platform we can use for file storage is One Drive. Google drive and Dropbox are other options if you aren’t restricted.

[**Abstract**](https://sketchapphub.com/resource/abstract/)  
[_Version control and file management for your Sketch files. Abstract enables designers to reliably version and manage…_sketchapphub.com](https://sketchapphub.com/resource/abstract/)[**Plant - version control app and Sketch plugin for designers**](https://plantapp.io/)  
[_Plant is a version control app and Sketch plugin for designers. Sync design versions, invite teammates and take full…_plantapp.io](https://plantapp.io/)

These are the first steps my team and I are going to try when starting this journey. Fingers crossed we make some headway. I would love to hear from other small teams, even a ‘team of one,’ to learn how they are tackling this challenge.

### Design System Directory

As promised, here are some design systems for inspiration or for “stealing like an artist:”

[**miukimiu/design-systems**](https://github.com/miukimiu/design-systems)  
[_design-systems - A curated list of design systems. Learning materials and tools for creating your own design system._github.com](https://github.com/miukimiu/design-systems)[**Atlassian Design Guidelines | Atlassian Design**](https://atlassian.design/)  
[_Design, develop, and deliver. Use Atlassian's end-to-end design language to create straightforward and beautiful…_atlassian.design](https://atlassian.design/)[**Building a Visual Language**](https://airbnb.design/building-a-visual-language/)  
[_Behind the scenes of our new design system. This article is part of a series on our new Design Language System. Karri…_airbnb.design](https://airbnb.design/building-a-visual-language/)[**BBC GEL | Homepage**](http://www.bbc.co.uk/gel/)  
[_Our Global Experience Language (GEL) is the BBC's shared design framework which enables us to create consistent and…_www.bbc.co.uk](http://www.bbc.co.uk/gel/)[**Carbon Design System**](http://carbondesignsystem.com/)  
[_Carbon is the design system for IBM Cloud products. It is a series of individual styles, components, and guidelines…_carbondesignsystem.com](http://carbondesignsystem.com/)[**Home - Office UI Fabric**](https://developer.microsoft.com/en-us/fabric#/)  
[_The official front-end framework for building experiences that fit seamlessly into Office and Office 365._developer.microsoft.com](https://developer.microsoft.com/en-us/fabric#/)[**Fluent Design System**](https://fluent.microsoft.com/)  
[_An eloquent design system for a complex world. Now's the time for bold, scalable, universal design. This is a…_fluent.microsoft.com](https://fluent.microsoft.com/)[**Harmony Design System**](http://harmony.intuit.com/)  
[_Harmony is a living design system that unites Intuit's small business products, brand and marketing experiences across…_harmony.intuit.com](http://harmony.intuit.com/)[**IBM Design Language**](https://www.ibm.com/design/language/)  
[_Use the IBM Design Language to create beautifully crafted products and enlightening user experiences._www.ibm.com](https://www.ibm.com/design/language/)[**Lightning Design System**](https://www.lightningdesignsystem.com/)  
[_The Lightning Design System provides accessible markup which will serve as a foundation for your application…_www.lightningdesignsystem.com](https://www.lightningdesignsystem.com/)[**Lonely Planet Travel Guides and Travel Information**](http://rizzo.lonelyplanet.com/styleguide/design-elements/colours)  
[_Style Guide Documentation Performance Monitoring About Rizzo_rizzo.lonelyplanet.com](http://rizzo.lonelyplanet.com/styleguide/design-elements/colours)[**Material Design**](https://material.io/)  
[_Material Design is a unified system that combines theory, resources, and tools for crafting digital experiences._material.io](https://material.io/)[**Nachos | Trello**](https://design.trello.com/)  
[_Trello - Pattern Library_design.trello.com](https://design.trello.com/)[**Pega UX Design System**](https://design.pega.com/)  
[_Pega is a powerful UX system for engaging customers and employees. Pega software solves complex business problems…_design.pega.com](https://design.pega.com/)[**Predix Design System**](https://www.predix-ui.com)  
[_Edit description_www.predix-ui.com](https://www.predix-ui.com)[**U.S. Web Design Standards: A design system for the federal government**](https://standards.usa.gov/)  
[_The Standards provide research-backed design patterns for building accessible, responsive, and consistent digital…_standards.usa.gov](https://standards.usa.gov/)[**SAP Fiori Design Guidelines**](https://experience.sap.com/fiori-design-web/)  
[_The original SAP Fiori user interface for web apps based on the SAPUI5 framework. Learn how to design engaging and…_experience.sap.com](https://experience.sap.com/fiori-design-web/)[**Shopify Polaris**](https://polaris.shopify.com/)  
[_Our style guide is the blueprint for our design system. It helps us collaborate across disciplines to build a great…_polaris.shopify.com](https://polaris.shopify.com/)[**Pattern Lab | Build Atomic Design Systems**](http://patternlab.io/)  
[_Unlike static design tools, Pattern Lab lets you easily swap in different representative content into your components…_patternlab.io](http://patternlab.io/)

#### Pattern Libraries / Style Guides

[**WTF is Solid? - Solid**](https://solid.buzzfeed.com/)  
[_Solid is BuzzFeed's CSS style guide. Influenced by frameworks like Basscss, Solid uses immutable, atomic CSS classes to…_solid.buzzfeed.com](https://solid.buzzfeed.com/)[**Style Guide**](https://buffer.com/style-guide)  
[_Buffer makes it super easy to share any page you're reading. Keep your Buffer topped up and we automagically share them…_buffer.com](https://buffer.com/style-guide)[**Duolingo: Design Guidelines**](https://www.duolingo.com/design/)  
[_When written, Duolingo is always a single word with an uppercase 'D'. The 'L' is never capitalized, and the name is…_www.duolingo.com](https://www.duolingo.com/design/)[**Pattern library - FutureLearn**](https://www.futurelearn.com/pattern-library)  
[_Enjoy free online courses from leading UK and international universities._www.futurelearn.com](https://www.futurelearn.com/pattern-library)[**Design Guidelines - The way products are built.**](http://designguidelines.co/)  
[_Web Developer from Somewhere_designguidelines.co](http://designguidelines.co/)[**Website Style Guide Resources**](http://styleguides.io/)  
[_A collaborative collection of resources for creating Front-End Style Guides and Pattern Libraries_styleguides.io](http://styleguides.io/)[**Grid System | MailChimp**](https://ux.mailchimp.com/patterns)  
[_Our grid system is composed of 8 flexible columns with a gutter between columns of 30px. We apply border-box so that…_ux.mailchimp.com](https://ux.mailchimp.com/patterns)[**Styleguide**](https://www.yelp.com/styleguide)  
[_Edit description_www.yelp.com](https://www.yelp.com/styleguide)

If you found this useful, you know what to do now. [Follow](https://medium.com/@msNaema) me to get more articles and tutorials on your feed.

