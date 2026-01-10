---
title: Why you should use GatsbyJS to build static sites
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-04T22:31:57.000Z'
originalURL: https://freecodecamp.org/news/why-you-should-use-gatsbyjs-to-build-static-sites-4f90eb6d1a7b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*c4wjZPrF_3AnRMUZd5tlpw.png
tags:
- name: education
  slug: education
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Ajay NS

  Gatsby has been growing over time, and I’m glad to see it in use by a huge number
  of sites like marketing sites, blogs, and generated static pages.

  What attracted me in the first place was the smooth development experience, incredible
  resu...'
---

By Ajay NS

Gatsby has been growing over time, and I’m glad to see it in use by a huge number of sites like marketing sites, blogs, and generated static pages.

What attracted me in the first place was the smooth development experience, incredible results, and the warm community. Going a bit in-depth into its workings, the ecosystem and also discussing its potential with more developers made me think about how powerful it is — much more than I had initially presumed.

This article seeks to make you see why it has gained popularity. If you’re already using it, you’ll get a better idea of the features that you could put to use for an even greater development experience.

Do note that this is what works for me, and I’m sharing just my views. I’m in no way telling you that your current setup that works for you is obsolete, but just trying to share how Gatsby has been great for me.

### What is Gatsby?

It’s another static site generator like Hugo, Jekyll and so on. So what makes it special? Why are we talking specifically about it?

Gatsby can be used to build static sites that are Progressive Web Apps, follow the latest web standards, and are optimized to be highly performant. It makes use of the latest and popular technologies including ReactJS, Webpack, GraphQL, modern ES6+ JavaScript and CSS.

