---
title: 'How to Create Your First Hugo Blog: a Practical Guide'
subtitle: ''
author: Flavio Copes
co_authors: []
series: null
date: '2020-01-08T08:44:58.000Z'
originalURL: https://freecodecamp.org/news/your-first-hugo-blog-a-practical-guide
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/Screen-Shot-2020-01-03-at-20.05.40.png
tags:
- name: blog
  slug: blog
- name: Hugo
  slug: hugo
- name: technical writing
  slug: technical-writing
seo_title: null
seo_desc: 'Hugo is a great tool to use if you want to start a blog.

  I use Hugo myself for my blog, flaviocopes.com, and I''ve been using it for more
  than two years. I have a few reasons for loving Hugo.

  First of all, it is simple, boring, flexible, and fast.

  The...'
---

Hugo is a great tool to use if you want to start a blog.

I use Hugo myself for my blog, [flaviocopes.com](https://flaviocopes.com/), and I've been using it for more than two years. I have a few reasons for loving Hugo.

First of all, it is **simple**, **boring**, **flexible**, and **fast**.

The main reason is that it is **simple**. There’s not much you have to learn to get started.

You write content in Markdown, a format that lets me use my favorite editor (Bear) to write posts.

Hugo is **boring**. Don’t get me wrong, this is a very positive thing. As a developer I am tempted to tweak things here and there all the time. There’s no fancy technology underlying Hugo. It’s built using Go, one of the languages I love the most, but that does not mean I want to dive into the internals of Hugo and change how it works.

And it does not surface any cool or next-generation stuff like many JavaScript frameworks tend to do.

Hence it is boring, which gives me a lot of time to do what is really useful when working on a blog: **writing content**. I focus on the content, not on the content container.

That said, Hugo is pretty darn **flexible**. I started my own blog with an open source theme, then changed it completely over time. Sometimes I want to do things in my website that are out of the scope of a simple blog, and Hugo allows me to create those things.

Finally, another reason I love Hugo is that it is **fast**. Why? First, it has Go at the core, which is known to be a very fast language. And in the Go ecosystem, there’s no concept of 100 megabytes dependencies. Things are made to be as fast as possible. Plus, Hugo does not need to do some of the fancy stuff that is needed when using fancy technology. This is a by-product of being boring.

Anyway, enough with words.

Hugo is amazing, especially if you are a developer and you’re willing to write in Markdown. Non-tech people might just refuse to use Markdown, and it’s perfectly understandable.

Also, you have to be prepared for a Git-centric workflow to make things really click.

This is the process for writing a blog: 

* write a post using Markdown, 
* then commit your changes to a Git repository, most commonly on GitHub, 
* and then some glue technology deploys the changes on the server that hosts the site.

## Hosting a Hugo website

A Hugo blog is completely **static**. This means you don’t need to host your own server, or use a special service for it.

Netlify, Now and GitHub Pages are three great places where you can host a Hugo blog, for free.

The only cost is the one you have to sustain for the domain name. I can’t stress enough the importance of having your own domain name. No `.github.io` or `.netlify.com` or `.now.sh` sites, please.

My own Hugo sites are hosted on Netlify.

## Choose a domain

Put your blog under your own domain. Pick one. Use your own name. And use `.com` or `.blog`. Don’t try to be clever by using a localized domain - for example, don’t use `.io`. `.com` just gives a better impression and it’s reusable for all your future projects, not just to host your blog. I picked that one.

Oh and if you have an old domain lying around, just use that. Why? The older your domain is, the better.

Note on subdomains: every subdomain, to Google, is a different website. So if your domain is `flaviocopes.com`, and you create your blog in `blog.flaviocopes.com`, then that’s a completely new website to Google, and it will have its own ranking separate from the main domain.

My suggestion is to avoid subdomains completely.

## Install Hugo

To install Hugo on macOS, from your terminal run

```bash
brew install hugo

```

_The `brew` command does not exist on your Mac? Check the [Homebrew guide](https://flaviocopes.com/homebrew/)_.

For Windows and Linux, check the [official installation guide](https://gohugo.io/getting-started/installing/).

## Create a Hugo site

Once Hugo is installed, you can create a Hugo site by running

```bash
hugo new site myblog

```

I suggest that you run this into a `www` folder in your Home directory, because the command will create a new `myblog` folder where you run it.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/hugo-cmd-tool.png)

## Pick a theme

Now before you can start you need to pick a theme. I wish Hugo included a default theme to make things straightforward, but it does not.

There are a lot of choices on [https://themes.gohugo.io](https://themes.gohugo.io/). My personal recommendation is to start with [https://themes.gohugo.io/ghostwriter/](https://themes.gohugo.io/ghostwriter/) and tweak it later.

I also recommend that you avoid the `git clone` workflow they suggest on that page. You’ll surely be tweaking the theme in the future, and I find it best to have a single repository for both content and theme. It simplifies deployment.

So, go to [https://github.com/jbub/ghostwriter/archive/master.zip](https://github.com/jbub/ghostwriter/archive/master.zip) to download the current version of the theme.

Then unpackage it in the `themes/ghostwriter` folder in your newly created Hugo website:

![Image](https://www.freecodecamp.org/news/content/images/2024/04/ghostwriter-theme.png)

Notice there is an `exampleSite` folder in the `themes/ghostwriter`. Open it, and open its `content` subfolder. In there, you can see the `page`, `post` and `project` subfolders.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/page-post-and-projects-subfolders.png)

Copy `page` and `post` in the `content` folder of the site:

![Image](https://www.freecodecamp.org/news/content/images/2024/04/copy-page-and-post-directories.png)

## The configuration

The sample data also provide a sample `config.toml` file in `themes/ghostwriter/exampleSite/config.toml`. This is the Hugo configuration file, which tells Hugo some details of the configuration without you having to hardcode information in the theme.

I recommend that you not copy that, because it has too many things, and instead use this:

```toml
baseurl = "/"
title = "My blog"
theme = "ghostwriter"

[Params]
    mainSections = ["post"]
    intro = true
    headline = "My headline"
    description = "My description"
    github = "https://github.com/XXX"
    twitter = "https://twitter.com/XXX"
    email = "XXX@example.com"
    opengraph = true
    shareTwitter = true
    dateFormat = "Mon, Jan 2, 2006"

[Permalinks]
    post = "/:filename/"

```

You can freely customize the information in this file later.

Now from the command line, run:

```bash
hugo serve

```

![Image](https://www.freecodecamp.org/news/content/images/2024/04/hugo-serve-output.png)

Open `http://localhost:1313` in your browser, and you should be able to see the site live!

![Image](https://www.freecodecamp.org/news/content/images/2024/04/live-site-localhost.png)

This is the site home page.

There is a list of posts that is taken from the `content/post` folder of your website:

![Image](https://www.freecodecamp.org/news/content/images/2024/04/content-post-samples.png)

Click the first, called “Creating a New Theme”:

![Image](https://www.freecodecamp.org/news/content/images/2024/04/creating-a-new-theme-post.png)

You can open the file `content/post/creating-a-new-theme.md` to change anything in the post.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/updating-markdown-of-post.png)

If you save, the website will automatically update with the new content.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/updated-post-live.png)

This is pretty awesome, right?

You can create a new post by creating a new `.md` file, prefixing it with anything you want. You can use incremental numbers, if you prefer. Or use a date.

If something doesn't look the way you want, you can open the `themes/ghostwriter/layouts` folder and tweak it.

The “post” template is defined in `themes/ghostwriter/layouts/post/single.html`:

![Image](https://www.freecodecamp.org/news/content/images/2024/04/post-template.png)

Hugo uses Go templates. The syntax can be pretty unfamiliar but the Hugo website does a very good job at explaining them in this [Go templates introduction](https://gohugo.io/templates/introduction/).

However, try to not look at customizing your template now.

If you want to tweak the colors, add a `<style>` tag with some CSS in the `themes/ghostwriter/layouts/partials/header.html`.

For example, make links black:

```html
<style>
.site-title a, .button-square {
    background: black;
}
a {
    color: black;
}
</style>

```

Focus on the content instead.

Remove the existing files, and write 2-3 posts to start with.

It’s too easy to get trapped in making things perfectly the way you want, but the important thing is the content.

And the cleaner your site is, the better for your readers.

Let me now write a little about deployment.

## Deploy the Hugo site to Netlify

I want to showcase how to deploy a Hugo site in 2 of the services I enjoy the most: Netlify and Now.

First, I’m going to create a GitHub repository to host the site.

I open GitHub Desktop, an app I use every day and that is part of my workflow. It’s the simplest way to use Git.

From the File menu, I pressed the “New Repository” option:

![Image](https://www.freecodecamp.org/news/content/images/2024/04/netlify-new-repository.png)

The same screen can be generated by simply dragging the `myblog` folder into the app.

I gave the `myblog` name to the repository, and picked the correct path for the repo.

The process automatically makes the first commit:

![Image](https://www.freecodecamp.org/news/content/images/2024/04/netlify-first-commit.png)

Now we can click the “Publish repository” button to push the repo to GitHub:

![Image](https://www.freecodecamp.org/news/content/images/2024/04/publish-repo.png)

You can keep the repo private, of course.

Once the repo is in GitHub:

![Image](https://www.freecodecamp.org/news/content/images/2024/04/private-repo-on-github.png)

we can move to Netlify.

From my Netlify dashboard I pressed the “New site from Git” button:

![Image](https://www.freecodecamp.org/news/content/images/2024/04/new-site-from-git.png)

I pressed GitHub, authorized Netlify to access my private repositories, then I picked the repo I just created:

![Image](https://www.freecodecamp.org/news/content/images/2024/04/access-to-private-repos.png)

Netlify automatically identified it as a Hugo repo, and entered the build command automatically:

![Image](https://www.freecodecamp.org/news/content/images/2024/04/netlify-enter-build-command.png)

Clicking “Deploy site” starts the deploy process:

![Image](https://www.freecodecamp.org/news/content/images/2024/04/netlify-deploy-site.png)

On a real site, I would set up a custom domain. Netlify has the option to purchase a domain through them, and it’s a very (VERY) straightforward process. I highly recommend it. The site can be live in just a few minutes after purchasing the domain.

A random `.netlify.com` subdomain is attached to the site, in this case `pedantic-engelbart-500c9a.netlify.com`, and HTTPS is automatically enabled.

We can therefore immediately see the site live:

![Image](https://www.freecodecamp.org/news/content/images/2024/04/preview-netlify-subdomain.png)

Now if you try to edit something in your local version, you just push the changes to GitHub, and Netlify will automatically update the site. You can see it building the site in the “Overview” panel of the site:

![Image](https://www.freecodecamp.org/news/content/images/2024/04/automatic-build.png)

To learn more about Netlify I recommend that you check out my [Netlify tutorial](https://flaviocopes.com/netlify/).

## Deploy the Hugo site to Zeit Now

Another awesome platform you can use for your Hugo blog is Zeit Now.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/zeit-now.png)

Once you sign up, from the dashboard you press the **New Project** button.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/zeit-now-new-project.png)

The first time you deploy from GitHub you have to first install the GitHub app by clicking “Install Now For GitHub”:

![Image](https://www.freecodecamp.org/news/content/images/2024/04/zeit-now-install-now-from-github.png)

This brings you to the GitHub page for the app, where you can authorize it for all your repos, or just for some:

![Image](https://www.freecodecamp.org/news/content/images/2024/04/zeit-now-authorize.png)

Once you get back, click the “New Project From GitHub” button:

![Image](https://www.freecodecamp.org/news/content/images/2024/04/zeit-now-new-project-from-github.png)

Select the project and click “Import”:

![Image](https://www.freecodecamp.org/news/content/images/2024/04/zeit-now-import.png)

In the meantime, go into the main folder of `mysite` and add a `package.json` file with this content:

```json
{
  "scripts": {
    "build": "hugo"
  }
}

```

This tells Now how to deploy the site.

When you get back to the dashboard, the new deploy should start soon, and you will see the site working live:

![Image](https://www.freecodecamp.org/news/content/images/2024/04/zeit-now-deployed.png)

![Image](https://www.freecodecamp.org/news/content/images/2024/04/zeit-now-live-site.png)

Note that in Now you have three URLs you can use to access the site:

* `myblog.flaviocopes.now.sh`
* `myblog-alpha-swart.now.sh`
* `myblog-git-master.flaviocopes.now.sh`

You can choose the one you prefer.

Plus, each deployment has its own URL, too. In this case I had `myblog-h8xks5jhn.now.sh` but it changes with every deployment.

And of course you can add your domain, too. Zeit has a great service to purchase your domain directly from them, available at [https://zeit.co/domains](https://zeit.co/domains).

And if you prefer working with the command line, the `now` command lets you purchase domains from there, as well.

I highly recommend that you check out my [Zeit Now tutorial](https://flaviocopes.com/zeit-now/) to learn more about this platform.

## Wrapping up

I hope this tutorial can give you a little guidance if you are planning to start a new blog. Hugo is my favorite platform, but it's not unique of course. Ghost (the platform powering freeCodeCamp) is great too, along with WordPress of course, and Gatsby.

Pick your favorite. In my opinion the platform does not matter as much as your content does. So, choose one and start writing!

