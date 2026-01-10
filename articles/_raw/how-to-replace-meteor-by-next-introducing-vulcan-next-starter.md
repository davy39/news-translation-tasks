---
title: How to Replace Meteor with Next — Introducing Vulcan Next Starter
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-01T06:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-replace-meteor-by-next-introducing-vulcan-next-starter
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/vulcan-next-starter-white-bg_1200.png
tags:
- name: GraphQL
  slug: graphql
- name: Meteor
  slug: meteor
- name: Next.js
  slug: nextjs
- name: node
  slug: node
- name: React
  slug: reactjs
seo_title: null
seo_desc: 'By Eric Burel

  2020, still looking for a productive JS framework

  When you create a product for your own company, you are free to spend time setting
  up a development environment that fits your own quirks. Granted, you''ll likely
  spend a reasonable amoun...'
---

By Eric Burel

## 2020, still looking for a productive JS framework

When you create a product for your own company, you are free to spend time setting up a development environment that fits your own quirks. Granted, you'll likely spend a reasonable amount of time.

But when developing for others, you don’t have this freedom. You have to deliver high quality code in a predictable amount of time.

To be competitive, you have to scale across clients. Each app can’t be your first app. Knowledge, and generic code, must be reused. Most of the time that means relying on frameworks.

As an agency owner, I’ve always loved Meteor. It’s one of the rare JavaScript frameworks that's truly productivity-focused: a package-first architecture, an isomorphic approach, a persistence solution out-of-the-box…

