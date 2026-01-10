---
title: 10 Popular Web Development Tools that Every Programmer Should Know
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-06T19:37:00.000Z'
originalURL: https://freecodecamp.org/news/handy-web-development-toolkit
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/screely-1586183781361.png
tags:
- name: 100DaysOfCode
  slug: 100daysofcode
- name: web
  slug: web
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Mehul Mohan

  Are you planning to get into web development? Take a tool with you, it''s scary
  out there. Let''s take a look at some common web development tools that''ll help
  you speed up your workflow and be a better web developer.

  Note that your mile...'
---

By Mehul Mohan

Are you planning to get into web development? Take a tool with you, it's scary out there. Let's take a look at some common web development tools that'll help you speed up your workflow and be a better web developer.

Note that your mileage may vary a lot. This article just lists the most popular solutions out there in the wild. You still need to integrate them in your projects and learn more about them. 

With that being said, here's a list of most common tools/packages I use in my workflows regularly.

## #1 VSCode ?

VSCode needs no introduction. It's a beautiful and powerful code editor that supports extensions, integrated terminal, snippets, themes, shortcuts, remote SSH, and much more - according to your needs. 

Running on top of electron, it is cross OS compatible and is constantly improved by Microsoft as an [open source project](https://github.com/microsoft/vscode). VSCode comes with a rich set of tools, IntelliSense through Language Server Protocol, and quick fixes/patches all through the year.

![VSCode](https://code.visualstudio.com/assets/home/home-screenshot-mac-2x.png)


Get VSCode now from the official [VSCode site](https://code.visualstudio.com/).

## #2 Webpack ?

Webpack sells itself as a module bundler, but in reality, it is much more extensible than that. You can attach a plethora of plugins and tweak its configuration to make it more robust and fit to your needs. 

Webpack 4 comes as a **zero config module bundler** - that means you can get started with Webpack almost immediately! You just have to download the module using `npm i webpack` and then run `npx webpack` in your directory. Here's how to setup zero configuration with webpack:

%[https://www.youtube.com/watch?v=g9_91gUHy6k]

## #3 Cypress ?

Cypress is a great e2e testing tool which can actually spin up a headless or a full chrome window to run actual tests of your code. It can interact with asynchronous code in a very intuitive manner. For example, it waits for resources to load/become available, unlike Selenium, which is quite an old technology made for automated testing of mostly static sites. Let's see how Cypress works through a quick video:

%[https://vimeo.com/237527670]

Cypress tests are very simple and human-friendly to write, and it does all the heavy lifting out of the box (like launching a chrome instance, proper keyboard events, trusted event emitters, you name it). Get cypress [here](https://www.cypress.io/).

## #4 TypeScript ?

Writing plain JavaScript? It can be really painful to find subtle bugs and errors without proper linting. To make it even more powerful with better type checking and module autocompletion, take TypeScript with you. 

TypeScript is a superset of JavaScript which transpiles down to JavaScript before executing. This means that you get JavaScript running just like before, but with the added development benefit of coding JS in a 'stricter' manner. 

It wouldn't be wrong to say that TypeScript really enables helpful JavaScript codebase maintenance and makes refactoring a breeze. You can start learning TypeScript through their [official docs](https://www.typescriptlang.org/docs/handbook/typescript-in-5-minutes.html).

## #5 Sentry ?

Sentry is an error reporting service for production. Many a time, especially on the front end, your users might face crashes or unexpected bugs. 

I personally use Sentry for [codedamn](https://codedamn.com), and I've fixed quite a few nasty bugs and causes of crashes which were rare and had happened to very specific users during very specific actions taken on the platform. 

As a bonus, Sentry exists on a lot of platforms, and is not only restricted to JavaScript runtimes. This means Sentry can be used with mostly any popular tech stack. 

Sentry sends full stack trace/information about the bug right into your dashboard so that you can fix that nasty bug on the next release cycle. Read about [sentry here](https://sentry.io).

%[https://player.vimeo.com/video/340759078]

## #6 Git ?

Git is the magic wand of any large project. Git is a Version Control System (VCS) allowing you to incrementally build your software, while maintaining a complete diff of the previous builds. This means you don't lose any history and can easily revert back to last working point. 

Not only this, you can branch off and work on something completely different, without actually affecting the original project. This concept is called branches in git. There's so much more about git you can learn. I love this series from thenewboston on git. Have a look:

%[https://www.youtube.com/playlist?list=PL6gx4Cwl9DGAKWClAD_iKpNC0bGHxGhcx]

The most popular solution for hosting git repos is GitHub. It offers free public and private repositories. You can learn more about git [here](https://git-scm.com/).

## #7 Babel ?

Babel allows you to write bleeding edge JavaScript features, but then transpile them to browsers in a standard those browsers know and have implemented for ages. 

Using babel with webpack is a very powerful combination that allows you to use cutting edge features and then bundle/minify them together. This provides the best experience for developers when developing apps as well as for serving minified builds to users for speed and performance.

For example, you can write ES2020 code in babel and let it transpile it down to the ES2015 version to ship to browsers. It makes writing JavaScript really fun and convenient as it allows you to use JavaScript from the future! Learn about babel [here](https://babeljs.io/).

## #8 Material UI ⭐️

Material UI is a specification from Google on how layouts should be created. On top of Material UI, there are a lot of component libraries available for a number of frameworks like Angular, React, or React Native. Some component libraries include:

1. [Material UI - React](https://material-ui.com/)
2. [React Native paper](https://callstack.github.io/react-native-paper/)
3. [Vuetify](https://github.com/vuetifyjs/vuetify)
4. [Angular Materials](https://github.com/angular/components)

This eases the process of building a lot of components manually for developers. And at the same time, it provides them with fast and well-designed components. Learn about Material UI [here](https://material-ui.com/).

## #9 Joi ?

Data validation is an important part of any application. This is because you can never trust data coming from a user. For large scale applications with multiple endpoints to reach to backend server, it can become very tricky to handle all the edge cases. 

Joi is a very handy library that helps you validate all the incoming data through a strict predefined schema. Joi allows you to construct schemas for arrays, objects and even the values they should accept. 

Should the input fail, it also allows you to customize the error messages. No more hassles of `obj && typeof obj === 'string'` in your code anymore! Using Joi's schema is not only safe but also makes your code much more readable for other developers. Learn more about Joi [here](https://github.com/hapijs/joi).

## #10 Docker ?

Setting up docker for development comes with its own set of challenges (speaking from experience). But once done, it's worth the investment. Partially because you remove the "it-works-on-my-machine" errors. 

But also, running sandboxed code has another benefit. In the unfortunate event that your web application is hacked or brought down, the docker container would make sure that the attack is contained to only that particular container and no other service is affected (unless, of course, your container has substandard security rules). 

You can get started with Docker today! Start with this playlist:

%[https://www.youtube.com/watch?v=avsJnrdN-YU&list=PLYxzS__5yYQlzv9_z1eZmZY8dzMlQFbaH&index=2&t=0s]

# Conclusion

The web is vast, and if you're just getting started it can be overwhelming to begin! Get some help from fellow developers who've been in your shoes. You can even reach out to me on [twitter](https://twitter.com/mehulmpt) / [instagram](https://instagram.com/mehulmpt) and connect. I'll be happy to help.

Do you wish to learn web development and other programming languages in a completely new way? Head on to a [new platform for developers](https://codedamn.com) I'm working on to try it out today! 

