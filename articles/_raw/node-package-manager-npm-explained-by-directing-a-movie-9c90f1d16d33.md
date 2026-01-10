---
title: Node Package Manager (NPM) explained by directing a movie
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-24T01:45:53.000Z'
originalURL: https://freecodecamp.org/news/node-package-manager-npm-explained-by-directing-a-movie-9c90f1d16d33
coverImage: https://cdn-media-1.freecodecamp.org/images/1*4Sqqu9cwZB7zXj00ULQ5Eg.jpeg
tags:
- name: education
  slug: education
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Kevin Kononenko

  If you understand the general way that Hollywood movies are made, then you can understand
  Node Package Manager (NPM).

  Did you know that the initial version of Node.js was written by just one programmer,
  Ryan Dahl, in 2009?

  Today, i...'
---

By Kevin Kononenko

**If you understand the general way that Hollywood movies are made, then you can understand Node Package Manager (NPM).**

Did you know that the initial version of Node.js was written by just one programmer, Ryan Dahl, in 2009?

Today, in 2018, millions of developers have used Node.js to create the back-end for their web applications. But, Node has relied on an active open-source community to build out many specialized packages within the Node Package Manager, or NPM.

There are two reasons why Ryan Dahl did not develop all of these specialized functions himself:

1. Developers would not want to use a massive, clunky framework that was written to cover hundreds of use cases.
2. It would take too damn long to create all the specialized packages yourself.

Instead, Ryan knew that if Node grew in popularity, developers would be willing to contribute. So, he launched NPM in 2010 to organize all these packages created by the community.

However, as a beginner web developer, it can be challenging to understand this whole ecosystem, and how to access it on your local computer.

After thinking on it for awhile, I realized that using NPM is kind of like being the director of a Hollywood movie. It’s your job to juggle a bunch of people (or packages) with specialized functions without making everyone crazy (or making it impossible to build your app).

