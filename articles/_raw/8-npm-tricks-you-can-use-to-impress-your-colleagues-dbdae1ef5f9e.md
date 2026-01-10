---
title: 8 npm Tricks You Can Use to Impress Your Colleagues
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-05-13T18:43:08.000Z'
originalURL: https://freecodecamp.org/news/8-npm-tricks-you-can-use-to-impress-your-colleagues-dbdae1ef5f9e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*r04YgvldF8rsv-sfttkvnA.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Adir Amsalem

  You watch a colleague coding, there’s a shorthand or trick being applied, somehow
  you’re not familiar with it and your mind blows away. Happens to all of us all the
  time.

  In this short post we will unveil some very useful npm tricks. ...'
---

By Adir Amsalem

You watch a colleague coding, there’s a shorthand or trick being applied, somehow you’re not familiar with it and your mind blows away. Happens to all of us all the time.

In this short post we will unveil some very useful npm tricks. There are many more than what we can cover here, so I chose to focus on those that are most relevant and useful for our day-to-day workflow as developers.

### Basic shorthands before we’re getting started

To get everyone aligned, especially the newcomers among us, let’s have a quick overview of the basic shorthands and make sure nobody miss anything trivial.

#### Installing a package:

Regular: `npm install pkg`, Shorthand: `npm i pkg`.

#### Installing a package globally:

Regular: `npm i --global pkg`, Shorthand: `npm i -g pkg`.

#### Installing a package and save it as a dependency:

Regular: `npm i --save pkg`, Shorthand: `npm i -S pkg`.

#### Installing a package and save it as a devDependency:

Regular: `npm i --save-dev pkg`, Shorthand: `npm i -D pkg`.

For additional shorthands read npm’s own [shorthand list](https://docs.npmjs.com/misc/config#shorthands-and-other-cli-niceties).

Let’s begin with the interesting stuff now.

#### 1. Initializing a new package

We all know `npm init`, it’s the first thing we do when creating a new package.

![Image](https://cdn-media-1.freecodecamp.org/images/8atnoWYLUL7DJoL1Y6MPQKHGjtxLTMlWHE2Q)

But, all those questions are quite annoying and we gonna modify it anyway, so why not just avoid it?

`npm init -y` and `npm init -f` to the rescue!

![Image](https://cdn-media-1.freecodecamp.org/images/PW1ehHF7TJY5445PiIzqKH17I1VEAAqbAffA)

#### 2. Running tests

Another command we all use is `npm test`. Most of us use it every day, several times a day.

![Image](https://cdn-media-1.freecodecamp.org/images/223EOKMiVqraBkOZaldXI3ZkrT20LPGkmyOj)

What if I told you that you can do the same with ~40% less characters? We use it so much, so it’s a nice win.

Fortunately, there’s `npm t`, which does exactly that!

![Image](https://cdn-media-1.freecodecamp.org/images/qBoBUCbrrSUwXqmgkobS8RSWo7DBikcSd8TN)

#### 3. List available scripts

We get to a new project and we wonder how to get started. We usually ask ourselves things like: how do we run it? which scripts are available?

One way to discover is to open the package.json file and check the `scripts` section.

![Image](https://cdn-media-1.freecodecamp.org/images/yeCx6ROfgZnv7DfJ-NQnYDvEsUPLODGWbHQ2)

We can do better of course, so we simply run `npm run` and get a list of all the available scripts.

![Image](https://cdn-media-1.freecodecamp.org/images/AW6DbH7UEeZu5bDIhBTMpWDZtzNsVZqEghGj)

Additional option is to install `ntl` (`npm i -g ntl`), and then run `ntl` in the project’s folder. It also allows to run the scripts, which makes it very convenient.

![Image](https://cdn-media-1.freecodecamp.org/images/pxg3xuyZ-EfD4j3yPpgYLH77haLQ7Dya-X4a)

#### 4. List installed packages

Similar to available scripts, sometimes we ask ourselves which dependencies we have in our project.

We can once again open the package.json file and check, but we already know we can do better.

Meet `npm ls --depth 0`.

![Image](https://cdn-media-1.freecodecamp.org/images/uplcv8ZLtwCPnCFTDIF4JmiTDAqys-d0GgRw)

To list the globally-installed packages, we can run the same with `-g` flag, `npm ls -g --depth 0`.

![Image](https://cdn-media-1.freecodecamp.org/images/32Rx5M4pyEtYxh6qy-EmoVUIAg0Yua2coV5W)

#### 5. Running locally-installed executables

We installed a package in our project, it comes with an executable, but it only works when we run it via an npm script. Did you wonder why, or how to overcome it?

First, let’s understand why — when we execute commands in our terminal, what actually happens is that it looks for an executable with the same name in all the paths that are listed in our `PATH` environment variable. That’s how they’re magically available from anywhere. Locally-installed packages register their executables locally, so they aren’t listed in our `PATH` and won’t be found.

How does it works when we run those executables via an npm script you ask? Good question! It’s because when running this way, npm does a little trick and adds an additional folder to our `PATH`, `<project-directory>/node_module`s/.bin.

You can see it by running `npm run env | grep "$PATH"`. You can also run just `npm run env` to see all the available environment variables, npm adds some more interesting stuff.

`node_modules/.bin`, if you wondered, is exactly where locally-installed packages place their executables.

Let’s run `./node_modules/.bin/mocha` in our project’s directory to see it in action.

![Image](https://cdn-media-1.freecodecamp.org/images/qwmAkkWrBqyDvqeEH0vy2-AIFRFf1YZ7rTSF)

Simple, right? Just run `./node_modules/.bin/<comma`nd> whenever you want to run a locally-installed executable.

#### 6. Find your package on the internet

You might came across the `repository` entry in the package.json file and wondered: “What is it good for?”.

To answer it, simply run `npm repo` and watch it open in your browser .

Same applies, by the way, for the `npm home` command and the `homepage` entry.

If you want to open your package page on [npmjs.com](https://www.npmjs.com/), there’s a nice shorthand for that as well, `npm docs`.

#### 7. Run scripts before and after other scripts

You’re probably familiar with scripts such as `pretest`, which allows you to define code that would run before the `test` script.

What you might be surprised to find out, is that you can have pre and post scripts for every script, including your own custom scripts!

![Image](https://cdn-media-1.freecodecamp.org/images/ei1rVwDYYd1qlgXsAlSK95Yb0BmYzCka9XMt)

It’s very useful for projects in which you use npm as your build tool and have many scripts you need to orchestrate.

#### 8. Bumping package’s version

You have a package, you use [semver](http://semver.org/) for versioning, and you need to bump the version before a new release.

One way to do this is to open the package.json file and change the version manually, but we’re not here for that.

An easier way is to run `npm version` with `major`, `minor` or `patch`.

![Image](https://cdn-media-1.freecodecamp.org/images/OS51ylDy5REYLrs0nhP6l7oKb-1DOKUGuyAu)

That’s all for now.

I hope you learned something new and found at least one of those tricks useful for your day-to-day workflow, and ideally you also know npm better now and have some new ideas for how you can utilize it better in your job.

Impressing your colleagues is great, but constantly learning new things and being more professional is even better!

If you know additional useful tricks, please share them in the comments!

