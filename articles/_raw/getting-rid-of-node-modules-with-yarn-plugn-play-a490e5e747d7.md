---
title: Getting rid of node_modules with Yarn Plug’n’Play
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-09T17:05:39.000Z'
originalURL: https://freecodecamp.org/news/getting-rid-of-node-modules-with-yarn-plugn-play-a490e5e747d7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*qYAlY8Iq5S4knk93upSneA.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: Productivity
  slug: productivity
- name: 'tech '
  slug: tech
- name: Yarn
  slug: yarn
seo_title: null
seo_desc: 'By Alcides Queiroz

  Reduce your install time up to 70%. Ask me how! ?


  Anyone who knows me can confirm that I’m a long-standing lover of JavaScript and
  its entire ecosystem. As a Front-end engineer, Node-based package managers have
  been a crucial part...'
---

By Alcides Queiroz

#### Reduce your install time up to 70%. Ask me how! ?

![Image](https://cdn-media-1.freecodecamp.org/images/F7mSgfClDgWzo8rkmxdF1mkiBw46HP5qbTRN)

Anyone who knows me can confirm that I’m a long-standing lover of JavaScript and its entire _ecosystem_. As a Front-end engineer, Node-based package managers have been a crucial part of my toolset since 2013.

First, I used Bower, which was primarily focused on the front-end world. Then, in 2015, I sadly (ok, _not really_) realized that Bower was dying and NPM, the default package manager for Node, was the way to go for the front-end too. It was strange for me, at first, to use NPM for other things than Node modules, but I got used to the idea and migrated seamlessly.

Finally, just one year later, Facebook gave us Yarn, a modern and blazing fast alternative to NPM. I loved it at first sight! **But some things were still problematic…**

### Inherited problems in Yarn

Besides the speed, Yarn brought a number of advantages when compared to the NPM version at the time, such as lock files, offline mode, network resilience, checksums and others. Nevertheless, Yarn borrowed some known problems from NPM:

#### node_modules here, there, everywhere

For each project on your machine that uses NPM or Yarn, a `node_modules` folder is created. It doesn't matter if 10 projects use the exact same version of a given module, it will be copied over and over into each `node_modules` folder of these projects.

#### Generating a new node_modules folder takes a really long time

Even taking a great leap forward in terms of installation speed, Yarn was constrained by node_modules limitations. Just creating the node_modules folder takes up to 70% of the time needed to run `yarn install` (with a warm cache). **It's a huge amount of files to be created on every installation.** So, don't blame it on Yarn.

#### Dependencies not added to package.json

Here’s a scenario for you: Your app works perfectly in development, but crashes in production. After hours of investigation, you finally realize that you forgot to add a dependency to your `package.json`. **Yes, it can happen.**

#### Slow module resolution at runtime

The boot time of your app is heavily impacted by the way Node resolves dependencies. It wastes time querying the file system to discover where a given dependency will be resolved from.

### Yarn Plug’n’Play to the rescue!

All of the above problems were addressed by the Yarn team with the release of the Plug’n’Play feature last September.

When you enable PnP, instead of copying every needed file from the cache to the `node_modules` folder, here's what Yarn does:

1. It creates a single file with static resolution tables. These tables will contain a bunch of important info, such as: packages available in the dependency tree, how they relate between themselves and their location on the disk.
2. A special resolver is used in order to help Node discovering where each dependency has been installed (under the Yarn cache folder). It solely relies on the resolution tables which were created previously. As these tables contain information about the entire dependency tree, the node_modules resolution process won’t need to make a lot of `stat` and `readdir` calls at runtime anymore, significantly reducing your app boot time. And as Yarn knows all of your dependencies, it will complain if you try to import a module that's not present in your `package.json`:

![Image](https://cdn-media-1.freecodecamp.org/images/08nON5DmVDa9ITAs2nhTlNoRqNug1C-pC1Zs)

### Using Yarn Plug’n’Play

Converting a project to make use of PnP is easy as 1–2–3. You just need to add a `installConfig` section to your `package.json`, with a `pnp` key set to `true`, like this one:

```
{    "installConfig": {     "pnp": true   }}
```

> **Note:** You need Yarn v1.12+ in order to use Plug’n’Play.

After that, just run `yarn install` and everything inside your `node_modules` folder will be deleted. From now on, every dependency will be resolved directly from Yarn's hot cache.

![Image](https://cdn-media-1.freecodecamp.org/images/PD4zmILDWgikOs6RcNxXQnmtKE8YPiu9oFwN)
_“yarn install” clears your node_modules folder when PnP is enable_

#### Using PnP in a new React project with create-react-app

If you use create-react-app 2+, the good news is that it works great with Yarn Plug’n’Play! Just append the `--use-pnp` option to the `create-react-app` command and you're good to go:

```
npx create-react-app your-app-name --use-pnp
```

![Image](https://cdn-media-1.freecodecamp.org/images/Q1KEkqQk4isuWAQUSB-kXGTIdOwZRW9oW7Qw)

#### Possible issues

As nothing is perfect in the world, PnP may incur new issues when used in projects relying on a custom install logic. If you need more info about these potential new issues, [you can find a detailed explanation in this paper](https://github.com/yarnpkg/rfcs/files/2378943/Plugnplay.pdf).

### Conclusion

Plug’n’Play solves some really annoying problems in Yarn. Besides, it dramatically improves dependency caching on CIs, saving installation time and allowing our builds to get right to the point: **running the tests!**

And that’s it! Have fun with Yarn PnP.