![Image](https://www.freecodecamp.org/news/content/images/2020/04/0_h-Af2amJ-W_85YYY.jpeg)

So here’s the full guide to NPM. In order to understand this tutorial, you just need to know the [difference between front-end v. backend](https://blog.codeanalogies.com/2018/04/07/front-end-v-back-end-explained-by-waiting-tables-at-a-restaurant/).

# What Is NPM?

Imagine that you are the director of a new Hollywood movie. After accepting the role, you immediately need to begin hiring actors and other executives to create the movie alongside you.

Of course, that brings the immediate question: which actors/actresses will you hire? How will you make sure that they can all work together? How will you fit it within budget?

Or, will you go in a completely different direction, and try to build the perfect team from scratch with relatively unknown actors?

If you want to hire out a team, you will need to look at some sort of directory to find the right people. I don’t know if Hollywood has some sort of internal directory, but [IMDB](http://imdb.com/) is one that comes to mind. Or, in the days, before the Internet, there was probably even a physical directory.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/0_OfNzoFOA9Scop-hQ.png)

Just like IMDB has information on thousands of actors that you can use to make a hiring decision, NPM has hundreds of thousands of “packages” that offer specialized functions. They are all written in JavaScript, so TECHNICALLY you could rewrite them… but that is not the point. They are meant to make your life easier by making new functionality instantly available.

It’s just like hiring a known actor/actress — that person is a specialist in certain types of roles due to past experience.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/0_gYvhN0Ws1rlLL6uo.jpeg)

_We all know Liam Neeson’s specialty…_

So, as a developer, you access the NPM registry to add specific packages to your web app, which should make your life easier. And just like all actors/actresses have built their own careers, all NPM packages have been built by individual developers or teams and contributed to the registry.

Within your code, all of these packages are tracked in the package.json file. So, that file is kind of like the list of people that are involved in the movie. Here is an example of that list:

![Image](https://www.freecodecamp.org/news/content/images/2020/04/0_94FQCRZXv3NGz2W8.png)

We will cover the versions later in this tutorial.

# Packages Explained

Let’s imagine that your movie has 100 roles that need to be filled. If you had an unlimited budget, would you want to fill all those roles with famous actors/actresses that had played similar roles in the past?

Probably not.

Everyone would want to be the star of the show and bend the rules to fit their character. It would be a nightmare. But, if you only hire unknown actors, it is going to be pretty tough to make an excellent movie!

It takes years of experience to become a great actor, after all.

Similarly, when you are building a web app, you are constantly faced with a choice — can I build this functionality myself, or should I use a package to accomplish the task?

Do you know the movie “[Super Troopers](https://en.wikipedia.org/wiki/Super_Troopers)“? It’s a comedy classic, and the budget was just $3 million dollars. However, most excellent movies cost $10–100 million dollars. You can build an incredible web app from scratch, but you probably want to use packages.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/0_H1HOGMdz6Swfae3H.jpeg)

Let’s say that you are hiring Mark Wahlberg, a famous American actor, for your movie. When Mark joins your movie, it is not just him. He has a team of people that support him and make him successful. A chef, a trainer, an agent.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/0_si4-ybeeHo_o6Sx1.png)

Similarly, each individual package does not operate independently. The package authors used other NPM packages to make their lives easier too. In fact, their package will share some dependencies with other packages, just like Mark Wahlberg might share a private chef with other actors and actresses.

Here’s the list of dependencies for [request](https://www.npmjs.com/package/request), a popular package:

![Image](https://www.freecodecamp.org/news/content/images/2020/04/0_aX2XcgXqhvH898m5.png)

So let’s return to our package.json example from above:

![Image](https://www.freecodecamp.org/news/content/images/2020/04/0_yzyTg-PLBa-Dyxsa.png)

When you add the “_axios_” package to your app, you are not just adding the axios file. You are also adding any dependencies that the _axios_ file will need, if you had not previously added them with another package. Those are not explicitly stated, but you can always find them within the _node_modules_ folder.

This is one of the benefits of npm. When you add a new package, you don’t even need to check if you are already using all the necessary packages that support the package that you are using. npm will automatically add the new ones to your directory.

# Versions Explained

Do you see the three sets of numbers next to each package above? That’s the **version number**. Since developers are constantly updating their packages, you can choose to use a specific version of a package, or automatically use the latest version.

So, when you are using 40 different packages in your project, and they are all constantly shifting, you may find that compatibility issues arise. For example, when ReactJS releases its newest version, your app may no longer function as you would expect. That’s where testing comes into play, but that’s the subject of another tutorial.

Think of it as actors/actresses at different stages of their career. Some may play similar roles throughout their career, while others may change drastically.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/0_JZullYOFh6dTh7hd.jpeg)

_Young vs. old Clint Eastwood_

# Using the Command Line

When you download Node and NPM to your local machine, you can instantly use a variety of commands to work with the NPM directory. One common one is:

_npm install_

If you want to install the _express_ package, you would type in the command line:

_npm install express_

Then, NPM would download the express code and its dependencies to your local computer. That’s kind of like the act of hiring a new actor. Or —

_npm uninstall express_

That’s like “firing” the express package from your app.

You can add new commands in the “scripts” section of your package.json file. One common one is “start”, which means “start running the node server”. It looks like this:

![Image](https://www.freecodecamp.org/news/content/images/2020/04/0_Z9ZoMm3vSFGk-Mud.png)

Kind of like a director yelling “Action!”

# Dependencies Explained

So far, we have only briefly touched on the concept of dependencies. Your app will likely have a couple packages that only run on the local version, like testing and transpiling tools. In other words, you should have a couple tools that you only use in your local environment, and not on the production version.

If you need a refresher on the difference between localhost and production, [check out this guide](https://blog.codeanalogies.com/2018/02/02/localhost-explained-by-trying-to-start-a-microbrewery/).

Think about all the time and energy that goes into making a movie. Only a small fraction of it occurs on the official set with the cameras rolling. Behind the scenes, there are hours of work on memorizing lines, lifting weights in the gym and learning new accents. To make the team more effective, the director might hire specialized coaches for each one of these functions.

So, when we look at all the packages being used by a Node app, we can actually divide it up into two categories:

1. Packages used in both production and local
2. Packages just used locally

![Image](https://www.freecodecamp.org/news/content/images/2020/04/0__kdSnu3_r0xpRRtu.png)

[Grunt](https://gruntjs.com/) is a task runner that automates repetitive commands on the command line. [Nodemon](https://github.com/remy/nodemon) automatically restarts your server upon any changes in your server code.

In your package.json file, these are separated into two sections: dependencies and devDependencies. Here is what that looks like:

![Image](https://www.freecodecamp.org/news/content/images/2020/04/0_tu-qbY_hG7z-qKzl.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/04/0_z4Y9LhCYX96HPGYL.png)

