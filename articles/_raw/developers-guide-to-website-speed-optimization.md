---
title: A Developer's Guide to Website Speed Optimization
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-12T16:07:06.000Z'
originalURL: https://freecodecamp.org/news/developers-guide-to-website-speed-optimization
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/Developers-Guide-To-optimize-website.png
tags:
- name: optimization
  slug: optimization
- name: Website performance
  slug: website-performance
seo_title: null
seo_desc: 'By Digvijay Singh

  I think a lot about how we can optimize our websites for speed. The world is getting
  busy and nobody likes to wait for a website to load.

  There are very few things a user can do to make a website go faster. But for developers
  like u...'
---

By Digvijay Singh

I think a lot about how we can optimize our websites for speed. The world is getting busy and nobody likes to wait for a website to load.

There are very few things a user can do to make a website go faster. But for developers like us, the possibilities are endless. The real optimization starts with the code and finishes on server side things like hosting, CDN's, caching and much more.

Here I have collected the best possible ways to optimize a website which I learned and implemented while creating a theme for my blog on Ghost CMS.

Here is a picture of the results.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/ghost-new-theme-speed-demo.png)
_Custom theme demo_

The theme is so fast because it contains no extra functionality other than what I need on a very minimal blog. I pay $5/month for cloud hosting. For now I've hidden the domain because its hosted temporarily (testing with some new things).

## Why Speed Matters

People are busy and they will not waste their precious time waiting for your website to load.

Website loading speed has been one of the most important factors in SEO since [April 2010](https://webmasters.googleblog.com/2010/04/using-site-speed-in-web-search-ranking.html). Users love fast websites where they can get useful information.

One more exciting thing about loading speed is that it affects your brand image. I can easily recall 3-4 superfast websites which load right after the click.

Suppose you are visiting a product site and it takes 10 seconds to load. Will you waste another 10 seconds in the billing page? How would this affect your trust? Will you trust a website which takes so much time to load?

> Think like a user before you act as a Developer.

Good websites load faster and users get the webpage in a flash.

## Different Speed Testing Tools

Now you know why we need to optimize our websites to load faster. Here is a quick overview of the tools which are popular in benchmarking performance.

### Your own browser

Yes, your browser has a powerful tool to let you know the loading speed of your website. I generally use it to get detailed information on the number of files (scripts and stylesheets) that load on each webpage request.

Open the developer’s tools of your browser (right-click then inspect) and then go to the networks tab. Reload the webpage with cache disabled and you will see the detailed statistics of loading speed.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/chrome-network-tools.png)
_Chrome network tools_

But this method is limited because it tests the loading speed from your location only. And we know that speed changes at different points around the globe.

### [Pingdom tools](https://tools.pingdom.com/)

Here is the solution for global speed testing: choose multiple locations from where to test your website loading speed.

It also provides a detailed report with recommendations you can use to further optimize.

### [Page Speed Insights](https://developers.google.com/speed/pagespeed/insights/) (Based on lighthouse)

Page Speed Insights created the belief that a score of 100 is must for SEO.

This is not completely true, though, because some of the most popular websites have a score less than 70.

Page speed insights use Lighthouse as their analysis tool and it's not directly related to SEO.

Lighthouse is an open-source website performance analysis tool. It audits the website for performance, SEO, accessibility, progressive web apps and much more.

Lighthouse is also available as a browser extension or [NPM package](https://www.npmjs.com/package/lighthouse) if you are developing a website locally.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/lighthouse-screenshot.png)
_Lighthouse website analysis report_

It gives some important optimizing details which other tools fail to report. It is very helpful to reduce the webpage size and optimize the loading speed of the website.

### [GTmetrix](https://gtmetrix.com/)

I find this much more accurate than other services. It gives accurate insights about the loading speed of your website. It also gives an in-depth report of the best practices which can further improve the performance of your website.

## The Best Ways to Optimize Website Loading Speed

Here comes the part where we'll start working on optimization. All these steps are very helpful in improving the performance of any website. 

But just remember that not all steps are necessary for everyone. You can skip the steps which might break your site (happens a lot during optimization).

### Avoid additional packages and scripts wherever possible

When I started web development, I preferred NPM install for each and every problem. But I was a noob :). Very soon I realised the cost of installing a new package for every problem I faced.

Using npm packages is good for rapid development but every new package comes with many additional functionalities which you might never need. 

