---
title: 5 npm Tips and Tricks to Help You Boost Your Productivity
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-29T14:05:16.000Z'
originalURL: https://freecodecamp.org/news/5-npm-tips-and-tricks
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/Being-Agile-Kanban-VS-Scrum--4-.png
tags:
- name: npm
  slug: npm
- name: Productivity
  slug: productivity
seo_title: null
seo_desc: 'By Niall Maher

  While this article will likely boost your productivity, at the very least it will
  also impress some of your colleagues with your new skills. People will now perceive
  you as smarter and potentially more interesting. ?

  I''ve kept away fro...'
---

By Niall Maher

While this article will likely boost your productivity, at the very least it will also impress some of your colleagues with your new skills. People will now perceive you as smarter and potentially more interesting. ?

I've kept away from the obvious shortcuts and tried to share information you probably don't know.

If you want the video version check it out below. If you are happy reading, then scroll on my friend... ?

%[https://youtu.be/EVT39ggmoM8]

## 1. List available scripts

To easily check all the available scripts in a project just run:  


```
npm run

```

This gives you a lovely output showing you the commands like this:

![npm run output](https://res.cloudinary.com/practicaldev/image/fetch/s--_LPtQBgD--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.imgur.com/HMIzHx7.png)

## 2. List installed packages

```
npm list

```

This shows us probably too much because we see the dependencies of our dependencies…  


![npm list output](https://res.cloudinary.com/practicaldev/image/fetch/s--kz7Rq87p--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.imgur.com/axrlVAi.png)

Use the `--depth` to limit the depth of your search

```
npm list --depth=0

```

And here you can see the output when you limit the depth:

![npm list --depth=0 output](https://res.cloudinary.com/practicaldev/image/fetch/s--u3jK9MGv--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.imgur.com/oS5z6Lw.png)

## 3. Open a package's homepage or repo

I really like this feature because you can quickly get the documentation for the packages.

To automatically open the packages homepage you can run:

```
npm home PACKAGE_NAME 

```

To open the repository you can just run:

```
npm repo PACKAGE_NAME 

```

This is super handy so you don't have to go Googling looking for the docs or npm pages and can quickly access the information you need on packages you don't know.

## 4. Show all the available versions for a package

To get the latest version of a package we can run:

```
npm v react version

```

![npm v react version output](https://res.cloudinary.com/practicaldev/image/fetch/s--iRvAhOEz--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.imgur.com/UsPEWEl.png)

Or for all the versions we just have to make "version" plural.

```
npm v react versions

```

We then get a lovely output of all the available versions which is super handy if you want to check what's new/old or if there are any alpha releases to try out.

Here's a piece of the output from running `npm v react versions`:

![npm v react versions output](https://res.cloudinary.com/practicaldev/image/fetch/s--PcoUrUC---/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.imgur.com/bFY7uNf.png)

## 5. Look for outdated packages

The `outdated` command will check the npm registry to see if any of your packages are outdated. It will print out a little table in your command line showing the current version, the wanted version, and the latest version.

```
npm outdated

```

If you see the packages in red like in my sample it means there are some major vulnerabilities and they should be updated. As you can see in this 4-year-old project it's all a nice healthy red...

![npm outdated output on an old project](https://res.cloudinary.com/practicaldev/image/fetch/s--6WBx9bX3--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.imgur.com/uwZUxfO.jpg)

If you want versions different than your current version you can actually run `npm update` to safely update these packages.

I think a better way for updating and checking for outdated stuff is actually running the `npm audit` command, as it gives a lot more detail. I didn't include it as a tip because it's always screaming at us to run it in the console when we install dependencies.

## Visual Studio Code Bonus Tip! ?

A lot of people don't know this but you can actually run your scripts directly from inside Visual Studio Code with their lovely interface.

Look for the "NPM Scripts" on the bottom left of your panel.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/TiTJeqh.png)
_[Showing the npm scripts tab in Visual Studio Code](https://i.imgur.com/TiTJeqh.png)_

You can open your scripts from here and just press the play icon to kick it off. I like this because it's a clear and easy way to do things for people that might not be too familiar with _npm_.

If you can't see this make sure it's active in your settings. ?

---

[Follow me on Twitter](https://twitter.com/nialljoemaher)

Subscribe on [Codú Community](https://www.youtube.com/c/Cod%C3%BACommunity)

