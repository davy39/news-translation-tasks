---
title: 'Hugo + Firebase: How to create your own static website for free in minutes'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-12T20:26:08.000Z'
originalURL: https://freecodecamp.org/news/hugo-firebase-how-to-create-your-own-dynamic-website-for-free-in-minutes-463b4fb7bf5a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*KAeUHR7NoyfTxOHsfPjqCw.jpeg
tags:
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Aravind Putrevu

  Ever thought of having your own website for putting up your project portfolio or
  resume or a blog for yourself. By the end of this article, you will be able to create
  one.

  Generally, to develop a website you need to know HTML, CSS,...'
---

By Aravind Putrevu

Ever thought of having your own website for putting up your project portfolio or resume or a blog for yourself. By the end of this article, you will be able to create one.

Generally, to develop a website you need to know HTML, CSS, and a bit of JavaScript (sometimes). But, for this, you don’t need to have any coding skills. You just need basic computer skills.

To put up a website, you need to have a “space” (aka hosting) where all your files will be uploaded. Whenever someone types your website and clicks enter, these are the files that are served/presented to the user on the browser.

Let’s get started with what you need to have/know:

#### Google Account

I believe you might already have a Gmail account, which is enough. If not create one.

#### Domain

This is optional. There are various domain name providers in the world, additionally you can buy one at [Google](https://www.google.co.in/search?q=buy+a+domain+name). You can find a list of domain name providers. It is as simple as shopping on [Amazon](http://amazon.com).

#### Hugo

[Hugo](https://gohugo.io/) is a [Go](https://golang.org/) language-based tool, which generates static websites. You can use various templates and make different types of websites like blogs, portfolio sites etc.

Download it from [here](https://github.com/gohugoio/hugo/releases).

#### Firebase

[Firebase](http://firebase.com/) is a mobile and web application platform, acquired by Google a few years ago. Firebase offers hosting as one of its features. However, many mobile developers use it for Analytics, Notifications, Crash Reporting of apps. We are going to use it for hosting our website.

#### Node.js

Node.js is an open-source JavaScript run time built on [Chrome’s V8 JavaScript engine](https://developers.google.com/v8/). For this tutorial, you need it to be installed on your machine for Firebase tools to work. You can download and install it from [here](https://nodejs.org/en/download/).

#### Step 1: Install Hugo on your machine

Windows: You will get a simple portable executable file. You can place it anywhere and run via command line. You can add it to your path variable in Windows environment variables to get it referenced anywhere.

Mac: You can install it using Homebrew. If you don’t have brew installed on your mac, you can download the tarball from [here](https://github.com/gohugoio/hugo/releases).

Either way, make sure you are able to access Hugo by giving below command.

#### Step 2: Create a template site

Head over to the location where you have decided to create your website and enter the command below:

```
$ hugo new site <path_to_folder>
```

At the given location you can see a folder structure as shown in below image.

![Image](https://cdn-media-1.freecodecamp.org/images/Gxfil53Td3cs6jmv9qEIBw6eGeRSPG6bzfi5)
_Image taken on Windows 10_

These folders are just placeholders for your content. All the text content of your site goes to _content_ folder.

You can run below commands to add new files.

```
$ hugo new about.md
```

If you want to add a blog post create a folder named “_blog”_ in _“content”_ folder and start adding your files. These files have an extension of _“.md”_ which are [Markdown](https://en.wikipedia.org/wiki/Markdown) files.

Markdown is a plain text formatting markup language. It is pretty and easy. There are umpteen guides on how to approach Markdown, here is [one](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet).

#### Step 3: Set a theme for the site

Hugo has a great community. Their [themes](https://themes.gohugo.io/) site is enriched with different categories of website themes. Head over to it and select a theme, that suits your requirement.

I chose the [Introduction](https://github.com/vickylaiio/hugo-theme-introduction) theme. Clicking the download button will redirect to [GitHub](https://github.com/vickylaiio/hugo-theme-introduction).

Each theme will have its own way of setting things up. This particular theme doesn’t have many steps. Just clone or download the zip to the themes folder. Copy the _config.toml_ file to the root folder of your website.

#### Step 4: Set up your preferences

Open the _config.toml_ file and start editing it. Give your name and other details you wish to show up on the website. Some themes support Google Analytics so that you can track the user visit count etc. You can give your GA Id to gather data.

#### Step 5: Set up a Firebase Hosting Project

As I mentioned earlier, [Firebase](https://en.wikipedia.org/wiki/Firebase) is a beautiful mobile platform with a ton of features. I used Firebase hosting to host my static website generated via Hugo.

To use Firebase services use your Google account and [login to Firebase website](https://firebase.google.com/).

Click on _“Go to console.”_ Create a project by giving it a name. You will be shown an overview page in which you should select “_getting started on Hosting.”_

#### Step 6: Set up Firebase tools on your machine

Open your terminal/command line interface on your machine and type command below.

```
$ npm install -g firebase-tools
```

The above command installs the Firebase-tools package. You need to execute a few more commands to be able to deploy your website directly.

```
$ firebase login
```

This command connects your machine to the Firebase project. It enables you to list and select the project to which you want to push your changes.

```
$ firebase list
```

You can run above command to see the project which you have created. One final touch to the entire workflow, we need to initialize the root folder of your website as Firebase project root.

```
$ firebase init
```

It will ask you some questions like

* Which Firebase CLI features do you want to setup? Answer: Hosting.
* Select a default Firebase project for this directory Answer: Select Firebase project you have created in Step 5.
* Do you want to use as your public directory? Answer: Yes.
* Configure as a single-page app? Answer: Yes.

To avoid confusion, I have detailed screenshots taken at each step for your reference. It can be downloaded [here](https://www.dropbox.com/s/z6siqqymi1rin0u/Screenshots_Firebase_Tools_Setup.zip?dl=0).

Finally! Firebase initialization is complete.

#### Step 7: Verify your website locally

Run below command to check your site locally on your machine.

```
$ hugo server -w
```

Hugo comes with a light-weight high-performance web server, where you can check all your changes. Make sure that all your images are put up in _static/img_ folder. In an iterative process, change your _config.toml_ and verify those on browser. Below is the port on which your server will be running.

```
http://localhost:1313
```

#### Step 8: Deploy your website

Type in below command to generate your site and push it to corresponding Firebase project which you have configured in **Step 5**.

```
$ hugo && firebase deploy
```

#### Step 9: Connect it to your domain (optional)

Firebase provides an option to connect your domain to Firebase app. Click on _connect domain_ and give your domain and add the TXT records to verify your domain ownership.

![Image](https://cdn-media-1.freecodecamp.org/images/bgk-Sh1N99CJ2qImzFWdiVnO7YdR-EGMw0K4)

For this log on to your domain registrar portal.

#### Step 10: Create a blog post

Creating a blog post is pretty simple. Hugo understands markdown files. Just head over to _content->b_log folder (folder location depends on the theme). Create a markdown file. Repeat the Step 8 to see the results.

If you have any queries or doubts, you can DM me on [twitter](https://twitter.com/aravindputrevu) !

Always Happy to help!

