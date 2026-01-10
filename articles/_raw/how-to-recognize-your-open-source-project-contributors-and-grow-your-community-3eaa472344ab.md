---
title: How to recognize your open source project contributors and grow your community
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-03T18:01:44.000Z'
originalURL: https://freecodecamp.org/news/how-to-recognize-your-open-source-project-contributors-and-grow-your-community-3eaa472344ab
coverImage: https://cdn-media-1.freecodecamp.org/images/0*4y_hyryvT4SZ0wKa
tags:
- name: community
  slug: community
- name: GitHub
  slug: github
- name: open source
  slug: open-source
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By David Herron

  There’s a truism — if a community is not growing, it is slowly dying. How is your
  open source community doing? Is your contributor base stagnant, shrinking or growing?
  Are you like many open source community leaders with little idea o...'
---

By David Herron

There’s a truism — if a community is not growing, it is slowly dying. How is your open source community doing? Is your contributor base stagnant, shrinking or growing? Are you like many open source community leaders with little idea of how to encourage new participation?

There are many opinions out there about growing the activity around an open source project. Successfully building an open source community-driven project is more than just throwing your code on Github and doing development in the open.

Folks must know the project exists, that you’re open to contributions, what the contribution process is, coding practices in the project, and so on.

One very visible tactic is to establish what some call “social proof”. That is, some kind of visual indicator that the project is currently receiving contributions.

What does the word “community” mean in this context?

A “community” is a group of people coming together for a shared purpose or shared goal. The traditional meaning is the folks living in a town, and their shared goal is living peacefully together in that city.

But communities can form for other purposes. For example, a Facebook group about electric motorcycles will host discussions of electric motorcycle brands, where to ride, how to maintain or customize the bikes, and so on. As the members get to know one another through discussing electric motorcycles, they form a community.

Likewise, the folks maintaining an open source software project also form a community whose goal is improving that software. This article is focused on one aspect of growing community participation in an open source project — acknowledging those who contribute to the project.

Many project websites have “widgets” showing data like build status, whether the tests are passing, and so forth. What if another widget showed an indicator of contributors to the project? Namely:

* A list of folks making code contributions — demonstrating to the public that this project has contributors
* Giving kudos to contributors, so they can have bragging rights, and to feel appreciated
* Demonstrate there is communal ownership of the project
* Demonstrate who has how much of a stake in the project
* Tell the public this project is not the hair-brained idea of one guy/gal who’s coding to suit their whims

The existence of build status widgets and the like demonstrates a place for automatically-updated widgets giving data about open source projects. These widgets are geared for the public, and the purpose is reassuring potential users or contributors the project has an automated build and test system, and whether the current status is green.

But that’s not the only kind of status system a project team may use. For team management purposes, a team might use a private dashboard giving the status of various aspects of their project. Commercial software projects regularly do this. Dashboards are maintained by the product manager to measure progress towards goals. This post is not talking about that kind of status system, but instead, one that is shown to the public.

Isn’t it reassuring to know an open source project is team driven? That there is more than one set of eyeballs looking for bugs? That the direction is not the mad ravings of one person but driven by a collaborative process? If you’re looking to integrate an open source tool into the software driving your business, don’t you need to know the tool has a stable future?

Let’s think first about a status widget that does some of the above. Then look at what some prominent open source projects are doing along these lines. Finally look for any existing tool of this nature.

### Brainstorming

Generally speaking, we’re talking about a “status widget” to install on project pages, like the source code repository. The widget must present some data about the contributors to the open source project, and implement as many of the ideas above as possible. Some possible attributes to show are:

* Easily installed — insert an HTML widget into websites
* Automatically retrieve data from Github/Gitlab/etc commits
* Identify the type, size, etc, of code changes in commits
* Present contributor data in several forms (customizability)
* Present useful information about each contributor
* Present useful information about total contributions
* Be utterly objective about listing contributors

### Actions by some Open Source projects to recognize contributors

Since it’s useful to take a look around and see what others are doing, let’s look at certain high profile open source projects. What are they are doing in terms of recognizing contributors?

