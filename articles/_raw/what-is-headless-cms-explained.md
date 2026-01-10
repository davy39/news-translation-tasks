---
title: Headless CMS Explained – What it is and When You Should Use it
subtitle: ''
author: Daniel Madalitso Phiri
co_authors: []
series: null
date: '2021-07-27T17:53:47.000Z'
originalURL: https://freecodecamp.org/news/what-is-headless-cms-explained
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/siora-photography-hgFY1mZY-Y0-unsplash-1.jpg
tags:
- name: cms
  slug: cms
- name: headless cms
  slug: headless-cms
seo_title: null
seo_desc: 'By Daniel Madalitso Phiri

  CMSs are pretty hard to ignore because they''re everywhere on the internet. WordPress,
  for example, powers nearly 40% of the internet today.

  In this article, we''ll cover what CMSs are and why you should care about them.
  I''ll ...'
---

By Daniel Madalitso Phiri

CMSs are pretty hard to ignore because they're everywhere on the internet. WordPress, for example, powers nearly [40% of the internet](https://kinsta.com/wordpress-market-share/) today.

In this article, we'll cover what CMSs are and why you should care about them. I'll also introduce you to a new type of CMS that seems to be everywhere at the moment – the Headless CMS. And we'll do all this with a story!

Life has a funny way of making you try things. And after years of ignoring CMSs as a technology, in mid 2020 I got a job at [Strapi](https://strapi.io), a headless CMS tool. Since then, I have developed a pretty good understanding of what these things do – so let's get into it.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/ezgif.com-gif-maker-2-.png align="left")

## What is a CMS?

A Content Management System (CMS) is a tool that helps users create, manage, and modify digital content.

In this article, however, I won’t get into the nitty-gritty of it. Instead, if you want to learn more you can have a look at [an article I wrote](https://strapi.io/blog/frontend-developers-headless-cms) that goes deeper into various types of CMSs.

## What is a Headless CMS?

A headless CMS has a back end where content is prepared – and that's it. The content and its data are only accessible via calls made to the API, whether it's REST or GraphQL.

I like to use this diagram to illustrate how Headless works, so hopefully it paints a clearer picture.

![Image](https://lh3.googleusercontent.com/zPdxhP33Y_kqX1SY-KXDq0Ma1IiJv15urJ_PVuiogvtI86tCa_A2qMJ0L2UqFD_U_MmTy0VHED1Oz9w5uumNipKSBzwmHYkHRrgXrdrLU0PNg9nvhUQC28Hy09H9Wrn5iiBep95U align="left")

*Monolithic vs decoupled vs headless architectures*

Besides serving content to multiple platforms, there are a couple other reasons why you would want to use a Headless CMS.

### You don’t want to give up developer flexibility

Adopting a Headless architecture by default means that you have the flexibility of selecting a front end tool of your choosing. And for many developers, this is a critical advantage.

### You need a secure content solution

Decoupling the front end from the back end makes targeted attacks much harder. This is something some traditional CMSs still struggle with today.

### You want to future proof your tech stack

Going headless also means that you’re less dependent on a single solution for a front end. Should you need to upgrade to a more modern front end or add a new front end altogether, headless makes this much easier.

### You need to create custom and personalized experiences

This is becoming a really important benefit for headless CMSs for many organizations.

With headless you have the opportunity to tailor different experiences for different platforms all from a single content source.

## How I got into Headless CMSs

So I really like GraphQL, and that’s how I got started with Strapi. Working for a CMS was like diving head first into this ecosystem. I thought I understood Headless CMSs because to me they were “data, API, frontend” and that’s how I thought about it.

Well, we use these things to build our front ends, but we often overlook the content management side of things when we think about building a front end like that. And it wasn't until I started working with Strapi that I recognized my assumption.

“Content Management” sounds kinda boring, right? And CMS? “Ewww why would I want to use such a tool?” I know! Me too, but hear me out. CMSs actually pretty useful. So let’s talk about how and why a CMS might help you out.

## Why Do You Need a Headless CMS?

For starters, there’s no downplaying the role of content in today's world. Content is everywhere and manifests itself in so many forms through text, audio, video, and more.

For a long time, computers and browsers were the main tool for content consumption. We read blogs, watched YouTube videos, and listened to podcasts on our personal computers.

Gradually our computers got smaller and less obvious. Content in its many shapes and forms started to appear all around us. It showed itself in mobile phones, on our smart televisions, in our cars, in our virtual assistants and wearable devices.

The way people consumed content changed, and so did the way we had to build content-consuming experiences.

### So How Does Headless CMS Help?

Traditionally, CMSs were monoliths with the front end and back end tightly coupled. The content you added in the CMS back end only showed up on the front end it was coupled to - think WordPress and Drupal.

This proved inefficient as developers needed a better way to build and adapt to this new consumer behavior.

The solution? Rip the head off a traditional CMS and make it possible for your back end to deliver content to multiple platforms. This was how Headless was born.

## Why You Might Not Need a Headless CMS

Headless isn't necessarily the right solution for all use cases, though. It might not be for you if...

### You have a small team

Adopting and building a headless architecture takes quite a bit of effort. To reap all its benefits you would have to have a dedicated developer team to build your front end as well as people on your team to work on adding content to your CMS.

### You rely heavily on a simple live preview implementation

Live previews on Headless CMSs aren’t the most intuitive to set up (as of writing this) and take some effort from developers to implement.

### You only require simple publishing capabilities

As we just learned, headless takes a reasonable amount of effort to get it working efficiently and effectively.

If you need only simple publishing capabilities without features like internationalization or role-based access control, then it’s best to wait till you need those additional features to use a Headless CMS.

## Use Cases for a Headless CMS

A lot of my early CMS projects centered around corporate sites and personal blogs, which are both solid use cases for headless. But I don’t build sites full time so I don’t ship code often.

Personally I’ve used a CMS to help build a [Restaurant Catalog](https://foodadvisor.strapi.io/), an [Event Website](https://conf.strapi.io/speakers), and an [Online Quiz](https://conf.strapi.io/quizz).

There’s folks using headless CMSs to build eCommerce sites, Covid tracking projects, hospital management systems, inventory management applications, mobile catalogs, VR games, and some people even run email campaigns with them. So many possibilities.

## Conclusion

Seeing what people are building with CMSs is very inspiring. And I’ve gained a huge appreciation for CMSs as a technology. What I once thought was a boring tool actually powers so much of the world around me.

There are lots of use cases for Headless CMS these days. And while at the moment there is a huge focus on serving developers (which many CMSs are doing well), we still have a ways to go to make the content editor's experience better.

It’s exciting having a foot in the race, and all I can tell you is that it's going to be an amazing next few years for Headless technology in general.

So hopefully this article helps you jump on the bandwagon and get a better understanding of what the technology can and cannot do.

After all, at the end of the day, the choice is yours!

![Image](https://www.freecodecamp.org/news/content/images/2021/06/javier-allegue-barros-C7B-ExXpOIE-unsplash.jpg align="left")

### Resources

* [Headless CMS](https://jamstack.org/headless-cms/) | Jamstack.org
    
* [What is a Headless CMS](https://strapi.io/what-is-headless-cms)
    
* [What’s a Headless CMS and Why Should You Care](https://www.stackbit.com/blog/what-is-a-headless-cms/)
    
* [CMS Comparison](https://cms-comparison.io/#/card)
