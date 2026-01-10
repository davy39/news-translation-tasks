---
title: How to Deploy Your React App Using Cloudflare Pages, Vercel, and Netlify
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2022-11-28T21:30:24.000Z'
originalURL: https://freecodecamp.org/news/deploy-react-app
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/mugshotbot.com_customize_color-pink-image-9129875b-mode-dark-pattern-none-theme-two_up-url-https___gifcoins.io.png
tags:
- name: deployment
  slug: deployment
- name: React
  slug: react
seo_title: null
seo_desc: "You have been working on a React application and now you're ready to actually\
  \ push it to the web. What services do you use to publish your site and make it\
  \ live to the world? \nWhether you're ready to release your website as a finished\
  \ product or you ..."
---

You have been working on a React application and now you're ready to actually push it to the web. What services do you use to publish your site and make it live to the world? 

Whether you're ready to release your website as a finished product or you are in the process of development, let's cover the 3 of the best (and free!) ways to deploy your React application right now. 

## How to Deploy a React App with Cloudflare Pages

One of the newest ways to deploy your React application is with Cloudflare Pages. 

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-11-24-at-12.41.27-PM.png)
_Cloudflare Pages_

Roughly 20% of all websites use Cloudflare for various reasons, often for free features such as their DDoS (Denial-of-service attack) mitigation.

Within the past couple of years, it has entered into the deployment space with Pages. Websites hosted on Cloudflare Pages are served from the Cloudflare edge network, which is one of the fastest ways to serve your website to users globally.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-11-24-at-12.47.53-PM.png)
_The Cloudflare edge is one the fastest networks_

To get started using Cloudflare pages, all you need is a (free) Cloudflare account.

You can deploy your site to Pages by selecting a Git repository from your GitHub account. Alternatively, you can push a folder directly that includes all of your site's resources. 

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-11-24-at-12.20.19-PM.png)
_Options to deploy to Cloudflare Pages_

After that, choose the framework that you are using. Pages includes options for React as well as Next.js. 

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-11-24-at-12.22.29-PM.png)
_Framework presets for Cloudflare Pages_

To finish your deployment, all you have to do is hit the Deploy button. Afterwards your site will be deployed to their edge network within a couple of minutes! 

Cloudflare Pages comes with built-in web analytics. But ultimately the best benefit to deploying to Cloudflare Pages is that you can deploy unlimited sites with unlimited bandwidth for free. 

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-11-24-at-1.04.33-PM.png)
_Cloudflare Pricing_

There are Pro and Business tiers, but these exist for customers who would like to have more concurrent builds (to build multiple sites at once), more site builds per month, and more custom domains.

## How to Deploy a React App with Vercel

Vercel is a deployment platform built by the same people responsible for the Next.js framework.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-11-24-at-1.10.53-PM.png)
_Vercel deployment platform_

As a result, Vercel is optimized for projects that are built with Next.js. However, any React framework that you choose is supported including Create React App and Gatsby. 

Out of all the deployment platforms, Vercel has the quickest deployments. A medium-sized Next.js application builds in a little over one minute. 

What's powerful about Vercel is that they have a great deal of integrations that make it very easy to connect with a bunch of other services that you're likely already using or may want to use. 

Integrations include databases like MongoDB or PlanetScale as well as CMS tools, monitoring tools, and developer tools.

Like Cloudflare Pages, Vercel also includes a worldwide CDN for your project to make content delivery while your site's assets very quickly, plus Git-based deployments, and built-in analytics. 

Vercel analytics monitor the performance of your website along with the amount of users on your website from day-to-day. 

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-11-24-at-1.28.24-PM.png)
_Vercel Analytics_

Vercel has a minimal, clean interface to manage your projects, which is more sophisticated than Cloudflare Pages. 

Vercel's pricing, however, will set you back if you have either a commercial project or you use more than 100 gigabytes of bandwidth per month. In that case you must upgrade to their Pro plan, which is $20 per month. 

## How to Deploy a React App with Netlify

Netlify is a very similar platform to Vercel, with a number of exclusive features, such as forms and authentication.

Both Vercel and Netlify support all React frameworks, are optimized for Next.js, have a built-in CDN, and deployments are made through Git. 

Netlify has a similarly sophisticated dashboard and user interface. Like Vercel, Netlify features a large number of integrations to add to your project instantly. 

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-11-24-at-12.33.09-PM.png)
_Netlify Integrations_

Netlify, however, has some features such as Netlify Analytics which come at a separate price. Additionally, Netlify has a forms service which allows you to receive form submissions without any server side code or JavaScript. 

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-11-24-at-12.34.20-PM.png)
_Netlify Forms_

It also includes some other solutions such as authentication with a service called Netlify identity, which is helpful if you want to authenticate users on your static site. 

![Image](https://www.freecodecamp.org/news/content/images/2024/08/premium-netlify-features.jpg)
_Premium Netlify Features_

It also has some new features like split-testing that allow you to test one feature against another in your website. 

When it comes to pricing, you can use Netlify for free even if you have a commercial product. If you exceed their 100GB free tier limit, you will need to upgrade to pro to get 1TB of bandwidth. 

If you want unlimited access to features such as Netlify Forms and Identity, Netlify will set you back $99 per month, which also includes 1.5 terabytes of bandwidth per month. In short, Netlify is very competitive with Vercel with some exclusive features that come at a price. 

## Thanks for reading!

Hopefully this article has given you a solid overview of these different deployment methods so you can get to deploying your React app in no time.

## Become a Professional React Developer

React is hard. You shouldn't have to figure it out yourself.

I've put everything I know about React into a single course, to help you reach your goals in record time:

[**Introducing: The React Bootcamp**](https://www.thereactbootcamp.com)

**It’s the one course I wish I had when I started learning React.**

Click below to try the React Bootcamp for yourself:

[![Click to join the React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Click to get started*