![Image](https://cdn-media-1.freecodecamp.org/images/Q4ApyCiQwPu6FgdgSTKvnBzFQqBv7ubTxZG9)

[**Vue.js**](https://github.com/vuejs/vue) — This leading UI framework for modern web applications has a “Contributors” widget that links over to a Github page which displays [Vue.js code contribution data](https://github.com/vuejs/vue/graphs/contributors). The contributor's widget is somehow derived from an [OpenCollective widget](https://opencollective.com/vuejs) showing “backers” of the Vue.js project. This shows monetary contributors. The avatars do not necessarily correspond to code contributors on the project.

![Image](https://cdn-media-1.freecodecamp.org/images/moMCsgpU77dEhhZZzCwZWmBX9ITffZ8AzBw5)

[**ReactJS**](https://reactjs.org/) — This leading UI framework for modern web applications has a well-developed Contributors area. But nowhere was there found a listing or recognition of contributors.

![Image](https://cdn-media-1.freecodecamp.org/images/heHQ4uxSD0Vio8Ml0A8RP0QAKSEithTjh-3d)

[**Bootstrap**](https://github.com/twbs/bootstrap) — This leading responsive UI framework has a well developed Contributors area. On the main page of the repository are mentioned Mark Otto and Jacob Thornton as the Creators. Under “Copyright” it mentions ownership is split between Twitter and “The Bootstrap Authors”. The latter linking to the Github-generated list of contributors.

![Image](https://cdn-media-1.freecodecamp.org/images/ugQVI44EsOks7Idb3cegcM0c5KPqIOatZg-x)

[**Webpack**](https://webpack.js.org/) — The project homepage shows several lists of monetary contributors. Each generated by OpenCollective. On the [Webpack project repository](https://github.com/webpack/webpack), it’s clear there is a well-developed Contributors area. It also includes a link to a Medium publication. Here they publish information about how to contribute to the Webpack project. The only folks mentioned here are the Webpack Core Team. Again the lists of monetary contributors generated by OpenCollective.

![Image](https://cdn-media-1.freecodecamp.org/images/3PiDzuv4oAthFV3MFpCCYvtPTGa41qDPrF4l)

[**jQuery**](https://jquery.com/) — This extremely popular library for DOM manipulation in web browsers has a very well [developed contributors guideline](https://contribute.jquery.org/). Nothing could be found listing the contributors.

![Image](https://cdn-media-1.freecodecamp.org/images/FqjvoLHaDPjoQy8oEuemMhog8k2ZjsvHJtAb)

[**ExpressJS**](https://github.com/expressjs/express/) — This popular framework for developing web applications with Node.js. It shows TJ Hollowaychuk as the original author and Douglas Wilson as the current project maintainer. It then links to the contributor list generated by Github. It’s clear from that list those two made the overwhelming majority of code contributions to the project.

![Image](https://cdn-media-1.freecodecamp.org/images/ItB6IMsKyiOJ1LopxoqLAT8-7oXsVoN0IZzr)

[**Node.js**](https://nodejs.org/en/) — This popular platform for JavaScript development outside web browsers has a Foundation and a highly structured set of maintainers. The Node.js Technical Steering Committee has final authority over technical direction and governance. There is a [manually maintained list of TSC members](https://github.com/nodejs/node/blob/master/README.md#tsc-technical-steering-committee) in the repository. Another manually maintained list contains [the other collaborators](https://github.com/nodejs/node/blob/master/README.md#current-project-team-members). These lists are replicated on the [main Node.js repository home page](https://github.com/nodejs/node).

Alongside the TSC is the [Community Committee](https://github.com/nodejs/community-committee) which is focused on “community-facing efforts”. A manually-maintained list of Community Committee members is in that projects repository.

One item of note about these manually maintained lists is that they’re in the project Git repository. The process for resigning from one of these teams is to issue a Pull Request against that page announcing the intention to resign from the project team. That’s an interesting use of Git, to track project members over time.

![Image](https://cdn-media-1.freecodecamp.org/images/cjbqk2D-6DF2j9f1pNoaoBQEvTEXfYQJ09ez)

[**Django**](https://www.djangoproject.com/) — This popular Python framework for developing web applications has both a Foundation to handle business matters, and a few technical teams for technical matters. [The technical team members are published on the project website](https://www.djangoproject.com/foundation/teams/). There is a well developed contributors guide.

![Image](https://cdn-media-1.freecodecamp.org/images/qp4fEmsYFD7W30dzhhfOx5FRpZ8gp7loVjxj)

[**Cheerio**](https://www.npmjs.com/package/cheerio) — This popular Node.js project implements a subset of the jQuery API to run on the Node.js project for server-side DOM manipulation. The project README includes a list of contributors that is generated by running Git commands. This makes it an automatically generated list but the user experience is pretty bad. The [Github repository](https://github.com/cheeriojs/cheerio) shows lists of monetary contributors generated by OpenCollective.

![Image](https://cdn-media-1.freecodecamp.org/images/sSP6E0Piqq-Y4bGYAwzpTKytYJCYklSUVvmS)

[**BabelJS**](https://babeljs.io/) — This popular JavaScript developer tool is a transpiler allowing us to use modern JavaScript while deploying to older environments. The website has an extensive “_Meet the Team_” page. This page lists a wide range of contributors, including a non-human contributor (a Twitter bot). The Github repository contains a list of monetary sponsors generated by OpenCollective.

![Image](https://cdn-media-1.freecodecamp.org/images/M8Z9rRyZCR58CyNTkW5hTW7HRuTwN7ANNedJ)

[**Rust**](https://www.rust-lang.org/) — This new systems programming language promises blazing fast execution, no segfaults, thread safety, and more. The [team page](https://www.rust-lang.org/en-US/team.html#Community) appears to be manually maintained, and lists a dozen or so teams supporting Rust. Each team has a dozen or more members.

### Tools to assist automagically recognize contributors

We learned in the previous section that most open source projects try to acknowledge contributors and core team members. But that in most cases this is with manually maintained lists.

Manually maintaining a list of contributors is an administrative burden. It can create a situation where a contributor does not get recognized because nobody remembered to add them to the list. Just as we strive to automate software testing to ensure good development processes, we might also strive to automate contributor recognition to ensure everyone is recognized fairly. Let’s look at several ways of implementing an automated widget.

**Use the auto-generated contributor list on Github or Gitlab:** Every Github project has an easily-accessed page showing contributions. Gitlab-hosted projects have a similar page that is harder to reach. Some projects simply link to these pages. The Github page is pretty useful, but it’s not the same as a status widget.

**Create your own list**: Using git commands (_git shortlog -sn_) it is possible to generate a list of committers. An inventive programmer could turn this into a list of avatars.

We found an older (seemingly abandoned) project that did just that: [https://github.com/blossom/contributors](https://github.com/blossom/contributors)

**The OpenCollective Widget**: [Open Collective](https://opencollective.com/) is a kind of social movement meant to create projects that are openly financed. It’s an interesting idea and worthy of further exploration. For the purpose of this article, the Open Collective team offers a dynamic widget that’s easy to install in a website, that shows contributors. Many open source projects are Open Collective projects, and use this widget. However, in this case “contributor” means monetary contributions rather than code contributions.

**Sourcerer.io Hall of Fame**: [Sourcerer.io](https://sourcerer.io) is a service to automatically generate a profile page for software engineers based on their source code commits. It supports generating a personal profile from any set of git repositories. Github and Gitlab get the best support. For example, see my profile [https://sourcerer.io/robogeek](https://sourcerer.io/robogeek).

The Sourcerer.io _Hall of Fame_ tool generates a summary of committers to Github projects. It picks up the user avatar, either from a Sourcerer profile or Github profile. Installation is very simple once you have a Sourcerer account. Head to the Hall of Fame tab in the Settings area and follow the directions. Sourcerer’s service takes care of the rest.

The associated [Github repository](https://github.com/sourcerer-io/hall-of-fame) has a few example Hall of Fame widgets, such as [iterative/dvc](https://github.com/iterative/dvc) and [epicmaxco/vuestic-admin](https://github.com/epicmaxco/vuestic-admin).

### Conclusion / Observations

We started this article theorizing that public recognition of contributors to an open source project would help the project to grow. The idea seems sound but we don’t know if it’s true. What we did learn is that many open source projects already have methods to recognize contributors (particularly the ones which do not seem to be corporate-backed — e.g. ReactJS).

Not all contributions are in the form of software. Some projects have teams for marketing, or documentation, or testing, or security. An automated tool that scans Git commits will not be able to list folks making non-code contributions to the project. Those contributions do not land in a Git repository. Therefore a tool to generate a contributors widget for source contributions has a limited scope. By listing code contributions the widget does not list the other contributors.

The primary acknowledgement tactic among the open source projects we examined are manually maintained lists of team members. A project may have one or more “teams” assigned to handle different areas. Of course some of these teams focus on non-coding work. These team lists acknowledge the non-code contributors as well as the coders.

Another common tactic is acknowledging monetary contributions using the OpenCollective widget. It is easily installed and OpenCollective’s systems take care of updating the widgets. Of course it has limited scope. It does not serve the purpose of recognizing code contributions to a project.

We started this noting many teams have automated status widgets, and pondering a status widget for code contributors. While one can roll their own code contributor status widget, the simplest method is to install the Sourcerer.io _Hall of Fame_ widget. It is easy to install and it manages itself. It concisely shows some of the contributors in a fashion that fits right next to the other status widgets. Keep in mind this only shows the code contributors.

Acknowledging team members isn’t the only step to building an active open source project with multiple contributors. The advice we [found](https://sudarmuthu.com/blog/how-to-encourage-contribution-in-open-source-projects/) focused more on having a well documented contribution process, for example. There are many aspects to building and nurturing a community of folks working together on a goal. Obviously giving acknowledgement is one.

With that in mind, an automated code contributor status widget should be one of many tools used for encouraging contributions to your open source project.

