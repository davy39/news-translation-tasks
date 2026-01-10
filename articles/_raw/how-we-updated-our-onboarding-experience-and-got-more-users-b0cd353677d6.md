---
title: How we updated our onboarding experience and got more users
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-20T19:05:18.000Z'
originalURL: https://freecodecamp.org/news/how-we-updated-our-onboarding-experience-and-got-more-users-b0cd353677d6
coverImage: https://cdn-media-1.freecodecamp.org/images/0*Kp5Z_lcq-cbmwAnI.png
tags:
- name: Design
  slug: design
- name: onboarding
  slug: onboarding
- name: 'tech '
  slug: tech
- name: UI
  slug: ui
- name: UX
  slug: ux
seo_title: null
seo_desc: 'By William Woodhead

  Methods we used to increase conversion by 60%


  Pilcro Artboard — User Onboarding

  As a product designer and developer, I have spent a lot of time thinking about the
  elements of a successful User Onboarding experience. It’s a diffic...'
---

By William Woodhead

#### Methods we used to increase conversion by 60%

![Image](https://cdn-media-1.freecodecamp.org/images/RngZsRjwpWrpromZzWL0nr472IPxxVrpidIC)
_Pilcro Artboard — User Onboarding_

As a product designer and developer, I have spent a lot of time thinking about the elements of a successful User Onboarding experience. It’s a difficult process that is crucial for good conversion, and it is often overlooked.

In this piece, I’m going to describe the process we went through, (while working on our [brand management software](https://www.pilcro.com)), so that you can apply the lessons we learnt for your own User Onboarding flow.

Why listen to me? Well we recently grew our overall sign-in conversion by 60% after launching our User Onboarding flow as part of our [product launch](https://www.pilcro.com/blog/pilcro-is-on-product-hunt) on Product Hunt. Here’s what [Jonathan Price](https://www.linkedin.com/in/jvprice) had to say about it on the day of the launch:

> _“The Product Hunt themed landing page was really outstanding — possibly the most polished Product Hunt launch I’ve seen. Great work.”_

### So what is User Onboarding?

Here’s a definition from [trychameleon](https://www.trychameleon.com/blog/what-is-user-onboarding):

> _“User onboarding is the system of actively guiding users to find new value in your product.”_

So it’s all about communicating valuable features to your users.

But who are these users? Are they first-time users? Are they new(ish) users who are returning to your product?

And what does “value” mean? Features that users might value? User behaviours that you might value? eg. sign-ins or subscriptions?

Immediately it’s clear that User Onboarding is not a straightforward UX task.

We have multiple users-types, and multiple features that we think the users would find valuable. How do we make sense of it all? How do we communicate the value of the product in an effective way? And then what are we actually trying to achieve by showing off features to users?

### First step — Audit your user journeys

It might seem obvious, but the first step is working out how new and existing users move through your app. Is there one journey that everyone takes, or are there multiple different paths?

We did this step with the help of the [General Assembly](https://generalassemb.ly/?ref=pilcro) UX students who employed user-testing to understand how new users experienced our app for the first time. This process also helped us categorize our users into three different user-types:

* First 20 seconds
* First session
* First month

At the end of this process we had a much better understanding about how users moved through our app. But we still didn’t know what value we wanted to communicate to them or what the end goal was.

### Introducing the Magic Moment

In the depths of our confusion about User Onboarding, we came across [this video](https://youtu.be/n_yHZ_vKjno). It talks about how Facebook designed their user journeys to get users to a “Magic Moment”.

The Magic Moment is when a user suddenly understands what the core value of your product really is. It’s the moment when a user “gets it”. For Facebook it was when you saw a photo of one of your friends.

For us at Pilcro, we realized our Magic Moment is when a user copies a brand asset for the first time. This is when they truly understand why they should use Pilcro.

With the Magic Moment in mind, we devised this table to help order our thoughts.

![Image](https://cdn-media-1.freecodecamp.org/images/KrklNMfoiB4RKCtZC0F4tCUwlAN3ikg04LL8)

Then we tried to map these same aims to possible strategies of achieving them.

![Image](https://cdn-media-1.freecodecamp.org/images/N7E0JpUjOAxo1rx5T1PQ7oN7gVvq8Z-6ax0U)

At this point we had some strategies to achieve the aims. It was time to look into what visual Onboarding components were available to us — what tools and tricks could we pull out of the User Onboarding locker to make it all come to life.

### User Onboarding Options

After all the analysis, User Onboarding still comes down to writing some UI components that communicate value to the users. So what are these UI components? What options are available to app developers and UX designers?

There are of course infinite options for User Onboarding components, but here is a concise list of our favourites with User Onboarding example images from other apps.

#### Modals

Take over the whole screen, forcing a user to stop in their tracks to show them something useful.

![Image](https://cdn-media-1.freecodecamp.org/images/dtKqT-MpF0wNnfH7ZrXGRuopT-NS8bg97UTm)
_The Google Photos Welcome Modal_

#### Contextual popups

Information when and where the user needs it. Tooltips are the most common example of this:

![Image](https://cdn-media-1.freecodecamp.org/images/2KcBvN8IseHl96Y1gLUbwa3TRhSsVgZ80lWD)
_Asana Tooltip_

#### Empty Space

Use empty lists and grids in the app’s UI to show helpful tips and call-to-actions.

![Image](https://cdn-media-1.freecodecamp.org/images/pRb5g2c-cLSD7sCeRLbik4KJl9BaBruLFMNV)
_Bear app — smart empty space_

#### Progress Indicator

Show an indicator of how well the user is doing. This can last for the entire lifespan of the user on your product and can be gamified.

![Image](https://cdn-media-1.freecodecamp.org/images/yjmoV2tY0eAJ83lluysEoJkz9NGSbrbRIO2P)
_Sentry setup progress indicator_

With these options in mind, we plotted this table to work out which User Onboarding options suited which user-types best and why. The green squares are the best fits while the red squares are a bad fit.

![Image](https://cdn-media-1.freecodecamp.org/images/e6OqaHHtsOX8W0RjqxDY8xLo8TvHoKT1oiWP)

At this point, we had all the pieces of the puzzle ready.

1. We had identified the different user-types.
2. We had identified the strategies to use for our user-types.
3. We had identified UI components to realise these strategies.

Time to put it all together.

### So what did we actually do?

#### User benefits modal

* Only on first visit
* Communicate some core user benefits of the app.
* **Purpose** — get users to hang around.

![Image](https://cdn-media-1.freecodecamp.org/images/98SKqUvFhyQTvi9qdra5aJRJGBLPuTiLhYfm)
_User benefits slideshow_

#### Contextual popups

* Get users familiar with the interface very quickly
* Show them the most important features and buttons.
* Product Hunt themed to give visitors from Product Hunt some visual consistency.
* **Purpose** — get users to the Magic Moment

![Image](https://cdn-media-1.freecodecamp.org/images/Jk9DUH218hBG6YU6A-FKEP36BUZEWtHZjZmP)
_Contextual popups — the swoosh_

#### Smart use of Empty Space

* Show call-to-actions where there is no content
* **Purpose** — never leave a user outside of a flow

![Image](https://cdn-media-1.freecodecamp.org/images/vRQSiXUVaaXOZAGN6swVvqqqOazIGPd4dw53)
_Pilcro’s empty space call to actions_

#### Progress indicator

* Show users a percentage bar of how much of a ‘power-user’ they are.
* **Purpose** — push users to behave how we want them to.

![Image](https://cdn-media-1.freecodecamp.org/images/1DY8iN-0EfG-jBm2t0AUwl2zEN4Wl1mjAMmT)
_Progress indicator in %_

### And the numbers don’t lie

How did we know that the User Onboarding design worked? Here are the stats.

We more than doubled our conversions to the product from the website in the week after deploying the new user onboarding.

![Image](https://cdn-media-1.freecodecamp.org/images/3zrVR3uzFrpt2DdBtit4xpsSiWCQJ7IjJzLz)
_Conversions to the product_

We grew our overall sign in conversion by 60%.

![Image](https://cdn-media-1.freecodecamp.org/images/Z6cMZDXS25TpmnU4LQgYGijKT2C4D8KbL3DY)

Admittedly, the launch helped with these stats as there was more buzz around our product. But the new User Onboarding undoubtedly played a crucial role in the success of the launch.

### Afterthought — Why is User Onboarding so difficult?

* Product owners are too close to the product. How can a product owner possibly know how it feels to experience their product for the first time?
* Different users find value in different parts of the product. So guiding them to find value is not a linear journey that all users share. Different users might have different Magic Moments.
* Different users behave differently and move through your product differently. Some users like having their hand held when Onboarding into a new product, some users just like to dive straight in and play around. How do you craft a UX experience that serves the Onboarding needs of all different users?
* Different users have different knowledge of your product. So how do you know how much information to give someone?
* The tech behind crafting a good User Onboarding experience is often very complex as it requires adding a whole new visual layer to your application.

User Onboarding is a complex challenge because you have to deal with a matrix of different users, features, aims and behaviours. However, if you approach it in the right way, you can make you app really shine for your new users. Good luck!

### Experience it for yourself

Check out our user onboarding for yourself at [this link](https://artboard.pilcro.com/). Let us know what you think!

_Pilcro offers free brand management software for G-Suite._

