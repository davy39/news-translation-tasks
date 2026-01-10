---
title: How to Deploy a Front End Application with Netlify
subtitle: ''
author: Idris Olubisi
co_authors: []
series: null
date: '2021-01-09T00:23:29.000Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-your-front-end-app
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/Turquoise-Confetti-Birthday-Greetings-Facebook-Cover.png
tags:
- name: app development
  slug: app-development
- name: deployment
  slug: deployment
- name: Front-end Development
  slug: front-end-development
- name: Netlify
  slug: netlify
seo_title: null
seo_desc: 'Hi everyone! In this article, I''m going to discuss how to deploy an application
  you''ve built.

  The application deployment process might seem complicated, and this might prevent
  some developers from deploying their applications after they''ve developed ...'
---

Hi everyone! In this article, I'm going to discuss how to deploy an application you've built.

The application deployment process might seem complicated, and this might prevent some developers from deploying their applications after they've developed them. 

So here, I will be taking you through a seamless process to spin up your application which can then be accessed anywhere in the world via a URL.

### Table of contents

- Why do you need to deploy your frontend applications?
- What is Netlify?
- What you can do with Netlify
- How to deploy your site
- Resources

## Why do you need to deploy your frontend applications?

There are numerous advantages to deploying your applications. Of course, you don't want your beautiful application to sit on your localhost forever. 

Deploying your application makes it easier to share your project, side-gig, or startup with potential investors or future employers. If they can see those projects, it helps them gauge your skills. It also lets you show off your progress to the world.

