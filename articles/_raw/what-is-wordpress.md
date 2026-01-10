---
title: What is WordPress? The Blog and Website Tool Explained
subtitle: ''
author: Jim Campbell
co_authors: []
series: null
date: '2020-11-23T19:48:14.000Z'
originalURL: https://freecodecamp.org/news/what-is-wordpress
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/wordpress.jpg
tags:
- name: beginners guide
  slug: beginners-guide
- name: Blogging
  slug: blogging
- name: PHP
  slug: php
- name: WordPress
  slug: wordpress
seo_title: null
seo_desc: "WordPress is the world’s most popular content management system, powering\
  \ about 38% of all websites. A content management system or CMS is software that\
  \ helps users create and manage content on a website with minimal technical knowledge.\
  \ \n\n“The basic..."
---

WordPress is the world’s most popular content management system, powering about 38% of all websites. A content management system or CMS is software that helps users create and manage content on a website with minimal technical knowledge. 

> “The basic WordPress software is simple and predictable so you can easily get started. It also offers powerful features for growth and success.” - WordPress.com

In short, WordPress is a reliable way to create a powerful website.

WordPress is easy to install and comes packed with functionality out of the box. The core features of WordPress have everything that you need to set up a website with pages, blog posts, navigation, and user management. 

But the real power of WordPress is the extensive options to quickly design a beautiful website with pre-built Themes and add incredible functionality with optional Plugins.

In this article we will cover the basics of WordPress including:

* WordPress’ origin and popularity
* Building the basics with Pages and Posts
* Improving design with Themes
* Extending functionality with Plugins

## Why is WordPress So Popular?

WordPress is used by about half a billion other websites, including recognizable names such as TechCrunch, The New Yorker, Variety, the official site of Sweden, and The Walt Disney Company. 

_Tip:_ to see if a site is running WordPress, you can View Page Source and search for “WordPress” or “wp-” and if you see directories such as “wp-includes” or “wp-content”, the site is running WordPress.

WordPress is still growing like crazy with over 500 new sites built everyday. 

Over the past three years, WordPress’ market share of software powering websites has grown by about 8% from 27.3% in 2019 to 35.2% in 2020.

Amazingly, WordPress now powers more websites than websites that do not use any CMS:

![Image](https://lh5.googleusercontent.com/bb4ZuDI2RZ71zvzMBLvczjjpzHybK-zs4X6CSnmU4WTaDrQLJ9yB4CUPKnxE40JjnT7AVibNXJGGGXgHeDF92C5Geb4JUBPVI9ENNmxLahaS_7M8sE8veN6NZ657PyKoAG9c41lr)
_Percent of All Websites Not Using a CMS vs. Percent of Sites Using Wordpress. There are more websites using WordPress than websites powered by a CMS. Source: w3techs_

One of the main drivers of WordPress’ popularity is that it is **free**. WordPress is licensed under the [GPLv2](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html), which means it is free to use and modify by anyone. 

WordPress is estimated to have had over 100 years of developer time contributed to the open source project.

## WordPress Basics – Pages and Posts

Setting up a WordPress website involves selecting a domain name, finding a hosting provider, and installing WordPress.

Installing WordPress sets you up with a fully functioning website. But unlocking the real power of WordPress comes with installing Themes, Plugins, and customizing the site. 

But let’s start with the basics.

Upon installing WordPress, you will be asked for a username and password. Your credentials can be used to access the admin backend of your website. This can be accessed at _yourdomainname.com/_**wp-admin**. 

The admin section looks like this:

![Image](https://lh5.googleusercontent.com/OpFPebq7IBpYQNAk1DnWbq3HI9mwgFKVKJrSAJtZm_U7RnAQr75AS_XPvwQrTyjTqcNMB0wLeB1-GTj5wNGn9ga8wUEsNa3TbQp5XBR74h5j8hxyGscQTEHVdFr36zeQirwKZGqx)
_The WordPress admin backend. Source: WordPress_

As you can see, WordPress comes loaded with features that are accessible via the left navigation. For the purposes of this article, let’s discuss the two important content types Pages and Posts.

### WordPress Pages

Pages allow you to quickly build web pages. By adding this type of content, you can create webpages at _yourdomain.com_/**newpage**.

WordPress has a built in editor that you can use to quickly format text and multimedia into a great looking webpage. The editor is built with “blocks” so that instead of worrying about the alignment and organization of the content, you can focus on creating. 

This is what editing content and adding blocks in WordPress looks like:

![Image](https://lh4.googleusercontent.com/BHBC2-MeN7JPjJMuAucwwwX-zYEu1bxNDtbrJci1K0PCwwT3Dt21HC0Jdo-v7Fa7bsAXpWLxJjLkogEA65AscfAV8OyLszAa-DdXH4e71byZ5DEoFg3CiFv8ieGNxfonvJAj1eNz)
_Easily insert different “blocks” like code into your Pages and Posts._

While the default WordPress Editor is great, it can be enhanced with Plugins and even replaced with content builders that make it easier to drag and drop content in a visual way such as Elementor, Visual Composer, or WP Bakery. The beauty of WordPress is that it is **infinitely customizable**.

Whatever editor you choose to use, using WordPress’ built-in Pages allows you to easily create dynamic and gorgeous web pages. 

### WordPress Posts

The Posts section has the same Editor as the Pages section, except this content category creates blog posts. Posts are at the core of WordPress because the software began as a blogging tool.  

Posts utilize the same content Editor as Pages, so creating Pages and Posts is the same experience. 

The main difference between Pages and Posts is volume. Let’s say a typical small business website will have 5-10 core pages (Home Page, About Us, Contact Us, Services, and so on). That same company could have 100s of blog posts.

To manage the high volume of Posts, WordPress comes with extensive categorization and hierarchy management. Posts can be easily organized into Categories.

![Image](https://www.freecodecamp.org/news/content/images/2024/08/pasted-image-0--2-.png)
_Example of categories to organize posts._

![Image](https://www.freecodecamp.org/news/content/images/2024/08/Screen-Shot-2020-11-21-at-9.39.10-AM.png)
_Example of hierarchies to organize posts._

You can add and nest as many categories as you need. With Categories, content can be displayed hierarchically on your website such a _yourdomainname.com_/**guides/best-business-practices/**_**yourcontent**._ 

Since WordPress is so highly customizable this "permalink" structure can also be easily changed in the Settings tab.

### Custom Post Types (advanced)

WordPress comes pre-loaded with the two main content types (Posts and Pages) but many users want to further customize their content types.

For example, if you want to build a travel website that has a directory of hotels, a custom post type called "Hotels" would be a great addition. 

These custom post types leverage WordPress' built-in Editor, categories, and other features of the Posts and Pages. As such, custom post types are a way to quickly develop a dynamic website. 

Custom post types can be added via a Plugin or by adding some code into the core _functions.php_ file. These additions are great example of how WordPress is **extremely customizable** and a **great platform to develop your coding skills**.   

![Image](https://www.freecodecamp.org/news/content/images/2024/08/pasted-image-0--1-.png)

![Image](https://www.freecodecamp.org/news/content/images/2024/08/pasted-image-0-1.png)
_Custom posts like Hotels and Products can be added into WordPress to better organize content and enhance the functionality of your custom WordPress site._

## WordPress Themes - Looking Good Is Easy 

Once you’ve set up your WordPress website, the next step is selecting a Theme. 

A theme is a collection of templates and stylesheets that define the appearance and functionality of a WordPress website. 

WordPress comes preloaded with a standard Theme but very few websites actually use this Theme (or hundreds of millions of sites would look the same!)

Themes allow WordPress users to very quickly have a great looking website. In about 10 minutes you can have a website that has the same backend, engine, and look like great sites such as TechCrunch. All that’s missing is the content!

One of the best parts of building a WordPress website is selecting a Theme due to the variety of designs and options. There are thousands of themes available.  


![Image](https://lh6.googleusercontent.com/K-rtleZSuRBt0F5fybx-H-R79LqI3T_NSeHacyKwFVFT5wd0vr8Ex3e4JkL6gnQMcmGRvCRoILWrz7HLs_1FY45w1bb1j6y4EWucCTHRyNVNj7gco7MQfMM_3D2j5isbghzN3ycw)

Premium Themes can typically be purchased for between $20 and $60. You can download a zip file and easily upload it to WordPress. Once the Theme is activated, your WordPress website adopts the templates and stylesheets. And just like that, you have a professionally designed website!

_A word of caution_: Theme selection can be tricky and there are many things to consider before installing. I would recommend looking for Themes that have high ratings (someone else has tested it), minimum Plugin dependencies, and are fast. 

To test the speed, find a demo of the Theme on the developers website and run it though Google Page Speed. If the Theme performs poorly, don't use it.

Once you select a great base Theme, you have the option to **endlessly customize it**. You can completely customize your site by editing the Theme file with HTML, PHP, CSS, and JavaScript. 

The easiest way to do this is to install a child theme so that you can still update your theme with the latest version.

With a great Theme, you can have a beautiful website. Plugins add the power.

## WordPress Plugins Make it More Than Just a Blog

WordPress’ history is rooted in personal publishing and blogging. The project started in 2003 when Mike Little and Matt Mullenweg began working on an “elegant and well-architected personal publishing system.”

But WordPress is now much more than just a blog.

WordPress has over 50,000 Plugins available. WordPress Plugins are PHP scripts that extend the functionality of the core content management system. They can add entirely new features to your site.

Plugins are developed by volunteers and companies. They are typically free and many have premium versions.

Beware of installing too many Plugins, as maintaining the updates can be a never-ending task for WordPress webmasters. 

![Image](https://www.freecodecamp.org/news/content/images/2024/08/Screen-Shot-2020-11-21-at-10.00.34-AM.png)

![Image](https://www.freecodecamp.org/news/content/images/2024/08/Screen-Shot-2020-11-21-at-10.01.45-AM.png)
_Plugins can be uploaded and updated directly from the admin backend._

## Wrapping It All Up

WordPress is a great tool to use to build a website. It is fast, reliable, and extendable.

While WordPress started as a simple publishing tool, it has grown far beyond its humble beginnings. Whether you are looking to create a personal blog, an ecommerce store, or a website for your business, WordPress is a great option.

Additionally, WordPress is a great way to start learning more about web development. 

When you start building in WordPress you will be coding with HTML, CSS, Javascript, PHP, and MySQL. Since WordPress is open source and insanely popular, there are a ton of free resources ([including right here on freeCodeCamp](https://www.freecodecamp.org/news/search/?query=wordpress)) to go as deep as you want.