The real problem lies in updating the project. Packages deprecate with time so managing a lot of packages is like a nightmare.

It's a good idea to try to solve basic problems by yourself instead of finding an NPM package to do it for you.

Here is a useful [VS Code extension](https://marketplace.visualstudio.com/items?itemName=wix.vscode-import-cost) that lets you know the size of the imported package.

The same thing applies to jQuery. There was a time when it was a must-have JavaScript library for each and every application. But now Vanilla JS stands strong.

If you can avoid using jQuery, it will save you about 30KB of additional loading to your webpage.

This website is helpful for finding jQuery alternatives: [Amazing collection of jQuery alternatives.](http://youmightnotneedjquery.com/)

I saved around 100ms only by removing jQuery from my Ghost CMS theme. It was a lot to work to replace jQuery with Vanilla Js but the result was awesome.

And it is good to say every script counts in performance.

### Remove unused CSS

CSS frameworks are very helpful in the rapid development of web applications. However, they have many components and styles which we never use in our projects.

[PurgeCSS](https://purgecss.com/) is very helpful in this case, as it removes the unused CSS from the stylesheet.

It is not as easy to use as it seems but it's worth the time investment. 

Just a heads up: sometimes PurgeCSS also removes the CSS which is useful to your projects. So I recommend that you manually verify and test the website properly after using it.

As an example, the dark theme of my website was broken because PurgeCSS removed the CSS variables as they were unused at that time.

### Minify CSS and JavaScript

You should minify Javascript and CSS files before pushing them to the production server.

Minify CSS and Javascript mean removing unnecessary code like comments, space, tabs from the file, because in production they are only for browsers to understand.

This reduces approximately 50% of the file size and enables your web pages to load much faster.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Minified-javascript-advantage.png)
_Minfied Javascript size reduced by 47%_

Here are online CSS and Javascript minifiers which you can use.

* [Online CSS Minifier](https://cssminifier.com/)
* [Online JavaScript Minifier](https://javascript-minifier.com/)

This is aother observation using Tailwind CSS with minify and purge CSS:

* Original size of stylesheet: ~150KB
* With Minify+Purge CSS: 4.9KB (and everything was working fine)

It was not a one-shot solution, though. Initially it broke many things (like night mode and many other functionalities triggered by Javascript) because purge CSS removed it as they were unused at that time.

I had to manually review and exclude those styles from the purge CSS plugin.

### Compress and resize images

Images are critical factors that affect the loading speed of any website. A lot of websites use high-resolution images even when they don't need it.

The perfect example is that you don't need a 2000 x 2000 image for a 250 x 250 author image.

Always consider cropping and compressing your images before you upload them to the web.

You can use online compression tools like [Tiny PNG](https://tinypng.com/) to compress images before using them on your website. You can reduce up to 60-70% of image size using image compression.

### Lazy loading images

As I said, images are critical factors in website loading speed. This means you must take the right steps toward optimizing images when loading them.

First, you can defer offscreen images. This means that the images after 1 viewport height will load once the user scrolls to them.

Lazy loading is also recommended and is very efficient in optimizing your website for fast loading.

It's helpful because sometimes the user doesn't need to scroll all the way to the bottom of the page and read all contents of your website. So lazy loading only loads images when the user scrolls to them.

You must implement lazy loading carefully and make sure JavaScript fallbacks are in place as an alternative.

You can take the example of Medium.com's articles for lazy loading of images. They put an image of very low resolution as a placeholder and load the original image once the user scrolls to it.

<p class="codepen" data-height="265" data-theme-id="dark" data-default-tab="html,result" data-user="malchata" data-slug-hash="mXoZGx" data-preview="true" style="height: 265px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;" data-pen-title="Lazy Loading Example">
  <span>See the Pen <a href="https://codepen.io/malchata/pen/mXoZGx">
  Lazy Loading Example</a> by Jeremy Wagner (<a href="https://codepen.io/malchata">@malchata</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://static.codepen.io/assets/embed/ei.js"></script>

### Defer JavaScript loading

You should always put all heavy scripts at the end of the page before the closing body tag.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Script Demo</title>
  </head>
  <body>
    <header>Some Beautiful Header that Rocks</header>
    <article> Some awesome Content ... </article>
    <section>Some more content...</section>


    <!-- This is Where all the heavy scripts and stylesheets should be present. -->
    <script src="js/scripts.js" defer></script>

  </body>
</html>

```

This is important because users can at least read the contents on slower connections while heavy scripts keep loading in the background.

This is one of the most common problems highlighted by Google speed insights. You can easily improve your score by implementing this step properly.

The defer attribute is helpful in this scenario, as it allows script execution only after the document is loaded.

### Select a good hosting provider

You can never expect good website loading speed on shared hosting of any low-quality hosting provider.

Go for VPS if you can afford it, or cloud hosting (they are as cheap as 5$ a month at Linode, Digital Ocean, and Vultr, for example).

Low quality hosting providers won't affect your website's speed much if you don't have many visitors. However, as the number of visitors grows they fail to handle such traffic.

That's why it is good to remain on the safe side and keep your website running on traffic spikes.

### Use a CDN

If your website has visitors from all around the globe, then CDNs will help deliver your assets quickly.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/CDN-vs-without-CDN.png)
_With CDN vs without CDN_

The users gets the assets from the nearest CDN node ensuring the shortest travel for data. This reduces the overall loading speed of the website and provides a consistent experience for all your users.

### Caching

Caching is the best possible solution for the fastest website loading speed. Cache as much as possible, but with care.

Caching on the server-side enables faster delivery of data and on the client-side empowers lightning-fast loading speed.

There are various resources like scripts, stylesheets, and some other common files which are used with every page load. We can cache them locally so next time they are fetched from the cache instead of the server.

Server-side caching prevents excess database operations each time and saves both time and money.

Just keep in mind that server-side caching is not suitable if you have too much dynamic data.

You must be careful with caching, though: if it's not implemented properly then the user may see the same old content each time they visit the site.

### Gzip compression

Gzip compression is one of the most common recommendations by the Pingdom speed test.

Gzip is a method of compressing files for faster delivery to your users. It is enabled by default by many hosting providers.

If you are using cloud hosting then you are on your own. But enabling Gzip compression will not only decrease the loading speed of your website but also reduce the bandwidth usage of servers.

Here is the code to add in configuration file to enable Gzip compression on Nginx server.

```nginx
gzip on;
gzip_disable "msie6";
gzip_vary on;
gzip_proxied any;
gzip_comp_level 6;
gzip_buffers 16 8k;
gzip_http_version 1.1;
gzip_types application/javascript application/rss+xml application/vnd.ms-fontobject application/x-font application/x-font-opentype application/x-font-otf application/x-font-truetype application/x-font-ttf application/x-javascript application/xhtml+xml application/xml font/opentype font/otf font/ttf image/svg+xml image/x-icon text/css text/javascript text/plain text/xml;
```

Here is the code to add in `.htaccess` file to enable Gzip on Apache server.

```apacheconf
<IfModule mod_deflate.c>
    AddOutputFilterByType DEFLATE application/javascript
    AddOutputFilterByType DEFLATE application/rss+xml
    AddOutputFilterByType DEFLATE application/vnd.ms-fontobject
    AddOutputFilterByType DEFLATE application/x-font
    AddOutputFilterByType DEFLATE application/x-font-opentype
    AddOutputFilterByType DEFLATE application/x-font-otf
    AddOutputFilterByType DEFLATE application/x-font-truetype
    AddOutputFilterByType DEFLATE application/x-font-ttf
    AddOutputFilterByType DEFLATE application/x-javascript
    AddOutputFilterByType DEFLATE application/xhtml+xml
    AddOutputFilterByType DEFLATE application/xml
    AddOutputFilterByType DEFLATE font/opentype
    AddOutputFilterByType DEFLATE font/otf
    AddOutputFilterByType DEFLATE font/ttf
    AddOutputFilterByType DEFLATE image/svg+xml
    AddOutputFilterByType DEFLATE image/x-icon
    AddOutputFilterByType DEFLATE text/css
    AddOutputFilterByType DEFLATE text/javascript
    AddOutputFilterByType DEFLATE text/plain
    AddOutputFilterByType DEFLATE text/xml
</IfModule>
```

[Source](https://www.keycdn.com/support/enable-gzip-compression).

### AMP for mobile

I read a [case study](https://kinsta.com/blog/disable-google-amp/) that AMP can affect your sales. But as I said earlier in the post you do not need to implement all steps in this post to make your website faster. Just choose wisely.

If you are running a publishing platform like a simple blog then you must go for AMP as it will only benefit you.

AMP also supports ads so this will have the least effect on your earning but the benefits are great. AMP has the fastest loading speed on mobile phones.

Here is a very basic AMP code. You can look [here](https://amp.dev/documentation/guides-and-tutorials/start/create/) for complete guide and best practices to create AMP version of your website.

```html
<!doctype html>
<html amp lang="en">
  <head>
    <meta charset="utf-8">
    <script async src="https://cdn.ampproject.org/v0.js"></script>
    <title>Hello, AMPs</title>
    <link rel="canonical" href="https://amp.dev/documentation/guides-and-tutorials/start/create/basic_markup/">
    <meta name="viewport" content="width=device-width,minimum-scale=1,initial-scale=1">
    <script type="application/ld+json">
      {
        "@context": "http://schema.org",
        "@type": "NewsArticle",
        "headline": "Open-source framework for publishing content",
        "datePublished": "2015-10-07T12:02:41Z",
        "image": [
          "logo.jpg"
        ]
      }
    </script>
    <style amp-boilerplate>body{-webkit-animation:-amp-start 8s steps(1,end) 0s 1 normal both;-moz-animation:-amp-start 8s steps(1,end) 0s 1 normal both;-ms-animation:-amp-start 8s steps(1,end) 0s 1 normal both;animation:-amp-start 8s steps(1,end) 0s 1 normal both}@-webkit-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@-moz-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@-ms-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@-o-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}</style><noscript><style amp-boilerplate>body{-webkit-animation:none;-moz-animation:none;-ms-animation:none;animation:none}</style></noscript>
  </head>
  <body>
    <h1>Welcome to the mobile web</h1>
  </body>
</html>
```

### Wordpress specific optimizations

#### Fewer plugins

Plugins are the power of WordPress. Or I should say that plugins are the curse of WordPress.

Both depend on the number and quality of plugins you use on your site.

The number of plugins directly affects the loading speed of your website. I always recommend that you use only the necessary plugins and avoid the rest.

#### A minimal theme will do the work

Let me tell you that your "Popular Wordpress theme" has inbuilt support for most of the popular WordPress plugins that you may never use.

Yes, this is the truth. They have a large number of customers to target so they built a one-stop solution for all (really?).

You should go with a minimal theme which is dedicated for a particular purpose.

If there is no theme that fits best then it is good to create your own theme from scratch. This will be a time-consuming process but it will load assets specific to your needs and will definitely have great speed benefits.

#### Use Autoptimize plugin

This is a simple plugin that solves most of the problems with stylesheets and JavaScript files. I got +20 score in Google speed insights right after installing this plugin.

It caches, defers and auto-minifies CSS and JavaScript files which improves page loading speed.

#### Do you really need WordPress?

I know this topic should not be here under WordPress optimizations. But it is important to ask yourself if you really need WordPress.

I love WordPress because it is mature and best for beginners. But sometimes I think it's too heavy for simple tasks.

WordPress is really heavy in its core because it has features for everyone. Whether you want to use these features or not they are there running and eating server resources.

If you need a simple publishing platform with no complex integrations, then these options are good alternatives.

* Ghost CMS (freeCodeCamp News uses it)
* Netlify CMS (Getting popular with Static Site generators).
* Gatsby, Hugo, Jekyll (Static site generators)

I wanted to include Strapi in the list, but it lacks tutorials and demo. It will get its own place in future web development as its community increases.

To demonstrate the effect here is a screenshot of the speed index on my current site on WordPress and a migrated version on Ghost CMS with a custom theme.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Wordpress-Neve-theme-performance.png)
_WordPress Theme performance with 3 additional plugins Installed only for Speed._

![Image](https://www.freecodecamp.org/news/content/images/2020/05/ghost-cms-custom-theme-performance.png)
_Ghost CMS custom theme_

I am by no means biased with anything. There are use cases for each. WordPress can handle complex things easily while Ghost wins for its simplicity and static site generators win on speed.

You can choose the alternatives to WordPress as per your needs.

## In the end: don't over-optimize

Optimizing is good but you should not try to be strict with all the steps. As I mentioned earlier, there is a high chance that certain steps might break your site and lead to hard debugging sessions.

Write out all the steps and then decide if each step is suited for your website or not.

Again, in the end over-optimization is usually bad. Speed is really necessary but on the other hand user experience (UI and UX) also matters a lot.

A good website maintains amazing speed with great UI and UX.

> I  can send you more articles like this with our [Weekly Newsletter](https://holycoders.com/newsletter/).

