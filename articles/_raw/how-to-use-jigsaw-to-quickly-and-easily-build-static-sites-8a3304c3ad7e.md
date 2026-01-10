---
title: How to use Jigsaw to quickly and easily build static sites
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-04T21:54:10.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-jigsaw-to-quickly-and-easily-build-static-sites-8a3304c3ad7e
coverImage: https://cdn-media-1.freecodecamp.org/images/0*CCMaHN9JpmvIFNdi
tags:
- name: Laravel
  slug: laravel
- name: PHP
  slug: php
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Rick West

  Let’s dive in to Jigsaw — a framework for rapidly building static sites using the
  same modern tooling that powers Laravel applications.

  Static sites aren’t a new concept. However, fully fledged, dynamic, Content Management
  System (CMS’s)...'
---

By Rick West

#### Let’s dive in to Jigsaw — a framework for rapidly building static sites using the same modern tooling that powers Laravel applications.

Static sites aren’t a new concept. However, fully fledged, dynamic, Content Management System (CMS’s) such as Wordpress, Drupal and Joomla, seemed to have taken over. That is, until fairly recently, where there has been a resurgence in the popularity of Static Site Generators such as Jekyll, Hugo, Pelican and now Jigsaw.

Whilst CMS’s do provide a powerful and useful tool to serve the user in certain situations, the tendency has become that developers try to shoehorn CMS’s into situations where they simply do not belong, or at least don’t fit the intended use case.

As its name suggests, a ‘Content Management System’s’ primary aim is to do just that, manage content. And they are excellent at doing that, especially in situations where bloggers, content marketers, and site owners need to update their website on a regular basis.

However, as a solution for building a brochure style marketing site for a business or a simple personal blog/portfolio? In my opinion? Not so great.

### What is a Static Site Generator?

Put simply, a Static Site Generator is an application that takes content (commonly written in Markdown), applies it to templates, and generates a set of purely static HTML files, ready to be delivered to visitors.

Static Site Generators combine the power of modern tooling and templating libraries with the ease of static HTML web pages.

The deployable output from a Static Site Generator requires no execution or interpretation by a web server.

