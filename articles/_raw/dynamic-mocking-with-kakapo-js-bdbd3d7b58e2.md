---
title: Dynamic mocking with Kakapo.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-06-25T08:11:07.000Z'
originalURL: https://freecodecamp.org/news/dynamic-mocking-with-kakapo-js-bdbd3d7b58e2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*AWc9hdd-JQUromU-wYWeDA.jpeg
tags:
- name: Design
  slug: design
- name: iOS
  slug: ios
- name: JavaScript
  slug: javascript
- name: open source
  slug: open-source
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By zzarcon

  3 months after the first commit, Kakapo.js reaches the first release and we are
  proud to announce that now it is ready to use. Let us introduce you Kakapo.


  Kakapo - The next generation mocking framework in Javascript


  Kakapo is just a set...'
---

By zzarcon

3 months after the first commit, [Kakapo.js](http://github.com/devlucky/Kakapo.js) reaches the first release and we are proud to announce that now it is ready to use. Let us introduce you Kakapo.

> Kakapo - The next generation mocking framework in Javascript

Kakapo is just a set of tools that tries to make your life easier when building web apps, specially when creating **client side mocks**. It provides components and APIs which let you easily replicate your backend logic and responses in the client-side.

This is nothing new and I’m quite sure you are familiar with tools like [jquery-mockjax](https://github.com/jakerella/jquery-mockjax), [FakeXMLHttpRequest](https://github.com/pretenderjs/FakeXMLHttpRequest) or [fetch-mock](https://github.com/wheresrhys/fetch-mock), those tools are great and have been there for quite a loot of time but in my opinion they are just one part of the solution of a big problem.

Why should you care about client side mocking? To solve the _Backend-Bottleneck_**.**

![Image](https://cdn-media-1.freecodecamp.org/images/1*UJ2ClAEKWpWAM_QF5kj9Kg.jpeg)

### Backend Bottleneck

Last sprint retrospective, after the third sprint in a row missing more than 50% of the planed points, we were starting to ask ourselves what was going wrong. Some back end devs were saying:

* _Yeah, we thought it was an easy task but we had to spend 1 week refactoring the current functionality to make it working as expected…_
* _Too much not planned stuff came out and we had to take care of those issues happening in production…_
* _Staging servers were not working at all and we had to re-deploy the service more than 5 times…_

On the other side, front end devs:

* _I spent the whole Monday trying to figure out why the endpoint was returning 500 status code instead of getting the expected response…_
* _We were building the user profile but the create endpoint was not documented, so we couldn’t make it for the release…_
* _Yesterday I had to switch too many times within different staging environments that I didn’t had time to work on the feature…_

I was very frustrated about the current situation and, specially, not being able to ship a small feature in the estimated time. It took me quite some time to realize that it was not a backend or client problem: the issue was something deeper and would require more time and effort to be fixed.

> What about not dealing with backend issues and staging environments but instead building the feature based on a JSON response agreed with the backend team beforehand?

Let’s see a basic example to get an idea of how it works:

In the example above we are just defining a couple of endpoints and one factory, then we define some business logic inside the request handlers in order to return the fake responses. To do this we use three key elements of Kakapo:

* [**Router**](http://devlucky.github.io/kakapo-js#router): Kakapo’s router recognizes URLs (routes) and dispatches them to the associated handlers. It also provides a **request** object as argument that gives you useful information about the incoming request.
* [**Database**](http://devlucky.github.io/kakapo-js#database): This class along with **factories** and **relationships** allows you to define how your entities should be represented and their behaviors.
* [**Server**](http://devlucky.github.io/kakapo-js#server): It connects all other components and lets you activate or deactivate them; this feature gives you the ability to switch between multiple databases and routers, we call this [scenarios](http://devlucky.github.io/kakapo-js#scenarios).

#### Client side mocking in real life

Usually mocking APIs is done by creating a **static JSON** for every single request and testing against it. Creating and maintaining the JSON is a repetitive task and error-prone.

Kakapo, instead, lets you **dynamically mock** your responses by defining how they should look like and automatically serialize them into JSON.

As an example, let’s try to make a CRUD

That’s how easy is to replicate a CRUD with Kakapo, you might also take a look at [fake data](http://devlucky.github.io/kakapo-js#fake-data) and [serializers](http://devlucky.github.io/kakapo-js#serializers) to see some goodies of Kakapo.

### Technical challenges

Besides all the stuff we have learned in the process of building the library, I would like to point out some of the most challenging things we had to face:

#### Interceptors

The [interceptor](http://devlucky.github.io/kakapo-js#interceptors)s components are the ones in charge of _intercepting_ the user request, check if matches any of the routes and apply the mock, they are designed in such a pluggable way that the user can define his owns. Currently we are supporting the browser networking APIs, [XMLHttpRequest](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest) and [fetch](https://developer.mozilla.org/en/docs/Web/API/Fetch_API) but soon we will support Node.js ?.

> Reinventing the wheel is not implicitly bad. You can learn a lot doing it.

I found this component complicated because you have to replicate the same functionality that the browser APIs provides, as soon as you behave a bit differently, the application might break since it depends on the native behavior. You can learn a lot while building this stuff directly with native APIs instead of using wrappers like jQuery, because you will really understand how it internally works.

While implementing the interceptors we had to make sure to not break popular networking libraries like [jQuery](http://api.jquery.com/jquery.ajax/) and [Superagent](http://visionmedia.github.io/superagent/); we created [_integration tests_](https://github.com/devlucky/Kakapo.js/tree/master/test/specs/integration) to ensure that Kakapo will continue to work as expected after introducing new changes.

#### Testing

Testing is a must when developing software, but is even more critical in open source projects that other developers will potentially use. We always had this in mind while creating Kakapo and this was the first project I ever did in a strict **TDD** way. I have to admit that the feeling I had at the beginning was way different than the one I have now. Sometimes I felt that writing so many tests was slowing us down, but now with [high code coverage](https://codecov.io/github/devlucky/Kakapo.js?branch=master), I feel really confident when I have to refactor a critical component or add a new feature to the library.

This is something you have to introduce in your workflow incrementally and define with the team. Since this was the biggest open source project I ever worked on, I learned how to coordinate and work with a team. Sometimes things need to be discussed [twice or more](https://github.com/devlucky/devlucky.github.io/issues/4) just to make sure that all the members are on the same page, but at the end is going to work out.

### Importance of documentation

Developers _hate_ writing documentation. Unfortunately, it is as important as having a good library and will be the first thing your users and contributors will see.

Think about it this way: you have been building your library for some months and now is finally ready, don’t you think it is worth the effort to spend some days [building a website](https://pages.github.com/) and writing some good examples?

This is a talk from React Europe 2016 in which [Christopher Chedeau](https://twitter.com/Vjeux) explains how Facebook deal with spreading open source libraries.

#### Jekyll

[Jekyll](https://jekyllrb.com/) literally saved us, it improved the way we write documentation and the velocity. Before choosing Jekyll, I used to build static websites with some css and html to then place there the docs. However, some developers might not be fluent and miss the simplicity of [Markdown](https://en.wikipedia.org/wiki/Markdown). That’s why we decided to go for Jekyll which lets you write your pages in [Kramdown](http://kramdown.gettalong.org/) (markdown with steroids) and is integrated with Github Pages.

Once we felt comfortable with the status of the docs and the examples, we also wanted to give a good first impression to newcomers. We created a [script](https://github.com/devlucky/Kakapo.js/blob/master/create-readme.js) which fetches the **md file** from the [github page](https://github.com/devlucky/devlucky.github.io), adds some content and outputs the [readme](https://github.com/devlucky/Kakapo.js/blob/master/README.md) ?

#### Demo Apps

Everyone likes demos, they show what your library does and how it does it. It might sound weird, but it will also help you to learn how to use your own library, as well as finding bugs or missing features.

Until we built our first [todo app](https://kakapo-todo-app.firebaseapp.com/) using Kakapo we didn’t realize about the major pain points and how to solve them, that’s why we later built our second demo app, a [github explorer](https://kakapo-github-explorer.firebaseapp.com/).

> Having a good library without documentation is like having rocket that nobody knows how to use it.

### ROADMAP

The project just started but we have ambitious plans for it; feel free to check the [open issues](https://github.com/devlucky/Kakapo.js/issues) or open new ones, we will really appreciate it! Here are some of the most important:

* Full [**JSON API**](http://jsonapi.org) serializer support
* **Node.js** interceptors support
* **Async handlers** support

We are also working hard to finish [the Swift version of Kakapo](https://github.com/devlucky/Kakapo) which is almost ready for the beta phase and we think is going to be a game changer to build iOS applications: stay tuned! ?

