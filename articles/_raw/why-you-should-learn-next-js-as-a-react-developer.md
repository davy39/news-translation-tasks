---
title: Why You Should Learn Next.js as a React Developer
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-10T16:42:06.000Z'
originalURL: https://freecodecamp.org/news/why-you-should-learn-next-js-as-a-react-developer
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/fccposter.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Next.js
  slug: nextjs
- name: React
  slug: react
seo_title: null
seo_desc: "By Mehul Mohan\nWe can all likely agree on one thing: React is one of the\
  \ most popular solutions out there for building interactive web applications, both\
  \ small and large. \nAnd it is used by so many startups and companies that it is\
  \ a very valuable sk..."
---

By Mehul Mohan

We can all likely agree on one thing: React is one of the most popular solutions out there for building interactive web applications, both small and large. 

And it is used by so many startups and companies that it is a very valuable skill to have these days.

I discovered Next.js a couple of years back, and was intrigued with what it was trying to accomplish. 

In this post, I'll describe my personal journey with Next.js. I'll also discuss why I believe that it is the right time to add it to your React stack.

## The Early Web

Back in the mid-2000s, when the web was young and growing, developers moved from static only HTML pages to more robust and dynamic solutions. 

This gave us the ability to create pages with dynamic content using tech like PHP (mind you, JavaScript was very young and non-performant at this time). 

You could have a single **profile.php** page and it would take care of Alice, Bob, John, Mehul, and all 15,000 registered people on your website – very convenient.

Then came the JavaScript age. People started realizing that there was this language supported for the web which could be used for so much. 

You could set up dynamic form submission, background HTTP requests, nice scrolling effects, and even create webpages on the fly. 

The rise of JavaScript and libraries like jQuery allowed web developers to create nice interfaces fully customizable with JavaScript.

Soon, every web developer started pushing more and more JavaScript down the network to the client. Sure, technology evolved, mobile phones and PCs became better with more RAM and cores, but JavaScript started evolving faster. 

More functionalities, more features, and more frameworks meant a better user experience and the ability to create an app-like feeling on the web. 

But this also meant pushing more and more JavaScript down the network on devices that could not keep up with evolving JavaScript limits.

## The Web was made for HTML

