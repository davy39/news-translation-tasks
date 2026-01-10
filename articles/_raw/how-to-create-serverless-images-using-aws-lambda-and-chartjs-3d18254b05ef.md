---
title: How to create serverless images using AWS lambda and ChartJS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-19T21:40:57.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-serverless-images-using-aws-lambda-and-chartjs-3d18254b05ef
coverImage: https://cdn-media-1.freecodecamp.org/images/1*UrOibhQ3ePj0qPlEQLsrhg.png
tags:
- name: AWS
  slug: aws
- name: chartjs
  slug: chartjs
- name: charts
  slug: charts
- name: serverless
  slug: serverless
seo_title: null
seo_desc: 'By Martin van Vliet

  I’m working on a project to push sprint burndown information to distributed Scrum
  teams working in Slack. The entire application is serverless and running inside
  AWS. To generate burndown images I wanted to build a lambda function...'
---

By Martin van Vliet

I’m working on a [project to push sprint burndown information to distributed Scrum teams working in Slack](https://sprintlr.io). The entire application is serverless and running inside AWS. To generate burndown images I wanted to build a lambda function that creates an image, then pushes it to an S3 bucket. In this article, I’ll describe the solution I came up with.

First, the charting library. After investigating a number of options, I settled on the use of the [ChartJS library](http://www.chartjs.org/). It’s a great charting library in Javascript that can render all sorts of graphs using the HTML5 canvas. Very flexible and configurable, too. But how do I run it, headless, inside of a lambda?

My first attempt was to create a simple lambda on my MacBook using three NPM packages: **chart.js** and two other libraries: [**chartjs-node-canvas**](https://www.npmjs.com/package/chartjs-node-canvas) and [**canvas-prebuilt**](https://www.npmjs.com/package/canvas-prebuilt). The former is a wrapper around ChartJS that supports rendering charts in node. The latter is a prebuilt, native version of the HTML5 canvas that allows rendering a canvas headlessly without a browser. I built the lambda with the [serverless framework](https://serverless.com/), a very useful tool to create and deploy serverless applications.

Here’s my sample lambda:

My lambda generated a sample graph and all looked well when I ran it locally. On AWS, though, it failed. What gives?

As it turns out, ChartJS uses _native NPM modules_ to render directly to the canvas. Obviously, the native modules I use on my MacBook don’t run inside of a lambda. So what to do?

To run native modules inside a lambda, I needed to use the native libraries that the [lambda runtime environment](https://docs.aws.amazon.com/lambda/latest/dg/current-supported-versions.html) needs. So I fired up an instance of the lambda runtime AMI on EC2 and logged into it. There, I took the same lambda I built earlier and ran **npm install** on the EC2 instance. This downloads the native NPM libraries ChartJS needs but this time for the lambda runtime environment. With these libraries as part of the lambda function, ChartJS is able to render an image just as it normally would. Yay!

Contrary to normal NPM projects, I checked in the downloaded node modules into my git repository. When updating or building the graphing lambda, take care not to overwrite any of your dependencies. One side-effect of this approach is that I can no longer run the code on my local laptop to test.

Next up: store the image file generated in an S3 bucket. This was actually a fairly simple task with many code snippets available online to learn from. For completeness, here’s mine:

That’s it! Now you can generate images cheaply, on-demand!

Using native libraries is not without its problems though. I’ve had the entire setup work or fail depending on the exact version of **canvas-prebuilt** that I use. The current setup actually uses two. One transitive dependency via **chartjs-node-canvas** (2.0.0-alpha.14). One that I specify directly (1.6.5-prerelease.1). If I remove one of them the application fails to start due to some linking errors. YMMV.

I’ve put together a git repo with the sample code and binaries on it if you want to try it out. [Check out the source code](https://github.com/techfu-io/chartjs-lambda).

_Martin works as VP Engineering for [StackState](https://www.stackstate.com) where he and his teams are building a next-generation monitoring and AIOps product. As a side project, Martin is working on [Sprintlr](https://sprintlr.io), a tool to improve distributed Scrum teams, and [techfu.io](https://techfu.io), a tool to automatically assess technical talent._

