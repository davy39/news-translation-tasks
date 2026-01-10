---
title: Announcing Matterhorn ? a Node.js API Server Boilerplate
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-09T16:27:16.000Z'
originalURL: https://freecodecamp.org/news/announcing-matterhorn-a-node-js-api-server-boilerplate-4994759f1bf6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Gpo6knTSfsz0E9qjtCmBEQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: Productivity
  slug: productivity
- name: 'tech '
  slug: tech
- name: TypeScript
  slug: typescript
seo_title: null
seo_desc: 'By Ethan Arrowood

  Happy holidays developers ? Recently, I published Matterhorn ?, an API boilerplate
  project built with Node.js and TypeScript. The API server uses Fastify, a fast and
  low overhead web framework. The project comes with a configured ty...'
---

By Ethan Arrowood

Happy holidays developers ? Recently, I published M[atterhorn ?,](https://github.com/Ethan-Arrowood/matterhorn) an API boilerplate project built with Node.js and TypeScript. The API server uses Fastify, a fast and low overhead web framework. The project comes with a configured type system (TypeScript), test runner (Jest), linter (TSLint), and even a CI pipeline (Azure DevOps).

This article will give a brief overview of the project and insights into certain design decisions.

[**Ethan-Arrowood/matterhorn**](https://github.com/Ethan-Arrowood/matterhorn)  
[_An API boilerplate project built on Node.js and TypeScript ? - Ethan-Arrowood/matterhorng_ithub.com](https://github.com/Ethan-Arrowood/matterhorn)

### Overview

> ? Psst! This overview section is very similar to the project docs on G[itHub](https://github.com/Ethan-Arrowood/matterhorn#matterhorn-)

Get started quickly by following these steps:

1. ? Fork the repository
2. ?‍♀️ Clone it to your computer
3. ?‍♀️ Run n`pm run install && npm run dev`
4. ? Edit any of the files in s`rc/`
5. ? Watch as the app magically rebuilds and relaunches itself

✨ That’s it for the basic user guide. Now let’s dive into some of the commands available to you by default. All of the commands below can be run with `npm run <scri`pt> . This project makes use of npm mo`dul`es op`n and` rimraf to enable platform agnostic npm scripts.

* `build` — build the TypeScript files and output to `lib/`
* `build:watch` — automatically rebuild files if changes are detected in `src/`
* `clean` — recursively delete the `lib/` and `coverage/` directories
* `clean:build` — recursively delete the `lib/` directory
* `clean:coverage` — recursively delete the `coverage/` directory
* `coverage` — run the test suite and generate code coverage reports
* `coverage:open` — run `npm run coverage` then open the results in a browser
* `dev` — concurrently run `build:watch` and `start:watch`
* `lint` — run the linter configured by TSLint on the `src/` directory
* `start` — run the app from `lib/`. Make sure to use `npm run build` first!
* `start:watch` — relaunch the server if new changes are detected in `lib/`
* `test` — run unit tests defined in the `tests/` directory
* `test:ci` — run unit tests and generate necessary files for CI integration

#### Command Line Arguments & Environment Variables

Matterhorn implements example usage of both command line arguments and environment variables. It uses `yargs-parser` to manage command line arguments. Command line arguments are passed in through the start command: `node lib/index.js <command line argumen`ts>.

The`--log` argument has been enabled as an example. Running `npm run start` starts up the project without any command line arguments. This command is intended to be used in production, so logging is disabled by default (i.e. we don’t pass the `—-log` argument).

If you are using this command to test your code locally and want to see the logging output, then run `npm run start —- -—log`. This passes the command line argument through npm and into the aliased command.

Environment variables work in a similar way to command line arguments. They can be set in multiple ways depending on the terminal and operating system you are using. In a bash terminal you can specify environment variables as you use any of the above mentioned scripts by prepending the assignment to the command.

For example, this project has the `PORT` environment variable enabled. In a bash terminal run `PORT=8080 npm run start` to run the API on port 8080.

### Design Decisions

I built this project because I found myself constantly copying and pasting config files for new Node.js projects. I love what the `create-react-app` team has accomplished and envision Matterhorn developing into a similar kind of tool. Down the road, I look forward to developing a complete CLI to help developers get up and running with Node.js and TypeScript even quicker.

Matterhorn is an opinionated project. The build and linting systems are configured to my preferences, but are very easy to change. For example, in `tslint.json` I defined the `"semicolon"` rule as `false` — to enforce semicolon usage throughout the app, change this to `true` .

Additionally, this project contains an `azure-pipelines.yml` file. This defines the CI (continuous integration) pipeline on Azure DevOps, a robust tool offered by Microsoft to enable teams to plan smarter, collaborate better, and ship faster with a set of modern dev services. This was another opinionated decision due to my experience with the tool. There are many other great CI options such as Travis CI or Circle CI that I hope to support in the future.

### Hope you enjoy!

Thank you for taking the time to read this article and checking out Matterhorn ?. The project is open sourced, and I encourage developers of any skill level to come contribute. Check it out on G[itHub](https://github.com/Ethan-Arrowood/matterhorn) and if you want to hear about future updates as well as other things I develop follow me on T[witter.](https://twitter.com/ArrowoodTech)

Best wishes ? ~ Ethan Arrowood

