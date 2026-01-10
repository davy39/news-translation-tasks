---
title: Yep, JavaScript Moves Fast. Build Your Component Library Anyway.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-06T13:05:16.000Z'
originalURL: https://freecodecamp.org/news/yep-javascript-moves-fast-build-your-component-library-anyway-a50576ab3031
coverImage: https://cdn-media-1.freecodecamp.org/images/1*JFxS_dW4owpFE2ZvJyk1Zw.png
tags:
- name: Angular
  slug: angularjs
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Cory House

  Here’s a question I’ve heard a few times recently:


  “What if we create a component library in React/Vue/Angular/whatever and a new component
  technology replaces it?”


  That’s not a question of if. It’s a question of when. These technolog...'
---

By Cory House

Here’s a question I’ve heard a few times recently:

> “What if we create a component library in React/Vue/Angular/whatever and a new component technology replaces it?”

That’s not a question of if. It’s a question of when. These technologies have become wildly popular, but they’re not the end game. Like all technologies, something better will eventually come along and replace them.

But that fact is largely irrelevant. Establishing a library of reusable components for your company today remains absolutely critical.

Here’s why.

### Move Faster Today

Reusable components help your team move faster by creating higher level abstractions. Components eliminate decision fatigue by programmatically enforcing a standardized approach. Just consider an opinionated form `TextInput` component.

It can eliminate all the following decisions:

1. Should I put the label above the input or beside it?
2. Should I display validation errors to the right or below the input?
3. What color should the error be?
4. How should I mark required fields?
5. Should I validate required fields on blur or upon submit?
6. How much padding should I place between the label and the input?

The list goes on. These aren’t questions your designers and developers should be asking every time they create a new form.

### Enforce Consistency

Reusable components enforce user interface consistency. Your company likely has many developers. Yet your job is to build an app that **looks like it was built by one developer.**

To do that, it’s critical to use reusable components. Copy/paste isn’t a design pattern. If designers and developers have the freedom to start from scratch again and again, your application will quickly become a patchwork of different looks, feels, and technologies.

### Improve Performance

In a client side rendered app, every time you use a component you improve performance. Why? Because it minimizes the application’s bundle size and memory footprint. Using a component a second time **requires no additional download, and hardly any extra memory**.

Without a component library, your team is highly likely to include duplicate JavaScript that solves the same problems in slightly different ways which will bloat the bundle and slow performance. Even worse, they’re likely to grab another competing library and thus require users to download multiple full libraries that do the same thing.

### Less Maintenance

More code leads to more maintenance. More maintenance leads to higher costs and more people which creates additional communication overhead that slows you down even further. Reusable components minimize the amount of code you need to create and maintain today.

### Easier Updates Later

Finally, yes, eventually the component tech you’re using today is going to be legacy. But by creating a reusable component library today, you minimize the surface area that needs updated later.

It’s far easier to migrate a carefully componentized app because you can replace existing components one component at a time. That’s not so easy when your application is a patchwork of different technologies and patterns. Reusable components minimize the surface area you’ll need to update later.

### Low Investment

A component library doesn’t actually require that much work. For instance, if you choose React, you need not, (and typically shouldn’t) start from scratch. There are [literally dozens of mature component libraries](https://github.com/enaqx/awesome-react#components) to choose from and 100’s of standalone components as well.

Use a popular component library as your starting point and tweak it to your needs. Trust me, this need not take long and the benefits are significant.

Alternatively, you could choose to create plain CSS components as your foundation. An example of this approach is [Stacks from StackOverflow](https://stackoverflow.design). The advantage to this approach is twofold:

1. If you move to a new technology in the future, the plain CSS foundation that you’re using behind the scenes in your JavaScript components can be reused.
2. If your company is currently using multiple component approaches such as React, Angular, and/or Vue, then this CSS approach can be used as the foundation for all.

The disadvantage? You have to build your components from scratch so that they utilize your plain CSS component foundation.

My preference? Leverage an existing JavaScript component library as your foundation to minimize the amount of code you need to write to get rolling.

### Summary

Don’t let the rapid innovation in JavaScript scare you away from investing in a reusable component library for your company. Yes, today’s technology will eventually be replaced, but change is the only constant in technology. For all the reasons above, reusable components are worth embracing today.

Looking for more details on how to get this done? I recently published “[Creating a Reusable React Component Library](https://app.pluralsight.com/library/courses/react-creating-reusable-components/table-of-contents)” on Pluralsight. ([free trial](https://help.pluralsight.com/help/free-trial-10-days-andor-200-minutes))

### Looking for More on React? ⚛️

I’ve authored [multiple React and JavaScript courses](http://bit.ly/psauthorpageimmutablepost) on Pluralsight.

![Image](https://cdn-media-1.freecodecamp.org/images/ukD8krGR7M8AnnK7lzjsuLRcFnAOUcCPEIZr)

Cory House is the author of multiple courses on JavaScript, React, clean code, .NET, and more on [Pluralsight](http://pluralsight.com/author/cory-house). He is principal consultant at [reactjsconsulting.com](http://www.reactjsconsulting.com), a Software Architect, Microsoft MVP, and trains software developers internationally on front-end development practices. Cory tweets about JavaScript and front-end development on Twitter as [@housecor](http://www.twitter.com/housecor).