![Image](https://cdn-media-1.freecodecamp.org/images/1*yCPN-lvsZ7k2WcRsPQYjqA.png)
_GraphQL + React + Webpack = ❤_

This means a lot of developers can jump in without much of a learning curve as they already know or have at least used one piece of this tech stack Gatsby is built on.

Furthermore, I’d like to add something I noticed working with developers who had no idea about the latest frameworks and libraries and were just used to the traditional HTML, JavaScript, CSS files way of building sites.

#### Approach to development

On one side, we have users expecting an app-like smooth experience on the web. The other side is developers, used to sites having pages with each being HTML files or maybe using some templating — at the very base — _sites as pages with internal linking_.

If you’re getting started with any of the latest frameworks, let’s take the case of React. You could have an app up and running with minimal configuration with [create-react-app](https://github.com/facebook/create-react-app). But if you take a look at the project structure it may not make much sense to a newbie or even some developers coming in from other tech stacks. The pattern is pretty different from what you’ve ever seen before.

It’s because without additional setup they aim at building Single-Page Applications, SPAs. To add routing, pages or optimizing for SEO, it will require more tools and configuration.

That doesn’t seem very convenient when you want static sites, does it? So here we have Gatsby, optimized for this specific use case. This could be more intuitive for developers, as there are pages created from components that follow the root idea that sites are pages with internal linking.

### Features

#### Components

Components are a key feature of React, and now they’re a commonly followed web design pattern. With the current level of complexity of user interfaces, it is almost impossible to write maintainable code in long pages of HTML or use templating engines and expect consistency.

So instead, we build reusable components and then use them to construct views. This way we have separate modules handling separate things, and it’s easier to manage and maintain. The component just contains all the information it requires, and Gatsby, since it uses React, follows the same pattern.

Atomic design is an approach that’s a good way of handling complex interfaces, and we could put it to use here with React components. Brad Frost has an amazing [blog post](http://bradfrost.com/blog/post/atomic-web-design/) describing what it is and how it works.

#### **Webpack bundling and latest tooling**

Webpack creates optimized, minified bundles of HTML, JavaScript, and CSS. When it’s pre-configured with Babel and more plugins, it allows you to use the latest ES6+ JavaScript and GraphQL.

Icing on the cake: we’ve got hot reloading and code splitting built-in, giving a better development experience and better site performance. This is aimed at making the developer write minimal tooling configuration and focus more on the actual site development.

#### **Gatsby plugins, starters and React packages**

You can use any of the packages you’ve already been using with NPM, particularly the React ones as it’s built on the same thing. But that’s not all: there’s a large number of ever-growing plugins, starters, and transformers by the Gatsby community.

You almost never come to the point where you actually have to build on your own tool or module, the community already offers a huge number to suit every need.

Using these, Gatsby can be extended with additional functionality. For instance, a couple of examples include responsive images, offline functionality, source data from CMS and data markup formats, adding third-party services (Google analytics etc), and so on.

#### Styling

Again, complex user interfaces mean complex styling patterns, and it’s only a matter of time before style-sheets get bloated. You get specificity issues, scroll through hundreds of lines of code trying to figure out things, and end up using `!important` to actually see the styling you added.

Gatsby has support for SCSS, CSS-in-JavaScript libraries, allowing you to manage styles better and with ease. Even the setup for this is fairly easy to handle with the installation of a plugin or package.

#### Responsive Images

Resizing images for responsiveness on different devices, lazy-loading, using `srcsets` and `picture`…Already sounds tedious when it is to be done manually.

![Image](https://cdn-media-1.freecodecamp.org/images/1*yhkSz2qqhyRZ-HpATSQx6Q.png)
_Different versions of the same image for responsiveness_

Although it is a requirement for performance and app-like optimized interfaces these days, we don’t see many tools that we can directly jump into and use.

Meanwhile, in Gatsby with just a plugin, particularly the [gatsby-plugin-sharp](https://www.gatsbyjs.org/packages/gatsby-plugin-sharp/), you can directly generate fluid images, add filters, change formats, blur up on load and a lot more. This saves a lot of work and time manually resizing images and writing explicit boilerplate code for responsive images. It also gives you way better performance along with a smoother user experience.

#### **App-like experience**

With the performance boost and features to add to the smoothness of the user experience, Gatsby aims at a full app-like experience borrowing from full PWAs. There are no reloads between pages when using [gatsby-link](https://www.gatsbyjs.org/docs/gatsby-link/) instead of hyperlinks, and the app still appears smooth and performant thanks to lazy-loading images and code-splitting.

For sites following standards that you also want to be performant, we’ve got tons of things to do and guides to follow: minification and bundling, browser caching and async loading scripts or files, and so on. When working with a framework like React, you have more things to worry about even though it solves a couple of problems: code-splitting, SEO, routing if required, responsive images, and the list goes on.

Gatsby aims to solve all these problems, with less time spent on tooling, configuration, and the environment and more time to actually design and develop the site.

### The Gatsby Ecosystem

#### Plugins

Gatsby was built to be extensible and flexible — using plugins is one way to make it so. They can be directly installed and be used for a variety of functionality including making the site offline, adding Google analytics, adding support for inline SVGs, you name it — the list is almost endless.

Of the different types of Gatsby plugins, the gatsby-source plugins in particular fetch data from a local or remote source and allow it to be usable via GraphQL. These sources could be CMSs such as Wordpress, Drupal, Plone, local markdown, XML or such files, databases, APIs and data formats as JSON, CSV.

This implies that almost anything at all can be used as a source to work with Gatsby and generate static sites.

> Note: GraphQL is a query language for APIs that works on the philosophy of just asking for exactly what you require. Unlike REST APIs, you don’t look for endpoints to provide your data and process them from the structure that’s given from it, but rather ask for what you want and directly use this data. Read more about how it works and how to use it in their [docs](https://graphql.org/).

After installation, some plugins can be used straight away by just listing them in `gatsby-config.js` and the others configured with an options object.

Go check out the [Gatsby plugin library](https://www.gatsbyjs.org/plugins/), it’s already got quite a large number of plugins and more are being added still by the active community.

#### Starters

These are basically boilerplate Gatsby sites which help you kick-start development quickly depending on what kind of site it is. They help you directly get onto working on the development of a site, configuration and basic features you need already taken care of. Which means, less time on the tooling, more time for development.

Gatsby plugins often have their corresponding starters which show or serve a quick way to get started with using it. They also act as a reference covering all the features and showcase configurations of the plugin in use.

![Image](https://cdn-media-1.freecodecamp.org/images/1*0EB7BqFJb70XAGAqt0LgRw.png)
_[Gatsby Starter library](https://www.gatsbyjs.org/starters/?" rel="noopener" target="_blank" title=")_

_Gatsby themes is a feature still in development which allows you to package and reuse these functionalities and patterns similar to what’s seen in starters. Read more about what’s brewing in the [Gatsby blog](https://www.gatsbyjs.org/blog/2018-11-11-introducing-gatsby-themes/)._

#### Static Sites

Firstly, let’s take a look at how Gatsby works internally. Unlike the SPAs that make API requests as you run the app, Gatsby does all the data fetching, including data sourcing from local files, during build time. All this data is then used to generate static HTML, JavaScript, and CSS files. This static rendering is what makes things work faster.

![Image](https://cdn-media-1.freecodecamp.org/images/1*8JLlG_T6onoeW2mVjVT_Gw.png)
_How Gatsby works_

That was a lot about Gatsby, its ecosystem and how it helps you create amazing static sites. But why would we want static sites? Doesn’t it sound like a step back from dynamic ones?

* They do not require complex server setup with databases, maintenance, and don’t have any scaling issues.
* Data is fully secure. CMSs and APIs have private features but the data is still present in the server which can be exploited. Gatsby only takes the required data to display from the source and the private or secured data is not even present in the final build. Which is the safest it can possibly get.
* Rather than relying on servers to generate pages dynamically, pre-render all of them on build and use CDNs for a blazing fast and smooth experience for users all around the globe.
* Gatsby does static rendering. Which makes content available as HTML, and search engine optimized, no long initial load time.

#### Try it out!

That should have shed some light on what’s all the hype around it and why some major companies are choosing to use it on their sites. The [Gatsby site showcase](https://www.gatsbyjs.org/showcase/) just seems to be growing with many amazing additions lately.

Maybe it’s time you dipped your hands and took a look around!

Thanks to [CodeSandbox](https://codesandbox.io), we can do this right away, in the browser itself.

If you’d like to run it locally, you should check out the [gatsby-cli](https://www.gatsbyjs.org/docs/). It is the quickest and easiest way to get started. They’ve also got amazing documentation and tutorials for you to dive into developing sites on [gatsbyjs.org](https://www.gatsbyjs.org/docs/).

_Hope you enjoyed this article and found it to be worthwhile. You can check out all my projects on [Github](http://github.com/ajayns/) or [Dribbble](https://dribbble.com/ajayns) and don’t hesitate to reach out to me on [Twitte](https://twitter.com/ajayns08)r!_

_You also might like to take a look at my other articles:_

[**Progressive Web Apps: Bridging the gap between web and mobile apps**](https://medium.freecodecamp.org/progressive-web-apps-bridging-the-gap-between-web-and-mobile-apps-a08c76e3e768)  
[_Unless you’ve been living under a rock, you’ve probably heard of PWAs or Progressive Web Apps. It’s a hot topic right…_medium.freecodecamp.org](https://medium.freecodecamp.org/progressive-web-apps-bridging-the-gap-between-web-and-mobile-apps-a08c76e3e768)[**Hackathon Report: What can you code in 30 hours? Quite a lot!**](https://medium.freecodecamp.org/hackathon-report-what-can-you-code-in-30-hours-quite-a-lot-ffd7224c9745)  
[_What can you build in 30 hours straight? As a group of second year college students with a growing portfolio of work…_medium.freecodecamp.org](https://medium.freecodecamp.org/hackathon-report-what-can-you-code-in-30-hours-quite-a-lot-ffd7224c9745)[**ACM Month Of Code 2k17: Building Moodify**](https://hackernoon.com/acm-month-of-code-2k17-building-moodify-d5d9e0c52ca7)  
[_March was a pretty productive month, all thanks to this major event hosted by Association for Computing Machinery, NIT…_hackernoon.com](https://hackernoon.com/acm-month-of-code-2k17-building-moodify-d5d9e0c52ca7)

