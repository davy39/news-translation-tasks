---
title: What Music Can Teach Us About The Way We Share Code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-19T19:04:36.000Z'
originalURL: https://freecodecamp.org/news/what-music-can-teach-us-about-the-way-we-share-code-a69c30ebded8
coverImage: https://cdn-media-1.freecodecamp.org/images/1*viBEEx_KTOQfLsV63PJM9w.png
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Jonathan Saring

  Not that long ago, many of us were carrying a suspicious-looking suitcase in the
  back of our cars, or had one hidden under our beds. Some of us had Ikea-made towers
  with multiple storage spaces standing proud in our living rooms. I...'
---

By Jonathan Saring

Not that long ago, many of us were carrying a suspicious-looking suitcase in the back of our cars, or had one hidden under our beds. Some of us had Ikea-made towers with multiple storage spaces standing proud in our living rooms. In both cases, this was the result of our impressive music CD-Roms collection. Today, chances are they are nostalgically stored in our garage.

After a short reign, music CD-Roms were replaced by iTunes and YouTube, with MP3 players in between. This revolution happened mainly because of 5 major disadvantages CDs had from day one:

1. They were cumbersome to use, carry and handle.
2. They took too much effort to purchase/create.
3. They were very hard to change and modify. Nobody really wanted to burn a new CD whenever a new Bieber song came out (don’t judge me).
4. They forced us to carry a bunch of songs we don’t listen to and zap through them just to listen to a single song we really wanted to listen to.
5. Who remembered which songs were on which CD? 90% of my burned CDs contained the same 10 songs anyways.

Surprisingly, this isn’t all that different from the way we share code today, between projects and between people. Let’s see how.

### How on earth is that like sharing code?

