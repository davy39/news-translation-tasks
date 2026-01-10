---
title: How to Deploy a React Router App to Netlify and Fix the "Page Not Found" Error
subtitle: ''
author: Israel Chidera
co_authors: []
series: null
date: '2022-10-03T17:16:24.000Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-a-routed-react-app-to-netlify
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/netlify1-1-1.png
tags:
- name: Netlify
  slug: netlify
- name: React
  slug: react
- name: react router
  slug: react-router
seo_title: null
seo_desc: 'Have you ever experienced a “PAGE NOT FOUND” error when trying to access
  or refresh an application that uses React Router? Don''t worry, you''re not alone.

  In this article, you will learn how to deploy a React application that uses react-router
  without...'
---

Have you ever experienced a “PAGE NOT FOUND” error when trying to access or refresh an application that uses React Router? Don't worry, you're not alone.

In this article, you will learn how to deploy a React application that uses react-router without any problems.

## The Problem with Deploying react-router Apps

To make sure your users are happy, you'll typically prioritize user experience when building an application. Good user experience ensures that your website or application is easy to understand, easy to use, and easy to navigate. 

If you have published a React app to Netlify that uses React router before now, you will likely notice that while navigating through your routes, you get an error (**page not found**) when you refresh your browser. This creates a bad user experience. 

Through this article, you will learn how to deploy a React app through the Netlify CLI and how to resolve the problem with deploying a react-router app.

## What is Netlify?

According to [their docs](https://docs.netlify.com/), "Netlify is an all-in-one platform for automating modern web projects." 

Netlify helps web developers build and deploy their applications instantly. This handy tool replaces your hosting infrastructure and helps facilitate your continuous integration and deployment pipeline with one workflow. It can really help increase your productivity.

The Netlify CLI (Command Line Interface) helps you easily build, test, and deploy applications straight from your command line. 

It lets you:

1. start a project in seconds
2. configure continuous deployment
3. run a local development server that you can share with other developers
4. deploy your projects globally

You can sign up for a [Netlify account](http://netlify.app) with your email or your Git account.  
If you don't have a Git account, you can create a GitHub, GitLab, or bitbucket account in no time.

So, let’s see how you can deploy your react-router app using the Netlify CLI.

## How to Deploy Your App Through the Netlify CLI

To start using Netlify’s CLI, you must have Node.js installed on your computer. You can visit [here](https://nodejs.org/en/download/) to install Node.js. 

Then you can get started by installing the Netlify CLI using this command:

```js
npm install netlify-cli -g
```

Now that you have installed Netlify’s CLI, you can deploy your application to Netlify. Before that, you might want to get your build folder (I'll explain why below). 

To get your build folder, type the following command:

```js
yarn run build
//or
npm run build
```

If you have not logged in to your Netlify account before now, you might see a pop-up window asking for permission to access Netlify.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/netlify3.png)

After getting access to the Netlify CLI, you will get a prompt asking what you would like to do. Select the option to **create and configure a new site**. You can use your arrow keys to navigate between options.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/netlify4.png)

You will get prompts to select a team and a site name for your app. You can either input your preferred name for your app or use the default name which you can change later.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/netlify5.1.png)

You will get a prompt asking which directory to publish. Input **build** as your deploy folder and press enter to get your React app deployed. The build folder which was generated at the beginning 0f this tutorial will serve as the deploy path.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/netlify7.png)

If you get a final response that states **“If everything looks good on your draft URL, deploy it to your main site URL with the --prod flag”**, you are on the right track. You will be provided with the website draft URL to preview your app.

You can deploy to the main site by running the following command:

```js
netlify deploy --prod
```

Awesome. You now have your website URL.

## How to Fix the "Page Not Found" Error

![Image](https://www.freecodecamp.org/news/content/images/2022/09/netlify1.png)
_page not found, netlify error_

To avoid the page-not-found error whenever you are either trying to access your app or you're on other routes, you have to set up a redirect and rewrite rules for your react-router application. 

The redirect rule will help your application avoid a 404 error. All requests will get redirected to the /index.html instead of giving a 404 error.

To configure your redirect rules, you have to create a file that does not have an extension named (_redirects) inside your public folder.

Include the following command in the _redirects file:

```_redirects
/*    /index.html  200
```

To view the changes in your app, you'll have to deploy it again with the following command:

```js
netlify deploy
```

## Conclusion

This article has explained how to deploy a react-router app using Netlify’s CLI and fix the page-not-found error while accessing your routes.

I hope you have found this article useful.

**Keep building, and keep deploying!**

