---
title: How to get started using Firebase Hosting
subtitle: ''
author: Flavio Copes
co_authors: []
series: null
date: '2018-02-08T15:19:38.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-started-using-firebase-hosting-439d4bd45cb6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*q2NlUEQNkZmI6KLvnT1tzA.png
tags:
- name: Firebase
  slug: firebase
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
- name: Web Hosting
  slug: web-hosting
seo_title: null
seo_desc: 'Interested in learning JavaScript? Get my ebook at jshandbook.com


  Firebase is a mobile and web application development platform that was developed
  by Firebase, Inc. in 2011. It was acquired by Google in 2014 and rolled up into
  the Google Cloud servi...'
---

> Interested in learning JavaScript? Get my ebook at [jshandbook.com](https://jshandbook.com/)

Firebase is a mobile and web application development platform that was developed by Firebase, Inc. in 2011. It was acquired by Google in 2014 and rolled up into the Google Cloud service. Now, it’s a flagship product of the Google Cloud offering.

Firebase is a complex and articulated product, mainly targeted at mobile applications.

One of its lesser known features that we’ll discuss in this article is the Firebase advanced web hosting service.

### Firebase Hosting Features

Firebase Hosting provides hosting for static web sites, such as

* sites you can generate using static site generators
* sites built with server-side CMS platforms, from which you generate a static copy of the website

You can host anything as long as it’s not dynamic. A WordPress blog, for example, is almost always a good candidate to be a static site if you use Disqus or Facebook comments.

Firebase Hosting delivers files through the Fastly CDN, using HTTPS and provides an automatic SSL certificate, with custom domain support.

Its **free tier is generous**, with cheap plans available if you outgrow it. It’s very developer-friendly, provides a CLI interface tool, an easy deployment process, and one-click rollbacks.

### Why should you use Firebase Hosting?

Firebase can be a good choice to deploy static websites, and Single Page Apps.

I like to use Firebase Hosting mainly because I tested many different providers and Firebase offers an **awesome speed** across multiple geographic locations without the need for a separate CDN on top, since **the CDN is built-in** for free.

While having your own VPS is a very good option, **the overhead of managing your own server** for a simple website is just not worth it. I’d prefer to focus on the content rather than on the operations, just like I’d deploy an app on Heroku.

Firebase is even easier to setup than Heroku.

### Install the Firebase CLI tool

Install the Firebase CLI with

```
npm install -g firebase-tools
```

or

```
yarn global add firebase-tools
```

Authenticate with the Google account (I’m assuming you already have a Google account) by running

```
firebase login
```

### Create a project in Firebase

Go to [https://console.firebase.google.com/](https://console.firebase.google.com/) and create a new project.

![Image](https://cdn-media-1.freecodecamp.org/images/0hzGqiYVSrZev8ogQPbGuw7yIa6K4VZWCgSq)

Now within the console, run the following from the root folder of the site you’re working on:

```
firebase init
```

![Image](https://cdn-media-1.freecodecamp.org/images/l8Egdd07uOmSD9DABh0yGz2afrukibewdZWa)
_firebase init_

Press Space to select the “Hosting” option, then Enter to confirm your choice.

Now you need to choose the project you want to deploy the site to.

![Image](https://cdn-media-1.freecodecamp.org/images/6J2TVueoEKaBSPIjJz6UvpZkLNNobMfBNmU9)

Choose “create a new project”.

Now you choose which folder contains the static version of your site. For example, `public`.

You’ll be asked two questions about the app configuration. Reply “**No**” to both of them:

* Configure as a single-page app (rewrite all urls to /index.html)?
* File public/index.html already exists. Overwrite?

This will prevent Firebase from adding its own default index.html file.

Now, you’re good to go:

![Image](https://cdn-media-1.freecodecamp.org/images/5NL3xuH0FsPqFq2whtP0QI6GL4tZIeyZLKa-)

### Configure the site

The Firebase CLI app created the `firebase.json` file in the root site folder.

In this article, I tell how to configure a simple feature in Firebase Hosting, by adding a small bit of configuration in the `firebase.json` file.

I want to set the Cache-Control header directive on all the site assets - images, CSS and JS files.

A clean `firebase.json` file contains the following:

```
{   "hosting": {    "public": "public",     "ignore": [       "firebase.json", "**/.*",       "**/node_modules/**"     ]   } }
```

It tells Firebase where is the site content, and which files it should ignore. Feel free to add all the folders you have, except `public`.

We’re going to add a new property in there, called `headers`:

```
{   "hosting": {     "public": "public",     "ignore": [       "firebase.json",      "**/.*",       "**/node_modules/**"    ],     "headers": [       {         "source" : "**/*.@(jpg|jpeg|gif|png|css|js)",         "headers" : [ {           "key" : "Cache-Control",           "value" : "max-age=1000000" //1 week+         } ]       }     ]   } }
```

As you can see, we tell that for all files ending with `jpg|jpeg|gif|png|css|js` Firebase should apply the `Cache-Control:max-age=1000000` directive, which means that all assets are cached for more than 1 week.

### Publish the site

When you are ready to publish the site, you just run the following command and Firebase will take care of everything.

```
firebase deploy
```

You can now open [https://yourproject.firebaseapp.com](https://yourproject.firebaseapp.com/) and you should see the website running.

### Custom Domain

The next logical step is to make your site use a custom domain.

Go to [https://console.firebase.google.com/project/_/hosting/main](https://console.firebase.google.com/project/_/hosting/main) and click the “Connect Domain” button:

![Image](https://cdn-media-1.freecodecamp.org/images/OktJ0asSC0uVphJs2HCoqYIrz3FvRD7yKKRA)

The wizard will ask you for the domain name, then it will provide a TXT record you need to add to your hosting DNS panel to verify the domain.

If the domain is brand new, it might take some time before you can pass this step.

Once this is done, the interface will give you two **A records** to add as well to your hosting DNS panel.

If you set up `yourdomain.com`, don’t forget to also set up `www.yourdomain.com` by making it a redirect.

![Image](https://cdn-media-1.freecodecamp.org/images/GCq9sjxSfJ1Jvw1JsZAVLjlF2EnJS213a4IH)

Now you just have to wait for your hosting to update the DNS records and for DNS caches to flush.

Also, keep in mind that your SSL certificate is automatically provisioned but requires a bit of time to be valid.

> Interested in learning JavaScript? Get my ebook at [jshandbook.com](https://jshandbook.com/)

