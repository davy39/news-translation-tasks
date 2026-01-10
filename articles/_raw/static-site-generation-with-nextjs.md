---
title: What is Static Site Generation? How Next.js Uses SSG for Dynamic Web Apps
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-11-18T17:49:33.000Z'
originalURL: https://freecodecamp.org/news/static-site-generation-with-nextjs
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/static-generation.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Next.js
  slug: nextjs
- name: Static Site Generators
  slug: static-site-generators
seo_title: null
seo_desc: "Static websites are as old as the web itself. But the rise of JavaScript\
  \ has opened the door to make those static sites more dynamic. \nWhile that can\
  \ include building an HTML file by hand, how can we leverage static generation to\
  \ build apps with mode..."
---

Static websites are as old as the web itself. But the rise of JavaScript has opened the door to make those static sites more dynamic. 

While that can include building an HTML file by hand, how can we leverage static generation to build apps with modern tools?

* [What is Static Generation?](#heading-what-is-static-generation)
* [What happens during Static Generation?](#heading-what-happens-during-static-generation)
* [How does Next.js use Static Generation?](#heading-how-does-nextjs-use-static-generation)
* [Statically generating an app with Next.js](#statically-generating-an-app-with-next-js)

%[https://www.youtube.com/watch?v=6ElI2ZJ4Uro]

## What is Static Generation?

Static Generation describes the process of compiling and rendering a website or app at build time. The output is a bunch of static files, including the HTML file itself and assets like JavaScript and CSS.

If you haven’t heard of Static Generation but that concept sounds familiar, you might have heard of it by its longer name Static Site Generation or its acronym SSG.

## What happens during Static Generation?

JavaScript-based web apps as we traditionally know them work by running libraries like React or scripts at run time in the browser. 

When the browser receives the page, it’s usually simple HTML without a lot of content. This then loads the scripts to pull the content into the page, a process also known as hydration.

With Static Generation, tools like Next.js try to render that page mostly like it would in the browser but at compile time. This gives us the ability to serve the entire content on first load. The scripts still hydrate the page during this process, but ideally with fewer changes or no changes at all.

## How does Next.js use Static Generation?

Out of the box, Next.js will attempt to statically generate any pages that it can. It does this by detecting how an app is fetching its data.

Next.js provides a [few different APIs to fetch data](https://nextjs.org/docs/basic-features/data-fetching) including `getStaticProps` and `getServerSideProps`, which, depending on how they’re used, determines how Next.js will build your app.

If you only use `getStaticProps` to fetch data, Next.js will fetch that data at build time, leaving you with a completely static page. 

If you use `getServerSideProps`, Next.js will know that the app requires a server to render those pages. 

Alongside a deployment solution like Vercel that [will automatically handle configuring a server](https://vercel.com/solutions/nextjs), Next.js will load any of the data when someone requests the page from the server.

While it doesn’t do it by default, Next.js also provides the ability to export the app into static files into a separate directory after the app has been built.

First, you would run the `next build` command to build the app, then you would run `next export` which, by default, makes the app available as static files in the `out` directory.

## How to statically generate an app with Next.js

To get an idea of how this works, we can quickly create a new Next.js app.

The only requirements for this is that you have [Node](https://nodejs.org/en/) installed with npm and the ability to use a terminal to run commands.

### How to create a Next.js app

Getting started is as simple as running a single line in the terminal.

Open up the directory you’d like to create your project in and run:

```
npx create-next-app my-static-nextjs-app

```

After the installation is complete, you can navigate to your new project directory:

```
cd my-static-nextjs-app

```

Once there, start your development server:

```
npm run dev

```

And once the server is ready, you can open up [http://localhost:3000](http://localhost:3000) in your browser where you can now see your new Next.js app!

![Image](https://www.freecodecamp.org/news/content/images/2020/11/new-nextjs-app.jpg)
_New Next.js app_

### How to build a Next.js app

Now that we have our application available, let’s try to build it.

In the same directory, run the command:

```
npm run build

```

If you look at the output inside of the terminal, we see a few important things happen.

First, Next.js lets us know that it’s running through its build process, including optimizing the app for performance, compiling the app, and collecting data.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/nextjs-build.jpg)
_Building with Next.js_

Next, we see that Next.js shows us a breakdown of how it’s built each page.

The default Next.js starting template includes a few static pages and an example API route. 

Using the legend at the bottom, we can see that all of the pages and assets were statically generated with one route tagged as requiring a server, which would be our API route.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/nextjs-static-generation.jpg)
_Next.js generating pages_

_Note: For the purposes of this walkthrough, we can ignore the API route, but Next.js along with Vercel provides the ability to build lambda functions as part of the Next.js API._

### How to build a static Next.js app

With our Next.js build output, we know that we just built some static pages, but we might have trouble finding them. If we look at the folders and files in our project, it’s not immediately clear where those files are.

When Next.js builds an app, by default, it only outputs that app inside the `.next` directory. This includes configuration files that tools like Vercel can use and understand to deploy the app.

Technically, that directory includes our entire app, but this isn’t something we can easily deploy to static hosting.

Next.js also provides the ability to export an app. This will take the app that we built and produce a set of static files which we can then use to deploy our app.

Inside of the `package.json` file, update the `build` script to include `next export`:

```
"build": "next build && next export",

```

Once updated, run the build command again in the project directory:

```
npm run build

```

And now we can see that not only did we build the app like we did in our last step, Next.js lets us know that we’re also exporting the app that we built into static files.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/nextjs-exporting-static-app.jpg)
_Exporting static Next.js app_

If we look inside of our project folder, we should now see a new directory called `out`.

If we look inside of that folder, we can now see our entire app statically compiled including the `index.html` file as well as all of the CSS and JS needed to use the app!

![Image](https://www.freecodecamp.org/news/content/images/2020/11/nextjs-static-output.jpg)

## Where can we go from here?

We learned that we can use Next.js and the concept of Static Generation to statically compile an app. 

Tools like Next.js can do this by compiling our code, similar to what we might see in a browser, so that by the time our app hits the browser, it’s all ready to go.

With a simple command, we can also build and compile our app, as well as export it into static files. We can deploy those static files to any static storage service like Vercel or AWS S3. This provides us with an easy way to craft dynamic web apps that are fast and cheap.

Learn more about how Next.js leverages its different APIs to provide both static and dynamic experiences by [visiting the Next.js docs](https://nextjs.org/docs/basic-features/data-fetching).

<div id="colbyfayock-author-card">
  <p style="margin: 1em 0;">
    <a href="https://jamstackhandbook.com/" style="display: block;">
      <img src="https://www.freecodecamp.org/news/content/images/size/w1600/2020/11/jamstack-handbook-banner.jpg" alt="Jamstack Handbook" style="width:100%;display: block;margin: 0;border: solid 1px #d2dee9;">
    </a>
  </p>
</div>

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Follow me for more Javascript, UX, and other interesting things!" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">🐦 Follow Me On Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">📺 Subscribe To My Youtube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;">📫 Sign Up For My Newsletter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://github.com/sponsors/colbyfayock" style="text-decoration: none;">💝 Sponsor Me</a>
    </li>
  </ul>
</div>