I am also a core contributor of [Sacha Greif’s Vulcan.js framework](http://vulcanjs.org/). Vulcan is an opinionated full-stack framework, implemented as a super-set of Meteor. It goes one step further by providing declarative patterns for very fast development and relying on Apollo GraphQL.

Everything (GraphQL schema, API, database structure, forms, data tables, and so on) is automatically generated based on a JavaScript schema. Cool, isn’t it?

![Image](https://www.freecodecamp.org/news/content/images/2020/06/how-vulcan-works.svg)

But Meteor's limitations are a glass ceiling. I’ve had successful projects with Meteor and Vulcan, but I could never push those frameworks to bigger clients. Too many scalability issues, lack of traction, poor test tooling, you name it.

Back to square one, I needed to find a framework I could get married with.

## Next vs Meteor?

### That’s comparing apples and oranges!

[When I first discovered Next back in 2017](https://medium.com/@eric.burel/next-the-next-big-thing-c7f9c34f9cce), it was a promising front-end-only framework. Front-end-only. I used it to build my company website and then forgot about it.

And then, people around me started to act weird. They suddenly talked about two frameworks with nothing in common, Meteor and Next, as if they were swappable. You traded Meteor for Next? Why not replace Express by Create React App while you’re at it?

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-240.png)
_You can even use create-react-app to fight hackers. Screenshot from the French TV show "Bureau des légendes" (Canal +)._

As far as I remember, [Reaction Commerce has been one of the first non trivial frameworks to do the switch.](https://blog.reactioncommerce.com/reaction-v2-0-0-release-preview/)

I wasn’t convinced. And indeed, they still had to implement a GraphQL API on top of their Meteor app to communicate with their Next front end. Trading one framework for 2 is not the best bargain, so we kept Vulcan a Meteor-based framework.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/next-static.png)

If you think that comparing Meteor to Next is comparing apples and oranges, you are not that wrong. To this day, Next's catchphrase is still “The React framework”. Not “The Node framework”.

And yet, I started to change my mind a few months ago.

### From front end to full stack with API routes

API routes were officially introduced in July 2019 with the [v9 release](https://nextjs.org/blog/next-9).

That’s what got me on the Next bandwagon again. API routes mean that Next.js is now a minimalistic, but perfectly viable full-stack framework.

Vulcan is built around GraphQL. And GraphQL is a great fit for API routes. The API is served through a unique, dynamic /graphQL endpoint. In Next, this translates by creating a graphql.js API route. Easy peasy.

## Nowadays, Next covers the full spectrum from static to full stack

Next is more and more referred to as a “hybrid framework”. That makes sense, as its versatility is extreme.

* You can develop a full-stack application with a serverless-style back end.
* You can develop a SaaS application with dynamic server-side rendering.
* You don’t want to maintain a server? You can follow the JAMstack philosophy, and export a static app with build-time server-side rendering.
* If you are allergic to client-side JS, you can go as far as removing JavaScript from the bundle and keep only HTML code.

But don’t think Next is a jack of all trades. It’s a serious contender with Gatsby in its static form. It’s a promising alternative to Meteor in its full-stack form. Vercel (ex Zeit) has been doing a tremendous job at keeping it both high quality and very lightweight, whatever the use case.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/next-production.png)

## Don’t drop Meteor yet

I want to make something clear. Replacing Meteor by Next as our core framework in Vulcan does not mean we think Meteor should be dropped altogether.

There is one big thing we learned from our experiments with Apollo and Meteor in Vulcan: if you plan to use Meteor, just embrace the way it works. Forget about GraphQL. Forget about Webpack. Though created by the same people, Apollo and Meteor conflict a lot. It feels weird for GraphQL developers, it feels weird for Meteor purists.

Use DDP, methods, pub/sub, learn how to scale your app, join the forum, buy coffee mugs with Meteor’s logo on them. [Now that Tiny has revived Meteor](https://techcrunch.com/2019/10/02/tiny-acquires-meteor), it’s a safe bet for the years to come.

With Vulcan + Next, we simply strive to provide a GraphQL alternative to Meteor. It’s not worst or better, it’s the same philosophy with a different implementation. 

A framework is like a music instrument. Don’t pick the trendiest, pick the one that fits you. If your instrument is Meteor, go for it.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/vulcan-next-starter--banner-2_1200-1.png)

## Introducing Vulcan Next Starter, a state-of-the-art Next application

Using Next out of the box is perfectly fine. You get a build system, a styling solution, a rational folder structure.

But if you want to build an app for the next billion dollar startup, you’ll probably need a few more tools. Remember, we are seeking for a productivity-first alternative to Meteor.

A cool setup could be this one:

* Cypress and Jest for unit and e2e testing
* Storybook for visual testing and design documentation
* Internationalization, alias i18n (especially if you are from France like me :))
* TypeScript, to express your domain model through static types
* Material UI to get a solid set of customizable core components
* Apollo Client to communicate with GraphQL APIs
* Optionally, Apollo Server to setup a GraphQL entry point, with Playground and Voyager for API exploration

Next provides [a handful examples in its core repo](https://github.com/zeit/next.js/tree/canary/examples). But that’s not enough in a real life context. These tools can interact altogether in unexpected way.

Typing client-side only components like Leaflet or Plotly may prove difficult. Same goes for unifying the build system of Next, Jest and Storybook, or avoiding bad interactions between Apollo and Material UI during server-side rendering. Redirection with SSR means handling server and client scenarios jointly. I18n is especially hard to set up on its own. And the list goes on.

Trust me, you don’t want to tackle such issues alone. And guess what? We’ve gone through the hassle for you!

**All those tools are installed in our new, shiny,** [**Vulcan Next Starter**](https://github.com/VulcanJS/vulcan-next-starter)**.**

We still have a long road ahead, but we are proud to say that it’s safe to use in production.

## Next steps

Our boilerplate fulfills only half our promise. You get a cool front-end setup, but still miss a database and guidelines to implement the back end. That’s not really comparable to Meteor at this point. A handful of lambdas is not a framework. Neither is subscribing to cloud-hosted solutions.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/vulcan-logo.png)

That’s where Vulcan comes in. Through the years, we have crafted a powerful GraphQL API generator, with Mongo as the database and tons of front-end utilities. Naturally, the next step for us is to combine both Vulcan and Next to create a true full-stack framework.

You can follow our progress by joining us on [Vulcan’s Slack](http://slack.telescopeapp.org/).

Next and Meteor will be first-class citizens of Vulcan, but any kind of JS front-end or back-end technology could enjoy it. Be it Gatsby or a custom Node micro-service. At Vulcan, we sell apples AND oranges, as long as they make you an efficient developer.

Now, it’s time for us to get back to work, we have a lot to do. Hope to see you at [Vulcan](http://vulcanjs.org/)!

## A starter from the trenches

Special thanks to Aplines, who trusted my company (LBKE) in using the latest technologies for their product. Thanks to them, we’ve tested all features included in Vulcan Next Starter altogether in a real-life professional application.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/logos-aplines-lbke-1.png)

They are looking for developers, so if you want to learn more about using Next and GraphQL at scale, that’s the place to go: [job@aplines.com](mailto:job@aplines.com)

