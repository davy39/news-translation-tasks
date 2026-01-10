---
title: How to start an Open Source project
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-04T21:42:17.000Z'
originalURL: https://freecodecamp.org/news/how-to-start-an-open-source-project-in-new-years-945bad8800d7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*skkIJz5B4nwZya06X4Q61w.jpeg
tags:
- name: open source
  slug: open-source
- name: project management
  slug: project-management
- name: Ruby
  slug: ruby
- name: Ruby on Rails
  slug: ruby-on-rails
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Dmitriy Strukov

  My name is Dima and I’m Ruby developer. Today I want to share my experience creating
  an open source solution. I will talk about what steps the project should take, how
  to choose the right functionality for the first release, and wh...'
---

By Dmitriy Strukov

My name is Dima and I’m Ruby developer. Today I want to share my experience creating an open source solution. I will talk about what steps the project should take, how to choose the right functionality for the first release, and what mistakes I faced personally when creating my open source project.

Half a year ago, I got the idea that it would be good to create an open source project. Instead of test tasks for the interview, it would be enough for me to send a link to the repository. The prospect of helping colleagues with the solution to their everyday problems inspired me.

I’ve always disliked gems for creating administration panels. Any extra movement needs to redefine the class, and for change fields you need to make changes to the files. After thinking and conversing with colleagues, I decided to create a new library which would be flexible and would not require dashboards or configuration files.

### Determine the goals

Every open source project solves a specific problem. Talk with colleagues, chats, forums, and share your idea. It all helps you on the first steps to understand important things, like which solutions already exist, and to hear criticism. Talk with people who already have open source projects. They can give you very valuable advice, so don’t be afraid to ask and take the initiative.

One important bit of advice which I got at that stage is to pay attention in the first place on the documentation of the project. You can have a very good project, but no one will spend the time to understand how it works.

The most important aspect, without which further steps are impossible, is motivation. The idea of the project should inspire you primarily. Most often people get used to the tools with which they work and fall into a comfort zone, so external opinions may be ambiguous.

### Planning

The choice of a certain task manager is a matter of taste. It should have a clear picture of the tasks and stages of your project.

Divide tasks into sub-tasks. Ideally, if one task does not take more than 3–4 hours, it is important to enjoy the implementation of small tasks. This will help to avoid burnout and loss of motivation.

I use [pivotal tracker](http://pivotaltracker.com/). The main advantage is a free version for open source projects where you can sort tasks by type (feature, bug, chore, release), and group them into releases and determined deadlines.

### Documentation

Every open source project should contain these things:

* README
* Open Source license
* Contributing guidelines
* Changelog

The README file not only explains how to use your project, but also the purpose of your project. If you do not know how to properly write a README file, you can look at other known open source projects or use a [template](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2).

The license guarantees that others can use, copy and modify the source code of the project. You need to add this file to each repository with your open source project. MIT and Apache 2.0 GPLv3 are the most popular licenses for open source projects. If you are not sure what to choose, you can use this convenient [service](https://choosealicense.com/).

The CONTRIBUTING file will help other developers contribute to the project. At the first steps of the project, it is not necessary to pay close attention to this file. You can use the already prepared template from another project.

Changelog contains a supported, chronologically-ordered list of significant changes for each version. As with the CONTRIBUTING file, I do not advise paying special attention to this at an early stage.

### Versioning

To track important changes for users and contributors, there is a [semantic version](https://semver.org/). The version number contains numbers and adheres to the following pattern X.Y.Z.

* X major release
* Y minor release
* Z patch release

### Continuous integration / Continuous delivery

To automatically run tests and build, I use [Travis CI](https://travis-ci.org/). It’s also a good idea to add badges to display the successful assembly of the build in the wizard, the test coverage ([Codecov](https://codecov.io/)), and the documentation ([Inch CI](https://inch-ci.org/)).

![Image](https://cdn-media-1.freecodecamp.org/images/GOv6LmGVzeTtbenyF6xAowGpn9QSBHNRr9oB)

After each new commit or merge in the master, I automatically have a deploy on [Heroku](http://heroku.com/) (very convenient integration with GitHub). All tools are absolutely free for an open source project.

### My mistakes

To analyze the initial stage, I had an idea, but there was no clear plan. I decided that I wanted to do this without having a clear idea of how much time it would take or a specific representation of the functions that would be in the first version of the library. I had just a lot of desire and lack of a clear plan.

Also, after reading the history of other projects (not only open source), I noticed that at an early stage, some plans are too optimistic. They need a reassessment of their strengths and capabilities. But it’s not easy to find time each day to write a new feature in the project. Most of the tasks eventually had to be weeded out, leaving the necessary minimum for [MVP](https://en.wikipedia.org/wiki/Minimum_viable_product).

At the moment my [simple-admin](https://github.com/evil-raccoon/simple_admin) project is in the alpha version. Further plans include creating a separate version of the library for [Hanami](http://hanamirb.org/).

