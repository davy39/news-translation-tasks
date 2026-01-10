---
title: How to deploy a React application to Netlify
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-31T17:35:13.000Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-a-react-application-to-netlify-363b8a98a985
coverImage: https://cdn-media-1.freecodecamp.org/images/1*hxXLMsJtGQCg2RNAdXd3bQ.png
tags:
- name: Design
  slug: design
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: software development
  slug: software-development
seo_title: null
seo_desc: 'By Abhishek Jakhar

  I’m going to teach you how to deploy and host your React app with Netlify.Netlify
  is a service that automates builds, deployments and manages your websites. It’s
  one of the fastest and easiest deployment solutions these days.

  Netli...'
---

By Abhishek Jakhar

I’m going to teach you how to deploy and host your React app with Netlify.  
**Netlify** is a service that automates builds, deployments and manages your websites. It’s one of the fastest and easiest deployment solutions these days.

[**Netlify**](https://www.netlify.com/) offers a free plan. So first, we will log in to [**Netlify**](https://www.netlify.com/) using any one of the options(Github, Gitlab, Bitbucket, Email) given on the login page.

![Image](https://cdn-media-1.freecodecamp.org/images/JVM7UWA0NJZBlBLjw9VovVR4B42w-Wp5LR1C)

![Image](https://cdn-media-1.freecodecamp.org/images/SnfWQ7EEIA5ni1Q0jSNotjADvHuH0jdtDpfK)

![Image](https://cdn-media-1.freecodecamp.org/images/o1fu3AiHPI8NBgsxRTUGsklGgVGi1kA6JbvJ)
_**Left**(Login Page) **Center**(Authorization) **Right**(Netlify Online App)_

We will start by creating a build of our application by running this command:

```
npm run build
```

So, now our build folder will get generated which will contain all the production-ready files.

Now, there are **two ways** to deploy our application to Netlify.

#### **Drag & Drop**

Netifly has made it so easy that we have to just **drag and drop** our **build folder** into their **online app** (Rightmost image above), and our application will get deployed to a live URL.

> **Note:** Netlify online app is the screen which appears after you have logged into your netlify account.

![Image](https://cdn-media-1.freecodecamp.org/images/Val5BuZKW8cVCM8TZ3UUWnezqGOy5SvKYbek)
_**Drag &amp; Drop build** folder to **Netlify Online Application** to Deploy_

#### **Netlify CLI**

Netifly also provides a command line interface that lets you deploy your app straight from the command line. That’s what we will do now.

So first, we’ll install the CLI using the following command:

```
npm install netlify-cli -g
```

Now, we’re ready to deploy it. To deploy the application we have to make sure that we’re in the project folder and then we will run this command:

```
netlify deploy
```

We might get a pop-up window which will ask us to log in with Netlify and grant access to the **Netlify CLI**.

![Image](https://cdn-media-1.freecodecamp.org/images/7Y2-XpgfmWPO-JBB6UgyuqeCyRTOqCHCgGT9)
_Pop-Up window asking you to log in with Netlify and grant access to the Netlify CLI_

Now, we’ll click Authorize. Now that we’re authorized, we can follow the command line prompts to deploy the app.

#### Command Line Prompts

1. In the console, it says that “**This folder isn’t linked to a site yet. What would you like to do?”** It wants to know if we want to link this directory to an existing site or create and configure a new site. Since this is a new site, we’ll select **Create & configure a new site.**

![Image](https://cdn-media-1.freecodecamp.org/images/jCjmOzAhGxe8iQTkmDWB6qjTjwecSm2Wxcq6)

2. It gives us the option to give our site a name. I’ll type **portfolio on netlify** (You can type any available name which you like).

![Image](https://cdn-media-1.freecodecamp.org/images/biH9rSuAPba39ANKe-jGWcJC5biol2bVmQrh)

3. Now it will ask for the Netlify account which you want to use, so I will select **my account (Abhishek Jakhar)**, you can select yours.

![Image](https://cdn-media-1.freecodecamp.org/images/shXwNfAQX9ecLo6fxTGFLC2zItwK3PlUZTa7)

4. Now, as deploy path, we need to specify our project's build directory which contains the assets for deployment. So, we will type **build** there and press enter.

![Image](https://cdn-media-1.freecodecamp.org/images/o0zMKENf5BfzR81Ej7jQbOtgDsvNUytgsB9i)

5. Now, our site will get created and will be deployed to a draft URL first, which we can view by copying and pasting the URL in the browser.

![Image](https://cdn-media-1.freecodecamp.org/images/w7qhwqu6ONS81HFHoTzSlTN2eHhAaHgQ-Eoz)

Now, back in the console, it says **“If everything looks good on your draft URL, take it to live with the --prod flag”**.

So to make our app live, we’ll run the command shown on the command line

```
netlify deploy --prod
```

It will ask us one more time to specify the deploy path for the live build which again is our build folder.

![Image](https://cdn-media-1.freecodecamp.org/images/wDrwvxPQo9IN3KFg1UO4V0CXfeGUFCvkKr7C)

Now, in the console output, we get two URLs. A **Unique Deploy URL,** which represents the unique URL for each individual deployment, and a **Live URL** which always displays your latest deployment.

So each time you update your website and deploy it, you’re going to get a unique URL for that deployment. Basically, if we deploy multiple times we will be having **multiple unique URLs** so that you can point users to a **specific version** of your application. But the **live URL** always displays your **latest changes** at the same URL.

> **Note:** Netlify automatically secures your site over **HTTPS** for **free**.

#### Page Not Found Error

![Image](https://cdn-media-1.freecodecamp.org/images/4skG2qD8TRKYRPFAjVSQ0dgEzrD2PECpdFPi)
_**404 Error** when we refresh application after navigating to a different route_

If you’re publishing an app that uses a router like React Router you’ll need to configure redirects and rewrite rules for your URLs. Because when we click on any navigation item to change the page (route) and refresh the browser, we get a 404 error page.

So Netlify makes configuring redirects and rewrite rules for your URLs really easy. We’ll need to add a file inside the build folder of our app named _redirects. Inside the file, we need to include the following rewrite rule.

```
/*    /index.html  200
```

This rewrite rule is going to serve index.html file instead of giving a 404, no matter what URL the browser requests.

![Image](https://cdn-media-1.freecodecamp.org/images/sXFzzGd39iKJRWwS1syabew0T-GSjCaQI5kw)
_The **_redirects** file inside the build folder containing **redirect rule**_

So now, to view the latest changes in the live URL, we need to deploy with `netlify deploy`. Again, we’ll specify build as the deploy path. Now, when we see the live URL and refresh the app after changing the route we will no longer see the 404 error page.

![Image](https://cdn-media-1.freecodecamp.org/images/HD3tmNtrQ0udjfcEry7TJgkDE0XK2FU5xLYF)

That's all there is to it. On netlify.com you can see your site settings. There you can do stuff like set up a custom domain or connect the site to a GitHub repository.

[**Netlify: All-in-one platform for automating modern web projects**](https://www.netlify.com/)  
[_Deploy modern static websites with Netlify. Get CDN, Continuous deployment, 1-click HTTPS, and all the services you…_www.netlify.com](https://www.netlify.com/)

I hope you’ve found this post informative and helpful. I would love to hear your feedback!

**Thank you for reading!**

