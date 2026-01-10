---
title: How to enable ahead-of-time compilation in an Angular hybrid app
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-06T08:34:39.000Z'
originalURL: https://freecodecamp.org/news/angular-hybrid-app-ahead-of-time-compilation-204ced918ec7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*iF8uCp-Dx8BfuCSgkbHvnQ.jpeg
tags: []
seo_title: null
seo_desc: 'By Kamil Maraz

  And why you’ll want to do this

  Ahead-of-time (AOT) compilation is a big word in the Angular community. Everybody
  wants to get it running. If you are starting with a new project using Angular CLI,
  you’ve won. There is nothing simpler th...'
---

By Kamil Maraz

#### And why you’ll want to do this

Ahead-of-time (AOT) compilation is a big word in the Angular community. Everybody wants to get it running. If you are starting with a new project using [Angular CLI](https://cli.angular.io/), you’ve won. There is nothing simpler than to [include “ — aot” option](https://angular.io/guide/aot-compiler#angular-compilation) in your terminal.

But what if you have a custom Webpack configuration? Or you are using [Upgrade module](https://angular.io/guide/upgrade) and you have a hybrid Angular application? Have a look at how we dealt with this particular problem in [Admin](https://admin.sli.do) — administration interface for [Slido](https://slido.com) users.

![Image](https://cdn-media-1.freecodecamp.org/images/1*iF8uCp-Dx8BfuCSgkbHvnQ.jpeg)

#### Ahead-of-Time vs. Just-in-Time

The difference between AOT and Just-in-Time compilation (JIT) rests in the step in which compilation happens. With AOT, we are talking about the build phase. It happens before running the application in the browser. JIT compilation is happening when the application is running in the browser.

As it is stated in the [Angular guide:](https://angular.io/guide/aot-compiler#the-ahead-of-time-aot-compiler)

> “The Angular Ahead-of-Time compiler converts your Angular HTML and TypeScript code into efficient JavaScript code during the build phase before the browser downloads and runs that code.”

One of the advantages of enabling AOT is **faster application rendering.** As all of the application parts are already compiled when downloaded by the browser, there is a significant decrease of bootstrap time of application as well as the rendering times during its use.

Another benefit can be a **smaller bundle size.** When you are using AOT, you do not need to include [@angular/compiler](https://angular.io/api/core/Compiler) as it is no longer needed. The compiled application can increase in its bundle size, but this strongly depends on the specifics of your application.

Thirdly, there is a much higher possibility to **spot compilation errors in templates,** as you will be notified by the compiler during build time. If you are using Visual Studio Code, you can use [Angular Language Service extension](https://marketplace.visualstudio.com/items?itemName=Angular.ng-template) as it has AOT diagnostics enabled in real-time.

#### Steps necessary to enable AOT

The first step, as it happens, is to run _npm install [@ngtools/webpack](https://www.npmjs.com/package/@ngtools/webpack)_.

Next, you have to configure Webpack properly. In this step, you want to configure AngularCompilerPlugin which comes with @ngtools. Using configuration parameters you will set up locations of tsconfig and entry files. Most of the time you want to use separate tsconfigs for JIT and for AOT. You will see why in a moment.

In your standard tsconfig you need to exclude main.aot.ts file, which is the entry point for applications compiled using AOT. In this file, you will import files which will be available only during the build time. This way you can separate between JIT and AOT builds easily, without any errors.

Tsconfig for AOT is ordinary. There is nothing special about it.

Next file is here to demonstrate how we can split builds between JIT and AOT. In this case, JIT is used in a dev environment and AOT is used in the production.

AOT uses platformBrowser instead of platformBrowserDynamic. Next important step is to import factory files which will be available during the build time.

#### Performance improvements

From the start, we wanted to have AOT enabled for a reason — to have better performance of [Admin](https://admin.sli.do) application. This is a short comparison of what improved and what remained the same:

As you can see, the initial load time significantly decreased even when the bundle size increased slightly.

![Image](https://cdn-media-1.freecodecamp.org/images/1*E9l7k2n4OsqbiQtlg26ANw.png)
_Apdex measured before and after the release of AOT to the production._

![Image](https://cdn-media-1.freecodecamp.org/images/1*lgQobPbYaeh8duw-2ePnTg.png)
_Average load times decreased even when throughput remained the same._

![Image](https://cdn-media-1.freecodecamp.org/images/1*LKYyX2rAR0r1p8zaUA2-kA.png)
_Average load times compared in a histogram overlay (dark=JIT,light=AOT)._

#### Wrap up

Enabling AOT resulted in a notable improvement for all of our users. Initial load times improved significantly and the application sped up as well.

If you’ve never considered enabling AOT in production, now is the time. Do you have any questions about this topic? Feel free to contact me.