![Image](https://www.freecodecamp.org/news/content/images/2020/08/meme.jpg)

Old, slow mobile devices started giving up - load times became high, there was more lag, JS engines were less powerful, and there was just so much JavaScript to parse!

With frameworks like React and Angular, you're basically pushing huge JavaScript bundles to clients which first have to download the small HTML pages.

Web developers who moved from the PHP age (server-rendered HTML) to the JavaScript age (client rendered HTML) soon started realizing that they screwed up big time. 

React was great for interactivity and high-performance components, but the fact that people starting using these tools to build **everything** started to create problems for clients. 

A simple **About Us** page, which could be a very simple static HTML/CSS page, was now a page with a whopping JS bundle. The browser first had to download, then parse, then execute, and then change the DOM to display the content.

This was bad for everyone. Clients had higher load times. Browsers had to work hard to run JS (browsers parse and run HTML/CSS very efficiently). And search engines like Google and Bing had a hard time understanding what your page was about, because your source code never contained the real content. It was always embedded somewhere in your JS bundle.

People loved React and similar tools. But they also understood the implications of running too much JS client-side. 

On the other hand, they loved how PHP worked, but they didn't like its architecture. So what was the solution?

## Server-Side Rendering (SSR) – the best of both worlds

When developers realized that pushing too much React code on the client was a problem, they thought: Hey, is it possible to code in React, but ship HTML documents to clients? 

After all, when the React code is done executing, all you really have is an HTML document anyway. 

So they did it. Server-Side Rendering (SSR) for React was born.

Now, with SSR, you can write React code, somehow run it on the server (which was more powerful than your typical client device – like a mobile phone), and then send the HTML document to the client.

Win-win for everybody. You, as a developer, get to code in React - the technology you love. And the visitor on your site gets a plain HTML document (with visible content, and a little rehydrated JS), which gets a massive performance boost. Plus, Google loves you now. 

Who wouldn't want that?

## But it was too difficult

Server-side rendering definitely seemed like the solution to this problem. But the problem? It was too difficult to set up correctly. 

Proper caching and cache-busting? Could you possibly create static HTML files for pages that didn't change? How should you build a seamless navigation experience on your website even if you have server-side rendered HTML? How should you ease down the load on your servers, or generate on-demand content? 

And on top of all this, how do you set up this whole architecture? Sure, React and the web provides all the APIs for these, but they are quite verbose and usually a one-time setup. 

If you're someone who's actually building something valuable, after some time you would want the majority of your time to be spent on the **business logic** of your application, and not on the underlying logic.

## Introducing Next.js

Next.js is a framework born in heaven. It ships with:

1. Best SEO practices
2. Caching and Automatic Static Optimization built-in
3. Fully server-rendered pages
4. 100% React support
5. Lambda function support (API routes)
6. Fine tweak your webpack/babel config if needed
7. And much more!

It abstracts away all those performance and development setups you need with a typical React app and allows you to focus only on what matters – your business logic code. 

I had my first experience with Next.js 2 years ago when it was very young.

But Next.js 9.5 was released this year with so many features. And I think it's safe to say that it is one of the most powerful tools available in the web development ecosystem, especially if you're a React developer. 

I run codedamn (a platform for developers to learn to code) myself on Next.js. There's a massive performance boost to the site compared to your regular React app.

If you're a React developer in 2020, one of the best skills you can learn is Next.js. Here are some benefits it offers you as a developer:

1. Definitely an emerging technology – more job opportunities and possibilities
2. Server rendered pages means better performance – more clients for you
3. SEO for your websites baked in – search engines love you
4. All the benefits of having a server in place – API routes, dynamic content fetching, and stale-while-revalidate feature (oh I love this one)
5. A great technical skill on your résumé

## Some Next.js features I'm excited about

Next.js is evolving really fast. They deprecate old functionalities and introduce shiny new things all the time. 

As of today, I'm super interested in the framework as a whole, but here are some of my top picks:

### #1 Stable Incremental Static Regeneration

Simply speaking, this feature allows you to generate static content _dynamically._ Wait, what? Let's see a quick example:

Say you have a blog website (like this one) with a lot of articles. When somebody visits `/news/[link]` (where `[link]` is anything), you want to serve them the static page as fast as you can. 

But it is possible that you don't want to create _all_ static pages at build time because it would take you a lot of time. In a few cases, this isn't possible at all at build time.

Also, sometimes your content _might_ change, like a quick blog edit - so you don't really want a completely static page forever either. So what's the solution?

Using Next.js 9.5+, now you can generate static pages dynamically to the dynamic path and refresh them. 

This means that once Next fetches that particular URL, it'll save it as a static page and serve it statically whenever somebody visits the path. At the same time, it'll be open to accepting new paths dynamically. 

Not only can you do this, with a revalidate parameter, you can also actually specify that Next.js should update your static pages once every X seconds in the background if there's any change!

### #2 Webpack 5 Support

Next.js is heading towards Webpack 5 support too. This is exciting as Webpack 5 brings in some sweet performance and bundle optimizations and drops support for deprecated things in webpack 4, making the core _lighter_. 

That means your Next.js apps will be faster than ever and more robust.

### #3 Dropping of getInitialProps

I personally didn't like the concept of having a single function execute on both environments - getInitialProps. 

Thankfully, Next.js figured out that there's a much better solution available and they brought in getServerSideProps and getStaticProps as two great methods with good names.

`getServerSideProps`, as the name suggests, allows you to inject props in your Next.js page from the server itself. And `getStaticProps` allows Next.js to still create static outputs at build time. 

`getStaticProps` combined with incremental static regeneration is a killer feature in my opinion. You get the many benefits of a dynamic backend without having a dynamic backend.

### #4 Persistent Caching for Page Bundles

Next.js now also supports persistent caches for pages that are not changed. Before, when you shipped a new Next.js app, Next.js would throw out the whole app and the user had to download all the CSS/JS again, even if those bundles were unchanged. 

In the latest version of Next.js released last week, our friends at Vercel introduced persistent caching which is again an absolutely great thing to have performance-wise.

### #5 Out of the box support for Sass Modules and TypeScript

If there's one thing I love more than JavaScript, it is TypeScript. And Sass is sweet too. Most people I know use Sass to power their CSS, and it provides a great developer experience. 

Next.js has long offered great support for TypeScript out of the box. But recently they added **module based support** for Sass as well. 

This means that your styles can now be written in Sass, local to your modules, with caching and revalidation - all managed by Next.js internally.

Seems like they really want you to develop the best products focusing only on the business logic.

## Learning Next.js [a Course]

I'm creating an exclusive video course on Next.js with best practices, latest framework updates, and super cool things you can do with it. I'm including a bunch of full projects with the framework so you'll get a deep understanding of how to work with this tool.

If you're interested, sign up for early access using this [Google form link](https://forms.gle/5eZAR3rZvexzBcno7) and I'll make sure to reach out to you when it's out.

## Conclusion

I'm going all in on Next.js. The speed with which they're iterating and developing the SSR concept and making it available to so many is just astonishing. 

If you signed up using the form link above, expect to hear from me soon with some awesome content for you.

Feel free to hit me up on social media to share what you think: [Twitter](https://twitter.com/mehulmpt) and [Instagram](https://instagram.com/mehulmpt).

