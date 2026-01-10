---
title: Let’s fix the good old command line
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-15T20:02:01.000Z'
originalURL: https://freecodecamp.org/news/lets-fix-the-good-old-command-line-b6eaa1f9c040
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0ClHN36X6976f6SnpcId6w.jpeg
tags:
- name: api
  slug: api
- name: command line
  slug: command-line
- name: Developer Tools
  slug: developer-tools
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Manuel Vila

  Although we have beautiful graphical user interfaces, it seems that we are using
  more and more command-line tools. And while many of them are really good, I think
  they could be even better if they were based on more modern foundations....'
---

By Manuel Vila

Although we have beautiful graphical user interfaces, it seems that we are using more and more command-line tools. And while many of them are really good, I think they could be even better if they were based on more modern foundations.

To show the issue, I will consider two essential characteristics: customizability and usability. And, by looking at some of the more popular tools, I will show how difficult it is to achieve both characteristics at the same time.

I’m going to talk mainly about JavaScript tools, because it’s the environment I’m the most comfortable with. But the problem is similar regardless of the development environment.

### Create React App

[Create React App](https://github.com/facebook/create-react-app) illustrates the case of a tool that is very easy to use but not very customizable. It brings together a set of tools, techniques, and best practices to start a modern web app in no time.

In this respect, it is extremely valuable, but it is implemented like a black box. It’s hard to change something inside. Yes, there is an `eject` feature, but I don’t think this is a real solution. It’s trading one characteristic for another. The tool becomes more customizable but is no longer easy to use.

### npm scripts and specific code

Here, we have the greatest level of customizability, but usability is low. By writing [npm scripts](https://medium.freecodecamp.org/introduction-to-npm-scripts-1dbb2ae01633) and specific code, it is possible to create any kind of builders, deployers, etc. But, this is not for everyone, and it’s a pretty laborious task. Putting together a set of tools using npm scripts (i.e., [Bash](https://www.gnu.org/software/bash/)) is not quite user-friendly, and writing code in JavaScript to configure and control tools through npm modules is somewhat cumbersome.

### [webpack](https://webpack.js.org/), [gulp](https://gulpjs.com/), [Serverless Framework](https://serverless.com/framework/), etc.

Finally, here are some tools that are both quite customizable and easy to use. But, the price to pay is high. We have to deal with their plugin system, or, rather, the fact that there is such a system.

The problem is that each time a tool offers a plugin system, it creates a new ecosystem. The result is that instead of having a global ecosystem of tools, we end up with a proliferation of ecosystems that operate in silos. So, many plugins are doing the same thing but for different ecosystems (e.g., `[awesome-typescript-loader](https://github.com/s-panferov/awesome-typescript-loader)`, `[gulp-typescript](https://github.com/ivogabe/gulp-typescript)`, `[serverless-plugin-typescript](https://github.com/graphcool/serverless-plugin-typescript)`, etc.). What a waste of time.

Very often, when a tool implements a plugin system, it is an indicator that something is going wrong. It is trying to solve a problem that should probably be addressed at a lower level.

![Image](https://cdn-media-1.freecodecamp.org/images/bknkJrgYXw8sDcmt4QdpnNeRsPTm5Rq078t0)

### *nix, Bash, etc.

Don’t get me wrong. All the tools I mentioned earlier are fantastic. Given the foundations on which they are based, they are doing great. I mean they have to struggle with Unix-like systems and shells such as [Bash](https://www.gnu.org/software/bash/). Can you believe that all our modern tools are based on foundations that have barely changed in nearly half a century?

Typically, when we work on a project, we use several tools such as (in the case of a modern web project), a dependency manager, a transpiler, a bundler, and so on. So we need a way to install, configure, and compose all these things. Unfortunately, our good old command line is not very good at this.

We use configuration files based on many different formats to configure our tools. We communicate with them through an array of strings (`argv`). To compose them, there is, well, Bash… Finally, since typical shells can’t handle several versions of the same tool, managing our development environment is painful when we have to deal with many projects.

Seriously, we cannot say that it’s user-friendly. Sure, we have great programming languages and rich libraries. The tools are beautiful inside, but outside, they are ugly. When it comes to configuring, composing and executing them, it’s not cool, and because of that, we end up with the customizability-usability dilemma.

### Hello, “resources”

I worked full time for a year trying to solve this problem, and I ended up with what I call a “[resource](https://run.tools/docs/introduction/what-is-a-resource)”. Also, as a proof of concept, I built “[Run](https://run.tools/),” a resource runtime.

So, what’s a resource for? Basically, a resource adds an object-oriented interface to the tools, making them easier to use both from the command line and, programmatically, from other tools.

If you create a tool, you can wrap it into a resource to improve its usability and save a lot of development time. First, since Run installs tools automatically, the installation problem disappears. Then, given that users configure tools using resources, you don’t need to manage configuration files. Finally, you no longer need to implement a command-line interface. Run provides it for you.

If you are an end developer, and you are working on an application, website, backend, and so on, you can use a resource to reference the tools your project needs, and specify their configuration. Then, since your development environment is defined in a single file, your project is super easy to transport and share. Just grab the resource and you are all set. Also, since your resource consumes tools that are themselves resources, everything becomes extremely easy to configure, compose, and use.

### What does it look like?

A resource is a JSON or YAML document allowing you to specify the following:

* The tools that the resource consumes (by inheriting or composing them)
* A set of attributes (to configure the tools)
* A set of methods (to add custom behaviors)

For example, to build a website, you can start with something like this:

```
{  "@import": "aws/s3-hosted-website#^0.1.0"}
```

Then, by invoking Run without any argument:

```
run
```

You get an auto-generated help reflecting the content of your resource:

![Image](https://cdn-media-1.freecodecamp.org/images/f1pzp0tOzgb4CAuXr60GlBWOg9wo3FJ-uTED)

Because the resource imports `"aws/s3-hosted-website"`, it inherits a number of attributes and methods. Let’s specify some attributes:

```
{  "@import": "aws/s3-hosted-website#^0.1.0",  "domainName": "www.example.com",  "contentDirectory": "./content"}
```

Finally, let’s invoke the `deploy` method:

```
run deploy
```

Voila! Your website is online. What about this `"aws/s3-hosted-website#^0.1.0"` thing? This is a reference to a resource that implements a tool for managing static websites hosted on AWS. And, to make it easier to use, it is stored in a [resource directory](https://resdir.com/).

I have played with resources pretty intensely for months, and really, it seems that the customizability-usability dilemma is solved. For example, here is a resource for a more realistic website including npm dependencies (without `package.json` file!) and a `build` method that runs a transpiler, a bundler, and a file copier:

```
{  "@import": ["aws/s3-hosted-website#^0.1.0", "js/resource#^0.1.0"],  "domainName": "www.example.com",  "contentDirectory": "./build",  "dependencies": {    "color": "^3.0.0",    "lodash": "^4.17.4"  },  "build": {    "@type": "method",    "@run": ["transpiler run", "bundler run", "copier run"]  },  "transpiler": {    "@import": "js/transpiler#^0.1.0",    "source": "./src",    "destination": "./dist",    "targets": {"chrome": "41", "safari": "10", "firefox": "50"},    "format": "esm"  },  "bundler": {    "@import": "js/bundler#^0.1.0",    "entry": "./dist/index.js",    "output": "./build/bundle.js",    "target": "browser",    "format": "iife"  },  "copier": {    "@import": "tool/file-copier#^0.1.0",    "sourceDirectory": "./",    "destinationDirectory": "./build",    "files": ["./index.html", "./images"]  }}
```

Pretty easy, don’t you think? If you are lost, Run’s auto-generated help is your guide. For example, to find out more about the bundler, just invoke:

```
run bundler
```

You should see something like this:

![Image](https://cdn-media-1.freecodecamp.org/images/LHZGwRocjigwamqLwwv7RiJFLpA618ONAv1v)

### Conclusion

I’m not saying that the resource concept is the Holy Grail, but it’s the best I have found so far, and it’s a work in progress. Specifications are not stable yet; everything can change, even the denomination “resource” can change.

To find out more about the current state of Run and resources, you can have a look at the [documentation](https://run.tools/docs) and the [GitHub repo](https://github.com/runtools/run).

So, what do you guys think? Is it just me having a problem with the command line? Or is it something that needs to be fixed? And if so, do you believe this resource concept is a step in the right direction?