In this article, we will be using the amazing [Netlify](https://www.netlify.com 'Netlify Homepage') platform to deploy our application.

That name sounds familiar, right? But if you haven't used it to deploy a web application yet, trust me I know how you feel. 

I will take you through the steps to get your site deployed to [Netlify](https://www.netlify.com) in less than 4 minutes. We'll also see some other functionalities that can be done with Netlify out of the box.

## What is Netlify?

[Netlify](https://netlify.com/) is a platform that lets developers automate modern web projects, and it's a place where you can deploy your application without worrying about frustrating configurations. 

You can also integrate cool features and dynamic functionality like serverless functions and form handling on Netlify. Sounds good, right?

## Netlify Features

### Configure builds 
Netlify helps you run the build command each time you push an update to your repository. 

There are additional settings that you can configure like auto-deploy along with other useful deployment settings.


### Site deploys [(Atomic deploys)](https://docs.netlify.com/site-deploys/overview/ ) 
One of the awesome features Netlify has is site deployment. It ensures that your site is deployed and always consistent. 

You can also enable deploy notifications, run a test while Netlify compares the new deploy with the existing one, and then update only the files that have been changed.


### Monitor sites [(Netlify Analytics)](https://docs.netlify.com/monitor-sites/analytics/)
Monitoring your site might become difficult if you don't have proper infrastructure in place. 

You can easily monitor your site'sactivities on this platform where you can track each log on the team's build usage.


#### Domains & HTTPS [(Register new domains)](https://docs.netlify.com/domains-https/netlify-dns/domain-registration) 
In simple terms, a domain is the URL anyone types into the browser to visit your site. You can assign a custom domain if you have already purchased one or secure a domain from Netlify. 

Either way, the domain name system management is handled by Netlify. They also provide free automatic HTTPS on all sites. Cool right?


#### Routing [(Learn about routing)](https://docs.netlify.com/routing/redirects/) 
Routing, Redirects, proxies, and so on all become much easier when your site is deployed on Netlify.


### Visitor access
Here's another cool feature I enjoy: whenever you need to add someone to the team, you can set up role-based access controls that allow the Admin/Senior developer to take control and give access to individuals on the team to avoid escalations.


### Forms [(Netlify Forms)](https://docs.netlify.com/forms/setup/) 
When you need to collect data from users on a site deployed on Netlify, you can do so using Netlify forms. This doesn't add API calls or extra JavaScript on your site, either.

Build bots handle form submission by parsing your HTML files directly at deploy time. You can also configure the receiver, group, and notifications.


### Functions [(Deploy serverless functions)](https://docs.netlify.com/functions/overview/) 
Serverless functions can be referred to as single-purpose, programmatic functions that are hosted on managed infrastructure.

Netlify lets you deploy serverless Lambda functions with management handled directly within Netlify, while they are built and deployed with the rest of your sites.


### The Netlify CLI [(Netlify command-line interface)](https://docs.netlify.com/cli/get-started) 
You might be wondering if all activities are carried out on the Netlify UI alone - well, no they're not. 

There is another great feature that allows developers to deploy sites or do some configuration right from their terminal. The Netlify CLI can be used to run a local development server that can be shared, including plugins.


### The Netlify API [(Netlify API)](https://docs.netlify.com/api/get-started/#authentication) 
Netlify's API can be used to handle the deployment of sites, script injections, and more. It uses JSON for serialization, which conforms to the REST standard.


### Accounts & billing 
Learn about [managing team members](https://docs.netlify.com/accounts-and-billing/team-management/manage-team-members) and how to transfer sites between teams.


> I hope you can now see how powerful Netlify is. Sut seeing sometimes can be deceiving, so let's try it out on our own.


As you can tell from the title of this article, I will only be showing you how to deploy your site to netlify.com. But to explore other functionalities [click here to read more](https://docs.netlify.com/), practice, and explore.

## How to Deploy a Site to Netlify


### Step One

Login or signup on netlify.com if you are a new user. It's free :)


### Step Two

As shown below, all you need is to select a site from Git by clicking on the button with the name “New site from Git”.

![Netlify](https://res.cloudinary.com/olanetsoft/image/upload/v1608119982/netlify%20deploy%20post/Screenshot.png)


### Step Three

You will see the interface below where you can choose the Git provider where your site source code is hosted.

![Netlify](https://res.cloudinary.com/olanetsoft/image/upload/v1608119980/netlify%20deploy%20post/select_git.png)


### Step Four

Choose the repository you want to link to your site on Netlify.

![Netlify](https://res.cloudinary.com/olanetsoft/image/upload/v1608119980/netlify%20deploy%20post/select_repo.png)


### Step Five

We are almost there :)

This section allows you to get more control over how Netlify builds and deploys your site with the settings option shown below:

![Netlify](https://res.cloudinary.com/olanetsoft/image/upload/v1608119981/netlify%20deploy%20post/select_to_deploy_site.jpg)


### Step Six

Wait, Netlify is getting things ready for you. :)


![Netlify](https://res.cloudinary.com/olanetsoft/image/upload/v1608119980/netlify%20deploy%20post/site_deploy_in_pgrogress.png)


### Step Seven

![Netlify](https://res.cloudinary.com/olanetsoft/image/upload/v1608119980/netlify%20deploy%20post/site.png)


Congratulation Your site is Live!

![Netlify](https://res.cloudinary.com/olanetsoft/image/upload/v1608119980/netlify%20deploy%20post/Screenshot1.png)


Click on the generated URL with the .netlify.com extension below the header that states “Deploys for”.

**Lastly: You can also set up a new domain or change the generated one to something nice by clicking on the “…” that embeds “Edit site name” but it will end with .netlify.com. [Click here to read more](https://docs.netlify.com/domains-https/custom-domains/)**

![Netlify](https://res.cloudinary.com/olanetsoft/image/upload/v1608119981/netlify%20deploy%20post/domain_setup.png)


I hope you have found this guide useful :)


NOTE: the Netlify URL extension is now netlify.app. All netlify.com URLs will now be redirected to netlify.app.


**Please don't forget to check out my other articles, it gives me joy :) and the vibes to write more stuff.**

You can also reach out to me on [Twitter](https://twitter.com/olanetsoft).



