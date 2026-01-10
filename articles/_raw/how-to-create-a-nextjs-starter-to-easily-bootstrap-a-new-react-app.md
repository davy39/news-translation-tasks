---
title: How to Create a Next.js Starter to Easily Bootstrap a New React App
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-08-18T15:33:48.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-nextjs-starter-to-easily-bootstrap-a-new-react-app
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/nextjs-starter.jpg
tags:
- name: Next.js
  slug: nextjs
- name: React
  slug: react
- name: Sass
  slug: sass
seo_title: null
seo_desc: "Getting started with a new React app is easier than ever with frameworks\
  \ like Next.js. But those frameworks don’t always include all of the tools you want\
  \ to use. \nHow can we use Starters to become super productive when starting a new\
  \ project with ou..."
---

Getting started with a new React app is easier than ever with frameworks like Next.js. But those frameworks don’t always include all of the tools you want to use. 

How can we use Starters to become super productive when starting a new project with our favorite tools?

* [What is Next.js?](#heading-what-is-nextjs)
* [What is a Starter?](#heading-what-is-a-starter)
* [What are we going to build?](#heading-what-are-we-going-to-build)
* [Adding Sass to a Next.js Starter](#heading-adding-sass-to-a-nextjs-starter)
* [Setting up Next.js Starter documentation for easy setup](#heading-setting-up-nextjs-starter-documentation-for-easy-setup)
* [Some other things to consider](#heading-some-other-things-to-consider)

%[https://www.youtube.com/watch?v=oFGs_x7kxZg]

## What is Next.js?

[Next.js](https://nextjs.org/) is an application framework from [Vercel](https://vercel.com/) that allows you to very quickly bootstrap a new [React](http://reactjs.org/) application.

Some basic features include creating [pages](https://nextjs.org/docs/basic-features/pages) and [data fetching](https://nextjs.org/docs/basic-features/data-fetching), and they allow you to generate a static site or use server side rendering to dynamically load your app. 

On top of that, you can take advantage of its advanced features like [Routing](https://nextjs.org/docs/routing/introduction) or creating an [API](https://nextjs.org/docs/api-routes/introduction) right next to your UI.

## What is a Starter?

Starters are basically a git repository in the form of a template that allows you to easily create a preconfigured app.

There’s nothing necessarily special about a Starter. At it’s core, it’s a Next.js app that’s already been set up a specific way and typically generalized so that anyone can use it.

For example, if you tend to build lots of apps the same way each time, you might have to repeat those same configuration steps every time you create a new app. 

Instead, you can create a Starter from where you'll start your projects – and it'll eliminate the need to repeat those first steps each time.

## What are we going to build?

We’re going to build a basic Next.js Starter that will let you or anyone else quickly and easily create a new project with that Starter as a starting point.

While we won’t go too heavy into features, as the goal here is to learn about Starters, we’ll test this out by adding [Sass](https://sass-lang.com/) to Next.js so someone can easily get started with CSS superpowers.

You can check out the [Starter](https://github.com/colbyfayock/next-sass-starter) on GitHub: [github.com/colbyfayock/next-sass-starter](https://github.com/colbyfayock/next-sass-starter).

## Creating a new Next.js Starter

To get started with creating a Starter, we need to start with a Next.js app.

We can do this by running the following command in whatever directory you want to create this in:

```
yarn create next-app
# or
npx create-next-app

```

Once you run that, Next.js will ask you for a project name. While you can use whatever you like, Next.js Starters typically have a name pattern of `next-[name]-starter`.

So because we’re creating a Sass Starter, I might call it `next-sass-starter`.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/command-line-new-nextjs-app.jpg)
_New Next.js app in the terminal_

Once Next.js has installed all of our dependencies, you’ll be ready to navigate to that folder and run the command to start your development server.

```
yarn dev
# or
npm run dev

```

And once the development server starts up, we should be ready to go!

![Image](https://www.freecodecamp.org/news/content/images/2020/08/new-nextjs-app-browser.jpg)
_New Next.js app in the browser_

At this point, we pretty much have a basic Starter. As mentioned before, there really isn’t much that’s actually special with a Next.js Starter. So if we pushed this up to Github, we could immediately start using it “as is”.

You can test this out by running the following:

```
yarn create next-app [project-name] -e [GitHub URL]
# or
npx create-next-app [project-name] -e [GitHub URL]

```

After running that, you should be set up with a new directory that has a project created from your Starter with all of the dependencies installed.

But we want to do more than that. Our goal is to add features that help get an app started with more than the default, so let’s add Sass.

[Follow along with the commit!](https://github.com/colbyfayock/next-colbyfayock-starter/commit/ed87ce9d6585b2b642adf7e6878d0fc01bba05ef)

## Adding Sass to a Next.js Starter

Note: For our example, we’re going to create a Sass starter as the name above might have implied. Feel free to add any features you want at this point, whether it includes Sass or not. 

Remember – the goal here will be to provide something that we’ll be able to use when creating a new project with this Starter.

Next, we want to actually add Sass to our project. To get started, we want to install sass as a dependency:

```
yarn add sass
# or
npm install sass

```

Next, because Next.js already looks for `.scss` as a file extension, we can simply update out two CSS files under the `styles` directory to `.scss`.

So change the following files:

```
styles/globals.css => styles/globals.scss
styles/Home.module.css => styles/Home.module.scss

```

Next, we need to set up our import statements to recognize our new file extensions.

In `pages/_app.js`, update the styles import at the top to:

```scss
import '../styles/globals.scss'

```

And in `pages/index.js`, update the styles import to:

```scss
import styles from '../styles/Home.module.scss'

```

At this point, you can start your development server and we should still see the default Next.js page.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/new-nextjs-app-browser.jpg)
_Next.js app should look the same_

To see our Sass in action, we can update some of our classes to use nested styles instead of individual selectors.

Update all of the `.footer` selectors inside of `styles/Home.module.scss` to the following:

```scss
.footer {

  width: 100%;
  height: 100px;
  border-top: 1px solid #eaeaea;
  display: flex;
  justify-content: center;
  align-items: center;

  img {
    margin-left: 0.5rem;
  }

  a {
    display: flex;
    justify-content: center;
    align-items: center;
  }

}

```

You can use the same nesting structure to update `.title` and `.card`.

We can also add the following to the top of our `styles/Home.module.css` file:

```scss
$color-primary: #0070f3;

```

And update all instances of the color in that file from `#0070f3` to `$color-primary`:

```scss
.title {
  ...
  a {
    color: $color-primary;

```

If you reload the page, nothing will change. But update that variable to your favorite color like:

```scss
$color-primary: blueviolet;

```

And now all of the colors change.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/nextjs-app-updated-colors.jpg)
_Updated colors in the Next.js app_

Finally, since we now have a Sass starter, let’s update the title of the page. Replace “Welcome to Next.js!” In `pages/index.js` to:

```jsx
<h1 className={styles.title}>
  <a href="https://nextjs.org">Next.js</a> Sass Starter
</h1>

```

And now we have a Sass starting point!

![Image](https://www.freecodecamp.org/news/content/images/2020/08/nextjs-app-updated-title.jpg)
_Updated title in the Next.js app_

Similar to before, you can test this out by creating a new project with your starter once all of the changes are on GitHub.

```
yarn create next-app [project-name] -e [GitHub URL]
# or
npx create-next-app [project-name] -e [GitHub URL]

```

[Follow along with the commit!](https://github.com/colbyfayock/next-sass-starter/commit/56c5b67e8a383d8dc89c72d88cbe86adbac3edb8)

## Setting up Next.js Starter documentation for easy setup

Arguably one of the most important things about a Starter is documentation. 

It might not be as important if you’re only using this yourself. But if you want other people to use it, you want them to know how to use it or else they’ll get stuck and become frustrated.

The most important part is getting the Starter set up. Setting up your Starter in a GitHub repo is a great first step. But if someone wants to use that Starter, they would have to clone or download that repo and then remove the git history.

Instead, you can add the command we used above in your `README.me` file to give people instructions on how to quickly get started, such as:

```mdx
## Getting Started

Run the following command to create a new project with this Starter:

```
yarn create next-app [project-name] -e https://github.com...
# or
npx create-next-app [project-name] -e https://github.com...
```

```

This will prevent people who might not understand how to do some of those things manually from getting stuck.

It’s also important to add any documentation of configuration options you’ve added.

If you’re adding some variables that allow you to change some site-wide features, make sure to add notes about those. 

You ultimately want people to understand how to use the features you added to make their lives easier. If they don’t understand it, they may just rip that code out and do it manually.

Ultimately, creating and publishing a Starter is about making people’s lives easier. Whether it’s you coming back to your Starter a few months later or a swarm of new people looking to get productive, you’re giving them a better developer experience by adding good documentation.

## Some other things to consider

### Generalizing features and adding configuration for a Next.js Starter

Adding features is a great way to make a Starter more likely to be used. If I used a Starter to create a new blog, I would love if that Starter included my name as an author and maybe even an About Me page.

But what I wouldn’t want is to have to replace someone else’s name 100 times throughout the code to update my own project. Not to mention, seeing that name on the Starter might make me feel more like it’s their blog rather than a template I can use for my project.

Consider starting off by using a generalized name throughout the project. Instead of using Colby Fayock’s Blog throughout the Starter, make it My Blog, which will make it feel less personal to the creator for the person using the Starter.

Also add some configuration options. It’s much easier to be able to update a single variable that would make my project include Colby Fayock instead of My Blog than it is to search all files to make that change manually.

### Choose carefully where to be opinionated

When using a tool like Sass, there is more than one way to use that tool. If you set up an incredibly specific and opinionated project structure, you’re alienating people using your Starter. 

It'll either force them to rework the entire project or make them want to delete a bunch of code which might make them avoid wanting to use it in the future.

You can create opinionated Starters, but choose wisely where you inject those opinions. This will make your work usable by a larger group of people who want to be productive.

If you want to create something very opinionated, consider naming it something different and using the tool as part of the name. For example, I could create an opinionated Sass Starter called Colby’s Sassy Next.js Starter.

## Did you create a new Starter?

[Share with me on Twitter!](https://twitter.com/colbyfayock)

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Follow me for more Javascript, UX, and other interesting things!" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">? Follow Me On Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">? Subscribe To My Youtube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;">✉️ Sign Up For My Newsletter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://github.com/sponsors/colbyfayock" style="text-decoration: none;">? Sponsor Me</a>
    </li>
  </ul>
</div>

