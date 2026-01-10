---
title: How to host a Git repository on a subdomain with Netlify
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-23T15:15:15.000Z'
originalURL: https://freecodecamp.org/news/how-to-host-a-git-repository-on-a-subdomain-with-netlify-b8afb5fca96e
coverImage: https://cdn-media-1.freecodecamp.org/images/0*yd8PzBwBVOc98lXb
tags:
- name: Netlify
  slug: netlify
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Hosting
  slug: web-hosting
seo_title: null
seo_desc: 'By Glyn Lewington

  Let’s say you have your portfolio, like [www.glynlewington.com](http://www.glynlewington.com),
  hosted on Netlify and want to add your projects onto the same domain. They are all
  separate git repositories and Netlify is made for host...'
---

By Glyn Lewington

Let’s say you have your portfolio, like `[www.glynlewington.com](http://www.glynlewington.com)`, hosted on Netlify and want to add your projects onto the same domain. They are all separate git repositories and Netlify is made for hosting from a single repository…but don’t fear! We can host them on subdomains like `project.glynlewington.com` with just a little work.

Netlify makes it super easy to host your static sites with them for free. I recently moved my portfolio from a VPS over to them, and it’s great that they automatically update your site every time you push to your git repository.

In the past, I had all my personal projects also hosted on subdirectories, e.g. `www.glynlewington.com/project`. This is either difficult or impossible with Netlify. Netlify is mostly set up for you to host everything in one site from one git repository.

The compromise I came to is hosting them on subdomains instead, like `project.glynlewington.com`. This also isn’t documented very well but it is possible.

* Go to [www.netlify.com](http://www.netlify.com,) and login or signup.
* Select “New site from git”.
* Choose your provider (e.g. GitHub) — You may need to authenticate here.
* Select the git repository you want to create a site from.
* Select the branch you want to deploy from.
* Choose any commands that need to be run. — _If it’s a React app you will need to run a build command._
* Choose the directory that you will publish from. It will contain files such as index.html. — _If it’s a React app this will probably be the build folder._
* Select “Build Site”.

At this point, you should have a functioning app hosted on a Netlify free domain such as `https://hungry-bose-fb0e6d.netlfiy.com`. If this isn’t working, check that there are no errors with the build process and fix these if there are.

Now to set up a custom domain.

* Go into your app overview on Netlify.
* It will say your site is deployed successfully and you can set up a custom domain.
* Click on set up a custom domain, type in the domain you want, including the subdomain, and click verify. E.g. `project.glynlewington.com`.

Next, login to your domain hosting provider. I use Cloudflare but it will be the same or similar using others.

* Go to DNS settings.
* Select a new CNAME record.
* Input a “Name” — this is the subdomain, it should be the same one you selected previously on Netlify. E.g. `project`
* Under “IPv4 Address” input the free domain for your Netlify site. E.g. `hungry-bose-fb0e6d.netlify.com`.
* If you are also using Cloudflare, turn off the traffic routing through Cloudflare. This messes with Netlify.
* Add record.

Done! Once you’ve done this you can access your site on the subdomain.

Netlify will also automatically add https security to your site, no need to worry about this.

