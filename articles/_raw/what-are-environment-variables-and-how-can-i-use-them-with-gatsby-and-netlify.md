---
title: What Are Environment Variables and How Can I Use Them with Gatsby and Netlify?
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-04-28T14:45:00.000Z'
originalURL: https://freecodecamp.org/news/what-are-environment-variables-and-how-can-i-use-them-with-gatsby-and-netlify
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/environment-variables.jpg
tags:
- name: continuous deployment
  slug: continuous-deployment
- name: deployment
  slug: deployment
- name: Gatsby
  slug: gatsby
- name: GatsbyJS
  slug: gatsbyjs
- name: Git
  slug: git
- name: JavaScript
  slug: javascript
- name: Netlify
  slug: netlify
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: React
  slug: reactjs
- name: technology
  slug: technology
seo_title: null
seo_desc: "When starting to integrate 3rd party services into your application or\
  \ website, you'll start to find it useful to have different environments, such as\
  \ a development and production environment. \nHow can we configure this so we don't\
  \ have to directly e..."
---

When starting to integrate 3rd party services into your application or website, you'll start to find it useful to have different environments, such as a development and production environment. 

How can we configure this so we don't have to directly edit our code to change our environment?

* [What are environment variables?](#heading-what-are-environment-variables)
* [How can environment variables be useful?](#heading-how-can-environment-variables-be-useful)
* [How can I keep these files secure?](#heading-how-can-i-keep-these-files-secure)
* [Gatsby and environment variables](#heading-gatsby-and-environment-variables)
* [Netlify and environment variables](#heading-netlify-and-environment-variables)
* [Step 1: Creating a "Hello, world" website](#heading-step-1-creating-a-hello-world-website)
* [Step 2: Creating a local environment variable with Gatsby](#heading-step-2-creating-a-local-environment-variable-with-gatsby)
* [Step 3: Deploying the website to Netlify](#heading-step-3-deploying-the-website-to-netlify)
* [Where can you add or update more variables in Netlify?](#heading-where-can-you-add-or-update-more-variables-in-netlify)

%[https://www.youtube.com/watch?v=oq_RPOI0xsU]

## What are environment variables?

Environment variables are predetermined values that are typically used to provide the ability to configure a value in your code from outside of your application.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/environment-variable-secret.jpg)
_MY_SECRET_KEY environment variable used for authorization_

When developing locally, or sometimes even in a deployment pipeline, you'll oftentimes find these variables stored in a file named with some kind of variation of  `.env`.

## How can environment variables be useful?

Probably the most common use case for environment variables is being able to set up different configuration options for different environments. Often when developing against third party services, you want to have a development version or sandbox available to make test requests against, that way it doesn't impact real production data.

Environment variables are helpful because they allow you to change which of your environments use which third party service environment by changing an API key, endpoint, or whatever the service uses to distinguish between environments.

The code you deploy should be predictable, so by not having to change any code, just the configuration outside of the code, you can maintain that predictability.

## How can I keep these files secure?

This is probably one of the more important points here – you need to ensure you're handling these files with care and not checking them into a git repository. By exposing these keys by inadvertently uploading them to a public location, the internet could easily find these keys and abuse them for their own gains.

For instance, [AWS](https://aws.amazon.com/) keys are a valuable source. People run bots with the sole purpose of trying to scan Github for keys. If someone finds an AWS key, they could use this key to access resources such as running a bitcoin operation at your expense. This isn't to scare you, its to make you aware so you avoid your keys getting compromised.

So how can we keep these secure? The easiest way is to add the environment file where you keep these keys to your `.gitignore` file.

To do this, simply open your existing `.gitignore` file or create a new one at the root of your repository and add the filename as a new line:

```
# Inside .gitignore
.env

```

If you want to get more advanced and make sure this never happens to a repository, you can check out some tools like [git-secrets](https://github.com/awslabs/git-secrets) from AWS Labs or [GitLeaks](https://github.com/zricethezav/gitleaks) that even has a [Github Action](https://github.com/marketplace/actions/gitleaks) to make it easy to integrate with Github.

## Gatsby and environment variables

[Gatsby](https://www.gatsbyjs.org/) by default makes two files available as part of its [environment variable workflow](https://www.gatsbyjs.org/docs/environment-variables/) that makes these values available in the client: `.env.development` and `.env.production`. These correlate to the `gatsby develop` and `gatsby build` scripts to either develop or build your site.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/environment-variable-secret-gatsby.jpg)
_MY_SECRET_KEY environment variable for development and production_

To make use of these files within the Gatsby development and build process, Gatsby requires you to prefix these variables with `GATSBY_`. This also works if you'd like to have them available from an OS process level.

Though you could integrate [dotenv](https://github.com/motdotla/dotenv) if you have more advanced needs or don't want to use the `GATSBY_` prefix, your path of least resistance is probably to just follow the Gatsby way when working in Gatsby.

## Netlify and environment variables

[Netlify](https://www.netlify.com/) provides the ability to add environment variables as part of its **Build & deploy** settings which gets picked up as part of the build processes.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/netlify-environment-variable.jpg)
_Adding an environment variable in Netlify_

Luckily, Netlify makes it easy to add whatever environment variable you'd like to the build process! To add one, you can simply navigate to the **Environment** section of your project's **Build & deploy** settings page and add a variable under **Environment variables.**

We'll walk you through this process a little later.

## Step 1: Creating a "Hello, world" website

For our walkthrough, we're going to set up a really basic example of a Gatsby website just for the purposes of testing this out.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/new-website-gatsby-starter-leaflet.jpg)
_New website with Gatsby Sass Starter_

Though this isn't really a common use case of environment variables, where normally you would use them for things like API keys and service configurations, this will give you a great idea of how it fundamentally works.

We're going to use this [Gatsby Sass Starter](https://github.com/colbyfayock/gatsby-starter-sass) I created which will give us a starting point and add "Hello, [Environment]" depending on where it's running.

To get started, let's create our local project by using the [Gatsby CLI](https://www.gatsbyjs.org/docs/gatsby-cli/). Navigate to where you'd like to store this project and run:

```shell
gatsby new my-env-project https://github.com/colbyfayock/gatsby-starter-sass

```

You can change `my-env-project` to whatever directory you'd like this project created in, but once you run this command, you'll now have a project in that new directory.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/new-gatsby-project-command-line.jpg)
_New Gatsby project in the terminal_

To get started, once inside that directory, run `yarn develop` to make changes locally or `yarn build` to compile your new site.

Once you're ready to go, you'll want to add this project to Github. If you're not familiar with how to do this, you can l[earn how to add an existing project to Github](https://help.github.com/en/github/importing-your-projects-to-github/adding-an-existing-project-to-github-using-the-command-line) here.

## Step 2: Creating a local environment variable with Gatsby

Our next step is to create a local environment and add a change that will let us see that it works.

To get started, let's first create a new file at the root of our project called `.env.development`. It might ask you if you really want to use the `.` prefix, make sure you say yes!

Inside that file, let's add:

```
# Inside .env.development
GATSBY_MY_ENVIRONMENT="Development"

```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/gatsby-development-environment-file.jpg)
_Creating an .env.development file_

Next, to make sure we don't forget to do this, let's also add this `.env.development` file to our `.gitignore` so we don't accidentally commit this to our git history. If you don't already have a `.gitignore` file, make sure you create it at the root of your project.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/adding-development-environment-file-gitignore.jpg)
_Adding .env.development to your .gitignore_

Finally, to check that this works, let's open `pages/index.js` and let's replace our `<h1>` tag's content with a "Hello, world!" variation:

```jsx
<h1>Hello, {process.env.GATSBY_MY_ENVIRONMENT}</h1>

```

And if we save that change and open it in our browser, we should see "Hello, Development"!

![Image](https://www.freecodecamp.org/news/content/images/2020/04/using-environment-variable-gatsby.jpg)
_Using an environment variable for your Gatsby site_

[Follow along with the commit!](https://github.com/colbyfayock/my-env-project/commit/e3e7000fbfab4cecac7739458034e70958e52211)

## Step 3: Deploying the website to Netlify

So we have our website created using a simple environment variable. Next we'll want to actually deploy that site to Netlify. If you haven't already, we'll need to [add our website to Github](https://help.github.com/en/github/importing-your-projects-to-github/adding-an-existing-project-to-github-using-the-command-line) or another Git provider. Make sure to have that set up before continuing on.

After creating an account and logging in to Netlify, let's click the **New site from Git** button the main dashboard, follow the instructions for connecting your Github or other Git provider to Netlify, and then find your new repository.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/adding-new-github-repository-netlify.jpg)
_Adding a new Github repository to Netlify_

Once you select your repository, you'll be asked to configure your build process. Luckily, Netlify can detect that we're using a Gatsby site and has it pre-filled for us. Unless you've added something special, keep the basic configuration to use `gatsby build` to build your project and `public/` for the output.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/configuring-netlify-build.jpg)
_Configuring Netlify build settings_

Now before we hit **Deploy**, there's one thing we want to add, and that's our environment variable!

Right above the **Deploy site** button there's an **Advanced** button. Click that and you'll see a new dropdown with an additional **New variable** button.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/configuring-environment-variable-netlify.jpg)
_Configuring an environment variable in the Netlify setup_

Click that **New variable** button, add our `GATSBY_MY_ENVIRONMENT` as a new variable and add `Production` as the value. And finally, hit **Deploy site**!

From here, you should be able to watch your website deploy and once finished, you'll see your new site with "Hello, Production"!

![Image](https://www.freecodecamp.org/news/content/images/2020/04/deployed-gatsby-site-with-environment-variable.jpg)
_Deployed Gatsby site using Netlify environment variable_

## Where can you add or update more variables in Netlify?

With our example, we only added one variable during the setup. But Netlify lets you add or update any other variables you'd like.

If you'd ever like to change that variable or add more, you can navigate to the **Environment** section of the **Build & deploy** settings, where you can edit and add any other variables in the **Environment variables** section.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/environment-variable-settings-netlify.jpg)
_Environment variables settings in Netlify_

## Looking to learn more?

Here are a few other things to help you get started with development fundamentals!

* [What is Gatsby and why it's time to get on the hype train?](https://www.colbyfayock.com/2019/09/what-is-gatsby-and-why-its-time-to-get-on-the-hype-train)
* [What is the JAMstack and how do I get started?](https://www.colbyfayock.com/2020/02/what-is-the-jamstack-and-how-do-i-get-started)
* [How to Become a Full Stack Web Developer in 2020](https://www.colbyfayock.com/2020/02/how-to-become-a-full-stack-web-developer-in-2020)
* [Put Down the Javascript - Learn HTML & CSS](https://www.colbyfayock.com/2019/08/put-down-the-javascript-learn-html-css)
* [Set Future You Up for Success with Good Coding Habits](https://www.colbyfayock.com/2020/04/set-future-you-up-for-success-with-good-coding-habits)

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
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">?️ Subscribe To My Youtube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;">✉️ Sign Up For My Newsletter</a>
    </li>
  </ul>
</div>

