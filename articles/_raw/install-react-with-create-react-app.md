---
title: How to Install React.js with create-react-app
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-10-28T00:12:06.000Z'
originalURL: https://freecodecamp.org/news/install-react-with-create-react-app
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c980e740569d1a4ca17e8.jpg
tags:
- name: create-react-app
  slug: create-react-app
- name: npm
  slug: npm
- name: React
  slug: react
seo_title: null
seo_desc: 'By Cem Eygi

  React is one of the most popular JavaScript libraries in the web development field
  today.

  As a Frontend Developer, I have personally worked with React in my projects and
  probably will continue to work with it in the future. One of the ste...'
---

By Cem Eygi

React is one of the most popular JavaScript libraries in the web development field today.

As a Frontend Developer, I have personally worked with React in my projects and probably will continue to work with it in the future. One of the steps that many people struggle with is the installation/configuration process of React.

So let's start with the basics. In this post, you are going to learn how to install and run a React application the easy way.

Since interest in learning React is also increasing rapidly day by day, I have also decided to create video tutorials about React on [my YouTube channel](https://www.youtube.com/channel/UC1EgYPCvKCXFn8HlpoJwY3Q/). Here's a video version of this tutorial:

%[https://youtu.be/QJZ-xgt4SJo]

## How to Download & Install Node.js

First of all, you are going to need NPM (or Yarn, alternatively). Let's use NPM for this example.

If you don't have it installed on your system, then you need to head to the [official Node.js website](https://nodejs.org/en/) to download and install Node, which also includes NPM (Node Package Manager).

![Image](https://www.freecodecamp.org/news/content/images/2020/10/nodejs.png)
_[Node.js' official website](https://nodejs.org/en/)_

Select the "Recommended For Most Users" button and download the current version for your operating system.

After you download and install Node, start your terminal/command prompt and run `node -v` and `npm -v` to see which versions you have.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/t1.png)

Your version of NPM should be at least 5.2.0 or newer because create-react-app requires that we have [NPX](https://github.com/npm/npm/releases/tag/v5.2.0) installed. If you have an older version of NPM, run this command to update it:

```
npm install -g npm
```

## What is create-react-app?

Since it is complicated and takes a lot of time, we don't want to configure React manually. create-react-app is a much easier way which does all the configuration and necessary package installations for us automatically and starts a new React app locally, ready for development.

Another advantage of using create-react-app is that you don't have to deal with Babel or Webpack configurations. All of the necessary configurations will be made by create-react-app for you.

[According to the React document](https://reactjs.org/docs/create-a-new-react-app.html)ation, create-react-app is one of the officially supported ways to create single-page applications in React. You can find other ways [here](https://reactjs.org/docs/create-a-new-react-app.html).

### How to Install Create-React-App

In order to install your app, first go to your workspace (desktop or a folder) and run the following command:

```js
npx create-react-app my-app
```

The installation process may take a few minutes. After it is done, you should see a folder that appears in your workspace with the name you gave to your app.

> Note: If you're on Mac and receiving permission errors, don't forget to be a super user first with the sudo command.

### How to Run the App You Created with Create-React-App

After the installation is completed, change to the directory where your app was installed:

```
cd my-app
```

and finally run `npm start` to see your app live on localhost:

```
npm start
```

![Image](https://www.freecodecamp.org/news/content/images/2020/10/rw.png)

If you see something like this in your browser, you are ready to work with React. Congratulations! :)

Thank you for reading!

