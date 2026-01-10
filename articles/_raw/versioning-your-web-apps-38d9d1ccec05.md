---
title: How to use version control to keep your web apps up to date
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-07-08T03:30:25.000Z'
originalURL: https://freecodecamp.org/news/versioning-your-web-apps-38d9d1ccec05
coverImage: https://cdn-media-1.freecodecamp.org/images/1*wS8MJ0MGrw6ZpVVQmPPHdA.png
tags:
- name: Git
  slug: git
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
- name: webpack
  slug: webpack
seo_title: null
seo_desc: 'By Kamlesh Chandnani

  Version Control helps you keep track of which users are using what version of your
  app.

  With native apps, you have to maintain the versioning of your app with each build.
  Then only you will be able to release the new version of y...'
---

By Kamlesh Chandnani

Version Control helps you keep track of which users are using what version of your app.

With native apps, you have to maintain the versioning of your app with each build. Then only you will be able to release the new version of your app to App Store/Play Store.

But how will you maintain versioning for your web apps?

Story Time!

In the early 90’s, there were server side languages like PHP, Java, and JSP, which helped all your users always get the latest version of your web app.

But now Web Apps have reached a new level. Everything is client side! Hence we can take advantages of the concepts like pre-caching, on demand load, rendering meaningful data at the same time, and so on.

But this can also introduce issues if the user always accesses the cached copy of our web app.

Imagine a SaaS company whose end users are not aware of how to use web apps/next generation web apps/PWAs in the right way.

When it comes to modern web apps like PWAs, you cannot ensure that all your users are using the latest copy of your app’s code.

Assume that you have shipped your web app for the first time, and the users have started using it.The app gets cached after the first visit, and thereafter on each repetitive visit the user will get the cached copy of your app until the new version of your apps code is available. Everything works smoothly.

But now assume that after some time, over the next iteration, you added some new functionality to your existing web app and deployed the new piece of code/bundles.

***BOOM***

How do you ensure that your users are using the latest version of your web app?

How will you identify how many users are still using the old version of your app?

All these questions encourage you to maintain and store the current version of your web app, so that whenever the users are using your app the app version is also getting stored in the DB server.

But the mystery of “How” to maintain versions remains unsolved!

[Git Revision Webpack Plugin](https://www.npmjs.com/package/git-revision-webpack-plugin) comes to your rescue if you use webpack for bundling your code.

It is a Simple [webpack](http://webpack.github.io/) plugin that generates `VERSION` and `COMMITHASH` files during builds based on a local [Git](https://www.git-scm.com/) repository.

### Usage

1. Add a tag to your commit.

```
syntax: git tag <tag-name>git tag v1.0
```

2. Add the following to your webpack config file:

```
const GitRevisionPlugin = require("git-revision-webpack-plugin");
```

```
const gitRevisionPlugin = new GitRevisionPlugin();
```

3. Add webpack [DefinePlugin](http://webpack.github.io/docs/list-of-plugins.html#defineplugin) in your plugins array.

```
const plugins = [.....new webpack.DefinePlugin({APP_VERSION_INFO: {  VERSION: gitRevisionPlugin.version(), //returns the output of git- describe command  COMMITHASH: gitRevisionPlugin.commithash(), // returns last commit hash  BRANCH: gitRevisionPlugin.branch() // returns the branch name from which the build was run};})...]
```

4. Now use `APP_VERSION_INFO` anywhere inside your app as it will be globally available.

```
console.log('Check App Version ', APP_VERSION_INFO);
```

**_Did you like this story?_**  
_Recommend (by clicking the ❤ button) or share this story so other people can read it!_

