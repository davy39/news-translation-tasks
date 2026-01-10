---
title: How to Deploy Multiple Repositories to Subfolders Under One Website with Netlify
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-07-13T14:57:25.000Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-multiple-repos-to-subfolders-under-one-website-netlify
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/pexels-xxss-is-back-777001.jpg
tags:
- name: documentation
  slug: documentation
- name: Netlify
  slug: netlify
- name: Next.js
  slug: nextjs
- name: React
  slug: reactjs
seo_title: null
seo_desc: 'By Abdulmalik Salawu

  Hi there! 👋 You''re probably here because you are trying to deal with hosting two
  separate websites or repositories under one website using Netlify.

  And maybe you''ve checked out the answers on the Netlify community page, but you
  ...'
---

By Abdulmalik Salawu

Hi there! 👋 You're probably here because you are trying to deal with hosting two separate websites or repositories under one website using Netlify.

And maybe you've checked out the answers on the Netlify community page, but you are still confused.

The same confusion and headache led me to write this tutorial so you don't have to struggle as much as I did.

It's tricky but it works: the solution to this problem is the `netlify.toml` or `_redirects file`.

Let's jump in.

I am working on a project with some colleagues, and we split up the tasks so that I'm working on the documentation.

<h2>Technologies We'll Use Here</h2>

* [Docusaurus](https://docusaurus.io/docs/) for shipping beautiful documentation sites in no time.
* Next.js/React.js for our main website

Let's get started and see how we can host the documentation. We dan do this in two ways:

1. Using a subdomain, docs.mainsite.dev
2. Using the main domain mainsite.dev and hosting the docs as a subdirectory on mainsite.dev/docs.

Based on what I have seen being implemented by other projects in their documentation, I wanted to host it as a subfolder via Netlify too. 

I figure it'd help our docs have that professional look.

If you will be hosting docusaurus as the subfolder too, you need to do some set up.

## Step 1 – Update the Base URL

Change the **baseUrl** in your docusaurus.config.js file to "**/docs/"** with the following code:

```javascript
  title: 'Your Docs Title',
  tagline: 'Your Docs Tagline',
  url: 'my-docs-site.netlify.app',
  baseUrl: "/docs/",
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: '/favicon.ico',
```

By changing your base URL to **/docs/**, it makes your website render exactly as **https://mainsite.dev/docs/**, which is the docs path.

If you were to set the **baseUrl** to "/" there will be error. This also means we don't have to deal with proxying our docs site.

## Step 2 – Update the routeBasePath

You'll also need to make sure that the documentation contents are served from your root domain by changing the **routeBasePath** to **'/'**. 

Just like you see in the snippet below:

```javascript
  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          routeBasePath: '/',
        },
      }),
    ],
  ],
```

This will help you activate the docs only mode on docusaurus. This way, your docs will be served from your root domain but with the path '/docs/' being the base path.

After that, your can run `npx docusaurus start` on your localhost to see if your docs site will build and render well without issues. 

If you have no issues, then you should see something like this:

![Image](https://www.freecodecamp.org/news/content/images/2022/07/docusaurus-run-localhost-1.jpg)
_Your docusaurus site should render like this on path '/docs/' being the base path._

To read more about the config for docusaurus docs only mode, you can read [this](https://docusaurus.io/docs/docs-introduction#docs-only-mode).

## Step 3 – Deploy to Netlify

Now it's time to deploy to your docs site to Netlify. If you don't already know how to do that, you can refer to this [guide](https://docusaurus.io/docs/deployment#deploying-to-netlify).

Once you are done deploying, your Netlify website URL should be available already like this: // my-docs-site.netlify.app.

## Step 4 – Proxying

Here comes the part where you will be doing the proxying.

You have already hosted your main website on Netlify and your docs site has been deployed to Netlify too.

Now you need to create a _netlify.toml_ file in the root of your project/repository of your main website, and add the following lines to it:

```markdown
[[redirects]]
from = "/docs/*"
to = "https://my-docs-site.netlify.app/:splat"
status = 200
force = false
```

The above rule makes sure that, whenever the /docs/ path is queried on your main site, your docs site loads up normally on your main-website.netlify.app/docs/ path.

Alternatively you can do this proxying via your docs site/repository. Just create a netlify.toml file in the root of your docs site/repository, and add the following lines to it:

```toml
[[redirects]]
from = "/*"
to = "https://main-website.netlify.app/docs/:splat"
status = 301
force = true
```

The above rule makes sure that whenever the /* path is queried on your docs site, it will load up normally on your main-website.netlify.app/docs/ path.

You will also notice that your docs site on the Netlify site is broken – but it works perfectly on your main site. 

Since it works and we have achieved our goals, then let it be 😁.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/docs-site-netlify-error.jpg)
_Broken docusaurus site for subfolder documentation_

**NOTE:** Never add the rules to your docs site and your main site at the same time, as this will cause a conflict of "TOO MANY REDIRECTS" errors.

So you either add the rules to your docs site or your main site, but not both.

## Let's Answer Some Questions

**Q:** Why would I choose to use the _netlify.toml_ file, and not the __redirects_ file?

Yeah, I first went for the easy option and tried the _redirects file too. But it wasn't that easy because you will have to always copy the __redirects_ file into your **build/** or **public/** folder while building your Netlify site.

This requires you to edit your Netlify build settings to something like this:

```txt
npm run build && cp _redirects public/
```

You can also achieve the proxying using the __redirects_ file. The rules will be in the following format for main-site:

```txt
/docs/* https://my-docs-site.netlify.app/:splat 200
```

and in this format for your docs site:

```txt
/* https://main-website.netlify.app/docs/:splat 301!
```

**Q:** Why would I choose to use Netlify URLs in all the proxying rules instead of our custom domain URL?

Well, the Netlify community advises that you use the Netlify URLs, since it is a more reliable way to do the proxying.

## Conclusion

Congratulations 🎉, glad you made it to the end of this guide. 

I believe you've learnt something new today.

It's time to go implement and make your project documentation look professional too by having it hosted in the subfolder of your main site. 👏.

You can also share this article, so that others can see it.

## Resources:

* [Netlify Rules Playground](https://play.netlify.com/redirects)
* [[Support Guide] Can I deploy multiple repositories in a single site?](https://answers.netlify.com/t/support-guide-can-i-deploy-multiple-repositories-in-a-single-site/179)   
  