![Image](https://cdn-media-1.freecodecamp.org/images/0*CCMaHN9JpmvIFNdi)
_Image Source ([https://www.slideshare.net/mackato/blogging-on-jekyll](https://www.slideshare.net/mackato/blogging-on-jekyll" rel="noopener" target="_blank" title="))_

### Advantages of a Static Site Generator

#### Tried and Tested Technology

Static Site Generators output static files that comprise only of HTML, CSS, and JavaScript. This means that they require no processing by a server and can be served directly from the web server’s file system exactly as stored. This is fast, uncomplicated, tried and tested technology.

#### Minimal Inexpensive Hosting

Static Site Generators most commonly run on your local machine, and then the output can be pushed up to a simple web host — any web host will do, since they’re just going to be serving static files. Therefore, static sites can be hosted totally free on platforms such as [Github Pages](https://pages.github.com/) or [Netlify](https://www.netlify.com/).

#### Security

One of the biggest threats of developing with a dynamic CMS is the lack of security. Their need for bigger server-side infrastructure opens the way for potential breaches.

Because a static site has no database layer, and little to no server side functionality, there is no exposure of additional attack surfaces.

#### Speed and Performance

Because Static Site Generators build already compiled files which are then served to the browser, without having to dynamically pull information from a database there is very little load time resulting in exceptional performance in the majority of cases.

#### Flexibility

The resurgence in the popularity of Static Site Generators is probably coupled to the gain in popularity of JavaScript.

JavaScript can now perform many of the same duties as regular server side scripting languages such as PHP or Python.

This has in turn led to much greater flexibility in static sites, such as being able to easily integrate with external web services such as analytics, form submission/mailing list sign-up options and payment gateways.

Whilst Static Site Generators may initially ask for more technical skills from a developer, compared to just producing static pages or using a CMS, we are also rewarded with infinitely more freedom.

### Static site options for PHP Developers

There are hundreds of Static Site Generators available but if, like me, PHP is your primary programming language, then that helps to narrow down the options significantly.

Choosing a tool written in a language that you are familiar with is pretty important when considering the learning curve, extensibility, debugging and development or your project.

Using [https://www.staticgen.com/](https://www.staticgen.com/) I was able to get a nice comparison of the most popular PHP Static Site Generators.

![Image](https://cdn-media-1.freecodecamp.org/images/0*sA3Jpj2t1OPIqn9s)
_A comparison of PHP Static Site Generators from [https://www.staticgen.com/](https://www.staticgen.com/" rel="noopener" target="_blank" title=")_

As you can see from the image, [Sculpin](https://sculpin.io/) and [Jigsaw](https://jigsaw.tighten.co/) are quite clear favourites.

Sculpin was first released in 2012 so is a mature, solid choice, built on top of [Symfony](https://symfony.com/) components.

Jigsaw, on the other hand, was released in 2015 by the team at [Tighten](https://tighten.co/) and leverages several Laravel components, such as Blade and Laravel Mix.

Being built on top of Laravel, and considering the notable popularity and community surrounding [Laravel](https://laravel.com/), this makes [Jigsaw](https://jigsaw.tighten.co/) a really exciting option ?.

With that said, let’s dig into Jigsaw a little further…

### Jigsaw — A framework for rapidly building static sites using the same modern tooling that powers your Laravel application.

![Image](https://cdn-media-1.freecodecamp.org/images/1*gyYn7QH6v4SVAt0tdB5h6Q.png)

### What is Jigsaw

Developed by the team at [Tighten](https://tighten.co/), [Jigsaw](https://jigsaw.tighten.co/) is a Static Site Generator that utilises components from the [Laravel](https://laravel.com/) framework for building static websites.

These components include the Blade templating engine, Collections and Laravel Mix for handling assets.

> “Static sites for Laravel developers.

> Jigsaw is a framework for rapidly building static sites using the same modern tooling that powers your web application.”

Considering all this, it was no surprise to me that Jigsaw ‘feels’ a lot like Laravel. Very clean, expressive syntax, easy to set up, infinitely powerful and everything ‘just works’ ?.

Let’s face it, the Laravel blueprint is a tried and tested one, it’s the most popular backend framework for a reason. So with Jigsaw utilizing Laravel components and embodying the Laravel ethos, it is definitely off to a great start.

![Image](https://cdn-media-1.freecodecamp.org/images/1*fwXQdEaEeAOttQL1gS_h1w.png)
_[https://jigsaw.tighten.co/](https://jigsaw.tighten.co/" rel="noopener" target="_blank" title=")_

### Getting started with Jigsaw

As part of the research I did into Jigsaw (this was originally a uni project that I’ve turned into a series of blog posts!), I reached out to [Keith Damiani,](https://medium.com/@rickwest8/jigsaw-my-interview-with-keith-damiani-senior-developer-at-tighten-and-lead-developer-on-the-55ead103514d) a Senior Developer at Tighten, who is also the lead on the Jigsaw project. In his own words, [Keith describes Jigsaw](https://medium.com/@rickwest8/jigsaw-my-interview-with-keith-damiani-senior-developer-at-tighten-and-lead-developer-on-the-55ead103514d):

> _“It’s definitely targeted at developers who are comfortable in the Laravel ecosystem, as it draws so heavily on Blade; so for someone who writes Laravel (or even PHP) all day, it’s a natural choice that involves a pretty short learning curve to get up and running.”_

Awesome.

To use Jigsaw, you just need PHP 7, Composer, Node and NPM installed on your machine. All of which are standard tools, as part of a modern PHP development workflow.

Getting up and running from there is then pretty simple, as the quality of the [Jigsaw documentation](https://jigsaw.tighten.co/docs/installation/) really is fantastic.

Installing Jigsaw all the way to previewing something in your browser can be achieved in as little as 4 simple steps:

1. Install Jigsaw via Composer:

```
composer require tightenco/jigsaw
```

2. Initialise your Jigsaw project:

```
./vendor/bin/jigsaw init
```

3. Generate your site by running the build command:

```
./vendor/bin/jigsaw build
```

4. Preview your site with PHP using the serve command:

```
./vendor/bin/jigsaw serve
```

Boom! This highlights just how easy it is to get started with Jigsaw. As I mentioned before, it ‘just works’!

Let’s take a further look at some other important aspects of the framework…

### Ecosystem and Support

[Tighten](https://tighten.co/), the driving force behind Jigsaw, is an integral part of the wider Laravel ecosystem as well as being an official ‘[Laravel Partner](https://laravel.com/partners)’.

With Jigsaw being built on top of, and therefore tightly coupled to, some of the Laravel components, this Tighten/Laravel connection bodes very well for Jigsaw and its future development.

Tighten and many members of its staff are also well known within the PHP/Laravel community for several other fantastic [open source projects](https://github.com/tightenco), producing online tutorials and hosting podcasts.

Being backed by such a passionate, prominent and successful company is a great sign of encouragement, and already Tighten is building a community around the Jigsaw project. In fact, they have already created [Built With Jigsaw](https://builtwithjigsaw.com/), a website to collect and showcase some of the great examples of projects built with Jigsaw, along with community resources and other interesting use cases of Jigsaw.

It is also worth noting that when [I reached out to Keith](https://medium.com/@rickwest8/jigsaw-my-interview-with-keith-damiani-senior-developer-at-tighten-and-lead-developer-on-the-55ead103514d) regarding interviewing him for my project, he was more than happy to take some time out of his day to answer a few of my questions. This willingness to engage directly with someone from the wider community (a random stranger from the UK) really emphasised to me just how committed to the community and enthusiastic the Jigsaw team is. Credit to Keith and the attitude of Tighten as a whole.

### Performance and Scalability

During my [interview with Keith](https://medium.com/@rickwest8/jigsaw-my-interview-with-keith-damiani-senior-developer-at-tighten-and-lead-developer-on-the-55ead103514d), he revealed that they know several developers who have built some very large sites (with 6,000+ pages) using Jigsaw.

The Jigsaw team have also been working on optimising the build times of Jigsaw, which will be especially of interest to those who maintain, or plan to build, large Jigsaw sites as it cuts build times down by about 75%.

### Features, flexibility and extensibility

Jigsaw ships complete with many features that aid the rapid development of static websites.

Referring to the [brilliant documentation](https://jigsaw.tighten.co/docs/installation/), I have summarised some of these primary features below:

#### Blade

The backbone of Jigsaw is the Blade templating engine. One of the biggest benefits of a templating language is template inheritance, the ability to create reusable layouts and partials. This dramatically reduces code duplication and lowers development time.

![Image](https://cdn-media-1.freecodecamp.org/images/1*bQxQDqNIR00k4v_WC9AI1Q.png)
_Blade example, take from [https://jigsaw.tighten.co/](https://jigsaw.tighten.co/" rel="noopener" target="_blank" title=")_

#### Markdown

As with many Static Site Generators, Jigsaw supports content written in Markdown. Markdown is a fantastic writing format for things like articles, blog posts, and documentation pages.

Jigsaw makes it painless to create a layout in Blade, and fill it with content written in Markdown.

#### Laravel Mix

Out of the box, Jigsaw comes with Laravel Mix configured and ready to use. Laravel Mix provides a fluent API for defining Webpack build steps for your application using several common CSS and JavaScript preprocessors.

As a Junior Developer, and someone with limited exposure to Webpack and modern front-end tooling, Laravel mix takes all the stress away and makes getting started with Webpack and asset compilation a breeze.

#### Events

This pull request [https://github.com/tightenco/jigsaw/pull/189](https://github.com/tightenco/jigsaw/pull/189) added 3 events to Jigsaw that you can hook into, in order to run custom code before and after the application build is processed.

The three events are ‘beforeBuild’, ‘afterCollections’ and ‘afterBuild’.

Registering an event listener is very simple, and these events offer a great opportunity to add custom code. This would be particularly useful, for example, in the event of wanting to pull in content from an external API-based CMS like [Contentful](https://www.contentful.com/) or in [generating an automated sitemap](https://mattstauffer.com/blog/adding-an-auto-generated-sitemap-to-your-jigsaw-based-static-site/) after the site is built.

#### Collections

Jigsaw provides powerful features for working with groups of related pages, or collections. Collections give you the ability to access your content at an aggregate level, enabling you to easily add near-dynamic features like menus, pagination, categories, and tags to your static site.

Collections can be used to generate pages of related content — for example, blog posts or articles that are sorted by date, with an index page displaying summaries of the five most recent posts — or for embedding related blocks of content within a page, for content like staff bios, product descriptions, or a portfolio of projects.

#### Packages

Although not officially released yet, the Jigsaw/Tighten team are working on a couple of starter template for Jigsaw. One for a blog and one for documentation style website.

Working with designer [Steve Schoger](https://twitter.com/steveschoger), there is no doubt that these templates will look pretty awesome, but this is also a great indicator that the team is taking the first steps in making Jigsaw extensible with the addition of an external plugin ecosystem.

No doubt that once the integration of plugins is possible, the Jigsaw and Laravel communities will start finding ways to extend Jigsaw in many innovative ways!

### Summary

Jigsaw is a stable, performant and inherently secure framework packed full of powerful and easy to implement features that make our lives as developers easier and therefore happier ?.

It’s so easy to get started with, having such a low barrier to entry for someone familiar with modern PHP development, that you can take a project from ‘jigsaw init’ to being hosted for FREE on Netlify or Github Pages in no time at all.

In my opinion, two of the most important factors when considering any framework or library are the quality of the documentation and also the ecosystem and support surrounding it.

In these cases, Jigsaw excels, above and beyond expectations. I found the documentation to be clear, concise and well presented and the community and support surrounding Jigsaw is second to none (other than perhaps Laravel itself!).

**Make sure to give Jigsaw a try in your next project, or when you finally get around to building that blog you keep talking about.**

**No more excuses. Jigsaw is awesome.**

_*As part of my research for this article, I reached out to [Keith Damiani](https://twitter.com/keithdamiani), a Senior Developer at Tighten, who is also the lead on the Jigsaw project._

_Keith was kind enough to answer a few of my question regarding the development of Jigsaw and the plans for the future._

_You can read that full interview here…[https://medium.com/@rickwest8/jigsaw-my-interview-with-keith-damiani-senior-developer-at-tighten-and-lead-developer-on-the-55ead103514d](https://medium.com/@rickwest8/jigsaw-my-interview-with-keith-damiani-senior-developer-at-tighten-and-lead-developer-on-the-55ead103514d)_

Thank you for reading! ? If you enjoyed it, hit that clap button below. I really appreciate your support and it helps other people see the story.

I am always happy to hear from like minded people, so feel free to shoot me an email or say hello on [Twitter](http://twitter.com/rick_west8).

