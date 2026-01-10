---
title: How to Use Dependabot to Keep Your Environment Up to Date
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-18T22:28:59.000Z'
originalURL: https://freecodecamp.org/news/using-dependabot-to-keep-your-environment-up-to-date
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/zhang-kenny-2CeWChQ7AD8-unsplash.jpg
tags:
- name: dependency management
  slug: dependency-management
- name: npm
  slug: npm
seo_title: null
seo_desc: 'By Leonardo Faria

  Adding dependencies to a project often helps you not reinvent the wheel. But at
  the same time it can cause issues in many different aspects of the project:


  Versioning: sometimes dependencies can require specific versions of other d...'
---

By Leonardo Faria

Adding dependencies to a project often helps you not reinvent the wheel. But at the same time it can cause issues in many different aspects of the project:

* Versioning: sometimes dependencies can require specific versions of other dependencies and this can cause hiccups in your app
* Bundling: you need to be careful not to end up with too much extra code that will bloat your bundles
* Updating: JavaScript moves fast, and if you don't update packages regularly you'll be playing Jenga in the future.

There are different tools to cover the task of updating dependencies, like [Dependencies.io](https://dependencies.io), [Snyk](https://snyk.io/), and [Dependabot](https://dependabot.com/). Since I have been using Dependabot for a while, I decided to write about my experience.

Dependabot is a tool acquired by GitHub a year ago that checks dependency files from different languages (Ruby, JavaScript, Python, PHP, Elixir, to name a few) and finds new versions of libraries you are using in your project. Here is the setup:

![Dependabot screenshot](https://leonardofaria.net/wp-content/uploads/2020/05/dependabot.jpg)

Daily updates can be overwhelming, and I think that weekly updates have a better cost/benefit. Also, I assign myself the Pull Requests so I can get notifications as soon they are opened.

## How to use Dependabot effectively

Dependabot includes, in each PR, release notes, changelogs, commit links and vulnerability details whenever available. This is useful because you can take a look at the information and decide to proceed or not.

However, as pragmatic programmers, we want to ensure things won't break. The PR details are important but more than that, we want a simulation of all (or almost all) deliverables that the project has.

![CI Integration](https://leonardofaria.net/wp-content/uploads/2020/05/semaphore.jpg)

This screenshot shows what happens every time a PR is opened in the components library codebase of my work.

* **Tests (Jest / Bundle)**: the Jest task will test the React components while the Bundle task will simulate the bundling commands we run when we want to update the package in the NPM registry
* **Linters (Stylesheets / JavaScript)**: the stylesheet files follow a custom sass-lint setup and the JS code follows a series of ESLint rules. If a PR introduces a new version of a linter with new rules, we will be able to capture that.
* **Cypress (Screenshot Testing / Accessibility Testing)**: if a new package introduces changes that may be reflected in the look and feel of components, Cypress will capture the difference, screenshot it, and store in S3. Since Cypress needs a live version of the documentation website, we also get the Gatsby build process covered.

With all these steps, it is very unlikely an external package will break our master branch. Kudos to my co-worker Grant Lee that also works on this project.

_Also posted on [my blog](https://bit.ly/2ZhD9GC). If you like this content, follow me on [Twitter](https://twitter.com/leozera) and [GitHub](https://github.com/leonardofaria). Cover photo by [Zhang Kenny](https://unsplash.com/@kennyzhang29?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/dependency-tree?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)_