![Image](https://cdn-media-1.freecodecamp.org/images/u740J5qArBLMtR08Bqlo-0Sl6m8E-xwV4WfQ)
_“I usually just like to listen to my light-saber swooshing back and forth…”_

Modularity has always been the holy grail of software development, and the key to better reusability, maintainability and testability.

Every day, more of the applications we build are designed with greater modularity through smaller components of code. Reusable functionalities, UI and Web components (such as React, Vue and Angular), Node.js modules, GraphQL APIs and even serverless functions are our building blocks.

Now let’s be honest — who knows exactly which reusable components were written in their codebase, organizes them, and shares them between their projects at scale? I know I didn’t. Then, I started asking myself why not.

Let me show you. Here is a [React movie application](https://github.com/teambit/movie-app) hosted on GitHub. As you can see, it contains a total of 49 files and 14 directories. One of these directories is the `components` sub-directory. Inside that sub-directory there are 8 reusable React components (such as `hero` and `navigation`).

```
├── src
```

```
│   ├── App.js
```

```
│   ├── App.scss
```

```
│   ├── App.test.js
```

```
│   ├── components
```

```
│   │   ├── hero
```

```
│   │   ├── hero-button
```

```
│   │   ├── item
```

```
│   │   ├── list-toggle
```

```
│   │   ├── logo
```

```
│   │   ├── navigation
```

```
│   │   ├── title-list
```

```
│   │   └── user-profile
```

```
│   ├── favicon.ico
```

```
│   ├── global.css
```

```
│   └── index.js
```

```
└── yarn.lock
```

Let’s say I have another React application, and I want to use my `hero` component in that different app as well, and also make it discoverable for my team to use in their projects and easily change it to suit their needs.

Copy-pasting code is a [very bad idea](https://stackoverflow.com/questions/4226284/how-to-convince-a-colleague-that-code-duplication-is-bad). This might seem like the quick way to go about it, but it’s really not. Don’t do it.

As of today, I really have three options:

1. **Publish nine packages**: Create eight new repos, boilerplate, and publish nine packages and change both project’s source code to **require** them. When I’ll want to modify a component, I’ll have to work very hard to make changes from different repos. Now imagine having 500 of these.
2. **I can use [Lerna](https://github.com/lerna/lerna)** to keep multiple packages in a single repo, but it only works if I really want to go monorepo. Even then, I’ll have to restructure my project, configure each package separately, and define their dependency tress, and every change will still have to go through the original repository.
3. **Shared library**: Create a new repo, group the components together, create the configurations needed for such a project, publish it as a new library, and change both projects’ source code. Every app using this library will add redundant code, weight, and complexity. Every modification will require republishing the whole library, and go through the owner.

The thing is, packages are **great** for larger projects. For smaller components and modules, these solutions share some of the same problems as music CD-Roms: Serious overhead, changes are hard, and discoverability is lacking.

In a way, setting up 500 repos and packages to share smaller components reminds me of using a mini-disc player (not my best-spent $100): you can’t solve this problem by optimizing it. You have to innovate.

### So… iTunes for shared code?

Obviously, comparing shared libraries to CD-Roms isn’t very technically accurate. The complexity of sharing functionality between complicated environments and contexts is different from that of listening to Lady Gaga.

Still, sharing common code between projects really shouldn’t be this hard. What we can really learn from the way we share and consume music today is that effective sharing requires a **better** **experience:** reducing overhead, increasing discoverability, and going from static to dynamic.

### So, we decided to build it

Sometime early 2017 we had that exact dream. One of the best things about open source is that having an idea is a perfectly good enough reason to build it.

We decided to go ahead and build [Bit](https://bitsrc.io) — an [open source project](https://github.com/teambit/bit) designed to do for code sharing what iTunes did for music sharing — make it simple, dynamic and easily accessible for everyone. [Bit](https://bitsrc.io)’s idea is simple: Kill the overhead of sharing code.

#### How it works

![Image](https://cdn-media-1.freecodecamp.org/images/U9MYoGOV4yiSkk3XYYreYkXfWnM9qUEv6MzJ)

It was built to provide the fastest experience possible for “managed copy-pasting” and be 100% compatible with Git and NPM.

The key lies in Bit’s ability to separate the representation of shared code from your project’s file system, and its ability to track shared code across repos and projects whether it’s installed or actually sourced in these projects.

It breaks the overhead of sharing code by eliminating the need to split your repos or having to restructure your project and boilerplate multiple packages inside it.

Instead, you can simply point Bit to any part of your repo that you would like to share, let Bit automatically isolate it (including dependencies), and share it to a shared location called Scope from which it can be installed with NPM.

Since Bit is able to track actual source code between projects, you can also use it to import the code itself into any repository, change it, and let Bit sync changes across your projects for you.

When sharing, you can even `eject` the code back to being a package dependency for your project.

As a result, there is basically no overhead for sharing code and making it available with NPM, discoverability is increased, and maintenance becomes much simpler. Scopes even help [building](https://docs.bitsrc.io/docs/building-components.html) and testing your code so you don’t have to configure these environments for every package.

Here is how [Bit’s workflow](https://docs.bitsrc.io/) looks:

1. Install Bit and initialize it for your project.
2. Choose which components of code to track from your project and which [environments](https://docs.bitsrc.io/) to add for build and test processes.
3. Share them to a remote Scope were they are hosted, organized, and made available to install using your favorite package manager.
4. Easily import their code into any repo, change it as needed, and update your changes across your codebase.

Let’s see an example.

#### Back to React movie-app

Let’s go back to the [React movie-app](https://github.com/teambit/movie-app).

[Adding Bit](https://docs.bitsrc.io/) to the project enabled me to track and isolate the reusable components inside, without setting up new repositories or changing my project’s code. Then, I shared them to this [collection](https://bitsrc.io/bit/movie-app).

Sharing it took very little time and my project wasn’t changed at all. No new `package.json` files were created and I didn’t have to configure multiple environments or fight my dependency tree.

![Image](https://cdn-media-1.freecodecamp.org/images/gAxTcRwrApKKUG1uju8B-q5IjsYr81O9Y0p8)
_React components with Bit_

As you can see, every component is now available to my entire team to install with NPM or to import into their own projects for further modifications.

They can search for it, and view useful information — from live rendering to build and test results, auto-parsed docs and examples — so they can judge its usefulness.

Our entire team can now organize and share our common code components without having to work hard or reinvent the wheel every day.

After using it for over 10 months, and after now being used by additional teams and communities, I welcome you to join and use it for your projects.

You can see a video demo of this project [here](https://www.youtube.com/watch?v=vm_oOghNEYs).

### Back to the future

Up until a few years ago, we had to burn a new project for every song we wanted to listen to. We had to store and maintain multiple static CDs and drag along a bunch of stuff just to listen to a single song. We duplicated songs between CDs and had trouble discovering the songs we really wanted.

iTunes provided us with the dynamic experience that helped us compose and share playlists, easily find the songs we wanted, and quickly update our playlists. When I’m at a party, I can easily play my up-tempo summer playlist, or just as easily play my romantic songs to my cat to get her to go to sleep.

We can learn a whole lot from how music moved from CD-Roms to shared playlists. [Bit](https://bitsrc.io) aims to make code sharing and reuse simple and accessible for everyone just like iTunes did for shared music. It’s still a work in progress, and as such it still has a lot of room to grow and evolve. You are welcome to [try it](https://bitsrc.io) out, suggest [ideas](https://gitter.im/bit-src/Bit) and [feedbacks](https://github.com/teambit/bit/issues), and help us take that leap forward.

> “ The secret to efficiently building ‘large’ things is generally to avoid building them in the first place. Instead, compose your large thing out of smaller, more focused pieces… “

> - A. Osmani

