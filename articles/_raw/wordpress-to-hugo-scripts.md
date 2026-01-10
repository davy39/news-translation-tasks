---
title: From WordPress to Hugo – How I Migrated a 250+ Page Site and the Scripts I
  Used
subtitle: ''
author: Lane Wagner
co_authors: []
series: null
date: '2022-08-30T23:25:47.000Z'
originalURL: https://freecodecamp.org/news/wordpress-to-hugo-scripts
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/1__D5sbQUd4XwTy9yt67BCCA-1.jpeg
tags:
- name: Hugo
  slug: hugo
- name: Static Site Generators
  slug: static-site-generators
- name: WordPress
  slug: wordpress
seo_title: null
seo_desc: 'I recently decided to switch Boot.dev''s blog from WordPress to a static
  site generator.

  I decided on Hugo, partly because I’m a huge fan of the Go programming language,
  but also because it just seemed like the best option from a dev-experience perspe...'
---

I recently decided to switch [Boot.dev's](https://boot.dev) blog from WordPress to a static site generator.

I decided on [Hugo](https://gohugo.io/), partly because I’m a huge fan of the Go programming language, but also because it just seemed like the best option from a dev-experience perspective. 

Here’s why I decided to move away from WordPress:

* I wanted to write and store all my posts in Markdown.
* I wanted to version control all my posts in Git/Github.
* I wanted to be able to use ctrl+shift+f to find and edit the content on my blog.
* I wanted a less buggy way to do “global blocks”
* I didn’t want to spend hours fine-tuning performance. My posts are just text and images, so page speed scores should be 100 by default!
* I wanted to use straight CSS for styling, making it easier for my blog and app to have identical styling.
* I wanted to host the site for free

With all those goals in mind, Hugo was a perfect choice. I’ve been super happy since making the switch, but there were some hiccups along the way. 

WordPress takes care of some of the nuances of SEO-tuning for you, and if you forget to redo them yourself, you’ll end up sacrificing rankings.

## How to Export WordPress Posts as Markdown

Manually copying and pasting all of your posts out of the WordPress GUI into Markdown files could take a _very_ long time. Especially if you have hundreds of posts like I do. 

In order to speed up the process, I used [this Markdown plugin](https://wordpress.org/plugins/wp-gatsby-markdown-exporter/) to export all of my posts as markdown at once. It’s called “Gatsby Markdown Exporter”, but it works for Hugo just as well.

I’m not going to go over the basics of getting up and running with Hugo, as I’m going to assume you are already familiar with it. But if you’re not, you can read the [quick start guide here](https://gohugo.io/getting-started/quick-start/).

## How to Use Hugo’s Built-in SEO Templates

WordPress and its various SEO plugins take care of a lot of SEO-related hocus-pocus for you. So when you move to a static site generator you often have to do some of that stuff yourself.

As it turns out, Hugo has some turn-key solutions for most of this, so using the right [internal templates](https://gohugo.io/templates/internal/) can get you all the open-graph, schema, and Twitter meta tags out of the box.

For me, that meant simply adding these 3 lines to my `layouts/partials/header.html` file within the `<head>` tag:

```html
{{ template "_internal/opengraph.html" . }}
{{ template "_internal/twitter_cards.html" . }}
{{ template "_internal/schema.html" . }}
```

Now we'll get into the scripts I wrote to help me with this process.

## Script 1 — Checking for Broken Links

You can solve a lot of your WordPress woes by installing plugins for various tasks. Well, assuming those plugins don’t break your entire WP installation.

With Hugo, I just write little text-manipulation or HTTP scripts to do my bidding.

This first script is just a simple iterator that crawls the site and reports any broken links. You can see the [full source code here](https://github.com/bootdotdev/blog/blob/main/scripts/linkcheck/main.go). It's small edit of the script the Go team uses to check for broken links on the Go programming language's website.

## Script 2 — Minifying Images

When working with WordPress, you would typically upload a blog post image, and some SEO plugin would optimize that image’s size for you. 

In Hugo, no such optimizations are made for you. It simply serves the exact image you add to your “static” folder.

I wrote a little script to optimize my images. It does the following:

* Takes an input image of nearly any type (.png, .jpeg, .gif, etc).
* Converts it to the `.webp` format (a performant format).
* Shrinks the image to a max image size I've configured if it’s too large.

This script is written in Node.js and [the source code can be found here](https://github.com/bootdotdev/blog/blob/main/scripts/image-min.js).

## Script 3 — Managing Global Shortcodes

WordPress had a feature called “global blocks”. They're super useful for things like newsletter signup boxes that show up in the middle of your articles, but that you want to be able to update in a single place. 

In Hugo, you can use [shortcodes](https://gohugo.io/content-management/shortcodes/) to achieve a similar purpose.

Unfortunately, it’s the inserting and removing of the shortcodes _themselves_ that actually becomes tedious at scale. 

For example, let’s say I added my newsletter signup shortcode after the 5th paragraph in all my articles, but now I want it to come after the 7th paragraph. I have to go manually copy/paste the short code!

Well, not anymore. Again, this is the great thing about storing all your blog posts in a text format — we can script some simple solutions. I wrote two scripts, and their source code can be found here:

* [rmshorts](https://github.com/bootdotdev/blog/blob/main/scripts/rmshorts/main.go)
* [addshorts](https://github.com/bootdotdev/blog/blob/main/scripts/addshorts/main.go)

These two scripts allow me move my global blocks with ease. For example, to remove all instances of `myshortcode` from the blog:

```bash
rmshorts myshortcode
```

Then to add `myshortcode` as its own paragraph after the 2nd section of every blog post across the site:

```bash
addshorts myshortcode 2
```

This has been a huge time saver.

## Script 4 — Converting .docx to Markdown

Last but not least, I work with some non-technical writers. My writers aren’t used to writing Markdown. Google docs is their tool of choice. 

I have no problem with that, as I want them to be effective. My solution was to write a [little bash script](https://github.com/bootdotdev/blog/blob/main/scripts/docxmd.sh) that uses [pandoc](https://pandoc.org/) under the hood to convert the Google Docs to Markdown files.

## Wrapping Up

I hope some of these scripts are valuable to you, and I really can’t recommend enough making the switch to a static site generator. If you’re willing to put in a few hours to get a great working environment up and running for your blog it will save you a lot of time and money in the long run.

Remember, always automate the boring stuff!

