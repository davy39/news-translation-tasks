---
title: How to Build A WordPress Website Locally - What You Need To Know
subtitle: ''
author: Jim Campbell
co_authors: []
series: null
date: '2021-02-22T19:22:52.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-wordpress-website-locally
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/ilya-pavlov-OqtafYT5kTw-unsplash.jpg
tags:
- name: WordPress
  slug: wordpress
seo_title: null
seo_desc: WordPress is the most popular content management system in the world. Whether
  you are an experienced developer using the tech that powers 38% of all websites
  or you are just getting started in WordPress, building locally on your computer
  is a low-cos...
---

WordPress is the most popular content management system in the world. Whether you are an experienced developer using the tech that powers 38% of all websites or you are just getting started in WordPress, building locally on your computer is a low-cost, testing-friendly, and fast way to create WordPress websites.

## What does building locally mean?

A "local development environment" or "developing locally" just means hosting the website's files on your computer as opposed to on a web host's servers.

You may already be doing this. Many programmers [develop backend applications locally](https://forum.freecodecamp.org/t/developing-backend-applications-locally/147374). 

If you are just starting out in web development, you may have built some basic sites with HTML and CSS using text editors like [Atom](https://atom.io/), [Sublime](https://www.sublimetext.com/), or [Visual Studio Code](https://code.visualstudio.com/). These simple sites are already hosted locally. 

When you start to run more advanced code that needs to utilize PHP, JavaScript, and SQL, you need some more advanced tools that we will discuss later.

## Why should I build a WordPress site locally?

Before getting to the tools you need to build a WordPress site locally, let's quickly touch on why you should.

I was recently speaking to a fellow web developer, Daniel, who builds all of his sites locally. He started out building simple HTML and CSS sites and also builds more advanced WordPress sites. 

His main reason for building locally, which I thought were excellent, are:

1. **Quick setup** - there is no need to wait for a hosting provider or to configure a domain name. I work for a number of small businesses and quickly getting a mockup design out the door is a huge benefit of local development. 
2. **Low cost** - hosting and domain names can be expensive. Developing locally is free!
3. **No domain name needed** - if you are not set on a domain name, you can still start building locally. This provides great flexibility and will save you the pains of migrating your WordPress website.
4. **Easy testing** - when you develop locally, you can experiment more easily with plugins, themes, and custom development. There are no worries if you break your website. You're the only person who can view and use the website, so move fast and break things!
5. **Site Speed** - when you make an update to your website, you don't need to wait for a server to render the page. It is like browsing the internet with instantaneous internet speeds.

## How to Build A WordPress Site Locally

Now that you've decided to build your Wordpress site locally, you need the help of a tool to build your site. 

These tools will set up a **web server software**, **PHP**, and **SQL database management** on your computer. Installing all of these separately on your computer can be confusing, so these tools will make your life easier and allow you to start building more quickly.

Here are two tools used to develop WordPress locally and the steps required to get started.

### DevKinsta

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image-110.png)

DevKinsta is free software provided by Kinsta, launched in January 2021. I recently used it to launch a site and it was incredibly easy to use. 

It makes local site creation and development quick and easy for beginners. DevKinsta installs Nginx, MariaDB, and more with a single click. 

It takes about 2 minutes to install and get started building your local site, developing themes, experimenting with plugins, and doing custom PHP development.

Since it is a tool provided by a hosting provider, when you’re ready to go live the site is sent to Kinsta. For this reason, you should only use this tool if you choose to host your WordPress website with Kinsta. I currently host 20 sites for myself and clients on Kinsta and think they are incredible. 

### XAMMP

%[https://www.youtube.com/watch?v=h6DEDm7C37A]

Using XAMPP requires more steps than DevKinsta, but will teach you a lot about what services and libraries need to be running in order to support your WordPress website. 

XAMPP is an open source package that is free and easy to install. The Apache distribution contains MariaDB, PHP, and Perl. Once you download and install the software, you will have access to the XAMPP control panel app.

Using the XAMPP control panel, you can run Apache web server as your local server and MySQL as your database server. You will need to "Start" the Apache and MySQL modules from this panel to effectively turn your computer into a server. Voilà - you have a server!

In addition to XAMMP, you will need to download Wordpress from Wordpress.org. Extract the zip file to **.../XAMPP/htdocs/{here}**. With MySQL and Apache turned on, you should now be able to access your website from a browser at **https://localhost/wordpress/.** Voilà - you have the core WordPress files! 

Going to the above URL will prompt you to follow the WordPress installation wizard with one more critical technical installation - the database. 

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image-111.png)

The phpMyAdmin app comes pre-installed with XAMPP. You can access it at **https://localhost/phpmyadmin/**. This is where you will create your database using a simpler interface that you may already be familiar with. 

Click on **Databases** and then **Create** to quickly add a new database. Voilà - you have the database you need! 

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image-112.png)

Return to your local website at **https://localhost/wordpress/** and enter in your new database information, using "root" as your username and no password.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image-113.png)

Click Submit and the next screen will finalize your WordPress installation. You will be asked to pick a Site Name, Username and Password. After that, you can access the backend of your local WordPress website at **https://localhost/wordpress/wp-admin.**

Using XAMPP can be complicated. I have grown incredibly frustrated with some of my local installations but there is plenty of help to be found online. 

Going through the exercise of setting up a local WordPress installation will teach you important aspects of server configuration, database management, and how the core files of WordPress function. 

Once you are up and running, you can experiment and develop with no limits of using a server. 

## Conclusion

Developing WordPress locally is something that every WordPress developer should be comfortable with. 

Working from home and not commuting has provided me with some extra time in the day that I have allocated to building websites. I have been able to revisit and reevaluate my local development toolkit to more easily create WordPress websites. Hopefully my thoughts are helpful to you. 

We only covered two tools to use in this article. CodeInWP has additional tools that they recommend for developing locally. Once you have picked a local development stack, built a WordPress website, created a great design and logo, and picked a hosting provider - your creation will be ready for the internet. Happy building!

